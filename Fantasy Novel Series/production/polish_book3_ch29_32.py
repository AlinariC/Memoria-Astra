#!/usr/bin/env python3
"""Revision pass 01n for Book Three chapters 29-32.

Replaces the Death-Dream champion scaffold with bespoke battle, party-fracture,
Arveth's chosen rest, Mara's no-crown temptation, and the living world's answer.
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
    29: r"""## Chapter 29: Champions of the Choir

The champions crossed the dark plain without footfalls.

That frightened Mara more than noise would have. Armies made noise even when commanders wanted silence. Armor rang. Breath rasped. Boots found grit. Fear lived in bodies and bodies betrayed themselves. These figures moved like conclusions. Conquest in the clean crest, Sacrifice beneath white flowers, Obedience with bells turning in its ribs, Vengeance carrying a red knife and a witness ledger, Stillness with empty hands and a chair from Edda Mar's kitchen. Behind them dragged the older answers of the first age: Chain, Crown, Closed Road, Corrected Song, Sealed Record, Perfect Engine.

Not monsters.

Answers that had forgotten how to end.

"Formation," Caldus said.

Then he stopped.

Mara saw the word catch in him. Formation was not wrong. Formation kept people alive. Formation had also been the first small shape of every command that wanted to continue after danger passed. His hand tightened on the wooden practice sword from Stillness, then loosened.

"Brakka takes weight," he said. "Unless she tells us no. Kesh, find us a road that can close behind only if you choose it. Saelith, break any rhythm that starts deciding for us. Ilyr, record what we become tempted to hide. Tavi, name harm before your tools get clever. Sava, write who objects. Mara..."

He looked at her and did not say lead us.

The omission steadied her.

"Mara," he finished, "stay answerable."

"That is the least inspiring battle instruction I have ever received," Kesh said.

"Good."

Conquest reached them first.

It wore Caldus's restored crest, blue enamel whole, silver lion bright, armor unscarred by exile or fever bridges. The champion lifted a sword so clean it reflected no bodies. Around it rose ranks of possible soldiers: Harrowmere knights, light-elf riders, dark-elf spear shadows, goblin scouts, gnome artillery crews, troll shield-bearers, dead cavalry, and young recruits from futures where Caldus had won quickly enough to build schools afterward. They charged in perfect order.

Caldus met them with a broken shield and bad knees.

The first impact rang through the plain. He slid backward three steps, teeth bared, but he did not plant himself as the only wall. "Brakka!"

Brakka moved in from the side and took the weight of the second rank, maul horizontal like a bridge beam. "Too much on one span," she growled.

"Then redistribute," Caldus said.

He ducked under the clean sword, struck the champion's knee with the wooden practice blade, and shoved command sideways. Brakka took three attackers. Kesh opened a road under two more and dropped them into a loop of their own marching feet. Tavi threw a pressure flare stamped KNOWN STRESS and made a perfect phalanx discover steam. Saelith sang a note just wrong enough that the ranks turned on different beats. Ilyr read names from the shield backs until the soldiers hesitated to step over the bodies their victory had hidden.

Conquest raised its sword toward Caldus's throat.

"One order," it said in his voice, clean and younger. "One road. One victory. You know how many die while everyone consents?"

"Some," Caldus answered.

The champion smiled.

"And if you command?"

"Others. Where I do not have to watch."

He dropped his shield.

Mara shouted before she could stop herself.

Caldus did not need rescue. The shield fell face-up, names burned inside it, and the soldiers behind Conquest saw themselves reflected in the hidden record. Not as ranks. As persons. A dead cavalry girl lowered her spear. A goblin scout stepped out of line because the route ahead smelled wrong. A troll shield-bearer refused to take weight without asking who had loaded the bridge. The formation rippled.

Conquest struck Caldus across the chest.

He went down.

Brakka roared and would have crushed the champion's skull, but Caldus caught her ankle.

"Pass it," he gasped.

"What?"

"The fight."

Brakka understood. She did not kill Conquest for him. She pinned the clean sword under her maul and shouted, "Kesh!"

Kesh cut the road beneath the champion's feet. Tavi vented steam through the crack. Saelith shattered the march rhythm. Ilyr named the bodies. Sava wrote, Command transferred under protest from all tyrants present. Arveth's mark flared approval so bright the page smoked.

Mara spoke only one sentence: "Caldus chose not to stand alone."

Conquest cracked from crest to throat.

It did not die. It became smaller. A tool instead of a master. It fell into Caldus's broken shield as a blue shard no larger than a coin, still dangerous, still useful if held with both history and doubt.

There was no time to celebrate.

Sacrifice opened its flowers.

White petals spilled across the battlefield and became bandages, shrouds, bridal veils, altar cloths, surrender flags, funeral sheets, and the pale underside of every hand lifted to say take me instead. The champion walked through them carrying Mara's beautiful dead body, the version from the District of Sacrifice with burned hands folded over a quiet heart. But now the corpse's face changed as it came: Mara, Saelith, Caldus, Tavi, Kesh, Brakka, Ilyr, Sava. Each body offered itself with perfect logic.

"One life," Sacrifice said, "properly given."

Saelith stepped forward.

Mara's whole body rebelled. "No."

Saelith glanced back. "You do not get to forbid the conversation because you fear the answer."

That was unfair. It was also true.

Sacrifice smiled with Serathiel's gentleness. "Beloved correction. You know the shape. A note can hold dissonance by spending itself. A voice can break so others do not. Your death would not be command. It would be gift."

Saelith's throat moved.

The white flowers showed Lumenorath after her death. No holy war. No Pale Remnant. No divided people wondering whether mercy had been poison in their mouths. Saelith's wrong note became doctrine, polished and safe because the woman who made it could no longer contradict her own sainthood.

Mara tasted bile.

"If you die," she said, "they will use you."

"If I live, they will use me badly and I will have to keep correcting them," Saelith answered, eyes still on the champion. "That is not a small fear."

Sacrifice held out a knife with no blood on it.

Saelith took it.

Mara reached for cinder heat. It surged eagerly, every dead name ready to protect what she loved. She could command the flowers to burn. She could stop Saelith's hand. She could make this scene end as proof that she had learned nothing.

Her hands shook at her sides.

Saelith turned the knife around and cut her own palm.

Not deep. Enough for blood. Enough for choice to become bodily and therefore no longer abstract.

"A gift can be real," Saelith said, "and still not be owed."

She pressed her bleeding palm against the corpse Sacrifice carried. The body changed again, cycling through everyone they had lost: Nera, Oren, Pell, Serathiel, Vaura, Halruun, Othrava's child, Joryn as Mara feared losing him. Saelith let each face arrive. She did not look away, and she did not step onto the altar hidden beneath the flowers.

"I will spend myself," she said. "Healing, singing, arguing, loving, failing. I will not become the clean story that spares the living from continuing badly after me."

The flowers browned.

Sacrifice slashed at her with the white knife.

Mara moved then, not to command, but to interpose a person where a person could be. The blade cut her sleeve. Caldus, still half-kneeling, knocked the champion's wrist aside. Tavi tossed Saelith a strip of cloth and shouted, "Wrap dramatic theology before it gets infected." Kesh kicked petals into the champion's face. Brakka took the corpse from Sacrifice's arms and laid it down gently, because even a false body deserved better than being used as leverage.

Saelith sang.

The note was not ugly this time. It was beautiful and brief. It ended before beauty could become law.

Sacrifice collapsed into a single white petal marked freely given, not universally owed. Saelith tucked it into her belt with a face that said she would argue with it later.

Obedience rang.

The sound split the company.

One bell became two, two became four, four became a city of tones. Every tone assigned a role. Caldus to defense. Brakka to weight. Tavi to mechanism. Ilyr to shadow. Kesh to edge. Saelith to mercy. Sava to record. Mara to witness at the center, useful and still.

Their feet moved before their minds could catch up.

Mara felt her body take its assigned place. It was efficient. Beautifully efficient. The champions of Chain and Perfect Engine turned toward them, delighted by all that readiness. If she stood exactly where Obedience placed her, she could hear every cinder in the battlefield. She could witness without moving. Others could fight around her. The living world would be organized around the one person who could bear the final answer.

No crown, she thought.

The bells corrected her posture.

Ilyr broke first.

Not free. Broke. His role was shadow, and shadow had old muscles in him. The bells gave him back a perfect Khar Veyl exile position: unseen, necessary, deniable. He could cut the bell-chain from hiding and save everyone without being answerable for what else his blade struck.

Instead he stepped into full view.

The effort made him gasp.

"Public correction," he said, and drove his shadow blade not into a bell but into its inscription.

The bell read EACH GIFT RIGHTLY PLACED.

He added BY WHOM?

The note went sour.

Sava, trapped in record-stance, began writing objections on her own sleeve because the register was pinned by bell-order to her hands. "Minutes object to being minutes only. Secretary objects to being handwriting with shoes. Arveth objects preemptively to whatever I am about to do."

Arveth's mark, bound flat on the page, scratched three letters.

