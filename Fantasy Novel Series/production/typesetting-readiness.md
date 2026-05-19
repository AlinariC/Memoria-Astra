# Typesetting Readiness Pass 01

Date: 2026-05-18

## Result

The trilogy output folders have been normalized for first-pass typesetting readiness while preserving the requested `manuscript.md` and `metadata.yaml` package shape.

## Book Package Summary

| Book | Chapters | Words | Estimated Pages |
| --- | ---: | ---: | ---: |
| The Ash Beneath the Crown | 36 | 106,801 | 356-427 |
| The Moon Below the World | 31 | 104,940 | 350-420 |
| The Dragon That Dreamed Death | 41 | 106,158 | 354-425 |

## Normalizations

- No structural manuscript fixes were required.
- Refreshed all book metadata to `complete bespoke first revision` status.
- Standardized target page/word range metadata to the requested 350-600 page epic range.
- Refreshed the output README and generated `output/series-production-manifest.yaml`.

## Validation

- Each manuscript has exactly one title heading and one reader-facing glossary/back matter section.
- Chapter sequences match the expected chapter counts.
- All books remain above the 350-page lower bound at 300 words per page.
- Chapter split workflow now emits `000-front-matter.md`, standalone part files, chapter files, and `999-back-matter.md`.

## Optional Publishing Platform Decisions

1. Choose final export targets: Markdown-only, DOCX, PDF, EPUB, or print-layout source.
2. Add publisher-specific copyright, ISBN, dedication, title-page styling, or map assets if required by the platform.
3. Keep `production/publishing-readiness-final.md` as the final handoff checklist for this manuscript pass.
