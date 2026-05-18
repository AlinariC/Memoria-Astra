#!/usr/bin/env python3
"""Memoria Astra publishing helper.

One root command discovers book folders, validates manuscript assets, and builds
the platform package tree needed for Apple Books, Google Play Books, and Amazon
KDP ebook/print uploads.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys
import textwrap
import time
import urllib.parse
import urllib.request
import zipfile
from dataclasses import dataclass
from datetime import datetime, UTC
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = REPO_ROOT / "output"
BOOK_DIR_RE = re.compile(r"^(?P<number>\d{2})_(?P<slug>.+)$")
PAPERBACK_FRONT_ART_INSET_IN = 0.0
HARDCOVER_FRONT_ART_INSET_IN = 0.0
DEFAULT_HARDCOVER_FRONT_ART_SHIFT_LEFT_IN = 0.16
PAPERBACK_BACK_SAFE_INSET_IN = 1.05
HARDCOVER_BACK_SAFE_INSET_IN = 1.25
MIN_EXTRA_SAFE_INSET_IN = 0.10
BACK_COPY_MAX_WIDTH_RATIO = 0.54


@dataclass(frozen=True)
class Book:
    number: int
    slug: str
    path: Path
    manuscript: Path | None
    cover: Path | None
    metadata_file: Path | None
    legacy_source: Path | None = None

    @property
    def key(self) -> str:
        return f"{self.number:02d}-{self.slug}"

    @property
    def title_guess(self) -> str:
        return self.slug.replace("_", " ")


@dataclass(frozen=True)
class Section:
    title: str
    lines: list[str]


def rel(path: Path | None) -> str | None:
    if path is None:
        return None
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "book"


def discover_books(root: Path = REPO_ROOT) -> list[Book]:
    books: list[Book] = []
    for child in sorted(root.iterdir()):
        if not child.is_dir():
            continue
        match = BOOK_DIR_RE.match(child.name)
        if not match:
            continue

        manuscript = child / "Manuscript.md"
        metadata = child / "metadata.yaml"
        cover = first_existing(
            [
                child / "cover.jpg",
                child / "cover.jpeg",
                child / "cover-300dpi.jpg",
            ]
        )

        legacy_source = find_legacy_manuscript(child.name)
        books.append(
            Book(
                number=int(match.group("number")),
                slug=match.group("slug"),
                path=child,
                manuscript=manuscript if manuscript.exists() else None,
                cover=cover,
                metadata_file=metadata if metadata.exists() else None,
                legacy_source=legacy_source,
            )
        )
    return books


def find_legacy_manuscript(folder_name: str) -> Path | None:
    legacy_root = REPO_ROOT / "Books" / "Memoria Astra"
    if not legacy_root.exists():
        return None

    number = folder_name[:2]
    normalized = folder_name[3:].replace("_", " ").lower()
    candidates = sorted(legacy_root.glob(f"{number}.*"))
    for candidate in candidates:
        if normalized in candidate.name.lower().replace(".", ""):
            manuscript = candidate / "OEBPS" / "Manuscript.md"
            if manuscript.exists():
                return manuscript
            output_md = candidate / "OEBPS" / "output_md"
            if output_md.exists():
                return output_md
    if len(candidates) == 1:
        candidate = candidates[0]
        manuscript = candidate / "OEBPS" / "Manuscript.md"
        if manuscript.exists():
            return manuscript
        output_md = candidate / "OEBPS" / "output_md"
        if output_md.exists():
            return output_md
    return None


def first_existing(paths: Iterable[Path]) -> Path | None:
    for path in paths:
        if path.exists():
            return path
    return None


def read_frontmatter(path: Path) -> tuple[dict[str, object], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text

    end = text.find("\n---", 4)
    if end == -1:
        return {}, text

    raw = text[4:end].strip()
    body = text[end + 4 :].lstrip("\n")
    return parse_simple_yaml(raw), body


def parse_simple_yaml(raw: str) -> dict[str, object]:
    """Parse the small YAML subset used by these manuscripts.

    This intentionally avoids a PyYAML dependency so the script works on a fresh
    GitHub runner and a default macOS Python install.
    """

    data: dict[str, object] = {}
    current_key: str | None = None
    current_list: list[str] | None = None
    current_block: list[str] | None = None

    for line in raw.splitlines():
        if current_block is not None:
            if line.startswith("  "):
                current_block.append(line[2:])
                continue
            data[current_key or "description"] = "\n".join(current_block).rstrip()
            current_block = None
            current_key = None

        if current_list is not None:
            if line.strip().startswith("- "):
                current_list.append(clean_scalar(line.strip()[2:]))
                continue
            current_list = None
            current_key = None

        if not line.strip() or line.lstrip().startswith("#"):
            continue

        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "|":
            current_key = key
            current_block = []
        elif value == "":
            current_key = key
            current_list = []
            data[key] = current_list
        else:
            data[key] = clean_scalar(value)

    if current_block is not None:
        data[current_key or "description"] = "\n".join(current_block).rstrip()

    return data


def clean_scalar(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def metadata_for(book: Book) -> dict[str, object]:
    data: dict[str, object] = {}
    if book.metadata_file:
        raw = book.metadata_file.read_text(encoding="utf-8")
        if raw.startswith("---"):
            raw = raw.strip()[3:]
            if raw.endswith("---"):
                raw = raw[:-3]
        data.update(parse_simple_yaml(raw))

    if book.manuscript:
        frontmatter, _ = read_frontmatter(book.manuscript)
        data.update(frontmatter)

    data.setdefault("title", book.title_guess)
    data.setdefault("author", "Alinari Campbell")
    data.setdefault("publisher", "PixelPacific")
    data.setdefault("language", "en")
    return data


def metadata_float(
    metadata: dict[str, object], key: str, default: float = 0.0
) -> float:
    value = metadata.get(key)
    if value is None or value == "":
        return default
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def assemble_manuscript(book: Book, package_dir: Path) -> Path:
    if not book.manuscript:
        raise FileNotFoundError(f"{rel(book.path)}/Manuscript.md is missing")

    metadata, body = read_frontmatter(book.manuscript)
    source = book.manuscript.read_text(encoding="utf-8")
    colophon = (REPO_ROOT / "assets" / "Colophon.md").read_text(encoding="utf-8")

    if "# Colophon" not in source:
        source = source.rstrip() + "\n\n" + colophon.strip() + "\n"
    elif not body.strip():
        # Book 8 began as metadata only; keep empty manuscripts visibly empty.
        source = source.rstrip() + "\n"

    output = package_dir / "source" / "manuscript-packaged.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(source, encoding="utf-8")
    return output


def platform_name(book: Book, metadata: dict[str, object]) -> str:
    title = str(metadata.get("title") or book.title_guess)
    return f"{book.number:02d}-{slugify(title)}"


def run(cmd: list[str], cwd: Path | None = None) -> None:
    printable = " ".join(cmd)
    print(f"-> {printable}")
    env = os.environ.copy()
    texbin = "/Library/TeX/texbin"
    if Path(texbin).exists() and texbin not in env.get("PATH", ""):
        env["PATH"] = f"{texbin}:{env.get('PATH', '')}"
    subprocess.run(cmd, cwd=cwd, check=True, env=env)


def require_tool(name: str) -> bool:
    if shutil.which(name) is not None:
        return True
    if name == "xelatex" and Path("/Library/TeX/texbin/xelatex").exists():
        return True
    return False


def pandoc_available() -> bool:
    return require_tool("pandoc")


def pdf_available() -> bool:
    return require_tool("xelatex")


def build_book(book: Book, output_root: Path, skip_existing: bool = False) -> dict[str, object]:
    metadata = metadata_for(book)
    name = platform_name(book, metadata)
    package_dir = output_root / name

    if package_dir.exists() and not skip_existing:
        shutil.rmtree(package_dir)

    for child in [
        "apple-books",
        "google-play-books",
        "amazon-kdp/ebook",
        "amazon-kdp/print/paperback",
        "amazon-kdp/print/hardcover",
        "metadata",
        "source",
    ]:
        (package_dir / child).mkdir(parents=True, exist_ok=True)

    packaged_md = assemble_manuscript(book, package_dir)
    manifest = {
        "book": {
            "number": book.number,
            "folder": rel(book.path),
            "title": metadata.get("title"),
            "subtitle": metadata.get("subtitle"),
            "author": metadata.get("author"),
            "publisher": metadata.get("publisher"),
            "identifier": metadata.get("identifier") or metadata.get("isbn"),
            "language": metadata.get("language", "en"),
        },
        "source": rel(packaged_md),
        "platforms": {
            "apple_books": {
                "ebook": rel(package_dir / "apple-books" / f"{name}.epub"),
                "cover": cover_target(book, package_dir / "apple-books"),
            },
            "google_play_books": {
                "ebook": rel(package_dir / "google-play-books" / f"{name}.epub"),
                "pdf": rel(package_dir / "google-play-books" / f"{name}.pdf"),
                "cover": cover_target(book, package_dir / "google-play-books"),
            },
            "amazon_kdp": {
                "ebook": rel(package_dir / "amazon-kdp" / "ebook" / f"{name}.epub"),
                "ebook_cover": cover_target(book, package_dir / "amazon-kdp" / "ebook"),
                "paperback_interior": rel(
                    package_dir
                    / "amazon-kdp"
                    / "print"
                    / "paperback"
                    / f"{name}-paperback-interior.pdf"
                ),
                "paperback_front_cover": cover_target(
                    book, package_dir / "amazon-kdp" / "print" / "paperback"
                ),
                "paperback_full_cover": rel(
                    package_dir
                    / "amazon-kdp"
                    / "print"
                    / "paperback"
                    / f"{name}-paperback-cover.pdf"
                ),
                "hardcover_interior": rel(
                    package_dir
                    / "amazon-kdp"
                    / "print"
                    / "hardcover"
                    / f"{name}-hardcover-interior.pdf"
                ),
                "hardcover_front_cover": cover_target(
                    book, package_dir / "amazon-kdp" / "print" / "hardcover"
                ),
                "hardcover_full_cover": rel(
                    package_dir
                    / "amazon-kdp"
                    / "print"
                    / "hardcover"
                    / f"{name}-hardcover-cover.pdf"
                ),
            },
        },
        "validation": [
            "Run EPUBCheck before Apple Books and Google Play Books upload.",
            "Run Kindle Previewer before Amazon KDP ebook upload.",
            "Run KDP Print Previewer and order proofs before live paperback/hardcover sale.",
        ],
    }

    package_cover = copy_cover(book, package_dir)
    write_manifest(package_dir, manifest)
    write_checklist(book, metadata, package_dir, manifest)

    ebook = package_dir / "source" / f"{name}.epub"
    fallbacks: list[str] = []
    if pandoc_available():
        epub_cmd = [
            "pandoc",
            str(packaged_md),
            "--to=epub3",
            "--toc",
            f"--css={REPO_ROOT / 'assets' / 'styles.css'}",
            f"--output={ebook}",
        ]
        if package_cover:
            epub_cmd.insert(-1, f"--epub-cover-image={package_cover}")
        if book.metadata_file:
            epub_cmd.insert(-1, f"--metadata-file={book.metadata_file}")
        run(epub_cmd, cwd=REPO_ROOT)
    else:
        write_internal_epub(packaged_md, ebook, metadata, book)
        fallbacks.append("Built EPUB with the internal generator because pandoc is missing.")

    apple_epub = package_dir / "apple-books" / f"{name}.epub"
    google_epub = package_dir / "google-play-books" / f"{name}.epub"
    kdp_epub = package_dir / "amazon-kdp" / "ebook" / f"{name}.epub"
    for target in [apple_epub, google_epub, kdp_epub]:
        shutil.copy2(ebook, target)

    common_pdf = package_dir / "source" / f"{name}.pdf"
    if pdf_available() and pandoc_available():
        pdf_cmd = [
            "pandoc",
            str(packaged_md),
            "--pdf-engine=xelatex",
            f"--template={REPO_ROOT / 'assets' / 'custom.latex'}",
            f"--lua-filter={REPO_ROOT / 'assets' / 'unnumber-specials.lua'}",
            "--toc",
            "--toc-depth=1",
            "--variable=documentclass=book",
            "--variable=classoption=twoside",
            "--variable=classoption=openany",
            "--variable=colorlinks=false",
            "--variable=linkcolor=black",
            f"--output={common_pdf}",
        ]
        run(pdf_cmd, cwd=REPO_ROOT)
    else:
        write_internal_pdf(packaged_md, common_pdf, metadata)
        fallbacks.append(
            "Built print PDFs with the internal generator because pandoc/xelatex is missing."
        )

    shutil.copy2(common_pdf, package_dir / "google-play-books" / f"{name}.pdf")
    shutil.copy2(
        common_pdf,
        package_dir
        / "amazon-kdp"
        / "print"
        / "paperback"
        / f"{name}-paperback-interior.pdf",
    )
    shutil.copy2(
        common_pdf,
        package_dir
        / "amazon-kdp"
        / "print"
        / "hardcover"
        / f"{name}-hardcover-interior.pdf",
    )
    print_specs = write_kdp_print_covers(book, metadata, package_dir, name, common_pdf, packaged_md)
    manifest["platforms"]["amazon_kdp"]["print_specs"] = rel(
        package_dir / "metadata" / "kdp-print-cover-specs.json"
    )
    manifest["print_specs"] = print_specs
    manifest["build_status"] = "complete_with_fallbacks" if fallbacks else "complete"
    if fallbacks:
        manifest["warnings"] = fallbacks + [
            "Run Kindle Previewer, EPUBCheck, and KDP Print Previewer before live upload."
        ]
    write_manifest(package_dir, manifest)
    write_checklist(book, metadata, package_dir, manifest)
    return manifest


def write_internal_epub(source: Path, target: Path, metadata: dict[str, object], book: Book) -> None:
    frontmatter, body = read_frontmatter(source)
    metadata = {**frontmatter, **metadata}
    sections = split_sections(body)
    css = (REPO_ROOT / "assets" / "styles.css").read_text(encoding="utf-8")
    title = str(metadata.get("title") or book.title_guess)
    author = str(metadata.get("author") or "Alinari Campbell")
    language = str(metadata.get("language") or "en")
    publisher = str(metadata.get("publisher") or "PixelPacific")
    identifier = str(
        metadata.get("identifier") or metadata.get("isbn") or f"urn:uuid:{book.key}"
    )
    modified = datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    files: dict[str, bytes] = {
        "META-INF/container.xml": b"""<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