Yes.

Sava screamed, not in fear but effort, and slammed the register shut on a bell tone.

The sound broke.

Kesh stumbled free and immediately chose a different edge than the one assigned. "I claim this edge. It is worse."

Tavi moved away from the Perfect Engine though every part of her wanted to see how it worked. Brakka stepped off the load-bearing line. Caldus lowered his shield. Saelith let her healing song miss a beat.

Mara took one step from the center.

The battlefield lurched.

Obedience's bells fell from its ribs and became small, frantic mouths. "Without roles, you lose."

"Probably," Mara said.

That answer hurt the champion more than defiance.

Vengeance used the opening.

The red knife came for Kesh from behind, wearing the face of every person he had named in the ravine, and every person he had not yet found courage to name. He turned too late. Ilyr shoved him aside and took the cut across his shoulder.

Kesh swore so violently one of the bell mouths shut itself.

"I did not ask you to become heroic at me."

"It was not heroism," Ilyr said through clenched teeth. "It was proximity."

Vengeance smiled. "Then name the price."

The plain became roads.

Not one road. Hundreds. Ravine roads, refugee roads, market roads, corpse roads, school roads not built yet, secret roads used to save people, secret roads used to sell them. Kesh stood at their crossing with the red knife in his hand now. Vengeance did not force it there. It merely reminded his fingers how knives worked.

"Choose who pays," it said. "A road always costs someone. You have only become honest enough to make the bill public."

Refugees appeared on one road. Rikka on another. Children from the dead woman's ravine. Goblin road captains who had profited and road children who would starve if every clever bargain were forbidden. Kesh's face went blank in the way Mara had seen before a joke became a wall.

Mara started toward him.

The Closed Road snapped shut between them.

Kesh did not look back.

He drove the knife into his own route token.

Green light and red verdict wax exploded outward. Every road on the plain flared with maps, not ownership marks but warnings, histories, debts, names of the dead, names of the living who had repaired and those who had not. The token cracked across its center. Kesh hissed as if something under his ribs had cracked with it.

"I do not choose who pays in secret," he said. "I publish the road and let travelers curse me with directions."

Vengeance cut him anyway.

Blood ran down his side. Not fatal. Not clean. A cost that did not flatter itself.

Brakka reached him first, because she had chosen the middle and the middle was sometimes nearest every disaster. She put one huge hand on his back and one on the road knot.

"Open enough," she said.

The roads held.

Vengeance broke into a red sliver marked consequence must face repair. Kesh caught it, cursed at it, and stuffed it into his cracked token.

The champions had lost four shapes.

Stillness remained.

It had not moved.

That was why it won.

While the others fought, Stillness had walked through the counter-choir with empty hands and asked the question no weapon could answer: Are you tired?

Bone lanterns dimmed across the plain.

Some had chosen waking in the gray district. Choosing once, Mara realized with cold horror, did not bind a person forever. Consent had to remain alive or it became another chain. The dead could be asked again. The living too.

Stillness knelt before a lantern whose flame Mara knew by its scratchy mark, by its bad timing, by the impossible nuisance of it.

Arveth.

Sava saw and ran.

Too late.

The gray champion touched the lantern.

The battlefield vanished.

Mara fell into a courthouse made of pages.""",
    30: r"""## Chapter 30: Arveth Chooses Rest

The courthouse had no walls.

It had margins.

They rose around Mara in columns of paper, each sheet written on both sides, footnoted, objected to, amended, stained by thumbprints, scored by claws, burned at edges, kissed by rain, and once, inexplicably, annotated with a recipe for lentils. Pages flew overhead like frightened birds. Others settled into benches where the company found themselves seated apart, each behind a desk too large for comfort. The floor was black ash polished to a mirror, and beneath it slept the faces of the dead who had given testimony since the first burned hill.

At the front stood a judge's chair.

It was empty.

That was the trap.

Sava stood before it with the register clutched to her chest. She looked younger than she was, or perhaps only more openly the age she had been when she first learned that good handwriting could make powerful people mistake her for furniture.

"Arveth," she said.

The register did not answer.

Stillness stood beside the empty chair, gray hands folded. No threat. No weapon. The champions of Conquest, Sacrifice, Obedience, and Vengeance had attacked as arguments with blades. Stillness knew better. It waited like a room after grief has left no one with strength to keep shouting.

Pages gathered in the judge's chair.

They became Arveth.

Not the lantern flame. Not the skeletal, papery voice that had insulted bad procedure from the safety of death. A man. Thin, sharp-nosed, dark-skinned, hair gone silver at the temples, ink stains on his cuffs, one shoulder crooked from an old beating, eyes alive with the terrible pleasure of finding a flaw in an argument everyone else had praised. He looked at his own hands as if hands were an unexpected administrative burden.

"Oh," he said.

Sava made a sound between sob and laugh. "You have a face."

"I have always had a face."

"You had a mark."

"A mark is a face optimized for people with limited patience."

She laughed then, and the courthouse pages fluttered.

Mara rose from her desk. A chain of footnotes snapped around her wrist and pulled her back down. Every desk had restraints made from cited precedent. Caldus strained against a ribbon of command doctrine. Saelith's hands were bound in healing vows. Ilyr's chair was locked by sealed context. Kesh's by unpaid debts. Tavi's by safety specifications. Brakka's by load tables. Each restraint was partly true, which made it hold.

Stillness addressed Arveth.

"You have served."

Arveth glanced at Sava. "That word always arrives wearing someone else's boots."

"You have witnessed."

"Yes."

"You have objected."

"With distinction."

"You have been used by kings, councils, refugees, corpses, rebels, courts, and one ash-runner who keeps mistaking refusal for a complete theory of governance."

Mara tried to object and found a footnote in her mouth.

Arveth gave her a look. "It is not entirely inaccurate."

Stillness lifted one hand.

The courthouse opened into every hearing Arveth had ever entered: a village court where plague widows were fined for unlawful burial; a goblin compact tribunal where route theft was called market correction; a light-elf chapel where mercy was entered as evidence against the dead; a dark-elf archive hearing where sealed truth learned to wear patience as camouflage; a troll bridge moot where weight was assigned to status instead of stone; a dragon judgment where the harmed were named, then filed away for later convenience.

In each scene, Arveth objected.

Sometimes he won.

Usually he did not.

The pages showed the cost. The beating that crooked his shoulder. The prison fever. The friends who stopped inviting him because dinners became cross-examinations. The spouse who loved him, left him, and wrote one letter that said, I cannot build a home inside your perpetual appeal. The apprentice who died carrying a petition Arveth had drafted too cleverly for guards to ignore. The final hearing where he refused to let a court erase the dead from a famine record, and the court solved the difficulty by making him one of them.

Mara had known Arveth as dead.

She had not known how tired a dead man could be before dying.

Stillness spoke with almost unbearable kindness.

"Enough."

The word moved through the courthouse like sleep.

Arveth closed his eyes.

Sava clutched the register harder. "No."

His eyes opened.

The word had struck him, but her voice did too.

"No is an insufficiently specific pleading," he said, softly.

"Then specific no. You do not get to vanish because a gray-robed horror with excellent courtroom acoustics tells you your work is done."

"It may be done."

Sava shook her head. "It is not."

Pages stirred.

Stillness did not interrupt.

That was crueler than argument. It let Sava hear herself.

She looked at the register, at all the marks Arveth had scratched through impossible roads. "You taught me that testimony matters."

"Yes."

"You taught Mara that personhood is maintained."

"A phrase I regret making memorable."

"You taught Caldus that law must face the people it burdens. You taught Ilyr that records can become cages. You taught Kesh that debt without names is theft in nice shoes. You taught me to object when minutes become burial."

"Then I have multiplied adequately."

Sava went still.

Arveth smiled sadly. "Ah. There it is."

"What?"

"You heard yourself. You listed what continues."

Stillness held out both hands. In one lay rest: not erasure, not prison, not forced silence. Rest chosen after work entered the world through other mouths. In the other lay eternal witness: Arveth preserved as perfect objection, painless, tireless, available to every court forever. The second hand shone brighter.

Mara understood the trap with a grief that made her ribs ache.

The danger was not Arveth choosing rest. The danger was the living refusing to let him because they had become better with him available.

Sava understood too.

Her face broke.

"That is unfair," she whispered.

Arveth stepped down from the judge's chair. As he moved, the restraints around the company loosened enough that Mara could stand. No one rushed forward. The courthouse had taught them at least that much. Love could become command if it reached too quickly.

Arveth stopped before Sava.

"I am afraid," he said.

She cried harder.

"Not of rest," he continued. "Of being made useful after my usefulness should have ended. That is a very embarrassing fear for a man of my principles."

Sava laughed once through tears. "Your principles are exhausting."

"Correct."

"I do not want you to go."

"Also correct."

"I still need you."

"There we must be careful."

The pages overhead slowed.

