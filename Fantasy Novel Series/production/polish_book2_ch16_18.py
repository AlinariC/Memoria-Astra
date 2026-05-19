#!/usr/bin/env python3
"""Revision pass 01d for Book Two chapters 16-18.

Replaces the remaining Khar Veyl scaffold with bespoke scenes: Umbral Seat
politics under archive pressure, Kesh's worst bargain aftermath, and the
drowned archive payoff that forces the Blackroot Road descent.
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
    16: r"""## Chapter 16: The Umbral Seat

The archive stair did not go down so much as remember sinking.

Water climbed around Mara's thighs, then her ribs, yet her lungs still found air. The drowned archive did not obey the usual agreements between body and world. Each step passed through a different depth of memory. On one, she smelled wet bark and old ink. On the next, smoke from a dragon war no living witness had survived. On the next, soap from Kell Ashgate's washhouse, which made no sense until she understood that the archive was not showing only its own past. It was testing what each reader carried into it.

Do not keep what comforts you, the undead clerk had warned.

Mara kept moving.

Behind her, Saelith whispered a dawn law under her breath, then stopped and replaced it with the names she had chosen to carry: Liora, Oren, Edrin, Sava, Mara. Ilyr walked beside Maelin, close enough to catch her if she stumbled and far enough that the choice remained hers. Tavi held a lantern whose light kept diving toward the lower steps. Kesh had one hand on the wall and the other over the gray coin moth mark on his wrist, as if he could keep it from becoming permanent by refusing to look at it.

Brakka descended last. The stair widened for her only after she hit it with the butt of her maul and said, "Road. Remember manners."

The stair widened.

"I enjoy negotiating with infrastructure," Kesh said.

"Infrastructure listens better than councils," Brakka replied.

At the bottom, they entered a chamber shaped like an open eye.

Its walls curved upward into darkness. Shelves rose from the water in rings, each loaded with sealed records. Some were black tablets. Some were white root strips. Some were bone cylinders, brass plates, coral knots, jars containing spoken words, and scraps of dragon scale written on with ink that moved whenever Mara breathed. At the center stood nine stone seats, arranged in a crescent around a flooded lectern.

The Umbral Seat.

Not the council in flesh. Its older shape.

Maelin touched the nearest chair with two fingers. "When the living Seat argues above, this chamber remembers what the office was before families made it hereditary and judges made it comfortable."

"Comfortable?" Tavi looked around at the drowned stones, drifting pages, and archive crabs clicking along the shelves. "This room has the hospitality of a cold accusation."

"Exactly," Maelin said. "Improvement has been uneven."

The water around the seats brightened.

One by one, shadows appeared above them: Vaura, Thalan Vey, the blade-scholar who wanted first strike, two seal wardens, an archive judge, a canal magistrate, the broker with coin moth sleeves, and a woman in a plain worker's coat whom no one had introduced but whom every shadow made room for. The living council had been called into the drowned chamber through water, witness, and emergency law.

Vaura's shadow fixed on Maelin. "You reached the old Seat."

"Your guards are observant," Maelin said.

"My guards are furious."

"Multitasking."

The blade-scholar's shadow leaned forward. "White-root vanguard has crossed the western under-pass. We waste time with theatrics while Serathiel brings cleansing to our gates."

The lamps around the old seats shifted violet.

Threat sharpened into truth.

Mara stepped into the crescent before anyone could advise her not to. Water pulled at her coat. The cinder cage at her hip was cold as buried iron.

"We came for the shared ledger," she said.

"You came because you woke the lower seal with improper mixed witness," the blade-scholar snapped.

"Then you should be grateful improper things keep finding what proper people hid."

Kesh made a soft, proud sound. Tavi whispered, "That may be admissible as engineering."

Vaura raised one hand. "The old Seat hears. The question before Khar Veyl: strike Lumenorath before the cleansing host reaches the second pass, seal all under-roads and abandon surface witnesses, or delay action until the drowned archive yields the shared ledger."

"Delay is death," said the blade-scholar.

"Strike is confession by panic," Ilyr said.

Every shadow turned toward him.

He stood in knee-deep archive water with the gray scar across his palm visible. He had changed since the Half-Truth Knife, though Mara could not have named how. Less hidden, perhaps. Not safer. A man who had lost the protection of elegance.

"House Noct-Vey sold curated memory," he said. "The Seat allowed delays that served deniability. Lumenorath polished fear into doctrine. Harrowmere turned under-script into hooks. If Khar Veyl strikes now, it does not strike as guardian of truth. It strikes as a guilty court trying to choose the first accusation."

The old seats glowed blue.

No lie.

The coin-moth broker smiled from his shadow. "Beautiful. The exile wounds us and asks us not to raise shields."

"Raise shields," Caldus said. "Do not call a spear a shield because you are afraid."

The broker looked him over. "Human soldier without rank."

"Yes."

"Why should we weigh your distinction?"

Caldus's fingers tightened on his staff. "Because I kept the wrong oath long enough to know how often fear asks violence to wear duty."

Blue again.

The plain-coated woman in the ninth seat spoke for the first time. "Surface witness, what do the poor do while courts determine guilt?"

Mara turned. The woman's shadow was rougher than the others, edges blurred by water. Not noble. Not house-marked. Her hands looked like work.

"They pay first," Mara said.

"Always?"

"Often enough that always is how it feels."

The woman nodded. "I am Velra of the lower canals. My district will flood if the second pass is sealed. My children will be called acceptable loss by people who can spell acceptable in four old scripts. I vote no sealing until evacuation is counted."

The broker's expression tightened. "Lower canal seats advise. They do not vote."

The old Seat lamps flashed green.

Omission.

Velra smiled without warmth. "Old emergency law says every district holding a seal-pump votes when seal-pumps may be sacrificed."

Vaura looked at Thalan Vey.

The old judge's shadow sighed. "Technically correct."

Tavi brightened. "Technical correctness saves lives. I have been saying this for years with worse examples."

The debate unfolded like knife work.

The seal wardens wanted to close roads and preserve the dragon-moon seal at any cost. The blade-scholar wanted to strike Lumenorath's hymn wagons before they reached the pass. Velra wanted evacuation and water-rights protected before any heroic stupidity. The broker wanted under-market passage contracts recognized in advance of collapse. Vaura wanted time. Thalan wanted procedure. Maelin wanted the ledger opened before everyone used its absence as permission.

Mara listened until the voices became less like arguments and more like the cinder networks Tavi had shown her: lines of fear, obligation, guilt, power, and old design all pulling toward the same buried pulse.

Then the archive water rose.

Not far. An inch. Enough to cover the first line carved into the old seats.

Edrin Vale, standing behind Brakka, read it aloud.

"No seat stands above the drowned record."

The chamber stilled.

The water climbed another inch.

Sava Rennet touched the flooded lectern. "The dead request standing."

"Denied," said the blade-scholar immediately.

The old Seat went black.

Not blue, green, red, or violet.

Black.

The undead clerk from the receiving chamber surfaced behind the lectern as if the water had been keeping him folded. Archive crabs clung to his shoulders. Silver eyes opened.

"Denial conflicts with expanded standing pending drowning," he said.

Kesh leaned toward Tavi. "I am starting to admire this clerk with my whole surviving soul."

The clerk raised a stamp.

"Orrowen citizen Edrin Vale and unclassified named dead Sava Rennet request hearing on any action affecting dragon-moon, dead civic standing, seal maintenance, or archive destruction."

Thalan Vey's shadow murmured, "There is no precedent."

The clerk stamped the flooded lectern.

The sound knocked water from every shelf.

"Precedent drowned. New filing accepted."

For one breath, Mara could have laughed. Then the cinder at her hip went cold enough to hurt.

The flooded lectern opened.

A column of water rose from it, carrying pages in a slow spiral. Pale root strips, black under-script, Orrowen tax records, gnome seal diagrams, goblin route receipts, troll bridge marks, human ministerial extracts. A history no one people could confess because every people had found a way to touch it and then wash their hands elsewhere.

At the center of the spiral floated a strip of dragon scale written in two elven hands and one dead civic seal.

