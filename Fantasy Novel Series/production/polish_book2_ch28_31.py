#!/usr/bin/env python3
"""Revision pass 01h for Book Two chapters 28-31.

Replaces the remaining Part V scaffold with the completed dragon-moon climax:
Tavi refusing the command engine, Orrowen's dead entering witness standing,
Serathiel's fall, and the Book Three hook.
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
    28: r"""## Chapter 28: Tavi Refuses the Command Engine

Tavi had always trusted machines more than people, not because machines were kinder, but because they could be forced to confess what they were built to do.

People hid intention behind manners, doctrine, titles, grief, love, and occasionally very good cheekbones. Machines hid intention behind casing, calibration, and cowardly labels like regulator or harmonizer, but if one found the correct screw, the lie came apart in the hand. Tavi had made a life from opening useful things and asking who had been made less human so the usefulness could remain clean.

The command engine wanted her to admire it.

That was its first mistake.

It rose from the side of the dragon-moon platform in rings of brass, cinder-glass, and old gnome mathematics, unfolding around her like a flower designed by a committee of murderers with excellent drafting tools. Each ring held a path of control. The lowest was inscribed with civic rolls: Orrowen dead names routed into obedience channels. The second carried military seals from Lumenorath and Khar Veyl. The third bore gnome load equations, human ash tallies, goblin road marks, troll bridge knots, and dragon-scale witness script, all translated into a central spindle aimed at the closed eye below.

It was, technically speaking, magnificent.

"I despise this thing with professional intimacy," Tavi said.

Kesh, still half-linked to the goblin road bridge above, shouted down, "Is that different from ordinary hatred?"

"It has footnotes."

"Terrifying."

The engine screamed again. Its brass gears did not grind; they sang in high avian shrieks, like a flock of metal birds trying to flee its own rib cage. The cinder-glass spindle turned toward the gathered dead of Orrowen. Around the platform, thousands of names streamed through the record storm Ilyr had opened. The command engine licked at those names with lines of red light, tasting how easily a person could become a function if the room became frightened enough.

Tavi wedged her bent wrench deeper between two teeth of the second ring.

The wrench snapped.

"Rude," she said.

Master Quen's voice came through the speaking tubes and the brass itself. Apprentice Tavira. Tools are not guilty for answering need.

Tavi closed her eyes.

The voice did not belong wholly to the living Quen, nor wholly to a ghost. It was an imprint, an engine memory, perhaps the part of Quen that had loved Tavi badly and built systems worse. That made it more dangerous. A monster could be dismissed. A teacher who had once put a coat over a sleeping apprentice under a workbench could still get a hand around the heart.

"You are not my master anymore," Tavi said.

No, Quen answered. I am your precedent.

The engine showed her a solution.

Not a theory. A working model. The spindle would pierce the witness stream, route Orrowen's dead into bridge-law channels, and freeze both armies before Serathiel could cleanse or Vaura could seal. The Choir's song would be locked into harmless hum. Vorrakai's pressure would be delayed. The dead would stand as perfect witnesses, never contradicting, never panicking, never choosing the wrong moment to refuse. No one on the platform would need to die in the next breath.

The vision was so useful it almost glowed.

Tavi saw Mara feel it.

That was the second mistake.

The engine had shown Tavi the outcome, but not the cost in a way an engineer would respect. So Tavi looked for the hidden load. She traced the red paths through the dead civic rolls, through Ruv Ossian and Leth of West Quay, through Nim of south laundries, through Sava's ink-stained hands, through Edrin's patient anger, through Arveth's dispersed voice. The command engine did not kill them. It did something tidier. It kept them present and removed the part that could say no.

"There," Tavi said. "There is the corpse under the clean floor."

The gnome engine-ghosts on the bridge bowed their heads.

One whispered, "Consent bypass."

"Say it louder," Tavi snapped.

The ghost looked up, ashamed even after death. "Consent bypass."

The chamber turned blue.

True.

The engine shrieked hard enough to make the platform chains tremble.

Caldus dragged himself up the slope of the dais, one arm still bound, sword in his good hand. "Can you break it without breaking the chamber?"

"Do you want the comforting answer or the answer that helps?"

"The second."

"No idea."

"Good. I can plan around that."

"How?"

"Badly, but honestly."

Tavi almost smiled. Then the third ring opened.

The command spindle swung toward Mara's cinder cage.

Mara flinched. Saelith caught her wrist. Brakka's maul rang once as bridge law tightened. The human bridge under Mara's feet lit with Ashgate tally marks, and the cinder in her cage answered like a coal offered a furnace mouth.

The engine had found the cleanest path.

Mara was a living witness-node, threaded through cinder memory, connected to Orrowen, Ashgate, Lumenorath, Khar Veyl, the dragon-moon, and the name of Vorrakai spoken kindly in canals. If the engine fed through her, it could command without shredding the record. It could use the person everyone had been trying to use since Book Two began and make the old temptation look mathematical.

Tavi moved before anyone told her to.

She threw herself across the spindle path.

Red light struck her chest.

The world went brass-white.

Mara screamed her name, but the engine took the sound and tried to file it under error. Tavi's boots left the gear rim. For a breath she hung in the command path, small body arched against a machine built by centuries, the root-hound collar burning around her wrist. The collar's cracked brass snapped open. A projection burst from it, not the hound itself, not even a ghost, but the memory of every impossible choice Tavi had taught that little machine to make: follow, disobey, warn, bite, stay, choose the road.

The projection bit the command spindle.

The spindle screamed.

Tavi dropped onto the ring, coughing smoke.

"You," she told the engine, "do not get her."

Quen's voice sharpened. Then you will take the load.

"No."

The answer surprised the engine.

It surprised Tavi too, perhaps. Mara saw it in the jerk of her head, the flash of old training meeting new refusal. Tavi had expected the shape of sacrifice. She had climbed ready to pay with her body because that was the story the world kept handing useful people: be good enough to be spent. But the command engine did not deserve her any more than it deserved Mara.

"No," Tavi said again, stronger. "I am not replacing one living node with another. I am not making my grief into your battery. I am not becoming the acceptable failure rate."

The gnome ghosts lifted their measuring rods.

Tavi pointed at them. "And none of you are either."

One of the ghosts blinked. "We are already dead."

"Then stop volunteering twice."

The ghost stared.

Kesh shouted from above, "I am emotional and I hate it!"

The engine opened its fourth ring.

This ring had no script. It held memories of outcomes: battles stopped, cities saved, refugees routed safely, dead witnesses preserved, children spared. Every possible good the engine could produce unfolded in a glittering circle. Tavi saw herself running a corrected version. Less cruel. Consent checks added. Manual override under mixed witness. Kill switches. Public ledgers. She could improve it. Of course she could. That was the final and most poisonous offer.

Master Quen's voice softened. Make it better.

Tavi stood very still.

Mara could not reach her. No one could. The ring had lifted Tavi above the platform on a rib of brass and glass. Sparks gathered around her hair. The record storm roared below. The dragon-moon eye twitched under its lid. Serathiel watched from the Lumenorath bridge with hunger disguised as grief. Vaura watched with calculation cracking under fear. The Choir watched as if all roads, command and surrender alike, ended in their song.

"It would be better," Tavi said.

Mara's stomach dropped.

"If I made it, it would be better. Fewer deaths. Slower harm. More warnings. Better labels, certainly. A user interface that does not look like a cathedral tried to swallow a clock."

"Tavi," Mara said.

"I'm not done."

Mara shut her mouth.

Tavi looked down at the engine. "But better slavery is still slavery. Better silencing is still silence. Better command is still command."

She pulled a small tool from her boot.

It was not impressive. A narrow brass pick, bent at the tip, the kind she used for locks, fine gears, and problems that did not yet know they were about to lose an argument. She had made it years ago from a discarded guild pin. Mara knew because Tavi had once described the theft with the tenderness other people reserved for childhood pets.

Tavi pressed the pick into the fourth ring's unmarked seam.

The engine stopped screaming.

Everything stopped.

The pick turned.

Click.

The unmarked ring opened, revealing the true core of the command engine.

It was not a gear.

It was a cradle.

Inside lay a fragment of dragon cinder shaped like an egg, wrapped in white root, black seal thread, gnome wire, and human ash cloth. It pulsed faintly, trying to become a heart because every machine around it had been built to make it answer like one.

Tavi's anger vanished.

In its place came reverence so fierce it looked like sorrow.

"Oh," she said. "You poor thing."

The command engine shuddered.

Quen's voice broke. Necessary.

"No," Tavi said. "Lonely."

She reached into the cradle.

Every tool in her pack screamed. The brass pick melted. Her gloves smoked. The gnome ghosts cried out. Caldus lunged and could not reach. Mara felt the heat through her own cinder cage, a sympathetic agony that filled her mouth with ash.

Tavi did not pull the cinder free.

She did something harder.

She opened the cradle.

The white root withdrew first, curling away from the cinder like fingers releasing a throat. The black seal thread snapped. The gnome wire uncoiled. The human ash cloth burned without smoke. The cinder fragment lifted from the cradle and hovered, no longer pointed at the dead, the armies, Mara, or the dragon-moon. It spun once in the air, confused by freedom.

Tavi put both bloody hands around it without touching.

"No command," she said.

The chamber took the phrase.

The gnome bridge repeated it. Then the human bridge. Then the goblin road marks and troll bridge knots and Orrowen civic rolls. Saelith said it. Caldus said it. Kesh said it from the causeway above and made it sound like a stolen password. Maelin said it through tears. Ilyr said it with what breath he had. Brakka said it, and bridge law turned it to stone.

No command.

The core cracked.

Not shattered. Cracked open like an egg.

Memory spilled from it: a dragon hatchling's first sight of sky, a gnome child laughing at sparks, an Orrowen clerk stamping a marriage license, a human worker warming hands over cinder stolen from a lord's tally, a light-elf healer singing a lullaby without doctrine in it, a dark-elf mother teaching her daughter three ways to hide a key. Nothing grand enough to justify a machine. Everything too alive to be commanded.

The command engine died.

It died badly.

Gears spun loose. Brass ribs snapped. Cinder-glass teeth flew into the air like birds finally escaping. The platform lurched. The record storm, no longer channeled, burst outward. The dragon-moon eye opened another slit. The Choir began to sing with sudden joy.

Tavi fell.

Mara moved. So did Caldus, Saelith, Kesh by road-script, even one of the gnome ghosts. But Brakka was fastest because the bridge under Tavi decided falling was a kind of crossing and gave the troll authority. A stone hand rose from the platform and caught Tavi before she struck the floor.

Tavi lay in the stone palm, smoking, bleeding, alive.

She opened one eye.

"I would like," she said, "to file a complaint."

Mara dropped beside her, laughing and crying in the same breath. "Against whom?"

"Everyone who has ever used the word optimal."

Sava stamped the air.

COMPLAINT ACCEPTED.

Kesh leaned over them, hair wild, eyes too bright. "I am afraid I love all of you, and I need that treated as confidential."

"Denied," Sava said.

The laughter lasted less than a breath.

The destroyed command engine had freed the record. It had also removed the only tool that could have forced the chamber to hold.

Names rushed upward in a storm.

Orrowen's dead cried out, not as ranks, not as weapons, but as thousands of persons suddenly uncontained in the room where everyone wanted them to mean something convenient. Their voices struck the bridges, the armies above, the white roots, the black seals, the dragon-moon's lid. Some screamed in anger. Some pleaded. Some recited legal standing. Some sang street songs. Some asked after children. Some demanded apologies from people long dead. Some simply said their own names over and over because saying it themselves was the first uncommanded act left to them.

Serathiel lifted both hands.

Vaura raised her cracked seal rod.

The Choir opened its mouths wider.

