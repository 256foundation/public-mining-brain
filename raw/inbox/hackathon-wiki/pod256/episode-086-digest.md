# POD256 Episode 086: Open Source vs. Closed Source: The Future of Bitcoin Mining

> Sources: POD256 (episode 086 transcript), 2025-09-10
> Raw: [POD256 episode 086 transcript](../../raw/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-10-e086.md)
> Updated: 2026-10-07

## Overview

Episode 086 was published on 2025-09-10 and runs 01:49:34. The voices on it are Skot, eco and Tyler; Rod is away preparing the ImagineIF event. The source is the publisher's machine transcript, so names and terms are often misspelled and speakers are not labelled. The talk moves from firmware developer fees to pool custody, open-source licensing, the Intel chip giveaway, a furnace retrofit with a home miner, and a state of the network rundown. Project news is short but concrete: Mujina will not charge a dev fee, Hydrapool is described as the stratum server piece for P2Pool, the donated Intel chips are all spoken for, and Ember One v4 is validated and close to release.

## Topics in order

### Firmware dev fees [00:00:01]

The episode opens on dev fees in third-party miner firmware. The fee is a share of running time that the miner spends hashing for the firmware maker's pool. The complaint raised is that switching between pools takes time, and that lost time comes out of the owner's share on top of the stated fee. The hosts accept that firmware is hard to build and that makers are justified in charging for it. They contrast the dev-fee model with licence-based pricing, which they say tells the user more plainly what they pay.

They note that the stock firmware could in principle divert hashrate without the owner knowing, and that the only check today is watching network traffic.

### Mujina and voluntary hashrate [00:01:39]

Mujina is named as an open-source alternative that does not charge a dev fee. The plan described, after a talk with Ryan, is to leave an option for users to split some hashrate to the 256 Foundation if they like the firmware. The user will be able to toggle it off and share nothing.

### Proto Fleet, MicroBT and home miners [00:06:57]

The hosts ask how paid firmware and paid fleet software will compete if Proto's Fleet and firmware are open and Mujina is available. A video recorded at a MicroBT site is described: asked about open-source miners and chip access, the answer was no. The same video briefly mentioned a 1.5 kilowatt hydro home miner entering R&D [00:09:07].

One host says Canaan's Avalon Home series used to be 1% of the company's revenue and is now 4% [00:09:40].

> **Status: Disputed**
> This episode puts the Avalon Home series at a low single-digit share of Canaan's revenue. In [episode 092](episode-092-digest.md) a host relays that home mining is about a third of it. Both are second-hand remarks made seven weeks apart, and neither transcript gives a source document.

### Heatbit Maxi [00:11:27]

Heatbit announced that its new miner, the Heatbit Maxi, will be open source. The hosts have no further detail. Its control board is said to run three small hash boards, each of which can be pointed at a different pool. A drawback noted with the current Heatbit: if you point it at your own pool, the app cannot show your rewards.

### DATUM splits and how Ocean pays out [00:14:32]

Tyler describes using DATUM splits at the pool level on heaters installed for friends and family. A small split, "1%, 2%", goes to Exergy so they can see when the heaters run.

This leads to a long critique of Ocean's "non custodial" claim [00:17:17]:

- An earlier pool that tried to pay directly from the coinbase could not fit more than about 16 addresses, a limit that comes from the firmware on Bitmain's miners.
- The hosts say Ocean did not solve that limit. Miners too small to be in the coinbase are paid later from addresses that Ocean or its custodian controls.
- One host says he knows this because he received his own Ocean rewards on chain from such an address.
- Even with unlimited coinbase space, the pool still runs the share accounting, so it still decides who is paid [00:22:32].

Later [00:41:32] the same host says he moved to Ocean because he could not support full pay per share pools any longer, and calls Ocean a great alternative to FPPS. He cites the claim that six miners control 95% of the mining templates.

### P2Pool and Hydrapool [00:23:48]

P2Pool version two is presented as the fix for centralized share accounting. It keeps a share chain separate from the Bitcoin blockchain, and rewards follow each miner's shares in a window of that chain.

Hydrapool is described as the stratum server component for P2Pool [00:28:50]:

- It can run in solo mode, mining to your own address.
- It can run with a PPLNS payout so a group shares a block in proportion to work.
- The goal is for many Hydrapool instances to network with each other on the P2Pool share chain, so that small pools at different spaces work as one.

At this point Tyler reports 12 and a half petahash and 117 workers on the space's DATUM gateway [00:30:27]. The hosts say Ocean's fee goes from 2% to 1% when a miner runs DATUM.

### Why run a Bitaxe, why heat with a miner [00:32:01]

Skot explains a joke post aimed at people who tell Bitaxe owners to buy an S19 instead. The heating case follows: one house was sized at five Avalon Mini 3 units, each said to make about "3,000 sets a day", against a furnace that earns nothing.

### Open source as the standard [00:35:41]

Skot's argument: proprietary operating systems were the standard on web servers until the early two thousands, then large players adopted open source and everyone followed. He expects mining to go the same way. Points made:

- ASIC makers could specialize in chips and leave the rest of the machine to others.
- With open firmware a large miner could make its own changes instead of lobbying Bitmain [00:48:59].
- The foundation uses the GPL. Under it, a miner can modify the code and run it in production without publishing the changes [00:49:37].
- The hosts frame the core issue as the individual's right to inspect, modify and run their own hardware [00:50:45].

### OP_RETURN scare, Lincoin, Parasite Pool, licences [00:36:48]

The hosts dismiss a claim that a virus placed in an OP_RETURN could cripple Bitcoin infrastructure. They note nobody's node crashed, and that a node executing arbitrary data would be a node bug.

Lincoin is in the news for joining a Google for Startups accelerator programme on AI for energy [00:39:29]. A host says he likes the team but calls Lincoin a proxy pool on full pay per share.

Parasite Pool is mentioned as a newer pool that gives a bonus to whoever finds the block, and whose team says it is very close to open-sourcing its server [00:42:34]. The hosts argue that if Ocean is based on Eligius (transcribed as "Allegis"), which was AGPL, the Ocean server should be open too [00:43:37]. Skot explains the difference: the GPL requires releasing changes when you distribute the code, while the AGPL requires it even when you only run it.

### Intel chip donations [00:56:27]

The fullest project update in the episode:

- Proto announced in January that it would give the foundation 256,000 chips.
- From January until about August there were four serious inquiries.
- The chips arrived in four boxes of 54,000 plus a smaller box of extras. The four big boxes went straight to the four interested parties.
- Interest rose sharply after a photo of the chips was posted. All 256,000 chips are now spoken for.
- The foundation plans to get more chips and give them out again.
- Two open designs are coming: Skot's Bitaxe Bonanza, using eight of the Intel chips, and then an Ember One using 12 of them.

### Furnace retrofit with an Avalon Q [01:02:21]

Tyler cut an opening at the furnace filter door and ducted an Avalon Q into the cold air return with cardboard and tape. Only the furnace fan runs; the gas stays off unless the miner cannot keep up. Control is through an ecobee thermostat and Home Assistant. He suggests trying the same with the Libre Board so that the miner switches the circulator fan itself [01:04:15]. He also asked his utility about a winter electric heating programme that would cut his power bill by 50%.

Solar permitting costs, running a house from a natural gas generator, and the history of hydronic heating follow [01:10:14 to 01:31:28].

### Hasher shout-outs [01:15:01]

The hosts read out worker names pointed at the foundation on several pools. They note that episodes eighty four and eighty five are the two nights of the Proto Rig launch livestream.

### State of the network [01:31:58]

Read live from mempool.space, Hashrate Index and Braiins:

| Measure | As spoken |
|---|---|
| Hashrate, one week moving average | 996 exahash, "just shy of" a zettahash |
| Difficulty | adjusted upward after September 4 |
| ASICs under 19 joules per terahash | $13.92 per terahash |
| ASICs under 25 joules per terahash | $7.56 per terahash |
| ASICs under 38 joules per terahash | $3.64 per terahash |
| Hash price | $52.79 per petahash per day |
| Hash value | 49,000 sats per petahash per day before the adjustment, about 46,500 after |

The hosts believe most miners still run stock firmware, partly to keep the warranty [01:35:48].

### Events, supporters and Ember One v4 [01:40:30]

- Telehash number three is planned for the day before NEMS in Nashville in January.
- ImagineIF is the following week in Nashville. Skot and Tyler will attend, and Ryan will be there too.
- Tyler has set a Heatpunk Summit at the space for February.
- Supporters thanked: Proto, HRF and OpenSats at tier one; Heatbit and Foundry at tier two; Rod, eco and Tyler (through Exergy) at tier three, plus two anonymous tier three donations [01:44:41].
- Ember One v4 [01:46:49]: Skot is confident in the validation. A release is coming once two small fixes go in, a BOM change and one wrong footprint. He is mailing a board to Ryan to integrate with Mujina.

## Notable claims and decisions

- Mujina will have no dev fee, only an optional, user-controlled hashrate split to the foundation.
- The foundation's licence choice is the GPL, picked so that large miners can modify privately.
- The first 256,000 donated Intel chips are fully allocated; a second round is intended.
- Hydrapool is positioned as the stratum server for P2Pool, with solo and PPLNS modes.

## See Also

- [POD256 Episode Guide: 2025](episode-guide-2025.md)
- [Open-Source Mining Stack Coverage on POD256](open-source-mining-stack-coverage.md)
- [Home Mining and Heat Reuse on POD256](home-mining-and-heat-reuse.md)
- [POD256 Episode 092 digest](episode-092-digest.md)
- [Mujina Firmware](../mujina/mujina-firmware.md)
- [Hydrapool](../hydrapool/hydrapool.md)
- [Ember One](../hardware/ember-one.md)
- [Libre Board](../hardware/libre-board.md)
- [Intel BZM2 Designs: BIRDS and Bonanza](../ecosystem/intel-bzm2-designs.md)
- [Bitaxe and Open Source Miners United](../ecosystem/bitaxe-and-osmu.md)
- [Telehash](../foundation/telehash.md)
- [Grants and Funding](../foundation/grants-and-funding.md)
- [Hashrate Heatpunks](../foundation/hashrate-heatpunks.md)