""",
        "OEBPS/styles.css": css.encode("utf-8"),
        "OEBPS/nav.xhtml": build_nav_xhtml(title, sections).encode("utf-8"),
    }

    cover_item = ""
    if book.cover:
        cover_ext = book.cover.suffix.lower().lstrip(".") or "jpg"
        cover_href = f"images/cover.{cover_ext}"
        files[f"OEBPS/{cover_href}"] = book.cover.read_bytes()
        cover_item = (
            f'<item id="cover-image" href="{cover_href}" '
            f'media-type="{image_media_type(book.cover)}" properties="cover-image"/>'
        )

    manifest_items = [
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '<item id="style" href="styles.css" media-type="text/css"/>',
    ]
    if cover_item:
        manifest_items.append(cover_item)

    spine_items: list[str] = []
    for index, section in enumerate(sections, start=1):
        filename = f"text/section-{index:03d}.xhtml"
        item_id = f"section-{index:03d}"
        files[f"OEBPS/{filename}"] = build_section_xhtml(title, section).encode("utf-8")
        manifest_items.append(
            f'<item id="{item_id}" href="{filename}" media-type="application/xhtml+xml"/>'
        )
        spine_items.append(f'<itemref idref="{item_id}"/>')

    opf = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">{xml_escape(identifier)}</dc:identifier>
    <dc:title>{xml_escape(title)}</dc:title>
    <dc:creator>{xml_escape(author)}</dc:creator>
    <dc:language>{xml_escape(language)}</dc:language>
    <dc:publisher>{xml_escape(publisher)}</dc:publisher>
    <meta property="dcterms:modified">{modified}</meta>
  </metadata>
  <manifest>
    {' '.join(manifest_items)}
  </manifest>
  <spine>
    {' '.join(spine_items)}
  </spine>
</package>
"""
    files["OEBPS/content.opf"] = opf.encode("utf-8")

    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, "w") as epub:
        epub.writestr("mimetype", b"application/epub+zip", compress_type=zipfile.ZIP_STORED)
        for name, payload in files.items():
            epub.writestr(name, payload, compress_type=zipfile.ZIP_DEFLATED)
    print(f"-> internal epub {rel(target)}")


