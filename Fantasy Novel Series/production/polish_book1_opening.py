#!/usr/bin/env python3
"""Revision pass 01 for Book One.

This pass replaces the generator-heavy opening chapters with bespoke prose and
updates metadata word counts. It intentionally leaves the rest of the epic
draft intact so the book stays in the requested page range while revision work
continues chapter by chapter.
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
    1: r"""## Chapter 1: The Girl in the Vent

The first rule of cinder work was never to answer anything you heard under the mountain.

Mara Venn had been told that before she was old enough to lace her own boots. Her mother had said it while rubbing lampblack out of Mara's hair with a rag soaked in vinegar. Her brother Joryn had said it the first time he took her downshaft and showed her where the stone sweated silver ash. Foremen said it without looking up from their ledgers. Priests said it after blessings, as if the warning were part of the prayer. Even the old runners, the ones with white burns webbed across their throats and coughs that sounded like gravel poured into a bucket, said it when the vents began to moan.

Never answer. Never whistle back. Never speak your name where the stone can learn it.

Mara had obeyed that rule for sixteen years, which was longer than most rules survived in Kell Ashgate. She obeyed it now with her cheek pressed to hot rock, her left shoulder wedged under a lip of black granite, and her right hand stretched into a crack barely wider than her wrist. Somewhere ahead, beyond the reach of her fingers, a valve chain clicked softly in the dark.

"You got it?" called Foreman Sedge from the crawl mouth.

His voice came thin through thirty feet of vent, flattened by heat and distance. Behind him, Mara could hear the pay bell in the yard and the wet coughing of the next runner waiting his turn. Not a boy. He would have said something stupid by now if he were a boy. Maybe old Harl, then, with his bad knees and five daughters. Maybe Ness, who had lied about her age so she could draw a half-share before winter.

Mara pushed two fingers deeper into the crack. The skin over her knuckles split. She felt blood slick the stone and hiss away.

"Almost," she lied.

The vent breathed around her.

That was what the guild called it, anyway. Breathing. A miner's word for a miner's terror. Cinder vents opened when the buried hearts under Kell Ashgate warmed and closed when they cooled, though no one in the city agreed on whether those hearts were dragon, giant, god, or only stone with a furnace's temper. The crown scholars had their measurements. The chapel had its hymns. The miners had burns.

Mara trusted burns.

Heat rolled over her in a slow pulse. The cloth over her mouth dampened at once. She counted through it because counting was better than thinking. Five heartbeats in. Three heartbeats holding. Seven heartbeats out. The rhythm had saved her more times than prayer. When the heat drew back, she shoved her shoulder hard against the rock, ignoring the scrape of skin, and caught the valve chain with the tips of two fingers.

It slipped.

She bit down on a curse. Cursing wasted air. So did fear, but fear was quicker than she was.

The vent tightened behind her with a soft mineral groan.

"Mara?" Sedge called.

She hated the way he said her name, already subtracting the cost of losing her from the value of the valve. A runner dead in the vent meant paperwork, a half-day delay, and maybe two pennies to the family if the company decided she had not been careless. The company loved that word. Careless. It could make a corpse guilty of anything.

Mara flattened herself until stone pressed her ribs like hands. The chain brushed her nail. She hooked it, twisted, and pulled.

Nothing happened.

She pulled again. Her fingers screamed. Her wrist jammed so tightly between the rocks that the bones ground together.

Then the chain gave.

Far ahead, beyond the dark, a valve opened with a clang that traveled through the vent and into Mara's teeth. The next breath of the mountain rushed past her, hotter but cleaner, dragging silver ash away from the lower galleries where men and women were trying not to die before payday. A cheer rose somewhere below, muffled by stone.

Mara allowed herself one grin into the filthy cloth over her mouth.

That was when something under her answered.

Not a sound. Not exactly. The vent did not speak in words. It remembered them. A pressure moved through the stone beneath Mara's cheek, deep and slow and impossibly old. It carried the shape of a bell, the ache of a burned wing, the taste of rain falling on scales the size of shields. For a moment Mara was not in the vent at all. She was high above a world without roads, looking down at forests uncut by axes and rivers that had never learned to turn mill wheels.

Then the memory folded, and inside it something said her name.

Mara.

Her whole body went cold despite the heat.

Never answer anything you heard under the mountain.

The rule stood in her mind as clear as a chapel door. She could almost hear Joryn saying it, his voice low and fierce, one hand on her shoulder the day she first asked why runners did not sing in the dark like other workers. Because songs are made of names, he had told her. Because names are handles. Because the mountain takes what it can hold.

The stone pulsed again.

Mara Venn.

She should have crawled backward. She should have shouted for the rope. She should have bitten her own tongue before she let a word loose in that burning throat of rock.

Instead she whispered, "Who are you?"

The vent went silent.

Silence in a cinder vent was worse than groaning. Groaning meant the rock was shifting, which meant it had not yet decided to close. Silence meant the mountain had drawn breath and was holding it.

Mara knew her mistake at once. It moved over her skin like spilled oil. She tried to pull her hand free, but her wrist was still caught in the crack. Her blood had dried there, sealing her to the stone in a dark little crust. Panic struck so fast it stole the count from her. She jerked once, twice, and felt something tear.

"Rope," she tried to shout, but the word came out as a cough.

At the crawl mouth, Sedge was arguing with someone. "...not until she gives the second pull. You want the lower shaft flooded? You go in after her."

The next runner answered too softly for Mara to hear.

The mountain breathed in.

The walls pressed closer. Pebbles ticked against the back of her neck. Mara shoved her knees against the lower seam and twisted, skinning her hip through her patched trousers. Her trapped hand would not move. She imagined the vent closing around her forearm first, politely, like a door shutting on a sleeve. Then her shoulder. Then her ribs. The company would mark the time, recover what they could, and ask Joryn whether he wanted the death share in coin or meal credit.

The thought made something hot and mean flare in her chest.

No.

Not like that. Not as a line in Sedge's ledger. Not as two pennies and a company stamp.

Mara braced both feet against the narrowing stone and pulled until the world became white pain. Her wrist slid half an inch. Bone scraped. She pulled again, harder, because being careful had never saved anyone poor. Her hand came free with a wet sound, and she slammed backward through the vent just as the upper seam dropped low enough to tear hair from her braid.

"Pull!" she screamed.

This time the word carried.

The rope around her ankle snapped tight. She shot backward through heat and ash, elbows cracking stone, shoulder striking a bend hard enough to burst sparks behind her eyes. Hands seized the back of her jacket and dragged her into gray light.

For three breaths, Mara lay on the cooling grate outside the vent and did nothing but cough.

The world returned in pieces. Iron rails overhead. Sedge's boots, polished at the toe and caked with ash at the heel. The sour stink of sweat trapped under oilcloth. Harl crouched nearby with his rosary wrapped around one fist. Ness beyond him, pale and furious, not old Harl after all. The pay bell still ringing in the yard, late now, each strike a reminder that wages were counted by time spent useful.

Sedge bent over Mara. He had a face like a closed purse.

"Did you get the valve?"

Mara laughed once, which hurt more than coughing.

Ness swore at him. Harl touched two fingers to the charm at his throat. Sedge only waited.

Mara lifted her bleeding hand. The skin across her knuckles hung in strips. A crescent of black stone was embedded near the base of her thumb, small as a clipped nail and warm enough to smoke in the open air.

Sedge saw it. His eyes sharpened.

"Give me that."

Mara closed her fist before she knew she meant to. Pain burst up her arm.

The stone under the grate answered.

Not loudly. Not in any way the others seemed to hear. A tremor passed through the soles of Mara's boots and climbed her bones, gentle as a hand under deep water.

Do not give them what remembers you.

Mara stopped breathing.

Sedge reached for her wrist.

The pay bell outside cracked from crown to lip.

The sound split the yard open. Men shouted. Mules screamed. Somewhere below, in the lower galleries, every lamp guttered blue at once. Mara saw the color bloom along the walls, saw Sedge's face lose its blood, saw Harl drop to his knees and begin a prayer too old for the chapel to approve.

Under Kell Ashgate, something vast shifted in its sleep.

Mara Venn, said the stone beneath the city.

This time, Mara did not answer.

But every bell in Kell Ashgate did.
""",
    2: r"""## Chapter 2: Ash Wages

By dusk, the cracked pay bell had become everyone's fault except the company men who owned it.

Kell Ashgate crowded into the yard under a roof of brown smoke. The chimneys above the cinder house coughed without rhythm, each breath carrying silver grit that clung to hair, eyelashes, teeth, the wet corners of children's mouths. Miners stood in their work lines with lamps at their belts and soot dried into the creases of their faces. Runners huddled together near the grate, smaller than everyone else and trying not to look small, because small was useful until it became disposable.