Three answers began again: cleanse, seal, end.

Mara stood.

Her knees shook. Her cut arm burned. Her cinder cage rattled with every name in the chamber.

"No," she said.

No one heard her.

The dead were too loud.

So Mara did not speak louder.

She listened harder.
""",
    29: r"""## Chapter 29: Witnesses of Orrowen

Listening was not passive.

Mara had learned that in Ashgate long before cinder ever found her. Listening was how a runner survived a city that wanted to eat quick feet: the shift in a foreman's tone before a quota became violence, the cough that meant mine gas, the pause in Joryn's breath before he lied for someone, the silence of a street where debt collectors had arrived before dawn. Powerful people mistook listening for obedience because they only listened long enough to decide where to speak.

Mara listened now until the dead of Orrowen stopped being a storm.

Not because they grew quieter.

Because she stopped trying to hear them all as one.

Ruv Ossian shouted for the river gate. Leth of West Quay demanded his tools. Nim of south laundries cursed a judge, then apologized to her mother, then cursed the judge again with better grammar. A child named Selli complained that no one had explained whether witness standing came with snacks. A dead light-elf healer asked whether her correction had reached the White Orchard. A Khar Veyl clerk recited inventory numbers until Sava told him sharply that no one was asking him to become useful yet. Farther down, deeper under the voices, dragon names moved like tectonic weather.

Mara listened, and the cinder in her cage changed.

It did not become gentle. It did not become safe. It became specific.

"Names," she said.

This time the chamber heard.

Sava understood first. She always did when a thing became paperwork at speed. "State names," she called. "Not rank unless chosen. Not classification unless chosen. Name, standing, refusal."

Edrin Vale lifted his hollow-eyed face. "Orrowen citizens, appear."

Bone lanterns ignited one by one around the chamber.

Each lantern held a face.

Not all the dead. There were too many. But enough to begin. Faces appeared in light above bridges, galleries, engines, chains, white roots, black seals, dead civic desks. Some clear, some blurred, some only a mouth, a scar, a hand holding a slate. Each said a name. Each name entered the chamber not as fuel, proof, guilt, or holy infection, but as the beginning of a person.

The command engine's corpse tried to twitch.

Tavi, lying in the stone hand, threw a broken gear at it without sitting up. "Stay dead."

The gear bounced off the casing.

"Intimidating," Kesh said. He was shaking too hard to make the joke land cleanly.

"It knows what it did."

Mara moved to the central dais.

The dead pressed toward her. Serathiel's roots pressed toward them. Vaura's seals flickered, wanting containment. The Choir's song slid under every voice, promising relief if the names would just stop needing to be answered.

Mara had no answer large enough.

That used to terrify her.

Now it clarified the task.

"I am not naming you," she said.

The chamber stilled just enough.

"I am not your queen, judge, priest, engine, keeper, or commander. I will not make you an army. I will not make you proof that one side is clean and the other is guilty. I will not make your pain into a torch for someone else's doctrine. I will not spend you to win."

The dead listened.

So did the living.

"Name yourselves," Mara said.

The first to answer was not grand.

A woman in a translucent market apron lifted a hand. "Nim of south laundries. Citizen. I refuse purification without consent. I refuse sealing without review. I refuse stillness while my sister's children are uncounted."

The chamber burned blue.

True.

A cavalry captain appeared in saltwater reflection along the platform edge. "Ruv Ossian. Citizen and former captain by choice. I refuse classification as mounted asset. I refuse command by engine, court, priest, or seal. I refuse to trample evacuees again in any world."

Blue.

"Selli," said the child with the slate. "Citizen. I refuse battles in rooms where children can see them. I also refuse no snacks."

For one wild moment, the chamber did not know what to do.

Then it burned blue.

Kesh put both hands over his face. "I would die for her."

"You will not," Caldus said.

"I said would. I am growing."

More names came.

Not as a list. As a city.

The dead of Orrowen entered themselves into standing. Sava stamped until her arm blurred. Othel summoned other clerks from galleries, offices, half-collapsed balconies, and the courthouse above. Orrowen bureaucracy, freed from the sentence that had kept it killing Arveth, turned with frightening appetite toward the work of recognizing its own people.

Mara stood in the middle and held the refusal open.

Serathiel could not bear it.

"This is chaos," he said.

Saelith turned to him. She looked exhausted, and because she looked exhausted, she looked real in a way Lumenorath's beautiful law had never allowed. "No. It is what mercy hears when it stops demanding harmony first."

"They are suffering."

"Yes."

"They should rest."

"If they choose it."

"Pain destroys choice."

"Then stand beside them until choice returns. Do not steal it and call the theft healing."

His roots curled around the Lumenorath bridge. They had blackened where the record touched them, but the core still shone white. Serathiel looked less serene now. The memory storm had stripped him of distance. Mara saw the man under the saint-general: grief, discipline, terror of a world where mercy could fail even when practiced perfectly.

That made him more dangerous, not less.

Vaura stepped forward from the Khar Veyl bridge. "Orrowen standing entered by self-witness. Khar Veyl recognizes provisional -"

The chamber went red.

False.

Maelin laughed once, tired and merciless. "Again with provisional."

Vaura's jaw tightened. She tried again. "Khar Veyl recognizes Orrowen civic standing under emergency -"

Red.

Velra of the lower canals shouted, "Stop trying to keep a handle on it!"

Vaura rounded on her. "Without limits, standing claims will collapse the seal structure."

Tavi pushed herself upright in the stone hand. "Maybe the seal structure is not the person whose feelings matter most right now."

"If it fails, everyone dies."

"Everyone keeps using that sentence before doing something unforgivable."

Vaura looked at the dragon-moon below, then at Maelin, then at the dead naming themselves. Mara saw the calculation and the fear and, underneath both, a mother who had chained her daughter to keep her alive and could not understand why survival had not become gratitude.

Vaura lowered her seal rod.

"Khar Veyl recognizes Orrowen civic standing," she said. "Not provisional. Not owned. Not under house review."

The chamber burned blue.

True.

The Khar Veyl bridge shook as if a foundation had cracked. Wardens shouted. The blade-scholar screamed from above. Dark seals along the chamber walls broke one by one, releasing records, locks, and a flock of black moths made from shredded emergency writs.

Maelin did not forgive her mother.

She did, however, breathe.

Mara saw Vaura notice and nearly break.

Serathiel saw it too and mistook it for weakness to exploit. "You yield to the dead because guilt has made your house soft."

Vaura looked at him with ancient contempt. "Guilt made my house clever. My daughter made me honest."

The chamber burned blue again.

Serathiel recoiled from that light.

The Choir's song rose behind him.

Not loud. Tender.

It found the places where the room hurt most. It told Orrowen the work of standing would never end. It told Lumenorath that mercy would always be questioned now. It told Khar Veyl that every opened record would become another demand. It told Mara she had saved no one from the burden of remaining themselves.

It told the truth in the direction of despair.

Some of the dead faltered.

A row of bone lanterns dimmed. A clerk lowered her stamp. A child stopped writing. Khar Veyl wardens sagged. Pale Bough officers closed their eyes. Even Vaura's seal rod dipped again.

Mara felt the song wrap around her own spine.

No command, it whispered. No more choices. Let the naming end while it still sounds noble.

She thought of the crossing shrine. The wire hound. Kesh's road token. Caldus's scarf thread. Saelith's white petal. Ilyr's archive pin. Maelin's broken chain. Her own bit of black glass.

Proof that nearly stopping was part of the road.

Not the end of it.

"Kesh," she said.

His head snapped up. "Yes?"

"Roads."

For once, he did not joke.

Kesh stepped onto the goblin bridge, blood on his temple, coin-moth debt glowing under his skin. He lifted both hands, and the road marks in the chamber woke: smuggler routes, fever roads, bridge detours, lower-canal passages, Ashgate runoff lanes, Blackroot paths, salt-flat reflections, every ugly little way people had found to move when the official doors closed.

"If you want stillness," Kesh said, voice shaking, "do not ask roads."

The goblin bridge flared red-gold.

"Reedmere remains open. Tallow Ford remains open. Neth-by-the-Salt remains open. Kavik night stair remains open. Orrowen civic roads remain open. Lumenorath retreat lanes remain open. Khar Veyl evacuation routes remain open. No road named for escape may be converted into a chain while I owe breath."

The coin moth on his wrist opened its wings.

Kesh gritted his teeth.

Mara saw the cost hit him. Road debt did not vanish because he spoke bravely. It multiplied, or maybe it finally became honest about its size. The gray mark spread from his wrist to his palm, not ownership now, but obligation mapped in living lines.

Brakka placed one huge hand over the mark.

"Bridge hears road."

The pain eased enough for Kesh to breathe.

"I had," he said faintly, "a much more charming version prepared."

"No," Brakka said.

"Fair."

The roads carried the names outward.

Through bridge law, the armies above heard Orrowen's citizens naming themselves. They heard Khar Veyl's recognition. They heard Pale Bough corrected soldiers answering the dead not with cleansing but with their own names. They heard routes opening that did not require victory first.

The Choir's song cracked.

Edrin Vale climbed onto the dais beside Mara.

Sava joined him.

"Orrowen appears," Edrin said.

This time, all the dead answered.

We appear.

The chamber shook.

Mara did not command them.

She witnessed their standing and let the force of it become theirs.

The dragon-moon eye opened wider, not in anger now, but in recognition of a noise old dragons had perhaps forgotten: the dead refusing to be used by the living and refusing also to be quiet for the comfort of grief.

Serathiel lifted both hands.

White roots tore from every remaining hymn wagon, every white-root lantern, every obedient soldier still clinging to the old beautiful law. They plunged down through the Lumenorath bridge toward the witnessing dead.

Saelith stepped into their path.

Mara moved with her.

So did Liora, the older standard-bearer, three Pale Bough officers, and a dozen soldiers above who had never imagined disobedience would require so much running.

The roots struck the red-gold line of corrected mercy and held.

Serathiel's face went terrible.

"Then I will save you from yourselves," he said.

His voice became a hymn.
""",
    30: r"""## Chapter 30: Serathiel Falls

Serathiel's final hymn had no words.

Words had failed him. That was what made the sound so dangerous. Doctrine could be argued with. Commands could be refused. Even beauty, once named, could be answered by another beauty. But the hymn he loosed into the dragon-moon chamber was older than the Pale Bough's laws and simpler than mercy. It was the sound a person made when he could no longer bear the freedom of those he loved.

White roots burst from the Lumenorath bridge.

They did not strike like spears this time. They grew like a forest.

In one breath, the platform became a grove of pale trunks and shining thorns. Roots wrapped the dais, the broken command engine, the witness bridges, the ledger case, the Orrowen lanterns, the Khar Veyl seals, the goblin road marks, the gnome gears, the human ash tags. They climbed toward the record storm not to destroy it, but to make it beautiful, orderly, painless. Wherever a root touched a name, the name softened. Rage became rest. Refusal became release. A person became a gentle light in a tree.

The first Orrowen citizen taken by it smiled.

That almost broke Mara.

Nim of south laundries looked so relieved when the root touched her. All the fight left her face. Her lantern glow became white and clean. She stopped cursing the judge. Stopped asking about her sister's children. Stopped being inconvenient.

"No!" Sava shouted.

The clerk's stamp struck the root and bounced off.

Serathiel's hymn deepened.

"He is not killing them," Caldus said, horror in his voice.

Saelith's face was ashen. "No. He is making them easy to mourn."

The phrase entered the chamber and burned blue.

True.

Mara ran toward Nim's lantern. A root lashed around her ankle, warm as a healer's hand. It did not hurt. That was the wrongness. It asked for trust with the patience of someone who had learned bedside manners before he learned conquest.

