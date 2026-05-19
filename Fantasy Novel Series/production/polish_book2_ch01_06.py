#!/usr/bin/env python3
"""Revision pass 01a for Book Two chapters 1-6.

Replaces Part I's draft-zero scaffold with bespoke sequel-opening scenes:
Mara's unwanted banner, Pale Bough sanctity, Khar Veyl's summons, Tavi's waking
map, Kesh's road-clan debt, and Mara's first command by refusal.
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
    1: r"""## Chapter 1: The First Banner

The first banner made Mara want to turn around.

It hung from a broken toll arch two miles east of Harrowmere, where the old crown road sagged into mud and refugee wagons had chewed the ruts deep enough to drown a boot. The cloth had once been a flour sack. Someone had dyed it with ash water and berry stain, then painted an open hand above a coal-bright circle.

Mara's hand.

Or what people thought her hand meant.

Wind snapped the sackcloth until the painted fingers seemed to beckon. Beneath it, a line of refugees waited for soup ladled from three dented army kettles. Miners from Kell Ashgate stood with palace laundresses, Harrowmere clerks, two bruised royal guards stripped of insignia, children with slate boards hung around their necks, and a dozen named dead sitting in the thin morning light because sunlight was still something some of them had asked for by name. Beyond the soup line, old wagons carried stolen ledgers, rolled chapel rugs, cracked regulator parts, and the ordinary wreckage of families that had fled before deciding what to be afterward.

The banner flew over all of them.

Mara stopped so sharply that Caldus almost walked into her.

"No," she said.

Kesh shaded his eyes and studied the painted hand. "Technically it is a strong likeness if one has never seen your hand."

"Take it down."

"That is less a greeting than some revolutions prefer."

"Kesh."

He looked at the line of hungry people. His smile softened into something less useful to him. "Taking down a symbol over a soup kettle can look like taking down the soup."

Mara hated that he was right. She hated more that he said it gently.

The company had left Harrowmere before dawn, skirting chapel gardens where white roots had begun to push through the flagstones in pale searching fingers. They were supposed to be traveling north after one last look at the city's fracture lines. Instead every road had bent toward the same problem: people using Mara's name faster than Mara could arrive to correct them.

Tavi climbed onto a milestone and adjusted the brass listener strapped across her chest. "For the record, the soup kettles are crown issue. The banner is local. The heat beneath us is not local, which I find upsetting in a professional way."

"Everything beneath us is upsetting now," Kesh said.

Brakka set her maul against the mud and listened through its haft. "Road full. Vow thin."

"What does that mean?" Mara asked.

"Many feet. Few promises."

Saelith stood a little behind Mara, gray travel coat damp with mist, pale hair braided without any ceremonial rings. She had been quiet since the chapel gardens. Quiet did not make her less visible. Several refugees had already noticed her ears and the luminous scar where she had cut away her order's white clasp. Their fear moved around her like cold water around a stone.

Ilyr noticed the fear too. Of course he did. He noticed everything that might later become a knife.

"If you take the banner down yourself," he said, "some will say humility. Some will say rejection. Some will say proof that the Cinder Saint walks among the hungry without needing colors."

Mara glared at him.

"I did not invent politics," he said. "I merely resent them with accuracy."

At the soup line, a little girl looked up from her bowl and saw Mara.

Recognition spread badly.

It was not one shout. One shout could be answered. It was a silence first, then a shift in posture, then the awful tilt of faces deciding what story had just arrived. Someone whispered Cinder Saint. Someone else said Ash Hand. A man with a bandaged scalp dropped to one knee before apparently realizing the mud was deep and dignity had limits. Two named dead turned their painted faces toward her with the patience of citizens waiting to see whether a new official understood the work.

Mara's chest tightened.

She had imagined fear would fade after Kell Ashgate. It had not. It had learned new clothes.

A woman in a soot-black shawl pushed through the line carrying a ladle like a scepter. She was broad, red-eyed, and too tired to be impressed by anyone's legend.

"You Mara Venn?" she asked.

"Yes."

"Good. Tell those fools by the banner to stop letting people kneel in the food mud. Makes the line slower."

Mara almost sagged with gratitude. "I can do that."

"Can you get us flour?"

That was harder.

Caldus moved beside her. "How many mouths?"

"Alive, named, or undecided?"

No one spoke for a breath.

The woman lifted her chin as if daring them to flinch. "We count all who ask."

Mara liked her immediately.

"Name?" Mara asked.

"Bessa Tarl. West washhouse. Formerly under palace contract. Presently under no one's boot if the morning is kind."

Mara nodded. "Bessa, who raised the banner?"

The woman jerked her chin toward the toll arch. "Harl's boys painted it. Not bad lads. Too much grief, not enough orders. The road needed a sign. We had yours."

"It is not mine."

"That is convenient for you and useless for everyone trying to find the soup."

Tavi muttered, "I did warn that symbols provide dangerously efficient wayfinding."

Mara walked to the arch.

The crowd parted. She wished it would not. She wished for one person to bump her shoulder and complain about mud. She wished for Dilla's kitchen, where affection came with orders and nobody mistook her discomfort for holiness.

Three young miners stood beneath the banner with spears made from cart poles. Kell Ashgate boys, by their ash scarves and bad boots. One had the beginnings of a beard that looked like an argument he was losing. Another wore a palace guard's helmet backward. The third recognized Mara and went white.

"We meant respect," he said.

"I know."

"People were coming from three roads. Royal patrols too. The banner made them think twice."

Mara looked up at the painted hand. "Did you ask any of the people under it what they wanted it to mean?"

The boys exchanged looks.

Behind her, the soup line waited. Not because she had commanded it to, but because hunger had been taught to wait around power and call it patience.

Mara climbed onto a fallen stone.

The old Mara, the ash-runner, would have hated being visible. The new Mara hated it too, but with witnesses.

"This banner does not make me your ruler," she said.

Her voice did not carry far enough. Caldus repeated it louder. Brakka repeated it louder still, and when Brakka spoke, even mud seemed to listen.

"It does not make me saint, captain, queen, or judge," Mara continued. "It means one thing if it means anything: no one here gets counted as less than a person. Not the hungry. Not the named dead. Not the guards who throw down orders. Not the children. Not the people who disagree with me. If that is too little for you, take it down. If that is enough, then the first work is soup, names, and a dry road."

"And flour," Bessa called.

"And flour," Mara said.

Someone laughed. The laugh saved more than the speech did.

Then the west road screamed.

Not a person. A road.

The sound ran through the mud under Mara's boots, a cinder-bell struck by panic. Three wagons at the edge of camp lurched as their harnessed oxen tried to bolt. Refugees shouted. A boy fell under a cart wheel. Caldus moved before Mara did, staff sweeping down to wedge the wheel while Kesh slid through the mud and dragged the boy clear by his collar.

"North ditch!" Kesh shouted. "Something under the water!"

The ditch beside the road boiled black.

Ash wights climbed from it, six, ten, more, their old soldier coats plastered with mud and crown seal-hooks glowing at their throats. Not Mordane's clean command lines. These hooks sparked erratically, pulling on whatever orders had survived the palace collapse. Protect crown stores. Clear unlawful assembly. Return bodies to audit. The dead jerked between instructions, which made them worse. A clear enemy could be fought. A broken command flailed until someone bled enough to simplify it.

People ran.

The banner snapped overhead.

Mara felt the cinder shard at her hip wake with an eagerness that made her stomach turn. Heat pooled in her burned palm. A word rose behind her teeth, old and draconic, a word that would push the wights flat into the mud if she let it become command.

Do not answer too quickly.

Arveth's voice was ash and margin inside memory.

"Names!" Mara shouted. "If you know them, say them!"

"We do not know soldiers!" someone cried.

"Then say what they are doing."

Ilyr understood first. "Uncertain dead on west ditch. Ten bodies. Crown hooks unstable. Witnessed by road camp."

"Witnessed!" Bessa roared, because some people were born with the gift of making a word useful.

The refugees took it up badly, raggedly, and that was enough to change the air.

Saelith moved into the line of injured, asking permission so quickly her words became breath. Tavi threw a brass coil into the ditch and shouted for everyone to stop stepping on the wire. Brakka planted her maul between the wights and the soup kettles. Kesh vanished behind the toll arch, reappeared above it, and cut the banner rope.

For one sick heartbeat Mara thought he was taking it down.

Instead he dropped the cloth over the front rank of wights.

Mud, ash dye, and berry stain smeared across their glowing hooks. The painted hand tore down the middle. The cinder command sputtered, confused by symbol, witness, and bad weather all at once.

"Now!" Kesh yelled.

Caldus led the push, not with a knight's charge but with the ugly practical work of making space. Brakka hooked two wights aside. Tavi's coil discharged with a sound like an insulted kettle. The ditch water flashed blue. Mara stepped close enough to smell drowned wool and old iron.

"Unknown," she said to the first wight. "Held. Witnessed. Not returned."

Her burned hand touched the torn banner between them.

The wight stopped.

One by one, the broken commands loosened. Not all. Three bodies collapsed into mud. Two kept fighting until Caldus and Brakka pinned them. One began saying the same word over and over, not a name, perhaps, but the shape of one. Bessa knelt in the mud with her soup ladle across her knees and said it back until the dead soldier quieted.

When it ended, no one knelt.

That felt like victory.

The toll arch stood bare. The banner lay ruined across the ditch, paint bleeding into mud.

The beardless miner stared at it, devastated. "We can make another."

"No," Mara said, too sharply.

He flinched.

She made herself breathe. "Not another me."

Tavi wiped mud from her cheek. "May I suggest a bowl? Bowls are politically underdeveloped."

Bessa looked at the kettles, the dead, the torn cloth, and the people beginning to stand. "An open bowl," she said. "With a name line under it."

Mara nodded. "A place to eat. A place to be counted. Not a person to obey."

The miner considered this with the gravity of someone being asked to repaint the world. "I can do a bowl."

Kesh picked berry-stained thread from his sleeve. "Heroism survives another branding meeting."

Mara looked at the road camp, at the injured, at the named dead being helped into sun, at the children watching to see whether the adults would turn the morning into a story too simple to live inside.

The first banner had fallen.

The problem under it had not.
""",
    2: r"""## Chapter 2: Saints Want Witnesses

The border chapel grew out of the road instead of beside it.

White roots rose from the mud in smooth arches, braided together into walls that seemed too delicate to hold a roof until Mara noticed the old stones caught in their grip. The chapel had swallowed an older human shrine, a milestone, three graves, and half a toll booth. Nothing had been destroyed exactly. Everything had been preserved inside the light-elf shape of the place, held where it could no longer argue with its new purpose.

