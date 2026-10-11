# Whatsminer M63

> Sources: shop.whatsminer.com detail page + official manual (captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [M63 shop page + manual](../../raw/hardware/microbt/2026-10-11-microbt-site-m63.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [MiningNow MicroBT rows](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The 19.9 J/TH hydro rung — 372 T banner rating on the 70°C-outlet hydro generation, the value tier of the hydro-cooled M6x family (coolingId 13).

## Specs (manufacturer, As-Of 2026-10-11)

Shop banner + tab, verbatim ([M63 shop page](../../raw/hardware/microbt/2026-10-11-microbt-site-m63.md)):

- Hashrate: 372T; Power efficiency: 19.9J/TH; Power on wall: 7402.80W; listing type SPOT, warehouses HK/USA
- Specification tab: PSU "AC380~480V, 3W+ ground, input 10kw"; Size "86mm*483mm*663mm with handle"; Weight "Net weight:27.5kg Gross Weight:30kg"; "Coolant demand per machine: About 1L"; power cable custom ≥16A; Ethernet

Official manual (English, October 2024 — "Hydro-Cooling (Outlet temperature reaches up to 70°C)"), verbatim:

- Power Ratio: 19.9 J/T ± 5 %
- Hashrate: 334 T –366 T ± 10 % (pdftotext bookmark artifact "3 34 T" joined; cross-checked 19.9 J/T × 350 T ≈ 6,965 W against the 10 kW input)
- Weight 27.5 / 30 kg; Size with handle 86 × 482.6 × 663 mm; AC 380 V –480 V, input 10 kW
- Environmental: inlet liquid 25–55 ℃ normal / 25–45 ℃ high-performance mode; control accuracy ±2 ℃; rated flow ≥10 L/min ±10%; pressure ≤400 KPa; medium "Pure water (or distilled water) + special corrosion inhibitor + antifreeze"; pH 7–8.7; storage/transport -40–+70 ℃; working humidity 5–85 %RH non-condensing
- The manual has NO Power On Wall row — only "Input 10 kW"; the banner's 7402.80W is the sole wall-power figure on record (= 372T × 19.9 J/T exactly)
- Shop banner 372T sits above the manual range top (334–366 T); page tag "WhatsMiner M63 360T" vs banner 372T — both preserved
- Storefront (As-Of 2026-10-11): $2,976 unit price / $8 per TH retail, $25/T partner channel (HK & USA)

## Cross-check (AMV + MiningNow, 2026-10-10)

- AMV: "M63 (334 Th)", release Nov 2023, 334 Th/s, 6646 W ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)) — the manual-range bottom (334 T), an earlier revision's rating
- MiningNow: "M63 (360TH/s)", 7200 W, 20 j/Th, best price $1,892.85, hydro, Oct 2023 ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md))
- Hashtate ratings differ across layers (334 manual-low / 360 tag / 372 banner / 360–366 DB rows) — same unit, successive firmware/binnings; the efficiency constant 19.9 J/T ±5% holds across all sources.

## Heat-reuse notes

- Hydro at up to **70 ℃ outlet** (this 70°C generation, vs the M7x 90°C-outlet generation — [M7B spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m7b.md)): inlet 25–55 ℃, ≥10 L/min, ≤400 kPa — outlet grade hot enough for hydronic direct use
- 7402.80W banner wall draw per unit into ~1 L coolant volume per machine — compact hydro form factor (86 mm wide)

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M63S](whatsminer-m63s.md)
- [Whatsminer M63S++](whatsminer-m63s-plus-plus.md)
- [Hydronic heat reuse](hydronic-heat-reuse.md)
