#!/usr/bin/env python3
"""Revision pass 01i for Book Three chapters 1-8.

Replaces the opening Book Three scaffold with bespoke Part I chapters:
the daylight rising of the dead, factional demands for cinder weapons,
the Pale Remnant's first strike, the dangerous open archive, the mixed
caravan of living and dead, Third Arch refuge, Arveth's fading name, and
the storm road toward the dragon court.
"""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "output" / "book-03-the-dragon-that-dreamed-death"
MANUSCRIPT = BOOK / "manuscript.md"
METADATA = BOOK / "metadata.yaml"
SUMMARY = ROOT / "output" / "README.md"


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


CHAPTERS: dict[int, str] = {
    1: r"""## Chapter 1: The Morning Corpses Rose

The first corpse rose in a cabbage field because the farmer had planted over an old road.

Mara learned that later, after the screaming, after the shovel, after Caldus had disarmed three frightened men without cutting any of them, after Tavi had knelt in the mud with a measuring wire between her teeth and declared that the dead man was producing no detectable engine heat unless one counted civic panic as a fuel source. At dawn there was only the farmer's daughter running barefoot into the refugee camp outside Harrowmere, nightshirt pasted to her legs with dew, breath torn into pieces.

"My father is in the field," she said.

Kesh glanced toward the pale tents and smoke-pots beyond the ditch. "Many fathers are in fields."

"He has been dead eleven years."

No one laughed.

The camp changed around the sentence. A kettle hissed over. Someone dropped a bucket. Three Orrowen dead who had come with Sava Rennet from the moon-chamber turned their translucent faces toward the road at once, as if hearing a bell too low for living ears. Saelith, who had slept sitting upright with her back against a wagon wheel, opened her eyes already afraid. Ilyr reached for the ledger strapped beneath his coat. Brakka rose without a word, huge hands closing around the haft of her maul. Caldus looked at Mara, not as if waiting for a command, but as if reminding her that no one else was allowed to make her one.

The dragon-moon had opened one eye beneath the world three nights ago.

Since then, nothing had slept correctly.

The farmer's field lay a mile east of the camp, where Harrowmere's wet lowland widened into orderly furrows and broken boundary stones. It should have been ordinary country: cabbages under silver dew, blackbirds arguing on a fence, a cart track glistening with puddles, smoke from a chimney built low against wind. Instead, every cabbage leaf trembled though the air was still. Water stood in the furrows without reflecting the sky. The old road lay invisible beneath the soil, but Mara felt it before Tavi found it, a line of cinder-grit and crushed white stone running from nowhere toward nowhere, buried by harvests and forgetting.

The dead farmer was on his knees among the cabbages.

He had not come up like a ghoul from tavern stories. He had not clawed, roared, or hungered. He had risen carefully, as if ashamed of damaging the crop. Soil clung to his burial shirt. Worms shone in the lace of his cuffs. One side of his face had fallen inward, but the other still held the shape of a man who had smiled often before dying badly. His hands, black with earth, rested open on his thighs.

His living wife stood ten paces away with a shovel raised in both hands.

"Thom," she said, and the name broke on the last letter.

The corpse turned his remaining eye toward her.

"I was walking to market," he said.

His voice was not a rasp. That made it worse. It came out soft, confused, with the old county lilt of a man asking why the weather had turned.

Mara tasted ash.

Not furnace ash. Not the poisonous throat-scratch of Kell Ashgate. This was older, sea-salt and snowmelt and scales over stone, a dragon memory stretched thin beneath tilled earth. The cinders under the buried road were not whole organs, not named witnesses, only fragments swept into gravel centuries ago, but after the dragon-moon opened they had begun to remember function. Road. Passage. Return.

The dead had heard road and obeyed it by mistake.

Behind Mara, the farmer's daughter whispered, "Do something."

There it was. The shape the world kept trying to put in Mara's hands. Do something meant save him, kill him, command him, explain him, become large enough that everyone else could become small and frightened without guilt. Do something had followed her from Ashgate, through Lumenorath's beautiful cruelty, into Khar Veyl's sealed guilt, down to Orrowen's moon-chamber where every cinder woke.

Mara stepped into the field.

Caldus said, "Slowly."

"I know."

"I am saying it for myself."

That nearly steadied her. He came two steps behind, close enough to reach, far enough not to own her answer. Saelith moved to the widow's side, hands visible, not touching until invited. Ilyr murmured to the Orrowen dead in their own record-cadence. Tavi began sketching the buried road with colored pegs while muttering at cabbages that had chosen a very inconvenient morning to become evidence. Kesh vanished toward the hedges, because fear in a field often had witnesses hiding nearby. Brakka planted herself between the corpse and the lane where villagers had begun to gather with hooks, knives, and family names sharpened by terror.

Mara knelt in the mud before the dead farmer.

"What is your name?" she asked.

His gaze slid over her and past her. "Market by sun-height. Cabbage early. Lora hates late cabbage."

The widow made a sound as if struck.

Saelith did touch her then, two fingers on the sleeve, asking first with the gentleness of the gesture. The woman did not pull away.

Mara swallowed. "Sir, I need your name."

"Road's open," the dead man said. "Have to go while the toll is down."

Under the field, cinder-grit warmed.

Go, it remembered. Carry. Return. Bring goods. Bring bodies. Bring names. The old road had moved soldiers once, then refugees, then condemned dead when Harrowmere's first kings decided public graves made rebellion too easy. The cinders did not understand the difference. The dead farmer had been buried beside that road with a market token in his hand, and now the world had opened every wrong instruction at once.

Mara placed her palm on the mud.

Heat climbed into her bones. A hundred fragments sang at once, each too small to be a voice and too wounded to be quiet. She could command them. That frightened her because it was true. Ever since the moon-chamber, every cinder answered faster. The dead farmer's head tilted toward her hand. The old road leaned close, eager to be useful.

Useful was the oldest trap she knew.

"No," Mara said softly.

The cinder-grit flared.

The farmer's corpse shuddered. Brakka's maul rose. Caldus shifted his weight. The villagers gasped and tightened around their weapons.

Mara did not command the road to close. She did not order the dead back under soil. She pushed her own memory into the heat instead: Kell Ashgate pay yard, short wages, men with ledgers explaining that other people were numbers because numbers did not cough blood where noble boots could see; Joryn's hands cut from ore carts; Arveth saying the dead were not always wise, sometimes merely uninterrupted; Selli writing a title for Mara in pencil because permanent things needed humility.

Witness, she told the cinder-grit, not command.

The old road hesitated.

The dead farmer blinked.

"Thom Arlet," he said.

His wife dropped the shovel.

"Lora?" he asked.

The field did not become kind. Mara hated stories that did that. Thom Arlet was still dead. He still had earth in his mouth. His wife still stared at the ruin of a face she had mourned eleven years and wanted back with a desperation that could not be answered cleanly. Around the field, villagers lowered weapons by inches, not because they understood, but because a name had made murder harder.

Then the second corpse rose.

Not in the field. In the lane.

A woman in rusted mail sat up under the hedge where no grave marker had stood. Then a child with a clay whistle hanging from a cord around his neck pushed through the soil beside the cart track. Then five hands came through the cabbage rows, patient as roots. Across the lowland, from fields, ditches, forgotten plague pits, pauper mounds, and one decorative shrine where Harrowmere had pretended never to execute debtors, the dead began to answer roads, bells, coins, prayers, and old orders.

The villagers broke.

Brakka's roar held the lane for three breaths. That was enough for Caldus to step into the first rush, shield raised, blade flat. "Back from the field! Living to the west! Dead to the rows if they can hear me!"

"They cannot all hear you," Ilyr said.

"Then interpret!"

Ilyr did. Not with kindness alone. His voice cut through the panic in Khar Veyl's old command-register, then corrected itself into Orrowen public witness, then into trade cant Kesh had taught him badly enough that Kesh shouted from the hedge, "You just told them to pickle their grandmothers!"

"Then improve it!"

Kesh sprang onto a stone wall, cloak flaring. "All right, dead neighbors and miscellaneous legal disasters, listen if listening is among your remaining talents! If you know your name, say it. If you do not, sit down and stop being dramatic. If you are under orders from a dead king, that king is bankrupt."

It should not have worked.

Some of it did.

The dead with names stopped first. Not all. A mail-clad woman kept marching toward Harrowmere with sword drawn, repeating, "Gate by noon, prince by dusk," until Brakka met her in the lane and caught the sword on stone. A child crawled toward the sound of his own whistle and bit Saelith when she tried to help. Saelith did not cry out. She sang one broken hymn note, then another, not the Pale Bough's old obedience, but the corrected interval she had made in the moon-chamber, the sound of beauty refusing to become law.

The child stopped biting.

Tavi ran from peg to peg, throwing little brass anchors into the mud. "The road fragments are amplifying return instructions. I can dampen them if no one steps on my anchors, breathes on my anchors, prays near my anchors, or bleeds excessively within six feet of my anchors."

"So no one be alive near Tavi's anchors!" Kesh called.

"That is not what I said."

"It is what you meant emotionally."

A royal rider chose that moment to appear on the eastern track.

He came with six soldiers in Harrowmere blue, horses lathered, banner wrapped for speed. The captain took in the field, the risen dead, Mara in the mud, and the cinder light leaking between cabbage roots. His fear lasted only long enough to choose a mask.

"Mara Venn," he called. "By order of the regency council, you are required to present yourself and any active cinder faculty for emergency use."

Caldus went very still.

Mara rose. Mud streaked her trousers. Her hand smoked faintly where the cinder-grit had burned a line into her palm. Behind her, Thom Arlet stared at his wife as if memory were an injury he could not stop touching.

"Emergency use," Mara said.

The captain's horse backed from her voice.

"The dead are rising across the county," he said. "The council requires control capacity."

In the field, the dead waited badly. Some whispered names. Some wept without tears. Some repeated orders from wars that had been dust before Mara's grandmother was born. The living watched her with the same terrible hunger the captain carried, only less polished.

Mara understood the shape of the road ahead then, though she would not have called it prophecy. The world had not asked whether the dead were people or danger. It had decided they were crisis, and crisis made old tools look holy.

"No," she said.

The captain blinked. "You have not heard the terms."

"I heard use."

His hand moved toward his sword.

Caldus's blade cleared an inch.

Brakka smiled, not pleasantly.

The captain reconsidered the speed of politics.

Mara turned back to the field. "We start with names," she said, loud enough for living and dead. "Not commands. Names, witnesses, and safe ground. If Harrowmere wants help, it sends food, blankets, clerks, and anyone who can read old burial roads. If it wants a weapon, it can dig up its own courage and be disappointed."

No one cheered. The morning was not made for it. Too many dead stood in the cabbage rows. Too many living had heard beloved voices from ruined mouths. But Lora Arlet stepped into the mud, took her dead husband's soil-black hand, and said his name again.

Thom did not become alive.

He did become less lost.

That had to matter.

By noon, riders had gone in every direction. By dusk, smoke signals and bell codes stitched news across Vael Taryn. Corpses rose in daylight in river towns, mine roads, elf groves, gnome railbeds, goblin toll camps, troll bridge foundations, dragon-scarred beaches, and sealed courts that had believed stone could keep history asleep.

Mara stood at the edge of the field until her burned palm stopped shaking.

Under the earth, the cinders listened.

Not for orders.

That was the terror and the hope of it.

They listened for what people would dare to call each other now.""",
    2: r"""## Chapter 2: Kings Want Weapons

The council hall of Harrowmere had been designed by men who believed panic looked more respectable under painted ceilings.

Thirty-seven maps covered the long table. Some were official royal charts inked on vellum and weighted with silver. Some were market maps stolen from caravan masters. One had been drawn in jam on the back of a tax notice by a child who had seen her dead uncle walk out of a millpond and point toward the old plague road. Tavi liked that one best because, she said, the jam had chosen color coding with more honesty than the regency.

Heat curled the map edges. Not fire heat. Engine heat. Every messenger who entered carried a little cinder-lamp, a speaking coil, a sealed emergency token, or a pocket shrine gone hot with prayers. The hall smelled of wax, rain, horse sweat, wet wool, and rich people discovering that locks did not work on consequences.

Mara sat at the foot of the table because she refused the chair they had placed at its head.

The chair had belonged to Harrowmere's dead king. It had lion paws, a high carved back, and fresh cushions embroidered with a dragon eye that had not been there yesterday. Someone had worked fast. Someone always did when symbolism needed to become a leash.

Regent Halven Rook stood behind it with both hands resting on the wood, as if the chair could lend him a spine. Beside him waited envoys from three human crowns, two gnome syndicates, the corrected but still fractious Pale Bough, Khar Veyl's shadow embassy, the Kavik road clans, and a troll lawkeeper whose patience had already begun to damage the floor. Sava Rennet had claimed a clerk's stool and was writing minutes no one had authorized, which meant everyone kept speaking more carefully than they wanted.

Arveth's ledger lay open beside her.

The ink inside it had thinned overnight.

Mara tried not to look.

"The facts are plain," Regent Rook said.

"Suspicious beginning," Kesh murmured.

Rook ignored him with the discipline of a man saving all his hatred for the poor person at the end of the table. "The dead are rising across crown lands. Some are peaceful. Some are violent. Some are military remains still bound to obsolete orders. All active cinders appear unusually responsive to Mistress Venn. Therefore emergency centralization is necessary."

"There is the corpse under the clean floor," Tavi said.

The regent blinked. "Pardon?"

"Nothing. Continue dressing the trap."

One of the human envoys, Lady Merrow of Eastmere, leaned forward. Her veil was black for mourning and edged in pearls for influence. "No one here wishes to exploit you, Mistress Venn."

Caldus made a small sound.

Mara did not look at him because she might laugh and laughing in council halls made rulers feel endangered, which was accurate but inconvenient.

Lady Merrow pressed on. "But if you can still the risen until burial rolls are confirmed, thousands may be spared."

"Still them how?" Mara asked.

"Temporarily."

"That is not how."

The gnome syndicate factor adjusted her spectacles. Brass lenses clicked through six levels of magnification before settling on Mara's face. "A relay apparatus could be constructed from existing civic nodes. Nothing as crude as the destroyed Orrowen command engine, naturally. More transparent. Rotating oversight. Consent provisions where feasible."

"Where feasible," Tavi repeated. Her voice went flat enough to cut metal.

The factor had the decency to color. "In immediate danger, perfect consent may not be possible."

"Then perfect refusal remains possible," Tavi said.

Saelith stood at the window where rain silvered the glass. She had not sat since they entered. The light elves across the room kept watching her the way citizens watched a cracked bell: grieving the break, fearing the next ring, needing the sound anyway. Their leader, Auralian Thrice-Crowned, wore white bark armor over a robe deliberately left unhemmed. Some Pale Bough houses had accepted Saelith's correction after the moon-chamber. Some had only learned to say the right words while sharpening old obedience into thinner knives.

"Lumenorath requests lawful coordination," Auralian said. "If the dead are persons, they must be registered. If they are dangers, contained. If they are both, the law must hold both truths."

Ilyr laughed once.

The sound made every light elf look at him.

"Forgive me," he said, not sounding forgiven or seeking it. "My people built sealed law around that exact sentence and called the result virtue for six centuries."

Vaura Noct-Vey, dark-elf envoy and Ilyr's sister by blood if not by mercy, watched him from beneath a hood threaded with amethyst. Her presence in a Harrowmere council hall would have caused diplomatic fainting two months ago. Now the dead were rising and everyone had discovered flexible principles.

"Khar Veyl requests containment of military dead first," Vaura said. "Not for convenience. For survival. Armies from the Second Obsidian War are walking in both directions. Some will attack any light-elf hymn, any dark-elf shadow, any human banner, any goblin road mark. Their orders predate half our treaties."

"And who commands containment?" Mara asked.

Vaura met her eyes. "That is precisely the wound."

Brakka shifted behind Mara. The floorboards complained.

"The Seven Arches make no request for command," the troll lawkeeper said. His name was Durn of the Rain-Scarred Pier, and he had a voice like stones deciding to be patient one last time. "We require vows. Every road opened for refugees must remain open after fear passes. Every bridge used to move soldiers must carry the wounded and the dead by name. Every faction here will sign or be named oathless."

"Charming," Lady Merrow said.

Durn smiled. "You will like charming less."

Kesh tipped his chair back. "The Kavik roads require payment in advance, public apology for twelve generations of outlaw notices, and a guarantee that no royal office may seize a caravan because someone panicked and called navigation strategic."

"This is not a market," Regent Rook snapped.

"Everything is a market when kings arrive empty-handed," Kesh said. "Some of us learned that from kings."

Rook's face hardened. "Mistress Venn, while your companions posture, people die."

There it was again. Usefulness wrapped in blood.

Mara looked at the maps. The jam map had begun to dry. Red smears marked villages along an old plague road. On the official maps, those villages were tiny black dots, unnamed unless they paid enough tax to deserve ink. On Sava's minutes, every message had become a sentence with a subject. Widow requests witness at South Fen. Mill dead attacked toll gate after royal drums. Child reports uncle seeking debt office. Five miners risen in Kell Ashgate north shaft, no violence, asking whether shift ended.

Her throat tightened at Kell Ashgate.

"How many cinder relays remain in Harrowmere?" she asked.

Tavi answered before any official could lie. "Seven intact, nineteen partial, probably three hidden because nobles enjoy secret plumbing."

"Can they send witness registers instead of commands?"

The gnome factor frowned. "Registers are slower."

"That was not my question."

"Yes," Tavi said. "If rebuilt correctly. Local name intake, route reports, danger signals, burial-road maps, emergency shelter calls. No compulsion."

"Could they be converted back?"

Tavi's expression went unpleasant. "Not if I get to insult the architecture with tools."

"Good."

Regent Rook leaned over the table. "You cannot answer national catastrophe with clerk work."

Sava looked up. "Clerk work is what remains after heroic speeches stop bleeding on the paper."

Arveth's ledger flickered.

Mara saw a line form in the thinning ink: Correct.

Then it faded.

Ilyr saw it too. So did Maelin, standing by the door with one hand on her dark-elf blade, pretending she had not. The part of Arveth that remained with them had been strong in Orrowen, where records remembered him. Outside the dead city, copied witness thinned every day. Mara had not known whether to speak of it. Avoiding grief never stopped it from learning the route.

Lady Merrow removed a sealed paper from her sleeve. "Eastmere offers formal recognition of your authority over active cinder faculties."

Mara stared at the paper.

It had ribbons. It had wax. It had the kind of language that turned theft into ceremony.

"No."

"You have not read it."

"It begins with authority."

"Authority can protect."

"So can a locked door," Mara said. "Ask the people inside whether that makes it a home."

The room went silent enough for rain to speak.

Rook exhaled through his nose. "Then you refuse to help."

Mara stood.

She had been short all her life. Short girls learned the difference between height and presence early, mostly from being denied both. In Kell Ashgate, foremen had looked over her head while counting her wages. In Harrowmere, nobles had looked past her shoulder for whoever truly owned the room. In Lumenorath, beautiful people had tried to turn her into a symbol tall enough to kneel before. In Khar Veyl, sealed law had measured her usefulness against disaster. In Orrowen, the dead had nearly made her a bridge because bridges did not get to choose who crossed.

Now every envoy watched her as if waiting to learn which kind of tool she would agree to be.

"I will help," Mara said. "I will not rule the cinders. I will not still the dead for your convenience. I will not become an emergency crown because crowns are easier to salute than neighbors are to answer."

She touched the jam map.

"We start with local witness halls. Living and dead both named. Dangerous orders identified and unwound by mixed witness: family, clerks, soldiers, healers, anyone who knows the person under the order. Cinder relays carry warning, not command. Roads remain open under bridge law. Goblin caravans are paid. Gnome engines are audited by people who can say no. Elven law answers in public. Human crowns send grain before soldiers."

"And if violent dead attack?" Vaura asked.

"Then we fight them," Mara said. "As people who became danger, not objects that were always only danger."

Caldus's eyes closed briefly, not in pain. In recognition.

The door behind the regent opened.

A page entered, pale enough to make his freckles look painted. "My lord. The northern gate reports an armed company under old royal colors. Dead cavalry. They claim the king's evacuation order from the Red Fever year still stands."

Rook seized on it. "You see?"

Mara did.

She saw the trap and the need inside it. She saw frightened citizens at the gate, dead riders with an obsolete mercy order that would become massacre if left alone, envoys waiting for her refusal to curdle into blood they could spend against her. She saw that being right in a council hall meant very little if people died outside the doors.

"Caldus," she said.

"With you."

"Tavi, can you make the relay repeat names from the gate?"

"Yes, but I will need the regent's private cinder line."

Rook stiffened. "There is no private cinder line."

Tavi looked at the ceiling. "The chandelier disagrees."

Kesh laughed like a knife leaving a sheath.

Mara pointed at Rook. "Give her access. Saelith, Ilyr, Sava, with me. Vaura, if those riders know old military registers, I need your forbidden memory. Auralian, if your law can soothe obedience without enforcing it, prove it. Durn, hold the road."

Durn struck the floor with two knuckles. "Witnessed."

Lady Merrow rose. "And us?"

Mara looked at the human envoys. "Open your purses."

The northern gate became the first test of the new world and nearly failed in the first minute.

Dead cavalry stood beyond the portcullis in rain-polished armor, horses skeletal but proud, banners rotten and still bright where cinder light ran through the threads. Their captain had no lower jaw. He spoke through the trumpet at his saddle, each word blown in a brassy moan.

Evacuation by royal order. Civilians to be removed east. Resistance punishable by field necessity.

Behind the gate, Harrowmere citizens screamed that east was where the plague pits lay. Children cried. Soldiers raised pikes. Someone on the wall loosed an arrow too soon. It passed through a dead rider's throat and struck the horse behind, which reared without pain and began to charge.

Mara put her burned palm against the cinder relay Tavi had torn from the gatehouse wall.

"Names," she said.

The relay answered with heat.

Not command. Names.

Sava read from a fever-year register as Tavi shoved power through the line, and Ilyr cut away false duplicates with dark-elf precision. Saelith sang one note under the names, not compelling, only holding the sound open. Vaura found the old military order and spoke the missing clause Rook's archives had omitted: evacuation east until fever towers fall.

"The fever towers fell two hundred and twelve years ago," Sava cried.

Mara pushed the fact into the relay.

The dead cavalry captain lowered his trumpet.

Rain filled the silence.

Then, one by one, the dead riders turned their horses aside from the gate.

They did not vanish. They did not rest. They formed a line along the road and faced outward, guarding the evacuation they had misunderstood for two centuries.

Harrowmere did not cheer.

It breathed.

That was enough for the moment.

On the wall, Regent Rook looked at the dead cavalry, then at Mara.

His fear had changed clothes. It now wore calculation.

Mara saw it and felt tired all the way down.

"He will try again," Caldus said quietly.

"I know."

"They all will."

Below, the dead captain lifted his trumpet in salute, not to a queen, not to a weapon, but to a corrected order.

Mara's burned palm throbbed.

"Then we keep correcting them," she said.""",
    3: r"""## Chapter 3: The Pale Remnant

At the Lumenorath border, the trees were trying to decide whether they were allowed to be ugly.

Mara noticed because Saelith did. The light-elf groves had always unsettled Mara with their impossible poise: white trunks smooth as polished bone, leaves like panes of green glass, flowers opening in exact theological numbers along branches trained by centuries of hymncraft. Even fallen petals had once landed in pleasing spirals, as if beauty itself feared discipline.

Now the border looked alive in a less obedient way.

Roots broke through the tiled road at uneven intervals. Some trees leaned. One had split its trunk to grow around the skull of a risen stag, not hiding the skull, not displaying it, simply making room. New leaves came in mismatched shades of green, amber, blue, and a stubborn rusty red. A bough over the gate flowered on one side and shed bark on the other. It was the most beautiful thing Mara had seen in Lumenorath because it did not appear to be asking permission.

Saelith stood beneath it with her hands folded so tightly her knuckles shone.

"They will call it corruption," she said.

"Is it?"

"No." She breathed in. "That may be why they will hate it."

The corrected Pale Bough had sent for them at dawn with a message written on unhemmed cloth. Some houses of Lumenorath had accepted Saelith's public correction after the moon-chamber: beauty without consent was only polished force; mercy that required silence was not mercy; law could be holy only if it could be answered. Other houses had not accepted anything except the temporary wisdom of retreat.

Those houses called themselves the Pale Remnant.

They had taken three border shrines, two healer schools, and a grove where dead light-elf oathkeepers had risen still singing the old obedience hymns.

"How many inside?" Caldus asked.

Auralian Thrice-Crowned, who had ridden with them from Harrowmere wearing exhaustion like a second cloak, looked toward the gate. "Living? Perhaps forty. Dead? Nineteen confirmed, more if the ossuary beneath the roots opened. Sympathizers? Too many to count honestly. The Remnant offers certainty. We taught our people to crave it."

Ilyr adjusted the strap of his black blade. "Certainty is generous. It saves one the labor of noticing corpses."

The light-elf leader looked at him. "Khar Veyl sealed its corpses."

"Yes," Ilyr said. "We preferred tidy hypocrisy. Your court preferred singing."

"Enough," Saelith said.

Both elves stopped.

Mara hid a smile. Not because the quarrel was amusing. Because a month ago Saelith would have apologized for interrupting. Now she looked like someone discovering that anger could be a clean tool if washed after use.

Kesh returned from scouting by dropping out of a tree that had not appeared to contain him. "Bad news, worse news, and personally insulting news."

"Order them by how much running they require," Tavi said.

"Bad news: the Remnant has archers in the west gallery. Worse news: the old shrine bells are tied to a cinder-white root system, so if they ring the obedience hymn, the risen oathkeepers will attack anything unregistered. Personally insulting news: someone stole my trap and improved it."

Tavi's eyes lit. "Improved how?"

"Do not look delighted. It is my trap."

Brakka cracked her neck. "Can we enter without bell ringing?"

Kesh sighed. "We can enter without ringing the bells. The bells are another matter. Bells have opinions."

The gate opened before they chose a plan.

Three light elves emerged in white bark masks shaped like serene faces. Their robes were immaculate. Their hands were empty. Behind them, through the gate, Mara glimpsed a courtyard tiled in silver and green, its central fountain clogged with leaves that had been dyed white after falling. On the far wall, dead oathkeepers stood in a row, translucent armor shining, mouths open in silent hymn.

The masked elf in the center bowed to Saelith.

"Dawnmere," she said. "You have been missed in the shape you abandoned."

Saelith's mouth tightened. "My name remains Saelith."

"Names remain. Duties do not always survive disgrace."

"Duties that require lies deserve funeral rites."

The masked elf inclined her head, as if receiving a clever child. "You have learned human bluntness."

Mara stepped forward. "I promise we teach worse."

The mask turned toward her. "Mara Venn. Traveling witness, subject to correction. The title is inelegant."

"It fits."

"It is temporary."

"So are masks."

For the first time, the elf's stillness flickered.

Auralian spoke. "Open the healer school. Release the risen oathkeepers from old hymn register. Submit your dispute to mixed witness."

"Mixed witness," the masked elf repeated. "A phrase for letting grief vote against order."

"Yes," Ilyr said. "Democracy does produce noise. One survives."

The elf ignored him. "We offer a cleaner solution. The dead are rising because the world's hidden disobediences have been forced into daylight. Restore the lawful hymn. Restore Serathiel's mercy. Restore ranks. Restore the beautiful chain before terror teaches every lesser will to call itself sacred."

Saelith went white.

Mara felt the cinder under the gate respond to the words. Not because they were true. Because they were shaped like old command. Cinders did not hear morality first. They heard structure, pressure, need. The Pale Remnant had built its whole theology to resemble a hand closing around a throat while calling itself comfort.

"Serathiel fell," Saelith said. Her voice shook once, then steadied. "I saw him try to cleanse Orrowen rather than hear it. I saw him call love what would have erased the dead. You know this."

"We know you stood beside enemies while a holy man was humiliated."

"I stood beside persons while a powerful man was corrected."

The shrine bells rang.

Not loudly. That was the horror of it. One clear note, then another, gentle enough for a nursery. The dead oathkeepers behind the gate opened their eyes. White roots under the road lit from within. The uneven trees shuddered, and their new red leaves curled as if ashamed.

Kesh swore. "My trap would never have chosen that key."

The dead oathkeepers began to sing.

Every living light elf in the courtyard lowered their head. Auralian staggered. Saelith clapped both hands over her ears. The hymn slipped through fingers, bone, memory, training. Mara heard no words, only a shape: kneel because kneeling is safe, obey because obedience is beautiful, be relieved of yourself because yourself is how cruelty enters the world.

Beside her, Caldus sank to one knee.

"No," he ground out.

The hymn had found his old oath scars.

Mara reached for him. Her hand stopped before touching. Command would be easy. Burn the cinder root. Silence the dead. Shatter the bells. She could do it now. That was the worst discovery since the moon-chamber: not that power tempted because it lied, but because it often told the truth about what it could prevent.

Saelith moved first.

She walked through the hymn.

Each step hurt her. Mara saw it in the tremor of her shoulders, the way blood threaded from one nostril, the way her lips formed old responses and then refused to speak them. The dead oathkeepers turned toward her, faces bright with the relief of command. The masked elves stepped aside, not from mercy, but from certainty. They believed the hymn would either reclaim her or condemn her.

Saelith stopped beneath the first shrine bell.

She looked back at Mara, not asking to be saved. Asking to be witnessed.

Mara nodded.

Saelith sang one wrong note.

It cracked the air.

The old hymn stumbled. The dead oathkeepers faltered like dancers whose music had lost a beat. Saelith sang again, placing the corrected interval from the dragon-moon chamber where obedience expected a perfect fall. The note was not pretty. It wavered. It scraped. It carried grief, anger, embarrassment, and an untrained human roughness she had borrowed from too many campfire songs with Kesh and Tavi.

The Remnant recoiled as if she had spat on an altar.

"You profane the mercy canticle," the masked elf hissed.

Saelith's voice rose.

The white roots under the road split.

From beneath them came the dead who had not been allowed into the official hymn: kitchen servants buried without white linen, dark-elf prisoners executed under diplomatic silence, human nurses who had died in Lumenorath plague wards and been called unfortunate necessities, goblin guides paid in exposure, a troll mason whose bridge-vow had been edited out because a beautiful arch looked better without foreign names carved at its base.

They did not attack.

They answered the missing note.

The courtyard filled with a choir no doctrine had rehearsed.

Caldus rose.

"Now?" Brakka asked.

"Now," Mara said.

The fight was a mess, which made it honest. Caldus broke the first shield line with the flat of his sword. Brakka caught a dead oathkeeper's spear under one arm and threw the warrior into a fountain hard enough to make dyed leaves explode like startled birds. Ilyr cut bell ropes by shadow rather than blade, each severed cord releasing a shriek of stored command. Tavi climbed the gate mechanism with a wrench in her teeth and a philosophical hatred for decorative access panels. Kesh found the person operating his stolen trap, apologized to himself for what he was about to do to such promising talent, and dropped the saboteur into a hedge that immediately began arguing.

Mara did not stand apart.

An oathkeeper came for Saelith while she sang, sword raised in both spectral hands. Mara met him with the short blade Caldus had made her practice until she cursed him fluently. The sword passed through her guard cold as moonwater and kissed her shoulder with dead pain. Her knees buckled. The cinder root beneath the gate offered itself.

Command him, it whispered in heat. Stop the danger.

Mara gripped her blade until her burned palm opened.

"Name," she said to the oathkeeper.

He struck again.

She caught the blow badly. Pain flashed white. "Name."

"Captain Elion of the Third Radiance," he said, and the sword halted an inch from her throat.

"What was your last order?"

"Preserve mercy."

"Who gave it?"

His mouth opened.

The hymn tried to fill it.

Saelith's rough note cut through.

Elion looked at the masked Remnant, then at the dead servants singing from beneath the roots, then at Mara bleeding in the road. "I do not remember mercy needing so many graves."

His sword lowered.

By sunset, the Pale Remnant had lost the border shrine, the healer school, and the comforting fiction that its beauty had been unanimous. The masked leader escaped west with a dozen followers and three dead oathkeepers still bound to the old hymn. That mattered. Mara would not let victory sand its own edges smooth.

Saelith sat on the cracked tiled road while healers tended the bitten and the bleeding. Red leaves drifted into her lap. One stuck in the blood beneath her nose.

"I made it ugly," she said.

Mara sat beside her. "You made it answerable."

"That is not the same as saved."

"No."

"Good." Saelith closed her eyes. "I am tired of saved things that cannot breathe."

Across the courtyard, Auralian and Ilyr carved names into the base of the beautiful arch while the dead corrected spelling. Brakka supervised with the air of a person willing to make grammar a physical issue. Kesh negotiated hazard pay for having his trap plagiarized. Tavi insisted on examining the stolen improvements while pretending she was not impressed.

Saelith leaned her shoulder against Mara's, light as a question.

Mara let the answer be weight.

Behind the border shrine, the uneven trees kept growing in all their unapproved directions.""",
    4: r"""## Chapter 4: The Open Archive

The Orrowen archive had been moved into a Harrowmere warehouse because no one trusted a dead city to keep its own secrets anymore.

This was unfair to Orrowen, Sava said, and also accurate.

The warehouse stood beside the canal where grain barges once unloaded under tax lanterns. Now its doors were guarded by Harrowmere soldiers, Khar Veyl shadows, Lumenorath oathkeepers with corrected hymn marks painted on their wrists, goblin caravan watchers, three troll vow-judges, and a line of citizens who had come to ask whether the newly risen dead in their homes were ancestors, criminals, soldiers, debtors, saints, accidents, or all of those at once.

Inside, records covered everything.

They hung from rafters in scroll nets. They filled barrels, crates, bread racks, borrowed chapel pews, and a bathtub someone had labeled URGENT MARRIAGE CONTRADICTIONS. Ghost-ink glowed along the walls. Dead clerks moved through the aisles with the grim joy of people who had been proven necessary during catastrophe. Living clerks followed with ink-stained hands and the hunted eyes of scholars who had slept in chairs for three days.

Mara loved and feared the place immediately.

It smelled like dust, wet rope, old glue, lamp oil, and the particular panic of truth becoming public before anyone had built enough tables.

"No," Sava said to a nobleman attempting to enter through the side door. "You may not have your grandfather's treason sealed for morale."

"It will destabilize three counties."

"Then three counties have been balancing on garbage."

"Do you know who I am?"

Sava dipped her pen. "A man delaying the line."

Arveth's ledger rested beside her elbow, open to a page where thin writing came and went like breath on glass.

Mara had begun to measure days by how long the writing lasted.

Today, the ink formed only fragments.

Standing. Correction. Objection. Tea?

Sava saw Mara looking. Her face softened in the exact amount she would have denied if accused. "He is stronger near Orrowen records. We have most of them here."

"Most."

"A dangerous word, but the best one I have."

Ilyr stood at the central sorting table with Maelin and Vaura. The three dark elves formed a triangle of family, exile, and state interest sharp enough to cut anyone foolish enough to call it reconciliation. Before them lay the full record Ilyr had opened in the moon-chamber: the double crime of Lumenorath and Khar Veyl, dragon-moon burial, shared concealments, edited martyrdoms, erased witnesses, names of those who had profited, names of those who had objected and been sealed.

People kept trying to steal it.

Not dramatically. No assassin had rappelled from the rafters, though Kesh claimed this was because the rafters lacked ambition. Instead, theft came as requests for responsible delay, partial release, diplomatic sequencing, public safety review, sacred privacy, national security, and one gnome proposal for an index so complicated no ordinary citizen could possibly use it, which was theft wearing spectacles.

"We publish the whole thing," Maelin said.

"We publish it in forms people can survive reading," Ilyr answered.

Vaura's laugh was quiet and bitter. "Listen to exile discover governance."

Ilyr did not flinch. "Listen to government discover confession."

Mara expected Maelin to smile. She did not. Book Two had left wounds too raw for easy satisfaction. Maelin had stood in Khar Veyl's sealed chamber and watched the state she had served become indictable in its own hand. Vaura had entered culpability without surrendering the habits that made culpability necessary. Ilyr had returned not as a forgiven son but as an opened door everyone blamed for the weather.

The archive made them work together anyway.

That was one of truth's less poetic virtues.

Tavi hauled a cinder relay casing onto the table and dumped out three illegal listening charms, two dead beetles, and a folded note that read, in excellent handwriting, Delay dragon names until after military stabilization.

"Who put this in my casing?" she demanded.

Every official in the warehouse found something else to study.

Kesh plucked up the note. "No signature. Good paper. Smells like lavender, fear, and a very expensive education."

Lady Merrow, across the aisle, said, "Many people use lavender."

"And yet my nose points socially."

Mara took the note.

The words dragon names made her burned palm ache.

Not every truth could be released the same way. That was the knife hidden under the archive's feast. The names of dragon cinders had power. The names of buried crimes had power. The names of risen dead restored personhood, but a name spoken into the wrong engine could become a handle. Secrecy had built the old world. Reckless openness could arm the new terror before people knew what they held.

Mara hated that because it sounded like the arguments of everyone she distrusted.

"We need rules," she said.

Sava looked up. "Careful. That is how clerks reproduce."

"Answerable rules."

"Slightly better offspring."

They gathered by the canal doors: Mara, Sava, Ilyr, Maelin, Vaura, Saelith, Tavi, Kesh, Brakka, Caldus, Auralian, Durn, and three citizens chosen by the line outside because Sava had announced that anyone who made archive policy without people actually waiting for records would be publicly mocked in the minutes. The citizens were Lora Arlet, whose dead husband now sat in a witness tent learning which memories were his and which belonged to the buried road; a miller named Jonn who wanted to know whether his risen aunt had been a debtor or a spy; and a young Harrowmere soldier whose brother was among the dead cavalry holding the north road.

"No dragon organ names in public copies," Tavi said. "Not while relay sabotage remains this easy."

"No sealed copies without mixed witness," Ilyr said.

"No state-only index," Maelin added, surprising Vaura enough to make her turn.

Maelin's jaw flexed. "If my people need truth, they need access not curated shame."

"Redactions must be named," Sava said. "A covered line gets a reason, a signer, a review time, and a person who can challenge it."

"Dead can challenge," Lora said.

Everyone looked at her.

She lifted her chin. "If my Thom is enough person to frighten the council, he is enough person to object."

Brakka struck her fist into her palm. "Witnessed."

The first riot began four minutes after the policy was read.

It began, as riots often did, with a man who said he was being reasonable.

His name was Lord Pellan Harrow, and he had discovered that three of his estates were built on confiscated plague graves whose dead had started walking toward the front doors. He wanted the confiscation rolls delayed. The citizens outside wanted them read aloud. Pellan called this inflammatory. A dead laundress called it Tuesday. Someone threw a stone. Someone else threw a ledger, which Sava later described as thematically stronger but physically regrettable.

Then the warehouse bells rang with an alarm no one had installed.

Cinder light flared in the bathtub of marriage contradictions.

Tavi yelled, "That is never a good sign!"

The ghost-ink on the walls began rearranging into a dragon name.

Mara felt it before she saw it. The first syllable crawled across the warehouse like lightning under skin. Every cinder-lamp bent toward it. The dead clerks froze. The living clerks dropped pens. Outside, the risen cavalry horses screamed without throats.

Someone had planted a name-seed in the archive.

Not enough to summon a dragon. Enough to make every cinder relay in Harrowmere turn its attention toward the warehouse and wait for the rest.

"Cover it!" Vaura shouted.

"With what?" Tavi snapped. "A blanket? A strongly worded ethical objection?"

Saelith began to sing the corrected interval, but the name was not obedience. It was hunger for completion. Ilyr and Maelin threw shadow across the wall, cutting off two strokes. Auralian pulled light into a lattice. The dragon name burned through both, not malicious, merely older than their tools.

Mara stepped toward it.

Caldus caught her wrist. "Do not become the plug in another engine."

"I am not."

"Say how."

That was why she trusted him. He did not stop at faith when method could save her.

Mara looked at the wall, the living, the dead, the officials, the citizens, the hidden thieves, the frightened people who wanted truth, and the equally frightened people who wanted truth delayed until it became another locked room. The name-seed wanted completion. It wanted everyone to lean toward a single secret.

So Mara made the room speak many truths at once.

"Read," she said.

Sava understood first. "All clerks! Active files! Names only, no seals! Begin!"

The warehouse erupted.

Dead clerks called names from plague rolls. Living clerks shouted confiscations, marriages, military orders, bridge vows, burial roads, tax lies, orphan ledgers, kitchen rosters, execution stays. Lora Arlet read Thom's market license. The miller read his aunt's debt appeal. The soldier read his brother's fever-year enlistment. Ilyr read Khar Veyl's culpability. Auralian read Lumenorath's. Kesh read a list of unpaid goblin invoices with theatrical injury. Brakka read bridge names in a voice that made the rafters listen.

Mara laid her burned palm against the wall.

The dragon name faltered, not because it was overpowered, but because it was no longer the only shape in the room.

Witness crowded command.

The name-seed split into harmless ash.

For one breath, the warehouse held.

Then Lord Pellan tried to run.

The dead laundress tripped him with admirable civic timing.

By evening, the archive had a new rule carved above the canal doors in three scripts and one goblin pictogram Kesh insisted was legally binding: Truth must be carried by more than one hand.

Mara stood beneath it with ink on her sleeve and ash under her nails.

Arveth's ledger flickered.

Good, the page wrote.

Then, after a pause:

More tea.

Sava pressed her lips together until the smile became official misconduct.

Mara laughed, and for one small moment in the warehouse full of public ruin, the sound did not feel stolen from grief.""",
    5: r"""## Chapter 5: Caravans of the Unburied

The caravan left Harrowmere at dawn with three hundred living, eighty-two dead, nineteen wagons, seven goats, one offended rooster, and a written agreement that Kesh described as "almost insulting enough to trust."

It was not an army. Mara kept saying that because everyone else kept looking at it and seeing one. Armies had banners. This caravan had laundry lines strung between wagons. Armies had drums. This caravan had babies crying, axles squealing, dead cavalry riding the rear guard under corrected fever orders, and Tavi's rooster declaring war on sunrise from a crate labeled DELICATE RELAY COMPONENTS. Armies marched to take ground. This caravan moved because staying had become another way to die.

The unburied came in many kinds.

Some were dead whose graves had opened and whose families had chosen to travel with them until name, memory, danger, and consent could be sorted somewhere safer than a cabbage field. Some were living refugees whose homes now stood on awakening roads. Some were Orrowen citizens who had never been buried properly because their city had mistaken legal persistence for civilization. Some were soldiers under obsolete orders. Some were people like Thom Arlet, who remembered loving his wife more clearly than dying and wanted to know whether wanting made him monstrous.

Mara walked near the middle because Kesh said important people belonged neither in front where archers expected them nor in back where guilt could collect.

"I am not important people," she said.

"Correct. You are important problem. Different rates."

He had negotiated those rates from the human envoys with the tenderness of a butcher selecting knives. Grain, coin, road indemnity, public revocation of six outlaw notices, and safe passage tokens stamped in full view of troll witnesses. When Regent Rook tried to add an emergency seizure clause, Brakka leaned both hands on the table and asked whether Harrowmere wished to be oathless before the Seven Arches by breakfast. The clause vanished.

Now Brakka walked ahead with Durn, setting bridge-law markers at each fork. Caldus trained a rotating watch of villagers, clerks, dead cavalry, and two embarrassed nobles whose purses had been judged insufficiently open. Saelith moved from wagon to wagon, tending bites, fear-fevers, and the delicate injury of families who did not know whether touching the dead was comfort or trespass. Ilyr and Maelin catalogued risen orders. Sava rode in the third wagon surrounded by records, slapping hands away from damp ink with priestly ferocity.

Arveth's ledger rested in Mara's satchel.

It had written nothing since they left the archive.

The road eastward ran through wheat country first. In another year, it might have been beautiful. Gold fields under a blue morning, wind combing the grain, little shrines at crossroads, scarecrows wearing old hats. Now the scarecrows turned their sackcloth heads as the caravan passed because cinder-grit in their stuffing remembered watch duty. Dead hands stuck from ditch banks like pale roots. Once, a whole line of skeletons rose under the wheat and walked in formation without disturbing the stalks, harvest shining through their ribs.

The living children stopped crying to stare.

Tavi stared too. "That is structurally inconsiderate."

"What is?" Mara asked.

"Being dramatic without breaking the crop. Sets unrealistic engineering expectations."

Near midday, they reached a toll village called Brindle Ford and found the bridge closed.

The bridge itself was a narrow stone span over brown floodwater, old enough to have troll marks under the moss and new enough to have Harrowmere toll spikes hammered along the rail. Twenty villagers stood before it with farm tools. Behind them, on the bridge, knelt a dozen dead in water-rotted clothes, hands bound with blue ribbon. Their mouths had been sewn shut.

Mara's caravan stopped.

Kesh's humor disappeared.

"Corpse-hunters," he said.

The village headman stepped forward. He was a broad man with red cheeks and a butcher's apron. "No dead cross. We heard what travels with you. We do not want it."

Brakka looked at the bound dead. "Then why keep those?"

The headman swallowed. "Protection."

"From?"

"Other dead."

Sava climbed down from her wagon so fast three clerks tried to catch the records instead of her. "You sewed their mouths."

"They were making people afraid."

One of the bound dead lifted her face. She had been a young woman once. River weed tangled in her hair. Her eyes burned with awareness and terror.

Mara felt the old, ugly arithmetic snap into place. Use the dead to guard against the dead. Silence them so their personhood did not complicate the arrangement. Call it protection. Charge toll.

The headman pointed at the caravan. "We are not cruel. We are practical. The blue ribbon keeps them from biting. The bridge stays safe. Travelers pay. Everyone lives."

"Except them," Saelith said.

"They are already dead."

Thom Arlet, standing beside Lora with a cloth over the ruined half of his face, spoke for the first time since morning. "That does not seem to stop hurt."

The villagers recoiled from his voice.

Caldus stepped in front of him without making it look like a threat, which of course made it more effective. "Open the bridge."

"No."

The dead cavalry at the rear shifted. Old horse bones clicked. The caravan tensed, living and dead together, fear seeking the quickest weapon.

Mara raised her hand.

She wanted to burn the ribbons. She could feel the cinder under the bridge, a thin road-spark trapped in the keystone, eager to carry force from her palm into stone, stone into ribbon, ribbon into ash. It would be just. It would also tell every frightened villager that the woman with cinder-burned hands had come to loose dead things on them by power alone.

She looked at Brakka.

"Whose bridge?" Mara asked.

Brakka's slow smile returned. "Excellent question."

Durn knelt by the first mossy stone and scraped away mud with one thumb. Old troll script emerged, deep and patient.

"Third Arch foundation law," he said. "Refuge crossing. No toll under flood, fire, war, plague, famine, exile, or return of wronged dead."

The headman went pale. "That mark is old."

"So is law when it is kept."

"Harrowmere granted toll rights."

Brakka walked to the toll spikes and closed one hand around the nearest iron point. "Harrowmere does not own old refuge."

She pulled.

Iron screamed out of stone.

That was when the corpse-hunters attacked from the mill.

They came with hooked poles, blue ribbon nets, and little cinder lanterns hooded in iron. Not villagers. Professionals. Men and women in boiled leather, faces smeared with ash to confuse the dead, moving with practiced efficiency toward the unburied in Mara's caravan. One net flew toward Thom. Another toward the dead cavalry captain. A hooked pole caught the river-dead woman by the throat and dragged her sideways.

Caldus shouted positions.

The caravan became chaos with training inside it. Villagers screamed and scattered. The dead cavalry wheeled without charging the living. That restraint mattered and nearly killed them. Corpse-hunters knew how to exploit dead hesitation. One drove an iron spike into a cavalry horse's skull and pinned it to the bridge rail while another opened a lantern toward the captain's chest.

Mara ran for the bound dead on the bridge.

Saelith reached them first. She took a knife to the arm cutting the first mouth stitch, then sang pain into steadiness while blood ran down her sleeve. The river-dead woman gasped when the last thread parted.

"Name," Saelith said.

"Nera Bell," the dead woman answered, voice torn. "Washer at south ford. Drowned in tax flood. They sold my arms after."

Brakka heard.

The bridge heard.

Every refuge mark under the moss lit blue.

Kesh hit the corpse-hunter leader from above, because apparently the mill roof had looked lonely. They tumbled into flour dust. "No one steals bodies on my road," Kesh snapped.

"Your road?" the leader spat.

"I am expanding emotionally."

Tavi lobbed a device into the nearest blue ribbon net. "Do not breathe near that!"

"What is it?" shouted a villager.

"A legal argument with shrapnel!"

It burst in a cloud of brass filings and vinegar steam. The net collapsed. The rooster, freed by either accident or ideology, charged through the steam and attacked a corpse-hunter's boot with magnificent irrelevance.

Mara reached the keystone.

The cinder under it surged. Refuge. Crossing. Toll. Return. Its old troll law and Harrowmere spikes and corpse-hunter lanterns tangled into a knot hot enough to blister the air. She could break it. Instead she pressed both palms to the stone and spoke names as they came: Nera Bell. Thom Arlet. Captain Osen of the fever road. Lora living witness. Brindle Ford old refuge. Third Arch foundation. Caravan under oath.

The bridge answered in stone, not command.

It lifted.

Not far. Not magically into the sky like a bard's nonsense. The span flexed, ancient trollwork straightening beneath later human iron. Toll spikes snapped. Blue ribbons burned away from dead mouths. The floodwater below roared as if glad to have been included.

The corpse-hunters broke.

Some ran. Some were caught by villagers who had realized, too late but not never, what protection had cost. Caldus disarmed three. Brakka held two by their collars over the river until they became eager to discuss restorative justice. Kesh found the leader's account book and read payment names aloud while Sava wrote them down with the expression of a woman buttering bread for an executioner.

By evening, Brindle Ford had become the caravan's first true witness camp.

The villagers cut stitches from the dead. The dead spoke. Not all kindly. One named the headman's brother as the man who sold her wedding ring. Another named herself and asked only to sit by the water until she decided whether rest was possible. The headman gave up the toll chest under Durn's supervision. It went to food, bandages, bridge repair, and payment for the Kavik road according to Kesh's aggressively annotated schedule.

Mara sat on the bridge rail as twilight purpled the flood.

Kesh climbed up beside her and offered a strip of dried pear.

"You called it your road," she said.

"Temporary madness."

"Sounded permanent."

"That is how they get you."

They watched Nera Bell walk across the bridge with Saelith beside her, each step a decision.

"I sold a road once," Kesh said.

Mara looked at him.

He kept his eyes on the river. "Not this one. Another. Information. Safer route for my caravan, worse route for someone else's. I have told you pieces."

"I know."

"The road is rude. It keeps collecting consequences."

"Yes."

"I may have to pay some old accounts before the Storm Isles."

Mara accepted the pear. It tasted of smoke and sugar. "We all are."

Behind them, the caravan settled around cookfires, living and dead sharing heat neither side fully understood. The bridge marks glowed until moonrise.

For the first time since the corpses rose, the road ahead looked less like flight and more like a promise with sore feet.""",
    6: r"""## Chapter 6: Third Arch Refuge

Third Arch did not rise out of the mountains so much as argue with them until they made room.

The refuge stood where three ravines met under a sky bruised by permanent storm. Ancient troll bridges crossed the empty air in stacked spans, some wide enough for wagons, some narrow as a held breath. Stone houses clung to cliff faces. Waterfalls dropped through gaps in the city and vanished into mist before sound found bottom. Prayer ropes, laundry lines, law knots, and children's carved charms hung from every rail. The whole place smelled of rain, iron lichen, woodsmoke, wet wool, and bread so dense it seemed to have legal standing.

Mara arrived soaked, exhausted, and carrying a dead child's clay whistle in her pocket because the child had finally remembered his mother lived near the Arches and then forgotten how to be brave about finding her.

The caravan stopped at the first bridge gate.

Brakka walked alone to the threshold.

Trolls waited there in gray mantles, faces weathered as cliff walls. Some were taller than Brakka. Some were bent with age. One had moss braided into her beard and a silver hook where her left hand should have been. All of them watched Brakka with the particular severity of family deciding whether love would be allowed to wear disappointment.

"Brakka of Third Arch," said the silver-hooked elder.

Brakka bowed. "Elder Morn."

"You return under broken clan standing."

"I return under refugee law."

"You bring dead across living bridges."

"I bring persons across refuge bridges."

A murmur moved through the gate trolls.

The child beside Mara clutched her sleeve with fingers that felt like cool smoke.

Elder Morn's eyes moved to the caravan: living villagers, Orrowen dead, Harrowmere cavalry, Kesh's road guards, Saelith's wounded, Tavi's rattling wagons, Sava's record crates, nobles pretending they had chosen hardship, goats eating a border shrub with treasonous focus.

"You bring a city," Morn said.

Brakka looked back once.

"Not yet," she said. "But perhaps the beginning of one that knows when it is being carried."

Morn's hook tapped the gate stone.

"Bridge asks vow."

This was why Mara had come to both love and fear troll law. It did not flatter. It did not hurry. It waited at thresholds and asked what weight a person intended to become.

Brakka turned to the caravan. "Those who cross Third Arch Refuge must speak one thing they will not take from those already afraid."

"That will take hours," Regent Rook's nephew complained from a wagon.

Morn's hook pointed at him. "Then begin with patience."

They did.

Not well. Not nobly. Some people muttered. Some cried. Some tried to make their vow clever until Brakka stared the cleverness out of them. The living promised not to take names, food, blankets, shelter, silence, grief, or the right to be frightened. The dead promised not to take warmth, bodies, obedience, old rank, or the road from those not ready to walk beside them. The dead child, whose name was Pell, promised not to take his mother's choice if she feared him.

Mara nearly broke at that.

When her turn came, rain ran from her hair into her eyes.

"I will not take refusal as betrayal," she said.

Caldus looked at her.

Saelith did too.

Brakka nodded once. Morn struck the gate stone, and Third Arch opened.

Inside, refuge was not soft.

It was organized because mercy without organization became a pile of good intentions and wet blankets. Troll cooks sent wagons to different ovens by need. Dead with unstable orders went to the lower echo courts where names could be tested safely. Living families went to cliff houses with colored door knots. Wounded to steam rooms. Dangerous relics to locked cisterns. Nobles to latrine duty, after a brisk legal clarification that rank was not a medical condition.

Tavi fell in love immediately.

"They have pulley kitchens," she said, staring at a network of baskets, ropes, counterweights, and soup cauldrons moving between levels. "Pulley kitchens with redundant brake systems. Mara, if I die here, bury me in a dumbwaiter."

"No one is dying in a dumbwaiter," Mara said.

"You cannot know that. The world is vast."

Kesh was less charmed. Goblins and trolls had old road debts, some honorable, some bloody, most involving bridges, tolls, and whose ancestor had technically cheated first. He spent the afternoon in a negotiation room with Durn and four Kavik elders who had arrived by a rope path no map admitted. When he emerged, he looked as if he had swallowed a contract and it was still fighting.

"Good news," he told Mara. "The roads may cooperate."

"Bad news?"

"I may have agreed to be publicly honest."

"That sounds terrible."

"I know. Send fruit."

The first attack came from below at dusk.

No enemy army climbed the ravine. No Pale Remnant hymn drifted on the rain. Instead, the bridges began to remember everyone who had ever died falling from them.

Mist thickened beneath the spans. Shapes formed in it: workers whose ropes snapped, children lost in storm, criminals thrown before the old reforms, soldiers who cut bridge lines rather than let refugees cross, one troll ancestor so ashamed of his cowardice that his memory had fossilized into the foundation stones. The dragon-moon's opening had woken not only cinders, but the old grief held by places built to carry lives over emptiness.

Third Arch groaned.

Every bridge in the refuge tightened.

People screamed as railings twisted inward, not attacking, remembering impact. A lower span cracked. Wagons slid. The dead cavalry horses reared. Pell's whistle shrilled in Mara's pocket though no breath touched it.

Brakka ran for the central arch.

Elder Morn caught her arm. "You cannot vow for every stone."

"I can remind them who they are."

"That is different."

"I know."

Brakka climbed onto the rain-slick rail of the central span while the whole city swayed over mist. Mara followed because apparently wisdom had been delayed by weather. Caldus shouted her name and came after. Saelith, Ilyr, Tavi, Kesh, Durn, and half the caravan ended up doing something dangerous in a pattern that suggested friendship was an incurable tactical condition.

At the arch crown, the stone roared with old falls.

Mara dropped to her knees and pressed her burned palm against it. The grief here was not cinder alone. It was troll work, human panic, goblin bargaining, elf exile, gnome miscalculation, dead weight, living hands. It had no single name, and therefore no single command could hold it.

"Brakka!" she shouted over the storm. "Bridge law is yours!"

Brakka stood above her, rain streaming down her tusked face, maul planted between her feet.

"Third Arch!" she bellowed. "Name your carried!"

The bridge answered by nearly throwing them off.

Mara's hand skidded. Caldus caught her belt. Kesh caught Caldus's cloak. Tavi caught Kesh and immediately regretted all known physics. Saelith's hymn-thread wrapped around the rail. Ilyr drove a shadow blade into a crack and held it open. Durn and Morn began speaking names from opposite ends of the span, their voices deep enough to reach stone memory.

Brakka did not repeat the command.

She changed it.

"Third Arch," she said, lower now, every word shaped with the care of someone lifting a wounded body. "We failed some. We carried many. We name both. We do not become only the fall."

The bridge groaned.

Mara felt the hinge. Places, like people, could become trapped in their worst memory. A bridge that remembered only falling would tighten until no one crossed. A world that remembered only betrayal would choose stillness and call it mercy.

Vorrakai's argument moved under the storm like a sleeping whale.

No more falling, it seemed to say. No more choice. No more bridges to break.

Mara almost understood.

That frightened her worse than hatred would have.

She pushed back not with denial, but with names. She gave the arch Pell's promise. Nera Bell's first free step. Thom Arlet holding Lora's hand without taking her answer. The dead cavalry turning outward. Saelith's ugly note. Sava's door rule. Kesh calling a road his. Caldus catching her belt because he had stopped using vows as excuses to die. Brakka returning broken and still carrying.

The bridge shuddered.

Then every prayer rope along Third Arch began to ring in the rain.

Not bells. Knots striking stone, wood, bone, metal, each tiny sound a life carried at least once. The mist below thinned. The falling dead did not vanish. They rose along the ravine walls as pale figures and placed their hands on the bridges from beneath.

Holding, not dragging.

At dawn, Third Arch Refuge declared a new law.

Refuge belonged not to the innocent, because innocence was too fragile a gate, nor to the useful, because usefulness was a hungry god, nor to the living alone, because the dead had been made homeless by living cowardice. Refuge belonged to the named who came without taking another's name.

Brakka carved the first mark herself.

Elder Morn watched, then placed her silver hook over Brakka's hand and drove the chisel deeper.

"Broken standing amended," Morn said.

Brakka blinked rain from her eyes. "Restored?"

"No. Amended. Restoration pretends the break taught nothing."

Brakka bowed her head.

Mara stood beside her on the new-carved bridge while the caravan prepared to move toward the storm roads. For one morning, at least, the dead and living ate dense troll bread under the same dripping awnings and complained about it with equal sincerity.

That, Mara thought, might be civilization in its earliest edible form.""",
    7: r"""## Chapter 7: Arveth's Fading Name

Arveth began disappearing during breakfast.

At first, Mara thought the rain had blurred the ledger ink. Third Arch mornings came wrapped in mist, and every surface sweated. The refuge cooks had given her a bowl of barley, mushrooms, and something Kesh identified as "troll cheese by legal definition only." She set the ledger beside the bowl, as she had every morning since the archive, waiting for Arveth's usual complaint about porridge, weather, clerical standards, or the metaphysical indignity of being transported in a satchel.

The page remained blank.

Then, slowly, a line appeared.

Do not shake the book. Undignified.

Mara let out a breath she had not meant to hold. "I was not going to."

You considered it.

"I consider many foolish things."

Admirable growth would involve fewer.

The letters faded before the last period dried.

Mara touched the page.

The ledger felt ordinary.

That was the wrongness. Arveth's copied witness had never felt alive exactly, but it had felt occupied: cool resistance under the leather, a patient argument against erasure. Now it felt like paper. Good paper. Old paper. Not a person. Not enough.

Sava found her there.

The clerk had slept two hours and made those two hours look ashamed of themselves. Ink stained her jaw. A seal ribbon stuck from one sleeve. She carried three mugs of tea by their handles in one hand, which Mara regarded as a higher magic than cinder-singing.

Sava saw the ledger and stopped.

"How long?" she asked.

"Since dawn."

"He wrote?"

Mara showed her.

Sava read the fading words. Her mouth trembled once and became stern by force. "Still insufferable. Good."

"Sava."

"I know."

They sat in the lee of a bridge pier while Third Arch woke around them. Above, workers repaired storm ropes. Below, dead fall-witnesses murmured names to bridge judges. Refuge children living and dead played a game involving chalk circles, shrieking, and rules so fluid Tavi had threatened to formalize them for science. Farther off, Kesh argued road compact terms with goblin and troll elders. Saelith helped a light-elf healer treat a dead cavalry horse's cracked leg because mercy had become weirdly specific. Caldus drilled volunteers in the rain. Brakka pretended not to watch Elder Morn watching her.

Life, inconvenient and damp, continued.

Arveth faded anyway.

"We knew copied witness might not hold outside Orrowen," Sava said.

"Knowing is not the same as agreeing."

"No. That is why clerks invented appeals."

"Can we take him back?"

Sava looked toward the east, where roads crawled with refugees, risen dead, royal envoys, Pale Remnant messengers, and stories already mutating faster than horses. "If we turn back now, some records strengthen and many people lose the road to the Storm Isles."

"So he becomes a cost."

Sava's eyes sharpened. "Do not use that word where he can hear you."

The ledger wrote one letter.

R.

Then nothing.

Mara stared until her eyes hurt.

R could be record. Return. Refusal. Ridiculous, if Arveth had enough strength left for brand loyalty.

Sava stood abruptly. "There is one place in Third Arch where names are tested without requiring the named to stay."

"That sounds invented for exactly this moment."

"Most useful institutions were invented by someone cornered."

The Name Alcove lay under the central arch, cut into the cliff behind a waterfall thin as gauze. Trolls used it for oath repair, Durn explained, not oath restoration. Restoration was vanity. Repair admitted visible joinery. The alcove walls were covered in names carved, inked, burned, tied, scratched, and in one case bitten into stone. Some belonged to living refugees. Some to dead. Some to bridges. Some to betrayals that needed naming before forgiveness could stop being theater.

They brought witnesses.

Mara did not ask for many. Many came anyway.

Sava carried the ledger. Ilyr brought the opened Khar Veyl record because Arveth had once insisted hidden truth was a form of murder with excellent posture. Maelin came beside him, not touching, not distant. Saelith brought the corrected hymn mark. Tavi brought the root-hound's empty collar and pretended it was relevant to acoustic testing. Kesh brought a debt token from a road he had not yet confessed aloud. Brakka brought a bridge chip from the courthouse steps where Orrowen had nearly swallowed them in law. Caldus brought nothing visible, which meant the thing he brought was probably the hardest.

At the alcove entrance, Pell the dead child appeared with his clay whistle.

"Can I watch?" he asked.

Mara knelt. "It may be sad."

He considered this with grave expertise. "Most things are. Some also have snacks."

Kesh looked wounded. "The child understands civic planning."

They let Pell in.

Sava laid the ledger on the central stone.

"Arveth of Orrowen," she said, voice formal enough to make grief stand straighter. "Executed under three regimes. Convicted under emergency continuance. Corrected to citizen standing by mixed witness. Present in copied, partial, improperly duplicated, and frequently annoying form."

The ledger flickered.

Annoying?

Sava pressed a hand over her mouth.

"Frequently," Mara said, and her voice broke on the word.

The page warmed.

The ink gathered itself into a thin figure standing on the paper. Not Arveth as he had been, exactly. A sketch of him. Tall, narrow, robe loose, face made of lines and omissions. The waterfall's mist passed through him and made the edges run.

"Well," he said. "This is humiliatingly well attended."

No one laughed at first, which disappointed him visibly.

Kesh rallied. "I can leave if it helps."

"Not enough."

There. Mara felt the room breathe around the joke. Personhood maintained not by solemnity alone, but by the right to be impossible at breakfast.

Sava stepped forward. "You are fading."

"Clerks. Always opening with the scandalous truth."

"Can we anchor you?"

Arveth looked at the names on the alcove walls. "Yes."

Hope struck Mara so hard she hated it.

He saw that, of course. He had always been inconveniently observant for a man partly made of filings.

"You should ask whether you may," he said.

The alcove quieted.

Mara understood and did not want to. "Do you want to be anchored?"

Arveth's ink face softened.

"I want not to be erased," he said. "I want every regime that killed me to remain accused. I want Orrowen's dead to keep their standing. I want the living to stop discovering, at the exact moment grief becomes expensive, that principles have budgetary limits."

"Then we anchor you."

"I was not finished."

Mara closed her mouth.

"I also want to be done when done is true." Arveth looked toward Pell, then Sava, then the rest. "There is a cruelty in erasure. There is another cruelty in preservation without permission. I have been a record, a warning, a legal problem, a weapon people attempted to load, and occasionally a friend. I refuse to become a relic because you are lonely."

The words struck with terrible gentleness.

Mara looked down at her hands. Burn scars crossed the palms now, new over old. Useful hands. Hands everyone watched when crisis needed a shape.

"I do not know how to lose people without making it mean I failed," she said.

Caldus drew in a breath behind her.

Saelith's eyes filled.

Arveth sat on the edge of the ledger page as if it were a bench. "That is because you were taught failure by people who profited when you confused love with output."

Tavi made a wounded sound and immediately pretended to cough.

Mara laughed once, wetly. "You sound very alive for someone making a final argument."

"Yes, well, I object to poor timing."

Sava knelt on the other side of the stone. "What do you choose?"

Arveth looked at her for a long time. "Not final rest. Not yet. There remains testimony I must give at the Dead Capital. But I choose a lighter anchor. Not in one book. Not in one person. Not in Mara's satchel like contraband conscience."

"Where?" Ilyr asked.

"Everywhere I was properly heard."

The Name Alcove answered.

Not with light. With pressure. The walls seemed to lean inward. Carved names warmed under mist. The bridge chip in Brakka's hand hummed. The Khar Veyl record opened by itself. Saelith's hymn mark shone. Tavi's collar clicked. Kesh's debt token darkened. Caldus finally opened his fist and revealed a small strip of Ashgate chain, the kind used in Mordane's foundry to bind dead laborers before Mara broke the arithmetic of usefulness.

Arveth looked at it.

"Ah," he said softly. "Yes. That too."

They spoke him into many places.

Not the way a command engine would. No single anchor. No master copy. Sava entered his corrected standing in the traveling register. Ilyr copied his testimony into the opened record with a challenge clause. Saelith sang his name into the flawed interval so beauty could not pretend he had been tidy. Brakka carved him under refuge law as one who crossed without taking. Tavi etched a small objection mark into the root-hound collar. Kesh placed his name beside an unpaid road debt and swore, with visible discomfort, that some debts could not be sold. Caldus tied the chain strip around the ledger clasp and said, "Witnessed by a man who once mistook obedience for honor."

Mara waited until the end.

"And me?" she asked.

Arveth looked at her with such kindness that she nearly stepped back.

"You carry not me," he said. "You carry the habit of asking whether someone has been made useful against their will. That is heavier. Sorry."

"You are not sorry."

"No."

His ink figure thinned.

Sava reached for him, then stopped herself before touching the page.

Arveth smiled at her. "Registrar Rennet."

"Citizen Arveth."

"Tea when I am next coherent."

"Bad tea," she said.

"Cruel, but motivating."

The figure dissolved into lines, then into letters, then into a single mark like a door left ajar.

The ledger did not feel occupied after that.

It did not feel empty either.

That was harder to name.

Outside the alcove, rain had stopped. Sun struck the bridges in broken pieces. Pell blew one soft note on his clay whistle, and from somewhere far below, a dead fall-witness answered with another.

Mara carried the ledger back to camp without holding it against her chest.

That was the first gift she could give him.

Not clinging.

Not yet letting go.

Making room.""",
    8: r"""## Chapter 8: Storm Road

The road to the Storm Isles began where maps gave up and weather started making threats.

No one agreed on the route because the route did not agree with itself. Gnome charts showed thermal towers and wind-bridges above the eastern sea. Goblin road marks described smugglers' paths along cliff tunnels that flooded upward during lightning tides. Troll stone memory insisted the oldest crossing was a chain of drowned arches visible only when thunder spoke a true name. Lumenorath star tables offered a clean celestial bearing that ignored the practical problem of cliffs. Khar Veyl shadow maps included three useful tunnels and one annotation that translated roughly as never bring drums here, which worried everyone because no one had mentioned drums.

The caravan could not go whole.

That was the first cut.

Third Arch would hold the refuge camp under Brakka's new law. Sava would remain to build traveling witness courts with troll judges, goblin route speakers, living clerks, and dead citizens who could challenge their own handling. Thom and Lora would stay for now. Nera Bell chose to walk river roads with a group of unburied dead seeking names downstream. The dead cavalry captain took half his riders north to guard refugee lanes against old military orders. Pell found his mother in the upper rope district and learned that she feared him, loved him, and needed time, which seemed to Mara like one of the bravest sentences any living person had spoken.

Mara's company shrank back toward its old shape and did not become simple.

Caldus. Saelith. Ilyr. Tavi. Kesh. Brakka, because Third Arch had amended her standing and immediately sent her away with the expression of a family that trusted love enough to demand work. Maelin came as Khar Veyl witness, which made Ilyr quiet. Auralian came for corrected Lumenorath law. Vaura sent three shadow envoys and one sealed apology that Ilyr read twice and refused to describe. Durn remained behind, but Elder Morn gave Brakka a bridge nail and told her to use it only when a road lied about being impossible.

Sava gave Mara the ledger.

"It is not him," Sava said.

"I know."

"It is still evidence."

"I know."

"Do not let dragons turn evidence into theater."

Mara looked toward the east, where storm clouds piled like black mountains beyond the real ones. "Is that a known dragon habit?"

Sava's smile was thin. "It is a known powerful habit."

The road out of Third Arch climbed through iron pine forest. Rainwater ran in red threads over the rocks. The air smelled of resin and lightning. For half a day, the journey felt almost ordinary in the punishing way of mountain travel: sore calves, slipping boots, Kesh complaining that honest roads lacked imagination, Tavi stopping to admire a naturally balanced stone and then being disappointed it was not secretly a machine. At noon they passed the last refuge marker. Brakka touched it with two fingers and said nothing.

After that, the dead began to thin.

Not vanish. Thin. The risen who traveled with them grew quieter as the storm road climbed. Arveth's ledger mark warmed and cooled like a distant pulse. The dead cavalry scouts turned back one by one, not from cowardice, but because old orders could not survive the pressure ahead. Even Pell's whistle, which Mara had kept for the boy until he decided whether he wanted it buried, made no sound when wind passed over it.

"Dragon weather," Ilyr said.

Tavi licked a finger, held it up, and frowned. "Weather does not usually object to being measured."

"This does."

Saelith wrapped her cloak tighter. "It feels like being judged by something that has not decided whether persons are worth the inconvenience."

"Wonderful," Kesh said. "I always enjoy legal proceedings where the ceiling can eat me."

At the first cliff tunnel, they found the bodies of three royal agents and one dead goblin guide.

The agents wore Harrowmere gray beneath travel cloaks. Their cinder lanterns had exploded inward, burning their chests without scorching the surrounding stone. The goblin guide lay apart from them with a knife in her hand and a road token under her tongue. Kesh went still when he saw the token.

"Kavik?" Mara asked.

"Orrin branch." He knelt without touching the body. "Her name was Rikka if she kept the one she liked. She sold river routes, lied at dice, sang badly on purpose, and owed me seven silver."

"Was she yours?"

His mouth twisted. "Goblins are not owned unless someone wants a memorable funeral."

He removed the token from under her tongue with two careful fingers. The road mark was scorched. On one side, in tiny scratches, Rikka had written: They promised storm toll and paid in silence.

Kesh closed his eyes.

The old account he had mentioned at Brindle Ford had found the road before him.

The tunnel breathed.

Not wind. Breath. Warm, mineral, vast. Mara felt it pass over her teeth.

A voice spoke from the stone in no language and every memory.

Who comes carrying broken witnesses?

No one moved.

The question did not sound like Vorrakai. Vorrakai's grief was deep, cold, almost tender in its desire to end motion. This voice was sharper. Old iron over flame. Curious in the way a blade was curious about pressure.

Mara put her burned hand on the tunnel wall. "Mara Venn. Traveling witness, subject to correction."

Laughter moved through the cliff.

The storm outside answered with lightning.

Small title.

"It keeps me from choking."

Brakka's mouth twitched.

One by one, the others named themselves. Caldus with no rank before his name. Saelith with Dawnmere and corrected oathkeeper both. Ilyr with exile and return. Tavi with engineer, field medic, and person currently disapproving of the tunnel's ventilation. Kesh of the Kavik Road, debtor and route speaker. Brakka of Third Arch, amended standing. Maelin of Khar Veyl, witness under opened record. Auralian Thrice-Crowned, correction pending.

The cliff listened hardest to that last phrase.

Honesty improves flavor, it said.

"I hate dragon courts already," Kesh whispered.

The tunnel opened.

Inside, darkness held old rain.

They walked single file. The walls were veined with cinder, not dead fragments like road-grit, but living scars that pulsed when Mara passed. Images moved in them: wings over cities not yet built, peoples around first fires, dragons lowering their heads to hear mortal law, mortals raising cages because awe had become fear, dragons answering cages with judgment because fear had become insult. None of the images lasted long enough to become history. That, Mara suspected, was deliberate. Dragons remembered truth, not always proportion. A mountain looked small from the sky.

Halfway through, the tunnel bells began.

No one had hung bells there. The sound came from droplets striking stone in patterns too exact for water. Tavi began counting under her breath and then stopped, pale.

"What?" Caldus asked.

"It is using prime intervals."

"Meaning?"

"Meaning the tunnel is either very good at mathematics or about to kill us with music."

The first sky eel struck before anyone could ask for the distinction.

It came through the wall as lightning with teeth, long and translucent, its body a ribbon of stormbone and blue fire. It had no wings. It swam through rock and air alike, mouth opening around Tavi's lantern heat. Caldus shoved Tavi down. The eel passed over them and bit the cinder lamp from her pack. It exploded in a spray of sparks that became tiny screaming fish before vanishing.

"Rude!" Tavi shouted from the floor.

More eels poured through the walls.

The tunnel became blade, lightning, wet stone, and too many bodies in too little dark. Caldus fought by sound, sword flat against eel skulls, each strike ringing like a struck harp. Brakka drove her maul into the wall and pinned one eel half in stone until Kesh ran along her back, leaped, and cut the heat-sack under its jaw. Saelith sang the corrected interval, but the eels did not understand obedience or mercy; they understood migration and hunger. Ilyr's shadow blade sliced one into harmless rain that smelled of copper. Maelin dragged Auralian out of a lightning coil and looked annoyed that rescue had involved touching.

Mara tried to reach the cinders in the wall.

They recoiled.

Not from her. From the eels. Sky eels fed on loose heat during lightning migrations. The royal agents had lit cinder lanterns in the tunnel and rung dinner through the storm. Rikka had died stopping them from reaching the deeper road.

Kesh saw the same truth in the scorched token.

"They forced her to guide," he said.

An eel lunged at him. He did not dodge fast enough.

Mara's hand lifted.

Command flashed open like a door.

Stop.

The eel froze for half a heartbeat.

So did every cinder vein in the tunnel.

So did Mara's blood.

The silence was perfect. It was beautiful. It saved Kesh's life.

It also made every face turn toward her with the same fear the council hall had worn.

Mara released it.

The eel crashed into the wall. Kesh rolled away, breathing hard.

"Sorry," she said.

"Save apologies until after teeth," he gasped.

But the tunnel had felt it. The dragon voice had felt it. Somewhere beyond the storm, attention sharpened.

Authority sits easily in your hand, small title.

Mara shook so hard her burned palm struck the stone. "It sits like a knife."

Then carry it by the blade.

"No."

She did not shout. The word cut cleaner for that.

Mara reached instead for witness. Rikka of Orrin branch, unpaid and unsilenced. Royal agents dead by their own greed. Sky eels migrating, not evil. Cinder veins living scars, not bait. Kesh alive because a friend had almost done the wrong thing for the right reason and stopped.

The tunnel changed.

Not obedience. Orientation.

Cinder veins dimmed. Tavi, catching on, smashed the remaining lamps with a wrench while making small bereaved noises. Saelith shifted her hymn to match water instead of law. Ilyr and Maelin opened shadow pockets where heat could drain harmlessly. Brakka and Caldus held the line while Kesh threw Rikka's scorched token into the deepest dark and shouted her name.

The eels turned.

One by one, they followed the token's falling heat through a crack in the world and vanished toward the storm below.

When the last eel passed, the tunnel went black.

For a while, everyone breathed like survivors and did not spoil it with speeches.

Then Tavi said, "I liked that lamp."

Kesh, still on his back, replied, "Invoice the dragon."

The tunnel laughed again.

At its far end, daylight appeared blue-white and violent.

They emerged onto a cliff above the eastern sea.

The Storm Isles floated beyond the horizon, not islands in any ordinary sense, but black masses of stone suspended inside revolving towers of cloud. Water climbed toward them in spirals. Lightning crawled upward. Shapes moved between the clouds, vast and winged and slow enough to make distance feel like a moral failing.

Mara stood at the edge until salt wind dried the blood on her palm.

Behind her, the tunnel voice spoke one last time.

The Court of Long Memory has heard you refuse the easy shape.

"And?"

Storm rolled over the sea like a dragon turning in sleep.

Now it will learn what shape breaks you.

No one spoke for a long moment.

Then Brakka set Elder Morn's bridge nail against a rock and drove it in with one blow. The stone cracked open into a narrow path along the cliff, impossible a breath earlier, wet with stormlight.

Kesh looked down at the path, then at Mara.

"Still not an army?"

Mara watched lightning climb into the sky.

"No," she said. "Something worse for everyone who wants one."

She stepped onto the storm road.

It held.""",
}


