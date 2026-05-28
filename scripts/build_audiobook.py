#!/usr/bin/env python3
"""Build audiobook tracks from a Markdown manuscript.

The OpenAI path expects OPENAI_API_KEY in the environment. The macOS path uses
the local `say` command as a guide-track fallback when API billing is unavailable.
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
import urllib.request
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BOOK_DIR = ROOT / "archive/Memoria_Astra/01_Terra_in_the_Mists"
DEFAULT_OUT_DIR = ROOT / "output/audiobooks/terra-in-the-mists"

OPENAI_MODEL = "gpt-4o-mini-tts"
OPENAI_MAX_CHARS = 3000
MACOS_MAX_CHARS = 9000

VOICE_PROFILES = {
    "classic": {
        "description": "Warm literary narration with a subtle Lyra voice shift.",
        "roles": {
            "header": {
                "openai_voice": "cedar",
                "macos_voice": "Daniel",
                "rate": "151",
                "instructions": (
                    "Read this section heading in a clean, neutral audiobook title style. Keep it simple, "
                    "measured, and unobtrusive. Do not dramatize, explain, or add words. Preserve the words exactly."
                ),
            },
            "aru": {
                "openai_voice": "cedar",
                "macos_voice": "Daniel",
                "rate": "151",
                "instructions": (
                    "Narrate like a premium literary science-fantasy audiobook: warm, ancient, "
                    "restrained, intimate, and mythic. Keep the pacing unhurried, with clean "
                    "diction and quiet awe. Avoid melodrama, announcer energy, or synthetic cheer."
                ),
            },
            "lyra": {
                "openai_voice": "marin",
                "macos_voice": "Samantha",
                "rate": "156",
                "instructions": (
                    "Narrate like a premium literary science-fantasy audiobook: intelligent, "
                    "curious, grounded, and emotionally contained. Let wonder build gradually. "
                    "Keep technical passages clear and human, never robotic."
                ),
            },
        },
    },
    "epic": {
        "description": "Deep single-narrator mythic performance with stronger emotional direction.",
        "roles": {
            "header": {
                "openai_voice": "cedar",
                "macos_voice": "Daniel",
                "rate": "150",
                "instructions": (
                    "Read this section heading in a clean, neutral audiobook title style. Keep it simple, "
                    "measured, and unobtrusive. Do not dramatize, explain, or add words. Preserve the words exactly."
                ),
            },
            "aru": {
                "openai_voice": "onyx",
                "macos_voice": "Daniel",
                "rate": "140",
                "instructions": (
                    "Narrate as a deep, resonant, epic literary audiobook storyteller. Use a low, "
                    "grave register; slow, deliberate pacing; real grief beneath the cosmic wonder; "
                    "and meaningful pauses. Tell the story as lived memory, not as text on a page. "
                    "Vary intonation and pacing so the listener feels awe, loss, tenderness, and hope. "
                    "Do not imitate any real person, living or dead. Preserve the words exactly."
                ),
            },
            "lyra": {
                "openai_voice": "onyx",
                "macos_voice": "Daniel",
                "rate": "142",
                "instructions": (
                    "Narrate as the same deep epic audiobook storyteller, but bring a clearer modern "
                    "edge for Lyra's sections: intelligence, curiosity, exhaustion, and rising awe. "
                    "Keep the voice low and cinematic, with emotional movement and deliberate pauses. "
                    "Do not imitate any real person, living or dead. Preserve the words exactly."
                ),
            },
        },
    },
    "emotional": {
        "description": "Neutral section headings with deeper, more emotional storytelling narration.",
        "separate_section_headers": True,
        "header_role": "header",
        "roles": {
            "header": {
                "openai_voice": "cedar",
                "macos_voice": "Daniel",
                "rate": "150",
                "instructions": (
                    "Read this section heading in a clean, neutral audiobook title style. Keep it simple, "
                    "measured, and unobtrusive. Do not dramatize, explain, or add words. Preserve the words exactly."
                ),
            },
            "aru": {
                "openai_voice": "onyx",
                "macos_voice": "Daniel",
                "rate": "136",
                "instructions": (
                    "Perform as Aru-Solien: an ancient survivor making a private confession to one listener. "
                    "Aim for a warm Black American bass-baritone audiobook feel with polished standard American "
                    "diction: deep, rich, human, and emotionally present, but never caricatured and never dialect. "
                    "Do not imitate any real person, living or dead. Underplay grandeur; make cosmic moments feel "
                    "remembered, not proclaimed. Do not give every sentence equal importance: move through exposition "
                    "naturally, slow before revelations, soften on tenderness, and let final lines land. Avoid monotone, "
                    "trailer voice, sermon cadence, synthetic cheer, and over-enunciation. Preserve the words exactly."
                ),
            },
            "lyra": {
                "openai_voice": "onyx",
                "macos_voice": "Daniel",
                "rate": "138",
                "instructions": (
                    "Use the same narrator as Aru-Solien, but let Lyra-focused passages carry a sharper modern current: "
                    "intelligence, exhaustion, urgency, wonder, and discovery. Keep the same deep, rich, polished "
                    "audiobook voice, with no caricature and no dialect. Do not imitate any real person, living or dead. "
                    "Let the signal feel chosen and alive; move faster through technical setup, then slow when awe or fear "
                    "breaks through. Avoid monotone, trailer voice, sermon cadence, synthetic cheer, and over-enunciation. "
                    "Preserve the words exactly."
                ),
            },
        },
    },
}


@dataclass
class Section:
    index: int
    title: str
    body: str
    voice_key: str

    @property
    def slug(self) -> str:
        slug = re.sub(r"[^a-z0-9]+", "-", self.title.lower()).strip("-")
        return f"{self.index:02d}-{slug}"

    @property
    def display_text(self) -> str:
        return f"{self.title}\n\n{self.body.strip()}\n"

    @property
    def header_text(self) -> str:
        return f"{self.title}\n"

    @property
    def body_text(self) -> str:
        return f"{self.body.strip()}\n"


def run(cmd: list[str], *, quiet: bool = False) -> None:
    if quiet:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        subprocess.run(cmd, check=True)


def require_tool(name: str) -> None:
    if shutil.which(name) is None:
        raise SystemExit(f"Required tool not found: {name}")


def read_markdown_sections(book_dir: Path) -> tuple[dict[str, str], list[Section]]:
    manuscript = book_dir / "Manuscript.md"
    text = manuscript.read_text(encoding="utf-8")
    metadata: dict[str, str] = {}

    if text.startswith("---\n"):
        _, front_matter, text = text.split("---", 2)
        for line in front_matter.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                metadata[key.strip()] = value.strip().strip('"')

    matches = list(re.finditer(r"^# (.+)$", text, flags=re.MULTILINE))
    sections: list[Section] = []
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        title = match.group(1).strip()
        body = clean_markdown_for_speech(text[start:end])
        voice_key = "lyra" if title in {"Chapter 8 - The Signal", "Epilogue - The Vault of Breath"} else "aru"
        sections.append(Section(i + 1, title, body, voice_key))

    return metadata, sections


def clean_markdown_for_speech(text: str) -> str:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = text.replace("*", "")
    text = text.replace("_", "")
    text = re.sub(r"\n-{3,}\n?", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_text(text: str, max_chars: int) -> list[str]:
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks: list[str] = []
    current = ""

    def push_current() -> None:
        nonlocal current
        if current.strip():
            chunks.append(current.strip())
        current = ""

    for paragraph in paragraphs:
        if len(paragraph) > max_chars:
            push_current()
            sentences = re.split(r"(?<=[.!?])\s+", paragraph)
            for sentence in sentences:
                if len(sentence) > max_chars:
                    for offset in range(0, len(sentence), max_chars):
                        chunks.append(sentence[offset : offset + max_chars].strip())
                elif len(current) + len(sentence) + 2 <= max_chars:
                    current = f"{current} {sentence}".strip()
                else:
                    push_current()
                    current = sentence
            continue

        if len(current) + len(paragraph) + 2 <= max_chars:
            current = f"{current}\n\n{paragraph}".strip()
        else:
            push_current()
            current = paragraph

    push_current()
    return chunks


def get_openai_api_key(key_file: str | None) -> str:
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key and key_file:
        api_key = Path(key_file).expanduser().read_text(encoding="utf-8").strip()
    if not api_key:
        raise SystemExit("OPENAI_API_KEY or --key-file is required for --engine openai")
    return api_key


def section_direction(title: str) -> str:
    directions = {
        "Prologue - Before the Silence": (
            "Open with sacred quiet. Let the first line feel ancient and inevitable. "
            "Build toward the Moon's arrival with dread, then soften into witness."
        ),
        "Chapter 1 - When the Sky Began to Fall": (
            "Carry deep nostalgia and restrained devastation. The descriptions of Terra should glow; "
            "the Moon's arrival should feel like doom entering the room."
        ),
        "Chapter 2 - The Weight of Air": (
            "Let unease accumulate slowly. Treat silence, weight, and falling as emotional pressure, "
            "not action beats."
        ),
        "Chapter 3 - The Awakening Ground": (
            "Begin disoriented and intimate, then widen into grief. The narrator is learning a broken "
            "world with his whole body."
        ),
        "Chapter 4 - Those Who Remained": (
            "Use wary wonder. The survivor encounter should feel ancient, physical, and quietly dangerous."
        ),
        "Chapter 5 - The First Fire": (
            "Make the fire scenes communal and sacred. There should be tenderness in the discovery that "
            "broken people still make meaning."
        ),
        "Chapter 6 - In the Silence Between Stars": (
            "Let loneliness carry the chapter. Keep the voice haunted, patient, and vast."
        ),
        "Chapter 7 - Outliers": (
            "Bring a colder modern texture without losing the old soul of the narrator. The emotion is "
            "distance, not anger."
        ),
        "Chapter 8 - The Signal": (
            "Make Lyra's curiosity become obsession. Technical language should stay clear, but the signal "
            "should feel alive and chosen."
        ),
        "Chapter 9 - The Breath Returns": (
            "Move from quiet astonishment into reverence. Let hope arrive carefully, like something fragile."
        ),
        "Chapter 10 - The New Harmony": (
            "Let the chapter swell emotionally. The return of mist should feel miraculous but earned, "
            "with tears close to the surface."
        ),
        "Epilogue - The Vault of Breath": (
            "Close with prophetic awe and purpose. The Venus vision should feel luminous and tragic; "
            "the final Mars turn should sound like destiny beginning."
        ),
    }
    return directions.get(title, "Tell this section with emotional specificity and cinematic restraint.")


def profile_setting(profile: str, key: str, default: object) -> object:
    return VOICE_PROFILES[profile].get(key, default)


def role_plan(profile: str, voice_key: str) -> dict[str, str]:
    return VOICE_PROFILES[profile]["roles"][voice_key]


def header_role_key(profile: str, override: str | None = None) -> str:
    return override or str(profile_setting(profile, "header_role", "header"))


def should_separate_section_headers(profile: str, force_separate: bool) -> bool:
    return force_separate or bool(profile_setting(profile, "separate_section_headers", False))


def synthesize_openai(
    text: str,
    output: Path,
    voice_key: str,
    section: Section,
    profile: str,
    key_file: str | None,
    *,
    is_header: bool = False,
) -> None:
    api_key = get_openai_api_key(key_file)
    plan = role_plan(profile, voice_key)
    if is_header:
        instructions = plan["instructions"]
    else:
        instructions = f"{plan['instructions']} Section direction: {section_direction(section.title)}"
    payload = {
        "model": OPENAI_MODEL,
        "voice": plan["openai_voice"],
        "input": text,
        "instructions": instructions,
        "response_format": "mp3",
    }
    request = urllib.request.Request(
        "https://api.openai.com/v1/audio/speech",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            output.write_bytes(response.read())
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenAI speech request failed with HTTP {exc.code}: {body}") from exc


def synthesize_macos(text: str, output: Path, voice_key: str, profile: str) -> None:
    require_tool("say")
    require_tool("ffmpeg")
    plan = role_plan(profile, voice_key)
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        text_file = tmp_path / "input.txt"
        aiff_file = tmp_path / "speech.aiff"
        text_file.write_text(text, encoding="utf-8")
        run([
            "say",
            "-v",
            plan["macos_voice"],
            "-r",
            plan["rate"],
            "-f",
            str(text_file),
            "-o",
            str(aiff_file),
        ], quiet=True)
        run([
            "ffmpeg",
            "-y",
            "-i",
            str(aiff_file),
            "-ac",
            "1",
            "-ar",
            "44100",
            "-codec:a",
            "libmp3lame",
            "-b:a",
            "96k",
            str(output),
        ], quiet=True)


def make_silence(path: Path, seconds: float) -> None:
    require_tool("ffmpeg")
    run([
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
        "96k",
        str(path),
    ], quiet=True)


def concat_audio(inputs: list[Path], output: Path, *, codec: str = "libmp3lame") -> None:
    require_tool("ffmpeg")
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".txt", delete=False) as list_file:
        for item in inputs:
            list_file.write(f"file '{item.resolve()}'\n")
        list_path = Path(list_file.name)
    try:
        cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(list_path)]
        if codec == "aac":
            cmd += ["-c:a", "aac", "-b:a", "96k"]
        else:
            cmd += ["-c:a", "libmp3lame", "-b:a", "96k"]
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


def write_voice_plan(
    out_dir: Path,
    metadata: dict[str, str],
    profile: str,
    *,
    separate_headers: bool = False,
    header_role: str | None = None,
) -> None:
    title = metadata.get("title", "Terra in the Mists")
    roles = VOICE_PROFILES[profile]["roles"]
    profile_separates_headers = bool(profile_setting(profile, "separate_section_headers", False))
    separate_headers = separate_headers or profile_separates_headers
    header_role = header_role_key(profile, header_role) if separate_headers else None
    header_line = ""
    if header_role and header_role in roles:
        header_line = f"- `{roles[header_role]['openai_voice']}`: neutral section headings.\n"
    content = f"""# {title} Audiobook Voice Plan