Mara kept her torn hand tucked against her ribs. The rag Ness had wrapped around it had gone black with blood and ash. The cinder shard beneath the cloth pulsed now and then, warm enough to sting. She could feel it as a second heartbeat, slower than her own and much less afraid.

Foreman Sedge stood on the pay platform with three clerks, two soldiers, and the expression of a man about to explain hunger to the hungry. Behind him, the cracked bell hung in its wooden frame. The split down its side was clean and shining, as if something inside the bronze had opened an eye.

"Work stoppage," Sedge said. "Property damage. Safety disruption. Emergency recalibration of the lower ventilation works."

Someone near the smelter line muttered, "She opened the vent."

Sedge did not look toward the voice. He never looked toward voices when they belonged to people he could punish later from a ledger. "The company recognizes effort. The company rewards usefulness. The company also survives because every loss is counted."

Joryn Venn stood three places ahead of Mara, shoulders still powdered with gray stone from the deep galleries. He had come up early when word spread that his sister had nearly been shut into Vent Twelve. He had not embraced her in the yard. That would have made them both too visible. He had only touched her elbow once, hard, and placed himself between her and Sedge's line of sight.

The clerks began handing out wage chits. Full shares to the men who had been underground before the bell cracked. Half shares to the runners. Quarter penalty for anyone assigned to the disrupted shaft. No hazard bonus because the valve had opened successfully. No injury credit because Mara had exited the vent under her own strength.

When Joryn reached the platform, Sedge smiled with one side of his mouth.

"Your household caused delay."

"My sister saved the lower shaft," Joryn said.

"Your sister failed to surrender recovered company material."

The yard quieted in the way only a poor crowd could quiet: not empty of sound, but full of swallowed sound. Mara felt heads turn without seeing them. Her fist closed around the wrapped shard.

Joryn held out his hand for the chit. "What material?"

Sedge leaned forward. "Do not be stupid for love, Venn. It is expensive."

For one moment Mara thought Joryn might hit him. She saw the wish move through her brother's shoulders, saw the exact shape of it. Joryn was twenty-three, broad across the back, strong from stone and hunger, and he could have reached Sedge before the soldiers reached him. Then he breathed in through his nose, took the half-pay chit, and stepped down.

His face was calm when he passed Mara. That was how she knew rage had gone somewhere dangerous.

They did not speak until they reached home. Home was one room above Dilla's tallow shop, with two narrow beds, one cracked stove, a shelf of patched cups, and a ceiling stain that looked like a map of a country no one would want to invade. The shop below smelled of rendered fat and lavender oil. In winter, the smell thickened and climbed the stairs until everything they owned seemed to sweat.

Joryn barred the door, checked the window, then held out his hand.

"Show me."

Mara unwrapped the rag. Blood had dried into the weave. When the cloth came free, the shard sat in the swollen meat below her thumb, black as old coal and crescent-shaped. Heat shimmered above it.

Joryn went very still.

"Tell me you did not answer."

Mara looked at the floorboards.

"Mara."

"It knew my name."

Joryn closed his eyes. For a moment he looked older than their father had ever lived to be. "Names are handles."

"I know."

"No. You remember being told. That is not the same as knowing." He crossed to the stove, took the small iron knife from its hook, and poured boiled water from the kettle over the blade. "Bite your sleeve."

Mara did. She had thought she was done with pain for the day. The knife taught her she had been optimistic.

Joryn cut the shard out with quick, brutal care. Mara shook so hard the bedframe knocked against the wall. Once, when the blade scraped stone, the lamps in the room burned blue and the ceiling stain rearranged itself into the shape of wings. Joryn whispered every prayer their mother had known and two she would have slapped him for using.

At last the shard clicked into a chipped cup on the table.

It looked smaller there. Harmless, if one had never worked below mountain roots or watched a bell split without being struck.

Mara spat out her sleeve. "We should throw it in the slag canal."

"Yes," Joryn said.

Neither of them moved.

From the street below came a long, low whine. One dog, then another, then every dog in the district. Their voices rose together until the whole lane sounded wounded. The shard warmed the cup. A hairline crack ran through the ceramic glaze.

Joryn wrapped Mara's hand with a clean strip torn from his spare shirt. He tied it too tight, then loosened it when she hissed. "Tomorrow you say nothing. You go nowhere near Sedge. You do not look at the bell. If anyone asks about the stone, you never saw it."

"And if the mountain says my name again?"

Joryn's fingers paused on the knot.

Outside, the dogs fell silent all at once.

"Then you make it sorry it learned," he said.
""",
    3: r"""## Chapter 3: The Bell That Rang Back

The chapel bell rang at midnight.

It had no right to. The bellkeeper had died three winters before, and the company had not replaced him because a dead bellkeeper did not draw wages. Since then, the chapel bell had rung only for crown inspections, mine collapses, and the rare funeral of someone whose family could afford enough oil to make a public grief of it. Yet there it was, striking once through the sleeping district, then again, and again, each note rolling down the street like a cartwheel over stone.

Mara woke with her hand on fire.

Across the room, Joryn was already sitting up, knife in hand. Pale light leaked from the chipped cup on the table. The cinder shard inside it had gone from black to the color of a coal buried under white ash.

The bell rang again.

The sound passed through the window, the floorboards, Mara's teeth. Beneath it came a second tone, lower and slower, too deep for bronze. It was not heard so much as endured. It moved through Kell Ashgate's foundations and pulled at the shard in the cup until the cup began to tremble.

"Do not," Joryn said.

Mara had not realized she was standing.

"I hear another one."

"Another bell?"

"Under us."

Joryn looked toward the floor as if expecting boards to split. "You are fevered."

Mara wished that were true. Fever was dangerous, but it belonged to the body. This belonged to the city.

She dressed in silence: trousers stiff with ash, patched coat, boots still damp from the yard. Joryn caught her sleeve before she reached the door.

"You go out there, you make it real."

"It is ringing whether I make it anything or not."

"Then let someone else answer."

Mara looked at him. In the dark, his face was all angles and old worry. He had spent most of his life trying to keep her alive by making her smaller in the eyes of the world. He had been good at it. She loved him for that and hated him for how well it had worked.

"No one else hears the second bell," she said.

That ended the argument badly, which was how most true things ended.

The streets of Kell Ashgate were filling with people in nightclothes and work boots. Lamps bobbed. Doors opened. Someone shouted for the chapel warden. Someone else shouted that the warden had been drunk since supper. Above the roofs, the bell tower rose black against a sky stained orange by furnace light. Its rope hung still through the open arch.

Still, the bell rang.

Mara took the alley behind the tallow shop, Joryn cursing softly behind her because he had failed to stop her and would now settle for failing nearby. Warm rain fell through soot and made the cobbles slick. Twice Mara nearly slipped. Each time the lower bell steadied her, not kindly, exactly, but with attention.

At the chapel square, the crowd had stopped at the iron fence. No one wanted to cross first. The chapel doors stood open. Blue light flickered inside.

Mara ducked under the fence.

"Mara," Joryn hissed.

"I know."

"You never know."

Inside, the chapel smelled of damp wool, old incense, and something sweet gone rotten. The bell rope hung in the center aisle, swaying though no hand held it. Each time the bell above struck, the rope jerked like a vein.

At the altar stood a miner.

For a breath Mara thought he was praying. His forehead rested against the rope. His hands hung at his sides. His coat was the brown canvas issued to lower-gallery workers, burned through at one shoulder. Then he turned, and the left side of his face came with him a moment late.

Joryn made a sound behind her.

The miner's mouth had been sewn shut around a brass work tag. The tag pulled his lower lip down so that black thread cut into gray flesh. His eyes were clouded. His boots left wet ash prints on the chapel floor though the night outside was rain, not ash.

The crowd beyond the fence began to murmur. Someone whispered dead. Someone whispered plague. Someone whispered royal mercy, and the whisper died as if ashamed of itself.

Mara stepped closer.

The dead miner lifted one hand. Not toward her. Toward the cup-sized hollow in the altar where offerings were burned. His fingers scraped stone, searching.

"He wants something," Mara said.

"He wants to bite you," Joryn said. "Possibly both."

Mara swallowed. "Do you know him?"

Joryn did not answer at once. That was answer enough.

"His name was Pell Orwick," he said finally. "West gallery. Two boys. A laugh like a busted pump."

The dead man's head twitched at the name.

Mara felt the cinder shard in her pocket pulse. She had not remembered taking it. Fear went through her so fast she almost dropped to her knees.

