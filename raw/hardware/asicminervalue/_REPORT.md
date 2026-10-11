# Cross-check report — current-gen flagship ASICs, ASIC Miner Value vs Mining Now (2026-10-10)

> Source: https://www.asicminervalue.com/manufacturers/{bitmain,microbt,canaan,bitdeer,auradine} + https://miningnow.com/latest-asic-miner-list/ (+ /coins/bitcoin/mining-hardware/ profitability layer)
> Collected: 2026-10-10
> Published: Unknown
> Registry ID: asicminervalue
> Posture: extract (profitability DB snapshot; volatile values As-Of — all $/day and prices are values as of 2026-10-10)

Scope: current-gen flagship set (~25–40 SKUs across 5 makers): Bitmain S21/S23, MicroBT M6xS + 2026 M7-series, Canaan A15/A14, Bitdeer SEALMINER, Auradine Teraflux. Numbers verbatim from each site's SSR HTML/flight payload as served 2026-10-10; no full-DB dumps. DesiWeMiner line (K9S 130 Th/s 4950 W; K10 Pro 170 Th/s 3825 W — reseller-listed, DesiWeMiner acquired by Bitdeer 2024-06) is NOT present on either DB (checked payload, sitemaps and vendor lists 2026-10-10) — nothing to fold in; treat as reseller-listed-only SKUs.

## SKUs found per site

| Maker | AMV (manufacturer page rows captured) | MiningNow (list-payload rows captured) |
|---|---|---|
| Bitmain | 25 | 26 |
| MicroBT | 29 | 24 |
| Canaan | 15 | 10 |
| Bitdeer | 13 | 13 |
| Auradine | 3 | 0 |
| **Total** | **85** | **73** |

Extra per-model files: 1 of ≤5 used — MiningNow Whatsminer M66S model page (`2026-10-10-miningnow-microbt-whatsminer-m66s-model-page.md`), taken to pin the top mismatch SKU's SSR profitability. Missing SKUs that have no page on either site (nothing to capture): SEALMINER A1 (MN page soft-404s; AMV 404), Teraflux AT1500/AT2860 (404 on AMV, absent on MN), Whatsminer M64/M64S/M65S (absent from both DBs), S21+ 225 Th (AMV-only, no MN page), A15XP-209T/A15Pro-221T (AMV-only).

## AMV vs MiningNow mismatches (same model, field, values)

Feeds wiki Disputed blocks. Dates: AMV publishes a single "Release" month; MiningNow separates "Announced" and "First batch (launch)" — both MN values shown. $/day profit columns are NOT directly comparable across sites (AMV nets at $0.10/kWh, MN at $0.07/kWh) — spec fields only below, plus best-price deltas >10%.

