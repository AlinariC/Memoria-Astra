#!/usr/bin/env python3
"""Revision pass 01k for Book Three chapters 17-20.

Replaces the closing War of Every Road scaffold with bespoke chapters for
the light-and-shadow alliance, Arveth's counter-choir, the dragon forge,
and the Choir's mercy becoming a real temptation for Mara.
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
    17: r"""## Chapter 17: Light and Shadow Line

The light elves arrived with white arrows and too many apologies.

The dark elves arrived with black blades and none.

They met on the Glass Reed Line, where an old battlefield had grown into a marsh of translucent stalks taller than riders. Each reed held a memory of fire. When wind moved through them, the marsh chimed with tiny voices reciting last orders from wars that both elven courts had edited into legends flattering to themselves. On the western bank, Lumenorath healers raised pale canvas shelters under trees whose white roots still grew unevenly after Saelith's correction. On the eastern bank, Khar Veyl scouts marked shadow trenches with violet lamps hooded in wet silk.

Between them ran the road the refugees needed.

Between them also ran six centuries of murder, doctrine, secrecy, and songs designed to make the other side sound born wrong.

Mara stood in the mud while rain softened the maps and watched survival fail to simplify anything.

"My riders will not stand under shadow cover," Auralian said.

Maelin, wearing Khar Veyl black without the comfort of certainty, looked toward the marsh. "Then the Choir archers will see them and make them beautiful corpses."

"Your shadow screens have hidden massacres."

"Your hymns have blessed them."

Saelith closed her eyes.

Ilyr did not. He watched Maelin, Auralian, the lines of frightened elves, and the reeds beyond where black Choir pennants shifted like holes in the rain. "Both statements are evidence," he said. "Neither is a plan."

That earned him hatred from everyone, which meant he had probably helped.

The Choir attacked before the argument finished maturing.

It did not charge. It sang old victories.

From the glass reeds came Lumenorath's anthem of the Second Radiance, but slower, gentler, stripped of drums and given a lullaby's mercy. Light-elf archers lowered their bows as if hearing home after exile. Then Khar Veyl's mourning cadence rose beneath it, the song sung for sealed dead whose names could not be public. Dark-elf scouts flinched, and several stepped backward into open ground.

The Choir understood history. Not accurately. Usefully.

White arrows flew too early. Black blades answered the wrong shadows. A dead rider in Choir gray walked into the marsh holding a child carved from cinder-glass and said, "No more old hatred. Lay down memory. Rest."

For one heartbeat, Mara wanted to let the marsh go silent.

Then a light-elf arrow struck a Khar Veyl scout through the shoulder.

The line broke.

Caldus shouted for shields. Kesh's route chimes rang warning. Brakka dragged a supply wagon sideways to make cover. Tavi, having been ordered not to improve any dangerous devices during active diplomacy, improved three. Mara reached for the cinder-grit under the reed roots and felt the old battlefield answer with eagerness.

Command us, it seemed to say. One note. One silence. One line.

Saelith stepped into the marsh before Mara could answer.

Ilyr cursed and followed.

The reeds chimed around them. White memory and black memory sliced through rain. A Choir arrow skimmed Saelith's cheek. Ilyr cut it from the air and took the next through his thigh. Saelith caught him before he fell, and the sight did what law could not. Light-elf archers saw Dawnmere hold Noct-Vey blood in both hands. Dark-elf scouts saw an exile lean his blade across her shoulders and throw shadow over her without asking payment.

The old songs faltered.

"Do not make us pure," Saelith shouted into the marsh.

Ilyr, teeth gritted against pain, lifted his blade. "Make us accurate."

They moved together then, not gracefully. That mattered. Saelith's rough hymn gave the light archers a rhythm that did not command. Ilyr's shadow marks showed where the dark scouts could strike without vanishing from witness. Maelin took the left trench. Auralian, pale with terror and pride, took the right shelter line. White arrows flew through black screens. Black blades moved under white flare. Each side saw the other's work save someone it had been taught to fear.

Mara did not command the cinders.

She witnessed the line and fed it names.

The marsh answered not with silence but with every edited casualty both courts had buried: light soldiers killed by dark orders, dark prisoners killed under white law, human nurses, goblin guides, troll bridge crews, gnome medics, dead who had never been allowed into either anthem. Their voices rose through the glass reeds and made the Choir's clean mercy stumble.

The cinder-glass child in the dead rider's arms cracked.

Inside was no child. Only a command seed wrapped in lullaby.

Tavi's device hit it first, a brass dart carrying vinegar, salt, and moral outrage. Brakka's maul finished the argument. The dead rider collapsed in the reeds, whispering a name too old to belong to either court alone.

By dusk, the road remained open.

Not safe. Open.

