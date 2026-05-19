#!/usr/bin/env python3
"""Revision pass 01p for Book Three chapters 37-41.

Replaces the remaining aftermath scaffold with bespoke prose: Khar Veyl's
public dark, Kavik's unsellable roads, Third Arch refuge law, Kell Ashgate's
loud homecoming, and Mara's final room-under-the-earth landing.
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
    37: r"""## Chapter 37: The Public Dark

Khar Veyl opened its lowest archive by extinguishing half the lamps.

That was not theater, though half the surface witnesses mistook it for theater and half the dark elves wished it had been. The under-realm's oldest record halls were not meant to blaze. Root-fire showed too much at once, and too much light in Khar Veyl was another method of control. In the old days, archivists taught apprentices that truth must emerge like a face at the edge of a cavern pool: slowly, under the eye's own labor, giving the beholder time to become responsible for seeing.

The old days had also produced sealed histories, dead advocates used as tools, records that named foreign crimes and hid domestic bargains, and a prince who had needed to be dragged by war into the habit of saying his own people's guilt aloud.

So Ilyr did not defend the old days when the lamps dimmed.

He stood beside the first public reading stone with Maelin on one side, his mother on the other, and the copied record of the Covenant Span open in front of him. Mara stood below the dais because everyone kept trying to put her on it. Saelith stood with the Lumenorath singers who had come to hear their names in enemy records. Caldus remained by the western exit and pretended that keeping people from trampling one another was not also a political argument. Tavi crouched behind a cracked root-fire vent with three gnome apprentices, whispering threats at a pressure regulator that had never before been asked to operate without bound cinder heat. Kesh had vanished into the crowd the moment anyone suggested visitor tokens. Brakka stood with both hands spread against the arch ribs, feeling for strain in the stone.

Sava sat at a small table near the front, blank pages stacked high, and wrote the first public rule in large letters.

No sealed record is opened alone.

"That is not law," Ilyr's mother said.

Sava did not look up. "It will have to suffer."

The gallery filled from three directions. Dark-elf citizens came first, many in formal black, some with mourning veils, some with knives worn openly because honest anger had apparently been granted wardrobe rights. Aboveground refugees came next: Orrowen dead in lantern bodies, Harrowmere soldiers without command seals, goblin road families with debt ribbons tied to their wrists, light-elf singers whose white robes had been hemmed in ash. Last came the people who had not been invited by any polite category: miners, cooks, stretcher-bearers, children sent to fetch water and staying because adults were about to say things that might finally explain them.

The public dark settled over all of them.

Not total darkness. Never that. The root-fire lamps burned low blue along the walls, each flame cupped in black glass. Faces became partial. Rank blurred. Beauty had less room to arrange itself. Mara could see eyes, hands, breath, the glint of tears, the flash of teeth when someone hated too honestly to keep lips closed.

Ilyr touched the reading stone.

The first record rose in the air, not as page or song, but as shadow-script written across the dim. Its title was very old.

Agreements With Surface Crowns Regarding Dragon Memory and Mortal Stability.

No one spoke for three breaths.

Then a woman in a miner's coat spat on the floor. "Pretty title."

Ilyr nodded once. "Yes."

That single word did more damage than a defense would have. The crowd had arrived armored for explanation. Khar Veyl had kept records because only deep houses understood context. Khar Veyl had bargained to prevent worse wars. Khar Veyl had hidden truths because surface courts would have turned them into weapons. Some of those arguments were even true, which made them more dangerous. Ilyr offered none of them before the first reading.

Maelin read.

Her voice shook on the third sentence and hardened on the fourth. The agreement named Harrowmere's first cinder tax, Lumenorath's songs of suppression, Khar Veyl's witnessing rights, and the clause by which dark-elf archivists had been permitted to examine bound dragon memory so long as their findings remained sealed until political danger passed.

"Political danger," the miner's-coat woman said.

Maelin looked down. "That is the phrase."

"My grandmother died in a royal mine warmed by one of those memories."

"What was her name?"

The woman recoiled as if Maelin had drawn a blade.

Mara understood the recoil. Names could be a kindness or a snare depending on the hand asking. She almost stepped forward. Saelith caught her sleeve, not to stop her forever, only to give the question time to remain Maelin's.

The woman said, "Vessa Mar."

Sava's pen scratched. "Vessa Mar. Kell Ashgate?"

The woman turned. "Yes."

"Relation to Edda Mar?"

"Daughter."

"Then your family has a claim in the pump records opened after the covenant break."

The woman looked as if she might fall. "A claim?"

"Not money only," Sava said. "Though money, if money is owed. A claim to know what was used, who authorized it, whether Vessa answered after waking, and what repair she asks if she chooses to ask."

The public dark shifted.

Anger, Mara was learning, changed shape when given a handle. It did not become smaller. It became less available to anyone who wanted to pour it into a mob and ride it.

The second record named Khar Veyl houses that had objected to the cinder economy and then accepted archive access in exchange for silence. Ilyr's house was listed twice. Once under objection. Once under acceptance.

His mother closed her eyes.

"Read it," said someone from the back.

Ilyr read it himself.

The first thrown stone struck the reading dais and split. It was not large enough to kill. It was large enough to tell the room that distance had ended.

Caldus moved, but Ilyr lifted a hand.

"No shield," Ilyr said.

"You are bleeding," Caldus answered.

"Yes."

That was not enough for Mara. She had lost patience with people using pain as proof that they were doing moral work. But Ilyr did not look purified. He looked frightened, ashamed, and present. Blood ran from his cheek to his collar, ruining the formal black his mother had clearly made him wear. He did not touch it.

"I cannot ask public trust while protected from public anger," he said. "I can ask not to be murdered before page three."

Kesh's voice came from somewhere near the ceiling. "A restrained procedural request. I support it with suspicion."

Several people laughed before remembering to be furious. The laugh did not excuse anyone. It loosened enough air for breathing.

Page three opened by itself.

That was the problem.

The old seal beneath the reading stone woke as if anger had fed it. Blue root-fire ran up the dais cracks. Drawers opened in the walls without hands. Sealed indexes spilled out, each one trying to join the public record before anyone had named the harmed. The archive had been built to prevent panic, and now that prevention had failed, it tried to correct by becoming indiscriminate. A hundred shadow-scripts flared at once: names of informants, names of victims, half-context confessions, death lists, private letters, witness accounts taken under fear, cinder inventories, records of children hidden during the Orrowen occupation, songs banned from Lumenorath because they remembered dark-elf prisoners as people.

Truth became a flood.

The crowd surged backward and forward at once. Someone screamed. A light-elf singer stumbled, hands over her mouth, as a record named her grandmother in a mercy choir that had silenced wounded soldiers after the Snow Cedar retreat. A dark-elf man lunged for a drawer that had opened beside him and tried to shove the papers back inside. The miner's-coat woman stared at Vessa Mar's name burning in four places above the floor, each version attached to a different official lie.

Mara heard the cinder under the archive.

Not bound now. Not commanded. Panicked.

It was not one dead witness. It was a chorus of record fragments that had spent centuries trapped inside the machinery of withholding. Freed from secrecy and robbed of structure, they cried out with the same desperate demand in a hundred voices.

See me first.

Every name wanted to be first.

The old Mara would have tried to catch them in herself and sort the pain by instinct. The throne had trained the world to expect that from her even after she refused it. She felt the pull. One breath, and she could make every shadow-script pause. One command framed as witness. One useful trespass.

Saelith's hand closed around hers.

"You are not a drawer," Saelith said.

Mara breathed until the cinders remained cinders and she remained Mara.

"Exits," she called.

Caldus heard the whole plan in the one word. "North and west open. No one leaves with loose records. No one is trapped for wanting air."

Brakka shoved both palms harder into the arch ribs. Stone boomed. "The hall is carrying too many voices. Tavi."

"I noticed," Tavi snapped, and jammed a copper wedge into the root-fire vent. "Apprentices, shutters half open. Half. If you open them all, we either blind the room or become a cultural crater."

Maelin climbed onto the reading stone.

"Stop reading everything," Ilyr's mother shouted.

"The archive is not reading," Maelin said. "It is screaming."

She took a lamp from the dais and turned its black-glass cup toward the wall. The shadow-scripts nearest it dimmed. Not vanished. Dimmed enough for choice to enter. Other dark-elf archivists saw and copied her, though some did it with faces like people assisting their own humiliation. Light-elf singers, trained for resonance, began humming notes that did not smooth the cries but separated them. Orrowen lanterns blinked one by one as the dead chose which records they would witness and which they would refuse to hold.

Kesh dropped from the upper stacks onto a balcony rail. "If you are here to grab the record that makes your enemy look worst, please form a line under the sign marked future bad idea."

"There is no sign," someone shouted.

"I am spiritually holding it."

"Get down," Caldus barked.

"That is also spiritually unlikely."

The foolish exchange kept three panicked youths from bolting through a crush of elders. Kesh saw it too and kept talking, selling nonsense as cheaply as breath could buy time.

Mara went to the miner's-coat woman, who was still staring at Vessa Mar's name.

"Edda," Mara said softly, guessing from the shape of grief and Sava's record.

The woman looked at her. "You knew her?"

"A cinder named Vessa spoke after the lock broke. She asked whether Kell was still loud."

Edda Mar's face broke open.

Mara did not touch her without asking. "May I stand with you?"

Edda nodded once.

They stood while the four records of Vessa Mar were lowered into one circle: employment ledger, death notice, pump authorization, cinder maintenance log. The records contradicted each other. In one, Vessa had died in a gas pocket. In another, she had volunteered for memorial warmth. In the third, she was listed as nonresponsive fuel. In the fourth, her name had been shortened to V. M. because full names created, in the clerk's words, "operational distress."

Edda made a sound that was almost a laugh and almost a curse. "Operational distress."

"Yes," Ilyr said. He had come down from the dais, blood drying on his cheek, and now stood in the public dark with no stone under him. "That clerk was Khar Veyl trained."

His mother inhaled.

Edda turned on her. "You knew?"

The old archivist did not pretend the question was simple. "No. I knew the training. I knew what shortening names does. I knew it was common in surface ledgers and said our work was only preservation, not use."

"That is a lot of knowing arranged around no."

"Yes."

Edda slapped her.

The sound cracked through the hall.

Caldus stepped forward and stopped himself because the old archivist did not ask for defense. Ilyr flinched harder than his mother did. Maelin looked at the floor. Sava wrote nothing until Edda spoke again.

"Do I get arrested for that?" Edda asked.

Ilyr's mother touched her reddening cheek. "Do you want the legal answer or the honest one?"

"Honest."

"I want to arrest the entire moment. I do not think I should be allowed."

Edda laughed then, once, bitter and real. "Put that in your record."

Sava wrote it word for word.

By dusk, the flood had become circles.

Not order. Circles. Some records were public immediately. Some were named and held until those most harmed could be found. Some were sealed again with public reasons and dates, not because secrecy had been redeemed, but because exposure could still wound people with no power to answer. Every resealed box had three names attached: who requested delay, who could challenge it, and when the challenge must be heard. No seal could outlive the people it claimed to protect without being accused in public.

Ilyr took no chair.

That offended nearly everyone. Those who hated him wanted him pinned to office. Those who trusted him wanted him responsible. Those who feared chaos wanted a keeper. Ilyr stood beneath the dim lamps and let each demand strike.

"Khar Veyl's records will have many keepers," he said. "Public keepers. Rotating keepers. Harmed keepers. Hostile keepers. Some trained here. Some not. I will serve a term if chosen by a circle that includes those named in our failures."

"Coward," someone shouted.

"Sometimes," Ilyr said.

The answer moved through the hall more strangely than any defense. It gave no handle to reverence.

Maelin stepped beside him. "I will not be your public dark's pleasant face."

"No," Ilyr said. "You will be worse."

"Thank you."

His mother removed the key-ring from her belt. She had worn it since before Mara was born, a black iron ring with seven bone keys and one root-fire shard. The old archive had bowed to those keys. Apprentices had bowed to them too. She held them out, not to Ilyr, but to Edda Mar.

