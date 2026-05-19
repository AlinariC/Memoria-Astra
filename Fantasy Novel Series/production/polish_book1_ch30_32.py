#!/usr/bin/env python3
"""Revision pass 01f for Book One chapters 30-32.

Replaces the first half of Part V with bespoke prose: Brakka bringing bridge-law
into Harrowmere, Saelith's public break with saint doctrine, and Mara carrying
names into the furnace without becoming a weapon.
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
    30: r"""## Chapter 30: The Bridge Comes to the City

The palace tried to become a fortress.

Harrowmere answered by becoming a road.

It began at the south breach, where Brakka stood with both feet planted in powdered marble and one hand on the vow-stone she had hammered into the palace floor. Around her, troll masons set smaller stones into cracks, stair edges, doorframes, statue plinths, and the broken mouths of decorative lions. Each stone carried one line of bridge-law. Each line had been spoken before in the Seven Arches, where roads were shrines, courts, ancestors, and arguments that had learned to carry weather.

This wall shelters the named before the crowned.

This step belongs to the foot that flees harm.

This door opens for the living by consent.

Royal guards pushed against the breach. The floor shifted under them. Not enough to throw them, not a miracle made from lazy hope, but enough to turn a charge into a stumble, a formation into a question. Citizens pressed from the square behind the masons: heatworkers, miners, laundresses, bakers, students, clerks clutching stolen records, families carrying old work tokens, children held high enough to breathe over the crush. They did not pour in as a mob. Brakka would not allow it.

"Road has lanes," she roared. "Panic walks last if panic cannot behave."

Kesh, clinging to the remains of a velvet curtain three yards above the floor, stared down at her. "You are organizing a riot."

"No," Brakka said. "Riot has poor engineering."

The city battle did not unfold as songs later tried to make it unfold.

There was no single line between crown and people. Some soldiers protected nobles. Some protected children. Some protected Mordane's retreat because orders were easier to hold than the faces of the dead. Some threw down weapons, then picked them up again when command-bound corpses lurched too close to civilians. Some did not know what they were doing and survived only because Tesson Vair, formerly royal soldier and recently prisoner, began shouting battlefield instructions with the authority of a man who had nothing left to lose but strangers.

Mara saw all of it from the lower throne steps.

The court was too loud. The city outside was louder. Bells rang without rhythm. Cinder braziers flared and dimmed as Othen's heat crews fought the crown coil from below. The coronation dead stood in broken rows, some still struggling under hidden hooks, some turning toward names called from the square, some staring at their own painted hands as if hands were a new discovery. Halea Voss stood nearest the dais, white robe torn, dead eyes fixed on Mordane's pinned ledger.

Mordane was gone.

Not far. Mara knew that with a certainty that tasted like cinder ash. He had slipped from the court when the throne cinder cracked, moving through whatever service door led back into the crown coil. Men like him did not flee danger. They relocated to whichever system still obeyed.

"He is going below," Ilyr said beside her.

He had blood on one cheek, no visible wound, and the look of someone listening to shadows argue.

"To the foundry?"

"To the undercroft beneath the throne. The command line between palace and regulator runs there."

Tavi's voice burst from the brazier horn. "Correct, and I resent confirming ominous people."

"Can you shut it?" Mara asked.

"I can make it less confident. Shutting requires hands near the crown coil, and my hands are currently preventing district valves from expressing themselves as steam."

Othen's voice followed, rough with static. "Lower districts holding. West infirmary dipped, recovered. Palace reserve dropping. Minister will try to seize reserve manually."

The king, still on his knees beside the cracked throne, looked as if every word was arriving from a country he had never visited.

Caldus crossed to him through the melee. A captain moved to stop him. The young guard who had thrown the spear into Mordane's ledger blocked the captain with both hands and a terrified expression. Caldus reached the king and did not bow.

"Order the north undercroft opened," he said.

The king blinked. "Sir Renn?"

"No. Caldus Renn. Your knight is dead, Majesty. Order the undercroft opened."

"I do not know the undercroft key."

Caldus looked toward Mara. "Then say that aloud."

The king's mouth trembled. The horns still carried the court because Tavi had never met a public system she did not want to steal. His admission went not only to the galleries, but into the square and down the streets.

"I do not know the undercroft key."

For a moment, the battle faltered from sheer embarrassment.

Kesh dropped from the curtain and landed badly on a toppled banner. "I know it."

Everyone looked at him.

"What?" he said. "Palaces overinvest in symbolism and underinvest in locksmiths."

Mara felt a laugh try to rise. It died when the east doors blew inward.

Command-bound dead entered from the palace service hall, a fresh wave pulled up through lifts Mordane still controlled. These had not been painted for ceremony. Foundry ash clung to them. Hooks glowed bare in their throats. Their number plates flashed in the cinderlight. They moved faster than the coronation dead, less stirred by names, more recently emptied.

The citizens at the breach screamed and pushed backward.

Brakka slammed her maul into the floor.

"Road holds."

The vow-stones answered.

The broken palace floor rose in three ridges, not walls, not traps, but guides. They formed channels between the breach and the side courts, between the side courts and the public stairs, between the public stairs and the square. A frightened crowd became movement with somewhere to go. Children first, injured next, those carrying records, then anyone too angry to think. Troll masons held the ridges with their bodies when the stone could not.

Old vows sheltered new people.

Mara ran toward the incoming dead.

Caldus caught up at her left. "Plan?"

"Names if we have them. Space if we do not."

"Bad plan."

"Improve it while moving."

Kesh sprinted past them toward the undercroft door. "I am improving the plan by not standing there."

Ilyr vanished into the shadow of a fallen banner and came up behind the first dead wave, cutting command cables where they ran from hook to hook. Saelith stood before the injured civilians and asked permission so quickly the words became a rhythm: May I bind this, may I steady you, may I carry light, may I touch your child. Yes, yes, yes, no, then she stopped and moved on, and that no mattered more than any yes.

