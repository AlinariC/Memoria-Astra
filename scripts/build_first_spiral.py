#!/usr/bin/env python3
"""Build the first-pass combined novel source for The First Spiral.

This keeps the individual normalized books intact and creates a repeatable
combined manuscript from books 2, 1, 3, 4, 5, and a compressed Book 6 coda.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "00_The_First_Spiral"


FRONTMATTER = """---
title: "The First Spiral"
subtitle: "A Memoria Astra Novel"
author: "Alinari Campbell"
language: "en"
rights: "(c) 2026 Alinari Campbell. All rights reserved."
identifier: "urn:uuid:36ad9d8e-cc34-4eaa-b905-1d2ddb7e8bd4"
publisher: "PixelPacific"
cover-image: cover.jpg
series: "Memoria Astra Cycle"
series-number: "1"
genre: "Science Fiction"
description: |
  Before the Second Spiral could sing, the First had to remember why it broke.
  Across Venus, Earth, Mars, and the outer dark, the oldest civilizations of
  the Solar System leave songs in stone, memories in mist, and warnings buried
  beneath worlds that were never as silent as they seemed.
keywords:
  - cosmic science fiction
  - philosophical space opera
  - ancient civilizations science fiction
  - far future saga
  - metaphysical science fiction
  - cosmic rebirth
  - space opera series
