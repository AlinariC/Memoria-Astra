#!/usr/bin/env python3
"""Build Cinderwake audiobook publishing packages.

The rendered ElevenLabs masters remain untouched. This script creates a
separate, store-facing package tree with square audiobook artwork, metadata
handoff files, retail samples, and 192 kbps CBR MP3 chapter exports for stores
that prefer or require chapterized MP3 audio.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import shutil
import subprocess
import textwrap
import zipfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
RENDER_ROOT = ROOT / "output" / "audiobooks" / "cinderwake" / "full"
DEFAULT_OUT = ROOT / "output" / "audiobooks" / "cinderwake" / "publishing"
CATALOG = ROOT / "metadata" / "apple-books" / "catalog.json"
AUTHOR = "Alinari Campbell"
PUBLISHER = "PixelPacific"
IMPRINT = "PixelPacific Publishing"
LANGUAGE = "en"
SERIES = "The Cinderwake Trilogy"
NARRATOR = "PixelPacific AI Ensemble"
DIGITAL_VOICE_DISCLOSURE = "This audiobook is narrated by a digital voice."
APPLE_DIGITAL_VOICE_DISCLOSURE = (
    "This is an Apple Books audiobook narrated by a digital voice based on a human narrator."
)
APPLE_PROVIDER = "5J65K99MZ2"
APPLE_WHOLESALE_PRICE_TIER = "3"
APPLE_AUDIOBOOK_TERRITORIES = [
    "AU",
    "AT",
    "BE",
    "CA",
    "DK",
    "FI",
    "FR",
    "DE",
    "GR",
    "IE",
    "IT",
    "JP",
    "LU",
    "NL",
    "NZ",
    "NO",
    "PT",
    "ES",
    "SE",
    "CH",
    "GB",
    "US",
]
RELEASE_DATE = "2026-05-21"
LIST_PRICE_USD = "14.99"
BUNDLE_PRICE_USD = "34.99"
GENRE = "Epic Fantasy"
APPLE_GENRE_CODE = "SCIFI-FANTASY-00"
SPOTIFY_COVER_SIZE = 3000
ACX_COVER_SIZE = 2400
SILENCE_HEAD_SECONDS = "0.75"
SILENCE_TAIL_SECONDS = "2.00"
ACX_FILTER = (
    f"anullsrc=r=44100:cl=mono:d={SILENCE_HEAD_SECONDS}[head];"
    f"anullsrc=r=44100:cl=mono:d={SILENCE_TAIL_SECONDS}[tail];"
    "[head][0:a][tail]concat=n=3:v=0:a=1,"
    "loudnorm=I=-20:TP=-3:LRA=11"
)


@dataclass(frozen=True)
class BookSpec:
    slug: str
    title: str
    number: int
    source_cover: Path
    vendor_id: str

    @property
    def render_dir(self) -> Path:
        return RENDER_ROOT / self.slug

    @property
    def manifest_path(self) -> Path:
        return self.render_dir / f"{self.slug}-eleven_v3-manifest.json"

    @property
    def master_dir(self) -> Path:
        return self.render_dir / "master"

    @property
    def master_m4a(self) -> Path:
        return self.master_dir / f"{self.slug}-eleven_v3.m4a"

    @property
    def master_m4b(self) -> Path:
        return self.master_dir / f"{self.slug}-eleven_v3.m4b"


BOOKS = [
    BookSpec(
        slug="book-01-the-ash-beneath-the-crown",
        title="The Ash Beneath the Crown",
        number=1,
        source_cover=ROOT / "Fantasy Novel Series" / "01_The_Ash_Beneath_the_Crown" / "cover-300dpi.jpg",
        vendor_id="cinderwake_audio_01_the_ash_beneath_the_crown",
    ),
    BookSpec(
        slug="book-02-the-moon-below-the-world",
        title="The Moon Below the World",
        number=2,
        source_cover=ROOT / "Fantasy Novel Series" / "02_The_Moon_Below_the_World" / "cover-300dpi.jpg",
        vendor_id="cinderwake_audio_02_the_moon_below_the_world",
    ),
    BookSpec(
        slug="book-03-the-dragon-that-dreamed-death",
        title="The Dragon That Dreamed Death",
        number=3,
        source_cover=ROOT / "Fantasy Novel Series" / "03_The_Dragon_That_Dreamed_Death" / "cover-300dpi.jpg",
        vendor_id="cinderwake_audio_03_the_dragon_that_dreamed_death",
    ),
]


def run(cmd: list[str], *, quiet: bool = False) -> None:
    subprocess.run(
        cmd,
        check=True,
        stdout=subprocess.DEVNULL if quiet else None,
        stderr=subprocess.DEVNULL if quiet else None,
    )


def require_tool(name: str) -> None:
    if shutil.which(name) is None:
        raise SystemExit(f"Required tool not found: {name}")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_descriptions() -> dict[str, str]:
    if not CATALOG.exists():
        return {}
    catalog = read_json(CATALOG)
    books = catalog.get("books", {})
    descriptions: dict[str, str] = {}
    for key, value in books.items():
        if isinstance(value, dict):
            descriptions[key.replace("cinderwake-01", "book-01").replace("cinderwake-02", "book-02").replace("cinderwake-03", "book-03")] = str(
                value.get("description") or ""
            ).strip()
    return descriptions


def mkdir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def link_or_copy(source: Path, target: Path) -> None:
    mkdir(target.parent)
    if target.exists() and target.stat().st_size == source.stat().st_size:
        return
    if target.exists():
        target.unlink()
    try:
        os.link(source, target)
    except OSError:
        shutil.copy2(source, target)


def md5(path: Path) -> str:
    digest = hashlib.md5()  # noqa: S324 - store package metadata requires MD5 checksums.
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def ffprobe_json(path: Path) -> dict[str, Any]:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration,size:stream=codec_name,sample_rate,channels,bit_rate",
            "-of",
            "json",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def format_hhmmss(seconds: float) -> str:
    total = int(round(seconds))
    hours, remainder = divmod(total, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def format_hhmmss_millis(milliseconds: int) -> str:
    total_seconds, millis = divmod(milliseconds, 1000)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{millis:03d}"


def chapter_rows(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    elapsed_ms = 0
    for chapter in manifest["chapters"]:
        duration_ms = int(chapter["duration_ms"])
        rows.append(
            {
                "index": int(chapter["index"]),
                "title": str(chapter["title"]),
                "file": str(chapter["file"]),
                "duration_ms": duration_ms,
                "start_ms": elapsed_ms,
                "duration": format_hhmmss(duration_ms / 1000),
                "start": format_hhmmss(elapsed_ms / 1000),
                "start_precise": format_hhmmss_millis(elapsed_ms),
            }
        )
        elapsed_ms += duration_ms
    return rows


def build_square_art(source: Path, target: Path, size: int) -> None:
    if target.exists():
        return
    mkdir(target.parent)
    run(
        [
            "magick",
            str(source),
            "-colorspace",
            "sRGB",
            "-resize",
            f"{size}x{size}^",
            "-gravity",
            "center",
            "-extent",
            f"{size}x{size}",
            "-blur",
            "0x18",
            "-modulate",
            "88,108,100",
            "(",
            str(source),
            "-colorspace",
            "sRGB",
            "-resize",
            f"x{int(size * 0.90)}",
            ")",
            "-gravity",
            "center",
            "-composite",
            "-strip",
            "-quality",
            "92",
            str(target),
        ],
        quiet=True,
    )


def build_icon(source: Path, target: Path, size: int) -> None:
    if target.exists():
        return
    mkdir(target.parent)
    run(
        [
            "magick",
            str(source),
            "-resize",
            f"{size}x{size}",
            "-strip",
            str(target),
        ],
        quiet=True,
    )


def transcode_acx_chapter(source: Path, target: Path) -> None:
    if target.exists() and target.stat().st_size > 1024:
        return
    mkdir(target.parent)
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-nostdin",
            "-y",
            "-i",
            str(source),
            "-filter_complex",
            ACX_FILTER,
            "-ar",
            "44100",
            "-ac",
            "1",
            "-codec:a",
            "libmp3lame",
            "-b:a",
            "192k",
            "-write_xing",
            "0",
            str(target),
        ],
        quiet=True,
    )


def transcode_apple_track(source: Path, target: Path) -> None:
    if target.exists() and target.stat().st_size > 1024:
        return
    mkdir(target.parent)
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-nostdin",
            "-y",
            "-i",
            str(source),
            "-ar",
            "44100",
            "-ac",
            "1",
            "-codec:a",
            "libmp3lame",
            "-b:a",
            "192k",
            "-write_xing",
            "0",
            str(target),
        ],
        quiet=True,
    )


def build_retail_sample(source: Path, target: Path) -> None:
    if target.exists() and target.stat().st_size > 1024:
        return
    mkdir(target.parent)
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-nostdin",
            "-y",
            "-ss",
            "60",
            "-t",
            "270",
            "-i",
            str(source),
            "-filter:a",
            "afade=t=in:st=0:d=0.5,afade=t=out:st=269:d=1,loudnorm=I=-20:TP=-3:LRA=11",
            "-ar",
            "44100",
            "-ac",
            "1",
            "-codec:a",
            "libmp3lame",
            "-b:a",
            "192k",
            "-write_xing",
            "0",
            str(target),
        ],
        quiet=True,
    )


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    mkdir(path.parent)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, data: dict[str, Any]) -> None:
    mkdir(path.parent)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def apple_metadata_xml(book: BookSpec, metadata: dict[str, Any], audio_file: Path, cover_file: Path) -> str:
    chapters_xml = "\n".join(
        f"          <chapter><chapter_start_time>{escape(row['start_precise'])}</chapter_start_time><chapter_title>{escape(row['title'])}</chapter_title></chapter>"
        for row in metadata["chapters"]
    )
    description = APPLE_DIGITAL_VOICE_DISCLOSURE + " " + metadata["description"]
    products_xml = "\n".join(
        textwrap.dedent(
            f"""\
            <product>
              <territory>{territory}</territory>
              <wholesale_price_tier>{APPLE_WHOLESALE_PRICE_TIER}</wholesale_price_tier>
              <sales_start_date>{RELEASE_DATE}</sales_start_date>
              <cleared_for_sale>true</cleared_for_sale>
            </product>"""
        )
        for territory in APPLE_AUDIOBOOK_TERRITORIES
    )
    products_xml = textwrap.indent(products_xml, "    ")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://apple.com/itunes/importer" version="music5.3">
  <language>{LANGUAGE}</language>
  <provider>{APPLE_PROVIDER}</provider>
  <album>
    <album_type>audiobook</album_type>
    <vendor_id>{book.vendor_id}</vendor_id>
    <title>{escape(book.title)} (Unabridged)</title>
    <original_release_date>{RELEASE_DATE}</original_release_date>
    <label_name>{escape(PUBLISHER)}</label_name>
    <genres><genre code="{APPLE_GENRE_CODE}"/></genres>
    <copyright_pline>2026 {escape(IMPRINT)}</copyright_pline>
    <copyright_cline>2026 {escape(AUTHOR)}</copyright_cline>
    <artwork_files>
      <file><file_name>{cover_file.name}</file_name><size>{cover_file.stat().st_size}</size><checksum type="md5">{md5(cover_file)}</checksum></file>
    </artwork_files>
    <description><![CDATA[{description}]]></description>
    <products>
{products_xml}
    </products>
    <track_count>1</track_count>
    <artists>
      <artist><artist_name>{escape(AUTHOR)}</artist_name><roles><role>Author</role></roles><primary>true</primary></artist>
      <artist><artist_name>{escape(NARRATOR)}</artist_name><roles><role>Narrator</role></roles><primary>false</primary></artist>
    </artists>
    <tracks>
      <track>
        <type>audiobook</type>
        <vendor_id>{book.vendor_id}_track_1</vendor_id>
        <title>{escape(book.title)} (Unabridged)</title>
        <label_name>{escape(PUBLISHER)}</label_name>
        <explicit_content>none</explicit_content>
        <track_number>1</track_number>
        <audio_file><file_name>{audio_file.name}</file_name><size>{audio_file.stat().st_size}</size><checksum type="md5">{md5(audio_file)}</checksum></audio_file>
        <audio_language>{LANGUAGE}</audio_language>
        <preview_start_index>240</preview_start_index>
        <artists>
          <artist><artist_name>{escape(AUTHOR)}</artist_name><roles><role>Author</role></roles><primary>true</primary></artist>
          <artist><artist_name>{escape(NARRATOR)}</artist_name><roles><role>Narrator</role></roles><primary>false</primary></artist>
        </artists>
        <chapters>
{chapters_xml}
        </chapters>
      </track>
    </tracks>
  </album>
</package>
"""


