#!/usr/bin/env python3
"""Stage Google Play audiobook upload assets for the Cinderwake trilogy.

Google's content association is filename-driven. The staged files use the
GGKEY tokens from the first no-ISBN placeholder pass without the literal
GGKEY: prefix, which Google allows for filenames. Partner Center later refused
to convert those placeholder rows through CSV, so treat these assets as a
manual-upload staging set unless proper audiobook GGKEYs are created.
"""

from __future__ import annotations

import csv
import json
import os
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PUBLISHING = ROOT / "output" / "audiobooks" / "cinderwake" / "publishing"
STAGING = PUBLISHING / "google-play-upload-ready"
METADATA_DIR = PUBLISHING / "metadata"
STATUS_DOC = ROOT / "output" / "cinderwake-google-play-audiobook-delivery-status.md"

AUTHOR = "Alinari Campbell"
NARRATOR = "PixelPacific AI Ensemble"
PUBLISHER = "PixelPacific"
SERIES = "The Cinderwake Trilogy"
RELEASE_DATE = "D:2026-05-21"
LIST_PRICE_USD = "14.99"
DIGITAL_VOICE_DISCLOSURE = "This audiobook is narrated by a digital voice."
SUBJECTS = (
    "Fiction / Fantasy / Epic [BISAC]; "
    "Fiction / Fantasy / Action & Adventure [BISAC]; "
    "Fiction / Fantasy / Dragons & Mythical Creatures [BISAC]"
)

HEADERS = [
    "Identifier",
    "Status (Do Not Modify)",
    "Label (Do Not Modify)",
    "Play Store Link (Do Not Modify)",
    "Enable for Sale?",
    "Title",
    "Subtitle",
    "Book Format",
    "Related Identifier [Format, Relationship], Semicolon-Separated",
    "Contributor [Role], Semicolon-Separated",
    "Biographical Note",
    "Language",
    "Subject Code [Schema], Semicolon-Separated",
    "Age Group, Comma-Separated",
    "Description",
    "Publication Date",
    "Page Count",
    "Series Name",
    "Volume in Series",
    "Preview Type",
    "Preview Territories",
    "Buy Link Text",
    "Buy Link",
    "Publisher Name",
    "Publisher Website",
    "Show Photos in Preview?",
    "PDF Download Allowed?",
    "Release Date",
    "Allow preorder?",
    "DRM Enabled?",
    "Show Photos in eBook?",
    "Include Scanned Pages?",
    "For Mature Audiences?",
    "Copy-Paste Percentage",
    "Duration",
    "Audiobook: Preview Length Minutes",
    "Audiobook: Preview Length Percentage",
    "Abridged Version?",
    "USD [Recommended Retail Price, Excluding Tax] Price",
    "Countries for USD [Recommended Retail Price, Excluding Tax] Price",
    "International Rounding for USD [Recommended Retail Price, Excluding Tax] Price",
]

BOOKS = [
    {
        "number": 1,
        "slug": "book-01-the-ash-beneath-the-crown",
        "title": "The Ash Beneath the Crown",
        "subtitle": "Book One in The Cinderwake Trilogy",
        "vendor_id": "cinderwake_audio_01_the_ash_beneath_the_crown",
        "audiobook_ggkey": "GGKEY:67UBUE7Q2B0",
        "ebook_ggkey": "GGKEY:YU9XS0DXEUE",
    },
    {
        "number": 2,
        "slug": "book-02-the-moon-below-the-world",
        "title": "The Moon Below the World",
        "subtitle": "Book Two in The Cinderwake Trilogy",
        "vendor_id": "cinderwake_audio_02_the_moon_below_the_world",
        "audiobook_ggkey": "GGKEY:T7WL07YPJ7Z",
        "ebook_ggkey": "GGKEY:YZQ7FJBUABQ",
    },
    {
        "number": 3,
        "slug": "book-03-the-dragon-that-dreamed-death",
        "title": "The Dragon That Dreamed Death",
        "subtitle": "Book Three in The Cinderwake Trilogy",
        "vendor_id": "cinderwake_audio_03_the_dragon_that_dreamed_death",
        "audiobook_ggkey": "GGKEY:JU2YE1L46Q9",
        "ebook_ggkey": "GGKEY:EU9D90XDYUG",
    },
]


