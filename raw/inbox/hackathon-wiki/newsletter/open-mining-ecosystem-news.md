# Open Mining Ecosystem News, 2025 to 2026

> Sources: 256 Foundation (newsletter #5, May 2025), 2025-05-05; 256 Foundation (newsletter #6, June 2025), 2025-06-19; 256 Foundation (newsletter #7, July 2025), 2025-07-15; 256 Foundation (newsletter #8, August 2025), 2025-08-18; 256 Foundation (newsletter #9, September 2025), 2025-09-25; 256 Foundation (Assembling Freedom #10), 2025-10-28; 256 Foundation (Assembling Freedom #11), 2025-11-24; 256 Foundation (Assembling Freedom #12), 2025-12-22; 256 Foundation (Assembling Freedom #13), 2026-01-14; 256 Foundation (Assembling Freedom #14), 2026-01-30; 256 Foundation (POD256 Episode 103 newsletter), 2026-02-05; 256 Foundation (Assembling Freedom #17), 2026-02-19; 256 Foundation (Assembling Freedom #22), 2026-04-05; 256 Foundation (Assembling Freedom #23), 2026-04-11; 256 Foundation (Assembling Freedom #24), 2026-04-15; 256 Foundation (Assembling Freedom #25), 2026-04-22; 256 Foundation (Assembling Freedom #26), 2026-05-13; 256 Foundation (Assembling Freedom #27), 2026-05-28
> Raw: [Newsletter May 2025](../../raw/newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md); [Newsletter June 2025](../../raw/newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md); [Newsletter July 2025](../../raw/newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md); [Newsletter August 2025](../../raw/newsletter/2025-08-18-is-open-source-communism.md); [Newsletter September 2025](../../raw/newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md); [Assembling Freedom #10](../../raw/newsletter/2025-10-28-assembling-freedom-10.md); [Assembling Freedom #11](../../raw/newsletter/2025-11-24-assembling-freedom-11.md); [Assembling Freedom #12](../../raw/newsletter/2025-12-22-assembling-freedom-12.md); [Assembling Freedom #13](../../raw/newsletter/2026-01-14-assembling-freedom-13.md); [Assembling Freedom #14](../../raw/newsletter/2026-01-30-assembling-freedom-14.md); [POD256 Episode 103 newsletter](../../raw/newsletter/2026-02-05-unlocking-decentralized-mining-deep-dive-into-pod256-episode.md); [Assembling Freedom #17](../../raw/newsletter/2026-02-19-assembling-freedom-17-unpacking-pod256-episode-105-chips-cha.md); [Assembling Freedom #22](../../raw/newsletter/2026-04-05-pod256-episode-110-newsletter-april-fools-real-progress-open.md); [Assembling Freedom #23](../../raw/newsletter/2026-04-11-assembling-freedom-23.md); [Assembling Freedom #24](../../raw/newsletter/2026-04-15-assembling-freedom-24-bitcoin-mining-renaissance-stratum-v2.md); [Assembling Freedom #25](../../raw/newsletter/2026-04-22-assembling-freedom-25.md); [Assembling Freedom #26](../../raw/newsletter/2026-05-13-assembling-freedom-26.md); [Assembling Freedom #27](../../raw/newsletter/2026-05-28-assembling-freedom-27.md)
> Updated: 2026-10-07

## Overview

Beyond the foundation's own projects, the newsletter tracked the wider open mining world. This page gathers that news by theme: how concentrated mining pools are, the protocols meant to fix that, solo miners who found blocks, the Bitaxe ecosystem, and what hardware vendors did. Most of the dated items come from the monthly 2025 issues, which had a section for free and open mining developments. The 2026 issues add protocol detail and a few vendor items. Dates without a year are in 2025.

## Pool concentration

- **B10C's analysis (April 15).** Only six pools mine more than 95% of blocks. Between 2019 and 2022 the top two pools held about 35% of hashrate and the top six about 75%. By December 2023 the top two held 55% and the top six about 90%.
- **Antpool and its proxies (June issue).** The newsletter says pools that cannot fund FPPS reserves let Antpool bankroll them and act as proxy pools. It names Poolin, Braiins, Ultimus Pool, Binance Pool, SecPool, SigmaPool, Rawpool, Luxor, CloverPool and Mining Squared. It estimates Antpool with its proxies at roughly 40% of network hashrate. Bitmain itself warned that 58% of hashrate is controlled by two pools.
- **Luxor's template (June 5).** Researcher boerst found Luxor sending out a block template tagged "Mined by AntPool". The templates from the two pools matched exactly, and his shares on it were accepted.
- **Invalid jobs (August 26).** boerst added an events panel to stratum.work. Antpool and others had been seen handing out jobs with empty Merkle branches but a coinbase reward above the subsidy. A block found on such a job would have been invalid. The cause was not established.
- **Foundry.** Issue #14 cites Foundry's 30% share as an example of pool dominance.

The newsletter's reading of these facts is in [Editorial Essays and Arguments, 2025](editorial-essays-2025.md).

## Stratum v2 and other pool protocols

**What Stratum v2 changes.** The newsletters credit it with encrypted connections between miner and pool, a binary format that uses less bandwidth, and the option for miners to run a node and build their own block templates.

- A case study published on June 12 by the Stratum v2 reference implementation team, with Hashlabs and DMND Pool, claims at least 7.4% more profit than Stratum v1. Part of the gain comes from encryption, which blocks hashrate hijacking. Braiins estimates that 1% to 2% of hashrate is being stolen. The study also reports faster block propagation and lower job latency.
- The Stratum v2 website was updated on July 3 with explanations for pools.
- At TabConf, Average Gary described packaging Stratum v2 for Start9 with hole punching, so miners behind home routers can mine peer to peer without a public IP. The idea is to make every meetup a pool.
- Issue #24 (April 2026) goes deeper. Job Negotiation lets miners propose templates that the pool validates but cannot censor. The pool operator still controls the coinbase payout and the share accounting. Header-only mining lets a device work on the block header alone. The issue puts the standard channel search space at about 280 TH per nTime value. The November 2025 issue gives a matching range for where nonce exhaustion begins.
- AxeOS, the Bitaxe firmware, is reported to have native Stratum v2 support. AxeOS also verifies the coinbase to protect against malicious pools.
- BlitzPool has a Stratum v2 solo pool and a non-custodial PPLNS roadmap (issue #25).

**Limits.** The newsletter repeats that template building alone does not decentralize mining while a central pool counts shares and pays out. The podcast compared Stratum v2 with DATUM and preferred Stratum v2 for its open specification and Rust tooling.

**Other designs.**

- **Hashpool.** Explained on a podcast on April 21. The pool issues an ehash token for every share. Tokens accrue value over a maturity window and can then be redeemed at the mint for bitcoin. Payouts resemble PPLNS.
- **P2Pool v2.** Jungly's decentralized pool work, with sharechains and atomic swaps for non-custodial payouts. The plan is for [Hydra Pool](../hydrapool/hydrapool.md) instances to combine work eventually.
- **Solo CK Pool.** On August 4 Con Kolivas released an all-in-one script that makes the pool easy to deploy. The newsletter saw it as confirming the Hydra Pool approach.
- **Public Pool.** On April 27 it patched a flaw that let modified Nerdminer firmware submit each valid share five times and appear to hash five times faster. Scammers had used it to sell fake firmware.
- **GridPool.** Issue #27 mentions its winners list as a way of smoothing variance.

## Solo miners finding blocks

| When | Pool | Miner size | Detail |
|---|---|---|---|
| April 11 | Solo CK Pool | about 230Th/s | Block #891952, worth 3.11 BTC |
| July 3 | Solo CK Pool, EU server | 2.3Ph/s | The pool's 301st block. About a 1 in 2,800 chance per day. |
| July 26 | Solo CK Pool, EU server | 49Th/s | The pool's 303rd block |
| August 17 | Solo CK Pool | 9Ph/s | Height 910,440. The pool's 12th block of the year. |
| September 7 | Solo CK Pool | 200Th/s | The pool's 307th block. About a 1 in 36,000 chance per day. The winning worker was a unit of about 38Th/s. |
| April 2026 | CKPool (two blocks), Public Pool, Node Runners | 18.5 TH/s on Public Pool, 4.8 TH/s on Node Runners | Four solo blocks in a week, including Public Pool's first block on its hosted instance |

The July issue ties block #903883, found by a miner of about 2.3Ph/s on Solo CK Pool in Europe, to the difficulty drop of June 28. The August issue dates what appears to be the same find to July 3.

> **Status: Disputed**
> The odds quoted do not scale with hashrate. The October 2025 issue gives a 200Th/s miner about a 1 in 36,000 chance per day. Issue #23 (April 2026) says an 18.5 TH/s miner beat 1-in-28,000 daily odds. A miner with less than a tenth of the hashrate is given better odds. Network difficulty differed between the two dates, but neither issue shows its working.

## Fees and orphaned blocks

- On June 7 mononautical confirmed that Mara had mined his transaction paying under 1 sat/vB, a month after he broadcast it. It cost 11 sats.
- His August 14 thread on the sub-sat summer explained the trade-off. Mara accepted below-standard fees to fill blocks during low demand. Such transactions are non-standard, so default nodes validate those blocks more slowly, which raises the risk of the block being orphaned.
- Between block heights 900,000 and 910,000 there were 11 orphaned blocks. Only one contained such transactions. At height 906,343 Antpool had a block orphaned by Foundry and lost a 3.145 BTC reward.
- Mara has since gone back to the standard minimum.

## The Bitaxe ecosystem

More background is in [Bitaxe and Open Source Miners United](../ecosystem/bitaxe-and-osmu.md).

**New makers and reach.**

- Digital Shovel announced the BluAx on June 11: a solo miner on the Bitaxe design, priced at $99 and drawing 18 watts.
- Gridless introduced the Bitshoka on June 25, made with a PCB manufacturer in Kenya.
- IxTech expanded its production of Bitaxe and NerdMiner devices (June 23).
- A Bitaxe workshop ran in El Salvador on June 20.
- Bitcoin educator Ziya Sadr posted about running a Bitaxe Gamma after the Oslo Freedom Forum (May 31).
- Jua Kali, hosted under the GridlessCompute GitHub account, is an open project for running ASIC hash boards on direct DC power such as solar panels or batteries.

**Clones and safety.**

- A Solo Satoshi article of April 8 set out the hidden cost of clones that ignore the open licenses.
- On June 16 a miner posing as a Bitaxe exploded.
- In October the podcast reported two Chinese entities trying to register the Bitaxe trademark in the US. Skot was opposing them and filing his own registration.

**Firmware and accessories.**

- AxeOS v2.9.0 came out on July 1 with log filtering, Stratum response time and API improvements.
- bitaxe-raw, published April 8 by @k1ix, lets a host send raw bytes to a Bitaxe over USB. Mujina development relies on it.
- A NerdQaxe firmware update to v1.0.31-RC was recommended on July 12 after a fault that blew a fuse and diodes.
- Pleb Style sold a low-profile cooler kit for the Bitaxe Gamma 601 at $93.00.
- IPv6 support for Bitaxe firmware was under discussion in October.

**New designs.**

- The Atlanta Bitlab Mining Hackathon ended on July 8. Minor League Miners won the software prize with a dashboard that gamifies small-scale mining. PC-AXE won the hardware prize with ASIC-equipped PCIe cards.
- Bitaxe Bonanza is built around the donated Intel BZM2 chips and uses a sidecar for Intel's 9-bit serial protocol (issue #22).
- Bitaxe Latte is a half-joking concept for a USB miner with a bill of materials of about $20 (issue #23).
- A new LVGL-based interface with support for external displays and knobs is described in issue #27.
- Dyson Labs planned to launch a Bitaxe CubeSat into low-Earth orbit.

## Hardware vendors

**Proto.** Proto supported the newsletter and donated chips. On August 14 it launched Rig.

- Rig makes up to 819 Th/s with all nine hash boards, at an efficiency as low as 14.1 J/Th and up to 12,000 Watts.
- It weighs 110 LBS and has three bays. Each bay holds a double fan assembly, three hash boards and a power supply.
- Fans, hash boards and power supplies can be swapped by hand, without tools, while the other bays keep hashing. The chassis becomes part of the site's permanent infrastructure.
- Proto also launched Fleet, its miner management software, in closed beta. Proto committed to making Fleet free and open source once fully released, with the mining firmware to follow.
- The author did not expect the hardware designs to be opened, and guessed Proto might sell its chips separately. He had nothing from Proto to cite for either point.
- At Bitcoin 2026 Proto demoed a compact mining box with open fleet management and a built-in touchscreen, and a pull request for Mujina was submitted from the conference floor.

**Intel BZM2 chips.** Proto donated 256,000 Intel BZM2 chips to the foundation, which passed all of them on to builders. The chips were made roughly 3-years earlier and are about as efficient as those in the Antminer S19j Pro. Reckless Systems launched Satoshi Starter on October 31 to produce an open reference design and chip documentation, so nobody has to reverse-engineer the chip.

**Canaan.** The December 2025 issue reports that Canaan published a GitHub repository with firmware source for its Avalon miners under a BSD3 license. The newsletter noted questions about compatibility with GPL-licensed code. It also noted Canaan's K230, a dual-core RISC-V processor. Canaan's turn toward home miners at the Heatpunk Summit is covered in [Hashrate Heat Reuse and the Heatpunk Summit](hashrate-heat-reuse.md).

**Bitmain.** On April 15 an S21+ firmware update blocked connections to the OCEAN and Braiins pools. Issue #13 passes on rumors of S23 air-cooled units and a pivot toward hydro and data-center gear.

**Others.**

- Braiins had recently open-sourced a control board, per the June 2025 issue. The foundation chose to build the [Libre Board](../hardware/libre-board.md) instead.
- Tether open-sourced its MOS fleet management platform (Episode 103 issue).
- FutureBit's Apollo 3 is cited in issue #17 as an example of open licensing.
- Issue #17 also relays a claim that 5nm chips such as the BM1366 are scarce.

## Tools for watching the network

- **stratum.work.** boerst's site shows what templates pools are sending. It gained a template detail page (April 26), a Sankey diagram of how pools assemble templates (July 11) and the events panel (August 26).
- **Mempool.** The Mempool Open Source Project released v3.2.0 on April 8 with a UTXO bubble chart and address poisoning detection.
- **UTXOracle.** A price oracle that uses only on-chain data (issue #22).
- **asic-rs and PyASIC.** Libraries for talking to miners from different makers through one interface.

## See Also

- [Editorial Essays and Arguments, 2025](editorial-essays-2025.md)
- [State of the Network, April to September 2025](state-of-the-network-2025.md)
- [Foundation Progress Timeline, 2025](foundation-progress-2025.md)
- [Foundation Progress Timeline, 2026](foundation-progress-2026.md)
- [Hydrapool](../hydrapool/hydrapool.md)
- [Bitaxe and Open Source Miners United](../ecosystem/bitaxe-and-osmu.md)