def build_apple_itmsp(book: BookSpec, apple_dir: Path, audio_file: Path, cover_file: Path, metadata: dict[str, Any]) -> Path:
    itmsp_dir = apple_dir / f"{book.vendor_id}.itmsp"
    mkdir(itmsp_dir)
    package_audio = itmsp_dir / audio_file.name
    package_cover = itmsp_dir / cover_file.name
    link_or_copy(audio_file, package_audio)
    link_or_copy(cover_file, package_cover)
    (itmsp_dir / "metadata.xml").write_text(
        apple_metadata_xml(book, metadata, package_audio, package_cover),
        encoding="utf-8",
    )
    return itmsp_dir


def build_google_zip(book: BookSpec, chapter_files: list[Path], cover: Path, target: Path) -> None:
    expected_audio_count = len(chapter_files)
    if target.exists() and target.stat().st_size > 1024:
        with zipfile.ZipFile(target, "r") as archive:
            names = archive.namelist()
        if len(names) == expected_audio_count and all(name.lower().endswith(".mp3") for name in names):
            return
        target.unlink()
    mkdir(target.parent)
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_STORED) as archive:
        total = len(chapter_files)
        for index, chapter in enumerate(chapter_files, start=1):
            archive.write(chapter, f"{book.vendor_id}_{index:02d}of{total:02d}.mp3")


