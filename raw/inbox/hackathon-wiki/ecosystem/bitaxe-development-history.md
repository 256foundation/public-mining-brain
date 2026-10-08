# Bitaxe Development History

> Sources: Skot and Bitaxeorg, 2026-10-07 (GitHub snapshots); Skot, 2023-08-21; Skot, 2024-02-07; Skot, 2024-08-19; OSMU, Unknown; OpenSats, 2024-02-25; OpenSats, 2026-04-21; Frank Corva, 2024-10-22; Con Kolivas, 2025-03-10
> Raw: [Repository overview](../../raw/inbox/2026-10-07-github-bitaxeorg-org-snapshot.md); [Grant](../../raw/ecosystem/2024-02-25-opensats-bitaxe-grant.md); [Origins interview](../../raw/ecosystem/2024-10-22-skot-bitaxe-origins-interview.md); [BM1387 prototype](../../raw/ecosystem/2022-05-26-bitaxe-bm1387-prototype-readme.md); [Hardware commits](../../raw/ecosystem/bitaxe-hardware-commit-records.md); [Gamma](../../raw/ecosystem/github-bitaxeorg-bitaxegamma.md); [ESP Miner](../../raw/ecosystem/github-bitaxeorg-esp-miner.md); [MIT license](../../raw/ecosystem/2022-11-25-bitaxe-mit-license.md); [BM1397 platform](../../raw/ecosystem/2023-05-11-bitaxe-bm1397-platform-readme.md); [OSMU](../../raw/ecosystem/osmu-wiki-osmu-about.md); [Firmware releases](../../raw/ecosystem/bitaxe-firmware-release-records.md); [Ultra prototype](../../raw/ecosystem/2023-07-20-bitaxe-ultra-prototype-readme.md); [Ultra and Supra posts](../../raw/inbox/2026-10-07-x-notable-bitaxe-ultra-supra.md); [Supra](../../raw/ecosystem/github-bitaxeorg-bitaxesupra.md); [Block reports](../../raw/inbox/2026-10-07-bitaxe-open-source-mining-blocks-found.md); [Hardware releases](../../raw/ecosystem/bitaxe-hardware-release-records.md); [Licenses](../../raw/ecosystem/bitaxe-current-repository-license-records.md); [CKPool logs](../../raw/ecosystem/2025-03-10-ckpool-bitaxe-ultra-block-log.md); [NerdAxe](../../raw/ecosystem/osmu-wiki-nerdaxe-about.md); [NerdQAxe++](../../raw/ecosystem/osmu-wiki-nerdqaxeplusplus-about.md); [Impact report](../../raw/ecosystem/2026-04-21-opensats-bitaxe-impact-report.md); [Gamma Hex](../../raw/ecosystem/github-bitaxeorg-bitaxegammahex.md); [Naja](../../raw/ecosystem/github-bitaxeorg-bitaxenaja.md); [Bonanza](../../raw/ecosystem/github-bitaxeorg-bitaxebonanza.md); [Max](../../raw/ecosystem/github-bitaxeorg-bitaxemax.md); [Ultra](../../raw/ecosystem/github-bitaxeorg-bitaxeultra.md); [Ultra Hex](../../raw/ecosystem/github-bitaxeorg-ultrahex.md); [Gamma Duo](../../raw/ecosystem/osmu-wiki-bitaxe-650.md); [GT](../../raw/ecosystem/github-bitaxeorg-bitaxegt.md); [Gamma posts](../../raw/inbox/2026-10-07-x-notable-bitaxe-gamma.md); [Max model](../../raw/ecosystem/osmu-wiki-bitaxe-100.md); [Ultra model](../../raw/ecosystem/osmu-wiki-bitaxe-200.md); [Hex model](../../raw/ecosystem/osmu-wiki-bitaxe-300.md); [Supra model](../../raw/ecosystem/osmu-wiki-bitaxe-400.md); [Gamma model](../../raw/ecosystem/osmu-wiki-bitaxe-600.md); [Interview publication](../../raw/inbox/2026-10-07-press-media-talks-research.md); [Chain verification](../../raw/inbox/2026-10-07-mempool-onchain-block-verification.md)
> Updated: 2026-10-07

## Overview

Bitaxe grew from Skot’s experiments with undocumented Bitcoin mining chips into a family of open hardware designs supported by shared firmware, independent manufacturers, and the Open Source Miners United community. Its central contribution is a reference design that people can build, inspect, modify, and manufacture themselves.