Maelin inhaled sharply.

"The preliminary covenant," she said.

The blade-scholar stepped toward the lectern. "Secure it."

"No," Mara said.

The word was too quiet for the chamber, but the cinder carried it. Not command. Witness.

"No one secures the first confession before it is read."

Vaura's shadow looked at the water, the dead, the lower-canal representative, the mixed company standing wet and exhausted in the old Seat. When she spoke, her voice had lost some of its armor.

"Khar Veyl delays first strike until the preliminary covenant is read under mixed witness."

The blade-scholar shouted. The broker objected. One seal warden cursed. Velra voted aye. Thalan, after visibly suffering through several legal collapses, said the old law permitted it. The dead witnesses added their standing. Vaura cast the deciding vote.

The old Seat lamps turned blue.

The strike was delayed.

One night.

Not peace. Not victory. A held breath in a room filling with water.

Mara took it.
""",
    17: r"""## Chapter 17: Kesh's Worst Bargain

Kesh hated the under-market because it understood him too quickly.

The lower reaches of Khar Veyl did not bother pretending they were civic virtue. They hung beneath the council terraces in stacked balconies, rope lifts, canal docks, and rooms carved behind rooms. Coin moths settled on contract ink. Echo merchants sold bottled last words at discount if the buyer did not ask whose. Smugglers mapped routes through closed passages on skin-thin paper that dissolved when lied over. Dark-elf brokers moved with the calm of people who knew every law had a service entrance.

It should have been Kesh's kind of place.

That was the problem.

They came there after the old Seat delayed first strike. One night of delay had to become movement before fear found a sharper tool. Vaura could not openly send Mara's company toward the Blackroot Road without giving hardliners a target. Maelin knew the drowned archive's preliminary covenant was only the first page; the rest waited deeper, along routes the official wardens claimed were flooded, sealed, or politically inconvenient. The under-market knew routes by less respectable names.

So Kesh led them down.

"Do not buy anything with your first name," he warned.

Tavi tucked both hands into her sleeves. "What about initials?"

"Only if you dislike your grandchildren."

"I have no grandchildren."

"You are in a market. Do not assume that remains true."

The first broker refused them. The second offered a map that would lead them safely to a room containing an invoice for the real map. The third tried to sell Saelith a remorse charm made from Pale Bough hymn-thread. Saelith looked at it until the seller apologized and put it away.

At last they reached a canal stall lit by three lamps, each a different color of distrust.

The broker waiting there wore a coat of layered gray contracts. Coin moths rested on his sleeves like living embroidery. Mara recognized him from the banquet.

"Veyr Tal," Kesh said.

"Kavik Kesh," said the broker. "Unpaid refusal. Fever-road debtor. Friend, apparently, which has done terrible things to your margins."

"I need Blackroot access."

"Many need impossible things. The trick is making them admit what they have already spent."

Caldus stayed near the rear, watching the bridges. Brakka stood by the canal, large enough that every passing boat reconsidered its route. Maelin leaned on a post with guards pretending she remained under their control. Ilyr watched Veyr Tal with naked dislike. Mara stood beside Kesh because not standing beside him would be worse.

The broker placed three objects on the counter.

A black key.

A folded route map.

A small glass bead full of green marsh light.

Kesh stopped breathing for one beat.

Mara saw it. So did Veyr Tal.

"Memory of home," the broker said. "Not stolen. Previously collateralized. You signed it away after the fever-road inquiry, then ran before collection."

Kesh's voice went light. Too light. "Everyone exaggerates youth."

"You were thirty-one."

"Goblin youth is emotionally complex."

The bead glowed. Inside it, Mara glimpsed a floating platform, mismatched bells, Rikka's red coat, a child laughing as Kesh lifted her over a puddle. Not a grand memory. That made it worse. A person could survive losing some grand things by calling them too heavy. Small warmth was harder to replace.

"Terms," Kesh said.

Veyr Tal touched the key. "Officially unrecorded passage from lower canals to Blackroot Road. Avoids hardliner checkpoints, seal wardens, and two Pale Bough root incursions. Includes one archive-safe boat, three silence papers, and temporary non-questions from my associates."

"Price."

"The collateral bead."

Kesh's face did not move.

Mara said, "No."

Both goblin and broker looked at her.

Kesh's smile returned in a thin, dangerous line. "This is a contract matter."

"It is a theft wearing your old signature."

"My old signature is legally enthusiastic."

Veyr Tal folded his hands. "The surface witness may pay instead."

Kesh's head snapped toward him. "No."

"She carries many valuable things. Route choices. Cinder resonance. Names that open rooms. A promise under her hand would cover passage."

The cinder at Mara's hip warmed.

Useful. Needed. Clear.

The old hunger rose so fast she almost missed it. Pay. Promise. Make herself the bridge so no one else lost something irreplaceable. The shape was familiar. Noble on the outside. A hook inside.

Kesh saw her understand.

"No," he said again, and this time the word was not a joke in any clothing. "You do not get to buy her usefulness from me."

Veyr Tal's coin moths lifted their wings.

"Then the bead."

Kesh looked at it.

For once, nobody interrupted.

He reached for the bead, picked it up, and held it against his palm. Green light seeped between his fingers. His face softened before he could stop it. Not with sentiment exactly, but recognition. A road under his feet. A bell tied to a child's wrist. Rikka calling him fool in a voice that still meant come back alive.

"I could pay it," he said.

Mara's throat tightened.

"I know," she said.

"I have paid worse."

"I know."

"Do not make this easy by being kind."

"I will try to be difficult."

He laughed once. It broke halfway.

Then he set the bead down.

"No."

Veyr Tal's smile sharpened. "You already tried refusal at banquet. The mark on your wrist says it did not settle accounts."

"I am not settling."

"Then what are you doing?"

Kesh drew his knife.

Caldus moved. Kesh raised his other hand, stopping him.

The goblin cut across the gray coin moth mark on his wrist. Blood welled black-red under the market lights. Coin moths rose from every stall nearby, wings whispering like paper money learning fear.

"Kesh of the Kavik Road files open default," he said.

The under-market went silent.

Veyr Tal's face changed. "Do not."

"I declare the fever-road debt unpaid, public, and attached to my road-name until carried through the three villages harmed by my sale. I reject memory seizure as settlement. I reject debt erasure as absolution. I place my name as surety for passage of mixed witnesses to Blackroot and for return passage of any civilian, dead or living, displaced by the lower-pass fighting."

The market's contract lamps turned white.

Not interest.

Alarm.

Veyr Tal hissed, "That is not a bargain. That is an infection."

Brakka looked pleased. "Standing spreads."

"You cannot pledge open passage through roads you do not own," the broker said.

Kesh smiled then, and this one had teeth enough to be true. "I am a goblin. We own the parts everyone else forgets they need."

Rikka's red-coated image flickered in the bead.

For a heartbeat, Mara thought the memory would shatter. Instead, the bead cracked and released a sound: mismatched bells ringing over marsh water.

The sound settled on Kesh's wrist, not erasing the gray mark, but changing it. The coin moth stain became a road line crossed by three bells. Open default. Unpaid, unhidden, active.

Veyr Tal stared as if Kesh had burned down a bank by telling the truth about interest rates.

"You have made your debt collectible by strangers," the broker said.

"Witnesses are rarely strangers for long."

"You have made your road-name unstable."

"It was getting boring."

"You have made yourself poor."

Kesh looked at Mara, then at the company, then at Maelin watching him with open delight, then at Brakka whose approval could have held up a bridge.

"Incorrect," he said.

Blue contract light flared.

The under-market accepted it.

Veyr Tal shoved the black key and folded map across the counter. "Take your passage before I regain professional composure."

Tavi snatched the map. "For the record, I am very moved and will express it later as criticism."

"Appreciated," Kesh said.

They left quickly because markets hated being forced into new ethics and tended to respond with fees, knives, or both. As they crossed the canal bridge, Mara walked beside Kesh.

"Do not thank me," he said.

"I was not going to."

"Good."

"I was going to say you are bleeding on the map."

