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
- Google Play Books repair/replacement uploads: use the primary `GGKEY` as the filename prefix, send `<GGKEY>.epub`, `<GGKEY>_interior.pdf`, and `<GGKEY>_frontcover.png`, and use a high-resolution `3000 x 4500` front-cover PNG.
- Amazon KDP ebook: `output/<slug>/amazon-kdp/ebook/<slug>.epub` and `output/<slug>/amazon-kdp/ebook/cover.jpg`.
- Amazon KDP paperback: `output/<slug>/amazon-kdp/print/paperback/<slug>-paperback-interior.pdf` and `output/<slug>/amazon-kdp/print/paperback/<slug>-paperback-cover.pdf`.
- Amazon KDP hardcover: `output/<slug>/amazon-kdp/print/hardcover/<slug>-hardcover-interior.pdf` and `output/<slug>/amazon-kdp/print/hardcover/<slug>-hardcover-cover.pdf`.

Flat upload staging was rebuilt at `/tmp/cinderwake-upload-assets` with 33 real, non-empty files and 0 symlinks. It mirrors the KDP, Apple Books, and Google Play Books assets for quick picker access.

KDP-only retry staging was rebuilt at `/tmp/cinderwake-kdp-upload-assets` with 18 real, non-empty files for Kindle eBook, paperback, and hardcover upload:

- `<slug>-kindle-ebook.epub`
- `<slug>-kindle-cover.jpg`
- `<slug>-paperback-interior.pdf`
- `<slug>-paperback-cover.pdf`
- `<slug>-hardcover-interior.pdf`
- `<slug>-hardcover-cover.pdf`

Apple Transporter `.itmsp` packages were generated under:

- `output/cinderwake-01-the-ash-beneath-the-crown/apple-books/cinderwake_01_the_ash_beneath_the_crown.itmsp`
- `output/cinderwake-02-the-moon-below-the-world/apple-books/cinderwake_02_the_moon_below_the_world.itmsp`
- `output/cinderwake-03-the-dragon-that-dreamed-death/apple-books/cinderwake_03_the_dragon_that_dreamed_death.itmsp`

Transporter delivery completed on 2026-05-18:

- `The Ash Beneath the Crown` delivered at 8:22 PM MST.
- `The Moon Below the World` delivered at 8:22 PM MST.
- `The Dragon That Dreamed Death` delivered at 8:23 PM MST.

Google Play Books bulk upload completed on 2026-05-18:

- `The Ash Beneath the Crown`: primary Google row `GGKEY:YU9XS0DXEUE`.
- `The Moon Below the World`: primary Google row `GGKEY:YZQ7FJBUABQ`.
- `The Dragon That Dreamed Death`: primary Google row `GGKEY:EU9D90XDYUG`.
- Initial content upload sent EPUB, PDF, and cover files. Covers were re-sent with GGKEY-prefixed filenames to attach them to the primary content rows.
- Bulk metadata/pricing upload `cinderwake-google-play-bulk-metadata-2026-05-18.csv` completed with `3` rows, `0` errors, and `0` warnings.
- Post-upload export confirms the three primary rows have title metadata, `The Cinderwake Trilogy` series data, and worldwide `$4.99` USD pricing.
- Google later returned `Needs Action` on all three rows for `Internal processing error (001)` plus poor image quality. Repaired through Partner Center > Book catalog > Advanced options > Upload content files with nine files staged in `/tmp/cinderwake-google-repair`.
- The repair set used primary-row filenames: `<GGKEY>.epub`, `<GGKEY>_interior.pdf`, and `<GGKEY>_frontcover.png`. The front covers are `3000 x 4500` PNGs at 300 dpi, and the replacement EPUBs embed the high-resolution covers.
- Partner Center accepted the repair set with `Uploaded 9 content files`.
- Partner Center Book catalog now shows all three primary Cinderwake rows as `Live on Google Play` with `$4.99` pricing.
- Ignore the cover-only placeholder rows created by the first no-ISBN cover filename pass: `GGKEY:67UBUE7Q2B0`, `GGKEY:T7WL07YPJ7Z`, and `GGKEY:JU2YE1L46Q9`.

Amazon KDP publish attempts:

- KDP Bookshelf search for `Cinderwake` returned no existing title shells.
- Creating a new Kindle eBook shell is blocked by KDP's account-side `Title creation limit exceeded` dialog: `The number of books that can be submitted for publishing has been exceeded by this account.`
- No Cinderwake Amazon listings were submitted. Retry from `/tmp/cinderwake-kdp-upload-assets` after the KDP limit clears.
- 2026-05-20 retry: the `Cinderwake` series shell existed in KDP with no description and no books. Book 1 Kindle eBook details were filled for `The Ash Beneath the Crown` with series slot `Cinderwake` book `1`, author, description, rights, categories, keywords, and release-now setting.
- 2026-05-20 retry blocker: both `Save and Continue` and `Save as Draft` returned the same KDP account-side `Title creation limit exceeded` dialog, so the Book 1 shell could not be saved or advanced to content upload.
- No Cinderwake Amazon listings were submitted on 2026-05-20. Retry from `/tmp/cinderwake-kdp-upload-assets` after the KDP title-creation throttle clears.

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
- Google Play Books Partner Center upload history: `cinderwake-google-play-bulk-metadata-2026-05-18.csv` completed with `3` rows, `0` errors, and `0` warnings.
- `unzip -t` on the three Google repair EPUBs in `/tmp/cinderwake-google-repair`: no archive errors.
- Google Play Books Partner Center Book catalog: the three Cinderwake primary rows are `Live on Google Play`.
- `unzip -t` on the three KDP Kindle EPUBs in `/tmp/cinderwake-kdp-upload-assets`: no archive errors.
- KDP Bookshelf: the `Cinderwake` series shell exists, but no Cinderwake book rows could be saved; new title creation is still blocked by Amazon's title creation limit.
