#!/usr/bin/env python3
"""Revision pass 01o for Book Three chapters 33-36.

Replaces the old covenant lock and first aftermath scaffold with bespoke prose:
the covenant break, the morning after magic, answerable oaths, and Saelith's
repair of beauty without silence.
"""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "output" / "book-03-the-dragon-that-dreamed-death"
MANUSCRIPT = BOOK / "manuscript.md"
METADATA = BOOK / "metadata.yaml"
SUMMARY = ROOT / "output" / "README.md"

MIN_WORDS = 105_000


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


CHAPTERS: dict[int, str] = {
    33: r"""## Chapter 33: Breaking the Old Covenant

The old lock had no door because it had never expected anyone to enter by consent.

It was a wound made into architecture.

The company fell through the broken Span and landed on a bridge that crossed nothing. The bridge stretched in both directions into a dark so old it had forgotten stars. Its stones were root, scale, oathstone, iron, shadowglass, songwood, brass, road-knot fiber, and pages pressed until they were hard enough to cut skin. Every material remembered the hand that had given it. Every hand had been afraid. Beneath the bridge, where water should have run, moved the first age's unspent terror: burned hills, dead children, starving dragonlings, hidden records, broken routes, forced testimony, crowds begging for certainty, judges accepting loneliness as if loneliness were proof of wisdom.

Mara stood with the soup ladle in one hand and the Kell Ashgate cloth tied tight around the other wrist.

"I feel underdressed," Kesh said.

Tavi looked over the side and immediately stepped back. "That is not a pit. That is a bad decision given depth."

Brakka touched the bridge with her maul head. The old Span answered by humming the first troll footing song, but wrong, each load note stretched until it became obedience.

"This bridge was asked to be a chain," Brakka said.

Caldus knelt beside a link of human iron. It bore a knightly oath in letters so fine Mara could barely read them. Protect the helpless, it said. Under that, in smaller script: define helpless by office. Under that: office subject to crown review. Under that: review suspended during emergency.

He closed his eyes. "That is how they did it."

"Who?" Sava asked.

"Everyone who wanted protection without being answerable to the protected."

The Span shook.

Vorrakai rose at the far end.

He was larger than any dragon Mara had seen, yet less solid than grief should have been. Star-black wings unfolded into the dark. Broken crown shards orbited his horns. Chain links hung from his ribs like jewelry made by a jailer who had learned to call himself physician. His heart glowed through his chest, not red, not gold, but gray-blue, the color of winter light on a river that would drown anyone who mistook stillness for safety.

At his feet lay the first lock.

It was a circle of seven seats carved into the bridge, each one empty, each one marked by a people and a fear: crown, song, record, road, stone, engine, wing. Not thrones. That would have been too honest. They were responsibility chairs. Work chairs. Chairs made for good people who were tired enough to accept final blame if that meant the screaming stopped.

Vorrakai spoke, and the old lock answered as if remembering its maker.

This is where I failed.

Mara did not move.

This is where I can still prevent you from failing worse.

"By closing the world around your grief," Saelith said.

By refusing to let fear invent cages again.

Ilyr opened the copied public record he had carried into the wound. "Fear is already here."

Yes.

"Then it is too late for a lock."

Vorrakai's eyes turned toward him. It was too late before history began. That is what you refuse to learn.

The seven chairs lit.

The living camp's objects, still embedded in the Span, trembled: soup ladle, warning plate, road ribbon, measuring cord, copied record, broken command token, cut throat cord, chalk, scale, kettle lid, boot, bridge stone, gear tooth, death list. The lock pulled at them, trying to sort clutter back into office. Soup became provision. Warning became engineering. Road ribbon became transit. Cord became mercy. Record became archive. Command token became defense. Scale became dragon. Everything useful strained toward category.

"No," Mara said.

The lock ignored her because she had not commanded.

The soup ladle flew from her hand and struck the provision chair. It melted into it, becoming a symbol rather than a tool.

Lora Arlet's voice came through the dark, faint and furious. "If that chair ruins my ladle, someone is paying."

Kesh blinked. "I remain fond of her."

The sound made the provision chair crack.

Not much.

Enough.

Mara understood. The old covenant could absorb solemnity. It could absorb duty. It had been built from duty. What it could not easily absorb was the ordinary owner of an ordinary tool refusing to let usefulness become sacred.

"Keep them themselves," Mara said.

Tavi lunged for the warning plate before it fused into the engine chair. Brass teeth snapped at her sleeve. She slammed the damaged perfect screw through the plate and into the bridge, pinning it sideways. "This warning remains ugly, dated, and subject to revision."

The engine chair hissed.

Kesh grabbed the road ribbon as the road chair tried to pull it straight. "No, no, no. Roads curve. Roads lie. Roads owe apologies." He tied three bad knots in it, then one proper knot around his cracked token. "And roads do not become offices without asking the travelers."

The ribbon snapped green light across the chair.

Brakka and Caldus reached the measuring cord together. The bridge chair and command chair both wanted it. Brakka held one end. Caldus held the other. Between them, the cord tightened around the question the first covenant had never answered: who decides what weight a vow must bear?

"The protected," Caldus said.

The command chair darkened.

"And the span," Brakka added.

The bridge chair cracked.

Saelith caught the cut throat cord as it tried to root into the song chair. The cord wanted to become doctrine. She held it against her bleeding palm and sang a note that began beautiful, then stopped before completion.

Silence followed.

Not imposed.

Chosen.

The song chair split down its carved back.

Ilyr and Sava went for the copied record. The archive chair opened drawers in the air, each one labeled with reasonable delays. Restricted until tempers cool. Sealed until war ends. Deferred until context can be preserved. Redacted to protect the vulnerable, though the vulnerable had not been asked. Ilyr's hand shook.

"A record can kill," he said.

"So can a drawer," Sava said.

She pressed Arveth's closed-by-consent mark against the copied page. The mark did not move. That was its power now. Sava chose anyway.

"Public copy," she said. "Context attached. Harm expected. Review scheduled. No dead advocate trapped in the binding."

The archive chair burned from the inside with root-fire.

Veyrasha's shed-scale trembled last.

It rose toward the wing chair, the largest and most beautiful of the seven. Dragon fear had shaped it. Dragon guilt had polished it. Dragon loneliness had made it almost irresistible. Vorrakai did not reach for it. He did not need to. The chair had been carved for him before he ever sat.

Othrava's voice entered the lock.

No.

The scale fell.

It did not fall into Mara's hand, or Veyrasha's, or any dragon's. It fell between everyone and shattered into seven blue-white sparks, each carrying one word of Othrava's name: Deep-Wing. Keeper. Winter. Rivers. Mother. Three. Storms.

The wing chair convulsed.

Vorrakai's face changed. "Othrava."

Her answer came through the broken Span, through the moon-eye, through a body that had been used too long as mechanism.

Do not speak my name as if naming repairs consent.

He flinched.

Mara had seen him angry. She had seen him tender. She had seen him certain. This flinch belonged to the young judge before the first forced chain, the one who had still known being corrected was possible.

The seven chairs began to collapse.

The lock fought back.

It did not attack with swords. It offered replacements. The chairs reshaped themselves around the company: Caldus as answerable commander, Saelith as living song-law, Ilyr as public record keeper, Kesh as road compact voice, Tavi as safety architect, Brakka as bridge oath, Sava as witness clerk, Mara as traveling witness over them all. Not crowns. Terms. Reviewable offices. Expiring oaths. Everything improved, every danger named.

"This is the better version," Tavi whispered.

"Yes," Mara said.

That was why it hurt.

The old lock had learned. It had listened through every refusal. It no longer offered conquest, sacrifice, obedience, vengeance, stillness, throne. It offered governance. Good governance. The kind that might actually save lives if held by people who had suffered enough to know what not to do.

Vorrakai looked at Mara across the breaking bridge.

You cannot answer disorder with refusal only. Build the lock better. Sit for one generation. One year. One war. One hour.

The word hour nearly took her.

One hour to stabilize the cinders. One hour to prevent cinder engines from exploding in cities. One hour to stop panicked armies outside. One hour to stop hungry roads from closing. One hour to keep dragon grief from becoming fire. One hour was so reasonable that Mara felt her body lean toward the witness chair before thought could catch it.

Sava slapped the register shut.

"Temporary power is where permanent power hides while packing," she said.

Mara breathed.

Kesh raised one hand. "I would embroider that on something if embroidery had not personally wronged me."

The witness chair cracked.

Caldus took the broken command token and placed it on the bridge floor, not in the command chair. "Oath expires when the protected can no longer answer."

Brakka laid the measuring cord beside it. "Span may refuse load."

Saelith laid the cut throat cord. "Song may end."

Ilyr laid the copied record. "Truth may anger before it heals."

Kesh laid the road ribbon. "Road may reroute around its keeper."

Tavi laid the warning plate. "Mechanism may be stopped by the harmed."

Sava laid the blank page. "Witness list intentionally incomplete."

Mara set down the soup ladle.

"People must eat while the law argues," she said.

It was not grand.

The lock had no defense against it.

The seven chairs broke, not into ash but into ordinary pieces: wood, stone, scale, iron, root, wire, paper. Useable. Repairable. No longer holy enough to be untouchable.

Vorrakai screamed.

The bridge beneath them split.

From the crack rose the first forced memory: Halruun in the Span, wing tearing under compelled truth; Eron dead in mud; the iron-guard confessing too late; Othrava landing between crowd and dragon; Vorrakai lifting one claw; the Covenant Span tightening.

This time the memory did not remain memory.

It became present.

Halruun's scream tore through the company. Mara felt her own shoulder rip with an old wound not hers. Caldus fell to one knee. Tavi dropped her tool and clutched her ears. Saelith's voice broke. Ilyr's record pages caught fire. Kesh's route token burned through his palm. Brakka's maul head cracked along an old fault. Sava's register opened to Arveth's mark, but the mark stayed closed because the dead man had chosen rest and would not be dragged back by crisis.

Vorrakai stood in the center of the memory with his claw raised.

Stop me, he said.

Not challenge.

Plea.

Mara understood with sick clarity. The old lock could not break until the first forced chain was answered differently. But the Death-Dream had never allowed them to change history. Witness, not interruption. Record, not rescue. Here, inside the lock, the rule had shifted. To break it, someone had to face the moment where all later stillness began.

The crowd shouted. The mother of Eron demanded truth. Halruun recoiled. Othrava roared warning. Arveth's living predecessor argued with language already failing under panic.

Vorrakai's claw began to fall.

Mara could command the cinders to hold him.

She did not.

She ran to the mother.

Not to the judge. Not the chain. Not the dragon. The mother.

The woman stared at her, grief wild and weapon-ready. Mara had no right to touch her. No right to ask patience. No right to make her dead son part of a lesson.

"Ask what you need to know," Mara said.

"My son is dead."

"Yes."

"I need truth."

"Yes."

"I need someone to pay."

"Yes."

The crowd surged because Mara had not denied them.

"Ask without tearing the answer out," Mara said. "If the truth must be forced from a body, the force becomes part of the truth."

The mother shook. "And if he refuses?"

Halruun trembled beneath the looming Span.

Mara looked at the dragon. "Then his refusal is evidence too. Not proof. Evidence. You keep asking. You keep him from fleeing. You keep the crowd from killing. You name uncertainty and let it hurt without giving it a chain."

"That could fail."

"Yes."

The mother's face collapsed. "I cannot bear yes."

Mara had no answer that would honor Eron by making his mother less broken. So she did the only thing left. She knelt in the mud beside the dead child and said his name.

"Eron."

The lock paused.

The dead child's name had been used as fuel for judgment, riot, fear, law, the Span, Vorrakai's grief. No one in the first memory had been able to let the name simply be a child's name long enough for the next question to enter.

Caldus knelt beside Mara.

"Eron," he said.

Saelith. "Eron."

Ilyr. "Eron."

Kesh. "Eron."

Tavi. "Eron."

Brakka. "Eron."

Sava. "Eron."

Othrava, through the moon-eye and the memory at once, lowered her head until storm milk and river ice filled the air. Eron.

Halruun whispered it last.

Eron.

Vorrakai's claw stopped one breath above the Span.

The mother fell to her knees, not soothed, not healed, but accompanied in the place where certainty had been trying to replace grief.

Arveth's living predecessor, mud on his robe, voice hoarse, spoke into the silence. "Emergency hearing. No compulsion. Dragon contained by perimeter. Crowd disarmed by named witnesses. Iron-guard questioned publicly. Child named before evidence."

Sava made a sound. "He was always irritating."

The memory bent.

Not history. The lock.

The Covenant Span did not tighten.

Instead its links went slack.

Truth came slower. The iron-guard broke under public questioning, not because a machine tore memory from a dragon, but because enough people were forced to stay with uncertainty that his lie had no clean panic left to hide inside. Halruun lived whole in the memory, though history did not change. Othrava did not become chain proof in this version of the lock. Vorrakai did not get the wound he had used as first law.

The old lock broke.

Every cinder in Vael Taryn cried out.

The cry passed through Mara and did not stop there. It moved into distributed objects, living hands, dead witnesses who chose waking, records, road ribbons, bridge stones, warning plates, broken command tokens, cut throat cords, soup ladles, dragon scales, and Othrava's seven sparks. Magic, which had once pooled around crowns, engines, cages, and commands, scattered like fireflies over a battlefield after rain.

Some lights went out.

Some went home.

Some entered the dead who wanted rest and gave them the strength to choose it.

Some entered the living and made them hear a name they had hoped to avoid.

Many simply vanished into earth, not destroyed but no longer available for anyone's use.

Vorrakai staggered.

Without the lock, his vastness thinned. He remained enormous, dangerous, grieving, but no longer inevitable. Behind his ribs, the gray-blue heart cracked open. Inside it was not darkness, not power, but a dragon curled around a memory of the laughing game stones, holding joy like evidence that could not save him.

Mara stepped toward him.

The bridge broke away under her foot.

Saelith caught her.

"Do not go alone," Saelith said.

Mara looked at Vorrakai. "I am not."

Othrava's eye blazed. The company stood with her. The living camp roared beyond the wound. Arveth did not return, and the fact of his absence held like one more witness.

Vorrakai's heart split.

The Death-Dream ended.

# Part VI: The Covenant After Fire""",
    34: r"""## Chapter 34: The Morning After Magic

Dawn found the world colder.

That was the first consequence anyone could understand.

Not victory. Not prophecy. Cold.

The cinder braziers outside the Dead Capital guttered at sunrise and did not relight when gnome engineers swore at them. Road-lamps that had burned for three hundred years went dark one by one along the ash plain. Lumenorath root-fire dimmed from holy white to the color of ordinary sap. Khar Veyl archive locks opened or failed depending on whether the cinder inside had chosen witness, rest, or escape. Harrowmere command seals cracked on saddlebags. Kavik route stones lost the trick that let them warm under a true path. Troll oath-bridges groaned as old borrowed heat left their joints. Dragon-shed relics stopped whispering to their owners and became beautiful bone.

People cheered for almost three breaths.

Then the first cooking line failed.

Lora Arlet stood over a dead cinder hearth with a pot of lentils, four hundred hungry mouths, and the expression of a woman who had no interest in metaphysical excuses.

"Wood," she said.

No one moved.

"The heat is gone. Trees remain. Axes exist. Anyone waiting for a miracle may do so while carrying kindling."

That became the first law of the morning after magic.

No one wrote it down, which improved it.

Mara woke under a canvas awning with Saelith asleep sitting beside her, one hand still wrapped around Mara's sleeve. For a moment she did not know where she was. The Dead Capital's towers stood against the honest sun, no longer leaning inward as if listening for a verdict. The dragon-moon eye had closed. The sky looked too large without it.

Her hands were cold.

That frightened her.

For three books, heat had lived under her skin whether she wanted it or not: furnace-heart, cinder-song, dead names, dragon memory, crown arithmetic, witness fire. Now the old burn had faded to a banked warmth so small she thought at first it had died. She pressed her palms together.

Nothing answered except pulse.

She began to cry quietly, which annoyed her because she was not sure whether the tears were grief, relief, terror, or her body making a late complaint.

Saelith woke at once.

"Mara?"

"I am here."

"Are you hurt?"

"Yes."

Saelith's face sharpened.

"Not dying hurt," Mara said. "Just... here."

Saelith understood enough to sit closer. She did not offer a beautiful answer. That was one reason Mara loved her more in the cold morning than she had in several battles.

Outside the awning, the camp discovered victory's first list.

Dead: fewer than feared, more than songs would tolerate.

Injured: too many for the healers whose songs no longer carried borrowed cinder light.

Missing: complicated by the undead who had chosen rest during the final break.

Useful relics now inert: almost all.

Dangerous relics now inert: not enough.

Arguments delayed by apocalypse now resuming: all.

Tavi came in carrying a dead pressure gauge, three cracked warning plates, and the wild-eyed joy of an engineer whose entire field had collapsed while she was not looking.

"Good news," she said. "Half the cinder systems failed into harmlessness."

Mara sat up too quickly and regretted it. "And the other half?"

"The other half failed into interesting shapes. I am not using good as a descriptor until after breakfast."

Kesh limped behind her. "Breakfast is now a political institution."

"Everything is," Sava said, entering with the register tucked under one arm. Her eyes were swollen from crying, but her chin had set itself in a new way. "Also, someone asked whether Arveth's release invalidates prior objections."

Mara's chest tightened.

"What did you say?"

"I said no, and then I asked why they wanted the dead advocate unavailable only when he inconvenienced them."

"And?"

"They have gone to reconsider in a posture resembling shame."

Saelith smiled. "He would have liked that."

Sava looked at the blank page where Arveth's mark did not move. "Yes."

That was all she said.

The morning widened.

They walked the camp because lying down made Mara feel as if the world might rearrange itself without asking. Everywhere she looked, people were learning how much of ordinary life had leaned on unconsenting dead heat. A baker beat a cold oven door with a peel until Lora put him in charge of fuel teams. Gnome engineers formed triage circles around failed devices, marking each with three questions before repair: whose memory powered it, where did that memory go, who is harmed by failure. A group of Harrowmere soldiers tried to requisition working lanterns and were stopped by fever bridge families who asked whether orders could now answer back. Troll bridge-readers crawled under wagon spans as old oath-heat left the joints. Dark-elf archivists carried boxes into sun because seals had failed and secrecy no longer had magical assistance. Light-elf singers stood in clusters, touching their throats as if their voices were newly mortal.

The undead made the hardest choices.

Some bone lanterns had gone out in the old lock's breaking. Those who remained woke dimmer, not weaker exactly, but less compelled by old summons. A dead cavalry rider sat under a wagon axle and stared at his own hands. Oren knelt beside him with a bowl of lentils.

"Do you want guard or rest?" Oren asked.

"You asked yesterday."

"Yesterday was before breakfast."

The dead rider looked toward the Dead Capital. "Guard. One hour. Then ask again."

Oren handed him the bowl. "Can you eat?"

"No."

"Hold it anyway. Warmer than your hands."

The rider obeyed and looked astonished by the useless kindness.

Mara had to turn away.

At the edge of camp, Veyrasha stood with one claw lifted while four bridge-readers argued about where she could step without collapsing a buried road. The dragon's patience looked carved from mountain fatigue.

"This is humiliating," she rumbled.

Brakka, measuring cord around her neck, did not look up. "Good."

The dragon blinked.

"Humiliation is proof that a large body has met a boundary and lived," Brakka said.

Veyrasha considered. "I dislike wisdom at ground level."

"Most tall people do."

Mara smiled despite herself.

Then the first messenger arrived from beyond Vael Taryn.

He was a human rider from Harrowmere with frost on his beard and panic in his mouth. His horse nearly collapsed under him. The royal cinder beacons had gone dark. River pumps driven by old dragon-memory had stopped. Border fortresses could no longer light command seals. A plague ward in Eastmere had opened because the cinder lock no longer recognized the dead healer bound inside it. People were alive because the bound healer had been freed. People were dying because the ward no longer worked.

The camp fell silent.

Vorrakai's argument returned without his voice: See what freedom costs.

Mara felt every eye want to turn toward her.

She looked at the messenger instead.

"Who is in charge there?"

"No one knows."

"Then they need someone from Eastmere. Not a crown order. Not me. Someone who knows the ward, the sick, the freed healer's name, and the living people now at risk."

The messenger stared. "That takes time."

"Yes."

He looked as if he might hate her. She let him.

Tavi stepped forward. "I can send engineers with non-cinder pumps. Slow, ugly, limited range."

Saelith said, "Healers too. Mortal song only. We will lose people."

Caldus said, "Escort without command seal. Answerable to local witness."

Kesh said, "Road to Eastmere is half-flooded. I know three bad routes and one worse one."

Brakka said, "Worse route has old bridge?"

"Yes."

"Then send me the load report."

Sava wrote. Not Arveth. Sava.

"Emergency compact," she said. "Expires at arrival. Renewed only by local witness and affected households."

The messenger looked from one to the other. "This is not how kingdoms move."

"No," Caldus said.

The morning after magic became movement.

Not triumphant. Not smooth. Wagons left with too few supplies and too many arguments. Engineers fought healers over space. Goblin scouts demanded hazard pay before Kesh reminded them the hazard had names now. Dragons carried loads only after landing circles were marked. Trolls cursed every wagon axle built by people who assumed roads were flat. Light and dark elves argued over whether a mortal song could hold fever panic without cinder resonance. They argued while packing.

Mara stood aside until no one needed her to point.

That was harder than battle.

Saelith noticed. "You want to go."

"Yes."

"Eastmere?"

"Everywhere."

Saelith took her hand. "That is a crown-shaped answer."

Mara closed her eyes.

"I know."

The old heat in her palms flickered once. Not command. Not summons. A single cinder-name, somewhere in the camp, asking to be heard by the person nearest it. Not Mara. Someone else.

She let it go.

The cold hurt.

It also left room for sunlight.

By noon, the camp had no songs of victory. It had work lists, funeral rows, fuel teams, emergency compacts, disabled devices, hungry people, angry people, relieved dead, and a dragon trying very hard not to step on a latrine trench.

Kesh looked over the scene and sighed. "I have seen prettier aftermaths."

Tavi snorted. "You have sold prettier aftermaths."

"Unfair. True, but unfair."

Mara sat on an overturned crate and ate lentils from a chipped bowl. They were under-salted. Oren was nowhere nearby to blame. She ate them anyway because the first law of the morning after magic had turned out to be older than every covenant:

People who would keep choosing needed feeding first.""",
    35: r"""## Chapter 35: Orders That Can Be Answered

The oath hall was built before anyone agreed it was an oath hall.

That was why it had a chance.

At first it was only three stone tables dragged from the Dead Capital's outer court because the camp needed somewhere flat to sort food, names, wounds, and blame. Trolls tested the stones for cracks. Gnomes chalked grids on them. Goblins tied ribbons to table legs to mark which queues led where. Harrowmere soldiers tried to stand at the head until Lora Arlet told them the head of a table was the part nearest the hungry person. Dark-elf clerks brought ink. Light-elf singers brought water because several people had begun confusing tears with hydration.

By afternoon, every table carried names on both sides.

On top: who had given an order.

Below: who could answer it.

Caldus stared at the arrangement for a long time.

Mara stood beside him, saying nothing because she knew the look of a person watching an old god die inside him. For Caldus, honor had once been a vertical line. Oath above, knight below, protected people somewhere beyond the shield. He had broken that line at the fever bridge and paid with exile. Then he had spent years learning that breaking a bad order did not automatically build a better oath.

Now the camp had built an ugly table and asked him to speak.

"No," he said.

Half the waiting officers startled.

Sava looked up from the register. "No to what?"

"To me founding anything alone."

Relief moved through Mara before she could stop it.

Caldus drew the broken blue shard of Conquest from his shield. It had stayed small after the Death-Dream, a coin-bright fragment set beside the names hidden on the shield's inner face. He placed it on the table. "This is useful. It is also dangerous. So is command."

An older Harrowmere captain, Lord Teren, folded his arms. "Command wins battles."

"Sometimes," Caldus said.

"Without command, the Eastmere wagons would still be arguing over wheels."

"With command, they might already be halfway there with the wrong supplies, no local witness, and three quiet injustices becoming future rebellions."

Teren's mouth tightened. "You learned contempt for officers while disgraced."

"No," Caldus said. "I learned contempt for orders that survive the people they claim to protect."

The table murmured.

Not approval. Unease. Better.

A fever bridge woman stepped forward. Mara recognized her from Conquest and the road outside the Dead Capital: Nera's cousin, maybe, or one of the living families whose names Caldus had carried in shield straps. She placed both hands on the stone.

"If a knight swears to protect me, do I get to tell him when his protection kills my child?"

Teren looked offended. "Any honorable knight would listen."

"No," Caldus said.

The captain stared.

Caldus did not look away. "No, he would intend to listen. He might even do it privately. But honor cannot depend on the honorable person's mood. Put it in the oath."

Sava wrote the line at once.

Teren flushed. "You would let civilians challenge battle orders?"

Kesh, sitting on the table because no one had yet made the mistake of forbidding him, lifted a finger. "Civilian is a charming word meaning person whose body receives the strategy."

"Stay out of Harrowmere law."

"I charge extra for staying out."

Brakka leaned her maul against the table. The sound ended several side arguments. "A bridge report lists who may close the span. Builder. Weight-reader. Person on span. Person barred from span if refusal harms them. Why should oaths be less careful than stone?"

Teren looked at the troll as if she had brought weather into a dining room.

Tavi, already chalking categories, said, "Because stone does not have noble feelings."

"Stone has better discipline," Brakka said.

The oath hall grew louder.

Old knights resisted. Not all from malice. Some were afraid of hesitation killing people. Some had watched towns burn while councils debated. Some remembered commanders who had saved lives precisely because no one had time to vote. Others simply disliked losing the invisible comfort of being obeyed first and questioned after. The table did not sort motives into clean piles. It made each one speak where the harmed could hear it.

Mara watched Caldus endure the hardest part: good arguments from people who were also wrong.

Captain Teren told the story of High Ford, where one officer ordered a retreat before civilians understood the river would rise. The retreat saved hundreds. A delayed order would have killed them. A woman from High Ford, older now, stood up and said her brother had been beaten for trying to fetch trapped neighbors after the retreat began. Both truths stood on the table, refusing to cancel.

Saelith brought water.

Ilyr wrote the stories on facing pages.

Sava made headings: emergency, review, refusal, protected party, expiration, redress.

The word redress made several officers deeply uncomfortable.

"An oath is not a debt ledger," Teren said.

Kesh inhaled.

Mara covered his mouth.

He licked her palm.

She yelped and released him.

"Everything is a debt ledger if you injure people and expect memory to do bookkeeping for free," Kesh said.

The fever bridge woman pointed at him. "Unfortunately, yes."

Caldus smiled for the first time all day.

Then the hard test arrived.

A scout came running from the northern ridge. A group of Pale Remnant fighters had taken hostages near a collapsed root road: three children, two undead witnesses, one gnome engineer, and a dragon-marked healer. They demanded Saelith and Mara come alone, unarmed, or the hostages would be purified before sunset.

Every eye turned to Caldus.

There it was: the old vertical line asking to be useful.

He could issue orders quickly. Secure ridge. Send archers. Use Kesh's bad road. Put Mara under guard. Keep Saelith away. He had the habit, the experience, the moral terror needed to turn thought into command before anyone else finished breathing.

Instead he put both hands on the table.

"Affected parties," he said.

Teren exploded. "There is no time."

"There is some time," Caldus said. "We spend it where it matters."

The hostage families came. So did the route scouts who knew the ridge. So did two undead witnesses who knew the Remnant's purification rites. So did Auralian, furious and off-key. So did a dragon who could see the collapsed root road from above but would cause panic if she flew too low. So did the gnome engineer's apprentice, who said her master had a habit of carrying smoke pellets in his left boot. So did Saelith, who refused to be discussed as terrain.

The plan they made was not clean.

It had three signals, two failures, one route no one liked, and an argument over whether a wrong-note chorus counted as weaponry. It placed Caldus in command of a timed approach that expired after twelve minutes. It gave the hostage families the right to call withdrawal if the Remnant began rites early. It gave Saelith the right to refuse being used as bait. It gave Mara no special authority, which she resented enough to feel reassured. It required Kesh to guide a rescue team through a drainage cut he described as "technically a road in the sense that regret is technically education."

The rescue worked.

Mostly.

One Remnant fighter died. Two escaped. The hostages lived. A child broke an arm. The gnome engineer's smoke pellets set fire to a bush and three reputations. Saelith sang one wrong note from a distance and the Remnant's purification rhythm collapsed long enough for Auralian's singers to drag the undead witnesses out by their lantern poles. Caldus's twelve-minute command expired while he was still shouting an order, and the fever bridge woman rang the expiration bell directly beside his ear.

He stopped.

For one heartbeat, the old knight in him looked murderous.

Then he lowered his sword.

"Renewal requested," he said, breathing hard.

"Denied," said the hostage mother.

Everyone froze.

She pointed at the western slope. "My daughter is out. The rest of the route risks others. Change plan."

Teren looked as if the world had ended.

Caldus looked at the slope, saw what she saw, and nodded. "Command ended. New plan."

That was the oath hall's founding.

Not the words Sava later polished, not the stone tables, not Caldus placing his broken shard into the compact box. It was the moment a knight stopped mid-order because the protected party answered.

Afterward, while healers tended the rescued hostages, Teren stood beside Caldus in the dusk.

"That could have cost us the remaining two," he said.

"Yes."

"You will live with that?"

Caldus watched the hostage mother hold her daughter with such ferocity that no oath could have improved it. "I will not live above it."

Teren had no reply.

Mara found Caldus later behind the oath tables, cleaning blood from his gauntlet with shaking hands.

"You did well," she said.

He gave her a look.

"Badly," she amended. "But in the right direction."

"That is our house motto now?"

"Probably."

He huffed.

For a while they listened to the hall argue. Sava read clauses aloud while people interrupted. Brakka corrected load metaphors. Kesh charged three officers for unsolicited honesty and was paid in bread. Tavi designed a bell that rang when an oath exceeded its expiration and then had to label it dangerous because everyone wanted one. Saelith sat with the rescued undead witnesses, asking whether they wanted guard, testimony, or rest.

"I used to think honor meant being ready to die for others," Caldus said.

Mara leaned beside him against the stone.

"Now?"

"Now I think dying is sometimes easier than being answerable to them."

"That sounds awful."

"It is."

"Good."

He smiled then, tired and real.

At sunset, the first answerable oath was carved on both sides of a stone table.

On one side: I swear to protect.

On the other: We reserve the right to answer what protection costs.

No one cheered. The stone was too heavy for cheering.

But when the fever bridge woman pressed her hand beneath the second line, the cinder spark inside Caldus's shield warmed without burning. Honor had not vanished. It had stepped down from the crest and taken a seat where it could be interrupted.

Mara thought Arveth would have objected to at least three commas.

Sava did too.

Neither of them fixed them yet.""",
    36: r"""## Chapter 36: Beauty Without Silence

Lumenorath arrived as a wound wrapped in blossoms.

Not the city itself. Not yet. The first grove to answer Saelith's call was a traveling grove, six wagons of white-root saplings carried from refugee camps, each tree planted in a clay tub cracked by road weather. Their leaves should have been luminous. Instead they came mottled: white and green, brown-edged, shadow-veined, some curling inward as if ashamed of their own survival. Singers walked beside them barefoot through ash mud. Dark-elf archivists walked at the rear with public record boxes. Orrowen dead drifted in bone lanterns between the wagons, choosing waking for this hearing and none too gently.

The old Lumenorath would have hidden the grove until it looked perfect.

Saelith had ordered it brought to the center of camp.

That was why half the light-elf singers hated her.

They gathered at dawn under the damaged saplings while steam rose from cooking fires and the oath hall still argued behind them. Some wore Pale Bough white with the cords cut short. Some wore traveling clothes. Some had shaved their heads in mourning. Some had painted Orrowen names on their sleeves. A few wore old perfect cords uncut, defiant as knives.

One of those stepped forward before Saelith could speak.

Her name was Elianth. She had been a senior cantor before the holy war split the boughs. Her voice, when she greeted the assembly, made Mara understand why people had once mistaken beauty for proof.

"We come," Elianth said, "to preserve what remains."

The grove sighed in relief.

Saelith stood very still.

Mara, at the edge of the circle, felt Kesh lean close. "That sentence has teeth."

"Yes."

"Polished teeth."

Saelith heard them and did not smile.

Elianth turned to her. "You broke the correction. You exposed the cleansing. You named Orrowen. Good. Necessary. But now the people are raw. Children wake screaming because songs no longer hold their dreams. Mourning rites fail midway. Old singers cannot find pitch without cinder resonance. The dead who choose testimony interrupt lullabies. Our beauty is damaged. We must preserve enough form that our people do not lose themselves entirely."

Every word was reasonable.

Mara wanted to distrust it cleanly and could not.

Saelith bowed her head. "Yes."

A stir moved through the singers.

Elianth's eyes sharpened. "Then you agree."

"I agree that people need form."

"And purity of form."

"No."

The grove's roots shifted in their cracked tubs.

Saelith lifted one hand to her throat. The cut cord from the Death-Dream hung there now, not as office, but as warning. "Purity is what our fear called beauty when it wanted no interruptions."

Elianth's voice cooled. "You would make ugliness doctrine."

"No. I would make interruption survivable."

Ilyr came forward with one of the record boxes. That made several light elves bristle. He noticed, because Ilyr noticed every room that wanted him smaller. He set the box down anyway.

"Public record of cleansed songs," he said.

Elianth's mouth tightened. "This is a Lumenorath rite."

Maelin, standing beside him, gave a smile with too many edges. "Orrowen's dead were included without invitation. We are improving the guest list."

The bone lanterns flickered.

One dead child laughed.

Saelith closed her eyes for a breath, then opened them and began the first repair song.

It was bad.

Not intentionally. That made it worse. Her voice cracked on the third phrase. The old cinder resonance that had once carried light-elf mercy through white roots was gone. Mortal breath had to do the work now, and mortal breath tired. The grove did not glow. It shivered. Several singers looked away in pity sharpened by relief: even Saelith Dawnmere, breaker of the correction, could not make beauty without the old borrowed power.

Elianth stepped forward and sang the phrase properly.

The difference hurt.

Her note rose clean as moonlit water. The saplings straightened. Children in the circle stopped fidgeting. Even Mara's shoulders lowered. It was not malicious. It was lovely. It made the world easier to bear for the length of one breath.

Then an Orrowen lantern went dim.

Not out. Dim.

Saelith stopped.

Elianth continued, eyes closed.

The lantern dimmed further.

Mara understood with a cold twist. The perfect note did not erase the dead as the old correction had. It simply made their interruption harder to hear. After everything, even stripped of cinder power, beauty still knew how to become polite silencing if no one named the cost.

Saelith put both hands over her ears.

Elianth's song faltered. "What are you doing?"

"Listening for what I cannot hear under you."

The circle went silent.

Saelith turned to the dim lantern. "Do you want song?"

The flame trembled.

The child's voice came thinly. "I want my mother's bad one."

A woman in the back made a strangled sound.

She was human, not elf. Orrowen by birth, ash-road refugee by survival, mother by the way her face broke before her feet moved. The circle parted. She came forward with hands pressed to her mouth.

"I cannot sing," she whispered.

The lantern brightened.

"That was not the question," Saelith said.

The mother's laugh broke into a sob. She sang four notes.

They were terrible.

Flat, cracked, tuneless with grief. The grove did not straighten. No child in the circle became calmer. No doctrine could have used that sound on a banner. But the lantern flared gold-white and then soft blue, the color of a dead child resting against a memory that belonged to him and not to a system.

Elianth looked as if someone had struck her.

Saelith wiped her face. "Beauty is not the note that most efficiently quiets pain."

"Then what is it?" Elianth asked.

Saelith looked around the circle: light elves ashamed and angry, dark elves suspicious, Orrowen dead listening, refugees who had not asked to become theology, children with dirty hands, Mara with burned palms, Ilyr holding a record box like a challenge, Kesh pretending not to cry, Caldus standing awkwardly beside a sapling because no one had told him where knights belonged now.

"Attention shaped with care," Saelith said. "Sometimes it is a perfect note. Sometimes it is a mother's bad one. Sometimes it is silence chosen after asking. Sometimes it is the ugly interruption that keeps a song from becoming a room with no door."

The grove did not glow.

It put out new leaves.

Small ones. Uneven. Some white, some green, some shadow-veined so dark they looked almost black until sun touched them. Dark-elf children at the edge gasped. A light-elf boy reached for one and stopped before touching.

"Ask," said three people at once.

The boy went scarlet.

He asked the sapling.

No one knew what answer to expect.

The leaf bent toward his hand.

He touched it with one finger and began to cry because it did not burn him, cleanse him, correct him, or turn away.

Elianth sank to her knees.

For a breath Mara thought the old cantor had been defeated. Then she saw Elianth's face. Not defeat. Grief. The particular grief of someone realizing that a thing she had loved had harmed people without ceasing to be lovable.

"I taught the old correction to children," Elianth said.

No one rescued her from the sentence.

Saelith knelt across from her. "Yes."

"I thought it saved them."

"I know."

"That does not make it harmless."

"No."

Elianth looked at the Orrowen lantern, then at the mother who had sung badly and beautifully by refusing to be useful. "What do I do?"

Saelith looked tired enough to be honest. "You learn broken harmonies from the people your perfect ones drowned."

That became the second repair.

Not a performance. A class.

The Orrowen mother taught four bad notes. Dark-elf archivists taught listening pauses where records could be read into song without becoming footnotes. Light-elf children taught the places their voices cracked after nightmares. Refugees taught road calls. A goblin girl added a rude rhythm because, she said, songs without exits were suspicious. A troll hummed a load note low enough to make the sapling tubs vibrate. Tavi demonstrated how not to let resonance collapse the clay. Kesh charged admission in compliments and received none, which he entered as cultural persecution.

Elianth sang again near dusk.

Her voice remained beautiful.

This time it left holes.

Into those holes came names, interruptions, a child's bad lullaby, a dark-elf correction, a silence no one filled until the lantern brightened by choice. The song became less pure and more alive.

Mara sat beside Saelith after the rite, both of them muddy to the knees, listening to the grove rustle with leaves no old law would have approved.

"You changed your people today," Mara said.

Saelith leaned against her shoulder. "A little."

"That is not little."

"It has to be. Large changes become banners too quickly."

Mara looked at the new leaves. "Arveth would complain about that sentence."

"Yes."

They sat with the ache of his absence.

After a while, Saelith said, "Part of me wanted Elianth to be cruel."

"So you could beat her?"

"So I could remain simple."

Mara took her hand. The grove smelled of sap, ash, sweat, and cooking smoke. The world after magic was colder, louder, less beautiful in the old way. But a dead child had heard his mother's bad song. A white root had bent toward a dark-veined leaf. Elianth had not been forgiven and had not fled. Saelith's voice would never again be the same, and that, perhaps, was how culture survived without becoming a cage.

At twilight, the traveling grove opened its first blossom.

It was small, uneven, white on one side and shadow-blue on the other.

No one sang over it.

They asked whether it wanted quiet.

For once, quiet answered yes.""",
}


