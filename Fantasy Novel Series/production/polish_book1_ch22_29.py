#!/usr/bin/env python3
"""Revision pass 01e for Book One chapters 22-29.

Replaces the first half of the finale with bespoke prose: Ashgate's quiet
uprising, the royal foundry descent, tactical mirror, Joryn's chain, Mordane's
arithmetic, the dead refusing command, Tavi's cinderbreak, and the coronation
catastrophe that launches the city battle.
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
    22: r"""## Chapter 22: Ashgate Rises Quietly

Kell Ashgate did not rise with banners.

It rose with soup.

Dilla's tallow shop gave out the first bowls before dawn, onion-thin and peppered hard enough to make the eyes water. The line looked harmless from the street: miners coming off night shift, widows with shawls pulled over ash-gray hair, children holding tin cups, two old men arguing about whether turnips counted as food or surrender. Royal patrols passed twice and saw hunger arranged in an ordinary shape. They did not see the paper sealed under the bread heel in each bowl. They did not see the work tokens changing hands under sleeves. They did not see Rella standing on a crate behind the stall, sorting names by district with the grim authority of a child who had been told too often to wait outside.

Mara saw all of it from the alley mouth and felt afraid in a new way.

Fear before had been a fist: the vent closing, a wagon leaving, a blade at her throat, Joryn's face behind bars. This was wider. This was fear with rooms in it. If she gave the wrong order, people she had never met would suffer for trusting her. If she hesitated too long, they would suffer for having trusted too late.

Kesh stood beside her, hood up, pretending not to be moved by organized soup. "I have seen worse rebellions."

"Is that supposed to help?"

"No. It is a professional observation. Better rebellions have breakfast."

Othen Brask came down the alley with two heatwork crew chiefs and a rolled map under his arm. He had washed the grease from his face badly, which meant he had tried. The burn scars along his throat pulled when he spoke.

"Bellweather Lane is holding," he said. "Saelith's hospice pipe stays warm if we shift load from the palace laundry for two hours."

"Will they notice?"

"The palace laundry?"

"Yes."

"Their towels will become civic participants."

Tavi, crouched over a gutter valve with three tools in her mouth, raised one finger in approval. "The foundation of democracy."

Mara looked toward Bellweather Lane. She had gone there first, as promised. Six patients lay in a hospice that smelled of rosemary, boiled linen, and fear. One old woman had caught Mara's sleeve and asked whether the names on the wall were true. Mara had said yes. The old woman had shut her eyes, whispered her son's name, and then told Mara to stop blocking the stove.

That was how rebellion kept happening. Not in speeches. In people deciding that grief did not excuse poor traffic management.

The plan for the north foundry spread in pieces because no single mouth could safely carry it.

Goblin runners took the road messages. Troll masons carried stone promises carved so small they looked like prayer beads. Heatworkers moved valve codes through shift whistles. Miners sent work tokens back to their families with scratches that meant stay home, gather, hide tools, bring water, keep children low. Dilla's soup line moved names under bread. Niv ran messages until Mara threatened to tie him to a chimney, at which point he demanded whether she meant a warm chimney or a dead one.

"Warm," she said.

"Then I accept the risk."

"You do not accept anything. You stay with Rella."

Rella looked up from her token piles. "No, thank you."

Mara stared at her.

The girl did not blink. "He miscounts when excited."

Niv made a wounded sound.

Joryn would have laughed.

The thought struck so hard Mara had to turn away. The north foundry road rose beyond the soot roofs, hidden by morning fog and the mountain's black shoulder. Somewhere under that road, Joryn was held near the command manifold because Mordane understood leverage with the intimacy of a man who mistook it for wisdom.

Caldus came to stand beside her. "The first rule of a hostage is that the captor wants you to narrow your world to one person."

"That sounds like knight schooling."

"It is older than knights."

"Does the second rule tell me how not to hate you for saying it?"

"No."

She glanced at him. He did not look sorry. That helped more than softness would have.

"What is the second rule?"

"Make the hostage's life depend on more people than the captor can control."

Below them, Dilla poured another bowl of soup. A miner with one eye took it, found the folded paper under the crust, read three names, and passed the bowl to the woman behind him before the patrol turned.

"We are doing that," Mara said.

"Yes."

"It does not feel like enough."

"It never does before the door opens."

Ilyr arrived by dropping from the roof without dislodging a single tile. Kesh, who had been standing in that tile's shadow, flinched and pretended he had not.

"I dislike your ankles," Kesh said.

"They are private."

"They are tactical insults."

Ilyr held out a strip of black paper. "Khar Veyl received Maelin's line."

Mara took the paper. The script changed when she looked at it, not into Common, but into intent: acknowledged, disputed, dangerous, coming.

"Coming here?"

"Eventually. Not soon enough to save anyone today."

"Then why tell me?"

"Because Mordane is no longer the only distant power making calculations about you."

Saelith heard that from the hospice door. Her white cloak had been traded for a gray shawl, but even disguised, she looked like a hymn trying to pass as laundry. Exhaustion had made her less perfect and more difficult to hate.

"The Pale Bough will move faster," she said.

"For me?"

"For what they believe you are."

Mara folded the black paper. "I am busy being a problem."

"That will not protect you from reverence."

"It may protect reverence from me."

Saelith almost smiled, then did not. "Saint-General Serathiel will call the broadsides proof that you have entered public witness. Under old law, she can demand custody for instruction."

"She can stand in line."

"She commands armies."

"Does she eat soup?"

Saelith blinked.

"Everyone who wants me as symbol, weapon, saint, spark, or official inconvenience can wait until the people in this city do not freeze and my brother is not chained under a furnace."

The old repetition of unwanted names passed through Mara's mind, but this time it did not close around her throat. It was not enough to say what she was not. Today she had to be something useful without becoming only use.

Arveth joined them with the original ledger wrapped in oilskin and tied to his chest. "The names are ready."

"For what?"

"To be read where command can hear them."

Behind Dilla's shop, Brakka stood in the yard with three troll masons and a row of stones no larger than apples. Each stone held a carved vow. The masons passed them from hand to hand, humming so low the mud trembled.

Mara crouched beside the stones. The marks looked simple until she tried to follow them. Then they became roads, bridges, weights, promises bending under weather but not breaking.

"What do they say?"

Brakka touched the first stone. "This road carries living feet by consent."

The second. "This wall shelters the named before the crowned."

The third. "This bridge may move if its vow is held by many hands."

Tavi looked up from the gutter valve. "That last one is either illegal or very exciting."

"Both," Brakka said.

"Excellent."

Mara understood only part of it, but the cinder at her hip warmed. Oaths were infrastructure. If enough people carried the same vow through a city built on cinder heat, roads and walls might answer differently. Not miracles. Not obedience. Permission.

The first test came before noon.

A royal patrol found the east wall broadside and tore it down. A second replaced it while the soldiers were still crumpling the paper. The captain struck the second man with a baton. Three miners stepped forward. No weapons raised, only bodies placed inconveniently in the path of power. The captain lifted his baton again.

Caldus walked into the street.

He did not draw his sword. That made the patrol more uncertain than steel would have. A disgraced knight with a scraped shield was an easier story than a man choosing where to stand after disgrace had failed to kill him.

"Stand aside," the captain ordered.

Caldus looked past him at the miners. "No."

"You have no rank here."

"Good."

The captain hesitated. The soldiers behind him knew Caldus's face from old posters or barracks rumor. Mara saw the hesitation ripple. A system changed first when its servants hesitated, Arveth had said. She had not believed how visible it would be.

Then a bell rang from the north road.

Not an alarm. A work bell. Three short, one long, two short. Shift change.

Othen went very still. "That is early."

"Trap?" Kesh asked.

"Worse," Othen said. "Opportunity."

The foundry was calling in extra heat crews before Mordane locked the city fully. If their people entered now, disguised as shift labor and emergency maintenance, they could reach the lower manifold. If they waited, the gates would seal.

Mara looked at the soup line, the broadside wall, the hospice, the children sorting tokens, the miners holding the street, the knight without rank, the light-elf whose law was hunting her, the dark-elf whose people were waking at the edge of the map, the goblin with knives under every joke, the gnome with a half-open valve and too much guilt, the troll with vow-stones in her hands, the dead witness carrying names.

"We go," she said.

No one asked whether she meant all of them.

Dilla shoved a wrapped parcel into Mara's hands as she passed. "Food."

"I am not hungry."

"That was not a question. Heroics make people stupid about lunch."

Niv thrust a work token at her. "This one is mine."

"You are not dead."

"Good. Then bring it back."

Mara closed her fingers around the token.

Rella held up a slate with three words written in careful chalk: Do not vanish.

Mara had no answer large enough, so she gave the smallest true one.

"I will try."

They left Kell Ashgate as a maintenance crew: Othen with his map, Tavi with a tool chest large enough to hide crimes, Kesh with forged papers, Saelith with hospice authorization, Caldus with a dented heat guard helm under one arm, Ilyr beneath a shadowed hood, Brakka walking as if no gate had ever been brave enough to stop her, and Mara in an ash-worker coat with Niv's token hidden in her sleeve.

Arveth came last, because the dead were still hardest to disguise.

At the north road checkpoint, Kesh found the first lie in the mud: royal seal-wax mixed with lamp oil, smeared where a hidden cart had passed.

"Living prisoners," he said softly. "Moved recently."

Mara looked toward the foundry gate. It rose from the mountainside like a furnace pretending to be a fortress, all black iron ribs and white chapel banners and clean royal seals hammered over older maker marks.

The work bell rang again.

This time, under it, Mara heard Joryn's chain answer.

Not with words. With weight.

"We enter as maintenance," Othen said.

Mara pulled her cap low. "No."

Everyone looked at her.

"We enter as witnesses pretending to be maintenance."

Kesh grinned. "Much more expensive."

The gate opened.

Heat breathed out, and the rebellion walked in quietly.""",
    23: r"""## Chapter 23: The Engine Below

The royal foundry had three faces.

The first face was for inspectors: clean stone floors, polished brass rails, heatworkers in gray coats, chapel attendants with white cuffs, royal clerks behind glass windows entering numbers with dry quills. It smelled of oil, metal, warmed bread from the staff kitchen, and order. A visitor could stand in the upper hall and believe, if belief was convenient, that Harrowmere's warmth came from discipline, engineering, and blessed sacrifice performed far from embarrassment.

The second face began below the first.

Othen led them through a service door marked Condensate Return. Tavi opened the lock with a tool shaped like a question mark and a muttered apology to the dead gnome who had designed something better before the crown simplified it. The door shut behind them, and the clean foundry ended.

Below, the engine breathed.

Furnaces lined a cavern large enough to swallow Kell Ashgate's market quarter. Not ordinary furnaces. These were vertical mouths built into the mountain, each ringed with white-thread command hooks and black glass gauges. Corpse-rails ran between them on overhead tracks. Carts moved along those rails with bodies standing inside, wrists looped through iron, heads bowed, feet strapped to sliding plates that forced them into work even when balance failed. Some bodies shoveled ash. Some carried cinder bricks. Some turned crank wheels with hands worn to bone. Some stood perfectly still under brass crowns of needles while clerks on a balcony wrote down the heat produced by what remained of them.

The smell was not rot.

That was the worst of it.

The foundry smelled of hot metal, salt, old leather, and the mineral sweetness of cinder. It smelled productive. It smelled clean enough for lies.

Mara stopped on the service stair.

Arveth placed one dead hand on the rail. His fingers left gray marks in the dust. "Unnamed labor line."

Tavi whispered a word Mara did not know. It sounded like a curse with ancestors in it.

Below, a dead man on the nearest rail turned a crank in perfect rhythm. A hook in his throat glowed with command script. Beside the hook hung a brass plate stamped with a number.

No name.

"Do not look at all of them at once," Caldus said.

Mara's voice came thin. "How do you know that?"

"Because you will try to save all of them at once."

"Should I not?"

"Yes. And not that way."

The answer was impossible and therefore probably true.

Kesh checked the forged papers again. "We have eleven minutes before someone asks why Condensate Return needs a troll."

Brakka looked down at the foundry floor. "It needs one."

"My point, but with paperwork."

Othen unfolded his map against the wall. Sweat shone on his scarred neck. "We reach the lower manifold by crossing three production wings. First wing is corpse-rail. Second is oath hooks. Third is regulator glass. Command manifold sits under the coronation feed. Joryn should be near there if the living tag is pending."

"Should," Mara said.

"If Mordane wants you, he keeps bait near the place he wants you to break."

Saelith flinched at bait. Mara saw it and did not spare her.

"Can you sense his binding?"

Saelith closed her eyes. Pale light moved under her lashes. "Faintly. North and down. The paired tag is not complete."

Not complete. Not yet. The words became a rope again.

Ilyr studied the clerks on the glass balcony. "Surveillance mirrors in every corner. Royal, chapel, and something older under both."

Tavi followed his gaze. "Black glass. Memory reflector. It records formations and repeats them where needed."

"A tactical mirror," Ilyr said.

"That was my next unhappy phrase."

Arveth looked at the unnamed dead. "The first production line must be interrupted. If we pass through without changing anything, the foundry's command rhythm will reinforce behind us."

"And if we interrupt it?" Kesh asked.

"The floor notices."

"I had hoped for a different noun."

Mara descended the stairs.

The first wing was not a battlefield until they made it one. At first, they moved like workers: heads down, tools visible, boots in rhythm with the shift bell. Othen nodded to two heatworkers at a pressure wheel. One looked away deliberately. The other tapped the wheel twice, paused, twice again. Names coming. Mara felt Brakka hear the code even before the troll answered with one knuckle against the stone.

A chapel attendant approached with a ledger board. "Authorization?"

Kesh flowed forward, all offended efficiency. "Emergency condensate irregularity under north return, palace laundry secondary draw, hospice priority override, and if you make me read the entire form aloud, the lower tenements will smell like boiled socks by noon."

The attendant blinked. "The palace laundry is not under lower tenement priority."

"It is now. New temporary emergency humility order."

"I have not heard of that."

"Naturally. Humility is often delayed."

Tavi coughed into her hand hard enough to hide a laugh. The attendant frowned, then looked toward Brakka.

"Why is there a troll?"

Brakka leaned down. "Condensate."

The attendant decided paperwork might not require perfect understanding. He stamped Kesh's forged sheet and moved on.

They reached the first command hook.

The dead worker under it had once been a woman broad through the shoulders, with miner's scars across both palms. Her brass plate read 7-19-Gray. The hook in her throat pulsed each time the overhead rail lurched. Her body shoveled ash from a conveyor into a furnace mouth. The motion was clean, efficient, endless.

Arveth stood before her.

"We need her name," Mara said.

He studied the plate, the scars, the stitch pattern at her collar, the shape of the old company brand on her sleeve. "Not from the plate."

Tavi opened a side panel beneath the hook. Inside, gears turned around a strip of white cloth blackened by ash.

"The name is not stored here," she said. "It has been stripped out. The hook works better because the body cannot remember what to refuse."

Mara felt sick.

"Can you break it?"

"Yes. Quietly, no."

"Then not yet."

Caldus looked at her.

"If we break one hook and trigger an alarm before the manifold, we lose Joryn and the heat transfer," Mara said. Saying it felt like swallowing glass. "We need another way."

