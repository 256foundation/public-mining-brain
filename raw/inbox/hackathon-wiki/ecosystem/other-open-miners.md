# PiAxe, QAxe and BitForge Nano

> Sources: Open Source Miners United (osmu.wiki, About Piaxe), collected 2026-10-07; Open Source Miners United (osmu.wiki, About Qaxe), collected 2026-10-07; Open Source Miners United (osmu.wiki, QAxe Assembly), collected 2026-10-07; Open Source Miners United (osmu.wiki, QAxe Installtion), collected 2026-10-07; Open Source Miners United (osmu.wiki, About the BitForge), collected 2026-10-07; bitaxeorg (foss-miner-list README), collected 2026-10-07
> Raw: [About Piaxe](../../raw/ecosystem/osmu-wiki-piaxe-about.md); [About Qaxe](../../raw/ecosystem/osmu-wiki-qaxe-about.md); [QAxe Assembly](../../raw/ecosystem/osmu-wiki-qaxe-assembly.md); [QAxe Installation](../../raw/ecosystem/osmu-wiki-qaxe-installation.md); [About the BitForge](../../raw/ecosystem/osmu-wiki-bitforge-bitforge.md); [foss-miner-list README](../../raw/ecosystem/github-bitaxeorg-foss-miner-list.md)
> Updated: 2026-10-07

## Overview

Three open miners documented on the OSMU wiki sit beside the Bitaxe line. The PiAxe is a mining HAT for a Raspberry Pi. The QAxe is a four-chip board that grew out of the PiAxe and the Bitaxe. The BitForge Nano is a two-chip home miner with its own firmware. The PiAxe and QAxe both depend on a separate computer running the piaxe-miner software, while the BitForge Nano is standalone like a Bitaxe.

## Comparison

| Miner | Chips | Stated hashrate | Controller | Software |
|-------|-------|-----------------|------------|----------|
| PiAxe | 1x BM1366 | ~500GH/s | Raspberry Pi | piaxe-miner |
| QAxe | 4x BM1366 | about 1.8TH/s | STM32, plus an external computer | piaxe-miner |
| BitForge Nano | 2x BM1370 | roughly 2.0 TH/s to about 2.6 TH/s | ESP32-S3-WROOM-1 | ForgeOS |

## PiAxe

The PiAxe is a HAT that plugs into a Raspberry Pi. It carries one BM1366 and is controlled over the Pi's GPIO pins. The wiki says its hashrate matches the Bitaxe Ultra.

Features listed on the wiki:

- Powered by 12V.
- A TVS diode and fuses.
- A revised buck switching regulator circuit.
- Smallest components are 0805 size, to make hand assembly easier.
- An LM75 compatible temperature sensor.
- Full compatibility with the PiAxe Miner software.

The wiki says only one build of the PiAxe exists so far, and points builders to the general PCB and assembly guides. See [Building a Bitaxe](building-a-bitaxe.md).

## QAxe

The QAxe is a quad-BM1366 miner based on the PiAxe and the Bitaxe.

**Revisions**

- rev1 is tested and runs at about 1.8TH/s average.
- rev2 reaches the expected speed after minor modifications, because its 330µF capacitors are wrongly placed.
- rev3 fixes the capacitor placement and adds a boot switch meant to put the STM32 into its DFU bootloader. The wiki says this was not yet tested.

**How it runs.** The QAxe uses an STM32 microcontroller and needs an external computer running the mining client. That client is piaxe-miner, a Python program derived from the original pyminer. It drives both the PiAxe and the QAxe.

**Flashing.** The STM32L072CB variant has a built-in DFU bootloader that starts when the BOOT button is held during reset. The firmware is then flashed over USB with dfu-utils. An older method using a CMSIS-DAP programmer, with Picoprobe firmware on a Raspberry Pi Pico, is marked deprecated. The wiki says it turned out to be a hassle for people who only want to flash the board once.

**Assembly.** The QAxe works with just 1 ASIC chip fitted. The wiki recommends working up to all four, and covering the connection pins of the empty ASIC pads before fitting a heatsink and testing.

## BitForge Nano

The BitForge Nano is an open-source, dual-chip miner for solo and home mining.

- **People.** It was developed by WantClue with the manufacturer DTV Electronics. The board is designed in Germany by WantClue Technologies and produced by DTV Electronics. The case, custom heatsink and airflow analysis came from The Solo Mining Co.
- **Chips.** Two Bitmain BM1370 ASICs. The wiki calls it one of the first dual-chip miners aimed at the home segment.
- **Controller.** An ESP32-S3-WROOM-1. It connects over Wi-Fi only, with no Ethernet port.
- **Firmware.** ForgeOS, open source, with a browser dashboard for pool configuration, monitoring and tuning.
- **Performance.** Three profiles, from roughly 2.0 TH/s in eco mode to about 2.6 TH/s in performance mode, drawing approximately 40 W. The wiki puts efficiency at around 15 J/TH.
- **Cooling.** Two 40×20 mm 12 V PWM fans feeding a custom heatsink, with measured noise around 30 dB.

## See Also

- [The Nerd Miner Family](nerd-miner-family.md)
- [Multi-Chip Bitaxe Designs](multi-chip-bitaxe-designs.md)
- [Open Mining Tools and Bitaxe Accessories](tools-and-accessories.md)
- [OSMU Wiki and the FOSS Miner List](osmu-wiki-and-foss-miner-list.md)
