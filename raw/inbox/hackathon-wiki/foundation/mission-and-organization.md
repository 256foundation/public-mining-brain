# 256 Foundation: Mission and Organization

> Sources: 256 Foundation (256foundation.org mission page), collected 2026-10-07; 256 Foundation (256foundation.org our-work page), collected 2026-10-07
> Raw: [256foundation.org mission](../../raw/foundation/256foundation-org-mission.md); [256foundation.org our work](../../raw/foundation/256foundation-org-our-work.md)
> Updated: 2026-10-07

## Overview

The 256 Foundation is a 501(c)(3) nonprofit that funds open-source replacements for every closed layer of the Bitcoin mining stack. Its stated mission is to decentralize Bitcoin mining so that the technology Bitcoin depends on cannot be owned, switched off, or permissioned by anyone. It describes its own role as "the Linux Foundation of Bitcoin Mining."

## The problem it names

The foundation says mining does three jobs for Bitcoin: it issues new coins, settles transactions, and secures the record. Today that machinery is closed, and one company controls most of the hardware and software.

It breaks a modern miner into four building blocks, each closed or concentrated:

- **Hash board.** Mining chips ship with no datasheets or pinouts and cannot be bought on their own.
- **Control board.** Locked bootloaders and limited I/O decide what a miner is allowed to be.
- **Firmware.** It cannot be audited, so nobody can verify it is not skimming hashrate or holding a kill switch. The foundation cites Antbleed as proof.
- **Pool.** The server side is concentrated and opaque, and trusting an operator is the only way to aggregate hashrate.

## The approach

The foundation reverse-engineered each layer, published the designs as open source, and funds the work to commoditize them. Its four core projects answer the four blocks: [Ember One](../hardware/ember-one.md) (hash board), [Libre Board](../hardware/libre-board.md) (control board), [Mujina](../mujina/mujina-firmware.md) (firmware) and [Hydrapool](../hydrapool/hydrapool.md) (pool). Together they form what it calls a permissionless development kit.

Its argument for being a nonprofit: a company has an edge to protect, so a company is the wrong vehicle. As a nonprofit, success means anyone can use, fork, build upon and compete with the work.

## Operating principles

- **Money from anyone, influence from no one.** Funding does not buy special treatment.
- **No obligation to capture value.** The nonprofit structure lets it act as a neutral home for shared dependencies and never compete with contributors.
- **It starts projects but does not own or sell them.** Every core project and grant is released under a recognized open-source licence.

## Programs beyond the core projects

- **Red Team Program.** Reverse engineering closed firmware and mining software, followed by responsible disclosure.
- **Working Group Program.** Convening the industry around standards, specifications, form factors, connectors and API endpoints.
- **Stewardship.** A neutral home for shared dependencies such as ASIC-rs. The foundation says it will not transfer the repo, take exclusive rights, or accept funding conditioned on ceding control.
- **Community Program.** Fiscal sponsorship for OSMU and Hashrate Heatpunks through two restricted, community-directed funds.
- **Education.** Developer calls, the forum, the podcast, the newsletter, and hands-on workshops.

## People

| Person | Role |
|---|---|
| Bitkite | Co-Founder. Co-founder of Bitcoin Park in Nashville and Austin. |
| Econoalchemist | Co-Founder and Project Manager. Co-host of the POD256 podcast. |
| Tyler Stevens | President of the Board. Mechanical engineer, founder of Exergy, instigated the Hashrate Heatpunks community. |
| Skot | Secretary of the Board. Electrical engineer who instigated the Bitaxe project. |
| Joe Wood | Treasurer of the Board. Licensed CPA, founder of Satoshi Pacioli. |

## See Also

- [Grants and Funding](grants-and-funding.md)
- [Telehash](telehash.md)
- [Bitaxe and Open Source Miners United](../ecosystem/bitaxe-and-osmu.md)
