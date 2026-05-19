#!/usr/bin/env python3
"""Revision pass 01e for Book Two chapters 19-21.

Replaces the first Blackroot Road scaffold chapters with bespoke scenes:
the fungal witness forest, the mirror cavalry salt flats, and Tavi's Glass
Engine crisis.
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
    19: r"""## Chapter 19: Fungal Forest of Witnesses

The forest began by borrowing faces.

At first Mara thought the pale shapes among the black trunks were travelers' masks. They hung at shoulder height from curtains of moss: child faces, old faces, hard-cheeked soldier faces, mouths open around words the damp air refused to release. Then the nearest one turned toward her without any neck to turn on, and she saw that it was not carved from wood or bone. It was a mushroom cap, translucent as wet parchment, grown into the suggestion of eyes, nose, lips, grief.

Behind her, Kesh said, "I would like to register my objection to vegetables that recognize me."

"Fungus," Tavi corrected, because fear had never stopped her from being exact.

"I object to scholarship that recognizes me."

Brakka lifted the glow-cage higher. Its beetles had dimmed since the road forked. Their little green bodies pulsed in the iron mesh like uncertain stars. Beyond them, the Blackroot Road narrowed between columns of root and stone. Some roots were thick as siege towers. Some hung from the roof of the cavern in veined curtains, drinking mineral water from the dark. Mushrooms grew everywhere: shelf-fans blue as twilight, white cups full of trembling rain, towers of red sponge, black bells whose undersides glittered with spores.

The place was beautiful in the way a wound could be beautiful when the blood caught light.

Mara had seen forests above ground, even if Ashgate had taught her trees mostly as fuel, beams, gallows, paper, price. This was not that. The fungal forest had no sun, no birdsong, no wind moving through leaf and branch. Its weather was breath. The whole cavern inhaled around them, slow and damp, then exhaled through a thousand gills.

Each breath carried voices.

Not words at first. Just the pressure of them. Testimony without mouths. Pleas without listeners. Mara felt them gather at the back of her teeth where cinder-singing always began, and she clenched her jaw until pain steadied her.

Saelith noticed. Saelith always noticed too much and then blamed herself for having eyes.

"Can you hear them?" she asked.

"Not clearly."

"That sounded like a merciful lie."

"It was a hopeful one."

Saelith's hand hovered near Mara's elbow, not touching. Since Lumenorath, even kindness between them had learned to ask permission. Mara loved and hated that. She wanted simple things no longer available to her: bread without prophecy, sleep without witnesses, hands without history. Instead she had a road under the world, a war behind her, dead law ahead, and a woman beside her whose former people might still decide mercy was treason.

The first borrowed face opened its mouth.

Light spilled out.

The forest vanished.

Mara stood in a hall she had never seen, under rafters carved with two moons. Dark elves in ink-black court robes faced light elves in white armor polished until it made the room seem guilty. Between them stood Orrowen dead, not yet called dead in the old records. Their skin held the gray luster of ash after rain. Some wore civic chains. Some wore armor. One elderly woman held a ledger against her ribs like a shield.

The vision smelled of hot wax, sea salt, and dragon blood.

"Emergency covenant," said a light-elf voice. "Temporary authority. Containment until the moon below is quieted."

"Witness rights preserved?" asked the elderly Orrowen woman.

"Preserved in principle," said a dark-elf judge.

The old woman looked at him as if principle were a knife she had seen before. "Principle does not open doors, Lord Noct-Vey."

Mara reached for the woman's name and found only static. The record had been rubbed thin there.

Then a stamp fell.

The hall shattered.

Mara staggered back into the cavern. Caldus caught her by the shoulder, not hard enough to trap, only enough to say she had returned. Tavi's root-hound crouched beside her boots, brass ribs trembling. It had been damaged in the Blackroot evacuation, one foreleg bound in wire, one glass eye cracked. Now it growled at the mushroom face as if the forest had insulted engineering.

"What happened?" Caldus asked.

"Old covenant." Mara tasted salt though there was none on her tongue. "Light and dark courts. Orrowen standing. They promised rights during an emergency."

Ilyr went very still.

Maelin Noct-Vey did not. The released daughter of Khar Veyl's ruling house stepped toward the mushroom face with the rigid grace of someone walking to her own sentencing. The half-healed binding marks around her wrists darkened in the glow.

"Which Noct-Vey?" she asked.

"Lord. Judge. I could not hear the given name."

"Convenient," Kesh muttered.

Maelin did not rebuke him. That worried Mara more than anger would have. "My house kept private seals from that period. We were told they were ceremonial duplicates."

Ilyr looked at her. "I helped catalogue some of them."

"Did you know?"

"No."

"Did you avoid knowing?"

The question struck more cleanly than a blade. Ilyr's face tightened, and for a moment he looked as young as he must have been when Harrowmere first taught him that elegant omissions could be survival.

"Yes," he said.

The forest breathed.

Every mushroom face turned toward him.

Spores lifted in a silver sheet.

"Down," Brakka said.

She shoved Maelin behind her shield as the spores crossed the path. They did not fall like dust. They arranged themselves into words. Mara saw them forming in the air, sentence after sentence written in glittering motes.

STATE NAME.

STATE OFFICE.

STATE WHAT YOU PRESERVED.

STATE WHAT YOU SOLD.

Ilyr drew one of his thin knives, then stopped because there was no throat to cut. His hand lowered. The most dangerous thing he could do in that forest was pretend the question was not his.

"Ilyr Noct-Vey," he said. "Former archivist to House Noct-Vey. Former under-script broker in Harrowmere. I preserved legal gaps. I sold access to names I had no right to price. I told myself I was keeping worse people from buying them. That was sometimes true and never enough."

The spores flared blue.

Accepted, Mara thought, though no voice spoke the word.

Then the forest turned to Kesh.

He smiled brightly. "Absolutely not. I am allergic to moral botany."

STATE NAME.

STATE OFFICE.

STATE WHAT YOU PRESERVED.

"Kesh," he said. "Just Kesh."

The spores did not move.

His smile thinned.

Brakka looked down at him. "Road asks plain."

"Road can wait in line."

Mara saw his fingers twitch toward the gray coin-moth mark on his wrist. The fever-road debt had not faded. It lay there like a sleeping insect under the skin: Reedmere, Tallow Ford, Neth-by-the-Salt. Three places he had promised by refusing to close the road easy. Three villages that would default unless someone held open a passage. Kesh had made jokes ever since because jokes were cheaper than terror.

STATE WHAT YOU PRESERVED.

His shoulders shifted as if he were trying to step out of his own body.

"Routes," he said at last. "Unlicensed passages. Smuggler roads. Names of people who needed to leave before law agreed they were people. I preserved exits."

STATE WHAT YOU SOLD.

"The same thing, when I was hungry."

The spores brightened, but not enough.

Kesh swallowed. His voice lost its shine.

"I sold exits to people who could pay and told myself the routes staying open helped the people who could not. Sometimes it did. Sometimes I just liked being necessary."

Blue fire ran through the fungal caps. Not forgiveness. Record.

Sava Rennet, who had not breathed for centuries and still managed to sound tired of everyone's foolishness, nodded. "Better."

"I was aiming for charming," Kesh said.

"You missed."

"Cruel archive."

The path accepted him.

They moved deeper.

The forest changed as they walked. It was not one place but a library grown in rot, each grove tuned to a different kind of memory. In one hollow, pale puffballs burst under their boots and filled the air with children's voices reciting bridge tolls from a city drowned before their grandparents were born. In another, black shelf-fungus grew from a broken spear and repeated the last argument of two soldiers who had died on opposite sides of the same lie. A yellow curtain of lace mushrooms whispered wedding vows from Orrowen's river district. A stand of red bells screamed whenever Saelith's dawn charm touched them, not in pain but in recognition.

"Stop," Saelith said, yanking her hand back.

The red bells showed Lumenorath.

Not the bright city Mara had seen above, not the sanctified roads and white towers. This was an older chamber, lower and humbler, where light-elf healers knelt beside Orrowen dead and washed ash from their hands. No hymn wagons. No cleansing decrees. No Serathiel with mercy sharpened into doctrine. A woman in plain white linen looked up at someone outside the vision and said, "If memory is the wound, then we must learn not to cut it out."

Saelith covered her mouth.

"Who is she?" Mara asked.

