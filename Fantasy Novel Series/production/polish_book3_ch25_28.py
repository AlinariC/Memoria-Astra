#!/usr/bin/env python3
"""Revision pass 01m for Book Three chapters 25-28.

Replaces the remaining Dead Capital false endings and opens the Death-Dream:
Vengeance, Stillness, the first wingbeat, and the betrayal before history.
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
    25: r"""## Chapter 25: District of Vengeance

The road into Vengeance was red, but not with blood.

It was paved in verdict wax.

Each stone had been sealed by some court, council, temple, road compact, clan moot, dragon judgment, or private promise made in a locked room by people who believed justice became truer when no one outside the room could interrupt it. Red wax filled the seams between paving blocks. It had run down the gutters in old drips and hardened around the roots of dead trees. It marked doors, wells, gallows posts, empty cradles, and statues whose faces had been chiseled away. Above the street, thousands of black bells hung from wires so thin Mara saw them only when lightning moved behind them. The bells did not ring in the wind.

They rang when someone lied.

At the district gate, a bell sounded once.

Everyone stopped.

Kesh glanced at his boots. "I did not say anything."

"You thought something," Tavi said.

"That has never been chargeable before."

Another bell rang.

Tavi's mouth shut with visible effort.

The District of Vengeance opened before them in terraces of accusation. Courthouse steps led nowhere. Cells hung from chains over empty plazas. Knives had been planted in the soil like flowers, each blade bearing a name. Doors stood ajar to show rooms after judgment: a noble's table split by fire, a guildmaster's bed filled with ash, a priest's white robe nailed to a wall, a dragon scale cracked on a witness stand, a goblin route marker ground beneath an iron heel, a child's toy placed carefully beside a noose too small for an adult.

Everywhere Mara looked, someone guilty had finally been found.

The district did not hide the crimes.

That was why it was dangerous.

In Conquest, the bodies had been cropped from the banners. In Sacrifice, the knife had been covered with flowers. In Obedience, prison had worn the face of peace. Here, nothing was disguised. A magistrate who sold poor prisoners to mines burned in the public square while the families he had ruined watched and did not have to pretend pity. A light-elf prelate who ordered Orrowen's dead cleansed sang the pleas he had ignored until his holy throat tore. A dark-elf archivist who sealed famine records clawed at a locked cabinet while hungry children counted keys outside. A toll captain who sold a refugee road twice walked barefoot over the bodies of the people his lies had sent into a ravine.

Kesh stopped breathing.

Mara turned to him too late.

The toll captain lifted his head.

He had a familiar scar across one eyebrow and a gap between his teeth. Serren of Kavik. Not the real man, unless the Dead Capital had found him and dragged him here, which Mara would not put past a city made by grief. He wore the green sash of a route officer and the gold pin of a compact witness. Blood ran from his feet. Behind him came women with packs cut open, children carrying cooking pots dented by rockfall, a mule with an empty harness, and an old man whose face had been smashed beyond recognition but whose hand still clutched a goblin road ribbon.

Kesh's own route token began to smoke.

"No," he said.

The district answered by ringing every bell above the plaza.

Serren smiled at Kesh with the exhausted relief of a guilty man who had found someone guiltier. "Little ledger. I wondered when the road would count you."

Kesh moved as if to draw a knife, but his fingers closed on nothing. The district had stolen every blade from him and planted them in the ground with names written down their spines. Mara saw Rikka's name on one. Saw Rook's. Saw three route families Kesh had mentioned only while drunk enough to be honest and sorry enough to be cruel to himself.

The dead refugees turned toward him.

Kesh did not flinch. That made it worse.

"This was not only me," he said.

A bell rang.

His face went gray.

Serren laughed softly. "Not only. There is a phrase that keeps a man warm. Not only me. Not first. Not worst. Not alone."

Kesh swallowed. "I sold one route."

The bells rang again, not because the sentence was false, but because it was incomplete.

He closed his eyes. "Two."

No bell.

The plaza listened.

Kesh opened his eyes and looked at the refugees. "One to get Rikka clear of debt collectors. One because I thought the people using it had better scouts than the people hunting them. I was wrong about the scouts. I knew I might be wrong and sold it anyway."

Serren's smile sharpened. "There. See? Justice."

The knives rooted in the earth lifted.

Caldus stepped forward, broken shield raised.

The knives ignored him.

They belonged to the injured. Their points turned toward Kesh, and the plaza filled with the sound of old debts calculating interest.

Mara felt the cinders beneath the wax. Not dragon heat here. Human heat, elven heat, goblin heat, troll heat, gnome heat, all the fierce little furnaces of wronged lives refusing to cool. Vengeance had built itself from a truth the powerful had always feared: the harmed remembered. The harmed could count. The harmed did not owe gentleness to those who had profited from their ruin.

She could not condemn that.

Vorrakai's voice entered with care.

You have named witness. Will you now deny consequence?

"No," Mara said.

The knives rose higher.

Then allow the sentence to finish.

Kesh looked at her. Not pleading. That would have been easier. His eyes were black and steady and full of the horrible humility of someone who knew the charge was real.

"Mara," he said, "do not make this a rescue if it is a debt."

Saelith drew a breath that trembled. Caldus cursed under his breath. Tavi looked as if she wanted to build a machine that could punch morality in the face and was furious at lacking parts.

Brakka walked past them all.

The troll oath-sister planted herself between Kesh and the knives. Not as shield. She did not raise her maul. She laid it down.

"Name the harm," she said.

The dead refugees stared at her.

Brakka's stone-gray face was set, but Mara saw the pulse beating in her throat. Troll justice had weight, not speed. A bridge that failed had to be marked, its builder named, its stones examined, its survivors compensated before anyone spoke of forgiveness. Brakka knew better than any of them that saying stop could become another theft if spoken before the harm had room to stand.

"Name the harm," she said again. "All of it. Then name what repair can still be made. Punishment that does not build a safer bridge is only collapse repeated for an audience."

The district disliked that.

The red wax bubbled.

Serren's face twisted. "Repair? Some are dead."

"Yes," Brakka said. "Dead is not beyond witness."

Arveth's mark flared on Sava's register behind them.

Correct, it wrote. Annoyingly.

Sava read it in a voice that cracked only on the last syllable.

One of the dead refugees stepped forward. A woman with rope burns around both wrists. Her eyes were not kind. Mara was grateful for that. Kindness would have made the district look generous. This woman's fury had weather in it.

"He sold our path," she said, pointing at Kesh. "He was not first. He was not worst. He was the one who smiled while taking payment and warned no child to hide her cooking pot because metal shines under moonlight."

Kesh bowed his head.

"What is owed?" Brakka asked.

"Names," said the woman.

Kesh looked up.

"You know who bought the route," she said. "You know whose wagons waited in the ravine. You know which compact witnesses took a share. You have kept those names because names are money in your mouth."

Kesh pressed his hand to his route token. "Yes."

"Speak them."

He did.

Not quickly. Not theatrically. He spoke like a man paying in teeth. Names fell into the plaza: merchants, captains, a Harrowmere quartermaster, two Kavik elders, one Lumenorath guide who had worn pilgrim white, one Khar Veyl collector who purchased survivors as sources and wrote their grief without entering the price. With each name, a knife dropped point-first into the red wax and became a witness marker instead of a weapon.

When Kesh finished, he was shaking.

Serren spat blood. "And who names you?"

Kesh looked at the dead woman.

"He already did," she said. "He named himself in the route where it mattered. But naming is not repair."

"No," Kesh said.

"You will carry our road open."

His eyes flickered.

"Not as owner," she said. "Not as clever little keeper of debts. You will carry it open. You will teach every route child how a sale becomes a grave. You will put our ravine on every public map. You will make your shame common enough that no one can profit from its mystery."

Kesh nodded once.

The knives fell away from him.

Serren screamed.

Because Vengeance had lost the part it loved: the moment punishment became permanent employment.

The plaza tore open.

Mara barely saw the second trial before it had Ilyr by the throat.

Shadow flowed from the courthouse steps and became Khar Veyl's Hall of Sealed Records. Its dark pillars rose between the red stones. Every archive box opened at once. Inside were memories with teeth.

Vaura stood at the top stair in exile black, hair bound with silver pins, eyes bright with the old contempt Ilyr had never managed to stop loving in a poisonous way.

Behind her came others. Serathiel in torn white. A dark-elf judge who had sentenced Ilyr's mother to silence. A child from Orrowen whose name had been replaced by a number. A dragon cage engineer whose hands were small and ink-stained. Every enemy Ilyr had stored safely in the category of necessary guilt.

The black bells rang before anyone spoke.

Vaura smiled. "Little historian. Have you come to correct us or to enjoy us corrected?"

Ilyr's face went smooth.

That was his danger sign. Kesh joked. Tavi swore. Caldus built walls from his body. Ilyr became courteous enough to hide a murder in grammar.

"I came to witness," he said.

A bell rang.

Saelith winced.

Vaura extended one hand. In her palm lay a memory, small and shining as a pearl. Mara recognized it without knowing how: Vaura as a girl, no older than Mara had been in the mines, hiding under an archive table while adults argued above her about whether dark elves could survive if they told the truth faster than enemies could weaponize it. A hand reaching down. An old keeper pressing a biscuit into her fingers. The lesson not yet cruel, only frightened. Hide first. Speak later. Keep the people alive.

Ilyr stared at it.

"No," he whispered.