Edda stared. "I am not an archivist."

"No," said Ilyr's mother. "That is one reason."

"I cannot read half your marks."

"Then the marks must answer to you before they answer to us."

Edda took the ring as if accepting a tool that might bite. "If this becomes a performance, I will throw it at someone."

Kesh leaned down from the balcony. "Aim with civic purpose."

The public dark did not end with reconciliation. That would have been another kind of lie. People left angrier than they had entered, but their anger carried names, dates, handles, witnesses, and appointments. Khar Veyl did not become innocent by opening its doors. It became less able to confuse darkness with virtue.

When the final lamp was cupped, Ilyr sat on the floor beside the reading stone and pressed his sleeve to his cheek.

Mara sat beside him.

"Do not say it went well," he said.

"It went alive."

He looked at her, tired eyes bright in the low blue flame. "That is a cruel standard."

"Yes."

Across the hall, Edda Mar was arguing with Ilyr's mother about whether key custody required breakfast meetings. Maelin had gathered three youths and was showing them how to hold a lamp so names could be seen without being turned into spectacle. Saelith hummed a broken harmony low enough that no one had to call it music. Caldus escorted an old enemy to the west exit because the man had asked to leave before becoming worse. Brakka took her hands from the arch and listened as the stone settled into its new load.

Khar Veyl's public dark remained dim.

That was the mercy of it.

Not hiding.

Room for sight to become responsible before it called itself truth.""",
    38: r"""## Chapter 38: Roads That Cannot Be Sold Alone

The Kavik road-moot gathered in a dry riverbed where every stone had been used at least once as a weapon, a marker, a seat, a debt token, or a cooking surface.

Kesh called this efficient.

Rikka called it evidence that goblins had been civilized longer than anyone willing to admit it.

The riverbed cut through red hills south of the storm road, a scar of polished stone and thorn-scrub where caravans had hidden from taxes, armies, dragons, love affairs, and several kinds of weather with legal ambitions. Dead cinder heat had once warmed the route stones buried along its bends. Those stones were cold now. Without them, a traveler could not touch a mile marker and know whether the next turn had been sold, blocked, poisoned, blessed, cursed, or merely occupied by cousins.

This, according to the old road houses, was a tragedy.

According to the refugees who had paid three tolls for one escape, it was Tuesday acquiring witnesses.

Mara sat on a flat stone beside Saelith while the moot assembled itself by argument. No one called order. Order in Kavik culture arrived only when enough people had insulted the alternatives. Banners hung from spear shafts: green for route families, rust for debt witnesses, yellow for guest-right, black for roads closed by blood, blue-white for the new cinder consent mark that no one agreed how to draw. Children ran between the markers carrying water skins and gossip. Three trolls from Third Arch stood at the north rim because bridge matters had become road matters and nobody liked how much that made sense. A pair of dark-elf observers kept notes under a shade cloth, looking delighted and appalled.

At the center of the moot lay the disputed road.

Not a map of it.

The road itself, or as much of it as could be brought into a dry riverbed: forty-seven stones, six ropes knotted with route-debt, a cracked toll bell, a mule shoe, a funeral charm, three bloodstained ribbons, and a small cold cinder that had once warmed under travelers who paid the proper fee. The old houses called it the South Ash Bend Spur. The refugees called it The Way We Almost Died. Kesh called it very expensive trouble, which meant he cared.

Rikka stood across from him with a ledger under one arm and a knife in the other.

"You betrayed the Spur twice," she said.

Kesh touched his chest. "I have grown as a person."

"You sold a warning to Harrowmere riders."

"I sold them the wrong warning."

"And a correct river level."

"It was a confusing day."

Rikka looked at Mara. "This is why he cannot be roadmaster."

"I have never wanted a title with that much paperwork," Kesh said.

"You wanted the toll rights."

"Briefly. I was young, charming, and underfed."

"You were thirty-two."

"Goblin youth is spiritually flexible."

The old road houses did not laugh. That told Mara who had arrived with something to lose.

Their speaker was a narrow woman named Varrik of the Fifth Mile House, dressed in patched green silk and bone buttons carved into tiny wheels. She had the road-family look Mara had seen in Kesh when he stopped joking: eyes that measured exits before faces, hands never far from cord, grief hidden behind arithmetic.

"The Spur belongs to the houses that maintained it," Varrik said. "Cinder heat is gone. Route stones are cold. Without ownership, no one will repair washouts, post bandit notices, or bury the dead who die between settlements."

A refugee man lifted his sleeve. Three toll marks had burned scars around his wrist. "You owned it when my wife had to pay twice to cross the same mile."

Varrik's face did not change. "Which house?"

"You ask like that helps."

"It may."

"It will not bring her back."

"No," Varrik said. "But it may identify who owes the burial fee and the answer fee."

The refugee stared, wrong-footed by precision when he had braced for denial.

Kesh leaned toward Mara. "This is why road people are the worst. They can be useful while morally offensive."

"I heard that," Varrik said.

"You were meant to."

The first vote failed before anyone counted.

It failed because the old houses had arrived with sale cords already braided. Under the proposed settlement, each road section would be assigned to a maintaining house, each house could sell passage contracts to merchants or armies, and refugees would receive discounted travel if witnessed by two recognized authorities. The phrase discounted travel detonated the moot.

By noon, five people had challenged Varrik, two had challenged Rikka, one had challenged Kesh, and a goat had eaten the corner of the proposed compact. Tavi declared the goat the only honest critic and was asked by three goblins whether she was available for civic office.

Then the ravine bell rang.

Every goblin in the riverbed went silent.

Kesh was on his feet before the second clang. "That bell is dead."

"Apparently not," Saelith said.

"No. I mean the bell-ringer is dead."

The sound came from the west, where the South Ash Bend Spur crossed a narrow ravine on a rope-and-plank span older than several grudges. A caravan had taken the upper turn despite the moot's halt markers. Mara saw dust first, then mule ears, then a pennant she recognized from the merchant table outside the Dead Capital. The same kind of traders who had tried to buy inert relics from hungry refugees now drove six wagons toward a disputed road whose ownership had not been settled.

At the ravine's lip, old route stones flared green.

Not warm.

Warning.

The first wagon rolled onto the span.

The ropes screamed.

Brakka was too far. Caldus shouted for the caravan to halt. The driver did not or could not hear over the bell, which rang faster now, frantic as a heart. Kesh ran.

No one in the riverbed ran like a goblin road thief. Kesh became angle and dust, heel and hand, taking the slope sideways where humans would have tumbled and elves would have wasted dignity. Rikka cursed and followed with three route runners. Mara and Saelith took the lower cut. Tavi grabbed a coil of wire. Brakka started across the riverbed at a speed that made stones leap aside as if reconsidering their commitments.

The span dropped six inches.

The mules screamed. The first wagon lurched, wheels half over the plank edge. A child cried from under the canvas. Not trade goods, then. People. The merchants had loaded families into covered wagons and claimed the disputed road before the moot could bind it. If the crossing succeeded, they would argue necessity. If it failed, the dead would become proof that roads needed owners.

Kesh reached the ravine post and cut the sale pennant with one slash.

Varrik shouted from above, "Do not cut the main line."

"I know roads," Kesh snarled.

"Then act like one."

That insult did something useful. Kesh stopped reaching for the knife again and pressed both palms to the cold route stone at the post.

"Who is ringing?" he demanded.

The bell answered in a child's voice Mara felt in her teeth.

Nim. South Bend. Age nine. Toll runner. Crushed under the third wagon. Still ringing because no one logged the washout.

The moot heard it.

Everyone heard it because the cinder economy had broken and the dead no longer had to speak only through sanctioned tools. Nim's voice ran along every route stone in the dry riverbed, thin, furious, and very tired.

Rikka fell to her knees at the post. "Nim was ours."

Kesh looked at her. "Yours?"

Her mouth twisted. "House debt. My mother's time."

The first wagon slipped another inch.

Mara wanted to sing. Wanted to hold. Wanted to command the route stones to brace. Instead she grabbed the mule harness with both hands and shouted to the family under the canvas, "Out the back. Crawl. Do not stand."

Caldus reached the wagon's rear and made himself a wall between panic and drop. Saelith pulled children into the dust. Tavi drove wire through two planks and around a wagon axle while explaining to no one that temporary engineering under moral duress should not be made precedent. Brakka arrived, planted her feet on the ravine side, and caught the span rope in both hands.

The entire bridge bowed toward her.

"Load is poorly distributed," she said through her teeth.

"I apologize for the road's lack of education," Kesh shouted.

Varrik had followed after all. She stripped the bone buttons from her green silk coat and threw them one by one to route runners. Each button unfolded into a coded marker. "House Fifth accepts emergency liability for the span until the wagon clears."

The refugee man with the burned toll scars grabbed one of the markers. "Can I witness that?"

Varrik looked at him for half a second. "Yes."

"Then I witness you waited until children were over the drop."

Her face went gray. "Witness accepted."

Together, they got the families off the wagons. Together, which was not the same as cleanly. One mule broke a leg and had to be killed. One trader tried to flee and was caught by Rikka's runners. A child bit Caldus hard enough to draw blood because terror does not respect rescue. The first wagon fell when it was empty, taking three planks and the sale contract into the ravine. The bell stopped only after Kesh lowered himself by rope and recovered a little brass clapper wedged in the post, green with old cinder light.

He climbed back up with Nim's clapper in his palm.

"No one logged the washout," he said.

No one answered.

"No one logged the child," he said.

Rikka stood. "I will."

"No," Kesh said. "We will. In the compact. First line."

They returned to the moot with dust in their teeth, rope burns on their hands, and one dead toll runner's name louder than every sale cord in the riverbed.

The second compact did not use the word ownership.

That took six hours, three near-fights, one actual fight, and Lora's soup arriving by wagon because hunger had begun sharpening everybody's philosophy. The old houses argued that a road without owner becomes neglect. Refugees argued that an owned road becomes a purse with corpses in it. Trolls argued that bridges ask about load, not title. Dark-elf observers asked whether hidden contracts would be public by default and were told by Rikka that anyone who liked secrets that much could sleep in the ravine. Tavi proposed a maintenance board; everyone hated the phrase board, so she renamed it a repair circle and claimed not to care.

At dusk, Kesh stood on the disputed stones with Nim's clapper tied to his cracked route token.

"First line," he said.

Rikka read it. "A road cannot be sold alone."

The riverbed answered with silence, the kind that tests whether words have enough bone.

She continued. "No house, captain, crown, merchant, army, refugee council, witness circle, or very persuasive thief may sell, close, tax, reroute, bind, bless, curse, or abandon a road without the road's named users being called to answer. Named users include maintainers, travelers, settlements served, those harmed by prior tolls, the dead recorded on the route, and any people present when the road is invoked."

"Very persuasive thief is unnecessary," Kesh said.

"It is legally clarifying," Rikka said.

"It is defamation in civic clothing."

"You asked for public trust."

"I asked for snacks."

"You got soup."

He considered. "Proceed."

The compact named Nim next. Then the wife who had died paying twice, and the mule, which led to a surprisingly heated debate about animal witness that ended with Brakka stating that loads did not become less real because they lacked grammar. It named maintenance obligations, toll disclosures, washout logs, emergency crossings, debt repair, and the right of travelers to see who profited before they paid. It required route-debt ribbons to show not just what was owed to houses but what houses owed back.

Varrik objected to almost all of it.

Then she signed.

The refugee man with the toll scars signed after her and did not forgive her. That was important. Forgiveness would have made everyone lazy.

Rikka turned to Kesh. "Your debts."

He had known it was coming. Mara saw it in the stillness of his shoulders. Jokes circled him like birds refusing to land.

Kesh untied three hidden ribbons from inside his coat. Not the public ones he had already shown. These were narrower, older, and worn soft from being touched.

