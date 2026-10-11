# MiningNow — Canaan (latest ASIC miner list, Canaan rows)

> Source: https://miningnow.com/latest-asic-miner-list/ (profitability cross-check: https://miningnow.com/coins/bitcoin/mining-hardware/)
> Collected: 2026-10-10
> Published: Unknown
> Registry ID: miningnow
> Posture: extract (profitability DB snapshot; volatile values As-Of)

Values as of 2026-10-10. MiningNow has no per-manufacturer listing pages; this snapshot takes the maker's rows from the SSR flight payload of the latest-ASIC-miner-list page (439 products embedded; maker rows filtered — flagship SKUs only, no full-DB dump). Profitability cross-checked against the SHA-256 (Bitcoin) mining-hardware page, where the site renders Profitability = embedded income − power × 24 h × $0.07/kWh (site default rate, user-editable input); BTC shown at $83,062.25 (+0.601%) at render check. Income/profit rounded to the site's 2-decimal display; the embedded payload carries full precision.

| Model (as listed) | Hashrate | Power | Efficiency (as listed) | Best price | Income $/day | Profit $/day (@ $0.07/kWh) | Announced | First batch | Cooling |
|---|---|---|---|---|---|---|---|---|---|
| Canaan Avalon A15 (194TH/s) | 194TH/s | 3647 W | 18.8 j/Th | $1,099.00 | 7.61 | 1.48 | Nov 2024 | Jan 2025 | air |
| Canaan Avalon A15 Pro (220TH/s) | 220TH/s | 3662 W | 16.65 j/Th | $1,310.00 | 8.63 | 2.48 | Nov 2024 | Dec 2024 | air |
| Canaan Avalon A15 Pro+ (240TH/s) | 240TH/s | 3720 W | 15.5 j/Th | not listed | 9.42 | 3.17 | Jul 2026 | Aug 2026 | air |
| Canaan Avalon A15XP (206TH/s) | 206TH/s | 3667 W | 17.8 j/Th | $1,274.00 | 8.08 | 1.92 | Nov 2024 | Dec 2024 | air |
| Canaan Avalon A1566 (185TH/s) | 185TH/s | 3420 W | 18.49 j/Th | $1,443.00 | 7.26 | 1.51 | May 2024 | Oct 2024 | air |
| Canaan Avalon A1566HA 2U (480TH/s) | 480TH/s | 8064 W | 16.8 j/Th | $3,657.73 | 18.83 | 5.29 | Jun 2025 | Jul 2025 | hydro |
| Canaan Avalon A1566I (249TH/s) | 249TH/s | 4500 W | 18.07 j/Th | $3,115.84 | 9.77 | 2.21 | Sep 2024 | Dec 2024 | immersion |
| Canaan Avalon A16 (282TH/s) | 282TH/s | 3900 W | 13.83 j/Th | $4,399.00 | 11.06 | 4.51 | Oct 2025 | Mar 2026 | air |
| Canaan Avalon A16XP (300TH/s) | 300TH/s | 3850 W | 12.83 j/Th | $5,829.00 | 11.77 | 5.30 | Oct 2025 | May 2026 | air |
| Canaan Avalon A1466 (150TH/s) | 150TH/s | 3230 W | 21.53 j/Th | $1,755.38 | 5.89 | 0.46 | Sep 2023 | Sep 2023 | air |

## Coverage notes

- A15XP-209T and A15Pro-221T (both on AMV) are absent from MiningNow; MiningNow alone lists A15 Pro+ 240 Th (announced Jul 2026, price not listed).
- A1566I: MiningNow slug AND hash_rate field both say 249 TH/s while AMV lists 261 Th — see _REPORT.md mismatch table.
- a15-pro-218th-s slug says 218 Th while the payload hash_rate field says 220TH/s (internal MiningNow inconsistency, captured as shown).
