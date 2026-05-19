#!/usr/bin/env python3
"""Revision pass 01c for Book Two chapters 13-15.

Replaces the opening Khar Veyl scaffold with bespoke under-realm scenes:
the downward gate, the Banquet of True Shadows, and Ilyr's half-truth reckoning.
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
    13: r"""## Chapter 13: The Downward Gate

# Part III: Khar Veyl

Khar Veyl did not rise to meet them.

It waited below.

The first stair descended from the sealed gate in a spiral cut through black basalt veined with blue fire. The light did not flicker like flame. It flowed inside the stone in patient lines, illuminating old chisel marks, wet mineral seams, and script that moved away when Mara looked too directly at it. Air climbed from the depths cool and metallic, smelling of ink, mushrooms, lamp oil, and deep water that had never learned the sky.

Behind them, Lumenorath's roots pressed against the closed gate.

Ahead, the under-road widened one step at a time.

No one spoke for the first hundred stairs.

Even Kesh respected the silence, which made the silence feel official.

Mara kept one hand on the wall. The stone remembered touch differently than white root. Lumenorath had tried to correct her posture, clean her story, arrange every grief toward beauty. Khar Veyl's stone did not correct. It recorded pressure. Every hand that had passed here had left some fraction of heat behind: exiles, judges, blade students, smugglers, children carrying water, prisoners going down, witnesses coming up, people who had spoken truth and people who had hidden behind the technical honesty of not speaking at all.

The cinder at her hip stayed quiet.

That worried her more than heat would have.

Ilyr walked ahead with his hood down and blood drying on his palm. In Lumenorath he had seemed sharp against the light, a dark line the realm wanted to edit out. Here he looked no more at ease. That surprised Mara until she understood: belonging did not mean safety. Sometimes it meant the people who knew exactly where to cut.

At the bottom of the stair stood the Downward Gate.

The gate was not the one they had crossed. That had been only the outer mouth. This was Khar Veyl's true threshold: three black arches set one behind another, each carved with thousands of names in scripts Mara could not read. Between the arches hung curtains of blue flame falling upward. On either side stood statues of Veyra figures holding knives against their own tongues.

Under the central arch waited seven dark elves in layered black and silver.

They did not look like villains from surface stories. No sneers. No theatrical cruelty. Their hair ranged from white to blue-black, their skin from deep brown to gray-violet, their eyes silver, amber, black, green. They wore scholar robes over blade harnesses. Each carried a book at one hip and a weapon at the other. Mara recognized the style of threat immediately: people who considered themselves too disciplined to be frightened by the damage they could do.

The central figure stepped forward.

"Ilyr Noct-Vey," she said. "Exile. Half-witness. Unfinished wound."

Ilyr bowed, not deeply. "Judge Vaura Noct-Vey."

Mara looked from one to the other.

The judge's face did not change. "He did not mention his mother?"

"No," Mara said.

"Good. Shame survives exile."

Ilyr's jaw tightened.

Kesh leaned toward Tavi. "Family reunions below are brisk."

Vaura's gaze moved to him. "Kavik road-debtor. Speak less until bargained for."

Kesh straightened. "I have been seen in my full legal beauty."

"You have been read."

"Worse."

The judge turned to Mara last.

"Mara Venn of Kell Ashgate," she said. "Cinder-singer. Refuser of sanctity. Human hazard named by light. Witness claimed by no court. You stand at the Downward Gate. Truth opens. Half-truth wounds. Lie returns."

"Returns where?" Mara asked.

The first blue flame curtain bent toward her.

"To the speaker," Vaura said.

Brakka made a low approving sound. "Good gate."

"Not good," Ilyr said. "Precise."

Vaura's mouth almost curved. "The Third Arch understands distinctions."

Caldus shifted his staff. "What is required?"

"One truth from each who passes. Not best truth. Not safest. A necessary one."

Mara's stomach sank.

Lumenorath had asked for a truth at the First Lyric Gate. She had gone through the ditch to refuse. There was no ditch here. Only black stone and upward flame. She wondered whether every civilization built gates that asked for pieces of the self because roads made people vulnerable and power enjoyed ceremony.

Saelith stepped forward first.

The blue flame brightened around her pale hair.

"I miss the certainty of obedience," she said.

The words landed hard. Not because they were surprising. Because they were not. The first flame parted.

No one comforted her. That was mercy in this place. They let the truth stand without dressing it.

Caldus went next. "Some part of me still wants rank to absolve me."

The second flame shivered open.

Tavi swallowed. "I can imagine the command engine too clearly."

The flame hissed. Opened.

Kesh rocked back on his heels. "I am afraid friendship is a debt I cannot run from."

The gate accepted it.

Brakka planted her maul. "I enjoy invalid vows breaking."

Vaura raised one eyebrow. The flame opened anyway.

Ilyr stood before the arch and said nothing for so long Mara heard water dripping somewhere far below.

Vaura's face remained unreadable. "Exile?"

Ilyr looked at his mother. "I hoped Maelin was dead because dead would mean I had no more chances to fail her."

The gate did not open at once.

The truth had landed, but not finished.

Ilyr closed his eyes. "And because if she lived, she remembered what I chose."

The blue flame split.

Mara was last.

The gate's heat was cold. It crawled over her scars, into the cuts that never quite stopped aching, into the empty places the hymn had tried to fill with a cleaner Mara.

Necessary truth.

She could say she feared Vorrakai. True. She could say she feared command. True. She could say she feared becoming saint, weapon, ruler, mistake. All true. Not necessary.

The cinder at her hip listened.

"I miss being useful," Mara said.

The others went very still.

She stared into the blue flame because looking at them would make the truth dress itself.

"I hate it. I know what usefulness did to me. I know what it did to the dead in Kell Ashgate. But some part of me still wants someone to need me clearly enough that I do not have to decide who I am without work in my hands."

The gate opened.

Not gently.

The blue flames pulled apart and showed Khar Veyl below.

The city descended around an underground lake so wide its far shore vanished into violet haze. Basalt terraces stepped down the cavern walls, each level linked by bridges of chain, black stone, and root-fire. Fungal stars glowed across the ceiling in constellations that had never seen night. Markets hung in vertical tiers. Blade schools rang with steel on stone. Canal boats moved across dark water with lamps hooded low. Archive towers thrust downward from the cavern roof like ink-black stalactites, their windows lit from within.

It was beautiful.

Not clean. Not kind. Not safe.

Alive.

Mara exhaled.

"Welcome," Vaura said, "to the city that keeps what the surface cannot bear."

"Does it return what it should not keep?" Mara asked.

For the first time, Vaura's expression changed.

"That," she said, "is why you are alive enough to enter."
""",
    14: r"""## Chapter 14: Banquet of True Shadows

The Banquet of True Shadows began before anyone ate.

Khar Veyl's feast hall hung over the underground lake on seven black chains, each chain thicker than an old tree and carved with witness marks. The floor was obsidian polished so deeply that Mara saw not only her reflection, but the reflection of every person trying not to look at her. Root-fire lamps burned blue in niches along the walls. Above, fungal stars glimmered in carved constellations: the Broken Scale, the Closed Eye, the Sister with Two Knives, the Road That Goes Under.

Courses arrived on obsidian mirrors.

Nobody touched them.

"Is the food cursed?" Kesh whispered.

Ilyr, seated beside him by deliberate cruelty or tactical humor, said, "Probably not in the way you mean."

"That sentence lacks nourishment."

Mara sat at the low table assigned to surface witnesses. The Umbral Seat occupied the crescent dais: nine figures in black, silver, and muted jewel tones, each with a blade, book, or memory vessel placed before them. Vaura Noct-Vey sat among them, not at the center. The center belonged to an empty chair draped in blue-black cloth.

"Maelin?" Mara asked.

Ilyr did not look at the chair. "No. The absent record."

"That is a person?"

"In Khar Veyl, sometimes."