Mara saw the whole counter-choir reflected in the ash floor: dead witnesses who had chosen to continue because someone living needed them, dead witnesses who had chosen rest, dead witnesses uncertain because usefulness had become the only proof anyone remembered them by. Vorrakai's mercy waited behind Stillness, ready to say: See? The living love the dead into labor. I only end the abuse.

Mara could not let him own that truth.

"Arveth," she said.

He turned.

"What do you want?"

The courthouse trembled. It had expected arguments about need, duty, timing, strategy, the battle still raging beyond the margins. It had not expected the simplest question to arrive without disguise.

Arveth considered it with the seriousness of a legal principle.

"I want my testimony to remain available," he said.

Sava inhaled hope.

"And I want not to be trapped inside its availability."

The hope changed shape.

"Can both be true?" Mara asked.

"They had better be," Arveth said. "Otherwise every archive is a mausoleum with delusions of civic virtue."

Ilyr, still half-bound at his desk, whispered, "Insufferable."

"Accurate," Arveth said.

Tavi raised one hand as far as her specification chains allowed. "Can we build a release mechanism?"

"No mechanisms," Saelith said, voice hoarse. "A ritual. Mechanisms pretend maintenance is enough."

Brakka leaned forward until her load-table bindings creaked. "A bridge with a removable center stone. Cross when called, return when chosen."

Kesh sniffed. "A route marker that says road ends here unless the traveler repaints it."

Caldus looked at the judge's chair. "An oath that expires unless renewed aloud."

Sava opened the register.

This time no mark moved her hand.

She wrote: Testimony remains. Witness released. Future invocation by consent only, with standing right to refuse, mock, or ignore bad procedure from beyond reach.

Arveth read over her shoulder.

"Comma after refuse."

Sava sobbed and laughed. "That is your final contribution?"

"No. Merely the most urgent."

Stillness shifted.

For the first time, the gray champion looked less like kindness and more like hunger denied a clean plate.

"Pain will return," it said.

Arveth nodded. "Almost certainly."

"Courts will lie."

"Constantly."

"The living will fail your work."

"They already have. I left notes."

Stillness looked at Mara. "You call this mercy?"

Mara looked at Sava, who held the register like a wound she had promised not to close with someone else's body. She looked at Arveth, afraid and relieved and almost unbearably alive for a man already dead. She looked at the company, bound by partial truths they would keep having to loosen. She looked at the ash floor full of faces.

"No," Mara said. "I call it asking."

Sava read the release aloud.

The courthouse pages rose.

They did not burn. They did not vanish. They multiplied. Copies flew outward through the Death-Dream, through the Dead Capital, through bone lanterns, through court ledgers, road compacts, bridge stones, archive boxes, song roots, engine plates. Arveth's objections scattered into the world as tools no one could mistake for his continued imprisonment. Some pages folded into birds. Some into ash. Some into small rude marks in margins where future clerks would feel suddenly less alone.

Arveth put one hand over Sava's.

"You will do this badly at first," he said.

"I know."

"Good. Anyone who begins well has usually hidden the difficult part."

She nodded.

"Do not make me a saint."

"Never."

"Do not make me a system."

"Absolutely not."

"Do, occasionally, quote me accurately."

She smiled through tears. "You ask too much."

He looked at Mara.

"Little witness."

Her throat closed.

"You are still attempting to become the exception to every danger you name."

She barked a laugh that hurt.

"Stop that," he said gently. "Exceptions are where crowns hatch."

Then he stepped backward.

Sava let him.

That was the heroism of the chapter. Not blade, not song, not cinder fire. A young woman unclenching her hands because love had been asked to stop short of ownership.

Arveth sat in the empty judge's chair.

Not as judge.

As a tired man accepting a seat.

His body became pages. The pages became birds. The birds became ash. The ash settled into the register as one final mark: a small, crooked objection sign, crossed by a line that meant closed by consent.

The restraints fell away.

Sava made no sound.

Mara went to her.

This time, reaching was not command. Sava folded against her and shook.

Stillness watched them, diminished but not destroyed. "You will miss him."

"Yes," Sava said into Mara's shoulder.

"You will call and he will not answer."

Sava lifted her head. Her face was wet, furious, young, and older than it had been when the courthouse opened.

"Then I will decide without making a corpse do my courage for me."

The gray champion cracked.

It did not shatter. A piece of it slipped into the register beside Arveth's mark, labeled rest requires release as well as memory.

The courthouse margins tore.

The battle returned in pieces: Conquest's shard flashing on Caldus's shield, Sacrifice's petal at Saelith's belt, Vengeance burning in Kesh's cracked token, Obedience bells scattered under Ilyr's boots, Chain thrashing across the plain, Crown rolling toward Mara with every cinder-name in Vael Taryn glowing along its rim.

Vorrakai stood beyond the Crown.

He had waited while Arveth chose.

Mara hated him for that courtesy and understood exactly why he had given it.

His voice filled the torn courthouse and the battlefield beneath.

You have freed one witness. Will you free all by refusing the throne, or will you admit that even your refusal requires someone to hold the final power?

The Crown Without Head opened.

Inside it was a throne made of warm names.

Every cinder answered Mara at once.""",
    31: r"""## Chapter 31: No Crown of Cinders

The throne was not made for sitting.

It was made for ending hesitation.

It rose from the Crown Without Head in rings of ash-gold, dragon bone, oathstone, shadowglass, white root, road knots, brass rivets, old iron, and pages from every testimony the world had failed to honor quickly enough. Names burned across it, not carved but alive. Kell Ashgate miners. Harrowmere fever dead. Orrowen's numbered children. Lumenorath singers who had swallowed doubt until it poisoned them. Khar Veyl archivists who had died trying to open a record one day too late. Goblin road families. Troll bridge-kin. Gnome apprentices. Dragonlings. Soldiers. Monsters. Kings. Servants. The guilty. The harmed. The ones who had chosen rest. The ones who had chosen waking and already regretted the work.

Warm names.

That was the cruelty.

Mara had expected power to feel cold, like Vorrakai's still mercy, or hot, like command cinders under Mordane's crown. This felt like hands reaching from a crowd, not to seize her but to be held. Every name on the throne wanted something reasonable. Do not let them forget me. Do not let this happen again. Do not leave the next frightened council to invent a chain because no one strong enough stopped them. Do not waste what I suffered by giving the living another chance to fail.

The cinders of Vael Taryn answered through her bones.

Not as tools.

As persons asking to matter.

Mara fell to one knee.

Saelith cried her name, but the battlefield stretched the sound until it arrived from very far away.

Vorrakai stood beside the throne. In this place, he was neither corpse nor dragon nor moon-shadow, but a figure shaped from the first age's grief. Star-black scales ran along his arms. His face held the young judge and the dead god at once. His eyes were winter rivers under a sky that had forgotten dawn.

"No chain," Mara said through her teeth.

He inclined his head. No chain.

"No command engine."

No engine.

"No stillness."

Not imposed.

She looked up sharply.

Vorrakai's voice softened, and that softness was the edge. You have taught me your vocabulary. Consent. Review. Release. Names asked individually. Very well. Take the throne and make those principles law no future fear can overturn.

The throne opened.

Mara saw what he offered.

Not tyranny as she had imagined it. Not dead stillness falling across the world. A corrected mercy, built from everything she had survived. Cinders would no longer be commanded by crowns or engines, but held in a witness compact she alone could anchor. Dead persons could choose rest or waking and renew that choice. Courts could not seal records without cinder witness burning the lie. Roads could not be sold in secret. Bridges could not deny weight by worthiness. Songs could not erase grief. Leaders could not order conquest without the hidden bodies appearing in every shield. Sacrifice could not become holy without consent tested beyond terror. Vengeance could not continue past repair. Obedience could not assign roles without review.

It was, in every visible way, better than the world.

Mara's breath came apart.

"You can do this?" she whispered.

With you, yes.

"And without me?"

Vorrakai did not answer.

The silence was honest enough to hurt.

The company fought below the throne's rise. Caldus held the Chain with Brakka, passing strain between shield and maul. Tavi crawled along the Perfect Engine's flank, carving failure labels into plates while gears tried to persuade her they had already accounted for everything. Kesh kept roads open with a broken token, bleeding each time someone crossed without permission from the Closed Road. Ilyr and Saelith stood back to back inside a storm of bell mouths and corrected notes, making disorder deliberate enough to survive. Sava guarded the register against Sealed Record, which offered to preserve Arveth perfectly if she only let the release clause become ceremonial.

They were losing.

Not dramatically. Honestly. Piece by piece. People with bodies tired. Principles under pressure bent. Every answer they had won in the Dead Capital required maintenance under impact, and impact did not pause for maintenance.

Mara looked at the throne.

If she took it, she could save them.

That was true.

She felt Arveth's absence like a hand not taking hers.

Exceptions are where crowns hatch.

"I am not an exception," she said.

Vorrakai's eyes narrowed. You are the only one who can hear them all.

"That is not the same."

You are the only one who has refused every false ending.

"Because people kept pulling me back, arguing, bleeding, insulting me, feeding me, refusing me, leaving me, choosing without me."

