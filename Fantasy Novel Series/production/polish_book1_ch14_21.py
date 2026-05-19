#!/usr/bin/env python3
"""Revision pass 01d for Book One chapters 14-21.

Replaces the Harrowmere/evidence arc with bespoke prose: Tavi's lockwork,
Saelith's complicated mercy, Ilyr's assassination attempt, Caldus's confession,
the royal winter speech, the drowned archive raid, and Mara's decision to turn
proof into rebellion.
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
    14: r"""## Chapter 14: Tavi's Impossible Lock

Tavi Quen was waiting for them at the edge of the goblin market with three bags, two pairs of goggles, one brass cage, and a machine that appeared to have been assembled during an argument with gravity.

"You are late," she said.

Mara looked at the mud on her boots, the blood on her bandage, the dead scholar beside her, the troll behind her, and the goblin guide currently trying to remove a leech from his sleeve with legal language. "Everyone says that. I am beginning to think clocks are against me."

"Clocks are merely honest machines with social expectations." Tavi thrust a leather satchel at Kesh, who caught it badly. "Carry this. If it ticks, put it down. If it sings, throw it away. If it apologizes, run."

Kesh peered inside. "What is it?"

"Rent."

"That seems unlikely."

"It will become rent if I survive."

Narka stood behind Tavi with her red coat buttoned to the throat and her cane across both hands. She had heard everything from the returning party: Old Jaw, the memory moths, Brakka's vow-stone, Arveth's ledger, the pale oathkeeper, Joryn's living face behind wagon bars. The old goblin had not interrupted. She had only tapped one contract ring after another, counting implications.

"The white-thread lock points to Harrowmere's lower road," Narka said. "Not the public gates. Old cinder service access. Gnomish work, crown-owned, badly maintained, spiritually rude."

Tavi brightened. "Almost certainly mine."

Mara stared. "Yours?"

"Not mine personally. My guild's. Possibly my aunt's. Possibly stolen from my aunt by my second instructor, who had flexible ethics and magnificent eyebrows. Hard to say without seeing the gear teeth."

"Can it get us closer to Joryn?"

Tavi's brightness dimmed into something more useful. "It can get us into the network that moved him. If the lock is still keyed. If the crown did not replace the regulator. If the cinder pressure is below lethal. If the whole access tunnel has not become a chapel crypt, which would be inconvenient and aesthetically predictable."

"That was many ifs."

"Engineering is the art of arranging ifs until people mistake them for bridges."

Brakka rumbled approval. "Gnome understands roads."

"Gnome understands liability," Tavi corrected.

They left the market by a dry ridge road at dusk. Narka sent three goblin runners ahead and two behind. Pell, Essa, and Tollen remained with the Kavik healers under protest, which for the dead meant a great deal of silence and one slate message from Tollen: Tell if road needs us. Mara promised she would. The vow warmed when she said it.

Arveth came with them because, as he put it, "The living have demonstrated insufficient competence regarding death."

The old cinder service gate lay under a ruined sheepfold six miles west of Harrowmere. By moonrise, the city could be seen beyond the hills: not the full capital yet, only its highest towers and the constant golden smudge of royal heat above them. Kell Ashgate glowed red and angry. Harrowmere glowed clean.

That made Mara hate it before she reached the walls.

The sheepfold had no sheep, only thorn scrub, fallen stones, and a circular slab set into the ground. The slab bore no handle. Around its edge, brass letters had been hammered flat.

Tavi lay on her stomach beside it and brushed dirt from the seam with a tenderness Mara had seen people reserve for children and weapons.

"Oh," the gnome said.

Kesh leaned over. "Good oh or professionally expensive oh?"

"Family oh."

"Those are rarely good."

Tavi ignored him. Her fingers traced the flattened brass. "Quen regulator pattern. Pre-compact. My grandmother's generation. This was built to vent excess cinder pressure from Harrowmere into the outer heatworks."

Caldus crouched at the hilltop, watching patrol lanterns on the road. "Can you open it?"

"Of course."

"Quietly?"

"That is a different question and an unfair emotional burden."

Mara knelt beside her. The cinder cage hummed softly, almost politely. "What does the lock want?"

Tavi blinked at her.

"What?"

"Roads want weight. Vows want witnesses. Cinders want memory. What does this want?"

For once, Tavi did not answer quickly. She set both palms on the slab. The moonlight caught the copper coils in her hair.

"Recognition," she said at last. "It was built by people whose work is now hidden under royal stamps. It wants the right hands. Or proof that the wrong hands know what they are touching."

She opened her tool roll. Inside were picks, wires, beetle-shell lenses, folded mirrors, wax plugs, a tiny hammer, and three objects that seemed to be only arguments made of brass. Tavi selected the smallest lens and fitted it over her right eye.

"No one bleed on anything."

Everyone looked at Mara.

"That happened once," she said.

"Once is often enough for historical disaster," Arveth murmured.

Tavi worked.

At first, the lock was silent. Then it began to sing. Not with melody, but with pressure tones: high brass, low stone, a little click every seven breaths. Tavi answered with tools. Wire into seam. Tap. Listen. Mirror under ring. Tap. Curse. Beetle lens adjusted. Curse with more ambition.

Mara watched the gnome's face change as she worked. The jokes fell away. Under them was grief sharpened into concentration.

"You said your guild built it," Mara said.

"A lock."

"A service gate."

"A system." Tavi did not look up. "We built systems. Regulators. Venting routes. Pressure valves. Heat balances. You cannot warm a city on cinder without regulation unless you enjoy crater-based urban planning."

"And the crown used it for wagons."

"The crown used roads for wagons. That does not indict cobblestones."

"Does it indict road builders?"

Tavi's wire snapped.

Kesh took a careful step backward.

The gnome stared at the broken wire between her fingers. "My first engine saved a flood town. It pumped water out for two days. Children lived because I made brass obey a problem." Her voice stayed flat, which made it worse. "Three years later, a militia captain bought the pattern and made a trench pump that drowned a siege tunnel with men inside. He wrote me a thank-you letter."

No one moved.

"So yes," Tavi said. "Sometimes it indicts builders."

The slab clicked.

Tavi wiped her face with her sleeve as if she had only sweat there. "Now be impressed."

The circular door opened four inches and released a breath of heat that smelled of iron, old ash, and hidden work.

Then the lock screamed.

Blue light burst around the slab. Tavi jerked backward. Caldus caught her by the belt before she fell into the opening. From below came the sound of gears waking far too fast.

"I said be impressed," Tavi shouted. "Not safe."

The hillside under them trembled. Patrol lanterns on the road turned.

Mara dropped beside the opening, cinder cage clutched in one arm. The lock's scream had words inside it, not human words, but repeated damage: wrong hands, wrong seal, wrong pressure, wrong dead. She could hear names caught in the gear teeth. Not enough to speak. Enough to hurt.

"It thinks we are the crown," she said.

"Can you correct it?" Tavi asked.

"I am tired of correcting old things."

"Yes, but can you?"

Mara placed her bandaged hand on the slab.

The cinder answered at once. Heat ran through her palm, searching for the Venn shape in her blood, the ash-runner exposure, the names she carried. The lock did not want her. It wanted an authorized seal. It wanted a guild hand. It wanted a royal override. It wanted the world to remain arranged as built.

Mara thought of roads that could be challenged.

"Tavi," she said through her teeth. "Put your hand here."

"It may burn."

"Everything may burn."

Tavi pressed her palm beside Mara's.

The lock's scream changed. The old Quen pattern recognized the gnome first, then resisted what that recognition meant. Mara pushed names into the cinder hum: Pell Orwick, Essa Brant, Tollen Reed, Joryn Venn, Lysa Mar, every person moved through systems built by clever hands and claimed by cleaner ones.

Tavi whispered, "I know what you became. Open anyway."

The lock opened.

Not quietly. The entire sheepfold sank two feet, the thorn bushes shook, and every sheep within a mile, if any existed, likely reconsidered agriculture. But the tunnel below lay clear, ribbed with brass, descending toward Harrowmere's hidden heatworks.

Kesh looked toward the road where patrol lights were now running.

"Good news," he said. "We are in."

"Bad news?" Mara asked.

"So is everyone who heard that."

Tavi grabbed her satchel and slid feet-first into the tunnel. "Then stop admiring my work and run through it."

Mara followed, and the door sealed above them just as the first royal shout reached the ruined sheepfold.""",
    15: r"""## Chapter 15: The Pale Envoy

The tunnel under Harrowmere was warmer than blood.

It sloped through the hill in a spiral of brass ribs and black stone, wide enough for carts and old enough that roots had grown through the ceiling in pale, blind fingers. Cinder pipes ran along both walls. Some glowed dull red. Others had gone dark and cold, their brass collars stamped with crown seals over older gnome marks. The air tasted like pennies and fever.

Tavi moved ahead with her goggles down, counting under her breath. Every so often she stopped to slap a pressure gauge or whisper something apologetic to a valve. Kesh followed close enough to complain and far enough not to be assigned labor. Brakka had to walk bent almost double. Caldus took rear guard with Arveth, who claimed not to breathe but still disapproved of the air.

Mara carried the cinder cage. Since the gate opened, the shard had gone restless. It hummed toward Harrowmere, toward the royal heat above, toward whatever systems had taught the capital to glow clean while Kell Ashgate coughed.

"How far?" Caldus asked.

"To what?" Tavi said.

"Anything that is not a tunnel."

"Emotionally or geographically?"

"Tavi."

"Half a mile to the first junction. After that, either lower heatworks, old service vaults, or immediate death by pressure inversion."

Kesh sighed. "I miss when roads merely had teeth."

The first junction had a white light in it.

At first Mara thought it was a lamp. Then the light moved, and pain vanished from her hand.

She stopped so abruptly Brakka nearly walked into her. The bandage around her palm loosened. The torn skin under it closed without heat, without sting, without blood. A scar knitted silver across her knuckles and then smoothed away. For one impossible second, her hand looked untouched.

Mara hated it before she understood why.

"Peace," said a voice ahead.

The woman in the pale cloak stood under the junction arch.

Saelith Dawnmere was not tall in the way Brakka was tall, but she had the kind of height that made rooms reorganize around posture. Her hair was white-gold, braided back from a face too composed to seem young until her eyes moved. Those eyes were gray, not cold, but carefully held away from warmth. A narrow band of light circled one wrist. At her belt hung no sword. Instead she carried a slender rod of white wood, grown rather than carved.

Caldus raised his sword.

The light around Saelith brightened.

"If I meant harm, Sir Renn, you would still be deciding whether to draw."

Caldus went very still. "Do not use that title."

"It is yours."

"Not anymore."

"That is not how oaths work."

Mara stepped between them before old wounds could take over the tunnel. "Where is my brother?"

Saelith looked at her, and Mara felt again that strange double sensation from Stonewake Ford: being examined and seen were not the same thing, and this woman was trying very hard to do only the first.

"Alive," Saelith said.

"You hurt him."

"I prevented a royal interrogator from doing worse."

"By hurting him first?"

Something moved in Saelith's face. Not guilt, exactly. A crack where guilt might grow later if allowed water. "Pain can be redirected. Fear can be quieted. Panic can be kept from opening a mind to rougher hands."

"Did he ask you?"

Silence.

Mara lifted the cinder cage. It hummed once, softly. "Then it was violence."

Arveth made a small approving sound behind her.

Saelith's gaze flicked to him. Her composure thinned. "An Oathbound of Orrowen."

"Witness clerk," Arveth corrected. "Execution survivor. Amateur tea critic. Please keep titles current."

"You should not be here."

"I hear that often from governments."

Kesh leaned toward Tavi. "I like him more every hour."

Saelith ignored them. "Mara Venn, I did not come to return your brother."

Mara's hand closed around the cage handle.

"Careful," Tavi whispered.

"I came to warn you," Saelith continued. "Mordane knows you entered the lower network. He expected you to chase the wagon. He did not expect you to understand the lock so quickly, which means he will adjust. Your brother is being moved to Harrowmere under chapel custody. If you attack the transfer, he will be tagged. If you enter the heatworks blindly, you will be taken. If you continue carrying that cinder fragment openly, every command system below the city will wake around you."

"That was almost useful," Kesh said. "Suspicious."

Mara did not look away from Saelith. "Why tell us?"

"Because Mordane is wrong about what you are."

"And what am I?"

The question made the tunnel listen.

Saelith's eyes lowered to Mara's unscarred hand. She had healed it without permission. Mara curled the fingers, feeling the absence of pain where pain had been earned.

"Dangerous," Saelith said. "But not profane."

"That is your compliment?"

"It is my disobedience."

From somewhere above came a distant clang. Tavi swore and pressed her ear to a pipe.

"Pressure doors," she said. "Someone is sealing junctions."

Saelith turned toward the sound. "Mordane's men."

Caldus stepped closer. "If you are helping, help."

"I already marked the weak point on your brother's binding."

"You also kept him in the wagon."

"Yes."

No excuse. No softness. That made Mara's anger stumble. She preferred enemies who defended themselves badly.

Saelith removed a narrow strip of pale cloth from inside her sleeve. It was the same material that had bound Mara's wrists in the quarry road. This strip, however, had been cut through the center. The severed threads glowed faintly.

"His binding answers to paired pressure," she said. "One line on the door, one on the body. Break one at the wrong moment and the other tightens. Break both together and he can move."

Tavi snatched the cloth before Mara could. "Oh, that is indecently elegant."

Saelith blinked.

"Morally vile," Tavi added. "But elegant."

"Can you open it?" Mara asked.

"With tools, time, and an opportunity during which no one stabs me."

"We can provide two of those," Kesh said.

The tunnel shook again. This time, the cinder pipes dimmed in sequence behind them.

Saelith lifted her white rod and drew a line of light across the junction floor. The air thickened like glass.

"That will slow them," she said.

"Come with us," Mara said.

The words surprised everyone, including Mara.

Saelith's face changed. For one heartbeat she looked young. "I cannot."

"Because of your oath?"

"Because if I vanish now, Mordane tags your brother before midnight. If I stay near him, I can delay."

"Or keep him caged."

"Both can be true."

Mara hated that too. The world had become full of both.

Saelith stepped backward into the white light. "The service junction below the west heatworks holds a drowned archive. Mordane's transfer ledgers pass through it before the palace copy. If you want proof, go there. If you want your brother, you will still need proof, because Harrowmere does not release what it can call mercy."

"Why should I trust you?"

"You should not." Saelith paused. "But you should use what I give you."

The light folded around her.

Then she was gone, leaving only the cut strip of hymn-cloth, Mara's healed hand, and a tunnel full of approaching soldiers.

Mara looked at the smooth skin over her knuckles and felt more violated by its perfection than she had by blood.

Tavi tucked the cloth into her satchel. "We need the archive."

"And Joryn."

"And your hand re-injured, apparently, if you keep staring at it like that."

Mara wrapped the clean hand in its old bloody bandage.

Caldus understood first. He did not comment. He only shifted his sword and nodded toward the left passage.

"West heatworks," he said.

They ran as the white barrier behind them cracked under the first royal blow.""",
    16: r"""## Chapter 16: The Exile at the Window

The west heatworks had been built for maintenance crews, not fugitives, trolls, dead scholars, and arguments.

Its service rooms were narrow and stacked along the underside of Harrowmere like organs the city preferred not to name. Boilers pulsed behind iron doors. Pipes sweated mineral water. Floor grates showed glimpses of red heat far below, where cinder furnaces warmed the capital's upper streets. The city above slept in clean sheets because rooms like this breathed all night under its floor.

Tavi led them through with growing fury.

"That valve is reversed. That gauge is decorative. That pressure line is being used as a drain, which should be a crime with an educational sentence. Who installed this bypass? Who looked at this and thought, yes, I enjoy future screaming?"

"Can you be angry quieter?" Kesh asked.

"Not ethically."

Brakka had remained behind at a fork too small for her shoulders, promising to hold the route and educate pursuers about toll law. That left Mara, Caldus, Kesh, Tavi, and Arveth moving through the heatworks toward the drowned archive Saelith had named. The absence of Brakka's weight made every passage feel less trustworthy.