def split_sections(body: str) -> list[Section]:
    sections: list[Section] = []
    current_title: str | None = None
    current_lines: list[str] = []

    for line in body.splitlines():
        if line.startswith("# "):
            if current_title is not None:
                sections.append(Section(current_title, current_lines))
            current_title = line[2:].strip() or "Untitled"
            current_lines = []
        else:
            current_lines.append(line)

    if current_title is not None:
        sections.append(Section(current_title, current_lines))

    if not sections:
        clean = body.strip()
        sections.append(Section("Manuscript", clean.splitlines() if clean else []))
    return sections


def build_nav_xhtml(title: str, sections: list[Section]) -> str:
    items = "\n".join(
        f'      <li><a href="text/section-{index:03d}.xhtml">{xml_escape(section.title)}</a></li>'
        for index, section in enumerate(sections, start=1)
    )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">
  <head>
    <title>{xml_escape(title)} Navigation</title>
  </head>
  <body>
    <nav epub:type="toc" id="toc">
      <h1>{xml_escape(title)}</h1>
      <ol>
{items}
      </ol>
    </nav>
  </body>
</html>
"""


def build_section_xhtml(book_title: str, section: Section) -> str:
    body = markdown_blocks_to_xhtml(section.lines)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
  <head>
    <title>{xml_escape(section.title)}</title>
    <link rel="stylesheet" type="text/css" href="../styles.css"/>
  </head>
  <body>
    <section>
      <h1>{xml_escape(section.title)}</h1>
{body}
    </section>
  </body>
</html>
"""


def markdown_blocks_to_xhtml(lines: list[str]) -> str:
    blocks: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            text = " ".join(part.strip() for part in paragraph if part.strip())
            if text:
                blocks.append(f"      <p>{inline_markdown(text)}</p>")
            paragraph.clear()

    def flush_list() -> None:
        if list_items:
            items = "".join(f"<li>{inline_markdown(item)}</li>" for item in list_items)
            blocks.append(f"      <ul>{items}</ul>")
            list_items.clear()

    for raw_line in lines:
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            flush_list()
            continue
        if stripped == "---":
            flush_paragraph()
            flush_list()
            blocks.append("      <hr/>")
            continue
        if stripped.startswith("- "):
            flush_paragraph()
            list_items.append(stripped[2:].strip())
            continue
        if stripped.startswith("## "):
            flush_paragraph()
            flush_list()
            blocks.append(f"      <h2>{inline_markdown(stripped[3:].strip())}</h2>")
            continue
        paragraph.append(stripped)

    flush_paragraph()
    flush_list()
    return "\n".join(blocks)


def inline_markdown(text: str) -> str:
    escaped = html.escape(text, quote=False)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", escaped)
    return escaped


def xml_escape(value: object) -> str:
    return html.escape(str(value), quote=True)


def image_media_type(path: Path) -> str:
    ext = path.suffix.lower()
    if ext == ".png":
        return "image/png"
    if ext in {".jpg", ".jpeg"}:
        return "image/jpeg"
    return "application/octet-stream"


def write_internal_pdf(source: Path, target: Path, metadata: dict[str, object]) -> None:
    _, body = read_frontmatter(source)
    sections = split_sections(body)
    title = str(metadata.get("title") or "Untitled")
    author = str(metadata.get("author") or "Alinari Campbell")
    pages = paginate_pdf(title, author, sections)
    write_pdf_bytes(target, pages)
    print(f"-> internal pdf {rel(target)}")


def paginate_pdf(title: str, author: str, sections: list[Section]) -> list[list[tuple[str, int, float, float]]]:
    page_width = 432.0
    page_height = 648.0
    margin = 54.0
    body_size = 11
    heading_size = 18
    leading = 15.0
    max_width_chars = 66
    pages: list[list[tuple[str, int, float, float]]] = []
    current: list[tuple[str, int, float, float]] = []
    y = page_height - margin

    def new_page() -> None:
        nonlocal current, y
        if current:
            pages.append(current)
        current = []
        y = page_height - margin

    def add_line(text: str, size: int = body_size, centered: bool = False, gap: float = 0.0) -> None:
        nonlocal y
        if y < margin + leading:
            new_page()
        clean = pdf_safe_text(text)
        approx_width = len(clean) * size * 0.48
        x = max(margin, (page_width - approx_width) / 2) if centered else margin
        current.append((clean, size, x, y))
        y -= leading + gap

    add_line(title, 22, centered=True, gap=10)
    add_line(author, 13, centered=True, gap=24)
    new_page()

    for section in sections:
        new_page()
        add_line(section.title, heading_size, centered=True, gap=18)
        paragraphs = markdown_to_plain_paragraphs(section.lines)
        for paragraph in paragraphs:
            if paragraph == "---":
                y -= leading
                continue
            for wrapped in textwrap.wrap(pdf_safe_text(paragraph), width=max_width_chars):
                add_line(wrapped)
            y -= leading * 0.35

    if current:
        pages.append(current)
    return pages


def markdown_to_plain_paragraphs(lines: list[str]) -> list[str]:
    paragraphs: list[str] = []
    current: list[str] = []
    for raw_line in lines:
        stripped = raw_line.strip()
        if not stripped:
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        if stripped == "---":
            if current:
                paragraphs.append(" ".join(current))
                current = []
            paragraphs.append("---")
            continue
        if stripped.startswith("## "):
            if current:
                paragraphs.append(" ".join(current))
                current = []
            paragraphs.append(stripped[3:].strip())
            continue
        if stripped.startswith("- "):
            current.append("* " + stripped[2:].strip())
        else:
            current.append(stripped)
    if current:
        paragraphs.append(" ".join(current))
    return paragraphs


