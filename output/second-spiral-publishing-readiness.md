# The Second Spiral Publishing Readiness

Checked: 2026-05-18

Scope: Book 16, `The Second Spiral`, rebuilt as one cohesive novel from Books 07-15.

## Editorial Assembly

- Read the end of `00_The_First_Spiral/Manuscript.md` and `06_Harmonic_Rebirth/Manuscript.md` to pick up the handoff: the Second Spiral begins with the children of flame and the children of breath growing apart from the same cradle.
- Built `16_The_Second_Spiral/Manuscript.md` with one front matter block, one combined novel identity, nine major parts, and new connective bridges.
- Preserved the expanded source manuscripts for Books 07-15.
- Added `scripts/build_second_spiral.py` so the combined novel can be regenerated from the standalone source books.

## Source Movements

| Part | Source | Source words |
| --- | --- | ---: |
| I - Foundations of Flame | `07_Foundations_of_Flame/Manuscript.md` | 14,947 |
| II - Inheritance of Song | `08_Inheritance_of_Song/Manuscript.md` | 7,016 |
| III - The Silent Accord | `09_The_Silent_Accord/Manuscript.md` | 8,543 |
| IV - Starforged Thrones | `10_Starforged_Thrones/Manuscript.md` | 12,147 |
| V - Lament of the Shattered Gate | `11_Lament_of_the_Shattered_Gate/Manuscript.md` | 10,577 |
| VI - Resonance of Ash and Dream | `12_Resonance_of_Ash_and_Dream/Manuscript.md` | 10,447 |
| VII - The Gathering Spiral | `13_The_Gathering_Spiral/Manuscript.md` | 10,969 |
| VIII - The Weeping Crown | `14_The_Weeping_Crown/Manuscript.md` | 11,721 |
| IX - The Final Loom | `15_The_Final_Loom/Manuscript.md` | 8,829 |

Generated manuscript shell word count: 96,885 by `wc -w`.

## Generated Deliverables

- Source EPUB/PDF: `output/16-the-second-spiral/source/`
- Apple Books EPUB, cover, strict `.itmsp` package, and metadata report: `output/16-the-second-spiral/apple-books/`
- Google Play Books EPUB/PDF/cover: `output/16-the-second-spiral/google-play-books/`
- Amazon KDP ebook EPUB/cover: `output/16-the-second-spiral/amazon-kdp/ebook/`
- Amazon KDP paperback interior and full wrap cover PDFs: `output/16-the-second-spiral/amazon-kdp/print/paperback/`
- Amazon KDP hardcover interior and full wrap cover PDFs: `output/16-the-second-spiral/amazon-kdp/print/hardcover/`

## Validation Run

- `python3 scripts/publish.py inventory` lists Book 16 as ready.
- `python3 scripts/publish.py build --number 16` completed.
- `python3 scripts/publish.py audit-print` reported `ok` for Book 16.
- Paperback page count: 471.
- Hardcover page count: 471.
- `unzip -t` passed for the Apple Books, Google Play Books, and KDP ebook EPUBs.
- `python3 scripts/build_apple_itmsp.py --book 16-the-second-spiral --strict` passed.
- Apple Books package warning: no ISBN found; confirm the permanent vendor ID before first upload if using ISBN-less Apple delivery.
- Cover art was converted from `covers/16_The_Second_Spiral.png` to `16_The_Second_Spiral/cover.jpg` and upscaled to 1600 x 2404 pixels for Apple cover validation.

## Storefront Safety

- `metadata/apple-books/catalog.json` includes `16-the-second-spiral` with vendor ID `memoria_astra_16_the_second_spiral`.
- Delivered to Apple Books / iTunes Connect through Transporter on 2026-05-17 at 23:39 MST.
- Transporter upload ID: `d65b8c0d-aea8-4f17-bb5e-e071739adc46`.
- Store processing/review may continue after delivery.