The throne pulsed. Names pressed closer, frightened by her refusal. Not commanding. Begging. Mara almost broke under the decency of it. How dare power be offered through need instead of vanity? How dare the throne contain the voices of people who had every right to want a world finally prevented from harming anyone else?

A miner's voice rose from the warm names.

Little ash-runner. We trusted you.

Mara's hands clenched.

Joryn's almost-voice came next, not from Stillness now, but from the part of her that remembered sharing bread under a leaking roof.

Eat first, then argue.

She almost laughed.

"I cannot eat if I become furniture."

Vorrakai stared.

The throne shuddered, confused by the shape of the refusal.

Mara stood.

"I will not be ruler."

The throne's names cried out.

"I will not be martyr."

Sacrifice's white petal flared at Saelith's belt far below.

"I will not be jailer, engine, bridge that carries all weight, road everyone must travel, record no one can revise, song no one can interrupt, judge who never leaves the chair."

Each sentence tore something from her. Not power. Want. The want to be enough. The want to stop watching friends bleed because her principles refused the fastest tool. The want to honor the dead by making their pain impossible to repeat. The want to be loved because she had finally become useful at the scale of the whole world.

Vorrakai's grief struck her.

Then what are you?

Mara looked at her hands.

Burned. Shaking. Empty.

"A witness," she said.

Too small.

"Yes."

Too late.

"Often."

Too weak.

"Alone, yes."

The throne snapped forward like a mouth.

Names wrapped around Mara's wrists. Not chains. Pleas. That made them harder to resist. She felt herself drawn toward the seat. If she sat, even for a breath, the cinders would align. She could issue one command shaped as consent. One perfect law against future crowns. One final safeguard. She could step down after. Surely she could step down after.

The thought smelled like verdict wax.

Mara screamed.

Not for power.

For help.

It was the least heroic sound she had made in three books and therefore one of the truest.

Saelith heard her.

So did everyone.

The battle below changed because Mara had not made herself unreachable.

Caldus abandoned the Chain at the worst possible moment and trusted Brakka to say whether she could hold it. "Can you?"

"No," Brakka grunted.

He turned back.

"But I can hold long enough," she said. "Go."

Caldus went.

Tavi leapt from the Perfect Engine before finishing her diagram and let a flaw remain unnamed because Mara was more urgent than completeness. Kesh opened a road that cost him a memory of Rikka's laugh; he cursed and opened it anyway. Ilyr left a record half-written. Saelith broke a beautiful note in the middle. Sava slammed the register into Sealed Record's drawer and shouted, "Released witnesses do not answer summons by emergency!"

They came up the throne's steps not as army, not as chosen council, but as a mess of people arriving badly and in time.

Caldus cut the name-pleas from Mara's left wrist with the wooden practice sword. It broke.

"Worth it," he said.

Tavi jammed her damaged perfect screw into the throne's hinge. "No system closes without showing wear."

Kesh tied his cracked route token around Mara's right wrist. "You are allowed exits."

Ilyr pressed Vaura's childhood pearl and charge-page into the throne's names. "Context. Not absolution. Also not fuel."

Brakka planted her maul at the base. "No bridge loads without consent from the span."

Saelith put her bleeding palm over Mara's heart. "No gift owed."

Sava opened the register to Arveth's closed-by-consent mark. "No witness kept past choosing."

The throne fought them.

Every name cried louder. Some in anger now. Some in fear. Some because Mara's refusal felt like abandonment to the dead whose suffering had bought her wisdom. She could not answer all of them with comfort. That was the truth the throne had tried to hide: no refusal worthy of the name spared everyone pain.

Mara turned toward the names.

"I hear you," she said.

The cinders paused.

"I cannot make your pain impossible to repeat by making everyone's choice smaller than mine."

You waste us, cried a dragonling.

"No."

You leave us unavenged, cried a ravine child.

"No."

You abandon the next dead, cried a fever mother.

Mara's voice broke. "I leave the living answerable to you. That is not enough. It is what I have."

The throne bucked.

Vorrakai's wings filled the sky.

You have learned nothing from history.

"I learned that every answer becomes a monster when it cannot be refused."

She reached into the throne, not for command but for the place where names touched one another. The cinders surged. For one awful breath, all Vael Taryn entered her: every dead city, every dragon memory, every crown, road, bridge, engine, record, song, knife, field, kitchen, court. It should have killed her. It might have, if she held it.

She did not hold it.

She opened her hands.

The names spilled outward.

Not uncontrolled. Witnessed. Each cinder flew to the person or place that had consented to carry part of the answer: to Caldus's shield shard, Saelith's petal, Ilyr's record, Kesh's route token, Brakka's maul, Tavi's damaged screw, Sava's register, bone lanterns that still chose waking, bridge stones, road marks, opened archives, flawed songs, ordinary living hands beyond the Death-Dream.

Power distributed itself badly, unevenly, reviewably.

The throne cracked.

Vorrakai recoiled.

For the first time, Mara saw fear in him that was not old grief wearing law.

The warm names no longer begged from one seat.

They spoke from everywhere.

That made them harder to command.

It also made them harder to silence.

The Crown Without Head split down its center. From the crack came light the color of banked fire and morning ash. The battlefield outside the throne shook. Chain shrieked. Closed Road opened in too many directions. Corrected Song lost the note that made silence beautiful. Sealed Record spilled drawers. Perfect Engine exposed a lever labeled SOMEONE STILL CHOOSES.

Mara fell.

Saelith caught one arm. Caldus the other. Kesh complained that catching heroes should be billable. Tavi said she had witnessed worse load distribution. Brakka held the stair while the throne collapsed behind them. Ilyr kept reading names until the last cinder left the seat. Sava wrote with both hands and probably invented six abbreviations that would horrify future scholars.

Vorrakai's voice cut through the breaking dream.

If no one holds the final power, the compact will fail.

Mara looked down through the crack in the battlefield.

For the first time, she saw beyond the Death-Dream into the living world outside it.

Vael Taryn had not been waiting.""",
    32: r"""## Chapter 32: The Answer of the Living

Outside the Death-Dream, the world was making a terrible noise.

It began as a tremor under Mara's knees, then became bells, drums, horns, road songs, bridge hammers, archive gongs, forge whistles, dragon roars, goblin chimes, troll foot-stomps, gnome pressure alarms, human shouting, light-elf wrong notes, dark-elf public readings, and the thin, stubborn clatter of ordinary people banging pots because someone had once told them noise could keep fear from arranging them into silence.

The living world had not solved itself while Mara fought in the dream.

That was the miracle.

It had nearly failed in many directions at once.

Through the crack left by the broken throne, she saw the Dead Capital's gates from outside. The caravan of the unburied had become an impossible camp spread across the ash plain: tents, wagons, dragon-shadow shelters, troll stone screens, goblin road ribbons, gnome scaffolds, elven song circles, human fire lines, undead lantern ranks. The factions of Vael Taryn had arrived not as one army but as a thousand arguments with weapons attached.

The Pale Remnant tried to seize the left ridge, declaring Mara trapped in holy combat and therefore in need of purification by loyal hands. They were stopped not by Saelith, not by Mara's command, but by Lumenorath singers who stood deliberately off-key and refused the Remnant's corrected intervals. Some were light elves. Some were dark. Some were humans with terrible pitch and magnificent volume. Auralian, robe still unhemmed, led them badly enough to save them.

Khar Veyl record-keepers tried to seal the Death-Dream breach for study, because terror often wore scholarship when it wanted a lock. Maelin broke their seal boxes with a hammer while Ilyr's mother, gray-haired and unsentimental, read restricted precedents aloud until the keepers either backed down or found themselves entered into public objection.

Harrowmere officers attempted to form emergency command.

The fever bridge families sat in the road.

No one wanted to trample them first.

That gave Caldus's old disgraced knights time to distribute command into small circles, each with a civilian witness, a withdrawal signal, and a written expiration. Several officers hated this so much they obeyed it out of spite.

Gnome engineers looked at the dragon-moon eye opening over the Dead Capital and immediately tried to build stabilizers. Tavi's Brassroot liability code, copied badly and widely, forced them to put warning panels on every device before activation. Pinna Vey stood on a crate screaming, "Known harm first!" until three different workshops named risks they had hoped to call unlikely.

Goblin road captains argued over evacuation routes.

The dead woman from the ravine appeared in lantern smoke above their map.

Every route captain who had ever sold a path in secret went very still.

Kavik children, sharper than their elders, began painting old route-debts directly onto wagon wheels. Kesh's cracked token flared in the dream, and Mara saw him see them.

"Oh," he said, very softly.

Troll clans arrived at the gates with bridge stones on their backs. Third Arch had sent more than fighters. It had sent weight-readers. Brakka's people did not ask who deserved passage. They measured stress, named capacity, moved bodies, and shouted at anyone who tried to turn emergency into worthiness. A troll grandmother with silver rings in her ears slapped a noble's horse and told it the bridge had better manners than its rider.

Dragons circled above all of it.

