#!/usr/bin/env python3
"""Revision pass 01f for Book Two chapters 22-24.

Replaces the remaining Blackroot Road scaffold with bespoke Orrowen scenes:
Arveth's courthouse, Vorrakai's first clear temptation, and the arrival of
the armies below.
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
    22: r"""## Chapter 22: Arveth's Courthouse

The courthouse had not learned the war was over because no one had filed the war's death certificate in the proper room.

It stood at the end of a canal street where the water ran uphill in narrow black ribbons, carrying petitions in glass bottles toward doors that opened only for the correct grievance. Its facade was built from white civic stone veined with old dragon-scale. Towers leaned over the entrance, each tower hung with bells. Some bells were bronze. Some were bone. Some were made from legal seals fused together until they looked like metal fruit.

Every bell rang at a different hour.

Every bell rang for Arveth.

Arveth of Orrowen, convicted under emergency continuance.

Death deferred until witness exhaustion.

Sentence reissued.

The voice rolled out across the square for the third time since they had entered the district. Orrowen citizens paused, adjusted satchels, bowed heads, cursed softly, or did not react at all because outrage repeated long enough became civic weather. A translucent woman selling lamp wicks spat into the canal. A skeletal messenger tightened the strap on his dispatch case. Two children, dead enough to glow and young enough to kick at puddles, recited the sentence under their breath in bored unison until their minder snapped at them to show respect.

Mara stopped at the foot of the courthouse steps.

"How many times?" she asked.

Sava Rennet's mouth flattened. "Every morning. Every appeal hour. Every public correction cycle. Every time an external witness enters the district. The sentence is hungry for exhaustion."

The ledger case in Ilyr's hands trembled.

Arveth's voice came from inside it, strained and precise. "I would like the record to show that I remain opposed to being used as architecture."

Kesh leaned closer to the case. "Still with us, counselor?"

"In copied, partial, improperly duplicated, and deeply annoyed form."

"That sounds alive enough by Orrowen standards."

"Do not flatter the jurisdiction."

Mara felt relief so sharp it hurt. Arveth was not alive. She would not lie to herself about that. He had spent his last death in Book One's furnace truth, choosing finality when everyone else wanted to keep him useful. But records had habits, and Orrowen had worse ones. His filings, arguments, objections, and copied witness fragments had followed them through archive and engine, not the man entire, but enough of him to be angry about being misread.

Enough to hurt when the bells rang.

Saelith stood beside Mara with the red fungal bell at her throat. "We correct the sentence."

"We try," Sava said.

"You do not sound confident."

"I am a clerk. Confidence is what judges have instead of preparation."

The courthouse doors opened.

Not inward. Not outward. They unfolded into categories. Public gallery, sealed archive, prisoner intake, witness confession, foreign appeal, mercy petition, execution record. Each door showed a different hallway behind it. Each hallway held the sound of turning pages.

Assistant Registrar Othel, who had insisted on escorting them because mixed witness without procedural supervision apparently offended his remaining bones, lifted a finger. "Do not choose mercy petition."

Caldus glanced at him. "Why?"

"Mercy acknowledges the sentence."

Ilyr nodded slowly. "Foreign appeal?"

"Foreign appeal confirms Orrowen cannot correct itself without external authority."

Maelin's eyes hardened. "Sealed archive?"

"You may enter. You will not leave before your descendants are embarrassing."

"I have no descendants."

"Then strangers will have to manage it."

Mara looked at the remaining doors. "Witness confession."

Sava shook her head. "That makes Arveth's personhood dependent on our pain."

"Prisoner intake?"

"That makes us prisoners."

Kesh held up both hands. "I vote strongly against the educational option."

Mara stared at the doors until their labels blurred. The courthouse was offering paths that all assumed the same hidden truth: the sentence mattered. Appeal it, confess to it, beg mercy from it, become trapped by it, but begin by accepting that the court had the right to continue killing Arveth one morning at a time.

She remembered what he had said in the furnace below Ashgate, before final fire took what remained of his voice. Unknown is not empty.

"Public gallery," Mara said.

Sava looked at her.

"We appear where the sentence is being performed," Mara said. "Not where it asks us to justify ourselves."

The public gallery door brightened.

"Finally," Arveth said from the ledger case, "someone insults the premise."

They entered.

The gallery beyond was immense and narrow, as if a cathedral had tried to become a courtroom and lost both arguments. Benches rose in tiers to a ceiling painted with civic constellations: scales, bridge, inkpot, lamp, river gate, open hand. Every bench was full. Orrowen dead sat shoulder to shoulder in robes, work coats, armor, funeral linen, market aprons, children's slate-smudged sleeves. Some had no faces left, only names burning where features should have been. Some were translucent. Some were only shadows holding papers. At the front stood a judge's bench made from fused emergency seals.

Behind it sat nine judges.

Only three were awake.

That, Sava whispered, was part of the problem.

The central judge had a skull of polished gray bone and eyes like ink under ice. The judge to his left was a woman whose skin had become parchment over blue flame. The judge to his right was a dark-elf shadow in old court robes, face hidden behind a violet veil. The six sleeping judges sat under dust, their seals dim, their names covered with cloth.

Before the bench stood a man made of repetition.

He looked like Arveth and did not. Tall, narrow, robe hanging from shoulders too tired for flesh, hair bound back with a strip of court linen. His outline flickered every time the bells rang. Behind him, chains ran not from his wrists but from stacked copies of his own sentence. Each copy hooked into him like a leech.

Mara's throat closed.

The ledger case snapped open.

Arveth's copied voice emerged thin and furious. "I object to that representation of my posture."

The repetition-man turned.

For one breath the whole gallery inhaled.

"Oh," the figure said. It was Arveth's voice without the jokes. "You came back wrong."

"So did you," said the ledger.

The central judge struck the bench. "Sentence cycle continues. Arveth of Orrowen, convicted under emergency continuance for obstruction of necessary containment, refusal of exhaustion, and unlawful persistence of personhood after civic utility expired."

Mara stepped into the aisle.

Caldus moved with her. Saelith too. Brakka came behind them, maul low, each step a bridge oath in waiting. Tavi walked with the root-hound's empty collar around her wrist. Kesh carried no visible knife, which meant he had at least four. Ilyr and Maelin bore the ledger case together. Edrin and Sava walked like citizens entering a room that had forgotten it belonged to them.

"Appearance," Sava called. "Mixed witness appears to correct standing."

The parchment-skinned judge opened one burning eye wider. "Standing of mixed witness unrecognized under emergency continuance."

"Emergency expired," Sava said.

The dark-elf judge behind the violet veil answered. "Expiration unacknowledged by oversight."

"Oversight expired."

"Unacknowledged."

"That is the problem," Sava snapped.

The gallery murmured. The sound went on too long, hundreds of dead citizens making the noise of a city that had spent centuries muttering in kitchens, markets, alleys, offices, funeral houses, and never in the room where the wrong kept happening.

The central judge struck again. "Defendant will answer whether he persists as person, record, civic asset, or hostile remainder."

The repetition-man closed his eyes.

The ledger Arveth went silent.

Mara understood, then, what the court had been doing.

It was not trying to kill him once. It was making him prove himself a person every day until proof became exhaustion. Every answer fed the sentence. Every argument made the hook deeper because the court did not care what he said, only that he kept spending himself to say it.

"No," Mara said.

The word cracked across the gallery.

The judges turned toward her.

The central judge's ink eyes narrowed. "Identify speaker."

"Mara Venn. Self-filed standing. Mixed witness."

"Relationship to defendant?"

She almost said friend. She had known Arveth mostly as voice, record, witness, irritation, sacrifice. Friend felt both too small and too sentimental. The court would eat either.

"Not relevant."

The gallery rustled.

The judge leaned forward. "All standing derives from relation."

