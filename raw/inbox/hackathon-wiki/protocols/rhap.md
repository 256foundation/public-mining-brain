# RHAP: Raw Hardware Access Protocol

> Sources: 256 Foundation (rhap README), collected 2026-10-07; 256 Foundation (rhapd-bitaxe-gamma README), collected 2026-10-07; 256 Foundation (emberone-usbserial-fw README), collected 2026-10-07
> Raw: [rhap README](../../raw/protocols/github-256foundation-rhap.md); [rhapd-bitaxe-gamma README](../../raw/protocols/github-256foundation-rhapd-bitaxe-gamma.md); [emberone-usbserial-fw README](../../raw/hardware/github-256foundation-emberone-usbserial-fw.md)
> Updated: 2026-10-07

## Overview

RHAP, the Raw Hardware Access Protocol, gives a host program direct access to the hardware on a mining board over USB. Firmware on the board's microcontroller passes the ASIC serial bus, I2C, GPIO and ADC through two USB serial ports, and the host drives the board through them. The board does no mining of its own. This is how [Mujina](../mujina/mujina-firmware.md) can run a Bitaxe or an [Ember One](../hardware/ember-one.md) as a plain hash board.

## Two roles

- **RHAP-D, the device role.** Firmware on the board's microcontroller. It exposes the hardware and waits for commands.
- **The host role.** The program at the other end of the USB cable. It decides what the board does.

The same access serves research, testing and debugging, not only mining.

## Implementations

| Role | Project | What it is |
|------|---------|------------|
| Device | rhapd-bitaxe-gamma | Firmware for the Bitaxe Gamma |
| Device | emberone-usbserial-fw | Firmware for the EmberOne hash board |
| Host | Mujina | Open source Bitcoin mining software |
| Host | emberone-miner | Python miner for EmberOne testing |
| Host | emberone-test-scripts | EmberOne bring-up and test scripts |

## Status of the specification

The `rhap` repository holds the protocol specification and client libraries. The specification is not written yet. Until it is, the rhapd-bitaxe-gamma README is the description of the protocol. The `rhap` repository is licensed under the Mozilla Public License 2.0.

## How the protocol works

A RHAP device shows up as two serial ports.

- **Data serial** is the second port. It is a pass-through to the ASIC UART. All data passes in both directions, and the USB baud rate is mirrored on the output.
- **Control serial** is usually the first port. It carries small command packets. Baud rate does not matter.

### Command packets

Every control command has the same layout:

| Byte | Field | Meaning |
|------|-------|---------|
| 0, 1 | Length, low byte then high byte | Number of bytes in the whole packet |
| 2 | ID | Any byte the host picks. It comes back in the response |
| 3 | Bus | Always `0x00` |
| 4 | Page | Which subsystem the command is for |
| 5 | Command | Depends on the page |
| 6 onward | Data | Variable length |

Pages shared by both device firmwares:

| Page | Value | Commands |
|------|-------|----------|
| I2C | `0x05` | write `0x20`, read `0x30`, readwrite `0x40`. Data is the I2C address, the bytes to write, and the number of bytes to read |
| GPIO | `0x06` | One command per pin. Data is the pin level |
| ADC | `0x07` | read VDD `0x50`, read VIN `0x51` |

### Response packets

The Bitaxe Gamma README documents the reply format. Every command except System produces a response. It carries the length, the echoed command ID, a status code, and then data. If the command could not be parsed, the ID is `0xFF`.

| Status code | Meaning |
|-------------|---------|
| `0x00` | Success. Data holds the response payload |
| `0x10` | Timeout |
| `0x11` | Invalid command |
| `0x12` | Buffer overflow |
| `0xFF` | Error with message. Data holds ASCII text |

## RHAP-D for the Bitaxe Gamma

This firmware runs on the ESP32-S3 of the Bitaxe Gamma. It displaces the stock firmware, esp-miner. It continues bitaxe-raw, the original implementation of what became RHAP. bitaxe-raw covers several boards. This repository targets only one.

Behaviour at startup:

- The ASIC is held in reset through the RST_N GPIO.
- The TPS546 core voltage rail is turned off.
- Both steps keep heat and power low until a host connects and is ready.
- The display shows the firmware name, the commit it was built from, and the serial number.

It adds a **System** page, `0x09`, with two commands: reboot, and reboot to bootloader. Each needs a four-byte magic payload. That guards against an accidental reboot from line noise or a framing desync. No response is sent. The host sees success when the USB device re-enumerates.

Its GPIO page lists one pin, RST_N.

### Building and flashing

The build needs rustup and the `just` command runner.

- `just setup-tools` installs the Xtensa-capable Rust toolchain and the flashing tool.
- `just build` builds the firmware.
- `just flash` flashes it. If the board already runs RHAP-D, the recipe reboots it into the bootloader by itself, with no buttons pressed. A board running anything else must be put into the bootloader by hand: hold the `BOOT` button while attaching power.
- `just checks` runs rustfmt and clippy before a commit.

## RHAP-D on the Ember One

The Ember One firmware runs on the board's RP2040. It uses the same packet layout and the same I2C and ADC pages. The differences from the Bitaxe Gamma firmware, as documented:

- GPIO has three pins: ASIC reset, ASIC power enable, and ASIC IO power enable. Leaving out the data byte reads the current level.
- There is an **LED** page, `0x08`, with one command to set an RGB colour.
- Its README does not list a System page or a response format.

See [Ember One Hardware Details](../hardware/ember-one-hardware.md) for the board itself.

## See Also

- [Mujina Firmware](../mujina/mujina-firmware.md)
- [Ember One](../hardware/ember-one.md)
- [Ember One Hardware Details](../hardware/ember-one-hardware.md)
- [Bitaxe and Open Source Miners United](../ecosystem/bitaxe-and-osmu.md)