For a moment, Mara feared they would become the old terror. Then Veyrasha descended to the ash plain, landed outside every marked circle, and folded her wings before speaking. She did not command. She asked where a body her size could help without crushing what it meant to save.

Othrava's moon-locked eye blazed in the sky.

The dragon body that had been used as lock, as proof, as mechanism, as moon, watched the living world answer without waiting for permission from the witness trapped inside the dream.

Mara wept.

Vorrakai saw it too.

The Death-Dream shook with his silence.

You think this proves freedom.

"No," Mara said. "It proves practice."

Below, the compact nearly failed.

Not once. Repeatedly. A Harrowmere officer pulled a sword on a goblin road captain who refused military priority. A dark-elf keeper tried to hide a casualty list until Maelin shoved him into a public reading circle. A dragon's wing gust overturned three medical tents, and frightened archers raised bows before Veyrasha apologized loudly enough to stop them. A gnome stabilizer exploded blue smoke over a group of undead witnesses, who then argued whether being smoked counted as harm if one no longer breathed. A troll bridge queue broke into pushing until Brakka's grandmother hit the ground with a staff and made everyone recite weight limits.

Every failure gave Vorrakai's argument teeth.

Every correction stole one.

Mara turned to the company.

"They are doing it."

Tavi's face was wet and grimy. "Badly."

"Yes."

"Without central design."

"Yes."

"I have never been so inspired and professionally distressed."

Kesh looked through the crack at the road children painting debts. His usual grin tried to arrive, found no room, and became something gentler. "They misspelled Serren."

Ilyr wiped blood from his chin. "Public records often begin as vandalism."

Saelith listened to the overlapping songs. "They are not in harmony."

"No," Mara said.

"Good."

Caldus watched the command circles expire and reform. "They will lose people this way."

Mara did not answer too fast.

"Yes."

His jaw tightened, then he nodded.

Brakka looked at the bridge queues. "They will save people this way too."

Sava held the register open. Arveth's released mark did not move. She read the living entries anyway, her own voice steadier than before. "Minutes note: world making ugly attempt."

The mark remained still.

She smiled through grief. "Objection not received. Proceeding."

Vorrakai rose above them.

The broken Crown shards circled him. Chain, Closed Road, Corrected Song, Sealed Record, and Perfect Engine drew back toward his body, no longer champions but arguments returning to the grief that had sent them. He looked beyond Mara to the living camp. For one breath she saw not a god or villain, but the young judge from the first age watching the council choose the slow answer and knowing it would not save everyone.

You ask me to trust what has already failed.

Mara's hands shook. "No."

The word caught him.

"I ask you to stop using failure as proof that only stillness deserves the future."

The living world answered by nearly collapsing again.

A wave of corpse-light rolled from the Dead Capital's walls, the Choir's last pressure from within. It struck the camp as memory: every person saw the worst thing their people had done and the worst thing done to them, side by side, without order, without mercy, without preparation. Light-elf singers choked on Orrowen. Dark-elf archivists saw sealed famine rooms. Humans saw crowns and fever bridges. Goblins saw sold roads. Trolls saw bridges held for the worthy and dropped for the inconvenient. Gnomes saw engines tested on those who could not sue. Dragons saw burned hills and broken chains.

The camp buckled.

Weapons rose.

The answer of the living almost became war.

Mara felt the cinders surge toward her, desperate to help. She could still command. Even after refusing the throne, enough power loved the idea of her voice. One word could freeze the camp until everyone remembered better.

She opened her mouth.

Saelith put a hand over it.

Not gently.

Mara stared at her.

Saelith's eyes were full of terror. "No."

The word held all of them.

Mara nodded once.

Saelith removed her hand.

Mara did not speak into the cinders.

She spoke through the crack, ordinary and too small for the scale of disaster.

"Ask."

The word did not command anyone.

Many did not hear it.

Some did.

Oren heard it, somehow, standing in the medical line with ash on his face. He turned to a dead soldier whose hand had closed on a spear and asked, "Do you want guard or rest?" The dead soldier stared, then lowered the spear and said, "Guard. Ten minutes. Then ask again."

A goblin child asked a human officer, "Are you protecting us or taking the road?" The officer, furious, almost lied. The fever bridge family in the road looked at him. He said, "Both," then threw up in shame and handed his command token to the civilian witness.

A light-elf singer asked a dark-elf keeper, "What record are you hiding because you think we cannot survive it?" The keeper showed her. She screamed. Then she kept singing, badly.

Veyrasha asked the archers whether her wing should move east or stay folded. They answered in panicked fragments. She waited through all of them and moved one claw-length.

Pinna Vey asked three engineers who would be harmed if their stabilizer failed. They named six groups, then seven, then one they had avoided because it made the design look worse. The warning panel changed. So did the device.

Brakka's grandmother asked the pushing crowd who could stand and who could not. People lied. Others corrected them. The bridge line changed shape.

Question by question, the corpse-light lost force.

Not because everyone became good.

Because enough people became interruptible.

Mara sagged against Saelith.

Vorrakai watched the camp survive without being saved cleanly.

The dragon-moon eye above the Dead Capital blinked.

For the first time, Othrava's voice entered the Death-Dream not as memory but as present will. It came through the eye, through river ice, storm milk, broken chain, and the immense patience of a being used as lock who had heard her own name restored.

Vorrakai.

The dead god went still.

Othrava's voice shook every shard of the Crown.

You made my body a door and called it mercy. You held my grief after killing my choice. You will not use my silence as consent again.

Vorrakai's face changed.

Mara had seen anger in him, grief, tenderness, contempt, patience. She had not seen shame arrive without defense.

Othrava continued.

I choose waking enough to answer. I choose rest enough not to become your eternal witness. I choose my name returned to me. Let the living make their ugly attempt.

The dragon-moon eye poured blue-white fire into the battlefield.

Not attack.

Witness.

Every cinder Mara had distributed answered, not to Mara, not to Vorrakai, but to the shared fact that Othrava had spoken for herself.

The Choir screamed.

It had fed on voices used after consent ended. Othrava's living answer cut through its deepest root.

Vorrakai reached toward the eye. Othrava's fire burned his claw, and he withdrew as if burned by the first true boundary he had respected in centuries.

Mara stood straighter.

"The world must choose freedom too," she said. "It is choosing badly. That still counts."

Vorrakai looked at the camp, at Othrava's eye, at the company, at the broken throne, at Arveth's silent mark, at the cinders no longer gathered where he or Mara could hold them all.

Then he did what grief does when denied its final shape.

He became enormous.

The Death-Dream tore open into the old covenant's wound. The broken Span rose from beneath the battlefield, larger than any bridge, chain, or law they had seen. Its links wrapped around sky and plain. At its far end lay Vorrakai's true heart: not in his chest, not in the moon, but in the first place he had decided no one could be trusted with fear.

Part VI waited beyond that wound.

Breaking the old covenant would not be a speech.

It would be a battle inside the first lock.

Mara looked at her friends. Not all of them whole. Not all of them ready. Arveth gone by consent. The living world noisy beyond the crack. Othrava awake enough to refuse use. The cinders scattered into accountable hands.

No hero's throne.

No clean answer.

Enough.

"Together?" she asked.

Kesh winced, one hand pressed to his side. "I hate that this remains our brand."

Tavi lifted her damaged screw like a holy tool. "I have never respected branding less."

Saelith took Mara's hand.

Caldus raised the shield with Conquest's shard set beside the fever names.

Ilyr opened the record.

Brakka set her maul on the first link of the broken Span.

Sava closed the register, then opened it again to a blank page of her own.

"Proceeding," she said.

They stepped into the wound.""",
}


WORD_FLOOR_DEEPENING: dict[int, str] = {
    29: r"""The battle did not move in a line after that.

The Death-Dream hated lines. Lines belonged to roads, chains, arguments, kings, and historians who wanted the dead to queue politely for meaning. The plain fractured into overlapping arenas, each one trying to convince a member of the company that their truest fear was also their rightful work.

Tavi fell into the Perfect Engine.

One moment she stood beside the others with a stolen first-age tool in one hand and soot on her cheek. The next, the battlefield folded around her and became a chamber of brass ribs, glass lungs, and pressure gauges large as shields. Every surface bore warning labels in her own handwriting. Known harm named. Relief valve tested. Consent interval renewed. Liability assigned. Maintenance visible. The machine had learned her ethics.

That made it worse.

At its center sat a small lever labeled PREVENT RECURRING CATASTROPHE.

Tavi laughed once. "That is not fair."

The engine answered in her aunt's voice. Fairness is a downstream metric.

It showed her Brassroot surviving every war because she had built the mechanism properly. No command engine. No hidden tests. No silenced apprentices. Every moving part accountable. Every risk named. Every harmful output assigned compensation before release. The device did not ask her to ignore harm. It asked her to believe that harm, if perfectly tracked, could be permitted to continue at scale.

Outside the chamber, Mara's scream came thin through the gears.

Tavi reached for the lever.

Her fingers stopped on the damaged perfect screw in her pocket.

