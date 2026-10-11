# Whatsminer M7A

> Sources: official spec-sheet PDF (Chinese edition, captured 2026-10-11); ASIC Miner Value snapshot (2026-10-10)
> Raw: [M7A spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m7a.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The A-series hydro family's base bin (cover dated April 2026) — 470–526 T at 14.5 J/T, ratings identical to the B-series M7B but on the **70 °C outlet** platform with a rated-flow row the B-series lacks.

## Specs (manufacturer, As-Of 2026-10-11)

From the official spec PDF, verbatim ([M7A spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m7a.md)):

- 功耗比 (Power Ratio): 14.5J/T±5%
- 算力 (Hashrate): 470T～526T ±10%
- 功率 (Power on wall): 7200 W±10%@ 正常模式 (normal mode)，10kW±10%@ 高性能模式 (high-performance mode)
- 重量 (Weight): 28.5kg net / 31kg gross; 尺寸（带把手） (Size with handle): 663mm×482.6mm×86mm
- 输入电压 (Input voltage): AC380V～480V; power cable custom ≥16A; coolant 约 1.3L per machine; Ethernet
- Environmental (70 °C class): inlet 25–55 ℃ normal / 25–45 ℃ high-performance; control ±2 ℃; storage -40–+70 ℃; rated flow **≥10 L/min** ±10%; pressure ≤400 KPa; pH 7–8.7; full humidity rows (working 5–85 %RH)
- No noise figure; "样机数据仅供参考。"
- No storefront price — not retail-listed as of 2026-10-11

## Cross-check (AMV, 2026-10-10)

- AMV: "M7A (470 Th)", release Jul 2026, 470 Th/s, 10000 W ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)) — AMV's 10000 W matches the sheet's **high-performance** mode rating; the normal mode is 7200 W. Mode ambiguity in DB wall-power rows is a live reconciliation point across the whole M7x generation.

## Heat-reuse notes

- 70 °C outlet class: heat-export grade below the B-series; the ≥10 L/min rated-flow row (absent from B-series manuals) is the loop-sizing number here
- Same 28.5 kg / 1.3 L chassis as the B-series — A vs B is a platform spec (outlet temperature class), not a form-factor change

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M7AS](whatsminer-m7as.md)
- [Whatsminer M7B](whatsminer-m7b.md)
- [Hydronic heat reuse](hydronic-heat-reuse.md)
