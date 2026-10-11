# Delving Bitcoin — mining-related topics census

> Registry ID: delving-bitcoin (unregistered, handoff-approved)
> Source: https://delvingbitcoin.org/tag/mining/l/latest.json (+ /tag/mining-pools/l/latest.json, /tag/stratum-v2/l/latest.json, /categories.json, /tags.json)
> Collected: 2026-10-10
> Published: n/d (forum snapshot; per-topic dates below)
> Posture: extract
> As-Of: 2026-10-10

## Site-structure discovery (important deviation from mission)

Delving Bitcoin is a Discourse forum. **There is NO `/c/mining/` category.** `/categories.json` returns exactly five categories: Implementation (226 topics), Protocol Design (326), Economics (14), Philosophy (26), Meta (19). Mining discussions are organized by **tags**, not a category. The census below therefore enumerates the mining-related tags via the Discourse JSON API (SSR site; JSON endpoints serve clean structured data):

- `#mining` — 10 topics (complete)
- `#mining-pools` — 6 topics
- `#stratum-v2` — 5 topics
- Overlap → **14 unique topics** total (mission target was "top ~20"; the mining tag has only 10 topics — all captured, none omitted).

Related tag counts from `/tags.json` (mining-relevant subset): mempool 33 · wg-cluster-mempool 10 · mining 10 · miniscript 7 · mining-pools 6 · stratum-v2 5 · braidpool 4 · txhash 2.

## Tag census: #mining (all 10 topics, sorted by latest activity)

| # | Topic (title verbatim) | ID | Created | Last post | Replies | Views | Likes | Also tagged |
|---|---|---|---|---|---|---|---|---|
| 1 | Disabling min-difficulty blocks on testnet4 | 2350 | 2026-03-22 | 2026-08-29 | 3 | 324 | 2 | — |
| 2 | SV2 Extensions for Payout Verification and Job Size at Scale | 2805 | 2026-08-14 | 2026-08-14 | 1 | 89 | 0 | mining-pools, stratum-v2 |
| 3 | New Extension Proposal for Stratum V2 | 2809 | 2026-08-14 | 2026-08-14 | 0 | 90 | 0 | stratum-v2 |
| 4 | P2share: how to turn any network (or testnet!) into a bitcoin miner | 2093 | 2025-11-07 | 2026-08-06 | 27 | 986 | 7 | mining-pools |
| 5 | Does Bitcoin's fee market price permanence, or just congestion? | 2750 | 2026-07-28 | 2026-07-28 | 0 | 75 | 0 | announcement, bitcoin-core, taproot |
| 6 | [Research] A clockless vardiff strands a slowing miner | 2718 | 2026-07-15 | 2026-07-25 | 7 | 523 | 10 | mining-pools, stratum-v2 |
| 7 | [Research] Bitcoin After Block Rewards : preventing miner's deviation when the Bitcoin rewards is zero | 2626 | 2026-06-21 | 2026-07-18 | 11 | 379 | 3 | — |
| 8 | Fee Selection for CTV-Based Mining Pool Fanouts | 2698 | 2026-07-08 | 2026-07-09 | 5 | 136 | 7 | softfork, ctv |
| 9 | Optimistic mining tip (slow block propagation) | 2139 | 2025-12-03 | 2025-12-05 | 6 | 259 | 4 | bitcoin-core |
| 10 | Analyzing Mining Pool Behavior to Address Bitcoin Core's Double Coinbase Reservation Issue | 1351 | 2025-01-01 | 2025-01-16 | 6 | 676 | 16 | — |

## Tag census: #mining-pools (6 topics)

| # | Topic | ID | Created | Last post | Replies | Views | Likes | Also tagged |
|---|---|---|---|---|---|---|---|---|
| 1 | SV2 Extensions for Payout Verification and Job Size at Scale | 2805 | 2026-08-14 | 2026-08-14 | 1 | 89 | 0 | mining, stratum-v2 |
| 2 | P2share: how to turn any network (or testnet!) into a bitcoin miner | 2093 | 2025-11-07 | 2026-08-06 | 27 | 986 | 7 | mining |
| 3 | [Research] Vardiff belongs at the frontier | 2734 | 2026-07-21 | 2026-07-26 | 1 | — | — | stratum-v2 |
| 4 | [Research] A clockless vardiff strands a slowing miner | 2718 | 2026-07-15 | 2026-07-25 | 7 | 523 | 10 | mining, stratum-v2 |
| 5 | Scaling Noncustodial Mining Payouts with CTV | 1753 | 2025-06-04 | 2026-07-08 | 18 | — | — | — |
| 6 | Radpool: Decentralised Mining Pool With Futures Contracts For Payouts | 1262 | 2024-11-16 | 2024-12-07 | 21 | — | — | — |

## Tag census: #stratum-v2 (5 topics)

| # | Topic | ID | Created | Last post | Replies | Views | Likes | Also tagged |
|---|---|---|---|---|---|---|---|---|
| 1 | SV2 Extensions for Payout Verification and Job Size at Scale | 2805 | 2026-08-14 | 2026-08-14 | 1 | 89 | 0 | mining, mining-pools |
| 2 | New Extension Proposal for Stratum V2 | 2809 | 2026-08-14 | 2026-08-14 | 0 | 90 | 0 | mining |
| 3 | [Research] Vardiff belongs at the frontier | 2734 | 2026-07-21 | 2026-07-26 | 1 | — | — | mining-pools |
| 4 | [Research] A clockless vardiff strands a slowing miner | 2718 | 2026-07-15 | 2026-07-25 | 7 | 523 | 10 | mining, mining-pools |
| 5 | Stratum v2 Noise Protocol: BIP324 nuggets? | 413 | 2024-01-15 | 2024-01-15 | 0 | — | — | — |

## Deduplicated union (14 unique topics)

Replies = posts_count − 1. "—" = field not fetched (views/likes only present on the #mining listing pages fetched).

Unique topic IDs: 2350, 2805, 2809, 2093, 2750, 2718, 2626, 2698, 2139, 1351, 2734, 1753, 1262, 413.

Signal highlights for stratum-in-practice: active 2026 Stratum V2 extension proposals (2805, 2809); vardiff research strand (2718, 2734); decentralized-pool designs (P2share 2093, Radpool 1262, CTV-based payouts 1753/2698); pool-behavior empirical analysis (1351, 16 likes — highest engagement).

## Parks

- Individual topic bodies/OP posts: not fetched (census-only posture; fetch on demand by topic ID via `/t/<id>.json`).
- Views/likes for topics outside the #mining listing: not fetched.
- No `/c/mining/` category exists to snapshot — see discovery note above; if a mining category is desired for the wiki, it must be a tag-based census (this file) or a future site change.
