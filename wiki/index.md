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
| [Bitmain ASIC reference](hardware/bitmain-asic-reference.md) | Antminer lineage, silicon frontier, current-gen lineup (S23 confirmation), desoldering economy, open questions. | 2026-10-10 |
| [Antminer S23 XP Hyd.](hardware/antminer-s23-xp-hyd.md) | 600 TH/s, 8.9 J/T wall @35℃, $15,300, shipping Nov 2026 — the live efficiency flagship; price Disputed. | 2026-10-10 |
| [Antminer S23e U2H](hardware/antminer-s23e-u2h.md) | 2U rack hydro, 865 TH/s / 10 J/T, feeds ANTSPACE HW7 (242 slots); naming + release-date Disputed. | 2026-10-10 |
| [Antminer S21 XP+ Hyd](hardware/antminer-s21-xp-plus-hyd.md) | 480 T / 5280 W / 11 J/T live sheet; DBs still carry older 500 Th / 5500 W rows — Disputed. | 2026-10-10 |
| [Antminer S21 XP Hyd](hardware/antminer-s21-xp-hyd.md) | 473 TH/s / 5676 W / 12 J/T @35℃, $8,041 on sale; specs agree, price Disputed. | 2026-10-10 |
| [Antminer S21 XP](hardware/antminer-s21-xp.md) | Air flagship 270 TH/s / 13.5 J/T @25℃, 76 dBA, single-phase; @25℃ vs @35℃ band convention. | 2026-10-10 |
| [Whatsminer overview](hardware/whatsminer-overview.md) | MicroBT lineup ladder M70S→M73, 17-row catalog, image-only-PDF gap, M7B/M6B paper launch, family Disputed table. | 2026-10-10 |
| [Whatsminer M66S](hardware/whatsminer-m66s.md) | 270–298 T ±10%, 18.5 J/T; AMV 298 vs MN 310 TH/s Disputed with $/kWh caveat; heater-fit immersion. | 2026-10-10 |
| [Whatsminer M66S+](hardware/whatsminer-m66s-plus.md) | 280–318 T, 17 J/T manual-only SKU (image-only performance gap); release-month dispute. | 2026-10-10 |
| [Whatsminer M63S+](hardware/whatsminer-m63s-plus.md) | Hydro 2U, 390–450 T, ≥10 L/min, 70 °C outlet; AMV/MN Disputed inside maker ±10% band. | 2026-10-10 |
| [Whatsminer M64](hardware/whatsminer-m64.md) | Compact hydro heater-fit (371×290×109 mm, single-phase, 80 °C outlet); 5 kW vs ~4 kW field record Disputed. | 2026-10-10 |
| [Whatsminer M65S](hardware/whatsminer-m65s.md) | 2U rack hydro 370–400 T / 18.5 J/T; absent from both spec DBs (omission Disputed). | 2026-10-10 |
| [Whatsminer M70S](hardware/whatsminer-m70s.md) | Shop card 248TH @13.5 J/TH; DBs agree on 226 @ 3140 W — bin-mismatch Disputed. | 2026-10-10 |
| [Whatsminer M73](hardware/whatsminer-m73.md) | 512TH @14.5 J/TH, 7424 W, 3-phase 10 kW input; DBs 470 @ 7200 W — Disputed. | 2026-10-10 |
| [Avalon overview](hardware/avalon-overview.md) | Canaan lineup ladder A16XP→A15→A14, Wayback park note (live 403), lab-results disclaimer, A4 attribution confusion. | 2026-10-10 |
| [Avalon A16XP](hardware/avalon-a16xp.md) | 300 TH/s / 12.8 J/TH flagship launched Dubai Oct 2025; release-date Disputed; no hydro variant. | 2026-10-10 |
| [Avalon A15Pro](hardware/avalon-a15pro.md) | 221T / 16.8 J/TH; 5,000+ sold via Luxor financing, 6,840 to Cipher — IR-corroborated field scale. | 2026-10-10 |
| [Avalon A15Pro+ 240T](hardware/avalon-a15pro-plus.md) | Higher-bin refresh 240T / 3720 W / 15.5 J/TH ($3,600); AMV doesn't carry the + SKU. | 2026-10-10 |
| [Avalon A15XP](hardware/avalon-a15xp.md) | 209T / 3667 W / 17.8 J/TH; 209-vs-206 dual-bin release-date Disputed. | 2026-10-10 |
| [Avalon A15](hardware/avalon-a15.md) | 194T / 18.8 J/TH entry card; specs agree everywhere; bulk-vs-street price spread recorded. | 2026-10-10 |
| [Avalon A1566HA-500T](hardware/avalon-a1566ha-500t.md) | A15-gen hydro heater-class: 500T / 8064 W / 16.8 J/TH 2U loop; bin-rotation + price Disputed. | 2026-10-10 |
| [Avalon A14 series](hardware/avalon-a14-series.md) | Prior-gen 1446/1466 air cards + immersion claims; PSU-vs-wall-power Disputed; Panther Creek fleet. | 2026-10-10 |
| [SEALMINER overview](hardware/sealminer-overview.md) | Bitdeer lineup A2→A4, SEAL01→04 chip ladder (18.1→6-7 J/TH target), DL1 Scrypt, DesiWeMiner fold-in pending. | 2026-10-10 |
| [SEALMINER A2](hardware/sealminer-a2.md) | $2,892.8 sold-out 226T / 16.5 J/T; release-date + roadmap-vs-page efficiency Disputed. | 2026-10-10 |
| [SEALMINER A2 Pro Air](hardware/sealminer-a2-pro-air.md) | 260T / 14.9 J/T, $3,380→$3,067 coupon history; vendor-vs-DBs Disputed. | 2026-10-10 |
| [SEALMINER A2 Pro Hydro](hardware/sealminer-a2-pro-hydro.md) | 500T / 7450 W 2U hydro, inlet 55→60 °C, outlet to 70 °C — heater-class; price spread dated. | 2026-10-10 |
| [SEALMINER A3](hardware/sealminer-a3.md) | 240–690 TH/s series (no product page — flagged); three-price A3 Pro Hydro Disputed. | 2026-10-10 |
| [SEALMINER A4 Ultra](hardware/sealminer-a4-ultra.md) | Roadmap flagship 886T / 9.45 J/T "Stay tuned", Q3 2026 mass production; unshipped-SKU price Disputed. | 2026-10-10 |
| [Teraflux overview](hardware/teraflux-overview.md) | Auradine (now velaura.ai): enterprise fleet posture, 500-unit minimum, Gen-3 9.8 J/TH, FluxOS demand-response. | 2026-10-10 |
| [Auradine AT2880](hardware/auradine-at2880.md) | Air flagship 0–270 TH/s, 16–18 J/TH modes, 5000 W; AMV-only cross-check. | 2026-10-10 |
| [Auradine AH3880](hardware/auradine-ah3880.md) | Hydro 600 TH/s, 10 kW 3-phase — commercial heater-class; efficiency Disputed across PRs. | 2026-10-10 |
| [Auradine AI3680](hardware/auradine-ai3680.md) | Single-phase immersion 365 TH/s / 7500 W; fluid-locked warranty flagged as deployment risk. | 2026-10-10 |

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
| [Pool Payout Schemes](pools/pool-payout-schemes.md) | FPPS vs PPLNS vs solo, SPPLNS proposal, pool centralization taxonomy, censorship vs 51% debate. | 2026-10-10 |
| [Foundry USA Pool](pools/foundry.md) | #1 pool: FPPS-only daily to whitelisted KYC addresses; quarterly fee tiers, no % published; SOC-audited custody. | 2026-10-10 |
| [AntPool](pools/antpool.md) | Bitmain's pool: selectable PPS/PPLNS/FPPS; fee table image-only; sanctions gate; default 0.005 BTC daily payouts. | 2026-10-10 |
| [F2Pool](pools/f2pool.md) | FPPS 4% / PPLNS 2% published per-coin; selectable thresholds; covers network fees; rank 3. | 2026-10-10 |
| [ViaBTC](pools/viabtc.md) | PPS+ itemized (4% block + 2% tx-fee) or PPLNS 2%; hourly settlement; wallet/trading/loans ecosystem. | 2026-10-10 |
| [OCEAN](pools/ocean.md) | TIDES-only, non-custodial coinbase-direct, "No KYC, only payout address"; 2%/1%-DATUM in binding ToS; DATUM origin. | 2026-10-10 |
| [SECPOOL](pools/secpool.md) | Top-8 pool with unpublished rates, unnamed operator, closed help center; multi-mode bundle disclosures. | 2026-10-10 |
| [Luxor Pool](pools/luxor-pool.md) | FPPS formula published (144-block lookback, p5-p95 trim); fee as "discount to spot", no %; US, SOC 2. | 2026-10-10 |
| [MARA Pool](pools/mara-pool.md) | Self-owned public-miner pool, "no fees to external operators" — while its public site is dead (As-Of 2026-10-10). | 2026-10-10 |
| [SpiderPool](pools/spiderpool.md) | PPLNS 1% / FPPS 4% published; client-rendered site; no custody/SV2 statements; rank 5. | 2026-10-10 |
| [Braiins Pool](pools/braiins-pool.md) | 2.5% FPPS (0% via Braiins OS), Lightning payouts, ex-Slush Pool since 2010, "Secure & Non-KYC", SV2 port 3336. | 2026-10-10 |

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
| [256F Community Timeline](history/256f-community-timeline.md) | Message-anchored milestones 2024→2026: incorporation, grants, hardware, Telehash, forum migration. | 2026-10-10 |

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
| [Air-Cooled Hashrate Heating](hardware/air-cooled-hashrate-heating.md) | Air-cooled ASIC space heating: HVAC return/furnace ducting, inline fans, CFM/static pressure, shrouds, quiet mods, VOCs, field data. | 2026-10-10 |
| [Heater Electrical & 120V Builds](hardware/heater-electrical-and-120v-builds.md) | Electrical rules for hashrate heaters: 80% rule, circuits/receptacles, contactors, 120V S19 builds (Loki/APW12), 208V, solar. | 2026-10-09 |
| [Hydronic Heat Reuse](hardware/hydronic-heat-reuse.md) | Water-side heat reuse: loop isolation, plate HX sizing, radiant floors, DHW, pools, dry coolers, glycol/corrosion, buffer tanks. | 2026-10-09 |
| [Immersion Heat Reuse](hardware/immersion-heat-reuse.md) | Immersion for heat: canola vs mineral vs engineered fluids, tanks, cable wicking, fan sims, Vnish limits, DIY hot-water builds. | 2026-10-09 |
| [Whatsminer M64-Family Hydro Heaters](hardware/whatsminer-m64-hydro-heaters.md) | M64/M64S/M74 hydro as heating cores: specs, coolant and fittings, power-control limits, HS05/RY3T/Aqueon, dated prices and MOQ. | 2026-10-09 |
| [Heater Firmware & Power Control](firmware/heater-firmware-and-power-control.md) | Braiins DPS vs LuxOS ATM vs Vnish vs Whatsminer modes for heaters: retune latency, temp offsets, sleep draw, drain:// fallback. | 2026-10-10 |
| [Home Assistant Heater Control](mining-software/home-assistant-heater-control.md) | Firmware → pyasic → hass-miner → Home Assistant stack: thermostats/deadband, sensors/plugs, miner APIs, outage fallbacks. | 2026-10-09 |
| [Pool Choice for Heat Miners](pools/pool-choice-for-heat-miners.md) | FPPS vs PPLNS vs OCEAN TIDES for on/off heaters (disputed; S9 side-by-side data), payout lag, DATUM setup, failover, solo. | 2026-10-10 |
| [Hashrate Heating Economics](economics/hashrate-heating-economics.md) | When hash heating pays vs gas, propane, oil, resistive and heat pumps: break-even/payback math, sizing, dated prices, tax. | 2026-10-10 |
| [Hashrate Heatpunks Community Timeline](history/heatpunks-community-timeline.md) | Dated Heatpunks milestones 2024-08 → 2026-10: heatpunks.org, Manifesto, Undermine/2026 summits, forum launch + backfilled threads (builds, TIDES-vs-FPPS experiment, The Space demo), Telehash, HA office hours. | 2026-10-10 |
| [Hashrate Heating Products & Installs](industry/hashrate-heating-products-and-installs.md) | Heating vendors (Heat Core, RY3T, Superheat, Softwarm, Ecobit…), commercial installs, UL/permits/insurance, barriers, scams. | 2026-10-10 |
| [Bitaxe Troubleshooting](getting-started/bitaxe-troubleshooting.md) | Symptom → cause → fix for Bitaxe: power faults, 0 GH/s, overheat, Wi-Fi/router, failed OTA, dead-subscription "hashing for nothing", rejects, duplicate shares, Flatline of Death, 2.14.0-era error-rate/upgrade reports (OSMU forum). | 2026-10-10 |
| [Bitaxe Models & Open-Source Miner Family](hardware/bitaxe-models.md) | Bitaxe lineage BM1387 → Max → Ultra → Hex → Supra → Gamma → GT/Naja: specs, board numbers, BM1370 primer, ESP32 module, derivatives, clones, legitlist; field reports from the OSMU forum. | 2026-10-10 |
| [Bitaxe Board Design, Power & Errata](hardware/bitaxe-board-design-and-errata.md) | Bitaxe power design (TPS40305 → TPS546, series domains, PMBus faults, 5V window), EMC2101 thermals, per-board errata, DFM, reflow, BAP. | 2026-10-10 |
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
