# Auradine Teraflux AT2880

> Sources: official Teraflux™ AT2880 data-sheet PDF (© 2025 Auradine, Inc.; site upload path dated 2025-09, hosted on velaura.ai), captured 2026-10-10; velaura.ai products page (auradine.com 301 → velaura.ai); archived Teraflux lineup history (2023-11-14 Gen-2 PR; 2025-02-12 Bitcoin.com review); ASIC Miner Value manufacturer listing; MiningNow latest-ASIC-list sweep
> Raw: [AT2880 data sheet](../../raw/hardware/auradine/2026-10-10-auradine-teraflux-at2880-datasheet.md); [Auradine/Velaura products page](../../raw/hardware/auradine/2026-10-10-auradine-velaura-products-page.md); [Lineup history archive](../../raw/hardware/auradine/2026-10-10-auradine-teraflux-lineup-history-archive.md); [ASIC Miner Value — Auradine](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-auradine.md); [MiningNow — Auradine](../../raw/hardware/miningnow/2026-10-10-miningnow-auradine.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

The AT2880 is Auradine's air-cooled SHA-256 flagship — "an ASIC-based air-cooled Bitcoin miner" managed by per-miner web console and APIs, with FluxVision™ (purchased separately) for at-scale configuration. It is the second-generation Teraflux air miner: announced 2023-11-14 at "an output of 0 to 260 TH/s, with an optimal efficiency of 16 J/TH", shipping since July 2024, and rated 0-270 TH/s on the current data sheet (© 2025 Auradine, uploaded 2025-09). Family context, rebrand (auradine.com → velaura.ai) and fleet posture: [Auradine Teraflux Overview](teraflux-overview.md).

## Specs (datasheet, As-Of 2026-10-10)

| AT2880 Product Specifications | Value |
|---|---|
| Crypto Algorithm | SHA-256 |
| Hashing Performance | Range: 0-270 TH/s (preliminary, ±8%) — Normal: 16 J/TH at 180 TH/s — Turbo: 18 J/TH at 270 TH/s |
| Operating Temperature Range | -4 to 122°F (-20 to 50°C at sea level) |
| Cooling Mechanism | Air-cooled |
| Power Supply Option A (dual input) | 5000 Watts, 2 x C20 input; 200-240V nominal (180-264V); 0-17.6 Amp per input; 2 x C19 to C20 cables |
| Power Supply Option B (single input) | 5000 Watts, 1 x PA45 input; 208-277V nominal (180-305V); 0-30 Amp; 1 x PA45 to C20 cable |
| AC Input Frequency | 48-62 Hz |
| Connectivity | RJ45 Ethernet 10/100/1000 |
| Dimensions (L/W/H) | 395 x 202 x 290 mm (15.5 x 8 x 11.5 in) |
| Weight | 19.3 kg (42.5 lbs) |
| Storage Temperature | -40 to 158°F (-40 to 70°C) |
| Operation Humidity | 20-80% RH non-condensing |
| Operation Altitude | up to 3,000M (9,840ft) |

Footnotes (verbatim): "Note products are for indoor use only."; hashrate figures are "Preliminary estimates, ±8%"; power is "PSU spec; system maximum may be slightly lower".

Products-page deltas (same capture): Output 40 – 270 TH/sec; Efficiency Normal 16J/TH, Turbo 18 J/TH; Operating Range -20 to 50º C; page footnote: TH/s & J/TH specs +/- 8 % at 25°C ambient.

**On-device software (datasheet claims):** EnergyTune™ DVFS sets power per miner, with ECO ("least power consumed per TH or maximum efficiency") and Turbo ("highest TH/s performance") modes; AutoTemp "continuously monitors the internal junction temperature of the ASICs and reduces the TH/s" and is "enabled on every miner"; "hardware-based root of trust secure boot"; APIs integrate with Foreman or AwesomeMiner; FluxVision™ adds miner groups and Zero Touch Provisioning.

## Cross-check

**AMV-only** (ASIC Miner Value has the SKU; MiningNow has none).

| AMV row (as listed) | Release | Hashrate | Power | Algorithm | Profit (as shown) |
|---|---|---|---|---|---|
| Auradine Teraflux AT2880 (180 Th) | Nov 2024 | 180 Th/s | 4680 W | SHA-256 | -$6.91 /day |

- AMV's 180 Th/s / 4680 W matches the datasheet Normal point (16 J/TH at 180 TH/s) rather than the 5000-Watts PSU rating; the datasheet footnote concedes "system maximum may be slightly lower". AMV profit cells on manufacturer pages show electricity cost only (its standard $0.10/kWh, top-coin column empty as served); values volatile As-Of 2026-10-10.
- **MiningNow: zero Auradine listings** as of 2026-10-10 — no cross-check possible there.
- Older generations (AT1500, AT2860): **no DB cross-check exists** — AMV lists only 3 Auradine SKUs (at1500/at2860 slugs returned 404 on 2026-10-10) and MiningNow has zero Auradine rows. AT1500 third-party measured numbers (180 TH/s at 25.34 J/TH high-power; 112 TH/s at 23.1 J/TH low-power) and the AT2860 spec gap are in the [lineup history raw](../../raw/hardware/auradine/2026-10-10-auradine-teraflux-lineup-history-archive.md).

## Heat-reuse notes

- **Class.** A 5000-Watts-class air-cooled tower (395 x 202 x 290 mm, 19.3 kg) is the same room-heater scale as the used S19/Whatsminer units the community ducts — but this is enterprise hardware: "Minimum Order 500 units", no public prices, FluxVision sold separately. Not a hobbyist buy; treat as fleet/commercial sourcing (see [overview posture](teraflux-overview.md#enterprise--fleet-posture)).
- **Control is the interesting part for heaters.** EnergyTune's ECO/Turbo modes run on DVFS that retunes in half the traditional iteration time without reboots, and Power Management integrates with QSEs such as Voltus for grid demand-response curtailment — the fast, reboot-free power scaling that heater builds otherwise lack on stock firmware (community context: [Air-Cooled Hashrate Heating](air-cooled-hashrate-heating.md)).
- **AutoTemp is always on**, reducing TH/s to keep ASIC junctions in a safe zone — a built-in guard for heater duty.
- **Indoor use only** per the datasheet footnote; airflow/noise work (inline fans, returns) is the same as any air miner — see [Air-Cooled Hashrate Heating](air-cooled-hashrate-heating.md) and [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md).

## See Also

- [Auradine Teraflux Overview](teraflux-overview.md) — rebrand, fleet posture, Gen-3, FluxOS/FluxVision
- [Air-Cooled Hashrate Heating](air-cooled-hashrate-heating.md)
- [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md)
