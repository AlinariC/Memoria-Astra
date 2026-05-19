# PixelPacific Publishing

Reusable publishing tooling for PixelPacific books and series.

This repository builds ebook, print, and storefront-ready packages from active book folders. Finished projects can be moved under `archive/`; archived projects stay in the repo for reference but are skipped by normal local builds and GitHub push runs.

## Quick Start

```bash
python3 scripts/publish.py inventory
python3 scripts/publish.py doctor
python3 scripts/publish.py build --all --allow-empty
python3 scripts/publish.py audit-print
```

Generated packages appear under `output/<package>/` with Apple Books, Google Play Books, Amazon KDP ebook, Amazon KDP paperback, Amazon KDP hardcover, source, and metadata folders.

## Active Content Layout

Create one folder per active series or standalone project. A series folder can include a `series.yaml` file and numbered book folders:

```text
New_Series/
├── series.yaml
├── assets/
│   └── Colophon.md
├── 01_First_Title/
│   ├── Manuscript.md
│   ├── metadata.yaml
│   └── cover.jpg
└── 02_Second_Title/
    ├── Manuscript.md
    ├── metadata.yaml
    └── cover.jpg
```

A standalone book can use the same numbered folder shape at the repository root or inside its own project folder.

`series.yaml` and `publishing.yaml` values are inherited by books below them. Useful shared fields include:

```yaml
project: "Example Series"
project-slug: "example-series"
package-prefix: "example-series"
publisher: "PixelPacific"
imprint: "PixelPacific Publishing"
author: "Author Name"
language: "en"
```

`package-prefix` is optional, but it keeps generated output names unique when more than one series has a `01_...` book.

Each book folder should include:

```text
01_First_Title/
├── Manuscript.md
├── metadata.yaml
└── cover.jpg
```

`Manuscript.md` or `metadata.yaml` should provide storefront metadata:

```yaml
---
title: "First Title"
subtitle: "Book One in the Example Series"
author: "Author Name"
language: "en"
publisher: "PixelPacific"
identifier: "urn:uuid:example-series-01-first-title"
cover-image: cover.jpg
series: "Example Series"
description: |
  Storefront-ready description copy goes here.
---
```

The publisher appends the nearest `assets/Colophon.md` automatically when the manuscript does not already include one.

## Archived Content

Archived projects live below `archive/`, `archives/`, or `archived/` and are skipped unless explicitly requested:

```bash
python3 scripts/publish.py inventory --include-archived
python3 scripts/publish.py build --book archive/Memoria_Astra/16_The_Second_Spiral
python3 scripts/publish.py build --all --include-archived
```

The GitHub Actions workflow also ignores archive paths, so pushing archive-only changes will not rebuild old catalogs.

## Local Dependencies

The app can generate EPUB/PDF packages with Python alone. For best typography and closer-to-final print interiors, install the optional Pandoc toolchain:

- `pandoc` for EPUB generation
- `xelatex` for print PDF generation
- `zip` and `unzip` for archive support

On macOS:

```bash
brew install pandoc basictex
```

On GitHub Actions, `.github/workflows/build_epub.yml` installs the optional Linux packages and publishes one ZIP package per active book.

## Notes

- Amazon KDP ebook upload uses EPUB. Kindle Previewer should still be used as the final preflight step.
- KDP paperback and hardcover uploads include interior PDFs and full back-spine-front cover PDFs.
- The hardcover front-cover generator applies the standard `0.16in` left shift unless a book overrides `kdp-hardcover-front-shift-left-in`.
- Google Play Books can accept both EPUB and PDF; this workflow gives it both when PDF generation is available.
- Apple Books wants EPUB validation before upload; use EPUBCheck or Transporter.