The screw had a crooked slot because she had made it so. A record of use. A refusal of immaculate systems that did not show who touched them last.

"Where is the off switch?" she asked.

The engine purred. Not needed if design is correct.

"That is what I was afraid you would say."

She drove the damaged screw into the lever housing and jammed it sideways. Brass shrieked. Warnings bloomed across every panel, not prewritten but fresh. Unknown harm. Operator temptation. Ethical overconfidence. Stop pretending maintenance is morality.

The engine tried to eject her.

Tavi clung to a gauge and laughed harder, half terrified, half delighted. "I am adding a manual refusal clause, you polished disaster."

When she fell back onto the battlefield, one of the Perfect Engine's ribs came with her. She used it to trip a bell-mouth that had been crawling toward Saelith's feet.

Brakka, meanwhile, fought the Chain That Had Been Called Bridge at the place where its links entered the plain.

The Chain knew troll memory. It knew load songs, stone vows, the pride of spans that held through flood and fire. It spoke in the voices of bridge-kin who had died with hands on support ropes. It showed Brakka every crossing lost because someone had insisted on asking one more question before taking weight. The Chain did not call itself obedience. It called itself responsibility.

Carry them, it said.

Brakka's arms shook. Links wrapped around her shoulders. Refugees appeared along the chain's length, thousands of them, living and dead, all needing passage. If she refused, they fell. If she carried too much, she became the bridge that never asked whether the stones consented to remain stones.

"Weight," she said through clenched teeth, "must be named."

Name later, urged the Chain. Hold now.

That was how emergency turned into law.

Brakka planted her maul and did the hardest thing a builder could do while people screamed on both banks.

She let one link fall.

The dream opened beneath it. No bodies dropped. Instead the false passengers vanished, revealed as pressure wearing faces. The real refugees behind them remained, fewer and more frightening because they were true.

Brakka shouted to them, "Who can walk?"

Some answered. Some could not.

"Who can carry?"

More answered.

"Who must be carried?"

Shame silenced several until others named them. The chain changed shape, not into one heroic span, but into many shorter crossings. Slower. Uglier. Less impressive from the air. Stronger because no single stone had to become holy through collapse.

Brakka broke three links and gave one to Caldus, one to Kesh, one to Sava.

"Temporary bridge law," she said.

Kesh peered at his link. "Does it come with instructions?"

"Ask weight. Then move."

"Horrifyingly concise."

Ilyr and Saelith were taken together by Corrected Song and Sealed Record.

They stood in a hall where every note had a file number and every file hummed in perfect pitch. Light and dark, sound and shadow, mercy and truth, all arranged so neither could wound the other. The room offered them peace between their peoples with a signature line at the bottom and rehearsal markings in the margin.

Saelith's hand hovered over the song.

Ilyr's over the seal.

"If we reject every offered concord," Saelith said, "do we become addicted to fracture?"

"If we accept one that cannot be interrupted, we become curators of a beautiful prison."

"That is a historian's answer."

"It is also true."

She looked at him. "I am tired of true things arriving without help."

He had no clever reply.

So he gave help.

Ilyr opened the sealed record and read the ugly entries aloud while Saelith sang beneath them, not to soften, not to erase, but to make breath possible between revelations. When her song became too lovely, he interrupted with a footnote. When his truth became a blade thrown for pride, she cracked the note under it until he heard the body it struck. They did not harmonize. They conversed.

Corrected Song screamed.

Sealed Record burst its locks.

The hall threw them back onto the field just in time to see Stillness touch Arveth's lantern.

That was how the company fractured: not by failure, but by each person carrying back the proof that their best answer could still become a door for the enemy. They landed closer to one another and less certain of themselves.

Then the courthouse margins rose, and all their partial victories were dragged into judgment.""",
    30: r"""Before Sava read the release aloud, the courthouse demanded its recess.

It did so by becoming the office where she had first met Arveth's work.

No one else recognized it. To Mara, it was a narrow room with dust stacked along shelves and a window too high to show anything except weather. To Sava, it was a kingdom. She was fourteen there, too thin, sleeves too short, hair pinned with a bent nail because actual pins cost money. Three clerks sat at desks, copying judgments with the bored cruelty of people who had learned that ink could ruin lives without raising the heart rate.

Young Sava stood in a corner holding clean paper.

On the chief clerk's desk lay a petition written in a hand so sharp it seemed to object to the page that held it. The petition concerned seven dead workers omitted from a collapse report because their contracts had expired six hours before the roof failed. The court had called them trespassers. Their families called them fathers, sisters, sons, wives. The petition used fourteen precedents, six insults disguised as procedural concerns, and one sentence Sava had copied into her own notebook until the paper wore thin:

An expired wage does not expire a body.

Arveth, alive then, entered in a coat with one cuff torn and asked whether the court intended to commit fraud before lunch or after.

Young Sava dropped the paper.

The chief clerk ordered him out.

Arveth stayed.

He lost that day. The court entered the workers as trespassers. The families received nothing. Arveth left with a split lip and two broken fingers. But before he went, he looked at the girl in the corner and said, "If you copy a lie neatly, it remains a lie. You may quote me."

Sava had.

For years, in margins so small no supervisor noticed, she had placed dots beside names that felt wrong. Dots became cross-references. Cross-references became memorized contradictions. Memorized contradictions became the habit of not letting minutes behave like graves. She had never told Arveth because by the time she could have, he was a mark in the kind of register people handled with gloves.

In the courthouse dream, she told him.

Arveth listened with his living face turned away, which Mara understood as tenderness from a man whose pride disliked being seen without armor.

"I thought I invented myself," Sava said. "I did not."

"No one does," Arveth said. "Self-invention is usually poor citation practice."

She laughed through tears. "I hate you."

"That is grief looking for a hat."

"I hate that too."

"Better."

Stillness waited while they spoke. It could afford patience because patience was one of its lovelier masks. It knew every memory made the release harder. The more Arveth had mattered, the more tempting it became to keep him.

Mara saw Sava understand that and almost fold under it.

"If I let you go," Sava said, "I am afraid the room becomes just a room again."

Arveth looked around the old office. "It was always just a room. You made it evidence."

"That is not enough."

"No. Enough is a myth people invoke when they are tired of maintaining what matters."

"Then why rest?"

He smiled, and the expression cut her. "Because maintaining what matters must be passed among the living, or it becomes another way to punish the dead for having been useful."

The room dissolved back into the margin-courthouse.

Sava's release clause trembled under her pen.

Mara thought of all the people whose lives had become tools after death because someone living could not bear the terror of choosing without them. Saints. Martyrs. Founders. Witnesses. Dragons. Brothers. Mothers. The dead turned into chairs, crowns, roads, songs, laws, excuses.

Arveth had spent his afterlife objecting to that pattern.

Now he was asking them not to repeat it with him.

When Sava wrote the comma after refuse, her hand steadied.

The courthouse watched the mark like a battlefield watches a flag.

Arveth adjusted the line with infuriating precision and said, "There. Now it can survive a hostile reading."

That was when Mara knew Sava would let him go: not because the letting stopped hurting, but because the hurt had become clean enough not to disguise itself as duty.""",
    31: r"""The throne did not only offer Mara law.

It offered revision.

The warm names turned like pages, and she saw each book of her life rewritten into a kinder argument for surrender. In the first, Kell Ashgate did not grind children into ash because a cinder witness in every mine stopped Mordane before his arithmetic learned to smile. Joryn never wore chain marks. Mara never learned to steal bread. She grew into a girl with strong hands, quick temper, a brother who teased her in sunlight, and no reason to believe being useful was the nearest door to being loved.

In the second, Harrowmere's fever bridge never burned. Caldus received a distributed command compact before the order came. He disobeyed with witnesses already in place. The sick crossed safely, the fever contained by consented quarantine, and no mother on either bank had to become an argument.

In the third, Lumenorath and Khar Veyl opened their records before Orrowen. Saelith grew up learning wrong notes as civic hygiene. Ilyr never became exile; Vaura never learned secrecy as a mother's milk; Serathiel failed younger and with fewer dead to his name.

In the fourth, Tavi's aunt survived because every prototype that touched a living body carried a cinder-witness capable of refusing activation. Brassroot became brilliant without graves in its foundation.

In the fifth, Kesh never sold the routes because the road itself screamed when payment hid bodies. Rikka lived without debt turning love into leverage. The ravine stayed only stone.

In the sixth, Brakka's bridges held because worthiness never entered weight.

In the seventh, Arveth died, rested, and was remembered correctly the first time.

Mara sobbed before she knew she was crying.

Vorrakai did not press. Pressing would have made refusal easier. He let the better worlds stand around her, each one containing less pain than the life she had actually endured.

"You said choice made cages," she whispered.

Choice without witness. Witness without power. Power without final guard. Take the throne and let suffering teach something permanent.

The rewritten Mara from the mine-that-never-was looked at her with clean hands.

That girl deserved to exist.

Mara hated the thought because it was true.

"Would she be me?" Mara asked.

Vorrakai's eyes softened. Does that matter more than her freedom from pain?

