# Antminer S21e XP Hyd

> Sources: Bitmain product API spec table (captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [Bitmain spec table](../../raw/hardware/bitmain/2026-10-11-bitmain-site-s21e-xp-hyd.md); [Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md); [AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md); [MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The value tier of the S21 XP hydro family — 430 T at 13 J/T, the "e" (efficiency-economy) variant of the XP Hyd line, sharing the ladder rung with the U3S21EXPH bundle ([Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md)).

## Specs (manufacturer, As-Of 2026-10-11)

From the API spec table, numbers verbatim ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-11-bitmain-site-s21e-xp-hyd.md)):

- Model row: "S21e XP Hyd."; SHA256|BTC/BCH/BSV
- Typical hashrate, TH/s(2-1): 430
- Power on wall @35℃(1-2), Watt(2-1): 5590
- Power efficiency on wall @35℃(2-2), J/T(2-1): 13
- Sheet note (verbatim): typical values; actual hashrate ±3%, power on wall and efficiency ±5%; "(2-2) Inlet coolant temperature"
- Power: 3-phase, 380~415 V, 50~60 Hz, input max current 12 A
- Server size 339*173*207 mm w/o package (570*316*430 boxed); net 13.8 kg, gross 15.7 kg
- Environment: inlet coolant 20~50 ℃; coolant flow 8.0~10.0 L/min; pressure ≤3.5 bar; working coolant Antifreeze/Pure water/Deionized water; pH bands 7.0~9.0 / 6.5~7.5 / 8.5~9.5; pipe connector OD10
- Storage -20~70 ℃; operation humidity (non-condensing) 10~90% RH; network RJ45 Ethernet 10/100M
- Storefront (As-Of 2026-10-11): 3870 USD (pricePerunit 9 USD/T), product status 2 (on sale); listing shipping note "Shipping from Q4 2026"

## Cross-check (AMV + MiningNow, 2026-10-10)

- AMV: "S21e XP Hyd (430 Th)", release Nov 2024, 430 Th/s, 5590 W ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md))
- MiningNow: "S21e XP Hyd (430TH/s)", 5590 W, 13 j/Th, best price $3,580.00, announced Nov 2024, hydro ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md))
- Hashrate/power/efficiency agree across all three sources: 430 / 5590 W / 13 J/T.

> **Status: Disputed** (price)
> Maker storefront 3870 USD vs MiningNow best price $3,580.00 (As-Of dates differ by one day; both snapshot evidence, not wiki claims).

## Heat-reuse notes

- 5590 W wall draw into coolant at 8.0~10.0 L/min, inlet band 20~50 ℃ — standard S21 hydro plumbing (OD10, ≤3.5 bar)
- Lightest unit in the XP hydro family at 13.8 kg net — the per-rack thermal planning number scales accordingly
- Same @35℃ hydro wall convention as the rest of the hydro track; do not line up against the air-cooled @25℃ sheets

## See Also

- [Bitmain ASIC reference](bitmain-asic-reference.md)
- [Antminer S21 XP Hyd](antminer-s21-xp-hyd.md)
- [Antminer U3S21EXPH](antminer-u3s21exph.md)
- [Antminer S21e Hyd](antminer-s21e-hyd.md)
- [Antminer S21j XP Hyd](antminer-s21j-xp-hyd.md)