They reached a rest room above an old dye shop just before dawn. It was not a safehouse. It was an abandoned workers' bunk with three rotted cots, a dry basin, and a window painted shut from the outside. Kesh declared it "safe-adjacent," then wedged three needles in the door and charged everyone for the phrase.

Mara sat under the window with the ledger open across her knees.

Her name remained there no matter how long she stared.

VENN, MARA. Vent runner. Responsive. Do not tag unless authorized.

She had been so certain the vent changed everything. Now she understood the crown had been watching patterns before she knew she was one. Her father. Perhaps others. Families made legible by work, not blood blessed by destiny. Poverty as inheritance. Exposure as lineage.

"You are trying to set the page on fire by glaring," Arveth observed.

"Is it working?"

"Only emotionally."

Tavi sat on the opposite cot, turning Saelith's cut hymn-cloth through her fingers with tweezers. "This binding is not only restraint. It is notification. Break it badly and whoever keyed it knows."

"Saelith?"

"Maybe. Maybe Mordane's chapel ward. Maybe both. Oaths are rude when networked."

Kesh was at the window, listening to the alley below. "Two patrols. One drunk. One pretending not to be drunk because he outranks the first."

Caldus leaned against the door, eyes half closed but not resting. "We leave in ten."

"You said that nine minutes ago."

"Then we leave in one."

The window opened behind Kesh.

It should not have. It had been painted shut. Kesh had checked. Caldus had checked after him because he trusted Kesh's traps and not his conclusions. Yet the frame lifted without a sound, and a narrow blade slid under Kesh's chin.

"Move," said a voice like velvet over ice, "and I correct several mistakes at once."

Everyone froze.

The man in the window was dark-elf, though Mara did not know the proper word yet. He was slender, black-haired, and gray-brown of skin, with silver lines tattooed from the corner of one eye into his hair. His clothes were matte black, not theatrical, but practical in a way that made darkness seem tailored. He held Kesh as if the goblin were a question already answered.

Kesh swallowed carefully. "I prefer written corrections."

"You prefer survival. Be quiet."

Caldus's sword was half drawn.

The blade at Kesh's throat pressed closer. "Finish that motion and the goblin dies first."

"First?" Kesh said. "Unnecessary ordering."

Mara stood slowly.

The dark-elf's eyes moved to her. The cinder cage hummed once.

"Mara Venn," he said. "You are louder than rumor promised."

"Everyone keeps knowing my name. It is getting stale."

"Names do that when carried carelessly."

Arveth folded his hands. "And you are?"

"No one you have authority to ask."

"Ah. Young, then."

For the first time, the assassin's composure flickered. A very small pleasure moved through Arveth's face.

Mara lifted both hands away from the cage. "Let Kesh go."

"No."

"Why are you here?"

"To prevent a catastrophe."

"By cutting throats in abandoned bunk rooms?"

"Methods rarely flatter necessity."

The window behind him showed the alley, pale with dawn. He should not have been able to balance there. He did anyway, one boot on the sill, the rest of him arranged around danger.

Tavi's hand moved toward her tool roll.

"Gnome," the assassin said, "if that is a flash gear, it will blind your friends first."

Tavi stopped. "Criticism accepted under protest."

Caldus spoke without moving. "If you came to kill her, you are wasting conversation."

"I came to decide whether killing her remains the least disastrous option."

Mara almost laughed. She was very tired. "And?"

The dark-elf looked at the cinder cage, at the ledger, at Arveth, at the bloodied bandage Mara had wrapped back around her healed hand. "Complicated."

That was when Mara heard his blade.

Not physically. Not with ears. The cinder shard in the cage resonated toward it, and something inside the steel answered: black halls under roots, a child's hand learning letters by touch in darkness, a court where every spoken truth had to be weighed against who might die if it traveled. The blade held grief like an edge.

"You are exiled," Mara said.

The blade at Kesh's throat trembled.

"Do not," the dark-elf whispered.

Mara should have stopped. She knew the shape of warning. She also knew, suddenly, that he had not come only for her.

"You revealed something," she said. "But not all of it."

His eyes widened.

Caldus moved.

Not toward the assassin. Toward Kesh. He slammed his shield into the window frame, breaking the assassin's balance. Kesh dropped straight down and rolled under the cot with admirable speed. Tavi threw something that became light halfway across the room. The world flashed white.

Mara heard the blade move before she saw again.

She brought up the cinder cage.

Steel struck brass. The cage rang. The shard inside flared black-blue, and the room filled with the smell of root-fire and rain under stone. For one impossible heartbeat, Mara saw the assassin as a boy in a dark hall while a woman with silver tattoos said, Truth is a knife. Carry by the handle and you cut others. Carry by the edge and you learn respect.

The light faded.

Caldus had the assassin pinned against the wall with a shield at his chest. Tavi held a smoking gear. Kesh emerged from under the cot with a knife in each hand and an expression of sincere professional offense.

"I liked this scarf," he said.

The assassin looked at Mara.

No, not at her. At the cage.

"What did you see?"

"A lesson."

"Then you saw nothing useful."

"Who sent you?"

Silence.

Arveth stepped forward. "If you kill her, the cinder network continues waking. If you spare her, it continues waking with a witness attached. I appreciate that both options are terrible, but one is at least informative."

The assassin's gaze sharpened. "Orrowen dead."

"Still current, yes."

"Your empire buried the first record."

"Several of them, badly. I complained at the time."

Caldus pressed the shield harder. "Name."

For a moment, Mara thought he would refuse until violence made the answer irrelevant. Then the assassin exhaled.

"Ilyr Noct-Vey."

Arveth went still.

Kesh looked from one to the other. "That name expensive?"

"Very," Arveth said.

Ilyr's eyes did not leave Mara. "Your gift can wake what my people sealed. The light courts will make you holy. The human crown will make you useful. The dead will make you necessary. All roads end badly from you."

"Then help me build a worse road for them."

That surprised him.

It surprised Mara too, but she liked the shape of it once spoken.

Caldus lowered the shield a fraction. "You trust him?"

"No."

"Good."

"I trust that he knows something everyone else is hiding."

Ilyr smiled, barely. "That is not trust."

"I am new at alliances."

The door needles rattled.

Kesh turned. "Patrol."

The room had no time left for murder, which was becoming a pattern in Mara's life.

Ilyr looked at the window, then at Mara. "Drowned archive. You will die there without a shadow-reader."

"Is that you?"

"Among other regrettable things."

Caldus released him.

Kesh made a hurt sound.

"We are just accepting knife-window into the group?"

"Temporarily," Mara said.

"That is how most stabbings start."

Ilyr stepped onto the sill. "Then follow quickly."

He vanished down the outer wall as the patrol struck the door.

Mara grabbed the ledger and cage. Caldus ripped the needles free. Tavi kicked open a floor vent she had absolutely noticed earlier and absolutely not mentioned. One by one, they dropped into the heat duct below.

Kesh went last, muttering, "If anyone else joins this company by threatening me, I am charging initiation dues."

Above them, the door burst open.

Below, Ilyr's voice floated from the dark.

"Too loud."

Mara, sliding through soot toward another hidden road, decided not to hate him until after he became less useful.""",
    17: r"""## Chapter 17: Saint-General's Letter

Ilyr led them through Harrowmere by shadows that were not always connected to objects.

Mara noticed on the third turn. The first two she blamed on exhaustion, poor light, and the fact that the service ducts under the capital seemed designed by people who hated knees. But the third shadow lay across the floor with no pipe, grate, person, or lantern to cast it. Ilyr stepped into it and was suddenly five paces ahead.

Kesh stopped at its edge. "No."

"It is safe," Ilyr said.

"So are many things immediately before they are not."

"It is safer than the patrol behind you."

"Low bar."

Caldus pushed through first, sword ready. Kesh followed with the expression of a man entering a contract after reading only the most insulting clauses. Mara stepped last, and the shadow folded cool around her. For a heartbeat she smelled wet roots, black stone, and something floral left too long in a sealed room.

Then she was through.

They emerged in the undercroft of a roadside chapel built into Harrowmere's outer wall. The room held old crates, cracked saint statues, and a rack of white candles labeled for plague seasons no one upstairs wanted to remember. Morning light seeped through floorboards above them. Voices moved overhead: priests, soldiers, someone crying quietly into cloth.

Ilyr closed the shadow behind them with two fingers.

Tavi stared. "That violates at least four spatial principles."

"Only surface ones."

"Those are where I keep my tools."

Arveth examined the saint statues. "This chapel predates the current crown."

Caldus's face had gone hard in a way Mara was beginning to recognize. "It predates the mercy wards too."

"You know it?" she asked.

"I know what it became."

Before he could say more, footsteps descended the stair.

Everyone moved at once. Caldus behind a pillar. Kesh under a table. Tavi into a crate that immediately protested in clinks. Ilyr vanished in a fold of shadow. Arveth stood very still beside a saint statue, which was less hiding than professional camouflage.

Mara ducked behind a stack of candle boxes just as a young acolyte entered carrying a silver tray.

On the tray lay a letter sealed in pale wax.

The acolyte set it on a table, wiped his eyes, and whispered, "Forgive me," to no one in particular. Then he fled back upstairs.

Kesh's hand emerged from under the table.

Caldus stepped on it.

Kesh whispered something creative.

Mara picked up the letter.

The seal showed a white branch over a closed eye. Saelith's wrist-light had carried the same shape. The wax was warm though the room was cold.

"Do not break it," Ilyr said from the shadow.

Mara almost dropped the letter.

"Stop doing that."

"No."

Tavi climbed out of the crate with a brass hinge stuck in her hair. "If we cannot break it, why are we gathered so dramatically?"

Ilyr stepped into view. "Because some letters read the reader back."

Arveth leaned closer. "Pale Bough correspondence?"

"Saint-General's office."

Caldus swore.

Mara looked at him. "Who is the saint-general?"

Ilyr answered. "Serathiel of the Pale Bough. Law in armor. Mercy with a blade. A woman who once saved three cities by burning the road between them and the plague."

"That sounds..."

"Effective?" Ilyr's mouth curved without humor. "Yes. That is the trouble with her."

Tavi adjusted her goggles. "I can open a reader seal if someone else is willing to experience mild spiritual trespass."

Everyone looked at Arveth.

He sighed. "Death has made me convenient in several undignified categories."

The process required Tavi's tweezers, Ilyr's shadow over the wax, Arveth holding the letter without breathing, and Kesh insulting the seal whenever it glowed too brightly. Mara watched the closed eye in the wax open once, look directly at her, and close again.

At last the letter unfolded.

The words inside were written in silver ink that shifted between languages. Ilyr read aloud, translating as the lines changed.

"Oathkeeper Saelith Dawnmere. You are instructed to preserve the subject Joryn Venn as leverage only until the ash-runner presents. Do not permit Mordane to tag the brother unless containment fails. The girl is not to be killed without order. If she demonstrates repeat cinder response, she is to be remanded to Pale Bough custody under provisional sanctity."

"Custody," Mara said.

"A lovely word," Kesh said. "Bars with manners."

Ilyr continued. "Human authorities are not to be trusted with long-term containment. Mordane's industrial rites risk premature resonance. The dragon-moon remains sealed. All surface disturbances must be corrected before dark courts notice opportunity."

The room changed around the phrase dark courts.

Ilyr stopped reading.

"Continue," Mara said.

His eyes remained on the letter. "No."

"Ilyr."

"The rest is not relevant."

Kesh brightened. "Ah, a lie. Finally, familiar ground."

Caldus stepped closer. "Read it."

Ilyr folded the letter.

Mara lifted the cinder cage. She did not know what she meant to do with it. Threaten? Listen? Accidentally worsen the entire political structure of the world? The shard inside warmed as if all three were acceptable.

"The letter mentions your people," she said. "It mentions the thing you were afraid I would wake. If you hide that part, you are doing exactly what you accused everyone else of."

Ilyr's face went still.

For a moment, Mara thought he would leave. Instead he opened the letter again and read.

"If Khar Veyl intervenes, invoke the old division. Remind them that the seal holds only while light keeps form and dark keeps silence. Serathiel's hand and witness."

Arveth closed his eyes.

"What does that mean?" Mara asked.

"It means," Arveth said softly, "the split between light and dark elves is not merely cultural."

Ilyr folded the letter with precise fingers. "It is a wound made into government."

"And you were not going to mention that?"

"I was exiled for mentioning less."

That landed harder than his earlier arrogance. Mara saw, suddenly, the shape of him: a man carrying truth like a blade by the edge because every handle had been claimed by someone dangerous.

Above them, bells began to ring.

Not cinder bells. Chapel bells. Warning, not memory.

Caldus moved to the stair. "They found our trail."

Tavi stuffed the letter into an oilskin sleeve. "We need the archive before this becomes a citywide hunt."

Mara looked at the seal, at Ilyr, at the stair where Caldus stood like a man trying not to remember. "This chapel. You know it."

Caldus did not turn. "Yes."

"Is this where..."

"Yes."

No one asked where. The room itself answered: mercy crates, old restraints hidden under candle cloth, a drain in the floor too wide for water alone.

The bells above rang again.

"Archive first," Caldus said.

But his voice had gone thin around an old wound, and Mara understood that the road to proof was about to pass through the place where his disgrace began.""",
    18: r"""## Chapter 18: The Ash-Marked Chapel

Caldus had not returned to the chapel in seven years.

He told them that while leading the way through a passage behind the saint wall, his voice so even that Mara knew each word cost him. The passage had been sealed with plaster and hymn-script; Tavi opened it with two tools and an expression of disgust. Behind the plaster, stairs descended into a darkness that smelled of ash, old blood, and lamp oil.

"I was twenty-four," Caldus said. "Sworn to the Crownreach. Escort detail under mercy seal. Prisoners from fever wards, we were told. Dangerous if frightened. Safer sedated. Safer unvisited. Safer unnamed."

The stairs ended at an iron door.

No one moved to open it.

"Caldus," Mara said.

"Nine were still alive when I understood." He touched the door, not the handle. "Fourteen already tagged. More in the side room. The priest in charge told me I was seeing necessary mercy. He said the crown had enemies, winter had teeth, and the dead owed service because the living had paid for burial."

Kesh whispered, "I withdraw every joke I was about to make."

"The first man I freed could not stand. The second bit me. The third asked whether his daughter had eaten." Caldus's hand tightened. "The priest called guards. I killed him before I knew I had drawn."

"Good," Brakka said.

Caldus shook his head. "Perhaps. But I had escorted two wagons before that night."

Silence pressed close.

Mara thought of Pell saluting him on the bridge. Sir. Not accusation only. Recognition too. "You kept the names."

"Because I did not keep the people."

Arveth stepped beside him. "Records do not resurrect. They do prevent convenient forgetting."

"That is a clerk's comfort."

"It is also true."

Caldus opened the door.

The undercroft beyond had been stripped, but stripping a room did not cleanse it. Scrape marks crossed the floor where tables had stood. Rust stained the wall hooks. A furnace mouth gaped at the far end, cold now, its brick arch marked with ash no broom had managed to remove. Above it, someone had painted over a mercy seal. The new limewash had cracked, revealing the black crown-flame beneath.

Mara's cinder cage went cold.

That frightened her more than heat would have.

The room did not want to remember. Or something in it did not want to be heard.

Tavi moved to the side wall, where brass pipe collars had been hammered flat. "This was a conversion pre-room."

"Meaning?" Kesh asked, though no one wanted the answer.

"Initial sedation. Tag preparation. Command compatibility testing before transport." Tavi's hand hovered over the pipe collars without touching. "These fittings are gnome. Old. Repurposed."

"Everything is repurposed," Mara said.

"No." Tavi looked at her, eyes bright behind goggles. "Some things are betrayed."

Ilyr stood near the furnace, reading marks in soot. "Shadow-scrape here. Someone came after Caldus and removed records."

"Mordane?" Caldus asked.

"Too crude for him. This was someone who feared old evidence, not current blame."

Saelith's letter seemed to grow heavier in Tavi's sleeve.

Mara crossed to the furnace. The ash inside lay smooth, too smooth for a room abandoned seven years. She held the cage closer. The shard did not warm. It dimmed further.

