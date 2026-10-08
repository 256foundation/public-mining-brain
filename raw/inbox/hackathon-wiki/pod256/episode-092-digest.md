# POD256 Episode 092: Hashrate at Home: Zigbee Thermostats, Bitaxe Wins, and Dockerized Pools

> Sources: POD256 (episode 092 transcript), 2025-10-29
> Raw: [POD256 episode 092 transcript](../../raw/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-29-e092.md)
> Updated: 2026-10-07

## Overview

Episode 092 was published on 2025-10-29 and runs 02:15:16, the longest of this run. eco, Skot and Tyler are on it. The source is the publisher's machine transcript, so names and terms are often misspelled and speakers are not labelled. Much of the episode is about home mining and self-hosting: Tyler's Home Assistant work with Canaan home miners, Zigbee sensors, RISC-V, and a long privacy segment. The project news is a public Hydrapool test instance and the decision to ship Hydrapool as Docker containers, Libre Board prototype boards about to be ordered, a parts shipment destroyed at customs, and the plan to show all four projects working together at the January Telehash and NEMS.

## Topics in order

### Forbes and heat reuse [00:02:12]

Tyler was interviewed for a Forbes article that featured several Heatpunk projects, including a MintGreen proposal in Vancouver to heat a community pool. The hosts were glad it also raised Bitmain's dominance and its lack of heat reuse products, in contrast with Canaan. Tyler passes on a second-hand claim that home mining is about a third of Canaan's revenue; Skot asks whether that means a third of the company or of its mining arm, and no one knows [00:05:04].

> **Status: Disputed**
> In this episode a host relays that home mining is about a third of Canaan's revenue. In [episode 086](episode-086-digest.md) a host said the Avalon Home series had gone from one percent to four percent of revenue. Both are second-hand remarks made seven weeks apart, and neither transcript gives a source document.

A rumour about Bitmain is also aired: that its burn-in period for new machines lasts as long as it takes to earn back the build cost [00:06:47]. The hosts present it as hearsay.

eco and Tyler met a video producer at an HRF event who is making a short film on mining centralization, Antbleed and ASICBoost, with their help [00:08:28].

### Canaan home miners in Home Assistant [00:10:33]

- Canaan publishes API documentation for its home miners: the Avalon Q, the Mini 3 and the Nano.
- Schnitzel's hass-miner plug-in, built on pyasic, normally makes setup a matter of entering an IP address. The Canaan units are not fully supported, and Tyler found a unit error in the Mini 3's maximum hashrate that he means to report.
- Dylan, Tyler's cofounder at Exergy, built the control flows in Node-RED instead, and they documented the method for people who do not write code [00:12:36].
- The Mini 3's intake sensor sits inches from its exhaust, so they tied the heater to a Zigbee temperature sensor on the far side of the room [00:14:41].
- Other automations pull in solar output, time-of-use pricing, hash price and hash value, and run the miner only when mining is free.
- Tyler says the space has about 500 terahash possible online.

Tyler shows the hub they use: a Raspberry Pi 5 with an NVMe expansion board and a Zigbee antenna [00:18:35]. Skot explains ISM bands and mesh networking. He notes that Espressif's new C6 chip supports Zigbee and 5 gigahertz Wi-Fi and has a RISC-V core [00:24:47].

### RISC-V and the Libre Board [00:25:17]

Skot explains RISC-V as an open processor standard that anyone can build without a licence, unlike x86 or ARM. eco ties it to a common criticism of open Bitcoin hardware that relies on closed processors and binary blobs. The Libre Board uses a standard compute module connector, so a user can fit a RISC-V, x86 or ARM module without changing the board. eco says Skot raised this from day one [00:31:05].

### Libre Board status and the customs loss [00:33:12]

- Schnitzel has been travelling, but the PCB designs are very close to going to the manufacturer for prototype boards. eco expects that this week.
- One of eco's boxes of surface mount components was destroyed by customs. A form declaring steel, aluminum or copper content was missing, the shipper did not respond, and the box was destroyed. Skot suspects the shipper used the wrong tariff code.
- The supplier refunded most of the order but not about $90 in reel fees and taxes. eco has paused orders with them until that is settled. Skot suggests buying from a US distributor even at higher cost [00:41:50].
- eco calls it a minor setback. He now expects the hardware to be produced around the Telehash in January, with Mujina, Libre Board and Ember One ready then [00:43:25].

### Hydrapool test instance and packaging [00:43:25]

- A test Hydrapool is running at `test.hydropool.org`. eco asks listeners to point miners at it; the port is spoken as "thirty three thirty three". The dashboard on the same site shows the PPLNS split changing as addresses join [02:00:03].
- Hydrapool is always in PPLNS mode. A lone miner on a private instance simply gets all the shares [00:44:27].
- The code is on the 256 Foundation GitHub.
- Packaging decision: Docker. The pool and the dashboard will each be a container. A Debian package was considered and dropped as harder to maintain across many systems [00:47:45].
- eco will write a step by step guide covering a home computer, a rented VPS with a public URL, and building from source.
- The hosts want it packaged for Start9 and Umbrel and call on AverageGary to help.
- The dashboard uses Prometheus as the database and Grafana for display [02:00:35].
- An earlier test server was used to check many Stratum clients, since miners format messages differently. Logs of hardware and firmware versions, with IP addresses removed, were meant to be available to developers [02:08:04].

### Freedom tech at home and privacy advice [00:48:48]

