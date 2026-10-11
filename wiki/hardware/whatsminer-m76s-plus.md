# Whatsminer M76S+

> Sources: official spec-sheet PDF (Chinese edition, captured 2026-10-11); ASIC Miner Value snapshot (2026-10-10)
> Raw: [M76S+ spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m76s-plus.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The oil-cooled family's top bin — 390–440 T at 12.5 J/T, the best efficiency in the M76 family at the same 5200/7000 W dual-mode rating ([M76S+ spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m76s-plus.md)).

## Specs (manufacturer, As-Of 2026-10-11)

From the official spec PDF, verbatim:

- 功耗比 (Power Ratio): 12.5J/T±5%
- 算力 (Hashrate): 390T～440T ±10%
- 功率 (Power on wall): 5200W ±10%@ 正常模式 (normal mode)；7000W ±10%@ 高性能模式 (high-performance mode)
- 重量 (Weight): 18 kg net / 19 kg gross; 尺寸（带把手） (Size with handle): 401mm×267.5mm×147mm
- 输入电压 (Input voltage): AC380V～480V; power cable custom ≥16A; Ethernet
- Environmental: inlet 25–55 ℃ normal / 25–45 ℃ high-performance; control ±2 ℃; rated flow ≥24 L/min; medium "绝缘液（S5X/S3X ）" (S5X/S3X insulating liquid)
- Family gaps: no noise; no liquid-pressure row ("≤400Kpa appears only in the hydro manuals"); no PH row; no working-humidity row; no per-machine coolant volume
- Cross-check: 12.5 J/T × 415 T midpoint = 5,187.5 W ≈ 5,200 W; "样机数据仅供参考。"
- No storefront price — not retail-listed as of 2026-10-11

## Cross-check (AMV, 2026-10-10)

- AMV: "M76S+ (390 Th)", release Dec 2025, 390 Th/s, 5200 W ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)) — range floor; no MiningNow row for the M76S+

## Heat-reuse notes

- 12.5 J/T in oil matches the M73S+/M70S+ hydro/air flagships — the 12.5 J/T tier now exists in all three cooling classes (air M70S+, hydro M7BS+/M73S+, oil M76S+)
- Same S5X/S3X dielectric loop, ≥24 L/min, inlet 25–55 ℃

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M76S](whatsminer-m76s.md)
- [Whatsminer M73S+](whatsminer-m73s-plus.md)
- [Immersion heat reuse](immersion-heat-reuse.md)