"South Ash Bend," he said. "Wrong warning sold to Harrowmere riders. Correct river level sold to the same because I wanted them to trust the wrong warning. Result: patrol delayed, two road families spared, one farm searched instead. I owe the farm."

Rikka wrote.

"Glass Reed crossing. I took payment from both sides to keep a ford secret. Flood came early. Three dead who might have reached high ground if the ford had been public."

He tied that ribbon to the disputed stones.

"Kell Ashgate ash road. I guided tax men around a miners' strike because I thought the strike would fail and I wanted paid before it did."

Mara went cold.

Kesh did not look at her. That was how she knew the confession cost him. He looked at the road.

"The strike broke. People were taken. Some came back. Some did not. I told myself routes are not causes. That was convenient."

The dry riverbed held its breath.

Mara remembered hunger, smoke, the way Joryn had hidden children under slag carts, the tax men's boots on stairs. She had known many reasons for that failed strike. She had not known Kesh was one of them.

Saelith's hand found hers. Mara did not know whether she wanted comfort or restraint. She accepted both.

Kesh finally looked at her. "I owe Kell Ashgate."

"Yes," Mara said.

No one rescued him from the smallness of the word.

He tied the third ribbon to his token.

Rikka's voice softened by half a grain. "Do you accept road office?"

"No."

"Do you accept road answer?"

"Yes."

"Term?"

"Until Kell Ashgate releases the debt or changes its shape. Until Glass Reed names repair. Until the farm family answers. Until Nim's washout is rebuilt with his name. Then ask again."

Rikka wrote it all, including then ask again.

The old houses hated the compact and needed it. The refugees mistrusted it and needed it. Kesh signed with a hand that did not shake until after the ink dried.

When the last mark was made, the cold route stones did not blaze back into old magic. No green path unfurled toward safety. No cinder heat returned to make the roads wise on behalf of the living.

Instead, the disputed stones clicked softly as people moved them into a circle large enough to walk through.

The road reopened because people lifted what had been left in the way.

Mara stood beside Kesh while the first families crossed under the new rule. No toll bell rang. Nim's clapper hung silent from the route post, where it would be rung only for washouts, closures, and names missed too long.

"Are you angry?" Kesh asked her.

"Yes."

"Good."

"Do not make my anger useful to you."

He looked wounded, then thoughtful, which was better. "I will try."

"Try publicly."

"Cruel."

"Answerable."

He sighed. "I miss when you were easier to rob."

"No you do not."

His smile flickered, true and tired. "No."

Above the riverbed, stars came out over roads that no longer pretended freedom was the absence of knots. Freedom, Mara thought, might be the right knots tied where hands could reach them, the right bells hung where anyone could ring, the right debts named before the road curled onward and called itself clean.

The next morning, Kesh helped rebuild the ravine span.

He complained the entire time.

