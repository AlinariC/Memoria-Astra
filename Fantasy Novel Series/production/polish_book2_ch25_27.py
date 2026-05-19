#!/usr/bin/env python3
"""Revision pass 01g for Book Two chapters 25-27.

Replaces the first half of the Part V scaffold with bespoke climax scenes:
the dragon-moon chamber, Saelith's public renunciation, and Ilyr opening the
full historical record before both elven courts.
"""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "output" / "book-02-the-moon-below-the-world"
MANUSCRIPT = BOOK / "manuscript.md"
METADATA = BOOK / "metadata.yaml"
SUMMARY = ROOT / "output" / "README.md"


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


CHAPTERS: dict[int, str] = {
    25: r"""## Chapter 25: The Chamber of the Dragon-Moon

The way down opened under the bridge no one had meant to build.

It began as a crack in the ghost-water at Brakka's feet. One moment the battlefield held its breath around a messy table of terms, healers crossing, clerks arguing, soldiers discovering the humiliating labor of not killing one another. The next, the dry riverbed at the center of Orrowen split along a seam older than the city. Pale light leaked upward, not white-root, not ghost-lamp, not cinder fire. It was the color of bone seen under deep water.

Every cinder in the cavern turned toward it.

Mara felt the pull in her teeth.

So did the armies.

Lumenorath's hymn wagons groaned as roots strained toward the crack. Khar Veyl seal rods shivered in wardens' hands. Orrowen ghost-lamps bent their flames low. The Choir, scattered among both banks of the dry riverbed, lifted their faces with the terrible peace of people hearing a door unlock from the inside.

Vorrakai did not speak.

It did not have to.

"Nobody move," Caldus said.

Naturally, everyone moved.

Serathiel stepped forward first, one white hand raised as if the underworld were a chapel that had forgotten its manners. Vaura Noct-Vey moved at the same time from the opposite bank, seal rod lowered, black-thread banner behind her. The blade-scholar tried to climb out of the riverbed again and was yanked back down by three Orrowen citizens who had developed strong procedural opinions about him. Saelith went after Serathiel. Maelin went after Vaura. Tavi dropped to her knees at the crack and began measuring a myth with a bit of wire.

Kesh looked at Mara. "I am sensing disagreement."

"Hold the line," Mara said.

"Which one?"

"All of them."

"Cruel management."

He vanished into motion anyway.

The crack widened.

Stone folded away in steps. Not broken. Folded, like paper creased long ago and opened by patient hands. Beneath the riverbed, a stair descended through a tunnel lined with dragon-scale plates and civic chains. Every plate bore the mark of a different people. Light-elf healing script. Dark-elf emergency law. Gnome equations. Troll bridge knots. Goblin route scratches. Human ash tallies. Orrowen names repeated until repetition became architecture.

At the top of the stairs appeared a line of blue fire.

TERMS REQUIRE CHAMBER WITNESS.

Assistant Registrar Othel made a sound of professional despair. "Of course they do."

Sava Rennet straightened. "The chamber was sealed pending full emergency review."

"When was review scheduled?" Tavi asked.

"After hostilities ceased."

Caldus glanced across the battlefield, where two armies, a dead city, and a dragon death cult had all paused with visible reluctance. "Optimistic committee."

Vaura struck her seal rod once. "Khar Veyl will descend with full warding authority."

Serathiel's white roots lifted behind him. "Lumenorath will descend with cleansing authority."

The crack flared.

AUTHORITY CONTESTED.

For the first time that day, both leaders looked offended by the same sentence.

Mara stepped to the stair.

"Mixed witness descends," she said.

The line of blue fire shifted.

ACCEPTED.

Serathiel's eyes found her. "You presume much."

"I have been told that by better judges and worse men."

Kesh reappeared at her shoulder. "And once by a vegetable-adjacent witness fungus."

"It was a fungus," Tavi said without looking up.

"The scholarship continues to wound me."

Brakka lifted her maul from the bridge point. The battlefield lights dimmed, but did not fail. She staggered once. Mara reached for her and stopped because Brakka shook her head.

"Bridge still holds," the troll said. "But chamber wants deeper oath."

"Can you give it?" Caldus asked.

Brakka's arms were cracked with vow-light from shoulder to wrist. "Can. Should is wider question."

"No one goes alone," Mara said.

The chamber answered with a sound like stone remembering laughter.

In the end, they descended as a company no law would have designed and no song would have believed. Mara went first because everyone argued until she stepped forward and ended the discussion by putting her boot on the stair. Caldus came behind her, one arm bandaged, sword loose in his good hand. Saelith followed with the red fungal bell at her throat and exile colors unhidden. Tavi carried the root-hound collar wrapped around one wrist and a pack full of tools that clicked with nervous intelligence. Kesh carried three stolen writs, two official triage tags, and one expression of deep innocence. Brakka carried the bridge.

Ilyr and Maelin bore the ledger case between them. Edrin and Sava came as Orrowen citizens. Assistant Registrar Othel came because he refused to allow an apocalypse to proceed with incomplete attendance. Vaura brought two wardens and Velra of the lower canals. Serathiel brought three Pale Bough officers and the shaved-headed scout who had requested correction, though he clearly had not meant to. Three Choir singers came without invitation. No one stopped them. Everyone noticed.

The armies remained above under bridge law, furious and alive.

The stair went down farther than it had room to go.

Mara had walked many descents by then: mines under Ashgate, Harrowmere's dead courts, Khar Veyl's drowned archive, the Glass Engine's hot galleries. This was different. Those places had been built by people trying to make stone obey. This stair felt grown from a wound that wanted witnesses before it closed or split.

At every landing, memory rose.

On the first, she saw dragons falling over an unmarked plain while gnomes beneath them calculated cinder yield with tears on their faces because grief had not stopped anyone from writing numbers. On the second, light-elf healers argued that death memory could be soothed, not owned. On the third, dark-elf judges argued that emergency custody would last one winter. On the fourth, human kings signed for ash allotments in exchange for silence. On the fifth, goblin road-keepers marked smuggler routes for refugees and then sold copies because hunger did not become noble merely because it stood beside courage. On the sixth, troll bridge-makers refused to close a crossing and were recorded as obstruction.

Brakka stopped at that landing.

The image showed a troll woman older than mountains standing on a bridge of living stone while elven soldiers shouted from both banks. Behind her, Orrowen children crossed with slates held over their heads.

"Kin?" Mara asked.

"Old oathmother," Brakka said.

In the vision, the troll woman was struck by seven spears and remained standing until the last child crossed. Then she sat down carefully so the bridge would not feel abandoned.

Brakka touched the wall. "Bridge remembers."

"It should," Caldus said.

No one made that sentence prettier.

They continued.

The final stair opened into a horizon.

Mara's mind refused it at first. The chamber beneath Orrowen was not a room, not a cavern, not any shape she had learned to trust. It was an interior sky. A vast curve filled the distance below them, pale and ridged and luminous, stretching from one side of the dark to the other until perspective broke. It was not moon in the way the surface moons were moons. It had no sky to hang in. It was a body curled under the world, scale and bone and cinder memory, a horizon made from a dead dragon's side.

Along that horizon lay an eye.

Closed.

Huge enough that Ashgate could have fit on its lid like a fleck of soot.

The company stood on a circular platform suspended above the dragon-moon by chains the size of towers. Seven bridges radiated from the platform to dark galleries. On each bridge burned the marks of a different people. Around the chamber's rim rose engines, seals, roots, chains, bells, glass ribs, prayer columns, old war machines, and civic desks. It was not one prison. It was every compromise that had ever been called temporary and then inherited by cowards.

Tavi whispered a word Mara had never heard her use in prayer or profanity.

Kesh's voice was small. "That is not a moon."

"No," Ilyr said. "It is what our courts agreed to call one so no one had to say body."

Serathiel stepped to the edge. White roots uncoiled behind him, trembling toward the closed eye. "Abomination."

The chamber shook.

Not violently.

In offense.

Sava's head snapped up. "Careful."

Serathiel did not listen. "A dead god's corpse bound under the world, leaking rot into memory. This is the source. Cleanse it, and the dead may sleep."

Vaura's seal rod struck the platform. "Touch it and every cinder line in Vael Taryn will fracture. You would burn the world to make your doctrine symmetrical."

"You locked the wound and called cowardice stewardship."

"We kept your ancestors from making a sun of it."

"You sold the lock key."

"And your priests used the light through the keyhole to invent purity."

Their voices rose.

The chamber responded.

On the platform floor, lines of dragon-scale script ignited. Every accusation became light. Every denial became heat. Serathiel's roots writhed. Vaura's seals smoked. The Choir singers smiled, and that frightened Mara more than the anger.

Mara understood then why the chamber had accepted mixed witness and rejected authority. It was built from power claims. Authority fed it. Confession changed its shape.

"Stop arguing like rulers," she said.

No one stopped.

So Brakka drove her maul into the platform.

The sound traveled down the chains, across the bridges, through engines and roots and seals, into the pale curve of the dragon-moon. The closed eye twitched.

"This chamber is bridge," Brakka said.

The declaration nearly broke her.

Mara saw it happen: vow-light splitting her arms again, crawling up her throat, turning her voice into stone over flood. Brakka did not fall. Caldus caught her shoulder anyway. She let him.

"Bridge between histories," Brakka continued. "No side crosses into answer until all dead under crossing are named as people."

The chamber listened.

Then it accepted.

Every bridge into the platform lit. On each gallery, sealed doors opened, revealing archives, engines, hymn roots, war ledgers, civic rolls. Records no one faction had owned because all of them had stolen pieces.

Edrin Vale bowed his head. "Orrowen appears."

"Orrowen appears," Sava echoed.

Serathiel's face had gone very still.

Vaura looked at the opened records as if every door had teeth.

Mara felt the cinder in her cage pulse in answer to the dragon-moon. The dead body below was not silent. Its sleep moved through her blood, massive and wounded. Vorrakai's dream lay curled within it, not the whole first dragon, not yet, but enough grief to drown a world if someone called drowning mercy.

One of the Choir singers began to hum.

Tavi turned so fast her tools rattled. "No."

The hum stopped.

The singer, a dark-elf woman with cinder-filmed eyes, smiled gently. "All bridges reach an ending."

"Some bridges reach lunch," Kesh said. "You people have no range."

The woman looked at him with pity.

Mara stepped between them before pity could become song. "Terms," she said. "The chamber accepted bridge law. We hear terms."

"My terms are simple," Serathiel said. "Lumenorath burns the corruption from the dragon-moon. Orrowen's dead are released from unclean continuance. Khar Veyl submits its records to cleansing review. Those who repent may be carried into dawn."

Saelith closed her eyes.

Mara watched her friend's face, the pain there, the old training pulling like hooks. Saelith had spent a lifetime being told mercy meant making suffering clean enough to manage. Serathiel's words were not crude. They were beautiful. That was why they had survived.

Vaura answered before Saelith could. "Khar Veyl seals the chamber, captures the Choir, and assumes emergency custody of all records until the dragon-moon stabilizes. Lumenorath withdraws under escort. Orrowen retains provisional standing under council review."

Maelin laughed.

It was a terrible sound, bright and hurt.

"You heard the courthouse void an eternal sentence this morning," she said. "And your imagination returned by lunch to provisional standing."

Vaura flinched. Only a little. Enough.

Ilyr opened the ledger case. "No term stands until the record is read."

The platform darkened.

Every opened gallery drew breath.

Serathiel looked at him. "You are a confessed trafficker in stolen names."

"Yes."

"Your record is poison."

"Yes."

Vaura's eyes sharpened. "Ilyr."

He did not look at her. "My record is poison because poison was the business model. That is why it must be read where no one can pretend the bottle is medicine."

Mara saw fear pass between Vaura and Serathiel, quick as a blade signal. Not fear of lies. Fear of full truth spoken where neither could curate it.

The chamber answered that fear with another line of fire.

TRUTH BECOMES TACTICAL NECESSITY.

Kesh stared at the words. "The room has a better sense of timing than most generals."

"Then let it command," one of Vaura's wardens muttered.

Tavi snapped, "That is how we got every terrible machine in this chamber."

Sava climbed onto the central dais. It had not been there a moment before, or perhaps it had waited to be needed. "Proceed by record."

"Proceed by witness," Edrin said.

"Proceed by bridge," Brakka said, voice rough.

Mara looked at Saelith. Saelith was still staring at Serathiel as if the most beautiful cage in her life had opened and she could not yet make herself step away.

Mara wanted to reach for her.

She did not.

Some crossings had to begin under a person's own feet.

Ilyr placed the first black page on the dais.

It unfolded into light.
""",
    26: r"""## Chapter 26: Saelith Breaks the Beautiful Law

The black page unfolded, and Serathiel sang over it.

He did not shout. That would have been easier to resist. His voice entered the chamber like dawn laid gently over a battlefield, tender enough that even the dead seemed to pause. White roots trembled along the Lumenorath bridge. The Pale Bough officers behind him lowered their heads by instinct. The rescued scouts flinched, then began to mouth the response before remembering why they had come.

Saelith did not move.

Mara saw the song reach her.

Beautiful law had always worked by making obedience feel like recognition. The melody carried hearths Saelith had lost, teachers she had trusted, children healed under white boughs, old prayers spoken over fever beds, a hundred true mercies braided into one command. It was not all false. That was how it held. It wrapped itself around the good that had been real and said, because this was real, the rest must be holy too.

The black page dimmed.

Ilyr's hand tightened on the edge of the dais. Maelin stepped beside him, but a white root shot from the Lumenorath bridge and coiled around the ledger case, not crushing, only stilling. Tavi reached for a tool. Caldus lifted his sword. Brakka's maul hummed in the platform.

Mara looked at Saelith.

Saelith was singing.

The sound was barely audible, but Mara knew the shape of it from Lumenorath: the cleansing response, the line that turned witness into contamination and fear into duty. Saelith's lips formed the words without her consent, old training walking through her mouth in clean sandals.

Serathiel saw.

His face softened.

"Come back," he said to her, and because he meant it, because some broken part of him truly wanted the girl he had raised into a blade to return before she was too stained to hold, the chamber did not flare against the sentence.

Saelith swayed.

Mara's cinder woke hard.

She could break the root. She could cut the song. She could throw her own name into the chamber and make a bigger noise. Every frightened part of her wanted to. Saelith was not a symbol, not a battlefield, not a lesson in respecting autonomy while roots climbed toward her throat.

But Saelith had told her: If you choose for me, even to spare me, you become another knife.

Mara kept her hands at her sides.

"Saelith," she said.

That was all.

Not command.

Not rescue.

Door.

Saelith's eyes found hers.

The cleansing response faltered.

Serathiel's expression sharpened. "She cannot save you from what you are."

"No," Saelith whispered.

The word was so small the chamber almost missed it.

Mara did not.

"No," Saelith said again.

White roots tightened around the ledger case. The Pale Bough officers began the harmony, their voices stronger, trained to cover doubt with beauty. The song rose through the chamber. It showed Mara what Lumenorath believed itself to be: not tyrant, not killer, but gardener, healer, gentle hand cutting rot before it spread to children.

Saelith stepped away from Serathiel's bridge.

The harmony cracked.

"I was taught," she said, and her voice shook badly enough that no one could mistake courage for ease, "that mercy is clean."

The red fungal bell at her throat glowed.

She touched it.

"I was taught that memory can become infection. That grief can rot a city. That the dead below us are wounds the living must not touch. I was taught to cut gently, to burn softly, to smile while removing what frightened us."

Serathiel's white roots lifted higher. "You were taught to spare the world a second drowning."

"I was taught to call people world when they obeyed and drowning when they did not."

The chamber flared gold and red.

The black page on the dais brightened again.

Serathiel's face hardened. "You speak in pain."

"Yes."

"Pain is not truth."

"No. But neither is comfort."

The rescued shaved-headed scout stepped from behind Serathiel's officers. Her name, Mara remembered, was Liora, corrected from the White Orchard rolls. She looked terrified. She looked at Saelith as if watching someone jump from a tower and deciding whether air might hold.

Saelith saw her.

The next words were not for Serathiel.

"Matriarch Aurenne wrote, 'If memory is the wound, then we must learn not to cut it out.'"

The chamber took the sentence and made it visible.

It appeared in red-gold light above the Lumenorath bridge. Every Pale Bough officer saw it. Every soldier above through bridge law felt its echo. Serathiel's roots recoiled as if burned.

"Forgery," he said.

The black page answered.

A memory unfolded beside the dais: Matriarch Aurenne in plain white linen, kneeling beside an Orrowen woman whose hands shook with death-memory. Not cleansing her. Washing her palms. We do not heal a song by tearing out the note that hurts, Aurenne said. We learn why it hurts and who taught it to suffer alone.

The Pale Bough officers stopped singing.

Only Serathiel continued.

His voice grew brighter, not louder. "Compassion without purity becomes permission for rot."

Saelith walked toward him.

No one stopped her. That might have been bridge law. It might have been awe. It might have been that everyone understood this bridge was hers and terrible.

White roots curled around her ankles.

She did not burn them.

She knelt.

For one sick heartbeat Mara thought she had surrendered.

Then Saelith pressed both hands to the roots and said, "I release myself from the command to cleanse what I fear."

The roots flashed.

Serathiel inhaled.

Saelith continued, each word steadier than the last. "I release myself from the beautiful law that made obedience feel like mercy. I release every lesson that taught my hands to ask whether a person was clean before asking whether they hurt. I release the right to call myself healer where I have been knife."

The roots around her ankles turned red-gold.

They did not die.

They changed direction.

They grew backward along the Lumenorath bridge, carrying Aurenne's forbidden line through the hymn roots, through the white-root lanterns above, through the wagons and ranks and frightened soldiers waiting under bridge law. Voices rose from above as the line reached them. Some in denial. Some in anger. Some in sobbing recognition.

Serathiel looked suddenly older.

"I loved you," he said.

Saelith stood. "You loved the shape I made when I obeyed."

"I saved you from a world that would have used your mercy."

"You used it first."

The chamber went silent.

Even Vorrakai's grief seemed to listen.

Serathiel's face did not twist. That would have been too honest. Instead it became perfect. Tranquil. Terrible.

"Then you are no longer Pale Bough."

Saelith reached to her shoulder and removed the last white thread of her old rank. It had been hidden under her travel-worn cloak, not because she cherished it, Mara thought, but because endings sometimes needed the object they ended. She held it up. The thread caught the dragon-moon light and shone.

Then she tied it around the red fungal bell.

"No," she said. "I am Pale Bough corrected."

The phrase struck the chamber like a bell.

Liora stepped forward.

"Pale Bough corrected," she said, trembling.

The young scout with shaking hands repeated it. Then the older standard-bearer. Then, impossibly, one of Serathiel's own officers, a woman with silver rings in her ears and tears on her cheeks.

"Pale Bough corrected."

Serathiel raised his hand.

The roots above him gathered into a spear of white light.

Caldus moved, but Mara caught his sleeve.

Saelith saw the spear form. She did not move away.

"If you strike me," she said, "let them see the law you kept under the hymn."

Serathiel's hand shook.

For the first time, Mara saw him hesitate not because he doubted himself, but because witnesses had made the cost visible. He could still do it. He could call it sorrow. He could say the fallen healer left him no choice. He could turn Saelith into proof.

But everyone would see him choosing.

The spear dissolved.

Kesh released a breath. "I am adding 'watched a doctrine trip over public accountability' to today's accomplishments."

Tavi wiped her eyes angrily. "Do not ruin this."

"I am improving it with accuracy."

Saelith returned to the dais.

She did not come to Mara first. Mara noticed and understood. Saelith went to Edrin and Sava, then to the Orrowen citizens gathered along the chamber bridge. She bowed, not as priest to patient, not as purifier to unclean dead, but as one person acknowledging another before asking to stand in their room.

"I harmed your names by believing fear made me gentle," she said. "I cannot repair what was done through me today. I can stand where correction costs me."

Sava considered her.

"Accepted provisionally," the clerk said.

Kesh blinked. "That was almost warm."

"Do not spread rumors."

The black page on the dais unfolded further.

Where the Lumenorath song had pressed it shut, Saelith's correction opened a seam. The memory changed. The chamber showed light-elf healers who had argued against cleansing and been edited into saints after death. It showed children in white orchards taught to fear the dark beneath their feet. It showed Serathiel young, standing beside a fever bed, weeping when a dead Orrowen witness would not stop repeating a child's last word. It showed the first time he chose to silence a witness and called the silence peace.

Serathiel turned away.

Mara almost pitied him.

Almost.

Pity could become another path to making him central. Saelith had paid too much for that.

Vaura seized the silence. "The record now shows Lumenorath coercion. Khar Veyl moves to secure the chamber pending review."

Maelin laughed again, sharper this time. "Mother."

Vaura's mouth tightened.

"You cannot hear someone else confess and mistake it for your acquittal," Maelin said.

Ilyr placed a second black page on the dais.

His hands shook.

"She is right," he said. "Lumenorath's beautiful law is not the whole crime."

Vaura's wardens shifted.

The blade-scholar's voice echoed faintly from above, still arguing with the riverbed. "Stop him!"

No one on the platform moved at first.

Then one of Vaura's wardens drew a knife.

Caldus knocked it from his hand with the flat of his sword so fast the man looked personally offended by physics.

"Bridge law," Caldus said.

"You are not bridge authority."

Brakka, pale with vow-light, opened one eye. "He borrows."

Caldus inclined his head. "Temporarily."

Tavi leaned toward Kesh. "Do we get badges for that?"

"I already stole us three."

"Of course you did."

Ilyr looked at the page as if it were a cliff.

Maelin took his hand.

"Open it," she said.

"It will burn your house."

"Then we stop living in its smoke."

He looked at Mara next, and that surprised her.

Not because he needed permission. Because he wanted witness.

Mara nodded once.

Ilyr opened the second page.
""",
    27: r"""## Chapter 27: Ilyr Opens the Record

The second page did not unfold into light.

It unfolded into a room.

Mara stood suddenly inside it, though her feet remained on the dragon-moon platform. The chamber had pulled everyone into witness at once: Serathiel, Vaura, Saelith, Maelin, Tavi, Kesh, Caldus, Brakka, Edrin, Sava, Orrowen citizens, Pale Bough officers, Khar Veyl wardens, even the Choir singers with their peaceful eyes. They all stood in the memory room together and watched the past realize it had run out of locked doors.

The room belonged to Khar Veyl before the city learned to polish its guilt.

Black stone. Low lamps. A table carved with nine house seals. At its center lay a strip of dragon scale, pale as moonbone, written in three hands. Light-elf healing script. Dark-elf emergency law. Orrowen civic seal.

The preliminary covenant.

Not the excerpt Maelin had seen in the drowned archive.

The whole first page.

A light-elf healer stood on one side of the table, her white sleeves rolled to the elbow, hands stained with ash. Beside her stood a dark-elf judge wearing the Noct-Vey seal. Across from them, an Orrowen civic minister with silver writing in her skin read every line aloud before allowing any mark to be made.

"Emergency custody of dragon remains," the minister read. "Temporary."

The dark-elf judge nodded. "Until seal stability is confirmed."

"Witness rights preserved."

"Yes."

"Dead citizens retain standing."

"Yes."

"No civic memory to be commanded for military, spiritual, commercial, dynastic, or doctrinal purpose."

The light-elf healer hesitated.

The Orrowen minister looked up.

"No purpose," the minister repeated.

The healer closed her eyes. "No purpose."

The covenant burned blue.

True.

Mara felt the platform under the memory answer. Every person watching understood at once what the later records had tried to blur: the first agreement had not failed because no one knew better. It had failed after people promised correctly and then found reasons to inherit exceptions.

The memory shifted.

Same table. Later year. Fewer Orrowen ministers. More elven officials. A gnome engineer with oil on her collar. A human royal envoy with Ashgate coal dust under his nails. A goblin route keeper standing near the door because no one had given him a chair and he had stolen one anyway.

"The dead civic rolls are excessive," said a light-elf officer. "They slow healing protocols."

"The rolls are people," said the goblin route keeper.

"They are dead."

"You say that like it makes them lighter."

The dark-elf judge, a younger Noct-Vey than the first, signed an amendment. "Temporary indexing. Names preserved in sealed custody."

Blue fire did not answer.

It flickered green.

Omission.

Ilyr made a small sound in the present.

Mara looked at him. His face had gone bloodless.

"That seal," Maelin whispered. "Our house."

"My training seal was patterned from it," Ilyr said. "They taught us it was a preservation mark."

The memory shifted again.

Harrowmere this time, though older than Mara had known it. Human ministers bought ash rights. Khar Veyl brokers sold access to names that could stabilize cinder furnaces. Lumenorath priests accepted purified extracts, labeled as grief-soot, for healing rites. Gnome guilds requested regulator samples. Goblin routes carried refugees and contraband records in the same sacks. Troll bridge disputes were reclassified as obstruction to emergency continuity.

Every people entered.

No people clean.

That was the chamber's cruelty and mercy both. It did not make guilt symmetrical. It made it specific.

Mara saw a human king sign for Orrowen ash while workers in cities like Ashgate were told fuel shortages required sacrifice. She saw Lumenorath heal a plague with memory distilled from dead citizens whose standing had been suspended. She saw Khar Veyl houses argue that selling curated memory to human courts kept worse buyers away, and then grow rich enough to forget the excuse. She saw gnome engineers invent limiters, then bypass them when rulers demanded more. She saw goblin caravans smuggle children out one gate and sell maps to soldiers at the next because routes had to stay open and hunger was a persuasive clerk.

Kesh did not look away.

Neither did Tavi.

Neither did Saelith, though tears tracked down her face.

Mara wanted to look away for all of them.

The chamber would not let her.

The record found Ilyr next.

Not his ancestors. Him.

Young Ilyr in Khar Veyl's private archive, elegant, bored, frightened under the boredom. He discovered a drawer of names classified as depreciated assets and understood enough to close it quietly. Later, Harrowmere. Ilyr selling under-script access to a minister who wanted dead names for furnace discipline. Ilyr telling himself he had altered the sale, removed the most vulnerable names, kept the worst harms from worse hands. Ilyr drinking afterward in a room full of mirrors, unable to look at any of them.

He trembled.

"Ilyr," Maelin said.

"No." He lifted one hand without looking away. "Let it stand."

The memory showed him again: returning to the archive years later, stealing copies, hiding them, not using them because using them would make him accountable to everyone he had failed before becoming useful.

Vaura's voice cut through the memory. "Enough. The witness has confessed. The rest is private house matter."

The chamber went cold.

Mara felt the dragon-moon's closed eye move beneath them.

Maelin turned on her mother.

"Private?" she said.

Vaura's face hardened into the ruler before Mara's eyes. "Do not mistake necessary exposure for permission to tear open every support beam while enemies stand in the room."

"The room is made from what you called support beams."

"Khar Veyl falls if every seal is invalidated at once."

"Then perhaps Khar Veyl should learn to stand on something other than sealed throats."

One of Vaura's wardens grabbed Maelin's arm.

Ilyr moved first.

He did not use a knife. He took the warden's wrist and pressed it to the glowing page.

The record opened the man.

Not physically. Worse. It showed the warden signing retention papers for Maelin when she was thirteen, not because he hated her, but because Vaura's office had told him the girl was too valuable, too unstable, too necessary to leave unbound. It showed him looking away while Maelin screamed once and then learned not to waste sound.

The warden released her as if burned.

Maelin stared at him. "You remembered."

He could not answer.

Vaura's seal rod cracked.

For a moment Mara thought Vaura would strike her own daughter, not because she wanted to, but because some rulers could only understand love as a thing defended by control. Instead Vaura looked at Maelin's exposed scars, then at the record, then at the dragon-moon horizon below.

"I kept you alive," Vaura said.

Maelin's face twisted. "Yes."

The answer hurt more than denial would have.

"And chained," Maelin said. "Both can be true. That is the part you keep trying to seal."

The chamber burned blue.

True.

Serathiel stepped into the memory light, perhaps to use the fracture, perhaps because he could not bear guilt that did not arrange itself conveniently around Khar Veyl. "Dark courts sold names. Human kings burned them. Gnome engines refined them. Lumenorath alone sought release."

Saelith's voice was hoarse. "Read the next page."

He looked at her.

"Saelith."

"Read it."

Ilyr did.

The next page unfolded into a Lumenorath hall. White boughs overhead. Serathiel younger, not yet serene. A council of healers arguing over the unquiet dead. At the center lay a report from Khar Veyl warning that cleansing rites destabilized the dragon-moon seal. In the margin, a light-elf hand had written: If the dead can be purified into rest, standing becomes unnecessary.

The note belonged to Serathiel.

He did not deny it.

The memory showed him at a bedside, as Saelith's earlier vision had, silencing a witness who repeated a child's last word. Then another. Then an archive of such silences, each justified by mercy, each recorded as release, each release feeding the doctrine that the dead should be quiet and the living should be grateful.

"They were suffering," Serathiel said.

Sava Rennet's voice cut like a page edge. "Did they choose silence?"

"They could not choose through pain."

"So you chose for them."

"Yes," he said, and the word rang with terrible honesty. "And I would again."

The chamber flashed blue.

True.

That truth did not absolve him. It made the danger cleaner. Serathiel believed what he had done was mercy. He would not be unmasked as a secret cynic. He was worse: a faithful man whose faith had made other people's consent optional.

The Choir singers began to hum.

Very softly.

Tavi noticed. "Do not."

One of them smiled at her. "Every record is a wound."

"Some wounds need air," Tavi snapped.

The singer touched the broken Glass Engine mark on the platform. "Air also feeds fire."

Below them, the dragon-moon eye shifted again under its lid.

The record light grew unstable.

Ilyr staggered. Opening the pages was costing him. Mara could see it now: each record pulling through his body because he had been one of the people who hid it, sold it, altered it, survived it. The chamber required no clean witness, but it demanded that unclean witnesses stop pretending the dirt was only on their boots.

"Enough," Mara said. "You can stop."

Ilyr laughed once, broken. "Can I?"

"Yes."

"That is kind. Also false."

He turned to the platform, to the armies above echoing through bridge law, to Orrowen's gathered citizens, to the people he had harmed and the courts that had trained him.

"Ilyr Noct-Vey," he said. "Former archivist. Broker. Liar by elegance, coward by delay, witness by correction if the harmed permit it."

Sava lifted her stamp. "Statement entered."

"I open the full record."

Vaura inhaled sharply. Serathiel raised a hand. The Choir's hum grew teeth.

Ilyr pressed both palms to the dais.

Every black page opened.

The chamber became a world made of records.

Names streamed upward from the dragon-moon horizon. Orrowen dead. Human ash-workers. Light-elf healers edited from doctrine. Dark-elf clerks ordered to seal what rulers feared. Gnome apprentices buried by regulators. Goblin children carried through illegal roads. Troll bridge-keepers classified as obstruction until their bridges were needed. Dragons whose cinders had been numbered by people too small to understand what they had made countable.

The armies above saw it. Bridge law carried the record into every held rank. Soldiers dropped weapons. Some from guilt. Some from horror. Some because the spear in their hand suddenly had a history too heavy to lift.

Mara saw Ashgate in the stream and nearly broke.

Not just the furnaces. The ledgers. The little decisions. A foreman changing one tally because a worker's daughter was sick. A minister ordering quotas rounded down because dead runners could be replaced cheaply. Kell hiding soap in flour sacks. Joryn refusing an easy promotion because it required choosing which children went to the lower vents. None of it clean. None of it abstract.

Truth frees no one until someone survives hearing it.

The chamber's earlier sentence returned, not as proclamation but as warning.

Ilyr collapsed.

Maelin caught him before he hit the dais.

The record kept opening.

Serathiel screamed.

Not in fear. In refusal.

White roots erupted from his bridge and stabbed into the streaming names, trying to burn away pain before pain could become accusation. Vaura's wardens raised seal rods to contain the flood. The Choir's song rose, offering stillness to everyone drowning in memory. The three answers came at once: cleanse, seal, end.

The chamber shook.

The dragon-moon eye opened the width of a blade.

Mara fell to one knee.

Every cinder in Vael Taryn answered in her blood.

She heard furnaces above, hearths, engines, charms, crown jewels, hidden bones, lamps, swords, roads, grave ash, every dead dragon memory waking enough to ask who had been using it.

Tavi threw herself at the regulator dais that had risen beside the platform, all brass gears and screaming glass birds. "There it is," she shouted. "Command function. If someone turns that, they can force the dead record into one channel."

"Can it stop the chamber from breaking?" Caldus asked.

Tavi's face went white.

"Yes."

The word was awful.

"Can it win the battle?" Kesh asked.

"Yes."

"Can it do that without enslaving every dead witness currently screaming through the room?"

Tavi looked at the dais.

The gears opened for her like a flower made of knives.

"No," she said.

The next choice arrived exactly where the world loved putting terrible choices: in the hands of someone good enough to hate using it.

Tavi climbed onto the command engine.
""",
}


