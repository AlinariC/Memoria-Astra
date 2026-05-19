#!/usr/bin/env python3
"""Revision pass 01b for Book One Part II.

Replaces chapters 7-8 with bespoke prose introducing Kesh, the Gloamfen, and
the goblin market under the sleeping beast.
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
    7: r"""## Chapter 7: Kesh's Bad Bargain

The slag culvert east of Dilla's shop was not a road. It was a long stone throat full of runoff, rat bones, steam, and every object Kell Ashgate had decided was easier to lose than repair.

Mara crawled through it on her elbows with Caldus ahead of her and the named dead behind. Her hand throbbed against the filth. Pell's work token tapped at her collarbone. The culvert ceiling was so low in places that Caldus had to drag his shield beside him and breathe through his teeth. His mail scraped stone with a sound that made Mara want to apologize to every patrol within a mile.

"You are very loud for a man trying to hide," she whispered.

"I was trained to enter halls, not drains."

"That explains the smell."

"The smell is not mine."

"Heroic denial."

Behind them, Dilla's voice floated down through a street grate, sharp and offended. She was still lying to the patrol in the tallow shop, and judging from the pitch of her outrage, she had promoted herself from harmless old woman to insulted taxpayer. Mara wished she could see it. She wished more that Joryn could. He would have laughed quietly into his fist and then told her laughing was dangerous.

The thought of him in the black wagon put its boot back on her chest.

She kept crawling.

Tollen Reed led them after the first turn. The dead courier moved awkwardly, but memory lived in his bones even if breath did not. He knew drainage routes the way living couriers knew market alleys, by slope, echo, rat traffic, and old chalk marks above the waterline. Twice he stopped with one hand raised, and twice royal boots passed overhead close enough to shake grit into Mara's hair.

At the third stop, Pell began to hum.

The sound was ugly through his torn mouth, broken by thread and dead tissue, but Essa Brant took it up, then Tollen. Caldus turned sharply.

"What are they doing?"

"Not obeying," Mara said.

That was her best guess. The hum trembled against the cinder shard in her pocket, and she felt command brush past the dead like a hook searching dark water. The hum gave them something else to hold. Not a song. A fence.

Caldus listened, then nodded once. He did not like what the world had become. He had the look of a man making a list of things he would dislike later when they had time.

The culvert ended behind the soap yard in a gate of rusted bars. Dilla's promised pry bar leaned in the mud beside it with a note tied around the handle.

Kesh. South reed path. Do not trust his first price.

Mara read it twice. "Who is Kesh?"

Tollen tapped Pell's work token. "Debt."

"That is not a person."

"Often," said a voice above them, "it is."

Something small dropped from the soap yard wall, landed on the crossbar of the gate, and crouched there with perfect balance. At first Mara saw only a hood, long fingers, and a grin too bright for the rain. Then the figure pushed the hood back.

Green skin. Sharp ears. Black eyes ringed in amber. A scarf patterned with red road-knots. More pockets than seemed possible on one body, each tied, buckled, buttoned, or guarded by a tiny bell that had been muffled with wax.

"Kesh of the Kavik Road," he said. "Guide, appraiser, negotiator, occasional poet under duress. Current rate for desperate fugitives is five silver links, two meals, and first refusal on any portable mysteries."

Mara stared at him through the bars. "You are a goblin."

"And you are bleeding in a drain. See how names help everyone?"

Caldus shifted behind her. "Open the gate."

Kesh looked at him, then at the scraped shield. "Knight rate is higher."

"Not a knight."

"Scraped-crest rate is higher still. Comes with emotional baggage, often contagious."

Mara found, against all good judgment, that she liked him a little.

Pell shuffled forward. Kesh's grin vanished.

"Oh," the goblin said.

Pell held out one gray hand. In his palm lay another work token, not his own. This one was stamped with a mark Mara did not know: a curved road under three dots.

Kesh dropped from the gate and took it carefully, without letting his fingers brush Pell's skin. The gesture was not disgust. It was respect, or fear dressed as respect. Maybe both.

