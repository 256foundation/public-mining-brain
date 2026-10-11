# Antminer U3S21EXPH

> Sources: Bitmain product API spec table (captured 2026-10-11); ASIC Miner Value snapshot (2026-10-10)
> Raw: [Bitmain spec table](../../raw/hardware/bitmain/2026-10-11-bitmain-site-u3s21exph.md); [Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md); [AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

Bitmain's 3U rack-form hydro unit — an 860 T multi-machine bundle in the S21 XP class, sold alongside the ANTSPACE HW7 container ecosystem (242× S23e U2H slots per its catalog row). The name encodes the form factor: **U3** (3U) **S21** class **EXPH** ([Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md)).

## Specs (manufacturer, As-Of 2026-10-11)

From the API spec table, numbers verbatim ([Bitmain spec table](../../raw/hardware/bitmain/2026-10-11-bitmain-site-u3s21exph.md)):

- Model row: "U3S21EXPH", Sub 860T, Version 10; SHA256|BTC/BCH/BSV
- Typical hashrate, TH/s(1-1): 860
- Power on wall @35℃(1-2), Watt(1-1): 11,180 (sheet renders with thousands separator "11,180"; catalog row: 11180W)
- Power efficiency on wall @35℃(1-2), J/T(1-1): 13.0
- Sheet note (verbatim): typical values; actual hashrate ±3%, power on wall and efficiency ±5%; "(1-2) Inlet coolant temperature"
- Power: 3-phase, 380~415 V, 50~60 Hz, input max current **24 A**, power port "LP34"
- Server size 900*482.6*130 mm w/o package (1,150*640*260 boxed) — 19-inch rack 3U form factor; net 42.7 kg, gross 48.6 kg
- Environment: inlet coolant 20~50 ℃; coolant flow **16.0~20.0 L/min** (double a single-unit hydro's 8.0~10.0); pressure ≤3.5 bar; pipe connector **OD14** (vs OD10 on 1U-class hydro units)
- Storage -20~70 ℃; operation humidity (non-condensing) 10~90% RH; network RJ45 Ethernet 10/100M
- Storefront (As-Of 2026-10-11): 7740 USD (pricePerunit 9 USD/T — multi-unit bundle pricing), product status 2 (on sale)

## Cross-check (AMV, 2026-10-10)

- AMV lists the same hardware under a different name: "S21e XP Hyd 3U (860 Th)", release Jan 2025, 860 Th/s, 11180 W — plus a priced storefront row at "$8,482 $10 / Th" ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md))
- Hashrate/power agree across both: 860 Th/s / 11180 W; AMV's 13j/Th matches the sheet's 13.0 (J/T row).
- Naming divergence is real, not an error: Bitmain's SKU is U3S21EXPH; AMV's row name is "S21e XP Hyd 3U". Cross-references between the two databases should expect either label.

## Heat-reuse notes

- 11,180 W wall draw per 3U slot at 16.0~20.0 L/min — the highest single-body thermal density in the S21 hydro family; the OD14 pipe connector (vs OD10 on 1U hydro units) carries the flow
- Designed for ANTSPACE HW7 / rack integration per the catalog notes — heat capture is container-level (dry-cooling tower / liquid-cooling container), not per-unit fan
- Coolant guidance ties to the "ANTSPACE HW7 Liquid cooling container & Dry-cooling Tower product manual" (sheet note 3-2)

## See Also

- [Bitmain ASIC reference](bitmain-asic-reference.md)
- [Antminer S23e U2H](antminer-s23e-u2h.md)
- [Antminer S21e XP Hyd](antminer-s21e-xp-hyd.md)
- [Antminer S21 XP Hyd](antminer-s21-xp-hyd.md)