Rain slid down the pale bark without darkening it.

Saelith stopped at the edge of the rootwork.

Mara had seen her afraid in battle, ashamed in confession, furious when gentleness was used as a chain. This was different. The chapel had taught Saelith's body old obedience. Her shoulders lowered. Her hands folded before she caught them and forced them apart.

"You do not have to go in," Mara said.

"That is the first kind thing the chapel has heard all morning," Kesh murmured.

Saelith looked at the open doorway. "If I do not enter, they will say guilt kept me out."

"If you do enter, they will say the chapel received you."

"Yes."

"Convenient people, your order."

"They call it harmony."

The refugees from the road camp waited behind them in a ragged caravan: Bessa with two kettles and a flour inventory, Fenna Clay with the quiet writ, the boy whose mother Sella Brin had been erased, three named dead under canvas shade, and twenty-seven others who had somehow become Mara's responsibility because she had failed to walk away quickly enough. Caldus had organized them into groups with the patience of a man pretending pain was theoretical. Brakka had marked the wheels with a Seven Arches sign that meant road under witness. Tavi had objected to every axle and improved most of them. Ilyr had said little since dawn, which meant he was either thinking about Khar Veyl or deciding where to hide a body. Possibly both.

The chapel bells rang without being touched.

Light gathered in the doorway.

Five Elyri stepped out in white travel robes, their hair bound with living root thread, their faces composed into the serene expression of people who had practiced mercy before mirrors. Four carried curved blades sheathed in pale wood. The fifth carried no weapon, which made Mara trust her least.

She was tall even for a light elf, brown skin warmed by inner gold, her left eye veiled with a translucent leaf scar. Around her throat hung a small branch of the Pale Bough, silver-white and blooming in rain.

Saelith went very still.

"Dawnmere," the woman said.

"Veyanna."

Not friend. Not title. A name with history sharpened behind it.

Veyanna's gaze moved to Mara. It did not crawl over her burns or linger on her ash-stained coat. Somehow that made it more invasive.

"Mara Venn of Kell Ashgate," she said. "Witness of the first unbinding. Bearer of the living coal. By mercy of the Pale Bough, this chapel opens sanctuary."

"For the refugees?" Mara asked.

"For all who stand under your disturbance."

Kesh coughed. "Lovely. We are a weather event."

Veyanna did not look at him. "For the hungry, food. For the wounded, healing. For the named dead, preservation until lawful discernment. For you, Cinder Saint, protection."

The word saint passed through the refugees like a hand through grain.

Mara felt Saelith flinch.

"Do not call me that," Mara said.

Veyanna inclined her head. "Holiness rarely names itself."

"Neither does theft."

The four blade-bearers shifted.

Caldus moved half a step. Brakka's maul touched mud. Tavi whispered, "Excellent. We have reached diplomacy's injury portion early."

Veyanna's expression did not change. "No theft is intended. Your acts have entered the public soul. A soul in upheaval requires form."

"People require soup," Bessa said from behind Mara.

That earned Veyanna's attention. "The chapel stores are open."

"With records?"

"Of course."

"Then start with flour and stop decorating the girl."

Mara could have kissed Bessa on the forehead.

Veyanna's smile was almost real. "The Pale Bough honors plain speech."

Saelith exhaled. "No, it does not. It curates it."

The rain seemed to pause.

One of the blade-bearers whispered Saelith's name as if it hurt him.

Veyanna turned fully to her. "You have cut away your clasp."

"I have."

"You travel without correction."

"I travel with witnesses."

"You travel with a cinder-bearer, a Veyra exile, a goblin debt-runner, and an unranked human soldier."

"And a troll oath-sister," Brakka said.

"Forgive me," Veyanna said, bowing with exact grace. "The Seven Arches should not be omitted from a list of complications."

Brakka grunted. "Forgiveness pending."

Mara stepped between them before courtesy found a blade. "We need passage north."

"You have it," Veyanna said too quickly.

Ilyr's eyes narrowed.

"In what shape?" he asked.

Veyanna looked at him as if noticing a stain she had already decided not to mention. "An honor escort. The road to Lumenorath is unsettled. Royal loyalists hunt witnesses. Khar Veyl agents move without declaration. Cinder-struck dead gather wherever command hooks fail. Serathiel offers protection until the matter of the dragon-moon can be discerned."

The last words struck the air cold.

Mara heard something beneath the chapel.

Not a cinder exactly. A root memory. White, old, deliberate. It hummed through the walls, carrying preserved voices in layers. Wedding vows. War hymns. Trial songs. Last words. Children's recitations. Confessions accepted and edited for beauty. Saelith's voice as a girl, high and clear, singing law before she understood law could be hungry.

Then another voice, deeper, folded under the hymns.

Saints want witnesses because witnesses can be arranged.

Mara put one hand to the root wall.

The chapel answered with light.

For a heartbeat she stood inside a version of herself made by strangers. Her burns were clean. Her coat was white. Her face was calm, obedient, merciful in a way that had no room for impatience or mud or Bessa's flour. Painted refugees knelt. Named dead smiled because the picture had removed the hooks from their throats and the uncertainty from their eyes. Saelith stood behind her restored to white, serene and forgiven. Ilyr was absent. Kesh was absent. Brakka had become a stone ornament at the chapel door.

Mara yanked her hand back.

"No," she said.

The root wall cracked under her palm.

Not far. A finger's width. Enough for rainwater to enter.

Every light elf in the doorway stared.

Saelith took Mara's injured hand carefully, with a question in the touch. Mara nodded. Saelith did not heal it. She only held it where Mara could feel a living grip.

"Your sanctuary edits," Mara said.

Veyanna's leaf-veiled eye lowered. "Sanctuary preserves the highest truth of a life."

"You mean the most useful one."

"Usefulness is not always corruption."

"I know," Mara said. "I was raised useful."

That landed. Not with Veyanna perhaps, but with the refugees. With the boy whose mother had been a washer and then an erased body. With Bessa. With the named dead under canvas. With Caldus, whose old oaths had called obedience useful until usefulness rotted in his hands.

The chapel bells rang again. This time they sounded irritated.

From the root doorway, a figure of woven light appeared: Serathiel of the Pale Bough, not present in flesh but projected through hymncraft. Mara remembered her from Harrowmere, the saint-general with the cracked white bough and the terrifying ability to make mercy look like surrender's older sister.

"Mara Venn," Serathiel said.

The refugees bowed before deciding not to. The mixed motion made the mud churn.

"Serathiel," Mara answered.

"You stand at a threshold with hunted people behind you and waking fire beneath you. I offer road, food, escort, and recognition."

"At what price?"

"Witness."

Ilyr laughed once, softly. No humor survived it.

Serathiel's projected gaze moved to him. "Ilyr Noct-Vey. Khar Veyl has sent its summons. You know what your people will do if the cinder-singer reaches them unguarded."

"Lie less beautifully than yours?"

"Seal her below, if fear prevails."

"And you?"

"Raise her where all can see."

Mara looked at the torn skin across her palm. "Those sound like different shelves in the same locked room."

For the first time, Serathiel's expression changed. Not anger. Interest.

"Then walk carefully, Cinder Saint."

"Mara."

"Mara," Serathiel corrected, and somehow made the correction feel temporary. "Accept the escort. Refuse the title if you must. Feed your people. The road to Lumenorath will open at dawn."

The projection faded.

No one moved until Kesh said, "I vote we accept the food and mistrust the furniture."

"The furniture?" Tavi asked.

He nodded toward the chapel. "Anything with roots that clean is planning something."

Bessa pushed past him toward the stores. "Fine. It can plan around inventory."

The refugees followed, cautious and hungry. The named dead paused at the threshold until Saelith asked each whether they wished to enter. Two said yes. One said sun. Brakka remained outside with that one under a canvas awning, holding the pole steady while rain softened the road.

Mara stayed in the mud.

Saelith stayed with her.

"Veyanna trained me," Saelith said after a while. "She taught me how to ask a wound what shape it wanted to become."

"Did she teach you to hear the answer?"

Saelith looked at the cracked root wall. "Not until you."

Mara did not know what to do with the tenderness in that, so she let the rain handle it.

At dusk, the chapel raised a new white marker beside the road. It bore no painted hand, no open bowl, no refugee tally.

Only three words in luminous script:

SANCTUARY FOR WITNESS.

Mara stared at it until the letters blurred.

"That is not a cage," Veyanna said behind her.

Mara thought of the chapel vision, of herself cleaned into usefulness, of Saelith's voice preserved before choice, of Serathiel offering two kinds of custody and calling one honor.

"Not yet," Mara said.
""",
    3: r"""## Chapter 3: The Exile's Summons

The Khar Veyl message arrived inside a dead man's shadow.

It happened at the chapel's north milestone while dawn still made the white roots glow from within. Refugees loaded flour. The Pale Bough escort arranged itself with graceful efficiency around the caravan, four blade-bearers ahead, two behind, and Veyanna moving wherever Mara's discomfort looked most measurable. Tavi inspected the root-lanterns and muttered about smug botany. Kesh sold three lies to a chapel quartermaster and bought back two as information. Brakka carved a road mark into a boundary stone because she did not trust any threshold that sang.

Ilyr stood alone with Arveth's ledger under one arm.

The shadow of the dead courier from Harrowmere fell wrong.

The man himself sat on a cart being bandaged by Saelith. His shadow stretched north like every other shape in the morning. Then it folded at the waist, stood upright, and bowed to Ilyr.

Every Pale Bough blade came half out.

Ilyr did not move.

"House Noct-Vey remembers its exile," the shadow said.

Its voice was not sound exactly. It was the pressure change before a tunnel collapse. Mara felt it in her teeth and in the cinder shard at her hip. The chapel roots dimmed.

"House Noct-Vey has an excellent memory for its own convenience," Ilyr said.

"You speak under surface witness."

"I find it reduces embellishment."

The shadow turned its blank head toward Mara. Where a face should have been, darkness held pinpricks like stars seen through deep water.

"Mara Venn. Cinder-singer. Ash witness. Unmeasured hazard."

"Charming people," Kesh murmured. "Very giftable."

The shadow ignored him. "By order of the Umbral Seat, Ilyr Noct-Vey will descend with the hazard to Khar Veyl for inquiry, containment, and historical correction."

Veyanna stepped forward. "The Pale Bough has accepted guardianship."

"The Pale Bough has accepted many things that were not offered."

For one bright second Mara liked the shadow. That seemed unsafe, so she stopped.

Ilyr's face had gone still in the way that meant every word cost him. "And if I decline?"

The shadow unfolded one long hand. Black wax appeared in its palm, stamped with a seal that hurt to look at: a crescent blade over a closed eye.

