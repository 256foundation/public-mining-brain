# Open Mining Tools and Bitaxe Accessories

> Sources: Open Source Miners United (osmu.wiki, About Antsniffer), collected 2026-10-07; Open Source Miners United (osmu.wiki, About Bitcrane), collected 2026-10-07; bitaxeorg (bitaxe-raw README), collected 2026-10-07; Open Source Miners United (osmu.wiki, About Bitaxe Accessories Port), collected 2026-10-07; Open Source Miners United (osmu.wiki, BitHalo), collected 2026-10-07; bitaxeorg (BitaxeGT README), collected 2026-10-07; bitaxeorg (BitaxeGammaHex README), collected 2026-10-07; bitaxeorg (bitaxeBIRDS README), collected 2026-10-07
> Raw: [About Antsniffer](../../raw/ecosystem/osmu-wiki-antsniffer-about.md); [About Bitcrane](../../raw/ecosystem/osmu-wiki-bitcrane-about.md); [bitaxe-raw README](../../raw/ecosystem/github-bitaxeorg-bitaxe-raw.md); [Bitaxe Accessories Port](../../raw/ecosystem/osmu-wiki-bitaxe-bap.md); [BitHalo](../../raw/ecosystem/osmu-wiki-bitaxe-bithalo.md); [BitaxeGT README](../../raw/ecosystem/github-bitaxeorg-bitaxegt.md); [BitaxeGammaHex README](../../raw/ecosystem/github-bitaxeorg-bitaxegammahex.md); [bitaxeBIRDS README](../../raw/ecosystem/github-bitaxeorg-bitaxebirds.md)
> Updated: 2026-10-07

## Overview

Besides complete miners, the OSMU community publishes tools for studying mining hardware and add-ons for the Bitaxe. Three are development tools: Antsniffer taps the cable inside an Antminer, Bitcrane drives an Antminer hashboard from a computer, and bitaxe-raw turns a Bitaxe into a USB bridge to its own ASIC. Two are accessory items: the Bitaxe Accessories Port, a connector on the board, and BitHalo, a light board.

## Development tools

### Antsniffer

Antsniffer taps the signals on an Antminer data cable so they can be read with a logic analyzer or used for other development work. The data cable is the one that connects a hashboard to the control board.

- The base design is a 2 layer PCB.
- It has 2 SMD connectors compatible with Antminer 18 pin data cables.
- Every data connection is broken out to a pin header, labelled with its function.
- Two switches are included. One resets the control board and the other resets the plug state of the miner.

### Bitcrane

Bitcrane is a tool for sending bytes to an Antminer hashboard over USB. It also controls fans and the power supply. It is built on the FTDI FT4232HQ.

It is meant for exploring and developing alternative Antminer firmware. The wiki is clear that it is not a drop-in control board replacement. It can be used with mining software such as piaxe-miner running on a PC or a Raspberry Pi, or with firmware you write yourself.

### bitaxe-raw

bitaxe-raw is firmware for the ESP32-S3 on Bitaxe boards. Instead of mining, it passes the ASIC UART, the board's I2C bus, GPIO and ADC through over USB serial. The README says it is for research, testing and debugging. It is written in Rust and flashed with the espflash tools.

How it behaves once connected:

- It creates two serial ports. The first is usually the control port, for I2C, GPIO and ADC. The second is the data port, a pass-through to the ASIC UART in both directions.
- On the data port the USB serial baud rate is mirrored on the output. On the control port the baud rate does not matter.
- After startup the ASIC is held in reset to limit heat and power until the host is ready. The host releases it by setting the `RST_N` line high through the control port.
- Control packets carry a length, a command id that is echoed in the response, a bus byte, a page byte that selects I2C, GPIO or ADC, a command and optional data.
- I2C supports write, read and readwrite. ADC commands read the `VDD` and `VIN` values.

Two practical notes: espflash does not restart the ESP32 after flashing, so press the `RESET` button. To change firmware again later, hold the `BOOT` button while attaching power to enter the bootloader.

A branch called bitaxe-raw-pico gives preliminary support for the Raspberry Pi Pico on the BIRDS board. See [Intel BZM2 Designs: BIRDS and Bonanza](intel-bzm2-designs.md).

## Accessories

### Bitaxe Accessories Port (BAP)

The BAP is a serial port that lets accessories talk to the ESP32 on a Bitaxe board. It sits on the top side of the board.

- It includes four serial ports, so several accessories can be connected at once, such as extra sensors or displays.
- It has a 5V power pin and a ground pin, so external devices can be powered from the board.
- Accessories must be compatible with the 5V supply the port provides.

The Gamma Turbo and the bitaxeorg Gamma Hex READMEs list a 12V version of the port. See [Multi-Chip Bitaxe Designs](multi-chip-bitaxe-designs.md).

### BitHalo

The OSMU wiki calls BitHalo the first add-on ever released for the Bitaxe. It is a light board with side-emitting LEDs, designed and made by TheSoloMiningCo, that reacts to what the miner is doing.

- While loading it shows a rotating purple effect.
- Each time a share is submitted it gives an orange pulse that flashes and fades out from all edges.
- It signals a found block as well.
- A switch on the rear turns the lighting off.

It was designed for the 201-204 series of Bitaxe boards. The wiki says it will be updated to follow newer Bitaxe releases.

## See Also

- [Bitaxe Model Lineup](bitaxe-models.md)
- [PiAxe, QAxe and BitForge Nano](other-open-miners.md)
- [Intel BZM2 Designs: BIRDS and Bonanza](intel-bzm2-designs.md)
- [Bitmain Mining ASIC Chips](mining-asic-chips.md)