The root showed Mara Ashgate quiet.

Furnaces cold. Joryn sleeping without pain. Kell's hands clean. Children unhungry. No ash-runners. No tallies. No one choosing who worked lower vents because no one worked at all. Peace as a white orchard laid over soot.

Vorrakai's grief moved under the hymn, delighted by kinship.

See, the deep voice seemed to say. He understands one door.

Mara cut the root with her knife.

The blade snapped.

Caldus reached her and severed it with his sword. The root bled white sap that smelled of hospital linen and graves.

"Up," he said.

"Nim."

"We get her together."

Saelith was already there, both hands pressed to the lantern root. Red-gold light poured from her fingers. The white root fought her, not with force, but with memory: Serathiel carrying a fever child, Serathiel teaching her to hold a dying hand, Serathiel saying mercy must arrive before fear becomes law. Saelith wept as she burned through it.

"He did good," she said through her teeth. "That is the cruelty. He did good, and then made the good a throne."

The root around Nim cracked.

Nim's eyes sharpened.

"My sister," she gasped. "Her children. Do not let me forget angry."

"I won't," Mara said.

Nim's lantern flared yellow, not white.

Across the platform, the same fight broke everywhere.

Brakka stood at the center, maul planted, roots climbing her legs like pale snakes. Every time one root crossed a vow-crack, it tried to turn bridge law into a peaceful permanent road: no more crossings, no more floods, no more choice, only a shining span no one could leave. Brakka roared and drove her maul deeper.

"Bridge is not cage!"

The troll bridge exploded with river-dark light, throwing roots back.

Tavi, still half-burned, dragged herself from the stone hand and began breaking roots with bits of the dead command engine. "I just killed one morally bankrupt device! Do not make me process a tree!"

One of the gnome ghosts handed her a cutter.

She stared. "You had this the whole time?"

"We remembered late."

"Story of every guild."

Kesh moved by road-script between roots and lanterns, slapping route tags onto dead citizens before the white roots could turn them into memorial glow. "Detour! Detour! You are not available for ornamental peace! This way to ugly continued personhood!"

Sava stamped every tag he placed.

Edrin called names until his voice cracked into blue sparks.

Ilyr could barely stand, so Maelin held him upright and read from the opened record in his place. Each page she read gave the roots something honest to choke on: Matriarch Aurenne's omitted line, Khar Veyl's custody crimes, human furnace contracts, gnome objections, goblin rescue routes, troll bridge deaths, Serathiel's first silence of a witness who had not consented.

Serathiel walked through it all.

The roots parted for him. He looked almost luminous now, not because he had become stronger, but because he had shed everything that was not the hymn. His robes burned at the hem. His hair floated in the moonlight rising from below. His eyes held tears.

He came to Saelith.

"I would have spared you this," he said.

She stood between him and Nim's lantern, hands shaking, face wet, red-gold light guttering around her fingers. "I know."

"You think that makes me worse."

"No." She swallowed. "It makes it hurt."

He closed his eyes, and for one impossible moment Mara thought he might stop.

Then a Choir singer stepped behind him and began to hum.

The hum wrapped his grief in Vorrakai's stillness.

Serathiel opened his eyes.

"Pain is not proof of truth," he said.

"No," Saelith answered. "But neither is quiet."

He lifted one hand toward her.

Mara stepped beside Saelith.

Caldus stepped beside Mara. Tavi, limping, came next. Kesh stumbled out of road-script and nearly fell, but Brakka caught him by the back of his coat and set him down on his feet as if correcting furniture. Ilyr and Maelin came with the open ledger. Edrin and Sava came with stamps and civic standing. Liora came with the corrected Pale Bough soldiers. Vaura came last, not as ally exactly, but as a ruler who had finally understood that standing aside was also a choice the chamber could read.

Serathiel looked at the line they made.

"You mistake company for righteousness," he said.

Mara shook her head. "No. We mistake being alone for danger."

The chamber burned blue.

True.

Serathiel's hymn faltered.

Not because Mara had defeated him. Not because the company was pure. They were a scandal of partial repairs, open debts, contested loyalties, injuries, guilt, and bad jokes. But the hymn required each person to meet Serathiel alone, as patient before healer, sinner before purifier, frightened child before beautiful law. It did not know what to do with people who kept interrupting one another's surrender.

Saelith stepped forward.

This time Mara let her go.

Serathiel's roots rose around Saelith like a white chapel.

"You can still come home," he said.

Saelith touched the red fungal bell at her throat, then the white thread tied around it. "Home is the place where my mercy can be corrected."

"Then you have none."

"Then I will help build one."

She began to sing.

It was not the cleansing response. It was not Aurenne's line alone. It was all the broken pieces Saelith had carried: lullaby, grief, apology, field command, prayer, witness filing, Mara's name spoken like a door, Nim's anger, Liora's lost name, the Pale Bough corrected. Her voice was not perfect. It cracked. It shook. It ran out of breath and found more. That was why the chamber listened.

The corrected Pale Bough soldiers joined her.

Then Orrowen's dead, not in harmony, because harmony would have made the old mistake. They joined in counterpoint: names, objections, street songs, last words, complaints, laughter, legal statements, children's nonsense. Khar Veyl wardens added seal oaths stripped of ownership. Goblin road marks clicked rhythm under Kesh's feet. Gnome ghosts tapped broken gears. Brakka's maul beat once, twice, like stone under a river. Caldus did not sing well, but he sang anyway, which made Tavi stare at him in delighted horror while also singing worse.

The white roots recoiled.

Serathiel covered his ears.

"No," he whispered.

The sound around him did not cleanse, seal, command, or still.

It remembered.

The root forest showed what it had hidden: every witness silenced for mercy, every child taught to fear memory, every healer who doubted and obeyed, every person Serathiel had truly comforted, every comfort he later used as proof that his hand should never be refused.

Honest memory broke his hymn.

Not by proving he had never loved.

By proving love had not made him safe.

Serathiel fell to his knees.

The roots collapsed around him, not dead, but unmastered. White branches shrank back into the Lumenorath bridge. Lanterns flickered. Pale Bough soldiers above dropped their hymn staves. Some wept. Some shouted. Some simply stared at their hands as if hands could be strangers.

Serathiel looked up at Saelith.

"What am I," he asked, "if not mercy?"

No one answered quickly.

That, Mara thought, was the first mercy he had been given all day.

Saelith knelt in front of him. "A man who wanted peace so badly he made people quiet."

His face crumpled.

"I cannot bear the noise."

Vorrakai's presence surged, tender as a grave. The Choir singer behind him smiled and opened her arms. Here was the last door Serathiel could take: if corrected mercy hurt too much, stillness would receive him and make the pain meaningful.

Mara felt him lean toward it.

Saelith felt it too.

She did not grab him.

"Do not make your defeat into another altar," she said.

Serathiel laughed once. It broke halfway through. "You learned cruelty."

"No. I learned not to confuse refusal with cruelty."

He closed his eyes.

For a breath, the whole chamber waited.

Then Serathiel removed the living white-root crown from his brow.

It tore skin when it came free. Blood ran silver down his face. The crown writhed in his hands, looking for doctrine, command, a head to sanctify.

Serathiel set it on the platform between them.

"I stand down," he said.

The chamber burned blue.

True.

The Lumenorath bridge cracked from end to end.

Above, the holy war stopped pretending it was holy.

That did not make it peace.

It made peace possible and everyone responsible for the uglier work after awe.

Vaura lowered her seal rod fully. "Khar Veyl recognizes cessation of hostilities under bridge law."

Liora lifted the upside-down white banner. "Pale Bough corrected recognizes cessation."

Sava stamped so hard the sound echoed into the armies above.

HOSTILITIES SUSPENDED BY MIXED WITNESS.

Not ended. Not healed. Suspended. The honest word mattered.

The Choir singer behind Serathiel stopped smiling.

Mara turned.

The singer's cinder-filmed eyes were fixed not on Serathiel now, but on the dragon-moon below. The command engine was dead. The roots were broken. The seals had yielded. The dead stood as witnesses. The war had stopped.

Every reason to hold the dragon-moon closed had weakened at once.

The chamber chains groaned.

Vorrakai spoke through the singer.

You have chosen noise.

Mara looked down at the pale horizon beneath the platform.

"Yes," she said.

Then hear what wakes beneath it.
""",
    31: r"""## Chapter 31: One Eye Opens

At first, the dragon-moon did not move.

That made the sound worse.

The groan came from everywhere: chains, bridges, roots, seals, gears, civic desks, ghost-lamps, the bones of Orrowen, the cinders under Ashgate, the white roots of Lumenorath, the black vaults of Khar Veyl, roads that had never seen the sun, hearths where families warmed their hands without knowing what dead fire remembered. It was the sound of a prison discovering that every lock had been built by someone with an excuse.

Mara stood at the edge of the platform and watched the horizon breathe.

The pale curve below them rose and fell once.

The dragon-moon was not a moon.

Not metaphor. Not prison only. Not wound only.

A body.

A dead body still dreaming because the world had never stopped using it.

The closed eye beneath them opened.

Only a slit.

That was enough.

Light rose from below, not bright, but total. It did not illuminate surfaces. It illuminated histories. Every person in the chamber cast more than one shadow: what they had done, what had been done to them, what they had excused, what they had refused, what they might yet become if the next fear found them quickly enough. Mara saw her own shadows spread across the platform. Ash-runner. Witness. Almost weapon. Friend. Coward sometimes. Brave sometimes. Hungry child. Woman who had said no to a dragon and still wanted rest badly enough to fear herself.

Across the chamber, others saw themselves too.

Caldus saw the king's cloak, then the man who snapped the lance in the salt flat, then a future where guarding became another way to avoid choosing. He lowered his sword point and did not look away.

Saelith saw white roots in her hands, red-gold light, the first witness she had silenced, Liora kneeling, Serathiel's crown on the floor. She wept without hiding.

Tavi saw the Glass Engine, the command engine, Master Quen's coat over a sleeping child, the root-hound's cracked eye, a hundred machines she had loved because they seemed less likely to betray her than people. She put one burned hand over the empty collar on her wrist.

Kesh saw roads opened and sold, his aunt carrying children through fever smoke, his own clever mouth closing over fear, three villages written under his skin, and a thousand possible exits that would cost more than charm. He looked ill. He also remained standing.

Brakka saw bridges that held and bridges that failed, oathmothers dying seated so stone would not feel abandoned, herself kneeling under an army's weight and wanting, for one breath, to let every traveler learn the river's lesson without her.

Ilyr saw names he sold. Names he saved. Names he delayed using because guilt had looked better when called timing. Maelin saw chains called love. Vaura saw a city kept alive by locks it had mistaken for spine. Serathiel saw every quiet face he had called healed.

No one in the chamber was clean.

No one in the chamber was empty.

Vorrakai's voice entered the light.

Not loud.

Everywhere.

Now you see.

Mara did not answer.

The first dragon's grief moved through the opened slit like deep ocean pressure. It did not command. It did not need to. It showed the next truths patiently, kindly, mercilessly. Lumenorath and Khar Veyl would argue the terms by morning. Orrowen's citizens would disagree among themselves about what standing meant after centuries of being misused. The Pale Bough corrected would splinter. Khar Veyl hardliners would not all stand down because Vaura had spoken one true sentence in a chamber. Human kingdoms above would learn the dead had become politically inconvenient persons and immediately ask how that affected fuel, roads, and war.

Every victory would become work.

Every work would hurt someone.

Every choice would leave a remainder.

I can end the remainder, Vorrakai said.

The Choir singers knelt.

Some Orrowen dead knelt too, exhausted beyond defiance. Some Lumenorath soldiers. Some Khar Veyl wardens. One of the gnome ghosts. Even Serathiel bowed his head, though whether in worship, shame, or simple fatigue Mara could not tell.