The light and dark elves counted their dead in separate columns at first. Sava saw this, walked into the rain, and drew a third column titled DIED WHILE BEING SAVED BY THE OTHER SIDE. No one liked it. No one crossed it out.

Saelith sat beside Ilyr while a Khar Veyl medic stitched his thigh and a Lumenorath healer held the lamp.

"They will turn us into a mural," she said.

"Almost certainly."

"I hate murals."

"They flatten the nose."

She laughed, then cried once, angrily.

Mara stood at the edge of the Glass Reed Line and listened as the marsh learned a new sound: not harmony, not forgiveness, not unity. Coordination. Awkward, resentful, beautiful coordination.

History resisted cooperation.

The road carried it anyway.""",
    18: r"""## Chapter 18: The Counter-Choir

The dead gathered at the old milestone road with bone lanterns beating like hearts.

They came from everywhere the War of Every Road had touched. Fever cavalry under corrected orders. River-dead with stitches cut from their mouths. Orrowen citizens carrying public ledgers. Fallen soldiers from Snow Cedar Pass. Kitchen servants from Lumenorath's buried law. Dark-elf prisoners whose names had survived in forbidden margins. Miners from Kell Ashgate, still coughing ash though they had no lungs. Some walked alone. Some were led by living family. Some came because they feared the Choir and some because they feared freedom more.

That last truth frightened Mara most.

The milestone road ran north toward the Dead Capital, though no map admitted the capital still had roads. Its stones were black with old rain and set with little hollows where travelers once left lamp oil for the lost. Now each hollow held a bone lantern, and each lantern pulsed with a dead person's chosen name. The light was not warm. It was present.

Arveth's mark appeared on a witness panel nailed to a wagon door.

Not a sentence. A door-shaped stroke of ink.

Then: Excessively dramatic assembly. Promising.

Sava made a sound between a sob and a reprimand. "Citizen Arveth, this is no time for style notes."

Style is what separates civic ritual from weather.

"You are fading again."

Correct.

The ink held.

Mara touched the panel's edge. "You said you needed to testify at the Dead Capital."

I said many brave things while incompletely embodied.

"Arveth."

The mark darkened. Yes. I am here.

The dead turned toward the panel.

The Choir's mercy had been moving ahead of them for days, entering camps not as conquest but as relief. It offered the dead an end to confusion, old orders, hunger for warmth, grief without bodies. It offered the living sleep, quiet children, streets without screams, marriages unbroken by corpses at the door. It did not always lie. Sometimes, Mara hated it most for that.

A dead woman in a blue apron stepped forward. "I want rest."

No one answered fast enough.

She looked around, ashamed and angry. "I was drowned in tax flood. I spoke my name. I accused the men who sold my arms. I crossed the bridge. I am tired. If Vorrakai offers quiet, why must I keep choosing because the living finally feel guilty?"

Nera Bell.

Mara knew her voice from Brindle Ford. She felt the whole gathering lean toward her question.

Arveth's ink thinned.

Then the panel wrote: You must not.

The dead murmured.

The words continued, slower. Rest chosen is not stillness imposed. The difference is the whole law.

Another dead man spoke. "And if I do not trust myself to choose? I followed a plague order for two centuries."

Oren Vall, fever cavalry captain.

Caldus answered him. "Then choose with witnesses who may contradict you."

"And if they are wrong?"

"Then they must answer too."

That was not comfort. It was something sturdier and less kind.

The Choir found them at moonrise.

Its singers came along the milestone road in gray cloaks, carrying no weapons. Behind them walked dead who had accepted stillness: faces peaceful, steps perfect, names unlit. At their center moved a woman Mara recognized with a pain that belonged to Saelith more than herself.

One of Serathiel's dead oathkeepers.

Her old white armor had gone soft and colorless. She smiled at the bone lanterns.

"Lay down the burden," she sang. "You have been named. You have suffered. Enough."

Bone lights flickered.

Several dead stepped forward.

Mara reached for cinder heat and stopped. Commanding the dead to reject stillness would be another stillness wearing her voice.

Arveth's mark burned.

Ask them to answer each other, he wrote.

So Mara did.

"If you choose rest," she called, "name who witnesses the choice. If you choose to stay, name why. If you do not know, say that too. No one enters silence because a song makes the question smaller."

The Choir's hymn swelled.

Nera Bell lifted her lantern. "I want rest, witnessed by the river that killed me, by Saelith who cut my stitches, by Brakka's bridge, and by myself. Not tonight. After the Dead Capital knows my name."

Her lantern steadied.

Oren Vall raised his. "I stay until no fever order uses my hands."

One by one, the dead answered. Some chose eventual rest. Some chose testimony. Some chose anger. Some chose uncertainty and were applauded by Sava as if uncertainty were a properly filed document. The bone lanterns beat out of rhythm, each pulse its own refusal.