"Who did this?" Kesh asked.

"Crown," Mara said. "Company. Mercy physicians. Pick a knife."

Kesh turned the token over. His mouth had gone hard. "Pell Orwick saved my auntie at Black Reed Ford. Flood year. Pulled her cart out with one mule and a vocabulary unfit for children."

Pell's cloudy eyes cleared at auntie.

Kesh saw it. Swallowed. Put the token inside his vest.

"Four silver," he said.

"You said five," Mara replied.

"I am overcome by sentiment. It will pass."

Caldus stepped closer to the gate. "We need the north road."

"No, you need every patrol on the north road to be less interested in you than they currently are. Since none of us has magic for making soldiers intelligent, you need a different road."

"Joryn is north," Mara said.

"Many regrettable things are north. The trick is reaching them alive."

"Can you get us there?"

Kesh looked at her injured hand, the cinder bulge in her pocket, the named dead in the culvert, Caldus's sword, then the roofs where company whistles had begun to shriek.

"No," he said.

Mara's heart dropped.

Kesh unlocked the gate with a key he had apparently stolen from the lock itself. "But I can get you to someone who sells impossible. Come on, vent-girl. Dawn is getting expensive."

The south reed path began as a drainage ditch, became a goat track, then surrendered all dignity and turned into marsh. Kell Ashgate fell behind them in gray terraces, its chimneys coughing into the rain. Ahead spread the Gloamfen, black reeds and shallow water and fungal hummocks under a sky the color of unpolished lead.

Kesh moved through it like punctuation: quick, necessary, difficult to predict. He stepped on boards Mara could barely see, hummed to mud before trusting it, and once stopped the entire party so he could insult a tuft of yellow moss until it retracted three thorny feelers from the path.

"Royal map says this is impassable," Caldus said.

"Royal map also says my grandmother's market is a temporary illegal encampment. It has had three mayors, two revolutions, and a theater district."

"The crown does not know this road?"

"The crown knows many things. It understands fewer."

Mara nearly slipped from a plank. Kesh caught her elbow and released it before she could decide whether to resent him.

"You are carrying cinder," he said softly.

Caldus's hand went to his sword.

Kesh rolled his eyes. "If I wanted to sell her, scraped-crest, I would have opened with flattery."

"You did sell us," Mara said. "You said someone paid you to delay us."

"Not yet I did not."

"But someone did?"

"Someone paid me to watch for a small ash-runner with a burned hand, a sad knight, and dead company. I was to slow you on the south path until the third bell after dawn."

Mara stopped. The plank dipped under her boot.

"You took the money."

"Of course I took the money. It was lonely."

Caldus drew half an inch of steel.

Kesh sighed. "I also sold them a route description that puts their patrols waist-deep in a leech nursery for the next two hours. I contain multitudes. Some of them invoice separately."

Mara should have been furious. She was furious. But under it, treacherously, was relief. The road ahead did not become safer, but it became possible in the way bad bargains sometimes were: not honest enough to trust, not false enough to discard.

"If you delay me from finding my brother," she said, "I will feed you to your grandmother's theater district."

"Harsh. They prefer comedy."

"Kesh."

The goblin's grin faded just enough to show the person behind it measuring her pain. "I know what black wagons mean. I do not joke about that part."

He turned and led them deeper into the reeds.

Behind them, a horn sounded from Kell Ashgate. Another answered from the north road. Then, far to the west where no patrol should have been, came a wet chorus of men screaming in leech country.

Kesh brightened. "Ah. There are my customers."

Mara looked at Caldus. Caldus looked at the marsh. Pell began to hum again.

For the first time since the vent, Mara felt the shape of a road under her feet that no company had built and no crown had counted. It was crooked, treacherous, overpriced, and led away from the brother she needed to save.

It was still a road.
""",
    8: r"""## Chapter 8: The Market Under the Sleeping Beast

The goblin market was built around a monster.

Mara did not understand that at first because the monster was too large for her mind to assemble. She saw a hill in the marsh, long and moss-backed, with black reeds growing along its sides and pools of rainwater gathered in hollows. Then the hill breathed. Lanterns trembled across its flank. A line of market stalls rose and fell by the width of a finger.

