#!/usr/bin/env python3
"""Revision pass 01c for Book One chapters 9-13.

Replaces the Memory Moths / Brakka / Seven Arches / Arveth sequence with
bespoke prose, then updates metadata and split chapter files.
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
    9: r"""## Chapter 9: Memory Moths

Old Jaw was a road only because people had agreed to keep lying about it.

It ran under the Gloamfen in drowned pieces: a sunken causeway here, the roof of an old tollhouse there, a chain of stones below black water, a plank bridge nailed to the ribs of something no one had wanted to identify after death. Kesh moved first, one hand lifted for silence, his other hand holding a reed knife with a curved bone handle. Mara followed with the cinder cage hugged against her chest. Behind her came Caldus, then Pell, Essa, and Tollen in their festival masks and eel baskets, traveling badly but traveling.

The underwater lanterns drifted beside them.

They were not lanterns, of course. Kesh had explained that in a whisper full of professional offense. Lanterns did not swim against current, blink in pairs, or try to arrange themselves into letters from dead languages. These were fen-lures: little pale things with light in their bellies and teeth where a sensible creature kept doubt.

"If they spell anything," Kesh whispered, "do not read it."

"How do you not read something?"

"Royal schooling helps."

Caldus made a faint sound behind them that might have been disapproval or a laugh strangled for discipline. Mara did not turn. The road beneath the water narrowed until her boots had to find each next stone by faith and Kesh's muttered instructions. Left. Not that left. Heel first. Stop. Swear quietly if you must, but do not splash.

Somewhere ahead, a wagon chain clinked again.

Mara's whole body leaned toward it.

Kesh caught her sleeve. "That sound is bait."

"You do not know that."

"Everything in Old Jaw is bait until it proves otherwise, and proof usually has digestion."

"It sounded like Joryn."

The words came out smaller than she wanted. Kesh's face changed. His hand loosened but did not let go.

"That is why it is good bait," he said.

The cinder cage hummed twice.

Tavi's rule returned to Mara so sharply she nearly dropped the cage. Twice, stop. Three times, run. She stopped. The others stopped behind her. The underwater lights stopped too.

Then the dark ahead filled with wings.

They came soundlessly at first, pale as onion skin, each moth no larger than a thumbnail and marked with a black dot like spilled ink. They rose from the drowned tollhouse windows in a cloud so delicate it looked like breath leaving the world. One landed on the cage. Another settled on Mara's bandaged wrist. Its feet were impossibly light.

Then it spoke in Joryn's voice.

"Living first," it whispered.

Mara forgot to breathe.

Kesh swore. "Memory moths. Cover your mouth. Do not answer anything in a beloved voice."

The moth on Mara's wrist opened and closed its wings. Joryn's voice came again, softer this time, the way he had sounded when she was little and fevered and pretending not to cry.

"Rage after."

Mara crushed the moth against her sleeve.

It burst into silver dust.

The dust went into her nose, mouth, eyes, wound. The road vanished.

She was six years old, under the table during a storm, watching her mother's skirts move past with a bowl of soup balanced in both hands. She was eight, holding wax plugs while her father slept with both palms over his ears. She was ten, watching Joryn lie to a foreman about her age so she could stay aboveground one more year. She was twelve, waking in the night because the east seam had spoken through the floorboards and she had answered in her sleep.

Mara.

She had answered before.

The memory hit so hard she fell to one knee in black water.

Caldus caught the back of her coat. "Mara."

The moths found his voice next. One settled on his scraped shield and spoke with the calm authority of a commander giving an order. "Escort under mercy seal. No inspection required."

Caldus went rigid.

Another landed on Kesh's scarf and said, in Kesh's own voice, "Take both payments. Roads belong to whoever survives them."

Kesh slapped it away too late. Mara heard the confession before he killed the moth. So did Caldus.

"Both payments?" Caldus said.

"This is an awkward time for accounting."

Moths swarmed the dead.

Pell began humming at once. Essa joined, then Tollen, their three broken voices threading through the wet dark. The moths hovered over them, whispering borrowed names, old debts, the last things said by mouths now hidden under masks. The dead shook under the weight of memory, but the hum held.

Mara clutched the cage and tried to stand. The cinder inside it glowed blue-white. The moths wanted it more than they wanted flesh. They gathered until the cage became a lantern of wings.

"Use the disk," Caldus said.

"Tavi said if it goes silent."

"It is screaming."

"Different rule."

Kesh grabbed Mara's injured wrist, not gently. "Vent-girl, listen to me. Memory moths do not eat memory. They move it. They spread what is hidden until nothing knows whose grief belongs to whom. If that cinder opens here, every secret in Old Jaw wakes up hungry."

"Then what do we do?"

Kesh looked toward the drowned tollhouse. "We pay toll."

"With what?"

His grin was gone. "Truth."

He stepped onto the half-submerged tollhouse roof and raised both hands. The moths turned toward him, recognizing a performance or a meal.

"I took the physician's money," he said. His voice shook, which made the truth heavier. "I took Narka's debt too. I meant to delay the girl if it profited me and save her if that profited me more. I told myself roads have no loyalty. I told myself survival is cleaner than care."

The moths swirled around him.

Mara could have hated him then. Part of her did. But his fear was naked, and he stood anyway.

"And?" she demanded.

Kesh looked at her. "And then Pell said your brother's name. Now I am here."

The moths struck him like rain.

He staggered but did not fall. The cloud lifted from the cage and spun around the tollhouse chimney. Each moth carried one fragment of confession, flashing pale and black. Mara understood suddenly. Truth was not purity here. It was weight. The road required something real enough to hold the swarm.

She climbed onto the roof beside Kesh.

"I heard the cinder before," she said.

Caldus inhaled sharply.

Mara forced the words out before fear made them small. "When I was a child. I forgot because it frightened me. Or because it wanted me to forget. My father heard it too. The company called him careless when he died, but he was not careless. Something under Kell Ashgate knew us."

The moths turned.

Her memory opened: her father's hand on the table, black crescent mark in his palm; her mother's face tight with terror; Joryn in the doorway, too young to understand and old enough to remember. Beneath the house, a low bell. A name not spoken aloud.

Not Mara.

Venn.

The moths poured that memory into the air, not as accusation, but as light. Caldus saw it. Kesh saw it. Even Pell, through the mask, lifted his head.

The cinder cage stopped screaming.

One moth remained on Mara's hand. It spoke in her father's voice, though she no longer knew if the voice was true.

"Do not let them spend the dead twice."

Then it dissolved.

The water before the tollhouse sank, revealing a stone stair down through the drowned road. On the lowest step lay a strip of black wagon cloth snagged on a nail and a brass chain link still warm from use.

Mara picked up the link.

Joryn had passed this way.

"How long ago?" she asked.

Kesh crouched, touched the wet stone, and smelled his fingers. "An hour. Maybe less."

"Then we move."

"Mara," Caldus said.

She turned on him. "If you tell me to rest, I will become unreasonable."

"I was going to say the moths exposed us too. Anyone who knows how to listen to this road just heard truths about you, Kesh, and the cinder."

"Then they can get in line."

Kesh gave a weak laugh. "That is not as strategic as it sounded in your head."

"No," Mara said, gripping the warm chain link until it hurt. "But it is honest."

They descended through the tollhouse stair. Behind them, memory moths settled back into the walls, carrying scraps of confession into the wet stone. Ahead, Old Jaw opened toward a pale slit of daylight and the distant thunder of water falling beneath the world.

Mara had remembered the mountain.

Now the mountain, wherever its sleeping heart lay, would know she remembered back.""",
    10: r"""## Chapter 10: Brakka's Toll

The Seven Arches appeared after the marsh ended, and for several minutes Mara's mind refused to accept them as bridges.

Bridges crossed things. Rivers, ravines, canals, roads. The Seven Arches crossed absence.

The land broke open without warning beyond the last black reeds, falling away into a canyon so deep the bottom held a second sky. Stars glimmered there at noon, cold and clear, as if night had sunk and pooled beneath the world. Across that impossible gulf, seven stone spans rose one after another, each broader than a city wall, each carved with figures too weathered to be gods and too stern to be decoration. Wind moved through them with the sound of distant throats.

Mara stopped at the edge.

Kesh, who had been insufferably pleased with himself since Old Jaw failed to eat them, stopped beside her. "Try not to look down like a tourist."

"I am not looking down like a tourist."

"You are looking down like someone about to ask whether those are real stars. That is tourist-adjacent."

"Are they?"

"Real enough to charge for."

Caldus came up behind them, face drawn from the forced pace. The disguised dead waited under a cluster of leaning pines. Pell's scarf hid his torn mouth, but not the effort it took him to remain upright. They had lost the wagon trail at the whitewater ford two miles back. Kesh believed the black wagons had taken the crown road across the Arches. Caldus believed that meant soldiers. Mara believed very little except that Joryn's chain link was still warm when she held it against her palm.

At the mouth of the Third Arch stood a troll.

Mara had seen drawings. Chapel books made trolls into hunched brutes with tusks, clubs, and the moral complexity of bad weather. The woman before the bridge did carry a stone maul taller than Mara, and tusks did push up from her lower jaw, but the books had failed in every important respect.

She was enormous, yes, green-gray, wide as a doorway, braided with copper rings and white stone beads. But she was not crude. Her armor was layered from carved slate plates fitted so carefully they moved like scales. Her hair was twisted back with strips of blue cloth. Around her neck hung small tablets of polished stone, each etched with lines of vow-script. Her eyes were amber, deep-set, and much too patient.

"Kesh," she said.

Kesh bowed. It was not one of his pretty bows. It was careful.

"Brakka of the Third Arch," he said. "May your stones remember only flattering foot traffic."

"They remember you owing six tolls."