That was the counter-choir.

Not a song against a song.

A thousand different answers refusing to become one easy mercy.

The Choir singers faltered. The still dead behind them did not wake, but some lifted their heads as if hearing rain after a long sealed room.

Arveth appeared then in the lantern light, not whole, not stable, a figure made from ink, witness panels, bridge chips, hymn scars, road debts, engine marks, and every place he had been properly heard. He looked at the Choir emissary with weary delight.

"I object," he said.

The milestone road flashed blue.

True.

The Choir retreated before dawn. It did not break. It never broke that kindly. It withdrew with many still dead behind it and left the counter-choir trembling in its own freedom.

Arveth's figure turned to Mara.

"The Dead Capital will not be won by volume," he said. "Vorrakai is not afraid of noise."

"What is he afraid of?"

"Consent that survives grief."

Then he faded back into the panel.

Sava stood very still, pen hovering over the page.

Mara looked north toward the road that no map admitted, where bone lanterns now marked the way to the city that had taught death how to organize itself.

Freedom was frightening even to the freed.

That did not make stillness merciful.""",
    19: r"""## Chapter 19: The Dragon Forge

The dragon forge was not in the Storm Isles.

It was under Brassroot.

Tavi took this personally.

"You cannot put a dragon forge under my people's ancestral engineering district and not label the access corridor," she said, crawling through a root-cable tunnel with a lantern between her teeth. "That is how civilizations lose manuals."

The tunnel descended below the emergency forge, below the liability-stamped release engines, below the dead tree's first root ring, into red heat and old stone. Eshkarun's bronze scale had begun burning against Mara's chest at dawn, pointing not north toward the Dead Capital but down. The dragons had given one storm path. They had not mentioned a buried forge under gnome territory, which told Mara either dragons forgot what mortals needed to know or enjoyed being dramatic. Likely both.

Kesh wriggled behind her. "Perhaps they assumed we would smell the ancient dragon furnace."

"It smells like every other catastrophic basement," Tavi snapped.

Brakka, who had to move sideways, grunted. "Basements should answer for themselves."

The tunnel opened into a chamber shaped like a rib cage.

Mara stopped.

A dragon had died there.

Not recently. Not cleanly. The bones arched through the stone, each rib plated with brass grafts, gnome clamps, white roots, dark-elf seals, human ash mortar, and goblin road tokens melted flat as washers. At the center of the chamber burned a heart-forge: not the dragon's heart, Mara sensed, but a furnace built where the heart had been removed. It pulsed with cinder pressure drawn from the release engines above.

Tavi's face went gray.

"No," she said.

The forge answered by opening every valve at once.

Heat slammed into them. Saelith threw a rough hymn shield over the front line. Ilyr and Maelin dragged shadow across the floor before the heat could find their boots. Caldus pushed Mara behind his broken shield though everyone knew shields were mostly suggestions at this temperature. Brakka drove Elder Morn's bridge nail into the stone, and the chamber steadied around it.

On the far side of the forge stood three gnome guild masters, two human officers, and a Choir emissary with a peaceful face.

Vellit Ock was among them.

Tavi stared at him. "You signed the code."

Vellit's eyes were fever-bright. "The code slows surface engines. This is older than guild law."

"That is the worst sentence engineers say before prosecution."

The Choir emissary smiled. "No prosecution is needed. No guilt. No liability. The forge can release every road at once if joined to stillness. No more explosions. No more old orders. No more frightened makers."

Mara felt the offer move through the chamber. It was not aimed at her first.

It was aimed at Tavi.

The heart-forge showed possibilities: release engines humming cleanly across Vael Taryn, no hidden command channels because command would no longer be hidden, no panicked witnesses failing to choose, no makers signing harm because harm had been made impossible by stilling the variables. A perfect system. A final diagram.

Tavi looked as if someone had struck her.

"You do not get to call people variables," she whispered.

The Choir emissary's smile saddened. "Your own law proves you know makers cannot bear the weight."

"My law proves we already bear it."

Vellit lifted a control rod. "With this forge, we can end cinder pressure before it tears cities apart."

Tavi looked at the dragon bones. "Whose forge was it?"

No one answered.

Mara knew before the cinders spoke.

Not Othrava. Another dragon, smaller, nameless in the records around her because a forge worked better when the fuel had no name. A young fire-drake taken during the first covenant wars, kept beneath the future Brassroot district while mortals and dragons learned to blame each other upward and outward. The gnomes had not started the crime alone. Humans had mortared it. Elves had sealed it. Dragons had abandoned the site after judgment failed. Goblins had carried parts. Trolls had reinforced the chamber. Everyone had a hand on the furnace and a story about necessity.