Mara wanted to kneel.

She did not.

Not because she was stronger than them. That lie had nearly killed her in other rooms. She remained standing because Saelith's hand found hers, and Caldus's shoulder touched her own, and Tavi leaned against her hip because standing independently was, at the moment, overrated. Kesh's road-script flickered around their boots. Brakka's bridge law hummed under the platform. Ilyr and Maelin held each other upright. Edrin and Sava stood with Orrowen's stamps raised. The company answered the eye the only way they knew how now: badly, together, and with insufficient dignity.

"No," Mara said.

The slit of the eye widened.

You say no because you can still imagine repair.

"Yes."

Repair is the longest cruelty.

"Sometimes."

You will fail.

"Yes."

You will be used.

"I know."

You will use others.

That struck deepest because it was not accusation alone. It was warning, prophecy, and memory. Mara thought of the way people already looked toward her, the way her refusals could become commands if spoken from the right height. She thought of saying "hold the line" and Kesh obeying before asking which one. She thought of Tavi between the spindle and Mara's cage. She thought of every underdog story that ended by placing a crown of usefulness on the person who had survived being used.

"Then they must correct me," Mara said.

Vorrakai's attention sharpened.

"Not worship me. Not trust me past witness. Correct me."

The chamber burned blue.

True.

Kesh exhaled shakily. "I have a list started."

"Of course you do," Mara said.

Tavi muttered, "Mine has diagrams."

Saelith squeezed Mara's hand.

The dragon-moon eye held them.

Then the light turned outward.

Every cinder in Vael Taryn answered.

Mara felt it happen more than saw it. In Ashgate, furnace ash rose from cold grates and formed names before startled workers. In Harrowmere, dead ledgers slammed open. In Lumenorath, white-root orchards flushed red-gold and whispered Aurenne's omitted line. In Khar Veyl, sealed archives rang like bells. In goblin roads, old route stones lit in forgotten tunnels. At troll bridges, rivers stopped for one breath. In gnome workshops, engines built around cinder cores refused calibration. In graveyards, hearths, crowns, weapons, lamps, and jewelry, dead dragon memory woke enough to ask, Who uses me?

The question passed over the world.

Then came the answer beneath it.

Vorrakai.

Not fully awake.

Not free.

But heard.

The chamber chains snapped one by one, not all, not enough to loose the dragon-moon, but enough to change the weight of the world. The platform lurched. Bridges buckled. Vaura shouted evacuation orders. Sava shouted better ones. Caldus dragged Serathiel to his feet when the former saint-general did not move quickly enough. Saelith helped Liora carry a Pale Bough officer whose roots had burned. Brakka took the central bridge on her shoulders again. Kesh opened roads so fast the coin-moth lines on his arm blazed. Tavi, half-conscious, directed gnome ghosts in stabilizing a collapsing chain with language so profane several ancient engineers looked impressed.

Mara went to the edge.

Below, the eye remained open as a slit of pale fire.

Not looking at the chamber now.

Looking through it.

"Mara!" Caldus called.

She should have turned.

Instead she looked into the eye and saw a court of long memory under a sky of broken dragons, a road made of cinders leading into Book Three's dark, and something vast moving toward the world not with hunger, but with exhausted love curdled into certainty.

Vorrakai did not want to burn Vael Taryn.

It wanted the world to stop hurting.

That was why it had to be stopped.

Mara stepped back from the edge.

"We leave," she said.

No one argued.

That worried her until Kesh limped past and said, "I am arguing internally for tradition."

They climbed out through a chamber that no longer trusted its own locks.

The armies above had not become friends. That would have been a child's lie and an insult to everyone who had died. But the lines had broken. Lumenorath medics worked beside Khar Veyl pump wardens. Orrowen citizens directed traffic through their own streets. Pale Bough corrected soldiers collected hymn staves and stacked them under Sava's supervision. Vaura stood in the battlefield with her seal rod lowered, issuing orders that began with citizen standing recognized. Serathiel sat under guard beside the upside-down white banner, crownless, silent, alive.

Saelith stopped before him.

Mara gave them distance, though not too much. That had become the company's grammar.

Serathiel looked up. Without the crown, he seemed smaller. Not harmless. Smaller.

"What will they do with me?" he asked.

"Ask those you harmed," Saelith said.

"And you?"

Her face trembled. "I will testify."

He closed his eyes. "Against me."

"Truthfully."

After a moment, he nodded.

It was not redemption. It was not enough. But it was a door he had not closed.

On the Khar Veyl side, Maelin stood before Vaura. They did not embrace. Mara did not know if they ever would. Vaura offered her daughter a broken chain link, the one removed from the house retention records when Orrowen standing invalidated the old bloodline clauses. Maelin looked at it for a long time.

"Keep it," she said.

Vaura flinched.

"Not as claim," Maelin added. "As evidence."

Vaura folded her hand around the link.

Ilyr, leaning on a borrowed staff, looked at both of them and wisely said nothing.

Tavi found the root-hound's cracked eye where she had set it into the Glass Engine bridge. It had gone dark, but when she touched it, one tiny projection flickered: a road, badly drawn, with a lopsided dog at the end. She pressed it to her forehead and did not make it noble.

Kesh's three road debts remained open, but Orrowen clerks had added routes, witnesses, and annoying annotations. He stared at the new filings in horror.

"I have become administratively supported," he said.

Sava smiled. "My condolences."

Brakka slept sitting upright against a bridge pillar, one hand still on her maul. Caldus tried to wake her for bandaging. She opened one eye and said, "Later." He, being wiser than he used to be, obeyed.

Near what passed for dawn under the world, Orrowen's bells rang.

Not Arveth's sentence.

Not alarm.

A civic assembly.

The dead city called itself to meeting.

Mara stood on a balcony overlooking streets of ghost-lamps, bone canals, black towers, wounded soldiers, freed prisoners, angry clerks, exhausted healers, and citizens who had been told for centuries that they were over. She should have felt triumph. Instead she felt the enormous practical terror of anything true beginning.

Saelith came beside her.

"You are shaking," she said.

"So are you."

"Yes."

They stood with that honest, unadorned fact for a while.

Below, Edrin Vale helped Sava arrange the first open roll of Orrowen citizens recognized by self-witness. The first name entered was not a ruler's, not a judge's, not a hero's.

Selli.

Someone had found her snacks.

Mara laughed then, finally, and the laugh hurt.

Caldus joined them with his arm re-bound. Kesh leaned on the balcony rail and pretended he had not come because he needed company. Tavi limped in last, smelling of smoke and victory's least glamorous consequences. Brakka remained asleep, which everyone agreed was bridge law.

The company looked out over the city.

Book Two's war was over.

Not healed.

Not tidy.

Stopped.

That mattered enough to stand on.

Then every cinder in the city pulsed.

Once.

Twice.

On the third pulse, a voice older than every nation in Vael Taryn moved through the stones, through Mara's blood, through the dragon-moon's opened eye far below.

Not command.

Not yet.

A greeting.

I remember you.

Mara gripped the rail.

Far under the world, a horizon curved where no horizon should be.

One eye watched from the moon below.

And across Vael Taryn, from crown to hearth to hidden grave, every cinder answered.
""",
}


EXTRA_DEEPENING: dict[int, str] = {
    28: r"""Listening harder did not make the dead easier to bear.

It made them less convenient.

The first voice Mara separated from the storm belonged to a man who did not know he was dead. He kept asking whether the south bakery had opened. Over and over, through the scream of the broken command engine and the groan of the dragon-moon chains, he asked about bread. Not prophecy. Not justice. Bread. The detail struck Mara with such force that she nearly lost the thread. The world had buried a dragon under Orrowen, split elves into light and dark over custody and fear, built engines to command memory, raised armies, made saints and judges and monsters, and somewhere inside the wound a man still wanted to know if the bakery had opened.

She found another voice, a woman reciting water-pump maintenance in panic because she had died before finishing the instructions and could not believe anyone else would remember the left valve stuck in winter. A boy swore he had not stolen the blue slate. A Khar Veyl clerk whispered inventory numbers because numbers had been the only way he was allowed to grieve. A Lumenorath healer kept saying, I thought release meant release. A gnome engineer repeated, I objected, then quieter, I signed anyway.

Mara let each one exist without asking what use they were.

That was harder than battle.

Around her, the chamber tried to become a single event. Serathiel's roots gathered for a final cleansing answer. Vaura's seals sparked, desperate to contain the witness flood before it tore the moon-lock wider. The Choir's hum made every separate voice blur at the edge, inviting them to lay down the burden of being distinct. Even the broken command engine contributed in death, its gears twitching whenever the noise grew too complex, as if usefulness were a reflex machines could not lose.

Tavi heard the twitching.

She rolled off the stone hand with a sound that was half groan, half insult, and crawled toward the engine's corpse.

"Absolutely not," she said.

Mara wanted to tell her to stay down. She also knew exactly what Tavi would do with that suggestion. So she listened and trusted Brakka, Caldus, and gravity to negotiate.

Tavi reached the engine, hauled herself upright by a cracked gear rim, and opened an inspection panel with her teeth because both hands were shaking too hard for tools. Three gnome ghosts moved to help. She glared at them until they stopped trying to do the work for her and instead held the panel steady. That distinction mattered to Tavi even while half-conscious. Especially then.

"Residual command pulse," she said, spitting brass dust. "It is trying to restart from witness panic. Because of course it is. Why should a morally obscene engine have the decency to die once?"

"Can you stop it?" Caldus asked.

"I can annoy it into structural embarrassment."

"Is that a yes?"

"It is a gnomish yes."

She jammed the root-hound collar into the opened panel. The collar had no power left, or should not have. Yet when it touched the command lattice, one last projection flickered: the lopsided dog standing with all four impossible legs braced, barking silently at a gear larger than a house.

Tavi's face collapsed for one breath.

Then she used the projection as a brace and tore out a bundle of red wires.

The command engine's corpse gave a final shudder and went dark.

"Good dog," Tavi whispered.

No one made it noble.

That was the mercy she had asked for, and the company had learned to pay attention.

The engine's death changed the sound of the chamber. The dead voices still roared, but the subtle drag toward use vanished. They were no longer being pulled into one channel. The names scattered. Some struck the Lumenorath bridge and made white roots bloom with memory instead of command. Some struck Khar Veyl seals and cracked them open from within. Some rushed toward the dragon-moon and woke scales along its closed lid. Some simply circled the platform, not ready to enter any law.

Mara had to resist the urge to organize them.

It was a small urge and a deadly one. She felt how easy it would be to say: you there, stand for grief; you, for proof; you, for outrage; you, for peace. The very act of saving them from other people's categories tempted her to make new ones. She understood then how tyrannies could be born inside rescue. Not because rescuers lied about caring, but because fear hated the time it took to let people arrive unarranged.

She opened both hands.

"I hear you," she said.

The chamber did not flare.

The sentence was too small for blue fire. It was also the first true thing she had.

"I hear you," she said again, to the bakery man, the pump woman, the slate boy, the clerk, the healer, the engineer, to every name she could catch and every name she could not. "I will not make one voice from you."

That was when Sava understood what the next law had to become.

The clerk climbed onto a broken piece of the command engine and lifted her stamp. "No collective standing without individual standing entered."

Assistant Registrar Othel gasped. "That invalidates half the emergency archive."

"Good."

"It will take centuries to repair."

"Then we had better stop wasting mornings sentencing Arveth."

Othel stared at her.

Then he smiled with half a jaw and summoned every clerk in Orrowen.

