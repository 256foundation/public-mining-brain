# Antminer S21 XP Imm

> Sources: Bitmain product API spec table (captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [Bitmain spec table](../../raw/hardware/bitmain/2026-10-11-bitmain-site-s21-xp-imm.md); [Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md); [AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md); [MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The immersion (oil) variant of the S21 XP class — a dual-working-mode unit whose sheet carries **two** spec columns: NEM (Normal Energy Mode) and HEM (High Energy Mode). The catalog lists it at the same 13.5 J/T rung as the air-cooled S21 XP ([Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md)).

## Specs (manufacturer, As-Of 2026-10-11)

From the API spec table, numbers verbatim ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-11-bitmain-site-s21-xp-imm.md)):

- Model row: "S21 XP Imm.", Version 300T-10; SHA256 | BTC/BCH/BSV; Working mode(1-1): "NEM | HEM"
- Typical hashrate, TH/s(1-2): 300 | 380 (NEM | HEM)
- Power on wall @30℃(1-3), Watt(1-2): 4050 | 5700
- Power efficiency on wall @30℃, J/TH(1-2): 13.5 | 15.0
- Sheet notes (verbatim): "(1-1) NEM: Normal Energy Mode; HEM: High Energy Mode"; typical values, hashrate ±3%, power/efficiency ±5%; "(1-3) Inlet oil temperature" — the immersion wall band is measured against **oil** at @30℃, a third convention beside air @25℃ and hydro @35℃
- Power: 3-phase, 380~415 V input range, 50~60 Hz, input max current 12 A
- Server size 364(2-2)*236*293 mm w/o package — "(2-2) The height includes a 44mm handle"; boxed 600*390*450; net 16.8 kg, gross 18.5 kg
- Environment: inlet oil temperature 20~50 ℃; oil flow **1 m3/h** (volumetric, vs L/min on hydro sheets); storage -20~70 ℃
- Network RJ45 Ethernet 10/100M; no humidity/altitude rows on this sheet (unlike the hydro units)
- Storefront (As-Of 2026-10-11): 2400 USD (pricePerunit 8 USD/T), product status 2 (on sale)

## Cross-check (AMV + MiningNow, 2026-10-10)

- AMV: "S21 XP Imm. (300 Th)", release Sep 2024, 300 Th/s, 4050 W ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md))
- MiningNow: "S21 XP Immersion (300TH/s)", 4050 W, 13.5 j/Th, best price $3,056.00, immersion, announced Jun 2024 ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md))
- Both databases list only the **NEM** column values (300 Th / 4050 W / 13.5); the sheet's HEM column (380 T / 5700 / 15.0) appears in neither DB — cited here from the manufacturer sheet alone.

## Heat-reuse notes

- Oil-immersed: 4050 W (NEM) rising to 5700 (HEM) into 1 m³/h oil flow — the HEM mode is the heat-reuse-relevant ceiling
- Inlet oil band 20~50 ℃ is narrower/cooler than the S21 Imm.'s 30~55 ℃ — oil-class units are not interchangeable in a shared loop without checking both bands
- No fan/noise/airflow rows exist (immersion): thermal output is fully liquid-side, 1 m³/h oil flow

## See Also

- [Bitmain ASIC reference](bitmain-asic-reference.md)
- [Antminer S21 Imm](antminer-s21-imm.md)
- [Antminer S21 XP](antminer-s21-xp.md)
- [Immersion heat reuse](immersion-heat-reuse.md)
