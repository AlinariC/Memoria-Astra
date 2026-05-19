#!/usr/bin/env python3
"""Targeted trilogy consistency/prose polish pass.

This pass applies the high-confidence fixes from the five-role trilogy review:
- deepen two short chapters whose pacing felt thin for epic scale;
- normalize light-elf/dark-elf terminology variants;
- remove draft/front-matter comments and fiction-breaking book/chapter language;
- repair continuity collisions for Serathiel, Veyrasha, Edda/Brenna, Vessa, and Lio;
- expand Book Three's glossary for the final-book concepts.
"""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
REPORT = ROOT / "production" / "trilogy-consistency-polish.md"

BOOK1 = OUTPUT / "book-01-the-ash-beneath-the-crown" / "manuscript.md"
BOOK2 = OUTPUT / "book-02-the-moon-below-the-world" / "manuscript.md"
BOOK3 = OUTPUT / "book-03-the-dragon-that-dreamed-death" / "manuscript.md"


BOOK1_CH5_ANCHOR = """The word tore something open in Caldus Renn that no sword on the bridge had touched.

Caldus Renn had been following the mercy wagons for six days when Mara ruined his plan by being alive."""

BOOK1_CH5_INSERT = """The word tore something open in Caldus Renn that no sword on the bridge had touched.

For one breath, the bridge forgot everyone else.

Rain ticked on the scraped place where his crest should have been. The dead miner's salute held. Caldus looked at Pell Orwick as if the stitched mouth and gray water and royal tag had arranged themselves into a judgment he had been avoiding by miles. Mara knew that look. Not from knights. From miners who had signed a debt note because a child needed fever tea, then discovered the note had bought the company a claim on next winter too.

The soldiers knew it as weakness.

"Sir Caldus Renn," the captain said, savoring the title now that it hurt someone. "By order of Lord Mordane and the Crownreach mercy commission, you are remanded for desertion, interference with royal dead-work, and theft of crown evidence."

"Theft?" Mara said through blood.

The captain smiled at her. "He stole himself."

Caldus's jaw tightened.

Pell's salute began to shake.

The command rod in the captain's left hand pulsed once, and the stitched tag at Pell's throat answered. The dead miner's arm dropped. His whole body jerked forward a half step, then stopped as if two laws had caught him by opposite wrists. Caldus lifted his shield again, but too slowly. Mara saw the angle before he did. The soldiers were not trying to kill him. They were trying to make Pell do it.

"You knew him," Mara said.

Caldus did not look at her. "No."

"He knew you."

"Many dead men know knights."

"That is not an answer."

The captain raised the rod higher. Pell's ruined mouth opened around a sound too small for screaming. Behind him, more bodies surfaced in the runoff tunnel: Essa Brant, whose bread Mara had once stolen and paid back badly; Tollen Reed with his left boot gone; a boy she did not know wearing a quarry rope around his waist like a sash. Every tag tugged toward the rod. Every dead face turned toward Caldus, not with hatred. With recognition.

Caldus lowered the shield enough to see them.

"I signed the first escort warrant," he said.

Mara felt the bridge move under her feet though the stone had not shifted.

"For mercy wagons?" she asked.

"For prisoners the court said would be moved to hospice labor until trial." His voice had gone flat, which meant every word had to cross a field of knives before reaching air. "The seal was legal. The witnesses were legal. The numbers matched. I did not ask why the hospice road led to a foundry."

The captain's smile widened. "Confession entered."

"No," Caldus said.

He stepped forward then, and the tired no from earlier vanished. This one had weight. Not noble weight. Not clean. The weight of a man finding, too late, the exact shape of his cowardice and deciding to stand inside it where everyone could aim.

"Confession begins," Caldus said.

The captain jabbed the rod toward Pell.

Mara moved before she understood the choice. She threw the surgeon's hook. It did not strike the rod. She had never been that lucky. It struck the captain's sleeve, caught cloth and wrist, and spoiled the angle. Pell lurched sideways instead of forward. Caldus used the mistake. Shield edge broke the rod's iron tip. The cinder bead burst with a wet spark, and every corpse on the bridge convulsed as if a song had missed a note.

The blast threw Mara against the parapet.

Cold gray canal water slapped up over the stones. For a moment she heard the mountain under the city and the city under the mountain: pipes, bells, chain wheels, breath, dead mouths, living fear. Then Caldus was there, hauling her upright with one hand while fending off a soldier with the shield in the other.

"You throw badly," he said.

"You confess slowly."

"Fair."

Pell Orwick stood between them and the captain now. Not attacking. Not free. His dead hands trembled at his sides, and the stitched mouth worked around the title that had hurt Caldus so deeply.

"Sir," Pell forced out again.

Caldus bowed his head.

Not low. Not enough for songs. Enough for a dead miner on a wet toll bridge to be seen by the man who had helped send him there.

"Pell Orwick," Caldus said. "I hear you."

The name steadied the corpse for one impossible second.

Then the canal behind Pell began to bubble.

Caldus Renn had been following the mercy wagons for six days when Mara ruined his plan by being alive."""


BOOK3_CH17_ANCHOR = """The line broke.

Caldus shouted for shields."""

