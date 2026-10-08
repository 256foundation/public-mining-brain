# POD256 Episode 087: Heat, Hash, and Hardware Freedom: Live at Bitcoin Park

> Sources: POD256 (episode 087 transcript), 2025-09-17
> Raw: [POD256 episode 087 transcript](../../raw/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-17-e087.md)
> Updated: 2026-10-07

## Overview

Episode 087 was published on 2025-09-17 and runs 01:29:09. It was recorded in the studio at Bitcoin Park in Nashville during the Bitcoin custody and treasury summit, two days before the ImagineIF conference. eco hosts with Ryan, the Mujina developer, in the room; Skot and Tyler join remotely. The source is the publisher's machine transcript, so names and terms are often misspelled and speakers are not labelled. This is the most Mujina-heavy episode of the autumn: Ryan describes his development setup, the first Ember One v4 arriving, the PMBus driver, and the launch plan that ties Mujina's public release to the first batch of Ember One boards. The episode also covers Hydrapool's planned share-audit API.

## Topics in order

### Opening and the Bitaxe origin story [00:00:03]

The hosts joke about installing a permanent mining-heated hot tub at the park. The M64 that was rigged to the hot tub at NEMS is described as going up to 5,000 watts and 228 terahash.

Skot retells how the Bitaxe started [00:04:12]. He wanted to build his own ASIC miner and assumed an open design existed. He found nothing except one old blog post by someone who had begun reverse engineering the chip in the Antminer S1. That post showed him the chips take serial data and block headers. He adds that he had lots of help.

### Buying miners as an individual [00:06:22]

Tyler says people who want one or two machines to heat a house have no clear place to buy. The process runs through chat apps and is full of scammers. Manufacturers sell direct, but are set up for commercial orders.

### Node sync speed [00:09:12]

A side discussion on initial block download. One host says a sync on a Raspberry Pi 4 took about four days when he first wrote it up and over two weeks earlier this year. Skot passes on an unverified idea from a core developer that a cryptographic function used in validation is not using the Pi 4 processor's hardware acceleration.

### Dummy work for off-grid miners [00:17:40]

Gridless is described as running miners that act as a balancing load on small grids. If the internet drops, the miners must keep drawing power, so they fall back to a fake pool. Ryan says hearing Gridless describe this at the first NEMS was the first spark for his firmware work: it should be solved in software by letting the miner hash dummy work [00:18:42]. Skot adds that the chips start hashing on their own once enabled; it is the firmware that turns them off when no jobs arrive. With Mujina the owner can choose the behaviour.

### Mujina update [00:22:38]

- Ryan received the very first Ember One v4 from Skot on Monday night. He has not powered it yet because he was packing for Nashville, and he wants to watch it in person before trusting it remotely.
- His bench is fully remote-controllable: power supplies, a logic analyzer and USB relays wired across switches, driven by his own Python scripts. He can switch a Bitaxe between bitaxe-raw and the normal firmware with one script [00:24:15].
- While waiting for the Ember One he has used a Bitaxe Gamma as a hash board, with special firmware that passes it through to Mujina so it behaves like an Ember One [00:30:05].
- He wrote the driver for the Gamma's power controller and kept it abstract. He describes it as basically a PMBus driver that should work with other PMBus parts with little change.

### Ember One power and v4.1 [00:29:01]

- Skot plans a more advanced voltage regulator with PMBus monitoring for the next Ember One. The Libre Board regulator is in the same series.
- The current Ember One lacks PMBus because it was hard to find a regulator for the 24 volt input. Ember One boards have a microcontroller that connects over USB, plus temperature sensors; v4 has an external I2C sensor near the regulator.
- There is now a v4.1 tag on the Ember One project [00:34:24]. It is a release candidate with a tiny bug fix and no functional change. Before the release, the team wants to build one and test the over-voltage protection circuit by trying to fry the board. Zach contributed that circuit. Only one working v4 exists, so Skot did not want to sacrifice it.
- Power supply choice is left to the builder. Each Ember One is about 100 watts. Skot estimates under one watt per board when on but disabled [00:37:12].

### Fans, spoofers and system-level control [00:40:22]

