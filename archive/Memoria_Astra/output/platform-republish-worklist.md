# Memoria Astra Platform Republishing Worklist

Live dashboard snapshot: May 2026. Updated after the 2026-05-18 Books 09-16 KDP package rebuild and staging refresh; `output/republishing-progress.md` and `output/kdp-upload-checkpoint.md` are the detailed live ledgers.

## Local Package Set

All local packages were generated under `output/` and each package has platform-specific EPUB, cover, PDF interior, and KDP print cover files.

| Package | Title | Page count | Local status |
|---|---|---:|---|
| 00 | The First Spiral | 393 | Complete |
| 01 | Terra in the Mists | 52 | Complete |
| 02 | Before the Mists | 61 | Complete |
| 03 | Crimson Reliquary | 86 | Complete |
| 04 | Children of the Divide | 76 | Complete |
| 05 | Echoes of Lyra | 74 | Complete |
| 06 | Harmonic Rebirth | 327 | Complete |
| 07 | Foundations of Flame | 120 | Complete |
| 08 | Inheritance of Song | 52 | Complete |
| 09 | The Silent Accord | 53 | Complete |
| 10 | Starforged Thrones | 65 | Complete |
| 11 | Lament of the Shattered Gate | 58 | Complete |
| 12 | Resonance of Ash and Dream | 52 | Complete |
| 13 | The Gathering Spiral | 62 | Complete |
| 14 | The Weeping Crown | 63 | Complete |
| 15 | The Final Loom | 51 | Complete |
| 16 | The Second Spiral | 471 | Complete |

## Recommended Upload Files

For each package:

- Apple Books: `output/<slug>/apple-books/<slug>.epub`, `output/<slug>/apple-books/cover.jpg`
- Google Play Books: `output/<slug>/google-play-books/<slug>.epub`, `output/<slug>/google-play-books/cover.jpg`; upload the PDF only if Google specifically asks for print-style preview or fixed PDF assets.
- Amazon KDP ebook: `output/<slug>/amazon-kdp/ebook/<slug>.epub`, `output/<slug>/amazon-kdp/ebook/cover.jpg`
- Amazon KDP paperback: `output/<slug>/amazon-kdp/print/paperback/<slug>-paperback-interior.pdf`, `output/<slug>/amazon-kdp/print/paperback/<slug>-paperback-cover.pdf`
- Amazon KDP hardcover: generated for every package at `output/<slug>/amazon-kdp/print/hardcover/`, but current KDP upload plan is hardcover only for 00, 06, and 16. Books 09-15 are below KDP's 75-page hardcover minimum and should stay Kindle/paperback unless they are expanded or the plan changes.

## Current Platform Inventory

### Amazon KDP

Confirmed on KDP Bookshelf:

| Package | Title on KDP | Ebook status | Ebook price | Paperback status | Paperback price | Hardcover |
|---|---|---|---:|---|---:|---|
| 08 | Inheritance of Song: Book Eight in the Memoria Astra Cycle | Awaiting review | $0.99 | Awaiting review | $5.99 | Not created |
| 01 | Terra in the Mists: Aru-Solien | Awaiting review for submitted updates | $0.99 | Awaiting review for submitted updates | $6.99 | Not created |
| 02 | Before the Mists | Awaiting review for submitted updates | $0.99 | Awaiting review for submitted updates | $6.99 | Not created |
| 03 | Crimson Reliquary | Awaiting review for submitted updates | $0.99 | Awaiting review for submitted updates | $7.99 | Not created |
| 04 | Children of the Divide | Awaiting review for submitted updates | $0.99 | Awaiting review for submitted updates | $6.99 | Not created |
| 05 | Echoes of Lyra | Awaiting review for submitted updates | $0.99 | Awaiting review for submitted updates | $6.99 | Not created |
| 07 | Foundations of Flame: Book Seven in the Memoria Astra Cycle | Awaiting review for submitted updates | $1.99 | Awaiting review for submitted updates | $7.99 | Not created |
| 00 | The First Spiral: A Memoria Astra Novel | Awaiting review | $3.99 | Awaiting review | $16.99 | Awaiting review, $24.99 |
| 06 | Harmonic Rebirth: Book Six in the Memoria Astra Cycle | Awaiting review for submitted updates | $3.99 | Awaiting review for submitted updates | $14.99 | Awaiting review, $22.99 |