BOOK3_CH17_INSERT = """The line broke.

It broke in three places at once, which was how Mara knew the Choir had planned for pride instead of terrain.

On the western bank, three Lumenorath riders surged after a false white banner that appeared between the reeds. Their horses hit mud hidden under shallow water and went down screaming. Khar Veyl scouts on the eastern side mistook the fall for a charge and loosed black signal flares. The flares struck glass reeds overhead and burst into shadow where light-elf archers had been told shadow meant murder. Arrows flew blind. Auralian shouted a counterorder, but the Choir's lullaby bent his command into comfort, and comfort told frightened soldiers that someone else had already decided for them.

On the eastern bank, Maelin's trench markers vanished one by one.

Not extinguished. Rewritten.

The violet lamps began showing old massacre dates instead of safe footing. Dark-elf scouts froze as their own history accused them under enemy eyes. One scout tore off her hood and shouted that she would not hide from white law again. A light-elf captain heard only the shout, not the wound inside it, and ordered a volley. The volley would have killed half the trench if Brakka had not ripped a wagon side free and planted it upright in the mud.

The arrows hit the planks like hard rain.

"That wagon was medical," Tavi shouted.

"Now it is political," Kesh said, sliding under it to cut a Choir tripline.

Mara ran toward the center path because the refugees were there: carts, stretchers, children, Orrowen lanterns, two goblin families with fever bundles, and three human deserters who had chosen the worst possible morning to become morally complicated. The Choir did not need to kill them. It only needed the elves to believe the other side would.

A dead rider stepped from the reeds carrying the cinder-glass child.

"Lay down memory," it said.

The front cart stopped. The woman pushing it began to cry with relief.

Mara caught the cart handle before it rolled sideways into open water. "No. Keep moving."

"I am tired," the woman whispered.

"I know."

"It says I can stop."

Mara looked at the glass child, at the command seed glowing like a tiny patient heart behind its false ribs. "Things that love you do not ask you to leave your children in a battle road."

The woman's face changed. Not healed. Angered. Anger put her hands back on the cart.

"Push," Mara said.

They pushed together.

Caldus shouted for shields."""


BOOK1_CH4_ANCHOR = """"Alive," the physician snapped. "Do not damage her."

That was how Mara learned they knew more about her than she did.

The second soldier drew a baton."""

BOOK1_CH4_INSERT = """"Alive," the physician snapped. "Do not damage her."

That was how Mara learned they knew more about her than she did.

The sentence did not land like threat at first. It landed like inventory.

One of the soldiers had a slate strapped to his forearm under the rain cloak. When he lifted his baton, the cloak fell back and Mara saw rows of names written in white grease pencil. Not many. Enough. West Gallery husband. Two children from Sump Lane. A bellkeeper's sister. Joryn Venn marked with a square beside his name, not a circle. Mara Venn marked with a circle, then a smaller sign she did not know, drawn in the same hand as the mercy seal.

Responsive, the physician had written beside her name.

Mara could read upside down because pay tables were usually posted by men who did not care whether short girls could see them.

Responsive to what? she wanted to ask, but the wagon answered before anyone else did. The dead inside leaned toward the pocket where the cinder shard burned, and the black tags at their throats clicked together like teeth. The physician's eyes flicked to the sound, then to Mara, not with surprise. Confirmation.

Joryn saw the slate too.

His face changed in the way Mara hated most: not fear for himself, but the instant calculation of what he would spend to keep her unnamed. He had raised her through debt collectors, furnace quotas, foremen with easy fists, and winters when hunger made every moral rule expensive. He knew how systems ate people. He had not known this one had already opened its mouth around her.

"She is a child," he said.

The physician did not look at him. "She is a response hazard."

"She is a girl from the vents."

"Those are not exclusive categories."

The calm of that answer was worse than cruelty. Cruelty at least admitted itself. This man believed he was handling risk, moving suffering into proper channels, preventing panic by making a girl into a line item before she could become a witness.

Mara remembered Mordane on the platform saying capacity as if the word had never broken a spine.

She understood then that mercy wagons did not only carry the sick away from Kell Ashgate. They sorted the city into uses: lungs, hands, dead labor, inconvenient witnesses, strange girls who made corpses turn their heads. The food wagons had not bought silence. They had bought time for the sorting.

The second soldier drew a baton."""


BOOK3_CH13_ANCHOR = """Everyone wanted one army.

That was the problem.

"One army moves faster," Rook's nephew insisted."""

BOOK3_CH13_INSERT = """Everyone wanted one army.

That was the problem.

Mara could see the hunger for it moving around the wagon-door table. It was not only ambition. Ambition would have been easier to despise. It was fatigue. A mother from the east road wanted one army because her sons were in different columns and she could not bear two messengers. A Harrowmere quartermaster wanted one army because five ration systems had become a mathematics of starvation. A Lumenorath singer wanted one army because every independent camp meant another place where a healing song might arrive too late. A Khar Veyl scout wanted one army because secrecy scattered too easily when frightened people improvised.

Caldus wanted one army for half a breath too.

Mara saw it cross his face before he mastered it: the old soldier's instinct that a line held by one voice broke less quickly than a crowd debating in rain. Then he looked past the map to the refugee wagons, to the dead cavalry waiting under their own names, to Saelith standing beside a dark-elf shadow screen without flinching, to Kesh watching road markers as if each one had a price and a prayer. The instinct did not vanish. It became ashamed of being incomplete.

That was the shape of the whole council.

Every simple answer had one honest piece in it. One command could save time. One route could prevent confusion. One seal could protect a record. One song could steady a field hospital. One engine could release pressure before a town burned. But the old world had been built from honest pieces forced into crowns, chains, engines, and doctrines until no one remembered the forcing.

Mara had not crossed that much fire, ash, records, bridges, and dragon grief to build a cleaner leash.

"One army moves faster," Rook's nephew insisted."""


BOOK3_GLOSSARY = """## Glossary

**Answerable oath:** A vow that must include the right of those affected to question, interrupt, refuse, revise, or end it.

**Bone lanterns:** Orrowen civic lanterns that hold and reveal named dead witnesses without turning them into fuel.

**The Choir:** Vorrakai's mortal and undead agents, who offer stillness as mercy and use true pain to make surrender sound kind.

**Cinder:** A buried dragon-heart or memory-organ used as fuel, archive, weapon, or sacred object.

**Cinder-singer:** A person able to hear and answer cinder memory.

**Death-Dream:** Vorrakai's projected perfect stillness: a world where pain has ended because choice, grief, and contradiction have been laid down.

**The old covenant:** The first-age pact that buried dragon memory into mortal systems, turning dead dragons and the dead of later peoples into heat, law, and power.

**Othrava:** The dragon-moon whose body and memory lie under Orrowen, mother of buried storms and the wound at the heart of the cinder economy.

**Public dark:** Khar Veyl's repaired principle that dangerous truth may need care, but not ownership, secrecy, or unanswerable custody.

**Kell Ashgate:** Mara's mining city, poisoned by ash and hidden royal extraction.

**The Seven Arches:** Troll-guarded bridge shrines across the star canyon.

**Lumenorath:** Light-elf forest-citadels where beauty and law are dangerously intertwined.

**Khar Veyl:** Dark-elf under-realms that guard sealed histories and costly truths.

**Orrowen:** The buried empire where the dead remember themselves too strongly to end.

**The Named:** Undead who retain personhood through name, memory, and witness.

**Veyrasha:** A living dragon of the Court of Long Memory who helps mortals build dragon-scale consent practices after the covenant breaks.

**Vorrakai:** The first dragon, whose ancient grief seeks perfect stillness."""


