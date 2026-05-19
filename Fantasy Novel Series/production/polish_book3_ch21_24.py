#!/usr/bin/env python3
"""Revision pass 01l for Book Three chapters 21-24.

Replaces the opening Dead Capital scaffold with bespoke chapters for the
Gate of Failed Victories and the first three false-ending districts:
Conquest, Sacrifice, and Obedience.
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
    21: r"""## Chapter 21: Gate of Failed Victories

The Dead Capital opened like an eye that had been pretending to be stone.

Rain struck the invisible road ahead of Mara and made each step appear only when water hit it. One moment there was empty gray air over a plain of ash. The next, a black paving stone flashed under rain, then another, then a hundred, leading toward walls so vast they looked less built than remembered by the earth. The city of Vael rose from the dead plain in terraces of broken marble, black glass, white root, rusted iron, and dragon-scale stone. Towers leaned inward as if listening to an execution. Bridges ran between districts that should not have shared height. Streets climbed into the sky, vanished, and returned below themselves.

No smoke rose.

No birds crossed it.

Even the wind, which had worried every road since Harth Bend, went quiet at the gate.

"That," Kesh said softly, "is a city designed by someone who disliked exits."

Tavi's measuring needles spun until she slapped the case shut. "My instruments have resigned."

Brakka stood with both hands on her maul, eyes narrowed. "Gates should declare terms."

The gate obliged.

Five arches unfolded from the wall, each one a different shape of welcome. The first was built from spears, banners, crowns, and shields fused into a triumphal mouth. The second rose white and gentle, covered in flowers that bloomed without roots. The third stood perfectly straight, every stone identical, every line clean as a ruler's dream. The fourth was made of broken scales, judges' benches, gallows beams, and knives arranged into a wheel. The fifth was plain gray stone, almost kind. No carving. No threat. Only a silence that made Mara's shoulders lower before she caught herself.

Conquest.

Sacrifice.

Obedience.

Vengeance.

Stillness.

The names entered her without sound.

Behind Mara, the counter-choir's bone lanterns guttered. The dead had followed this far in a long, uneven line, living witnesses among them, road compact markers tied to packs, liability panels strapped to wagons, goblin route ribbons whipping wet against poles. Not an army. Something more fragile and harder to command. Arveth's mark shone on Sava's traveling register like a door drawn in ink.

Sava looked at the five arches and swallowed. "Minutes note: city presents moral architecture without prior agenda review."

"Object," Arveth's thin voice came from the register.

"On what grounds?"

"Everything."

No one laughed loudly. That made the small laughter matter more.

Mara stepped closer to the gate. The ground before it was paved with victories.

She saw them in the stones. Harrowmere kings holding bridges while plague wagons burned. Lumenorath saints smiling over silent courts. Khar Veyl archivists sealing records before war could use them and then calling the absence peace. Gnome guildmasters unveiling engines that saved cities and erased the names of those used in testing. Goblin road captains selling one path to save another. Troll clans editing vows so bridges stood while people fell. Dragons descending in fire to punish cages and crushing villages that had never seen the chain.

Every stone showed an ending that had worked.

For someone.

Caldus knelt and touched one black shield set into the road. His face changed. "This was a fever bridge."

The image rose: a younger knight holding a crossing, not breaking his oath, obeying the order he had once refused. Nobles escaped. The king praised him. His rank remained. The fever wagons burned on the far bank, but in the image no one showed them after the smoke began.

The city offered victory with the bodies cropped out.

Mara gripped his shoulder. "Caldus."

"I see it."

"Do you?"

He looked up. Pain crossed his face, then the harder thing beneath pain. "Yes."

The gate opened wider.

Vorrakai's voice moved through the arches, not cold now, but intimate as a hand laid on a fevered brow.

Every people has rehearsed an easy answer, little witness. I did not invent them. I only listened until I knew what ending each heart would choose if grief were tired enough.

Mara tasted ash and rain. "Then you know tired hearts lie."

Often, said Vorrakai. They also confess.

The plain behind them changed.

For a moment Mara saw the whole world they had crossed: Kell Ashgate's mines, Harrowmere's council hall, Lumenorath's uneven trees, Khar Veyl's opened records, Orrowen's moon-chamber, Third Arch, Snow Cedar Pass, Brassroot, Harth Bend, the moving road city, the counter-choir. All of it bruised. All of it unfinished. All of it still capable of becoming worse.

The fifth arch, Stillness, waited without argument.

Mara understood the first rule of the Dead Capital then. It did not tempt by lying about evil. It tempted by proving that every other answer had already failed somewhere.

Tavi crouched by the paving stones and scraped a sample into a vial. "The road is made of selected evidence."

Ilyr gave a tired smile. "A historian's nightmare."

"No, a politician's dream."

Saelith looked at the white arch of flowers. Her face had gone bloodless. "It will show each of us what we most fear wanting."

"Good," Brakka said.

Everyone turned to her.

The troll oath-sister tightened her grip on the maul. "A bridge that hides its weight kills. Better to know."

The counter-choir stirred. Some dead wanted to enter. Some wanted to flee. Some wanted final rest before the city could name them wrong. Arveth's mark pulsed hard enough to darken the page.

"No one enters alone," Mara said.

The arches shuddered.

That, apparently, had been an answer the city disliked.