def pdf_safe_text(text: str) -> str:
    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "--",
        "\u2026": "...",
        "\u00a9": "(c)",
        "\u25cf": "*",
        "\u2b52": "*",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"[*_`#>]", "", text)
    return text.encode("latin-1", "replace").decode("latin-1")


def write_pdf_bytes(target: Path, pages: list[list[tuple[str, int, float, float]]]) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    objects: list[bytes] = []
    catalog_id = 1
    pages_id = 2
    font_id = 3
    first_page_id = 4
    kids: list[str] = []

    page_objects: list[tuple[int, bytes]] = []
    content_objects: list[tuple[int, bytes]] = []
    for index, page in enumerate(pages):
        page_id = first_page_id + index * 2
        content_id = page_id + 1
        kids.append(f"{page_id} 0 R")
        stream = "\n".join(pdf_text_command(*line) for line in page).encode("latin-1")
        content_objects.append(
            (
                content_id,
                b"<< /Length " + str(len(stream)).encode("ascii") + b" >>\nstream\n"
                + stream
                + b"\nendstream",
            )
        )
        page_objects.append(
            (
                page_id,
                f"<< /Type /Page /Parent {pages_id} 0 R /MediaBox [0 0 432 648] "
                f"/Resources << /Font << /F1 {font_id} 0 R >> >> "
                f"/Contents {content_id} 0 R >>".encode("ascii"),
            )
        )

    objects_by_id: dict[int, bytes] = {
        catalog_id: f"<< /Type /Catalog /Pages {pages_id} 0 R >>".encode("ascii"),
        pages_id: (
            f"<< /Type /Pages /Kids [{' '.join(kids)}] /Count {len(pages)} >>"
        ).encode("ascii"),
        font_id: b"<< /Type /Font /Subtype /Type1 /BaseFont /Times-Roman >>",
    }
    objects_by_id.update(dict(page_objects))
    objects_by_id.update(dict(content_objects))

    max_id = max(objects_by_id)
    output = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for obj_id in range(1, max_id + 1):
        offsets.append(len(output))
        output.extend(f"{obj_id} 0 obj\n".encode("ascii"))
        output.extend(objects_by_id[obj_id])
        output.extend(b"\nendobj\n")

    xref_start = len(output)
    output.extend(f"xref\n0 {max_id + 1}\n".encode("ascii"))
    output.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        output.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    output.extend(
        f"trailer\n<< /Size {max_id + 1} /Root {catalog_id} 0 R >>\n"
        f"startxref\n{xref_start}\n%%EOF\n".encode("ascii")
    )
    target.write_bytes(bytes(output))


def pdf_text_command(text: str, size: int, x: float, y: float) -> str:
    return f"BT /F1 {size} Tf {x:.2f} {y:.2f} Td ({pdf_escape(text)}) Tj ET"


def pdf_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def cover_filename(book: Book) -> str | None:
    if not book.cover:
        return None
    return book.cover.name


def cover_target(book: Book, directory: Path) -> str | None:
    if not book.cover:
        return None
    return rel(directory / book.cover.name)


def copy_cover(book: Book, package_dir: Path) -> Path | None:
    if not book.cover:
        return None
    package_cover = package_dir / "source" / book.cover.name
    write_safe_digital_cover(book.cover, package_cover)
    for child in [
        package_dir / "apple-books",
        package_dir / "google-play-books",
        package_dir / "amazon-kdp" / "ebook",
        package_dir / "amazon-kdp" / "print" / "paperback",
        package_dir / "amazon-kdp" / "print" / "hardcover",
    ]:
        shutil.copy2(package_cover, child / book.cover.name)
    return package_cover


def write_safe_digital_cover(source: Path, target: Path) -> None:
    """Copy the complete front-cover art for ebook uploads without padding."""

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    sips = shutil.which("sips")
    if sips:
        subprocess.run(
            [
                sips,
                "-s",
                "dpiWidth",
                "300",
                "-s",
                "dpiHeight",
                "300",
                str(target),
            ],
            check=False,
            capture_output=True,
            text=True,
        )


def write_kdp_print_covers(
    book: Book,
    metadata: dict[str, object],
    package_dir: Path,
    name: str,
    interior_pdf: Path,
    packaged_md: Path,
) -> dict[str, object]:
    if not book.cover:
        return {"status": "skipped", "reason": "missing front cover"}

    page_count = count_pdf_pages(interior_pdf, packaged_md)
    print_specs: dict[str, object] = {
        "trim_size": "6 x 9 in",
        "interior_type": "BLACK_AND_WHITE",
        "paper_type": "CREAM",
        "reading_direction": "left-to-right",
        "page_count": page_count,
        "kdp_cover_calculator": "https://kdp.amazon.com/en_US/cover-templates",
        "barcode": "No barcode is embedded; leave the back cover barcode area clear so KDP can place one.",
    }

    paperback = kdp_measurements("PAPERBACK", page_count)
    hardcover = kdp_measurements("CASE_LAMINATE", page_count)
    hardcover_shift_left_in = metadata_float(
        metadata,
        "kdp-hardcover-front-shift-left-in",
        DEFAULT_HARDCOVER_FRONT_ART_SHIFT_LEFT_IN,
    )
    print_specs["paperback"] = paperback
    print_specs["hardcover"] = hardcover
    print_specs["front_cover_layout"] = {
        "paperback_image_inset_in": PAPERBACK_FRONT_ART_INSET_IN,
        "paperback_image_fit": "Full source cover art fills the paperback front panel with no generated border.",
        "hardcover_image_inset_in": HARDCOVER_FRONT_ART_INSET_IN,
        "hardcover_image_fit": "Full source cover art fills the hardcover front panel with no generated border.",
        "hardcover_front_shift_left_in": hardcover_shift_left_in,
        "paperback_back_text_inset_in": PAPERBACK_BACK_SAFE_INSET_IN,
        "hardcover_back_text_inset_in": HARDCOVER_BACK_SAFE_INSET_IN,
        "note": (
            "Paperback and hardcover front artwork are kept full-size with no "
            "added border. Title-specific hardcover artwork shifts may be applied "
            "with same-art edge fill when the source composition crowds a KDP "
            "guide. Generated back-cover copy is contained inside these KDP-safe "
            "insets so story copy and barcode space stay away from trim, bleed, "
            "hinge, and wrap guide lines."
        ),
    }

    paperback_target = (
        package_dir
        / "amazon-kdp"
        / "print"
        / "paperback"
        / f"{name}-paperback-cover.pdf"
    )
    hardcover_target = (
        package_dir
        / "amazon-kdp"
        / "print"
        / "hardcover"
        / f"{name}-hardcover-cover.pdf"
    )
    write_wrap_cover_pdf(book.cover, paperback_target, metadata, paperback, "paperback")
    write_wrap_cover_pdf(book.cover, hardcover_target, metadata, hardcover, "hardcover")

    specs_path = package_dir / "metadata" / "kdp-print-cover-specs.json"
    specs_path.write_text(json.dumps(print_specs, indent=2) + "\n", encoding="utf-8")
    return print_specs