"Flattery has failed me."

"Often."

Mara stepped forward because Kesh was useful but also allergic to arriving at a point. "We need to cross."

Brakka looked down at her. The troll's gaze moved over the bandaged hand, the cinder cage, Pell's token, the chain link, the exhausted knight, the masked dead. It missed nothing and hurried nowhere.

"Everyone needs," Brakka said. "Need is wind. Toll is weight."

Caldus touched the purse at his belt. "We can pay coin."

The troll's nostrils flared. "Coin pays ferry. Coin pays tavern. Coin pays fool to say yes before thinking. Third Arch takes vow."

"A vow to what?" Mara asked.

"That is the toll."

Mara had not slept enough to be patient with sacred ambiguity. "We are chasing mercy wagons carrying my brother. Royal soldiers are ahead. Dead workers are behind me. I have a cinder in a cage that keeps making everything worse. If you want a poem, ask Kesh."

"I charge extra," Kesh said.

Brakka studied Mara for a long moment. Then she laughed.

It was not loud, but the bridge heard it. Stone under Mara's boots vibrated once, like a drum struck deep inside the arch.

"Little ash," Brakka said. "You think vow is poem?"

"I think powerful people love making desperate people promise things."

The troll's amusement vanished.

The wind through the canyon grew colder.

"Yes," Brakka said. "They do."

No one spoke. Kesh found something fascinating on his sleeve. Caldus shifted, ready for the conversation to become a fight and ashamed of wanting that simplicity.

Brakka planted the butt of her maul on the stone. "A true vow is not chain. A true vow is bridge. It binds two shores so crossing may happen. If one shore owns all the crossing, bridge is not bridge. It is trap."

Mara thought of the hymn-script cloth that had tightened around her wrists, of Mordane's mercy seal, of company contracts her neighbors signed because not signing meant hunger. "And who decides if a vow is true?"

Brakka touched one of the tablets at her throat. "Stone remembers. Witness answers. Those bound may challenge."

"May they win?"

Another long look. "If weight is true."

That was the first thing about vows Mara had ever liked.

A horn sounded from the far side of the bridge.

Kesh swore. Caldus moved to the edge of the pines. Across the Third Arch, black wagons were already halfway over, guarded by soldiers in wet cloaks. Mara's heart lurched. She could not see Joryn. She could see wagon chains. Wheels. Mercy seals.

"Let us pass," she said.

"Toll first."

"My brother is on that bridge."

"Then vow with speed."

Mara wanted to scream. Instead she gripped Pell's token until the metal dug into her skin. What could she promise that mattered? Not success. Only fools and kings promised outcomes no human could command. Not obedience. Never that. Not vengeance, though it burned bright and tempting.

Pell stood behind her, swaying under his reed cloak. His masked face turned toward the wagons.

Tell Lio. Tell Tam.

Names.

Mara looked back at Brakka. "I vow to return the names I take from the dead to someone living who will speak them. Not use them. Not count them. Speak them. If I cannot find kin, I will make witness. If I fail, the road may refuse me."

The Third Arch went silent.

Even the far horn seemed to pause.

Brakka's amber eyes narrowed. "You make large door with small hands."

"Is it enough?"

"No."

Mara's breath caught.

The troll leaned closer. "It is too much for one crossing. You sure?"

No. The honest answer was no. Mara was sixteen, half-fevered, terrified for Joryn, and already carrying more names than she understood. But Pell's token lay against her throat. Essa and Tollen waited behind her in borrowed masks. The black wagons rolled ahead under a mercy seal. If a vow was a bridge, perhaps it could carry what she could not.

"I am sure enough to start," she said.

Brakka smiled then, slow and fierce. She drew a stone knife from her belt and cut her own palm. Gray-green blood welled, thick as wet clay. She pressed the bleeding hand to the arch. The stone drank.

"Witness," she said.

The canyon answered.

Not with words. With weight. Mara felt the vow settle around her shoulders, not like a chain, not like hymn-cloth, but like a pack she had agreed to carry and could one day set down before those with the right to judge her.

Brakka stepped aside.

"Cross, little ash."

Mara ran.

The bridge was wider than it had looked and longer than was fair. Stars shone below through gaps in the stone. Wind slammed sideways, smelling of rain, old snow, and mineral dark. The black wagons ahead picked up speed as the soldiers noticed pursuit.

Caldus caught up beside her. "We cannot fight them in the open."

"Then do not."

"That is not a plan."

Kesh appeared on her other side, breathing hard. "It is barely a sentence."

From behind came a sound like stone clearing its throat.

Brakka of the Third Arch was following them.

She moved with impossible force, each stride shaking dust from carvings older than the crown. Her maul rested on one shoulder. Her oath tablets clacked against her armor.

Kesh looked betrayed. "You charged us and came anyway?"

Brakka did not slow. "Toll accepted. Road endangered. Also bored."

The far soldiers began turning the first wagon. One raised a command rod.

The cinder cage hummed in Mara's arms.

Under the bridge, the stars at the canyon bottom brightened as if looking up.