Nim's clapper did not ring once.""",
    39: r"""## Chapter 39: The Third Arch Opens

The Seven Arches crossed the star canyon in a procession of impossible stone.

At dawn, the canyon was violet shadow split by threads of white river so far below that sound arrived late and humbled. At noon, the stone shone iron-red and every carved oath along the parapets threw a black line of shade. At night, stars filled the depth as well as the sky, reflected in mineral pools and old glass veins until walking the bridges felt like crossing between two heavens while trying not to drop anything important into either.

The Third Arch had always been the narrowest.

That was one reason Brakka loved it.

The First Arch carried kings and armies because flat places attract those who believe weight is a compliment. The Second carried trade under a roof of toll bells. The Fourth was wide enough for dragon landing, though dragon consent had become a new and exhausting branch of bridge law. The Fifth and Sixth had shrine houses built into their piers. The Seventh carried funeral crossings, its stones polished by generations of hands saying goodbye.

The Third carried difficult people.

Exiles. Fugitives. Oathbreakers. Bridge children born during storms. Refugees whose papers had burned. Trolls who had lost standing and not yet earned a new place to put their feet. The Third had survived because it did not ask whether the person crossing was admirable. It asked whether the load could be borne, whether the crossing harmed those already on the span, and what repair would be owed after arrival.

That had been old law in small form.

Brakka had tried to make it large.

Now the elders had called her home to explain herself.

The elder ring sat on the eastern pier, carved directly into the arch root. Twelve stone seats, each marked by a load-song older than Harrowmere's first crown. Nine were filled. Two stood empty for dead elders whose names had not yet been lowered from office. The twelfth had once belonged to Brakka's teacher. It was empty because everyone present was too polite to say it had become the shape of the argument.

Mara stood behind Brakka with the company and approximately four hundred people who had come because a bridge trial sounded more stable than most governments. Saelith had brought a group of singers to learn load pauses. Ilyr and Maelin carried the Khar Veyl public record of refugee names. Kesh had three fresh rope burns and no permission to be near toll boxes. Tavi looked blissfully irritated by bridge mechanics. Caldus had taken charge of keeping Harrowmere soldiers from standing like an occupying force, which involved much eyebrow work.

At the western approach waited the first hard case.

They had not arrived as one group, but fear had sorted them together: a dozen Pale Remnant singers who had laid down knives after Saelith broke the old correction; seven Harrowmere soldiers who had enforced cinder seizures and now carried names of the taken; three goblin toll men from a house that had sold the South Ash Bend crossing; two dark-elf sealers who had locked public records during the flood in Khar Veyl; and a young dragon-shadow handler who had whipped a landing beast because his captain had told him fear kept small bodies alive.

Oathbreakers, by any ordinary measure.

Also people standing in wind with nowhere safe behind them.

Elder Granth of the Deep Foot spoke first. His voice made dust lift from the bridge seams. "The Third Arch is not a drain for every guilt that fears consequence."

"No," Brakka said.

Elder Surn tapped a stone nail against her seat. "You opened refugee law during war."

"Yes."

"War makes foolish openings look noble."

"Yes."

The elders shifted. Brakka's agreement annoyed them more than defiance would have.

"Do you understand," Granth said, "what it means if those who harmed refugees may cross under refugee law?"

Brakka's hands stayed open at her sides. "It means the law must learn repair or become purity theater."

Kesh whispered, "I am writing that down before someone ruins it with dignity."

Tavi held out a charcoal nub without looking.

An elder with quartz beads in her beard leaned forward. "Purity is not always theater. Sometimes it is the only clean cup left after poison."

Saelith's face tightened. Mara saw the sentence strike her. Light-elf mercy had loved clean cups.

Brakka bowed her head to the elder. "Yes. Some spans must refuse."

The western group heard that and changed shape. One Remnant singer began to cry. A Harrowmere soldier squared his shoulders as if rejection would at least be familiar. The dragon-shadow handler looked toward the canyon as if measuring whether falling might be simpler than waiting.

Mara's gift stirred at the edge of the arch. Not cinder command. Bridge memory. Stone remembered feet. The Third Arch remembered everyone who had crossed without being made admirable first: a mother carrying stolen grain, a troll child who had broken a shrine window, a human deserter with fever, a goblin who had lied about a toll and then saved three strangers in a storm, Brakka herself at nineteen, bleeding from a vow she had taken too early.

The arch did not forgive them.

It held weight while they crossed.

"Then why open?" the quartz-bearded elder asked.

Brakka looked at the western approach. "Because refusal is also a load. If we send every oathbreaker to ravines, forests, armies, and desperate roads, we do not keep the bridge clean. We move the weight to places not built to carry it."

The Third Arch hummed.

Low. Interested.

Granth's eyes narrowed. "The bridge likes your words. Bridges have liked foolish words before."

"Yes," Brakka said. "That is why we test with weight."

The test began at noon.

No one had expected it to be literal except everyone who knew trolls, which meant it absolutely was. The elders brought out load stones from the shrine vault: each one carved with a kind of harm. Blood Taken Under Order. Shelter Sold. Song Used To Silence. Name Sealed For Convenience. Road Closed For Profit. Beast Struck In Fear. Each accused crosser had to choose the stones that fit their harm and carry them to the center of the Third Arch.

"This is barbaric," one dark-elf sealer said.

Ilyr looked at the stone marked Name Sealed For Convenience. "It is also concise."

"I will not be shamed for obeying emergency protocol."

Maelin handed him the stone. "Then carry emergency protocol in public."

He nearly dropped it.

The first Remnant singer chose Song Used To Silence and Blood Taken Under Order. The stones were small by troll standards and brutal by human arms. She made it twenty paces before her knees shook. Saelith stepped forward, then stopped when Brakka glanced at her.

"May I walk beside her?" Saelith asked.

The elder ring murmured.

The Remnant singer looked horrified. "I hurt your people."

"Yes," Saelith said. "I am asking to walk, not absolve."

The singer nodded.

They walked. The bridge recorded both sets of feet.

One Harrowmere soldier refused the stone Blood Taken Under Order because, he said, he had never personally taken blood. Caldus asked him to name the houses emptied by his seizure list. The man named two, then stopped. Caldus waited. The bridge waited. Wind crossed the canyon and returned with no sympathy. At the fifth name, the soldier took the stone.

Kesh watched the goblin toll men choose Shelter Sold and Road Closed For Profit. "You forgot Cowardice With Excellent Margins."

Rikka, who had come for road witness, elbowed him. "Not a recognized stone."

"Yet."

The young dragon-shadow handler stood longest before Beast Struck In Fear. He was perhaps sixteen. His hands were scarred from reins meant for creatures larger than homes. "If I had not struck her, she would have crushed the landing crew."

Veyrasha, who had landed on the Fourth Arch after three hours of consent negotiation, lowered her head toward him. The entire eastern pier held its breath.

"What was her name?" the dragon asked.

The boy swallowed. "We called her Hook-Wing."

Veyrasha's eyes cooled. "That is not a name. That is an injury."

He flinched.

Mara hated the captain who had taught him. Hated the old systems that made children small enough to hurt beasts and then called their fear discipline. Hated that hating systems did not lift the stone from his hands.

"She did not give me another," he whispered.

Veyrasha was silent a long while. "Then carry Beast Struck In Fear and Name Withheld By Fear. If she wakes to answer one day, you will ask again."

The elders looked startled by the second stone. It had not been placed for him.

Brakka nodded to a bridge child, who ran to the vault and returned with a blank load stone. Tavi scratched the new name into it with an awl while muttering that she was not qualified for sacred engraving, which meant she did it carefully.

The crossings began.

Some failed.

That mattered.

The first dark-elf sealer reached the center of the arch, heard the record names below his feet, and tried to set down his stone without speaking the name of the woman whose testimony he had delayed. The Third Arch groaned. Hairline cracks flashed across the parapet. Brakka stepped onto the span and raised one hand.

"Bridge refuses."

The sealer went white. "You said oathbreakers could cross."

"I said repair could begin. You are still hiding the load."

"If I speak it, they will hate me."

Edda Mar, who had arrived with the Khar Veyl key-ring and no interest in pity, shouted from the crowd, "We already hate you. At least become accurate."

The sealer sank to his knees and said the woman's name.

The arch steadied.

He crossed the last half crawling.

No one cheered.

Mara was grateful.

Cheering would have mistaken survival for completion.

Then the canyon moved.

At first Mara thought it was thunder. The Third Arch gave a sound like a lung taking in too much air. Dust streamed from the underside. Brakka spun toward the western pier. Tavi swore in three languages. The old cinder heat leaving the Seven Arches had opened a fault in the support seam, and the day's living load had found it.

The center span dipped.

People screamed. The oathbreakers froze at midspan, each carrying stones. Refugees behind them surged, then stopped because a crush would kill faster than a crack. On the Fourth Arch, Veyrasha spread her wings and did not launch because no one had yet cleared her landing path. The elders stood as one.

Granth shouted, "Clear the span."

Brakka shouted, "No."

Every elder stared at her.

She planted herself at the center seam beside the trembling oathbreakers. "If they drop the stones and run, the bridge learns fear. If we drag them back, it learns purity. We carry the load through."

"It may fall," Surn said.

"Yes."

Mara had come to recognize the terrible honesty of yes. It opened no comfort and left no lie to lean on.

Brakka turned to the oathbreakers. "Name what you carry. Not for absolution. For balance."

The Remnant singer gasped, "Song used to silence."

Saelith answered, "Witnessed."

The Harrowmere soldier: "Blood taken under order."

Caldus: "Witnessed."

The goblin toll men, voices shaking: "Road closed for profit. Shelter sold."

Rikka: "Witnessed."

The sealer: "Name sealed for convenience."

Ilyr and Edda together: "Witnessed."

The dragon handler: "Beast struck in fear. Name withheld by fear."

Veyrasha's voice crossed from the Fourth Arch, huge and quiet. "Witnessed."

Each named load changed the bridge song. Not lighter. Plainer. Brakka lowered her shoulder against the fault seam as if she could hold the entire canyon together with stubbornness and a moral argument. Trolls along both piers began the old load hum. Not a perfect unison. The elders' voices were deep, the bridge children's high, Brakka's rough with strain, human and elf and goblin voices entering badly but entering.

Mara felt the Third Arch ask.

Not for command. For distribution.

She pressed one palm to the stone. "Who else carries?"

Hands landed all along the parapets. Refugees. Elders. Soldiers. Singers. Road families. Dark-elf archivists. A dragon claw on the Fourth Arch, carefully placed on a connecting pier after permission was shouted across the wind. The load moved outward. Cracks slowed.

Tavi slid under a brace line with wire clenched in her teeth. "I need three pins, two wedges, and someone heavy who can follow instructions."

Every troll within earshot looked offended at the singular.

"Fine," she said. "Several heavy people with humility."

Brakka laughed once, the sound nearly breaking under strain.

They saved the bridge the way most holy things are saved: with panic, muscle, names, math, and someone yelling that the next person who stepped on the repair line would be personally converted into an example.

By sunset, the Third Arch stood.

Changed.

The center seam had been opened, braced, and marked. A new stone line crossed the span where the fault had shown itself. On one side were the old load songs. On the other, the names carried that day, including the oathbreakers who had crossed and those refused until repair began. No one got to vanish into a category. The bridge would remember them as weight, harm, and possible next step.

The elder ring reconvened under stars.

Granth's face was unreadable. "Brakka of the Third."

Mara heard the title and knew it was being offered or taken away.

"You have opened old law beyond old bounds," Granth said. "You have placed strangers' repair inside troll standing. You have taught the bridge new load without full elder consent. You have risked collapse."

"Yes," Brakka said.

"You have also prevented us from lying about where refused weight goes."

The elders murmured.

Granth lifted the stone nail from his seat. "You lose standing in this ring for one year and one day."

Brakka bowed her head.

Mara took a step before she could stop herself. Saelith caught her sleeve again, which was becoming a sacred office.

Granth continued. "During that year, you will live on the Third Arch approach and hear every refused crossing. You will not rule the bridge. You will teach the repair circles you have inconvenienced us into needing. At year's end, the bridge children, the harmed, the elders, and those refused may answer whether you return to the ring."

Brakka lifted her head.

This was not exile. It was not acquittal either.

It was standing changed into work.

Her eyes shone. "Accepted."

The bridge children cheered because children had better timing than elders. The elders allowed it, which made the cheer suspiciously legal.

Later, when stars filled the canyon below, Mara found Brakka sitting at the midpoint of the Third Arch with her maul across her knees.

"You lost your seat," Mara said.

"For now."

"Are you all right?"

Brakka looked down into the star-filled depth. "I thought I wanted the ring to say I was right."

"And?"

"The bridge asked better."

Mara sat beside her. The stone still held the day's warmth where many hands had carried. Behind them, oathbreakers slept under guard and witness, refugees crossed in small groups, and Veyrasha spoke softly with the dragon-shadow handler about names that were not injuries. Ahead, the Third Arch remained narrow.

It would always be narrow.

That was part of its mercy. Not everyone could cross at once. Not every load could be carried in the same hour. But the arch stood open, and its openness was not softness. It was a hard, measured, public way of refusing to throw difficult people into places with no bridge at all.

"Again mattered," Brakka said.

Mara smiled. "It keeps doing that."

The canyon returned their voices late, gentled by distance, as if even echoes had learned to ask before becoming law.""",
    40: r"""## Chapter 40: Kell Ashgate Loud

Kell Ashgate announced itself by smell before sight.

Coal ash. Hot iron gone cold. Rainwater standing in slag pits. Lentils burning in someone's unwatched pot. The sour bite of old mine gas venting from cracks where cinder pumps had failed. Beneath it all, impossibly, grass. Thin green blades pushed through black heaps in stubborn patches, catching the wind as if the city had decided beauty was allowed only after proving it could survive poor soil.

Mara stopped on the ridge.

For most of her life, Kell Ashgate had been the shape of necessity: pit mouths, rope lifts, slag towers, company houses, ash roads, the crown weigh station, the furnace shrine where people prayed to heat that had not cared whether they lived. She had left it as an ash-runner with more fury than future, then returned in chains, then in rebellion, then as the girl people wanted to call witness, spark, saint, weapon, answer. Every road since had widened her until home became both smaller and more dangerous in memory.

Now Kell Ashgate lay below her under a gray afternoon, smoking, patched, loud enough that she could hear the argument from the ridge.

Kesh shaded his eyes. "Are they rioting?"

"Maybe," Mara said.

Joryn, who had ridden out to meet them on a mule that clearly outranked him, spat into the grass. "Council meeting."

Kesh brightened. "I love cultures with honest acoustics."

Joryn looked older. Not old, exactly. The mines aged people without the courtesy of years. His beard had gone iron-white at the chin, his left shoulder sat wrong from the chain yard fight, and one ear had a slice missing. But his eyes were the same: practical, irritated, more tender than he would ever admit while sober.

He climbed down from the mule and stood in front of Mara.

For a moment, neither moved.

Then he pulled her into a hug hard enough to hurt.

"You are thin," he said into her hair.

"I killed the old covenant."

"Did it not feed you?"

She laughed, then cried once, then hit his shoulder because anything else would have become too much.

Joryn held her at arm's length. "Do not look at me like you are asking permission to come home."

Mara swallowed.

"Home changed the locks badly," he said. "You can still get in."

That did worse things to her than any welcome speech could have.

They descended the ridge with the company behind them and no trumpets, because Kell Ashgate had used all available brass to repair pump fittings. The ash road had been dug open in five places. Children directed wagons around trenches with flags made from old tax notices. A row of inert cinder lamps hung outside the weigh station, each tagged with a name if known and a question mark if not. At the crown yard gate, where soldiers had once counted ore and bodies with equal boredom, someone had painted in tar:

NO HEAT WITHOUT ANSWER.

Under it, in smaller letters:

ALSO NO ONE TOUCH TAVI'S TEST PIPE.

Tavi stopped dead. "I have never been more honored or more concerned."

"Both are appropriate," Joryn said.

The council met in the old sorting hall because it was the largest roof that did not leak aggressively. Long tables made from mine doors filled the space. Miners, widows, pump hands, cooks, ash-runners, fever bridge families, children, two former crown clerks, one dark-elf archivist, three goblin road witnesses, and a dead cinder lantern in a cracked safety cage all shouted at once. At the far end, Edda Mar stood with Khar Veyl's key-ring on her belt and a hammer in her hand. Beside her, Selli, who had been twelve when Mara last saw her and now looked tall enough to accuse the sky, tried to record motions on a slate while being interrupted every third word.

The room did not fall silent when Mara entered.

This was the first proof that Kell Ashgate had improved.

People saw her, reacted, and kept arguing.

"If the pumps stay cold, the lower houses flood by winter," a pump hand shouted.

"If we bind Vessa back into the pump, I will drown the pump myself," Edda said.

"No one said bind."

"You said temporary heat."

"Temporary is a word."

"So is theft."

"So is pneumonia," someone else snapped. "My mother sleeps over a wet floor."

The cinder lantern flickered.

Every voice stopped.

Mara felt Vessa before she heard her: old coal warmth, a woman's patience worn down to a cutting edge, the memory of a pump room where the air tasted of iron and fear.

Do not argue around me, Vessa said from the lantern.

Edda's hand tightened on the hammer. "Aunt?"

The lantern warmed, not bright, just enough to put orange in the safety cage cracks.

I am not your aunt for decisions you want softened. I am Vessa Mar. I died in Pump Three. I was used after death without answer. I am willing to advise on pump heat. I am not willing to be installed.

The pump hand rubbed both hands over his face. "Advise how? We do not have enough coal. The old cinder lines are dead. The new pipe knocks itself apart. Children are sleeping damp."

Tavi stepped forward before anyone could stop her. "Show me the pipe."

Half the room shouted no, yes, who is she, absolutely not, and is that the gnome from the warning plates? Tavi smiled like a person being handed a festival.

Mara expected Joryn to ask her to speak then. To calm them. To explain the world after magic. To become useful. Instead he handed her a cup of water.

"Drink," he said.

"The council is-"

"Loud. Yes."

"Should I-"

"No."

She looked at him.

Joryn shrugged. "Unless you have become a pipe."

Kesh made a small reverent sound. "I like him."

The council split into working groups with all the elegance of a dropped toolbox. Tavi took the pump hands, Vessa's lantern, and six children who insisted they understood pressure better than adults because adults kept exploding things. Edda led the name-record circle. Caldus went to speak with former crown clerks about seized wages and emerged twenty minutes later looking as if he had aged three moral decades. Saelith joined a group of singers trying to replace cinder-warmed nursery rooms with bodies, blankets, and consented song. Ilyr and Maelin unrolled Khar Veyl copies of pump contracts on a sorting table, where miners leaned over them with coal-black fingers and a hunger that was not only for revenge.

Mara sat where Joryn put her: on an overturned ore crate near the door.

For the first hour, people came to stare and then remembered something urgent elsewhere. For the second, children approached in packs, dared one another to ask whether dragons smelled bad, and fled when Saelith answered with scholarly seriousness. For the third, old neighbors arrived with bread, accusations, blessings disguised as insults, and three different opinions about whether Mara looked like her mother, which was complicated because Mara had almost no memories of her mother's face.

One woman kissed Mara's forehead and called her the Ash Saint.

The sorting hall went dangerously quiet.

Mara stood.

Before she could speak, Selli climbed onto a table.

"Motion to ban Ash Saint," Selli shouted.

"Seconded," said Joryn.

"Thirded," said Edda.

"Can a motion be thirded?" Caldus asked.

"In Kell, if the first two are not loud enough," Joryn said.

Selli pointed at Mara with her slate. "Mara Venn is not a saint. Saints do not owe road debts, lose arguments, bleed on ledgers, or forget people's birthdays."

Mara blinked. "Whose birthday did I forget?"

"Mine," Selli said.

"I was in a death-dream."

"I accept late gifts."

The hall laughed. Mara felt the laugh enter places victory had not reached. It did not make her smaller. It made her less available to worship.

"Motion passes," Selli declared. "No Ash Saint. Other titles?"

"Pump hazard," Tavi called from under a table.

"Witness," Ilyr said.

Edda shook her head. "Witness is work, not title."

"Good correction," Ilyr said, and wrote it down.

"Mara," Joryn said.

The room settled around the name. Not silence. Agreement with enough elbow room for future complaint.

"Mara," Selli wrote on the slate. "Late gift pending."

Then the lower mine alarm sounded.

For one horrible breath, Mara was twelve again, running messages through ash while the ground shook and adults lied about how much time remained. The alarm bell clanged from Shaft Four, uneven and hand-struck. Not old cinder warning. Human panic.

Joryn was already moving. "Gas pocket."

Tavi rolled from under the pump table with a wrench in each hand. "If someone used my test pipe-"

"Wrong shaft," Joryn said.

The council became a rescue crew before anyone voted. That was Kell Ashgate's oldest law, written in lungs and rope burns. Caldus and Brakka took the heavy braces. Kesh and three ash-runners cut across the roof beams to drop signal cords. Saelith gathered singers, not to charm the gas, but to keep the waiting families breathing together. Edda carried Vessa's lantern to the shaft mouth. Mara ran.

The entrance to Shaft Four had slumped inward where rainwater and old heat loss had softened the supports. Two miners were trapped beyond the first fall. Gas seeped through the crack with a sweet, rotten smell. A crowd had formed too close.

"Back," Mara shouted.

Some moved. Not enough.

The old power rose in her like a remembered fever. She could make them move. She could put command into the cinder dust still clinging to Kell Ashgate's bones and push the crowd back before gas found flame. It would be easy because it would work.

Vessa's lantern flared.

Ask us, the dead miner said.

Mara turned to the crowd. "Who knows this shaft?"

Hands went up.

"Who can brace without sparks?"

More hands.

"Who is too angry to be careful?"

No hands, because people are people.

Joryn raised his.

Then Edda.

Then, slowly, three others.

"Good," Mara said. "You haul rope. Not tools."

The rescue became a shape made by answer instead of command. Brakka held the outer beam while two mine carpenters wedged a brace under her direction and corrected her once because troll strength did not know local rot. Caldus carried timbers and obeyed a fourteen-year-old ash-runner who told him where to put his noble shoulders. Kesh crawled through the ventilation cut with a signal cord tied to one ankle, cursing in a tone that meant he was frightened. Tavi built a hand fan from canvas, wire, and someone's best soup paddle, for which Lora would later demand structural compensation.

Mara lay flat at the crack and listened.

Not to command.

To hear.

Beyond the fall, one miner coughed twice. The other did not. Stone shifted. Gas pressed against Mara's nose until her eyes watered. In the dark under the shaft, tiny cold cinder remnants stirred. Old pump names. Dead heat. Vessa's panic.

Need task.

Mara closed her eyes. "Do you want to help vent without being bound?"

The cinder remnants fluttered.

Vessa answered for herself. I will show the old airflow. I will stop when asked. I will not hold the shaft.

Edda heard. Tears cut tracks through coal dust on her face. "Witnessed."

Mara repeated the terms loudly. The rescue crew answered one by one. Vessa's lantern warmed, and the gas moved, not because a dead woman became a tool again, but because she remembered where air had once gone and chose to point.

"Vent two," Joryn shouted.

"Vent two collapsed in winter," a carpenter said.

"Then open its ghost," Tavi snapped. "Sorry. Metaphor. Open the old cut."

They dug.

The first trapped miner came out coughing and alive. The second came out limp, then Saelith's singers and a mine healer worked over him while the whole shaft yard held its breath in one body. He woke angry, which everyone agreed was an excellent sign.

Only after both were clear did the old support fail.

Shaft Four folded inward with a roar that threw black dust into the sky. Brakka dragged two carpenters back by their belts. Caldus shielded a child. Kesh emerged from the ventilation cut gray with ash and announced that he had discovered several new religions underground and rejected them all.

No one died.

That was not the same as no cost.

Shaft Four was gone. Work would stop there for months, perhaps forever. Families who needed wages would need food. The city that had survived the crown, rebellion, cinder theft, and world-breaking magic now had to survive a ledger.

The council returned to the sorting hall dirtier and more honest.

This time, when people argued pumps, wages, closures, and repairs, Vessa's lantern sat in the center with a slate beside it.

Her terms were written first.

Kell Ashgate did not decide that night. Mara loved it for that. It did not turn rescue into consensus. It did not mistake no deaths for a plan. It shouted until midnight. It named debts. It assigned food stores. It voted emergency wage shares from crown-seized accounts. It scheduled a public review of every remaining cinder remnant. It asked Vessa whether she wished to advise the pump circle for nine days, and Vessa said seven, because death had not made her generous with meetings.

Near dawn, Joryn walked Mara to the old furnace shrine.

The shrine had changed. The crown seal had been pried from the lintel. The furnace mouth stood cold. Inside, where people had once fed offerings to the heat, someone had built shelves. On them sat tags, broken tools, names, lunch tins, bits of slag with finger marks, letters, and one ugly little clay figure of a mule.

"Memory room," Joryn said. "Not shrine."

"Who made the mule?"

"Selli."

"It is terrible."

"Aye. We honor accuracy."

Mara stepped inside. The cold furnace smelled of dust, iron, and old prayers that had lost their address. She found her own ash-runner tag on the second shelf, bent at one corner.

"I thought this was gone."

"So did we. Edda found it in the tax yard."

Mara touched the tag. The girl who had worn it had wanted out so badly that leaving had felt like the only kind of living. Now she stood in the room her younger self had hated, and the room did not ask her to stay small.

"Kell does not need me," she said.

Joryn leaned against the furnace wall. "Good."

It hurt.

He saw that because he had raised enough hungry children to recognize pain disguised as agreement.

"Needing you small was what the city did when it had nothing else to spend," he said. "We need you different now. Sometimes here. Sometimes gone. Sometimes wrong in public. Mostly eating when told."

"That is a demanding civic role."

"We are a serious people."

Outside, the council started shouting again about whether council benches should have term limits. Selli's voice rose above the rest, accusing someone of trying to make old chairs into new thrones. Tavi screamed from the pump yard that if anyone touched the test pipe without asking, she would teach the pipe to testify. Kesh laughed. Saelith's answering laugh followed, softer and nearer.

Mara stood in the cold furnace room and felt the shape of home change around her.

Not smaller.

Not safe.

Alive enough to argue without asking her to become its fire.

Before she left the room, she tied her old ash-runner tag to the shelf under a blank card. On the card she wrote one word.

Ask.

Joryn read it and nodded.

"Again?" he said.

Mara smiled through sudden tears. "Always."

At sunrise, Kell Ashgate rang every bell it had left. Not in unison. Not well. Some were cracked, one was a pan, and Nim's road clapper answered from the south gate where the new compact had been posted. The sound went up the slag heaps and over the grass patches, rough enough to make saints impossible.

Mara walked into the noise with coal dust on her face and no one kneeling.

It was the best welcome home she could have survived.""",
    41: r"""## Chapter 41: Room Under the Earth

The room under the earth had no throne because everyone who loved Mara had become extremely suspicious of chairs.

It had been a side chamber once, cut off from the old furnace tunnels below Kell Ashgate, too small for ore carts and too dry for pumpwork. Children had hidden there during tax raids. Ash-runners had used it to trade messages when the crown yard watched the streets. Later, Joryn had sealed it because the wall sweated cinder warmth and nobody trusted warmth that did not name its source. After the covenant broke, the sealed stones cooled. A draft began to move through them, carrying the clean mineral scent of deep water and black rock.

Mara found the room three days after Shaft Four fell.

She did not go alone.

That was one of the new rules she had not written but had grudgingly accepted. Saelith came with a lantern that burned ordinary oil. Caldus came because underground rooms made him stand straighter. Tavi came with a measuring cord, a pressure gauge, and three promises not to improve anything without permission. Kesh came because sealed rooms offended him personally. Brakka came last and had to duck through two doorways that had not expected troll grief to become part of their architecture. Ilyr, Maelin, Sava, Edda Mar, Joryn, Selli, and Vessa's lantern followed when word spread, which meant privacy became a local rumor.

"This is too many people for a secret room," Kesh said.

"Good," Sava answered.

The chamber walls were black stone veined with dull silver. No root-fire. No crown seal. No dragon scale hidden in the roof. Tavi confirmed this three times and looked disappointed each time, as if reality had failed to provide a worthy argument. At the back of the room, a narrow crack opened into darkness. Cool air breathed through it in slow pulses.

Mara stood before the crack and waited for the world to ask something of her.

Nothing did.

That frightened her more than command.

For years, there had always been a need louder than breath. Run the ash road. Find the heart. Hear the dead. Refuse the crown. Break the chain. Name the first wound. Choose against stillness. Even rest had arrived carrying orders disguised as mercy. Now the room offered no vision. No cinder plea. No dragon thunder. No dead advocate clearing his throat. No old lock pretending to be useful rubble.

Only air.

Saelith stood beside her. "What do you hear?"

Mara closed her eyes.

At first, she heard the others because the living are rarely as quiet as they think. Caldus's armor creaked. Tavi's gauge clicked. Kesh breathed through his mouth because he had been punched in the nose by history and several people. Brakka's fingers brushed the wall in a slow load rhythm. Sava's pen hovered above a page. Edda's key-ring tapped her hip. Joryn's bad knee cracked. Selli whispered, "That was loud," and was shushed by nobody because nobody wanted to become that sort of adult.

Mara listened deeper.

The cinders of Vael Taryn did not gather.

Some slept. Some argued in far places. Some had chosen rest and did not answer because absence was not abandonment. Some had become questions in public records, route stones, bridge seams, nursery songs, pump designs, trial circles, and names spoken before meals. A few still drifted, frightened by freedom, looking for tasks because tasks were easier than personhood. None pressed against Mara's skin and demanded a shape.

The room had space where a command might have been.

Mara began to cry.

No one rushed her. That was how she knew they had learned something.

Saelith asked after a while, "May I touch you?"

Mara nodded.

Saelith took her hand, and the room remained a room.

"I thought I would feel empty," Mara said.

"Do you?"

"No." She wiped her face with her sleeve. "That is the problem. I feel here."

Kesh made a strangled sound. "That is very inconvenient for anyone writing a legend."

"Good," Joryn said.

Sava wrote that down.

"Do not write that down," Kesh said.

"Too late."

The laughter moved through the small chamber and did not turn holy. Mara was grateful enough that she had to sit on the floor.

One by one, because living people cannot resist making a quiet room into a meeting, they sat with her. Not in a circle exactly. The room was too uneven. Caldus leaned near the entrance where he could see the corridor. Tavi sprawled by the wall crack and took readings with only moderate reverence. Kesh claimed a stone ledge and immediately complained it had been designed by enemies of circulation. Brakka sat cross-legged with her shoulders brushing both walls. Saelith stayed beside Mara. Ilyr and Maelin sat close enough for their elbows to touch and far enough to pretend it was accidental. Sava placed Arveth's closed-by-consent page in her lap. Edda hung the archive key-ring on a nail someone had driven into the wall years before.

Vessa's lantern warmed.

This room knows hiding, Vessa said.

Mara looked up. "Yes."

It knows children not breathing loud. It knows messages passed in coal dust. It knows fear waiting above.

Selli, who had been brave in the way teenagers are brave when adults are too tired to stop them, moved closer. "Does it know us now?"

The lantern flickered. If you tell it.

So they did.

It began badly, which was the only trustworthy way left. Joryn told the room about hiding seven children during the winter raid and lying to soldiers with a pot of burned beans in his hands. Edda told it about learning to hate the pump sound before she knew Vessa's name. Selli told it about wanting to leave Kell Ashgate and feeling guilty because everyone now acted as if staying was virtue. Tavi told it three structural concerns and one confession: that she missed the clarity of machines even though machines had been excellent hiding places for cowardice.

Kesh told the room he had sold the ash road once.

No one gasped because they already knew. That made the telling harder.

"I will answer Kell," he said. "Not today only. Not by paying a fee and becoming charming again. I hate that part, for the record."

"Recorded," Sava said.

"Cruel woman."

"Answerable man."

Brakka told the room about losing her elder standing and being relieved because standing had weighed less honestly than work. Ilyr told it about watching his mother hand archive keys to Edda and feeling pride, shame, and professional jealousy in the same ugly breath. Maelin told it she was afraid public truth would become another spectacle and more afraid that fear would make her close doors. Caldus told it about the first order he had obeyed after he knew obedience could be wrong. It was not a famous order. It involved moving hungry villagers away from a noble supply cart. He spoke the village name and did not look up until he finished.

Saelith did not sing.

That was her telling.

She sat in the room with her hands open and let silence remain unadorned. After a long while, she said, "I am going to Lumenorath again."

Mara's hand tightened before she could choose otherwise.

Saelith felt it. "Not to stay forever. Not to become proof. The broken harmonies have reached schools, and some teachers want to make them curriculum before anyone understands them."

Tavi winced. "Weaponized pedagogy. Terrifying."

"Yes," Saelith said. "I need to interfere."

"Good," Mara said, and hated that good could hurt.

Saelith looked at her. "Come when you choose. Do not come because my people become another wound only you can hold."

Mara swallowed. "Ask me again."

"I will."

The words settled into the chamber with more power than promises had any right to carry. Ask me again did not guarantee yes. It did not hide no. It kept the door in the sentence.

Caldus cleared his throat. "Harrowmere has requested that I return to assist with answerable oath reforms."

Kesh groaned. "Requested. Adorable."

"They used six seals and three apologetic phrases."

"So ordered with perfume."

"Yes," Caldus said. "I am considering ignoring the seals and answering the people who signed underneath."

Mara smiled. "Good."

He looked embarrassed. "I may need help refusing honors."

Joryn snorted. "Stand near Mara. It becomes contagious."

Ilyr said, "Khar Veyl's public circles are spreading. Badly."

"That is cheerful," Tavi said.

"I did not say badly was failure. I said badly because people are trying to do them without enough lamps, too many lamps, hidden moderators, public moderators, and in one case a trained actor reading atrocity records for dramatic pacing."

Maelin covered her face. "That actor has been banned from three halls."

"Only three?" Kesh asked.

"It is early."

Ilyr looked at Mara. "I am going back. My mother and Edda have not killed each other, which both consider progress. But there are sealed Orrowen records that need living and dead witnesses from outside Khar Veyl. Not you as authority. You if you choose. Later."

"Ask me again," Mara said.

Kesh looked offended by the pattern. "Everyone is going to start saying that now."

"Ask me again?" Selli tried.

"No, from you it becomes extortion."

"Late gift pending," she said.

Kesh nodded gravely. "See?"

Brakka would return to Third Arch before winter. Tavi would travel first to Brassroot, then Eastmere, where Hessa Wound-Binder's nine days of advice had become eleven because fever had poor respect for calendars and Hessa had revised her own terms twice. Kesh had road debts in three directions and repair work in five, which he described as persecution by geography. Sava would carry Arveth's closed page to Orrowen for one year, not to wake him, but to let the dead there see a mark that had been allowed to stop. Edda would stay in Kell Ashgate for now because the keys were heavy and because someone had to make archivists eat while they were being hated.

Veyrasha sent no representative.

She arrived herself.

The room under the earth could not hold a dragon, which prevented several theological complications. Her eye filled the upper shaft where a roof crack opened toward the slag yard. Everyone looked up at the sudden silver-black iris and made undignified sounds. Tavi dropped the pressure gauge. Kesh said a word that Selli immediately asked him to define.

"No," said every adult present.

Veyrasha's voice came through stone, amused and tired. "Othrava sends no command."

Mara stood.

"She sends her name when wanted, her absence when not, and a storm over the eastern sea because weather remains hers and she enjoys reminding ships."

Saelith smiled. "That sounds like her."

"Vorrakai's first trial circle has convened in the dragon courts," Veyrasha continued. "It is going poorly."

"Good," Brakka said automatically.

The dragon's eye shifted toward her. "That appears to be the mortal judgment on most honest beginnings."

"Often accurate," Brakka said.

"He has answered three names and refused two. Othrava refused to let refusal end the hearing. The third name was Eron."

The room stilled.

Mara felt the first forced chain again: mud, grief, a mother's need, a child's name turned into machinery. Not as command. As memory with a place to stand.

"Did he say it?" she asked.

"Yes," Veyrasha said. "Badly."

Sava wrote: Vorrakai said Eron badly. Trial continues.

No one improved it.

Veyrasha lowered her voice. "The dragon courts ask whether Mara Venn will witness when mortal testimony is called."

Every person in the room looked at Mara and then looked away quickly, which was almost worse.

The old temptation did not arrive as glory. It arrived as usefulness with a tired face. She could go. She should go, maybe. Eron's name deserved every witness. Mortal records deserved someone who had stood in the lock. Dragons would twist themselves into high language if no one brought mud into the court.

And if she said yes too quickly, the world would learn again that Mara Venn could be summoned by any wound large enough to sound like duty.

She took Saelith's hand.

Then she looked up at Veyrasha. "Ask me again after the first mortal circle forms without me."

The dragon blinked once.

Kesh exhaled like a man watching a knife miss his favorite organ.

Veyrasha bowed her eye. "I will carry that answer."

"It is not no," Mara said.

"No," said the dragon. "It is a door with a guard who has finally been allowed to sleep."

The eye withdrew from the crack, and ordinary gray light returned.

For a long time, the room said nothing.

Then Selli whispered, "Does the dragon owe me a late gift too?"

Joryn pointed at her without looking. "Do not start diplomacy."

The laughter after that had too many tears in it, but it was laughter.

When the others left the room, they did it slowly. No one wanted to be first because first departures make endings visible. Caldus went when a messenger from the wage circle found him. Tavi went because someone had touched the test pipe and survived only technically. Kesh went because Rikka had arrived at the south gate and was asking whether hiding counted as travel. Brakka went to help lift a collapsed brace. Ilyr and Maelin went to copy Vessa's terms in a form pump hands could read. Sava went last before Saelith, pausing at the doorway with Arveth's page in her hands.

"I keep expecting him to object," Sava said.

Mara looked at the blank page.

"I do too."

"Does that mean we failed to let him rest?"

Mara listened.

No papery voice. No dry correction. No dead advocate using absence as a trick. Only the quiet left by someone whose no had been honored.

"No," Mara said. "It means we miss him."

Sava pressed the page to her chest. "Good."

"Everyone keeps saying that."

"Everyone is learning."

She left.

Mara and Saelith remained in the room under the earth with the ordinary oil lantern between them.

For a while, they did not discuss kingdoms, roads, records, dragons, mines, pumps, schools, trials, oaths, or the moral dangers of chairs. Saelith leaned back against the black stone and closed her eyes. Mara watched the lamp flame move in the draft.

"What do you want?" Saelith asked eventually.

Mara almost answered with work. That was the old habit. Go to Lumenorath. Go to Khar Veyl. Go to Harrowmere. Go to the dragon courts. Go wherever the wound was loudest and make herself the first bandage. She had done enough of that to know it could be love and vanity in the same coat.

So she waited for the room.

It offered air.

"Breakfast tomorrow," Mara said.

Saelith opened one eye. "Ambitious."

"Then a walk to the upper grass. Then I should help Joryn with the wage board because he will pretend numbers are weather and suffer them bravely. Then sleep. Then maybe the south road in a week."

"Only maybe?"

"Ask me in a week."

Saelith smiled. "I can do that."

Mara touched the Kell cloth at her wrist. Inside it were onion skin, ash dust, a fiber from the Kavik road ribbon, a flake of bridge stone, a shadow-blue petal long since dried, and a little blank space where she refused to put a crown shard, a command token, or anything that wanted to become proof. The cloth was filthy, overfull, and hers.

"Will you come?" Mara asked.

"On the walk?"

"The south road. Later. If you choose."

Saelith was quiet long enough that the answer remained free.

"Ask me in a week," she said.

Mara laughed, and the laugh did not break anything.

They climbed out of the room near dusk.

Kell Ashgate waited above them in all its unpolished mercy. The pump yard clanged. Someone cursed creatively at a valve. Children chased one another between grass patches on the ash heaps. The council bell rang twice, stopped, then rang again because whoever held the rope had no rhythm. Smoke from ordinary wood fires moved over the roofs. No cinder lamps burned. In their place, people carried oil, coal, lantern glass, and the irritation of having to remember fuel.

At the south gate, a new board listed roads open, roads closed, roads under answer, and roads nobody trusted yet. Nim's clapper hung beside it. Beside that, Selli had added a smaller board titled Gifts Owed To Me By Important People. Mara's name was first. Veyrasha's had been added in ambitious lettering.

"She will become mayor," Mara said.

Joryn, passing with a sack of nails, said, "Not if the city survives."

"That sounded like pride."

"It was dread."

"Same root, in Kell."

He grunted because she was right and he hated that in public.

They ate in the sorting hall that night. Not a feast. Feasts required surplus, and Kell Ashgate had opinions about pretending. There was soup with too many onions, bread with one burned side, pickled root, weak beer, and a small honey cake Selli guarded until Mara admitted three times that forgetting her birthday had been a serious diplomatic failure. Saelith sang no formal song. Kesh cheated at dice and was caught by a child. Caldus listened to miners explain why armor was impractical underground and took notes. Tavi fell asleep with her head on a pump diagram. Brakka carried benches as if furniture had finally found an honest vocation. Ilyr spilled soup on a copied record and was forced by Edda to write Soup happened in the margin.

Mara sat among them and was not at the center of the room.

That was how she knew the ending had begun to live.

Later, under stars half-hidden by smoke, she walked to the upper grass with Saelith. The ash heaps rose black around them. New blades shivered in the night air. Far off, one of the mine vents breathed cool instead of hot. The world after magic was poorer in miracles and richer in questions. Its roads were slower. Its songs cracked. Its records angered. Its bridges demanded work. Its dragons faced trial badly. Its dead chose rest, witness, confusion, or complaint. Its living kept reaching for old shapes and sometimes caught themselves in time.

Mara did not feel chosen.

She felt tired, scarred, loved, watched, corrected, and free enough to be uncertain.

"There will be another crisis," Saelith said.

"Yes."

"Someone will say only you can answer."

"Yes."

"They will be wrong."

Mara looked at Kell Ashgate below, every window an ordinary argument with the dark.

"Sometimes I will answer anyway," she said.

"I know."

"Not first every time."

"Good."

"Not alone."

Saelith took her hand. "No."

They stood until the night wind carried up the city's noise: a bell, a laugh, a quarrel, a child calling for someone to wait, a hammer striking metal, Vessa's lantern voice faintly correcting a pump hand who had tried to skip a step, Joryn shouting that soup was not a philosophy no matter what Lora claimed, Kesh insisting that debt repair should include hazard pay for emotional growth.

No command rose beneath it.

No throne waited in the earth.

Only room.

Mara turned toward the south road, not to leave yet, not to promise, only to see where it began. The road was dark beyond the gate. It would ask things of her. She would ask things back. In the morning there would be breakfast. In a week, maybe travel. In a year, maybe dragon court. In ten years, perhaps a child would ask why the woman in the old stories kept refusing chairs, and someone would answer badly enough to keep the truth alive.

For now, Mara Venn stood on the ash heap grass with Saelith's hand in hers, the world unfinished around her, and the cool dark under the earth making space instead of law.

For now, that was enough.

In the city below, the council bell rang a third time.

Mara laughed.

Then she went down to answer only what was hers.""",
}


