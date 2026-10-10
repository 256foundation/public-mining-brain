# ASIC Thermals and Heat Reuse

> Sources: 256 Foundation Telegram group (t.me/the256foundation), 2024-02-24 → 2026-10-07; bitaxeorg/ESP-Miner and bitaxeorg hardware GitHub issues, 2023-01 → 2026-10; OSMU wiki (captured 2026-10-07)
> Raw: [256F Telegram signal digest](../../raw/history/2026-10-08-256f-telegram-signal.md); [ESP-Miner #1927 EMC2101 fan scaling](../../raw/firmware/esp-miner/2026-08-29-github-esp-miner-issue-1927-emc2101-fan-duty-cycle-is-scaled.md); [ESP-Miner #2000 overheat on sensor faults](../../raw/firmware/esp-miner/2026-09-25-github-esp-miner-issue-2000-overheat-protection-acts-on-sens.md); [OSMU wiki: tips & FAQ](../../raw/hardware/bitaxe-osmu/osmu-wiki-tips-faq.md)
> Updated: 2026-10-09
> Status: Draft

## Overview

What mining silicon and hashboards can actually tolerate thermally, from practitioners who run miners as heaters and who reverse-engineer hashboards for a living. Headlines: S9-era chips are near-indestructible for heat duty; 3nm-class silicon is far less tolerant; the practical limit on hot operation is usually the secondary components (comms/analog), not the ASICs; and temperature *reporting* is unreliable enough across firmwares that field anecdotes matter as much as datasheets.

## Chip temperature limits

- Smaller-process ASICs handle hot running worse: 7nm-era chips tolerate high temps, but at 3nm the tiny channels suffer cross-channel bleed that disrupts operation — the core obstacle for high-temp heat-reuse rigs [#540 · 2024-03-21 · econoalchemist]
- Bitmain's support docs list the S9 chip temp max as 135°C [#553 · 2024-03-23 · Skot Bitaxe]; hashboard laminates get reflowed at > 220°C during assembly so the substrate is not the limiting factor, though component operating specs may drift when hot [#566 · 2024-03-23 · Skot Bitaxe]
- FutureBit designed 14nm ASICs rated to run at 110c, with prototype hashboards demonstrated boiling distilled water [#550 · 2024-03-22 · Jstefanop]
- Braiins built several hundred custom Marathon rigs from Bitmain S17 chips (BM1397) on aluminum PCBs; the custom firmware's "dangerous temp" default was 110C and efficiency around 45j per terahash; the rigs were later donated to Unbound — an aluminum PCB + 7nm chip validated as a high-temp platform [#549 · 2024-03-22 · Zack Bomsta]
- Newer Bitmain chips dropped on-die temperature sensors, so chip temp is inferred rather than measured directly like on older boards [#557 · 2024-03-23 · Skot Bitaxe]

> **Status: Disputed** — S9 practical max
> Bitmain's docs say 135°C [#553 · 2024-03-23 · Skot Bitaxe]; field experience says stock firmware reads chip temp roughly 15 degrees higher than real, so the practical max is likely only 120 [#556 · 2024-03-23 · Brett Rowan]. Best assessment: treat 135°C as the silicon's rated ceiling and ~120 as the trustworthy operating ceiling for heat-reuse duty.

## The real blocker: secondary components

- The "PCB temp" in miner readouts is an air-temperature sensor mounted on the PCB; that reading is an environment spec for secondary components, not for the laminate itself [#558 · 2024-03-23 · Brett Rowan] [#561 · 2024-03-23 · Skot Bitaxe]
- The real blocker for running silicon past the 100C mark is comms/analog parts, not the ASICs: FutureBit's high-temp test boards lasted about a week before comms/analog components began failing [#570 · 2024-03-23 · Jstefanop]
- A hashboard needs little besides ASICs and passives, which is what makes a stripped-down high-temp board plausible [#576 · 2024-03-23 · Skot Bitaxe]
- Open question raised in-community: could wide-bandgap silicon carbide / gallium nitride push chip temps past that 100C mark? [#4423 · 2026-02-13 · context thread]

## Sensor reality (EMC2101 and friends)

- EMC2101 reporting 127.875 degrees is the sensor's maximum value — a symptom of a hardware problem (short/open in the connection to the ASIC diode), not a real temperature; datasheet table 4-2 cited [#4604 · 2026-03-12 · Ryan] [#4605 · 2026-03-12 · Ryan]
- esp-miner goes through undocumented-diode setup (ideality/gain parameters) for the EMC2101 on Bitmain ASICs; Mujina users were told to check the same values [#4148 · 2026-01-06 · Skot Bitaxe] [#4151 · 2026-01-06 · Skot Bitaxe]

## Small-board (Bitaxe) thermal lessons

Bitaxes are single-digit-to-tens-of-watts boards, which makes them a clean lab for chip-level thermal behavior. Builder details (sensor wiring, fan hardware, regulator faults) live in [Bitaxe Board Design, Power & Errata](bitaxe-board-design-and-errata.md); the transferable lessons:

- **Diode readings need tuning, not averaging.** The EMC2101 reads an undocumented on-die diode, and gain/ideality must be tuned per ASIC: Gamma 600 builds "overheated" within minutes until the BM1370 readings were fixed "with better temp diode tuning on the EMC2101" ([bitaxeGamma #12](../../raw/hardware/bitaxe-osmu/2024-10-28-github-bitaxegamma-issue-12-some-bitaxegamma-builds-are-over.md)); the corrected firmware read about 10 degrees Celsius higher than before ([ESP-Miner #512](../../raw/firmware/esp-miner/2024-11-23-github-esp-miner-issue-512-chip-temperature-2-3-0-2-4-0.md)), and the GT's EMC2103 needed a -10C offset ([ESP-Miner #881](../../raw/firmware/esp-miner/2025-05-02-github-esp-miner-issue-881-need-to-tune-temperature-sensor-f.md)). Series resistance in the diode path errs by +0.7°C per ohm per the EMC2101 datasheet ([bitaxeGamma #13](../../raw/hardware/bitaxe-osmu/2024-11-03-github-bitaxegamma-issue-13-determine-proper-asic-temp-diode.md)). Chips without a die diode (BM1366) fall back to a board sensor near the ASIC, which reads cooler the farther away it sits ([ESP-Miner #1228](../../raw/firmware/esp-miner/2025-09-10-github-esp-miner-issue-1228-add-support-for-bitaxeultra-207.md)).
- **Leakage is real and measurable.** On a Supra 401 at a fixed operating point, power tracked temperature at ~0.16 W/°C; running 6 °C cooler was worth ~1 W on a 14 W board, about 3% efficiency ([ESP-Miner #1927](../../raw/firmware/esp-miner/2026-08-29-github-esp-miner-issue-1927-emc2101-fan-duty-cycle-is-scaled.md)).
- **But colder is not always faster.** One overclocked Gamma 602 lost about 100 hashrate per 5° drop; KillerInk found most of his ASICs dislike running below 60°C and drop above 65°C, while VR temperature didn't seem to matter ([ESP-Miner #1347](../../raw/firmware/esp-miner/2025-11-12-github-esp-miner-issue-1347-strange-behavior-when-surroundin.md)).
- **Fan power has an optimum.** Because fan power climbs steeply with RPM while temperature gains shrink, total system power on that Supra was flat between 76% and 85% duty and rose beyond — a controller that just chases a temperature target overshoots it. The same issue found the EMC2101 driver over-driving fans (scaling against 63 instead of 46), so naively fixing the scaling cut airflow by 27% and pushed a board from 68 °C to the 75 °C throttle point ([ESP-Miner #1927](../../raw/firmware/esp-miner/2026-08-29-github-esp-miner-issue-1927-emc2101-fan-duty-cycle-is-scaled.md)).
- **Idle is not zero.** With ASIC reset held low a Gamma still draws about 2 W — enough to make a fanless 40mm heatsink uncomfortably hot — and the fan's power-up default depends on which EMC2101 variant the assembler fitted ([bitaxe-raw #10](../../raw/hardware/bitaxe-osmu/2026-03-19-github-bitaxe-raw-issue-10-fan-default-behavior-seems-interm.md)).
- **Overheat protection pitfalls.**
  - Thresholds are guesses: ESP-Miner trips at 75 °C (ASIC) and 105 °C (TPS546 regulator) ([ESP-Miner #1099](../../raw/firmware/esp-miner/2025-06-30-github-esp-miner-issue-1099-enhancement-request-overheat-con.md)), while the OSMU FAQ's safe ranges are ASIC below 70°C and voltage regulator below 90°C ([OSMU FAQ](../../raw/hardware/bitaxe-osmu/osmu-wiki-tips-faq.md)); proposals to raise the ASIC limit lacked datasheet evidence ([ESP-Miner #316](../../raw/firmware/esp-miner/2024-09-02-github-esp-miner-issue-316-raise-overheat-limit.md)).
  - Sensor faults masquerade as heat: an open-circuit EMC2101 diode decodes to exactly 127.0 °C (compare the 127.875 maximum above), and a cached garbage regulator word caused repeated frequency downgrades that persist to NVS ([ESP-Miner #2000](../../raw/firmware/esp-miner/2026-09-25-github-esp-miner-issue-2000-overheat-protection-acts-on-sens.md)). Boot races after rapid restarts also tripped false overheat mode; invalid temps should default the fan to full ([ESP-Miner #1186](../../raw/firmware/esp-miner/2025-08-11-github-esp-miner-issue-1186-random-device-overheats-when-rap.md)).
  - Protection is silent: it lowers frequency by 100 per trip without a visible dashboard warning (open) ([ESP-Miner #1631](../../raw/firmware/esp-miner/2026-03-24-github-esp-miner-issue-1631-device-frequency-is-set-low-see.md)) ([ESP-Miner #1638](../../raw/firmware/esp-miner/2026-03-30-github-esp-miner-issue-1638-overheat-self-protect-mode-overh.md)).
  - A dead fan is the usual root cause, and an EMC2103 with no tach still reads 960 RPM and passes self-test ([ESP-Miner #1970](../../raw/firmware/esp-miner/2026-09-12-github-esp-miner-issue-1970-fan-rpm-display-will-not-move-fr.md)).
- **Mounting pressure is a thermal parameter.** Replacing the Gamma's spring clamps with M3 bolts let a user run 595MHz @ 1150mV, beyond the stock 525MHz cooler limit ([ESP-Miner #369](../../raw/firmware/esp-miner/2024-09-30-github-esp-miner-issue-369-lower-the-default-hash-frequency.md)); extra mounting holes and thicker PCBs fight board warp on multi-ASIC Bitaxes ([bitaxeGT #16](../../raw/hardware/bitaxe-osmu/2025-09-23-github-bitaxegt-issue-16-build-with-thicker-pcbs.md)).

## Cooling approaches

### Liquid cooling and cold plates

- Server-hardware research uses milled micro-jet cold plates directly over the hottest die area [#581 · 2024-03-23 · Skot Bitaxe]
- FutureBit's closed-loop micro-jet waterblocks dissipate 600 watts at 2k rpms; blocks cost $200-300 each and getting that price down is the open problem [#582 · 2024-03-23 · Jstefanop] [#585 · 2024-03-23 · Jstefanop]
- Antminer hydro hashboards only touch water blocks to the tops of the chips — nothing on the backside of the fiberglass PCB; consistent with ASIC datasheets: the large majority of heat conducts out the die surface on top [#4480 · 2026-02-21 · Skot Bitaxe] [#4481 · 2026-02-21 · Skot Bitaxe]; confirmed on S21 XPs [#4483 · 2026-02-21 · Boots Stribling]
- Skot added exposed, soldermask-free pads on board backs "just in case"; an actual rear-heatsink experiment on a Bitaxe made no difference [#4488 · 2026-02-21 · Skot Bitaxe] [#4489 · 2026-02-21 · Skot Bitaxe]
- Hydro-cooled Bitaxes run fine on plain distilled water — 'anything up to and probably including salt water' [#1435 · 2024-11-22 · Elijah Sanders]

### Immersion

- BitCool dielectric coolants are NSF-designated 'food grade' [#1813 · 2025-04-13 · Kendal Pappas]
- Karl's canola-oil immersion: no component reactions observed beyond wire-insulation stiffening; vitamin E oil added to slow oxidation; the only proof is running it until something fails [#2913 · 2025-08-16 · Karl] [#2915 · 2025-08-16 · Karl] [#2916 · 2025-08-16 · Karl]
- Gianluca (patented oil-immersion system, developed 2016-2018): 10kw dissipated in a standard 19-inch rack using only 37 L of oil, stable at 40C with 22C water in the exchanger; 3 years of 365-day immersion left hardware like new; use nylon-coated cables [#2613 · 2025-07-02 · Gianluca L] [#2629 · 2025-07-02 · Gianluca L] [#2919 · 2025-08-16 · Gianluca L] [#2920 · 2025-08-16 · Gianluca L]
- MintGreen's digital boiler / CADDY2 brochures circulated; the ~85C outlet temp attributed to their hashboard choice was questioned [#1833 · 2025-04-13 · Karl] [#1831 · 2025-04-13 · Karl]

### Thermal interface materials

- Juergen's TIM survey: squishy gap-filler pads (7.5wmk class, reusable, doesn't dry out in 6 months like Fujipoly at ~3wmk), graphite pads above 40wmk but incompressible, phase-change pads that go gooey at modest temps; 7.5wmk costs maybe only twice the cost of paste [#2903 · 2025-08-16 · Mæstro Juergen] [#2905 · 2025-08-16 · Mæstro Juergen] [#2906 · 2025-08-16 · Mæstro Juergen]
- Gianluca's endgame: gallium-indium alloy thermal pads, 75W/mK, chemically inert — better than the liquid alloy he tried first (mercury-like, very slow to apply) [#2907 · 2025-08-16 · Gianluca L] [#2908 · 2025-08-16 · Gianluca L]

### Heat-reuse thresholds

- Most absorption chillers need input heat somewhat above 80C; ~100C input enables efficient absorption chilling, opening a miner-driven heater/chiller/load-balancer appliance for buildings [#546 · 2024-03-22 · Tyler Stevens] [#590 · 2024-03-24 · Tyler Stevens]

## Related hardware facts

- Antminer S19 XP hashboards use BM1366 ASICs [#371 · 2024-03-03 · Nikos]
- BM1366 chips have soldered-on heatsinks, which makes them very difficult to reuse [#4667 · 2026-04-14 · Skot Bitaxe]
- Fan-connector taxonomy: S19 XP and older use four 1x4 connectors; S19k Pro uses two 1x4 + two 2x2; S21 and newer use four 2x2 [#4448 · 2026-02-18 · Skot Bitaxe]; bitcrane PCB footprints accept either, but unsoldering is a pain [#4447 · 2026-02-18 · Skot Bitaxe]

## See Also

- [Ember One & the BZM2 Hardware Stack](ember-one-bzm2.md)
- Same topic: [Bitaxe Board Design, Power & Errata](bitaxe-board-design-and-errata.md)
- Getting started: [Bitaxe Troubleshooting](../getting-started/bitaxe-troubleshooting.md)
- [Open Mining Economics](../economics/open-mining-economics.md)
- [Mujina](../firmware/mujina.md)
- Same topic: [Air-Cooled Hashrate Heating](air-cooled-hashrate-heating.md)
- Same topic: [Hydronic Heat Reuse](hydronic-heat-reuse.md)
- Same topic: [Immersion Heat Reuse](immersion-heat-reuse.md)
- Same topic: [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md)
