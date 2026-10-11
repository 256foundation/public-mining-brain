# Whatsminer M7BS

> Sources: official spec-sheet PDF (Chinese edition, captured 2026-10-11)
> Raw: [M7BS spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m7bs.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The 90 °C-outlet hydro family's S-bin — 500–552 T at 13.5 J/T, February 2026 manual, same 28.5/31 kg chassis and 7200 W/10 kW dual-mode rating as the B-series trio.

## Specs (manufacturer, As-Of 2026-10-11)

From the official spec PDF, verbatim ([M7BS spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m7bs.md)):

- 功耗比 (Power Ratio): 13.5J/T±5%
- 算力 (Hashrate): 500T～552T ±10%
- 功率 (Power on wall): 7200 W±10%@ 正常模式 (normal mode)，10kW±10%@ 高性能模式 (high-performance mode)
- 重量 (Weight): 28.5kg net / 31kg gross; 尺寸（带把手） (Size with handle): 663mm×482.6mm×86mm
- 输入电压 (Input voltage): AC380V～480V; power cable custom ≥16A; coolant 约 1.3L per machine; Ethernet
- Environmental (90 °C class): inlet 25–60 ℃ normal / 25–50 ℃ high-performance; control ±2 ℃; storage -40–+70 ℃; max inlet-outlet delta 40 ℃; outlet ≤90 ℃; pressure ≤400 KPa; pH 7–8.7
- NO liquid-flow row in this edition (gap); no noise figure; "样机数据仅供参考。"
- Cross-check: 13.5 J/T × 533 T ≈ 7,196 W ≈ 7,200 W rated
- No storefront price — not retail-listed as of 2026-10-11; no AMV/MiningNow rows in the 2026-10-10 snapshots for the M7BS (only the M7BS+ twin is DB-listed)

## Heat-reuse notes

- Same 90 °C outlet class as M7B/M7BS+ — one more efficiency point (13.5 vs 14.5 J/T) at identical 7200 W normal draw means more hashrate per exported thermal kW

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M7B](whatsminer-m7b.md)
- [Whatsminer M7BS+](whatsminer-m7bs-plus.md)
- [Hydronic heat reuse](hydronic-heat-reuse.md)
