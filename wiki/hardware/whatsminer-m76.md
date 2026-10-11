# Whatsminer M76

> Sources: official spec-sheet PDF (Chinese edition, captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [M76 spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m76.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [MiningNow MicroBT rows](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The 2026 oil-cooled (油冷) family's base bin — 336–374 T at 14.5 J/T with the family's dual-mode rating (5200 W normal / 7000 W high-performance). The official index classes it coolingId 14 (immersion); the manual itself says 油冷, oil cooling, with S5X/S3X insulating liquid.

## Specs (manufacturer, As-Of 2026-10-11)

From the official spec PDF, verbatim ([M76 spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m76.md)):

- 功耗比 (Power Ratio): 14.5J/T±5%
- 算力 (Hashrate): 336T～374T ±10%
- 功率 (Power on wall): 5200W ±10%@ 正常模式 (normal mode)；7000W ±10%@ 高性能模式 (high-performance mode)
- 重量 (Weight): 18 kg net / 19 kg gross; 尺寸（带把手） (Size with handle): 401mm×267.5mm×147mm
- 输入电压 (Input voltage): AC380V～480V; power cable custom ≥16A; Ethernet
- Environmental: inlet 25–55 ℃ normal / 25–45 ℃ high-performance; control ±2 ℃; rated flow **≥24 L/min**; medium "绝缘液（S5X/S3X）" — insulating liquid (dielectric oil, same as M66)
- Family gaps: no noise, no liquid-pressure/PH rows, no working-humidity row, no per-machine coolant volume (flow given instead)
- Cross-check: 14.5 J/T × 355 T midpoint = 5,147.5 W ≈ 5,200 W normal rating
- No storefront price — not retail-listed as of 2026-10-11

## Cross-check (AMV + MiningNow, 2026-10-10)

- AMV: "M76 (336 Th)", release Dec 2025, 336 Th/s, 5200 W ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)) — the manual range floor
- MiningNow: "M76 (336TH/s)", 5200 W, 15.48 j/Th, best price $3,638.00, Dec 2025 ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md))

## Heat-reuse notes

- Oil-cooled at 5200/7000 W dual-mode — heat export needs a dielectric-oil loop (S5X/S3X), not water; inlet band 25–55 ℃
- The 7000 W high-performance mode is the loop-sizing ceiling; normal-mode arithmetic (14.5 J/T × midpoint) confirms the 5200W rating

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M76S](whatsminer-m76s.md)
- [Whatsminer M66](whatsminer-m66.md)
- [Immersion heat reuse](immersion-heat-reuse.md)
