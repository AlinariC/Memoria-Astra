# Memoria Astra Republishing Progress

Started: 2026-05-16 23:45 MST.
Last updated: 2026-05-17 21:36 MST.

## Local Packages

| Scope | Action | Status |
|---|---|---|
| 00-08 | Rebuilt all Apple Books, Google Play Books, and Amazon KDP package folders with Pandoc/XeLaTeX | Complete |
| 00-08 | Ingested the new generated front cover images into each normalized book folder as `cover.jpg` and `cover-300dpi.jpg` | Complete |
| 00-08 | Added missing `metadata.yaml` files/descriptions so every package has the same manuscript, metadata, and cover contract | Complete |
| KDP ebook | Removed the padded/shrunken cover treatment so Kindle cover uploads use the full source front-cover art with no border | Complete |
| KDP paperback | Removed the generated front-cover inset/border so paperback wraps use full-size front cover art on the front panel | Complete |
| KDP print | Fixed stale page-count detection by using macOS PDFKit through Swift before KDP cover generation | Complete |
| KDP print | Switched print interiors to KDP-safe mirrored two-sided margins after Previewer rejected the 06 paperback gutter | Complete |
| KDP print | Removed numbered print headings and tightened section heading line breaking after KDP Previewer rejected `00` page 135 for a long chapter heading outside the margins | Complete |
| KDP print | Replaced the old flat back-cover layout with an image-backed back panel, gold typography, barcode quiet zone, and safer spine treatment | Complete |
| KDP print | Corrected hardback board-wrap/front-panel positioning and moved back-cover copy into explicit safe text boxes after KDP guide review showed the 00 hardback cover was misaligned | Complete |
| KDP print | Preserved the approved hardback cover treatment; current generator uses full-panel/no-border paperback front art, 1.05 in paperback back-copy inset, and 0.72/1.25 in front/back hardcover insets | Complete |
| KDP print | Rebuilt paperback and hardcover wrap covers and refreshed `metadata/kdp-print-cover-specs.json` manifests | Complete |
| KDP print | Ran `python3 scripts/publish.py audit-print` | Pass: all generated interiors match specs and all cover MediaBoxes match KDP sizes |
| KDP print | Ran a PDFKit text-boundary scan for all generated paperback and hardcover interiors | Pass: 18 interiors checked, 0 pages outside KDP minimum safety margins |
| KDP staging | Rebuilt `/tmp/memoria-kdp-upload-assets` with 54 real files, 0 symlinks, all 9 Kindle EPUBs ZIP-verified, and contact sheets rendered for paperback/hardcover wraps | Complete |
| KDP staging | Re-ran final local sanity checks after KDP audit: `python3 scripts/publish.py audit-print`, staging file/symlink/empty-file counts, and all 9 staged Kindle EPUB ZIP tests | Pass at 2026-05-17 21:17 MST |
| Cleanup | Removed legacy `Books/`, ingested `covers/`, old `cover.png`/dated cover variants, and obsolete cover-generation scripts/workflows | Complete |

Latest KDP print rebuild page counts: `00` 393, `01` 52, `02` 61, `03` 86, `04` 76, `05` 74, `06` 327, `07` 120, `08` 52.

## Google Play Books

| Package | Title | Action | Status |
|---|---|---|---|
| 00 | The First Spiral | Created a new Google Play Books ebook shell (`GGKEY:A02YGJX45RY`), filled title/subtitle/description/publisher/page count/dates, added BISAC Science Fiction and Space Opera, added author, created `Memoria Astra Cycle` ebook series shell, uploaded refreshed EPUB/PDF/cover, set worldwide USD list price to $3.99, and clicked Publish after action-time confirmation | Live on Google Play |
| 01 | Terra in the Mists | Uploaded refreshed EPUB/PDF/cover and verified U.S. price at $0.99 | Live on Google Play |
| 02 | Before the Mists | Uploaded refreshed EPUB/PDF/cover and verified U.S. price at $0.99 | Live on Google Play |
| 03 | Crimson Reliquary | Uploaded refreshed EPUB/PDF/cover and verified U.S. price at $0.99 | Live on Google Play |
| 04 | Children of the Divide | Uploaded refreshed EPUB/PDF/cover and changed worldwide USD list price from $4.99 to $0.99 | Live on Google Play |
| 05 | Echoes of Lyra | Uploaded refreshed EPUB/PDF/cover and changed worldwide USD list price from $4.99 to $0.99 | Live on Google Play |
| 06 | Harmonic Rebirth | Filled/verified listing details, uploaded refreshed EPUB/PDF/cover, set worldwide USD list price to $3.99, and clicked Publish after action-time confirmation | Live on Google Play |
| 07 | Foundations of Flame | Created the Google Play Books listing with ISBN `9798281667579`, filled metadata, uploaded refreshed EPUB/PDF/cover, set worldwide USD list price to $1.99, and clicked Publish after action-time confirmation | Live on Google Play |
| 08 | Inheritance of Song | Created a new Google Play Books ebook shell (`GGKEY:U06Z1PYBT8H`), filled metadata, skipped series association, uploaded refreshed EPUB/PDF/cover, set worldwide USD list price to $0.99, and clicked Publish after action-time confirmation | Live on Google Play |