DEEPENING: dict[int, str] = {
    25: r"""The first black page did not accuse.

It counted.

That was worse, somehow. Accusation could be argued with, dodged, discredited, turned into a matter of tone. Counting simply continued. The page unrolled names in measured light, each one entering the chamber with a sound like a footstep crossing a bridge.

Rola Fen.

Berrit of Canal Nine.

Sesh Anvar.

Nim of south laundries.

Ruv Ossian.

Leth of West Quay.

Then names Mara did not know, too many and too specific to become a crowd. Orrowen ministers, gnome engineers, dark-elf copyists, light-elf healers, human furnace carriers, goblin route-menders, troll oath-witnesses, dragon names that were less words than weather breaking against thought. The chamber accepted every name by making room for it. The platform widened. The bridges strengthened. The dragon-moon's closed lid trembled as if sleep had become a place full of knocks.

Serathiel's expression flickered with pain before he mastered it.

Vaura's fingers tightened on the cracked seal rod.

Mara knew, with the miserable certainty of cinder-sense, that both of them could endure a thousand nameless dead more easily than ten named ones. A thousand became policy. Ten became people who might ask why the powerful kept arriving late with beautiful explanations.

Kesh stood very still through the counting.

When one name appeared in goblin road-script, he sucked in a breath.

"Kavik?" Mara asked softly.

"My aunt," he said. "Officially she died of poor route discipline. Unofficially she carried three Orrowen children through a fever checkpoint and sold the checkpoint map afterward to pay for medicine."

"Both true?"

"Both true." His mouth twisted. "Families are rude that way."

Tavi listened to the gnome names with her eyes shut. Every few breaths her fingers moved as if tightening screws that were no longer there. Caldus bowed his head for the human names and did not try to separate the soldiers from the workers. Saelith whispered Matriarch Aurenne's forbidden line every time a light-elf healer appeared, not as prayer now, but as apology with teeth.

The counting went on until the chamber had made its first point.

No policy had ever acted on a category.

Only on persons forced into one.""",
    26: r"""Saelith's correction did not end the danger of Lumenorath.

It made the danger visible.

Above, through bridge law, the Pale Bough ranks split not into clean halves but into human confusion. Some soldiers knelt and repeated the corrected phrase. Some shouted that Saelith had been poisoned by dead law. Some looked to Serathiel and then to the red-gold line burning through their own roots, discovering that obedience became harder when the root under it was older than the command.

Liora, the shaved-headed scout, asked Saelith, "What do we do if we are wrong?"

The question carried through the chamber.

Serathiel looked almost relieved, as if doubt were a wandering child he could take by the hand and lead home. "You return to the law. That is why it exists."

Saelith shook her head. "No. We return to the person in front of us."

"And if the person lies?"

"Then we answer the lie. We do not erase the person to simplify the answer."

Liora swallowed. "And if we have already erased?"

Saelith's face changed. Mara saw the old wound open, not as spectacle, but as office: the cost Saelith would have to keep paying because public renunciation did not undo private harm.

"Then we spend the rest of our lives making it harder for anyone to praise us for it."

No one cheered.

That was right. Cheering would have made it too easy.

Instead, one Pale Bough officer unfastened the white thread at her shoulder and tied it around her wrist where it could not pretend to be rank. Another lowered his spear. A third did neither, but stopped singing. Small acts, partial, frightened, insufficient. Saelith watched them all and did not demand they become a revolution quickly enough to comfort her.

Mara felt affection rise in her so fiercely it almost knocked her sideways.

Saelith had broken a beautiful law and refused to replace it with a beautiful lie.

That, too, was a kind of heroism songs usually missed because it did not shine. It simply made the next command harder to obey.""",
    27: r"""Mara reached for Ilyr as Maelin held him against the dais.

He was shaking so hard his teeth clicked. The full record streamed around them, naming its way through the chamber, and every name that had passed through his hands cut him on the way out. Maelin had one arm around his shoulders and the other pressed to the page, refusing to let the record take him alone.

"Breathe," Mara said.

Ilyr laughed without air. "Elven elegance has failed. Instructions unclear."

"That is Kesh's line."

"He invoices."

Kesh, pale and bleeding from a cut no one had noticed him receive, appeared on the other side of the dais. "I do, actually."

The absurdity made Ilyr draw one broken breath.

Maelin looked at Mara over his bowed head. "If he dies for this, I will be impossible."

"You already are."

"More."

Mara believed her.

The record light softened around Ilyr, not because it forgave him, but because Maelin had made the cost shared by choice. That mattered. The chamber was learning them as they learned it. Not clean, not safe, but responsive to the difference between sacrifice demanded and burden chosen.

Sava stamped the dais beside Ilyr's hand.

WITNESS ALIVE, COST CONTESTED.

Ilyr coughed. "That is the kindest thing a document has ever said about me."

"Do not become sentimental," Sava said. "It weakens margins."

The command engine screamed behind them.

Tavi had reached its first ring.""",
}


