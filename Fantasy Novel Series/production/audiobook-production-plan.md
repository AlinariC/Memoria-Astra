# Cinderwake Audiobook Production Plan

Status: started 2026-05-20

## North Star

This should play like an ensemble epic, not a flat reading. The listener should feel soot, rain, law, hunger, witness, and old dragon memory pressing through ordinary bodies. The performance rule is:

> Intimacy first. Scale second. No character becomes a symbol before the listener believes them as a person.

The trilogy's sound is built around the conflict between command and witness. Command sounds smooth, clean, beautiful, procedural, inevitable. Witness sounds specific, embodied, inconvenient, and alive.

## ElevenLabs Production Notes

- Use **Text to Dialogue** with `eleven_v3` for ensemble scenes with multiple distinct voices. Keep each request at or below about 2,000 total characters for reliable generation. The current API exposes dialogue-level stability rather than full per-speaker style settings, so the renderer derives chunk stability from the active character arcs.
- Use single-voice **Text to Speech** for long narration stretches when dialogue separation would add cost without better storytelling. Use `eleven_v3` for emotional set pieces and `eleven_multilingual_v2` for steadier long-form rendering if needed.
- Do not prepend actor directions to generated manuscript text by default. Some bracketed tags can affect delivery, but they can also be spoken by the model; use arc metadata and manuscript context first, with explicit tags only for manually reviewed pickup lines.
- Split, render, and stitch in small chunks. Keep manifests with model, voice, role, chunk, and source so regenerations stay controlled.

Official docs checked:

- https://elevenlabs.io/docs/overview/capabilities/text-to-speech
- https://elevenlabs.io/docs/api-reference/text-to-speech/convert
- https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue
- https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert

## Files Added For This Pass

- `production/audiobook-cast.json`: machine-readable role-to-voice casting map.
- `production/audiobook-samples/book-01-chapter-01-opening.dialogue.json`: first curated proof scene.
- `scripts/render_elevenlabs_dialogue.py`: renderer for curated Text to Dialogue scripts.
- `output/audiobooks/cinderwake/`: generated sample output location.

## Core Cast

| Role | Voice | Performance Center |
| --- | --- | --- |
| Narrator | John Doe Intimate | Intimate epic narration; grave wonder, ash-level closeness, cinematic restraint. |
| Mara Venn | Sarah | Guarded, practical, fierce under exhaustion. Least "chosen" when most powerful. |
| Joryn Venn | Chris | Miner-brother warmth under irritation; protective, dry, frightened of losing old Mara. |
| Sir Caldus Renn | Brian | Low soldier's voice; clipped duty, shame, discipline, tenderness in small exact breaks. |
| Ilyr Noct-Vey | Daniel | Precise, controlled, archival, blade-like; shame under elegant restraint. |
| Saelith Dawnmere | Lily | Trained beauty and law slowly gaining cracks, breath, and consent. |
| Tavi Quen | Laura | Fast workshop intelligence; jokes as pressure release over guilt. |
| Kesh of the Kavik Road | Callum | Quick road-trader wit, invoices as armor, silences that hurt. |
| Brakka of the Third Arch | Matilda | Low oath-sister gravity; every sentence load-bearing. |
| Arveth the Named | River | Dry undead scholar; papery wit, legal precision, personhood preserved. |
| Vorrakai / cinder voice | George | Vast dragon grief as private comfort; terrifying because it sounds merciful. |
| Mordane / crown authority | Adam | Polished administrative cruelty; arithmetic, not snarling. |
| Foreman Sedge | Adam | Petty company authority; ledger logic in a small ugly room. |
| Shared male support | Roger | Miners, soldiers, road witnesses, one-scene men. |
| Shared female support | Bella | Witnesses, healers, mothers, clerks, one-scene women. |

## Character Acting Bible

### Mara Venn

Mara is the emotional lens across all three books. She begins with a small, wary Ashgate register: direct, unsentimental, physically tired. Her leadership should arrive reluctantly, as if every command risks becoming the thing she hates. In Book 3, she is powerful but must still sound like a person choosing, not destiny speaking through a throat.

Performance traps: do not make her grandiose by default, saintly, or YA-quippy. Her humor is survival pressure.