"Matriarch Aurenne," Saelith whispered. "First oathmother of the Pale Bough. Serathiel quotes her in every cleansing litany."

"Does he quote that part?"

Saelith laughed once, too harsh for humor. "No."

The red bells dimmed.

Behind them, something cracked.

Caldus raised his sword. The sound came again, farther right: a wet, fibrous snap. Then another. Then a whisper of movement through the mushroom stands.

Brakka sniffed. "Not forest."

"How can you tell?" Tavi asked.

"Forest is old. This is impatient."

The attack came from borrowed faces.

Mushroom masks tore free from their stems and lunged on bodies made of root, corpse-bone, and black hyphae. They had no eyes except the false ones grown into their caps. They moved in quick, jerking bursts, each one wearing a dead person's last expression. One came at Caldus with a child's face and a spear of hardened root. Another dropped from above onto Brakka's shield, fingers digging grooves in ironwood. A third opened three mouths at once and spoke in voices Mara knew from the drowned archive.

Emergency authority.

Temporary containment.

Acceptable loss.

The words hit harder than the bodies. Where they landed, the company faltered. Caldus's sword wavered when the child-faced thing thrust at him. Saelith's charm guttered under the phrase acceptable loss. Maelin went white at temporary containment.

Mara understood too late. These were not Orrowen's witnesses.

They were the lies that had grown on top of them.

"Do not answer the faces," Edrin Vale called. The dead Orrowen citizen stood with waterless archive light in his hollow eyes. "Answer the record underneath."

A root spear slashed Mara's sleeve. She felt the skin open along her forearm, hot first, then cold. Saelith stepped between her and the next blow, dawnlight flaring from her palms. The light struck a mushroom mask and the borrowed face changed. For one awful heartbeat it wore Saelith's own features, serene and empty, mouth forming words from Lumenorath's decree.

Clean mercy requires clean ash.

Saelith froze.

Mara slammed into her, knocking them both down as the root spear passed above their heads. Pain flared through Mara's cut arm. She rolled, grabbed a fallen glow-cage hook, and drove it through the thing's ankle. It did not bleed. It leaked spores.

"Saelith," Mara said.

Saelith's eyes were wide, not with fear of death but with recognition. "That was me."

"No. That was what they wanted you to become."

"How do you know the difference?"

Mara shoved herself upright. Around them the forest shook with fighting: Brakka breaking a root-body against a stone, Kesh darting under a spear to cut fibrous tendons, Tavi shouting at the root-hound to stop trying to bite philosophy, Caldus putting himself between Maelin and a half-grown lie in judge's robes.

"Because you are still asking," Mara said.

Saelith breathed in.

Then she stood.

Her next light was not white.

It was gold, faint, imperfect, threaded through with the red of the fungal bells. It did not burn the masks. It revealed the bodies beneath them. Each root-thing flickered, and inside each Mara saw a buried record: a toll-taker whose name had been replaced with "asset," a canal child counted as "water loss," a soldier labeled "unrecoverable," a dead clerk recorded only as "ink-hand." Not monsters. Not even ghosts. Misfiled people, used by the forest's infected edges because no one had corrected the entries.

Mara tasted cinder heat.

The old hunger to command rose with it. She could have pushed. The cinder would have obeyed, maybe. The root-bodies were full of memory. She could have taken their names and made them still.

Vorrakai stirred somewhere far below.

The sensation was not speech. Not yet. A deep attention, patient and kind in the way a grave was kind: no struggle, no shame, no wrong choices left to make.

Mara recoiled from it so hard she nearly dropped to one knee.

Caldus saw. "Mara!"

"Names," she gasped. "Give me names. Not titles."

Edrin understood first. "Rola Fen, lower tolls. Berrit of Canal Nine. Sesh Anvar, clerk of repairs. Dama Veyt, ferry guard. Olun, no house name recorded."

Sava added hers, voice cutting through the fight like a filing blade. "Nim of south laundries. Hessar, bridge-lighter. Pell-Under-Red, licensed peddler. Maeth of the ash quay."

The root-bodies slowed.

Maelin joined, reading from the copied ledger with shaking hands. Ilyr took the other side of the case and read with her, his voice less beautiful and more honest than Mara had ever heard it. Kesh, bleeding from a cut above one ear, started calling route names as if they were sacred: "Reedmere north ditch. Tallow Ford mill hollow. Neth-by-the-Salt third cellar. Kavik night stair. Ashgate east runoff. If a road carried you, it remembers."

Brakka planted her maul and spoke troll bridge oaths in a language that made the stones hum. Tavi held the damaged root-hound against her hip and read brass inventory marks from its cracked eye, because apparently even a machine could remember the hands that made it badly and lovingly both. Saelith said Matriarch Aurenne's forbidden line again and again until the red bells answered.

If memory is the wound, then we must learn not to cut it out.

Mara opened her cut hand over the cinder cage.

"You are entered," she said.

The words went through the forest.

Not command.

Not absolution.

Record.

The root-bodies collapsed. Masks fell from them like wet leaves. Some dissolved into spore-light. Some remained as small white caps on the ground, each marked with a new line no one had carved.

Rola.

Berrit.

Sesh.

Nim.

Olun.

The forest exhaled.

For a long time no one spoke.

Then Tavi sniffed and said, "I am putting that entire event under 'hostile indexing.'"

Kesh sat down heavily on a stone. "Please also note that I bled for cataloguing reform. I expect future historians to describe my cheekbones kindly."

"They will write that you were loud," Sava said.

"Accurate and cruel."

Caldus knelt by Mara. "Your arm."

"Later."

"Now."

There were many versions of Caldus. The king's knight, the broken oath, the man learning to ask before guarding, the soldier who could make one word heavier than a lecture. This was the version that looked at a bleeding wound and refused drama.

Mara let him bind it.

Saelith stood beside them, still pale. "I heard it."

Mara did not have to ask what.

"The thing beneath," Saelith continued. "The stillness."

Kesh's jokes went quiet.

Ilyr looked down the road, where the fungal trunks leaned away from a darkness that did not belong to the forest. "Vorrakai."

The name did not echo. That was worse. The cavern absorbed it like soil taking rain.

"It felt merciful," Saelith said.

No one contradicted her.

That was the honest terror of it. Mara had felt it too. Not cruelty. Not rage. A vast invitation to lay down every burden and call the silence peace. She thought of Ashgate workers who would have taken it on their worst nights. Of fever-road children. Of soldiers dying under banners they had never chosen. Of dead Orrowen citizens forced to keep arguing because the living had never finished betraying them.

Of herself, before Joryn, before cinder, before anyone had asked what she wanted and waited for the answer.

Brakka broke the silence. "Mercy that takes your mouth is not mercy."

The troll's words settled into the road with the weight of law.

Past the cleared grove, the fungal forest thinned. The borrowed faces no longer watched from every stem. Instead they turned in one direction, all of them angled toward a pale gap between black roots.

Edrin bowed to the caps. "Witnesses indicate passage."

"To Orrowen?" Mara asked.

"To the old salt flats," he said. "Orrowen's outer memory. Armies liked to die there because commanders could see themselves being important."

"That is the most honest military history I have ever heard," Caldus said.

They packed what could be packed. Tavi tightened the splint on the root-hound's leg. Ilyr and Maelin sealed the ledger case together, and neither pretended the gesture was nothing. Saelith cut one red bell from its stem only after asking the forest aloud if it objected. It did not. She tucked the fungus into a glass vial with water and a strip of white linen.

Mara lingered by the first borrowed face.

Its features had changed. Not child, soldier, judge, or clerk. For a breath it looked like Arveth as Mara had last seen him in memory: not alive, not safely dead, smiling as if he had found a loophole in extinction and intended to irritate history with it.

Then the cap folded inward, and a spore-letter formed on its surface.

COURTHOUSE CONTINUES.

Mara touched the line with two fingers.

"We are coming," she said.

The forest gave no blessing. It did not need to. Behind her, the company gathered itself around wounds, ledgers, debts, and choices that had not become easier simply because they had become clearer.

They stepped through the pale gap.

The air changed from damp breath to salt.

Ahead, under a cavern roof lost in starless dark, a white plain spread wider than any field Mara had ever seen. It shone with shallow water and salt crust, reflecting the glow of distant bone-fires until the whole world seemed upside down.

At the far edge of that brightness, something moved in the reflections before it moved on the ground.

Horses.

Lances.

Riders without faces.

Caldus drew his sword.