He looked down. "That is practical affection. I accept."

Saelith bound his wrist only after he nodded. Brakka walked behind him like a wall that had decided debt could be defended. Caldus said nothing, which was sometimes the most respectful thing he knew how to do.

At the far end of the bridge, Siven waited with a small pack and an expression of criminal determination.

Vaura was not with him.

Maelin looked at the boy. "Absolutely not."

Siven lifted his chin. "The correction record requires a field clerk."

"The correction record requires you to grow up."

"I am doing that during the walk."

Kesh groaned. "No. No apprentices. Apprentices become invoices with feet."

Siven held up Mara's torn banner scrap. "You told me to record mixed witness. I cannot record it from a safe room while adults make history imprecisely."

Mara looked at the boy, then at Caldus. Caldus gave her the look of a man who knew arguments could be correct and still lose.

"You stay behind the second line," Mara said.

Siven's face lit.

"And if anyone tells you to run, you run."

"Define anyone."

"Me," Brakka said.

Siven swallowed. "Accepted."

Kesh muttered, "This is why I avoid inspiring children."

Mara glanced at his bleeding wrist, the altered debt mark, the black key in his hand.

"Too late," she said.

The under-market bells rang behind them, already changing the story of what had happened because every road wanted its version first. Kesh did not look back.

That was how Mara knew what it had cost.
""",
    18: r"""## Chapter 18: The Archive That Drowned

The drowned archive opened below the breath line.

Mara had expected to hold air in her lungs and fight panic. Instead, when the stair sank fully under black water, the archive taught her a different fear. She could breathe. The water entered no mouth, filled no throat, wet no page it did not choose to wet. It surrounded her with cold pressure and let her live by rules she had not agreed to.

Consent again.

Every realm had its favorite way of skipping it.

The stair ended in a corridor lined with shelves and slow-moving pages. Archive crabs walked along the walls, each carrying fragments of text under translucent shells. Root-fire burned in globes of trapped air. The floor was glass, and under the glass lay another archive, and under that another, descending through water and dark until Mara could no longer tell whether she looked down into storage or history's throat.

Tavi kept one hand on a brass pressure gauge that had given up numbers and begun drawing worried faces.

"I dislike a system that can make my tools poetic."

"Poetry is what tools do when frightened," Maelin said.

"Do not make that useful."

The undead clerk guided them without walking. He drifted ahead, robes moving like drowned ink. "Readers will pass through beneficial lies. Do not keep what comforts you."

"You said that already," Kesh said.

"Most warnings fail from under-repetition."

They reached the first lock.

It was a round door of black glass with no handle. In its surface, each of them saw a different reflection. Mara saw Kell Ashgate after victory, but cleaner: no hungry lines, no named dead unsure whether families would open doors, no Joryn staying behind because rebuilding needed him more than adventure did. In the reflection, the city simply loved her, and love required nothing complicated in return.

Her hand moved toward it.

Saelith caught her sleeve. "What do you see?"

"A lie I would like to rest in."

"Then do not rest yet."

Mara pulled back.

The lock opened.

Others struggled in turn. Saelith saw Lumenorath reformed without rupture, Serathiel smiling as if no war had been necessary. Ilyr saw Maelin freed and forgiving before he had to listen. Kesh saw Rikka telling him the debt had been a misunderstanding and the fever villages had recovered without names. Tavi saw a command engine dismantled before she ever imagined it. Caldus saw a king who had deserved him. Brakka saw a vow declared valid by those who had edited it. Edrin saw Orrowen accepting death with tidy civic grace.

Each had to speak the comfort aloud and refuse it.

By the time the first lock opened, everyone looked older.

The second lock was guarded by archive crabs.

Hundreds clung to the shelves around a circular chamber, their shell scraps rustling. At the center floated a ledger bound in scale, root, basalt thread, and civic bone. It was chained by four traditions: white root, black under-script, brass sealwork, and a road knot tied from something that looked like hair and stone fiber.

"Preliminary covenant's companion ledger," Maelin whispered.

"Can we take it?" Caldus asked.

The undead clerk turned his silver eyes on him. "No."

"Can we read it?"

"Insufficiently."

"Can anyone in this archive answer without becoming a weather pattern?"

"No."

Kesh pointed at the clerk. "I like him less underwater."

Tavi examined the brass sealwork. "The locks are meant to be opened together. Light, dark, craft, road, dead civic. But someone removed the living dragon witness."

Mara looked at the ledger.

The cinder cage at her hip had gone silent again.

Too silent.

The old dragon voice was not absent. It was waiting to be needed.

"What happens if we open it without dragon witness?" she asked.

"Distortion," Maelin said. "Each people reads itself as necessary and the others as regrettable."

"Convenient."

"Foundationally."

Saelith touched the white root chain. "I can answer for Lumenorath, but not with authority."

Ilyr touched the black under-script. "Authority has not improved us."

Tavi set both hands on the brass sealwork. "I answer for gnome craft under protest from every guild that will deny me."

Brakka took the road knot. "Road answers because feet drowning."

Edrin and Sava stood at the civic bone chain. "Orrowen answers," Edrin said, "because it paid and was erased."

All eyes turned to Mara.

Dragon witness.

She could open the cinder cage. Let the shard speak. Let Vorrakai's old grief pour through the lock and recognize its own kind. It would work. She knew it would. That was the danger.

The shard whispered without words: useful.

Mara took Niv's token from her pocket instead.

The scratched metal had no ancient authority. No dragon scale. No law. Just a work token carried by a girl who had once been counted as shift labor and later refused to become a better kind of tool.

She pressed it to the ledger.

"Human witness," the clerk said. "Not dragon."

"Good," Mara said. "Dragons were not the only ones buried under the story."

For one second, nothing happened.

Then the ledger opened.

The archive crabs clicked all at once. Pages loosened from shelves and circled the chamber. The water filled with images: ancient Elyri and Veyra standing together under a sky full of falling fire; gnome engineers building seal frames from dragon-scale math; troll road-keepers binding paths away from the burial site; goblin caravans carrying refugees no court wanted recorded; human kingdoms swearing not to mine certain cinders and breaking that oath within three generations; Orrowen civic treasuries paying labor, grain, and dead to a seal project whose purpose was hidden even from many who funded it.

At the center of everything lay the dragon-moon.

Not a moon in the sky. A vast cinder-body buried under Orrowen, curved horizon under the world, made from a piece of Vorrakai's dream after the first dragon refused to die cleanly. The ancient courts had not created the evil. They had contained grief. Then they had hidden containment so completely that hiding became another crime.

The ledger spoke in layered voices.

Division of memory prevents single command.

Division of peoples prevents unified claim.

Teach light that shadow hid guilt.

Teach shadow that light sought cleansing.

Teach the dead their levy was honored.

Do not teach them what it purchased.

Saelith made a sound like pain leaving bone.

Ilyr bowed his head.

Edrin's painted face cracked. Not metaphorically. A line opened through the old paint on his cheek.

"They taxed us for our own erasure," he said.

The ledger pages turned faster.

Then the third lock failed.

Not because of them.

Above, somewhere through stone and root, a white hymn struck the archive water. Serathiel's vanguard had reached a lower pass and sung into the seal lines. At the same moment, black under-script flashed from the opposite wall: Khar Veyl hardliners answering with severance blades. Two armies had not met yet, but their first spells were already touching the drowned record.

The water convulsed.

Salt memory tore through the chamber.

Everyone saw the dragon-moon differently. Saelith saw a wound to cleanse. Ilyr saw a danger to seal. Tavi saw a machine large enough to command every cinder if she only stopped being afraid. Kesh saw a road that could be sold once for enough to buy back every debt. Caldus saw an oath that would finally tell him where to stand. Brakka saw a bridge that could close forever and keep all feet safe by ending travel.

Mara saw a use for herself so vast it felt like love.

Open me, whispered grief older than nations. End the argument. Be needed. Be enough.

Her hand closed around Niv's token until the edge cut skin.

"No," she said.

The water did not hear.

"Names," she gasped.

