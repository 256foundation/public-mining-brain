# Foundation Progress Timeline, 2025

> Sources: 256 Foundation (newsletter #5, May 2025), 2025-05-05; 256 Foundation (newsletter #6, June 2025), 2025-06-19; 256 Foundation (newsletter #7, July 2025), 2025-07-15; 256 Foundation (newsletter #8, August 2025), 2025-08-18; 256 Foundation (newsletter #9, September 2025), 2025-09-25; 256 Foundation (Assembling Freedom #10), 2025-10-28; 256 Foundation (Assembling Freedom #11), 2025-11-24; 256 Foundation (Assembling Freedom #12), 2025-12-22
> Raw: [Newsletter May 2025](../../raw/newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md); [Newsletter June 2025](../../raw/newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md); [Newsletter July 2025](../../raw/newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md); [Newsletter August 2025](../../raw/newsletter/2025-08-18-is-open-source-communism.md); [Newsletter September 2025](../../raw/newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md); [Assembling Freedom #10](../../raw/newsletter/2025-10-28-assembling-freedom-10.md); [Assembling Freedom #11](../../raw/newsletter/2025-11-24-assembling-freedom-11.md); [Assembling Freedom #12](../../raw/newsletter/2025-12-22-assembling-freedom-12.md)
> Updated: 2026-10-07

## Overview

The 256 Foundation published a monthly newsletter through 2025, written by econoalchemist and supported by Proto from the sixth issue on. Each issue reported on the month before it. Read in order, the eight issues from May to December 2025 give a month-by-month record of the four grant projects: the [Ember One](../hardware/ember-one.md) hash board, the [Libre Board](../hardware/libre-board.md) control board, [Mujina](../mujina/mujina-firmware.md) firmware and [Hydra Pool](../hydrapool/hydrapool.md). The year ran from the launch of three new grants on April 5 to a public Hydra Pool release on October 26 and a public Mujina Developer Preview announced in November. Several target dates slipped along the way, and this page keeps both the plans and what happened.

## The newsletter itself

- Issues five to nine carried essay-style titles. The tenth issue, for October 2025, renamed the newsletter Assembling Freedom and made it shorter.
- The eleventh issue dropped the State of the Network section and turned the Freedom Tech News section into a summary of that month's POD256 podcast episodes.
- The twelfth issue was the last monthly one. It said the newsletter would move to a weekly cadence after January 1, 2026, and thanked Proto for 12 months of support.

For the opinion pieces see [Editorial Essays and Arguments, 2025](editorial-essays-2025.md). For the network figures see [State of the Network, April to September 2025](state-of-the-network-2025.md). The 2026 issues are covered in [Foundation Progress Timeline, 2026](foundation-progress-2026.md).

## Month by month

### April (reported in the May issue)

- **Grants.** Ember One was the first fully funded grant. It launched in November 2024 for six months. Three more grants launched on April 5: Mujina, Hydra Pool and Libre Board. The date was chosen for the 6102 anniversary.
- **Ember One.** The first grant cycle ended on April 30. It produced a standard hash board: about 100W, a 12-24v input range, USB-C data, on-board temperature sensors and a 125mm x 125mm form factor. The first version, the 00, uses Bitmain BM1362 ASIC chips. The first official release was v3. Lead engineer: Skot (@skot9000). The next version was planned around the Intel BZM2 chip.
- **Mujina.** Ryan Kuester (@ryankuester) started writing the firmware from scratch in Rust. He used a Bitaxe running bitaxe-raw to stand in for an Ember One and got the first replies from an ASIC chip. The repo was still private.
- **Libre Board.** Schnitzel began adapting the open Raspberry Pi Compute Module I/O Board design. Changes included removing one of the two HDMI ports, adding a 40-pin header and accepting the same 12-24vdc range as Ember One.
- **Hydra Pool.** Jungly built an early version forked from CK Pool for Telehash #2. It paid out to the foundation's address automatically, so donors could use any username. The dashboard was forked from CKstats. The test server was a bare metal machine in Florida with 64 cores and 128 GB of RAM. The newsletter said the foundation "has no plans on becoming a mining pool operator".

### May (June issue)

- **Telehash #2.** Held on May 5 in Austin, TX. It ran for 8-hours with panels on each of the four projects. Public Pool ran a parallel instance mining to the same address with roughly 120 Ph/s. At the peaks there were roughly 2,500 workers and roughly 245 Ph/s. The best difficulty was 43.5T, from Mega Watt, the same miner who found the block at Telehash #1. No block was found and no money was raised. The Hydra Pool server was restarted approximately nine times in the first few hours before a fix went in. See [Telehash](../foundation/telehash.md).
- **Telehash #1 in hindsight.** The May issue recalled over 350 entities pointing hashrate at the first event, with closer to 800 Ph/s on the pool when the block was found.
- **TEMS.** The Texas Energy and Mining Summit followed over the next two days. Most of the grant recipients sat on a panel there.
- **Funding.** OpenSats included the foundation in its eleventh wave of Bitcoin grants, announced on May 14. HRF gave another grant for 2025. See [Grants and Funding](../foundation/grants-and-funding.md).
- **Ember One.** Version v4 was planned with reverse polarity protection and a circuit to protect USB devices from voltage spikes. Work on the BZM2 version was set to resume in the fall.
- **Libre Board.** The first connector list was published. It included an SD card slot, HDMI, Ethernet, four USB-C data-only ports, four hash board fan connectors, a Raspberry Pi HAT, two 100-pin Compute Module connectors and an NVME SSD connector.
- **Mujina.** The firmware could now deliver work to the ASICs and get a response. That is one of four main interfaces. The others are the API, pool communication and reading on-board sensors.
- **Hydra Pool.** The team dropped CK Pool as the code base. They looked at DATUM and Stratum v2, then chose to write a simple Stratum server from the ground up in Rust.

### June (July issue)

- **Published plan.** First Ember One 00 v4 boards with testers by the end of August. First official Libre Board and Hydra Pool releases by the end of September. A Mujina beta around the same time, and the first official Mujina release by the end of December.
- **Ember One.** 10 commits went into the v4 branch in June. A few prototypes were built and were being validated. The first batch was expected to ship in mid-August.
- **Libre Board.** All ports were mapped and placed. One Libre Board can drive up to four Ember One hash boards. The NVME port lets a user add an SSD and run a full Bitcoin node. The board matches the Ember One form factor so both fit one enclosure.
- **Mujina.** Hot-swapping a hash board without a reboot was described as a core feature. A terminal interface was planned next to the web UI.
- **Hydra Pool.** The new Rust Stratum server benchmarked comparably to CK Pool. The first release would offer solo mode and PPLNS mode.
- **Outreach.** Rod Roudi presented at BTCPay Day in Prague on June 22.

### July (August issue)

- **Plan revised.** The first batch of Ember Ones was taking longer than expected. Libre Board and Hydra Pool releases moved to the end of October. The first official Mujina release was now due at the end of December, maybe January 2026.
- **Ember One.** Skot hand assembled v4 prototypes and got first signs of life from all 12 ASIC chips. The reverse polarity circuit was contributed by @zbomstaz. A small run of roughly 100 units for testers was planned.
- **Hydra Pool.** A new test server went up on Signet at `test.hydrapool.org`. The newsletter asked readers to point miners at it for five minutes so the team could collect logs from many kinds of hardware.

### August (September issue)

- **Ember One.** v4 passed validation and was declared ready for production. The newsletter described it as a board of about 100W built around BM1362AC chips, capable of roughly 3.5Th/s.
- **Libre Board.** Tracing through the 6-layer PCB was finished. At the last minute the team swapped both voltage regulators for newer parts with an I²C interface, so the board can report power draw. That change touched about 10 components.
- **Mujina.** Developed on a Bitaxe Gamma as a stand-in. Discovery, hot-plugging, monitoring, logging, a pool client (stratum v1 only for now), work distribution, the API and early CLI and TUI clients were all taking shape.
- **Hydra Pool.** Over 30 different kinds of miners connected to the test server and exposed issues that were then fixed. Work moved on to PPLNS paid straight from the coinbase. The pool will not copy Bitmain's limit of some 16 payout addresses, though old stock Antminers cannot handle more. Share data will be exposed through an API so anyone can audit the pool. The first release was expected the following month.
- **Assembly line.** On August 9 econoalchemist set up a pick and place machine and a reflow oven to build the foundation's designs. The newsletter is clear that this is a private venture separate from the 256 Foundation. First jobs: a few Libre Board prototypes, then about 100 Ember One boards.
- **Proto Rig.** The foundation attended Proto's launch of its Rig miner on August 14 and recorded two live POD256 episodes there. See [Open Mining Ecosystem News, 2025 to 2026](open-mining-ecosystem-news.md).

### September (October issue)

- **Chip donation.** On September 2 the foundation took possession of 256,000 Intel BZM2 ASIC chips donated by Proto Mining. All of them were disbursed to builders. Technical documentation could not be included.
- **Ember One.** The 00 design moved to v5 as a release candidate. It has a new voltage regulator with live power monitoring. The trade-off is a narrower input range, from 12-24vdc down to 12-17vdc. Parts for 5 prototypes were ordered.
- **Libre Board.** The team recorded a nearly 2-hour schematic review. Prototype materials were on order.
- **Mujina.** Now running on an Ember One 00 v4.1 prototype. The design goal is to mix boards with different chips and share work according to what each chip can do. The repo was to go public with the first Ember One production batch.
- **Hydra Pool.** The Stratum server was finished, including PPLNS rules and share auditing. Jungly appeared on the Stephan Livera podcast to talk about P2Pool v2.
- **Events.** econoalchemist spoke at the first ImagineIF Summit in Nashville on September 20. Tom's Hardware covered the chip donation.

### October (November issue)

- **Hydra Pool released.** The pool was released on October 26 and had reached v1.1.18 by the time of the newsletter. It supports solo mining and PPLNS, pays from the coinbase, exposes share accounting through an API, ships a Prometheus and Grafana dashboard, is written in Rust and is licensed AGPLv3. It was limited to 100 users for coinbase and block weight reasons. An instance was mining on mainnet at `test.hydrapool.org`.
- **Ember One.** Boards and parts arrived for the first five v5 prototypes.
- **Libre Board.** Prototypes were delayed after customs destroyed a shipment of components.
- **Mujina.** Ryan prepared a Developers Preview. Its disclaimer opens: "This software is under heavy development and not ready for production use."
- **Events.** Several grantees attended TabConf in Atlanta. The podcast also teased a Telehash in January on Hydra Pool.

### November (December issue)

- **Mujina.** At the Bitcoin++ event the foundation announced that the Mujina Developer Preview was open to the public.
- **Community.** Pull requests arrived in the Hydra Pool repo. Community repos such as asic-rs joined the foundation's GitHub organization.
- **Advocacy.** Keonne Rodriguez of Samourai Wallet joined POD256 #96. See [Samourai Wallet Case and Developer Liability](samourai-wallet-case.md).

## Plans against outcomes

| Milestone | First stated target | Later target | What the newsletters record |
|---|---|---|---|
| Ember One test batch ships | Mid-August (July issue) | Slipping (August issue) | Still at the v5 prototype stage in the November issue |
| Hydra Pool first release | End of September (July issue) | End of October (August issue) | Released on October 26 |
| Libre Board first release | End of September (July issue) | End of October (August issue) | Prototype parts delayed in customs, per the November issue |
| Mujina first official release | End of December (July issue) | End of December, maybe January 2026 (August issue) | Developer Preview opened to the public in November |

## See Also

- [Foundation Progress Timeline, 2026](foundation-progress-2026.md)
- [Editorial Essays and Arguments, 2025](editorial-essays-2025.md)
- [State of the Network, April to September 2025](state-of-the-network-2025.md)
- [Hashrate Heat Reuse and the Heatpunk Summit](hashrate-heat-reuse.md)
- [Telehash](../foundation/telehash.md)
- [Grants and Funding](../foundation/grants-and-funding.md)
- [256 Foundation: Mission and Organization](../foundation/mission-and-organization.md)
