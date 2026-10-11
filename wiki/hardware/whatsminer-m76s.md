# Whatsminer M76S

> Sources: official spec-sheet PDF (Chinese edition, captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [M76S spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m76s.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [MiningNow MicroBT rows](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The oil-cooled family's middle bin — 362–406 T at 13.5 J/T, same dual-mode 5200/7000 W rating and 18 kg chassis as the whole M76 family ([M76S spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m76s.md)).

## Specs (manufacturer, As-Of 2026-10-11)

From the official spec PDF, verbatim:

- 功耗比 (Power Ratio): 13.5J/T±5%
- 算力 (Hashrate): 362T～406T ±10%
- 功率 (Power on wall): 5200W ±10%@ 正常模式 (normal mode)；7000W ±10%@ 高性能模式 (high-performance mode)
- 重量 (Weight): 18 kg net / 19 kg gross; 尺寸（带把手） (Size with handle): 401mm×267.5mm×147mm
- 输入电压 (Input voltage): AC380V～480V; power cable custom ≥16A; Ethernet
- Environmental: inlet 25–55 ℃ normal / 25–45 ℃ high-performance; control ±2 ℃; rated flow ≥24 L/min; medium "绝缘液（S5X/S3X ）" insulating liquid
- Family gaps: no noise, no pressure/PH rows, no working-humidity row, no per-machine coolant volume
- Cross-check: 13.5 J/T × 384 T midpoint = 5,184 W ≈ 5,200 W; "样机数据仅供参考。"
- No storefront price — not retail-listed as of 2026-10-11

## Cross-check (AMV + MiningNow, 2026-10-10)

- AMV: "M76S (362 Th)", release Dec 2025, 362 Th/s, 5200 W ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)) — range floor
- MiningNow: "M76S (362TH/s)", 5200 W, 14.36 j/Th, best price $5,199.00, Dec 2025 ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md))

## Heat-reuse notes

- Same oil loop as the M76 (S5X/S3X dielectric, ≥24 L/min); 13.5 J/T at the same 5200W normal rating yields more hashrate per kW of exported heat than the M76 base bin

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M76](whatsminer-m76.md)
- [Whatsminer M76S+](whatsminer-m76s-plus.md)
- [Immersion heat reuse](immersion-heat-reuse.md)
