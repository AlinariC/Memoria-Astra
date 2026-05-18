# Memoria Astra Publishing

Memoria Astra is a 15-book science fiction cycle by Alinari Campbell, published
by PixelPacific.

This repository is now organized around one simple workflow:

1. Put a finished `Manuscript.md` in a numbered book folder.
2. Add a final `cover.jpg` beside it.
3. Run one command from the repository root.
4. Upload the generated platform folders to Apple Books, Google Play Books, and
   Amazon KDP.

## Quick Start

```bash
python3 scripts/publish.py inventory
python3 scripts/publish.py doctor
python3 scripts/publish.py build --number 8
python3 scripts/publish.py audit-print
```

To rebuild the combined novel source before packaging:

```bash
python3 scripts/build_first_spiral.py
python3 scripts/publish.py build --all
python3 scripts/build_apple_itmsp.py --all --provider AlinariCampbell
```

To build every numbered book folder that has a manuscript:

```bash
python3 scripts/publish.py build --all
python3 scripts/publish.py audit-print
```

`audit-print` checks every generated KDP paperback and hardcover package against
the recorded page count and wrap-cover size before you upload to KDP.

The generated package appears under `output/<book>/`:

```text
output/<book>/
├── apple-books/
│   ├── <book>.epub
│   └── cover.jpg
├── google-play-books/
│   ├── <book>.epub
│   ├── <book>.pdf
│   └── cover.jpg
├── amazon-kdp/
│   ├── ebook/
│   │   ├── <book>.epub
│   │   └── cover.jpg
│   └── print/
│       ├── paperback/
│       │   ├── <book>-paperback-interior.pdf
│       │   ├── <book>-paperback-cover.pdf
│       │   └── cover.jpg
│       └── hardcover/
│           ├── <book>-hardcover-interior.pdf
│           ├── <book>-hardcover-cover.pdf
│           └── cover.jpg
├── metadata/
│   ├── kdp-print-cover-specs.json
│   ├── manifest.json
│   └── publishing-checklist.md
└── source/
    └── manuscript-packaged.md
```

## Book Folder Contract

Each publishable book folder should look like this:

```text
08_Inheritance_of_Song/
├── Manuscript.md
├── metadata.yaml
└── cover.jpg
```

`Manuscript.md` should start with YAML front matter:

```yaml
---
title: "Inheritance of Song"
subtitle: "Book Eight in the Memoria Astra Cycle"
author: "Alinari Campbell"
language: "en"
publisher: "PixelPacific"
identifier: "urn:isbn:..."
cover-image: cover.jpg
---
```

The publisher app appends `assets/Colophon.md` automatically when the manuscript
does not already include a colophon.

## Local Dependencies

The app can generate EPUB/PDF packages with Python alone. For best typography
and closer-to-final print interiors, install the optional Pandoc toolchain:

- `pandoc` for EPUB generation
- `xelatex` for print PDF generation
- `zip` and `unzip` for archive support
On macOS:

```bash
brew install pandoc basictex
```

On GitHub Actions, `.github/workflows/build_epub.yml` installs the optional
Linux packages and publishes one ZIP package per book in the release.

## Notes

- Amazon KDP ebook upload uses EPUB. Kindle Previewer should still be used as
  the final preflight step.
- KDP paperback and hardcover uploads include interior PDFs and full
  back-spine-front cover PDFs. The publisher uses KDP's cover-calculator
  measurements for the current page count and records them in
  `metadata/kdp-print-cover-specs.json`.
- Google Play Books can accept both EPUB and PDF; this workflow gives it both
  when PDF generation is available.
- Apple Books wants EPUB validation before upload; use EPUBCheck or Transporter.
- Built-in fallback PDFs are useful for drafts and preflight packages. Install
  Pandoc/XeLaTeX before final print upload when typography matters.

---

© 2025 Alinari Campbell | Published by PixelPacific
