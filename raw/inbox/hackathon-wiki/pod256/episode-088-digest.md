# POD256 Episode 088: Freedom Tech in Action: Open Miners, Sovereign Homes, and the Post-ImagineIF Debrief

> Sources: POD256 (episode 088 transcript), 2025-09-24
> Raw: [POD256 episode 088 transcript](../../raw/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-24-e088.md)
> Updated: 2026-10-07

## Overview

Episode 088 was published on 2025-09-24 and runs 00:55:04. Rod is back after a month away organizing ImagineIF, and joins eco, Skot and Tyler; Jack helps produce in the background. The source is the publisher's machine transcript, so names and terms are often misspelled and speakers are not labelled. The first half is a debrief of ImagineIF and a talk about public miners moving to AI and HPC. The second half carries the project news: the Telehash date, Libre Board prototypes about to be ordered, an early look at Ember One v5, Hydrapool expected in October, a new tier one supporter, and the statement that Bitaxe will become an official project of the foundation.

## Topics in order

### ImagineIF debrief [00:03:26]

Rod thanks the three for taking part and says the event drew over 500 people plus a livestream audience. Each host sums up his part [00:08:00]:

- eco's talk was called "Freedom Tech is Fundamental to a Free Society". His message was to support open-source developers, because without them there is no freedom tech.
- Tyler's talk was titled "Sovereign Smart Home". His thesis is that a Bitcoin miner belongs in the home as a box that monetizes excess energy and gives supplemental heat, and that running one leads people on to nodes and other open tools.
- Skot was on a panel on innovating in Bitcoin mining. His angle was that it must be open source. Philip Walton of Gridless joined the panel at short notice.

### Telehash announced [00:11:25]

Rod announces the next Telehash for Wednesday, January 21 in Nashville, Tennessee. The Nashville Energy and Mining Summit follows on the next two days. Telehash will be open as a free meetup for people who cannot get a NEMS ticket. Rod expects Ryan and Schnitzel to attend and is not sure about Jungly. He notes that it will be about a year since the foundation mined its block, and that the event is a chance to show what was done with it. He is working on hashrate commitments.

### State of the network [00:13:47]

| Measure | As spoken |
|---|---|
| Block height | 916222 |
| Hash price | 51 US dollars per petahash |
| Hash value | 40,000 sats per petahash per day |
| S21 XP price quoted | $5,600 for 270 terahash |
| Next halving | nine hundred and eleven days away |

The one week hashrate is transcribed as "1.09 per second" with the unit lost; the hosts treat it as the milestone they had made bets about. One host observes that the Bitcoin price is about where it began the year while hashrate is 30% higher. A solo calculator gives 270 terahash an expected seventy three years to find a block [00:15:54].

### Public miners and HPC [00:17:25]

The hosts discuss a claim that investors are pushing large public miners toward AI and HPC. Rod agrees: a miner that holds power contracts can get a guaranteed margin from a compute customer, which is easier than mining alone on a fixed electricity cost. One host says to let them go and leave room for dedicated miners. A related prediction is mentioned that hashrate might fall as large miners switch.

A stretch on treasury companies and the state of Bitcoin Twitter follows [00:23:38].

### Foundation project updates [00:32:29]

**Libre Board.** Just before the show the team livestreamed a schematic review with Schnitzel. eco says they are probably ready to order prototype PCBs and components as early as next week, more likely the week after. The first run is just five units, to see whether the design works at all. The files will be on GitHub, but eco advises others to wait because revisions are likely.

**Ember One v5.** Skot shared early pictures the night before [00:33:35]. He has upgraded the voltage regulator, which removes many components and cleans up the board. The new regulator allows power monitoring and lets the board cut 100% of the power to the chips on demand. Skot explains why that matters: for heating and other uses you want very low draw when not mining. Adding a fan controller is still undecided.

**Ember One v4 and Mujina.** Skot built v4 by hand and validated it, then shipped it to Ryan. Ryan is preparing the firmware so it is ready when the first batch of Ember Ones is produced [00:36:15].

**Hydrapool.** eco calls it right on track and expects something people can pull from GitHub and deploy in October [00:36:46]. Jungly has the PPLNS payout, the share accounting and the difficulty adjustment working. There will be many user-configurable options. The foundation will probably run a hosted instance for testing, but eco stresses it is not in the business of operating a pool.

### Miners who care about energy [00:38:55]

Tyler reports from a University of Wyoming event where mine operators on stage were asked what excites them about open-source miners and firmware. He says none answered. He passes on a distinction from Philip Walton: on-grid miners running flat out care about hashrate, while off-grid operators, home miners and heat reusers care about energy.

### Home miner of the week [00:42:19]

A member of the Open Source Miners United chat posted a rack of about 15 hydro-cooled Bitaxes with custom water blocks, power supplies, two large batteries, a solar charge controller and industrial PLCs, plus his own interface showing hashrate, temperature and best difficulty for each unit. The chip temperatures shown are around 39 C. Skot says there is some evidence the chips run better warmer, in the 50 to 60 degrees Celsius range, though Bitmain publishes no data on this.

### Supporters and Bitaxe [00:50:02]

- HRF and OpenSats are thanked for continued support.
- Open Source Miner, described as the person behind Public Pool, is now a tier one supporter of the foundation.
- eco states that the foundation stands behind Skot, Public Pool and OSMU despite recent drama.
- eco says the foundation will partner with OSMU and make Bitaxe an official project of the foundation, with more to come [00:51:35].

Hasher shout-outs close the show [00:52:09].

## Notable claims and decisions

- Telehash is set for Wednesday, January 21 in Nashville, the day before NEMS.
- Libre Board moves to a first prototype run of five units.
- Ember One v5 gets a new regulator with power monitoring and a full power cut to the chips.
- Hydrapool is to be self-hosted by users; the foundation will not operate a pool as a business.
- Bitaxe is to become an official foundation project.

## See Also

- [POD256 Episode Guide: 2025](episode-guide-2025.md)
- [Open-Source Mining Stack Coverage on POD256](open-source-mining-stack-coverage.md)
- [Home Mining and Heat Reuse on POD256](home-mining-and-heat-reuse.md)
- [Libre Board](../hardware/libre-board.md)
- [Ember One](../hardware/ember-one.md)
- [Mujina Firmware](../mujina/mujina-firmware.md)
- [Hydrapool](../hydrapool/hydrapool.md)
- [Bitaxe and Open Source Miners United](../ecosystem/bitaxe-and-osmu.md)
- [Public Pool](../ecosystem/public-pool.md)
- [Telehash](../foundation/telehash.md)
- [Grants and Funding](../foundation/grants-and-funding.md)