### Sir Caldus Renn

Caldus sounds trained: clipped consonants, tactical clarity, a man used to issuing orders. But every clean sentence has guilt behind it. His best scenes are not heroic thunder; they are moments when command catches itself and becomes accountability.

Performance traps: no noble swagger. Let him be tired, useful, ashamed, and precise.

### Kesh

Kesh should change the air immediately. He is fast, funny, transactional, and afraid of stillness because stillness lets guilt catch him. His jokes must remain charming, but when the jokes stop, the listener should feel the floor drop.

Performance traps: no cartoon goblin voice. Road-cadence, not creature gag.

### Brakka

Brakka is vow-law made bodily. She is sparse, literal, and deeply moral. Slow does not mean dull; it means weight. Her humor is dry because she has no patience for decorative language.

Performance traps: do not make her monstrous or stupid. She is one of the trilogy's clearest legal minds.

### Tavi Quen

Tavi's pace is a defense. Technical explanations should sound like thought happening faster than grief can catch it. When she breaks, it should feel like a machine overheating, not a monologue asking for sympathy.

Performance traps: avoid squeaky engineer energy. She is sharp, guilty, and brilliant.

### Saelith Dawnmere

Saelith begins as controlled beauty: hymn-trained, formal, compassionate, and dangerously obedient. Over the trilogy, her voice should become less perfect and more human. The cracks are the victory.

Performance traps: do not villain-code her early reverence. She means mercy, which is why the arc matters.

### Ilyr Noct-Vey

Ilyr is a historian with a blade's posture. His control should sound expensive. Pauses matter: he withholds because withholding once felt like survival, then became poison.

Performance traps: avoid generic shadow-villain texture. His darkness is record-keeping, exile, and shame.

### Arveth, Sava, And The Named Dead

The dead must remain people. Their voices can be reduced by death, fatigue, or damaged breath, but never collapsed into one spooky effect. Arveth is legal wit and devastating humanity. Sava is clerk-energy sharpened into moral force.

Performance traps: no one-size undead voice.

### Vorrakai And The Dragons

Vorrakai should sound like relief offered without consent. The voice is ancient, tired, intimate, almost kind. Other dragons can be spacious, but keep intelligibility and personhood. Young Vorrakai and Othrava in Book 3 must sound like people before catastrophe, not symbols.

Performance traps: no monster growl. The horror is persuasive tenderness.

## Book-Level Performance Arcs

### Book 1: The Ash Beneath The Crown

The opening must be claustrophobic and bodily: vent heat, counting breaths, skin scraping stone, bells answering from below. Keep the first chapters close to workers and ledgers. The mythic voice enters as pressure under ordinary life, not as spectacle.

Middle chapters shift into road energy as Kesh, Brakka, Tavi, Saelith, Ilyr, and Arveth join. Let each new register expand the world without turning the book into a parade of accents. Harrowmere should sound warm, clean, and morally filthy.

The climax is civic, not merely explosive. "Where are the names?" should grow from question to public rhythm. Arveth's sacrifice should be dry, restrained, and devastating. Victory sounds like soup, bad ledgers, tired bodies, and people choosing.

### Book 2: The Moon Below The World

Book 2 needs clear institutional sound families:

- Ashgate/Crownreach: plain, work-worn, direct.
- Lumenorath: formal, musical, beautiful enough to coerce.
- Khar Veyl: low, precise, legalistic, controlled.
- Kavik roads: quick, transactional, amused under pressure.
- Orrowen: civic, procedural, ancient, dry, insistently alive.

Saelith and Serathiel carry the key vocal contrast: obedience learning to crack versus mercy turning into control. Kesh's worst bargain, Ilyr/Maelin's retained witness wound, Tavi's Glass Engine refusal, and Brakka's bridge law all need room to breathe.

Production risk found and fixed before narration: Book 2 had two residual Serathiel male-wording lines in the manuscript and split Chapter 24. Both were corrected to match the she/her continuity standard.

### Book 3: The Dragon That Dreamed Death

Book 3 is ensemble-heavy and mythic, but the emotional center remains practical people refusing symbolic capture. The narrator must move between apocalypse and lentils without treating aftermath as lesser drama.

