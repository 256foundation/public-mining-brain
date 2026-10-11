# Avalon A1566HA-500T

> Sources: shop.canaan.io product page (Wayback snapshot 2025-10-06); ASIC Miner Value + MiningNow snapshots (values as of 2026-10-10)
> Raw: [A1566HA-500T shop page](../../raw/hardware/canaan/2025-10-06-wayback-shop-canaan-a1566ha-500t.md); [AMV Canaan](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-canaan.md); [MiningNow Canaan](../../raw/hardware/miningnow/2026-10-10-miningnow-canaan.md); [A15 series page](../../raw/hardware/canaan/2026-06-11-wayback-canaan-miner-a15-series.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Specs (maker shop listing, snapshot 2025-10-06)

- Listing: "Avalon Miner A1566HA-500T" — badge "Specification: 500T | 8064W | 16.8J/T — Cooling System: Hydro-cooling — Payment Method: USD | BTC | USDT(ERC20)"; price "$5,800.00 ($11.6/T)"; Ships From CN.
- Parameters table (verbatim): Hashrate "500TH/s, -5%~+5%"; Power Consumption "8064W, -10%~+10%@Wall-Plug"; Power Efficiency "16.8J/TH, -3%~+3%"; Cooling Hydro; Operating Temperature "10℃~50℃"; Net Dimensions "556mm *482.6mm* 86mm"; Net Weight 20kg; Accessory Power Supply.
- Warranty: "A 360-day warranty is provided starting from the date of pick-up from the seller."
- Variant history (capture notes): A1566HA seen at 440T (2026-02), 460T (2025-06), 480T (2025-07), 500T (2025-10) — the hydro bin rotates; "HA" suffix = hydro.

## Cross-check (AMV vs MiningNow, 2026-10-10)

| Source | Hashrate | Power | Efficiency | Price | Release |
|---|---|---|---|---|---|
| Maker shop (2025-10) | 500 TH/s ±5% | 8064 W | 16.8 J/TH | $5,800.00 ($11.6/T) | — |
| [AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-canaan.md) | 480 Th/s | 8064 W | — | — | Jun 2025 |
| [MiningNow](../../raw/hardware/miningnow/2026-10-10-miningnow-canaan.md) | 480TH/s | 8064 W | 16.8 j/Th | $3,657.73 | Jun 2025 / Jul 2025 |

> **Status: Disputed** — hashrate 500T (shop snapshot, Oct 2025) vs 480T (both DBs, Jun 2025): different shipped bins of the same A1566HA rack captured months apart, not a measurement conflict (both at 8064 W / 16.8 J/TH); price $5,800.00 (Canaan shop) vs MiningNow $3,657.73 (street). AMV carries no A15Pro Hyd SKU — "the hydro entry in the A15 generation is the Avalon A1566HA 2U (480 Th, 8064 W)" (AMV capture note).

## Heat-reuse notes

- **The A15-generation heater-class unit**: 8064 W hydro loop in a 2U rack chassis (556×482.6×86 mm, 20 kg), operating window 10–50 ℃ — commercial hydronic-loop hardware, not a hobbyist box.
- Lineage: the A1566 line is "the second generation of 1xJ/T series products" (Canaan's Nov 2024 HIVE PR, quoted in the shop capture); Dec 2024 IR PR records an agreement with AGM Group for 2,000 Avalon A15 Hydro units "with an option for the customer to acquire up to 30,000 additional units." Immersion sibling: A1566I (249T/261T listings; AMV 261 Th / 4500 W).

## See Also

- [Avalon overview](avalon-overview.md), [A15Pro](avalon-a15pro.md), [Whatsminer M63S+](whatsminer-m63s-plus.md) (the 2U-hydro class comparison)