"Why is it quiet?"

Arveth's face tightened. "Ash can be salted."

"Saltwater dampens cinder resonance," Tavi said. "But dry salt worked into ash can mute memory too. Not forever. Long enough."

Mara thought of someone returning here after Caldus fled, salting ash, scraping records, painting mercy over mercy, making the room safer for lies.

"Can we unsalt it?"

Tavi opened her mouth, closed it, then looked at Arveth.

The dead scholar removed one bone plaque from his bracelet. It had no name carved on it. Blank bone, polished by long handling.

"With witness," he said.

Caldus took out the oilcloth packet he had carried for years. The prisoner ledger. His first ledger, not Arveth's stolen copy. The pages were worn, damp-edged, written in the hand of a young knight trying not to shake.

He knelt in the ash.

"Essa Brant," he read.

Mara started. "Essa was at the bridge."

"Her name was here first." Caldus swallowed. "Pell Orwick. Tollen Reed. Marra Kove. Sen Hal. Davi Sorn. Othen Vale. Rusk. No surname. Child, perhaps twelve."

Each name struck the room differently. Not cinder fire. Something smaller. The ash stirred. The painted seal above the furnace cracked wider. Arveth held the blank plaque over the ash, and gray dust rose to cling to it.

Mara joined him.

Not with magic, at first. With voice.

She repeated the names Caldus read. Kesh repeated them after her. Tavi did too, stumbling on one, then correcting herself fiercely. Brakka spoke each name like a stone set into a wall. Ilyr's voice was quiet, precise, foreign around the human sounds and therefore careful. Arveth did not repeat until the end. When he did, the room grew warmer.

The ash lifted.

For one breath, the undercroft filled with shadows of people not fully seen. Hands on table edges. Faces turned away from light. A child clutching a boot. A woman with a miner's braid. A man mouthing a name around a tag not yet sewn.

Caldus bowed his head.

Mara wanted to tell him it was not his fault. That would have been easy, and therefore false. She wanted to tell him it was entirely his fault. That would have been simple, and therefore false too.

Instead she knelt beside him.

"What did the third ask?" she said.

He looked at her.

"The one who asked about his daughter. What was his name?"

Caldus looked back at the ledger. His finger found the line because he had found it a thousand times before.

"Berrit Low."

"Then when we find her, we tell her he asked."

The knight closed his eyes.

Not forgiven. Not absolved. Given work.

That, Mara was learning, was sometimes kinder.

The blank bone plaque in Arveth's hand darkened. Words appeared, not carved but stained: ASH-MARKED CHAPEL, NINE LIVING, FOURTEEN TAGGED, NAMES HELD.

Arveth gave it to Caldus.

"Carry this until you can give it to someone with the right to decide what it means."

"Who has that right?"

Mara stood. "The families."

The cinder cage warmed again.

Tavi moved to the rear wall. "The chapel drain connects to the drowned archive. I can open it."

"Quietly?" Kesh asked.

Everyone looked at Tavi.

"Why do people keep asking me that with hope?" she said.

The first royal boots sounded on the stairs above.

Caldus rose, ash on his knees, plaque in one hand, sword in the other. His face was not healed. It was better than healed. It had direction.

"Open it loudly," he said.

Tavi grinned despite the room.

"Finally," she said, and blew the back wall into the river dark.""",
    19: r"""## Chapter 19: The King's Winter Speech

They reached Harrowmere's public square through a drain beneath the old river wall, which was not how Mara had imagined entering a capital.

She had imagined, if she had imagined anything, gates and trumpets, clean streets, towers white as bone. Harrowmere did have gates. It had trumpets too. She heard both from below while crawling through runoff that smelled of fish rot, hot metal, and human denial. When Kesh pried open the drain grate behind a statue of some forgotten king, Mara emerged on hands and knees into an alley paved with pale stone and nearly vomited on the capital's idea of dignity.

Above the alley, Harrowmere shone.

The city was beautiful in the way a polished knife was beautiful. White stone terraces climbed the hill toward the palace. Heat pipes ran under the avenues, keeping frost from the market tiles. Public fountains steamed gently in the morning cold. Glass lamps burned gold even by daylight. Every balcony had banners. Every banner looked clean.

Mara thought of Kell Ashgate's children coughing silver ash into rags.

"I hate it," she said.

Kesh wrung river water from his scarf. "Give it time. You may find specific reasons."

The square beyond the alley was filling with people. Nobles in fur-lined cloaks stood on raised platforms. Merchants arranged themselves by guild color. Priests moved through the crowd with bowls of white ash, marking brows before the king's winter address. Soldiers guarded the streets in ceremonial armor. None of the dead wore tags where anyone could see.

Caldus pulled his hood lower. "We should not stay."

Arveth looked toward the palace balcony. "We should listen."

"To the king?"

"To what the city believes while being warmed."

Mara wanted the archive. She wanted Joryn. She did not want speeches. But the square had trapped every road around it, and Tavi needed time to trace the archive's lower access. So they became part of the crowd: Mara wrapped in a borrowed cloak, Kesh pretending to be her very rude cousin, Caldus a laborer with bad posture, Tavi a bundle of tools under a shawl, Ilyr a shadow where a shadow had no right to be, Arveth hidden beneath a pilgrim's hood and veil.

Brakka could not enter the square without causing theology, so she waited in the drain and judged the masonry.

The king appeared to cheers.

Mara had expected a monster, which was foolish. Kings did not need to look monstrous. This one looked tired, pale, and expensive. He wore a crown of black iron and gold leaf, the old Harrowmere style, and a cloak so heavy two pages had to manage its train. Beside him stood Lord Cael Mordane, neat and gray and calm, his hands folded as if the entire square were a ledger already balanced.

The king raised both hands.

The crowd quieted.

"Children of Harrowmere," he began.

Mara's stomach tightened. Mordane had used nearly the same opening in Kell Ashgate.

The speech was beautiful. That made it worse. The king spoke of winter roads cleared, border forts supplied, plague wards funded, refugee bread distributed, children warmed in charity houses, old soldiers pensioned, widows paid. He named the crown's mercy. He named sacrifice. He named the dead only once, and then as beloved foundations upon which the living built peace.

The square wept.

Not all of it falsely. That was the horror. A woman beside Mara clutched a ration token and whispered thanks. A man with one arm bowed his head when the king mentioned veteran heat grants. Children cheered because the fountains would run warm through winter. The crown's lies were braided through actual bread, actual heat, actual lives spared by systems fed with other lives stolen.

Mara felt her anger lose its simple shape.

Mordane stepped forward after the king.

He did not raise his voice. He did not need to. The square leaned toward him.

"Mercy," he said, "is not softness. Mercy is structure. Mercy is the courage to count suffering honestly and spend where spending saves most."

Caldus went rigid beside Mara.

Mordane continued. "Our enemies call us cruel because we refuse to let sentiment starve a realm. They call order tyranny because disorder profits them. They call sacrifice murder because they do not have the discipline to ask who lives when hard choices are made."

Mara's hand found Pell's token under her cloak.

"Remember this," Mordane said. "A kingdom is not saved by those who shout that every cost is sacred. A kingdom is saved by those willing to carry cost where others carry outrage."

The crowd applauded.

Mara could barely hear it over the blood in her ears.

Arveth's voice came softly from under the pilgrim veil. "There it is."

"What?"

"The philosophy that makes a person into material without ever admitting the word."

On the balcony, Mordane turned his head slightly.

His gaze moved over the crowd.

Mara knew before his eyes found her that he would. Not because of magic alone. Because she hated him too loudly inside herself, and men like Mordane spent their lives listening for unbalanced accounts.

Their eyes met.

He smiled.

Not surprise. Satisfaction.

"Leave," Caldus said.

Too late.

Soldiers began closing the side streets.

Kesh took Mara's elbow. "I recommend an exit with poor architectural approval."

Tavi pointed across the square to a steaming fountain shaped like a dragon biting its own tail. "Archive sluice under that."

"Naturally," Kesh said. "Public plumbing during a royal speech. Subtle."

Mordane lifted one gloved hand on the balcony.

The ceremonial soldiers drew batons.

Then Brakka came out of the drain.

She did not roar. She simply lifted the statue king beside the alley two inches off its base, decided it was portable enough, and set it down across the nearest soldier line. The crowd screamed. Kesh whooped. Tavi sprinted for the fountain. Caldus shoved Mara after her.

Mara glanced back once.

Mordane remained on the balcony, still smiling as panic broke his perfect square.

He had wanted her to hear the speech. She understood that with sudden cold clarity. He did not only want to capture her. He wanted her to know the argument she would have to defeat.

The fountain dragon's mouth opened when Tavi jammed a tool into its eye.

"Down," the gnome shouted.

Mara dropped into steaming water, carrying Mordane's words with her like poison that had learned to sound reasonable.""",
    20: r"""## Chapter 20: Drowned Archive Raid

The drowned archive lay beneath the public square, under the fountain dragon and the winter speech and three centuries of Harrowmere pretending water forgot what it carried.

It had once been a river archive, Arveth said, back when the city admitted the river existed instead of forcing it through stone lungs. Now it was a flooded vault where old records were kept because dry rooms cost money and wet secrets discouraged casual curiosity. Shelves rose from black water in long rows. Iron walkways crossed above them. Pale crabs moved over ledgers, their shells tagged with scraps of parchment and brass numbering pins.

Tavi loved it for six seconds.

"This is a catastrophic preservation environment," she whispered, delighted and appalled. "Who stores transfer ledgers in moving humidity? Who designed these shelf lifts? Why are the indexing crabs alive?"

One of the crabs lifted both claws as if insulted.

"Sorry," Tavi said automatically.

"Do not apologize to archive crabs," Kesh said. "They remember tone."

Mara stood knee-deep in cold water, trying not to think about what else remembered tone. Above them, the square thundered with panic and soldiers. Below, the archive breathed damp paper, rust, and river weed. Saelith's cut hymn-cloth glowed faintly in Tavi's hand, pointing toward the western stacks.

"Find transfer ledgers," Caldus said. "Fast."

"Fast is not how archives work," Arveth said.

"Then incorrectly."

"That is how governments work. Different craft."

Ilyr moved along the walkway without sound. "There are wards in the shadows."

"Crown?" Mara asked.

"Older."

That word had become less informative and more threatening every time someone used it.

They split because every bad plan eventually did. Tavi and Kesh took the crab index, which involved Kesh bribing one crab with a fish eye and Tavi trying to determine whether it understood filing categories. Caldus and Brakka held the entrance stairs. Ilyr mapped the shadow wards. Arveth led Mara through the western stacks, reading shelf marks that seemed to have been written by a drunk clerk during an earthquake.

"Here," he said at last.

The shelf before them was locked with three seals: royal black wax, chapel white thread, and a pale root mark that made Ilyr stop breathing even though he did not need to.

"Pale Bough," Mara said.

"Yes."

"Can we open it?"

"Certainly. The question is how many institutions we offend."

"All of them."

"An efficient answer."

Arveth pressed one bone plaque to the royal seal. It cracked, not open but listening. Mara held the cinder cage near the chapel thread. The shard hummed, and the thread tightened like a live thing. She thought of Joryn's wrists, of Saelith's fingers on his brow, of beauty becoming restraint.

"Do not pull," Arveth said.

"I was not."

"You wanted to."

"I want to pull many things."

"A charming epitaph."

Ilyr appeared beside them. "The root mark answers to old division."

"What does that mean in useful terms?" Mara asked.

"It expects light to form and dark to silence."

"I hate elf locks."

For the first time, Ilyr smiled like he meant it. "So do elves."

He placed his shadow over the pale root mark. Not darkness exactly. Refusal of being seen. The root seal responded by tightening. Ilyr winced.

"It is hurting you."

"It has practice."

Mara thought of Brakka's vow-stone asking who could challenge her. She stepped closer and put her bandaged hand between Ilyr's shadow and the seal.

"What are you doing?" he asked.

"Being neither light nor dark. It confuses people."

The cinder warmed.

The seal hesitated.

Arveth laughed softly. "Bureaucracy hates unfiled categories."

The three seals opened at once.

Inside the shelf lay ledgers wrapped in oilskin and tied with black cord. Mara pulled the first free. Names. Dates. Mercy marks. Transfer routes. Kell Ashgate appeared again and again. Harrowmere. North heatworks. Crown foundry. Chapel holding. The handwriting changed, but the system did not.

Then she found the page with Joryn.

JORYN VENN. Held under Pale observation. Leverage. Do not process without ministerial order.

Under his entry, in smaller writing: Sister responsive. Father: prior incident. Bloodline exposure useful.

Mara's vision narrowed.

"Mara," Arveth said.

"They knew about my father."

"Yes."

"They let the company call him careless."

"Yes."

"They were watching us."

"Yes."

Each yes landed like a stone. Arveth did not soften them. She was grateful later. In the moment, she wanted to smash every shelf until the river carried Harrowmere's secrets through its own streets.

The water stirred.

Not from her. From below.

Ilyr drew both knives. "Something is coming."

The archive crabs fled first, skittering up shelves with pages clattering on their shells. Then the water between stacks bulged. A pale shape slid underneath, long and jointed, drawn by Saelith's healing thread, by the cinder, by disturbed records, perhaps by the simple fact that no secret enjoyed being stolen without teeth.

Tavi shouted from three rows away. "Do not use healing magic."

"We are not," Kesh yelled.

"Then stop looking wounded near the water."

The predator surfaced.

It had the body of an eel, the forelimbs of a drowned saint statue, and a mouth full of filing pins. Ledger strips trailed from its gills. Someone, at some point, had built wards to keep archive pests from eating records. The wards had taken the suggestion creatively.

"Archive guardian?" Mara asked.

"Indexing error," Arveth said.

The creature lunged.

Ilyr cut its first strike aside. Caldus charged from the stairs and took the second on his shield. Brakka could not fit between the shelves, so she seized the iron walkway above and bent it down into a ramp, creating space through architectural disagreement. Kesh slid under a shelf and came up behind the creature with a crab net. It did not help, but it was brave in a goblin-adjacent way.

Mara clutched the ledgers under one arm and the cage under the other. The cinder shard flared. She heard the creature's hunger: not animal, not evil. It had been made to preserve records. Records were threatened. Therefore everything warm was a thief.

"It thinks we are destroying the archive," she said.

"We are!" Tavi shouted.

"Borrowing."

"With explosions?"

"Not yet."

The creature lunged again, knocking Caldus into a shelf. Ledgers splashed into the water. Mara saw names bleed from ink into black ripples.

Names.

"Arveth, the records."

"I see them."

"No, speak them."

The dead scholar understood instantly. He began reading from the floating pages, voice rising over water and battle. "Lysa Mar. Bek Sorn. Hala Vesh. Orit Dane. Pell Orwick. Essa Brant. Tollen Reed. Joryn Venn."

The creature faltered.

It had been built to preserve records. Spoken names were records too.

Mara joined him. So did Tavi, coughing as she dragged a ledger from the water. Kesh shouted names with terrible pronunciation and absolute conviction. Ilyr read from a page that should have dissolved in his hand but did not. Caldus, pinned against the shelf, found the old prisoner names and spoke them like penance. Brakka's voice rolled from the stairwell, making every name sound carved.

The archive guardian lowered its head.

Tavi threw a flash gear into its open mouth.

The explosion was small, bright, and academically offensive. The creature collapsed into the water, stunned but not dead.

"You said names were working," Mara said.

"They were," Tavi replied, grabbing another ledger. "I improved morale."

The stairs above filled with soldiers.

Caldus shoved the wet ledgers into oilskin. "Out."

"Which way?" Kesh asked.

The archive crabs answered by fleeing through a low tunnel behind the western shelf.

Kesh pointed. "I vote crab."

They followed the crabs.

Mara looked back once as they crawled into the tunnel. The archive guardian had lifted its head again. It did not pursue. It watched the floating pages, listening as the water carried names from shelf to shelf.

For the first time, Harrowmere's drowned records were speaking aloud.""",
    21: r"""## Chapter 21: The Price of Evidence

Proof was heavier wet.

They learned that while crawling through the crab tunnel under Harrowmere, dragging oilskin-wrapped ledgers through mud and roots while soldiers shouted behind them and archive crabs clicked ahead like irritated clerks. The tunnel came out in a cellar under a shuttered dye warehouse near the river steps. Kesh bribed the lock with wire. Tavi bribed it with leverage. Brakka, who had caught up by taking an entirely different route and breaking only one wall, offered to bribe it with finality.

The lock opened for Kesh. Possibly out of self-preservation.

They collapsed into the warehouse among vats of dried indigo and madder root. Everyone smelled of river archive and panic. Caldus barred the cellar door. Ilyr checked the upper windows. Tavi spread the rescued ledgers across dye tables and began counting damage. Arveth stood over her, reading entries upside down with the focus of a man watching his own grave being itemized.

Mara wanted to go north.

No one said she could not. That made it harder.

The ledgers lay between her and the door: proof that Kell Ashgate's dead had been harvested; proof that chapel mercy wagons fed crown foundries; proof that Mordane knew; proof that the Pale Bough had intervened; proof that Joryn had been kept as leverage; proof that her father had not died careless but noted.

Proof, proof, proof.

It did not warm anyone. It did not cut Joryn's bonds. It did not put Pell back at his hearth or Lysa Mar back beside Rella. It only sat there swelling in damp paper, waiting for someone powerful to agree it mattered.

"We take it to the courts," Caldus said, though he sounded as if he hated the sentence.

Kesh snorted. "Which court? The royal court that signs the transfer orders, the chapel court that blesses the wagons, or the merchant court that will ask whether corpses count as labor competition?"

"There are still honest magistrates."

"Name three."

Caldus opened his mouth.

Kesh lifted one finger. "Living, employed, and not currently Mordane's lunch guests."

Caldus closed his mouth.

Tavi did not look up from the ledgers. "We could copy everything. Send packets to guild halls, road clans, troll arches, miners' committees."

"And Joryn?" Mara asked.

The room quieted.

Tavi's pencil stopped.

Mara hated the silence before anyone spoke. It was always where people arranged the gentle version of no.

Arveth saved them from gentleness. "If we run north now, we may reach your brother. We will not keep him. Mordane wants you angry, isolated, and carrying proof no one else has seen. If you trade yourself for him, the ledgers vanish and the foundries continue. Your brother knows this, which is why he told you no."

Mara rounded on him. "Do not use him against me."

"I am using his choice in your favor."

"That is a clerk's trick."

"Yes. Some tricks are useful."

She wanted to slap him. It would have been absurd. He was dead, for one thing, and also right in the most unbearable way.

Brakka sat on an overturned dye barrel. It groaned under her. "Little ash made vow. Names need road. Proof is road."

"Proof is paper."

"Paper can be road if feet follow."

Mara looked at the ledgers again. Joryn's name waited on one page. Her father's on another. Every name in the archive had become a door she could not open alone.

Ilyr stood at the window, watching the street below. "You cannot appeal upward. Mordane holds upward. You appeal outward."

"To whom?"

"Everyone inconvenient."

Kesh's ears lifted. "That is my favorite jurisdiction."

"Miners," Ilyr said. "Goblin roads. Troll arches. Gnome guilds embarrassed by their own fittings. Families of the named dead. Human border towns already losing people. The crown survives because each district thinks its grief is private."

Tavi looked up slowly. "Make the system visible."

"Systems hate that," Kesh said. "Very flattering."

Caldus leaned both hands on the dye table. "Visibility will bring soldiers to Kell Ashgate."

"They are already coming," Mara said.

The sentence came out calm. She felt everyone hear the change in it. She was not less afraid. Perhaps more. But fear had been running in circles inside her all day and had finally worn a road.

"Mordane thinks I will chase Joryn alone because he would," she said. "He thinks proof matters only if power stamps it because that is how he built his world. But Kell Ashgate knows the missing. The road clans know the wagons. The trolls know the bridge. The dead know their names. We do not need one court first. We need witnesses."

Arveth's expression softened.

"Careful," he said. "That was nearly strategy."

"I am horrified too."

Kesh clapped once. "Excellent. Witness packets. I know smugglers, printers, three bad poets, and a woman who can forge a chapel broadside so insulting it becomes theology."

Tavi began sorting ledgers into piles. "I need dry paper, lampblack, gum, rollers, and no one asking why this will take time."

"How much time?" Mara asked.

"Too much. Less if Kesh steals better tools."

"Finally," Kesh said, "my grief language."

Caldus looked at Mara. "This makes you a rebel."

"Was I not already?"

"No. You were a fugitive with evidence."

"And now?"

"Now you intend to move people against the crown."

Mara thought of Mordane on the balcony, telling a warm square that mercy was the courage to spend lives. She thought of the king's tired face, the crowd's real gratitude, the children cheering for heat built from hidden dead. If rebellion meant only tearing down warmth, Mordane would win the argument after all. They needed more than accusation. They needed a way to say no one should freeze and no one should be burned in secret to prevent it.

"Then we do it properly," she said.

Kesh looked delighted. "No one does rebellion properly."

"We do."

Brakka tapped the vow-stone tablet at her throat. "Begin with terms."

So they wrote terms in a dye warehouse while Harrowmere searched for them.

Not a manifesto. Mara refused that word when Arveth offered it, because it sounded like something written by people who enjoyed hearing themselves become history. They wrote witness claims. Names. Routes. Seals. Demands. Return the living held under mercy custody. Identify the dead used in crown labor. Open the foundries to family witness. Suspend cinder-command production. Let every district audit its heatworks. Let the dead be named before any crown called them service.

With each line, the thing became larger than Joryn.

That hurt.

Mara wrote his name anyway.

Near midnight, the first packets left the warehouse. Goblin runners took three. A troll courier took one for the Seven Arches, rolling it into a stone tube as if paper were something that needed armor. Tavi sealed copies for Brassroot guild contacts who would deny knowing her until guilt made them curious. Ilyr took one written in cipher for dark-elf eyes. Arveth copied the names of the dead in a hand so precise it looked like judgment.

Caldus kept the original prisoner ledger.

Mara noticed.

"You do not have to carry it alone anymore," she said.

He looked down at the oilcloth packet, then at the new copies spreading across the table. "I know."

"But you will."

"For now."

That was honest enough.

At last Mara stood at the warehouse window and looked north. Somewhere beyond the city, Joryn was still bound. Perhaps Saelith delayed his tagging. Perhaps Mordane waited. Perhaps every hour made rescue harder.

She pressed her palm to the glass.

"Hold on," she whispered again.

This time, she did not promise to come alone.

Behind her, the presses began: soft thump of ink, paper, witness, paper, witness, paper. Not bells. Not yet. But a rhythm the crown had not written.

By dawn, Harrowmere would wake to names on its walls.

And Kell Ashgate would know it had not been grieving by itself.""",
}