"No single hero," she continued. "No perfect victim. No pure judge. No obedient peace. No private revenge. No quiet without consent. We enter in witness, and we answer by name."

The gate of spears opened first.

Conquest breathed out: iron, sweat, horse blood, and applause.

Caldus stood.

"Of course," he said.

Mara looked at him.

He smiled without humor. "Old wounds first. Efficient city."

They entered beneath the banners, and the gate closed behind them with the sound of a crowd cheering a battle it had not survived.""",
    22: r"""## Chapter 22: District of Conquest

In the District of Conquest, every banner told the truth from the victor's side.

They snapped above avenues wide enough for armies, bright despite the dead sky: Harrowmere blue, Lumenorath white, Khar Veyl violet-black, Brassroot brass, Kavik green, troll stone-gray, dragon fire-gold, and a hundred older standards whose kingdoms had become footnotes or recipes. Each banner showed the same scene from a different angle. A city taken. A tyrant thrown down. A plague contained. A road secured. A cage broken. A rebellion saved from itself by someone willing to command.

The streets were clean because the dead had been moved out of sight.

Mara noticed that first.

Caldus noticed the soldiers.

They stood along the avenue in ranks: human knights, light-elf riders, dark-elf spear shadows, goblin scouts in military paint, gnome artillery crews, troll shield-bearers, dead cavalry, dragon silhouettes cast in flame against the walls. None attacked. All saluted Caldus.

He flinched as if struck.

At the far end of the avenue rose a dais. On it lay a shield newly forged, blue enamel unmarred, silver lion bright at its center. Beside it rested a sword fitted to Caldus's hand before his old wound. A clean cloak hung from a command chair. Above the chair, in letters cut from crown gold, stood the words:

HONOR RESTORED BY NECESSITY.

"Subtle," Kesh muttered.

The district ignored him because temptation had chosen better prey.

A younger Caldus walked out of the banners.

Not a ghost. Worse. A possible man. His armor was polished, his sword-arm strong, his face unmarked by the years of exile that had made the real Caldus kinder and more tired. Behind the possible man, the fever bridge appeared. This time he obeyed. He cut the bridge. The noble children crossed safely. The royal line survived. The chronicles praised his discipline. Harrowmere held. Later, under that survival, fewer wars came. Better roads. Stronger granaries. A kingdom capable of facing the dead rising without wagon-door councils in the rain.

The district did not show the burned fever wagons until Mara asked it to.

"Show them."

The banners snapped harder.

"Show them," Caldus said.

The avenue darkened. Smoke crawled from beneath the paving stones. People appeared on the far bank: mothers with fevered children, old miners, debtors, servants, a boy with one shoe, a woman pounding on the broken bridge posts until her hands bled. Their bodies burned in the version that made Caldus honorable.

The possible Caldus looked at them and did not move.

"You saved a kingdom," he told the real one.

Caldus's hand tightened on his cracked shield. "I saved a chain of command."

"You saved grain routes. Armories. Law. A king who later held the western line."

"And killed the poor where no chronicler had to smell it."

The possible man stepped closer. "You think your disobedience made you clean? Fever spread anyway. Villages died beyond the bridge because your mercy carried sickness with it. Your refusal did not save everyone. It only ruined your usefulness."

Mara's stomach twisted.

That was the district's sharpest blade. Not false accusation. Partial truth.

Caldus had broken an order and people had still died. He had saved some, perhaps doomed others, and lived long enough to be praised by no one except the people who could afford gratitude least. Conquest offered the seduction of decisions made clean by authority. A commander could stop counting after the objective. A disgraced man had to keep counting faces.

The soldiers along the avenue began to chant.

Take the shield.

Take the chair.

End the argument.

Caldus looked back at Mara. For a breath she saw how tired he was. His old wound had worsened since Snow Cedar. His honor had been rebuilt in pieces by people who kept needing him to stand, fight, decide, not die. The clean shield called to the part of him that wanted one oath that did not bleed through the bandage.

"If I take it," he said, "I could command the dead lines through the next gate."

"Yes," Mara said.

"It might save lives."

"Yes."

He closed his eyes.

She did not tell him not to. That would have made the refusal hers.

Brakka planted her maul on the stones. "What does the shield ask you not to see?"

Caldus opened his eyes.

He walked to the dais.

The district brightened. The possible Caldus smiled. Soldiers lowered spears in salute. The blue shield lifted itself toward his good hand.

The real Caldus took the shield.

Then he turned it around.

On the back, hidden from every cheering street, were names in tiny burned script. Not the kings saved. Not the battles won. The people cropped from victory. Fever wagons. Villages. Soldiers used as proof. Enemies executed after surrender because order needed a period at the end of the sentence.

Caldus read until his voice broke.

Then he drove his sword through the shield.

Blue enamel cracked. Silver lion split. The avenue screamed applause backward.

"I do not reject command because command is never needed," he said, loud enough for every banner. "I reject conquest because it asks me to call the dead background."

The possible Caldus drew his perfect sword.

The attack came from every victorious version of him at once.

Mara reached for cinder heat, but Caldus shook his head once. His fight. Not alone, but his. Brakka took the left flank. Ilyr cut shadows from beneath banner soldiers. Saelith's rough hymn kept the chanting from becoming orders. Tavi threw a liability-stamped pressure flare under the dais and shouted, "Known harm named!" Kesh rang route chimes so the company knew where the real Caldus stood when identical versions tried to surround him.

