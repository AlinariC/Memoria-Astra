# Apple Books Delivery Log - Books 09-16

Delivered: 2026-05-17 23:39 MST

Destination: Apple Books / iTunes Connect via Transporter app, provider `AlinariCampbell`.

| Book | Title | Vendor ID | Transporter log | Upload ID |
| --- | --- | --- | --- | --- |
| 09 | The Silent Accord | `memoria_astra_09_the_silent_accord` | `AlinariCampbell_memoria_astra_09_the_silent_accord__2026-05-17-233910.txt` | `57cbef6d-9dc1-4a77-80c1-89a1ce2cfb07` |
| 10 | Starforged Thrones | `memoria_astra_10_starforged_thrones` | `AlinariCampbell_memoria_astra_10_starforged_thrones__2026-05-17-233916.txt` | `fc6d15c0-9387-406e-8784-005051ff5d9d` |
| 11 | Lament of the Shattered Gate | `memoria_astra_11_lament_of_the_shattered_gate` | `AlinariCampbell_memoria_astra_11_lament_of_the_shattered_gate__2026-05-17-233919.txt` | `11d7c023-c676-43d1-b3c6-674156f3e355` |
| 12 | Resonance of Ash and Dream | `memoria_astra_12_resonance_of_ash_and_dream` | `AlinariCampbell_memoria_astra_12_resonance_of_ash_and_dream__2026-05-17-233926.txt` | `7f503697-2e63-44bd-a556-c9d58bdca528` |
| 13 | The Gathering Spiral | `memoria_astra_13_the_gathering_spiral` | `AlinariCampbell_memoria_astra_13_the_gathering_spiral__2026-05-17-233930.txt` | `bd8f23b7-0035-4606-9b79-7dfbdf945397` |
| 14 | The Weeping Crown | `memoria_astra_14_the_weeping_crown` | `AlinariCampbell_memoria_astra_14_the_weeping_crown__2026-05-17-233937.txt` | `802327e8-7a42-4278-9525-59cbf373fd25` |
| 15 | The Final Loom | `memoria_astra_15_the_final_loom` | `AlinariCampbell_memoria_astra_15_the_final_loom__2026-05-17-233957.txt` | `33a274d0-a5e7-4ebf-9015-bd308f001c42` |
| 16 | The Second Spiral | `memoria_astra_16_the_second_spiral` | `AlinariCampbell_memoria_astra_16_the_second_spiral__2026-05-17-233940.txt` | `d65b8c0d-aea8-4f17-bb5e-e071739adc46` |

Verification:

- Transporter UI showed delivered states for Books 13-16 while the batch completed.
- New Transporter log files were created for each of Books 09-16.
- Each log contained a successful upload result and an Apple upload ID.
- `python3 scripts/build_apple_itmsp.py --book <slug> --strict` still passes for Books 09-16.

Notes:

- Books 09-16 are delivered to Apple for processing/review. Store availability may lag delivery.
- Books 09-16 use ISBN-less underscore vendor IDs; keep these IDs stable for future Apple Books updates.
