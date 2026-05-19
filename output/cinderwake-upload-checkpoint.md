# Cinderwake Trilogy Upload Checkpoint

Prepared: 2026-05-19
Apple delivery updated: 2026-05-18 20:23 MST
Google Play Books bulk upload updated: 2026-05-18 21:40 MST

| Package | Title | Kindle | Paperback | Hardcover | Apple Books | Google Play Books |
|---|---|---|---|---|---|---|
| 01 | The Ash Beneath the Crown | Ready: EPUB and cover built; ZIP test passed | Ready: 486-page interior and wrap cover audited | Ready: 486-page interior and wrap cover audited | Delivered through Transporter on 2026-05-18 at 8:22 PM MST | Bulk uploaded to Google row `GGKEY:YU9XS0DXEUE`; metadata/pricing accepted; status `In process` |
| 02 | The Moon Below the World | Ready: EPUB and cover built; ZIP test passed | Ready: 498-page interior and wrap cover audited | Ready: 498-page interior and wrap cover audited | Delivered through Transporter on 2026-05-18 at 8:22 PM MST | Bulk uploaded to Google row `GGKEY:YZQ7FJBUABQ`; metadata/pricing accepted; status `In process` |
| 03 | The Dragon That Dreamed Death | Ready: EPUB and cover built; ZIP test passed | Ready: 482-page interior and wrap cover audited | Ready: 482-page interior and wrap cover audited | Delivered through Transporter on 2026-05-18 at 8:23 PM MST | Bulk uploaded to Google row `GGKEY:EU9D90XDYUG`; metadata/pricing accepted; status `In process` |

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
- Partner Center currently shows the three primary rows as `In process` while Google finishes content processing.
- Do not use the cover-only placeholder rows from the first filename pass as live listings: `GGKEY:67UBUE7Q2B0`, `GGKEY:T7WL07YPJ7Z`, and `GGKEY:JU2YE1L46Q9`.