They came through doors the chamber had not possessed a moment before. Dead clerks, living clerks, ink-bone clerks, clerks who were only hands and stamps, clerks carried in memory by children who had watched them die. They came muttering about forms, jurisdiction, ink, precedent, and the emotional irresponsibility of apocalypse. They came because bureaucracy had been weapon, cage, and coffin in Orrowen, and Sava had decided it could also become a crowbar.

Tables unfolded from the platform.

Ledgers opened.

Stamps lifted.

Mara laughed once, helplessly.

Caldus looked at her as if checking for injury. "What?"

"The dead are saving themselves with paperwork."

Kesh, pale and sweating, appeared beside her with road-script still sparking around his boots. "I have never been more frightened or aroused by civic process."

Tavi, flat on her back near the engine, lifted one burned hand. "Do not make me regret saving you."

"Too late."

The laughter that followed was thin and uneven, but it moved through the chamber like fresh air through a sealed room.

Then Serathiel's roots tightened.

He had heard the clerks. He had heard Orrowen choosing complexity over release. It wounded him in a place Mara almost understood. His mercy could survive being opposed by soldiers. It could survive dark-elf seals, human crowns, gnome engines, even Mara's refusal. It could not survive the dead looking at quiet and choosing forms, argument, delay, and more mornings.

"This is cruelty," he said.

Saelith turned toward him.

"No," she said. "This is consent taking longer than your pity can bear."

The chamber burned blue.

True.

Serathiel's final hymn began as a single note under his breath.

Mara kept listening.

The dead kept naming.

And Tavi, who had killed the command engine rather than win by theft, closed her eyes against the pain and said, "Somebody write down that I was right."

Three clerks did.
""",
    29: r"""The witness rolls began as chaos and became a city remembering how to stand in public.

Sava divided the platform into precincts before anyone could ask if that was allowed. "Market dead to the west rail. Civic officers by last chosen office, not imposed classification. Children with slate witnesses near the blue lamps. Those who cannot remember names to the pending table. Those who remember too many names to the contested table. Anyone trying to volunteer as symbol will be struck from the queue until they develop self-respect."

"Can she do that?" Kesh asked.

Othel clutched a stack of blank forms to his chest. "I think she just did."

The chamber accepted the divisions not because they were perfect, but because each one included a path of refusal. The market dead argued immediately about whether fishmongers belonged with river trades or food sellers. Two ancient judges attempted to claim priority and were sent to the back by a laundress with a louder voice. A row of dead soldiers asked whether they could enter as soldiers if soldier had been the only word they had chosen in life. Sava said yes, if chosen, no, if assigned to erase something else. Three of them began arguing with their own records.

It was impossible.

It was working.

Mara moved among the tables while the armies above received every entered name through bridge law. She did not lead the process. She carried water, fetched ledgers, repeated names when voices failed, and once held a dead child's slate while he drew a map to the house he wanted entered beside his name. The work steadied her. No one could call a person a banner while she was trying to spell a canal address correctly.

At the pending table, she found the Lumenorath healer whose voice had trembled through the storm.

The healer was dead, young by elf measure, hair braided with white thread and ash. Her hands kept making the old cleansing sign and then flinching from it.

"I do not know what I am," the healer said.

"You do not have to decide all of it now," Mara said.

"I silenced witnesses. Then I smuggled names. Then I died before I returned them. If I enter as healer, I lie. If I enter as criminal, I erase the smuggling. If I enter as rescuer, I insult the people I silenced."

Mara looked toward Sava, but the clerk was busy threatening a judge with procedural demotion. Saelith came instead.

The dead healer stared at her exile colors. "Pale Bough?"

"Corrected," Saelith said. "In progress."

"That sounds insufficient."

"It is."

The healer nodded, oddly relieved. "Then enter me as Aneth of White Orchard, healer and silencer, smuggler of seventeen names, seeking the other twelve."

Saelith wrote it down.

Her hand shook on silencer. She did not cross it out.

Across the platform, Maelin supervised Khar Veyl witnesses whose standing had been tangled in house custody. She was not gentle. Gentleness would have let too many people hide. But she was careful. She made wardens state whether they had signed retention documents by order, fear, agreement, or convenience. She made retained witnesses state whether they wanted house names removed, contested, or kept as evidence. Vaura watched from a distance until Maelin looked at her and said, "If you are going to hover like a guilty tower, carry forms."

Vaura carried forms.

She carried them badly at first, with the stiffness of a ruler unused to being useful without being obeyed. Then Velra snapped that she was handing the wrong sheet to flood-canal witnesses, and Vaura corrected herself without ordering Velra arrested. The chamber noticed. It did not make Vaura good. It made her present.

Ilyr sat at the edge of the dais with a blanket around his shoulders, looking like a beautiful corpse who had declined the appointment. Kesh sat beside him because the goblin road bridge still threw him back to the chamber whenever the upper battlefield grew too tempted to improvise violence.

"I have decided," Kesh said, "that public accountability is exhausting and should be available only by appointment."

Ilyr looked at him. "You would miss the walk-ins."

"True. They carry better purses."

After a while, Ilyr said, "Do they hate me?"

Kesh did not ask who. "Yes."

Ilyr nodded.

"Also no. Also not only. It is a very crowded office."

"That is not comforting."

"It was not meant to be. Comfort is extra."

Ilyr watched Maelin hand a form to a dead woman whose name he had once redacted from a sale copy. The woman took it, spat at his feet, and then asked Sava where to file a correction because the spit had not been enough.

Ilyr closed his eyes.

Mara saw Kesh reach over and, with great irritation at himself, rest two fingers against Ilyr's sleeve.

The Orrowen roll grew.

Not just Orrowen. That was the surprise. Once the dead entered themselves, the living began to understand the shame of remaining categories. Lumenorath soldiers entered names beside corrections. Khar Veyl wardens entered offices beside culpabilities. Human ash tallies woke along the bridge and asked who had been counted as fuel. Gnome ghosts entered objections filed after death and promised, under Tavi's glare, to stop calling posthumous dissent sufficient.

The dragon-moon watched through its widening slit.

Its attention pressed on every name, vast and old. Mara felt that pressure and understood why the first courts had panicked. This much memory could drown a people. Maybe it had drowned Orrowen in the beginning. Maybe every terrible emergency measure in the chamber had begun as someone staring at a flood and reaching for the nearest gate.

That did not excuse the gate becoming a throne.

At the center table, Selli climbed onto a chair.

"I have a statement," she announced.

Sava did not look up. "Is it relevant?"

"Yes."

"Proceed."

Selli held up her slate. On it she had written in large, uneven letters: CHILDREN ARE NOT EVIDENCE UNLESS THEY WANT TO BE AND ALSO SNACKS ARE CIVIC.

Othel began to object to the second clause. Sava silenced him with one finger.

"Entered," Sava said.

The chamber burned blue.

True.

That, absurdly, was when the witness standing became irreversible.

Not because of snacks. Probably. Because the chamber had accepted a child's refusal to be made pure proof of anyone's argument. Lumenorath could not use dead children as reason to cleanse. Khar Veyl could not use them as reason to seal. The Choir could not use them as reason to end choice. Orrowen could not use them as a sentimental shield against its own failures. Selli had claimed herself and her appetite in the same breath, and the dragon-moon had heard.

The bone lanterns ignited higher.

One by one, the witness bridges changed color. Orrowen blue became many blues, market, canal, court, school, bridge. Lumenorath white threaded red-gold. Khar Veyl violet broke open around lower-canal green. Goblin road marks ran wherever someone needed a path between categories. Gnome brass dimmed from command to tool. Human ash tags lifted from Mara's bridge and became not fuel tallies, but names pending correction.

Mara felt the power of it rise.

It was not her power.

Thank all buried dragons, it was not her power.

It belonged to the witnesses and therefore could not move as quickly as a weapon. It argued with itself. It paused for spelling. It objected to procedures it had requested five breaths earlier. It required translation, apology, amendment, and snacks. It was the least efficient force Mara had ever seen.

It was the first force in the chamber that did not want to own anyone.

Vorrakai's Choir began to lose voices.

The singers did not all renounce. Some clung harder to stillness, faces peaceful and wet. But others faltered as names reached them. One woman lowered her hands when she heard her brother self-enter as a canal mason and complain about her singing. A dead man in ash-gray robes whispered that he had joined the Choir because no one remembered his village, then heard Kesh's road marks speak the village name from an old route debt. He began to sob.

The Choir's harmony broke into persons.

Vorrakai did not withdraw.

The grief below the chamber deepened.

Mara felt it like weather pressure before a storm.

You teach them to keep hurting, Vorrakai said.

The voice touched every witness, every bridge, every open roll.

Mara stood with one hand on Selli's chair and one on the central dais. "No."

Then what do you teach?

She thought about that. She refused the first answer because it sounded too much like a slogan. Refused the second because it made her sound wiser than she was. At last she looked around the chamber: Tavi bleeding beside a dead engine, Saelith writing a healer's confession, Kesh making roads for people who might never pay him, Brakka holding a bridge no one thanked enough, Caldus guarding without owning, Ilyr surviving hatred, Maelin making forms sharp enough to cut chains, Vaura carrying papers, Serathiel preparing to turn mercy into a final hymn.

"To answer each other," Mara said.

Vorrakai's silence became attention.

"Not well. Not cleanly. Not forever. But answer."

The chamber burned blue.

True.

Serathiel's final hymn rose.
""",
    30: r"""Serathiel did not fall quickly.

That mattered.

Too many stories let beautiful tyrants break at the first honest song, as if the world were eager to reward truth with clean timing. Serathiel had spent centuries teaching mercy to obey him. His roots ran through soldiers, orchards, prayers, hospital rooms, children's lessons, funeral rites, and every person who had been comforted by the order he later weaponized. Honest memory broke his hymn, but it did not erase the reasons people had sung it.

His final grove fought on.

White roots still held a dozen lanterns. They did not silence the dead fully now, but they softened them, making each witness sound less angry, less inconvenient, more ready to be forgiven by the people who wanted forgiveness to arrive before accountability. Pale Bough officers who had corrected themselves still reached instinctively for the old harmony when fear spiked. Khar Veyl hardliners pointed to the root-silenced dead as proof that Lumenorath could not be trusted. Vaura's wardens reached for seals. The Choir's broken singers hummed wherever exhaustion made an opening.

Peace could fail in a hundred small ways after the grand gesture.

Mara learned that in the minutes after Serathiel's hymn cracked.

A Lumenorath soldier tried to drag a silenced Orrowen lantern away for "protection." Sava struck him with a stamp and entered assault. A Khar Veyl warden attempted to reclassify root-touched dead as unstable evidence. Maelin tore the form in half and made him write unstable person requiring chosen support. A Choir singer put both hands on Serathiel's shoulders and whispered that he could rest now, that everyone had seen enough, that his surrender could be perfect if he stopped choosing through pain.

Saelith saw that last danger first.

She did not go to Serathiel alone.

"Liora," she said.

The shaved-headed scout came, trembling but armed with the upside-down banner. Two corrected Pale Bough officers followed. Then Aneth of White Orchard, the dead healer and silencer, whose pending record still glowed at her breast. Saelith looked at them all.

"If I speak alone, he can make me his lost daughter," she said. "If you speak alone, he can make you confused followers. We speak as corrected witness."

Liora swallowed. "What do we say?"

"The truth we can bear."

They walked to Serathiel through roots that wanted to recognize Saelith and reject the rest. She did not let them. Every step she took, she waited for the others to step with her. The delay was painful. It saved them from becoming a tableau with Saelith at the center and everyone else proof of her courage.

Mara saw that and loved her for it.

Serathiel looked up as they approached. His face was blood-streaked from the torn crown. White roots trembled around his hands. He seemed old now, but not weak. Never weak. The danger in him had moved from certainty into ruin, and ruin could still want an audience.