Kesh put one hand over Mara's mouth before she could say anything interesting.

"Quietly," he whispered. "Grandmother sleeps light when strangers make theological noises."

Mara removed his hand with two fingers. "Your grandmother is the monster?"

"My grandmother owns the market. The sleeper is Auntie Grum."

"Of course it is."

"Do not sound judgmental. You have a mountain."

The market climbed Auntie Grum in ropes, stilts, plank bridges, and carts chained to old spear shafts sunk harmlessly into her hide. Goblin children ran along her ribs with bare feet and bells tied into their hair, though every bell had been stuffed with wool. Smoke rose from cookpots shaped like helmets. Eel skins dried between poles. A gnome argued with a goblin butcher over whether an invoice could be considered a threat if written in polite ink. Somewhere, a violin played under its breath.

The air smelled of frying root, wet fur, lamp oil, marsh mint, and the sour mineral tang of old relics. It was the first place Mara had ever entered that did not seem to care what the crown thought of it. That should have comforted her. Instead it made her aware of how many other powers might be waiting to care in worse ways.

The named dead drew stares.

Not screams. Not immediately. Goblins noticed danger the way cats noticed open doors: with interest first, then with decisions. Conversations thinned as Pell, Essa, and Tollen followed Kesh through the lower planks. Hands moved to knives, charms, ledgers, and children. A woman with a silver nose ring spat into a bowl and murmured a ward. A boy no older than ten leaned close to another and whispered, "They still got names?" The other boy shrugged as if this were the most important technical question.

Kesh heard it. "They do."

That changed the market. Not enough to make it welcoming. Enough to make it lawful.

At the base of a rope ladder, a goblin woman in a red coat waited with both hands planted on a cane made from polished bone. She was short even for a goblin, old enough that her green skin had darkened toward olive, and heavy with jewelry that looked decorative until Mara noticed how many pieces had sharp edges. Her ears were pierced from root to tip with contract rings.

"Kesh," she said.

"Grandmother," he replied, and bowed with a magnificence that made several nearby goblins snicker.

"You were sent to delay a fugitive."

"I delayed several soldiers."

"You were paid to delay the fugitive."

"I improved the contract."

"You stole the contract."

"I personalized it."

The old woman looked at Mara. Her eyes were black, bright, and entirely unimpressed. "You are the vent-girl."

Mara was beginning to dislike the name. "Mara Venn."

"Names cost here."

"So does silence."

The old woman's cane tapped once on the plank. Around them, the market paused more completely.

Kesh made a small strangled sound. Caldus shifted his weight. Mara realized too late that she had either passed a test or stepped in one.

The old goblin smiled.

"I am Narka of the Kavik Road. Kesh is my sister's daughter's least profitable child. You carry one of Pell Orwick's debts."

Mara touched the token at her neck. "He said to tell."

The market seemed to lean closer.

So Mara told them.

Not everything. Not the cinder's voice or the way names felt like knots under her skin. But she told them about the chapel bell, Pell's tag, the mercy ribbon, the black wagons, the dead in royal helms, and the man from West Gallery with a needle through his tongue. She told them Joryn had been taken north. She told them the crown was making workers from the unnamed dead.

When she finished, no one spoke.

Above them, Auntie Grum's flank rose in a long breath. The planks creaked. A jar rolled off a shelf and was caught by three goblin hands before it struck the ground.

Narka turned to Pell. "Is this witnessed?"

Pell stepped forward. The crowd drew back. He did not seem offended. Perhaps the dead had less room for insult when holding themselves together took so much work.

"Witnessed," he rasped.

"Do you claim your name?"

His torn mouth worked. "Pell Orwick."

"Debt?"

He lifted one gray hand toward Mara. "Tell Lio. Tell Tam."

Narka closed her eyes for a moment.

When she opened them, the market had already changed.

"A road will be found," she said. "A bad one, because the good ones are watched. Kesh, you will take her to Black Reed Ford, then through Old Jaw if the water has not risen."

