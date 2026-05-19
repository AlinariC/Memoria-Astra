#!/usr/bin/env python3
"""Revision pass 01b for Book Two chapters 7-12.

Replaces the Lumenorath scaffold with bespoke scenes: the coercive White Road,
the spell-fruit orchard raid, Saelith's trial, Mara's memory-rewriting hymn,
Serathiel's private mercy, and the cleansing decree that breaks diplomacy.
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
    7: r"""## Chapter 7: The White Road

# Part II: Lumenorath

The White Road began by correcting their footsteps.

Mara noticed it on the first pale mile, where mirror-bark trees leaned over the path and caught dawn on every silver trunk. The road looked like stone at a distance, smooth and luminous as a bone left under moonlight, but underfoot it had the faint give of living root. Each time she stepped crooked because her burned hand throbbed or her pack pulled wrong, the road softened, nudged, and tried to place her foot more gracefully.

She hated it immediately.

Kesh walked five paces before stopping. "The ground is flirting with my ankles."

"The road assists posture," Veyanna said.

"My posture has survived several authorities without assistance."

Tavi crouched and pressed a brass probe between two white seams. The probe chimed politely, then bent itself into a decorative curl. She stared at it. "That was my best rude probe."

"The White Road receives tools according to their highest form," Veyanna said.

"Its highest form was poking things."

Saelith had gone quiet.

Not the controlled quiet she wore before danger. A smaller quiet. She walked as someone who had once known where every root would rise, every mirrored trunk would turn, every dawn hymn would begin. The road made space for her without touching her boots. It remembered her body even after she had cut away its claim.

Mara slowed until Saelith matched her pace.

"It is beautiful," Mara said.

Saelith's face tightened. "Yes."

"You say that like you are apologizing."

"I love it," Saelith said. "That is worse."

The road climbed through a valley of mirror-bark. Each trunk reflected them differently. In one, Mara saw herself as she was: mud on cuffs, scarred palm wrapped badly, cinder cage at her hip, eyes too tired for awe. In the next, she wore white and walked with serene hands folded around a coal that did not burn her. In another, she was taller, cleaner, already carved into a statue's patience.

She looked away too late.

The cinder shard warmed.

Do you prefer the wound or the ornament? whispered a voice older than trees.

"Neither," Mara muttered.

Caldus heard. "Problem?"

"The scenery has opinions."

"So does the road." He lifted his staff and showed the bottom. White root had grown around it in a neat spiral, trying to mend the crack in the wood. "It keeps improving my property."

Brakka stopped at a milestone half-swallowed by root. Beneath the luminous bark, old troll marks showed through in dull amber.

"Road wearing road," she said.

Veyanna inclined her head. "Lumenorath preserves all paths it receives."

Brakka put one hand on the stone. "Does path consent?"

"Stones do not consent."

The troll looked at Mara. "People say same before cages."

The Pale Bough escort shifted. The three named dead beneath canvas shade stirred as if the road's hymn had reached even them. One, Edrin Vale, raised a stiff hand.

"The roots are asking us to rest," he said.

"Do you want to?" Saelith asked.

Edrin considered with the gravity of someone whose wants had been mislabeled by several regimes. "No. But it asks sweetly."

That was the danger in Lumenorath. Harrowmere had lied with ledgers, chains, and furnaces. Lumenorath lied with correct light. The road did not shove. It suggested until resistance felt like poor manners.

By noon, they reached the First Lyric Gate.

It was not a gate in any useful sense. No wall crossed the road. No guardhouse stood. Instead, seven mirror-bark trees bent toward one another, their branches braided overhead. A stream ran through the arch without wetting the path. White petals fell upward from the water and vanished among leaves. Beyond it, the realm opened in terraces of pale forest, suspended bridges, root towers, and coral gardens glowing in colors Mara had no names for.

The refugees behind her gasped.

So did Mara.

She did not want to. Wonder felt like surrender here. But Lumenorath was too much for pride. Towers rose from living root, not built on the hills but coaxed through them, balconies blooming with lantern flowers, windows clear as frozen rain. Walkways curved between trees with no visible support. Far off, a choir sang the hour, and the sound folded through the valley until even the mules stood straighter.

"Careful," Ilyr said.

Mara glanced at him. He looked ill.

"Light poisoning?" Kesh asked.

"Memory," Ilyr said. "They make it public here."

At the gate, Veyanna turned. "All who enter Lumenorath speak one truth they are willing to preserve."

"No," Mara said.

The word dropped like a boot in a ballroom.

Veyanna's leaf-veiled eye cooled. "It is custom."

"So is taxation. I dislike surprise versions of both."

"A truth freely spoken harms no one."

"Then it can wait until freely asked."

The gate's upward-falling petals slowed.

Saelith looked at Mara, something like terror and hope crossing her face. "The road will not open fully without a truth."

"It is open enough to see through."

"Not enough to enter."

Mara studied the arch. No bars. No wall. Just beauty pretending refusal was impossible. She thought of the road camp sign: EAT. SPEAK NAME. LEAVE FREE. The last two words mattered most.

She stepped off the White Road.

Her boot sank into ordinary mud beside the luminous path.

The Pale Bough escort inhaled as one. Kesh grinned. Tavi whispered, "Oh, that is socially explosive." Brakka stepped off after Mara, and the mud accepted her with honest squelching.

Mara walked around the First Lyric Gate through wet grass, thorny brush, and a drainage ditch that smelled like every other ditch in the world. The cinder cage bumped against her hip. Her trousers caught on brambles. Her boots collected several pounds of Lumenorath's less curated earth. When she reached the other side, she stood beyond the arch without having offered a truth for preservation.

The gate did not collapse. The towers did not dim. The realm did not end.

It only looked offended.

Kesh applauded once before Caldus caught his wrist.

One by one, the others followed. Caldus limped through the ditch without comment. Tavi lost a boot and declared the route scientifically superior. Ilyr moved through mud with dark-elf elegance sharpened into insult. Saelith hesitated longest, then stepped off the White Road and into the drainage ditch.

The mud took her white borrowed boot to the ankle.

She laughed.

It was small. It was shocked. It was not beautiful by Lumenorath standards.

Mara loved it.

Veyanna remained under the gate, face unreadable. "You enter without blessing."

"We enter with mud," Brakka said.

"Mud records honestly," Ilyr added.

Beyond the gate, a group of Elyri citizens had gathered along the terraces. Some stared at Mara with awe, some with dislike, some with the careful pity of people looking at an injury they believed should be covered. Children peered around white-robed adults. One child lifted a hand in shy greeting.

Mara lifted her scarred hand back.

The mirror-bark tree beside the child reflected her as the serene saint again.

The child looked from the reflection to Mara's mud-caked boots and frowned, as if deciding which version had lied first.

Good, Mara thought.

Let the realm start with a question.
""",
    8: r"""## Chapter 8: Fruit of Stolen Spells

The floating orchard was forbidden, which meant Kesh had found three entrances by supper.

"Forbidden is an emotional word," he said, spreading a stolen root-paper map across Tavi's work crate. "Architecturally, the orchard is more of a suggestion with guards."

The party had been housed in a guest hall grown from white root and mirror bark, with beds that adjusted to their bodies and windows that brightened if anyone whispered too angrily. Veyanna called it welcome lodging. Ilyr called it a cage with pillows. Brakka slept outside under a rain tree because the hall kept trying to straighten her spine.

Mara had not meant to raid anything on their first night in Lumenorath.

Then Vennic Reed-Quick, the Kavik scout, found the orchard registry.

The registry listed confiscated songcraft, hymn fragments, dream-spells, and "unstable folk workings" taken from border villages, refugee camps, and dead cities for preservation. Each entry ended with a fruit mark: pear, fig, pomegranate, moon-apple. Storage form. Not destroyed. Not returned.

Saelith read the list three times.

"These are not all dangerous," she said.

"Define dangerous in a society allergic to untidy grief," Ilyr said.

Her finger stopped on one line. "Children's rain-hymn, village of Leth-in-Mist. Confiscated after unsanctioned flood intervention."

Tavi leaned over. "A child sang rain away from a field?"

"Likely."

"And they put the spell in fruit?"

Saelith's face had gone pale. "They call it gentling. A working is removed from an untrained vessel and preserved until lawful use."

Mara thought of Mordane's ledgers, which had also preferred clean nouns.

The orchard hung over the east terraces, visible from the guest hall after moonrise. Root bridges curved into empty air. Silver pears drifted above them, tethered by threads of light to branches that grew sideways from no soil Mara could see. Pomegranates glowed red under translucent skins. Moon-apples orbited slowly in clusters, each holding a faint sound at its core.

