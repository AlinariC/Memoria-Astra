# Cinderwake Audiobook Publishing Readiness

Prepared: 2026-05-21

## Store Package Set

| Book | Runtime | Chapters | List Price | Primary Package Paths |
|---|---:|---:|---:|---|
| 1. The Ash Beneath the Crown | 13:18:03 | 36 | $14.99 | `output/audiobooks/cinderwake/publishing/book-01-the-ash-beneath-the-crown/spotify`, `output/audiobooks/cinderwake/publishing/book-01-the-ash-beneath-the-crown/google-play`, `output/audiobooks/cinderwake/publishing/book-01-the-ash-beneath-the-crown/apple-books` |
| 2. The Moon Below the World | 13:34:52 | 31 | $14.99 | `output/audiobooks/cinderwake/publishing/book-02-the-moon-below-the-world/spotify`, `output/audiobooks/cinderwake/publishing/book-02-the-moon-below-the-world/google-play`, `output/audiobooks/cinderwake/publishing/book-02-the-moon-below-the-world/apple-books` |
| 3. The Dragon That Dreamed Death | 13:26:09 | 41 | $14.99 | `output/audiobooks/cinderwake/publishing/book-03-the-dragon-that-dreamed-death/spotify`, `output/audiobooks/cinderwake/publishing/book-03-the-dragon-that-dreamed-death/google-play`, `output/audiobooks/cinderwake/publishing/book-03-the-dragon-that-dreamed-death/apple-books` |

## Recommended Upload Targets

- Spotify for Authors: use each book's `spotify/` folder, the 3000 x 3000 cover, the chapterized MP3 audio, and the retail sample. Select the digital voice narration disclosure option.
- Google Play Books: use each book's `google-play/` folder. The ZIP contains chapterized MP3 audio; the standalone `_frontcover.jpg` is included for thumbnail upload.
- Apple Books audiobooks: direct Transporter API delivery succeeded on 2026-05-21 using the Apple-ready `apple-books/*.itmsp` packages.
- Amazon/Audible via ACX: use each book's `acx-audible/` folder as a technical package only. ACX has stricter policy and QA gates around digital narration than Spotify/Google/Apple-partner routes, so treat this as staged rather than guaranteed accepted.

## Pricing

- Individual audiobook list price: `$14.99` USD.
- Suggested trilogy bundle or direct-store bundle: `$34.99` USD.
- Keep Google Play's list price no higher than the same audiobook on other platforms.

## Official Portal References

- Spotify/Findaway digital narration support: https://newsroom.spotify.com/2025-02-20/spotify-opens-up-support-for-elevenlabs-audiobook-content/
- Google Play Books audiobook file guidelines: https://support.google.com/books/partner/answer/3424254
- Apple Books audiobook author guidance: https://authors.apple.com/audiobooks
- Apple Books preferred partners: https://itunespartner.apple.com/books/partners
- ACX audio submission requirements: https://www.acx.com/help/acx-audio-submission-requirements/201456300

## Rights And Disclosure

- Author: Alinari Campbell.
- Publisher/imprint: PixelPacific / PixelPacific Publishing.
- Narrator field: PixelPacific AI Ensemble.
- Digital narration disclosure: `This audiobook is narrated by a digital voice.`
- Do not list individual ElevenLabs stock voice names as human narrators.
- Confirm final AI/digital narration disclosure in each portal before submitting for public sale.

## Local Verification

- All three source M4B masters exist and include chapter markers.
- Apple `.itmsp` packages were generated with one full-length 192 kbps MP3 track per title, package-local metadata, package-local cover art, and chapter start times with millisecond precision.
- All three Apple packages passed Transporter verification and were uploaded through the Apple API key route. All three reported `In Review`, `NotLive-WaitingForReview`, and upload state `Imported` after the final status check.
- ACX-style chapter exports are 44.1 kHz mono MP3 at 192 kbps CBR, with short head/tail silence and conservative loudness limiting.
- Square audiobook covers were generated at 3000 x 3000 and 2400 x 2400, plus 1024/512/256/128 icon sizes.
- Retail samples were generated at four minutes thirty seconds for each title.

## Final Human Checks

- Spot-listen to the first minute of each exported upload set after any portal transcoding.
- Verify every portal's digital voice / AI narration disclosure wording after import.
- Use existing ebook listings to link the audiobook edition where the portal supports edition linking.
- Final review, release, and storefront visibility actions should be checked in each portal after delivery.
