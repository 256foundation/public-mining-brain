# Whatsminer M7AS

> Sources: official spec-sheet PDF (Chinese edition, captured 2026-10-11); ASIC Miner Value snapshot (2026-10-10)
> Raw: [M7AS spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m7as.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The A-series S-bin — 500–552 T at 13.5 J/T on the 70 °C-outlet platform (April 2026 manual), rating-twin of the B-series M7BS but with the flow row present.

## Specs (manufacturer, As-Of 2026-10-11)

From the official spec PDF, verbatim ([M7AS spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m7as.md)):

- 功耗比 (Power Ratio): 13.5J/T±5%
- 算力 (Hashrate): 500T～552T ±10%
- 功率 (Power on wall): 7200 W±10%@ 正常模式 (normal mode)，10kW±10%@ 高性能模式 (high-performance mode)
- 重量 (Weight): 28.5kg net / 31kg gross; 尺寸（带把手） (Size with handle): 663mm×482.6mm×86mm
- 输入电压 (Input voltage): AC380V～480V; power cable custom ≥16A; coolant 约 1.3L per machine; Ethernet
- Environmental (70 °C class): inlet 25–55 ℃ normal / 25–45 ℃ high-performance; control ±2 ℃; rated flow ≥10 L/min ±10%; pressure ≤400 KPa; pH 7–8.7; humidity rows standard
- No noise figure; Chinese edition only; "样机数据仅供参考。"
- No storefront price — not retail-listed as of 2026-10-11

## Cross-check (AMV, 2026-10-10)

- AMV: "M7AS (520 Th)", release Oct 2026, 520 Th/s, **7500 W** ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)) — AMV's 7500 W matches neither the sheet's 7200 W normal nor its 10 kW high-performance mode (7200 × 1.04 ≈ 7500, inside the ±10% envelope, but the mode basis is unstated). No MiningNow row (the coverage note records the M7AS/M7BS gap).

## Heat-reuse notes

- 70 °C class with the full flow spec (≥10 L/min ±10%) — loop sizing is documented, unlike the B-series twins

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M7A](whatsminer-m7a.md)
- [Whatsminer M7AS+](whatsminer-m7as-plus.md)
- [Hydronic heat reuse](hydronic-heat-reuse.md)
