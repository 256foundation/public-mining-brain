# Antminer S23 XP Hyd

> Sources: Bitmain product page/API spec table (captured 2026-10-10); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [Bitmain spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s23-xp-hyd.md); [Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md); [AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md); [MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

Bitmain's current efficiency flagship (8.9 J/T on wall, the top of the live-catalog ladder) and the first confirmed retail unit of the S23 generation. Captured from the shop's product JSON API, which backs the JS-shell product page ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s23-xp-hyd.md)).

## Specs (manufacturer, As-Of 2026-10-10)

From the API spec table, numbers verbatim ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s23-xp-hyd.md)):

- Model row: "S23 XP Hyd.", Version 600T-10; SHA256 / BTC/BCH/BSV
- Typical hashrate: 600 TH/s
- Power on wall @35℃(1-2), Watt(1-1): 5340 W
- Power efficiency on wall @35℃(1-2), J/T(1-1): 8.9 J/T
- Sheet note (verbatim): "hashrate/power/efficiency are typical values; actual hashrate fluctuates ±3%, actual power and efficiency ±5%" — and "(1-2) Inlet coolant temperature", i.e. the wall-efficiency band is hydro @35℃
- Input: 3-phase 380~415 V, 50~60 Hz, max 12 A; RJ45 Ethernet 10/100M
- Server size 409*176*208 mm w/o package; net 15.8 kg
- Hydro loop: inlet coolant temperature 20~50 ℃, coolant flow 8.0~10.0 L/min, coolant pressure ≤3.5 bar, OD10 pipe connector; working coolant antifreeze/pure water/deionized water (pH 7.0~9.0 / 6.5~7.5 / 8.5~9.5 per type); storage temperature -40~90; operation humidity (non-condensing) 10~90% RH
- Coolant maintenance per "ANTSPACE HW7 Liquid cooling container & Dry-cooling Tower product manual", Chapter 9, Article 3, Point 6
- Storefront: 15300 USD (pricePerunit 25.5 USD/T), product status 1 (pre-sale; presellFlag=1), "Shipping from November 2026"; 365-day warranty from shipping date, original purchaser only
- Performance curves (hashrate and efficiency vs inlet coolant temperature) are embedded images only — recorded as image-only gap

## Cross-check (AMV vs MiningNow, 2026-10-10)

- AMV: "Bitmain Antminer S23 XP Hyd (600 Th)", release Oct 2026, 600 Th/s, 5340 W; manufacturer-page profit -$12.82/day; homepage row adds 8.9j/Th, best price $16,399 ($27 / Th), profit $10.92/day ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md))
- MiningNow: "Bitmain Antminer S23 XP Hyd (600TH/s)", 5340 W, 8.9 j/Th, best price $14,999.00, income 23.54/day, profit 14.57/day (@ $0.07/kWh), announced Aug 2026, first batch Nov 2026, hydro ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md))
- Hashrate/power/efficiency agree across all three sources: 600 / 5340 W / 8.9 J/T.

> **Status: Disputed** (price and $/day)
> Maker storefront: 15300 USD MSRP, pre-sale, "Shipping from November 2026" ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s23-xp-hyd.md)). AMV homepage best price $16,399; MiningNow best price $14,999.00 — neither DB states the provenance of its price cell. Release dates also differ: AMV says Oct 2026, MiningNow announced Aug 2026 / first batch Nov 2026, the maker sheet says shipping from November 2026. On $/day: AMV computes profit at its $0.10/kWh site rate, MiningNow at $0.07/kWh (user-editable), so the two $/day figures are not comparable; gross income (profit + power × 24 h × rate) agrees within about 1% here (23.54/day MiningNow vs AMV's $10.92/day plus implied electricity).

## Heat-reuse notes

- Hydro-cooled (shop cooling flag 2): rated heat output equals the 5340 W wall draw; the capture lists no coolant outlet temperature (the curve section that would carry it is image-only)
- Loop the sheet specifies: 8.0~10.0 L/min at ≤3.5 bar, inlet coolant 20~50 ℃, OD10 pipe connector, antifreeze/pure water/deionized water with per-type pH bands
- Wall-efficiency band is hydro @35℃ inlet — not comparable with air-cooled units rated @25℃
- 3-phase 380~415 V, 12 A max: not a single-phase residential unit as captured

## See Also

- [Bitmain ASIC reference](bitmain-asic-reference.md)
- [Antminer S23e U2H](antminer-s23e-u2h.md)
- [Antminer S21 XP+ Hyd](antminer-s21-xp-plus-hyd.md)
- [Antminer S21 XP Hyd](antminer-s21-xp-hyd.md)
- [Antminer S21 XP](antminer-s21-xp.md)
