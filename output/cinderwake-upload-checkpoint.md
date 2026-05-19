# Cinderwake Trilogy Upload Checkpoint

Prepared: 2026-05-19
Apple delivery updated: 2026-05-18 20:23 MST
Google Play Books bulk upload updated: 2026-05-18 21:57 MST

| Package | Title | Kindle | Paperback | Hardcover | Apple Books | Google Play Books |
|---|---|---|---|---|---|---|
| 01 | The Ash Beneath the Crown | Ready: EPUB and cover built; ZIP test passed | Ready: 486-page interior and wrap cover audited | Ready: 486-page interior and wrap cover audited | Delivered through Transporter on 2026-05-18 at 8:22 PM MST | Live on Google Play after repair upload to `GGKEY:YU9XS0DXEUE`; metadata/pricing accepted |
| 02 | The Moon Below the World | Ready: EPUB and cover built; ZIP test passed | Ready: 498-page interior and wrap cover audited | Ready: 498-page interior and wrap cover audited | Delivered through Transporter on 2026-05-18 at 8:22 PM MST | Live on Google Play after repair upload to `GGKEY:YZQ7FJBUABQ`; metadata/pricing accepted |
| 03 | The Dragon That Dreamed Death | Ready: EPUB and cover built; ZIP test passed | Ready: 482-page interior and wrap cover audited | Ready: 482-page interior and wrap cover audited | Delivered through Transporter on 2026-05-18 at 8:23 PM MST | Live on Google Play after repair upload to `GGKEY:EU9D90XDYUG`; metadata/pricing accepted |

## Local Staging Folder

`/tmp/cinderwake-upload-assets` contains 33 real, non-empty upload files and 0 symlinks.

For each title it includes:

- KDP ebook EPUB and cover JPG
- KDP paperback interior PDF and wrap-cover PDF
- KDP hardcover interior PDF and wrap-cover PDF
- Google Play Books EPUB, PDF, and cover JPG
- Apple Books EPUB and cover JPG

## Next Update Rule

After each storefront step, update this checkpoint from the real portal state rather than from expected generator output.

## Completed Apple Books Delivery

- Opened the three generated `.itmsp` packages in the signed-in Transporter app under provider `Alinari Campbell`.
- Delivered `cinderwake_01_the_ash_beneath_the_crown`.
- Delivered `cinderwake_02_the_moon_below_the_world`.
- Delivered `cinderwake_03_the_dragon_that_dreamed_death`.
- Transporter displayed all three Cinderwake titles in the Delivered section with green delivered checks.

## Completed Google Play Books Bulk Upload

- Uploaded the Cinderwake Google EPUB, PDF, and cover files through Partner Center > Book catalog > Advanced options > Upload content files.
- Google assigned the primary content rows `GGKEY:YU9XS0DXEUE`, `GGKEY:YZQ7FJBUABQ`, and `GGKEY:EU9D90XDYUG`.
- Re-uploaded the covers with GGKEY-prefixed filenames so the covers attach to the primary content rows.
- Uploaded `cinderwake-google-play-bulk-metadata-2026-05-18.csv` through Partner Center > Upload book list. Google marked the list `Complete` with `3` rows, `0` errors, and `0` warnings.
- A fresh post-upload book-list export confirmed title, author, subtitle, BISAC subjects, series, volume, release date, DRM, and `$4.99` worldwide USD price for all three primary Cinderwake rows.
- Google later flagged all three primary rows as `Needs Action` with `Internal processing error (001)` and `The image quality is poor - upload a version with higher quality`.
- Repaired the content upload from `/tmp/cinderwake-google-repair` using Google-native primary-row filenames:
  - `YU9XS0DXEUE.epub`, `YU9XS0DXEUE_interior.pdf`, and `YU9XS0DXEUE_frontcover.png`
  - `YZQ7FJBUABQ.epub`, `YZQ7FJBUABQ_interior.pdf`, and `YZQ7FJBUABQ_frontcover.png`
  - `EU9D90XDYUG.epub`, `EU9D90XDYUG_interior.pdf`, and `EU9D90XDYUG_frontcover.png`
- The repair covers are `3000 x 4500` PNGs at 300 dpi, and the rebuilt EPUBs embed those high-resolution covers.
- Partner Center accepted the nine repair files and displayed `Uploaded 9 content files`.
- Partner Center Book catalog now shows all three primary Cinderwake rows as `Live on Google Play` with `$4.99` pricing.
- Do not use the cover-only placeholder rows from the first filename pass as live listings: `GGKEY:67UBUE7Q2B0`, `GGKEY:T7WL07YPJ7Z`, and `GGKEY:JU2YE1L46Q9`.