Tavi used the brazier horns as weapons.

"If you are in the west gallery," her amplified voice shrieked, "stop standing under the chandelier unless you have deep religious commitment to gravity."

People moved. The chandelier fell where royal guards had been forming.

"That was not me," Tavi added. "That was poor maintenance and civic destiny."

Mara reached the first foundry dead. No plate she recognized. No family shouting from the crowd. The hook in the throat burned too bright for a voice to pass.

Halea Voss stepped beside her.

"Unknown," the dead scholar said.

The word was not failure. It was classification.

"Unknown," Mara repeated. "Held. Witnessed. Not used."

The dead worker struck at her. Caldus turned the blow. Brakka caught the body's harness and pinned it to the floor. Mara pressed a vow-stone into the body's ash-stiff hand.

"If anything in you wants stillness, hold this," she said.

The hand closed.

The hook sputtered.

Not every name could be found in the middle of a fight. But not knowing did not give them permission to turn the dead back into tools. Unknown was a beginning. Unknown was at least not number.

The battle widened through the court.

Rakka Fen led freed prisoners in cutting white collars from the coronation dead. Tesson Vair and the hesitant soldiers formed a line that protected civilians from both crown guards and stumbling dead. Dilla appeared at the breach with a soup ladle in one hand and a kitchen knife in the other, and no one, including a palace captain, seemed willing to discover which was more dangerous. Niv was not there, thank every sensible thing. Rella was. She stood on a fallen plinth with a slate, taking names shouted from the crowd and passing them to Arveth, who wrote with a hand that shook only when he stopped.

Mara saw Joryn then.

He had no business being in the court. He was pale, bruised, and leaning on Harl Brim's shoulder, but he was there, helping carry the mother with the baby toward the south breach. He looked up and caught Mara's eye across the chaos.

Go, he mouthed.

She looked toward the undercroft door.

Kesh had it open.

Beyond it, stairs descended under the throne into blue-white dark.

Mordane's remaining command pulsed from below. The dead in the court jerked toward it. The throne cinder answered with a cracked, hungry bell.

If they held the court but lost the undercroft, Mordane would seize the crown coil and turn every half-freed dead body in Harrowmere into a weapon. If they chased Mordane and left the court, civilians would be crushed under the next wave.

Mara hated leadership. It was mostly choosing which guilt could wait.

"Brakka," she shouted.

The troll looked up, maul across three pinned dead.

"Can the road hold without me?"

Brakka's amber eyes burned. "Road never held because of one foot."

That was answer enough.

"Caldus, stay."

He looked toward the undercroft, then the civilians, then Mara. The old Caldus would have argued that he belonged between her and danger. This Caldus saw the line breaking near the breach and understood what she was asking.

"Yes," he said.

No title. No protest. One word, freely given.

Saelith reached Mara at the undercroft door with light bleeding from her sleeves. Ilyr emerged from shadow with command cable wrapped around one blade. Kesh bowed toward the dark stair as if presenting a dinner hall. Arveth came last, clutching the ledger and three loose name plates.

"I should stay with the dead above," Arveth said.

"Can the dead above keep choosing if Mordane takes the coil?"

"No."

"Then come below."

He nodded.

Mara looked once more at the court. Brakka had turned a palace into road. Caldus held a human line without rank. Joryn was alive and letting her leave.

Then the undercroft bell rang again, and Mara descended toward the heart of the crown.""",
    31: r"""## Chapter 31: No Saint, No Weapon

The undercroft beneath the throne was older than Harrowmere.

The palace had been built over it the way a polite lie is built over a debt. The stair dropped through layers of human ambition: polished marble, then kingstone, then the black foundation blocks of the first fortress, then a rough tunnel cut directly into mountain bone. At each layer, someone had carved a claim. By blood. By charter. By conquest. By winter law. By mercy covenant. Under all of them, older marks remained where no king had quite managed to scrape them away: gnome warning spirals, troll road signs, dark-elf shadow script, light-elf root hymns, goblin contract nicks, and at the bottom, dragon-scale grooves worn smooth by heat.

Mara ran her fingers over one groove as they passed.

The cinder answered.

Not now, she thought.

It answered anyway, not with words but with the sense of a vast creature opening an eye under a mountain of small arguments.

Kesh went first with a stolen palace lantern. "I am going to say something unpopular."

"Narrow that down," Tavi's voice crackled from a speaking pipe above them.

Kesh glared at the pipe. "Why is she everywhere?"

"I improved the palace," Tavi said.

"You are not here."

"Morally, I haunt you."

Mara nearly smiled, then saw the first saint mark on the tunnel wall.

It had been painted recently in white and gold: a stylized girl with open hands, cinderlight behind her head, the crown kneeling in gratitude. The face had no features. That made it worse. Someone had already begun preparing the image before Mara ever reached the court.

Saelith stopped.

Her face went hollow.

"You knew," Mara said.

"Not this image."

"But something like it."

Saelith did not defend herself. "Serathiel believed if the crown could not hold you as fugitive, the Pale Bough could preserve you as saint. Public witness creates a path. Reverence is harder for kings to challenge than prison."

"And easier for you to justify?"

The words struck, but Saelith accepted the wound.

"Yes."

Ilyr watched the tunnel behind them. "Useful confession. Can we continue before doctrine catches up with knives?"

They descended into a circular chamber lit by the crown coil.

The coil rose from the floor like a metal tree grown in a furnace, its trunk made of braided brass, black glass, white thread, and cinder-veined stone. Roots sank through the floor toward the foundry regulator. Branches climbed through the ceiling toward the throne. Around it stood twelve stone plinths. Ten held old crowns. One held a white bough grown from living light. One stood empty.

Mordane waited beside the empty plinth.

He had removed his gloves.

That frightened Mara more than armor would have. His hands were thin, ink-stained, and burned at the fingertips from the throne cinder's crack. He held the blank ledger against his chest like a wounded animal. The spear still pierced its spine.