def replace_chapters(text: str) -> str:
    pattern = re.compile(r"(?m)^## Chapter (\d+): .*$")
    matches = list(pattern.finditer(text))
    by_no = {int(m.group(1)): m for m in matches}
    back_matter = re.search(r"(?m)^## Back Matter\b", text)
    missing = sorted(set(CHAPTERS) - set(by_no))
    if missing:
        raise ValueError(f"Missing chapters in manuscript: {missing}")
    for chapter_no in sorted(CHAPTERS.keys(), reverse=True):
        match = by_no[chapter_no]
        start = match.start()
        later_starts = [m.start() for m in matches if m.start() > start]
        if later_starts:
            end = min(later_starts)
        elif back_matter and back_matter.start() > start:
            end = back_matter.start()
        else:
            end = len(text)
        replacement = CHAPTERS[chapter_no].strip()
        text = text[:start] + replacement + "\n\n" + text[end:].lstrip()
        matches = list(pattern.finditer(text))
        by_no = {int(m.group(1)): m for m in matches}
        back_matter = re.search(r"(?m)^## Back Matter\b", text)
    return text


def update_metadata(word_total: int) -> None:
    meta = METADATA.read_text(encoding="utf-8")
    meta = re.sub(r"produced_word_count: \d+", f"produced_word_count: {word_total}", meta)
    meta = re.sub(r"at_300_words_per_page: \d+", f"at_300_words_per_page: {round(word_total / 300)}", meta)
    meta = re.sub(r"at_275_words_per_page: \d+", f"at_275_words_per_page: {round(word_total / 275)}", meta)
    meta = re.sub(r"at_250_words_per_page: \d+", f"at_250_words_per_page: {round(word_total / 250)}", meta)
    meta = re.sub(
        r'current_form: ".*"',
        'current_form: "full-length draft zero with Book Three chapters 1-8 revised in pass 01"',
        meta,
    )
    METADATA.write_text(meta, encoding="utf-8")


def update_summary(word_total: int) -> None:
    if not SUMMARY.exists():
        return
    text = SUMMARY.read_text(encoding="utf-8")
    text = re.sub(
        r"\| The Dragon That Dreamed Death \| `book-03-the-dragon-that-dreamed-death` \| [\d,]+ \| \d+-\d+ \|",
        f"| The Dragon That Dreamed Death | `book-03-the-dragon-that-dreamed-death` | {word_total:,} | {round(word_total / 300)}-{round(word_total / 250)} |",
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
    print(f"Book Three chapters 1-8 revised. Word count: {total}")


if __name__ == "__main__":
    main()
