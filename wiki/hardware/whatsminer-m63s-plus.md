# Whatsminer M63S+

> Sources: official MicroBT product manual (PDF, verbatim, Chinese edition); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [MicroBT manual: M63S+](../../raw/hardware/microbt/2026-10-10-microbt-site-m63s-plus.md); [MicroBT shop catalog](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [MiningNow MicroBT rows](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md); [AMV/MN cross-check report](../../raw/hardware/asicminervalue/_REPORT.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

Big-box 2U-rack hydro unit (86mm × 482.6mm × 663mm) and one of the largest AMV-vs-MiningNow mismatches in the MicroBT family. Not retail-listed on the maker shop — captured from the official product-manual PDF (pre-sales API file id 28, hydro), manual dated October 2024.

## Specs (manufacturer sheet, As-Of 2026-10-10)

Verbatim values, labels translated from the Chinese edition (神马 M63S+):

| Item | Value |
|---|---|
| Power ratio | 17J/T ±5% |
| Hashrate | 390T ～ 450T ±10% |
| Cooling class | hydro (水冷), outlet water temperature up to 70 °C |
| Size with handle | 86mm × 482.6mm × 663mm |
| Weight | 29.5kg net / 32kg gross |
| Input | AC380V ～ 480V, 输入 10kW (input 10kW); power cable custom, ≥16A; Ethernet |
| Coolant per server | approx. 1 L |
| Liquid flow | rated ≥ 10 L/min; control accuracy ±10% |
| Liquid pressure | ≤ 400 Kpa |
| Liquid medium | pure water (or distilled water) + dedicated corrosion inhibitor + antifreeze (mix ratio per freezing point) |
| Coolant pH | control range 7 ～ 8.7 |
| Liquid temperature | inlet 25 °C ～ 55 °C @ normal mode, 25 °C ～ 45 °C @ high-performance mode; storage/transport -40 °C ～ +70 °C |
| Humidity | working 5%RH ～ 85%RH (non-condensing); storage 5%RH ～ 95%RH; long-term 30%RH ～ 69%RH |

Source PDF: [神马 M63S+ manual](https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/%E7%A5%9E%E9%A9%ACM63S%2B_1766127927637.pdf). Gap note: PERFORMANCE section is chart images only; no text values.

## Cross-check disputes (AMV vs MiningNow, 2026-10-10)

> **Status: Disputed** — M63S+ hashrate and wall power: AMV says 424 Th/s @ 7208 W, MiningNow says 450TH/s @ 7650 W, maker sheet says 390T ～ 450T ±10% at 17J/T. Note the $0.10-vs-$0.07/kWh profitability caveat — gross income agrees ~1% where specs agree.

| Field | ASIC Miner Value | Mining Now | Maker sheet |
|---|---|---|---|
| Hashrate | 424 Th/s | 450TH/s | 390T ～ 450T ±10% |
| Wall power | 7208 W | 7650 W | 输入 10kW (input 10kW); no per-unit wall draw in text |
| Efficiency | not listed | 17 j/Th | 17J/T ±5% |
| Release | Aug 2024 | Jul 2024 (ann + first batch) | manual October 2024 |

- Both DB hashrates sit inside the maker's ±10% band; MiningNow's 450TH/s equals the sheet's top rating, AMV's 424 Th/s sits mid-band. Each DB pair is internally consistent at the 17 J/T class ratio.
- Economics as served 2026-10-10: AMV cell −$17.30 /day at its $0.10/kWh standard; MiningNow best price $3,653.64, income 17.66/day, profit 4.80/day at $0.07/kWh.

## Heat-reuse notes

- The ≥ 10 L/min rated flow is the defining loop constraint for this chassis — roughly double the M65S requirement (≥ 5 L/min) and triple the M64's (≥ 3.5 L/min). Loop sizing, HX isolation and coolant chemistry (pure water + corrosion inhibitor + antifreeze, pH 7 ～ 8.7): [Hydronic Heat Reuse](hydronic-heat-reuse.md).
- 70 °C outlet water and a 10kW-class three-phase input put this in the commercial/dry-cooler class of heater core, not the residential single-phase niche — that niche is the [Whatsminer M64](whatsminer-m64.md) (see also [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md)).

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M65S](whatsminer-m65s.md) — same 2U-rack chassis, 18.5 J/T
- [Whatsminer M64](whatsminer-m64.md) — compact single-phase hydro unit