Beautiful.

Again.

Always a warning.

Their objective was supposed to be simple: enter, copy enough registry marks to prove the Pale Bough preserved stolen workings, and leave before the dawn hymn. Tavi loved plans containing the word simple because, she said, they bloomed into evidence against optimism. Caldus assigned positions. Brakka refused the root bridge and climbed the terrace wall by hand. Ilyr became a shadow among white shadows. Saelith knew the old ward responses and hated that knowledge with every whispered instruction.

Mara followed Kesh onto the first floating bridge.

The bridge swayed without moving. It was like walking across a held breath. Below, Lumenorath's coral gardens glowed blue and green, and the streams between them carried reflected stars that did not match the sky. Farther down, beyond beauty's reach, dark service paths wound between root foundations. People moved there carrying waste buckets, pruning knives, and covered trays.

"There are servants," Mara whispered.

Kesh looked down. "There are always servants."

"No one mentioned them."

"That is usually how one identifies servants."

The first silver pear drifted near her face.

Inside its skin, a child's voice sang three notes and stopped.

Mara froze.

Saelith turned too late. "Do not touch the fruit."

The pear brushed Mara's burned hand.

The orchard vanished.

Rain hammered a field of green barley. A child stood barefoot in mud, no older than nine, singing at the sky because her father had fallen in the flooded ditch and the water kept rising. The song was wrong by every formal measure, cracked, desperate, alive. Clouds opened. Water bent away. Men shouted. Someone laughed. Then white-robed riders came three days later and told the village a miracle without law was a wound in the world.

The child's name was Liora.

Mara came back gasping with the taste of rain in her mouth.

The silver pear had dimmed.

Saelith caught her elbow. "What did you hear?"

"A girl saving her father's field."

Saelith closed her eyes.

Across the orchard, a bell chimed.

Not alarm yet. Inquiry.

Tavi's voice hissed from the bridge behind them. "The fruit noticed being accused."

Moonlight gathered into three wardens at the far platform. They were Elyri constructs grown from root and polished bone, faces smooth except for closed eyes carved over closed mouths. Each carried pruning shears as long as swords. The shears opened with a sound like polite applause.

"I dislike gardening," Kesh said.

The wardens moved.

The raid became vertical.

Kesh cut three tether-lines and sent silver pears floating into the wardens' path, each fruit releasing half a stolen spell when struck. One burst into kitchen fire that smelled of cinnamon and panic. Another unfolded a fisherman's net made of moonlight. A third released a grandmother's curse so specific that Tavi shouted, "I want that archived properly!"

Caldus held the narrow bridge while Saelith sang a counter-note that kept the wardens from calling the whole terrace awake. His staff cracked against pruning shears. White sparks fell into the gardens below. Brakka, hanging by one hand from the terrace wall, seized a root support and hauled herself onto the platform behind the constructs.

"Orchard has poor consent," she said, and broke the first warden in half.

Mara ran for the registry tree.

It grew at the orchard's center, a slender white trunk covered in hanging bark strips. Each strip bore names of seized workings written in luminous ink. Some had family names. Many did not. Too many said unknown origin, unsafe keeper, border dialect, pre-law practice, dead tongue.

Ilyr stood there already, copying with impossible speed.

"We need the Leth-in-Mist entry," Mara said.

"We need all of them."

"Can you copy all?"

He looked offended. "Eventually."

A warden's shears closed where his head had been. Mara grabbed a bark strip and tore.

The tree screamed.

Every fruit in the orchard opened its inner voice.

Hundreds of stolen spells cried out at once. Rain songs, birth charms, field blessings, fisher knots, grief keens, miners' heat calls, goblin road rhymes, troll bridge hums, dark-elf lullabies taken as contraband at old borders. The sound drove Mara to her knees. The cinder shard answered beneath it, translating too much, too fast.

Use them, whispered the old dragon grief. They were stolen. Make them useful.

No.

Not useful. Witnessed.

Mara pressed the torn Liora strip to her burned palm. "Liora of Leth-in-Mist sang rain aside to save her father," she said. "Not unstable vessel. Not unlawful miracle. Child. Witnessed."

The pear that had touched her hand split open.

Rain fell upward from it.

Not enough to flood. Enough to wet every bark strip within reach. The luminous ink ran. Names blurred, then reformed darker, less elegant, harder to edit. The registry tree shuddered as if a thousand preserved workings had remembered they were not fruit by nature.

"Mara!" Caldus shouted.

The bridge behind them was collapsing in graceful segments.

Tavi threw a coil across the gap. "Everyone admire the engineering after surviving it!"

They fled through raining spells.

Kesh slid down a moon-apple tether, laughing because terror sometimes chose bad doors. Saelith carried three bark strips under her coat and wept without slowing. Ilyr vanished and reappeared on the lower bridge with a bundle of registry copies. Brakka jumped from the platform into a coral tree that bent, complained in leaf-rustle, and launched her onto the service path.

Mara was last.

A warden caught her sleeve.

Its closed mouth opened for the first time. From inside came Liora's voice, gentled and perfect.

Thank you for preserving me.

Mara stopped running.

The warden raised its shears.

She put her burned hand on its smooth face. "That is not her."

The cinder did not flare. The stolen rain did.

Water filled the carved eyes. The root-bone softened. The warden fell apart into white twigs and a single pear seed.

Mara took the seed.

By the time they reached the guest hall, Lumenorath was awake with bells.

Veyanna waited in the doorway.

Her gaze moved over mud, torn sleeves, bark strips, Saelith's tear-streaked face, Tavi's smoking coil, and the pear seed in Mara's hand.

"You entered a preserved orchard unlawfully," she said.

"Yes," Mara answered.

Veyanna's mouth tightened. "Why?"

Mara held out the seed. It pulsed once with a child's stolen rain-song.

"Because beautiful theft is still theft."
""",
    9: r"""## Chapter 9: Trial of the Oathkeeper

Saelith's trial began at dawn with a hymn about clean hands.

That was not an accident. Nothing in the Pale Bough court was accidental. The chamber had been grown under the central root tower, circular and open to the sky, with white branches weaving overhead like ribs. Water ran in shallow channels through the floor, carrying fallen petals past the feet of judges, witnesses, and accused. Every voice in the room sounded better than it should. Even Kesh's muttered complaints acquired a formal resonance that annoyed him deeply.

Saelith stood in the center without her gray travel coat.

They had taken it from her at the door and offered white robes. She refused the robes. So she stood in a plain linen shirt, travel-stained trousers, and boots still marked with ditch mud from the First Lyric Gate. Her cut-away clasp scar showed at her throat.

Mara stood behind the witness rail with Caldus, Kesh, Tavi, Brakka, Ilyr, Vennic, Bessa, and the three named dead. Veyanna stood opposite them in white, her leaf-veiled eye bright with sleeplessness. Above the court, on a living dais, Serathiel sat beneath a branch of the Pale Bough.

In person, the saint-general was harder to hate.

She had no obvious cruelty in her face. That made Mara wary. Cruelty often announced itself badly. Conviction knew how to dress.

The first judge sang the charges.

"Saelith Dawnmere, oathkeeper of the Pale Bough, is called for breach of clasp, unsanctioned travel, counter-hymn against lawful escort, interference with preservation bells, companionship with declared hazard, and unlawful witness of confiscated workings."

"Declared by whom?" Mara asked.

Every head turned.

Caldus leaned close. "Usually one waits to be recognized."

"I dislike giving bad ideas time to settle."

Serathiel's gaze rested on Mara. "Mara Venn may speak when called."

"Then call me before the lies get rhythm."

A ripple moved through the court. Not laughter. Lumenorath did not waste surprise so openly.

Saelith turned just enough for Mara to see her profile. "Mara," she said softly. A warning. A plea. Not stop. Be careful.

Mara bit down on the next words.

Veyanna stepped into the water channel. "The accused does not deny the acts."

"I do not," Saelith said.

"You cut your clasp."

"Yes."

"You used restricted melody on the White Road."

"Yes."

"You entered the Orchard of Held Workings and removed preserved spell records."

"I carried stolen names out of a theft."

Veyanna's voice cooled. "The court will determine language."

"That," Saelith said, "is why I used mine quickly."

Mara felt fierce pride rise in her, bright enough to be dangerous.