Pell Orwick.

The name did not sound like a handle. It sounded like a door.

Mara spoke it.

The dead man's eyes cleared.

It lasted only a heartbeat. In that heartbeat, he was not a thing, not a warning, not proof, not a monster. He was a man in terrible pain who knew he had come home too late. Tears welled in eyes that should not have been able to make them. His sewn mouth worked around the tag.

Joryn reached for the thread with his knife, but Pell shook his head hard enough to tear skin. He lifted one hand again and pointed to the altar hollow.

Mara looked inside.

There, under old ash and candle ends, lay a strip of royal black ribbon stamped with a mercy seal.

Outside, a horse screamed. Iron clattered on cobbles. The crowd scattered from the fence as masked soldiers rode into the square.

Pell's clouded eyes returned. His hand dropped. The rope jerked once more, and the chapel bell cracked from lip to crown with a sound like a bone breaking under the city.

Mara took the ribbon.

Joryn seized her arm.

They ran as the soldiers entered the chapel and the dead miner turned to bar the aisle.
""",
    4: r"""## Chapter 4: The Minister's Mercy

Lord Cael Mordane arrived the next morning in a carriage clean enough to be insulting.

Everything in Kell Ashgate carried ash. It lived in sleeve cuffs and bread crusts, in the wet corners of windows, in wedding veils folded away for daughters who might never have the coin to use them. Even the chapel saints wore gray noses unless someone scrubbed them before inspection days. But Mordane's carriage rolled through the south gate lacquered black and shining, with brass hubs bright as coins and curtains the color of fresh cream.

Behind it came relief wagons.

That was why people cheered.

Mara stood with Joryn at the edge of the pay yard while the wagons creaked in under royal guard. Sacks of barley. Salt pork. Lamp oil. Physician's chests. Blankets wrapped in waxed cloth. The sight of so much survival made the crowd forget its fear for a moment. Hunger could turn suspicion into gratitude faster than any sermon.

Mordane understood that. Mara knew he understood it by the way he waited before stepping down, letting the city see the food first and the man second.

He was not what she expected evil to look like. He was spare, neatly dressed, dark hair threaded with silver at the temples. His face had the calm of a ledger closed after balancing. When he climbed the platform beneath the cracked pay bell, he removed his gloves finger by finger and looked at the miners as if each of them mattered in a precise, temporary way.

"Children of the Crownreach," he began.

Joryn muttered, "That is never how anyone starts a sentence before improving your day."

Mara nearly laughed, which hurt because she had not slept.

Mordane spoke beautifully. He spoke of winter stores, of the crown's duty, of sacrifice shared between palace and pit. He named last year's collapse and the fever season before it. He praised Kell Ashgate's usefulness as if usefulness were a hymn. Men and women who had cursed the company twelve hours earlier wiped their eyes when he promised no child in the ash district would go without ration bread that week.

Then the physicians opened their chests.

The line formed at once. Coughs, burns, crushed fingers, bad lungs, fevered babies. Royal mercy smelled of alcohol, clean linen, and the sharp green paste the chapel used for infection. Mara watched soldiers guide the sick by categories. Workers fit for return. Workers fit for rest. Workers requiring transport to the mercy ward.

Transport.

The word crawled under her skin.

Near the third wagon, a woman from West Gallery began to cry. Not loudly. A thin, humiliated sound. Her husband had been marked for transport after a coughing fit. Two soldiers held her back while a physician with kind eyes explained that treatment in Harrowmere would save his lungs.

Mara saw the ribbon on the physician's sleeve: black silk stamped with the same mercy seal she had taken from the chapel altar.

Joryn saw it too.

"No," he said under his breath.

Mara turned to him. "We have to tell someone."

"Who?"

The question landed harder than shouting would have. The foremen were on the platform. The chapel wardens were blessing the wagons. The soldiers wore royal masks. The crowd was hungry enough to hate any person who endangered the food by asking the wrong question.

Mordane continued speaking above them, his voice warm with practiced sorrow. "No kingdom survives by pretending need is gentle. We endure because each citizen gives according to capacity, and receives according to wisdom."

At the edge of the yard, a dead miner in a new helm stood among the soldiers.

Pell Orwick's face was hidden, but Mara knew the angle of his shoulders. She knew the burn in his coat. He stood perfectly still while living men shifted around him. A strip of black thread showed beneath the helm's cheek guard.

Her hand went to the cinder shard in her pocket.

Pell's head turned.

Not much. Enough.

After the speech, the relief wagons unloaded half their cargo and rolled the rest toward the north road. The mercy wagons followed. They were black-paneled, windowless, and heavier than food wagons should have been after giving so much away.

Joryn said, "Go home."

Mara said, "Do not be stupid for love. It is expensive."

He flinched because she had used Sedge's words, and because they both knew she was right to wound him with them.

They followed from the alleys, then the drainage cut, then the scrub beyond the slag canal. The city noise thinned behind them. Ahead, the wagons stopped where the old quarry road dipped between two banks of black thorn. Soldiers dismounted. Physicians climbed down.

One wagon door opened.

The man from West Gallery was dragged out half-conscious. A physician held his jaw. Another took a needle threaded with black cord.

Joryn's hand clamped over Mara's mouth before she could cry out.

"Living first," he whispered against her ear. His own voice shook. "Evidence first. Rage after."

The physician pierced the man's tongue.

The scream that followed was not a sound Mara could obey around. She bit Joryn's palm, tore free, and ran.

She made it three steps before the cinder shard burned through her pocket and every dead thing in the wagon turned its head toward her.
""",
    5: r"""## Chapter 5: A Knight Without a Crest

Mara learned three things about royal soldiers in the next hour.

First, they did not like being bitten.

Second, they were faster than men in polished masks had any right to be.

Third, courage did not matter nearly as much as numbers.

She had a stone in one hand and a stolen surgeon's hook in the other when they dragged her back toward Kell Ashgate. Her lip was split. One eye had swollen half shut. The cinder shard, curse it forever, had gone cold the moment she needed it to burn someone useful. Joryn was gone. She had last seen him doubled over in the quarry road, two soldiers on him and a third raising a club. If she let herself think beyond that image, she would become too weak to walk, so she made hatred hold her up instead.

The soldiers took the old toll bridge because the main gate had filled with citizens waiting for ration bread. The bridge arched over a drainage channel thick with gray water and floating slag. On inspection days the company hung flags there so visitors could imagine the canal was picturesque. Today no flags had been wasted on truth.

"Keep moving," said the soldier on her left.

Mara spat blood on his boot.

He hit her hard enough that the world flashed white. When it returned, a man stood at the far end of the bridge.

He wore a travel-stained cloak and carried a shield with the crest scraped off. Not painted over. Scraped, gouged, punished. A sword hung at his hip. His beard was dark with rain, and his hair had been cut with either a knife or indifference. He looked like a beggar who had once known exactly how to stand before a throne.

"You have the wrong girl," he said.

The soldiers stopped.

Mara tried to place his accent and failed. Crownreach, yes, but not Kell Ashgate. Harrowmere, maybe. The capital made its words cleaner than its hands.

"Move," said the captain.

"No."

It was not a dramatic no. It was tired. That made the soldiers hesitate.

The captain laughed once and drew his sword. "Do you know whose warrant this is?"

"Mordane's."

"Then you know enough to step aside."

"I know enough to wish I had stepped sooner."

The first soldier charged.

The stranger broke him with the shield.

Mara had seen yard fights, tavern fights, knife fights over bread and debt. This was not that. The man moved with an economy that made violence look like work he disliked but knew well. Shield edge into wrist. Pommel into throat. Foot behind knee. Turn, breathe, strike. He used the flat of the blade until one soldier shouted, "Oathbreaker!"

Then the stranger's face changed.

Only a little. Enough that Mara understood she was watching a door open over a pit.

The edge came out.

By the time the last soldier stumbled backward, the bridge was slick with rain and blood. The captain dropped his sword and ran. The stranger let him. That told Mara more about him than killing would have.

He turned to her. "Can you walk?"

"I can bite."

"Useful, but not what I asked."

"Who are you?"

He looked past her toward the quarry road, then toward the town, calculating danger with the bleak competence of someone who had survived by arriving too late. "Caldus Renn."

The name meant nothing to her. His missing crest meant more.

"Are you a knight?"

"Not anymore."

"Did you rescue me?"

"Regrettably."

Mara almost laughed. Her face hurt too much.

He cut the rope around her wrists with a small knife. "Go home. Hide. Tell no one you saw me. Tell no one what you saw on that road. Forget the wagons if you want to live."

"My brother is on that road."