Kesh was first, because sometimes cowards learned the shape of courage by running out of exits. "Rikka. Sella Brin. Liora. Pell. Haden. Fever villages I still owe and will not rename as lesson."

Saelith followed. "Oren. Liora. The bird whose wing was broken. The child I was before obedience."

Ilyr's voice shook. "Maelin. Arveth. Joryn chained because my house sold under-script. Every name hidden behind sequence."

Tavi gripped the brass seal. "Low Fen Gate. Every town saved by a tool. Every town harmed by its cousin. Makers who admit both."

Caldus: "Tesson Vair. The king I served too long. The prisoners I did not see in time."

Brakka: "Third Arch. Invalid vow. Road opens while feet still choosing."

Edrin and Sava spoke Orrowen names until the water filled with a civic roll older than the split.

Mara pressed the token harder.

"Joryn Venn. Dilla. Niv. Rella. Arveth. Halea Voss. Kell Ashgate. Mara Venn, not enough and not meant to be."

The ledger steadied.

The dragon-moon did not sleep again.

But it stopped asking her to be the answer.

For now.

The undead clerk slammed his stamp onto the open page.

Correction entered.

The sound cracked the chamber.

Water rushed upward. Archive crabs scattered, carrying scraps. Maelin seized the ledger's loosened companion pages. Tavi cut the brass chain with a tool she swore she had not been saving for this exact crime. Brakka lifted Edrin bodily after asking and receiving the fastest yes in recorded dead civic history. Caldus shoved Siven toward the stair, because of course the boy had followed them despite all practical orders and was now trying to keep his tablet dry with his own shirt.

The clerk pointed to a side passage opening in the collapsing shelves.

"Blackroot Road," he said.

"Is it safe?" Mara shouted.

The clerk looked almost offended. "It is a road."

Kesh coughed water that had never entered his lungs. "I cherish clarity."

They ran.

Behind them, the drowned archive folded around the open ledger, not destroyed, not saved, changed. Above, the first clash between white-root hymn and dark severance shook the lower passes. Ahead, the side passage sloped into fungal dark where bone-lit water moved under root and stone.

At the threshold, Saelith and Ilyr stopped together.

Not long. Long enough.

Their peoples had made the lie separately and together. Their faces held no absolution. Only inheritance.

Mara looked back once.

Through the rushing water, she saw the dragon-moon's horizon curve beneath the archive.

An eyelid moved.

Not open.

Not closed.

Listening.

Then the Blackroot Road swallowed them.
""",
}


EXPANSIONS: dict[int, str] = {
    16: r"""The one-night delay had conditions.

Khar Veyl never gave mercy without paperwork, and even emergency mercy arrived with teeth. Vaura's shadow named the terms while the old Seat water climbed around the carved bases of the chairs.

"Mixed witness party proceeds to companion ledger under archive supervision. Findings copied to the living Seat, lower canal districts, provisional dead standing, and sealed military command. No public release until evacuation routes are marked."

Velra of the lower canals lifted one wet hand. "Correction. No public release until evacuation routes are marked and opened."

Blue.

Vaura accepted the change with a tilt of her head.

The blade-scholar looked ready to draw on a shadow, which Mara suspected would be both impossible and illegal. "You will let surface panic read our oldest wound while Serathiel's host gathers?"

"No," Maelin said. "We will let surface panic stop pretending the wound is yours alone."

"You are retained."

Maelin smiled. "Less than yesterday."

That landed with a pleasure sharp enough to be dangerous. Ilyr looked at his sister as if every word she spoke was a coin he could not spend, only count.

Thalan Vey spoke from his old judge's chair. "If the ledger reveals mutual guilt, both armies may intensify. Purity narratives often grow louder when starved."

"Then feed them something indigestible," Tavi said.

Everyone looked at her.

She lifted both hands. "As a technical proposal. Bad doctrines are like bad engines. If you cannot dismantle them before they explode, you jam the gear that makes explosion efficient."

Kesh stared. "I understood some of that and resent the intimacy."

Tavi pointed toward the spiral of pages. "The ledger is not enough. We need copies that cannot be owned by one court, routes that cannot be cut by one army, and witnesses annoying enough that killing one creates ten more records."

Velra looked at the gnome with new respect. "Lower canals can move copies if passage is recognized."

The broker's coin moths fluttered. "Under-market can move anything if paid."

Kesh's wrist mark burned gray. "Or if debt opens."

The broker's shadow went very still.

Mara noticed. So did Brakka.

"There," Brakka said.

"There what?" Caldus asked.

"Next ugly bridge."

Kesh looked suddenly as if he wanted to be elsewhere, which in Kesh's case meant the truth had found his ankle.

Vaura's gaze settled on him. "The Kavik debtor may have relevance."

"I prefer decorative irrelevance," Kesh said.

"Denied."

The old Seat water accepted the denial as procedural and not cruel. Mara had begun to tell the difference. She did not enjoy the skill.

The undead clerk stamped three copies from the spiral and sent them skimming over the water to different shadows: Vaura, Velra, Thalan. A fourth copy drifted to Edrin. A fifth, unexpectedly, came to Mara. It sealed itself into a hard scale-thin strip when it touched her palm.

Preliminary covenant. Mixed witness copy. Do not preserve without correction.

The words itched.

"Why me?" she asked.

The clerk looked at her. "You ask that often."

"People keep handing me things."

"Then learn to hand them onward before they become you."

That was too useful to like.

The Seat shadows began to fade. Each returned to crisis above: troop signals, canal evacuations, hardliner containment, the terrible choreography of trying to delay war without admitting weakness to people who worshipped certainty.

Vaura lingered last.

"Mara Venn," she said.

"Yes?"

"My daughter lives partly because you made her inconvenient to kill."

Maelin, beside Mara, made a face. "I also contributed."

"You contributed by being difficult to kill from childhood."

"A family trait, inconsistently admired."

Vaura's shadow almost softened. Almost. "The Seat owes no gratitude while judgment is incomplete."

"I did not ask for gratitude," Mara said.

"Good. It is often a leash." Vaura looked at Ilyr. "Exile."

He stood straighter.

"If you return from the archive, you will stand second hearing."

"For restoration?"

"No. Restoration is for people pretending there was a clean place to return to. You will stand correction."

Ilyr bowed his head. "Accepted."

Maelin leaned toward Mara. "That is motherly warmth, below."

"I heard," Mara said.

Vaura vanished.

The old Seat chamber dimmed. Water fell from the pages into the lectern with sounds like small verdicts.

Kesh looked at the exit toward the under-market and sighed from the deepest part of his untrustworthy soul.

"I know where the next road is," he said.

"And?" Mara asked.

"And I was hoping to become unconscious before mentioning it."
""",
    17: r"""The Blackroot map was alive enough to object to handling.

It writhed on Tavi's crate after they reached the lower canal safe room, folding and unfolding its own corners, trying to hide the most useful routes under decorative lies. Veyr Tal had sold them passage, yes, but he had sold it like an under-market broker: technically complete, ethically carnivorous. The map showed six roads to Blackroot. Three led through hardliner checkpoints. One led through a Pale Bough root incursion. One led through a closed pumping district Velra had not yet evacuated. The last route kept vanishing whenever anyone honest looked at it.

"That one," Kesh said.

Maelin leaned over the table. "It disappears under honest attention?"

"Smuggler courtesy."

Tavi pulled goggles over her eyes. "I can make myself ethically blurry."

"You already do," Caldus said.

"And yet it hurts when you say it."

Kesh placed his bleeding wrist over the map. The open-default mark flared. The vanishing route steadied into a thin black line running from the drowned archive outlet through fungus cisterns, old gnome seal tunnels, and something labeled old battlefield seep, do not sing.

Saelith read the last part. "Why would anyone sing?"

Ilyr and Maelin answered together. "Fear."

Mara stared at the route. "Can civilians use it?"

"Not easily," Kesh said.

Brakka set both hands on the table until the map stopped twitching. "Question not easy. Question possible."

