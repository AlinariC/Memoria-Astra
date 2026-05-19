#!/usr/bin/env python3
"""Split each output manuscript into generated revision files.

The splitter keeps part headings as their own files so they do not end up inside
the preceding chapter or front matter during revision and typesetting.
"""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"


def slugify(title: str) -> str:
    title = title.lower()
    title = re.sub(r"[^a-z0-9]+", "-", title)
    return title.strip("-")


def clear_generated(chapters_dir: Path) -> None:
    for pattern in ("chapter-*.md", "part-*.md"):
        for old in chapters_dir.glob(pattern):
            old.unlink()
    for generated in ("000-front-matter.md", "999-back-matter.md"):
        path = chapters_dir / generated
        if path.exists():
            path.unlink()


def split_book(book_dir: Path) -> int:
    manuscript = book_dir / "manuscript.md"
    if not manuscript.exists():
        return 0

    text = manuscript.read_text(encoding="utf-8")
    chapters_dir = book_dir / "chapters"
    chapters_dir.mkdir(exist_ok=True)
    clear_generated(chapters_dir)

    back_matter_match = re.search(r"(?m)^## (?:Back Matter|Glossary)\b", text)
    body_limit = back_matter_match.start() if back_matter_match else len(text)
    body_source = text[:body_limit]

    tokens = list(re.finditer(r"(?m)^(# Part .+|## Chapter (\d+): (.+))$", body_source))
    if not tokens:
        return 0

    front = text[: tokens[0].start()].rstrip() + "\n"
    (chapters_dir / "000-front-matter.md").write_text(front, encoding="utf-8")

    chapter_count = 0
    part_count = 0
    for i, token in enumerate(tokens):
        start = token.start()
        end = tokens[i + 1].start() if i + 1 < len(tokens) else body_limit
        body = body_source[start:end].strip() + "\n"
        heading = token.group(1)
        if heading.startswith("# Part "):
            part_count += 1
            title = heading.removeprefix("# Part ").strip()
            filename = f"part-{part_count:03d}-{slugify(title)}.md"
            (chapters_dir / filename).write_text(body, encoding="utf-8")
        else:
            chapter_count += 1
            chapter_no = int(token.group(2))
            title = token.group(3).strip()
            filename = f"chapter-{chapter_no:03d}-{slugify(title)}.md"
            (chapters_dir / filename).write_text(body, encoding="utf-8")

    if back_matter_match:
        back_matter = text[back_matter_match.start() :].strip() + "\n"
        (chapters_dir / "999-back-matter.md").write_text(back_matter, encoding="utf-8")

    return chapter_count


def main() -> None:
    for book_dir in sorted(p for p in OUTPUT.iterdir() if p.is_dir() and p.name.startswith("book-")):
        count = split_book(book_dir)
        print(f"{book_dir.name}: {count} chapters")


if __name__ == "__main__":
    main()