Across the hall, delegations watched from shadowed galleries: blade students, archive wardens, under-market brokers, exile clerks, house heirs, canal captains, and three figures veiled in gray whom everyone seemed to avoid looking at directly. Refugees from the surface had been given a narrow gallery under Brakka's road mark. The three named dead sat there too, because Khar Veyl had not decided whether to honor or fear them and had compromised with good seating.

Vaura struck a black spoon against an empty bowl.

Every lamp dimmed.

"The Banquet of True Shadows receives contested witnesses," she said. "Here, a lie changes light. A truth changes appetite. An evasion changes seating. Speak with intention or be rearranged by architecture."

Tavi leaned toward Mara. "I want to hate that, but as civic design it has power."

The first course was clear soup in black cups. It tasted of mushrooms, salt, and something floral Mara distrusted until she realized it was simply pleasant. Each guest drank, then spoke a formal opening.

Vaura began. "Khar Veyl did not invite war."

The hall's light shifted.

Not much. One blue lamp behind her turned green.

A murmur ran through the hall.

Vaura looked at the lamp and inclined her head. "Correction. Khar Veyl did not invite this war honestly."

The green lamp returned to blue.

Mara stared. "That is allowed?"

Ilyr's mouth tightened. "Public correction before challenge. Yes."

Serathiel would have loved and hated this room.

One by one, members of the Umbral Seat spoke. Some admitted Khar Veyl had retained records. Some insisted retention preserved the world. Some said Lumenorath's cleansing decree proved every old caution wise. Each time a word bent too far, the lamps changed: blue to green for omission, blue to red for falsehood, blue to violet for truth sharpened into threat.

Then the Seat questioned Mara's company.

Caldus stood with staff in hand. "I broke oath to a king after keeping it too long."

No lamp changed.

Saelith stood. "I served a law that hurt people and still fear a world without law."

No lamp changed.

Tavi stood. "I can build the thing everyone here is afraid someone else will build first."

Every lamp went white.

That was apparently not a lie color. It was worse. Interest.

"Sit down," Mara, Caldus, and Ilyr said together.

Tavi sat. "I phrased that responsibly."

Kesh rose before anyone called him, which made several judges reach for note tablets.

"Kesh of the Kavik Road," Vaura said. "Smuggler, debt-runner, route-seller. You have carried records through three jurisdictions while wanted in five. What is your intention below?"

"To survive with style."

Four lamps went green.

Kesh sighed. "Fine. To help my friends survive with style."

Two green lamps remained.

He rolled his eyes. "To help my friends survive, even if it makes my life financially incoherent."

The lamps returned to blue.

Mara smiled despite herself.

Then a violet lamp flared above the empty chair.

The hall stilled.

From the far gallery, a voice said, "Ask him what he sold before the fever roads."

Kesh went still.

Rikka had not come below. No Kavik elder stood here. The voice belonged to a Veyra broker with coin moths pinned to his sleeves, a thin man smiling like a contract written in small script.

"Under-market has records," the broker said. "Kavik Kesh sold a flood route to a fever boss. Three villages suffered. He travels now with a cinder-singer who speaks names. Does she know all of his?"

The hall's light leaned toward Kesh.

Mara did not rescue him. She hated that she knew not to.

Kesh's hands flexed at his sides. "She knows enough."

Three lamps went red.

Silence sharpened.

Kesh closed his eyes. "No. She does not. I sold the route. I suspected what it would be used for. I told myself suspicion was not knowledge because knowledge would cost more. People died. I bought medicine with the money. That part is also true and not enough."

The lamps burned blue.

No one moved.

Mara felt the shape of the bargain he had always made with himself: survival on one side, guilt on the other, jokes laid like planks between them. The banquet had kicked the planks away.

The broker smiled. "And if offered the same price today?"

Kesh looked at Mara, then away. "Today I would try to steal the medicine, lie about the route, and offend everyone more efficiently."

One lamp turned green.

"I would fail at least once," Kesh added.

Blue.

Brakka grunted approval. "Good bad truth."

The hall did not know whether to record that.

At last Ilyr stood.

The empty chair's cloth stirred though no wind moved.

Vaura's hand tightened on her spoon. "Ilyr Noct-Vey, exile of House Noct-Vey, accused half-witness, called by Maelin's retention. What is your intention below?"

Ilyr looked at the Umbral Seat, at his mother, at the empty chair, at Mara.

"To finish betraying my house correctly."

The hall went black.

Every lamp extinguished.

For one breath, darkness held them.

Then the floor lit from beneath, showing shadows instead of faces. Each person cast not one shadow, but several: the self they offered, the self they hid, the self they feared, the self someone else needed them to be. Mara saw her own shadows at her feet: ash-runner, saint, weapon, child, commander, empty-handed girl. She did not like any one of them alone. Together, at least, they made a crowd harder to use.

Across the hall, Ilyr's shadows split like broken glass.

One held a sealed record. One held a bloody knife. One turned away from a younger woman reaching through bars.

The empty chair spoke with Maelin's voice.

"At last," it said.

Ilyr flinched.

Vaura stood. "The retained witness is not scheduled."

"Retained witnesses dislike schedules," Maelin's voice replied.

Mara saw the blue-black cloth over the empty chair lift as if someone beneath it had taken a breath.

The Banquet of True Shadows had found its appetite.
""",
    15: r"""## Chapter 15: The Half-Truth Knife

Maelin Noct-Vey arrived as a voice, a shadow, and a legal problem.

The empty chair at the Banquet of True Shadows remained empty. The blue-black cloth over it shaped itself into the outline of a seated woman, then lost the shape, then found it again from another angle. A retained witness, Ilyr had explained once, was neither prisoner nor ghost by Khar Veyl's law. It was a category created by people who enjoyed not admitting what they had done. Maelin's body was somewhere under guard. Her testimony had been separated, indexed, and allowed to appear where useful.

Mara understood enough to be furious.

"Put her back in herself," she said.

The hall erupted.

Vaura's spoon struck the bowl. "Surface witness will not instruct retention law."

"Then retention law can stop behaving like theft with footnotes."

Kesh whispered, "The footnotes will be armed."

Maelin's chair laughed.

The sound struck Ilyr visibly. Not because it was cruel. Because it was familiar.

"She is delightful," Maelin said. "You brought a hammer to a room of scalpels, brother."

Ilyr's face had gone bloodless. "Maelin."

"You took your time."

The Umbral Seat conferred without moving their mouths. Shadows leaned between them, carrying words too low for surface ears. Tavi pretended not to adjust a device under the table. Caldus saw and moved his staff to hide her hand. Saelith watched Maelin's chair with healer's horror. Brakka watched the floor, perhaps listening to the hall decide whether to become road or trap.

Vaura spoke. "The retained witness may answer three questions before being returned to custody."

"No," Ilyr said.

The word rang.

The hall's lamps stayed blue.

He stepped away from the table. "No more measured truth. No more enough to move the next knife. If Maelin testifies, she testifies in full. If I answer, I answer in full. If House Noct-Vey falls, let it fall with proper documentation."

Vaura's expression did not change, which meant something in her had.

"You demand much for an exile."

"I learned appetite from home."

The empty chair sighed. "Better."

From the Umbral Seat's center, an old judge with silver eyes lifted a narrow blade from a case. Its edge was black. Its handle was white. The two colors did not meet cleanly; they overlapped in a gray seam down the middle.

"The Half-Truth Knife," Ilyr said.

Mara leaned toward him. "That sounds like something a healthy court would avoid naming."

"It cuts testimony from excuse."

"Of course it does."

The old judge set the knife on the table before Ilyr. "Speak with hand on blade. Omission draws blood. Falsehood takes memory. Full truth leaves scar."

"Absolutely not," Caldus said.

Ilyr put his hand on the blade.

Blood welled at once.

Mara started forward. Ilyr stopped her with one look.

