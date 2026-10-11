# Whatsminer M73

> Sources: shop.whatsminer.com detail page + catalog (SSR, verbatim); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [M65S manual](../../raw/hardware/microbt/2026-10-10-microbt-site-m65s.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [MiningNow MicroBT rows](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md); [AMV/MN cross-check report](../../raw/hardware/asicminervalue/_REPORT.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

The shop's hydro flagship: 512TH card at 14.5J/TH, second rung of the retail shipping ladder behind the M70S (see [Whatsminer overview](whatsminer-overview.md)). No manual PDF captured for this SKU; the shop detail page is the maker-side record.

## Specs (manufacturer sheet, As-Of 2026-10-10)

Shop detail page, verbatim:

| Item | Value |
|---|---|
| Card | 512TH, 14.5J/TH, $12.0/T (HK; unit price $6,144) |
| Power on wall | 7424.00W |
| PSU | "AC380~480V, 3W+ ground, input 10kw" |
| Size | "86mm*483mm*663mm with handle" |
| Weight | Net weight: 27.5kg, Gross Weight: 30kg |
| Coolant demand per machine | "About 1L" |
| Cooling class | hydro (official spec-file list coolingId 13; MiningNow cooling field hydro) |
| pid/skuId | 80/191 |

The M73 shares the 2U-rack hydro chassis with the M65S and M63S+ (86mm-class × 483mm × 663mm) and sits in MicroBT's hydro file-list group with M73S/M73S+ above it.

## Cross-check disputes (AMV vs MiningNow, 2026-10-10)

> **Status: Disputed** — M73 hashrate, efficiency and wall power: shop says 512TH @ 14.5J/TH and 7424.00W on wall, AMV says 470 Th/s @ 7200 W, MiningNow says 470TH/s @ 7200 W (15.32 j/Th). Note the $0.10-vs-$0.07/kWh profitability caveat — gross income agrees ~1% where specs agree.

| Field | Shop (maker) | ASIC Miner Value | Mining Now |
|---|---|---|---|
| Hashrate | 512TH | 470 Th/s | 470TH/s |
| Efficiency | 14.5J/TH | not listed | 15.32 j/Th |
| Wall power | 7424.00W | 7200 W | 7200 W |
| Release | — | Dec 2025 | Dec 2025 (ann + first batch) |
| Cooling | hydro (file list) | (no cooling column) | hydro |

- The two DBs agree with each other exactly (470 TH/s-class @ 7200 W, Dec 2025); each source is internally consistent at its own bin — the shop pair at 14.5J/TH-class, the DB pair at MiningNow's listed 15.32 j/Th. Same maker-card-vs-DB-row pattern as the M70S.
- Siblings on the DBs: M73S 500 Th/s @ 7200 W (both DBs agree), M73S+ 540 Th/s @ 7200 W (AMV only — no MiningNow row). The whatsminer.com hero banner (modified 2025-12-09) is the M73S+, tagged "Born for mining".
- Economics as served 2026-10-10: AMV cell −$17.28 /day at its $0.10/kWh standard; MiningNow best price $4,617.00, income 18.44/day, profit 6.34/day at $0.07/kWh.

## Heat-reuse notes

- Hydro 2U-rack chassis ("86mm*483mm*663mm with handle"), ~1 L coolant per machine, 10kw-class three-phase input — a dry-cooler/commercial-loop heater core like the M63S+/M65S, not a single-phase residential unit (that remains the [Whatsminer M64](whatsminer-m64.md)).
- No manual text captured for this SKU, so no maker flow/temperature ratings on file — the M65S sheet (same chassis class) is the nearest documented reference: ≥ 5 L/min, outlet up to 80 °C. Loop design: [Hydronic Heat Reuse](hydronic-heat-reuse.md).

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M70S](whatsminer-m70s.md) — the air-cooled rung below it on the shop ladder
- [Whatsminer M65S](whatsminer-m65s.md) — same 2U-rack hydro chassis class
- [Hydronic Heat Reuse](hydronic-heat-reuse.md)