Caldus paused.

"Then pray he is dead."

Mara hit him.

It was a terrible punch. Her hand was injured, her stance was wrong, and she struck his mail under the cloak rather than his jaw. Pain burst up her arm. Caldus accepted the blow without blinking, which made her angrier.

"If that was comfort," she said, "you are very bad at it."

"It was not comfort. It was knowledge."

Behind them, the drainage canal moved.

At first Mara thought a body had surfaced. Then it stood.

Pell Orwick climbed from the gray water in his soldier's helm, uniform dragging with filth, sewn mouth working around the tag. His dead eyes fixed on Caldus. He lifted one shaking hand to his brow in a salute.

Caldus went white.

The dead miner held the salute.

"Sir," Pell forced through the stitches.

The word tore something open in Caldus Renn that no sword on the bridge had touched.
""",
    6: r"""## Chapter 6: The First Spark

Caldus tried to run from the dead man's salute.

Not with his feet. His body stayed on the bridge, sword still ready, shield still lifted between Mara and the road. But his eyes fled years backward. Mara saw it happen. Whatever he remembered was worse than the soldiers, worse than the quarry, worse than Pell Orwick standing in drainage water with thread through his mouth.

"Who did this to him?" Mara asked.

Caldus swallowed. "Men following orders."

"That is not an answer."

"It is the one they used."

Pell lowered his hand. The salute had cost him. Black fluid ran from the torn corners of his mouth. The brass tag through his tongue clicked against his teeth. Behind him, farther down the canal, more shapes moved under the water.

Royal shouts rose from the quarry road. The captain had found courage in reinforcements.

Caldus seized Mara's sleeve. "We leave."

"My brother."

"If we go back now, we die before reaching him."

"Then be useful and die in the right direction."

His grip tightened, not in anger but recognition. "You think rage is a map."

"It got me here."

"And now?"

Before she could answer, Pell jerked upright. His head turned toward the town. A command moved through him like a hooked chain. Mara did not hear words, but the cinder shard in her pocket did. It flared hot enough to scorch through cloth. Pell stepped toward her.

Caldus raised his sword.

"No," Mara said.

"He is under command."

"He is Pell."

The next dead man surfaced behind him. Then another. Four, six, nine. Miners in soldier masks. A woman in a chapel shift. A boy no older than thirteen wearing a courier's belt. Every one of them had a tag sewn through the mouth. Every one of them turned toward Mara.

The shard burned.

This time she did not hear a bell. She heard knots.

That was the only word her mind could make for it. Each dead person held a knot where a name should have rested. Around that knot, someone had tied command: stand, march, guard, silence, kill. The commands were not strong because they were powerful. They were strong because nothing inside the dead had been allowed to answer back.

Mara tasted ash and old rain.

Pell, she thought.

The knot trembled.

"Mara," Caldus warned.

Pell Orwick, she said inside herself, and then aloud because names belonged in air. "Pell Orwick."

The dead miner stopped.

The command chain pulled. Mara felt it pull through the shard, through her burned palm, through the place behind her eyes where memory lived. Something in the mountain answered. Not with strength. With witness.

"Pell Orwick," she said again. "West Gallery. Two boys. A laugh like a busted pump."

She did not know the last part from Joryn or herself or the dead man. It came with the name, warm and ordinary and unbearable.

The brass tag in Pell's mouth glowed red. Smoke curled from the stitches. The dead man's hands rose, not to salute, not to attack, but to clutch at his own throat.

Caldus stared. "How are you doing that?"

"Badly."

The tag burst.

Pell fell to his knees. His mouth opened around torn thread, and the sound that came out was not a groan. It was sobbing.

The other dead advanced.

Mara should have stopped. She could feel the cost already. It moved through her memories like water through ash, blurring edges. Her mother's face flickered, not gone but suddenly farther away. The smell of lavender from the tallow shop vanished, returned, vanished. She clung to it and nearly lost Pell's name.

Caldus stepped between her and the dead.

"Names," she gasped. "I need their names."

He understood too quickly for a man who wanted ignorance.

From inside his cloak, he pulled a packet wrapped in oilcloth. It was worn nearly soft from handling. He opened it with fingers that shook and revealed pages covered in close writing. Names. Ages. Work marks. Chapel transfer numbers. Prisoner descriptions. Some lines had been blurred by rain or thumbprints.

"I could not save them," he said.

"Read."

So he did.

"Essa Brant. Lower pump crew. Scar over left brow."

Mara repeated the name. The woman in the chapel shift staggered. Her tag smoked.

"Tollen Reed. Courier. No kin listed."

"He has kin now," Mara said, and spoke him back into himself.

The bridge filled with blue fire and human grief. One by one the command sigils burned out of dead skulls. One by one the dead collapsed, not lifeless, not living, but present. Pell crawled to the side of the bridge and vomited black water though he had no breath to lose.

The cost struck after the fifth name.

Mara forgot the color of her mother's eyes.

She knew she had forgotten because the absence had a shape. It was a hole punched through love. She made a sound, and Caldus faltered mid-name.

"Keep reading," she snarled.

He did.

By the time royal soldiers reached the bridge, nine dead miners stood between them and Mara Venn. Not under command. Not free in any simple way. But named. That was enough for the moment.

Pell turned toward the soldiers who had worn his obedience like armor. His torn mouth shaped one word.

"Run."

They did.

Caldus caught Mara before she fell. She tried to shove him off and discovered her legs had resigned from politics.

"My brother," she whispered.

"We will find him."

"Do not say we if you mean no."

He looked at the freed dead, at the oilcloth ledger, at the road where royal soldiers fled toward Mordane's wagons. When he looked back, something in him had chosen pain on purpose.

"We," he said.

Under the bridge, the canal water shivered. Far below Kell Ashgate, the cinder that had learned Mara's name listened to the names she had given back, and for the first time in all the years the city had burned its dead for warmth, the mountain sounded almost afraid.
""",
}


EXPANSIONS: dict[int, str] = {
    1: r"""The bell did not stop after the first impossible answer.

It rolled through Kell Ashgate in uneven waves, not ringing now so much as remembering being rung. The cracked pay bell in the yard gave its broken note. The chapel bell took it up, deeper and cleaner. Then the small handbells in the company infirmary began to shiver on their hooks, and the mule bells in the cart sheds, and the rusted warning clappers above the lower shafts that had not moved since Mara was eight and the south gallery drowned twenty-seven workers in black steam.

Every bell answered every other, and under all of them Mara heard the second sound.

The city had a bell beneath it.

Not bronze. Not iron. Something older than metal, older than the mine roads and the company stamps and the little chalk marks families left on their doors when they could not pay rent. Its voice came up through the grates in the yard and through the soles of Mara's boots. It did not ring with alarm. Alarm was a living thing, sharp and brief. This was recognition.

Foreman Sedge backed away from her.

That, more than the bells, frightened the miners.

Sedge was not a brave man, but he was a company man, and company men were paid to stand still while other people flinched. When he retreated, a space opened around Mara on the grate. Harl remained kneeling. Ness stared from Mara's bleeding hand to the bell and back again, her mouth parted, her young face trying to decide whether it had seen a miracle, a crime, or the beginning of a very bad week.

"Nobody touches her," Joryn said.

Mara had not heard him arrive. One moment Sedge's hand had been reaching for her wrist. The next, Joryn stood between them, still in his lower-gallery harness, lamp swinging at his hip, shoulders dusted white with powdered stone. He had come upshaft hard. Sweat ran clean lines through the ash on his face.

Sedge found his voice because men like him always did when the first fear passed and the ledgers returned. "Your sister is concealing company material."

"My sister is bleeding on company property," Joryn said. "You want to charge her rent for the blood too?"

Someone laughed. It was the wrong sound, too quick and too hungry. The yard shifted around it.

Sedge noticed the shift. So did the soldiers by the north gate. Their hands moved toward batons. Not swords, not yet. Batons were for workers, and the company preferred to remember the difference between punishment and war until forced.

Joryn bent and lifted Mara by the elbow. His fingers found the place below her sleeve where her pulse was racing. He did not look at her hand. He did not look at the shard. He looked at her face, which was worse, because Joryn could always read too much there.

"Can you walk?"

"No," Mara said.

His face tightened.

"I can run," she added.

It was a stupid thing to say. It made Ness laugh again, this time with a sob in it. It made Harl cross himself in the old way, thumb to brow, lips, heart, and throat. It made Joryn close his eyes for half a heartbeat as if asking whatever gods still listened to give him a sister with fewer opinions next time.

Then he put one arm around Mara's waist and walked her out of the yard while every bell in Kell Ashgate rang them through the gate.