"No," Mara said again. "That is how you keep the trial alive. You ask him what he is. Then you ask who confirms it. Then you ask what confirms them. Then you wait for everyone to get tired enough to call the unanswered question a verdict."

The dark-elf judge's veil stirred though there was no wind. "Argumentative."

"Yes."

"Untrained."

"Also yes."

"Potentially inadmissible."

Kesh coughed. "Happens to her constantly."

Mara kept her eyes on the bench. "I am not here to prove Arveth is a person."

The repetition-man opened his eyes.

The hooks in his sentence copies loosened, barely.

The central judge struck the bench hard enough to make dust fall from the sleeping judges. "Then you concede."

"No. I refuse your right to ask."

The courthouse shook.

Pages flew from shelves. Bells swung without ringing. In the high gallery, children shrieked with delight until the old woman in the ink veil told them to hush because history was finally being rude in the proper room.

The parchment-skinned judge whispered, "Improper correction path."

Sava stepped beside Mara. "Proper paths have failed for four hundred and twelve years."

Edrin Vale joined her. "Citizen witness supports refusal."

Assistant Registrar Othel, looking as if he might perish from either fear or professional excitement despite already being dead, lifted his stamp. "Clerk's office notes material procedural irregularity."

"Denied," said the central judge.

Othel stamped the air anyway.

MATERIAL PROCEDURAL IRREGULARITY appeared above the aisle in blue fire.

The gallery erupted.

The court did not.

The fused emergency seals behind the bench ignited violet and white. Lumenorath and Khar Veyl marks, layered over Orrowen civic law, woke as if offended by the possibility of retirement. The three awake judges rose together. From the floor between Mara and the bench, chains of written law lashed upward. They struck Caldus's sword and wrapped his wounded arm. They looped around Saelith's wrists, forcing white light into her palms. They snared Brakka's maul, Ilyr's throat, Maelin's old binding scars, Kesh's coin-moth debt, Tavi's empty collar.

The court fought with what everyone carried.

Mara's chain came last.

It emerged from the floor as black cinder script and wrapped around her injured forearm, sliding under Caldus's bandage into the cut. It found the ash-runner she had been, the hungry girl useful because she could carry messages faster than someone important could be bothered to walk, the frightened woman who had almost let every name in the furnace use her mouth because being useful felt safer than being herself.

The central judge spoke. "All witnesses exhaust."

The chains tightened.

Vorrakai's stillness stirred below the courthouse.

Mercy, it seemed to say, though no voice had fully formed. You do not have to keep arguing.

Mara nearly believed it.

Then Arveth laughed.

The repetition-man and the ledger laughed together, one bitter, one bright.

"Oh, absolutely not," said the ledger. "I did not spend a perfectly good death escaping Mordane's arithmetic so a bench of under-maintained legal furniture could rediscover tyranny in triplicate."

The repetition-man turned from the judges to the gallery.

"Citizens," he said.

The word broke the first chain.

Not Mara's. His.

"I have argued my humanity long enough to become evidence against myself. I am finished."

The central judge raised both hands. "Defendant will answer."

"No," Arveth said.

Every copy of his sentence flared.

Mara felt the cost before she understood it. The copied voice in the ledger dimmed. The repetition-man lost color. Arveth was refusing to feed the trial, and because the trial had eaten so much of him, refusal meant tearing himself out by the roots.

"Arveth," Mara said.

"Do not make a touching speech," the ledger whispered. "I have standards."

The repetition-man smiled at her, and for a moment he looked like himself. "Unknown is not empty, Mara Venn. Neither is silence. Use it."

Then he turned to the prisoners.

Mara had not seen them until that moment because the court had taught everyone where not to look. Along both walls stood rows of figures chained to docket columns: workers, soldiers, clerks, children grown old in repetition, light-elf healers listed as contaminants, dark-elf wardens listed as necessary liars, human refugees who had died carrying orders no one claimed. Each was being asked the same question in a different legal costume.

Prove you count.

Prove you count.

Prove you count.

Arveth lifted his hands.

His sentence copies tore open.

The memory inside them poured out, not as light but as scenes: Arveth before the war teaching a child to file a land claim; Arveth arguing bridge fees with a troll matriarch and losing politely; Arveth laughing in a market with ink on his nose; Arveth in prison sharing his bread with someone whose name the court had replaced; Arveth in Ashgate's furnace telling Mara that personhood had to be maintained; Arveth choosing final death; Arveth objecting, always objecting, not because argument saved him but because argument made a record for the next person.

The scenes struck the docket columns.

Chains broke.

The gallery surged to its feet.

Caldus snapped the law-chain from his wounded arm with a grunt that was half pain and half command. Saelith let white fire rise in her palms, then deliberately stained it red-gold with the fungal bell's memory, burning the chain without purifying what it held. Brakka planted her maul between two floor stones and declared, "Bridge law enters," with such force that three benches became temporary crossings and dozens of chained prisoners stumbled free along them.

Tavi pressed the root-hound's empty collar to the chain around her wrist. "You do not get to use grief as a lever," she told the court, and the brass clasp bit through script like a tiny loyal jaw.

Kesh looked at the coin-moth chain on his wrist. "Nontransferable, remember?" he said, and slid free because Orrowen's own clerk had stamped it that way.

Ilyr could not break his chain. It had found every name he had sold. He went to his knees.

Maelin caught the chain with both hands.

"House authority contested," she said.

"Maelin," he rasped.

"Do not argue. I am enjoying this."

She pulled. The old retention scars on her arms split, not bleeding this time but shedding violet light. Ilyr's chain cracked.

Mara stood in the center of it all with cinder script under her skin and no heroic answer large enough for the room.

So she used silence.

She did not command the cinder. She did not sing the court into surrender. She did not make herself a saint, weapon, judge, or replacement law. She held up her injured arm, let the chain write its question through her blood, and refused to answer.

The court waited.

The chain tightened.

Mara said nothing.

The question starved.

All across the courthouse, old sentences lost their teeth.

The central judge cracked from crown to jaw. The parchment-skinned judge burst into loose pages that flew into the gallery, each page blank for the first time in centuries. The dark-elf judge behind the veil lifted one hand, removed the violet cloth, and revealed no face at all, only a seal stamped over emptiness.

"Oversight expired," Maelin said to it.

The faceless judge bowed.

Then the six sleeping judges woke.

They did not rise. They did not attack. They looked at the broken bench, the freed prisoners, the gallery standing, the citizens entering their own courthouse at last.

One by one, they removed the cloths from their names.

Sava Rennet climbed the judge's dais, seized the central stamp, and looked down at the hall.

"Correction filed," she said.

The stamp fell.

Arveth of Orrowen, sentence void for lack of standing.

Emergency continuance expired.

Death no longer deferred.

Witness exhaustion denied.

The repetition-man exhaled.

He became less.

Not destroyed. Not rescued into life. Less trapped.

The ledger voice was very faint when it spoke. "Well. That was almost properly done."

Mara swallowed grief. "Almost?"

"You allowed Kesh to speak in court."

"Unavoidable emergency."

"Accepted."

The repetition-man touched two fingers to his brow in the old Orrowen salute.

"Do I lose you?" Mara asked.

His smile turned gentle, which was unfair of him.

"You never had me in the way loss means. That is not cruelty. It is accuracy."

"I am tired of accuracy."

"Then let it carry itself for a while."

Behind him, the freed prisoners moved into the gallery, not leaving yet, not knowing how. The courthouse doors had changed. Public gallery remained open. Witness confession had closed. Mercy petition had become civic repair. Prisoner intake had become citizen return.

The bells rang again.

This time they did not say his sentence.

They rang one clear note.

Arveth's repetition bowed to the court, to the citizens, to Sava, to Edrin, to the company, and last to Mara.