def normalize_terms(text: str) -> str:
    text = re.sub(r"\blight elf(s?)\b", r"light-elf\1", text)
    text = re.sub(r"\bdark elf(s?)\b", r"dark-elf\1", text)
    return text


def remove_draft_comment(text: str, notes: list[str], book: str) -> str:
    cleaned = re.sub(
        r"\n?<!-- Full-length draft-zero manuscript generated for epic page-count targets\..*?-->\n",
        "\n",
        text,
        count=1,
        flags=re.DOTALL,
    )
    if cleaned != text:
        notes.append(f"{book}: removed draft-generation HTML comment.")
    return cleaned


def replace_once(text: str, old: str, new: str, label: str, notes: list[str]) -> str:
    if old in text:
        notes.append(label)
        return text.replace(old, new, 1)
    if new in text:
        return text
    raise ValueError(f"Could not find anchor for {label}")


def replace_many(text: str, replacements: list[tuple[str, str]], notes: list[str], label: str) -> str:
    changed = 0
    for old, new in replacements:
        if old in text:
            count = text.count(old)
            text = text.replace(old, new)
            changed += count
    if changed:
        notes.append(f"{label}: applied {changed} exact replacements.")
    return text


def replace_in_prefix(text: str, marker: str, transform, label: str, notes: list[str]) -> str:
    idx = text.find(marker)
    if idx == -1:
        raise ValueError(f"Could not find marker for {label}: {marker}")
    before = text[:idx]
    after = text[idx:]
    new_before = transform(before)
    if new_before != before:
        notes.append(label)
    return new_before + after


def replace_in_chapter(
    text: str,
    chapter_no: int,
    transform,
    label: str,
    notes: list[str],
) -> str:
    start_match = re.search(rf"(?m)^## Chapter {chapter_no}: .+$", text)
    if not start_match:
        raise ValueError(f"Could not locate chapter {chapter_no} for {label}")
    end_match = re.search(r"(?m)^## Chapter \d+: |^## Back Matter\b|^# Part ", text[start_match.end() :])
    end = start_match.end() + end_match.start() if end_match else len(text)
    before = text[: start_match.start()]
    chapter = text[start_match.start() : end]
    after = text[end:]
    new_chapter = transform(chapter)
    if new_chapter != chapter:
        notes.append(label)
    return before + new_chapter + after


def normalize_book_two_part_order(text: str, notes: list[str]) -> str:
    text = replace_once(
        text,
        "## Chapter 7: The White Road\n\n# Part II: Lumenorath\n\n",
        "# Part II: Lumenorath\n\n## Chapter 7: The White Road\n\n",
        "Book Two: moved Part II heading before Chapter 7.",
        notes,
    )
    text = replace_many(
        text,
        [
            (
                "## Chapter 13: The Downward Gate\n\n# Part III: Khar Veyl\n\n",
                "# Part III: Khar Veyl\n\n## Chapter 13: The Downward Gate\n\n",
            )
        ],
        notes,
        "Book Two: part-heading order",
    )
    return text


