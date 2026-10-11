# Auradine Teraflux AI3680

> Sources: official Teraflux™ AI3680 data-sheet PDF (© 2025 Auradine, Inc.; site upload path dated 2025-02, hosted on velaura.ai), captured 2026-10-10; velaura.ai products page (auradine.com 301 → velaura.ai); archived Teraflux lineup history (2023-11-14 Gen-2 PR); ASIC Miner Value manufacturer listing; MiningNow latest-ASIC-list sweep
> Raw: [AI3680 data sheet](../../raw/hardware/auradine/2026-10-10-auradine-teraflux-ai3680-datasheet.md); [Auradine/Velaura products page](../../raw/hardware/auradine/2026-10-10-auradine-velaura-products-page.md); [Lineup history archive](../../raw/hardware/auradine/2026-10-10-auradine-teraflux-lineup-history-archive.md); [ASIC Miner Value — Auradine](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-auradine.md); [MiningNow — Auradine](../../raw/hardware/miningnow/2026-10-10-miningnow-auradine.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

The AI3680 is Auradine's "ASIC-based single-phase immersion-cooled Bitcoin miner" — same web-console/APIs-plus-FluxVision™ management model as the rest of the Teraflux line. Announced with the Gen-2 wave on 2023-11-14 at "an output of 0 to 375 TH/s, with an optimal efficiency of 15 J/TH", it is rated 0-365 TH/s on the current data sheet (© 2025 Auradine, Inc., uploaded 2025-02). This sheet additionally documents **FluxGPT**, "the generative AI-based conversational experience that's designed to assist you in finding answers or information on Auradine products quickly and efficiently" (a FluxVision feature). Family context and fleet posture: [Auradine Teraflux Overview](teraflux-overview.md).

## Specs (datasheet, As-Of 2026-10-10)

| AI3680 Product Specifications | Value |
|---|---|
| Crypto Algorithm | SHA-256 |
| Hashing Performance | Range: 0-365 TH/s (preliminary, ±8%) — Normal: 16 J/TH at 250TH/s — Turbo: 19 J/TH at 365 TH/s |
| Fluid Inlet Temperature | 68 to 122°F (20 to 50°C) |
| Cooling Mechanism | Single-phase immersion |
| Coolants Supported | "Qualified with, and warrantied for, use with Engineered Fluids Bitcool 888 and Shell S3X only." |
| Power Supply Option A (dual input) | 7500 Watts, 2 x C20 input; 200-240V nominal (180-264V); 0-17.6 Amp per input |
| Power Supply Option B (single input) | 7500 Watts, 1 x PA45 input; 208-277V nominal (200-305V); 0-45 Amp |
| AC Input Frequency | 48-62 Hz |
| Connectivity | RJ45 Ethernet 10/100/1000 |
| Dimensions (L/W/H) | 310 x 202 x 290 mm (12.2 x 8 x 11.5 in) |
| Weight | 40 lbs / 18.1 kg |
| Storage Temperature | -40 to 158°F (-40 to 70°C) |
| Operation Humidity | 20-80% RH non-condensing |
| Operation Altitude | up to 3,000M (9,840ft) |

Products-page deltas (same capture): Output 40 - 365 TH/sec; Efficiency Normal 16J/TH, Turbo 19 J/TH; Operating Range 0 to 50º C.

Generation note: the 2023-11-14 Gen-2 PR claimed 0 to 375 TH/s at 15 J/TH; the live 2025-02 datasheet rates 0-365 TH/s at 16 J/TH Normal — both recorded verbatim per source.

## Cross-check

**AMV-only** (ASIC Miner Value has the SKU; MiningNow has none).

| AMV row (as listed) | Release | Hashrate | Power | Algorithm | Profit (as shown) |
|---|---|---|---|---|---|
| Auradine Teraflux AI3680 (360 Th) | Dec 2024 | 360 Th/s | 6840 W | SHA-256 | -$16.42 /day |

- AMV's 360 Th/s / 6840 W sits between the datasheet Normal (16 J/TH at 250TH/s) and Turbo (19 J/TH at 365 TH/s) points; the 7500-Watts PSU rating is the ceiling and "system maximum may be slightly lower" per the datasheet footnote. AMV profit cells show electricity cost only at its standard $0.10/kWh (top-coin column empty as served); values volatile As-Of 2026-10-10.
- **MiningNow: zero Auradine listings** as of 2026-10-10 — no cross-check possible there.

## Heat-reuse notes

- **Immersion for tank installs.** This is a drop-in single-phase immersion miner for a tank: 7500-Watts-class draw, fluid inlet 68 to 122°F (20 to 50°C) — tank design guidance in [Immersion Heat Reuse](immersion-heat-reuse.md) and [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md).
- **Warranty is fluid-locked**: "Qualified with, and warrantied for, use with Engineered Fluids Bitcool 888 and Shell S3X only." Plan fluid sourcing and compatibility before deployment — an off-warranty fluid choice is a business risk, not just a technical one.
- **Enterprise posture, not hobbyist**: "Minimum Order 500 units", no public prices, FluxVision purchased separately — see the [overview posture](teraflux-overview.md#enterprise--fleet-posture). Hobbyist single-tank immersion economics look very different; see [Immersion Heat Reuse](immersion-heat-reuse.md).
- **Same demand-response stack** as the AT2880 (QSE/Voltus integration via FluxVision, EnergyTune ECO/Turbo) — relevant if a heated tank doubles as a curtailable load.

## See Also

- [Auradine Teraflux Overview](teraflux-overview.md) — rebrand, fleet posture, Gen-3, FluxOS/FluxVision
- [Immersion Heat Reuse](immersion-heat-reuse.md)
- [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md)