FINAL_DEEPENING: dict[int, str] = {
    25: r"""The chamber required witnesses from every bridge.

It did not announce this in any language. It simply refused to let the records continue until each lit causeway had weight upon it. When only Mara's company stood near the dais, the black pages dimmed. When Serathiel's officers remained clustered behind him, their bridge went pale. When Vaura's wardens kept one foot angled toward retreat, the Khar Veyl seal marks smoked with contempt so precise that even Kesh looked impressed.

"I believe the room is judging our attendance," he said.

Assistant Registrar Othel adjusted his empty spectacles. "Chambers of final civic review often do."

"You say that as if there are several."

"Standards matter most when examples are scarce."

Sava pointed to the bridges. "Each authority that claims the moon must stand where the moon can answer."

No one liked that.

Which meant, Mara thought, that it was probably correct.

The witnesses took their bridges slowly. Liora and the older standard-bearer stood on the Lumenorath span with Saelith, not beside Serathiel. That mattered. The white roots beneath their feet shivered at the insult and the possibility. On the Khar Veyl span, Velra of the lower canals shoved past a noble warden who tried to tell her the first position belonged to house authority.

"My pumps flooded for your house seals," Velra said. "My boots get the front."

Vaura opened her mouth, then closed it. The chamber recorded that too.

On the gnome bridge, Tavi stood alone at first. Then, from one of the opened side galleries, three gnome engine-ghosts emerged carrying cracked measuring rods. They wore old guild aprons and expressions of acute embarrassment. Tavi stared at them.

"You are kidding," she said.

One ghost bowed. "We filed objections after death."

"That is a little late."

"Yes."

"Infuriating."

"Also yes."

Tavi looked away, furious and moved despite herself. "Stand there and do not touch anything."

"That was our objection, broadly."

On the goblin route bridge, Kesh tried to stand with his usual air of having arrived by accident and found the silverware vulnerable. Then the bridge produced more witnesses: route beads, road names, a memory of his aunt laughing with a stolen chair under one arm, three ghostly children holding fever passes. Kesh's face shut down.

"Oh, don't," he told the bridge.

The bridge did.

It placed at his feet a little brass route token pierced with red thread, the twin of the one he had left at the crossing shrine.

Mara watched him bend to pick it up and fail to make a joke.

Brakka stood on the troll bridge with Caldus because bridge law had borrowed him and because Caldus, to his credit, did not pretend to understand the honor fully. He stood with his wounded arm bound, sword point down, looking less like a knight than a man who had learned that holding a line was not the same as owning it.

The human bridge troubled Mara most.

It lit last.

No king appeared. No minister. No royal envoy brave enough to take responsibility even as memory. Instead the bridge filled with small signs: Ashgate tally sticks, furnace tags, broken lunch tins, a child's slate, a strip of Kell's washcloth, Joryn's old boot nail, the kind with a bent head he used to keep in his pocket because replacing nails cost less than replacing boots and still more than people liked.

Mara stood there because no one else could.

The chamber did not call her queen, saint, or champion.

It wrote: WORKER WITNESS.

Her eyes burned.

Saelith saw the words from across the dais. Caldus saw. Kesh saw and pretended to be studying a chain. Tavi saw and nodded once as if the chamber had finally produced an accurate label.

Mara put one hand on the human bridge rail.

"Ashgate appears," she said.

The furnace tags rang like little bells.

Then the dragon bridge lit.

No one stood on it.

No one could.

It arched from the central platform into open air and ended above the pale curve of the dragon-moon, unfinished, broken, or waiting. Its surface was made of black scale veined with red fire. Names moved beneath it too large for language. The first step burned with a question the chamber did not translate.

Vorrakai's grief touched the platform.

Mara felt every witness turn toward the dragon bridge.

The Choir singers smiled.

"No," Mara said before anyone could ask her to cross it.

Serathiel looked at her. "Afraid?"

"Yes."

The chamber flared blue.

True.

Mara let the truth stand. "And not stupid enough to mistake fear for an answer. The dragon bridge waits until the dead dragon is not being used as proof by people who just discovered they had to stand in the room."

For once, no one replied quickly.

The black page resumed opening.

Around the chamber, every bridge now held not armies, not races, not arguments, but witnesses particular enough to be inconvenient. The platform steadied. The enormous chains above them stopped groaning. The dragon-moon's closed eye settled beneath its lid.

Mara understood with a shiver that this was not safety.

It was attention properly distributed.

Power concentrated had made the prison. Witness shared might keep it from becoming a grave or a throne.

For a few breaths, the chamber held that impossible shape.""",
    26: r"""Before Saelith spoke again, the chamber gave her the memory she had avoided.

It was not dramatic. That made it cruel.

A small room in Lumenorath. White walls. A basin. Saelith at fifteen, hair cut blunt at her jaw, sleeves rolled high, hands trembling over an Orrowen witness bound in silver root. The witness had been a man once, perhaps a baker, perhaps a canal clerk. His name had been removed from the lesson because names distracted novices from principle. He repeated the same phrase again and again: Tell Vara I closed the west gate.

Young Saelith looked at her teacher. Not Serathiel then. A woman with kind eyes and a voice like warm bread.

"He is suffering," the teacher said.

"Can we find Vara?" young Saelith asked.

The teacher's face softened with such pity that the child Saelith flushed, ashamed of the wrong question. "Mercy does not chase every echo. Mercy releases."

Young Saelith placed her hands over the man's mouth and sang.

The witness went quiet.

The memory did not show whether Vara ever learned the west gate had closed.

Present Saelith made a sound that almost tore free of her.

Serathiel saw the memory and used it. "You gave peace."

"I stole a message," Saelith said.

"You were a child."

"Yes." She looked at him with such naked grief that even Serathiel's roots stilled. "Who taught the child what praise would cost?"

The question moved through the Lumenorath bridge and into the army above. Mara felt it pass through soldiers who had been praised for clean hands after dirty orders, through healers who had been told a quiet patient meant success, through priests who had inherited songs so beautiful they had never asked what the songs interrupted.

Liora sank to her knees.

"I did it too," she said. "At White Orchard. We cleansed three dead scouts from the old road. One kept saying a name. I thought it was corruption."

Saelith knelt in front of her.

"What name?"

Liora shook her head, weeping. "I do not remember."

"Then that is where correction begins."

"How?"

Saelith looked toward Sava.

The clerk's face remained stern, but her voice was gentler than the face admitted. "You file the absence. You do not fill it with invention because guilt wants a quick repair. You record that a name was taken and that you failed to preserve it. Then you search."

Liora pressed both hands over her mouth.

Serathiel's voice lowered. "You would bury them in guilt."

Mara answered before Saelith could. "No. You buried them in quiet."

His eyes cut to her. "And you, ash-runner, would have every wound opened?"

"No." Mara thought of Joryn, of Arveth, of the furnace, of Saelith's shaking hands. "I would stop calling closed wounds healed just because they are easier to look at."

The chamber did not flare blue.

Not because the statement was false.

Because it was not complete.

Mara felt that and corrected herself.

"And I would let people choose when to open their own, whenever choice is still possible."

Blue.

True.

Saelith rose with Liora beside her. "Pale Bough corrected does not mean Pale Bough pure. It does not make us innocent because we changed a phrase. It means every song is answerable to the person it touches. It means no healer may call silence success until consent stands beside it. It means we do not cut memory out to make doctrine graceful."

The red-gold roots carried the words upward.

Above, through bridge law, the old battlefield shifted. White-root lanterns lost their flat glare and became individual lights, each held by a frightened person. Some went dark. Some burned red-gold. Some stayed white and shaking, unwilling to change and unable to pretend nothing had happened.

Serathiel watched his order become plural.

That, Mara realized, wounded him more deeply than accusation. He could survive being hated as a necessary savior. He did not know how to survive being one voice among many people who could still choose.

"You will splinter them," he said.

Saelith's mouth trembled. "They were already splintered. You called the pressure unity."

The chamber lit blue.

True.

Serathiel closed his hand.

Somewhere high above, one hymn wagon cracked from root to wheel.""",
    27: r"""The full record did not arrive in order.

History rarely did. It came like floodwater through streets, lifting what had been hidden under beds and behind walls, carrying silver cups beside bones, lullabies beside orders, ledgers beside children's drawings. The chamber showed covenant, amendment, theft, mercy, sale, panic, hunger, strategy, cowardice. It refused to arrange them into a clean ladder of blame.

Mara saw a light-elf healer smuggling Orrowen witness names out of a cleansing house, then saw that same healer later authorize silence for a dead child because she was too exhausted to hear one more last word. She saw a dark-elf archivist preserve a civic roll under her floorboards, then sell a duplicate to a human furnace office to buy protection for her sister. She saw a gnome apprentice sabotage a regulator, killing three soldiers and saving a district. She saw a goblin road captain sell the same route to refugees and raiders in the same week, then die holding the raiders at the wrong bridge so the refugees had time to flee. She saw humans in Ashgate pray over cinder furnaces and then feed them because children needed heat and rulers had made every other choice expensive.

No clean people.

No empty categories.

No excuse broad enough to cover the next decision.

That was the record's true violence. It did not allow anyone to become innocent by comparison.

Vaura lowered her cracked seal rod.

For a moment Mara thought she had yielded. Then Vaura spoke, and her voice carried the ruin and stubbornness of Khar Veyl together.

"Khar Veyl enters culpability."

The wardens behind her stared.

"Mother," Maelin said softly.

Vaura did not look at her. If she had, perhaps she could not have finished.

"House Noct-Vey enters culpability for emergency custody extended beyond mandate, retention of civic names, sale of curated memory, unauthorized standing suspension, bloodline retention practices, and use of provisional protection to delay public review."

Each phrase struck her like a thrown stone. Mara saw it in the ruler's shoulders, in the white pressure around her mouth. Vaura was not making herself good. She was making retreat harder.

The chamber burned blue.

True.

The blade-scholar's voice echoed from above, furious. "You betray the under-realm!"

Velra of the lower canals shouted back through the bridge law, "You tried to abandon half of it behind pumps!"

Kesh looked delighted. "I adore her."

Vaura continued, louder now. "Khar Veyl does not surrender seal defense. It surrenders sole claim to seal authority."

The distinction mattered. The chamber accepted it in green.

Incomplete, but no longer hidden.

Serathiel watched Vaura with something like contempt and envy. Confession from an enemy could be dismissed. Confession from a mirror made the room smaller.

Saelith turned to him.

"Enter Lumenorath culpability."

"I will not condemn mercy because you have learned new language for shame."

"Then enter what you did and let the chamber judge mercy for itself."

His face hardened.

The full record moved behind him, showing white halls, quieted witnesses, cleansed names, corrected doctrines uncorrected again by later hands. Pale Bough officers watched their own history pass through the air. Some wept. Some denied. One began to sing and stopped when Liora took his hand.

Serathiel raised his chin. "Lumenorath enters no guilt for seeking rest."

The chamber did not flare.

It waited.

Mara understood the danger of that waiting. Serathiel had not lied exactly. He had sought rest. But truth narrowed around omission could still become a knife.

Saelith stepped onto his bridge.

Everyone saw what it cost her. Her hands shook. The roots under her boots were half white, half red-gold, unsure whether to welcome or cut.

"Then I enter what I carried for you," she said.

Serathiel's serene mask cracked.

"Saelith."

"Lumenorath enters culpability for cleansing without consent, for turning suffering into uncleanness, for editing Matriarch Aurenne, for teaching children to call silence mercy, for using the dead as proof that the living should obey, for loving beauty more than persons when beauty and persons could not both be kept."

The chamber burned blue.

True.

The white roots around Serathiel blackened at the tips.

He looked at her then not as disobedient student, not as fallen healer, but as someone who had become capable of harming him with the truth because he had failed to make her less real than doctrine.

"You were my daughter in mercy," he said.

Saelith's tears spilled. "Then you should have wanted me alive enough to disagree."

Mara wanted to go to her. She stayed where she was because Saelith was standing.

Ilyr, still shaking in Maelin's arms, laughed once.

Mara looked at him.

"What?"

"We are all very bad at being saved by people who love us."

Maelin held him tighter. "Speak for yourself."

"I was."

"Obviously."

That small exchange, absurd and wounded, steadied the dais more than any seal rod could have. Mara felt the chamber learn again: people were not only what had been done to them, or what they had done. They were also this, the ridiculous insistence on answering despair with correction, annoyance, hand on shoulder, breath dragged back into a failing body.

Then Tavi shouted from the command engine, "I need everyone to stop having devastating personal revelations for twelve seconds!"

No one did.

But they did look at her.

She was halfway inside the brass mechanism now, one boot braced on a gear tooth, hair full of sparks, face streaked with grease and tears. The engine's rings had unfolded around her like a predatory flower. Each ring bore a command path: dead civic rolls to army discipline, Orrowen witness stream to seal reinforcement, dragon-moon resonance to battlefield obedience.

"This thing is a moral disaster with excellent load distribution," she said.

"Can you disable it?" Caldus called.

"Yes."

"Can you keep the chamber from breaking while doing that?"

Tavi looked down at the dragon-moon's half-opening eye.

For once, she did not answer quickly.

"Maybe," she said.

Master Quen's cracked voice drifted from the engine through an old speaking tube. Mara had not seen where the gnome had gone after the Glass Engine, but some part of her, memory or echo or living woman dragged by her own invention, remained in the machinery.

Apprentice Tavira. Command is the only path left that does not require faith.

Tavi's jaw clenched.

"That is why cowards love it," she said.

The engine screamed like birds again.

The next chapter's choice had arrived, brass-toothed and useful enough to damn them all.""",
}