"Vengeance has a clean offer," Vaura said. "Destroy this. Leave only what I became. Is that not more useful? The public record will not be confused by context. Your friends will not mistake my childhood fear for innocence. The dead will have a simpler monster to condemn."

The knives in the plaza turned toward the memory in her hand.

Mara felt Saelith's fingers find hers.

Ilyr had built himself from records. He had survived exile by believing the record could hold what people lied around. But records could become knives too, if sharpened only toward the ending that made judgment easy.

"She does not deserve protection," Caldus said quietly.

Ilyr nodded.

"But the memory might," Caldus finished.

Ilyr looked at him with naked surprise.

The bells stayed silent.

Vorrakai's voice returned, threaded through knife metal and court wax.

See how mercy enters through the smallest door. Leave the door open and the guilty return wearing childhood as armor.

Ilyr closed his hand around the air as if holding an invisible blade. "Yes," he said. "They do."

Vaura's smile deepened.

"And if we destroy every door," Ilyr said, "we build a room where only vengeance can breathe."

The smile faltered.

He walked up the steps.

Mara wanted to stop him. The urge came from love and cowardice both. If he destroyed the memory, she would understand. If he spared it, she feared what it would cost him. Ilyr's hatred had kept him warm for years. To set part of it down in Vaura's presence was not forgiveness. It was walking unarmed through a corridor where every portrait knew his wounds.

He reached Vaura.

She held out the memory.

"Say it," she whispered.

Ilyr's mouth trembled.

"You were a child before you were a jailer," he said.

The memory brightened.

The black bells went mad. Not because he lied. Because Vengeance hated a sentence that refused to end where punishment wanted it to end.

Ilyr took the pearl from Vaura's palm and pressed it into Sava's register. Ink spread around it, recording the memory as evidence, not absolution.

"Public record," he said. "Protected context. Full charge remains."

Vaura's face changed.

For one impossible second, the girl under the archive table looked out through the woman's eyes. Then the district took the image back, furious.

Knives flew.

Mara moved without command. That mattered. She did not order the cinders to shield them. She spoke names: Kesh of Kavik, debtor and witness; Ilyr Noct-Vey, exile and record; Saelith Dawnmere, wrong-note singer; Caldus of the fever bridge; Tavi Quen of known harm named; Brakka of Third Arch; Sava Rennet, minutes taker under impossible conditions; Arveth, objection sustained; the dead refugees of the ravine; Vaura, guilty and once afraid.

The names did not stop the knives.

They made the knives choose.

Some struck the ground. Some shattered against Caldus's shield. One grazed Mara's cheek. One cut Ilyr's sleeve and drew blood over Vaura's childhood memory, sealing it into the record. The rest turned on Serren, the false judges, the purified enemies, and all the versions of guilt that wanted to remain simple enough to kill forever.

The district shook.

At the far plaza, a gallows collapsed into scaffolding. A judge's bench became a table. A punishment wheel broke into bridge spokes. The red wax softened and ran backward into the seams, no longer seal but mortar.

Not forgiveness.

Something more difficult.

Accountability with an end.

Vengeance opened its exit like a wound learning to close.

Kesh stood beside Ilyr, both men pale, neither looking at the other.

"For the record," Kesh said, voice rough, "I hated your door metaphor."

Ilyr wiped blood from his wrist. "It was structurally sound."

"That is not better."

Saelith laughed once, weak with relief.

Mara looked back over the district. The dead refugees were still there. The crimes remained named. The guilty were not cleansed by complexity, and the harmed were not made cruel by refusing endless punishment. Vengeance had not been defeated by softness. It had been defeated by refusing to let pain become a profession that outlived the repair it was owed.

At the exit, the dead woman from the ravine waited for Kesh.

He bowed. "I will put the ravine on every public map."

"You will start with the road children," she said.

"Yes."

"You will not make yourself hero of the confession."

His mouth twisted. "That one may take practice."

"Practice in public."

He nodded.

She stepped aside.

Beyond her lay a plain gray district with no knives, no bells, no verdict wax, and no visible walls.

The relief was immediate.

Mara distrusted it at once.

Stillness waited with both hands empty.""",
    26: r"""## Chapter 26: District of Stillness

The District of Stillness did not threaten them.

It welcomed them home.

After the red wax and knives of Vengeance, its first mercy was space. Gray fields opened beneath a pearl-white sky. Low houses stood with doors unbarred. Water moved through channels without sound. Trees grew in careful rows, not symmetrical enough to feel like Obedience, not wild enough to require attention. The air held no smoke, no rot, no iron, no ash. Mara breathed and felt her chest loosen before fear could stop it.

No one cried out.

No one begged.

No one accused.

People sat on porches in the distance, hands folded, faces calm. Dead soldiers slept in shaded courtyards with weapons laid across their knees like tools retired after honest work. A troll mason leaned against a finished bridge and watched water pass beneath it. Goblin caravans stood with wheels unbroken and animals watered. Light elves and dark elves rested under the same trees without turning toward each other, but without knives hidden in sleeves. A dragon lay along the horizon like a mountain, breathing so slowly the clouds did not notice.

"I hate it," Tavi whispered.

"Because it is a trap?" Caldus asked.

"Because part of me has already planned where to put the workshop."

Kesh rubbed both hands over his face. "I saw three unpaid debts take a nap. It was obscene."

Even Brakka did not answer. She was looking at the bridge.

It was perfect.

Not ornate. Not impossible. A practical stone bridge with a broad deck, low walls, and deep footings. Refugees crossed it without hurry. No one counted them. No one weighed them against capacity. No one asked which side deserved passage. Brakka's maul sagged in her hand.

"Brakka," Mara said gently.

"It holds," the troll said.

Mara could hear what that cost.

For Brakka, the bridge was not decoration. It was absolution from the oldest terror of her people: that love could load a span beyond its strength. Stillness offered her the dream every builder feared wanting. A world where nothing was asked to hold more than it could bear because nothing urgent ever arrived.

The road became Harth Bend.

Mara stopped so hard Saelith nearly walked into her.

The gray fields folded into soot-brown streets and low houses with red clay roofs. Rain barrels stood full. Laundry hung without ash. Edda Mar's kitchen window glowed. Oren sat on the step with a cup in both hands, no tremor, no frozen grief. Nera Bell swept the threshold, alive or dead in a way Stillness did not bother distinguishing. Children walked past with bread. The old fountain ran clear.

No one sang.

No one needed to.

The town had been spared panic, plague, occupation, piety, command, heroism, and Mara Venn. It had simply been allowed to rest.

Mara felt Saelith's hand tighten.

"I know," Saelith said before Mara could speak.

Mara looked at her.

Saelith was staring at Lumenorath.

The white trees rose beyond Harth Bend's rooftops, but their leaves were not perfectly white. Some had browned at the edges. Some had shadow running through their veins. No one cut them away. In a clearing, Pale Bough singers sat with shadow archivists, neither group trying to correct the other. Serathiel stood at the edge of the grove, not forgiven, not condemned, only quiet. Orrowen's dead sat among the roots with their names carved in living bark. Saelith's mother, or a memory of her, looked up and smiled without asking Saelith to be useful.

Saelith's breath broke.

"It knows everything," she said.

Vorrakai answered from everywhere and nowhere.

I listened.

The voice did not sound triumphant. That was the worst part. It sounded tired.

I listened to every prison call itself safety, every crown call itself order, every sacrifice call itself love, every vengeance call itself justice. I listened until even my hatred became weary. Stillness is not punishment, little witness. It is the end of the wound being reopened by morning.

The town around them deepened.

Joryn stepped out of Edda Mar's kitchen with flour on his hands.

Mara's knees almost failed.

He was older than when she had last seen him, but not worn by fear. A scar crossed his chin where the mines had once split him, but the scar was pale, old, done. He held a heel of bread and frowned at her in the exact way that had once meant she had stolen his blanket.

"Mara," he said. "You look awful."

Kesh made a strangled sound that might have been laughter or grief.

Mara could not move.

The cinders in her chest went quiet.

Not dead. Resting.

Joryn came down the steps. "Come eat."

No spell had ever been crueler.

Mara had endured command engines, dragon courts, dead witnesses, holy law, public trials, roads through storm, and the knife-flower altar of Sacrifice. All of them had asked something of her. This asked her to stop.

Behind Joryn, she saw a table crowded with people. Her mother, whom memory had blurred until the Dead Capital kindly sharpened her. Her father, still with ash in his eyebrows. Edda Mar. Oren. Nera. Pell. Children from Kell Ashgate grown safely. Dead miners with clean hands. Lio from Third Arch, not shot through by road fear. Tavi's aunt at a workbench, humming. Kesh's Rikka without debt in her shoulders. Caldus's fever bridge families, alive in a house with windows open. Ilyr's mother reading beside a lamp. Brakka's lost bridge-kin leaning over bowls of stew.

Every grief had been set down.

Every name had a chair.

Mara took one step.

Saelith did not stop her.

That made the step hers.

Joryn held out the bread. "You did enough."

Mara opened her mouth. Nothing came out.

The district spread beyond them, revealing more homes, more tables, more sleeping dead. The counter-choir's bone lanterns dimmed, not from attack but contentment. Arveth's mark on Sava's register faded to a thin gray line.

Sava pressed the page with both hands. "Arveth?"

No answer.

The absence was peaceful.

Sava began to cry in helpless, furious silence.

Caldus looked at a courtyard where his younger self sat with fever survivors and no one blamed anyone because blame had been made unnecessary by a world without next wounds. His broken shield slid from his arm.