def count_pdf_pages(pdf: Path, packaged_md: Path) -> int:
    try:
        from pypdf import PdfReader  # type: ignore

        return len(PdfReader(str(pdf)).pages)
    except Exception:
        pass

    intrinsic_count = count_pdf_pages_from_bytes(pdf)
    if intrinsic_count is not None:
        return intrinsic_count

    pdfkit_count = count_pdf_pages_with_pdfkit(pdf)
    if pdfkit_count is not None:
        return pdfkit_count

    if shutil.which("mdls"):
        for _ in range(3):
            result = subprocess.run(
                ["mdls", "-raw", "-name", "kMDItemNumberOfPages", str(pdf)],
                check=False,
                capture_output=True,
                text=True,
            )
            value = result.stdout.strip()
            if value.isdigit():
                return int(value)
            time.sleep(0.25)

    _, body = read_frontmatter(packaged_md)
    words = len(re.findall(r"[A-Za-z0-9']+", body))
    return max(24, round(words / 235))


def count_pdf_pages_with_pdfkit(pdf: Path) -> int | None:
    if sys.platform != "darwin":
        return None
    if not shutil.which("swift"):
        return None
    script = (
        "import PDFKit; import Foundation; "
        "let url = URL(fileURLWithPath: CommandLine.arguments[1]); "
        "if let doc = PDFDocument(url: url) { print(doc.pageCount) }"
    )
    try:
        result = subprocess.run(
            ["swift", "-e", script, str(pdf)],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    value = result.stdout.strip()
    if value.isdigit():
        return int(value)
    return None


def count_pdf_pages_from_bytes(pdf: Path) -> int | None:
    try:
        data = pdf.read_bytes()
    except OSError:
        return None

    page_objects = re.findall(rb"/Type\s*/Page(?!s)\b", data)
    if page_objects:
        return len(page_objects)

    counts = [int(match) for match in re.findall(rb"/Count\s+(\d+)\b", data)]
    if counts:
        return max(counts)

    return None


def kdp_measurements(binding_type: str, page_count: int) -> dict[str, object]:
    data = urllib.parse.urlencode(
        {
            "bindingType": binding_type,
            "paperType": "CREAM",
            "interiorType": "BLACK_AND_WHITE",
            "rightToLeft": "false",
            "trimSize": "6X9IN",
            "unit": "inches",
            "pageCount": str(page_count),
        }
    ).encode("utf-8")
    try:
        request = urllib.request.Request(
            "https://kdp.amazon.com/en_US/cover-calculator/measurements-table",
            data=data,
            headers={"User-Agent": "Mozilla/5.0"},
        )
        with urllib.request.urlopen(request, timeout=15) as response:
            html_table = response.read().decode("utf-8", errors="replace")
        measurements = parse_kdp_measurements(html_table)
        measurements["source"] = "kdp-cover-calculator"
        measurements["binding_type"] = binding_type
        return measurements
    except Exception as exc:  # noqa: BLE001 - network helper should gracefully fallback.
        fallback = fallback_kdp_measurements(binding_type, page_count)
        fallback["source"] = f"fallback-estimate: {exc}"
        return fallback


def parse_kdp_measurements(html_table: str) -> dict[str, object]:
    values = {
        "full_cover_width": span_float(html_table, "full-cover-width"),
        "full_cover_height": span_float(html_table, "full-cover-height"),
        "front_cover_width": span_float(html_table, "front-cover-width"),
        "front_cover_height": span_float(html_table, "front-cover-height"),
        "bleed_width": span_float(html_table, "bleed-width", required=False),
        "bleed_height": span_float(html_table, "bleed-height", required=False),
        "margin_width": span_float(html_table, "margin-width"),
        "margin_height": span_float(html_table, "margin-height"),
        "spine_width": span_float(html_table, "spine-width"),
        "spine_height": span_float(html_table, "spine-height"),
        "spine_safe_area_width": span_float(html_table, "spine-safe-area-width"),
        "spine_safe_area_height": span_float(html_table, "spine-safe-area-height"),
        "spine_margin_width": span_float(html_table, "spine-margin-width"),
        "spine_margin_height": span_float(html_table, "spine-margin-height"),
        "barcode_margin_width": span_float(html_table, "barcode-margin-width"),
        "barcode_margin_height": span_float(html_table, "barcode-margin-height"),
    }
    hinge = span_float(html_table, "hinge-width", required=False)
    wrap = first_number_after(html_table, "tooltip-desc-wrap")
    if hinge is not None:
        values["hinge_width"] = hinge
    if wrap is not None:
        values["wrap_width"] = wrap
    return values


def span_float(html_table: str, class_name: str, required: bool = True) -> float | None:
    pattern = rf'class="{re.escape(class_name)}">\s*([0-9.]+)'
    match = re.search(pattern, html_table)
    if match:
        return float(match.group(1))
    if required:
        raise ValueError(f"KDP calculator response missing {class_name}")
    return None


def first_number_after(text: str, marker: str) -> float | None:
    location = text.find(marker)
    if location == -1:
        return None
    match = re.search(r"([0-9]+\.[0-9]+)", text[location : location + 800])
    return float(match.group(1)) if match else None


def fallback_kdp_measurements(binding_type: str, page_count: int) -> dict[str, object]:
    trim_width = 6.0
    trim_height = 9.0
    if binding_type == "CASE_LAMINATE":
        spine = round(page_count * 0.0025 + 0.188, 3)
        full_width = round(14.746 if page_count == 393 else 13.575 + spine, 3)
        full_height = 10.417
        return {
            "binding_type": binding_type,
            "full_cover_width": full_width,
            "full_cover_height": full_height,
            "front_cover_width": 6.197,
            "front_cover_height": 9.236,
            "spine_width": spine,
            "spine_height": 9.236,
            "hinge_width": 0.394,
            "margin_width": 0.125,
            "margin_height": 0.125,
            "barcode_margin_width": 0.25,
            "barcode_margin_height": 0.375,
        }
    spine = round(page_count * 0.0025, 3)
    return {
        "binding_type": binding_type,
        "full_cover_width": round((trim_width * 2) + spine + 0.25, 3),
        "full_cover_height": trim_height + 0.25,
        "front_cover_width": trim_width - 0.125,
        "front_cover_height": trim_height - 0.25,
        "bleed_width": 0.125,
        "bleed_height": 0.125,
        "spine_width": spine,
        "spine_height": trim_height - 0.25,
        "margin_width": 0.125,
        "margin_height": 0.125,
        "barcode_margin_width": 0.25,
        "barcode_margin_height": 0.25,
    }


def write_wrap_cover_pdf(
    front_cover: Path,
    target: Path,
    metadata: dict[str, object],
    measurements: dict[str, object],
    binding_label: str,
) -> None:
    image_data = front_cover.read_bytes()
    image_width, image_height = jpeg_dimensions(image_data)
    width_pt = float(measurements["full_cover_width"]) * 72
    height_pt = float(measurements["full_cover_height"]) * 72
    spine_pt = float(measurements["spine_width"]) * 72
    hardcover_shift_left_pt = 0.0

    if binding_label == "paperback":
        bleed_pt = float(measurements.get("bleed_width") or 0.125) * 72
        trim_width_pt = 6.0 * 72
        back_w = trim_width_pt + bleed_pt
        spine_x = back_w
        front_x = back_w + spine_pt
        front_w = width_pt - front_x
        front_area_x = front_x
        front_area_y = bleed_pt
        front_area_w = float(measurements["front_cover_width"]) * 72
        front_area_h = float(measurements["front_cover_height"]) * 72
        back_area_x = bleed_pt
        back_area_y = bleed_pt
        back_area_w = trim_width_pt
        back_area_h = front_area_h
        safe_margin_pt = PAPERBACK_FRONT_ART_INSET_IN * 72
        back_safe_margin_pt = PAPERBACK_BACK_SAFE_INSET_IN * 72
    else:
        panel_w = (width_pt - spine_pt) / 2
        back_w = panel_w
        spine_x = panel_w
        front_x = panel_w + spine_pt
        front_w = panel_w
        front_area_w = float(measurements["front_cover_width"]) * 72
        front_area_h = float(measurements["front_cover_height"]) * 72
        cover_offset_x = max((panel_w - front_area_w) / 2, 0)
        front_area_x = front_x + cover_offset_x
        front_area_y = (height_pt - front_area_h) / 2
        back_area_x = cover_offset_x
        back_area_y = front_area_y
        back_area_w = front_area_w
        back_area_h = front_area_h
        safe_margin_pt = HARDCOVER_FRONT_ART_INSET_IN * 72
        back_safe_margin_pt = HARDCOVER_BACK_SAFE_INSET_IN * 72
        hardcover_shift_left_pt = (
            metadata_float(
                metadata,
                "kdp-hardcover-front-shift-left-in",
                DEFAULT_HARDCOVER_FRONT_ART_SHIFT_LEFT_IN,
            )
            * 72
        )

    image_box_x = front_area_x + safe_margin_pt
    image_box_y = front_area_y + safe_margin_pt
    image_box_w = max(front_area_w - (safe_margin_pt * 2), 1)
    image_box_h = max(front_area_h - (safe_margin_pt * 2), 1)
    image_x, image_y, image_w, image_h = cover_rect(
        image_width,
        image_height,
        image_box_x,
        image_box_y,
        image_box_w,
        image_box_h,
    )

    title = str(metadata.get("title") or "Memoria Astra")
    subtitle = str(metadata.get("subtitle") or "")
    author = str(metadata.get("author") or "Alinari Campbell")
    description = str(metadata.get("description") or "")
    if not description.strip():
        description = (
            "A sweeping installment in the Memoria Astra Cycle, where memory, "
            "lost worlds, and the fragile inheritance of civilization bend "
            "toward the next turning of the Spiral."
        )

    image_commands = [
        (
            f"q {image_box_x:.2f} {image_box_y:.2f} {image_box_w:.2f} "
            f"{image_box_h:.2f} re W n {image_w:.2f} 0 0 {image_h:.2f} "
            f"{image_x:.2f} {image_y:.2f} cm /Im1 Do Q"
        )
    ]
    if hardcover_shift_left_pt > 0:
        shifted_image_x = image_x - hardcover_shift_left_pt
        image_commands.append(
            (
                f"q {image_box_x:.2f} {image_box_y:.2f} {image_box_w:.2f} "
                f"{image_box_h:.2f} re W n {image_w:.2f} 0 0 {image_h:.2f} "
                f"{shifted_image_x:.2f} {image_y:.2f} cm /Im1 Do Q"
            )
        )

    content = [
        "0.035 0.035 0.045 rg",
        f"0 0 {width_pt:.2f} {height_pt:.2f} re f",
        f"q /GSBackArt gs {back_w:.2f} 0 0 {height_pt:.2f} 0 0 cm /Im1 Do Q",
        "q /GSVeil gs 0.025 0.022 0.03 rg",
        f"0 0 {back_w:.2f} {height_pt:.2f} re f Q",
        "0.035 0.027 0.032 rg",
        f"{spine_x:.2f} 0 {spine_pt:.2f} {height_pt:.2f} re f",
        "0.018 0.016 0.020 rg",
        f"{front_x:.2f} 0 {front_w:.2f} {height_pt:.2f} re f",
        "0.12 0.08 0.035 rg",
        f"{front_area_x:.2f} {front_area_y:.2f} {front_area_w:.2f} {front_area_h:.2f} re f",
        *image_commands,
    ]
    content.extend(
        back_cover_text_commands(
            title,
            subtitle,
            author,
            description,
            back_area_x,
            back_area_y,
            back_area_w,
            back_area_h,
            back_safe_margin_pt,
        )
    )
    content.extend(spine_text_commands(title, author, spine_x, spine_pt, height_pt))

    objects: dict[int, bytes] = {}
    objects[1] = b"<< /Type /Catalog /Pages 2 0 R >>"
    objects[2] = b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>"
    objects[3] = (
        f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {width_pt:.2f} {height_pt:.2f}] "
        "/Resources << /XObject << /Im1 4 0 R >> "
        "/Font << /F1 5 0 R /F2 6 0 R >> "
        "/ExtGState << /GSBackArt 8 0 R /GSVeil 9 0 R /GSSoft 10 0 R >> >> "
        "/Contents 7 0 R >>"
    ).encode("ascii")
    objects[4] = (
        f"<< /Type /XObject /Subtype /Image /Width {image_width} /Height {image_height} "
        f"/ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length {len(image_data)} >>\n"
        "stream\n"
    ).encode("ascii") + image_data + b"\nendstream"
    objects[5] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Times-Roman >>"
    objects[6] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Times-Bold >>"
    content_bytes = "\n".join(content).encode("utf-8")
    objects[7] = (
        f"<< /Length {len(content_bytes)} >>\nstream\n".encode("ascii")
        + content_bytes
        + b"\nendstream"
    )
    objects[8] = b"<< /Type /ExtGState /ca 0.13 /CA 0.13 >>"
    objects[9] = b"<< /Type /ExtGState /ca 0.94 /CA 0.94 >>"
    objects[10] = b"<< /Type /ExtGState /ca 0.42 /CA 0.42 >>"
    write_pdf_objects(target, objects, 1)
    print(f"-> KDP {binding_label} cover {rel(target)}")