The trial unfolded like embroidery over a wound. Witnesses spoke in formal sequence. Veyanna produced the cracked hymn bell from the quarry and argued it had been altered by unauthorized contact before inspection. Tavi nearly climbed the witness rail. Caldus held her by the back of her coat.

"Unauthorized contact is how inspections happen!" Tavi hissed.

"Later," Caldus said.

Ilyr was called next, mostly so the court could look disgusted at a dark elf under oath. He stepped into the water channel and placed two fingers on the black witness slate.

"Do you swear by shadow to speak no falsehood?" Veyanna asked.

"No."

The court stirred.

Ilyr's mouth curved. "I swear by exile to make each evasion visible."

Serathiel leaned forward slightly. "Accepted."

That surprised him. It surprised Mara more that it made sense. Serathiel wanted order, not stupidity. She would use a sharp tool if the cut served her.

Ilyr described the orchard registry, the altered hymn bells, and Maelin's warning. He did not spare Khar Veyl. He named his own house's trade in old memory. Light-elf faces hardened not because they disbelieved him, but because truth from an enemy was so impolite.

Then Bessa Tarl testified.

She stepped into the court wearing road mud and carrying a soup ladle because no one had managed to disarm her of it without becoming ridiculous.

"I do not know your music words," she said. "I know when hungry people are asked questions that make them smaller. I know when wounded people are soothed until they stop objecting. I know the difference between a hand offered and a hand deciding it knows best. Saelith Dawnmere asks now. That is why she is on trial."

The chamber did not know what to do with Bessa. That made her the most powerful person in it for three breaths.

Veyanna recovered. "Plain speech can be moving without being complete."

"So can fancy speech," Bessa said.

Kesh whispered, "I may propose adoption."

At last Serathiel lifted one hand.

The court stilled.

"Saelith Dawnmere," she said. "Why did you cut your clasp?"

Saelith looked up at the branch above the dais. For a moment Mara saw the child she had been, throat aching from drilled hymns, grateful when law finally told her where to stand.

"Because it had become easier to ask the law than the wounded," Saelith said.

No one wrote for a heartbeat.

"And do you reject the Pale Bough?" Serathiel asked.

Saelith's hands trembled. She did not hide it. "No."

Mara's stomach dropped.

Saelith drew a breath. "I reject its ownership of mercy. I reject preservation without consent. I reject correction that begins by silencing the corrected. But I do not reject every song that held me when I was afraid. I do not reject every healer who believed obedience was the only way to prevent harm. I do not reject beauty because it has been used as a lock."

Serathiel's face softened.

That softness frightened Mara more than anger would have.

"Then return," Serathiel said. "Stand under correction. Teach us what you have learned after the fever of rebellion leaves you. Bring Mara Venn under sanctuary with you, and no one here need break."

The offer moved through the court like warm water.

Mara felt its pull. Not for herself. For Saelith. Rest. Belonging. A way to make disobedience useful to the very structure it had wounded. A beautiful trap with an open door.

Saelith closed her eyes.

"No," she said.

The word was small.

It held.

Serathiel's softness remained. "Then the court must protect what you cannot yet protect in yourself."

Mara gripped the rail.

"Saelith Dawnmere is remanded to restorative custody until the cleansing inquiry concludes," Serathiel said.

White roots rose from the water around Saelith's boots.

Mara moved.

So did everyone else.

Caldus caught one root with his staff. Brakka stepped onto another and cracked the channel stone. Kesh threw a knife that cut nothing important but insulted several ceremonial lines. Tavi launched a brass disk under the witness rail, and every root-lantern in the chamber flashed red. Ilyr drew one blade.

Mara did not reach for the cinder.

She climbed over the rail and stepped into the water channel.

"You asked witnesses," she said.

Serathiel looked down at her. "I heard them."

"No. You displayed them."

The roots around Saelith tightened.

Mara put both burned hands into the water. The channel carried every word spoken in the court, every polished charge, every answer corrected by echo, every plain truth made prettier by the room. Beneath it all, she found Saelith's no.

Not loud.

Free.

"Saelith Dawnmere refused," Mara said. "The court is witnessed ignoring refusal."

The water darkened with ink from Ilyr's slate. Tavi's red lantern flare caught in it. Brakka's cracked stone bled amber vow-light. Bessa slammed the ladle against the witness rail once, and the named dead spoke together:

"Witnessed."

The roots stopped.

Not released. Stopped.

Serathiel's gaze sharpened.

"You are learning dangerous forms," she said.

"People keep teaching them while trying to own me."

For a moment, no one breathed cleanly.

Then Serathiel lowered her hand. The roots withdrew from Saelith's boots.

"Custody is suspended," she said. "Until public discernment at the noon hymn. If Mara Venn trusts witness, let her stand before Lumenorath and be witnessed."

Kesh muttered, "That sounds like a stage with teeth."

Mara helped Saelith from the water. Saelith's fingers were cold around hers.

"I am sorry," Saelith whispered.

"For what?"

"Part of me wanted to say yes."

Mara thought of how tired Saelith looked, how beautiful the trap had been, how rest could become the sweetest chain.

"Then part of you is witnessed too," Mara said.
""",
    10: r"""## Chapter 10: The Hymn That Rewrote Her

At noon, Lumenorath gathered to improve Mara.

They called it public discernment. The phrase appeared on white banners along the terraces, sung from bell platforms, written in root-light across the bridges. Citizens came in layered robes, work aprons, scholar veils, gardener gloves, blade harnesses, children's festival scarves. Servants stood in the side paths until Bessa noticed and loudly asked whether discernment spoiled if the people carrying water heard it. After that, the servants were permitted nearer the amphitheater, which everyone pretended had been intended.

Mara stood on the central platform with mud cleaned from her boots against her will.

That small theft bothered her more than expected.

"I can reapply mud," Kesh whispered from below. "Discreetly or as doctrine."

"Wait."

"I dislike waiting in matters of footwear."

Saelith stood to Mara's right, pale but unbound. Caldus stood to her left with the cracked staff. Tavi had hidden devices on at least six people and one decorative vine. Ilyr watched the upper terraces where Khar Veyl assassins would have stood if they had been invited or discourteous. Brakka stood with the named dead, one hand on a root pillar, teaching it through pressure that stone remembered other laws.

Serathiel entered without spectacle.

That was the spectacle. The crowd quieted not because bells commanded it, but because everyone had been trained to recognize her restraint as a kind of weather. She wore no armor. Only white, the cracked branch at her throat, and a sword so plain it had to be famous.

"Mara Venn," she said, voice carrying through root and water. "You fear being made symbol."

"I object to it."

"Fear is not dishonor."

"Neither is objection."

A few citizens murmured. Not approval. Interest.

Serathiel lifted one hand. "Then let Lumenorath witness without chain. Let the public soul perceive what your acts have already made."

The hymn began under Mara's feet.

It did not sound like attack.

It sounded like being understood by someone kinder than anyone had ever been. The first notes gathered the story of Kell Ashgate: ash, hunger, dead miners, a girl running messages through heat tunnels, a brother's rough hands, a furnace, names rising. Mara felt tears start before she understood why. The hymn knew the shape of pain. It did not mock. It did not deny.

Then it began to clean.

Joryn's fear became noble protection. Dilla's soup line became rustic blessing. Kesh's bargains became comic loyalty without blood under them. Tavi's guilt became cleverness. Ilyr's half-truth became mysterious shadow. Saelith's disobedience became proof that even the Pale Bough had prepared a companion for the saint. Caldus's broken oath became a knightly fall designed for Mara's rise.

No.

Mara tried to move and found the platform warm around her boots.

The crowd watched, faces softening.

In the air above the amphitheater, root-light shaped scenes from her life. Not lies. Worse. Truths arranged until they no longer cut anyone important. The foundry appeared without stink. The dead rose without terror. Mordane fell without all the people who had helped him. Mara stood at the center clean-handed, small enough to pity, strong enough to worship, empty enough to fill.

Her burned hand stopped hurting.

That was when she panicked.

Pain had become part of how she knew where she ended.

"Mara!" Saelith shouted.

The sound reached her from very far away.

The hymn corrected it into a harmony.

Mara tried to remember Niv's token. She knew there had been a token. Scratched metal. A promise. The hymn offered a better version: a shining keepsake given by grateful children, not a stolen work token passed through fear and love and nearly lost in ash.

No.

What was the scratch shaped like?

She could not remember.

The cinder at her hip woke. It offered heat, command, dragon certainty. Burn the hymn. Break the singers. Take back the story by force.

For one breath, she almost said yes.

