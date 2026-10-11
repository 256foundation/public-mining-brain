# Hashrate Heating & Mining Infrastructure Companies

> Sources: 18 company official sites, captured 2026-10-11 (curl, browser UA; CleanSpark PR via reader fetch); *Bitcoin Mining Heat Reuse* (Stevens, 2025) ch. 4 case-study catalog; per-company captures linked inline in each section below
> Raw: [A15 company vetting report](../../raw/industry/_REPORT-companies-2026-10-11.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

## Overview

This is the bot-facing company tracker: every company here has a registry row (see `sources/registry.md` → Heat-Reuse & Home-Mining Companies), so the update loop re-checks them on cadence. The vetting mandate (Tyler, 2026-10-11): ingest only companies that are obviously legit with industry impact — **any hesitation means out**. Bitcoin mining spawns throwaway startups constantly; the tracker is deliberately short.

What belongs where:

- **This article** — who the tracked companies are, what they build, why they passed vetting. Anchor dates: 2026-10-11.
- [Hashrate Heating Products & Installs](hashrate-heating-products-and-installs.md) — dated field claims, installs, and performance reports from the community.
- [Repair, Supply & Vendors](repair-supply-and-vendors.md) — the repair/parts grey market and trusted-vendor mechanics.
- [Public Miner Economics](public-miner-economics.md) — the public tickers; `griid` below is the bridge case.

## The vetting bar

A company is tracked only with: (1) a live official site, and (2) independent corroboration — press, patents, funding announcements, or sustained community adoption in the 256F/Heatpunks channels. Anything unverifiable stayed out; the skip list with reasons is in the [vetting report](../../raw/industry/_REPORT-companies-2026-10-11.md). Book-profiled companies additionally carry a chapter anchor from [Successful case studies (ch. 4)](../../raw/books/braiins-heat-reuse/04-successful-case-studies.md).

## Home heating appliances

**Heatbit** — UL-certified bitcoin space heaters (Trio, Maxi line); 2026 flagship push is Bitair, a portable air purifier with a solo miner inside. Homepage: "The world's first portable air purifier with a solo Bitcoin miner." — [capture](../../raw/industry/heatbit/2026-10-11-heatbit-home.md). Still shipping (October batch, Trustpilot 4.5/350+); book profile anchors the heater line.

**Hotmine** — Ukrainian pioneer; own blog says mining-hardware developers "since 2013", store actively selling heater-miners: "Hotmine CM-1. Smart-heater $1 200 $1 000" — [capture](../../raw/industry/hotmine/2026-10-11-hotmine-home.md). CES 2026 floor coverage of its mining water heater (~$2,000).

**RY3T** — Swiss boiler-integrated miner feeding an existing home water system. "The resulting waste heat is recovered and integrated into your home's heating infrastructure." — [capture](../../raw/industry/ry3t/2026-10-11-ry3t-home.md). First single-family home heated per Switzerland Global Enterprise. Book ch. 4 profile.

**Superheat** — CES 2026 award winner; H1C is a 50-gal electric water heater with compute inside, Founding Batch preorders open. "Meet the world's first water heater that produces hot water while generating Bitcoin." — [capture](../../raw/industry/superheat/2026-10-11-superheat-home.md). Already tracked from the firmware side: clock speed driven by water temperature [#8609 · 2026-01-08 · Tyler Stevens] in [Hydronic Heat Reuse](../hardware/hydronic-heat-reuse.md).

**Hestia Heating** — Labrador City, NL; "Thermal Compute Furnaces (TCF) put high-performance computing to work as a heat source, giving businesses a low-cost, clean alternative to traditional heating." — [capture](../../raw/industry/hestia/2026-10-11-hestia-home.md). 25+ furnaces deployed, 4 US patents, ETL/Intertek listed; commercial/industrial focus. Book ch. 4 profile.

**Constellation Heating** — immersion pool boiler, 600 TH top config. "100% heat reused 3 operating modes 600 TH top hashrate" — [capture](../../raw/industry/constellation-heating/2026-10-11-constellation-home.md). Founder Nicolas Drouin (@BTC_Grid); Daniel Batten coverage. Book ch. 4 profile.

## Liquid-cooled systems & commercial heat

**Fog Hashing → Fog Computing** — Paul Jin Li's company (wrote the foreword to *Bitcoin Mining Heat Reuse*); the home-immersion C Series is the community's default tank. Site banner: "Fog Hashing is now Fog Computing. Read the announcement" — [capture](../../raw/industry/foghashing/2026-10-11-foghashing-home.md). Lines now span home kits (C Series), hydro/immersion mining (H/B Series), AI containers (FogPod), and electrical gear (transformers, UL 891 switchboards) — track under both mining and AI-infra frames.

**Hashrate House** — US-built home immersion: HashTub (miner pre-installed), Aqueon line, hydro systems. "Smart home mining systems designed to turn Bitcoin mining heat into useful energy for your home, workshop, water, pool, or thermal system." — [capture](../../raw/industry/hashrate-house/2026-10-11-hashrate-house-home.md). Heat Punk Innovation Award; Snorkel hot-tub partnership. Book ch. 4 profile.

**HeatCore** — MicroBT's authorized hydro partner (sales + repair on WhatsMiner Hydro): "As a global leader in sustainable Bitcoin mining and integrated energy solutions, HeatCore combines cutting-edge standardized manufacturing with streamlined logistics, supported by 24/7 worldwide after-sales service." — [capture](../../raw/industry/heatcore/2026-10-11-heatcore-home.md). H→E rack lines, heating/stranded-gas/desalination solutions. Book ch. 4 profile.

**MintGreen** — BC district-heat vendor; site headline: "MINTGREEN DIGITAL BOILERS RECOVER OVER 96% BITCOIN MINING ENERGY FOR LOW CARBON HEATING": "Canadian cleantech company specializing in heat recovery from Bitcoin mining. We use clean energy to mine crypto and heat communities sustainably." — [capture](../../raw/industry/mintgreen/2026-10-11-mintgreen-home.md). Lonsdale Energy contract (North Vancouver) is the reference district-heat deal.

## DIY hardware & vendors

**Pivotal Pleb Tech** — Utah; Loki Kit 120V ASIC conversion + Njord Cloudline board. "Paying WITH Bitcoin? Save 15% when you use discount code \"BTCPay\" AND use the BTCPay payment option!" — [capture](../../raw/industry/pivotal-pleb-tech/2026-10-11-pivotal-home.md). Loki Kit out of stock 2026-10-11; ecosystem ubiquity via Altair, D-Central "Loki Edition", book ch. 3.

**256 | HEAT** — Toine's shop (Wi-Fi PDUs, Zigbee sensors, shrouds, consulting): "Browse our turn-key hashrate heating systems or turn your old, unprofitable, ASIC into a programmable and profitable heater." — [capture](../../raw/industry/256heat/2026-10-11-256heat-home.md). The community-standard Wi-Fi PDU in 256F field reports.

**CryptoCloaks** — Colorado; free S9-heater STLs and testing data ("The Future of Space Heaters") — [capture](../../raw/industry/cryptocloaks/2026-10-11-cryptocloaks-home.md). The de-facto DIY heater-enclosure standard in community chat.

**D-Central** — Laval, QC institution: Bitaxe/open-source units, "Bitcoin Space Heaters 11 products", quiet modded Antminers, repair — [capture](../../raw/industry/d-central/2026-10-11-dcentral-home.md).

**Altair Technology** — reseller/glue for the ecosystem (Loki Rigs category, home-miner lines, live network widget) — [capture](../../raw/industry/altair-tech/2026-10-11-altair-home.md).

**Nakamoto Mining LTD.** — Schnitzel's store ("FREE shipping over $99 for Canadians! 🇨🇦"), 120V Home Mining category + FILE DEPOT — [capture](../../raw/industry/nakamoto-mining/2026-10-11-nakamoto-home.md). HashTub builder profiled in the book.

**Solo Satoshi** — "Your Trusted Bitcoin Hardware source. Fast Shipping!" — home-miner retail with a dedicated Heaters subcategory (Bitaxe, Nerdaxe, Avalon, solo miners; Learning Center, podcast, firmware flasher) — [capture](../../raw/industry/solosatoshi/2026-10-11-solosatoshi-home.md). Broke the Superheat CES 2026 unveiling.

## Shut down

**Unbound Networks** (active ~2023–2025) — Zack Bomsta ("the guy behind Unbound", previously of the Njord Cloudline and Loki board work) with business partner Clay (Missoula/Montana deployment); sold ASIC-based heating systems pre-modified from industrial hashboards. Book ch. 4: "reuses industrial miner hashboards, pre-modifying the machines for easy home use and quiet operation." (p. 57) — [book extract](../../raw/books/braiins-heat-reuse/04-successful-case-studies.md). At Undermine 2025 the team showed beta units — "My business partner Clay is out there building that network." — [summit panel transcript](../../raw/history/heatpunks-summit/20251111-undermine-2025-small-scale-bitcoin-mining-panel.md) — a little over a petahash deployed in Montana homes. Provenance: Braiins donated its experimental aluminum-PCB Marathon/S17 rigs to Unbound [#549 · 2024-03-22 · Zack Bomsta] — see [ASIC Thermals & Heat Reuse](../hardware/asic-thermals-and-heat-reuse.md). Press: ABC4/NerdWallet profile (Provo, Utah; radiant-floor pilot; bot-walled, pointer only). End state: employment records end 2025-08; unboundnetworks.com parked (registrar lander) with no bitcoin-era Wayback capture; Tyler confirms shut down (2026-10-11) — [shutdown record](../../raw/industry/unbound-networks/2026-10-11-unbound-networks-shutdown.md). Registry: `unbound-networks` (`dormant`, static).

## Infrastructure & energy

**Gridless** — mining as energy infrastructure beside African renewables: "Gridless runs compute beside renewable power plants in Africa. Communities get the power they need first. AI runs on the firm supply. Bitcoin buys everything left." — [capture](../../raw/industry/gridless/2026-10-11-gridless-home.md). Block/Stillmark-backed; the reference case for the emergent-grid thesis.

**GRIID Infrastructure** — *absorbed*. NASDAQ GRDI; CleanSpark "announced today the completed acquisition of GRIID Infrastructure Inc. (Nasdaq: GRDI)" effective 2024-10-30, ~0.06959 CLSK per GRDI share, 400 MW Tennessee/TVA buildout planned — [capture](../../raw/industry/griid/2026-10-11-cleanspark-griid-acquisition.md). Registry row kept `dormant` for history; successor coverage lives under `sec-edgar-miners` (CLSK).

**Flare-gas / field-gas infra** — Crusoe (AI pivot, NYDIG acquired its mining op), Upstream Data (BlackBox), Giga Energy (AI data-center pivot) — already tracked under Industry rows since A10; see [Public Miner Economics](public-miner-economics.md) for the AI/HPC pivot economics.

**Hosting / mining hotels** — Abundant Mines, Hotmine's hotel, Freedomtech — see [Mining Hotels & Hosting](mining-hotels-and-hosting.md).

## Research & consulting (no registry row)

**Hashlabs Mining** (Jaran Mellerud) — consultancy voice on Nordic mining and heat reuse (The Mining Pod, Energy-to-Compute). No official site verified (domain guesses DNS-fail 2026-10-11), so per the vetting bar it gets this mention only — track via podcast transcripts, not a site row.

## Skipped at vetting (2026-10-11)

- ~~**Unbound Networks**~~ — removed from the skip list 2026-10-11: Tyler confirmed it was legit but shut down; now tracked as history in [Shut down](#shut-down). Lesson recorded: no verifiable live footprint ≠ not legit.
- **Bitcoin Bloem** — tulip-farm case covered via book ch. 4 extract; no verified 2026 activity → no row.
- **Sato Technologies, Heata, Soluna, Bitmine Immersion, BitFury/Allied** — unverified or out of scope; reasons in the [vetting report](../../raw/industry/_REPORT-companies-2026-10-11.md).
- Assorted micro-startups: not researched = not tracked; the bar is deliberate.

## Registry mapping

| Company | Registry ID | Cadence |
|---|---|---|
| Fog Hashing / Fog Computing | `foghashing` | monthly |
| Heatbit | `heatbit` | monthly |
| MintGreen | `mintgreen` | monthly |
| HeatCore | `heatcore` | monthly |
| RY3T | `ry3t` | monthly |
| Hestia Heating | `hestia` | monthly |
| Constellation Heating | `constellation-heating` | monthly |
| Superheat | `superheat` | weekly (preorder phase) |
| Hotmine | `hotmine` | monthly |
| Hashrate House | `hashrate-house` | monthly |
| Pivotal Pleb Tech | `pivotal-pleb-tech` | monthly |
| 256 \| HEAT | `256heat` | monthly |
| D-Central | `d-central` | monthly |
| CryptoCloaks | `cryptocloaks` | monthly |
| Altair Technology | `altair-tech` | monthly |
| Nakamoto Mining | `nakamoto-mining` | monthly |
| Solo Satoshi | `solosatoshi` | monthly |
| Abundant Mines (hosting) | `abundant-mines` | monthly |
| Unbound Networks (shut down) | `unbound-networks` | static |
| Gridless | `gridless` | monthly |
| GRIID (dormant) | `griid` | static |
| Exergy (Tyler's own; docs/calcs/forum) | `exergy-docs` · `exergy-calculators` · `exergy-forum` | monthly/weekly |