"My house guarded the third under-seal of the dragon-moon," he said. "Seventy-three years ago, House Noct-Vey discovered pulse fractures and concealed them from the Umbral Seat."

The knife darkened.

Blood ran over his fingers.

"Correction," he said through his teeth. "Elements of the Umbral Seat knew enough to prefer deniability."

Three lamps went green, then blue.

Vaura closed her eyes briefly.

Ilyr continued. "My grandfather sold curated memory access to Lumenorath hardliners seeking proof that shadow carried original guilt. My mother knew."

All eyes turned to Vaura.

The judge did not look away. "I knew after the second sale."

The knife cut deeper into Ilyr's palm until Mara smelled blood over the feast.

"My father sold under-script to human intermediaries," Ilyr said. "Regulator geometry. Command dampening. Corpse-hook theory disguised as preservation mechanics. I found the ledger. I exposed the light-elf purchases. I hid the human line."

Mara saw the foundry.

Not memory. Not magic. Rage reconstructing what truth made possible: Mordane's hooks, Joryn chained, dead workers with number plates, Arveth burning bright enough to become final witness. Under those horrors, old under-script sold by a house that had thought itself too careful to be monstrous.

Ilyr's voice shook once. "I told myself Khar Veyl would collapse if human kingdoms learned enough to accuse us before we had secured the deeper seal. I told myself sequence mattered. Maelin told me sequence had become cowardice with a timetable."

The chair's shadow bowed its head.

"She stole the missing ledger," Ilyr said. "I fled with the lesser proof and let the court retain her as sole illegal carrier. I believed I would return quickly."

The knife went still.

"I did not."

No lamp changed.

Full truth leaves scar.

Ilyr lifted his hand from the blade. A gray line crossed his palm where the cut closed too quickly, leaving something that looked less healed than marked.

Mara could not speak.

If she spoke too soon, she would use the truth as a weapon because it hurt and weapons were easier than grief.

Saelith spoke first. "Lumenorath bought proof of guilt because it wanted permission to fear."

Maelin's chair turned toward her. "Yes."

"Khar Veyl sold proof in pieces because it wanted payment for being right."

"Also yes."

Tavi's voice was very quiet. "Humans built machines from the pieces."

"And gnomes improved them," Maelin said.

Tavi flinched as if struck.

"Trolls kept roads open and asked fewer questions when tolls were paid," Brakka said.

Maelin's chair angled toward her. "Yes."

Kesh swallowed. "Goblins carried messages between people who paid not to meet."

"Yes."

The banquet hall had gone painfully blue. Not pure. Honest. There was a difference, and it had teeth.

Mara looked at Ilyr.

"You should have told me before Lumenorath," she said.

"Yes."

"Before the foundry, if you knew enough."

"I did not know Mordane's line. I knew enough to suspect human use."

"That is not better."

"No."

His acceptance made anger harder to throw and harder to put down.

The old judge reached for the Half-Truth Knife.

Mara put her burned hand over it first.

Every blade in the hall whispered from its sheath.

"Mara," Caldus warned.

The knife bit her palm with cold.

She did not speak to the court. She spoke to the cinder memory under it, to the dragon-moon pulse beneath all their careful architecture, to the parts of herself that still missed usefulness because usefulness told pain where to stand.

"I want someone to pay enough that the dead feel answered," she said.

The knife cut.

"I know punishment can become another machine if I feed it names too quickly."

The knife burned.

"Ilyr Noct-Vey is witnessed guilty of half-truth. House Noct-Vey is witnessed guilty of sale. Khar Veyl is witnessed guilty of secrecy made profitable. Lumenorath is witnessed guilty of beauty made custody. Harrowmere is witnessed guilty of arithmetic made law. Brassroot is witnessed guilty of tools outrunning conscience. The road clans are witnessed guilty of passage priced against desperation. I am witnessed wanting this to make someone simple enough to hate."

The knife stopped cutting.

The hall did not move.

Maelin's chair whispered, "There."

The blue-black cloth collapsed.

For one heartbeat Mara thought they had lost her. Then a door opened behind the Umbral Seat, and a woman walked in under guard.

Maelin Noct-Vey was thinner than Ilyr, shorter than Mara expected, with silver hair cut at her jaw and a face so like Ilyr's that the differences hurt: less guarded, more exhausted, eyes bright with fever and savage amusement. Black retention marks ringed her throat and wrists.

Ilyr made a sound.

Maelin looked at him. "Do not cry. It will make Mother smug."

Vaura did not smile. Her eyes shone anyway.

The Umbral Seat erupted into argument.

Hardliners demanded Maelin's return to custody. Seal wardens demanded immediate mobilization against Lumenorath before Serathiel reached the lower passes. Archive judges demanded copies, delays, procedures, blood. Under-market brokers began pricing evacuation routes in whispers until Kesh turned and showed his teeth.

Mara pulled her hand from the knife. Gray marked her palm beside old burns.

Maelin crossed the hall, guards uncertain whether law required stopping her. She stopped before Mara.

"You are the cinder-singer."

"You are the retained sister."

Maelin's mouth twitched. "Let us both become less useful."

Mara liked her immediately, which was inconvenient.

Then horns sounded from the lower lake.

Three notes.

Ilyr went rigid. Vaura's face hardened. The Umbral Seat fell silent.

"Lumenorath?" Caldus asked.

"No," Maelin said.

Far below, through the feast hall's obsidian floor, something vast pulsed blue-black beneath the city.

"The dragon-moon heard the knife," she said.
""",
}


EXPANSIONS: dict[int, str] = {
    13: r"""The descent from the gate into the city took an hour because Khar Veyl believed arrival should educate the feet.

Their escort did not bind them. That would have been too simple. Instead, Vaura assigned seven witness-clerks, two blade students, one canal guide, and a child no older than twelve who walked backward in front of them reciting every law they were currently violating by being alive in the wrong place. His name was Siven, and he took the work with grim delight.

"Surface fire-bearing witness must not touch root-fire unless invited by keeper, emergency, duel, flood, or recognized metaphor," he said.

"Recognized by whom?" Tavi asked.

Siven frowned at his tablet. "Pending committee."

"I respect him," Tavi said.

Khar Veyl opened around them in levels. On the upper terraces, blade schools practiced under blue lamps, students moving in silence while instructors corrected them with taps of ink-black rods. On the market tier, vendors sold memory-safe paper, sealed jars of echo-water, mushrooms that glowed only when insulted, and knives labeled according to whether they were for cooking, testimony, or family. Along the canals, boatwomen poled flat craft through dark water while singing numbers backward to measure depth. No one stared openly at Mara's scars. Everyone noticed them.

That was different.

In Lumenorath, looking had been a form of arrangement. Here, not looking was a form of record. Mara felt herself entered into hundreds of private ledgers before she reached the guest house.

The guest house had no beds that adjusted themselves. It had narrow cots, clean blankets, a basin of hot water, and a note on the wall:

Hospitality is not trust.

Kesh read it twice. "Finally, honest lodging."

Ilyr stood by the window, looking down at the lake. Far below, small lights moved across the black water toward an island archive.

"Where is Maelin?" Mara asked.

"Retained witnesses are kept where escape would be legally inconvenient."

"That sounds like everywhere here."

"Yes."

He touched the window frame. His hand shook once, then steadied. "I thought returning would make me feel judged. It is worse. It makes me remember when I wanted judgment to mean belonging."

Mara joined him at the window. Across the cavern, a group of children ran along a bridge with slates under their arms, laughing until an adult corrected their volume with one raised finger. They lowered their voices and kept laughing. Khar Veyl had not killed joy. It had trained joy to carry documentation.

"This place is not what surface stories said," she said.

"No place is."

"It is still frightening."

"Yes. Stories sometimes find the right wound for the wrong reason."

Below, a horn sounded from the feast hall. Vaura's invitation arrived on a strip of black paper that unfolded from the door's shadow without anyone opening it.