No one stopped them.

That was how Mara knew the day had gone from bad to dangerous. The company could explain injury. It could explain delay. It could explain a cracked bell if given enough ink and a dead enough witness. What it could not yet explain was fear, and until it found a shape for that fear, it let her pass.

At the alley mouth, Mara looked back.

Sedge stood under the broken bell with his polished boots planted in silver ash. He was no longer looking at her hand. He was looking at the grate where she had lain, and then past it, down into the breathing dark.

The mountain had spoken in front of witnesses.

By morning, someone would decide whose fault that was.

Joryn took the long way home.

There were shorter routes through Kell Ashgate, but short routes belonged to people who did not have a half-conscious sister, a bleeding hand, and the attention of every bell in the city. He guided Mara through the boiler lane, then under the ropewalk, then behind the cooper's yard where steam from the barrel sheds rolled thick enough to hide them from the pay yard watch. Mara hated needing the support. She hated the way her knees forgot the argument every time she tried to pull away.

"Stop rescuing me so visibly," she muttered.

"Next time I will do it with a hat."

"A quiet hat."

"A hat of shadows."

The joke was old. Their mother had started it years ago after Joryn, aged ten and solemn as a chapel brick, declared that he would protect them all when he was grown. With what, little lord? she had asked, flour on her cheek, grief already living in the corners of her eyes. A sword? A crown? Joryn had answered, A hat of shadows, because Mara had been four and frightened of thunder and believed any sufficiently large hat could hide the house from storms.

Mara remembered that now with sudden, piercing clarity. Her mother's flour-white cheek. Joryn's missing front tooth. Rain on the roof. The memory felt placed in her hands by someone who wanted her to notice it before it could be taken.

She stopped walking.

Joryn tightened his arm around her. "What?"

"I remembered Mother."

"You do that sometimes. It is allowed."

"No. I remembered her because the stone wanted me to."

The steam curled between them. Joryn's face changed in the white drift, softened by fear he did not want to spend where she could see.

"Do not make it kind," he said.

"I am not."

"You are. You hear a thing under the mountain speak once, and already you are giving it wants that sound almost human. That is how hooks work, Mara. They do not begin by tearing. They begin by catching."

She had no answer. The shard in her palm still seemed to hold the aftershape of the memory, warm and intimate as a coal from a family hearth. That frightened her more than Sedge's reaching hand. A threat was easy to hate. A comfort asked to be trusted.

They passed old Barren's cooper shop, where rings of iron hung from rafters like black halos. Barren himself stood in the doorway, shirt open over a chest furred white with age, pipe unlit between his teeth. He looked at Mara's bandaged hand. Then he spat into the gutter.

"Bell cracked clean," he said.

Joryn did not stop. "Aye."

"Clean cracks are struck from inside."

"You a bellwright now?"

"I am old. Same thing, if the listener is desperate."

Mara looked back. Barren tapped two fingers to his brow, not a blessing, not quite warning. "Girl. If the lower dark calls again, ask what it paid last time someone answered."

Joryn's hand dug into her side.

They kept moving.

By the time they reached the tallow shop stairs, the bells had stopped. Their silence had weight. The whole district seemed to be waiting for the company to provide an official version of the impossible, preferably one that could be punished. Doors shut as Mara and Joryn passed. Curtains twitched. A child waved from behind a rain barrel until his mother yanked him back by the collar.

Mara had spent her life unnoticed except where her labor could fit. Now invisibility peeled away from her like burned skin, and she felt the air touch every raw place underneath.

At the stairwell, Joryn paused. "Before we go in, give it to me."

Mara knew what he meant. She opened her fist. The cinder shard lay black against the blood-wet bandage, small enough to lose, heavy enough to change the room around it. Joryn did not reach for it immediately.

"If I take this," he said, "and it speaks to me?"

"Do not answer."

He gave her a look.

"Yes," she said. "I heard it."

He took the shard with the corner of his sleeve, never letting skin touch stone. For all his caution, the lamps in Dilla's lower shop flared blue through the floorboards above them. A woman downstairs gasped. Joryn swore.

From somewhere below the city, the buried bell gave one final note. Not loud. Not even a sound the neighborhood could hear. It touched only Mara, or perhaps Mara was only the one foolish enough to admit being touched.

This time the note carried no word.

Only a feeling: old attention turning toward her family.""",
    101: r"""Dilla opened the door before Joryn knocked.

She was small, round-backed, and wrapped in a shawl that had once been red before the ash district taught it humility. A candle stub burned in one hand. In the other she held a skimmer from the tallow vat, which would have been funny if Mara had not seen Dilla use it to chase a debt collector down three flights of stairs.

"Inside," Dilla said.

Joryn blinked. "You do not know what happened."

"Every bell in the district screamed and your sister is leaking on my step. I have made a beginning."

The room above the shop had never seemed so small. Joryn barred the door while Dilla set Mara in the good chair, meaning the one with only one questionable leg. She unwrapped the bandage and clicked her tongue at the wound, not with pity but professional offense. Dilla had no formal training. She had simply outlived three husbands, two fevers, one riot, and every physician the company sent into the ash district. That gave her opinions.

"Something in it?" she asked.

Joryn set the shard on the table.

Dilla did not touch it. She did not gasp either. She leaned close, candlelight gathering in the wrinkles around her eyes, and whispered a word Mara did not know.

The shard answered with a pulse of blue.

Joryn stepped between Dilla and the table. "What did you say?"

"An old word for wakefulness."

"Why do you know an old word for wakefulness?"

"Because I was young once and pretty girls learn foolish songs from foolish boys."

"That is not an answer."

"It is the only one you have paid for."

Mara would have laughed if the room had not begun to tilt. Dilla caught her chin, forced bitter drops onto her tongue, and told her not to be dramatic unless she intended to charge admission. The medicine tasted of rust, honey, and punishment. It steadied the edges of things.

"Your father came here after the east seam spoke," Dilla said quietly.

Joryn's face closed. "Not tonight."

"Tonight came without asking you." Dilla looked at Mara. "He had a mark in his palm. Not like yours. Smaller. He said the mountain had mistaken him for someone else."

Mara's injured hand throbbed.

"Who?"

"He would not say. The next day he went downshaft and did not come back."

The shard cooled. The candle guttered. Outside, the district held its breath around the silence the bells had left behind.

Joryn picked up the shard with the sleeve again and put it into the chipped cup. His hands were steady now, which meant he had become very frightened indeed.

"No more old words," he told Dilla.

She looked at him sadly. "Boy, the old words have already remembered you."

Mara closed her eyes. Under pain, under fever, under the bitter medicine and the smell of tallow, she felt the mountain settle back into itself. Not asleep. Listening.

By morning, she knew, Sedge would come for the shard. The company would come for an explanation. The crown would come for anything the company feared.

Mara wanted, very briefly, to be the sort of girl who could hand every strange thing to an older person and receive an answer in return. But the room held only Joryn, who was too young to have become as tired as he looked, and Dilla, who knew old words but not safe ones, and a shard of black memory no sensible person would claim to understand. The world had not chosen a prepared soul. It had noticed a girl in a vent because she was there, bleeding and angry and inconveniently alive.

That felt less like destiny than bad management.

She slept at last in pieces. Each time she woke, the shard was still in the cup, Joryn was still in the chair, and Dilla's candle still burned in the room below. Ordinary things, all of them. That was what made them precious. Ordinary things could be taken without prophecy, without thunder, without any grand enemy declaring itself. The company had been proving that for years.

So Mara counted them before sleep could steal them: brother, room, candle, breath, name, door, rain, shard, and the stubborn beat of her own heart.

She did not yet know that the world had begun counting back.

It would count in bells first, then debts, then graves, then roads.

Mara, who had survived by staying uncounted, slept through the first lesson.

When dawn came, the lesson would still be waiting, patient as stone and less forgiving.

It had all the time buried things possess.

And somewhere in the sealed dark beneath Kell Ashgate, a buried heart knew the Venn family was still alive.""",
    2: r"""Mara did not sleep after Joryn cut the shard from her palm.

She lay on her narrow bed with her injured hand propped on a folded coat, watching blue light gather and fade inside the chipped cup. Joryn sat at the table until the candle guttered out, then stayed there in the dark. He had wrapped the shard in three rags and put a bowl over the cup. The bowl glowed at the rim. Neither of them mentioned that.

Through the floorboards came Dilla's soft footsteps in the tallow shop. The old woman lived below them and heard everything because walls in the ash district were built from thrift and apology. Twice she paused under their room. Twice she moved on. That was kindness in Kell Ashgate: the decision not to know something until knowing might save a life.