Kesh's ears angled back. "Old Jaw is haunted by tax collectors."

"Then you will feel at home."

"Grandmother, I am wounded."

"Frequently, if wisdom finds you."

Tavi Quen entered the story by falling out of a hanging engine.

The machine was suspended from Auntie Grum's third rib by cables, pulleys, and the sort of confidence Mara associated with bad bridges. It coughed twice, spat green sparks, and dropped a small gnome into a pile of eel nets. The gnome bounced, swore in three languages, and emerged with a wrench in one hand and her goggles hanging around her neck.

"No one touch that lever," she shouted.

Every goblin in reach touched a different lever.

The machine screamed. Auntie Grum snorted in her sleep. The whole market rose two feet and dropped one. Stalls swayed. A cookpot slid. Caldus grabbed a support rope. Mara grabbed Kesh. Kesh grabbed his purse.

The gnome looked around as if only now noticing the audience. She was broad-faced, brown-skinned, and no taller than Mara's shoulder, with copper coils braided into her hair and burn marks up both sleeves. Her eyes landed on the cinder bulge in Mara's pocket.

"Oh," she said. "That is not market-safe."

Mara had spent the last day being hunted, beaten, named by a mountain, and dragged through a culvert. She did not have much patience left for gnomes falling from the sky.

"Neither are you," she said.

The gnome grinned. "Excellent. I am Tavi Quen."

Narka thumped her cane. "You owe me rent."

"I owe your market three demonstrations of applied ventilation."

"You blew smoke into my cousin's soup."

"A successful demonstration of directionality."

Kesh leaned toward Mara. "That means yes, she owes rent."

Before Mara could answer, a tremor passed through Auntie Grum. Not a breath. A twitch. Every goblin in the market froze.

The cinder shard in Mara's pocket warmed.

From somewhere below the monster's hide came a faint answering chime.

Tavi's grin vanished.

"Tell me," she said carefully, "that is not a raw cinder fragment next to a hibernating marsh titan with old dragon-bone in her spine."

Mara looked at Kesh.

Kesh looked at Narka.

Narka looked at the sleeping beast under all their feet.

Auntie Grum opened one eye.

It was the size of a chapel window and yellow as old wax. It rolled once, fixing on Mara with the offended weariness of a creature disturbed by history.

No one moved.

Then the memory moths came.

They rose from the reeds in a pale cloud, wings thin as onion skin, each marked with a black dot like an inkblot. At first Mara thought they were drawn to Auntie Grum's waking. Then the cloud turned in the air and poured toward her hand.

Kesh said something sharp in goblin.

Narka's cane struck the planks. "Cover your mouths. Speak no secrets."

Too late.

The first moth landed on Caldus's scraped shield. In a child's voice it said, "Mercy wagons go north by night."

Another settled on Kesh's sleeve and whispered, "I took both payments."

A third brushed Mara's cheek, and suddenly the market smelled of flour, thunder, and her mother laughing under a roof that did not leak. Mara gasped. The memory was not stolen exactly. It was tasted.

Auntie Grum's eye narrowed.

Tavi shoved a brass mesh cage into Mara's hands. "Put the cinder in here unless you want every secret in this market flying around with legs."

"Wings," Kesh said.

"I know what I built."

"You built moth legs?"

"Focus, criminal."

Mara took the shard from her pocket. The moment it touched the mesh, the cage glowed blue. The moths swarmed it, whispering in dozens of voices: debts, names, lies, recipes, betrayals, lullabies, last words. The sound battered Mara until she could not tell which memories were hers and which belonged to the market.

Pell's voice cut through them.

"Joryn Venn," he said.

The moths stilled.

Mara looked at him.

Pell pointed north with one gray finger, then east, then down.

Narka's face hardened. "Old Jaw, then."

Kesh swallowed. "That road is closed."

"Open it."

"By what authority?"

Narka tapped Pell's token at Mara's throat with the tip of her cane. "By debt. By witness. By the fact that if the crown is making soldiers from named workers, every road we own will be next."

