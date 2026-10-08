# POD256 Episode 091: Hash, Heat, and Hardware: LibreBoard, Mujina, and the BitAxe Battle

> Sources: POD256 (episode 091 transcript), 2025-10-22
> Raw: [POD256 episode 091 transcript](../../raw/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-22-e091.md)
> Updated: 2026-10-07

## Overview

Episode 091 was published on 2025-10-22 and runs 01:41:51. eco hosts with Skot and Tyler. The source is the publisher's machine transcript, so names and terms are often misspelled and speakers are not labelled. The episode opens with Skot's account of two attempts to register the Bitaxe trademark in the United States and his formal opposition. It then moves to Tyler's immersion heating tests and the control problem in hashrate heating, a Libre Board status update, the first Hydrapool release on GitHub, the difference between ESP-Miner and Mujina, a work-distribution problem Ryan found, asic-rs, and a project to put a Bitaxe in orbit.

## Topics in order

### The Bitaxe trademark [00:00:06]

Skot's account:

- Two different Chinese parties are trying to register the Bitaxe trademark in the United States.
- Bitaxe has been used as a trademark for over two years, but Skot never registered it with the US Patent and Trademark Office because he dislikes bureaucracy.
- An applicant must sign under penalty of perjury that the mark is theirs. Skot says these applicants lied.
- The applications are still pending. Skot understands that a trademark is approved unless someone opposes it.
- He now has a lawyer and has formally opposed the applications. He has also applied for the trademark himself [00:03:12].
- He would have preferred a public domain trademark, which does not exist. He does not want people to have to trust him not to issue takedowns, but he does not want someone else to be able to take down sellers or the GitHub repository.
- The lawyers' first step is to contact the applicants' US lawyers and ask them to withdraw [00:08:14]. Skot says he has good evidence of years of use.
- Elsewhere: he says Bitaxe trademarks have been approved in China to someone else, in Germany to a friendly organization he is in contact with, and that someone holds one in the UK [00:06:25].
- He admits people warned him early and he should have listened.

Skot explains that open-source licences are copyright tools and do not cover trademarks [00:10:30]. He stays committed to copyleft open hardware and calls it uncharted territory.

### Immersion heating and the control problem [00:14:13]

Tyler is in the basement of the space beside the radiant floor plumbing. He swapped the M64 that had been heating the floor for a Fog Hashing C2 immersion tank holding two S19 or S21 class miners. The system is going to a customer with all-electric heat.

- The miners run Braiins OS with fans off, using its dynamic performance scaling as a fail-safe that walks power down as temperatures rise [00:15:51].
- The tank, dry cooler and miners are separate control loops that do not know about each other. Tyler calls it janky. The dry cooler bleeds off excess heat to protect the miners, which is waste when the goal is heating.
- He keeps the miner cooling loop and the building heating loop apart with a heat exchanger. A friend who ran domestic water through a water block got corrosion [00:23:32].
- A water heater is hard because it is a closed loop: as the tank warms, the miner must be walked down. Tyler thinks a few Ember One boards with Libre Board and Mujina could make a proper mining water heater [00:22:01].
- His conclusion is that control is best done in software, with a thermostat talking to the miner, and that this is what Mujina and Libre Board are needed for [00:18:25].

### Thermostats and a Libre Board thermostat idea [00:26:13]

Tyler has found that thermostat makers are closing their APIs or requiring developer accounts, and that not all APIs let you run only the furnace fan. Skot explains that household thermostat wires are almost always dry contacts on 24 volts AC, and that powering a smart thermostat from them is the hard part. Tyler proposes a Libre Board based thermostat that drives the furnace blower through those wires and talks to the miner in software. Skot says the Libre Board is not a low power device, so a small separate accessory on the wall is more likely, with the Libre Board at the furnace able to supply it constant power.

### Libre Board status [00:33:16]

eco says the Libre Board design may be finalized as early as this week, or next week since Schnitzel is travelling. This is the first design for the prototyping phase; prototypes must then be built and validated.

Skot explains impedance-controlled traces. High speed differential signals need matched traces. On the Libre Board this matters most for the PCIe connection, which must support whatever people attach, such as NVMe storage. The designer length-matches the pairs and the PCB maker adjusts trace width to hit the target impedance, for a small extra cost [00:34:17].

The Libre Board is line powered, at 12 to 17 volts and potentially 100 watts, and is not designed for low power [00:37:58].

### Getting started, docs and Hydrapool release [00:39:45]

- eco has a list of people interested in Ember One boards, mostly developers. He has not taken money from anyone. Heat sink, fan and power supply recommendations are still to be worked out.
- Each project's GitHub repo is the first source of information. eco also plans a website per project with step by step guides [00:41:46].
- eco says Jungly has technically done the first Hydrapool release on GitHub. The two stepped through it that morning and found a couple of bugs to fix [00:42:56].
- eco will start a video series called "assembling freedom" showing his work in the shop: KiCad, ordering PCBs and parts, and running the pick and place machine [00:44:00].

### Why the Bitaxe matters, and making money on open source [00:46:41]

