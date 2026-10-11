# WhatToMine — ASIC Miner Profitability Ranking (SSR extract, SHA-256 focus)

> Registry ID: whattomine
> Source: https://whattomine.com/asics
> Collected: 2026-10-10
> Published: n/d (live SSR snapshot)
> Posture: extract
> As-Of: 2026-10-10

HTTP 200, 84,611 B, full SSR table (unlike /coins, the /asics ranking IS server-rendered).

## SHA-256 rows (exact literals, per-row power cost as shown by WTM)

- "Bitmain Antminer U3S23H | Jan 2026 | 1.16 Ph/s @ 11020W | SHA-256 | $0.19/kWh | 9.50 W/Th | $49.03 | $22.58" — Top Coins Revenue: "QUAI $49.03, FB $45.88, XEC $45.68"; Top Coins Profit: "QUAI $22.58, FB $19.43, XEC $19.23"
- "Bitdeer Sealminer A4 Ultra Hydro | May 2026 | 886.00 Th/s @ 8373W | SHA-256 | $0.19/kWh | 9.45 W/Th | $37.50 | $17.40"
- "Bitmain Antminer S23 Hyd | Jan 2026 | 580.00 Th/s @ 5510W | SHA-256 | $0.19/kWh | 9.50 W/Th | $24.59 | $11.36" — Top: "QUAI $24.59, XEC $23.14, FB $23.05"
- "Bitdeer Sealminer A4 Pro Hydro | May 2026 | 680.00 Th/s @ 7412W | SHA-256 | $0.16/kWh | 10.90 W/Th | $28.81 | $11.02"

## Non-SHA reference rows (context, same SSR table)

- "Bitmain Antminer Z15 Pro | Jun 2023 | 840.00 kh/s @ 2560W | Equihash | $0.74/kWh | 3.05 W/kh | $45.77 | $39.63" (ZEC)
- "Bitmain Antminer X9 | Jul 2026 | 1.00 Mh/s @ 2500W | RandomX | $0.60/kWh | 2.50 W/kh | $35.70 | $29.70" (XMR)
- "Bitdeer Sealminer DL1 Hydro | Jun 2026 | 52.50 Gh/s @ 7850W | Scrypt | $0.15/kWh | 149.52 W/Gh | $29.11 | $10.27"

## Observations

- WTM's SHA-256 economics assume ~$0.16–0.19/kWh power cost per row (row-level assumption, not user-set).
- Best SHA-256 machines cluster at 9.45–9.50 W/Th efficiency; 10.90 W/Th hydro unit still profitable at $0.16/kWh.
- SHA-256 "Top Coins" on WTM now include QUAI, FB (Fractal Bitcoin), XEC alongside BTC — merged-mining/alt SHA-256 revenue streams materially rank above plain BTC in the revenue column.
- Implied SHA-256 revenue per TH at snapshot: S23 Hyd $24.59/day ÷ 580 Th ≈ $0.0424/Th/day (~$0.042 USD/TH/day) — consistent with Braiins' hashprice widget scale (see braiins-insights captures).
- Profit 24h column at these power costs implies S23 Hyd margin ≈ 46% of revenue ($11.36/$24.59) at $0.19/kWh.