"Your name will be removed from memory-law. Your testimony will be inadmissible. Your house will deny issue. Your dead will not answer you. Your roads below will close."

Saelith stopped bandaging.

Tavi whispered, "Can they do that?"

"Yes," Ilyr said.

Mara heard the word under the word. Not fear exactly. Something lonelier.

Caldus planted his staff in the mud. "No court has claim over a man not standing in it."

"Human law is very fond of geography," the shadow said.

"So are spears."

Brakka made a pleased sound.

Ilyr lifted one hand, stopping the company before the moment became violence. "You said historical correction."

"Maelin Noct-Vey is retained."

The name struck him harder than the threat had.

Mara remembered the black paper at the first road camp: Maelin retained in moonward custody. Exile Noct-Vey answer for half-truth.

"Retained where?" Ilyr asked.

"Under the Umbral Seat, pending answer."

"That is not where."

"It is enough where for an exile."

The insult landed so cleanly even Veyanna looked away.

Mara stepped beside Ilyr. "Who is Maelin to you?"

The shadow tilted toward her. "Not your record."

"I asked him."

Ilyr's jaw worked. "My sister."

The road seemed to narrow around them.

"I thought she was dead," he said, quieter. "Or erased. Khar Veyl encouraged both understandings."

"Because you left with half a treason," the shadow said. "Return with the other half."

The cinder at Mara's hip warmed.

Under the milestone, under the chapel roots, a black road remembered old feet. Not evil. Not holy. A road pressed into darkness by people who had learned that truth could be stolen if left in sunlight. Mara heard fragments: children reciting lineage backward, judges cutting lies from testimony with knives of obsidian, a woman laughing in a tunnel while alarms rang, Ilyr younger and bleeding, Maelin saying If you tell it, tell all of it, coward.

Ilyr closed his eyes.

"They sent you where surface witnesses could hear," Mara said to the shadow.

Its star-prick face turned to her.

"That means they want us frightened, but not silent. They need something from us."

"The hazard reasons."

"The hazard is standing here."

Kesh leaned toward Tavi. "I liked saint better than hazard."

"You like anything that sounds billable."

Mara kept her eyes on the shadow. "Tell your court this: I will come below. Not as prisoner. Not as weapon. Not because you threatened Ilyr's name. Because Maelin is retained, and retained is another word people use when they want not-dead to sound tidy."

The shadow's head dipped. "Terms are not yours."

Brakka's maul struck the milestone.

The sound rolled through mud, root, and buried stone. The chapel bells rang once in protest. Pale Bough blades cleared their sheaths. Refugees ducked. The shadow's edges frayed.

"Road under witness," Brakka said. "Threat on road answers road."

"This is not Seven Arches jurisdiction," Veyanna snapped.

Brakka looked at the white roots holding the old milestone. "Milestone disagrees."

The stone under her maul glowed with old troll script, older than chapel or crown. For one breath the north road appeared beneath the visible road: a dark seam descending through root, clay, and buried ruins toward a depth where blue-black fires burned in disciplined rows.

The shadow bowed to Brakka this time, and not politely.

"Third Arch speaks out of turn."

"Third Arch speaks while standing. Common confusion."

Mara could feel the situation deciding whether to become a battle. Caldus shifted his weight. Saelith moved between refugees and blades. Tavi's hand hovered over a device that whined like a kettle full of bad decisions. Kesh had vanished, which meant either ambush or theft.

Ilyr opened his eyes.

"I will answer," he said.

Mara looked at him. "Ilyr."

"No." His voice cut gently, which somehow hurt more. "This part is mine. I will answer Khar Veyl. I will answer Maelin. I will answer what I did not tell you."

The shadow extended the black wax seal.

Ilyr did not take it.

"But I will not deliver Mara Venn as hazard, saint, hostage, proof, or apology. If the Umbral Seat wants her testimony, it will receive a witness who can refuse."

The shadow's edges tightened.

"That phrasing will anger them."

"I was exiled for efficiency. I have chosen thoroughness."

Kesh reappeared behind the shadow holding a strip of black paper. "Speaking of thoroughness, does anyone want to discuss why our ominous friend carries two messages?"

The shadow spun.

It was fast. Kesh was already moving. The darkness cut through where his throat had been and found only chapel rain. Caldus slammed his staff down, pinning the shadow's reaching arm to the milestone's light. Saelith's hand lifted, then stopped because she did not know whether healing light could become harm if used on a shadow. Tavi solved the question by throwing a pocket mirror into the mud.

"Down!" she shouted.

The mirror flared with stored chapel light.

The shadow became seven shadows, each showing a different possible strike. Ilyr moved through the false bodies with one blade drawn and cut the black wax seal in half.

The real shadow froze.

Mara heard a cry far below. Not pain. Surprise.

Kesh landed beside her, panting, and shoved the stolen strip into her hand. "Invoice later."

The paper was cold.

Words surfaced in silver-black script:

If Pale Bough escort reaches White Road unchallenged, Serathiel claims saint before Seat can question witness. Maelin to be moved moonward. Bring all records. Trust neither preservation nor secrecy.

Ilyr read it over her shoulder.

For the first time since she had known him, he looked young.

"Maelin wrote that," he said.

The shadow, pinned by broken seal and reflected light, began to unravel. Its voice came from farther away. "Message integrity compromised."

"Yes," Tavi said. "Deeply sad. Learn pockets."

"Ilyr Noct-Vey," the shadow said. "Seven nights."

"Until what?" Mara asked.

The last of its star-prick face turned toward her.

"Until memory-law forgets mercy."

Then it collapsed into the dead courier's ordinary shadow, which behaved itself so abruptly that everyone distrusted it.

The Pale Bough escort resheathed blades with offended grace. Refugees resumed breathing. The dead courier looked at his shadow and asked if anyone else had seen it commit treason.

Ilyr held the cut wax seal in his palm.

Mara waited.

He closed his fingers around it. "Maelin is my younger sister. She helped me expose the first half of a court lie. I left before I could expose the part that condemned my own house."

"Why?"

He smiled without humor. "Because cowardice is often disguised as strategy by people with education."

Veyanna approached. "This proves Khar Veyl intends to seize you."

"It proves Khar Veyl is as divided as you are," Mara said.

"The road to Lumenorath remains safest."

"No," Caldus said. "It remains nearest to your strength."

The chapel roots shivered, perhaps with offense.

Mara looked north, where the visible road ran toward white-root forests and the hidden road bent below toward a sister not dead, not safe, not silent. She could feel both powers pulling. Saint above. Hazard below.

"We keep moving," she said. "We take the White Road because Serathiel already has her hand on the next gate. But we carry Maelin's message, and we do not let the escort close around us."

"That is almost a plan," Kesh said.

"I am improving."

Ilyr tucked the black paper into Arveth's ledger.

"Mara," he said.

"Yes?"

"When I tell you the rest, you may wish you had left me unnamed."

She thought of ash wights in mud, of Sella Brin, of the quiet writ, of all the records powerful people edited because truth made poor furniture for clean rooms.

"Then tell it before I get sentimental," she said.

He almost smiled.

Behind them, the border chapel rang its bells again.

Ahead, the road forked in ways no map admitted.
""",
    4: r"""## Chapter 4: Tavi's Waking Map

Tavi found the impossible pattern in a mill that had stopped grinding grain and begun drawing circles.

The mill stood where the north road crossed a shallow river, its waterwheel turning though the sluice had been closed for winter repairs. Moss covered the roof. White-root scouts had marked the bridge safe, which made Kesh laugh until Veyanna asked why and he said, "Nothing, I just enjoy optimism in hostile architecture." The miller and his family had fled two days earlier after the stones began scratching maps into spilled flour.

They were still scratching when Mara arrived.

The lower room smelled of damp grain, hot brass, and fear left behind in a hurry. Flour dust lay over everything. Across the floor, the millstones had carved ring after ring into it: circles within circles, some broken, some joined by lines that ran through chair legs and under sacks as if furniture were an inconvenience geography would not indulge. Each time the waterwheel turned, the stones groaned and the pattern deepened.

Tavi stepped into the doorway and went silent.

That frightened Mara more than swearing would have.

"It is a map," the gnome said.

Veyanna looked down at the rings. "Of what?"

"If I knew, I would be insufferable already." Tavi crouched, set her brass listener on the floor, and tapped the outer circle. "This is Harrowmere. Here, Kell Ashgate. Seven Arches. Brassroot relay. Lumenorath rootward axis. Khar Veyl under-road alignment. That ugly bit is probably the Gloamfen or a badly drawn pastry."

Kesh leaned in. "We prefer both."

Tavi did not smile. She touched the central ring.

The flour there had turned gray, then blue-black. The circle was not drawn around a place on any surface map. It sat below them in the pattern, beneath every other line, tugging each route toward itself.

"Orrowen," Ilyr said.

Saelith crossed her arms against a sudden chill. "Orrowen is a dead empire, not a center."

"Dead things can be centers," Ilyr said. "Ask any court."

Mara knelt beside Tavi. The cinder shard at her hip had gone hot enough to sting through leather. Under the scrape of stone she heard a pulse. Slow. Vast. Not heartbeat exactly. Too old, too patient. A sleeping continent might have sounded like that if continents dreamed in grief.

The waterwheel turned.

The map scratched a new line from Lumenorath to Orrowen.

Then another from Khar Veyl.

Then one from every small cinder site Tavi had named.

"That should not happen," Tavi said.

"Say that in a more useful way," Caldus said.

"All right. Imagine every hearth, lamp, regulator, engine, shrine, weapon, and grave-bell built on cinder memory is a cup. They should be separate cups. Some leak, some sing, some explode because humans are enthusiastic and maintenance is a myth. But separate."

"And now?"

Tavi touched the central blue-black ring. The flour trembled around her finger. "Now someone has set all the cups on the same table, and the table is breathing."

No one liked that.

Brakka stood in the mill yard with one hand on the bridge stone. "River dislikes wheel."

"The wheel is closed," Tavi said.

"Wheel still turns."

"Yes, I noticed that in a calm and professional manner."

The Pale Bough escort would not enter the mill. They waited outside where the light was cleaner, hands on sword hilts, while Veyanna watched Mara watch the map.

"Serathiel must see this," Veyanna said.

Ilyr's laugh was dry. "Naturally. The first rule of dangerous knowledge is to hand it to whoever already prepared a doctrine."

"And Khar Veyl would bury it."

"With labels."

"Enough," Mara said.

The millstones stopped.

For one breath the room was quiet enough to hear rain tapping the roof.

Then every brass fitting Tavi carried began to scream.

