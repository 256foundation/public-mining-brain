# Libre Board

> Sources: 256 Foundation (projects page), collected 2026-10-07; 256 Foundation (newsroom: Libre Board funding), collected 2026-10-07; 256 Foundation (newsroom: MARA Foundation), collected 2026-10-07
> Raw: [256foundation.org projects](../../raw/foundation/256foundation-org-projects.md); [Libre Board funding](../../raw/foundation/256foundation-org-newsroom-libre-board-funding.md); [MARA Foundation $100,000](../../raw/foundation/256foundation-org-newsroom-mara-foundation-tier1-supporter.md)
> Updated: 2026-10-07

## Overview

Libre Board is the 256 Foundation's open-source control board for Bitcoin miners. It runs full Linux instead of a vendor firmware image, so the mining firmware becomes one program on a general-purpose computer. It is licensed CERN-OHL-S. As of the latest funding announcement, the design works and the remaining job is validating revision three.

## The gap it fills

A control board sits between the hash boards and everything else. It holds the firmware, the interfaces and the power sequencing, and so it decides what a miner is allowed to be. A closed board blocks custom firmware, a display, Wi-Fi at a remote site, or a flow sensor for a heating system.

## What it is

- Runs full Linux, with [Mujina](../mujina/mujina-firmware.md) supported natively.
- Can host a Bitcoin full node and a local Stratum server.
- Raspberry Pi 40-pin header, GPIO, and fan connectors.
- Ethernet, WiFi, HDMI and NVMe.
- Swappable compute, so one board can scale across system complexity.
- Power stages rated from 12 to 24 volts DC.

## Status and funding

The 2026 term was set in April and scheduled through December, contingent on funding. Funding ran short and the work paused. Additional funding reactivated it for four months, from September through December. The scope covers:

- Validating power and interface stages across their rated ranges.
- Confirming the full peripheral set.
- Checking mechanical fit and connector placement.
- Bringing the board up end to end with Mujina.
- Cutting revision three to fabrication with matching design files and bill of materials.

## DOOMAXE

At Bitcoin 2026, Schnitzel built DOOMAXE, a fully open-source reference miner, in a few days before the conference. Libre Board was the control board and ran Mujina. A Bitaxe served as the hash board because no [Ember One](ember-one.md) was on hand. A Raspberry Pi compute module on top ran [Hydrapool](../hydrapool/hydrapool.md) and its own Bitcoin node, on the miner itself. It also ran Proto Fleet, an open-source miner management system. The front screen played Doom.

## People

Schnitzel is the core architect and lead maintainer.

## See Also

- [Ember One](ember-one.md)
- [Mujina Firmware](../mujina/mujina-firmware.md)
- [Grants and Funding](../foundation/grants-and-funding.md)
- [Libre Board Design and Grant Scope](libre-board-design.md)
