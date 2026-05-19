#!/usr/bin/env python3
"""Revision pass 01j for Book Three chapters 9-16.

Replaces the Storm Isles and early War of Every Road scaffold with bespoke
chapters for the dragon court, witnessed memory, Kesh's public accounting,
Mara's refusal of dragon authority, the answerable war compact, the avalanche
battle, the goblin road compact, and Tavi's engineering liability code.
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
    9: r"""## Chapter 9: The First Living Dragon

The first living dragon Mara saw did not descend from the clouds like judgment.

It climbed out of the sea.

The Storm Isles hung above the eastern horizon in towers of black stone and revolving weather, but the water below them was no ordinary water. It rose in slow spirals toward the floating islands, drawn upward by heat, moon-pull, and old dragon craft. Waves lifted from the surface in columns the color of hammered steel. Lightning crawled up them instead of down. Between the columns, the narrow path Brakka had opened along the cliff ended at a platform of salt-white rock with no bridge beyond it.

Kesh looked over the edge and immediately stepped back. "No."

Tavi, who had been sketching the impossible tide with shining eyes, said, "That was not a measurement."

"It was a conclusion."

"We need the measurements before the conclusion."

"Measure my conclusion from a distance."

Mara stood at the platform's lip with spray cold on her face. Below, the eastern sea turned like an eye. The path had held through the night, slick with stormlight, narrow enough that Caldus walked behind her with one hand never far from her pack strap. Saelith's corrected hymn mark had glowed whenever thunder spoke. Ilyr and Maelin had traded shadow signs over every blind corner. Auralian had looked progressively more offended by weather that refused all liturgy. Brakka had carried Elder Morn's bridge nail wrapped in oilcloth at her belt. Kesh had not stopped watching the scorched road token he took from Rikka's mouth.

Now there was no road.

"There is always a road," Kesh said, because pride sometimes outran terror. "Unfortunately, this one appears to be vertical, wet, and philosophically hostile."

The sea opened.

A head rose from the spiral tide, larger than Harrowmere's northern gate, plated in dark bronze scales veined with blue fire. Horns swept back like storm-bent pines. Water streamed from a mane of black spines. One golden eye opened, and every cinder scar in Mara's palms went hot.

The dragon looked at her.

The world became very old.

Mara had heard dragon memory since the mine vents of Kell Ashgate. She had tasted it in cinders, bells, engines, moon-chambers, old roads, and the death-grief of Vorrakai. All of that had been echo, organ, ash, remnant, wound. This was breath. This was muscle under scale. This was a person whose first language had been thunder and whose childhood might have watched mountains still deciding where to stand.

Everyone around Mara bent.

Not kneeling. Not quite. The body did things before politics explained them. Caldus lowered his head like a knight before a sovereign he did not serve. Saelith's breath caught on the edge of hymn. Auralian folded in half with the reflex of a people trained to recognize the sky as witness. Maelin's shoulders tightened. Ilyr went still in the way a blade went still before striking. Tavi whispered a number under her breath and then gave up because no number wanted the job.

Mara's knees tried to follow.

She locked them.

The dragon's eye narrowed.

Small ash-witness, said the dragon, not in sound but in pressure through bone and salt air. Why do you remain upright?

Mara swallowed seawater she had not meant to breathe. "Because if I fall down every time power gets large, I will spend my life on the floor."

Kesh made a small strangled noise that might have been admiration or preparation for death.

The dragon's nostrils flared. Steam rolled across the platform and turned Tavi's hair into a damp disaster.

You name insolence as balance.

"Often."

The dragon lifted higher from the sea. Wings unfolded beneath the water first, then broke the surface in a thunder of spray, each membrane patterned with lines of lightning. When they spread, the sun vanished. The platform darkened under scale-shadow, and Mara understood why ancient peoples had mistaken dragons for weather. Weather had the decency to be impersonal. This had opinions.

I am Eshkarun of the First Thermals, keeper of the eastern ascent, witness of seven covenants and breaker of three.

"Mara Venn," she said. "Traveling witness, subject to correction."

Eshkarun's eye brightened with amusement. A title built to rot before it roots. Sensible, for a short-lived flame.

"It was written by a child."

Then perhaps your children understand authority better than your kings.

The dragon's gaze moved over the company. Each person stiffened when it touched them. Caldus's old wound pulsed under his armor. Saelith's hymn mark bled light. Ilyr's shadow blade whispered against its sheath. Tavi's tools clicked in their rolls, recognizing craft beyond craft. Kesh's scorched token smoked.

Eshkarun paused on Kesh.

Debt-bearer.

Kesh's smile arrived late and armed. "Many people greet me that way, though usually while presenting an invoice."

The dragon said nothing more to him.

That was worse.

Brakka stepped forward. The platform trembled under her weight and the dragon's regard. "We seek the Court of Long Memory."

The court has already smelled you.

"That is not an answer."

It is the first mercy. Answers bind.

Brakka considered this, then grunted. "Troll law agrees halfway."

Eshkarun opened his mouth. Teeth, each the length of Mara's forearm, shone like wet ivory. Between them burned blue-white heat.

The ascent requires proof that you understand falling.

Kesh pointed down without looking. "I understand it."

The dragon's laughter rolled into the sea. The spiral tide rose faster. Wind tore at cloaks. The salt platform cracked along old seams, revealing glassy channels beneath. Storm heat surged upward and formed a road of vapor from the platform to the first floating isle.

No rail. No stone. Only rising wind.

Tavi crouched and thrust a hand into the thermal, then snatched it back. "It is a pressure column with lateral memory! Also it would like us dead if we step wrong."

"Can it hold us?" Caldus asked.

"That depends on whether holding includes temporary screaming."

Eshkarun lowered his head until Mara could see scars along his muzzle, pale grooves cut by something too large to imagine. He was not only majesty. He was history that had survived history badly.

You woke the dead organs and did not command them. You woke the dragon-moon and did not claim it. You broke a command engine and brought no replacement crown. The court is curious whether this is wisdom or poverty of imagination.

"It can be both," Mara said.

The dragon looked amused again.

Beyond him, the Storm Isles turned in their towers of cloud. Living shapes moved between them, vast and slow, some winged, some coiling through water lifted into air, some perched on black crags with their eyes reflecting storms older than Vael Taryn's nations.

Mara felt awe then. Not obedience. Awe. The difference mattered. Awe widened a person. Obedience narrowed her until she fit someone else's hand.

She stepped onto the wind road.

The thermal caught her boots.

For one breath, it held.

Then it dropped.

Mara fell five feet and slammed into rising air hard enough to drive a cry from her. Caldus lunged after her, but Brakka caught his belt. Saelith sang one fractured note. Tavi shouted instructions that were almost certainly useful to someone with better lungs. Kesh, pale beneath green-brown skin, took three running steps and leaped onto the thermal beside Mara because friendship had apparently ruined his survival instincts.

"Invoice," he gasped as wind hurled him upward.

Mara laughed despite terror.

One by one, the others followed: Caldus with soldier balance, Saelith with prayer turned into breath, Ilyr and Maelin stepping through shadow pockets that the wind tried to swallow, Auralian muttering old star names, Brakka trusting the road only after striking it with the bridge nail, Tavi whooped once and pretended it was a scream when no one believed her. The thermal lifted them in rough spirals toward the first sky-isle.

Halfway up, sky eels flickered in the cloud wall.

Eshkarun moved faster than thought. The dragon rose beside the thermal, wings shaping wind, one claw cutting a path through lightning. He did not shield them gently. He redirected danger with the indifference of a mountain deciding an avalanche should go elsewhere. A sky eel struck his shoulder and shattered into blue rain. He did not flinch.

Long memory has learned arrogance, Mara thought.

Then Eshkarun's wing dipped, scar tissue straining, and for one instant she saw pain in the great body. The old wound along his muzzle was not decorative. Neither were the scars under his wing joints. Dragons had suffered and made proportion out of scale. That did not make them right. It made them people large enough to be dangerous when wrong.

They landed on the first sky-isle in a field of black grass that rang like glass underfoot.

Above them, Eshkarun circled once. His shadow covered the sun, withdrew, covered it again.

Stand upright if you must, small title, he said. The court will decide whether your spine is courage, vanity, or useful fracture.

Mara wiped salt and blood from her mouth.

"Tell the court I decide those in mixed witness."

Eshkarun's laughter shook rain from the air.

The first living dragon turned toward the higher storms, and the road behind them vanished.""",
    10: r"""## Chapter 10: Evidence Made of Memory

The Court of Long Memory held session inside the hollow of a floating mountain.

Not a cavern. A hollow. The difference mattered because the mountain still seemed alive around them, black stone ribs curving toward an open roof where storms revolved in slow, deliberate circles. Rain fell upward along the walls. Rivers entered from nowhere, crossed the air in shining ribbons, and vanished into cracks full of stars. The floor was a vast disk of translucent scale, each plate larger than a house and each plate holding a memory beneath it: cities burning, children laughing, dragons coiled around first fires, mortals raising their first walls, mortals raising their first cages, dragons breaking cages and calling it justice.

Mara tried not to look down.

This was difficult because the floor kept accusing her of having feet.

Seven dragons occupied the tiers above the scale disk. Eshkarun crouched nearest the storm gate, bronze and blue, still wet from the ascent. A white dragon with feathered spines lay along a ledge of ice that did not melt. A red-gold dragon rested with her head on folded claws, eyes half-lidded but never sleepy. Two smaller green dragons coiled together around a tree growing upside down from the ceiling. A black dragon shaped like midnight over water watched from a pool suspended in the air. The oldest was not the largest. She was gray, narrow, scarred to the bone in places, with one horn broken and moss growing in the crack.