EXTRA_DEEPENING: dict[int, str] = {
    25: r"""The chamber also made them wait.

That was perhaps its most radical demand. Every power in the room had arrived with emergency speed. Cleanse now. Seal now. Surrender now. Command now. Even Mara, who distrusted rulers' urgency, felt the animal panic of the dragon-moon below them and wanted some decisive act to make the next breath safer.

Instead the chamber dimmed all but the witness bridges and made the companies stand inside the consequences of being specific.

The waiting changed the room.

On the Lumenorath bridge, one of Serathiel's officers began to whisper the old cleansing response, then stopped when Liora looked at him. He did not apologize. He did not have the shape for it yet. But he stopped. On the Khar Veyl bridge, Velra forced Vaura's wardens to make space for two lower-canal clerks who had followed her down with wet boots and sharper memories. The wardens obeyed badly. The clerks entered anyway. On the gnome bridge, Tavi demanded the engine-ghosts identify themselves by name and not guild number. Two managed. One could not remember anything except the machine that killed her. Tavi wrote "name pending, person entered" on a scrap and pinned it to the ghost's apron.

Kesh watched that and swallowed.

"I hate when she makes compassion look like inventory," he said.

"You do not hate it," Mara said.

"No. But I resent being known accurately in public."

The human bridge gave Mara its own waiting. Ashgate signs trembled around her, not accusing exactly, but refusing to let her represent them as an uncomplicated victim people. She saw workers who protected one another. Workers who stole from one another. Mothers who lied to keep children from lower vents. Fathers who reported neighbors for double rations. Joryn breaking a man's nose for selling ash masks at flood prices. Kell hiding the broken-nosed man afterward because the city guard would have hanged him for less.

Mara's people had been used.

They had also survived by using what they could.

She wanted a cleaner inheritance and did not get one.

The chamber wrote beneath WORKER WITNESS:

NOT EMPTY. NOT PURE.

Mara let that stand.

Below, the dragon-moon waited with its eye closed, and every waitable second felt stolen from disaster. But in that held breath, the witnesses became less like armies and more like people who might be unable to obey quickly enough when someone ordered them to simplify the world again.""",
    26: r"""Serathiel tried one last gentleness.

He stepped down from the white-root bridge until only a pace separated him from Saelith. The roots made no weapon this time. His hands were empty. That frightened Mara because empty hands could still carry the old shape of a leash.

"You think correction will love you back," he said.

Saelith went very still.

"It will not," he continued. "These dead will accept your confession, stamp it, file it, and still remember what you did. Mara Venn will witness you and still not be able to make you sleep. Your new friends will need you, and their need will be less gentle than my law. Come home before you mistake endless debt for freedom."

Mara hated him most in that moment because he understood enough of the wound to press it precisely.

Saelith's eyes filled.

"You are right," she said.

Serathiel's face softened with victory too soon.

"Correction will not love me back," Saelith said. "The dead do not owe me comfort for naming what I helped do. Mara cannot make me sleep. My friends will need me and sometimes unfairly. Freedom will ask more of me than obedience ever did."

She took the white thread and red fungal bell in her hand.

"I choose that anyway."

The chamber turned blue from bridge to bridge.

True.

Serathiel's hand fell.

It was the first time Mara saw him look truly alone. Not hated. Not defeated. Alone in the way people become when they realize the cage they built for others had also been their house.

For half a breath, she thought he might choose differently.

Then the Choir hummed from the chamber's edge, and his loneliness found a softer prison.

Vorrakai's grief touched him.

Serathiel closed his eyes.

"Then I will save what remains," he said.

Saelith stepped back, shaking.

Mara took her hand this time. Not to choose for her. Because the choice had been made and the cost had arrived.

Saelith gripped back hard enough to hurt.""",
    27: r"""The record reached the armies above in uneven waves.

Bridge law carried it through the causeways, but people received truth according to the defenses they had built. Some Lumenorath soldiers heard Aurenne's omitted line and wept because it explained a discomfort they had buried under obedience. Some heard it and grew angrier, because anger was easier than grieving the years spent as someone else's clean hand. Some Khar Veyl wardens saw the private seals and immediately began calculating which records could still be protected, then looked down to find Orrowen ghost-water reflecting the calculation back at them in humiliating detail.

The blade-scholar finally stopped shouting.

That worried Kesh.

"I mistrust quiet zealots," he said.

Above, the blade-scholar knelt in the dry riverbed with both hands pressed to the mud. The record had shown him as a child in a lower war school, watching his older brother die because a Lumenorath purification patrol mistook a fever ward for a necromancer's cache. It showed him later using that grief to justify sealing canals with children still behind them. Both memories stood side by side, refusing to let cause excuse consequence.

He looked up, and for one heartbeat he seemed breakable.

Then he reached for a fallen seal spear.

"No," Kesh said, and was moving before Mara could ask how he had planned to stop a man two levels above them.

The goblin bridge answered him.

Route marks flared from Kesh's boots to the upper battlefield. He vanished from the chamber platform and reappeared on the causeway above in a shower of red road-script, stumbled, cursed with impressive variety, and kicked the spear out of the blade-scholar's hand.

"You do not get to turn tragic backstory into fresh murder while I am emotionally available," Kesh snapped.

The blade-scholar lunged.

Kesh ducked, slapped one of the stolen triage tags onto the man's chest, and shouted, "Noncombatant pending review!"

The tag flared green.

The blade-scholar froze in outrage so complete it became almost artistic.

Sava, watching through bridge law, stamped the air without hesitation.

TEMPORARILY ACCEPTED.

Kesh looked down through the connection at Mara. "I am a legal innovator."

"You are a menace," Tavi shouted from the engine.

"Categories overlap!"

The laughter that passed through the chamber was strained, frightened, and real. It kept the record from becoming only despair for three precious breaths.

Then the command engine opened its second ring, and all laughter ended.""",
}


