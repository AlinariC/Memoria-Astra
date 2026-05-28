#!/usr/bin/env python3
"""Render curated Cinderwake dialogue scripts with ElevenLabs.

This is intentionally script-driven instead of fully automatic speaker
guessing. Epic audiobook casting needs human-reviewable role assignments before
we spend credits on full chapters.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CAST = ROOT / "Fantasy Novel Series/production/audiobook-cast.json"
DEFAULT_KEY_FILE = Path.home() / "Documents/API-KEYS/elevenlabs-codex-cinderwake-studio-audiobook-2026-05-20.key"
DEFAULT_OUT_DIR = ROOT / "output/audiobooks/cinderwake"
TEXT_TO_DIALOGUE_ENDPOINT = "https://api.elevenlabs.io/v1/text-to-dialogue"
SAFE_DIALOGUE_CHARS = 1900
MAX_DIALOGUE_VOICES = 10


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "dialogue-render"


def require_tool(name: str) -> None:
    if shutil.which(name) is None:
        raise SystemExit(f"Required tool not found: {name}")


def run(cmd: list[str], *, quiet: bool = False) -> None:
    subprocess.run(
        cmd,
        check=True,
        stdout=subprocess.DEVNULL if quiet else None,
        stderr=subprocess.DEVNULL if quiet else None,
    )


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


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def with_delivery_tag(text: str, role: dict[str, Any], *, include_tags: bool) -> str:
    text = normalize_text(text)
    if not text:
        return ""
    if not include_tags:
        return text
    if text.startswith("["):
        return text
    tag = str(role.get("delivery_tag") or "").strip()
    return f"{tag} {text}".strip() if tag else text


def split_long_text(text: str, limit: int) -> list[str]:
    text = normalize_text(text)
    if len(text) <= limit:
        return [text]

    pieces: list[str] = []
    current = ""
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    for paragraph in paragraphs:
        if len(paragraph) > limit:
            sentences = re.split(r"(?<=[.!?])\s+", paragraph)
            for sentence in sentences:
                if len(sentence) > limit:
                    for offset in range(0, len(sentence), limit):
                        pieces.append(sentence[offset : offset + limit].strip())
                    continue
                if len(current) + len(sentence) + 1 <= limit:
                    current = f"{current} {sentence}".strip()
                else:
                    if current:
                        pieces.append(current)
                    current = sentence
            continue

        if len(current) + len(paragraph) + 2 <= limit:
            current = f"{current}\n\n{paragraph}".strip()
        else:
            if current:
                pieces.append(current)
            current = paragraph

    if current:
        pieces.append(current)
    return pieces


def prepared_segments(
    script: dict[str, Any],
    cast: dict[str, Any],
    limit: int,
    *,
    include_delivery_tags: bool,
) -> list[dict[str, str]]:
    roles = cast.get("roles", {})
    prepared: list[dict[str, str]] = []
    for raw in script.get("segments", []):
        role_key = raw.get("role")
        if role_key not in roles:
            raise SystemExit(f"Unknown role {role_key!r}; add it to {DEFAULT_CAST.name} or fix the script.")
        role = roles[role_key]
        tagged_text = with_delivery_tag(
            str(raw.get("text", "")),
            role,
            include_tags=include_delivery_tags,
        )
        for part in split_long_text(tagged_text, limit):
            prepared.append(
                {
                    "role": role_key,
                    "voice_id": str(raw.get("voice_id") or role["voice_id"]),
                    "voice_name": str(role.get("voice_name", "")),
                    "text": part,
                }
            )
    return prepared


def chunk_dialogue_segments(segments: list[dict[str, str]], limit: int) -> list[list[dict[str, str]]]:
    chunks: list[list[dict[str, str]]] = []
    current: list[dict[str, str]] = []
    current_chars = 0
    current_voices: set[str] = set()

    def flush() -> None:
        nonlocal current, current_chars, current_voices
        if current:
            chunks.append(current)
        current = []
        current_chars = 0
        current_voices = set()

    for segment in segments:
        length = len(segment["text"])
        next_voices = current_voices | {segment["voice_id"]}
        would_exceed_chars = current and current_chars + length > limit
        would_exceed_voices = current and len(next_voices) > MAX_DIALOGUE_VOICES
        if would_exceed_chars or would_exceed_voices:
            flush()
        current.append(segment)
        current_chars += length
        current_voices.add(segment["voice_id"])

    flush()
    return chunks


def render_dialogue_chunk(
    *,
    api_key: str,
    chunk: list[dict[str, str]],
    model_id: str,
    output_format: str,
    seed: int | None,
) -> tuple[bytes, dict[str, str]]:
    payload: dict[str, Any] = {
        "inputs": [{"text": item["text"], "voice_id": item["voice_id"]} for item in chunk],
        "model_id": model_id,
        "apply_text_normalization": "auto",
    }
    if seed is not None:
        payload["seed"] = seed

    url = f"{TEXT_TO_DIALOGUE_ENDPOINT}?{urllib.parse.urlencode({'output_format': output_format})}"
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "xi-api-key": api_key,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=240) as response:
            audio = response.read()
            headers = {
                "request_id": response.headers.get("request-id", ""),
                "history_item_id": response.headers.get("history-item-id", ""),
                "character_count": response.headers.get("x-character-count", ""),
            }
            return audio, headers
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"ElevenLabs request failed with HTTP {exc.code}: {body}") from exc


def concat_audio(inputs: list[Path], output: Path) -> None:
    require_tool("ffmpeg")
    if len(inputs) == 1:
        output.write_bytes(inputs[0].read_bytes())
        return

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".txt", delete=False) as list_file:
        for item in inputs:
            list_file.write(f"file '{item.resolve()}'\n")
        list_path = Path(list_file.name)
    try:
        run(
            [
                "ffmpeg",
                "-y",
                "-f",
                "concat",
                "-safe",
                "0",
                "-i",
                str(list_path),
                "-codec:a",
                "libmp3lame",
                "-b:a",
                "128k",
                str(output),
            ],
            quiet=True,
        )
    finally:
        list_path.unlink(missing_ok=True)


def render_script(args: argparse.Namespace) -> None:
    cast = read_json(Path(args.cast).resolve())
    script_path = Path(args.script).resolve()
    script = read_json(script_path)
    model_id = args.model_id or script.get("model_id", "eleven_v3")
    output_format = args.output_format or script.get("output_format", "mp3_44100_128")
    limit = int(args.max_chars)
    segments = prepared_segments(
        script,
        cast,
        limit,
        include_delivery_tags=args.include_delivery_tags,
    )
    chunks = chunk_dialogue_segments(segments, limit)

    print(f"script={script_path}")
    print(f"title={script.get('title', script_path.stem)}")
    print(f"model={model_id}")
    print(f"segments={len(segments)} chunks={len(chunks)} chars={sum(len(s['text']) for s in segments)}")
    for index, chunk in enumerate(chunks, start=1):
        voices = sorted({item["role"] for item in chunk})
        chars = sum(len(item["text"]) for item in chunk)
        print(f"chunk {index:02d}: chars={chars} roles={', '.join(voices)}")

    if args.dry_run:
        return

    api_key = read_api_key(Path(args.key_file).expanduser() if args.key_file else DEFAULT_KEY_FILE)
    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    title_slug = slugify(str(script.get("title") or script_path.stem))
    final_output = Path(args.output).resolve() if args.output else out_dir / f"{title_slug}.mp3"
    chunks_dir = out_dir / f"{title_slug}-chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)

    chunk_files: list[Path] = []
    manifest_chunks: list[dict[str, Any]] = []
    for index, chunk in enumerate(chunks, start=1):
        chunk_file = chunks_dir / f"{index:03d}.mp3"
        if not chunk_file.exists() or args.force:
            audio, headers = render_dialogue_chunk(
                api_key=api_key,
                chunk=chunk,
                model_id=model_id,
                output_format=output_format,
                seed=(args.seed + index - 1) if args.seed is not None else None,
            )
            chunk_file.write_bytes(audio)
            if args.pause > 0:
                time.sleep(args.pause)
        else:
            headers = {"request_id": "", "history_item_id": "", "character_count": ""}
        chunk_files.append(chunk_file)
        manifest_chunks.append(
            {
                "index": index,
                "file": str(chunk_file.relative_to(out_dir)),
                "characters": sum(len(item["text"]) for item in chunk),
                "roles": sorted({item["role"] for item in chunk}),
                "request_id": headers.get("request_id", ""),
                "history_item_id": headers.get("history_item_id", ""),
                "reported_character_count": headers.get("character_count", ""),
            }
        )

    concat_audio(chunk_files, final_output)
    manifest_path = final_output.with_suffix(".manifest.json")
    manifest_path.write_text(
        json.dumps(
            {
                "title": script.get("title", script_path.stem),
                "book": script.get("book"),
                "chapter": script.get("chapter"),
                "source": script.get("source"),
                "script": str(script_path.relative_to(ROOT) if script_path.is_relative_to(ROOT) else script_path),
                "cast": str(Path(args.cast).resolve().relative_to(ROOT)),
                "model_id": model_id,
                "output_format": output_format,
                "output": str(final_output.relative_to(ROOT) if final_output.is_relative_to(ROOT) else final_output),
                "chunks": manifest_chunks,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"output={final_output}")
    print(f"manifest={manifest_path}")


def list_cast(args: argparse.Namespace) -> None:
    cast = read_json(Path(args.cast).resolve())
    for role_key, role in cast.get("roles", {}).items():
        print(f"{role_key}\t{role.get('display_name')}\t{role.get('voice_name')}\t{role.get('voice_id')}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cast", default=str(DEFAULT_CAST), help="Path to audiobook-cast.json.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    cast_parser = subparsers.add_parser("list-cast", help="Print role to voice mappings.")
    cast_parser.set_defaults(func=list_cast)

    render_parser = subparsers.add_parser("render-script", help="Render a curated dialogue JSON script.")
    render_parser.add_argument("script", help="Path to a .dialogue.json script.")
    render_parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR), help="Output directory for audio and manifests.")
    render_parser.add_argument("--output", help="Exact final MP3 path. Defaults to a slug in --out-dir.")
    render_parser.add_argument("--key-file", help="ElevenLabs key file. Defaults to the local Documents/API-KEYS key.")
    render_parser.add_argument("--model-id", help="Override the model_id from the script.")
    render_parser.add_argument("--output-format", help="Override output_format from the script.")
    render_parser.add_argument("--max-chars", type=int, default=SAFE_DIALOGUE_CHARS, help="Maximum characters per Text to Dialogue request.")
    render_parser.add_argument("--seed", type=int, help="Optional deterministic seed base. Each chunk increments by one.")
    render_parser.add_argument("--pause", type=float, default=0.25, help="Delay between API requests.")
    render_parser.add_argument("--force", action="store_true", help="Regenerate existing chunk files.")
    render_parser.add_argument("--dry-run", action="store_true", help="Print chunk plan without calling ElevenLabs.")
    render_parser.add_argument(
        "--include-delivery-tags",
        action="store_true",
        help="Experimental: prepend role delivery tags to spoken text. Off by default because tags may be spoken.",
    )
    render_parser.set_defaults(func=render_script)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