When she breathed, the floor memories trembled.

Mortal witnesses, said the gray dragon. Present proof.

Auralian bowed until his forehead nearly touched scale. "Honored court, Vael Taryn suffers a crisis of unburied memory. We request judgment, aid, and correction of the old covenant."

The red-gold dragon opened one eye. You request much in a court you did not build.

Mara heard Saelith inhale, preparing a formal answer.

Mara spoke first. "People usually build courts because someone else was taking too much."

The white dragon lifted her head. Snow slid from her neck and vanished before touching the floor. This one has poor survival music.

"It has been mentioned," Caldus said.

The gray dragon's gaze moved to him. Knight without crown. Your obedience broke before your pride did. Interesting sequence.

Caldus's jaw tightened.

Mara stepped closer to him before she understood why. The court did not ask questions like people asked questions. It opened the body and read the injury aloud. Dragons accepted witnessed memory because words were easy to arrange. Memory, they believed, resisted lies.

They were partly right.

That was what made them dangerous.

The gray dragon lifted one claw. A basin of blue fire rose from the floor.

Memory given under fear is often poison, she said. Memory hidden during catastrophe is often worse. Choose.

"Choose what?" Tavi asked.

What truth each of you will carry into evidence.

No one moved.

Then Caldus stepped forward.

He placed his hand over the blue flame. It did not burn him, not visibly. His face changed anyway.

The scale floor filled with Harrowmere rain, a younger Caldus in clean armor, a line of villagers on a bridge, an order stamped with the royal seal: hold the bridge for noble evacuation, cut it before fever wagons arrive. Mara had heard pieces of the story. She had never seen Caldus's hand on the rope knife. She had never seen him look back at the wagons, at the poor sick reaching for a crossing he had been ordered to deny. She had never seen him cut the wrong rope first.

Not the bridge rope.

The royal banner rope.

In the memory, the banner fell into mud. Soldiers shouted. Fever wagons crossed. Noble riders cursed. Caldus was stripped of rank before sunset.

The gray dragon watched without blinking. One disobedience. Many still died.

"Yes," Caldus said.

You offer failure as virtue?

"No. I offer failure as evidence that obedience did not save them either."

The basin dimmed.

Saelith went next. Her memory rose in white-gold flame: a young light elf singing in a perfect hall, praised for vanishing inside harmony. Then Orrowen's chamber, Serathiel's mercy turning toward cleansing, Saelith placing one ugly note where beauty expected surrender. The dragons saw her shame at disobedience. They saw her relief. They saw the people under Lumenorath's polished law whom she had not noticed because beauty had trained her eyes upward.

The white dragon said, You broke a holy instrument and call the sound improved.

Saelith's lips trembled. "No. I call it answerable."

Ilyr's memory cut the chamber cold. Khar Veyl sealed records. His own younger hand releasing half a truth because the whole would have damned people he loved. Exile. Pride made noble by timing. Maelin stood rigid while the memory showed the hidden half: names omitted, victims delayed, the comfort of being right without being complete.

The black dragon in the suspended pool spoke. Shadow folk understand preservation.

Ilyr bowed slightly. "We understand embalming too. It is not governance."

Brakka gave a bridge memory: her clan declaring one of her vows invalid after it became inconvenient, the way sacred law changed shape in powerful mouths. Tavi gave the command engine, not its destruction, but the second before refusal, when she had believed she could make slavery safer if the interface improved. Auralian gave the border shrine, the old hymn trying to reclaim Saelith, and his own desire to let it because chaos frightened him more than injustice.

Each memory entered the floor.

Each memory wounded someone who did not deserve the wound.

That was the cruelty of proof. Caldus had to watch fever wagons again. Saelith had to watch herself obey beautifully. Ilyr had to let Maelin see the pride he had hidden behind sacrifice. Tavi had to stand while gnome eyes in the court delegation shifted away from her. Brakka had to hear her old clan law in the mouth of stone. Auralian had to discover he could still want obedience if it promised enough peace.

Kesh did not step forward.

The court waited.

He smiled. It was one of his best smiles, narrow and bright and built to be admired from a safe distance. "I am willing to provide receipts, route maps, and three sworn statements of moderate usefulness."

The gray dragon lowered her head.

The floor under Kesh brightened with coin-shaped sparks.

No.

Kesh's smile stayed. His hands did not.

Mara saw the tremor.

"Kesh," she said.

"I heard the court. It has a wonderfully rude voice."

Memory not offered may still be weighed when debt enters judgment.

Brakka's eyes narrowed. "That is not consent."

It is consequence.

"Those are not the same stone," Brakka said.

For the first time, the dragons murmured among themselves. The sound moved through the hollow mountain like distant tectonics.

Mara stepped onto the center of the scale disk. Her burned palms ached. "If you take memory because you are large enough, you prove the old covenant should break."

The red-gold dragon's lips peeled back from her teeth. Mortals hid dragon organs in engines and call us large thieves.

"Yes," Mara said.

The court stilled.

Mara's own memory rose before she chose it.

Not stolen. Answering. Kell Ashgate's pay yard under soot. Joryn's hands bleeding. Mordane's ledgers making dead labor clean. Orrowen's court trying to keep Arveth useful. Thom Arlet in the cabbage field. Nera Bell with stitches cut from her mouth. Pell asking not to take his mother's choice. Selli writing "traveling witness, subject to correction" in pencil.

The floor took those memories and did not know what size to make them.

To dragons, a cabbage field was small. To Lora Arlet, it had been the whole world. To kings, a pay yard was industry. To Mara, it had been where usefulness first learned her name. The memories flickered, not weakly, but in many measures at once.

Eshkarun leaned closer.

You ask us to judge proportion by those crushed beneath it.

"I ask you to admit you cannot judge them without being answered by them."

The gray dragon's broken horn glowed.

Then the court will hear the debt-bearer.

Kesh's smile finally failed.

The scale beneath his feet opened like a wound of light.""",
    11: r"""## Chapter 11: Kesh's Visible Betrayal

Kesh's hidden road appeared in the dragon floor as a line of red dust.

It began beautifully, which made the betrayal harder to watch. A younger Kesh ran along a Gloamfen causeway under lantern moss, laughing with a girl whose braids were tied with copper wire. Rikka of Orrin branch, Mara understood before anyone spoke. Alive. Quick-handed. Singing badly on purpose because the children in the caravan laughed when she missed notes with conviction. Painted wheels rolled behind them. Goblin aunties argued over spice. A child slept under a cart with both hands around a wooden horse. Rain tapped tarps in gentle rhythm.

Then came the flood season.

Then came hunger.

Then came a human toll captain with clean gloves, a sealed offer, and soldiers hidden badly enough that every goblin saw them and no one said so because seeing did not solve hunger.

The memory showed Kesh at nineteen, thinner, sharper, smiling as if a smile could be a roof. His caravan had three sick children, two broken axles, and no coin for the high causeway. The captain offered safe passage for Kesh's branch if he marked an alternate route used by smugglers from the Orrin wagons. Not a death sentence, the captain promised. Only inspection. Only seizure of untaxed goods. Only a delay.

Only was a word powerful people used when someone else paid the rest.

Kesh took the stylus.

Mara did not look away. Neither did anyone else, because the dragons had made privacy impossible and called it proof.

The red dust line split. Kesh's caravan crossed the high causeway. Rikka's caravan turned toward the reed road. The toll captain's soldiers followed. Then the memory changed to night, torchlight, shouting, wagons mired axle-deep, tax seals slapped on food sacks, a soldier striking Rikka's uncle with a spear butt, children crying while rain rose around their knees. Not massacre. That would have been easier to hate cleanly. It was theft made legal, delay made deadly, survival bought with someone else's winter.

Rikka found Kesh three months later.

The memory showed them under a broken bridge. She threw seven silver at his feet.

"Your share," she said.

Kesh did not pick it up.

"I was nineteen."

"So was I."

"My little cousins were sick."

"Mine learned hunger from your mercy."

The younger Kesh said nothing.

Rikka spat into the mud. "Keep the road, then. May it always know your name."

The memory ended with Kesh alone under the bridge, seven silver shining between his boots.

In the court, the coin-shaped sparks fell around him.

No one spoke.

Kesh looked smaller than Mara had ever seen him. Not physically. Goblins were good at refusing the measurements other peoples found convenient. He looked small in the way a person did when every joke had been taken down and the wall behind it showed rot.

The red-gold dragon lifted her head. This is the mortar of mortal law. Hunger. Bargain. Harm renamed necessity. You ask to govern the woken dead while selling roads among the living.

Kesh bowed.

Not theatrically.

"Yes," he said.

Mara felt the word hit harder than any defense.

Kesh turned to her first. That mattered. The court wanted spectacle. He chose witness.

"I told you I sold information once to save my caravan," he said. "I did not tell you the road had a name. I did not tell you Rikka's branch paid for my branch to live. I did not tell you because I liked being the useful thief with tragic footnotes better than being a man whose survival had a bill."

"Why now?" Ilyr asked quietly. Not accusation. A historian's knife.

Kesh looked at the red dust under his feet. "Because she died in the tunnel with my kind of token under her tongue. Because the road kept the account even when I made myself very busy. Because Mara keeps doing this unbearable thing where she asks people to be more than their best excuse."

