# Public Mining Brain — Index

One row per article, grouped by topic. Articles appear as ingestion proceeds; see `log.md` for the operation history and `sources/registry.md` for what we monitor.

## getting-started

Newcomer path: what mining is, choosing hardware, first run, joining a pool.

| Article | Summary | Updated |
|---------|---------|---------|
| [Community Workshop Wisdom](getting-started/community-workshop-wisdom.md) | Field-tested advice from the 256F community: node storage, EE books, parts ordering, WSL dev, scam defense. | 2026-10-08 |

## hardware

ASIC manufacturers and models, components, cooling, repair, DIY builds.

| Article | Summary | Updated |
|---------|---------|---------|
| [ASIC Thermals and Heat Reuse](hardware/asic-thermals-and-heat-reuse.md) | What mining silicon and hashboards tolerate: chip limits, secondary-component blockers, cooling, TIMs, immersion. | 2026-10-08 |
| [Ember One & the BZM2 Hardware Stack](hardware/ember-one-bzm2.md) | The 256F open hardware program: emberOne series, Intel BZM2 donation, BitaxeBIRDS, aditBoard, Libre Board. | 2026-10-08 |

## firmware

Stock, open-source, and commercial ASIC firmware; feature matrices; tuning.

| Article | Summary | Updated |
|---------|---------|---------|
| [Mujina](firmware/mujina.md) | 256F's open Rust mining firmware: architecture, ports (Gamma, S19j Pro, Amlogic, BCB100, Zynq, Canaan), internals. | 2026-10-08 |

## mining-software

Farm management, monitoring, node tooling, marketplaces.

| Article | Summary | Updated |
|---------|---------|---------|
| [asic-rs and the Fleet-Tooling Stack](mining-software/asic-rs.md) | pyasic → asic-rs succession, Home Assistant integrations, gateway tooling, proto-fleet adoption. | 2026-10-08 |

## pools

Per-pool pages, payout schemes, fees, decentralization.

| Article | Summary | Updated |
|---------|---------|---------|
| [Hydrapool](pools/hydrapool.md) | 256F's Rust stratum server: direct-coinbase payouts, solo/PPLNS semantics, auditable shares, ops quirks. | 2026-10-08 |
| [Pool Payout Schemes](pools/pool-payout-schemes.md) | FPPS vs PPLNS vs solo, SPPLNS proposal, pool centralization taxonomy, censorship vs 51% debate. | 2026-10-08 |

## protocols

Stratum V1/V2, getblocktemplate, job negotiation, template distribution.

| Article | Summary | Updated |
|---------|---------|---------|
| [Decentralized Pool Designs](protocols/decentralized-pool-designs.md) | DATUM, custody-free payouts, GridPool heaviest-Winners-List, P2Poolv2, pool-sig, midstate archaeology. | 2026-10-08 |

## economics

Profitability math, hashprice, difficulty, electricity, curtailment, heat reuse.

| Article | Summary | Updated |
|---------|---------|---------|
| [Open Mining Economics](economics/open-mining-economics.md) | $8-$12/TH vs Bitmain's scale, the mission-over-price debate, heat-as-service, sell-vs-hodl math. | 2026-10-08 |

## history

Mining eras, key events, companies, geographic shifts.

| Article | Summary | Updated |
|---------|---------|---------|
| [256F Community Timeline](history/256f-community-timeline.md) | Message-anchored milestones 2024→2026: incorporation, grants, hardware, Telehash, forum migration. | 2026-10-08 |

## industry

Farms, public miners, hosting, colocation, energy interplay.

| Article | Summary | Updated |
|---------|---------|---------|
| [Repair, Supply & Vendors](industry/repair-supply-and-vendors.md) | Repair grey market (ZeusBTC), schematics peer review, JLCPCB economics, GekkoScience dispute, hosting, Canaan. | 2026-10-08 |

## hashrate-market

Hashrate derivatives, indexes, forwards, hosting markets.

| Article | Summary | Updated |
|---------|---------|---------|
| [On-Demand Hashrate](hashrate-market/on-demand-hashrate.md) | Price points (Braiins Hashpower, Rigly), Telehash fuel model, heat arbitrage. | 2026-10-08 |

## meta

How the brain works, data dictionary.

| Article | Summary | Updated |
|---------|---------|---------|
| [Air-Cooled Hashrate Heating](hardware/air-cooled-hashrate-heating.md) | Air-cooled ASIC space heating: HVAC return/furnace ducting, inline fans, CFM/static pressure, shrouds, quiet mods, VOCs, field data. | 2026-10-09 |
| [Heater Electrical & 120V Builds](hardware/heater-electrical-and-120v-builds.md) | Electrical rules for hashrate heaters: 80% rule, circuits/receptacles, contactors, 120V S19 builds (Loki/APW12), 208V, solar. | 2026-10-09 |
| [Hydronic Heat Reuse](hardware/hydronic-heat-reuse.md) | Water-side heat reuse: loop isolation, plate HX sizing, radiant floors, DHW, pools, dry coolers, glycol/corrosion, buffer tanks. | 2026-10-09 |
| [Immersion Heat Reuse](hardware/immersion-heat-reuse.md) | Immersion for heat: canola vs mineral vs engineered fluids, tanks, cable wicking, fan sims, Vnish limits, DIY hot-water builds. | 2026-10-09 |
| [Whatsminer M64-Family Hydro Heaters](hardware/whatsminer-m64-hydro-heaters.md) | M64/M64S/M74 hydro as heating cores: specs, coolant and fittings, power-control limits, HS05/RY3T/Aqueon, dated prices and MOQ. | 2026-10-09 |
| [Heater Firmware & Power Control](firmware/heater-firmware-and-power-control.md) | Braiins DPS vs LuxOS ATM vs Vnish vs Whatsminer modes for heaters: retune latency, temp offsets, sleep draw, drain:// fallback. | 2026-10-09 |
| [Home Assistant Heater Control](mining-software/home-assistant-heater-control.md) | Firmware → pyasic → hass-miner → Home Assistant stack: thermostats/deadband, sensors/plugs, miner APIs, outage fallbacks. | 2026-10-09 |
| [Pool Choice for Heat Miners](pools/pool-choice-for-heat-miners.md) | FPPS vs PPLNS vs OCEAN TIDES for on/off heaters (disputed; S9 side-by-side data), payout lag, DATUM setup, failover, solo. | 2026-10-09 |
| [Hashrate Heating Economics](economics/hashrate-heating-economics.md) | When hash heating pays vs gas, propane, oil, resistive and heat pumps: break-even/payback math, sizing, dated prices, tax. | 2026-10-09 |
| [Hashrate Heatpunks Community Timeline](history/heatpunks-community-timeline.md) | Dated Heatpunks milestones 2024-08 → 2026-10: heatpunks.org, Manifesto, Undermine/2026 summits, forum, Telehash, HA office hours. | 2026-10-09 |
| [Hashrate Heating Products & Installs](industry/hashrate-heating-products-and-installs.md) | Heating vendors (Heat Core, RY3T, Superheat, Softwarm, Ecobit…), commercial installs, UL/permits/insurance, barriers, scams. | 2026-10-09 |
