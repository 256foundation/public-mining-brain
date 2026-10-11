# Antminer S21e Hyd

> Sources: Bitmain product API spec table (captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [Bitmain spec table](../../raw/hardware/bitmain/2026-10-11-bitmain-site-s21e-hyd.md); [Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md); [AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md); [MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The bottom rung of the live catalog's efficiency ladder — 288 T at 17 J/T, the value-tier hydro unit whose catalog row closes the 8.9 → 17 J/T spread (S23 XP Hyd. → S21e Hyd.) ([Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md)).

## Specs (manufacturer, As-Of 2026-10-11)

From the API spec table, numbers verbatim ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-11-bitmain-site-s21e-hyd.md)):

- Model row: "S21e Hyd."; SHA256 | BTC/BCH/BSV
- Typical hashrate, TH/s(2-1): 288 — the served sheet renders the glance cell with an empty second column ("288 | ")
- Power on wall @35°C(2-2), Watt(2-1): 4896 (same empty-second-column rendering; note this sheet uses the degree sign "°C" where sibling hydro sheets use "℃")
- Power efficiency on wall @35°C(2-2), J/TH(2-1): 17
- Sheet note (verbatim): typical values; actual hashrate ±3%, power on wall and efficiency ±5%
- Power: 3-phase, 380~415 V, 50~60 Hz, maximum input current 12 A
- Server size 339*176*208 mm w/o package (570*316*430 boxed); net 14.3 kg, gross 16.2 kg
- Environment: inlet coolant 20~50 ℃; coolant flow 8.0~10.0 L/min ("Coolant Flow" capitalization as served); pressure ≤3.5 bar; working coolant "Antifreeze/ Pure water/ Deionized water"; pH bands 7.0~9.0 / 6.5~7.5 / 8.5~9.5; pipe connector OD10
- Storage -20~70 ℃; operation humidity (non-condensing) 10~90% RH; network RJ45 Ethernet 10/100M
- Storefront (As-Of 2026-10-11): 1728 USD (pricePerunit 6 USD/T), product status 2 (on sale); "Shipping in 20 working days after fully paid"
- This sheet uniquely carries a **Payment** section: "USDT(TRC20), USDT(ERC20), BTC,ETC and USD are accepted in this batch", 48-hour proof-of-transfer window, and the note that "The price of cryptocurrency mining machines has to be adjusted frequently in accordance with variables like the exchange rate of the cryptocurrency with fiat, the cryptocurrency's network difficulty, or the expected difficulty increase."

## Cross-check (AMV + MiningNow, 2026-10-10)

- AMV carries two revisions: "S21e Hyd (288 Th)" Apr 2025 at 4896 W, and "S21e Hyd (310 Th)" Aug 2025 at 5270 W ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md))
- MiningNow: "S21e Hyd (288TH/s)", 4896 W, 17 j/Th, best price $1,210.00, hydro ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md))
- The live-catalog sheet matches the 288 Th revision (4896 W / 17 J/T); the 310 Th (5270 W) row is a newer hardware revision under the same model name. Efficiency rating (17 J/T) is constant across both.

## Heat-reuse notes

- 4896 W wall draw into coolant at 8.0~10.0 L/min, inlet band 20~50 ℃, OD10 — standard S21 hydro plumbing
- 17 J/T is the least efficient hydro rung on the ladder: per-TH heat output is the highest in the hydro track, which for heat-reuse deployments is a feature (more wall watts captured per terahash purchased)

## See Also

- [Bitmain ASIC reference](bitmain-asic-reference.md)
- [Antminer S21+ Hyd](antminer-s21-plus-hyd.md)
- [Antminer S21e XP Hyd](antminer-s21e-xp-hyd.md)
- [Antminer S23 XP Hyd](antminer-s23-xp-hyd.md)