Kesh's mouth tightened. "Possible if the road clans accept open default. Possible if lower canals guide evacuees to the old cisterns. Possible if Khar Veyl does not arrest every smuggler on principle. Possible if Pale Bough scouts do not decide all movement below is infection. Possible if I survive several family conversations that will be louder than war."

"So possible," Tavi said.

"I liked you more when you exploded quietly."

Mara looked at the map, then at Kesh. "You do not have to make every debt useful immediately."

"I know."

"Do you?"

"No, but I am performing growth and hoping it sticks."

The safe room door opened before anyone could answer. Velra entered with two canal workers and Siven, who was supposed to be asleep under guard and instead looked freshly guilty.

"Lower canals will move civilians to the cistern routes," Velra said. "We need marks that Pale Bough and hardliner scouts cannot easily forge."

Brakka tore a strip from her sleeve and began marking it with road-law mud. "Marks need feet sworn, not pretty."

Saelith removed the last white thread from her old clasp scar and laid it beside Brakka's strip. "Use this only to warn of coercive hymns, not to bless passage."

Ilyr added a sliver of black witness paper. "This mark says record before command."

Tavi added a brass shaving. "This mark says if found, return to someone with tools and moral anxiety."

Kesh looked at them all, then at his wrist.

Mara said nothing.

He cut a thread from the cuff of his coat, green with old marsh dye. "This mark says road debt open. Passage first. Accounting later."

Siven wrote so fast his hand blurred.

"Do not make it sound noble," Kesh snapped.

The boy looked up. "How should I make it sound?"

Kesh opened his mouth, closed it, and looked offended by the question's competence.

"Expensive," he said.

Siven wrote that.

Velra gathered the marks. "If this works, thousands may move before the pass collapses."

"And if it fails?" Caldus asked.

Velra looked at the map. "Then at least the people making the decision will be wet, frightened, and nearby. That improves accountability."

Mara liked her.

The first explosion sounded above the safe room then.

Dust fell from the ceiling. The map curled around the Blackroot route like a startled leaf. Distant horns answered, Khar Veyl and Pale Bough both, so similar in urgency that for a moment no one could tell which fear belonged to whom.

Maelin took the companion ledger copies and tucked them into waterproof cases. "The armies have started arguing with architecture."

"We leave now," Caldus said.

"We always leave now," Kesh muttered. "I miss someday."

At the door, Mara caught his sleeve.

He glanced back, ready with some defense.

"You are not the road," she said.

The words surprised both of them.

Mara tried again. "You opened one. That is different."

Kesh's expression shifted, humor trying to cover an injury and failing. "You are dangerously close to thanking me."

"No. I am correcting the record."

He looked down at Siven's tablet, at the map, at his altered wrist mark.

"Fine," he said. "But make the correction expensive."

"Always."

They went out into the lower canal alarms together, carrying maps that did not want to be owned and debts that had finally stopped pretending to be paid.
""",
    18: r"""The Blackroot passage did not wait politely while the archive collapsed.

It opened like a throat behind the companion ledger chamber, swallowing water, pages, and people with equal disregard. The mixed witness party stumbled into a tunnel lit by green fungus and blue root-fire, while the archive roared behind them. Maelin had three waterproof cases under one arm and a knife in the other. Ilyr carried Sava Rennet after the named dead's leg stiffened in the cold. Brakka carried Edrin because Edrin had consented and because no one sane argued with Brakka carrying the dead through a flood.

Mara ran until the tunnel widened into a cistern.

There, the first evacuees were already arriving.

Velra's canal marks had worked faster than hope. Lower-canal families poured through side passages carrying packs, children, ledgers, cooking pots, sleeping mats, and the small furious items people saved when large things were impossible. A dark-elf boy carried a cage of glow beetles. A human woman carried two sleeping infants and a blade she clearly did not know how to use. Three goblin guides argued over which route had the least doom per mile. A pair of old Veyra men pushed a cart holding a water pump, because some people fled catastrophe by bringing plumbing with them.

Pale Bough hymn-light flickered through one side tunnel.

Khar Veyl severance-script flashed through another.

The war had reached the evacuation routes before anyone finished feeling clever.

"We need to split movement," Caldus said, already counting bodies, exits, chokepoints. "Noncombatants through the low cistern. Witness cases through Blackroot. Fighters hold side passages only until the last cart clears."

"Who made you commander?" a Veyra canal guard demanded.

Caldus looked tired. "No one. Please improve the plan if you can."

That worked better than rank.

The guard pointed to a narrow spillway. "Children through there. It meets the old mushroom road."

Brakka slammed her maul into the cistern floor. Road-law amber spread through the water. "Feet first. Arguments walk after."

Kesh climbed onto a pump housing and held up his marked wrist. "Open default! Passage first, accounting later! If you are carrying a person, record, child, elder, named dead, or emotionally significant cookware, move left. If you are carrying only pride, throw it at the nearest army and move left anyway."

People moved.

Mara stood in the center of it with water to her knees, cinder cold at her hip, ledger cases passing hand to hand, Saelith guiding wounded through without smoothing their fear, Tavi rigging a pump to spit steam across a side passage, Maelin shouting Khar Veyl directions like insults, Ilyr translating them into fewer insults, Siven writing while walking and nearly falling twice.

Then Serathiel's voice entered the cistern.

Not in person. Through root-hymn. It flowed along the Pale Bough light and filled the water with aching clarity.

Stand aside. We come to seal the wound.

From the opposite tunnel, the blade-scholar's severance-script answered in black fire.

Advance and be cut from memory.

The evacuees froze.

Two armies, still out of sight, had managed to make terrified civilians feel like trespassers in their own escape.

Mara wanted to scream.

Instead, she took the companion ledger copy from Maelin's case, held it over her head, and stepped onto Brakka's road-law mark.

"This road carries the people your histories spent," she said.

Her voice shook. The road did not care. It carried the words.

"Light court, dark court, dead city, road clan, craft guild, crown town. All of you touched the seal. All of you hid behind the part someone else did wrong. No one blocks this passage and calls it purity."

For one breath, both hymns faltered.

That was enough.

Tavi's pump screamed and blasted steam into the Pale Bough tunnel. Kesh dropped from the pump housing and cut a rope that sent three empty carts rolling into the severance-script passage. Caldus and the canal guard moved together to pull a fallen child from under the cart flow. Saelith sang her flawed counter-note, not against Serathiel exactly, but against the part of every command that tried to make fear kneel neatly. Ilyr and Maelin spoke under-script in alternating lines, not sealing the route, but labeling every evacuee as witness-in-transit.

The named dead began the Orrowen civic roll.

Names filled the cistern.

The Blackroot Road opened wider.

Not by miracle. By weight. So many feet needed it that the old road remembered purpose.

When the last child passed into the low cistern, the side tunnels broke.

White-root blades entered from one side. Dark hardliner masks from the other. They saw each other across the evacuation water and, for one dangerous second, forgot the civilians completely.

Mara felt the dragon-moon stir under the world.

Here, said the old grief. See? Choice becomes war. End it.

The cinder cage warmed.

She could have struck both sides.

She could have been useful enough to stop them all.

Brakka's hand closed around her shoulder.

"Road first," the troll said.

Mara exhaled.

"Road first."

They ran into Blackroot as the two armies collided behind them.

The tunnel swallowed light quickly. Fungal stars opened overhead, green and gold. Bone-lit water moved beside the path. The air smelled of mushrooms, salt, old battlefields, and something like prayer left too long in a closed room.

Behind them, Khar Veyl and Lumenorath began the war both had claimed to fear.

Ahead, Orrowen waited to decide whether the dead would be witnesses, citizens, or weapons.

Mara carried one ledger case against her chest and Niv's token cutting into her palm.

She was not enough to stop a war.

That hurt.

It also saved her from becoming the kind of answer that would.
""",
}


DEEPENING: dict[int, str] = {
    16: r"""The preliminary covenant did not read in order.

That was its first accusation. The pages rose from the lectern in fragments, each fragment written by a different hand, each hand insisting its part had been necessary. Mara watched the old Seat try to assemble a history that had been cut apart so thoroughly that even the pieces had learned to mistrust one another.

Saelith took the first white-root strip.

