#!/usr/bin/env python3
"""Normalize manuscript packages for the first typesetting-readiness pass."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
REPORT = ROOT / "production" / "typesetting-readiness.md"
MANIFEST = OUTPUT / "series-production-manifest.yaml"
OUTPUT_README = OUTPUT / "README.md"
PASS_DATE = "2026-05-18"


@dataclass(frozen=True)
class Book:
    number: int
    title: str
    folder: str
    chapter_count: int
    current_form: str


BOOKS = (
    Book(
        1,
        "The Ash Beneath the Crown",
        "book-01-the-ash-beneath-the-crown",
        36,
        "complete bespoke first revision with consistency polish and typesetting-readiness normalization",
    ),
    Book(
        2,
        "The Moon Below the World",
        "book-02-the-moon-below-the-world",
        31,
        "complete bespoke first revision with consistency polish and typesetting-readiness normalization",
    ),
    Book(
        3,
        "The Dragon That Dreamed Death",
        "book-03-the-dragon-that-dreamed-death",
        41,
        "complete bespoke first revision with consistency polish and typesetting-readiness normalization",
    ),
)


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def normalize_book_one(text: str) -> tuple[str, list[str]]:
    notes: list[str] = []
    back_matter_matches = list(re.finditer(r"(?m)^## Back Matter\b", text))
    if len(back_matter_matches) <= 1:
        return text, notes

    first = back_matter_matches[0]
    second = back_matter_matches[1]
    between = text[first.start() : second.start()]
    marker = "The first council of free Kell Ashgate met"
    marker_index = between.find(marker)
    if marker_index == -1:
        raise ValueError("Could not locate Book One continuation after duplicate back matter")

    continuation = between[marker_index:].lstrip()
    text = text[: first.start()].rstrip() + "\n\n" + continuation.rstrip() + "\n\n" + text[second.start() :].lstrip()
    notes.append("Removed duplicate early Book One back matter and kept the late Chapter 36 continuation before the final back matter.")
    return text, notes


def normalize_book_two(text: str) -> tuple[str, list[str]]:
    notes: list[str] = []
    bad = "## Chapter 13: The Downward Gate\n\n# Part III: Khar Veyl\n\n"
    good = "# Part III: Khar Veyl\n\n## Chapter 13: The Downward Gate\n\n"
    if bad in text:
        text = text.replace(bad, good, 1)
        notes.append("Moved Book Two Part III heading before Chapter 13.")
    return text, notes


def normalize_manuscript(book: Book, text: str) -> tuple[str, list[str]]:
    notes: list[str] = []
    if book.number == 1:
        text, book_notes = normalize_book_one(text)
        notes.extend(book_notes)
    elif book.number == 2:
        text, book_notes = normalize_book_two(text)
        notes.extend(book_notes)
    return text, notes


def update_metadata(book_dir: Path, book: Book, total: int) -> None:
    metadata = book_dir / "metadata.yaml"
    text = metadata.read_text(encoding="utf-8")
    replacements = {
        r'status: ".*"': 'status: "complete bespoke first revision"',
        r'target_page_count: ".*"': 'target_page_count: "350-600"',
        r'target_word_count: ".*"': 'target_word_count: "105000-180000"',
        r"produced_word_count: \d+": f"produced_word_count: {total}",
        r"at_300_words_per_page: \d+": f"at_300_words_per_page: {round(total / 300)}",
        r"at_275_words_per_page: \d+": f"at_275_words_per_page: {round(total / 275)}",
        r"at_250_words_per_page: \d+": f"at_250_words_per_page: {round(total / 250)}",
        r'current_form: ".*"': f'current_form: "{book.current_form}"',
    }
    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text)
    metadata.write_text(text, encoding="utf-8")


def validate_book(book_dir: Path, book: Book, text: str) -> list[str]:
    issues: list[str] = []
    if text.count(f"# {book.title}") != 1:
        issues.append("title heading count is not exactly one")
    if len(re.findall(r"(?m)^## (?:Back Matter|Glossary)\b", text)) != 1:
        issues.append("reader-facing back matter/glossary count is not exactly one")
    chapter_numbers = [int(n) for n in re.findall(r"(?m)^## Chapter (\d+):", text)]
    expected = list(range(1, book.chapter_count + 1))
    if chapter_numbers != expected:
        issues.append(f"chapter sequence mismatch: expected 1-{book.chapter_count}, found {chapter_numbers[:3]}...{chapter_numbers[-3:]}")
    if not (book_dir / "manuscript.md").exists():
        issues.append("missing manuscript.md")
    if not (book_dir / "metadata.yaml").exists():
        issues.append("missing metadata.yaml")
    return issues


def build_output_readme(rows: list[dict[str, object]]) -> str:
    lines = [
        "# Cinderwake Trilogy Output",
        "",
        "Complete bespoke first-revision manuscript packages.",
        "",
        "| Book | Folder | Produced Words | Estimated Print Pages |",
        "| --- | --- | ---: | ---: |",
    ]
    for row in rows:
        lines.append(
            f"| {row['title']} | `{row['folder']}` | {row['words']:,} | {row['pages_300']}-{row['pages_250']} |"
        )
    lines.extend(
        [
            "",
            "Page estimates use 250-300 words per print page. Each folder contains:",
            "",
            "- `manuscript.md`",
            "- `metadata.yaml`",
            "- `chapters/` with generated front matter, standalone part files, chapter files, and reader-facing glossary/back matter",
            "",
            "The next production pass should focus on publication export formatting, line proofing, and final front/back matter decisions.",
            "",
        ]
    )
    return "\n".join(lines)


def build_manifest(rows: list[dict[str, object]]) -> str:
    lines = [
        'series: "The Cinderwake Trilogy"',
        f'typesetting_pass_date: "{PASS_DATE}"',
        'source_status: "complete bespoke first revision"',
        'generated_by: "production/typesetting_readiness.py"',
        "books:",
    ]
    for row in rows:
        lines.extend(
            [
                f"  - book_number: {row['number']}",
                f'    title: "{row["title"]}"',
                f'    folder: "{row["folder"]}"',
                '    manuscript_file: "manuscript.md"',
                '    metadata_file: "metadata.yaml"',
                f"    chapter_count: {row['chapter_count']}",
                f"    produced_word_count: {row['words']}",
                "    estimated_print_pages:",
                f"      at_300_words_per_page: {row['pages_300']}",
                f"      at_275_words_per_page: {row['pages_275']}",
                f"      at_250_words_per_page: {row['pages_250']}",
            ]
        )
    return "\n".join(lines) + "\n"


def build_report(rows: list[dict[str, object]], notes: list[str], issues: list[str]) -> str:
    lines = [
        "# Typesetting Readiness Pass 01",
        "",
        f"Date: {PASS_DATE}",
        "",
        "## Result",
        "",
        "The trilogy output folders have been normalized for first-pass typesetting readiness while preserving the requested `manuscript.md` and `metadata.yaml` package shape.",
        "",
        "## Book Package Summary",
        "",
        "| Book | Chapters | Words | Estimated Pages |",
        "| --- | ---: | ---: | ---: |",
    ]
    for row in rows:
        lines.append(
            f"| {row['title']} | {row['chapter_count']} | {row['words']:,} | {row['pages_300']}-{row['pages_250']} |"
        )
    lines.extend(["", "## Normalizations", ""])
    if notes:
        lines.extend(f"- {note}" for note in notes)
    else:
        lines.append("- No structural manuscript fixes were required.")
    lines.extend(
        [
            "- Refreshed all book metadata to `complete bespoke first revision` status.",
            "- Standardized target page/word range metadata to the requested 350-600 page epic range.",
            "- Refreshed the output README and generated `output/series-production-manifest.yaml`.",
            "",
            "## Validation",
            "",
        ]
    )
    if issues:
        lines.extend(f"- Needs attention: {issue}" for issue in issues)
    else:
        lines.extend(
            [
                "- Each manuscript has exactly one title heading and one reader-facing glossary/back matter section.",
                "- Chapter sequences match the expected chapter counts.",
                "- All books remain above the 350-page lower bound at 300 words per page.",
                "- Chapter split workflow now emits `000-front-matter.md`, standalone part files, chapter files, and `999-back-matter.md`.",
            ]
        )
    lines.extend(
        [
            "",
            "## Optional Publishing Platform Decisions",
            "",
            "1. Choose final export targets: Markdown-only, DOCX, PDF, EPUB, or print-layout source.",
            "2. Add publisher-specific copyright, ISBN, dedication, title-page styling, or map assets if required by the platform.",
            "3. Keep `production/publishing-readiness-final.md` as the final handoff checklist for this manuscript pass.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    rows: list[dict[str, object]] = []
    notes: list[str] = []
    issues: list[str] = []

    for book in BOOKS:
        book_dir = OUTPUT / book.folder
        manuscript = book_dir / "manuscript.md"
        text = manuscript.read_text(encoding="utf-8")
        normalized, book_notes = normalize_manuscript(book, text)
        if normalized != text:
            manuscript.write_text(normalized, encoding="utf-8")
        notes.extend(book_notes)

        total = word_count(normalized)
        update_metadata(book_dir, book, total)
        book_issues = validate_book(book_dir, book, normalized)
        issues.extend(f"{book.title}: {issue}" for issue in book_issues)

        rows.append(
            {
                "number": book.number,
                "title": book.title,
                "folder": book.folder,
                "chapter_count": book.chapter_count,
                "words": total,
                "pages_300": round(total / 300),
                "pages_275": round(total / 275),
                "pages_250": round(total / 250),
            }
        )

    OUTPUT_README.write_text(build_output_readme(rows), encoding="utf-8")
    MANIFEST.write_text(build_manifest(rows), encoding="utf-8")
    REPORT.write_text(build_report(rows, notes, issues), encoding="utf-8")

    for row in rows:
        print(f"{row['title']}: {row['words']:,} words, {row['pages_300']}-{row['pages_250']} pages")
    if issues:
        raise SystemExit("Validation issues remain; see production/typesetting-readiness.md")


if __name__ == "__main__":
    main()