Caldus fought badly at first.

That saved him.

The perfect versions moved with clean doctrine. The real man favored one arm, stumbled on broken paving, used his cracked shield edge, took help when Brakka shouted, ducked when Mara warned him, and let Saelith pull him back before pride could hold him in place. Each imperfect choice cut one banner loose.

At last only the possible Caldus remained.

"History will not forgive you," it said.

Caldus lowered his sword.

"Good," he said. "Let the living review me instead."

The district broke.

Banners fell, and beneath each one was a body, a name, a story interrupted by someone else's order. The avenue became a road of witness stones. No cheering. No clean crest. Just a way forward.

Caldus returned to Mara with blood on his mouth and the broken blue shield hanging from one strap.

"I wanted it," he said.

"I know."

"Not the killing. The ending. The part where someone says enough and the world obeys."

Mara looked toward the next district, where white flowers opened without roots.

"That is how it keeps finding us."

Caldus nodded, then stepped aside.

For the first time since she had known him, he let someone else walk into danger first because the next temptation was not his.

Saelith took Mara's hand.

Together they entered the District of Sacrifice.""",
    23: r"""## Chapter 23: District of Sacrifice

The District of Sacrifice smelled of clean linen, rain-washed stone, and flowers that had never known dirt.

No blood marked the altars.

That was its first lie.

They bloomed everywhere: white platforms under arched trees, little roadside shrines, marble steps, open rooms with no roofs, each altar covered in harmless flowers whose petals drifted upward when touched. Bells rang softly from towers with no doors. Water ran in shallow channels beside the path, clear enough to show reflections that were kinder than faces.

Mara saw herself in the water and looked away.

The reflection kept walking beside her.

In it, she was dead.

Not ruined. Not cold. Beautifully dead, which was worse. Her burned hands rested over her heart. Ashgate cloth wrapped her wrist. The cinders of Vael Taryn shone around her body like banked stars. Beyond the reflected altar, the world breathed easier. Dead soldiers rested. Harth Bend slept without stolen silence. Kell Ashgate children played in streets where the air did not cough. Saelith smiled without blood on her face. Caldus lived old enough to train better oathkeepers. Tavi built release engines no one could corrupt. Kesh's roads carried refugees without debt. Brakka's bridges stood crowded and safe. Arveth's testimony entered every court, then chose rest.

All because Mara had given herself to the cinders and become the answer no one else had to carry.

She stopped walking.

Saelith's grip tightened around her hand.

"Do not look alone," Saelith whispered.

"I am not."

But Mara wanted to.

That was the shame of it. The District of Sacrifice did not offer death as punishment. It offered relief from being unfinished. Every argument behind them, every slow compact, every casualty list, every person harmed while the right answer assembled badly, could end if Mara made herself the perfect victim. The district understood the old wound under her ribs: usefulness as the nearest thing to love. Here was the final usefulness. Holy, praised, irreversible.

At the central altar stood Joryn.

Mara knew it was not him. Her brother lived far behind them, or she hoped he did, in a world still messy enough to let him be angry at her. This Joryn wore miner's clothes clean of ash. His hands were whole. He smiled the way he had before the mines taught both of them to count bread before joy.

"Little spark," he said.

Mara nearly broke.

Saelith stepped between them. "No."

The false Joryn looked at her kindly. "You love her. Then you know what she can spare."

Flowers opened along the altar. Each one held a scene: a child saved from a corpse road, a troll bridge not collapsing, a gnome forge not exploding, a dark-elf archive opened without riot, light and dark elves standing together without old hatred, dragons lowering their heads in shame, Vorrakai's grief quieted by one bright death.

"One life," the false Joryn said. "One life freely given against thousands spared. Is that not what all your witness has taught you? Count the cost. Name it. Choose."

Saelith's hand shook.

Mara felt it and understood that the district had a second victim in mind.

Saelith had been trained to sanctify sacrifice. The Pale Bough had called obedience beautiful. Serathiel had called erasure mercy. Even after she broke the law, some part of her still feared that refusing a perfect offering was selfishness wearing ethics.

"If she chooses it," the false Joryn said to Saelith, "will you deny her? Will you make love into a chain?"

Saelith went white.

Mara heard Vorrakai behind the flowers.

No crown. No command. No conquest. Only gift. Even you cannot condemn a chosen gift, little witness.

The altar steps warmed under Mara's feet.

She wanted Joryn safe. Wanted Saelith spared. Wanted Caldus to stop bleeding and Tavi to stop burning her hands and Kesh to stop finding old debts in new roads. Wanted Brakka's bridges full of refugees who lived. Wanted the dead to rest when they chose and the living to stop making every choice under knives. Wanted, with sudden fury, to be done being a person with limits.

Saelith turned to her.

"Do you want this?" she asked.

Mara could have lied. A heroic lie. A clean refusal. Instead she said, "Part of me does."

The flowers brightened.

Saelith nodded, tears on her face. "Then I witness that part. I do not crown it."

The false Joryn frowned.

Saelith faced the altar. "A choice made inside a machine built to make one answer holy is not free enough to end the world."

"You fear her freedom," the false Joryn said.

"Yes," Saelith said. "Because love fears losing what it loves. Fear is not always control. Sometimes it is evidence that someone matters beyond function."

