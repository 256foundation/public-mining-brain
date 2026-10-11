# Whatsminer M70S+

> Sources: official spec-sheet PDF (Chinese edition, captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [M70S+ spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m70s-plus.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [MiningNow MicroBT rows](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The air-cooled M7x generation's efficiency point — 244–280 T at 12.5 J/T, the best air-cooled rating in MicroBT's current official file list (cover dated December 2025; coolingId 12, air; not retail-listed at capture).

## Specs (manufacturer, As-Of 2026-10-11)

From the official spec PDF, verbatim ([M70S+ spec PDF](../../raw/hardware/microbt/2026-10-11-microbt-site-m70s-plus.md)):

- 功耗比 (Power Ratio): 12.5J/T±5%@25°C
- 算力 (Hashrate): 244T～280T ±5%
- 功率 (Power on wall): 3140 W ～3500 W ±10%
- 重量 (Weight): 11.5kg net / 12.6kg gross; 尺寸 (Size): 430mm×155mm×226mm
- 工作温度 (Working temperature): -5°C～+35°C; 风量 (Air flow): 350CFM
- 电源线 (Power cable): IEC C19 ≥16A; 输入电压 (Input voltage): AC220V～240V; Ethernet
- No noise figure; Chinese-edition PDF only; "样机数据仅供参考。"
- Arithmetic cross-check: 12.5 J/T × 262 T midpoint = 3,275 W, inside the 3140–3500 W band
- No storefront price — not retail-listed as of 2026-10-11

## Cross-check (AMV + MiningNow, 2026-10-10)

- AMV: "M70S+ (244 Th)", release Dec 2025, 244 Th/s, 3140 W ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)) — the manual range floor
- MiningNow: "M70S+ (244TH/s)", 3140 W, 12.87 j/Th, best price $2,665.23, air, Dec 2025 ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md))
- Distinct SKU from the retail M70S (248 TH / 13.5 J/TH card) — the S+ suffix is a different, more efficient bin

## Heat-reuse notes

- Air-cooled at 12.5 J/T: 3140 W –3500 W per unit across a 244–280 T range — the highest air-side efficiency on record in the wiki's MicroBT set
- Same 350 CFM chassis — per-rack heat per TH drops proportionally to the efficiency gain

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M70](whatsminer-m70.md)
- [Whatsminer M70S](whatsminer-m70s.md)
- [Air-cooled hashrate heating](air-cooled-hashrate-heating.md)