Mara's anger arrived late. When it came, it came hot and clean enough to frighten her. She remembered Kesh beside her in Ashgate, in Lumenorath, in Khar Veyl, in Orrowen, on the storm road. She remembered him leaping onto the thermal after her, calling invoice while wind tried to kill them both. She remembered trust built in mud and danger.

She also saw the children in the reed road rain.

"I am angry," she said.

Kesh nodded. "Good. I was worried the dragons had stolen everyone's sense."

"Do not make this easier."

"I do not know how."

That was almost true. Almost. He knew how to make anything easier for a minute. He had chosen not to.

Brakka stepped beside him. "Debt named."

The gray dragon watched her. Naming is not payment.

"No," Brakka said. "But unnamed debt charges interest in blood."

Tavi wiped both eyes with the heel of her hand and glared at everyone who might notice. "Can we repair this without letting the giant prosecution lizards win the philosophy?"

Eshkarun bared teeth in something too dangerous to be amusement.

Saelith moved to Kesh's other side. "What payment does the road require?"

Kesh swallowed. "Not forgiveness. Not from people absent and dead. Rikka is beyond my bargaining. Her branch has survivors. I know some names. I avoided knowing others."

"Then stop avoiding," Mara said.

He flinched.

She did not apologize.

Kesh reached into his coat and removed the scorched token from the tunnel. Then he removed another token, older, polished smooth from years of being touched when no one saw. Seven tiny scratches marked one side.

"I kept the silver," he said.

The court murmured.

"Not to spend. Not because that makes it noble. I kept it because throwing it away would have let me pretend I was done." He placed both tokens on the scale floor. "I enter debt to the Orrin branch, Rikka named first among my witnesses. I enter the red road as unsellable by one caravan alone. I enter my own name as unsafe for route command without mixed witness."

The tokens sank into the floor.

For a moment, nothing happened.

Then the red dust road spread across the scale disk. It crossed goblin marshes, human toll bridges, troll foundations, dead military roads, refugee paths, ash-lanes, river fords, sky-isle thermals, and old plague tracks. Everywhere a road had been sold by someone with no right to sell it alone, a spark lit.

There were thousands.

The dragons went quiet.

Mara looked up at them. "There is your proportion."

The black dragon in the suspended pool narrowed his eyes. A wound does not become law because many share it.

"No," Mara said. "But law that cannot see the shared wound becomes a weapon that thinks it is clean."

Kesh looked at her then. Not forgiven. Not restored. Seen under worse light and still not thrown away. That was more difficult than mercy.

"Mara," he said.

"Do not thank me yet."

"I was going to ask whether this means I am no longer allowed near maps."

Despite herself, she laughed once. It hurt.

"It means you are never alone with a map again."

"Cruel but fair."

The gray dragon lowered her broken horn until its shadow crossed Kesh's road. Debt entered. Harm witnessed. Correction pending.

"Pending," Kesh repeated. "That word has teeth."

"Good," Brakka said.

The court floor cooled under him.

Mara felt the company re-form around the wound, differently shaped. Trust had not snapped cleanly and returned. It had become something with scar tissue, rules, and a place where anger could stand without being mistaken for abandonment.

Above them, the dragons watched as if this was the strangest evidence yet.

Perhaps it was.

Perhaps creatures who lived for ages had mistaken endurance for repair.""",
    12: r"""## Chapter 12: Judgment of Scales

After Kesh's road, the dragons offered Mara a crown without calling it one.

They waited until the court floor had cooled and the coin-sparks faded. They waited until Kesh had stepped back among the company with his old tokens gone and his hands empty. They waited until Mara's anger settled into something she could carry without spilling it on the wrong person. Dragons, she was learning, understood timing the way hunters understood wind.

The gray dragon raised her broken horn.

Beneath the scale floor, every memory dimmed except the cinders.

They appeared not as stones, engines, lamps, or organs, but as a buried constellation under Vael Taryn: thousands of red-gold points scattered through mines, roads, bridges, archives, shrines, forges, palace walls, plague pits, dragon graves, and the sleeping moon-lock body of Othrava beneath Orrowen. Each point answered faintly to Mara's breath.

Tavi whispered, "That is an irresponsible amount of infrastructure."

The white dragon looked down at her. Accurate.

Mara's palm burned.

Eshkarun spoke, and this time his voice used sound. "The old covenant failed because dragons judged from height and mortals built cages from fear. Vorrakai saw the failure and chose stillness. We reject his ending."

The red-gold dragon's eyes flared. "But rejection is not repair."

The gray dragon extended one claw. The buried cinder constellation tightened into lines, all of them running toward Mara.

"No," Caldus said.

The dragons ignored him because they were dragons and had spent too many centuries mistaking size for relevance.

The gray dragon said, Small ash-witness, you stand where no dragon may stand and no king should. You hear the dead organs. You refuse command, which makes command safer in your hand.

Mara felt the trap close around the compliment.

Saelith heard it too. "Do not praise her into a chain."

The red-gold dragon bared teeth. Would you prefer we choose a tyrant?

"I would prefer you stop choosing for everyone."

The court stirred. Wind moved upward through the hollow mountain, carrying the smell of lightning and old blood.

The gray dragon did not look away from Mara. Become instrument of judgment. Not queen. Not martyr. Instrument. Wield cinders to still violent dead, expose hidden commands, break engines of enslavement, and hold mortal rulers answerable until the Dead Capital can be entered. We will bind you against selfish use. We will witness you.

Mara almost laughed.

Not because it was absurd. Because it was beautiful.

That was the horror. The offer would save lives. She saw dead cavalry released from obsolete orders before they harmed towns. She saw corpse-hunters stripped of hidden ledgers. She saw kings unable to turn cinder relays back into weapons without her hearing it. She saw the Pale Remnant's hymns failing wherever they tried to bind the risen. She saw a world in which every frightened person could point toward Mara and say, there, the answer is walking; let her carry it.

Useful. Holy. Safe.

She wanted it.

The wanting was small and exhausted and human. She wanted one lever large enough to move suffering without endless meetings, arguments, ledgers, vows, apologies, and people dying while the right thing assembled itself badly. She wanted to be done negotiating with men like Regent Rook, done watching Saelith bleed for a note, done asking Kesh to confess in public because privacy had become expensive, done measuring every act of power for the shape of a cage.

Vorrakai's distant grief moved under the mountain.

See, it seemed to say. Choice always returns to burden. Let burden end.

Mara closed her burned hand until pain steadied her.

"If I become your instrument," she said, "who corrects the hand holding me?"

The gray dragon's eyes narrowed. The court.

"Who corrects the court?"

Silence.

There it was. Not malice. Architecture.

Ilyr stepped forward. "Khar Veyl said sealed oversight was answerable because the overseers had records."

Auralian said, "The Pale Bough said beauty corrected law because the holy could hear harmony."

Tavi said, "The gnome guilds said devices were neutral because their diagrams were public to people trained to read diagrams."

Brakka said, "My clan said a broken vow could be edited by those least harmed by the edit."

Caldus said, "Harrowmere said oaths made orders honorable."

Kesh looked at the floor. "Road captains said survival settled accounts."

Saelith took Mara's burned hand. "Serathiel said mercy excused erasure."

Mara looked up at the dragons. "Every cage in this age was built by someone certain they were the responsible one."

The court did not roar. That would have been easier. It listened, and listening by dragons felt like being measured by weather.

Eshkarun spoke first. Then refuse and take less aid. Refuse and more towns burn while mortals argue. Refuse and dead soldiers march another day. Refuse and Vorrakai's Choir grows.

"Yes," Mara said.

The word hurt more than defiance should.

The gray dragon lowered her claw. You accept that cost?

"No. I admit it exists. Acceptance sounds too clean."

The oldest dragon studied her for a long time. Then she dipped her broken horn toward the scale floor. The cinder constellation loosened. Lines to Mara thinned, then vanished.

Judgment withheld.

Mara's knees nearly gave.

Not from relief. From the loss of the beautiful lever.

The white dragon unfurled one wing. We will not give you command. We will give you storm routes, three true names of places where the Dead Capital can be entered, and witness of Vorrakai's first crime.

The mountain darkened.

A memory rose from every scale at once: the first age, not golden, not innocent. Mortals terrified of dragon judgment. Dragons terrified of mortal cages. A battlefield after a war no song remembered correctly. Vorrakai, black and vast and grieving, standing among the dead of both kinds. Not monster. Not yet. A judge who had seen too many choices become slaughter and decided mercy required an ending large enough to hold everyone still.

Mara felt pity.

She hated that too.

The gray dragon let the memory fade. He will call your refusal cruelty. He will not be entirely wrong. That is why his argument survives.

"I know," Mara said.

Eshkarun extended a single bronze scale, shed from the scar under his wing. It fell to the floor with a sound like a shield dropped in a cathedral.

Carry this to the War of Every Road. It will open one storm path when no road remains. Use it once. No more.

Tavi eyed the scale. "Does it explode?"

Only if insulted by amateurs.

"So yes."

For the first time, the gray dragon's mouth curved.

Kesh looked toward the storm gate. "What happens now?"

The court roof opened wider. Far below, through impossible distance, Vael Taryn glowed with war signals: red along the mountain passes, blue from Third Arch, white from Lumenorath, violet from Khar Veyl, green goblin road lamps moving in frantic lines, black Choir fires appearing where no army had yet marched.

The red-gold dragon answered. Now you return to your short-lived arguments and prove they can move faster than doom.