Mara began to cry then, not prettily.

The district shifted tactics.

Every altar showed Mara stepping forward. Every companion kneeling, grateful, grieving, saved. The counter-choir singing her name into final rest. History kinder because the underdog girl had become the one sacrifice powerful enough to absolve everyone else of politics.

Kesh's voice cut through the flowers. "I object to absolution offered before payment schedules are complete."

Tavi sniffed. "Also, if anyone calls becoming a magic battery a sustainable architecture, I will haunt the diagram."

Brakka planted herself at the altar base. "No bridge demands one stone carry all weight."

Caldus added, "And no oath is holy because it kills the only person willing to take it."

The false Joryn's smile vanished.

Mara climbed the altar.

Saelith moved with her, hand still in hers. At the top, Mara looked down at the reflection where her death saved everyone. Then she spat into the water.

It was not elegant.

The reflection rippled.

"My life is not a solution that saves the rest of you from choosing after me," Mara said. "If I die, I die a person. Not a shortcut."

The flowers browned at the edges.

The false Joryn reached for her. "Little spark."

Mara looked at him. "My brother would tell me to eat first, then argue."

Saelith laughed through tears.

The district broke.

Altars cracked, revealing old stains beneath the marble. Not blood only. Ink. Ash. Milk. Tears. All the substances people had spilled while making one victim carry what a community refused to change. The water ran muddy. The harmless flowers rooted at last in actual soil and became ordinary, fragile, mortal.

Mara stepped down shaking.

Saelith caught her.

"You said part of you wanted it," Saelith whispered.

"Yes."

"Thank you for not hiding that from me."

Mara leaned her forehead against Saelith's shoulder. The city had not been defeated. It had only been answered once.

Ahead, the streets straightened into impossible symmetry.

Obedience waited, quiet and beautiful, with every role prepared.""",
    24: r"""## Chapter 24: District of Obedience

The District of Obedience had no guards because no one inside it needed watching.

That was how Mara knew it was a prison.

The streets aligned with impossible symmetry. Houses stood at exact intervals, each door painted the right color for the work inside. Bells rang every quarter hour, and every person moved on the sound: bakers lifting bread, clerks opening ledgers, soldiers turning at corners, children raising slates, healers washing hands, dead neighbors sweeping porches they had swept in life. No one hurried. No one resisted. No one looked unhappy.

No one looked surprised.

Saelith stopped at the first intersection.

Ilyr stopped beside her.

Across the square, a light-elf court and a dark-elf archive faced each other, joined by a bridge of white root and black stone. On the bridge stood Serathiel, Vaura, Auralian, Maelin, and every lawgiver who had ever told either people that peace required the right kind of silence. They were not arguing. That made them look dead even when some of them were only memories.

A voice spoke from the bells.

All things in their place. All gifts used rightly. All wounds prevented by order.

Saelith's face went still.

Mara had seen that stillness before, in Lumenorath, before Saelith learned that obedience could be a wound with flowers around it.

"Saelith," Mara said.

"I hear it."

"What does it sound like?"

Saelith swallowed. "Home before I knew better."

Ilyr's mouth twisted. "Khar Veyl before I admitted better was expensive."

The district gave them roles.

Saelith's robe changed first. Her travel-stained sleeves whitened. Blood vanished from the hem. A Pale Bough cord appeared at her throat, corrected interval woven into it so the district could pretend it had learned. Ilyr's coat darkened into formal archive black, exile marks removed, public shame edited into honorable return. Maelin's opened-record scars vanished. Auralian's unhemmed robe hemmed itself. Even Mara felt a title settle against the back of her neck: Witness, recognized, useful within proper bounds.

She clawed at the sensation.

Kesh swore as route tokens clicked into a regulated chain across his chest. "I am allergic to proper bounds."

Tavi stared in horror as her tools sorted themselves by approved use. "My wrench just joined a committee."

Brakka's maul became ceremonial.

The troll's expression promised the district a short future.

But the trap belonged to Saelith and Ilyr.

The bridge between white court and black archive opened. On it, the impossible city offered them what their peoples had never managed: Lumenorath beauty without open cruelty, Khar Veyl truth without public panic, light and shadow balanced in fixed roles. Saelith would sing mercy. Ilyr would record truth. Neither would overstep. Neither would bleed. Their people would stop killing each other because the district would assign them peace.

"No more holy war," said the bell voice.

"No more sealed guilt."

"No more ugly correction."

Saelith took one step toward the bridge.

Ilyr took one too.

Mara reached for them, but the street shifted. A perfect crowd moved between her and her friends, each person smiling, each body exactly where order placed it. To shove them aside would be violence. To wait would be surrender. That was obedience's cruelty: it made every interruption look like the first sin.

The counter-choir's lanterns dimmed.

Arveth's mark flickered on Sava's register. Procedural horror, it wrote, then faded.

Mara tried to call Saelith's name. The bell rang over her.

Saelith and Ilyr reached the center of the bridge.

Serathiel's memory bowed to Saelith. "You corrected mercy. Now let mercy have a shape."

Vaura's memory bowed to Ilyr. "You opened the record. Now let the record keep the peace."

Maelin, or a version of Maelin without rage, held out a black-and-white ledger. "Sign the concord."