Tavi saw Brassroot without liability panels because no mechanism had ever harmed anyone enough to need them. Her burned fingers loosened around her tools.

Kesh saw a road where debts ended at payment and no cleverness had to defend the hungry from the hungry. His route token stopped chiming.

Ilyr saw a public archive where every record was complete and no one needed to read it because no one would repeat the crime.

Brakka saw her bridge hold.

Mara saw the table.

Vorrakai spoke again, softer than rain.

You call me death because you still believe motion proves life. Look. They are not screaming. They are not being commanded. They are not being used. They are not afraid. Tell me, witness, what cruelty remains?

Mara thought of Harth Bend before the town broke the stolen quiet. The relief on faces when they did not have to remember pain. She had been angry then because the quiet had been taken without consent. But what if the choice came honestly? What if every exhausted heart, given the whole truth, chose an end to becoming?

Joryn's hand remained extended.

"Come eat," he said again.

Mara reached for the bread.

The counter-choir went out.

Darkness fell in lantern after lantern. Dead witnesses sighed and settled. Sava shouted names into the book. No marks answered. The living did not notice at first because Stillness had lowered every alarm inside them. Even fear rested here.

Saelith noticed Mara's hand.

She did not grab it.

She stepped beside her and looked at Joryn.

"Would you ask her to stay if staying ended everyone else's choosing?" Saelith asked.

The image of Joryn frowned. "Everyone is tired."

"That is not an answer."

"It is the only honest one."

Mara's hand hovered inches from the bread.

She wanted it.

Not the illusion. Not the lie. The rest. The table. The end of being sharpened against disaster until even love arrived as another task. She wanted to sit beside her brother and let someone else decide whether the world could bear its own weight.

"Part of me says yes," Mara whispered.

Stillness brightened.

Saelith nodded as she had in Sacrifice, but her face had changed. There was no altar here, no holy demand, no perfect victim. This temptation was not asking Mara to die for others. It was asking whether life itself had earned the right to continue making more grief.

Caldus spoke from behind them, voice raw. "If rest is chosen, it must be possible."

Mara turned.

He had picked up his shield again but held it low. "There are dead who want rest. Living who need sleep. Soldiers who should be allowed to stop. If we answer this by praising struggle, we lie."

Vorrakai's silence approved.

Brakka walked away from the perfect bridge. Each step looked like tearing stone from her own chest.

"A bridge has ends," she said. "People cross or they do not. I cannot build a span that carries them by refusing to let them leave the bank."

Kesh's laugh came out broken. "I am possibly about to agree with architecture."

Tavi knelt beside one of the darkened bone lanterns. Her hands shook as she opened the casing. "This did not go out. It was soothed out. Like a pressure valve closed by lullaby."

"Can you wake it?" Sava asked.

"Maybe. If it wants to wake."

That stopped everyone.

Tavi looked up, eyes wet and furious. "If it wants to wake. That is the point, yes? Rest is not the enemy. A closed system pretending consent is."

Mara looked back at Joryn.

The bread smelled like childhood hunger answered too late.

"Are you my brother?" she asked.

He smiled sadly. "I am what your grief kept."

"Would he want me alive?"

"Yes."

"Would he want everyone held still so I could stop being afraid?"

The image did not answer quickly enough.

Mara lowered her hand.

The bread became ash.

Stillness shuddered, but it did not break. Of all the false endings, it was strongest because it had learned not to be false all the way through.

Vorrakai's voice lost its gentleness by one degree.

You would preserve pain to defend choice.

"No," Mara said. "I would preserve choice even when it chooses rest. You are not offering rest. You are offering no more choosing."

The gray houses trembled.

At the table, her mother looked down. Her father closed his eyes. Edda Mar put one hand over her bowl as if protecting soup from dust. Joryn's face blurred between memory and need.

Mara's chest burned.

She raised both hands, palms outward, and did not command the cinders.

"Who here wants to sleep?" she asked.

The district recoiled.

Mara spoke louder. "Who here wants to wake?"

For a breath, nothing happened.

Then one bone lantern guttered.

Arveth's mark scratched across Sava's register in a line so faint she had to hold the page to her face.

Ask individually, it wrote. Obvious. Finally.

Sava laughed and sobbed at the same time.

Mara turned to the dead soldiers in the courtyard. "Name by name."

Caldus understood first. He began with the fever bridge dead. Saelith went to the Orrowen grove. Ilyr opened the archive and read not categories but names. Kesh knelt beside road ghosts and asked whether the path ahead was wanted or done. Brakka stood at the perfect bridge and asked each crosser which bank called them. Tavi repaired lantern housings only when the witness inside sparked toward her touch.

Some chose rest.

The manuscript of the world did not punish them for it.

An old cavalry rider laid down under a gray tree and faded with a smile of such exhausted relief that Mara almost fell. A child from Orrowen chose to wake because she had not finished hating the people who had numbered her. A troll mason chose rest after making Brakka promise to teach his footing song without improving the rude verses. Nera Bell chose to wake long enough to tell Oren that soup needed salt, then chose sleep and went out like a candle consenting to dawn. Arveth argued with the question for seven full minutes and finally chose to continue because too many bad procedures remained alive.

Stillness cracked wherever a choice was made.

Not where waking triumphed.

Where consent entered.

Mara came last to Joryn.

He stood outside Edda Mar's kitchen, ash-bread gone from his hand.

"You are not him," she said.

"No."

"You are not nothing."

"No."

That hurt more.

"What do you want?" Mara asked.

The image looked toward the table, then toward the road. "I want you to stop confusing being needed with being loved."

Mara made a sound with no dignity in it.

Saelith stepped close, but again did not take the choice away by holding her up before she asked.

"Can I keep that?" Mara asked.

The Joryn-memory smiled. "If you stop using it as a chair."

He touched her forehead.

For one heartbeat she smelled the mines, stale bread, sweat, a blanket shared in winter, and her brother muttering that whoever invented hope owed poor people interest.

Then he vanished.

The kitchen went dark.

Harth Bend dissolved. Lumenorath, Brassroot, Khar Veyl, Third Arch, all the perfected places folded into gray dust and blew across the plain. The people who had chosen rest were gone. The people who had chosen waking stood shaken but present, lanterns dim and stubborn.

Stillness split down its quiet center.

Beyond the crack was no street.

It was an eye.

The dragon-moon eye from the end of Orrowen, vast enough to be mistaken for the sky, opened beneath their feet instead of above their heads. Its pupil was black, ringed with cold fire. Through it Mara saw stars moving in blood, mountains rising before they had names, dragons descending through young weather, and people small as sparks lifting hands not yet trained into fists.

No one stepped through at once.

The gray district had left gifts behind, and each gift demanded refusal with manners.

Caldus found a small wooden practice sword lying where the fever courtyard had dissolved. He picked it up and turned it over in both hands. Someone had carved a crooked lion on the hilt, the kind a child might make for a knight who had not disappointed anyone yet. Caldus held it for so long Mara thought he might break. Then he tucked it through his belt instead of throwing it away.

"A reminder?" she asked.

"A promise that training children is different from commanding them."

Tavi had a brass screw in her palm. It had come from the workshop that never needed liability panels. The screw was perfect. No burrs, no scorch, no warped threading from a rushed repair in bad light while someone screamed for help. She looked at it with open longing, then scored it with her own knife until the slot bent.

Kesh stared. "You damaged perfect hardware."

"I introduced a record of use," she said.

"You are terrifyingly romantic."

"Tell no one."

Brakka took a pebble from the perfect bridge and pressed it into a crack in her maul head, where it did not fit. "Wrong stone," she said, satisfied.

Ilyr copied a line from the archive that had never needed reading: Complete records do not excuse citizens from attention. He underlined it twice, then added, Incomplete records do not excuse despair.

Sava kept waiting for Arveth to make some cutting remark about phrasing. When no mark came, she touched the register page with two fingers. "You chose to continue," she said.

At last the ink scratched back: I chose to remain interruptible. Different.

Sava laughed through her nose. "Of course it is."

Mara had nothing in her hand.

That seemed wrong until Saelith looked at her and said, "Maybe you are the one who leaves something."

Mara looked back at the empty Harth Bend street. The kitchen was gone. The chair was gone. Joryn's almost-voice had vanished into the place all almost-things went when a person chose to keep walking. But the ground still held the imprint of her step toward the bread.

She knelt and pressed her burned palm into the gray dust.

"I wanted rest," she said.

The dust warmed.

"I still do."

No bell rang. No knife rose. No altar opened. Stillness, even broken, had enough truth in it to accept the confession.

"If we win," Mara said, and felt how impossible the sentence was, "we build ways for people to rest before grief has to become a god to offer it."

Saelith knelt beside her and placed two fingers beside Mara's handprint.

"Together," she said.

One by one, the others left marks: Caldus's practice sword nick, Tavi's damaged screw, Kesh's route token pressed edgewise, Brakka's pebble-dust, Ilyr's inked thumb, Sava's pen point, Arveth's argumentative slash, bone lantern soot from the dead who had chosen waking. Not a monument. A poor little record on the threshold of the Death-Dream, easily scuffed, already imperfect, and therefore closer to a vow than anything the Dead Capital had offered them.

The eye below them watched.

Vorrakai waited on the far side.

Not as corpse.

Not as god.

As a grief old enough to have mistaken itself for mercy.

