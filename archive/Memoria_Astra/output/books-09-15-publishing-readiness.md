# Books 09-15 Publishing Readiness

Checked: 2026-05-18

Scope: Standalone Books 09-15 only. Book 16 / The Second Spiral has since been rebuilt as a combined novel; see `output/second-spiral-publishing-readiness.md`.

## Manuscript and Print Length

| Book | Title | Words | Paperback pages | Status |
| --- | --- | ---: | ---: | --- |
| 09 | The Silent Accord | 8,675 | 53 | Meets 50-page floor |
| 10 | Starforged Thrones | 12,276 | 65 | Meets 50-page floor |
| 11 | Lament of the Shattered Gate | 10,708 | 58 | Meets 50-page floor |
| 12 | Resonance of Ash and Dream | 10,569 | 52 | Meets 50-page floor |
| 13 | The Gathering Spiral | 11,102 | 62 | Meets 50-page floor |
| 14 | The Weeping Crown | 11,853 | 63 | Meets 50-page floor |
| 15 | The Final Loom | 8,964 | 51 | Meets 50-page floor |

## Generated Deliverables

Each title has been rebuilt with the current manuscript and cover:

- Source EPUB and PDF under `output/<slug>/source/`
- Apple Books EPUB, cover, strict `.itmsp` package, and metadata report under `output/<slug>/apple-books/`
- Google Play Books EPUB/PDF/cover under `output/<slug>/google-play-books/`
- Amazon KDP ebook EPUB/cover under `output/<slug>/amazon-kdp/ebook/`
- Amazon KDP paperback interior PDF and full wrap cover PDF under `output/<slug>/amazon-kdp/print/paperback/`
- Amazon KDP hardcover interior PDF and full wrap cover PDF under `output/<slug>/amazon-kdp/print/hardcover/`

## Validation Run

- `wc -w` confirmed every manuscript is substantially expanded.
- `python3 scripts/publish.py build --number 9` through `--number 15` completed.
- `python3 scripts/publish.py audit-print` reported `ok` for books 09-15, with paperback page counts between 51 and 65.
- `unzip -t` passed for all Apple, Google Play Books, and KDP ebook EPUBs for books 09-15.
- `python3 scripts/build_apple_itmsp.py --book <slug> --strict` passed for books 09-15.
- `python3 scripts/publish.py inventory` lists books 09-15 as ready and does not list book 16.

## Known Publishing Notes

- Apple Books packages pass strict local validation, but each currently warns that no ISBN is present. Apple allows ISBN-less uploads, but confirm the permanent vendor IDs before first upload.
- KDP paperback page-count requirements are satisfied: the current 6x9 black-and-white paperbacks exceed both the user-requested 50-page floor and KDP's 24-page minimum.
- KDP hardcover files were generated, but books 09-15 are below KDP's current 75-page hardcover minimum. Do not upload these as standalone hardcovers unless the manuscripts are expanded further or hardcover is intentionally skipped.
- Run KDP Print Previewer and order proofs before any live paperback sale.
- Apple Books / iTunes Connect delivery completed through Transporter on 2026-05-17 at 23:39 MST; see `output/apple-books-delivery-09-16.md`.

KDP references checked on 2026-05-18:

- Paperback page-count minimum: https://kdp.amazon.com/en_US/help/topic/G201857950
- Hardcover page-count minimum: https://kdp.amazon.com/en_US/help/topic/GAVW3FZZAKA2KY3B

## Book 16 Status

Superseded: Book 16 has been rebuilt as `16_The_Second_Spiral/` and packaged under `output/16-the-second-spiral/`.

This file remains useful as the standalone 09-15 publishing ledger.
