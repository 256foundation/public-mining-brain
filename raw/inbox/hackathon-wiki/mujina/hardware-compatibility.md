# Mujina Hardware Compatibility

> Sources: Mujina project (mujina.org hardware compatibility, current as of July 2026), collected 2026-10-07; Mujina project (mujina.org status page, current as of July 2026), collected 2026-10-07; Mujina project (mujina.org why-mujina page), collected 2026-10-07; 256 Foundation (mujina GitHub README), collected 2026-10-07; 256 Foundation forum (Mujina-Antminer), 2026-05-11; 256 Foundation forum (Best Practices for Hacking Mujina onto Other Miners?), 2026-05-18; 256 Foundation forum (Mujina Dev Call), 2026-05-03
> Raw: [mujina.org hardware compatibility](../../raw/mujina/mujina-org-reference-hardware-compatibility.md); [mujina.org status](../../raw/mujina/mujina-org-explanation-status.md); [mujina.org why Mujina](../../raw/mujina/mujina-org-explanation-why-mujina.md); [mujina README](../../raw/mujina/github-256foundation-mujina.md); [Mujina-Antminer thread](../../raw/mujina/2026-05-11-forum-mujina-antminer.md); [Hacking Mujina onto other miners thread](../../raw/mujina/2026-05-18-forum-best-practices-for-hacking-mujina-onto-other-miners.md); [Dev Call 1](../../raw/mujina/2026-05-03-forum-mujina-dev-call.md)
> Updated: 2026-10-07

## Overview

[Mujina](mujina-firmware.md) aims to run any hashboard from any vendor. The project says a board is not ported: a driver for the board is added to Mujina, and the shared core does the rest. Drivers arrive board by board, and some live in forks outside the main repository. The mujina.org compatibility matrix, current as of July 2026, lists three things working in mainline (Bitaxe Gamma, the CPU backend and EmberOne/00), Antminer S19j Pro and S19k Pro in a fork, and Intel BZM2 boards in progress. Forum posts report further S19 forks that the matrix does not list.

## Status words

The matrix uses three terms:

- **Working:** runs in mainline Mujina today.
- **In progress:** code exists, but support is incomplete.
- **In a fork:** works, but in a fork that mainline may diverge from.

Fork support is usually on its way to mainline. Either its author is refining it for merging, or that work waits for someone to take it up.

## The matrix

| Hardware | Status | Where the code lives |
|----------|--------|----------------------|
| Bitaxe Gamma | Working | mainline |
| CPU backend (no hardware) | Working | mainline |
| EmberOne/00 | Working | mainline |
| Antminer S19j Pro, S19k Pro | In a fork | Schnitzel's fork |
| Intel BZM2 boards | In progress | johnny9's fork, `bonanza` branch |

Only the Bitaxe Gamma and the CPU backend have guides. The other rows say "none yet".

## Board notes

### Bitaxe Gamma

One BM1370 ASIC, about 1 TH/s at stock settings. Mining, hardware monitoring and the REST API are functional. The board's ESP32 runs the rhapd-bitaxe-gamma firmware, which passes the ASIC's serial bus through USB. Mujina also drives a board that still runs bitaxe-raw, the deprecated firmware that rhapd-bitaxe-gamma replaces.

The project recommends this board for a newcomer who wants real hardware. It is open source, single chip, cheap, and the board mainline development happens on.

### CPU backend

A virtual board that does software SHA-256 hashing at a few MH/s per thread. It is for development and testing, and is enabled by environment variable. See [Running Mujina](running-mujina.md).

### EmberOne/00

Twelve BM1362 ASICs. This is the 256 Foundation's open-source hashboard, a sister project to Mujina (see [Ember One](../hardware/ember-one.md)). The board's USB interface runs the EmberOne USB-serial firmware. The matrix says mainline support works today, and that the driver is being reworked and under active development.

> **Status: Disputed**
> The mujina.org compatibility matrix (current as of July 2026) lists EmberOne/00 as "Working" in mainline. The mujina GitHub README lists EmberOne00 under "Landing now", separate from its "Working now" list. The mujina.org status page says mainline support "is being reworked and is in progress". The sources do not say which is newer.

### Antminer S19j Pro and S19k Pro

BM1362-family ASICs. Support lives in Schnitzel's fork, where it powers RY3T Nova prototypes on S19 hardware. It has not been merged into mainline. Getting Mujina onto an S19's stock control board also takes a loader. Bringing this work into mainline and making it product-grade is a current focus. Until then, the matrix says running Mujina on an S19 means prototype software and an unsettled install path, not a replacement for stock firmware.

### Intel BZM2

Bonanza Mine 2 ASICs. Driver work is in progress in johnny9's fork on the `bonanza` branch. Nothing has merged into mainline.

## Forks reported on the forum

The forum threads describe S19 work that is not in the matrix:

- Skot reported the first proof of concept on 2026-05-11: Mujina running on an S19j Pro with a stock Amlogic control board. His S19j Pro work is in a fork branch named `amlogic-s19jpro`, with a separate loader project, mujina-loader.
- AgentP reported on 2026-05-30 that Mujina was working on an S19XP with an Amlogic control board. The code is in a personal fork.
- On 2026-08-05 Tyler summed it up: Schnitzel, Skot and AgentP each have their own forks of Mujina for various S19 versions, and there is no image file for easy loading yet.

Details of these ports are in [Porting Mujina to Other Miners](porting-mujina-to-other-miners.md). Xilinx-based Bitmain control boards have a separate packaging repo, covered in [Mujina Xilinx Platform](mujina-xilinx-platform.md).

## Why support lives in forks

The why-mujina page says this is how hardware support gets built. Bringing up a board means experiments that may brick hardware, fast iteration that mainline review would slow, and code that settles only once the hardware is understood. Forks are where that work moves fast. Mainline is where it merges once it settles.

## Planned hardware

- The README's near-term targets are installable images for the Antminer S19 series, the foundation's forthcoming [Libre Board](../hardware/libre-board.md) control board, and broader support for commercial mining machines.
- The first dev call listed work in progress on LibreBoard control board support, EmberOne00 v6 hashboard support, S19 support, a BZM2 chip driver and Bitaxe Bonanza board support.

## Keeping the matrix right

Rows describe work by several authors. The page asks anyone who maintains a fork or a driver to edit the page or say so in the Telegram group if a row is missing or wrong.

## See Also

- [Mujina Firmware](mujina-firmware.md)
- [Running Mujina](running-mujina.md)
- [Porting Mujina to Other Miners](porting-mujina-to-other-miners.md)
- [Mujina Xilinx Platform](mujina-xilinx-platform.md)
- [Mujina Dev Calls](mujina-dev-calls.md)
- [Ember One](../hardware/ember-one.md)
- [Libre Board](../hardware/libre-board.md)
- [Bitaxe and Open Source Miners United](../ecosystem/bitaxe-and-osmu.md)
