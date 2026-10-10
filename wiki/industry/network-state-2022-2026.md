# Network State 2022–2026

> Sources: POD256 show notes ("State of the Network" segment and news links), 2022-12-03 → 2026-09-28; POD256 episode 126 machine transcript (2026-09-21); 256 Foundation monthly newsletter "Bitcoin Network" sections, 2025-05 → 2025-10, and weekly "Assembling Freedom" issues, 2025-11 → 2026-05; 256 Foundation website, Telehash page and forum, 2026; heatpunks.org summit page (captured 2026-10-07); POD256 transcripts (2025-04 → 2026-09)
> Raw: [POD256 ep 031](../../raw/history/pod256/2023-10-30-pod256-031-no-holds-barred-w-special-guest-bitmaker-creator.md); [POD256 ep 046](../../raw/history/pod256/2024-05-24-pod256-046-no-holds-barred-w-special-guest-luke-dashjr-chair.md); [Newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md); [Newsletter, Jul 2025](../../raw/history/256f-newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md); [Newsletter, Oct 2025](../../raw/history/256f-newsletter/2025-10-28-assembling-freedom-10.md); [POD256 ep 126 transcript](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-21-e126.md); [POD256 e086 transcript](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-10-e086.md); [POD256 e088 transcript](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-24-e088.md); [POD256 e101 transcript](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-01-14-e101.md); [POD256 e119 transcript](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-07-08-e119.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

This page collects dated snapshots of the Bitcoin mining network as the 256 Foundation's podcast ([POD256](../history/pod256-podcast.md)) and newsletter reported them between December 2022 and September 2026: network hashrate, difficulty, hashvalue/hashprice, ASIC price tiers, fee-market episodes such as 2025's "sub-sat summer", and the corporate, policy/legal and conference events those sources covered. From mid-2025 the POD256 machine transcripts add on-air readings — the network crossing a zetahash in September 2025, record-low hashprice in spring 2026, the December 2025 China hashrate drop, the S23 delays, the AI/HPC pivot of public miners and the August 2026 BIP 110 fork. Transcripts have no speaker labels, so on-air claims are attributed as the hosts identified themselves and opinions are marked as opinions. **Every number here is volatile and is stamped with the date of the source that reported it** — none of it is current data. Values are copied in the units and formatting the source used (Eh vs Eh/s, sats/TH/day vs sats/Ph/day); where sources disagree the conflict is shown rather than resolved. Use it as a reference for what the network looked like around a given event and as context for home-mining economics, not as a live dashboard.

## Reading the numbers (durable reference)

| Metric | What the sources report | Where they got it |
|---|---|---|
| Hashrate | Network hashrate on a **14-day moving average** (2023–Aug 2025); the September 2025 newsletter switched to a **7-day MA**; 2026 podcast readings quote spot, 3-day and 7-day figures | mempool.space ([ep 005](../../raw/history/pod256/2023-01-27-pod256-005-expected-difficulty-adjustment-trending-miner-pri.md); [newsletter, Oct 2025](../../raw/history/256f-newsletter/2025-10-28-assembling-freedom-10.md)) |
| Difficulty | Current value in trillions ("T") plus the expected % change at the end of the numbered epoch | Bitrawr's estimator, replaced by Newhedge by late 2023 ([ep 005](../../raw/history/pod256/2023-01-27-pod256-005-expected-difficulty-adjustment-trending-miner-pri.md); [ep 030](../../raw/history/pod256/2023-10-07-pod256-030-no-holds-barred-w-special-guest-skot-instigator-b.md)) |
| Hashvalue | Sats earned per unit of hashrate per day — sats/TH/day until early 2024, then sats/Ph/day | Braiins Insights |
| Hashprice | The same in USD, $/Ph/day | Braiins Insights ([ep 043](../../raw/history/pod256/2024-04-06-pod256-043-special-guest-skot-instigator-bitaxe-state-of-the.md)) |
| ASIC prices | USD per TH of machine capacity, by efficiency tier (2025 tiers: <19 J/Th, 19–25 J/Th, >25 J/Th) | Luxor's Hashrate Index |

Two practical notes for home miners. First, hashvalue roughly halves at a halving — the show's readings went from 160k sats/PH/day the day before the April 2024 halving to 80k sats/Ph/day a month after ([ep 044](../../raw/history/pod256/2024-04-19-pod256-044-state-of-the-network-news-tangents-home-miner-of.md); [ep 046](../../raw/history/pod256/2024-05-24-pod256-046-no-holds-barred-w-special-guest-luke-dashjr-chair.md)). Second, the hosts argue that price per terahash and cost per kilowatt-hour are the units home miners relate to, not hashprice per petahash ([ep 126 transcript](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-21-e126.md)). For profitability math see [Open Mining Economics](../economics/open-mining-economics.md) and [Hashrate Heating Economics](../economics/hashrate-heating-economics.md).

**On-air readings (2025–2026).** In the transcribed episodes the hosts read hashrate off mempool.space's one-week moving average (sometimes the three-day) and hashprice/hashvalue off Braiins Insights, and read the numbers aloud, so values below are copied as the machine transcript rendered them ("996 x a hash", "1.09 per second") ([e086](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-10-e086.md); [e088](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-24-e088.md)). Difficulty notation itself was debated on air in January 2026: AxeOS settled on giga-style SI prefixes while some hosts preferred million/billion/trillion, the ambiguity being B (billion) versus G (giga) ([e101](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-01-14-e101.md)).

**Network energy and average efficiency.** Two rough estimates came up on air, both explicitly hedged by the hosts:

- On 2025-08-27 Tyler divided the Cambridge electricity-consumption index (about 170 terawatt hours, "I don't know how accurate that is") by the seven-day hashrate and got 27 joules per terahash in January 2025 and 23 at recording — far from latest-generation machines, which he read as many older machines still running ([e082](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-08-27-e082.md)).
- On 2025-10-29 a host read the Cambridge (CCAF) dashboard's estimate of 26 gigawatts for Bitcoin; Eco cautioned that after the 2021 China ban the same site still showed some 60% of hashrate in China, so it lags ([e092](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-29-e092.md)).
- In September 2026 Tyler summarized an article by Safedine hypothesizing that Bitcoin mining's total energy use has peaked as large on-grid miners move to AI; Tyler disagreed, citing new integration use cases, and Scott noted efficiency gains lower energy per terahash at constant hashrate ([e126 transcript](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-21-e126.md)). This is an opinion exchange, not a measurement.

## Snapshots

### Late 2022: capitulation

- Episode 001 (published 2022-12-03) opened with hashrate down ~14% from its all-time high, hashprice in all-time-low territory and new-generation ASICs at all-time-low valuations ([ep 001](../../raw/history/pod256/2022-12-03-pod256-001-hashrate-down-14-from-ath-hashprice-at-atl-territ.md)).
- A week later difficulty was down 7.3% amid miner capitulation ([ep 002](../../raw/history/pod256/2022-12-10-pod256-002-miner-capitulation-and-compute-north-bankruptcy-d.md)); by 2022-12-16 difficulty was headed back up while public miners were "against the ropes" ([ep 003](../../raw/history/pod256/2022-12-16-pod256-003-public-miners-against-the-ropes-esg-anti-bitcoin.md)).
- Luxor's CEO later said miners who simply kept machines on in May 2023 made almost 11% more bitcoin ([ep 021](../../raw/history/pod256/2023-06-10-pod256-021-state-of-the-network-news-tangents-home-miner-of.md)).

### Late 2023 → April 2024 halving (POD256 weekly readings)

From episode 031 the show notes wrote out difficulty, hashrate and hashvalue. Dates are episode publish dates; hashrate is the 14-day MA unless noted.

| Ep | Published | Block | Difficulty (expected change) | Hashrate | Hashvalue |
|---|---|---|---|---|---|
| [031](../../raw/history/pod256/2023-10-30-pod256-031-no-holds-barred-w-special-guest-bitmaker-creator.md) | 2023-10-30 | 813948 | 61T (~2.3% up, end of epoch 403) | 440Eh | 212 sats/TH/day |
| [032](../../raw/history/pod256/2023-12-18-pod256-032-no-holds-barred-w-special-guests-diverter-author.md) | 2023-12-18 | 821220 | 67.3T (after -0.95% on December 9, 2023) | 484Eh | 255 sats/TH/day |
| [033](../../raw/history/pod256/2024-01-25-pod256-033-nems-2024-recap-state-of-the-network-tangents-new.md) | 2024-01-25 | 827188 | 70.3T (~2% up, epoch 410) | roughly 515Eh | 190 sats/TH/day |
| [034](../../raw/history/pod256/2024-02-02-pod256-034-home-open-source-mining-initiative-state-of-the-n.md) | 2024-02-02 | 828411 | 70.3T (~6% up, epoch 410) | 526Eh | 190sats/TH/day |
| [035](../../raw/history/pod256/2024-02-10-pod256-035-no-holds-barred-w-special-guests-wilson-mining-st.md) | 2024-02-10 | 829415 | 75.5T (7-12% up, epoch 411) | 565Eh, all-time high | 180 sats/TH/day |
| [036](../../raw/history/pod256/2024-02-16-pod256-036-no-holds-barred-w-special-guest-bassload-energy-p.md) | 2024-02-16 | 830468 | 70.3T (~7% up, epoch 411) — see Disputed | 568Eh | 180 sats/TH/day |
| [037](../../raw/history/pod256/2024-02-24-pod256-037-no-holds-barred-w-special-guest-rapha-zagury-alph.md) | 2024-02-24 | 831444 | 81.7 Trillion (~5% down, epoch 412) | 569Eh | 160sats/TH/day |
| [038](../../raw/history/pod256/2024-03-01-pod256-038-state-of-the-network-news-tangents-home-miner-of.md) | 2024-03-01 | 832577 | 81.7 Trillion (roughly 3% down, epoch 412) | 569Eh, below a recent high of 581Eh | 170sats/TH/day |
| [039](../../raw/history/pod256/2024-03-09-pod256-039-no-holds-barred-w-special-guest-pennyether-bitcoi.md) | 2024-03-09 | 833445 | 79.3 Trillion (roughly 0.25% down, epoch 413) | 577Eh | 170sats/TH/day |
| [040](../../raw/history/pod256/2024-03-15-pod256-040-state-of-the-network-news-tangents-home-miner-of.md) | 2024-03-15 | 834555 | 79.3 Trillion (roughly 5.8% up, epoch 413) | 591Eh, new all-time high | 160sats/TH/day |
| [041](../../raw/history/pod256/2024-03-22-pod256-041-no-holds-barred-w-special-guest-zack-bomsta-found.md) | 2024-03-22 | 835558 | 83.9 Trillion (roughly 0.3% down, epoch 414) | 612Eh, new all-time high | 150 sats/TH/day |
| [042](../../raw/history/pod256/2024-03-30-pod256-042-no-holds-barred-w-special-guest-montana-dukes-ceo.md) | 2024-03-30 | 836541 | 83.9 Trillion (roughly 1.5% down, epoch 414) | 594Eh | 150 sats/TH/day |
| [043](../../raw/history/pod256/2024-04-06-pod256-043-special-guest-skot-instigator-bitaxe-state-of-the.md) | 2024-04-06 | 837580 | 83.1 Trillion (roughly 2% up, epoch 415) | 603Eh | 160k sats/Ph/day; hashprice roughly $103/Ph/day |
| [044](../../raw/history/pod256/2024-04-19-pod256-044-state-of-the-network-news-tangents-home-miner-of.md) | 2024-04-19 | 839818 | 86.3 Trillion (decrease expected, epoch 416) | 629Eh, new ATH going into the halving | 160k sats/PH/day; hashprice $102/Ph/Day |
| [046](../../raw/history/pod256/2024-05-24-pod256-046-no-holds-barred-w-special-guest-luke-dashjr-chair.md) | 2024-05-24 | 844622 | 83.1 Trillion (roughly 1% up, epoch 418) | 591Eh, down from the ATH of 639Eh on April 27th | 80k sats/Ph/day; hashprice $56/Ph/Day |

- **Leap-day adjustment.** Episodes 037–038 expected the epoch 412 adjustment to land on February 29th, which the notes call the only difficulty adjustment on a leap-year day in Bitcoin's history ([ep 038](../../raw/history/pod256/2024-03-01-pod256-038-state-of-the-network-news-tangents-home-miner-of.md)).
- **ASIC prices, early 2024.** Miners under 25J/Th sold for roughly $13.73/Th, "relatively flat since October", in episodes 039–043, then roughly $12.21/Th in episodes 044 and 046 ([ep 039](../../raw/history/pod256/2024-03-09-pod256-039-no-holds-barred-w-special-guest-pennyether-bitcoi.md); [ep 044](../../raw/history/pod256/2024-04-19-pod256-044-state-of-the-network-news-tangents-home-miner-of.md)).
- **Mempool, February 2024.** About 250k transactions were pending and those paying less than 24 sats/v-byte were being purged ([ep 034](../../raw/history/pod256/2024-02-02-pod256-034-home-open-source-mining-initiative-state-of-the-n.md)).
- After the halving the countdown reset to 1,407 days ([ep 046](../../raw/history/pod256/2024-05-24-pod256-046-no-holds-barred-w-special-guest-luke-dashjr-chair.md)). From episode 047 the show notes stop printing figures.

> **Status: Disputed** — difficulty around epoch 411
> Episode 035 (2024-02-10) gives 75.5T; episode 036 (2024-02-16) gives 70.3T while still expecting an increase; episode 037 (2024-02-24) gives 81.7 Trillion ([ep 035](../../raw/history/pod256/2024-02-10-pod256-035-no-holds-barred-w-special-guests-wilson-mining-st.md); [ep 036](../../raw/history/pod256/2024-02-16-pod256-036-no-holds-barred-w-special-guest-bassload-energy-p.md); [ep 037](../../raw/history/pod256/2024-02-24-pod256-037-no-holds-barred-w-special-guest-rapha-zagury-alph.md)). Best assessment: 70.3T in episode 036 is a stale carry-over from episodes 033–034; the notes never corrected it.

### 2025 monthly readings (256 Foundation newsletter)

Each row is the newsletter's month-in-review. Hashrate is the mempool.space 14-day MA (7-day MA for September).

| Month | Hashrate | Difficulty | Hashvalue / hashprice | Source |
|---|---|---|---|---|
| April 2025 | ~826 Eh/s → peak ~907 Eh/s (April 16) → ~841 Eh/s; ~1.8% for the month | 113.76T–123.23T; Epoch #444 brought -3.3% on May 3; ~8.5% YTD | ~56,000 → ~52,000 sats/Ph per day; hashprice $46.00/Ph → $49.00/Ph per day | [May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md) |
| May 2025 | ~837 Eh/s → all-time high ~917 Eh/s (~9.5%) | 119.12T–126.98T; ~15.6% YTD through Epoch #446 | peak ~59,000, close ~52,000 sats/Ph per day | [Jun 2025](../../raw/history/256f-newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md) |
| June 2025 | ~915 Eh/s → 840 Eh/s (roughly -8.1%) | 126.98T → 116.96T (~7.8% down); ~6.5% YTD through Epoch #448 | roughly 50k → 55k sats/Ph/day | [Jul 2025](../../raw/history/256f-newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md) |
| July 2025 | ~832 Eh/s → 906 Eh/s (+8.8%); +15.2% YTD | 116.96T–127.62T; ~16.2% YTD through Epoch #450 | roughly 54k → 49k sats/Ph/day | [Aug 2025](../../raw/history/256f-newsletter/2025-08-18-is-open-source-communism.md) |
| August 2025 | ~913 Eh/s → ~966 Eh/s (+5.8%); +22.9% YTD | 127.62T → 129.7T; ~18.1% YTD through Epoch #452 | around 49k sats/Ph/day | [Sep 2025](../../raw/history/256f-newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md) |
| September 2025 | ~969 Eh/s → ~1,060 Eh/s (1.06 Zh/s), +9.4%; +34.8% YTD (7-day MA) | 129.7T → 142.3T (9.7%); ~29.6% YTD through Epoch #455 | ~48k → ~44.5k sats/Ph/day | [Oct 2025](../../raw/history/256f-newsletter/2025-10-28-assembling-freedom-10.md) |

The September 2025 issue put the next halving (block height 1,050,000) around March 29, 2028 ([newsletter, Oct 2025](../../raw/history/256f-newsletter/2025-10-28-assembling-freedom-10.md)). The monthly network section ended when the newsletter went weekly in 2026 ([newsletter, Dec 2025](../../raw/history/256f-newsletter/2025-12-22-assembling-freedom-12.md)).

### 2025–2026 on-air readings (POD256 transcripts)

Dates are episode publish dates. Hashrate is mempool.space's one-week moving average unless noted; numbers are as the machine transcript rendered the spoken values.

| Episode (published) | Hashrate | Difficulty | Hashprice / hashvalue | Other | Source |
|---|---|---|---|---|---|
| e080 (2025-08-01) | 895.6 exahashes (seven-day), almost 900 | — (a recent negative 7.5% adjustment mentioned as since rebounded) | hashvalue 50,000 per petahash per day; hashprice $59 per petahash per day | halving nine hundred and seventy seven days away | [e080](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-08-01-e080.md) |
| e081 (2025-08-20) | "roughly" one zetahash (Tyler) | — | — | — | [e081](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-08-20-e081.md) |
| e082 (2025-08-27) | "about to pass one Zeta Hash" | — | — | — | [e082](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-08-27-e082.md) |
| e086 (2025-09-10) | 996 x a hash, "just shy of a Zeta hash" | 129,700,000,000,000.0 until September 4, then 136,040,000,000,000.00 | hashprice $52.79 per petahash per day; hashvalue 49,000 sats before the adjustment → about 46,500 sats per petahash per day | — | [e086](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-10-e086.md) |
| e088 (2025-09-24) | 1.09 (zetahash) one-week — the network crossed a zetahash in 2025, settling an on-air wager | 142,340,000,000,000.00 at block height 916222 | hashprice 51 US dollars per petahash; hashvalue 40,000 sats per petahash per day | halving nine hundred and eleven days away; Scott: bitcoin's price about where it began the year while hashrate is 30% higher | [e088](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-24-e088.md) |
| e092 (2025-10-29) | 1.12 Zeta Hash | — | — | — | [e092](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-29-e092.md) |
| e101 (2026-01-14) | 1.01 zeta hash | 146,470,000,000,000.00 at block height 932289 | — | — | [e101](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-01-14-e101.md) |
| e109 (2026-03-25) | (garbled in transcript) | — | "Hash price in the dumps": a year earlier $50 per petahash (5¢ per terahash), now 3¢ | — | [e109](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-03-25-e109.md) |
| e112 (2026-04-15) | — | — | hashprice "already at its lowest ever", 3¢ a terahash per day | — | [e112](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-04-15-e112.md) |
| e114 (2026-05-13) | 984 ex a hash | — | — | — | [e114](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-05-13-e114.md) |
| e126 (2026-09-21) | see September 2026 snapshot below | | | fees averaged 2,100,000 sats per block above the subsidy over the last 144 blocks; under 85,000 transactions in the mempool | [e126](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-21-e126.md) |

### Crossing a zetahash (September 2025)

The newsletter's September 2025 row above ends at ~1,060 Eh/s (1.06 Zh/s) on the 7-day MA. On air, the hosts tracked the approach: Tyler called the network "roughly" one zetahash on 2025-08-20, the hosts were "about to pass one Zeta Hash" a week later, the one-week average was 996 x a hash on 2025-09-10 and 1.09 on 2025-09-24 ([e081](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-08-20-e081.md); [e082](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-08-27-e082.md); [e086](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-10-e086.md); [e088](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-24-e088.md)). On 2025-10-29 a host relayed an article by Marty saying that six weeks after one zeta hash the network had already added another 100 x a hash, whereas it took twelve years to reach the first 100 x a hash; the reading that day was 1.12 Zeta Hash ([e092](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-29-e092.md)). Hashrate then drifted back: 1.01 zeta hash in January 2026, 984 ex a hash in May and about 936 in September 2026 ([e101](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-01-14-e101.md); [e114](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-05-13-e114.md); [e126 transcript](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-21-e126.md)).

Scott's rough supply-side math in August 2025: latest chips do about one terahash each, so a zetahash is about a billion chips; a circulated, unverified TSMC allocation showing Bitmain at 120,000 wafers for the rest of 2025 and 2026 would represent "in the neighborhood of 260, ex a hash" by his estimate ([e082](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-08-27-e082.md)).

### Record-low hashprice (spring 2026)

Hashprice fell from $59 per petahash per day (2025-08-01) to $52.79 (2025-09-10) and 51 US dollars per petahash (2025-09-24) in the readings above. By March 2026 the hosts put it at 3¢ per terahash versus 5¢ a year earlier, and on 2026-04-15 called it "at its lowest ever", 3¢ a terahash per day, wondering whether it could trigger a mass hashrate decline ([e109](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-03-25-e109.md); [e112](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-04-15-e112.md)). The hosts' takeaway was that public miners pivoting to AI/HPC might reduce demand for industrial rigs and push ASIC makers toward home and heat-reuse customers — an opinion, see the AI/HPC section below.

### China hashrate drop (December 2025)

On 2025-12-17 a host read a chart he attributed to Blockspace Media: computing power had dropped by a 100 exahash versus the previous day, estimated as 1.3 to 1.63 gigawatts winding down (he also said "Some, like, three gigawatts of capacity went offline") ([e099](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-12-17-e099.md)). Causes were unclear on air: the piece recalled China's province-by-province ban of 2021 and a "system of favoritism", which the host called "mostly, like, insider scoop speculation", while Eco favored the narrative that miners were moving their power to AI hosting. No follow-up figure appears in these sources.

### ASIC price tiers, 2025 (Hashrate Index via the newsletter)

USD per TH of machine capacity, as reported at each month's end.

| Month | <19 J/Th | 19–25 J/Th | >25 J/Th | Source |
|---|---|---|---|---|
| April 2025 | $17.29 | $11.05 | $3.20 | [May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md) |
| May 2025 | $17.77 | $8.85 | $3.02 | [Jun 2025](../../raw/history/256f-newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md) |
| June 2025 | $17.22 | $7.52 | $2.82 | [Jul 2025](../../raw/history/256f-newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md) |
| July 2025 | $17.94 | $6.52 | $3.04 | [Aug 2025](../../raw/history/256f-newsletter/2025-08-18-is-open-source-communism.md) |
| August 2025 | $13.92 | $7.56 | $3.64 | [Sep 2025](../../raw/history/256f-newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md) |
| September 2025 | $14.11 | $4.75 | around $3.52 | [Oct 2025](../../raw/history/256f-newsletter/2025-10-28-assembling-freedom-10.md) |

In April and May 2025 the newsletter added that a new-gen miner with 230+ Th/s cost roughly $4,000 ([May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md)).

> **Status: Disputed** — August 2025 tier prices
> The September 2025 issue gives August's closing prices as $13.92/Th, $7.56/Th and $3.64/Th ([Sep 2025](../../raw/history/256f-newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md)). The October 2025 issue describes the same tiers as up from $13.96/Th, down from $8.57/Th "at the beginning of the month", and compared to $3.92/Th last month ([Oct 2025](../../raw/history/256f-newsletter/2025-10-28-assembling-freedom-10.md)). Best assessment: the later issue appears to quote a different snapshot date of the index (start of September rather than end of August); treat the per-row values as approximate. Supporting the September-issue figures: on 2025-09-10 the podcast read the same three values ($13.92, $7.56 per terahash, $3.64 per terahash) as current hashrateindex.com prices, labeling the tiers "under 19", "under 25" and "under 38" joules per terahash rather than ">25" — the hosts noted the free Intel BZM2 chips fall in that last tier ([e086](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-10-e086.md)).

### Machine and chip prices read on air (2025–2026)

| Episode (published) | Item | Price as read | Source |
|---|---|---|---|
| e080 (2025-08-01) | Antminer S21 XP (270 TH class) via Altair; single chips | $27 a terra hash; each chip $26.90 | [e080](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-08-01-e080.md) |
| e086 (2025-09-10) | Antminer S23 | hosts unsure: heard 7 or $8,000, "maybe it's $12,000" with coupons bringing it down; Eco estimated about 220 days to pay off a $12,000 unit if hashrate stayed flat | [e086](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-10-e086.md) |
| e088 (2025-09-24) | Antminer S21 XP via Altair | $5,600 for 270 Terahash | [e088](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-24-e088.md) |
| e095 (2025-11-19) | TSMC two-nanometer wafer (Scott, via an AI estimate) | $20,000 each, roughly 300 dies per wafer → around $70 a chip | [e095](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-11-19-e095.md) |
| e101 (2026-01-14) | Antminer S21 XP, 270 terahash, carrying 273 BM1370 chips | around $4,900, which is $27 per terahash | [e101](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-01-14-e101.md) |
| e105 (2026-02-18) | Single BM1370 chip (Bitaxe Gamma chip), when obtainable | $30.40 | [e105](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-02-18-e105.md) |
| e112 (2026-04-15) | Used Antminer S19 J Pro (MegaMiner), 100 terahash units, 90-unit minimum | $99 each — roughly a dollar per terahash; a host recalled paying a $100 per terahash for a 110 terahash S19 in 2021 | [e112](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-04-15-e112.md) |
| e117 (2026-06-17) | Antminer S23 hydro (rack-mount) / smaller hydro form factor | "like $23,000" / "15 or $16,000" (hosts' recollection) | [e117](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-06-17-e117.md) |

The hosts disliked quoting miners in dollars per terahash ("I hate that miners have this, like, commodity unit basis") and read the unit as a sign of a monopoly market ([e101](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-01-14-e101.md)). For a mid-2026 snapshot of unit economics, a host read electronics.dev's page on 2026-05-27: an Antminer S23 Hydro "could earn a daily profit of $11.91", breaking even at 15¢ a kilowatt hour, while an Antminer T19 Hydro would lose $2.87 a day, breaking even at 3.8¢; the same data set forecast 2 joules per terahash in 2031 ([e115](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-05-27-e115.md)).

### June 2025 difficulty drop

On June 28, 2025 difficulty dropped ~7.5%, which the newsletter called the biggest downward adjustment since the 2021 Chinese mining ban (when difficulty fell by almost 40% in one adjustment). Speculated causes ranged from interrupted Iranian mining during US bombing to large miners curtailing in a Texas heat wave. A home-sized miner with ~2.3Ph/s then found block #903883 on Solo CK Pool ([newsletter, Jul 2025](../../raw/history/256f-newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md)). POD256 had read market signs as pointing to a possible difficulty drop a few days earlier ([ep 075](../../raw/history/pod256/2025-06-26-pod256-075-sourcing-chips-and-building-bitaxes.md)). Hashrate rebounded within a month (July row above).

### "Sub-sat summer" (2025 fee market)

- On June 7, 2025 mononautical confirmed that his sub 1-sat/vB transaction was mined by Mara about a month after broadcast, showing some miners accept fees below the usual minimum relay fee ([newsletter, Jul 2025](../../raw/history/256f-newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md)).
- His August 14 thread explained the trade-off: Mara filled blocks with sub-1 sat/vB transactions during low block-space demand to raise rewards, but such blocks are non-standard and slower for default nodes to validate, so they carry more orphan risk. Of 11 orphaned blocks between heights 900,000 and 910,000 only one contained sub-1 sat/vB transactions; at height 906,343 Antpool lost its 3.145 BTC reward to a Foundry orphan. Mara later reverted to the 1-sat/vB minimum ([newsletter, Sep 2025](../../raw/history/256f-newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md)).
- Low fees and node configuration were also discussed on air ([ep 078](../../raw/history/pod256/2025-07-18-pod256-078-devs-on-trial-privacy-on-the-line.md)). A year later the hosts debated whether network usage and fee pressure can support miners as the subsidy shrinks ([ep 126](../../raw/history/pod256/2026-09-22-pod256-126-why-open-source-bitcoin-mining-matters-more-than.md)).

### Early 2026 difficulty drop

POD256 episode 104 (2026-02-11) discussed "the recent major difficulty drop and what it means for home miners" ([ep 104](../../raw/history/pod256/2026-02-11-pod256-104-ai-open-source-bitcoin-mining-and-battling-survei.md)); the newsletter summary called it the largest Bitcoin difficulty drop since the 2021 China ban and framed it as making home mining viable again ([newsletter #16](../../raw/history/256f-newsletter/2026-02-11-assembling-freedom-16-ai-open-source-bitcoin-mining-and-batt.md)). Neither source states the percentage; on air a host guessed "Like, 15% downward or something?" ([ep 104 transcript](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-02-11-e104.md)).

> **Status: Disputed** — biggest since the China ban
> The July 2025 newsletter already gave that title to the ~7.5% drop of June 28, 2025 ([newsletter, Jul 2025](../../raw/history/256f-newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md)); the February 2026 sources give it to the early-2026 drop ([newsletter #16](../../raw/history/256f-newsletter/2026-02-11-assembling-freedom-16-ai-open-source-bitcoin-mining-and-batt.md)). Both can be true only if the 2026 drop was larger than ~7.5%, which the sources do not confirm (the 15% figure is an on-air guess). The 2026 weekly newsletters look AI-generated from episodes and are lower confidence.

### September 2026 snapshot (on air)

From the machine transcript of episode 126, recorded 2026-09-21 ([ep 126 transcript](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-21-e126.md)) — numbers were spoken, so they are given as transcribed:

- Hashrate "currently floating around 936" exahash (transcribed "936 x a hash"), "nine sixty on the three day moving average, nine thirty one on the seven day".
- Difficulty "one thirty two point seven six trillion with the last retarget going up 4.16%", at block height 967,680 on September 19.
- Average block reward 3.146 bitcoin.
- Seven-day block share: Foundry 23.7%, AntPool (transcribed "amp pool") 20.3%, F2Pool 16%; Ocean down to 1.8% after bouncing back to 3.3% following the BIP 110 episode.

## Hardware market: share, roadmaps and rumors (2025–2026)

### Bitmain market share (hosts' estimates)

No source here measures ASIC market share; the figures are the hosts' recurring estimates and vary between 80% and 90%:

| Episode (published) | Claim | Source |
|---|---|---|
| e067 (2025-04-14) | Scott: incumbents "control, like, 80% or more of the market" | [e067](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-04-14-e067.md) |
| e082 (2025-08-27) | Bitmain "controls 80% of the market", so public miners preorder by default and falling behind on hashrate acts as an unofficial halving | [e082](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-08-27-e082.md) |
| e092 / e094 (2025-10-29 / 2025-11-12) | "90 plus percent market dominance" / "90% market share", in discussions of a Bitcoin Magazine video on Bitmain; Canaan described as having single-digit share, "or maybe, like, 10%" | [e092](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-29-e092.md); [e094](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-11-12-e094.md) |
| e097 (2025-12-03) | roughly 80% (90% elsewhere in the same episode), so a US import ban would severely limit miner supply | [e097](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-12-03-e097.md) |
| e101 (2026-01-14) | "somewhere in the neighborhood of 80%" | [e101](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-01-14-e101.md) |
| e103 (2026-02-04) | Scott's Plan B talk: Bitmain controls "80% of the market by hash rate"; his slide claimed 99.999% of blocks since ASICs were mined by closed-source miners | [e103](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-02-04-e103.md) |
| e117 (2026-06-17) | Core developers at Oslo BitDevs were often unaware Bitmain "controls 80% of the hardware market" | [e117](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-06-17-e117.md) |

### Efficiency targets and the S23 saga

| Episode (published) | Report | Source |
|---|---|---|
| e081 (2025-08-20) | Scott: the Antminer S23, supposed to ship "in January 26" (January 2026), is listed at 9.5 (spoken as "listed at 9.5", joules per terahash implied); Proto's Rig cited 14.1 joules per terahash | [e081](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-08-20-e081.md) |
| e085 (2025-09-07) | Rod: Bitmain's top of the line at "12 and a half or maybe even lower", with Bitmain claiming "nine and a half" for the S23 at the beginning of the year | [e085](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-07-e085.md) |
| e092 (2025-10-29) | S23 "supposed to be nine"; Canaan "just announced the a 16, which is 12 joules per terra hash"; Tyler: for heating the difference between nine and twelve doesn't matter, for on-grid miners it is a deal breaker | [e092](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-29-e092.md) |
| e098 (2025-12-13) | Scott: S23 targeting about 9.5 joules per terahash for release in Q1 2026; Bitdeer had claimed a 5 joules-per-terahash SealMiner by Q2 2025 but its best in Q4 2025 was 12.5 joules per terahash — investors filed a class action and the stock was down 41% | [e098](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-12-13-e098.md) |
| e098 (2025-12-13) | MicroBT M70 series (announced at Bitcoin MENA, per Tyler): five of six models need 380 to 480 volts three-phase, only one is two-twenty volt and none is one-twenty volt | [e098](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-12-13-e098.md) |
| e101 (2026-01-14) | The air-cooled S23 disappeared from Bitmain's website, with rumors that only "a couple thousand air cooled machines" were made; the hydro S23 reportedly not shipping until March. Scott suspected chip performance/yield; Rod suspected weak demand as public miners shift to AI (both speculation). Rod also relayed an unconfirmed rumor that MicroBT may exit Bitcoin mining hardware | [e101](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-01-14-e101.md) |
| e103 (2026-02-04) | "Bitmain just pulled the s 23 high air cooled" — hydro only; with MicroBT's 70 series mostly hydro/three-phase, few or no 240 volt miners remain | [e103](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-02-04-e103.md) |
| e105 (2026-02-18) | FutureBit Apollo three announced: 18 terahash, 13 joules per terahash, up to 400 watts (Scott believes Auradine chips, unconfirmed) | [e105](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-02-18-e105.md) |
| e107 (2026-03-11) | The S23 had been promised for "Q one, twenty twenty six" with twenty days left in the quarter; S23 hydros touted at "ten, eleven joules per terahash" | [e107](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-03-11-e107.md) |
| e112 (2026-04-15) | Rumor relayed by a host: the S23 series was delayed and partly canceled by a failed tape-out, "like a $20,000,000 oopsies" | [e112](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-04-15-e112.md) |
| e117 (2026-06-17) | At BTC Prague a Bitmain booth staffer told Scott the air-cooled S23 would ship "never" — by his count the second cancellation; S23 Hydro units were on display. The rumored S23 chip is transcribed "BM thirteen seventy three" | [e117](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-06-17-e117.md) |
| e125 (2026-09-07) | Bitmain's S23 XP is 8.9 joules per terahash, hydro-only and three-phase | [e125](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-07-e125.md) |
| e126 (2026-09-21) | At Bitcoin Asia in Hong Kong and a mining summit, Bitmain announced its next S23-generation chip and devoted slides to heat reuse; Tyler argued real hydronic heating needs boiler-like control, not a dry cooler | [e126 transcript](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-21-e126.md) |

> **Status: Outdated** (2026-10-10)
> The August–December 2025 expectation that the S23 would ship in January / Q1 2026 at about 9.5 joules per terahash ([e081](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-08-20-e081.md); [e098](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-12-13-e098.md)) did not hold for the air-cooled model, which was pulled and, per a Bitmain staffer in June 2026, will ship "never" ([e117](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-06-17-e117.md)). The hydro line continued, with the S23 XP read at 8.9 joules per terahash in September 2026 ([e125](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-07-e125.md)).

> **Status: Disputed** — S23 efficiency
> The quoted target moved between 9.5 (August and December 2025), "nine" (October 2025) and "ten, eleven" for the hydros (March 2026) ([e081](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-08-20-e081.md); [e092](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-29-e092.md); [e107](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-03-11-e107.md)). These are hosts recalling listings and marketing, not spec sheets; the only model-specific figure is the S23 XP at 8.9 joules per terahash ([e125](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-07-e125.md)).

Context on slowing efficiency gains: Scott argued in August 2025 that low-hanging chip-efficiency gains are gone and that "two nanometers" is largely a marketing term near physical limits ([e082](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-08-27-e082.md)); in May 2026 hosts relayed a rumor that TSMC is not ready for mining ASICs at two nanometers ([e115](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-05-27-e115.md)). Operators at TEMS 2026 were moving from immersion to hydro cooling — "No one no one is bullish on immersion anymore" ([e115](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-05-27-e115.md)).

## AI/HPC pivot of public miners (2025–2026)

- **August 2025.** Hosts said public miners diversify revenue via AI/HPC and merge mining (Rootstock and Slipstream named) ([e082](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-08-27-e082.md)).
- **September 2025.** Rob Warren's ImagineIF takeaway, as relayed: activist investors push large public miners toward AI/HPC to lift stock prices, and hashrate might decline as they shift; Foreman's customer off-site was dominated by HPC talk. Rod: HPC tenants paying "17 times, 20 times, or 10 times" the cost of electricity beat standalone grid mining; Scott noted Core Scientific investing in higher-tier HPC data centers ([e088](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-24-e088.md)).
- **October 2025.** An infrastructure vendor told Tyler hyperscalers turn to Bitcoin miners such as CleanSpark and TeraWulf because firms able to build two-gigawatt sites are booked years out, and that HPC switchgear is about nine times as large as a mining site's for equivalent power because of redundancy ([e092](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-29-e092.md)).
- **December 2025.** Hut 8 partnered with Google to double its power capacity across four new US sites on a fifteen-year, $7,000,000,000 data-center lease; Scott said miners' AI advantage is existing power purchase agreements and transformers ([e099](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-12-17-e099.md)).
- **March 2026.** Auradine appeared to rebrand as an AI company (name heard as "Valora"); Marathon, Bitdeer and Core Scientific were cited as pivoting toward AI; Scott expected chip vendors to need new customers as large miners buy fewer industrial machines ([e106](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-03-04-e106.md)).
- **May 2026.** At TEMS many miners were pivoting part of operations to AI/HPC; Tyler said Auradine "just vaporized" after selling hardware, so his commercial heating project would likely use WhatsMiners instead — supplier risk ([e115](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-05-27-e115.md)).
- **September 2026.** The peak-energy hypothesis (see Reading the numbers) ties the same trend to network energy use ([e126 transcript](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-21-e126.md)).

Rod's taxonomy of public miners (September 2025, opinion): bitcoin accumulators via financial engineering (he cited Mara), diversified operators with treasury teams (CleanSpark), and fiat/stock maximizers that may not hold bitcoin (Iren) ([e088](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-24-e088.md)).

## BIP 110 fork timeline (2026)

The BIP 110 soft fork, proposed by Luke Dashjr to restrict arbitrary data, ended in a short-lived chain split in August 2026. Dated reads from the transcripts (hosts were openly opposed; Eco's opinions were flagged as not necessarily the foundation's):

| Episode (published) | Event | Source |
|---|---|---|
| e092 (2025-10-29) | Eco relayed unverified reports of legal letters circulating to mining companies urging a switch to Knots; he criticized the BIP's language warning non-adopters of legal consequences | [e092](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-29-e092.md) |
| e112 (2026-04-15) | Matt Kratter urged followers to rent hashrate to signal for BIP 110 via version bits; hosts called rented signaling inauthentic and warned of a chain split without enforcing miners | [e112](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-04-15-e112.md) |
| e119 (2026-07-08) | Orange Surf's simulator: mandatory signaling at block nine six one six three two "expected around August 2026"; activation needs 55% of blocks in a difficulty epoch, then a 2,016 block lock-in; e.g. a window ending at block 961,631 means fork risk from 963,648. Wicked's dashboard showed 7.4 exahash signaling, "around point 5%" of hashrate | [e119](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-07-08-e119.md) |
| e122 (2026-08-03) | Mandatory activation due the following week with "two percent best case" signaling; OCEAN made its default non-DATUM stratum endpoint a BIP 110 node and opened a separate non-BIP 110 endpoint; OCEAN's dashboard showed between thirty and forty exahash across both | [e122](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-03-e122.md) |
| e123 (2026-08-10) | Activation began at the start of the signaling period (difficulty epoch four seventy seven) with zero mainnet blocks signaling; the BIP 110 chain forked off, got two blocks, and the main chain's "two seventy five block lead" made overtaking statistically impossible; the fork was mined essentially by Roughnecks alone. OCEAN reportedly offered refunds for hashrate redirected via its default endpoint | [e123](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-10-e123.md) |
| e124 (2026-08-17) | Luke Dashjr stepped down as OCEAN's CTO, followed by Mechanic on sabbatical; OCEAN's fork endpoint showed about 1.15 exahash with the last fork block five days earlier; the fork ("LukeCoin") targeted a September proof-of-work change to Blake2b | [e124](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-17-e124.md) |
| e125 (2026-09-07) | The fork got a total of four blocks before switching to Blake2b; its hashrate came from Roughnecks, reportedly largely rented | [e125](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-07-e125.md) |
| e126 (2026-09-21) | OCEAN's seven-day block share had bounced to 3.3% after the fork episode, then fell to 1.8%, though OCEAN's site showed 21.63 x a hash (about 2.3%) — the gap reflecting luck | [e126 transcript](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-21-e126.md) |

> **Status: Disputed** — fork block count
> The 2026-08-10 episode says the BIP 110 chain "only got two blocks in" by then ([e123](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-10-e123.md)); on 2026-08-17 a host floated "Five blocks now?" ([e124](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-17-e124.md)); on 2026-09-07 the hosts settled on "a total of four blocks" before the Blake2b switch ([e125](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-07-e125.md)). Best assessment: four, the latest on-air figure; none is checked against a block explorer.

## Pool concentration readings

Covered in depth in [Pool Centralization & FPPS](../pools/pool-centralization-and-fpps.md); the dated datapoints these sources carried:

| When | Claim | Source |
|---|---|---|
| April 2023 | No BS Bitcoin: Foundry had received 50% of all new hashrate, and had begun charging fees | [ep 013](../../raw/history/pod256/2023-04-14-pod256-013-state-of-the-network-news-tangents-home-miner-of.md) |
| April 2024 | mononautical: "A single custodian now controls the coinbase addresses of at least 9 pools, representing 47% of total hashrate." | [ep 044](../../raw/history/pod256/2024-04-19-pod256-044-state-of-the-network-news-tangents-home-miner-of.md) |
| April 2025 | B10C: top two pools ~35% and top six ~75% (2019–2022) → top two 55% and top six ~90% by December 2023; top six now mine ~95% of blocks | [newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md) |
| June 2025 | Antpool plus proxies roughly 40% of hashrate; Luxor templates matched AntPool's 1:1 | [newsletter, Jun 2025](../../raw/history/256f-newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md); [newsletter, Jul 2025](../../raw/history/256f-newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md) |
| September 2026 | Foundry 23.7%, AntPool 20.3%, F2Pool 16% (7-day) | [ep 126 transcript](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-21-e126.md) |

## Corporate and public-miner events

| When (source date) | Event | Source |
|---|---|---|
| 2022-12-03 | Compute North sold two data centers amid its bankruptcy; Marathon weighed a bid for its assets a week later | [ep 001](../../raw/history/pod256/2022-12-03-pod256-001-hashrate-down-14-from-ath-hashprice-at-atl-territ.md); [ep 002](../../raw/history/pod256/2022-12-10-pod256-002-miner-capitulation-and-compute-north-bankruptcy-d.md) |
| 2022-12-16 | A creditor offered Core Scientific capital to avoid bankruptcy | [ep 003](../../raw/history/pod256/2022-12-16-pod256-003-public-miners-against-the-ropes-esg-anti-bitcoin.md) |
| 2023-02-17 | Argo Blockchain's CEO stepped down after the Helios sale to Galaxy Digital | [ep 008](../../raw/history/pod256/2023-02-17-pod256-008-state-of-the-network-argo-blockchain-ceo-steps-do.md) |
| 2023-04-21 | Iris Energy went from 3.6 EH/s to 4.6 EH/s in a week; Intel discontinued Blockscale chips with no future generations | [ep 014](../../raw/history/pod256/2023-04-21-pod256-014-state-of-the-network-news-tangents-home-miner-of.md) |
| 2023-04-29 / 2023-05-05 | Marty Bent claimed more ASICs were sold in Russia than the USA; a Luxor RFQ report put North and South American buyers in the majority with Russia not on the list (Disputed — the sources are a tweet vs an RFQ dataset) | [ep 015](../../raw/history/pod256/2023-04-29-pod256-015-state-of-the-network-news-tangents-home-miner-of.md); [ep 016](../../raw/history/pod256/2023-05-05-pod256-016-state-of-the-network-news-tangents-home-miner-of.md) |
| 2023-05-13 | SEC subpoena to Marathon | [ep 017](../../raw/history/pod256/2023-05-13-pod256-017-state-of-the-network-news-tangents-home-miner-of.md) |
| 2023-05-28 | Upstream Data sued Crusoe for patent infringement; Mempool Accelerator launched | [ep 019](../../raw/history/pod256/2023-05-28-pod256-019-state-of-the-network-news-tangents-home-miner-of.md) |
| 2023-06-10 | Cathedra's off-grid partnership with 360 Mining (about 5MW of stranded-gas infrastructure) | [ep 021](../../raw/history/pod256/2023-06-10-pod256-021-state-of-the-network-news-tangents-home-miner-of.md) |
| 2023-06-17 | Blockstream announced plans for its own ASIC in Q3 2024 | [ep 022](../../raw/history/pod256/2023-06-17-pod256-022-state-of-the-network-news-tangents-home-miner-of.md) |
| 2023-07-01 | Riot–MicroBT deal, including an option on 99,840 immersion-cooled M56S+ and M56++ units | [ep 024](../../raw/history/pod256/2023-07-01-pod256-024-state-of-the-network-news-tangents-home-miner-of.md) |
| 2024-02-02 | Swan announced 4.5Eh online with another 3.5Eh incoming | [ep 034](../../raw/history/pod256/2024-02-02-pod256-034-home-open-source-mining-initiative-state-of-the-n.md) |
| 2024-03-01 / 2024-03-15 | Riot bought 31,500 Miners from MicroBT for Rockdale; invested in Reformed Energy | [ep 038](../../raw/history/pod256/2024-03-01-pod256-038-state-of-the-network-news-tangents-home-miner-of.md); [ep 040](../../raw/history/pod256/2024-03-15-pod256-040-state-of-the-network-news-tangents-home-miner-of.md) |
| 2024-11-11 / 2025-09-24 | Core Scientific shifting to AI servers; possible HPC/AI pivots by large public miners | [ep 057](../../raw/history/pod256/2024-11-11-pod256-057-from-sweden-to-silicon-bitcoin-s-global-journey.md); [ep 088](../../raw/history/pod256/2025-09-24-pod256-088-freedom-tech-in-action-open-miners-sovereign-home.md) |
| August 14, 2025 | Proto launched Rig: up to 819 Th/s from nine hashboards, tool-less hot-swappable bays | [newsletter, Sep 2025](../../raw/history/256f-newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md) |
| September 2, 2025 | 256 Foundation took possession of 256,000 Intel BZM2 chips donated by Proto | [newsletter, Oct 2025](../../raw/history/256f-newsletter/2025-10-28-assembling-freedom-10.md) |
| 2025-11-05 | Canaan published code on GitHub (CGMiner, a RISC-V K230 SDK), raising a BSD-3 vs GPLv3 question | [ep 093](../../raw/history/pod256/2025-11-05-pod256-093-decentralize-or-die-open-miners-pool-payouts-and.md) |
| 2025-12-03 / 2025-12-13 | Reported federal probe of Bitmain; Bitdeer missed its ASIC roadmap and faced an investor lawsuit; MicroBT's M70 line pushes three-phase units | [ep 097](../../raw/history/pod256/2025-12-03-pod256-097-from-lab-to-hash-ember-one-libre-board-and-an-ope.md); [ep 098](../../raw/history/pod256/2025-12-13-pod256-098-from-mauritius-to-modular-miners-open-source-bitc.md) |
| 2026-01-14 / 2026-02-04 | Rumoured air-cooled Bitmain S23; OEMs moving to hydro-only, three-phase units with fewer 240V options; Tether open-sourced its MOS fleet platform | [ep 101](../../raw/history/pod256/2026-01-14-pod256-101-hydrapool-hashdash-and-the-telehash-playbook-open.md); [ep 103](../../raw/history/pod256/2026-02-04-pod256-103-closed-source-is-retarded-building-bitcoin-miners.md) |
| 2026-05-13 | 256 Foundation won a $100,000 grant through MARA Foundation's community vote | [ep 114](../../raw/history/pod256/2026-05-13-pod256-114-open-source-wins-in-vegas-100k-boost-doomaxe-demo.md) |
| 2026-06-17 | Braiins launched a BraiinsForge initiative with renewed open-source signals | [ep 117](../../raw/history/pod256/2026-06-17-pod256-117-decentralizing-the-dark-corner-building-an-open-m.md) |
| 2026-08-14 / 2026-08-18 | First commercial product on Mujina firmware (solar-following power control) — see Disputed below | [256F website PR #12](../../raw/history/256f-org/2026-08-14-github-website-pr-12-the-ry3t-nova-first-product-built-on-mu.md); [ep 124](../../raw/history/pod256/2026-08-18-pod256-124-mining-forks-firmware-red-teams-and-the-future-of.md) |
| 2026-08-18 | Luke Dashjr departed as CTO of Ocean Mining amid the BIP 110 controversy and a "LukeCoin" proof-of-work fork | [ep 124](../../raw/history/pod256/2026-08-18-pod256-124-mining-forks-firmware-red-teams-and-the-future-of.md) |

> **Status: Disputed** — Riot or RY3T?
> The episode 124 show notes credit a solar-responsive mining product from Riot built on Mujina ([ep 124](../../raw/history/pod256/2026-08-18-pod256-124-mining-forks-firmware-red-teams-and-the-future-of.md)). The 256 Foundation newsroom says the first commercial Mujina product is the Nova from RY3T, an energy hardware company in Wil, Switzerland ([RY3T Nova](../../raw/history/256f-org/256foundation-org-newsroom-ry3t-nova.md)), and the episode 126 transcript thanks "our friends at Riot over in Switzerland" ([ep 126 transcript](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-09-21-e126.md)). Best assessment: "Riot" is a mis-hearing of RY3T, not Riot Platforms. See [Mujina](../firmware/mujina.md).

## Policy and legal events

| When (source date) | Event | Source |
|---|---|---|
| 2022-12-10 | ERCOT/Texas mining issues; "is nuclear a LARP?" | [ep 002](../../raw/history/pod256/2022-12-10-pod256-002-miner-capitulation-and-compute-north-bankruptcy-d.md) |
| 2023-01-21 | Sen. Elizabeth Warren's December 14 bill called "full overreach"; in April 2023 she sought information on all miners | [ep 004](../../raw/history/pod256/2023-01-21-pod256-004-recap-nashville-energy-mining-summit-2023-state-o.md); [ep 015](../../raw/history/pod256/2023-04-29-pod256-015-state-of-the-network-news-tangents-home-miner-of.md) |
| 2023-03-04 | Griid's curtailment letter to the TVA (with Harry Sudock) | [ep 010](../../raw/history/pod256/2023-03-04-pod256-010-state-of-the-network-news-tangents-home-miner-of.md) |
| 2023-03-18 / 2024-03-15 | Biden administration's proposed 30% tax on electricity used for bitcoin mining; a year later industry said it would "destroy" US mining | [ep 012](../../raw/history/pod256/2023-03-18-pod256-012-state-of-the-network-news-tangents-home-miner-of.md); [ep 040](../../raw/history/pod256/2024-03-15-pod256-040-state-of-the-network-news-tangents-home-miner-of.md) |
| 2023-04-21 | Mining tax hike of 6,000% (headlined as EU; the linked CoinDesk story is about Sweden) | [ep 014](../../raw/history/pod256/2023-04-21-pod256-014-state-of-the-network-news-tangents-home-miner-of.md) |
| 2024-05-24 | Show notes start carrying Samourai Wallet defense donation links | [ep 046](../../raw/history/pod256/2024-05-24-pod256-046-no-holds-barred-w-special-guest-luke-dashjr-chair.md) |
| 2025-08-01 | Samourai developers' plea cut maximum exposure from 25 years to five, with $6,000,000 in fines; sentencing set for November | [ep 080](../../raw/history/pod256/2025-08-01-pod256-080-the-chilling-effect-legal-risks-in-privacy-softwa.md) |
| 2025-10-22 | 256 Foundation/Skot opposed third-party USPTO filings on the Bitaxe mark | [ep 091](../../raw/history/pod256/2025-10-22-pod256-091-hash-heat-and-hardware-libreboard-mujina-and-the.md) |
| 2025-11-05 | FCC/UL/CE/RoHS certification and insurance described as a gauntlet for open hardware and heaters | [ep 093](../../raw/history/pod256/2025-11-05-pod256-093-decentralize-or-die-open-miners-pool-payouts-and.md) |
| 2025-11-27 | Keonne Rodriguez on his five-year federal sentence and the "unlicensed money transmission" theory, which he argued could reach developers, node operators and even miners | [ep 096](../../raw/history/pod256/2025-11-27-pod256-096-from-open-source-to-federal-sentence-the-governme.md) |
| 2025-12-17 → 2026-03-18 | Pardon petition push (incl. a reported acknowledgment from President Trump); by March 2026 both developers were serving federal sentences | [ep 099](../../raw/history/pod256/2025-12-17-pod256-099-code-is-not-crime-samourai-petition-pool-scams-an.md); [newsletter, Dec 2025](../../raw/history/256f-newsletter/2025-12-22-assembling-freedom-12.md); [ep 108](../../raw/history/pod256/2026-03-18-pod256-108-from-mixers-to-miners-why-samourai-matters-for-al.md) |
| 2026-07-08 → 2026-08-18 | BIP 110 debate: what counts as "spam", miner- vs user-activated soft forks; then the Ocean fallout | [ep 119](../../raw/history/pod256/2026-07-08-pod256-119-soft-forks-censorship-risks-and-open-source-bitco.md); [ep 123](../../raw/history/pod256/2026-08-10-pod256-123-coldcard-fallout-mining-firmware-and-the-bip-110.md); [ep 124](../../raw/history/pod256/2026-08-18-pod256-124-mining-forks-firmware-red-teams-and-the-future-of.md) |
| 2026-08-03 / 2026-09-08 | Coldcard entropy exploit; Liquid sidechain exploit | [ep 122](../../raw/history/pod256/2026-08-03-pod256-122-weak-entropy-broken-trust-and-the-90m-coldcard-fa.md); [ep 125](../../raw/history/pod256/2026-09-08-pod256-125-why-open-source-and-ai-are-colliding-in-bitcoin-m.md) |

## Conferences and community events

| When | Event | Source |
|---|---|---|
| January 2023 | Nashville Energy & Mining Summit 2023 (NEMS) recapped | [ep 004](../../raw/history/pod256/2023-01-21-pod256-004-recap-nashville-energy-mining-summit-2023-state-o.md) |
| September 2023 | Telehash idea grew out of conversations at the Global Bitcoin Summit in Nashville | [ep 029](../../raw/history/pod256/2023-09-21-pod256-029-pod-256-s-telehash-uniting-bitcoiners-for-a-cause.md) |
| January 2024 | NEMS 2024 recap | [ep 033](../../raw/history/pod256/2024-01-25-pod256-033-nems-2024-recap-state-of-the-network-tangents-new.md) |
| December 2024 | Africa Bitcoin Conference (Nairobi trip) | [ep 058](../../raw/history/pod256/2024-12-26-pod256-058-from-nairobi-to-nashville-rise-of-open-source-bit.md) |
| Early 2025 | Telehash #1: over 350 entities pointed as much as 1.12Eh/s at peak; about 800 Ph/s when block 881423 was found | [newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md); [ep 060](../../raw/history/pod256/2025-02-06-pod256-060-we-hit-a-block-behind-the-scenes.md) |
| May 2025 | First Texas Energy and Mining Summit (TEMS), with Telehash #2 in Austin | [ep 071](../../raw/history/pod256/2025-05-16-pod256-071-reviewing-the-first-ever-texas-energy-and-mining.md); [newsletter, Jun 2025](../../raw/history/256f-newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md) |
| July 2025 | ATL BitLab mining hackathon | [ep 077](../../raw/history/pod256/2025-07-14-pod256-077-battle-of-the-minehackers-with-stephen-delorme.md) |
| August 13–14, 2025 | Proto Rig launch event, Dalton, Georgia (POD256 live both nights) | [ep 084](../../raw/history/pod256/2025-09-08-pod256-084-proto-launch-party-live-night-1.md); [ep 085](../../raw/history/pod256/2025-09-08-pod256-085-proto-launch-party-live-night-2.md) |
| September 2025 | ImagineIF debrief | [ep 088](../../raw/history/pod256/2025-09-24-pod256-088-freedom-tech-in-action-open-miners-sovereign-home.md) |
| October 2025 | TabConf updates | [ep 090](../../raw/history/pod256/2025-10-15-pod256-090-make-every-meetup-a-pool-stratum-v2-hole-punching.md) |
| November 2025 | Bitcoin Veterans telehash peaked near 98.5 PH; Bitcoin++ Durham on Nov 15, where the Mujina developer preview was announced | [ep 094](../../raw/history/pod256/2025-11-12-pod256-094-pplns-pick-and-place-and-pardon-a-deep-dive-into.md); [ep 093](../../raw/history/pod256/2025-11-05-pod256-093-decentralize-or-die-open-miners-pool-payouts-and.md); [ep 095](../../raw/history/pod256/2025-11-19-pod256-095-open-source-or-bust-mujina-miner-firmware-wars-an.md) |
| December 2025 | African Bitcoin Conference in Mauritius (Skot on open-source mining) | [ep 098](../../raw/history/pod256/2025-12-13-pod256-098-from-mauritius-to-modular-miners-open-source-bitc.md) |
| January 2026 | NEMS and Telehash #3 (first time all four core projects ran together) | [ep 102](../../raw/history/pod256/2026-01-30-pod256-102-why-open-firmware-wins-a-post-nems-debrief-with-m.md); [Telehash page](../../raw/history/256f-org/256foundation-org-telehash.md) |
| Feb 27–28, 2026 | Heatpunk Summit 2026, Denver (150+ builders); the 2025 edition "Undermine" drew ~150 | [newsletter #18](../../raw/history/256f-newsletter/2026-03-04-assembling-freedom-18-high-signal-in-the-hashtub-workshops-o.md); [heatpunks.org summit](../../raw/history/256f-org/heatpunks-org-summit.md) |
| April–May 2026 | Bitcoin 2026, Las Vegas: two 256 Foundation panels incl. "Open Sourcing the Bitcoin Mining Ecosystem" (Monday, April 27) | [ep 109](../../raw/history/pod256/2026-03-25-pod256-109-hashrate-heat-home-sovereignty-and-the-open-sourc.md); [forum: Vegas panels](../../raw/history/256f-org/2026-05-14-forum-bitcoin-las-vegas-2026-256f-panels.md) |
| May 19, 2026 | Telehash #4 at Bitcoin Park Austin: average 1.32 EH/s, peak 2.495 EH/s, no block | [forum: Telehash #4](../../raw/history/256f-org/2026-04-26-forum-telehash-4-may-19th-bitcoin-park-austin.md); [ep 115](../../raw/history/pod256/2026-05-27-pod256-115-from-bitaxe-to-exahash-inside-hydropool-s-record.md) |
| June 2026 | Oslo Freedom Forum and BTC Prague; BTC++ Nairobi mining workshop | [ep 117](../../raw/history/pod256/2026-06-17-pod256-117-decentralizing-the-dark-corner-building-an-open-m.md); [ep 118](../../raw/history/pod256/2026-06-24-pod256-118-from-nairobi-to-mugena-teaching-bitcoin-mining-wi.md) |
| September 12, 2026 | First in-person 256 Foundation fundraiser, Presidio Bitcoin, San Francisco | [Presidio fundraiser](../../raw/history/256f-org/256foundation-org-newsroom-presidio-bitcoin-fundraiser.md) |
| September 2026 | Midwest Bitcoin Summit, Columbus | [ep 127](../../raw/history/pod256/2026-09-28-pod256-127-self-hosted-ai-and-open-mining-tools-for-a-more-s.md) |

## Contradictions & Open Questions

- Epoch 411 difficulty (2024-02-16 notes), August 2025 ASIC tier prices, the competing claims to the largest drop since the China ban and Riot vs RY3T are recorded as Disputed above.
- The early-2026 difficulty drop has no sourced percentage in these raws.
- The 2026 snapshot comes from a machine transcript; spoken numbers ("936", "one thirty two point seven six trillion") should be checked against a block explorer before reuse.

## See Also

- [POD256 Podcast](../history/pod256-podcast.md)
- [Pool Centralization & FPPS](../pools/pool-centralization-and-fpps.md)
- [Open-source solo blocks](../history/open-source-solo-blocks.md)
- [Open Mining Economics](../economics/open-mining-economics.md)
- [Hashrate Heating Economics](../economics/hashrate-heating-economics.md)
- [On-demand hashrate](../hashrate-market/on-demand-hashrate.md)
- [Bitmain ASIC reference](../hardware/bitmain-asic-reference.md)
- [Mining firmware security](mining-firmware-security.md)
- [256 Foundation Organization](../history/256-foundation-organization.md)
- [256 Foundation community timeline](../history/256f-community-timeline.md)