Then he stepped backward into the freed crowd and became a voice among voices.

The ledger case closed by itself.

Mara stood in the aisle until Saelith touched her elbow, the permission asked and given in the same small pressure.

"He is gone?" Saelith asked.

Mara listened.

The cinder in her blood heard many things: the dragon-moon below, the ruined Glass Engine trying to pulse, armies in under-roads, Vorrakai's grief moving closer.

She did not hear Arveth as a single voice.

"No," she said. "He is not being used."

Outside, Orrowen's courthouse square had changed. Citizens crowded the steps. Freed prisoners blinked at canals, shops, ghost-lamps, children, notices, small arguments about repair fees, the ordinary impossible continuance of a city that had been told it was over and had refused to end politely.

Far below, something heard the court stop killing one man.

Vorrakai spoke Mara's name.
""",
    23: r"""## Chapter 23: Vorrakai Speaks Kindly

The first time Vorrakai spoke clearly, it did not sound like a monster.

That was the worst of it.

Mara had expected thunder, furnace roar, dragon bone grinding against the roots of the world. She had expected command because commands were honest about their violence. She had expected hunger because every crown, engine, court, and prophecy that reached for her had wanted to eat something.

Vorrakai sounded tired.

Mara.

Her name moved through Orrowen's canals after the courthouse bells changed. It passed under bridges, through ghost-lamps, along dragon-scale paving, into the cut on her forearm and the old ash behind her ribs. No one else flinched at first. The voice was for her, or it had learned to arrive where her loneliness could mistake it for privacy.

She stopped at the edge of a canal whose water was black enough to show no reflection. The company had left the courthouse square under Sava's sharp direction, taking a lower civic road toward the outer battlefield. Freed prisoners and newly frantic clerks were still arguing behind them. Somewhere above the city, armies moved closer. Somewhere below, the dragon-moon slept badly.

Mara.

Saelith turned. "What is it?"

"It knows my name."

Kesh's hand went to a knife. "I dislike pronouns in this context."

Ilyr looked at the canal. "Vorrakai?"

The water did not ripple.

Yes, said the voice, and everyone heard it that time.

Caldus stepped in front of Mara despite the sling and his pallor. Brakka's maul lowered. Tavi's hand closed around the root-hound collar at her wrist. The rescued Lumenorath scouts made ward signs. Maelin whispered an old Khar Veyl denial under her breath, then stopped because denial had not saved anyone yet.

Do not fear the name, Vorrakai said. Names are the kindest thing your world has kept.

Mara hated that the sentence was beautiful.

The canal brightened.

Not with light. With memory.

She saw the first dragon before it was first. Not as the old carvings showed dragons: wings spread over mountains, fire making cities small, eyes like judgment. Vorrakai in the memory was vast and dark and young in the way mountains were young when the world had not yet wounded them into shapes. Around it flew others. Red, gold, blue, green, white as stormbone, black as deep water. They crossed the sky over a world without nations. Their shadows passed over forests, seas, plains, gnome hill-cities not yet buried, elf courts not yet divided into light and dark, human river camps, troll bridges made from living stone, goblin roads drawn by laughter and hunger and nerve.

Then the memory changed.

Dragons fell.

Not all at once. Not cleanly. Spears of star-metal. Cinder engines. Songs sharpened by fear. Treaties broken because the first victory made the second betrayal easier to justify. Mara felt each fall in her teeth. She smelled burned scale, heard hatchlings calling through smoke, saw kings and courts and desperate villages alike use dragon death as warmth, weapon, scripture, proof.

We gave memory, Vorrakai said. You made it ownership.

The vision slid to Ashgate.

Joryn's back bent over a furnace rail. Kell Ashgate washing cinder soot from a child's hair. Mara at fourteen carrying messages through alleys while men with full bellies argued whether ash-runners counted as labor or expendable speed.

You know this, Vorrakai said gently.

"Stop," Mara whispered.

The canal showed Harrowmere. Mordane's arithmetic. Dead names arranged into obedience. The furnace where Arveth had chosen not to be used. It showed Lumenorath, Serathiel's face tender with certainty. It showed Khar Veyl children learning which truths could be sold and which could only be inherited as knives. It showed Tavi's root-hound half-sealed in glass. Caldus with a lance through his arm. Kesh's wrist marked with roads that might still fail. Saelith watching her old prayers become weapons in other mouths.

No one should have to carry this much choice, Vorrakai said.

Mara could not breathe.

Because it was not wrong.

That was the trap. Not falsehood. Not flattery. Truth arranged toward surrender.

"What do you want?" she asked.

The canal deepened until the black water became sky. In it hung the dragon-moon beneath the world, pale and immense, its closed eye visible through layers of stone and civic law and old sin.

Rest, Vorrakai said.

"For whom?"

All.

Kesh laughed without humor. "Ah. Universal offers always hide appalling details."

Vorrakai did not grow angry. I will not burn your cities. I will not crown myself. I will not demand worship. I will end the bargain by which every living thing must choose, harm, regret, and choose again. The dead will not be forced to argue. The living will not be forced to become useful. Grief will stop moving.

The words entered them one by one.

Saelith's hand trembled. Mara saw what the voice offered her: every cleansing litany unsung, every person she had failed to save held quiet beyond judgment, the Pale Bough no longer able to twist mercy into order because no one would need mercy at all.

Caldus closed his eyes. His offer was simpler. Lay down the sword. No more oaths to break. No more bodies between danger and someone he loved. No more discovering that obedience had been cowardice too late to save the dead.

Tavi's grief sharpened the air. No more machines making choices. No more apprentices buried. No more loyal things dying because she had taught them to follow.

Kesh looked at his wrist and went very still. No more unpaid roads. No villages defaulting. No cleverness needed because no one would ever again be trapped behind a locked gate.

Even Brakka bowed her head. Troll bridge law was made from the knowledge that rivers killed and crossings failed. What was a bridge in a world where no one had to cross?

Mara felt each temptation because Vorrakai did not isolate her from her friends. It used love more elegantly than cruelty ever had.

Choose for them, the voice said.

There it was.

The smallest command, wrapped in the largest mercy.

Mara's cinder cage warmed. The latch, melted in the Glass Engine and rewired by Tavi, clicked once. The flake of dead dragon memory inside wanted to answer the greater dead thing below. Of course it did. A candle wanted sunrise even if sunrise burned the house down.

"No," Mara said.

The word was weak.

Vorrakai heard the weakness and did not pounce.

You are so tired.

Mara's eyes filled before she could stop them.

Yes.

She was.

She was tired of being brave in public. Tired of seeing the clever shape of every trap and still having to walk into rooms because people behind her needed the door open. Tired of correcting names only to find deeper ledgers. Tired of how every victory became another argument over whether personhood should count this time. Tired of loving people whose pain made her own choices heavier.

Vorrakai's kindness pressed closer.

No saint. No weapon. No banner. No ash-runner. No more names thrown at you by need. Only quiet.

Mara stepped toward the canal.

Saelith caught her hand.

The grip was not gentle. It was terrified and living.

"Look at me," Saelith said.

Mara could not.

"Mara."

The voice from below and the voice beside her held the same name differently. Vorrakai held it like a cradle. Saelith held it like a door she refused to let close.

Mara looked.

Saelith's face was wet. "I want it too."

The confession broke something.

Not the temptation. The loneliness inside it.

"All my life," Saelith said, "I was promised peace if everything unclean could be cut away. I know how beautiful an ending can sound when it is tired enough. If you choose for me, even to spare me, you become another knife."

Caldus set his good hand on Mara's shoulder. "I do not want rest purchased by your surrender."

Tavi came to her other side. "And if the universe offers you a simple solution through a buried dragon corpse, check the tolerances."

Kesh swallowed. "For once, and I want this entered into whatever vindictive city ledger is listening, I am willing to keep owing."