"You are persistent," he said.

"You are cornered."

"No. Corners are architectural. I am situationally narrowed."

Kesh sighed. "I hate when villains have vocabulary."

Mordane's eyes moved over them: Mara, Saelith, Ilyr, Kesh, Arveth. He noted who was absent. "Your knight stayed above. Sensible. Your troll too. Your brother lives. Admirable distribution of sentiment."

Mara did not answer. She looked at the empty plinth.

Its base had been carved with her name.

Not fully. The letters were shallow, hurried, but clear enough.

MARA VENN, CINDER SAINT OF THE CROWNREACH.

The cage at her hip warmed as if insulted.

Saelith made a sound. "No."

Mordane looked at her. "Not your order's version, no. Mine would have been more practical. A saint gives legitimacy to sacrifice. A weapon gives leverage. Miss Venn is inconvenient because she refuses to be either while producing the effects of both."

"I produce nothing for you," Mara said.

"Today? Not yet." His mouth tightened. "But the public has seen you with the dead. The king has spoken stolen names. The Pale Bough will come. Khar Veyl will come. Every frightened town that depends on cinder heat will come. You think refusal keeps you free. Refusal only invites better claimants."

The white bough on its plinth began to glow.

Serathiel entered without footsteps.

She did not hurry. Hurry would have made her seem less inevitable. White light followed her down the stair, and behind it came two oathkeepers in pale armor and four chapel guards with hymn-staves. Caldus and Brakka had held the court, but Serathiel had found a path because beautiful institutions always kept one door for themselves.

Saelith stepped between Mara and the saint-general again.

Serathiel looked at the empty plinth, then at Saelith's bloodied hands. "You have brought her to the place of claiming."

"I brought myself," Mara said.

"Child, you are standing in a chamber designed before your grandmother's grandmother knew fear. There are forces here you cannot interpret."

"Then interpret them honestly."

Serathiel's gaze sharpened. "Honesty without order ruins lives."

"Order without honesty already did."

Mordane laughed softly. "There. You see why I admire her."

"Be silent," Serathiel said, and for once Mordane did.

The crown coil pulsed. Above, the battle shook the ceiling. Dust fell in pale threads. The dead in the court cried out as Mordane's reserve command tugged at them through the coil. Mara felt it too, not as command but as pressure to become the shape that could stop it. Saint, weapon, banner, instrument, key. Every faction in the chamber had a word for making her useful.

Serathiel lifted the white bough from its plinth.

"Mara Venn," she said. "By witness public and cinder mark manifest, I offer sanctuary under the Pale Bough. Your power will be taught. Your body will be guarded. Your grief will be given form. No crown will own you."

It sounded beautiful.

That was the danger.

Mara saw Saelith hearing it with the part of herself still trained to long for beautiful law. She saw Ilyr's hand tighten on his blade because Khar Veyl knew the cost of truths hidden for safety. She saw Arveth's dead face close, remembering every regime that had said preservation while building a cage. She saw Kesh's eyes flick over exits, calculating whether sanctuary could be stolen from.

Mara thought of Joryn telling her to keep small because small had once meant alive.

She thought of the mirror's worst Mara, willing to spend others for one rescue.

She thought of Mordane's numbers.

She thought of the children with a mitten full of work tokens.

"No," Mara said.

Serathiel's expression softened. That was worse than anger. "Fear speaks first."

"No," Mara said again. "That was me."

The white bough brightened. "You do not understand the danger you pose."

"I understand enough to know everyone here keeps describing my danger as if it begins when I choose instead of when you claim."

Mordane's eyes moved to the coil. He was waiting. Let saint and rebel pull at each other, then take the system while they named virtue at one another.

Mara stepped onto the empty plinth.

Saelith gasped. "Mara."

Serathiel stilled, hope and alarm crossing her face so quickly that only someone watching for possession would have seen both.

Mordane smiled.

Mara looked down at the unfinished carving of her name.

"No saint," she said.

The plinth cracked.

"No weapon."

The cinder cage at her hip snapped open one finger's width. Blue-white heat rose, but she did not reach for the key. She did not open it farther. The chamber held its breath.

"No banner with a girl buried inside it."

She drove Niv's token into the carved name.

The plinth split down the middle.

The crown coil shuddered.

Serathiel raised the bough. Saelith caught it with both hands.

Light exploded between them.

Saelith screamed, but she did not let go. "Ask her!"

"She will die untaught!"

"Then teach by asking!"

"That is not how power survives."

"It is how people do."

Saelith wrenched the bough downward. White light cracked against the plinth and ran through Mara's broken name into the coil. For one breath, the coil had two commands available: Mordane's arithmetic and Serathiel's sanctity. Both reached for Mara.

She gave them neither.

"Arveth," she said.

The dead witness understood. He opened the ledger of stolen names and placed it on the broken plinth beside her. Not Mordane's ledger. The witness ledger. Ink, paper, corrections, uncertainties, names marked incomplete rather than forced.

"Read," Mara said.

Arveth began.

Not loudly at first. Not magically. He read as a clerk reads when accuracy matters more than drama. Lysa Mar. Mav Corren. Tomas Vale. Halea Voss. Pell Orwick. Essa Brant. Tollen Reed. Orra Pell. Maelin Noct-Vey, retained, status unknown. Joryn Venn, living hold, freed. Unknown woman with blue thread. Unknown child, found under hospice cloth. Unknown worker, left hand missing two fingers, held in witness until named.

The crown coil received the names as input.

It did not know what to do with them.

Mordane lunged for the coil controls.

Ilyr intercepted him. Their blades met not in a grand duel, but in three ugly movements near a brass console. Mordane had a concealed knife and enough skill to make surprise dangerous. Ilyr had spent a life distrusting polished rooms. He cut Mordane's sleeve, then the console line, then the shadow under Mordane's hand so the hidden command glyph there spilled visible black light across the floor.