"No one look down," he said.

Mara looked anyway, because underdogs and heroes were both mostly made of bad timing.

In the saltwater at her feet, the cavalry lifted their lances and began to charge.
""",
    20: r"""## Chapter 20: Mirror Cavalry

The cavalry came first in reflection.

On the salt flat itself, nothing moved but the company and the shiver of their own pale shadows. The cavern roof arched so high above them that Brakka's glow-cage could not find it. Bone-fires burned miles away, blue and steady, making the shallow water at Mara's boots shine like polished steel. Every step cracked salt crust under the thin flood. Every crack multiplied beneath them until the ground looked like a map of broken vows.

But in the water, riders gathered.

They did not rise. They were already there, upside down and waiting. Horses of black glass pawed at a reflected sky that did not exist. Lances lowered. Helmets turned. Their armor was ceremonial, too clean for battle, each breastplate stamped with Orrowen civic seals and old elven emergency marks burned over them like brands.

"That is objectionable," Kesh said, very softly.

Tavi crouched despite Caldus's order and peered through the cracked lens she used when ordinary terror needed a diagram. "The light is not behaving. Reflections are leading the bodies by three breaths."

"Then we move before they arrive," Caldus said.

"You say that as if the ground is not made of enormous inconvenient mirror."

Brakka swung her maul onto one shoulder. "Break mirror."

Edrin Vale shook his dead head. "This flat was laid with oath-salt and dragon-scale dust. It remembers whoever looks upon it. Break one piece and every piece repeats the wound."

"So," Kesh said, "no looking, no breaking, no dying. Narrow path."

"Narrow paths are still paths," Brakka said.

The riders charged.

In the reflection, hooves struck water that did not splash. The sound arrived above ground one heartbeat later, enormous and hollow. Mara felt it through the soles of her boots. The cinder cage at her hip rattled against its leather straps.

"Run," Caldus said.

They ran.

The flat made running a negotiation. Salt cracked underfoot, then slid. Shallow water hid channels deep enough to twist an ankle. Pale ridges cut through the surface like old scars. Reflections turned every step into a lie. Mara saw herself below: ash-runner, cinder-singer, unwilling banner, mouth open in a shout that had not reached her throat yet. She saw Saelith beside her with wings of white fire she did not possess. She saw Kesh carrying a crown of coin moths. Tavi's reflection had four mechanical hands and no face. Brakka's carried a bridge on her back.

Caldus's reflection still wore a king's black cloak.

He saw it too.

His stride broke.

A lance burst from the water.

Mara shouted, but Caldus was already moving. He twisted aside, not fast enough. The lance scored his shoulder and kept rising, hauling a rider after it. The cavalryman emerged from the reflection like a blade drawn from a wound: first the lance, then the gauntlets, then the helmet, then the glass horse's head with no eyes and too many teeth. Saltwater ran upward off him into the air, then fell as glittering rain.

Caldus met the next thrust with his sword. Steel rang against salt-glass. The blow drove him back to one knee.

Brakka hit the horse.

Her maul did not smash it. It rang. The sound traveled across the flat in expanding circles, and in every circle Mara saw more riders turning toward them under the water.

"Regret," Brakka said.

"We can schedule that later," Kesh snapped.

Saelith raised both hands. Dawnlight spilled over the flat. For a moment the reflected cavalry faded, and Mara thought the light had helped. Then the riders above ground sharpened. The dawn had given them bodies.

Saelith gasped and closed her fists.

"They are using witness," Ilyr said. "Anything that reveals them completes the record."

"Excellent," Tavi said. "We are being murdered by documentation."

Another rider rose beside Maelin. Its armor bore the Noct-Vey seal under Orrowen's civic chain. Maelin did not retreat. Perhaps she was tired of stepping back from her family's ghosts. She drew the short blade Vaura had given her and struck the seal instead of the throat.

The seal cracked.

The rider screamed.

Not with pain. With memory.

The salt flat around them filled with voices.

Left wing hold.

Do not let citizens cross.

Emergency command preserves the city.

Names later.

Names later.

Names later.

Mara stumbled. The phrase hooked into her like a command. Names later was what powerful people said when they needed a body to become a number long enough for the ink to dry. Names later had fed Ashgate furnaces, Harrowmere ledgers, Lumenorath cleansing books, Khar Veyl emergency seals. Names later could justify almost anything because later never had to arrive.

The riders lowered lances again.

There were too many to fight.

Caldus rose, blood darkening his sleeve. "To the ridge."

The ridge lay half a mile ahead: a spine of black stone crossing the flat, dry enough to break reflection. Between here and there the cavalry fanned out beneath the water, matching the company's speed with impossible ease.

"They will cut us off," Ilyr said.

"Then we change what they are riding toward," Mara said.

Everyone looked at her.

She hated how often that happened now.

"The fungal forest gave names," she said. "Edrin, Sava, you know these riders?"

Edrin stared into the water. The reflections rippled across his dead face. "Some."

"Enough?"

"For accusation, perhaps. Not for freedom."

"Accusation is a door," Sava said. "Freedom is what we do after."

Kesh laughed once, sharp and delighted despite the blood at his temple. "I love a clerk who understands momentum."

Mara took the ledger case from Ilyr.

"Protect me," she said.

Caldus stepped in front of her before the last sound left her mouth. Brakka came to her right. Saelith to her left. Tavi knelt behind them, dragging the root-hound close and forcing its cracked eye open toward the water. Kesh vanished into the slant of Brakka's shadow. Ilyr and Maelin braced the case while Mara unlatched it.

The cavalry struck.

The world became hooves, salt spray, shouting, and the terrible music of lances hitting shields. Caldus fought with one good shoulder and the patience of a man who had spent his life learning exactly how long a line could hold. Brakka's maul rang again and again, each blow shaking reflected riders into brief distortions. Saelith did not use dawnlight this time. She used shadow. The red fungal bell in her vial glowed against her throat, and the light she cast was low, warm, truthful rather than pure. It showed where bodies ended and stories had been nailed on top.

Mara opened the ledger.

The pages fluttered though there was no wind.

Ink crawled toward her cut forearm. The wound Caldus had bound in the forest pulsed under the cloth. Blood had dried there, and cinder recognized blood too easily.

"No," she whispered to it. "We read. We do not take."

The cinder heat retreated half an inch, sullen as a living thing.

Edrin began naming.

"Captain Ruv Ossian, River District Fourth Civic Horse. Executed under elven emergency seal after refusing to trample evacuation boats."

A rider beneath the water faltered.

Sava joined him. "Leth of West Quay. Farrier. Listed as cavalry after death to justify horse requisitions."

Another rider's lance dipped.

Maelin read from a Noct-Vey annex, her voice cracking on the names her house had hidden. "Nerreth Vale, signal rider, testimony sealed. Imra Dass, messenger, transferred to containment. Solun and Vei, twins, not soldiers, classified mounted because they died near saddles."

The cavalry shuddered.

But the lead riders kept coming.

Their helmets turned toward Mara. No faces. Only reflective metal, and in each blank front she saw what the world kept trying to make of her: weapon, saint, answer, girl-shaped disaster. It would have been easier to become one of them. A clear shape. A useful shape. Something no longer required to decide.

Vorrakai's stillness brushed the edge of her mind.

Lay it down, the deep attention seemed to say without words. Let the cavalry stop. Let all engines stop. Let witness end in peace.

Mara almost answered.

Then Caldus cried out.

A lance had slipped past his guard and buried itself through his upper arm. The glass horse reared over him. He caught the shaft with both hands and held it there, muscles shaking, keeping it from driving deeper into his chest.

Mara's fear became clean.

Not command. Not surrender.

Choice.

"Caldus Veyr," she shouted, using the name he had once hated because it belonged to the knight and not the man. "Former captain of the Crown Stair. Witness to the King's unlawful ash levies. Survivor of Mordane's arithmetic. Protector by choice, not rank."

Caldus looked at her through pain.

"Still correcting," he said.

He snapped the lance.

The rider staggered.

Mara turned to the blank helmets. "If you want him as he was, you cannot have him. If you want us as the record made us, you cannot have us. We are not later."

The cinder under the salt flat answered.

It did not flare. It listened.

"Ruv Ossian," Mara said. "Leth of West Quay. Nerreth Vale. Imra Dass. Solun. Vei. Dama Veyt. Hessar. Pell-Under-Red. You are not cavalry because a court needed bodies. You are not horses because a ledger needed value. You are entered as yourselves."

