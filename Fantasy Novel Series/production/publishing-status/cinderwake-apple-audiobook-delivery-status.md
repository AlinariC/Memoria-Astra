# Cinderwake Apple Audiobook Delivery Status

Updated: 2026-05-21 17:55 MST

## Result

Apple API-key delivery succeeded for all three Cinderwake audiobooks through
Transporter.

The original Apple M4A/AAC package format verified at the metadata level but
failed Apple media validation with an unsupported `aac` codec result. A
temporary codec package confirmed that Transporter accepts a package-local
192 kbps MP3 audiobook track, so the Apple package builder now creates a
full-length MP3 track for each `.itmsp` package while preserving the M4A/M4B
masters alongside the store package.

All three rebuilt `.itmsp` packages passed `iTMSTransporter -m verify`, then
uploaded successfully with the Apple API key stored outside the repo.

## Uploaded Packages

- Book 1, `The Ash Beneath the Crown`: uploaded successfully.
- Book 2, `The Moon Below the World`: uploaded successfully.
- Book 3, `The Dragon That Dreamed Death`: first upload attempt hit a transient
  Apple delivery-service timeout before payload upload; retry uploaded
  successfully.

## Latest Transporter Status

Transporter status checked after upload:

- `cinderwake_audio_01_the_ash_beneath_the_crown`: `In Review`,
  `NotLive-WaitingForReview`, upload state `Imported`, Apple identifier
  `6771994498`.
- `cinderwake_audio_02_the_moon_below_the_world`: `In Review`,
  `NotLive-WaitingForReview`, upload state `Imported`, Apple identifier
  `6771994459`.
- `cinderwake_audio_03_the_dragon_that_dreamed_death`: upload state
  `Imported`, `In Review`, `NotLive-WaitingForReview`, Apple identifier
  `6771995035`.

## Apple-Ready Packages

- `output/audiobooks/cinderwake/publishing/book-01-the-ash-beneath-the-crown/apple-books/cinderwake_audio_01_the_ash_beneath_the_crown.itmsp`
- `output/audiobooks/cinderwake/publishing/book-02-the-moon-below-the-world/apple-books/cinderwake_audio_02_the_moon_below_the_world.itmsp`
- `output/audiobooks/cinderwake/publishing/book-03-the-dragon-that-dreamed-death/apple-books/cinderwake_audio_03_the_dragon_that_dreamed_death.itmsp`

Each package contains:

- `metadata.xml` at package root.
- One 192 kbps MP3 audiobook track under 23 hours.
- One 3000 x 3000 square cover image.
- Chapter markers with millisecond start times.
- Apple digital narration disclosure at the beginning of the description.
- Store product metadata for the configured Apple audiobook territories.

## Logs

Transporter logs are under:

- `output/apple-transporter-logs/`
- `output/apple-transporter-errorlogs/`

Key log files from this run:

- `verify-api-book01-20260521-174836.log`
- `verify-api-book02-20260521-174852.log`
- `verify-api-book03-20260521-174906.log`
- `upload-api-book01-20260521-174948.log`
- `upload-api-book02-20260521-175036.log`
- `upload-api-book03-retry-20260521-175211.log`
- `status-api-cinderwake-20260521-175346.log`
- `status-api-cinderwake-20260521-175438.log`

## Follow-Up

- Review the three audiobook records in Apple Books Connect once processing is
  complete, especially price tier, territory availability, digital narration
  disclosure, and edition linking back to the ebook listings.