There lay the deepest hook. Mara could say yes and sound monstrous. She could say no and become the person willing to erase herself, her friends, their failures, their hard-won choices, in exchange for a cleaner ledger. The throne did not ask for vanity. It asked whether identity was worth the suffering that had shaped it.

She thought of Saelith's palm on hers after Sacrifice. Of Caldus admitting he wanted the clean crest. Of Kesh naming the second route. Of Ilyr preserving Vaura's childhood. Of Tavi damaging perfection. Of Brakka letting one false link fall. Of Sava releasing Arveth. None of those moments justified the wounds that made them possible.

But neither could a throne abolish wounds by abolishing every future self that might answer them.

"Pain did not make us worthy," Mara said.

The better worlds listened.

"It did not make us stronger in some clean song way. It broke things. It stole. It wasted. It made us cruel sometimes. I will not defend pain as a teacher."

Vorrakai leaned closer.

Then end it.

Mara shook her head, tears dropping onto the throne's first step. "Ending all choice is not the same as ending pain. It is ending everyone who might tell you whether your cure became another wound."

The clean-handed Mara faded first.

Mara reached for her before she could stop herself.

"I am sorry," she told the girl.

The girl smiled sadly, with Joryn's crooked mouth. "Eat first."

Then she was gone.

One by one, the rewritten worlds vanished. Mara mourned each, because refusing a false cure did not require pretending the cured world had been ugly. The throne's temptation remained powerful because it contained real mercy misdirected by finality.

When the last better world disappeared, only the actual battlefield remained.

Actual Saelith bleeding. Actual Caldus limping. Actual Kesh unreliable and beloved. Actual Tavi swearing at a gear. Actual Ilyr ink-stained and afraid of simplicity. Actual Brakka holding weight no one should romanticize. Actual Sava with a grief no released witness would carry for her.

Actual Mara.

Burned hands.

Empty throne.

Enough to refuse, not enough to replace refusal with ease.""",
    32: r"""The first person outside the Death-Dream to understand the new shape was not a king, dragon, scholar, engineer, priest, or commander.

It was Lora Arlet from Third Arch, who had once organized soup distribution with the merciless competence of a person who knew hunger did not respect speeches.

She stood in the camp below the Dead Capital with a ladle in one hand and a ledger in the other, watching the cinder sparks scatter from the broken throne into ordinary objects: a road ribbon, a bridge nail, a cracked bowl, a soldier's buckle, a child's chalk, a dragon shed-scale, a gnome warning plate, a dark-elf inkstone, a light-elf throat cord cut deliberately short. Each spark carried a name and a pressure, not command but witness asking for a place to be heard.

People recoiled.

Lora hit a pot with her ladle.

"Do not grab them," she shouted.

Half the camp ignored her because half the camp had no idea who she was.

She hit the pot again, harder.

"Do not grab them unless you want to explain to every dead person attached why your hands are qualified."

That worked better.

The sparks hovered.

The living had learned many bad habits from power, but one useful habit from terror: when a woman with a soup ladle sounded exactly like the person preventing dinner from becoming chaos, people paused.

Lora pointed at a bridge nail glowing with troll-blue fire. "Bridge people. Ask that one."

Three trolls approached, all speaking at once. The nail dimmed.

Lora sighed so fiercely a nearby Harrowmere officer stepped back. "One at a time. And someone who is not already proud."

A young troll mason came forward, hands shaking. She asked the name in the nail whether it wanted to be carried in the west span, the medical bridge, or not at all. The nail warmed toward the medical bridge. The mason wept and took it there with both hands.

Lora pointed at a goblin ribbon snapping green sparks. "Road people. Same rule. If anyone says emergency authority, I will put them on turnip duty."

No one knew what turnip duty meant.

Everyone feared it.

That was how the distributed cinders first entered the camp: not through grand compact, but through a soup line's logic. Ask. Assign temporarily. Review. Feed people meanwhile.

Mara saw this from the dream and laughed until she had to hold her side.

"What?" Saelith asked.

"The world may be saved by catering."

Kesh, pale from blood loss, nodded solemnly. "Never underestimate logistics. Or turnips."

As the sparks settled, arguments changed texture. They did not become gentle. Some became louder because witness made evasion harder. A Harrowmere captain who accepted a cinder-name into his command token heard every soldier his family had spent for honor and had to sit down before issuing another order. A light-elf singer carrying an Orrowen spark lost her voice for three minutes whenever she attempted a note too beautiful for the grief beneath it. A dark-elf archivist who accepted a famine spark found sealed drawers opening when hungry people entered the room. A goblin route captain with a ravine spark could still bargain, but the ribbon heated whenever he left a dead road off the map.

Power had not vanished.

It had become embarrassingly talkative.

This, too, nearly caused violence.

Some people tried to throw the sparks away. Some tried to collect several. Some claimed their suffering gave them better right to carry names than those who had caused suffering. Some were right about that in particular cases and wrong when they made it universal. The camp became a series of small hearings, each one imperfect, urgent, necessary, and irritating.

Othrava watched through the moon-eye and laughed once.

The sound rolled over the camp like spring flood under ice. Dragons in the air startled. Mortals ducked. Several pots overturned. A gnome engineer shouted that acoustic impact should have been disclosed in advance.

Veyrasha lifted her head.

Othrava spoke to the dragons first.

Do not make my waking a banner.

The dragons lowered their wings.

Then she spoke to the mortals.

Do not make my suffering a weapon that proves you harmless.

Many eyes dropped.

Finally, through the crack, she spoke to Mara.

Little witness. You have returned my name. Do not keep it.

Mara bowed her head. "I will not."

Then Othrava addressed Vorrakai, and the camp's noise thinned into listening.

We were betrayed. We betrayed. We were chained. We chained. None of this grants you custody of every future fear.

Vorrakai's grief darkened the Death-Dream sky.

The old Span rose higher, its links cutting stars.

The living camp saw it through the eye and understood only part of what it meant. That was enough. People began bracing what could be braced, moving the injured, marking exits, arguing over who had authority, then remembering to ask who had capacity. The compact was not born as parchment. It was born as behavior repeated under pressure.

Mara watched ordinary leaders choose accountability while still being ordinary.

Lora with a ladle. Pinna with a warning panel. Auralian with a song that cracked. Maelin with a hammer and a public record. Brakka's grandmother with bridge math. Oren with soup salt and a dead soldier's ten-minute guard shift. Veyrasha asking where to place her claws. Children painting debt names on wheels because adults had spent too long calling maps complicated.

None of them could replace Mara.

That was the point.

She could not replace them either.

When the old Span opened into the wound, the living did not cheer. Cheering belonged to stories that cropped bodies from victory. Instead they made more room, checked bandages, tied road ribbons, relit lanterns, renewed questions, and kept the noise going so fear would have a harder time arranging them into one obedient shape.

The answer of the living was not yes.

It was again.

Again ask. Again repair. Again object. Again release. Again feed. Again count. Again stop the person trying to make again unnecessary forever.

Mara carried that word with her as she stepped into the wound.""",
    132: r"""Before the wound accepted them, it demanded witnesses from both sides of the dream.

The old covenant had been made by representatives who thought representation could substitute for return. One queen, one keeper, one singer, one roadmother, one bridge-speaker, one forge-master, one dragon judge, each carrying more fear than any one body could safely translate. The wound remembered that error and tried to repeat it. It opened seven bright places on the broken Span, each shaped like an office waiting for someone important enough to fail on behalf of everyone else.

Mara felt the invitation reach for her friends.

Caldus could stand for oaths. Saelith for mercy. Ilyr for record. Kesh for roads. Tavi for engines. Brakka for bridges. Sava for witness. Seven offices, seven trusted people, one cleaner covenant than the world deserved.

"Absolutely not," Sava said.

Everyone looked at her.

She wiped her face with a sleeve that already contained ink, ash, and what might have been dragon soot. "I have had a day. I am no longer emotionally available for symbolic architecture."

Kesh put a hand over his wound. "Seconded with bleeding emphasis."

The Span brightened, impatient.

From the living camp below, answers rose before the company could decide wrongly. Not speeches. Objects.

A soup ladle flew first, tossed through the crack by Lora Arlet with enough force and poor aim that it struck the Span and rang like a bell. It carried no authority except the authority of having fed people who would otherwise confuse politics with hunger.

Then came a warning plate from Pinna Vey's stabilizer, edges scorched blue, listing three harms discovered after deployment and one crossed-out phrase: acceptable losses. A goblin road ribbon followed, painted by a child's uneven hand with the name of the ravine and an arrow pointing both ways. A troll measuring cord landed across Brakka's link, knotted at intervals for bodies that could walk, bodies that could be carried, and bodies that should not have been made to prove either. A page from Maelin's public reading slapped against Ilyr's boot, covered in restricted records copied so quickly half the letters leaned. A broken Harrowmere command token came spinning after it, split by a civilian witness mark. A light-elf throat cord cut deliberately short drifted down like a white root that had chosen not to grow into a noose.