The lead rider stopped.

The saltwater below him turned black, then clear.

For the first time Mara saw his face. Not in the helmet. In the reflection. A broad, tired face with a broken nose and eyes full of a rage so old it had become discipline.

"Who files correction?" he asked.

His voice made the water ripple.

Mara wanted to say her own name. It was what heroes did in stories, signing their courage across the sky. But she had learned too much in Khar Veyl for that vanity.

"Mixed witness," she said. "Living and dead. Human, light elf, dark elf, troll, gnome, goblin, Orrowen citizen. No single owner."

Kesh peeked from behind Brakka's shield. "I object to being last in that list."

"You were hiding."

"Strategically available."

The rider's reflected mouth almost smiled.

Then the cavalry changed.

One by one the blank helmets lifted. Faces appeared in the water first, then above it. Some were Orrowen dead in civic armor. Some were children. Some were workers. Some were actual riders with grief like weather in their eyes. The horses lost their glass teeth and became bone-thin mounts of salt and shadow, still terrible but no longer false.

The corrected did not vanish.

They turned.

Behind them, on the far side of the flat, new figures had appeared: pale-armored scouts bearing Lumenorath's cleansing white, and dark-cloaked hardliners marked with the blade-scholar's violet knots. Both groups had followed the Blackroot Road by separate arrogance and arrived at the same inconvenient truth.

"Ah," Kesh said. "Diplomacy."

The scouts saw the company, saw the corrected cavalry, and made the universal battlefield mistake of assuming anything not on their side should be struck before it spoke.

Arrows flew.

The cavalry charged.

Not at Mara.

Past her.

Hooves hammered water into white spray. Lances dipped, not to kill but to break formation. The first rank of Lumenorath scouts collapsed as horses split their reflections from their feet. Dark-elf hardliners tried to invoke emergency passage seals; the salt flat answered by showing their signatures on earlier sealed losses. One man dropped his sword and ran. Another kept shouting law until a rider named Imra Dass knocked him into a pool deep enough to silence him without drowning.

"Move!" Caldus said.

The company ran again, this time behind a wall of corrected dead.

Mara and Saelith half-carried Caldus between them despite his offended attempts to pretend a spear through the arm was a logistical inconvenience. Tavi's root-hound limped at their heels, barking sparks whenever reflections tried to reform near them. Brakka carried the ledger case under one arm and Kesh under the other after he slipped on salt and declared gravity a monarchist plot.

"Put me down," Kesh said.

"No."

"I am being transported without contract."

"Good."

Ilyr and Maelin ran together, each keeping one hand on the other's sleeve whenever the glare tried to separate them. Edrin and Sava moved in the strange tireless way of the dead, crossing water without ripple. Behind them, the cavalry broke both pursuer bands apart and then wheeled back toward the company with alarming speed.

"Are they still helping?" Tavi asked.

"Define helping," Kesh said from under Brakka's arm.

The captain with the broken nose rode beside Mara's reflection, not her body. "Correction filed. Toll remains."

Mara's lungs burned. "What toll?"

"Look."

"That seems to be the thing we are not supposed to do."

"Look truly."

She looked down.

The water no longer showed riders. It showed the war above and behind them: Lumenorath hymn wagons crossing under-roads, Khar Veyl war knots sealing canal gates, lower-canal evacuees moving in narrow files through pumps and cisterns. She saw Vaura arguing with the blade-scholar in the Umbral Seat while Velra slammed a wrench onto an ancient seal desk. She saw Serathiel standing before a white-root vanguard and raising his hands not like a priest but like a man conducting an execution politely. She saw the dragon-moon far below all of it, an immense pale curve under stone, sleeping with a closed eye the size of a city square.

Then the vision shifted.

She saw a courthouse.

Every morning, a bell rang.

Every morning, a sentence was read.

Arveth of Orrowen, convicted under emergency continuance, death deferred until witness exhaustion.

Every morning, the sentence killed him again because the court could not admit the file was wrong.

Mara stumbled so hard Saelith nearly fell with her.

"What did you see?" Saelith asked.

"Arveth."

The ledger case under Brakka's arm clicked open by itself.

From inside came Arveth's voice, dry as old paper and furious as spring water under ice. "I object to the accuracy, grammar, jurisdiction, and moral hygiene of that sentence."

Kesh twisted in Brakka's grip. "Is the dead barrister in the box?"

"Not entirely," Ilyr said, staring at the ledger. "His copied filings are reacting to the court record."

"Naturally. Why have one haunted legal document when you can encourage correspondence?"

They reached the black stone ridge.

The moment Mara's boots hit dry rock, the salt flat behind them lost half its brightness. The corrected cavalry slowed at the water's edge. They did not cross. Their horses stood fetlock-deep in reflection, breathing steam that smelled like sea caves.

Captain Ruv Ossian saluted with his lance.

"Road paid," he said. "Court waits."

"Can you come with us?" Mara asked.

"We are outer memory. We hold the flat until correction travels. Orrowen does not move all at once."

"Nothing good does," Caldus said, then leaned dangerously.

Saelith and Mara lowered him onto a rock before he could fall with dignity and hurt himself further. Saelith cut away the torn sleeve. The wound was ugly but clean, glass-salt edges gleaming in the meat of his arm. Caldus set his jaw while she worked.

"You should have pulled back," Mara said.

"Yes."

"That is all?"

"I am trying honesty. It is briefer than justification."

She wanted to be angry. Anger would have been easier than gratitude. Instead she pressed a cloth above the wound while Saelith's hands glowed red-gold in the low light. Caldus watched Mara, not Saelith, perhaps because pain needed a place to stand.

"You named me," he said.

"You were bleeding in my direction."

"You named what I was and what I chose."

Mara looked away first. "Someone should."

Across the ridge, Tavi had found old brass studs set into the stone. She was on hands and knees, root-hound beside her, fear forgotten under the stronger drug of a machine being rude.

"These are alignment pins," she called. "Gnomish, but pre-Brassroot. No, not pre. Adjacent. Argumentative cousin-work."

"Should I know what that means?" Kesh asked.

"It means there is an engine beyond this ridge, and whoever built it wanted the salt flat to feed witness-pressure into something below."

Maelin joined her, face shadowed. "A regulator?"

Tavi scraped salt from a symbol with her knife. "A glass regulator, maybe. Cinder-tempered. Designed to harden unstable memory into fixed channels."

Sava made a sound like paper tearing.

Edrin translated the dead silence. "Engines that fix memory can also command it."

The words settled over them heavier than exhaustion.

Behind them, corrected cavalry stood in the shining flat.

Ahead, beyond the ridge, a low amber light pulsed at the mouth of a carved tunnel. It was beautiful, steady, precise.

Tavi's face had gone pale.

"That is guild work," she said.

"Your guild?" Mara asked.

"No." Tavi swallowed. "Worse. My guild's bedtime story. The Glass Engine every engine child is told never existed because if it did, someone would have used it."

The root-hound whined.

From the tunnel below came the sound of liquid glass beginning to move.
""",
    21: r"""## Chapter 21: The Glass Engine

The tunnel beyond the salt ridge was tiled in brass prayers.

Tavi hated that immediately.

Prayers belonged to people who had done the hard work of wanting something beyond themselves. Brass belonged to people who had done the harder work of making gears behave. Combining them had always seemed to her like a confession that the maker wanted obedience and applause at the same time.

The tiles curved along the tunnel walls in interlocking plates, each etched with gnomish script so fine Mara could not read it while walking. Tavi could. Her lips moved as she passed them, and with every line her expression worsened.

"What does it say?" Mara asked.

"Depends whether you translate charitably or accurately."

"Accurately."

"Function is mercy when variance is pain."

Kesh groaned. "I have stolen from temples with better slogans."

"It repeats," Tavi said. "Different equations, same disease."

The air warmed as they descended. Not fire-warm. Kiln-warm. Workshop-warm. The smell of mineral oil, hot metal, wet stone, and something sweet underneath like sugar left too long in a pan. Amber light pulsed from below in exact intervals. The root-hound counted them with twitching ears: one, two, three, pause. One, two, three, pause.

Caldus walked because refusing help was one of the last stupid powers left to wounded men. Saelith had sealed the worst of the spear cut, but his arm hung in a sling made from Mara's spare scarf and a strip of Brakka's pack leather. He had tried to object to the scarf.

