# Libre Board & Mining Control Boards

> Sources: libreboard.org and 256foundation/libreboard GitHub issues & PRs, 2025-02 → 2026-04 (captured 2026-10-07); 256foundation/emberone-usbserial-fw README, issues & PRs, 2025-01 → 2026-03; 256foundation/BCB100 and bos-build READMEs; Mujina repo, forum & mujina-xilinx-platform captures, 2026-03 → 2026-10; 256 Foundation newsroom & Assembling Freedom newsletter, 2025-05 → 2026-09; 256 Foundation Telegram group, 2025-05 → 2026-07; POD256 transcripts, 2025-10 → 2026-09
> Raw: [libreboard.org](../../raw/hardware/256f-hardware/libreboard-org-home.md); [Libre Board connector placement (#16)](../../raw/hardware/256f-hardware/2025-05-30-github-libreboard-issue-16-connector-placement.md); [Libre Board rev 3 funding](../../raw/history/256f-org/256foundation-org-newsroom-libre-board-funding.md); [BCB100 README](../../raw/hardware/256f-hardware/github-256foundation-bcb100.md); [emberone-usbserial-fw README](../../raw/hardware/256f-hardware/github-256foundation-emberone-usbserial-fw.md); [mujina-xilinx-platform README](../../raw/firmware/mujina/github-256foundation-mujina-xilinx-platform.md); [POD256 e091](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-22-e091.md); [POD256 e092](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-29-e092.md); [POD256 e098](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-12-13-e098.md); [POD256 e099](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-12-17-e099.md); [POD256 e100](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-12-31-e100.md); [POD256 e102](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-01-30-e102.md); [POD256 e103](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-02-04-e103.md); [POD256 e109](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-03-25-e109.md); [POD256 e113](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-04-22-e113.md); [POD256 e114](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-05-13-e114.md); [POD256 e123](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-10-e123.md); [POD256 e126](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-21-e126.md); [POD256 e127](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-28-e127.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

A **control board** is the computer in a miner: it talks to the hashboards, sequences power, drives fans, and runs the mining firmware. On commercial machines it is closed — a vendor image on a locked-down board — which is why the 256 Foundation funds **Libre Board**, an open-hardware (CERN-OHL-S) control board that runs full Linux on a swappable compute module and drives [Ember One](ember-one-bzm2.md) hashboards over USB-C ([libreboard.org](../../raw/hardware/256f-hardware/libreboard-org-home.md); [Libre Board funding newsroom](../../raw/history/256f-org/256foundation-org-newsroom-libre-board-funding.md)). This article covers Libre Board's grant, design decisions, errata and status; compares it with the two other boards the open-mining community actually hacks on — the **Braiins BCB100** (open-sourced, forked by the 256 Foundation) and **stock Antminer control boards** (Amlogic and Xilinx Zynq-7007S); and documents **emberone-usbserial-fw**, the RP2040 board-management firmware that sits on the hashboard side of the USB link. For a newcomer: if you want to run open firmware today, a stock S19 board or a BCB100 is the hacking path; Libre Board is the reference design meant to make that unnecessary.

## Control boards compared

| | Libre Board | Braiins BCB100 | Antminer stock (Amlogic) | Antminer stock (Xilinx Zynq-7007S) |
|---|---|---|---|---|
| License | CERN-OHL-S ([libreboard.org](../../raw/hardware/256f-hardware/libreboard-org-home.md)) | Open-sourced by Braiins; bos-build is GPL v3.0 ([bos-build](../../raw/hardware/256f-hardware/github-256foundation-bos-build.md)) | Proprietary | Proprietary |
| Compute | Any module on the two 100-pin CM connectors (Raspberry Pi CM5; x86/RISC-V intended) | STM32MP157CAB3: two 650MHz A7 cores + Cortex M3 ([BCB100](../../raw/hardware/256f-hardware/github-256foundation-bcb100.md)) | Amlogic SoC | Zynq-7007S (ARMv7 + FPGA) ([mujina-xilinx-platform](../../raw/firmware/mujina/github-256foundation-mujina-xilinx-platform.md)) |
| Hashboard link | USB-C (4 ports) | Antminer ribbon connectors | Antminer ribbon connectors | Antminer ribbon connectors via FPGA |
| Power in | 12-24 VDC | 12V from PSU auxiliary connector | PSU auxiliary | PSU auxiliary |
| Open firmware path | Raspberry Pi OS / MujinaOS (planned) | bos-build images; community Mujina fork | Mujina via LuxOS or USB burn | mujina-xilinx-platform ramdisk |
| Status (2026-10) | Rev 3 in validation | Shipping hardware | Mujina in forks | Development package |

## Libre Board

### Grant and license

- The grant officially launched on April 5, 2025, funding one project manager (@econoalchemist) and one engineer (@Schnitzel) on six-month cycles renewable "pending negotiations"; exact dollar amounts are kept confidential, disbursed monthly in equal amounts ([libreboard.org](../../raw/hardware/256f-hardware/libreboard-org-home.md)).
- The project is "fully open-source CERN-OHL-S licensed"; sales, distribution, marketing and customer technical support were excluded from the proposal ([libreboard.org](../../raw/hardware/256f-hardware/libreboard-org-home.md)).
- Six-month deliverable: a board based on the Raspberry Pi Compute Module I/O Board with USB hub, fan support, NVME, two 100-pin compute-module connectors, Ethernet, HDMI, an Rpi 40-pin header, a MIPI touchscreen port, and 12-24 VDC input — built so future ARM, x86 and RISC-V modules can be supported ([libreboard.org](../../raw/hardware/256f-hardware/libreboard-org-home.md)).
- Stated mission beyond driving hashboards: run a Bitcoin full node and a stable Stratum server on the same board ([libreboard.org](../../raw/hardware/256f-hardware/libreboard-org-home.md)); the Telegram vision is an all-in-one box plugged via USB to every hashboard, running Mujina OS with an integrated node and pool ([256F Telegram](../../raw/history/2026-10-08-256f-telegram-signal.md)).
- Why not just adopt the newly open-sourced Braiins Control Board? The Foundation explicitly decided not to, and laid out its own I/O list instead ([newsletter, 2025-06-19](../../raw/history/256f-newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md)).

### Compute: the CM5 and bring-your-own-module connectors

- Libre Board is a fork of the Raspberry Pi CM5 I/O board; the standard two 100-pin connectors let the end user choose which Linux-compatible compute module and how much RAM to run. Until boards ship, a CM5 plus Raspberry Pi's own I/O board is "super close" for developing Mujina ([256F Telegram #3422/#3425](../../raw/history/2026-10-08-256f-telegram-signal.md)).
- On POD256 #92 (2025-10-29) Ryan explained the philosophy: "we shouldn't box users into telling them which processor they have to use on their Libre board" — RISC-V compute modules adhering to the two 100-pin standard could be swapped in, or x86, or ARM, without changing the underlying hardware; Milk-V was named as one of the companies making RISC-V compute modules ([POD256 e092](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-29-e092.md)).
- ≥2 TB storage was recommended so a full node fits ([256F Telegram](../../raw/history/2026-10-08-256f-telegram-signal.md)).
- Libre Board has no FPGA, so the CM5 must do all job/midstate generation. Ryan hypothesised a CM5 could easily handle a bunch of BM13xx chips; Reckless Apotheosis cautioned that Bitmain systems use an FPGA because "the typical control board can't generate 300 jobs", and that Intel chips need much more handholding ([256F Telegram #3521–#3547](../../raw/history/2026-10-08-256f-telegram-signal.md)).
- Software plan: Libre Board runs Raspberry Pi OS out of the box; the bigger goal is MujinaOS, a whole Linux OS for Libre Board and eventually other control boards ([256F Telegram](../../raw/history/2026-10-08-256f-telegram-signal.md)).

### Design decisions (rev 1 issue tracker)

| Decision | Detail | Source |
|---|---|---|
| Input power | CM5 IO board's 5V-only input changed to 12-24V like Ember One; a 12V output added because CM5 IO fans are 5V (closed 2025-09-24) | [#1](../../raw/hardware/256f-hardware/2025-04-09-github-libreboard-issue-1-12-24v-input-voltage.md) |
| Fans | Keep the CM5 JST-SH PWM header; add 4 hashboard fan connectors on an EMC2305 5-port I2C PWM controller (no Pi PWM pin used) | [#3](../../raw/hardware/256f-hardware/2025-04-09-github-libreboard-issue-3-fan-connectors.md) |
| Ports trimmed | USB-A → USB-C to match Ember One; one of two HDMI and one of two MIPI removed | [#2](../../raw/hardware/256f-hardware/2025-04-09-github-libreboard-issue-2-change-usb-a-ports-to-usb-c.md), [#4](../../raw/hardware/256f-hardware/2025-04-09-github-libreboard-issue-4-remove-1-of-two-hdmi-ports.md), [#5](../../raw/hardware/256f-hardware/2025-04-09-github-libreboard-issue-5-remove-1-of-two-mipi-interfaces.md) |
| Form factor | 128mm x 128mm first proposed; Ember One changed to 125x125mm, Libre Board followed with matching corner holes so boards stack on standoffs | [#6](../../raw/hardware/256f-hardware/2025-04-09-github-libreboard-issue-6-agree-on-formfactor.md), [#11](../../raw/hardware/256f-hardware/2025-05-13-github-libreboard-issue-11-feature-request-board-holes-which.md) |
| Hashboard ports | At least 4 USB-C so three hashboards plus one accessory run without a hub; two USB3 stacks added (2025-06-09) | [#10](../../raw/hardware/256f-hardware/2025-05-13-github-libreboard-issue-10-feature-request-at-least-4-usb-c.md) |
| Serial console | Pi header pins 6, 8, 10 routed to a 3-pin .100-inch header, reachable with a HAT installed | [#12](../../raw/hardware/256f-hardware/2025-05-13-github-libreboard-issue-12-feature-request-route-serial-cons.md) |
| Status LED | Same SK6812 RGB LED as Ember One; needs an SPI-capable pin because Linux cannot bit-bang its timing (CM5 PIO would tie the design to the CM5) | [#13](../../raw/hardware/256f-hardware/2025-05-13-github-libreboard-issue-13-feature-request-an-indicator-led.md) |
| Qwiic | 4-pin JST SH I2C (Qwiic/STEMMA QT) next to the M2 slot | [#14](../../raw/hardware/256f-hardware/2025-05-13-github-libreboard-issue-14-feature-request-an-4-pin-connecto.md) |
| Boot button | Momentary pushbutton in parallel with the boot jumper — eMMC modules don't boot from SD; holding the boot pin low after power-up puts the CM5 in USB loader mode for rpiboot | [#15](../../raw/hardware/256f-hardware/2025-05-28-github-libreboard-issue-15-feature-request-a-momentary-pushb.md) |
| Regulators | 12v and 5v regulators upgraded to I²C-capable parts (about 10 components changed) so per-rail power can be monitored; UK-specific Pi I/O board parts removed from the BOM; the board is a 6-layer PCB | [newsletter, 2025-09-25](../../raw/history/256f-newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md) |
| Manufacturability | Consider switching 0402 parts to 0603 or 0805 for easier pick-and-place | [#20](../../raw/hardware/256f-hardware/2026-03-11-github-libreboard-issue-20-consider-switching-0402-component.md) |

**Power budget** (POD256 #91): the Libre Board is designed to be line-powered, not battery-sipping — "You need to provide your 12 to 17 volts", "at potentially a 100 watts continuously. And I I don't think it makes sense to make that low power"; low-power optimization is left to accessories ([POD256 e091](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-22-e091.md)). (The 12-17V figure tracks the v5 Ember One input range it drives — see the input-voltage Disputed block in [Ember One & the BZM2 Hardware Stack](ember-one-bzm2.md).)

**Connector placement** (issue #16, opened for community feedback before first test production): power input (12-24v) and the two USB double-stacks on the back edge, aligned with Ember One; power button, boot button, SD slot and three LEDs on the top edge; MIPI, HDMI, Ethernet and one USB-C on the front edge; fans, HAT, compute-module connectors, battery and M2/NVME on the board face. The top-edge USB-C maps to the CM5 IO board's J11 port used for flashing the eMMC ([#16](../../raw/hardware/256f-hardware/2025-05-30-github-libreboard-issue-16-connector-placement.md)). The two-edge choice came from heater cases such as the Stealth Miner, which expose only one board edge — port, button and SD placement decide whether you can flash without disassembly ([256F Telegram](../../raw/history/2026-10-08-256f-telegram-signal.md)).

**Graceful shutdown** on power loss was requested for Mujina OS. The on-board CR2032 only powers the RTC; zbomz noted a CR2032's typical max pulse current is 15mA versus CM5 draw of about 400mA idle and 900mA operating, suggesting a small LiPo with a charge controller (with the caveat that LiPo is sensitive at high temperature) ([#8](../../raw/hardware/256f-hardware/2025-05-03-github-libreboard-issue-8-feature-request-provision-for-grac.md)).

**Antminer hashboards**: options listed for S9 boards were flashing Mujina onto the S9 board itself, using Libre Board with the Adit Board adapter, or forking Libre Board as a direct replacement ([#9](../../raw/hardware/256f-hardware/2025-05-06-github-libreboard-issue-9-feature-request-s9-board-plug-and.md)). An even earlier suggestion was to start from the Antminer BeagleBone-Black-style control board, at "around 10USD per unit" ([libre-board-website #2](../../raw/hardware/256f-hardware/2025-02-06-github-libre-board-website-issue-2-controllboard-form-factor.md)). See the aditBoard section of [Ember One & the BZM2 Hardware Stack](ember-one-bzm2.md).

On POD256 #99 Scott drew the division of labor: Libre Board is also an Antminer control-board replacement but "it it is a Raspberry Pi also", "that would run Mugena on it directly" — the choice for a standalone unit — "Added board and bit crane are just kind of a different way of doing it", pushing the firmware out to a separate host over USB ([POD256 e099](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-12-17-e099.md)). The Adit itself is more than wire routing: Bitmain's hashboard data connector has about 20 pins (enable, I2C to the temperature sensors, serial to the ASICs and more), so the Adit runs an RP2040 as a USB-to-serial bridge — and a Whatsminer variant is "not a big change. It is a change, but it shouldn't be too hard" ([POD256 e099](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-12-17-e099.md)). Conversely, Libre Board talks USB-C data to the hashboards, so driving traditional proprietary-connector hashboards needs an adapter like the Adit ([POD256 e127](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-28-e127.md)).

### Adit board build arc (POD256)

- 2025-12-13 (e098): Eco had made 150 Adit boards but expected "maybe five that'll actually work out the gate without any rework" — cheap Amazon solder paste bridged the RP2040 pins ([POD256 e098](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-12-13-e098.md)).
- 2025-12-31 (e100): "I've got almost a 100 of these soldered together now, and I'm ready to to try powering them up and testing them, flashing them with the appropriate firmware" — the Adit lets a user talk to an Antminer hashboard over USB-C instead of the proprietary data connector ([POD256 e100](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-12-31-e100.md)).
- 2026-09-28 (e127): of the 100 made, "like, 80 that actually responded" when plugged into his laptop — ready only for firmware; the Ant Hats still need to be built; and Kurt from Gridless made a WhatsMiner version of the Adit board ([POD256 e127](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-28-e127.md)).

### Rev 1 errata: the TUSB4041I USB hub

On rev 1 the on-board 4-port hub (U11) stopped enumerating upstream after working for several hours ([#22](../../raw/hardware/256f-hardware/2026-04-19-github-libreboard-issue-22-onboard-4-port-usb-hub-does-not-e.md)). The follow-up issues list datasheet violations — a checklist worth running on any TUSB4041I design:

| Pin | Problem | Fix | Source |
|---|---|---|---|
| USB_VBUS (pin 16) | Tied straight to 5V; absolute max 1.4V | Divider to stay under 1.15V | [#23](../../raw/hardware/256f-hardware/2026-04-19-github-libreboard-issue-23-usb-vbus-on-u11-pin-16-exceeds-ab.md) |
| XI (pin 30) | Driven by a 3.3V clock; absolute max 2.45V | 1.8V clock source | [#24](../../raw/hardware/256f-hardware/2026-04-19-github-libreboard-issue-24-oscillator-input-on-u11-pin-30-is.md) |
| GRTz reset (pin 18) | Must be held 3ms after power is stable; the 10k × 100nF RC (1ms) crosses the threshold too early | Longer reset delay | [#25](../../raw/hardware/256f-hardware/2026-04-19-github-libreboard-issue-25-grtz-u11-pin-18-reset-timing-is-i.md) |
| TEST (pin 17) | Floating (has an internal pulldown) | External 4.7k pulldown per reference design | [#26](../../raw/hardware/256f-hardware/2026-04-19-github-libreboard-issue-26-test-u11-pin-17-left-floating.md) |
| Power switching | Hub wired for ganged power | Per-port switching so Mujina can power-cycle individual hashboards (also the only way to hard-reset an Ember One's always-on 3V3 rail) | [#21](../../raw/hardware/256f-hardware/2026-03-19-github-libreboard-issue-21-consider-wiring-the-usb-hub-in-a.md) |

### Status and demos

- Late 2025: prototypes delayed when customs destroyed a shipment of components ([newsletter, 2025-11-24](../../raw/history/256f-newsletter/2025-11-24-assembling-freedom-11.md)); a nearly 2-hour live schematic review covered ground vias, regulators, thermal management, USB-C power negotiation, I2C bus management, GPIO multiplexing, fan control and LED timing ([newsletter, 2025-10-28](../../raw/history/256f-newsletter/2025-10-28-assembling-freedom-10.md)).
- 2026-01-30 (POD256 e102): first Libre Board boot — at Telehash 2 a Libre Board prototype ran Mujina driving three Ember One hashboards to HydraPool live on stream for eight hours ("first LibreBoard boot up as well from Schnitzel. And it worked"), with a water temperature probe feeding back into the control board for the sous-vide demo ([POD256 e102](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-01-30-e102.md); [POD256 e103](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-02-04-e103.md)).
- One Libre Board drives 4 Ember Ones, "about 400 Watts of the way there" toward a larger build ([256F Telegram #3855](../../raw/history/2026-10-08-256f-telegram-signal.md)). On POD256 #109 (2026-03-25) the hosts reconfirmed four hashboards — "has four USB C ports on it. So I think you could plug in a USB hub to one of those expand that capacity" — with the ceiling set by a bandwidth limit Schnitzel would know, and framed the board's purpose as connecting "to relays and switches and sensors to integrate their miners into other systems like home heating systems", with "version three out later this year" ([POD256 e109](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-03-25-e109.md)).
- April 2026: "LibreDOOMAxe" — Schnitzel ran Doom on a Libre Board with a Bitaxe as hashboard via bitaxe-raw under Mujina, plus OLED stats, Qwiic temperature sensors, fan RPM control, RGB temperature indicators and an HDMI dashboard. The same issue brainstormed Libre Board as a bridge translating 24V home-thermostat "heat calls" into miner ramp commands ([newsletter, 2026-04-22](../../raw/history/256f-newsletter/2026-04-22-assembling-freedom-25.md)). POD256 #113 grounds the sprint: after the April 1 grant restart Schnitzel went "pedal to the metal, going through LibreBoard, trying to make improvements to the voltage regulator, addressing some of the bugs that we had from versions one and two, getting version three ready to go into production", validating by plugging in displays and devices — including Doom on a Raspberry Pi hat with a miniature joystick board and LED grid showing armor left. The stated goals: run a full node on it, deploy HydraPool across platforms, and be "that bridge that integrates with whatever your miners are trying to heat" — talk to sensors, control switches and relays, read temperature sensors. The episode also hatched the thermostat-HAT idea: wire a thermostat's 24-volt stage-one signal "straight to a Libre board", ideally as a little Raspberry Pi-style HAT ([POD256 e113](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-04-22-e113.md)).
- May 2026: Schnitzel's **Doom Axe** — a battery-powered 3D-printed box with a Libre Board running Mujina and HydraPool, a Bitaxe as miner, stats screens and LEDs, playable Doom — "he had a full full node running on the box too, running on LibreBoard", "He had the SSD in there" — and the whole thing came together in about eight days ([POD256 e114](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-05-13-e114.md)).
- Bitcoin 2026: **DOOMAXE**, a fully open reference miner (Libre Board + Mujina + Bitaxe hashboard, with Hydrapool and a node on the miner) whose front screen plays Doom ([MARA Foundation newsroom](../../raw/history/256f-org/256foundation-org-newsroom-mara-foundation-tier1-supporter.md)).
- July 2026: rev 3 about 70% done in PCB design and schematic, with roughly 2 months to a validated rev 3 (3 if a rev 4 is needed); "Libreboard and Mujina already have full emberOne support" ([256F Telegram #5085/#5102](../../raw/history/2026-10-08-256f-telegram-signal.md)).
- August 2026 (POD256 #123): the on-board M.2 NVMe slot as the node-enabler — "if you have something like the LibreBoard that has an m two NVMe slot in it, then you could get a much more affordable, like, 32 gig or 64 gig drive" (~$20) and run a pruned node, putting "a node right in your miner" ([POD256 e123](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-10-e123.md)).
- September 2026 (POD256 #126): during the earlier rev 3 work AI had been used to help design the USB configuration and "in fact, incorrectly instructed us to do" it; months later, pointed at the same problem again, AI identified the flaw in its own earlier advice — an emblem of how fast the tooling is moving ([POD256 e126](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-21-e126.md)).
- September 2026 (POD256 #127), rev 3 manufacturing: with Eco's pick-and-place machines not set up, "we're gonna use a third party vendor to build the third revision"; Eco will pass his box of leftover first-revision components to Schnitzel to hand-solder "a couple of the through hole components" and finish the boards; "sometime in October, we've got a third revision on the bench being validated", and pending that, either further revisions or a design manufacturers can "grab and go" with, followed by extensive documentation ([POD256 e127](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-28-e127.md)). Design philosophy from the same episode: "it's a lot easier for people to like remove things from the design than to add things to the design" — e.g. if you don't need the HDMI port, deleting that section in KiCad is easier than adding one would have been ([POD256 e127](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-28-e127.md)).
- Funding: Libre Board "has had funding paused for months" before the HRF grant of August 25, 2026 ([HRF newsroom](../../raw/history/256f-org/256foundation-org-newsroom-hrf-renews-support.md)). The reactivated term runs four months, September through December, to validate rev three: power and interface stages from 12 to 24 volts DC across compute options, the full peripheral set, mechanical fit, end-to-end bring-up with Mujina, and cutting rev three to fab with an updated BOM ([Libre Board funding newsroom](../../raw/history/256f-org/256foundation-org-newsroom-libre-board-funding.md)).

## Braiins BCB100 (256foundation fork)

The BCB100 is described in the 256foundation fork as the "final production release of Braiins BCB100" ([BCB100 README](../../raw/hardware/256f-hardware/github-256foundation-bcb100.md)).

| Spec | Value |
|---|---|
| Compatibility | All S19 models except Hydro; immersion ready; fits standard enclosures |
| MPU | STM32MP157CAB3 (two 650MHz A7 cores + Cortex M3, LFBGA354) |
| Memory | 128 MB RAM, 4GB eMMC |
| Network | 10/100 Mb Ethernet via Microchip 8710 PHY (no USB port, per [256F Telegram #4661](../../raw/history/2026-10-08-256f-telegram-signal.md)) |
| Power | 12V from the PSU auxiliary connector; 3.3V/1.35/0.65V rails; average draw 250 mA |
| Board | 6-layer PCB, 110mm × 100mm, ~130g |
| Boot | eMMC by default; to boot SD, insert the card and reset the MPU |

All values: [BCB100 README](../../raw/hardware/256f-hardware/github-256foundation-bcb100.md). The Braiins Mini Miner (BMM 100) uses the same board with an extra display connector ([bos-build](../../raw/hardware/256f-hardware/github-256foundation-bos-build.md)).

### Building and flashing Braiins OS with bos-build

1. Nix is the only dependency: `nix run .#bootstrap`, `nix run .#configure`, then `nix run .#make` (OpenWrt-based; images land in `build/openwrt/bin/targets/stm32mp15/ii1/`).
2. eMMC image set: TF-A first-stage bootloader, a U-Boot FIP, a SquashFS rootfs and an eMMC sysupgrade tar; SD images are a packed card image plus SD sysupgrade.
3. First install boots from SD, then writes to internal eMMC (OTP MAC/serial programming, hardware partitioning, then `dd` of FSBL/FIP/rootfs).
4. Serial prefixes by revision: P02 `BCB100A0A...` (first limited series), P03 rev A1.1 `BCB100A1A1...`, P03 rev A1.2 (BMM 100, the final one with LCD connector).
5. **Gotcha:** `mmc write_reliability set -y` is one-time programmable and irreversible.

Source: [bos-build README](../../raw/hardware/256f-hardware/github-256foundation-bos-build.md) (GPL v3.0).

### Mujina on BCB100

- April 2026: Aadhi M published BCB100_Mujina, a Mujina build for the BCB100 running Debian, to test on Loki rigs; one of his boards arrived without Braiins OS and did not respond over SWD ([256F Telegram #4655–#4683](../../raw/history/2026-10-08-256f-telegram-signal.md)). The newsletter framed it as expanding Mujina to whole generations of S19s ([newsletter, 2026-04-11](../../raw/history/256f-newsletter/2026-04-11-assembling-freedom-23.md)).

## Stock Antminer control boards

Two problems are distinct: getting arbitrary software onto a locked control board, and adding Mujina support for that board; porting docs must lead with safety warnings ([Mujina dev call #2](../../raw/firmware/mujina/2026-05-05-forum-mujina-dev-call-2.md)).

### Amlogic boards (S19 family)

- 2026-03-09: Skot got "a very rough version of Mujina compiled and working on a S19j Pro with a stock bitmain control board" ([256F Telegram #4553](../../raw/history/2026-10-08-256f-telegram-signal.md)); POD256 #107 described flashing over Ethernet/USB via LuxOS (no SD card), with Rust drivers for temp sensors, fans and the undocumented APW12 PSU interface ([newsletter, 2026-03-11](../../raw/history/256f-newsletter/2026-03-11-assembling-freedom-19-revolutionizing-bitcoin-mining-hacking.md)).
- Real S19 support means driving BM1362 chips over UART, the APW12 over I2C, fans, EEPROM decode and PIC sensor reads; `skot/amlogic-cb-tools` validates those interfaces ([Mujina PR #55](../../raw/firmware/mujina/2026-05-04-github-mujina-pr-55-make-non-glibc-linux-cross-compilation-w.md)).
- **Methods**: (1) with LuxOS installed — stop LuxOS, compile Mujina for ARM, copy it over ([256F Telegram #4734](../../raw/history/2026-10-08-256f-telegram-signal.md)); (2) "USB burn" — the board enumerates as a USB device in USB Burning mode (jumper or U-Boot command), works even on bricked installs, but you must use Bitmain's signed bootloader and boot partitions ([256F Telegram #4737–#4755](../../raw/history/2026-10-08-256f-telegram-signal.md)).
- **Persistence**: the stock Bitmain filesystem is not writeable; the daemonc root exploit used by LuxOS was blocked by a Bitmain update in mid-2025 and recent LuxOS turned off root, so recent-firmware boards need USB burn to roll back to early-2025 firmware ([Mujina forum: Antminer](../../raw/firmware/mujina/2026-05-11-forum-mujina-antminer.md)).
- Tip: start from Skot's `amlogic-s19jpro` Mujina fork rather than rebuilding PSU control logic ([Mujina forum: best practices](../../raw/firmware/mujina/2026-05-18-forum-best-practices-for-hacking-mujina-onto-other-miners.md)).
- Ampminer (April 2026): a stock S19j Pro on Mujina using the control board's hidden USB port with a hub for a Wi-Fi dongle and a touchscreen ([newsletter, 2026-04-22](../../raw/history/256f-newsletter/2026-04-22-assembling-freedom-25.md)).

### Xilinx Zynq-7007S boards: mujina-xilinx-platform

- RSA authentication is permanently enabled in eFuses, so BOOT.bin and the kernel cannot be replaced; but U-Boot verifies the ramdisk only by SHA256 against the mtd3 signature partition. Writing a custom ramdisk to mtd1 and patching mtd3 bytes 1024-1279 with its SHA256 boots custom firmware ([mujina-xilinx-platform](../../raw/firmware/mujina/github-256foundation-mujina-xilinx-platform.md)).
- NAND layout: mtd0 40MB BOOT.bin + kernel (preserved), mtd1 32MB ramdisk (replaced), mtd2 8MB configs, mtd3 2MB signatures (patched), mtd4 171MB reserve ([mujina-xilinx-platform](../../raw/firmware/mujina/github-256foundation-mujina-xilinx-platform.md)).
- Build: Linaro GCC 7.2-2017.11 with 4.6.x headers for the stock 4.6.0-xilinx kernel; stock `bitmain_axi.ko` and `fpga_mem_driver.ko` modules are reused. First install uses `bitmain_ramdisk_install.sh`; serial console needs a 3.3V USB-TTL adapter (never 5V) at 115200 8N1 ([mujina-xilinx-platform](../../raw/firmware/mujina/github-256foundation-mujina-xilinx-platform.md)).
- A test-fixture kit runs Bitmain's factory `single_board_test` without fixture hardware via an LD_PRELOAD shim, with `fpga_logger` polling FPGA registers for reverse engineering ([xilinx test fixture](../../raw/firmware/mujina/github-mujina-xilinx-platform-br2-external-bitmain-board-xil-2.md)).
- Origin: Dan Sokil moved his buildroot work to the 256 Foundation in November 2025 — "first to execute Mujina on a Zynq" — initially reusing the Bitmain FPGA bitstream ([256F Telegram #3419–#3499](../../raw/history/2026-10-08-256f-telegram-signal.md)).

### PSU and power gotchas

- Stopping the LuxOS service caused the PSU to cut hashboard power, so chips could not be read until PSU control was handled ([Mujina forum: best practices](../../raw/firmware/mujina/2026-05-18-forum-best-practices-for-hacking-mujina-onto-other-miners.md)).
- Without proper driver tuning, boards on Mujina can overheat and bad fan control can trip breakers; community APW12 120V mods exist ([newsletter, 2026-03-11](../../raw/history/256f-newsletter/2026-03-11-assembling-freedom-19-revolutionizing-bitcoin-mining-hacking.md)). AgentP's S19XP test used one hashboard, an external duct fan and an APW12 modded for 120V, with LuxOS at 110MHz for "\~10TH and 290W" ([Mujina forum: best practices](../../raw/firmware/mujina/2026-05-18-forum-best-practices-for-hacking-mujina-onto-other-miners.md)).
- Community request: PSU bypass support so S19 owners don't need Loki kits ([Mujina forum: Antminer](../../raw/firmware/mujina/2026-05-11-forum-mujina-antminer.md)).
- Sleep-mode hazard: hashboards without a PIC keep the VRM active in sleep, so chips stay hot with no mining — dangerous on PSUs with no communication with the control board ([256F Telegram](../../raw/history/2026-10-08-256f-telegram-signal.md)).

## emberone-usbserial-fw (RP2040 board management)

Every Ember One carries an RP2040 that turns USB into the hashboard's control and ASIC buses; the control board (Libre Board, a laptop, anything running Mujina) is the host ([emberone-usbserial-fw README](../../raw/hardware/256f-hardware/github-256foundation-emberone-usbserial-fw.md)).

**Build/flash**: Rust, target `thumbv6m-none-eabi`; flash via probe-rs over SWD (`cargo flash --release --chip RP2040`) or convert to UF2 with `elf2uf2-rs`.

**Ports**: the first serial port is *control* (I2C, GPIO, ADC, LED; baud rate ignored); the second is *data*, a transparent UART pass-through to the ASIC chain whose baud rate mirrors the USB setting.

**Control packet** (`LEN LO, LEN HI, ID, BUS, PAGE, CMD, DATA`): length is the whole packet; ID is echoed back; BUS is always 0x00.

| Page | Commands |
|---|---|
| I2C `0x05` | write `0x20`, read `0x30`, readwrite `0x40`; data = [address, bytes to write, bytes to read] |
| GPIO `0x06` | `0x00` ASIC reset (active low), `0x01` ASIC power enable, `0x02` ASIC IO power enable; omit data to read the level |
| ADC `0x07` | `0x50` read VDD, `0x51` read VIN |
| LED `0x08` | `0x10` set RGB colour |

Example: write 0xDE to I2C address 0x4F is `08 00 01 00 05 20 4F DE` ([README](../../raw/hardware/256f-hardware/github-256foundation-emberone-usbserial-fw.md)). The same framing is used by Bitaxe's bitaxe-raw host-control firmware ([bitaxe-raw README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxe-raw.md)).

### History and USB identity

| Date | Change | Source |
|---|---|---|
| 2025-03-15/16 | DMA NeoPixel and ADC commands added | [PR #3](../../raw/hardware/256f-hardware/2025-03-15-github-emberone-usbserial-fw-pr-3-add-dma-neopixel-command.md), [PR #4](../../raw/hardware/256f-hardware/2025-03-15-github-emberone-usbserial-fw-pr-4-add-adc-command.md) |
| 2026-02-18 | Placeholder VID:PID 0xc0de:0xcafe replaced by **1209:256f**, allocated to Ember One via pid.codes | [PR #16](../../raw/hardware/256f-hardware/2026-02-06-github-emberone-usbserial-fw-pr-16-feat-usb-use-pid-codes-vi.md) |
| 2026-03-19 | USB serial number from the flash chip's per-chip unique ID (0x4B) — the JEDEC ID gave every board the same serial; `v5_support` branch (VDDIO_EN GPIO) merged to main | [PR #19](../../raw/hardware/256f-hardware/2026-03-19-github-emberone-usbserial-fw-pr-19-fix-usb-derive-serial-num.md), [PR #17](../../raw/hardware/256f-hardware/2026-03-19-github-emberone-usbserial-fw-pr-17-feat-merge-emberone-v5-su.md) |
| 2026-03-20 | **bcdDevice scheme**: major = hardware revision, minor.patch = firmware version, restarting per revision (v5.0.0 for hardware 5) so Mujina can tell v4/v5/later boards apart | [PR #15](../../raw/hardware/256f-hardware/2026-01-18-github-emberone-usbserial-fw-pr-15-feat-usb-set-bcddevice-to.md) |
| 2026-03-19 (open) | Reboot and reboot-to-bootloader commands, guarded by a magic payload, sending no response (success = USB re-enumeration or a UF2 device) | [PR #18](../../raw/hardware/256f-hardware/2026-03-19-github-emberone-usbserial-fw-pr-18-feat-reboot-add-system-re.md) |
| 2026-03-28 (open at capture) | **Breaking**: every response gets a status byte at offset 3 (0x00 = success) and length means total packet length, bumping firmware to v5.1.0 | [PR #20](../../raw/hardware/256f-hardware/2026-03-28-github-emberone-usbserial-fw-pr-20-fix-control-unify-respons.md) |

Why v5.1.0 matters for host code: before it, success responses used payload-only length while errors used total length, and an error code sat where the first data byte would be — no way to tell them apart on the wire ([PR #20](../../raw/hardware/256f-hardware/2026-03-28-github-emberone-usbserial-fw-pr-20-fix-control-unify-respons.md)). Mujina's PR #107 (2026-08-30) describes a "v1 response frame the EmberOne firmware also uses", selected by product string, while bitaxe-raw boards keep the v0 frame ([Mujina PR #107](../../raw/firmware/mujina/2026-08-30-github-mujina-pr-107-feat-bitaxe-support-the-rhap-d-firmware.md)).

Open requests: a static `device_type` command so the control board can detect board features, and multi-board support (two emberOnes on a Mac showed only one set of ports) ([#13](../../raw/hardware/256f-hardware/2025-04-18-github-emberone-usbserial-fw-issue-13-add-static-device-type.md), [#14](../../raw/hardware/256f-hardware/2025-04-18-github-emberone-usbserial-fw-issue-14-support-multiple-usb.md)). Stratum V2 belongs in Mujina, not the hashboard firmware ([#1](../../raw/hardware/256f-hardware/2025-01-30-github-emberone-usbserial-fw-issue-1-stratum-v2.md)).

## Contradictions & Open Questions

- Libre Board repo naming: the newsroom links `github.com/256foundation/libre-board` while the captured README is `256foundation/libreboard` ([funding newsroom](../../raw/history/256f-org/256foundation-org-newsroom-libre-board-funding.md); [libreboard README](../../raw/hardware/256f-hardware/github-256foundation-libreboard.md)).
- Whether the CM5 alone can generate enough work for large chains without an FPGA is untested at Antminer scale (see Compute above).
- PR #20 (v5.1.0 response format) was still open in the 2026-10-07 capture; confirm which frame your board answers with via bcdDevice before writing host code.

## See Also

- [Ember One & the BZM2 Hardware Stack](ember-one-bzm2.md)
- [Mujina](../firmware/mujina.md)
- [Bitmain ASIC Reference](bitmain-asic-reference.md)
- [Heater Electrical & 120V Builds](heater-electrical-and-120v-builds.md)
- [Heater Firmware & Power Control](../firmware/heater-firmware-and-power-control.md)
- [RHAP](../protocols/rhap.md)
- [Mining Firmware Security](../industry/mining-firmware-security.md)
- [256 Foundation Organization](../history/256-foundation-organization.md)
