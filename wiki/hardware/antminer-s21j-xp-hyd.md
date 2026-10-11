# Antminer S21j XP Hyd

> Sources: Bitmain product API spec table (captured 2026-10-11); ASIC Miner Value snapshot (2026-10-10)
> Raw: [Bitmain spec table](../../raw/hardware/bitmain/2026-10-11-bitmain-site-s21j-xp-hyd.md); [Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md); [AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The 12 J/T tier of Bitmain's hydro ladder — a 495 T sibling of the S21 XP Hyd at the same 12 J/T efficiency, shipping "from October 2026" at capture ([Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md)).

## Specs (manufacturer, As-Of 2026-10-11)

From the API spec table, numbers verbatim ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-11-bitmain-site-s21j-xp-hyd.md)):

- Model row: "S21j XP Hyd.", Version 495T-10; SHA256 | BTC/BCH/BSV
- Typical hashrate, TH/s(1-1): 495
- Power on wall @35℃(1-2), Watt(1-1): 5940
- Power efficiency on wall @35℃(1-2), J/TH(1-1): 12.0 (sheet unit rendered J/TH; catalog row: 12J/T)
- Sheet note (verbatim): typical values; actual hashrate ±3%, power and efficiency ±5%; "(1-2) Inlet coolant temperature" — hydro wall band @35℃, not the air-cooled @25℃ convention
- Power: 3-phase, 380~415 V, 50~60 Hz, input max current 12 A
- Server size 430*176*208 mm w/o package (570*316*430 boxed); net 16.2 kg, gross 18.3 kg
- Environment: "Inlet coolant temperature, °C" 20~50; coolant flow 8.0~10.0 L/min; pressure ≤3.5 bar; working coolant "Antifreeze/ Pure water/Deionized water"; pH bands Antifreeze 7.0~9.0 / "Prue water" (sic, preserved) 6.5~7.5 / Deionized 8.5~9.5; pipe connector OD10
- Storage -20~70 ℃; operation humidity (non-condensing) 10~90% RH; network RJ45 Ethernet 10/100M
- Storefront (As-Of 2026-10-11): 8415 USD (pricePerunit 17 USD/T), product status 2 (on sale)

## Cross-check (AMV, 2026-10-10)

- AMV: "S21j XP Hyd (495 Th)", release Mar 2026, 495 Th/s, 5940 W, 12j/Th ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md))
- Hashrate/power/efficiency agree across both sources: 495 Th/s / 5940 W / 12 J/T.
- No MiningNow row for this model in the 2026-10-10 snapshot; the AMV site-rate caveat ($0.10/kWh) applies to its profit cells.

## Heat-reuse notes

- Hydro-cooled: 5940 W wall draw lands in coolant at 8.0~10.0 L/min with a 20~50 ℃ inlet band — the @35℃ wall rating, comparable to the S21 XP Hyd / S21 XP+ Hyd hydro convention, not to air-cooled @25℃ sheets
- Coolant pH spec matters for loop chemistry: three bands (antifreeze/pure/deionized), one per coolant type
- Compact hydro form factor (16.2 kg, 430 mm deep) vs the 2U rack S23e U2H — different mounting class at the same efficiency tier

## See Also

- [Bitmain ASIC reference](bitmain-asic-reference.md)
- [Antminer S21 XP Hyd](antminer-s21-xp-hyd.md)
- [Antminer S21 XP+ Hyd](antminer-s21-xp-plus-hyd.md)
- [Antminer S23 XP Hyd](antminer-s23-xp-hyd.md)