LAST_DEEPENING: dict[int, str] = {
    27: r"""The engine's second ring did not offer itself to Tavi alone.

It offered itself to everyone who was afraid.

A vision opened above the brass teeth: the battlefield stabilized, armies frozen before the first illegal strike, Orrowen's dead arranged into neat witness ranks, Serathiel unable to cleanse, Vaura unable to seal, the Choir unable to sing. No blood on the crossing. No roots lashing toward Saelith. No seal spears. No collapsing chamber. The command engine could do what bridge law struggled to do with pain and argument. It could make everyone stop.

For one dazzling heartbeat, even Mara wanted it.

She saw the temptation move through the chamber. Caldus's wounded body leaned toward any tool that would spare the people behind him. Saelith looked at the white roots and imagined them unable to touch another frightened novice. Vaura saw Khar Veyl preserved from its hardliners. Serathiel saw an end to corruption without choosing which hand would burn. Orrowen citizens saw a court that could never again ask them to prove themselves because no one would ask anything. The Choir smiled because command and stillness were cousins under different banners.

Tavi saw all of that.

That was why her face broke.

"It would work," she said.

No one contradicted her.

The engine heard the silence and opened another petal.

Master Quen's voice came again, closer now, intimate with every gear. Working is not wicked. Failure kills too.

Tavi pressed both hands to the ring. Blood from a cut on her palm ran into the brass and made the engine purr. "You always did that."

Mara could barely hear her over the record storm.

Tavi spoke louder. "You always put the corpse beside the calculation. If the bridge fails, they die. If the engine fails, they die. If you refuse the useful horror, you own every death that follows. That was how you made cowardice look like rigor."

The gnome engine-ghosts bowed their heads.

One whispered, "We believed it."

"So did I," Tavi said.

She looked at Mara then. Not asking permission. Not even asking witness. Letting herself be seen at the exact moment usefulness reached for the loneliest part of her.

"If I destroy the command function," Tavi said, "the chamber may break."

"Yes," Mara said.

"If I use it, we win this hour."

"Yes."

"And lose everyone it touches."

Mara thought of Arveth's courthouse, of Vorrakai's kindness, of every system that had promised to spare people from choice by first taking away their mouths.

"Yes," she said.

Tavi nodded once.

"I hate honest answers."

Kesh, still linked through the goblin bridge above, called down, "We can return to lying after the apocalypse."

"No, we cannot," Sava said.

"Cruel day."

The engine's third ring opened, revealing the command spindle: a needle of cinder-glass pointed at the dragon-moon's closed eye. It was beautiful. It was precise. It was everything Tavi loved about machines and everything she had learned to distrust about people who wanted the world to behave.

Tavi climbed toward it.

The full record streamed around her like a storm of names.

Below, the eye watched through its lid.

Above, both armies waited for someone to make terror simple.

Tavi reached for the spindle with a wrench in one hand and grief in the other.""",
}