Kesh read over Mara's shoulder. "Banquet of True Shadows. Formal witness. Possible seating rearrangement. Oh good. Dinner with furniture that judges."

Brakka took up her maul. "Eat truth first."

"I prefer bread first."

Mara looked once more at the lake. Somewhere under it, the dragon-moon pulse waited. Somewhere in this city, Maelin waited with her testimony separated from her hands. Somewhere above, Serathiel's cleansing campaign had begun moving toward the lower passes.

Every road now led into someone's careful fear.

Khar Veyl at least had the courtesy to label the door.
""",
    14: r"""Maelin's unscheduled voice changed the banquet from courtship to surgery.

No one reached for food after that. Servants came silently and removed the mirror plates, leaving the table bare enough to look like a battlefield. The blue lamps remained low, so every person in the hall was known by shadow first and face second. Mara understood then why Khar Veyl loved this room. In ordinary light, everyone could pretend to be one self at a time.

Here, plurality had teeth.

Vaura spoke into the darkness. "Retained witness, state how you entered the banquet record."

Maelin's chair rustled. "Badly."

One lamp went green.

"Fine," Maelin said. "Through a kitchen shadow, an under-market favor, two sympathetic clerks, and Siven's lunch box."

From somewhere near the door, the law-reciting child squeaked, "It was sealed!"

Kesh leaned back, delighted. "I adore him."

Vaura's gaze cut toward the child. "Later."

The broker with coin moths on his sleeves rose. "This circus proves why retained testimony cannot be permitted loose. Lumenorath marches. We should seal the upper roads, strike the white-root supply roots, and hold the dragon-moon record until the surface exhausts itself."

Several lamps turned violet: truth sharpened into threat.

A blade-scholar stood from the opposite gallery. "Strike first, and Serathiel's decree becomes prophecy. Wait, and her army reaches the lower pass. The surface has forced our hand."

Green light flickered.

Mara stood.

Ilyr caught her sleeve. "This room eats quick speeches."

"Then I will chew."

That was not as clever as she wished, but Kesh nodded supportively.

Mara faced the Umbral Seat. "You keep saying surface like it is one thing. Harrowmere burned poor people for heat. Lumenorath turns mercy into custody. Brassroot builds tools too quickly. Goblins sell roads. Humans look away. Khar Veyl sells truth in doses. There is no clean above for you to hide from and no clean below for you to hide in."

The hall's lamps stayed blue.

That helped.

"Serathiel is marching because fear found a beautiful road," Mara continued. "If you strike first, fear finds a dark one too. If you seal everything, the dragon-moon keeps waking under all of us while courts congratulate themselves on not losing arguments."

"And your alternative?" asked the old judge who had not yet named himself.

Mara hated that question. Alternatives were where speeches went to be murdered by reality.

"Open Maelin's full record to mixed witness," she said. "Light, dark, human, gnome, goblin, troll, named dead. No one owns the first confession. No one gets to carry only the part that makes them righteous."

The hall reacted as if she had suggested everyone dine naked.

Tavi whispered, "I am revising several engineering metaphors in admiration."

The old judge leaned forward. "Mixed witness has no standing in under-law."

Brakka's maul thudded once. "Then under-law too short."

Vaura looked at the troll. "You would place Seven Arches law over Khar Veyl?"

"No. Beside. Bridges work that way."

Blue lamps brightened.

Maelin's chair gave a soft, pleased hum. "I told you surface roads were becoming interesting."

Ilyr stood at last. His shadows gathered around him like witnesses unwilling to be dismissed.

"Mother," he said.

Vaura did not move, but the title struck her harder than any accusation.

"If you return Maelin to retention after this, House Noct-Vey survives one more night and dies correctly later. If you release her, we may die incorrectly now with better company."

"That is your argument?" Vaura asked.

"My arguments were more elegant when I was a coward."

For one breath, the hall forgot to be disciplined.

Then Vaura turned toward the old judge. "Bring the Half-Truth Knife."

Ilyr's face did not change.

Maelin's chair whispered, "There you are."
""",
    15: r"""The first argument after the horn was about whether anyone had heard it.

This, Mara decided, was how courts survived themselves: when terror arrived, they debated the receipt. The old judge claimed the third note came from the lower lake. A blade-scholar insisted it came from the western seal. An under-market broker suggested it might have been a resonance artifact caused by unauthorized retained testimony, which made Maelin laugh until one guard remembered to look offended.

Then the floor pulsed again.

No one argued with that.

Blue-black light rose through the obsidian. For one breath, the feast hall became transparent enough to show the lake below, and beneath the lake, far beneath stone and water and law, a curve of pale darkness too vast to belong underground. Not the full dragon-moon. A hint of horizon where no horizon should be.

Mara's knees weakened.

The cinder at her hip answered with painful warmth.

Every lamp in the Banquet of True Shadows went white.

Interest, Tavi had called it earlier.

This was not interest.

This was recognition.

Maelin gripped the back of the empty chair as if she could hold the city in place. "The lower seal heard mixed witness through the knife."

"Impossible," said the broker.

Tavi made a strangled sound. "I have had a very long week with that word."

Vaura rose. "Seal wardens to station. Archive judges secure the third ledger. Blade schools to ready without deployment. No one strikes Lumenorath without Seat vote."

"Too slow," the blade-scholar snapped. "Serathiel's vanguard reaches the lower passes by second dark."

"Then run faster to your station."

The command cracked like a whip. For a moment Mara saw the power Vaura had kept sheathed: not kindness, not apology, but the ability to make disciplined people remember why discipline had survived.

The hall began moving.

Not panic. Khar Veyl did not waste fear that way. Shadows detached from galleries and became messengers. Judges folded records into waterproof cases. Blade students took positions at doors. Servants cleared paths before anyone thought to ask. The named dead from the witness gallery rose together, their painted faces turned toward the light under the floor.

Edrin Vale spoke. "That is not only dragon."

Mara looked at him. "What do you hear?"

"A city under a city. Dead law answering old moon."

Maelin's eyes sharpened. "Orrowen."

The name moved through the hall like a draft from an opened tomb.

The old judge with the Half-Truth Knife wiped the blade with a black cloth and looked at Mara. "Cinder-singer. You asked mixed witness. You have woken mixed jurisdiction."

"That sounds like blame wearing a hat."

Kesh nodded. "A formal hat."

The judge ignored him. "If Orrowen's dead heard the knife through the dragon-moon, they may claim standing."

Saelith stepped close to Mara. "Can they?"

Ilyr answered. "If they remember being citizens."

Brakka's amber eyes brightened. "Dead city with law. Road getting crowded."

Mara almost laughed. It came out as a breath.

Maelin crossed to Ilyr. The guards let her because everyone was suddenly busy with larger disasters or because Vaura looked away at exactly the right moment.

"You bled prettily," Maelin said.

Ilyr stared at her, grief and relief fighting so hard neither won. "You are alive."

"Retained. Try to keep up."

"I am sorry."

"Yes."

He flinched.

Maelin touched the gray scar across his palm. "Be sorry while moving. It saves time."

Mara liked her even more. Inconvenient had become inadequate.

Vaura approached them. For a moment mother, son, and daughter stood inside the same pool of white lamp light, each carrying a different version of the same family wound.

"Maelin remains under guard," Vaura said.

Mara began, "No."

Maelin held up one hand. "Let her finish the terrible compromise."

Vaura's jaw tightened. "Maelin remains under guard but no longer separated from her testimony. She will accompany the mixed witness party to the drowned archive."

"What mixed witness party?" Caldus asked, though his face said he already knew.

Vaura looked at Mara. "Yours."

"We just arrived."

"And have proved unusually efficient at making hidden catastrophes public."

Tavi brightened despite everything. "That may be the nicest insult I have ever heard."