Mara flexed her fingers. Pain ran from knuckle to wrist, bright and mean. The bandage smelled of boiled linen and Joryn's shirt. He had torn the cleanest one for her, the one he wore to chapel on inspection days so the wardens could pretend he was merely poor and not furious.

"Say it," he said at last.

Mara turned her head. "Say what?"

"Whatever you have been trying not to say for an hour."

"The mountain knew me."

"That is not what you are trying not to say."

She hated him a little for knowing her. It was a small hate, domestic and familiar, the kind siblings stored beside love because there was nowhere else to put it.

"It warned me not to give the shard to Sedge."

Joryn exhaled through his nose. He did not call her a liar. That scared her more than if he had.

"When Father started hearing the lower vents," he said, "Mother made him sleep with wax in his ears."

Mara sat up too quickly. The room swung. "Father heard them?"

"Once. Maybe twice."

"You never told me."

"You were six."

"I became older."

"Not enough."

The words struck harder because they were not cruel. Joryn rubbed both hands over his face. He looked suddenly like a man who had been holding a door shut for years and had just heard something large lean against the other side.

"He answered," Joryn said. "Not like you. He was half-asleep, fevered from ash lung. He said he heard someone calling from under the east seam. He answered because he thought it was a trapped miner."

"What happened?"

Joryn's silence filled the room before he did.

Mara knew the family story. Everyone knew it because the company had written it on a death slip. Her father had gone down during an emergency pressure drop and failed to clear the seam before the vent closed. Careless. That word again. The company loved it because it had no witnesses and required no corrections.

"He was not careless," she said.

"No."

The shard under the bowl pulsed once, throwing their shadows huge against the ceiling. In that blue flicker, the stain above Mara's bed looked less like a map and more like a wing folded around a city.

Joryn stood so fast the chair scraped.

"Tomorrow," he said, "we throw it in the canal."

"You said that already."

"Tomorrow we mean it."

Mara looked toward the covered cup. She wanted to mean it. She wanted the shard gone, the bells silent, the mountain returned to the old arrangement in which it hated everyone equally and did not know her name.

But the company had wanted the shard. Sedge had wanted it badly enough to forget witnesses. That made it evidence, weapon, or bait. Possibly all three. Poor people did not throw away things powerful people feared. They hid them badly, argued about them, and hoped the hiding lasted one day longer than the danger.

"Joryn," she said.

"No."

"You did not hear what it sounded like."

"Good."

"It sounded hurt."

That finally turned him. "So do we. That does not make us safe."

Outside, the last dog in the district began to whine again. Not loudly. Just enough for the dark to notice.

Joryn took the bowl off the cup, wrapped the shard in a strip of oilcloth, and tucked it inside the loose brick behind the stove where they kept emergency coins. The shard's light vanished. The warmth did not.

"Sleep," he said.

Mara lay down because she was too tired to win another argument. Joryn stayed by the stove until dawn, one hand on the loose brick, guarding her from the thing they had decided not to throw away.""",
    3: r"""The soldiers reached the chapel doors just as Pell Orwick stepped into the aisle.

He did not move like a monster. That was what made it worse. His first step was clumsy, the boot scraping because the left leg had stiffened in death or in whatever had been done after. His second step found an old habit. Miners learned balance young or died owing rent. Pell's shoulders settled. His hands lowered. The dead man placed himself between the soldiers and the Venns with the exhausted practicality of a worker blocking a draft.

"By royal mercy," the lead soldier said, "stand aside."

Pell tried to answer. The stitches in his mouth stretched. A bead of black fluid slid down his chin.

Mara's stomach turned. Joryn pulled her backward toward the side passage that led to the vestry, but she could not stop watching the brass tag through Pell's tongue. It had numbers stamped above the name. Not mine numbers. Transfer numbers. Inventory numbers.

The soldier lifted his baton.

Pell moved first.

He did not strike hard. He simply caught the man's wrist and held it. The soldier screamed. Not because Pell crushed bone, though perhaps he did. He screamed because a dead hand had closed around him with human intention. The other soldiers surged into the aisle. Pell went down beneath them, and still the bell rope jerked, ringing the cracked bell above with a sound too broken to belong in a chapel.

"Move," Joryn snapped.

The vestry stank of mildew and old candle wax. Mara stumbled over a stack of hymn boards. Joryn barred the door with a bench and dragged open the rear shutter. It had been painted shut sometime before either of them was born. He put one shoulder to it, cursed, and hit it again. Wood split. Rain blew in.

Behind the vestry door, something heavy struck the bench.

Mara clutched the ribbon in her good hand. The mercy seal shone black in the dark, a little crown over a little flame. She had seen it on the wagons, on the physicians' sleeves, on the chapel stores where the poor lined up for cough paste after winter collapses. A good symbol. A kind symbol. That was why it made such a useful mask.

Joryn boosted her through the window into the alley behind the chapel. She landed badly, pain flashing up her injured hand when it hit stone. He followed, broad shoulders scraping brick. They ran bent low under wash lines, past rain barrels and the locked door to the undertaker's shed.

At the corner, Mara stopped.

"Pell."

Joryn turned on her with a face like thunder. "Pell is dead."

"He held the aisle."

"Because someone made him."

"No. Because I said his name."

Joryn opened his mouth, then closed it. The rain slid through his hair and down his jaw. In the chapel square beyond the alley, soldiers shouted. The cracked bell gave one last ugly note and fell silent.

"If that is true," he said, "it is worse."

"How can it be worse?"

"Because then there is still someone inside them when the crown uses them."

The words took the warmth from the air.

Mara had wanted proof because proof could become a weapon. She had not understood that proof could also become a wound too deep to close. Dead workers were horror enough. Dead workers who felt the command, who heard through it, who could be steadied by a name and then trapped again when the name faded - that was a cruelty with rooms inside it.

Joryn pulled her onward before the thought could finish breaking her.

They cut through Cobbler's Run, crossed behind the ration shed, and reached the tallow shop just before dawn began staining the smoke over the roofs. Dilla opened the back door before they knocked. She looked at their faces, the ribbon in Mara's fist, the blood on Joryn's sleeve that was not his.

"I am too old," Dilla said, "for whatever this is."

"Then do not ask," Joryn said.

"I did not say I was too old to help."

She let them in, bolted the door, and set water to boil. Only after Mara sat at the kitchen table did she realize she had carried a smear of Pell Orwick's black blood across her palm. It lay in the lines of her skin like ink that had chosen a story before she had.

From somewhere under the city came one soft answering note, too deep for any chapel bell.

Dilla froze.

Joryn looked at Mara.

Mara closed her hand around the mercy ribbon and understood that sleep was finished with them.""",
    4: r"""The shard gave Mara away before she reached the wagons.

It did not blaze like a heroic thing in a street play. It heated with the practical malice of a coal dropped into a pocket. Mara yelped, slapped at her coat, and stumbled from the black-thorn ditch in full view of two royal soldiers, a mercy physician, and the half-conscious man with the needle in his tongue.

For one breath everyone stared.

Joryn was first to move. He came out of the ditch low and fast, shoulder driving into the nearest soldier's knees. The man went down with a shout. Mara lunged for the physician's hand. The needle flashed. She caught thread instead of wrist, and the black cord sliced into her fingers as the physician jerked back.

"Alive," the physician snapped. "Do not damage her."

That was how Mara learned they knew more about her than she did.

The second soldier drew a baton. Joryn took the blow across his back and still managed to get one hand around the wagon door. Inside, shapes shifted in the dark. Not prisoners. Not all of them. Mara saw helmets, gray hands, brass tags. The dead crowded the wagon benches like workers riding downshaft before dawn.

Every head turned toward the cinder in her pocket.

The mercy physician was young. That was the detail Mara hated afterward. He had freckles across his nose and one of those soft mouths that probably made old women trust him with fevered children. He looked terrified when the dead stirred, but his hands kept working. Training did that. Training could make a coward efficient.

"Sedate the brother," he said. "The girl goes to Mordane."

Mara threw the mercy ribbon at his face. It did nothing except make him blink. Joryn shouted her name. A soldier caught her braid and yanked her backward so hard sparks burst behind her eyes. She kicked, missed, kicked again, connected with a knee, and nearly got free before the baton struck her shoulder.

Pain folded the world.

Through it she heard the wagons.

Not wheels. Not wood. The things inside. Commands moving from corpse to corpse in a language made of pressure and absence. Stand. Wait. Guard. Silence. Return. Each word hooked into the place where a name should have rested. The cinder shard answered them with a heat that felt almost angry.

Mara.

Not now, she thought at the mountain, as if ancient buried hearts respected timing.