def cover_rect(
    image_width: int,
    image_height: int,
    box_x: float,
    box_y: float,
    box_w: float,
    box_h: float,
) -> tuple[float, float, float, float]:
    image_ratio = image_width / image_height
    box_ratio = box_w / box_h
    if image_ratio > box_ratio:
        draw_h = box_h
        draw_w = draw_h * image_ratio
    else:
        draw_w = box_w
        draw_h = draw_w / image_ratio
    draw_x = box_x + (box_w - draw_w) / 2
    draw_y = box_y + (box_h - draw_h) / 2
    return draw_x, draw_y, draw_w, draw_h


def back_cover_text_commands(
    title: str,
    subtitle: str,
    author: str,
    description: str,
    area_x: float,
    area_y: float,
    area_width: float,
    area_height: float,
    safe_margin: float,
) -> list[str]:
    inner_left = area_x + safe_margin
    inner_right = area_x + area_width - safe_margin
    top = area_y + area_height - safe_margin
    bottom = area_y + safe_margin
    safe_width = max(inner_right - inner_left, 1)
    target_width = min(safe_width, area_width * BACK_COPY_MAX_WIDTH_RATIO)
    text_width = max(min(target_width, safe_width), min(120, safe_width))
    centered_left = area_x + (area_width - text_width) / 2
    left = min(max(centered_left, inner_left), inner_right - text_width)
    wrap_width = max(34, min(58, int(text_width / 5.4)))
    author_y = bottom + 24
    body_bottom = author_y + 58

    commands = [
        "q /GSSoft gs 0.70 0.47 0.18 rg",
        f"{left:.2f} {top - 18:.2f} {max(text_width * 0.78, 80):.2f} 1.25 re f",
        f"{left:.2f} {author_y - 18:.2f} {max(text_width * 0.60, 80):.2f} 1.25 re f Q",
        "0.965 0.84 0.52 rg",
    ]
    y = top - 42
    label = "MEMORIA ASTRA CYCLE"
    commands.append(pdf_text("F1", 9, label, left, y))
    y -= 27
    title_size = 18 if len(title) > 18 else 20
    commands.append(pdf_text("F2", title_size, title.upper(), left, y))
    y -= 27
    if subtitle:
        commands.append(pdf_text("F1", 10, subtitle.upper(), left, y))
        y -= 42
    else:
        y -= 18

    commands.extend(
        [
            "q /GSSoft gs 0.03 0.025 0.033 rg",
            f"{left - 14:.2f} {max(body_bottom - 12, y - 250):.2f} {text_width + 28:.2f} {max(y - body_bottom + 34, 80):.2f} re f Q",
            "0.86 0.76 0.58 rg",
        ]
    )
    commands.append("0.88 0.79 0.62 rg")
    for paragraph in normalized_paragraphs(description):
        for line in textwrap.wrap(paragraph.strip(), width=wrap_width):
            if y < body_bottom:
                break
            commands.append(pdf_text("F1", 10, line, left, y))
            y -= 15
        y -= 8

    commands.append("0.965 0.86 0.62 rg")
    commands.append(pdf_text("F2", 15, author.upper(), left, author_y))
    return commands


