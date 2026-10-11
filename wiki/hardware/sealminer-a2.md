# SEALMINER A2

> Sources: Bitdeer SEALMINER A2 product page (bitdeer.com/shop/product/P250414000002, 2026-10-10); Bitdeer shop catalog (2026-10-10); Bitdeer SEALMINER roadmap (2026-10-10); ASIC Miner Value + MiningNow DBs (2026-10-10)
> Raw: [SEALMINER A2 product page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a2-product.md); [Bitdeer shop SEALMINER catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md); [SEALMINER roadmap (SEAL01–SEAL04)](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md); [ASIC Miner Value — Bitdeer listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md); [MiningNow — Bitdeer rows](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md); [AMV/MN cross-check report](../../raw/hardware/asicminervalue/_REPORT.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

The SEALMINER A2 is Bitdeer's air-cooled SEAL02-chip miner, sold at $2,892.8 ($12.8/T) and shown Sold-Out (spot) at capture. Bitdeer's page copy: "Powered by the SEAL02 Bitcoin mining chip, the SEALMINER A2 pushes the hashrate limits—up to 226TH/s for the air-cooling model and 446TH/s for the hydro-cooling model. Hashrate like never before." ([A2 page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a2-product.md)). The hydro sibling is covered by the same page copy and priced $6,690 ($15/T) in the shop ([shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)); the Pro refresh is in [SEALMINER A2 Pro Air](sealminer-a2-pro-air.md) and [SEALMINER A2 Pro Hydro](sealminer-a2-pro-hydro.md).

## Specs (Bitdeer shop, As-Of 2026-10-10)

From the product page listing (server-rendered + embedded product object) ([A2 page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a2-product.md)):

| Item | Value |
|---|---|
| Product | SEALMINER A2 |
| Subtitle | BTC/BCH/BSV SHA256 Air-cooling Miner |
| Hashrate | 226T |
| Power consumption | 3729W |
| Power efficiency | 16.5J/T |
| Price | $2,892.8 ($12.8/T) USD |
| Status | Sold-Out (spot) |
| Power supply | "Power Supply(4pin to C19 with power cord)" |
| Weight | 17.5 KG |
| Shipping | "Ships in 7 business days after full payment." |
| Product group key | `A2-Batch4-Common-Product` |
| Warranty | "BITDEER guarantees a 365-day warranty starting from the shipment date." |

- Payment methods: BTC | BCH | ETH | LTC | USDT | USDC | USD ([A2 page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a2-product.md)).

- Chip: SEAL02 (2nd-gen, released Q3 2024 at 13.5J/TH chip-level) ([roadmap](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md)).
- Hydro sibling (same page copy): 446TH/s; A2 Hydro banner: "Equipped with Bitdeer's advanced SEAL02 chip, this powerhouse achieves 446 TH/s at a super-efficient 16.5J/TH." Shop row: 7359W, $6,690 ($15/T) ([A2 page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a2-product.md); [shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)).
- Temperatures (per Bitdeer test data): "The air-cooling model operates stably from -20°C to 50°C, while the hydro-cooling model performs flawlessly from 20°C to 55°C." ([A2 page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a2-product.md); [shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)).
- Meta description (verbatim): "Buy the official SEALMINER A2 at Bitdeer. Featuring 16.5J/T efficiency and 3729W power consumption. Get expert technical specs, professional after-sales support, and weekly updated mining tips." ([A2 page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a2-product.md)).
- Variance: "*The actual hash rate and power efficiency of each product delivered may vary by ±10% and ±5% respectively. These figures are for reference only, and the actual product delivered shall prevail." ([shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)).
- Gap: the "Product Specifications" tab renders as images — dimensions, fan, noise and network specs are not machine-readable at capture; only weight (17.5 KG) is in text ([A2 page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a2-product.md)).

## Cross-check

**ASIC Miner Value row** (manufacturer listing; Profit cells on this page type are electricity-cost-only negatives at the site's $0.10/kWh rate, top-coin column empty) ([AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md)):

| Model (as listed) | Release | Hashrate | Power | Algorithm | Profit (as shown) |
|---|---|---|---|---|---|
| Bitdeer SealMiner A2 (226 Th) | Feb 2025 | 226 Th/s | 3730 W | SHA-256 | -$8.95 /day |

**MiningNow row** (profit at the site's $0.07/kWh default rate) ([MN](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md)):

| Model (as listed) | Hashrate | Power | Efficiency (as listed) | Best price | Income $/day | Profit $/day | Announced | First batch | Cooling |
|---|---|---|---|---|---|---|---|---|---|
| Bitdeer SealMiner A2 (226TH/s) | 226TH/s | 3729 W | 16.5 j/Th | $3,099.00 | 8.87 | 2.60 | Nov 2024 | Dec 2024 | air |

> **Status: Disputed** (power, release)
> Power: AMV lists 3730 W, MiningNow 3729 W, vendor page 3729W ([AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md); [MN](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md); [cross-check](../../raw/hardware/asicminervalue/_REPORT.md)). Release: AMV Release Feb 2025 vs MiningNow announced Nov 2024 with first batch Dec 2024 ([cross-check](../../raw/hardware/asicminervalue/_REPORT.md)). Best assessment as of 2026-10-10: 3729W per the vendor page; the release spread is an AMV Release (Feb 2025) vs MN launch (Dec 2024) database-convention difference.

> **Status: Disputed** (efficiency, roadmap vs product page)
> Roadmap: "SEALMINER A2 — Power efficiency of 14.9J/TH" (mass production and delivery started Q1 2025). Product page: 16.5J/T. The 14.9J/T figure matches the A2 Pro pages, so the roadmap number may reflect the Pro refresh or an updated bin; both recorded verbatim ([roadmap](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md); [A2 page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a2-product.md)). Best assessment as of 2026-10-10: buy-page spec is 16.5J/T; treat 14.9J/TH as the roadmap/Pro figure until Bitdeer reconciles them.

## Heat-reuse notes

- A 3729W air-cooled unit is a classic space-heating-class load: ductable airflow heat with the A2's stated -20°C to 50°C air-side operating window (per Bitdeer test data) — cold-weather installs are explicitly in vendor spec ([A2 page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a2-product.md); [shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)). Ducting practice: [Air-Cooled Hashrate Heating](air-cooled-hashrate-heating.md).
- The hydro sibling (446TH/s, 7359W shop / 7360 W AMV, 20°C to 55°C hydro loop) is the water-loop variant; see [Hydronic Heat Reuse](hydronic-heat-reuse.md) for loop design and [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md) for component limits ([shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md); [AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md)).
- At 16.5J/T the A2 is two generations behind the A4's 9.45J/T — same heat per watt, fewer TH/s per watt of heat (see [SEALMINER A4 Ultra Hydro](sealminer-a4-ultra.md)).

## See Also

- Lineup: [SEALMINER Overview](sealminer-overview.md)
- Models: [SEALMINER A2 Pro Air](sealminer-a2-pro-air.md), [SEALMINER A2 Pro Hydro](sealminer-a2-pro-hydro.md), [SEALMINER A3](sealminer-a3.md), [SEALMINER A4 Ultra Hydro](sealminer-a4-ultra.md)
- Same topic: [Air-Cooled Hashrate Heating](air-cooled-hashrate-heating.md)
- Same topic: [Hydronic Heat Reuse](hydronic-heat-reuse.md)
- Same topic: [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md)
- Same topic: [Heater Electrical and 120V Builds](heater-electrical-and-120v-builds.md)
