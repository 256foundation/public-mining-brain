# Whatsminer M6AS++

> Sources: official spec-sheet PDF (Chinese edition, captured 2026-10-11)
> Raw: [M6AS++ spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m6as-plus-plus.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The 70 °C-outlet A-series' 15.5 J/T bin (April 2026 manual) — 434–478 T. No DB rows; official PDF is the sole spec source.

## Specs (manufacturer, As-Of 2026-10-11)

From the official spec PDF, verbatim ([M6AS++ spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m6as-plus-plus.md)):

- 功耗比 (Power Ratio): 15.5J/T±5%
- 算力 (Hashrate): 434T～478T ±10%
- 重量 (Weight): 28.5kg net / 31kg gross; 尺寸（带把手） (Size with handle): 86mm×482.6mm×663mm (as printed — dimension order differs from the M7AS sheets, same physical dims)
- 输入电压 (Input voltage): AC380V～480V — 输入 10kW (input 10 kW)
- **No 功率 (Power on wall) row in this manual** (gap; only the 10 kW input limit)
- Environmental (70 °C class): inlet 25–55 ℃ normal / 25–45 ℃ high-performance; control ±2 ℃; rated flow ≥10 L/min ±10%; pressure ≤400 KPa; pH 7–8.7; humidity rows standard
- No noise figure; cross-check 15.5 J/T × 464.5 T midpoint ≈ 7,200 W (arithmetic only); "样机数据仅供参考。"
- No storefront price — not retail-listed as of 2026-10-11

## Heat-reuse notes

- AS platform (70 °C outlet, ≥10 L/min flow spec present); the ++ bin matches the M63S++'s 15.5 J/T rating on the newer platform

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M6AS+](whatsminer-m6as-plus.md)
- [Whatsminer M6BS++](whatsminer-m6bs-plus-plus.md)
- [Hydronic heat reuse](hydronic-heat-reuse.md)