WORD_FLOOR_DEEPENING: dict[int, str] = {
    37: r"""The next morning, the public dark tried to become a program.

That was when Mara understood how fast repair could learn bad habits.

Someone had copied Sava's first rule onto clean boards and hung them outside three reading halls. No sealed record is opened alone. Beneath the rule, a clerk had written schedules, seating arrangements, queue markers, speaker categories, response times, and a polite reminder that disruptive grief would be moved to the side chambers for facilitation. The handwriting was beautiful. The problem was not cruelty. The problem was efficiency arriving before trust could catch its breath.

Edda Mar read the board twice, took it down, and broke it over her knee.

The clerk made a strangled sound. "That was the public procedure."

"It was a fence painted like a door."

Ilyr's mother, who had been walking with a bruise darkening along one cheek, looked at the broken board and said, "The side chambers were my idea."

Edda turned to her.

The old archivist did not flinch, which Mara respected and distrusted in equal measure. "I told myself some people would need quiet to speak."

"Some will."

"I also told myself the main hall would become unmanageable if grief entered without order."

"It will."

"And I would have used that as proof that those already trained in order should remain nearest the records."

Edda nodded once. "That is the part I heard."

No one clapped. No one forgave anyone. But the broken board stayed on the floor long enough for passing citizens to see what had nearly happened by accident. Sava wrote a second rule under the first, directly on the stone wall because boards were apparently suspect.

Procedure must answer to the harmed before it protects itself.

Kesh appeared with breakfast rolls he had obtained through methods no one wanted recorded. "This wall is becoming aggressive."

"Good," said three people, and then looked annoyed at having become a chorus.

The public circles that followed were slower and stranger. One record named a dark-elf physician who had smuggled Orrowen children through a plague tunnel, then hidden the children under false names that later prevented their descendants from claiming kinship. The physician's granddaughter wanted honor. The descendants wanted names back. An Orrowen lantern wanted to know why no one had asked the children whether safety required erasure. The answer was that they had been too young. The counteranswer, spoken by a child sitting in the front row with both feet swinging, was that young people were often used as an excuse by adults who liked decisions quiet.

The room had to stop for water after that.

Another circle opened a Lumenorath exchange in which Khar Veyl archivists had accepted copies of mercy songs known to suppress panic. Saelith sat with the singers and did not defend beauty. Maelin read the song names aloud. One light-elf elder began to explain that the songs had saved field hospitals, then heard her own tone and stopped.

"They did save some," she said at last. "They also hid others. I want the record to say both because I am afraid my people will choose the half that lets us sleep."

Ilyr wrote that in the margin himself.

By evening, the old archive had developed a new sound. Not the sealed hush Mara had heard when she first entered Khar Veyl, and not the scream from the flood of records. This sound was rougher: pages turning, lamps being cupped and uncupped, people asking whether a name could be said, people saying no, people saying yes and regretting it, children carrying water, Edda arguing over key custody, Ilyr's mother correcting a clerk and then correcting herself for correcting too quickly.

Mara stood in the passage outside the first hall, listening.

Ilyr came to stand beside her.

"I used to think the dark made us careful," he said.

"It can."

"Yes. That is the infuriating part. Some old practices were wise before power found them useful."

Mara thought of cinder heat, bridge law, road knots, songs, oaths, every tool that had begun as mercy and learned to bite. "Then the practice answers too."

He smiled faintly. "You make everything stand trial."

"No. I make everything answer breakfast questions."

"A harsher court."

From inside the hall, Edda shouted that if anyone scheduled grief into fifteen-minute blocks again, she would introduce the schedule to a hammer. Ilyr's mother replied that the hammer would need a sign-out ledger. Edda said the hammer answered to the harmed.

Ilyr covered his face.

Mara laughed.

Khar Veyl did not heal. Not in a day. Not because doors had opened, keys had changed hands, and princes had bled where people could see. But the under-realm's darkness had altered. It no longer belonged entirely to those who knew where lamps were kept.

That was not redemption.

It was a public place to begin being hated without hiding.

For Khar Veyl, Mara thought, that might be the first honest sunrise they could bear.""",
    38: r"""The South Ash Bend compact reached its first loophole before the ink dried.

This improved everyone's respect for it.

A merchant named Pol Trevish announced that he had not purchased the road, closed the road, taxed the road, rerouted the road, or abandoned the road. He had merely purchased exclusive rights to the shade cast by the west-side cliff between noon and third bell, which happened to be where travelers stopped before the ravine span. Anyone wishing to rest in that shade could pay a shade consideration. Anyone who did not wish to pay could continue walking in the sun and enjoy what he called their theoretical freedom.

Kesh looked at Mara. "Do you see why I dislike honest criminals? They bring paperwork."

Rikka did not smile. "Shade serves the road."

Pol Trevish spread his hands. "Shade is not road."

The old houses watched closely. The refugees watched harder. This was how bad systems returned, Mara realized: not always by repealing the new rule, but by discovering which nearby thing the rule had forgotten to name.

Kesh climbed onto the disputed shade rock and rang Nim's clapper once.

The sound was small in the dry riverbed. It did not summon magic. It summoned attention, which was more difficult to control.

"Witness question," Kesh said. "Who has used this shade?"

Hands rose: refugees, route runners, mule handlers, a troll bridge-child, two house guards, one dark-elf observer embarrassed to be included, three children who admitted they had used it mostly to avoid chores.

"Who maintained it?"

No hands.

A woman at the back said, "My sons cleared scorpions last spring."

"Names?"

She gave them.

Rikka wrote.

"Who was harmed when shade was denied?"

At first no one moved. Harm sounded too large for heat, pride, discomfort, a place to sit. Then an old man lifted his hand. His wife had fevered during the first flight from the war. They had stopped in that shade because she could not stand. A house guard had moved them along for unpaid rest rights. She had lived, he said, so perhaps it was not harm. The silence afterward corrected perhaps without anyone speaking.

Pol Trevish cleared his throat. "I did not own the shade then."

"You wanted to own the shade after knowing such ownership could matter," Rikka said.

"Everything matters if someone tells a sad story around it."

Mara saw Kesh go still.

For once, he did not answer with a knife, joke, or bargain. He stepped down from the rock, walked to Pol Trevish, and held out Nim's clapper.

"Ring it," Kesh said.

The merchant frowned. "Why?"

"If shade is not part of the road, ring the road bell and say so to the dead toll runner who kept warning travelers at this ravine after everyone forgot him."

Pol looked at the clapper as if it had become dirty.

"No? Then I will." Kesh rang it again, softly. "Nim of South Bend, the compact forgot shade. We are asking whether the road includes rest."

No cinder voice answered.

That mattered too.

The dead were not bells to be rung until policy improved. Kesh waited anyway, letting the non-answer stand in public.

Finally the old man whose wife had fevered said, "A road without rest is a trap with distance."

Brakka, from the bridge delegation, grunted approval. "Load requires pause."

Tavi wrote that down and muttered, "I hate when poetry is structurally sound."

The amendment took an hour. It named shade, wells, safe pull-offs, warning posts, and places where travelers waited for the injured, young, old, sick, grieving, or merely exhausted. Not every resting place could be free of obligation; someone still had to clear scorpions, repair roofs, and haul water. But no one could sell rest without calling those who used it and those who maintained it. No one could price exhaustion as if exhaustion were consent.

Pol Trevish refused to sign.

The compact allowed refusal. It also allowed public notice. By sunset, a board at the shade rock read:

Pol Trevish claims private shade rights here. Claim unanswered by users, maintainers, and harmed. Travelers may rest. Donations for scorpion clearing to Widow Am Ren and sons, not to Pol.

Kesh admired the board for a long time.

"It is mean in a lawful way," he said.

"That is the dream," Rikka answered.

That night, around cookfires in the riverbed, goblin children played road-moot. One child tried to sell moonlight. Another objected that moonlight was a sky road and therefore required bird witness. A third, playing Kesh with insulting accuracy, claimed emotional damages and stole everyone's beans.

Mara sat with Saelith and watched Kesh pretend not to watch them.

"Do you think it will hold?" Saelith asked.

"The compact?"

"Yes."

Mara looked at the boards, the stones, the scorpion-clearing donations, the exhausted old houses, the refugees sleeping in unsold shade. "No."

Saelith turned to her.

"Not by itself," Mara said. "It will tear. People will find shade rights, air rights, grief rights, every clever edge. Then someone will ring a bell or break a board or call a circle, and they will mend it if enough people still care."

"That sounds tiring."

"I think that is what alive means when nobody gets to be a god."

Kesh came over then, holding three bowls of beans he had definitely not earned.

"I heard godhood was discussed," he said. "I remain opposed unless it includes flexible repayment terms."

Mara took a bowl. "You owe Kell."

"Yes."

"And Glass Reed."

"Yes."

"And the farm."

"Yes."

"And Selli says you owe her birthday money on my behalf because you encouraged my bad habits."

He looked betrayed. "That child is a road house in human form."

"Sign here," Saelith said, offering an imaginary ledger.

Kesh laughed and, after a heartbeat, let the laughter fade into something quieter. "I will go to Kell with you."

Mara looked at him.

"Not to be forgiven," he said. "Do not make that face. I have seen forgiveness. It asks too much of the person who did not create the debt. I will go to be inconveniently accurate."

"Good."

He winced. "You all have made that word unbearable."

Nim's clapper moved once in the night breeze, silent because no hand rang it.

The road did not glow.

It waited, which was better. Waiting meant travelers would have to keep arriving with questions. Waiting meant no compact could become holy without first surviving a child trying to sell moonlight.

Mara slept beside the dry riverbed and dreamed of roads that curled away from every throne.""",
    39: r"""Brakka's first day without elder standing began before sunrise.

The Third Arch approach had no proper house for her because no one had decided whether her new work was punishment, office, apprenticeship, exile, or an architectural inconvenience. Bridge children solved the problem by dragging three awnings, two benches, a cracked shrine screen, and someone's laundry frame to the western pier. The result leaned in four directions. Tavi inspected it and declared that it held together through social pressure. Kesh offered to sell shares in it. Brakka sat beneath the awning with solemn dignity until the laundry frame fell on her head.

The children screamed with laughter.

Brakka removed the frame, considered the crowd, and said, "Structure requires revision."

This became the first lesson.

By midmorning, the approach had become a repair yard. Oathbreakers who had crossed the previous day worked beside people they had harmed or people appointed to stand in for the absent harmed. The work was not symbolic, which annoyed several former officials who had hoped for ceremonies. Stones needed moving. Brace lines needed tightening. The new fault seam needed a drainage channel before winter ice made it widen. Refugees needed a sleeping wall. Someone had to cook. Someone had to ask the dragon-shadow handler whether he was eating or merely holding food near his face out of obedience.

Brakka noticed Mara watching him.

"Go," she said.

Mara blinked. "What?"

"You are about to turn concern into hovering."

"I was not."

"Your feet disagree."

Mara looked down. Her feet had, in fact, moved toward the boy.

Brakka pointed her maul toward an elderly troll woman teaching two Remnant singers how to listen for load notes in a rope. "There. Hover where education can resist you."

Mara obeyed, offended and grateful.

The elderly troll was named Ossh of the Underbrace. She had no patience for remorse that did not improve hand placement. "If you pull against the rope, you fight the bridge. If you pull with it, you flatter yourself. Listen first."

One singer closed her eyes.

Ossh tapped her knuckles. "Ears open. Eyes open. Shame loves darkness."

Saelith, nearby, repeated the phrase under her breath. Mara knew it would find its way into Lumenorath, where it would make several teachers uncomfortable and therefore deserved travel.

At noon, the first refused crossing came.

A Harrowmere tax captain arrived with six armed retainers and a letter bearing three seals. He had escorted cinder seizures in the northern mines, then deserted after the covenant broke. Now he claimed refugee right because his own soldiers would hang him if he returned and the miners would kill him if he stayed on the road.

The Third Arch approach went quiet.

Kell Ashgate names had not yet reached this bridge, but Mara felt them in her teeth.

Brakka asked, "What stones?"

The captain looked at the load stones laid beside the approach: Blood Taken Under Order, Shelter Sold, Name Sealed For Convenience, Road Closed For Profit, Beast Struck In Fear, and several new blanks from the day before. "I request review by rank equivalent."

No one moved.

Mara almost laughed because rank equivalent had arrived at the Third Arch wearing polished boots.

Brakka said, "Bridge does not know that song."

"I commanded under crown law."

Caldus stepped from the crowd. His face had gone still in the old knightly way, but his voice did not. "Then I can hear your first statement, not as rank equivalent. As someone who knows the shape of the excuse."

The captain recognized him and paled. "Sir Caldus."

"No title needed here."

That cost Caldus. Mara saw it. Titles were not only vanity; sometimes they were handles people used to lift themselves through shame. He set his down anyway.

The captain chose no stones.

The bridge refused before he stepped onto it.

Not dramatically. A single crack opened across the approach, thin as a drawn line. Wind came up from the canyon and pushed his sealed letter out of his hand. It skittered to Mara's boot. She did not pick it up.

Brakka's voice remained even. "You may stay on the west approach under guard and witness. You may send for those harmed. You may name one action without excuse before sunset. You may not cross today."

"They will kill me on the road."

"Then you should be grateful the road is asked to answer now too."

The captain stared at her. "This is not mercy."

Ossh of the Underbrace snorted. "At last, a student."

Mara expected the captain to rage. Instead his face folded in on itself. He looked suddenly like a man who had run out of procedures before running out of fear.

"I ordered a boy whipped for hiding his father's pick," he said. "The pick was all they had left to sell."

Caldus closed his eyes.

Brakka lifted a blank stone and set it before him. "Name it."

The captain's mouth worked. "Hunger punished as theft."

Tavi, who had been repairing a brace line, stopped and carved the words badly into the blank.

He did not cross that day. No one pretended one named harm outweighed the unnamed rest. But he slept inside the guard ring instead of on the open road, and the next morning a messenger left for the northern mines with his first statement and a request for harmed witness.

That evening, Brakka sat under the repaired awning, exhausted.

Mara brought her soup.

"You look like an elder," Mara said.

Brakka took the bowl. "Insult."

"Sorry."

"Accepted."

They watched the Third Arch in twilight. Refugees crossed in pairs. Oathbreakers worked until their hands shook. Bridge children chalked new marks beside old ones. The elder ring had sent no approval, but three elders had come to observe and stayed to tie rope. That was the kind of apology trolls considered least embarrassing.

"You lost standing," Mara said.

"I lost the part that wanted standing to make the work stop arguing with me."

"Does it?"

Brakka smiled into her soup. "No. It follows me with blank stones."

Below, stars woke in the canyon. Above, Veyrasha circled once, waiting for the landing signal instead of taking sky as permission. The Third Arch did not shine. It held.

Mara was beginning to love things that held without shining.

They were harder to worship.

They were easier to use without lying.""",
    40: r"""Kell Ashgate's second welcome came from the people who did not come to dinner.

Mara noticed the absences more than the bread. Empty places around sorting-hall tables had a weight no feast could hide: families still angry that their dead had not spoken, miners who thought the council had become another room for loud people, former crown clerks afraid of being named, old strikebreakers, young workers who wanted the lower mines reopened no matter what Vessa said, and people who simply had no strength left to attend history after a shift hauling water.

In the morning, she went looking for them.

Joryn found her at the south stair and handed her a basket.

"If you are going to meddle, bring food."

"I was not going to meddle."

"Basket."

She took it.

Saelith came because she understood the difference between witness and intrusion better every day and still worried Mara might forget it around home. Kesh came because one of the absent names belonged to the family from the strike he had betrayed. Caldus came until Mara told him armor at angry breakfast doors might create the wrong atmosphere. He accepted this with the tragic dignity of a man denied useful guilt.

The first door belonged to Taren Pell, whose brother had died in the chain yard uprising and whose father had informed for the crown. Taren opened the door, saw Mara, and nearly shut it.

Mara held up the basket. "Joryn said food."

"Joryn says many things to avoid saying sorry."

"Yes."

That earned her one inch of open door.

They sat on the step because Taren did not invite them in. His house smelled of damp wool and boiled root. Two children watched from behind a curtain. Saelith placed bread on the step and then moved back, making it clear the food was not payment for politeness.

Taren looked at Kesh. "I know you."

"You do."

"You guided tax men."

"Yes."

"My father gave names after they came."

Kesh swallowed. "I did not know that."

"Convenient."

"Yes."

Mara had heard Kesh talk through knives, dragons, toll houses, curses, debt circles, and flirtation with death. She had rarely heard him stop. He stopped now. The silence did not fix anything. It kept him from stealing the scene with charm.

Taren picked up the bread and tore it in half. "What do you want?"

Mara answered carefully. "To know what the council is missing."

"You."

The word struck mean because it was meant to.

"Not because you are special," Taren said. "Because everyone is busy arguing about the dead used in pumps and the living who resisted. No one wants to sit with those of us who come from people who did harm and were hungry too."

Mara thought of the Third Arch, of the tax captain naming hunger punished as theft. "What would sitting change?"

"Maybe nothing."

"Then may I sit badly?"

He stared at her, then laughed despite himself. "You always were strange."

"So I have been told by experts."

The children came out for bread.

By noon, the basket was empty and Mara had learned three things no council ledger had held. First, some informer families had been paid in coal chits that were now worthless, leaving children blamed for betrayals they had not chosen and hungry because the payment had vanished. Second, the lower-house flood would hit those families first because they lived in the cheapest damp. Third, several absent miners had found an untagged warm stone in an old shaft and were hiding it, not to restore the cinder economy, they said, but to keep babies from freezing.

Tavi's test pipe suddenly seemed less urgent and more urgent at once.

They found the miners near dusk in a roofless shed behind the slag mill. Five adults, one old woman, four children, and a warm stone wrapped in rags. When Mara entered, the oldest miner lifted a pick.

"No saints," he said.

"Banned by motion," Mara answered.

The pick lowered half an inch.

Vessa's lantern, carried by Edda after someone sensible fetched her, warmed at the sight of the stone.

The dead inside was not Vessa.

For a sick moment Mara thought it would be a child. It was not. The voice that came from the stone was slow, confused, and formal.

I was Deputy Weighmaster Coll.

Every miner in the shed recoiled.

Coll had signed seizure warrants. Coll had counted ore against food. Coll had vanished during the uprising, presumed dead or fled. Now his memory warmed a stolen stone in a shed full of children whose families he had helped starve.

"Break it," someone whispered.

"Use it," said someone else, just as quietly.

The old woman holding a baby began to cry. "He is warm."

There it was, the world after magic in one cruel object: a guilty dead man, a freezing child, a room full of people with no patience for clean answers.

Mara knelt outside the circle. "Coll, do you know where you are?"

Kell Ashgate, the stone said. Lower west district. Unauthorized heat retention.

A bitter laugh moved through the shed.

Mara closed her eyes. "Do you choose to provide heat?"

Pause.

Under what authority?

"None."

Longer pause.

That is irregular.

Edda made a sound between fury and grief. "He would."

Kesh crouched beside Mara. "Ask him who is cold."

Mara did.

The stone dimmed, then warmed again. Children. Widow Marret. Pell line. Informer kin. Strike kin. Lower west.

"Do you understand you harmed some of them?"

The stone went nearly cold.

No.

Then, after a time: Records unavailable.

Ilyr would have wanted to be there. Sava too. But the shed could not wait for perfect witnesses. Mara asked if Coll would enter public answer to learn the records before choosing further heat. The stone asked whether public answer was mandatory. Edda said no, then clenched both fists as if the no had cut her.

The stone remained warm.

I will answer for one night. Heat continues until morning. Then records.

Not enough. Still something.

The old woman pressed the baby closer to the wrapped stone and sobbed with shame because relief had arrived through a hated name. Saelith sat beside her without song. Kesh went outside and was quietly sick. Mara stayed until morning, when Coll's stone was carried to the sorting hall under guard, witness, and the baby's furious objection.

The council that day was uglier and better.

It added informer kin to food lists without wiping informers clean. It created a heat emergency circle that could accept consented dead help only by name, term, and review, with the harmed notified before honorifics attached. It assigned lower-west repairs before decorative memorials. It sent Taren Pell to argue on the wage board, where he immediately became inconvenient.

Near evening, Selli found Mara by the memory room.

"Your late gift can be this," she said, handing Mara a slate.

On it was written: People who do not come to dinner still count.

Mara read it twice.

"That is a good law."

"It is a terrible birthday gift."

"Yes."

"You still owe me."

Mara hugged her, and Selli allowed it for approximately three seconds before declaring oppression.

Kell Ashgate remained loud.

Now, at least, some of the quiet had been accused.""",
    41: r"""Before dawn, Mara woke in the memory room above the old furnace, not because anyone called her, but because no one did.

It took her a moment to understand why that felt strange. No cinder tugged at her blood. No messenger pounded on a door. No dragon filled the sky with terms too large for roofs. The city breathed around her in ordinary discomfort: a baby fussing in the lower west, a cough in the hall, rain ticking through a bad patch in the eaves, someone stoking an actual fire and muttering about wet kindling. The quiet had not become peace. It had become unsupervised.

Mara lay still under a blanket that smelled of smoke and borrowed soap.

Across the room, Saelith slept on a pallet with one hand tucked under her cheek. She looked younger asleep and less unreachable, not a singer out of legend, not a broken-harmony teacher, only a woman tired enough to trust a room that had once been a shrine to heat. Near the door, Joryn snored in a chair because he had claimed he was only resting his eyes before checking the wage board. Vessa's lantern sat dark on the shelf by consent. The ash-runner tag with Ask written beneath it moved faintly whenever the draft found it.

Mara got up without waking them and stepped outside.

Kell Ashgate before sunrise was not noble. It was damp, soot-streaked, and argumentative even in sleep. But at the upper edge of the slag heaps, grass held beads of rain so small they looked like bits of starlight dropped by an inattentive sky. She climbed to the place where the south road began and looked back.

For one terrifying, tender moment, she saw all of it at once.

Khar Veyl under dim lamps, learning that public darkness could reveal without owning sight. Kavik's dry riverbed, where roads waited to be amended by everyone clever enough to harm them and everyone stubborn enough to mend them. The Third Arch carrying refused people without pretending crossing was forgiveness. Lumenorath's grove opening crooked blossoms to bad songs and worse metaphors. Harrowmere scratching answerable oaths into stained paper. Orrowen holding Arveth's closed page like a candle no one was allowed to relight. Dragon courts beginning badly. Eastmere fever wards arguing with a dead healer who had earned the right to be inconvenient. Kell Ashgate, loud below her, counting absent dinner places and guilty warm stones.

None of it gathered into a crown.

Mara pressed both hands over her face and laughed once, shaking.

She had spent so long fearing that if she refused the single answer, the world would shatter. The world had shattered anyway, then remained. Poorly. Loudly. With leaks, debts, trials, bridges, soup, and children selling imaginary moonlight. Perhaps survival had never been the art of keeping the world whole. Perhaps it was the practice of making enough room that broken pieces could answer what shape they wanted next.

Footsteps crunched behind her.

Saelith came up the path wrapped in a blanket, hair loose, eyes half-open. "You left before breakfast."

"I came to check whether the road was still there."

"And?"

"Suspiciously."

Saelith stood beside her. They watched the first smoke lift from the sorting hall chimney. A bell rang once and stopped, as if embarrassed to have opinions before dawn.

"Do you want to go down?" Saelith asked.

Mara thought of the room under the earth, the road beyond the gate, the south, the dragon courts, every place that would eventually ask and every place that had to learn not to ask her first.

"Yes," she said. "Breakfast first."

Saelith smiled. "Heroic."

"Revolutionary."

They walked back as the city woke. No song rose under their feet. No hidden power approved them. The road behind waited. The road ahead waited. Waiting, Mara had learned, was not emptiness when no one had the right to fill it without asking.

At the memory room door, Joryn opened one eye. "You two done saving the sunrise?"

"It managed without us," Mara said.

"Good. Soup wants chopping."

Mara looked once more toward the south gate, where the first light touched Nim's clapper and the board of roads nobody trusted yet.

Then she went inside, took the knife Joryn handed her, and began with onions.""",
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
        'current_form: "full-length draft zero with Book Three chapters 1-41 revised in pass 01"',
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
    check_scaffold("\n\n".join([*CHAPTERS.values(), *WORD_FLOOR_DEEPENING.values()]))
    text = MANUSCRIPT.read_text(encoding="utf-8")
    revised = normalize_part_headings(replace_chapters(text))
    total = word_count(revised)
    if total < MIN_WORDS:
        raise ValueError(f"Revision would reduce Book Three below {MIN_WORDS:,} words: {total:,}")
    MANUSCRIPT.write_text(revised, encoding="utf-8")
    update_metadata(total)
    update_summary(total)
    print(f"Book Three chapters 37-41 revised. Word count: {total}")


if __name__ == "__main__":
    main()