Auntie Grum's eye closed. The market exhaled with her.

Mara stood in the hush with the glowing cage in her hands and understood that the world beyond Kell Ashgate was not kinder. It was stranger, older, and full of people who calculated survival in languages she did not yet speak.

But it had roads the crown did not own.

For now, that was enough.""",
}


EXPANSIONS: dict[int, str] = {
    7: r"""The road punished them for noticing.

Past the first reed wall, the marsh changed from wet ground into a set of negotiations. A patch of green water accepted Kesh and rejected Caldus's boot to the knee. A hummock that looked solid sank when stepped on, as if it had been waiting all morning to prove a point. Thorn vines leaned away from Pell and toward Mara, as if living plants understood the dead better than the living did. Twice, Kesh stopped to pay tolls Mara could not see: a copper shaving dropped into a frog's mouth, a whispered apology to a stump, three crumbs of black bread placed on a stone no larger than her thumb.

"Are you bribing the scenery?" she asked.

"Maintaining infrastructure."

"It is a frog."

"A respected local functionary."

Caldus hauled himself free of the green water with dignity badly damaged. "How much of this road is alive?"

Kesh glanced around. "How philosophical are we feeling?"

Mara would have laughed if a horn had not sounded behind them. Not close, but closer than she liked. Royal patrols were learning. That seemed unfair. She had hoped the marsh would keep them stupid longer.

Pell stumbled. Essa caught him, and the two dead stood for a moment hand to hand, balancing each other in the reeds. The sight quieted Mara more effectively than danger. The dead were tiring. She had not known the dead could tire. Perhaps it was not flesh that weakened but the names holding them to themselves. Pell's token lay cold against her throat.

"How far to your grandmother's market?" she asked.

"Far enough to regret asking. Close enough to start running if I say so."

"And are you saying so?"

Kesh tilted his head. His ears moved independently, listening to places Mara could not separate from rain.

"Not yet."

They crossed a plank bridge made from mismatched doors. Each door had a name carved into it. Some human, some goblin, some in marks Mara could not read. Kesh stepped on the edges, never the centers. When Mara did the same, he gave her a quick approving look, then spoiled it by saying, "Good. You can be taught, assuming you survive the invoice."

"You make jokes when you are afraid."

"I make jokes when I am awake. Fear is merely a loyal audience."

"Who paid you?"

His face shuttered.

Mara had not expected an answer. She asked because silence had weight, and sometimes throwing a question at it showed where the walls were. Kesh walked three more planks before speaking.

"A man with chapel-clean hands. Human. Capital vowels. Wore a physician's pin but watched like a broker. He knew your height, your hand, your brother's name, and that a dead courier might seek Pell's road debt."

Mara's stomach tightened. "He knew Joryn?"

"He knew to say Joryn where I could hear it."

"And you still took the money."

Kesh stopped on a door carved with seven goblin names and one human one. Rain ticked off his hood. "Vent-girl, I take money from enemies because enemies spend too much to lie badly. The trick is not purity. The trick is making sure, when the knife turns, you are holding the handle."

"And are you?"

For once, he did not grin. "Ask me after the market."

Ahead, something vast exhaled. The reeds bent in a slow circle. Warm air rolled over them, smelling of mud, old scales, and cooking smoke.

Kesh's grin returned, but softer now and much less careless.

"There," he said. "Try not to call Auntie Grum a hill. She is sensitive about geology." """,
    8: r"""It took the market ten minutes to become itself again after the moths.

That, Kesh assured Mara, was unusually fast. The last time memory moths had blown through, three marriages had ended, two had begun, one butcher had discovered she owed herself money under a childhood name, and Auntie Grum had rolled over in her sleep, flattening a tax office that everyone agreed had been asking for it.

"We do not speak of the tax office?" Mara asked.

"We sing of it twice a year."

Tavi set the brass mesh cage on a workbench bolted between two of Auntie Grum's old scale ridges. The cinder shard glowed inside like a sulking coal. Around it, the mesh hummed in three different pitches. Tavi listened with her ear nearly touching the wires, then pulled back and made a face.

