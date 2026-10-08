# Ember One Hardware Details

> Sources: 256 Foundation (emberone.org home page), collected 2026-10-07; 256 Foundation (emberone00-pcb README), collected 2026-10-07; 256 Foundation (emberone01-pcb README), collected 2026-10-07; 256 Foundation (emberone-usbserial-fw README), collected 2026-10-07; 256 Foundation (Hydra Pool hardware tests page), collected 2026-10-07
> Raw: [emberone.org home](../../raw/hardware/emberone-org-home.md); [emberone00-pcb README](../../raw/hardware/github-256foundation-emberone00-pcb.md); [emberone01-pcb README](../../raw/hardware/github-256foundation-emberone01-pcb.md); [emberone-usbserial-fw README](../../raw/hardware/github-256foundation-emberone-usbserial-fw.md); [Hydra Pool hardware tests](../../raw/hydrapool/hydrapool-org-hardware-tests-html.md)
> Updated: 2026-10-07

## Overview

This article covers the hardware side of the Ember One hash board: the standard specification, the emberOne/00 board built on the Bitmain BM1362, which chip variants work, the roadmap for other ASICs, the onboard USB-serial controller, and the design files. For what Ember One is and why it exists, see [Ember One](ember-one.md).

## The standard board

The project site lists these features for every Ember One:

- Power consumption of ~100W.
- Input voltage range of 12-24vdc.
- USB-C data communication.
- On-board temperature sensors.
- A 125mm x 125mm form factor.

Each six-month grant cycle is meant to bring a new version for a different ASIC chip. All versions fit the same form factor. The goal is interchangeable parts: a user can run one hash board or several, and can pick which ASIC they want.

A hash board does not run on its own. It needs a separate control board connected over USB. The site says support is coming in [Libre Board](libre-board.md), and firmware support is coming in [Mujina](../mujina/mujina-firmware.md).

## emberOne/00

The emberOne/00 is the first version. Its README calls it a 100W open source hash board.

- It is based on the BM1362 from the Bitmain Antminer S19j Pro.
- The README says it should reach about 3.5 TH/s.
- The [Hydrapool hardware tests](../hydrapool/hydrapool-hardware-tests.md) table lists Ember One 00 on test firmware at 3 Th/s and 33.3 J/Th.

The board can be built by hand. The README says this is difficult but possible with minimal equipment and patience, and points to assembly tips in the repository.

### Which BM1362 chips work

| Variant | Status per the README |
|---------|-----------------------|
| BM1362AA, AB, AC, AD | Use these |
| BM1362AI, BD | Might work, untested |
| BM1362AJ, AK | Will not work |

### Early firmware

Before Mujina support, testing used emberOne support hacked into a PiAxe/Pyminer fork. That fork lives in the `skot/emberone-miner` repository.

## emberOne/01 and the roadmap

The site lists planned future versions: an Intel BZM2 ASIC version, an Auradine ASIC version, and a Proto Mining ASIC version.

A second PCB repository exists, `emberone01-pcb`. As collected, its README is the same text as the emberOne/00 README. It still carries the emberOne/00 heading and still describes the BM1362. The raw sources do not say which chip emberOne/01 uses.

## The onboard USB-serial controller

Each board carries an RP2040 microcontroller that acts as the board management controller. Its firmware is in the `emberone-usbserial-fw` repository and is written in Rust.

When plugged in, the board shows up as two serial ports:

- **Control serial** (usually the first port). It carries I2C, GPIO, ADC and LED commands. Baud rate does not matter.
- **Data serial** (the second port). It passes the ASIC UART straight through in both directions. The USB baud rate is mirrored on the output.

Through the control port the host can:

- Read and write I2C devices.
- Drive three GPIO lines: ASIC reset (active low), ASIC power enable and ASIC IO power enable (both active high).
- Read the VDD and VIN voltages through the ADC.
- Set the colour of the onboard LED.

This is the device side of the [Raw Hardware Access Protocol](../protocols/rhap.md). That article explains the packet format.

The firmware can be flashed over SWD with `probe-rs`, or as a UF2 image made with `elf2uf2-rs`.

## Design files and license

The PCB is designed in KiCad, a free and open-source PCB CAD tool. The README invites people to fork, hack and release. The project site links the words open-source to the CERN-OHL-S license.

> **Status: Disputed**
> The emberone.org home page links the board's license to CERN-OHL-S. The existing [Ember One](ember-one.md) article, compiled from the 256 Foundation projects page, describes the design as GPL-licensed. Both claims are kept until a source settles it.

## People

The site names @skot9000 as lead engineer and @econoalchemist as project manager.

## See Also

- [Ember One](ember-one.md)
- [Libre Board](libre-board.md)
- [Libre Board Design and Grant Scope](libre-board-design.md)
- [RHAP: Raw Hardware Access Protocol](../protocols/rhap.md)
- [Hydrapool Hardware Tests](../hydrapool/hydrapool-hardware-tests.md)
