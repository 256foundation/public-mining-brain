# Auradine Teraflux AH3880

> Sources: official Teraflux™ AH3880 data-sheet PDF (© 2025 Auradine, Inc.; site upload path dated 2025-09, hosted on velaura.ai), captured 2026-10-10; velaura.ai products page (auradine.com 301 → velaura.ai); 2025-03 Business Wire launch note (as recorded in the lineup-history archive capture); ASIC Miner Value manufacturer listing; MiningNow latest-ASIC-list sweep
> Raw: [AH3880 data sheet](../../raw/hardware/auradine/2026-10-10-auradine-teraflux-ah3880-datasheet.md); [Auradine/Velaura products page](../../raw/hardware/auradine/2026-10-10-auradine-velaura-products-page.md); [Lineup history archive](../../raw/hardware/auradine/2026-10-10-auradine-teraflux-lineup-history-archive.md); [ASIC Miner Value — Auradine](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-auradine.md); [MiningNow — Auradine](../../raw/hardware/miningnow/2026-10-10-miningnow-auradine.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

The AH3880 is Auradine's hydro-cooled SHA-256 miner — "an ASIC-based hydro-cooled Bitcoin miner" in a rack-mount form factor (665 x 485.65 x 88 mm, 64 lbs / 29 kg, 2U-style), announced March 2025 (Business Wire: "The rack-mounted hydro miner achieves an exceptional 600TH/s with efficiency as low as 14.5J/TH in normal mode"). It runs the same FluxOS/FluxVision software stack as the AT2880, though this sheet omits the "Hardware-Based Secure Boot" section that appears on the AT2880/AI3680 sheets. Family context and fleet posture: [Auradine Teraflux Overview](teraflux-overview.md).

## Specs (datasheet, As-Of 2026-10-10)

| AH3880 Product Specifications | Value |
|---|---|
| Crypto Algorithm | SHA-256 |
| Hashing Performance | Range: 0-600TH/s — Eco: 14.3J/TH at 400TH/s — Mid: 15.8J/TH at 500TH/s — Turbo: 17.5J/TH at 600 TH/s (estimates, ±8%, using PG25 liquid coolant) |
| Cooling Mechanism | Hydro |
| Coolant per miner | Approximately 1L |
| Coolant Temperature Range | 10°C to 60°C |
| Coolant Flow Rate | ~5L/min to 20L/min |
| Power | 10000 Watts (PSU spec) |
| AC Input (three phase) | 380-480V nominal, 320-528V min/max |
| AC Input Current | 20 Amps per phase |
| AC Input Frequency | 48-62Hz |
| Power Cable | 1 x SA2-30 to SA2-30 |
| Connectivity | RJ45 Ethernet 10/100/1000 |
| Dimensions (L/W/H) | 665 x 485.65 x 88 mm (26.2 x 19.1 x 3.5 in) |
| Weight | 64 lbs / 29 kg |
| Storage Temperature | -40 to 158°F (-40 to 70°C) |
| Operation Humidity | 20-80% RH non-condensing |
| Operation Altitude | up to 3,000M (9,840ft) |

Products-page deltas (same capture): Output 100 - 600 TH/sec; Efficiency Normal 14.3 J/TH, Turbo 17.5 J/TH; Operating Range 0 to 60º C.

March-2025 Business Wire extras (recorded verbatim from that release, cited for context): "Flexible Power Management allows maximum power usage of up to 10KW", "with ability to scale down to 1,800 watts", plus an "Integrated OLED Screen" and leak detection ("Advanced Liquid Detection quickly identifies leaks").

## Cross-check

**AMV-only** (ASIC Miner Value has the SKU; MiningNow has none).

| AMV row (as listed) | Release | Hashrate | Power | Algorithm | Profit (as shown) |
|---|---|---|---|---|---|
| Auradine Teraflux AH3880 (600 Th) | Mar 2025 | 600 Th/s | 10740 W | SHA-256 | -$25.78 /day |

- AMV's 10740 W exceeds the datasheet's 10000-Watts PSU figure; the datasheet footnote concedes "system maximum may be slightly lower" — direction here is the opposite, so the discrepancy is unexplained. AMV profit cells show electricity cost only at its standard $0.10/kWh (top-coin column empty as served); values volatile As-Of 2026-10-10.
- **MiningNow: zero Auradine listings** as of 2026-10-10 — no cross-check possible there.

> **Status: Disputed** — normal-mode efficiency
> The datasheet and products page say 14.3J/TH Eco / Normal 14.3 J/TH; the March 2025 Business Wire release said "as low as 14.5J/TH in normal mode"; and the 2025-11-12 Gen-3 PR table shows hydro at 11 (normal) / 9.8 (eco). Best assessment as of 2026-10-10: the PR numbers describe the third-generation systems, not the AH3880 data-sheet hardware; treat 14.3 J/TH (Eco, PG25 coolant, ±8%) as the AH3880 datasheet value and 14.5 J/TH as the launch-release figure.

## Heat-reuse notes

- **Commercial heater-class hardware.** 600 TH/s at 10000 Watts on a three-phase 380-480V input is commercial/facility-class heat (≈ a small commercial boiler's worth of demand per miner) — and with the enterprise posture ("Minimum Order 500 units", no public prices) this is not a hobbyist unit. Community single-phase hydro workarounds live in [Hydronic Heat Reuse](hydronic-heat-reuse.md) and [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md) — note the AH3880 needs 3-phase 380-480V, so it does not solve the single-phase hydro gap either.
- **Hydro loop per miner**: Approximately 1L of coolant, 10°C to 60°C coolant temperature, ~5L/min to 20L/min flow, PG25-qualified estimates — direct hydronic-plumbing territory (chemistry and HX isolation guidance: [Hydronic Heat Reuse](hydronic-heat-reuse.md), [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md)).
- **Power scaling for heater duty**: the same EnergyTune/QSE demand-response stack as the AT2880, with the Business Wire release claiming scale-down "to 1,800 watts" and an OLED screen plus "Advanced Liquid Detection" for leaks — leak detection matters in any occupied-space hydro loop.
- 2U-style rack format and 10000-Watts-class draw make it a container/rack-heating building block (Auradine's own containers house 100-200 miners at 1 or 2MW).

## See Also

- [Auradine Teraflux Overview](teraflux-overview.md) — rebrand, fleet posture, Gen-3, FluxOS/FluxVision
- [Hydronic Heat Reuse](hydronic-heat-reuse.md)
- [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md)
- [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md)