The Dead Capital sequence is a set of temptation chambers. Each role should sound seduced by the version of command that flatters their wound: Caldus by clean orders, Saelith by beautiful sacrifice, Kesh by absolved debt, Tavi by perfect engineering, Brakka by unquestioned load-bearing, Mara by rest and usefulness.

The ending is anti-triumphal by design: cold rooms, bad meetings, road law, public dark, repaired songs, and Kell Ashgate without command under it. The final note should feel free of grand finality.

## Shared Voice Families

Use shared performers deliberately:

- Crown/company officials: Sedge, captains, physicians, heralds, Regent Rook, tax officers. Clean, procedural, status-forward.
- Ashgate/civic witnesses: Dilla, Harl, Ness, Bessa, Rella, Othen, Fenna, Lenn Voss. Working-class texture, each with local shape.
- Light-elf authority: Veyanna, Liora, Aneth, Auralian, Elianth, Pale Bough officers. Musical formality with role-specific warmth or brittleness.
- Dark-elf/Khar Veyl officials: Vaura, blade-scholars, sealers, archivists, Velra. Low precision, civic knife-work.
- Kavik/road-clan voices: Rikka, Veyr Tal, Auntie Varr, Varrik, Serren, Pol Trevish. Fast bargaining and road memory.
- Troll elders: Durn, Granth, Surn, Ossh, Elder Morn. Weight, age, vow-law, different degrees of patience.
- Children/teens: Selli, Nim, Tovin, road children. Sharp and specific; not cute by default.

## Pronunciation Sheet

| Term | Working Pronunciation |
| --- | --- |
| Mara | MAH-ruh |
| Joryn | JOR-in |
| Caldus | KAL-dus |
| Kesh | KESH |
| Brakka | BRAH-kuh |
| Tavi Quen | TAH-vee KWEN |
| Saelith | SAY-lith |
| Serathiel | seh-RATH-ee-el |
| Ilyr Noct-Vey | IL-eer NOKT-vay |
| Arveth | AR-veth |
| Sava Rennet | SAH-vuh REN-it |
| Mordane | mor-DAYN |
| Vorrakai | VOR-uh-kye |
| Othrava | oh-THRAH-vuh |
| Veyrasha | vay-RAH-shuh |
| Eshkarun | ESH-kuh-roon |
| Rhyssara | rih-SAR-uh |
| Vael Taryn | VAYL TAIR-in |
| Kell Ashgate | KELL ASH-gate |
| Harrowmere | HAR-oh-meer |
| Gloamfen | GLOHM-fen |
| Lumenorath | loo-MEN-oh-rath |
| Khar Veyl | KAR VAYL |
| Orrowen | OR-oh-wen |
| Pale Bough | Pale BOW, where bough rhymes with cow |

High-risk clusters:

- Saelith / Serathiel
- Sava / Saelith / Serathiel
- Vaura / Vorrakai / Veyra / Veyrasha / Khar Veyl
- Oren / Edrin / Orrowen
- Varr / Varrik
- Vessa / Vael

Packaging note: use **The Dragon That Dreamed Death** everywhere. One cover filename says "who"; the manuscript and metadata use "that."

## Production Workflow

1. Lock source text for each chapter before rendering.
2. Run consistency scans for pronouns, title spelling, and high-risk names.
3. Build a curated `.dialogue.json` script for the chapter or scene.
4. Dry-run the renderer and verify chunk count, character count, and roles.
5. Render a short proof, listen, adjust delivery tags or casting, then render the full scene.
6. Save manifests beside every generated MP3.
7. Stitch full chapters, then full-book M4B masters with chapter metadata.
8. Keep a regeneration log so replacement chunks do not drift across the performance.

## Immediate Next Samples

1. Book 1, Chapter 1 opening: narrator / Mara / Sedge claustrophobic proof.
2. Book 1, Chapter 5 bridge scene: Mara / Caldus / captain / Pell to test action and guilt.
3. Book 1, Chapter 7 Kesh entrance: road humor and bargain texture.
4. Book 2, Chapter 14 Banquet of True Shadows: institutional voices, Kesh confession, Ilyr/Maelin.
5. Book 3, Chapter 30 Arveth Chooses Rest: dry wit into grief.
