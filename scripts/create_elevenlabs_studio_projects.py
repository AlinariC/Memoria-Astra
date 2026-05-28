#!/usr/bin/env python3
"""Create ElevenLabs Studio projects for the Cinderwake audiobooks.

Studio is the long-form route for whole books. This script builds structured
chapter content with per-node voice IDs, uploads it to ElevenLabs Studio, and
can ask Studio to start conversion asynchronously.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

import render_cinderwake_audiobooks as renderer


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CAST = renderer.DEFAULT_CAST
DEFAULT_ARCS = renderer.DEFAULT_ARCS
DEFAULT_KEY_FILE = renderer.DEFAULT_KEY_FILE
DEFAULT_OUT_DIR = ROOT / "output/audiobooks/cinderwake/studio"
STUDIO_PROJECTS_ENDPOINT = "https://api.elevenlabs.io/v1/studio/projects"


def read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def read_api_key(key_file: Path | None) -> str:
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if api_key:
        return api_key
    if key_file and key_file.exists():
        return key_file.read_text(encoding="utf-8").strip()
    raise SystemExit("Set ELEVENLABS_API_KEY or pass --key-file with a valid ElevenLabs key.")


def multipart_body(fields: list[tuple[str, str]]) -> tuple[bytes, str]:
    boundary = f"----cinderwake-{int(time.time() * 1000)}"
    parts: list[bytes] = []
    for name, value in fields:
        parts.append(f"--{boundary}\r\n".encode("utf-8"))
        parts.append(f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode("utf-8"))
        parts.append(value.encode("utf-8"))
        parts.append(b"\r\n")
    parts.append(f"--{boundary}--\r\n".encode("utf-8"))
    return b"".join(parts), boundary


def request_json(
    url: str,
    *,
    api_key: str,
    method: str = "GET",
    json_payload: dict[str, Any] | None = None,
    multipart_fields: list[tuple[str, str]] | None = None,
    timeout: int = 240,
) -> dict[str, Any]:
    headers = {"xi-api-key": api_key}
    data: bytes | None = None
    if json_payload is not None:
        data = json.dumps(json_payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    if multipart_fields is not None:
        data, boundary = multipart_body(multipart_fields)
        headers["Content-Type"] = f"multipart/form-data; boundary={boundary}"

    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read()
            if not raw:
                return {}
            return json.loads(raw.decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"ElevenLabs Studio request failed with HTTP {exc.code}: {body}") from exc


def chapter_paths(book_slug: str) -> list[Path]:
    book = renderer.BOOKS[book_slug]
    chapters_dir = Path(book["dir"]) / "chapters"
    return sorted(chapters_dir.glob("chapter-*.md"), key=renderer.chapter_index_from_path)


def build_studio_content(
    *,
    book_slug: str,
    cast: dict[str, Any],
    arcs: dict[str, Any],
    max_chars: int,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    book = renderer.BOOKS[book_slug]
    book_number = int(book["number"])
    roles = cast.get("roles", {})
    content: list[dict[str, Any]] = []
    stats: dict[str, Any] = {
        "chapters": [],
        "role_characters": {},
        "dialogue": {},
        "total_characters": 0,
        "total_nodes": 0,
    }
    role_chars: dict[str, int] = {}
    dialogue_stats: dict[str, int] = {}

    for path in chapter_paths(book_slug):
        chapter_index = renderer.chapter_index_from_path(path)
        parsed, parse_stats = renderer.parse_chapter(path, book_number=book_number)
        units = renderer.build_render_units(
            parsed,
            arcs=arcs,
            book_number=book_number,
            chapter_index=chapter_index,
            max_chars=max_chars,
        )
        title = renderer.chapter_title(path)
        blocks: list[dict[str, Any]] = []
        for unit in units:
            role = unit.role if unit.role in roles else "narrator"
            role_plan = roles[role]
            sub_type = "p"
            blocks.append(
                {
                    "sub_type": sub_type,
                    "nodes": [
                        {
                            "type": "tts_node",
                            "voice_id": role_plan["voice_id"],
                            "text": unit.text,
                        }
                    ],
                }
            )
            role_chars[role] = role_chars.get(role, 0) + len(unit.text)
            stats["total_characters"] += len(unit.text)
            stats["total_nodes"] += 1

        for key, value in parse_stats.items():
            if key.startswith("dialogue:"):
                dialogue_stats[key] = dialogue_stats.get(key, 0) + int(value)

        content.append({"name": title, "blocks": blocks})
        stats["chapters"].append(
            {
                "index": chapter_index,
                "title": title,
                "source": str(path.relative_to(ROOT)),
                "nodes": len(units),
                "characters": sum(len(unit.text) for unit in units),
                "parse_stats": dict(parse_stats),
            }
        )

    stats["role_characters"] = role_chars
    stats["dialogue"] = dialogue_stats
    return content, stats


def voice_settings_for_book(
    *,
    book_slug: str,
    cast: dict[str, Any],
    arcs: dict[str, Any],
) -> list[dict[str, Any]]:
    book = renderer.BOOKS[book_slug]
    book_number = int(book["number"])
    midpoint = len(chapter_paths(book_slug)) // 2 or 1
    settings_by_voice: dict[str, dict[str, Any]] = {}
    for role_key, role in cast.get("roles", {}).items():
        stage, settings = renderer.arc_for_role(arcs, role_key, book_number=book_number, chapter_index=midpoint)
        voice_id = role["voice_id"]
        if voice_id in settings_by_voice:
            continue
        payload = {
            "voice_id": voice_id,
            "stability": settings.get("stability", 0.5),
            "similarity_boost": settings.get("similarity_boost", 0.78),
            "style": settings.get("style", 0.35),
            "speed": settings.get("speed", 1.0),
            "use_speaker_boost": settings.get("use_speaker_boost", True),
            "stage": stage,
        }
        settings_by_voice[voice_id] = payload
    return list(settings_by_voice.values())


def create_project(args: argparse.Namespace) -> None:
    cast = read_json(Path(args.cast).resolve())
    arcs = read_json(Path(args.arcs).resolve())
    api_key = read_api_key(Path(args.key_file).expanduser() if args.key_file else DEFAULT_KEY_FILE)
    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    book = renderer.BOOKS[args.book]
    content, stats = build_studio_content(book_slug=args.book, cast=cast, arcs=arcs, max_chars=args.max_chars)
    voice_settings = voice_settings_for_book(book_slug=args.book, cast=cast, arcs=arcs)
    content_path = out_dir / f"{args.book}-studio-content.json"
    stats_path = out_dir / f"{args.book}-studio-stats.json"
    content_path.write_text(json.dumps(content, indent=2), encoding="utf-8")
    stats_path.write_text(json.dumps(stats, indent=2), encoding="utf-8")

    print(f"book={args.book}")
    print(f"title={book['title']}")
    print(f"chapters={len(content)} nodes={stats['total_nodes']} chars={stats['total_characters']}")
    print(f"content={content_path}")
    print(f"stats={stats_path}")
    if args.dry_run:
        return

    fields: list[tuple[str, str]] = [
        ("name", f"Cinderwake {book['number']} - {book['title']}"),
        ("title", str(book["title"])),
        ("author", "Alinari Campbell"),
        ("description", "Role-aware AI audiobook production project for The Cinderwake Trilogy."),
        ("default_title_voice_id", cast["roles"]["narrator"]["voice_id"]),
        ("default_paragraph_voice_id", cast["roles"]["narrator"]["voice_id"]),
        ("default_model_id", args.model_id),
        ("from_content_json", json.dumps(content)),
        ("quality_preset", args.quality_preset),
        ("volume_normalization", "true"),
        ("apply_text_normalization", "auto"),
        ("language", "en"),
        ("content_type", "Novel"),
        ("target_audience", "adult"),
        ("fiction", "fiction"),
        ("auto_convert", "true" if args.auto_convert else "false"),
    ]
    for item in voice_settings:
        stage = item.pop("stage", None)
        fields.append(("voice_settings", json.dumps(item)))
        item["stage"] = stage

    response = request_json(
        STUDIO_PROJECTS_ENDPOINT,
        api_key=api_key,
        method="POST",
        multipart_fields=fields,
        timeout=args.timeout,
    )
    project = response.get("project", response)
    project_id = project.get("project_id")
    project_path = out_dir / f"{args.book}-studio-project.json"
    project_path.write_text(
        json.dumps(
            {
                "book": args.book,
                "title": book["title"],
                "project_id": project_id,
                "auto_convert": args.auto_convert,
                "model_id": args.model_id,
                "quality_preset": args.quality_preset,
                "project": project,
                "content_file": str(content_path.relative_to(ROOT)),
                "stats_file": str(stats_path.relative_to(ROOT)),
                "voice_settings": voice_settings,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"project_id={project_id}")
    print(f"project={project_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("book", choices=sorted(renderer.BOOKS), help="Book slug to create as a Studio project.")
    parser.add_argument("--cast", default=str(DEFAULT_CAST), help="Path to audiobook-cast.json.")
    parser.add_argument("--arcs", default=str(DEFAULT_ARCS), help="Path to audiobook-voice-arcs.json.")
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR), help="Output directory for Studio manifests.")
    parser.add_argument("--key-file", help="ElevenLabs API key file.")
    parser.add_argument("--model-id", default="eleven_v3", help="Studio default model.")
    parser.add_argument("--quality-preset", default="standard", choices=("standard", "high", "ultra", "ultra_lossless"))
    parser.add_argument("--max-chars", type=int, default=4000, help="Maximum characters per Studio tts_node.")
    parser.add_argument("--timeout", type=int, default=600, help="Upload timeout in seconds.")
    parser.add_argument("--auto-convert", action=argparse.BooleanOptionalAction, default=True, help="Ask Studio to start conversion after upload.")
    parser.add_argument("--dry-run", action="store_true", help="Build local content JSON without creating a Studio project.")
    args = parser.parse_args()
    create_project(args)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
