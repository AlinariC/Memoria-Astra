#!/usr/bin/env python3
"""Revision pass 01g for Book One chapters 33-36.

Replaces the final stretch with bespoke prose: Caldus's human oath above the
furnace, the collapse of Mordane's last census-command, the dragon-heart's
series hook, and Mara's road-after-victory ending with back matter preserved.
"""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "output" / "book-01-the-ash-beneath-the-crown"
MANUSCRIPT = BOOK / "manuscript.md"
METADATA = BOOK / "metadata.yaml"
SUMMARY = ROOT / "output" / "README.md"


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


CHAPTERS: dict[int, str] = {
    33: r"""## Chapter 33: Caldus Keeps the Wrong Oath

When the hooks went dark, the Crown Court did not become peaceful.

Freedom did not know where to stand.

The dead rose from their knees, stumbled, stopped, touched their own throats, looked at painted hands, looked at living faces, looked at the open doors, the broken dais, the king on the floor, the citizens pressing through the south breach. Some began walking toward names called from the crowd. Some folded as if strings had been cut. Some stood so still that people swerved around them, afraid stillness might become violence.

The living were worse.

Harrowmere had spent years being told the dead in service were honored, preserved, blessed into usefulness beyond grief. Now those honored dead stood in front of them with hooks under torn collars and paint cracking from their cheeks. A baker tried to embrace a dead sister and recoiled when the body did not know how to answer. A noblewoman fainted into a pile of velvet. A heatworker fell to his knees before a woman he had once logged as Line Nine output and said her name until his voice broke. Three palace guards formed a ring around the king. Four formed a ring around the broken ledger because habit, like command, did not die instantly.

Caldus stood at the east gallery stair with his shield split nearly in half.

The split ran through the place where his crest had been scraped away.

Captain Veyr came down the stair with twelve royal knights behind him.

They were not Mordane's clerks or chapel guards or frightened young soldiers trying to make sense of a room that had betrayed their training. These were Crownreach knights, silver-collared, winter-cloaked, old names on their sword belts, faces set in the grim relief of men arriving late enough to believe clarity belonged to them.

Veyr saw Caldus and stopped.

"Renn."

The old name struck the stair like a gauntlet. Rakka Fen spat over the rail. Tesson Vair tightened his grip on a stolen spear. Joryn, leaning against the wall with one arm wrapped around his ribs, looked from Caldus to the knights and muttered, "Ah. Family argument with blades."

Caldus did not lift his sword. He had thrown it away below. He had a guard's baton in one hand now, dented and ugly, and the broken shield on his arm.

"Captain," he said.

Veyr looked past him at the dead, the citizens, Brakka's vow-stones, the king, the broken throne, the ash still rising from the undercroft stair.

"By royal emergency law, this court is sealed," Veyr said. "All unauthorized persons are to be removed. All continuation bodies are to be contained. All records are to be secured for crown review."

The words were not Mordane's. That made them more dangerous. They were the words of men who could look at a shattered crime and think first of jurisdiction.

Caldus shifted his shield. "No."

Veyr's face tightened. "You have no rank to refuse."

"You said that last time."

That landed. Veyr's eyes flicked once toward the chapel doors, as if the Ash-Marked Chapel lay behind them and not years in the past.

"Last time," Veyr said, "you broke formation and six prisoners vanished into city drains. Two were found dead within the week. One killed a guard. One was never accounted for. You turned a bad transport into a scandal and called it conscience."

Ilyr was not in the court to hear Maelin's ghost in those words. Maybe that was mercy. Maybe it was another delay.

Caldus felt the old wound open. Not shame alone. The worse thing: the part of Veyr's accusation that was true enough to bleed. His disobedience had saved some and failed others. His silence afterward had failed more.

"Yes," Caldus said.

Veyr blinked.

"Yes," Caldus repeated. "I acted late. Badly. Partly. Then I let disgrace become an excuse for doing little. You may put all of that in whatever report survives today."

"Stand aside."

"No."

The knights behind Veyr drew steel.

Brakka turned from the breach, eyes narrowing. Caldus lifted one hand without looking at her. Wait.

He had no right to command a troll oath-sister. She waited anyway, because wait was not command when spoken with trust and need.

Caldus stepped down one stair.

"You see disorder," he said. "I see people who were denied lawful answer. You see bodies to contain. I see citizens whose names were taken by systems we guarded. You see records to secure. I see evidence the crown has no right to hide from those it harmed."

"Pretty speech," Veyr said. "Still treason."

"No. Treason is betrayal of a crown. I am speaking of betrayal by one."

That sent a murmur through the court.

The king heard. He flinched as if struck. Caldus let him hear it.

Veyr raised his sword. "I will not let you hand this city to a mob and a herd of unbound dead."

Halea Voss turned her dead face toward him. "Herd."

One word. Dry, scholarly, lethal.

Veyr's sword point trembled.

Caldus stepped between the captain and Halea. "You will not call her that again."

"You draw a line for a corpse over your king?"

Caldus looked at the king. The old man had struggled to his feet with the aid of the split-lipped guard. Ash settled on his crown. He looked smaller under it than bareheaded men nearby.

"Majesty," Caldus said, "will you order these people contained without witness?"

The court froze.

The king stared at him. No adviser whispered. Mordane was ash. Serathiel was below or on the stair, her authority cracked. The horns, gods help them, still carried too much.

"I..." The king swallowed. "I must preserve order."

Veyr nodded once, satisfied.

Caldus closed his eyes.

There it was. The old oath waiting for him, wounded and familiar: preserve order, protect the crown, obey emergency law until inquiry can determine truth. It was not evil as written. That was why it had survived. It sounded like the thing honorable men should do when rooms burned.

He opened his eyes.

"No," he said.

Veyr's satisfaction vanished.

Caldus unbuckled the last remnant of his knightly collar. It was hidden under his stained coat, a strip of dark metal he had kept without admitting why. Not a crest. Not rank. A memory of belonging to something that had once made him feel clean.

He dropped it on the stair.

"I kept the wrong oath before because it was the only one anyone taught me to name. I will not keep it again."

Veyr moved.

So did Caldus.

The duel lasted less than a minute and did not look like justice. It looked like two tired men who had trained under the same masters trying to kill each other's conclusions. Veyr had the better sword, the better shoulder, the better armor. Caldus had a broken shield, a baton, and no remaining interest in looking like a knight. He fought low, ugly, practical. He took a cut across the thigh to get inside Veyr's reach. He slammed the broken shield into Veyr's wrist. He drove the baton under the captain's knee and brought him down hard on the stair.

The royal knights surged.

The split-lipped guard stepped in front of them.

Not alone. Tesson Vair joined him. Then two former prisoners. Then three soldiers who had hesitated earlier. Then Rakka Fen with a baton in each hand. Then Harl Brim, who should not have been standing and was therefore unbearable about it.

"Line holds for the living," the young guard said, voice shaking.

Caldus looked at him.

The words had come back changed, and therefore alive.

Veyr, on one knee, spat blood. "You have ended any chance of restoration."

Caldus leaned on the broken shield. Pain had turned his face gray. "Good."

"Good?"

"Now no one can mistake this for ambition."

The king spoke from the foot of the throne. "Caldus Renn."

Caldus turned.

For one wild heartbeat, the old shape offered itself: pardon, restoration, a place in a reformed court, a clean story in which the king had been deceived and the broken knight returned to serve properly. Caldus could almost see it. He could almost want it.

The king said, "What would you have me do?"

There was the trap again, softer than command. Power asking the wounded man to tell it how to be absolved.

Caldus looked at Mara's empty place by the undercroft stair. He looked at the dead standing in the court. He looked at the citizens waiting for a king to say something that might make the world simpler.

"Do not ask me to make you clean," he said. "Open the court. Open the records. Let the families in. Let the dead choose where they stand. Put down the crown until you know what it has covered."

The king's hand rose to the circlet on his head.

He did not remove it.

Not yet.

But he did not order the court sealed.

That was not triumph. It was a door unbarred a finger's width.

Below, from the undercroft, heat roared up, and all of them turned as the furnace gave back the names.""",
    34: r"""## Chapter 34: Mordane's Last Number

Mordane died before his system did.

That was the unfairness of systems. A person could fall into a furnace, a ledger could burn, a command coil could split, and still the habits built around them kept reaching for the old shape. Clerks gathered papers before they gathered wounded people. Captains asked who held authority. Chapel attendants tried to separate the dead into safe and unsafe rows. Nobles demanded escorts through the same shelter lanes they had tried to cut ahead of children. The palace kept trying to count.

The last number appeared on the dead horns.

No one knew who first saw it. Perhaps Tavi in the brazier network. Perhaps Othen at the lower valve board. Perhaps one of the clerks whose hands kept moving because terror looked too much like work. The number spread across black-glass plates and cinder gauges, writing itself wherever Mordane's census logic still had a surface.

1.

One necessary authority. One emergency command. One civic body. One acceptable sacrifice.

"Oh, I hate that," Tavi said through every horn in the court.

The number brightened.

The dead who had been free for minutes bent forward as if a wind pressed against their backs. Living soldiers stiffened. The king grabbed the throne rail. Heatworkers shouted from below as district valves tried to align with the crown coil's dead habit. Mordane's body was gone, but his arithmetic had one last reflex: when complexity threatened control, reduce the world to one.

Mara reached the court from the undercroft stair with ash in her hair and Arveth's absence beside her like a missing limb.

She had no time to grieve properly. That felt like another theft.

Joryn saw her and started toward her. The pressure from the number hit him halfway. His knees buckled. Mara caught him before he fell.

"What is happening?" he gasped.

"Mordane left a ghost made of math," Kesh said, coming up behind Mara with one sleeve smoking.

Tavi's voice cracked through the horn. "A census-command fallback. If the operator dies, emergency law collapses all local identities into civic aggregate. One body. One need. One order."

"Can you break it?"

"I can insult it with tools, but not fast enough."

Othen shouted from another horn. "Valves pulling inward. If that number settles, all heat routes answer the crown again."

Halea Voss stood at the center of the court. The number shone across her dead face. She spoke with effort. "A census is not witness."

Mara looked at the black-glass plates. 1. 1. 1. On every gauge, every horn, every polished court mirror. The final lie of Mordane's life was not that people did not matter. It was that people mattered only when added into something easier to command.

"How do we answer it?" Caldus asked.

He was limping badly. Blood ran down his leg. His knightly collar lay on the stair behind him.

Mara thought of Arveth reading names into fire. Of his ledger now on Ilyr's back. Of uncertain entries. Of unknowns. Of not making truth cleaner than it was.

"Not with one answer," she said.

She climbed onto the broken dais again. The throne cinder under it was cracked, no longer a clean amplifier, but still hot enough to carry sound.

"Read," she said.

Ilyr understood first. He opened Arveth's ledger and began with the first page. "Pell Orwick."

Dilla shouted from the breach, "Lower East Vent."

"Essa Brant."

Rella, standing on a statue base with chalk dust on her hands, answered, "Hummed in the drains."

"Tollen Reed."

Kesh answered, unexpectedly quiet. "Road courier. Bad handwriting. Good debt."

The number flickered.

Not gone. Flickered.

Mara pointed to the crowd. "More."

The court became disorderly in exactly the way the command hated.

Names came from ledgers, mouths, memory, work tokens, family arguments, half-burned broadsides, tattoos, scars, habits, songs, debts, dislikes. Harl Brim shouted that Mav Corren snored like a cracked pump. A woman in a green shawl insisted her sister's name was spelled with two n's and threatened to haunt any clerk who wrote it wrong. A goblin runner named a dead aunt and included three unpaid loans as identifying details. Othen named heatworkers by shift and valve preference. Saelith named mercy patients whose records had been hidden under doctrine. Serathiel, after a long stillness, named three cinder-singers taken into Pale Bough custody generations before and did not call them saints.

That shook Lumenorath more than the court understood.

The number dimmed.

Then it returned, brighter, forcing itself over the names. 1.

Mordane's last command was stubborn because it was simple. Simplicity always had endurance. It offered exhausted people relief from the labor of difference.

Mara felt it press against her too. One city. One victory. One girl to hold the story. One grief. One road.

She nearly let the people chant her name.

They wanted to. She could feel it building as the number weakened: Mara, Mara, Mara, a counter-one to Mordane's one. A cleaner one. A beloved one. The mirror shard at her wrist, still embedded, warmed with warning.

No.

"Not mine," she shouted.

The court stumbled.

"Do not answer one with one. Answer with everyone."

Joryn, leaning on the dais step below her, began laughing. Not because it was funny. Because it was her and not her, the sister he had known and the woman he was learning not to cage.

"You heard her," he shouted. "Everyone be inconvenient."

It was not the line a bard would have chosen.

It worked.

The court broke into multiplicity. Not a chant now, but a storm of particularity. People named themselves too. Rakka Fen, unpaid and angry. Tesson Vair, no sir, no rank, still standing. Dilla Marr, soup not optional. Brakka of the Third Arch, road witness. Caldus Renn, oathbreaker by crown and oathkeeper by choice. Saelith Dawnmere, disobedient healer. Ilyr Noct-Vey, exile with a ledger. Kesh of the Kavik Road, guide, thief, and temporarily undercharging.

The dead added what they could. Some spoke names. Some raised hands. Some took a step. Some lay down and made lying down their first chosen act.

Mara did not speak her own name until the end.

When she did, she said it once. "Mara Venn. Not one. One of."

The number shattered.

Every black-glass plate in the court cracked at once. The cinder gauges went dark. The remaining crown coil pressure vented through Othen's open flues in a harmless belch of blue ash that coated nobles, guards, citizens, and king alike. It made everyone look ridiculous and equally mortal.

Kesh sneezed. "Justice is dusty."

The court laughed.

Then it cried.

Then it began, awkwardly, to work.

The king took off his crown at last.

No one cheered. That was wise. A crown removed did not rebuild a city. It only exposed a head.

He set it on the broken step and looked at the people before him. "The court is open," he said.

Mara almost told him that courts had never been enough. But for today, open mattered. Records mattered. Heat mattered. Names mattered. The dead deciding whether to stand or rest mattered. Caldus lowering himself to sit before his injured leg failed mattered. Joryn's hand on her elbow mattered.

Mordane's last number was gone.

What remained could not be counted quickly.

That was the beginning of its freedom.""",
    35: r"""## Chapter 35: You Woke Us Too Soon

The first dragon voice came from the well.

It was a small well in the palace kitchen court, old enough that servants still lowered buckets by hand when the pumps failed. A scullery boy heard it while filling pitchers for the wounded. He dropped the rope, screamed once, and then apologized to the well because whatever had spoken through it sounded too ancient to interrupt.

By the time Mara reached the court, the well was glowing blue-white.

So were the bread ovens.

So were three cracked hearthstones in the lower district, the baptismal canal under the Ash-Marked Chapel, the old floodbell in Kell Ashgate, the vow-stones Brakka had set in the palace floor, and, according to a goblin runner who arrived breathless and offended, Auntie Grum's left nostril.

"That last one may be metaphor," Kesh said.

The runner shook his head. "It sneezed prophecy."

Tavi, soot-blackened and limping, pushed through the kitchen court with a cracked gauge in one hand. "Everyone stop making folklore. I need measurements."

"The well is talking," Joryn said.

"Then it can wait its turn."

The well spoke again.

Mara heard it not through ears but through every burn on her hands, every ash scar in her lungs, every memory the cinder had brushed raw. Many voices moved inside the water. Some distant as storm over mountains. Some close as breath on the back of her neck. Some curious. Some enraged. Some so wounded they had forgotten the difference.

You woke us.

The kitchen court went still.

People who could not hear the words still felt the pressure of them. Pots trembled. Water climbed the well stones against gravity. Flour lifted from a table and hung in the air like pale ash.

Mara stepped toward the well.

Joryn caught her sleeve. Not to stop her. To be felt before letting go.

"Careful," he said.

"No one is careful enough for wells now."

"Try anyway."

She did.

She did not open the cinder cage. She did not kneel. She did not answer as saint, weapon, crown, or chosen anything. She stood with burned hands loose at her sides and spoke as a girl from a mining city whose vents had been lying all her life.

"We woke the names being burned."

The water rose higher.

Names are sparks, said one dragon voice.

Names are hooks, said another.

Names are small cages, said a third.

Names are doors, Mara answered.

That silenced them for a breath.

Then the grief-heavy presence she had felt below the foundry moved through the well. It was larger than the others without being louder. Vorrakai, though the name had not yet been given aloud. The first dragon, or the oldest wound still capable of speech, or something that had once been a creature and was now a desire wrapped around memory.

Too soon, it said.

The words rolled through Harrowmere.

Not only the kitchen court. Bells answered in towers. The palace ovens boomed. The floodbell in Kell Ashgate rang once, hard enough to crack its old frame. In the Seven Arches, stars glimmered at noon below the bridges and Brakka's clan felt the stone underfoot remember a heavier sky. In Lumenorath, white roots curled away from mirror pools as Serathiel's absent superiors heard a sound their doctrine had kept behind glass. In Khar Veyl, bowls of memory water split, and Ilyr went very still because the phrase the moon below had stopped being poetry. Far under Orrowen, the dead capital opened one sealed window.

Too soon, the voices said.

Mara gripped the well stones. "Too soon for what?"

The water showed her fragments.

Not a clean vision. The dragons were too many, too old, too bad at caring which memories belonged to human bodies. She saw a moon under the world, pale and scaled, sleeping beneath dead streets. She saw light-elf armies burying a song and dark-elf scholars cutting the last verse out of history. She saw gnome engines threaded through root-cities, all ringing with cinder alarms. She saw goblin roads flooded with memory moths. She saw trolls standing on bridges while stars below them went out one by one. She saw a black dragon eye opening in perfect stillness.

Then she saw herself.

Not crowned. Not sanctified. Not dead.

Walking.

Every road behind her carried names. Every road ahead carried armies.

She tore her hands from the well.

Saelith caught her before she hit the stones. "May I?"

Mara nodded once.

Healing light steadied her. Did not erase the burns. Did not take the vision. Only kept her body from following her mind into the water.

Ilyr crouched beside the well, face drawn. "The moon below is not metaphor."

"You said that already."

"I hoped to be wrong with repetition."

Serathiel stood at the court arch, cracked bough in hand, listening to the bells of her own distant city answer from nowhere. Her expression had become the face of an order realizing its silence had not kept the world safe, only delayed the bill.

"Lumenorath will come for you," she said.

Mara coughed, tasted ash, and looked up. "To claim me?"

Serathiel's mouth tightened. "Some will."

"And you?"

The saint-general looked at Saelith, then at the well. "I do not know."

It was the first answer Mara had heard from her that did not try to be a law.

Kesh leaned over the well and immediately leaned back. "I dislike water that looks back."

Tavi shoved him aside and lowered the cracked gauge. It spun until the needle broke off.

"Wonderful," she said. "Useless instrument, continent-scale panic, and I think my left boot is melting."

"What does it mean?" Joryn asked.

Tavi looked at Mara, then at the glowing ovens, then at the sky where blue ash still drifted over Harrowmere. "It means the cinder network is not sleeping evenly anymore. Harrowmere woke a node. Other nodes answered. Some were already close. Some were restrained. Some are angry. Some are..."

"Hungry?" Kesh supplied.

"Curious," Tavi said, which frightened everyone more.

The well water lowered suddenly.

At the bottom, arranged in wet ash, were three marks.

A white root.

A black crescent.

A moon beneath a line.

Saelith, Ilyr, and Arveth's absent ledger all seemed to answer at once, each in Mara's memory.

Lumenorath. Khar Veyl. Orrowen.

The next road named itself before anyone chose it.

Mara hated that. Then she remembered hatred was not refusal by itself.

Vorrakai's presence lingered in the stones.

Too soon, it said once more, softer now. Not warning alone. Not threat alone. Almost grief.

"Maybe," Mara said. "But we are awake now too."

The well went dark.

For one heartbeat, everyone breathed.

Then every bird in Harrowmere took flight at once, fleeing east.

On the horizon, under a sky still bright with foundry ash, three pale banners appeared where no army had stood an hour before.""",
    36: r"""## Chapter 36: The Road After Victory

Morning made Kell Ashgate look gentler than it had any right to.

Ash silvered the slag heaps. Steam lifted from vents in soft columns. Broken windows caught sunrise and turned briefly to gold. The pay yard where foremen had once counted bodies by shift and wage was full of tables now, doors pulled from hinges and laid across barrels. On them lay ledgers, work tokens, chapel papers, crown seals, bread, bandages, cups of Dilla's soup, and lists that kept growing faster than anyone could copy.

Victory looked like bad handwriting.

Mara sat on the pay yard steps with a blanket around her shoulders and Niv's scratched token in her hand. She had slept for twenty minutes and dreamed of wells. Her burns hurt. Her lungs hurt. Her head felt full of bells that had not stopped ringing so much as moved underground.

Across the yard, the dead chose.

No one liked that phrase at first because it sounded too simple for what was happening. Some of the named dead wanted final rites, and Saelith, with permission asked each time and help from chapel attendants who no longer looked certain of their own hands, gave what peace could be given. Some wanted to sit in sun. Some wanted to hear records read. Some wanted to walk to houses where families might open doors or might not. Some could not say what they wanted, and those were hardest. Unknown was not empty, Arveth had taught them. Unknown required patience, and patience after revolution was rarer than courage.

Halea Voss had taken over a table.

Dead scholar, white robe torn, paint half washed from her cheeks, she held a quill with stiff fingers while Rella stood beside her on a crate and read names from chalk slates. Ilyr sat across from them copying Arveth's ledger in dark-elf cipher, Common, and a third script he refused to explain. Every so often he stopped, touched one line, and breathed like someone choosing not to close a wound too early.

Mara brought him water.

"You look terrible," she said.

"Your diplomacy grows."

"Arveth would have corrected your margins."

Ilyr looked down at the page. "He already is."

In the margin, a line of ash had arranged itself under one entry. Uncertain. Verify with second witness.

Mara smiled and had to look away because grief, if met directly, would sit down and refuse to move.

At the east edge of the yard, Caldus argued with three former royal officers and won by refusing every version of command they offered him. He had let Tavi stitch his leg while insulting his pain management. He had slept even less than Mara. The broken shield leaned beside him, crestless and split. When one officer called him sir, he said, "No," and pointed to Tesson Vair for the answer about guard rotations.

That more than anything convinced Mara he might live.

Brakka and the troll masons were rebuilding the north road gate as something that was not quite a gate. More of a question with hinges. Refugees could pass. Records could pass. Soldiers could pass only under witness and without drawn steel. Brakka called it temporary. Tavi called it structurally rude. Kesh called it difficult to monetize and therefore suspicious.

Kesh himself was counting stolen palace signets on a crate while Dilla watched.

"You will return those," Dilla said.

"Define return."

"Kesh."

"I will redistribute them into civic accountability."

"You will put them in that evidence box or I will make soup from your scarf."

He put three signets in the evidence box and palmed a fourth. Rakka Fen slapped it out of his hand without looking up from her bread.

Mara laughed, then coughed until Joryn appeared with a cup of water and the expression of a man personally betrayed by lungs.

"You are leaving," he said.

No greeting. No easing in. Joryn had never had much use for doors when a wall could be kicked.

Mara drank water to buy time. It tasted like iron and clean morning. "Yes."

He sat beside her. Carefully. Every movement cost him. "When?"

"Soon."

"That is not a time."

"Before the armies arrive."

He looked east, where the pale banners had vanished behind morning haze but not from anyone's mind. "Light-elves?"

"Some. Maybe royal loyalists from the outer forts. Khar Veyl will send someone after Maelin's line. Tavi says Brassroot will panic professionally. Ilyr says if Orrowen heard the moon-below phrase, the dead there may start sending opinions."

"Sounds crowded."

"Roads usually are."

He took the scratched token from her hand, turned it over, and pressed it back into her palm. "Still scratched."

"I brought it back."

"You brought yourself back with it. That counts."

The words undid her more gently than kindness might have. For years Joryn had loved her by making the world smaller around her. Work quiet. Keep low. Survive. Now he sat beside a liberated pay yard full of dead citizens, stolen records, troll road-law, and approaching armies, and tried to love her without making her small.

"Come with me," she said.

The offer escaped before she could decide whether it was fair.

Joryn looked at the yard. At Dilla, Niv, Rella, the miners, the wounded, the dead who needed witnesses, the living who needed heat lines rebuilt before nightfall. His jaw shifted.

"I want to."

"That is not an answer."

"It is half of one."

She waited.

"Kell Ashgate needs people who remember what it was before everyone starts arguing about what it should become. Dilla can shame them. Othen can keep pipes alive. Brakka can make the gate rude. But someone has to tell children when the old lies start wearing new coats."

"You?"

"I am very annoying."

"Qualified, then."

He smiled. The real one. The laugh followed, quiet and cracked and fully remembered.

Mara held it carefully inside herself.

"You are letting me leave," she said.

"I hate it."

"I know."

"I am doing it anyway. Do not make it noble."

"I would never."

"You might. People are doing strange things around you."

Across the yard, Saelith stood with Serathiel near a hospice cart. They were not reconciled. Anyone who thought so had never watched two people speak across a broken doctrine. Serathiel held the cracked white bough. Saelith held nothing in her hands on purpose.

Mara went to them before cowardice could call itself rest.

Serathiel looked different in morning light. Less untouchable. More dangerous, perhaps, because uncertainty had entered her and had not made her gentle.

"The Pale Bough banners will reach Harrowmere by tomorrow," she said. "Some will demand custody. Some will demand trial. Some will call for your protection with words almost indistinguishable from imprisonment."

"And you?"

"I will tell them I witnessed refusal."

"Will that help?"

"It will make everyone angry."

Kesh, passing with a box of evidence, said, "A robust opening position."

Saelith looked at Mara. "I am not going back with Serathiel."

Serathiel's face did not move. The bough in her hand tightened with light.

"Where will you go?" Mara asked.

"Where I can learn to heal without owning what I touch."

"That sounds like the road I am taking."

Saelith's composure cracked into something shy and exhausted. "If you permit."

"I am not in charge of your feet."

"No," Saelith said. "But I am asking whether you want the company."

Mara thought of white light without permission. White light asking. White light holding her from the furnace because she had said yes with her whole body when words failed. The answer was not simple. That made it honest.

"Yes," Mara said. "And I reserve the right to be furious with you."

"Granted."

"Do not make that sound official."

Saelith almost smiled. "Trying."

Ilyr joined them with Arveth's copied ledger wrapped in black oilskin. "Khar Veyl has answered."

He held out a strip of dark paper. Mara did not touch it. The script moved anyway.

Maelin retained. Moon-below reference confirmed. Bring witness. Trust no root-light promise.

Serathiel read over Mara's shoulder and went very still.

"No root-light promise," Saelith murmured.

Ilyr folded the paper. "My people remain charming."

"Maelin is alive?" Mara asked.

"Retained," he said. "That is not alive. Not dead. Not safe. But not gone."

The next road gained another weight.

Tavi limped up with a pack nearly as large as herself and two smaller packs carried by unwilling apprentices she had apparently acquired from the heatworks. "If everyone is done making ominous interpersonal arrangements, Brassroot sent a panic code through the north relay."

"Already?" Kesh said.

"Gnomes pride ourselves on speed during catastrophe. Also someone has noticed three cinder regulators singing in languages they were not built to know."

Brakka came last, wiping stone dust from her hands. "Third Arch heard bells under canyon. My clan sends vow: roads open for named and nameless until counting ends."

"Counting never ends," Mara said.

"Then road stays open."

That was as close to a blessing as Brakka gave.

By noon, the company stood at the east road.

Not all who had begun. Arveth was ash and witness. Pell, Essa, Tollen, Lysa, Tomas, Halea, and too many others remained behind in whatever forms choice had left them. Joryn stayed in Kell Ashgate with Dilla's soup line, Othen's valves, Rella's slates, Niv's fierce insistence on being taller soon, and a city that had to learn freedom before armies taught it fear again.

Mara stood at the road's edge with the cinder cage at her hip.

It was quieter now.

Not safe. Never safe. But no longer screaming to be opened. Inside it, the shard glowed softly, as if listening with her instead of for her.

Joryn held out his hand.

Mara gave him the scratched token.

"Keep it," he said.

"You complained."

"I am versatile."

"Niv told me to bring it back."

"Then bring it back again."

The words were too much. She hugged him hard enough that he swore at his ribs. He hugged her back anyway.

"Do not become smaller to come home," he said into her hair.

She closed her eyes. "Do not make home too small to hold me."

"Rude."

"Inherited."

He laughed. She carried the sound with her when she let go.

The road east ran toward Harrowmere's smoking towers, then beyond them toward white-root forests, dark under-realms, buried moons, and all the powers that had heard a girl from Kell Ashgate tell a dragon-heart that the living were awake too.

Behind Mara, Kell Ashgate rang the floodbell.

Not in alarm.

In witness.

Mara walked.

After a while, the others walked with her.

Under the road, very far below, something ancient listened to the rhythm of their feet and did not yet decide whether it was hope or warning.


## Back Matter

### Closing Note

Book One resolves the liberation of Kell Ashgate and the fall of Mordane's foundry. Its unanswered promise is the waking of the wider cinder network, the unresolved fate of Maelin Noct-Vey, and the journey toward Lumenorath, Khar Veyl, and the moon below Orrowen.

### Glossary

**Cinder:** A buried dragon-heart or memory-organ used as fuel, archive, weapon, or sacred object.

**Cinder-singer:** A person able to hear and answer cinder memory.

**Kell Ashgate:** Mara's mining city, poisoned by ash and hidden royal extraction.

**The Seven Arches:** Troll-guarded bridge shrines across the star canyon.

**Lumenorath:** Light-elf forest-citadels where beauty and law are dangerously intertwined.

**Khar Veyl:** Dark-elf under-realms that guard sealed histories and costly truths.

**Orrowen:** The buried empire where the dead remember themselves too strongly to end.

**The Named:** Undead who retain personhood through name, memory, and witness.

**Vorrakai:** The first dragon, whose ancient grief seeks perfect stillness.""",
}