Arveth nodded. "Witness first. Break after."

They began gathering names.

Not all. Not enough. But more than the foundry expected anyone to attempt while walking through it alive. Kesh moved along the rail stealing brass plate rubbings with wax and cloth. Ilyr shadow-read the black glass for where bodies had been received. Tavi copied hook patterns and maker marks. Saelith, pale and shaking, read chapel hymn residue from the white threads and whispered where each transport had been blessed. Brakka marked the floor with tiny vow-stones no larger than teeth. Caldus placed himself between the party and every clerkly glance that lingered too long.

Mara listened.

At first the foundry was only noise: chains, wheels, furnace breath, clerks calling numbers, dead feet dragging in command rhythm. Then names began to surface under the numbers. Not full names. Fragments. A laugh caught in ash. A child's word for father. A kitchen song. The way a woman had hated carrots. The smell of soap from someone who had washed before being taken because dignity was a habit even terror could not steal.

Mara did not command the dead.

She remembered toward them.

The first dead worker faltered.

Only once. Her shovel struck the furnace lip instead of the ash trough. A clerk looked up.

Caldus dropped a tool crate.

It burst open across the floor with a crash loud enough to make five workers and three attendants turn. Tools skittered under carts. Kesh began swearing in three languages about inventory liability. Tavi fell to her knees to collect parts and, in the process, removed a command pin from the rail junction.

The dead woman's next shovel stroke missed again.

This time Mara caught the whisper under it.

Lysa.

She turned to Arveth.

"Lysa Mar," he said, voice rough. "From the archive."

Mara whispered the name.

The hook in Lysa's throat flickered.

Not free. Not yet. But the command rhythm stumbled, and every overhead rail in the first wing clicked one tooth out of time.

Othen's eyes widened. "That gives us a window."

"How long?"

"A minute if the foundry is lazy. Twenty seconds if it is well managed."

"It is evil, not lazy," Kesh said.

"Then move."

They crossed the wing as the corpse-rails stuttered above them. A dead man dropped a cinder brick. Another turned his head a fraction toward Mara. A third whispered through torn lips, not a name but the shape of wanting one.

At the far gate, two royal guards barred the service corridor.

"Maintenance halt," one said.

Ilyr stepped into the guard's shadow and came out behind him. Kesh threw a stamped form at the second guard's face. Caldus caught the first man's baton on his shield, shoved him into the wall, and did not strike again when the guard went down. Saelith touched the second guard's wrist before he could shout. Pale light sealed his voice, then loosened at once when Mara looked at her.

"Temporary," Saelith said.

"Consent?"

"No. Necessity."

"Remember the difference."

Saelith's face tightened, but she nodded.

Beyond the gate, the second wing descended through a forest of hooks.

Oath hooks hung from chains at every height, hundreds of them, white and black and brass, each baited with a different command. Some were made for the dead. Some were made for soldiers. Some were made for workers who had sworn employment contracts under hunger. The air itself felt barbed.

Brakka stopped at the threshold.

Her tusk rings trembled.

"This room lies about vows," she said.

The floor behind them rang as the production wing alarm finally caught up.

The corpse-rails began moving faster.

Arveth looked back once at Lysa Mar, still shoveling, still faltering on every third stroke.

"She heard," Mara said.

"Yes."

"Will that help her?"

"If we survive long enough to make hearing matter."

The second wing gate opened with a sound like a throat clearing before judgment.

Mara stepped inside, carrying stolen names against her ribs while the hooks above her swung gently, searching for promises to use.""",
    24: r"""## Chapter 24: The Tactical Mirror

The oath-hook wing wanted them to mean well.

That was its first cruelty.

The hooks did not lash out like traps in stories. They waited, bright and patient, each one dangling from a chain etched with promises: protect the weak, obey lawful command, preserve civic warmth, repay debt, honor mercy, keep the road, guard the named, save blood of your blood. True words, most of them. Good words. Words that had fed people, sheltered them, steadied them in grief.

In this room, every good word had been sharpened.

Caldus crossed the threshold and one hook swung toward his throat. Not fast. Not violently. Like a friend offering a necklace.

Kesh caught his sleeve. "No."

Caldus had gone pale. "It says hold the line."

"It says die where someone else points."

"That is not the same."

"In this room it is."

Brakka moved in front of Caldus. The hook turned toward her instead. Its script changed, crawling across white metal: a vow may be edited by those who inherit its burden.

The troll's face hardened.

"Little hook knows old wound."

Tavi lifted her goggles and stared down the long chamber. "It reads unresolved oath-memory and offers simplified obedience. Technically brilliant. Morally landfill."

"Can we shut it down?" Mara asked.

"Everything in here is wired into the central lock. If I cut the hooks, the foundry seals. If Brakka contests them one by one, we all die of age or soldiers."

Ilyr touched the black-glass wall. Their reflections ran along it, delayed by half a second, each image carrying a faint silver thread from throat to hook.

"The room does not need to catch us," he said. "Only teach the mirror how."

At the far end stood a gate of black glass. It reflected the company not as they were, but as the foundry understood them.

Caldus was a wall without a face.

Kesh was a hand opening purses while the room burned.

Tavi was a little engine with no one near enough to stop it.

Brakka was a bridge crushed beneath those crossing it.

Saelith was white light closing around a struggling figure.

Ilyr was a knife cutting out half a truth and calling the wound secrecy.

Arveth was a ledger walking because it had forgotten how to be a man.

Mara was standing over all of them with the cinder cage open, using every name like a lever.

She hated the mirror most for not being entirely wrong.

Behind them, soldiers entered the hook wing. The first one lifted a whistle. A hook dipped and touched his shoulder. He lowered the whistle, eyes emptying into obedience, and drew his sword without haste.

"Move," Caldus said.

"Not forward," Tavi snapped. "The mirror records formation. If we do what we always do, it predicts us."

"Then we do what we do badly," Kesh said.

"That is your whole life."

"At last, recognition."

The room attacked by making them themselves.

Caldus tried to take the front. Hooks swarmed him, whispering rank, duty, shield, atone. He stumbled. Brakka shoved past him and took the blow meant for his oath. A hook struck her shoulder plate and shattered, but the vow-script crawled up her armor, trying to name her burden as road property. She laughed, low and furious.

"No bridge owns feet."

She swung her maul, not at the hooks, but at the floor. Stone buckled. Chains above lost tension. The nearest hooks sagged.

Kesh ran into the open.

"That is new and upsetting," Caldus said.

The goblin waved both arms at the soldiers. "Legal notice: anyone stabbing me accepts full responsibility for all resulting emotional damage."

Three command-bound soldiers turned after him. Kesh led them under the sagging hooks, slid on one knee, and cut two boot straps as he passed. They fell into each other. A hook meant for Caldus brushed the first soldier's neck. The man froze, then began reciting his enlistment oath in a child's voice. Saelith reached him before the next hook could sink deeper.

"Let go," she told the magic.

White light flared around her hand.

The hook resisted.

Saelith did not wrap the soldier in hymncraft. She did not command calm. She took the hook's bright order in her bare palm and let it cut her instead.

The soldier collapsed, gasping.

Mara saw blood on Saelith's hand. Real blood, red and uncertain.

"That was stupid," Mara shouted.

"I know," Saelith said, and sounded almost relieved.

Tavi reached the first control plinth. The mirror showed her older, laughing as a city drowned behind one of her inventions. She stopped so hard her boots slipped.

Mara saw it. "Tavi."

"Busy."

"It is using guilt."

"Guilt is data."

"Not all data deserves a steering wheel."

Tavi's mouth twisted. Then she closed her eyes, reached into her tool roll, and handed Mara the brass key that could open the cinder cage fully.

Mara stared. "Why are you giving me this?"

"Because my worst self keeps dangerous tools where no one can stop me. Hold it. Do not use it unless I ask and you disagree."

Trust was sometimes heavier than suspicion. Mara took the key.

The mirror flickered.

Ilyr moved next. Instead of vanishing into shadow, he stepped into the brightest line of foundry light. Every mirror caught him. Every hidden surveillance plate saw his face.

"Ilyr," Arveth warned.

"No more half-truth."

He cut his palm and pressed blood to the black glass. Dark-elf script spread from the mark, not concealing but revealing. For a moment the whole chamber showed what the foundry had recorded and buried: living prisoners under chapel cloth, workers signing silence oaths with winter at their backs, dead bodies receiving numbers where names had been, Mordane on the observation balcony practicing sorrow before a speech.

The soldiers faltered.

The hooks hated witnesses. They swung wildly now, striking stone, armor, air.

Arveth walked through them.

A hook pierced his shoulder. He stopped, looked down at it, and sighed. "I have been commanded by better tyrants."

The hook's script lit: serve beyond death.

Arveth placed both hands around it. "No."

Not loud. Not magical in the way Mara had learned to fear. Only exact. The kind of no that had been written down, appealed, denied, buried, and then spoken anyway.

The hook cracked.

At the black-glass gate, Mara faced herself.

The reflected Mara opened the cage. Blue-white memory poured out around her like a crown. In the reflection, Caldus knelt because she needed a shield. Kesh bled because she needed a door. Tavi burned because she needed a device. Saelith vanished into light because she needed a miracle. Ilyr's secrets became weapons. Brakka's vow became a road only Mara could cross. Arveth's dead mouth spoke names until nothing of him remained.

The reflected Mara saved Joryn.

Only Joryn.

The image knew exactly where to put the knife.

Mara stepped closer.

"You could do it," the reflection said in her own voice. "Open the cage. Command the hooks. Make the dead hold the soldiers. Make the living prisoners sleep through fear. Make everyone useful for one hour, and afterward you can apologize to whoever remains."

The chamber noise fell away.

Mara thought of Mordane before she had even met him face to face: the softness of a voice that called spending people necessary, the neatness of numbers arranged so no cry could interrupt them. She had hated him enough that part of her wanted a cleaner kind of power with which to defeat him.

Clean power was the lie.

"I want my brother," Mara said.

The reflection smiled. "Yes."

"I want him more than I want most of these people alive."

The smile widened.

Mara heard Caldus inhale. Heard Saelith's small wounded sound. Heard Joryn's chain, far below, answer in weight.

"That is true," Mara said. "And it does not get to decide."

She pressed Niv's work token to the glass. Then Pell's. Then the strip of Kell Ashgate cloth. Then Tavi's brass key, held flat and unused.

"I am not less dangerous because I love people," Mara told the mirror. "I am dangerous because love can become arithmetic if I let it."

The reflected Mara lifted the cinder cage.

Mara did not.

Behind her, the party changed shape.

Caldus lowered his shield and helped a fallen soldier crawl away from a hook. Brakka guarded him while he did it. Kesh stopped running and held the attention of three hooks with a chain of false contracts, each one more insulting than the last. Tavi disabled the plinth and shouted instructions to Othen through the speaking pipe. Saelith freed another soldier by asking his name before touching the hook. Ilyr kept his blood on the glass, making hidden recordings public. Arveth stood with a hook through his shoulder and recited the names they had gathered until the chains around him trembled.

The mirror had learned their roles.

It had not learned their choices.

Black glass split from floor to ceiling.

The gate opened.

The hook wing collapsed into chaos behind them, but not defeat. Some soldiers dropped weapons. Some ran. Some still obeyed. The difference mattered. Command hated difference.

Mara passed through the broken gate last.

As she crossed, the reflection caught her eye from one remaining shard.

It did not look monstrous now.

It looked possible.

That frightened her more than if it had vanished.

Beyond the gate, the air turned colder. The corridor descended toward the conversion pens. White thread webbed the walls like frost. Somewhere ahead, living prisoners breathed in uneven rows.

And under all those breaths, one chain dragged once against stone.

Joryn.

Mara ran.""",
    25: r"""## Chapter 25: Joryn's Chain

The conversion pen had been built like a chapel hospital.

That was how Mara knew it was meant to be forgiven.

The walls were whitewashed. The beds were narrow and clean. Bowls of water stood beside each one. Lavender hung from the rafters to sweeten the air, failing against rust, sweat, fear, and the sharp mineral scent of cinder tags. At the far end, a painted panel showed a saint laying one hand on a dying worker's brow while a city glowed warm behind them.

Below the painting, twenty-seven living prisoners sat chained to iron rails.

Some were miners. Some wore hospice blankets. Two were royal soldiers with their insignia cut away. One was a goblin woman whose ears had been tied flat under a chapel scarf. A dark-elf youth lay curled around a cracked rib, eyes open and empty with practiced refusal. Every prisoner wore a white-thread loop around one wrist. Every loop ran to a central spindle beside the furnace door.

Joryn sat nearest that door.

For one second Mara saw only him.

Not the spindle, not the guards, not the priest-physician reaching for a bell pull, not the furnace timing wheel behind the glass, not the fact that the room was designed to punish exactly the movement her body wanted. Joryn. Split lip, ash in his hair, one eye swollen, shoulders still stubborn under a torn work coat. Alive.

He saw her and shook his head.

She had crossed half the room before the first chain snapped taut.

Pain struck every prisoner at once.

Joryn folded around it without making a sound. Others cried out. The goblin woman bit her own sleeve. The dark-elf youth slammed his head back against the wall. The white-thread loops brightened. The central spindle began turning.

Saelith shouted, "Stop!"

Mara stopped.

The priest-physician's hand froze near the bell pull. Caldus had reached him from the side and set a sword edge against his wrist. Ilyr cut down the first guard before the man could reach the furnace lever, not killing him but leaving him convinced the floor was safer. Kesh threw a smoke bead under the second guard's feet. Tavi ran to the spindle.

Joryn sucked in air through his teeth. "Took you long enough."

Mara laughed and nearly broke.

"You look terrible," she said.

"You brought friends."

"You said not alone."

"I meant fewer terrifying ones."

Brakka ducked through the doorway, took in the room, and growled so low the lavender shook.

"All right," Joryn said, staring. "One terrifying one is fine."

Tavi slapped a gauge. "No one move toward anyone they love."

Kesh looked around. "That is oddly specific."

"Because the spindle measures paired pressure. Every personal rescue tightens the communal chain. Whoever designed this deserves to be haunted by furniture."

Saelith stood very still. "It is a mercy-hold."

Mara turned on her. "You knew this design?"

"I knew a cleaner version. For fever wards. If one patient seized, the loop alerted healers before others were harmed."

"And this?"

Saelith looked at the prisoners. The horror on her face did not undo anything. It mattered anyway. "This turns care into leverage."

"Yes," Arveth said. "A common institutional evolution."

The priest-physician found enough courage to speak. "These people are under lawful continuance evaluation."

Caldus pressed the blade closer. "You will be quiet or briefly educational."

The man went quiet.

Mara forced herself to look away from Joryn and count the room the way Caldus had taught her: guards down, one priest, two doors, twenty-seven prisoners, central spindle, furnace timer, white-thread loops, cinder tag tray. A row of brass tags lay ready beside the spindle, each shaped like a small open mouth.

One tag had Joryn's name scratched into the back.

Not stamped. Scratched. Someone had written it secretly and badly, as if in haste.

Saelith saw Mara looking. "I did that."

Mara did not thank her.

"Can we free them?" she asked Tavi.

"Yes."

"All."

"That was included in yes, because I value my remaining teeth."

"How?"

