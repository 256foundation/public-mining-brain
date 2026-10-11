# Antminer S23e U2H

> Sources: Bitmain product page/API spec table (captured 2026-10-10); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [Bitmain spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s23e-u2h.md); [Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md); [AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md); [MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

Bitmain's 2U rack-form hydro miner (2UH): the hashboard-class unit of the S23 generation, sold both standalone and as the fill of the ANTSPACE HW7 container. Captured from the shop's product JSON API ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s23e-u2h.md)).

## Specs (manufacturer, As-Of 2026-10-10)

From the API spec table, numbers verbatim ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s23e-u2h.md)):

- Model row: "S23e U2H", Version 865T-10; SHA256 / BTC/BCH/BSV
- Typical hashrate: 865 TH/s
- Power on wall @35℃(1-2), Watt(1-1): 8650 W
- Power efficiency on wall @35℃(1-2), J/T(1-1): 10 J/T
- Sheet note (verbatim): hashrate/power/efficiency are typical values; actual hashrate ±3%, actual power and efficiency ±5%; "(1-2) Inlet coolant temperature" — hydro wall band @35℃
- Server size 600*483*86 mm w/o package (2U rack)
- Storefront: 19030 USD (pricePerunit 22.0 USD/T), product status 1 (pre-sale; presellFlag=1), "Shipping from Q4 2026"
- Gap: the shop spec table is short-form — no PSU, coolant, weight or noise rows published in this listing (the catalog "weight" field says 30); other rows may exist only in product images/manual

## Cross-check (AMV vs MiningNow, 2026-10-10)

- AMV: "Bitmain Antminer S23e Hyd 2U (865 Th)", release Apr 2026, 865 Th/s, 8650 W; manufacturer-page profit -$20.76/day; homepage row adds 10j/Th, best price $10,000 ($12 / Th), profit $13.46/day ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md))
- MiningNow: "Bitmain Antminer S23e Hyd 2U (865TH/s)", 8650 W, 10 j/Th, best price $9,519.00, income 33.94/day, profit 19.41/day (@ $0.07/kWh), announced Jan 2026, first batch May 2026, hydro ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md))
- Hashrate/power/efficiency agree across all three sources: 865 / 8650 W / 10 J/T.

> **Status: Disputed** (name, shipping state, price)
> The maker storefront calls it "S23e U2H"; both DBs list it as "S23e Hyd 2U" — same 865 TH/s / 8650 W / 10 J/T numbers under two names. Shipping state conflicts: the maker sheet is pre-sale "Shipping from Q4 2026" (as of the 2026-10-10 capture), MiningNow records first batch May 2026 and AMV a Apr 2026 release. Price: 19030 USD maker MSRP vs $10,000 (AMV) vs $9,519.00 (MiningNow), provenance unstated. $/day caveat: AMV profits use $0.10/kWh, MiningNow $0.07/kWh — gross income (profit + power × 24 h × rate) agrees within about 1% (33.94/day MiningNow vs AMV's $13.46/day plus implied electricity).

## Heat-reuse notes

- 2U rack hydro form factor (600*483*86 mm w/o package): the dense format Bitmain's own container pairs it with — the ANTSPACE HW7 listing is "242 2U-type (S23e U2H) miners or 396 T-type miners" in a 2000 kW, $169,000 package ([Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md))
- Wall rating @35℃ inlet basis, 8650 W per unit; the capture gives per-unit watts and the HW7 container total (2000 kW) only — no per-rack thermal figure is published
- Coolant flow/pressure/temperature rows are absent from the short-form listing — captured gap; treat hydro plumbing figures as unpublished until a fuller spec sheet is captured

## See Also

- [Bitmain ASIC reference](bitmain-asic-reference.md)
- [Antminer S23 XP Hyd](antminer-s23-xp-hyd.md)
- [Antminer S21 XP+ Hyd](antminer-s21-xp-plus-hyd.md)
- [Antminer S21 XP Hyd](antminer-s21-xp-hyd.md)
- [Antminer S21 XP](antminer-s21-xp.md)
