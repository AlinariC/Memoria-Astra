# Cinderwake Google Play Audiobook Delivery Status

Prepared: 2026-05-21

Last updated: 2026-05-21 15:54 MST

Follow-up updated: 2026-05-22

## Current Partner Center State

- Google Play Books Partner Center exposes audiobook upload tooling for this account.
- The existing live ebook rows remain correct and should not be modified:
  - `GGKEY:YU9XS0DXEUE` - The Ash Beneath the Crown
  - `GGKEY:YZQ7FJBUABQ` - The Moon Below the World
  - `GGKEY:EU9D90XDYUG` - The Dragon That Dreamed Death
- The old cover-only placeholder rows are not usable through CSV conversion. Partner Center still shows them as `Format: Ebook`, and a fresh exported book list reports them as `Unsupported - Unknown book`. They were left untouched after the metadata/content format mismatch became clear.
- Proper audiobook records were created through the Partner Center audiobook flow and linked back to the corresponding ebook rows as alternative formats.
- The new audiobook rows are not publicly published from this workflow. Book 1 and Book 2 are visible in Partner Center as `Needs approval`; Book 3 is complete on the Review page with the `Publish` button still unclicked.

## New Audiobook Records

| Title | New audiobook row | Linked ebook row | Partner Center status | Price | Territories | Public publish clicked |
|---|---|---|---|---:|---|---|
| The Ash Beneath the Crown | `GGKEY:LARYPC5EQEU` | `GGKEY:YU9XS0DXEUE` | `Needs approval` | USD 14.99 | WORLD | No |
| The Moon Below the World | `GGKEY:3JLNSLLZYP9` | `GGKEY:YZQ7FJBUABQ` | `Needs approval` | USD 14.99 | WORLD | No |
| The Dragon That Dreamed Death | `GGKEY:N2RZ7L2S0Y7` | `GGKEY:EU9D90XDYUG` | Ready on Review page; not submitted | USD 14.99 | WORLD | No |

## Shared Audiobook Metadata

- Publisher: `PixelPacific`
- Author: `Alinari Campbell`
- Narrator: `PixelPacific AI Ensemble`
- Narration disclosure: digital/synthesized narration, `Synthesized Voice - Unspecified`
- Release and publication date: `2026-05-21`
- Abridged: No
- Mature content: No
- Default Google Play sample length left unchanged.
- Series search for `The Cinderwake Trilogy`/`Cinderwake` did not surface an existing Partner Center series, so no duplicate series was created.
- Genres:
  - `Fiction / Fantasy / Epic` (`FIC009020`)
  - `Fiction / Fantasy / Action & Adventure` (`FIC009100`)
  - `Fiction / Fantasy / Dragons & Mythical Creatures` (`FIC009120`)

## Placeholder Rows Tested

| Placeholder row | Intended audiobook | Existing ebook row |
|---|---|---|
| `GGKEY:67UBUE7Q2B0` | The Ash Beneath the Crown | `GGKEY:YU9XS0DXEUE` |
| `GGKEY:T7WL07YPJ7Z` | The Moon Below the World | `GGKEY:YZQ7FJBUABQ` |
| `GGKEY:JU2YE1L46Q9` | The Dragon That Dreamed Death | `GGKEY:EU9D90XDYUG` |

## Upload-Ready Files

| Title | Active audiobook row | ZIP | Cover | Google-ready cover | ZIP size |
|---|---|---|---|---|---:|
| The Ash Beneath the Crown | `GGKEY:LARYPC5EQEU` | `output/audiobooks/cinderwake/publishing/google-play-upload-ready/LARYPC5EQEU.zip` | `output/audiobooks/cinderwake/publishing/google-play-upload-ready/LARYPC5EQEU_frontcover.jpg` | `output/audiobooks/cinderwake/publishing/google-play-upload-ready/LARYPC5EQEU_frontcover_2400.jpg` | 1098.3 MB |
| The Moon Below the World | `GGKEY:3JLNSLLZYP9` | `output/audiobooks/cinderwake/publishing/google-play-upload-ready/3JLNSLLZYP9.zip` | `output/audiobooks/cinderwake/publishing/google-play-upload-ready/3JLNSLLZYP9_frontcover.jpg` | `output/audiobooks/cinderwake/publishing/google-play-upload-ready/3JLNSLLZYP9_frontcover_2400.jpg` | 1121.0 MB |
| The Dragon That Dreamed Death | `GGKEY:N2RZ7L2S0Y7` | `output/audiobooks/cinderwake/publishing/google-play-upload-ready/N2RZ7L2S0Y7.zip` | `output/audiobooks/cinderwake/publishing/google-play-upload-ready/N2RZ7L2S0Y7_frontcover.jpg` | `output/audiobooks/cinderwake/publishing/google-play-upload-ready/N2RZ7L2S0Y7_frontcover_2400.jpg` | 1109.7 MB |