Joryn had the physician by the collar. He was saying something into the man's face. Mara could not hear it over the sudden roar in her ears, but she saw the physician's expression change. Fear, then recognition, then calculation.

He had recognized Joryn.

A third soldier stepped from behind the wagon and struck Joryn at the base of the skull.

Mara screamed. She got one hand free, clawed the soldier holding her, and felt skin gather under her nails. Another baton came down. This time her knees went. The ash road rose up, hard and wet.

Boots moved around her. Joryn was dragged to the second wagon. He was limp but breathing. Mara tried to crawl. A soldier put one boot between her shoulder blades and pressed until mud filled her mouth.

The physician crouched beside her. His freckles were very clear from that close.

"You should have stayed invisible," he said. Not cruelly. Almost sadly.

Mara spat mud at him.

His sadness vanished.

They bound her wrists, but not with rope. With a strip of white cloth marked in hymn-script. The cloth tightened when she struggled. Light-elf work, though she did not know that yet. All she knew was that it smelled faintly of rain and marble and someone else's clean hands.

The wagons began to move.

Joryn's wagon went north.

Mara's guards turned her south, back toward Kell Ashgate and whatever questioning Mordane thought a girl from the vents deserved. She twisted until she could see the black panels through the trees. One curtain shifted. For half a heartbeat she saw her brother's hand hanging over the wagon bench, fingers streaked with ash.

Living first. Evidence first. Rage after.

Mara had failed at all three. But rage, at least, remained loyal.""",
    5: r"""Caldus Renn had been following the mercy wagons for six days when Mara ruined his plan by being alive.

He did not tell her that on the bridge. He would not tell her for some time. But the shape of those six days was already on him: the mud dried to the hem of his cloak, the bloodless set of his mouth, the way he counted soldiers before he counted exits because once, years before, he had counted mercy seals and believed them.

After Pell saluted him, Caldus lowered his sword.

Mara noticed because no one sane lowered a sword in front of the dead. The motion was small, almost involuntary, but Pell saw it. Something like relief moved across the dead man's ruined face.

"Sir," Pell said again, or tried to.

Caldus flinched as if the title had struck him.

The canal behind Pell began to bubble. More dead were coming up through the runoff tunnel, drawn by the shard or the bells or the command that had not finished with them. Caldus looked from them to Mara, then to the road where royal shouts drew closer.

"How many did you see in the wagons?" he asked.

"Too many."

"Living?"

"Some."

"Your brother?"

Mara's throat closed. She nodded.

Caldus swore, not loudly, but with the weary precision of a man adding one more stone to a sack already breaking his back. "Then listen carefully. I can get you off this bridge. I may be able to find the wagons. I cannot do both if you keep trying to sprint at every horror the crown places in your path."

"You talk like a manual."

"Manuals are written by people who survived mistakes."

"Or people who watched others die making them."

That landed. She saw it in his face.

Before either of them could use the wound, Pell moved. The command inside him had recovered from whatever Mara's presence disrupted. His arm lifted, stiff and shaking, toward Caldus's throat.

Caldus did not defend himself.

Mara did. She stepped between them and caught Pell's wrist with both hands.

His skin was cold. Not winter cold. Cellar cold. Stone cold. A body that remembered warmth but could not make it.

"Pell," she said.

His hand trembled. The command pulled against her through him, and the cinder shard burned in her pocket. For a moment Mara saw the hook inside his name. Saw how the brass tag held it open. Saw how the command had been nailed where speech should have lived.

"Pell Orwick," she said again.

Caldus stared at her. "How do you know that?"

"His wife probably knows it better. Help me get him back to her."

"He is dead."

"He is busy."

It was a stupid answer. It was also the only one she could bear.

The first royal soldier reached the far side of the bridge and stopped when he saw the canal dead gathering behind Pell. Men who would club a girl without hesitation became suddenly religious when corpses stood upright in daylight. One made a warding sign. Another raised a command rod, black iron with a cinder bead set into the tip.

The rod pulsed.

Pell screamed through his stitches.

Caldus moved then. He crossed the bridge in three strides, shield up, and smashed the command rod before the soldier finished speaking. The bead burst into sparks. Every dead thing in the canal jerked as if a chain had been cut and immediately tied again by clumsier hands.

"Run," Caldus said.

"You first."

"I am wearing mail."

"Then sink dramatically."

Kell Ashgate chose that moment to ring again. Not all its bells this time. Just the cracked pay bell, far behind them, one broken note moving through rain. The dead heard it. Pell heard it. Mara heard the bell beneath it, deeper than fear.

Mara Venn.

She clenched her injured hand.

"I said not now," she whispered.

Caldus looked at her as if deciding whether she was mad, cursed, or merely inconvenient. "Who are you speaking to?"

"The mountain."

He accepted that with the expression of a man whose day had already lost the right to disbelief.

Together, with royal soldiers gathering and the dead waiting for the next command, they backed off the bridge toward the tannery alleys, where Joryn's trail and Mordane's wagons had vanished into the ash-colored rain.""",
    6: r"""The freed dead did not know what to do with their hands.

That was the detail Mara remembered later, more than the blue fire or the burst tags or the way Caldus read names like a man cutting his own skin open line by line. Pell Orwick knelt on the bridge with both palms lifted before him, staring at them as if they belonged to a stranger. Essa Brant pressed her fingers to her mouth again and again, touching torn thread, touching absence, touching the place where speech had been stolen and returned imperfectly. Tollen Reed, the courier with no kin listed, kept smoothing his belt though every pouch on it was empty.

They were not free the way songs meant free. They were loose. Uncommanded. Present enough to understand damage and not yet steady enough to survive it.

Mara sat with her back against the bridge wall, shaking so hard her teeth clicked. The color of her mother's eyes had come back. Brown. No, hazel. No, brown with a ring of green near the pupil when she laughed. Mara clung to that correction like a rope. She repeated it under her breath until Caldus crouched beside her.

"What did it take?"

"Do not make me explain myself while I am trying not to vomit."

"I need to know if doing it again will kill you."

"Everything kills you if done enough."

"Mara."

The use of her name should have annoyed her. It steadied her instead, because Caldus said it like something that belonged to her.

"Memories," she said. "It takes memories. Or loosens them. I do not know. I lost my mother's eyes for a minute."

Caldus looked away.

"What did you lose?" she asked.

He folded the oilcloth ledger carefully, too carefully, and tucked it back inside his cloak. "The right to be surprised."

Before she could answer, Pell crawled toward them.

Caldus stiffened. Mara put a hand on his arm without thinking. Pell stopped an arm's length away and bowed his head. The movement pulled at the torn corners of his mouth.

"Joryn," Mara said. "My brother. Did you see where they took him?"

Pell's eyes clouded, cleared, clouded again. Whatever held him together was fragile. His name had made a bridge, but command had burned much of the country on either side.

"North," he forced out. "Black wagon. Not dead."

Mara closed her eyes.

Not dead.

It was not rescue. It was not safety. It was enough to stand on.

Pell reached into his ruined coat and drew out a small brass disk. A work token, the kind miners used to claim tools from the company cage. He pressed it into Mara's hand. On one side was stamped P. ORWICK. On the other, in scratches so faint she almost missed them, two smaller names: Lio. Tam.

His boys.

"Tell," he said.

"I will."

The word left Mara before she weighed it. Brakka was not yet in her life to call it a vow, but the world seemed to hear it anyway. The cinder shard cooled in her pocket. The cracked pay bell went silent.

Caldus stood. "Then we need the north road."

"We?"

"I said we once. I try not to waste words."

"You waste plenty. They are just gloomy."

That almost made him smile. Almost. It changed his face enough for Mara to see the man he might have been before mercy wagons and missing crests.

They moved before the soldiers recovered courage. Caldus guided the named dead into the tannery yard, where old hides hung in long brown rows and the stink discouraged casual witnesses. He spoke to them not as troops, not as monsters, but as people in shock. Sit here. Stay low. If command returns, hum. If you remember a name, say it to another.

Mara watched him and understood that whatever he had done, he had not begun as a coward.

At the tannery gate, she looked back toward the bridge. The rain had thinned. Beyond the roofs, the mountain rose black and veined with furnace glow. Somewhere under it lay the thing that knew her name. Somewhere north, Joryn rode in a mercy wagon toward a fate the crown considered useful.

Mara tied Pell's work token to the cord around her neck.

She had left the vent alive. She had answered the mountain. She had spoken the dead back into pain. None of it made her a hero. Heroes in chapel glass looked clean and certain and usually taller.

Mara was wet, shaking, hungry, and wanted by men with ledgers.

It would have to do.