def fix_serathiel_book_two(text: str, notes: list[str]) -> str:
    replacements = [
        (
            """He had heard the clerks. He had heard Orrowen choosing complexity over release. It wounded him in a place Mara almost understood. His mercy could survive being opposed by soldiers. It could survive dark-elf seals, human crowns, gnome engines, even Mara's refusal. It could not survive the dead looking at quiet and choosing forms, argument, delay, and more mornings.

"This is cruelty," he said.""",
            """She had heard the clerks. She had heard Orrowen choosing complexity over release. It wounded her in a place Mara almost understood. Her mercy could survive being opposed by soldiers. It could survive dark-elf seals, human crowns, gnome engines, even Mara's refusal. It could not survive the dead looking at quiet and choosing forms, argument, delay, and more mornings.

"This is cruelty," she said.""",
        ),
        ("Serathiel's final hymn began as a single note under his breath.", "Serathiel's final hymn began as a single note under her breath."),
        (
            "His roots curled around the Lumenorath bridge. They had blackened where the record touched them, but the core still shone white. Serathiel looked less serene now. The memory storm had stripped him of distance. Mara saw the man under the saint-general: grief, discipline, terror of a world where mercy could fail even when practiced perfectly.",
            "Her roots curled around the Lumenorath bridge. They had blackened where the record touched them, but the core still shone white. Serathiel looked less serene now. The memory storm had stripped her of distance. Mara saw the woman under the saint-general: grief, discipline, terror of a world where mercy could fail even when practiced perfectly.",
        ),
        ('"Then I will save you from yourselves," he said.', '"Then I will save you from yourselves," she said.'),
        (
            """Serathiel walked through it all.

The roots parted for him. He looked almost luminous now, not because he had become stronger, but because he had shed everything that was not the hymn. His robes burned at the hem. His hair floated in the moonlight rising from below. His eyes held tears.""",
            """Serathiel walked through it all.

The roots parted for her. She looked almost luminous now, not because she had become stronger, but because she had shed everything that was not the hymn. Her robes burned at the hem. Her hair floated in the moonlight rising from below. Her eyes held tears.""",
        ),
        ('"I would have spared you this," he said.', '"I would have spared you this," she said.'),
        ("He closed his eyes, and for one impossible moment Mara thought he might stop.", "She closed her eyes, and for one impossible moment Mara thought she might stop."),
        ("Then a Choir singer stepped behind him and began to hum.", "Then a Choir singer stepped behind her and began to hum."),
        ("The hum wrapped his grief in Vorrakai's stillness.", "The hum wrapped her grief in Vorrakai's stillness."),
        ("Serathiel opened his eyes.", "Serathiel opened her eyes."),
        ('"Pain is not proof of truth," he said.', '"Pain is not proof of truth," she said.'),
        ("He lifted one hand toward her.", "She lifted one hand toward her."),
        ('"You mistake company for righteousness," he said.', '"You mistake company for righteousness," she said.'),
        ('"You can still come home," he said.', '"You can still come home," she said.'),
        ("Serathiel covered his ears.\n\n\"No,\" he whispered.", "Serathiel covered her ears.\n\n\"No,\" she whispered."),
        (
            "every person Serathiel had truly comforted, every comfort he later used as proof that his hand should never be refused.",
            "every person Serathiel had truly comforted, every comfort she later used as proof that her hand should never be refused.",
        ),
        ("Honest memory broke his hymn.", "Honest memory broke her hymn."),
        ("Serathiel fell to his knees.", "Serathiel fell to her knees."),
        ('"What am I," he asked, "if not mercy?"', '"What am I," she asked, "if not mercy?"'),
        (
            """Saelith knelt in front of him. "A man who wanted peace so badly he made people quiet."

His face crumpled.""",
            """Saelith knelt in front of her. "A woman who wanted peace so badly she made people quiet."

Her face crumpled.""",
        ),
        (
            """Here was the last door Serathiel could take: if corrected mercy hurt too much, stillness would receive him and make the pain meaningful.

Mara felt him lean toward it.

Saelith felt it too.

She did not grab him.""",
            """Here was the last door Serathiel could take: if corrected mercy hurt too much, stillness would receive her and make the pain meaningful.

Mara felt her lean toward it.

Saelith felt it too.

She did not grab her.""",
        ),
        ('Serathiel laughed once. It broke halfway through. "You learned cruelty."\n\n"No. I learned not to confuse refusal with cruelty."\n\nHe closed his eyes.', 'Serathiel laughed once. It broke halfway through. "You learned cruelty."\n\n"No. I learned not to confuse refusal with cruelty."\n\nShe closed her eyes.'),
        (
            """Then Serathiel removed the living white-root crown from his brow.

It tore skin when it came free. Blood ran silver down his face. The crown writhed in his hands, looking for doctrine, command, a head to sanctify.

Serathiel set it on the platform between them.

"I stand down," he said.""",
            """Then Serathiel removed the living white-root crown from her brow.

It tore skin when it came free. Blood ran silver down her face. The crown writhed in her hands, looking for doctrine, command, a head to sanctify.

Serathiel set it on the platform between them.

"I stand down," she said.""",
        ),
        (
            "Serathiel had spent centuries teaching mercy to obey him. His roots ran through soldiers, orchards, prayers, hospital rooms, children's lessons, funeral rites, and every person who had been comforted by the order he later weaponized.",
            "Serathiel had spent centuries teaching mercy to obey her. Her roots ran through soldiers, orchards, prayers, hospital rooms, children's lessons, funeral rites, and every person who had been comforted by the order she later weaponized.",
        ),
        (
            "A Choir singer put both hands on Serathiel's shoulders and whispered that he could rest now, that everyone had seen enough, that his surrender could be perfect if he stopped choosing through pain.",
            "A Choir singer put both hands on Serathiel's shoulders and whispered that she could rest now, that everyone had seen enough, that her surrender could be perfect if she stopped choosing through pain.",
        ),
        (
            '"If I speak alone, he can make me his lost daughter," she said. "If you speak alone, he can make you confused followers. We speak as corrected witness."',
            '"If I speak alone, she can make me her lost daughter," she said. "If you speak alone, she can make you confused followers. We speak as corrected witness."',
        ),
        (
            "Serathiel looked up as they approached. His face was blood-streaked from the torn crown. White roots trembled around his hands. He seemed old now, but not weak. Never weak. The danger in him had moved from certainty into ruin, and ruin could still want an audience.",
            "Serathiel looked up as they approached. Her face was blood-streaked from the torn crown. White roots trembled around her hands. She seemed old now, but not weak. Never weak. The danger in her had moved from certainty into ruin, and ruin could still want an audience.",
        ),
        ('"You come to judge," he said.', '"You come to judge," she said.'),
        ("Serathiel closed his eyes.\n\n\"Enough,\" he whispered.", "Serathiel closed her eyes.\n\n\"Enough,\" she whispered."),
        ("The roots around his hands loosened.", "The roots around her hands loosened."),
        ("When he placed it on the platform, the crown tried to crawl back to him.", "When she placed it on the platform, the crown tried to crawl back to her."),
        (
            "Serathiel stared at it. Without the crown's living light, the wound it left at his brow looked raw and human. Silver blood ran down the bridge of his nose. He did not wipe it away.",
            "Serathiel stared at it. Without the crown's living light, the wound it left at her brow looked raw and human. Silver blood ran down the bridge of her nose. She did not wipe it away.",
        ),
        ('"I stand down," he said again, but quieter, as if the first time had been spoken to the chamber and the second to the part of himself that had never believed it possible.', '"I stand down," she said again, but quieter, as if the first time had been spoken to the chamber and the second to the part of herself that had never believed it possible.'),
        (
            "Mara looked at Serathiel. He sat very still beneath the upside-down banner, alive because those he had harmed had not yet decided what justice required. He had wanted peace. He had wanted it sincerely enough to destroy people for refusing the shape of it.",
            "Mara looked at Serathiel. She sat very still beneath the upside-down banner, alive because those she had harmed had not yet decided what justice required. She had wanted peace. She had wanted it sincerely enough to destroy people for refusing the shape of it.",
        ),
        ('"No," Mara said. "But don\'t let grief turn him back into only what he gave you."', '"No," Mara said. "But don\'t let grief turn her back into only what she gave you."'),
        ('"Don\'t let anger turn him into only what he took, either," Mara added, surprising herself.', '"Don\'t let anger turn her into only what she took, either," Mara added, surprising herself.'),
        ("The Choir singer who had stood behind Serathiel stepped away from him.", "The Choir singer who had stood behind Serathiel stepped away from her."),
        ("After Serathiel stood down, the people who had needed him did not know where to put their hands.", "After Serathiel stood down, the people who had needed her did not know where to put their hands."),
        ("did not require him at the center.", "did not require her at the center."),
        ("His face was unreadable, but his hands shook in his lap.", "Her face was unreadable, but her hands shook in her lap."),
        (
            '"Those harmed by a doctrine should not be left alone with the man who carried it," she said. "Those who followed him should not be spared seeing him as a man."',
            '"Those harmed by a doctrine should not be left alone with the woman who carried it," she said. "Those who followed her should not be spared seeing her as a person."',
        ),
        ("Vaura saw Mara watching him.", "Vaura saw Mara watching her."),
        ('"He may yet become martyr," the dark-elf ruler said.', '"She may yet become martyr," the dark-elf ruler said.'),
        ("Serathiel, still seated under guard, lifted his head.", "Serathiel, still seated under guard, lifted her head."),
        ("It cost him to say it.", "It cost her to say it."),
        ("watching a dangerous man learn how not to be obeyed.", "watching a dangerous woman learn how not to be obeyed."),
        ("Caldus dragged Serathiel to his feet when the former saint-general did not move quickly enough.", "Caldus dragged Serathiel to her feet when the former saint-general did not move quickly enough."),
        (
            'Serathiel looked up. Without the crown, he seemed smaller. Not harmless. Smaller.\n\n"What will they do with me?" he asked.',
            'Serathiel looked up. Without the crown, she seemed smaller. Not harmless. Smaller.\n\n"What will they do with me?" she asked.',
        ),
        (
            'Serathiel, under guard, entered his name and former office. When asked standing, he said, "Contested."',
            'Serathiel, under guard, entered her name and former office. When asked standing, she said, "Contested."',
        ),
        ("Serathiel needed guards who would neither worship nor murder him.", "Serathiel needed guards who would neither worship nor murder her."),
        (
            "Serathiel standing before a white-root vanguard and raising his hands not like a priest but like a man conducting an execution politely.",
            "Serathiel standing before a white-root vanguard and raising her hands not like a priest, but like a saint-general conducting an execution politely.",
        ),
        (
            "Serathiel at its head, robes unstained despite the under-road's filth. Hymn wagons rolled behind him on wheels wrapped in cleansing script.",
            "Serathiel at its head, robes unstained despite the under-road's filth. Hymn wagons rolled behind her on wheels wrapped in cleansing script.",
        ),
        (
            "Serathiel walked at the front beneath a canopy of living white branches that had rooted into the wagon behind him. His beauty had become severe since Mara last saw him. Mercy had burned away everything in his face except certainty.",
            "Serathiel walked at the front beneath a canopy of living white branches that had rooted into the wagon behind her. Her beauty had become severe since Mara last saw her. Mercy had burned away everything in her face except certainty.",
        ),
        (
            "For one heartbeat his certainty cracked into something personal. Mara saw recognition, grief, and perhaps love if love had been starved and trained to salute. Then his gaze moved from Saelith to Mara, to the ledger case, to Edrin and Sava, to the Orrowen citizens gathering along the battlefield edges.",
            "For one heartbeat her certainty cracked into something personal. Mara saw recognition, grief, and perhaps love if love had been starved and trained to salute. Then her gaze moved from Saelith to Mara, to the ledger case, to Edrin and Sava, to the Orrowen citizens gathering along the battlefield edges.",
        ),
        ('"Cinder-bearer," he called.', '"Cinder-bearer," she called.'),
        ("Serathiel raised one hand, and the white-root branches behind him stirred.", "Serathiel raised one hand, and the white-root branches behind her stirred."),
        ("He looked down.\n\nAn Orrowen child, translucent and solemn, stood in the water before him holding a slate.", "She looked down.\n\nAn Orrowen child, translucent and solemn, stood in the water before her holding a slate."),
        ("His eyes lifted to hers.", "Her eyes lifted to hers."),
        ("Behind him, some Pale Bough soldiers looked at one another.", "Behind her, some Pale Bough soldiers looked at one another."),
        ("Serathiel felt it too; his hand tightened.", "Serathiel felt it too; her hand tightened."),
        (
            "Serathiel's conviction that if he stopped, all he had sacrificed would become murder instead of mercy.",
            "Serathiel's conviction that if she stopped, all she had sacrificed would become murder instead of mercy.",
        ),
        ("Serathiel stared at him as if betrayal had learned his hymns.", "Serathiel stared at him as if betrayal had learned her hymns."),
        ("Serathiel's white roots lifted behind him.", "Serathiel's white roots lifted behind her."),
        ("Serathiel stepped to the edge. White roots uncoiled behind him,", "Serathiel stepped to the edge. White roots uncoiled behind her,"),
        ("When Serathiel's officers remained clustered behind him,", "When Serathiel's officers remained clustered behind her,"),
        ("Serathiel raised his hand.", "Serathiel raised her hand."),
        (
            "It showed Serathiel young, standing beside a fever bed, weeping when a dead Orrowen witness would not stop repeating a child's last word. It showed the first time he chose to silence a witness and called the silence peace.",
            "It showed Serathiel young, standing beside a fever bed, weeping when a dead Orrowen witness would not stop repeating a child's last word. It showed the first time she chose to silence a witness and called the silence peace.",
        ),
        (
            "Serathiel looked almost relieved, as if doubt were a wandering child he could take by the hand and lead home.",
            "Serathiel looked almost relieved, as if doubt were a wandering child she could take by the hand and lead home.",
        ),
        ("Serathiel watched his order become plural.", "Serathiel watched her order become plural."),
        ("Serathiel closed his hand.", "Serathiel closed her hand."),
        ("Serathiel closed his eyes.", "Serathiel closed her eyes."),
        (
            "Serathiel stepped into the memory light, perhaps to use the fracture, perhaps because he could not bear guilt that did not arrange itself conveniently around Khar Veyl.",
            "Serathiel stepped into the memory light, perhaps to use the fracture, perhaps because she could not bear guilt that did not arrange itself conveniently around Khar Veyl.",
        ),
        (
            '"Yes," he said, and the word rang with terrible honesty. "And I would again."',
            '"Yes," she said, and the word rang with terrible honesty. "And I would again."',
        ),
        (
            "That truth did not absolve him. It made the danger cleaner. Serathiel believed what he had done was mercy. He would not be unmasked as a secret cynic. He was worse: a faithful man whose faith had made other people's consent optional.",
            "That truth did not absolve her. It made the danger cleaner. Serathiel believed what she had done was mercy. She would not be unmasked as a secret cynic. She was worse: a faithful woman whose faith had made other people's consent optional.",
        ),
        ("Saelith turned to him.\n\n\"Enter Lumenorath culpability.\"", "Saelith turned to her.\n\n\"Enter Lumenorath culpability.\""),
        ("His face hardened.\n\nThe full record moved behind him,", "Her face hardened.\n\nThe full record moved behind her,"),
        ("Serathiel raised his chin.", "Serathiel raised her chin."),
        (
            "Mara understood the danger of that waiting. Serathiel had not lied exactly. He had sought rest.",
            "Mara understood the danger of that waiting. Serathiel had not lied exactly. She had sought rest.",
        ),
        ("Saelith stepped onto his bridge.", "Saelith stepped onto her bridge."),
        ("He looked at her.\n\n\"Saelith.\"", "She looked at her.\n\n\"Saelith.\""),
        (
            "The note belonged to Serathiel.\n\nHe did not deny it.\n\nThe memory showed him at a bedside, as Saelith's earlier vision had, silencing a witness who repeated a child's last word.",
            "The note belonged to Serathiel.\n\nShe did not deny it.\n\nThe memory showed her at a bedside, as Saelith's earlier vision had, silencing a witness who repeated a child's last word.",
        ),
        ("Mara almost pitied him.", "Mara almost pitied her."),
        ("making him central.", "making her central."),
        ("His eyes cut to her.", "Her eyes cut to her."),
        ("Vorrakai's grief touched him.", "Vorrakai's grief touched her."),
        ('Serathiel closed her eyes.\n\n"Then I will save what remains," he said.', 'Serathiel closed her eyes.\n\n"Then I will save what remains," she said.'),
        ("The Choir singer behind him smiled", "The Choir singer behind her smiled"),
        ("Honest memory broke his hymn, but it did not erase the reasons people had sung it.", "Honest memory broke her hymn, but it did not erase the reasons people had sung it."),
        ("His final grove fought on.", "Her final grove fought on."),
        (
            "Mara watched and thought that this, more than Serathiel's crown on the floor, was his fall: the people he had shaped learning practices that did not require her at the center.",
            "Mara watched and thought that this, more than Serathiel's crown on the floor, was her fall: the people she had shaped learning practices that did not require her at the center.",
        ),
        ("Sava assigned two Orrowen citizens and one corrected Pale Bough officer to guard him.", "Sava assigned two Orrowen citizens and one corrected Pale Bough officer to guard her."),
        ("Serathiel saw every quiet face he had called healed.", "Serathiel saw every quiet face she had called healed."),
        ("Even Serathiel bowed his head,", "Even Serathiel bowed her head,"),
        (
            "Mara watched Serathiel watching his own soldiers become particular. His face had gone white under the white-root glow.",
            "Mara watched Serathiel watching her own soldiers become particular. Her face had gone white under the white-root glow.",
        ),
        ("Serathiel's expression flickered with pain before he mastered it.", "Serathiel's expression flickered with pain before she mastered it."),
        ('"Yes." She looked at him with such naked grief that even Serathiel\'s roots stilled.', '"Yes." She looked at her with such naked grief that even Serathiel\'s roots stilled.'),
        ("Not because Mara had defeated him. Not because the company was pure.", "Not because Mara had defeated her. Not because the company was pure."),
        (
            "Words had failed him. That was what made the sound so dangerous. Doctrine could be argued with. Commands could be refused. Even beauty, once named, could be answered by another beauty. But the hymn he loosed into the dragon-moon chamber was older than the Pale Bough's laws and simpler than mercy. It was the sound a person made when he could no longer bear the freedom of those he loved.",
            "Words had failed her. That was what made the sound so dangerous. Doctrine could be argued with. Commands could be refused. Even beauty, once named, could be answered by another beauty. But the hymn she loosed into the dragon-moon chamber was older than the Pale Bough's laws and simpler than mercy. It was the sound a person made when she could no longer bear the freedom of those she loved.",
        ),
        ('"He is not killing them," Caldus said, horror in his voice.', '"She is not killing them," Caldus said, horror in his voice.'),
        ('Saelith\'s face was ashen. "No. He is making them easy to mourn."', 'Saelith\'s face was ashen. "No. She is making them easy to mourn."'),
        ("See, the deep voice seemed to say. He understands one door.", "See, the deep voice seemed to say. She understands one door."),
        ('"He did good," she said through her teeth. "That is the cruelty. He did good, and then made the good a throne."', '"She did good," she said through her teeth. "That is the cruelty. She did good, and then made the good a throne."'),
        ("bedside manners before he learned conquest.", "bedside manners before she learned conquest."),
        ("He came to Saelith.", "She came to Saelith."),
        ("She stood between him and Nim's lantern,", "She stood between her and Nim's lantern,"),
        ("She stood between her and Nim's lantern,", "Saelith stood between Serathiel and Nim's lantern,"),
        ("The sound around him did not cleanse, seal, command, or still.", "The sound around her did not cleanse, seal, command, or still."),
        ("Not by proving he had never loved.", "Not by proving she had never loved."),
        ("By proving love had not made him safe.", "By proving love had not made her safe."),
        ("The roots collapsed around him, not dead, but unmastered.", "The roots collapsed around her, not dead, but unmastered."),
        ("That, Mara thought, was the first mercy he had been given all day.", "That, Mara thought, was the first mercy she had been given all day."),
        ("The Choir singer behind him hissed.", "The Choir singer behind her hissed."),
        ('Then Saelith asked, "Is it wrong that I am grieving him?"', 'Then Saelith asked, "Is it wrong that I am grieving her?"'),
        ("He removed the white-root crown.", "She removed the white-root crown."),
        ('He closed his eyes. "Pale Bough command will not pass through my office, my name, my former rank, or any doctrine entered under my correction without review by those harmed."', 'She closed her eyes. "Pale Bough command will not pass through my office, my name, my former rank, or any doctrine entered under my correction without review by those harmed."'),
    ]
    return replace_many(text, replacements, notes, "Book Two Serathiel continuity")