Source manuscript: `archive/Memoria_Astra/01_Terra_in_the_Mists/Manuscript.md`

Production target: OpenAI `{OPENAI_MODEL}` through `/v1/audio/speech`.

Production profile: `{profile}` - {VOICE_PROFILES[profile]["description"]}

## Selected Voices

{header_line}{"- Section headings render as separate neutral audio parts.\n" if separate_headers else ""}
- `{roles["aru"]["openai_voice"]}`: Aru-Solien / primary narrator.
- `{roles["lyra"]["openai_voice"]}`: Lyra-focused sections.

## Section Assignment

- Prologue through Chapter 7: `{roles["aru"]["openai_voice"]}`
- Chapter 8, "The Signal": `{roles["lyra"]["openai_voice"]}`
- Chapter 9 and Chapter 10: `{roles["aru"]["openai_voice"]}`
- Epilogue, "The Vault of Breath": `{roles["lyra"]["openai_voice"]}`

## Disclosure

This audiobook is AI-generated narration and should be disclosed as such on any storefront or distribution page.
"""
    (out_dir / f"voice-plan-{profile}.md").write_text(content, encoding="utf-8")


def write_chapter_metadata(master_input: Path, master_output: Path, sections: list[Section], chapter_files: list[Path]) -> None:
    start = 0
    lines = [
        ";FFMETADATA1",
        "title=Terra in the Mists",
        "artist=Alinari Campbell",
        "album=Memoria Astra Cycle",
        "genre=Audiobook",
    ]
    for section, chapter in zip(sections, chapter_files):
        length = duration_ms(chapter)
        end = start + length
        safe_title = section.title.replace("=", "-")
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
    run([
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
    ], quiet=True)


def build(args: argparse.Namespace) -> None:
    require_tool("ffmpeg")
    require_tool("ffprobe")
    if args.profile not in VOICE_PROFILES:
        raise SystemExit(f"Unknown profile: {args.profile}")
    separate_headers = should_separate_section_headers(args.profile, args.separate_section_headers)
    required_header_role = header_role_key(args.profile, args.header_role)
    if separate_headers:
        if required_header_role not in VOICE_PROFILES[args.profile]["roles"]:
            raise SystemExit(
                f"Profile {args.profile!r} does not define header role {required_header_role!r}; "
                "choose a profile with a header role or add one to VOICE_PROFILES."
            )

    book_dir = Path(args.book_dir).resolve()
    out_dir = Path(args.out_dir).resolve()
    run_key = args.engine if args.profile == "classic" else f"{args.engine}-{args.profile}"
    chunks_dir = out_dir / f"{run_key}-chunks"
    chapters_dir = out_dir / f"{run_key}-chapters"
    master_dir = out_dir / "master"
    for directory in (chunks_dir, chapters_dir, master_dir):
        directory.mkdir(parents=True, exist_ok=True)

    metadata, sections = read_markdown_sections(book_dir)
    write_voice_plan(
        out_dir,
        metadata,
        args.profile,
        separate_headers=separate_headers,
        header_role=required_header_role,
    )

    max_chars = OPENAI_MAX_CHARS if args.engine == "openai" else MACOS_MAX_CHARS
    silence_short = out_dir / "silence-0750ms.mp3"
    silence_chapter = out_dir / "silence-2500ms.mp3"
    make_silence(silence_short, 0.75)
    make_silence(silence_chapter, 2.5)

    chapter_files: list[Path] = []
    manifest: list[dict[str, object]] = []
    for section in sections:
        render_jobs: list[tuple[str, str, str, bool]] = []
        if separate_headers:
            render_jobs.append(("header", section.header_text, required_header_role, True))
            for chunk_index, chunk in enumerate(split_text(section.body_text, max_chars), start=1):
                render_jobs.append((f"body-{chunk_index:02d}", chunk, section.voice_key, False))
        else:
            for chunk_index, chunk in enumerate(split_text(section.display_text, max_chars), start=1):
                render_jobs.append((f"part-{chunk_index:02d}", chunk, section.voice_key, False))
        chunk_files: list[Path] = []
        body_voice = role_plan(args.profile, section.voice_key)["openai_voice"]
        header_voice = role_plan(args.profile, required_header_role)["openai_voice"] if separate_headers else None
        voice_label = f"header={header_voice}, body={body_voice}" if separate_headers else f"voice={body_voice}"
        print(f"{section.slug}: {len(render_jobs)} part(s), {voice_label}", flush=True)
        for part_name, chunk, voice_key, is_header in render_jobs:
            chunk_file = chunks_dir / f"{section.slug}-{part_name}.mp3"
            if not chunk_file.exists() or args.force:
                if args.engine == "openai":
                    synthesize_openai(
                        chunk,
                        chunk_file,
                        voice_key,
                        section,
                        args.profile,
                        args.key_file,
                        is_header=is_header,
                    )
                    time.sleep(args.pause)
                else:
                    synthesize_macos(chunk, chunk_file, voice_key, args.profile)
            chunk_files.append(chunk_file)

        chapter_inputs: list[Path] = []
        for i, chunk_file in enumerate(chunk_files):
            chapter_inputs.append(chunk_file)
            if i < len(chunk_files) - 1:
                chapter_inputs.append(silence_short)

        chapter_file = chapters_dir / f"{section.slug}.mp3"
        concat_audio(chapter_inputs, chapter_file)
        chapter_files.append(chapter_file)
        manifest.append({
            "index": section.index,
            "title": section.title,
            "voice": body_voice,
            "body_voice": body_voice,
            "header_voice": header_voice,
            "header_role": required_header_role if separate_headers else None,
            "separate_section_header": separate_headers,
            "profile": args.profile,
            "chunks": len(render_jobs),
            "file": str(chapter_file.relative_to(out_dir)),
            "duration_ms": duration_ms(chapter_file),
        })

    master_inputs: list[Path] = []
    for i, chapter_file in enumerate(chapter_files):
        master_inputs.append(chapter_file)
        if i < len(chapter_files) - 1:
            master_inputs.append(silence_chapter)

    master_no_chapters = master_dir / f"terra-in-the-mists-{run_key}.m4a"
    master_with_chapters = master_dir / f"terra-in-the-mists-{run_key}.m4b"
    concat_audio(master_inputs, master_no_chapters, codec="aac")
    write_chapter_metadata(master_no_chapters, master_with_chapters, sections, chapter_files)

    manifest_path = out_dir / f"{run_key}-manifest.json"
    manifest_path.write_text(json.dumps({
        "title": metadata.get("title", "Terra in the Mists"),
        "author": metadata.get("author", "Alinari Campbell"),
        "engine": args.engine,
        "profile": args.profile,
        "model": OPENAI_MODEL if args.engine == "openai" else "macOS say",
        "master": str(master_with_chapters.relative_to(out_dir)),
        "sections": manifest,
    }, indent=2), encoding="utf-8")
    print(f"master={master_with_chapters}")
    print(f"manifest={manifest_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--book-dir", default=str(DEFAULT_BOOK_DIR))
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    parser.add_argument("--engine", choices=("openai", "macos"), default="openai")
    parser.add_argument("--profile", choices=sorted(VOICE_PROFILES), default="classic")
    parser.add_argument("--key-file", help="Read the OpenAI API key from a local file when OPENAI_API_KEY is unset.")
    parser.add_argument(
        "--separate-section-headers",
        action="store_true",
        help="Render each section heading as its own audio part using the profile's header_role.",
    )
    parser.add_argument("--header-role", help="Override the role used for separately rendered section headings.")
    parser.add_argument("--force", action="store_true", help="Regenerate chunks even when files already exist.")
    parser.add_argument("--pause", type=float, default=0.2, help="Delay between OpenAI chunk requests.")
    args = parser.parse_args()
    build(args)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