Mara picked up Eshkarun's scale. It was warm and terribly light.

"Then we had better get back before someone makes me general."

Caldus smiled without humor. "Too late."

"Then we had better disappoint them quickly."

The storm gate opened beneath their feet.

They fell toward the war.

# Part III: The War of Every Road""",
    13: r"""## Chapter 13: No Single Army

The first war council after the dragon court met on three wagon doors laid across rain barrels.

That was Mara's fault.

Regent Rook's nephew had offered a command tent with blue banners, guarded entrances, and a raised chair placed where every messenger would have to look up before speaking. Auralian suggested a formal ring of dignities. Vaura's shadow envoys proposed a sealed chamber so the factions could discuss sensitive deployments without rumor. The gnome guild factor wanted a speaking order based on technical relevance. Kesh, still raw from the dragon court, said nothing at all, which worried Mara more than all the banners.

So she asked two refugee carpenters to unhinge wagon doors and set them across barrels in the middle of the road.

Rain fell on everyone equally.

"This is inefficient," said the gnome factor.

Sava Rennet, newly arrived from Third Arch with three clerks, a dead witness named Othel, and no tolerance left for dignity, opened a dry ledger under an oilcloth. "Efficiency has filed a grievance. It will be heard after survival."

The road around them had become a moving city. Goblin wagons painted in clan colors stood beside Harrowmere grain carts, Lumenorath healer sledges, Khar Veyl shadow tents, troll stone crews, gnome forge-wheels, Orrowen record barrows, and dead cavalry who waited in disciplined lines under fever-year banners corrected with strips of refugee cloth. Beyond the wagons, columns of smoke marked towns where the dead had risen under old orders or the Choir had promised stillness to the terrified.

Everyone wanted one army.

That was the problem.

"One army moves faster," Rook's nephew insisted.

"One army obeys one chain," Brakka said.

"Chains can be useful," the nephew replied.

Brakka smiled. "So can hammers."

Vaura's envoy tapped the wet map. "Without central command, contradictory orders will cost lives."

"With central command," Ilyr said, "wrong orders cost more lives faster."

Auralian looked exhausted enough to be honest. "Lumenorath can coordinate hymn-healers, but not under Khar Veyl shadow routing."

Maelin's eyes sharpened. "Khar Veyl can move scouts behind Choir lines, but not if every light-elf patrol sings our location into the weather."

"Our songs no longer compel."

"They still carry."

Tavi slapped a brass marker onto the map. "Meanwhile, cinder pressure is rising under three railbeds, two bridges, and one extremely unwise palace kitchen. If the guilds build release engines without oversight, they will accidentally invent tyranny with better rivets. If they wait for full oversight, the kitchen explodes first."

Kesh finally spoke. "Road clans can move refugees through five routes the crowns do not know."

Every human official looked interested.

Kesh's voice went cold. "And will continue not knowing unless route witness agrees."

Mara watched him. The old Kesh would have made the secrecy charming. This one held it like a wound he was refusing to sell twice.

Caldus stood at the edge of the wagon-door table, arms folded, looking like a man trying not to become exactly what everyone wanted. They trusted him because he knew war. That was fair. They wanted him to command everyone because trust was easier when given to a single uniform. That was dangerous.

"We need battle lines," he said. "But battle lines are not government."

The rain thickened.

Mara touched Eshkarun's bronze scale beneath her coat. One storm path. Use it once. No more. A gift that was not a leash only because she had refused the leash first.

She climbed onto a barrel.

This gave her perhaps ten inches of height and absolutely no dignity. Good.

"No single army," she said.

The council erupted before the sentence finished rippling through rain.

She let them shout. Shouting used air. Air eventually ran out.

"No single army," she repeated when the road quieted. "No single crown. No single court. No single guild. No single witness. The Choir wants one answer because one answer can be captured. Vorrakai wants stillness because stillness cannot argue. We are not building his shape in order to fight him."

"Then what are we building?" Vaura's envoy asked.

"A compact of answerable roads."

Sava's pen began moving faster.

Mara pointed to the map. "Caldus coordinates battle warnings, not civil orders. Brakka and the Seven Arches hold refugee law and bridge disputes. Kesh and the road clans choose routes under mixed route witness and public payment, with no route sold by one caravan alone. Tavi's forge teams build pressure-release engines, but every device carries maker liability, refusal function, and citizen oversight. Saelith and Auralian coordinate healer hymns with dark-elf shadow screens so songs do not become lanterns for enemies. Ilyr, Maelin, Vaura, and Sava manage records: orders, names, redactions, challenges. Dead witnesses may object."

Othel, the dead clerk, raised a translucent hand. "May we object preemptively?"

"Frequently," Mara said.

He looked pleased.

The nephew frowned. "Who resolves conflict?"

"The people affected first," Mara said. "Then mixed witness. Then emergency action with review after. Review is not optional. If someone says no time, they sign their name beside the harm."

The gnome factor stared. "You want minutes during apocalypse."

"Especially then."

Kesh made a faint sound that might have been a laugh returning from a long trip.

The attack came as a horn from the north.

Not a Choir horn. A human alarm. A messenger stumbled into the council circle, snow in his hair though the road lay under rain. "Snow Cedar Pass is closing. Harrowmere infantry, Lumenorath riders, Khar Veyl scouts, and dead cavalry all converged under separate orders. Choir banners in the pass. Avalanche signs. No one can see who commands."

Every face turned to Mara.

There it was. The old hunger. Make one choice, carry one burden, become one answer.

Mara stepped down from the barrel.

"Caldus, battle warning. Not command. Brakka, bridge and evacuation. Kesh, alternate roads. Tavi, pressure readings. Saelith, healers. Ilyr and Maelin, shadow screens. Sava, minutes."

The nephew grabbed her arm. "This is madness. They need a general."

Mara looked at his hand until he removed it.

"They need to hear each other before the mountain falls."

Caldus buckled his sword belt tighter. "And if they do not?"

Mara looked north, where the rain had begun to turn white.

"Then we learn whether our slower freedom can outrun a fast cage."

No one liked that answer.

That was how Mara knew it might be honest.""",
    14: r"""## Chapter 14: The Avalanche Battle

Snow Cedar Pass was blind before they reached it.

The storm came sideways through the cedars in white sheets, thick enough to erase banners, faces, cliffs, and the difference between ally and enemy. Trees cracked under the weight of new ice. The pass road climbed between black rock walls veined with cinder-grit, every vein pulsing under the pressure of thousands of frightened feet. Somewhere ahead, horns called contradictory orders. Somewhere above, the mountain answered in low, shifting booms.

Mara could not see the war.

She could hear it.

Pikes striking shields. Horses screaming. Dead cavalry trumpets. Light-elf hymn bells bright and terrified. Dark-elf shadow whistles. Goblin wheel chimes. Troll stone calls. Gnome pressure gauges shrieking in little brass voices. Choir singers under all of it, humming one note that made panic feel like relief.

Come still, the note promised. Stop choosing. Stop falling. Stop losing each other in snow.

Mara's breath fogged around her. Her burned palm found cinder under the road. The pass wanted a command. Every road did when fear crowded it.

Caldus caught her wrist before she asked the mountain for anything.

"Names first," he said.

The fact that he had to remind her saved them both.

Sava, who had insisted on coming because minutes taken after a massacre were only archaeology, thrust a slate into Mara's free hand. "Signal plan."

"I did not make one."

"Excellent. No time for bad handwriting."

They made one in motion.

Kesh sent goblin runners by sound: three wheel chimes for living evacuation, two for dead orders, one cracked bell for Choir contact. Brakka and Durn's bridge crews hammered stone calls into the cliff walls, teaching the pass where refuge routes lay under snow. Tavi shoved brass pressure stakes into the road and cursed each one by name so she could hear when it answered. Saelith sang healer positions in rough intervals that would have horrified her old tutors and saved lives by being impossible to mistake for the Choir's smooth mercy. Ilyr and Maelin spread shadow screens low to the ground, not to hide armies, but to mark edges where cliffs began.

Caldus moved through the white with a commander's mind and no commander's throne.

"Left line, hold by sound! Do not chase shapes! Dead cavalry, turn your trumpets outward. Lumenorath riders, answer three notes only. Khar Veyl scouts, no silent kills unless named hostile. Harrowmere infantry, if you cannot see a face, use your shield, not your point."

Some listened.

Some did not.

That was battle. Freedom did not make people wise. It gave them room to be responsible and then punished everyone when they refused. Mara hated that. She also knew the alternative had been offered in dragon fire and Vorrakai's grief.

A figure lunged from the snow.

Brakka smashed it aside with her maul, then stopped before the killing blow. The figure was a dead Harrowmere soldier under a Red Fever evacuation order, helm packed with ice, eyes lit by Choir stillness.

"Name!" Brakka roared.

"Gate by noon," the dead man whispered.

Wrong order. Wrong century. Current danger.

Mara pressed her hand to his breastplate. Cinder cold burned under the metal. "Name."

"Oren Vall."

"Oren Vall," she said. "The fever towers fell. The road changed. Hold the living line west."

The dead soldier trembled. The Choir note reached for him.

Saelith's rough hymn cut under it. Ilyr added shadow, not concealing the order but giving it an edge. Oren turned, lifted his shield, and blocked an arrow meant for a light-elf healer.

Then the mountain cracked.

The first avalanche did not roar. It sighed.

Snow slid from the upper cedars in a single white sheet, slow enough to be understood and fast enough to make understanding useless. The pass became motion. Men and horses vanished waist-deep. Wagons slewed sideways. A gnome forge-sled tipped toward the ravine, its pressure engine glowing red. If it fell, the cinder vein below would burst and take the lower refugee road with it.

Tavi ran for it.

"Of course she did," Kesh shouted, and ran after her.

Mara plunged through snow to follow. Caldus got ahead of her because he always got between danger and the person it wanted. His old sword-arm failed halfway across the slope. She saw it happen: the shudder through his shoulder, the brief opening in his guard, the way he looked offended that flesh still insisted on being part of war.

A Choir champion came out of the white.

It had been a troll once, or something close, now plated in frozen cinder and stitched with pale song. Its face was peaceful. That was worse than rage. It raised an axe made of packed bones and brought it down toward Caldus's weakened side.

Mara almost commanded the cinder vein.

Stop.

The word formed in her mouth.

Then Kesh's chime rang once, cracked and urgent: Choir contact.

One chime meant listen.

Mara listened.

Under the champion's stillness, under the cinder plate, under Vorrakai's merciful note, someone was trapped in a body being used as an argument.

"Name!" she shouted.

The champion swung.

Caldus blocked with his shield and went to one knee.

"Name!"

Brakka hit the champion from the side with enough force to crack its cinder plate. "Answer!"

"Harrow," the champion whispered through a mouth full of snow. "No. Hara. Harak of Broken Span. I fell holding bridge west."

Brakka froze for half a heartbeat. "Troll?"

"Oath invalid," the champion whispered. "No more falling."

Vorrakai's mercy thickened.

Mara understood the trap: the Choir did not recruit only cowards. It recruited exhausted protectors. People who had fallen once and could not bear another fall. It offered them stillness and called it fulfilled duty.

"Harak," Brakka said, voice breaking like stone under thaw. "Bridges are not made by never falling. They are made by being repaired."

The champion screamed.

The avalanche struck the lower road.

Eshkarun's bronze scale burned against Mara's chest.

One storm path. Use it once.

Not here, she thought.

The refusal was terrible. The scale could open a path through snow, save the forge-sled, maybe save everyone on the lower road. It would also spend the only dragon aid before the Dead Capital, before whatever impossible road waited there. Mara saw the calculation and hated every part of it.

"Tavi!" she shouted.

"Busy!"

Tavi had reached the forge-sled. Kesh braced her by the belt while she jammed both hands into the engine's undercarriage. "If anyone has a prayer, preferably one with engineering competence, now!"

Saelith sang. Ilyr cast shadow. Brakka held Harak. Caldus pushed upright with blood on his teeth. Dead cavalry trumpets turned outward. Goblin wheel chimes spread the warning down the road. Refugees moved by sound, not sight, following calls they had learned only hours ago at wagon-door tables in the rain.

The compact held.

Not perfectly.

People died.

Mara would remember that whenever anyone called it victory.

Tavi found the release valve and kicked it open with both heels. Steam and cinder pressure blasted sideways into the snowpack. The avalanche split around the forge-sled, roaring past in two white rivers. Kesh vanished under one and came up swearing creatively enough to prove survival. The lower road held by a margin no engineer would have signed.

Harak of Broken Span collapsed when Brakka broke the Choir plate from his chest.

He was still dead. Still dangerous. Still weeping snowmelt.

"No more falling," he whispered.

Brakka knelt beside him. "No. More catching."

When the storm cleared near dusk, Snow Cedar Pass belonged to no single army.

It belonged to the exhausted living digging out the dead, the dead holding lanterns for the living, goblins marking safe snow, gnomes venting pressure stakes, light and dark elves arguing while sharing bandages, trolls carving new refuge notches into rock, and Caldus sitting on a broken shield while Saelith stitched his shoulder with shaking hands.

Mara stood in the trampled snow and listened to the mountain.

The Choir had withdrawn.

Not fled. Withdrawn.

In the cinder veins under the pass, Vorrakai's grief left one sentence like a footprint.

You call this freedom and count the bodies later.

Mara closed her eyes.

"Yes," she said to the empty pass. "And you call stillness mercy because it keeps you from seeing the faces."

No answer came.

The snow kept falling, softer now.

Around her, the compact carried the wounded by sound.""",
    15: r"""## Chapter 15: The Goblin Road Compact

The goblin road city arrived under ash rain with every wheel painted a different color.

It came over the western ridge at sunset: hundreds of wagons, sledges, rope carts, goat-barges dragged on rollers, narrow scout perches, folding kitchens, mobile shrines, and three stages where musicians played too loudly because fear hated rhythm it could not own. Lanterns swung from curved poles. Clan marks flashed in green, yellow, red, black, and stubborn pink. Children ran between wagons with message ribbons tied to their elbows. Old goblins sat on roof benches wrapped in quilts, judging the world and finding it poorly organized.

Kesh stood in the road and watched his people arrive.

He had washed after the avalanche. He had not managed to look clean.

Mara stood beside him with Snow Cedar mud still on her boots. "Are you all right?"

"Certainly. I enjoy being publicly flayed by dragons, surviving mountain collapse, and then attending family negotiations."

"That sounds like no."

"It is a cultural no. More decorative."

The lead wagon stopped before them. Its wheels were painted with a silver spiral Mara recognized from Kesh's old knife. An elder climbed down using a cane made from three kinds of wood and one suspiciously polished bone. Her hair was white, her skin deep green-brown, her ears ringed with route tokens. She looked at Kesh for a long time.

"Debt-bearer," she said.

Kesh bowed. "Auntie Varr."

"Do not auntie me yet."

"Yes, Varr."

"Do not remove respect to dodge affection."

Kesh closed his mouth.

Mara liked Varr immediately and feared for everyone.

The road city folded itself into camp with astonishing speed. Wagons became walls. Walls became alleys. Alleys became markets. Markets became argument. Within an hour, soup boiled, axle shops opened, children inventoried refugee boots, scouts traded weather, and three separate card games had created temporary economies. The living and dead from Snow Cedar Pass watched in dazed gratitude as goblin route speakers assigned them places not by rank, but by need, skill, and likelihood of wandering into traffic.

Then the profiteers arrived.

They were goblins too.

Kesh saw Mara notice and said, "We produce our own villains. Imported ones lack local nuance."

The profiteers came in lacquered wagons with quiet wheels and guards wearing road masks without clan paint. Their leader, a smooth-faced goblin named Serren Pike, carried a contract tube of black cedar and a smile polished by other people's hunger.

"Kavik roads are prepared to serve the crisis," Serren announced in the central market ring. "For appropriate guarantees, exclusive route rights, and military protection, my consortium can move thirty thousand refugees before the Choir closes the western valleys."

The human officials brightened.

So did fear.

Mara saw it move through the crowd. Thirty thousand was a holy number when one's children stood in the path of war. Exclusive route rights sounded ugly until the alternative looked like snow over faces. Serren knew that. He let silence fatten the offer.

Kesh stepped into the ring.

"No," he said.

Serren's smile widened. "Kesh of Kavik. I heard the dragons made a theater of you."

"They lacked your talent for ticket pricing."

Laughter moved through the market, sharp and nervous.

Serren tapped the contract tube. "You gave away your authority when you entered debt against your own road judgment."

"Yes."

That stopped the laughter.

Kesh turned so the crowd could hear him. "Yes. I sold a route once that was not mine alone to sell. Rikka of Orrin branch paid for it. Children paid for it. I entered debt in dragon court. I do not get to decide alone."

Serren recovered quickly. "Then let those without such stain decide. The consortium holds clean contracts."

Varr's cane struck stone.

"Clean contracts are often washed in someone else's water," she said.

The crowd murmured agreement, but agreement was not structure. Mara had learned that too often. Without a better answer, Serren's offer would win because fear could sign faster than justice could assemble.

Kesh removed a folded packet from inside his coat.

Mara knew it by the way he held it. His best contract. The one he had never shown her. The one with enough hidden routes, debt calls, favors, toll exemptions, and private obligations to make him powerful in a world where roads had become survival.

Serren saw it too.

"Careful," the profiteer said. "Sentiment is expensive."

"So is trust."

Kesh unfolded the packet. Pages, tokens, ribbons, and little metal tabs hung from it in a complicated web. Then he held it over a cookfire.

His hand shook once.

He burned it.

Every goblin in the ring went silent.

The flames turned green, blue, and gold as old inks died. Kesh watched without blinking. When the last tab fell into ash, he spoke.

"No road belonging to more than one life may be sold by one hand. No emergency route may be exclusive while refugees stand unnamed. No clan may hide a safe path from mixed witness for profit, and no crown may seize a path because witness made it public. Payment remains required. Charity that starves the guide is theft with soft music. But payment is entered openly, debt challenge allowed, route harm recorded, and every closed road must name who closes it and why."

Tavi whispered, "He wrote policy in grief."

"Dangerous medium," Sava said, already writing.

Serren laughed. "Beautiful. Impossible. While you debate open ledgers, people die."

Mara stepped forward. "Then sign the compact and start moving them."

"I do not answer to you."

"Good," Mara said. "Answer to them."

She pointed to the road city, to refugees, to dead cavalry, to bridge judges, to goblin elders, to children with message ribbons, to Rikka's name newly painted on Kesh's empty contract tube, to Varr watching with wet eyes she would probably deny under oath.

Serren's guards shifted.

Brakka shifted too.

The guards reconsidered posture.

It was Auntie Varr who finished it. She stepped into the ring and spat into the ashes of Kesh's burned contract.

"Orrin debt enters," she said. "Kavik witness enters. I sign."

One by one, clan elders came forward. Not all. Never all. Some held back, calculating future profit. Some argued clauses until Sava threatened to record them as poetry. Some demanded toll protections, fair enough. Some demanded military escort, also fair. The compact formed not as a song but as a market fight where mercy kept receipts.

By midnight, the first routes opened.

Painted wagons rolled under ash rain toward valleys that had no official roads. Goblin scouts led Harrowmere children through smugglers' gullies. Troll crews reinforced rope bridges. Dark-elf shadows hid lantern lines from Choir watchers. Light-elf healers kept pace with route songs that had learned not to command. Dead cavalry guarded the rear. Every route board carried names: guides, refugees, risks, payments, objections.

Kesh stood apart when the first convoy left.

Mara joined him.

"I am still angry," she said.

"Good."

"I also trust you with this."

He swallowed. For once, no joke arrived fast enough to save him.

"That may be unwise."

"It is answerable."

Kesh looked at the ash of his contract, then at the moving wagons. "I liked being impressive."

"You still are."

"No. This is worse." He rubbed both hands over his face. "This is being known."

The road city bells rang route-open.

Across the camp, Serren Pike signed the compact with a hand that promised future trouble.

Mara saw it. Kesh saw it too.

"He will exploit a clause by morning," Kesh said.

"Probably."

"I put in a clause for that."

"Of course you did."

His smile returned, smaller and less armored.

Under ash rain, the goblin roads opened like veins carrying a frightened world away from stillness.""",
    16: r"""## Chapter 16: The Engineer's Liability

The Brassroot emergency forge had been built inside the roots of a tree that had died before gnomes invented regret.

Its trunk rose from a valley of red clay and black stone, wide enough to hold a district, hollowed into workshops, lifts, dormitories, foundries, lecture balconies, and argument pits. Root-cables ran from the dead tree into the earth, pulsing with cinder pressure drawn from nearby railbeds and old forge veins. Steam climbed through brass chimneys. Hammer song rang day and night. Every wall carried diagrams. Half of them had been corrected in angry handwriting by someone shorter than the original drafter.

Tavi inhaled when she saw it.

Then she said, "I hate being home-adjacent."

The guild factors met them at the root gate wearing insulated aprons, polished badges, and expressions of tragic indispensability. Their spokesperson was Master Pell Quen's successor, a neat gnome named Vellit Ock, whose beard was braided around four silver rulers.

"Apprentice Tavira," he said.

"Field Engineer Quen," Tavi replied.

His smile thinned. "Your guild standing remains under review."

"So does your moral standing, but mine has better minutes."

Sava, beside Mara, opened a ledger with predatory delight.

Vellit looked at the road compact delegation: Mara, Caldus with his arm bound after Snow Cedar, Saelith still hoarse from healer hymns, Ilyr and Maelin carrying shadow maps, Kesh with route ink on both hands, Brakka looming in wet travel stone, two goblin elders, a troll lawkeeper, three dead witnesses, and a line of refugees whose towns sat above rising cinder pressure.

"We are prepared to build release engines," Vellit said. "The guilds request indemnity for emergency deployment."

Tavi stared at him. "No."

"You have not heard the terms."

"They begin with indemnity."

"Tools used under catastrophe cannot be judged by peacetime standards."

"Then catastrophe is when standards matter most."

Inside the forge, gnome engineers had already begun assembling the release engines. Mara watched through the open gate as brass frames curved around cinder-safe stone, pressure flues, root valves, cooling bells, and witness panels Tavi had designed in charcoal during the avalanche aftermath. The machines were not command engines. They did not still the dead or route names into obedience. They bled excess cinder pressure from roads and railbeds into harmless heat, warning light, and, in one version Tavi disliked but allowed, bread ovens.

They would save towns from exploding.

They could also be altered.

That was the shadow under every useful thing.

Vellit spread his hands. "We cannot attach personal liability to every maker. Innovation will stop."

"If innovation only moves when harm has nowhere to knock, let it stop and think," Tavi said.

A younger engineer behind Vellit muttered, "Easy to say after destroying the greatest control apparatus of the age."

Tavi turned toward her. "I destroyed a slavery engine."

"You destroyed proof that gnome craft could govern cinder chaos."

"Govern." Tavi laughed once. It was not a happy sound. "There it is, wearing clean gloves."

Mara felt the root-cables pulse. Deep under the forge, cinder pressure surged from the war roads. Every delay mattered. So did every clause. The world had become very good at making ethics feel like a luxury purchased with other people's survival.

"Show us the engines," Mara said.

Vellit hesitated.

Brakka leaned closer. "Refusal enters minutes."

"This way," he said.

The main forge chamber roared with heat. Gnome teams moved on rails, ladders, swing platforms, and little wheeled stools propelled by kicks and ambition. Release engines stood in various states of birth: some skeletal, some glowing, some already humming as cinder pressure entered and left as steam. Tavi's face changed despite herself. Anger did not erase craft. She saw beauty in the curve of valves, in the redundancy of safety bells, in the clever little vents that sang when pressure dropped.

Then she saw the hidden bypass.

Mara saw Tavi see it.

No one else had time to wonder before Tavi crossed the chamber, climbed a half-built engine, and tore off a polished cover plate with both hands.

Under it lay a narrow command channel.

Not active. Not labeled. Waiting.

The forge went quiet by degrees, hammer song dying platform by platform.

Vellit paled. "A contingency."

"A throat," Tavi said.

"If pressure cannot be released, a central halt may be necessary."

"A central halt of what?"

He did not answer fast enough.

One of the dead witnesses, Othel, leaned over the channel. "This looks sized for name current."

The refugees understood before the engineers wanted them to.

Voices rose.

Outside, the root-cables pulsed harder.

Choir sabotage would have been simpler. This was worse because it belonged to fear wearing Tavi's own diagrams. The guilds had taken her release design and added a place where command could be installed later, when everyone was too desperate to object.

Tavi stood on the engine frame, small and furious in the forge heat.

"No engine leaves with a hidden channel."

Vellit's face hardened. "Then engines do not leave fast enough."

"They leave slower and honest."

"People will die."

"Yes," Tavi said. "And if we build the channel, more people will live long enough to be made functions. I am done pretending delayed harm is a discount."

The younger engineer who had muttered before climbed onto the opposite platform. "You would put every maker on trial for every misuse?"

"No. I would put every maker in the same room as foreseeable harm before calling the diagram complete."

Tavi pulled a charcoal pencil from her hair. Mara had no idea how it had survived there. Tavi began writing directly on the engine frame.

Maker named.

Purpose named.

Known harms named.

Refusal function visible.

Alteration logged.

Emergency override expires.

Affected witness may challenge.

Vellit stared. "This is not engineering."

"It is now."

The root-cables screamed.

Every warning bell in the forge rang at once. Cinder pressure spiked through the dead tree, red light racing along roots. A railbed north of the valley had collapsed under the weight of marching dead, and the pressure wave hit Brassroot like a fist. Three unfinished engines flared. The hidden command channels lit, responding faster than the release valves because command was always designed to be efficient.

The forge offered one answer.

Halt.

Every cinder-fed machine in the chamber leaned toward the word.

Mara felt it in her teeth. She could seize the halt, hold it, force the engines quiet. The dragons had offered her that shape. The guild had built it anyway. The world kept placing her hand on the same lever and changing the inscription.

Tavi looked down at her.

"Do not," she said.

Mara stepped back.

Not because she was unafraid. Because Tavi had the right to own this answer.

Tavi slammed both heels against the engine frame. "Witness panels open!"

For half a second, no one moved.

Then Kesh threw a wrench at a lever. Brakka ripped a cover from the second engine. Saelith dragged refugees toward the panels and put their hands on brass plates. Ilyr and Maelin cut shadow routes between overheating channels. Caldus, one arm useless, held a buckling support with his shoulder while two gnomes bolted it. Sava shoved Othel toward a name plate. "Object usefully!"

Othel placed his dead hand on the panel. "I object to being fuel."

The panel flashed blue.

True.

Others followed. Living, dead, gnome, goblin, troll, elf, human. Not trained. Not efficient. Answerable. The hidden halt channels stuttered as refusal current entered the system. Tavi opened each visible release valve in sequence, shouting names as she did: makers, risks, towns saved, harms not excused. Steam blasted through the forge roof. Bread ovens exploded in a rain of half-baked loaves, which Kesh later called the most emotionally complicated miracle of the war.

The pressure wave passed.

The engines held.

The hidden channels melted into slag.

Tavi climbed down from the frame with both hands burned and her face streaked with soot.

Vellit looked at the ruined command channels, the saved engines, the refugees still touching witness panels, and the guild engineers watching him with faces no longer safely obedient.

"You have made us liable," he said.

Tavi's laugh shook. "No. I made you admit you already were."

By morning, the first Brassroot liability code was stamped onto every release engine leaving the forge. Some guild masters refused to sign. Their engines stayed. Some signed and looked as though the ink weighed more than metal. The younger engineer who had challenged Tavi asked, very quietly, whether the refusal function could be made harder to bypass. Tavi handed her a wrench and said, "Finally, a romantic question."

The engines rolled out by noon toward railbeds, bridges, and towns bright with pressure warnings.

Mara found Tavi sitting under the dead tree's outer root, hands bandaged, head tipped back against the bark.

"You changed engineering law," Mara said.

"I added paperwork to explosions."

"That is one of the definitions of civilization."

Tavi closed her eyes. "My master would hate it."

"Good?"

"No." She opened her eyes. "Not good. But true."

From the road, one of the new engines began to hum. Not command. Release. It sounded plain, ugly, and necessary.

Tavi listened until the engine passed out of sight.

"Tools inherit makers' morals," she said. "I kept trying to make better tools. Annoyingly, I may have to keep making better makers."

Mara sat beside her under the dead tree while steam drifted over Brassroot like weather that had finally been told who it might harm.

Far north, the Choir's black fires multiplied.

This time, the roads had engines that could say no.""",
}


