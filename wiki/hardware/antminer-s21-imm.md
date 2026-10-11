# Antminer S21 Imm

> Sources: Bitmain product API spec table (captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [Bitmain spec table](../../raw/hardware/bitmain/2026-10-11-bitmain-site-s21-imm.md); [Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md); [AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md); [MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The entry immersion unit of the live catalog's efficiency ladder — dual-mode NEM/HEM like the S21 XP Imm., but with a warmer 30~55 ℃ inlet-oil band and the ladder's second-highest J/T (16 NEM / 18.5 HEM) ([Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md)).

## Specs (manufacturer, As-Of 2026-10-11)

From the API spec table, numbers verbatim ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-11-bitmain-site-s21-imm.md)):

- Model row: "S21 Imm.", Version 10; SHA256 | BTC/BCH/BSV; Working mode(1-1): "NEM | HEM"
- Typical hashrate, TH/s(1-2): 215 | 301 (NEM | HEM)
- Power on wall @30℃(1-3), Watt(1-2): 3440 | 5569
- Power efficiency on wall @30℃, J/TH(1-2): 16.0 | 18.5
- Sheet notes (verbatim): "(1-1) NEM: Normal Energy Mode; HEM: High Energy Mode"; typical values, hashrate ±3%, power/efficiency ±5%; "(1-3) Inlet oil temperature"
- Power: 3-phase, 380~415 V input range, 50~60 Hz, input max current 12 A
- Server size 293*236*364(2-2) mm w/o package — "(2-2) The height includes a 44mm handle"; boxed 600*390*450; net 17.15 kg, gross 20.45 kg
- Environment: inlet oil temperature **30~55 ℃** (warmer band than S21 XP Imm.'s 20~50 ℃); oil flow 1 m3/h; storage -20~70 ℃
- Network RJ45 Ethernet 10/100M; no humidity/altitude rows on this sheet
- Storefront (As-Of 2026-10-11): 1290 USD (pricePerunit 6 USD/T), product status 2 (on sale)

## Cross-check (AMV + MiningNow, 2026-10-10)

- AMV: "S21 Imm. (301 Th)", release Dec 2024, 301 Th/s, 5569 W ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md))
- MiningNow: "S21 Immersion (301TH/s)", 5569 W, 18.5 j/Th, best price $1,548.00, immersion ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md))
- Both databases list only the **HEM** column (301 Th / 5569 W / 18.5); the sheet's NEM column (215 T / 3440 W / 16.0) is the catalog row's basis — the two naming layers point at different working modes of the same unit.

## Heat-reuse notes

- HEM mode is the heat-relevant number: 5569 W wall draw into 1 m³/h oil; NEM runs 3440 W
- Inlet oil band 30~55 ℃ — the warmest oil band in the S21 immersion pair, which matters for direct heat-export designs (hotter inlet = more usable-grade heat)
- Same no-fan/no-noise-row immersion sheet shape as S21 XP Imm.; all thermal output is liquid-side

## See Also

- [Bitmain ASIC reference](bitmain-asic-reference.md)
- [Antminer S21 XP Imm](antminer-s21-xp-imm.md)
- [Immersion heat reuse](immersion-heat-reuse.md)
- [Antminer S21e Hyd](antminer-s21e-hyd.md)