Her fingers shook before she touched it. Mara almost reached for her, then stopped. Witness, Edrin had reminded her, was not rescue if it stole the answer first.

Saelith read aloud.

"The Elyri conservators agree to hold surface memory of the burial in forms that reduce public panic and prevent unsanctioned pilgrimage to the lower wound."

The strip brightened and showed light-elf healers tending children with dragon-grief fever, villages where people had stopped sleeping, orchards burning because every fruit had begun singing one dead name. The first preservation had not been cruel. That was the blade in it. People had been frightened. People had been helped. Then help had grown roots into ownership.

Saelith's voice thinned. "Margin note: beauty makes fear bearable."

Veyanna would have loved that sentence. Serathiel might have written it over a hospital door.

Maelin handed Ilyr a black under-script plate.

He read without flinching, which told Mara exactly how much it cost. "The Veyra wardens agree to divide access to structural truth among houses sworn to secrecy, preventing any single court from leveraging the dragon-moon against the others."

The plate showed early Khar Veyl, less subterranean then, its halls crowded with refugees carrying burned books and sleeping children. Wardens sealed corridors not to hoard power, but to stop memory-plague from rolling through every frightened mind. Then the vision shifted by years, decades, generations. A sealed corridor became a family privilege. A family privilege became leverage. Leverage became sale.

Ilyr read the margin note. "What cannot be stolen must first be kept."

The old Seat lights went green, then blue, as if even the archive recognized a sentence turning slowly from caution into rot.

Tavi took the brass diagram next. She held it at arm's length like it might bite. "Gnome craft compact agrees to construct dampening frames, evacuation locks, and dispersal engines according to split specifications. Addendum: no single craft hall receives full pattern."

The diagram unfolded into a beautiful engine none of them understood entirely. It was not a weapon. Not at first. It redistributed pressure from the sleeping dragon-moon into harmless heat, light, and sealed motion. Then later hands copied pieces without warnings. Later guilds optimized outputs. Later ministers asked what else a dampening frame could dampen.

Tavi swallowed. "Margin note: if the whole pattern is dangerous, fragments may be safe."

"Were they?" Caldus asked.

Tavi's face twisted. "You have met our fragments."

Kesh received the road-knot record and looked immediately offended by destiny.

"Goblin road clans agree to carry displaced persons, sealed warnings, and unmarked burdens between courts without claiming knowledge of contents," he read. "Payment to be distributed by weight, danger, and discretion."

The vision smelled of rain, sweat, packed wagons, children hidden under tarps, sealed jars no driver was allowed to open. Goblin roads had saved lives. Goblin roads had also carried secrets for people who paid extra not to hear crying from the cargo.

Kesh did not need to read the margin. Mara saw it on his face.

He did anyway.

"A road survives by not asking every passenger why they run."

Brakka took the troll mark last. It was carved into a stone no larger than her palm. "Seven Arches agree to close three old roads and leave one under vow, for retreat, witness, and fools."

"Fools?" Tavi asked.

Brakka looked almost proud. "Ancestors knew complete plans dishonest."

The vision showed troll road-keepers standing before armies, refugees, dragons, and weather, refusing to close every path because no court knew the future well enough to own all exits. Then later toll kings narrowed the open road. Later clans argued over whose vow had authority. Later Brakka's own vow had been declared invalid because it made powerful travel inconvenient.

The margin note read: A bridge that never refuses becomes road for conquest. A bridge that always refuses becomes wall.

The old Seat chamber held the words.

Then Edrin lifted the Orrowen civic page.

The water went very cold.

"Orrowen Third, Fourth, and Moonward Districts agree to emergency levy of grain, stone, labor, civic dead, and unnamed prisoners for lower seal stabilization," he read. "Compensation guaranteed in perpetuity by elven conservators and under-wardens."

No one spoke.

The vision did not show grand courts. It showed carts. Storehouses emptying. Prison ledgers. Families signing because refusing a world-saving levy made them traitors before they understood the question. Dead citizens moved under civic seal, not enslaved, not free, used because memory anchored power and the dead remembered strongly. Orrowen had not merely paid. Orrowen had been made into part of the lock.

Sava Rennet touched the page with one dead finger. "Margin."

Edrin's voice cracked. "Teach the dead their levy was honored. Do not teach them what it purchased."

The old Seat went black again.

Not lie. Not omission.

Grief too large for color.

Mara felt Vorrakai move far below, an old attention turning toward fresh anger. The dragon grief did not create the rage in the chamber. It only offered shape.

Use it, the cold seemed to say. Name them guilty. Break the seal. Let every hidden dead hand rise.

Mara pressed Niv's token against her palm.

"No," she whispered.

Vaura's shadow heard. "No what?"

Mara looked at the council, the dead, the records, the companions carrying different inheritances of the same wound.

"No first answer," she said. "Not from me. Not from Khar Veyl. Not from Orrowen. We read before we punish. We move people before we prove ourselves righteous. We keep the road open before every court decides the other court's guilt makes civilians expendable."

The old Seat lights returned, dim and blue.

Velra of the lower canals cast her vote first for delay, evacuation, and mixed copying. Edrin cast the dead civic vote second. Brakka placed her road vote beside theirs without asking permission. One by one, enough shadows followed.

The blade-scholar did not.

"You delay until Serathiel's mercy reaches our children," he said.

Mara met his eyes. "You strike until your children become someone else's proof."

For a heartbeat, his face changed. Not enough. But something in the old Seat recorded the crack.

One night was granted.

One night to move civilians, copy a confession, find the deeper ledger, and stop two armies from turning truth into ammunition before breakfast.

Kesh looked at the vanishing shadows and then at the under-market exit.

"I repeat," he said. "Unconsciousness would have been a reasonable schedule."
""",
    17: r"""The fever-road debt followed Kesh into the canal safe room.

Not metaphorically. Khar Veyl disliked leaving guilt in the abstract. While the others marked evacuation strips and argued over routes, three small shadows detached from the map and stood on the table. Each was shaped like a village marker: a well, a bridge, a grain tower. Kesh saw them and stopped speaking mid-insult.

Mara saw his face and knew the names before he said them.

"The fever villages," she said.

He gave one sharp nod.

The first shadow marker spoke in a woman's voice. "Reedmere."

The second, a child's. "Tallow Ford."

The third, old and rough. "Neth-by-the-Salt."

Kesh sat down on the nearest crate. Not dramatically. More as if his knees had decided honesty required less height.

"Under-market collections are crueler than road-clan ones," he said.

"These are not collections," Maelin said, studying the shadows. "They are debt witnesses. Veyr Tal released them when Kesh filed open default."

"That sounds like collection with theater."

"Yes."

The markers turned toward Kesh.

No accusation came. That was worse.

He rubbed both hands over his face. The bandage around his wrist was already spotted through. "I sold a route to a flood boss who wanted to move workers around quarantine. I suspected fever. I priced suspicion below knowledge because knowledge would have obligated refusal. He paid in medicine. My caravan lived through marshlung that winter. Reedmere buried nineteen. Tallow Ford lost thirty-one. Neth-by-the-Salt stopped counting at forty because the clerk died."

No one softened the room.

Mara was grateful. She was also angry enough to want softness because softness would have made the anger easier to hold.

Kesh looked at the shadow markers. "I told myself the fever might have traveled anyway."

The map lamps flashed green.

"It might have," he said. "That is true and not enough."

Blue.

"I told myself medicine bought with dirty money still saves clean children."

Blue, but dim.

"I told myself survival excuses what apology cannot repair."

Red.

He flinched.

The child's shadow, Tallow Ford, stepped closer. "Open default requires carried record."

Kesh's laugh came out broken. "Of course it does."

"What does that mean?" Mara asked.

Veyr Tal had not followed them. He did not need to. His contract had teeth inside the map. The shadow of Reedmere answered, "Debtor carries names until delivered to each village or lawful descendant. If debtor dies, debt attaches to chosen road."

Brakka's eyes narrowed. "Dangerous vow."

"Yes," Kesh said. "That is why sane people settle with memory."