EXPANSIONS: dict[int, str] = {
    33: r"""The court opened in the most literal way first.

Brakka and the masons broke the western doors off their hinges.

They did not smash them. Smashing would have pleased too many people and helped too few. Instead, Brakka set three vow-stones in the doorframe, spoke a road-law older than hinges, and pushed until the gold-lacquered doors sagged outward into the square. The crowd beyond recoiled, then pressed forward, then recoiled again when the dead became visible under the chandeliers. No one had prepared the living for the sight of those they had prayed over standing in torn robes and ash.

"Slow," Brakka ordered.

The word did more than any soldier line. The crowd slowed because the troll's voice made panic feel badly mannered.

Dilla came through first with two women carrying buckets of water and a boy balancing a stack of cups. She glanced at the dead, at the king, at the wounded, at Caldus bleeding on the stair, and clicked her tongue.

"No one in this room has eaten since yesterday, have they?"

That was how the Crown Court became a shelter.

Nobles hated it. Some of them said so until Rakka Fen discovered that noble boots had excellent resale value and that fear made men easy to tip sideways. The gallery benches were dragged down for splints. Velvet banners became bandages. Palace guards who had been striking citizens an hour earlier found themselves carrying water under the supervision of laundresses with terrifying standards. Chapel attendants washed paint from the dead, asking now before touching. Not all of them remembered at first. Saelith's name passed through the court whenever someone forgot: ask, ask, ask. It became a new kind of bell.

Caldus did not sit until Joryn shoved him onto the lower stair.

"Leg," Joryn said.

"There are injured civilians."

"You are bleeding on the injured civilians' floor."

"That sentence lacks military precision."

"I was a miner, not a poet. Sit."

Caldus sat. His thigh wound pulsed badly. Joryn tore a strip from a fallen curtain and bound it with the competence of someone who had learned mine injuries from necessity rather than training.

"Too tight?" Joryn asked.

"Yes."

"Good."

The answer startled a laugh out of Caldus. It hurt his ribs. That felt deserved.

The split-lipped guard approached with the spear he had thrown at the ledger. He held it like evidence against himself. He could not have been older than nineteen.

"Sir," he said.

Caldus looked up. "No."

The young man's face tightened. "Renn?"

"Caldus, if you need my attention. What is your name?"

"Evan Tor."

"Then ask your question, Evan Tor."

The guard swallowed. "Did I commit treason?"

The court noise seemed to dim around that small terror. Caldus remembered being young enough to want the word treason defined by someone else. He wished, with an ache that went beyond the cut in his leg, that someone had answered him better.

"Maybe," he said.

Evan went pale.

"Against what?" Caldus continued. "Against a minister's system, yes. Against an unlawful command, no. Against a crown that hid murder, perhaps. Against the people you shielded when you threw that spear, no."

"That is not clear."

"No."

"What do I do with that?"

Caldus looked at the open doors, the dead, the king without his crown, the citizens entering the court with names and buckets. "You live carefully until clarity catches up. And when someone offers it too quickly, distrust them."

Evan nodded as if the answer frightened him more usefully than comfort.

At the center of the court, Halea Voss stood before the king.

Dead scholar and uncrowned king faced each other while a schoolmaster copied the exchange because Arveth was gone and someone had to be irritatingly exact. Halea's voice came stiffly, each word pulled through a throat no longer built for speech.

"You will open the lower archives."

The king looked at the broken crown on the step. "Yes."

"You will preserve the witness ledgers outside crown custody."

"I... yes."

"You will not declare the dead property, saints, weapons, honored labor, or civic continuance without answer from the named and their witnesses."

The king looked to Serathiel. She did not rescue him. He looked to Caldus. Caldus did not rescue him either.

"Yes," he said.

Halea leaned closer. Paint flaked from her cheek. "You will learn to say no when the next useful man tells you mercy requires hidden rooms."

That answer took longer.

"I will try."

Halea considered him. "Record: insufficient, but better than silence."

The schoolmaster wrote it down.

Caldus found himself smiling despite everything. Arveth would have liked her.

Then the undercroft shook, and Mara's absence became a physical thing again. Heat roared up through the stair. The dead in the court cried out. The king fell back. Caldus tried to stand and failed.

Joryn caught him.

"She is below," Caldus said.

"Yes."

"We should go."

"No."

Caldus stared at him.

Joryn's face was gray with pain, but his voice held. "She told you to stay."

"She is in danger."

"She is always in danger. That is apparently who we know now."

"You are her brother."

"Yes," Joryn said, and every word cost him. "Which is how I know running after her because I am afraid is not the same as helping."

Caldus looked at the court he was holding, the injured line, the dead who needed space, the soldiers deciding whether their next act would be old obedience or new choice. He hated Joryn for being right. Then he respected him for it. Then he understood, fully, that Mara had learned leadership from someone who thought he had only taught her to survive.

The roar below changed pitch.

Caldus lifted his broken shield, not to charge, but to steady himself. "Then we hold the stairs."

Joryn picked up the fallen spear. "Now you are learning."

They held.

Not for glory. Not against a clean enemy. Against panic, falling stone, half-free command, and the constant temptation to abandon the hard place for the dramatic one.

By the time Mara climbed back up with ash in her hair and grief in her face, Caldus had kept the wrong oath long enough for it to become the right one.""",
    34: r"""Mordane's last number did not break only in the Crown Court.

It fought through the city first.

In Bellweather Lane, the hospice pipes groaned as the number tried to claim all warmth for the crown coil. The six patients who had started the morning as the reason Saelith betrayed a courier gate lay under blankets while attendants held valves open with broom handles and prayer. One old woman, the one who had told Mara to stop blocking the stove, demanded to be propped upright.

"If the city is becoming one body," she said, "then this body has opinions."

She made the attendants write the patients' names on strips of bandage and tie them to the heat pipe. It was not a spell in any formal sense. That did not stop the pipe from holding three breaths longer than Othen's gauges predicted.

In the lower tenements, children chalked their names on doors as parents shouted names from windows. Some spelled them wrong. That mattered less than the shouting. A one-eyed miner stood in the street reciting every nickname he had ever heard for everyone in his building, including rude ones, until the black-glass tax plate above the alley cracked from the effort of reducing them to household units.

At the north foundry gate, the sergeant who had stamped Kesh's forged papers stood with the broadside Mara had left face down by the brazier. He read it aloud to his checkpoint. Then he read the names written on the back, added his own mother's name though she was not dead, and ordered the gate opened for witnesses.

"Is that legal?" one soldier asked.

"No idea," he said. "Write that down too."

The number dimmed wherever people became specific.

It brightened wherever people waited for someone important to tell them which specifics counted.

That was how Mara understood the shape of the last battle. Not force against force. Not spell against spell. A terrible argument over whether the world was easier to manage if most people became categories.

She moved through the court while Ilyr read from Arveth's ledger. She did not have to carry every name herself now. That should have relieved her. It did, a little. Mostly it frightened her with the knowledge that leadership meant making a thing large enough to survive her absence.

"Mara," Saelith said.

She was standing by a fallen chapel singer whose arm bent wrong. The singer had been part of Serathiel's crescent, one of those who had hardened the air against citizens. Now she stared at Saelith with fear and pain.

"She says no," Saelith said quietly.

Mara looked at the arm. "To healing?"

"To my touch."

"Then no."

"The break is bad."

"Then ask who she will allow."

The singer's eyes filled. "I do not know."

Saelith knelt, hands folded in her lap. "Then I will sit here until you know, unless you ask me to leave."

It was a small thing. No crowd saw. No horn carried it. It did not crack the number by itself. But Mara felt something in the room become less one and more many. Even harm done by enemies did not make their bodies public property.

Serathiel watched from the broken arch.

"You approve?" she asked Mara.

"I am not the approval office."

"Everyone is making you one."

"Then everyone is wrong."

Serathiel considered that. "You say it as if wrongness will stop them."

"No. I say it because I need practice."

The saint-general looked toward the city beyond the open doors, where names rose in ugly, mismatched waves. "Practice may not be enough when Lumenorath arrives."

"Then practice on the road."

"You invite me?"

Mara almost laughed. "No."

For the first time, Serathiel's mouth curved with something too tired to be offense. "Wise."

"I invite Saelith. I invite anyone who can ask before touching and listen before naming. You can decide whether that includes you before your army does."

That answer was dangerous. Mara knew it as soon as she said it. It gave Serathiel no clean role: enemy, guardian, penitent, judge. It made her choose later without pretending later was mercy.

The number above them flickered again.

1.

Joryn climbed onto a broken plinth below Mara. "Everyone be inconvenient!"

The line spread faster than any elegant slogan could have. Kesh took it up with improvements. "Be specifically inconvenient!" Dilla made it useful. "Be specifically inconvenient while carrying water!" Brakka made it law. "Every foot has its own weight!" Tavi, through the horns, made it technical. "District valves love inconvenience!"

The number began to fail.

Mordane's arithmetic could handle opposition. It had budgets for unrest, projections for sabotage, acceptable losses for riot. It could not handle everyone refusing in slightly different ways at once.

A noblewoman named her maid before herself and then looked shocked by the order. A palace clerk confessed that the west archive had duplicate transport ledgers and was immediately surrounded by three laundresses, two guards, and one dead scholar who all demanded directions. A royal cook opened the kitchen stores and declared that if the civic body was one, the civic stomach was hungry. Children drew arrows to safe lanes. Heatworkers shouted valve numbers and then added the names of the people stationed at them so the numbers could not float free.

The final 1 shrank until it became a black dot on the largest court mirror.

Mara stood before it.

In its dark curve she saw herself again. Not the mirror chamber's worst Mara exactly. A new possible version: the girl who could let the crowd answer Mordane's one with her one. The girl whose name would be easier to paint than thousands of stolen ones. The girl history might prefer because she fit on a banner.

She spat on the mirror.

Kesh made a proud sound.

The dot cracked.

After the number shattered, Mordane's remaining records tried one last defense. Pages burst from hidden wall slots all around the court, census sheets, heat ledgers, mercy authorizations, employment contracts, death classifications, compensation denials, emergency clauses. They flew into the air in a white storm, each one stamped, signed, numbered.

For a heartbeat, the room flinched. Paper still had power. Ink had condemned many of them before any hook touched flesh.

Halea Voss raised one dead hand.

"Do not burn them."

Tavi, halfway through lighting a match with extreme enthusiasm, paused. "Are we sure?"

"Evidence," Halea said.

Dilla snatched the match from Tavi. "No burning records unless you have copied them, child."

"I am older than I look."

"So is paper."

The court began catching pages. Evidence boxes filled. The king himself caught one sheet against his chest and stared at the denial of compensation for Edrin Venn. Mara saw his eyes move from her father's name to her face.

"I did not know," he said.

It was a useless sentence. A true one, perhaps. Useless still.

Mara took the page from him.

"Now you do."

She handed it to Rella for copying.

That, more than spitting on the mirror, broke Mordane's last number. Not fury. Procedure returned to the people it had harmed. Records pulled from the system and made answerable. A king told that knowing late was not absolution but the beginning of work.

The court did not cheer when the number died.

It exhaled.

Then the well in the kitchen court began to glow, and victory turned its head toward the wider world.""",
    35: r"""The voices did not stop at Harrowmere's walls.

Reports arrived all afternoon, carried by riders, runners, birds, bells, broken instruments, and one furious gnome relay that Tavi insisted had been stable before everyone began awakening ancient memory organs without filing engineering notices.

From the Gloamfen: memory moths rose in daylight and formed the shapes of old road signs over Auntie Grum's sleeping back. Narka sent a message written on eel skin: Your girl made the marsh remember debts no one currently alive incurred. Congratulations. Terrible manners. Market still open.

From the Seven Arches: the stars below the canyon brightened at noon. Brakka's clan heard three bridge-vows spoken by no living troll. One was shelter. One was warning. One was in a language Brakka refused to translate in public because some words deserved a stone before a mouth.

From Brassroot: the Glass Engine flooded its own lower chamber with harmless green light, then printed the same phrase on every regulator panel: NODE STATUS DISPUTED. Tavi read that message three times and sat down hard.

"That is not possible," she said.

Kesh looked over her shoulder. "I have noticed possible is struggling today."

"No, I mean grammatically. The Glass Engine does not know the word disputed."

"Perhaps it learned from us."

Tavi looked horrified and touched.

From Khar Veyl: black paper, no sender, no seal, only script that appeared in water before ink. Maelin retained. Moon-below watches. Bring witness. Trust no root-light promise. Ilyr read it alone first, then again with Mara, then a third time while Saelith stood near enough to hear and far enough not to demand trust.

From Lumenorath: no written message. Only every white-root instrument in Serathiel's travel chest rang once and cracked along the grain. Serathiel went pale when it happened.

"What does that mean?" Mara asked.

"It means the Pale Bough heard the same thing I did and will pretend it has a name for it before sunset."

"Does it?"

"No."

The last report came from Orrowen without messenger.

At dusk, every shadow in the Crown Court leaned east.

Not long. Not dramatically enough for panic among those who had learned to be tired before afraid. But Ilyr saw. Halea Voss saw. The dead who had chosen to remain standing saw. The shadows leaned toward a place below the world, and for one heartbeat the air smelled of salt, bone dust, and moonlit stone.

Halea whispered, "The buried empire has opened a listening gate."

Ilyr closed his eyes. "Then Book Two will be unpleasant."

"What?" Mara asked.

He opened one eye. "A dark-elf idiom."

"It is not."

"No. But it should be."

The dragon voices returned after sunset, not as a roar this time, but as a council arguing through small things.

A hearth in the hospice said wait in a voice like scales on snow.

A cracked lantern in the pay yard said burn what binds.

The floodbell in Kell Ashgate said remember the first bargain.

The cinder shard in Mara's cage said nothing, which worried her more than if it had shouted.

She carried the cage to the slag ridge above the city and sat where she had once hidden to avoid foremen. Below, Kell Ashgate glowed in patches: emergency lamps, cookfires, exposed heat pipes, the blue-white shimmer of names still rising from foundry ash. Harrowmere smoked beyond the ridge. The palace no longer looked clean.

Joryn found her there.

"You brood badly," he said.

"I am not brooding."

"You are sitting on a ridge with a mysterious cage after a dragon well told you the world woke too soon. That is advanced brooding."

She did not answer. He lowered himself beside her with a hiss of pain.

"I saw you with the well," he said.

"I did not know if I was answering right."

"Did anyone?"

"No."

"Then you were at least equally qualified."

The cage between them glowed faintly. Mara touched the brass mesh. "What if it is right?"

"The dragon?"

"What if we woke something too early? What if Mordane's foundry was only one bad room in a house full of worse doors? What if every name we freed rang a bell something hungry can follow?"

Joryn was quiet for once.

Mara looked at him. "This is where you tell me to stop borrowing trouble."

"Trouble appears to have collateral on you. Borrowing is no longer the problem."

She laughed despite herself.

He nudged her shoulder with his. "Maybe too soon is the only time anyone wakes. If people waited until safe, Kell Ashgate would still be crawling into vents for men who counted coughs as inefficiency."

"That was almost wise."

"Do not tell Dilla. She will assign me speeches."

Below, someone began reading names in the pay yard again. The sound drifted up, thin but steady.

Mara closed her eyes.

Vorrakai listened.

She knew the grief-heavy presence now not as a friend, not as an enemy, but as a horizon with intention. It did not want Mordane's arithmetic. It did not want Serathiel's sanctuary. It wanted stillness. Perfect, unspent, unburning, ungrieving stillness. Part of Mara understood why such a thing might seem merciful to a creature whose heart had been mined for ages.

The living are noisy, she thought toward it again.

This time, the answer came softer.

Noise becomes fire.

"Sometimes," Mara whispered.

Joryn looked at her. "Dragon?"

"Yes."

"Tell it we have enough fire."

She almost did. Then she chose better.

"We are learning what to do with it," she said.

The presence withdrew.

Not gone. Never gone now. But distant enough that the night returned: insects in the slag grass, hammers in the city, someone cursing cheerfully over a stuck valve, Dilla shouting that grief did not excuse wasting onions.

Mara breathed.

The next morning would bring banners, messages, demands, histories waking with teeth. Tonight, the city was alive, the dead were named or being sought, and the road had not yet required her feet.

"You will go," Joryn said.

It was not a question.

"Yes."

"Because of the banners?"

"Because of Maelin. Because of Lumenorath. Because of Orrowen. Because the cinders are awake enough to be used again by whoever arrives first with a beautiful excuse."

"Because you heard them."

She looked down at her burned hands. "Because I heard them."

Joryn nodded.

He did not say stay.

The restraint was so large Mara could feel its edges.

The floodbell rang below, once, then again. Not alarm. Witness. Practice for a city learning how to speak before power translated it.

On the eastern horizon, the pale banners appeared and vanished in ash haze.

Too soon, the dragon had said.

Mara watched the road until dark covered it.

"Maybe," she said. "But not alone."""
    ,
    36: r"""The first council of free Kell Ashgate met in the pay yard because no one trusted the guildhall and the chapel roof had a hole in it.

Calling it a council was generous. It was a table argument with witnesses. Dilla presided because she had soup, and soup had become the closest thing to a neutral institution. Othen represented the heat crews, though he kept insisting no one represented heat crews without three meetings and a fistfight. Rella represented the children until someone objected, at which point every child in earshot objected louder. Joryn represented miners who did not trust speeches. Halea represented the named dead who wanted civic answer. Brakka represented the road by refusing to sit in a chair that looked structurally dishonest.

Mara tried not to represent anything.

This failed at once.

"You should speak first," said the schoolmaster.

"No."

"You led the..."

"No."

Dilla set a bowl in front of him hard enough to splash his notes. "Girl said no. Write it down if you need to feel useful."

The schoolmaster wrote: Mara Venn declined first speech.

Halea leaned over. "Good record."

The council decided very little and named many things that could not wait. Heat before trials. Copies before accusations. Witness halls before monuments. No statues until every missing name had been sought twice and every living tenant had a roof. The dead who chose final rites would have them outside chapel monopoly. The dead who chose to remain would be citizens under provisional witness, not property, not relics, not proof of anyone's virtue. The king's temporary envoys could speak only in open yard. The crown could send food, engineers, and records before it sent soldiers.

"And if it sends soldiers first?" someone asked.

Brakka touched the rude new gate. "Then road becomes narrow."

That went into the record too.

By midmorning, Mara understood why Mordane had loved numbers. They were easier than this. This was slow, contentious, repetitive, full of people correcting one another's memory and motives. It made no clean song. It also did not require hidden rooms.

When she finally slipped away, Kesh was waiting by the east road with three packs.

"I packed yours," he said.

"That was kind."

"Please do not insult me. I packed expensive necessities and one spoon."

"One?"

"A shared spoon builds fellowship."

"A shared spoon builds murder."

"Then we shall eat carefully."

Tavi arrived with five packs, none of them reasonable, and a Brassroot apprentice trailing behind carrying a box that ticked. "Do not jostle that."

"What is it?" Mara asked.

"A regulator listener, a cinder alarm, and possibly rent."

"Possibly?"

"If it survives, I can invoice history."

Saelith came next with no white cloak. She wore a gray travel coat borrowed from Dilla and mended at the sleeves. Without the pale order around her, she looked both smaller and more dangerous, like a blade taken out of a ceremonial case and discovered to have an edge.

Ilyr brought Arveth's ledger and the black paper from Khar Veyl. He had slept not at all. His eyes held the east like a debt.

Brakka arrived last, though she had said she would stay at the gate.

Mara raised an eyebrow.

"Road goes east," Brakka said.

"Kell Ashgate needs you."

"Kell Ashgate has stones. Stones remember instructions."

"Your clan?"

"My clan sent reply." Brakka showed a small tablet etched in fresh vow-script. "Third Arch opens for refugees, records, and fools walking toward old trouble. They assume I am the third."

Kesh peered at the tablet. "That is familial affection?"

"Yes."

"Trolls are warm people."

"We hide it under accuracy."

Caldus approached with a staff instead of a sword. His leg was bound. His shield remained behind in the pay yard, propped near the evidence tables. When Mara looked at the empty space on his arm, he shrugged.

"It broke."

"You could mend it."

"I might. Later. Today I need a hand free."

"For what?"

He looked toward the road. "Whatever asks before becoming an oath."

That answer was almost unbearably him.

At noon, Joryn walked Mara to the first bend.

The company gave them room. Even Kesh, which meant either kindness or fear of Dilla. The road dust was warm. The sky was clear in that hard blue way that often followed catastrophe, as if weather disliked being upstaged.

"I am supposed to say something older-brotherly," Joryn said.

"Please do not."

"I prepared notes."

"Burn them."

"Tavi said paper should not be wasted."

"Tavi has never had an older brother."

He smiled, then took her hands carefully because of the burns. "You are not leaving because home is too small."

"No."

"You are leaving because home is large enough to matter."

Mara had no breath for that.

"That was good," she managed.

"I know. I hate when wisdom happens to me."

She hugged him. He held on longer than he had in the foundry, longer than either of them could pretend was practical. When he let go, his eyes were wet and annoyed by it.

"Bring the token back again," he said.

"I will try."

"No." He closed her fingers around it. "Try is for things you control. Promise to want to come back. That is enough."

Mara held the scratched metal, the ordinary impossible weight of it. "I promise."

That was true.

He stepped back before she could.

The company began walking east.

Mara did not look back until the bend because she was brave in many ways and a coward in several useful ones. When she did, Joryn stood in the road with Dilla, Niv, Rella, Othen, Halea, and half of Kell Ashgate behind him. The floodbell rang once. Everyone in the city seemed to hear it differently. Alarm. Farewell. Witness. Work bell. Road bell.

Mara lifted her hand.

Niv shouted, "Do not scratch it more!"

She laughed and kept walking.

The road east bent toward Harrowmere first, where the crown lay off the king's head and records lay open in the court. Beyond Harrowmere waited pale-root forests and the order that wanted to name her danger. Beneath the road waited dark paths to Khar Veyl, where Maelin's retained line pulled at Ilyr like a hook he had chosen to follow. Farther still, under dead Orrowen, the moon below the world had heard its name.

The cinder cage at Mara's hip warmed.

Not screaming. Not commanding. Listening.

Under the earth, Vorrakai listened too.

Mara walked with ash on her hands, a scratched token in her pocket, a company at her side, a freed city behind her, and a waking world ahead.

For once, the road did not feel like escape.

It felt like answer.

They made their first camp before sunset because Caldus nearly fell into a ditch and refused to admit the ditch had won.

"It was strategically placed," he said, sitting on a milestone while Tavi unwrapped his leg bandage with the cold satisfaction of a woman being proved right by blood.

"The ditch?" Kesh asked.

"Yes."

"I will note the ditch as a hostile actor."

"Do not encourage him," Tavi said. "His wound has opinions."

The camp stood in a hollow east of the Ashgate road, below a line of wind-bent pines. From there they could see Harrowmere's smoke smudging the west and, farther north, the black shoulder of Kell Ashgate. The city lights came on unevenly as dusk fell. Not the old clean grid of crown heat, but patches: a hospice lamp, a valve crew's brazier, a line of lanterns in the pay yard, the floodbell tower, the rude new gate where Brakka's stones glowed faintly.

Mara sat with her back against a pine and let the distance hurt.

Leaving had seemed like one act at the road bend. It was not. Every mile repeated it. Every time she looked back and the city was smaller, she had to choose again. She hated that. She was beginning to suspect that courage was mostly repetition with worse scenery.

Saelith came to sit near her. Not beside. Near.

"May I check your hand?"

Mara held it out.

The question still made something in her unclench.

Saelith cleaned the torn bandage with warm water from Tavi's kettle. The burns from the furnace had blistered at the edges. The cut from Tavi's key had reopened. Ash had settled into the lines of Mara's palm so deeply it looked like a map.

"This will scar," Saelith said.

"Good."

"Good?"

"I keep needing proof I was there and did not imagine being brave."

Saelith looked at the hand in hers. "You do not need scars for proof."

"No. But I like evidence."

The light-elf almost smiled. "Arveth's influence."

The name sat between them.

Mara looked toward Ilyr. He was across the hollow, copying the ledger by firelight even though his eyes must have ached. Kesh had fallen asleep for three minutes, claimed it was reconnaissance, and was now sharpening a knife while watching the road. Brakka stood at the edge of camp with both hands on her maul, listening to the ground. Tavi had three devices open on a blanket and was threatening to name one of them after Caldus's ditch.

"I did not thank him," Mara said.

"Arveth?"

"Not properly."

"Would he have accepted it properly?"

Mara thought of the dead clerk's dry voice. "No. He would have corrected my phrasing."

"Then honor him inaccurately and let the ledger object."

That was unexpectedly kind. Mara looked at Saelith, who looked tired enough that the old smoothness could not cover her.

"Why did you come?" Mara asked.

Saelith folded the fresh bandage carefully. "Because I have spent my life inside a beautiful room where every answer arrived before the wounded were allowed to finish speaking. Because I helped hurt your brother. Because I touched you without leave. Because when I asked, you still let me stand near enough to help. Because if I go home now, they will explain me back into obedience."

"That is many reasons."

"I am making up for lost complexity."

Mara flexed her newly wrapped hand. "I am still angry."

"I know."

"I may stay angry."

"I know."

"You do not get to turn that into penance you can admire."

Saelith went still, then bowed her head. "Thank you."

"That was not a kindness."

"It was a boundary. I am learning to be grateful for those."

Mara did not know what to do with that, so she let it stand unpolished.

At the fire, Tavi's cracked regulator listener began clicking.

Everyone stopped.

The device was no larger than a bread loaf, all brass ribs, glass dials, and one little flag Kesh had painted with a rude face while Tavi was not looking. It had been quiet since the road bend. Now the needle spun east, north, east again, then down.

"That is not a direction," Kesh said.

"It is if you are a cinder signal traveling under the world," Tavi replied.

"I preferred geography before it developed ambition."

The device clicked out three pulses, then seven, then one. Tavi's expression changed.

"Brassroot code?" Mara asked.

"No. Older. Root-relay pattern." She adjusted a dial. "White-root resonance from Lumenorath is moving west. Fast."

Saelith's face tightened. "How fast?"

"If by horse, impossible. If by root-road, dawn."

Brakka turned from the camp edge. "Root-road crosses under old treaty stones."

"Can it reach Kell Ashgate?" Mara asked.

"Not directly," Saelith said. "But it can reach Harrowmere's chapel gardens."

No one liked that.

Kesh stood and kicked dirt over the smallest edge of the fire. "So the beautiful army arrives while the city is still counting its own teeth."

"Not an army," Saelith said.

He looked at her.

She corrected herself. "Not only an army."

The regulator clicked again. This time the needle swung north and stayed.

Ilyr looked up from the ledger.

"Khar Veyl."

Tavi frowned. "How do you know?"

"Because the fire just cast a shadow in the wrong direction."

It had. Every pine shadow leaned north though the sun was gone west. Ilyr stood, ledger in one hand, black paper in the other. The script on the paper shifted.

Witness party moving. Do not bring root-light into lower gates. Maelin retained in moonward custody. Exile Noct-Vey answer for half-truth.

Kesh made a face. "That last part sounds unfriendly."

"It is family," Ilyr said.

"I repeat myself."

Mara watched him fold the paper. "Will they take the ledger?"

"They will try to decide whether it should exist."

"And you?"

Ilyr looked at the pages under his hand. "I will disappoint them thoroughly."

That seemed to be the most sincere vow a dark-elf exile could make.

The third sign came from below.

Not the regulator. Not the fire. The ground.

A low tone passed through the hollow, so deep the pine needles trembled. Mara tasted salt. For one second the dirt under her boots felt like a shore at low tide, though no sea lay near Kell Ashgate. The cinder cage warmed and then cooled. Brakka set one palm to the earth. Tavi's devices all went silent at once, which was so unnatural that even Kesh stopped joking.

Mara heard a whisper under the tone.

Moon below.

Then, fainter, in Arveth's dry cadence though not his voice:

Second witness required.

Ilyr closed his eyes.

"Orrowen," he said.

No one asked whether he was sure.

The campfire snapped. Somewhere in the dark beyond the road, an owl called once and then decided against a second opinion.

Mara looked around the small hollow: a disgraced knight with no shield, a goblin guide whose loyalty had outgrown his invoices, a gnome engineer holding a device that had learned the wrong languages, a light-elf healer wanted by her own law, a dark-elf exile carrying a dead clerk's ledger, a troll oath-sister listening to roads under roots, and herself, an ash-runner with burned hands and too many powers eager to turn her into an answer.

"We cannot outrun all of them," Caldus said.

Mara looked at him.

"Lumenorath by dawn," he continued. "Khar Veyl already shadowing. Orrowen listening below. Royal loyalists will gather west. Kell Ashgate is exposed. Harrowmere is unstable. If we try to run from each pressure, we become exactly what Mordane wanted you to be: a single moving point everyone chases."

"Then what?"

Caldus grimaced as Tavi tightened the bandage. "We choose where to be found."

Brakka nodded. "Road with vow, not ditch."

"Enough about the ditch," Caldus said.

Mara stood and walked to the edge of the hollow. The road split there. East toward Harrowmere and Lumenorath's reach. North toward old quarry roads and, beyond them, the first hidden passes to Khar Veyl. Southeast toward dry riverbeds that might, if Ilyr's maps were right, lead eventually to Orrowen's dead approaches. None were safe. Safe had become a word for people pretending not to see the hook.

She took Niv's scratched token from her pocket.

Not one road. Not one answer. But they could not walk three directions tonight.

The token was warm from her hand. She thought of Niv demanding it back unscratched, Joryn changing the promise, Arveth marking uncertain entries, Brakka's road carrying different feet at different weights.

"We go to Harrowmere first," she said. "Not into the chapel gardens. Near enough to see which Pale Bough faction arrives and whether the city can hold without us. Then north before they close root-roads around the passes."

"Toward Khar Veyl?" Saelith asked.

"Toward Maelin's line."

Ilyr looked at her for a long moment. "That will make my people suspicious."

"Good. We should arrive familiar."

Kesh smiled. "There she is."

"And Orrowen?" Tavi asked.

Mara looked down at the road under her boots. The moon-below whisper had gone quiet, but quiet was no longer absence.

"Orrowen gets the second witness after we understand the first lie."

Ilyr nodded slowly. "That is almost a strategy."

"Everyone keeps saying that like it is bad news."

They did not get to sleep immediately.

The road refused to let strategy remain theoretical.

Kesh heard the riders first. He lifted one hand, head angled, and every loose part of him went still. Mara had seen him lie, bargain, steal, laugh with bread in his mouth, and pretend not to care about courage. Stillness looked strangest on him. It made his sharp face older.

"Three coming," he said. "No. Four. One hurt. Two trying to sound like four more."

Caldus reached for the sword he no longer carried. His fingers closed on air. For one breath his face showed the loss plainly, not of the weapon, but of the old certainty that a weapon could decide what kind of man stood behind it. Then he took up the staff Tavi had mocked and planted it beside his bad leg.

"Royal?" Mara asked.

Kesh listened. "Shoes say palace road. Breathing says terrified. Harness says stolen badly. The last one is bleeding enough to be honest."

"You can hear honesty?"

"Only when it drips."

Brakka stepped to the road. The stones under her feet shifted, not much, just enough to make the hollow's entrance narrower. Tavi dragged her regulator blanket back with a hissed curse and snapped two devices closed. Saelith banked the fire with careful hands so the light fell low and did not blind them. Ilyr wrapped the ledger and slid it beneath a root, then put one palm over it as if the earth might be persuaded to keep quiet.

The riders burst out of the dark badly.

The first horse stumbled. Its rider, a palace courier in a torn green coat, clung with one hand and pressed the other to his side. Behind him came a woman in kitchen whites gone gray with soot, riding without stirrups and carrying a bundle against her chest. The third rider was no rider at all but a boy no older than Rella, tied to a saddle because fear had shaken him past balance. The fourth followed at a distance with a short spear and the posture of someone who had been given authority by panic.

"Stop!" the spear carrier shouted.

Nobody stopped in a way he wanted.

Brakka's stone lip rose across the road. The first horse jolted to a halt and nearly threw the courier. Kesh caught the bridle. Saelith moved toward the wound, then stopped.

"May I help you?" she asked.

The courier looked at her ears, her light-elf face, the gray travel coat, the ruined road behind him, and nearly laughed from terror. "If you are not here to take us back."

"I am not."

"Then yes."

She put her hands to his side and light answered softly, not a blade, not a command, only warmth around torn cloth. The courier sagged against Kesh, who complained about blood on his sleeve and held him up anyway.

The spear carrier did not lower his weapon. He had the broad face of a lesser guard and the wide eyes of a man standing inside events larger than his training. "By emergency order of the Harrowmere provisional court, these witnesses are to be returned."

"Returned to whom?" Caldus asked.

The guard blinked. Recognition crossed his face and made him angry, because anger was easier than kneeling or asking. "Sir Caldus?"

"No."

"You are wanted for deposition."

"I am standing here. Depose efficiently."

The guard's grip tightened. "The city is not safe. The king's loyalists have claimed the western barracks. The kitchen court says every prisoner must be witnessed before removal. The royal chaplains say every dead thing must be locked below the palace until law can decide what it is. The Pale Bough sent word that contaminated persons are to be placed under serene protection."

"That is a lot of people with chains discovering nicer nouns," Kesh said.

The woman in kitchen whites slid down from her horse with the bundle in her arms. It was not a child. Mara saw wax seals, folded parchment, and one brass plate snapped from a ledger cover.

"I am Fenna Clay," the woman said. Her voice shook, but the name stood. "Second cook, west hearth. I watched Lord Mordane order the dead brought through the warming tunnels. I heard the king agree to sign the quiet writ. I stole this because the first clerk who tried was killed."

Ilyr's gaze sharpened. "Quiet writ?"

Fenna held out the brass plate. "Names to be removed from public record."

The cinder cage at Mara's hip warmed.

Not command.

Recognition.

The boy tied to the saddle made a small sound. His eyes were fixed on the brass plate. Saelith still had one hand at the courier's wound, and she turned her head only enough to see him.

"Your name is on it," Mara said.

The boy flinched as if she had struck him.

Fenna's mouth tightened. "His mother. Palace washer. Dead last winter, they said. Serving still, I think. He saw her in the lower hall after the bells. He ran."

The spear carrier lifted his weapon half an inch. "This is why they must return. The court cannot hold if every witness scatters."

"The court cannot hold if every witness is gathered conveniently for the people who want silence," Caldus said.

"You deserted your oath."

Caldus looked down at his staff, then at the road, then at the shaking boy tied to the saddle. "No. I finally found the part it was meant to protect."

The guard stepped forward.

Mara felt the cinder listen.

The easy thing would have been fire. Heat under the road. A word sharp enough to throw the guard into the ditch Caldus had lost to. The cinder offered shapes of it, not as temptation exactly, but as memory. Kings had ended arguments that way. Dragons had ended kingdoms that way. Mordane had ended people in quieter versions of the same sentence.

Mara took Niv's scratched token from her pocket instead.

"What is your name?" she asked the guard.

He stared. "This is not a hearing."

"It is now."

"By whose authority?"

Mara almost answered badly. She felt the old furnace-wound in her chest, the place where power wanted to stand taller than fear. Then she looked at the boy, the cook, the courier bleeding into Kesh's sleeve, Caldus with no shield, Saelith waiting for permission even with light in her hands, Ilyr guarding a ledger that had become more dangerous than a blade, Brakka holding the road without closing it.

"By witness," Mara said. "Not mine alone. Everyone here hears you. Say your name before you take people back into someone else's lock."

The guard's face worked.

For a moment, he might have attacked.

Then the boy tied to the saddle whispered, "Lenn Voss."

The guard looked at him.

The boy swallowed. "His name is Lenn Voss. He used to let kitchen boys sleep near the bakehouse in winter."

Fenna nodded once. "He did."

The courier, gray with pain, added, "He carried old Meret down the west stair when smoke took the laundry. I saw."

Lenn Voss stood in the road with his spear half-raised while other people made him larger than his order.

That was the trap in names, Mara was learning. Not that they bound you to what you had been, but that they made it harder to pretend you had only ever been what fear required next.

His spear lowered by inches.

"If I let them go," he said, "my captain will call it treason."

"Probably," Kesh said.

Tavi elbowed him.

Mara stepped closer. Not too close. The spear was still a spear. "Then do not let them go. Come with them as guard. Stand in Harrowmere tomorrow and say you kept witnesses alive because someone has to."

"I cannot leave my post."

"Your post is burning."

"My family is in the western quarter."

That changed the shape of the road.

Brakka listened to the ground. "West road not closed yet."

Tavi opened the smallest of her devices. "If palace relays are still singing, I can make the old heat markers show false traffic for a little while. Not long. Long enough for a guard with sense to move a family through a service culvert."

"You can do that from here?" Kesh asked.

"No. I can do something arrogant from here and hope the equipment mistakes confidence for access."

"A proud gnome tradition."

"Foundational."

Lenn Voss looked from Tavi to Mara, and Mara saw the terrible thing she had offered him. Not forgiveness. Not safety. Choice. Choice was heavier than command because nobody else could carry it once handed over.

"If I run," he said, "I am done."

Caldus answered quietly. "Yes."

"If I return them, they may die."

"Yes."

"If I take the writ north, every faction will want it."

Ilyr lifted his chin. "Yes."

Lenn gave a strangled laugh. "Does anyone here know how to say anything comforting?"

Brakka considered. "Road exists."

Kesh spread his hands. "There you are. Practically a lullaby."

The boy on the horse began to cry then, silently at first, then with the exhausted force of someone who had not had time to be young during the collapse of a kingdom's lies. Fenna reached up and untied him. He slid down, stumbled, and did not fall because Saelith caught his elbow after asking with her eyes and receiving the smallest nod.

"My mother did not know me," he said.

Mara's throat closed.

No one answered too quickly.

At last Ilyr took the brass plate from Fenna and held it where the fire could show the scratched columns. "Then we make a record that knows her."

"Will that help her?"

"I do not know."

The boy looked furious at the honesty, then grateful, then both together.

Mara knelt in the road before him. Her burned hand hurt when she set it on her knee. "What was her name?"

"Sella," he said. "Sella Brin. She sang badly. She saved buttons in blue jars. She said palace soap was too proud to clean anything properly."

The cinder at Mara's hip warmed again, and this time the warmth passed into the ground, small as a coal carried under ash. No voice rose. No dead woman appeared. The world did not reward grief with spectacle.

But under the road, something noted the name.

Fenna bowed her head. Lenn Voss turned away and wiped his face with the heel of his hand as if sweat had become suddenly tragic. Kesh pretended to inspect the horse's tack. Caldus looked east. Saelith kept her light around the courier's wound and asked before tightening it.

Mara stood.

"Tavi," she said. "Can you send the false heat markers?"

The gnome bared her teeth at the device. "I can offend several design principles at once."

"Do it."

"With joy."

For the next quarter hour, the camp became a small, furious workshop. Tavi tuned brass ribs by moonlight, using Kesh's knife, Saelith's hairpin, and three insults from her grandmother's dialect. Brakka walked twenty paces down the road and pressed her palm to a boundary stone until old vow-script glimmered under moss. Ilyr copied the quiet writ in two scripts while Fenna corrected spellings over his shoulder with the authority of a cook who had once managed six ovens and forty fools. Caldus taught Lenn Voss how to wrap his spear in cloth so it looked like a walking staff from a distance, and did not mention that both of them knew it was still a weapon.

Mara watched them all and understood, with an ache almost too large for her ribs, that this was what came after victory when victory was real: not peace, not applause, not rest, but people deciding in the dark what kind of evidence they would become.

At last Tavi's device clicked once.

Far west, down in Harrowmere, three dead heat markers would flare in empty alleys, then fade toward the river. Palace patrols would chase ghosts made of bad math and gnome spite. Lenn Voss would ride west for his family with Fenna's spare horse and no promise except that the road had not closed yet. Fenna, the boy, the courier, and the quiet writ would remain with Mara's company until dawn, then split toward the troll-open refugee road under Brakka's mark.

Before Lenn left, he faced Mara.

"I do not know what you are," he said.

Mara looked at the cinder cage. "That makes two of us."

"But I know what he was." Lenn nodded toward Harrowmere, where Mordane's absence still felt like a hand under a cloth. "If they ask who stopped me, what name do I give?"

For a heartbeat, the old fear rose: ash-runner, nobody, furnace girl, expendable. Then she felt Joryn's token in her pocket and Arveth's uncertain margin under the earth and the boy's voice saying Sella Brin.

"Mara Venn," she said. "Of Kell Ashgate."

Lenn repeated it once, carefully, as if making a record.

Then he rode west into the dark.

They slept in watches after that, though sleep was a generous name for lying down and letting fear file its paperwork. Mara took the last watch before dawn. The sky paled behind the pines. The road waited. Under it, the world listened.

She did not answer too quickly.

That, at least, she had learned.


## Back Matter

### Closing Note

Book One resolves the liberation of Kell Ashgate and the fall of Mordane's foundry. Its unanswered promise is the waking of the wider cinder network, the unresolved fate of Maelin Noct-Vey, and the journey toward Lumenorath, Khar Veyl, and the moon below Orrowen.

### Glossary

**Cinder:** A buried dragon-heart or memory-organ used as fuel, archive, weapon, or sacred object.

**Cinder-singer:** A person able to hear and answer cinder memory.

**Kell Ashgate:** Mara's mining city, poisoned by ash and hidden royal extraction.

**The Seven Arches:** Troll-guarded bridge shrines across the star canyon.

**Lumenorath:** Light-elf forest-citadels where beauty and law are dangerously intertwined.

**Khar Veyl:** Dark-elf under-realms that guard sealed histories and costly truths.

**Orrowen:** The buried empire where the dead remember themselves too strongly to end.

**The Named:** Undead who retain personhood through name, memory, and witness.

**Vorrakai:** The first dragon, whose ancient grief seeks perfect stillness.""",
}