Vaura did not blink. "The drowned archive contains the shared crime's oldest surviving ledger. Light and dark entries, before the split became doctrine. If Serathiel reaches the lower pass with only her version, Khar Veyl hardliners will strike first. If we open the drowned archive with mixed witness, we may delay both armies long enough to choose a less catastrophic mistake."

Mara looked at Maelin. "Is that where the full record is?"

"One full record," Maelin said. "There are always more. Anyone promising final truth is selling furniture."

Kesh sighed. "I am learning and resent it."

The horn sounded again, one note this time, deep enough to tremble in Mara's teeth.

Far below, the dragon-moon pulse faded, but the silence after it was worse. It felt attentive.

Mara looked at Ilyr's scarred palm, her own gray cut from the knife, Saelith's clasp scar, Tavi's burned sleeves, Brakka's road-marked hands, Kesh trying not to look shaken by a room that had made his guilt visible, Caldus bracing himself for yet another road where rank would not save anyone.

"Drowned archive," she said.

Vaura nodded. "You leave within the hour."

"Of course we do," Kesh said. "I was worried we might digest."

Maelin smiled at him. "There will be archive crabs."

"I withdraw all optimism."

Mara touched the cinder cage at her hip. Under the city, under the lake, under every court that had tried to own a piece of history, the moon below the world listened.

For the first time, it had listened back.
""",
}


DEEPENING: dict[int, str] = {
    13: r"""The guest house did not keep them long.

Khar Veyl believed rest was what one earned after orientation, and orientation was apparently a civic weapon. Siven returned with a stack of black tablets and informed them that surface witnesses had to be shown the civic strata before banquet so they could not later claim ignorance as legal shelter.

"He says this like ignorance is a cloak we brought for weather," Tavi said.

"Ignorance is very warm," Siven replied. "People wear it often."

Mara liked him despite herself.

The tour descended by canal lift. The platform lowered through mist beside a chain bridge where Veyra children practiced blade footwork on numbered stones. Below that lay the echo market, louder than Mara expected and quieter than any surface market its size. Vendors called prices in half-voices. Contract bells chimed in bowls. Coin moths fluttered over ink, their wings stamped with tiny valuations. A mushroom seller argued with a memory-paper maker about whether "freshly harvested silence" could be advertised if three people had already commented on it.

"This is less grim than promised," Kesh said.

Siven gave him a pitying look. "You are standing in the tourist-facing shadow economy."

"I retract admiration and replace it with professional concern."

They passed a school where young scribes practiced copying testimony while water dripped steadily onto the page. If the ink ran, Siven explained, the testimony had been written to flatter dryness. They passed a shrine containing no statue, only a table and a single empty chair for anyone whose name had been removed elsewhere. They passed a public board listing corrections to yesterday's public board.

At the correction board, Edrin Vale stopped.

The named dead stared at the neat columns. "You correct records publicly."

"If correction is sealed, error keeps office," Siven recited.

"Who may request correction?"

Siven hesitated. "Citizens."

The word stood like a gate.

Edrin's painted face did not change. "I was a citizen of Orrowen. Executed by three regimes, recorded by none of yours. Am I eligible?"

Siven looked to Vaura's clerks. The clerks looked at one another. Law, Mara was learning, had many ways to become weather.

Brakka set one hand on the correction board's frame. "Dead witness asks road. Board says no?"

The frame creaked.

"Do not break the civic board," Caldus said.

"Board considering flexibility."

Mara stepped beside Edrin. "If Khar Veyl keeps what the surface cannot bear, it can bear a correction request from the dead."

One clerk, younger than the others, swallowed and produced a blank strip. "Provisional standing may be recorded pending Seat review."

Edrin took the strip. His stiff fingers trembled. "Write: Orrowen citizen Edrin Vale objects to being discussed as evidence before being received as person."

The clerk wrote.

The public board accepted the strip.

No bells rang. No law collapsed. A few market-goers stopped to stare. One old Veyra woman touched two fingers to her brow in respect before moving on.

Mara felt the cinder at her hip warm.

Not command. Approval, perhaps, though she distrusted approval from dead dragons. Still, something under the city had noticed a dead citizen entering a living correction board.

Vaura, who had joined them without announcing herself, watched the board. "You make standing contagious."

"You say that like disease."

"I say it like infrastructure stress."

"Good," Mara said. "Stress shows what was carrying too much."

Vaura's eyes narrowed, not in anger. Assessment. "You speak like someone who has watched a mine roof."

"I have."

"Then understand this: if too many props are removed at once, everyone dies under honest stone."

Mara looked up through the cavern haze toward the sealed roads where Serathiel's army moved somewhere above. "If rotten props stay because removing them is dangerous, everyone dies slower and calls it architecture."

Vaura almost smiled.

"Come," she said. "The banquet will enjoy you or attempt to digest you."

"Is there a third option?"

"Only for citizens."

Behind them, Edrin's correction strip dried on the public board, a small line of dead objection in a city that had not yet decided whether it was brave enough to read it aloud.
""",
    14: r"""The second course arrived after Maelin's voice and before anyone could pretend appetite had survived.

It was served in covered bowls of black glass. When the lids lifted, each person saw a different meal. Mara saw Dilla's pepper stew, steam rising as if from home. Kesh saw Kavik marsh cakes and went dangerously quiet. Saelith saw a white bowl of clear broth and pushed it away before anyone asked why. Ilyr saw nothing at all. His bowl remained empty.

"Memory course," he said.

"That seems invasive," Mara said.

"It is."

Vaura lifted her spoon. "The course reveals what the witness believes comfort costs."

Tavi peered into her bowl. "Mine is a burnt kettle valve. I feel accused by dinner."

The old judge at the Seat, whose name was Thalan Vey, asked the first deliberate question of the course. "Mara Venn, what does comfort cost?"

Mara stared at the stew. For one cruel second she smelled Dilla's kitchen so clearly that the cavern hall vanished: onions, pepper, ash on coats, Joryn pretending not to hover, Niv stealing crust. She wanted to eat so badly her hand shook.

Then she looked at Ilyr's empty bowl.

"Sometimes comfort costs the truth you do not want to interrupt it," she said.

Her stew darkened but did not disappear.

Blue lamps held.

Thalan turned to Saelith. "And you, Pale Bough severed?"

Saelith's fingers curled around the bowl she would not eat. "Comfort cost me the right to notice pain that had permission."

A violet lamp flared, then blue. Threat turned into truth, or truth refusing to be harmless.

The Seat murmured.

The broker with coin moths leaned forward. "Dark courts are not on trial for light-elf childhood."

Maelin's empty chair answered, "All courts are on trial for the childhoods they produce."

Mara heard a soft sound from the gallery. Siven, maybe. Or one of the blade students. It was gone quickly.

Kesh had not touched his marsh cakes.

The broker noticed. "And Kavik comfort?"

Kesh looked at the bowl. His usual smile approached, saw the room, and wisely retreated.

"Comfort cost me the ability to say I had no choice," he said.

Blue.

The banquet did not forgive him. It made the truth sit near him like an unpaid guard.

Then the third course came: obsidian mirrors with no food on them, only reflections of the person seated across from each guest. Mara's mirror showed Vaura. Vaura's showed Mara. That was intentional. Khar Veyl trusted coincidence less than it trusted knives.

"Question across reflection," Vaura said. "Each asks one. Each answers."

Mara looked at the judge who was Ilyr's mother, Maelin's keeper, and possibly the only reason they had not been imprisoned at the gate.

"Did you sell under-script to humans?" Mara asked.

The hall went still.

Vaura's reflection did not blink. The real Vaura did not either.

"No."

Blue lamps held.

Mara's stomach turned with relief she did not want.

Vaura continued. "I allowed the house to delay exposing that it had been sold."

Green flared, corrected to blue before anyone could speak.

"Why?"

"One question," Vaura said.

The rules mattered now because they protected the answer she had already given. Mara understood that and hated it.