Google Play rejected the original larger cover dimensions during the manual flow, so each active audiobook row uses the resized 2400 x 2400 cover file.

## Single-File Fallback Files

On 2026-05-22, Partner Center showed `Needs action` for all three processed
audiobooks with a content-page warning but no obvious visible error. The ZIP
packages validate locally, but a simpler fallback set was staged using Google's
recommended single-file audiobook pattern `ID_1of1.mp3`.

| Title | Active audiobook row | Single-file audio | Audio format | Size |
|---|---|---|---|---:|
| The Ash Beneath the Crown | `GGKEY:LARYPC5EQEU` | `output/audiobooks/cinderwake/publishing/google-play-upload-ready/LARYPC5EQEU_1of1.mp3` | MP3, 44.1 kHz mono, 192 kbps | 1.1 GB |
| The Moon Below the World | `GGKEY:3JLNSLLZYP9` | `output/audiobooks/cinderwake/publishing/google-play-upload-ready/3JLNSLLZYP9_1of1.mp3` | MP3, 44.1 kHz mono, 192 kbps | 1.1 GB |
| The Dragon That Dreamed Death | `GGKEY:N2RZ7L2S0Y7` | `output/audiobooks/cinderwake/publishing/google-play-upload-ready/N2RZ7L2S0Y7_1of1.mp3` | MP3, 44.1 kHz mono, 192 kbps | 1.1 GB |

Recommended recovery path if the Content tab issue remains hidden:

1. Open the audiobook row's `Content` tab.
2. Use the audiobook content-version dropdown to inspect `Pending Content Files`,
   `Draft Content`, and `Disapproved Content`.
3. If an `Issues` tab or issue row appears, record the exact message.
4. If no issue is visible, upload the matching `GGKEY_1of1.mp3` file as a new
   audio version from the Content tab, then submit/review again after processing.

## Metadata Upload Attempts

| Time | File | Rows | Errors | Warnings | Result |
|---|---|---:|---:|---:|---|
| 2026-05-21 14:36 MST | `google-play-audiobook-upload-2026-05-21.csv` | 3 | 0 | 0 | Complete, but placeholder records did not update. |
| 2026-05-21 14:43 MST | `google-play-audiobook-upload-2026-05-21.csv` | 3 | 0 | 0 | Complete after adding runtimes and narrator role, but placeholder records did not update. |
| 2026-05-21 14:47 MST | `google-play-audiobook-upload-2026-05-21-export-base.csv` | 3 | 0 | 0 | Complete using Google-exported status/template fields, but placeholder records still did not update. |

## Metadata Files

- `output/audiobooks/cinderwake/publishing/metadata/google-play-audiobook-upload-2026-05-21.csv` sets `Book Format` to `Audiobook`, includes each runtime, uses `PixelPacific AI Ensemble [Narrator]`, applies worldwide USD pricing at `$14.99`, includes digital narration disclosure, and links each audiobook to its live ebook row.
- `output/audiobooks/cinderwake/publishing/metadata/google-play-audiobook-upload-2026-05-21-export-base.csv` is based on a fresh Partner Center export and preserves Google's exported `Default Settings`/status context for the three placeholder rows.

## Next Action

Do not keep trying CSV conversion on the old placeholder rows. The active Google Play audiobook setup now lives in the three new audiobook records above. Final public submission should only happen after the user chooses to press the Partner Center `Publish` action from the Review page or catalog workflow.