CODA_DEEPENING: dict[int, str] = {
    27: r"""Mara could not follow her onto the engine.

That was the shape of the lesson and the cruelty of it. The chamber had given every person a bridge, but not every bridge could be crossed by company. Mara had wanted, all her life, someone larger to step between her and the furnace door. Then she had become the person people looked toward, and discovered that heroism did not mean reaching every hand in time. Sometimes it meant staying close enough that the person choosing could still hear you breathing.

"Tavi," she called.

The gnome did not look down. "If you say anything inspiring, I will fall on purpose."

"I was going to say your left boot is on a loose gear."

Tavi glanced, shifted her weight, and swore. "Useful. Continue in that tradition."

Mara almost smiled.

The spindle rotated toward her cinder cage, hungry for the living witness-node Quen had named in the Glass Engine. Tavi saw it and slammed the wrench between two teeth, forcing the engine's attention back to herself.

"No," Tavi said. "You are not flirting with my friend while I am dismantling you."

The brass screamed.

Mara felt the cinder in her cage answer, then felt Saelith's hand close around hers, Caldus's presence at her shoulder, Brakka's bridge vow underfoot, Kesh's road-script somewhere above, Ilyr's ragged breath beside Maelin, Sava's stamp lifted and ready. The engine wanted one perfect conductor. It found instead an aggravating crowd.

For once, Mara let the crowd be enough.""",
}