Mara tied the Kell Ashgate cloth around her wrist again. Her hands were shaking. No one pretended not to see.

"We go together," she said.

The eye blinked.

The world fell upward.

# Part V: The Death-Dream""",
    27: r"""## Chapter 27: Inside the First Wingbeat

Mara expected the beginning of the world to roar.

It whispered.

She fell through black fire and landed on wet stone so new it still remembered being below the earth. Steam curled from cracks around her boots. Rain struck the ground and turned to silver mist. Above her, mountains lifted their shoulders into existence, slow and terrible, as if some sleeping giant under the crust had rolled over. Rivers had not yet learned their beds. Forests stood in clusters of enormous ferns, white-barked saplings, black glass reeds, and flowers shaped like open mouths drinking stormlight. The air smelled of metal, lightning, sap, and the first rot of things brave enough to die.

For a while, Mara heard no war.

Only wings.

They crossed the young sky in hundreds. Dragons, but not the solemn ruin of Othrava's moon-locked body or the cold authority of the Court of Long Memory. These were wild and various as weather. Some were long and narrow, blue-black as river shadows, their wings combing rain into veils. Some were ember-red, horned, laughing thunder through their teeth. One pale green dragon flew low enough that the downdraft knocked Mara to one knee and left the smell of crushed mint in the air. Farther off, a storm-white dragon folded itself through a cloud and came out jeweled with hail.

No crown hung above them.

No chain lay beneath them.

They were not innocent. Mara felt that at once. Power so vast could not be innocent in the way children were innocent, if children ever were. The dragons broke trees by landing. Their games carved valleys. One snapped at another over a herd of antlered beasts and sent lightning across a hill where small figures scattered. The dragon did not notice them until after the hill burned.

It noticed then.

That mattered.

The ember-red dragon landed beside the fire, massive head lowering, eyes wide with a grief unpracticed enough to be clumsy. The small figures were not human only. Mara saw early humans with hair braided in wet cords, light elves whose skin held dawn before Lumenorath had a name, dark elves with shadow bright in their palms, gnomes carrying stone bowls, goblins lean and quick with route paint made from crushed green beetles, trolls no taller than Brakka's shoulder but already broad as doorways, and others whose descendants had been swallowed by history or marriage or war. They did not kneel to the dragon. They threw mud, stones, curses, and one very brave spear.

The spear bounced off a scale.

The dragon flinched anyway.

Mara stood frozen, watching the first shape of a lesson neither side knew how to learn.

"Where are the others?" Saelith called.

Mara turned.

Saelith stood knee-deep in silver grass ten paces away, rain shining in her hair. Caldus was beyond her with shield raised toward threats too large to block. Tavi had landed beside a steaming rock and was already taking notes with the expression of someone furious that the origin of history had poor measurement standards. Kesh hung upside down from a low branch by one boot, which did not stop him from saying, "I meant to do this."

Brakka pulled him down by the ankle.

Ilyr was not with them.

Neither was Sava.

Neither, for that matter, were half the counter-choir's lanterns.

Mara's heart kicked.

"Names," she said.

The wet stone warmed under her hands. The Death-Dream did not answer like the cinders. It was not memory stored in ash. It was memory before ash, before witness had learned script, before the dead had agreed on the privacy of death. It moved around her instead of toward her, too large to enter whole.

She felt Ilyr to the east, inside shadow cast by wings.

Sava below, though below did not mean underground here.

Arveth everywhere a bad procedure might happen.

"We find them," Caldus said.

The ember-red dragon roared.

Not at them. At the burned hill.

A small figure climbed a blackened stump and shouted back. Mara did not know the language, yet understood it as the dream translated grief instead of words.

You did not see us.

The dragon lowered its head until one golden eye filled half the hill.

I see you now.

The figure spat ash. Too late.

The dragon did not argue.

That, more than anything, made Mara ache. The first age did not begin with monsters who loved cages and mortals who loved knives. It began with scale and flesh failing to understand the size of each other's fear.

Saelith moved closer. "This is not Vorrakai's version yet."

"No," Mara said. "This is before the story hardened."

They followed the burned survivors toward a valley where rain gathered in bowls of black stone. The people walked warily, but not all looked back at the dragon with hatred. A gnome elder limped in the rear, one arm burned. When the ember-red dragon tried to lift a fallen tree from their path, the elder struck its claw with a staff and pointed to the ground. The dragon blinked, then placed the tree down gently, inch by inch, until the people could climb over it themselves.

Tavi made a small noise.

"What?" Mara asked.

"First liability correction," Tavi whispered, and wiped rain from her face too roughly.

At the valley, they found Ilyr among children.

He sat with his back against a stone, surrounded by early dark-elf children whose shadows kept detaching from their heels and chasing each other. One child had braided a strip of wet grass into Ilyr's hair. He looked mortified, which meant alive.

"I woke in a cautionary footnote," he said.

"Were you harmed?" Saelith asked.

"A child asked whether my coat was a funeral animal."

Kesh looked at the grass braid. "It improves you."

Ilyr rose with dignity that survived almost three steps before another child grabbed his sleeve and hid behind him.

The sky darkened.

A dragon descended into the valley.

Not red. Not wild with accident. This one was black-blue, its scales holding stars that had not yet been born. Its horns swept back like river ice. Its face was narrow, severe, beautiful in a way that made Mara think of a blade before anyone decided whether it would cut rope or throat.

The children went silent.

The dragon landed with impossible care.

Every claw chose stone instead of mud because mud held footprints and footprints meant small lives had passed there.

Mara knew him before the dream named him.

Vorrakai.

Young.

His grief not yet a kingdom.

He surveyed the valley, the burned people, the red dragon waiting beyond the ridge with head lowered in shame, the mortals gripping spears that could not pierce scale, the children hiding behind Ilyr's coat.

When he spoke, the rain stopped falling for the length of each word.

Harm has occurred.

No one breathed.

An early human woman stepped forward. She had gray in her hair, a baby tied against her chest, and a burn down one side of her face. "Your kind burned our hill."

The ember-red dragon rumbled in misery from beyond the ridge.

Vorrakai did not turn away from the woman. My kind did.

"Will you punish him?"

If punishment alone restored what was lost, I would begin there.

The woman stared.

Mara felt Caldus shift beside her. A young Vorrakai who distrusted simple punishment was almost unbearable after Vengeance.

The woman lifted her chin. "Then begin where?"

Vorrakai lowered his head until his eye was level with hers. Teach us to see you before fire.

The valley held that impossible sentence.

It should have saved everything.

For a season in the dream, it almost did.

Time moved strangely inside the Death-Dream. Mara blinked and watched shelters rise in the valley: not cities yet, but circles of stone and woven reed, platforms high enough that dragon tails did not sweep them, signal towers bright with colored flame, listening bowls carved by gnomes, route marks painted by goblins, bridge stones placed by trolls where young rivers kept changing their minds. Dragons learned to land beyond the third marker. Mortals learned which wing signs meant storm, grief, hunger, mating, memory-sickness, and do not approach unless you are tired of having a shape.

There were mistakes.

Many.

A young troll tried to ride the pale green dragon and invented three new kinds of broken bone. A goblin route scout stole a scale because beauty and market value had not yet been properly separated. A dragon ate an entire storehouse of fermented plums and slept for four days while the people responsible argued whether the event was theft, tribute, or comedy. Dark-elf children discovered that dragon shadows could tell stories from places no foot had gone and nearly vanished following one too far. Light elves sang to calm a storm dragon and accidentally proposed marriage on behalf of the valley.

Tavi kept stopping to stare at devices too young to be called devices. "They are using heated scale-shed as signal amplifiers."

"Is that good?" Kesh asked.

"It is reckless, brilliant, and insulting to several laws not yet written."

Brakka stood for a long time beside the first true bridge between a mortal settlement and a dragon ledge. It was not large. Stone on one side, white root on the other, scale plates embedded as flexible joints. Mortals could cross. Dragons could not. That was the point. A dragon lowered one claw to the far end and waited for a child to place a hand against the scale joint.

"Consent marker," Brakka said softly.

Mara looked at her.

The troll's eyes were wet. "The bridge is teaching size to ask."

Saelith had found the first shared song.

It was not beautiful.

An early light-elf singer stood on a rock while a dragon tried to hum below her pitch and shook leaves from half the valley. Dark elves answered with hand-beats on hollow logs because their shadow-magic heard rhythm before melody. Humans joined with work chants. Goblins added road calls so no one missed exits. Gnomes hammered tool-tempo. Trolls sang too low for Mara's ears until her bones understood.

The result lurched, cracked, collided, and then, for three breaths, held.

Saelith covered her mouth.

"The Pale Bough cut this out," she said.

Ilyr's face darkened. "Khar Veyl footnoted it as primitive noise."

"It was neither."

"No."

The dream turned.

Not abruptly. No villain entered with a banner. No crown fell from the sky. The first betrayal began as accumulation.

A winter came early. Herds moved south. Dragons, hungry from storm-mating and long flights, took too much game. Mortals stored grain in caves dragons could not enter, then refused to share when dragonlings began to starve. A fever spread through low marsh settlements, and a desperate dragon carried the sick in its claws to higher ground, saving some and terrifying all. Light-elf healers learned that dragon heat could burn fever out of blood. Dark-elf keepers learned that dragon memory could preserve the names of the dead. Gnomes learned to build around shed scales. Humans learned dragons could be lured by grief-song. Goblins learned routes dragons could not smell. Trolls learned which stones anchored chains.

Knowledge became safety.

Safety became leverage.

Leverage learned to call itself wisdom.

Mara watched young Vorrakai stand at the center of a council ring where mortals and dragons argued in stormlight.

Othrava was there.

Not moon-locked. Not a corpse in the sky. Living.

Deep-Wing, Keeper of Winter Rivers, Mother of Three Storms. She was vast and blue-white, her wings veined with river silver, her eyes warmer than the Court of Long Memory had allowed Mara to imagine. Three dragonlings tumbled around her tail, snapping at rain. One mortal child sat boldly on Othrava's foreclaw, braiding reeds between two talons while adults shouted.

Mara's throat tightened.

Othrava listened more patiently than anyone else in the ring.

A human chief demanded dragon fire for a northern enemy. A dark-elf keeper demanded access to dragon memory before winter erased testimony. A goblin roadmother demanded compensation for routes crushed by careless landings. A light-elf healer begged for heat to save fever children. A gnome forge-master wanted scale-shed under contract. A troll oathstone speaker wanted dragons to swear landing boundaries in stone. A storm-red dragon demanded grain stores opened to starving dragonlings. Othrava's smallest child gave a thin, hungry cry, and half the council looked away because need was harder to negotiate when it had a face.

Vorrakai spoke last.

No one here is wrong to fear.

The council quieted.

No one here is innocent of using fear.

It should have been enough.

It was not.

The Death-Dream shivered. Mara saw possible futures branching from that council like lightning. In one, the valley broke into war that killed dragons and mortals alike until only ash learned the songs. In another, dragons withdrew and mortals built crowns from absence. In another, mortals bowed and dragons called obedience peace. In another, councils multiplied, slow and flawed and maddening, and children grew up knowing where dragons could land because their grandparents had argued markers into law.

That last future was difficult.

The others were faster.

Vorrakai looked at Othrava.

She looked back with grief and warning.

"This is where he begins," Mara whispered.

"Begins what?" Caldus asked.

The answer came from Sava's voice, far below them and above them at once.

"Procedure."

The world folded.

Mara saw Sava standing in a ring of record stones with Arveth beside her, young and alive and furious. Not the Arveth they knew, but the first man whose name had later become the dead advocate's. Or perhaps the Death-Dream had given their Arveth an older face so the pattern could be seen. He argued with Vorrakai over words that had not yet become law.

"You cannot make consent permanent," Arveth said.

Vorrakai's wings darkened the council ring. I can make harm less likely.

"By turning today's fear into tomorrow's cage."

By preventing tomorrow's dead.

Arveth slammed both hands on a stone. "The dead will still arrive. And then they will find you used them as excuse."

Young Vorrakai flinched.

Mara wanted to look away because she knew that flinch. She had felt it in herself every time someone used a dead name to demand a living surrender.

The council returned. Othrava lowered her head toward Vorrakai.

Do not make grief efficient, she said.

The dream translated dragon speech into Mara's bones. Othrava's words carried river ice, storm milk, wing-shadow over eggs, the memory of a dragonling's first hunt, the ache of being large among small lives.

Vorrakai answered with winter stars.

I am trying to keep them alive.

Othrava's eyes softened.

Then keep asking.

The Death-Dream darkened at the edges.

Mara felt the later Vorrakai listening through the younger one. Not correcting the memory. Waiting to see whether she would misunderstand it. He wanted her to see that he had not begun with hatred. He wanted her to admit that cages could be built by people who truly feared the dead they might otherwise cause.

She would not give him the simple answer of calling that false.

"He loved them," Saelith said, voice thin.

"Yes," Mara said.

"All of them?"

Mara looked at the council: mortals shouting, dragons rumbling, children hungry, records incomplete, every people already collecting reasons to distrust the rest.

"Enough to think he could decide for them."

The first wingbeat ended with thunder.

Not war yet.

Only a dragon rising from the council ring, carrying the idea of a solution no one had consented to but everyone, in secret and exhaustion, might be persuaded to welcome if it promised their children would not burn, starve, vanish, or be forgotten.

Mara reached for Saelith.

Saelith was gone.

So were Caldus, Tavi, Kesh, Brakka, Ilyr, and the valley.

Mara stood alone on a crown of black stone while the first age bent toward betrayal around her.

Below, mortals quarried oathstone.

Above, dragons circled with chain shadows already forming beneath their wings.

At the center of it all, young Vorrakai wept where no one could see him and began designing mercy with locks.""",
    28: r"""## Chapter 28: The Betrayal Before History

The first chain was made by people who called it a bridge.

Mara watched them build it under a rain of ash-gray pollen while dragons slept on the surrounding cliffs and mortal children sang counting songs to keep fear from entering the work too early. It did not look like a weapon. That was the important thing. Its links were white root, troll oathstone, shed dragon scale, dark-elf shadowglass, light-elf living song, human iron, goblin route knots, and gnome heat-rivets that glowed blue when touched. Every people had contributed something precious. Every people had insisted on a clause. No one called it surrender. No one used the word cage.

They called it the Covenant Span.

It would allow a dragon to anchor memory safely during fever seasons. It would let mortals request fire without making every request a plea under talons. It would keep dragonlings from starving by binding grain stores into reciprocal routes. It would mark landing grounds, record injuries, preserve testimony, limit vengeance, regulate scale-shed, and prevent any one frightened group from deciding alone.

It was, on paper, beautiful.

Tavi would have wept over the engineering if Mara had been able to find her.

Mara moved through the work camp unseen, or seen only as weather. The Death-Dream had scattered the company into the memory, each companion pulled toward the part of history most likely to wound them accurately. She sensed Saelith somewhere among singers, Ilyr beneath the record stones, Kesh on the first marked roads, Brakka in the span footings, Caldus among oath-guards, Tavi in the heat-rivet forge, Sava in procedure, Arveth in objection. She could not reach them yet. The dream wanted her alone with the shape.

So she watched.

An early gnome forge-master named Pelket adjusted a rivet with tongs twice her height. Her hair stood out from her head in white sparks. "If the scale plate flexes under memory load, the whole joint sings instead of shears. Brilliant. Horrifying. I want three."

A troll oathstone speaker rumbled, "One."

"Two."

"One, and the privilege of not being sat on."

Pelket considered. "I accept under protest."

Nearby, a goblin roadmother tied route knots through the white root links. Each knot represented a way out. She had demanded them fiercely. "A bridge with no exit is a throat," she said whenever anyone complained about complexity.

Mara liked her instantly.

A light-elf singer tuned living wood around the chain with a note Saelith would have recognized as an ancestor of the Pale Bough's mercy hymn. Beside him, a dark-elf keeper set shadowglass tablets into the links so every use of the Span would leave record. Human smiths hammered iron around both, practical and sweating, arguing over whether beauty weakened metal or only made it smug.

At the cliff's edge, Othrava watched with her three young curled against her side.

Vorrakai stood beside her.

He looked older than in the council, though perhaps only decisions had aged him. The star-black scales along his jaw had dulled. His eyes stayed on the chain with an intensity Mara recognized from engineers, priests, commanders, and children trying to hold a cracked bowl together by staring hard enough.

Othrava spoke first.

This is too much weight for one agreement.

Vorrakai did not look away. It is many agreements braided.

Braids can strangle.

Only if tightened.

Othrava's tail curled protectively around her children. And frightened hands never tighten?

Below them, mortals laughed at something Pelket had dropped. The sound rose bright and ordinary.

Vorrakai closed his eyes.

I cannot bear another burned hill.

Othrava's voice softened. You are not asked to bear it alone.

That is precisely what they ask when they ask a judge.

Mara felt the answer shiver through centuries. There it was, almost small enough to forgive: the loneliness of being trusted to decide because everyone else was tired of decisions that could kill. Vorrakai had not seized judgment first. It had been handed to him, again and again, by councils grateful that someone vast could hold the final blame.

Then he had kept it.

The camp shifted.

The first test came at dawn.

Othrava volunteered.

Mara wanted to shout across time. The sound died in her mouth. The Death-Dream allowed witness, not interruption. That cruelty was almost honest.

Othrava stepped into the Covenant Span willingly, or as willingly as anyone could inside a world that had made refusal expensive. The chain rose around her foreclaw first, white root bright against blue-white scale. She touched each link with her breath. The shadowglass recorded. The goblin knots remained loose. The living song hummed. The oathstone held. The heat-rivets warmed.

Her children watched, restless and proud.

Mortals cheered.

Dragons lowered their heads in respect.

Vorrakai looked relieved.

For a while, the Span worked.

Fever seasons came, and dragon memory held names that would otherwise have vanished. Grain routes opened to dragon ledges. Landing markers spread across valleys. Mortals stopped stealing scales because shed-scale contracts made theft unnecessary and unfashionable. Dragons stopped taking herds without account because goblin route ledgers followed them into clouds with humiliating persistence. Troll bridges learned dragon-weight math. Light and dark songs braided into weather warnings. Human iron gates opened under witnessed conditions instead of panic. Gnome engines vented heat away from nests.

Children grew up with rules instead of terror.

That was why the betrayal succeeded.

It had evidence.

Mara found Brakka beneath the Span during the third winter.

The troll stood among the footings, one hand pressed to oathstone, face carved by grief. Around her, early troll masons argued with mortal chiefs and dragon delegates about load. Brakka was not part of the memory, yet the memory used her understanding like a doorway.

"It held," Brakka said.

Mara stood beside her. "For a while."

"That matters."

"Yes."

Brakka's fingers dug into stone. "A failed bridge that once held is not a lie. It is a warning about changed weight."

The Span above them groaned.

Changed weight came in the form of a murdered child.

The dream did not make Mara watch the death. She was grateful and angry. It showed aftermath: a human boy found crushed near a landing ground, his mother keening, dragon claw marks in mud, a young storm dragon wild-eyed and insisting the boy had been dead when he landed, a goblin scout swearing there had been another route mark tampered with, a dark-elf keeper demanding time to examine shadow residue, light-elf singers trying to keep grief from becoming mob, human iron-guards drawing spears because spears gave hands something to do while hearts broke.

The dead boy's name was Eron.

The storm dragon's name was Halruun.

The record mattered. Mara clung to it.

Vorrakai arrived before the council turned riot.

He listened to every account. He named the mother. He named the dragon. He named the broken route marker. He named uncertainty. The crowd hated him for that last one.

"Uncertainty buried my son," the mother said.

Halruun spread shaking wings. I did not kill him.

"Then submit to the Span," someone shouted.

Halruun recoiled.

The Covenant Span had never been designed for compulsion.

That sentence moved through the crowd as a weakness.

Vorrakai felt it.

Mara saw the moment.

His eyes flicked to the mother, then to the dragon, then to the armed guards, then to Othrava on the ridge with her children grown now and watching in fear, then to the crowd of mortals who had learned enough safety to feel betrayal as theft rather than weather. He saw futures again. Riot. Retaliation. Dragons withdrawing. Mortals chaining in secret. Children dead on both sides. Or one coerced submission now, witnessed by all, to prevent the world from reopening.

Arveth appeared beside him.

Alive, older, already limping from some argument that had become physical.

"Do not," Arveth said.

Vorrakai's voice was low. If he is innocent, the Span will show it.

"Not if the question is forced."

If he refuses, they will kill him.

"Then protect his refusal too."

Vorrakai looked at the spears.

Mara understood the terror in him. Protection with no perfect tool. A crowd too hurt for patience. A dragon too frightened for trust. A dead child between them. A world still young enough to lose everything.

Vorrakai lifted one claw.

The Covenant Span tightened.

Halruun screamed.

Every dragon in the valley rose half a wingbeat. Every mortal flinched and then, horribly, some relaxed because the danger had been contained. The shadowglass blazed with memory. The living song broke into a note Saelith would one day spend her life unlearning. The goblin route knots burned shut, all exits turning decorative in the same instant. Troll oathstone took the weight and did what stone does when forced beyond oath: it remembered the crack.

The Span showed truth.

Halruun had not killed Eron.

A human iron-guard had moved the route marker to keep children away from a grain theft and caused the boy to cross beneath a landing path. The guard had hidden the body near claw marks because guilt was easier to survive if it became someone else's shape.

For one breath, the valley had the truth.

Then everyone saw the cost of how it had been obtained.

Halruun collapsed with one wing useless. The forced memory had torn something inside him no healer knew how to mend. The mother of Eron screamed at the iron-guard, then at Vorrakai, then at the dragon she had accused, because grief had too many true targets and no order that could make them bearable.

Othrava landed between Halruun and the crowd.

Her voice shook mountains.

You used the Span as chain.

Vorrakai stared at Halruun. I saved him from execution.

You broke him to prove he should not die.

The words crossed the valley and found every future crown waiting.

Mara could not breathe.

The dream pulled her away before she saw whether Halruun lived.

She stood next in a hall under a mountain where the first crowns were made.

Not royal crowns. Not yet. These were circlets of oathstone and dragon scale, meant to distribute responsibility among mortal leaders so no crowd could demand one frightened judge do everything. Each people sent representatives. Humans sent a queen because they already liked singular nouns. Light elves sent three singers and pretended that was not a hierarchy. Dark elves sent archivists with veto knives hidden in sleeves. Goblins sent roadmothers who refused chairs unless the chairs had wheels. Gnomes sent engineers, which meant the proceedings began with a warning label. Trolls sent bridge-speakers who tested the floor before trusting the politics above it.

The crowns were supposed to bind fear into answerable office.

Mara felt Ilyr before she saw him. He stood behind a dark-elf archivist, watching the first public record decide which parts of the Halruun incident would be copied widely and which would be held in restricted context until tempers cooled.

"Restricted context," Ilyr said in disgust.

"It sounds reasonable," Mara said.

"It always does."

He did not look at her. His eyes were on the archivist, a woman with Vaura's mouth and a child's fear hidden behind adult precision.

"If they publish the forced-chain horror, dragons withdraw," he said. "If they hide it, mortals learn that records exist to preserve peace from truth. If they publish the iron-guard's guilt without the crowd's role, humans become convenient villains. If they publish everything, the valley may burn."

"What should they do?"

Ilyr's jaw tightened. "I do not know."

The honesty frightened him more than the hall.

Below, Vorrakai refused a crown.

The mortal representatives argued that he must take one. Dragons argued he must not. Othrava stood silent, which hurt worse than accusation. Arveth spoke for procedure so long that even the Death-Dream seemed tired of him. Sava, watching from a future corner with their Arveth's mark flickering in her register, whispered, "He is magnificent. Insufferable, but magnificent."

Vorrakai finally spoke.

No single head should carry judgment.

For a moment, hope entered the hall.

Then he continued.

So judgment must be placed where no single will can alter it.

Tavi appeared beside a forge trough, face smeared with soot, hands full of tools she had stolen from history. "Oh no."

Mara turned. "What?"

"That is how every engineer sounds before inventing a disaster with excellent intentions."

The crowns were not placed on heads.

They were placed into the Covenant Span.

Office became mechanism. Fear became repeatable. Every leader could claim the system required what no person wanted to own. The Span, damaged by Halruun's forced testimony, learned compulsion as precedent. The shadowglass accepted sealed context. The living song accepted corrected intervals. The route knots accepted emergency closure. Oathstone accepted impossible weight because everyone promised the impossibility was temporary.

Temporary became a country.

Mara saw centuries in fragments.

A dragon restrained to preserve a city from flood fire, then kept because release risked retaliation. A human king crowned not to command but to coordinate, then obeyed because coordination had armies now. Light-elf mercy codified into beauty and then into erasure. Dark-elf records sealed until truth became property. Goblin routes licensed until roads remembered toll more clearly than direction. Gnome engines built to reduce harm and then improved past conscience. Troll bridges assigned weights by worthiness instead of stone. Undead testimony feared, used, sanctified, silenced, summoned, dismissed. Every people taking the tool that once saved them and turning it, under pressure, toward someone smaller.

No faction owned innocence.

No faction owned guilt.

That did not make guilt vanish.

It made witness harder.

Mara staggered through the fragments until she found Saelith in the first chapel of the corrected song.

There were no white trees yet. Only a living wood hall, mortals and dragons gathered under branches, singers attempting to repair the broken note left by Halruun's forced chain. Saelith stood among them, horrified, as the correction turned grief into harmony too soon.

"They are trying to keep everyone from panicking," she said.

"Yes."

"It is beautiful."

"Yes."

Saelith closed her eyes. "And it is wrong."

The singers found a note that made dragons lower their heads and mortals stop shouting. It did not erase memory. Not at first. It softened the sharpest edges so councils could continue. Then someone used it after a riot. Then before a riot. Then when a child asked a question during mourning. Then when Orrowen refused to be quiet centuries later. The song became mercy by repetition and weapon by convenience.

Saelith sang one ugly wrong note into the chapel.

The memory shook.

Not enough to change history. Enough to mark that someone had heard the earlier fork.

Kesh was on the first closed road.

He stood beside the goblin roadmother Mara had liked, watching her discover that her exit knots could be ordered shut by emergency crown protocol. A caravan waited behind her. Ahead, dragon fire blocked the open route. Behind, human soldiers demanded priority passage for grain. The roadmother held three bad choices in both hands and one worse choice in her mouth.

"You make the bargain," Kesh said softly.

She looked at him as if she knew he was a future debt with legs. "I sell one road to keep two alive."

"You will regret the one."

"If I do not, I am already dead."

Kesh bowed his head. "Put the name on the map."

She stared.

"The one you sell," he said. "Put it on the map. Do not let cleverness hide the grave."

Again, history did not change.

But the Death-Dream recorded the advice as witness, and somewhere far ahead in time, a dead woman from a ravine might have smiled.

Caldus stood with the first oath-guards when they received the doctrine of emergency obedience.

He watched good people accept commands because delay had bodies attached. He watched one guard refuse an order and save a dragon child, then get exiled for risking a village. He watched another obey and save the village while the dragon child died. The doctrine recorded one as dangerous, the other as tragic. Caldus broke the stone tablet with the flat of his shield.

"Both records," he said. "Or neither teaches."

Brakka drove a wedge into a Span footing where oathstone had hidden its first crack.

Tavi carved known harm named into the underside of a heat-rivet before history could polish it.

Ilyr stole a restricted record and left it in a public wall.

Saelith left her wrong note humming in the first chapel.

Kesh tied a road knot that could not be ordered fully shut.

Sava entered objections until Arveth's living predecessor told her she had admirable nuisance potential.

None of it saved the first age.

All of it changed what the Death-Dream could claim had gone unwitnessed.

Mara came last to Vorrakai.

He stood alone in the ruins of the council valley after the first true dragon-mortal war. The Covenant Span lay broken across the river, half bridge, half chain, all wound. Othrava's three children were gone. One dead, one fled beyond storm, one captured by mortals who believed hostage was another word for peace. Othrava herself circled above, wounded, river-silver blood falling as rain. Mortals burned dead dragons for heat. Dragons carried mortal dead into high places because they still did not know what burial meant and were trying, terribly late, to honor enemies.

Vorrakai looked at the world and saw only pattern.

Choice had made promises.

Fear had bent them.

Pain had armed memory.

Love had taken sides.

Crowns had moved blame from hands into systems.

Systems had taught hands to stop feeling.

He turned toward Mara.

Not the young Vorrakai now. Not fully the dead god either. Both overlaid: first judge, failed guardian, dragon corpse, moon-shadow, mercy sharpened into prison.

You see, he said.

Mara's face was wet. She did not know whether from rain, grief, or Othrava's blood.

"I see that you were hurt."

The air tightened.

You see that I was right.

"No."

The word seemed too small for the first age. She said it anyway.

Vorrakai's eyes burned cold. Tell me which part is false.

Mara looked at the broken Span. "None of the grief is false."

Then-

"Your ending is."

The valley shook.

He spread wings large enough to roof a city. Choice made cages.

"People made cages. Dragons too."

Choice made betrayal.

"Fear did. Love did. Hunger did. You did."

Choice made crowns.

Mara looked down at her burned hands, at the Kell Ashgate cloth, at the ash under her nails from battles centuries after this one. "Crowns were made to bind fear into obedience. Some people wore them. Some built them into systems. Some hid them in songs. Some called them roads, records, bridges, engines, mercy, law. You are right about that."

Vorrakai went still.

Because she had not denied enough.

Mara stepped closer.

"But the answer to a crown is not one final crown so large no one can see it on your head."

His grief struck her like winter surf.

She saw every person he had failed to save. Every dragon broken by mortal panic. Every mortal burned by dragon carelessness. Every child turned into proof. Every council where the slow answer died under a fast fear. The weight should have crushed her.

It would have, if she had tried to hold it alone.

Hands found her.

Saelith first, warm and shaking. Caldus, a shield at her back but not over her mouth. Tavi with soot-smeared fingers. Kesh smelling of rain and road dust. Ilyr with ink on his sleeve. Brakka like a foundation choosing not to imprison. Sava with the register open. Arveth's mark burning in the page. Lanterns of the counter-choir, some dim, some bright, every one chosen.

The company had reassembled inside the memory because each had left a witness where history had tried to close.

Vorrakai looked at them with something like pity.

You will fail.

"Yes," Mara said.

Some of your repairs will become weapons.

"Yes."

Some choices will kill the innocent.

Mara's voice almost broke. "Yes."

Then why defend it?

She thought of Joryn's memory telling her to stop confusing being needed with being loved. Of Kesh naming the ravine. Of Ilyr preserving Vaura's childhood without clearing her charge. Of Brakka walking from the perfect bridge. Of Saelith's wrong note. Of Caldus saying accountability after conquest went to die. Of Tavi insisting on known harm named. Of Sava reading Arveth's rude little truths aloud because procedure, at its best, gave grief a place to stand without becoming a weapon.

"Because pain proves life mattered," Mara said. "Not that life should stop."

The Death-Dream cracked.

Vorrakai roared, and the roar became a battlefield made of memory.

From the broken Span rose figures in armor of old choices: champions of the Choir, each wearing a false ending like a banner. Conquest with clean crest. Sacrifice with white flowers. Obedience with perfect bells. Vengeance with red knives. Stillness with empty hands. Behind them moved other shapes not yet named: a dead child, a chained dragon, a crowned machine, a road closed for safety, a song corrected into silence.

The first age fell away.

Mara stood with her company on a dark plain beneath the dragon-moon eye.

Vorrakai's voice filled the sky.

Answer, then. Not with refusal. With victory.

Kesh drew a knife that had not been returned to him by Vengeance and smiled without humor. "I miss when villains monologued in rooms with exits."

Tavi lifted a stolen first-age tool. "I have historical crimes in my pocket."

Saelith sang one ugly note, and the champions turned.

Ilyr opened the record in his bleeding hand.

Caldus raised the broken shield.

Brakka took the center without asking permission.

Mara felt the cinders of Vael Taryn beneath the dream, not waiting for command, but listening for the kind of witness that could survive battle.

She did not feel ready.

That, at least, was honest.

The champions charged.""",
}