"But you did not," Saelith said.

"I am experimenting with stupidity."

Caldus crouched so he was level with Kesh and the table. "Do you choose the road?"

"Do not make this noble."

"I am making it precise."

Kesh stared at him, then at Mara, then at the three village shadows. "No."

The red lamp flashed.

He hissed. "Fine. Yes and no. I choose not to pass the debt to a road if I die. I choose to carry it myself as long as I am alive. If I die before delivery, the record goes to Rikka of the Kavik Road, who will curse me in seven dialects and do the work correctly."

The three markers brightened.

"Names," said Neth-by-the-Salt.

Kesh looked sick.

Mara understood suddenly. The debt was not a number. It was not even guilt. It was memory as cargo, and this cargo would not be light.

"You do not have to read them alone," she said.

He looked at her sharply. "Yes, I do."

The red lamp did not flash.

She nodded, accepting the correction.

Kesh unfolded the first shadow strip.

Names spilled across the table in green marsh light. He read until his voice gave. Then he drank water, swore at everyone for looking emotionally expensive, and read more. Reedmere. Tallow Ford. Neth-by-the-Salt. Children, boatwrights, fever nurses, a baker who had continued making bread with shaking hands, a ferryman who had moved sick neighbors without charging and died before anyone could pay him, three people listed only as unknown traveler.

At unknown traveler, Edrin lifted his head.

"Unknown is not empty," he said.

Kesh closed his eyes. "I know."

He read them as unknown traveler, witnessed under fever-road debt.

When the last name settled onto the map, the Blackroot route stopped trying to hide.

Not because the debt was paid.

Because the road had learned who was carrying it.

Siven wrote with silent fury, tears running down his face and ignored by everyone polite enough not to name them. Tavi pretended to adjust the pressure gauge. Caldus stared at the floor. Saelith kept one hand near Kesh's bandage, waiting for permission. Brakka stood by the door as if any enemy trying to interrupt this accounting would have to argue with stone first.

Mara listened.

That was all.

Sometimes all was heavy enough.

When Kesh finished, he looked at the three village markers. "I will carry them."

The markers bowed, not forgiving, not absolving. Acknowledging.

Then they folded into the open-default mark on his wrist.

Kesh swayed. Saelith stepped forward. He nodded once. She caught him before pride could do something medically stupid.

"If anyone calls that character growth," he said, "I will become worse out of spite."

Mara smiled because he needed one person to treat him as alive and not only guilty.

"Would not dream of it."

"Liar."

"Often. Not now."

The map opened the Blackroot route fully then, and the first evacuation bells began to ring above them.
""",
    18: r"""The first page they saved from the drowned archive tried to crawl back into the water.

Maelin pinned it to the tunnel wall with a knife and told it to develop civic responsibility. The page quivered, then flattened, revealing two columns of old script. Saelith read the pale column. Ilyr read the black. Edrin read the dead civic seal pressed below both.

"The dragon-moon was never meant to be permanent," Saelith said.

"The seal was a tourniquet," Ilyr said. "Not a cure."

Edrin touched the civic seal. "Orrowen was promised review every ninety-nine years."

No one spoke.

They all knew, by then, that no review had come.

Tavi leaned against the tunnel wall, dripping archive water from her sleeves. "So all the regulators, hymns, under-seals, toll-closures, memory laws, and corpse hooks are built on emergency measures that forgot to expire."

Maelin pulled the knife free. "Forgot is charitable."

"I was being polite to history."

"History abuses politeness."

Behind them, the archive kept collapsing in controlled sections. Controlled, the undead clerk had insisted as a shelf fell into black water and nearly took Kesh with it. In Khar Veyl, even disaster wanted classification. But some records were choosing the Blackroot Road, skittering after them as crabs, scraps, floating bark, and one very aggressive brass plate that attached itself to Tavi's pack.

"Stop that," Tavi told it.

The plate displayed a gnome maker's oath from the first seal project.

Tavi stopped walking.

Mara saw the change in her face. "Tavi?"

"This is signed by Quen-of-Deep-Spiral."

"Family?"

"Professional ancestor. Maybe blood. Gnomes prefer arguing craft lineage until everyone forgets birthdays."

The plate brightened, showing a gnome engineer standing before a vast curved darkness, goggles cracked, hands burned. His oath read: No engine built for emergency shall be copied for governance.

Tavi laughed once.

It was not happy.

"We broke that in every century."

The brass plate clicked against her pack as if agreeing with unnecessary enthusiasm.

"What will you do with it?" Caldus asked.

Tavi held the plate carefully. "Carry it until it becomes inconvenient enough to publish."

Kesh, pale from fever names and running, still managed, "A fine scholarly standard."

They moved again.

The Blackroot tunnel widened into a cavern of fungal columns. Their caps glowed in greens, golds, and ghostly white. Between them ran shallow streams over bones so old they had become part of the stone. Some bones were dragon-kin. Some were human-sized. Some belonged to creatures Mara did not have names for, and she was no longer grateful for ignorance.

The evacuees entered behind them in waves.

This was where the archive payoff stopped being a revelation and became work.

Mara expected people to clutch the new truth and understand the urgency. Instead, they asked for water, lost children, argued over carts, accused one another of cutting the line, refused to travel near the named dead, demanded proof that the route did not lead to a worse trap, and wept because they had left soup on a hearth that might never exist again.

Reality, she thought, was history with wet boots.

Caldus took one look and began building order from exhaustion. "Families by cart. Injured to the right. Anyone carrying records keeps them above water. Anyone carrying rumors gives them to Kesh so he can make them less efficient."

"I have become municipal equipment," Kesh said.

"Useful municipal equipment," Tavi said.

"Low blow."

Saelith moved among the wounded, asking permission with each touch. Some refused because she was light-elf. She accepted the refusal and found water, cloth, or someone else to help. That acceptance did more for the route than any speech. Ilyr and Maelin argued with Veyra evacuees who did not want to take instructions beside named dead. Brakka marked the fungal columns with road-law: pass living, pass dead, pass record, pass regret.

Siven stood on a stone and read the archive correction aloud to each group entering Blackroot.

Not all of it. No one had time. He read the line that mattered for feet.

"Emergency measures expired unreviewed. Passage remains open under mixed witness."

The words were too large for a frightened crowd. Still, they did something. They made the route feel less like smuggling and more like a door history had owed them.

Mara helped a child find a grandmother, carried a ledger case until her shoulder burned, gave Niv's token to a boy to hold while he crossed a slick stone because he said he needed luck and she said it was not luck, it was stubborn metal, which he accepted solemnly. The token came back wetter and unscratched.

Then the first wounded hardliner stumbled through the side passage.

He was young, masked, bleeding from a white-root cut across the ribs. A dozen evacuees shouted. A Veyra canal guard lifted a spear. Saelith stepped toward him and stopped when he flinched from her light-elf face.

"May I help?" she asked.

He stared at her as if the question belonged to a dead language.

Behind him, a Pale Bough blade-bearer staggered in with black severance-script burned across one arm.

The route went very quiet.

There it was: the war reaching the people who had carried it. Not as banners. As bodies.

Mara looked at the hardliner, then at the blade-bearer. Both young. Both terrified. Both full of training that told them the other's wound mattered less.

The dragon grief stirred.

Make them stop, it whispered. Make them kneel. Make them useful to peace.

Mara felt the shape of the command in her bones.

Instead, she stepped between the two wounded soldiers and the crowd.

"This road carries people who stop fighting while on it," she said.

The hardliner laughed bitterly, then winced. "And if we do not?"

Brakka's maul settled beside Mara.

"Then road narrows."

The blade-bearer looked at Saelith. "You are the oathbreaker."

Saelith held his gaze. "Yes. May I help?"

He looked at his burned arm. He looked at the hardliner. He looked at the civilians watching him decide whether pain or hatred spoke first.

"Yes," he said.

The hardliner closed his eyes. "Yes."

Saelith exhaled and began.

