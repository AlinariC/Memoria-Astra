# Cinderwake Spotify And Audible Delivery Status

Prepared: 2026-05-21

Last updated: 2026-05-21 17:16 MST

## Summary

- Spotify for Authors submission is complete for all three Cinderwake audiobooks. *The Ash Beneath the Crown*, *The Moon Below the World*, and *The Dragon That Dreamed Death* all show `Submitted` in the Spotify catalog and are processing for release.
- Audible through ACX is not currently a clean submission lane for these ElevenLabs ensemble productions. ACX public guidance says ACX currently accepts human narration only, with a separate invited narrator voice-replica beta. Do not submit the ElevenLabs digital-voice files to ACX unless Audible/ACX explicitly confirms this is allowed for the account/title.
- No ACX upload was attempted.

## Spotify For Authors

Current state:

- Account is signed in and the Spotify catalog shows `Drafts (3)` because submitted audiobooks remain listed under that tab while processing.
- All three rows show `Submitted`:
  - `The Dragon That Dreamed Death`, *The Cinderwake Trilogy*, Number 3, last updated `May 22, 2026`.
  - `The Moon Below the World`, *The Cinderwake Trilogy*, Number 2, last updated `May 22, 2026`.
  - `The Ash Beneath the Crown`, *The Cinderwake Trilogy*, Number 1, last updated `May 21, 2026`.
- Catalog metadata verified across the three rows: author `Alinari Campbell`, narrator `Digital Voice PixelPacific AI Ensemble`, publisher `PixelPacific`, language `English`, edition `Unabridged`.
- Spotify displayed the post-submit confirmation for Book 3: `Your audiobook has been uploaded`; it says submitted audiobooks can take up to 72 hours to go live.
- Audio upload verification:
  - Book 1: submitted manually by the user.
  - Book 2: uploaded and submitted after user confirmation; review page showed `32 files`, `32 Completed`, `0 Uploading`, `0 Errors`.
  - Book 3: uploaded and submitted after user confirmation; review page showed `42 files`, `42 Completed`, `0 Uploading`, `0 Errors`.

Current Spotify policy notes from official help:

- Audio files can be MP3, WAV, or FLAC.
- Cover art can be PNG or JPEG in a 1:1 aspect ratio, with 3000 x 3000 px recommended.
- A sample file can be provided for listener preview.
- Spotify accepts digital voice narration, including providers like ElevenLabs.
- Spotify currently does not share digital voice narrated audiobooks with INaudio referral partners.
- Direct Spotify upload is non-exclusive, and the rights holder retains ownership.

Local Spotify package readiness:

| Title | Folder | Audio files | Cover | Sample |
|---|---|---:|---|---|
| The Ash Beneath the Crown | `output/audiobooks/cinderwake/publishing/book-01-the-ash-beneath-the-crown/spotify` | 36 | `cinderwake_audio_01_the_ash_beneath_the_crown_cover_3000.jpg` | `retail-sample.mp3` |
| The Moon Below the World | `output/audiobooks/cinderwake/publishing/book-02-the-moon-below-the-world/spotify` | 31 | `cinderwake_audio_02_the_moon_below_the_world_cover_3000.jpg` | `retail-sample.mp3` |
| The Dragon That Dreamed Death | `output/audiobooks/cinderwake/publishing/book-03-the-dragon-that-dreamed-death/spotify` | 41 | `cinderwake_audio_03_the_dragon_that_dreamed_death_cover_3000.jpg` | `retail-sample.mp3` |

Verified locally:

- Spotify chapter MP3 count: 108 total, matching the 36/31/41 chapter metadata.
- Spotify covers are 3000 x 3000 px.
- Retail samples are approximately 270 seconds each and encoded at 192 kbps.

## Audible / ACX

Current state:

- URL opened: `https://www.acx.com/`
- Status: public site reachable; no login or upload attempted.
- Account/title prerequisites:
  - ACX says the account holder must have audio rights.
  - The title must be available as an ebook on Amazon in order to claim it on ACX.
  - If the Cinderwake Kindle editions are not live yet, that is an additional blocker before any ACX title claim.

