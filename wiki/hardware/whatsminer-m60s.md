# Whatsminer M60S

> Sources: shop.whatsminer.com detail page + official manual (captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [M60S shop page + manual](../../raw/hardware/microbt/2026-10-11-microbt-site-m60s.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The 18.5 J/TH air-cooled rung between the M60 (19.9) and M60S+ (17) — three banner hashrate options (188T/186T/184T) all sharing one efficiency rating ([MicroBT catalog](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md)).

## Specs (manufacturer, As-Of 2026-10-11)

Shop banner, verbatim ([M60S shop page](../../raw/hardware/microbt/2026-10-11-microbt-site-m60s.md)):

- Hashrate (banner select, three options): 188T / 186T / 184T — each option carries Power efficiency 18.5J/TH
- Power on wall: 3478.00W; listing type SPOT, warehouses HK/USA
- Specification tab: Working Temperature -5°C~35°C; Size 430mm*155mm*226mm; Weight "13.5KG"; Ethernet; IEC C19 ≥16A; PSU "P221B/P222B AC220V ~ 240V"

Official manual (English, October 2024, attached to the page), verbatim:

- Power Ratio: 18.5 J/T ± 5 % @ 25 °C
- Hashrate: 170 T –186 T ± 5 %
- Power On Wall: 3145 W –3441 W ± 10 %
- Air Flow: 350 CFM; Weight 11.5 kg (Net) / 12.6 kg (Gross); Size 430 × 155 × 226 mm
- Input Voltage: AC 220 V –240 V; Working Temperature -5 °C –+35 °C; "Prototype data for reference only."
- Shop-vs-manual notes preserved: banner top 188T sits above the manual range top (186 T) but within ±5%; shop 3478.00W slightly above the manual band max 3441 W yet within its ±10% envelope; shop "13.5KG" vs manual 11.5/12.6 kg — both carried verbatim
- Storefront (As-Of 2026-10-11): $1,692 unit price / $9 per TH (HK & USA)

## Cross-check (catalog + DBs)

- Catalog card: "MICROBT WhatsMiner M60S | 184~188TH | 18.5J/TH | $9.0 | HK" ([MicroBT catalog](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md)) — matches the three-option banner.
- No M60S row in the 2026-10-10 AMV/MiningNow MicroBT snapshots — shop page + manual are the sources on record.

## Heat-reuse notes

- Air-cooled: 3145–3441 W wall band, 350 CFM — same chassis and airflow class as the whole 430×155×226 mm M6x air family
- The 188T banner option is the heat-output ceiling variant; all three options share the 18.5 J/T rating, so per-TH heat is constant and per-unit heat scales with the selected hashrate option

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M60](whatsminer-m60.md)
- [Whatsminer M60S+](whatsminer-m60s-plus.md)
- [Air-cooled hashrate heating](air-cooled-hashrate-heating.md)