Vaura looked at her reflection of Mara. "If you gain proof that one person you love enabled a horror you survived, will you preserve their personhood while seeking consequence?"

Mara wanted to look at Ilyr.

She did not.

"I do not know," she said.

The lamps stayed blue.

The answer ashamed her. The banquet accepted it anyway.

Around the hall, other questions cut. Caldus was asked whether discipline without kings could survive fear. He answered that it had better, because kings had not survived morality. Tavi was asked whether she would destroy her own notes if the command engine became possible. She said yes, then corrected under green light: "I would hide one copy out of terror that destruction might doom someone. Then I would need friends willing to steal it from me." Brakka was asked whether road-law could bind people who did not honor roads. She said, "Feet honor road by needing ground."

No one improved on that.

By the time Ilyr stood, the room had already bled more truth than any sane dinner required.

That was when Maelin's voice entered.
""",
    15: r"""They left the banquet hall through a corridor that had not existed before Maelin was given back her testimony.

Khar Veyl architecture, Mara decided, behaved like a bureaucrat with secrets and excellent stonework. One moment a wall held a mural of the first under-road. The next, after Vaura pressed two fingers to a witness mark and spoke a word too low to hear, the mural split into stairs descending toward the lake.

Maelin walked between two guards. Not bound. Not free. The retention marks at her throat glimmered whenever she moved too far from Vaura's shadow.

Ilyr kept looking at them.

"Stop," Maelin said.

He looked at her face instead.

"That too, eventually," she added.

"I do not know how to do this."

"Good. Confidence would be obscene."

Mara followed close enough to hear because Maelin had made no effort to lower her voice and because everyone in this family seemed to bleed in public while pretending it was procedure.

"Did they hurt you?" Ilyr asked.

Maelin glanced at Vaura's back. "Yes."

Vaura did not stumble.

"Did Mother order it?"

"Sometimes. Sometimes she prevented worse. Sometimes that is not absolution. You see? Nuance. Our ancestral curse."

Ilyr's face folded around pain.

Mara slowed until she walked beside him. "You do not have to earn forgiveness before the next stair."

"In Khar Veyl, one can be invoiced for less."

"I am serious."

"So am I."

Maelin turned her head. "He thinks if he arranges remorse elegantly enough, I will have fewer years missing."

"Will you?" Mara asked.

Maelin smiled. "I like her."

Ilyr made a helpless sound that was almost a laugh.

The stairs opened onto a dock carved directly into the cavern wall. Black water slapped the stone. Canal boats waited there, long and narrow, with root-fire lanterns hooded at bow and stern. Across the lake, archive towers pierced the water upside down, their lower floors drowned, their upper floors hanging from the cavern roof in defiance of ordinary architecture. Pages drifted on the surface around them, pale as fish.

The drowned archive.

Even from here, Mara felt its memory pressure. Not a voice. A weight. Thousands of records soaked, distorted, preserved by salt and cinder, each one waiting to be read by someone willing to admit no page was clean.

Tavi stepped onto the dock and forgot to joke.

"Liquid glass residue in the water," she said. "Old gnome sealant. Very old. Very expensive. Very misused."

Vaura looked at her. "The archive was flooded during the split to prevent either court from removing the full ledger."

"That is a sentence containing at least three disasters disguised as decisions."

"Yes."

The admission startled Tavi enough to silence her.

Behind them, horns sounded again from the feast hall, then from the upper terraces. Different pattern. Caldus listened, soldier still alive under exile and staff.

"Alarm."

Siven appeared at the stair mouth, breathless, clutching his tablet. "White-root vanguard at the lower western pass. Khar Veyl hardliners moving without full Seat authorization. Also someone stole six canal permits."

Kesh looked offended. "I have been with you the entire time."

"No one accused you."

"You included it in my direction."

Vaura took the tablet. Her face hardened. "The hardliners mean to meet Serathiel before the Seat can vote."

"Then the archive matters now," Mara said.

"It mattered before," Vaura replied. "Now others know."

Maelin stepped to the edge of the dock. The black water reflected her retention marks as rings spreading from her throat.

"The full ledger is in the east stacks," she said. "Underwater, behind archive crabs, pressure locks, and a memory current that makes readers relive the last lie they benefited from."

Kesh closed his eyes. "I miss roads that merely taxed blood."

Saelith looked across the water. "Can the ledger stop the armies?"

Maelin's smile faded. "No. Ledgers do not stop armies. People who can no longer pretend they do not know sometimes slow them."

Mara thought of the knife cutting her palm. I want someone to pay enough that the dead feel answered. The desire still lived in her. It had not become noble because she named it.

Ilyr stood beside her, staring at the water.

"I sold you a half-truth until it reached your dead," he said quietly.

"Yes."

"I do not ask you to trust me."

"Good."

"I ask to go into the archive first."

Mara looked at him then. "To prove something?"

"To pay something."

"No."

He blinked.

"You go because you can read the locks," she said. "You come back because Maelin just got herself partly un-stolen and I refuse to carry your elegant guilt through another funeral."

Maelin laughed. "I do like her."

Ilyr's eyes shone. He looked away before the tears could decide.

Vaura assigned boats with ruthless speed. Mara, Ilyr, Maelin, Tavi, and Saelith in the first. Caldus, Brakka, Kesh, Edrin, and two Veyra wardens in the second. Siven tried to climb into the third with the clerks and was stopped by Vaura without a word.

"But the tablet record-" he began.

"Will be updated by someone not twelve."

"Thirteen in two months."

"Then survive two months."

Siven looked mutinous. Mara understood him better than she wanted to. Being left behind because adults called danger practical had nearly defined her whole life.

She took the torn strip of banner from her pack, the one from the first road camp, and tore a smaller piece from it. "Record this," she told him, handing it over. "Mixed witness party entered drowned archive because every court had made truth too small."

Siven clutched it with both hands. "That is not formal phrasing."

"Good."

The first boat pushed away from the dock.

Black water accepted them without ripple.

Above, horns called armies toward each other.

Below, pale pages circled the oars like fish with something to say.
""",
}


FURTHER_DEEPENING: dict[int, str] = {
    13: r"""Before the banquet summons, the named dead were separated from the living for "status clarification."

The phrase came from a clerk with kind eyes and a knife at his belt, which was becoming a pattern Mara disliked. He explained that Khar Veyl recognized testimony from the dead under three categories: ancestral retained, oath-anchored civic, and hostile remnant. None neatly covered Edrin Vale and the other Orrowen dead traveling under canvas through a living under-realm.

"Then make a fourth," Mara said.

The clerk looked genuinely pained. "Categories cannot be made at reception."

Edrin's painted face remained calm. "I have been executed by governments with more imagination."

Kesh made a small appreciative sound.

They had been brought to a side hall near the guest house. It was beautiful in Khar Veyl's stern way: black stone benches, blue root-fire, a basin of still water where names could be spoken and shown as ripples. Three Veyra wardens waited beside the basin with record chains coiled over their arms. Not shackles, they said. Anchors.

Mara heard Mordane in the correction.

So did Caldus. His staff tapped once on the floor.

Brakka stepped between the wardens and the dead. "No chain before vow."

"Anchor," the clerk corrected.

"No polite chain before vow."

Edrin lifted one stiff hand. "I will answer status questions."

"You do not have to," Mara said.

"I know. That is why the answer matters."

He approached the basin. The first warden asked his name. He gave it. The water rippled and showed a city Mara did not know: pale towers under a black sky, banners hanging in no wind, people in layered robes walking beside canals of bone-white water. Orrowen before death, perhaps. Or after. With the dead, sequence was increasingly negotiable.

"Civic affiliation?" the clerk asked.

"Orrowen, Third Civic District, archive license provisional, tax delinquent in two regimes due to execution."

The clerk's quill hesitated.

"Write it," Edrin said.

The quill wrote.

