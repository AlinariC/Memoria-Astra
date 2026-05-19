# Production Plan

## Length Targets

The trilogy is now built as complete epic first-revision manuscripts, with each
book safely inside the requested 350-600 page range at 250-300 words per page.
The current package target is roughly 105,000-180,000 words per book, with
future expansion focused on scene depth rather than padding.

| Book | Draft Target | Finished Page Range | Structural Goal |
| --- | ---: | ---: | --- |
| Book 1: The Ash Beneath the Crown | 105k-180k | 350-600 | origin, party formation, city rebellion |
| Book 2: The Moon Below the World | 105k-180k | 350-600 | faction war, underworld descent, moral cost |
| Book 3: The Dragon That Dreamed Death | 105k-180k | 350-600 | apocalypse, convergence, final covenant |

## Drafting Structure

Use `manuscript.md` as the canonical source and regenerate chapter files after
every manuscript-level polish pass.

Current output path:

```text
output/
  book-01-the-ash-beneath-the-crown/
    manuscript.md
    metadata.yaml
    chapters/
  book-02-the-moon-below-the-world/
  book-03-the-dragon-that-dreamed-death/
```

Chapter length target: usually 2,500 to 5,500 words, with occasional short
impact chapters when the scene earns the compression.

Current book structure:

- Book One: 1 part, 36 chapters.
- Book Two: 3 parts, 31 chapters.
- Book Three: 6 parts, 41 chapters.

## Revision Passes

1. **Discovery draft:** get the story down; track continuity, but do not polish endlessly.
2. **Structure pass:** fix cause/effect, book arcs, escalation, travel logic, and payoff placement.
3. **Character pass:** deepen motivation, relationship movement, secrets, wounds, and transformations.
4. **World pass:** enrich environments, cultures, food, law, economy, monster ecology, and sensory continuity.
5. **Magic pass:** enforce cinder rules, costs, limits, and consequences.
6. **Line pass:** prose, rhythm, clarity, action choreography, scene openings and endings.
7. **Continuity/copyedit pass:** spelling, grammar, capitalization, style sheet,
   continuity register, and cross-book name/pronoun checks.
8. **Typesetting pass:** front matter, back matter, map placement, print and ebook formatting.

## Front Matter

- Half title
- Title page
- Copyright
- Dedication
- Map
- Optional dramatis personae
- Optional pronunciation guide
- Optional epigraph

## Back Matter

- Acknowledgments
- Glossary
- Optional appendix of realms, orders, and peoples
- Preview of next book for Books One and Two
- About the author
- Also by author

## Continuity Controls

Maintain these documents from the beginning:

- `production/continuity-register.md`
- `production/full-trilogy-review.md`
- `production/trilogy-consistency-polish.md`
- `series_bible/03-character-bible.md`
- `series_bible/01-world-and-magic.md`
- `output/series-production-manifest.yaml`
- A future travel timeline with dates, distances, injuries, and supplies.
- A future glossary and pronunciation guide.

Epic fantasy collapses when nobody knows where the wound, secret, sword, promise, army, or dragon was three chapters ago. Track those early.