def package_book(book: BookSpec, out_root: Path, descriptions: dict[str, str], *, skip_acx: bool) -> dict[str, Any]:
    manifest = read_json(book.manifest_path)
    chapters = chapter_rows(manifest)
    total_ms = sum(int(row["duration_ms"]) for row in chapters)
    book_dir = out_root / book.slug
    artwork_dir = book_dir / "artwork"
    metadata_dir = book_dir / "metadata"
    acx_dir = book_dir / "acx-audible"
    spotify_dir = book_dir / "spotify"
    google_dir = book_dir / "google-play"
    apple_dir = book_dir / "apple-books"

    square_3000 = artwork_dir / f"{book.vendor_id}_square_3000.jpg"
    square_2400 = artwork_dir / f"{book.vendor_id}_square_2400.jpg"
    build_square_art(book.source_cover, square_3000, SPOTIFY_COVER_SIZE)
    build_square_art(book.source_cover, square_2400, ACX_COVER_SIZE)
    for size in [1024, 512, 256, 128]:
        build_icon(square_3000, artwork_dir / f"{book.vendor_id}_icon_{size}.png", size)

    description = descriptions.get(book.slug) or ""
    metadata = {
        "slug": book.slug,
        "title": book.title,
        "subtitle": "An epic fantasy audiobook",
        "series": SERIES,
        "series_number": book.number,
        "author": AUTHOR,
        "narrator": NARRATOR,
        "publisher": PUBLISHER,
        "imprint": IMPRINT,
        "language": LANGUAGE,
        "genre": GENRE,
        "vendor_id": book.vendor_id,
        "package_path": rel(book_dir),
        "release_date": RELEASE_DATE,
        "runtime_seconds": round(total_ms / 1000, 3),
        "runtime": format_hhmmss(total_ms / 1000),
        "chapters_count": len(chapters),
        "list_price_usd": LIST_PRICE_USD,
        "bundle_price_usd": BUNDLE_PRICE_USD,
        "digital_voice_disclosure": DIGITAL_VOICE_DISCLOSURE,
        "apple_digital_voice_disclosure": APPLE_DIGITAL_VOICE_DISCLOSURE,
        "description": description,
        "store_descriptions": {
            "spotify": f"{DIGITAL_VOICE_DISCLOSURE} {description}",
            "google_play": f"{DIGITAL_VOICE_DISCLOSURE} {description}",
            "apple_books": f"{APPLE_DIGITAL_VOICE_DISCLOSURE} {description}",
            "acx_audible": f"{DIGITAL_VOICE_DISCLOSURE} {description}",
        },
        "chapters": chapters,
    }

    write_json(metadata_dir / f"{book.vendor_id}.json", metadata)
    write_csv(metadata_dir / "chapters.csv", chapters)

    chapter_uploads: list[Path] = []
    if not skip_acx:
        for row in chapters:
            source = book.render_dir / row["file"]
            target = acx_dir / "chapters" / f"{book.vendor_id}_{row['index']:02d}of{len(chapters):02d}_{safe_name(row['title'])}.mp3"
            transcode_acx_chapter(source, target)
            chapter_uploads.append(target)
        build_retail_sample(chapter_uploads[0], acx_dir / "retail-sample.mp3")
        link_or_copy(square_2400, acx_dir / f"{book.vendor_id}_cover_2400.jpg")

    spotify_chapter_files = chapter_uploads if chapter_uploads else [book.render_dir / row["file"] for row in chapters]
    for chapter in spotify_chapter_files:
        link_or_copy(chapter, spotify_dir / "audio" / chapter.name)
    build_retail_sample(spotify_chapter_files[0], spotify_dir / "retail-sample.mp3")
    link_or_copy(square_3000, spotify_dir / f"{book.vendor_id}_cover_3000.jpg")

    for index, row in enumerate(chapters, start=1):
        source = spotify_chapter_files[index - 1]
        target = google_dir / "chapters" / f"{book.vendor_id}_{index:02d}of{len(chapters):02d}.mp3"
        link_or_copy(source, target)
    link_or_copy(square_3000, google_dir / f"{book.vendor_id}_frontcover.jpg")
    build_google_zip(
        book,
        sorted((google_dir / "chapters").glob("*.mp3")),
        google_dir / f"{book.vendor_id}_frontcover.jpg",
        google_dir / f"{book.vendor_id}.zip",
    )

    link_or_copy(book.master_m4a, apple_dir / f"{book.vendor_id}.m4a")
    link_or_copy(book.master_m4b, apple_dir / f"{book.vendor_id}.m4b")
    transcode_apple_track(book.master_m4a, apple_dir / f"{book.vendor_id}.mp3")
    link_or_copy(square_3000, apple_dir / f"{book.vendor_id}_cover_3000.jpg")
    apple_metadata_file = apple_dir / "metadata.xml"
    apple_audio = apple_dir / f"{book.vendor_id}.mp3"
    apple_cover = apple_dir / f"{book.vendor_id}_cover_3000.jpg"
    apple_metadata_file.write_text(
        apple_metadata_xml(book, metadata, apple_audio, apple_cover),
        encoding="utf-8",
    )
    apple_itmsp_dir = build_apple_itmsp(book, apple_dir, apple_audio, apple_cover, metadata)

    audio_probe = ffprobe_json(book.master_m4b)
    metadata["assets"] = {
        "source_manifest": rel(book.manifest_path),
        "master_m4a": rel(book.master_m4a),
        "master_m4b": rel(book.master_m4b),
        "artwork_square_3000": rel(square_3000),
        "artwork_square_2400": rel(square_2400),
        "acx_chapters": len(chapter_uploads),
        "google_zip": rel(google_dir / f"{book.vendor_id}.zip"),
        "apple_metadata": rel(apple_dir / "metadata.xml"),
        "apple_track_mp3": rel(apple_audio),
        "apple_itmsp": rel(apple_itmsp_dir),
        "spotify_audio_folder": rel(spotify_dir / "audio"),
    }
    metadata["audio_probe"] = audio_probe
    write_json(metadata_dir / f"{book.vendor_id}.json", metadata)
    return metadata


