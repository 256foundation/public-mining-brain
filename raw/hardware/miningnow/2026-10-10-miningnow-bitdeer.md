# MiningNow — Bitdeer (latest ASIC miner list, Bitdeer rows)

> Source: https://miningnow.com/latest-asic-miner-list/ (profitability cross-check: https://miningnow.com/coins/bitcoin/mining-hardware/)
> Collected: 2026-10-10
> Published: Unknown
> Registry ID: miningnow
> Posture: extract (profitability DB snapshot; volatile values As-Of)

Values as of 2026-10-10. MiningNow has no per-manufacturer listing pages; this snapshot takes the maker's rows from the SSR flight payload of the latest-ASIC-miner-list page (439 products embedded; maker rows filtered — flagship SKUs only, no full-DB dump). Profitability cross-checked against the SHA-256 (Bitcoin) mining-hardware page, where the site renders Profitability = embedded income − power × 24 h × $0.07/kWh (site default rate, user-editable input); BTC shown at $83,062.25 (+0.601%) at render check. Income/profit rounded to the site's 2-decimal display; the embedded payload carries full precision.

| Model (as listed) | Hashrate | Power | Efficiency (as listed) | Best price | Income $/day | Profit $/day (@ $0.07/kWh) | Announced | First batch | Cooling |
|---|---|---|---|---|---|---|---|---|---|
| Bitdeer SealMiner A2 (226TH/s) | 226TH/s | 3729 W | 16.5 j/Th | $3,099.00 | 8.87 | 2.60 | Nov 2024 | Dec 2024 | air |
| Bitdeer SealMiner A2 Hyd (446TH/s) | 446TH/s | 7359 W | 16.5 j/Th | $6,086.00 | 17.50 | 5.14 | Nov 2024 | Dec 2024 | hydro |
| Bitdeer SealMiner A2 Pro Air (255TH/s) | 255TH/s | 3790 W | 14.86 j/Th | $3,292.00 | 10.00 | 3.64 | Mar 2025 | Mar 2025 | air |
| Bitdeer SealMiner A2 Pro Hyd (500TH/s) | 500TH/s | 7450 W | 14.9 j/Th | $5,629.00 | 19.62 | 7.10 | Mar 2025 | Mar 2025 | hydro |
| Bitdeer SealMiner A3 Air (260TH/s) | 260TH/s | 3640 W | 14 j/Th | $4,173.00 | 10.20 | 4.09 | Sep 2025 | Oct 2025 | air |
| Bitdeer SealMiner A3 Hyd (500TH/s) | 500TH/s | 6750 W | 13.5 j/Th | $6,800.00 | 19.62 | 8.28 | Sep 2025 | Oct 2025 | hydro |
| Bitdeer SealMiner A3 Pro Air (290TH/s) | 290TH/s | 3625 W | 12.5 j/Th | $4,308.00 | 11.38 | 5.29 | Sep 2025 | Oct 2025 | air |
| Bitdeer SealMiner A3 Pro Hyd (660TH/s) | 660TH/s | 8250 W | 12.5 j/Th | $7,449.00 | 25.89 | 12.03 | Sep 2025 | Oct 2025 | hydro |
| Bitdeer SealMiner A4 Pro Air (336TH/s) | 336TH/s | 3662 W | 10.9 j/Th | $3,607.00 | 13.18 | 7.03 | Apr 2026 | May 2026 | air |
| Bitdeer SealMiner A4 Pro Hyd (680TH/s) | 680TH/s | 7412 W | 10.9 j/Th | $8,689.00 | 26.68 | 14.23 | Apr 2026 | May 2026 | hydro |
| Bitdeer SealMiner A4 Ultra Hyd (886TH/s) | 886TH/s | 8372 W | 9.45 j/Th | $9,999.00 | 34.76 | 20.70 | Apr 2026 | May 2026 | hydro |
| Bitdeer SealMiner DL1 Air (25GH/s) | 25GH/s | 3725 W | 0.15 j/Th | $4,678.52 | 13.58 | 7.32 | Mar 2026 | Apr 2026 | air |
| Bitdeer SealMiner DL1 Hydro (52.5GH/s) | 52.5GH/s | 7823 W | 0.15 j/Th | $9,999.00 | 28.52 | 15.38 | Jun 2026 | Jun 2026 | hydro |

## Coverage notes

- SEALMINER A1: not in the latest-list payload; the sitemap page https://miningnow.com/asic-miner/bitdeer-sealminer-a1-226th-s/ now serves a soft-404 ('The Miner you are looking for is not found') as of 2026-10-10 — A1 effectively delisted.
- DesiWeMiner K9S / K10 Pro (acquired by Bitdeer 2024-06): not listed on MiningNow (no 'desiwe', 'k9s' or DesiWeMiner K10 rows in the payload or sitemap). Task's reseller-listed SKUs (K9S 130 Th/s 4950 W; K10 Pro 170 Th/s 3825 W) are NOT PRESENT on this DB at collection — reseller-listed (DesiWeMiner acquired by Bitdeer 2024-06), no values to cross-check.