def fix_serathiel_book_three(text: str, notes: list[str]) -> str:
    replacements = [
        ("I saw him try to cleanse Orrowen rather than hear it. I saw him call love what would have erased the dead.", "I saw her try to cleanse Orrowen rather than hear it. I saw her call love what would have erased the dead."),
        ("while a holy man was humiliated.", "while a holy woman was humiliated."),
        ("Serathiel failed younger and with fewer dead to his name.", "Serathiel failed younger and with fewer dead to her name."),
    ]
    return replace_many(text, replacements, notes, "Book Three Serathiel continuity")


def remove_meta_language(text: str, notes: list[str], book: str) -> str:
    replacements = [
        ("Book Two opened under her feet without naming itself.", "The next road opened under her feet before any of them could name it."),
        ('Ilyr closed his eyes. "Then Book Two will be unpleasant."', 'Ilyr closed his eyes. "Then the road ahead will be unpleasant."'),
        ("Book One resolves the liberation of Kell Ashgate and the fall of Mordane's foundry. Its unanswered promise is the waking of the wider cinder network, the unresolved fate of Maelin Noct-Vey, and the journey toward Lumenorath, Khar Veyl, and the moon below Orrowen.", "Kell Ashgate is free, Mordane's foundry has fallen, and the wider cinder network is waking toward Lumenorath, Khar Veyl, and the moon below Orrowen."),
        ('"It sounds like exactly where you will be useful, which is how every horrible device in this trilogy tries to flirt with you."', '"It sounds like exactly where you will be useful, which is how every horrible device in this catastrophe tries to flirt with you."'),
        ("He had spent his last death in Book One's furnace truth,", "He had spent his last death in Kell Ashgate's furnace truth,"),
        ("The next chapter's choice had arrived, brass-toothed and useful enough to damn them all.", "The next terrible choice had arrived, brass-toothed and useful enough to damn them all."),
        ("since Book Two began", "since the first road out of Kell Ashgate began"),
        ("leading into Book Three's dark", "leading into the next war's dark"),
        ("Book Two's war was over.", "The war below the world was over."),
        ('"Book Two ends here," Kesh said suddenly.', '"This war ends here," Kesh said suddenly.'),
        ('"What is Book Two?" Tavi mumbled without opening her eyes.', '"What war?" Tavi mumbled without opening her eyes.'),
        ("A metaphorical unit of suffering.", "This particular unit of suffering."),
        ("Book Three had opened its eye.", "The next nightmare had opened its eye."),
        ("Mara held both truths because the book had taught her what happened when anyone kept only one.", "Mara held both truths because the road had taught her what happened when anyone kept only one."),
        ("Mara would not survive Book Three by choosing a cleaner blindness.", "Mara would not survive the next waking by choosing a cleaner blindness."),
        ("Book Two resolves the elven holy war and the immediate enslavement of Orrowen's dead. Its unanswered promise is the opened eye of the dragon-moon and the return of Vorrakai's dream.", "The elven holy war has stopped, Orrowen's dead stand in their own names, and the opened eye of the dragon-moon points toward the return of Vorrakai's dream."),
        ("Book Two had left wounds too raw for easy satisfaction.", "The war below Orrowen had left wounds too raw for easy satisfaction."),
        ("since Book One's road", "since the first road out of Kell Ashgate"),
        ("The manuscript of the world did not punish them for it.", "The ledger of the world did not punish them for it."),
        ("The first clash did not yet belong to Chapter Twenty-Nine, but it gave that chapter its debt.", "The first clash had not yet become the next battle, but it gave that battle its debt."),
        ("That was the heroism of the chapter.", "That was the heroism of the hour."),
        ("Book Three closes the trilogy by breaking the old covenant, ending the cinder economy, and leaving Vael Taryn freer, poorer, louder, and alive.", "The old covenant is broken, the cinder economy has ended, and Vael Taryn is left freer, poorer, louder, and alive."),
        ("She had spent three books of her life refusing to be used.", "She had spent the whole long road from Kell Ashgate refusing to be used."),
        ("For three books, every crisis had tried to teach her", "For the whole long road, every crisis had tried to teach her"),
        ("It was the least heroic sound she had made in three books and therefore one of the truest.", "It was the least heroic sound she had made since the first corpse rose and therefore one of the truest."),
        ("For three books, heat had lived under her skin whether she wanted it or not:", "For the whole long road, heat had lived under her skin whether she wanted it or not:"),
    ]
    return replace_many(text, replacements, notes, f"{book}: removed fiction-breaking book/chapter language")