Sources: [Project repositories](../../raw/inbox/2026-10-07-github-bitaxeorg-org-snapshot.md); [OpenSats grant announcement](../../raw/ecosystem/2024-02-25-opensats-bitaxe-grant.md)

The public hardware record begins on 2022-03-04. A practical standalone miner emerged in 2023, followed by newer ASIC generations, browser-based management through AxeOS, and designs with multiple mining chips. The development history therefore has several beginnings: the first experimental boards, the working Max platform, and the community that made the designs reproducible.

### Before Bitaxe

In a 2024-10-22 interview, Skot recalled encountering Bitcoin in 2011 and building an FPGA miner two years later. The open code available for that earlier hardware helped him learn how mining worked. His later ASIC experiments began as a technical challenge and developed into a commitment to opening the mining hardware and firmware that Bitcoin users depend on.

Sources: [Skot interview](../../raw/ecosystem/2024-10-22-skot-bitaxe-origins-interview.md); [Interview publication record](../../raw/inbox/2026-10-07-press-media-talks-research.md)

### The first boards

The initial Bitaxe design used BM1387 ASICs associated with the Antminer S9. The 2022-05-26 README recorded 2 assembled boards, but Skot had not yet obtained a response from the chips. This was an experimental platform for learning the electrical interface and protocol. Manufacturing files and a revised parts list followed in June.

Sources: [May 2022 README](../../raw/ecosystem/2022-05-26-bitaxe-bm1387-prototype-readme.md); [June manufacturing files](../../raw/ecosystem/bitaxe-hardware-commit-records.md)

### What is open

Bitaxe publishes board designs and manufacturing data, while ESP-Miner provides open firmware and the AxeOS web interface. The Bitmain ASIC silicon remains proprietary. Reverse engineering the chip interface makes it possible to build an open miner around that silicon; it does not make the chip itself an open design.

Sources: [Gamma hardware documentation](../../raw/ecosystem/github-bitaxeorg-bitaxegamma.md); [ESP-Miner](../../raw/ecosystem/github-bitaxeorg-esp-miner.md)

The chronology below distinguishes development commits, public demonstrations, firmware releases, and tagged hardware releases. GitHub dates follow the UTC timestamps in the public record. Performance figures describe the reported configuration and period, rather than a guaranteed specification for every board.

## Development timeline 2022 and 2023

### 2022-03-04 Public hardware history begins

Skot made the initial import into skot/bitaxe. A 2022-03-05 commit recorded the first routed board. These commits anchor the public development history before the better-known standalone miners of 2023.

Sources: [Initial import](../../raw/ecosystem/bitaxe-hardware-commit-records.md); [First routing commit](../../raw/ecosystem/bitaxe-hardware-commit-records.md)

### 2022 Experiments and a license

The BM1387 boards were assembled but still under investigation in May. June brought revised manufacturing files and the start of a BM1397 experiment under the name bitaxePro. The repository added an MIT license on 2022-11-25.

Sources: [Prototype README](../../raw/ecosystem/2022-05-26-bitaxe-bm1387-prototype-readme.md); [BM1397 experiment](../../raw/ecosystem/bitaxe-hardware-commit-records.md); [MIT license](../../raw/ecosystem/2022-11-25-bitaxe-mit-license.md)

### Early 2023 The Max platform takes shape

The BM1397 design developed into the platform later called Bitaxe Max. Its ESP32-S3 controller, Wi-Fi, adjustable core voltage, power measurement, and fan control established much of the architecture used by subsequent single-chip boards.

Sources: [May 2023 hardware record](../../raw/ecosystem/2023-05-11-bitaxe-bm1397-platform-readme.md)

### March 2023 Open Source Miners United forms

OSMU dates its founding to March 2023. The community became the shared venue for hardware experiments, firmware work, assembly knowledge, and collaboration beyond any single board revision.

Sources: [OSMU history](../../raw/ecosystem/osmu-wiki-osmu-about.md)

### 2023-07-01 ESP Miner reaches version 1

ESP-Miner v1.0 targeted Bitaxe v2.2 and documented Stratum V1, Wi-Fi, OLED statistics, and power management for solar applications. Its release notes reported 300-350 GH/s, providing a dated record of a usable standalone miner.