eco answers the usual criticisms of the Bitaxe (low hashrate, high cost per terahash, chips taken from working miners): it is the necessary first step, because everything had to be reverse engineered. Skot stresses that taking part is not a vow of poverty. Companies can build and sell on this stack, and some already profit. Tyler argues heat reuse has not scaled because miners are proprietary and built for data centers, and he criticizes large district heating operations as ordinary mining sites that never feel that pain [00:53:27].

### ESP-Miner, Mujina and bitaxe-raw [00:56:08]

Skot's explanation for Tyler:

- ESP-Miner runs bare metal on the Bitaxe's ESP32, a cheap Wi-Fi microcontroller that cannot run Linux.
- Mujina is called firmware but is an application that can be built and run on a desktop computer. It cannot run on the ESP32. It targets larger systems with more hash boards and more integration.
- bitaxe-raw, written by a community member, replaces ESP-Miner on a Bitaxe and passes the ASIC and board peripherals straight through over USB. The Bitaxe then behaves like a dumb hash board, much as the Ember One will [00:59:20].
- eco adds that Ryan's first try overheated at once, because with bitaxe-raw the host must run the fan.

### Work distribution problems Ryan found [01:01:38]

- eco relays that above roughly 260 or 280 terahash on Stratum v2, work cannot be split across that many chips without duplication, because the chips roll through the available bits too fast. He says it is easy to fix in several ways. Ryan is weighing whether to fix it now or ship first for the smaller devices.
- Skot's view: Stratum v1 templates leave the miner a lot of extranonce space to roll. He thinks a Stratum v2 mode where the pool does that rolling could be the bottleneck. He has not yet replied to Ryan.
- Intel chips differ from Bitmain chips [01:05:27]. Bitmain chips take a broadcast job and divide it themselves. With the Intel chips the firmware must address each engine in each chip. eco says a 12 chip Ember One design would need about 3,000 separate work orders. His worry is CPU load on the host.
- Skot has two miners with hundreds of BZM2 chips that work, so it can be done. He notes the chips use time division multiplexing and default to five megabaud serial, which has been a trouble spot.

### asic-rs and pyasic [01:09:07]

Brett's pyasic collects the manufacturers' differing, poorly documented miner APIs under one interface. asic-rs is the Rust version. Brett asked to host both under the 256 Foundation organization on GitHub. pyasic has been added to PyPI and asic-rs to crates.io [01:14:52]. Skot separates the two layers: Stratum carries the mining work, and the API is everything else. Mujina will have its own well documented, extensible API [01:12:50].

### Bitaxe auto-tuning [01:16:27]

A member of Tyler's space wrote a script that retunes his Bitaxe every thirty seconds and reports doubled shares. Skot is cautious: fan speed and voltage are easy to change live, but frequency must be ramped. More shares per minute may only reflect the pool's difficulty adjustment restarting, not more hashrate.

### Hashers and hardestblocks.org [01:23:01]

After the shout-outs, the hosts look at hardestblocks.org, which ranks blocks by the difficulty of the winning share. The top entry shown is 50.54 e at block 756,951, with the next at 18.7 e.

### A Bitaxe in space [01:32:58]

Skot spoke at TABConf with Bob McElrath, who is working with a team seriously pursuing a launch of a Bitaxe into low earth orbit, under the name dyson-labs.com. Skot says it is not a practical place to mine but is worth doing as a platform, and that an open design makes the needed changes possible. Tyler, who used to work in aerospace, explains radiative cooling and the need for heaters on shaded electronics. The team is looking for investors and partners.

## Notable claims and decisions

- Skot has formally opposed two US applications for the Bitaxe trademark and filed his own.
- Libre Board's first prototype design is days from final.
- A first Hydrapool release is on GitHub, with known bugs being fixed.
- pyasic and asic-rs are hosted under the foundation's GitHub organization.
- Mujina will define its own documented API.

## See Also

- [POD256 Episode Guide: 2025](episode-guide-2025.md)
- [Open-Source Mining Stack Coverage on POD256](open-source-mining-stack-coverage.md)
- [Home Mining and Heat Reuse on POD256](home-mining-and-heat-reuse.md)
- [Bitaxe and Open Source Miners United](../ecosystem/bitaxe-and-osmu.md)
- [AxeOS / ESP-Miner Firmware](../ecosystem/axeos-esp-miner-firmware.md)
- [Open Mining Tools and Bitaxe Accessories](../ecosystem/tools-and-accessories.md)
- [Intel BZM2 Designs: BIRDS and Bonanza](../ecosystem/intel-bzm2-designs.md)
- [Libre Board](../hardware/libre-board.md)
- [Libre Board Design and Grant Scope](../hardware/libre-board-design.md)
- [Ember One](../hardware/ember-one.md)
- [Mujina Firmware](../mujina/mujina-firmware.md)
- [Hydrapool](../hydrapool/hydrapool.md)
- [asic-rs](../tools/asic-rs.md)
- [RHAP: Raw Hardware Access Protocol](../protocols/rhap.md)