"That is not a fuel shard."

Mara flexed her bandaged hand. "It came out of a vent."

"Many terrible things come out of vents. That is why civilized engineers build covers."

"Can you tell what it is?"

"Yes."

Mara waited.

Tavi found a pencil behind one ear, discovered it was broken, found another in her hair, and began writing on the back of a fish wrapper. "I can tell that it is old, awake, responsive to name pressure, contaminated with blood contact, resonant with corpse-command structures, and likely to attract every dangerous scholar, priest, engine-wright, grave singer, and ambitious idiot within courier distance."

"That is many words for no."

"Precision is not verbosity when lives are at stake."

Kesh leaned against the bench. "She also means no."

Tavi pointed the pencil at him. "I mean no with supporting evidence."

Narka arrived with three goblins carrying ledgers, a covered basket, and a map drawn on eel skin. She snapped her fingers. Nearby merchants resumed pretending not to listen.

"The Old Jaw road opens at low blackwater," she said. "It runs below the north patrol line and comes out two miles east of the mercy road. It is unpleasant, semi-legal, and occasionally carnivorous."

"How can a road be carnivorous?" Caldus asked.

"Poorly, if travelers are alert."

Mara leaned over the map. It looked less like geography than an argument someone had lost to a snake. Lines bent through reed marks, sink symbols, little teeth, and a skull with an apologetic hat.

"How long?"

Narka looked at Kesh.

Kesh looked at the ceiling, which was to say Auntie Grum's sleeping flank. "If the water behaves, six hours. If the water negotiates, ten. If Old Jaw remembers it hates me, we discuss my legacy."

"Your legacy owes me rent," Tavi said.

"Everyone is very focused on my debts today."

Mara touched Pell's token. "Can we catch the wagon?"

Kesh's jokes drained away again. "Maybe. If your brother is still in a wagon. If they do not switch roads. If the physician who hired me does not know about Old Jaw."

"Does he?"

"He knew enough to find me."

That answer sat heavily over the workbench.

Pell stood beside the stall, watching the map with clouded concentration. His finger rose, trembled, and tapped a point east of the marked road.

Tavi frowned. "That is not Old Jaw."

Pell tapped again.

Narka's expression sharpened. "That is the drowned tollhouse."

"Bad?" Mara asked.

"Everything drowned is bad by temperament."

Pell forced air through his throat. "Switch."

Kesh cursed.

"What?" Mara demanded.

"He thinks they will switch wagons there."

Mara looked at the dead miner, at the token on her neck, at the cinder cage humming on the bench. Pell had died, been named, and still he was trying to help her find Joryn. She did not have language large enough for the debt.

"Then we go there."

Caldus was already studying the map as if obedience to a bad idea could be improved by posture. "We need supplies, quiet boots, dry lamp cord, and something to hide the dead."

"Rude," Kesh said.

"Accurate," Pell rasped.

The goblin market moved around them. Not chaotically, not once Narka began issuing orders. A woman with arm tattoos brought reed cloaks that smelled like mud. A boy delivered black bread, dried eel, and a jar of paste that Tavi claimed would keep leeches off unless the leeches were unusually motivated. Someone gave Pell a scarf to cover his mouth. Someone else brought a child's slate and chalk so Tollen could write when his voice failed.

No one called it kindness. Perhaps that would have made it too expensive.

Before they left, Narka took Mara aside beneath a string of muffled bells.

"You carry debt now," the old goblin said.

"I know."

"No. You carry the kind people will try to turn into a crown. A debt can be clean. A crown never is. Remember the difference."

Mara looked back at the company forming around the workbench: Caldus with his scraped shield, Kesh arguing with Tavi, Pell standing too still, the cage glowing blue. She did not feel like anyone who could wear a crown. She felt like a girl who had slept badly and wanted her brother.

"I just want Joryn back."

Narka's face gentled, which did not make it softer. "Most wars begin with just."

