# Pool Centralization & FPPS

> Sources: 256 Foundation monthly newsletter, 2025-05 → 2025-10 (citing B10C, boerst/stratum.work, mononautical, Braiins, OrangeSurf); 256 Foundation FAQ (captured 2026-10-07); POD256 episode notes, 2023-02 → 2026-04; @Public_Pool_BTC and @skot9000 posts on X, 2025; bitaxeorg/ESP-Miner GitHub issues, 2024-04 → 2025-08; hydrapool.org (captured 2026-10-07); 256 Foundation Telegram group, 2024-04
> Raw: [newsletter, May 2025 (B10C data)](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md); [newsletter, Jun 2025 (FPPS and proxies)](../../raw/history/256f-newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md); [newsletter, Jul 2025 (Luxor/AntPool)](../../raw/history/256f-newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md); [newsletter, Sep 2025 (invalid jobs)](../../raw/history/256f-newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md); [256F FAQ](../../raw/history/256f-org/256foundation-org-faq.md); [POD256 #044](../../raw/history/pod256/2024-04-19-pod256-044-state-of-the-network-news-tangents-home-miner-of.md)
> Updated: 2026-10-09
> As-Of: 2026-10-09
> Status: Draft

## Overview

A pool decides two things that matter for Bitcoin beyond its own customers: **which transactions go into the block template** its miners hash on, and **who holds the reward** until it is paid out. Most hashrate today sits in a handful of pools paying Full Pay Per Share (FPPS), a scheme that pays a steady amount per share and therefore needs a large bitcoin reserve to ride out bad luck. Pools that cannot carry that reserve end up as proxies bankrolled by a larger pool — in 2025 reporting, mostly Antpool — so template control and custody concentrate further than the pool names on a block explorer suggest. This page collects the dated evidence for that picture (concentration statistics, proxy-pool evidence, invalid-job incidents), the 256 Foundation's editorial position, and the tools that let anyone check what pools are doing. Every figure is a snapshot; read the dates.

For how FPPS, PPLNS and TIDES pay out — and why FPPS can still be the right call for an on/off heater — see [Pool Payout Schemes](pool-payout-schemes.md) and [Pool Choice for Heat Miners](pool-choice-for-heat-miners.md).

## Concentration data (dated)

| As of | Claim | Who said it | Source |
|---|---|---|---|
| 2019–2022 | Top two pools ~35% of hashrate; top six ~75% | B10C (Mining Centralization Index article, April 15, 2025) | [newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md) |
| December 2023 | Top two 55%; top six ~90% | B10C | same |
| April 2025 | Six pools mine more than 95% of blocks | B10C | same |
| Spring 2023 | Foundry received 50% of all new hashrate and began charging fees | No BS Bitcoin, via POD256 #013 (2023-04-14) | [POD256 #013](../../raw/history/pod256/2023-04-14-pod256-013-state-of-the-network-news-tangents-home-miner-of.md) |
| April 2024 | One custodian controls the coinbase addresses of at least 9 pools, representing 47% of total hashrate | mononautical, via POD256 #044 (2024-04-19) | [POD256 #044](../../raw/history/pod256/2024-04-19-pod256-044-state-of-the-network-news-tangents-home-miner-of.md) |
| May 2025 | 58% of hashrate is controlled by just two pools | Bitmain (as reported by the newsletter) | [newsletter, Jun 2025](../../raw/history/256f-newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md) |
| May 2025 | Antpool plus its proxies ≈ 40% of network hashrate | 256F newsletter | same |
| 2025-08-17 | Eight consecutive blocks from Foundry | Public Pool on X | [Public Pool on X](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md) |
| Undated (FAQ captured 2026-10-07) | ~90% of hashrate controlled by four pool operators and their proxies; ~40% of mining rewards going to a single custodian; one hardware/firmware company with ~90% market dominance | 256 Foundation FAQ | [256F FAQ](../../raw/history/256f-org/256foundation-org-faq.md) |

B10C's own suggested remedy included more individuals home-mining with small miners, while noting that home hashrate was still negligible next to industrial hashrate ([newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md)).

> **Status: Disputed** — how concentrated, exactly?
> The figures measure different things: share of hashrate vs share of blocks; pools by name vs pools grouped by who controls the coinbase. The FAQ's four pool operators and their proxies (~90% of hashrate), B10C's six pools (>95% of blocks) and the newsletter's Antpool-plus-proxies (≈ 40%) are not contradictory so much as non-comparable. The single-custodian figures (47% of hashrate in April 2024; ~40% of rewards in the undated FAQ) differ by metric and date. Best assessment: the order of magnitude — a handful of entities controlling the large majority of templates — is consistent across all sources; treat any single percentage as a dated snapshot.

## Proxy pools: the Antpool network

- **Mechanism.** FPPS pays a steady amount per share while block finds are variable, so an FPPS pool needs a large balance sheet to absorb bad luck (the newsletter points to OrangeSurf's Pool Survival Analysis for the reserve math). Operators who cannot afford the reserves ask Antpool to bankroll them as a proxy ([newsletter, Jun 2025](../../raw/history/256f-newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md)).
- **Pools named as absorbed** (newsletter, June 2025): Poolin, Braiins, Ultimus Pool, Binance Pool, SecPool, SigmaPool, Rawpool, Luxor, CloverPool (formerly BTC.com) and Mining Squared (same source). This is the newsletter's characterization, not a disclosure by those pools.
- **Template evidence (June 5, 2025).** boerst showed Luxor's template coinbase tag change from "Powered by Luxor Tech" to "Mined by AntPool"; the AntPool and Luxor templates were an exact 1:1 match, and his Bitaxe kept getting shares accepted by Luxor on the mangled template for several minutes. The newsletter called this confirmation that Luxor is an AntPool proxy, and asked how such tags can be trusted at all ([newsletter, Jul 2025](../../raw/history/256f-newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md)).
- **Why it matters (April 2024 Telegram debate).** Proxy front-ends can hide how much hashrate one entity really controls; the community consensus was that template censorship is the nearer-term risk than a 51% attack. See the Disputed block in [Pool Payout Schemes](pool-payout-schemes.md).

## The FPPS critique: custody and templates

- **Two problems driven by FPPS** (newsletter, June 2025): custody — a custodian can influence pool operators — and templates — the operator dictates which transactions miners hash on. Both raise censorship risk, and concentration raises 51% risk ([newsletter, Jun 2025](../../raw/history/256f-newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md)).
- **Miner-built templates are not enough.** After Antpool announced (May 27, 2025) that miners could build their own templates while it kept FPPS payouts, the newsletter argued that a centralized pool still counting shares and coordinating payouts can be coerced into excluding shares built on non-conforming templates, or excluding a user's payout address; DATUM and SV2 are "good steps" but over-marketed, and "centralized pools will never decentralize Bitcoin mining" (same source).
- **SV2's limit.** Stratum V2 job negotiation lets miners propose templates the pool validates but cannot censor at the transaction level, yet the pool still controls the coinbase payout and share accounting ([newsletter, Apr 2026](../../raw/history/256f-newsletter/2026-04-15-assembling-freedom-24-bitcoin-mining-renaissance-stratum-v2.md)); the July 2025 issue called the SV2/DATUM decentralization emphasis overblown while centralized pools still do accounting and payouts ([newsletter, Jul 2025](../../raw/history/256f-newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md)).
- POD256 #112 (2026-04-15) described today's pool landscape as centralized around FPPS ([POD256 #112](../../raw/history/pod256/2026-04-15-pod256-112-stratum-v2-nonce-space-and-the-diy-miner-s-comeba.md)).

> **Status: Disputed** — can a pool still censor miner-built templates?
> On the ESP-Miner SV2 issue, benjamin-wilson (Public Pool) argued that a pool can still censor proposed templates; TheBlueMatt countered that under the SV2 reference implementation a miner whose template is rejected falls back to another pool or solo mining, which turns censorship into a passive act, and miners doing custom job declaration broadcast the blocks they find themselves ([ESP-Miner #168](../../raw/firmware/esp-miner/2024-04-23-github-esp-miner-issue-168-adding-support-for-stratumv2-prot.md)). Best assessment: SV2 job declaration removes the pool's power to silently alter a template, but not its power to refuse shares or payouts — which is the 256 Foundation's point about accounting and custody.

## Pool security and integrity incidents

| Date | Incident | Source |
|---|---|---|
| April 15 (2025) | A Bitmain S21+ firmware update was reported to block connections to OCEAN and Braiins pools — pool choice constrained at the firmware level | [newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md) |
| April 27 (2025) | Public Pool patched a duplicate-share check: scam NerdMiner firmware submitted each valid share five times to fake five times the hashrate | same |
| June 5 (2025) | Luxor serving a "Mined by AntPool" template (see above) | [newsletter, Jul 2025](../../raw/history/256f-newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md) |
| June 2025 | Braiins estimated 1% to 2% of hashrate is stolen by hijacking unencrypted Stratum V1 connections (cited in SV2 coverage) | same |
| August 2025 | stratum.work's new events panel flagged invalid mining jobs from Antpool and others during forks: empty Merkle branches yet coinbase totals above the subsidy (fees for non-existent transactions). A golden nonce on one of those jobs would have produced an invalid block. Theories ranged from a botched selfish-mining attempt to glitchy template code; b10c published an analysis; root cause unresolved | [newsletter, Sep 2025](../../raw/history/256f-newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md) |
| Summer 2025 | Sub-sat summer: Mara accepted transactions below 1-sat/vB; at height 906,343 Antpool had a block orphaned by Foundry and lost its 3.145 BTC reward. A template-policy trade-off between fee revenue and propagation risk | same |

Other dated notes: scam pools and coinbase-checking tools were discussed on POD256 #099 ([POD256 #099](../../raw/history/pod256/2025-12-17-pod256-099-code-is-not-crime-samourai-petition-pool-scams-an.md)); for firmware-level trust issues see [Mining Firmware Security](../industry/mining-firmware-security.md).

## Transparency tools

- **stratum.work** (boerst) connects to pools and visualizes their live jobs ([POD256 #048](../../raw/history/pod256/2024-06-12-pod256-048-decentralizing-bitcoin-mining-insights-from-boers.md)). April 26 (2025): a per-pool block-template detail page, including OP_RETURN data and merge mining such as RSK ([newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md)). July 11 (2025): a Sankey diagram tracing how pools assemble templates through shared Merkle branches ([newsletter, Aug 2025](../../raw/history/256f-newsletter/2025-08-18-is-open-source-communism.md)). August 26 (2025): an events panel for forks and invalid templates ([newsletter, Sep 2025](../../raw/history/256f-newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md)).
- **Coinbase tags on your own miner.** By 2025-08-20 ESP-Miner logged the block height and miner tag from each job (e.g. `ckpooleu/solo.ckpool.org/`), so a Bitaxe owner can see whose template they are hashing ([ESP-Miner #1011](../../raw/firmware/esp-miner/2025-06-06-github-esp-miner-issue-1011-show-block-header-information-in.md)). Tags are self-declared — the Luxor incident shows they can be wrong.
- **Auditable share accounting.** Hydrapool exposes its PPLNS shares through an API so miners can check payouts instead of trusting the operator ([hydrapool.org](../../raw/pools/hydrapool/hydrapool-org-home.md)); see [Hydrapool](hydrapool.md) for the pool-signature and mempool.space attribution debate.
- **On-chain checks.** How to decode a block's coinbase tag yourself: [Solo Blocks Found by Open-Source & Home Miners](../history/open-source-solo-blocks.md).

## Editorial positions (dated)

- **256 Foundation FAQ:** mining is dangerously centralized across hardware/firmware, pools and reward custody; the mission is to open-source the whole stack ([256F FAQ](../../raw/history/256f-org/256foundation-org-faq.md)). Hydrapool exists so communities can stand up their own non-custodial pools and move hashrate away from choke points quickly if pools are coerced to KYC users or censor transactions ([hydrapool.org](../../raw/pools/hydrapool/hydrapool-org-home.md)).
- **June 2025 newsletter:** Antpool's miner-template announcement should be met with skepticism; only pools without central accounting and custody decentralize mining ([newsletter, Jun 2025](../../raw/history/256f-newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md)).
- **skot (2025-06-05):** home miners on open hardware who aren't subject to FPPS shenanigans are what fixes mining ([X post](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md)).
- **Public Pool (2025-08-17):** eight consecutive Foundry blocks show how much work remains for open-source mining (same source).
- **Early POD256 (2023):** fedipool was floated as a mitigation for pool centralization ([POD256 #007](../../raw/history/pod256/2023-02-11-pod256-007-state-of-the-network-industrial-scale-miner-conso.md)).
- **Counterpoint inside the community:** for intermittent heater hashrate FPPS is often the conservative choice, and its fee handling is opaque but convenient — see [Pool Choice for Heat Miners](pool-choice-for-heat-miners.md).

## What a home miner can do

1. **Solo with your own template:** self-hosted [Public Pool](public-pool.md) or Solo CKPool-style software on your own node.
2. **Non-custodial pooled payouts:** run or join a [Hydrapool](hydrapool.md) instance (coinbase payouts, auditable shares), or use designs from [Decentralized Pool Designs](../protocols/decentralized-pool-designs.md).
3. **Check what you hash:** read the miner tag in your firmware logs and spot-check pools on stratum.work.
4. **Encrypt the connection:** prefer SV2 or TLS stratum where offered to avoid hashrate hijacking — see [Stratum in Practice](../protocols/stratum-in-practice.md).

## See Also

- [Pool Payout Schemes](pool-payout-schemes.md)
- [Pool Choice for Heat Miners](pool-choice-for-heat-miners.md)
- [Hydrapool](hydrapool.md)
- [Public Pool](public-pool.md)
- [Decentralized Pool Designs](../protocols/decentralized-pool-designs.md)
- [Stratum in Practice](../protocols/stratum-in-practice.md)
- [Mining Firmware Security](../industry/mining-firmware-security.md)
- [Network State 2022–2026](../industry/network-state-2022-2026.md)
- [Solo Blocks Found by Open-Source & Home Miners](../history/open-source-solo-blocks.md)
- [Open Mining Economics](../economics/open-mining-economics.md)