She dropped three devices before the straps burned her. The listener on the floor unfolded by itself, ribs spreading like an insect made by an angry clockmaker. Needles spun. Glass dials blackened. A paper strip shot from the side covered in numbers so tight they looked like panic.

"Out," Tavi said.

Caldus grabbed the nearest flour sacks and threw them through the doorway. "Everyone out."

"Not the map!" Tavi snapped.

"The map is not breathing smoke."

"That is diagnostic smoke."

Mara caught Tavi by the back of her coat as a brass needle whipped toward her eye. The gnome swore in a language that made Veyanna flinch despite not understanding it.

The waterwheel turned faster.

Outside, the river rose.

Not from rain. From below. Water bulged upward under the bridge in smooth dark humps, each reflecting a different sky. Morning. Night. Stars underground. A white forest burning. A black hall flooded with mirrors. The dead city of Orrowen seen from above though it lay below, its towers hanging downward like teeth.

The refugees on the road began shouting.

Root-hounds burst from the tree line.

They were gnome-bred ward beasts, Tavi had told Mara once, though bred was too tidy a word for things assembled from bone, root, brass scent-cages, and loyalty contracts. These three had broken their handlers or outlived them. Their bodies were lean and low, their muzzles plated in copper, their paws leaving sparks wherever they touched wet stone. They were not hunting flesh. Their blind faces turned toward Tavi's devices.

"My guild marks," Tavi said.

Kesh drew knives. "Your guild has enthusiastic dogs."

"Ward beasts."

"Enthusiastic tax categories."

The first root-hound leapt for the mill door. Brakka met it with the haft of her maul and knocked it sideways into the mud. It rolled, rose, and opened its copper muzzle. The sound that came out was a regulator command, high and precise.

The ash wights under the refugee cart covers stirred.

Mara's blood went cold.

"They are calling hooks," Saelith said.

Veyanna's blade flashed into her hand. "Destroy them."

"No," Tavi said.

"They will wake the dead."

"They are waking everything because my people built them to amplify leaks instead of admit failure."

The second hound hit the bridge. Caldus intercepted, staff cracking across copper jaw. He was slower with the bad leg, but more economical now, no wasted heroics. The hound's command shriek cut off. The named dead under the cart covers settled as Bessa and Fenna held them, saying names, names, names.

Mara reached for the cinder and found the old dragon word waiting.

No.

She reached past it.

Under the hounds' command-sound was pain. Not person-pain, maybe, but pressure, purpose twisted until the creatures had no world except leaks to track and orders to obey. The cinder shard translated too eagerly: Break. Burn. Silence.

Mara asked instead, What are you following?

The answer came as smell, map, hunger: blue-black pulse, brass guilt, Tavi's maker-mark, Orrowen below, all roads drawing inward.

"Tavi," Mara shouted. "They are following your signature."

Tavi stared at the screaming listener. "Of course they are."

"Can you change it?"

"My professional pride says no. My criminal instinct says probably."

"Use the useful one."

Tavi dove back into the mill.

The third hound followed. Kesh dropped onto its back from the roof, which raised several questions no one had time to ask. It bucked. He clung to the copper muzzle with one hand and jammed a chapel root-pin into its scent cage with the other.

"I regret!" he yelled. "Several choices!"

Brakka seized the hound by the hind legs and dragged it backward. "Keep regret centered."

Inside the mill, Tavi shoved both hands into the unfolded listener. Sparks climbed her wrists. She screamed once, furious rather than afraid, and twisted something Mara could not see.

The map on the floor changed.

The central Orrowen ring brightened. Lines that had pulled inward snapped outward, then settled into a truer shape. Not one table. A web. A wound-web. Cinder sites did not simply answer Orrowen. They had been wired to do so by old design, then patched by centuries of regulators, hymns, seals, and lies. Now the patches were failing because the dragon-moon beneath the world had begun to stir.

The root-hounds stopped attacking.

One by one, their muzzles lowered.

The river fell back into its banks.

Tavi stumbled from the mill with smoke rising from her sleeves and the listener clutched to her chest. "I need everyone to appreciate that I did not explode."

"We are overwhelmed," Kesh said from the mud, still lying across a root-hound's back.

Veyanna stared at the map visible through the doorway. "This cannot leave here."

"It already has," Ilyr said. "The pattern is under every road."

"Then it must be contained."

Tavi turned on her. Her face was streaked with flour and soot. "Contained is what my guild wrote on the first regulator contracts. Contained is what humans wrote above foundry dead. Contained is what you write on people before arranging them in chapels. The word has lost credibility."

Veyanna's mouth tightened. "And your alternative?"

Tavi looked at Mara.

That was unfair. Everyone kept looking at Mara when the right answer did not want to be born.

Mara stepped back into the mill. The floor map trembled around her boots. At the center, beneath the flour, something blue-black pulsed.

"We copy it," Mara said. "All of it. For Serathiel. For Khar Veyl. For Brassroot. For Bessa's road camp if they want to know why their soup kettles sing at night. No one owns the first warning."

"Open knowledge can start panic," Veyanna said.

"Hidden knowledge already started a war."

Ilyr looked at Mara then, and something in his guarded face bent toward respect.

Tavi let out a shaky breath. "I will need paper, charcoal, three dry boards, and nobody saying the word impossible for an hour."

"Impossible," Kesh said.

She threw a flour scoop at him.

They spent the afternoon copying the waking map while rain softened the road and root-hounds slept uneasily beside the bridge. Mara knelt in flour until her knees ached, tracing lines that made no political distinction between beautiful Lumenorath, secret Khar Veyl, practical Brassroot, stubborn Seven Arches, hungry human towns, goblin roads, and the dead empire below.

Everything was connected.

That did not make the world holy.

It made every lie structural.
""",
    5: r"""## Chapter 5: Road Tax in Blood

The Kavik caravan crossing floated on the marsh like an argument that had learned carpentry.

Painted wagons stood on platforms lashed to blackwood piles. Rope bridges sagged between them. Lanterns burned green over water the color of old tea. Little boats nosed through reed channels carrying baskets, children, knife-grinders, brass parts, dried fish, gossip, and at least one goat with a legal ribbon tied around its horns. Bells hung everywhere, but none matched. They rang when the wind shifted, when a plank moved, when a stranger stepped where a stranger had not paid to step.

Kesh stopped at the first bridge and looked homesick in a way Mara had never seen on him.

Then a bell rang sharp above his head.

Every goblin in sight turned.

"Ah," Kesh said. "I remain beloved."

A crossbow bolt struck the plank between his boots.

"With nuance," Tavi said.

From the nearest wagon roof, a goblin woman in a red coat stood with one foot on a chimney pipe and a crossbow in her hands. Her braids were threaded with coins, bone tags, and tiny road bells. Her smile was Kesh's smile if Kesh's smile had survived three more betrayals and become management.

"Kavik road remembers Kesh-of-No-Receipt," she called.

Kesh put a hand over his heart. "Aunt Rikka. Your hospitality remains projectile."

"You owe six clans, three widows, two ferry sisters, and a mule."

"The mule was a misunderstanding."

"The mule wrote a song."

Mara looked at him.

"I was younger," he said.

"This was last spring," Rikka called.

The Pale Bough escort waited at the marsh edge with visible distaste. White boots did not enjoy floating markets. Veyanna had argued for taking the chapel road around the marsh. Ilyr had argued that every official road between here and Lumenorath now belonged to someone trying to arrange Mara. Brakka had listened to the marsh pilings and declared them rude but honest. That had settled it.

Now the crossing refused to lower the bridge.

Behind Mara, the refugee wagons bunched along the bank. They had split from the larger road camp after Tavi's map, carrying three copies hidden in three unpleasant places Kesh had suggested. Bessa's soup kettles had gone west under troll mark. Fenna and the quiet writ had gone toward the Seven Arches. Mara's company had kept the smallest and most dangerous caravan: the copied map, Arveth's ledger, Maelin's message, three named dead who insisted on seeing Lumenorath accuse them in person, and enough witnesses to make every faction nervous.

The marsh bells rang again.

Rikka aimed at Kesh's hat this time. "Payment."

Kesh removed the hat before she could improve it. "We need passage."

"Many need passage. Passage is what makes passage expensive."

"We carry warning."

"Everyone carries warning. Some wrap it around theft and call it public service."

Mara stepped forward. The nearest platform dipped under her boot. Marsh water sucked at the piles. Somewhere in the reeds, something large exhaled.

"We can pay in work," she said.

Rikka's eyes flicked to her burned hand, the cinder cage at her hip, the gray-coated light elf, the dark-elf exile, the gnome devices, the troll maul, Caldus's staff. "You are the banner girl."

"No."

"Good. Banners are terrible negotiators. What work?"

Before Mara could answer, the marsh sang in a child's voice.

Not a song. A lure.

The bells went silent all at once.

Every goblin on the platforms dropped low.

Kesh seized Mara's sleeve and yanked her down a heartbeat before a reed as thick as a spear whipped through the space where her throat had been.

The water erupted.

Reed giants rose from the channel.

They were not true giants, not like stories painted in taverns. They were marsh things that had learned the shape of height: bodies woven from black reeds, old bones, fish spines, and the waterlogged armor of travelers who had followed the wrong bell. Their heads were hollow cages. Inside each, memory moths flickered pale as fingernails. When they opened their mouths, they spoke in borrowed voices.

"Mara," one called in Joryn's voice.

Her body moved toward it before thought caught up.

Caldus hooked his staff across her chest. "No."

The reed giant's head tilted. "Mara, come here. Road's safe."

Joryn's cadence. Joryn's impatience. Joryn's love turned into bait.

Rage went through her so cleanly it almost became command.

The marsh erupted in motion. Goblin roof-guards fired bolts trailing red thread. Children vanished into wagon trapdoors. Rikka slid down a rope, kicked a lantern into one giant's hollow head, and shouted prices for rescue as if battle were an auction. Kesh was already moving across the rope bridge, cutting bells from their lines and throwing them into the water.

"Why bells?" Mara shouted.

"They mimic what answers!"

Tavi dropped to her knees beside the first platform and shoved a probe into the marsh. "Cinder leak under the crossing. Old one. The memory moths are feeding on spoken names."

Saelith drew light into her hands. "How do we stop them?"

"Stop saying names!"

"That is an unusual tactic for us," Ilyr said.

The second reed giant hauled itself onto the platform where the three named dead waited under canvas. Its hollow head spoke in three voices at once, each voice stolen from someone the dead remembered. The dead froze.

Brakka hit the giant with her maul.

It broke beautifully and reassembled badly.

"Annoying marsh," she said.