| Model | Field | ASIC Miner Value | Mining Now |
|---|---|---|---|
| Antminer S21 (200 Th) | Power (W) | 3550 | 3500 |
| Antminer S21 (200 Th) | Release/first batch | Feb 2024 (AMV Release) | Aug 2023 (MN launch; ann Aug 2023) |
| Antminer S21 Pro (234 Th) | Release/first batch | Jul 2024 (AMV Release) | Mar 2024 (MN launch; ann Mar 2024) |
| Antminer S21 Pro (245 Th) | Power (W) | 3510 | 3675 |
| Antminer S21 Pro (245 Th) | Release/first batch | Nov 2025 (AMV Release) | Mar 2024 (MN launch; ann Mar 2024) |
| Antminer S21+ (235 Th) | Release/first batch | Jun 2025 (AMV Release) | Feb 2025 (MN launch; ann Feb 2025) |
| Antminer S21 XP (270 Th) | Release/first batch | Sep 2024 (AMV Release) | Oct 2024 (MN launch; ann Jun 2024) |
| Antminer S21 XP Imm. (300 Th) | Release/first batch | Sep 2024 (AMV Release) | Oct 2024 (MN launch; ann Jun 2024) |
| Antminer S21+ Hyd (319 Th) | Release/first batch | Feb 2025 (AMV Release) | Mar 2025 (MN launch; ann Oct 2024) |
| Antminer S21+ Hyd (358 Th) | Release/first batch | Aug 2025 (AMV Release) | Mar 2025 (MN launch; ann Nov 2024) |
| Antminer S21e Hyd (288 Th) | Release/first batch | Apr 2025 (AMV Release) | May 2025 (MN launch; ann Apr 2025) |
| Antminer S21e Hyd (310 Th) | Release/first batch | Aug 2025 (AMV Release) | Sep 2025 (MN launch; ann Aug 2025) |
| Antminer S21 Hyd (335 Th) | Release/first batch | Feb 2024 (AMV Release) | Sep 2023 (MN launch; ann Sep 2023) |
| Antminer S21 XP+ Hyd (500 Th) | Best price | $8,799 | $7,556.00 |
| Antminer S21 XP+ Hyd (500 Th) | Release/first batch | Jul 2025 (AMV Release) | Mar 2025 (MN launch; ann Jan 2025) |
| Antminer S23 Imm. (442 Th) | Best price | $9,479 | $6,547.00 |
| Antminer S23 XP Hyd (600 Th) | Release/first batch | Oct 2026 (AMV Release) | Nov 2026 (MN launch; ann Aug 2026) |
| Antminer S21e XP Hyd (430 Th) | Release/first batch | Nov 2024 (AMV Release) | Mar 2025 (MN launch; ann Nov 2024) |
| Antminer S21 XP Hyd (473 Th) | Best price | $6,629 | $1,413.00 |
| Antminer S21 XP Hyd (473 Th) | Release/first batch | Nov 2024 (AMV Release) | Oct 2024 (MN launch; ann Jun 2024) |
| Antminer S21j XP Hyd (495 Th) | Best price | $6,700 | $5,450.00 |
| Antminer S23e Hyd 2U (865 Th) | Release/first batch | Apr 2026 (AMV Release) | May 2026 (MN launch; ann Jan 2026) |
| Antminer S23 Hyd 3U (1.16 Ph) | Best price | $28,599 | $12,648.00 |
| Antminer S21e XP Hyd 3U (860 Th) | Release/first batch | Jan 2025 (AMV Release) | Nov 2024 (MN launch; ann Sep 2024) |
| Antminer S23 Hyd (580 Th) | Best price | $15,800 | $12,499.00 |
| WhatsMiner M63 (334 Th) | TH/s | 334 | 360 (payload field; slug 'm63-360th-s') |
| WhatsMiner M63 (334 Th) | Power (W) | 6646 | 7200 |
| WhatsMiner M63 (334 Th) | Release/first batch | Nov 2023 (AMV Release) | Oct 2023 (MN launch; ann Oct 2023) |
| WhatsMiner M63S (390 Th) | TH/s | 390 | 406 (payload field; slug 'm63s-406th-s') |
| WhatsMiner M63S (390 Th) | Power (W) | 7215 | 7308 |
| WhatsMiner M63S (390 Th) | Release/first batch | Nov 2023 (AMV Release) | Oct 2023 (MN launch; ann Oct 2023) |
| WhatsMiner M63S+ (424 Th) | TH/s | 424 | 450 (payload field; slug 'm63s-plus-450th-s') |
| WhatsMiner M63S+ (424 Th) | Power (W) | 7208 | 7650 |
| WhatsMiner M63S+ (424 Th) | Release/first batch | Aug 2024 (AMV Release) | Jul 2024 (MN launch; ann Jul 2024) |
| WhatsMiner M63S++ (464 Th) | TH/s | 464 | 478 (payload field; slug 'm63s-plus-plus-478th-s') |
| WhatsMiner M63S++ (464 Th) | Power (W) | 7200 | 10000 |
| WhatsMiner M66 (280 Th) | TH/s | 280 | 276 (payload field; slug 'm66-276th-s') |
| WhatsMiner M66 (280 Th) | Power (W) | 5572 | 5492 |
| WhatsMiner M66 (280 Th) | Release/first batch | Nov 2023 (AMV Release) | Oct 2023 (MN launch; ann Oct 2023) |
| WhatsMiner M66S (298 Th) | TH/s | 298 | 310 (payload field; slug 'm66s-310th-s') |
| WhatsMiner M66S (298 Th) | Power (W) | 5513 | 5580 |
| WhatsMiner M66S (298 Th) | Release/first batch | Nov 2023 (AMV Release) | Oct 2023 (MN launch; ann Oct 2023) |
| WhatsMiner M66S+ (318 Th) | Release/first batch | Aug 2024 (AMV Release) | Jul 2024 (MN launch; ann Jul 2024) |
| WhatsMiner M66S++ (356 Th) | TH/s | 356 | 348 (payload field; slug 'm66s-plus-plus-348th-s') |
| WhatsMiner M66S++ (356 Th) | Power (W) | 5518 | 5394 |
| WhatsMiner M7AS+ (540 Th) | J/TH | 12.5 (homepage) | 13.89 |
| WhatsMiner M7AS+ (540 Th) | Release/first batch | Oct 2026 (AMV Release) | Nov 2026 (MN launch; ann Sep 2026) |
| Avalon A15-194T (194 Th) | Release/first batch | Dec 2024 (AMV Release) | Jan 2025 (MN launch; ann Nov 2024) |
| Avalon A15Pro-218T (218 Th) | TH/s | 218 | 220 (payload field; slug 'canaan-avalon-a15-pro-218th-s') |
| Avalon A15Pro-218T (218 Th) | Release/first batch | Feb 2025 (AMV Release) | Dec 2024 (MN launch; ann Nov 2024) |
| Avalon A16XP-300T (300 Th) | Release/first batch | Apr 2026 (AMV Release) | May 2026 (MN launch; ann Oct 2025) |
| Avalon A1566I (261 Th) | TH/s | 261 | 249 (payload field; slug 'canaan-avalon-a1566i-249th-s') |
| Avalon A1566I (261 Th) | Release/first batch | Jul 2024 (AMV Release) | Dec 2024 (MN launch; ann Sep 2024) |
| Avalon A1566HA 2U (480 Th) | Release/first batch | Jun 2025 (AMV Release) | Jul 2025 (MN launch; ann Jun 2025) |
| Avalon Made A1346 (110 Th) | Release/first batch | Nov 2022 (AMV Release) | Oct 2022 (MN launch; ann Oct 2022) |
| Avalon Made A1366 (130 Th) | Release/first batch | Nov 2022 (AMV Release) | Oct 2022 (MN launch; ann Nov 2022) |
| Avalon Miner A1366I (119 Th) | TH/s | 119 | 122 (payload field; slug 'canaan-avalon-a1366i-122th-s') |
| Avalon Miner A1366I (119 Th) | Release/first batch | May 2024 (AMV Release) | Jul 2023 (MN launch; ann May 2023) |
| SealMiner A2 (226 Th) | Power (W) | 3730 | 3729 |
| SealMiner A2 (226 Th) | Release/first batch | Feb 2025 (AMV Release) | Dec 2024 (MN launch; ann Nov 2024) |
| SealMiner A2 Hyd (446 Th) | Power (W) | 7360 | 7359 |
| SealMiner A2 Hyd (446 Th) | Release/first batch | Feb 2025 (AMV Release) | Dec 2024 (MN launch; ann Nov 2024) |
| SealMiner A3 Air (260 Th) | Release/first batch | Sep 2025 (AMV Release) | Oct 2025 (MN launch; ann Sep 2025) |
| SealMiner A3 Hydro (500 Th) | Release/first batch | Sep 2025 (AMV Release) | Oct 2025 (MN launch; ann Sep 2025) |
| SealMiner A3 Pro Air (290 Th) | Release/first batch | Sep 2025 (AMV Release) | Oct 2025 (MN launch; ann Sep 2025) |
| SealMiner A3 Pro Hydro (660 Th) | Best price | $12,760 | $7,449.00 |
| SealMiner A3 Pro Hydro (660 Th) | Release/first batch | Sep 2025 (AMV Release) | Oct 2025 (MN launch; ann Sep 2025) |

