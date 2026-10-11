# Farm Management Overview

> Sources: Foreman/OBM marketing + docs (`foreman-docs`), Foreman API knowledge base (`foreman-api`), Braiins Manager (`braiins-manager`), Luxor Commander (`luxor-commander`), Awesome Miner (`awesome-miner`), SimpleMining OS (`simplemining`), NiceHash (`nicehash`) — captured 2026-10-10
> Raw: [Foreman product (obm.io/miners)](../../raw/mining-software/foreman/2026-10-10_foreman-docs_obm-io-miners-product-overview.md); [Foreman features](../../raw/mining-software/foreman/2026-10-10_foreman-docs_obm-io-features.md); [Foreman pricing](../../raw/mining-software/foreman/2026-10-10_foreman-docs_obm-io-pricing.md); [Foreman API quick guide](../../raw/mining-software/foreman/2026-10-10_foreman-api_quick-guide-foreman-api.md); [Foreman OpenAPI surface](../../raw/mining-software/foreman/2026-10-10_foreman-api_swaggerhub-openapi-endpoint-surface.md); [Foreman client-ID article](../../raw/mining-software/foreman/2026-10-10_foreman-api_how-to-find-the-client-id.md); [Foreman/Luxor report](../../raw/mining-software/foreman/_REPORT-foreman-luxor.md); [Commander landing](../../raw/mining-software/luxor-commander/2026-10-10_luxor-tech-commander-landing.md); [Commander getting started](../../raw/mining-software/luxor-commander/2026-10-10_docs-luxor_commander-getting-started.md); [Commander pricing](../../raw/mining-software/luxor-commander/2026-10-10_docs-luxor_commander-pricing.md); [Commander agents](../../raw/mining-software/luxor-commander/2026-10-10_docs-luxor_commander-agents.md); [Braiins Manager landing](../../raw/mining-software/braiins-manager/2026-10-10-braiins-com-manager-landing.md); [Braiins Manager overview](../../raw/mining-software/braiins-manager/2026-10-10-academy-braiins-manager-overview.md); [Braiins Manager components](../../raw/mining-software/braiins-manager/2026-10-10-academy-braiins-manager-using-components.md); [Braiins/vendors report](../../raw/mining-software/braiins-manager/_REPORT-basn.md); [Awesome Miner home](../../raw/mining-software/awesome-miner/2026-10-10-awesomeminer-home.md); [Awesome Miner pricing](../../raw/mining-software/awesome-miner/2026-10-10-awesomeminer-signup-pricing.md); [SimpleMining home](../../raw/mining-software/simplemining/2026-10-10-simplemining-home.md); [SimpleMining features](../../raw/mining-software/simplemining/2026-10-10-simplemining-features.md); [NiceHash Miner README](../../raw/mining-software/nicehash/2026-10-10-github-nicehashminer-readme.md); [NHOS README](../../raw/mining-software/nicehash/2026-10-10-github-nhos-readme.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

Farm management software is the layer between miner firmware and the pool: discovery, fleet-wide pool changes, power control, alerting, and — increasingly — power-price-responsive automation. This page maps the six products in Tyler's approved set (Foreman/OBM, Braiins Manager, Luxor Commander, Awesome Miner, SimpleMining, NiceHash) against each other and against the open-source fleet layer ([asic-rs](asic-rs.md), Hashscope). The firmware-side mechanics each product drives are in the firmware articles: [Braiins OS](../firmware/braiins-os.md), [LuxOS](../firmware/luxos.md), [Vnish → HashCore](../firmware/vnish-hashcore.md).

## The landscape (As-Of 2026-10-10)

| Product | Target | Scale claim | Pricing | Agent/OS | API |
|---|---|---|---|---|---|
| Foreman (OBM) | Industrial ASIC farms | "trusted by more than 10,000 customers" | "$0.60 Per Miner / Month, Billed Monthly" (Essential) + Enterprise custom | Pickaxe (on-prem agent) | REST v2, **92 paths**, `Authorization: Token` |
| Braiins Manager | ASIC fleets, mid-size | "Reliably managing 1+ GW across mining sites worldwide" | free plan + paid premium support | Agent on "Ubuntu and Debian Linux servers, as well as Windows 11 servers" | public-api in Academy docs |
| Luxor Commander | Industrial, LuxOS-coupled | fleet monitoring + "One-Click Bulk Actions" | Lite free; Pro "$100 / MW / Month" or "+0.25% Hashrate Adder" | Commander Agent, Linux or "Windows Server 2019+"; "macOS Not Supported" | REST `/v2/commander/*` |
| Awesome Miner | Windows users, GPU+ASIC | "Scalable up to 200,000 ASIC miners and 25,000 GPU/CPU miners" | "$2/miner/mo", volume discounts | Windows app + Remote Agent | API documentation link |
| SimpleMining | GPU rigs | GPU-only Linux distro, cloud dashboard | "| 1 - 49 rigs | 2.0$ |", "FREE with one rig for 30 days" | SMOS images (i073/i088/i090) | web dashboard |
| NiceHash Miner | Home/Windows rigs | profitability auto-switching | free software | Windows 10 x64 | — |

## Foreman (OBM)

Foreman is OBM's flagship: "Foreman is OBM's flagship Bitcoin mining management software that enables miners to remotely manage their sites from anywhere with automation, operational insights, and precision controls to optimize efficiency and profitability." Essentials cover monitoring, miner management with a Site Map, issue alerting to "Discord, Telegram, Google Chat, and Slack", infrastructure integration ("Smart PDUs & Phase Balancing — Monitor each miner's consumption directly from the PDU port and perform hard reboots through your dashboard"), and rule-based Power Controls ("time of day, miner temperatures, or profitability").

The premium layer is where the energy-market machinery lives — Price Response Plus with three strategies ("Basic — Delivers reliable on/off control when strike price thresholds are met", "Power Mode — Adds discrete states to underclock or overclock", "Wattage Target — Enables granular, wattage-level precision"), "Aggregators such as Voltus, CPower, and GridBeyond" partner integrations, Adaptive Dispatches ("Execution Sequences – Mine only your most profitable miners when you curtail part of your load"), plus Assets & Inventory, Foreman Intelligence, and "SOC 1 and SOC 2 reports, and maintains ISO 27001 certification".

Pricing: "Essential Pricing $0.60 Per Miner / Month, Billed Monthly, Free 30-day trial", Enterprise custom, premium modules as add-ons.

**API** (`foreman-api`): base `https://api.foreman.mn/api/v2/`, API-key auth, 92 OpenAPI paths — fleet reads (`GET /clients/{clientId}/miners/summary`), actions (`POST /actions/reboot/{minerId}`, `POST /actions/power-mode/{minerId}`, `POST /actions/change-pools/{minerId}` + `/bulk/{clientId}`), and the utility-facing surface: `POST /curtailment/{clientId}/once` — "This is intended to be the mechanism to connect the system to a utility signal" — plus `/dispatches/{clientId}` ("a paid feature disabled by default") and Voltus/CPower/HiveOS broker endpoints. Pagination caps at `per_page` 100; 429 → exponential backoff. Note: support.foreman.mn HTML is Cloudflare-403 to curl; the Zendesk JSON API (206 articles) is fully open — that's the capture route.

## Braiins Manager

Alive and standalone (not folded into Braiins OS; formerly Krater — a testimonial on the landing reads "I've been using Braiins Manager (formerly Krater) since its inception"). The Academy docs tree is ~36 pages (public-api, agent, controlflow, curtailment). Positioning: "Easily manage thousands of devices", "Reliably managing 1+ GW across mining sites worldwide". Batch operations: "Manage multiple miners on the [Workers page], allowing actions like restarting or changing pool settings". Price Adapt handles curtailment/energy response; the Agent runs on "Ubuntu and Debian Linux servers, as well as Windows 11 servers". Free plan exists; monetization is premium support tiers.

## Luxor Commander

"Luxor Commander brings real-time miner monitoring software, bulk remote commands, and automated profitability optimization together with your pool, firmware, and energy tools — all in one platform." Works with "miners running LuxOS, stock Bitmain, and MicroBT firmware" (agent has "protocol handlers for both Bitmain (Antminer), MicroBT (Whatsminer) and Canaan (Avalon)"); the deep features — "Intelligent Miner profile optimization and ATM configuration" — are LuxOS-specific (see [LuxOS](../firmware/luxos.md)).

Plans: **Commander Lite (Free)** covers "dashboard and miners table, installing and updating LuxOS, and bulk actions to change pool, power and temperature settings" — and, notably, uninstalling third-party firmware "such as Braiins OS or Vnish". **Commander Pro** adds Reports, Automation Rules, Sitemap, Inventory, Intelligent Miner, Hashrate Routing ("site-level proxy... automatic failover"), and ancillary-services participation, paid either "**$100 / MW / Month**" via Stripe or as a "**+0.25% Hashrate Adder**" on the Luxor pool rate. The agent is Linux/Windows-only ("macOS Not Supported"), outbound TCP 9001 to `agent-gateway.commander.luxor.tech`; offline, mining continues but "Automation Rules will not fire".

The grid-interactive layer is the differentiator: Intelligent Miner "ingests spot hashprice, live power prices, and your energy-contract terms" every five minutes and claims "+8–14% more profit than on/off curtailment"; Demand Response programs (e.g. "ERCOT's ECRS") at "$40–100K+ grid revenue per MW / yr"; 4CP optimizer "~$40–67K transmission charges avoided per MW / yr". These bracket the same numbers Giga Energy publishes from the container side — see [Public Miner Economics](../industry/public-miner-economics.md).

## Awesome Miner

Windows-centric central management: "Scalable up to 200,000 ASIC miners and 25,000 GPU/CPU miners", "A total of more than 200 ASIC miner models are supported", "trigger conditions and more than 40 different actions are available", GPU rigs via Remote Agent on Linux. Pricing (on /signup, not /pricing): "$2/miner/mo" base with volume discounts (25+ 10% → 5000+ 75%), Yearly $36. The Interesting coupling: Awesome Miner's "Antminer firmware" edition "with a 2.8% mining fee doesn't consume any license in Awesome Miner" — the same 2.8% fee LuxOS charges (see [LuxOS](../firmware/luxos.md)), pointing at Braiins/ Luxor-adjacent licensing economics.

## SimpleMining

GPU-farm Linux distro (SMOS): cloud dashboard, "overclock and mining groups, set tags, reboot, reload, pause or power off", "Telegram Messenger if your rig is offline". Pricing table: "| 1 - 49 rigs | 2.0$ |" per rig/month with volume tiers down to 5000+, "FREE with one rig for 30 days". Operator is SimplePod.ai. Pure GPU focus — the ASIC fleet products above don't cover this niche.

## NiceHash

www.nicehash.com is a **JS shell** to curl (every probed route returns the same ~962 B Vue `<div id="app">` — park recorded; the sitemap lists 2,070 URLs, all client-rendered). Captured instead from the official GitHub READMEs: NiceHash Miner (Windows 10 x64) exposes profitability-switching configuration — `MinimumProfit`, `SwitchProfitabilityThreshold`, `KwhPrice`, `RigGroup` — the home-scale ancestor of the power-price-responsive logic the industrial products sell; NHOS is a thin Linux rig OS (flash instructions only).

## Cross-cutting themes

- **Power-price responsiveness is now table stakes**: Foreman Price Response Plus, Braiins Price Adapt, Commander Intelligent Miner, NiceHash `SwitchProfitabilityThreshold` — the same control loop (price in, power state out) at scales from one rig to a gigawatt. The filings show why: energy was 54.9% of MARA's owned mining revenue in Q2'26 ([Public Miner Economics](../industry/public-miner-economics.md)).
- **The agent pattern**: every serious product ships an on-prem agent that scans the LAN and phones home — Foreman's Pickaxe, Braiins Manager Agent, Commander Agent (outbound-only TCP 9001). Discovery + telemetry + command relay is the architecture; the vendor cloud is just the control plane.
- **GPU vs ASIC lineages**: Awesome Miner and SimpleMining grew up GPU and bolted on ASIC management; Foreman, Braiins Manager and Commander are ASIC-first. Home miners straddle both ([Heater Firmware & Power Control](../firmware/heater-firmware-and-power-control.md)).
- **Firmware coupling as strategy**: Commander's premium features require LuxOS; Foreman sells a KB guide to "Install and Manage LuxOS with Foreman"; Awesome Miner bundles its own Antminer firmware edition. Firmware and fleet software are converging on the same 2-2.8% fee economics ([Mining Firmware Security](../industry/mining-firmware-security.md)).

## Where asic-rs fits

The open-source fleet layer under all of this is [asic-rs and the Fleet-Tooling Stack](asic-rs.md): one Rust abstraction over the same firmware dialects these products deploy (Braiins OS, Vnish/HashCore, LuxOS, Marathon FW, stock Antminer/Whatsminer/Avalon), with Python/JS/Go bindings and Hashscope on top. Where Foreman's API gives 92 vendor-hosted paths and Commander's agent gives protocol handlers per vendor, asic-rs gives the same reach without the SaaS — the home-lab and research counterpart to everything above. Hashscope ([docs](https://github.com/256foundation)) builds the fleet UI on it.

## Disputed / caveats

- **NiceHash**: no first-party marketing copy captured — www.nicehash.com serves a JS shell; READMEs are the grounding. A rendered-browser pass is a Phase B candidate.
- **Awesome Miner pricing** lives on /signup (no /pricing page); tiers may change without notice.
- **Commander** FAQ answers on the landing are collapsed accordions (questions only in server HTML); plan details above come from the docs.
- **support.foreman.mn** HTML is Cloudflare-challenged; captures use the open Zendesk JSON API.

## See Also

- [asic-rs and the Fleet-Tooling Stack](asic-rs.md) — the open-source layer under all of this
- [Hashscope](hashscope.md) — 256F fleet tooling
- [LuxOS](../firmware/luxos.md) / [Braiins OS](../firmware/braiins-os.md) / [Vnish → HashCore](../firmware/vnish-hashcore.md) — the firmware these managers drive
- [Home Assistant Heater Control](home-assistant-heater-control.md) — the home-scale control stack
- [Public Miner Economics](../industry/public-miner-economics.md) — what industrial fleet software is worth at 1+ GW
- [Mining Firmware Security](../industry/mining-firmware-security.md) — the phone-home surface these agents join