Then a boot hit the platform.

Not hard enough to hurt. Hard enough to smear mud across the white root by her feet.

Kesh stood below with one shoe in his hand. "Discreet failed."

The mud was ugly. Ordinary. It smelled of quarry rain, marsh rot, and honest roads. The hymn tried to make it symbolic and choked.

Tavi's voice cracked from six hidden devices at once. "Mara Venn once threatened to throw my regulator into soup if it clicked during breakfast. This is historically relevant."

The crowd startled.

Caldus stepped forward. The platform pushed against him. He leaned on his staff and forced the words through the hymn. "Mara Venn is impatient, suspicious, brave in ways that irritate planning, and wrong often enough to require counsel."

"She snores when exhausted," Bessa called from the servant path.

Mara heard laughter break somewhere in the terraces. Real laughter, not hymn-shaped.

Ilyr's voice followed, dry and precise. "Mara Venn has trusted me less since learning I deserved less trust. This indicates judgment."

Brakka pressed her palm to the root pillar. "Mara Venn steps off pretty road into ditch."

The pillar cracked.

Saelith walked onto the platform.

Every singer in the amphitheater faltered. She was not supposed to move. Not after trial, not during discernment, not toward the person the hymn was arranging.

Saelith took Mara's burned hand.

"May I?" she whispered.

The question reached Mara through all the music.

Yes, Mara thought.

She was not sure her mouth moved.

Saelith pressed Mara's hand against the scar where her clasp had been. Not healing. Witness. Burned palm to broken obedience.

"Mara Venn does not make my disobedience pure," Saelith said. "She makes it mine."

The hymn tore.

Memory flooded back wrong and glorious: Dilla threatening Kesh with soup, Joryn's ribs under her hug, Niv shouting not to scratch the token, Arveth correcting margins, Caldus saying no to rank, Tavi's devices smoking, Brakka's ditch wisdom, Ilyr's shame, Saelith asking, always asking now, as if consent could be rebuilt one touch at a time.

Mara screamed.

Not a song. Not a command. An ugly sound, entirely hers.

The root-light saint above the amphitheater shattered.

Pieces fell as white petals, then ash, then plain rain.

For one heartbeat, the crowd saw Mara without arrangement: scarred, furious, muddy, shaking, frightened by her own power, loved by people who disagreed with her, dangerous because she refused to become simple.

The silence afterward was not victory.

It was exposure.

Serathiel stood at the high dais, face unreadable.

"You could have burned the hymn," she said.

Mara's throat hurt. "I wanted to."

"But you did not."

"Do not make that yours."

Serathiel inclined her head. "I will not."

Somehow the promise was sincere.

That made it worse.

In the crowd, not everyone looked freed. Some looked betrayed. Some had wanted the clean Mara. Some had needed her. One woman clutched a child and wept as if Mara's refusal had taken food from her hands. A group of young blade-bearers stared at Saelith with open disgust. A servant in the side path touched muddy fingers to his own boot and smiled before hiding it.

Every story had split.

No one could gather it cleanly again.

Mara swayed. Caldus and Saelith caught her together.

Kesh, still holding one shoe, looked at the shattered root-light above the amphitheater. "I believe we are not getting our lodging deposit back."

Tavi wiped her eyes angrily. "Worth it."

Serathiel raised her hand, and the crowd stilled by habit even after the hymn's failure.

"Public discernment is complete," she said. "The witness refuses sanctification."

Mara straightened.

"Good," she rasped.

Serathiel's eyes met hers.

"Then we must speak of war without the comfort of your holiness."
""",
    11: r"""## Chapter 11: Serathiel's Mercy

Serathiel's private garden had no guards.

That was the first warning.

The second was the child asleep on a bench beneath coral leaves, one arm wrapped in white root bandage, breath rasping in a rhythm Mara recognized from foundry lungs. A human child. Road dust still marked the hem of his shirt. Beside him, a light-elf healer dozed upright, exhausted past ceremony.

"His name is Oren," Serathiel said. "He was pulled from the quarry after your restraint prevented an ambush from becoming slaughter."

Mara stood at the garden gate with Caldus behind her and Saelith at her side. Kesh had argued against the meeting, then argued that if Mara insisted, he should lurk nearby in a shrubbery capacity. Serathiel had said the garden would not permit hidden knives. Kesh had replied that sounded like a personal challenge. Mara had left him with Tavi and hoped Lumenorath was insured.

The garden glowed under soft rain. Coral leaves cupped drops like glass beads. Root lanterns floated over pools where silver fish carried tiny written prayers along their scales. Everything smelled of rain, green bark, and medicine.

Serathiel knelt beside the sleeping child.

Not theatrically. Her knees touched wet stone. She checked the bandage with fingers as gentle as Saelith's. The child stirred. Serathiel hummed one note, and his breathing eased without losing its rough truth.

Mara did not want the enemy to be kind.

It complicated hatred, and hatred was one of the few tools grief offered ready-made.

"You heal humans," Mara said.

Serathiel looked up. "Yes."

"Refugees."

"Yes."

"People who might fight you."

"Pain is not allegiance."

The answer was too good. Mara trusted it less for being true.

Serathiel rose and led them deeper into the garden. Saelith moved stiffly beside Mara. Caldus counted exits with his eyes and found too few. In the central pool, a white branch grew from black water, its blossoms closed though rain touched them.

"When I was young," Serathiel said, "Khar Veyl opened a sealed memory under the western rootlands. Not all of it. A fragment. They claimed they were correcting a light-elf omission. Perhaps they were. The memory carried dragon grief unfiltered. Three villages stopped sleeping. Parents drowned children they believed they were saving from future war. My sister cut out her own voice because the memory told her every word would someday become a weapon."

Saelith's breath caught.

Serathiel touched one closed blossom. "We contained the breach. We preserved the survivors. We burned the unanchored memory. Khar Veyl denied responsibility, then proved our oldest fear: truth without form is a plague."

Ilyr was not there to answer. Mara wished he were. She was also glad he was not. Both feelings stood uncomfortably together.

"That happened," Saelith said.

Not a question.

"Yes."

"You never told us."

"Training children with catastrophe breeds either zealots or cowards. We try to make servants."

Mara almost laughed. "You hear yourself?"

Serathiel looked at her calmly. "Every day."

The garden rain deepened. The pool's black water reflected no sky.

"You think I enjoy containment," Serathiel said. "I do not. I think it is inferior to trust and superior to mass graves. I think most people who praise freedom have not stood in a village where every free mind is being eaten by an ancient dragon's grief."

Mara thought of the cinder voice offering comfort, command, certainty. She thought of wanting to burn the hymn.

"You are not entirely wrong," she said.

Caldus shifted behind her. Saelith looked at Mara, startled.

Serathiel did not look pleased. "No. That is why I remain dangerous."

There it was. Honesty sharp enough to respect and fear.

Serathiel stepped to a stone table where three objects lay: the cracked hymn bell from the quarry, Liora's pear seed in a glass bowl, and one of Tavi's waking maps pinned beneath a white root thread. Evidence Mara had carried into Lumenorath. Evidence Serathiel had allowed into this garden.

"I have examined your proof," Serathiel said. "Some charges stand. Some practices must end. Veyanna's escort used bells altered beyond lawful healing. The Orchard of Held Workings contains seizures that should have been returned. Saelith's counter-hymn revealed a flaw in our restoration law."

Saelith went very still.

"You admit it?" Mara asked.

"I am not Lord Mordane. I do not need every fact to flatter me."

"Then stop the cleansing decree."

Serathiel touched the map. The Orrowen circle pulsed under the root thread.

"The decree is why I can admit these faults without losing the realm."

"That makes no sense."

"It makes statecraft." Serathiel's voice did not harden. That was the horror of it. "Lumenorath is frightened. The hymn failed publicly. The orchard bled stolen workings. Khar Veyl's shadow violated a border chapel and named your companion hazard. If I tell my people only that we were wrong, the hardliners will turn to prettier liars by morning. If I name Khar Veyl's concealed dragon crime and direct fear outward, I can reform inward abuses while preventing panic from devouring us."

Caldus said, "You are choosing a war to manage a crowd."

"I am choosing a campaign to prevent uncontrolled war."

"That is what people call it before the dead object," Mara said.

Serathiel's gaze moved to her. "And you? You held rebels from attacking a supply train by giving them proof and an enemy later. You did not end their anger. You arranged its next shape."

Mara had no quick answer.

The saint-general saw that and did not press. Mercy again. Or strategy. In Serathiel they were too close to tell apart.