WORD_FLOOR_DEEPENING: dict[int, str] = {
    25: r"""At the boundary between Vengeance and Stillness, no one crossed for a long time.

The red district did not pursue them. That restraint felt more frightening than another attack. Behind them, bells hung silent over half-ruined courts. Witness markers stood where knives had been. The dead refugees had gone to whatever road their own answers had chosen, but their absence was not light. It had weight, like a pack set down beside the fire that still belonged to someone and could not be moved without permission.

Kesh sat on a verdict stone and retied his route token with fingers that kept missing the knot.

Mara sat beside him because she did not know what else to do.

"If you tell me I did well, I will charge you double for the insult," he said.

"I was going to ask whether you wanted water."

"Devious. Harder to reject."

She handed him the skin.

He drank, wiped his mouth, and looked back at the district. "I used to think public shame was what happened when private cleverness failed."

"And now?"

"Now I suspect private cleverness is what shame does before it becomes expensive enough to notice."

Mara let that sit. Some sentences needed room to decide whether they were wisdom or self-harm.

Ilyr stood several paces away with Sava's register open before him. The pearl-memory of Vaura's childhood glimmered in the page like a trapped star. He had not moved since the district broke. Saelith watched him without approaching, which was a kind of love Mara was still learning: the discipline not to make comfort another demand.

At last Ilyr spoke.

"I need a category."

Sava, who had been pressing grit from the register's hinge, looked up. "For the memory?"

"For evidence that must neither reduce charge nor permit simplification."

Arveth's mark appeared faintly. Difficult evidence.

Ilyr stared at the page. "That is not a category. That is a mood."

Then invent one, the mark wrote.

Ilyr's mouth twitched despite himself. "Posthumous legal advice remains irritating."

He wrote: Context preserved. Charge unsoftened. Sentence subject to living review.

The words looked small against the horror of Vaura's life and crimes. They also looked necessary. Mara thought of all the ways people had tried to make her simple: saint, spark, threat, weapon, crown, cure. Simplicity was often the first kindness power offered before asking to own the rest of the room.

Brakka carried broken spokes from the punishment wheel and laid them in a pile. "Bridge material," she said when Tavi stared.

"That was a vengeance wheel."

"Now it can learn load distribution."

Tavi considered. "I hate that this is technically elegant."

Caldus bound Kesh's cut hands, then Ilyr's, then Mara's cheek, moving from person to person with the quiet usefulness of a man trying not to become command again. When he finished, the fever mother from Conquest appeared at the edge of the red street. She did not speak. She handed him a strip of blue banner cloth with names burned on the back and vanished before he could bow.

Caldus folded it into his shield straps.

"Not decoration," Mara said.

"No," he answered. "Weight."

The company made a poor meal there because hunger had survived moral architecture. Stale bread, hard cheese, dried mushrooms that Kesh insisted were legally distinct from poison, and one small pot of tea Saelith brewed from leaves given by a dead clerk in Obedience. The tea tasted like dust and mint and municipal complaint. Everyone drank it anyway.

For a few minutes, they were not symbols standing between world and death. They were tired travelers at the border of a quieter danger, eating badly, arguing over bandage tightness, and trying not to look relieved whenever someone they loved was still breathing.

Mara watched the gray district ahead.

No bells rang there.

No knives turned.

No court demanded confession.

After Vengeance, that mercy felt like a hand covering a mouth.

"It will offer what punishment cannot," Saelith said beside her.

"What?"

"Permission to stop being answerable."

Mara thought of Joryn. Of Ashgate. Of the dead who had chosen to continue because a name still needed saying, and the dead who would have chosen rest if anyone had asked instead of used them. She tied the Kell cloth tighter until the knot pressed into her pulse.

"Then we ask better questions," she said.

The gray road waited.

It did not need to hurry. Tired hearts walked toward it on their own.""",
    27: r"""Mara found one more memory before the first age bent toward chain.

It came folded inside a child's game.

The valley children had painted circles on flat stones and were teaching three dragonlings to place claws with care. The game was impossible, which appeared to be its attraction. A dragonling's smallest talon covered four circles at once. Human children shouted corrections. Goblin children cheated with admirable openness. A young dark-elf girl kept score in shadow marks that rearranged themselves whenever no one watched. A light-elf boy sang each rule as if making it musical would make it obeyed. A troll child sat on the largest stone so no one could move it without negotiation.

Othrava watched from nearby, pretending not to be invested.

One of her dragonlings lost.

It made a sound like a collapsing chimney and flopped onto its side in despair.

The mortal children cheered with the savagery of all children who have discovered fairness includes the mighty losing in public.

Othrava lowered her head until her breath stirred their hair. Is this justice?

The goblin child with paint on her teeth answered, "This is rules."

The troll child added, "Justice is when you do not eat the board after."

The dragonling, who had plainly considered eating the board, looked offended.

Othrava's laugh rolled through the valley and shook rain from the leaves. It was the first time Mara had heard a dragon laugh without thunder inside it. The sound had river bends, egg warmth, and old snow cracking under spring. It made several children fall down. They got up delighted.

Vorrakai stood at the edge of the clearing, watching.

For once, his face held no calculation.

Mara realized that if history had stopped there, every later argument would have been simpler and less true. It would be easy to say fear destroyed the first covenant. But joy had helped build it. Shared jokes. Games no body was shaped to play perfectly. The strange delight of telling something vast, no, you must wait your turn, and seeing it wait because it wanted to belong more than it wanted to win.

Saelith came to Mara's side, drawn by the laugh.

"We lost this," she said.

"Yes."

"Not only law. Not only truth. This."

The dragonling nudged the board and looked around with exaggerated innocence. Every child shouted. Othrava covered her eyes with one wing in theatrical shame.

Ilyr, still wearing a grass braid, said, "For the record, dragons have always been poor losers."

A small dragonling sneezed sparks at him.

Tavi stepped between them with scholarly urgency. "Do that again."

"Do not encourage infant weather," Caldus said.

The laughter faded when the Death-Dream moved, but it left a mark in Mara sharper than any wound. Vorrakai's later mercy had not only tried to end pain. It had tried, perhaps without admitting it, to preserve a world where dragonlings could lose games to children and not be feared for the size of their disappointment.

That made him harder to hate.

It also made him more dangerous.

Because a person who remembers joy can convince himself that imprisoning the world is an act of preservation, not conquest.

Othrava seemed to hear Mara's thought. She looked across the clearing with eyes like winter rivers under stars.

Little witness, she said, though her mouth did not move. If grief shows you what it loved, do not let love excuse what grief becomes.

Mara bowed her head.

The dragon lowered hers in return.

Then the valley slid away, children and game stones and laughing dragonlings dissolving into rain. The sound of Othrava's laughter stretched thinner and thinner until it became the first strained note of the corrected song.""",
    28: r"""After the champions appeared, Vorrakai did not send them forward immediately.

He made the company look at them.

That was the old judge in him, still demanding the record before sentence. The five false endings stood across the dark plain, each one shaped from the memories they had just survived. Conquest wore Caldus's restored crest on armor polished bright enough to hide the faces reflected in it. Sacrifice carried Mara's dead body in white flowers and smiled with Joryn's stolen mouth. Obedience rang bells from Saelith's throat and Ilyr's pen. Vengeance held Kesh's route token in one hand and Vaura's childhood pearl in the other, daring him to choose which truth deserved a knife. Stillness came unarmed, gray-robed, with bone lanterns sleeping at its feet.

Behind those five moved the older failures of the first age.

The Chain That Had Been Called Bridge dragged broken links of root, scale, stone, song, iron, route knot, and heat-rivet across the plain. The Crown Without Head rolled like a wheel, every circlet embedded into mechanism, every mechanism insisting no person had chosen what it did. The Closed Road wore goblin knots burned shut. The Corrected Song had no face, only a mouth full of beautiful notes. The Sealed Record carried cabinets on its back, each drawer labeled TEMPORARY. The Perfect Engine clicked with Tavi's own fear: a device so accountable on paper no one could find the hand that turned it.

Mara's company saw their private futures in the enemy line.

Caldus saw himself winning the coming battle by taking command so completely no one else had time to become guilty. His fingers tightened on the shield.

Saelith saw herself singing the company steady until steady became silence.

Ilyr saw a record of the fight already written, all context preserved and no one alive enough to read it.

Kesh saw roads opened by debts so public they became another form of ownership.

Tavi saw harm named, measured, diagrammed, compensated, and repeated because the compensation mechanism worked better every time.

Brakka saw bridges that never fell because no one heavy with grief was allowed onto them.

Sava saw minutes so complete they replaced action.

Arveth wrote, Uncalled for.

Vorrakai's voice moved over them.

These are not my inventions. They are your best answers continuing past their rightful end.

No one contradicted him.

Mara hated that most.

She had wanted, somewhere under all the better lessons, to reach the final enemy and find a lie large enough to stab cleanly. Instead Vorrakai had arrayed truths spoiled by fear. Every champion was an answer the world had needed once. Command in crisis. Sacrifice freely chosen. Order after chaos. Consequence after hidden harm. Rest after unbearable labor. None began as evil. Each became monstrous by refusing to stop.

Saelith touched Mara's wrist.

"Then our answer cannot be purity," she said.

"No."

"Or refusal only."

Mara looked at the charging line held in suspension. "No."

Kesh exhaled. "I dislike battles where the enemy has a philosophical warranty."

Tavi lifted the first-age tool in her hand. It was half wrench, half tuning fork, and fully illegal in at least three future guilds. "Everything breaks under wrong use."

Brakka nodded. "Then we name rightful load."

Caldus rolled his shoulder, winced, and set his feet. "And pass command before it becomes conquest."

Ilyr opened the bleeding record. "And publish context before it becomes concealment."

Saelith hummed one note, let it crack, and did not correct it. "And let song end."

Kesh spun his knife once. "And mark roads without owning every traveler."

Sava raised her pen. "And take minutes that do not mistake themselves for the meeting."

Arveth's mark flashed: Finally.

Mara looked at Stillness, the gentlest champion, and thought of those who had chosen rest in the gray district. "And let endings be chosen one by one."

The dragon-moon eye narrowed overhead.

For the first time since they had entered the Death-Dream, Vorrakai seemed uncertain.

Not afraid.

Only presented with an answer too procedural, too relational, too stubbornly unfinished to fit inside his clean mercy.

Mara almost smiled.

"You wanted victory," she called to him. "Fine. But we are not giving you one hero. You get a terrible committee."

Kesh groaned. "That sounded stronger in your head."

"It did."

Tavi grinned despite the battlefield. "I liked it."

The champions moved.

The suspended moment broke into sound: bells, hooves, wings, chain shriek, choir note, road chime, shield impact, dragon roar, and underneath it all the living beat of people who had not solved the world and were going to fight for it anyway.""",
    128: r"""The first clash did not yet belong to Chapter Twenty-Nine, but it gave that chapter its debt.

Conquest reached them first because command is always quickest when fear opens the gate. Caldus met the clean crest with his broken shield and, before the impact could turn him into the center of the field, shouted, "Brakka, take weight. Kesh, left road. Saelith, call retreat if I forget to hear it."

The orders worked because he gave them away as soon as they landed.

Brakka took weight, not glory. Kesh cut left, then cut farther left because routes resented prediction. Saelith held one cracked note ready, not to steady everyone forever, but to break the moment when steadiness became obedience. Tavi struck the Chain That Had Been Called Bridge with her first-age tool and shouted, "Known stress point!" The chain screamed like a law discovering inspection.

Vengeance came for Ilyr.

It wore Vaura's face, Serren's smile, Serathiel's white hands, and a hundred other guilty mouths. In one palm it held the pearl-memory. In the other it held a knife red with every name that had not received repair.

"Choose," it said.

Ilyr did not choose quickly.

That was how Mara knew he had learned.

He opened Sava's register and placed the pearl on one page, the charge on the facing page. "Both entered. Neither cancels."

The knife struck the binding. Arveth's mark flared up through the cut, incandescent with offended procedure, and the blade stopped one finger-width from Ilyr's wrist.

Stillness walked toward Mara while the others fought.

No rush. No weapon. No argument.

It carried a chair from Edda Mar's kitchen.

Mara hated that chair. She loved it so fiercely she hated herself for hating it. One leg had always been shorter than the others. Joryn used to wedge folded paper under it and declare the table politically unstable. The champion placed it on the battlefield between dragon roar and chain shriek.

"Sit," Stillness said with Joryn's almost-voice.

Mara's knees weakened.

Saelith could not reach her. Caldus was under the crest. Tavi was inside chain links. Kesh had vanished into a road that kept closing. Brakka held a weight no bridge should hold. Ilyr bled over the record. Everyone needed her.

And Stillness offered the one thing no one ever offered without cost: a chair.

Mara put one hand on its back.

The battlefield dimmed.

Then Sava, of all people, threw a pen at her.

It hit Mara on the ear.

"Ow."

"Minutes require standing witness," Sava shouted, terrified and furious and very alive.

Arveth wrote something on the air too rude to preserve.

Mara laughed.

The chair cracked.

Not because rest was wrong. Because this rest had arrived as an order shaped like tenderness. Mara pushed it aside gently, almost apologetically, and promised herself that if the world survived, she would sit in a real chair badly, with soup, without becoming useful to anyone for at least ten minutes.

Stillness stepped back.

It did not look defeated.

It looked patient.

That patience was the warning the next battle carried forward: false endings did not need to win once. They only needed to remain available each time exhaustion made them look like wisdom.""",
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
        if chapter_no == 28 and 128 in WORD_FLOOR_DEEPENING:
            replacement += "\n\n" + WORD_FLOOR_DEEPENING[128].strip()
        text = text[:start] + replacement + "\n\n" + text[end:].lstrip()
        matches = list(pattern.finditer(text))
        by_no = {int(m.group(1)): m for m in matches}
        back_matter = re.search(r"(?m)^## Back Matter\b", text)
    return text


def normalize_part_headings(text: str) -> str:
    text = re.sub(r"\n# Part V: The Death-Dream\n+", "\n", text)
    chapter_27 = "## Chapter 27: Inside the First Wingbeat"
    return text.replace(chapter_27, f"# Part V: The Death-Dream\n\n{chapter_27}", 1)


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
        'current_form: "full-length draft zero with Book Three chapters 1-28 revised in pass 01"',
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
    print(f"Book Three chapters 25-28 revised. Word count: {total}")


if __name__ == "__main__":
    main()
