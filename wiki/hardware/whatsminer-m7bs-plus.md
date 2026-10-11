# Whatsminer M7BS+

> Sources: official spec-sheet PDF (Chinese edition, captured 2026-10-11); ASIC Miner Value snapshot (2026-10-10)
> Raw: [M7BS+ spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m7bs-plus.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The 90 °C-outlet hydro family's flagship (B-series, cover dated February 2026) — 540–600 T at 12.5 J/T, the hottest-outlet hydro unit in MicroBT's official file list (coolingId 13, tag 最新). Not retail-listed at capture; spec record is the official PDF.

## Specs (manufacturer, As-Of 2026-10-11)

From the official spec PDF, verbatim ([M7BS+ spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m7bs-plus.md)):

- 功耗比 (Power Ratio): 12.5J/T±5%
- 算力 (Hashrate): 540T～600T ±10%
- 功率 (Power on wall): 7200 W±10%@ 正常模式 (normal mode)，10kW±10%@ 高性能模式 (high-performance mode)
- 重量 (Weight): 28.5kg net / 31kg gross; 尺寸（带把手） (Size with handle): 663mm×482.6mm×86mm
- 输入电压 (Input voltage): AC380V～480V; power cable custom ≥16A; coolant 约 1.3L per machine; Ethernet
- Environmental (the 90 °C-class deltas): inlet 25–60 °C normal / 25–50 °C high-performance; control ±2 °C; storage -40–+70 °C; **max inlet–outlet delta 40 °C; outlet ≤90 °C**; pressure ≤400Kpa; medium pure/distilled water + corrosion inhibitor + antifreeze; pH 7–8.7; humidity rows standard
- **NO liquid-flow row** in this manual — the environmental table goes straight from liquid temperature to liquid pressure (recorded gap)
- Cross-check: 12.5 J/T × 576 T midpoint ≈ 7,200 W rated
- No storefront price — not retail-listed as of 2026-10-11

## Cross-check (AMV, 2026-10-10)

- AMV: "M7BS+ (540 Th)", release May 2026, 540 Th/s, 10000 W ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)) — AMV's 10000 W matches the sheet's high-performance mode; the normal mode is 7200 W. No MiningNow row (the coverage note records the M7BS-family gap).

## Heat-reuse notes

- The 90 °C outlet class at the 12.5 J/T flagship tier: up to 10 kW per unit delivered at ≤90 °C outlet with a 40 °C max inlet–outlet delta — directly usable-grade heat for hydronic/export designs
- Like the whole B-series, the manual omits the rated-flow row — flow sizing must come from commissioning data, not the manual

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M7BS](whatsminer-m7bs.md)
- [Whatsminer M7AS+](whatsminer-m7as-plus.md)
- [Hydronic heat reuse](hydronic-heat-reuse.md)
