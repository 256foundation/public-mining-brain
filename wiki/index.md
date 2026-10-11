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
| [ASIC Thermals and Heat Reuse](hardware/asic-thermals-and-heat-reuse.md) | What mining silicon and hashboards tolerate: chip limits, secondary-component blockers, cooling, TIMs, immersion. | 2026-10-09 |
| [Ember One & the BZM2 Hardware Stack](hardware/ember-one-bzm2.md) | The 256F open hardware program: emberOne series, Intel BZM2 donation, BitaxeBIRDS, aditBoard, Libre Board. | 2026-10-10 |

## firmware

Stock, open-source, and commercial ASIC firmware; feature matrices; tuning.

| Article | Summary | Updated |
|---------|---------|---------|
| [Mujina](firmware/mujina.md) | 256F's open Rust mining firmware: architecture, ports (Gamma, S19j Pro, Amlogic, BCB100, Zynq, Canaan), internals. | 2026-10-10 |

## mining-software

Farm management, monitoring, node tooling, marketplaces.

| Article | Summary | Updated |
|---------|---------|---------|
| [asic-rs and the Fleet-Tooling Stack](mining-software/asic-rs.md) | pyasic → asic-rs succession, Home Assistant integrations, gateway tooling, proto-fleet adoption. | 2026-10-10 |

## pools

Per-pool pages, payout schemes, fees, decentralization.

| Article | Summary | Updated |
|---------|---------|---------|
| [Hydrapool](pools/hydrapool.md) | 256F's Rust stratum server: direct-coinbase payouts, solo/PPLNS semantics, auditable shares, ops quirks. | 2026-10-10 |
| [Pool Payout Schemes](pools/pool-payout-schemes.md) | FPPS vs PPLNS vs solo, SPPLNS proposal, pool centralization taxonomy, censorship vs 51% debate. | 2026-10-08 |

## protocols

Stratum V1/V2, getblocktemplate, job negotiation, template distribution.

| Article | Summary | Updated |
|---------|---------|---------|
| [Decentralized Pool Designs](protocols/decentralized-pool-designs.md) | DATUM, custody-free payouts, GridPool heaviest-Winners-List, P2Poolv2, pool-sig, midstate archaeology. | 2026-10-10 |

## economics

Profitability math, hashprice, difficulty, electricity, curtailment, heat reuse.

| Article | Summary | Updated |
|---------|---------|---------|
| [Open Mining Economics](economics/open-mining-economics.md) | $8-$12/TH vs Bitmain's scale, the mission-over-price debate, heat-as-service, sell-vs-hodl math. | 2026-10-10 |

## history

Mining eras, key events, companies, geographic shifts.

| Article | Summary | Updated |
|---------|---------|---------|
| [256F Community Timeline](history/256f-community-timeline.md) | Message-anchored milestones 2024→2026: incorporation, grants, hardware, Telehash, forum migration. | 2026-10-09 |

## industry

Farms, public miners, hosting, colocation, energy interplay.

