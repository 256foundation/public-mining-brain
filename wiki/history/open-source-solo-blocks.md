# Solo Blocks Found by Open-Source & Home Miners

> Sources: mempool.space REST API on-chain verification (run 2026-10-07); press and vendor reports compiled 2026-10-07 (CoinTelegraph, Decrypt, CoinDesk, crypto.news, Umbrel community forum, D-Central); ckpool solo block log (2025-03-10); @Public_Pool_BTC, @osmu_global and @256FOUNDATION posts on X, 2024 → 2026; 256 Foundation newsletter, 2025-05 → 2026-04; 256 Foundation Telehash page; POD256 episode notes, 2023 → 2026; OpenSats Bitaxe impact report (2026-04-21)
> Raw: [mempool.space on-chain verification](../../raw/history/256f-research/2026-10-07-mempool-onchain-block-verification.md); [Bitaxe solo-block research notes](../../raw/history/256f-research/2026-10-07-bitaxe-open-source-mining-blocks-found.md); [press and media research](../../raw/history/256f-research/2026-10-07-press-media-talks-research.md); [ckpool block log 887212](../../raw/hardware/bitaxe-osmu/2025-03-10-ckpool-bitaxe-ultra-block-log.md); [X: @Public_Pool_BTC posts](../../raw/history/256f-research/2026-10-07-x-notable-public-pool.md); [256F Telehash page](../../raw/history/256f-org/256foundation-org-telehash.md)
> Updated: 2026-10-09
> As-Of: 2026-10-09
> Status: Draft

## Overview

Since July 2024, small open-source miners — Bitaxes, NerdQaxe-family boards and other home rigs — have repeatedly won full Bitcoin blocks by solo mining, either through Solo CKPool or through a Public Pool instance (hosted or self-hosted on a home node). This page keeps a table of those blocks that have been checked against the chain, separates what the chain proves (height, time, pool coinbase tag) from what only press or pool operators claim (the hardware), and records the claims that do not survive checking. As of 2026-10-07 there were 12 on-chain-verified solo blocks from the open-source mining era: 4 relayed by Solo CKPool with press Bitaxe attribution and 8 tagged by Public Pool ([mempool.space verification](../../raw/history/256f-research/2026-10-07-mempool-onchain-block-verification.md)). The odds for any single small miner are tiny; the steady trickle of wins comes from the very large number of devices hashing.

## What "verified" means here

The coinbase transaction of a block records the pool that built it (its tag) and where the reward went. It does **not** record which device found the winning nonce. So every row below has two layers:

- **On-chain (authoritative):** height, UTC timestamp, coinbase tag, first coinbase output — pulled from mempool.space on 2026-10-07.
- **As published (unverified):** the hardware, from press reports, pool posts or the winner's own account.

Where earlier notes and the chain disagree on a timestamp, the on-chain value wins ([mempool.space verification](../../raw/history/256f-research/2026-10-07-mempool-onchain-block-verification.md)).

## Verified blocks

| Height | UTC (on-chain) | Coinbase tag | First output (vout 0) | Hardware as published |
|---|---|---|---|---|
| 853742 | 2024-07-24 17:43:43 | `/solo.ckpool.org/` | 312,864,161 sats | First widely reported Bitaxe block; reward 3.192 BTC; Solo CKPool's 290th solo block. Hashrate disputed (see below) |
| 887212 | 2025-03-10 19:22:04 | `/solo.ckpool.org/` | — | Worker `bitaxeultra4` at 486G (1-day) in an account totalling about 3.22T; ckpool's dev: "with a 480GH bitaxe" ([ckpool log](../../raw/hardware/bitaxe-osmu/2025-03-10-ckpool-bitaxe-ultra-block-log.md)) |
| 888989 | 2025-03-23 00:30:28 | `Public Pool on Umbrel` | 315,188,086 sats | First self-hosted Public Pool block; Umbrel forum analysis: "likely a Bitaxe" and "not a NerdMiner" |
| 889975 | 2025-03-29 13:12:09 | `/solo.ckpool.org/` | — | Press: stock Bitaxe Gamma |
| 920440 | 2025-10-23 19:32:45 | `Public Pool on Umbrel` | 314,115,228 sats | Six NerdQaxe++ plus one Avalon Q, ~130 TH/s total; winning board a NerdQaxe++ rev6; payout about 3.14 BTC |
| 924569 | 2025-11-21 14:13:06 | `/solo.ckpool.org/` | — | Press: Bitaxe Gamma-class (~1.2 TH/s per Decrypt) |
| 928985 | 2025-12-22 14:50:14 | `Public Pool on Umbrel` | 312,788,664 sats | Not published |
| 937218 | 2026-02-18 11:22:29 | `Public Pool on Umbrel` | 314,345,306 sats | Not published |
| 943466 | 2026-04-03 06:07:40 | `Public-Pool` | — | First block on the hosted Public Pool; NerdOctAxe / NerdQaxe (disputed) |
| 947073 | 2026-04-28 22:52:18 | `Public Pool on Umbrel` | 314,143,172 sats | Not published (an r/BitAxe thread the same day) |
| 948146 | 2026-05-06 09:28:35 | `Public Pool on Umbrel` | 315,458,553 sats | Not published |
| 957382 | 2026-07-10 03:30:34 | `Public-Pool` | 313,823,506 sats | Hosted Public Pool's second block, "By a lone Bitaxe" |