"Accept sanctuary," Serathiel said. "Not as saint. As witness under protection. Stand beside me when I announce the decree. I will name the abuses you revealed. I will forbid coercive hymnwork without consent. I will return the gentled spells that can be safely returned. In exchange, you will affirm that Khar Veyl must answer for the dragon-moon before any descent."

"And Ilyr?"

"He will be held, not harmed."

"Saelith?"

"Restored with reforms she helped inspire."

Saelith's face twisted. Restored. The sweetest poison.

Mara looked at the sleeping child, the cracked bell, the pear seed, the waking map. Serathiel had listened. Serathiel had learned. Serathiel would save some people with the very hand she used to point an army underground.

That was worse than simple evil.

"No," Mara said.

Serathiel closed her eyes briefly.

When she opened them, grief lived there without softening anything.

"Then I will proceed without your witness."

"You will proceed against it."

"Yes."

Saelith stepped forward. "Serathiel, please."

The saint-general looked at her former pupil. For the first time, Mara saw pain break through discipline.

"I would have sheltered you from this burden," Serathiel said.

Saelith's voice shook. "You keep calling cages shelter."

"Because I have seen open doors become graves."

"So have I."

Rain gathered on the closed blossom above the black pool. One drop fell. The flower opened, showing a center dark as cinder.

Mara heard a whisper from beneath the garden.

Moon below.

Serathiel heard something too. Her hand went to the branch at her throat.

"By dawn," she said softly, "even hesitation will become a side."

Mara turned toward the gate.

"It already has."
""",
    12: r"""## Chapter 12: The Cleansing Decree

White petals fell like ash over the root amphitheater.

They fell from no tree Mara could see, drifting from the open sky in slow, luminous sheets. Each petal dissolved when it touched the water channels, sending a tiny note through the floor. By the time the amphitheater filled, the ground itself was singing under thousands of feet.

Lumenorath had come dressed for grief.

That was how Saelith explained the pale veils, the unadorned sleeves, the absence of festival color. Grief, here, had grammar. Even fear knew how to stand in rows. Citizens filled the terraces: healers, gardeners, blade-bearers, rootwrights, scholars, servants permitted into sight because the public hymn had cracked more than Mara first understood. On the upper arches stood the Pale Bough. At the center waited Serathiel.

Mara's company stood on the lower witness path with one cracked hymn bell, three black witness slates, six orchard registry strips, Tavi's waking map, and no illusions that evidence alone could stop a people determined to make war feel clean.

Ilyr kept his hood down.

That was brave and foolish, which meant it was probably necessary.

The first shout came before Serathiel spoke.

"Veyra poisoner!"

Then another. "Shadow thief!"

The crowd's fear found Ilyr as water finds low ground. Pale guards moved subtly closer. Caldus put himself between Ilyr and the nearest steps. Brakka's hand settled on the root wall. Kesh scanned the terraces, lips moving as he counted exits that did not yet exist.

Serathiel lifted both hands.

The amphitheater stilled.

"We gather without comfort," she said.

Her voice carried perfectly. No strain. No spell Mara could feel, though in Lumenorath the difference between training and magic had become annoyingly thin.

"We gather after public witness revealed faults within our own bough. Healing bells were altered into instruments of softened refusal. Held workings were preserved beyond lawful need. Restoration law failed to distinguish correction from custody. These wrongs will be answered."

Murmurs moved through the terraces. Surprise. Shame. Relief. Resistance.

Mara felt hope, unwanted and dangerous, lift its head.

Then Serathiel turned toward Ilyr.

"We also gather because these faults grew in the shadow of an older crime. Khar Veyl, keeper of sealed histories, hid fractures in the dragon-moon seal. Its houses traded controlled memories to surface powers. Its courts retained Maelin Noct-Vey for carrying records they feared to release. Its agents name Mara Venn hazard while seeking to bring her below under their law."

Now the crowd's fear sharpened.

Ilyr did not flinch.

Mara stepped forward. "Name the light-elf half."

The amphitheater sucked in breath.

Serathiel's gaze found her. "You will have your turn."

"War never leaves turns for later."

Kesh whispered, "Good line, catastrophic timing."

Mara raised the orchard strips. "The Pale Bough stole workings from children and called it preservation. Your bells held cinder chips. Your road tried to take truth as toll. If Khar Veyl hid fractures, Lumenorath polished the ceiling until nobody looked down."

Voices rose. Serathiel let them rise for exactly three breaths, then cut them off with one note.

"Yes," she said.

The word struck harder than denial.

"Lumenorath has preserved too much without consent. I name this fault before root, witness, and sky. But confession without action is ornament. The dragon-moon stirs. Orrowen answers. Khar Veyl moves Maelin moonward and refuses open council. If we wait for perfect mutual repentance, the seal will break under liars arguing procedure."

Tavi muttered, "I hate when villains understand committee failure."

Serathiel drew the plain sword.

It made almost no sound.

"Therefore, by authority of the Pale Bough and emergency covenant of root and witness, I declare a cleansing campaign."

The amphitheater erupted.

Not only cheering. Some cried out in alarm. Some protested. Some sang. Some fell to their knees. The word cleansing moved through them in different meanings and gathered danger from each.

"Against Khar Veyl hardliners," Serathiel continued, "against concealed dragon crime, against any seal-warden who refuses public answer."

Ilyr spoke, voice clear. "And who decides refusal?"

"Those who arrive asking and are denied."

"An army asking at a gate makes denial inevitable."

"A sealed gate over a waking moon makes arrival necessary."

He bowed slightly. "Then we are all very tidy and doomed."

Veyanna's blade came half out. Saelith stepped in front of Ilyr.

That movement broke the next part of Serathiel's plan.

Every eye turned to Saelith Dawnmere, oathkeeper on trial, singer of a flawed counter-hymn, child of this realm standing between white blade and dark exile.

Saelith was shaking.

She spoke anyway.

"If cleansing begins with the assumption that what resists you is infection, you will call every living will diseased by dusk."

Serathiel's face tightened. "Saelith."

"No." Saelith's voice grew stronger because the first no had survived. "You taught me that mercy must go where harm is, not where reputation prefers. Harm is here too. If you march without naming that fully, you do not carry law. You carry fear dressed in white."

The crowd went silent enough for petals to be heard dissolving.

Then the upper roots moved.

Not fast. Fast would have seemed violent. They descended like curtains. White root strands lowered around the witness path, around Ilyr, around Saelith, around Mara's company. Protective, someone might have said. Containment, if one was honest.

Mara reached for the cinder.

The old dragon grief surged up, eager. Break root. Burn path. Take your witnesses and run.

This time, she did answer quickly enough to refuse.

"Brakka," she said.

The troll had already set both hands to the root wall. Amber vow-light crawled from her palms into Lumenorath's living architecture.

"Road wearing road," Brakka said. "Old road remembers."

Beneath the amphitheater, buried under centuries of curated root, old stones woke: milestone, service path, work stair, drainage channel, funeral road, servant route, exile track. Lumenorath had preserved them all, thinking preservation meant ownership. Brakka asked them what they had been before beauty.

They answered.

The witness path cracked open.

Not a chasm. A road.

Mud showed beneath white root.

Kesh laughed once, wild with relief. "I adore infrastructure with resentment."

Caldus shoved the named dead toward the opening. Tavi snatched the waking map and two slates. Ilyr caught Saelith's arm, then released it immediately so she could choose to run. She did. With him. That choice rang louder than bells.

Serathiel did not order arrows.

Mara saw the restraint and hated owing anything to it.

"Mara Venn!" Serathiel called.

Mara turned at the edge of the opened road.

The saint-general stood amid falling petals, sword lowered, grief naked now and still not enough to stop her.

"Khar Veyl will not receive you kindly," Serathiel said.

"Neither did you."

"I received you with every mercy I had."

"I know."

That was the worst answer because it was true.

Serathiel's eyes flashed. "Then when the dark below shows you what unbound truth can do, remember that I tried to spare you."

Mara looked at the crowd, at the servants in side paths, at Veyanna torn between blade and doubt, at Saelith breathing hard beside Ilyr, at the cracked roots revealing all the roads Lumenorath had swallowed.

"When the dark below shows me something terrible," she said, "I will try not to turn terrible in answer."

Then Brakka pulled the road wider, and the company fled under the amphitheater.

Behind them, Serathiel's decree became song.