Mara had stared at him until he discovered respect for textile strategy.

They reached a gallery overlooking the engine.

For once, no one spoke.

The Glass Engine filled a cavern the size of Ashgate's lower foundry and Lumenorath's judgment court combined. It rose from a black chasm in seven stacked rings, each ring turning in a different direction around a central column of clear molten glass. The glass did not burn red. It glowed with captured colors: funeral blue, dawn gold, root green, royal black, the impossible pale of the dragon-moon glimpsed in water. Brass ribs arched from wall to engine. Cables thicker than bridges fed into gearhouses. Glass channels ran along the floor in branching veins, carrying slow, luminous streams toward sealed doors.

Every surface was engraved.

Names, Mara realized.

Not all names. Not enough. But thousands of them, written in brass, cut into glass, stamped on cinder-tempered plates. Some had been crossed out and replaced with offices. Some had been corrected and crossed out again. Some were only scratches where a name had fought being erased.

Tavi gripped the railing so hard her knuckles whitened.

"This is not supposed to be possible," she said.

"That phrase has been having a busy year," Kesh said.

"No. Listen. A regulator stabilizes unstable output. A memory engine can index witness, maybe store impressions if you do not mind being unethical and dead inside. A cinder regulator can smooth resonance. But this..." She swallowed. "This is all of them married badly. It does not store memory. It decides which version is stable enough to persist."

Ilyr's voice was flat. "A machine for official history."

"A machine for making official history physically true."

The engine turned.

On the far side of the cavern, figures moved along lower walkways. Gnomes, mostly, or what remained of them in Orrowen memory: small bodies in heat masks and leather aprons, some living, some translucent, some neither. Their hands were inked with guild marks that glowed whenever the engine pulsed. A few dark-elf hardliners stood among them with drawn blades. Two light-elf scouts in torn white armor were bound near a glass channel, not prisoners of mercy so much as ingredients waiting for a recipe.

At the central console stood a gnome woman with silver hair braided in nine loops. She wore an old Brassroot torque around her neck and a newer violet knot at her shoulder.

Tavi made a sound Mara had never heard from her. Not fear. Betrayal with teeth.

"Master Quen."

The woman below looked up.

Across the roaring engine, her eyes found Tavi.

"Apprentice Tavira," she called. Her voice carried through brass speaking tubes and arrived at the gallery as if she stood beside them. "You are late."

Tavi's jaw worked. "You are dead."

"Professionally disputed."

"I saw your memorial plate."

"Yes. Very tasteful. I approved the font."

Kesh leaned toward Mara. "I understand why Tavi became like this."

"Do not," Tavi snapped.

Master Quen smiled. "Good. Still reactive. Still allergic to awe. I told Brassroot they trained the fear out of you too early and the suspicion in too deep."

"You built the Glass Engine."

"I completed what frightened committees abandoned."

"You built a memory tyrant."

"I built a splint for a broken world."

At the lower channel, one of the bound light-elf scouts struggled. A hardliner struck him with a blade hilt. The scout's blood fell into a glass gutter and flashed white. The engine answered by turning faster.

Mara's cinder cage burned cold.

Saelith stepped to the rail. "Those are Serathiel's scouts."

"They crossed into engine precinct with hostile writs," Quen said. "Their witness-pressure is therefore admissible."

"They are people," Saelith said.

"All components were people at some point."

The sentence dropped into the cavern like a tool placed carefully on a bench.

Tavi went very quiet.

Mara had learned that Tavi's quiet was more dangerous than Tavi's shouting. The shouting was steam release. The quiet was calculation sharpening into decision.

Brakka set one hand on the little gnome's shoulder, absurdly gentle for someone who could break a horse-sized glass construct. "Plain vow?"

Tavi did not look away from Quen. "No one gets fed to the machine."

"Good vow."

"Also," Tavi said, "I am going to be extremely unpleasant."

"Better vow."

The root-hound barked once. Its cracked eye projected a trembling map into the air: seven rings, twelve overflow channels, three emergency valves, one central regulator, and a red pulse moving from lower intake toward the outer roads. The engine was not merely running. It was flooding.

"Liquid glass," Tavi said. "If those channels fill, the road behind us seals. The salt flat, the fungal forest, maybe the lower canal routes. Everything becomes stable."

"Stable meaning trapped?" Mara asked.

"Stable meaning unable to change. Which is a kind of trapped engineers should be ashamed to invent."

Maelin looked from the projection to the lower console. "Why now?"

Ilyr answered before Tavi could. "Because both armies are entering the under-roads. The engine can choose the clean version of the war before witnesses complicate it."

Below, Master Quen lifted a brass key as long as her forearm. "Not choose. Harmonize. Lumenorath brings cleansing pressure. Khar Veyl brings emergency authority. Orrowen brings excessive continuity. Your little company brings mixed witness. If left unregulated, all four will tear the dragon-moon seal open."

"And your answer is to freeze the world into the version you prefer?" Saelith said.

"My answer is to prevent the worse answer."

Mara heard the deep stillness under the engine, Vorrakai's attention wrapped around the turning rings like a hand around a cup.

Not Quen alone, then.

No tyrant ever lacked a philosophy, and no machine that called itself mercy lacked a mouth whispering where to aim.

"We need the valves," Tavi said. "Three of them. Red handles, lower east, midwest gantry, top ring. Pull in sequence, not together. Together vents glass into the gallery and we all become cautionary sculpture."

"Who goes where?" Caldus asked.

"You sit down."

"No."

"Your arm has a hole."

"I have another."

"You are making me miss when you were emotionally repressed in silence."

Mara cut in before Caldus tried to win a medical argument through posture. "Brakka and Kesh to lower east. Saelith with the bound scouts. Ilyr and Maelin get the upper access if you can pass the seals. Tavi and I go to the central console."

"Absolutely not," Tavi said.

"Which part?"

"The part where you put your cinder blood near a machine designed to rewrite witness."

"That sounds like exactly where I should be."

"It sounds like exactly where you will be useful, which is how every horrible device in this trilogy tries to flirt with you."

Mara blinked.

Kesh pointed at Tavi. "That was rude, accurate, and structurally important."

Tavi's face softened just enough to hurt. "Mara."

"I know."

"Do you?"

No. Not fully. That was the terror. Mara knew furnaces, hunger, roads, ash, names. She knew what it felt like when power reached for her and offered to make decision unnecessary. But she did not know engines the way Tavi did. She did not know how beautiful control looked from the inside to someone who had spent her life watching chaos kill the poor first.

"I know I need you to tell me when I am being used," Mara said.

Tavi exhaled. "Infuriatingly good answer."

They moved.

Action inside the Glass Engine had no clean battle line. It was all height, heat, glare, and bad footing. Brakka and Kesh took the lower stairs at a run. A hardliner tried to stop Brakka with a blade and discovered that political conviction did not improve mass. Kesh slid under a glass pipe, cut a purse, threw the purse at another guard's face, and used the distraction to steal the guard's key.

"Why did you steal the purse?" Brakka shouted.

"Reflex!"

Saelith crossed a narrow channel toward the bound scouts. White fire gathered in her palms, then died. She looked down at the red fungal bell against her throat and chose the softer light instead. The first scout flinched from her.

"I am not here to cleanse you," she said.

"You wear exile colors," he spat.

"I earned them."

She cut his bonds.

Above, Ilyr and Maelin reached a seal bridge marked with House Noct-Vey authority. The bridge refused to lower. The engine's brass voice spoke in court language.

AUTHORIZED LINE HOLDER REQUIRED.

Maelin looked at Ilyr. "It wants me retained."

"No."

"It may not accept partial release."

"Then we argue."

"With a bridge?"

"I have argued with less honest structures."

Ilyr sliced his palm, then offered the blood to the seal and said, "Ilyr Noct-Vey, former house archivist, confesses unauthorized sale, suppression, and correction of under-script names. Maelin Noct-Vey, daughter of the line, is present by her own standing and not as property. House authority is contested."

The bridge hummed.

Maelin added, "Maelin Noct-Vey. Retention subject, partially released by emergency mixed witness. I contest my family's right to use my blood as a key without my consent."

The bridge lowered halfway, grudging as a noble at a public apology.

"Good enough," Ilyr said.

They climbed.

