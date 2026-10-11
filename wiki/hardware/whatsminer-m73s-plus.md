# Whatsminer M73S+

> Sources: official spec-sheet PDF (Chinese edition, captured 2026-10-11); ASIC Miner Value snapshot (2026-10-10)
> Raw: [M73S+ spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m73s-plus.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

MicroBT's current hero product — the whatsminer.com home hero (modified 2025-12-09: titleEn "M73S+", introductionEn "Born for mining") — 540–600 T at 12.5 J/T on the 70°C-outlet hydro generation, the hydro flagship of the official file list. Not retail-listed at capture; spec record is the official PDF (coolingId 13).

## Specs (manufacturer, As-Of 2026-10-11)

From the official spec PDF, verbatim ([M73S+ spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m73s-plus.md)):

- 功耗比 (Power Ratio): 12.5J/T±5%
- 算力 (Hashrate): 540T～600T ±10%
- 功率 (Power on wall): 7200 W±10%@ 正常模式 (normal mode)，10kW±10%@ 高性能模式 (high-performance mode)
- 重量 (Weight): 29.5kg net / 32kg gross; 尺寸（带把手） (Size with handle): 663mm×482.6mm×86mm
- 输入电压 (Input voltage): AC380V～480V; power cable custom ≥16A; coolant "约 1L" per machine; Ethernet
- Environmental: inlet 25–55 ℃ normal / 25–45 ℃ high-performance; control ±2 ℃; rated flow ≥10 L/min ±10%; pressure ≤400 KPa; medium pure/distilled water + corrosion inhibitor + antifreeze; pH 7–8.7; storage -40–+70 ℃; working humidity 5–85 %RH
- Outlet class: 水冷（出水温度达 70°C) — 70 °C outlet; cross-check 12.5 J/T × 576 T midpoint ≈ 7,200 W rated
- No noise figure; Chinese edition only (the English-named file has no resolvable URL via the API); "样机数据仅供参考。"
- No storefront price — not retail-listed as of 2026-10-11

## Cross-check (AMV, 2026-10-10)

- AMV: "M73S+ (540 Th)", release Dec 2025, 540 Th/s, 7200 W ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)) — the manual range floor; no MiningNow row exists for the M73S+ (the coverage note records M7AS/M7BS-family gaps)

## Heat-reuse notes

- The hydro flagship at 12.5 J/T ties the M70S+ air unit's efficiency — the J/T gap between air and hydro cooling classes has effectively closed at the flagship tier
- Dual-mode rating again: 7200 W normal, 10 kW high-performance — loop design must take the 10 kW ceiling
- 70 °C outlet class (not the M7B family's 90 °C — [M7B spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m7b.md)): heat-export grade is bounded by the outlet temperature

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M73S](whatsminer-m73s.md)
- [Whatsminer M7BS+](whatsminer-m7bs-plus.md)
- [Hydronic heat reuse](hydronic-heat-reuse.md)