Auntie Grum breathed beneath them. The market rose and fell. The Old Jaw road waited somewhere in the reeds with teeth, secrets, and perhaps the last trail to a black mercy wagon.

Mara took the cinder cage from Tavi and followed Kesh down the rope ladder, leaving the market under the sleeping beast quieter than it had been when she entered.""",
    108: r"""The departure took longer than urgency wanted.

Urgency, Mara was learning, had no respect for straps, food, maps, wounds, or the fact that dead people could not simply be wrapped in blankets and expected to pass as sleepy cousins. Narka solved the last problem with a trader's practicality. She sent for reed masks painted with festival teeth, long oilskin coats, and three baskets of marsh eels whose smell could have hidden an army of corpses.

"You are making them into merchants?" Caldus asked.

"I am making everyone nearby wish to look elsewhere," Narka said. "Different craft."

Pell accepted the mask without complaint. Essa looked at hers for a long moment, then touched the painted mouth where her own had been stitched. Mara expected refusal. Instead the dead woman put it on and stood straighter, as if a false face were easier to bear than the damage beneath. Tollen took the slate and wrote with slow, careful strokes: Not hiding. Traveling.

Mara read it and nodded. "Traveling."

The word changed something. Not much. Enough.

Tavi adjusted the brass cage until its hum dropped from three notes to one. She wrapped leather around the handle and thrust it at Mara.

"Do not sleep with this against your heart. Do not bleed on it again. Do not let anyone sing formal hymncraft within arm's reach. Do not put it near dragon-bone, ghost salt, oath-stone, old bells, new bells, intelligent fungus, experimental batteries, or Kesh."

Kesh put a hand to his chest. "I object to being listed after fungus."

"Improve yourself."

"In this economy?"

Mara took the cage. "What happens if I ignore the list?"

Tavi stared at her. "Why do people always ask that as if the exciting answer is the useful one?"

"Because useful answers are usually bad."

"Fine. It may wake nearby memory structures, attract corpse commands, cause local weather to become symbolic, erase your least defended memory, or make something ancient decide you are conversational."

"That last one already happened."

Tavi's expression sharpened. "The cinder spoke?"

Caldus said, "We are leaving."

"Wait," Tavi said.

"No."

"Absolutely wait. Spoken response from a raw cinder fragment means either she is a resonance prodigy, which is historically fatal, or the fragment is not a fragment, which is geographically rude, or something under Kell Ashgate was already awake enough to identify bloodline, name-shape, or emotional pressure."

Mara heard only one word clearly. "Bloodline?"

Tavi winced. "Not royalty. Do not make that face. Blood remembers exposure, injury, work, illness, proximity. Families who labor near cinders for generations become... legible."

"Legible to what?"

Tavi looked at the cage.

The shard pulsed once.

Narka's cane struck the planks. "Scholar later. Road now."

For that, Mara loved her a little.

At the edge of the market, Kesh stopped beneath a line of hanging charms made from fishbone and red thread. He selected one, bit the thread in half, and tied it around Mara's wrist above the bandage.

"What is it?"

"A promise to the road that you will not step where it has clearly expressed objections."

"How will I know?"

"When I yell."

"That is less mystical than I hoped."

"Mysticism costs extra."

Auntie Grum slept again, if the slow rise and fall beneath their feet could be trusted. As Mara climbed down the final ladder, she looked back at the market: lamps low, watchers everywhere, Narka in her red coat standing like a nail driven into the world. The place had taken her in not because she was chosen, blessed, or good, but because Pell's debt had weight and the crown's crime threatened the road.

That was sturdier than destiny.

At the bottom, black water lapped over Mara's boots. Old Jaw opened ahead as a gap in the reeds. Warm breath came from it, carrying the stink of mud, old teeth, and a current that ran the wrong way.

Kesh lifted one finger. "Rules. Stay behind me. If something asks for your name, lie badly. If water laughs, step back. If you see lanterns under the surface, do not follow them unless you enjoy becoming folklore. If I say run, do not ask whether I mean now."

"Do you?"

He listened to the dark gap.