Mara and Tavi descended through a rain of amber sparks toward the central console. Heat pressed against Mara's eyes. Liquid glass surged through the column beside them, not flowing so much as deciding to be elsewhere. Within it she saw images harden and crack: Serathiel crowned in white root, Vaura standing over drowned canals, Arveth's sentence stamped daily, Mara herself at the center of a dead army with no face because the engine had not yet decided what kind of monster would be most efficient.

The console was a half-circle of brass levers, glass keys, and cinder plates. Master Quen stood behind it with both hands on the long key.

Up close, she looked less like a villain than Mara wanted. Small, lined, exhausted. Her silver braids were singed at the ends. Her guild torque had cut sores into her neck. One of her eyes was living brown; the other was glass with cinder light behind it.

"Apprentice," Quen said.

"Do not call me that."

"You keep the wound and reject the title. Sentimental."

"I keep the wound because people like you keep calling scars credentials."

Quen's gaze moved to Mara. "Cinder-singer. You have been improvising with forces my people measured for generations."

"My people died in forces your people measured."

"Yes." Quen's honesty was worse than denial. "And mine died when rulers demanded impossible stability from devices built to delay catastrophe for one more season. Every people in this underworld has learned to be someone else's component."

"So stop building machines that agree with them," Tavi said.

The first valve opened below.

Brakka's roar shook the lower ring. Red light shifted to green along one third of the engine. Liquid glass diverted from an outer channel into a containment basin. The floor lurched. Kesh whooped, either in triumph or because something expensive had broken.

Quen did not look down. "You think breaking it is mercy because you have only lived downstream of failed control."

"I lived downstream of your successes too," Tavi said. "They were not prettier."

The second valve opened halfway up, then jammed.

Ilyr shouted something. Maelin screamed, not in pain but fury. The bridge above them flooded with violet seal light.

The engine began to sing.

Not music. Alignment. A tone that made Mara's bones want to arrange themselves in straight lines. Around the chamber, gnome workers staggered. The bound scouts Saelith had freed clapped hands over their ears. Hardliners dropped to their knees with blissful terror on their faces. The root-hound howled and projected warnings in frantic red.

STABILITY CASCADE.

MEMORY VARIANCE EXCEEDS TOLERANCE.

CORRECTION BY FORCE IMMINENT.

Mara's cinder cage snapped open.

No hand touched it.

The cinder inside lifted.

It was small. Ridiculously small for the weight everyone put on it. A black-red flake of dead dragon memory, no bigger than a thumbnail, spinning in air before the Glass Engine like an ember deciding whether to become a star.

The engine recognized it.

Every ring turned toward Mara.

Master Quen's expression changed. Not triumph. Hunger and grief, welded.

"There," she whispered. "A living witness-node. With you, the engine can harmonize without mass loss."

"Mass loss," Kesh shouted from below, "means murder for people with rulers' dictionaries!"

Tavi stepped between Mara and the cinder.

"You touch her and I will invent a new category of explosion," she said.

"You could run it," Quen said to her.

The words landed with surgical cruelty.

Tavi froze.

Quen's voice softened. "You see the flaws. I know you do. Brassroot never understood elegance. The old councils wanted obedience, not precision. I was alone too long. But you could correct it. Your root-hound is already modeling alternate valve logic. You could make the engine less cruel."

Tavi looked at the console.

Mara saw the temptation, and because she loved Tavi, she did not insult it by pretending it was small.

Tavi could improve it. Of course she could. She could make the Glass Engine smarter, less wasteful, less openly monstrous. She could reduce the number of people it devoured before it made history lie flat. Engineers were always being asked to turn atrocities into systems with acceptable failure rates. Sometimes the world rewarded them for it.

"Tavi," Mara said.

"I know."

"I was not warning."

Tavi did not look at her. "Then what?"

"Witnessing."

The second valve opened.

High above, Maelin had shoved her own arm into the seal bridge mechanism to hold it apart while Ilyr cut the jammed chain. Blood ran down her sleeve, but she laughed through her teeth like someone discovering that pain chosen for herself hurt differently than pain assigned by a house.

"Top ring!" Tavi shouted.

The last valve was above the central column, reachable only by a maintenance ladder that ran beside molten glass. The root-hound bolted before anyone ordered it, scrambling up the ladder with its broken leg sparking. Tavi swore and ran after it.

Mara followed.

Master Quen turned the long key.

The central column burst.

Liquid glass rose around the ladder in a clear, burning tide. It did not splash. It climbed with intent, sealing rungs behind them. Mara felt heat lick the soles of her boots. Tavi was faster, smaller, furious. The root-hound reached the top platform and bit the red valve handle.

It could not turn it.

"Hold on!" Tavi shouted.

The hound held.

Glass closed over its hind legs.

Tavi made a sound like something tearing.

Mara reached the platform behind her. The heat was unbearable now, pressing tears from her eyes, filling her mouth with the taste of scorched sugar and metal. The cinder hovered below, tethered to the engine by strands of red light.

Vorrakai spoke.

For the first time, the voice was almost a voice.

No more running.

It was gentle.

No more choosing who burns.

The words did not come through her ears. They arrived in the place exhaustion had carved in her soul.

Let the engine finish. Let the glass hold. Let history stop hurting you.

Mara's fingers slipped on the railing.

For one breath she wanted it with a longing so raw she hated herself for having it. No more carrying names. No more being asked to choose between people who all had reasons. No more turning every road into witness and every victory into another door opening on worse need.

Then she saw Tavi with both hands on the valve, sobbing with rage because the root-hound was being sealed alive in glass and she still had to pull.

Mara put her hands over Tavi's.

"Not alone," she said.

Together they turned the valve.

The top ring opened.

The engine screamed.

Glass that had been climbing toward them reversed in a luminous waterfall. Channels burst. Brass ribs buckled. Below, Quen shouted commands that the engine no longer recognized as superior to physics. Saelith dragged the last freed scout behind a shield of red-gold light. Brakka lifted a gnome worker bodily from an overflow trough. Kesh cut the central pulley line, not because he understood it but because it looked expensive and central and sometimes instinct was philosophy.

The root-hound's body was half encased in cooling glass.

Tavi dropped to her knees beside it.

"No, no, no, no."

Its cracked eye flickered. A projection stuttered against her chest: not a map, not a warning. A memory. Tavi at twelve, hair wild, hands ink-stained, sleeping under a workbench while a younger Quen draped a coat over her. Tavi at fourteen throwing a wrench at a boy who called her scholarship charity. Tavi at sixteen building the first illegal root-hound from guild scraps and loneliness. Quen watching from a doorway, proud and already choosing the machine over the girl.

Then the hound projected one final diagram.

Not of the engine.

Of a road.

Glass fractures spread from the top platform through the floor, forming a path across the chasm toward a sealed Orrowen gate.

Tavi pressed her forehead to the hound's brass skull. "You ridiculous loyal machine."

Its tail clicked once.

The eye went dark.

Mara wanted to say something. There were no words clean enough. She put a hand on Tavi's back and left it there. Tavi leaned into it for one second, no more, then stood with grief burning every childish thing out of her face.

Below, Master Quen had survived.

She stood amid ruined brass, one hand on the console, glass eye cracked. The engine rings still turned, slower now, wounded rather than dead. Around her, gnome workers were fleeing through side doors. Hardliners lay bound or unconscious. The freed light-elf scouts huddled near Saelith, too shocked to decide whether their rescuer was enemy or apostate.

"You have doomed the seal," Quen said.

Tavi descended the ladder with the root-hound's cracked eye in her fist.

"No," she said. "I have doomed your ownership of the problem."

"Without regulation, witness will cascade. Armies will bring incompatible truths into Orrowen. The dragon-moon will wake."

"Maybe," Tavi said.

Quen flinched as if maybe were obscenity.

"Maybe is where people live," Tavi continued. "You tried to engineer it out because you could not bear a world that might still hurt after you saved it."

For the first time, Quen looked old.

"I buried too many apprentices."

"So you built a tomb big enough for everyone."

Mara reached the lower floor as the engine settled into a broken pulse. The cinder had returned to her cage, though the latch was melted. She closed it with shaking fingers and a strip of wire Tavi handed her without looking.

Caldus, pale but upright, stood guard over the captured hardliners. "The outer channels?"

"Diverted," Tavi said. "Not sealed. The road behind us remains open, though rude."

"The road ahead?" Ilyr asked.

Tavi looked toward the fracture path the root-hound had shown them.