"You come to judge," he said.

Saelith shook her head. "To answer."

Liora stepped forward first. "I followed your cleansing writ into Orrowen. I would have burned citizens because I trusted your fear more than their names."

"I carried that fear for you," Serathiel said.

"No," Liora said, voice breaking. "You taught me to carry it and call the weight holiness."

The chamber burned blue.

Aneth of White Orchard lifted her translucent hands. "I silenced the dead and called it healing. Your doctrine praised me. Your doctrine also hid the names I smuggled back. It wanted my obedience and my goodness, but not my contradiction."

Another blue flare.

The older standard-bearer planted the upside-down banner. "I entered children as unclean. I ask correction."

Serathiel closed his eyes.

"Enough," he whispered.

"No," Saelith said, and her voice was almost gentle. "That is the word you took from others."

The roots around his hands loosened.

The Choir singer behind him hissed.

Serathiel looked toward the dragon-moon eye, then back to Saelith. "If I stand down, what remains of Lumenorath?"

"People," she said.

"People are not enough to hold against old grief."

"No," she said. "But neither was your law."

That sentence did not burn blue. It burned gold and red and Orrowen blue and Khar Veyl violet and goblin road green and troll river-black, because it was not merely true. It was witnessed.

The final roots fell from Serathiel's hands.

He removed the white-root crown.

When he placed it on the platform, the crown tried to crawl back to him. Saelith stepped on it.

Kesh made a strangled noise of appreciation.

"Do not," Tavi said, without opening her eyes.

"I said nothing."

"You radiated commentary."

The crown stopped moving under Saelith's boot.

Serathiel stared at it. Without the crown's living light, the wound it left at his brow looked raw and human. Silver blood ran down the bridge of his nose. He did not wipe it away.

"I stand down," he said again, but quieter, as if the first time had been spoken to the chamber and the second to the part of himself that had never believed it possible.

The Pale Bough bridge answered.

White-root lanterns across the army above went out one by one.

Not all. Some remained white, defiant or simply afraid. But enough went dark that the army ceased being a single instrument. Enough burned red-gold that soldiers began looking at one another instead of the saint-general. Enough lowered their weapons that the Khar Veyl line, seeing an enemy become people badly, had to decide whether to keep performing war alone.

Vaura made that decision before her hardliners could.

"Weapons down under bridge law," she ordered.

The blade-scholar, freed at last from Kesh's temporary noncombatant tag by sheer volume of offended dignity, shouted, "The Seat has no authority to surrender the under-realm to dead disorder!"

Velra hit him with a pump wrench.

It was not a killing blow. It was, however, persuasive.

Vaura looked at the unconscious blade-scholar, then at Velra.

"That was not authorized."

Velra lifted her chin. "Enter it."

Vaura paused.

"Entered as necessary interruption."

Sava stamped the air from across the chamber.

ACCEPTED.

Kesh wiped his eyes. "This is the most beautiful government I have ever seen."

"It is a mess," Caldus said.

"I said what I said."

The holy war ended in no grand cheer.

It ended in ragged commands, weapons lowered reluctantly, medics crossing with shaking hands, Orrowen clerks establishing complaint tables, and three separate factions arguing over whether suspended hostilities required two stamps or six. It ended with Serathiel crownless under guard and Vaura forced to speak standing recognition in front of her own hardliners. It ended with Saelith sitting on the floor because her legs stopped agreeing with ideology and muscle at the same time.

Mara sat beside her.

For a moment they said nothing.

Then Saelith asked, "Is it wrong that I am grieving him?"

Mara looked at Serathiel. He sat very still beneath the upside-down banner, alive because those he had harmed had not yet decided what justice required. He had wanted peace. He had wanted it sincerely enough to destroy people for refusing the shape of it.

"No," Mara said. "But don't let grief turn him back into only what he gave you."

Saelith nodded, crying silently.

"Don't let anger turn him into only what he took, either," Mara added, surprising herself.

Saelith leaned her shoulder against Mara's. "That is much harder."

"Yes."

The dragon-moon chains groaned.

The chamber's brief, bruised stillness ended.

Below, the eye opened further.

The Choir singer who had stood behind Serathiel stepped away from him. Her face had changed. Without Serathiel's grief to borrow, her peace looked less kind. More ancient.

"You stopped a war," she said to Mara. "You broke command. You entered standing. You made each side answerable."

Mara rose slowly.

The singer smiled with Vorrakai's mouth.

"Now answer this."

The dragon-moon opened one eye.
""",
    31: r"""The eye did not simply look.

It remembered at them.

Mara saw the chamber as the dragon-moon remembered it: not stone and bridge and platform, but pressure, bindings, cinder-pain, the tiny bright panic of nations crawling over a dead body and calling their fear civilization. She saw the first chain laid with prayers. The second with law. The third with engineering. The fourth with mercy. The fifth with profit. The sixth with hunger. The seventh with the exhausted agreement that if everyone was guilty, no one would have to stop.

Then she saw the dragon whose body had become the moon.

Not Vorrakai. Not entirely. A lesser dragon by age, perhaps, though lesser meant only that mountains might have survived her landing. Her name struck Mara as weather: Othrava, Deep-Wing, Keeper of Winter Rivers, Mother of Three Storms. She had died before the burial. Her body had been used because it was vast, because the cinder memory in her bones could hold a piece of Vorrakai's dream, because the living had already learned to speak of dead dragons as material.

Mara fell to her knees.

Not in worship.

In apology so large her body could not keep standing around it.

The eye turned toward her.

For a moment, Mara felt Othrava's memory beneath Vorrakai's grief: not words, not forgiveness, but the sensation of cold wind over scales, hatchlings tucked under a wing, river ice cracking in spring. A life. A life so enormous that nations had built metaphors around its corpse rather than admit they were using a mother as a lock.

Mara pressed both hands to the platform.

"Othrava," she said.

The chamber shook.

Every dragon-scale bridge lit.

Vorrakai's voice sharpened, not in anger. In attention.

You hear too much for something so young.

"Not enough," Mara whispered.

No. Never enough.

The eye showed her more.

Across Vael Taryn, cinders woke with Othrava's name inside them. In Ashgate, old furnace cinders remembered river ice though no worker there had seen such water. In Lumenorath, white-root orchards trembled under a winter wind that did not belong to their climate. In Khar Veyl, sealed pools froze around archive shelves. In goblin tunnels, road beads clicked like hail. At troll bridges, rivers rose with snowmelt memory. Gnome engines locked because their cinder cores briefly refused to be only heat.

The world learned it had been built on a person.

Then, because the world was still itself, people began shouting.

Vaura ordered evacuation from the lower causeways before the bridge chains snapped. Sava countermanded three of her directions because Orrowen civic stairs had priority under self-standing. Tavi, barely upright between two gnome ghosts, insisted that the eastern chain would hold if everyone stopped "pulling on the emotionally significant load-bearing murder cable." Caldus got Serathiel moving when the former saint-general froze under the eye. Saelith gathered the corrected Pale Bough soldiers and sent them to carry wounded, not banners. Kesh opened route after route until blood ran from his nose and the coin-moth map on his arm lit to the elbow.

Mara stayed on her knees.

Not because she could not move.

Because the eye had not finished asking.

What will you do with the name? Vorrakai asked.

The question chilled her more than accusation.

A name could become witness. It could also become a handle. Every faction in the chamber would want Othrava now. Lumenorath could mourn her into sainted purity. Khar Veyl could classify her as primary seal body. Gnome guilds could model the cinder response. Human kings could hunt echoes of winter-river cinder. The Choir could use her as proof that the living only ever found new ways to use the dead.

Mara wanted to say she would protect it.

That was too close to keeping it.

She wanted to say she would release it.

That was too close to deciding what release meant.

She remembered Sava's first lesson in the courthouse: do not choose the door that accepts the sentence. She remembered Saelith refusing to be another knife. Tavi refusing to become the acceptable failure rate. Kesh refusing to close roads by paying with ownership. Brakka refusing to let a bridge become a cage.

"We enter it," Mara said.

Vorrakai's attention deepened.

"Not as weapon. Not as lock. Not as saint. Othrava, Deep-Wing, Keeper of Winter Rivers, Mother of Three Storms. Dragon. Person. Used without consent. Witness pending her own answer if answer remains possible."

Sava heard and began writing before Mara finished.

Othel wept ink.

The chamber burned blue.

True.

The eye closed halfway.

Vorrakai's grief did not lessen, but it changed direction. For the first time, Mara felt not an offer, not persuasion, but regard. She had not defeated the first dragon. She had not even truly argued with it. She had done something more dangerous in the long shape of things.

She had refused to let grief be simple.

The chamber chains stopped snapping.

Some held.

Some did not.

The western bridge collapsed into pale light, taking three empty hymn wagons with it. The gnome bridge cracked, and Tavi screamed at the ghosts until they stabilized it with their own measuring rods. The human bridge shed ash tags like black snow. Each tag that fell became a name pending review instead of fuel. The dragon bridge remained broken and waiting.

Brakka rose under the central maul, shaking from crown to heel. "Leave now."

"Can the chamber hold?" Caldus asked.

"No."

Everyone looked at her.

Brakka blinked slowly. "Also yes. Different question. Leave."

"I understand troll engineering less every day," Kesh said.

"Good."

They left badly.

That was the only honest way left to do anything. Wounded went first because Caldus shouted until people obeyed him and then apologized to bridge law afterward. Orrowen citizens carried their own rolls. Lumenorath soldiers carried Khar Veyl wounded because Saelith assigned them by name and none dared argue after the eye. Khar Veyl wardens carried dead lanterns that had chosen transport. Gnome ghosts carried Tavi's tools because she threatened to haunt them in advance. Kesh ran road-lines through collapsing stairs and cursed every heroic story that had ever implied exits were less important than entrances.

Mara walked last until Brakka picked her up by the back of her coat and set her ahead of Sava.

"No," Mara protested.

"Bridge decides order."

"I can walk."

"Then walk there."

Mara walked there.

Behind them, the dragon-moon chamber settled into a new shape. Not sealed as it had been. Not open. The eye remained a slit under the world, watching through chains that had become witness instead of only prison. Othrava's name burned over the central platform in blue fire. Vorrakai's dream moved behind it, vast and patient.

Soon, the first dragon had said without saying.

Not today.

That was what they had won.

Mara did not despise the smallness of it.

Back in Orrowen's upper battlefield, dawn did not come because dawn belonged to the surface. Instead, the city made its own morning. Bone lanterns brightened by district. Canal bells rang. Market awnings opened, some for the first time in centuries. The dry riverbed filled with a thin line of ghost-water, enough to reflect faces without swallowing them. Citizens gathered in arguments that sounded almost festive if one ignored the blood, ash, broken roots, and occasional shouted legal threat.

The first assembly of Orrowen standing was held on the battlefield where two armies had almost ended them.

Sava presided because no one else dared take the central desk from her. Edrin recorded. Selli sat on the desk eating something that may or may not have been a snack recognized by civic law. Vaura entered Khar Veyl's recognition under protest, then crossed out under protest herself and replaced it with under witness. Liora entered Pale Bough corrected recognition. Serathiel, under guard, entered his name and former office. When asked standing, he said, "Contested." Sava looked at Saelith. Saelith nodded once.

Contested was entered.

That was not mercy.

It was a beginning honest enough not to flatter itself.

Mara watched from the edge of the assembly with her company around her in various degrees of collapse.

Caldus had finally allowed a medic to stitch his arm and looked betrayed by the concept of thread. Tavi slept sitting against Brakka's knee, one hand locked around the root-hound eye. Brakka slept sitting up, or perhaps meditated in a way that resembled a small landslide. Kesh had acquired a clerk, two new debt annotations, and a plate of food he claimed had followed him. Ilyr leaned against Maelin, who pretended not to support him while supporting him entirely. Saelith stood beside Mara, silent.