Brakka rested her maul against the bridge rail. "Bridge exists because crossing hurts. Still worth building."

Ilyr looked down into the canal. "I have mistaken fewer choices for safety before. It was only smaller imprisonment."

Maelin's voice was quiet. "Do not make my freedom permanent by making me unable to use it."

Edrin Vale and Sava Rennet stood together, dead citizens under ghost-lamps.

"We argued too long," Edrin said. "We were also right to argue."

Sava folded her hands. "Exhaustion is not consent."

Mara breathed.

The company did not defeat Vorrakai.

They made a room in which Mara was not alone with it.

That was enough to choose inside.

She pulled her hand from above the canal and pressed it against the cinder cage. "I will not choose stillness for people who have not chosen it."

Vorrakai's grief filled the district.

For a moment every ghost-lamp dimmed. The canal water rose without spilling. Far below, the dragon-moon's closed eye twitched.

I do not want your worship, the voice said.

"I know."

I want your mercy.

"No," Mara said, stronger now. "You want my exhaustion to call itself mercy."

Silence.

Then Vorrakai laughed.

It was not cruel. That made it colder.

You are young, ash-runner.

"Yes."

You think choice is sacred because it recently became yours.

Mara flinched. The truth in it cut deep. She had been poor, used, cornered, named by need. Choice did feel sacred to her partly because she had gone so long without it.

Saelith's grip tightened.

Mara did not look away from the water. "Maybe. Or maybe people who have been denied a thing know its weight better than those who spent it casually."

The canal stilled.

For the first time, Vorrakai's attention sharpened into something like anger.

Around them, Orrowen citizens began to turn. Dead faces in windows. Clerks at doorways. Children on bridge rails. Freed prisoners from the courthouse. The city heard the argument not as doctrine but as weather changing pressure.

Vorrakai spoke through all the canal mouths at once.

The armies are coming.

The black water showed them.

Lumenorath's vanguard descended through a white-root tunnel, Serathiel at its head, robes unstained despite the under-road's filth. Hymn wagons rolled behind him on wheels wrapped in cleansing script. The Pale Bough soldiers looked frightened and righteous, which made them more dangerous than hatred.

Khar Veyl came from the opposite passage: Vaura Noct-Vey under a banner of black thread and silver seal, blade-scholar hardliners pressing at her flank, lower-canal defenders among the ranks with pump tools beside knives. Their fear wore discipline. Their discipline wore guilt.

Between them lay Orrowen's outer battlefield, an old civic mustering ground where ancient armies had once killed each other so thoroughly the stones still expected blood before discussion.

They will break the seal, Vorrakai said. Each side believes the other is the key to suffering. Let me end the equation.

Mara looked at Serathiel's white host. At Vaura's dark one. At the dead citizens of Orrowen who had been turned into weapon, warning, argument, inheritance.

"No," she said.

Then we will meet where choice fails.

The canal emptied.

Not drained. Emptied. One heartbeat black water, the next slick stone descending into a dry channel that led toward the battlefield. Along its floor, old route marks glowed: Orrowen civic chains, Khar Veyl emergency signs, Lumenorath healing script, and beneath them all, dragon-scale letters pulsing like a heartbeat.

Tavi peered over the edge. "That is not a maintenance route."

Kesh looked at the downward channel. "It is absolutely a maintenance route. It maintains our ongoing relationship with terrible decisions."

Caldus flexed his bandaged arm and winced. "How far?"

Edrin listened. "Close. Too close."

Saelith wiped her face and lifted her chin. The red fungal bell at her throat glowed like a banked coal. "Serathiel will not stop for me."

"He might stop to condemn you," Kesh said. "Some people are generous like that."

"Let him," she said.

Maelin checked the ledger straps. "Vaura will try to hold formation. The blade-scholar will look for an excuse to strike first."

"Then we deny him one," Ilyr said.

Brakka climbed down into the dry canal first. "Battlefield needs bridge."

Mara followed.

As her boots touched the channel floor, Vorrakai spoke once more, softer than before.

I will remember that you tried.

The kindness almost undid her.

Mara kept walking.
""",
    24: r"""## Chapter 24: The Armies Below

War entered Orrowen from two directions and brought its own lighting.

From the east came Lumenorath, white-root lanterns bobbing above ranks of pale armor, hymn wagons creaking behind the vanguard, banners painted with open hands and clean flame. Their light should have made the buried battlefield brighter. Instead it flattened everything it touched, sanding detail from bone walls, ghost-lamps, old bridge marks, the faces of frightened soldiers. Serathiel walked at the front beneath a canopy of living white branches that had rooted into the wagon behind him. His beauty had become severe since Mara last saw him. Mercy had burned away everything in his face except certainty.

From the west came Khar Veyl, violet lamps and black thread standards moving like night water. Vaura Noct-Vey rode no beast and carried no crown. She walked with a blade at her hip and a seal rod in one hand, surrounded by wardens, lower-canal defenders, archive clerks, hardliners, and messengers breathless from too many emergency corridors. The blade-scholar marched three paces behind her with enough obedience to be insulting. His followers carried hooked spears and the look of people who had already chosen where regret would be filed.

Between them lay the outer battlefield.

Mara had imagined a field, because surface words failed underground. Orrowen's battlefield was a cavern wide enough to lose weather in, with a roof hidden by ash-mist and old banners moving in wind from no sky. Causeways crossed it in broken layers. Some were stone, some bone, some cooled glass from wars before the Glass Engine, some dragon-scale plates chained together over black channels. At the center stood a dry riverbed full of helmets, petitions, spearheads, children's slates, rusted cooking pans, and white flowers growing without roots.

The dead had not cleared the debris.

Maybe they refused to tidy what the living kept trying to repeat.

Mara's company came out of the drained canal onto a low bridge just as both armies saw each other.

The cavern tightened.

Every soldier in both hosts seemed to inhale at once.

Saelith whispered, "Serathiel."

The light-elf priest stopped.

For one heartbeat his certainty cracked into something personal. Mara saw recognition, grief, and perhaps love if love had been starved and trained to salute. Then his gaze moved from Saelith to Mara, to the ledger case, to Edrin and Sava, to the Orrowen citizens gathering along the battlefield edges.

"Cinder-bearer," he called. His voice carried with unnatural clarity. "Step away from the unquiet dead."

The Orrowen citizens hissed.

Vaura's rod struck stone from the opposite side. "Serathiel. One more word like that and you will have to cleanse your own teeth from the floor."

Kesh glanced at Mara. "I missed diplomacy."

The blade-scholar smiled. "Let him speak. Every insult clarifies the necessity."

Vaura did not turn. "Every sentence you enjoy makes me suspect it."

Mara stepped onto the central causeway before anyone gave her permission, which was becoming a habit and maybe a flaw. Caldus moved with her, slower because of his wounded arm but no less stubborn. Saelith came too, head bare, exile colors visible. Tavi, Kesh, Ilyr, Maelin, Edrin, Sava, and the three rescued scouts followed. Brakka did not follow.

Brakka walked past them.

The troll strode to the very center of the battlefield, where three causeways met over the dry riverbed, and drove her maul into the stone.

The sound cracked across Orrowen.

"This is bridge," she said.

The declaration rolled outward. It crossed broken causeways, black channels, old trenches, ranks of living soldiers, rows of dead citizens, white-root wagons, violet seal lamps. It entered stone and found older words waiting there.

Bridge law hears.

The battlefield answered.

Every causeway lit from below.

Lumenorath's front rank stumbled as white roots tangled under their boots, not attacking, only holding. Khar Veyl hardliners found their hooked spears suddenly heavy as bridge tolls. The dry riverbed filled with ghost-water that did not wet the ground. Across it appeared countless crossings: plank, rope, stone, bone, memory, hand extended over flood.