WORD_FLOOR_DEEPENING: dict[int, str] = {
    33: r"""When the old lock broke, it tried one last disguise.

It became useful rubble.

The broken pieces of the seven chairs scattered across the bridge, and each piece offered itself to the company as a tool. A command splinter that could make frightened soldiers pause before striking. A song shard that could calm panic without quite silencing grief. An archive latch that could open sealed rooms when names were spoken. A road knot that could reveal hidden paths to the hungry. A bridge pin that could hold impossible weight for one emergency. An engine rivet that could power a ward without anyone noticing the dead name inside. A dragon scale that could translate fear between large and small bodies before someone burned.

Tavi stared at the rivet.

"It is still doing it," she said.

"What?" Mara asked.

"Making necessity sound like consent."

The lock whispered through every shard: take only what saves. Leave what harms. You are wiser now. You will use us better.

Mara wanted to believe that.

So did everyone.

The camp beyond the wound had sick people, hungry people, injured people, roads collapsing, dragons afraid to land, engines going cold. Useful magic lay at their feet in pieces too small to look like a crown. That was how systems survived revolutions: by breaking into tools before anyone could bear to throw them away.

Brakka lifted the bridge pin, weighed it, and set it down.

"Maybe one day," she said.

Tavi looked horrified. "Maybe?"

"If the span asks. If the carried ask. If the pin can refuse. If someone remembers this conversation and makes it annoying to repeat."

Tavi considered, then nodded reluctantly. "Annoyance as structural safeguard."

Kesh held the road knot between two fingers. It glowed toward him like a shortcut that loved him personally.

"I hate this," he said.

"Because you want it?" Ilyr asked.

"Because I can already imagine the justification."

He dropped it into Sava's open register. "Future review. Public. With snacks, because otherwise no one behaves."

Sava wrote: Tempting fragments retained only as named hazards. No emergency use without affected witness and post-use repair. Snacks recommended but not legally determinative.

Mara looked at her.

"What?" Sava said.

"Legally determinative?"

"I am grieving. Let me have phrases."

The lock weakened further because the company had not pretended usefulness was harmless. The fragments dulled. Some remained. Most became only material, waiting for a future brave enough to ask better than the first covenant had asked.

Mara left the command splinter where it lay.

That cost her more than she expected.""",
    34: r"""News kept arriving after noon.

Every messenger carried a different version of the same sentence: the world had leaned on the dead and was now discovering the posture. In the south, fishing towns lost tide bells that had warned them of dragon-made storms. On the eastern steppe, undead plow teams stopped mid-field and asked whether they were workers, ancestors, prisoners, or weather. In Brassroot, three factories shut down because safety governors powered by bound cinder memory went dark; two more tried to keep operating and were occupied by apprentices who had learned Tavi's worst habits. In Lumenorath, nursery songs failed, and children slept badly for the first honest night in generations. In Khar Veyl, doors opened that had been sealed to protect truth from panic, and panic immediately made several excellent arguments for why the doors should close again.

Mara wanted a map.

Then she wanted a bigger map.

Then she realized wanting a bigger map was the old throne clearing its throat inside her.

She went to Lora instead.

The soup line had become a council by accident. People brought problems because they were hungry, and hunger made hierarchy look foolish. Lora sorted bowls, fuel teams, and messengers with the same ladle she had nearly lost to the old lock.

"I need to know how not to try to hold all of this," Mara said.

Lora handed her a sack of onions.

Mara blinked. "Is this symbolic?"

"It is onions."

"Right."

"Peel them."

Mara sat on a crate and peeled onions while the world reported its fractures. The work made her eyes water, which let everyone politely ignore the fact that she had been close to crying anyway. Each onion was small, local, immediate, and no substitute for saving Eastmere or Brassroot or any child sleeping without old songs. That was the lesson. Not enough. Still necessary.

After the sixth onion, Mara understood why Lora had not given her advice.

Advice could become a banner.

Onions became soup.""",
    35: r"""The oath hall did not end with Harrowmere.

That was Caldus's private disappointment and public relief.

Once the first answerable oath was carved, everyone wanted to borrow it badly. Lumenorath singers wanted healing vows that could be interrupted by the healed. Khar Veyl archivists wanted record oaths that could be challenged by those named in the file. Goblin road captains wanted route contracts that expired loudly when sold without witness. Gnome engineers wanted maintenance oaths with emergency exceptions so broad Tavi threatened to bite someone. Troll bridge-readers wanted all of the above translated into load language before sunset.

The stone tables became crowded with people trying to turn one hard-won idea into a universal template.

Caldus saw the danger before Mara did.

"No model oath," he said.

Groans rose from every clerk within hearing.

Sava looked personally betrayed. "You cannot be serious."

"I am very serious."

"Do you know how much copying that creates?"

"Yes."

"You monster."

He almost smiled. "If the protected must answer, the protected must shape the words. Harrowmere's oath cannot wear Lumenorath's injuries and call the fit good."

Saelith touched the cut cord at her throat. "He is right."

Ilyr closed the folder he had already begun preparing. "Annoyingly."

Kesh stretched on the table. "I support local variation when it prevents paperwork from becoming a climate."

Tavi jabbed chalk at him. "You support local variation because it lets you hide fees in dialect."

"Also true."

So the oath hall split into circles. No central doctrine. No clean export. Each people borrowed the questions, not the answers: who gives the order, who bears the cost, who may refuse, who reviews, when does authority expire, what repair follows harm, where are names recorded, who feeds everyone while this argument continues. The questions traveled better than any oath could have.

Mara watched them move from circle to circle and felt something in her chest unclench.

Not hope exactly.

Hope, she had learned, was too often asked to do work planning should have done.

This was rougher.

Practice.""",
    36: r"""The first blossom did not stay singular.

By morning there were five, and by noon eleven, each one wrong by the old measures. One had petals shaped like little listening ears. One opened only while a dark-elf child read from a record of Orrowen. One closed whenever Elianth's pitch became too perfect and reopened when she laughed at herself. One grew upside down beneath the wagon bed, where Kesh claimed it had chosen superior company. One remained a tight bud until a human boy with no voice signed a road song with his hands.

The grove became a scandal immediately.

Pilgrims came because rumor travels faster than reform and arrives wearing perfume. Some wanted proof that Lumenorath had been redeemed. Some wanted to denounce corruption. Some wanted a petal as relic. One attempted to kneel to Saelith, which went poorly because Mara stepped on his robe before he completed the motion.

"Accident," Mara said.

Kesh, beside her, looked at the perfectly clear sky. "Roads are dangerous."

Saelith saw the kneeling man and went pale. Not with anger. With recognition. Sainthood had survived worse than being refused. It knew how to crawl back under gratitude.

She climbed onto a wagon tongue.

"Do not kneel," she said.

Several people froze halfway down, which created an unfortunate posture.

"Do not make this grove proof that the work is done," Saelith continued. "Do not make me proof. Do not make Orrowen's dead proof. Do not make new blossoms proof. Beauty is not acquittal."

Elianth, standing below, added, "Beauty is evidence requiring cross-examination."

Everyone stared.

Ilyr closed his eyes. "That metaphor needs supervision."

Maelin whispered, "I love it."

The crowd did not know what to do with a miracle that came with procedural warnings. That, Saelith later told Mara, gave the miracle a fighting chance.

At dusk, the grove held its first quiet by consent. No one sang. No one filled the space because silence looked vulnerable. The Orrowen lanterns dimmed comfortably. Children slept against wagon wheels. Elianth sat with the mother whose bad song had opened the first repair and asked to learn it again, this time without improving it.

Mara watched Saelith listen.

Not lead.

Listen.

It was the most beautiful thing in the grove, which meant Mara kept the thought to herself so beauty would not have to carry it.""",
    133: r"""The Death-Dream did not release them immediately after the lock broke.

It made them walk through what had been freed.

Mara hated it for that until she understood that hatred was another wish for a clean ending. The old lock had held too much for too long. When it failed, every imprisoned consequence needed somewhere to go. The bridge dissolved into a field of floating rooms, each one lit by a different freed cinder. Some rooms were tiny: a child's bedside, a forge corner, a toll booth, a prison stair. Some were vast enough to hold cities. Every room contained a place where the world had once used dead memory as invisible support.

In one, a Harrowmere widow stood before a wall of command seals and realized her husband's ghost had been bound for thirty years to verify noble orders. In another, a gnome apprentice watched a safety governor spit out the name of the woman whose memory had been powering it since a laboratory accident no one had recorded honestly. In a third, a light-elf cradle song failed because the dead Orrowen child woven into its comfort chose to stop soothing descendants of the people who had numbered him.

The company could not fix the rooms.

They could only witness where the freed names went.

Some names fled upward and vanished into rest. Some moved toward living people who would hate what they heard. Some curled in confusion, having been tools so long that personhood felt like exposure. A few tried to return to the broken lock because use was familiar and freedom had no instructions.

Mara reached toward one of those without thinking.

It was a miner from Kell Ashgate, a woman named Vessa who had died before Mara was born and whose memory had warmed a slag pump for decades. Vessa hovered as a coal-shaped light, pulsing with panic.

Need a task, the cinder whispered.

Mara's throat tightened. "You do not have to have one."

Need a task.

Kesh looked away. Tavi swore under her breath. Caldus bowed his head. No one had told the dead that freedom might first feel like being unemployed by reality.

Mara sat on the dissolving bridge floor beside the coal-light.

"Then your task is to decide whether you want a task," she said.

That sounded ridiculous. It also made Vessa pause.

"Who asks?" the cinder whispered.

"Mara Venn. Kell Ashgate. Former ash-runner. Bad at resting."

The coal warmed.

Kell?

"Still loud."

Good.

Vessa drifted toward Mara's wrist and stopped before touching the Kell cloth. Ask later?

"Yes."

The cinder vanished toward the living world.

Mara knew, with a certainty that was not command, that one day someone in Kell Ashgate would feel old heat near a cold pump and hear a dead woman ask whether work was wanted. That person might answer badly. Might try to use Vessa. Might honor her. Might build a better pump. Freedom did not guarantee goodness. It only returned the question to the place where answer could happen.

Room after room opened.

Othrava passed through them in fragments of blue-white light. She did not gather the dragon cinders to herself, though many turned toward her. A dead stormling called Mother. A chained river-drake called Judge. A burned hill dragon called Witness. Othrava trembled under each name.

Take us, some begged.

No, she answered, voice breaking mountains inside the dream. I will not become the gentler lock.

The dragon cinders scattered, some furious, some relieved.

Vorrakai watched from the edge of the broken heart.

For the first time, his face held envy.

"You could choose too," Mara said.

His eyes found hers.

Choose what? Rest? Trial? Shame? A world where my grief becomes one voice among many and may be outvoted by fools?

"Yes."

He laughed then, and the laugh had no thunder left. Only tiredness.

You think that mercy.

"No. I think it is what remains when mercy stops trying to win forever."

The rooms began to fall away.

The Death-Dream loosened around them. The old lock's last memory showed the laughing game stones from the first age: dragonlings losing to mortal children, Othrava laughing, young Vorrakai watching without calculation. The image did not accuse. That made it harder.

Vorrakai reached toward it.

The game stones dissolved before his claw touched them.

He closed his hand around absence.

The company fell toward morning.""",
    134: r"""By late afternoon, the camp had invented three new kinds of failure.

The first was honest failure. A non-cinder pump assembled by Brassroot engineers broke after six minutes and sprayed muddy water over a line of injured soldiers. The engineers named the failed seal, apologized to the soaked patients, and fixed it in public while Pinna wrote the repair on a board large enough for angry people to read. The patients remained angry. The pump improved. This, Tavi declared, was civilization making an unattractive noise.

The second was nostalgic failure. A group of Harrowmere officers found an old command lantern that still held a little cinder glow and tried to use it to coordinate supply lines. The lantern lit once. The name inside it screamed. Every horse within fifty paces bolted, and the officers spent the next hour retrieving flour sacks from ash mud while the fever bridge families watched without sympathy. Caldus entered the incident into the oath hall as evidence that convenience had a memory and sometimes a voice.

The third was predatory failure.

That one frightened Mara most.

By sunset, merchants from the outer caravan had begun buying dead relics for almost nothing from refugees who did not yet understand what had changed. Cold cinder stones. Inert route charms. Cracked song roots. A dragon-scale cup that no longer whispered weather but still carried the prestige of having done so. People sold because they needed food, passage, medicine, boots. Buyers smiled with the old patience of profit arriving before law.

Kesh found them first.

He did not draw a knife.

That was how Mara knew he was truly angry.

He set his cracked route token on the merchant table. The green spark inside it pulsed once, and every purchased relic named itself. Not loudly. Loud enough. A widow's husband. A dead road child. A dragonling's shed fever memory. A prisoner who had powered a lock in a jail where no one remembered his face. The merchants backed away as if names were contagious.

"Emergency resale compact," Kesh said.

"You have no authority," one merchant snapped.

Kesh smiled. "Correct. This is an invitation to avoid being named creatively by every hungry person you attempted to underpay."

Mara arrived with Lora, which helped because Lora carried a ladle and no patience.

The compact they made was ugly and immediate. No relic sale without name disclosure if known. Food debts could not be paid in dead memory until a witness circle asked whether sale was necessary or coerced by hunger. Inert relics could be traded as material, but not under claims of power they no longer had. Any object containing a responsive cinder had to be asked. If no answer came, the sale waited.

"This will slow the market," the merchant said.

Lora looked at the soup line, the failed hearths, the injured, the dead choosing rest, the living trying not to become worse because survival was expensive.

"Good," she said.

Mara felt the old crown-shaped urge again: make the rule everywhere, immediately, perfectly.

Instead she peeled another onion.

The merchant watched her, baffled and furious. It was possible, Mara thought, that one defense against becoming a ruler was being seen doing work no ruler would choose for a mural.""",
    135: r"""Night did not quiet the oath hall.

It changed who had courage to speak.

During the day, captains and clerks dominated because they were used to rooms becoming official when they opened their mouths. After moonrise, the quieter people came: cooks, stretcher-bearers, undead witnesses, apprentices, children sent to listen and failing to remain unseen, a dragon-shadow handler whose job had never appeared on any command chart because everyone assumed dragons simply chose where not to crush people.

They brought small orders.

That was what undid Caldus.

Grand oaths had prepared him for grand correction. Protect the weak. Defend the road. Serve the crown, then the people, then the answerable compact. But the small orders showed where command entered the body. Stand there. Move faster. Wait. Carry this. Do not speak. Hold the line. Leave the body. Stop crying. Sing softer. File later. Eat after. Smile for morale.

A stretcher-bearer named Min said, "If I am ordered to leave someone because more wounded are coming, who answers me afterward?"

No one answered quickly.

Good, Mara thought.

An undead witness, a former drummer with half a jaw, tapped a rhythm on the table. Sava translated from the witness slate: If ordered to continue guard after choosing rest, what bell may I strike?

Caldus wrote that one himself.

A child asked whether parents could swear answerable oaths.

Everyone became extremely interested in their cups.

Lora, who had come to deliver soup and stayed because she smelled cowardice, said, "Yes."

The child nodded with terrifying satisfaction.

By midnight, the oath hall had stopped sounding like military reform and begun sounding like a world learning how many orders had hidden in ordinary life. That was when Teren, the old captain, returned. He had washed his face. He looked smaller without certainty arranged around him.

"I gave an order at High Ford," he said.

The hall quieted.

"After the retreat. A boy tried to go back. I struck him. His sister died on the far roof. I told myself the order had saved hundreds, and it had. I did not enter the strike because it seemed small beside the flood."

The High Ford woman who had spoken earlier looked at him for a long time.

"Her name was Lysa," she said.

Teren bowed his head. "Lysa."

The cinder shard in Caldus's shield warmed.

Not absolution. Witness.

"What repair?" Sava asked.

Teren's face twisted. "I do not know."

"Good start," Kesh muttered.

The High Ford woman said, "Teach it with the retreat. Both. Every time."

Teren nodded.

"And when you teach command expiration," she added, "use her name before the river map."

His hands shook. "Yes."

Caldus wrote the addendum with care.

Mara watched him and realized the oath hall had done something no battle could have done. It had made honor slower. Not weaker. Slower. Slow enough for a dead girl's name to enter before the lesson became clean.

At dawn, the stone tables held more than law.

They held hesitation, amendments, bad handwriting, soup stains, grief, and the first public record of people learning that answerable orders did not make authority impossible.

They made authority heavier.

That was the point.""",
    136: r"""The grove's repair reached the dark elves before anyone invited it to.

That was another useful scandal.

Khar Veyl observers had come to document Lumenorath's discomfort, which was a noble scholarly purpose if one ignored how much they enjoyed it. They stood with inkstones, root-fire lamps, and faces arranged into professional neutrality. Then the shadow-veined blossoms opened toward their records, and the ink changed color.

Not black.

Not white.

Blue, like Othrava's winter river fire.

The archivists panicked quietly, which meant only six people noticed and all six were delighted.

Ilyr took the changed inkstone from his mother's hands. "It wants song in the record."

"Records do not want," she said automatically.

The ink pulsed.

She sighed. "Apparently records have become impertinent."

Saelith invited the Khar Veyl observers into the circle.

Elianth looked alarmed, then ashamed of looking alarmed, then irritated that shame had become visible. "They do not know the forms."

Maelin laughed. "Neither do you anymore."

That should have become a fight.

Instead the Orrowen mother began her bad four-note lullaby again, and the changed ink recorded it as both sound and gap. Dark-elf archivists added names between notes. Light-elf singers answered with breath rather than correction. A goblin child clapped on the wrong beat and was immediately defended by three other children as an emerging tradition.

The song-record formed in the air.

It was not music only. It was not text only. It was a living public thing, ugly in several directions, impossible to seal because sealing one part made another part sing louder. Ilyr stared at it with open hunger.

"Do not fall in love with an archive," Kesh said.

"Too late," Maelin said.

Ilyr ignored both of them. "This could hold testimony without freezing it."

Saelith shook her head. "Could. Not will."

"Yes."

"It will need singers who accept correction."

"And archivists who accept being heard."

"Difficult."

"Catastrophic."

They smiled at each other like people admiring a cliff they intended to climb badly.

Mara saw in that moment the shape of repairs still to come: Khar Veyl's public dark, Kavik's road compact, Third Arch's refuge bridges, Kell Ashgate's loud future. None would be solved by the old magic breaking. The break had merely removed the excuse that cages were necessary because no alternative had been imagined.

The grove rustled.

A shadow-blue blossom dropped one petal into the inkstone.

Ilyr's mother picked it up and, after a long pause, asked the nearest Orrowen lantern, "May I enter this in record?"

The lantern answered, "Only if my mother sings badly beside it."

The old archivist bowed. "So entered."

Mara leaned against Saelith and felt both of them shake with tired laughter.

Beauty had survived.

It had also become significantly harder to manage.

That seemed like a good sign.""",
    233: r"""Veyrasha nearly took Vorrakai's final fragment.

No one blamed her.

When the Death-Dream loosened, a shard of the gray-blue heart fell to the bridge. It was small enough to fit in a dragon's claw and large enough to make every living creature present feel that the world might become safer if someone strong carried it carefully. The fragment held Vorrakai's memory of every first-age failure. Not command. Not stillness. Knowledge. Dangerous knowledge, but knowledge that could warn dragons away from old mistakes.

Veyrasha landed beside it with a sound like cliffs deciding to kneel.

Othrava's light went very still.

Mara said nothing. The shard did not belong to her refusal.

Veyrasha lowered one talon. "If dragons do not remember this, we will repeat it."

Othrava answered, Yes.

"If mortals hold it, they will fear us with it."

Yes.

"If no one holds it, memory scatters."

Yes.

Veyrasha's talon trembled over the shard. She was magnificent, ancient, wounded, and still young compared with the mistake at her feet. Mara saw the same temptation the throne had offered her, scaled for dragon grief: become keeper for the good of those too small, too brief, too forgetful.

Othrava did not command her.

That was the gift.

At last Veyrasha drew back. "Then we make it public among dragons and mortals both, and we do not let any one nest sleep with it under wing."

The shard split into many dark sparks.

Some flew to dragon scales. Some to mortal records. One to Brakka's measuring cord. One to Lora's ladle, which rang in outrage somewhere beyond the dream. One to the blank page in Sava's register. None to Mara alone.

Veyrasha bowed her head, shaking.

"I wanted it," she said.

Othrava's voice softened. So did I.

The old lock lost another root. Not because desire had vanished, but because two dragons had named it before it became law.""",
    234: r"""Eastmere's second message arrived before the first rescue party left the camp.

The plague ward had not merely opened. It had begun arguing.

The dead healer freed from the cinder lock was named Hessa Wound-Binder, and Hessa had chosen waking long enough to tell Eastmere that the ward protocols were wrong. Half the town wanted to bind her again because the old protocols had saved them for generations. The other half wanted to burn the ward because anything built on a dead healer's bondage felt poisoned beyond use. Meanwhile fever did what fever does when ethics arrive late: it spread.

Mara listened to the messenger and felt the familiar trap close: two sides, both right enough to bleed for, both wrong enough to kill.

Saelith asked the question first. "What does Hessa want?"

The messenger stared. "She is dead."

"Yes."

"She is also arguing with the mayor."

"Then she has a position."

The answer, when dragged out through exhausted testimony, was practical. Hessa did not want the ward burned. She had built some of it while alive. She did not want to be bound again. She wanted three apprentices trained, all living, all answerable, and she wanted her name removed from the lockstone and entered on the teaching wall. She would advise for nine days, then be asked again whether she chose rest.

"That is not enough to stop the fever," the messenger said.

Saelith's face tightened. "No."

Tavi added two non-cinder pump teams. Lora added onions, which the messenger did not understand until someone explained soup. Kesh found a route that passed through a village owed compensation by Eastmere and made the debt part of the escort agreement. Caldus assigned guards under an oath that expired at the ward gate. Sava wrote Hessa's requested terms first, before mayor, town, or crisis.

Mara watched the plan form around a dead healer's consent and living bodies' need.

It was slow.

It was inadequate.

It was the opposite of Vorrakai's mercy.

The messenger left with a packet of bad answers made public enough to improve on the road.""",
    235: r"""The family-oath circle became the loudest table by accident.

No one had wanted to begin there. Armies were easier. Roads were easier. Even dragon landing consent, for all its massive logistical problems, offended fewer people than asking whether households contained orders that needed answering. But the child who had asked about parents came back with four friends, two older siblings, and a grandmother whose eyes suggested that she had waited seventy years for law to become this inconvenient.

"Children cannot answer every parental order," a father said.

"Correct," Caldus said.

The father relaxed too soon.

"That means the oath must name which orders they can answer, when, and who witnesses if answer is unsafe."

The relaxation died.

Mara watched Caldus struggle not to flee. He had faced dragons with less fear. But the oath hall had dragged him from battlefield into kitchen, workshop, school, sickroom, marriage bed, apprenticeship contract. Power did not stop being power because it wore a familiar face.

Lora took over when everyone began speaking at once.

"Food rule," she said.

"This is not about food," someone objected.

"Everything is eventually about food. Rule: the person who eats last gets to say if the system is fair."

The grandmother pointed at her. "I like that one."

They began with meals because meals were safer than love and more honest than philosophy. Who ate first. Who ate less. Who was told sacrifice built character. Who controlled the pantry. Who got sent from the table before hard questions. By the time the circle returned to orders, several adults had stopped using the word natural.

Caldus wrote until his hand cramped.

At the bottom of the page he added: Protection inside a household remains protection subject to answer.

The child read it aloud, stumbled over subject, and grinned anyway.

Mara thought of Kell Ashgate, of Joryn pushing bread into her hand and calling it strategy, of every system that had taught poor families to spend themselves before anyone called it law.

Answerable oaths, she realized, would not make homes gentle.

They might make some cruelties less invisible.

That had to count.""",
    236: r"""Elianth's old students arrived on the third day.

They came in white traveling robes, twenty-seven singers with perfect posture and exhausted eyes. Some had fought with the Pale Remnant and surrendered. Some had broken from it late. Some had merely stayed silent because silence had seemed safer than betraying teachers, friends, parents, music, memory. They stood outside the traveling grove and asked whether they were allowed to hear the broken harmonies.

No one knew who had authority to answer.

That was progress.

Elianth walked to them alone.

Mara tensed, but Saelith shook her head. "This part is hers."

The old cantor faced her students. For a moment, she looked again like the woman who had once taught children to make mercy beautiful enough to obey. Then she bowed, not low enough to perform repentance, low enough to mean it hurt.

"I taught you to perfect notes before asking what they covered," she said.

Several students began crying at once.

"I will not ask your forgiveness today," Elianth continued. "That would make my shame another lesson you must complete. I ask whether you will learn what I failed to teach."

A young singer at the front said, "We do not know how to sing if every note may be challenged."

Saelith answered from the grove edge. "Good."

The student flinched.

Saelith softened. "Good because that fear is honest. Start there."

They did.

The first lesson for the old students was not song. It was waiting while Orrowen names were read. No harmonizing. No weeping loudly enough to become the center. No correcting pronunciation unless asked. No making grief pretty. Several failed in the first hour. The Orrowen mother whose bad lullaby had opened the repair told one student, "Your tears are standing on my son." The student looked wrecked and stayed.

By evening, one perfect singer managed four cracked notes without improving them.

The grove opened another shadow-blue blossom.

Elianth sat down hard in the mud and laughed with a sound no choir would have admitted.

Saelith laughed too.

Mara did not understand the musical victory, not fully. But she understood the sight of people remaining after the story in which they had been good finally ended.

That, too, was a kind of courage.""",
    333: r"""The last thing Mara saw before morning was Vorrakai choosing not to vanish.

That choice mattered.

The lock was broken. The throne was gone. The first forced chain had been answered differently inside the wound. Othrava had taken back her name, the cinders had scattered, and the vast architecture of his mercy had collapsed into fragments no single will could hold. It would have been easy, almost beautiful, for Vorrakai to dissolve into ash and leave the living to call it victory.

Instead he remained.

Smaller now. Still immense, but no longer the size of inevitability. His star-black scales had dulled to the color of wet slate. The crown shards around him had fallen. The gray-blue heart in his chest leaked light in thin streams, each one carrying a name he had once used as evidence for ending choice.

Mara stood across from him on the last piece of the bridge.

No one spoke for a while.

Then Vorrakai said, I do not know how to be judged by those who will die before understanding me.

Mara thought of every immortal arrogance she had learned to hate, then heard the fear beneath it. To a dragon who had watched generations vanish between one grief and its echo, mortality itself must have looked like a court with no memory.

"Then be judged in pieces," she said.

His eyes narrowed.

"Not one final sentence. Not one eternal prison. Not one acquittal because your pain was old. Pieces. By those harmed. By those who inherit the harm. By dragons. By mortals. By the dead who choose to testify and the living who have to deal with what testimony costs."

That is chaos.

"Yes."

His mouth curved faintly, not quite a smile. You have become consistent.

"I am horrified too."

Veyrasha stepped onto the bridge fragment, claws careful around cracks. "Dragon courts will answer for what was done with Othrava's body."

Ilyr added, "Mortal records will answer for cages built from dragon fear."

Saelith said, "Songs will answer for making grief too beautiful to interrupt."

Caldus said, "Oaths will answer for calling emergency eternal."

Kesh said, "Roads will answer for selling exits."

Tavi said, "Engines will answer for hiding operators behind diagrams."

Brakka said, "Bridges will answer for weight assigned by worth."

Sava opened her blank page. Her hand trembled. "Witness will answer for keeping the dead too useful."

Vorrakai looked at Mara last.

And you?

Mara almost said witness. The word had saved her before. It could become a hiding place now.

"I answer for every time refusing a crown made me proud enough to stop listening," she said.

That reached him.

Not because it was large. Because it was small enough to be true.

Vorrakai lowered his head.

I choose waking, he said, and every living thing on the bridge recoiled. For trial. Not rule. Not counsel. Not mercy. Trial.

Othrava's light sharpened.

Then you wake bound by answer, not chain.

The distinction cut the last strand of the old lock.

Vorrakai's body dissolved into seven dark sparks and a thousand gray ones. The seven went to no one. They hung above the broken bridge, waiting for courts not yet built. The thousand scattered into the world, each carrying not power but charge: a question that would not let any people pretend the final villain had carried all their guilt away.

Mara understood then that victory had become heavier, not lighter.

The Death-Dream let them fall.""",
    334: r"""Mara kept one onion skin.

She did not know why at first. It clung to her thumb after the peeling, thin as old parchment, gold-brown, ordinary enough to be dismissed. She almost brushed it into the soup scraps. Instead she folded it into the Kell cloth at her wrist.

Saelith noticed because Saelith noticed the things Mara tried to hide by making them small.

"Relic?" she asked.

"Absolutely not."

"Good."

"Reminder."

"Of?"

Mara looked across the camp at all the work that had no interest in becoming legend: people chopping wood, hauling water, arguing over ward terms, relabeling dead relics, repairing wheels, asking undead witnesses whether they wanted another hour, teaching children not to touch glowing objects without permission, and ruining three batches of lentils before Lora noticed.

"That the world after magic smells like onions," Mara said.

Saelith leaned against her. "Less poetic than expected."

"Better for us."

The onion skin stayed in the cloth. Later, when people asked what token Mara carried from the breaking of the old covenant, she would show them ash scars, road dust, and if she trusted them, one brittle scrap from the morning she learned that not becoming a crown required doing something with her hands.""",
    335: r"""Caldus kept the first oath draft with every ugly correction.

Sava offered to make a clean copy. He refused so quickly she looked offended.

"Clean copies are for after we remember what they hide," he said.

The page had soup stains, child handwriting, a smear of blood from the ridge rescue, three contradictory definitions of emergency, and one line where Kesh had written absolutely not beside a proposed clause allowing commanders to suspend witness for road security. The paper looked less like law than a fight that had run out of breath.

Caldus folded it into his shield beside the fever names.

"That will not preserve well," Tavi said.

"Neither do people," he answered.

No one improved the sentence. It did not need improving.

Later, Teren asked for a copy after all.

Caldus handed him a blank page instead.

"Write your own with the people who can answer it," he said.

Teren looked down at the blankness like a man facing an enemy without armor. Then he went to find the High Ford woman, which was the first wise thing Mara had seen him do without being cornered by catastrophe.

Blank pages, she was learning, could be heavier than shields.

They also left room for the next person to refuse being summarized.

That, too, was law beginning badly enough to live.

Again mattered.""",
    336: r"""That night, the grove's quiet ended by accident.

Someone hiccuped.

It was a small sound, probably from a child who had eaten too quickly. In the old Lumenorath, an accidental sound during consented quiet would have drawn correction, then shame, then the soft social machinery that taught bodies to become decorative. Here, everyone froze from inherited habit.

Then Elianth hiccuped too.

On purpose.

The grove went absolutely still.

Kesh whispered, "I may forgive her."

Children began laughing first. Then singers. Then the Orrowen mother. Then Saelith, so hard she had to sit down in the mud. The quiet did not survive. The consent did. When laughter faded, the grove asked again, and this time the quiet that followed had room inside it for bodies that made noise.

Mara decided that was worth a blossom.

The grove apparently agreed.

The next blossom opened near Elianth's knee.

She stared at it with an expression so nakedly uncertain that Mara almost looked away. The old cantor had spent a lifetime knowing which notes made flowers answer. This one had opened for a hiccup, a laugh, a quiet asked twice, and the humiliating survival of bodies. It was not a language she could master quickly.

"I do not know what it wants," Elianth said.

The Orrowen mother sat beside her. "Good."

"Everyone keeps saying that."

"Everyone is enjoying your discomfort."

Elianth gave a startled laugh, then covered her mouth as if the sound had escaped without permit. The blossom did not close. It leaned toward her, patient and impertinent.

Saelith watched from Mara's shoulder. "She is learning."

"So are you."

"I know. I hate it less today."

Mara looked at the grove, then toward the oath hall, then beyond the camp where roads waited for rules and Khar Veyl waited for public dark and Kell Ashgate waited for whatever came after being loud enough to hear itself. Victory had not made the world simple. It had made simplicity harder to defend.

That felt, in the cold evening, like a miracle small enough to trust.""",
}


