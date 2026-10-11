# Antminer S21 XP+ Hyd

> Sources: Bitmain product page/API spec table (captured 2026-10-10); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [Bitmain spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s21-xp-plus-hyd.md); [Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md); [AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md); [MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

The S21-generation hydro model that sits directly under the S23 XP Hyd. on Bitmain's live ladder (11 J/T), still on sale as of the 2026-10-10 capture. Captured from the shop's product JSON API ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s21-xp-plus-hyd.md)).

## Specs (manufacturer, As-Of 2026-10-10)

From the API spec table, numbers verbatim ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s21-xp-plus-hyd.md)):

- Model row: "S21 XP+ Hyd.", Version 480T-10; SHA256 / BTC/BCH/BSV
- Typical hashrate: 480 T
- Power on wall @35℃(1-2), Watt(1-1): 5280 W
- Power efficiency on wall @35℃(1-2), J/T(1-1): 11 J/T (spec-table cell: 11.0)
- Sheet note (verbatim): typical values; actual hashrate ±3%, actual power and efficiency ±5%; "(1-2) Inlet coolant temperature" — hydro wall band @35℃
- Input: 3-phase 380~415 V, 50~60 Hz, max 12 A; RJ45 Ethernet 10/100M
- Server size 430*176*208 mm w/o package; net 16.2 kg
- Hydro loop: inlet coolant temperature 20~50 ℃, coolant flow 8.0~10.0 L/min, coolant pressure ≤3.5 bar, OD10 pipe connector; working coolant antifreeze/pure water/deionized water (pH 7.0~9.0 / 6.5~7.5 / 8.5~9.5 per type); storage temperature -20~70; operation humidity (non-condensing) 10~90% RH
- Storefront: 9120 USD (pricePerunit 19.0 USD/T), product status 2 (on sale), "Shipping from October 2026"

## Cross-check (AMV vs MiningNow, 2026-10-10)

- AMV: "Bitmain Antminer S21 XP+ Hyd (500 Th)", release Jul 2025, 500 Th/s, 5500 W; manufacturer-page profit -$13.20/day; homepage row adds 11j/Th, best price $8,799 ($18 / Th), profit $6.58/day ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md))
- MiningNow: "Bitmain Antminer S21 XP+ Hyd (500TH/s)", 5500 W, 11 j/Th, best price $7,556.00, income 19.62/day, profit 10.38/day (@ $0.07/kWh), announced Jan 2025, first batch Mar 2025, hydro ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md))
- Efficiency agrees at 11 across all three sources; hashrate and power do not (Disputed below). The two DBs also disagree with each other on dates (AMV release Jul 2025 vs MiningNow announced Jan 2025 / first batch Mar 2025).

> **Status: Disputed** (hashrate and wall power)
> Maker sheet (live capture, 2026-10-10): Version 480T-10, 480 T typical, 5280 W on wall @35℃ ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s21-xp-plus-hyd.md)). Both DBs carry an older-looking 500 Th/500TH/s at 5500 W (AMV release Jul 2025; MiningNow announced Jan 2025, first batch Mar 2025). Best assessment: the DB rows appear to predate the live 480T-10 version; efficiency lands at 11 in every source either way. Prices: 9120 USD maker MSRP vs $8,799 (AMV) vs $7,556.00 (MiningNow). $/day caveat: AMV uses $0.10/kWh, MiningNow $0.07/kWh — gross income (profit + power × 24 h × rate) agrees within about 1% (19.62/day MiningNow vs AMV's $6.58/day plus implied electricity).

## Heat-reuse notes

- Hydro-cooled (shop cooling flag 2): wall rating 5280 W on the @35℃ inlet basis; capture lists no coolant outlet temperature
- Loop requirements from the sheet: flow 8.0~10.0 L/min at ≤3.5 bar, inlet coolant 20~50 ℃, OD10 pipe connector, antifreeze/pure water/deionized water with per-type pH bands — identical coolant rows to the S23 XP Hyd. and S21 XP Hyd. captures
- 3-phase 380~415 V, 12 A max input

## See Also

- [Bitmain ASIC reference](bitmain-asic-reference.md)
- [Antminer S23 XP Hyd](antminer-s23-xp-hyd.md)
- [Antminer S23e U2H](antminer-s23e-u2h.md)
- [Antminer S21 XP Hyd](antminer-s21-xp-hyd.md)
- [Antminer S21 XP](antminer-s21-xp.md)