Tavi pointed to the spindle. "We need three things at once. Saelith must loosen the hymncraft without taking control. I must reverse the pressure logic. Someone must keep the furnace cycle from advancing. And no one, absolutely no one, may yank a chain because feelings are loud."

Joryn lifted his bound hands a fraction. "Mara."

"Do not."

"Listen."

"No."

"Mara Venn."

Her full name struck harder than command. She looked at him.

He was afraid. He had always hidden fear from her as if older brothers were issued a private law against needing comfort. Now there it was, naked under bruises.

"If it comes to me or them," he said, "you know the answer."

"The answer is I find another answer."

"That is not always how the world works."

"Then the world has had lazy teachers."

The smallest smile touched his mouth, and suddenly she could not remember the sound of his childhood laugh.

The absence opened under her like a pit.

She knew he had laughed. Knew the shape of it, knew the way he covered his mouth, knew he had once laughed so hard at a foreman's wig slipping sideways that soup came out his nose. But the sound itself was gone. Not hidden. Gone for now, burned as tinder by the cinder she had used in the mirror chamber.

Mara's knees nearly gave.

Joryn saw something change. "What?"

"Nothing."

"That face has never meant nothing."

"Tavi," Mara said, voice shaking. "Tell me what to do."

Joryn closed his eyes. He understood then. Not the lost laugh, perhaps, but that she had chosen the room over running to him.

"Good," he whispered.

Tavi began the count.

"On three. Saelith, you ask the loops what they were before the corruption. Do not sing over them. Ask. Brakka, hold the rail. If it snaps, make it regret ambition. Kesh, cut the guards' belt keys and get them to Caldus. Ilyr, the furnace timer has shadow script under the chapel paint. Ruin it. Arveth, names. Mara..."

"Yes?"

"You are the pressure they expect. Be something else."

Mara walked to the center of the room, not toward Joryn. Each step made the white loops brighten. Prisoners watched her with terrible hope. She wanted to apologize to each of them for how badly she wanted to ignore them.

Instead she said, "Tell me your names."

No one answered at first.

The goblin woman did. "Rakka Fen."

Then the old miner. "Harl Brim."

A soldier. "Tesson Vair. Not sir. Not anymore."

The dark-elf youth whispered, "Siv Noct-Tal."

Names came slowly, some broken by pain, some given with suspicion, some flung like curses. Mara repeated each one. Arveth repeated them after her in a clerk's cadence, fixing them to witness. Saelith knelt by the first loop and did not command it to open. She touched the white thread as if asking forgiveness from something too small to bear the crime it had been made to commit.

"You were made to warn," she whispered. "Not punish. Remember."

The loop slackened.

Tavi swore in triumph and fear. "Again."

The furnace timer lurched. Ilyr drove a blade through the painted saint's eye, revealing black script underneath. The timer stuttered. Kesh tossed belt keys across the floor one after another. Caldus caught them, unlocked shackles, moved to the next prisoner, never rushing toward Joryn though the effort carved itself into his face.

Mara kept naming.

The spindle fought them. It tightened on love first. When Mara said Joryn Venn, the room clenched. Every loop brightened. Joryn gasped. Mara almost reached for him.

He shook his head again.

This time, she listened.

"Joryn Venn," she said again, not as brother first, but as one of the living held in a room built to make him lever and bait. "Miner. Card cheat. Bad singer. Worse liar. Mine."

The loop on his wrist loosened one thread.

"Not yours only," Arveth said gently.

Mara swallowed. "His own."

The second thread loosened.

Joryn looked at her. Something old and protective in him broke, not in defeat, but because it had been outgrown by love itself.

"My own," he said.

The spindle cracked.

Brakka seized the rail and held it together long enough for Tavi to reverse the final gear. Saelith cut her palm and fed light into the loops without closing them. Ilyr tore the shadow script free. Kesh, having run out of keys, picked the last three locks with a chapel hairpin and a look of professional offense.

The prisoners came free.

Not cleanly. Not quickly. Some could not stand. Some ran and had to be stopped before they triggered side wards. Harl Brim tried to punch the priest-physician and was allowed one controlled attempt. Rakka Fen took the man's shoes. Tesson Vair picked up a fallen baton, looked at Caldus, then threw it into the furnace.

Joryn remained seated after his chain fell away.

Mara crossed to him then. Slowly. With permission in every step.

"Can I?"

He held out his arms.

She dropped into them and became, for three breaths, no leader at all.

He smelled of sweat, ash, blood, and the sour fear he would have hidden if he could. His hands shook against her back. Her own did too. She waited for the memory of his laugh to return. It did not.

"I forgot something," she whispered.

His arms tightened. "About me?"

"Your laugh."

She felt him go still.

"For how long?"

"I do not know."

He pulled back enough to look at her. The bruise around his eye made him look half-stranger. "Then I will have to be very funny."

She made a sound between laugh and sob.

"There," he said. "Practice."

The furnace timer snapped.

Tavi spun around. "Everyone who is emotionally reunited, run."

The far door opened before any of them reached it.

Lord Cael Mordane stood beyond it in a dark coat without armor, silver hair tied back, one gloved hand resting on a ledger that floated open beside him. Behind him waited no army. Only two clerks, four command-bound dead, and the calm of a man who had arranged the room before entering it.

"Mara Venn," he said. "You have made a generous mistake."

Joryn tried to stand between them. His knees failed.

Mara caught him.

Mordane's gaze moved over the freed prisoners, the cracked spindle, Saelith's bleeding hand, Tavi's tools, Arveth's ledger, Caldus's scraped shield.

"Twenty-seven lives recovered," he said. "Very moving. Now let us calculate what you have spent to do it."

The room seemed to tilt toward him.

Mara kept one arm around Joryn and lifted her chin.