Row sources: on-chain columns from [mempool.space verification](../../raw/history/256f-research/2026-10-07-mempool-onchain-block-verification.md); hardware from [Bitaxe solo-block research](../../raw/history/256f-research/2026-10-07-bitaxe-open-source-mining-blocks-found.md), [press research](../../raw/history/256f-research/2026-10-07-press-media-talks-research.md), [Public Pool on X](../../raw/history/256f-research/2026-10-07-x-notable-public-pool.md) and [open-source mining posts on X](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md). "—" means the verification file did not record that output.

mempool.space's own Public Pool profile (pool id 161) lists exactly these 8 Public Pool blocks, matching the regexes `Public-Pool` and `Public Pool on Umbrel` ([mempool.space verification](../../raw/history/256f-research/2026-10-07-mempool-onchain-block-verification.md)). For pool-side detail see [Public Pool](../pools/public-pool.md).

## Other reported solo and home-miner blocks (not independently verified here)

These are pool-announced or community-announced wins that the verification run did not cover. The heights come from the cited posts; check them on-chain before reuse.

| Height / ordinal | Date | Pool | Miner as reported | Source |
|---|---|---|---|---|
| 274th Solo CK block | posted 2023-05-28 | Solo CKPool | A miner with 750Th | [POD256 #019](../../raw/history/pod256/2023-05-28-pod256-019-state-of-the-network-news-tangents-home-miner-of.md) |
| 881423 | posted 2025-03-22 | 256 Foundation Telehash #1 (pool disputed, see below) | 350+ entities, up to 1.12Eh/s at peak, about 800 Ph/s when found; reward 3.146 BTC | [256F Telehash page](../../raw/history/256f-org/256foundation-org-telehash.md); [newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md) |
| 888737 | posted 2025-03-21 | Solo (FutureBit Apollo) | A solo miner with a FutureBit Apollo | [256F on X, 2025 H1](../../raw/history/256f-research/2026-10-07-x-256foundation-2025-h1.md) |
| 891952 | April 11 (2025) | Solo CKPool | ~230Th/s; 3.11 BTC | [newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md) |
| 903883 (Solo CK's 301st) | July 3 (2025) | Solo CKPool, EU server | ~2.3Ph/s home-sized miner | [newsletter, Jul 2025](../../raw/history/256f-newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md); [newsletter, Aug 2025](../../raw/history/256f-newsletter/2025-08-18-is-open-source-communism.md) |
| Solo CK's 303rd | July 26 (2025) | Solo CKPool, EU server | 49Th/s | [newsletter, Aug 2025](../../raw/history/256f-newsletter/2025-08-18-is-open-source-communism.md) |
| 910,440 | August 17 (2025) | Solo CKPool (its 12th of the year) | 9Ph/s | [newsletter, Sep 2025](../../raw/history/256f-newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md) |
| Solo CK's 307th | September 7 (2025) | Solo CKPool | 200Th/s account; winning worker "Blockbuster" | [newsletter, Oct 2025](../../raw/history/256f-newsletter/2025-10-28-assembling-freedom-10.md) |
| Two blocks, early April 2026 | posted 2026-04-11 | Solo CKPool | Old Antminers | [newsletter, Apr 2026](../../raw/history/256f-newsletter/2026-04-11-assembling-freedom-23.md) |
| One block, early April 2026 | posted 2026-04-11 | Node Runners pool | ~4.8 TH/s NerdQaxe++ | [newsletter, Apr 2026](../../raw/history/256f-newsletter/2026-04-11-assembling-freedom-23.md) |

Notes: 903883 and the 301st Solo CK block are the same event — both newsletters link the same ckpool post. POD256 also reported a fully self-sovereign block by a FutureBit Apollo miner (published 2024-11-11) without a height ([POD256 #057](../../raw/history/pod256/2024-11-11-pod256-057-from-sweden-to-silicon-bitcoin-s-global-journey.md)).

## Odds framing

Solo odds scale with your share of network hashrate, so published figures are only comparable at similar difficulty:

| Hashrate | Odds as published | Context | Source |
|---|---|---|---|
| ~500 GH/s | "1 in 1.1 billion" per 10 minutes | vs ~552 EH/s network, July 2024 (CoinTelegraph) | [Bitaxe solo-block research](../../raw/history/256f-research/2026-10-07-bitaxe-open-source-mining-blocks-found.md) |
| ~3 TH/s | 1 in 1.2 MILLION per day; once every 3500 YEARS on average | ckpool's dev on block 853742 | [Bitaxe solo-block research](../../raw/history/256f-research/2026-10-07-bitaxe-open-source-mining-blocks-found.md) |
| 18.5 TH/s | 1-in-28,000 daily | Public Pool's first hosted block, April 2026 | [newsletter, Apr 2026](../../raw/history/256f-newsletter/2026-04-11-assembling-freedom-23.md) |
| 200Th/s | about 1 in 36,000 per day | Solo CK's 307th, September 2025 | [newsletter, Oct 2025](../../raw/history/256f-newsletter/2025-10-28-assembling-freedom-10.md) |
| 2.3Ph/s | roughly 1 in 2,800 per day | Solo CK's 301st, July 2025 | [newsletter, Aug 2025](../../raw/history/256f-newsletter/2025-08-18-is-open-source-communism.md) |

> **Status: Disputed** — the 18.5 TH/s odds figure
> The April 2026 newsletter gives one 18.5 TH/s miner 1-in-28,000 daily odds, but the October 2025 newsletter gives a 200Th/s miner — over ten times the hashrate — only about 1 in 36,000. Network difficulty was in the same range in both periods (Public Pool cited a target of ~120T in February 2026 — [Public Pool on X](../../raw/history/256f-research/2026-10-07-x-notable-public-pool.md)), so both cannot be right. The 2026 weekly newsletters are summaries of podcast episodes and are lower-confidence than the 2025 monthlies. Best assessment: the 18.5 TH/s figure understates the long odds by roughly an order of magnitude; trust the 2025 ckpool-sourced figures.

Aggregate claims, by date: Bitcointalk (2025-10-24) — "Users who host Public Pool themselves have found 2 blocks in 7 months" ([Bitaxe solo-block research](../../raw/history/256f-research/2026-10-07-bitaxe-open-source-mining-blocks-found.md)); Skot in OpenSats' 2026-04-21 report — self-sovereign miners had solo mined "at least six blocks" ([OpenSats report](../../raw/hardware/bitaxe-osmu/2026-04-21-opensats-bitaxe-impact-report.md)); CoinDesk (2026-07-14) — 24 solo blocks in the prior 12 months, +41% YoY; CoinTelegraph called 957382 the 12th hobby-level block of 2026 ([press research](../../raw/history/256f-research/2026-10-07-press-media-talks-research.md)). These count different sets (self-hosted only; Bitaxe only; all solo) and should not be compared directly with the 12-block verified tally above.

For the economics of running small miners as lottery tickets or heaters, see [Open Mining Economics](../economics/open-mining-economics.md).

## Disputed and corrected claims

> **Status: Disputed** — block 868790 (claimed "October 2024", Bitaxe Gamma on Public Pool)
> A D-Central blog claims a ~1.2 TH/s Bitaxe Gamma found 868790 on Public Pool ([Bitaxe solo-block research](../../raw/history/256f-research/2026-10-07-bitaxe-open-source-mining-blocks-found.md)). On-chain, 868790 (2024-11-04 06:06:05 UTC) has the coinbase tag `/ViaBTC/`, mempool.space attributes it to ViaBTC, and it is absent from Public Pool's block list ([mempool.space verification](../../raw/history/256f-research/2026-10-07-mempool-onchain-block-verification.md)). Best assessment: **not** a Public Pool or Bitaxe solo block; the claim is unsupported.

> **Status: Disputed** — which pool found Telehash #1's block 881423
> The 256 Foundation's Telehash and community pages say participants pointed hashrate at "our Hydrapool instance" ([256F Telehash page](../../raw/history/256f-org/256foundation-org-telehash.md); [256F community page](../../raw/history/256f-org/256foundation-org-community.md)). But the May 2025 newsletter says the first Hydra Pool version was built "specifically for the upcoming Telehash #2" ([newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md)); the Foundation posted that it ran a FutureBit Apollo as its node and stratum server ([256F on X, 2025 H1](../../raw/history/256f-research/2026-10-07-x-256foundation-2025-h1.md)); and POD256 #100 describes an Apollo-powered solo pool that briefly wrangled an exahash ([POD256 #100](../../raw/history/pod256/2025-12-31-pod256-100-dismantling-the-black-box-hydra-pool-libre-board.md); [newsletter, Jan 2026](../../raw/history/256f-newsletter/2026-01-14-assembling-freedom-13.md)). Best assessment: 881423 was found on a solo pool run on a FutureBit Apollo; the website's Hydrapool wording is retroactive branding. See [Hydrapool](../pools/hydrapool.md).

> **Status: Disputed** — hashrate behind block 853742
> ckpool's developer called the winner "only a tiny 3TH" miner (~3 TH/s); Altair Technology and CoinTelegraph reported a ~500 GH/s device ([Bitaxe solo-block research](../../raw/history/256f-research/2026-10-07-bitaxe-open-source-mining-blocks-found.md); [press research](../../raw/history/256f-research/2026-10-07-press-media-talks-research.md)). The exact hardware generation was never identified. Best assessment: a Bitaxe-class device on an account of roughly 3 TH/s; the same pattern is documented for 887212, where a ~480 GH/s Bitaxe Ultra worker won inside a ~3.3 TH account ([ckpool log](../../raw/hardware/bitaxe-osmu/2025-03-10-ckpool-bitaxe-ultra-block-log.md)).

> **Status: Disputed** — the miner behind block 943466
> OSMU called it "the first known block of a NerdOctAxe" ([OSMU on X](../../raw/history/256f-research/2026-10-07-x-osmu-global.md)); the 256 Foundation newsletter says a ~18.5 TH/s NerdQaxe ([newsletter, Apr 2026](../../raw/history/256f-newsletter/2026-04-11-assembling-freedom-23.md)). Best assessment: NerdQaxe-family (NerdOctAxe-class) hardware; exact model unverified.

> **Status: Outdated** (2026-10-07) — timestamps from earlier notes
> The research notes gave 853742 at ~11:43 UTC and 888989 on 2025-03-22 at 20:30:28 UTC, and listed later Public Pool blocks several hours earlier than on-chain (e.g. 928985 at 09:50:14); press dated 889975 to 2025-03-23. The chain says 853742 at 17:43:43, 888989 at 2025-03-23 00:30:28, 928985 at 14:50:14 and 889975 on 2025-03-29. The offsets look like explorer local-time display; use the on-chain values ([mempool.space verification](../../raw/history/256f-research/2026-10-07-mempool-onchain-block-verification.md); [Bitaxe solo-block research](../../raw/history/256f-research/2026-10-07-bitaxe-open-source-mining-blocks-found.md); [press research](../../raw/history/256f-research/2026-10-07-press-media-talks-research.md)).

## How to verify a block yourself

The 2026-10-07 run used the public mempool.space REST API ([mempool.space verification](../../raw/history/256f-research/2026-10-07-mempool-onchain-block-verification.md)):

```bash
curl -s https://mempool.space/api/block-height/{HEIGHT}        # height -> block hash
curl -s https://mempool.space/api/block/{HASH}                 # timestamp, height
curl -s https://mempool.space/api/block/{HASH}/txid/0          # coinbase txid
curl -s https://mempool.space/api/tx/{TXID}                    # decode vin[0].scriptsig hex -> ASCII for the tag; read vout[0]
curl -s https://mempool.space/api/v1/mining/pool/publicpool          # pool profile + attribution regexes
curl -s https://mempool.space/api/v1/mining/pool/publicpool/blocks   # pool's attributed blocks
```

Tips: convert the Unix timestamp with an explicit UTC zone; a pool tag proves the pool, never the hardware; and an explorer's "miner" label is just the regex match on that tag. Some endpoints failed in the run (`/blocks/all` returned HTTP 500; the 1-year hashrate endpoint 404), so prefer the per-pool block list.

## See Also

- [Public Pool](../pools/public-pool.md)
- [Hydrapool](../pools/hydrapool.md)
- [Pool Payout Schemes](../pools/pool-payout-schemes.md)
- [Bitaxe Models](../hardware/bitaxe-models.md)
- [256 Foundation Community Timeline](256f-community-timeline.md)
- [256 Foundation Organization](256-foundation-organization.md)
- [Open Mining Economics](../economics/open-mining-economics.md)
- [Network State 2022–2026](../industry/network-state-2022-2026.md)