BANNED_SCAFFOLD = (
    "The chapter's truth settled slowly",
    "Trouble came wearing the local weather",
    "did not reveal itself all at once",
    "When the attack came",
    "purpose was clear enough",
    "remained before them",
    "under it all",
    "Book Three is",
    "shape of Book Three",
)


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
        if chapter_no in WORD_FLOOR_DEEPENING:
            replacement += "\n\n" + WORD_FLOOR_DEEPENING[chapter_no].strip()
        extra_key = chapter_no + 100
        if extra_key in WORD_FLOOR_DEEPENING:
            replacement += "\n\n" + WORD_FLOOR_DEEPENING[extra_key].strip()
        second_extra_key = chapter_no + 200
        if second_extra_key in WORD_FLOOR_DEEPENING:
            replacement += "\n\n" + WORD_FLOOR_DEEPENING[second_extra_key].strip()
        third_extra_key = chapter_no + 300
        if third_extra_key in WORD_FLOOR_DEEPENING:
            replacement += "\n\n" + WORD_FLOOR_DEEPENING[third_extra_key].strip()
        text = text[:start] + replacement + "\n\n" + text[end:].lstrip()
        matches = list(pattern.finditer(text))
        by_no = {int(m.group(1)): m for m in matches}
        back_matter = re.search(r"(?m)^## Back Matter\b", text)
    return text


