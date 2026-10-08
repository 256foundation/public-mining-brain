# ASIC Thermals and Heat Reuse

> Sources: 256 Foundation Telegram group (t.me/the256foundation), 2024-02-24 → 2026-10-07
> Raw: [256F Telegram signal digest](../../raw/history/2026-10-08-256f-telegram-signal.md)
> Updated: 2026-10-08
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
- [Open Mining Economics](../economics/open-mining-economics.md)
- [Mujina](../firmware/mujina.md)
