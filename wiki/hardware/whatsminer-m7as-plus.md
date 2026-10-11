# Whatsminer M7AS+

> Sources: official spec-sheet PDF (Chinese edition, captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [M7AS+ spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m7as-plus.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [MiningNow MicroBT rows](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The 70 °C-outlet platform's flagship — 540–600 T at 12.5 J/T (April 2026 manual), rating-twin of the 90 °C-class M7BS+; the AS/BS pair differs only in outlet-temperature class and flow spec.

## Specs (manufacturer, As-Of 2026-10-11)

From the official spec PDF, verbatim ([M7AS+ spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m7as-plus.md)):

- 功耗比 (Power Ratio): 12.5J/T±5%
- 算力 (Hashrate): 540T～600T ±10%
- 功率 (Power on wall): 7200 W±10%@ 正常模式 (normal mode)，10kW±10%@ 高性能模式 (high-performance mode)
- 重量 (Weight): 28.5kg net / 31kg gross; 尺寸（带把手） (Size with handle): 663mm×482.6mm×86mm
- 输入电压 (Input voltage): AC380V～480V; power cable custom ≥16A; coolant 约 1.3L per machine; Ethernet
- Environmental (70 °C class): inlet 25–55 ℃ normal / 25–45 ℃ high-performance; control ±2 ℃; storage -40–+70 ℃; rated flow ≥10 L/min ±10%; pressure ≤400 KPa; pH 7–8.7; working humidity 5–85 %RH
- Distinguishing mark vs the M7BS+ twin (per the capture): AS = 70 °C outlet / 25–55 ℃ inlet / ≥10 L/min flow row present; BS = 90 °C outlet / 25–60 ℃ inlet / no flow row
- No noise figure; "样机数据仅供参考。"; no storefront price — not retail-listed as of 2026-10-11

## Cross-check (AMV + MiningNow, 2026-10-10)

- AMV: "M7AS+ (540 Th)", release Oct 2026, 540 Th/s, 7500 W, 12.5j/Th, plus a storefront row "$7,000 $13 / Th" ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)) — 7500 W again matches neither sheet mode exactly (inside ±10% of 7200 W)
- MiningNow: "M7AS+ (540TH/s)", 7500 W, 13.89 j/Th, "not listed" price, Sep–Nov 2026, hydro ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md))

## Heat-reuse notes

- 12.5 J/T flagship of the 70 °C class; the A-series' documented ≥10 L/min flow makes it the loop-planning reference for the 12.5 J/T tier
- High-performance mode (10 kW) is the thermal design ceiling as across the M7x generation

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M7AS](whatsminer-m7as.md)
- [Whatsminer M7BS+](whatsminer-m7bs-plus.md)
- [Hydronic heat reuse](hydronic-heat-reuse.md)