Sources: [Firmware v1.0](../../raw/ecosystem/bitaxe-firmware-release-records.md#v10)

### 2023-07-10 to 2023-08-21 Ultra becomes a working miner

2023-07-10 commits introduced BM1366 design assets and the Ultra name. The 2023-07-20 README described a built prototype responding over serial, with mining firmware adaptation still pending. On 2023-08-21, Skot reported a single BM1366 hashing at 527 GH/s and 20 J/TH, crediting OSMU.

Sources: [Ultra naming commit](../../raw/ecosystem/bitaxe-hardware-commit-records.md); [July prototype status](../../raw/ecosystem/2023-07-20-bitaxe-ultra-prototype-readme.md); [Skot Ultra launch post](../../raw/inbox/2026-10-07-x-notable-bitaxe-ultra-supra.md)

### 2023-09-15 to 2023-11-27 More chips and easier operation

Six-chip Ultra Hex development was already underway in September. ESP-Miner v2.0.0, released 2023-10-04, added BM1366 support, the AxeOS web interface, an HTTP API, wireless updates, and access-point onboarding. Version 2.0.4 added Swarm management on 2023-11-27.

Sources: [Hex development commit](../../raw/ecosystem/bitaxe-hardware-commit-records.md); [Firmware v2.0.0](../../raw/ecosystem/bitaxe-firmware-release-records.md#v200); [Swarm release](../../raw/ecosystem/bitaxe-firmware-release-records.md#v204)

## Development timeline 2024

### 2024-02-07 Supra is publicly introduced

The Supra moved to the BM1368 used in the Antminer S21. Skot announced a working single-BM1368 miner running around 620 GH/s, credited OSMU, and said further work was needed before shipping. This was the next single-chip generation, following the BM1397 Max and BM1366 Ultra.

Sources: [Skot Supra launch thread](../../raw/inbox/2026-10-07-x-notable-bitaxe-ultra-supra.md); [Supra hardware](../../raw/ecosystem/github-bitaxeorg-bitaxesupra.md)

### 2024-02-25 OpenSats announces funding

OpenSats included Bitaxe in its fourth wave of Bitcoin grants. The announcement emphasized its role as an adaptable reference design and the importance of manufacturing and firmware documentation. Skot later said the grant enabled him to work on the project full time.

Sources: [Grant announcement](../../raw/ecosystem/2024-02-25-opensats-bitaxe-grant.md); [Skot interview](../../raw/ecosystem/2024-10-22-skot-bitaxe-origins-interview.md)

### 2024-03-04 Shared firmware supports Supra

ESP-Miner v2.1.0 added BM1368 support and refactored the AxeOS interface. The release credits johnny9 for the ASIC support. Supporting a new chip in the shared firmware let the hardware family continue using a common software foundation.

Sources: [Firmware v2.1.0](../../raw/ecosystem/bitaxe-firmware-release-records.md#v210)

### 2024-07-24 The first publicly reported Bitaxe block

Block 853742 was credited to a Bitaxe miner on Solo CKPool. Pool operator Con Kolivas reported approximately 3 TH/s for the miner. The event demonstrated a real block find by the project’s small-miner community, while the contemporary records do not settle the exact board configuration.

Sources: [Pool operator report](../../raw/inbox/2026-10-07-bitaxe-open-source-mining-blocks-found.md); [On-chain confirmation](../../raw/inbox/2026-10-07-mempool-onchain-block-verification.md)

### 2024-08-19 Gamma is demonstrated

Skot announced Gamma with the BM1370 from the Antminer S21 Pro, reporting approximately 1 - 1.2 TH/s at around 15 J/TH from one chip. Gamma’s hardware documentation identifies it as Bitaxe’s fifth major revision.

Sources: [Skot Gamma launch thread](../../raw/inbox/2026-10-07-x-notable-bitaxe-gamma.md); [Gamma hardware](../../raw/ecosystem/github-bitaxeorg-bitaxegamma.md)

### 2024-10-10 Gamma 600 hardware is released

The first tagged Gamma release followed the August demonstration. Its notes describe a design based on Supra 402, adapted for BM1370 and a TPS546 regulator with integrated switches. The tagged release is the clearest manufacturing milestone for the initial Gamma.

Sources: [Gamma 600 release](../../raw/ecosystem/bitaxe-hardware-release-records.md#gamma-600)

### 2024-12-27 Hardware licensing changes

The original hardware repository changed its license to CERN-OHL-S. This established a strongly reciprocal open hardware license for the designs. Current model repositories use CERN-OHL-S-2.0, while ESP-Miner uses GPL-3.0.

Sources: [License change](../../raw/ecosystem/bitaxe-hardware-commit-records.md); [Current hardware license](../../raw/ecosystem/bitaxe-current-repository-license-records.md); [Firmware license](../../raw/ecosystem/bitaxe-current-repository-license-records.md)

## Development timeline 2025 and early 2026

### 2025-03-10 An Ultra worker finds another block

CKPool confirmed block 887212 from the worker named bitaxeultra4. The account’s total hashrate was approximately 3.3 TH/s; the winning worker’s longer-term rate was around 480 GH/s. The original logs distinguish the individual worker from the larger group of miners.

Sources: [CKPool operator and logs](../../raw/ecosystem/2025-03-10-ckpool-bitaxe-ultra-block-log.md)

### 2025-04-04 The repository points to Bitaxeorg

A README update in skot/bitaxe announced that the hardware had split into model-specific repositories under bitaxeorg. This is a dated public marker of the organizational change, rather than the date every repository was created or transferred.

Sources: [Repository notice](../../raw/ecosystem/bitaxe-hardware-commit-records.md)

### 2025-04-07 Gamma 602 improves manufacture

The Gamma 602 release recorded improvements to design for manufacture and routing. Work on Gamma continued after its initial release, with board revisions improving reproducibility and assembly.

Sources: [Gamma 602 release](../../raw/ecosystem/bitaxe-hardware-release-records.md#gamma-602)

### By 2025 Community derivatives broaden the design

The ecosystem extended the reference design into devices such as NerdAxe and NerdQAxe++. OSMU documents their origins in Bitaxe Ultra. NerdAxe combines Ultra mining logic with a different display platform; NerdQAxe++ uses four BM1370 chips and its own firmware derivative.

Sources: [NerdAxe lineage](../../raw/ecosystem/osmu-wiki-nerdaxe-about.md); [NerdQAxe++ lineage](../../raw/ecosystem/osmu-wiki-nerdqaxeplusplus-about.md)

### 2025-11-15 Swarm management develops further

ESP-Miner v2.11.0 added a Swarm grid view, rearranged layouts, device notifications, and broader interface changes. Fleet management had become a continuing part of the firmware project, building on the first Swarm release in 2023.

Sources: [Firmware v2.11.0](../../raw/ecosystem/bitaxe-firmware-release-records.md#v2110)

### 2026-01-05 and 2026-01-06 GT 801 gets a hardware release

The Gamma Turbo 801 hardware release published the dual-BM1370 design on 2026-01-05. ESP-Miner v2.12.2 followed 2026-01-06 with GT self-test and power-management improvements. OpenSats later reported a vendor configuration of about 2.15 TH/s at roughly 43 watts.

Sources: [GT 801 hardware](../../raw/ecosystem/bitaxe-hardware-release-records.md#gt-801); [Firmware v2.12.2](../../raw/ecosystem/bitaxe-firmware-release-records.md#v2122); [OpenSats impact report](../../raw/ecosystem/2026-04-21-opensats-bitaxe-impact-report.md)

### 2026-02-05 to 2026-02-20 Gamma Duo and Gamma 603 are released

Gamma Duo 650 received a hardware release on 2026-02-05, followed by Gamma 603 on 2026-02-17. OSMU describes Duo as a way to reuse lower-performing S21-family chips. ESP-Miner v2.13.0 on 2026-02-20 added 650 and 801 configuration support, TLS, and further BAP improvements.

Sources: [Duo 650 release](../../raw/ecosystem/bitaxe-hardware-release-records.md#gamma-duo-650); [Gamma 603 release](../../raw/ecosystem/bitaxe-hardware-release-records.md#gamma-603); [Firmware v2.13.0](../../raw/ecosystem/bitaxe-firmware-release-records.md#v2130)

## Development timeline later 2026

### 2026-04-21 OpenSats records the project’s scale

In its hardware impact report, OpenSats published Skot’s estimate that more than 100,000 Bitaxe units had been sold and at least six blocks had been solo mined. These were project-lead estimates, reflecting the difficulty of counting independently manufactured devices and private miners.

Sources: [Open Hardware for Open Money](../../raw/ecosystem/2026-04-21-opensats-bitaxe-impact-report.md)

### 2026-06-04 Stratum V2 enters a stable firmware release

ESP-Miner v2.14.0 included Stratum V2 support, a customizable AxeOS dashboard, a WebSocket API, and changes to nonce handling and factory self-testing. The release expanded protocol support and the tools used to operate and manufacture miners.

Sources: [Firmware v2.14.0](../../raw/ecosystem/bitaxe-firmware-release-records.md#v2140)

### 2026-07-20 and 2026-07-27 Gamma Hex hardware is published

A 2026-07-20 commit recorded the Gamma Hex hardware release, followed by README publication on 2026-07-27. The 1300 design uses six BM1370 chips arranged in two domains, with a 12 V input, a color display, and a four-phase regulator. This is a separate generation from the earlier BM1366 Ultra Hex.

Sources: [Hardware release commit](../../raw/ecosystem/bitaxe-hardware-commit-records.md); [Gamma Hex documentation](../../raw/ecosystem/github-bitaxeorg-bitaxegammahex.md)

### 2026-08-21 Firmware updates become simpler

ESP-Miner v2.15.0 embedded the AxeOS interface inside the main firmware binary, removing the need to update a separate web-interface file. The release also added mDNS discovery so users could reach the dashboard by the miner’s hostname.

Sources: [Firmware v2.15.0](../../raw/ecosystem/bitaxe-firmware-release-records.md#v2150)

### 2026-09-18 New ASIC drivers are added

ESP-Miner v2.15.2 added BM1372 and BM1373 drivers. Driver support is a software milestone; it does not by itself establish a production release for every board using those chips.

Sources: [Firmware v2.15.2](../../raw/ecosystem/bitaxe-firmware-release-records.md#v2152)

### The development frontier

The public repositories also preserve experiments alongside released hardware. Bitaxe Naja’s README describes an untested dual-BM1340 prototype. Bonanza explores eight Intel BZM2 chips and explicitly records unresolved issues preventing operation. These projects show how Bitaxe’s design practice extends to additional ASICs while keeping experimental status visible.

Sources: [Naja prototype](../../raw/ecosystem/github-bitaxeorg-bitaxenaja.md); [Bonanza experiment](../../raw/ecosystem/github-bitaxeorg-bitaxebonanza.md)

Taken together, the later milestones show development moving in two directions: more ASICs and newer chip interfaces, and easier operation through shared firmware. Tagged boards, device support, and usability improvements each contribute a different part of a reproducible mining system.

## Hardware generations and branches

Model series identify related board designs. They are not a simple count of successive generations: the Hex branches and dual-chip boards developed alongside the single-chip line. Historical performance figures below retain their original source context.

| Model family | ASICs | Historical marker | Development contribution or reported performance |
| --- | --- | --- | --- |
| [Early Bitaxe](../../raw/ecosystem/2022-05-26-bitaxe-bm1387-prototype-readme.md) | BM1387 | 2022 experimental boards | Protocol investigation; 2 assembled boards recorded in May. |
| [Max 100 series](../../raw/ecosystem/github-bitaxeorg-bitaxemax.md) | 1 BM1397 | 2023 standalone platform | ESP-Miner v1.0 reported 300-350 GH/s. |
| [Ultra 200 series](../../raw/ecosystem/github-bitaxeorg-bitaxeultra.md) | 1 BM1366 | 2023 working prototype | Skot reported 527 GH/s at 20 J/TH in August. |
| [Ultra Hex 300 series](../../raw/ecosystem/github-bitaxeorg-ultrahex.md) | 6 BM1366 | 2023 multichip development | Larger 12 V design; revisions documented regulator issues. |
| [Supra 400 series](../../raw/ecosystem/github-bitaxeorg-bitaxesupra.md) | 1 BM1368 | 2024-02-07 announcement | Approximately 620 GH/s in Skot’s announcement. |
| [Gamma 600 series](../../raw/ecosystem/github-bitaxeorg-bitaxegamma.md) | 1 BM1370 | 2024-10-10 first tagged release | Approximately 1.2 TH/s per board in project documentation. |
| [Gamma Duo 650](../../raw/ecosystem/osmu-wiki-bitaxe-650.md) | BM1370 family | 2026-02-05 release | Reuses lower-performing chips from the S21 lineup. |
| [Gamma Turbo 801](../../raw/ecosystem/github-bitaxeorg-bitaxegt.md) | 2 BM1370 | 2026-01-05 first release | About 2.15 TH/s at 43 watts in an OpenSats-reported vendor configuration. |
| [Gamma Hex 1300](../../raw/ecosystem/github-bitaxeorg-bitaxegammahex.md) | 6 BM1370 | 2026-07-20 hardware publication | Two ASIC domains, 12 V input, color LCD, and four-phase regulation. |

GH/s and TH/s measure hashes per second. J/TH measures energy per trillion hashes. A lower J/TH figure means greater energy efficiency. Rates depend on the chip, voltage, frequency, cooling, and firmware settings.

Sources: [Early firmware performance](../../raw/ecosystem/bitaxe-firmware-release-records.md#v10); [Ultra demonstration](../../raw/inbox/2026-10-07-x-notable-bitaxe-ultra-supra.md); [Supra announcement](../../raw/inbox/2026-10-07-x-notable-bitaxe-ultra-supra.md); [GT performance context](../../raw/ecosystem/2026-04-21-opensats-bitaxe-impact-report.md)

## Community and lasting milestones

### A shared engineering effort

Skot instigated the hardware project, and OSMU provided a place for contributors to work across board design, ASIC protocols, firmware, and assembly. The ESP-Miner v2.0.0 release credited benjamin-wilson, Skot, Georges760, developeralgo8888, SatsForFreedom, and OSMU. Later releases record contributions from johnny9, WantClue, mutatrum, and many others. The release histories document a continuing collective effort.

Sources: [ESP-Miner v2.0.0 credits](../../raw/ecosystem/bitaxe-firmware-release-records.md#v200); [BM1368 contribution](../../raw/ecosystem/bitaxe-firmware-release-records.md#v210); [Later contributions](../../raw/ecosystem/bitaxe-firmware-release-records.md#v2130)

### Manufacturing became reproducible

The combination of board files, parts lists, manufacturing outputs, assembly guidance, and matching firmware allowed independent builders to reproduce the designs. Sellers and derivatives broadened the project’s reach. OpenSats funding supported dedicated development, while public documentation let manufacturers work from the same reference designs.

Sources: [Manufacturing and assembly record](../../raw/ecosystem/github-bitaxeorg-bitaxeultra.md); [Funding announcement](../../raw/ecosystem/2024-02-25-opensats-bitaxe-grant.md)

### Usability became part of the mining design

The transition from ESP-Miner v1 to AxeOS mattered alongside each ASIC upgrade. Browser onboarding, wireless firmware updates, APIs, and Swarm management reduced the work needed to configure miners and operate several boards together. The 2026 protocol and packaging releases continued that process with Stratum V2 support and a single firmware binary containing the web interface.

Sources: [AxeOS introduction](../../raw/ecosystem/bitaxe-firmware-release-records.md#v200); [First Swarm release](../../raw/ecosystem/bitaxe-firmware-release-records.md#v204); [Stratum V2 release](../../raw/ecosystem/bitaxe-firmware-release-records.md#v2140); [Unified firmware](../../raw/ecosystem/bitaxe-firmware-release-records.md#v2150)

### Open hardware could be adapted

Ultra-derived projects such as NerdAxe and NerdQAxe++ demonstrate reuse beyond the original board and display. The later GT and Gamma Hex designs also show that the same open development approach can support different ASIC counts, power systems, and physical formats. CERN-OHL-S provides the reciprocal licensing framework used by the current hardware designs.

Sources: [Derivative lineage](../../raw/ecosystem/osmu-wiki-nerdqaxeplusplus-about.md); [GT hardware](../../raw/ecosystem/github-bitaxeorg-bitaxegt.md); [Hardware license](../../raw/ecosystem/bitaxe-current-repository-license-records.md)

### Block wins proved participation

The publicly documented 2024 and 2025 block finds show that small ASIC miners can submit valid Bitcoin blocks. Their historical importance is participation and a visible result from community hardware. They do not establish a predictable return for any particular miner. The difference between a winning worker’s rate and an account’s aggregate rate matters when describing these events.

Sources: [First block report](../../raw/inbox/2026-10-07-bitaxe-open-source-mining-blocks-found.md); [March 2025 operator logs](../../raw/ecosystem/2025-03-10-ckpool-bitaxe-ultra-block-log.md)

### Source record

The dated entries link to the public evidence for each milestone. Repository snapshots preserve prototype status, while tagged releases anchor hardware and firmware publication. Interviews and archived public posts provide Skot’s account of the project’s origins and demonstrations. The history follows the linked source records, with prototype status and reported estimates retained.
