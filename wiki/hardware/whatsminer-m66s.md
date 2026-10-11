# Whatsminer M66S

> Sources: shop.whatsminer.com listing (SSR) + official MicroBT product manual (PDF, verbatim); ASIC Miner Value + MiningNow snapshots (2026-10-10), incl. MiningNow per-model page
> Raw: [MicroBT shop + manual: M66S](../../raw/hardware/microbt/2026-10-10-microbt-site-m66s.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [MiningNow MicroBT rows](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md); [MiningNow M66S model page](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt-whatsminer-m66s-model-page.md); [AMV/MN cross-check report](../../raw/hardware/asicminervalue/_REPORT.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

MicroBT's immersion-cooled workhorse and the top AMV-vs-MiningNow mismatch SKU. Retail-listed on the maker shop; manual dated October 2024.

## Specs (manufacturer sheet, As-Of 2026-10-10)

Official manual (WhatMinerM66S product manual, October 2024 — Immersion Cooling) + shop listing, verbatim:

| Item | Value |
|---|---|
| Power ratio | 18.5 J/T ± 5 % |
| Hashrate | 270 T – 298 T ± 10 % |
| Power on wall (shop page) | 5291.00W |
| Shop card | 286~290TH, 18.5J/TH, $9.0/T (HK warehouse; unit price $2,574) |
| Cooling class | Immersion (manual header; MicroBT file list coolingId 14) |
| Size with handle | 267.5 mm × 147 mm × 401 mm |
| Weight | 16 kg net / 17 kg gross |
| Input | AC 380 V – 480 V; power cable custom made, ≥ 16 A; Ethernet |
| Liquid temperature | inlet 25 °C – 55 °C @ normal mode, 25 °C – 45 °C @ high-performance mode; inlet control accuracy ± 2 °C; storage/transport -40 °C – +70 °C |
| Liquid flow | rated ≥ 24 L/min; control accuracy ± 10 % |
| Liquid medium | insulating liquid (S5X/S3X) |

- Manual PDFs linked from the shop page: English and Chinese editions on MicroBT's S3 bucket (see raw). The manual's PERFORMANCE section is chart images only — no text-form hashrate-vs-temperature values.

## Cross-check disputes (AMV vs MiningNow, 2026-10-10)

> **Status: Disputed** — M66S hashrate and wall power: AMV says 298 Th/s @ 5513 W, MiningNow says 310TH/s @ 5580 W, maker sheet says 270 T – 298 T ± 10 % at 18.5 J/T ± 5 % (shop page 5291.00W; shop card 286~290TH @ 18.5J/TH). Note the $0.10-vs-$0.07/kWh profitability caveat — gross income agrees ~1% where specs agree.

| Field | ASIC Miner Value | Mining Now | Maker sheet / shop |
|---|---|---|---|
| Hashrate | 298 Th/s | 310TH/s | 270 T – 298 T ± 10 % (shop card 286~290TH) |
| Wall power | 5513 W | 5580 W | 5291.00W (shop page) |
| Efficiency | not listed | 18 j/Th | 18.5 J/T ± 5 % |
| Release | Nov 2023 | ann Oct 20, 2023 / first batch Oct 25, 2023 | manual October 2024 |

- AMV's 298 Th/s equals the sheet's top rating; MiningNow's 310TH/s is above the top rating but inside its ±10% band. Each source pair is internally consistent at its own hashrate (AMV's pair at the 18.5 J/T ratio, MiningNow's at its listed 18 j/Th) — the dispute is which bin the M66S SKU is, not the arithmetic.
- MiningNow tags the cooling field `hydro` and its model-page copy reads "With an efficient Liquid cooling system" — MicroBT's own file list puts the M66S under immersion (coolingId 14). Naming dispute, not a spec dispute (see [Whatsminer overview](whatsminer-overview.md), air-vs-hydro section).
- MiningNow per-model page (SSR): gross income $12.48/day, electricity $9.37/day, net $3.11/day at $0.07/kWh — described as "$12.48 worth of BitcoinCash every day", BTC shown at $83,062.25 at render check; site FAQ stamp Oct 11, 2026; ROI 715–3087 days. AMV's manufacturer-page cell is −$13.23 /day at its $0.10/kWh standard (electricity-cost-only negative as served). The gross-income gap here is itself a product of the 298 vs 310 TH/s dispute (cross-check report, signal 5).
- Minor per-model-page drift vs the manual: MiningNow lists weight 18 Kg (manual: 16 kg net) and size 267 x 147 x 401 mm (manual: 267.5 mm × 147 mm × 401 mm with handle).

## Heat-reuse notes

- This is the immersion branch of the M66 family: dedicated loop, insulating liquid S5X/S3X, rated flow ≥ 24 L/min, inlet window 25 °C – 55 °C (25 °C – 45 °C in high-performance mode). Not a domestic-water hydro loop — coolant chemistry and HX isolation rules live in [Immersion Heat Reuse](immersion-heat-reuse.md).
- Because the manual's PERFORMANCE section is image-only, there is no manufacturer text curve for heat-reuse derating; field numbers would have to come from builders.
- For the hydro-heater story on this maker's compact chassis, see [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md).

## See Also

- [Whatsminer overview](whatsminer-overview.md) — shipping ladder, naming conventions, family dispute table
- [Whatsminer M66S+](whatsminer-m66s-plus.md) — 17 j/Th sibling on the same immersion chassis (MN row: 318TH/s @ 5406 W)
- [Whatsminer M64](whatsminer-m64.md) — the compact hydro unit
