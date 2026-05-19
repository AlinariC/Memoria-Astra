#!/usr/bin/env python3
"""Build Book 16, The Second Spiral, from Books 07-15.

The source books remain standalone titles. This script creates a single-novel
manuscript with one front matter block, nine major parts, and short bridges
that carry the reader from the end of The First Spiral through the whole second
arc without retail-book seams.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import textwrap


REPO_ROOT = Path(__file__).resolve().parents[1]
TARGET = REPO_ROOT / "16_The_Second_Spiral"


FRONTMATTER = """\
---
title: "The Second Spiral"
subtitle: "A Memoria Astra Novel"
author: "Alinari Campbell"
language: "en"
rights: "(c) 2026 Alinari Campbell. All rights reserved."
identifier: "urn:uuid:memoria-astra-16-the-second-spiral-draft"
publisher: "PixelPacific"
cover-image: cover.jpg
series: "Memoria Astra"
genre: "Science Fiction"
description: |
  After the First Spiral gives way to a universe of breath, memory, flame, and song, two civilizations rise from the same sacred cradle and mistake distance for destiny. The Ashforged carry survival in engines and thrones; the Resonants carry consent in roots and gates. When an old hunger learns to wear mercy's face, flame and song must cross the Silent Rivers, survive the Shattered Gate, and choose whether the Second Spiral will become another empire of grief or a living cosmos brave enough to begin again.
keywords:
  - cosmic science fantasy
  - epic space opera
  - metaphysical science fiction
  - science fantasy saga
  - memory and rebirth
  - cosmic civilization
  - universe creation fiction
---
"""


OPENING = """
# Prologue - The Song Still Silent

At the end of the First Spiral, the universe did not close like a book.

It breathed.

The Shaper loosened its hold on the garden it had tended through silence, patience, and sacred becoming. The Wells dreamed beneath newborn fields. The Loom held its tension without command. Seeds that had slept in breath and memory trembled near awakening, and the Traveler, who had watched endings become beginnings before, folded itself into stillness so deep that even witness became a kind of reverence.

Life rose from that stillness in two far-flung children.

One child woke where breath grew thin and stars pressed hard against the fragile will to survive. There, ashfields taught hunger its first grammar. Hands blackened by ruin found old Wells, broken machines, and the stubborn ember of endurance. These would become the Ashforged, children of flame, steel, memory, and hard-won covenant.

The other child woke nearer the Loom's breathing skin, where roots heard currents before maps could name them and song learned that a road without consent was only conquest wearing light. These would become the Resonants, children of root, tide, gate, and refusal.

For a long age, they did not know one another.

They grew beneath the same Spiral and called themselves alone. They turned grief into craft, survival into law, wonder into custom, caution into doctrine. The Traveler watched. The Wells remembered. In the deep places between stars, where the Silent Rivers bent around wounds older than light, something uncarried listened.

The First Spiral had warned what would come: awe, terror, sorrow vast enough to make even the Spiral weep.

The warning was true.

But warnings are not endings.

