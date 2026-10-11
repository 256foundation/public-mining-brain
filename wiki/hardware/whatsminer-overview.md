# Whatsminer Overview

> Sources: shop.whatsminer.com catalog + detail pages and the official whatsminer.com spec-file list (SSR/API, verbatim); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [MicroBT shop catalog + 2026 model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [M66S shop + manual](../../raw/hardware/microbt/2026-10-10-microbt-site-m66s.md); [M66S+ manual](../../raw/hardware/microbt/2026-10-10-microbt-site-m66s-plus.md); [M63S+ manual](../../raw/hardware/microbt/2026-10-10-microbt-site-m63s-plus.md); [M64 manual](../../raw/hardware/microbt/2026-10-10-microbt-site-m64.md); [M65S manual](../../raw/hardware/microbt/2026-10-10-microbt-site-m65s.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [MiningNow MicroBT rows](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md); [MiningNow M66S model page](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt-whatsminer-m66s-model-page.md); [AMV/MN cross-check report](../../raw/hardware/asicminervalue/_REPORT.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

MicroBT's Whatsminer line as it ships and as the profitability databases list it, as of 2026-10-10. Per-model pages: [Whatsminer M66S](whatsminer-m66s.md), [Whatsminer M66S+](whatsminer-m66s-plus.md), [Whatsminer M63S+](whatsminer-m63s-plus.md), [Whatsminer M64](whatsminer-m64.md), [Whatsminer M65S](whatsminer-m65s.md), [Whatsminer M70S](whatsminer-m70s.md), [Whatsminer M73](whatsminer-m73.md).

## The shipping ladder (shop catalog, 2026-10-10)

shop.whatsminer.com fronts 17 SKUs. Read by efficiency tier, the ladder of what is actually retail-listed runs:

- **M70S** — 248TH card, 13.5J/TH, $13.0/T (HK) — the efficiency flagship on the shop
- **M73** — 512TH, 14.5J/TH, $12.0/T (HK; unit price $6,144; power on wall 7424.00W)
- **M63S++** — 464TH, 15.5J/TH, $10.0/T (the M60S++ 218TH sits at the same 15.5J/TH tier)
- **M60S+** — 200TH, 17J/TH, $16.0/T
- **M66S** — 286~290TH, 18.5J/TH, $9.0/T (HK; unit price $2,574)

Below that: the 19.9J/TH value tier (M66 276TH, M63 372TH, M60 160TH — all $8.0/T) and the M50/M30 legacy tail down to 34J/TH. Prices are card asks as served 2026-10-10, not street prices.

## Shop catalog (SSR, verbatim)

| Model | Hashrate | Efficiency | Price/T | Warehouse | pid/skuId |
|---|---|---|---|---|---|
| MICROBT WhatsMiner M70S | 248TH | 13.5J/TH | $13.0 | HK | 79/190 |
| MICROBT WhatsMiner M73 | 512TH | 14.5J/TH | $12.0 | HK | 80/191 |
| MICROBT WhatsMiner M63S++ | 464TH | 15.5J/TH | $10.0 | HK | 75/170 |
| MICROBT WhatsMiner M60S++ | 218TH | 15.5J/TH | $10.0 | HK | 74/169 |
| MICROBT WhatsMiner M60S+ | 200TH | 17J/TH | $16.0 | HK | 71/154 |
| MICROBT WhatsMiner M66S | 286~290TH | 18.5J/TH | $9.0 | HK (unit $2,574) | 69/148 |
| MICROBT WhatsMiner M66 | 276TH | 19.9J/TH | $8.0 | HK | 68/134 |
| MICROBT WhatsMiner M63S | 408T | 18J/T | $9.0 | USA (unit $3,672 per card) | 67/132 |
| MICROBT WhatsMiner M63 | 372TH | 19.9J/TH | $8.0 | USA | 57/112 |
| MICROBT WhatsMiner M60S | 184~188TH | 18.5J/TH | $9.0 | HK | 66/188 |
| MICROBT WhatsMiner M60 | 160TH | 19.9J/TH | $8.0 | HK | 65/166 |
| MICROBT WhatsMiner M50S++ | 154~162TH | 21J/TH | $10.6 | USA | 56/186 |
| MICROBT WhatsMiner M50S+ | 148T | 23J/T | $7.8 | USA | 55/110 |
| MICROBT WhatsMiner M50S | 124TH | 26J/TH | $6.0 | USA | 54/175 |
| MICROBT WhatsMiner M50 | 124TH | 28J/TH | $6.0 | USA | 53/179 |
| MICROBT WhatsMiner M30S++ | 102~104TH | 31J/TH | $7.0 | USA | 52/139 |
| MICROBT WhatsMiner M30S+ | 100TH | 34J/TH | $4.6 | USA | 50/150 |

## Spec-sheet gaps: the image-only PERFORMANCE charts

- The official manuals for the M66S+, M63S+, M64 and M65S carry no text-form performance numbers: the PERFORMANCE section is chart images only (the M66S+ sheet notes "样机数据仅供参考" — prototype data for reference only). Hashrate-vs-temperature and per-mode wall-draw curves have to be read off images, so several spec fields below stop at the rating line.
- Retail pages have the same class of gap: the M70S detail page shows Power on wall as "No data" — the capture notes 13.5J/TH ⇒ ~3,348 W implied from the card, not stated on the page.
- Where a wall-power figure exists in text at all, it comes from the shop page, not the manual: M73 7424.00W, M66S 5291.00W (shop pages).

## Next-gen M7B/M6B family status

- Official spec-file additions tagged "最新"/latest, created 2026-05-07: M7BS+/M7BS/M7B, M6BS++/M6BS+, M7AS+/M7AS/M7A, M6AS++/M6AS+ (M7B/M6B = next-gen hydro family), plus M76/M76S/M76S+ immersion.
- Already in the profitability DBs on 2026-10-10: M7A (470 Th/s @ 10000 W, Jul 2026; MiningNow lists 21.28 j/Th), M7AS (520 Th/s @ 7500 W, AMV only — no MiningNow row), M7AS+ (540 Th/s @ 7500 W; AMV homepage says 12.5j/Th, MiningNow 13.89 j/Th — disputed below), M7BS+ (540 Th/s @ 10000 W, AMV only). The M7B/M7BS and M6B sheets themselves have no shop detail pages and no DB rows captured — paper launch as of this snapshot.
- Top of the maker's DB income ladder: M79S (1.35 Ph/s @ 20000 W, Dec 2025), listed at 14.815j/Th on the AMV homepage and 14.81 j/Th on MiningNow.
- Home-page hero banner (API, modified 2025-12-09): "M73S+" — "Born for mining".

## Air vs hydro vs immersion: naming conventions

- MicroBT's own spec-file map: air cooling (coolingId 12): M70, M70S, M70S+, M60S++, M60S, M60, M50S++, M50S+, M50S, M50; hydro-cooling (coolingId 13): M7BS+, M7BS, M7B, M6BS++, M6BS+, M7AS+, M7AS, M7A, M6AS++, M6AS+, M73S+, M73S, M73, M7DS, M7D, M6DS++, M6DS+, M54S++, M53S+, M53S, M53, M53S++, M63, M63S, M63S+, M63S++, M64, M65S; immersion (coolingId 14): M76S+, M76S, M76, M56S+, M56S, M56, M56S++, M66, M66S, M66S+, M66S++.
- AMV encodes cooling in the model-name suffix (Hyd / Imm. / 2U / 3U) and reserves Hyd for true hydro SKUs. MiningNow keeps a separate cooling field but tags the M63/M66/M73/M76/M79 family `hydro` — including units MicroBT classes as air or immersion; its M66S page copy reads "With an efficient Liquid cooling system". Treat MiningNow cooling tags as noisy for this maker; the maker sheet wins.
- Wiki convention: model articles use the bare maker model name, state the maker cooling class in Specs, and keep DB cooling tags inside the dispute blocks.

## The M64S rename flag

- M64S appears in no current official list captured — not in the shop catalog, not in the spec-file list. Recorded as a gap; possibly renamed or superseded.
- Both profitability DBs omit M64/M64S/M65S entirely on 2026-10-10. The community heater record references a later M64S keeping the M64 form factor (see [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md)).

## Cross-check disputes (AMV vs MiningNow, 2026-10-10)

> **Status: Disputed** — MicroBT M6x/M7x family: the two DBs disagree on hashrate, wall power, efficiency and release dates across the family; maker sheets are the tiebreaker where they exist (field-by-field below). Note the $0.10-vs-$0.07/kWh profitability caveat — "Normalized gross income agrees within ~1% where specs agree"; AMV manufacturer-page profit cells are electricity-cost-only negatives at its standard $0.10/kWh.

| Model | Field | ASIC Miner Value | Mining Now |
|---|---|---|---|
| M66S | Hashrate | 298 Th/s | 310TH/s |
| M66S | Wall power | 5513 W | 5580 W |
| M66S | Release | Nov 2023 | ann Oct 20, 2023 / first batch Oct 25, 2023 |
| M66S+ | Release | Aug 2024 | Jul 2024 (ann + first batch) |
| M66S++ | Hashrate | 356 Th/s | 348TH/s |
| M66S++ | Wall power | 5518 W | 5394 W |
| M63S+ | Hashrate | 424 Th/s | 450TH/s |
| M63S+ | Wall power | 7208 W | 7650 W |
| M63S++ | Hashrate | 464 Th/s | 478TH/s |
| M63S++ | Wall power | 7200 W | 10000 W |
| M7AS+ | J/TH | 12.5j/Th (homepage) | 13.89 j/Th |
| M7AS+ | Release | Oct 2026 | ann Sep 2026 / first batch Nov 2026 |

- Headline cases: M66S 298 Th/s vs 310TH/s (power 5513 W vs 5580 W) and M63S+ 424 Th/s vs 450TH/s (7208 W vs 7650 W) — on the M63S+ both DB values sit inside the maker's 390T ～ 450T ±10% band. The M63S++ power row (7200 W vs 10000 W) is the largest single-field gap in the family.
- Full 67-row mismatch list: [AMV/MN cross-check report](../../raw/hardware/asicminervalue/_REPORT.md).

## Heat-reuse notes

- Cooling classes across the current family: air (M70/M70S/M70S+ and the M60/M50 value tiers); immersion (M66S family — dedicated insulating-liquid loop, S5X/S3X, rated flow ≥ 24 L/min, inlet 25 °C – 55 °C); hydro 2U-rack big-boxes (M63S+/M65S/M73 — flows ≥ 10 L/min and ≥ 5 L/min, outlets up to 70 °C and 80 °C respectively); and the compact hydro M64 (371mm × 290 mm × 109mm, ≥ 3.5 L/min, 80 °C outlet, single-phase 220–277 V input) — the heater-fit unit.
- Heater builds around the compact hydro chassis: [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md). Loop design and chemistry: [Hydronic Heat Reuse](hydronic-heat-reuse.md). Air-side reuse: [Air-Cooled Hashrate Heating](air-cooled-hashrate-heating.md).

## See Also

- [Whatsminer M66S](whatsminer-m66s.md) · [Whatsminer M66S+](whatsminer-m66s-plus.md) · [Whatsminer M63S+](whatsminer-m63s-plus.md) · [Whatsminer M64](whatsminer-m64.md) · [Whatsminer M65S](whatsminer-m65s.md) · [Whatsminer M70S](whatsminer-m70s.md) · [Whatsminer M73](whatsminer-m73.md)
- [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md), [Hydronic Heat Reuse](hydronic-heat-reuse.md)