"Name her," Mara said.

The Choir emissary's eyes sharpened.

Vellit frowned. "What?"

"The dragon whose ribs you are using. Name her."

The forge roared.

Cinder fire crawled along the ribs. Old clamps glowed. Above them, the release engines began answering the buried heart-forge, their liability panels flashing red. Tavi seized the nearest panel and shouted for every engineer in the upper forge to open witness lines. Her voice carried through speaking tubes and root-cables.

"Maker named! Harm named! Dragon named if we can find her! No engine answers an unnamed furnace!"

Vellit pulled the rod.

The heart-forge reached for the road network.

Mara could have used Eshkarun's scale. One storm path. One impossible opening. She felt it burn through her coat. Instead, she held it out to the dragon bones.

"You remember storms," she said. "Do you remember her?"

The scale cracked.

Eshkarun's memory entered the forge: a small fire-drake diving through first thermals beside him, copper-red, laughing in sparks, named Veyrasha-of-Ember-Reed before war taught everyone shorter names for easier mourning. The heart-forge screamed when the name touched it.

"Veyrasha," Mara said.

Tavi repeated it into the witness tube.

Above, engineers, refugees, dead witnesses, and road clerks repeated it through every liability panel. Veyrasha. Veyrasha. Veyrasha. Not fuel. Not ancient infrastructure. Person.

The heart-forge cracked down the center.

The Choir emissary lunged for Mara. Caldus met him with the broken shield. Saelith's rough hymn cut the stillness from his smile. Ilyr and Maelin pinned his shadow to the rib wall. Brakka struck the control dais and turned gnome brass into expensive regret. Kesh tackled Vellit before the guild master could pull the secondary rod, and both rolled under a shower of sparks.

Tavi climbed the heart-forge.

"Bad idea," Mara shouted.

"Current professional theme!"

Tavi jammed both burned hands into the cracked core and opened every release valve outward, not into the road network, not into command, but into the chamber's witness ring. Fire became memory. Memory became heat. Heat became a roar of wings that had not moved for centuries.

The dragon bones lifted.

Not alive. Not resurrected. Released enough to stop being machinery.

Veyrasha's skull turned toward Mara with empty sockets full of ember light.

Thank you, said the heat.

Then the forge went out.

The chamber fell dark except for liability panels glowing blue one by one.

True.

True.

True.

When they climbed back into Brassroot, every release engine in the network had recorded the buried forge, its makers, its users, its harm, and Veyrasha's name. The dragons would learn of it. The guilds would not bury it again. Vellit, soot-covered and silent, signed his confession under Sava's gaze with Kesh standing close enough to make running theoretical.

Tavi sat on a workbench, hands shaking.

"My people built over a dragon grave," she said.

Mara sat beside her. "Many people did."

"That is not better."

"No."

Below, the dead forge cooled.

Above, far to the north, the Choir's black fires dimmed for one hour.

Only one.

It was enough for the roads to move.""",
    20: r"""## Chapter 20: The Choir's Mercy

The captured town looked healed.

That was the worst of it.

Mara had expected black banners, chained dead, frightened citizens, cinder fires in the streets. Instead, the town of Harth Bend shone under morning rain. Windows were mended. Gutters ran clear. Bread cooled on sill boards. The market square had been swept. Children sat in a circle around a woman telling a story in a soft voice. The dead stood beside the living without hunger, confusion, or grief. No one screamed when Mara's company entered through the west gate.

No one chose to look at them either.

Their faces turned in unison, peaceful as pond water.

Kesh's hand went to his knife. "I hate tidy."

Tavi whispered, "The pressure readings are stable."

"That does not make me hate it less."

Saelith's hymn mark had gone cold. Ilyr's shadow clung too close to his boots. Caldus walked with his injured arm bound tight, eyes moving over rooftops, alleys, windows, every ordinary place danger liked to wear. Brakka touched a bridge charm at her belt and murmured something too low for translation.

At the fountain in the square waited the Choir emissary.

Not the one from the dragon forge. This one had been human once, an old woman with silver hair braided neatly down her back and a baker's burn scar on one wrist. She wore no armor. Her gray cloak was clean. Her smile held no mockery.

"Mara Venn," she said. "You are tired."

Mara almost denied it.

The town made denial feel childish.

She was tired. Tired of mud, meetings, triage, bodies under snow, names on ledgers, people asking her to carry what they feared, people dying because she refused faster levers, people nearly enslaved because faster levers worked. Tired of power and restraint both. Tired down to the part of her that had once been a girl in Kell Ashgate measuring life by shift bells and whether Joryn had saved enough bread.

"Who are you?" Mara asked.

"Edda Mar. I baked for this town for forty years. I buried two children, one husband, one sister, and every apprentice the fever took. I joined the Choir three nights ago."