def normalized_paragraphs(text: str) -> list[str]:
    paragraphs: list[str] = []
    current: list[str] = []
    for raw_line in text.splitlines():
        line = " ".join(raw_line.strip().split())
        if not line:
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        current.append(line)
    if current:
        paragraphs.append(" ".join(current))
    return paragraphs


def spine_text_commands(
    title: str, author: str, spine_x: float, spine_width: float, page_height: float
) -> list[str]:
    if spine_width < 28:
        return []
    spine_center = spine_x + spine_width / 2
    text = f"{title.upper()}   {author.upper()}"
    font_size = max(8, min(13, int((page_height * 0.66) / max(len(text) * 0.56, 1))))
    text_run = len(text) * font_size * 0.56
    y_start = max(54, min((page_height - text_run) / 2, page_height - text_run - 54))
    return [
        "0.22 0.15 0.08 rg",
        f"{spine_x + 4:.2f} 44.00 {max(spine_width - 8, 1):.2f} {page_height - 88:.2f} re f",
        "0.965 0.86 0.62 rg",
        f"BT /F2 {font_size} Tf 0 1 -1 0 {spine_center + (font_size / 3):.2f} {y_start:.2f} Tm ({pdf_escape(pdf_safe_text(text))}) Tj ET",
    ]


def pdf_text(font: str, size: int, text: str, x: float, y: float) -> str:
    return f"BT /{font} {size} Tf {x:.2f} {y:.2f} Td ({pdf_escape(pdf_safe_text(text))}) Tj ET"


def jpeg_dimensions(data: bytes) -> tuple[int, int]:
    index = 2
    while index < len(data):
        if data[index] != 0xFF:
            index += 1
            continue
        marker = data[index + 1]
        index += 2
        if marker in {0xD8, 0xD9}:
            continue
        length = int.from_bytes(data[index : index + 2], "big")
        if 0xC0 <= marker <= 0xC3:
            height = int.from_bytes(data[index + 3 : index + 5], "big")
            width = int.from_bytes(data[index + 5 : index + 7], "big")
            return width, height
        index += length
    raise ValueError("Could not read JPEG dimensions")


def write_pdf_objects(target: Path, objects_by_id: dict[int, bytes], catalog_id: int) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    output = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    max_id = max(objects_by_id)
    for obj_id in range(1, max_id + 1):
        offsets.append(len(output))
        output.extend(f"{obj_id} 0 obj\n".encode("ascii"))
        output.extend(objects_by_id[obj_id])
        output.extend(b"\nendobj\n")
    xref_start = len(output)
    output.extend(f"xref\n0 {max_id + 1}\n".encode("ascii"))
    output.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        output.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    output.extend(
        f"trailer\n<< /Size {max_id + 1} /Root {catalog_id} 0 R >>\n"
        f"startxref\n{xref_start}\n%%EOF\n".encode("ascii")
    )
    target.write_bytes(bytes(output))