The bridge rail bloomed with names of people who would live if they signed. Thousands. Maybe real. Maybe possible. In the Dead Capital, possible carried the weight of prophecy if the heart wanted it enough.

Saelith lifted the pen.

Ilyr caught her wrist.

For one terrible breath, Mara thought he was stopping her.

Then he put the pen in her hand properly, not as command but as question. "Do you want it?"

Saelith's eyes filled. "Yes."

Ilyr closed his eyes. "So do I."

The bridge brightened.

He opened them again. "That is why we should mistrust the version that costs us nothing."

Saelith looked at the concord. "It costs us freedom."

"The district will call that maturity."

"It costs our people the right to remain angry."

"It will call that healing."

"It costs the dead the right to interrupt beauty."

"It will call that reverence."

Saelith's hand shook.

The bell rang again, harder. People in the street turned toward Mara with serene accusation. Caldus tried to push through and found his own body slowing to match the crowd. Kesh's regulated token chain tightened. Tavi's tools clicked into locked slots. Brakka's ceremonial maul grew heavier in her hands.

Mara had one way to stop it quickly.

Command.

The cinders under the district were aligned like perfect teeth. One word from her could break the rhythm, freeze the crowd, pull Saelith and Ilyr back. The district had been built to expose the hypocrisy of freedom under pressure.

Mara put both burned hands at her sides.

"Saelith!" she shouted between bells. "Wrong note!"

Saelith laughed once, wet and startled.

Then she sang the ugliest note Mara had ever heard.

It was too sharp, too low, and cracked in the middle. It did not harmonize with the bells. It did not improve the concord. It did not make peace easier to admire. It sounded like a living person refusing to be arranged.

Ilyr drove his shadow blade through the ledger, not to destroy the record, but to split it open. Names spilled out: not categories, not functions, but objections. Light-elf servants. Dark-elf prisoners. Mixed children. Dead witnesses. He read them as fast as they fell, and Maelin's real voice joined from the street, furious and alive.

"Incorrect spelling," she shouted. "Typical."

The perfect crowd stumbled.

Tavi ripped her wrench from the approved rack and threw it to Kesh, who used it to pry open his token chain. Brakka snapped the ceremonial head off her maul and discovered the real stone under it. Caldus punched a bell post with the flat of his broken shield. Sava began recording every person who stepped out of assigned place, which somehow made stepping out look official enough for several clerks to attempt it.

Mara ran.

This time, the crowd did not part. People chose badly, slowly, unevenly, and that was enough. A baker dropped bread. A dead sweeper stopped sweeping. A child wrote the wrong letter on a slate and grinned as if inventing crime. The bridge shook.

Saelith tore the Pale Bough cord from her throat.

Ilyr took it, tied it around the split ledger, and handed both to Maelin. "Public archive."

Maelin smiled with all her teeth. "Messy."

"Essential."

The district cracked along every perfect line.

No explosion. No heroic collapse. The houses slumped by inches. Doors repainted themselves in colors no system had approved. Bells rang at different times until the sound became noise and then, finally, choice.

Saelith came back to Mara trembling.

"I wanted the concord," she said.

Mara took her hand. "I know."

Ilyr looked at the broken bridge. "I did too."

Behind them, a dead clerk swept half the street, stopped, and walked away laughing softly.

Peace without consent had failed to remain peace.

Ahead, the road turned red.

The District of Vengeance waited with every knife already named.""",
}


EXTRA_DEEPENING: dict[int, str] = {
    21: r"""Before the Conquest arch swallowed them, the gate made them pay admission in memory.

Not blood. The Dead Capital was subtler than that. A shallow basin opened in the road, black water filling it from no visible source. Each person who meant to enter saw one failed victory in the surface. Caldus saw the fever bridge. Saelith saw Serathiel saving Lumenorath by cleansing Orrowen and being crowned saint for it. Ilyr saw Khar Veyl sealed, safe, unanswerable, with his exile erased because no one had opened enough truth to make exile necessary. Tavi saw the command engine improved until no one called it command. Kesh saw a caravan saved by selling a route and no one ever finding the bill. Brakka saw a bridge standing because every inconvenient refugee had been turned away before weight became dangerous.

Mara saw Kell Ashgate free under a new crown.

That was the cruelest image because it looked better than truth. Mordane dead. Ashgate air clear. Joryn alive, older, laughing in a square named for Mara. The miners paid. The dead honored. Children running where slag heaps had been gardens. At the center stood a statue of Mara with one hand lifted over a furnace heart, and every person below it knew what to do because the statue's inscription had decided the shape of courage for them.

USEFUL UNTO DEATH.

Mara almost kicked the basin.

Arveth's mark scratched across Sava's register. Statues are often delayed cages.

"Noted," Sava whispered.

The basin asked for a token.

Brakka offered a chip from Third Arch, not as surrender but as witness that bridges could carry the condemned as well as the celebrated. Kesh dropped one public route ribbon into the water and watched it twist into a chain before dissolving. Tavi put in a burnt screw from the destroyed command engine. Saelith gave a loose thread from the cord she had torn away in Lumenorath. Ilyr gave a scrap copied from Khar Veyl's opened record, a line naming his own omission. Caldus, after a long moment, took the last strap from the broken blue shield he carried and laid it on the water.

Mara had nothing prepared.

Then she unwrapped the Kell Ashgate cloth from her wrist.

