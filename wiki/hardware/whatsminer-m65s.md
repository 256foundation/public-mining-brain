# Whatsminer M65S

> Sources: official MicroBT product manual (PDF, verbatim, Chinese edition); ASIC Miner Value + MiningNow snapshots (2026-10-10, both omit the SKU); Heatpunks forum signal via telegram digest
> Raw: [MicroBT manual: M65S](../../raw/hardware/microbt/2026-10-10-microbt-site-m65s.md); [MicroBT shop catalog](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [MiningNow MicroBT rows](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md); [AMV/MN cross-check report](../../raw/hardware/asicminervalue/_REPORT.md); [Heatpunks telegram digest](../../raw/economics/2026-10-09-heatpunks-telegram-signal.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

2U-rack hydro unit sharing its 86mm × 482.6mm × 663mm chassis with the M63S+ and the M7x hydro line (the shop-listed M73 shows the same "86mm*483mm*663mm with handle" chassis). Not retail-listed on the maker shop — captured from the official product-manual PDF (pre-sales API file id 25, hydro), manual dated October 2024.

## Specs (manufacturer sheet, As-Of 2026-10-10)

Verbatim values, labels translated from the Chinese edition (神马 M65S):

| Item | Value |
|---|---|
| Power ratio | 18.5J/T ±5% |
| Hashrate | 370T ～ 400T ±10% |
| Cooling class | hydro (水冷), outlet water temperature up to 80 °C |
| Size with handle | 86mm × 482.6mm × 663mm |
| Weight | 27.5kg net / 30kg gross |
| Input | AC380V ～ 480V, 输入 10 kW (input 10 kW); power cable custom, ≥16A; Ethernet |
| Coolant per server | approx. 1 L |
| Liquid flow | rated ≥ 5 L/min; control accuracy ±10% |
| Liquid pressure | ≤ 400 Kpa |
| Liquid medium | per manual — pure water + corrosion inhibitor + antifreeze (standard hydro line coolant mix) |
| Coolant pH | control range 7 ～ 8.7 |
| Liquid temperature | inlet 30 °C ～ 60 °C @ normal mode, 30 °C ～ 50 °C @ high-performance mode; storage/transport -40 °C ～ +70 °C |
| Humidity | working 5%RH ～ 85%RH (non-condensing); storage 5%RH ～ 95%RH; long-term 30%RH ～ 69%RH |

Source PDF: [神马 M65S manual](https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/%E7%A5%9E%E9%A9%ACM65S_1766127981375.pdf). Gap note: PERFORMANCE section is chart images only; no text values.

## Cross-check disputes (AMV vs MiningNow, 2026-10-10)

> **Status: Disputed** — M65S third-party coverage: absent from both AMV and MiningNow on 2026-10-10 (both coverage notes; the cross-check report logs Whatsminer M64/M64S/M65S as missing from both DBs, M65S alongside them). The manual is the only number set on file — 370T ～ 400T ±10% at 18.5J/T ±5% — so there is no DB field to dispute and the $0.10-vs-$0.07/kWh profitability caveat is moot here (gross income agrees ~1% only where specs agree).

| Field | ASIC Miner Value | Mining Now | Maker sheet |
|---|---|---|---|
| Hashrate | not listed | not listed | 370T ～ 400T ±10% |
| Wall power | not listed | not listed | 输入 10 kW (input 10 kW) |
| Efficiency | not listed | not listed | 18.5J/T ±5% |
| Release | not listed | not listed | manual October 2024 |

- One field datapoint from the field: the first Heat Core NS200 system was commissioned with a WhatsMiner M65S on "~35% propylene glycol + demineralized water", with Whatsminer documentation calling for a "composite corrosion inhibitor from Peric" dosed in wt% and no clear product name or EU source (heatpunk forum, 2026-02-11, via the telegram digest).

## Heat-reuse notes

- 80 °C outlet on the shared 2U-rack chassis, ≥ 5 L/min rated flow (half the M63S+ requirement), inlet window 30 °C ～ 60 °C normal mode — a hotter window than the M66S immersion units run, a cooler-ended one than the M64's.
- Coolant story in practice: the Heat Core NS200 commissioning used ~35% propylene glycol + demineralized water; the Peric inhibitor sourcing gap is recorded in [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md) (coolant section).
- Loop design and chemistry: [Hydronic Heat Reuse](hydronic-heat-reuse.md).

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M63S+](whatsminer-m63s-plus.md) — same chassis, 17 J/T, ≥ 10 L/min flow
- [Whatsminer M64](whatsminer-m64.md) — compact single-phase hydro unit
- [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md)
