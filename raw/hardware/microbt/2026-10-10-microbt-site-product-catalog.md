# MicroBT — shop catalog snapshot + 2026 model map (WhatsMiner)

> Source: https://shop.whatsminer.com/products (SSR catalog) + https://www.whatsminer.com/src/views/product_manual.html (official spec-file list)
> Collected: 2026-10-10
> Published: Unknown
> Registry ID: microbt-site

## Shop catalog cards (SSR, verbatim; price shown is USD/T from card, unit price where captured)

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

## New-gen (M7x) detail-page data captured

- M73 (shop detail, verbatim): 512TH card; 14.5J/TH; Power on wall 7424.00W; PSU "AC380~480V, 3W+ ground, input 10kw"; Size "86mm*483mm*663mm with handle"; Weight "Net weight:27.5kg Gross Weight:30kg"; Coolant demand per machine "About 1L"; unit price $6,144, $12/T (HK).
- M70S (shop detail, verbatim): 248T; 13.5J/TH; Power on wall shows "No data" on the page (gap — spec only on card: 13.5J/TH ⇒ ~3,348 W implied, not stated on page).

## Official spec-file list (product_manual API, cooling map)

- Air cooling (coolingId 12): M70, M70S, M70S+, M60S++, M60S, M60, M50S++, M50S+, M50S, M50
- Hydro-cooling (coolingId 13): M7BS+, M7BS, M7B, M6BS++, M6BS+, M7AS+, M7AS, M7A, M6AS++, M6AS+, M73S+, M73S, M73, M7DS, M7D, M6DS++, M6DS+, M54S++, M53S+, M53S, M53, M53S++, M63, M63S, M63S+, M63S++, M64, M65S
- Immersion (coolingId 14): M76S+, M76S, M76, M56S+, M56S, M56, M56S++, M66, M66S, M66S+, M66S++

2026 additions in the official file list (tagged "最新"/latest, created 2026-05-07): M7BS+/M7BS/M7B, M6BS++/M6BS+, M7AS+/M7AS/M7A, M6AS++/M6AS+ (M7B/M6B = next-gen hydro family), plus M76/M76S/M76S+ immersion.

## 2025-12 home-page hero

whatsminer.com home banner (API `/renren-fast/app/home/queryList`, modified 2025-12-09): titleEn "M73S+", introductionEn "Born for mining", alt text "MicroBT WhatsMiner M70 Series / M73 Series Bitcoin Miner".

## Gaps / not capturable this run

- M64S: appears in NO current official list captured (not in shop catalog, not in spec-file list). Possibly renamed/superseded; recorded as gap.
- M66S+ / M63S+ / M64 / M65S: no shop detail pages (not retail-listed); captured from official product-manual PDFs instead.
- M66S++ / M63S++ spec sheets exist in the file list but were not downloaded (file cap).
- The old microbt.com "product center" (www.whatsminer.com/src/views/product.html) now redirects into the Nuxt shop app; no separate spec-showcase site remains reachable.