Rikka landed beside Kesh. "You brought this?"

"It was here before me."

"So was your debt."

"Can we put both in the minutes?"

The first giant lunged again, wearing Joryn's voice. Mara did not answer the voice. She looked at the water under it, at the moths flashing inside the reed cage, at the way the creature's feet tangled in old road chains below the surface.

Roads remember unpaid debts.

"Kesh," she said, carefully not saying anyone else's name. "What debt does this crossing owe?"

His eyes snapped to the water. "No."

"What?"

"No, that is clan shame and highly specific."

Rikka fired a bolt through a moth cluster. "It is also why we are dying, idiot nephew."

Kesh's face changed. The joke left it.

"The first Kavik crossing took payment from refugees during the salt famine," he said. "Too much payment. Some drowned trying to go around. The marsh remembers the voices of those who called from the water. We built bells to confuse the lures."

"And kept charging," Mara said.

"We kept surviving."

"Both can be true."

That hurt him. It needed to.

The reed giants closed in. The Pale Bough escort tried to join the fight from the bank, but their white-root blades slid off wet reed without cutting deep. Veyanna sang a preservation hymn that froze one giant in a perfect glassy shape for three breaths, then the marsh broke it open from inside.

Tavi's probe sparked. "If we vent the leak, the moths scatter."

"Vent where?" Caldus asked.

"Up."

"That is where we keep our heads."

"I am aware of design drawbacks."

Kesh looked at Rikka. "Blood tax."

Her face went flat. "Do not be dramatic."

"It is literally named."

"It is also symbolic."

"Then you should have named it less specifically."

He drew his knife and cut his palm before anyone stopped him. Goblin blood, dark and bright at once, hit the plank. Rikka swore. Every bell on the crossing rang once.

Kesh pressed his bleeding hand to the old toll board nailed beside the bridge. "Kesh of the Kavik Road acknowledges debt carried under charm, joke, contract, and cowardice. Passage taken from the drowning is unpaid. Passage sold to the hunted is not clean. My name stands surety for this caravan and for three crossings of refugees under witness."

Rikka stared at him. "You cannot stake that much reputation."

"Watch me diversify."

The toll board drank the blood.

Under the marsh, old chains rose.

Not to bind the living. To bind the leak. Iron links surfaced through black water, each carrying carved names softened by silt. The reed giants screamed in all their stolen voices as the chains pulled the cinder seep open and upward. Blue flame burst from the channel in a thin line. Memory moths swarmed toward it.

"Now!" Tavi yelled.

Mara opened the cinder cage only enough to let heat answer heat.

She did not command the moths. She witnessed what they had eaten.

Hunger. Lost voices. Refugees turned away. Goblin children taught never to count what survival cost because counting made hands shake. A mule song, wildly inappropriate, somehow threaded through the grief. The marsh was ridiculous and cruel and alive with unpaid records.

"Witnessed," Mara said.

The blue flame turned white.

The moths flew into it and vanished.

The reed giants collapsed into ordinary reeds, old bones, and armor nobody wanted to claim.

Silence fell. Then every mismatched bell on the crossing rang again, softer.

Kesh swayed.

Rikka caught his wrist, saw the blood mark on the toll board, and for once had nothing sharp ready.

"Three crossings," she said.

"I may have gotten carried away."

"You staked your road-name."

"It was cluttered with complaints."

"Kesh."

He looked at her.

The humor did not return.

"They are hunting witnesses," he said. "Not heroes, not saints, not profitable fools. Witnesses. If we charge them like ordinary cargo, we become the road that taught the marsh to sing."

Rikka's jaw tightened. Around her, goblins pretended not to listen with the focused discipline of family.

At last she spat into the water. "Three crossings. Refugees under witness. No shrine banners. No holy discounts. Anyone claiming to travel as Mara Venn's official anything pays double for being annoying."

"Fair," Mara said.

Rikka pointed at her. "And you. Banner girl who says no. You pass because my fool nephew has placed his name where money should be."

"I know what that costs."

"Do you?"

Mara looked at Kesh's bleeding hand, at the toll board, at the channels where old chains sank back into black water. "I am learning."

Rikka studied her, then kicked the bridge lever.

The first rope bridge lowered.

The caravan crossing opened by inches, bells ringing them in.

As they stepped onto the swaying planks, Kesh leaned close. "For the record, I hate meaningful personal growth."

"Invoice me," Mara said.

"I just did."

Below them, the marsh settled. Not healed. Not absolved. But changed.

Behind them, the Pale Bough escort crossed with expressions of restrained horror. Ahead, painted wagons shifted to make a road no map would admit existed.
""",
    6: r"""## Chapter 6: A Commander by Accident

The rebel camp smelled of wet wool, boiled turnips, sharpened iron, and the dangerous relief of people who had found someone else to blame.

It occupied the old quarry above the White Road, where pale roots began to thread through black stone and the marsh gave way to fir slopes. Rain had turned the quarry floor to gray paste. Tents leaned against abandoned cutting frames. Cooking fires smoked under tarps. Someone had painted the open bowl on three shields and Mara's hand on six more, despite every correction carried north by every exhausted messenger. Symbols traveled faster than consent. Tavi said this with academic disgust. Kesh said it with a gambler's admiration. Mara said nothing because if she started, she might not stop.

Two hundred people had gathered there.

Not an army. Not yet. That was what made them dangerous.

Miners from Kell Ashgate stood beside Harrowmere apprentices, escaped palace servants, road-camp guards, three Kavik scouts, and a dozen human soldiers who had abandoned royal colors without abandoning the habit of forming lines. Some had come to protect refugees. Some had come to join the Ash Hand, a thing Mara had not founded and already despised. Some had come because a rumor claimed she could wake the dead and send them against the Pale Bough. Those people avoided looking at the three named dead traveling under canvas shade.

At the quarry's center, a man with a red scarf stood on a stone block and shouted over the rain.

"The white-roots are ahead of us by half a day," he cried. "Their saint-general gathers blades in Lumenorath. Their escort cages our own witness under courtesy. Khar Veyl sends shadows. Harrowmere loyalists regroup west. If we wait, we die in committees. If we strike the Pale Bough supply train tonight, we show them the Ash Hand has teeth."

Cheers rose.

Mara looked at Caldus. "Who is that?"

"Darron Pell. Quarry foreman. Lost two sons in a crown levy."

"And gained a speech habit."

"Grief often recruits volume."

The red-scarfed man saw her.

The cheer changed shape.

Mara felt it come toward her: hope, hunger, vengeance, relief. All of it searching for a place to put its weight. She wanted to step aside. There was no aside. Behind her stood the refugee wagons. Ahead, the road to Lumenorath. Underfoot, cinder lines tugged toward Orrowen. Around her, people were preparing to kill in her name because mercy felt too slow.

Darron Pell dropped from the stone and pushed through the crowd.

"Mara Venn," he said. "We held the quarry for you."

"I did not ask you to."

That answer landed badly.

He recovered with the quickness of someone who had argued with crews and hunger. "No. You did more. You showed us asking is how they keep us kneeling."

Kesh made a pained sound. "That sentence is going to cost lives."

Darron's eyes flicked to the goblin, dismissed him, then returned to Mara. "We have eighty fighters fit enough to move. The Pale Bough supply train carries root-blades, hymn bells, and prison silk. We strike before moonrise, take what we can, burn the rest, and send one survivor back to Serathiel with your mark."

"No," Mara said.

The word was too small for the quarry. It vanished under rain and restless feet.

Darron leaned closer. "You have not heard the plan."

"I heard enough."

"They will come for us."

"Yes."

"They will put collars on the named dead."

"If they can."

"They will call you saint and use you until nothing of you is left."

"Probably."

"Then why are you standing there like refusal is strategy?"

That stung because she had asked herself the same question in every mile since Kell Ashgate.

Before she could answer, a woman near the front shouted, "My sister was taken by white-roots!"

Another voice: "Mine by crown men!"

"Mordane is gone because she fought!" someone yelled. "Let her fight!"

Let her.

Not fight with her. Not ask her. Let her. As if Mara were a locked furnace they had a moral right to open because their grief was real.

Saelith stepped forward, pale with anger. "The supply train carries wounded."

Darron turned on her. "Your people say that when they hide blades behind blankets."

"Sometimes they do," Saelith said. "Sometimes wounded are wounded."

"Convenient."

"Yes," she said. "Truth often is inconvenient in both directions."

The crowd muttered.

Veyanna and the Pale Bough escort had halted at the quarry edge, hands near hilts. Their presence made every human fighter more furious. Ilyr had disappeared into the cutting frames. Tavi was already inspecting the quarry crane, which meant either escape route or catastrophe. Brakka stood beside the three named dead, a quiet wall.

Caldus spoke low. "If you simply forbid them, half will go anyway."

"If I agree, they all go."

"Yes."

"I hate command."

"Good commanders often do."

"That is not comforting."

"No."

The rain intensified. Water ran down Mara's neck. Mud sucked at her boots. The cinder at her hip warmed, sensing the crowd's desire for a voice that would make choice easy. She could give them one. She knew that now. Not by shouting. By singing through the buried heat under the quarry, by striking grief until it rang in one direction. The thought horrified her because part of her wanted to know if she could.

Do not answer too quickly.

Mara climbed onto Darron's stone.

The quarry quieted in pieces.

"You want to hit the supply train because it is close," she said.

Darron's jaw tightened. "Because it is enemy."

"Because it is close," Mara repeated. "Because you can imagine winning against wagons. Because losing children to crowns and roots and command hooks leaves anger with nowhere clean to stand. I know."

"Do you?"

Mara held up her burned hand.

The crowd looked at the scars. That was another kind of trap. Pain made easy credentials.

"I know enough not to spend your grief badly," she said.

A murmur moved through them.

"The supply train has wounded," she continued. "It has blades too. It has hymn bells that can cage memory if Serathiel's people have tuned them. It has scouts waiting for exactly this attack because angry people are easier to predict than hungry ones. If we strike it as Darron plans, we kill some healers, capture some blades, lose thirty people, and give Serathiel proof that every refugee camp raising my name is an insurgent nest."

"So we do nothing?" someone shouted.

"No. We do the harder thing."

Tavi looked up from the crane. "I adore and fear that phrase."

Mara pointed toward the north ridge. "We move the wounded and the named dead off the White Road before the train passes. We send three unarmed witnesses under Brakka's road mark to demand inspection of the hymn bells. We make the demand in front of Veyanna's escort, Kesh's scouts, Caldus's soldiers, and every person here who can repeat what happens accurately. If the Pale Bough refuses, they refuse in public. If they attack, they attack witnesses. If the bells are clean, we do not invent guilt because we need somewhere to put our rage."