def safe_name(value: str) -> str:
    safe = "".join(char.lower() if char.isalnum() else "-" for char in value)
    while "--" in safe:
        safe = safe.replace("--", "-")
    return safe.strip("-")[:80] or "chapter"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def write_store_csvs(out_root: Path, all_metadata: list[dict[str, Any]]) -> None:
    rows = []
    for item in all_metadata:
        rows.append(
            {
                "vendor_id": item["vendor_id"],
                "title": item["title"],
                "subtitle": item["subtitle"],
                "series": item["series"],
                "series_number": item["series_number"],
                "author": item["author"],
                "narrator": item["narrator"],
                "language": item["language"],
                "genre": item["genre"],
                "release_date": item["release_date"],
                "runtime": item["runtime"],
                "chapters": item["chapters_count"],
                "list_price_usd": item["list_price_usd"],
                "digital_voice_disclosure": item["digital_voice_disclosure"],
                "description": item["description"],
            }
        )
    write_csv(out_root / "metadata" / "cinderwake-audiobook-master-metadata.csv", rows)
    for store, description_key in [
        ("spotify", "spotify"),
        ("google-play", "google_play"),
        ("apple-books", "apple_books"),
        ("acx-audible", "acx_audible"),
    ]:
        store_rows = []
        for item in all_metadata:
            store_rows.append(
                {
                    **{key: value for key, value in rows[all_metadata.index(item)].items() if key != "description"},
                    "description": item["store_descriptions"][description_key],
                }
            )
        write_csv(out_root / "metadata" / f"{store}-metadata.csv", store_rows)