| Article | Summary | Updated |
|---------|---------|---------|
| [Repair, Supply & Vendors](industry/repair-supply-and-vendors.md) | Repair grey market (ZeusBTC), schematics peer review, JLCPCB economics, GekkoScience dispute, hosting, Canaan. | 2026-10-10 |
| [Mining Policy and Legal](industry/mining-policy-and-legal.md) | Samourai prosecution and money-transmitter theory, operation Red Sunset, Bitaxe USPTO trademark fight, tariffs/customs, UL-FCC-CE, net metering. | 2026-10-10 |

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
| [Hashrate Heating Economics](economics/hashrate-heating-economics.md) | When hash heating pays vs gas, propane, oil, resistive and heat pumps: break-even/payback math, sizing, dated prices, tax. | 2026-10-10 |
| [Hashrate Heatpunks Community Timeline](history/heatpunks-community-timeline.md) | Dated Heatpunks milestones 2024-08 → 2026-10: heatpunks.org, Manifesto, Undermine/2026 summits, forum launch + backfilled threads (builds, TIDES-vs-FPPS experiment, The Space demo), Telehash, HA office hours. | 2026-10-10 |
| [Hashrate Heating Products & Installs](industry/hashrate-heating-products-and-installs.md) | Heating vendors (Heat Core, RY3T, Superheat, Softwarm, Ecobit…), commercial installs, UL/permits/insurance, barriers, scams. | 2026-10-09 |
| [Bitaxe Troubleshooting](getting-started/bitaxe-troubleshooting.md) | Symptom → cause → fix for Bitaxe: power faults, 0 GH/s, overheat, Wi-Fi/router, failed OTA, dead-subscription "hashing for nothing", rejects, duplicate shares, Flatline of Death, 2.14.0-era error-rate/upgrade reports (OSMU forum). | 2026-10-10 |
| [Bitaxe Models & Open-Source Miner Family](hardware/bitaxe-models.md) | Bitaxe lineage BM1387 → Max → Ultra → Hex → Supra → Gamma → GT/Naja: specs, board numbers, BM1370 primer, ESP32 module, derivatives, clones, legitlist; field reports from the OSMU forum. | 2026-10-10 |
| [Bitaxe Board Design, Power & Errata](hardware/bitaxe-board-design-and-errata.md) | Bitaxe power design (TPS40305 → TPS546, series domains, PMBus faults, 5V window), EMC2101 thermals, per-board errata, DFM, reflow, BAP. | 2026-10-10 |
| [Bitmain BM13xx ASIC Reference](hardware/bitmain-asic-reference.md) | BM1387–BM1370 (+BM1340/72/73) specs with disputed figures, pinouts, UART frames, CRC5, registers, PLL, nonce math, temp sensing. | 2026-10-09 |
| [Libre Board & Mining Control Boards](hardware/libre-board-and-control-boards.md) | Libre Board (CM5, CERN-OHL-S, errata) vs Braiins BCB100 and stock Antminer Amlogic/Zynq boards; emberone-usbserial firmware. | 2026-10-10 |
| [OSMU Open Miners](hardware/osmu-open-miners.md) | Open miners beside the Bitaxe: NerdMiner ESP32 line and display hybrids (NerdNOS, NerdAxe, NerdQAxe+/++), PiAxe/QAxe build paths, BitForge Nano, WarpAxe, firmware forks, OSMU-forum pool/tool ecosystem (dvb-WarpPool, Pogolo, BTC PoW Lab, Bitaxe Monitor). | 2026-10-10 |
| [ESP-Miner / AxeOS](firmware/esp-miner-axeos.md) | Bitaxe's open firmware: architecture, flashing/recovery, AxeOS API, mDNS, security posture, stratum/SV2 behavior, releases 1.0 → 2.15.3; OSMU-forum feature requests and independent API reimplementations. | 2026-10-10 |
| [Community Channels & X Presence](getting-started/community-channels-and-x.md) | Where the community gathers: Telegram supergroups, Discourse forums, Nostr, OSMU Discord, and the X accounts (@osmu_global, @heatpunks, @Public_Pool_BTC) — measured sizes and activity, censused 2026-10-07/10. | 2026-10-10 |
| [HashScope](mining-software/hashscope.md) | 256F's Stratum man-in-the-middle proxy: architecture, quick start, API, Nostr agent fleet for watching pool behavior. | 2026-10-09 |
| [Public Pool](pools/public-pool.md) | Open-source solo pool (hosted or self-hosted): stratum server + GUI, operation, SV2 support, block record, Bitaxe/OSMU ties. | 2026-10-09 |
| [Pool Centralization & FPPS](pools/pool-centralization-and-fpps.md) | Who controls templates and rewards: concentration data, proxy-pool networks, FPPS custody critique, pool incidents, transparency tools. | 2026-10-10 |
| [Stratum V1 & V2 in Practice](protocols/stratum-in-practice.md) | Stratum V1 as implemented (message order, BIP 310/320 rolling, extranonce, difficulty, rejects, word-swap) plus SV2 adoption and disputes. | 2026-10-10 |
| [RHAP (Raw Hardware Access Protocol)](protocols/rhap.md) | Host-driven hashboard access over USB for Mujina: RHAP-D device role, packet format, commands, bitaxe-raw → rhapd history. | 2026-10-10 |
| [The 256 Foundation](history/256-foundation-organization.md) | 501(c)(3) structure, mission, programs (grants, Red Team, SV2 WG), grants given and received, Telehash fundraisers #1–#4. | 2026-10-10 |
| [Solo Blocks Found by Open-Source & Home Miners](history/open-source-solo-blocks.md) | On-chain-verified table of solo blocks won by Bitaxes and home miners since July 2024, odds framing, disputed attributions. | 2026-10-09 |
| [POD256 Podcast](history/pod256-podcast.md) | The 256 Foundation's weekly show (001–127, 2022-12 → 2026-09): format, hosts, episode/guest index, recurring themes. | 2026-10-10 |
| [Mining Firmware Security](industry/mining-firmware-security.md) | 256 Red Team audits, closed-firmware incidents (Antbleed, pool blocking, OEM SSH), vendors going open source, operator hardening. | 2026-10-10 |
| [Network State 2022–2026](industry/network-state-2022-2026.md) | Dated hashrate, difficulty, hashprice, fee and ASIC-price snapshots plus industry, policy and conference events, as reported. | 2026-10-10 |
| [Mining Nodes & Block Templates](protocols/mining-nodes-and-templates.md) | Running your own node for templates: pruned nodes (disputed), AssumeUTXO, Floresta/Utreexo, Core v30 IPC, DATUM blocknotify. | 2026-10-10 |