The glass had cooled into a bridge across the chasm. It was clear as water and threaded with red cracks. Beneath it, far below, something vast and pale curved under the earth.

Not a moon in the sky.

A moon buried under the world.

Mara felt it before she understood what she saw. The dragon-moon's surface was not stone. It was scale, bone, memory, sleep. Its closed eye lay beyond the reach of the ruined engine, and yet every cinder in the cavern tilted toward it.

The bridge led to a gate carved with civic chains, troll bridge marks, light-elf healing script, dark-elf emergency law, gnome measurements, human ash tallies, and small goblin route signs tucked into the margins where no official engraver had bothered to look. Above the gate, Orrowen had written its own name in letters that hurt to read because each one contained too many voices.

Edrin Vale bowed his head.

Sava Rennet straightened her stained clerk's cuffs.

"The courthouse comes first," she said. "Always paperwork before apocalypse."

Kesh wiped blood from his cheek. "Finally, a civilization with priorities."

Tavi walked to the bridge and knelt. She set the root-hound's cracked eye into a notch between two glass ribs. The bridge lit from within, accepting the piece as toll, key, and memorial.

"I am sorry," Mara said.

Tavi did not cry. Not then. "Do not make it noble."

"I won't."

"It was a machine. I made it. It followed me because I taught it to. It died because I asked too much."

"It chose the road."

Tavi looked up sharply.

Mara held her gaze. "You taught it choice too."

For a moment Tavi's mouth trembled. Then she nodded once, very small, and stood.

Behind them, Quen laughed.

Not triumph. Not madness either. Something closer to despair finding its old rhythm.

"You think broken engines stop being engines?" she asked. "The Glass Engine will keep trying to stabilize. Every witness you bring into Orrowen will feed the moon. Every correction will be pressure. Every name will be heat."

Mara turned back.

"Then we will be careful."

"Careful is not enough."

"No," Mara said. "It isn't."

That was the answer no ruler liked, no engineer trusted, no saint could survive admitting. Careful was not enough. Love was not enough. Truth was not enough. But the lack of enough did not excuse surrender to machines, crowns, courts, or merciful graves.

She stepped onto the glass bridge.

It held.

One by one, the company followed: Caldus with his bound arm, Saelith with the rescued scouts walking uncertainly behind her, Ilyr and Maelin carrying the ledger between them, Brakka with her maul resting on one shoulder like a portable law, Kesh pretending not to limp, Edrin and Sava bringing the dead record home, Tavi last with the root-hound's empty collar wrapped around her wrist.

The ruined engine pulsed behind them.

Ahead, the Orrowen gate opened without being touched.

The sound was not stone scraping stone.

It was a bell ringing in a courthouse that had never learned the trial was over.

Arveth's voice rose from the ledger case, sharper now, nearer.

"Oh," he said. "They are still doing this."

Mara looked through the opening at a city of bone-lit canals, black civic towers, and streets paved in dragon-scale. Ghost lamps burned in windows. Dead citizens moved behind glass. Somewhere deep in that impossible city, a court reissued the same death sentence every morning because no one had forced it to read the correction.

She thought of Ashgate. Harrowmere. Lumenorath. Khar Veyl. Every place that had called an old wrong necessary because the paperwork had become architecture.

"Then we make them stop," Mara said.

No one called her saint.

No one called her weapon.

They were all too tired, too hurt, too honest for that.

They crossed into Orrowen as a company of witnesses, carrying broken machines, open debts, corrected cavalry, stolen ledgers, and a grief so large it had begun to sound like mercy from below.
""",
}


DEEPENING: dict[int, str] = {
    21: r"""The gate did not lead directly into a street.

It led into an argument about whether a street had ever been legally closed.

Mara discovered this when the threshold opened onto a vast entry hall paved in black dragon-scale and tiled with notices. The notices hung from chains, drifted in waterless air, or glowed under glass in the floor. Some were written in Orrowen civic script, some in dark-elf legal marks, some in Lumenorath healing shorthand, some in gnomish adjustment symbols, some in human tally cuts so old they had stopped pretending to be numbers. They all contradicted one another.

NO PASSAGE UNDER EMERGENCY AUTHORITY.

CIVIC ACCESS PRESERVED PENDING REVIEW.

REVIEW POSTPONED UNTIL HOSTILITY CEASES.

HOSTILITY CEASED IN YEAR 0 OF THE DROWNING.

HOSTILITY NOT RECOGNIZED AS CEASED BY ELVEN OVERSIGHT.

OVERSIGHT EXPIRED.

EXPIRATION UNACKNOWLEDGED.

Someone had written beneath the last notice in small, furious letters: ACKNOWLEDGE IT, YOU COWARDS.

Kesh stared at that line with real affection. "I have never felt so welcomed by architecture."

The hall's ceiling was lost in blue shadow. Balconies circled it, crowded with ghost-lamps and watchful figures. Some figures were translucent. Some were only bones clothed in civic robes, tendons replaced by silver writing. Some looked almost living until they moved and the air remembered not to move with them. A row of children stood on one balcony, each holding a slate. An old woman with an ink-black veil corrected their posture whenever they leaned too far over the rail.

Dead city, Mara had expected.

Not this.

Not order.

Not boredom.

Not a clerk with half his jaw missing stepping forward, adjusting spectacles that had no glass left in them, and saying, "Arrivals state purpose, lineage if relevant, standing if contested, and whether you carry active fire, plague, siege writ, royal debt, private god, unsupervised prophecy, or unfiled dragon matter."

No one answered at once.

The clerk sighed. "Travel parties are always less prepared than invasions."

Sava Rennet stepped forward and gave him a look so severe it should have required a permit. "Assistant Registrar Othel."

The clerk blinked. "Senior Copyist Rennet?"

"Promoted posthumously, apparently."

"Congratulations."

"Do not sound happy. I have been unpaid for centuries."

Edrin Vale bowed to the clerk. "Citizen Edrin Vale. Return under mixed witness. Standing contested by old emergency authority, repaired provisionally by drowned archive filing."

The hall changed.

Not visibly at first. The change was in attention. Ghost-lamps brightened. The balcony children stopped fidgeting. On the walls, notices turned toward Edrin as if paper could have ears.

Mara felt the dragon-scale paving warm under her boots.

The clerk's dead fingers moved over an invisible ledger. "Return under mixed witness requires committee."

"No," Sava said.

"Senior Copyist, the law says -"

"The law says committee review if the returning citizen has no active external witness. He has nine, plus two unwilling scouts, one contested house daughter, one grieving engineer, one bridge-bound troll, and a goblin with open fever-road debt."

Kesh raised a finger. "Open debt should remain less public."

"Pay it faster."

"Yes, ma'am."

The clerk peered at Mara. "And the cinder-singer?"

The hall went very still.

Mara had been called many things since leaving Ashgate. Most had felt like someone trying to fit a handle to her. Cinder-singer was close enough to truth to hurt and broad enough to be dangerous. She set her injured hand over the cage at her hip.

"Mara Venn," she said. "Human. Ashgate. Former runner. No lineage relevant."

The paving under her feet warmed again, this time almost approving.

"Standing?" the clerk asked.

The old reflex rose: none, unless someone grants it. The answer a poor girl learned before she learned letters. She had spent her life standing where she was useful, kneeling where she was told, ducking where a blow might land. Standing was what people with seals and names and doors decided you had.

Saelith shifted beside her, not touching.

Caldus, pale from blood loss, said nothing. That mattered. He knew when an answer had to be hers.

Mara lifted her chin. "Self-filed. Contested by everyone who finds it inconvenient."

The clerk considered this.

Then he stamped the air.

The sound rang through the hall.

PROVISIONALLY ACCEPTED appeared in blue fire above Mara's head, then dissolved before she could decide whether to be relieved or insulted.

Tavi pointed at it. "Can I get one of those for engineering disputes?"

"Only if you survive appeal," the clerk said.

"I have been doing that professionally."

The rescued Lumenorath scouts came last. There were three of them: a woman with a shaved head and burn scars along one cheek, a young man whose hands would not stop shaking, and an older standard-bearer whose white cloak had been torn to strips in the engine. They had followed Saelith through the gate because she had cut their bonds and because the road behind them contained a ruined machine, corrected cavalry, hostile hardliners, and all the other persuasive features of catastrophe.

Now, facing Orrowen citizens, their terror sharpened into doctrine.

"We cannot enter," the standard-bearer said. "The dead below are unclean."

