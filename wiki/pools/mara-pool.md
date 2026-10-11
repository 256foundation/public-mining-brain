# MARA Pool

> Sources: marapool.com / mara.com site-status checks + MARA's own press releases on ir.mara.com (2021-09-09 and 2025-04-03, captured in full 2026-10-10); mempool.space pool-share API (1w/3m) and network state (2026-10-10)
> Raw: [MARA pool site status](../../raw/pools/mara/2026-10-10-marapool-site-status.md); [MARA first-party statements (ir.mara.com PRs)](../../raw/pools/mara/2026-10-10-mara-pool-first-party-statements.md); [mempool pool share 1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md); [mempool pool share 3m](../../raw/pools/mempool/2026-10-10-mempool-pool-share-3m.md); [mempool network state](../../raw/pools/mempool/2026-10-10-mempool-network-state-snapshot.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

**The site is gone; the pool is not.** MARA Pool (MaraPool) is the in-house mining pool of MARA Holdings, Inc. (NASDAQ: MARA; formerly Marathon Digital Holdings) ([site status](../../raw/pools/mara/2026-10-10-marapool-site-status.md)). On 2026-10-10 it ranked #6 on mempool.space's trailing-week table with 50 of 1,072 blocks (avg block match rate 97.17%, avg fee delta +0.0541) and #6 over 3 months with 648 of 13,346 blocks (98.83% match rate) ([1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md); [3m](../../raw/pools/mempool/2026-10-10-mempool-pool-share-3m.md)) — while its dedicated public site is gone ([site status](../../raw/pools/mara/2026-10-10-marapool-site-status.md)):

- `https://marapool.com` and `https://www.marapool.com` resolve (AWS Global Accelerator addresses, e.g. 3.33.152.147) but the **TLS handshake fails on 443**: LibreSSL reports `tlsv1 alert internal error`, reproduced repeatedly on collection day ([site status](../../raw/pools/mara/2026-10-10-marapool-site-status.md)).
- Plain `http://marapool.com` answers 301 → `https://www.mara.com/` — the former pool domain now forwards to the corporate marketing site ([site status](../../raw/pools/mara/2026-10-10-marapool-site-status.md)).
- The corporate site carries no pool product page: its sitemap.xml lists marafw (firmware), about-us, operations, insights and posts — zero URLs containing "pool" ([site status](../../raw/pools/mara/2026-10-10-marapool-site-status.md)).
- The 2021 launch press release directed prospective members to "visit marapool.com" to apply; that funnel no longer exists at this domain ([site status](../../raw/pools/mara/2026-10-10-marapool-site-status.md); [statements](../../raw/pools/mara/2026-10-10-mara-pool-first-party-statements.md)).

That contrast is the story: a top-6 pool by blocks with no public web presence, whose first-party terms survive only in investor-relations press releases ([site status](../../raw/pools/mara/2026-10-10-marapool-site-status.md); [statements](../../raw/pools/mara/2026-10-10-mara-pool-first-party-statements.md)). Network context: 1.02 ZH/s current hashrate, 58% through the epoch, next retarget estimated 2026-10-16 19:39 UTC ([network state](../../raw/pools/mempool/2026-10-10-mempool-network-state-snapshot.md)).

## Fees and payout

- **Nothing payout-related is published on any reachable MARA-controlled page** — no fee %, payout scheme, threshold or cadence (As-Of 2026-10-10) ([site status](../../raw/pools/mara/2026-10-10-marapool-site-status.md)).
- **First-party fee posture (Apr 3, 2025 PR).** CEO Fred Thiel called MARAPool "the only self-owned and operated mining pool among public miners" and said "Operating our own pool means no fees to external operators", with higher earnings and superior performance ([statements](../../raw/pools/mara/2026-10-10-mara-pool-first-party-statements.md)). Read carefully, that is a statement about MARA not paying external pool operators — not a published member fee schedule; whether external members are charged is not stated, and no numeric fee is disclosed ([statements](../../raw/pools/mara/2026-10-10-mara-pool-first-party-statements.md)).
- The same PR claims "MARA Pool's luck factor has exceeded the network average by over 10% since launch" ([statements](../../raw/pools/mara/2026-10-10-mara-pool-first-party-statements.md)).
- March 2025 operating stats (MARAPool only, excluding joint ventures): 242 blocks won (+17% m/m), 829 BTC produced, 5.8% share of available miner rewards, transaction fees 1.3% of total, energized hashrate 54.3 EH/s ([statements](../../raw/pools/mara/2026-10-10-mara-pool-first-party-statements.md)).
- On mempool.space's 1w table MARA Pool is the only pool in the top 10 with a positive avg fee delta (+0.0541); its 3m delta is -0.0004 — both are mempool.space's template-match observables, not pool-published fees ([1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md); [3m](../../raw/pools/mempool/2026-10-10-mempool-pool-share-3m.md)).

## Custody and access

- **2021 opening to external North American miners.** DMG Blockchain became "the first North American Bitcoin miner, excluding Marathon, to join Marathon's mining pool, MaraPool", pointing 100% of its hashrate at the pool from Sept 13, 2021 ([statements](../../raw/pools/mara/2026-10-10-mara-pool-first-party-statements.md)). Thiel at the time: "After experiencing difficulties with mining pools outside the U.S., we decided to launch our own pool that would reflect the values and needs of enterprising North American Bitcoin miners" ([statements](../../raw/pools/mara/2026-10-10-mara-pool-first-party-statements.md)).
- **Audit and member services.** The 2021 PR describes the pool as "fully audited by a third-party firm in the U.S.", providing "industry leading transparency, an intuitive reporting system", and "exclusive services from NYDIG" ([statements](../../raw/pools/mara/2026-10-10-mara-pool-first-party-statements.md)).
- **Positioning.** "MaraPool is a U.S.-based Bitcoin mining pool" focused on "reducing the environmental impact of Bitcoin mining through carbon neutral mining" ([statements](../../raw/pools/mara/2026-10-10-mara-pool-first-party-statements.md)). Context the PR does not restate: Marathon had earlier in 2021 announced a "fully compliant" pool filtering OFAC-sanctioned transactions — widely reported and controversial ([statements](../../raw/pools/mara/2026-10-10-mara-pool-first-party-statements.md)).
- **Membership was application-based** (2021), for miners "that share our beliefs"; the current join path is not published — the pool site is down and the corporate site lists no pool page (As-Of 2026-10-10) ([statements](../../raw/pools/mara/2026-10-10-mara-pool-first-party-statements.md); [site status](../../raw/pools/mara/2026-10-10-marapool-site-status.md)).

## SV2 / DATUM

Not mentioned in either press release, nor on any reachable MARA-controlled page (As-Of 2026-10-10) ([statements](../../raw/pools/mara/2026-10-10-mara-pool-first-party-statements.md); [site status](../../raw/pools/mara/2026-10-10-marapool-site-status.md)).

## See Also

- [SECPOOL](secpool.md)
- [Luxor Pool](luxor-pool.md)
- [SpiderPool](spiderpool.md)
- [Braiins Pool](braiins-pool.md)
- [Pool Centralization & FPPS](pool-centralization-and-fpps.md)
- [Pool Payout Schemes](pool-payout-schemes.md)
- [Network State 2022–2026](../industry/network-state-2022-2026.md)
- [Stratum in Practice](../protocols/stratum-in-practice.md)
