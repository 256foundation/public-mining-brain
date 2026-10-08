# Libre Board Design and Grant Scope

> Sources: 256 Foundation (libreboard.org home page), collected 2026-10-07; 256 Foundation (libreboard README), collected 2026-10-07
> Raw: [libreboard.org home](../../raw/hardware/libreboard-org-home.md); [libreboard README](../../raw/hardware/github-256foundation-libreboard.md)
> Updated: 2026-10-07

## Overview

This article covers what the Libre Board project site says about the board's design and the grant behind it: the planned connections, the swappable compute module, what the grant pays for, and what it leaves out. For the project overview, status and funding history, see [Libre Board](libre-board.md).

## Design intent

Libre Board is an open-source control board designed for the [Ember One](ember-one.md) hash boards. The site says there were no open-source control boards before it. Aftermarket control boards exist, but they are all closed source.

The first job of the board is to complete the Ember One mining system. Beyond that, the first board is meant to be able to run a Bitcoin full node and a stable Stratum server while also running the hash boards.

Two design choices make it flexible:

- **Standard I/O.** USB for the Ember One hash boards, plus Ethernet, HDMI, NVME, fan connectors and WiFi. Later forks can change the form factor, the I/O, and the fan and hash board connectors to match Antminers, Whatsminers, or any other miner.
- **Swappable compute.** Two standardized 100-pin connectors hold the compute module. The user chooses the processor: RISC-V, ARM, or something else. The site also names x86 as a long-term goal. Because [Mujina](../mujina/mujina-firmware.md) is Linux based, it can run on whichever module is chosen.

## Planned connections

The grant's six-month deliverable is a control board based on the Raspberry Pi Compute Module I/O Board, with at least:

- USB hub integration
- Fan connections
- NVME expansion
- Two 100-pin connectors for the compute module
- An Ethernet port
- An HDMI port
- An Rpi 40-pin header
- A MIPI port for a touchscreen
- 12-24 VDC input power

## The grant

- The grant officially launched on April 5, 2025.
- It funds one project manager and one engineer.
- The term is six months. It can be extended at the end of each six-month cycle, pending negotiations.
- The budget covers fair-market pay for the project manager, plus materials, travel and living expenses for the engineer. Prototype materials are included.
- Funds are paid monthly in equal amounts. Exact dollar amounts are kept confidential for security reasons.
- A renewal opportunity opens within 30-days before the grant cycle expires.
- Sales, distribution, marketing and customer technical support are excluded.

The site ties the grant to the foundation's mission: “Dismantle the proprietary mining empire to make Bitcoin and freedom tech accessible to anyone”.

## License and repository

The project is licensed CERN-OHL-S. The GitHub repository is `256foundation/libreboard`. Its README is short: a one-line description, a pointer to libreboard.org, the logo, and front and back renders of the board.

## People and help

The site names @Schnitzel as lead engineer and @econoalchemist as project manager. Help is offered through the 256 Foundation public forum on Telegram.

## See Also

- [Libre Board](libre-board.md)
- [Ember One](ember-one.md)
- [Ember One Hardware Details](ember-one-hardware.md)
- [Grants and Funding](../foundation/grants-and-funding.md)