"Willingly?"

"Gratefully."

Around the square, Harth Bend continued being peaceful. A risen man folded laundry beside his living daughter. A child with a scarred cheek shared a pear with a dead dog whose tail wagged with perfect contentment. Two former enemies sat on a bench, hands folded, eyes empty of rage.

Edda saw Mara looking. "No one here suffers."

"No one here chooses."

"Choice brought us to the suffering."

The sentence should have sounded monstrous. It sounded like a woman who had washed too many fever sheets.

Mara's certainty cracked, not because Edda lied, but because she did not.

Edda led them through town.

The company moved carefully. No one attacked. No one begged. In the schoolhouse, children copied letters in perfect silence. In the infirmary, the dying slept without pain while dead nurses changed bandages with gentle hands. In the old debt office, ledgers had been burned and the clerks sat smiling among ash. At the cemetery, graves stood open, but the risen dead sat on their own headstones and watched rain bead on flowers.

"We do not erase names," Edda said. "We end the wound that makes names knives."

Arveth's mark stayed cold in Mara's satchel.

That frightened her more than any attack.

At the bakery, Edda broke a loaf and handed Mara half. It smelled like Kell Ashgate bread on rare good mornings, dense and warm, with a cracked crust and salt tucked into the dough because poor people needed flavor where they could get it.

Mara took it before she meant to.

She remembered Joryn stealing heel ends from cooling racks, remembered her mother laughing once before ash-fever turned laughter into coughing, remembered the first time she understood that hunger made people easier to command. She had spent three books of her life refusing to be used. Here was a town where no one was useful because no one wanted anything.

It looked like rest.

Vorrakai spoke beneath the silence.

Not loudly. Not even in words at first. A pressure under the bread's warmth, a grief old enough to be patient with her anger.

You count the bodies because you still believe counting redeems the road.

Mara closed her eyes.

Edda said, "He will speak with you if you let him."

Caldus stepped forward. "No."

Mara held up a hand.

Not command. Request.

He stopped because he trusted her and hated this.

Vorrakai's voice formed inside the quiet town.

I was judge before I was monster. I watched dragons burn cities for cages built by frightened children. I watched mortals bind living hearts because judgment from the sky made them small. I watched love become grief, grief become law, law become war, war become memory, memory become weapon. You have seen enough now to know I do not offer emptiness. I offer an end to the wheel.

Mara opened her eyes.

Across the bakery, a dead boy kneaded dough beside his living grandmother. His hands moved perfectly. He smiled when she smiled. Neither had to remember he had drowned in the millrace last spring. Neither had to decide what love meant after death.

Edda's voice softened. "Would you make them hurt again to prove they are free?"

There was the knife.

Mara had answered kings, dragons, guilds, courts, and armies. This question found the girl under all of it: the one who had wanted Joryn safe more than she had wanted any grand truth, the one who would have traded philosophy for one winter without coughing in the walls.

Saelith came beside her. "Mara."

Her voice shook. The town tempted her too. A law without cruelty. A mercy that did not require her to break hymns open and bleed for every correction.

Ilyr stared at the burned debt office as if imagining Khar Veyl without sealed guilt. Tavi looked at machines that could no longer be misused because no one desired misuse. Kesh watched the quiet roads with the face of a man who knew what bargains cost and saw, for one terrible moment, a road with no debt. Caldus looked at children who would never be ordered to hold a bridge. Brakka looked at bridges no one would need to cross in terror.

The whole company understood.

That was Vorrakai's mercy.

Not villainy.

Conclusion.

Mara set the bread down.

"Wake one person," she said.

Edda's smile dimmed. "Why?"

"If it is mercy, let one person choose it after waking."

"Pain will return."

"Yes."

"Cruel girl."

The words struck. Mara did not dodge them.

"Maybe," she said. "Wake one."

Edda looked toward the square. For the first time, uncertainty crossed her face. The Choir did not like uncertainty. The town's silence tightened. Rain paused on window glass.

Then the dead boy in the bakery turned his head.

Not fully awake. Not free. A flicker.

"Gran?" he whispered.

The living grandmother dropped the dough.

Pain entered her face like a storm breaking a sealed room. Love followed so close behind that Mara could not tell which was which. She reached for the boy, stopped, asked without words, and he flung himself into her arms. Both began to sob.

The town screamed.

Not from mouths. From the spell of peace tearing around one chosen grief.

Edda staggered. Caldus drew his sword. Choir stillness poured through the streets, trying to smooth the wound. Saelith sang the rough interval, but softly, so the awakened pain had somewhere to stand. Ilyr and Maelin opened shadow paths for people who began to wake frightened. Tavi smashed a stillness node hidden inside the bakery oven. Kesh rang route chimes from the square, calling names, not exits yet. Brakka stood at the fountain and roared, "No one takes refusal as betrayal!"

