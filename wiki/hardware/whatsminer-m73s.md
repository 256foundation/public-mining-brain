# Whatsminer M73S

> Sources: official spec-sheet PDF (Chinese edition, captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [M73S spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m73s.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [MiningNow MicroBT rows](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The 70°C-outlet hydro generation's S-bin — 500–552 T at 13.5 J/T with a dual-mode power rating (7200 W normal / 10 kW high-performance). Not retail-listed at capture; spec record is the official file-index PDF (coolingId 13, hydro).

## Specs (manufacturer, As-Of 2026-10-11)

From the official spec PDF, verbatim ([M73S spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m73s.md)):

- 功耗比 (Power Ratio): 13.5J/T±5%
- 算力 (Hashrate): 500T～552T ±10%
- 功率 (Power on wall): 7200 W±10%@ 正常模式 (normal mode)，10kW±10%@ 高性能模式 (high-performance mode) — dual-mode rating, new vs the M6x single-band sheets
- 重量 (Weight): 29.5kg net / 32kg gross; 尺寸（带把手） (Size with handle): 663mm×482.6mm×86mm
- 输入电压 (Input voltage): AC380V～480V; power cable custom ≥16A; coolant "约 1L" per machine; Ethernet
- Environmental: inlet 25–55 ℃ normal / 25–45 ℃ high-performance; control ±2 ℃; rated flow ≥10 L/min ±10%; pressure ≤400 KPa; medium pure/distilled water + corrosion inhibitor + antifreeze; pH 7–8.7; storage -40–+70 ℃; working humidity 5–85 %RH
- Outlet temperature class: 水冷（出水温度达 70°C) — water cooling, outlet up to 70 °C (the generation below the M7B family's 90 °C — [M7B spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m7b.md))
- Cross-check: 13.5 J/T × 533 T ≈ 7,200 W rated; no noise figure; "样机数据仅供参考。"
- No storefront price — not retail-listed as of 2026-10-11

## Cross-check (AMV + MiningNow, 2026-10-10)

- AMV: "M73S (500 Th)", release Dec 2025, 500 Th/s, 7200 W ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)) — the manual range floor
- MiningNow: "M73S (500TH/s)", 7200 W, 14.4 j/Th, best price $4,520.00, hydro, Dec 2025 ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md))
- Both DB rows sit at the range floor with the normal-mode wall rating; the sheet's 552 T top and 10 kW high-performance mode appear only in the PDF.

## Heat-reuse notes

- Hydro at 13.5 J/T, 500–552 T: the per-unit heat ceiling is the 10 kW high-performance mode — a hydronic loop must be sized for 10 kW ±10%, not the 7200 W normal rating
- 70°C outlet class: usable for direct hydronic heat export, one generation behind the 90°C-outlet M7B family

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M73S+](whatsminer-m73s-plus.md)
- [Whatsminer M73](whatsminer-m73.md)
- [Hydronic heat reuse](hydronic-heat-reuse.md)
