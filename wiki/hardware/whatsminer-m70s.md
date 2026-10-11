# Whatsminer M70S

> Sources: shop.whatsminer.com catalog + detail page (SSR, verbatim); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [MiningNow MicroBT rows](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md); [AMV/MN cross-check report](../../raw/hardware/asicminervalue/_REPORT.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

The shop's air-cooled efficiency flagship (13.5J/TH card) and the top rung of the retail shipping ladder — see [Whatsminer overview](whatsminer-overview.md). No official manual PDF captured for this SKU; the shop card and detail page are the maker-side record.

## Specs (manufacturer sheet, As-Of 2026-10-10)

Shop listing, verbatim:

| Item | Value |
|---|---|
| Card | 248TH, 13.5J/TH, $13.0/T (HK warehouse) |
| Power on wall (detail page) | "No data" — the capture notes 13.5J/TH ⇒ ~3,348 W implied from the card, not stated on the page |
| Cooling class | air (official spec-file list, coolingId 12) |
| pid/skuId | 79/190 |

The M70S sits in the air-cooling group of MicroBT's official file list alongside M70, M70S+, M60S++ and the M50/M60 tiers. Gap note: like the M7x manual sheets, the retail page leaves the performance numbers image-only or empty — here the wall-power field is simply "No data".

## Cross-check disputes (AMV vs MiningNow, 2026-10-10)

> **Status: Disputed** — M70S hashrate and efficiency: shop card says 248TH @ 13.5J/TH, AMV says 226 Th/s @ 3140 W, MiningNow says 226TH/s @ 3140 W (13.89 j/Th). Note the $0.10-vs-$0.07/kWh profitability caveat — gross income agrees ~1% where specs agree.

| Field | Shop (maker) | ASIC Miner Value | Mining Now |
|---|---|---|---|
| Hashrate | 248TH | 226 Th/s | 226TH/s |
| Efficiency | 13.5J/TH | not listed | 13.89 j/Th |
| Wall power | "No data" (~3,348 W implied) | 3140 W | 3140 W |
| Release | — | Dec 2025 | Dec 2025 (ann + first batch) |
| Cooling | air (file list) | (no cooling column) | air |

- The two DBs agree with each other exactly (226 TH/s-class @ 3140 W, Dec 2025); the spread is maker card vs DB rows. The shop's 248TH card lands between AMV's M70S (226 Th/s) and M70S+ (244 Th/s) rows — both DBs list the M70S+ at 244 with the same 3140 W (AMV) and 12.87 j/Th (MiningNow), so the shop card may describe a higher bin than the DBs' M70S entry.
- Economics as served 2026-10-10: AMV cell −$7.54 /day at its $0.10/kWh standard; MiningNow best price $2,799.00, income 8.87/day, profit 3.59/day at $0.07/kWh.

## Heat-reuse notes

- Air-cooled 3140 W-class box: ducting/containment practice and fan-side heat pickup in [Air-Cooled Hashrate Heating](air-cooled-hashrate-heating.md).
- The missing wall-power figure on the maker page is the same capture-gap pattern as the image-only M7x manual PERFORMANCE charts — for heating sizing, the ~3,348 W card-implied figure is the only maker-side number on file (see [Whatsminer overview](whatsminer-overview.md), spec-sheet gaps).

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M73](whatsminer-m73.md) — the hydro flagship above it on the shop ladder
- [Air-Cooled Hashrate Heating](air-cooled-hashrate-heating.md)
