#!/usr/bin/env python3
"""Render full Cinderwake audiobook chapters with role-aware ElevenLabs TTS.

The renderer keeps performance notes out of the spoken payload. It uses those
notes only to choose voices and stage-specific voice settings while the actual
API text remains manuscript text.
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
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CAST = ROOT / "Fantasy Novel Series/production/audiobook-cast.json"
DEFAULT_ARCS = ROOT / "Fantasy Novel Series/production/audiobook-voice-arcs.json"
DEFAULT_KEY_FILE = Path.home() / "Documents/API-KEYS/elevenlabs-codex-cinderwake-studio-audiobook-2026-05-20.key"
DEFAULT_OUT_DIR = ROOT / "output/audiobooks/cinderwake/full"
TEXT_TO_SPEECH_ENDPOINT = "https://api.elevenlabs.io/v1/text-to-speech"
TEXT_TO_DIALOGUE_ENDPOINT = "https://api.elevenlabs.io/v1/text-to-dialogue"
DEFAULT_MODEL = "eleven_v3"
DEFAULT_OUTPUT_FORMAT = "mp3_44100_128"
DEFAULT_MAX_CHARS = 4500
DEFAULT_DIALOGUE_MAX_CHARS = 1850
MAX_DIALOGUE_VOICES = 10

BOOKS = {
    "book-01-the-ash-beneath-the-crown": {
        "number": 1,
        "title": "The Ash Beneath the Crown",
        "dir": ROOT / "Fantasy Novel Series/output/book-01-the-ash-beneath-the-crown",
    },
    "book-02-the-moon-below-the-world": {
        "number": 2,
        "title": "The Moon Below the World",
        "dir": ROOT / "Fantasy Novel Series/output/book-02-the-moon-below-the-world",
    },
    "book-03-the-dragon-that-dreamed-death": {
        "number": 3,
        "title": "The Dragon That Dreamed Death",
        "dir": ROOT / "Fantasy Novel Series/output/book-03-the-dragon-that-dreamed-death",
    },
}

DIALOGUE_VERBS = (
    "said|asked|answered|replied|called|shouted|whispered|muttered|snapped|"
    "continued|breathed|told|warned|hissed|growled|said softly|said quietly|"
    "said through|said with|said after|said before|cried|laughed|gasped|"
    "added|finished|began|objected|declared|ordered|insisted|admitted|"
    "repeated|corrected|cut in|interrupted"
)

ROLE_GENDER = {
    "mara": "she",
    "joryn": "he",
    "caldus": "he",
    "ilyr": "he",
    "saelith": "she",
    "tavi": "she",
    "kesh": "he",
    "brakka": "she",
    "arveth": "he",
    "vorrakai": "it",
    "mordane": "he",
    "sedge": "he",
    "general_male": "he",
    "general_female": "she",
}

ROLE_ALIASES = {
    "mara": ["Mara Venn", "Mara", "cinder-singer", "ash-runner", "vent-girl"],
    "joryn": ["Joryn Venn", "Joryn"],
    "caldus": ["Sir Caldus Renn", "Caldus Renn", "Sir Caldus", "Caldus", "scraped-crest"],
    "ilyr": ["Ilyr Noct-Vey", "Ilyr"],
    "saelith": ["Saelith Dawnmere", "Saelith"],
    "tavi": ["Tavi Quen", "Tavira Quen", "Tavi", "Tavira"],
    "kesh": ["Kesh of the Kavik Road", "Kavik Kesh", "Kesh"],
    "brakka": ["Brakka of the Third Arch", "Brakka"],
    "arveth": ["Arveth the Named", "Arveth"],
    "vorrakai": ["Vorrakai", "cinder voice", "Cinder Voice", "dragon-moon", "first dragon"],
    "mordane": ["Lord Cael Mordane", "Cael Mordane", "Lord Mordane", "Mordane"],
    "sedge": ["Foreman Sedge", "Sedge"],
    "general_female": [
        "Dilla",
        "Ness",
        "Rella",
        "Fenna",
        "Bessa",
        "Veyanna",
        "Liora",
        "Aneth",
        "Vaura",
        "Maelin",
        "Sava",
        "Rikka",
        "Veyrasha",
        "Othrava",
        "Elianth",
        "Lora",
        "Nera",
        "Vessa",
        "Brenna",
    ],
    "general_male": [
        "Harl",
        "Barren",
        "Pell",
        "Tollen",
        "Darron",
        "Edrin",
        "Othel",
        "Oren",
        "Lenn",
        "Durn",
        "Morn",
        "Eshkarun",
        "Rhyssara",
        "Varrik",
        "Thom",
        "Tovin",
        "Regent Rook",
        "Rook",
        "Captain Teren",
    ],
}


@dataclass
class SpeechUnit:
    role: str
    text: str
    source: str
    stage: str = "default"
    voice_settings: dict[str, Any] | None = None


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "chapter"


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


def clean_markdown_for_speech(text: str) -> str:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)
    text = text.replace("*", "")
    text = text.replace("_", "")
    text = re.sub(r"\n-{3,}\n?", "\n", text)
    return normalize_text(text)


def alias_pairs() -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for role, aliases in ROLE_ALIASES.items():
        for alias in aliases:
            pairs.append((alias, role))
    return sorted(pairs, key=lambda item: len(item[0]), reverse=True)


ALIASES = alias_pairs()


def find_last_role_mention(text: str) -> str | None:
    last_role: str | None = None
    last_index = -1
    for alias, role in ALIASES:
        for match in re.finditer(rf"\b{re.escape(alias)}\b", text, flags=re.IGNORECASE):
            if match.start() > last_index:
                last_index = match.start()
                last_role = role
    return last_role


def alias_attribution_role(text: str) -> str | None:
    for alias, role in ALIASES:
        escaped = re.escape(alias)
        patterns = [
            rf"\b{escaped}\b\s+(?:{DIALOGUE_VERBS})\b",
            rf"\b(?:{DIALOGUE_VERBS})\s+\b{escaped}\b",
            rf"\b{escaped}\b\s*,\s*(?:who\s+)?(?:{DIALOGUE_VERBS})\b",
        ]
        for pattern in patterns:
            if re.search(pattern, text, flags=re.IGNORECASE):
                return role
    return None


def pronoun_attribution_role(text: str, focus_role: str | None, last_speaker: str | None) -> str | None:
    match = re.search(rf"\b(she|he|they|it)\b\s+(?:{DIALOGUE_VERBS})\b", text, flags=re.IGNORECASE)
    if not match:
        return None
    pronoun = match.group(1).lower()
    candidates = [focus_role, last_speaker]
    for candidate in candidates:
        if not candidate:
            continue
        gender = ROLE_GENDER.get(candidate)
        if pronoun == "they" or pronoun == gender:
            return candidate
    return None


def alternate_speaker(recent_speakers: list[str]) -> str | None:
    if len(recent_speakers) < 2:
        return None
    return recent_speakers[-2]


def infer_speaker(
    *,
    prefix: str,
    suffix: str,
    focus_role: str | None,
    last_speaker: str | None,
    recent_speakers: list[str],
    quote_only: bool,
) -> tuple[str, str]:
    window = f"{prefix[-260:]} {suffix[:260]}"
    role = alias_attribution_role(window)
    if role:
        return role, "alias"

    role = pronoun_attribution_role(window, focus_role, last_speaker)
    if role:
        return role, "pronoun"

    if quote_only:
        role = alternate_speaker(recent_speakers)
        if role:
            return role, "alternating"

    return "narrator", "unknown"


def add_recent_speaker(recent_speakers: list[str], role: str) -> None:
    if role == "narrator":
        return
    if recent_speakers and recent_speakers[-1] == role:
        return
    recent_speakers.append(role)
    del recent_speakers[:-4]


def chapter_index_from_path(path: Path) -> int:
    match = re.search(r"chapter-(\d+)-", path.name)
    return int(match.group(1)) if match else 0


def parse_chapter(path: Path, *, book_number: int) -> tuple[list[SpeechUnit], Counter[str]]:
    raw = path.read_text(encoding="utf-8")
    text = clean_markdown_for_speech(raw)
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    stats: Counter[str] = Counter()
    units: list[SpeechUnit] = []
    focus_role: str | None = "mara"
    last_speaker: str | None = None
    recent_speakers: list[str] = []

    def append_unit(role: str, value: str, source: str) -> None:
        value = normalize_text(value)
        if not value:
            return
        units.append(SpeechUnit(role=role, text=value, source=source))
        stats[f"role:{role}"] += len(value)

    for paragraph in paragraphs:
        parts = re.split(r'(".*?")', paragraph)
        has_quote = any(part.startswith('"') and part.endswith('"') for part in parts)
        if not has_quote:
            append_unit("narrator", paragraph, "narration")
            focus_role = find_last_role_mention(paragraph) or focus_role
            continue

        quote_count = sum(1 for part in parts if part.startswith('"') and part.endswith('"'))
        quote_only = quote_count == 1 and normalize_text("".join(part for part in parts if not (part.startswith('"') and part.endswith('"')))) == ""
        for i, part in enumerate(parts):
            if not part:
                continue
            if part.startswith('"') and part.endswith('"'):
                spoken = normalize_text(part[1:-1])
                prefix = "".join(parts[:i])
                suffix = "".join(parts[i + 1 :])
                role, method = infer_speaker(
                    prefix=prefix,
                    suffix=suffix,
                    focus_role=focus_role,
                    last_speaker=last_speaker,
                    recent_speakers=recent_speakers,
                    quote_only=quote_only,
                )
                append_unit(role, spoken, f"dialogue:{method}")
                stats[f"dialogue:{method}"] += 1
                if role != "narrator":
                    last_speaker = role
                    focus_role = role
                    add_recent_speaker(recent_speakers, role)
                continue

            append_unit("narrator", part, "narration")
            focus_role = find_last_role_mention(part) or focus_role

    return units, stats


def split_text(text: str, max_chars: int) -> list[str]:
    text = normalize_text(text)
    if len(text) <= max_chars:
        return [text]

    chunks: list[str] = []
    current = ""
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    for paragraph in paragraphs:
        if len(paragraph) > max_chars:
            sentences = re.split(r"(?<=[.!?])\s+", paragraph)
            for sentence in sentences:
                if len(sentence) > max_chars:
                    for offset in range(0, len(sentence), max_chars):
                        chunks.append(sentence[offset : offset + max_chars].strip())
                    continue
                if len(current) + len(sentence) + 1 <= max_chars:
                    current = f"{current} {sentence}".strip()
                else:
                    if current:
                        chunks.append(current)
                    current = sentence
            continue

        if len(current) + len(paragraph) + 2 <= max_chars:
            current = f"{current}\n\n{paragraph}".strip()
        else:
            if current:
                chunks.append(current)
            current = paragraph

    if current:
        chunks.append(current)
    return chunks


def arc_for_role(arcs: dict[str, Any], role: str, *, book_number: int, chapter_index: int) -> tuple[str, dict[str, Any]]:
    settings = dict(arcs.get("default_voice_settings", {}))
    stage = "default"
    for candidate in arcs.get("role_arcs", {}).get(role, []):
        if candidate.get("book") != book_number:
            continue
        if int(candidate.get("chapter_min", 1)) <= chapter_index <= int(candidate.get("chapter_max", 999)):
            stage = str(candidate.get("stage", stage))
            settings.update(candidate.get("voice_settings", {}))
            break
    return stage, settings


def build_render_units(
    units: list[SpeechUnit],
    *,
    arcs: dict[str, Any],
    book_number: int,
    chapter_index: int,
    max_chars: int,
) -> list[SpeechUnit]:
    render_units: list[SpeechUnit] = []

    def push(role: str, text: str, source: str) -> None:
        stage, settings = arc_for_role(arcs, role, book_number=book_number, chapter_index=chapter_index)
        for part in split_text(text, max_chars):
            render_units.append(
                SpeechUnit(
                    role=role,
                    text=part,
                    source=source,
                    stage=stage,
                    voice_settings=settings,
                )
            )

    current_role: str | None = None
    current_source = ""
    current_text = ""
    for unit in units:
        separator = "\n\n" if unit.source == "narration" else " "
        if current_role == unit.role and len(current_text) + len(unit.text) + len(separator) <= max_chars:
            current_text = f"{current_text}{separator}{unit.text}".strip()
            current_source = f"{current_source}+{unit.source}" if current_source else unit.source
        else:
            if current_role and current_text:
                push(current_role, current_text, current_source)
            current_role = unit.role
            current_text = unit.text
            current_source = unit.source

    if current_role and current_text:
        push(current_role, current_text, current_source)

    return render_units


def render_tts_chunk(
    *,
    api_key: str,
    text: str,
    voice_id: str,
    model_id: str,
    output_format: str,
    voice_settings: dict[str, Any] | None,
    seed: int | None,
    previous_text: str | None,
    next_text: str | None,
) -> tuple[bytes, dict[str, str]]:
    payload: dict[str, Any] = {
        "text": text,
        "model_id": model_id,
        "apply_text_normalization": "auto",
    }
    if voice_settings:
        payload["voice_settings"] = voice_settings
    if seed is not None:
        payload["seed"] = seed
    supports_context_text = model_id != "eleven_v3"
    if previous_text and supports_context_text:
        payload["previous_text"] = previous_text[-900:]
    if next_text and supports_context_text:
        payload["next_text"] = next_text[:900]

    query = urllib.parse.urlencode({"output_format": output_format})
    request = urllib.request.Request(
        f"{TEXT_TO_SPEECH_ENDPOINT}/{urllib.parse.quote(voice_id)}?{query}",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "xi-api-key": api_key,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=240) as response:
            return response.read(), {
                "request_id": response.headers.get("request-id", ""),
                "history_item_id": response.headers.get("history-item-id", ""),
                "character_count": response.headers.get("x-character-count", ""),
            }
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        if voice_settings and exc.code == 422:
            return render_tts_chunk(
                api_key=api_key,
                text=text,
                voice_id=voice_id,
                model_id=model_id,
                output_format=output_format,
                voice_settings=None,
                seed=seed,
                previous_text=previous_text,
                next_text=next_text,
            )
        raise RuntimeError(f"ElevenLabs TTS failed with HTTP {exc.code}: {body}") from exc


def chunk_dialogue_units(
    units: list[SpeechUnit],
    *,
    roles: dict[str, Any],
    max_chars: int,
) -> list[list[SpeechUnit]]:
    chunks: list[list[SpeechUnit]] = []
    current: list[SpeechUnit] = []
    current_chars = 0
    current_voices: set[str] = set()

    def flush() -> None:
        nonlocal current, current_chars, current_voices
        if current:
            chunks.append(current)
        current = []
        current_chars = 0
        current_voices = set()

    for unit in units:
        role = unit.role if unit.role in roles else "narrator"
        voice_id = str(roles[role]["voice_id"])
        unit_chars = len(unit.text)
        unit_voices = current_voices | {voice_id}
        if current and (current_chars + unit_chars > max_chars or len(unit_voices) > MAX_DIALOGUE_VOICES):
            flush()
        current.append(unit)
        current_chars += unit_chars
        current_voices.add(voice_id)

    flush()
    return chunks


def render_dialogue_chunk(
    *,
    api_key: str,
    units: list[SpeechUnit],
    roles: dict[str, Any],
    model_id: str,
    output_format: str,
    seed: int | None,
) -> tuple[bytes, dict[str, str]]:
    settings = dialogue_settings_for_units(units)
    payload: dict[str, Any] = {
        "inputs": [
            {
                "text": unit.text,
                "voice_id": str(roles[unit.role if unit.role in roles else "narrator"]["voice_id"]),
            }
            for unit in units
        ],
        "model_id": model_id,
        "apply_text_normalization": "auto",
    }
    if settings:
        payload["settings"] = settings
    if seed is not None:
        payload["seed"] = seed

    query = urllib.parse.urlencode({"output_format": output_format})
    request = urllib.request.Request(
        f"{TEXT_TO_DIALOGUE_ENDPOINT}?{query}",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "xi-api-key": api_key,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=240) as response:
            return response.read(), {
                "request_id": response.headers.get("request-id", ""),
                "history_item_id": response.headers.get("history-item-id", ""),
                "character_count": response.headers.get("x-character-count", ""),
            }
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"ElevenLabs dialogue failed with HTTP {exc.code}: {body}") from exc


def dialogue_settings_for_units(units: list[SpeechUnit]) -> dict[str, Any] | None:
    weighted_stability = 0.0
    total_weight = 0
    stabilities: list[float] = []
    for unit in units:
        settings = unit.voice_settings or {}
        stability = settings.get("stability")
        if not isinstance(stability, int | float):
            continue
        clamped = max(0.0, min(1.0, float(stability)))
        weight = max(1, len(unit.text))
        weighted_stability += clamped * weight
        total_weight += weight
        stabilities.append(clamped)

    if not stabilities or total_weight <= 0:
        return None

    average = weighted_stability / total_weight
    most_expressive = min(stabilities)
    stability = (average * 0.7) + (most_expressive * 0.3)
    return {"stability": round(max(0.0, min(1.0, stability)), 3)}


def make_silence(path: Path, seconds: float) -> None:
    require_tool("ffmpeg")
    if path.exists():
        return
    run(
        [
            "ffmpeg",
            "-y",
            "-f",
            "lavfi",
            "-i",
            "anullsrc=r=44100:cl=mono",
            "-t",
            f"{seconds:.2f}",
            "-codec:a",
            "libmp3lame",
            "-b:a",
            "128k",
            str(path),
        ],
        quiet=True,
    )


def concat_audio(inputs: list[Path], output: Path, *, codec: str = "libmp3lame") -> None:
    require_tool("ffmpeg")
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".txt", delete=False) as list_file:
        for item in inputs:
            list_file.write(f"file '{item.resolve()}'\n")
        list_path = Path(list_file.name)
    try:
        cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(list_path)]
        if codec == "aac":
            cmd += ["-c:a", "aac", "-b:a", "128k"]
        else:
            cmd += ["-c:a", "libmp3lame", "-b:a", "128k"]
        cmd.append(str(output))
        run(cmd, quiet=True)
    finally:
        list_path.unlink(missing_ok=True)


def duration_ms(path: Path) -> int:
    require_tool("ffprobe")
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return int(float(result.stdout.strip()) * 1000)


def write_chapter_metadata(master_input: Path, master_output: Path, title: str, chapter_files: list[tuple[str, Path]]) -> None:
    start = 0
    lines = [
        ";FFMETADATA1",
        f"title={title}",
        "artist=Alinari Campbell",
        "album=The Cinderwake Trilogy",
        "genre=Audiobook",
    ]
    for chapter_title, chapter_file in chapter_files:
        length = duration_ms(chapter_file)
        end = start + length
        safe_title = chapter_title.replace("=", "-")
        lines += [
            "[CHAPTER]",
            "TIMEBASE=1/1000",
            f"START={start}",
            f"END={end}",
            f"title={safe_title}",
        ]
        start = end + 2500

    metadata_file = master_output.with_suffix(".ffmetadata")
    metadata_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(master_input),
            "-i",
            str(metadata_file),
            "-map_metadata",
            "1",
            "-codec",
            "copy",
            str(master_output),
        ],
        quiet=True,
    )


def chapter_title(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^##\s+(.+)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else path.stem


def render_book(args: argparse.Namespace) -> None:
    require_tool("ffmpeg")
    require_tool("ffprobe")
    book = BOOKS[args.book]
    cast = read_json(Path(args.cast).resolve())
    arcs = read_json(Path(args.arcs).resolve())
    roles = cast.get("roles", {})
    book_dir = Path(book["dir"])
    chapters_dir = book_dir / "chapters"
    chapter_paths = sorted(chapters_dir.glob("chapter-*.md"), key=chapter_index_from_path)
    if args.start_chapter:
        chapter_paths = [path for path in chapter_paths if chapter_index_from_path(path) >= args.start_chapter]
    if args.end_chapter:
        chapter_paths = [path for path in chapter_paths if chapter_index_from_path(path) <= args.end_chapter]
    if args.limit_chapters:
        chapter_paths = chapter_paths[: args.limit_chapters]
    if not chapter_paths:
        raise SystemExit("No chapters matched the selected range.")

    book_number = int(book["number"])
    out_dir = Path(args.out_dir).resolve() / args.book
    chunks_root = out_dir / "chunks"
    chapters_out = out_dir / "chapters"
    master_dir = out_dir / "master"
    for directory in (chunks_root, chapters_out, master_dir):
        directory.mkdir(parents=True, exist_ok=True)

    dry_stats: Counter[str] = Counter()
    chapter_plans: list[dict[str, Any]] = []
    for path in chapter_paths:
        chapter_index = chapter_index_from_path(path)
        parsed, stats = parse_chapter(path, book_number=book_number)
        unit_max_chars = args.max_chars if args.engine == "tts" else min(args.max_chars, args.dialogue_max_chars)
        render_units = build_render_units(
            parsed,
            arcs=arcs,
            book_number=book_number,
            chapter_index=chapter_index,
            max_chars=unit_max_chars,
        )
        dry_stats.update(stats)
        chapter_plans.append(
            {
                "path": path,
                "chapter_index": chapter_index,
                "title": chapter_title(path),
                "render_units": render_units,
                "stats": stats,
            }
        )

    total_chars = sum(len(unit.text) for plan in chapter_plans for unit in plan["render_units"])
    total_units = sum(len(plan["render_units"]) for plan in chapter_plans)
    role_chars = Counter()
    stage_units = Counter()
    for plan in chapter_plans:
        for unit in plan["render_units"]:
            role_chars[unit.role] += len(unit.text)
            stage_units[f"{unit.role}:{unit.stage}"] += 1

    print(f"book={args.book}")
    print(f"title={book['title']}")
    print(f"engine={args.engine}")
    print(f"chapters={len(chapter_plans)} units={total_units} chars={total_chars}")
    print(f"dialogue_alias={dry_stats.get('dialogue:alias', 0)} dialogue_pronoun={dry_stats.get('dialogue:pronoun', 0)} dialogue_alternating={dry_stats.get('dialogue:alternating', 0)} dialogue_unknown={dry_stats.get('dialogue:unknown', 0)}")
    print("role_chars=" + json.dumps(role_chars.most_common(), ensure_ascii=True))
    if args.dry_run:
        return

    api_key = read_api_key(Path(args.key_file).expanduser() if args.key_file else DEFAULT_KEY_FILE)
    silence_short = out_dir / "silence-0120ms.mp3"
    silence_chapter = out_dir / "silence-2500ms.mp3"
    make_silence(silence_short, 0.12)
    make_silence(silence_chapter, 2.5)

    chapter_files: list[tuple[str, Path]] = []
    manifest_chapters: list[dict[str, Any]] = []
    for plan in chapter_plans:
        chapter_slug = f"{plan['chapter_index']:03d}-{slugify(plan['title'])}"
        chapter_chunks = chunks_root / chapter_slug
        chapter_chunks.mkdir(parents=True, exist_ok=True)
        unit_files: list[Path] = []
        manifest_units: list[dict[str, Any]] = []
        render_units: list[SpeechUnit] = plan["render_units"]
        if args.engine == "dialogue":
            dialogue_chunks = chunk_dialogue_units(render_units, roles=roles, max_chars=args.dialogue_max_chars)
            dialogue_results: dict[int, tuple[Path, dict[str, str]]] = {}

            def render_dialogue_job(job_index: int, chunk_units: list[SpeechUnit], chunk_file: Path) -> tuple[int, Path, dict[str, str]]:
                if chunk_file.exists() and not args.force:
                    return job_index, chunk_file, {"request_id": "", "history_item_id": "", "character_count": ""}
                audio, headers = render_dialogue_chunk(
                    api_key=api_key,
                    units=chunk_units,
                    roles=roles,
                    model_id=args.model_id,
                    output_format=args.output_format,
                    seed=(args.seed + job_index - 1 + (plan["chapter_index"] * 1000)) if args.seed is not None else None,
                )
                chunk_file.write_bytes(audio)
                if args.pause > 0:
                    time.sleep(args.pause)
                return job_index, chunk_file, headers

            jobs: list[tuple[int, list[SpeechUnit], Path]] = []
            for index, chunk_units in enumerate(dialogue_chunks, start=1):
                chunk_file = chapter_chunks / f"{index:04d}-dialogue.mp3"
                jobs.append((index, chunk_units, chunk_file))

            if args.jobs > 1:
                with ThreadPoolExecutor(max_workers=args.jobs) as executor:
                    futures = {
                        executor.submit(render_dialogue_job, index, chunk_units, chunk_file): index
                        for index, chunk_units, chunk_file in jobs
                    }
                    completed = 0
                    for future in as_completed(futures):
                        index, chunk_file, headers = future.result()
                        dialogue_results[index] = (chunk_file, headers)
                        completed += 1
                        print(
                            f"chapter={chapter_slug} dialogue_chunk={completed}/{len(jobs)}",
                            flush=True,
                        )
            else:
                for index, chunk_units, chunk_file in jobs:
                    _, rendered_file, headers = render_dialogue_job(index, chunk_units, chunk_file)
                    dialogue_results[index] = (rendered_file, headers)

            for index, chunk_units, chunk_file in jobs:
                rendered_file, headers = dialogue_results[index]
                unit_files.append(rendered_file)
                manifest_units.append(
                    {
                        "index": index,
                        "engine": "dialogue",
                        "roles": sorted({unit.role if unit.role in roles else "narrator" for unit in chunk_units}),
                        "stages": sorted({unit.stage for unit in chunk_units}),
                        "dialogue_settings": dialogue_settings_for_units(chunk_units) or {},
                        "characters": sum(len(unit.text) for unit in chunk_units),
                        "file": str(rendered_file.relative_to(out_dir)),
                        "request_id": headers.get("request_id", ""),
                        "history_item_id": headers.get("history_item_id", ""),
                        "reported_character_count": headers.get("character_count", ""),
                        "unit_count": len(chunk_units),
                        "text_preview": chunk_units[0].text[:140] if chunk_units else "",
                    }
                )
        else:
            for index, unit in enumerate(render_units, start=1):
                role = unit.role if unit.role in roles else "narrator"
                role_plan = roles[role]
                chunk_file = chapter_chunks / f"{index:04d}-{role}.mp3"
                headers = {"request_id": "", "history_item_id": "", "character_count": ""}
                if not chunk_file.exists() or args.force:
                    previous_text = render_units[index - 2].text if index > 1 else None
                    next_text = render_units[index].text if index < len(render_units) else None
                    audio, headers = render_tts_chunk(
                        api_key=api_key,
                        text=unit.text,
                        voice_id=str(role_plan["voice_id"]),
                        model_id=args.model_id,
                        output_format=args.output_format,
                        voice_settings=unit.voice_settings,
                        seed=(args.seed + index - 1 + (plan["chapter_index"] * 1000)) if args.seed is not None else None,
                        previous_text=previous_text,
                        next_text=next_text,
                    )
                    chunk_file.write_bytes(audio)
                    if args.pause > 0:
                        time.sleep(args.pause)
                unit_files.append(chunk_file)
                manifest_units.append(
                    {
                        "index": index,
                        "engine": "tts",
                        "role": role,
                        "stage": unit.stage,
                        "voice_name": role_plan.get("voice_name"),
                        "voice_id": role_plan.get("voice_id"),
                        "source": unit.source,
                        "characters": len(unit.text),
                        "file": str(chunk_file.relative_to(out_dir)),
                        "request_id": headers.get("request_id", ""),
                        "history_item_id": headers.get("history_item_id", ""),
                        "reported_character_count": headers.get("character_count", ""),
                        "text_preview": unit.text[:140],
                    }
                )

        chapter_inputs: list[Path] = []
        for i, unit_file in enumerate(unit_files):
            chapter_inputs.append(unit_file)
            if i < len(unit_files) - 1:
                chapter_inputs.append(silence_short)
        chapter_file = chapters_out / f"{chapter_slug}.mp3"
        concat_audio(chapter_inputs, chapter_file)
        chapter_files.append((plan["title"], chapter_file))
        duration = duration_ms(chapter_file)
        print(f"chapter={chapter_slug} units={len(unit_files)} duration_ms={duration}", flush=True)
        manifest_chapters.append(
            {
                "index": plan["chapter_index"],
                "title": plan["title"],
                "source": str(plan["path"].relative_to(ROOT)),
                "file": str(chapter_file.relative_to(out_dir)),
                "duration_ms": duration,
                "units": manifest_units,
                "stats": dict(plan["stats"]),
            }
        )

    master_inputs: list[Path] = []
    for i, (_, chapter_file) in enumerate(chapter_files):
        master_inputs.append(chapter_file)
        if i < len(chapter_files) - 1:
            master_inputs.append(silence_chapter)

    master_no_chapters = master_dir / f"{args.book}-{args.model_id}.m4a"
    master_with_chapters = master_dir / f"{args.book}-{args.model_id}.m4b"
    if not args.no_master:
        concat_audio(master_inputs, master_no_chapters, codec="aac")
        write_chapter_metadata(master_no_chapters, master_with_chapters, str(book["title"]), chapter_files)

    manifest_path = out_dir / f"{args.book}-{args.model_id}-manifest.json"
    manifest_path.write_text(
        json.dumps(
            {
                "book": args.book,
                "title": book["title"],
                "engine": args.engine,
                "model_id": args.model_id,
                "output_format": args.output_format,
                "source_dir": str(book_dir.relative_to(ROOT)),
                "cast": str(Path(args.cast).resolve().relative_to(ROOT)),
                "arcs": str(Path(args.arcs).resolve().relative_to(ROOT)),
                "master": str(master_with_chapters.relative_to(out_dir)) if not args.no_master else None,
                "chapters": manifest_chapters,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"manifest={manifest_path}")
    if not args.no_master:
        print(f"master={master_with_chapters}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("book", choices=sorted(BOOKS), help="Book slug to render.")
    parser.add_argument("--cast", default=str(DEFAULT_CAST), help="Path to audiobook-cast.json.")
    parser.add_argument("--arcs", default=str(DEFAULT_ARCS), help="Path to audiobook-voice-arcs.json.")
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR), help="Output directory.")
    parser.add_argument("--key-file", help="ElevenLabs key file. Defaults to the local Documents/API-KEYS key.")
    parser.add_argument("--engine", choices=("dialogue", "tts"), default="dialogue", help="Render with grouped Text to Dialogue or per-unit Text to Speech.")
    parser.add_argument("--model-id", default=DEFAULT_MODEL, help="ElevenLabs TTS model.")
    parser.add_argument("--output-format", default=DEFAULT_OUTPUT_FORMAT, help="ElevenLabs output format.")
    parser.add_argument("--max-chars", type=int, default=DEFAULT_MAX_CHARS, help="Maximum characters per TTS request.")
    parser.add_argument("--dialogue-max-chars", type=int, default=DEFAULT_DIALOGUE_MAX_CHARS, help="Maximum characters per Text to Dialogue request.")
    parser.add_argument("--start-chapter", type=int, help="First chapter number to render.")
    parser.add_argument("--end-chapter", type=int, help="Last chapter number to render.")
    parser.add_argument("--limit-chapters", type=int, help="Render only the first N chapters in the selected range.")
    parser.add_argument("--seed", type=int, help="Optional deterministic seed base.")
    parser.add_argument("--pause", type=float, default=0.2, help="Delay between API requests.")
    parser.add_argument("--jobs", type=int, default=1, help="Concurrent Text to Dialogue requests per chapter.")
    parser.add_argument("--force", action="store_true", help="Regenerate existing chunks.")
    parser.add_argument("--dry-run", action="store_true", help="Plan the render without calling ElevenLabs.")
    parser.add_argument("--no-master", action="store_true", help="Skip M4B master creation.")
    args = parser.parse_args()
    render_book(args)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