FINAL_WORD_FLOOR: dict[int, str] = {
    27: r"""Above them, through the bridge-law link, the held armies felt the same thing.

Not inspiration. That would have been too clean.

They felt responsibility spread until it no longer fit inside a single girl, a single priest, a single ruler, a single machine. A Lumenorath medic picked up a dropped spear and moved it out of reach instead of using it. A Khar Veyl warden opened a casualty lane without waiting for Vaura's seal. An Orrowen child with a slate wrote TAVI IS ARGUING WITH A BAD ENGINE and held it up because accuracy was apparently contagious.

The chamber, absurdly, accepted the filing.

Tavi barked a laugh from inside the gears.

"Tell the child the engine objects to adjective placement."

Sava stamped the air. "Objection denied."

For three breaths, inside the terror, the room remembered how to be alive.""",
}


TINY_BUFFER: dict[int, str] = {
    27: r"""Mara held on to those three breaths.

Not because they solved anything. Because they proved the chamber was not only a place where ancient powers decided the fate of smaller lives. It could also hold interruption, correction, badly timed humor, frightened mercy, and a child making a sign about a gnome insulting a machine. The world Vorrakai wanted to still was unbearable.

It was also, stubbornly, not finished speaking.""",
}


SAFETY_BUFFER: dict[int, str] = {
    27: r"""Then the command spindle turned again.

All three breaths ended at once. The witness bridges tightened. The record storm leaned toward the engine. Tavi's wrench bent in her hand, and the cinder-glass needle aimed itself, not at the dragon-moon now, but at the gathered dead of Orrowen.

Winning, the engine suggested in brass and heat, could still be so easy.

Tavi smiled without humor.

"There it is," she said. "The sales pitch." """,
}