Mara pressed both burned hands to the wet stones.

Not command.

Witness.

Harth Bend woke unevenly. Some screamed. Some begged to return to quiet. Some struck at the company. Some clung to the dead. Some chose, when fully awake, to enter rest under witness, and the counter-choir's distant lanterns answered. The town did not become healed. It became alive again, which was messier and less defensible.

Edda Mar knelt in the street, weeping.

"You brought back the hurt," she said.

Mara knelt opposite her. "Yes."

"How do you bear that?"

Mara thought of every road behind her, every name entered, every body counted, every choice that had failed to save enough. She thought of the beautiful lever the dragons had offered and the quiet bread Vorrakai had offered. She thought of Joryn, of Kell Ashgate, of the dead boy sobbing into his grandmother's apron.

"Badly," Mara said. "With witnesses."

The answer did not comfort Edda.

It did not comfort Mara either.

North of Harth Bend, the road to the Dead Capital opened.

Not on any map. Not with light. The rain simply began falling in a line where no road had been, and every drop struck invisible stone.

Vorrakai's voice faded beneath it.

Then come count the first wound, little witness.

Mara rose, bread cooling behind her, and followed the rain road toward Vael.""",
}


EXTRA_DEEPENING: dict[int, str] = {
    17: r"""The line did not hold because elves became better people in a single rainstorm.

It held because the first hour after the battle made cowardice visible.

A light-elf captain refused to let dark-elf scouts carry his wounded through shadow. A Khar Veyl surgeon refused to cross the white-root shelter threshold until Maelin physically pushed him and called it diplomatic pressure. Auralian caught two young oathkeepers scraping the third casualty column off Sava's board because it embarrassed their house. Ilyr found a dark-elf scout hiding a Lumenorath arrow wound so no one would say she had been saved by white hands.

Mara wanted to order them all into one tent and make them stay there until shame did something useful.

Instead, she carried water.

It was not symbolic. People needed water. Carrying it put her where speeches would have put distance: between cots, beside muttered slurs, under the eyes of wounded soldiers who hated needing the enemy's bandages. She heard one light-elf boy ask whether shadow medicine would stain his soul. The dark-elf medic cleaning his wound said, very calmly, "Only if your soul is stored in your calf."

The boy laughed before remembering not to.

That was how the alliance began to become harder than a mural. Not in banners. In jokes no doctrine had prepared for. In Maelin holding a lamp for Saelith while Saelith pulled black arrow splinters from Ilyr's thigh. In Auralian ordering his own house to carve the names of dark-elf dead into white root markers because "temporary markers" had become too familiar an excuse. In Ilyr admitting, in public and with visible suffering, that a Lumenorath healer's knots were superior for arterial wounds.

"I would like that entered without adjectives," he told Sava.

Sava did not look up. "Denied."

Near midnight, the Glass Reed Line chimed again.

Everyone reached for weapons.

But the reeds were not singing old victories. They repeated the new casualty column, name by name, each voice accompanied by an arrow note and a shadow note. The marsh had learned the alliance in the ugliest honest form available: who died being saved by whom.

Saelith stood beside Mara in the rain, exhausted past posture.

"This will not end the hatred," she said.

"No."

"It may give the next person something to point at when hatred claims it has no alternative."

Mara watched Ilyr accept broth from a light-elf medic and pretend not to need help holding the cup.

"Sometimes a road begins as evidence," she said.

The glass reeds chimed until dawn.""",
    18: r"""The counter-choir needed rules by sunrise because freedom without shape frightened the dead almost as much as the Choir did.

That was Sava's sentence, and everyone hated how useful it was.

They built the rules on wagon boards around the milestone road. Rest by consent, witnessed and challengeable. Staying by consent, witnessed and challengeable. Uncertainty protected. No dead person required to perform testimony for living comfort. No living family permitted to demand persistence from the dead as proof of love. No one accepted into final rest while under active command, sedative hymn, cinder compulsion, debt threat, family coercion, or heroic speech delivered by someone who would not have to endure the result.

"That last clause feels personal," Kesh said.

"All good law begins by insulting someone specific," Sava replied.

The dead argued over every line. That saved them from becoming an army.

Oren Vall wanted military order because order had been the only thing keeping his mind from shredding during two centuries of wrong marching. Nera Bell wanted river law because water remembered debts differently. The Lumenorath kitchen dead wanted beauty admitted as evidence and Saelith insisted beauty could enter only if ugliness sat beside it. The miners from Kell Ashgate wanted labor tallies read aloud so no one called them brave when they had been hungry.