The others went still. She had worn it since Book One's road, since before anyone beyond the mines thought her name mattered. It was only cloth, soot-stained and frayed, but it had been proof that the small life before crowns and courts and dragons had not been overwritten.

"I want it back," she told the basin.

The water accepted that as a vow instead of a gift.

The cloth sank and rose again, wet but whole.

The gate seemed almost amused.

The Dead Capital did not want them stripped of who they had been. It wanted those selves available for use. It wanted every wound ready to become architecture.

Mara tied the cloth around her wrist again, tighter.

"Everyone remember," she said. "If this city offers you the clean version of yourself, ask who got cleaned away."

They passed under the first arch.

Behind them, the basin filled with all the victories they had refused to enter unnamed.""",
    22: r"""The District of Conquest did not release Caldus after the banners fell.

It followed him in smaller shapes.

Every broken shield stone became a question under his boots. Could he have saved Snow Cedar Pass faster if he had claimed command? Could he have held Harth Bend in order if he had not waited for Mara's witness? Could he save the company now by taking responsibility so completely that no one else had room to fail? The district had lost its parade, but conquest did not need banners. Sometimes it wore care. Sometimes it sounded like a tired soldier saying, Let me decide so you can rest.

They found the bodies cropped from victory gathering the fallen banners.

Not corpses. Witnesses. A fever mother with smoke in her hair. A dark-elf prisoner executed after a city "secured" its future. A goblin child whose road had been seized for strategic passage. A troll bridge mason forced to choose which side of a battle line would cross. They folded banners without reverence and laid them over the stones where the district had hidden names.

Caldus went to help.

The fever mother let him take one corner of the Harrowmere blue. She looked at his cracked armor and his ruined shoulder. "Were you the man on the bridge?"

"Yes."

"Which version?"

He answered slowly. "The one who disobeyed."

"Did my sister live?"

He closed his eyes. "I do not know."

The woman nodded, not forgiving him, not condemning him, entering the answer where certainty had been trying to stand. "Then carry I do not know honestly. It is heavier than a crest and kills fewer people."

Mara watched him receive that like a knighthood no king could confer.

Later, when they found the exit, it was blocked by a portcullis made of swords pointed downward. The possible Caldus's voice returned from the metal.

One commander. One order. One road open.

Every sword bore a name of someone who might die in the next districts if the company stayed slow. The city did not threaten abstractions. It had learned their ledgers. Tavi Quen. Saelith Dawnmere. Ilyr Noct-Vey. Kesh of Kavik. Brakka of Third Arch. Sava Rennet. Othel. Nera Bell. Pell. Joryn Venn. The names hung sharp over the road.

"Mara," Caldus said, "do not touch them."

"I was not going to."

"You were thinking fast."

She grimaced. "Yes."

He handed her his cracked shield.

"Hold this."

"Why?"

"Because I cannot break a gate of swords while holding the symbol of every time I wished command would make me clean."

He took off his sword belt next.

That frightened her more.

Caldus walked to the portcullis unarmed. The blades trembled, eager to be used by someone noble enough to call violence protection. He placed both hands on the lowest sword and pushed upward. Blood opened in his palms. Brakka moved to help; he shook his head. Then the fever mother stepped beside him. Then the goblin child. Then the bridge mason. Witnesses cropped from victories put their hands on the swords and lifted with him.

The portcullis rose.

Not because Caldus was strong enough.

Because command stopped being alone.

When he returned, Mara gave back the cracked shield. He did not strap it on.

He carried it under one arm, awkwardly, like a thing still useful but no longer allowed to define the shape of his body.""",
    23: r"""The District of Sacrifice followed Mara with tenderness after the central altar broke.

It did not rebuild the false Joryn. It did something worse. It made ordinary people grateful.

As they walked, figures appeared along the road: an Ashgate child holding a clean tin cup; a dead cavalry rider laying down his trumpet; Nera Bell walking into rest without fear; Tavi asleep with unburned hands; Kesh laughing with Rikka in a road camp where no bargain had ever poisoned them; Brakka's bridges crowded but never cracking; Saelith under trees that bloomed unevenly and harmed no one; Joryn old, safe, irritated at a stew pot. None begged Mara to die. They simply lived in the world her death could buy.

That courtesy hurt more than demand.

Mara walked until she could not keep her breathing steady, then stopped beside a dry fountain full of white petals gone brown at the edges.

"I used to think sacrifice meant someone else choosing you for the knife," she said.

Saelith stood beside her. "Often it does."

"This district knows I might choose the knife myself."

"Yes."

"Then what makes it wrong?"

Saelith did not answer quickly. That was one reason Mara loved her and feared loving her. Saelith had been trained to give beautiful answers before pain could ask follow-up questions. Now she let silence do its honest work.

"Sometimes it is not wrong to die for someone," Saelith said at last. "Caldus would have died at Snow Cedar. Brakka would die for a bridge full of refugees. I would die for you, and that frightens me less than some things I have lived through."

Mara looked at her.

Saelith's eyes shone. "The lie is not that a life can be given. The lie is that one gift can absolve everyone else of changing."

The fountain petals stirred.

Mara thought of Ashgate's old ledgers. Someone always willing to spend a poor life so the system could continue with a plaque on the wall. A heroic death could become the cleanest form of the same arithmetic if the world used it to avoid becoming answerable.