def write_manifest(package_dir: Path, manifest: dict[str, object]) -> None:
    target = package_dir / "metadata" / "manifest.json"
    target.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_checklist(
    book: Book, metadata: dict[str, object], package_dir: Path, manifest: dict[str, object]
) -> None:
    title = metadata.get("title") or book.title_guess
    identifier = metadata.get("identifier") or metadata.get("isbn") or "MISSING"
    lines = [
        f"# Publishing Checklist: {title}",
        "",
        "## Core Metadata",
        f"- Title: {title}",
        f"- Subtitle: {metadata.get('subtitle', '')}",
        f"- Author: {metadata.get('author', 'Alinari Campbell')}",
        f"- Publisher: {metadata.get('publisher', 'PixelPacific')}",
        f"- Identifier / ISBN: {identifier}",
        f"- Language: {metadata.get('language', 'en')}",
        "",
        "## ISBN Decision",
        "- KDP ebook can publish without an ISBN.",
        "- KDP paperback and hardcover require separate ISBNs; choose KDP free ISBNs during upload, or buy and enter separate ISBNs before the final rebuild.",
        "- If using your own ISBNs, match the ISBN agency title, author, publisher, and imprint exactly.",
        "",
        "## Apple Books",
        "- Upload the EPUB from `apple-books/`.",
        "- Upload the external cover image from `apple-books/`.",
        "- Validate with EPUBCheck or Apple Transporter before submission.",
        "",
        "## Google Play Books",
        "- Upload the EPUB from `google-play-books/`.",
        "- Upload the PDF from `google-play-books/` when present for original-page view.",
        "- Use ISBN/GGKEY-friendly filenames; this script avoids spaces and punctuation.",
        "",
        "## Amazon KDP Ebook",
        "- Upload the EPUB from `amazon-kdp/ebook/`.",
        "- Preview in Kindle Previewer before publishing.",
        "- Avoid KDP Select exclusivity if the same ebook must stay on Apple and Google.",
        "",
        "## Amazon KDP Print",
        "- Upload the paperback interior PDF from `amazon-kdp/print/paperback/`.",
        "- Upload the paperback full cover PDF from `amazon-kdp/print/paperback/`.",
        "- Upload the hardcover interior PDF from `amazon-kdp/print/hardcover/`.",
        "- Upload the hardcover full cover PDF from `amazon-kdp/print/hardcover/`.",
        "- The generated wrap covers reserve barcode space and use KDP cover-calculator dimensions for the current page count.",
        "- Run KDP Print Previewer and order physical proofs before enabling sales.",
        "",
        "## Generated Paths",
        "```json",
        json.dumps(manifest["platforms"], indent=2, ensure_ascii=False),
        "```",
        "",
    ]
    (package_dir / "metadata" / "publishing-checklist.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )


def command_audit_print(args: argparse.Namespace) -> int:
    output_root = Path(args.output).resolve()
    package_dirs = sorted(path for path in output_root.iterdir() if path.is_dir())
    failures = 0

    for package_dir in package_dirs:
        specs_path = package_dir / "metadata" / "kdp-print-cover-specs.json"
        if not specs_path.exists():
            continue

        specs = json.loads(specs_path.read_text(encoding="utf-8"))
        manuscript = package_dir / "source" / "manuscript-packaged.md"
        for binding in ["paperback", "hardcover"]:
            interior = first_matching(
                package_dir / "amazon-kdp" / "print" / binding, "*-interior.pdf"
            )
            cover = first_matching(package_dir / "amazon-kdp" / "print" / binding, "*-cover.pdf")
            binding_specs = specs.get(binding, {})
            expected_page_count = specs.get("page_count")
            expected_size = (
                float(binding_specs.get("full_cover_width", 0)),
                float(binding_specs.get("full_cover_height", 0)),
            )

            problems: list[str] = []
            if interior is None or cover is None:
                problems.append("missing print PDF")
                page_count = None
                cover_size = None
            else:
                page_count = count_pdf_pages(interior, manuscript)
                cover_size = media_box_inches(cover)
                if page_count != expected_page_count:
                    problems.append(f"pages {page_count} != spec {expected_page_count}")
                if cover_size is None:
                    problems.append("cover MediaBox missing")
                elif (
                    abs(cover_size[0] - expected_size[0]) > 0.005
                    or abs(cover_size[1] - expected_size[1]) > 0.005
                ):
                    problems.append(
                        f"cover {cover_size[0]:.3f}x{cover_size[1]:.3f} != "
                        f"spec {expected_size[0]:.3f}x{expected_size[1]:.3f}"
                    )
                kdp_margin = max(
                    float(binding_specs.get("margin_width") or 0),
                    float(binding_specs.get("margin_height") or 0),
                )
                back_safe_inset = (
                    PAPERBACK_BACK_SAFE_INSET_IN
                    if binding == "paperback"
                    else HARDCOVER_BACK_SAFE_INSET_IN
                )
                if back_safe_inset < kdp_margin + MIN_EXTRA_SAFE_INSET_IN:
                    problems.append(
                        f"back safe inset {back_safe_inset:.2f}in is too close to "
                        f"KDP margin {kdp_margin:.2f}in"
                    )

            status = "ok" if not problems else "FAIL"
            if problems:
                failures += 1
            size_text = (
                "missing"
                if cover_size is None
                else f"{cover_size[0]:.3f}x{cover_size[1]:.3f} in"
            )
            safe_text = (
                f"full-panel/{PAPERBACK_BACK_SAFE_INSET_IN:.2f}in"
                if binding == "paperback"
                else f"full-panel/{HARDCOVER_BACK_SAFE_INSET_IN:.2f}in"
            )
            print(
                f"{status:4} {package_dir.name:32} {binding:9} "
                f"pages={page_count} cover={size_text} front/back-safe={safe_text}"
            )
            for problem in problems:
                print(f"     - {problem}")

    return 1 if failures else 0


def first_matching(directory: Path, pattern: str) -> Path | None:
    matches = sorted(directory.glob(pattern))
    return matches[0] if matches else None


def media_box_inches(pdf: Path) -> tuple[float, float] | None:
    try:
        sample = pdf.read_bytes()[:2048]
    except OSError:
        return None
    match = re.search(
        rb"/MediaBox\s*\[\s*0\s+0\s+([0-9.]+)\s+([0-9.]+)\s*\]",
        sample,
    )
    if not match:
        return None
    return float(match.group(1)) / 72, float(match.group(2)) / 72


def command_inventory(args: argparse.Namespace) -> int:
    books = discover_books()
    print("Memoria Astra inventory")
    print("======================")
    for book in books:
        metadata = metadata_for(book)
        status = "ready" if book.manuscript and book.cover else "needs-attention"
        if book.manuscript and not book.cover:
            status = "missing-cover"
        if not book.manuscript and book.legacy_source:
            status = "legacy-source-only"
        elif not book.manuscript:
            status = "missing-manuscript"
        print(f"{book.number:02d}. {metadata.get('title', book.title_guess)} [{status}]")
        print(f"    folder: {rel(book.path)}")
        print(f"    manuscript: {rel(book.manuscript)}")
        print(f"    cover: {rel(book.cover)}")
        print(f"    metadata: {rel(book.metadata_file)}")
        if book.legacy_source:
            print(f"    legacy source: {rel(book.legacy_source)}")
    return 0


def command_doctor(args: argparse.Namespace) -> int:
    missing_optional = []
    for tool in ["pandoc", "xelatex", "zip", "unzip"]:
        if require_tool(tool):
            print(f"ok: {tool}")
        else:
            print(f"missing: {tool} (internal fallback available)")
            if tool in {"pandoc", "xelatex"}:
                missing_optional.append(tool)

    if missing_optional:
        print()
        print("The publisher can still generate EPUB/PDF packages with built-in fallbacks.")
        print("Install optional tools for the higher-typography Pandoc/XeLaTeX path.")
        print("macOS quick path: brew install pandoc basictex")
        print("GitHub Actions also installs these in .github/workflows/build_epub.yml.")
    return 0


def command_build(args: argparse.Namespace) -> int:
    output_root = Path(args.output).resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    books = discover_books()
    selected = select_books(books, args)
    if not selected:
        print("No matching books found.")
        return 1

    failures = 0
    for book in selected:
        if not book.manuscript:
            print(f"Cannot build {book.key}: missing {rel(book.path / 'Manuscript.md')}")
            failures += 1
            continue
        try:
            build_book(book, output_root, skip_existing=args.skip_existing)
        except Exception as exc:  # noqa: BLE001 - top-level CLI should report and continue.
            print(f"Failed to build {book.key}: {exc}", file=sys.stderr)
            failures += 1

    return 1 if failures else 0


def select_books(books: list[Book], args: argparse.Namespace) -> list[Book]:
    if args.all:
        return [book for book in books if book.manuscript]
    if args.book:
        target = Path(args.book).resolve()
        if target.is_file():
            target = target.parent
        return [book for book in books if book.path.resolve() == target]
    if args.number is not None:
        return [book for book in books if book.number == args.number]
    cwd = Path.cwd().resolve()
    return [book for book in books if book.path.resolve() == cwd]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build Memoria Astra publishing packages from Manuscript.md."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    inventory = sub.add_parser("inventory", help="List discovered books and asset readiness.")
    inventory.set_defaults(func=command_inventory)

    doctor = sub.add_parser("doctor", help="Check local publishing dependencies.")
    doctor.set_defaults(func=command_doctor)

    build = sub.add_parser("build", help="Build one book or all books.")
    build.add_argument("--all", action="store_true", help="Build every numbered book folder.")
    build.add_argument("--book", help="Path to a book folder or Manuscript.md.")
    build.add_argument("--number", type=int, help="Book number to build, such as 8.")
    build.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output directory.")
    build.add_argument(
        "--skip-existing",
        action="store_true",
        help="Keep existing package directory contents instead of replacing them.",
    )
    build.set_defaults(func=command_build)

    audit_print = sub.add_parser(
        "audit-print", help="Verify KDP print page counts and wrap-cover sizes."
    )
    audit_print.add_argument(
        "--output", default=str(DEFAULT_OUTPUT), help="Output directory to audit."
    )
    audit_print.set_defaults(func=command_audit_print)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
