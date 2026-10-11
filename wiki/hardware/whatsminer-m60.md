# Whatsminer M60

> Sources: shop.whatsminer.com detail page + official manual (captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [M60 shop page + manual](../../raw/hardware/microbt/2026-10-11-microbt-site-m60.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The base air-cooled unit of the M6x retail ladder — 160 T at 19.9 J/TH on the shop banner, the value rung of the air-cooling family (coolingId 12) ([MicroBT catalog](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md)).

## Specs (manufacturer, As-Of 2026-10-11)

Shop banner, verbatim ([M60 shop page](../../raw/hardware/microbt/2026-10-11-microbt-site-m60.md)):

- Hashrate: 160T; Power efficiency: 19.9J/TH; Power on wall: 3184.00W; listing type SPOT, warehouses HK/USA
- Specification tab: Working Temperature -5°C~35°C; Size 430mm*155mm*226mm; Weight "13.5KG"; Ethernet; power cable IEC C19 ≥16A; PSU "P221B/P222B AC220V ~ 240V"

Official manual (English, October 2024, attached to the page), verbatim:

- Power Ratio: 19.9 J/T ± 5 % @ 25 °C — the air-cooled wall band @25℃, not hydro @35℃ or immersion @30℃
- Hashrate: 150 T –172 T ± 5 %
- Power On Wall: 2985 W –3422 W ± 10 %
- Air Flow: 350 CFM
- Weight: 11.5 kg (Net), 12.6 kg (Gross); Size 430 mm × 155 mm × 226 mm
- Input Voltage: AC 220 V –240 V (single-phase band, P221B/P222B PSU — not the AC380~480V hydro units)
- Working Temperature: -5 °C –+35 °C; "Prototype data for reference only."
- Shop-vs-manual discrepancies preserved: banner 160T sits inside the manual range; shop "Weight: 13.5KG" vs manual 11.5/12.6 kg; no noise figure anywhere; shop 3184.00W inside the manual band
- Storefront (As-Of 2026-10-11): $1,280 unit price / $8 per TH (HK & USA)

## Cross-check (catalog + DBs)

- The 2026-10-10 shop catalog card lists "MICROBT WhatsMiner M60 | 160TH | 19.9J/TH | $8.0 | HK" ([MicroBT catalog](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md)) — matches the banner.
- No M60 row in the 2026-10-10 AMV/MiningNow MicroBT snapshots (AMV coverage note: "M63/M66 families only" for this tier — [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)) — the shop page + manual are the two independent sources on record.

## Heat-reuse notes

- Air-cooled: 2985–3422 W wall draw (±10%), 350 CFM airflow, -5~+35 ℃ ambient — the classic fan-side heat rejection profile; no liquid loop
- Single-phase 220–240 V input distinguishes the whole M6x air family from the 380–480 V hydro/immersion tracks — electrical planning differs accordingly

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M60S](whatsminer-m60s.md)
- [Whatsminer M63](whatsminer-m63.md)
- [Air-cooled hashrate heating](air-cooled-hashrate-heating.md)