The seven offices flickered.

More objects came.

Too many to arrange.

That was their power.

A child's chalk. A dragon shed-scale marked with landing questions. A kettle lid used as an alarm. A death list with errors corrected publicly and angrily. A boot from a refugee who could not stand but insisted his boot could count him in the line. A cracked archive seal. A bridge stone too small for ceremony. A gear tooth from an engine that had stopped when asked by the person it endangered. A fever family's ribbon. A dead soldier's ten-minute guard mark. A page from Sava's release clause copied by someone who had misspelled Arveth and then corrected it without hiding the mistake.

The old Span tried to reject the clutter.

It had been designed for solemn offerings.

The clutter held.

Mara knelt and picked up the soup ladle.

"This is ridiculous," she said, voice shaking.

"That may be its legal strength," Ilyr said.

Saelith touched the cut throat cord. "No one object can become the answer if there are too many to crown."

Brakka ran the measuring cord through her hands. "Many small loads."

Tavi lifted the warning plate and smiled fiercely. "Post-deployment correction as sacred artifact. I may start a religion."

"Please do not," Caldus and Kesh said together.

The living camp kept sending witnesses until the seven bright offices guttered out, replaced by a rough scatter of places anyone might touch and no one could occupy forever. The old covenant wound had expected leaders. It received tools, mistakes, food service, protest, repair, and bad handwriting.

Vorrakai's shadow moved over the Span.

You trivialize the first wound.

Mara stood with the ladle in one hand and the Kell cloth tight around the other wrist. "No. We refuse to make it grand enough that ordinary people cannot interrupt it."

The Span shook.

Below, the camp heard some echo of that answer. Noise rose again, not triumphant, not unified. Lora shouted for more soup because apparently apocalypse did not exempt anyone from eating. Pinna demanded that every new cinder-object be tagged with date, carrier, and known risks. Maelin began organizing public copies before anyone could declare the moment too sacred for distribution. Auralian taught three children the broken song interval and accepted immediate criticism from all of them. Veyrasha moved one claw west and waited for a bridge-reader's approval. Brakka's grandmother declared the old Span "showy and under-reviewed," which did not destroy it but visibly offended several ancient laws.

Sava watched with the register open to her own blank page.

For the first time since Arveth's rest, she wrote without looking for his mark.

Mara saw the line: Witness list intentionally incomplete.

Sava caught her looking. "It is a start."

"He would have corrected the adverb."

"I know."

Sava's mouth trembled, but she did not stop writing.

The wound accepted the objects one by one, not as replacements for the company, but as proof that the company did not arrive alone. Each item embedded itself in the broken Span. The chain-bridge shuddered under soup ladle, warning plate, road ribbon, measuring cord, copied record, command token, short throat cord, and a hundred lesser witnesses. Where they touched, the ancient links could not decide whether they were chain, bridge, road, record, engine, song, or tableware.

That confusion opened passage.

Not wide.

Not safe.

Enough for people willing to enter without pretending entrance made them masters.

Caldus went first, then stopped and stepped aside. "Habit."

Brakka snorted and entered beside him, not behind. Kesh limped through on the other side, muttering that if the afterlife contained this much committee work he wanted a refund. Tavi followed with three tools and five warnings. Ilyr carried the copied restricted page where everyone could see it. Saelith held the cut cord like a note she had promised not to complete. Sava came with the register open. Mara entered last because for once last did not mean lesser.

As the wound closed around them, the living camp did not fade.

Its noise came with them.

Soup pots, warning whistles, bridge hammers, wrong notes, public readings, route chimes, dragon breath, civilian objections, children correcting maps. A world not saved, not pure, not wise enough to be trusted without review, but present. The sound threaded through the broken Span and kept the Death-Dream from arranging the company into seven offices again.

Mara carried the word again into the old lock.

Again, not forever.

Again, for now.

Again, with witnesses.

It was a small word to take against a dead god.

Small things, she had learned, were harder to turn into thrones.""",
    232: r"""The passage remembered everyone who hesitated.

That, too, became part of the witness. The old covenant had been full of people who later claimed they had known better at once, as if wisdom had arrived clean and immediate in every worthy heart. Mara had seen enough records to know that was another kind of lie. Good choices often stood for a long time at the edge of bad ones, breathing hard.

Caldus hesitated over the broken command token because part of him still wanted one order strong enough to save the camp without asking the camp to become brave. Saelith hesitated over the cut throat cord because part of her still believed a beautiful enough song could keep people from hurting one another. Ilyr hesitated over the copied page because public truth had never stopped being dangerous merely because secrecy was worse. Tavi hesitated over the warning plate because every named risk made the unnamed ones feel like accusations. Kesh hesitated over the road ribbon because routes opened for everyone could still be used by hunters. Brakka hesitated over the measuring cord because some weights remained impossible even when named. Sava hesitated over the blank page because writing without Arveth answering made the ink feel too loud.

Mara hesitated over all of them.

The passage did not punish hesitation.

It recorded it.

That was new.

The first covenant had been built by people ashamed of fear, and shame had driven fear underground until it became chain. This time fear walked beside them where everyone could see its limp.

"Minutes note," Sava said quietly, "all parties entered afraid."

No mark corrected her.

She added, "No objection."

Mara looked back once through the narrowing crack. The living camp was still a confusion of light and argument. Somewhere in it, Lora's ladle rang again. Somewhere, a dragon asked where to step. Somewhere, a child painted a dead name on a wheel and spelled it wrong and was corrected by someone who had almost hidden the name entirely.

That was what they carried into the lock: not certainty, not courage without tremor, but fear kept public long enough that it could not pretend to be law.

The wound closed around them with the sound of an old chain learning, unwillingly, that it had been named.""",
    332: r"""After it closed, one sound still came through.

Not a roar. Not a command. A spoon against a pot, struck three times, unevenly.

Mara did not know whether Lora meant courage, dinner, warning, or irritation. Probably all four. That made it better than a banner. The sound had no doctrine in it, no promise that history would finally behave, no demand that anyone die beautifully. It only said: people remain, and people need feeding, and someone is annoyed enough to keep rhythm.

Mara smiled in the dark.

"What?" Saelith whispered.

"Nothing holy."

"Good."

The spoon rang once more, farther away.

Then the old lock opened beneath their feet.""",
    432: r"""Inside the first step, the company felt the cinder distribution take hold behind them.

It was not comfortable. Comfort would have meant the old pattern had learned a prettier costume. Instead Mara felt small tugs in every direction, each one a reminder that the names she had released would now interrupt people she loved and people she distrusted alike. Caldus winced as a cinder in his shield objected to the angle of his stance. Tavi snapped at a warning spark that chose the middle of a crisis to ask who maintained the maintenance notes. Kesh's cracked token heated whenever he thought the word shortcut with too much affection. Saelith's cut cord hummed whenever her mercy became tidier than her grief. Ilyr's page rustled when silence tempted him as efficiency. Brakka's measuring cord tightened when she forgot to ask whether someone wanted to be carried. Sava's blank page remained blank, which somehow accused her most of all.

"This is going to be unbearable," Kesh said.

"Yes," Mara answered.

He looked almost pleased. "Then it is probably not a crown."

That made Caldus laugh once, short and surprised. The laugh moved through the dark passage like a human thing trespassing in myth. The old lock recoiled from it. Myth liked solemnity. Solemnity made people easier to arrange.

Mara held Saelith's hand and let the laugh stay in the record too.""",
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
        if chapter_no == 32 and 132 in WORD_FLOOR_DEEPENING:
            replacement += "\n\n" + WORD_FLOOR_DEEPENING[132].strip()
        if chapter_no == 32 and 232 in WORD_FLOOR_DEEPENING:
            replacement += "\n\n" + WORD_FLOOR_DEEPENING[232].strip()
        if chapter_no == 32 and 332 in WORD_FLOOR_DEEPENING:
            replacement += "\n\n" + WORD_FLOOR_DEEPENING[332].strip()
        if chapter_no == 32 and 432 in WORD_FLOOR_DEEPENING:
            replacement += "\n\n" + WORD_FLOOR_DEEPENING[432].strip()
        text = text[:start] + replacement + "\n\n" + text[end:].lstrip()
        matches = list(pattern.finditer(text))
        by_no = {int(m.group(1)): m for m in matches}
        back_matter = re.search(r"(?m)^## Back Matter\b", text)
    return text


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
        'current_form: "full-length draft zero with Book Three chapters 1-32 revised in pass 01"',
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
    revised = replace_chapters(text)
    total = word_count(revised)
    if total < MIN_WORDS:
        raise ValueError(f"Revision would reduce Book Three below {MIN_WORDS:,} words: {total:,}")
    check_scaffold("\n\n".join([*CHAPTERS.values(), *WORD_FLOOR_DEEPENING.values()]))
    MANUSCRIPT.write_text(revised, encoding="utf-8")
    update_metadata(total)
    update_summary(total)
    print(f"Book Three chapters 29-32 revised. Word count: {total}")


if __name__ == "__main__":
    main()
