# Whatsminer M64

> Sources: official MicroBT product manual (PDF, verbatim, Chinese edition); ASIC Miner Value + MiningNow snapshots (2026-10-10, both omit the SKU); Hashrate Heatpunks community record
> Raw: [MicroBT manual: M64](../../raw/hardware/microbt/2026-10-10-microbt-site-m64.md); [MicroBT shop catalog](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [MiningNow MicroBT rows](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md); [AMV/MN cross-check report](../../raw/hardware/asicminervalue/_REPORT.md); [Heatpunks telegram digest](../../raw/economics/2026-10-09-heatpunks-telegram-signal.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

Compact/short form-factor hydro unit (371mm × 290 mm × 109mm, single-phase 220–277 V input) — the heater-fit oddball of the M6x hydro line, distinct from the 2U-rack M6x hydro chassis. The maker spec sheet here is the manual dated October 2024 (pre-sales API file id 26).

## Specs (manufacturer sheet, As-Of 2026-10-10)

Verbatim values, labels translated from the Chinese edition (神马 M64):

| Item | Value |
|---|---|
| Power ratio | 19.9J/T ±5% |
| Hashrate | 180T ～ 206T ±10% |
| Cooling class | hydro (水冷), outlet water temperature up to 80 °C |
| Size with handle | 371mm × 290 mm × 109mm |
| Weight | 16kg net / 17kg gross |
| Input | AC220V ～ 277V, 输入 5kW (input 5kW); power cable custom, ≥25A; Ethernet |
| Coolant per server | approx. 1 L |
| Liquid flow | rated ≥ 3.5 L/min; control accuracy ±10% |
| Liquid pressure | ≤ 400 Kpa |
| Liquid medium | pure water (or distilled water) + dedicated corrosion inhibitor + antifreeze (mix ratio per freezing point) |
| Coolant pH | control range 7 ～ 8.7 |
| Liquid temperature | inlet 35 °C ～ 70 °C @ normal mode, 35 °C ～ 55 °C @ high-performance mode; storage/transport -40 °C ～ +70 °C |
| Humidity | working 5%RH ～ 85%RH; storage 5%RH ～ 95%RH; long-term 30%RH ～ 69%RH (all non-condensing) |

Source PDF: [神马 M64 manual](https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/%E7%A5%9E%E9%A9%ACM64_1766127962171.pdf). Gap note: PERFORMANCE section is chart images only; no text values. The inlet window (35 °C ～ 70 °C normal mode) runs hotter than the inlet windows on the M66S/M66S+/M63S+ immersion/hydro siblings — relevant when returning domestic-loop water to the miner.

## Cross-check disputes (AMV vs MiningNow, 2026-10-10)

> **Status: Disputed** — M64 rated power: the manual lists 输入 5kW (input 5kW), while the community heater record measures "4000 Watts (normal mode M64)" and does the arithmetic "19.9j x 200Th is about 4kw not 5". There is no DB cross-check at all: AMV and MiningNow both omit the SKU (the cross-check report logs Whatsminer M64/M64S/M65S as absent from both DBs), so the $0.10-vs-$0.07/kWh profitability caveat has nothing to compare — gross income agrees ~1% only where specs agree, and here no third-party specs exist.

| Field | ASIC Miner Value | Mining Now | Maker sheet |
|---|---|---|---|
| Hashrate | not listed | not listed | 180T ～ 206T ±10% |
| Wall power | not listed | not listed | 输入 5kW (input 5kW); community: about 4kw at normal mode |
| Efficiency | not listed | not listed | 19.9J/T ±5% |
| Release | not listed | not listed | manual October 2024 |

- Rated power reading: plan around 4kw in normal mode (19.9 J/T class at ~200 T), with the 5kW manual input as ceiling; the fuller dispute record (HeatCore "5kw" marketing vs field data) lives in [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md).
- The M64S appears in no official list captured — rename flag in [Whatsminer overview](whatsminer-overview.md).

## Heat-reuse notes

- Heater-fit profile: 80 °C outlet, single-phase 220–277 V input, and only ≥ 3.5 L/min rated flow — the smallest loop demand in the MicroBT hydro line. The community headline specs when it landed were single-phase PSU and "80 C / 176 F water outlet temp" (2024-08-19).
- Manual coolant spec is pure water + corrosion inhibitor + antifreeze, pH 7 ～ 8.7; loop chemistry, aluminum water blocks and HX-isolation practice are documented in [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md) and [Hydronic Heat Reuse](hydronic-heat-reuse.md).
- Hot-inlet tolerance (35 °C ～ 70 °C normal mode) is wider than the M66S/M63S+ class — relevant when cascading off an existing hydronic return.

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md) — the community build record
- [Whatsminer M65S](whatsminer-m65s.md), [Whatsminer M63S+](whatsminer-m63s-plus.md) — 2U-rack hydro siblings
- [Hydronic Heat Reuse](hydronic-heat-reuse.md)