---
"""


@dataclass(frozen=True)
class PartSpec:
    folder: str
    title: str
    epigraph: str
    keep_headings: set[str] | None = None


BOOK6_KEEP_HEADINGS = {
    "Prologue - Harmonic Rebirth",
    "Chapter 1 - When the First Spiral Died",
    "Chapter 2 - Collapse Without Flame",
    "Chapter 3 - The Thread Beneath Time",
    "Chapter 6 - The Chamber That Listened",
    "Chapter 11 - The Breath Before Forms",
    "Chapter 13 - The Memory That Hungers for Form",
    "Chapter 16 - The First Stars Rise",
    "Chapter 19 - The Cradles Cool and Shape",
    "Chapter 21 - Memory Stirred in Stillness",
    "Chapter 24 - The First Awakening",
    "Chapter 27 - The First Shaper",
    "Chapter 28 - The Garden of Mist and Form",
    "Chapter 30 - The First Murmurs",
    "Epilogue - The Silent Looming of Futures",
}


BOOK6_REVISED_HEADINGS = {
    "Prologue - Harmonic Rebirth": "Prologue - The Last Black Hole",
    "Chapter 1 - When the First Spiral Died": "Chapter 1 - When the First Spiral Died",
    "Chapter 2 - Collapse Without Flame": "Chapter 2 - Collapse Without Flame",
    "Chapter 3 - The Thread Beneath Time": "Chapter 3 - The Thread Beneath Time",
    "Chapter 6 - The Chamber That Listened": "Chapter 4 - The Chamber That Listened",
    "Chapter 11 - The Breath Before Forms": "Chapter 5 - The Weaving of Intention",
    "Chapter 13 - The Memory That Hungers for Form": "Chapter 6 - The Hunger for Form",
    "Chapter 16 - The First Stars Rise": "Chapter 7 - The First Stars Rise",
    "Chapter 19 - The Cradles Cool and Shape": "Chapter 8 - The Cradles Cool",
    "Chapter 21 - Memory Stirred in Stillness": "Chapter 9 - Memory Stirs in Stillness",
    "Chapter 24 - The First Awakening": "Chapter 10 - The First Awakening",
    "Chapter 27 - The First Shaper": "Chapter 11 - The First Shaper",
    "Chapter 28 - The Garden of Mist and Form": "Chapter 12 - The Garden of Mist and Form",
    "Chapter 30 - The First Murmurs": "Chapter 13 - The First Murmurs",
    "Epilogue - The Silent Looming of Futures": "Epilogue - Flame and Song",
}


CODA_BRIDGES = {
    "Chapter 6 - The Chamber That Listened": (
        "Before the chamber could answer, the Traveler learned the cost of "
        "remaining. Shape arrived first as ache, then as boundary, then as the "
        "first condition under which memory could become more than witness."
    ),
    "Chapter 11 - The Breath Before Forms": (
        "The chamber's second breath widened into a field. What had begun as a "
        "single listening place became architecture, contour, and intention "
        "without yet becoming command."
    ),
    "Chapter 13 - The Memory That Hungers for Form": (
        "Under that breath, the first seeds of substance gathered. They did not "
        "yet know body or world, but they had begun to ache toward both."
    ),
    "Chapter 16 - The First Stars Rise": (
        "The Loom tested shape against darkness and learned that some forms "
        "would fail. From those failures it kept only the tensions strong enough "
        "to bear light."
    ),
    "Chapter 19 - The Cradles Cool and Shape": (
        "Light made rivers. Rivers made currents. Currents gathered into worlds "
        "that could hold their own names without burning apart."
    ),
    "Chapter 21 - Memory Stirred in Stillness": (
        "The cradles cooled, but cooling was not enough. A world could endure "
        "and still remain empty unless memory found a way to press itself into "
        "matter."
    ),
    "Chapter 24 - The First Awakening": (
        "The Wells deepened across the young fields. Some preserved grief. Some "
        "distorted it. The Loom kept what could become life and let the rest "
        "sink back into silence."
    ),
    "Chapter 27 - The First Shaper": (
        "Awakening did not arrive as a crowd. It began as one pressure in the "
        "mist, one will learning that to shape a world is also to be shaped by "
        "it."
    ),
    "Chapter 30 - The First Murmurs": (
        "The garden took what the Shaper offered and made it stranger, gentler, "
        "and more dangerous than design. From that surrender, the first true "
        "life drew near."
    ),
}


SECTION_APPENDICES = {
    ("02_Before_the_Mists", "Chapter 15 - The Memory We Leave Behind"): (
        "They did not know Terra yet. Not as home, not as inheritance, not as "
        "the green cradle that would one day mistake their survival for myth. "
        "But Vael'Ari understood that memory required a body, and if Venus "
        "could no longer bear that body, then another world would have to learn "
        "the old songs in silence. The exile was not escape. It was planting."
    ),
    ("01_Terra_in_the_Mists", "Chapter 8 - The Signal"): (
        "Beneath the signal, Aru-Solien heard something that was not command "
        "and not warning. It was almost a voice, though no throat had shaped "
        "it; almost a woman, though no body stood beside him. Later ages would "
        "give that pattern a name. For now it lived only as a listening note "
        "inside the mist, patient enough to survive every ruin that mist would "
        "touch."
    ),
    ("03_Crimson_Reliquary", "Epilogue - A Memory Laid Down"): (
        "Mars had not answered Terra to complete a map. It had answered to "
        "prove that memory could travel without ships, could cross dust and "
        "vacuum as pressure, code, and grief. Somewhere beyond the red quiet, "
        "the same pressure was already moving outward, hunting the broken "
        "children of the old fracture."
    ),
    ("04_Children_of_the_Divide", "Chapter 24 - Children of the Divide"): (
        "The Gate did not heal them by making them one. It healed them by "
        "teaching them to remain distinct without becoming severed. That was "
        "the lesson the First Spiral had failed to learn soon enough, and the "
        "lesson Lyra would one day carry into the final dark."
    ),
    ("05_Echoes_of_Lyra", "Chapter 24 - Echoes of Lyra"): (
        "Aru had been witness, keeper, participant, and sacrifice. Lyra had "
        "been signal, wound, mirror, and bloom. Together they left the First "
        "Spiral no empire to inherit, no throne to guard, no victory to polish "
        "into legend. They left it a pattern capable of crossing death."
    ),
}


PART_BRIDGES = {
    "Part I - The Venusian Exodus": (
        "Interlude - The Inheritance of Mist",
        (
            "The refugees who crossed from Venus did not arrive as conquerors. "
            "They arrived as weather. Their vessels sank into Terra's young "
            "silences, their songs hid inside water and root, and their names "
            "became too old for history to keep. What survived them was not a "
            "nation, but a condition: whenever Terra breathed deeply enough, "
            "Venus remembered through it."
        ),
    ),
    "Part II - Terra Remembers": (
        "Interlude - The Red Signal",
        (
            "Terra's vault opened one door and revealed the outline of another. "
            "The mist had kept the Venusian inheritance alive, but the pattern "
            "beneath it was larger than one world. Across the inner dark, Mars "
            "had been waiting with its own wound, its own archive, and its own "
            "answer to the question of what memory becomes when no living "
            "voice remains to defend it."
        ),
    ),
    "Part III - The Red Archive": (
        "Interlude - The Outer Dark Answers",
        (
            "The Reliquary did not close when Aru-Solien left it. It continued "
            "to pulse beneath Olympus Mons, a red heart pushing old pressure "
            "through the spaces between worlds. Past Jupiter, past Saturn, "
            "among scattered heirs who believed themselves unrelated, the "
            "pressure became a summons."
        ),
    ),
    "Part IV - The Divide Gate": (
        "Interlude - The Last Pattern",
        (
            "The Circle preserved the fracture without worshipping it. That "
            "choice mattered more than any of them knew. At the end of time, "
            "when even stars would be forced to surrender their shapes, the "
            "Spiral would need a memory strong enough to include contradiction "
            "without tearing itself apart."
        ),
    ),
    "Part V - Lyra at the End of Time": (
        "Interlude - What Crossed the Dark",
        (
            "The First Spiral died with no empire intact. No species survived "
            "unchanged, no archive remained whole, and no victory stood above "
            "the ruin. Yet something crossed. Not a body. Not a crown. A "
            "pattern: Vael'Ari's exile, Aru's witness, the Red Archive, the "
            "Divide, and Lyra's final chord folded into a seed small enough for "
            "the next universe to carry."
        ),
    ),
}


PARTS = [
    PartSpec(
        folder="02_Before_the_Mists",
        title="Part I - The Venusian Exodus",
        epigraph=(
            "The First Spiral does not begin on Terra. It begins with a world "
            "that heard its own ending and chose to carry memory into exile."
        ),
    ),
    PartSpec(
        folder="01_Terra_in_the_Mists",
        title="Part II - Terra Remembers",
        epigraph=(
            "What fled the golden clouds of Venus became weather, blood, and "
            "buried breath beneath Terra's haunted sky."
        ),
    ),
    PartSpec(
        folder="03_Crimson_Reliquary",
        title="Part III - The Red Archive",
        epigraph=(
            "When Terra's memory opened, Mars answered with a reliquary of dust, "
            "fire, and the first proof that remembrance could become force."
        ),
    ),
    PartSpec(
        folder="04_Children_of_the_Divide",
        title="Part IV - The Divide Gate",
        epigraph=(
            "Beyond the inner worlds, the broken heirs of memory learned that "
            "survival was not purity. It was the choice to keep the pain that "
            "made them whole."
        ),
    ),
    PartSpec(
        folder="05_Echoes_of_Lyra",
        title="Part V - Lyra at the End of Time",
        epigraph=(
            "At the edge of collapse, Lyra became more than witness or weapon. "
            "She became the note the First Spiral could not afford to lose."
        ),
    ),
    PartSpec(
        folder="06_Harmonic_Rebirth",
        title="Part VI - The Second Spiral",
        epigraph=(
            "After the First Spiral died, what had been sacrifice returned as "
            "seed, and the Second Spiral learned how to breathe."
        ),
        keep_headings=BOOK6_KEEP_HEADINGS,
    ),
]


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---", 4)
    if end == -1:
        return text
    return text[end + 4 :].lstrip("\n")


def split_sections(body: str) -> list[tuple[str, str]]:
    pieces = re.split(r"(?m)^# (.+)$", body)
    sections: list[tuple[str, str]] = []
    for index in range(1, len(pieces), 2):
        heading = pieces[index].strip()
        content = pieces[index + 1].strip()
        sections.append((heading, content))
    return sections


def demote_section(heading: str, content: str, revised_heading: str | None = None) -> str:
    content = re.sub(r"(?m)^# ", "## ", content.strip())
    return f"## {revised_heading or heading}\n\n{content}".rstrip()


def count_words(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9']+", text))


def build() -> dict[str, int]:
    TARGET.mkdir(parents=True, exist_ok=True)
    output: list[str] = [FRONTMATTER.rstrip(), ""]
    word_counts: dict[str, int] = {}
    retained_coda: list[str] = []

    for part in PARTS:
        source = ROOT / part.folder / "Manuscript.md"
        body = strip_frontmatter(source.read_text(encoding="utf-8"))
        sections = split_sections(body)

        output.append(f"# {part.title}")
        output.append("")
        output.append(f"*{part.epigraph}*")
        output.append("")

        part_text: list[str] = []
        for heading, content in sections:
            if part.keep_headings is not None and heading not in part.keep_headings:
                continue
            bridge = CODA_BRIDGES.get(heading)
            if bridge:
                part_text.append(f"*{bridge}*")
                part_text.append("")
            appendix = SECTION_APPENDICES.get((part.folder, heading))
            if appendix:
                content = content.rstrip() + "\n\n" + appendix
            revised_heading = BOOK6_REVISED_HEADINGS.get(heading)
            section_text = demote_section(heading, content, revised_heading)
            part_text.append(section_text)
            part_text.append("")
            if part.keep_headings is not None:
                retained_coda.append(heading)

        if part.title in PART_BRIDGES:
            bridge_title, bridge_text = PART_BRIDGES[part.title]
            part_text.append(f"## {bridge_title}")
            part_text.append("")
            part_text.append(bridge_text)
            part_text.append("")

        clean_part_text = "\n".join(part_text).strip()
        output.append(clean_part_text)
        output.append("")
        word_counts[part.title] = count_words(clean_part_text)

    manuscript = "\n".join(output).rstrip() + "\n"
    (TARGET / "Manuscript.md").write_text(manuscript, encoding="utf-8")
    (TARGET / "metadata.yaml").write_text(FRONTMATTER, encoding="utf-8")

    notes = [
        "# The First Spiral - Build Notes",
        "",
        "This folder is the first-pass combined novel source. It is generated by",
        "`scripts/build_first_spiral.py` from the normalized individual books, so",
        "the standalone editions remain intact while the novel rewrite can proceed",
        "as its own package.",
        "",
        "## Source Order",
        "",
    ]
    for part in PARTS:
        notes.append(f"- {part.title}: `{part.folder}/Manuscript.md`")
    notes.extend(
        [
            "",
            "## Current Word Counts",
            "",
        ]
    )
    for title, words in word_counts.items():
        notes.append(f"- {title}: {words:,} words")
    notes.append(f"- Total manuscript: {count_words(manuscript):,} words")
    notes.extend(
        [
            "",
            "## Harmonic Rebirth Coda",
            "",
            "Book 6 was compressed by retaining these sections and omitting repeated",
            "waiting/silence/becoming passages between them:",
            "",
        ]
    )
    for heading in retained_coda:
        notes.append(f"- {heading}")
    notes.extend(
        [
            "",
            "## Next Editorial Pass",
            "",
            "- Expand character-level connective tissue across Parts I-V.",
            "- Make Lyra's signal visible before Part V.",
            "- Convert remaining episodic chapter endings into novel-driving turns.",
            "- Trim repeated sacred cadence in the coda after line editing.",
        ]
    )
    (TARGET / "RevisionNotes.md").write_text("\n".join(notes) + "\n", encoding="utf-8")
    return word_counts


def main() -> int:
    word_counts = build()
    total = sum(word_counts.values())
    for title, words in word_counts.items():
        print(f"{title}: {words:,} words")
    print(f"Total body words: {total:,}")
    print(f"Wrote {TARGET.relative_to(ROOT)}/Manuscript.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