def link_or_copy(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.stat().st_size == source.stat().st_size:
        return
    if target.exists():
        target.unlink()
    try:
        os.link(source, target)
    except OSError:
        shutil.copy2(source, target)


def read_metadata(book: dict[str, Any]) -> dict[str, Any]:
    path = METADATA_DIR.parent / book["slug"] / "metadata" / f"{book['vendor_id']}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def html_description(metadata: dict[str, Any]) -> str:
    description = metadata["store_descriptions"]["google_play"].strip()
    if not description.startswith(DIGITAL_VOICE_DISCLOSURE):
        description = f"{DIGITAL_VOICE_DISCLOSURE} {description}"
    return "<p>" + description.replace("\n\n", "</p><p>").replace("\n", " ") + "</p>"


def short_ggkey(identifier: str) -> str:
    return identifier.replace("GGKEY:", "")


def stage_assets() -> list[dict[str, str]]:
    staged: list[dict[str, str]] = []
    for book in BOOKS:
        token = short_ggkey(book["audiobook_ggkey"])
        google_dir = PUBLISHING / book["slug"] / "google-play"
        source_zip = google_dir / f"{book['vendor_id']}.zip"
        source_cover = google_dir / f"{book['vendor_id']}_frontcover.jpg"
        target_zip = STAGING / f"{token}.zip"
        target_cover = STAGING / f"{token}_frontcover.jpg"
        link_or_copy(source_zip, target_zip)
        link_or_copy(source_cover, target_cover)
        staged.append(
            {
                "title": book["title"],
                "identifier": book["audiobook_ggkey"],
                "zip": str(target_zip.relative_to(ROOT)),
                "cover": str(target_cover.relative_to(ROOT)),
                "zip_size_mb": f"{target_zip.stat().st_size / 1024 / 1024:.1f}",
                "cover_size_kb": f"{target_cover.stat().st_size / 1024:.1f}",
            }
        )
    return staged


def metadata_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for book in BOOKS:
        metadata = read_metadata(book)
        row = {header: "" for header in HEADERS}
        row.update(
            {
                "Identifier": book["audiobook_ggkey"],
                "Enable for Sale?": "Yes",
                "Title": book["title"],
                "Subtitle": book["subtitle"],
                "Book Format": "Audiobook",
                "Related Identifier [Format, Relationship], Semicolon-Separated": (
                    f"{book['ebook_ggkey']} [Digital, Alternative format]"
                ),
                "Contributor [Role], Semicolon-Separated": f"{AUTHOR} [Author]; {NARRATOR} [Narrator]",
                "Language": "eng",
                "Subject Code [Schema], Semicolon-Separated": SUBJECTS,
                "Description": html_description(metadata),
                "Publication Date": RELEASE_DATE,
                "Series Name": SERIES,
                "Volume in Series": str(book["number"]),
                "Preview Type": "20%",
                "Preview Territories": "WORLD",
                "Publisher Name": PUBLISHER,
                "Release Date": RELEASE_DATE,
                "DRM Enabled?": "Yes",
                "For Mature Audiences?": "No",
                "Duration": metadata["runtime"],
                "Audiobook: Preview Length Minutes": "10",
                "Abridged Version?": "No",
                "USD [Recommended Retail Price, Excluding Tax] Price": LIST_PRICE_USD,
                "Countries for USD [Recommended Retail Price, Excluding Tax] Price": "WORLD",
            }
        )
        rows.append(row)
    return rows


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-16", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADERS, dialect="excel-tab")
        writer.writeheader()
        writer.writerows(rows)


def write_status(staged: list[dict[str, str]], metadata_path: Path) -> None:
    lines = [
        "# Cinderwake Google Play Audiobook Delivery Status",
        "",
        "Prepared: 2026-05-21",
        "",
        "## Current Partner Center State",
        "",
        "- Google Play Books Partner Center exposes audiobook upload tooling for this account.",
        "- The three old cover-only placeholder rows were tested, but Partner Center did not accept CSV conversion to audiobook records.",
        "- Do not modify the existing live ebook rows; those remain the primary ebook listings.",
        "",
        "## Audiobook Placeholder Mapping",
        "",
        "| Audiobook row | Title | Existing ebook row |",
        "|---|---|---|",
    ]
    for book in BOOKS:
        lines.append(f"| `{book['audiobook_ggkey']}` | {book['title']} | `{book['ebook_ggkey']}` |")
    lines.extend(
        [
            "",
            "## Upload-Ready Files",
            "",
            "| Title | ZIP | Cover | ZIP size |",
            "|---|---|---|---:|",
        ]
    )
    for item in staged:
        lines.append(f"| {item['title']} | `{item['zip']}` | `{item['cover']}` | {item['zip_size_mb']} MB |")
    lines.extend(
        [
            "",
            "## Metadata Sheet",
            "",
            f"- `{metadata_path.relative_to(ROOT)}` is UTF-16 tab-delimited, matching the prior successful Google upload format.",
            "- It sets Book Format to `Audiobook`, links each audiobook row to the corresponding live ebook row, applies worldwide USD pricing at `$14.99`, and includes the digital narration disclosure in the description.",
            "",
            "## Next Action",
            "",
            "Do not keep retrying CSV conversion against the old placeholder rows.",
            "Create proper audiobook records through Partner Center's audiobook flow, or manually convert each placeholder row in the UI and save it as an audiobook before uploading audio from that book's own Content tab.",
        ]
    )
    STATUS_DOC.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    staged = stage_assets()
    metadata_path = METADATA_DIR / "google-play-audiobook-upload-2026-05-21.csv"
    write_tsv(metadata_path, metadata_rows())
    write_status(staged, metadata_path)
    print(f"Prepared Google Play audiobook files in {STAGING.relative_to(ROOT)}")
    print(f"Prepared Google Play audiobook metadata at {metadata_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