Ahead, the mud road sloped down through roots, old stone, and cooling light. The air changed from flower-clean to mineral damp. White petals stuck to Mara's coat like ash. After a hundred paces, the sound of Lumenorath faded.

Something else took its place.

Black water dripping.

Far below, a gate answered Ilyr's blood with a blue-dark flame.

Khar Veyl had opened a way.

Or set a trap.

In Mara's experience, important roads often did both.
""",
}


EXPANSIONS: dict[int, str] = {
    7: r"""The city beyond the gate did not unfold like a map. It unfolded like an argument every resident had learned to sing through.

The upper terraces were all light, water, and deliberate grace. Root towers rose through rings of garden balconies. Mirror-bark halls reflected the sky until the buildings seemed full of weather. Bridges curved between trunks, carrying citizens who moved with the calm of people trained never to rush where strangers could see. Children in pale green practice robes recited dawn law while walking in pairs. Gardeners trimmed coral leaves with silver shears and laid each fallen piece in a dish instead of letting it touch the ground uncounted.

Then Mara looked where servants walked.

Below the terraces, half-hidden by hanging roots, narrow service paths ran in damp shade. Humans, gnomes, goblins, and light elves without court robes carried laundry, compost, trays, pruning waste, bandage jars, and buckets of something that smelled ordinary enough to comfort her. Their clothing was clean but patched. Their eyes slid away from the main paths by habit. Beauty had a back door. Of course it did.

"There," Mara said.

Veyanna followed her gaze. "The lower ways keep the upper gardens clear."

"Clear of whom?"

"Of interruption."

Bessa, who had insisted on accompanying the smaller witness caravan as far as the guest hall, snorted. "Interruption is what clean people call work when someone else does it."

Several Elyri citizens heard. None responded. That was worse than offense.

As they passed a fountain, the water lifted in seven arcs and sang the names of honored preservers. Serathiel's name rang last, and people bowed. The three named dead under canvas did not. Edrin Vale looked into the fountain until the water tried to reflect him as living, cheeks full, eyes bright, death painted over with health.

"It lies kindly," he said.

Saelith moved beside him. "Do you want the cover drawn?"

"No. I want to see whether it tires first."

Mara liked him more every mile.

The guest hall stood on a terrace overlooking the coral gardens. Its doorway shaped itself wider for Brakka and lower for Tavi without being asked. Kesh refused to enter until he had checked the roof, the window latches, the pantry, and two exits the house had not admitted to owning. Caldus stood in the central room and frowned at the beds.

"Too soft," he said.

Tavi dropped face-first onto one. "I will investigate this threat."

The bed rose slightly around her in a supportive cradle.

She lifted her head. "It knows my spine. I hate it and may require several hours of further study."

Mara should have laughed. Instead she walked to the balcony.

Below, Lumenorath shone in afternoon light. White bridges, singing water, towers that looked grown from prayer. Farther down, under roots, a servant girl dumped a bucket, straightened quickly when a robed official passed, then rubbed her wrist as if the bucket had been heavy and the gesture forbidden.

Mara took the torn banner cloth from her pack. The painted hand, ripped down the palm, looked absurd against the polished balcony rail.

Saelith came to stand beside her.

"The realm will try to make you ashamed of mud," Saelith said.

"It is already trying."

"It will try to make shame feel like elevation."

Mara tied a strip of the torn banner around the balcony rail, low where anyone looking up for grandeur would miss it and anyone carrying buckets below might see. Not a banner. Not a claim. A reminder: the hand had torn. The bowl mattered more.

"Is that allowed?" Saelith asked.

"No idea."

Below, the servant girl saw the dirty strip, then saw Mara. Her eyes widened. Mara lifted one muddy boot onto the spotless balcony rail long enough to leave a print.

The girl covered her mouth.

Maybe laughing. Maybe horrified.

Either would do.
""",
    8: r"""They did not return from the orchard by the way they entered.

Kesh took one look at the bells waking across the terraces and led them down through a service stair so narrow Brakka had to turn sideways and mutter about architecture with class prejudice. The stair smelled of wet bark, soap, fruit rot, and the mineral tang of root sap. It descended behind the coral gardens into Lumenorath's lower workings, where beauty's discarded parts were sorted before being made invisible again.

There, they found the orchard keepers.

Not robed wardens. Not judges. Workers.

Five of them stood in a sap room around a table covered in split fruit, their aprons stained silver, red, and blue. Two were Elyri. One was human. One was a gnome with root thread sewn through both sleeves. The last was a goblin old enough that Kesh immediately became polite, which told Mara more than any title could have.

They froze when the company burst in.

The human keeper saw the pear seed in Mara's hand and whispered, "Liora."

Saelith's face changed. "You know her?"

The woman looked toward the ceiling, where alarm bells rang like distant glass. "I know the fruit. We are not given children."

"You are given spells taken from children," Mara said.

The woman flinched. "Yes."

No defense. No doctrine. Just the word, tired and ashamed.

Tavi, still smoking from the coil, pointed at the cut fruit. "What happens when the registry tree is wounded?"

The gnome keeper answered because craft fear outranked politics. "The held workings may revert, leak, or seek original vessels."

"Original vessels who may be dead, grown, missing, or across half the continent," Tavi said.

"Yes."

"Splendid disaster shape."

The old goblin keeper leaned on a pruning hook. "If you came to burn us, burn quickly. If you came to save songs, stop waving the seed near the sap drain."

Kesh blinked. "Auntie?"

"Not yours," the old goblin said. "But I accept the respect retroactively."

Mara closed her fingers around the seed. It pulsed in panic. Not Liora herself. Not exactly. A working torn from her and kept alive without a life around it. Preservation had made it fragile.

"How do we keep it from hurting her if it seeks her?" Mara asked.

The keepers exchanged looks.

"Ask it what it wants to remember," the human woman said.

Veyanna would have called that unlawful. Serathiel would have called it risky. Mordane would have asked what it could power.

Mara knelt on the sap-stained floor.

Alarms rang overhead. Wardens moved in the walls. The stolen registry strips crackled under Saelith's coat. There was no time, which was usually when people excused doing violence quickly.

Mara set the pear seed on her burned palm. "Liora's rain-song is witnessed. Not commanded. Not returned by force. What do you want to remember?"

The seed warmed.

Rain. Mud. Bare feet. Father's hand gripping grass at the ditch edge. A child's terror turning into song because nobody official was close enough to forbid it. Not the whole spell. One thing under it.

Love, clumsy and immediate.

The seed cracked.

Inside was not light but a drop of ordinary water.

The human keeper began to cry.

"That can travel," she said. "Water remembers road better than fruit."

Tavi produced a glass vial from somewhere. "For once, I am overpacked in a thematically appropriate way."

They sealed the drop.

The old goblin keeper opened a waste chute hidden behind a rack of moon-apple skins. "This leads to the lower compost slides. It is disgusting and therefore not watched by anyone important."

Kesh bowed. "My favorite kind of infrastructure."

Mara paused at the chute. "Come with us."

The human keeper shook her head. "If we run, they replace us with people who believe the labels."

"They will punish you."

"They already taught us to call this work gentle." She looked at the split fruit. "Punishment is overdue."

Saelith took one registry strip from under her coat and placed it on the table. "Then keep this unedited if you can."

The keeper pressed her stained fingers over it. "If I cannot?"

"Hide one true word badly enough that someone kind finds it."

The compost chute dropped them into darkness, rot, and a slide so foul that Kesh, for once, had no immediate joke.

When they spilled out below the guest terrace, covered in pulp and sap, the city above still rang with alarm. Mara clutched the vial of Liora's rain-song against her chest.

They had stolen proof.

They had also found accomplices.

That made Lumenorath more dangerous, not less. A cruel place full only of cruel people could be fought cleanly. A beautiful place full of trapped decent ones required sharper mercy.
""",
    9: r"""Suspended custody turned out to mean guarded freedom inside a room without corners.

After the trial, Saelith was escorted to a reflection chamber beneath the court. Mara refused to leave her. Serathiel allowed Mara to stay, which made both of them distrust the permission. The chamber walls curved in a continuous oval of mirror-bark polished so deeply that every reflection lagged half a breath behind the body it copied. If Saelith lifted a hand, the reflected Saelith lifted hers a moment later, smoother, calmer, already corrected.

"Training room?" Mara asked.

Saelith sat on the floor because no chair had been provided and standing felt like surrender. "Confession room."

"Of course it is."

"The delay helps initiates see the shape they might become after correction."

Mara watched her own reflection fold its hands with serene patience she had never possessed. "I may punch the wall."

