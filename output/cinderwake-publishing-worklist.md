# Cinderwake Trilogy Publishing Worklist

Prepared: 2026-05-19

## Local Package Set

Generated packages should be built under `output/` with the `cinderwake` prefix.

| Package | Title | Source Folder | Target Status |
|---|---|---|---|
| 01 | The Ash Beneath the Crown | `Fantasy Novel Series/01_The_Ash_Beneath_the_Crown` | Complete; print audit passed at 486 pages |
| 02 | The Moon Below the World | `Fantasy Novel Series/02_The_Moon_Below_the_World` | Complete; print audit passed at 498 pages |
| 03 | The Dragon That Dreamed Death | `Fantasy Novel Series/03_The_Dragon_That_Dreamed_Death` | Complete; print audit passed at 482 pages |

## Recommended Upload Files

For each package:

- Apple Books: `output/<slug>/apple-books/<slug>.epub`, `output/<slug>/apple-books/cover.jpg`, plus the generated `.itmsp` folder.
- Google Play Books: `output/<slug>/google-play-books/<slug>.epub`, `output/<slug>/google-play-books/cover.jpg`, and `output/<slug>/google-play-books/<slug>.pdf` if Google asks for the PDF asset.
- Amazon KDP ebook: `output/<slug>/amazon-kdp/ebook/<slug>.epub` and `output/<slug>/amazon-kdp/ebook/cover.jpg`.
- Amazon KDP paperback: `output/<slug>/amazon-kdp/print/paperback/<slug>-paperback-interior.pdf` and `output/<slug>/amazon-kdp/print/paperback/<slug>-paperback-cover.pdf`.
- Amazon KDP hardcover: `output/<slug>/amazon-kdp/print/hardcover/<slug>-hardcover-interior.pdf` and `output/<slug>/amazon-kdp/print/hardcover/<slug>-hardcover-cover.pdf`.

Flat upload staging was rebuilt at `/tmp/cinderwake-upload-assets` with 33 real, non-empty files and 0 symlinks. It mirrors the KDP, Apple Books, and Google Play Books assets for quick picker access.

Apple Transporter `.itmsp` packages were generated under:

- `output/cinderwake-01-the-ash-beneath-the-crown/apple-books/cinderwake_01_the_ash_beneath_the_crown.itmsp`
- `output/cinderwake-02-the-moon-below-the-world/apple-books/cinderwake_02_the_moon_below_the_world.itmsp`
- `output/cinderwake-03-the-dragon-that-dreamed-death/apple-books/cinderwake_03_the_dragon_that_dreamed_death.itmsp`

Transporter delivery completed on 2026-05-18:

- `The Ash Beneath the Crown` delivered at 8:22 PM MST.
- `The Moon Below the World` delivered at 8:22 PM MST.
- `The Dragon That Dreamed Death` delivered at 8:23 PM MST.

## Store Setup Defaults

- Series: `The Cinderwake Trilogy`
- Author: `Alinari Campbell`
- Publisher/imprint: `PixelPacific` / `PixelPacific Publishing`
- Language: English
- BISAC: `FIC009020` Epic Fantasy, `FIC009100` Fantasy Action & Adventure, `FIC009120` Dragons & Mythical Creatures
- Ebook list price: `$4.99`
- KDP paperback list price: `$17.99`
- KDP hardcover list price: `$27.99`
- Trim/paper: `6 x 9 in`, black-and-white interior, cream paper
- Kindle DRM: `No`
- KDP Select: `No`

## Public-Action Guardrails

- Local prep, draft creation, validation, and save-as-draft/review staging are okay.
- Final `Publish`, `Deliver`, or equivalent live-sale controls should remain a manual/user-confirmed action.
- KDP AI-content disclosure must be completed accurately during upload.

## Local Verification

- `python3 scripts/publish.py inventory`: all three Cinderwake books are discovered as `ready`.
- `python3 scripts/publish.py build --all`: generated Apple Books, Google Play Books, KDP ebook, paperback, and hardcover packages for all three books.
- `python3 scripts/build_apple_itmsp.py --book ... --provider AlinariCampbell --strict`: all three `.itmsp` packages generated with no blockers; expected no-ISBN warnings remain.
- `python3 scripts/publish.py audit-print`: Cinderwake paperback/hardcover covers match generated KDP specs and page counts.
- `unzip -t` on all three KDP ebook EPUBs: no archive errors.