They are doors waiting for those brave enough to open them slowly.
"""


@dataclass(frozen=True)
class Part:
    folder: str
    title: str
    bridge: str


PARTS = [
    Part(
        folder="07_Foundations_of_Flame",
        title="Part I - Foundations of Flame",
        bridge="""\
        The first child of the Second Spiral woke coughing ash.

        Before it could name beauty, it had to bargain with extinction. Before it could ask what the Wells remembered, it had to learn whether breath could be bound to a broken world without becoming another chain. In the far reaches, under skies scraped raw by ruin, survival became a forge.
        """,
    ),
    Part(
        folder="08_Inheritance_of_Song",
        title="Part II - Inheritance of Song",
        bridge="""\
        While flame learned to carry memory through engines and thrones, another inheritance unfolded in the fertile heartlands of the Spiral.

        Here the danger was gentler at first glance, and therefore no less perilous. Roots heard distance. Children listened to roads before elders had finished naming them. Song became passage, and passage learned that an open door without consent could become a wound.
        """,
    ),
    Part(
        folder="09_The_Silent_Accord",
        title="Part III - The Silent Accord",
        bridge="""\
        Flame and song found each other first by not crossing.

        Across the Silent Rivers, the Ashforged and the Resonants sensed the shape of another civilization through echoes, absences, and restraint. Their first language was not speech. It was the discipline of leaving room where fear wanted certainty, and that interval drew the hunger close.
        """,
    ),
    Part(
        folder="10_Starforged_Thrones",
        title="Part IV - Starforged Thrones",
        bridge="""\
        Peace without shape could not remain untouched by power.

        The Ashforged built thrones to keep memory from scattering. The Resonants deepened their houses of refusal to keep roads from becoming conquest. Between them moved rumor, grief, ambition, and the listening dark, each searching for the place where caution might harden into command.
        """,
    ),
    Part(
        folder="11_Lament_of_the_Shattered_Gate",
        title="Part V - Lament of the Shattered Gate",
        bridge="""\
        First contact arrived with the worst possible mercy.

        A cry crossed the distance between flame and song. Engines answered. Gates answered. Hearts answered faster than wisdom could move. In that beautiful, fatal haste, the old hunger found the seam it had been practicing against since before either people knew its name.
        """,
    ),
    Part(
        folder="12_Resonance_of_Ash_and_Dream",
        title="Part VI - Resonance of Ash and Dream",
        bridge="""\
        After the Shattered Gate, no victory could be claimed.

        The survivors had only names, wounds, and the terrible discovery that both peoples had erred from the same ache: the desire to answer suffering before asking whether the answer had permission to enter. In dream, ash and root began the slower work.
        """,
    ),
    Part(
        folder="13_The_Gathering_Spiral",
        title="Part VII - The Gathering Spiral",
        bridge="""\
        A sanctuary could teach grief to share a room, but the Spiral itself remained wounded.

        Refugees, engineers, keepers, rebels, and reluctant witnesses began to gather where maps changed under honest hands. No single banner could hold them. That was the point. The road to the Loomheart would have to be made from those who could leave as well as those who chose to come.
        """,
    ),
    Part(
        folder="14_The_Weeping_Crown",
        title="Part VIII - The Weeping Crown",
        bridge="""\
        The old temptation returned wearing the face of mercy.

        If grief was dangerous, why not govern it? If roads could wound, why not close them all from a single height? The Crown offered peace by containment, safety by command, and the end of sorrow through obedience. It almost sounded kind.
        """,
    ),
    Part(
        folder="15_The_Final_Loom",
        title="Part IX - The Final Loom",
        bridge="""\
        Beyond the Crown waited the choice no throne could make and no gate could force.

        The Spiral did not need a ruler strong enough to carry every grief. It needed a grammar in which grief could remain witnessed without becoming fuel, in which every road remembered how to close, and in which even the hunger left uncarried from the First Spiral might learn the first edge of breath.
        """,
    ),
]


ENDING_NOTE = """
# Closing Note - The Spiral Begins Again

The Second Spiral did not end because every wound closed.

It endured because the living learned that closure without consent was only another hunger, and that memory, to remain holy, must never be turned into a throne.

Flame remembered root. Root remembered flame. Dream remembered ash. Ash remembered song.

And somewhere beyond the last charted road, the Traveler stepped forward into a future that waited instead of commanded.
"""


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    match = re.match(r"^---\n.*?\n---\n", text, flags=re.DOTALL)
    if not match:
        return text
    return text[match.end() :]


def demote_headings(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("#"):
            hashes = len(line) - len(line.lstrip("#"))
            if hashes < 6 and line[hashes : hashes + 1] == " ":
                line = "#" + line
        lines.append(line)
    return "\n".join(lines).strip()


def dedent(text: str) -> str:
    return textwrap.dedent(text).strip()


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", strip_frontmatter(text)))


def build() -> None:
    TARGET.mkdir(exist_ok=True)
    sections: list[str] = [FRONTMATTER.strip(), dedent(OPENING)]
    notes = [
        "# The Second Spiral Build Notes",
        "",
        "Generated by `scripts/build_second_spiral.py` from Books 07-15.",
        "",
        "## Source Movements",
        "",
    ]

    total_source_words = 0
    for part in PARTS:
        source_path = REPO_ROOT / part.folder / "Manuscript.md"
        source = source_path.read_text(encoding="utf-8")
        body = demote_headings(strip_frontmatter(source))
        source_words = word_count(source)
        total_source_words += source_words
        notes.append(f"- {part.title}: `{part.folder}/Manuscript.md` ({source_words:,} words)")
        sections.extend(
            [
                f"# {part.title}",
                dedent(part.bridge),
                body,
            ]
        )

    sections.append(dedent(ENDING_NOTE))
    manuscript = "\n\n".join(section.strip() for section in sections if section.strip()) + "\n"
    (TARGET / "Manuscript.md").write_text(manuscript, encoding="utf-8")
    (TARGET / "metadata.yaml").write_text(FRONTMATTER, encoding="utf-8")

    combined_words = word_count(manuscript)
    notes.extend(
        [
            "",
            "## Word Counts",
            "",
            f"- Source words, Books 07-15: {total_source_words:,}",
            f"- Combined manuscript words: {combined_words:,}",
            "",
            "## Editorial Shape",
            "",
            "- One front matter block for the combined novel.",
            "- Book-level headings are demoted beneath nine novel parts.",
            "- New opening and part bridges carry the handoff from the end of The First Spiral.",
            "- The source books remain intact as standalone files.",
        ]
    )
    (TARGET / "RevisionNotes.md").write_text("\n".join(notes) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build()