"There," Ilyr said. "The other half."

Kesh drove a stolen signet into the exposed glyph and twisted. "And there is the half with paperwork."

The coil bucked.

Above them, the dead in the court began shouting. Not all in words. Some in sound. Some in movement. Some by falling where they chose to fall. The crown coil tried to turn witness into command and failed because witness did not move in one direction.

Serathiel staggered back from Saelith, bloodless for the first time.

"You have broken sanctuary," she whispered.

Saelith, still holding the cracked bough, shook her head. "No. I found the door."

Mara stepped off the ruined plinth.

The cinder cage closed at her hip.

She had not become saint. She had not become weapon. She had become a person standing in a chamber full of systems built to make personhood impractical.

That would have to be enough.

Then the floor under the crown coil split, and the heat from the foundry roared up.""",
    32: r"""## Chapter 32: Names in the Furnace

The undercroft opened into the furnace throat.

It was not a room. It was the place rooms were built to avoid naming.

Below the cracked crown coil, a shaft dropped through stone and brass into the heart of the foundry. Walkways clung to its sides in broken rings. Pipes crossed it like ribs. White-thread cables snapped and whipped in rising heat. At the bottom, far enough down that distance became terror, the dragon-heart glowed through layers of glass, iron, and old bone. Every time it beat, the shaft filled with light, and every dead body in Harrowmere shuddered between command and self.

Mordane had fallen to the first lower ring.

He was hurt. Not enough. One arm hung wrong. The blank ledger had landed beside him, spear still pinning it half open. He dragged it toward the crown coil's lower control with his good hand.

"Persistent," Kesh said, peering over the edge.

Mara did not look at him. "Can we reach the ring?"

"Yes, but in the sense that falling is travel."

Tavi's voice crackled from a wall pipe, thinner now. "There is a maintenance ladder on the west side. Also, the furnace index is overloading. Also, if anyone cares, my cinderbreak device is now on fire in three colors, only two of which I designed."

"Can it hold?"

"The device?"

"The names."

There was a pause.

"Not unless the furnace receives them faster than command can reclaim them."

Arveth looked down into the shaft. "The furnace is where the names were taken inward."

Mara understood. It made her stomach twist.

"So we carry them there."

Serathiel stood at the edge of the split floor, the cracked white bough in one hand. "If you send names into a ruptured dragon-heart, you may wake every cinder tied to this node."

"They are already waking."

"Not like this."

Ilyr looked at the red-black glow below. "She is right."

Mara turned to him.

"Khar Veyl has a phrase," he said. "The moon below hears through broken names. I thought it was metaphor. I am beginning to dislike our poets for accuracy."

"Will this wake Orrowen?"

"It may remind Orrowen that Harrowmere exists."

"That sounds bad."

"It is."

Mara looked at Arveth. "And if we do not?"

The dead witness held the ledger against his chest. "Mordane retakes the coil. The dead kneel. The city learns that witness is a dangerous interruption best left to ministers and saints."

No clean doors.

Mara was getting tired of rooms designed that way.

Saelith leaned on the broken plinth, pale with blood loss and light-spent hands. "If you go down, I can shield the heat for a short while."

"With permission," Kesh muttered.

Saelith gave him a flat look. "I have become insufferable about it, yes."

"Growth is unpleasant to be near."

Mara started toward the west ladder.

Serathiel caught her arm.

Not hard. That was why Mara did not pull away immediately.

"If you survive this," the saint-general said, "you will need training."

"Probably."

"From someone who understands cinder witness."

"Do you?"

The question struck more deeply than insult. Serathiel released her.

"I understand what uncontrolled power costs."

"Then learn what controlled people cost."

Mara climbed down.

The west ladder burned her palms even through bandage and ash-callus. Kesh came after her because, he said, if she died owing him several invoices his accounting would suffer. Ilyr moved down the wall without ladder, all shadow and balance. Arveth descended slowly, the ledger tied to his back. Saelith remained above, singing no hymn, only breathing light into a heat shield each time Mara said yes. Serathiel stood beside her after a long moment and added her own light, not around Mara, but around the cracking chamber.

That mattered.

Not forgiveness. Not alliance. A first correct placement of power.

On the lower ring, Mordane had reached the control.

"You are late," he called up.

His voice had lost its softness. Under it lived pain and something smaller than pain: humiliation.

Mara dropped the last six feet onto the ring. Heat slammed into her knees. The dragon-heart beat below, enormous and unhurried.

"You keep saying that," she said.

"Because it is the central fact of your life. Late to your father's truth. Late to your brother's capture. Late to governance. Late to the realization that systems do not care whether you feel righteous while breaking them."

He pulled a lever.

The furnace throat lit white.

Across Harrowmere, every hook flared.

Above, through the pipe, Mara heard the court cry out. Caldus shouting. Brakka roaring. Joryn's voice, distant and furious. The dead in the court were being dragged back toward kneeling.

Arveth opened the witness ledger.

The heat nearly tore the pages from him.

"Read," Mara said.

"The furnace will burn the book."

"Then read faster."

Arveth smiled. "At last, an editorial note."

He began.

Names went into the furnace throat.

Each one struck heat and became more than sound. Lysa Mar entered as a woman who hated furnace draw and wet boots. Mav Corren entered with blue-thread shirts and a wife who refused to let him lose anything. Tomas Vale entered with two bad whistle notes and a mother dead last spring. Pell Orwick entered with floodwater around his knees and a goblin aunt pulled from a cart. Essa Brant entered humming in a drain against command. Tollen Reed entered with road memory and slate messages. Halea Voss entered with appeals filed after death and one dry word, late. Joryn Venn entered not as leverage but as brother, miner, terrible singer, his own.

Mordane slammed the lever again.

"You are feeding sentiment into a furnace."

"No," Arveth said. "Correction. We are feeding evidence."

The furnace changed color.