def fix_book_three_identity_collisions(text: str, notes: list[str]) -> str:
    def forge_dragon(chapter: str) -> str:
        return chapter.replace("Veyrasha", "Rhyssara")

    text = replace_in_chapter(text, 19, forge_dragon, "Book Three chapter 19: renamed buried forge-dragon to Rhyssara.", notes)

    def pre_public_dark(prefix: str) -> str:
        prefix = re.sub(r"\bEdda Mar\b", "Brenna Holt", prefix)
        prefix = re.sub(r"\bEdda's\b", "Brenna's", prefix)
        prefix = re.sub(r"\bEdda\b", "Brenna", prefix)
        prefix = re.sub(r"\bLio's\b", "Tovin's", prefix)
        prefix = re.sub(r"\bLio\b", "Tovin", prefix)
        prefix = prefix.replace("Tovin from Third Arch, not shot through by road fear.", "Tovin from Harth Bend, not drowned in the millrace.")
        return prefix

    text = replace_in_prefix(text, "## Chapter 37: The Public Dark", pre_public_dark, "Book Three: separated Harth Bend Brenna/Tovin from Kell Ashgate Edda/Lio names.", notes)
    text = replace_many(
        text,
        [
            ('"My grandmother died in a royal mine warmed by one of those memories."', '"My aunt died in a royal mine warmed by one of those memories."'),
            ('"Relation to Edda Mar?"\n\n"Daughter."', '"Relation to Edda Mar?"\n\n"Niece."'),
        ],
        notes,
        "Book Three: corrected Vessa/Edda family relation",
    )
    return text


