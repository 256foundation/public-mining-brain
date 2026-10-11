# Whatsminer M70

> Sources: official spec-sheet PDF (Chinese edition, captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [M70 spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m70.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [MiningNow MicroBT rows](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The M7x air-cooled generation's base unit — 214–236 T at 14.5 J/T per the official manual (cover dated December 2025). Not retail-listed on the shop as of capture; the spec record is the official file-index PDF (coolingId 12, air).

## Specs (manufacturer, As-Of 2026-10-11)

From the official spec PDF, verbatim ([M70 spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m70.md)):

- 功耗比 (Power Ratio): 14.5J/T±5%@25°C
- 算力 (Hashrate): 214T～236T ±5%
- 功率 (Power on wall): 3140 W ～3500 W ±10%
- 重量 (Weight): 11.5kg net / 12.6kg gross; 尺寸 (Size): 430mm×155mm×226mm
- 工作温度 (Working temperature): -5°C～+35°C; 风量 (Air flow): 350CFM
- 电源线 (Power cable): IEC C19 ≥16A; 输入电压 (Input voltage): AC220V～240V; Ethernet
- No noise figure in the manual — only the 350 CFM airflow; "样机数据仅供参考。" (prototype data for reference only)
- Arithmetic cross-check: 14.5 J/T × 225 T midpoint = 3,262 W, inside the 3140–3500 W band
- No storefront price — not retail-listed as of 2026-10-11

## Cross-check (AMV + MiningNow, 2026-10-10)

- AMV: "M70 (214 Th)", release Dec 2025, 214 Th/s, 3140 W ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)) — the manual range bottom, same 3140 W band floor
- MiningNow: "M70 (214TH/s)", 3140 W, 14.67 j/Th, best price $2,403.10, air, Dec 2025 ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md)) — its 14.67 j/Th is DB-derived (3140/214), vs the sheet's 14.5 J/T ±5% rating; both round to the same platform

## Heat-reuse notes

- Air-cooled, same 430×155×226 mm chassis and 350 CFM as the M6x air family — the M7x air generation slots into identical racks at higher efficiency (14.5 vs 19.9 J/T base)
- Single-phase 220–240 V input retained

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M70S](whatsminer-m70s.md)
- [Whatsminer M70S+](whatsminer-m70s-plus.md)
- [Air-cooled hashrate heating](air-cooled-hashrate-heating.md)