The hosts criticize hacks that exist only because stock firmware is closed: fan spoofers, and boards that fake power supply messages. Ryan says system-level issues such as a shared fan are something Mujina has not addressed yet. On a Bitaxe the fan is on the board and Mujina monitors and controls it. The Ember One fan is a system fan, and for now Mujina does not control it [00:43:33].

A right-to-repair digression follows [00:44:37].

### Mujina on other miners [00:48:19]

- eco wants Tyler's heated floor at the space, now run by a Whatsminer, to run on open software. Epic has reverse engineered the Whatsminer protocol, and an open-source effort out of Kenya is said to be working on the same thing.
- Ryan restates the order of work: Ember One first, then the Intel-chip Ember One, with industrial miners "down the list a little bit" [00:51:59].
- Skot rejects the claim that firmware must start from scratch for each new chip. Stratum, work generation, the dashboard, fans and power supply control do not change with the chip [00:52:29].
- Skot thinks stock Bitmain hash boards are not far off, because the first Ember One uses Bitmain chips [01:02:53]. He wants Mujina running on a J Pro hash board soon.

The hosts also respond to a critical thread about the Proto Rig [00:53:32] and argue that home miner makers should open-source their home products [00:58:29].

### Launch plan [01:04:28]

This is the key decision of the episode:

1. eco will build one Ember One, and he and Skot will try to fry it.
2. If that goes well, eco will order materials for about 100 boards.
3. Ryan's deadline is the day those boards ship. Mujina must work with the Ember One by then.
4. That day is the public release of Mujina. The GitHub repo is private for now, until the foundation of the code is in place.

Ryan guesses this is a month or two away. On day one Mujina will support two boards: the Ember One and the Bitaxe Gamma used as a hash board, including several Gammas at once [01:06:37].

### Adapter board and a protocol name [01:07:42]

Skot describes a tiny board that plugs into the data connector of a Bitmain hash board and gives it a USB port. It uses the same microcontroller and firmware as the Ember One, with an I2C control channel. Any USB host can then drive the board, including a Libre Board or a Raspberry Pi. Ryan says the hash board protocol needs its own name and specification. Skot has been calling it Bitaxe Raw. He notes the Intel chips need nine bit serial, so some options will be required [01:08:46].

### Open pools and share auditing [01:10:20]

- Someone reverse engineered the DATUM protocol and published a first-pass server that a stock DATUM client can talk to instead of Ocean's servers. Skot repeats that Ocean's server software is not open source.
- The stated aim for Hydrapool is to remove developer skill as a requirement for starting a pool [01:12:30].
- Hydrapool will open an API endpoint so anyone can watch the pool validate shares, log them and build their own database to hold the operator accountable [01:15:07].
- The design choice is to expose the live validation stream rather than make the server store long share histories. Some persistence is still needed so workers do not lose shares on a restart [01:17:48].
- Ryan suggests Mujina could log accepted shares in a standard format that matches the pool's API, so a miner can compare its own ledger with the pool's [01:15:44]. Skot notes no existing firmware lets you audit shares sent and at what difficulty.
- P2Pool is named as the longer-term answer.

### Hashers and ImagineIF [01:22:45]

Worker names on several pools are read out. eco and Tyler are preparing ten minute talks for ImagineIF; Skot is on a panel.

## Notable claims and decisions

- Mujina's public release is tied to the first Ember One production batch.
- Mujina will launch with support for the Ember One and the Bitaxe Gamma.
- Ember One v4.1 is a release candidate pending a destructive over-voltage test.
- Hydrapool will offer a share-audit API endpoint.

## See Also

- [POD256 Episode Guide: 2025](episode-guide-2025.md)
- [Open-Source Mining Stack Coverage on POD256](open-source-mining-stack-coverage.md)
- [Mujina Firmware](../mujina/mujina-firmware.md)
- [Mujina Hardware Compatibility](../mujina/hardware-compatibility.md)
- [Ember One](../hardware/ember-one.md)
- [Ember One Hardware Details](../hardware/ember-one-hardware.md)
- [Libre Board](../hardware/libre-board.md)
- [Hydrapool](../hydrapool/hydrapool.md)
- [RHAP: Raw Hardware Access Protocol](../protocols/rhap.md)
- [Bitaxe and Open Source Miners United](../ecosystem/bitaxe-and-osmu.md)
- [Home Mining and Heat Reuse on POD256](home-mining-and-heat-reuse.md)
