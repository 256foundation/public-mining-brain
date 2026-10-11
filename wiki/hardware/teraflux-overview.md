# Auradine Teraflux Overview

> Sources: Auradine/Velaura products page (auradine.com 301 → velaura.ai), captured 2026-10-10; official Teraflux AT2880 / AH3880 / AI3680 data-sheet PDFs (© 2025 Auradine, Inc., hosted on velaura.ai); archived Teraflux lineup history (2023 launch PRs, 2025-02-12 Bitcoin.com review, 2025-11-12 Gen-3 announcement); ASIC Miner Value manufacturer listing; MiningNow latest-ASIC-list sweep
> Raw: [Auradine/Velaura products page](../../raw/hardware/auradine/2026-10-10-auradine-velaura-products-page.md); [AT2880 data sheet](../../raw/hardware/auradine/2026-10-10-auradine-teraflux-at2880-datasheet.md); [AH3880 data sheet](../../raw/hardware/auradine/2026-10-10-auradine-teraflux-ah3880-datasheet.md); [AI3680 data sheet](../../raw/hardware/auradine/2026-10-10-auradine-teraflux-ai3680-datasheet.md); [Lineup history archive](../../raw/hardware/auradine/2026-10-10-auradine-teraflux-lineup-history-archive.md); [ASIC Miner Value — Auradine](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-auradine.md); [MiningNow — Auradine](../../raw/hardware/miningnow/2026-10-10-miningnow-auradine.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

Teraflux™ is Auradine's Bitcoin-mining hardware family: air, hydro and immersion-cooled SHA-256 miners, modular megawatt containers, a sellable 3nm ASIC chip, and the FluxOS™ firmware / FluxVision™ fleet-management stack with grid demand-response built in. The company positions the portfolio as delivering "the lowest total cost of ownership for Bitcoin mining solutions" (AT2880 data sheet). Per-model pages: [Auradine Teraflux AT2880](auradine-at2880.md), [Auradine Teraflux AH3880](auradine-ah3880.md), [Auradine Teraflux AI3680](auradine-ai3680.md).

## The rebrand (As-Of 2026-10-10)

- As of the 2026-10-10 capture, `auradine.com` 301-redirects to `velaura.ai`; the site title is "Ultra-Low-Power Infrastructure for the AI Era".
- The Bitcoin section is still branded "Teraflux™ Bitcoin Mining Solutions — Engineered in the USA", and the contact email is info@velaura.ai (older copy on the page still shows info@auradine.com). Address: 3200 Coronado Drive, Santa Clara, CA 95054.
- An archived products page from 2026-01-16 (web.archive.org) shows the identical lineup still under the Auradine name — the rebrand is recent and the product data is unchanged.

## Enterprise / fleet posture

- The contact form states "Minimum Order 500 units" — this is a B2B/fleet vendor, not a hobbyist reseller.
- No prices anywhere on the products page; no pricing or availability was disclosed for the third-generation systems either (see below).
- No per-product HTML pages exist on the live site; specs live on the products page and in PDF data sheets only.
- FluxVision (cloud fleet management) is purchased separately; every miner ships with a web console and on-device APIs. Fleet integrations: Foreman and AwesomeMiner.
- Containers: "Containers house 100-200 miners each", with "Options for both 1 or 2MW" and "Air, immersion, and hydro-cooled options." The Gen-3 announcement similarly describes "A fully integrated solution, from advanced ASICs to scalable 1 MW and 2 MW modular containers".

## The three product lines (As-Of 2026-10-10)

| Model | Cooling | Datasheet range | Products-page range | Modes (datasheet) | PSU class |
|---|---|---|---|---|---|
| [AT2880](auradine-at2880.md) | Air | 0-270 TH/s | 40 – 270 TH/sec | Normal: 16 J/TH at 180 TH/s; Turbo: 18 J/TH at 270 TH/s | 5000 Watts |
| [AH3880](auradine-ah3880.md) | Hydro | 0-600TH/s | 100 - 600 TH/sec | Eco: 14.3J/TH at 400TH/s; Mid: 15.8J/TH at 500TH/s; Turbo: 17.5J/TH at 600 TH/s | 10000 Watts |
| [AI3680](auradine-ai3680.md) | Single-phase immersion | 0-365 TH/s | 40 - 365 TH/sec | Normal: 16 J/TH at 250TH/s; Turbo: 19 J/TH at 365 TH/s | 7500 Watts |

Range note: the datasheets print "Range: 0-… TH/s" while the products page prints a higher floor (e.g. 40 – 270 TH/sec for the AT2880); both recorded verbatim. Products-page footnote: TH/s & J/TH specs +/- 8 % at 25°C ambient; datasheet footnotes say preliminary estimates, ±8%.

**Sellable ASIC one-liner.** The Teraflux™ ASIC is also sold as a component: 3nm process node, Hash Rate up to 0.87 TH/s, Power Consumption 12 watts typical, Input Voltage 240-350 mV, Max Junction Temp 110º C, Package Size 8 x 8mm — contact-sales CTA, no price.

## Third generation (announced 2025-11-12) — no model numbers yet

- The 2025-11-12 announcement ("Auradine Advances Teraflux™ BTC Mining Product Portfolio…") claims the new Teraflux systems are "Powered by Auradine's third-generation ASIC and FluxVision™ software suite" with a 9.8 J/TH headline. No model numbers were published (still true on the 2026-10-10 products page).
- Efficiency table as printed in the PR (Cooling Mode | Air | Hydro | Immersion): Normal J/TH (TH/s) — 11 (310) | 11 (900) | 10.7 (360); Eco J/TH (TH/s) — 10.3 (240) | 9.8 (600) | 9.8 (240).
- "SMART (Scalable Miner Architecture for Resilience and Fault Tolerance) hashboard design allows continued operation even with multiple chip failures" (PR wording).
- Also announced: a FluxVision™ fleet-management mobile app "available on the App Store and Google Play soon".
- Context (Yahoo Finance, same day): "Auradine did not disclose pricing or availability details for the Teraflux lineup." The raise history: $81 million Series A (May 2023, led by Celesta Capital and Mayfield) and a $150 million raise (April 2025, MARA among investors).
- Discrepancy to flag: these Gen-3 PR numbers (e.g. hydro 11 J/TH normal / 9.8 J/TH eco) do not describe the AH3880 data-sheet numbers (14.3 J/TH Eco); recorded verbatim per source — see [AH3880](auradine-ah3880.md#cross-check).

## FluxOS / FluxVision — the demand-response tie-in

- **Grid integration claim (AT2880 sheet, verbatim):** "Auradine is the only hardware OEM to directly integrate with the power grid and Qualified Scheduling Entities (QSEs) such as Voltus." Power Management, under which "A QSE can modulate power consumption on your mining farm based on demand response to grid supply and load curtailment for cost savings", is available with FluxVision.
- **FluxOS™ miner firmware** (products page): EnergyTune™ — "Real time tuning with no reboots, no downtime"; Secure Boot — "Protects against boot process tampering with secure software installation"; On-Device APIs — "Comprehensive APIs for full control — no external software required"; Remote Diagnostics; Stratum V2 — "Native encrypted protocol with lower bandwidth for secure, reliable, and high-performance mining."
- **FluxVision™ management software** (products page): "Manage your entire fleet from one platform with intuitive, real-time control"; "Adjust hash rate and power instantly for optimized energy use and demand response"; "Automate recurring curtailment events to align with grid and energy market needs"; pool-config whitelisting; fleet-wide updates; Zero Touch Provisioning; cloud APIs; a FluxVision mobile app was announced 2025-11-12.
- **DVFS detail (AT2880 sheet):** Auradine's built-in DVFS "perform these optimizations in half the time" of the ten-minutes-per-iteration, reboot-prone tuning on traditional miners — the mechanism behind EnergyTune's ECO/Turbo modes.
- Relevance for heat-reuse builders: scheduled curtailment and dynamic hash/power control are exactly the levers heater duty-cycling needs, but the fleet posture (see above) puts these machines out of hobbyist reach — see the per-model heat-reuse notes.

## Lineage and gaps

- **Gen 1 (2023-07-25 PR, archived):** "world's first 4nm silicon chip technology for bitcoin mining" designed in the US; air-cooled hash rates up to 185 TH/s claimed; $81 million Series A. Model numbers not named in the PR.
- **Gen 2 (2023-11-14 PR, archived):** AT2880 air at "an output of 0 to 260 TH/s, with an optimal efficiency of 16 J/TH"; AI3680 immersion at "an output of 0 to 375 TH/s, with an optimal efficiency of 15 J/TH". AT2880 shipments "began in July 2024, with production volumes said to be ramping up in Q3 2024" (Bitcoin.com, 2025-02-12). The live datasheets (2025 uploads) rate the AT2880 at 0-270 TH/s and the AI3680 at 0-365 TH/s.
- **AT1500 (Gen 1 air):** third-party measured numbers only (Bitsbetrippin' review via Bitcoin.com, 2025-02-12): 180 TH/s at 25.34 J/TH high-power; 112 TH/s at 23.1 J/TH low-power. The live site no longer lists this generation (archive capture only).
- **AT2860:** listed in fleet-management software (pyasic: "AT1500 (Stock)", "AT2860 (Stock)", "AT2880 (Stock)") but no official spec sheet was found live or archived — numbers remain a gap.
- **Gen 3 (2025-11-12):** 9.8 J/TH headline, model numbers not yet published (see above).

## Cross-check (As-Of 2026-10-10)

- **ASIC Miner Value: 3 Auradine SKUs, all current-gen flagships** — AT2880 (180 Th/s, 4680 W, Nov 2024), AI3680 (360 Th/s, 6840 W, Dec 2024), AH3880 (600 Th/s, 10740 W, Mar 2025). AMV standard electricity cost $0.10/kWh; on manufacturer listing pages the SSR Profit cells show electricity cost only (top-coin column empty as served). Profitability values are volatile; see the raw capture for the As-Of snapshot.
- **MiningNow: zero Auradine listings** — no 'auradine'/'teraflux' slugs in the 439-product payload, the 438-URL sitemap, or the SHA-256 hardware page as of 2026-10-10, so nothing cross-checks there (that DB rendered BTC at $83,062.25 with a $0.07/kWh default at capture).
- **AT1500 / AT2860: no DB cross-check exists** — AMV lists only the 3 SKUs above (probes of the at1500/at2860 slugs returned 404 on 2026-10-10) and MiningNow has zero Auradine rows.

## See Also

- Models: [Auradine Teraflux AT2880](auradine-at2880.md) · [Auradine Teraflux AH3880](auradine-ah3880.md) · [Auradine Teraflux AI3680](auradine-ai3680.md)
- Heat reuse: [Air-Cooled Hashrate Heating](air-cooled-hashrate-heating.md) · [Hydronic Heat Reuse](hydronic-heat-reuse.md) · [Immersion Heat Reuse](immersion-heat-reuse.md) · [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md)
- Single-phase hydro alternatives: [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md)
