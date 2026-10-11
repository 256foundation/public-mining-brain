# Whatsminer M7B

> Sources: official spec-sheet PDF (Chinese edition, captured 2026-10-11)
> Raw: [M7B spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m7b.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The next-gen hydro family's base bin (B-series, cover dated February 2026) — 470–526 T at 14.5 J/T, the first MicroBT hydro line rated for **90 °C outlet**. Not retail-listed at capture; spec record is the official PDF (coolingId 13, tag 最新).

## Specs (manufacturer, As-Of 2026-10-11)

From the official spec PDF, verbatim ([M7B spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m7b.md)):

- 功耗比 (Power Ratio): 14.5J/T±5%
- 算力 (Hashrate): 470T～526T ±10%
- 功率 (Power on wall): 7200 W±10%@ 正常模式 (normal mode)，10kW±10%@ 高性能模式 (high-performance mode)
- 重量 (Weight): 28.5kg net / 31kg gross (lighter than the M73S class's 29.5/32); 尺寸（带把手） (Size with handle): 663mm×482.6mm×86mm
- 输入电压 (Input voltage): AC380V～480V; power cable custom ≥16A; coolant "约 1.3L" per machine (up from ~1 L); Ethernet
- Environmental (the 90 °C-class deltas): inlet 25–60 ℃ normal / 25–50 ℃ high-performance; control ±2 ℃; storage -40–+70 ℃; **max inlet-outlet delta 40 ℃; outlet ≤90 ℃**; pressure ≤400 KPa; medium pure/distilled water + corrosion inhibitor + antifreeze; pH 7–8.7; humidity rows as the hydro standard
- **NO liquid-flow row** in the B-series manual — no rated-flow figure in this edition (recorded gap)
- Cross-check: 14.5 J/T × 498 T midpoint ≈ 7,221 W ≈ 7,200 W rated
- No storefront price — not retail-listed as of 2026-10-11

## Heat-reuse notes

- The 90 °C outlet class is the heat-reuse headline: 7.2–10 kW per unit delivered at up to 90 °C outlet — directly usable-grade heat for hydronic/export designs, a generation above the 70 °C class
- Wider inlet band (25–60 ℃) and the 40 ℃ max delta tolerance are the loop-design parameters that come with it; the missing rated-flow row means flow sizing must come from commissioning data, not the manual

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M7BS](whatsminer-m7bs.md)
- [Whatsminer M7A](whatsminer-m7a.md)
- [Hydronic heat reuse](hydronic-heat-reuse.md)