Arveth appeared in pieces as they argued: a line of ink on a panel, a voice in a bone lantern, a dry comment from a bridge chip, once a hand made entirely of footnotes pointing at a badly phrased clause.

Mara found him after dawn in the shadow of an old milestone.

"Are we spending you?" she asked.

The ink on the stone took time.

Yes.

Her throat tightened.

Then: With consent. Do not ruin a perfectly difficult distinction.

"You could choose rest."

I will. After I have made myself maximally inconvenient to tyranny.

She laughed because he wanted her to, and because not laughing would have made grief too pleased with itself.

At noon the counter-choir practiced.

It sounded terrible.

No bard would have called it music. Bone lanterns beat at different tempos. Dead cavalry recited corrected orders. Drowned workers spoke river names over kitchen testimony. Miners counted wages. Orrowen clerks objected. Lumenorath servants sang one ugly note each. The whole thing lurched, contradicted itself, stopped, restarted, and refused every attempt by Auralian to make it more beautiful.

The Choir's distant stillness pressed against the milestone road.

The counter-choir answered badly.

It answered anyway.

Mara understood then why Arveth had chosen not one anchor but many. A single perfect voice could be captured, revered, silenced, or turned into law. This stumbling assembly could be harmed. It could be infiltrated. It could waste hours on clauses while war moved. But no single hand could close around all of it at once.

Freedom did not sound like triumph.

It sounded like the dead learning procedure while the world burned.

That was less inspiring than a song and more likely to survive one.""",
    19: r"""The dragons answered Veyrasha's name before the soot settled.

They did not come in bodies. Brassroot's sky was too low, its forge vents too crowded, its railbeds too full of refugees and engines stamped with maker liability. Instead, rain over the dead tree turned to steam and the steam shaped seven shadows on the clouds. Eshkarun's profile was easiest to know: bronze horn, torn wing, scarred muzzle held too still.

The guilds came out to stare. So did the refugees. So did the dead witnesses whose lanterns had pulsed blue when Veyrasha's name entered the panels.

Tavi stood with both hands bandaged and refused to bow.

Mara liked her more for that.

Eshkarun's storm-shadow looked down at the forge gates.

Veyrasha-of-Ember-Reed was entered lost in the third covenant war, he said. Not buried under Brassroot. Lost.

"Convenient word," Tavi said.

The steam shadow darkened. Yes.

Mara heard the cost of that yes ripple through every dragon-facing memory in the valley. Dragons had counted mortal cages and missed dragon abandonment. Mortals had counted dragon judgment and missed the bodies hidden under their own workshops. The old covenant had not failed in one direction. It had failed everywhere powerful grief found a tool.

Vellit Ock was brought from the lower cells to hear the cloud witness. He looked smaller without his rulers braided into his beard. Sava made him stand beside the liability panels and read aloud the chain of custody for the buried forge. His voice cracked on the names of gnome masters long dead and human officers honored in Harrowmere. It nearly failed when he reached the signatures of early guild founders.

"Continue," Tavi said.

He did.

Each name entered public record. Each craft lineage lost a little innocence it had never earned.

Then Pinna Vey, the young engineer, raised her wrench. "What do we build over the chamber now?"

Tavi looked exhausted enough to become honest without jokes. "Nothing over. Around. Access stays open. Records stay visible. Heat readings continue. Veyrasha's name goes on every engine line descended from that forge."

"That will implicate half the guild."

"At least."

Pinna nodded slowly. "Good."

The dragon shadows watched mortals choose public shame without being forced by dragon fire. Perhaps that was why Eshkarun spoke again.

One storm debt enters repair.

Mara felt the bronze scale, now cracked and dull in her pocket. "Repair is not forgiveness."

No, said the dragon. But it moves.

For one hour, as the Choir fires dimmed in the north, gnomes and refugees and dead witnesses opened the sealed lower doors and turned the dragon forge from hidden engine into public wound. They did not make it beautiful. Tavi forbade that with such force that even Auralian, who had just arrived with the light-and-shadow wounded, decided not to suggest memorial symmetry.

They built a stair.

Plain. Wide. Named at every landing.

So no one could again say they did not know what held the floor.""",
    20: r"""Harth Bend did not recover after waking.

That was important.

It rioted, wept, prayed, cursed Mara, thanked her, begged her to leave, begged her to stay, and demanded that someone explain how grief was supposed to fit back into cupboards after three days of perfect quiet. The dead boy from the bakery, whose name was Lio, chose to remain until evening and then chose witnessed rest with his grandmother's hands around his. His grandmother screamed when he passed. Then she slapped Mara. Then she hugged her. Then she asked whether hating her made the gratitude invalid.

"No," Mara said, cheek stinging. "It may be part of it."

Edda Mar did not flee with the Choir.

She helped wake the town instead.