They did not take the north road immediately. That would have been the brave thing, and bravery without food, maps, or the ability to stand upright was just another way to make the company write careless on a death slip. Caldus said as much while half-carrying Mara through a lane behind the tannery. Mara told him he had a gift for making cowardice sound organized. He said organization was how cowardice survived long enough to become strategy.

The named dead followed at a distance, not because anyone ordered them, but because no one else in Kell Ashgate would know what to do with them. Pell kept one hand on the wall as he walked. Essa Brant hummed through her torn mouth whenever her eyes began to cloud. Tollen Reed watched the roofs with a courier's habit, tracking paths no one had asked him to run. Each of them looked wrong in the gray morning, but wrong was not the same as evil. Mara held on to that distinction because everything else in her wanted to become simple and sharp.

Dilla opened the tallow shop door before Caldus knocked. The old woman took in Mara, the knight, the blood, the dead miners waiting politely in the alley, and the sword in Caldus's hand.

"No," she said.

Mara leaned against the doorframe. "You do not know what we are asking."

"I know enough from the queue."

"What queue?"

Dilla's mouth tightened. "Company men are taking names in the square. Anyone with a missing relative, anyone who saw chapel trouble, anyone who heard bells after midnight. They are calling it a witness roll."

Caldus said, "Witness rolls become arrest lists by supper."

"I guessed that, metal man."

"Knight," he said automatically.

Dilla looked at his scraped shield. "Not today."

For the first time since the bridge, Mara laughed. It came out small and cracked and nearly became a sob. Dilla's face softened by the width of a candlewick. She stepped aside.

"The dead stay in the rendering shed," she said. "If they drip on my floor, they mop. I am not running a charitable haunt."

Pell bowed with heartbreaking seriousness.

"Do not bow either," Dilla snapped. "That is worse."

Inside, the tallow shop was close and warm, crowded with molds, wick racks, and blocks of rendered fat wrapped in cloth. The smell should have made Mara sick. Instead it dragged her backward into childhood: her mother buying one blue candle for Midwinter because blue smoke was supposed to confuse fever; Joryn stealing a shaving of wax to plug a hole in Mara's boot; Dilla pretending not to notice because their mother still had her laugh then and the whole lane had been kinder around it.

Memory returned with pain attached. Mara pressed her injured hand to her stomach.

Caldus noticed. Of course he did. He noticed everything that could become fatal. "Sit."

"Stop ordering me."

"Fall, then."

She sat.

Dilla cleaned Mara's face with a rag soaked in herb water and asked no questions until the silence grew too full to be useful. Then she pointed at Caldus with the rag. "You. Why is the crown hunting children out of my attic?"

"Because one of them can unmake crown property," Caldus said.

"I am sixteen," Mara said.

"That was not the part I expected you to contest."

Dilla's eyes moved to Mara's bandaged hand. "Your father heard the lower vent once."

Mara went still.

Joryn had kept that secret like a sealed wound, and here Dilla spoke it while rinsing blood from a rag.

"You knew?"

"I knew your mother came down here three nights running for wax plugs and bitterroot tea. I knew your father stopped singing after the east seam answered him. I knew the company buried him with a closed mouth and an open debt. I am old, girl. Old women know the shape of lies because people stop hiding them properly."

Caldus had gone quiet. Mara did not look at him. If she did, she might see pity, and she had no room for it.

"What did he hear?" she asked.

Dilla wrung the rag out over a basin. The water went pink, then gray. "A name, I think. Not his."

The cinder shard in Mara's pocket cooled as if listening.

Outside, the rendering shed door creaked. One of the named dead had begun humming, low and uneven. Another joined. Not a song exactly. More like people trying to remember what songs were for.

Caldus moved to the window. "Patrol."

The word changed the room. Dilla set the basin down without a sound. Mara stood too fast, swayed, and caught herself on the table. Through the shutters she saw royal masks at the alley mouth, three soldiers and a company clerk with a witness roll tucked under one arm.

"Back stairs," Dilla said. "Roof to the cooper's loft. Then east. Do not step on the green tiles unless you want to meet old Barren by falling through his ceiling."

Mara stared at her.

"I said I was old, not dead. Go."

At the rear door, Mara stopped. The named dead waited in the shed, uncertain and terribly visible. Pell looked at her through the half-open door.

"They cannot climb roofs," she said.

Caldus looked toward the approaching patrol, then at the shed, and Mara watched the old machinery of command try to rise in him: abandon weight, preserve objective, save the living first. She hated that she understood it. She hated more that he did not say it.

Instead he opened the shed door. "Can you walk to the slag culvert?"

Pell nodded. Essa nodded after him. Tollen touched his empty courier belt and pointed toward a drainage lane.

"Then we divide," Caldus said. "Dilla, can the culvert still be opened from the soap yard?"

"With a pry bar and language."

"Kesh," Tollen Reed rasped.

Mara turned. "What?"

The dead courier swallowed air he could not use. "Kavik Road. Goblin guide. Owes Pell. Market under beast."

Dilla snorted. "Everyone owes Pell. Man lent like a fool."

Pell's ruined face changed. It might have been pride.

Mara touched the work token at her neck. The north road held Joryn, but north was watched. The dead had given her another road. Not safe. Not clean. Not free. A goblin road, then.

The patrol knocked at the front door.

Dilla lifted her chin and became, all at once, a harmless old shopkeeper with bad knees and no patience. "Go before I start enjoying this."

Mara climbed the back stairs after Caldus, every step sending pain through her hand, Pell's token knocking softly against her collarbone. Below, Dilla opened the front door and began lying with the calm, offended fluency of a woman who had sold candles to company wives for forty years.

By the time the soldiers entered the shop, Mara was on the roof, crawling east through chimney smoke toward a goblin debt, a hidden culvert, and the first road in her life that no company ledger owned.""",
}


def replace_chapters(text: str) -> str:
    pattern = re.compile(r"(?m)^(#{1,2}) Chapter (\d+): .*$")
    matches = list(pattern.finditer(text))
    by_no = {int(m.group(2)): m for m in matches}
    for chapter_no in sorted(CHAPTERS.keys(), reverse=True):
        match = by_no[chapter_no]
        start = match.start()
        later = [m.start() for m in matches if m.start() > start]
        end = min(later) if later else len(text)
        replacement = CHAPTERS[chapter_no].strip()
        if chapter_no in EXPANSIONS:
            replacement = replacement + "\n\n" + EXPANSIONS[chapter_no].strip()
        if chapter_no == 1 and 101 in EXPANSIONS:
            replacement = replacement + "\n\n" + EXPANSIONS[101].strip()
        text = text[:start] + replacement + "\n\n" + text[end:].lstrip()
        matches = list(pattern.finditer(text))
        by_no = {int(m.group(2)): m for m in matches}
    return text


def update_metadata(word_total: int) -> None:
    meta = METADATA.read_text(encoding="utf-8")
    meta = re.sub(r"produced_word_count: \d+", f"produced_word_count: {word_total}", meta)
    low = round(word_total / 300)
    mid = round(word_total / 275)
    high = round(word_total / 250)
    meta = re.sub(r"at_300_words_per_page: \d+", f"at_300_words_per_page: {low}", meta)
    meta = re.sub(r"at_275_words_per_page: \d+", f"at_275_words_per_page: {mid}", meta)
    meta = re.sub(r"at_250_words_per_page: \d+", f"at_250_words_per_page: {high}", meta)
    meta = re.sub(
        r'current_form: ".*"',
        'current_form: "full-length draft zero with Book One opening revised in pass 01; continuing literary revision needed"',
        meta,
    )
    METADATA.write_text(meta, encoding="utf-8")


def update_summary(word_total: int) -> None:
    if not SUMMARY.exists():
        return
    text = SUMMARY.read_text(encoding="utf-8")
    page_low = round(word_total / 300)
    page_high = round(word_total / 250)
    text = re.sub(
        r"\| The Ash Beneath the Crown \| `book-01-the-ash-beneath-the-crown` \| [\d,]+ \| \d+-\d+ \|",
        f"| The Ash Beneath the Crown | `book-01-the-ash-beneath-the-crown` | {word_total:,} | {page_low}-{page_high} |",
        text,
    )
    SUMMARY.write_text(text, encoding="utf-8")


def main() -> None:
    original = MANUSCRIPT.read_text(encoding="utf-8")
    revised = replace_chapters(original)
    MANUSCRIPT.write_text(revised, encoding="utf-8")
    total = word_count(revised)
    update_metadata(total)
    update_summary(total)
    print(f"Book One opening revised. Word count: {total}")


if __name__ == "__main__":
    main()