EXPANSIONS: dict[int, str] = {
    14: r"""The tunnel did not feel like rescue once the slab sealed.

The dark swallowed the last royal shout, then gave it back in pieces. Voices passed through the brass ribs overhead, stretched thin by stone and distance until they sounded like ghosts arguing inside a wall. Dust sifted down. Tavi lay flat with one ear pressed to a pipe and one hand lifted for quiet. Her goggles glowed green at the edges. In that strange light, the whole tunnel became a rib cage around them, each curve sweating heat.

"Six soldiers," she whispered. "No, seven. One has a limp. One is pretending not to panic. One is the sort of man who says stand clear before doing something stupid."

Kesh crouched beside her. "Can your pipe truly tell you all that?"

"No. The pipe tells me feet. Experience tells me stupidity."

Above them, metal struck the sealed door. The whole tunnel rang.

Brakka grimaced. "Loud little hammer."

"It is a breaching spike," Caldus said.

"Then it is a loud little spike."

Mara wanted to laugh because laughing would have been easier than kneeling in the hot dark with the royal road above and Joryn somewhere ahead of her, still alive only because enemies had uses for him. The cinder cage pulled at her hands. Not hard. More like a child tugging toward a familiar door. She tightened her grip and felt the hum through the bones of her arms.

Tavi looked at the cage, then at Mara. "Do not answer it in here."

"I am not doing anything."

"That is usually when machines begin making requests."

The breaching spike struck again. This time the sealed slab did not ring. It groaned.

Tavi scrambled upright. "Good news, the door is stubborn. Bad news, whoever built the royal breaching spike understands Quen counterteeth."

"Family again?" Kesh asked.

"Worse. Student."

She took off down the tunnel at a run too quick for her short legs to make sense of. Mara followed with Caldus close behind. Brakka moved last, shoulders scraping brass, her maul dragging sparks where stone narrowed. Arveth kept pace without effort, which was irritating in a dead man and useful in a witness.

The service tunnel sloped under the hill in long smooth sweeps. It had once been beautiful. Mara could see that even through the heat-haze and cinder grime. The brass ribs were engraved with tiny repeating leaves. The floor tiles fit so tightly no mud grew between them. Every fifty paces, a service niche held a porcelain-faced gauge, a hand pump, and a little enamel plaque naming the maker. Crown seals had been hammered over most of the plaques, but the older letters still showed around the edges like teeth under a mask.

Tavi slowed at each niche just long enough to read what remained.

"Quen. Vale. Briarwick. Quen again. Oh, Grandmother, what did they do to your beautiful redundancies?"

"She speaks to dead machinery more tenderly than she speaks to me," Kesh observed.

"Dead machinery keeps better promises."

At the fourth niche, Tavi stopped so suddenly Mara nearly stepped on her.

The plaque there had not been covered by a crown seal. Someone had tried and failed. The stamp lay cracked on the floor, split clean through. Beneath it, the maker's mark remained: a round door under three stars.

Kesh drew a small breath. "That is the mark from Pell's road token."

Mara touched the token at her collar. "The curved road under three dots."

"Not road," Tavi said. "Rail."

She brushed soot from the plaque. More letters emerged.

Auxiliary Transfer Junction. Living freight prohibited without consent. Quen Safety Covenant, Article Nine.

No one spoke for a moment.

Caldus read the line twice. "Living freight."

"The covenant forbade it," Tavi said. Her voice had gone flat. "The old gnome guilds built service rails for fuel, ash, pressure vessels, emergency evacuation. No living cargo without consent, witness, and return route. Article Nine. Everyone learns it. Children learn it. We put it in nursery puzzles because our ancestors were very proud of having ethics after needing them badly."

Mara looked down the tunnel. "And the crown used it for mercy wagons."

"The crown used it after it scraped off the names of the people who made the warnings."

Tavi opened the gauge housing with fingers that shook. Inside was no pressure gear. Someone had hollowed out the box and fitted it with a small crystal reader veined in white.

Saelith's light.

Arveth leaned close. "A pairing sensor. One mark on the gate. One mark on cargo."

Mara thought of Joryn behind wagon bars, shoulders tense, shaking his head at her. She had understood his no as love. Now she understood another piece of it. A wrong rescue would have tightened the hidden system around him.

"Can we break the line from here?" she asked.

Tavi did not answer at once. She took out the cut strip of hymn-cloth Saelith had given them and held it near the crystal. The threads lifted toward the reader like grass toward light.

"Not break," Tavi said. "Teach it a different song."

"Will that free him?"

"It might make the system believe the body-mark is already accounted for. It might make the door half-blind when we reach him. It might also convince every pressure lock in Harrowmere that we are a cart full of unauthorized sacred laundry."

"Is that better or worse than now?"

"Different disasters are a form of variety."

The breaching spike struck far behind them. A crack answered through the sealed door.

Caldus looked back. "We are out of time."

"We are in engineering," Tavi said. "Time is something people say when they do not understand tolerances."

She sat cross-legged in the tunnel, set the hymn-cloth on her knee, and began unmaking the crystal reader. Kesh watched the dark behind them. Brakka planted her maul in the floor and listened to the soldiers. Caldus kept looking between Tavi and Mara as if deciding which of them needed saving most and resenting the lack of a clear answer.

Mara knelt beside Tavi. "Tell me what to do."

"Hold the cage near the reader. Do not open it. If the cinder speaks, do not answer in words. Think names. Specific ones. Living ones first."

"That sounds like answering."

"It is the difference between conversation and throwing furniture through a window. Very important."

Mara lifted the cage.

The cinder woke.

Not fully. Not like the vent. Not like Old Jaw, where memory moths had turned every confession into weather. This was a small waking, intimate and worse for it. The shard pulsed blue-white behind its brass mesh, and Mara felt the old pressure in her mouth, the sense of a word waiting behind her teeth that was not her own.

Venn.

She did not say it.

She thought Joryn instead. Joryn teaching her to count breaths under a table while their mother wept quietly in the other room. Joryn stealing a second heel of bread from a supervisor's lunch pail and then blaming a rat with political motives. Joryn standing in the wagon and refusing to let her be turned into someone else's weapon.

The white threads in Tavi's hand darkened at their severed ends.

"Good," Tavi whispered. "More."

Mara thought Pell Orwick, who had saved a goblin aunt in flood year and died under a company stamp. Essa Brant, who had hummed in a drain so command could not take the dead again. Tollen Reed, whose slate messages had more courage than most speeches. Rella of the alley, Niv with his runny nose, Dilla in her tallow shop. Her father. Her mother. The names came faster than fear could file them away.

The crystal reader chimed.

Tavi slid a wire through the hymn-cloth and tied it with a knot so small it looked like a mistake. "There. I changed the handshake."

"The what?"

"The polite lie machines tell each other before betrayal."

Behind them, the sealed door gave way with a shriek.

Royal light poured into the far bend.

"Run," Caldus said.

They ran again, but now the tunnel answered differently. Gauges fluttered as Mara passed. Old maker marks glowed under crown stamps, not with rebellion, not with miracle, but with recognition. Hidden routes branched to either side, thin lines of blue-white tracing themselves through dust: one toward lower heatworks, one toward the west archive, one toward the palace transfer vault.

For one dizzy heartbeat, Mara understood the service network as a body.

Harrowmere was not simply a city above them. It was a sleeping beast of pipes, locks, ledgers, and lies. Its clean lamps, its public fountains, its warm chapels, its bright squares, all of them were fed by hidden throat-roads like this one. And under every crown seal, there had once been a warning.

"Tavi," Mara said.

"I see it."

"All of it?"

The gnome's face was pale behind her goggles. "Enough to be afraid."

The tunnel forked ahead. A pressure door on the right stood open a hand's breadth. White light breathed through the gap.

Saelith's warning had been true. West heatworks. Drowned archive.

The soldiers behind them rounded the bend.

Brakka turned, put one hand against the ceiling to brace herself, and struck the nearest brass rib with the butt of her maul. The tunnel roared. Steam exploded from a relief pipe between the party and the soldiers, turning pursuit into a wall of white.

Tavi made a wounded sound. "That was a historical rib."

"It had history," Brakka said. "Now it has purpose."

Mara ducked through the half-open door and into the white-lit junction beyond. The air changed at once. It smelled of winter linen, clean water, and something too bright to trust.

The pale envoy was waiting ahead, exactly where an enemy would stand if she wanted to be mistaken for help.""",
    15: r"""The west passage became narrow enough that Brakka had to turn sideways and the others had to pass single file between pipes sweating hot mineral water. The white barrier behind them cracked twice, then held, then cracked again with a sound like ice breaking on a lake too deep to swim. Saelith's light did not fail all at once. It thinned. That was worse, because every footstep behind them arrived through the dying wall in fragments: boots, orders, a captain's curse, metal teeth grinding into stone.

Mara flexed the healed hand inside the old bloody bandage.

The skin did not pull. The nerves did not flare. Her body had accepted Saelith's mercy with the treacherous obedience of flesh. She could grip the cinder cage without pain now. She could run farther, climb faster, fight better. The gift was useful.

That was what made it feel dirty.

Caldus noticed her looking at it again. He kept his voice low. "Healing without leave is still a trespass."

"Knights have rules for everything."

"Not enough. That was the problem."

The answer should have opened a door to questions. Mara did not have breath for them. Tavi was ahead, muttering to the hymn-cloth strip as if it were a rude apprentice. Kesh had dropped back beside a pressure vent and was laying tiny black seeds along the seam.

"What are those?" Mara asked.

"Insurance."

"Against what?"

"Anyone allergic to explosive mushrooms."

"Are soldiers usually allergic?"

"Everyone is allergic eventually."

He pressed the last seed into place and spat on it. The seed twitched, sprouted a hair-fine root, and vanished into the brass seam.

The tunnel opened into a maintenance gallery above a river of light.

Mara stepped to the grated edge and nearly lost her balance. Thirty feet below, molten cinderwash moved through a stone channel, not flame exactly, not water, but a thick amber glow full of slow sparks. Great wheels turned in it. Chains rose from the wheels through the floor into the city above. Every rotation sent warmth upward. Every rotation made the streets over their heads survivable.

On the far wall, workers in gray heat masks monitored gauges from narrow walkways. Human, gnome, a few goblins, and one troll with a shaved head and burn scars across both arms. They were not soldiers. They did not look enslaved. They looked tired, paid, and careful. One woman adjusted a valve with the gentle precision of someone keeping a child alive.

Mara's anger faltered.

Tavi saw it and nodded without satisfaction. "This is the part Mordane shows visitors."

"It is not false."

"No. That is why it works."

Below, a bell rang twice. Workers moved in practiced lines. A small crack opened in a side gate and a cart rolled through, covered in white canvas. Two chapel attendants walked beside it, their faces hidden by masks sewn with pale thread.

Mara froze.

"Is that Joryn?"

Tavi adjusted her lens. "Too small for a person. Ash canisters."

"Or pieces of one," Arveth said.

No one thanked him.

The cart stopped at a receiving lock. One attendant placed a hand on the white thread panel, and a series of brass arms unfolded from the wall. Each arm carried a needle. They pierced the canvas and withdrew shining with black-gray dust. The gauge above the lock flared green. Approved.

Mara understood what she was seeing before she had words for it.

"They test the dead like ore."

"Like fuel," Tavi said.

Below, the worker with the burn-scarred arms looked up. Not at the attendants. At Mara's gallery. His eyes widened for one second, then slid away.

Kesh's hand moved to his knife. "He saw us."

"He did," Caldus said.

"And he did not call."

The troll worker lifted one wrench and tapped the valve beside him three times, paused, then once. Brakka went very still.

"Bridge code," she rumbled. "Danger near. Old code."

"Can you answer?"

Brakka took the edge of the grating in one hand and struck it twice with one tusk ring. Metal answered down the gallery, soft enough to pass for stress in the pipe.

The worker returned to his gauge.

"What did you say?" Mara asked.

"Names coming."

Tavi swallowed. "If heatworkers are already warning each other, Mordane's control is thinner than it looks."

"Or they are bait," Kesh said.

"Both can be true," Mara replied, and hated that Saelith had given her the phrase.

They moved along the upper gallery. The floor vibrated under each step. Through breaks in the masonry, Mara glimpsed Harrowmere above: a laundry courtyard steaming in clean morning air, a schoolroom where children practiced letters beside a heat pipe, a bakery with golden loaves cooling on racks, a chapel infirmary where an old woman slept under a warmed blanket. None of those people looked monstrous. None of them had chosen Pell's death. They had only accepted warmth from a system built to keep them from asking what it burned.

The cinder cage hummed softly, and Mara thought of Mordane's argument before hearing him make it: would she freeze those children for truth? Would she crack the city open and let winter pour in because her grief was righteous?

She nearly hated him more for being able to ask a good question with rotten hands.

At the gallery's far end, a narrow bridge crossed the cinderwash. The bridge was folded up against the wall and locked with three separate mechanisms: brass, white thread, and an old oath-stone tablet bolted through the hinge.

Tavi knelt. "Oh, this is just rude."

"Can you open it?" Caldus asked.

"Yes."

"Quietly?"

She looked at him.

"Habit," he said.

"I can open the brass. Mara can confuse the thread. Brakka can speak to the stone. Kesh can do whatever criminal grooming makes him feel included."

"I can hear respect under that."

"That is your illness."

The white barrier behind them shattered. A pressure wave rolled down the gallery. Workers below shouted. Soldiers spilled into the far end of the maintenance level, batons drawn, crossbows lifted.

"Now would be a useful time," Arveth said.

Mara lifted the cage to the thread lock and thought Joryn, Joryn, Joryn until the cinder hum became a pulse in her teeth. Tavi's fingers blurred inside the brass housing. Brakka pressed her forehead to the oath-stone and spoke in a language older than bridges. Kesh flung something tiny and glassy over his shoulder.

The first crossbow bolt hissed past Mara's ear.

Caldus stepped in front of her shield-first. The bolt struck iron and spun away.

Kesh's glass bead broke at the soldiers' feet. Black mushrooms bloomed across the grating in a sudden slick carpet. Boots went out from under men. A captain fell with so much armor dignity that the crash sounded expensive.

"Allergic," Kesh announced.

The bridge dropped.

Not gently. It slammed across the cinderwash, bounced once, and settled with a groan. Workers below scattered from the spray of sparks. The troll heatworker with the scarred arms looked up again and touched two fingers to his brow. Brakka returned the gesture.

Halfway across, Mara glanced down.

The cinderwash below was full of faces.

Not bodies. Not ghosts as chapel paintings made them. Faces made from heat and memory, rising in the amber flow, vanishing before she could name them. Some screamed. Some slept. One turned toward her and opened a mouth that shaped no sound.

She would have stopped if Caldus had not pushed her between the shoulders.

"Move."

They reached the far side as royal soldiers recovered behind them. Tavi struck the bridge release with her wrench. The span folded back up, taking two pursuing men with it until they threw themselves onto the near platform and clung there shouting.

The party plunged through a low arch marked West Service. Beyond it, the noise of the heatworks dulled at once. The air went cooler. Damp replaced metal. Somewhere below, water moved in patient darkness.

Tavi held up Saelith's cut cloth. The severed threads pointed down.

"Drowned archive," she said.

Mara looked back once through the arch. The heatworks continued turning. Workers returned to their valves. Warmth kept climbing into Harrowmere.

Proof would have to be more than accusation. It would have to answer what came after.

She did not know how yet.

The healed hand inside its bloody bandage closed tighter around the cage, and for the first time since Saelith touched her, Mara was grateful for the strength without forgiving the gift.""",
    16: r"""The heat duct below the safehouse did not deserve the dignity of being called a road.

It was a rectangular throat of soot and old grease barely wide enough for Mara to slide on her elbows. Hot air pushed from behind in uneven gusts. Somewhere below, a fan thumped with the tired rhythm of a failing heart. Tavi went first because she claimed she could smell dead ends. Kesh followed, claiming the same gift with people. Mara came after with the ledger strapped flat under her coat and the cinder cage bumping painfully against her ribs. Caldus was last for several miserable yards until the duct narrowed and forced him to remove his shield, curse softly, and drag the thing beside him by its strap.

Ilyr Noct-Vey moved outside the duct.

That was the only explanation Mara would accept. Whenever they reached a grate, he was already beyond it: a pale shadow crossing a laundry roof, a dark hand signaling from a gutter, a pair of violet-black eyes in a chimney alcove. He had attacked them, explained very little, and then appointed himself guide with the confidence of someone who had never asked permission and would have found it vulgar.

Mara did not like him.

She liked less that he was good.

At the third grate, Ilyr lifted one finger for silence. Tavi stopped so suddenly Kesh's nose hit her boot.

"I am wounded," he whispered.

"Emotionally or profitably?" she whispered back.

Ilyr pointed through the grate.

Below them lay a dye court open to the gray sky. Strips of blue cloth hung from lines like drowned banners. Two royal search parties moved between vats with lanterns raised, checking doors, crates, drains. One soldier carried a white-thread reader, its needle sweeping slowly from side to side. Another held a wanted notice protected from drizzle in waxed paper. Mara saw the crude sketch of her own face and was offended by the chin.

"That is not my chin," she whispered.

Caldus, behind her, made the smallest possible sound of disbelief.

The reader needle swung toward the duct.

Ilyr's hand moved once.

A line of shadow detached from the roof, fell soundlessly behind the soldier with the reader, and became Ilyr. He touched two fingers to the reader's crystal. It went black. The soldier turned. Ilyr smiled politely, struck him behind the ear, caught him before he splashed into a dye vat, and lowered him to the stones. The whole thing took less time than Mara needed to decide whether she was impressed.

The second soldier saw movement.

Caldus kicked the grate open.

That was not quiet, but it was clear.

Mara dropped into the court with hot soot in her hair and the cage in one hand. Kesh landed beside her on both feet and stole a lantern from a soldier who had not yet realized a fight had started. Tavi rolled under a vat spigot, came up with a wrench, and hit a man's knee hard enough to make engineering sound personal. Caldus descended in armor like a bad decision made by a staircase, shield-first, knocking two soldiers into a vat of blue dye.

Brakka was not with them. She had taken another route after the heatworks because the ducts had been built by people with insufficient respect for shoulders. Mara had not realized how much safer the troll made a space feel until she was gone.

Ilyr fought like grammar.

Every movement made the next one inevitable. A wrist turned, a baton missed, a boot slid, a blade pressed against a strap instead of a throat, and an armed soldier became an embarrassed obstacle. He did not kill. Mara noticed that, because she had expected him to. Dark-elf exile, blade-scholar, assassin sent to stop her. The words had arranged themselves into something simple in her mind. Ilyr refused to move simply.

One soldier lunged at Mara while she was watching him.

The healed hand moved before thought. She caught the baton, twisted, and felt the man's fingers open under leverage she should not have had yesterday. The bandage around her palm came loose. Smooth skin flashed white in the rainy court.

The soldier stared.

"Saint's mark," he breathed.

Mara punched him with the cinder cage.

He went down.

The cage rang. The cinder answered. For one wild second the dye court filled with whispers from under Kell Ashgate: old vents, broken chains, Joryn's no, Pell's name, the faces in the cinderwash. The cloth strips overhead snapped in a wind no weather had sent.

Ilyr caught Mara's wrist.

"Do not bloom here."

She almost struck him too. "Let go."

"If the cinder wakes fully in a city of pipes, everyone above us hears you."

"Good."

"Mordane hears you first."

That landed.

Mara shut her fingers around the cage handle until the hum became pain and the pain became hers. The whispers retreated. Rain began sounding like rain again.

Tavi shoved the unconscious reader-soldier under a hanging cloth. "We need to leave before someone wonders why the laundry is winning."

Kesh had already found the court's side gate. "This way goes to the rag market, then the old bellstairs, then a cellar where my cousin once lost a lawsuit and a boot."

"Is that a safe route?" Caldus asked.

"It is a route."

Ilyr wiped rain from his blade with the edge of a royal cloak. "No. The rag market is watched. They expect goblin habits."

Kesh stiffened. "My habits are a jewel box of personal artistry."

"They are documented by three governments."

"Slander with footnotes is still slander."

Ilyr pointed toward an upper walkway half hidden by blue cloth. "There. Dye guild counting room. It connects to the chapel storehouses."

Mara eyed him. "You know Harrowmere too well for someone exiled from under it."

"I was not exiled from Harrowmere."

"Then why are you here?"

He looked at her through rain and hanging cloth. For the first time since the attack, the clever edge went out of him. What remained was older, not in years, but in grief.

"Because the dead of Orrowen were counted here before they were moved," he said. "Because my sister's name appears in ledgers your crown claims do not exist. Because the light courts decided patience was virtue and the dark courts decided secrecy was strategy, and both are words people use when someone else is being burned."

Arveth, who had been securing the ledger under his coat with dreadful calm, looked up.

"Your sister?"

Ilyr's jaw tightened. "Maelin Noct-Vey."

Arveth closed his eyes.

"You know her," Ilyr said.

"I wrote her intake line."

Rain tapped the vats. For a moment the whole court seemed to wait for the next kind of violence.

Ilyr stepped toward him. Caldus moved between them, not drawing his sword, which was wiser than Mara would have managed.

"Where was she sent?" Ilyr asked.

Arveth opened his eyes. "I do not know. That is why I still walk."

It was the wrong answer and the only honest one.

Ilyr's face did something Mara recognized because she had felt it in her own bones: the mind trying to keep grief shaped like anger because anger could stand.

"Then you will help me find out."

"Yes," Arveth said.

No oath. No performance. Just yes.

The side gate rattled. More soldiers were coming.

Mara grabbed the waxed wanted notice from where it had fallen near the dye vat and stuffed it into her coat.

Kesh stared. "Collecting flattering art?"

"Proof they are hunting me."

"Your face looks like a suspicious potato."

"Then it is proof of slander too."

They climbed the upper walkway as the gate burst inward. Crossbow bolts punched through blue cloth. Dye vats shattered. Indigo ran across the stones like spilled night. Mara looked down once and saw the soldier she had struck stirring, alive. She was glad. Then she was annoyed she had time to be glad.

Ilyr led them through the counting room, past ledgers of dye lots and wages and merchant debts. He stopped at a small wall shrine beside the door: two candles, a bowl of salt, and a painted leaf of the Pale Bough. Someone had scratched a different symbol into the wood below it: a crescent under a buried star.

Ilyr touched it.

"Dark-elf mark?" Mara asked.

"A promise that light is not the only witness."

The cinder cage warmed.

For a heartbeat, Mara saw not the room but a black forest beneath a silver-rooted city, children learning blade forms between mushroom lanterns, an elder singing names into a bowl of water, a white army at the border, a treaty table where every chair had a knife under it.

Ilyr saw her see it.

"Cinder-singer," he said softly.

"Do not say that like you know me."

"I know what waking memory costs."

"Then stop giving me more."

"I am trying to stop the world from giving you everything at once."

The honesty of that irritated her because it sounded almost kind.

They escaped the counting room through a trap in the floor and slid down a laundry chute into a cart of wet blue cloth. Kesh emerged first, hair dyed at one temple. Tavi followed, sneezing. Caldus landed with the dignity of a collapsed tower. Arveth simply stood up from under linen as if being buried in laundry were a clerical inconvenience.

Ilyr came last and closed the trap above them.

Mara looked at him over the rim of the cart. "If you betray us, I will know."

"No," he said. "You will suspect. There is a difference."

"Fine. I will suspect hard."

His mouth twitched. "Acceptable."

The cart rolled out into a narrow alley as bells began ringing two districts over. Ahead, above a row of roofs black with rain, Mara saw the chapel spire marked in ash and gold.

Caldus saw it too.

His face changed before he could hide it.

Whatever waited there was not only evidence. It was memory with doors still locked.""",
    17: r"""The room above the chapel storehouse had once been a choir school.

Mara knew because the walls still bore painted scales and old children's handprints in gold ash. Someone had scrubbed away the song titles, but not well enough. Under the new whitewash, little black letters showed where warm hands and poor brushes had once named morning hymns, winter blessings, bread songs, wake songs. Now crates stood where benches had been. Mercy blankets lay folded in stacks. White-thread cuffs hung from wooden pegs in sizes from adult wrist to child.

No one touched those pegs.

Caldus stood near the door with his back to them. Since reading the Saint-General's letter, he had become a man walking inside armor older than steel. Mara had seen him afraid before. She had seen him ashamed, angry, stubborn, tender in quick accidental flashes. This was different. This was recognition.

Tavi worked at a locked cabinet in the corner. "The letter is not just a threat. It is routing authority. Saint-General Serathiel's seal overrides chapel custody, royal custody, and most medical objections. If this is real, the Pale Bough can take Mara from Mordane without calling it kidnapping."

"Comforting," Kesh said. "I adore being fought over by institutions."

"You are not the one they want."

"A familiar wound."

Ilyr took the letter from Tavi and held it near the window. The pale seal caught the rainlight, and hidden script rose around the edge like frost.

"Real," he said.

Saelith had not followed them. That did not make Mara feel alone. It made every white corner seem capable of becoming her.

"What does Cinder Saint mean?" Mara asked.

The others looked at Arveth.

The dead witness clerk folded his hands. "The phrase is older than the current doctrine. During the first cinder wars, people who could hear buried dragon-hearts were sometimes used to calm broken fragments, redirect heat, identify dangerous seams. Some were revered. Some were chained. The difference depended on who wrote afterward."

"And now?"

"Now the church pretends the practice ended."

Tavi shut her eyes. "That is never a good sign."

"A saint is allowed no private will once declared necessary," Arveth continued. "Every refusal becomes selfishness. Every injury becomes offering. Every exhaustion becomes proof of devotion. It is one of the cleanest cages ever invented."

Mara thought of Saelith healing her hand without permission. Useful. Beautiful. Wrong.

"They can dress me in white and call it mercy," she said.

"Yes."

The word settled colder than the rain.

Caldus turned at last. "They will need a knight to escort you."

Mara looked at him. "That sounds specific."

His mouth tightened.

Kesh, who was often foolish in wise ways, said nothing.

The bells above rang again. Not alarm bells. Chapel bells. Three slow notes, each one so pure it made the storehouse cuffs seem even uglier.

Caldus walked to the nearest peg and lifted a child's white-thread cuff between two fingers. His hand trembled.

"I was twenty-three," he said. "Not old enough to know youth is not innocence. Old enough that not knowing was no excuse."

Mara did not move.

"The king's Mercy Reforms were new. Border fever had taken three towns. Cinder accidents were rising. The court said the chapel had found a way to preserve those who could still serve after death. Not undeath, they said. Continuance. Honored labor. Temporary, witnessed, blessed."

Arveth's face had gone still.

Caldus kept looking at the cuff. "My unit escorted the first mercy transports from Orrowen through Harrowmere. We were told the passengers were already legally dead. We were told their families had consented. We were told inspection would profane the rites."

"Did you believe them?" Mara asked.

"Yes."

She hated him for the answer. She also needed him to keep speaking.

"At the Ash-Marked Chapel, one crate began knocking. Not from the outside. From within. A captain said residual motion was common. A priest said a body may resist kindness after the soul departs. I ordered the line to continue."

The room seemed to shrink.

Ilyr's hand moved to his blade, then stopped. Arveth did not blink.

Caldus's voice became very quiet. "A girl inside said her name."

No one asked which girl.

Ilyr did not breathe.

"I heard her," Caldus said. "I knew I heard her. I looked at the captain. He looked at me. The priest began singing louder. I let the wagon roll ten more paces."

Mara felt the cinder cage warm against her hip.

"Then?"

"Then I stopped it."

Ilyr moved so quickly Caldus had no time to defend himself. The dark-elf blade touched the hollow under Caldus's jaw.

"Ten paces," Ilyr said.

"Yes."

"Her name."

Caldus closed his eyes. "Maelin Noct-Vey."

The blade pressed harder. Blood showed.

Mara stepped forward, but Arveth raised one dead hand.

"Let him finish," the clerk said.

Caldus opened his eyes. He did not look away from Ilyr. "I broke the wagon seal. Maelin was alive. So were three others. The captain ordered me arrested for sacrilege. My own men hesitated. I hesitated too, which I will carry longer than any scar. Then Maelin bit the priest hard enough to free a hand, and the choice became easier."

Ilyr's blade shook once.

"She lived?"

"Through that hour."

The room broke around the answer without making sound.

Caldus continued because stopping would have been mercy for himself. "We freed six. Lost two. The captain killed one at the chapel door. Maelin ran with the others into the lower drains. I held the stair until the city guard arrived. By then the surviving transports were gone. The court stripped my crest, sealed the inquiry, and declared the recovered bodies fever-mad. I was told I could keep my life if I kept silence."

Ilyr lowered the blade by the width of a breath. "Where did she go?"

"I do not know. I searched after exile. Not enough. Never enough."

"Why did you never tell this?"

Caldus gave a small, ugly smile. "To whom? The court that sealed it? The chapel that sang over it? The families I could not find? Myself, until I believed confession counted as repair?"

Mara heard her own anger shift shape. It did not disappear. It became something with edges better suited to use.

"You should have spoken anyway," she said.

"Yes."

"Earlier."

"Yes."

"Louder."

"Yes."

Ilyr stepped back and sheathed his blade with visible effort. "If my sister died after your ten paces, I may still kill you."

"I know."

"If she lived because you stopped the wagon, I may still hate you."

"That would be fair."

Kesh exhaled. "This company is developing very complicated terms of employment."

Tavi's lock clicked open. She pulled the cabinet door wide with too much force, grateful for the interruption. Inside lay ledgers, but not the transfer ledgers Saelith had promised. These were chapel intake copies: names in pale ink, dates, custody seals, blessings administered, objections noted and then crossed through.

Arveth moved beside her.

His fingers hovered over one page.

"Maelin Noct-Vey," he said.

Ilyr closed his eyes.

Mara leaned in. The entry had not been completed. Beside Maelin's name, someone had written diverted under irregular custody breach. A second hand, sharper and later, added: not recovered. Risk lineage noted.

"Not recovered," Tavi whispered.

Hope entered the room like a dangerous animal.

Ilyr pressed both hands flat to the table. "This ledger goes with us."

"All of them do," Mara said.

Caldus looked toward the stair. "The main archive will have the royal copy. The chapel copy proves a breach. The royal copy proves where the rest went."

"And this chapel is between us and it," Mara said.

He nodded.

"Then we go through."

Caldus looked down at the child's cuff still in his hand. He folded it carefully, not to save it, but because throwing it would have been too easy. Then he placed it in his belt pouch.

"No," he said. "I go first."

Mara did not argue. Some roads were confession before they were strategy.

Below them, the chapel bells changed pitch.

Alarm, at last.

Tavi stuffed the chapel intake ledger into an oilskin sleeve. Ilyr took the Maelin page copy and held it against his chest once before hiding it under his coat. Kesh cracked the door and listened.

"Stairs full of piety with weapons," he whispered.

Mara lifted the cage. The cinder inside glowed as if it recognized the chapel under the chapel.

"Then let them hear names when we pass," she said.

Arveth smiled sadly. "That is becoming your answer to many doors."

"It keeps opening them."

Caldus drew his sword and started down into the Ash-Marked Chapel, carrying at his throat the thin red line Ilyr had given him and in his hand the key made of a mistake he had finally said aloud.""",
    18: r"""The breach Tavi made in the chapel wall did not open straight into the drowned archive.

It opened into a forgotten baptismal canal.

Cold black water surged up to meet them, climbing over the broken stones and around Caldus's boots. The chapel above filled with smoke, bells, and the righteous shouting of men who had mistaken volume for holiness. Tavi coughed through dust and pointed with her wrench toward a narrow ledge running along the canal wall.

"That way. The canal feeds the archive basin."

Kesh looked at the dark water. Something pale moved beneath its surface. "Does the basin feed anything back?"

"Almost certainly."

"I ask because almost certainly has teeth."

Brakka dropped from the broken chapel wall into the canal with a splash that slapped everyone else's knees. She sniffed the water and made a face. "Old vows. Bad lime. Dead flowers."

"Can you smell vows?" Mara asked.

"Can humans not?"

"No."

"Sad people."

They moved along the ledge with their shoulders against damp stone. Behind them, royal soldiers entered the chapel through the upper doors. Caldus had delayed the first wave long enough for Tavi's blast, but not cleanly. Blood ran down one side of his face. The child's cuff from the choir school remained tucked at his belt like a wound he had chosen to carry where others could see.

Mara walked behind him.

She had thought confession might make him smaller. Instead it had stripped away the shape he had been using to keep from collapsing. What remained was not noble, not simple, not forgiven. It was a man who knew the weight of ten paces and was finally walking them in the other direction.

Ahead, the canal widened around a stone platform half sunk in water. Three statues stood there: a crowned king, a robed saint, and a miner holding a lamp. The king's face had been carefully restored. The saint's hands had been gilded. The miner's lamp was broken off.

Mara stopped.

Tavi, who nearly walked into her, hissed, "If this is a symbolic pause, make it brief."

Mara waded to the platform and picked up the broken lamp piece from the water. It was only stone, slick with algae, but the missing shape in the miner's hand felt like a sentence.

"They even repair statues upward," she said.

Arveth looked at the king, then the saint, then the miner. "Records behave the same way when power owns the ink."

Ilyr listened to the shouts behind them. "We are about to be revised with arrows."

The first arrow struck the canal wall and cracked into splinters.

They ran.

The ledge ended at an iron grate. Beyond it, the canal dropped into a vertical shaft where water fell so far the sound arrived back as thunder. Tavi thrust her tools at the grate lock, swore, changed tools, swore with more education, and finally said, "This is not mine."

Kesh brightened. "At last, a lock with taste."

He crouched, inserted two thin picks, and became still in a way Mara had never seen. The joking left him. His ears angled toward the lock. His whole body listened through his fingers. Soldiers shouted behind them. Water hammered below. The cinder cage pulled toward the shaft.

Kesh whispered, "Someone has been here recently."

"Opening it?"

"Closing it in a hurry."

"Joryn?"

"Human hands. Bound wrists, maybe. Scraped blood on lower bar."

Mara went cold.

Caldus stepped beside her, shield raised toward the arrows. "Can you tell if he went through?"

"No."

"Open it."

"I am engaging in that heroic theme."

A bolt struck Caldus's shield. Another skipped off Brakka's shoulder plate. The troll growled, not in pain but insult.

Mara held the cage close to the blood smear on the grate. It was brown-black, nearly washed away. She did not know if it was Joryn's. Wanting it to be his felt terrible; not wanting it felt worse.

The cinder hummed.

For a breath, the canal vanished.

Joryn stood at this grate in the dark, hands bound, Saelith's pale light over his shoulder. He had one split lip. He was wet to the waist. He looked down into the shaft and laughed once, very softly, because fear had surprised him by being absurd.

"You people build dramatic plumbing," he said.

A royal guard struck him across the mouth.

Saelith said, "Enough."

The vision broke.

Mara nearly fell into the grate.

"He was here," she said.

Tavi looked up from the lock. "Alive?"

"Mouthy."

Kesh clicked the final pin. "Then definitely alive."

The grate swung open. A cold wind rose from below, carrying the smell of river mud, old paper, and something that had been waiting patiently for a long time.

"There is no ladder," Caldus said.

Tavi peered down. "There was."

"Was?"

"Technically many things are ladders once."

Brakka took a coil of rope from her belt. It looked like thread in her hands but was thick enough to moor a ferry. "I go first."

"The shaft may narrow," Tavi warned.

"Then shaft learns regret."

She tied the rope around an iron ring set in the stone. Mara noticed the ring bore an old maker's mark half covered by chapel lime. A road under three stars.

Tavi noticed too. Her jaw tightened.

The soldiers reached the platform behind them.

Brakka dropped into the shaft.

The rope snapped taut. Stone dust fell. Then her voice rose from below. "Wet. Wide. Angry water. Come."

Kesh went next because he claimed thieves fell better than honest people. Tavi followed after securing the chapel ledger to her chest in an oilskin sling. Arveth descended with unsettling grace, like a body remembering burial in reverse. Ilyr slid down one-handed, watching Caldus the whole time.

Mara turned to Caldus. "You can still go back."

He looked at the advancing soldiers, then at the chapel behind them. Smoke rolled under the painted ceiling. White-thread cuffs burned where Tavi's blast had scattered sparks. Priests shouted orders from behind armed men.

"I did that once," he said.

Then he climbed down.

Mara was last.

She hooked the cage to her belt, gripped the rope with her healed hand, and stepped backward into the shaft. The old wound no longer hurt. She wished it did. Pain would have made the choice feel more hers. Instead she had Saelith's strength in one hand, Joryn's courage in her chest, and the cinder's hunger tugging below.

Halfway down, an arrow cut the rope above her.

For one suspended instant, Mara saw the severed fibers bloom.

Then she fell.

She hit water hard enough to empty her lungs and steal the world. Cold closed over her. The cage slammed against her ribs. Somewhere near her, someone shouted, but water turned all names into thunder. She sank past floating petals, old ash, torn strips of white thread. The cinder cage glowed blue beneath her chin.

Do not answer anything you hear under the mountain.

The rule followed her into the drowned dark.

This was not the mountain.

The thought was not comforting.

A hand caught the back of her coat and hauled upward. Mara broke the surface choking. Brakka held her by one fist, standing chest-deep in a basin lit by green lamps. Tavi was waist-deep on a submerged stair, soaked and furious. Kesh clung to a shelf of stone with both arms around a satchel. Caldus surfaced nearby, blood streaming from his temple into the water. Ilyr crouched on a ledge with a knife between his teeth. Arveth stood in the basin as if drowning were an administrative category he had already appealed.

Above them, the cut rope fell in a limp coil.

The shaft mouth was a bright coin far overhead. Soldiers looked down from it, too high to shoot cleanly through steam.

Tavi coughed. "Everyone alive?"

Arveth raised a hand.

"Present," Tavi corrected.

The basin stretched beyond the green lamps into rows of shelves rising from black water. Stone cabinets. Brass drawers. Waterproof scroll tubes chained by the thousand. A whole buried hall, half-submerged, its ceiling lost in darkness. The drowned archive.

Mara wiped water from her eyes.

On the nearest shelf, a ledger floated open under glass. Names moved across its page in pale ink, rewriting themselves as drops fell from the ceiling.

At the end of the aisle, something large shifted under the water.

Kesh whispered, "Archive with teeth."

Tavi pulled herself onto the stair and wrung water from one braid. "No one panic. Drowned archives are designed with guardians."

"Designed by whom?" Mara asked.

The water rose in a smooth hump.

Tavi stared at it. "People with confidence."

The hump opened one yellow eye.""",
    19: r"""The fountain did not lead straight down.

It turned them, spun them, swallowed them, and spat them through a maintenance sluice under the square with enough force to send Kesh into Tavi, Tavi into Caldus, and Caldus into a wall that had done nothing to deserve him. Mara surfaced in thigh-deep water beneath an iron grate. Above the grate, thousands of feet stamped, screamed, ran, and gathered again because crowds were not single creatures. Panic moved through them in waves, but curiosity pulled just as hard.

Mordane's speech had not ended.

His voice came through amplification horns fixed to the balcony pillars, bruised by distance and water but still smooth.

"Citizens, remain calm. An act of sabotage has disturbed this lawful observance. Remain calm, and witness how swiftly disorder is answered."

Kesh wrung water from one ear. "I dislike how composed villains sound when damp."

Tavi coughed fountain water and spat out a copper coin. "Someone wished for terrible politics."

Mara pressed herself under the grate and looked up.

The square above had become a broken painting. The statue Brakka had moved lay across a line of soldiers, not crushing them but trapping their advance. People surged around it. Mothers dragged children toward arcades. Heat vendors pulled shutters down. A group of students in blue scholar caps had climbed onto a fountain rim to see better. Workers in gray stood in clusters instead of fleeing, watching the palace balcony with faces gone careful.

Lord Cael Mordane remained where he had stood, framed by gold banners and steam.

He did not look frightened.

That frightened Mara.

Beside him, the king gripped the balcony rail. He was older than his portraits, thinner than the coins, his crown too heavy for his neck. For one wild moment, Mara saw not a monster but a tired man surrounded by people who had made his fatigue useful. Then Mordane leaned close and said something, and the king straightened as if a hand had been placed inside him.

The horns carried the king's voice now.

"Harrowmere is not so easily shaken."

The crowd quieted by degrees. Not because it trusted him fully. Because it needed to. Winter pressed against the city walls. Families needed pipes to work, bread to bake, medicine to warm, schools to stay open. Need made people listen to anyone who promised the floor would not vanish.

Mara understood that. She hated that too.

"For ten years," the king continued, "our cinderworks have kept the capital and the border towns alive through failed harvests, plague winds, and mountain ash. Those who attack this system attack the poor first."

The words entered Mara like cold needles. Around her, the others stilled. Even Kesh stopped muttering.

Mordane had not only wanted her to hear the argument. He had arranged for her to feel it under a square full of people who would suffer if the heat died.

"We need the archive," Caldus said quietly.

"I know."

"Mara."

"I know."

But knowing did not make her move.

Above, Mordane stepped forward again. "There are those who would profane honored labor by calling sacrifice theft. There are those who would weaponize grief against the living. There are those who would tear open old wounds and call the bleeding justice."

Arveth, soaked beside the sluice wall, said, "He has read the ledgers."

Ilyr's face was unreadable. "He has read people."

The amplification horns hissed. Mordane's voice softened.

"If you have lost someone to mercy service, know this: the crown remembers. The chapel remembers. Their names are not gone. Their warmth remains in every house, every infirmary, every school where a child survives the cold."

In the square, some people wept.

Mara's stomach turned. Not because the grief was false. Because it was real and he had built a throne on it.

Then a boy's voice shouted from the crowd.

"Where are the names, then?"

Silence struck the square faster than any baton.

The boy stood near the overturned statue, thin, soot-haired, no older than Niv. A woman grabbed for him too late. A soldier turned.

"My da went mercy," the boy shouted, voice cracking. "They said his name would be kept. Where?"

Mordane did not move.

A captain signaled.

Mara's body was moving before thought could turn coward.

She shoved the grate upward. It did not open. Tavi grabbed her arm.

"No."

"They will take him."

"And you, and the ledgers we do not have yet."

The soldier reached the boy.

Then a gray-clad heatworker stepped between them. The same troll from the heatworks, burn scars visible under his rolled sleeves. He did not raise a weapon. He only stood.

Another worker joined him. Human woman, valve grease on her cheek. Then a baker. Then a student. The soldier found himself facing not a mob, but a small line of citizens who were suddenly too visible to strike cleanly.

The king looked confused.

Mordane smiled.

"You see," he said through the horns, as if this too belonged to him, "how grief seeks order. The crown will receive all petitions after the observance. Return to your homes. Trust the systems that have kept you warm."

"He will disappear the boy tonight," Ilyr said.

"Unless the names reach the walls first," Arveth replied.

The sluice trembled. More soldiers entered the service channel behind them, their lanterns flashing on wet stone.

Brakka, still above in the alley somewhere after moving the statue, bellowed once. The sound came through the square, the grate, and Mara's bones.

Tavi peered down the sluice. "Drowned archive access is two turns east, one drop, and probably a gate that hates me."

"Probably?" Kesh asked.

"I am trying optimism."

Mara looked once more through the grate. The boy had vanished into the crowd, hidden by people who might not yet know they had taken a side. Mordane remained on the balcony, patient as winter accounting. The king waved with stiff fingers. The square did not cheer as loudly as before.

That mattered.

Not enough.

Mara lowered the grate.

"We get the names," she said.

Caldus nodded. "Then we answer the speech."

"Not with a speech."

"With what?"

She thought of the boy asking where his father's name had gone. She thought of Pell's token, Arveth's ledgers, Maelin's unfinished line, Joryn's blood on the grate. She thought of the heatworker standing unarmed in front of a soldier, making violence harder by becoming visible.

"With receipts," she said.

Kesh clasped both hands to his chest. "I have never been prouder."

They splashed east through the service channel while soldiers closed from behind. At the first turn, Tavi opened a maintenance hatch by insulting its hinge. At the second, Ilyr cut a lantern line and dropped the passage into darkness. At the drop, Caldus went first and caught Mara by the waist before she hit the lower floor badly enough to regret it.

The city above continued listening to Mordane.

Below, under the square, they followed the sound of water into a hall where every wall was carved with old warning script. Most of the warnings had been plastered over. One remained visible beside a rusted wheel.

Tavi wiped slime from it and read aloud.

"Records of burden must outlive the burdened, or craft becomes hunger."

"Gnome proverb?" Mara asked.

"Gnome law."

The wheel would not turn. Brakka reached them at last by dropping through a side shaft and landing in the channel with a satisfied grunt.

"Statue useful," she said.

"I noticed," Mara replied.

Brakka put one hand on the wheel. It turned.

The wall opened into a descending stair drowned to the fifth step. Cold air breathed from below. It carried paper rot, river silt, and the faint, metallic scent of cinder commands stored too long in ink.

Behind them, soldiers shouted at the upper turn.

Mara stepped onto the first flooded stair.

Mordane's argument still moved inside her, poisonous because parts of it touched need. She would not defeat it by pretending warmth did not matter. She would defeat it by proving that warmth bought with hidden people was not mercy. It was theft made comfortable.

The stair sank under black water.

She went down.""",
    20: r"""The archive guardian's yellow eye followed Mara as she moved between shelves.

It had no fixed shape, or perhaps too many. At first it seemed like a crocodile made of ledger leather and brass hinges. Then it turned, and Mara saw a long skull plated with porcelain drawer labels, a spine of chained scroll tubes, ribs of black wood, claws made from broken seal stamps. Archive crabs swarmed over its back, cleaning silt from its joints with frantic devotion. Every time it breathed, pages fluttered in cabinets all around the basin.

Tavi held both hands out. "No one threaten the records."

"I was going to threaten the monster," Kesh whispered.

"The monster is the records."

Kesh lowered his knife. "I respect scholarship."

The guardian opened its mouth. Inside, instead of teeth, hundreds of little brass nameplates clicked up and down.

Arveth stepped forward.

"Witness Clerk Arveth of Orrowen," he said. "Custody irregular, death status disputed, name retained."

The nameplates stilled.

Caldus raised his shield slightly. Arveth did not look back.

"We seek transfer ledgers under royal seal," he continued. "Mercy intake, cinder command allocation, labor continuation, living holds. We seek copies for witness action, not destruction."

The guardian's eye shifted to Mara.

The cinder cage pulsed.

Tavi made a warning sound. "Mara."

Mara stepped beside Arveth. Water tugged at her knees. "Mara Venn of Kell Ashgate. Living. Angry. Trying not to become reckless in ways that help murderers."

The guardian clicked.

Kesh leaned toward Caldus. "Do we think it appreciates honesty?"

"We are alive, so perhaps."

Mara lifted Pell's token. "Pell Orwick. Essa Brant. Tollen Reed. Lysa Mar. Maelin Noct-Vey. Joryn Venn. I need the places where their names were taken."

The guardian lowered its head until the water rose around Mara's waist. Its breath smelled of ink, mud, and extinguished candles. The nameplates in its mouth rattled, arranging and rearranging.

Then a shelf behind it unlocked.

Not open. Unlocked. The difference mattered because the archive was still waiting to see what they did with permission.

Tavi exhaled. "Thank every difficult ancestor."

They moved fast after that.

The drowned archive had been built for disaster. Drawers rose from the water on counterweights. Glass-front ledgers turned pages when spoken to in the right custody formulas. Scroll tubes surfaced from submerged racks like fish approaching bait. Tavi knew some of the mechanisms. Arveth knew the record logic. Ilyr knew which names to look for from Orrowen. Caldus knew enough royal seal structure to identify which pages mattered most and enough shame to flinch each time he found one.

Mara knew none of that.

So she did what ash-runners did: she went where smaller bodies could go.

The shelf the guardian had unlocked jammed after the third drawer. Tavi tried a tool. The tool snapped. Tavi looked personally betrayed.

"There is a crawl gap behind it," Mara said.

"There is a drowning gap behind it."

"I fit."

"You fit many places you should reconsider."

Mara handed the cage to Caldus.

The moment her fingers left it, the cinder screamed.

Not aloud. Worse. Inside her skull. The sound drove her to one knee in the water. Every lamp in the archive flared blue. The guardian surged. Archive crabs scattered up the shelves.

Caldus shoved the cage back into her hands.

Silence snapped down.

Mara gasped.

"Apparently," Tavi said, voice thin, "you remain a package."

"I hate that."

"Yes. Crawl with it."

Mara tied the cage tight against her chest and squeezed behind the shelf. The gap was colder than the basin, packed with roots, silt, and bits of old paper soft as skin. She pushed forward on elbows and knees, the cage scraping stone beneath her. Behind the shelf, the archive became intimate: no grand hall, no monster, only the backs of cabinets where names had leaked through cracks in ink.

Whispers started at once.

Mara Venn.

She ignored them.

Venn blood.

She ignored that too.

Daughter of the man who listened.

Her hand slipped.

The crawlspace narrowed around her ribs. Ahead, a brass latch glimmered. She reached for it and found a human fingernail wedged in the mechanism, old but not ancient. Someone had been forced behind here before. Someone had tried to open this drawer from the wrong side.

The cinder showed her.

Not because she asked. Because the archive was full of memory and the cinder was greedy.

A woman crawled where Mara crawled now, older than Joryn, younger than Caldus, dark hair braided close, wrists cut by white thread. Maelin Noct-Vey. She had one hand free. Behind her, water rose. Ahead, the latch refused. She whispered a word in dark-elf speech that sounded like a blade laid down carefully. Then she drove her bleeding thumb into the mechanism and turned pain into leverage.

The drawer opened.

Hands dragged her backward before she could reach what was inside.

The vision ended with Mara's mouth full of silt.

She coughed, spat mud, and forced her fingers around the latch. It was stuck on the old nail, the old blood, the old failure. Her healed hand had strength. Her unhealed heart had more anger than sense. She pressed until the skin split again over Saelith's perfect repair.

Good.

Pain flared. The latch turned.

The drawer opened into the hall with a boom.

"Found something," she shouted, which was dignified considering she was wedged behind furniture and bleeding on history.

Tavi's whoop echoed through the archive. "That drawer was impossible from this side."

"It had help from before."

When Mara crawled out, Ilyr was already at the open drawer. He lifted a packet wrapped in black oilskin. His face went so still it frightened her more than anger.

"Maelin's hand," Mara said quietly.

He looked at the blood on her bandage, then at the drawer. "She opened it?"

"Almost."

Arveth took the packet. "Then we finish the motion."

Inside lay not Maelin herself, not a body, not even a confession. It was a cross-index. Names diverted from chapel custody after irregular breach. Destinations hidden under heatwork codes. Some lines ended in foundry numbers. Some in military command trials. Some in the word retained.

Maelin Noct-Vey: retained. Choir suitability uncertain. Memory resistance unusually high.

Ilyr made no sound.

"Alive?" Mara asked.

Arveth shook his head slowly. "Retained does not always mean alive. It means not spent."

"That is a horrible sentence," Tavi said.

"Yes."

Another drawer surfaced at Caldus's call. This one bore Kell Ashgate allocation marks. Mara waded to it with dread moving ahead of her.

Pell Orwick: locomotor utility after naming failure, assigned ash-load rotation.

Essa Brant: vocal resistance noted, command instability, assigned silence trial.

Tollen Reed: courier mapping retained, road-memory extraction.

Lysa Mar: furnace draw, low command yield.

Joryn Venn: living hold, leverage classification, paired tag pending.

Mara read the last line again and again until the words stopped becoming safer.

Paired tag pending.

Pending meant not yet.

Saelith was still delaying him, or Mordane was still waiting for Mara to do something foolish enough to make the tag useful. Either way, Joryn had not been converted into a command instrument. Not yet.

That not yet became a rope inside Mara.

"We copy everything," she said.

Tavi was already assembling a copying rig from mirror plates, waxed paper, and a lamp she swore was not technically stolen because archives belonged to the public in any decent civilization. Kesh sorted waterproof tubes. Brakka guarded the stair with her maul across her knees. Caldus read seal lines aloud while Arveth confirmed legal meaning. Ilyr copied Maelin's cross-index by hand with a steadiness that looked like grief trained until it could hold a pen.

Then the archive began to drain.

At first Mara thought the water was only shifting. Then a tide mark appeared on a shelf. Archive crabs clicked in alarm and fled upward. The guardian lifted its head, nameplates clattering.

Tavi looked at the nearest gauge and went pale.

"They opened the purge sluices."

"What does that do?" Kesh asked.

"Drains water out. Lets fire in."

"Why would an archive need fire?"

"To prevent contamination."

Arveth looked toward the stair where soldiers' lanterns now burned. "By truth."

Heat rolled through the floor.

The guardian moved.

Not toward them. Toward the lower gates. Its huge body slid through the receding water, scraping shelves, gathering fallen ledgers against itself as if trying to shield them. Archive crabs swarmed after it. The thing had been built to protect records, but the system that made it had also built the purge. It could not choose both.

Mara understood that kind of trap.

She lifted the cinder cage.

Tavi grabbed her arm. "If you wake it here, you may ignite the whole basin."

"Can the guardian stop the fire alone?"

"No."

"Can you?"

"No."

"Then let go."

Tavi did not.

"Mara, names are not water pressure. You cannot answer every system by throwing your soul at it."

"I am not throwing."

"You are leaning dramatically."

Despite everything, Mara smiled once. "Then anchor me."

Tavi stared, then swore. "Fine. Terrible. Educational."

She wrapped one end of Saelith's cut hymn-cloth around Mara's wrist and tied the other to her own belt. "If your eyes go blue and ancient, I am kicking you."

"Helpful."

Mara opened the cage one finger's width.

The cinder did not explode. It breathed.

She gave it names, not power. Pell. Essa. Tollen. Lysa. Maelin. Joryn. The boy in the square who wanted his father's name. The troll heatworker. The unnamed clerk who had scratched a warning into a wall and died before anyone thanked them. She did not ask the cinder to burn. She asked it to remember what burning had been made to hide.

The archive answered.

Every ledger in the hall opened at once.

Pages rose from water, cabinets, scroll tubes, and submerged shelves, each page glowing with a name. Not all. Not enough. But hundreds, then thousands. The guardian stopped before the purge gate. Its nameplates stilled, then rang like tiny bells. The water that remained in the basin lifted into a mist bright with ink.

The incoming fire hit the mist and died.

Steam filled the hall.

Mara nearly went with it.

For one breath she was not only herself. She was every intake line, every crossed-out objection, every legal fiction written over a human name. She felt the vast terrible convenience of numbers. She felt how easy it was to make a person into a unit if no one said their name aloud.

Tavi kicked her in the shin.

Mara returned to herself with a gasp.

"Eyes," Tavi said, terrified and trying not to show it. "Less ancient. Good."

The purge failed. Somewhere above, mechanisms screamed. Soldiers shouted in confusion. The guardian turned its great ledger-skull toward Mara and bowed.

Not to a saint.

To a witness.

Caldus shoved another packet into oilskin. "We have enough."

Arveth, surrounded by floating pages, looked older than death. "Enough to begin."

That was all proof ever was.

They fled through the crab tunnel with ledgers, copies, and wet names pressed against their bodies. Behind them the guardian settled over the lower shelves, shielding what remained. As Mara crawled after Kesh through mud and roots, the cinder cage lay quiet against her chest.

Not satisfied.

Never satisfied.

But listening.""",
    21: r"""The first broadside came off Tavi's borrowed press with the ink too heavy and the margins crooked.

Kesh loved it at once.

"It looks illegal," he said, holding the sheet by two corners. "That is a difficult aesthetic to fake."

"It looks rushed," Tavi said.

"Rushed is a dialect of true."

Mara took the paper. Across the top, in block letters cut from a dye crate lid, ran the words: WHERE ARE THE NAMES? Below, Arveth had written the first witness claim in clear, merciless lines. Pell Orwick, of Lower East Vent, declared dead after company incident, reassigned under mercy labor seal. Essa Brant, vocal resistance noted. Tollen Reed, courier mapping retained. Maelin Noct-Vey, diverted after custody breach. Joryn Venn, living hold.

The list continued down the page until the paper seemed too small to bear it.

At the bottom, Mara had insisted on one sentence.

Warmth is owed to the living, but no one may be burned in secret to buy it.

Tavi had argued that owed was legally tricky. Arveth had said legally tricky was often where truth lived. Kesh had suggested adding several insulting remarks about Mordane's hair. Brakka had offered to carve the sentence into stone for durability. In the end, the line remained plain.

Plain had teeth.

They worked through the night.

The dye warehouse became a rebellion by accident of furniture. Tables turned into sorting stations. Vats became hiding places for oilskin packets. Laundry lines held wet prints. A back room became an infirmary where Tavi cleaned Mara's split hand with vinegar, needle, and much professional muttering about patients who reopened expensive miracles.

"It was not expensive," Mara said.

"Morally expensive."

"Then charge Saelith."

"I intend to, if she survives my invoice."

The cut on Mara's hand hurt properly now. Saelith's perfect healing had torn along a real line when she opened Maelin's drawer. Tavi stitched it with small black thread and left the scar visible.

"There," the gnome said. "Imperfect. You are welcome."

Mara looked at the new seam across her palm. It was not the same wound as before, but it belonged to her. "Thank you."

Tavi's expression softened, then immediately became businesslike to protect itself. "Do not bleed on the broadsides. Ink is already complicated."

Near the warehouse door, Caldus drilled volunteers with quiet commands.

They had volunteers now.

Not many. Not an army. A troll courier from the arches. Two goblin runners from Narka's road. The burn-scarred heatworker from the square, whose name was Othen Brask and whose first request was that they stop calling him the burn-scarred heatworker. A human baker who had hidden the boy who shouted. Three dye workers who had lost cousins to mercy service and had never been told where the ashes went. One student with blue scholar cap still dripping fountain water, shaking so badly Kesh gave him busywork and called it espionage.

Each arrival changed the room.

Mara had imagined rebellion as banners, weapons, a crowd roaring one word. This was smaller and more frightening: people deciding in twos and threes that silence had cost too much, then looking at her as if she knew where courage should stand.

She did not.

So she kept asking what they could do next.

Othen knew which heatwork crews would read before reporting. The baker knew which bread carts passed palace checkpoints before dawn. The dye workers had access to cloth bundles shipped to inns and barracks. The student knew how to get into the scholars' notice court if someone distracted the night porter with a plausible fire.

"I can provide an implausible fire," Tavi offered.

"Plausible," Mara said.

"Fine. Small-minded."

Ilyr spent the night copying Maelin's line in three scripts. He did not ask for comfort and no one offered it badly. At one point, Mara found him alone near the loading door, holding the copy so carefully the paper did not tremble.

"Retained means a chance," she said.

"It means a use."

"A chance to find the use."

He looked at her. "You turn knives around in your hands until you find the handle."

"Ash-runners do not get clean tools."

"Dark courts teach the same lesson, with better poetry."

She leaned against a crate beside him. Rain ticked on the warehouse roof. In the city beyond, bells marked the last quarter of night.

"Will you stay?" she asked.

"Until Maelin's line ends."

"And after?"

"Ask me after."

It was more honest than promises. Mara accepted it.

At the main table, Arveth finished the list of first names to release. He had chosen fewer than Mara wanted and more than caution liked. "A flood becomes mud if it has no channel," he said when she protested. "We begin with names tied directly to recoverable ledgers. Then we widen."

"Every delay is a person waiting."

"Every error is a person Mordane will use to discredit the rest."

She hated that he was right. She was beginning to collect useful hatred the way Kesh collected keys.

Caldus placed the original ledger in front of her. "You should decide where this goes."

"You carried it."

"That is why you should decide."

Mara looked at the oilskin packet. The old version of her would have taken it and run north. The slightly older version would have given it to Caldus because knights knew courts and seals. The woman sitting in the dye warehouse with ink on her sleeves and stitches in her palm understood that no single hand should hold proof everyone needed.

"Three copies leave before dawn," she said. "Original goes to Brakka's arch until we can build a public place to read it. Not a court. A witness hall."

Brakka's amber eyes warmed. "Stone remembers."

"Good. Let stone be harder to bribe."

Caldus nodded and, for the first time since Mara had met him, looked relieved to be overruled.

Just before dawn, Saelith came to the warehouse.

No one saw her enter. One moment the back corner was shadow, and the next it held pale light and a woman with rain silvering her cloak. Every weapon in the room lifted. Ilyr's blade touched air. Caldus had his sword half drawn. Brakka's hand closed around her maul.

Mara stood with one palm on the wet broadside.

"Where is Joryn?"

Saelith's composure was badly made now. One braid had come loose. There was blood on the cuff of her pale sleeve, not much, but enough to prove that someone had resisted or she had.

"Moved to the north foundry road," Saelith said. "Not tagged."

The words nearly took Mara's knees.

"Alive?"

"Yes. Angry. He told me to tell you that my sense of timing inspires no confidence."

Mara laughed once before she could stop herself. It came out broken.

Saelith looked at the broadsides hanging from the lines. Her face moved through alarm, calculation, and something like awe. "You did not come for him."

"I am coming," Mara said. "But not alone."

"Mordane will call this sedition."

"He would have called breathing suspicious if it inconvenienced him."

Kesh pointed at her. "That one is mine. I said something adjacent."

Saelith stepped closer to the nearest broadside. "If these go out, the chapel cannot shield him openly. Mordane may accelerate the transfer."

"Can you delay it?"

"Less than before."

"Then help more than before."

The room held its breath.

Saelith looked at the names. Pell. Essa. Tollen. Maelin. Joryn. Her fingers lifted but did not touch the ink.

"I was taught that mercy without order becomes cruelty," she said.

Arveth replied, "You were not taught what order becomes without consent?"

Her eyes lowered.

Mara did not beg. She was done arranging her pain into shapes enemies found acceptable.

"If your oath is worth anything," she said, "make it answer to the people it touched."

Saelith closed her hand around the cut strip of hymn-cloth still tied at Tavi's belt. Tavi startled but did not pull away.

Light passed from Saelith's palm into the cloth, faint and steady.

"This will open one chapel courier gate," Saelith said. "Only once. After that, they will know I gave it."

"What happens to you then?"

"I find out whether obedience was protecting me or only delaying the price."

Mara accepted the charged cloth.

Outside, the first bell of dawn rang.

The packets began to move.

Goblin runners slipped through dye drains. Bread carts rolled toward palace districts with names under the loaves. Troll stone tubes left by river barge. Students carried folded sheets inside lesson slates. Heatworkers tucked lists into gauge houses where crews changed shifts. By the time Harrowmere's first fires brightened the rooftops, the question had spread farther than any one patrol could chase.

Where are the names?

Mara climbed to the warehouse roof to watch.

The city looked almost peaceful from above. Steam rose in gentle threads. Bells called people to work, prayer, breakfast, duty. But on three walls already, black letters appeared where clean plaster had been: Pell Orwick. Essa Brant. Tollen Reed. Maelin Noct-Vey. Joryn Venn. Names like cracks. Names like doors.

Below, her company gathered around the next map: north road, foundry approaches, Ashgate contacts, chapel courier gate. The rescue had not been abandoned. It had grown teeth, feet, witnesses.

Mara pressed her stitched palm against the cinder cage.

"Hold on," she whispered again, but this time the words traveled with runners, carts, stone, bread, and ink.

This time, the city whispered back.

The whisper became trouble before breakfast.

From the warehouse roof, Mara watched a palace patrol stop at a baker's cart three streets over. The soldiers were careful at first. That told her more than brutality would have. They looked around before lifting the cart's cloth, spoke softly to the baker, checked whether anyone watched from windows. Harrowmere had not become brave in one dawn. It had become watchful, and watchfulness made cruelty consider its posture.

The baker, a square woman with flour up both arms, folded her hands over her stomach and answered something Mara could not hear.

The captain reached into the cart and pulled out a loaf. A broadside fluttered from the split crust, black letters bright against steam.

Where are the names?

The soldiers stared at the paper.

Then the boy from the square appeared at the alley mouth, grabbed the loaf from the captain's hand, and ran.

Mara made a sound that might have been prayer if she had believed anyone polite was listening.

The alley erupted. Not with a riot, not yet. With obstruction. A milk cart lost a wheel in a way Kesh admired from three rooftops away. Two laundry lines fell at once, dropping sheets between soldiers and boy. A scholar in a blue cap began shouting that the captain had violated a municipal bread tax procedure, and did so with such confidence that three bystanders joined in before understanding the charge. The boy vanished under a fishmonger's awning and did not reappear.

The captain could have ordered batons.

He did not.

Too many windows had faces in them.

"There," Arveth said beside Mara.

She had not heard him climb to the roof. "There what?"

"A system changes first when its servants hesitate."

"I thought it changed when people like us did something dramatic."

"Dramatic people are often remembered because clerks need clean beginnings. Hesitation is where the record actually turns."

Below, the patrol withdrew with less dignity than it wanted. Someone pasted another broadside to the side of the milk cart before it rolled away.

Mara let herself breathe once.

Then another bell rang from the palace district, sharp and fast.

Tavi's head emerged from the roof hatch. "We have a problem shaped like success."

"Specifics?"

"The palace has sealed the public archive, the chapel has recalled all mercy couriers, and three heatwork districts have asked their crews to swear emergency silence."

Kesh popped up behind her. "Also, Narka sent a runner. She says congratulations, you have made everyone expensive."

"That sounds like approval."

"With Narka, approval often arrives carrying knives."

They went back below.

The warehouse had become louder and more crowded. Not safer. Crowded did not mean safe. It meant decisions now had witnesses. Othen Brask stood over the map with his broad hands planted on either side of Harrowmere's heatwork marks. He had cleaned the grease from his face, which made the burn scars down his neck look rawer. Beside him, two crew chiefs argued in low voices while a dye worker barred the door with a beam.

"If you shut the north foundry wrong," Othen said as Mara approached, "the lower districts lose heat within six hours. Palace won't. Rich pipes have reserve coils. Tenements do not."

"We are not shutting it wrong," Tavi said.

Othen pointed at her with a wrench. "That is a hope with goggles."

"It is also a professional insult, but continue."

He tapped three points on the map. "Foundry draws from Ashgate cinder rails, palace command coils, and chapel intake. You break one, Mordane shifts load to the others. You break all, people freeze before noon if the wind turns. You expose ledgers only, he calls you sentimental saboteurs. You seize the foundry and cannot run it, same result with more smoke."

Mara looked at the map until the lines became veins. "Then what does work?"

Othen's mouth tightened. "A transfer. We take heatwork control from the crown coil and put it onto district valves. Slow. Messy. Crews in every quarter have to agree. Someone inside the foundry has to open the command manifold. Someone outside has to keep soldiers off the valves. Someone has to prove to ordinary families that you are not here to make their children cold."

"So not dramatic," Kesh said.

"Very dramatic," Othen replied. "Just with more math."

Caldus leaned over the table. "Can the crews do it?"

The two crew chiefs exchanged a look.

One was an older human man with a white mustache stained yellow by pipe smoke. The other was a young gnome woman with both eyebrows burned half off. The gnome spoke first.

"Crews hate emergency silence oaths. Means management plans to blame workers. If the witness packets keep moving, some will listen."

"Some is not all," the older man said.

"Some is how all begins," Brakka rumbled from the doorway.

Mara traced the north road toward the foundry where Joryn had been taken. "The rescue and the heat transfer are the same path."

Othen nodded once. "If your brother is leverage, he will be near the command manifold. Living tags need signal. If Mordane intends to use you, he wants you in the same place."

"A trap," Caldus said.

"A trap can be a door if you bring enough people to disagree with it," Kesh said.

Everyone looked at him.

He raised both hands. "What? Occasionally my mouth finds architecture."

The roof bells rang again. This time the pattern came from three directions: palace, chapel, and lower market. Harrowmere was answering itself badly.

Mara took the wanted notice from her coat. Rain had blurred the sketch, making her chin worse. She set it beside the broadside.

"Mordane wants a single villain," she said. "Ash-runner, cinder witch, saint, saboteur. Something people can point at instead of the system. So we do not give him one."

Tavi's eyes narrowed with quick approval. "Distributed nuisance."

"Witness cells," Arveth corrected.

"That is less fun."

"And more admissible."

Mara touched the map. "Kesh, Narka needs copies to every road out of Harrowmere and every Ashgate contact who can move without drawing patrols. Brakka, the ledger goes to the Third Arch and stone copies begin there. Tavi, you and Othen make a plan that keeps heat in the lower districts when the foundry changes hands. Ilyr, send Maelin's line to anyone in Khar Veyl who still cares what happened to Orrowen."

Ilyr's mouth curved without warmth. "That will disturb very dangerous people."

"Good. They can stand in line with the rest."

Caldus waited. She knew he was waiting. He would accept any order that made him useful enough not to think about ten paces, which meant she had to choose carefully.

"Caldus," she said. "Find the soldiers who hesitate."

He looked up.

"Not the cruel ones. Not the ones who would sell their mothers for a cleaner uniform. The ones who heard the boy in the square. The ones who know emergency silence means something rotten. We will need doors opened from inside."

"They may not listen to me."

"Then tell them why they should not have listened to you before."

The words hurt him. They were meant to. Not as punishment. As key.

He bowed his head once. "I will."

Saelith stood apart from the table, pale as a candle in daylight. No one had given her a task. No one trusted her enough. Mara saw the way she accepted that as if distrust were cleaner than forgiveness.

"Saelith," Mara said.

The light-elf turned.

"You know chapel courier routes. You know how they hide living holds. I need every hour you can steal for Joryn, and I need you to tell us which mercy houses will hurt people first when the broadsides reach them."

"You are asking me to betray my order."

"No," Mara said. "I am asking whether your order betrayed its mercy."

Saelith closed her eyes. When she opened them, the careful distance in her face had not vanished, but it had cracked enough for pain to show honestly.

"There is a hospice on Bellweather Lane," she said. "They keep six patients on cinder warmth who cannot be moved. If panic cuts that pipe, they die before the palace notices. Start there."

Othen marked the map.

The room changed again. Not kinder. More real.

For the next hour, they did not speak like heroes. They spoke like people trying to keep strangers alive while stealing power from murderers. It was harder than fury. It required lists. Routes. Names of valve crews. Names of informants. Names of sick houses, orphan kitchens, winter schools, ash tenements, old soldiers' homes. The work was dull in the way foundations were dull, buried under everything until they failed.

Mara found herself at the center of it because people kept bringing her questions.

She answered what she could. When she could not, she said so. That surprised them more than confidence would have. It surprised her too, how often ignorance spoken plainly made room for someone else's expertise. Tavi corrected her twice. Othen corrected her five times. Kesh corrected everyone and was right enough to be unbearable. Arveth kept the record.

By full morning, the first answer came from Kell Ashgate.

It arrived in the hands of Niv, filthy, breathless, and furious at being shorter than every barricade he had climbed. Rella was with him, carrying a sack of nail-studded scrap and wearing an expression that dared anyone to mention bedtime.

Mara crossed the warehouse so fast she nearly knocked over a stack of wet prints.

"You should not be here," she said.

Niv puffed up. "That is what the road guards said."

"How did you get past them?"

Rella opened the sack. Inside were dozens of work tokens, old company badges, bits of broken cinder cage, and a strip of red cloth from Dilla's shop.

"Kell Ashgate sent names," she said.

Her voice was small but steady. "More than would fit in one packet."

Mara took the sack as if it were heavier than any ledger in the archive.

Niv wiped his nose on his sleeve. "Dilla says if you start a rebellion without proper soup she will come here and make everyone ashamed."

Kesh looked solemn. "A terrifying logistics threat."

Mara knelt so she could meet Niv's eyes. "Is the city ready?"

He considered lying. She saw him reject it because children from places like Kell Ashgate learned early which lies wasted time.

"No," he said. "But it is angry in organized ways."

That was enough to make the room fall silent.

Mara stood with the sack of tokens in both hands. Pell's token at her throat warmed against the others, or perhaps that was only her pulse. For one moment she saw the road ahead: north foundry, Joryn, Mordane, heat valves, chapel gates, soldiers who might hesitate, dead who might be named, living who might freeze if she mistook destruction for justice.

This was bigger than rescue now.

That still hurt.

It also meant Joryn had more people coming for him than one frightened sister with a cage.

Mara poured the tokens onto the map. They scattered across Harrowmere's streets like fallen sparks.

"All right," she said. "We start with Bellweather Lane. Then we take the north road."

Outside, the city bells tangled with market noise, patrol whistles, and the first distant chant rising from a wall where someone had begun reading names aloud.

This time, the city did not merely whisper back.

It learned the rhythm.""",
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
        'current_form: "full-length draft zero with Book One chapters 1-21 revised in pass 01; continuing literary revision needed"',
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
    print(f"Book One chapters 14-21 revised. Word count: {total}")


if __name__ == "__main__":
    main()