Not cooler. Truer. Blue-white heat braided with red-gold, then with the black shimmer of shadow-script, the green spark of goblin contract teeth, the white of broken hymncraft, the gray of troll vow-stone dust, the dull orange of honest valves keeping tenements warm.

The dead above began choosing again.

Mara felt each choice like a spark landing on her skin. Stand. Fall. Hold. Leave. End. Strike. Protect. Some choices contradicted each other. Some came too late to save the body making them. It was ugly, uneven, alive in the broadest and most painful sense.

Mordane stumbled as the coil rejected his command.

He looked genuinely bewildered.

"They are dead."

Mara stepped toward him. "You keep saying that like it means empty."

"It means ended."

"No. It means you stopped listening."

He raised the blank ledger between them. Its pages filled again, desperate now, with columns that would not hold straight. The names Arveth read crawled across the numbers. Unknowns refused to become zeros. Mordane's own handwriting twisted and smudged.

"You cannot govern from exceptions," he said.

"These are not exceptions. They are people."

"People die."

"Yes."

Mara thought of all the dead who had not been saved, whose names were still missing, whose bodies had chosen furnace or collapse or had no choice left to make. She would not turn them into a pretty answer.

"And you do not get to use death as a deed of ownership."

Mordane struck at her with the ledger.

Ilyr caught his wrist. Kesh hooked the spear through the ledger spine and yanked. The book tore free, pages spinning into the furnace shaft like startled birds. Each page burned with a number before the names ate through it.

Mordane lunged after the ledger.

Mara caught him by the sleeve.

For one second she could have pushed.

The mirror shard in her wrist burned, reminding her how easy it would be to call that justice. Mordane's death would be useful. Clean. Popular. His fall would make a shape everyone understood.

She did not push.

"Witness custody," she said.

Mordane stared at her, furious.

Then the lower ring broke.

The choice vanished under physics.

Kesh grabbed Mara's belt. Ilyr caught the ladder. Arveth seized Mordane's torn sleeve with one dead hand. The ring tilted toward the furnace throat. Heat roared up. The dragon-heart opened wider below, not hungry exactly, but awake enough that hunger and grief were beginning to resemble each other.

Mordane looked at Arveth holding him.

"You?" he said, as if insulted that a dead clerk should decide his weight.

Arveth's face was calm. "Witness custody."

The sleeve tore.

Mordane fell.

He did not scream until he understood no system had caught him.

The furnace took the blank ledger first. Then the minister who had written too many people into it.

Mara did not feel triumph.

She felt the shaft shake as every remaining command tied to Mordane snapped loose at once.

Above, the dead cried out.

Arveth clung to the broken ring. His hand, the one that had held Mordane, was burning with black cinder fire. It climbed his arm toward the ledger tied to his back.

"Arveth!"

He looked at Mara. "If the witness ledger burns here, the names scatter into the furnace without record."

Kesh reached for him. "Then climb, clerk."

Arveth shook his head. "The ledger must go up. The command residue must go down."

Mara understood and refused in the same breath. "No."

"Do not command me."

The words stopped her.

Arveth unfastened the ledger and thrust it toward Ilyr. "Take it. Copy it. Argue with it. Correct it when wrong."

Ilyr took the ledger with both hands.

Arveth smiled at Mara. "Personhood is not declared once."

"It is maintained," she said, and her voice broke.

"Yes. Maintain it loudly."

Then Arveth let the black fire take him.

He did not fall like Mordane. He stepped backward into the furnace throat as if entering an archive that had kept him waiting too long. For a breath, his shape burned bright with every name he had carried. Then the fire opened around him, and the command residue that had clung to the dead across Harrowmere went with him.

The hooks above went dark.

The dead were free.

The dragon-heart woke.""",
}


EXPANSIONS: dict[int, str] = {
    30: r"""The undercroft door swallowed Mara's party, but the city battle did not pause politely behind them.

Above, Caldus discovered that holding a line without command was more difficult than commanding one. Men kept looking to him for orders because armor, scars, and habit had trained them to. The freed prisoners looked because he had opened their door. The hesitant soldiers looked because he had given them a word that did not require obedience to feel like courage. Even the king looked once, as if hoping the disgraced knight might tell him how to be innocent too late.

Caldus refused the old shape.

"Tesson," he called. "Where do you need shields?"

Tesson Vair stared at him for half a heartbeat, then pointed with a bloodied hand. "East gallery stairs. If those guards reach the horns, they cut Othen off."

"Take six."

"I asked where, not for permission."

Caldus almost smiled. "Then I will take six."

He did, and the difference mattered. He did not gather knights. He gathered whoever stood nearest and understood the stair: a baker with a cleaver, two former soldiers, one palace footman who had removed his livery coat, Rakka Fen with a stolen baton, and the young guard with the split lip. They reached the stairs as crown loyalists pushed down from the gallery. Caldus lifted his shield and felt old training rise in him, all clean lines and formal calls. He let it pass. This was not a parade ground. This was a stair full of frightened people with different reasons to be brave.

"Do not let them cut the horn," he said.

Rakka Fen snorted. "That all?"

"No. Do not die for furniture."

"Better."

Across the court, Brakka's road kept changing.

Each vow-stone needed a living or dead hand to keep it honest. If no one bore the promise, stone became stone again. So civilians became bridge-keepers. A laundress pressed both palms to a cracked column and whispered the shelter vow while children passed under it. The schoolmaster from the charcoal yard held a stair-lane open by reciting names from a broadside whenever panic tried to turn the passage into a crush. Harl Brim sat on a fallen statue and shouted at dead workers by trade, not number: "You with the left-hand limp, did you work east bellows? East bellows, stand if you can hear me." Sometimes one stood. Sometimes none did. Harl kept shouting.

Brakka saw a nobleman trying to force his way through the children's lane with two guards and a jeweled cloak.

She picked him up by the back of the cloak.

"This road carries small feet first."

"I am Lord Veyr."

"Road is sad for you."