Mara did not know whether her vow had given her the right to this road or merely made the road aware of her. Either way, Third Arch carried her forward, and for the first time since Joryn's wagon vanished into rain, she felt something under her feet answer not with hunger, but with law.""",
    11: r"""## Chapter 11: Siege of Third Arch

The first command rod struck the bridge like a thrown nail of black fire.

It hit ten paces ahead of Mara and burst into a ring of blue sparks. The stone underfoot shuddered. Every carved figure along the parapet opened its weathered mouth at once, though no sound came out. Pell cried behind his mask and dropped to one knee. Essa and Tollen faltered with him, the command reaching for the hooks the crown had driven into their stolen names.

Mara stopped running.

Caldus swore. "Do not stop in a kill lane."

She heard him, but the cinder cage was humming against her ribs and the vow on her shoulders had tightened. The command rod had not been aimed at her. It had been aimed at the dead. The soldiers at the far wagon did not care whether she reached Joryn if they could reclaim the named dead first.

Pell clawed at his scarf. The festival mask had slipped, showing the torn corners of his mouth. His eyes clouded.

"Hum," Mara shouted.

He did not hear.

Brakka did.

The troll planted herself between Pell and the command rod, slammed one foot down, and began to hum.

It was not musical. It was stone remembering pressure. The note rolled through the bridge, deep enough to make Mara's bones ache. Pell's head jerked up. Essa found the sound and joined it. Tollen followed. Their broken hum threaded into Brakka's until the command sparks guttered.

The far soldiers hesitated.

Then the siege engine appeared.

It came from the far guardhouse, dragged by four oxen and six men, iron-ribbed and squat, with a cinder bead mounted in a cradle at its nose. Caldus went very still.

"That is not for fugitives," Kesh said.

"No," Caldus replied. "That is for bridges."

Mara stared across the long span. The mercy wagons were nearly off the far side. One black curtain shifted. She saw a hand inside, pale against dark wood. Not enough to know. Enough to hope, which was crueler.

The engine fired.

Brakka moved first. She swung her maul not at the bolt, which would have been absurd, but at the bridge itself. Stone cracked under the impact. The whole span flexed. The cinder bolt struck where Mara had stood a heartbeat earlier and tore a smoking trench through the roadway.

"You hit the bridge!" Kesh yelled.

"Bridge and I have understanding."

"Does understanding involve structural collapse?"

"Sometimes."

Royal soldiers poured from the far guardhouse. More emerged behind them on the near side, cutting off retreat. The bridge had become exactly what Caldus had feared: a kill lane with stars beneath it and no walls high enough to hide behind.

Then the trolls under the bridge began to climb.

Mara had thought the Seven Arches were guarded at their mouths. She had not imagined the clans living in the stone itself. Hands like carved roots gripped seams in the arch. Gray-green faces rose over the parapets. Trolls hauled themselves from maintenance paths, shrine ledges, and openings that had looked like shadow until they moved. Some carried hammers. Some carried spears. One carried a soup pot and looked personally offended by the interruption.

Brakka shouted in a language made of thunder and stonefall.

The trolls shouted back.

Kesh translated while ducking an arrow. "They are debating whether the bridge is a road, a shrine, or a corpse."

"Now?" Mara said.

"Troll law is robust under pressure."

Caldus shoved her behind a broken parapet as crossbow bolts snapped overhead. "Can the law hurry?"

Brakka heard him. "Law hurries for no man."

The siege engine fired again.

This time the bolt struck one of the carved figures along the parapet. The figure shattered. A sound came from the bridge that was not stone. It was pain.

Every troll stopped arguing.

Brakka's face changed.

"Corpse, then," she said.

The trolls roared.

They hit the royal soldiers from below, above, and the sides, turning the bridge into a battlefield of bad angles. Caldus pulled Mara through the chaos toward the first wagon. Kesh vanished over the parapet and reappeared under the wagon axle with a knife between his teeth. Tavi was not there to make anything explode, which Mara considered deeply unfair.

The cinder cage hummed twice.

Mara saw why.

The command rod officer had reached the named dead. He stood behind Pell, rod lifted, lips moving around a command shaped like a hook. Pell's hum broke. Essa staggered. Tollen dropped his slate and clawed at his throat.

Mara ran toward them.

The officer saw her coming and smiled. He was young, blond, and terrified enough to be cruel quickly.

"Stand down," he said, and the rod flared.

The command struck Mara through the cinder cage. For one sick heartbeat she was in the foundry she had not yet seen, surrounded by brass tags and furnace heat. She felt how easy it would be to order the dead. Easier than freeing them. Easier than holding all their pain. Command was a road too, straight and clean and built over buried people.

She nearly wanted it.

Then Pell's token burned against her throat.

Mara opened the cage.

The cinder shard flared black-blue. Not enough to blast the officer, not enough to save the bridge, not enough for any song worth singing. Enough to carry one name.

"Pell Orwick," she said.

The officer's command snagged.

"Essa Brant."

The rod cracked.

"Tollen Reed."

The crack widened. Blue fire ran up the officer's sleeve. He screamed and dropped the rod. Pell surged upright, not attacking, simply becoming too present to be commanded. Essa grabbed Tollen and pulled him back behind Brakka's maul.

The siege engine fired a third time.

Kesh had been under it.

The bolt went nowhere. The engine leapt, coughed, and folded sideways as its own axle abandoned the profession of being an axle. Kesh rolled out from beneath it covered in grease and looking delighted.

"I have improved it!" he shouted.

The engine exploded.

Not dramatically enough to kill everyone. Dramatically enough to throw soldiers, oxen, and one extremely surprised troll into a heap of ropes and smoke. The far wagon team panicked. The first black wagon lurched, wheel striking a broken stone. Its door flew open.

Mara saw inside.

Not Joryn.

Three strangers, alive, bound, gagged. A woman with a shaved head. An old man with chapel ink on his brow. A boy in a courier's belt.

Mara's heart fell so hard she almost missed the second wagon turning off the bridge road beyond the far gate.

Joryn's wagon.

"No," she said.

Caldus caught her before she sprinted into the retreating soldiers. "We cannot reach it."

"Let go."

"We cannot reach it alive."

That word again. Alive. It was always being used as a wall.

Brakka stepped beside them, breathing hard, stone dust on her armor. The trolls had driven the soldiers toward the far guardhouse, but the second wagon was already vanishing into a road cut through the cliffs.

"Road has branches," Brakka said.

Mara turned on her. "What branch?"

"Old crown road. Closed by rockfall. Not closed to those who know bridge bones."

Kesh wiped grease from his face. "I hate knowing bridge bones."

Brakka looked at Mara. "Your vow continues?"

Mara stared at the open first wagon, at the living prisoners blinking in daylight, at Pell and Essa holding themselves upright, at the broken command rod smoking on the stones.

Joryn was farther away because she had stopped to save others.

Living first.

The words hurt worse when they were right.

"It continues," Mara said.

The Third Arch rumbled underfoot.

Brakka nodded as if something had been settled between Mara and the stone. "Then we take the branch."

Behind them, the trolls began singing to the shattered parapet. Not mourning exactly. Accounting, perhaps. Naming damage so the bridge could decide what to become after pain.

Mara helped cut the prisoners free with hands that shook from rage, cinder heat, and the awful knowledge that every life saved had weight. The boy in the courier belt clung to her sleeve and sobbed. She did not know his name yet. She would.

Across the canyon, Joryn's wagon disappeared into the cliff road.

Mara tied the cinder cage shut, lifted her eyes to the Seven Arches, and followed Brakka into the bones of the bridge.""",
    12: r"""## Chapter 12: A Vow Is a Road

The bones of the bridge were full of doors.

Brakka opened the first by striking a carved kneecap with the butt of her maul. A section of parapet shifted inward, revealing a stair so narrow Caldus had to turn sideways to enter. Kesh looked at the dark, then at the stars shining under the canyon, then at the dark again.

"I vote for literally any third option."

"Denied," Brakka said.

"You did not let me campaign."

"Also denied."

Mara ducked into the stair before either of them could improve the conversation. The air inside was cold and mineral, smelling of wet stone, old smoke, and something like crushed mint. The walls were carved with lines of vow-script. Some marks were deep and clean. Others had been rubbed nearly smooth by centuries of hands. The stair wound downward through the arch itself, not into a tower or tunnel but into the bridge's body, where each footstep made the stone hum.

The freed prisoners from the first wagon followed with the named dead. The woman with the shaved head was called Rella. The old man was Father Othen, though he insisted the title had been mostly paperwork. The boy was Niv, a courier apprentice who had bitten through one gag already and looked prepared to bite the world if given time.

Mara took their names one by one. Not magically. Not with cinder heat. Simply listening, repeating, making sure each sounded like itself in her mouth. The vow on her shoulders warmed every time she did.

"Does it hurt?" Niv asked.

"Being polite?"

"Being... whatever you are."

Mara considered several lies and found she was too tired to decorate them. "Yes."

The boy nodded, satisfied by honesty. "Good. If it did not hurt, I would not trust it."

Kesh leaned close to Mara. "I like him. Terrible sign."

They reached a chamber where the arch widened around a hollow of pale stone. At its center stood a vow-stone taller than Brakka, black with handprints. Water dripped from the ceiling though they were inside a bridge with no water above it. The drops struck the stone and vanished.

Brakka knelt.

Every troll in the chamber knelt with her.

Mara had not realized more had joined them. Trolls emerged from side passages, shrine alcoves, hidden steps: elders with slate-white hair, young warriors with chipped tusks, children carrying bowls of gravel and herbs. They watched Mara with the solemn curiosity of people observing a tool that might be a weapon or a witness.

An elder stepped forward. He was smaller than Brakka only in the way a hill was smaller than a cliff. One of his tusks had broken and been mended with gold. His stone tablets hung so thick across his chest that he chimed when he breathed.

"Brakka of Third Arch," he said. "You opened bone-road to unpaid travelers."

"I did."

"You brought crown violence inside ancestor."

"Crown violence struck ancestor outside first."

Several trolls rumbled approval. Several did not. Troll debate, Mara was learning, happened partly in sound and partly in pressure. The chamber felt like weather deciding whether to become a storm.

The elder turned to Mara. "Little ash made vow too large."

"People keep telling me that after accepting it," Mara said.

Kesh covered his eyes.

Brakka's mouth twitched.

The elder did not smile. "A vow beyond strength becomes lie."

Mara wanted to say she knew. Instead she looked at Pell, at Essa, at Tollen, at Rella and Othen and Niv. She thought of the black wagon ahead, of Joryn, of every name she had touched and every name she had not reached in time.

"Then help make it a road," she said.

Silence.

Brakka looked at her sharply.

Mara stepped toward the vow-stone. "If a vow is a bridge, it needs more than one person crossing. I cannot carry every name from every dead worker to every living witness. But Kell Ashgate can. Goblin roads can. Troll bridges can. Anyone who hears can become part of it."

The elder's eyes narrowed. "You ask clans to carry human dead?"

"I ask anyone who uses a road to admit roads carry more than feet."

Kesh whispered, "That was almost good."

"Almost?"

"I have notes."

The elder lifted one massive hand. "Stone decides weight."

He pressed his palm to the vow-stone. Brakka did the same. One by one, trolls added hands. The chamber filled with a sound like distant avalanche. The vow-stone darkened where each palm touched, drinking witness. Then Brakka reached for Mara.

Mara hesitated.

She had given enough blood to old things lately.

Brakka did not rush her. That mattered.

Mara placed her bandaged hand on the stone.

Cold shot through her. Not cinder cold. Mountain river cold. It ran up her arm, through her chest, into the place where the vow had settled. For a moment she felt roads: the Third Arch under siege, the Old Jaw swallowing secrets, Kell Ashgate alleys, goblin plank paths, royal roads built straight over graves, little foot trails made by children avoiding foremen. Every road remembered refusal. Every bridge remembered weight.

Then the stone asked a question without words.

Who may challenge you?

Mara almost said no one. Not because she believed it, but because fear loved that answer. No one could challenge you if no one could stop you. No one could make you small again. No one could take your vow and twist it.

But a vow no one could challenge was a crown.

"Those whose names I carry," she whispered. "Those whose dead I speak for. Those who walk the road with me."

The stone warmed.

Brakka exhaled, a long rumble. "True enough to bear."

The elder removed his hand. "Bone-road opens."

The chamber shifted. Stone ground against stone somewhere below. A hidden passage opened behind the vow-stone, sloping down through the arch toward the cliff road where Joryn's wagon had vanished.

Mara pulled her hand away. The bandage was wet, but not with blood. Clear water soaked it, smelling of rain on old stone.

Niv stared at her. "Are you a troll now?"

"No."

"Could you be?"

"Also no."

Brakka considered. "Small for it."

"Thank you."

"Not praise. Measurement."

For reasons Mara could not defend, that made her laugh. It broke the chamber's pressure. Even the elder's mouth twitched. The freed prisoners breathed again. Kesh clapped Niv on the shoulder and told him never to ask useful questions without charging.

They rested for twelve minutes because Caldus insisted on twelve and Brakka claimed thirteen belonged to funerals. Saelith and Ilyr were not yet with them. Tavi was back at the market. Their company was incomplete, strange, and already too entangled to abandon cleanly.

At the passage mouth, Brakka stopped beside Mara.

"You hate vow less?"

"I hate bad vows more."

"Good. Hate can guard door if taught manners."

"Does yours have manners?"

Brakka smiled, showing tusks. "No. It is young."

They descended.

Behind them, the trolls began carving new marks into the chamber wall: Pell Orwick, Essa Brant, Tollen Reed, Rella, Othen, Niv, and Mara Venn, who had made a vow too large and survived the stone's first question.

They did not descend at once.

Brakka made them wait in the shadow of the passage while she listened to the stone. This, apparently, was not a metaphor. She knelt with one palm flat on the floor and her ear almost touching the wall, while Kesh shifted from foot to foot with the reverence of a man watching a door decide whether to invoice him.

"What does it say?" Mara asked.

"Many things."

"Could it say the useful ones?"

"Stone speaks in weight. You want gossip."

Mara looked toward the darkness below. The black wagon had stopped somewhere beyond the bend. She could not see it, but she could feel time moving away from her like water through fingers.

Brakka lifted her head. "Road below has broken oath."

Kesh closed his eyes. "That sounds expensive."

"Bridge promised passage after old rockfall. Crown mended with iron and did not name dead builders. Their weight remains. Road angry."

Mara stared. "Roads can be angry?"

"Roads can be made of anger. Humans do this often."

Niv, crouched beside Kesh, whispered, "Is that why crown roads are straight?"

Kesh patted his shoulder. "Child, that is either profound or treason. Often a profitable overlap."

Brakka pointed to a side cut almost hidden by hanging roots. "We go anger's edge. Quiet. No metal on stone."

Caldus looked down at his mail.

"You are entire metal," Kesh said.

"I am aware."

Brakka removed a coil of woven root from a wall niche and tossed it to him. "Wrap."

So the disgraced knight of Harrowmere stood in a troll passage while a goblin boy and a dead courier helped bind strips of root around his mail to keep him from ringing like dropped cookware. Mara would have laughed if her brother had not been somewhere below. Caldus endured the process with the expression of a monument being decorated by vandals.

When they were done, Pell touched the root binding at Caldus's wrist. His cloudy eyes cleared for an instant.

"Sir," he whispered.

Caldus looked as if he might argue with the title again, but did not. "Pell."

The dead man's hand tightened once, then fell away.

That was another kind of bridge, Mara thought. Not forgiveness. Not yet. But the smallest possible crossing.

They moved along anger's edge, where the passage narrowed to a ledge outside the bridge bone. The canyon opened beside them. Stars shone below in full daylight. Wind clawed at their clothes. The tollhouse grew clearer with every careful step. Mara could see a pale-cloaked woman now, tall and white-haired, standing beside the black wagon with one hand resting on the door. She was not threatening anyone. That made her worse.

The cinder cage hummed once.

The woman looked up.

Across distance, wind, stone, and law, her gaze found Mara.

Mara felt the hymn-script cloth again around her wrists, tightening with beautiful courtesy.

Then the woman turned back to the prisoner at her feet and touched his brow with two fingers.

Joryn screamed.

Mara moved.

This time, no one was fast enough to stop her.

Ahead, the crown road waited in the dark, and every step Mara took felt less like pursuit and more like the beginning of something the crown had not meant to build.""",
    13: r"""## Chapter 13: The Dead Remember Names

Arveth the Named was waiting in a ruined tollhouse with a cup of tea.

That was the first unreasonable thing about him.

The second was that the tollhouse had no roof, no hearth, and no visible means of boiling water. It clung to the cliff road below the Third Arch, half-swallowed by ivy and old rockfall, its windows open to the canyon wind. Yet a kettle steamed on a flat stone beside him, and the cup in his long gray fingers gave off the smell of bitter leaves and mint.

The third unreasonable thing was that he was dead and seemed embarrassed by how obvious this was.

He rose when Mara entered, carefully, as if his bones were a library ladder. His skin was parchment-gray, drawn tight over a narrow face. Silver thread stitched a clean line up one side of his throat, but unlike Pell's brutal black stitches, these had been placed with care. His eyes were pale, clear, and very tired. He wore a scholar's robe patched with travel leather, and around his wrist hung a bracelet of small bone plaques, each carved with a name.

"Mara Venn," he said. "You are late."

Mara lifted the cinder cage. "Everyone keeps saying that like I received an appointment."

"You did not. That is why I risked tea. Would anyone else like some?"

Kesh appeared behind Mara, took in the dead scholar, the tea, and the ruined tollhouse. "I have several questions and resent all of them."

"Excellent," Arveth said. "Curiosity is the last decent vice."

Caldus entered with his sword half drawn. Brakka ducked through the broken doorway and filled most of what remained of the room. Pell, Essa, Tollen, and the rescued prisoners gathered near the wall. The named dead had grown quieter since the vow-stone, steadier but thinner somehow, as if every mile stretched the thread holding them.

Arveth saw them and bowed.

Not to Mara. To them.

Pell bowed back, awkward under his scarf. Essa began to hum, then stopped when Arveth lifted one gentle hand.

"No command reaches here," he said. "Not for a little while."

Mara did not like the little.

Arveth poured tea into chipped cups that appeared from a satchel far too small to hold them. Kesh watched closely, perhaps hoping to learn the trick or steal the cups. Brakka sniffed hers, suspicious, then drank it in one swallow and looked betrayed by its temperature.

"You are wondering what I am," Arveth said.

"I was raised not to ask rude questions of corpses," Kesh said.

"And yet you look professionally pained by restraint."

"It is a burden."

Arveth smiled. The expression made him look almost alive and, somehow, sadder. "I am undead, yes. I am also Arveth of Orrowen, witness clerk of the seventh civic court, executed under three governments, vindicated by none, and still in possession of my name through stubbornness and clerical error."

Mara sat because her knees had begun making arguments. "You know about Mordane's wagons."

"I know about the practice that made them possible. Mordane did not invent it. He industrialized it, which is the talent of small men with large budgets."

Caldus lowered his sword a fraction. "Necromancy."

"A chapel word. Imprecise, morally dramatic, useful in sermons." Arveth touched the bracelet at his wrist. "Cinders hold memory. Names steady memory. Commands can be fastened where names have been cut away. The dead become obedient not because they are empty, but because something has been nailed over the door from inside."

Pell made a sound.

Arveth turned to him. "Yes. You are still in there. I am sorry."

The room changed around those words. No revelation, no blue fire, no bridge law. Only apology, offered without trying to own the pain it named.

Mara's throat tightened. "Can they be healed?"

"Define healed."

"Do not do that."

"I must. It is where false hope hides." Arveth folded his hands around the cup. "Some can be steadied. Some can be released. Some can remain, if their name is held and their will is their own. Some are too damaged by command to do more than rest. None are tools unless someone makes them so."

Rella, the shaved-headed prisoner, whispered, "The crown says the dead serve by mercy."

"The crown says many things. That is one of its diseases."

Kesh gave a small approving hum.

Mara pulled Pell's token from her neck. "He asked me to tell Lio and Tam."

"Then you must."

"I know."

"No," Arveth said. Not harshly. Precisely. "You know the promise. You do not yet know the work. The living do not always want the names returned. Names bring grief. Grief brings anger. Anger asks who profited. Many households prefer ghosts to accounting."

"That does not release me."

"Good."

Brakka rumbled approval.

Caldus had gone pale. Not from fear this time. From recognition. "You said Mordane did not invent it."

"No."

"How old?"

Arveth looked toward the window, where the Third Arch cut a dark curve across the starry canyon below. "Older than Harrowmere. Older than the split courts of the elves. Older than most maps currently lying about their own importance."

Mara thought of the cinder under Kell Ashgate, of her father answering the seam, of the memory moth speaking in his voice. "Dragons."

Arveth's pale eyes returned to her. "Careful."

"Everyone says that after it is too late."

"Because late is when people begin listening."

He stood and crossed to the cinder cage. The shard brightened as he approached. The silver stitches in his throat glowed faintly.

"This is not simply a shard," he said.

Tavi had said the same. Mara hated when clever people agreed about bad news.

"What is it?"

"A splinter of a listening organ. Perhaps from the cinder beneath Kell Ashgate. Perhaps from something older under it. You did not wake it by being chosen. You woke it by being legible."

"Tavi said that word too."

"Then your gnome is irritating but promising."

"She is not my gnome."

"No one useful is anyone's for long."

Caldus stepped closer. "Can Mordane track it?"

"Yes."

"Can he track her?"

Arveth looked at Mara with apology already in his face. "More easily now."

The room went cold.

Outside, from the crown road below, came the distant sound of wheels.

Mara stood so quickly the tea sloshed. "Joryn."

Arveth lifted one hand. "Wait."

"No."

"If you run now, you reach the road after the wagon passes and before the soldiers behind it do. That is an excellent arrangement if your ambition is capture."

"Then help us."

"I am."

He reached into his satchel and withdrew a small ledger bound in green-black leather. Its edges were water-stained, its clasp made from bone. He held it out to Caldus.

Caldus did not take it. "What is that?"

"A partial register of mercy transfers between Kell Ashgate, Harrowmere, and three facilities that officially do not exist."

Every face in the room turned toward him.

Arveth looked apologetic again. "I steal slowly. It is a flaw of being thorough."

Caldus took the ledger at last. His hand shook when he opened it. Names filled the pages in three inks. Dates. Work marks. Mercy seals. Transfer routes. Some lines were crossed out with red. Some had small circles beside them.

Mara found Joryn's name on the fourth page.

Alive, the mark beside it said.

Holding, north foundry route. Priority: tongue uncut.

She read the line three times before she understood the last part.

"They have not tagged him yet."

"No," Arveth said. "They are saving him for someone who wants to ask you questions."

Mara closed her eyes. Relief and terror struck together so hard she could not separate them.

Kesh leaned over the ledger. "North foundry route branches at Stonewake Ford. If we leave now and Brakka's bone-road does not murder us for trespass, we can cut ahead."

"It will not murder," Brakka said.

"That is a suspiciously narrow promise."

Arveth placed a bone plaque on the table. A name was carved into it: PELL ORWICK. Beneath it, in smaller letters, LIO. TAM.

"For when you find them," he told Mara.

Pell bowed his head.

Mara took the plaque and felt her vow settle around it.

"Are you coming?" she asked Arveth.

He looked mildly surprised. "Obviously."

"Why?"

"Because Mordane is using my notes badly."

Kesh blinked. "That is your reason?"

"No. But it is the one least likely to become sentimental in public." Arveth lifted his satchel. "Also, someone should explain death to all of you before you make further policy."

Brakka smiled. "I like dead clerk."

"Witness clerk," Arveth corrected.

The wheels below grew louder.

Mara gripped the ledger, Pell's plaque, and the cinder cage. She had wanted a straight road to Joryn. Instead she had gained a vow, a troll, a dead scholar, a ledger full of names, and the knowledge that the crown's cruelty had roots older than the crown.

The story was getting larger again. She hated that.

But Joryn was alive.

For the moment, that was a bridge strong enough to cross.""",
}