def expand_book_three_glossary(text: str, notes: list[str]) -> str:
    old = re.search(r"(?s)(?:## Back Matter\n\n)?(?:### Closing Note\n\n.*?\n\n)?(?:### |## )Glossary\n\n.*\Z", text)
    if not old:
        raise ValueError("Could not locate Book Three back-matter glossary")
    new_text = text[: old.start()] + BOOK3_GLOSSARY + "\n"
    if new_text != text:
        notes.append("Book Three: expanded final glossary and removed meta closing language.")
    return new_text


def polish_book_one(text: str, notes: list[str]) -> str:
    text = remove_draft_comment(text, notes, "Book One")
    text = replace_once(text, BOOK1_CH4_ANCHOR, BOOK1_CH4_INSERT, "Book One chapter 4: expanded Mordane mercy-wagon sorting beat.", notes)
    text = replace_once(text, BOOK1_CH5_ANCHOR, BOOK1_CH5_INSERT, "Book One chapter 5: expanded Caldus/Pell bridge beat.", notes)
    fixed_quotes = re.sub(r'"Maybe," she said\. "But not alone\."*', '"Maybe," she said. "But not alone."', text)
    if fixed_quotes != text:
        notes.append("Book One: fixed missing closing quotation mark.")
        text = fixed_quotes
    text = remove_meta_language(text, notes, "Book One")
    return normalize_terms(text)