She set him behind a group of ash widows and returned to the breach before he decided whether outrage could survive proximity to her maul.

The dead in the court were no longer one thing.

That was the hardest truth for the living to accept. People wanted them blessed or monstrous, saved or dangerous, victims or army. Instead they were a broken crowd with wounds no one could sort quickly. Halea Voss helped Arveth's assistants identify Orrowen dead by old academic marks and funeral knots. Lysa Mar, having been led up from below by Rakka's people, stood at a furnace-brazier and struck any command cable that lit within reach. Tomas Vale remained on his knees with the broken lever clutched in both hands, refusing whatever tried to reclaim him by falling whenever command said rise.

Joryn found Caldus at the east stairs when the second push came.

"Mara went down?"

"Yes."

The word should have been enough. It was not.

Joryn looked toward the undercroft door, every protective instinct in his body pulling one way while the injured mother and baby behind him pulled another. He was no soldier. He was half-collapsed from the conversion pen. Still, he took a fallen spear and wedged it through the gallery rail to slow the charge.

"She always did find the worst crawlspaces."

"She learned from someone."

Joryn grunted. "If that is a compliment, make it shorter."

The guards hit the stair.

Caldus held the first blow. Joryn, with mine-yard practicality, used the wedged spear to trip the second man into the third. Rakka laughed. The young guard swore. The palace footman hit a loyalist with a serving tray and looked astonished by his own politics.

At the breach, Dilla's voice rose over the chaos. "Soup line moving west! If you can swing a ladle, you can carry water!"

Water began passing hand to hand through the court. For burns. For smoke. For people whose courage had turned into coughing. It was ridiculous and exactly right.

The city was not winning because it had become an army.

It was surviving because it remembered how to work.""",
    31: r"""The chamber of claiming did not end when the plinth broke.

It became more dangerous.

Breaking a symbol in front of the people who believed in it did not make belief vanish. It made belief bleed. Serathiel's oathkeepers stared at Saelith as if she had cut a branch from their own bodies. The chapel guards looked between the saint-general and the broken plinth, uncertain whether to seize Mara, Mordane, Saelith, or the whole impossible room. Mordane, even wounded by the exposed glyph, watched uncertainty the way a starving man watched bread.

"You think refusal frees you," he said. "It only multiplies claimants."

Mara stood among the pieces of her own carved name and felt how true that might become. Above them, people were already chanting names. By nightfall some would chant hers. By tomorrow someone would draw her with cleaner hands and better hair. A week from now, if armies did not arrive first, children might dare one another to touch the broken throne step where the ash girl stood. Every story would try to make her easier to carry.

"Then I will keep correcting them," she said, though exhaustion made the promise feel enormous.

Arveth, still reading, gave a faint nod without looking up.

Serathiel lowered the cracked bough. Her voice had lost none of its beauty. That made the hurt in it sharper. "Dawnmere, you have mistaken consent for wisdom. A drowning person may consent to the wrong hand because it is nearest."

Saelith's hands shook. "And a rescuer may hold too tightly and call the drowning gratitude."

"You speak like her."

"No," Saelith said. "I speak near her. There is a difference."

Mara felt that difference like warmth offered at a distance.

The crown coil surged again. All around the chamber, the old crowns on their plinths rang. Each crown had belonged to a dead ruler, and each had been wired into the coil as a ceremonial amplifier. Their names were engraved in gold, polished, preserved, honored beyond use. Beneath them, in the lower foundry, workers had been stripped of names so those crowned names could glow.

Kesh saw the same ugly geometry. "That is excessive even by palace standards."

"Can you disconnect them?" Mara asked.

"Probably. Can I do it while Serathiel's people decide whether I am a blasphemy or a locksmith?"

"Yes."

"I admire your confidence from a distance."

Ilyr moved with him, cutting shadows under the plinths so Kesh could reach the hidden clasps. The first crown toppled. The coil's light dipped. A chapel guard shouted and lunged. Saelith lifted one bloody hand.

"Stop."

The guard stopped. Not because she commanded with hymncraft. Because she had been his superior once, and habit caught him before doctrine did.

She saw it and dropped her hand as if burned.

"No," she said. "Choose."

The guard stared at her. "Oathkeeper..."

"Choose."

His staff lowered, not all the way, but enough.

Serathiel's face closed. "You are teaching disobedience as virtue."

"No," Saelith said. "I am learning obedience is not innocence."

Another crown fell. Kesh's fingers flew over the clasps. "Royal dead are weirdly cooperative once robbed of wiring."

Mordane reached the lower control and drove his bloodied hand into the glyph Ilyr had exposed. The coil answered him with a howl. The empty plinth where Mara's name had been carved tried to pull itself together, fragments sliding across the floor toward her boots. New letters formed, not in stone this time, but in cinderlight.

SAINT.

WEAPON.

ASSET.

THREAT.

BANNER.

The words circled her.

Mara's breath shortened. A title was only a hook with better manners. The words pressed against her skin, each offering a reason to stop being only a person. Above, the city needed her. Below, the dead needed names. Joryn lived because others had carried risk. Arveth's voice shook from reading too long. Saelith bled. Kesh and Ilyr cut crowns loose. Tavi kept valves alive from a burning regulator. Every fact said become enough.

The cinder cage opened another finger's width.

Power rose. Not command yet. Possibility.

Mara's hand moved toward it.

Saelith saw.

She did not grab Mara. She did not sing. She did not throw herself between Mara and the cage.

She asked, "Do you want me to stop you?"

Mara froze.

That question gave her back the breath titles had stolen.

Did she?

Part of her did. Part of her wanted someone else's hand to keep her clean. Part of her wanted to be stopped so she would never know whether she might have become the reflected Mara after all.

"No," Mara said.

Saelith's face flickered with fear.

Mara closed the cage herself.

The cinderlight words broke apart.

"I wanted the choice," Mara said.

Serathiel looked from one woman to the other and, for the first time, seemed not certain whether she was witnessing corruption or a form of holiness her order had failed to define.

