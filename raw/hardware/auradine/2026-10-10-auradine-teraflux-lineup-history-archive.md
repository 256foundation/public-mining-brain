# Auradine Teraflux™ lineup history — AT1500/AT2860 (previous gens) and third-gen 9.8 J/TH announcement

> Source: https://web.archive.org/web/20230815055608/https://auradine.com/auradine-unveils-worlds-first-4nm-bitcoin-mining-systems-with-highest-performance-and-breakthrough-energytune-technology/ + https://web.archive.org/web/20231207200805/https://auradine.com/auradine-unveils-next-generation-teraflux-bitcoin-miners-setting-new-benchmarks-for-efficient-and-sustainable-mining/ + https://news.bitcoin.com/u-s-designed-bitcoin-miner-delivers-promising-results/
> Collected: 2026-10-10
> Published: 2023-07-25 (launch PR, archived); 2023-11-14 (next-gen PR, archived); 2025-02-12 (Bitcoin.com review article)
> Registry ID: auradine-site

**ARCHIVE CAPTURE** — the live site no longer lists the AT1500/AT2860 generation; this file documents the lineage from archived press releases and a third-party review. Snapshot URLs and dates above.

## Gen 1 (Jul 2023) — world's-first 4nm claim (verbatim, archived launch PR, 2023-07-25)

- "The game-changing Teraflux™ family is powered by the world's first 4nm silicon chip technology for bitcoin mining designed by the Auradine team in the US."
- "world's fastest air-cooled system performance with hash rates up to 185 TH/s and up to 3x higher hashing density (TH/s per unit volume) immersion miners"
- "ability to operate air-cooled miners up to 50°C ambient, boot-up in sub-zero temperatures, and maintain operations without reboots"
- "The systems will ship to early access customers in Q3 with production volumes starting in Q4 2023."
- Model numbers not named in this PR (family-level claims only). CEO quote from Fred Thiel, Marathon Digital Holdings (customer/investor).
- Funding context: "$81 million in Series A funding led by Celesta Capital and Mayfield" (May 2023).

## Gen 2 (Nov 2023) — AT2880 + AI3680 announced (verbatim, archived PR, 2023-11-14)

- "AT2880 air-cooled miners are capable of achieving an output of 0 to 260 TH/s, with an optimal efficiency of 16 J/TH."
- "AI3680 immersion-cooled miners are capable of achieving an output of 0 to 375 TH/s, with an optimal efficiency of 15 J/TH."
- "Capability to operate at temperatures up to 50°C (122°F)"
- "EnergyTune™ and AutoTune™ technologies allow miners to dynamically adjust the Bitcoin hash rate based on-demand response needs of the electrical grids."
- Also introduced: "Invest in Bitcoin America program".
- Shipments of AT2880 "began in July 2024, with production volumes said to be ramping up in Q3 2024" (per Bitcoin.com, below).

## AT1500 (first-gen air-cooled) — third-party measured numbers (verbatim, Bitcoin.com, 2025-02-12)

- "Bitsbetrippin' reviewed Auradine's earlier generation Teraflux miner, the air-cooled AT1500. That model delivered a hashrate of 180 TH/s with an efficiency of 25.34 J/TH in high-power mode. In low-power mode, the AT1500 achieved 112 TH/s at 23.1 J/TH."
- Same article on the AT2880 gen: "Auradine initially announced the launch of its Teraflux AT2880 bitcoin miner in November 2023, highlighting a hashrate range of 0–260 TH/s with optimal efficiency of 16 J/TH. Shipments began in July 2024, with production volumes said to be ramping up in Q3 2024."
- Independent tweet quoted in the article ( Bitsbetrippin, Jan 12, 2025): "…ielding 222TH (17jt) and 2) set to fixed 150T (2500w) (16.8jt) in lower power mode."

**Gap:** AT2860 model — exists in fleet-management software (pyasic lists Auradine AD models "AT1500 (Stock)", "AT2860 (Stock)", "AT2880 (Stock)" at docs.pyasic.org/en/latest/miners/auradine/AD), but no official spec sheet was found live or archived during this capture. Numbers for the AT2860 remain a gap.

## Gen 3 announced (2025-11-12) — 9.8 J/TH, model numbers not yet published (verbatim from auradine.com PR "Auradine Advances Teraflux™ BTC Mining Product Portfolio…", surfaced via search; PR dated November 12, 2025)

- "Powered by Auradine's third-generation ASIC and FluxVision™ software suite, the new Teraflux™ systems set a new benchmark for efficiency, reliability, and operational ease." (9.8 J/TH headline)
- Efficiency table as printed (Cooling Mode | Air | Hydro | Immersion):
  - Normal J/TH (TH/s): 11 (310) | 11 (900) | 10.7 (360)
  - Eco J/TH (TH/s): 10.3 (240) | 9.8 (600) | 9.8 (240)
- "SMART (Scalable Miner Architecture for Resilience and Fault Tolerance) hashboard design allows continued operation even with multiple chip failures"
- "A fully integrated solution, from advanced ASICs to scalable 1 MW and 2 MW modular containers"
- "Auradine is also announcing its FluxVision™ fleet management mobile app, available on the App Store and Google Play soon."
- Context (Yahoo Finance, same day): "Auradine did not disclose pricing or availability details for the Teraflux lineup." Also notes "$150 million raise" (April 2025) and MARA as investor.

## Notes

- Discrepancy to flag: the live products page lists AH3880 "Normal: 14.3 J/TH", the 2025-03 Business Wire release said "as low as 14.5J/TH in normal mode", and the 2025-11-12 PR table shows 11 J/TH normal / 9.8 eco for "Hydro" — the PR numbers appear to describe the third-generation systems, not the AH3880 data-sheet numbers. Recorded verbatim from each source.
- The 3nm / 0.87 TH/s-per-chip ASIC on the live products page is the sellable chip product (May 2025 PR "Auradine Expands Bitcoin Mining Solutions with ASIC chips…" announced chip sales; not captured in full).