One of the other named dead, a woman called Sava Rennet, stepped forward next. She had spoken little since the road camp. Now she touched the basin and said, "I do not remember my district. I remember a blue door, my wife's hands, and being told my memory was insufficient for personhood. If that is not enough here either, say so plainly."

The basin stayed still.

The clerk swallowed. "Insufficient for classification. Not for personhood."

Sava closed her dead eyes.

Mara felt the whole side hall balance on that distinction.

The warden with the chains lowered them.

"Provisional person-standing," the clerk said, and wrote before anyone could advise him not to.

Brakka grunted. "Good small law."

When they left, the clerk looked terrified by what he had done. Mara understood. There were revolutions quieter than bells. Sometimes a terrified clerk wrote a category that made cruelty work harder next time.

At the guest house door, Edrin paused beside Mara. "You argued before I chose."

"I know."

"Do not become so eager to defend the dead that you speak over us."

The rebuke landed clean.

Mara bowed her head. "Witnessed."

Edrin's mouth twitched. "Good. You are educable."

Inside, the banquet summons waited.

Mara picked it up with Edrin's correction still burning in her face. Every realm taught her the same lesson in different architecture: witness was not rescue if it stole the answer first.
""",
    14: r"""The banquet's fourth course was negotiation.

No plates arrived. Instead, under-market brokers crossed the hall carrying small lacquer boxes, each box containing an offer that had been written before the speaker knew whether conscience would survive dinner. One came to Tavi: Brassroot safe conduct in exchange for exclusive review of her waking maps. One came to Saelith: passage for three Pale Bough dissenters if she would publicly state that Serathiel's decree was fear, not malice. One came to Brakka: Seven Arches recognition of under-road toll rights if she would declare the lower passes neutral.

Kesh received six boxes.

"Popular," Mara said.

"Vultures admire a colleague."

He opened none of them at first. Then one began ticking.

Tavi leaned over. "That is either a timer or a beetle."

"In under-markets, overlap is traditional."

The box opened by itself. Inside lay a coin moth with black wings and one tiny strip of contract paper: Deliver Mara Venn's route choice before dawn. Payment: cancellation of fever-road debt record.

Kesh's face emptied.

The broker with coin moth sleeves watched from across the hall.

Mara reached for the paper. Kesh closed the box before she touched it.

"No," he said.

"Kesh."

"No. If I show you the exact shape, part of me gets to pretend refusal is performance."

The lamps stayed blue.

He stood, box in hand, and walked to the center of the hall. The room quieted because commerce disliked public suicide but respected spectacle.

"I reject this bargain," Kesh said.

The broker smiled. "You have not stated terms."

"I reject the part of me that wanted to read them twice."

Blue lamps brightened.

"Debt remains," the broker said.

"Yes."

"Fever-road record remains."

"Yes."

"Your road-name remains compromised."

Kesh's jaw worked. "Yes."

Mara understood then why this was his worst bargain: not because he lost something, but because he refused the deal that would have let him call himself clean without becoming clean.

The coin moth fluttered out of the box and settled on his wrist. Its wings turned from black to dull gray, marking unpaid refusal.

Kesh looked at it with naked hatred.

Brakka leaned toward him. "Good ugly mark."

"Everyone keeps complimenting my consequences."

"You choose better ones lately."

He returned to the table and sat down too carefully.

Mara did not thank him. Thanking would have made it hers. She touched two fingers to the table between them instead. A road sign, perhaps. She was learning to let gestures carry less ownership.

Kesh looked at her fingers, then away.

"Invoice later," he said, voice rough.

Above them, Maelin's empty chair laughed softly. "Oh, he is delightful. Keep that one."

"I am not inventory," Kesh said.

Every lamp stayed blue.
""",
    15: r"""They were halfway to the boats when the hardliners tried to make the archive unnecessary.

The attack came without a speech, which Mara almost respected. Three blade-scholars stepped from the dock shadows as Vaura assigned boats. Their robes bore no house mark, only the closed-eye seal of emergency silence. One threw a black glass bead into the water. Another drew a short blade and cut the bead's reflection instead of the bead.

The lake rose in the shape of a wall.

Not water only. Memory water. Its surface showed a hundred possible disasters: Serathiel's army burning in under-roads, Khar Veyl children under white roots, the dragon-moon opening, Orrowen dead marching in borrowed armor, Mara with her hands full of blue fire while everyone she loved knelt because she had finally become useful enough to terrify the world.

For a breath, everyone saw the ending they feared most.

That was all the attackers needed.

One lunged for Maelin.

Ilyr intercepted so fast Mara saw only the afterimage of his blade. Steel rang. Maelin ducked, swore at both of them, and kicked the attacker in the knee with excellent practicality. Caldus shoved Siven behind a mooring post. Tavi dropped flat and rolled under a dock chain, already pulling wire. Kesh threw a knife at the reflection of the second attacker, and the man cursed as his real sleeve pinned itself to his own shadow.

"I love learning local mechanics," Kesh said, slightly hysterical.

The third attacker came for Mara.

Not to kill her. She saw the restraint in the blade angle. Capture, then leverage. Hazard, saint, witness, hostage. The names changed. The hand reaching for her did not.

Mara reached for the cinder and stopped.

The memory wall still showed her burning everyone into obedience. It wanted an answer. It wanted proof.

No.

She grabbed the nearest archive pole instead and swung low the way Joryn had taught her for mine rats and men who thought smaller people only struck upward. The pole cracked across the attacker's ankle. Brakka's maul hit the dock beside him, close enough to drop him from fear and physics.

"Alive," Caldus called.

"Annoyingly," Brakka confirmed.

The memory wall surged higher. Saelith stepped toward it and sang one flawed note from the counter-hymn, not to soothe, not to command, but to interrupt the rhythm of fear. The visions blurred. In them, the terrible Mara became several Maras: afraid, angry, muddy, scarred, undecided, not yet surrendered to any one future.

Mara added her voice, not song, just names.

"Joryn. Dilla. Niv. Arveth. Sella Brin. Liora. Edrin Vale. Pell and Haden. Maelin Noct-Vey."

The wall fell back into the lake.

Vaura stood over the captured attackers with a knife in hand and a mother's fury she would probably later document as civic necessity.

"Who ordered this?" she asked.

The first attacker spat blood. "No one. That is why it was clean."

"Nothing done in fear is clean," Maelin said.

The attacker's eyes flicked to her retention marks. "You should have stayed indexed."

Maelin smiled. "You should have stretched before treason."

Kesh made an involuntary sound of admiration.

Vaura ordered the attackers bound by their own shadows and sent under guard to the Seat. Then she looked at Mara.

"The archive is now more urgent."

"Because they tried to stop us?"

"Because they thought stopping us would be easier than surviving what we read."

The boats waited. The black water had gone smooth again, pretending it had not just worn everyone's fear as a face.

Mara stepped in with wet boots and a shaking hand.

Under the lake, pale pages turned.
""",
}


FINAL_DEEPENING: dict[int, str] = {
    15: r"""The crossing to the drowned archive was not long. It only felt like entering another book of the dead.

The boats moved without wake. Veyra canal craft, Maelin said, were built to disturb neither water nor memory unless the rower intended to start a lawsuit. The oars dipped through reflections of the cavern ceiling and brought up strings of pale weed. Every stroke revealed pages below the surface: scraps of luminous bark, black parchment, thin sheets of beaten silver, tablets sealed in glass, all drifting in slow circles around the archive towers.

Archive crabs surfaced near the first boat.

Kesh had expected something small enough to mock. These were broad as shields, their shells layered with scraps of writing held under translucent mineral. They moved sideways over the water as if the lake had forgotten to tell them sinking was customary. One climbed the side of Mara's boat and held up a claw tipped with a fragment of white root-paper.

Tavi leaned close. "Is it offering or threatening?"

"Archive crabs collect loosened text," Maelin said. "If it offers a scrap, it believes the scrap is looking for its argument."

"That is not an answer."