Mordane did not waste uncertainty. He tore the spear from his blank ledger, spilling black light from the spine, and hurled the broken weapon into the lower mechanism.

The coil split the floor.

Heat roared up, and the chamber of claiming became a throat leading down to the furnace.""",
    32: r"""The ledger was heavier than Ilyr expected.

That should not have mattered. He had carried bodies. He had carried secrets through three kingdoms and one underground court that punished truth by making it expensive. But Arveth's witness ledger dragged at his arms as if the names inside had weight separate from paper and ink. Perhaps they did. Perhaps that was the lesson everyone else had been late to learn.

"Do not drop it," Kesh said from the broken ring above him.

Ilyr looked up. "Your tactical insight is unmatched."

"I am emotionally invested in the clerk's dramatic last request."

"So am I."

That ended the joke.

Arveth burned below them.

Not as the command-bound dead burned, not as fuel. The black cinder fire had taken the residue from his body and revealed the witness underneath: a man who had been executed by regimes that feared records, a scholar who had kept personhood sharpened into procedure, a dead citizen who had insisted that unknown was not the same as empty. His outline stood in the furnace throat for one breath longer than flesh should have allowed. Then it broke into sparks that moved upward, not down.

Each spark found a hook.

Across Harrowmere, hooks went dark.

In the Crown Court, Halea Voss touched her own throat and laughed once, a dry astonished sound. Lysa Mar dropped her shovel and then, after considering, picked it up again by choice. Tomas Vale let go of the broken lever. The unknown dead worker with the vow-stone in his hand sat down on the marble and did nothing at all, which made three civilians burst into tears because nothing was the first thing anyone had allowed him to do.

In the conversion pen, Joryn felt the last white loop fall limp beside his boot.

He did not know Arveth well. Not really. A dead clerk with precise manners, irritating honesty, and a way of making grief feel entered into the record whether grief wanted dignity or not. Still, when the loop fell, Joryn bowed his head.

"Witnessed," he said, because Mara would want someone to say it.

Below, Mara did not hear him.

She heard the dragon-heart.

With Arveth gone and Mordane's command residue burned, the furnace had no single tyrant's will to resist. That did not make it safe. The cinderbreak device had opened names. The witness ledger had protected them from scattering. The district valves had kept the living warm. But the dragon-heart under Harrowmere had been cut, mined, regulated, lied to, and fed stolen dead for longer than any human in the room could imagine. Freedom arrived to it not as comfort but as impact.

The heart beat again.

The shaft widened.

Stone cracked in a ring around the lower platform. The maintenance ladder tore loose. Saelith's shield above flared white and nearly failed. Serathiel, beside her, lifted the broken bough and added power without command, her face rigid with effort and with the humiliation of learning from the student she had come to retrieve.

Tavi's voice came through the pipe in a burst of static. "Mara, if the heart vents straight up, palace, court, and three warm districts become historic steam."

"How do I stop it?"

"You do not stop a dragon-heart."

"Tavi."

"You give it somewhere honest to send the pressure."

Mara looked down. "The foundry stacks."

"Yes, if Brakka's road can move people clear and Othen opens the ash flues."

Othen answered before Mara could ask. "Flues are manual."

"Where?"

"Lower east. Full of heat. Bad place to stand."

Kesh looked toward the lower east catwalk, where three red wheels glowed through steam. "Naturally the honest pressure exit is on fire."

Ilyr tied the witness ledger across his back, then stepped toward the catwalk.

Mara caught his sleeve. "No."

"I can reach it."

"You are carrying the names."

"All the more reason not to be where the platform collapses."

"Ilyr."

He stopped. She had not used his name like that before, not as command, not as suspicion, but as a witness to the person under the usefulness.

Kesh sighed. "I will do it."

Mara stared. "You just said it was on fire."

"Yes. I have been brave for worse compensation."

"Kesh..."

"Vent-girl, I am small, quick, professionally offended by locked wheels, and currently less burdened by the sacred dead than our gloomy friend. Also, if I die, Narka will blame you so thoroughly that history will need a side appendix."

No one laughed. Kesh looked annoyed by that.

"Fine," he said. "I will not die. Better?"

He ran.

Mara and Ilyr held the broken ring while Kesh crossed the lower catwalk through steam. Twice he vanished completely. Once he screamed a curse so elaborate that Tavi, over the pipe, shouted, "That part is not load-bearing!" He reached the first wheel and threw his whole body against it. It did not move.

"Contract tooth," Mara shouted.

"What?"

"Your uncle's tooth in the cinderbreak. Bargain magic. What did it bind?"

Kesh's face changed. He pressed his bloodied thumb to the wheel. "Road opens if risk is shared."

The wheel turned.

The second turned when Ilyr cut his palm and pressed shadow-script into the pipe from above. The third turned when Brakka's voice boomed through the shaft from the court, speaking bridge-law down the flue until the metal remembered it connected places rather than owned them.

The ash flues opened.

The dragon-heart vented.

Not upward through the throne. Out through the foundry stacks, over the slag fields, into the gray morning air above Kell Ashgate and Harrowmere. A pillar of blue-white ash rose, full of names, not burning them, carrying them. The city saw. The mining roads saw. The Seven Arches, far off across the star canyon, trembled under Brakka's old vow. In the Gloamfen, Auntie Grum shifted in sleep. In Khar Veyl, black bowls of memory water cracked. In Lumenorath, white roots recoiled from their own bells. Deep under Orrowen, something like a moon turned in its grave.

The dragon-heart spoke through the vented ash.

Many voices. Too many. Old, wounded, curious, furious, relieved, afraid.

You woke us.

Mara held the ring with both hands and answered without opening the cage.

"We woke names you were being used to burn."

The voices moved around that. Some accepted. Some did not care. One grief-heavy presence listened more deeply than the rest.

Too soon, it said.

The words rolled through Mara's bones.

