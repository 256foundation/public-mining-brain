# SEALMINER Overview

> Sources: Bitdeer shop catalog (bitdeer.com/shop, 2026-10-10); Bitdeer SEALMINER technology roadmap (bitdeer.com/sealminer/roadmap, 2026-10-10); ASIC Miner Value + MiningNow profitability DBs (2026-10-10)
> Raw: [Bitdeer shop SEALMINER catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md); [SEALMINER roadmap (SEAL01–SEAL04)](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md); [SEALMINER A2 product page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a2-product.md); [SEALMINER A2 Pro Air product page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a2-pro-air-product.md); [SEALMINER A2 Pro Hydro product page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a2-pro-hydro-product.md); [SEALMINER A4 Ultra Hydro product page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a4-ultra-hydro-product.md); [ASIC Miner Value — Bitdeer listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md); [MiningNow — Bitdeer rows](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md); [AMV/MN cross-check report](../../raw/hardware/asicminervalue/_REPORT.md); [Bitdeer capture report](../../raw/hardware/bitdeer/_REPORT.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

SEALMINER is Bitdeer's in-house ASIC miner line, built on its own SEAL chip generations and sold retail through bitdeer.com/shop with USD prices, crypto payment and coupon pricing. The lineup spans the A2 generation (SEAL02, shipping), the A3 generation (SEAL03) and the A4 generation (SEAL04, roadmap), plus a new Scrypt DL1 line for LTC+DOGE. Everything on this page is As-Of 2026-10-10: the shop listed 13 SEALMINER products that day, with per-model pages captured for the A2, A2 Pro Air, A2 Pro Hydro and A4 Ultra Hydro ([shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md); [capture report](../../raw/hardware/bitdeer/_REPORT.md)).

Bitdeer frames the line around chip-level transparency — the roadmap page opens: "In the dynamically evolving mining market, industry transparency is particularly crucial for Bitcoin miners. Bitdeer is committed to driving greater industry transparency over the long haul." ([roadmap](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md)). All shop figures carry a variance disclaimer: "Note: Product performance may vary by ±10% in hashrate and ±5% in power efficiency. Final specifications are based on delivered units." ([shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)).

## Lineup (Bitdeer shop, As-Of 2026-10-10)

13 products in the shop's embedded ItemList, in listed order ([shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)). TH/s is not printed on the shop listing itself — only power and price; hashrates below come from the product pages and series copy where captured.

| # | Product | Type | Power | Price shown | Status |
|---|---------|------|-------|-------------|--------|
| 1 | SEALMINER A3 Pro Hydro | SHA256 hydro | 8250W | $9,900 ($15/T); coupon $9,478 ($14.36/T) | Buy Now |
| 2 | SEALMINER A3 Hydro | SHA256 hydro | 6750W | $6,750 ($13.5/T); coupon $6,411 ($12.82/T) | Buy Now |
| 3 | SEALMINER A4 Ultra Hydro | SHA256 hydro | 8372.7W | (price not shown — "Learn More / Stay tuned") | Stay tuned |
| 4 | SEALMINER A4 Pro Air | SHA256 air | 3662.4W | (price not shown) | Pre-Order |
| 5 | SEALMINER A4 Pro Hydro | SHA256 hydro | 7412W | (price not shown) | Pre-Order |
| 6 | SEALMINER DL1 Air | Scrypt \| LTC+DOGE air | 3725W | (price not shown) | Pre-Order |
| 7 | SEALMINER DL1 Hydro | Scrypt \| LTC+DOGE hydro | 7823W | (price not shown) | Pre-Order |
| 8 | SEALMINER A2 Pro Air | SHA256 air | 3874W | $3,380 ($13/T); coupon $3,067 ($11.8/T) | Sold-Out |
| 9 | SEALMINER A2 Pro Hydro | SHA256 hydro | 7450W | $6,500 ($13/T); coupon $5,897 ($11.8/T) | Sold-Out |
| 10 | SEALMINER A3 Air | SHA256 air | 3640W | (price not shown) | Pre-Order |
| 11 | SEALMINER A3 Pro Air | SHA256 air | 3625W | (price not shown) | Pre-Order |
| 12 | SEALMINER A2 Hydro | SHA256 hydro | 7359W | $6,690 ($15/T) | Listed |
| 13 | SEALMINER A2 | SHA256 air | 3729W | $2,892.8 ($12.8/T) | Sold-Out |

- **SEALMINER A1 (1st gen) is no longer listed in the shop** — "SEALMINER A1 (1st gen) is no longer listed in the shop — current-gen only." A1 lineage lives on the roadmap page ([shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md); [roadmap](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md)). The profitability DBs agree it is delisted: AMV has no A1 row (probe of `/miners/bitdeer/sealminer-a1` and `sealminer-a1-226th` returned 404 on 2026-10-10) ([AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md)), and MiningNow's A1 sitemap page serves a soft-404 ("The Miner you are looking for is not found") ([MN](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md)).
- **DB coverage:** the same 13 SKUs appear on both ASIC Miner Value (13 Bitdeer rows) and MiningNow (13 rows) as of 2026-10-10 ([AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md); [MN](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md); [cross-check](../../raw/hardware/asicminervalue/_REPORT.md)). Spec-field mismatches between the two DBs are logged per model in the model articles.
- **Shop upsells:** Minerbase containers "Minerbase A40-CE — 336 PCS \| ≈12*2.4*2.9M — $26,999" and "Minerbase A40-UL — 336 PCS \| ≈12*2.4*2.9M — $34,999", plus a "$0.99 Reservation for Advanced Bitcoin Mining Technology!" notice strip ([shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)).
- **Series-tier summary (Bitdeer's own framing):** A2 up to 226TH/s air / 446TH/s hydro; A2 Pro 260T air / 500–530TH/s hydro; A3 lineup spans "240–690 TH/s across air- and hydro-cooling variants"; A4 "Hashrate up to 900 TH/s, Power efficiency as low as 9.45 J/TH" ([shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)).

## Chip lineage: SEAL01 → SEAL04

Bitdeer publishes its chip roadmap publicly, an efficiency ladder of "18.1J/TH → 13.5J/TH → 9.7J/TH → 6-7J/TH" ([roadmap](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md)):

| Chip | Released | Chip efficiency | Miner it powers | Miner efficiency / status |
|---|---|---|---|---|
| SEAL01 | Q1 2024 | 18.1J/TH | SEALMINER A1 | "Power efficiency ranges from 20 J/TH to 23 J/TH. Mass production and delivery started in Q3 2024" |
| SEAL02 | Q3 2024 | 13.5J/TH ("Surpassing the expected power efficiency target of 14 J/TH") | SEALMINER A2 | "Power efficiency of 14.9J/TH. Mass production and delivery started in Q1 2025" |
| SEAL03 | Q1 2025 | 9.7J/TH | SEALMINER A3 | "Power efficiency of 12.5J/TH. Mass production and delivery started in Q4 2025" |
| SEAL04 | Q4 2025 | "Power efficiency ranges from 6 J/TH to 7 J/TH" | SEALMINER A4 | "Power efficiency of 9.45J/TH. Expected to start mass production and delivery in Q3 2026" |

All roadmap rows are Bitdeer claims captured 2026-10-10; Q3/Q4 2025 and Q3 2026 dates are forward-looking roadmap statements, not observed shipping events ([roadmap](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md)). SEAL01 is described as a "4nm Process Chip"; no node is given for SEAL02–SEAL04.

> **Status: Disputed** (A2 efficiency, roadmap vs product page)
> The roadmap lists "SEALMINER A2 — Power efficiency of 14.9J/TH", while the A2 product page lists 16.5J/T (the 14.9J/T figure matches the A2 Pro pages). Both recorded verbatim; the roadmap figure may reflect the Pro refresh or an updated bin ([roadmap](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md); [A2 page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a2-product.md)). Details in [SEALMINER A2](sealminer-a2.md).

## A4 status (roadmap, future-dated)

The A4 Ultra Hydro is the 2026 flagship: 886T / 8372.7W / 9.45J/T on the product page, with the shop banner "SEALMINER A4 Ultra Hydro — 886T | 9.45J/T — Stay tuned" — no retail price at capture (`retailBuying` disabled, presell type) ([A4 Ultra page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a4-ultra-hydro-product.md); [shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)). Per the roadmap, "SEALMINER A4 — Power efficiency of 9.45J/TH. Expected to start mass production and delivery in Q3 2026" — a forward-dated roadmap claim; as of 2026-10-10 the shop still shows "Stay tuned" rather than a buyable price, and both profitability DBs already list the SKU with third-party prices ($9,999 on each) despite no Bitdeer retail price ([roadmap](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md); [AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md); [MN](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md)).

## DL1 (Scrypt, one-liner)

New product category alongside the SHA-256 line: SEALMINER DL1 Air (3725W) and DL1 Hydro (7823W, 2U server form factor), Scrypt miners for LTC+DOGE (BELLS, JKC, LKY and PEP named as "algorithmic compatibility only"), both Pre-Order with no price shown ([shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)).

## DesiWeMiner fold-in note

Capture-loop A7 folds DesiWeMiner coverage into `bitdeer-sealminer` (registry row `desiwe-miner`: standalone site defunct, reseller listings only, fold coverage into `bitdeer-sealminer` — [sources/registry.md](../../sources/registry.md)). Neither profitability DB carries DesiWeMiner rows: no K9S or K10 Pro on AMV ("no K9S/K10 Pro rows found in the AMV dataset") and none on MiningNow ("no 'desiwe', 'k9s' or DesiWeMiner K10 rows in the payload or sitemap") ([AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md); [MN](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md); [cross-check](../../raw/hardware/asicminervalue/_REPORT.md)).

The figures on record for the reseller-listed SKUs, from the capture notes (DesiWeMiner acquired by Bitdeer 2024-06 — registry note records a 140M all-stock acquisition via FreeChain Inc.; standalone site defunct, reseller listings only):

- DesiWeMiner K9S — 130 Th/s, 4950 W ([cross-check scope note](../../raw/hardware/asicminervalue/_REPORT.md); [MN coverage note](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md))
- DesiWeMiner K10 Pro — 170 Th/s, 3825 W (same notes)

*Reseller listing capture pending* — no DesiWeMiner capture exists under `raw/` (checked 2026-10-10), so these two spec rows come from the registry/capture notes, not from any captured reseller page. They are not cross-checked and are not Bitdeer-shop figures.

## See Also

- Models: [SEALMINER A2](sealminer-a2.md), [SEALMINER A2 Pro Air](sealminer-a2-pro-air.md), [SEALMINER A2 Pro Hydro](sealminer-a2-pro-hydro.md), [SEALMINER A3](sealminer-a3.md), [SEALMINER A4 Ultra Hydro](sealminer-a4-ultra.md)
- Same topic: [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md)
- Same topic: [Hydronic Heat Reuse](hydronic-heat-reuse.md)
- Same topic: [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md)
- Tooling: [asic-rs and the Fleet-Tooling Stack](../mining-software/asic-rs.md) — 256foundation/asic-rs carries SEALMINER web-API support code (PR #253, chore(ci): fix sealminer web api dead code warning, merged 2026-05-19) ([asic-rs #253](../../raw/mining-software/256f-tools/2026-05-19-github-asic-rs-pr-253-chore-ci-fix-sealminer-web-api-dead-co.md))
- Economics: [Hashrate Heating Economics](../economics/hashrate-heating-economics.md)