Policy risk:

- ACX public guidance says it currently accepts human narration only.
- ACX has a narrator voice-replica beta, but that is an ACX-controlled workflow involving invited narrator replicas and ACX production tools.
- The existing Cinderwake audiobook files were produced with an external ElevenLabs ensemble, so they should be treated as technically ACX-shaped but not policy-cleared for Audible.

Local ACX technical package readiness:

| Title | Folder | Audio files | Cover | Sample |
|---|---|---:|---|---|
| The Ash Beneath the Crown | `output/audiobooks/cinderwake/publishing/book-01-the-ash-beneath-the-crown/acx-audible` | 36 | `cinderwake_audio_01_the_ash_beneath_the_crown_cover_2400.jpg` | `retail-sample.mp3` |
| The Moon Below the World | `output/audiobooks/cinderwake/publishing/book-02-the-moon-below-the-world/acx-audible` | 31 | `cinderwake_audio_02_the_moon_below_the_world_cover_2400.jpg` | `retail-sample.mp3` |
| The Dragon That Dreamed Death | `output/audiobooks/cinderwake/publishing/book-03-the-dragon-that-dreamed-death/acx-audible` | 41 | `cinderwake_audio_03_the_dragon_that_dreamed_death_cover_2400.jpg` | `retail-sample.mp3` |

Verified locally:

- ACX chapter MP3 count: 108 total, matching the 36/31/41 chapter metadata.
- Spot-checked first chapter of each book: MP3, 44.1 kHz, mono, 192 kbps.
- Longest ACX chapter file is 2961.84 seconds, under the 120-minute single-file limit.
- ACX covers are 2400 x 2400 px.

## Metadata To Reuse

- Publisher/imprint: `PixelPacific`
- Author: `Alinari Campbell`
- Narrator: `PixelPacific AI Ensemble`
- Series: `The Cinderwake Trilogy`
- Language: `English`
- Abridgement: `Unabridged`
- Release date: `2026-05-21`
- List price: `USD 14.99`
- Digital narration disclosure: `This audiobook is narrated by a digital voice.`
- Primary BISAC subjects:
  - `Fiction / Fantasy / Epic` (`FIC009020`)
  - `Fiction / Fantasy / Action & Adventure` (`FIC009100`)
  - `Fiction / Fantasy / Dragons & Mythical Creatures` (`FIC009120`)

## Next Action

1. Monitor Spotify over the next 72 hours for each title to move from `Submitted`/processing to live availability.
2. Spot-listen after Spotify transcodes the live titles.
3. Treat Audible as blocked pending a human narration plan, an ACX voice-replica route, or written confirmation from Audible/ACX that these ElevenLabs-produced files can be accepted.

## Official References Checked

- Spotify upload help: `https://support.spotify.com/ml-en/authors/article/uploading-audiobooks/`
- Spotify digital voice narration help: `https://support.spotify.com/ml-en/authors/article/digital-voice-narration/`
- Spotify INaudio/referral partner help: `https://support.spotify.com/ml-en/authors/article/getting-your-audiobook-on-other-listening-platforms/`
- Spotify metadata and asset guide: `https://support.spotifycdn.com/pdf/SFA%20Metadata_Asset%20Guide_2024.pdf`
- ACX author workflow: `https://www.acx.com/mp/how-it-works/authors`
- ACX human narration guidance: `https://www.acx.com/mp/blog/all-ears-a-comprehensive-guide-to-reviewing-your-audio`
- ACX narrator voice-replica beta: `https://www.acx.com/mp/blog/now-in-beta-narrator-voice-replicas-on-acx`
- ACX cover art requirements: `https://g-ecx.images-amazon.com/images/G/01/Audible/en_US/acx/pdf/OfficialAudibleCoverArtRequirements.pdf`
