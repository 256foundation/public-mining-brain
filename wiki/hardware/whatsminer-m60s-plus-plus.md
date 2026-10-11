# Whatsminer M60S++

> Sources: shop.whatsminer.com detail page + official manual (captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [M60S++ shop page + manual](../../raw/hardware/microbt/2026-10-11-microbt-site-m60s-plus-plus.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The efficiency flagship of the air-cooled M6x retail family — 218 T at 15.5 J/TH, sharing the catalog's best air-cooled rating with the hydro M63S++ ([MicroBT catalog](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md)).

## Specs (manufacturer, As-Of 2026-10-11)

Shop banner, verbatim ([M60S++ shop page](../../raw/hardware/microbt/2026-10-11-microbt-site-m60s-plus-plus.md)):

- Hashrate (banner select, single option): 218T; Power efficiency: 15.5J/TH; Power on wall: 3379.00W; listing type SPOT, warehouses HK/USA
- Specification tab: Working Temperature -5°C~35°C; Size 430mm*155mm*226mm; Weight "13.5KG"; Ethernet; IEC C19 ≥16A; PSU "P221B/P222B AC220V ~ 240V"

Official manual (English, December 2024, attached to the page), verbatim:

- Power Ratio: 15.5 J/T ± 5 % @ 25 °C
- Hashrate: 200 T –226 T ± 5 %
- Power On Wall: 3230 W –3570 W ± 10 %
- Air Flow: 350 CFM; Weight 11.5 kg (Net) / 12.6 kg (Gross); Size 430 × 155 × 226 mm
- Input Voltage: AC 220 V –240 V; Working Temperature -5 °C –+35 °C; "Prototype data for reference only."
- Shop 218T inside the manual range; shop 3379.00W inside the manual band; "13.5KG" vs 11.5/12.6 kg discrepancy preserved; page tag typo "15.5J/H" as served
- Storefront (As-Of 2026-10-11): $2,180 unit price / $10 per TH (HK & USA)

## Cross-check (catalog + DBs)

- Catalog card: "MICROBT WhatsMiner M60S++ | 218TH | 15.5J/TH | $10.0 | HK" ([MicroBT catalog](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md)) — matches the banner.
- No M60S++ row in the 2026-10-10 AMV/MiningNow MicroBT snapshots — shop page + manual are the sources on record.

## Heat-reuse notes

- Air-cooled: 3230–3570 W wall band, 350 CFM — the highest heat-per-rack-position among air units at equal chassis, since 218 T concentrates the 3230 W –3570 W band in the same 430×155×226 mm box
- Single-phase 220–240 V; same electrical planning note as the rest of the air family

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M60S+](whatsminer-m60s-plus.md)
- [Whatsminer M63S++](whatsminer-m63s-plus-plus.md)
- [Air-cooled hashrate heating](air-cooled-hashrate-heating.md)
