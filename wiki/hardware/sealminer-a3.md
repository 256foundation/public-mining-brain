# SEALMINER A3

> Sources: Bitdeer shop catalog A3 series claims (bitdeer.com/shop, 2026-10-10); Bitdeer SEALMINER roadmap (2026-10-10); ASIC Miner Value + MiningNow DBs (2026-10-10). No A3 product page was captured (file cap) — per-model data below is shop-listing + series copy + DB rows.
> Raw: [Bitdeer shop SEALMINER catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md); [SEALMINER roadmap (SEAL01–SEAL04)](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md); [ASIC Miner Value — Bitdeer listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md); [MiningNow — Bitdeer rows](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md); [AMV/MN cross-check report](../../raw/hardware/asicminervalue/_REPORT.md); [Bitdeer capture report](../../raw/hardware/bitdeer/_REPORT.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

The SEALMINER A3 series is Bitdeer's SEAL03-chip generation — four SKUs spanning air- and hydro-cooling. Shop listing, As-Of 2026-10-10: A3 Hydro 6750W at $6,750 ($13.5/T) with coupon $6,411 ($12.82/T), A3 Pro Hydro 8250W at $9,900 ($15/T) with coupon $9,478 ($14.36/T) — both Buy Now; A3 Air 3640W and A3 Pro Air 3625W — both Pre-Order with no price shown ([shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)). Chip: SEAL03, "Released in Q1 2025", "Power efficiency of 9.7J/TH" ([roadmap](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md)).

## Specs (Bitdeer shop, As-Of 2026-10-10)

Series claims (verbatim from the shop's embedded page data; there is no captured per-model spec table) ([shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)):

- Range: "Built on the same A3 chip, the lineup spans 240–690 TH/s across air- and hydro-cooling variants—flexible enough for plug-and-play setups or high-throughput mining farms."
- Efficiency split: "With A3 Pro models reaching 12.5 J/TH and A3 models between 13.5–14 J/TH, the A3 series sets a new bar for energy-to-performance optimization."
- PSU: "A3 All models are equipped with high-efficiency power supplies achieving up to 97% efficiency"
- Packaging: "A3 Air-cooling models feature compact builds for flexible site compatibility and strong thermal performance; hydro-cooling models use a 2U server form factor for dense racking and centralized maintenance."
- Acoustics: "A3 Air-cooling units run 3–4 dB quieter than typical models; hydro-cooling units are near-silent"

Roadmap header strip (shop + roadmap pages): "SEALMINER A3 Pro Hydro — 660T | 12.5J/T — $9,900 ($15/T) / $9,478 ($14.36/T) — Buy Now" ([shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md); [roadmap](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md)).

Per-SKU figures (shop listing power/price; DB hashrates — the shop SSR listing itself prints no TH/s) ([shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md); [AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md); [MN](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md)):

| SKU | Shop power | Shop price | AMV row | MN row |
|---|---|---|---|---|
| A3 Air | 3640W, Pre-Order | — | 260 Th/s, Sep 2025 | 260TH/s, 14 j/Th, $4,173.00, first batch Oct 2025 |
| A3 Pro Air | 3625W, Pre-Order | — | 290 Th/s, Sep 2025 | 290TH/s, 12.5 j/Th, $4,308.00, first batch Oct 2025 |
| A3 Hydro | 6750W, $6,750 ($13.5/T) | coupon $6,411 ($12.82/T) | 500 Th/s, Sep 2025 | 500TH/s, 13.5 j/Th, $6,800.00, first batch Oct 2025 |
| A3 Pro Hydro | 8250W, $9,900 ($15/T) | coupon $9,478 ($14.36/T) | 660 Th/s, Sep 2025 | 660TH/s, 12.5 j/Th, first batch Oct 2025 |

Note the tension between the series copy (A3 non-Pro at "13.5–14 J/TH") and the listed units: MN shows the A3 Hydro at 13.5 j/Th but the A3 Air at 14 j/Th; roadmap attributes "Power efficiency of 12.5J/TH" to the A3 generation as a whole while the shop reserves 12.5 J/TH for the Pro models ([roadmap](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md); [shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md); [MN](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md)).

## Cross-check

- **Release dating (all four SKUs):** AMV Release Sep 2025 vs MiningNow announced Sep 2025 with first batch Oct 2025 — the recurring AMV-vs-MN convention gap, logged per SKU in the cross-check report ([cross-check](../../raw/hardware/asicminervalue/_REPORT.md)).
- **A3 Pro Hydro best price:** AMV homepage $12,760 (€11,390, $19 / Th, profit $6.31/day) vs MN $7,449.00 — the cross-check report flags this as an example of "Reseller-tier MN prices run consistently below AMV's best price on identical SKUs" ([AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md); [MN](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md); [cross-check](../../raw/hardware/asicminervalue/_REPORT.md)).
- **Vendor vs roadmap timeline:** roadmap says A3 "Mass production and delivery started in Q4 2025"; AMV lists Release Sep 2025 — both vendor-adjacent claims, captured verbatim, not yet reconciled ([roadmap](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md); [AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md)).
- **Vendor price vs DB prices (A3 Pro Hydro):** shop $9,900 ($15/T) → coupon $9,478 ($14.36/T), against AMV $12,760 and MN $7,449.00 — three different price points for one SKU on one day ([shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md); [AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md); [MN](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md)).

## Heat-reuse notes

- **Hydro SKUs (A3 Hydro 6750W, A3 Pro Hydro 8250W)** are heater-class: 2U server packaging with hydro-cooling units described as "near-silent", for "dense racking and centralized maintenance" ([shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)). An 8250W 2U box is in the same heat class as the A2 Pro Hydro (7450W) — see [SEALMINER A2 Pro Hydro](sealminer-a2-pro-hydro.md) and [Hydronic Heat Reuse](hydronic-heat-reuse.md).
- **Air SKUs (A3 Air 3640W, A3 Pro Air 3625W)** are space-heater-class air loads with the vendor's "3–4 dB quieter" acoustic claim — relevant to in-home placement ([shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)); see [Air-Cooled Hashrate Heating](air-cooled-hashrate-heating.md).
- The A3 Pro Hydro's 12.5 J/TH (AMV homepage lists 12.5j/Th) is mid-ladder: better than the A2 generation (14.9–16.5), behind the A4's 9.45J/T ([AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md); [roadmap](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md)).

## See Also

- Lineup: [SEALMINER Overview](sealminer-overview.md)
- Models: [SEALMINER A2](sealminer-a2.md), [SEALMINER A2 Pro Air](sealminer-a2-pro-air.md), [SEALMINER A2 Pro Hydro](sealminer-a2-pro-hydro.md), [SEALMINER A4 Ultra Hydro](sealminer-a4-ultra.md)
- Same topic: [Hydronic Heat Reuse](hydronic-heat-reuse.md)
- Same topic: [Air-Cooled Hashrate Heating](air-cooled-hashrate-heating.md)
- Same topic: [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md)