def polish_book_two(text: str, notes: list[str]) -> str:
    text = remove_draft_comment(text, notes, "Book Two")
    text = normalize_book_two_part_order(text, notes)
    text = fix_serathiel_book_two(text, notes)
    text = remove_meta_language(text, notes, "Book Two")
    return normalize_terms(text)


def polish_book_three(text: str, notes: list[str]) -> str:
    text = remove_draft_comment(text, notes, "Book Three")
    text = replace_once(text, BOOK3_CH13_ANCHOR, BOOK3_CH13_INSERT, "Book Three chapter 13: expanded no-single-army compact stakes.", notes)
    text = replace_once(text, BOOK3_CH17_ANCHOR, BOOK3_CH17_INSERT, "Book Three chapter 17: expanded Glass Reed Line battle and refugee beat.", notes)
    text = fix_serathiel_book_three(text, notes)
    text = fix_book_three_identity_collisions(text, notes)
    text = remove_meta_language(text, notes, "Book Three")
    text = expand_book_three_glossary(text, notes)
    return normalize_terms(text)


def write_report(notes: list[str]) -> None:
    coverage = [
        "Book One: removed draft HTML comment, fixed the Chapter 35 closing quote, and deepened Chapters 4-5.",
        "Book Two: removed draft HTML comment, moved Part II/III headings to clean boundaries, removed fiction-breaking book/chapter language, and normalized Serathiel as she/her throughout.",
        "Book Three: removed draft HTML comment, deepened Chapters 13 and 17, renamed the buried forge-dragon to Rhyssara, kept living Veyrasha distinct, renamed Harth Bend's baker to Brenna Holt, renamed the Harth Bend boy to Tovin, corrected Vessa/Edda's family relation, and expanded the final glossary.",
        "All books: normalized light-elf/dark-elf terminology and removed visible draft/scaffold language from the fiction.",
    ]
    lines = [
        "# Trilogy Consistency Polish Pass",
        "",
        "Date: 2026-05-18",
        "",
        "This pass applies the concrete continuity, flow, and production fixes surfaced by the five-role review team.",
        "",
        "## Pass Coverage",
        "",
    ]
    lines.extend(f"- {item}" for item in coverage)
    lines.extend(["", "## Last Run Notes", ""])
    if notes:
        lines.extend(f"- {note}" for note in notes)
    else:
        lines.append("- No new manuscript changes were required; pass is idempotent against the current files.")
    lines.extend(
        [
            "",
            "## Follow-Up Watchlist",
            "",
            "- Run a final line proof for repeated rhetorical endings after the structural consistency pass.",
            "- Decide final publication front matter and whether closing notes stay as back matter or move into production-only files.",
            "- Continue using the generated chapter split as the revision workspace after every manuscript-level polish run.",
            "",
        ]
    )
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    notes: list[str] = []

    BOOK1.write_text(polish_book_one(BOOK1.read_text(encoding="utf-8"), notes), encoding="utf-8")
    BOOK2.write_text(polish_book_two(BOOK2.read_text(encoding="utf-8"), notes), encoding="utf-8")
    BOOK3.write_text(polish_book_three(BOOK3.read_text(encoding="utf-8"), notes), encoding="utf-8")
    write_report(notes)
    print(f"Applied trilogy consistency polish pass with {len(notes)} note groups.")


if __name__ == "__main__":
    main()
