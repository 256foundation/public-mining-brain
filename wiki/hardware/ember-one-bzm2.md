# Ember One & the BZM2 Hardware Stack

> Sources: 256 Foundation Telegram group (t.me/the256foundation), 2024-02-24 → 2026-10-07
> Raw: [256F Telegram signal digest](../../raw/history/2026-10-08-256f-telegram-signal.md)
> Updated: 2026-10-08
> Status: Draft

## Overview

The 256 Foundation's open hardware program: **Ember One** hashboards (a model series keyed to chip vendors), the **Intel BZM2** chips that made it real (donated by Proto), **BitaxeBIRDS** (the Bitaxe-family BZM2 board), **aditBoard** (a bridge to native Antminer hashboards), and **Libre Board** (the open control board that drives them). The through-line: chips on reels with proper documentation, so anyone can build a miner without dismantling Bitmain hardware.

## The emberOne model series

- emberOne is named by chip vendor: emberOne/00 = Bitmain BM1362, emberOne/01 = Intel BZM2 (Blockscale), emberOne/02 maybe Auradine — each a reference design for vendors willing to work cooperatively with the community [#2266 · 2025-05-22 · Ryan] [#2270 · 2025-05-23 · Skot Bitaxe]
- Positioning: a 100 W-class board for use-cases where a full-size Antminer hashboard (roughly a kilowatt) doesn't fit; usable as-is or as a dev board for other hashboards [#2172 · 2025-05-15 · Skot Bitaxe]
- Future emberOnes deliberately use chips from new vendors selling directly to hardware producers — 'blazing the trail for a new category of mining systems'; the stated goal is never needing a Bitmain-chip model again [#2177 · 2025-05-16 · Ryan] [#2267 · 2025-05-22 · Ryan]
- Product vision data point: a plug-in 1,500W 256F BZM2 miner-heater would deliver ~40 TH with wifi controls [#1871 · 2025-04-23 · Reckless Apotheosis] [#1874 · 2025-04-23 · Reckless Apotheosis]

## The BZM2 windfall

- Provenance: Proto donated 256k Intel ASICs (the canceled-2023 BZM2) to the Foundation at NEMS fall 2024; Proto had bought the chips while winding down, planning mass MDK production, but their own internal ASIC took off [#3007 · 2025-09-02 · Mæstro Juergen] [#3009 · 2025-09-02 · Reckless Apotheosis] [#3012 · 2025-09-02 · Reckless Apotheosis]
- For open-source devs the chips are free, brand-new on reel, no desoldering; technical docs to be released with reference designs; Tom's Hardware covered the story [#3021 · 2025-09-03 · econoalchemist] [#3035 · 2025-09-03 · econoalchemist] [#3038 · 2025-09-05 · econoalchemist]
- BZM2 throughput: appx 400 GH/s per chip [#2183 · 2025-05-16 · Mike Hamilton]
- Chip marking decoded from the reel: HASH IC, 12W, 5nm TSMC Process, LGA BZM2-HASH-IC-FF0.5, 99ALPD — DVT1 silicon [#3681 · 2025-11-24 · Reckless Apotheosis] [#3673 · 2025-11-24 · Skot Bitaxe]
- NOOP (opcode 4'hF) is the ASIC ping; the BZM2 answers 2ZB in the wild, while the datasheet says 24'h425A4D ("BZM") and the architectural spec says "BZ2" — the Intel docs disagree with each other [#3687 · 2025-11-24 · Skot Bitaxe] [#3697 · 2025-11-24 · Skot Bitaxe] [#3700 · 2025-11-24 · Reckless Apotheosis]
- Backdoor reality check: you couldn't really hide a backdoor in the ASIC itself — the vectors are hashboard control chips, the control-board FPGA, or its software [#3033 · 2025-09-03 · Reckless Apotheosis] [#3034 · 2025-09-03 · Reckless Apotheosis] [#3032 · 2025-09-03 · Jstefanop]

## BitaxeBIRDS

- bitaxeBIRDS (a 4× BZM2 board) repo published 2025-11-13: github.com/bitaxeorg/bitaxebirds [#3311 · 2025-11-13 · Skot Bitaxe]
- First bring-up: communication established with all 4 chips in the chain after a set of fixes tracked in the repo issues [#3647 · 2025-11-23 · Skot Bitaxe]
- Runs the bitaxe-raw-pico firmware on an RP2040 Pico, exposing the ASIC chain serial directly over USB — no ESP32 because that MCU can't do 9-bit serial; RP2350 (Pico 2) port in progress by johnny9; bring-up test scripts at github.com/skot/bzm-raw-py [#3660 · 2025-11-23 · Skot Bitaxe] [#3661 · 2025-11-23 · Skot Bitaxe] [#3662 · 2025-11-23 · Skot Bitaxe] [#3663 · 2025-11-23 · Skot Bitaxe] [#3664 · 2025-11-23 · Skot Bitaxe] [#3665 · 2025-11-23 · Skot Bitaxe]
- ASIC_ID changed to 0x42 and NOOP answered from all 4 BZM2s; TPS546D24 voltage regulator and new manual fan control verified [#3747 · 2025-11-30 · Skot Bitaxe]
- High-speed serial experiments: 5 Mbaud 9-bit serial working on the RP2040 (bitaxe-raw pico branch); Mike Hamilton's custom S9 control-board FPGA image does 10 Mbaud 9-bit and talks to BZM2s [#3314 · 2025-11-13 · Skot Bitaxe] [#3318 · 2025-11-13 · Mike Hamilton]
- Peer review of the BIRDS schematic caught the TX_OUT→TX_IN level-shifter pull-down referenced to GND_H instead of GND_L — acknowledged as a post-fab errata (issue #2): 'wish I had noticed that before getting boards made' [#3736 · 2025-11-29 · Loren Lang] [#3739 · 2025-11-29 · Skot Bitaxe]
- A second build holding TXO low traced to an ASIC soldering issue [#3750 · 2025-11-30 · Skot Bitaxe]
- Form factors compared: emberOne 130×130 mm vs BitaxeBIRDS 68×123 mm [#3745 · 2025-11-30 · Loren Lang]
- BoM reality: ~$30/board before it 'does quite a few boards' (no fan, heatsink or Pico included); buy Coilcraft inductors directly from coilcraft.com rather than marketplace listings [#3785 · 2025-12-02 · Reckless Apotheosis] [#3791 · 2025-12-02 · Skot Bitaxe]
- Up to 25 BitaxeBIRDS targeted assembled in time for NEMS 2026 [#4029 · 2026-01-03 · Reckless Apotheosis]

## BZM2 power-domain math

- 16 BZM2 arranged in 4 domains of 4 chips: 2.8V for the whole stack at nominally 70A, on a 4-phase TPS546 for headroom; alternative: 8 domains of 2 → about 5.6V and only 35A [#5106 · 2026-07-22 · Skot Bitaxe] [#5119 · 2026-07-22 · Skot Bitaxe] [#5121 · 2026-07-22 · Aadhi M]
- The TPS546's limiting factor is its 5.5V max Vout (TI app note sdaa417 linked as a workaround path) [#5111 · 2026-07-22 · Skot Bitaxe]
- Aadhi shrank his domains to a 9-chip version on the same buck and switched to LTC regulators for high-VIN use [#5109 · 2026-07-22 · Aadhi M] [#5117 · 2026-07-22 · Aadhi M]
- Skot: the emberOne form factor needs to be re-thought, informed by next-gen Bitaxe work on the TPS546 (which is on the more recent emberOne revs) [#5087 · 2026-07-22 · Skot Bitaxe]

## BM1362 supply crunch (July 2025)

- BM1362 unavailable new in trays/reels (Power Mining could not find any); hashboards are easy to buy but require desolder/clean/test labor [#2656 · 2025-07-03 · Kristaps Stikuts]
- Only AA/AB/AC/AD variants exist (different footprints); Skot had been ordering new from NBTC until 'supply chain nonsense' cut supply — harvest from S19j Pro boards is the fallback [#2657 · 2025-07-03 · Skot Bitaxe] [#2658 · 2025-07-03 · Skot Bitaxe]
- emberOne requires same-bin chips (some bins don't work well together); all chips on a single jPro hashboard are likely one bin — a silver lining of harvesting [#2659 · 2025-07-03 · Skot Bitaxe]
- Harvest economics: disassembly + prep + cleaning + testing ≈ 5 minutes per chip; SMT feeders need pristine cleaning [#2660 · 2025-07-03 · Kristaps Stikuts] [#2666 · 2025-07-03 · Kristaps Stikuts]
- Repair-side data point: new chips by the bin haven't been purchasable since the S17 days [#2661 · 2025-07-03 · Mæstro Juergen]
- Juergen's harvest method: 300×300 heat plate, ultrasonic board cleaning, flux — chips come off needing little cleanup; works even on boards with soldered-on bottom heatsinks [#2662 · 2025-07-03 · Mæstro Juergen] [#2664 · 2025-07-03 · Mæstro Juergen] [#2667 · 2025-07-03 · Mæstro Juergen]
- Counter-data: Nick from Mega Miner can supply BM1362AC brand-new on the reel (quoted July 2025); bin matching unknown [#2665 · 2025-07-03 · econoalchemist]

## Ember One revisions & production

- 2025-06-12: v4 changed enough from the released v3 that the plan became prototype-first, then a 100+ unit order; pending list ~110 hashboards (largest: jstefanop 50, Scott Offord 25) [#2456 · 2025-06-12 · econoalchemist]
- 2025-07-02: production order slipped to mid-July with ~4-week turnaround → shipping mid-August; hashboards only — no PSU, heat-sink, fan, firmware or control board [#2643 · 2025-07-02 · econoalchemist]
- 2025-08-27: Skot resolved the ASIC-communication issue with v4 validation expected that week; production moved from Ben's original quote ($150/unit + $500 setup) to econoalchemist's new in-house pick-and-place line (100 units) [#2983 · 2025-08-27 · econoalchemist]
- v5 release candidate (published 2025-09-26): voltage-regulator circuit gutted and upgraded (Vishay-class reg); max-input requirement dropped from 24V to 17V — far more practical for high-current, low-voltage regulators; the OVP circuit still needs a prototype-sacrifice test [#3059 · 2025-09-23 · econoalchemist] [#3063 · 2025-09-23 · Jstefanop] [#3087 · 2025-09-25 · Skot Bitaxe] [#3089 · 2025-09-26 · econoalchemist] [#3091 · 2025-09-26 · econoalchemist]
- 2025-12-09: prototype PCBs + components on hand for only 5 boards — validate, revise, re-prototype before production; one Libre Board drives 4 Ember Ones (roughly 400 watts) [#3843 · 2025-12-09 · econoalchemist] [#3855 · 2025-12-09 · econoalchemist]
- 2026-01-02: first Ember One 00 v5 prototype finally on the pick-and-place [#4025 · 2026-01-02 · econoalchemist]
- 2026-01-08: first two Ember One (00 v5) boards assembled and shipped to Ryan to start validation; v5 remains a release candidate until validated [#4193 · 2026-01-08 · econoalchemist] [#4167 · 2026-01-07 · econoalchemist]

### Sleep-mode hazard (field report)

- csh2000/Loki: in sleep mode, hashboards with a PIC shut down, but PIC-less boards keep the VRM active — chips stay hot while not mining, leaving you fully dependent on fans; he had repeated fan-failure meltdowns/PSU trips before diagnosing it; flagged as critical for the Ember HB on PSUs with no regulation/communication [#3053 · 2025-09-18 · csh2000] [#3054 · 2025-09-18 · csh2000]
- emberOne can cut all power to the ASIC chips → very low quiescent draw [#3058 · 2025-09-23 · Skot Bitaxe]
- Stacking note (NebulaMiner): with Libre Board bottom facing emberOne bottom, LED + USB share a corner (only power-tab polarity flips) and ASIC heatsink heat ends up opposite the compute module and other M.2-sensitive components [#3075 · 2025-09-24 · NebulaMiner] [#3076 · 2025-09-24 · NebulaMiner]

## aditBoard & Auradine

- aditBoard (github.com/skot/aditBoard): adaptor from Antminer's proprietary data ribbon to USB-C so Libre Board + Mujina can eventually drive native Antminer hashboards; Libre Board provides 4 USB-C hashboard connectors (3 boards + spare) [#2166 · 2025-05-15 · econoalchemist] [#2250 · 2025-05-22 · econoalchemist]
- aditBoard as designed targets the S19j Pro, but should be mechanically and electrically compatible with everything down to the S9 — the remainder is software work (plus level shifters for Bitmain's 1.2V core) [#2446 · 2025-06-10 · Dimi8146] [#2451 · 2025-06-10 · Skot Bitaxe]
- Mike Hamilton wrote firmware that exercised S19 PSUs and offered to dig up his old code/documentation on their I2C interface [#2452 · 2025-06-10 · Mike Hamilton]
- aditBoard production: 100 boards quoted at $450 total; later 250 panelized boards sitting ready for the pick-and-place, queued behind Ember One & Libre Board prototypes [#2733 · 2025-07-31 · Dimi8146] [#3506 · 2025-11-21 · econoalchemist]
- Auradine: samples of 4nm and 3nm ASICs in hand, and the 256 Foundation was granted an entire reel of the 3nm ASICs; Auradine has tape-out in December [#3450 · 2025-11-20 · Reckless Apotheosis] [#3454 · 2025-11-20 · Reckless Apotheosis]; 'Auradine ASICs up for grabs' announcement [#3342 · 2025-11-18 · econoalchemist]
- Nobody sells Bitcrane or aditBoard yet (as of Nov 2025) — expected to change 'now that there is something to do with them' [#3504 · 2025-11-21 · Skot Bitaxe]

## Libre Board status

- Compute is open: any module conforming to the two-100-pin standard — Raspberry Pi CM5, x86, even RISC-V; ≥2 TB storage recommended so a full node fits [#2252 · 2025-05-22 · econoalchemist] [#2254 · 2025-05-22 · econoalchemist]
- First revision's connectors/layout opened for community feedback (GitHub issue #16) before the first test production [#2514 · 2025-06-17 · Michael Schmid @Schnitzel]
- Heater cases like the Stealth Miner expose only a single board edge, so port/button/SD placement matters for flashing without disassembly; Libre Board settled on two edges with user-accessible ports (front and top) [#2523 · 2025-06-18 · AgentP] [#2526 · 2025-06-18 · Michael Schmid @Schnitzel]
- Community PSU shortlist for a 10-hashboard stack: Bitmain APW7 (OK at 240V, weaker at 110V, keep under 80% load), Mean Well SE-1500-15, HP DPS-600PB, Mean Well LRS-600-12 [#2291 · 2025-05-27 · Toobahlou] [#2300 · 2025-05-28 · Toobahlou]
- rev 3 (July 2026): ~70% done in PCB design + schematic; remaining = build via assembly service and test; ~2 months to a validated rev 3, ~3 months if a rev 4 is needed; full documentation to follow [#5085 · 2026-07-22 · Michael Schmid @Schnitzel] [#5086 · 2026-07-22 · Michael Schmid @Schnitzel]
- 'Libreboard and Mujina already have full emberOne support' [#5102 · 2026-07-22 · Skot Bitaxe]

### Mini-rack direction (July 2026)

- After seeing rjk256's sous-vide setup, Skot proposed a native mini-rack form factor: 1U is 1.75-inch tall — fit a hashboard and heatsink in that and call it EmberOneU; one controller per rack driving hashboards over a USB hub; two 1200W APW3/7 PSUs side-by-side in 2U; possible hydro option [#5088 · 2026-07-22 · Skot Bitaxe] [#5093 · 2026-07-22 · Skot Bitaxe] [#5094 · 2026-07-22 · Skot Bitaxe] [#5097 · 2026-07-22 · Skot Bitaxe] [#5098 · 2026-07-22 · Skot Bitaxe] [#5100 · 2026-07-22 · Skot Bitaxe]

## Form-factor explorations

- The PC-AXE, a WIP drop-in graphics-card replacement: 'a drop in replacement for your graphics card with 14.4Th/s Hashrate at 180W' [#2472 · 2025-06-16 · Tyler Stevens]
- Skeptics: a PCIe slot supplies only 75W (hence extra power connectors), and dumping the heat inside a closed PC chassis is the real problem — called a non-starter without blower-style airflow [#2474 · 2025-06-16 · Reckless Apotheosis] [#2482 · 2025-06-16 · Reckless Apotheosis] [#2486 · 2025-06-16 · Reckless Apotheosis]
- Dimi's counter-direction: skip the GPU form factor — put hashboards on a server backplane (power + heat management integrated) with aditboards, or a unifi-style mini-lab where one 8-inch RU holds two stacked Ember Ones [#2501 · 2025-06-16 · Dimi8146] [#2508 · 2025-06-16 · Dimi8146] [#2510 · 2025-06-16 · Dimi8146]
- Proof-of-Steak: 'the first sous vide Bitcoin cooked steak' [#4356 · 2026-01-22 · Reckless Apotheosis]
- ProofofPrint: 3D-printer heated-bed hashrate project surfacing in the community (NYC collab) [#4412 · 2026-02-08 · MΛRCUS]

## Satoshi Starter

- Reckless Systems + My First Bitcoin: single-ASIC BZM2 miner crowdfund on Geyser — soft launch 2025-10-30, hard launch on White Paper Day 2025-10-31; billed as the first commercial BZM2 miner, first DIY-solderable kit miner, and the first miner with open ASIC documentation [#3166 · 2025-10-28 · Reckless Apotheosis] [#3187 · 2025-10-30 · Reckless Apotheosis] [#3202 · 2025-10-31 · Reckless Apotheosis] [#3203 · 2025-10-31 · Reckless Apotheosis]

## RDS bring-up (September 2026)

- Attempting a community PR on an Intel RDS with 300× BZM2 ASICs — if it works on the Intel controller it would be the highest-hashrate Mujina system so far; the first 2026 firmware build was written by Claude and deployed fully remotely [#5482 · 2026-09-14 · Reckless Apotheosis] [#5489 · 2026-09-14 · Reckless Apotheosis]
- 3.8kW of Mujina-controlled hash available to dump into a tank for the NYC workshop [#5522 · 2026-09-29 · Reckless Apotheosis]

## See Also

- [Mujina](../firmware/mujina.md)
- [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md)
- [Open Mining Economics](../economics/open-mining-economics.md)
- [Repair, Supply & Vendors](../industry/repair-supply-and-vendors.md)

## Contradictions & Open Questions

- Priority dispute: aditBoard-first vs emberOne-first (and what the foundation's economic logic even is) — see [Open Mining Economics](../economics/open-mining-economics.md).
- Whether BM1362 can be bought new on reels at all: Power Mining found none, Skot's NBTC channel dried up, yet Mega Miner quoted BM1362AC new on reel in July 2025 — bin matching unverified [#2656 · 2025-07-03 · Kristaps Stikuts] [#2665 · 2025-07-03 · econoalchemist].
- Proto-rig immersion claims (air/immersion convertible) questioned: flow-reversal warnings, asymmetric heatsinks and fan handling would need work; the 48V-fan boost reg sits on the hashboard [#2848 · 2025-08-15 · Wade Bowlin] [#2849 · 2025-08-15 · Wade Bowlin] [#2852 · 2025-08-15 · econoalchemist] [#2854 · 2025-08-15 · Wade Bowlin] [#2861 · 2025-08-15 · Skot Bitaxe] [#2863 · 2025-08-15 · Wade Bowlin]
