# Whatsminer M63S

> Sources: shop.whatsminer.com detail page (captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [M63S shop page](../../raw/hardware/microbt/2026-10-11-microbt-site-m63s.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [MiningNow MicroBT rows](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The 18 J/T hydro rung — 408 T banner rating on the 70°C-outlet hydro generation ([M63 manual](../../raw/hardware/microbt/2026-10-11-microbt-site-m63.md)). The shop page carries no manual attachment (gap noted in the capture); the spec record for this unit is the shop banner + tab ([MicroBT catalog](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md)).

## Specs (manufacturer, As-Of 2026-10-11)

Shop banner + tab, verbatim ([M63S shop page](../../raw/hardware/microbt/2026-10-11-microbt-site-m63s.md)):

- Hashrate: 408T; Power efficiency: "18J/T" (as printed on the banner — "J/T", not the family's usual "J/TH"); Power on wall: 7344.00W; listing type SPOT, warehouses HK/USA
- Specification tab: PSU "AC380~480V, 3W+ ground, input 10kw"; Size "86mm*483mm*663mm with handle"; Weight "Net weight:27.5kg Gross Weight:30kg"; "Coolant demand per machine: About 1L"; power cable custom ≥16A; Ethernet
- Shop 7344.00W = 408T × 18 J/T exactly
- Storefront (As-Of 2026-10-11): $3,672 unit price / $9 per TH retail, $28/T partner channel (HK & USA)

## Gaps / notes (from the capture)

- No noise figure anywhere; no attachment/manual section on the shop page. The official file index lists WhatsMinerM63S.pdf (id 29, coolingId 13, created 2025-04-21) — not downloaded this pass (recorded as the known gap for this SKU).
- No rated-flow/pressure figures on the shop page — the M63 family's manual values (≥10 L/min, ≤400 KPa, pH 7–8.7, inlet 25–55 ℃ normal / 25–45 ℃ high-performance) are documented on the M63 page and should not be assumed identical for the M63S until its own manual is captured.

## Cross-check (AMV + MiningNow, 2026-10-10)

- AMV: "M63S (390 Th)", release Nov 2023, 390 Th/s, 7215 W ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md))
- MiningNow: "M63s (406TH/s)", 7308 W, 18 j/Th, best price $2,840.32, hydro, Oct 2023 ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md))
- Banner 408T vs AMV 390 vs MiningNow 406 — successive ratings of the same 18 J/T platform; wall-power rows (7344 / 7215 / 7308 W) are each hashrate × 18 within rounding.

## Heat-reuse notes

- Hydro: 7344.00W banner wall draw per unit, "About 1L" coolant per machine
- Same 86 mm-wide hydro chassis as M63/M63S+/M63S++; rack-density planning is per-position, not per-volume

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M63](whatsminer-m63.md)
- [Whatsminer M63S+](whatsminer-m63s-plus.md)
- [Hydronic heat reuse](hydronic-heat-reuse.md)