Brakka's skin darkened from gray to river-black. Pale lines opened along her arms, not wounds, exactly, but vows becoming visible.

"No blood on crossing until terms are heard," she said.

The blade-scholar lifted his spear. "Troll oath has no standing over elven war."

The bridge under his feet vanished.

He dropped waist-deep into the dry riverbed with a sound that would have been funny in a kinder hour. His followers jerked back. Kesh covered his mouth with both hands and achieved nothing useful.

Brakka looked at the blade-scholar. "Standing granted by falling."

Even Vaura's mouth twitched.

Serathiel raised one hand, and the white-root branches behind him stirred. "I recognize no bridge built over corruption."

The ghost-water rose around his boots.

He looked down.

An Orrowen child, translucent and solemn, stood in the water before him holding a slate. On it she had written Matriarch Aurenne's forbidden line in careful script.

If memory is the wound, then we must learn not to cut it out.

Serathiel's face changed.

Saelith saw it and went very still.

"You know it," she called.

His eyes lifted to hers. "I know many lines twisted by desperate mouths."

"You omitted this one."

"I preserved what would save the living."

"You preserved the part that let you decide which living counted."

The white-root branches lashed toward her.

Bridge law caught them midair.

The roots hung above the causeway, trembling, unable to cross while terms were unspoken. Serathiel's serene mask cracked further. Behind him, some Pale Bough soldiers looked at one another. The rescued scouts shifted closer to Saelith, not yet loyal, not even convinced, but no longer able to pretend the only choices were obedience and contamination.

Vaura stepped forward from the Khar Veyl line. "Terms, then. Orrowen's standing recognized provisionally. Lumenorath withdraws cleansing writ. Khar Veyl maintains seal defense. Mixed witness reviews the old covenant."

"Generous," Ilyr murmured, "if one ignores the dagger under every word."

Maelin's voice was louder. "No."

Vaura turned.

The battlefield loved family arguments. Every bridge light leaned in.

Maelin walked to the edge of the Khar Veyl rank, sleeve torn, old retention scars visible. "No provisional standing. No review owned by Khar Veyl. No seal defense that returns Orrowen to a locked room."

Vaura's expression did not soften. "Daughter."

"Do not use the office-word for property."

A murmur went through the dark-elf ranks. Some shocked. Some approving. Some frightened because truth spoken aloud had a way of requiring new paperwork.

The blade-scholar tried to climb from the riverbed. Brakka placed one foot on his spear shaft without looking at him.

Ilyr joined Maelin. "House Noct-Vey's private seals appear in the old covenant. Our authority is evidence, not solution."

Vaura's jaw tightened.

"You would shame the house before enemies?"

"I am tired of hiding shame until enemies weaponize it better."

From the Lumenorath side, Serathiel's voice rang out. "You see? Khar Veyl confesses corruption and still asks to keep the prison key."

Sava Rennet stepped onto the causeway, climbed a broken plinth, and unrolled a sheaf of courthouse corrections with the flair of a woman who had waited centuries to be irritating at scale.

"Orrowen objects to being discussed as prison, key, corruption, resource, proof, battlefield, inheritance, wound, or weapon before citizen standing is entered."

Serathiel looked at her as if a document had grown teeth.

"You are dead," he said.

"And yet punctual."

The Orrowen citizens along the battlefield edges laughed.

It was not a kind laugh. It was a city remembering lungs.

Mara felt the moment tilt. Humor made the dead harder to sanctify or fear. It made them people in a way speeches could not. Serathiel felt it too; his hand tightened. Vaura felt the hardliners shifting behind her. Everyone on that battlefield had brought a story in which they alone stood at the necessary center, and Orrowen was making the story crowded.

Then the Choir arrived.

They came through the dry riverbed, not marching but appearing where no one had been looking: men and women in ash-gray robes, faces serene, eyes filmed with pale cinder. Some were living. Some were dead. Some were the terrible middle left by old dragon dreams. They carried no weapons. That made them worse. Soldiers knew what to do with blades. They did not know what to do with people who smiled as if already forgiven.

Vorrakai's Choir opened their mouths.

The note they sang was almost silence.

White-root lanterns dimmed. Violet lamps guttered. Ghost-water went still. The bridge lights flickered under Brakka's feet.

Mara's cinder cage pulsed.

Across the battlefield, both armies faltered. A Lumenorath soldier lowered his spear and began to weep. A Khar Veyl warden dropped her seal rod. An Orrowen dead man sat down on the edge of the causeway with sudden, heartbreaking relief. Even Serathiel and Vaura swayed, two leaders who had carried certainty like armor discovering how heavy armor was when someone offered to take it off forever.

The Choir's song said what Vorrakai had said to Mara, but without words.

No more.

No more.

No more.

Mara almost knelt.

The battlefield blurred. All its arguments, terms, corrections, crimes, names, debts, choices became a single unbearable noise. She felt every army's fear at once. She felt Serathiel's conviction that if he stopped, all he had sacrificed would become murder instead of mercy. She felt Vaura's terror that one loosened seal would open a flood no law could survive. She felt Orrowen's exhaustion, Khar Veyl's guilt, Lumenorath's dread, Tavi's grief, Caldus's pain, Kesh's debt, Saelith's exile, Brakka's vows cracking her skin.

The Choir offered quiet.

Mara's knees bent.

Saelith shouted her name.

Not enough.

Caldus tried to reach her, but his wounded arm failed.

Not enough.

Tavi threw the root-hound's empty collar.

It struck Mara's cinder cage with a bright, ridiculous clang.

The sound was small.

It was enough.

Mara sucked in a breath that hurt like first life.

She grabbed the collar before it fell and held it against the cage. Brass, grief, choice. A dead machine's last loyalty interrupting the first dragon's perfect sorrow.

"No," she said.

The Choir did not stop singing.

Mara walked toward them.

Each step tried to become surrender. Each step remembered Ashgate roads, Harrowmere chains, Lumenorath's white orchard, Khar Veyl's drowned archive, the fungal forest, mirror cavalry, Glass Engine, courthouse bells. Every place had offered a different reason to let someone else decide what persons were worth. This reason was gentler. That did not make it clean.

"You do not get to call exhaustion peace," Mara said.

Her voice did not carry far enough.

Brakka heard anyway.

The troll lifted her maul from the stone. Blood, or vow-light, ran down both her arms. The battlefield trembled, bridge law straining under army, dead city, Choir, and dragon grief.

"Terms are not finished," Brakka said.

She brought the maul down again.

The causeways answered with every crossing they had ever been: troll-built river spans, gnome maintenance catwalks, goblin rope roads, human planks over mine floods, elven treaty bridges, Orrowen civic steps across canals. Across the battlefield, soldiers looked down and saw not a field for killing but the thing a battlefield had been before rulers named it: ground between people who had to decide whether to cross.

"No blood on crossing until terms are heard," Brakka repeated.

This time the dead said it with her.

Thousands of Orrowen voices rose from the battlefield edges, courthouse square, canal bridges, ghost-lamp windows, freed prisoner lines.

No blood on crossing until terms are heard.

The Choir's song broke.

Not ended. Broken enough.

Mara reached the nearest singer, a human woman with ash-gray robes and tears running down her face. The woman looked at Mara with gratitude so pure it hurt.

"He will stop it," the woman whispered.

"He will stop you," Mara said.

"Yes."

"That is not the same."

The singer wept harder.

Mara touched her shoulder, not to command, not to cleanse, not to arrest. "Choose later if you must. But choose with your own mouth."

The woman's song faltered.

Around her, other Choir voices cracked as living lungs remembered they were allowed to breathe badly.

Serathiel seized the opening.

"Now!" he shouted.

White roots tore forward from his wagons.