Not because Mara convinced her with a speech. Because Lio's grandmother asked her to hold the bowl of wash water while they prepared his body. Edda stood in the bakery kitchen with flour on her sleeves and watched pain return to a room she had thought mercy had cleaned. When the grandmother began telling a story about Lio stealing raisins, Edda flinched as if the memory were a thrown stone.

"Stillness kept that from hurting," Edda said.

"It also kept her from telling it," Mara answered.

Edda looked at the grandmother's face: wrecked, alive, furious with love.

"I do not know if I can leave the Choir," she whispered.

"Then say that where witnesses can hear you."

So she did.

By nightfall, Harth Bend had become the ugliest victory of the war. Some citizens chose the counter-choir's road. Some chose witnessed rest. Some remained loyal to Vorrakai because peace, even stolen, had tasted real. Caldus wanted to call that dangerous. Brakka did call it dangerous. Arveth's distant mark, flickering on a bakery peel Tavi had converted into a witness panel, wrote: Danger is not invalidity. Annoying but foundational.

Mara slept for twenty minutes under the bakery table and woke with her hand around the cooled half-loaf.

Saelith sat beside her.

"You scared me," Saelith said.

"In the town?"

"Before. When you took the bread."

Mara stared at the loaf. "I wanted it to be true."

"I know."

The honesty hurt more than reassurance would have.

"Part of me still does," Mara said.

Saelith leaned her head back against the table leg. "Part of me wanted the healer school quiet. No more houses arguing. No more old law finding new mouths. No more choosing against beauty every time beauty behaves badly."

"What stopped you?"

"The boy asked for his grandmother."

Mara closed her eyes.

That was the answer Vorrakai could not bear. Not that suffering was good. It was not. Not that choice always redeemed pain. It did not. Only this: sometimes pain carried the shape of love returning to itself, and no judge, dragon, saint, crown, or exhausted hero had the right to sand that shape smooth for everyone.

Outside, rain kept striking the invisible road north.

Each drop revealed a stone for an instant, then another, a road made visible only by weather hitting it. Harth Bend's awakened citizens stood at windows and watched. Some spat toward it. Some prayed. Some packed.

Mara finished the stale bread because hunger was not philosophy, and because Joryn had taught her never to waste what someone might have needed.

Then she stepped outside.

The road to the Dead Capital waited in rain, and beyond it the districts of failed endings stirred: conquest, sacrifice, obedience, vengeance, stillness. She did not know their names yet, not all of them, but she felt them like rooms under her skin.

Caldus joined her with his cracked shield strapped badly over one shoulder.

"We are past the war roads," he said.

"No," Mara said, looking back at Harth Bend. "We are taking them with us."

Behind her came Saelith, Ilyr, Tavi, Kesh, Brakka, Maelin, Sava, living witnesses, dead witnesses, and the first trembling voices of the counter-choir.

Mara stepped onto the rain road.

This time, no one asked whether it would hold.

They had learned better questions.""",
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
        if chapter_no in EXTRA_DEEPENING:
            replacement += "\n\n" + EXTRA_DEEPENING[chapter_no].strip()
        text = text[:start] + replacement + "\n\n" + text[end:].lstrip()
        matches = list(pattern.finditer(text))
        by_no = {int(m.group(1)): m for m in matches}
        back_matter = re.search(r"(?m)^## Back Matter\b", text)
    return text


def normalize_part_headings(text: str) -> str:
    text = re.sub(r"\n*# Part IV: The Dead Capital\n+", "\n\n", text)
    text = re.sub(
        r"(?m)^## Chapter 21:",
        "# Part IV: The Dead Capital\n\n## Chapter 21:",
        text,
        count=1,
    )
    return text


def update_metadata(word_total: int) -> None:
    meta = METADATA.read_text(encoding="utf-8")
    meta = re.sub(r"produced_word_count: \d+", f"produced_word_count: {word_total}", meta)
    meta = re.sub(r"at_300_words_per_page: \d+", f"at_300_words_per_page: {round(word_total / 300)}", meta)
    meta = re.sub(r"at_275_words_per_page: \d+", f"at_275_words_per_page: {round(word_total / 275)}", meta)
    meta = re.sub(r"at_250_words_per_page: \d+", f"at_250_words_per_page: {round(word_total / 250)}", meta)
    meta = re.sub(
        r'current_form: ".*"',
        'current_form: "full-length draft zero with Book Three chapters 1-20 revised in pass 01"',
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
    revised = normalize_part_headings(replace_chapters(text))
    MANUSCRIPT.write_text(revised, encoding="utf-8")
    total = word_count(revised)
    update_metadata(total)
    update_summary(total)
    print(f"Book Three chapters 17-20 revised. Word count: {total}")


if __name__ == "__main__":
    main()
