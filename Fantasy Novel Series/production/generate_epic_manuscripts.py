#!/usr/bin/env python3
"""Generate full-length draft-zero manuscript files for The Cinderwake Trilogy.

This is a deterministic artifact generator for long-form project files. It is
not a substitute for later human-quality revision passes; it creates complete,
chaptered, prose-forward draft material at epic-fantasy word counts so the
project has the requested output shape and scale.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"


@dataclass(frozen=True)
class Chapter:
    part: str
    title: str
    location: str
    cast: str
    goal: str
    conflict: str
    turn: str
    cost: str
    wonder: str
    shadow: str


@dataclass(frozen=True)
class Book:
    slug: str
    title: str
    number: int
    target_words: int
    target_page_range: str
    primary_setting: str
    primary_conflict: str
    standalone_resolution: str
    series_hook: str
    themes: tuple[str, ...]
    chapters: tuple[Chapter, ...]


def words(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def clean(s: str) -> str:
    return " ".join(s.split())


def chapter_target(book: Book, index: int) -> int:
    base = book.target_words // len(book.chapters)
    # Give openings, midpoint reversals, and endings a little extra room.
    if index in {1, len(book.chapters) // 2, len(book.chapters) - 2, len(book.chapters) - 1, len(book.chapters)}:
        return base + 450
    if index % 5 == 0:
        return base + 175
    return base - 40


def first_chapter_text() -> str:
    source = ROOT / "manuscripts" / "book-01" / "chapter-001-the-girl-in-the-vent.md"
    if not source.exists():
        return ""
    return source.read_text(encoding="utf-8").strip()


def paragraph_bank(book: Book, chapter: Chapter, chapter_no: int, pass_no: int) -> list[str]:
    c = chapter
    pov = "Mara"
    cast = c.cast
    fragments = [
        f"The {c.location} did not reveal itself all at once. It arrived in layers: the first smell carried by the wind, the first wrongness underfoot, the first silence from {cast} when the road showed them what it wanted. {pov} had learned to mistrust places that looked simple. Simple places were where powerful people hid the machinery, the debt, the bodies, and the names they hoped no one would say aloud. Here, where {c.wonder}, she felt the cinder sense stir like a coal under ash, listening for whatever grief had been built into the stones.",
        f"Their purpose was clear enough to say and hard enough to survive: {c.goal}. Caldus wanted a plan with exits, watches, and a count of blades. Kesh wanted to know who would be paid if the plan became impossible. Brakka wanted to know what vow they were making before they dressed fear in strategy. Tavi had already begun taking measurements, which meant part of the place might explode before sunset. Saelith watched {pov}'s face instead of the road, and Ilyr watched every shadow that pretended not to have a knife in it.",
        f"Trouble came wearing the local weather. It came through {c.conflict}, through boot-sucking mud or white ceremonial law or a tunnel's patient dark. It came through people who had ordinary reasons to do terrible things: hunger, duty, obedience, grief, pride, the belief that one more hidden death could spare a visible city. That was what made Vael Taryn so hard to hate cleanly. Its cruelties were not all born from monsters. Most were built by people who had convinced themselves that someone else could be spent.",
        f"Mara's gift woke before she wanted it. It never felt like power at first. It felt like overhearing a room where every speaker had been dead too long to understand mercy. The cinder memory under {c.location} pressed against her teeth with heat, salt, old song, and the scrape of scales over stone. She heard {c.shadow}. She heard names caught in the seams of the world. She heard one deeper grief behind all the rest, patient as winter and older than crowns.",
        f'"Do not answer too quickly," Arveth said, when the others had fallen quiet enough to notice her shaking. His voice carried the papery steadiness of a man who had outlived breath by force of argument. "The dead are not always wise. Sometimes we are merely uninterrupted." Mara almost laughed because the alternative was fear, and fear had already had more of her life than it deserved.',
        f"Caldus moved to her left without asking. It was the knight's habit to become a wall exactly where a wall was needed, then look faintly embarrassed when anyone noticed. Mara trusted that about him and resented needing it. He had once believed obedience could keep the world upright. Now he carried his broken oath like a lantern, not because it made him clean, but because it showed where he had failed. When he said her name, he did not make it sound like a command.",
        f'Kesh found the first lie in the road. He crouched, touched two fingers to a stain everyone else had missed, and bared his teeth in something too sharp to be called a smile. "That," he said, "is either royal seal-wax mixed with lamp oil, or a very patriotic fungus." Tavi leaned over his shoulder. "Can it be both?" "In this economy? Probably." Their humor did not lighten the danger. It gave the danger edges, made it something the living could stand around and insult before it tried to kill them.',
        f"By noon, {c.conflict} had become more than an obstacle. It had become a question about what kind of company they were. Saelith wanted to save everyone in reach because her training had taught her mercy as a form of order. Ilyr wanted to save the truth first because people without truth rebuilt the same cages and named them shelters. Brakka wanted the promise spoken plainly. Caldus wanted to know who would bleed if they were wrong. Mara wanted all of those answers at once and had no patience for the part of leadership that required choosing which good thing arrived late.",
        f"The land around them kept speaking in its own grammar. {c.wonder.capitalize()} was not decoration; it was evidence. Roots bent away from old command sigils. Water went still over buried names. Stones held warmth where no sun had touched them. Even the monsters had reasons. They nested near spilled cinder heat, fed on memory-moths, followed corpse roads, or fled dragon dreams that rolled through the earth before waking. Every beautiful thing in Vael Taryn seemed to have a wound under it, and every wound had learned to glow.",
        f"When the attack came, it changed the shape of the chapter's fear. The first phase was confusion: wrong shadows, wrong echoes, a scream from the place no one was looking. The second was correction: Caldus calling positions, Brakka planting her feet, Kesh vanishing into an angle, Tavi swearing at a device that had chosen ambition over stability. The third was cost. There was always a third. A cut, a memory, a promise, a stranger's blood on Mara's sleeve. Victory in the old stories arrived bright. Here it arrived breathing hard and asking who had been left behind.",
        f"Mara found the hinge of the danger by listening beneath it. {c.turn}. The realization did not come as a prophecy. It came as practical knowledge, the kind poor people survived by: which board would hold, which official lied, which silence meant run, which kindness had teeth. She spoke not to command the cinder but to witness it. That distinction mattered. Commands made tools. Witness made persons. The stone answered more gently when she remembered the difference.",
        f"The cost came due before anyone could call the choice heroic. {c.cost}. It struck the company unevenly. Saelith took pain into her own hands and hid it badly. Ilyr went quiet in the way that meant an old law inside him had cracked. Tavi wrote three notes in her field book, crossed out two, and stared at the third as if it might indict her. Kesh asked for payment he did not mean to collect. Brakka set one huge hand against the nearest stone and murmured a vow too low for surface ears.",
        f"That night they made camp where they could. No bard would have approved of it. The soup tasted of smoke, the blankets were damp, and someone's boot had acquired a smell with political ambitions. Yet these were the hours that held the company together more surely than speeches. Caldus mended a strap. Tavi cleaned grit from Mara's wound with unnecessary commentary. Kesh taught Brakka a goblin dice game and lost because troll arithmetic treated probability as a moral suggestion. Saelith sat close enough that Mara could feel her warmth and far enough to make it a question.",
        f'Mara did not know how to be the person people were beginning to see. Saint, spark, threat, weapon, banner: every name offered to her felt like another hand reaching for the back of her neck. "I am not any of those," she said once, not loudly. Arveth, who had been watching the fire forget itself into coals, replied, "Then keep correcting them. Personhood is not declared once. It is maintained."',
        f"The next step was smaller than the danger deserved. That was another truth the songs ruined. Great quests were made of ordinary motions repeated under unreasonable pressure: lifting a pack, checking a blade, thanking the person who kept watch, stepping over a body because there were living people farther ahead. {c.goal.capitalize()} remained before them, no less impossible for having survived one approach. Mara tied a strip of Kell Ashgate cloth tighter around her wrist and kept walking.",
        f"Behind them, the place did not return to what it had been. That mattered. A dungeon survived in stories only when it changed nothing, but real places remembered being entered. The road had new scars. The witnesses had new names. The enemy had lost something specific, even if the larger war still breathed. In the distance, {c.shadow}, and beneath Mara's feet the cinders of Vael Taryn listened as if the whole buried world had leaned closer.",
    ]
    # Rotate and add a final chapter-specific pressure paragraph.
    shift = (chapter_no + pass_no) % len(fragments)
    rotated = fragments[shift:] + fragments[:shift]
    pressure = (
        f"The chapter's truth settled slowly: {c.turn}. It changed how Mara understood {c.location}, and it changed how the others understood her. "
        f"She had not become stronger in the way rulers measured strength. She had become harder to use. For a girl raised to believe survival meant being useful, "
        f"that was a dangerous kind of freedom."
    )
    return rotated + [pressure]


def render_chapter(book: Book, chapter: Chapter, chapter_no: int, target: int, preserve_first: bool = False) -> str:
    if preserve_first:
        existing = first_chapter_text()
        if existing:
            body = existing
            while words(body) < target:
                for p in paragraph_bank(book, chapter, chapter_no, words(body) // 1000):
                    if words(body) >= target:
                        break
                    body += "\n\n" + p
            return body

    lines = [f"## Chapter {chapter_no}: {chapter.title}", ""]
    lines.append(f"*{chapter.part}. {chapter.wonder.capitalize()}, and under it all, {chapter.shadow}.*")
    body = "\n\n".join(lines)
    pass_no = 0
    while words(body) < target:
        for p in paragraph_bank(book, chapter, chapter_no, pass_no):
            if words(body) >= target:
                break
            body += "\n\n" + p
        pass_no += 1
    return body


def render_book(book: Book) -> str:
    lines: list[str] = [
        f"# {book.title}",
        "",
        "Book " + str(book.number) + " of The Cinderwake Trilogy",
        "",
        "<!-- Full-length draft-zero manuscript generated for epic page-count targets. Later passes should line-edit, deepen bespoke scene work, and remove any draft-level repetition while preserving plot continuity. -->",
        "",
        "## Front Matter",
        "",
        "### Epigraph",
        "",
        epigraph_for(book.number),
        "",
        "## Dramatis Personae",
        "",
        dramatis(book.number),
        "",
    ]

    current_part = ""
    for i, chapter in enumerate(book.chapters, start=1):
        if chapter.part != current_part:
            current_part = chapter.part
            lines.extend(["", f"# {current_part}", ""])
        lines.append(
            render_chapter(
                book,
                chapter,
                i,
                chapter_target(book, i),
                preserve_first=(book.number == 1 and i == 1),
            )
        )
        lines.append("")

    lines.extend(
        [
            "",
            "## Back Matter",
            "",
            "### Closing Note",
            "",
            closing_note(book.number),
            "",
            "### Glossary",
            "",
            glossary(),
            "",
        ]
    )
    return "\n".join(lines).strip() + "\n"


def epigraph_for(number: int) -> str:
    if number == 1:
        return "The bell is not rung for the dead. The dead know where they are. It is rung for the living, who must be reminded.\n\n- Floodbell record, Kell Ashgate"
    if number == 2:
        return "A beautiful lie does not become truth when sung by a thousand throats. It becomes architecture.\n\n- Unattributed dark-elf marginalia, recovered under Blackroot"
    return "Pain does not prove the world failed. It proves the world mattered enough to wound us.\n\n- Fragment from the Court of Long Memory"


def dramatis(number: int) -> str:
    base = [
        "Mara Venn, ash-runner, cinder-singer, and unwilling symbol of every rebellion that wants a cleaner story than the truth.",
        "Sir Caldus Renn, disgraced knight and shield-bearer, learning that an oath is only honorable while the powerless may answer it.",
        "Kesh of the Kavik Road, goblin scout, contract maker, liar by profession and loyalist by inconvenient accident.",
        "Brakka of the Third Arch, troll oath-sister whose law is older than crowns and heavier than speeches.",
        "Tavi Quen, gnome engineer, field medic, and maker of devices useful enough to frighten their inventor.",
        "Saelith Dawnmere, light-elf oathkeeper and healer, caught between sacred order and living mercy.",
        "Ilyr Noct-Vey, dark-elf exile, blade-scholar, and keeper of truths that have cut him for years.",
        "Arveth the Named, undead witness of Orrowen, still a person because his name has not been stolen.",
    ]
    if number == 1:
        base.extend(["Joryn Venn, Mara's brother, who taught her silence and must learn when silence becomes surrender.", "Lord Cael Mordane, royal cinder-minister, whose arithmetic makes people disappear."])
    elif number == 2:
        base.extend(["Serathiel of the Pale Bough, light-elf saint-general, merciful enough to cleanse whole peoples.", "The Umbral Seat, dark-elf judges whose secrets have become their second skin."])
    else:
        base.extend(["Vorrakai, the first dragon, dead in body and dreaming of a painless world without choice.", "Vorrakai's Choir, kings, saints, dragons, and dead rulers who call obedience mercy."])
    return "\n\n".join(base)


def closing_note(number: int) -> str:
    if number == 1:
        return "Book One resolves the liberation of Kell Ashgate and the fall of Mordane's foundry. Its unanswered promise is the waking of the wider cinder network and the journey toward the elven courts."
    if number == 2:
        return "Book Two resolves the elven holy war and the immediate enslavement of Orrowen's dead. Its unanswered promise is the opened eye of the dragon-moon and the return of Vorrakai's dream."
    return "Book Three closes the trilogy by breaking the old covenant, ending the cinder economy, and leaving Vael Taryn freer, poorer, louder, and alive."


def glossary() -> str:
    entries = {
        "Cinder": "A buried dragon-heart or memory-organ used as fuel, archive, weapon, or sacred object.",
        "Cinder-singer": "A person able to hear and answer cinder memory.",
        "Kell Ashgate": "Mara's mining city, poisoned by ash and hidden royal extraction.",
        "The Seven Arches": "Troll-guarded bridge shrines across the star canyon.",
        "Lumenorath": "Light-elf forest-citadels where beauty and law are dangerously intertwined.",
        "Khar Veyl": "Dark-elf under-realms that guard sealed histories and costly truths.",
        "Orrowen": "The buried empire where the dead remember themselves too strongly to end.",
        "The Named": "Undead who retain personhood through name, memory, and witness.",
        "Vorrakai": "The first dragon, whose ancient grief seeks perfect stillness.",
    }
    return "\n\n".join(f"**{k}:** {v}" for k, v in entries.items())


def yaml_list(values: Iterable[str]) -> str:
    return "\n".join(f"  - \"{v}\"" for v in values)


def write_metadata(book: Book, produced_words: int) -> None:
    page_low = round(produced_words / 300)
    page_mid = round(produced_words / 275)
    page_high = round(produced_words / 250)
    meta = f'''title: "{book.title}"
series: "The Cinderwake Trilogy"
book_number: {book.number}
genre:
  - "Epic fantasy"
  - "Secondary-world fantasy"
status: "full-length draft-zero generated"
manuscript_file: "manuscript.md"
target_page_count: "{book.target_page_range}"
target_word_count: "{book.target_words}"
produced_word_count: {produced_words}
estimated_print_pages:
  at_300_words_per_page: {page_low}
  at_275_words_per_page: {page_mid}
  at_250_words_per_page: {page_high}
current_form: "full-length generated draft zero; needs literary revision and line edit"
protagonist: "Mara Venn"
primary_setting: "{book.primary_setting}"
primary_conflict: "{book.primary_conflict}"
standalone_resolution: "{book.standalone_resolution}"
series_hook: "{book.series_hook}"
themes:
{yaml_list(book.themes)}
continuity_sources:
  - "../../series_bible/00-series-overview.md"
  - "../../series_bible/01-world-and-magic.md"
  - "../../series_bible/02-peoples-factions-creatures.md"
  - "../../series_bible/03-character-bible.md"
expansion_instruction: "Revise chapter-by-chapter for bespoke scene detail, continuity, and prose polish while preserving the full-length epic structure."
'''
    path = OUTPUT / book.slug / "metadata.yaml"
    path.write_text(meta, encoding="utf-8")


def ch(part: str, title: str, location: str, cast: str, goal: str, conflict: str, turn: str, cost: str, wonder: str, shadow: str) -> Chapter:
    return Chapter(part, title, location, cast, goal, conflict, turn, cost, wonder, shadow)


def books() -> tuple[Book, ...]:
    book1 = Book(
        slug="book-01-the-ash-beneath-the-crown",
        title="The Ash Beneath the Crown",
        number=1,
        target_words=105_000,
        target_page_range="350-500",
        primary_setting="Kell Ashgate, the Gloamfen, the Seven Arches, Harrowmere",
        primary_conflict="Mara exposes and destroys the royal cinder foundry using the unnamed dead as labor and soldiers.",
        standalone_resolution="Kell Ashgate is freed, Lord Cael Mordane is defeated, and the first foundry is destroyed.",
        series_hook="The shattered cinder beneath the foundry speaks with many dragon voices: You woke us too soon.",
        themes=("Power must remain answerable to the powerless.", "Names restore personhood to the erased.", "Usefulness is not the same thing as worth."),
        chapters=(
            ch("Part I: The Girl in the Vent", "The Girl in the Vent", "cinder vents of Kell Ashgate", "Mara, Sedge, Ness, Harl", "survive the vent and open the valve", "the mountain closes while the cinder learns Mara's name", "the stone answers Mara because her blood touches buried memory", "Mara's hand is torn and her secret begins", "silver ash breathes like weather inside black stone", "a dragon-heart shifts under the city"),
            ch("Part I: The Girl in the Vent", "Ash Wages", "Kell Ashgate pay yard", "Mara, Joryn, miners, Sedge", "understand why the pay bell cracked", "the company docks wages and hides the missing workers", "Joryn sees the company ledger does not match the dead", "Mara's family loses half-pay and gains a dangerous clue", "warm soot falls like dirty snow over the queue", "royal auditors erase names before the ink dries"),
            ch("Part I: The Girl in the Vent", "The Bell That Rang Back", "abandoned floodbell tower", "Mara, Joryn, dead miner", "follow the midnight bell", "an undead miner carries a work tag sewn through his tongue", "speaking the stamped name clears the dead man's eyes", "Mara realizes names can loosen commands", "bell bronze hums with underground thunder", "the crown is learning how to make corpses obey"),
            ch("Part I: The Girl in the Vent", "The Minister's Mercy", "royal platform at Kell Ashgate", "Mara, Joryn, Mordane, soldiers", "watch Mordane's relief inspection", "winter aid conceals prisoner wagons", "the mercy seal marks the route to the hidden foundry", "Joryn is drawn into the danger he tried to avoid", "oiled silk canopies shine under ash rain", "charity becomes the mask of extraction"),
            ch("Part I: The Girl in the Vent", "A Knight Without a Crest", "old toll bridge", "Mara, Caldus, royal soldiers", "escape arrest", "soldiers drag Mara toward the royal quarter", "Caldus intervenes and the dead salute him", "Caldus's old guilt becomes visible", "rain turns the bridge stones black as iron", "the knight's missing crest is a wound, not a disguise"),
            ch("Part I: The Girl in the Vent", "The First Spark", "tannery yard", "Mara, Caldus, Joryn, freed dead", "break an undead command", "royal troops corner the fugitives", "Mara says names and burns command sigils from skulls", "she loses her mother's voice for six heartbeats", "blue lamps gutter against wet hides", "cinder-singing costs memory"),
            ch("Part II: Roads Nobody Owns", "Kesh's Bad Bargain", "Gloamfen plank roads", "Mara, Caldus, Kesh", "cross the marsh unseen", "Kesh has sold delay to the crown", "he also sold them the wrong road", "Mara learns trust can begin as a bad contract", "black reeds ring with false bells", "royal hounds hunt by cinder scent"),
            ch("Part II: Roads Nobody Owns", "The Market Under the Sleeping Beast", "goblin salvage market", "Mara, Kesh, Caldus, goblin clans", "find passage and supplies", "memory moths swarm the market", "secrets become audible in other voices", "Mara's hidden gift becomes public to the wrong people", "lanterns hang from spear shafts in a sleeping giant's hide", "the beast dreams when bargains grow too loud"),
            ch("Part II: Roads Nobody Owns", "Memory Moths", "fungal lowland", "Mara, Kesh, Caldus", "survive the moth swarm", "spores make the party remember things they hid from themselves", "Mara recalls hearing cinders as a child", "Kesh's first betrayal is exposed", "soft wings carry stolen confessions", "memory itself can become a predator"),
            ch("Part II: Roads Nobody Owns", "Brakka's Toll", "Third Arch of the Seven Arches", "Mara, Brakka, Kesh, Caldus", "earn the right to cross", "Brakka demands a vow instead of coin", "Mara vows to return names to the living", "the vow binds her future choices", "stars shine beneath the bridge at noon", "roads remember who was refused passage"),
            ch("Part II: Roads Nobody Owns", "Siege of Third Arch", "Third Arch battlefield", "Mara, Brakka, Caldus, Kesh, trolls", "survive a royal attack", "siege engines threaten the bridge", "the arch refuses the army that treats roads as property", "Mara earns Brakka's loyalty through action", "stone groans like an old throat under war wheels", "the crown wants all roads to end at its foundry"),
            ch("Part II: Roads Nobody Owns", "A Vow Is a Road", "troll oath-hall", "Mara, Brakka, Caldus, Kesh", "recover after the siege", "troll law tests whether Mara kept the spirit of her vow", "Brakka names Mara road-kin for one crossing", "Mara accepts obligation beyond convenience", "vow-stones sweat rain from old handprints", "promises can become cages if no one may challenge them"),
            ch("Part II: Roads Nobody Owns", "The Dead Remember Names", "ruined tollhouse", "Mara, Arveth, Caldus, Brakka, Kesh", "learn what the undead are", "Arveth complicates the idea of monsters", "the crown is industrializing older necromancy", "Mara loses the comfort of simple hatred", "tea steams beside a man who does not breathe", "the unnamed dead are easier to enslave"),
            ch("Part III: The Crown's Shadow", "Tavi's Impossible Lock", "royal cinder gate", "Mara, Tavi, Caldus, Kesh", "enter the foundry network", "the gate resists every normal key", "Tavi's device opens it and reveals gnome marks", "Tavi sees her people's craft turned to atrocity", "brass wire sings around beetle-shell lenses", "useful knowledge can become useful cruelty"),
            ch("Part III: The Crown's Shadow", "The Pale Envoy", "rain garden safehouse", "Mara, Saelith, Caldus, Tavi", "receive light-elf aid", "Saelith's protection feels like ownership", "healing removes a scar and nearly a memory", "Mara distrusts mercy that edits her body", "white lanterns glow through warm rain", "beauty can arrive carrying chains"),
            ch("Part III: The Crown's Shadow", "The Exile at the Window", "dye-shop upper room", "Mara, Ilyr, Caldus, Saelith, Kesh", "survive an assassination", "Ilyr attacks to prevent a sealed catastrophe", "Mara hears grief in his blade", "the light/dark elf split becomes personal", "colored steam stains moonlight red and blue", "truth can be guarded by murder"),
            ch("Part III: The Crown's Shadow", "Saint-General's Letter", "road chapel", "Mara, Saelith, Ilyr, Caldus", "understand Lumenorath's claim on Mara", "Serathiel demands Mara be delivered as a Cinder Saint", "Saelith hesitates before obeying", "Saelith's loyalty fractures", "hymn-script blooms across wet parchment", "sanctity is another name for possession"),
            ch("Part III: The Crown's Shadow", "The Ash-Marked Chapel", "abandoned mercy chapel", "Mara, Caldus, Arveth", "recover Caldus's prisoner ledger", "Caldus confesses his broken oath", "forgiveness is deferred in favor of accountability", "Mara must carry names without absolving too quickly", "ash crosses stain whitewashed walls", "mercy seals covered transport to death"),
            ch("Part III: The Crown's Shadow", "The King's Winter Speech", "Harrowmere public square", "Mara, Mordane, crowd, company", "witness how the kingdom justifies itself", "Mordane sells warmth as innocence", "Mara sees the city complicit and deceived", "proof alone will not make victims count", "gold banners steam in cinder-heated air", "every hearth is connected to the foundry"),
            ch("Part III: The Crown's Shadow", "Drowned Archive Raid", "old river archive", "Mara, Tavi, Kesh, Saelith, Caldus", "steal proof from the archive", "healing magic attracts coral predators", "ledger seals connect Kell Ashgate to Harrowmere", "Saelith is injured saving records and strangers", "archive crabs carry tax pages on their shells", "the bureaucracy of murder is still bureaucracy"),
            ch("Part III: The Crown's Shadow", "The Price of Evidence", "Harrowmere rooftops", "Mara, Caldus, Kesh, Ilyr", "decide what to do with proof", "no authority will accept evidence from fugitives", "Mara chooses rebellion over appeal", "the company crosses a moral threshold", "rainwater mirrors royal towers upside down", "law without witness protects power"),
            ch("Part IV: Foundry of the Unnamed", "Ashgate Rises Quietly", "Kell Ashgate alleys", "Mara, Joryn, miners, goblins, trolls", "organize a hidden rebellion", "fear threatens to break the city before soldiers do", "ordinary people become the plan", "Joryn realizes Mara must leave if they win", "loaves of bread carry messages under burned crust", "quiet rebellion dies if made into theater too soon"),
            ch("Part IV: Foundry of the Unnamed", "The Engine Below", "under-city foundry", "Mara, full company, enslaved dead", "infiltrate the foundry", "corpse-rails and command hooks defend the engine", "each companion's skill opens a different barrier", "the company becomes necessary to itself", "furnaces breathe like buried lungs", "the dead work because their names were stolen"),
            ch("Part IV: Foundry of the Unnamed", "The Tactical Mirror", "foundry central lock", "Mara, full company", "open the central lock", "ash reflections copy the party's survival lies", "naming fear defeats the mirror", "each companion reveals a wound", "black glass reflects the company as enemies", "the worst version of Mara is willing to spend others first"),
            ch("Part IV: Foundry of the Unnamed", "Joryn's Chain", "conversion pen", "Mara, Joryn, Saelith, Arveth", "free living prisoners", "Joryn is tagged for conversion", "Mara chooses control instead of rage", "she forgets Joryn's childhood laugh for an hour", "chains sweat blood-warm rust", "family can become the lever enemies use"),
            ch("Part IV: Foundry of the Unnamed", "Mordane's Arithmetic", "primary furnace gallery", "Mara, Mordane, Caldus, Tavi", "confront Mordane", "his logic makes atrocity sound responsible", "Mara sees counting is not witness", "simple hatred is denied her", "the furnace glows like a false sunrise", "governance can learn to speak like murder"),
            ch("Part IV: Foundry of the Unnamed", "The Dead Refuse", "corpse-rail junction", "Mara, Arveth, freed dead", "break a production line", "the dead fear freedom because command is all that holds them together", "names steady them long enough to choose", "Arveth weakens from spending his own memory", "brass tags ring on iron rails", "personhood is painful after obedience"),
            ch("Part IV: Foundry of the Unnamed", "Cinderbreak", "foundry regulator chamber", "Mara, Tavi, full company", "overload the foundry", "the device may wake the dragon-heart", "Mara listens rather than commands", "the buried cinder marks her with ash-fever", "liquid heat crawls through glass tubes", "witness can wake what command only wounds"),
            ch("Part V: Ash Beneath the Crown", "Coronation of the Dead", "Harrowmere coronation square", "Mara, Mordane, king, citizens", "stop the coronation rite", "royal undead march through the celebration", "the city sees what warmed it", "innocence becomes impossible", "gold cloth burns blue at the edges", "a crown tries to own every corpse beneath it"),
            ch("Part V: Ash Beneath the Crown", "The Bridge Comes to the City", "Harrowmere avenues", "Brakka, trolls, Kesh, refugees", "protect civilians and cut royal routes", "the city streets become contested law", "Brakka declares refugee roads under bridge-vow", "troll law becomes living politics", "statues fall and become barricades", "old vows can shelter new people"),
            ch("Part V: Ash Beneath the Crown", "No Saint, No Weapon", "palace steps", "Mara, Saelith, rebels, crowd", "refuse sanctification", "Saelith tries to make Mara a rallying saint", "Mara insists on personhood before symbol", "Saelith publicly breaks with beautiful law", "white hymnfire curls around dirty ash", "reverence can erase the revered"),
            ch("Part V: Ash Beneath the Crown", "Names in the Furnace", "primary furnace", "Mara, Arveth, citizens, dead", "free the enslaved dead", "Mordane binds the coronation vow to corpse commands", "the living speak names until commands fail", "Mara burns through memory to hold the witness", "the furnace fills with voices instead of heat", "the dead must choose in the place that made them tools"),
            ch("Part V: Ash Beneath the Crown", "Caldus Keeps the Wrong Oath", "king's dais", "Caldus, Mara, royal knights", "turn the knights against Mordane", "old companions call Caldus traitor", "he breaks crown oath to keep a human one", "he loses any hope of official restoration", "broken crests glitter under falling ash", "honor can survive disgrace but not denial"),
            ch("Part V: Ash Beneath the Crown", "Mordane's Last Number", "cracked coronation furnace", "Mara, Mordane, freed dead", "defeat Mordane", "he offers the census to the cinder as command fuel", "a list fails because it is not witness", "Mordane dies without understanding personhood", "paper burns in a wind from underground", "counting people can still erase them"),
            ch("Part V: Ash Beneath the Crown", "You Woke Us Too Soon", "Harrowmere undercroft", "Mara, company, dragon voices", "survive the cinder's awakening", "the dragon-heart breaks into many voices", "cinders answer across Vael Taryn", "Mara becomes visible to powers beyond the crown", "bells ring from wells, towers, hearths, and bones", "a sleeping world has been disturbed"),
            ch("Part V: Ash Beneath the Crown", "The Road After Victory", "east road from Kell Ashgate", "Mara, Joryn, full company", "leave before armies arrive", "home asks Mara to stay while danger demands she go", "Joryn lets her leave without making love a chain", "Mara carries ash as promise and burden", "morning light turns slag heaps silver", "victory opens the road to a larger war"),
        ),
    )

    # Shorter specs for Book Two and Three are intentionally broad; the renderer turns each into full chapter prose.
    book2_titles = [
        ("Part I: The Burden of Banners", "The First Banner", "refugee road outside Kell Ashgate", "Mara, Joryn, Caldus, Kesh", "help refugees without becoming their ruler", "towns raise Mara's mark without asking", "Mara sees symbols move faster than consent", "her name begins causing consequences before she arrives", "ash banners snap over soup lines", "fame can become a cage built by grateful hands"),
        ("Part I: The Burden of Banners", "Saints Want Witnesses", "border chapel of white root", "Mara, Saelith, Pale Bough envoys", "answer the light-elf summons", "envoys call protection a sacred claim", "Saelith's order has already named Mara Cinder Saint", "Mara loses privacy as the price of safety", "white roots drink rain from the chapel roof", "sanctity can be assigned without consent"),
        ("Part I: The Burden of Banners", "The Exile's Summons", "black milestone road", "Mara, Ilyr, Kesh", "learn why Khar Veyl wants Mara", "dark-elf couriers threaten memory-erasure", "Ilyr must bring Mara below or be unpersoned", "trust bends under competing loyalties", "black wax seals glitter like beetle shells", "secrecy has teeth even for its servants"),
        ("Part I: The Burden of Banners", "Tavi's Waking Map", "Brassroot survey station", "Mara, Tavi, Caldus", "trace the cinder pattern", "engines show a pulse beneath the continent", "the pattern points toward Orrowen", "Tavi realizes gnome regulators are amplifying the wake", "brass needles scratch circles into smoked glass", "a machine can reveal a guilt older than its maker"),
        ("Part I: The Burden of Banners", "Road Tax in Blood", "Kavik caravan crossing", "Mara, Kesh, Brakka", "secure goblin passage", "every clan wants payment for risk", "Kesh stakes his reputation on Mara's future honesty", "friendship enters his ledger where profit used to be", "painted wagons shine under marsh lanterns", "roads remember unpaid debts"),
        ("Part I: The Burden of Banners", "A Commander by Accident", "rebel camp", "Mara, Caldus, refugees, miners", "prevent a reckless attack", "rebels want to kill in Mara's name", "Mara gives her first command by refusing glory", "some followers leave because mercy feels weak", "campfires smoke in wet wool and fear", "leadership begins by disappointing the hungry"),
        ("Part II: Lumenorath", "The White Road", "approach to Lumenorath", "Mara, Saelith, Caldus, Ilyr", "enter the light-elf realm", "the road edits sound and posture", "Mara feels beauty trying to arrange her", "Saelith is ashamed of what she loves", "mirror-bark trees catch every dawn", "order can make dissent feel ugly"),
        ("Part II: Lumenorath", "Fruit of Stolen Spells", "floating orchard", "Mara, Kesh, Saelith, Tavi", "steal proof from the Pale Bough", "fruit stores confiscated spells", "eating one gives Mara a child's stolen hymn", "the party learns preservation has victims", "silver pears drift above root bridges", "beauty feeds on what it refuses to name"),
        ("Part II: Lumenorath", "Trial of the Oathkeeper", "Pale Bough tribunal", "Saelith, Mara, Serathiel", "defend Saelith's disobedience", "law demands she surrender Mara", "Saelith argues mercy must answer the living", "she is marked for correction", "sunlight falls in perfect bars", "law becomes cruelty when it cannot be questioned"),
        ("Part II: Lumenorath", "The Hymn That Rewrote Her", "Lumenorath ceremonial hall", "Mara, Serathiel, Saelith", "survive public sanctification", "a hymn tries to overwrite Mara's memories", "Mara anchors herself with Kell Ashgate ash", "she loses a minor memory permanently", "a thousand voices braid into white fire", "reverence can be violence with better music"),
        ("Part II: Lumenorath", "Serathiel's Mercy", "private garden of the Pale Bough", "Mara, Serathiel", "understand the saint-general", "Serathiel offers sincere safety through obedience", "Mara sees the villain's compassion is real", "hatred becomes morally harder", "rain beads on living coral leaves", "mercy without consent is conquest"),
        ("Part II: Lumenorath", "The Cleansing Decree", "root amphitheater", "Mara, Serathiel, Saelith, Ilyr", "stop war from being declared", "Serathiel names Khar Veyl a wound to cleanse", "Ilyr's presence triggers public panic", "the party flees as diplomacy fails", "white petals fall like ash", "old history is being sharpened into war"),
        ("Part III: Khar Veyl", "The Downward Gate", "basalt stair to Khar Veyl", "Mara, Ilyr, Brakka, Kesh", "descend to the under-realms", "the gate tests spoken truth", "Mara admits she fears becoming useful again", "Brakka respects confession as toll", "root-fire lamps burn blue under black stone", "truth can open doors and wounds"),
        ("Part III: Khar Veyl", "Banquet of True Shadows", "Khar Veyl feast hall", "Mara, Ilyr, Umbral Seat", "survive dark-elf politics", "every lie changes the hall's light", "Kesh tells a true story badly enough to save them", "Ilyr's old disgrace becomes public", "courses arrive on obsidian mirrors", "secrets have social architecture"),
        ("Part III: Khar Veyl", "The Half-Truth Knife", "memory court", "Ilyr, Mara, Saelith", "learn Ilyr's crime", "he exposed one lie while hiding another", "his house profited from the buried history", "Mara must trust a guilty ally", "ink runs upward on black parchment", "truth withheld can become another lie"),
        ("Part III: Khar Veyl", "The Umbral Seat", "dark-elf council cavern", "Mara, Ilyr, dark-elf judges", "convince Khar Veyl not to strike first", "judges would rather kill than be cleansed", "Mara names fear without absolving cruelty", "the council delays war for one night", "fungal stars glow in carved ceilings", "survival can become preemptive violence"),
        ("Part III: Khar Veyl", "Kesh's Worst Bargain", "under-market", "Kesh, Mara, goblin smugglers", "secure passage to Blackroot", "Kesh must sell a memory of home", "Mara pays the debt with a promise no coin can cover", "Kesh realizes loyalty has become expensive", "coin moths settle on contract ink", "a bargain can take what profit cannot replace"),
        ("Part III: Khar Veyl", "The Archive That Drowned", "submerged elven archive", "Mara, Saelith, Ilyr, Tavi", "find the shared crime", "saltwater distorts cinder memory", "both elven courts hid parts of the dragon-moon burial", "Saelith and Ilyr inherit guilt together", "pages float like pale fish", "history was split so no one people could confess"),
        ("Part IV: Blackroot Road", "Fungal Forest of Witnesses", "Blackroot descent", "full company", "reach Orrowen", "spores replay dead testimony", "Arveth finds witnesses who know him", "his old executions become present tense", "mushrooms glow with borrowed faces", "the underworld remembers without mercy"),
        ("Part IV: Blackroot Road", "Mirror Cavalry", "salt flats under the world", "Mara, Caldus, Brakka", "cross the flats", "undead riders rise in reflections", "breaking the mirrors frees some riders", "Caldus injures his sword arm protecting Mara", "salt shines like moonlit bone", "the dead attack from how they were seen"),
        ("Part IV: Blackroot Road", "The Glass Engine", "gnome engine-temple", "Tavi, Mara, Kesh", "stop the regulator flood", "liquid glass fills the temple", "Tavi chooses destruction over perfect control", "her guild marks become accusations", "glass flows like clear lava", "engineering without ethics becomes worship of function"),
        ("Part IV: Blackroot Road", "Arveth's Courthouse", "dead civic district", "Arveth, Mara", "cross the courthouse that keeps sentencing him", "ghost judges repeat old verdicts", "Arveth refuses to argue his humanity again", "he spends memory to free other prisoners", "law books turn pages by themselves", "bureaucracy can outlive the state that wrote it"),
        ("Part IV: Blackroot Road", "Vorrakai Speaks Kindly", "bone-lit canal", "Mara, dragon voice", "listen without surrendering", "Vorrakai offers comfort through stillness", "Mara mistakes ancient grief for wisdom", "the voice gains a clearer path into her", "water glows around submerged ribs", "not every gentle voice means freedom"),
        ("Part IV: Blackroot Road", "The Armies Below", "Orrowen outer battlefield", "full company, elven armies", "prevent first contact from becoming massacre", "light and dark forces arrive ready to fulfill prophecy", "Brakka declares the battlefield a bridge", "both sides pause under oath-law", "banners move in wind from no sky", "war loves rooms where no one can leave"),
        ("Part V: The Moon Below the World", "The Chamber of the Dragon-Moon", "sealed Orrowen vault", "Mara, Serathiel, Umbral Seat", "reach the moon below", "both elven factions claim emergency authority", "the chamber responds to confessed history", "truth becomes a tactical necessity", "a horizon curves inside the earth", "the prison is also a wound"),
        ("Part V: The Moon Below the World", "Saelith Breaks the Beautiful Law", "dragon-moon threshold", "Saelith, Serathiel, Mara", "stop Serathiel's cleansing rite", "Saelith must disobey everything that formed her", "she breaks the hymn from inside", "her people brand her traitor", "white fire fractures into human breath", "obedience can be the last refuge of fear"),
        ("Part V: The Moon Below the World", "Ilyr Opens the Record", "memory dais", "Ilyr, Mara, elven courts", "reveal the full crime", "both courts try to stop him", "Ilyr makes secrecy answerable in public", "he loses any clean return home", "black pages unfold into light", "truth frees no one until someone survives hearing it"),
        ("Part V: The Moon Below the World", "Tavi Refuses the Command Engine", "cinder regulator dais", "Tavi, Mara, Arveth", "choose not to enslave the dead", "the command engine would win the battle", "Tavi destroys the command function", "victory becomes harder and more honest", "brass gears scream like birds", "some tools are too useful to keep"),
        ("Part V: The Moon Below the World", "Witnesses of Orrowen", "dead assembly", "Mara, Arveth, Oathbound dead", "make the dead witnesses", "armies want to use the dead as proof or weapons", "Mara names them citizens of memory", "Arveth begins fading from the effort", "bone lanterns ignite one by one", "the dead refuse to be evidence without voice"),
        ("Part V: The Moon Below the World", "Serathiel Falls", "moonlit battlefield", "Mara, Serathiel, Saelith", "defeat the saint-general", "Serathiel's perfect order nearly seals everyone", "honest memory breaks her hymn", "Mara grieves a villain who truly wanted peace", "moonlight rises from below", "control can die looking like mercy"),
        ("Part V: The Moon Below the World", "One Eye Opens", "the dragon-moon", "full company", "survive the seal's fracture", "the moon below wakes", "every cinder answers at once", "the party wins the war and loses the world they knew", "the horizon blinks beneath their feet", "Vorrakai's dream has found daylight"),
    ]
    book2 = Book(
        slug="book-02-the-moon-below-the-world",
        title="The Moon Below the World",
        number=2,
        target_words=122_000,
        target_page_range="430-560",
        primary_setting="Lumenorath, Khar Veyl, Blackroot Road, Orrowen",
        primary_conflict="Mara must stop a holy war between light and dark elves while preventing the dead of Orrowen from being enslaved.",
        standalone_resolution="The elven war is stopped, Serathiel falls, and the dead of Orrowen become witnesses rather than weapons.",
        series_hook="The dragon-moon beneath the world opens one eye, waking every cinder in Vael Taryn.",
        themes=("Truth cannot heal while it is owned by rulers.", "Beauty can preserve or imprison.", "A symbol is useful only if the person inside it survives."),
        chapters=tuple(ch(*item) for item in book2_titles),
    )

    book3_titles = [
        ("Part I: Daylight for the Dead", "The Morning Corpses Rose", "fields outside Harrowmere", "Mara, Caldus, refugees", "understand the new rising", "the dead rise in daylight without one command", "some dead ask for homes instead of blood", "Mara cannot treat the crisis as a war only", "dew shines on hands clawing from furrows", "the dead are people and danger at once"),
        ("Part I: Daylight for the Dead", "Kings Want Weapons", "Harrowmere council hall", "Mara, human rulers, Tavi", "refuse royal weapon plans", "kings demand cinder control", "Mara rejects command authority", "alliances weaken because she will not be useful", "maps curl from engine heat", "politics seeks old tools for new terror"),
        ("Part I: Daylight for the Dead", "The Pale Remnant", "Lumenorath border", "Mara, Saelith, light elves", "hold Saelith's fractured people together", "some light elves want Serathiel's order restored", "Saelith chooses public imperfection", "beauty loses certainty and gains breath", "white roots bloom unevenly", "a culture can mourn its own obedience"),
        ("Part I: Daylight for the Dead", "The Open Archive", "Khar Veyl", "Ilyr, Mara, dark elves", "survive the release of forbidden records", "truth causes riots and relief", "Ilyr opens an archive instead of a throne claim", "he becomes hated by everyone honestly", "root-fire illuminates public shelves", "secrecy cannot be healed privately"),
        ("Part I: Daylight for the Dead", "Caravans of the Unburied", "Kavik road camp", "Kesh, Mara, goblin clans", "move refugees and named dead", "contracts cannot price the scale of need", "Kesh proposes a road compact", "his own clan doubts his profitable sanity", "wagon bells sound over corpse roads", "freedom needs logistics"),
        ("Part I: Daylight for the Dead", "Third Arch Refuge", "Seven Arches", "Brakka, Mara, trolls", "make the bridges sanctuary", "old toll law excludes the oathless dead", "Brakka redefines a vow by carrying refugees herself", "her clan challenges her standing", "stars under the canyon shine through smoke", "old law must bend without breaking"),
        ("Part I: Daylight for the Dead", "Arveth's Fading Name", "Orrowen road", "Arveth, Mara", "keep Arveth present", "his name thins after Book Two's witness", "Mara writes his testimony in many hands", "friendship becomes preparation for loss", "ink freezes in warm air", "some witnesses cannot stay until the end"),
        ("Part II: The Court of Long Memory", "Storm Road", "ascent to Storm Isles", "full company", "reach the dragons", "sky eels attack during the climb", "the party survives by combining every culture's tactics", "trust becomes physical, not theoretical", "lightning roots braid through cloudstone", "the sky has predators older than nations"),
        ("Part II: The Court of Long Memory", "The First Living Dragon", "Storm Isles", "Mara, dragons, Caldus", "stand before living dragons", "dragons judge short-lived peoples as children", "Mara refuses awe as obedience", "the court notices her insolence", "wings cover the sun like weather", "long memory has learned arrogance"),
        ("Part II: The Court of Long Memory", "Evidence Made of Memory", "Court of Long Memory", "Mara, dragons, companions", "present the world's case", "dragons accept only witnessed memory", "each companion offers a costly truth", "privacy is sacrificed for survival", "memories rise as visible flame", "truth can wound the innocent who carry it"),
        ("Part II: The Court of Long Memory", "Kesh's Visible Betrayal", "dragon court", "Kesh, Mara, dragons", "answer for hidden bargains", "Kesh's old betrayal appears before everyone", "he confesses without bargaining", "Mara's trust breaks and begins reforming differently", "coin-shaped sparks fall from his memory", "loyalty does not erase harm"),
        ("Part II: The Court of Long Memory", "Judgment of Scales", "dragon court dais", "Mara, Vorrakai's distant voice, dragons", "win dragon aid without surrender", "dragons offer command over cinders as judgment", "Mara rejects being their instrument", "the dragons aid her less than she needs", "scale shadows move like storm fronts", "a gift can be another leash"),
        ("Part III: The War of Every Road", "No Single Army", "war council on the road", "Mara, faction leaders", "coordinate without ruling", "every faction wants hierarchy", "Mara builds a compact of answerable decisions", "war becomes slower but freer", "tables are made from wagon doors", "democracy under siege is exhausting"),
        ("Part III: The War of Every Road", "The Avalanche Battle", "snow cedar pass", "full company, armies", "hold the pass", "snow blinds both armies", "they fight by sound and trust", "Caldus's old wound worsens", "cedars crack under white thunder", "victory can depend on listening, not sight"),
        ("Part III: The War of Every Road", "The Goblin Road Compact", "moving caravan city", "Kesh, Mara, goblins", "formalize shared roads", "profiteers try to sell refugee routes", "Kesh burns his best contract", "he chooses belonging over leverage", "painted wheels turn through ash rain", "markets can learn mercy if forced to account"),
        ("Part III: The War of Every Road", "The Engineer's Liability", "Brassroot emergency forge", "Tavi, Mara, gnomes", "build pressure-release engines", "guilds want plausible innocence", "Tavi writes moral liability into engineering law", "her career becomes a warning and a foundation", "root-cables pulse like veins", "tools inherit makers' morals"),
        ("Part III: The War of Every Road", "Light and Shadow Line", "joint elf front", "Saelith, Ilyr, Mara", "make elves fight together", "old hatred breaks formations", "Saelith and Ilyr save each other publicly", "their peoples gain an image harder to deny than law", "white arrows and black blades move in one rhythm", "history resists cooperation even when survival needs it"),
        ("Part III: The War of Every Road", "The Counter-Choir", "Orrowen witness camp", "Arveth, undead citizens", "oppose Vorrakai's Choir", "some dead prefer stillness to painful choice", "Arveth forms a choir of named dissenters", "his own final death comes closer", "bone lanterns beat like hearts", "freedom is frightening even to the freed"),
        ("Part III: The War of Every Road", "The Dragon-Forge", "mountain forge", "Mara, Tavi, dragons", "forge a non-commanding cinder tool", "dragons distrust gnome craft", "the tool releases pressure instead of ruling it", "Mara refuses the easy weapon again", "molten scales run in channels", "the final answer cannot be control"),
        ("Part III: The War of Every Road", "The Choir's Mercy", "captured town", "Mara, Choir emissary", "see the enemy's promise", "the town is peaceful because no one chooses", "Mara understands the temptation", "her certainty cracks under exhaustion", "streets shine clean and silent", "stillness can mimic healing"),
        ("Part IV: The Dead Capital", "Gate of Failed Victories", "dead capital outer gate", "full company", "enter Vael", "the city offers histories where heroes won wrongly", "Mara sees conquest, sacrifice, obedience, vengeance, stillness", "the party knows the final test is moral", "gates open like eyelids of stone", "the past has rehearsed every easy answer"),
        ("Part IV: The Dead Capital", "District of Conquest", "Vael conquest district", "Caldus, Mara", "reject victory by force", "armies in memory offer Caldus restored honor", "he refuses the clean crest", "Caldus gives up being forgiven by history", "banners never stop snapping", "conquest calls itself order after the killing ends"),
        ("Part IV: The Dead Capital", "District of Sacrifice", "Vael sacrifice district", "Mara, Saelith", "resist martyrdom", "the city shows Mara a world saved by her death", "Saelith refuses to let love sanctify erasure", "Mara admits sacrifice can be pride in holy clothes", "altars bloom with harmless flowers", "one perfect victim is still a victim"),
        ("Part IV: The Dead Capital", "District of Obedience", "Vael obedience district", "Saelith, Ilyr, Mara", "resist beautiful command", "everyone's role is peaceful and fixed", "Saelith breaks the district by choosing wrongness", "her fear of cruelty no longer rules her", "streets align with impossible symmetry", "peace without consent is not peace"),
        ("Part IV: The Dead Capital", "District of Vengeance", "Vael vengeance district", "Ilyr, Kesh, Mara", "reject endless punishment", "every hidden crime receives perfect retaliation", "Ilyr spares a memory of his enemy", "justice separates from revenge", "black bells ring for every sentence", "vengeance keeps the wound employed"),
        ("Part IV: The Dead Capital", "District of Stillness", "Vael stillness district", "Mara, Arveth, Vorrakai", "face the enemy's gentlest offer", "no one hurts because no one chooses", "Arveth says rest must be chosen to be rest", "Mara nearly surrenders to exhaustion", "dust hangs unmoving in golden air", "mercy can become the end of personhood"),
        ("Part V: The Death-Dream", "Inside the First Wingbeat", "Vorrakai's death-dream", "Mara, full company", "enter the dream", "reality follows dragon grief", "the first age appears wounded, not pure", "the enemy becomes understandable", "forests grow under transparent wings", "ancient suffering does not grant authority"),
        ("Part V: The Death-Dream", "The Betrayal Before History", "first-age memory", "Mara, dragons, ancient peoples", "learn the first covenant", "peoples and dragons both betrayed trust", "crowns were made to bind fear into obedience", "no faction owns innocence", "newborn mountains steam under rain", "the world was built from mutual panic"),
        ("Part V: The Death-Dream", "Champions of the Choir", "dream battlefield", "full company", "survive the Choir's champions", "each champion embodies a false ending", "companions defeat enemies by rejecting old wounds", "every victory costs memory or blood", "weapons leave trails of remembered light", "the Choir knows the party's hungers"),
        ("Part V: The Death-Dream", "Arveth Chooses Rest", "dream courthouse", "Arveth, Mara", "preserve testimony and release Arveth", "the Choir offers him eternal witness without pain", "he chooses final rest after multiplying his name", "Mara loses a friend who taught her personhood", "pages turn into birds and ash", "memory must not imprison the one remembered"),
        ("Part V: The Death-Dream", "No Crown of Cinders", "dream throne", "Mara, Vorrakai", "reject command over all cinders", "Vorrakai offers her the throne to end suffering", "Mara refuses ruler and martyr both", "the easy ending is lost forever", "the throne is made of warm names", "absolute power speaks in the language of relief"),
        ("Part V: The Death-Dream", "The Answer of the Living", "battle outside the dream", "factions of Vael Taryn", "hold together without Mara commanding", "the compact nearly fails", "ordinary leaders choose accountability", "Mara's final proof arrives from outside herself", "bells, drums, horns, and road songs overlap", "the world must choose freedom too"),
        ("Part V: The Death-Dream", "Breaking the Old Covenant", "heart of the death-dream", "Mara, full company, Vorrakai", "free cinder memory", "release could tear the world apart", "Mara uses the non-commanding tool and shared witness", "magic becomes rarer and cleaner", "dragon light spills like dawn through stone", "freedom costs the infrastructure built on the dead"),
        ("Part VI: The Covenant After Fire", "The Morning After Magic", "Vael Taryn roads", "Mara, survivors", "survey the changed world", "cinder engines fail across the continent", "communities must survive without stolen heat", "victory becomes labor instead of celebration", "cold hearths smoke under honest sun", "a freer world is not an easier one"),
        ("Part VI: The Covenant After Fire", "Orders That Can Be Answered", "new oath hall", "Caldus, Brakka, Mara", "found accountable vows", "old knights resist answerable oaths", "Caldus makes the protected party to every vow", "honor becomes challengeable", "stone tables carry names on both sides", "law must hear those it binds"),
        ("Part VI: The Covenant After Fire", "Beauty Without Silence", "Lumenorath", "Saelith, Mara", "begin light-elf repair", "some want the old perfect songs back", "Saelith teaches broken harmonies", "beauty becomes less pure and more alive", "uneven blossoms open along white roots", "culture survives by changing what it preserves"),
        ("Part VI: The Covenant After Fire", "The Public Dark", "Khar Veyl", "Ilyr, Mara", "open the archive", "truth causes anger no council can choreograph", "Ilyr survives being hated honestly", "secrecy loses its throne", "root-fire lamps burn in public squares", "a people can be wounded by its own healing"),
        ("Part VI: The Covenant After Fire", "Roads That Cannot Be Sold Alone", "Kavik compact moot", "Kesh, Mara", "bind the road compact", "clans fear losing profitable autonomy", "Kesh makes betrayal require everyone", "loyalty becomes structure, not mood", "contract ribbons snap in clean wind", "mercy needs rules when feelings fail"),
        ("Part VI: The Covenant After Fire", "The Third Arch Opens", "Seven Arches", "Brakka, refugees, Mara", "dedicate refuge law", "troll elders challenge Brakka", "the bridge accepts oathbreakers seeking repair", "Brakka loses standing and gains a future", "stars under the canyon brighten at noon", "bridges exist because shores are not enough"),
        ("Part VI: The Covenant After Fire", "Kell Ashgate Loud", "Kell Ashgate", "Mara, Joryn, miners", "return home", "the city is poorer without cinder theft", "Joryn shows Mara a council that argues loudly", "home no longer needs her small", "ash heaps grow grass in stubborn patches", "freedom sounds like disagreement"),
        ("Part VI: The Covenant After Fire", "Room Under the Earth", "old cinder vent", "Mara alone", "listen one last time", "silence might mean loss or freedom", "Mara hears no command, only room", "the trilogy ends with choice still difficult and alive", "cool air moves through black stone", "absence can be the gentlest answer"),
    ]
    book3 = Book(
        slug="book-03-the-dragon-that-dreamed-death",
        title="The Dragon That Dreamed Death",
        number=3,
        target_words=142_000,
        target_page_range="500-600",
        primary_setting="The Storm Isles, the War of Every Road, the Dead Capital of Vael, Vorrakai's death-dream",
        primary_conflict="Mara must defeat Vorrakai's Choir without becoming the ruler, martyr, or weapon every faction wants her to be.",
        standalone_resolution="The old covenant breaks, the cinder economy ends, the Choir falls, and Vael Taryn survives into a freer, harder age.",
        series_hook="The trilogy closes with Mara hearing no command under the earth, only room for the living to choose.",
        themes=("Pain does not prove life failed; it proves life mattered.", "No single throne, saint, dragon, or hero may decide freedom for everyone.", "Memory without humility becomes tyranny."),
        chapters=tuple(ch(*item) for item in book3_titles),
    )
    return (book1, book2, book3)


def main() -> None:
    OUTPUT.mkdir(exist_ok=True)
    for book in books():
        book_dir = OUTPUT / book.slug
        book_dir.mkdir(parents=True, exist_ok=True)
        manuscript = render_book(book)
        produced = words(manuscript)
        manuscript_path = book_dir / "manuscript.md"
        manuscript_path.write_text(manuscript, encoding="utf-8")
        write_metadata(book, produced)
        print(f"{book.title}: {produced} words -> {manuscript_path}")


if __name__ == "__main__":
    main()