"No," she said. "Now you calculate with them in the room.""",
    26: r"""## Chapter 26: Mordane's Arithmetic

Mordane did not raise his voice.

That was one of the reasons men like him survived long enough to become history's problem. He let other people shout. He let bells ring, furnaces roar, prisoners sob, soldiers bleed, and cities panic. Then he spoke softly enough that everyone leaned toward him and mistook the leaning for respect.

"You have interrupted a conversion cycle," he said. "The north foundry feeds seventeen percent of Harrowmere's lower district warmth during winter draw, thirty-two percent of palace command reserve, and seventy-one percent of emergency infirmary response. You have freed twenty-seven unprocessed subjects and destabilized two hundred and six continuation laborers. If the manifold fails before transfer protocols complete, children in three districts begin dying before nightfall."

Harl Brim spat blood on the whitewashed floor. "Heard villains sound worse."

Mordane looked at him with mild interest. "Most villains are bad administrators."

Mara hated him then with a clarity almost calming.

The floating ledger beside him turned a page by itself. Numbers arranged in black columns. Heat output. Labor losses. Mortality projections. Cost of winter. Expected unrest. Acceptable variance.

Acceptable.

"You call people subjects because bodies is too honest," Mara said.

"I call them subjects because law requires categories."

"Law required their names too. You removed those."

"Names impair certain forms of service."

Joryn made a low sound and tried to rise again. Mara held him down. His body trembled with the effort not to become the lever Mordane wanted.

Mordane saw it. Of course he did.

"Your brother understands," he said. "He has spent years making small calculations for your safety. A skipped meal here. A lie to a foreman there. Silence when truth would cost wages. You condemn arithmetic because you dislike seeing it done at scale."

"Do not speak to him," Mara said.

"You prefer the private version? Most do. Families are allowed sacrifices. Governments are condemned for admitting they require them."

Caldus stepped forward. "Governments are condemned for stealing them."

Mordane turned his calm on him. "Sir Renn. Still looking for the one disobedience that will make all earlier obedience clean?"

Caldus went white. He did not look away.

"No," he said. "I am looking for the next person I can help."

Mordane's ledger flicked another page. "A smaller ambition. Healthier."

Saelith stood with blood drying on her palm. "The Pale Bough did not authorize living holds for foundry leverage."

"No. It authorized saint custody, emergency mercy exceptions, hymncraft restraints, posthumous continuance, and civic preservation clauses broad enough to house the architecture. Do not blame me for reading the rooms your order built."

The blow landed. Saelith's face tightened, but she did not retreat into doctrine.

"Then I will help tear them down."

"You will be disciplined by people whose beauty you still love."

"Yes."

"And then?"

"Then I will deserve the pain honestly."

For the first time, Mordane looked almost annoyed.

Tavi took advantage of it.

She rolled a brass beetle under the floating ledger. The beetle climbed the air as if it had found an invisible table, bit the ledger's spine, and exploded in a puff of green sparks. The ledger dropped three inches and recovered.

Mordane glanced at it. "Gnomish."

"Correct," Tavi said. "We put signatures on our insults."

"Your profession built half this foundry."

"My profession also invented locks. That does not make every prison my child."

"No. Only the clever ones."

Tavi flinched. Mara saw it. So did Mordane. He was not fighting them with spells first. He was assigning each of them the worst meaning of their history and waiting for shame to do what soldiers had not.

Ilyr moved into the room's shadow. Mordane looked directly at him.

"Khar Veyl sends children now?"

"Exiles," Ilyr said.

"A distinction without budgetary relevance."

"Maelin Noct-Vey."

The name changed the room more than a blade would have. One of the command-bound dead behind Mordane twitched. Arveth lifted his head sharply.

Mordane's eyes moved to Ilyr's face, then away. "Retained assets are not discussed in production areas."

Ilyr smiled without warmth. "You just discussed her."

The shadow under Mordane's ledger deepened. For one heartbeat, the hidden records Ilyr had revealed in the mirror chamber flashed across the white walls: intake lines, transfer seals, Maelin's retained mark, Joryn's pending tag, Lysa Mar's furnace draw. The freed prisoners saw. The clerks saw. One clerk dropped his pen.

Mordane sighed.

"The tragedy of witness," he said, "is that it believes seeing creates capacity."

The foundry answered him.

A bell rang deep under the floor. The conversion pen doors sealed. Overhead, the corpse-rails changed direction. The four command-bound dead behind Mordane lifted their heads. Hooks glowed in their throats.

"I do not need to win a debate," Mordane said. "I need to restore operation."

The dead attacked.

Not like monsters. Like workers whose bodies had been given tasks. One moved to seize the freed prisoners. One to the spindle. One to Mara. One to the furnace lever. Their efficiency made them horrible.

Brakka met the first with her shoulder and drove him through a row of beds without crushing him. "Name?" she shouted.

Arveth searched the dead man's collar. "No plate."

"Then we hold."

Caldus intercepted the one moving toward the prisoners. He did not strike the head or throat. He hooked his shield under the dead man's arms and pinned him against the wall while Tesson Vair and Rakka Fen dragged prisoners out of reach.

Kesh went for the clerks.

"This is not abduction," he told them while cutting the satchel from one man's belt. "This is expedited labor reclassification."

Tavi crawled under the spindle and began removing the part Mordane needed most. Sparks showered her hair. Saelith stood over her, healing nothing unless asked, blocking everything she could.

Mara faced the dead worker coming for her.

He had been young. She could see it under the command: narrow wrists, one front tooth chipped, a green thread bracelet still tied around his left hand. The hook in his throat had no plate. No number visible. No name.

The cinder cage burned at her hip.

Open me, it seemed to say, though perhaps that was only fear trying to borrow a voice.

Mordane watched from beyond the fighting. "You can stop this quickly."

Mara backed away from the dead worker's reaching hands.

"Open the cinder," he said. "Command them. Use the tool before the tool uses you."

The dead worker lunged. Mara ducked. His hand closed on her coat and tore the shoulder. He was strong with borrowed obedience. Stronger than hunger, fear, shame, and all the small human reasons a living body stopped.

Mara slammed Niv's token against the hook in his throat.

"No."

It did not break.

The worker seized her wrist.

She thought of the mirror. Of reflected Mara saving Joryn alone. Of love becoming arithmetic. Of Mordane waiting for her to prove his world true by using his methods with better intentions.

She did not open the cage.

"Tell me something," she said to the dead worker.

His grip tightened. Bones ground in her wrist.

"Anything," she gasped. "A song. A smell. A joke. Someone who hated your soup. Anything."

The hook flared. The worker's mouth opened. Command tried to turn the motion into a bite.

Instead, a sound came out.

Not a word. A whistle. Two notes, badly tuned.

From the prisoner line, Harl Brim shouted, "That is Cava's boy."

The worker froze.

Harl shoved past Caldus's shield. "Tomas! You little fool, your mother said you whistle like a kettle."

The dead worker's grip loosened.

Mara repeated it. "Tomas."

The hook cracked.

Mordane's face went still.

That was when Mara understood his arithmetic had a flaw. Not mercy. Not pity. He had accounted for grief as unrest, love as leverage, memory as fuel. He had not accounted for recognition moving sideways through a room faster than command could fall from above.

Tomas turned.

Not fully free. Not alive. But turned.

He seized the dead worker reaching for the furnace lever and dragged him back. The two command hooks screamed against each other.

Mordane lifted one hand.

The room's hooks brightened. Every freed prisoner's loop, though cut, snapped upright like snakes. White thread rose from the floor. Saelith cried out as the hymncraft recognized her blood and tried to make her its door.

"I can seal it," she said through clenched teeth.

Mara knew what seal meant in her mouth. Close around. Bind. Make safe by taking choice away.

"No."

"They will die."

"Ask them."

Saelith looked at the freed prisoners. There was no time for a vote, no orderly consent, no beautiful law. Only faces, fear, and the old question her order had answered too often without waiting.

"Will you let me hold the thread off you?" she asked.

Rakka Fen bared her teeth. "Ask faster next time. Yes."

"Yes," said Tesson Vair.

"Yes," Harl snapped. "Before we become decorative."

Yes spread through the room, ragged, frightened, real.

Saelith sang.

The hymn was not the one she had been trained to use. It broke where it should have smoothed. It left space where command wanted closure. The white threads struck her light and stopped, not trapped, but held off like rain under a roof.

Mordane's ledger flickered.

Othen's voice crackled through the speaking pipe in the wall. "Lower manifold crew in position. District valves ready in four. Maybe three if nobody cares about eyebrows."

Tavi shouted from under the spindle, "I care about eyebrows."

"Noted. Three."

Mordane heard it.

For the first time, he moved quickly. He turned toward the far door.

Ilyr was already there.

Blade drawn. Face calm. Shadow behind him full of the records Mordane had buried.

"The arithmetic is changing," Ilyr said.

Mordane looked from him to Mara, then to the freed prisoners, the faltering dead, Saelith's broken hymn, Caldus holding a line that no rank had ordered, Brakka pinning command-bound bodies without reducing them to obstacles, Kesh distributing stolen keys to people he could not profit from, Tavi dismantling the spindle that proved her own profession's shame.

"You think this is victory?" Mordane asked.

"No," Mara said. "It is addition."

The floor shook.

Deep below, the district valves began to turn.""",
    27: r"""## Chapter 27: The Dead Refuse

The district valves turned like reluctant moons.

At first nothing visible changed. That was the terror of real infrastructure. A sword swing told the room what it had done. A spell announced itself with light, smoke, pain, or at least arrogance. But valves moved in walls. Heat shifted inside pipes. Pressure climbed where no eye could follow. People trusted or died by mathematics they could not see.

Then the foundry screamed.

Every command hook in the conversion pen rang at once. The corpse-rails beyond the sealed door hammered forward, stopped, hammered again. The furnaces below dragged breath through the mountain. Somewhere in the north wing, a pressure plate burst and released steam hot enough to make the walls sweat.

Othen's voice came through the pipe. "Transfer started. Crown coil resisting."

Tavi slid out from under the spindle with grease on her cheek and a grin too wild to be reassuring. "Good. If it resisted politely, I would worry."

"Can you hold it?" Mara asked.

"Define hold."

"Tavi."

"Not alone."

The sealed door exploded inward.

Ash wights poured through on corpse-rails.

They were not the named dead Mara had seen before, not Pell with cloudy eyes remembering floodwater, not Arveth with his precise grief, not Tomas stumbling toward a whistle. These were bodies burned thin by command, skin gray and cracked, throats crowded with hooks, brass number plates nailed across collars, wrists fixed to rail braces that forced them forward in timed waves. Each carried a tool made weapon by use: shovel, ash rake, furnace hook, chain hammer.

The production line had become an army because someone had changed the work order.

Caldus lifted his shield.

Mara caught his arm. "Not just hold."

He looked at the incoming wave, then at her.

It cost him something to lower the shield a fraction. "What do you need?"

That question, from him, in that room, was its own broken oath.

"Room for names."

"Then I will buy room."

"No dying."

"That is less tactical."

"Learn."

He smiled once, grim and almost young. "Yes, Mara."

The first wave hit.

Caldus did not stand still and absorb it. He moved. Shield to redirect, sword pommel to unbalance, shoulder to turn a body away from prisoners, boot to jam a rail brace. Brakka fought beside him with even greater restraint, which was somehow more terrifying than force. She caught an ash wight by the chain harness, swung him into two others, and pinned all three under her maul without crushing a skull.

"Names!" she roared.

Arveth and Mara moved into the gap.

The first wight had a number plate half torn from his collar. Under it, a scrap of cloth remained, stitched with blue thread. Arveth read the weave. "Ashgate east laundry. Male. Forty years or more. Scar on left jaw."

Harl Brim, leaning on Joryn because neither of them should have been standing, shouted, "Mav Corren! His wife dyed blue thread on everything because he kept losing shirts."

Mara repeated it. "Mav Corren."

The wight's hammer stopped above Caldus's head.

The second wave crashed over the first.

Kesh vanished under a rail cart and came up riding it backward. "Who designed timed waves? I have complaints."

"Clerks," Tavi shouted.

"I hate being right."

He threw stolen keys into the prisoner crowd. Rakka Fen caught two and began unlocking rail braces from fallen wights while swearing at them like stubborn relatives. Tesson Vair took a furnace hook, blocked a wight's strike, and shouted for soldiers who had been prisoners five minutes ago to form on him. Some did.

Not all.

Choice made everything slower.

That was the point.

The command system wanted clean movement. Bodies forward. Tools up. Strike. Drag. Burn. Mara gave it friction: names, questions, hesitation, recognition. Each hesitation opened a dangerous space where someone living could die. Each space also proved the dead were not machinery.

Saelith stood at the center of the room with white thread burning around her hands. She had stopped singing. Now she asked. Again and again, through blood and light.

"May I hold this from you?"

"Yes."

"Name?"

"Dessa Hale."

"May I touch your wound?"

"Yes, curse you, hurry."

"Name?"

"Tomas," whispered the dead worker, kneeling beside the furnace lever.

Saelith looked at him. The old training in her face wanted to call him beyond help. The new wound in her would not let it.

"May I steady the hook?"

The dead man's mouth trembled.

"Ma," he said.

Mara understood. Not consent. Not refusal. A person reaching through a ruin for the one word still tied to living.

Saelith did not touch him.

She turned to Harl. "Do you know his mother?"

"Cava died last spring."

"Then no one here can give that leave for him."

Tomas's hook flared. Command seized the opening. His body lunged for the lever again.

Brakka caught him.

Saelith looked stricken.

Arveth stepped beside her. "The dead may not be able to consent in the forms the living prefer. That does not make consent yours to invent."

"Then what do we do?"

"Witness. Offer. Refuse to lie about the uncertainty."

The answer hurt because it did not solve enough.

Mara moved to Tomas and pressed Niv's token to the hook again. "Tomas, if any part of you wants the lever broken, fall."

The body shook.

The command hook screamed.

Tomas fell.

He dragged the lever with him.

The furnace feed for the conversion pen slammed shut.

Tavi whooped. "That counts as consent adjacent."

"Do not make doctrine," Arveth warned.

"I am making survival."

"Make it humbly."

The second wave broke against the shut feed. The rails jammed. Ash wights piled at the door, command trying to push bodies through an order the room no longer physically supported.

Mordane had vanished during the first wave.

That frightened Mara more than his presence had. He had retreated to the system. To the crown coil, the manifold, the coronation feed where numbers could become public spectacle.

Othen's voice burst through the pipe again. "Crown coil pulling back. We need the witness line at the lower hooks now or it reroutes through the palace."

"How far?" Caldus asked.

"Through the rail maze, down two furnace stairs, across the glass regulator."

Kesh stared at the corpse-rail pile. "Naturally."

Arveth picked up a fallen number plate. His dead fingers closed around it until the brass bent.

"The production line will keep sending waves unless we interrupt naming failure at source."

"Meaning?" Joryn asked.

Arveth looked toward the rail maze beyond the broken door. "The stolen names are not destroyed. They are stored to keep the bodies empty."

Mara felt the cinder answer at her hip.

"Where?"

"In the furnace index."

Tavi went still. "That is in the regulator chamber."

"Of course it is," Kesh said. "All roads lead to the thing most likely to explode."

The freed prisoners who could move began helping those who could not. Rakka Fen cut rail braces. Tesson Vair organized two former soldiers at the door. Harl Brim sat beside Tomas's fallen body and whistled two bad notes over and over, as if keeping a coal alive.

Mara looked at Joryn. "Can you walk?"

"Badly."

"Can you stay?"

He stared at her.

"The prisoners need someone they trust who is angry enough to be practical," she said. "You know mines. You know panicked people. You know me, which means you know when my plans are stupid."

"You are leaving me again."

"I am asking you to hold the room."

"That is a fancy way of leaving."

"Yes."

The honesty struck them both.

Joryn looked toward the prisoners, then toward the door through which Mordane had escaped. When he looked back, the old protective brother was there, but he was not alone in his face anymore.

"If you die, I will be furious."

"I am counting on that."

"Do not count. Mordane counts."

Mara swallowed. "Then I am witnessing it."

He caught her wrist before she could turn. "Mara."

"What?"

He smiled, deliberately ridiculous, despite the bruise, despite the pain, despite the fact that she could not remember the sound that belonged with it. Then he made an exaggerated snorting laugh so false and awful that even Rakka Fen turned to stare.

"How was that?" he asked.

The memory returned.

Not all at once. A spark first, then a sound under a table in a storm, then Joryn at twelve trying not to laugh while their mother scolded them both, then the soup-through-nose incident in glorious, disgusting detail. Mara grabbed the memory so hard it hurt.

"Terrible," she said, crying.

"Good. Come back and I will improve."

She squeezed his wrist and let go.

The next road was the rail maze.

Kesh led because every rail had a lie in it. Caldus followed, no longer front by default but ready when needed. Brakka carried two vow-stones glowing under command pressure. Tavi ran with the dismantled spindle part under one arm. Saelith came with both hands bloodied and no hymn unbroken. Ilyr moved ahead of the light. Arveth carried bent number plates like evidence from a grave.

Mara went last for three steps, looking back.

Joryn had already turned away from her. He was helping Rakka Fen lift a prisoner, shouting at Harl to stop whistling in people's ears unless he meant to kill them again by annoyance. He was alive. He was not safe. He was not hers to carry.

The third wave of ash wights struck the far door as Mara entered the rail maze.

Behind her, Tomas's body, still pinned by Brakka's broken chain, lifted one hand from the floor.

Not under command.

In refusal.

The production line stuttered across the entire foundry.""",
    28: r"""## Chapter 28: Cinderbreak

The regulator chamber was a cathedral built by people who claimed not to worship anything.

Glass tubes as wide as chimneys climbed from the floor into darkness, each filled with liquid heat that moved slowly, like honey remembering fire. Brass walkways circled them at seven levels. Gear wheels turned in the walls with teeth taller than Mara. White-thread command cables ran from tube to tube, tied into black-glass gauges and crown coil receivers. In the center of the chamber hung the furnace index: a rotating sphere of brass plates, each plate engraved with a number on the outside and a name on the inside, hidden from the body it belonged to.

The names were still there.

That nearly broke Mara more than if they had been destroyed.

Tavi stood at the threshold and made a small sound, all the jokes gone out of her.

"They inverted the registry," she said.

Arveth's face had become very still. "Explain."

"Old safety design kept name and body linked so a worker could not be moved through hazardous systems without consent record. The crown reversed it. Name stored here. Body emptied there. Command moves through the absence."

Kesh looked at the spinning sphere. "So if we give the names back?"

"The hooks lose their clean path. Dead may resist. Foundry loses labor timing. Crown coil loses reserve."

"And the city?"

Othen's voice came from a brass speaking trumpet beside the door, crackling through static. "District valves can hold warmth if the regulator does not shatter."

Everyone looked at Tavi.

She opened her tool chest.

Inside lay the cinderbreak device.

Mara had seen Tavi build pieces of it in stolen minutes: a folded tripod, glass needles wrapped in copper, a gear heart, a mirror no larger than a coin, Saelith's charged hymn-cloth, a goblin contract tooth Kesh claimed had belonged to an uncle nobody liked, troll vow dust from Brakka's stones, and a fragment of Arveth's bent number plate. It looked too small to matter and too complicated to trust.

"It was originally meant to sever command from cinder output," Tavi said. "Now it must also keep the regulator from overcorrecting, return names to bodies, prevent the district valves from cooking everyone, and avoid waking the dragon-heart below us."

"How likely is all that?" Caldus asked.

"In a just universe? Low. In this one? Insultingly possible."

Mara looked down through the grating.

Far below the glass tubes, beneath layers of brass and stone, something enormous glowed red-black. Not a furnace. Not a machine. The buried cinder under Harrowmere's crown. A dragon-heart, or part of one, vast enough that the entire foundry had been built around it like a parasite pretending to be architecture.

It was asleep.

It was also listening.

Mordane's voice entered through every speaking trumpet at once.

"Miss Quen," he said, "if you overload the regulator, you will become the finest murderer in this room."

Tavi flinched.

Mara stepped toward the trumpet.

Mordane continued. "You know this. That is why you have delayed. The foundry's crime does not make its heat imaginary. If you break what you do not yet understand, you will teach the lower districts the difference between justice and competence."

"He is in the crown coil chamber," Ilyr said. "Below the coronation feed."

"Can you reach him?" Caldus asked.

"Not before he says more useful poison."

Tavi's hands hovered over the cinderbreak device.

Mara touched her shoulder. "Talk to me."

"He is right in the way knives are right about skin."

"That is not an answer."

"My first flood engine saved Brassroot's south burrows. Then a guildmaster modified the design for siege pumps and drowned a gate town. I told myself invention was not guilt. Then I told myself guilt was not reason to stop inventing. Both were useful half-truths."

"What is the whole truth?"

Tavi looked at the device. "No tool is innocent after it works."

Mara thought of the cinder cage. Of the key in her pocket. Of her own voice becoming a tool in every room she entered.

"Then we choose what watches the tool," she said.

"Poetic. Vague."

"Us. Names. Consent where we can get it. Admission where we cannot. No command function."

Tavi stared at her.

"The command function makes the device safer."

"For whom?"

"For the operator."

"Remove it."

The chamber shook. The crown coil had begun pulling heat upward. In the glass tubes, liquid fire climbed faster. Plates on the furnace index spun until numbers blurred.

Tavi swallowed. "If I remove command, the cinderbreak cannot force the names back. It can only open the path."

"Then the dead choose."

"Some may choose fire."

Arveth spoke softly. "Some will."

"Some may choose Mordane's command because it is the only shape they remember."

"Then we witness that too," Mara said, though the words hurt.

Tavi closed her eyes, took a screwdriver from her sleeve, and removed the central command pin from the device.

The whole cinderbreak sagged in its frame.

"There," she said. "It is less safe and less monstrous. My favorite engineering category."

They went to work.

The regulator chamber became movement. Kesh climbed the lower ring to cut false-route wires and kept up a running commentary about whoever had last serviced the gears being either drunk, royal, or philosophically opposed to stairs. Brakka hammered vow-stones into the main supports, each strike making the chamber's oath-geometry less obedient to crown seals. Caldus and Ilyr held the entry bridge against command-bound guards trying to reach the device. They fought badly together at first, shield and shadow arguing without words, then better when Caldus stopped trying to protect Ilyr from risks Ilyr had already chosen and Ilyr stopped assuming every offered shield was a cage.

Saelith stood beneath the furnace index with blood on both palms.

"May I carry light where command has hidden names?" she asked the air.

No one answered.

She did not pretend they had.

"I will carry it only as far as the opening," she said. "No farther."

That was the most honest hymn Mara had heard from her.

Arveth fed number plates into the cinderbreak device one by one. Each plate rang when it touched the gear heart. Inside the spinning sphere, hidden name plates answered. Lysa Mar. Mav Corren. Tomas Vale. Dessa Hale. Pell Orwick. Essa Brant. Tollen Reed. Names they knew, names they did not, names broken by bad records, names guessed with humility and marked uncertain rather than forced clean.

Mara stood at the center and listened.

The cinder below woke by degrees.

It did not speak in a single voice. It breathed memories: wings over black seas, claws sunk into mountains, eggs under moonlight, fire given freely before fire was mined, pain when the first crowns cut dragon-hearts from bodies and called the pieces cinder. The grief was older than human law. Older than elf schism. Older than troll vows, goblin contracts, gnome engines, undead records. It did not care about Harrowmere's district valves.

That was the danger.

"Mara," Tavi shouted. "Anchor."

"How?"

"The way you keep doing impossible things without terminology."

Mara laughed once, terrified.

She pulled out Niv's token, Pell's token, the strip of Kell Ashgate cloth, the black paper from Khar Veyl, the charged hymn-cloth from Saelith, the brass key Tavi had given her, and the tiny vow-stone Brakka had pressed into her palm before the gate. She set them around the cinderbreak device.

Not symbols.

Evidence.

"This is not the first age," she told the dragon-heart below. "These are the people being burned now."

The cinder answered with heat.

Her skin blistered. Saelith took one step toward her and stopped, asking with her eyes. Mara nodded. Saelith touched her shoulder. Healing light entered the burn and did not erase the pain, only kept the flesh from failing. Consent did not make pain gentle. It made it shared honestly.

Mordane's voice returned, strained now. "You are trading a system for chaos."

Othen's voice cut over his from another trumpet. "District valves at half transfer."

A second voice. Dilla's, somehow, carried through a hijacked street horn. "Soup line holding east square."

Kesh whooped from the walkway. "Who gave Dilla a horn?"

"History," Tavi shouted.

More voices followed. Heat crews, miners, hospice attendants, bread carts, troll masons, goblin runners. Not clean. Not organized enough to satisfy anyone who loved command. But alive. The city was not waiting to be saved by one room.

The cinderbreak device opened.

It did not explode.

For one breath, every name plate in the furnace index turned inside out.

The foundry filled with names.

They poured through pipes, rails, hooks, gears, white-thread loops, black-glass mirrors, ledger boards, and furnace mouths. Some came as whispers. Some as screams. Some as a single syllable held for years past death. The ash wights in the rail maze faltered. The conversion pen fell silent. Production wings across the foundry stuttered as command found bodies suddenly crowded with themselves.

Then the dragon-heart below opened one ember eye.

The floor dropped six inches.

Glass tubes cracked. Liquid heat crawled across the chamber in bright veins. The cinderbreak device kept spinning, but now the whole regulator spun around it, too much system waking too fast.

Tavi stared down. "That is earlier than ideal."

"Can we stop it?"

"No."

"Can we steer it?"

"Not without command."

Mara looked at the open cage key in her hand.

Tavi saw and shook her head. "Do not make me right to have trusted you."

Mara closed her fist around the key until its teeth cut skin.

"I will not."

The regulator chamber doors burst open from the upper side. Royal coronation horns sounded beyond them, bright and obscene over the foundry's groan.

Mordane had not stopped the transfer.

He had moved the battlefield.

Othen's voice came through the trumpet, broken by static. "Coronation feed opening. Palace is drawing the dead upward."

Arveth closed his eyes. "He means to display control publicly."

Ilyr looked toward the upper doors. "Or prove rebellion made control necessary."

Below them, the dragon-heart breathed again.

Every bell in Harrowmere answered.

The foundry had been broken open too early.

And the crown was about to make the dead kneel in daylight.""",
    29: r"""## Chapter 29: Coronation of the Dead

They climbed toward the coronation through a city vein.

The passage had not been built for people. It had been built for heat, command, and the convenient movement of things no one wished to count in daylight. Brass pipes crowded the walls. White-thread cables pulsed overhead. Below the grating, liquid warmth rushed toward the palace district in a channel that now ran unevenly, surging when district valves resisted the crown coil, thinning when the foundry tried to pull its power back.

The whole city was arguing under their feet.

Mara ran with one hand burned, one hand bleeding from Tavi's key, and the cinder cage thumping against her ribs. The ash-fever had begun behind her eyes. Not full fever yet. Sparks in the edges of sight. A sense of other wings moving when she turned her head. A taste of old smoke in water she had not drunk.

Joryn was alive behind her.

The dead were waking behind her.

The dragon-heart was waking below her.

Ahead, horns announced a king.

"Too many directions," Kesh said, breathless.

"Pick up your feet," Caldus replied.

"My feet are carrying the good half of this plan."

"Which half?"

"The half currently not wearing armor."

The banter was thin now, but it still held. Mara could feel each voice like a knot in a rope.

Othen guided them from speaking trumpet to speaking trumpet, his voice relayed by heat crews and hijacked street horns. "Upper coronation feed is two turns ahead. Palace guards have sealed the public stairs. Brakka's masons are moving through south arcade. Dilla says if anyone sees Niv near the palace, they are to sit on him."

"Effective?" Mara asked.

"She says only if they are heavy."

Saelith stumbled. Mara caught her elbow. The light-elf's hands were raw where white thread had cut them. Her face had the calm of someone walking toward punishment she had finally chosen.

"You can still go," Mara said.

"No."

"That was not a test."

"I know." Saelith straightened. "The Pale Bough will be in the coronation court. If Serathiel sees you marked by cinder and public witness, she will try to claim you in front of everyone."

"Let her try."

"That is not bravado?"

"It is scheduling."

Saelith laughed once, small and startled. The sound vanished under the horns.

Ilyr appeared at the next junction with blood on his cheek and a stolen palace sash tied around one arm. "Royal guard lines split ahead. Mordane is moving command-bound dead through the east lift."

"How many?" Caldus asked.

"Enough for a doctrine."

Arveth's head lifted. "I can hear them."

Mara could too.

The dead were being drawn upward in ranks. Not all the foundry's dead. The system was too damaged for that. But enough. Dozens, then hundreds, moved through hidden lifts and palace service stairs, hooks glowing, name plates newly stirred by the cinderbreak but not yet strong enough to refuse. Mordane was rushing them into daylight before names could become choice.

The passage ended at a grate under the coronation dais.

Through it, Mara saw gold.

Harrowmere's Crown Court blazed with banners, mirrors, polished armor, and the controlled glow of cinder braziers. The king stood beneath a canopy of white and red, robed in winter velvet, his old face powdered into ceremony. Nobles filled the galleries. Guildmasters stood in assigned ranks. Chapel officials in pale vestments formed a crescent around the throne steps. At the center of that crescent stood a tall light-elf woman whose beauty seemed less like grace than architecture.

Saelith went still.

"Serathiel," Mara whispered.

"Yes."

The saint-general did not look toward the grate. She did not need to. Her gaze was fixed on the king, but her presence filled the court with the pressure of a hand hovering above an unhealed wound.

Mordane stood at the king's right.

He had changed coats. Of course he had. This one was black with silver embroidery, immaculate despite the foundry's chaos. He held no weapon. Only a ledger, closed, one gloved hand resting on it as if on scripture.

The court herald lifted a staff.

"By winter law, cinder charter, and mercy covenant," the herald cried, "let the Crownreach witness continuance."

Continuance.

The east doors opened.

The dead entered.

They came in rows through the gold court, ash-gray bodies washed, clothed in white work robes, hooks hidden under high collars, number plates polished bright. Their feet struck the marble together. Their faces had been painted with chapel calm. To anyone too far away to smell the foundry on them, they might have looked like honored ancestors summoned to bless a king.

Mara's vision narrowed.

Kesh whispered, "Oh, that is vile."

Mordane stepped forward.

"Citizens of Harrowmere," he said, and the horns carried him beyond the court to the square outside, perhaps to every street where broadsides still clung to walls. "Today, disorder has tried to frighten you with hidden things. Let us answer by bringing hidden service into honored light."

The dead knelt.

All at once.

Marble rang under their knees.

The crowd gasped, then murmured in awe and horror and confusion. Some nobles recoiled. Some chapel officials began to sing. The king stared as if he had not been told the shape of the miracle until it stood before him.

Mordane's voice gentled. "These are not stolen bodies. They are citizens whose service continues. These are not erased names. Their names are held by the crown, preserved from unrest, protected from misuse. These are not slaves. They are proof that duty outlives death."

Arveth made a sound Mara had never heard from him.

Not anger.

Grief stripped of language.

The dead lifted their faces.

For a heartbeat, because of the cinderbreak, because of the name plates turning in the regulator, because of every broadside and every witness stone and every person reading names aloud in the streets, some of those painted faces flickered with recognition.

Then Mordane opened his ledger.

Command fell through the court.

The dead bowed their heads.

Outside, the square erupted.

Not with cheering. With the sound a city makes when an official lie becomes visible enough that everyone must decide whether to help it stand.

Serathiel turned her head.

Her eyes found the grate under the dais.

Mara felt the recognition strike like cold light.

"Mara Venn," the saint-general said, though no ordinary ear should have heard her through the stone.

Saelith gripped Mara's arm. "She has you."

"No," Mara said.

The word shook. It held anyway.

Caldus was already working the grate bolts. Tavi jammed a tool into the hinge. Kesh unrolled a chain of forged credentials and threw them aside with regret. Ilyr drew both blades. Brakka, too large for the narrow grate passage, had taken a different route and now answered from somewhere beyond the south wall with a roar that made the court's chandeliers tremble.

Mordane heard it.

His eyes moved to the south arcade.

The first bridge-stone broke through the palace wall.

Not a thrown stone. A piece of road, gray and vow-marked, shouldering its way through marble as if the city had remembered it was allowed to rearrange. Troll masons followed behind it. Brakka came through the gap with dust on her shoulders and a smile like a gate opening the wrong way.

"Road comes," she said.

The Crown Court became a battlefield.

Royal guards rushed the south breach. Command-bound dead rose from their kneel. Nobles screamed and discovered their jewels were poor armor. Chapel singers lifted hymns that hardened the air into white glass. Goblin runners poured from service doors, cutting curtain ropes and dropping banners across guard lines. Heatworkers in gray seized cinder braziers before palace officers could turn them into weapons.

The grate burst open.

Mara climbed into daylight under the throne.

For one impossible second, the whole court saw her: ash-worker coat torn at the shoulder, burned hand bandaged badly, cinder cage at her hip, Niv's token tied to her sleeve, no crown, no staff, no halo, no army that looked like armies were supposed to look.

Mordane smiled as if she had arrived on schedule.

Serathiel lifted one pale hand.

"Cinder Saint," she said, and the title moved through the court like a net.

The word wanted to settle on Mara. Wanted to make sense of her. Wanted to turn every filthy, frightened, stubborn choice into destiny and therefore property.

Saelith stepped between Mara and the saint-general.

"No," she said.

The court heard that too.

Serathiel's face did not change, which made the pain in Saelith's more visible. "Dawnmere."

"She is not yours."

"You are overwrought by proximity to profane memory."

"I am under-informed by a lifetime of beautiful omissions."

White light gathered around Serathiel.

Mordane raised his ledger.

The dead turned toward Mara.

Chapter and city and rebellion narrowed to one terrible image: a crown court full of painted corpses, a saint-general with a net of reverence, a minister with numbers sharp enough to cut throats, and a girl from Kell Ashgate standing between what the living needed and what the dead had been forced to become.

Mara lifted her empty hands.

Not the cage.

Hands.

"Where are the names?" she shouted.

The words struck the court harder than magic because half the city outside had already learned the rhythm.

From the square, thousands answered.

"Where are the names?"

The dead twitched.

Mordane's smile vanished.

The coronation broke open.""",
}