Google Play Books result: all 9 catalog entries were confirmed `Live on Google Play` in Partner Center on 2026-05-17.

## Amazon KDP

| Package | Format | Action | Status |
|---|---|---|---|
| 07 Foundations of Flame | Kindle eBook | Current confirmed pass uploaded `07-foundations-of-flame-ebook.epub` and full-size no-border `07-foundations-of-flame-ebook-cover.jpg`, confirmed duplicate AI/accuracy attestations, KDP conversion and quality check completed with no spelling or image issues, verified 35% royalty and Amazon.com Kindle price `$1.99` | Draft saved in KDP at 2026-05-17 19:13 MST; final publish click remains manual |
| 07 Foundations of Flame | Paperback | Current confirmed pass uploaded `07-foundations-of-flame-paperback-interior.pdf` and no-border full-panel `07-foundations-of-flame-paperback-cover.pdf`, confirmed AI attestation, approved KDP Print Previewer with guides visible at `Cover / 120`, verified only the recurring font-embedding notice, summary page count 120, Amazon.com printing cost `$2.44`, glossy finish from the existing listing, and Amazon.com list price `$7.99` | Draft saved in KDP at 2026-05-17 19:19 MST; final publish click remains manual |
| 08 Inheritance of Song | Kindle eBook | Created new Kindle draft `A1NE6AVK1RIKL2`, uploaded `08-inheritance-of-song-ebook.epub` and full-size no-border `08-inheritance-of-song-ebook-cover.jpg`, confirmed AI disclosure/accuracy attestation, set DRM to no, publisher to `PixelPacific`, KDP Select off, worldwide rights, 35% royalty, and Amazon.com Kindle price `$0.99`; KDP quality check showed non-blocking `5` possible spelling errors | Draft saved in KDP at 2026-05-17 20:54 MST; final publish click remains manual |
| 08 Inheritance of Song | Paperback | Created new paperback draft `TEX2F46X5RR`, assigned free KDP ISBN `9798197426697`, uploaded `08-inheritance-of-song-paperback-interior.pdf` and no-border full-panel `08-inheritance-of-song-paperback-cover.pdf`, confirmed AI disclosure, approved KDP Print Previewer with guides visible at `Cover / 52`, verified only the recurring font-embedding notice, summary page count 52, Amazon.com printing cost `$2.30`, worldwide rights, and Amazon.com paperback price `$5.99`; no hardcover draft created because the local page count is below KDP hardcover eligibility | Draft saved in KDP at 2026-05-17 21:09 MST; final publish click remains manual |
| 06 Harmonic Rebirth | Kindle eBook | Uploaded refreshed EPUB and cover, set AI attestation, set Amazon.com Kindle price to $3.99 | Unpublished changes saved in KDP at 2026-05-17 18:23 MST; final publish click remains manual |
| 06 Harmonic Rebirth | Paperback | Uploaded latest corrected `06-harmonic-rebirth-paperback-interior.pdf` and `06-harmonic-rebirth-paperback-cover.pdf`, confirmed AI attestation, approved KDP Print Previewer with guides visible, verified page range `Cover / 327`, summary page count 327, and Amazon.com printing cost `$4.92` | Unpublished changes saved in KDP at 2026-05-17 18:30 MST; final publish click remains manual |
| 06 Harmonic Rebirth | Hardcover | Created KDP hardcover draft from the Bookshelf `+ Create hardcover` path, assigned free KDP ISBN `9798197416933`, uploaded `06-harmonic-rebirth-hardcover-interior.pdf` and `06-harmonic-rebirth-hardcover-cover.pdf`, set cream/no-bleed/matte 6x9 case-laminate print options, confirmed AI disclosure, approved KDP Print Previewer with guides visible at `Cover / 327`, verified print cost `$9.57`, and set Amazon.com list price to `$22.99` | Draft saved in KDP at 2026-05-17 18:42 MST; final publish click remains manual |
| 05 Echoes of Lyra | Kindle eBook | Current confirmed pass uploaded `05-echoes-of-lyra-ebook.epub` and full-size no-border `05-echoes-of-lyra-ebook-cover.jpg`, confirmed duplicate AI/accuracy attestations, KDP conversion and quality check completed with no spelling or image issues, verified 35% royalty and Amazon.com Kindle price `$0.99` | Draft saved in KDP at 2026-05-17 19:25 MST; final publish click remains manual |
| 05 Echoes of Lyra | Paperback | Current confirmed pass uploaded `05-echoes-of-lyra-paperback-interior.pdf` and no-border full-panel `05-echoes-of-lyra-paperback-cover.pdf`, confirmed AI attestation, approved KDP Print Previewer with guides visible at `Cover / 74`, verified summary page count 74, Amazon.com printing cost `$2.30`, glossy finish from the existing listing, and Amazon.com list price `$6.99` | Draft saved in KDP at 2026-05-17 19:34 MST; final publish click remains manual |
| 04 Children of the Divide | Kindle eBook | Current confirmed pass uploaded `04-children-of-the-divide-ebook.epub` and full-size no-border `04-children-of-the-divide-ebook-cover.jpg`, confirmed duplicate AI/accuracy attestations, KDP conversion and quality check completed with no spelling or image issues, verified 35% royalty and Amazon.com Kindle price `$0.99` | Draft saved in KDP at 2026-05-17 19:38 MST; final publish click remains manual |
| 04 Children of the Divide | Paperback | Current confirmed pass uploaded `04-children-of-the-divide-paperback-interior.pdf` and no-border full-panel `04-children-of-the-divide-paperback-cover.pdf`, confirmed AI attestation, approved KDP Print Previewer with guides visible at `Cover / 76`, verified only the recurring font-embedding notice, summary page count 76, Amazon.com printing cost `$2.30`, and Amazon.com list price `$6.99` | Draft saved in KDP at 2026-05-17 19:56 MST; final publish click remains manual |
| 03 Crimson Reliquary | Kindle eBook | Current confirmed pass uploaded `03-crimson-reliquary-ebook.epub` and full-size no-border `03-crimson-reliquary-ebook-cover.jpg`, confirmed duplicate AI/accuracy attestations, KDP conversion and quality check completed with no spelling or image issues, verified 35% royalty and Amazon.com Kindle price `$0.99` | Draft saved in KDP at 2026-05-17 20:02 MST; final publish click remains manual |
| 03 Crimson Reliquary | Paperback | Current confirmed pass uploaded `03-crimson-reliquary-paperback-interior.pdf` and no-border full-panel `03-crimson-reliquary-paperback-cover.pdf`, confirmed AI attestation, approved KDP Print Previewer with guides visible at `Cover / 86`, verified only the recurring font-embedding notice, summary page count 86, Amazon.com printing cost `$2.30`, glossy finish from the existing listing, and Amazon.com list price `$7.99` | Draft saved in KDP at 2026-05-17 20:10 MST; final publish click remains manual |
| 02 Before the Mists | Kindle eBook | Current confirmed pass uploaded `02-before-the-mists-ebook.epub` and full-size no-border `02-before-the-mists-ebook-cover.jpg`, confirmed duplicate AI/accuracy attestations, KDP conversion and quality check completed with no spelling or image issues, verified 35% royalty and Amazon.com Kindle price `$0.99` | Draft saved in KDP at 2026-05-17 20:16 MST; final publish click remains manual |
| 02 Before the Mists | Paperback | Current confirmed pass uploaded `02-before-the-mists-paperback-interior.pdf` and no-border full-panel `02-before-the-mists-paperback-cover.pdf`, confirmed AI attestation, approved KDP Print Previewer with guides visible at `Cover / 61`, verified only the recurring font-embedding notice, summary page count 61, Amazon.com printing cost `$2.30`, glossy finish from the existing listing, Expanded Distribution from the existing listing, and Amazon.com list price `$6.99` | Draft saved in KDP at 2026-05-17 20:25 MST; final publish click remains manual |
| 01 Terra in the Mists | Kindle eBook | Current confirmed pass uploaded `01-terra-in-the-mists-ebook.epub` and full-size no-border `01-terra-in-the-mists-ebook-cover.jpg`, confirmed duplicate AI/accuracy attestations, KDP conversion and quality check completed with no spelling or image issues, verified 35% royalty and Amazon.com Kindle price `$0.99` | Draft saved in KDP at 2026-05-17 20:30 MST; final publish click remains manual |
| 01 Terra in the Mists | Paperback | Current confirmed pass uploaded `01-terra-in-the-mists-paperback-interior.pdf` and no-border full-panel `01-terra-in-the-mists-paperback-cover.pdf`, confirmed AI attestation, approved KDP Print Previewer with guides visible at `Cover / 52`, verified only the recurring font-embedding notice, summary page count 52, Amazon.com printing cost `$2.30`, glossy finish from the existing listing, Expanded Distribution from the existing listing, and Amazon.com list price `$6.99` | Draft saved in KDP at 2026-05-17 20:37 MST; final publish click remains manual |
| 00 The First Spiral | Kindle eBook | Current confirmed pass uploaded `00-the-first-spiral-ebook.epub` and full-size no-border `00-the-first-spiral-ebook-cover.jpg`, confirmed duplicate AI attestations, KDP conversion completed with the same non-blocking `29` possible spelling errors, verified Amazon.com Kindle price at `$3.99` on the 70% royalty plan | Draft saved in KDP at 2026-05-17 18:49 MST; final publish click remains manual |
| 00 The First Spiral | Paperback | Current confirmed pass uploaded `00-the-first-spiral-paperback-interior.pdf` and no-border full-panel `00-the-first-spiral-paperback-cover.pdf`, confirmed AI attestation, approved KDP Print Previewer with guides visible at `Cover / 393`, verified summary page count 393, Amazon.com printing cost `$5.72`, set Amazon.com list price to `$16.99`, and verified KDP's draft-saved banner | Draft saved in KDP at 2026-05-17 18:59 MST; final publish click remains manual |
| 00 The First Spiral | Hardcover | Current confirmed pass uploaded `00-the-first-spiral-hardcover-interior.pdf` and `00-the-first-spiral-hardcover-cover.pdf`, confirmed KDP ISBN `9798197379412`, confirmed black-and-white cream/no-bleed/matte 6x9 case-laminate settings, approved KDP Print Previewer with guides visible at `Cover / 393`, verified summary page count 393 and Amazon.com printing cost `$10.37`, set Amazon.com list price to `$24.99`, corrected marketplace-derived pricing, and verified KDP's draft-saved banner | Draft saved in KDP at 2026-05-17 19:09 MST; final publish click remains manual |