The quarry did not like that.

Neither did Darron.

"Inspection?" he said. "You want us to ask politely?"

"I want you alive tomorrow with truth that can travel."

"Truth does not stop blades."

Brakka's voice rolled over the quarry. "Untrue."

Everyone looked at her.

"Truth stops wrong blade in right hand. Not all. Enough sometimes."

Kesh murmured, "Put that on a less flammable banner."

Darron jabbed a finger toward the Pale Bough escort. "They will twist any public moment. Elves live on ceremony."

Saelith's face tightened, but she did not deny it.

Ilyr's voice came from atop a cutting frame. "Then make the ceremony carry more than one record."

He dropped lightly to the ground and held up three small black slates. "Khar Veyl witness slates. They record light, sound, and lies by omission poorly but usefully."

Veyanna stiffened. "Those are forbidden in Lumenorath."

"Many useful things are."

Tavi raised a hand. "I can attach one to the crane arm and swing it over the road for an excellent viewing angle."

"Why were you already planning that?" Caldus asked.

"Because I believe in civic visibility."

"Because you wanted to play with the crane."

"Multiple truths can improve a society."

The crowd's anger wavered. Not gone. Never gone. But forced to share space with method.

Darron saw it and grew desperate.

"She is making you weak," he shouted. "Mordane fell because we stopped waiting. Kell Ashgate rose because people finally took fire in their hands."

"Kell Ashgate rose because people stopped letting men like Mordane decide who could be spent," Mara said. "I will not become a prettier version of his arithmetic."

The quarry went quiet enough for rain to speak.

Darron's face reddened. "My sons died."

"Tell me their names."

He recoiled. "What?"

"Tell me their names before you ask strangers to die in the shape of them."

The cruelty of that question hit Mara only after she asked it. Caldus looked at her sharply. Saelith closed her eyes. Kesh stopped smiling altogether.

Darron stared at Mara with hatred bright enough to warm the rain.

"Pell and Haden," he said. "Pell was named for my father. Haden for hers. They were seventeen and nineteen. Crown levies took them east. One came back as a hook-soldier. One did not come back enough to bury."

Mara bowed her head.

Not deeply. Not theatrically. Enough.

"Pell and Haden are witnessed," she said. "Not as permission. As people."

For a moment, Darron looked as if he might strike her.

Instead he stepped off the stone.

"Do your inspection," he said. "When it fails, do not ask me to clap for wisdom."

"I will not."

The next hour turned the quarry from mob into work, which was less inspiring and more useful. Caldus split fighters into escort, evacuation, and reserve groups, giving orders as suggestions until people obeyed them and then pretending not to notice. Brakka marked the unarmed witness party with road-law mud across their palms. Kesh chose three Kavik scouts with the expression of a man lending out favorite knives. Tavi rigged the crane arm with slates, wire, and a pulley that threatened everyone equally. Saelith went tent to tent asking the wounded what they wanted if the Pale Bough train offered healing. Some said yes. Some said never. She wrote both answers down.

Mara found Veyanna at the quarry edge.

"Will your people allow inspection?" Mara asked.

Veyanna's leaf-veiled eye rested on the busy camp. "You are learning command."

"That was not my question."

"No. Serathiel's train will not allow hostile inspection."

"Then call it witness."

"That may work once."

"Once is tonight."

Veyanna almost smiled. "You dislike symbols, yet you make them."

"I dislike cages. Tools are different."

"Every cage begins as a tool someone trusts."

That was too true to answer quickly.

At dusk, the Pale Bough supply train appeared on the White Road below: six wagons drawn by white-root harness, lanterns glowing under rain, wounded lying beneath silk covers, blade-bearers walking in pairs, hymn bells hanging from the lead axle. Their sound was gentle. Too gentle. It made Mara want to sleep, kneel, forgive, and forget the order of those desires.

She stood on the quarry rim with mud on her boots, rain in her hair, and two hundred angry people waiting to see whether refusal could lead.

"No one moves unless they strike witnesses," she said.

Darron stood below her with his jaw clenched and his sons' names raw between them.

The witness party walked down under Brakka's mark.

The hymn bells rang.

For one heartbeat, the quarry leaned toward blood.

Mara held up her burned hand.

Not as banner. Not as saint.

As stop.
""",
}


EXPANSIONS: dict[int, str] = {
    1: r"""The work after the fight took longer than the fight, which was how Mara knew it mattered.

The ash wights had to be moved without pretending they were cargo. Bessa found three doors, laid them over barrels, and announced that anyone who said bier in a dramatic voice would be assigned latrine duty. The beardless miner who had painted Mara's hand on the banner helped carry the first body. He wept while doing it, not because he knew the soldier, but because the body was heavier than the idea of rebellion had been.

"What do we write?" he asked.

Ilyr stood beside a plank with Arveth's copied ledger open and rain spotting the page. "Unknown soldier, crown road ditch. Hook unstable. Witnessed resisting command."

"That sounds cold."

"It is a record, not a funeral song. We can have both, but one must survive bad weather."

The miner looked to Mara as if she could improve death by phrasing. She shook her head. "Write it exactly."

He did.

The named dead from the road camp watched with unnerving stillness. One of them, Halea Voss's former student named Edrin Vale, asked for charcoal and added his own note beneath Ilyr's line in a hand made clumsy by death: Did not strike child when commanded. That, too, was a record. Not absolution. A fact. Facts were smaller than mercy and more stubborn than grief.

By afternoon, the camp had changed its sign.

The new cloth showed an open bowl beneath a line of small marks, each mark different. A pick. A needle. A child's slate. A guard's broken spear. A white root crossed out, then repainted as a root with a question mark because Bessa said the first version would get them killed and the second might get them argued with. Under the bowl, the beardless miner painted words in uneven black:

EAT. SPEAK NAME. LEAVE FREE.

"It is not poetry," Saelith said.

"Good," Bessa replied. "Poetry gets people founding orders."

Mara helped carry flour sacks until her burned hand throbbed. Caldus tried to stop her once. She gave him the look Dilla had taught her, and he retreated with tactical dignity. Tavi repaired the western kettle with a copper patch and charged Bessa one promise that nobody would put holy water in it without asking the soup. Brakka and two troll masons raised stepping stones through the worst mud. Kesh taught children how to spot a forged ration token, then acted offended when Rella's cousin spotted the one in his sleeve.

It should have felt like rest.

Instead, the fallen banner kept drawing Mara's eye.

It lay beside the ditch in two stained pieces. The painted hand had torn across the palm, dividing the coal circle in half. Refugees stepped around it all day. No one threw it away. No one wanted to touch it. At last Mara picked it up herself.

The cloth was wet and cold. She expected the cinder at her hip to warm, but it stayed quiet. The symbol had never been powerful because of her. It had been powerful because hungry people needed a place to hang what they could not carry alone.

That frightened her more than worship.

Near dusk, Joryn's token knocked against the cinder cage as she tucked the torn cloth into her pack.

Saelith saw. "You are keeping it?"

"Evidence."

"Against whom?"

Mara looked at the soup line, the new bowl sign, the dead soldiers recorded under rain, the road stretching north toward powers already deciding what to call her.

"Against me, if I start liking the wrong version."

Saelith nodded as if that answer deserved more ceremony than either of them trusted. "Then I will remember you said it."

"That sounds threatening."

"A little."

Mara smiled despite herself.

The smile did not last. At sunset, the road beneath the new sign pulsed once, slow and deep. Every bowl in the soup line trembled. Every named dead lifted their head. Far off, where the north road bent toward the white-root border, bells answered with a sound too graceful to be friendly.

Veyanna's escort was coming.

Bessa spat into the mud. "Saint-makers."

Mara looked at the open bowl, at the line of marks, at the words leaving people a way out.

"Feed them too if they ask," she said.

Bessa's eyes narrowed. "That mercy or strategy?"

Mara shouldered her pack. "I am hoping there is overlap."
""",
    2: r"""Night inside the border chapel was worse than danger because it was almost beautiful enough to forgive.

The roots dimmed to pearl. Rain whispered down living gutters. Refugees slept under woven alcoves that adjusted themselves to cradle sore backs and feverish children. The named dead sat where they had chosen: two in a side court open to the wet air, one in the chapel library with a book resting unread in his lap because he liked the weight. Every object had a place. Every place had a purpose. Even the pantry shelves seemed morally composed.

Mara distrusted it with her whole tired body.

She carried flour with Bessa until a chapel attendant tried to take the sack from her hands and called the labor inappropriate. Bessa asked inappropriate to what. The attendant said to station. Bessa said the sack's station was on the shelf and anyone blocking its destiny could move. Mara laughed so hard she nearly dropped it.

That laugh cost her.

People turned toward it. Not everyone. Enough. Refugees, attendants, blade-bearers, even one of the named dead. They watched the laugh as if it revealed a relic under common cloth. Mara closed her mouth.

Bessa noticed. Of course she did.

"Do not let them steal ugly sounds from you," she said.

"My laugh is ugly?"

"Most honest things are a little ugly."

In the chapel court, Veyanna had arranged a witness table. The phrase sounded harmless until Mara saw the shape of it: three pale chairs on one side, one plain stool on the other, a root-lantern above that brightened whenever the person on the stool spoke. Refugees were invited to tell what they had seen in Harrowmere, Kell Ashgate, and the road camp. Invited. Such a soft word. Blade-bearers stood at the door. Scribes copied every answer into luminous bark sheets.

Fenna Clay came away shaking.

"They asked when I first saw you touch the cinder," she told Mara.

"Not when Mordane ordered the dead moved?"

"They asked that after. But first, you."

Mara walked to the table before thinking better of it.

Veyanna looked up from the bark sheets. "Do you object to preservation of testimony?"

"I object to organizing every testimony around me."

"You are the event through which many understood the harm."

"Mordane was the harm."

"Lord Mordane was one expression of it."

That was true. Mara hated when wrong people carried true pieces.

"Then ask about the system first," Mara said. "Ask who paid. Ask who signed. Ask who looked away. Ask whose ovens stayed warm because miners did not. Ask the named dead what they want recorded before you decide what their existence proves about my soul."

The root-lantern brightened over her though she was not on the stool.

Every scribe wrote.

Mara stopped. "Do not write that as doctrine."

One scribe's quill froze.

Veyanna folded her hands. "You cannot control what your words become."

"I can object early."

"And often, I suspect."

"You learn quickly."

Across the court, Saelith stood in the shadow of a white pillar. She was watching the table, not with surprise, but with memory. Mara crossed to her.

"Was this how they trained you?"

"No," Saelith said. "Training was kinder."

"That is not comforting."