def normalize_part_headings(text: str) -> str:
    text = re.sub(r"\n# Part VI: The Covenant After Fire\n+", "\n", text)
    chapter_34 = "## Chapter 34: The Morning After Magic"
    return text.replace(chapter_34, f"# Part VI: The Covenant After Fire\n\n{chapter_34}", 1)


def check_scaffold(text: str) -> None:
    for phrase in BANNED_SCAFFOLD:
        if phrase in text:
            raise ValueError(f"Scaffold phrase still present: {phrase}")


def update_metadata(word_total: int) -> None:
    meta = METADATA.read_text(encoding="utf-8")
    meta = re.sub(r"produced_word_count: \d+", f"produced_word_count: {word_total}", meta)
    meta = re.sub(r"at_300_words_per_page: \d+", f"at_300_words_per_page: {round(word_total / 300)}", meta)
    meta = re.sub(r"at_275_words_per_page: \d+", f"at_275_words_per_page: {round(word_total / 275)}", meta)
    meta = re.sub(r"at_250_words_per_page: \d+", f"at_250_words_per_page: {round(word_total / 250)}", meta)
    meta = re.sub(
        r'current_form: ".*"',
        'current_form: "full-length draft zero with Book Three chapters 1-36 revised in pass 01"',
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
    total = word_count(revised)
    if total < MIN_WORDS:
        raise ValueError(f"Revision would reduce Book Three below {MIN_WORDS:,} words: {total:,}")
    check_scaffold("\n\n".join([*CHAPTERS.values(), *WORD_FLOOR_DEEPENING.values()]))
    MANUSCRIPT.write_text(revised, encoding="utf-8")
    update_metadata(total)
    update_summary(total)
    print(f"Book Three chapters 33-36 revised. Word count: {total}")


if __name__ == "__main__":
    main()
