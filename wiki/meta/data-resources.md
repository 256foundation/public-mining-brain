# Data Resources — Live-Endpoint Pointer Table

> Sources: registry `link-only` rows (`elektronics-dev`, `hashdash`), agent-accessible data sources (`mempool-space`, `asicminervalue`, `stratum-work`), and the 256F pool Prometheus API contract in `automation/AGENT-PLAYBOOK.md`
> Raw: [stratum.work homepage extract](../../raw/protocols/stratum-work/stratum-work-homepage--extract.md); [stratum.work README](../../raw/protocols/stratum-work/bboerst-stratum-work-readme--verbatim.md); [mempool pool-share 1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md); [mempool pool-share 3m](../../raw/pools/mempool/2026-10-10-mempool-pool-share-3m.md); [mempool network-state snapshot](../../raw/pools/mempool/2026-10-10-mempool-network-state-snapshot.md); [Delving mining census](../../raw/protocols/reference-census/delving-bitcoin-mining-topics--census.md); [AMV Bitmain](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md); [AMV MicroBT](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [Hashrate Index homepage snapshot](../../raw/economics/hashrate-index/2026-10-10-homepage-snapshot.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Purpose

This wiki separates **citations** (frozen raw captures under `raw/`) from **live endpoints** (URLs worth checking in real time). This page is the pointer table for the live layer: what each endpoint is good for, how to query it, and its house rules. Anything with numbers quoted in wiki articles should be backed by a raw capture; these pointers are for *checking current values*, not for sourcing claims.

## The pointers

| Endpoint | What it serves | How to query | Posture / contract | Wiki consumers |
|---|---|---|---|---|
| **256F pool Prometheus** | Live pool/hasher telemetry: PromQL over the 256F pool's own metrics | `GET https://pool.256foundation.org/api/v1/query?query=<PromQL>` | Agent-playbook contract; the **only** sanctioned live-number source for 256F systems | Mujina fleet story, [asic-rs](../mining-software/asic-rs.md) |
| **dash.256f.org** (`hashdash`) | Tyler's dashboard — visualization only | Browser | **NOT a data source — do not scrape**; pull live numbers from the pool Prometheus endpoint above | — |
| **stratum.work** (`stratum-work`) | Live stratum message visualization per pool: real jobs, templates, Merkle branches, Sankey template flows, BIP-110 column | https://stratum.work — static chrome is prerendered; the job stream is websocket `/api/stream` (SSE per the repo) | Site = extract (chrome); live stream = session, not capture. Repo README documents collector→RabbitMQ/MongoDB→SSE architecture | [Stratum in Practice](../protocols/stratum-in-practice.md) |
| **mempool.space** (`mempool-space`) | Network/pool stats: pool share (1w/3m), difficulty, hashrate, block details | https://mempool.space/api — e.g. `/v1/mining/pools/1w` | extract; snapshot captures kept under `raw/pools/mempool/` | [Pool Centralization & FPPS](../pools/pool-centralization-and-fpps.md), [Network State](../industry/network-state-2022-2026.md) |
| **ASIC Miner Value** (`asicminervalue`) | Cross-vendor spec/profitability DB — the third-party cross-check for Bitmain/MicroBT spec tables | https://www.asicminervalue.com | extract (SSR); per-manufacturer pages | [Bitmain ASIC reference](../hardware/bitmain-asic-reference.md), hardware articles (AMV cross-checks) |
| **elektronics.dev** (`elektronics-dev`) | Rapha Zagury's curated mining dataset — "coming soon" at capture | https://elektronics.dev/about | **link-only** (no data published yet; capture on event) | this table; Phase B re-check |
| **Hashrate Index** | Hashprice spot + forward curve (Luxor) | https://hashrateindex.com — homepage numbers render SSR; API not captured | extract, snapshot only | [Hashprice and Difficulty](../economics/hashprice-and-difficulty.md) |
| **CBECI** | Cambridge network electricity estimates | https://ccaf.io/cbnsi/cbeci — live numbers need a rendered browser (reCAPTCHA-gated client-side); `/data/live` 400s to curl | documented in [CBECI landing capture](../../raw/economics/cbeci/cbeci-landing.md) | [Open Mining Economics](../economics/open-mining-economics.md) and the DMIR extract |

## Query conventions

- Every claim in this wiki cites a **raw capture**, never a live endpoint — re-run the capture if the number matters, then cite the new file.
- The pool Prometheus endpoint is the exception: it is the designated live surface for 256F operational state (dashboards, controllers) per `automation/AGENT-PLAYBOOK.md`.
- `link-only` registry rows (elektronics.dev, hashdash) exist so wiki pages can point at them without implying a verbatim capture exists.

## See Also

- [Hashprice and Difficulty](../economics/hashprice-and-difficulty.md) — the market data these endpoints feed
- [Network State 2022–2026](../industry/network-state-2022-2026.md) — dated snapshots from the same sources
- [Public Miner Economics](../industry/public-miner-economics.md) — the filings-side view
