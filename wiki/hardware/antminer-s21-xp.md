# Antminer S21 XP

> Sources: Bitmain product page/API spec table (captured 2026-10-10); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [Bitmain spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s21-xp.md); [Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md); [AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md); [MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

The current air-cooled S21-series flagship in Bitmain's live catalog — the top of the air track while hydro takes the efficiency ladder above it. Captured from the shop's product JSON API ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s21-xp.md)).

## Specs (manufacturer, As-Of 2026-10-10)

From the API spec table, numbers verbatim ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s21-xp.md)):

- Model row: "S21 XP", Sub 270, Version 10; SHA256 / BTC/BCH/BSV
- Typical hashrate: 270 TH/s
- Power on wall @25℃(1-2), Watt(1-1): 3645 W
- "Power efficiency on wall @25℃(1-2), J/TH(1-1)": 13.5 J/T (sheet row unit rendered J/TH; catalog row: 13.5J/T)
- Sheet note (verbatim): typical values; actual hashrate ±3%, power and efficiency ±5%; "(1-2) Inlet air temperature" — air wall band @25℃, not the hydro @35℃ band
- Input: single-phase 220~277 V, 50~60 Hz, 20 A ("Single-phase AC input 20A")
- Server size 450*219*293 mm w/o package; net 18.7 kg
- Noise(2-3) @30℃: 76 dBA (fan at max RPM); max airflow(2-4) 550 CFM (airflow reduces in dusty/poorly ventilated conditions)
- Operation temperature -20~45 ℃; storage -20~70; operation humidity (no condensation) 10%~90% RH; operation altitude(2-5) ≤2000 m (above 900 m, max operating temperature drops 1℃ per 300 m)
- Storefront: 4590 USD (pricePerunit 17.0 USD/T), product status 2 (on sale), "Shipping in 7 working days after fully paid"
- Source-table typo preserved in the raw for fidelity: "Hardware Ronfiguration"

## Cross-check (AMV vs MiningNow, 2026-10-10)

- AMV: "Bitmain Antminer S21 XP (270 Th)", release Sep 2024, 270 Th/s, 3645 W; manufacturer-page profit -$8.75/day. S21 XP does not appear in the AMV homepage top-20 cross-reference captured the same day ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md))
- MiningNow: "Bitmain Antminer S21 XP (270TH/s)", 3645 W, 13.5 j/Th, best price $2,799.00, income 10.59/day, profit 4.47/day (@ $0.07/kWh), announced Jun 2024, first batch Oct 2024, air ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md))
- Hashrate/power/efficiency agree across all three sources: 270 / 3645 W / 13.5 J/T.

> **Status: Disputed** (price)
> Maker storefront: 4590 USD MSRP ("Shipping in 7 working days after fully paid") vs MiningNow best price $2,799.00 — AMV shows no price for this model on the captured pages (manufacturer-page profit cells on that page type carry electricity cost only, with coin revenue absent as served). $/day caveat: AMV's site rate is $0.10/kWh, MiningNow's $0.07/kWh, so $/day cells are not comparable across the two DBs.

## Heat-reuse notes

- Air-cooled: 3645 W wall draw, 76 dBA at max fan (measured @30℃), 550 CFM max airflow — the fan/noise/airflow rows exist only on this air-cooled sheet; the hydro captures carry coolant rows instead
- Wall-efficiency band is @25℃ inlet air (sheet note), the convention difference to keep in mind when lining this unit up against the @35℃ hydro ratings
- Single-phase 220~277 V at 20 A — unlike the 3-phase 380~415 V hydro units; derating note verbatim from the sheet: above 900 m altitude, max operating temperature drops 1℃ per 300 m

## See Also

- [Bitmain ASIC reference](bitmain-asic-reference.md)
- [Antminer S23 XP Hyd](antminer-s23-xp-hyd.md)
- [Antminer S23e U2H](antminer-s23e-u2h.md)
- [Antminer S21 XP+ Hyd](antminer-s21-xp-plus-hyd.md)
- [Antminer S21 XP Hyd](antminer-s21-xp-hyd.md)