Missing from the completed KDP Bookshelf pass: none for Books 00-08 as of the 2026-05-17 21:11 MST audit. Books 09-16 are the next Amazon creation/upload scope.

KDP hardcover action: create/refresh hardcover only for 00, 06, and 16 in the current pricing plan. Books 09-15 have regenerated local hardcover PDFs, but their page counts are below KDP's current hardcover minimum.

Amazon KDP note: all intended current-pass manuscripts/covers were uploaded and saved as drafts or unpublished changes by Codex. The user reported manual final submission is complete and all titles are awaiting review.

### Google Play Books

Confirmed in Partner Center:

| Package | Title on Google | Status | Price |
|---|---|---|---:|
| 00 | The First Spiral | Live on Google Play | $3.99 |
| 01 | Terra in the Mists: Book One in the Memoria Astra Cycle | Live on Google Play | $0.99 |
| 02 | Before the Mists: Book Two in the Memoria Astra Cycle | Live on Google Play | $0.99 |
| 03 | Crimson Reliquary: Book Three in the Memoria Astra Cycle | Live on Google Play | $0.99 |
| 04 | Children of the Divide: Book Four of the Memoria Astra Cycle | Live on Google Play | $0.99 |
| 05 | Echoes of Lyra: Book Five of the Memoria Astra Cycle | Live on Google Play | $0.99 |
| 06 | Harmonic Rebirth | Live on Google Play | $3.99 |
| 07 | Foundations of Flame | Live on Google Play | $1.99 |
| 08 | Inheritance of Song | Live on Google Play | $0.99 |
| 09 | The Silent Accord: Book Nine in the Memoria Astra Cycle | In process | $0.99 |
| 10 | Starforged Thrones: Book Ten in the Memoria Astra Cycle | In process | $0.99 |
| 11 | Lament of the Shattered Gate: Book Eleven in the Memoria Astra Cycle | In process | $0.99 |
| 12 | Resonance of Ash and Dream: Book Twelve in the Memoria Astra Cycle | In process | $0.99 |
| 13 | The Gathering Spiral: Book Thirteen in the Memoria Astra Cycle | In process | $0.99 |
| 14 | The Weeping Crown: Book Fourteen in the Memoria Astra Cycle | In process | $0.99 |
| 15 | The Final Loom: Book Fifteen in the Memoria Astra Cycle | In process | $0.99 |
| 16 | The Second Spiral: A Memoria Astra Novel | In process | $3.99 |

Missing from Google Play Books catalog: none as of the 2026-05-18 Partner Center check recorded in `output/republishing-progress.md`. Books `09`-`16` are present with accepted metadata/pricing and remain in Google's content-processing queue.

### Apple Books

Confirmed in iTunes Connect:

| Package | Title on Apple | Status |
|---|---|---|
| 00 | The First Spiral | Delivered through Transporter; Waiting for Review in iTunes Connect |
| 01 | Terra in the Mists | Delivered through Transporter; existing Apple ID retained |
| 02 | Before the Mists | Delivered through Transporter |
| 03 | Crimson Reliquary | Delivered through Transporter |
| 04 | Children of the Divide | Delivered through Transporter |
| 05 | Echoes of Lyra | Delivered through Transporter |
| 06 | Harmonic Rebirth | Delivered through Transporter |
| 07 | Foundations of Flame | Delivered through Transporter |
| 08 | Inheritance of Song | Delivered through Transporter |
| 09 | The Silent Accord | Delivered through Transporter |
| 10 | Starforged Thrones | Delivered through Transporter |
| 11 | Lament of the Shattered Gate | Delivered through Transporter |
| 12 | Resonance of Ash and Dream | Delivered through Transporter |
| 13 | The Gathering Spiral | Delivered through Transporter |
| 14 | The Weeping Crown | Delivered through Transporter |
| 15 | The Final Loom | Delivered through Transporter |
| 16 | The Second Spiral | Delivered through Transporter |

Apple Books note: packages `00`-`08` were delivered through Transporter on 2026-05-17 in the morning pass, and packages `09`-`16` were delivered through Transporter on 2026-05-17 at 23:39 MST. Store processing/review may continue after delivery.

## Public-Action Guardrails

Before clicking final platform submission buttons, confirm:

- Ebook prices from `output/pricing-plan.md`
- KDP AI-content attestation answers are accurate
- KDP final submission/publish controls must be clicked manually by the user
- KDP free ISBNs already assigned during this pass: `06` hardcover `9798197416933`, `08` paperback `9798197426697`