At the same moment, the blade-scholar dragged himself from the dry riverbed and screamed for Khar Veyl to strike.

Both armies surged.

Bridge law held for one breath.

Then the battlefield began to tear.

Caldus ran to the Lumenorath front and took the first spear on his sword, bad arm and all. Saelith stepped into Serathiel's white roots and burned them red-gold from within. Ilyr threw the ledger case to Maelin and drove a stolen seal rod into the causeway, turning a hardliner charge into a sudden legal bottleneck. Kesh appeared beside the blade-scholar, cut his belt, stole his emergency writ, and kicked him back into the riverbed.

"You are not having a dramatic exit twice," Kesh said.

Tavi was already at the hymn wagon. She climbed it like a woman with a professional grudge against wheels, jammed a glass pin into its root axle, and shouted, "If anyone asks, this was a manufacturing defect!"

Vaura saw Serathiel's roots break bridge law and made the first decent choice Mara had seen from her.

"Hold!" she commanded Khar Veyl. "Defensive formation. Strike no Orrowen citizen."

The blade-scholar howled from below. Several hardliners ignored her.

Maelin stepped in front of them.

She held the ledger case like a shield. "House Noct-Vey authority contested. Orrowen standing entered. Strike me if your emergency needs a daughter shaped like a door."

They stopped.

Not from mercy. From witness.

On the Lumenorath side, the rescued scouts ran to their own ranks. The shaved-headed scout shouted Matriarch Aurenne's forbidden line until her voice broke. The young scout held up the fungal bell vial Saelith had given him. The standard-bearer, shaking, planted his torn white banner upside down.

"Parley under bridge law!" he cried.

Serathiel stared at him as if betrayal had learned his hymns.

Mara reached Brakka at the center.

The troll was on one knee.

The vow-lines along her arms had become cracks. Through them shone water, stone, old sunlight on rivers Mara had never seen.

"Brakka."

"Bridge holds," Brakka said.

"At what cost?"

"Question later."

"No."

Brakka's dark eyes shifted to her. "Good. You learn."

Mara put the root-hound collar around the haft of Brakka's maul. Tavi saw and understood at once. She ran to them, slapped both hands onto the collar, and began muttering calculations that sounded like insults to physics. Kesh joined, tying the stolen emergency writ around the collar because if law wanted to behave like rope he would treat it like rope. Saelith added the red fungal bell. Ilyr and Maelin pressed the ledger against the maul. Caldus, bleeding again, set his sword across the haft like an oath he had chosen rather than inherited.

Edrin and Sava stepped into the ghost-water.

"Orrowen appears," Edrin said.

"Citizen standing entered," Sava said.

Mara placed her injured hand on the maul last.

The cinder in her blood answered the dragon-scale under the battlefield.

Vorrakai's presence surged below them.

The dragon-moon's eye opened a slit.

Not fully.

Enough.

Pale light rose through every crack in the field. Soldiers froze. Dead citizens turned. Serathiel fell silent. Vaura looked suddenly young and terrified. The Choir dropped to their knees, some in joy, some in horror, some because their legs had simply remembered fear.

In that light, every side saw what they had come to use.

Not a resource.

Not a prison.

Not a god.

A vast dead dragon body curled beneath the world, dreaming because the living had built too many locks from its bones and called the locks peace.

Mara heard Vorrakai breathe.

Soon, the first dragon said.

The eye closed.

The battlefield remained.

Bridge law held.

No army moved.

Brakka bowed her head over the maul, still on one knee but alive. Tavi kept muttering, hands shaking. Caldus leaned against his sword. Saelith faced Serathiel across the stopped roots. Vaura faced Maelin across the held spears. Orrowen citizens filled the causeways until no one could pretend the dead were an empty category.

Mara stood at the center of armies that wanted a weapon, a saint, an answer, a surrender.

She gave them none of those.

"Terms," she said.

Her voice carried through the whole cavern.

"Now."

Above the battlefield, the old banners moved in wind from no sky.

Below it, the moon dreamed with one eye almost open.
""",
}


DEEPENING: dict[int, str] = {
    22: r"""It did not speak again at once.

That was almost worse.

The courthouse had changed, and every change needed witnesses before it trusted itself. Freed prisoners stood in clusters on the steps, uncertain whether they were allowed to leave, uncertain whether leaving was a trick, uncertain whether a city that had made them prove personhood for centuries could become ordinary enough to contain errands. Orrowen citizens came toward them slowly. No one rushed. Some bowed. Some offered water that did not steam in dead hands. Some simply said names.

Mara watched one old soldier, translucent from the waist down, touch the face of a woman who had been chained two columns from Arveth's repetition. They did not embrace. They argued immediately about whether she had been foolish to volunteer for a river gate defense without proper boots. Then both began to cry.

Kesh stood beside Mara with unusual tact for almost half a minute.

"Do not tell anyone," he said at last, "but I am beginning to suspect paperwork can be dramatic."

"Your secret is safe."

"My reputation depends on it."

Sava Rennet emerged from the courthouse carrying three stamps, four ledgers, and the expression of a woman who had stolen back her own desk from history. Assistant Registrar Othel followed with a stack of complaint forms and a reverence that was trying very hard to remain professional.

"The sentence is void," Sava said. "The related dockets are unstable. We opened more cells than expected."

"That sounds good," Tavi said.

"It is also a crisis."

"Most good things arrive with terrible implementation."

Sava looked at her, considered, and nodded. "Yes. You may assist later if you promise not to describe clerical infrastructure as stupid where it can hear you."

Tavi's mouth twitched. "I promise to be specific."

Mara turned back to the courthouse doors. "Arveth?"

Edrin Vale stood at the threshold, head bowed. The old civic light inside him had brightened since the correction, but his face looked more sorrowful, not less. "No single voice. Many released records. He is in the city now as witness should be, dispersed by consent."

"That should comfort me."

"It may, later."

Saelith came to Mara's side. "You did not save him by keeping him."

Mara laughed once, empty. "That sounds like something wise people say when no one wants to hear it."

"I despise how often wisdom arrives dressed as loss."

Caldus sat on the lowest step while a dead medic argued with a living Lumenorath scout over whether his shoulder wound counted as contaminated by salt cavalry. He looked pale, stubborn, and too tired to hide either. "Arveth chose what remained of himself," he said. "You honored that."

"You make it sound clean."

"No." Caldus flexed his good hand. "I make it sound chosen."

Above the square, a notice changed.

ARVETH OF ORROWEN, SENTENCE VOID.

Below it, another line appeared in smaller letters.

PUBLIC CORRECTION CONTINUES BY CITIZEN ACTION.

The whole square read it.

Mara felt the words enter Orrowen like rain entering soil. Not enough. Never enough. But not nothing. Around the courthouse, citizens began taking down other notices, comparing dockets, calling for relatives, arguing over where newly freed people should sleep. A city did not heal because a bell changed. It became responsible for what the bell had hidden.

Then the canals went black.

Ghost-lamps dimmed one by one, not extinguished, only listening. The ordinary clamor of the square thinned. Kesh's coin-moth mark folded tight under his skin. Tavi's root-hound collar cooled until frost gathered on the brass. Saelith's red fungal bell turned inward, its glow hidden as if a hand had closed around it.

Mara heard her name from below the city.

Not a shout.

An invitation.

She knew before anyone spoke that the trial had only opened the next door. Arveth's sentence had stopped, and some immense grief beneath the world had noticed the shape of that mercy and decided to answer with its own.

When Vorrakai spoke her name again, every freed prisoner in the square looked down.""",
    23: r"""The dry canal did not hurry them toward the battlefield.

It made them walk through what armies preferred to skip.