EXPANSIONS: dict[int, str] = {
    9: r"""The stair through the drowned tollhouse did not go directly up or down. It turned through old rooms half-filled with black water, past hooks where toll lamps had once hung and counters worn smooth by hands that had paid to cross before the marsh swallowed the road. Names were carved everywhere. Not grand names. Not kings. Drovers, ferrymen, eelers, smugglers, children who had learned letters by cutting them badly into public wood. Some had been scratched over. Some had been circled. Some had dates beside them and little marks Mara did not understand.

Pell stopped at one post and touched a name nearly hidden under lichen.

"Friend?" Mara asked.

His head moved in a way that might have been no, or yes, or both after death had damaged the grammar of his body. Tollen took the slate from under his coat and wrote with wet chalk: Toll names. Safe crossing if remembered.

Kesh read it over Mara's shoulder. "Old practice. You carved your name if you crossed and wanted the road to know you were not sneaking. Some places charged less if you returned with the same name."

"How does a road charge?"

"Badly, if annoyed."

"You answer everything like that."

"Because you keep asking questions whose true answers have teeth."

The cinder cage gave a low answering note. Mara tightened her grip. The memory moth dust had left a taste in her mouth like cold metal and overripe fruit. Worse, it had left doors open. She could feel the remembered storm from childhood waiting behind her eyes. If she blinked too long, she saw her father's marked palm, heard the lower seam ring, felt a child's mouth forming an answer she had spent years forgetting.

"You said the physician paid you," she said to Kesh.

"A heroic attempt to change the subject from haunted toll architecture."

"His name."

Kesh stepped over a gap where water breathed up through the floorboards. "He did not give one."

"Describe him again."

"Human. Hands too clean for travel. Ink stain on the left thumb. Physician's pin from Harrowmere, not chapel issue. He wore a ring under his glove. Silver, flat, no jewel. Seal mark pressed into the skin when he took the glove off to pay me."

Caldus, behind them, said, "Mordane's office uses flat silver seals."

"You know that because?"

"Because I delivered reports there before I knew what the reports meant."

No one had a good answer to that. Even Kesh let it stand.

They reached a chamber where the tollhouse roof had collapsed and moon-pale fungus climbed the broken beams. Memory moths hung there in sheets, asleep or pretending. Their wings trembled with words not yet spoken. The route out lay across a fallen beam above chest-deep water.

Kesh went first. Then Mara, cage held high. Halfway across, a moth opened on the beam beside her boot and spoke in Joryn's voice.

"You always run toward the thing that can hurt you most."

Mara froze.

"That is not him," Caldus said.

She knew. She knew the way one knew a knife was sharp. The voice was wrong by a hair, too polished, too complete. Joryn's real voice always carried the grit of whatever work had stolen sleep from him. But the words were his sort of words, and that was enough to hurt.

Another moth opened.

Her mother's voice this time. "Let your brother carry it, little flame."

Mara swayed. The beam shifted.

Kesh turned back. "Vent-girl."

"Stop calling me that."

"Then keep moving, Mara."

Her name in his voice did what the moths had tried to counterfeit. It gave her a place to stand. She crossed the beam and stepped onto broken stone just as the moths rose again, stirred by the cinder, by memory, by the living foolish enough to bring both through their house.

The swarm followed them out.

For a hundred yards the road became running, slipping, half-falling through water and rotten boards while moths burst around their heads speaking secrets in stolen voices. A moth with Sedge's voice listed company fines. A moth with Caldus's voice said, "No inspection required." A moth with Kesh's voice laughed, "Both payments." A moth with Mara's own voice whispered, "If you command them, they will stop suffering."

She almost answered that one.

Pell saved her.

He stumbled into her path and caught the cage against his chest. The cinder flashed through reed mask and cloth. For a moment Mara saw him not as the dead thing beside her but as he had been: broad hands, crooked grin, boots by a hearth, two boys climbing him like a tree while a woman in a blue kerchief told all three of them they were fools. The memory did not belong to her. Pell gave it anyway.

Tell Lio. Tell Tam.

"I will," she said.

The moth wearing Mara's voice turned to ash.

When they finally burst from Old Jaw into daylight, they came out below the canyon road with mud to their waists and secrets clinging like cobweb. The black wagons were gone, but the warm chain link and wheel ruts showed the route. Across the rising land, seven stone spans cut the sky.

Kesh leaned against a rock, panting. "Good news. The road did not eat us."

Caldus looked back at the dark mouth of Old Jaw, where the last moths hovered just inside the shade.

"Bad news?" Mara asked.

Kesh wiped silver dust from his cheek. "It learned our names."

At the canyon rim, a horn sounded, low and vast, nothing like a royal signal. The Seven Arches had seen them coming.

Mara looked at Pell's token, at the chain link, at the bridges ahead, and understood that every road they took would remember them now. For a girl who had survived by being forgettable, that felt like a second kind of exposure.

She kept walking anyway.""",
    10: r"""They did not catch the wagon in the first rush across Third Arch.

Mara hated that sentence before anyone said it. It formed in Caldus's face, in Kesh's quick calculations, in the distance between her and the black wheels already rolling toward the far guardhouse. She ran until her breath scraped. The bridge was too long. The wind shoved at her with both hands. Every star below seemed to hold its place while she crossed no distance at all.

Then Brakka caught her by the back of the coat and lifted.

Mara's boots left stone.

"Put me down."

"You run like falling knife," Brakka said. "Sharp. Useless after first wall."

"My brother is on that wagon."

"Maybe. Maybe not. You die before knowing if stupid."

Mara twisted hard enough to hurt herself. Brakka set her down, not gently, beside a carved marker halfway across the bridge. The black wagons rolled through the far gate. Soldiers turned. One pointed. Horns answered from both ends of the arch.

Caldus arrived, breathing hard. "She's right."

"Do not start sentences like that," Mara snapped.

"You cannot outrun horses on an open bridge."

"I do not need to outrun horses. I need to reach the wagon."

Kesh bent over with both hands on his knees. "A distinction beloved by corpses."

The cinder cage hummed once. The vow on Mara's shoulders warmed, not urging and not restraining. Witness, it seemed to say, which was infuriating advice when what she wanted was speed.

Brakka pointed with her maul to the carved marker beside them. It was a waist-high stone figure with no face, only hands extended over the road. Travelers had pressed tokens into its palms for so many years that the stone fingers had worn smooth. Around its base were names.

"Toll point," Brakka said. "All who cross recorded."

"Can it tell us if Joryn crossed?"

"If name paid."

"He was a prisoner."

"Then road remembers weight, not name."

Mara crouched before the marker. The stone was cold despite the sun. She put one hand on it and felt nothing at first except the sting of her bandage and the tremor of distant soldiers. Then the cinder cage answered. Its hum dropped into the stone.

Weight moved through her.

Not images. Not exactly. Pressure. Wheels. Iron. Five bound prisoners in the first wagon, one sick, one praying, one angry enough to kick. Three in the second. One broad-shouldered, half-conscious, pulse strong, wrists raw. The road did not know Joryn's name, but it remembered the way his weight had shifted when he tried to rise.

"He crossed," Mara said.

Kesh's ears flicked. "Alive?"

"Alive."

The word held everyone for one breath.

Then the near-side soldiers reached the bridge.

They came with crossbows, command rods, and a captain in a black cloak who shouted for Brakka to surrender royal fugitives. He did not sound as if he expected obedience. He sounded as if he wanted witnesses to his reasonableness before violence made its usual argument.

Brakka turned with grand slowness. "Third Arch has not received crown request in proper form."

The captain blinked. "What?"

"Improper request denied."

"This bridge stands under Harrowmere protection."

The troll looked around at the ancient span, the canyon stars, the carvings older than the kingdom, and then back at him. "No."

Kesh whispered, "I love bureaucracy when it has a maul."

The captain lifted one command rod. Not toward Brakka. Toward Pell, Essa, and Tollen.

Mara felt the command gather before it fired. The cinder cage went hot. She remembered the names from the bridge, from the tollhouse, from the ledger not yet in Caldus's hands. Her vow tightened.

Brakka saw where the captain aimed.

"Dead are under road witness," she said.

"The dead are crown material."

Every troll on the bridge heard that.

Stone changed when anger entered it. Mara felt the Third Arch become more than road beneath her feet. It became a held breath. Brakka's tablets clicked softly as she stepped forward.

"Say again," the troll said.

The captain was not wise enough to fear invitation. "The dead are crown material."

The Third Arch answered.

The face carved into the toll marker opened its smooth stone mouth. Around the bridge, every worn figure did the same. No sound emerged, but the command rod in the captain's hand cracked from tip to grip. Blue sparks spilled between his fingers. He cried out and dropped it.

Brakka smiled.

"Improper material claim denied."

Then the siege horn sounded from the far guardhouse, and the choice to stand became a battle.""",
    11: r"""The rescued prisoners from the first wagon were not grateful in any tidy way.

Rella, the woman with the shaved head, punched Caldus when he cut her ropes because he wore mail and she woke seeing armor. Father Othen blessed everyone, cursed twice, then apologized to the nearest troll for blessing without consent. Niv, the courier boy, bit through his gag, spat cloth into the road, and demanded to know whether anyone had seen his satchel. When Kesh said no, Niv called him a mud-eared vulture in what sounded like competent goblin.

Kesh looked delighted.

"Who taught you that?"

"Your cousin."

"That narrows nothing."

Mara wanted to ask every one of them about Joryn. Had they seen him? Was he awake? Had they heard the soldiers say where the second wagon would stop? But Rella was shaking so hard she could not stand, Othen had a burn in the shape of a mercy seal on his wrist, and Niv's first brave fury had collapsed into hiccuping breath. Questions were another kind of demand. Mara hated that compassion had timing.

The battle had not ended cleanly. Battles, she was learning, rarely understood when the important part was over. Trolls still wrestled soldiers near the far parapet. One ox from the broken siege engine had decided the safest place in the world was behind Brakka and refused all royal efforts to persuade it otherwise. Smoke from Kesh's axle improvement drifted low over the bridge. The shattered command rod hissed every time rain touched it.

Caldus dragged the remains of the rod away from Pell with the edge of his shield.

"Do not touch it," Mara said.

"I was not planning to develop a hobby."

The rod pulsed weakly. Pell flinched.

Mara knelt beside it, cage in one hand. The cinder shard inside flickered like a coal under breath. The rod's command bead was smaller, darker, cut smooth and mounted in iron. Not a cinder-heart. A splinter. A disciplined cruelty.

"Can it still command them?"

Caldus looked toward the named dead. "Not if I break it."

"Wait."

He did, though his jaw tightened.

Mara listened.

The bead was not alive the way her shard felt alive. It was stored pressure, names scraped out and replaced by orders. Under the order lay something else: a worker's lullaby, half-burned; the smell of a chapel infirmary; a hand gripping a cot frame while someone said mercy required stillness. Mara drew back so fast she nearly fell.

"These are made from people too."

Caldus closed his eyes. "Of course they are."

There was no surprise in his voice, only the exhaustion of a man whose worst guesses kept becoming practical.

Brakka came to them with stone dust on her cheek and royal blood drying on her maul. "Far wagon gone to cliff road."

"How far ahead?" Mara asked.

"Far."

"That is not a measure."

"It is when chasing on foot."

Kesh appeared dragging Niv's satchel from under a dead soldier. "Cliff road rejoins at Stonewake Ford if the old maps are still arrogant. There may be a shorter way through bridge bones."

Brakka grunted. "Shorter. Not kinder."

"Kind roads are a myth told by shoe sellers."

Rella had stopped shaking enough to listen. "You are going after the second wagon?"

"My brother is in it," Mara said.

The woman's expression changed. She touched her shaved head, where small cuts marked places hair had been torn out rather than cut cleanly. "They took my wife three days ago. Mercy ward at North Harrow. If you find records..."

She did not finish. She did not need to. Mara's vow settled around another name not yet spoken.

"Her name?"

"Lysa Mar."

Mara repeated it. "Lysa Mar."

The bridge warmed under her boots.

Father Othen gave Mara a look too sharp for a harmless old priest. "Be careful, child. Institutions love people who collect grief. They will call you necessary while making you hollow."

"People keep warning me after giving me more grief."

"Yes," he said sadly. "That is how we make heroes and then blame them for bleeding."

No one had time to answer because the far guardhouse exploded.

This one was not Kesh's doing. He said so immediately and with some disappointment. The blast came from inside the guardhouse, blue-white and silent for the first heartbeat, then thunder slammed across the bridge. Stone chips sprayed the road. The trolls shouted. The remaining royal soldiers broke and ran.

Through the smoke, Mara saw a figure on the cliff road: a woman in a pale cloak, standing beside the second wagon. Too far to see her face. Close enough for the cinder cage to hum.

The woman lifted one hand toward Mara.

Not greeting. Measurement.

Then she stepped into the wagon, and the horses lunged forward into the cliff cut.

"Who was that?" Mara asked.

Caldus looked as if he had swallowed iron. "Pale Bough."

"Light elf?"

"Oathkeeper, maybe. Or worse."

Kesh muttered a word in goblin that required no translation.

Brakka pointed toward the bridge bones. "If going, go."

Mara looked at Rella, Othen, Niv, the named dead, the injured trolls, the shattered bridge. Every road away from here demanded that she abandon someone. Every road forward demanded that she arrive late.

She hated leadership already, and she did not even have any.

"Rella and Othen stay with the trolls," she said. "Niv too."

"No," Niv said.

"Yes."

"My satchel is going where I go."

"Your satchel can make wiser choices."

Kesh crouched to the boy's height. "Can you run quiet, bite only enemies, and refrain from correcting adults at tactically inconvenient moments?"

Niv thought about it. "No."

"Honest. I like him."

Mara almost said no again. Then she saw the courier belt, the way Niv had tracked every movement on the bridge, the fury in him looking for a road instead of a wall.

"You stay behind Caldus," she said.

Niv nodded solemnly.

"And if Caldus says stop, you stop."

"Does he say useful things?"

"Sometimes by accident."

Caldus gave her a look. It had less despair in it than before. Maybe he was getting used to her. Poor man.

They entered the bridge bones through Brakka's hidden door while the trolls sang over the damaged arch and the freed prisoners spoke Lysa Mar's name until Mara had it anchored. Behind them, the Third Arch held. Ahead, the cliff road swallowed the second wagon and the pale-cloaked woman who had looked at Mara like an answer to a question Mara had not agreed to ask.

The story widened again, and all Mara could do was run through it.""",
    12: r"""The hidden passage through the bridge bones did not permit haste in any form recognizable to Mara.

It sloped, twisted, narrowed, widened, doubled back, and once required everyone to crawl through a space Brakka claimed was ceremonial rather than badly designed. Kesh disputed this in whispers until the ceiling lowered another inch above his head, at which point he apologized to the architecture. The ceiling rose again.

"The bridge is petty," he said.

"The bridge has ears," Brakka replied.

"I am praising its attention to detail."

Mara crawled behind Niv, who moved with the quick confidence of someone used to courier ducts and adult underestimation. Pell and the named dead followed more slowly. Arveth was not yet with them, but the thought of an undead scholar had begun to seem possible in a world where roads accepted apologies and bridges took offense.

The vow-stone's water had dried on Mara's bandage and left pale mineral lines across the cloth. Every time she touched a name, the lines tingled. Lysa Mar. Pell Orwick. Essa Brant. Tollen Reed. Rella. Othen. Niv. Joryn Venn. The names did not sit quietly in her. They arranged themselves like people waiting for doors to open.

Halfway through the passage, Brakka stopped before a wall carved with hundreds of little bridges.

"Why stop?" Caldus asked.

"Because little ash must learn one more thing before road teaches with teeth."

Mara leaned against the wall, breathing hard. "Can the teeth wait?"

"Teeth never wait. That is teeth nature."

Kesh nodded. "Hard to argue."

Brakka touched one carved bridge with her thumb. "This mark is vow kept."

She touched another, cracked through the center. "Vow broken."

Another, crossed by three lines. "Vow challenged."

"What happens when a vow is challenged?" Mara asked.

"Those bound gather. Weight is spoken. Harm is counted. Stone listens. Vow changes, stands, or dies."

"And if powerful people refuse the challenge?"

Brakka's eyes met hers. "Then vow was already dead. Only chain remains."

Mara thought of company contracts, of chapel mercy, of the crown calling the dead material. "Humans are very bad at vows."

"Trolls also bad. We only keep records longer."

That surprised a laugh from her.

Brakka looked pleased, or perhaps only less severe. "You think trolls born wise? No. We are born loud. Wisdom is what happens when loud lasts long enough to hear echo."

They moved on.

The passage opened at last into a chamber where old supplies had been stored in stone bins: dried roots hard as nails, clay jars sealed with wax, blankets wrapped in oilskin, coils of rope, and a rack of stone-headed spears. Brakka distributed food with grave ceremony. Kesh accepted a root, bit it, and immediately looked betrayed by every choice that had led him there.

"This is not food."

"It is bridge ration."

"That is a legal category, not a flavor."

Niv gnawed his with apparent indifference. "I have eaten worse."

"That is not the comfort adults hope children will provide."

Mara sat beside Pell and helped adjust the scarf over his mouth. His hands shook less now. Essa held the slate while Tollen wrote names he remembered from the wagon: Bek Sorn, Hala Vesh, Orit Dane. Mara repeated each one. The vow warmed. The cinder cage answered softly, not interfering, but listening.

Caldus watched from the supply rack.

"You are allowed to sit," Mara said.

"I am watching the door."

"There are six doors."

"I am suffering efficiently."

She almost smiled. Almost. "You knew the pale woman?"

His face closed.

"Caldus."

"I knew her order. The Pale Bough serves Lumenorath. Oathkeepers, healers, wardens of old law. If one is with Mordane's wagons, then the foundry reaches farther than I thought."

"Or they are against Mordane and still took Joryn."

"That possibility is not kinder."

No, it was not. Mara rubbed her thumb over the chain link. The world kept refusing to divide into captors and rescuers, monsters and people, roads and traps. Everything had hinges. Everything opened the wrong way if pushed by fear.

Brakka sat opposite her, making the stone floor creak. "You carry brother-name heavy."

"He carried mine first."

"Explain."

Mara did not know why she answered. Perhaps because the passage smelled of stone and old vows, and Brakka asked like weight mattered.

"After our father died, the company wanted me in the vents. I was small. Small pays less. Joryn lied and said I had fever fits, that I froze in tight places, that I would cost more dead than alive. He took double shifts for a year to keep me aboveground. Then winter came and we needed coin anyway."

"He failed?"

Mara's first instinct was anger. Brakka's face held no insult, only the blunt edge of fact.

"No," Mara said. "He bought me a year."

Brakka nodded. "A year is bridge. Not forever. Still crossing."

That settled in Mara more gently than comfort would have.

Kesh, who had been pretending not to listen, cleared his throat. "If we are done appreciating temporary infrastructure, the wagon is becoming farther away."

Brakka rose. "Bone-road opens to cliff path soon."

"Soon in troll?"

"Soon."

"Deeply informative."

They packed quickly. Niv tucked two bridge rations into his satchel. Kesh saw and added a third with the air of a bad influence performing charity. Caldus checked the prisoners' knots, then cut them shorter so they could be removed quickly if needed. Mara took one last drink from a stone basin where the water tasted of rain and iron.

Before leaving, she pressed her palm to the wall of carved bridges.

"If I break it," she whispered, "tell me."

The stone did not answer in words. It warmed once under her hand.

Brakka grunted. "Good. Road likes honest fear."

"Does road like anything pleasant?"

"Road likes being road."

They emerged from the bridge bones onto a ledge above the cliff path, with the crown road below and wheel tracks fresh in the mud. Far ahead, a black wagon crawled toward a ruined tollhouse perched over the next ravine. Smoke rose from its chimney.

Kesh shaded his eyes. "That tollhouse is supposed to be empty."

Pell, below the scarf, made a sound like recognition.

Mara lifted the cinder cage.

Inside, the shard glowed as if someone in the ruin had just spoken her name.""",
    13: r"""Arveth let them argue for exactly seven minutes after revealing Joryn's entry in the ledger.

Mara knew because Niv, unable to bear silence, counted under his breath until Kesh told him that numbers attracted tax spirits. The boy stopped at once, then restarted more quietly. The argument itself circled like a trapped bird. Mara wanted to run. Caldus wanted to scout. Kesh wanted to know whether the tollhouse had rear exits, side exits, roof exits, and exits that had not yet become exits but might be persuaded. Brakka wanted someone to state the vow governing the rescue before everyone pretended speed excused confusion.

Arveth poured more tea.

"How are you doing that?" Mara demanded.

"By allowing water to become hot near leaves."

"There is no fire."

"Death teaches small economies."

Kesh pointed at him. "That is the sort of sentence people say before charging admission."

Arveth looked pleased. "You may yet become civilized."

Caldus closed the ledger. "We need what you know about the north foundry route."

"Yes."

"Now."

"Impatience is often mistaken for clarity."

"My patience was court-martialed."

Arveth's pale eyes sharpened with interest, but he did not press. "Very well. The wagon below will not carry your brother directly to a foundry. Not yet. Mordane's people use holding sites because living prisoners require sorting. Labor, leverage, experiment, ransom, silence. Your brother is leverage."

The word made Mara's hands cold.

"Against me."

"Most likely."

"Then they will keep him alive."

"Until leverage becomes less useful than punishment."

No one softened that. Mara was grateful and furious.

Arveth opened another section of the ledger and turned it toward them. The entries were marked with tiny symbols beside the names: hook, candle, chain, eye, crown. He tapped the eye.

"Priority: observe. That mark appears beside your brother. It appears beside seven others taken from cinder-adjacent families in the last six months."

"Cinder-adjacent," Kesh said. "A phrase that should be illegal."

"Many useful phrases should be."

Mara leaned over the page. "Families like mine?"

"Miners. Bellkeepers. Chapel cleaners assigned to heat vaults. Gnome mechanics. A grave singer from Westmere. Two children from a town built on dragon-bone limestone."

The room seemed to tilt. "Why?"

Arveth touched his stitched throat. "Because cinders do not speak equally to everyone. Exposure matters. Repetition matters. Labor matters. Grief matters. Bloodline only in the sense that families often inherit the same dangers because poverty assigns them the same work."

Tavi had been right. Not royalty. Legibility.

"My father heard it," Mara said.

"Yes."

"You knew?"

"I suspected when I saw your name."

"My name is in your ledger?"

Arveth hesitated.

That was answer enough.

He turned one more page. There, in a hand different from the others, was written: VENN, MARA. Vent runner. Responsive. Do not tag unless authorized.

Mara could not hear the room for a moment. Do not tag. Not because she was safe. Because someone had plans for her tongue.

Caldus reached for the ledger as if to tear the page out. Arveth stopped him with one dry hand.

"Do not destroy records because they hurt. That habit built half the world's graves."

Caldus let go, breathing hard.

Brakka touched the hilt of her maul. "Who wrote?"

"Mordane's office. Perhaps Mordane himself. The hand is too disciplined to identify from this copy."

Mara looked at her own name until the letters became scratches. She had thought the mountain made her visible. The crown had been watching before the vent. Perhaps not understanding. Perhaps only noticing patterns. But enough.

"Why leave this where we could find it?"

Arveth smiled without humor. "I did not find it. I stole it, copied it, returned the original, stole it again when the copy proved incomplete, then spent three weeks being chased by a man with an admirable hat and no imagination."

Kesh placed one hand over his heart. "A fellow professional."

"Hardly. He wore the hat sincerely."

Despite herself, Mara laughed once. It broke something in her chest that had been too tight to breathe around.

Arveth closed the ledger gently. "You are not the first person the cinders answered. You may not be the last. But you are the first I have found who speaks names back into the dead without immediately trying to own them."

"That is a low bar."

"History is mostly low bars decorated by victors."

Below the tollhouse, wheels ground over stone. The black wagon was moving again.

Caldus rose. "Plan."

Arveth pointed to a map scratched into the tollhouse table. "The road bends at Stonewake Ford. Wagons must slow there because the bridge has been out for twenty years and the replacement dislikes haste. If you take the goat ledge behind this ruin, you can reach the ford before them."

"Dislikes haste?" Kesh asked.

"It collapses."

"Ah. Strong preference."

"The pale-cloaked woman," Mara said. "Who is she?"

Arveth's fingers stilled on the map. "I saw her once in Harrowmere, behind a screen in Mordane's archive. She did not speak. Mordane did."

"Name."

"Saelith Dawnmere, if my informant had courage and accuracy in the same hour. Oathkeeper of Lumenorath. Healer. Attached to the Pale Bough."

Caldus swore softly.

Brakka looked between them. "Light elf law?"

"Old law," Arveth said. "Beautiful law. The sort that can make a cage feel like rescue."

Mara thought of hymn-script tightening around her wrists in the quarry road. "She bound me."

"Then she has touched this already."

Another road opened, not underfoot but in the story. Mara could feel it: Kell Ashgate to Mordane, Mordane to Harrowmere, Harrowmere to light elves, light elves to older crimes. She wanted one rescue. The world kept handing her systems.

Arveth packed his cups with maddening calm.

"We go to Stonewake Ford," Mara said.

"Yes."

"We get Joryn."

"We try."

"Do not improve my sentence."

"I am dead, not obedient."

Kesh laughed. Brakka rumbled. Caldus almost smiled and then remembered not to waste time.

At the door, Arveth paused beside Pell. The two dead looked at one another for a long moment. Mara wondered what passed between them: recognition, warning, grief, perhaps the simple relief of not being the only impossible thing in a room.

"Hold your name with both hands," Arveth told him.

Pell touched the scarf over his mouth. "Trying."

"Good. Trying is a living habit. Keep it."

They left the ruined tollhouse by the goat ledge, which Kesh immediately accused of being a rumor with rocks. The canyon wind shoved at them. Far below, water flashed white over Stonewake Ford. Ahead, the black wagon rolled toward the crossing with Mara's brother alive inside it and a light-elf oathkeeper riding beside him.

The goat ledge punished panic better than any lecture could.

Mara made it six strides before loose shale slid under her boot. The world dropped. She caught a root with her injured hand and pain tore up her arm bright enough to blind her. Below, the canyon waited with its impossible daylight stars. Above, Caldus swore and threw himself flat, one arm shooting over the edge.

"Give me your hand."

"This one is busy."

"The other one."

"Holding the cage."

"Drop it."

"No."

Kesh's face appeared beside Caldus's, upside down from Mara's perspective and deeply annoyed. "I admire commitment to bad priorities, but perhaps consider living."

The root creaked.

Brakka did not tell Mara to be calm. Brakka reached over both men, caught Mara by the back of her coat, and hauled her up as if retrieving laundry from a line. Mara hit the ledge on her stomach, gasping, cinder cage clutched under one arm.

For one heartbeat no one spoke.

Then Niv said, "That was stupid."

Mara coughed grit. "Yes."

The agreement seemed to alarm him.

Caldus crouched beside her. His face was white under the road dirt. "Do not do that again."

"He screamed."

"I heard."

"Then why are you all moving so slowly?"

The unfairness of it cracked something open. She knew it was unfair while saying it and could not stop. Caldus had bled for her. Kesh had betrayed and helped and nearly died on roads that hated him. Brakka had opened ancestral stone. The dead had carried their own pain beside hers. Still, Joryn had screamed, and every step not toward him felt like betrayal.

Arveth knelt in front of her.

He had followed lightly enough that she had forgotten he was dead, which seemed rude of reality.

"Because speed without arrival is vanity," he said.

"Do not give me scholar words."

"Very well. If you run at the woman in the pale cloak, she takes you too. Your brother becomes leash. You become key. Mordane thanks everyone for their assistance."

Mara looked away.

Below, the pale woman had stepped back from Joryn. He sagged between two soldiers but remained on his feet. Alive. Conscious. Hurt. The three words tore at one another inside Mara until none of them became comfort.

"What is she doing to him?"

Arveth watched carefully. "Testing response. Pain, perhaps. Memory pressure. Light-elf hymncraft can quiet wounds, bind oaths, preserve testimony, or convince the body that captivity is rest. It depends on the singer and the consent."

"He did not consent."

"Then it is violence."

The cleanness of that answer steadied her.

Saelith Dawnmere, if Arveth had the name right, lifted her hand again. This time a line of pale light moved from her fingers to the wagon door, drawing a sigil in the air. It was beautiful. Mara hated that it was beautiful. The soldiers around Joryn relaxed as if warmed by it. Joryn did not. Even from the ledge, Mara could see him fight to lift his head.

"He knows you are near," Caldus said.

"How?"

"Because if I were him, I would know."

That was not logic. It helped anyway.

Brakka set her maul down with a soft stone click. "We need branch under branch."

Kesh opened one eye. "Please tell me that means hidden path, not philosophical nightmare."

"Both possible."

Arveth pointed to the map scratched on the underside of the ledge in old toll marks. "There is a culvert beneath the ford. Built to relieve floodwater. If it still opens, it comes out behind the tollhouse stable."

"If it does not?" Niv asked.

"Then it is a grave with excellent drainage."

"You are bad at comfort too."

"Death edits priorities."

Mara sat up slowly. Her hand throbbed. Blood had seeped through the bandage again. The cinder cage rested against her ribs, warm but not screaming. She forced herself to breathe until the world stopped narrowing to Joryn's scream.

"Plan," she said.

Caldus nodded once, accepting the apology she had not shaped. "Kesh and Niv find the culvert mouth. Brakka opens anything that objects. Arveth tells us which dead we may meet before they tell us badly. I go first if there are soldiers."

"No," Mara said.

His eyes sharpened.

"You are wrapped in roots and jingle when anxious. Kesh goes first. You go second."

Kesh looked personally betrayed by her confidence.

"I was hoping to be decorative."

"You are not dressed for it."

Brakka picked up her maul. "Little ash learns command."

"No," Mara said. "I learn ordering friends badly."

The troll considered, then nodded. "Beginning of command."

That frightened Mara more than the ledge. But below, Joryn was being pushed back into the wagon, alive, and the pale woman was turning toward the ford. The road was moving again. So they moved with it, not as fast as fear demanded, but fast enough to arrive.

Behind them, high in the cliff, the ruined tollhouse stood with its roofless walls and cooling tea. Arveth had left one cup on the stone table for the dead who might pass after them. Mara had no idea whether that was sentiment, ritual, or scholarship.

She was beginning to suspect the best things were often all three.

The culvert mouth was hidden under a skirt of roots and white mineral scale. Kesh found it by nearly falling into it, which he insisted was an advanced scouting method. Niv found the release pin before anyone else could praise him, then pretended not to be pleased when Brakka grunted approval.

The grate over the culvert was iron, old and swollen with rust. Brakka could have torn it free. Caldus could have cut the weaker bars if given time. Instead, Arveth knelt beside it and tapped three times on the stone frame.

"If there is anyone in there with legal standing," he said, "we request passage."

Kesh stared at him. "Did you just knock on a drain?"

"One should be polite to infrastructure older than one's current government."

For a moment nothing happened.

Then something knocked back.

Niv made a small noise and immediately tried to look like he had not. The grate shivered. Rust flaked away. The bars lifted inward, not opened by hinges but by a pressure that remembered hinges as a social possibility. A smell came out: cold water, old moss, and the sour breath of things that had drowned with complaints unfinished.

"Politeness," Arveth said, "remains underrated."

"I am charging more for this road," Kesh muttered.

They entered single file. Kesh first, as ordered, though he described the decision as anti-goblin prejudice. Niv followed him with the slate tucked under one arm. Caldus went next, root-wrapped mail scraping softly. Mara followed with the cinder cage. Arveth came behind her, then Pell, Essa, Tollen, and Brakka last, because if the tunnel objected to her shoulders it would need to object with conviction.

The culvert ran under the ford in a low curve. Above them, water hammered over stone. Hooves crossed. Wheels groaned. Voices passed through the ceiling in broken pieces.

"...keep him awake..."

Mara stopped so abruptly Arveth nearly walked into her.

Joryn.

Not clear, not close, but his name lived in her body more truly than any magic. She pressed one hand to the culvert ceiling. Water seeped between her fingers. The cinder cage hummed, not loud enough to warn, only enough to listen.

"Move," Caldus whispered from ahead.

She did not.

Above, the pale-cloaked woman spoke. Her voice came through water and stone as a song almost too clean to be language.

"Joryn Venn, hear me. You are in pain. Let the pain become distant."

Mara's vision went red at the edges.

Joryn answered with something that might have been a laugh if he had not been hurt. "Pain pays rent. I know where to find it."

Kesh looked back at Mara and mouthed, Brother?

She nodded once.

Saelith Dawnmere's voice softened. "Your sister is alive."

The whole culvert seemed to stop breathing.

"I know," Joryn said.

"She is dangerous."

"She bites."

"The people around her will make her into a weapon."

"Then they should worry about the handle."

Mara pressed her fist against her mouth. The laugh that tried to come out would have broken her.

Arveth touched her shoulder, light as paper. "Remember him like this too."

Above, a soldier said something sharp. A door slammed. Wheels creaked forward.

"We can take them at the stable exit," Caldus whispered.

Kesh shook his head. "Too many boots. Four horses. Two rods, maybe three. Pale woman. Also whatever made that hymn-light."

"We cannot let them leave."

Mara forced herself to move. Each step through the culvert felt like betrayal until the tunnel bent and she saw the exit: a square of gray light behind rotted stable slats. Beyond it, the black wagon rolled past so close she could see mud on the wheels.

Joryn sat inside, wrists bound, face bruised, head up.

Their eyes met.

It lasted less than a heartbeat.

It lasted long enough.

Joryn shook his head once.

No.

Mara understood and did not. No, do not attack. No, not here. No, living first. No, use your head. No, rage after. Every lesson he had ever given her compressed into one stubborn movement while the wagon carried him away.

She nearly broke anyway.

Caldus's hand closed around her arm. Not restraining. Anchoring.

The pale-cloaked woman turned as the wagon passed the culvert. For the second time, her gaze found Mara through places sight should not go. Up close, Saelith Dawnmere looked younger than Mara had expected and older than anyone living should. Her white hair was braided with gold thread. Her face was calm, but there was strain around her mouth, as if whatever she had done to Joryn had cost her something she had not wished to spend.

She saw Mara.

She did not call the soldiers.

Instead, she lifted two fingers to her own wrist, where a thin band of pale light circled like the hymn-cloth that had bound Mara in the quarry road. Then she touched those fingers to the wagon door.

A mark appeared there, brief and white: a door-shaped sigil with one line broken.

Arveth inhaled, though he did not need to.

"What?" Mara whispered.

"That was not a command mark. That was a flaw."

"A what?"

"She showed us where the binding can break."

The wagon rolled beyond the stable yard and turned toward the north road.

Kesh looked from Saelith to Mara to Arveth. "I dislike helpful enemies. It complicates invoicing."

"She is still taking him," Mara said.

"Yes," Caldus replied. "And she just told us how to get him back later."

Mara hated later. Later was a room where powerful people stored the suffering of others. Later was how the company paid death shares, how chapel physicians explained mercy, how everyone told the desperate to become reasonable while wagons rolled away.

But Joryn had said no.

So she let the wagon go.

It was the hardest thing she had done all day, which was a crowded field.

When the wheels faded, Mara realized she was shaking. Not from fear now. From obedience freely chosen, which felt nothing like the other kinds. She had not obeyed Saelith or Caldus or Arveth. She had obeyed the person Joryn had spent years teaching her to be: angry, yes, but alive enough to arrive.

Arveth reached through the stable slats and touched the fading sigil on the wagon track where light had fallen. A thread of white came away on his finger, fine as spider silk.

"Can you follow it?" Mara asked.

"Not directly. But I can recognize its family."

"Meaning?"

"Meaning we need someone who understands locks made by people who think beauty excuses trespass."

Kesh brightened. "I know an engineer who owes rent."

Mara looked toward the road where Joryn had vanished.

"Tavi."

"Tavi," Kesh agreed. "Excellent at locks. Terrible at rent. Occasionally the same skill."

The next road was no longer a straight chase. It was worse. It had become a rescue that required knowledge, allies, and patience sharp enough not to become surrender.

Mara looked at the cinder cage. The shard inside had gone dim, as if exhausted by restraint. She knew the feeling. Every part of her wanted to break something large enough that the world would have to stop and return her brother. Instead, she had a white thread from an enemy's spell, a dead scholar's ledger, a troll's vow, a goblin's road debt, and the memory of Joryn shaking his head.

It was not enough.

It was also more than she had possessed yesterday.

Niv wiped his nose on his sleeve and tried to pretend he had not been crying when Joryn passed. "Your brother is rude to kidnappers."

Mara laughed once. It hurt. "He has practice being rude to authority."

"Good," Niv said. "Means he is probably annoying them."

"That is his gift."

Caldus glanced toward the north road, then toward the hidden culvert. "They will expect you to follow the wagon."

"So we do not?"

"We follow the lock."

Arveth lifted the white thread. In the gray light it seemed almost harmless, a bit of pale silk caught between dead fingers. Then it twisted toward the cinder cage like a compass needle finding a star.

"Locks have makers," he said. "Makers have habits. Habits have doors."

Kesh sighed. "And doors have Tavi."

Brakka rolled one shoulder, settling her maul. "Then we return to market."

Mara took one last look north. She did not pray. Prayer felt too much like asking permission from someone who might say later. She made a promise instead, quiet enough that only the road, the dead, and perhaps the buried hearts below the world could hear it.

"Hold on," she said to Joryn, wherever the wagon carried him. "I am learning how."

The road gave no answer, but for once Mara did not mistake silence for refusal. Sometimes silence was only room to begin, and continue onward.

Mara followed with the ledger against her chest, her own name burning in memory like a brand she refused to let anyone else hold.""",
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
        'current_form: "full-length draft zero with Book One chapters 1-13 revised in pass 01; continuing literary revision needed"',
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
    print(f"Book One chapters 9-13 revised. Word count: {total}")


if __name__ == "__main__":
    main()
