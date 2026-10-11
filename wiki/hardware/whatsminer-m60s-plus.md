# Whatsminer M60S+

> Sources: shop.whatsminer.com detail page + official spec file (captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [M60S+ shop page + spec file](../../raw/hardware/microbt/2026-10-11-microbt-site-m60s-plus.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The 17 J/TH efficiency rung of the air-cooled M6x family — 200 T banner rating, the best air-side efficiency in the current retail catalog's M60 tier ([MicroBT catalog](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md)).

## Specs (manufacturer, As-Of 2026-10-11)

Shop banner, verbatim ([M60S+ shop page](../../raw/hardware/microbt/2026-10-11-microbt-site-m60s-plus.md)):

- Hashrate: 200T; Power efficiency: 17J/TH; Power on wall: 3400.00W; listing type SPOT, warehouses HK/USA
- Specification tab: Working Temperature -5°C~35°C; Size 430mm*155mm*226mm; Weight "13.5KG"; Ethernet; IEC C19 ≥16A; PSU "P221B/P222B AC220V ~ 240V"

Official spec file (Chinese edition, October 2024, resolved from the official file index — the shop page itself has NO attachment section), verbatim values:

- 功耗比 (Power Ratio): 17J/T ±5%@25°C
- 算力 (Hashrate): 190T～210T ±5%
- 墙上功率 (Power on wall): 3230W～3570W ±10%
- 风量 (Air flow): 350CFM
- 重量 (Weight): 11.5kg net / 12.6kg gross; 尺寸 (Size): 430mm×155mm×226mm
- 工作温度 (Working temperature): -5°C～+35°C; 输入电压: AC220V～240V; "样机数据仅供参考。" (prototype data for reference only)
- Shop 3400.00W falls inside the manual band; shop "13.5KG" vs manual 11.5/12.6 kg discrepancy preserved
- Storefront (As-Of 2026-10-11): $3,200 unit price / $16 per TH (HK & USA)

## Cross-check (catalog + DBs)

- Catalog card: "MICROBT WhatsMiner M60S+ | 200TH | 17J/TH | $16.0 | HK" ([MicroBT catalog](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md)) — matches; note the catalog's $16/T ask is the highest in the shop's M6x tier despite mid-pack efficiency, a spot-market quirk on record as a dated As-Of row.
- No M60S+ row in the 2026-10-10 AMV/MiningNow MicroBT snapshots — shop page + official spec file are the sources on record.

## Heat-reuse notes

- Air-cooled: 3230–3570 W wall band, 350 CFM, -5~+35 ℃ ambient — same air chassis as M60/M60S/M60S++
- 17 J/T at 200 T (shop 3400.00W): the efficiency-focused M60 variant; per-unit heat slightly below the M60S options at the same chassis

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M60S](whatsminer-m60s.md)
- [Whatsminer M60S++](whatsminer-m60s-plus-plus.md)
- [Air-cooled hashrate heating](air-cooled-hashrate-heating.md)
