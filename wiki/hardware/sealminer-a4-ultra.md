# SEALMINER A4 Ultra Hydro

> Sources: Bitdeer SEALMINER A4 Ultra Hydro product page (bitdeer.com/shop/product/P260328000003, 2026-10-10); Bitdeer shop catalog + SEALMINER roadmap (2026-10-10); ASIC Miner Value + MiningNow DBs (2026-10-10)
> Raw: [SEALMINER A4 Ultra Hydro product page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a4-ultra-hydro-product.md); [Bitdeer shop SEALMINER catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md); [SEALMINER roadmap (SEAL01–SEAL04)](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md); [ASIC Miner Value — Bitdeer listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md); [MiningNow — Bitdeer rows](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md); [AMV/MN cross-check report](../../raw/hardware/asicminervalue/_REPORT.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

The SEALMINER A4 Ultra Hydro is Bitdeer's 2026 flagship and the current efficiency leader of the SEALMINER line: 886T at 9.45J/T from 8372.7W, on the SEAL04 chip. At capture it had no retail price — shop status "Learn More / Stay tuned" (`retailBuying` disabled, presell type: Presell) — with the hero banner "SEALMINER A4 Ultra Hydro — 886T | 9.45J/T — Stay tuned" ([A4 Ultra page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a4-ultra-hydro-product.md); [shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)). Series framing: "SEALMINER A4 — Hashrate up to 900 TH/s, Power efficiency as low as 9.45 J/TH" ([A4 Ultra page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a4-ultra-hydro-product.md); [shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)).

## Specs (Bitdeer shop, As-Of 2026-10-10)

From the product page listing ([A4 Ultra page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a4-ultra-hydro-product.md)):

| Item | Value |
|---|---|
| Product | SEALMINER A4 Ultra Hydro |
| Subtitle | BTC/BCH/BSV SHA256 Hydro-cooling Miner |
| Hashrate | 886T |
| Power consumption | 8372.7W |
| Power efficiency | 9.45J/T |
| Price | none published — "Learn More / Stay tuned" (`retailBuying` disabled, presell type: Presell); price field in page data = 0 |
| Weight | 23.5 KG |
| Product group key | `A4Ultra-Hydro-Common-Product` |
| Chip | SEAL04 (roadmap: "Released in Q4 2025") |

Series claims (verbatim, from embedded page data) ([A4 Ultra page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a4-ultra-hydro-product.md); [shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)):

- "Led by the A4 Ultra Hydro, we've pushed power efficiency down to 9.45 J/TH* , shattering the 10-point ceiling. The A4 Pro series also maintains a stable 10.9 J/TH* ."
- "From up to 900 TH/s* on the A4 Ultra Hydro, to 730 TH/s* at the upper end of the A4 Pro Hydro range, and 360 TH/s* for the A4 Pro Air, the A4 series defines a clear hashrate tier."
- "Leveraging advanced hydro cooling, the A4 Ultra Hydro and A4 Pro Hydro ensure stable operations across a broad spectrum of 20°C to 55°C, effectively mitigating chip thermal fatigue."

Sibling SKUs (shop listing, both Pre-Order, no price): A4 Pro Air 3662.4W; A4 Pro Hydro 7412W ([shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)).

Roadmap context (captured claims, forward-dated): SEAL04 chip "Released in Q4 2025" with "Power efficiency ranges from 6 J/TH to 7 J/TH" at chip level; "SEALMINER A4 — Power efficiency of 9.45J/TH. Expected to start mass production and delivery in Q3 2026" ([roadmap](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md)).

## Cross-check

**ASIC Miner Value row** (manufacturer listing; Profit cells on this page type are electricity-cost-only negatives at the site's $0.10/kWh rate, top-coin column empty) ([AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md)):

| Model (as listed) | Release | Hashrate | Power | Algorithm | Profit (as shown) |
|---|---|---|---|---|---|
| Bitdeer SealMiner A4 Ultra Hydro (886 Th) | May 2026 | 886 Th/s | 8372 W | SHA-256 | -$20.09 /day |

AMV homepage top-20 row (same DB, the only AMV surface showing J/TH + best price + net profit) ([AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md)):

| Model | Release | Hashrate | Power | Efficiency (as listed) | Best price (as listed) | Profit (as listed) |
|---|---|---|---|---|---|---|
| Bitdeer SealMiner A4 Ultra Hydro | May 2026 | 886 Th/s | 8372 W | 9.449j/Th | $9,999 $11 / Th | $14.96 /day |

**MiningNow row** (profit at the site's $0.07/kWh default rate) ([MN](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md)):

| Model (as listed) | Hashrate | Power | Efficiency (as listed) | Best price | Income $/day | Profit $/day | Announced | First batch | Cooling |
|---|---|---|---|---|---|---|---|---|---|
| Bitdeer SealMiner A4 Ultra Hyd (886TH/s) | 886TH/s | 8372 W | 9.45 j/Th | $9,999.00 | 34.76 | 20.70 | Apr 2026 | May 2026 | hydro |

- **Agreement:** 886 and 8372 W agree across vendor and both DBs (shop 8372.7W vs DB 8372 W is display rounding); efficiency 9.45 agrees (AMV homepage prints 9.449j/Th); both DBs date the SKU May 2026 and price it $9,999 — while Bitdeer itself still shows no price ([AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md); [MN](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md); [A4 Ultra page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a4-ultra-hydro-product.md)).

> **Status: Disputed** (hashrate: listed unit vs marketing maximum)
> Product page lists 886T; series marketing says "up to 900 TH/s*" with the asterisk pointing to Bitdeer's variance disclaimer (±10% hashrate). Best assessment as of 2026-10-10: 886T is the listed unit spec; 900 TH/s is an asterisked marketing ceiling, not a SKU variant ([A4 Ultra page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a4-ultra-hydro-product.md); [shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)).

> **Status: Disputed** (price: none from vendor, two from DBs)
> No Bitdeer retail price exists at capture ("Stay tuned"; price field = 0). AMV homepage shows $9,999 ($11 / Th); MN shows $9,999.00. Treat both as third-party DB prices for an unshipped SKU, not vendor pricing ([A4 Ultra page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a4-ultra-hydro-product.md); [AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitdeer.md); [MN](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md)).

- **Roadmap framing:** the Q3 2026 mass-production date is a forward-looking roadmap claim ("Expected to start mass production and delivery in Q3 2026"), not an observed ship date; as of 2026-10-10 the shop still gates the SKU behind "Stay tuned" while DBs already list first batch May 2026 — the two stories have not converged ([roadmap](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md); [MN](../../raw/hardware/miningnow/2026-10-10-miningnow-bitdeer.md)).
- **Ladder context (cross-check report):** flagship efficiency ladder reads "Bitmain S23 XP Hyd 8.9 j/Th (600 Th, 5340 W) → Bitdeer A4 Ultra Hyd 9.45 (886 Th, 8372 W)" — the A4 Ultra is second only to Bitmain's S23 XP Hydro on listed J/TH as of 2026-10-10 ([cross-check](../../raw/hardware/asicminervalue/_REPORT.md)).

## Heat-reuse notes

- **Heater-class hardware on the roadmap.** 8372.7W of heat per 2U-class hydro box with a "20°C to 55°C" hydro operating window — the same plumbing problem class as the A2 Pro Hydro (7450W) and the M64-family heaters, at the top of the SEALMINER efficiency ladder ([A4 Ultra page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a4-ultra-hydro-product.md); [shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)). Loop design: [Hydronic Heat Reuse](hydronic-heat-reuse.md).
- **Efficiency ≠ less heat.** At 9.45J/T every watt still leaves as heat — the gain is hashrate per watt of heat (886T per 8372.7W vs the A2 Pro Hydro's 500T per 7450W), not a smaller heating load. For heat buyers the A4 is the same-size heater with more hashrate attached ([A4 Ultra page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a4-ultra-hydro-product.md); [A2 Pro Hydro page](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-a2-pro-hydro-product.md)).
- **Availability caveat.** Until the Q3 2026 mass-production date lands, this is a roadmap product: no vendor price, presell-gated shop page — plan heat-reuse deployments around shipping SKUs (A2 Pro Hydro, A3 Hydro/Pro Hydro) and treat the A4 as the next-generation drop-in ([roadmap](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md); [shop catalog](../../raw/hardware/bitdeer/2026-10-10-bitdeer-shop-sealminer-catalog.md)).
- Chip headroom: SEAL04's "6 J/TH to 7 J/TH" chip-level target implies further efficiency (not heat) gains in later A4 bins ([roadmap](../../raw/hardware/bitdeer/2026-10-10-bitdeer-sealminer-roadmap-chips.md)).

## See Also

- Lineup: [SEALMINER Overview](sealminer-overview.md)
- Models: [SEALMINER A2](sealminer-a2.md), [SEALMINER A2 Pro Air](sealminer-a2-pro-air.md), [SEALMINER A2 Pro Hydro](sealminer-a2-pro-hydro.md), [SEALMINER A3](sealminer-a3.md)
- Same topic: [Hydronic Heat Reuse](hydronic-heat-reuse.md)
- Same topic: [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md)
- Same topic: [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md)
- Economics: [Hashrate Heating Economics](../economics/hashrate-heating-economics.md)