"It is Khar Veyl. You will get used to it or develop a facial twitch."

Mara took the scrap.

The writing was water-blurred but legible in two inks, one pale, one black:

...seal to be divided so no single court may command the dream...

Below it, in a different hand:

...division to be taught as moral necessity, not mutual fear...

Saelith read over Mara's shoulder and went utterly still.

Ilyr closed his eyes.

"Light and dark hands on the same page," Mara said.

Maelin nodded. "Before the story split them into clean enemies."

The archive crab clicked its claws twice, then scuttled back into the water with the dignity of a librarian who had completed a difficult transaction.

Behind them, the dock shrank. Vaura stood there with Siven, the captured hardliners, and half a dozen guards. From this distance she looked less like a judge and more like a mother who had built herself out of law because flesh had proved too easy to wound. Siven held Mara's torn banner scrap in both hands.

In the second boat, Edrin Vale reached into the water.

"Careful," Caldus said.

"I am dead, not careless."

Edrin touched a floating page. The page lit under his fingers. His painted face changed.

"This is Orrowen court script," he said.

Maelin turned sharply. "That should not be in this ring."

"It is a tax record." Edrin's voice thinned. "Third Civic District. Grain levy, moonward emergency. My district paid into the seal project."

"Orrowen funded the dragon-moon burial?" Tavi asked.

"Or was made to," Ilyr said.

The water under both boats darkened.

Mara heard the pulse again. Not loud. Not even close. But the lake seemed to lean toward Edrin's hand, toward the Orrowen page, toward the fact that the dead city below them was not merely a consequence of elven history. It had been involved, used, taxed, erased, perhaps punished for knowing too much. The world widened in the worst way. More people implicated meant more people had been silenced. More guilt meant more witnesses.

Edrin held the page to his chest. "I request this record be included under my provisional standing."

Maelin looked at him, then at Mara. "He learns quickly."

"The dead have had time," Edrin said.

The first archive tower loomed overhead.

It descended from the cavern roof into the lake, its upper levels dry and lit, lower windows drowned in black water. Chains held it steady. Fungal stars clung to its sides. At the waterline, a circular door opened and closed with the rhythm of a slow breath. Each time it opened, Mara glimpsed stairs going down beneath the lake.

No one spoke as the boats approached.

There were moments when even Kesh knew words would only make fear feel crowded.

The door opened.

Cold air poured out, smelling of salt, old ink, and glass.

Mara tucked the scrap from the archive crab beside Liora's vial, Maelin's warning, and the torn banner cloth. So many small things. So many records that should not have had to survive in pockets.

The boat slid into the archive mouth.

Above them, armies moved.

Below them, history waited wet and awake.
""",
}


THRESHOLD_DEEPENING: dict[int, str] = {
    15: r"""Inside the archive mouth, sound changed allegiance.

The lake noise fell behind them. Ahead, every drip became a word almost spoken. The boats slid into a round receiving chamber where the walls were lined with shelves disappearing below black water. Some shelves held sealed tablets. Some held jars of ink with labels floating inside the glass. Some held nothing but the darker rectangles where records had been removed and never returned.

Tavi lifted her lantern.

The light bent downward.

"That is not good optics," she whispered.

"The archive teaches attention to descend," Maelin said.

"It could do that with stairs and less menace."

At the center of the chamber stood a desk half-submerged in water. Behind it sat an undead clerk.

Not named by paint like Arveth had been. Not command-bound like Mordane's dead. This clerk wore a dark robe sealed in wax at the seams, and his skull showed through skin gone translucent with long soaking. Tiny archive crabs moved across his shoulders, rearranging scraps on his collar. When the boats bumped the receiving rail, he opened eyes filmed with silver.

"Purpose," he said.

Edrin bowed before anyone else could decide whether to. "Mixed witness party seeking the shared ledger of the dragon-moon burial, light and dark entries, Orrowen tax appendices, and any correction filed by the dead."

The clerk considered. Water dripped from his chin.

"Standing?"

Edrin held up his provisional strip from the Khar Veyl correction board. It had become damp in his hand, but the ink held.

The clerk read it.

Then he looked at Mara, at Saelith, at Ilyr, at Maelin, at Tavi's lantern, at Kesh trying not to touch anything valuable, at Brakka who filled the doorway like a patient landslide, at Caldus with staff ready and eyes tired.

"Insufficient," the clerk said.

Mara's heart sank.

Then the clerk reached under the water and produced a stamp the size of a brick. He pressed it onto Edrin's strip. The sound echoed through the chamber like a door unlocking.

"Expanded standing pending drowning."

Kesh raised one hand. "I object to the final clause."

"Noted nowhere," the clerk said.

Mara almost smiled. The archive had a sense of humor. Terrible sign.

The clerk stamped three more slips and handed them to Sava, the other named dead, and Mara. Hers read: Surface cinder-singer, disruptive witness, provisional reader under objection from all relevant traditions.

"That is the most accurate title I have received," she said.

The clerk's silver eyes shifted. "Do not enjoy titles."

"I am trying not to."

"Try better below."

Behind the desk, the submerged shelves groaned. A stair surfaced from the water one step at a time, each black tread shedding streams as it rose. On the first step lay a white petal from Lumenorath. On the second, a strip of black under-script. On the third, a scale no larger than Mara's thumbnail, pale and curved like a piece of moon.

The cinder cage at her hip went cold.

Not quiet.

Cold.

The clerk folded his hands over the flooded desk. "Shared ledger rests under breath line. Readers will encounter beneficial lies first. Do not keep what comforts you."

Saelith swallowed. Ilyr looked at Maelin. Maelin looked delighted in the way people looked when terror confirmed their thesis. Tavi muttered a note to herself and then crossed it out.

Caldus stepped onto the first stair. "Order?"

Brakka answered, "Witnesses. Then those who keep witnesses from drowning."

"That includes everyone."

"Good road."

Mara put one foot on the stair. Water climbed around her boot though the step was rising. It was cold enough to ache. Under the water, something vast dreamed of an eye.

She thought of the Downward Gate, of necessary truths, of missing usefulness and fearing freedom. She thought of every court above them trying to survive by making truth smaller.

Then she stepped down.

Behind her, the undead clerk stamped one final blank strip and set it floating after them.

Mara saw the words form as the water carried it into the dark:

Corrections remain open.

For reasons she could not explain, that frightened her more than judgment. Judgment ended a sentence. Correction meant the sentence could keep finding you.

Kesh, descending behind her, read it over her shoulder and made a wounded noise.

"An archive with open-ended billing," he said. "This is how civilizations fall."

Maelin, one step below, looked back through wet silver light. "No. This is how they avoid pretending they have finished standing."

"I dislike inspirational accounting."

"Then you will suffer productively here."

Mara kept walking before the exchange could become affection in a place that might stamp it. The stair curved under the waterline. Cold climbed to her knees, then her thighs. Each step asked whether she meant to continue after the easy air ended.

She did.
""",
}


def replace_chapters(text: str) -> str:
    pattern = re.compile(r"(?m)^(?:# Part III: Khar Veyl\n\n)?## Chapter (\d+): .*$")
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
        if chapter_no in DEEPENING:
            replacement += "\n\n" + DEEPENING[chapter_no].strip()
        if chapter_no in FURTHER_DEEPENING:
            replacement += "\n\n" + FURTHER_DEEPENING[chapter_no].strip()
        if chapter_no in FINAL_DEEPENING:
            replacement += "\n\n" + FINAL_DEEPENING[chapter_no].strip()
        if chapter_no in THRESHOLD_DEEPENING:
            replacement += "\n\n" + THRESHOLD_DEEPENING[chapter_no].strip()
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
        'current_form: "full-length draft zero with Book Two chapters 1-15 revised in pass 01"',
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
    print(f"Book Two chapters 13-15 revised. Word count: {total}")


if __name__ == "__main__":
    main()