def replace_chapters(text: str) -> str:
    pattern = re.compile(r"(?m)^(?:#{1,2}) Chapter (\d+): .*$")
    matches = list(pattern.finditer(text))
    by_no = {int(m.group(1)): m for m in matches}
    for chapter_no in sorted(CHAPTERS.keys(), reverse=True):
        match = by_no[chapter_no]
        start = match.start()
        later = [m.start() for m in matches if m.start() > start]
        end = min(later) if later else len(text)
        replacement = CHAPTERS[chapter_no].strip()
        if chapter_no in EXPANSIONS:
            replacement += "\n\n" + EXPANSIONS[chapter_no].strip()
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
        'current_form: "full-length draft zero with Book One chapters 1-36 revised in pass 01; Book One has a complete bespoke first revision"',
        meta,
    )
    METADATA.write_text(meta, encoding="utf-8")


def update_summary(word_total: int) -> None:
    if not SUMMARY.exists():
        return
    text = SUMMARY.read_text(encoding="utf-8")
    text = re.sub(
        r"\| The Ash Beneath the Crown \| `book-01-the-ash-beneath-the-crown` \| [\d,]+ \| \d+-\d+ \|",
        f"| The Ash Beneath the Crown | `book-01-the-ash-beneath-the-crown` | {word_total:,} | {round(word_total / 300)}-{round(word_total / 250)} |",
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
    print(f"Book One chapters 33-36 revised. Word count: {total}")


if __name__ == "__main__":
    main()