"I do not want to leave you to fix everything after me," Mara said.

"That is almost romantic."

"Almost?"

"It still assumes we would be competent without you."

Mara laughed, and the district flinched at the sound because it had expected reverence.

At the district's edge, they found a small altar with no flowers on it. Only a loaf of bread, half stale, like the one Edda Mar had given Mara in Harth Bend. Beside it lay a knife. No inscription. No threat. Only the oldest choice in the world: eat and continue, or turn hunger into proof of holiness.

Mara took the bread.

She cut it unevenly and handed pieces to everyone, living and dead.

"Terrible portion control," Tavi said.

"File a complaint."

Sava accepted her piece. "Already titled."

They ate in the District of Sacrifice, and the act of feeding each other broke the last white stones behind them. Martyrdom did not know what to do with a meal shared badly and without ceremony.

Ahead, the symmetrical streets waited.

Mara kept the knife, not for the blade, but because it had failed to become an altar.""",
    24: r"""The District of Obedience left its mark on the company in the form of habits.

That was the part Mara disliked most.

After the bells fell out of rhythm and the perfect bridge cracked, people kept moving as if the quarter-hour might still ring. Kesh reached for his regulated token chain twice though he had broken it. Tavi lined her tools by approved use before noticing and scattering them with a muttered insult. Caldus apologized for stepping out of formation where no formation existed. Even Brakka, who had seemed built from refusal and stone, paused at an intersection as if waiting for permission to choose left.

Saelith and Ilyr were worst.

They kept speaking at the same time and stopping for the other. Courtesy, on its surface. Underneath, the district's residue: light yielding to shadow, shadow yielding to light, both trapped in the perfect choreography of never colliding hard enough to change.

Maelin saw it before Mara did.

"Argue," she said.

Ilyr frowned. "About what?"

"Anything."

Saelith looked exhausted. "This is hardly the time."

"Exactly the time." Maelin shoved the split ledger into Ilyr's chest. "You have been agreeable for six minutes. It is grotesque."

Ilyr stared at her, then at Saelith. "Your wrong note was late."

Saelith blinked.

"Excuse me?"

"Effective, but late. The bell nearly settled into the third interval before you broke it."

Her eyes narrowed with immediate, glorious offense. "I was resisting a district designed from the bones of all obedience. Forgive my tempo."

"Accuracy matters."

"So does not sounding like a dying hinge."

Tavi looked up. "I enjoyed the hinge note."

"Thank you," Saelith snapped.

"I did not say as music."

The argument spread like warmth. Ilyr criticized Lumenorath training. Saelith criticized Khar Veyl's idea that muttering truth in a basement counted as civic courage. Maelin smiled. Auralian, who had been trying not to smile, failed. The counter-choir picked up the rhythm, bone lanterns beating at different times until the city's lingering bell-order finally lost its grip.

Mara watched relief become noisy and understood why obedience was so seductive. It spared people the discomfort of returning to themselves after every wound. But selves were noisy. They contradicted. They took up room. They asked why the map placed them there and whether a door could be repainted.

At the district's far edge, a dead clerk waited with a broom over one shoulder.

"I left my porch half swept," he told Sava.

"Rebellion?"

"Experiment."

"Result?"

He considered. "Dust remained. World continued."

Sava entered this with the seriousness of a military dispatch.

The exit arch had no lock. It had instructions.

PROCEED WHEN ASSIGNED.

Mara picked up a piece of fallen bell metal and scratched out WHEN ASSIGNED.

Kesh added BY WHOM?

Tavi added DEFINE PROCEED.

Brakka carved OR STAY AND ARGUE.

Saelith drew one crooked musical note beneath it. Ilyr added a footnote mark with no footnote attached, which made Sava furious enough to prove the district fully broken.

Only then did the arch open.

The road beyond ran red under a sky full of suspended knives.

The District of Vengeance did not sing, command, or flatter.

It named the guilty.

Every one of them.

Mara stepped forward with the taste of shared bread still in her mouth and knew the next false ending would not ask anyone to be clean. It would ask them to be right.""",
}


WORD_FLOOR_DEEPENING: dict[int, str] = {
    21: r"""The gate also counted those who did not come.

That was the first time the Dead Capital made Mara afraid for people beyond reach. Faces appeared in rain along the wall: Joryn in Kell Ashgate, Selli with a pencil tucked behind her ear, Lora Arlet holding Thom's hand at Third Arch, Pell's mother standing at a rope bridge with grief and courage balanced badly in both hands, Pinna Vey beside a liability panel, Auntie Varr watching road lamps move through ash rain. Not illusions of death. Worse. Lives continuing without Mara, each one vulnerable to whatever choice she made inside the city.

The wall seemed to ask whether she could bear being absent from the lives she claimed to defend.

Mara pressed her palm to the wet stone.

"I am not the wall around them," she said.

The faces blurred.

It was a hard sentence to mean. For three books, every crisis had tried to teach her that love meant arriving in time, standing in front, becoming the person who could not be spared because everyone else might break. The gate offered a subtler conquest than banners: the belief that if she loved enough, she should be everywhere her name had given people hope.

Saelith touched the back of her wrist, not the burned palm, not the cinder scars.

"They are not safer because you imagine yourself beside every door," she said.

"No."

