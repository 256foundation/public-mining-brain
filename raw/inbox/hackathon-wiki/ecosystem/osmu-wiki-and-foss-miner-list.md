# OSMU Wiki and the FOSS Miner List

> Sources: Open Source Miners United (osmu.wiki, home page), collected 2026-10-07; bitaxeorg (osmu-wiki README), collected 2026-10-07; bitaxeorg (foss-miner-list README), collected 2026-10-07; Bitaxe.org (FAQ page), collected 2026-10-07; Open Source Miners United (osmu.wiki, About OSMU), collected 2026-10-07
> Raw: [osmu.wiki home](../../raw/ecosystem/osmu-wiki-home.md); [osmu-wiki README](../../raw/ecosystem/github-bitaxeorg-osmu-wiki.md); [foss-miner-list README](../../raw/ecosystem/github-bitaxeorg-foss-miner-list.md); [bitaxe.org FAQ](../../raw/ecosystem/bitaxe-org-faq.md); [About OSMU](../../raw/ecosystem/osmu-wiki-osmu-about.md)
> Updated: 2026-10-07

## Overview

Open Source Miners United keeps two public directories of its work. The OSMU wiki at osmu.wiki holds documentation and build guides for the community's projects. The FOSS miner list is a short table of open hardware designs and firmware with links to their repositories. This article describes both and works as a map to the other ecosystem articles. For OSMU itself, see [Bitaxe and Open Source Miners United](bitaxe-and-osmu.md).

## The OSMU wiki

The home page describes the wiki as documentation, build guides and hard-won knowledge for open-source Bitcoin mining hardware, written by the people who designed it. Its headline is "The origin of every big open source mining project." The page shows four figures: 39 wiki pages, 13 project sections, founded 2023, and 100% open source.

Project sections on the home page, with the article here that covers each:

| Wiki section | Covered in |
|--------------|------------|
| Bitaxe, from the 100 / Max through to the 801 / Gamma Turbo | [Bitaxe Model Lineup](bitaxe-models.md), [Multi-Chip Bitaxe Designs](multi-chip-bitaxe-designs.md) |
| Bitaxe API and BAP | [AxeOS API](axeos-api.md), [Open Mining Tools and Bitaxe Accessories](tools-and-accessories.md) |
| Nerdminer, NerdNOS, NerdAxe, NerdQAxe+ and NerdQAxe++ | [The Nerd Miner Family](nerd-miner-family.md) |
| OSMU Lab notes on the mining ASICs | [Bitmain Mining ASIC Chips](mining-asic-chips.md) |
| AxeOS, the ESP-Miner firmware | [AxeOS / ESP-Miner Firmware](axeos-esp-miner-firmware.md) |
| PiAxe, QAxe and BitForge | [PiAxe, QAxe and BitForge Nano](other-open-miners.md) |
| Tips: building PCBs, assembly and FAQ | [Building a Bitaxe](building-a-bitaxe.md) |
| Public Pool | [Public Pool](public-pool.md) |
| Bitcrane, Antsniffer and BitHalo | [Open Mining Tools and Bitaxe Accessories](tools-and-accessories.md) |

### How the wiki is built

The wiki's source is the bitaxeorg osmu-wiki repository. Its README says the wiki is the place to store all information about projects affiliated to OSMU, to make them searchable and more accessible, and that any participation is welcome.

- It is built with the Starlight template on top of Astro.
- Every page has an edit button at the bottom that leads to the page on GitHub.
- New content goes in the `src/content/docs` folder. By convention each project has its own folder with an `about.md` page.
- A page appears in the sidebar only after it is added to `astro.config.mjs`.
- Frontmatter at the top of a page can carry a title, a logo, a Discord channel, a GitHub repository and a list of shops. A shop entry has a name, a link, a region and an optional official flag that shows a badge.
- Local development needs Node.js. Contributors are asked to run the build before pushing to catch errors.
- Commits that reach the master branch are deployed automatically through Vercel.

## The FOSS miner list

The foss-miner-list repository holds two tables.

**Hardware designs.** Each row gives a name, the ASIC count and type, and a GitHub link. The entries fall into groups:

- Single-chip Bitaxe boards: Max, Ultra, Supra and Gamma.
- Two-chip boards: Bitaxe Gamma Duo, Bitaxe GT and BitForge Nano.
- Six-chip Hex boards, from bitaxeorg and from TinyChipHub.
- Nerd boards: NerdAxe, NerdQAxe variants and the eight-chip NerdOCTAXE boards.
- The PiAxe, a single-chip Pi HAT.

**Firmware.** Five entries, each tied to its target hardware:

| Firmware | Target hardware |
|----------|-----------------|
| ESP-Miner (AxeOS) | Bitaxe |
| ESP-Miner-NerdAxe | NerdAxe single-chip variants |
| ESP-Miner-NerdQAxePlus | NerdQAxe+, NerdQAxe++ and Octaxe boards |
| ForgeOS | BitForge Nano |
| ESP-Miner-TCH | Bitaxe 70x |

## What ties them together

Bitaxe.org's FAQ says OSMU projects release all design files and firmware to the public, unlike nearly every other mining equipment manufacturer. It gives three reasons: transparency, repairability and keeping development decentralized. OSMU's own about page says the group rejects industry gatekeeping and secrecy. Both pages date the founding to March 2023 and invite people to the OSMU Discord.

## See Also

- [Bitaxe and Open Source Miners United](bitaxe-and-osmu.md)
- [Bitaxe Model Lineup](bitaxe-models.md)
- [The Nerd Miner Family](nerd-miner-family.md)
- [256 Foundation: Mission and Organization](../foundation/mission-and-organization.md)