The channel sloped under narrow bridges and behind houses whose back doors opened onto old flood stairs. At each landing, Orrowen had left evidence of interrupted lives. A copper pot still hanging over a cold stove. A child's boot sealed inside clear resin to preserve the name stitched into its cuff. A mural of blue fish painted by hands that had not agreed on perspective. An old election notice where three candidates, all dead, had continued adding campaign insults in different inks for centuries.

Kesh slowed before the notice. "That one promises lower canal tolls and revenge against ducks."

Tavi glanced over. "There are no ducks underground."

"A visionary platform."

Mara was grateful for the nonsense because the canal walls kept showing Vorrakai's offer in smaller, meaner mirrors. Here was a doorway where a family had been separated by emergency locks. Here was a bridge where healers had chosen who crossed first and never forgiven themselves for the second name. Here was a maintenance ladder with claw marks from someone who had tried not to be stable, indexed, contained, or saved.

No more, the Choir's almost-song had promised.

The words clung to the stone even after Vorrakai's voice withdrew.

At a bend where the canal widened, they found a shrine that was not a shrine until Mara understood it. Hundreds of small objects had been wedged into cracks between dragon-scale blocks: buttons, teeth, broken seal rings, toy wheels, goblin route beads, scraps of white-root, dark-elf hair pins, human ash tags, gnome measuring tabs, troll bridge pebbles worn smooth by thumbs. Nothing matched except the need to leave proof that someone had stood there and chosen to keep going.

Brakka touched one of the pebbles. Her huge face softened. "Crossing shrine."

"For travelers?" Saelith asked.

"For those who nearly stopped."

No one moved for a moment.

Then Tavi unwound a sliver of wire from her sleeve, bent it into the rough shape of a dog with deeply inaccurate legs, and pushed it between two blocks.

"There," she said fiercely to nobody. "You are filed as impossible to standardize."

Kesh took a coin from inside his boot. Not a valuable coin. That would have been easier for him. This one was rubbed nearly smooth, pierced through the center, tied with red thread. He held it longer than he meant to.

"Kavik road token," he said when Mara looked.

"You do not have to."

"I know. That is why it counts."

He set it beside Tavi's wire hound.

Caldus had nothing on him that was not practical except the torn scrap of Mara's scarf binding his sling. He cut one loose thread, rolled it between his fingers, and left it on the shrine without ceremony. Saelith added a white petal from the root-scar in her sleeve, then touched the red fungal bell as if asking it to witness the contradiction. Ilyr removed a small archive pin from his collar, one of the last signs of office he had kept because shame sometimes disguised itself as memory. Maelin placed beside it a broken link from her old retention chain.

Mara had no relic she trusted.

Everything she carried was useful, dangerous, borrowed, or needed later. Ashgate cloth. Cinder cage. Knife. Ledger copies. Names. Hunger. The shrine did not ask for treasure. It asked for proof that she understood nearly stopping was part of the road too.

She found a bit of black glass in her pocket from the Glass Engine bridge. It had cut through the fabric and nicked her thumb more than once. She set it among the other objects.

"Not noble," she told it, remembering Tavi's words.

"No," Tavi said. "Still ours."

They moved on.

The canal narrowed until they had to walk single file. The walls leaned close enough that Mara could touch both sides if she spread her arms. The dragon-scale under her left hand was warm. The civic stone under her right was cold. Between them, her body felt like a small argument history had somehow failed to settle.

Behind her, Saelith spoke quietly to one of the rescued scouts. The young man, the one whose hands shook, asked what exile felt like. Saelith did not answer quickly.

"At first," she said, "like falling out of the only story where you know your lines."

"And now?"

"Like discovering the story had margins."

"That sounds lonely."

"It is." A pause. "It is also where people wrote warnings I needed."

Ahead, Caldus and Brakka discussed whether bridge law had provisions for a battlefield with three or more hostile entities, a buried dragon-moon, and an active metaphysical invitation to surrender. Brakka said yes. Caldus asked how specific the precedent was. Brakka said, "Specific enough if brave." He accepted this with the expression of a man filing concerns for later.

Kesh drifted back to Mara. He did not look at her.

"If I start singing about peaceful oblivion, stab me lightly."

"Lightly?"

"Enough to redirect. Not enough to damage charm."

"That is a narrow target."

"I have faith in you."

They walked three more steps.

"Thank you," he said, so quietly the canal almost took it.

"For what?"

"Not guaranteeing the debt. I thought you would. I was ready to be furious and grateful and unbearably handsome about it."

"Sorry to deny you range."

"Cruel leadership."

Mara smiled despite everything.

Then the canal opened onto a watch pocket overlooking the battlefield approach, and all small warmth vanished.

Below, white light moved through one tunnel and violet through another. Between them, Orrowen's outer field waited in old ash-mist. From this distance the armies looked almost beautiful: order entering darkness, banners steady, lamps unwavering, thousands of individual fears hidden by formation.

Mara thought of the crossing shrine. Of nearly stopping. Of all the tiny proofs left by people who had not wanted to be turned into categories.

Vorrakai had offered rest because it knew how badly rest was needed.

That was why it could not be allowed to choose for them.

Brakka stepped to the edge of the watch pocket and looked down at the converging lights.

"Battlefield," she said.

It did not sound like fear.

It sounded like a bridge seeing a flood.""",
    24: r"""The first term was silence.

Not Vorrakai's silence. Not the Choir's soft suffocation, not the court's exhausted waiting, not the silence rulers used after ordering someone inconvenient removed. This silence had edges. It was made by thousands of people holding back the old sentence long enough for a new one to be attempted.

Serathiel broke it badly.

"You would negotiate with infection while the root of death wakes beneath us?"

Saelith turned toward him. "I would negotiate with people while men call them infection."

"You were my brightest mercy."

"I was your most obedient knife."

The words crossed the causeway and struck harder than flame. Lumenorath's ranks shifted. Mara saw soldiers hearing what had been hidden inside their honor, not all at once, not enough to remake them, but enough to make certainty stumble.

Vaura used the stumble. "Khar Veyl will suspend first strike if Lumenorath withdraws cleansing writs and recognizes Orrowen standing under mixed witness."

"Khar Veyl recognizes first," Maelin said.

Vaura's gaze cut to her.

Maelin did not look away.

The blade-scholar, still in the riverbed and apparently determined to lose with consistency, spat blood and salt. "The daughter does not speak for the Seat."

Sava Rennet looked down at him. "The Seat is not currently in the riverbed."

Kesh sighed happily. "I am going to send her flowers."

"You will send me records," Sava said.

"Crueler than flowers."

Mara felt laughter ripple, small and incredulous, through people who had been ready to kill a moment earlier. The sound did not make the war smaller. It made the people inside it harder to flatten.

Brakka lifted her head. "Second term. No side owns road."

Edrin nodded. "Orrowen roads remain civic, not military, not cleansing, not house property, not Choir passage."

The ash-robed singers at the riverbed stirred when the Choir was named. Some looked bereft. Some looked relieved to be accused in public of something less holy than salvation.

"Third," Tavi said, still gripping the maul-collar assembly as if it were a device likely to misbehave. "Nobody touches the Glass Engine. Nobody repairs it, completes it, worships it, improves it, apprentices under it, or says the words 'acceptable stability adjustment' in my hearing."

Assistant Registrar Othel, who had somehow followed them onto the battlefield with a stack of forms, raised his stamp. "Technical language may require refinement."

"It may refine itself off a bridge."

Othel considered this. "Entered as emotional engineering objection pending vocabulary review."

"Good enough."

Caldus drew a breath through pain. "Fourth. Wounded pass first. Both armies. Orrowen citizens decide the route."

That term did what speeches had not. Soldiers looked at their own injured, then at the people they had been preparing to make injured. A Lumenorath medic stepped forward. A Khar Veyl pump warden answered. The two stared across a causeway that had almost become a killing line.

"Under bridge law," Brakka said, "healers cross."

The bridge lights brightened.