The balcony children leaned farther over the rail.

The old woman in the ink veil smacked one slate with her pointer.

Saelith closed her eyes.

Mara braced for anger, but Saelith did not give the hall anger. She walked to the scouts and unfastened the red fungal bell from her throat. Its water-filled vial glowed faintly in her palm.

"I was taught the same sentence," Saelith said. "I taught it to others. I put a clean word on a dirty fear and called the fear holy. That is on my record. If you need someone to despise while you learn to stand here, despise me first."

The young scout stared at her. "You betray the Bough."

"No," Saelith said. "I am trying to find where its root was before men like Serathiel taught it to strangle."

The shaved-headed scout looked at the vial. "What is that?"

"A forbidden line from Matriarch Aurenne. If memory is the wound, then we must learn not to cut it out."

The standard-bearer flinched. He knew the name. Of course he did. Doctrine always kept its founders as statues so no one had to hear them speak.

On the nearest balcony, one of the dead children wrote the sentence on a slate and showed it to the others.

The hall's notices shifted again.

FOREIGN RELIGIOUS CORRECTION FILED.

REVIEW PENDING.

Mara almost laughed. It came out too tired to be laughter, but close enough that Kesh looked encouraged.

"I adore this city," he said. "It weaponizes minutes."

"You adore anything that can delay consequence," Caldus said.

"And yet consequence keeps following me. A tragic romance."

The banter thinned when Kesh's wrist lit.

The gray coin-moth mark rose under his skin, wings opening. Three sparks crawled from it and hovered over the floor: Reedmere, Tallow Ford, Neth-by-the-Salt, each written in road-script and fever tally. The Orrowen hall noticed debt the way sharks noticed blood.

Assistant Registrar Othel bent closer. "Open road obligation. Nonlocal. Voluntary?"

Kesh's smile did not arrive. "Voluntary in the sense that the alternative was letting villages die behind paperwork."

"Payment schedule?"

"Optimistic."

"Collateral?"

"My charm."

"Insufficient."

Brakka snorted.

Kesh shot her a wounded look. "Betrayal from a bridge authority."

The clerk lifted his stamp.

Mara stepped between them before she knew she would. "His debt remains open because the roads remain open. If you close it here, people behind us lose passage."

"You speak as guarantor?"

Caldus stiffened. "Mara."

She knew. She knew too well. Every debt wanted a body. Every road wanted blood to prove someone meant it. Kesh looked at her with naked alarm, all jokes stripped away.

"Do not," he said.

Mara did not take the debt. That was the old version of heroism, the story trap where one person became noble enough to be consumed and everyone else clapped with clean hands. She had walked too far with too many ledgers to romanticize being spent.

"No," she said. "I speak as witness that no debt serving evacuation may be converted into ownership without mixed review."

Assistant Registrar Othel's stamp paused.

Sava smiled. It was a small, terrifying expression.

"Correct," she said. "Emergency road obligations fall under bridge law when civilian movement is at stake."

Brakka set her maul on the floor. The impact rolled through the hall like thunder learning grammar. "Bridge law hears."

The stamp changed color from black to green.

OPEN, NONTRANSFERABLE, REVIEW REQUIRED appeared over Kesh's wrist. The coin moth mark folded its wings and sank back under his skin.

Kesh looked at Mara, then away. "I had a beautiful speech about not needing rescue."

"Save it," Mara said.

"For when?"

"When it is true."

He barked a laugh, but his eyes were wet.

Past the arrival hall, Orrowen opened in pieces.

The city was not underground in the simple sense. It had sky, if sky meant a vault of dark stone threaded with rivers of blue fire. It had weather, if weather meant drifting ash that never touched the ground and bells of cold mist rising from canals. Streets ran in terraces along black water. Bridges crossed at angles that made Tavi mutter appreciatively despite grief. Towers of bone-white civic stone leaned toward one another as if exchanging gossip. In windows, ghost-lamps burned beside flower boxes full of pale fungi. A vendor with no visible skin argued with a customer over ink pears. A patrol of skeletal officers stopped to let a group of translucent laundry workers cross.

Life, Mara thought, and corrected herself.

Not life.

Continuance.

That was not lesser. It was stranger, more stubborn, and perhaps more honest.

Everywhere, the city's old emergency showed. Chains across alleys. Seals on doors. Public fountains dry because some long-dead command had diverted water to war engines that no longer stood. Yet everywhere, too, Orrowen had pushed back against its own paperwork. Citizens had painted names over evacuation numbers. Children had chalked jokes on tribunal steps. Someone had tied ribbons around a gallows and turned it into a market stall for lamp oil.

At the first canal bridge, Tavi stopped.

Mara stopped with her.

Below them, black water reflected no faces at all.

"It should show something," Tavi said.

"Maybe Orrowen got tired of mirrors."

Tavi held the root-hound's empty collar in both hands. Her jaw was hard, but grief had begun to find the cracks in it. "I keep thinking I should have built it less loyal."

"Would that have saved it?"

"No."

"Would it have made you hurt less?"

Tavi considered lying. The city, with its stamps and witnesses and merciless patience, seemed to discourage the habit.

"Maybe."

Mara leaned beside her on the bridge rail. The others gave them space, except not too much. That was the company now: distance enough for dignity, nearness enough for catching.

"In Ashgate," Mara said, "we used to name the carts."

Tavi blinked. "Carts."

"Ore carts. Ash carts. Broken-wheeled things that tried to kill us on slopes. Joryn said naming made workers careless because you mourned tools when they broke. Then he named the worst one Old Bite because it took his thumbnail."

Tavi's mouth twitched despite herself.

"I thought it was stupid," Mara said. "Then Old Bite cracked an axle in the rain, and half the line cried over a cart that had bruised all of us. Joryn said grief was not proof we had mistaken the cart for a person. It was proof our hands had spent years telling the world it mattered enough to fix."

Tavi looked down at the collar.

"That is a very rude thing to say to someone trying to be rational."

"I learned from you."

The bell rang.

It came from deeper in the city. Not loud, but every citizen stopped. The vendor put down an ink pear. The patrol halted mid-step. The balcony children in the arrival hall, far behind them now, fell silent as if the sound had reached backward.

Assistant Registrar Othel bowed his head.

Sava's face went cold.

Arveth's ledger case trembled in Ilyr's hands.

The bell rang again.

A voice followed, carried through civic speaking tubes, courthouse stones, and the memory of a city that refused to forget the wrong thing.

Arveth of Orrowen, convicted under emergency continuance.

Death deferred until witness exhaustion.

Sentence reissued.

The city resumed moving.

Not because the sentence did not matter.

Because it had happened every day for so long that even outrage had learned a schedule.

Mara's hands closed around the bridge rail.

Vorrakai's grief moved below the city, vast and gentle, offering an end to bells, ledgers, wounds, choices, the daily obscenity of a court that could not stop killing a man who had already given his last death to truth.

Mara felt the offer and hated how well it understood her.

Saelith came to her side. Caldus stood behind her. Kesh, Tavi, Brakka, Ilyr, Maelin, Edrin, Sava, and the uncertain scouts gathered without command.

This was how the company answered temptation now.

Not by being fearless.

By making sure no one was alone with the thing that knew their weakest name.

Sava pointed down the canal, toward a courthouse whose windows burned with pale procedural light.

"That way," she said.

Mara pushed away from the rail.

The city watched them go.

This time, when the bell began its third toll, Mara did not flinch.

"File us," she said to the air, to the road, to Orrowen, to every old machine and court and god beneath the world that thought exhaustion was consent. "We are appearing." """,
}


def replace_chapters(text: str) -> str:
    pattern = re.compile(r"(?m)^## Chapter (\d+): .*$")
    matches = list(pattern.finditer(text))
    by_no = {int(m.group(1)): m for m in matches}
    for chapter_no in sorted(CHAPTERS.keys(), reverse=True):
        match = by_no[chapter_no]
        start = match.start()
        later = [m.start() for m in matches if m.start() > start]
        end = min(later) if later else len(text)
        replacement = CHAPTERS[chapter_no].strip()
        if chapter_no in DEEPENING:
            replacement += "\n\n" + DEEPENING[chapter_no].strip()
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
        'current_form: "full-length draft zero with Book Two chapters 1-21 revised in pass 01"',
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
    print(f"Book Two chapters 19-21 revised. Word count: {total}")


if __name__ == "__main__":
    main()
