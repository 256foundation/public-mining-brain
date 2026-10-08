# POD256 Episode 089: Copyleft and Cold Rooms: Open Hardware, Passive Heat, and Economic Nodes

> Sources: POD256 (episode 089 transcript), 2025-10-05
> Raw: [POD256 episode 089 transcript](../../raw/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-05-e089.md)
> Updated: 2026-10-07

## Overview

Episode 089 was published on 2025-10-05 and runs 01:09:02. Only Skot and Tyler are on it; eco and Rod are away. The source is the publisher's machine transcript, so names and terms are often misspelled and speakers are not labelled. With two voices, most of the hardware answers are plainly Skot's and most of the questions Tyler's. The episode is the fullest account of the Ember One v5 design decisions, followed by ideas for fanless heaters, IPv6 on the Bitaxe, the Bitcoin Core and Knots policy dispute, and a long explanation of copyleft and the open hardware licence the foundation uses.

## Topics in order

### Ember One v5 design [00:00:39]

Skot wrapped up v5 late the previous week and sent the design to eco.

- **Fan control.** Ryan is running a v4 on his desk over USB with the fan hardwired to the 12 volt input at full speed, and asked for a fan controller. Skot declined to build one in, because the Ember One is a reference hash board with no single target system. Users may run it alone, in immersion, on water blocks, or several together with a separate fan controller. The compromise: spare controller pins, plus power and ground, are broken out to a header so a small daughter board can add fan control [00:02:24]. Skot also drew such a daughter board and posted it on his own GitHub.
- **Voltage regulator.** This is the big change [00:03:35]. The new part is more modern, uses smaller inductors, and reports its temperature digitally. It can be programmed to shut off the output on over-temperature, and it monitors input voltage, output voltage and output current.
- **Why a regulator at all.** Large Antminers have no regulator on the hash board; the power supply output feeds chains of chips in series. The Ember One has 12 chips, which in series only reach 3.6 volts, so the input must be stepped down at high current [00:04:52].
- **Input voltage.** v5 no longer accepts 24 volts. The maximum is now 17. Skot calls this a concession to the newer regulators. Someone who wants a higher supply voltage can use an external regulator [00:10:39].
- **Status.** v5 is not validated yet, but the design is already posted on the 256 Foundation GitHub. eco will build boards at Bitcoin Park so the design can be validated and then released [00:09:37].

Skot contrasts this with stock hash boards that have no over-current protection and can burn while the power supply keeps feeding them.

### Building systems from Ember Ones [00:13:42]

- The Ember One happens to be the same height as an S9 hash board, so it slides into an S9 chassis. Skot says six will fit, and the S9 power supply can be reused.
- One Libre Board drives four hash boards. Because the boards are USB, a hub can add more, limited by USB and by bandwidth [00:14:54].
- Tyler imagines a wall-mounted, fanless stack with large heat sinks acting as a radiator. Skot thinks a fanless design could work if convection is set up right, with firmware that protects the chips and holds a room temperature [00:16:01].
- A plain dry contact thermostat could be wired straight to the control board and read by the software there [00:18:07].
- Combined with hashing dummy work when the network is down, the result is a heater that still works offline.

### IPv6 on the Bitaxe [00:19:50]

An OSMU member (the name is garbled in the transcript) started work on native IPv6 support for the Bitaxe. Skot explains IPv4 address scarcity, dynamic addresses and dynamic DNS for Tyler. He says adding support looks easier than testing it, since a real test needs the whole network path to support IPv6.

### Bitcoin Core, Knots and mempool policy [00:29:43]

Skot summarizes the dispute and says it is outside his core skill set:

- Core proposed changes to relay and mempool policy, both defaults and function. Knots reverts those changes and makes the settings more configurable.
- A proposed BIP would let a node define its mempool policy with a small script. Skot liked the idea.
- His main objection to Core is that it is removing knobs, not just changing defaults [00:34:58].
- Tyler argues that defaults are where the power sits, since few people change them.

They then separate economic nodes, which are connected to miners or wallets, from nodes that only hold a copy of the ledger [00:38:07]. Skot still wants more people to run any node, because it lowers the barrier to becoming an economic one. Tyler's view is that people will get a miner first, for heat, and then a node to go with it. He says the space's DATUM gateway has about 120 workers [00:41:28].

### TABConf [00:41:28]

TABConf is about two weeks away in Atlanta. Skot says he and Ryan plan a talk on what the foundation is working on, and that the Bitaxe table from last year will be stepped up.

### Does open source pay [00:44:00]

Tyler asks whether any large company grew by backing open source from the start. Skot's points:

- There are few good hardware examples; in software there are many.
- A proprietary SaaS model is a high time preference choice. It is hard for a closed product to compete once a free and open one exists.
- Reference designs are the clearest case. Chip makers outside Bitcoin all publish them because they only gain when more people understand their parts [00:49:22].
- The first push of the Bitaxe to GitHub under that name was May 2022. Skot did not have to write all the firmware or build the UI; others turned up and contributed [00:47:46].
- A good idea gets copied whether or not it is open, so a closed design loses the community's help and is cloned anyway [00:52:36].

Tyler is less sure that opening a whole product built from off-the-shelf parts adds much value.

### Copyleft and the open hardware licence [00:54:21]

Skot's explanation:

- MIT is permissive: a closed version can be made and distributed, with credit given.
- Copyleft requires that anything built from the source is published under the same licence. The aim is to pass on the freedoms to inspect, understand, modify and distribute to every later user.
- Bitaxe and the hardware coming out of the 256 Foundation use a copyleft licence, the open hardware licence, which tries to do for hardware what the GPL does for software [01:00:17].
- That licence requires source in the preferred format for making modifications. Skot says a PDF of a schematic does not qualify, nor do Gerbers. It means the actual CAD files for schematic and layout [01:01:20].
- He argues the CAD tool should itself be open, and names KiCad.
- On who decides what is a violation: the copyright holders are everyone who contributed, but in practice it comes down to lawyers [01:04:23]. He cites a past lawsuit that forced a router maker to release Linux-based firmware, which he credits with starting OpenWrt.

Tyler notes the counter-view: if enforcement needs the state, some will prefer MIT.

## Notable claims and decisions

- Ember One v5: new regulator with digital monitoring and programmable shutdown, a header for an optional fan daughter board, and a lower maximum input of 17 volts.
- v5 design files are public before validation.
- One Libre Board supports four hash boards directly.
- The foundation's hardware is under a copyleft open hardware licence, and source must be editable CAD files.

## See Also

- [POD256 Episode Guide: 2025](episode-guide-2025.md)
- [Open-Source Mining Stack Coverage on POD256](open-source-mining-stack-coverage.md)
- [Home Mining and Heat Reuse on POD256](home-mining-and-heat-reuse.md)
- [Ember One](../hardware/ember-one.md)
- [Ember One Hardware Details](../hardware/ember-one-hardware.md)
- [Libre Board](../hardware/libre-board.md)
- [Mujina Firmware](../mujina/mujina-firmware.md)
- [Bitaxe and Open Source Miners United](../ecosystem/bitaxe-and-osmu.md)
- [AxeOS / ESP-Miner Firmware](../ecosystem/axeos-esp-miner-firmware.md)
- [Editorial Essays and Arguments, 2025](../newsletter/editorial-essays-2025.md)