FINAL_MINIMUM_BUFFER: dict[int, str] = {
    27: r"""Mara felt the offer reach for her too: one more useful horror, one more excuse with excellent math. She set her feet on the human bridge and did not move.

"We hear you," she told the engine. "That is not the same as consent." """,
}


ABSOLUTE_FLOOR_BUFFER: dict[int, str] = {
    27: r"""The chamber stamped the sentence in blue fire, and the command engine screamed as if grammar itself had become sabotage.""",
}


TEN_WORD_BUFFER: dict[int, str] = {
    27: r"""Tavi lifted the wrench. The next answer would be hers.""",
}


def replace_chapters(text: str) -> str:
    pattern = re.compile(r"(?m)^## Chapter (\d+): .*$")
    matches = list(pattern.finditer(text))
    by_no = {int(m.group(1)): m for m in matches}
    for chapter_no in sorted(CHAPTERS.keys(), reverse=True):
        match = by_no[chapter_no]
        start = match.start()
        later = [m.start() for m in matches if m.start() > start]
        end = min(later) if later else len(text)
        replacement = CHAPTERS[chapter_no].strip()
        if chapter_no in DEEPENING:
            replacement += "\n\n" + DEEPENING[chapter_no].strip()
        if chapter_no in FINAL_DEEPENING:
            replacement += "\n\n" + FINAL_DEEPENING[chapter_no].strip()
        if chapter_no in EXTRA_DEEPENING:
            replacement += "\n\n" + EXTRA_DEEPENING[chapter_no].strip()
        if chapter_no in LAST_DEEPENING:
            replacement += "\n\n" + LAST_DEEPENING[chapter_no].strip()
        if chapter_no in CODA_DEEPENING:
            replacement += "\n\n" + CODA_DEEPENING[chapter_no].strip()
        if chapter_no in FINAL_WORD_FLOOR:
            replacement += "\n\n" + FINAL_WORD_FLOOR[chapter_no].strip()
        if chapter_no in TINY_BUFFER:
            replacement += "\n\n" + TINY_BUFFER[chapter_no].strip()
        if chapter_no in SAFETY_BUFFER:
            replacement += "\n\n" + SAFETY_BUFFER[chapter_no].strip()
        if chapter_no in FINAL_MINIMUM_BUFFER:
            replacement += "\n\n" + FINAL_MINIMUM_BUFFER[chapter_no].strip()
        if chapter_no in ABSOLUTE_FLOOR_BUFFER:
            replacement += "\n\n" + ABSOLUTE_FLOOR_BUFFER[chapter_no].strip()
        if chapter_no in TEN_WORD_BUFFER:
            replacement += "\n\n" + TEN_WORD_BUFFER[chapter_no].strip()
        text = text[:start] + replacement + "\n\n" + text[end:].lstrip()
        matches = list(pattern.finditer(text))
        by_no = {int(m.group(1)): m for m in matches}
    return text


def update_metadata(word_total: int) -> None:
    meta = METADATA.read_text(encoding="utf-8")
    meta = re.sub(r"produced_word_count: \d+", f"produced_word_count: {word_total}", meta)
    meta = re.sub(r"at_300_words_per_page: \d+", f"at_300_words_per_page: {round(word_total / 300)}", meta)
    meta = re.sub(r"at_275_words_per_page: \d+", f"at_275_words_per_page: {round(word_total / 275)}", meta)
    meta = re.sub(r"at_250_words_per_page: \d+", f"at_250_words_per_page: {round(word_total / 250)}", meta)
    meta = re.sub(
        r'current_form: ".*"',
        'current_form: "full-length draft zero with Book Two chapters 1-27 revised in pass 01"',
        meta,
    )
    METADATA.write_text(meta, encoding="utf-8")


def update_summary(word_total: int) -> None:
    if not SUMMARY.exists():
        return
    text = SUMMARY.read_text(encoding="utf-8")
    text = re.sub(
        r"\| The Moon Below the World \| `book-02-the-moon-below-the-world` \| [\d,]+ \| \d+-\d+ \|",
        f"| The Moon Below the World | `book-02-the-moon-below-the-world` | {word_total:,} | {round(word_total / 300)}-{round(word_total / 250)} |",
        text,
    )
    SUMMARY.write_text(text, encoding="utf-8")


def main() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")
    revised = replace_chapters(text)
    MANUSCRIPT.write_text(revised, encoding="utf-8")
    total = word_count(revised)
    update_metadata(total)
    update_summary(total)
    print(f"Book Two chapters 25-27 revised. Word count: {total}")


if __name__ == "__main__":
    main()
