# Antminer S21+ Hyd

> Sources: Bitmain product API spec table (captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [Bitmain spec table](../../raw/hardware/bitmain/2026-10-11-bitmain-site-s21-plus-hyd.md); [Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md); [AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md); [MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The mid-ladder hydro unit — 358 T at 15 J/T, one rung below the S21e XP Hyd's 13 J/T and two above the S21 Imm.'s 16 J/T in the live catalog's efficiency ladder ([Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md)).

## Specs (manufacturer, As-Of 2026-10-11)

From the API spec table, numbers verbatim ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-11-bitmain-site-s21-plus-hyd.md)):

- Model row: "S21+ Hyd."; SHA256|BTC/BCH/BSV
- Typical hashrate, TH/s(2-1): 358
- Power on wall @35℃(1-2), Watt(2-1): 5370
- Power efficiency on wall @35℃(2-2), J/T(2-1): 15
- Sheet note (verbatim): typical values; actual hashrate ±3%, power on wall and efficiency ±5%; "(2-2) Inlet coolant temperature"
- Power: 3-phase, 380~415 V, 50~60 Hz, input max current 12 A
- Server size 339*173*207 mm w/o package (570*316*430 boxed); net 14.5 kg, gross 16.4 kg
- Environment: inlet coolant 20~50 ℃; coolant flow 8.0~10.0 L/min; pressure ≤3.5 bar; working coolant Antifreeze/Pure water/Deionized water; pH bands 7.0~9.0 / 6.5~7.5 / 8.5~9.5; pipe connector OD10
- Storage -20~70 ℃; operation humidity (non-condensing) 10~90% RH; network RJ45 Ethernet 10/100M
- Storefront (As-Of 2026-10-11): 2864 USD (pricePerunit 8 USD/T), product status 2 (on sale)

## Cross-check (AMV + MiningNow, 2026-10-10)

- AMV carries **two** S21+ Hyd revisions: "S21+ Hyd (319 Th)" Feb 2025 at 4785 W, and "S21+ Hyd (358 Th)" Aug 2025 at 5370 W ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md))
- MiningNow carries three: 319TH/s (4785 W), 358TH/s (5370 W), and a 395TH/s / 5925 W variant at 15 j/Th ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md))
- The live-catalog sheet matches the newest revision: 358 Th / 5370 W / 15 J/T. The 319 Th (4785 W) and 395 Th (5925 W) rows are earlier/other hardware revisions of the same model name — do not average them; the efficiency rating (15 J/T) is constant across all three.

## Heat-reuse notes

- 5370 W wall draw into coolant at 8.0~10.0 L/min, inlet band 20~50 ℃, OD10 connector — the standard S21 hydro plumbing shared with S21e XP Hyd / S21 XP Hyd
- At 15 J/T this rung converts ~15% more wall power per TH than the XP hydro tier — a heat-reuse-relevant inefficiency only if compared per-TH; per-unit thermal output (5370 W) is mid-pack

## See Also

- [Bitmain ASIC reference](bitmain-asic-reference.md)
- [Antminer S21e XP Hyd](antminer-s21e-xp-hyd.md)
- [Antminer S21 XP Hyd](antminer-s21-xp-hyd.md)
- [Antminer S21e Hyd](antminer-s21e-hyd.md)
