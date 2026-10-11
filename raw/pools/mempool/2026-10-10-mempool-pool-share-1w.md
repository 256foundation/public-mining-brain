# mempool.space — pool share, 1w window

> Source: https://mempool.space/api/v1/mining/pools/1w
> Collected: 2026-10-10
> Published: Unknown
> Registry ID: mempool-space

---

Snapshot of mempool.space's mining-pool share ranking for the **1w** query window, fetched from the public API on 2026-10-10.

- Total blocks in window: **1072**
- Pool-wide estimated hashrate (lastEstimatedHashrate): **995.45 EH/s** (lastEstimatedHashrate3d: 951.15 EH/s; lastEstimatedHashrate1w: 1.01 ZH/s)
- The API response for this window carries **no per-pool estimated hashrate / share field** (those fields are null/absent) and **no explicit query-window end date**; block counts are the ranking metric.

| Rank | Pool | Blocks | Empty blocks | poolId | poolUniqueId | Avg block match rate | Avg fee delta |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Foundry USA | 288 | 0 | 112 | 111 | 99% | -0.0241 |
| 2 | AntPool | 213 | 1 | 45 | 44 | 97.54% | -0.0521 |
| 3 | F2Pool | 183 | 1 | 37 | 36 | 98.7% | -0.0490 |
| 4 | ViaBTC | 105 | 0 | 74 | 73 | 98.91% | -0.0269 |
| 5 | SpiderPool | 73 | 0 | 103 | 102 | 99.42% | -0.0871 |
| 6 | MARA Pool | 50 | 0 | 116 | 115 | 97.17% | +0.0541 |
| 7 | SECPOOL | 44 | 0 | 142 | 141 | 97.93% | -0.0601 |
| 8 | Luxor | 35 | 0 | 5 | 4 | 97.04% | -0.0635 |
| 9 | OCEAN | 29 | 0 | 143 | 142 | 92.61% | -0.2389 |
| 10 | Braiins Pool | 14 | 0 | 44 | 43 | 99.06% | -0.0932 |
| 11 | Unknown | 11 | 0 | 1 | 0 | 98.92% | -0.0250 |
| 12 | BTC.com | 9 | 0 | 7 | 6 | 92.71% | -0.0347 |
| 13 | NiceHash | 8 | 0 | 52 | 51 | 98.63% | -0.0324 |
| 14 | WhitePool | 4 | 0 | 144 | 143 | 95.41% | -0.0529 |
| 15 | Poolin | 3 | 0 | 95 | 94 | 98.05% | -0.0492 |
| 16 | Binance Pool | 3 | 0 | 106 | 105 | 97.97% | -0.0819 |

*Note: `1w` = trailing 1 week of blocks per mempool.space. `Avg fee delta` and `Avg block match rate` are mempool.space's template-match observables, not pool-published fees.*