"It was meant to make obedience feel like relief. After drills, after hunger, after hours singing until our throats bled, the law would finally tell us where to stand. We mistook the end of uncertainty for peace."

Mara leaned beside her against the pillar. "What happens if you go back?"

Saelith's eyes followed Veyanna. "They will offer restoration first. Then correction. Then containment presented as rest."

"And if you do not?"

"Then I become an example."

The root wall beside them hummed. In its preserved layers, Mara heard Saelith's young voice again, then another voice correcting it, smoothing the edge from a note until the child sounded less alive and more perfect.

Mara touched the wall only with one knuckle.

"Saelith Dawnmere," she said softly, "is witnessed refusing restoration."

Saelith looked at her.

"Too formal?" Mara asked.

"No." Saelith's face opened in a way that made the chapel seem suddenly less luminous. "No, it is exactly formal enough."

At the witness table, Veyanna's quill moved.

Mara pointed at her without looking away from Saelith. "And that is not yours."

For once, Veyanna did not write.
""",
    3: r"""They did not leave the chapel cleanly.

No one ever left a place like that cleanly. The roots held memories in their walls, and memories had hooks even when no one meant harm. A boy from the refugee wagons refused to step beyond the north arch until Saelith promised the chapel had not kept his mother's name. A named dead woman asked whether preservation was a kindness if decay no longer frightened her. Veyanna gave an answer so elegant that Mara saw the woman almost accept it before remembering to ask herself.

"Sun," the woman said at last.

Brakka carried her outside.

The Pale Bough escort did not approve, but disapproval had difficulty arguing with a troll carrying a citizen into morning light.

Ilyr walked at the caravan's rear. Mara let him, for a while. There was mercy in not pursuing a wound the moment it showed itself. There was also cowardice. She was still learning the difference.

At the first rise beyond the chapel, she slowed until he came level.

"You said Maelin was your sister," she said.

"I noticed."

"That was not the whole answer."

"No."

The road climbed through fir and white-root saplings. The roots did not own the forest yet, but they were trying. Pale threads looped around old trunks, threaded through moss, crossed stones with the polite persistence of law arriving before consent. Khar Veyl's hidden road ran somewhere beneath them. Mara could feel it occasionally, a cool pressure under her left foot, as if the earth remembered a second path and resented the one on top.

Ilyr kept his eyes ahead. "Maelin was better than I was at three things: sword forms, court patience, and refusing to let cleverness become an excuse."

"Older or younger?"

"Younger by twelve years. Older by moral inconvenience."

"I would like her."

"Everyone did. That was part of the problem."

He stopped beside a stone where black lichen grew in the shape of script. The others continued ahead, close enough to intervene, far enough to pretend privacy. Kesh glanced back once and then loudly accused Tavi of overpacking, which drew her into an argument usefully noisy enough to cover pain.

"Khar Veyl teaches children that truth is a blade," Ilyr said. "A blade must be sheathed, sharpened, drawn for purpose. The surface leaves truth lying about like broken glass, and then acts surprised when everyone bleeds. I believed this. I still believe some of it."

"And Maelin?"

"She believed truth was also bread. Useless if locked away by people congratulating themselves on restraint."

Mara thought of Bessa's flour shelves, of the witness table, of ledgers people died to keep open.

"What was the lie?"

Ilyr's mouth tightened. "The old split between Lumenorath and Khar Veyl. We were taught the Elyri sought to cleanse all shadow after the dragon war, and the Veyra alone preserved the dangerous record. That is true. It is also incomplete in the way a knife is incomplete if one describes only the handle."

"Your house profited."

He looked at her sharply.

"Maelin's message said half-truth. Your face said the rest."

For a moment he seemed irritated enough to become himself again. Then it passed.

"House Noct-Vey guarded one of the first seals over the dragon-moon. We discovered fractures generations ago. Instead of warning both courts, we sold controlled access to selected memories. To light-elf hardliners who wanted proof of ancient guilt. To Veyra hardliners who wanted proof surface peace was impossible. To human cinder ministers who wanted extraction methods without admitting sources."

Mara felt cold spread through her.

"Mordane?"

"Not directly. His teacher, perhaps. His ministry's earliest regulator designs carried under-script from our vaults."

The road tilted.

For a heartbeat she saw Joryn chained in the foundry, Arveth ash in the furnace, Sella Brin erased from a quiet writ, and beneath them a dark-elf house selling old truth in measured doses because poison was profitable if labeled medicine.

Ilyr did not look away.

"I exposed the trade to the Umbral Seat," he said. "But I hid our sale to human ministers because I thought Khar Veyl would collapse into civil blood if humans learned enough to accuse us before we accused ourselves. Maelin called that cowardice. I called it sequence."

"And then?"

"She took the missing records. I fled with the lesser proof. She was caught."

The word sat between them, too small.

Mara wanted to say something kind. Kindness arrived carrying soft lies, so she made it wait.

"You should have told me before," she said.

"Yes."

"I am angry."

"Yes."

"I may stay angry."

"You have precedent."

That almost made her smile. Almost.

The cinder shard warmed, not with command, but with attention. Under the road, something old listened to guilt with terrible patience.

"I am not leaving you unnamed," Mara said. "But I am not carrying your truth for you either."

Ilyr bowed his head. "That is fair."

"No. It is what I can afford."

Ahead, the Pale Bough escort had stopped at a rise where the White Road began in earnest, pale and smooth as bone through the trees. Lumenorath's first distant towers shimmered above the forest, impossibly slender, like moonlight taught to stand.

Ilyr looked at them with open dislike.

"Beautiful," Mara said.

"Yes."

"You say that like an accusation."

"It often is."
""",
    4: r"""The copies of the waking map refused to stay still.

Tavi made six before admitting the problem was not her handwriting, which took longer than honesty strictly required. Charcoal lines shifted on paper whenever the pages passed near a cinder lamp, a chapel root, Ilyr's black seal fragments, or Mara's hip. The Orrowen circle always moved first. Then the roads. Then the smaller sites, twitching like nerves.

"Maps are agreements with arrogance," Tavi said, pinning one sheet under four stones. "The world is violating basic courtesy."

They had camped in the abandoned mill yard because the root-hounds would not leave. Three of them lay beside the bridge with muzzles on paws, blind copper faces turned toward Tavi whenever she moved. The Pale Bough escort wanted them destroyed. Brakka said beasts that stopped biting when told the truth deserved a better hearing than several kings. Kesh tried feeding one dried fish. It ate the fish, the wrapper, and part of his glove.

"That is affection," Tavi said.

"That is invoicing," Kesh replied.

Near the river, Saelith helped a wounded refugee decide whether to accept chapel thread in a torn muscle. Accepting would heal faster. Refusing would avoid luminous root in human flesh. Saelith laid out the choice without leaning on either side, though Mara could see how badly she wanted to mend the pain. That restraint cost her. It made the healing slower and truer.

Mara sat with Tavi by the map boards.

"You said your guild marks drew the root-hounds," she said.

Tavi did not look up. "I hoped we might enjoy a brief period where no one explored my tragic professional history."

"Was it your first invention?"

"No. My first invention was a kettle valve that screamed when water boiled. Brassroot called it unnecessary. My grandmother called it honest. Several neighbors called it unforgivable."

"Tavi."

The gnome sighed and set down the charcoal.

"I built a flood regulator for Low Fen Gate when I was sixteen. It worked. Saved a town. Very dramatic. Speeches. Apprenticeship offers. My mother cried on three officials, which remains one of my proudest memories."

"And later?"

"Later the Compact sold the design to border forts. Someone discovered that if a regulator can release floodwater away from a town, it can release floodwater toward an army, a village, a negotiation one dislikes." She tapped the Orrowen circle. "I said that was misuse. Everyone says misuse when a tool does what the tool permits and the owner has poor morals."

Mara thought of Mordane saying winter, arithmetic, necessity.

"So you keep building?"

"Yes."

"Why?"

Tavi's jaw set. "Because not building did not unmake the first design. Because people with worse questions kept improving it. Because guilt is not a craft plan. Because sometimes a device in the right hands does save the town, and I refuse to leave every lever to people who call casualties optimization."

The waterwheel creaked though no water pushed it now.

Mara looked at the map. "Can this be used as a weapon?"

"Absolutely."

"Can you stop that?"

"Absolutely not."

"Comforting."

"I can make misuse harder. I can make copies so no one faction owns it. I can mark uncertainties instead of pretending accuracy. I can refuse to build the next thing someone asks for."

The last sentence changed the air.

"Someone will ask?"

Tavi stared at the central ring. "If all cinder sites are linked, a clever monster will wonder whether one device could speak to the whole web at once."

Mara heard it before Tavi named it: command engine.

The cinder at her hip warmed like a held breath.

"Can one?"

Tavi's silence was answer enough.

Mara picked up one of the shifting maps. The charcoal line from Kell Ashgate to Orrowen trembled under her thumb. "Then promise me something."

"I dislike promises. They have fewer loopholes than contracts."

"Good."

Tavi looked at her then.

"If I ask you to build a thing that makes the dead obey, refuse me."

The gnome's expression lost every joke.

"Mara."

"Promise."

Tavi swallowed. "If you ask me to build a command engine, I will refuse you, insult you, sabotage myself, and recruit Kesh to steal parts from me."

"Why am I involved?" Kesh called from the bridge.

"Because you steal emotionally."

"Fair."

Mara held out her hand. Tavi gripped it, small fingers strong and grease-stained around burned skin.

One of the root-hounds lifted its head and made a low sound, almost a bell, almost a warning.

The map under Mara's thumb shifted again.

This time the Orrowen circle opened like an eye drawn by a child who had never seen mercy.
""",
    5: r"""Kavik hospitality improved after the blood tax, though improvement was a matter of local definition.

They were given a floating platform for the night, three lanterns, a stew that contained fish by rumor, and a guard who announced she would stab them only if contractually required. Rikka called this premium treatment. Kesh said premium used to include cushions. Rikka said cushions were for people whose road-names had not recently been nailed to a toll board.

The crossing moved around them until Mara could not tell whether the wagons made streets or the streets had wagon wheels. A cobbler drifted past selling boot patches. Two children poled a raft of onions through a fog bank. An old goblin tattooed debts onto strips of eel leather while arguing with a customer about whether betrayal counted as a weather event. Everywhere bells rang in little disagreements with the water.

Mara found herself liking the place before she trusted it.

That felt, increasingly, like the world's compromise.

Kesh avoided his aunt by doing useful things, which fooled no one. He checked lashings, spoke with scouts, paid three old debts with two jokes and one actual coin, and taught the refugee boy from Harrowmere how to step on floating planks without looking down. When he finally ran out of tasks, Rikka cornered him beside a lantern strung with blue shells.