The medic and the pump warden walked toward each other.

No one struck them.

Mara felt the battlefield exhale.

Not peace. Not yet. Perhaps not even close. But the first living body crossed without dying, and sometimes history was dragged away from catastrophe by motions so practical the songs forgot to make them pretty.

Vorrakai watched from below.

Mara could feel its grief, patient and immense, not defeated by one held field. The dragon-moon had shown one eye and closed it again. Serathiel still believed himself merciful. Vaura still had a city to defend and secrets to answer for. The Choir still waited at the edge of surrender. The old covenant was still only half read. The Glass Engine still pulsed behind them. Every victory in Orrowen came with filings attached.

But the armies did not kill each other.

Not yet.

For that hour, not yet was a country.

Mara looked at the bridge where the first healers met, at Brakka bleeding vow-light into the stones, at Saelith standing in exile colors before the man who had made mercy cruel, at Maelin facing the mother who had loved her through chains, at Tavi holding grief together with engineering spite, at Kesh pretending the wetness in his eyes was battlefield humidity, at Caldus choosing guard duty even when his body had begun filing formal complaints.

She understood something then that no prophecy had offered because prophecy preferred cleaner shapes.

She was not leading them because she knew the road.

She was leading because she kept refusing to let any single power name the road's end for everyone else.

Above, the banners moved.

Below, the moon waited.

Between them, on a bridge declared in the middle of a battlefield, the living and dead began the ugliest, most necessary conversation in the world.

It began, as most necessary conversations did, with everyone trying to make it smaller.

Serathiel wanted to discuss contamination protocols. Vaura wanted to discuss seal jurisdictions. The blade-scholar, still being held in the riverbed by a combination of bridge law and Kesh's stolen belt, wanted to discuss treason at a volume no one appreciated. Lumenorath officers wanted casualty corridors only for the visibly living. Khar Veyl wardens wanted Orrowen citizens kept behind the third causeway. Orrowen citizens wanted the right to define the word citizen before anyone used it to exclude them.

Mara listened until the terms became another kind of battle.

Then she took the ledger case from Maelin.

It was lighter without Arveth's single voice in it. That hurt every time she noticed. But it was not empty. Pages shifted inside, eager and frightened, like a crowd at a door.

"Names first," Mara said.

Serathiel looked at her. "Names will not hold the seal."

"No. They will hold the room long enough for us to stop pretending the seal is the only thing here."

Vaura's eyes narrowed. "You are not appointed speaker."

"Good," Mara said. "Appointed speakers keep bringing armies."

Kesh made a small approving sound. Caldus closed his eyes as if asking patience from whatever gods still accepted requests from injured knights. Saelith stood very still, and Mara felt the courage of that stillness. It was not easy for Saelith to let someone else face Serathiel. It was harder because Mara was right to.

Sava opened the ledger.

Edrin read the first name.

"Ruv Ossian."

From the salt-flat edge, the corrected cavalry captain appeared in reflection along a strip of ghost-water.

"Leth of West Quay," Sava read.

"Nim of south laundries."

"Hessar, bridge-lighter."

"Matriarch Aurenne's omitted line, entered by Saelith of the Pale Bough."

"Maelin Noct-Vey, standing contested by herself and entered by mixed witness."

Maelin flinched at her own name, then lifted her chin.

"Kesh of Kavik routes, open road obligation nontransferable."

"Could we have used less official phrasing?" Kesh asked.

"No," Sava said.

"Cruel but consistent."

"Tavira Brassroot," Edrin continued, "engineer in grief, objecting to stability by force."

Tavi wiped her face with the back of her wrist and said nothing.

"Caldus Veyr, protector by choice."

The Lumenorath line murmured. The Khar Veyl line did too. Titles they understood. Choice made them suspicious.

"Brakka Stone-Over-Water, bridge declarant."

Brakka dipped her head once, though the vow-cracks in her arms still glowed.

"Mara Venn," Sava said last.

Mara's stomach tightened.

Sava did not add saint, weapon, banner, cinder-bearer, ash-runner, or answer.

"Self-filed," the clerk said. "Still appearing."

The ledger shut.

For a moment no one knew what to do with a battlefield where names had been placed before demands.

Then the shaved-headed Lumenorath scout stepped into the open with both hands raised. "Liora of White Orchard company," she said, voice shaking. "I was ordered to identify dead citizens as unclean hostiles. I request correction before I obey another order."

A Khar Veyl pump warden answered from the other side. "Vel Taryn lower-canal auxiliary. I was ordered to seal passage if cleansing began. I request correction before I drown evacuees for strategy."

One by one, more voices followed.

Not many at first. Never enough at first. A medic. A clerk. A spear carrier. A hymn wagon driver who confessed he did not know what the roots were feeding on. A dark-elf archer who had carried three emergency writs and believed none of them. An Orrowen child who shouted, "I am Selli and I hate this battle," which was admitted with unusual enthusiasm from the gallery of dead citizens.

The Choir heard the names and wavered.

Vorrakai had offered them an end to unbearable difference. Names made difference stubborn again. Painful again. Alive, even in the dead.

Mara watched Serathiel watching his own soldiers become particular. His face had gone white under the white-root glow. Vaura watched her wardens with a different fear, less holy and more political, which at least had the advantage of being honest about power.

"This will not last," Caldus murmured.

"No," Mara said.

"You know that?"

"Yes."

"Good."

She glanced at him.

He gave her the tired shadow of a smile. "It means you are seeing the field, not the song."

The first wounded crossed under the new terms.

Not in noble procession. In confusion, pain, argument, and practical urgency. Lumenorath medics carried a Khar Veyl spearman whose leg had been crushed when a causeway shifted. A lower-canal defender helped a Pale Bough soldier wash ghost-water from her eyes. Orrowen dead guided stretchers across bridges that appeared only when someone said where they were going and who they carried. Tavi found herself repairing a hymn wagon brake with one hand while threatening to dismantle its root harness with the other. Kesh stole three unauthorized triage tags and returned five better ones. Brakka remained kneeling, holding the field's shape with her body because bridges were always more expensive than travelers wanted to admit.

Mara stood at the center and did not feel victorious.

She felt the next failure gathering at the edges. The Choir still breathed. Serathiel still believed. Vaura still calculated. The dragon-moon still waited below, and Vorrakai had learned the sound of Mara's refusal.

But a child named Selli was being argued into a safer seat by two dead grandmothers and one living soldier who seemed alarmed to have developed feelings. A wounded man who would have been an enemy ten minutes ago was cursing at a healer from the wrong army and living through it. Names moved faster than orders.

For now, that was enough work for hope to disguise itself as logistics.

Mara looked down through the bridge light to the pale curve of the dragon-moon far below.

Around her, the first written terms traveled from hand to hand. They were ugly, crossed out, rephrased, challenged, stamped, nearly torn, then rewritten again on the backs of old writs and shield straps. No bard would ever sing about the fifth version of a casualty corridor clause. No child would play at being the person who made sure Orrowen stretchers could pass both armies without surrendering civic standing. Yet Mara found herself watching those small labors with fiercer hope than any shining charge had ever given her.

This, she thought, was what stillness hated most.

Not heroism. Not victory. Revision.

The stubborn, humiliating, living work of trying again while everyone could still object.

Kesh read one clause upside down and said it needed theft-proof margins. Tavi told him margins were not moral technology. Sava stamped both comments as pending. Somehow, absurdly, the battlefield stayed still.

"Soon," Vorrakai had said.

"Not alone," Mara answered, and though the first dragon did not reply, the bridge under her feet held.""",
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
        'current_form: "full-length draft zero with Book Two chapters 1-24 revised in pass 01"',
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
    print(f"Book Two chapters 22-24 revised. Word count: {total}")


if __name__ == "__main__":
    main()