eco describes his new Linux laptop and a trailer rental he walked away from because it required a selfie. The hosts discuss data collection by retailers, cars, doorbell cameras and city camera contracts. eco's starter list for privacy [01:13:18]:

1. Use a password manager with a unique password per account.
2. Move off Google services, for example to a de-Googled Android system.
3. Use an encrypted email provider.
4. Use an encrypted messenger instead of SMS.
5. Self-host what you can, accepting that you become a part-time sysadmin.

### Skot's single-board heater [01:18:03]

Skot built a one-board miner from an S19j Pro hash board in a stealth miner enclosure sent by a community member. It uses a small USB adapter board (transcribed variously as "ADIT" and "AddIt") on the hash board's data connector, a Raspberry Pi, and a Pi accessory board he calls the ant hat to run the fans. The mining software for now is his own small project; he says Mujina will replace it. He plans to use the heat to cure tobacco. He confirms the Ember One demo at an earlier event ran in a very similar way, with the same processor passing data through to the chips [01:21:14].

Tyler mentions plans for a hashrate hot tub party at the Heatpunk Summit [01:22:47]. Later he says tickets for the next summit are on sale [01:58:27].

### Block Open IP, Canaan and the underdogs [01:23:17]

Tyler reads an announcement that Block is launching an Open IP initiative and pledging some patents under it. The hosts welcome it cautiously. Skot's argument: smaller makers cannot beat Bitmain on efficiency for on-grid mining, so they should go after other markets such as heating, where efficiency is not the whole game. Efficiency figures quoted in passing are 18 joules per terahash for Canaan's baseboard unit, 12 for its newly announced A16, and nine for Bitmain's S23 [01:28:44].

### HPC, hashrate and electricity rates [01:29:51]

- An infrastructure supplier told Tyler that AI companies are turning to public miners because few firms can bring large sites online. Electrical gear for HPC is far larger for the same power because of redundancy.
- A cited article says that six weeks after reaching one zettahash the network had added another 100 exahash [01:33:30]. Skot questions the measurement window.
- Tyler floats hashrate growth as a better prosperity measure than GDP; the others push back.
- Tyler's new time-of-use rate makes his Canaan miner profitable outside peak hours [01:40:25].

### Telehash plans [01:43:18]

- d++ is helping with livestream graphics and ideas to make the event interactive, under the nickname "Teledash".
- The Telehash will run on Hydrapool. eco recalls that the May attempt had hiccups on the first iteration and says much has changed since [01:44:26].
- For Telehash and NEMS the plan is to show all four projects together: an Ember One, controlled by a Libre Board, running Mujina, pointed at Hydrapool [02:01:10]. That depends on the parts shipment.

### Soft fork proposal and pool contracts [01:45:27]

The hosts criticize a soft fork proposal linked to Luke Dashjr, mainly for language about legal consequences for those who do not run it. eco repeats an unverified report of legal letters to mining companies. Skot says large public miners have negotiated contracts with their pools, so switching is not simple. eco heard the opposite from one executive. They agree nobody outside knows for sure [01:49:51].

### A NerdQAxe solo block [01:53:28]

A NerdQAxe++ found a block while solo mining on a self-hosted Public Pool. Skot calls it the NerdQAxe's second block and its first solo-mined one, and Public Pool's second block but the first from a small open-source miner. The finder posted about it and said he would pay off his mortgage.

### Hashers and network notes [01:55:41]

After the shout-outs, eco says he has three Bitaxes pointed at the test Hydrapool. Other notes:

- Network hashrate on the one week view is read as 1.12 zettahash [02:01:40].
- Skot thinks the nonce and extranonce patterns on chain hint at which machines found blocks. Any deliberate Bitaxe identifier would have to be opt in [02:06:23].
- Pools see each miner's user agent, hardware and firmware. Skot suggests making the user agent configurable in Mujina or ESP-Miner [02:13:19].
- Public Pool's site lists connected miner types. It showed 72,088 Nerd Miners with a total near one terahash, a figure Skot believes is too high and wants to ask the operator about [02:10:40].

## Notable claims and decisions

- Hydrapool ships as Docker containers, with a public test instance already running.
- Libre Board prototype PCBs go to the manufacturer this week.
- A customs loss pushes the first hardware batch toward January.
- The January Telehash will run on Hydrapool and aims to show the full stack.

## See Also

- [POD256 Episode Guide: 2025](episode-guide-2025.md)
- [Open-Source Mining Stack Coverage on POD256](open-source-mining-stack-coverage.md)
- [Home Mining and Heat Reuse on POD256](home-mining-and-heat-reuse.md)
- [POD256 Episode 086 digest](episode-086-digest.md)
- [Hydrapool](../hydrapool/hydrapool.md)
- [Running Your Own Hydrapool](../hydrapool/running-hydrapool.md)
- [Libre Board](../hardware/libre-board.md)
- [Libre Board Design and Grant Scope](../hardware/libre-board-design.md)
- [Ember One](../hardware/ember-one.md)
- [Mujina Firmware](../mujina/mujina-firmware.md)
- [Telehash](../foundation/telehash.md)
- [Hashrate Heatpunks](../foundation/hashrate-heatpunks.md)
- [The Nerd Miner Family](../ecosystem/nerd-miner-family.md)
- [Public Pool](../ecosystem/public-pool.md)
- [Bitaxe and Open Source Miners United](../ecosystem/bitaxe-and-osmu.md)
- [asic-rs](../tools/asic-rs.md)