"It will only show you punching more beautifully."

That made Mara laugh, which echoed badly and returned as a refined little sound from the walls. She stopped.

Saelith drew her knees to her chest. "Part of me still hears the return hymn."

"From the court?"

"From childhood. It says restoration is not defeat if the bough bends to receive you. It says disobedience is fever. It says the healed self will thank the hand that held it still."

Mara sat beside her. Not too close. "What do you say?"

"I say I am tired."

That answer had no heroic shape. It was truer for that.

Outside the chamber, two blade-bearers stood guard. Their shadows showed under the door. One shifted often, perhaps nervous. The other did not move at all. From farther away came court noise, witnesses arguing, Tavi insulting evidence procedures, Bessa insisting that soup ladles were not weapons unless necessary.

Saelith rested her head against the mirror wall. Her reflection did it gracefully. She did it like someone whose bones hurt.

"When I was twelve," she said, "Veyanna praised me because I healed a bird without asking permission."

Mara glanced at her. "That seems unlike Veyanna."

"She praised the power. Then she broke the bird's wing again and made me ask properly before healing it a second time."

The room went very still.

Mara felt heat rise in her palm.

"She said mercy without form teaches arrogance," Saelith continued. "I believed her because the second healing held cleaner."

"Saelith."

"I know." Her voice thinned. "I know now. But memory does not update like a ledger. Some part of me is still proud I learned quickly."

Mara wanted to burn the reflection chamber to the root.

Instead, she held out her scarred hand, palm up, not touching.

Saelith looked at it.

The question between them had become familiar and still mattered every time.

Saelith placed her hand in Mara's.

The mirror walls reflected the gesture a breath late. In their version, Saelith looked serene and Mara looked saintly. In the real room, Saelith's fingers were cold, Mara's bandage had loosened, and both of them were frightened.

"This is the one I keep," Saelith whispered.

The door opened.

Veyanna stood there.

For once, she looked older than her composure.

"The noon hymn will not be gentle," she said.

Mara stood. "Is that warning or threat?"

"Regret."

Saelith did not rise. "You broke a bird's wing."

Veyanna closed her eyes.

"Yes."

No doctrine followed. No correction. No explanation about form. The missing defense was almost worse.

"I thought pain with purpose was kinder than power without obedience," Veyanna said. "I still fear the second. I have fewer defenses for the first than I did yesterday."

"Will you stand with us?" Mara asked.

Veyanna opened her eye. The leaf veil trembled. "No."

Honesty, then. Hard and useless.

"But I will not lie about what I have seen," she said.

Saelith looked up. "In Lumenorath, that may become the same thing too late."

Veyanna bowed her head. "I know."

When she left, the door remained open.

Not freedom. Not quite.

Enough for sound to enter unpolished.

Mara and Saelith sat together until the first notes of public discernment began above them, and neither pretended not to be afraid.
""",
    10: r"""The hymn left bruises no healer could show.

After the amphitheater emptied, Mara sat on the lowest step with Saelith's cloak around her shoulders and tried to list true things. Her name. Mara Venn. Her brother. Joryn. The token. Scratched along one edge, dented near the hole, warmer when held too long. Dilla's soup, too much pepper when angry. Niv shouting across the road. Arveth writing Unknown is not empty. Tavi's regulator clicking before disaster. Kesh with one shoe in hand and mud like a legal argument. Brakka saying road exists. Caldus saying no and making the word into shelter.

She got to Caldus and forgot the shape of his shield.

Panic rose so fast she nearly vomited.

"Broken," Caldus said from beside her.

She looked at him.

He had sat two steps down, leaving space, staff across his knees. "My shield was broken. Crest split. You saw it in the pay yard."

The memory returned with a snap: crestless wood, cracked rim, empty arm. Mara pressed her burned hand against her mouth.

"The hymn took that?"

"Borrowed," Ilyr said from the shadow of a root pillar. "Theft implies honesty about ownership."

Tavi crouched in front of Mara and held up three fingers. "How many fingers?"

"Three."

"How many am I emotionally?"

"Too many."

"Excellent. Core cognition survives."

Mara laughed, then cried, then hated both under so many watching terraces.

Not all the watchers were hostile. That was part of the ache. A servant boy stood at the water path with muddy fingertips hidden in his sleeve. Two young Elyri argued in whispers over whether the hymn should ever be sung again. An elderly rootwright touched the cracked pillar where Brakka had pressed old road-law and looked shaken, not angry. The public soul Serathiel had tried to arrange had not become one thing.

Serathiel knew it. Mara could feel that too.

Bessa approached with a cup of something hot. "Drink."

"What is it?"

"Ugly tea."

Mara drank. It tasted of bitter leaves, smoke, and practical affection. "That is accurate."

"Good. Your mouth remembers honesty."

Saelith returned from speaking with one of the named dead. Her face was drawn. "Edrin lost an hour."

Mara went cold. "What?"

"The hymn tried to render him as redeemed testimony. He forgot why he refused preservation long enough to thank a warden."

"Is he back?"

"Angry. That helps."

Mara stood too quickly. The world tilted. Caldus caught her elbow and let go as soon as she steadied.

They found Edrin in the side court with Brakka, staring into a fountain that kept trying to show him alive. His dead hands gripped the stone rim.

"I thanked them," he said when Mara approached.

"The hymn made you."

"My mouth did it."

"Mouths can be occupied territory," Kesh said softly.

Edrin looked at him, surprised.

The goblin shrugged. "Road clans know several things about speaking under duress."

Mara knelt by the fountain. "What do you want written?"

Edrin's painted eyes turned to her. "That I was made to praise a cage and object afterward."

Ilyr took out his ledger. "Exact wording?"

"Yes."

He wrote it.

The fountain's reflection of Edrin flickered. For a moment it showed him furious and dead instead of peacefully alive. He nodded once, satisfied.

Across the court, a small girl in green practice robes stepped away from her mother and approached Mara. Her hands twisted in her sleeves.

"The hymn showed you kind," the child said.

Mara was too tired to be careful. "I hope I am, sometimes."

"Then it showed you not angry."

"That part lied."

The girl's brow furrowed. "Can kind be angry?"

Saelith closed her eyes as if the question hurt.

Mara thought of Dilla, of Joryn, of Bessa, of every furious hand that had ever fed someone anyway.

"It had better be," Mara said. "There is a lot to be angry about."

The child considered this with grave attention. Then she crouched, scooped mud from the edge of Mara's boot print, and pressed it onto her own clean shoe.

Her mother made a strangled sound.

The girl ran before correction arrived.

Kesh watched her go. "Revolutionary footwear spreads."

Mara smiled, but her hand shook around the tea.

The hymn had failed to rewrite her completely. It had not failed to hurt her. That mattered. Survival was not the same as escape, and if she forgot that, she would ask others to be grateful for wounds that stopped short of killing them.

Above the court, Serathiel's private messenger arrived in white and requested Mara's presence in the garden.

Mara looked at Saelith.

"Trap?" Kesh asked.

"Obviously," Tavi said.

Caldus rose. "We go carefully."

Mara touched the scratched token in her pocket and made herself remember every dent.

"No," she said. "We go honestly afraid."
""",
    11: r"""The garden did not end when Mara refused.

That was another cruelty of beautiful places. They kept being beautiful after truth failed to save them.

Serathiel walked them back toward the gate without calling guards. The sleeping child, Oren, stirred on his bench. Mara paused despite herself. His bandage had begun to glow too brightly at the edges.

Saelith saw it too. "The root is overknitting."

Serathiel turned.

For the first time since the conversation began, uncertainty broke her rhythm. She knelt and touched the bandage. The child whimpered. White root had sealed the wound cleanly, then continued, fine threads creeping past torn flesh into healthy skin.

"It should have stopped," Serathiel said.

"Did he consent to root binding?" Saelith asked.

The attending healer woke with a start, horrified. "He was fevered. We had no time."

Old Saelith would have accepted that. Mara could feel it. The reflex toward emergency obedience, toward the clean answer. New Saelith took a breath that shook.

"May I remove the excess?" she asked the child.

Oren's eyes opened, bright with fever and fear. "Will it hurt?"

"Yes," Saelith said. "Less than leaving it."

Serathiel watched.

The whole garden seemed to watch.

Oren nodded.

Saelith worked with both hands and no hymn. She unwove root thread from living skin while the boy cried and Mara held his free hand because he asked for someone not wearing white. Serathiel did not look away. The attending healer wept silently. Caldus stood at the path entrance like a man guarding a battlefield nobody would sing about.