Amazon KDP result: final Bookshelf audit completed on 2026-05-17 21:11 MST. All intended Amazon formats for `00` through `08` had current-pass manuscripts/covers staged and saved as drafts or unpublished changes, with no final publish/submission clicks made by Codex. KDP displayed those latest modifications as May 18, 2026.

Post-submission update: on 2026-05-17 21:36 MST, the user reported that all KDP drafts had been manually published/submitted and are awaiting review.

Remaining KDP work: wait for review results and address any KDP review issues if they appear.

Live KDP upload state and the final Bookshelf audit table are tracked in `output/kdp-upload-checkpoint.md`.

## Apple Books

Local Apple Books Transporter packages have been generated for every book under `output/*/apple-books/*.itmsp`.

Transporter provider and package status:

- Provider short name verified from Transporter auth logs: `AlinariCampbell`.
- `01 Terra in the Mists` uses the existing Apple Books vendor ID `10083606179` for its update package.
- Apple rejected the first regenerated packages for publication metadata schema details; `scripts/build_apple_itmsp.py` was corrected to emit `identifier scheme="isbn13"`, `languages/language type="main"`, and `description format="plain"`.
- Apple rejected hyphenated vendor IDs for the two ISBN-less packages; `00 The First Spiral` now uses `memoria_astra_00_the_first_spiral`, and `08 Inheritance of Song` now uses `memoria_astra_08_inheritance_of_song`.
- All 9 `.itmsp` packages (`00`-`08`) were regenerated locally with the new covers and delivered through Transporter on 2026-05-17.
- Transporter showed successful delivered states for all 9 Apple packages: `00`, `01`, `02`, `03`, `04`, `05`, `06`, `07`, and `08`.
- `00 The First Spiral` and `08 Inheritance of Song` still have no ISBNs; Apple accepts ISBN-less books, but the underscore vendor IDs above are now the permanent Apple package IDs and must remain stable.
- iTunes Connect picked up the deliveries and assigned/confirmed Apple IDs. Recent Activity shows most delivered packages as `Not on 1 Store` while Apple review/store processing catches up; `00 The First Spiral` detail page shows Review Status `Waiting for Review`, United States rights cleared for sale, DRM enabled, and Tier 4 ($3.99 USD).

## Notes

- KDP print covers now use the actual PDF page counts, not word-count estimates. This prevents the stale-cover-size failure that initially occurred on the 07 paperback upload.
- Rebuilding book 03 corrected the stray `interior 2.pdf` print filenames; `python3 scripts/publish.py audit-print` now passes for every generated paperback and hardcover package.
- Google Play content processing can take time. Newly uploaded replacement rows may show "Completed step 1 of 6" before full availability changes.
