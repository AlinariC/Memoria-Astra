#!/usr/bin/env python3
"""Build Apple Books Transporter .itmsp packages from generated PixelPacific outputs."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = REPO_ROOT / "output"
DEFAULT_CATALOG = REPO_ROOT / "metadata" / "apple-books" / "catalog.json"
PUBLICATION_NS = "http://apple.com/itunes/importer/publication"
DEFAULT_PACKAGE_VERSION = "publication5.0"
ISBN_RE = re.compile(r"(?:urn:isbn:)?(?P<isbn>97[89][0-9]{10})$")


@dataclass(frozen=True)
class AssetInfo:
    source: Path
    file_name: str
    size: int
    md5: str
    image_size: tuple[int, int] | None = None


@dataclass(frozen=True)
class ApplePackage:
    slug: str
    title: str
    vendor_id: str
    package_dir: Path
    metadata_xml: Path
    warnings: list[str]
    blockers: list[str]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_catalog(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"defaults": {}, "books": {}}
    catalog = read_json(path)
    catalog.setdefault("defaults", {})
    catalog.setdefault("books", {})
    return catalog


def discover_package_dirs(output_root: Path) -> list[Path]:
    if not output_root.exists():
        return []
    return sorted(
        child
        for child in output_root.iterdir()
        if child.is_dir()
        and (child / "apple-books").is_dir()
        and (child / "metadata" / "manifest.json").exists()
    )


def select_package_dirs(package_dirs: list[Path], requested: list[str]) -> list[Path]:
    if not requested:
        return package_dirs

    wanted = {normalize_book_selector(value) for value in requested}
    selected = [path for path in package_dirs if path.name in wanted]
    missing = sorted(wanted - {path.name for path in selected})
    if missing:
        raise ValueError(f"No generated package found for: {', '.join(missing)}")
    return selected


def normalize_book_selector(value: str) -> str:
    path = Path(value)
    if path.exists():
        if path.is_file():
            path = path.parent
        return path.name
    return value.strip().strip("/")


def build_package(package_dir: Path, catalog: dict[str, Any], provider_override: str | None) -> ApplePackage:
    slug = package_dir.name
    manifest = read_json(package_dir / "metadata" / "manifest.json")
    book_manifest = manifest.get("book", {})
    defaults = catalog.get("defaults", {})
    overrides = catalog.get("books", {}).get(slug, {})
    merged = {**defaults, **book_manifest, **overrides}
    if "print_specs" in manifest and "print_specs" not in merged:
        merged["print_specs"] = manifest["print_specs"]

    title = required_text(merged, "title", slug)
    author = required_text(merged, "author", "Alinari Campbell")
    publisher = required_text(merged, "publisher", "PixelPacific")
    language = required_text(merged, "language", "en")
    description = str(merged.get("description") or "").strip()
    provider = provider_override or os.environ.get("APPLE_BOOKS_PROVIDER") or str(merged.get("provider") or "").strip()
    package_version = str(merged.get("package_version") or DEFAULT_PACKAGE_VERSION)
    identifier = str(merged.get("identifier") or "").strip()
    isbn = isbn_from_identifier(identifier)
    vendor_id = str(merged.get("vendor_id") or isbn or identifier_to_vendor_id(identifier) or slug)

    apple_dir = package_dir / "apple-books"
    epub = find_single_asset(apple_dir, "*.epub")
    cover = find_cover(apple_dir)
    epub_info = asset_info(epub)
    cover_info = asset_info(cover)

    warnings: list[str] = []
    blockers: list[str] = []

    if not provider:
        blockers.append("Missing Apple provider short name; set provider in catalog or APPLE_BOOKS_PROVIDER.")
    elif str(merged.get("provider_status")) == "assumed_from_publisher_name" and not provider_override and not os.environ.get("APPLE_BOOKS_PROVIDER"):
        warnings.append(f"Provider short name is assumed as {provider}; confirm against Apple Books account.")

    if len(description) < 50:
        blockers.append("Description is missing or shorter than Apple's 50-character guidance.")

    subjects = normalize_subjects(merged.get("subjects"))
    if len(subjects) < 2:
        blockers.append("Apple metadata should include a primary and secondary subject category.")

    if "draft" in vendor_id.lower():
        blockers.append("Vendor ID contains 'draft'; replace with a permanent Apple vendor ID before public upload.")

    if not isbn:
        warnings.append("No ISBN found; Apple allows ISBNs to be optional, but confirm the permanent vendor ID before first upload.")

    if cover_info.image_size:
        shortest_side = min(cover_info.image_size)
        if shortest_side < 1400:
            blockers.append(
                f"Cover shortest side is {shortest_side}px; Apple requires at least 1400px."
            )
    else:
        warnings.append("Could not inspect cover pixel dimensions with the built-in parser.")

    itmsp_dir = apple_dir / f"{safe_filename(vendor_id)}.itmsp"
    if itmsp_dir.exists():
        shutil.rmtree(itmsp_dir)
    itmsp_dir.mkdir(parents=True)

    epub_target = itmsp_dir / epub_info.file_name
    cover_target = itmsp_dir / cover_info.file_name
    shutil.copy2(epub_info.source, epub_target)
    shutil.copy2(cover_info.source, cover_target)

    # Recalculate from copied files so metadata always describes package-local assets.
    epub_info = asset_info(epub_target)
    cover_info = asset_info(cover_target)
    metadata_xml = itmsp_dir / "metadata.xml"
    write_metadata_xml(
        target=metadata_xml,
        package_version=package_version,
        provider=provider,
        vendor_id=vendor_id,
        isbn=isbn,
        metadata=merged,
        title=title,
        author=author,
        publisher=publisher,
        language=language,
        description=description,
        subjects=subjects,
        epub=epub_info,
        cover=cover_info,
        include_products=bool(merged.get("include_products", True)),
    )
    write_report(apple_dir, slug, vendor_id, metadata_xml, epub_info, cover_info, warnings, blockers)

    return ApplePackage(
        slug=slug,
        title=title,
        vendor_id=vendor_id,
        package_dir=itmsp_dir,
        metadata_xml=metadata_xml,
        warnings=warnings,
        blockers=blockers,
    )


def required_text(metadata: dict[str, Any], key: str, fallback: str) -> str:
    value = str(metadata.get(key) or "").strip()
    return value or fallback


def isbn_from_identifier(identifier: str) -> str | None:
    match = ISBN_RE.match(identifier.replace("-", ""))
    if match:
        return match.group("isbn")
    return None


def identifier_to_vendor_id(identifier: str) -> str | None:
    if not identifier:
        return None
    value = identifier
    for prefix in ["urn:isbn:", "urn:uuid:", "uuid:"]:
        if value.startswith(prefix):
            value = value[len(prefix) :]
            break
    return safe_filename(value) if value else None


def find_single_asset(directory: Path, pattern: str) -> Path:
    matches = sorted(
        path for path in directory.glob(pattern) if path.is_file() and ".itmsp" not in path.parts
    )
    if len(matches) != 1:
        found = ", ".join(path.name for path in matches) or "none"
        raise FileNotFoundError(f"Expected one {pattern} in {rel(directory)}; found {found}")
    return matches[0]


def find_cover(directory: Path) -> Path:
    for name in ["cover.jpg", "cover.jpeg"]:
        candidate = directory / name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(f"Expected cover.jpg or cover.jpeg in {rel(directory)}")


def asset_info(path: Path) -> AssetInfo:
    data = path.read_bytes()
    return AssetInfo(
        source=path,
        file_name=safe_filename(path.name),
        size=len(data),
        md5=hashlib.md5(data).hexdigest(),  # noqa: S324 - Apple metadata requires MD5 checksums.
        image_size=image_dimensions(data, path.suffix.lower()),
    )


def safe_filename(value: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip())
    return safe.strip(".-") or "asset"


def image_dimensions(data: bytes, suffix: str) -> tuple[int, int] | None:
    if suffix == ".png" and data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
        return int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")

    if suffix in {".jpg", ".jpeg"} and data.startswith(b"\xff\xd8"):
        index = 2
        while index + 9 < len(data):
            if data[index] != 0xFF:
                index += 1
                continue
            marker = data[index + 1]
            index += 2
            if marker in {0xD8, 0xD9}:
                continue
            if index + 2 > len(data):
                return None
            length = int.from_bytes(data[index : index + 2], "big")
            if length < 2 or index + length > len(data):
                return None
            if marker in {
                0xC0,
                0xC1,
                0xC2,
                0xC3,
                0xC5,
                0xC6,
                0xC7,
                0xC9,
                0xCA,
                0xCB,
                0xCD,
                0xCE,
                0xCF,
            }:
                height = int.from_bytes(data[index + 3 : index + 5], "big")
                width = int.from_bytes(data[index + 5 : index + 7], "big")
                return width, height
            index += length
    return None


def normalize_subjects(raw: Any) -> list[dict[str, str]]:
    subjects: list[dict[str, str]] = []
    if not isinstance(raw, list):
        return subjects
    for item in raw:
        if isinstance(item, str):
            subjects.append({"scheme": "BISAC", "code": item})
        elif isinstance(item, dict):
            code = str(item.get("code") or "").strip()
            scheme = str(item.get("scheme") or "BISAC").strip()
            if code:
                subjects.append({"scheme": scheme, "code": code})
    return subjects


def write_metadata_xml(
    *,
    target: Path,
    package_version: str,
    provider: str,
    vendor_id: str,
    isbn: str | None,
    metadata: dict[str, Any],
    title: str,
    author: str,
    publisher: str,
    language: str,
    description: str,
    subjects: list[dict[str, str]],
    epub: AssetInfo,
    cover: AssetInfo,
    include_products: bool,
) -> None:
    ET.register_namespace("", PUBLICATION_NS)
    package = ET.Element(qname("package"), {"version": package_version})
    if provider:
        child(package, "provider", provider)

    book = ET.SubElement(package, qname("book"))
    child(book, "vendor_id", vendor_id)

    metadata_node = ET.SubElement(book, qname("metadata"))
    child(metadata_node, "publication_type", "book")
    if isbn:
        identifiers = ET.SubElement(metadata_node, qname("identifiers"))
        identifier = ET.SubElement(identifiers, qname("identifier"), {"scheme": "isbn13"})
        identifier.text = isbn
    child(metadata_node, "title", title)
    if metadata.get("subtitle"):
        child(metadata_node, "subtitle", str(metadata["subtitle"]))
    contributors(metadata_node, author)
    languages = ET.SubElement(metadata_node, qname("languages"))
    language_node = ET.SubElement(languages, qname("language"), {"type": "main"})
    language_node.text = language
    page_count = page_count_from_metadata(metadata)
    if page_count:
        child(metadata_node, "number_of_pages", str(page_count))
    if subjects:
        subjects_node = ET.SubElement(metadata_node, qname("subjects"))
        for index, subject in enumerate(subjects):
            attrs = {"scheme": subject["scheme"]}
            if index == 0:
                attrs["primary"] = "true"
            subject_node = ET.SubElement(subjects_node, qname("subject"), attrs)
            subject_node.text = subject["code"]
    description_node = ET.SubElement(metadata_node, qname("description"), {"format": "plain"})
    description_node.text = description
    child(metadata_node, "publisher", publisher)
    if metadata.get("publication_date"):
        child(metadata_node, "publication_date", str(metadata["publication_date"]))
    if include_products:
        products(metadata_node, metadata)

    assets = ET.SubElement(book, qname("assets"))
    asset(assets, "full", epub)
    asset(assets, "artwork", cover)

    ET.indent(package, space="  ")
    tree = ET.ElementTree(package)
    target.write_bytes(b'<?xml version="1.0" encoding="UTF-8"?>\n')
    with target.open("ab") as file:
        tree.write(file, encoding="utf-8", xml_declaration=False, short_empty_elements=False)
        file.write(b"\n")


def page_count_from_metadata(metadata: dict[str, Any]) -> int | None:
    print_specs = metadata.get("print_specs")
    if isinstance(print_specs, dict):
        page_count = print_specs.get("page_count")
        if isinstance(page_count, int):
            return page_count
    page_count = metadata.get("page_count")
    if isinstance(page_count, int):
        return page_count
    return None


def child(parent: ET.Element, name: str, text: str) -> ET.Element:
    node = ET.SubElement(parent, qname(name))
    node.text = text
    return node


def contributors(parent: ET.Element, author: str) -> None:
    contributors_node = ET.SubElement(parent, qname("contributors"))
    contributor = ET.SubElement(contributors_node, qname("contributor"))
    child(contributor, "primary", "true")
    child(contributor, "name", author)
    child(contributor, "sort_name", author_sort_name(author))
    roles = ET.SubElement(contributor, qname("roles"))
    child(roles, "role", "author")


def author_sort_name(author: str) -> str:
    parts = author.split()
    if len(parts) < 2:
        return author
    return f"{parts[-1]}, {' '.join(parts[:-1])}"


def products(parent: ET.Element, metadata: dict[str, Any]) -> None:
    products_node = ET.SubElement(parent, qname("products"))
    product = ET.SubElement(products_node, qname("product"))
    child(product, "territory", str(metadata.get("territory") or "US"))
    child(product, "cleared_for_sale", bool_text(metadata.get("cleared_for_sale", True)))
    if metadata.get("price_tier") is not None:
        child(product, "price_tier", str(metadata["price_tier"]))
    child(product, "release_type", str(metadata.get("release_type") or "digital-only"))
    if metadata.get("sales_start_date"):
        child(product, "sales_start_date", str(metadata["sales_start_date"]))
    child(product, "drm_free", bool_text(metadata.get("drm_free", False)))


def bool_text(value: Any) -> str:
    return "true" if bool(value) else "false"


def asset(parent: ET.Element, asset_type: str, info: AssetInfo) -> None:
    asset_node = ET.SubElement(parent, qname("asset"), {"type": asset_type})
    data_file = ET.SubElement(asset_node, qname("data_file"))
    child(data_file, "file_name", info.file_name)
    child(data_file, "size", str(info.size))
    checksum = ET.SubElement(data_file, qname("checksum"), {"type": "md5"})
    checksum.text = info.md5


def qname(name: str) -> str:
    return f"{{{PUBLICATION_NS}}}{name}"


def write_report(
    apple_dir: Path,
    slug: str,
    vendor_id: str,
    metadata_xml: Path,
    epub: AssetInfo,
    cover: AssetInfo,
    warnings: list[str],
    blockers: list[str],
) -> None:
    report = {
        "slug": slug,
        "vendor_id": vendor_id,
        "package": rel(metadata_xml.parent),
        "metadata_xml": rel(metadata_xml),
        "assets": {
            "epub": {
                "file_name": epub.file_name,
                "size": epub.size,
                "md5": epub.md5,
            },
            "cover": {
                "file_name": cover.file_name,
                "size": cover.size,
                "md5": cover.md5,
                "dimensions": list(cover.image_size) if cover.image_size else None,
            },
        },
        "warnings": warnings,
        "blockers": blockers,
    }
    (apple_dir / "apple-package-report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build Apple Books Transporter .itmsp packages from generated PixelPacific assets."
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Build all generated Apple Books package folders. This is the default when no --book is supplied.",
    )
    parser.add_argument(
        "--book",
        action="append",
        default=[],
        help="Output package slug or path to build, for example 01-terra-in-the-mists.",
    )
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Generated output root.")
    parser.add_argument(
        "--catalog",
        default=str(DEFAULT_CATALOG),
        help="Apple Books metadata overlay JSON.",
    )
    parser.add_argument(
        "--provider",
        help="Apple Books provider short name. Overrides catalog and APPLE_BOOKS_PROVIDER.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero if any generated package still has account/metadata blockers.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    output_root = Path(args.output).resolve()
    catalog = load_catalog(Path(args.catalog).resolve())
    package_dirs = select_package_dirs(discover_package_dirs(output_root), args.book)
    if not package_dirs:
        print("No generated Apple Books folders found; nothing to package.")
        return 0

    packages: list[ApplePackage] = []
    failures = 0
    for package_dir in package_dirs:
        try:
            package = build_package(package_dir, catalog, args.provider)
            packages.append(package)
        except Exception as exc:  # noqa: BLE001 - CLI should report all packages.
            failures += 1
            print(f"FAIL {package_dir.name}: {exc}", file=sys.stderr)

    for package in packages:
        status = "BLOCKED" if package.blockers else "OK"
        print(f"{status:7} {package.slug}: {rel(package.package_dir)}")
        for warning in package.warnings:
            print(f"        warning: {warning}")
        for blocker in package.blockers:
            print(f"        blocker: {blocker}")

    if failures:
        return 1
    if args.strict and any(package.blockers for package in packages):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