Mara did not mean to listen.

The platform was small. Also, Kesh would have listened to her.

"You staked three crossings," Rikka said.

"You mentioned."

"Do you know what follows if the clans honor it?"

"Fewer drowned refugees?"

"Do not become noble at me. I am tired."

"Then ask the question under the question."

Rikka's bells clicked in her braids as she leaned close. "Are you coming back to carry the debt, or did you put your name down because martyrdom is cheaper at a distance?"

Kesh looked across the water. Without his smile ready, his face seemed made of sharper hunger.

"I sold a route once," he said.

Rikka went still.

"Not to crown men. Worse. To a flood boss who wanted to move around a quarantine. He paid enough to buy medicine for the caravan. He used the route to move sick workers out before the tally could catch him. Three villages took fever."

"We heard."

"You did not call me back."

"Your mother asked us not to."

For once, Kesh had no answer.

Rikka softened by half an inch, which in Kavik terms might have been an embrace. "You keep making loyalty into math because math can be argued down. This thing you are doing now will not argue down."

"I know."

"Do you?"

He looked toward Mara then, and she wished he had not. Not because she disliked being part of the answer, but because she could see what it cost him to let anyone know.

"No," he said. "But I am tired of surviving by becoming smaller after every bargain."

Rikka's mouth twisted. "That girl paying you?"

"Badly."

"Then why?"

"She says names like they weigh something."

The lantern between them swung, throwing blue shells of light over his face.

Rikka glanced at Mara's shadow and raised her voice. "If the eavesdropper breaks your road-name, I sell her boots separately."

Mara stepped into view. "Understood."

Kesh sighed. "Subtle as royalty, both of you."

Rikka studied Mara for a long moment. "You are not what the songs say."

"Good."

"That does not mean you are safer."

"I know."

"No, you do not. People who refuse crowns often forget knives fit in empty hands too."

Before Mara could answer, the marsh bells went silent again.

Not all. One remained ringing far out in the dark, a small silver sound moving against the current.

Kesh's face changed. "Child bell."

Every goblin on the crossing moved.

No shouting this time. No auction jokes. Ropes flew. Lanterns shuttered. Rikka shoved a pole into Mara's hands and pointed toward a skiff already sliding from the platform.

"If you mean to learn roads, learn fast."

They found the child clinging to a root snag two channels away, no older than six, too cold to cry, a little bell tied around her wrist. A reed giant's remains drifted nearby, twitching with the last memory moths. Mara held the skiff steady while Kesh crawled along the snag and cut the child free. The water tried to turn his own voice against him, whispering from below in his mother's cadence, Rikka's, Mara's, all offering bargains.

He did not answer.

He came back shaking, child wrapped against his chest.

When they returned, Rikka took the child and pressed her forehead to Kesh's for one brief, fierce second.

"One crossing paid forward," she said.

Kesh closed his eyes.

Mara looked at the marsh, where bells began to ring again, each one a little different, all of them refusing to let the dark have only one voice.

By morning, the Kavik had painted a new mark on the bridge post beside Kesh's blood: an open bowl on a road line, with no hand above it.

It was ugly.

It was perfect.
""",
    6: r"""The hymn bells reached the witness party before the wagons did.

Their music drifted up the quarry road in silver strands, each note soft enough to seem harmless alone. Together they made a net. Mara felt it settle over the ridge: breathe slower, lower your hand, trust the white road, let anger become quiet, let quiet become consent. Around her, the rebels' shoulders eased. A woman who had been gripping a spear loosened her fingers. Darron Pell stared at the supply train as if forgetting, for one dangerous breath, why his sons' names hurt.

"Tavi," Mara said.

"Already offended." The gnome twisted the crane pulley.

The Khar Veyl witness slates swung out over the road on a line of chain, wobbling badly. One slate spun, catching the train, the unarmed witnesses, the hymn bells, and the line of armed blade-bearers walking too close behind the silk-covered wounded. Ilyr murmured a word. The slate darkened, drinking light.

The witness party reached the lead wagon.

Their leader was Bessa Tarl, because no one else had been able to make the word unarmed sound so threatening. Beside her walked a Kavik scout named Vennic Reed-Quick, who had introduced himself by explaining that Reed-Quick was not a family name but an unfavorable review. The third was Lenn Voss, the Harrowmere guard who had ridden west for his family and returned by dawn with two cousins, a bandaged cheek, and a refusal to explain how many palace patrols were now chasing false heat markers.

Bessa raised both empty hands.

"Road witness requests inspection of hymn bells," she called.

The lead blade-bearer did not draw. That was something. He wore a white mask over the lower half of his face, not for secrecy, Saelith said, but to keep breath from profaning sung law. Mara had several thoughts about that and saved them for a less flammable hour.

"Inspection is denied," the blade-bearer said. "These bells soothe the injured."

"They are soothing the armed," Bessa replied.

The quarry murmured.

The bells brightened.

Mara felt the net tighten. Her burned hand lowered an inch before she caught herself. Saelith made a sound of pain beside her, not from wound, but recognition.

"Counter-hymn?" Mara asked.

Saelith's throat moved. "If I sing against them, the Pale Bough will call it proof of corruption."

"If you do not?"

"Some of your people may walk down smiling and wake in restraints."

"Then sing as yourself."

Saelith looked at her.

"Not as their law," Mara said. "As yourself."

Below, the blade-bearer stepped toward Bessa. "Return to your camp."

Lenn Voss shifted, but kept his hands open.

Darron Pell whispered, "They are going to cut her down."

"Hold," Caldus said.

"Easy for you."

"No," Caldus said. "It is not."

Saelith began to sing.

It was not loud. At first Mara could barely hear it under the bells. It had none of the chapel's polished inevitability, none of Serathiel's serene force. Saelith's song shook. It missed one note and corrected itself without hiding the flaw. It sounded like a hand asking before it touched, like a door left open, like a law being rewritten while the ink was still wet.

The hymn net frayed.

People on the quarry ridge inhaled as if surfacing from water.

Veyanna turned on Saelith. "That melody is restricted."

Saelith did not stop singing.

Mara lifted her burned hand again. This time it stayed lifted.

Below, Bessa stepped past the lead blade-bearer and put one hand on the first bell. "Inspection," she said.

The bell cracked.

Not from force. From disagreement.

Inside it was not a clapper but a coil of white root wrapped around a black chip of cinder. The chip pulsed in time with the soothing hymn.

Tavi swore so loudly half the quarry learned a new word.

The Khar Veyl slate above the road flared, recording light, sound, bell, chip, blade, witness.

"Prison silk," Saelith said, voice still threaded through song. "The bells soften refusal. The silk holds memory once softened."

The supply train erupted.

Blade-bearers moved to surround Bessa. Rebels surged on the ridge. Darron lifted his spear. Caldus slammed the butt of his staff into the mud before the first fighter could pass him.

"Hold!" he roared.

Mara did not shout.

She listened.

Under the road, the cinder chip inside the cracked bell was small and terrified, a splinter of memory forced to make comfort into a leash. She could break it. She could break all the bells. The desire swept through her with dragon heat. Then she saw the wounded under the silk covers, real wounded, frightened by the sudden violence around them. A broken bell might free the ridge and kill those who needed the only gentle sound keeping pain from swallowing them.

No clean answers.

Again. Always.

"Witnesses back," Mara said.

No one heard.

Brakka did. Brakka made the road hear.

The quarry stones boomed. The slope under the rebels lifted in shallow ridges, not enough to throw them, enough to slow the charge. Down on the White Road, old milestone law answered and opened a narrow line behind Bessa, Vennic, and Lenn.

"Witnesses back!" Mara called, and this time her voice rode the stone.

Bessa retreated one step. The blade-bearer grabbed her sleeve. Lenn Voss hit him with an open palm, not a strike to harm, a soldier's shove to make space. Vennic cut the bell strap, caught the cracked bell in his cloak, and ran.

The White Road became chaos.

But not massacre.

The distinction mattered more than songs would later admit.

Rebels threw stones, not spears, because Caldus and Darron together beat spearpoints down. Pale Bough blades cut the air before bodies. Saelith's flawed song held the hymn bells in dissonance. Tavi's crane swung the witness slates over everything, recording so enthusiastically that one slate snapped free and nearly killed Kesh, who called this typical scholarship.

Mara ran down the slope.

Not leading a charge. Chasing the cracked bell.

Vennic reached her first and thrust the cloak bundle into her hands. The bell inside was warm and crying without a mouth. The cinder chip pressed a memory into her palm: a dying dragon's scale, an elf child singing to it, a promise to preserve, centuries of hands turning preservation into obedience by fractions so small each keeper could claim innocence.

Mara held the bell out to Veyanna, who had followed in horror.

"Look at it," Mara said.

Veyanna's leaf-veiled eye filled with reflected white fire.

"This is not standard escort practice."

"That is a sentence people use when they want evil to sound like paperwork."

The light-elf flinched.

Good.

On the road, the supply captain ordered withdrawal. The train closed around its wounded and began moving north at speed, leaving one cracked bell, one cut strap, three injured rebels, two injured blade-bearers, and an entire quarry full of witnesses who had not become the ambush Serathiel could easily condemn.

Darron Pell stood in the mud below the ridge, shaking with unused violence.

"We should have taken them," he said.

"We took proof," Mara answered.

"Proof does not bury sons."

"Neither would dead healers."

He looked at her with wet eyes and an anger no victory could repair. "Half the camp will leave."

"I know."

"Some will call you coward."

"I know."

"And if Serathiel comes with more bells?"

Mara looked at the cracked cinder in her hands, at Saelith pale from singing, at Tavi's slates smoking with evidence, at Caldus holding a line he had once thought required a crown, at rebels learning that discipline could feel like defeat.

"Then we make sure more people know what bells can hide."

That night, Darron left with forty-three fighters.

He did not attack the train. That was the mercy. He did not stay either. That was the cost.

Mara watched their torches move west through rain until the last one vanished.

Caldus stood beside her.

"A commander by accident," he said.

"A bad one."

"No. A new one."

Below, in the quarry, the people who remained were fewer, colder, and less certain. They were also alive. They had a cracked hymn bell, three witness slates, and a story Serathiel would not be able to make entirely beautiful.

Mara had given her first command by refusing glory.

It felt nothing like triumph.

That was how she trusted it.
""",
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
        'current_form: "full-length draft zero with Book Two chapters 1-6 revised in pass 01"',
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
    print(f"Book Two chapters 1-6 revised. Word count: {total}")


if __name__ == "__main__":
    main()