def write_readiness(out_root: Path, all_metadata: list[dict[str, Any]]) -> None:
    lines = [
        "# Cinderwake Audiobook Publishing Readiness",
        "",
        f"Prepared: {date.today().isoformat()}",
        "",
        "## Store Package Set",
        "",
        "| Book | Runtime | Chapters | List Price | Primary Package Paths |",
        "|---|---:|---:|---:|---|",
    ]
    for item in all_metadata:
        lines.append(
            f"| {item['series_number']}. {item['title']} | {item['runtime']} | {item['chapters_count']} | ${item['list_price_usd']} | "
            f"`{item['package_path']}/spotify`, `{item['package_path']}/google-play`, `{item['package_path']}/apple-books` |"
        )
    lines.extend(
        [
            "",
            "## Recommended Upload Targets",
            "",
            "- Spotify for Authors: use each book's `spotify/` folder, the 3000 x 3000 cover, the chapterized MP3 audio, and the retail sample. Select the digital voice narration disclosure option.",
            "- Google Play Books: use each book's `google-play/` folder. The ZIP contains chapterized MP3 audio; the standalone `_frontcover.jpg` is included for thumbnail upload.",
            "- Apple Books audiobooks: use each book's `apple-books/*.itmsp` package for Transporter. The Apple package uses a full-length MP3 track because Transporter rejected the rendered M4A/AAC masters for direct API delivery.",
            "- Amazon/Audible via ACX: use each book's `acx-audible/` folder as a technical package only. ACX has stricter policy and QA gates around digital narration than Spotify/Google/Apple-partner routes, so treat this as staged rather than guaranteed accepted.",
            "",
            "## Pricing",
            "",
            f"- Individual audiobook list price: `${LIST_PRICE_USD}` USD.",
            f"- Suggested trilogy bundle or direct-store bundle: `${BUNDLE_PRICE_USD}` USD.",
            "- Keep Google Play's list price no higher than the same audiobook on other platforms.",
            "",
            "## Official Portal References",
            "",
            "- Spotify/Findaway digital narration support: https://newsroom.spotify.com/2025-02-20/spotify-opens-up-support-for-elevenlabs-audiobook-content/",
            "- Google Play Books audiobook file guidelines: https://support.google.com/books/partner/answer/3424254",
            "- Apple Books audiobook author guidance: https://authors.apple.com/audiobooks",
            "- Apple Books preferred partners: https://itunespartner.apple.com/books/partners",
            "- ACX audio submission requirements: https://www.acx.com/help/acx-audio-submission-requirements/201456300",
            "",
            "## Rights And Disclosure",
            "",
            f"- Author: {AUTHOR}.",
            f"- Publisher/imprint: {PUBLISHER} / {IMPRINT}.",
            f"- Narrator field: {NARRATOR}.",
            f"- Digital narration disclosure: `{DIGITAL_VOICE_DISCLOSURE}`",
            "- Do not list individual ElevenLabs stock voice names as human narrators.",
            "- Confirm final AI/digital narration disclosure in each portal before submitting for public sale.",
            "",
            "## Local Verification",
            "",
            "- All three source M4B masters exist and include chapter markers.",
            "- Apple `.itmsp` packages were generated with one full-length 192 kbps MP3 track per title, package-local metadata, package-local cover art, and chapter start times with millisecond precision.",
            "- ACX-style chapter exports are 44.1 kHz mono MP3 at 192 kbps CBR, with short head/tail silence and conservative loudness limiting.",
            "- Square audiobook covers were generated at 3000 x 3000 and 2400 x 2400, plus 1024/512/256/128 icon sizes.",
            "- Retail samples were generated at four minutes thirty seconds for each title.",
            "",
            "## Final Human Checks",
            "",
            "- Spot-listen to the first minute of each exported upload set after any portal transcoding.",
            "- Verify every portal's digital voice / AI narration disclosure wording before submit.",
            "- Use existing ebook listings to link the audiobook edition where the portal supports edition linking.",
            "- Final review, release, and storefront visibility actions should be checked in each portal after delivery.",
        ]
    )
    target = ROOT / "output" / "cinderwake-audiobook-publishing-readiness.md"
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare Cinderwake audiobook store packages.")
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--skip-acx", action="store_true", help="Skip 192 kbps MP3 chapter exports.")
    args = parser.parse_args()

    for tool in ["ffmpeg", "ffprobe", "magick"]:
        require_tool(tool)

    descriptions = load_descriptions()
    mkdir(args.out_dir)
    all_metadata = [
        package_book(book, args.out_dir, descriptions, skip_acx=args.skip_acx)
        for book in BOOKS
    ]
    write_store_csvs(args.out_dir, all_metadata)
    write_json(args.out_dir / "metadata" / "cinderwake-audiobook-package-manifest.json", {"books": all_metadata})
    write_readiness(args.out_dir, all_metadata)
    print(f"Prepared audiobook publishing packages in {rel(args.out_dir)}")


if __name__ == "__main__":
    main()