AMV-only SKUs (9): Antminer S21+ (225 Th), Avalon Made A1446 (135 Th), WhatsMiner M79 (920 Th), WhatsMiner M7AS (520 Th), WhatsMiner M7BS+ (540 Th), WhatsMiner M76S+ (390 Th), Avalon A15Pro-221T (221 Th), Avalon A15XP-209T (209 Th), Auradine Teraflux AT2880 (180 Th) / AI3680 (360 Th) / AH3880 (600 Th) — all Auradine absent on MN

MiningNow-only SKUs among the captured set: Antminer S21 Hyd (302 Th), Antminer S21+ Hydro (395 Th), Avalon A15 Pro+ (240 Th)

## Signal lines

1. **Efficiency (J/TH as listed, 2026-10-10)** — flagship ladder: Bitmain S23 XP Hyd 8.9 j/Th (600 Th, 5340 W) → Bitdeer A4 Ultra Hyd 9.45 (886 Th, 8372 W) → Bitmain S23 Hyd/S23e Hyd 2U 9.5–10 → air-cooled leaders: S23 318 Th @ 11 (MN) and Bitdeer A4 Pro Air 10.9; AMV- and MN-listed MicroBT air flagship M70S+ lands 12.87–13.89 j/Th. Hydro/3U boxes (S21e XP Hyd 3U 13 j/Th, M79S 14.81 j/Th) trail the 6U hydro class.
2. **Hydro vs air naming**: AMV encodes cooling in the model name suffix (Hyd / Imm. / 3U / 2U) and reserves "Hyd" for true hydro SKUs; MiningNow uses a separate cooling field and tags the *air-cooled* M63/M63S/M66/M66S/M73/M76/M79 family as `hydro` (M66S page copy: "efficient Liquid cooling system") — a naming-practice dispute for the wiki. Both sites agree S21-series hydro variants (S21+ Hyd, S21 XP Hyd, S21e Hyd) are hydro.
3. **Price ranges (best price as shown, values as of 2026-10-10)** — air flagships: $968 (S21 200 Th, MN) to $5,647 (S23 318 Th, MN) / $16,399 (S23 XP Hyd, AMV home); hydro 2U/3U big-boxes: $8,482–$12,760 on AMV vs $7,449–$12,648 on MN. Reseller-tier MN prices run consistently below AMV's best price on identical SKUs — e.g. S23 Hyd 3U $12,648 (MN) vs $28,599 (AMV); S21 XP Hyd $1,413 (MN) vs $6,629 (AMV); A3 Pro Hydro $7,449 (MN) vs $12,760 (AMV).
4. **2026 next-gen is already in both DBs**: Bitmain S23 family (air 318 Th Jan 2026 → S23 Hyd 3U 1.16 Ph @ 9.5 j/Th, S23 XP Hyd 600 Th @ 8.9 j/Th Oct 2026), MicroBT M7-series (M79S 1.35 Ph @ 14.81 j/Th; M7DS 680 Th @ 13.53 j/Th; M7A/M7AS/M7AS+ 2026), Canaan A16-282T / A16XP-300T (13.83 / 12.83 j/Th), Bitdeer A4 Pro/Ultra (10.9 / 9.45 j/Th) — while Auradine's newest listed rows remain AT2880/AI3680/AH3880 (Nov 2024–Mar 2025) and AT1500/AT2860 are absent everywhere.
5. **Profitability columns are rate-shifted, not comparable raw**: AMV standard $0.10/kWh ("Profit = coin rewards − electricity cost"; manufacturer-page SSR cells are electricity-cost-only negatives, e.g. S23 Hyd 3U −$26.45/day) vs MN default $0.07/kWh (site-rendered S23 Hyd 3U $27.00/day net at BTC $83,062.25). Normalized gross income agrees within ~1% where specs agree: S23 Hyd 3U $45.89/day gross (AMV homepage profit $19.44 + elec $26.45) vs $45.51/day (MN payload income) — the residual gap tracks BTC price drift between snapshots, while the M66S/M63 family gross gap (MN $12.48 vs AMV n/a) is itself a product of the TH/s dispute (298 vs 310).

## Cross-check method notes

- AMV: manufacturer listing pages carry the full model table SSR (Bitmain 141 rows, MicroBT 56, Canaan 29, Bitdeer 13, Auradine 3); flagship subsets captured above. AMV homepage top-20 leaderboard used as the only AMV surface showing J/TH + best price + net profit; it covers 14 of the flagship SKUs.
- MiningNow: single latest-list page embeds all 439 products in the Next.js flight payload; maker rows extracted verbatim. Rendered profitability verified live in-browser against the payload formula (income − W×24×$0.07) — matches exactly (S23 Hyd 3U $27.00, A4 Ultra Hyd $20.70).
- Both DBs volatile: all values stamped values as of 2026-10-10; MN page data stamp 2026-10-11 UTC.
