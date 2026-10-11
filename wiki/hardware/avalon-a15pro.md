# Avalon A15Pro (A15Pro-221T)

> Sources: Canaan A15 series page (Wayback snapshot 2026-06-11) + miner index (2026-04-12 snapshot); ASIC Miner Value + MiningNow snapshots (values as of 2026-10-10)
> Raw: [A15 series page](../../raw/hardware/canaan/2026-06-11-wayback-canaan-miner-a15-series.md); [Canaan miner index](../../raw/hardware/canaan/2026-04-12-wayback-canaan-miner-index.md); [AMV Canaan](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-canaan.md); [MiningNow Canaan](../../raw/hardware/miningnow/2026-10-10-miningnow-canaan.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Specs (maker series card, snapshot 2026-06-11)

- Card (verbatim): Avalon Miner A15Pro — "Quite a Bitcoin Harvester" — "From $2762.50 (Bulk Order)" — "221T · 3 Work Modes · 3662W · 16.8J/TH · -5 - 35 ℃ · 2 x 12050 Fan · L301mm x W192mm x H292mm · 14.9Kg".
- "3 Work Modes" ("Fine control of costs" per the index page) — Canaan's multi-mode tuning knob.
- Maker disclaimer on every card: "* All provided data and parameters are based on laboratory results in a controlled environment."

## Cross-check (AMV vs MiningNow, 2026-10-10)

| Source | Hashrate | Power | Efficiency | Price | Release |
|---|---|---|---|---|---|
| Maker | 221T | 3662 W | 16.8 J/TH | From $2,762.50 (bulk) | — |
| [AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-canaan.md) | 221 Th/s | 3662 W | — | — | Mar 2025 |
| [MiningNow](../../raw/hardware/miningnow/2026-10-10-miningnow-canaan.md) | 220TH/s | 3662 W | 16.65 j/Th | $1,310.00 | Nov 2024 / first listed Dec 2024 |

> **Status: Disputed** — hashrate 221 vs 220 (bin rounding, inside ±5%); price maker $2,762.50 bulk vs MiningNow street $1,310.00 (different channels, both verbatim); AMV release Mar 2025 vs MiningNow Nov 2024. Hashrate/power agree.

## Field scale (IR corroboration)

- Sep 8, 2025 PR (live IR mirror, quoted in the A15 capture): the Luxor financing partnership "already facilitated the sale of more than 5,000 Avalon® A15 Pro bitcoin mining machines in August to a leading U.S.-based institutional bitcoin miner."
- Feb 23, 2026 6-K (miner-index capture Notes): Canaan "purchased an additional 6,840 Canaan Avalon A15Pro-AVG-221T mining rigs from Cipher" (~4.4 EH/s West Texas; site-level fleet efficiency ~25.7 J/TH).

## Heat-reuse notes

- 3662 W air-cooled unit, 2×12050 fans, 14.9 kg — the classic home-rack class; the A15Pro+ refresh (higher bin) is the [A15Pro+ 240T](avalon-a15pro-plus.md) page.

## See Also

- [Avalon overview](avalon-overview.md), [A15Pro+ 240T](avalon-a15pro-plus.md), [A16XP](avalon-a16xp.md)
