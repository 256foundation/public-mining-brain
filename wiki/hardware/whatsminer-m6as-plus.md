# Whatsminer M6AS+

> Sources: official spec-sheet PDF (Chinese edition, captured 2026-10-11)
> Raw: [M6AS+ spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m6as-plus.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The 70 °C-outlet A-series' 17 J/T bin (April 2026 manual) — 390–450 T, M6-generation counterpart of the AS platform. No DB rows; official PDF is the sole spec source.

## Specs (manufacturer, As-Of 2026-10-11)

From the official spec PDF, verbatim ([M6AS+ spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m6as-plus.md)):

- 功耗比 (Power Ratio): 17J/T±5%
- 算力 (Hashrate): 390T～450T ±10%
- 重量 (Weight): 28.5kg net / 31kg gross; 尺寸（带把手） (Size with handle): 86mm×482.6mm×663mm (as printed — dimension order differs from the M7AS sheets, same physical dims)
- 输入电压 (Input voltage): AC380V～480V — 输入 10kW (input 10 kW)
- **No 功率 (Power on wall) row in this manual** — wall power cannot be quoted from this source (gap; only the 10 kW input limit)
- Environmental (70 °C class): inlet 25–55 ℃ normal / 25–45 ℃ high-performance; control ±2 ℃; rated flow ≥10 L/min ±10%; pressure ≤400 KPa; pH 7–8.7; humidity rows standard
- No noise figure; cross-check 17 J/T × 420 T midpoint = 7,140 W (arithmetic only — no served wall-power row)
- No storefront price — not retail-listed as of 2026-10-11

## Heat-reuse notes

- AS-platform flow spec present (≥10 L/min) unlike its BS twin; 70 °C outlet bounds the heat-export grade

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M6AS++](whatsminer-m6as-plus-plus.md)
- [Whatsminer M6BS+](whatsminer-m6bs-plus.md)
- [Hydronic heat reuse](hydronic-heat-reuse.md)