Then the lower platform broke.

Kesh leapt for the catwalk rail. Ilyr caught him by the scarf again. Mara grabbed Ilyr's belt. Saelith's light caught Mara from above, asked through pressure rather than words, and Mara did not have breath to say yes but thought it with her whole body. The light held. Serathiel's joined it. Brakka's vow-stones ground against cracking rock. Othen vented the last pressure through the stacks.

The furnace throat stopped widening.

The foundry did not survive.

Its command lines were dead. Its rails hung broken. Its regulator cracked. Its crown coil split like a rotten tooth. But the city above did not freeze. The hospice pipes held. The lower districts held. The dead were no longer kneeling.

Mara climbed out of the furnace throat with ash in her hair, burns on her hands, Arveth gone, Mordane gone, and the first dragon words of a larger war still ringing under every thought.

At the top, Joryn was waiting.

He took one look at her and said, "You brought my token back?"

Mara began to laugh.

Then she began to cry.

The city bells rang without command.

No one knew what to do with silence afterward.

Not a true silence. The foundry still groaned as metal cooled badly. People still shouted above. Somewhere a wall fell with a crash that made Kesh flinch and then pretend he had been preparing to duck anyway. The ash flues roared like distant surf. But the command rhythm, the constant under-beat of hook and rail and crown coil, had stopped. Its absence was so large that everyone kept listening for it to return.

Mara sat on the broken upper ring with Joryn's token in her palm and discovered she did not have enough body left for standing.

Joryn sat beside her because he had even less.

For three breaths they said nothing. Then he took the token from her hand, turned it over, and frowned.

"You scratched it."

"I drove it into a saint plinth."

"That is not what I gave it to you for."

"What did you give it to me for?"

"To bring back unscratched."

She laughed again, a raw small thing. He leaned his shoulder against hers. The old version of him would have pulled her away from the ledge, told her to stop looking at the furnace, made the world smaller until it fit around the two of them. This version looked down with her.

Below, the place where Arveth had stepped into the fire still glowed.

"Who was he?" Joryn asked.

Mara wiped her face with the heel of one bandaged hand and made a mess of ash and tears. "A clerk."

Joryn nodded as if that explained everything important. "Good one?"

"Annoying."

"Ah. Important, then."

Ilyr climbed up from the lower ring with the witness ledger strapped to his back. He moved carefully, not because he was hurt badly, though he was, but because the book had changed how he occupied space. He reached them and knelt, setting the ledger between Mara and the furnace.

"It is intact," he said.

Mara touched the cover. The leather was warm. Arveth's handwriting remained inside. So did errors marked uncertain, names half known, places where he had refused to make truth prettier than evidence. She had thought grief would arrive as a blow. Instead it came as work still waiting.

"We need copies," she said.

Kesh groaned from the catwalk. "She is grieving into administration. The clerk has possessed her."

Ilyr's mouth twitched once. "He would object to the terminology."

Saelith descended last, half supported by Serathiel. The sight was so strange that Mara forgot to be diplomatic. The saint-general looked as if she had swallowed a winter thorn. Saelith looked half-dead and stubbornly present.

"Is the city safe?" Mara asked.

Serathiel answered before Saelith could. "Safer than it should be."

"That is not an answer."

"It is the only one honest enough for the hour."

Mara accepted it because she was too tired to argue with accuracy. Saelith lowered herself onto a step, breathing through pain.

"The dead above are choosing," Saelith said. "Some are leaving the court. Some are asking to be witnessed into final rest. Some are simply standing. The living do not know whether to help, fear, kneel, or apologize."

"All of those sound reasonable," Joryn said.

Mara looked toward the shaft. "Can they hear Arveth?"

Ilyr opened the ledger to the first page. A small line of ash had appeared in the margin, not written in ink, not burned through. Just ash arranged with impossible precision.

Witness continues.

No signature.

It did not need one.

Mara pressed her fingers to the words.

The dragon-heart shifted below, and all of them went still.

The grief-heavy presence was not speaking now. It was listening. That was somehow worse than being threatened. A threat had direction. Listening could become anything.

Tavi's voice cracked through the pipe, weak but triumphant. "Anyone not dead, please report. Anyone dead but administratively active may also report, but speak clearly."

Mara closed her eyes. "Alive."

"Injured?"

"Yes."

"Define."

"Later."

"Everyone says later when they mean Tavi will be angry."

Othen cut in. "District valves stable. Foundry command dead. Palace reserve gone. We will need crews on every pipe by nightfall or victory gets cold."

There it was again. Work. Not glory. Not ending. Work.

Mara opened her eyes and saw the road beyond this moment: Caldus still holding the court, Brakka's vow-stones keeping lanes open, the king with no numbers to hide behind, Mordane gone but his systems not yet dismantled, Serathiel watching her with a new and dangerous uncertainty, Khar Veyl hearing Maelin's retained line, Lumenorath hearing Saelith's no, Orrowen perhaps hearing the phrase Ilyr feared.

The foundry had fallen.

The world had noticed.

Mara stood because the floor needed someone on it who had no business being a statue.

"Then we go back up," she said.

Joryn caught her wrist before she could move.

"Mara."

She looked down.

He held out the scratched token. "You still owe me this returned properly."

She closed her fingers around it. "I am standing right here."

"For now."

It should have sounded like accusation. It did not. It sounded like the beginning of letting her go before either of them was ready.

Mara wanted to promise she would come home before anyone needed her elsewhere. She wanted it badly enough to know the promise would be a lie. So she squeezed his hand once, hard, and let truth stand smaller than comfort.

Above them, the city bells kept ringing, uneven and human, while the dead learned what hands were for when no hook pulled them.""",
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
        'current_form: "full-length draft zero with Book One chapters 1-32 revised in pass 01; continuing literary revision needed"',
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
    print(f"Book One chapters 30-32 revised. Word count: {total}")


if __name__ == "__main__":
    main()