That was not peace. Mara knew better now. It was a moment, thin as a page, easily torn. But Siven wrote it down. Edrin witnessed it. Kesh told the crowd anyone interrupting medical neutrality would be charged a stupidity toll. Tavi found a brace. Caldus assigned the two wounded fighters to opposite sides of the same cart because, he said, if they were going to glare, they might as well keep each other awake.

The Blackroot Road kept opening.

Behind them, the drowned archive released one final bell note.

Mara felt it pass through the ledger case against her chest and into the road ahead.

Orrowen heard.
""",
}


FINAL_DEEPENING: dict[int, str] = {
    17: r"""Before they left the safe room, Kesh made one more bad decision and called it preparation.

He took Siven's tablet, turned to a blank page, and began drawing from memory: three village marks, a marsh route, a quarantine bridge, a flood boss's seal, and the side channel where he had first accepted the money. His lines were ugly at first. Then steadier. No smuggler's elegance, no false trails, no decorative confusion to protect the maker from being followed.

"What are you doing?" Mara asked.

"Making a map I should have made years ago."

"To the fever villages?"

"To the route that hurt them."

Tavi looked over his shoulder and said nothing, which for Tavi was a full civic ceremony.

Kesh added the names Reedmere, Tallow Ford, and Neth-by-the-Salt in blocky trade script. Under them he wrote: Open default carried by Kesh of the Kavik Road. No settlement accepted. No erasure purchased. Witness copies permitted.

Siven's eyes widened. "You are authorizing copies?"

"Do not sound so delighted. It makes me want to commit fraud for privacy."

"How many?"

Kesh stared at the page. "Enough."

Siven waited.

"I hate children trained by archives," Kesh said. "Three for the villages. One for Rikka. One for the mixed witness record. One for me if I become tempted to improve my biography."

Mara saw his hand shake only after he lifted the pen. She reached for the ink before it tipped. He let her steady it and did not make a joke.

That worried her more than the bleeding.

Maelin watched from the doorway. "The under-market will consider that a self-indictment."

"The under-market considers sunlight a hostile audit."

"It is brave."

"No," Kesh said. "It is late."

The map copied badly. Every copy blurred at the route's worst turn, as if memory itself disliked standing still there. Siven solved it by pressing Kesh's bloodied wrist mark beside the smudge. The mark fixed the line.

When the copies were done, Kesh folded the first and gave it to Mara.

"Why me?"

"Because you collect inconvenient paper like some people collect knives."

"That is not an answer."

"Because if I die, and if Rikka kills everyone else for handling my business, you will still say the names wrong but loudly enough that someone corrects you."

The trust in that was so crooked it almost passed for an insult.

Mara tucked the map beside the covenant scale. "I will say them carefully."

"Do not get poetic."

"No promises."

He groaned. The sound was closer to himself.

Outside the safe room, evacuation bells shifted from warning to movement. The Blackroot route was no longer only theirs. That made the road more dangerous and more honest. Kesh looked once at the table where the village shadows had stood, then opened the door.

"Fine," he said to no one visible. "Accounting later. Road now."
""",
    18: r"""They did not stop when the Blackroot Road swallowed the battle's light.

Stopping would have turned the evacuation into a pile of fear. Caldus knew it, Brakka knew it, Velra's canal workers knew it, and Kesh, who had made half a life from roads nobody else wanted, knew it best. So they kept the line moving through fungal dark while the first clash behind them became echo.

Blackroot was not a tunnel. It was an old country under the country.

The ceiling rose and fell in green-lit vaults. Fungal columns grew around broken statues whose faces had been scraped away by time or policy. Bone-lit streams crossed the path without bridges, and each crossing had to be tested by staff, maul, boot, and curse. Root systems hung from cracks like pale veins. Some belonged to Lumenorath, thin and searching. Some burned blue with Khar Veyl seal-fire. Some were older, black and glossy, pulsing faintly whenever the ledger cases passed.

The evacuees learned the road by being changed by it.

Children stopped crying first, not because they were less afraid, but because the fungal stars responded to high voices by dimming. An old canal woman began humming low to keep the lights steady, and soon half the line hummed with her. The named dead walked near the middle, where people had first avoided them and then, after the third slick crossing, begun asking them to remember who had already crossed safely. The two wounded soldiers, Pale Bough and hardliner, lay on the same cart and argued in whispers about which side had worse field bandages until Saelith told them both they were correct and therefore equally foolish.

Mara moved along the line with the ledger case.

She found herself doing small things because large things were too far away: tightening a pack strap, lifting a child over black water, taking a pot from someone whose arm shook, repeating Siven's simplest line until frightened people could say it back.

Emergency measures expired unreviewed. Passage remains open under mixed witness.

The words were too strange to comfort anyone. After a while, Mara shortened them.

"This road is owed."

That worked better.

People understood owed.

At the third stream, a root-hound emerged from the dark.

Not one of Tavi's three, or perhaps changed enough that recognition needed humility. Its copper muzzle was cracked. Fungus grew along one flank. It limped into the road and lowered its head toward Tavi.

Tavi froze.

"No," she said softly. "No, no, you should not be below."

The hound opened its muzzle and released a brassroot distress pattern. Tavi's face drained.

"What is it?" Mara asked.

"Glass Engine relay," Tavi said. "Part IV problem arriving early, because apparently geography has poor manners."

The hound projected a flickering image from its scent cage: a gnome engine-temple flooding with liquid glass, Brassroot workers trapped on upper gantries, command harmonics pulsing through the same cinder web the dragon-moon had stirred. Not now, perhaps. Soon. A warning traveling ahead of disaster and nearly dying on the road.

Tavi knelt before the root-hound. "May I?"

The creature pushed its broken muzzle into her hands.

She repaired enough of the scent cage to quiet its pain, using wire from her sleeve, a clasp Saelith gave without hesitation, and one of Kesh's lock picks that he surrendered with funeral dignity. When the hound stood again, it took position near the front of the evacuee line and began marking unstable ground with sparks.

"Your enthusiastic dog has joined the committee," Kesh said.

"Ward beast," Tavi said, voice thick.

"Your enthusiastic ward beast has joined the committee."

Mara looked at the projected image fading from the hound's cage. Blackroot Road, then glass engine, then Orrowen. The book's next roads were announcing themselves before the last one had stopped shaking.

Good, she thought, and hated that good could feel like dread.

Near what passed for midnight underground, they reached a cavern where the road split.

One branch sloped toward the low cistern refuges Velra had marked. One continued through fungal forest toward old battlefields and, beyond them, Orrowen. The evacuees had to go left. Mara's company had to go deeper.

This time no one pretended the leaving was simple.

Velra clasped Mara's forearm. "Lower canals will carry the copies."

"Do not make them martyrs."

"I am a pump warden. I make people wet and late, not holy."

Mara liked her enough to feel the goodbye.

Siven tried to stand with Mara's company.

Caldus said, "No."

Siven opened his mouth.

Brakka said, "No."

The boy closed it.

Mara gave him the non-poetic fever-road copy Kesh had made. "You carry corrections back to Vaura, Velra, and whoever is angry enough to read them."

His chin shook. "That is behind."

"Behind is not lesser."

She heard Joryn in her own voice and had to look away for a breath.

Siven clutched the copy. "Corrections remain open."

"Yes."

The evacuee line turned left.

Mara watched until the last glow beetle cage vanished between fungal columns. Then she faced the deeper road with Caldus, Saelith, Ilyr, Maelin, Tavi, Kesh, Brakka, Edrin, Sava, the damaged root-hound, and a ledger case full of truths no army would thank them for carrying.

Behind them, two civilizations collided.

Ahead, the dead empire waited.

Mara stepped onto the Orrowen road before anyone could call her saint, hazard, or answer.
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
        if chapter_no in DEEPENING:
            replacement += "\n\n" + DEEPENING[chapter_no].strip()
        if chapter_no in FINAL_DEEPENING:
            replacement += "\n\n" + FINAL_DEEPENING[chapter_no].strip()
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
        'current_form: "full-length draft zero with Book Two chapters 1-18 revised in pass 01"',
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
    print(f"Book Two chapters 16-18 revised. Word count: {total}")


if __name__ == "__main__":
    main()
