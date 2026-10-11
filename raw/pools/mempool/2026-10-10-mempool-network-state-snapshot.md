# mempool.space — network state snapshot (difficulty + hashrate)

> Source: https://mempool.space/api/v1/difficulty-adjustment + https://mempool.space/api/v1/mining/hashrate/3d
> Collected: 2026-10-10
> Published: Unknown
> Registry ID: mempool-space

---

One-shot snapshot of Bitcoin network state from mempool.space's public API, collected 2026-10-10 (context for the pool-share captures in this directory).

## Difficulty / retarget

- Current difficulty: **58%** through the epoch (next retarget at height **971,712**)
- Estimated difficulty change at next retarget: **+3.67%** (previous retarget: -0.03%)
- Estimated retarget date: **2026-10-16 19:39 UTC**
- Blocks remaining this epoch: **853** (~5.7 days); expected blocks: 1122.8
- Time avg: 9.7 min/block

## Hashrate (3d endpoint)

- Current hashrate: **1.02 ZH/s** — current difficulty: **132,716,002,350,731.3**

Series from `/api/v1/mining/hashrate/3d` — the 3-day window contains only 3 daily points (well under the ~10-point truncation cap, so all are kept). Dates are UTC:

| Date (UTC) | Avg hashrate |
|---|---:|
| 2026-10-09 | 916.13 EH/s |
| 2026-10-10 | 960.70 EH/s |
| 2026-10-11 | 1.02 ZH/s |

*`difficulty` array in the response is empty for this window.*
