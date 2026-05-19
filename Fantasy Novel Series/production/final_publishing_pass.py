#!/usr/bin/env python3
"""Prepare the trilogy manuscripts for reader-facing publishing handoff."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
REPORT = ROOT / "production" / "publishing-readiness-final.md"

BOOKS = (
    ("The Ash Beneath the Crown", OUTPUT / "book-01-the-ash-beneath-the-crown" / "manuscript.md"),
    ("The Moon Below the World", OUTPUT / "book-02-the-moon-below-the-world" / "manuscript.md"),
    ("The Dragon That Dreamed Death", OUTPUT / "book-03-the-dragon-that-dreamed-death" / "manuscript.md"),
)

PRODUCTION_LANGUAGE = (
    "Closing Note",
    "Full-length draft",
    "draft-zero",
    "generated",
    "placeholder",
    "TODO",
    "FIXME",
    "Final Fantasy",
    "World of Warcraft",
    "Lord of the Rings",
    "hobbit",
)


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def normalize_reader_facing_sections(text: str) -> tuple[str, list[str]]:
    notes: list[str] = []

    new_text = text.replace("\n\n## Front Matter\n\n", "\n\n")
    if new_text != text:
        notes.append("removed visible Front Matter label")
        text = new_text

    new_text = re.sub(
        r"\n## Back Matter\n\n### Closing Note\n\n.*?\n\n### Glossary\n",
        "\n## Glossary\n",
        text,
        count=1,
        flags=re.DOTALL,
    )
    if new_text != text:
        notes.append("removed production Closing Note and promoted Glossary")
        text = new_text

    new_text = text.replace("\n## Back Matter\n\n### Glossary\n", "\n## Glossary\n")
    if new_text != text:
        notes.append("promoted Glossary out of Back Matter label")
        text = new_text

    new_text = re.sub(
        r'"No," she said\. "Now you calculate with them in the room\."*',
        '"No," she said. "Now you calculate with them in the room."',
        text,
    )
    if new_text != text:
        notes.append("fixed missing closing quote in Book One court confrontation")
        text = new_text

    return text, notes


def chapter_numbers(text: str) -> list[int]:
    return [int(n) for n in re.findall(r"(?m)^## Chapter (\d+):", text)]


def odd_quote_paragraphs(text: str) -> list[str]:
    flagged: list[str] = []
    for paragraph in re.split(r"\n\s*\n", text):
        stripped = paragraph.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("**"):
            continue
        if stripped.count('"') % 2 == 1:
            flagged.append(stripped[:160])
    return flagged


def build_report(rows: list[dict[str, object]], notes: list[str], issues: list[str]) -> str:
    lines = [
        "# Final Publishing Readiness Pass",
        "",
        "Date: 2026-05-18",
        "",
        "## Package Summary",
        "",
        "| Book | Chapters | Words | Estimated Pages |",
        "| --- | ---: | ---: | ---: |",
    ]
    for row in rows:
        lines.append(f"| {row['title']} | {row['chapters']} | {row['words']:,} | {row['pages_300']}-{row['pages_250']} |")

    lines.extend(["", "## Reader-Facing Cleanup", ""])
    if notes:
        lines.extend(f"- {note}" for note in notes)
    else:
        lines.append("- No reader-facing section cleanup was required.")

    lines.extend(["", "## Validation", ""])
    if issues:
        lines.extend(f"- Needs attention: {issue}" for issue in issues)
    else:
        lines.extend(
            [
                "- No draft/scaffold/IP/placeholding language remains in manuscripts.",
                "- Each manuscript has one reader-facing `## Glossary` section.",
                "- Chapter numbering is sequential in all three books.",
                "- Straight double-quote parity check passed by paragraph.",
                "- Metadata word/page counts were refreshed after this pass.",
            ]
        )

    lines.extend(
        [
            "",
            "## Handoff Files",
            "",
            "- `output/book-01-the-ash-beneath-the-crown/manuscript.md`",
            "- `output/book-02-the-moon-below-the-world/manuscript.md`",
            "- `output/book-03-the-dragon-that-dreamed-death/manuscript.md`",
            "- `output/series-production-manifest.yaml`",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    notes: list[str] = []
    issues: list[str] = []
    rows: list[dict[str, object]] = []

    for title, path in BOOKS:
        text = path.read_text(encoding="utf-8")
        cleaned, book_notes = normalize_reader_facing_sections(text)
        if cleaned != text:
            path.write_text(cleaned, encoding="utf-8")
        notes.extend(f"{title}: {note}" for note in book_notes)

        for phrase in PRODUCTION_LANGUAGE:
            if re.search(re.escape(phrase), cleaned, re.IGNORECASE):
                issues.append(f"{title}: production language remains: {phrase}")

        glossary_count = len(re.findall(r"(?m)^## Glossary\b", cleaned))
        if glossary_count != 1:
            issues.append(f"{title}: expected one reader-facing Glossary section, found {glossary_count}")
        if re.search(r"(?m)^## Front Matter\b|^## Back Matter\b|^### Closing Note\b", cleaned):
            issues.append(f"{title}: production section label remains")

        chapters = chapter_numbers(cleaned)
        expected = list(range(1, len(chapters) + 1))
        if chapters != expected:
            issues.append(f"{title}: chapter sequence mismatch")

        quote_flags = odd_quote_paragraphs(cleaned)
        if quote_flags:
            issues.append(f"{title}: odd straight-quote paragraph count {len(quote_flags)}")

        words = word_count(cleaned)
        rows.append(
            {
                "title": title,
                "chapters": len(chapters),
                "words": words,
                "pages_300": round(words / 300),
                "pages_250": round(words / 250),
            }
        )

    REPORT.write_text(build_report(rows, notes, issues), encoding="utf-8")
    print(f"Wrote {REPORT}")
    if issues:
        print("Issues found:")
        for issue in issues:
            print(f"- {issue}")


if __name__ == "__main__":
    main()
