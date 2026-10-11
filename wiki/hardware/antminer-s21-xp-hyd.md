# Antminer S21 XP Hyd

> Sources: Bitmain product page/API spec table (captured 2026-10-10); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [Bitmain spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s21-xp-hyd.md); [Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md); [AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md); [MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

The hydro counterpart of the S21 XP line, still on sale in Bitmain's live 2026-10 catalog and in the shop's home "Hot Products" carousel. Captured from the shop's product JSON API ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s21-xp-hyd.md)).

## Specs (manufacturer, As-Of 2026-10-10)

From the API spec table, numbers verbatim ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s21-xp-hyd.md)):

- Model row: "S21 XP Hyd."; SHA256 / BTC/BCH/BSV
- Typical hashrate: 473 TH/s
- Power on wall @35℃(2-2), Watt(2-1): 5676 W
- Power efficiency on wall @35℃(2-2), J/T(2-1): 12 J/T
- Sheet note (verbatim): typical values; actual hashrate ±3%, actual power and efficiency ±5%; "(2-2) Inlet coolant temperature" — hydro wall band @35℃
- Input: 3-phase 380~415 V, 50~60 Hz, max 12 A; RJ45 Ethernet 10/100M
- Server size 339*173*207 mm w/o package; net 13.8 kg
- Hydro loop: inlet coolant temperature 20~50 ℃, coolant flow 8.0~10.0 L/min, coolant pressure ≤3.5 bar, OD10 pipe connector; working coolant antifreeze/pure water/deionized water (pH 7.0~9.0 / 6.5~7.5 / 8.5~9.5 per type); storage temperature -20~70; operation humidity (non-condensing) 10~90% RH
- Storefront: 8041 USD (pricePerunit 17.0 USD/T), product status 2 (on sale), "Shipping from Q4 2026"
- Capture note: the "Version" row is absent from this unit's table (present on the S23 XP Hyd. and S21 XP+ Hyd. tables)

## Cross-check (AMV vs MiningNow, 2026-10-10)

- AMV: "Bitmain Antminer S21 XP Hyd (473 Th)", release Nov 2024, 473 Th/s, 5676 W; manufacturer-page profit -$13.62/day; homepage row adds 12j/Th, best price $6,629 ($14 / Th), profit $5.09/day ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md))
- MiningNow: "Bitmain Antminer S21 XP Hyd (473TH/s)", 5676 W, 12 j/Th, best price $1,413.00, income 18.56/day, profit 9.02/day (@ $0.07/kWh), announced Jun 2024, first batch Oct 2024, hydro ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md))
- Hashrate/power/efficiency agree across all three sources: 473 / 5676 W / 12 J/T.

> **Status: Disputed** (price)
> Specs line up everywhere, but prices do not: 8041 USD maker MSRP (on sale, "Shipping from Q4 2026") vs $6,629 AMV best price vs $1,413.00 MiningNow best price — neither DB documents where its price cell comes from, so the spread is recorded, not resolved. $/day caveat: AMV computes profit at $0.10/kWh, MiningNow at $0.07/kWh, so the $/day cells are not comparable; gross income (profit + power × 24 h × rate) agrees within about 1% (18.56/day MiningNow vs AMV's $5.09/day plus implied electricity).

## Heat-reuse notes

- Hydro-cooled (shop cooling flag 2): wall rating 5676 W on the @35℃ inlet basis; capture lists no coolant outlet temperature
- Loop requirements from the sheet: flow 8.0~10.0 L/min at ≤3.5 bar, inlet coolant 20~50 ℃, OD10 pipe connector, antifreeze/pure water/deionized water with per-type pH bands — same coolant envelope as the S23 XP Hyd. and S21 XP+ Hyd. captures
- Smaller chassis than the XP+ (339*173*207 mm vs 430*176*208 mm) at similar wall draw; 3-phase 380~415 V, 12 A max

## See Also

- [Bitmain ASIC reference](bitmain-asic-reference.md)
- [Antminer S23 XP Hyd](antminer-s23-xp-hyd.md)
- [Antminer S23e U2H](antminer-s23e-u2h.md)
- [Antminer S21 XP+ Hyd](antminer-s21-xp-plus-hyd.md)
- [Antminer S21 XP](antminer-s21-xp.md)