"Book Two ends here," Kesh said suddenly.

Everyone looked at him.

He blinked. "What? It has the feeling."

"What is Book Two?" Tavi mumbled without opening her eyes.

"A metaphorical unit of suffering."

"Then yes."

Mara laughed before she could stop herself.

It moved through the company, soft and disbelieving. Even Caldus smiled. Even Saelith. Even Ilyr, though it made him cough. The laughter did not erase anything. That was why it mattered.

Saelith looked over the assembly. "The war is stopped."

"Suspended," Caldus said.

"Corrected into difficulty," Tavi muttered.

"Still stopped," Mara said.

She let herself feel that much.

The war that had chased them from Lumenorath through Khar Veyl into Orrowen had stopped. The dead were not saved into simplicity, but they stood as witnesses. Serathiel had fallen. Vaura had yielded sole claim. Tavi had killed the engine. Ilyr had opened the record. Saelith had broken the beautiful law. Brakka had made a battlefield into a bridge. Kesh had kept roads open. Caldus had held lines he did not own. Mara had not become a saint, weapon, or crown.

She had become someone her friends could correct.

For now, that was the only kind of hero she trusted.

Then the cinder at her hip pulsed.

Every conversation in the assembly stopped.

The pulse came again.

Not from the chamber below alone. From everywhere. From Orrowen ghost-lamps, Khar Veyl seals, Lumenorath roots, Ashgate ash, road beads, bridge stones, gnome tools, crown jewels, hearth embers, grave dust. Every cinder in Vael Taryn had heard Othrava's name. Every cinder had heard Vorrakai's greeting. Every cinder now answered in a rhythm older than language.

Mara gripped the balcony rail.

Far below, the dragon-moon's eye looked through the world.

Vorrakai spoke, not to Mara alone this time, but to every person who carried dead dragon memory without knowing the dead had been listening.

I remember you.

The words passed outward.

On the surface, kings would wake. Priests would deny. Engineers would measure. Children would hear names in hearthfire. Graves would glow. Dragons living in far mountains would turn their heads toward Vael Taryn and wonder who had spoken a buried name loudly enough to trouble sleep.

Mara's company felt it too.

No one asked what came next.

They knew the shape if not the road.

Book Three had opened its eye.

Mara stood in the city of the dead, surrounded by the living, the wounded, the guilty, the corrected, the impossible people she loved, and listened as the world answered back.

Across Vael Taryn, every cinder woke.
""",
}


MORE_DEEPENING: dict[int, str] = {
    28: r"""The gnome ghosts did not leave when the engine died.

That surprised Tavi, though she did not say so in any vulnerable arrangement of words. They stood around the dead command core with their measuring rods lowered, uncertain what to do with themselves now that objection had finally become action. One of them, the ghost who could not remember her name, touched the opened cradle with two translucent fingers.

"I helped build the bypass," she said.

Tavi pushed herself onto one elbow. "Yes."

"I was told the dead civic rolls would panic if left unregulated."

"They did panic."

"Then I was right?"

Tavi stared at her. The chamber roared with names. Sava shouted for more ink. Serathiel's first pale root was beginning to coil at the edge of the Lumenorath bridge. The dragon-moon eye twitched below them. It was not, perhaps, an ideal hour for a lecture on ethical engineering. That made it exactly the hour.

"You were observant," Tavi said. "Not right."

The ghost flinched.

Tavi's voice softened without becoming gentle. "Panic is data. It is not permission. If a bridge shakes, you do not solve it by nailing everyone's feet to the planks."

The ghost looked at Brakka.

Brakka, bleeding vow-light through both arms, grunted approval. "Bad bridge."

"There," Tavi said. "Peer reviewed."

The ghost's outline flickered. "My name was Pella."

The chamber burned blue.

True.

Pella looked startled by her own existence.

Tavi's eyes filled, and she immediately disguised it as fury. "Good. Pella, your first task as a person remembered by name is to keep that secondary gear housing from eating the witness table."

"Yes," Pella said, and ran.

Two other gnome ghosts followed her. Not because a guild ordered them. Because a woman who had refused the command engine had given them work that did not require obedience as proof of worth.

Mara saw it and understood another piece of Tavi: the reason she loved tools was not that tools obeyed. It was that a good tool made a hand more itself. The command engine had been the opposite. It made persons into handles for fear.

Tavi caught Mara looking. "If you say that with feelings, I will deny all of it."

"I did not say anything."

"Your face is editorial."

"So is yours."

"Mine has earned credentials."

Mara smiled despite the trembling in her legs.

The moment helped. Small warmth could not defeat the dragon-moon, but it reminded Mara why the world did not deserve stillness. It contained Tavi, half-burned and arguing with named ghosts. It contained Kesh loudly misunderstanding decency. It contained Sava weaponizing forms. It contained Brakka's impossible patience, Caldus's practical courage, Saelith's corrected mercy, and all the dead citizens currently objecting to being made beautiful before being heard.

No wonder Vorrakai wanted to end choice.

Choice was unbearably noisy.

It was also the only sound in the chamber that had not yet become a chain.""",
    29: r"""The living began to enter witness after the dead, which embarrassed them.

It should have. That was Sava's opinion, and Sava's opinion had acquired the force of a weather system. She set a second series of tables near the witness rolls and labeled them LIVING CULPABILITY, LIVING CORRECTION, LIVING CONFUSION, and LIVING PEOPLE WHO INSIST THEY ARE ONLY HERE TO HELP BUT HAVE NOT YET STATED A NAME.

The last table filled fastest.

Kesh laughed until Sava pointed at him. Then he discovered urgent road work elsewhere.

Lumenorath officers came first in clumps, because courage often needed company when it had been trained to salute. Some tried to confess grandly. Sava rejected grand phrasing. "State the act. Spare us your soul's weather unless directly relevant." A captain who had intended to deliver a moving speech about doctrine instead entered three names he had called unclean on the march down. He looked smaller afterward. Also steadier.

Khar Veyl wardens came with more arguments. They wanted categories: necessary delay, sealed for protection, unlawful only under revised standing. Maelin stood at their table with a torn sleeve and expression like a drawn knife. "If your explanation takes longer than the name you harmed, begin again."

Vaura listened.

Once, she corrected a warden who tried to say retained subject.

"Person retained," Vaura said.

Maelin's pen stopped.

Mother and daughter looked at each other across the table. Nothing healed. Nothing forgave. But a phrase changed in public, and sometimes language was the first stone removed from a prison wall.

On the human bridge, Ashgate's pending tags had gathered into a little storm around Mara. They wanted entries too. Not all today; no one could do all today. But enough. Joryn's boot nail. Kell's washcloth. A tally stick with four notches cut by a child whose name Mara did not know yet. Human guilt had been easy for elven courts to use as proof that humans were crude consumers of cinder. The tags argued otherwise. Humans had been users, yes. Also used. Also thieves. Also caretakers. Also cowards. Also hungry.

Mara wrote the first human entry herself.

Joryn Vale, Ashgate foreman by appointment, protector by choice, complicit in furnace quotas, resistor of child vent assignments, dead before correction.

Her hand shook on complicit.

Caldus stood beside her. "Do you want me to write?"

"No."

He nodded and did not turn her refusal into distance.

Kell's entry came next. Then a dozen she did not know. Mara wrote unknown where needed and did not let the blank become empty.

By the time Serathiel's final hymn rose, the chamber held more than dead witness. It held the living beginning the uglier work of remaining answerable after the awe left.

That, perhaps, was why the hymn had to strike when it did.

If it waited longer, there would be too many named people to make peaceful at once.""",
    30: r"""After Serathiel stood down, the people who had needed him did not know where to put their hands.

That was the first visible consequence. Not theology. Hands. Soldiers who had held hymn staves since childhood lowered them and found their fingers empty. Healers trained to touch white root before touching skin looked at wounded enemies and hesitated over the old order of operations. Officers who had taken pride in perfect formation stood in imperfect clusters around a crownless man and realized their lines had been doing some of their thinking for them.

Saelith saw it and went to work.

She did not make a speech. She took the nearest healer's hands and placed them on a Khar Veyl warden's bleeding shoulder. "Ask his name."

The healer blinked. "What?"

"Ask his name before the wound."

"But he is -"

"Ask."

The healer looked at the warden. The warden looked as if he would rather bleed out than participate in a corrective intimacy exercise, but Velra stood behind him with her wrench, so he said, "Orren Veyt."

The healer repeated it, then began the work.

All along the Lumenorath bridge, corrected Pale Bough soldiers did the same. Badly at first. Too formal. Too apologetic. Too eager to be forgiven. Saelith corrected them each time, not because she had become their new saint, but because she recognized the old mistakes in their hands.

"Do not ask the wound to absolve you."

"Do not make his pain educational before it is treated."

"Do not call her brave because you need her not to be angry."

"Say the name again."

Mara watched and thought that this, more than Serathiel's crown on the floor, was his fall: the people he had shaped learning practices that did not require him at the center.

Serathiel watched too.

His face was unreadable, but his hands shook in his lap.

Sava assigned two Orrowen citizens and one corrected Pale Bough officer to guard him. Not as insult. As precision. "Those harmed by a doctrine should not be left alone with the man who carried it," she said. "Those who followed him should not be spared seeing him as a man."

Serathiel did not object.

That frightened Mara a little. She trusted remorse less when it arrived too clean. But then Serathiel looked at Saelith correcting a healer's hands and flinched, not from accusation, but from irrelevance. That flinch was ugly enough to be honest.

Vaura saw Mara watching him.

"He may yet become martyr," the dark-elf ruler said.

"So may you."

Vaura's mouth curved without warmth. "I intend to be too inconvenient."

"Good."

"That was not praise I expected from you."

"It was not praise."

"Better."

For a moment they stood side by side, neither allied nor opposed cleanly enough for comfort. Below them, Serathiel's crown lay under a sealed glass bowl because Tavi had shouted that leaving active ideological rootware loose on a battlefield was "how we get recurring villains."

Mara had not understood every word.

She had understood enough.

The crown scratched faintly against the glass, still trying to find a head.

No one gave it one.""",
    31: r"""Before they left Orrowen's battlefield, the company made one private circle.

It was Tavi's idea, which meant she introduced it by saying, "Everyone is being unbearably historic and I require a smaller meeting with fewer banners." She was pale enough that Caldus tried to insist she lie down. She threatened to repair his sling into a decorative restraint. He yielded with dignity he had not earned.

They gathered under a broken bridge arch: Mara, Saelith, Caldus, Tavi, Kesh, Brakka, Ilyr, Maelin. Edrin and Sava stood just beyond, close enough to be included and far enough to let the living think they had privacy. The city murmured around them. Above, the suspended armies negotiated corridors. Below, the dragon-moon watched with one slit eye. Everywhere, the world had become too large.

Kesh produced a flask.

Caldus looked at it. "Where did you get that?"

"From a man who no longer needed it because he had discovered accountability."

"You stole it."

"From accountability."

Tavi took it first. She sniffed. "This could strip varnish."

"A gnomish compliment."

She drank, coughed, and passed it to Brakka, who drank as if the liquid had merely asked permission to become part of a larger geological process. The flask went around. Mara took the smallest sip and felt it burn all the way down.

No one toasted victory.

At last Ilyr said, "I do not know where to go."

Maelin, beside him, looked at the city where her house's authority had cracked open. "Neither do I."

"I thought confession would produce direction."

"That was optimistic."

Kesh snorted. "Confession produces paperwork, enemies, and occasional dramatic lighting."

Saelith held the flask without drinking. "I cannot go back to Lumenorath as I was."