When it was done, the bandage glowed less beautifully and the child's breathing steadied.

Serathiel touched the cut-away threads in Saelith's palm. "This is what you mean."

"Part of it," Saelith said.

"We would have caught the overgrowth at next review."

"He would have carried it until then."

No accusation could have landed harder.

Serathiel stood slowly. "You think one overknit bandage disproves a realm."

"No," Saelith said. "I think a realm is made of what it calls acceptable until review."

Mara saw pain cross Serathiel's face. Real pain. Useful pain, maybe, if it had time. But dawn was coming, and Serathiel had already chosen a shape for fear.

A bell rang beyond the garden wall.

Not public. Military.

Caldus heard the difference at once. "Troop signal."

Serathiel did not deny it.

Tavi's voice drifted from somewhere above the wall. "Also root wagons moving east, if anyone cares about my illegal vantage."

Kesh's voice followed. "She means west."

"I mean map-left!"

Serathiel looked toward the wall with weary resignation. "Your companions are difficult to contain."

"Yes," Mara said. "That is why they are companions."

From the top of the wall, something small dropped into the pool with a plunk. A rolled strip of root-paper bobbed among the silver fish. Caldus retrieved it with his staff and passed it to Mara.

It was a partial muster list.

White-root companies. Hymn bearers. Preservation wagons. Mercy tents. Blade cohorts. Destination: lower passes approaching Khar Veyl's first sealed road.

At the bottom, in Tavi's cramped hand: THEY ARE PACKING FOR BOTH RESCUE AND INVASION, WHICH IS RUDELY EFFICIENT.

Mara handed the paper to Serathiel.

The saint-general read it, then gave it back.

"You let us see this," Mara said.

"Your friends saw it."

"In your garden, behind your wall, while you had no guards."

Serathiel said nothing.

Saelith stared at her former teacher. "You wanted us to know where to stand."

"I wanted you to understand the cost of standing elsewhere."

"That is not the same thing."

"It is the closest mercy left to me."

Mara looked at the child sleeping easier now, at the muster list, at the woman who could admit an overknit wound and still send wagons toward war because terror at scale had become arithmetic with flowers.

"No," Mara said. "It is the mercy you kept after throwing the others away."

Serathiel took that like a blade. She did not bleed where anyone could see.

At the garden gate, Veyanna waited with Mara's mud-stained boot print on the hem of her white robe. She noticed Mara notice.

"A child stepped on me," Veyanna said.

"Good."

"I did not correct her."

Saelith looked sharply at her.

Veyanna's leaf veil hid half her face, not enough. Doubt had entered and found furniture.

"Public decree at dawn," Veyanna said. "If you intend to leave, every road will be watched."

Brakka's low voice came from the path beyond. "Not every road admits being road."

Veyanna closed her eye briefly. "I suspected as much."

She stepped aside.

Not alliance. Not rebellion.

But space.

Sometimes history first changed by an inch.
""",
    12: r"""The road under the amphitheater was not empty.

At first Mara thought the darkness ahead belonged to the descent itself: old drainage stones, root shadows, mineral damp swallowing Lumenorath's clean light. Then the shadows detached from the ceiling and dropped onto the path with white-root hooks in their hands.

Pale Bough retrieval wardens.

Not soldiers, Saelith had time to say. Worse, her face said. Wardens were trained to bring people back alive enough to thank them later.

"Run," Caldus ordered.

The road was too narrow for running well. It twisted between old foundation stones and living roots that kept trying to reseal the way Brakka had opened. Behind them, the amphitheater still sang the cleansing decree. Ahead, blue-dark flame marked Khar Veyl's gate, farther than it looked. The three named dead moved slowly, and Edrin's left leg dragged when the road sloped.

Mara reached for him.

"No," he said. "Witnesses do not become luggage without consent."

"Then consent faster."

He laughed, dry as old paper, and took her arm.

The first warden cast a loop of white root. It wrapped Caldus's staff and bloomed thorns. Caldus pulled instead of letting go, dragging the warden off balance. Kesh cut the loop. Tavi threw a device that unfolded into a shrieking wheel and rolled back uphill toward their pursuers.

"What does that do?" Mara shouted.

"Ideally? Embarrass them."

It exploded in a burst of sticky blue foam.

"Also that."

Brakka held the rear, one shoulder against a root mass trying to close. "Road forgets promise!"

"Can it do that?" Kesh asked.

"People do."

Saelith stopped so suddenly Mara nearly collided with her.

Ahead, a curtain of white roots dropped across the passage, sealing the path. The roots glowed with familiar court light. Not a wall, a restoration mesh. It hummed the opening notes of the return hymn.

Saelith went pale.

Mara touched her elbow. "You do not have to."

"I know."

The wardens advanced through Tavi's foam, slowed but not stopped. Caldus's bad leg buckled. Ilyr caught him before he fell, then looked offended to have been useful in such a straightforward way.

Saelith stepped to the mesh.

She did not sing against it.

She spoke.

"I was twelve when Veyanna broke the bird's wing," she said.

The mesh flickered.

Mara understood and felt horror and pride together.

Saelith put both hands near the roots without touching. "I healed it better after asking permission. I learned the wrong lesson because pain with purpose was praised by people I loved. I am still learning. I am still angry. I am still afraid of becoming cruel without rules. I refuse restoration that requires me to forget this."

The roots dimmed.

Not broken by power. Starved of the lie that she wanted their correction.

The mesh opened.

Saelith staggered. Mara caught her.

"Too much?" Mara asked.

"Enough."

They ran.

Behind them, the wardens reached the opened mesh. One paused, perhaps because Saelith's confession still hung in the roots. The other raised a hook toward Mara.

Ilyr turned.

His blade caught blue-dark light from the gate ahead. For the first time since Lumenorath, he looked like what surface stories feared when they said dark elf: precise, beautiful, mercilessly quick. He cut the hook, then the shadow holding it, not deep enough to kill, exact enough to make pursuit reconsider its career.

"No killing," Caldus snapped.

"I am being culturally restrained."

"Be more restrained faster."

The blue flame gate grew.

It stood in an arch of black basalt swallowed by root. Khar Veyl script burned across it in lines that hurt Mara's eyes if she tried to read them directly. Ilyr cut his palm without ceremony and pressed blood to the center.

"House Noct-Vey requests road under answer," he said.

Nothing happened.

Kesh looked back at the wardens. "I love dramatic pauses in theory."

Ilyr's jaw tightened. "House Noct-Vey requests road under witness."

Still nothing.

Mara felt the cinder wake. Not with command. Recognition. Under the gate, a memory waited for a second witness. Not Ilyr. Not his house. Someone outside the old lie.

She stepped beside him and pressed her burned palm to the basalt.

"Mara Venn of Kell Ashgate requests road for the named, the living, the ashamed, and the inconvenient."

The gate's flame turned from blue to black.

Then inward.

Cold wind rushed out, smelling of stone, ink, mushrooms, and deep water.

The named dead crossed first because Brakka insisted witnesses outrank panic. Tavi followed with the maps. Kesh went backward, making a rude gesture at the wardens with both hands. Caldus limped through beside Saelith. Ilyr remained at the threshold, staring into the under-road as if every childhood fear had been kind enough to wait.

Mara touched his sleeve. "Together?"

"That may make it worse."

"Most things."

They crossed.

The gate sealed behind them just as white-root hooks struck basalt.

For a moment there was only dark.

Then lights opened below, thousands of them, blue and green and violet, descending through a cavern so vast Mara's knees forgot their duty. Terraces of black stone curved down around an underground lake. Root-fire lamps burned in disciplined rows. Bridges hung from chains. Far below, a city waited with windows like watchful eyes.

Khar Veyl.

Not evil.

Not safe.

A place that had made secrecy into architecture.

From somewhere in the depth, a horn sounded once.

Ilyr exhaled. "They know."

"That we arrived?"

"That I came back."

Mara looked behind, where Lumenorath's white roots pressed silently against the sealed gate, then ahead into the dark city that had opened because she and Ilyr asked together.

The war above had begun singing.

The truth below had teeth.
""",
}


def replace_chapters(text: str) -> str:
    pattern = re.compile(r"(?m)^(?:# Part II: Lumenorath\n\n)?## Chapter (\d+): .*$")
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
        'current_form: "full-length draft zero with Book Two chapters 1-12 revised in pass 01"',
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
    print(f"Book Two chapters 7-12 revised. Word count: {total}")


if __name__ == "__main__":
    main()