"They are safer if the doors belong to them."

Mara nodded, though it hurt.

The wall let the distant faces fade. In their place, the five arches waited, patient as old arguments. Mara understood then that the Dead Capital was not merely a place Vorrakai ruled. It was the shape of every answer powerful grief had ever rehearsed. To walk it was to admit those answers lived in her too.""",
    22: r"""At the last boundary of Conquest, Caldus found a training yard.

It was small, almost hidden between two fallen victory towers, and that made it crueler than the parade avenue. Young soldiers drilled there with wooden swords. Human, elf, goblin, troll, gnome, living, dead. None wore rank. All watched an instructor whose back was turned. Mara knew the set of his shoulders before he faced them.

Caldus, older than now.

Not restored. Not crowned. Simply alive long enough to teach.

The vision offered no cheering. No conquest. Only an order founded after war, with oaths that could be challenged by the people they affected. It was close enough to Caldus's true future that even Mara wanted to trust it.

The older vision said, "Take command now and this can exist."

Caldus's face folded with grief.

"You are learning," the vision continued. "You know command can be answerable. You know conquest was wrong because it hid bodies. So conquer openly. Win first. Build accountability after."

There it was, the best version of the lie.

Caldus looked at the students. One dead cavalry girl corrected a human boy's stance. A goblin recruit rolled her eyes at a troll shield drill. A future that deserved protection.

"After is where accountability goes to die," Caldus said.

The vision smiled sadly. "Then children die while you build procedure."

"Some will."

Mara saw what the admission cost him.

"And if I conquer first, others die where I do not have to watch. That has been the bargain every tyrant calls temporary."

He saluted the training yard with his broken shield, not as obedience, but as apology to the future he could not purchase by becoming its contradiction. The yard vanished, leaving only a muddy square and the sound of real children far behind them who would need teachers if the world survived.

Caldus walked on, older in a way no vision could counterfeit.""",
    23: r"""The bread did not taste like victory.

It tasted stale, sour at one edge, gritty with altar dust because Tavi had dropped her piece and claimed the floor owed her flavor damages. That imperfection became important. The District of Sacrifice had offered Mara flowers without soil and death without rot, a clean end that would make everyone else's grief noble. The shared bread was ordinary enough to be almost insulting. It required chewing. It stuck in the teeth. It gave no one absolution.

Arveth's mark appeared on Sava's register while they ate.

Martyrdom dislikes digestion.

Sava read it aloud because she had no mercy when the record was good.

Mara laughed with her mouth full, then almost choked. Caldus pounded her back too hard. Kesh said he would enter assault by rescue in the minutes. Saelith cried again, but this time while laughing, which made the district's last white petals curl inward as if embarrassed.

The false Joryn appeared once more at the edge of the road.

Not strong now. Not clean. Only a boy Mara remembered, holding two stolen heel ends under his coat and whispering that she had to eat hers before anyone saw. The district had found a truer image by accident.

"He would want you alive," Saelith said.

Mara looked at the fading boy. "He would want me home."

"Yes."

"Those are not always the same."

"No."

The false Joryn smiled sadly and vanished, leaving one heel of bread on the stone. Mara picked it up, wrapped it in the Kell cloth, and put it in her pocket. Not as holy relic. As lunch delayed.

The District of Sacrifice cracked a little more because nothing offended it like a person choosing to need food later.""",
    24: r"""Obedience tried one last time at the exit.

It did not use bells. It used relief.

For three breaths after the arch opened, every person knew exactly where to stand for the next district. Brakka in front, because strength belonged in front. Caldus beside Mara, because shields belonged beside leaders. Saelith behind, because healers belonged behind pain. Ilyr in shadow, because truth belonged out of sight until needed. Kesh on the edge, because goblins belonged to edges. Tavi near the mechanisms, Sava near the record, the dead in a following line. All sensible. All efficient. All slightly wrong.

Mara felt herself accept it before she caught the shape.

"No," she said.

The line loosened.

Kesh blinked. "Was I about to stand where stereotypes put me?"

"Yes," Ilyr said.

"Offensive. I choose a different edge."

"That is still an edge."

"But it is mine."

Brakka moved from the front to the middle, forcing everyone to reorganize around her absence. Caldus walked at the rear for the first hundred steps, hating it and doing it anyway. Saelith took point with the crooked note still raw in her throat. Ilyr walked in full view. Tavi gave Sava a wrench and took the ledger for six minutes, during which history became nervous. The dead witnesses spread among the living rather than behind them.

It slowed them.

It also returned them to themselves.

When the red road of Vengeance sharpened ahead, the company met it in a formation no doctrine would have designed. Mara thought that might be the first honest defense they had carried into the Dead Capital: not strength, not purity, not perfect order, but the practiced refusal to let fear assign everyone their most useful place.""",
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
        if chapter_no in WORD_FLOOR_DEEPENING:
            replacement += "\n\n" + WORD_FLOOR_DEEPENING[chapter_no].strip()
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
        'current_form: "full-length draft zero with Book Three chapters 1-24 revised in pass 01"',
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
    MANUSCRIPT.write_text(revised, encoding="utf-8")
    total = word_count(revised)
    update_metadata(total)
    update_summary(total)
    print(f"Book Three chapters 21-24 revised. Word count: {total}")


if __name__ == "__main__":
    main()