EXTRA_DEEPENING: dict[int, str] = {
    9: r"""The climb did not end with landing. The first sky-isle tested them for another mile.

Black grass cut at their boots with glassy edges. Pools of rain held reflections from different hours: Mara saw herself at dusk though morning stood overhead; Caldus saw a battlefield and stopped walking until Saelith touched his sleeve; Kesh saw a road under reed flood and turned his face away. Above them, little storm-birds made of static nested in the ribs of ruined towers. They snapped at Tavi's brass buttons until she threatened to classify them as weather with criminal intent.

The island had once been a listening post. Eshkarun said this without saying it. Mara felt the shape of the place in cinder scars and scale seams: dragons had perched here to hear mortal petitions before courts were invented to make listening less personal. The old steps were still carved for feet of many sizes. Human sandals. Elven slippers. Troll pads. Goblin climbing notches. Gnome boot hooks. Dragon claws. Evidence that, once, ascent had not required being nearly killed by wind.

"Why break the old road?" Mara asked.

Eshkarun landed on a higher ridge with such force that thunder rolled from the grass. Roads are broken by those who use them badly.

"Convenient. Then the powerful always get to close the gate and blame travelers."

The dragon turned his great scarred head. Below his left eye, the pale groove along his muzzle crossed three scales and disappeared under the jaw. Mara saw, with sudden certainty, that a mortal chain had made that scar. Not a sword. Not another dragon. A chain thick with cinder-work, pulled by engines and fear.

Eshkarun noticed her seeing.

Yes, he said. Mortals made cages. Dragons made judgments. Both called the other proof.

Mara thought of Othrava, named in Orrowen as dragon, person, used without consent, witness pending her own answer if answer remained possible. "And Othrava? Does the court count what happened to her as a mortal crime or a dragon failure?"

For the first time, Eshkarun did not answer at once.

The storm around the sky-isle grew quieter.

The court counts slowly, he said at last.

"That sounds like no."

It sounds like shame, small title. Learn the difference before you spend yours.

He launched before she could reply, leaving the company under a rain that tasted faintly of iron. Mara stood with the others among broken steps built for a more answerable age and felt the true size of the court ahead. Dragons would not be simple allies. They were not ancient decorations for human awe. They were people who had survived long enough to build elegant excuses around their own wounds.""",
    10: r"""The court did not only receive mortal evidence.

That, Mara realized, would have been too easy for dragons. They were proud, not careless. When the company's memories finished burning, the gray dragon lowered her broken horn and opened one of her own.

The scale floor filled with the first age seen from above. Mara saw a valley before Vael Taryn had a name, when human camps smoked beside elf groves and troll bridges crossed rivers still arguing with their banks. Dragons descended not as conquerors but as witnesses, enormous and curious, lowering their heads to hear tiny disputes over water, oath, marriage, burial, boundary, song. For a breath, the vision was almost gentle.

Then fear learned craft.

Mortals built the first cinder chain from a dragon scale given freely and a law written badly. They told themselves it would bind only violent judgment, only rogue fire, only one dragon for one season until treaties settled. Mara watched the chain close around a young storm-dragon's throat. She felt the terror of every person holding the chain and the terror of the dragon held by it. Both were real. Both became excuse.

The memory shifted. Dragons retaliated against a valley that had not forged the chain. Mortals built deeper cages. Dragons judged entire cities by the worst engines hidden beneath them. Mortals hid more engines. The circle tightened until law became preparation for betrayal.

The gray dragon ended the memory before anyone could turn it into comfort.

We remember proportion poorly when hurt is large, she said.

"Then why should your memory judge us?" Maelin asked.

Several dragons looked at her. Khar Veyl's opened record had not made her fearless; it had made fear less persuasive.

The black dragon in the suspended pool answered. Because memory admits injury where speech arranges innocence.

"Memory arranges innocence too," Ilyr said. "It simply uses better lighting."

The green twins coiled tighter around their inverted tree. One of them spoke in a voice like leaves dragged over stone. Short lives make sharp ethics. You die before consequences finish blooming.

"And long lives make tidy distance," Sava said from behind Mara, where she had somehow managed to continue taking notes in a dragon court. "You outlive the people who would correct your version."

The court liked that least of all.

Mara felt the balance shift. Not in their favor. Not against. Toward difficulty. The dragons had expected mortals to plead, defend, and perform guilt. They had not expected clerks, exiles, oathbreakers, engineers, and debt-bearers to make memory itself answerable.

That, more than any speech, became evidence.""",
    11: r"""The memory did not release Kesh when the court pronounced debt entered.

It showed what came after.

Rikka's branch did not vanish into one clean tragedy. They survived in pieces, which was harder for Kesh because survival kept sending invoices. A boy named Noll lost two fingers to frost after the toll seizure took the winter gloves. Rikka's aunt sold her painted wagon wheels one by one. Three children joined another caravan and changed their clan paint because shame travels faster than fact when powerful people write the first notice. Rikka learned to guide dangerous clients because safe ones had become too expensive to trust.

Then the memory showed the storm tunnel, not as Mara had seen it, but from Rikka's last hour. Royal agents in gray cloaks had promised storm toll and paid in silence. They wanted the route to the dragon court because kings, too, had begun to dream of authority over cinders. Rikka led them as far as she had to, then jammed her road token into a heat seam and drew the sky eels with her own blood-warmed knife. She did not die cleanly. She did die keeping the agents from reaching the court before Mara.

Kesh made no sound.

That was how Mara knew the memory had struck the deepest place. Kesh had built his life out of sound: joke, bargain, insult, road call, song sung badly on purpose. Silence on him looked like a bandage wrapped too tight.

When the vision faded, Auntie Varr was not there to accuse him. Rikka was not there. No survivor of the Orrin branch stood in the dragon court to say what payment meant. That absence had weight.

Mara named it.

"We cannot finish this here."

The gray dragon tilted her head. Why?

"Because the harmed are not present."

The red-gold dragon's tail scraped sparks from stone. Harm may be weighed by witness.

"Weighed is not repaired."

Kesh looked at her then, and his eyes were wet in a way he would once have turned into comedy. "Some will not want repair from me."

"Then you will owe them the dignity of not being useful."

He laughed once, brokenly. "That is a cruel sentence."

"It has your name on it."

Brakka grunted approval. "Debt with no forced forgiveness. Better."

The court entered that too. Mara felt it sink into the scale floor beside the red dust road: correction pending not only because Kesh needed to act, but because the people harmed retained the right to refuse his performance of remorse. Dragons remembered truth. Mortals, at their best, could insist truth did not end the matter.

Kesh stood among them afterward with nothing clever in his hands.

It was not redemption.

It was the first honest mile.""",
    12: r"""The refusal cost them before they left the court.

Messages arrived in stormfire, bursting above the scale floor one after another. A village under the north rail had vanished into a sink of awakened dead. A Pale Remnant hymn cell had seized a healer school and promised families their risen children would become peaceful if entered under white law. Harrowmere's council had authorized emergency cinder seizures despite Mara's refusal. In the west, Vorrakai's Choir walked into plague camps and offered the dead rest without names and the living a night without nightmares.

Every report made the dragon offer look wiser.

That was part of the trial too, whether the dragons admitted it or not.

Mara stood beneath the storm reports and let herself want command again. She did not pretend herself clean. Cleanliness was another costume power wore when it had time to dress. She wanted the lever. She wanted the fast answer. She wanted to stop hearing children in reports.

Then Sava's voice came from behind her. "Minutes note: refusal maintained while visibly miserable."

Mara turned. "That cannot be an official category."

"It is now. Many important decisions should be banned if the decider enjoys them too much."

The gray dragon studied Sava as if clerks had suddenly become a weather system.

Eshkarun pushed his shed scale toward Mara with one claw. The bronze surface held stormlight and a memory of his scar. Use it badly and it will remember.

"Everything does," Mara said.

The white dragon added three place-names not in any mortal map: Gate of Failed Victories, Arch of Unchosen Sacrifice, Canal of Last Refusals. Each name cut Mara's tongue when she repeated it. Each marked an entrance to the Dead Capital, and each carried a warning. The way in would choose which temptation arrived first.

The black dragon gave no gift, only a sentence. Vorrakai cannot be beaten by proving him cruel. He has admitted cruelty into mercy and made a bed for it.

"Then what beats him?"

The black dragon's eyes were old pools. A world that suffers and still refuses his conclusion.

No one liked that answer either.

When the storm gate opened, Mara looked once more toward the court tiers. "Othrava remains witness pending."

Several dragons lowered their heads. Not enough. But not nothing.

The gray dragon answered, Enter the Dead Capital and bring us a question she can answer, if answer remains in her.

Mara held that vow, imperfect and overdue, as the floor disappeared beneath her boots.""",
    13: r"""The compact's first hour was mostly failure.

That mattered enough that Sava recorded it under a separate heading.

A Harrowmere captain tried to reroute dead cavalry without notifying the dead. A Lumenorath healer refused Khar Veyl shadow cover until Saelith stood in the rain and asked whether she preferred pure casualties. A goblin route speaker rejected a refugee column because its payment seal was wrong; Kesh backed the refusal until he learned the seal had been issued by a dead clerk whose hand no longer matched the living registry. Three gnome engineers argued that maker liability slowed deployment, and Tavi told them if they wanted innocence they should build furniture and even chairs harmed people when designed by cowards.

Mara wanted to scream.

Instead, she carried messages.

That was the hidden labor of refusing rule. People imagined it meant standing above power with clean hands. It meant walking through mud between furious groups, repeating what one side had actually said until the other side stopped improving it into an insult. It meant admitting when speed mattered and when speed was only hierarchy trying to sound practical. It meant letting people be angry at her because she was visible and the actual problem was too large to fit in one face.

At the wagon-door table, Othel the dead clerk raised his translucent hand so often Sava threatened to assign him a bell.

"Point of procedural irritation," he said.

"Recognized with regret," Sava replied.

"If dead witnesses may object to living orders, living witnesses must be permitted to object to dead orders. Equality of nuisance."

Durn carved the phrase into a bridge chip before anyone could stop him.

By the time the Snow Cedar alarm arrived, the compact had acquired seventeen amendments, four temporary contradictions, and one snack schedule everyone pretended was not essential. It was ugly. It was slow. It made every commander in the rain look older.

It also meant that when Mara named tasks, people already knew who could challenge them.

That, not inspiration, sent the first runners north.""",
    14: r"""The dead were the first to find the buried.

After the avalanche split, after the Choir withdrew, after the pass stopped moving long enough for people to pretend the ground had forgiven them, the living searched where they could see. The dead searched where they remembered falling. Oren Vall led fever-year cavalry to a drift below the second switchback and dug with gauntleted hands until they found a Lumenorath healer alive inside a pocket of branches. Harak of Broken Span, freed from the Choir plate but not from grief, sat with his back against a cedar and named every crack he could hear under the snow.

"There," he said whenever the mountain shifted wrong. "There. There."

Each there became a body found, living or dead.

Mara moved from knot to knot, lending heat where cinder veins could warm without command, pulling back when the warmth began to want orders. That restraint exhausted her more than force would have. Force had a clean line: spend power, see result. Restraint required staying present with all the things power might have fixed and all the things it would have stolen while fixing.

Caldus tried to stand three times.

On the fourth, Saelith put one bloody hand on his good shoulder and said, "If you rise before I finish stitching, I will sing a hymn about your stupidity in three languages."

"Only three?"

"I am injured."

He sat.

Mara knelt beside him after Saelith moved away. Snow had melted into his beard. His shield lay cracked in two pieces beside him.

"Old wound?" she asked.

"Old pride, mostly."

"Caldus."

He looked toward the pass where living soldiers and dead cavalry carried a stretcher together. "I could have commanded better."

"Maybe."

He smiled faintly. "That was not the comfort I was fishing for."

"We are low on comforting lies."

"Good." His face tightened as pain moved through his shoulder. "The compact worked because people had practiced answering before fear arrived. Remember that when they beg you to skip the practice."

She did.

That night, Sava read the casualty names aloud in the snow. Not numbers. Names. The list took longer than anyone wanted and less time than the dead deserved. When the last name entered the minutes, the pass felt heavier, not lighter.

Victory, Mara thought, should always be made to carry its own dead.""",
    15: r"""The compact did not become real when elders signed it.

It became real at Little Cinder Ford, three hours before dawn, when Serren Pike tried to break it.

His lacquered wagons had taken the south branch with two hundred refugees and a sealed claim that the route was proprietary under prior consortium discovery. Kesh read the claim by lantern, said a word Mara had not heard before and did not need translated, and ran. By the time they reached the ford, Serren's guards had blocked the crossing and begun charging families extra for passage on rafts made from stolen doors.

The Choir had seen the delay.

Black fires moved on the ridge.

Kesh did not draw a knife. That was how Mara knew the dragon court had changed him in a way that hurt.

He walked into the ford light with both hands visible. "Route challenge."

Serren laughed. "Now?"

"Especially now."

"Children are waiting."

"Yes," Kesh said, voice carrying over water and fear. "So stop standing on their road."

Serren held up the sealed claim. "Prior discovery. Consortium protection. Emergency surcharge."

Auntie Varr spat into the river. "Emergency theft."

Mara felt the old urge in the crowd: let the thief continue if continuation moved faster. That was how cruel systems survived catastrophe. They made themselves the bridge and dared mercy to burn them.

Kesh turned to the refugees. "You can cross while we argue. Payment enters public debt, not Serren's purse. If I lose the challenge, I owe the difference."

Serren's smile sharpened. "You cannot cover it."

"No," Kesh said. "We can."

Goblin clans stepped forward. Not all. Enough. Then a troll bridge crew. Then two dead cavalry. Then a Harrowmere woman who had nothing but a wedding ring and gave it anyway until Sava made her take it back and entered the gesture as moral collateral, which everyone agreed was less spendable and more embarrassing.

The first raft crossed under mixed witness.

The second.

The black fires reached the ridge crest just as the last child crossed.

Serren's claim failed by dawn. He had discovered the route, yes. He had done so with three unnamed guides, one dead, two unpaid, and a bridge mark belonging to Third Arch. Under the compact, that made the road shared, the surcharge void, and his purse vulnerable to public creativity.

Kesh watched Serren sign the correction.

"That could have been me," he said.

Mara stood beside him in the gray light. "It was."

He closed his eyes.

"And?"

"And now it was not."

The answer did not forgive him. It did something more useful. It gave the next choice room.""",
    16: r"""The liability code changed the sound of Brassroot.

Before, the forge had rung with mastery: hammers certain of their rhythm, valves snapping open and shut, engineers shouting over one another in the cheerful violence of people who believed the world improved when properly assembled. After Tavi's code, another sound entered. Names.

Maker named: Jessa Pin, apprentice valvewright.

Purpose named: pressure release for north railbed.

Known harm: scald radius if gauge ignored; possible name-current if altered.

Refusal function: visible panel, mixed living-dead witness.

Alteration logged: none, under penalty of public minutes and personal liability.

At first the engineers muttered the words as if embarrassed. Then the refugees waiting outside the forge began listening. Then the dead witnesses began correcting omissions. Then the younger engineers started arguing over whether a known harm had been named honestly enough, and the argument sounded different from guild vanity. It sounded like fear being made useful without being allowed to rule.

The young engineer who had challenged Tavi was named Pinna Vey. She followed Tavi from engine to engine with a wrench, a slate, and the expression of someone discovering that admiration was less comfortable when it required changing sides.

"If we make the refusal panel too easy," Pinna said, "panic can shut down release during a pressure spike."

"Yes," Tavi said.

"If we make it too hard, refusal becomes decorative."

"Also yes."

"That is annoying."

"Engineering."

Pinna frowned at the panel. "Dual threshold. One trained, one affected witness. Emergency temporary bypass expires when pressure drops below red."

Tavi looked at her for a long moment. "Good. Write your name beside it."

Pinna did. Her hand shook.

Mara, watching from the root stair, understood then why Tavi's victory hurt. Tavi had not defeated the guilds. She had made them less able to hide from the people their tools touched. That meant every future failure would have a signature. It also meant future repair could find a door.

Near sunset, the first liability-stamped engine reached a town called Wether Mill before its railbed burst. The report came back by goblin runner and cinder relay together: pressure released, dead miners uncommanded, three burns, no name-current, maker panels intact. The town sent bread in gratitude. Half the loaves were from the accidental oven blast and tasted of smoke.

Kesh ate two. "Ethical bread is complicated but filling."

Tavi leaned against a root, eyes closed, bandaged hands in her lap. "If anyone calls it Tavira's Law, I will fake my death."

"Too late," Sava said, writing.

"Sava."

"History is cruel."

"History can meet me behind the forge."

Mara laughed. It felt good and alarming, like standing too near a machine that had stopped exploding.

Then Othel's translucent head lifted.

"Message from the north record line."

The forge quieted.

Othel listened to something none of the living could hear. "Dead witnesses are gathering near the old capital roads. Many. Not under Choir command. They are asking for Arveth."

Mara's hand went to the ledger mark in her satchel.

Arveth had chosen a lighter anchor. Not one book. Not one person. Everywhere he was properly heard.

The mark warmed.

One word appeared on the nearest witness panel, thin as ink in rain.

Coming.

Tavi stared at it. "That is either comforting or legally alarming."

Mara looked north, where black Choir fires pricked the horizon and the roads of the dead began turning toward Vael.

"Both," she said.

The War of Every Road had found its counter-song.""",
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
    text = re.sub(r"\n*# Part II: The Court of Long Memory\n+", "\n\n", text)
    text = re.sub(r"\n*# Part III: The War of Every Road\n+", "\n\n", text)
    text = re.sub(
        r"(?m)^## Chapter 9:",
        "# Part II: The Court of Long Memory\n\n## Chapter 9:",
        text,
        count=1,
    )
    text = re.sub(
        r"(?m)^## Chapter 13:",
        "# Part III: The War of Every Road\n\n## Chapter 13:",
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
        'current_form: "full-length draft zero with Book Three chapters 1-16 revised in pass 01"',
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
    print(f"Book Three chapters 9-16 revised. Word count: {total}")


if __name__ == "__main__":
    main()