Tavi leaned against the bridge stone. "Excellent, because you were gloomy and over-regulated."

"I may not be welcome as I am."

Mara looked at her. "Then we build somewhere the corrected can stand while welcome catches up."

The words surprised her. They surprised everyone else too.

Brakka nodded first. "Bridge camp."

"That sounds temporary," Caldus said.

"All bridges temporary while river moves."

Kesh lifted a finger. "I support any organization named in a way that makes tax law nervous."

Mara felt heat rise in her face. "I did not mean founding something."

Tavi's eyes narrowed. "You absolutely meant founding something and are now frightened by the administrative implications."

"I have learned to fear administration."

"Healthy."

They laughed quietly.

But the idea did not vanish. A place, or a route, or a compact, not a kingdom, not an order, not another beautiful law. A bridge camp. A witness road. A way for people cracked out of old systems to stand together while refusing to become a new cage. It was too early. Too fragile. Probably impossible.

Mara kept it anyway.

Caldus looked at her, and she saw him understand the burden forming. "If you make this, they will look to you."

"Then you remind me to look back."

"I can do that."

"You already do."

He looked away first, which was satisfying.

Saelith finally drank from the flask and grimaced. "That is vile."

Kesh placed a hand over his heart. "It has been a day of many wounds."

Mara looked around the small circle. None of them were whole. None were clean. None knew the next road. Yet for the first time since Ashgate, the thought of being followed did not feel only like hands reaching for her neck. These people would argue. They would correct. They would refuse. They would need her and resent needing her and sometimes save her by being inconvenient.

That might be enough to begin.

Then the cinders pulsed, and the private circle became part of the larger world again.""",
}


FINAL_DEEPENING: dict[int, str] = {
    30: r"""The suspended war required witnesses of its own.

That was Brakka's insistence, and because Brakka was still glowing in several places no one wanted to tell her bridge law had become inconvenient. She made the first representatives from each force step onto the central crossing and state what they were not allowed to do before stating what they wanted. It slowed everything. It also kept three near-fights from becoming actual fights before the first corridor opened.

"Lumenorath will not cleanse Orrowen citizens without consent," Liora said, voice raw.

The chamber burned blue.

"Khar Veyl will not seal Orrowen roads under house authority," Velra said, staring directly at Vaura's wardens.

Blue.

Serathiel, still seated under guard, lifted his head. "Pale Bough command will not pass through my office."

The chamber hesitated.

Saelith's face tightened. "Not enough."

He closed his eyes. "Pale Bough command will not pass through my office, my name, my former rank, or any doctrine entered under my correction without review by those harmed."

Blue.

It cost him to say it. Good, Mara thought, and then wondered whether good was too simple a word for watching a dangerous man learn how not to be obeyed.

Vaura's turn came last.

She stood with the broken seal rod in both hands. "The Umbral Seat will not claim sole custody of the dragon-moon record."

Green fire, not blue.

Incomplete.

Maelin crossed her arms.

Vaura's jaw tightened. "The Umbral Seat will not claim custody of the dragon-moon record without Orrowen civic standing, mixed witness, and public correction of prior custody crimes."

Blue.

Maelin nodded once.

It was not forgiveness. The chamber, increasingly wise about these things, did not mistake it for any.""",
    31: r"""Later, Mara would remember the smell most clearly.

Not the moonlight from below, not the opened eye, not the sound of every cinder answering. The smell. Orrowen after battle smelled of wet stone, hot brass, white-root sap, ink, blood, lamp oil, river salt, and the sharp mineral scent of dragon-scale cooling after old magic had moved through it. It smelled like a place that had survived being made symbolic and now had to clean the floors.

That grounded her when awe threatened to take over.

People needed bandages. Witness rolls needed dry shelves. Children needed food. Serathiel needed guards who would neither worship nor murder him. Vaura needed opponents in the same room before she started calling control stewardship again. Tavi needed sleep and would not admit it. Kesh needed someone to notice the road-debt lines had reached his elbow. Saelith needed silence that was not abandonment. Caldus needed his stitches checked. Brakka needed everyone to stop stepping on weak sections of bridge while arguing about destiny.

Mara could not solve all of it.

For once, she did not try.

She assigned nothing at first. She asked. Who can carry? Who can write? Who knows this street? Who needs to sit before they fall? Who has not been heard? The questions moved faster than commands because people could answer from where they stood. Orrowen citizens answered in their own city. Lumenorath healers answered beside the wounded. Khar Veyl clerks answered beside the records. Goblin road signs answered by lighting the least-collapsed stairs.

That was how the first hour after the world changed passed.

Not in prophecy.

In logistics with names attached.

Only when the immediate bleeding slowed did Mara let herself look down toward the sealed chamber again. The eye remained open somewhere below, hidden by stone and distance and every old chain that still held. She could feel it the way one feels weather through healed bone.

Vorrakai had not lost.

Neither had they.

The truth was less clean and more frightening: the next war had become possible because they had won this one without surrendering the dead.

Mara touched the cinder cage at her hip. It no longer felt like a secret. It felt like a bell that had been rung once and would never be unheard.

"Mara," Saelith said.

She turned.

The company was waiting. Not for orders exactly. For the next honest sentence.

Mara breathed in Orrowen's ink-and-stone air.

"We rest," she said. "Then we find out who else heard that."

Across the city, every cinder pulsed again, as if answering: everyone.""",
}


WORD_FLOOR_DEEPENING: dict[int, str] = {
    31: r"""The answer did not come only as dread.

That was the strange mercy of the moment. When the cinders pulsed across Orrowen, some people cried out in fear, but others laughed because a hearth that had been cold for years whispered a grandmother's name. A Khar Veyl clerk dropped three ledgers when the ink began correcting old custody marks by itself. A Lumenorath medic stared at her white-root charm as it repeated Aurenne's forbidden line in a voice like leaves. One of the gnome ghosts began arguing with a wrench that had apparently remembered being forged from dragon-heated ore.

The world waking was terrible.

It was also crowded with persons.

Mara held both truths because the book had taught her what happened when anyone kept only one. Vorrakai would keep the suffering and call stillness mercy. Serathiel had kept mercy and called consent optional. Vaura had kept danger and called custody love. The command engine had kept outcomes and called persons load. Mara would not survive Book Three by choosing a cleaner blindness.

She looked at her friends.

"When I start sounding certain," she said, "be worried."

Kesh raised a hand immediately. "I have concerns retroactively."

"Entered," Sava said from below, without looking up.

Tavi groaned. "We have made accountability too portable."

Saelith smiled then, small and exhausted and real. Caldus leaned on the rail, watching the city instead of the horizon, which told Mara he had understood the assignment better than most knights in songs ever did. Brakka opened one eye from her bridge-sleep and said, "Good."

It was not comfort exactly.

It was better.

The world had answered with every cinder it owned, and the company answered back by remaining difficult.""",
}


FINAL_BUFFER: dict[int, str] = {
    31: r"""A little later, when Selli climbed onto the balcony carrying two rolls and a stolen pastry, she pointed at Mara with the pastry end.

"Are you in charge now?"

Every adult nearby made a different uncomfortable sound.

Mara crouched so she was eye level with the dead child. "No."

Selli narrowed her eyes. "Are you lying?"

"Not on purpose."

"That is what adults say before forms."

"Then enter it as pending."

Selli considered this, took a bite, and nodded. "Mara Venn, in charge pending objection."

"No," Mara said.

Sava called from the assembly floor, "Objection entered."

Kesh leaned over the rail. "This is the finest legal system in the world."

Mara looked at Selli, at the pastry crumbs, at the open rolls, at the city that had decided even a child could make authority answerable if the room agreed to hear her.

"How about this?" Mara said. "Mara Venn, traveling witness, subject to correction."

Selli wrote slowly.

The letters glowed blue.

True.

Mara felt the title settle lightly enough that she could still breathe.""",
}


LAST_BUFFER: dict[int, str] = {
    31: r"""That, more than the opened eye, frightened and steadied her. A title that could be corrected might not become a cage. A road that admitted objections might not become an army. A hero named lightly might remain a person long enough to do the next right thing badly and revise.""",
}


FLOOR_BUFFER: dict[int, str] = {
    31: r"""Below, Selli underlined the title twice and added, in smaller letters, MUST BRING SNACKS TO FUTURE APOCALYPSES. The chamber accepted only the first half as binding, which everyone agreed showed restraint.""",
}


FINAL_FLOOR_BUFFER: dict[int, str] = {
    31: r"""Mara did not argue the second half too strongly. Some laws were foolish, some were dangerous, and some were how frightened people admitted they intended to survive long enough to be hungry again.""",
}


TRUE_FINAL_BUFFER: dict[int, str] = {
    31: r"""That seemed worth entering, even if only in pencil, even at the edge of the world's next waking nightmare.""",
}


ACTUAL_FINAL_BUFFER: dict[int, str] = {
    31: r"""Sava stamped it anyway. Pencils, she said, were how permanent things learned humility. Clearly.""",
}


def replace_chapters(text: str) -> str:
    pattern = re.compile(r"(?m)^## Chapter (\d+): .*$")
    matches = list(pattern.finditer(text))
    by_no = {int(m.group(1)): m for m in matches}
    back_matter = re.search(r"(?m)^## Back Matter\b", text)
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
        if chapter_no in MORE_DEEPENING:
            replacement += "\n\n" + MORE_DEEPENING[chapter_no].strip()
        if chapter_no in FINAL_DEEPENING:
            replacement += "\n\n" + FINAL_DEEPENING[chapter_no].strip()
        if chapter_no in WORD_FLOOR_DEEPENING:
            replacement += "\n\n" + WORD_FLOOR_DEEPENING[chapter_no].strip()
        if chapter_no in FINAL_BUFFER:
            replacement += "\n\n" + FINAL_BUFFER[chapter_no].strip()
        if chapter_no in LAST_BUFFER:
            replacement += "\n\n" + LAST_BUFFER[chapter_no].strip()
        if chapter_no in FLOOR_BUFFER:
            replacement += "\n\n" + FLOOR_BUFFER[chapter_no].strip()
        if chapter_no in FINAL_FLOOR_BUFFER:
            replacement += "\n\n" + FINAL_FLOOR_BUFFER[chapter_no].strip()
        if chapter_no in TRUE_FINAL_BUFFER:
            replacement += "\n\n" + TRUE_FINAL_BUFFER[chapter_no].strip()
        if chapter_no in ACTUAL_FINAL_BUFFER:
            replacement += "\n\n" + ACTUAL_FINAL_BUFFER[chapter_no].strip()
        text = text[:start] + replacement + "\n\n" + text[end:].lstrip()
        matches = list(pattern.finditer(text))
        by_no = {int(m.group(1)): m for m in matches}
        back_matter = re.search(r"(?m)^## Back Matter\b", text)
    return text


def update_metadata(word_total: int) -> None:
    meta = METADATA.read_text(encoding="utf-8")
    meta = re.sub(r"produced_word_count: \d+", f"produced_word_count: {word_total}", meta)
    meta = re.sub(r"at_300_words_per_page: \d+", f"at_300_words_per_page: {round(word_total / 300)}", meta)
    meta = re.sub(r"at_275_words_per_page: \d+", f"at_275_words_per_page: {round(word_total / 275)}", meta)
    meta = re.sub(r"at_250_words_per_page: \d+", f"at_250_words_per_page: {round(word_total / 250)}", meta)
    meta = re.sub(
        r'current_form: ".*"',
        'current_form: "full-length draft zero with Book Two chapters 1-31 revised in pass 01; Book Two has a complete bespoke first revision"',
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
    print(f"Book Two chapters 28-31 revised. Word count: {total}")


if __name__ == "__main__":
    main()