From somewhere inside Old Jaw came a small metallic sound. A wagon chain, perhaps. Or a bell. Or a thing pretending to be one.

Kesh's ears lowered. "Now would not be ridiculous."

Mara tightened her grip on the cinder cage, thought of Joryn in a black wagon, and stepped into the road that had teeth.""",
    208: r"""The first step into Old Jaw sank to Mara's ankle.

The second found stone.

The third found something that might have been bone and might have been wood, and she decided not to ask the road for clarification. Behind her, Caldus muttered instructions to the disguised dead with the care of a commander trying not to sound like one. Pell's eel basket knocked softly against his knee. Tavi had come as far as the waterline despite Narka telling her not to, which apparently meant Tavi had heard and filed the instruction under charming local weather.

"Vent-girl," Tavi called.

Mara looked back.

The gnome tossed her a small brass disk on a cord. Mara caught it against her chest.

"If the cage changes pitch twice, stop. Three times, run. If it goes silent, put the disk on the cage and get everyone away from you."

"What happens then?"

"I become very impressed from a distance."

"Tavi."

"It vents pressure. Probably."

Kesh groaned. "I preferred her before she gave us explosives."

"It is not an explosive," Tavi said. "It is an apology to physics in advance."

Mara tied the disk beside Pell's token. The two bits of metal touched once with a small, ordinary click. Debt and danger, hanging together at her throat. That felt about right.

Then the reeds closed behind them, and the market became lantern-glow, then rumor, then nothing.

Old Jaw swallowed sound differently than the culvert had. The culvert had echoed. This place absorbed. Boots entered water and made no splash. Breath left mouths and seemed to go nowhere. Even the dead grew quieter. Mara wondered what kind of road had learned to keep secrets so completely, and whether it had learned from kindness or hunger.

Ahead, Kesh raised one hand.

Everyone stopped.

In the dark water before them, a lantern bloomed under the surface. Then another. Then a third, small and golden and impossible, drifting against the current in a line that looked almost like an invitation.

Mara remembered Kesh's rule.

"Do not follow lanterns under the surface," she whispered.

The lanterns stopped.

One by one, they turned toward her.""",
    308: r"""The cinder cage hummed once.

Not danger, Tavi had said. Not yet. But the note moved through Mara's injured hand and found the place where the mountain had spoken her name. The underwater lights shivered as if pleased to be noticed.

"Kesh," Caldus whispered.

"I see them."

"Are they alive?"

"That is a rude question in a swamp."

Mara wanted to step back. The road behind her had already vanished under black water. Old Jaw did not offer retreat as a direction. It offered only forward, and perhaps down.

Pell's token tapped her chest.

Joryn was somewhere ahead, if ahead meant anything in a road that ate maps.

Mara lifted the cage, and the lights under the water gathered like listening eyes.""",
    408: r"""Somewhere far ahead, a chain clinked once, and Mara forgot every argument against hurrying. Joryn had made that sound once, dragging ore carts home through rain. He was near. Too near. Now.""",
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
            replacement = replacement + "\n\n" + EXPANSIONS[chapter_no].strip()
        extra_key = 100 + chapter_no
        if extra_key in EXPANSIONS:
            replacement = replacement + "\n\n" + EXPANSIONS[extra_key].strip()
        second_extra_key = 200 + chapter_no
        if second_extra_key in EXPANSIONS:
            replacement = replacement + "\n\n" + EXPANSIONS[second_extra_key].strip()
        third_extra_key = 300 + chapter_no
        if third_extra_key in EXPANSIONS:
            replacement = replacement + "\n\n" + EXPANSIONS[third_extra_key].strip()
        fourth_extra_key = 400 + chapter_no
        if fourth_extra_key in EXPANSIONS:
            replacement = replacement + "\n\n" + EXPANSIONS[fourth_extra_key].strip()
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
        'current_form: "full-length draft zero with Book One chapters 1-8 revised in pass 01; continuing literary revision needed"',
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
    print(f"Book One Part II opening revised. Word count: {total}")


if __name__ == "__main__":
    main()