EXPANSIONS: dict[int, str] = {
    22: r"""The north road took them through the industrial throat of Kell Ashgate.

No one who had not lived there would have called it a road. It was a stacked argument between mule carts, slag channels, footbridges, broken rail, laundry lines, and heat vents that coughed without warning. Mara had crossed it a thousand times as a runner and had never seen it look so deliberately ordinary. That was the genius of Othen's plan and Dilla's soup: rebellion did not hide by vanishing. It hid by becoming the work everyone already expected the poor to do.

A boy with a coal basket dropped three pieces near a drain. Kesh bent to help him and came away with a roll of route marks tucked inside his sleeve. A woman beating rugs above a soot balcony shook out more dust than any rug deserved; the dust drifted down in two waves, then one, then three. Brakka answered by shifting the work pole on her shoulder. Signal received. Tavi stopped twice to tighten bolts on street valves that did not need tightening, leaving behind pressure marks only heat crews would notice. Caldus carried himself badly on purpose, as if his old armor habits had been crushed into a hired guard's slouch. He was terrible at it. The disguise worked because no one wanted to look at a disgraced man long enough to correct him.

At a charcoal yard below the north incline, they met the first cell that had chosen to exist.

There were nine of them: four miners, two furnace apprentices, an old chapel laundress, a schoolmaster with ink on his cuffs, and the baker from Harrowmere who had hidden the boy from the square. They stood around a cart of cracked coal bricks and pretended to argue over weight. When Mara approached, the laundress lifted one brick and revealed the hollow inside. It held broadsides rolled tight, two packets of salt, a coil of copper wire, and a child's mitten full of work tokens.

"For the dead," the laundress said.

Mara touched the mitten. "Whose?"

"Children from Bellweather school. They said if the dead needed names, maybe they also needed something warm."

Kesh looked away very quickly.

The schoolmaster cleared his throat. "We can keep two patrols busy when the north bell rings. No more than two. We are not brave enough for three."

"Two is enough," Mara said.

"Is that true?"

"It is true enough to start with."

He considered that, then nodded. "I can teach children with that."

At the next corner, trouble almost ended them without drama. A royal sergeant recognized Saelith.

He was a young man with pale eyebrows and a burn scar on his chin, standing beside the checkpoint brazier with a ledger board under one arm. His eyes moved over the forged hospice papers, passed Kesh, dismissed Tavi, climbed Brakka with visible distress, then found Saelith under the gray shawl. Recognition flared.

"Oathkeeper?"

The word froze everyone.

Saelith did not reach for hymncraft. That was the first thing Mara noticed and the first thing that kept the moment from becoming disaster.

The light-elf bowed her head, not deeply. "Formerly attached to mercy inspection."

"You are not on the shift record."

"No."

"Then why are you here?"

Saelith looked at the hospice authorization in her hand. Mara saw the old answer rise in her: order, sealed duty, need-to-know, some beautiful phrase that would have slid around the man's suspicion and made him feel smaller for asking. She did not use it.

"Because six patients on Bellweather Lane will die if the palace keeps stealing their heat."

The sergeant blinked. "The palace does not..."

Othen stepped in. "It does."

The sergeant knew him. That was dangerous too. His eyes flicked to the burn scars, the gray coat, the map tube.

"Brask, you are supposed to be on lower west intake."

"I am supposed to keep people warm."

The sergeant's jaw worked. Behind him, two younger soldiers watched with the tight faces of men discovering that orders had edges. Caldus shifted his weight. Not forward. Ready.

Mara thought of her own instruction to him: find the soldiers who hesitate.

Caldus removed his heat guard helm.

The sergeant's face went whiter. "Renn."

"Yes."

"You are under old censure."

"Also new urgency."

"If I let you pass..."

"Then tonight someone in Bellweather Lane breathes longer."

"And if this is sedition?"

Caldus looked at the north foundry gate, then back at the young man's face. "Then choose which law you want standing beside you when you remember today."

The sergeant stared at him for three long breaths.

Then he stamped the papers.

"Condensate crew through," he said too loudly. "Move before your authorization becomes interesting."

They moved.

Mara did not thank him. Gratitude would have named his disobedience too clearly in front of the others. But as she passed, she set one folded broadside beside the checkpoint brazier, face down. The sergeant's hand covered it before the wind could lift it.

Past the checkpoint, the road rose into fog. The foundry gate grew larger with every step. Mara felt the city behind her not as a crowd, but as many small decisions beginning to lean the same way: soup ladles, hidden tokens, hesitating soldiers, schoolchildren's mittens, hospice pipes, a sergeant's stamp.

Joryn's chain answered again under the mountain.

This time, Mara did not run toward it.

She walked with everyone else.""",
    23: r"""The oath-hook wing forced them to slow.

Slowing inside a foundry felt like standing in front of a wave and asking it to become thoughtful. The production alarm behind them had become a cycling bell, three notes repeated, then answered by a deeper horn below. Workers in upper galleries moved faster. Clerks sealed record shutters. Chapel attendants pulled white veils over their faces, not in prayer, Mara thought, but so they would not have to look too directly at what obedience did when interrupted.

Brakka entered the wing first because the hooks feared her and wanted her equally.

The room was taller than it was wide, a vertical forest of chains dangling over narrow walkways. Each hook had a different shape. Some were curved like fishhooks. Some opened like hands. Some were delicate as jewelry. Others were blunt iron, designed not to pierce but to drag. Every one carried script. Troll vow-law, knightly oath clauses, chapel mercy language, employment contracts, debtor marks, guild pledges, marriage promises, funeral duties, military commands. The foundry had scavenged every way people bound themselves to each other and taught those bonds to feed a machine.

Mara hated it with a coldness deeper than rage.

"Do not read anything in full," Brakka said.

"What happens?" Kesh asked.

"You begin agreeing."

"I make a point of never doing that accidentally."

The first walkway narrowed between two rows of hooks. Tavi held a small mirror out in front of her. The reflection showed hooks swinging though the air itself was still.

"They respond to intention," she whispered. "If you intend to break them, they catch the intention. If you intend to pass, they ask why. If you intend to save someone..."

A hook swung toward Mara so fast Caldus's shield barely caught it.

The impact rang through his arm. Script crawled across the shield face: protection justifies command.

Caldus stared at it.

"Do not listen," Mara said.

"I know."

"No, you agree with it."

His jaw tightened. "Yes."

That was worse, and better. Caldus shoved the hook away with a grunt, then turned the shield inward so he could not see the words.

They crossed by changing intentions out loud.

It was Arveth's suggestion, which made Kesh complain that the dead had an unfair advantage in embarrassing the living. Each person had to speak what they were doing in plain terms, not heroic ones. Caldus was not protecting the weak; he was blocking a hook for nine steps. Saelith was not offering mercy; she was keeping her hands to herself unless asked. Tavi was not saving the heatworks; she was opening a left-side maintenance hatch and promising nothing about success. Kesh was not betraying profit for friendship; he was cutting a chain because it offended his professional standards. Brakka was not carrying the road; she was putting one foot in front of the other and letting the road decide whether it deserved her.

Mara's turn came at the second bridge.

Hooks gathered above her, bright with the promises everyone wanted from her now. Save your brother. Save the city. Speak for the dead. Become what fear can follow. Become what soldiers can see. Become what elves can name. Become enough that no one else has to be.

She could not speak.

The hooks lowered.

Joryn's chain pulled under her ribs. The cinder cage warmed. The room offered her a clean bargain: become the thing they needed, and movement would become easy.

Ilyr spoke from the far side. "Say the ugly version."

She wanted to curse him. Instead she understood.

"I am walking across a bridge," Mara said, voice shaking, "because if I stop here to become important, my brother dies and the city gets a statue instead of help."

The hooks paused.

Kesh breathed, "Ugly but effective."

Mara took one step. Then another. The hooks followed but did not fall.

At the final gate, they found an old corpse sitting upright in a maintenance chair.

Not command-bound. Not working. A gnome in a burned leather apron, bones held together by a safety harness and old habit. One hand still gripped a shutoff lever. On the wall beside the chair, scratched with a tool point, were the words: Article Nine was not a suggestion.

Tavi went still.

"Do you know them?" Mara asked.

"No." Tavi's voice had gone hoarse. "But I know the handwriting style. Brassroot engineers used to leave jokes in inaccessible places. Proof they had been there. This is not a joke."

The shutoff lever had been wired around. Crown work. Messy, effective, insulting. Tavi knelt and examined the bypass.

"They died holding the line," Caldus said.

Tavi shook her head. "They died making sure the line could someday be held by someone else."

She removed a small brass maker tag from her tool roll and tied it to the old harness. Quen. Not because the dead gnome was family by blood. Because Tavi was choosing the inheritance.

Then she pulled the lever.

For one breath, every hook in the wing lost light.

The party ran.

Behind them, the old gnome's chair collapsed into ash and leather scraps, duty finally allowed to stop. Ahead, the black-glass gate woke with all their reflections waiting.""",
    24: r"""The broken mirror did not stop reflecting after they passed it.

That was the worst part. Shards of black glass clung to their boots, cuffs, hair, and weapons, each one catching a sliver of a possible self. Kesh kept finding tiny versions of his hands stealing from frightened people. Tavi saw machines blooming into disasters in the curve of her wrench. Saelith saw herself laying white light over Mara's face until the girl under it vanished. Caldus saw an empty shield standing upright long after the man behind it had died. Ilyr saw a mouth speaking half a truth. Brakka saw a road that accepted every foot and collapsed beneath the weight. Arveth saw nothing at all in the glass, which frightened him more than images might have.

They could not stop to clean the shards away. The conversion pens waited below. Joryn's chain dragged once, then again.

Mara had her own shard embedded in the bandage at her wrist.

In it, the reflected Mara no longer smiled. She watched.

"If it begins giving advice," Kesh said, "I recommend billing it."

Mara wrapped the bandage tighter. "It does not need to advise. It already told the truth."

Caldus looked back. "Not the whole truth."

"Enough of it."

"Enough truth without mercy is another trap."

That sounded like something he had learned by bleeding on it. Mara kept it.

The corridor below the mirror chamber had no guards. That worried everyone. Empty corridors in royal facilities were not gifts; they were decisions made elsewhere. Tavi found three listening wires and cut two. She left the third connected after tying it around a tiny gear that clicked out nonsense rhythms into the surveillance system.

"What is it saying?" Mara asked.

"That we are either rats, a loose belt, or a clerk with intestinal distress."

"Will that help?"

"It helped me."

They reached a side alcove where old maintenance cloaks hung on pegs, stiff with cinder dust. There, for three minutes, they became still enough to feel what the mirror had done to them. Not wounded exactly. Opened. The company avoided looking at one another because each had seen the shape of the harm they could do when fear wore virtue.

Arveth broke the silence. "The mirror is not prophetic."

Tavi snorted. "Good, because mine lacked nuance."

"It is diagnostic," he said. "It shows the command system's preferred path through you. Not fate. Vulnerability."

Saelith flexed her cut palm. "A vulnerability can still become fate if praised by the right people."

Mara looked at her. That was the closest Saelith had come to naming her own cage without someone dragging the words out.

"What did they praise in you?" Mara asked.

Saelith's first answer was posture. It straightened her back and cooled her face. Then she let it go.

"Obedience that looked like serenity," she said. "Power that left no bruise. Mercy that made no scene."

"And what did they punish?"

"Questions that made pain visible."

Mara thought of the conversion pen ahead. "Then make pain visible."

Saelith looked at her for a long moment. "You ask difficult things very plainly."

"I was poorly educated."

"No," Saelith said softly. "You were educated by consequences."

Before Mara could answer, Ilyr lifted one hand. Footsteps below. Not soldiers marching. Dragging. Many people trying not to sob.

They moved to the grate at the alcove's edge and looked down into a lower passage. Prisoners were being herded toward the conversion wing under chapel guards. Living prisoners, hands bound, white loops ready. Among them walked a woman with a newborn tied against her chest. The baby did not cry. That silence was more terrible than crying would have been.

Caldus's hand closed around his sword.

"No," Mara whispered.

His face went hard. "They are going in now."

"If we break this convoy here, the pens seal and Joryn moves."

"Mara."

"I see them."

Every word cost.

Below, the mother stumbled. A guard caught her by the shoulder, not cruelly, almost gently, and pushed her onward. Ordinary hands doing terrible work. Again and again that was the shape of the crown's horror.

Mara looked at Tavi. "Can you mark the passage?"

Tavi's eyes were bright with fury. "For return?"

"For opening from inside the pens."

"Yes."

Kesh was already moving. "I can slow them without stopping them."

"How?"

"Offensively."

He dropped through a side hatch, vanished into pipe shadow, and reappeared below as a maintenance worker with a bucket. How he found the bucket in six seconds Mara decided not to ask. He crossed the passage in front of the convoy, tripped, and spilled something that smelled like vinegar, fish, and legal consequences across the floor.

The guards halted. Prisoners recoiled. Kesh began apologizing so extravagantly that every eye moved to him. While he babbled, Tavi lowered a copper marker on a thread through the grate. It stuck under the passage arch, tiny and dull.

Saelith watched the mother and child.

"If the loops touch the baby," she whispered, "the hymn will read them as one body."

"Can you stop it?"

"In the pens. Not here. Not without closing the whole convoy around myself."

"Then in the pens," Mara said, and made it sound like certainty because uncertainty would not help anyone walk.

Kesh's delay lasted forty-seven seconds. Long enough. Not enough.

The convoy moved on.

Mara stayed at the grate until the last prisoner vanished below. The mirror shard in her bandage caught her face. For a moment she saw the reflected Mara's accusation: you chose Joryn first by not choosing them now.

"No," Mara told the shard. "I chose the room where I can open all the chains."

The shard did not answer.

That was good. She did not need forgiveness from the worst version of herself. She needed warning.

They descended after the convoy, carrying warning like a blade held carefully by the flat.""",
    25: r"""The conversion pen did not empty after the first prisoners came free.

It became a place where freedom had to be organized while danger kept arriving.

That was the part no story had prepared Mara for. Chains falling away were only the beginning. Bodies that had been held too long did not become useful because someone needed them to. One man fainted and struck his head on the rail. The mother from the convoy clutched her silent baby and would not let Saelith near until Rakka Fen said, "She asks now," which was apparently enough to make the mother cry and nod. A former soldier tried to run back the way they had come because he believed his unit would help if he could explain. Tesson Vair punched him once, then apologized, then recruited him to lift stretchers because panic needed a job.

Joryn sat against the wall while Mara wanted to be beside him every second.

Instead she carried water.

It was absurd and necessary. She filled bowls from a pump Tavi declared "probably not poison unless the crown has become artistically petty" and passed them down the line. She learned names as she did: Avel Moss, Sera Pike, Omi Thread, Vennic Hall, Orra Shell, Siv Noct-Tal, Bren the bellows boy, Miri with the baby, whose child was named Sol because she had refused to let a winter birth have a winter name. Each name took space in Mara. Each one made Joryn both less alone and harder to reach.

He watched her understand it.

"This is why I told you to keep small," he said when she finally crouched beside him.

"Because water distribution is frightening?"

"Because once people know you will carry a bowl, they hand you wells."

She looked at him, startled by the bitterness. "You are angry."

"Yes."

"At me?"

"At everyone. You are nearest."

The honesty hurt and steadied her at once. "Good. I was worried you would be noble about it."

He laughed, and because the memory had returned, the sound nearly undid her. It was quiet, cracked by pain, but it was his.

"I do not like them looking at you," he said.

"Who?"

"All of them. Like you are the door. Like if they say your name right, you will open."

Mara leaned back against the wall beside him. The conversion pen stank of blood, lavender, smoke, and freed fear. "I do not like it either."

"Then stop."

"How?"

He closed his eyes. "That is the problem. I do not know anymore."

There it was: the fracture she had feared. Joryn had spent years being the one who knew where to stand, what lie to tell, how small to make them both so the world stepped over instead of on them. Now she was asking him to stand in a room full of strangers and accept that smallness had stopped saving anyone.

"I still need you," she said.

"Not the same way."

"No."

He swallowed. "I hate that."

"Me too."

The floor shook before either could soften it.

Tavi shouted from the spindle, "Anyone currently engaged in family honesty should relocate."

The furnace cycle had tried to restart. Without the spindle's full pressure logic, it stuttered and began drawing from loose loops. White threads crawled along the floor toward freed wrists, seeking the nearest old pattern. Saelith saw and went pale.

"I need consent from each cluster," she said. "Fast."

"Do it," Joryn told Mara.

"You are bleeding."

"I am also bossy. Go."

Mara went cluster by cluster. Not asking beautifully. Not making speeches. "Can Saelith hold the thread off you?" she demanded. Yes. Yes. What does that mean? It means the white magic does not grab your wrist again. Then yes. Can she touch the baby's blanket? Miri stared at Saelith, at Mara, then at the thread crawling toward Sol's tiny hand. "Only the blanket," she said. Saelith obeyed exactly.

Exactness became a kind of redemption. Not enough to erase. Enough to build the next moment on.

When the last thread withdrew, the spindle cracked fully open and revealed its inner core: a small black-glass bead full of reflections. Tavi picked it out with pliers.

"Found the cruelty seed."

"Can you break it?" Mara asked.

"Yes, but it is recording every pressure response from this room. If we copy it first, we can prove the design was intentionally modified from warding to coercion."

Joryn groaned. "Copy it while fleeing?"

Tavi pointed at him with the pliers. "I like this one."

The far door opened then, and Mordane arrived with his floating ledger.

Later, Mara would remember details out of order: Joryn trying to stand, Caldus's sword at the priest-physician's wrist, Saelith turning away from the baby because permission ended, Kesh quietly passing stolen keys to Rakka, Arveth's dead face becoming more alive with anger than many living faces in the room.

Most of all, she would remember Mordane looking pleased to see the freed prisoners upright.

Not surprised.

Pleased.

Because he had wanted witnesses for his argument.

And because he believed arguments, like people, could be owned by the one who arranged the room.""",
    26: r"""The room did not become brave after Mordane's numbers failed to silence it.

It became divided.

That was more frightening. Some freed prisoners stared at Mara as if she had already won, which was dangerous because hope could be another way of handing her a chain. Others stared at Mordane because what he said had touched the terror they had lived with all winter: heat going out, children coughing, infirmary pipes freezing, old people dying under blankets while officials argued about guilt. A few looked at the floor, which meant they had understood both sides enough to feel trapped between them.

Mordane saw that too.

"Ask them," he said.

Mara did not answer.

He lifted one hand toward the freed prisoners. "Ask whether they will personally accept a winter without continuance labor. Ask whether they want the hospice pipes cold tonight. Ask whether every person in this room is prepared to die for the dignity of the dead when the living begin freezing."

Rakka Fen bared her teeth. "I am prepared for you to stop talking."

"A stirring policy."

Harl Brim, still beside Tomas, said, "You make it sound like only two doors exist."

Mordane's eyes moved to him. "Because most doors are decorative."

Othen's voice crackled through the speaking pipe. "Not if workers build them."

The freed prisoners turned toward the pipe. Mordane's jaw tightened by the smallest degree.

Othen continued, voice carrying static, breath, and the noise of a crew shouting behind him. "District valves at first transfer. Bellweather Lane warm. East tenements warm. Palace reserve down twelve percent."

A murmur passed through the pen.

"Impossible," said one of Mordane's clerks.

Tavi looked delighted. "That is often the first review."

Mordane's ledger flipped pages faster. "Temporary redistribution. Unstable. Dependent on worker compliance, illicit routing, and untested gnomish modification."

"You say that like it is worse than corpses with hooks in their throats," Tavi snapped.

"It may kill fewer people today and more tomorrow."

"Then we keep working tomorrow."

"Ah," Mordane said. "The rebel discovers maintenance."

There was power in that insult because maintenance was not glorious and everyone knew it. No final victory, no single lever, no beautiful end to all harm. Just people showing up again and again to stop systems from becoming murder with paperwork.

Mara found herself smiling.

Mordane noticed. "Have I amused you?"

"No. You just made our side sound better."

For a moment the prisoners looked at her not like a door, but like someone who had said a thing they could carry.

Mordane changed tactics.

He opened the floating ledger wider. The pages glowed with cinder-script. Names appeared on them, thousands of names, each one crossed by a heat value and a survival projection. The ledger's magic pressed on the room, not command exactly, but persuasion weighted by fear. Mara felt it try to make care too heavy to lift.

"This is governance," Mordane said. "Not romance. Not vengeance. The arithmetic of need. A kingdom is not saved by refusing to count."

The ledger turned toward Mara.

Her father's name appeared.

Edrin Venn. Auditory cinder sensitivity. Fatal accident classification useful. Family compensation denied under negligence clause. Daughter possible recurrence.

The room vanished.

For one breath Mara was under the table again, hearing storm rain and her father's cough, seeing his hand close around a black crescent mark in his palm. The company had called him careless. Mordane's ledger called him useful. Different lie, same grave.

Joryn shouted her name.

The sound brought her back.

Mordane watched her with clinical interest. "Your father heard the cinder and hid it poorly. His death prevented unrest and produced data. That is not cruelty. It is the proper use of accident."

Caldus moved before Mara did.

He struck the ledger with his sword.

The blade bounced off a sheet of cinder light and cracked at the edge. Mordane raised one brow.

"The knight attacks a record. Very modern."

Caldus looked at the damaged sword, then at the prisoners, then at Mara. "I am done guarding documents that murder people."

He threw the sword aside.

Then he picked up the priest-physician's ring of keys and unlocked the door to the rail maze.

Mordane's eyes sharpened. "That door holds the production line."

"Yes."

"Open it and the dead enter uncontrolled."

Caldus looked at Mara. In his face she saw the concession Carson's note had asked for, though she would never know that note existed: he was not clearing the board for her, not deciding the shape of victory by old rank or old guilt. He was asking.

Mara listened beneath the door.

The dead waited there. Not empty. Not safe. Not obedient cleanly anymore. Names stirred like banked coals behind hooks. The production line wanted to be told whether to kill, work, kneel, or burn. Mordane was ready to command them. The foundry was ready to spend them. The room was ready to fear them.

"Open it," Mara said.

Caldus did.

The dead entered, and the arithmetic began to fail in earnest.""",
    27: r"""The first named dead to enter the room was Lysa Mar.

Mara knew her by the break in the rhythm. Every other ash wight came forward on command cadence: left, drag, lift, strike. Lysa came like someone walking into a room she had not been invited to and intended to make that everyone's problem. Her shovel hung loose in one hand. The hook in her throat glowed, dimmed, glowed again. Ash clung to the remains of her work dress. Her eyes were cloudy, but not empty.

Behind her came Mav Corren, Tomas Vale dragging the broken furnace lever, two dead with number plates half torn free, then more, crowding the doorway in a gray press of bodies not yet an army and no longer a tool.

Mordane lifted his ledger.

"Line seven, restore operation."

The hooks flared.

Several dead jerked forward. Lysa stopped. The dead behind her struck her back and stalled. Command traveled through the line, met her refusal, and buckled.

Mara said her name.

"Lysa Mar."

The hook in Lysa's throat cracked down one side.

Arveth stepped beside Mara and began reading from the oilskin ledger. "Lysa Mar. Lower west furnace draw. Low command yield. Family objection crossed through by chapel clerk. No final witness."

The dead woman's head lifted.

Mordane's ledger brightened. "Line seven, restore operation."

This time Harl Brim answered. "Lysa hated furnace draw. Said it made the city smell like a wet boot."

A laugh went through the freed prisoners, ragged and incredulous. Not because it was funny enough. Because a preference had survived where command wanted output.

Lysa turned toward Mordane.

The room changed.

It was not liberation yet. Some dead still obeyed. One lunged at a prisoner and had to be pinned by Brakka. Another clawed at its own throat until Saelith, with permission from the dead man's brother, held the hook steady enough for Arveth to speak a name. A third collapsed and did not rise, and Mara felt the cost of not forcing choice. Freedom was not efficient. It was not safe. It did not arrange itself into a clean battle line.

But it was real.

Mordane began issuing numbers faster.

The ledger pages whipped. "Units twelve through eighteen, secure rebel principals. Units twenty through thirty, protect heat reserve. All unassigned continuation labor, kneel."

Some knelt.

That hurt. Mara wanted the name-work to be complete, wanted witness to sweep the room like fire in dry straw. Instead it moved unevenly, catching where memory had tinder, failing where damage had gone too deep. She felt the temptation again: open the cage, command them to stand, make refusal look clean.

The mirror shard at her wrist glinted.

Possible.

She closed her fist over it until glass cut skin.

"No," she whispered.

Joryn, from the prisoner line, heard. "No what?"

"Shortcuts."

"Good. You are awful with those."

Mara laughed, badly, and the sound steadied her.

Tesson Vair and the former soldiers formed a living wall around the weakest prisoners. Caldus joined them without taking command. That mattered. He did not tell them how to stand until Tesson asked. Then he spoke quickly, practically, no rank, no old parade voice. Kesh moved among the dead who had knelt, cutting number plates free where he could, muttering apologies each time a plate took skin with it. Tavi and Othen argued through the pipe over pressure redistribution while she stripped parts from the spindle and turned them into a portable hook jammer.

"You invented that now?" Kesh shouted.

"I invented half of it before and object to your tone."

"What does it do?"

"Annoys tyranny in a cone."

"Marry me professionally."

Saelith stood before Tomas Vale.

The dead worker still gripped the broken furnace lever. His hook was cracked but not broken. His mouth moved around the one word he had found: Ma.

Saelith did not touch him.

"Tomas," she said. "I cannot ask your mother. I cannot ask you clearly. I can ask what your body is doing now."

His dead hand tightened on the lever.

"Do you want this lever kept from them?"

The hook flared. Tomas fell to one knee but did not release it.

Saelith turned. "He is refusing through action."

Arveth nodded once. "Record it as such."

"I am not a clerk."

"Today everyone is."

She smiled then, despite blood and terror, and took the portable hook jammer from Tavi. "Then I will make a note."

The jammer screamed when she drove it into the floor beside Tomas. White light and brass sparks burst outward. Hooks across the room flickered. Not dead. Not gone. Interrupted.

Lysa Mar moved.

She crossed the room slowly, every step a war between old command and new name. Mordane backed one pace. Only one. Enough.

"You cannot govern by anecdote," he said.

Mara stepped with Lysa. "You cannot murder by spreadsheet when the cells start talking."

"That was Kesh's line," Kesh objected from under a rail brace.

"You can invoice me later."

Lysa reached Mordane's floating ledger and struck it with her shovel.

The blow did not destroy the ledger. It knocked it open to a page he had not chosen.

Names spilled across the air: every dead worker currently in the room, every heat value beside them, every family objection, every erased witness. The freed prisoners saw. The command-bound guards saw. The clerks saw their own handwriting. One clerk began to sob.

Mordane's control wavered.

The room did not become safe.

It became answerable.

That was when Othen shouted through the pipe, "Crown coil at breach! If the regulator does not open now, the palace takes the heat and the lower districts freeze."

Tavi looked at Mara.

Mara looked at the dead.

Some stood. Some knelt. Some shook under hooks. Some reached toward names. Some had no reach left.

"We go to the regulator," Mara said.

Lysa Mar turned her ruined face toward her.

For a moment Mara thought the dead woman would follow.

Instead Lysa planted her shovel in the floor between Mordane and the prisoners.

Choice.

Not Mara's choice. Lysa's.

The first unmistakable one.

The dead had refused, and refusal held the room while the living ran.""",
    28: r"""The cinderbreak device did not only open names.

It opened distance.

As the furnace index turned inside out, Mara saw where the names were going. Not in lines, not through pipes as heat did, but across memory. Lysa Mar's name struck the hook in her throat and became a shovel planted in a conversion pen. Pell Orwick's name touched a dead hand under goblin care in the market beneath Auntie Grum, and miles away, if Mara understood the sudden smell of marsh mint correctly, Pell lifted his head. Maelin Noct-Vey's retained mark flared somewhere beyond the foundry map, behind black doors and older secrecy. Joryn's living tag burned white, not completed, not broken, exposed.

The network was larger than Harrowmere.

Tavi saw it too. She was hanging from the second ring of the regulator, one arm wrapped around a glass support, goggles blazing with reflected fire.

"Oh," she shouted.

"Good oh?" Kesh called.

"Continent oh."

Othen's voice came through the trumpet, half drowned by static. "Repeat?"

Tavi looked down at Mara. "This foundry is not central. It is a node."

The word meant little to most of them and too much to Mara. The cinder below answered with faraway echoes: other buried hearts, other heatworks, other cities glowing clean over hidden rooms, other names turned inward on brass plates. Not all the same. Not all Mordane's. Some older, some sleeping, some wounded in ways that had not yet become policy.

Book Two opened under her feet without naming itself.

She nearly fell into it.

Saelith tightened her hand on Mara's shoulder. "Stay here."

"I am."

"No. You are listening outward."

"There is outward."

"There will be after today."

Mara forced her attention back to the regulator chamber. The floor was cracking. Liquid heat crawled from broken tubes, turning screws red, licking at the brass plates of the furnace index. Kesh and Ilyr had reached the third ring to cut crown coil receivers. Caldus held the entry bridge against guards in palace livery, shield denting under repeated strikes. Brakka had wedged her maul through a gear wheel the size of a millhouse and was holding it from turning with both arms, every muscle in her body shaking. Arveth stood waist-deep in fallen name plates, feeding them into the cinderbreak as if each one were a coal being returned to a hearth.

Tavi needed more time.

The dragon-heart was done giving it politely.

A memory rose from below, huge enough to bend the chamber.

Mara saw the first covenant not as history, but as heat: dragons circling over a dead capital, humans and elves and trolls and goblins and gnomes gathered under ash-dark sky, the dying of the first age, the bargain to bury power so the world could continue. She felt the lie hidden inside the bargain too. Not everyone had consented. Not every dragon had died. Not every heart had been meant to become fuel.

One grief-heavy presence turned in the dark.

Not a name yet.

A shape.

Vorrakai.

Mara did not know how she knew it. The knowing left ash on her tongue.

The presence offered stillness. Not death exactly. Quiet. An end to spending, burning, wanting, counting. A world no longer hungry enough to hurt itself.

For one fevered breath, it sounded merciful.

Then Joryn's laugh, newly returned, cut through the old grief like a badly tuned whistle.

No, Mara thought. The living are noisy. That is the point.

The dragon-heart withdrew, not defeated, but interested.

Glass shattered above her.

Kesh fell from the third ring.

Ilyr caught his scarf with one hand and a pipe brace with the other. Kesh dangled over a river of liquid heat, eyes wide.

"I take back every ankle remark," Kesh said.

"Too late," Ilyr replied, hauling him up by inches.

Caldus could not leave the bridge. Brakka could not leave the gear. Tavi could not leave the device. Mara moved before deciding. She climbed the regulator frame, burned hand slipping on hot brass, legs shaking with ash-fever. Saelith shouted after her. Mara ignored her until the light-elf said, "May I steady you?"

Mara grabbed the next rung. "Yes."

Light caught her back, not pushing, not binding, only holding where her strength failed. She climbed faster.

At the third ring, Ilyr's grip slipped.

Mara reached them and caught Kesh's wrist.

The goblin stared at her hand. "You are very warm."

"Complain later."

"I complain as prayer."

Together, she and Ilyr hauled him onto the ring. Kesh lay flat, breathing hard. Then he shoved a cut crown receiver into Mara's hand.

"Put that in Tavi's arrogant little tripod."

"You almost died for this?"

"I dislike almost. It cheapens the brand."

Mara carried it down as the whole chamber tipped into a new angle. Tavi caught the receiver, slammed it into the cinderbreak, and twisted.

The device sang.

Not a hymn. Not a command. A rough, impossible chord made from brass, contract tooth, vow dust, number plate, hymn-cloth, shadow-blood, heatwork valve code, and the witness of names spoken badly but honestly. It opened the path.

Names rushed home.

Across the foundry, the dead began to choose.

Some chose to stand.

Some chose to fall.

Some chose to hold doors while living prisoners escaped.

Some chose the furnace, not because command dragged them but because their bodies were too ruined and they wanted the heat of their ending to go somewhere named.

Arveth cried out at that, a broken sound.

Mara understood. Witness did not get to edit grief into comfort.

The crown coil screamed as district valves took the load. In Harrowmere, bells answered. In Bellweather Lane, hospice pipes held. In lower tenements, heat shuddered, dipped, returned. In the palace laundry, towels went cold with revolutionary dignity.

The foundry did not explode.

It broke open.

That was worse for Mordane and better for everyone else.

Then the coronation horns sounded through the upper doors, and every dead who had not yet chosen received one final command.

Kneel in daylight.

The cinderbreak had succeeded too early. Or too late. Or exactly when history could no longer be kept underground.

Mara looked down at Tavi. "Can the device keep working without us?"

"It can keep failing usefully for twelve minutes."

"Good."

"That was not a yes-shaped good."

"No."

They ran for the upper passage while the dragon-heart watched from below, ember eye open, learning the taste of Mara's refusal.""",
    29: r"""The chant outside the Crown Court did not begin as a chant.

It began as many people saying the same question badly.

Where are the names?

At first the words reached the court through walls and horns and broken windows in pieces. A woman near the east gate. A group of heatworkers under the balcony. Children in an upper street reading from a broadside too large for their hands. Goblin runners laughing as they pasted names over royal notices. Troll masons speaking each word like stone being set. Miners from Kell Ashgate arriving breathless, ash-covered, not enough to take a palace and more than enough to make one ashamed.

Where are the names?

Then the rhythm found itself.

Mordane lifted his ledger to drown it.

Serathiel lifted white light to sanctify it.

Mara lifted empty hands and let the city be louder.

The dead in the court shook.

Not all at once. A tremor passed through the kneeling rows. Painted calm cracked around mouths. White collars shifted as hooks struggled under hidden cloth. One dead woman raised her head a finger's width. A noble screamed as if the movement itself had bitten her. A chapel singer lost the note and began sobbing into her veil.

Mordane's command struck again.

"Continue kneeling."

Several dead obeyed. Several did not. The difference tore the spectacle apart.

Brakka and the troll masons widened the breach in the south wall. They did not simply smash, though there was plenty of that. They set vow-stones into broken marble and spoke road-law over palace floor. The court had been built to separate ruler from ruled: dais above floor, gallery above petitioners, throne above witnesses. Under troll hands, the architecture began disagreeing. Steps shifted. A railing cracked and settled into a ramp. A decorative arch leaned until it became a brace between guards and civilians.

"Road comes," Brakka said again, and this time people understood enough to move along it.

Kesh darted through the chaos cutting curtain ropes, purse strings, command tags, and at least one noble's belt, which he insisted was tactically necessary. Tavi reached a cinder brazier and rewired it into a speaking horn, shouting Othen's valve instructions into the palace network while heatworkers in the square answered through stolen trumpets. Ilyr climbed the gallery rail and drove a blade through a black-glass surveillance plate. The plate spilled hidden images into the air: foundry pens, the kneeling dead being painted, Mordane rehearsing phrases, clerks smoothing collars over hooks.

The nobles saw what the white robes hid.

Some turned away.

Mara saw them turn and shouted, "Look!"

Her voice cracked across the court.

"If you used the warmth, look at what carried it."

That was cruel. It was also necessary. She had used the warmth too. Kell Ashgate had survived winters on cinder heat, cheap ash, hidden labor, and accidents labeled careless. Innocence was not waiting anywhere clean. Only responsibility.

Saelith stood between Mara and Serathiel.

The saint-general's light grew until every white surface in the court shone. She looked like mercy carved into a weapon and taught to believe itself a window.

"Move aside, Dawnmere."

"No."

"You bleed disorder."

"I bleed because people do."

Serathiel's gaze flicked to Mara. "Child, you stand in dangerous public witness. You are untrained, cinder-marked, politically contaminated, and surrounded by opportunists. The Pale Bough can keep you from becoming what the crown fears."

Mara laughed once. It surprised everyone, including her.

"You still think my danger is what I might become."

"Yes."

"Look around."

The dead were rising unevenly. Guards were choosing sides by the heartbeat. Citizens flooded the south breach. The king had backed away from the throne, staring at Mordane with dawning horror or dawning fear for himself. The city outside kept asking for names.

"My danger is that I keep making people answer for what they already are."

Serathiel's face hardened. "Reverence can protect the revered."

Saelith's voice shook. "Reverence can erase the revered."

The words struck the light between them.

For the first time, Serathiel looked wounded.

Mordane used the moment.

He turned the ledger toward the dead and spoke a command not to their hooks, but to the city horns Tavi had not yet captured.

"Citizens of Harrowmere," his voice boomed into the square. "The rebels have broken foundry regulation. If order is not restored, lower districts will lose heat. The continuation dead now kneeling in this court are the only force capable of protecting you from the sabotage committed in your name."

There it was. The old trap made public. Fear against witness. Warmth against dignity. Living need against stolen dead.

The square wavered.

Mara felt it, though she could not see all of them. Thousands of people asking whether truth would make their children cold. Mordane's argument did not need to be pure. It only needed to be frightening.

Othen's voice cracked through the brazier horn Tavi had seized. "Bellweather warm. East tenement warm. South market warm. District valves holding."

Another heatworker answered from outside. "West infirmary warm."

Dilla's voice followed, fierce and distorted. "Soup hot too, since ministers care so deeply about civic temperature."

Laughter hit the square, incredulous and sharp. It did not solve fear. It punctured Mordane's ownership of it.

The king stepped forward at last. "Minister Mordane."

Mordane did not look at him. "Majesty, stand back."

The court heard the command in the courtesy.

So did the king.

Too late, perhaps, but hearing mattered.

Mara moved toward the dead rows. Serathiel's light reached for her. Saelith blocked it and screamed as the force drove her to one knee.

"Saelith!"

"Do not stop," Saelith said through her teeth. "I gave permission for this."

That was not funny. It still sounded like growth.

Mara reached the first dead woman who had raised her head. The collar hid the hook. Mara pulled it open. A number plate hung there, polished for ceremony.

"Arveth!" she shouted.

The dead witness climbed from the broken grate, slower than before, one shoulder still torn by the hook from the mirror chamber. He saw the plate. "Number twelve-seven. Foundry index..."

He stopped.

"What?"

"I know this one."

The dead woman's cloudy eyes moved toward him.

Arveth's voice broke. "Professor Halea Voss. Orrowen civic historian. Executed under the third revision. I argued your appeal after you were already dead."

The dead woman's mouth opened.

"Late," she whispered.

Arveth bowed his head. "Yes."

The hook under her collar split.

Halea Voss stood.

Not tall. Not dramatic. A dead scholar in a white robe with paint cracking on her cheeks. She turned to the row behind her and spoke one word in a language older than Harrowmere.

Remember.

The coronation dead began to rise.

Mordane's ledger flared so bright it burned the air.

The crown court became no longer a display, no longer a debate, but the first public battle between command and witness.

And outside, the city found the rhythm fully at last.

Where are the names?

Where are the names?

Where are the names?

The answer was standing up.

The first palace guard to lower his weapon did it badly.

He did not make a speech. He did not throw his sword clattering across the marble in a gesture clean enough for songs. He looked at Halea Voss standing in her painted death-robe, then at the hook splitting under her collar, then at the king, then at Mordane's ledger. His hands began to shake. The spear point dipped. A captain struck him across the face with a gauntlet.

The guard fell.

Caldus caught him before his head hit the floor.

That was the moment many soldiers saw him.

Not the old crest. Not the disgrace posters. Not the formal shape of rank. A man with a cracked sword and scraped shield catching a frightened guard he might once have ordered to stand. Caldus set the young man behind him and raised the shield toward the captain.

"Line holds for the living," he said.

The captain snarled. "You have no command."

"Good. Then choose."

The words moved through the nearest soldiers with more force than command because they made no promise of safety. Two stepped back. One joined the captain. One threw his spear down and dragged the fallen guard farther from the dead rows. Difference spread, and command hated difference.

Mordane raised the ledger higher.

"All crown-bound personnel, secure the dais."

Some soldiers obeyed. Some froze. Some looked toward the king, waiting for a command that would make choice unnecessary.

The king did not give it.

His powdered face had gone slack with age, fear, and the discovery that a lifetime of being protected from truth had left him powerless in front of it. Mara wanted to hate him cleanly. She could not. He was not innocent. He was not sovereign in any meaningful sense either. He was a man in a crown standing beside the minister who had learned to make royal silence useful.

Mordane saw the king's hesitation and stepped in front of him.

"Majesty, for your safety."

The phrase was a hand over a mouth.

Joryn would have spat at it.

Mara moved toward the dais.

The dead rows shifted with her. Not following. Not yet. Turning, some toward her, some toward Mordane, some toward the doors where citizens pressed against guard lines, some toward nothing anyone living could see. Names had not made them simple. Names had made them present.

Serathiel lifted both hands.

White branches of light grew from the marble at Mara's feet. They did not burn. They bloomed, beautiful, fast, and strong, curving around her ankles, knees, waist. The court gasped. The light smelled like rain on clean stone and funeral lilies.

"Enough," Serathiel said. "A cinder-marked child cannot adjudicate the dead in public panic."

The branches tightened.

Saelith rose from one knee, blood soaking both sleeves. "You taught me mercy listens."

"Mercy hears what disorder cannot safely interpret."

"No," Saelith said. "Mercy hears, then asks."

She pressed her bleeding palms to the nearest branch of light. It shuddered. Serathiel's eyes sharpened with pain, not physical yet, but doctrinal: a favored student becoming a contradiction in front of witnesses.

"Dawnmere, release."

"I do not have her."

Saelith looked at Mara.

"May I break this?"

The question landed in the court like a thrown stone into glass.

Serathiel's lips parted. She understood the rebellion inside the grammar before anyone else did. Saelith could have broken the binding by treating Mara as someone to protect. Instead she asked. Publicly. In the face of her order. With a thousand people hearing what beautiful law had forgotten to do.

Mara's throat hurt. "Yes."

Saelith broke the branches.

They shattered into white leaves that cut her hands further and dissolved before touching the floor. She swayed. Ilyr was there, catching her by the elbow with a gentleness that looked strange on him only if one had not been paying attention.

Serathiel lowered her hands slowly.

"You will answer for this."

Saelith looked at the dead standing in rows, at the citizens crowding the breach, at Mara with ash on her face. "At last."

Tavi's brazier horn screamed with feedback. "Mara! Crown coil is pulling through the dais. Mordane is using the coronation cinder under the throne as a command amplifier."

Mara looked down.

Lines of blue-white light ran under the marble from the throne to the dead rows, from the dead rows to Mordane's ledger, from the ledger down into the foundry. The court itself was part of the machine. Of course it was. The spectacle had never only been symbolic. The kneeling dead, the king, the crown, the chapel crescent, the witnesses in the square: all arranged as a circuit. Public belief made command heavier. Awe made obedience easier.

"Can you cut it?" Mara shouted.

"Not from here," Tavi answered through the horn. "Someone has to break the dais circuit or change what the court is witnessing."

Kesh appeared beside the throne steps holding three stolen signet rings, a palace curtain tassel, and a look of great professional injury. "Breaking the dais circuit sounds specific."

"Can you do it?"

"With time, tools, and fewer emotionally charged corpses."

Halea Voss turned her dead face toward him. "You have one of those."

Kesh stared. "Did the dead scholar just heckle me?"

"Yes," Arveth said, and there was pride in it.

Mara saw the circuit then not as Tavi did, not as brass and cinder lines, but as a lie given architecture. The court was witnessing continuance as duty because Mordane had staged it that way. Change the witness, change the weight.

She climbed onto the lowest throne step.

Mordane's gaze snapped to her. "Careful, Miss Venn. The last person who mounted those steps without leave lost a hand."

"Did you count it?"

"Naturally."

"Then watch."

Mara turned her back on him.

That frightened him. She felt it like a gap in heat.

She faced the court, the square beyond the broken wall, the soldiers half-choosing, the nobles half-hiding, the dead half-risen, the king half-awake to his own uselessness, the city half-starved for truth and half-terrified of what truth would cost.

"These are not honored servants," Mara said. The horns caught her voice because Tavi loved theft and had apparently given every brazier in the court opinions. "They are not proof that duty outlives death. They are people whose names were taken so their bodies could be made useful without asking. Some may choose to serve. Some may choose to stop. Some may choose endings we do not like. But if you only honor the dead after stealing the word no from them, you are not honoring them. You are decorating a theft."

Mordane spoke behind her. "And when heat fails?"

Mara turned enough to include him in the answer without giving him the room. "Then we fix heat with living hands and accountable systems. We do not hide murder under winter blankets and call everyone who objects sentimental."

Othen's voice boomed from the square horn. "District valves holding."

"For now," Mordane said.

"Yes," Mara snapped. "For now. That is how work works. You keep doing it."

The line was not grand. That made people laugh. A small, frightened laugh, but real. It belonged to heatworkers, miners, laundresses, bakers, schoolmasters, valve crews, people whose lives were made of work that never became ceremony. It moved through the court and loosened something Mordane had tightened.

The blue-white circuit under the marble flickered.

Halea Voss took one step toward the dais. "My name," she said.

Arveth answered. "Halea Voss."

Another dead voice. "Mine."

A living woman in the crowd screamed, "Orra Pell! That is my aunt!"

"Orra Pell," Mara repeated.

Another. Another. Some names came from Arveth's ledger. Some from families. Some from fragments: blue thread, bad whistle, scar over left eye, woman who hated carrots, man who sang west-road lullabies, soldier with a missing thumb, goblin with a gold tooth, gnome who wrote Article Nine was not a suggestion. Not all could be certain. Arveth marked uncertain aloud when uncertain came. It mattered that they did not lie to make the moment cleaner.

Each name changed the circuit.

The court was no longer witnessing Mordane's continuance.

It was witnessing theft.

The throne cinder under the dais cracked.

Mordane struck Mara then, not with a blade, but with the ledger's full command weight. Numbers slammed into her mind: winter deaths prevented, heat units produced, unrest suppressed, bodies allocated, acceptable variance, her father, Pell, Lysa, Joryn, Mara Venn possible recurrence, asset risk, asset value. The arithmetic tried to make her see herself as another column. If she could be useful enough, the suffering could balance. If she could spend herself correctly, no one else would need to choose.

For one heartbeat, that sounded almost peaceful.

Then Niv's token burned against her wrist.

Bring it back, he had said.

Not spend it well. Not become worthy. Bring it back.

Mara gripped the token and held the ledger's pressure off with the smallest, least heroic fact in the world: a child expected her to return something borrowed.

"No," she said.

The word moved through the cinder lines under the dais.

Not command. Refusal.

The throne cinder split open with a sound like a bell struck under the earth.

Every dead person in the court lifted their head.

Outside, the city fell silent at once.

In that silence, from far below, the dragon-heart answered the cracked throne.

Once.

The sound was too low for ears and too large for thought. It passed through marble, bone, pipe, bell, bread ovens, hospice beds, and the oldest stones under Harrowmere. Across the court, candles blew sideways. The king dropped to his knees. Serathiel looked not frightened, but informed against her will. Ilyr whispered something in dark-elf speech that sounded like a forbidden door opening.

Mordane's ledger went blank.

For the first time, he had no number ready.

The king found his voice in the blankness.

It was not a kingly voice. Not at first. It cracked like an old hinge and came out too soft for the horns until Tavi, somewhere by the brazier, cursed and twisted the pickup toward him.

"Minister," the king said.

Mordane turned slowly.

That was another silence. Smaller than the dragon-heart's, but human enough to cut. Everyone in the court had spent years hearing the king named as law, mercy, winter father, shield of the Crownreach. Now he stood in his heavy robe with ash settling on his powdered hair, and he looked less like law than a man discovering law had been used while he slept inside ceremony.

"Majesty," Mordane said, recovering too quickly. "Step back."

The king flinched.

Not from fear of harm. From habit.

Mara saw it and understood, to her disgust, that crowns could become cages too. Rich cages. Gilded cages. Cages with servants and songs and warm rooms. But cages if every truth entering them had been trimmed to fit.

The king looked at the dead. At Halea Voss. At the cracked collars. At the living people crowding his polished court with soot on their clothes and names in their hands.

"Were they named?" he asked.

Mordane did not answer.

The king's face folded around something too late to deserve pity and too real to dismiss. "Were they named to me?"

"Majesty, governance requires protected channels."

"That is not an answer."

No one moved.

Mordane's blank ledger fluttered, pages trying to find numbers and finding none. His control had always depended on speaking for systems that answered him. For one breath, the system had gone quiet.

The king turned toward Mara.

People would later say she bowed. She did not. Her knees were busy holding her up.

"Girl," he said, then stopped as if hearing himself. "Mara Venn."

Her name in his mouth made the court lean. She hated that too. A king speaking a poor girl's name was not justice. It was only a sound overdue.

"Do you ask judgment?" he said.

Mordane's eyes sharpened.

Serathiel watched like a blade in prayer.

The square waited.

Mara thought of how easy it would be to say yes. To make the king useful. To let authority stamp the truth so everyone could feel cleaner about believing it. Then the mirror shard in her wrist cut again, and she saw reflected Mara taking a crown's permission because permission was faster than witness.

"No," Mara said.

The court breathed.

"I ask you to hear," she said. "Then answer with everyone else."

The king stared at her.

No one had told him that being included could feel like being lowered from a throne.

Halea Voss stepped forward. "My name was not a petition."

Arveth repeated, voice clear despite the tear in his shoulder. "Halea Voss. Witnessed."

The woman from the crowd cried again, "Orra Pell!"

"Orra Pell," Mara answered.

Then the king, old and powdered and late, said it too.

"Orra Pell."

The name did not absolve him. It did not repair the foundry. It did not turn monarchy into justice with one trembling word. But the court heard the crown speak a stolen name as something it had failed, not something it owned.

That was enough to make Mordane move.

He lunged for the blank ledger, not with hands but with whatever command still lived in him. The pages flared black at the edges. Numbers returned in fragments. Not all. Enough to hurt. He would rebuild the arithmetic if given seconds. Men like him could make a system out of ash, fear, and a chair.

Caldus saw it.

So did Mara.

So did the guard Caldus had caught.

The young guard, blood running from his split lip, threw his spear.

It did not strike Mordane. It struck the ledger's spine.

The weapon lodged there and pinned the book to the marble floor.

The crowd gasped.

Caldus looked at the young guard.

The guard looked terrified.

"Good," Caldus said.

The word moved through the soldier ranks like a different kind of order.

The coronation was over.

The battle for the city had begun.""",
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
        'current_form: "full-length draft zero with Book One chapters 1-29 revised in pass 01; continuing literary revision needed"',
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
    print(f"Book One chapters 22-29 revised. Word count: {total}")


if __name__ == "__main__":
    main()
