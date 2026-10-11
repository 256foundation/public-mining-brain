# Whatsminer M66S+

> Sources: official MicroBT product manual (PDF, verbatim, Chinese edition); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [MicroBT manual: M66S+](../../raw/hardware/microbt/2026-10-10-microbt-site-m66s-plus.md); [MicroBT shop catalog](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [MiningNow MicroBT rows](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md); [AMV/MN cross-check report](../../raw/hardware/asicminervalue/_REPORT.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

The 17 J/T higher-bin sibling of the [Whatsminer M66S](whatsminer-m66s.md), same immersion chassis. Not retail-listed on the maker shop — captured from the official product-manual PDF (resolved via the whatsminer.com pre-sales API, file id 32), manual dated October 2024.

## Specs (manufacturer sheet, As-Of 2026-10-10)

Verbatim values, labels translated from the Chinese edition (神马 M66S+):

| Item | Value |
|---|---|
| Power ratio | 17 J/T ±5% |
| Hashrate | 280 T ～ 318 T ±10% |
| Cooling class | oil/immersion (油冷); MicroBT file list coolingId 14 |
| Size with handle | 267.5 mm × 147 mm × 401 mm |
| Weight | 18 kg net / 19 kg gross |
| Input | AC380V ～ 480V; power cable custom, ≥16A; Ethernet |
| Liquid temperature | inlet 25 °C ～ 55 °C @ normal mode, 25 °C ～ 45 °C @ high-performance mode; control accuracy ±2 °C; storage/transport -40 °C ～ +70 °C |
| Liquid flow | rated ≥ 24 L/min; control accuracy ±10% |
| Liquid medium | dedicated coolant — insulating liquid (S5X/S3X) |
| Humidity | storage 5%RH ～ 95%RH (non-condensing); long-term 30%RH ～ 69%RH |

Source PDF: [神马 M66S+ manual](https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/%E7%A5%9E%E9%A9%ACM66S%2B_1760947644674.pdf). Gap note from the capture: the manual's PERFORMANCE section is a chart image only ("样机数据仅供参考" — prototype data for reference only); no text-form hashrate-vs-temperature numbers.

## Cross-check disputes (AMV vs MiningNow, 2026-10-10)

> **Status: Disputed** — M66S+ release date: AMV says Aug 2024, MiningNow says Jul 2024 (announced and first batch both Jul 2024); maker manual is dated October 2024. Hashrate and wall power agree across both DBs — note the $0.10-vs-$0.07/kWh profitability caveat — gross income agrees ~1% where specs agree.

| Field | ASIC Miner Value | Mining Now | Maker sheet |
|---|---|---|---|
| Hashrate | 318 Th/s | 318TH/s | 280 T ～ 318 T ±10% |
| Wall power | 5406 W | 5406 W | not stated in text (image-only charts) |
| Efficiency | not listed | 17 j/Th | 17 J/T ±5% |
| Release | Aug 2024 | Jul 2024 | manual October 2024 |

- The DB hashrate equals the maker sheet's top rating (318 T), unlike the M66S case where the two DBs split. The only disputed field is the release month: Aug 2024 (AMV) vs Jul 2024 (MiningNow).
- Economics as served 2026-10-10: AMV cell −$12.97 /day at its $0.10/kWh standard; MiningNow best price $2,769.00, income 12.48/day, profit 3.39/day at $0.07/kWh.

## Heat-reuse notes

- Same immersion loop requirements as the M66S: insulating liquid S5X/S3X, rated flow ≥ 24 L/min, inlet 25 °C ～ 55 °C normal mode. The 17 J/T ratio at up to 318 T makes it the more efficient way to put the same immersion loop to work.
- PERFORMANCE curves are image-only in the manual — no manufacturer text derating data (see [Whatsminer overview](whatsminer-overview.md), spec-sheet gaps).

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M66S](whatsminer-m66s.md) — 18.5 J/T sibling, same 267.5 mm × 147 mm × 401 mm chassis
- [Immersion Heat Reuse](immersion-heat-reuse.md)
