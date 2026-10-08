# Bitaxe Model Lineup

> Sources: Open Source Miners United (osmu.wiki, Bitaxe Models), collected 2026-10-07; Open Source Miners United (osmu.wiki, Bitaxe 100 'Max'), collected 2026-10-07; Open Source Miners United (osmu.wiki, Bitaxe 200 'Ultra'), collected 2026-10-07; Open Source Miners United (osmu.wiki, Bitaxe 400 'Supra'), collected 2026-10-07; Open Source Miners United (osmu.wiki, Bitaxe 600 'Gamma'), collected 2026-10-07; Bitaxe.org (hardware page), collected 2026-10-07; Bitaxe.org (home page), collected 2026-10-07; bitaxeorg (bitaxeMax README), collected 2026-10-07; bitaxeorg (bitaxeUltra README), collected 2026-10-07; bitaxeorg (bitaxeSupra README), collected 2026-10-07; bitaxeorg (bitaxeGamma README), collected 2026-10-07; bitaxeorg (foss-miner-list README), collected 2026-10-07
> Raw: [Bitaxe Models](../../raw/ecosystem/osmu-wiki-models.md); [Bitaxe 100 'Max'](../../raw/ecosystem/osmu-wiki-bitaxe-100.md); [Bitaxe 200 'Ultra'](../../raw/ecosystem/osmu-wiki-bitaxe-200.md); [Bitaxe 400 'Supra'](../../raw/ecosystem/osmu-wiki-bitaxe-400.md); [Bitaxe 600 'Gamma'](../../raw/ecosystem/osmu-wiki-bitaxe-600.md); [bitaxe.org hardware](../../raw/ecosystem/bitaxe-org-hardware.md); [bitaxe.org home](../../raw/ecosystem/bitaxe-org-home.md); [bitaxeMax README](../../raw/ecosystem/github-bitaxeorg-bitaxemax.md); [bitaxeUltra README](../../raw/ecosystem/github-bitaxeorg-bitaxeultra.md); [bitaxeSupra README](../../raw/ecosystem/github-bitaxeorg-bitaxesupra.md); [bitaxeGamma README](../../raw/ecosystem/github-bitaxeorg-bitaxegamma.md); [foss-miner-list README](../../raw/ecosystem/github-bitaxeorg-foss-miner-list.md)
> Updated: 2026-10-07

## Overview

The single-chip Bitaxe has gone through four main generations: Max, Ultra, Supra and Gamma. Each one moves to a newer Bitmain ASIC and keeps the same basic idea of one chip, one ESP32-S3 and Wi-Fi. This article compares the four and records where the sources disagree. For what Bitaxe is and how it relates to the 256 Foundation, see [Bitaxe and Open Source Miners United](bitaxe-and-osmu.md). Boards with more than one chip are in [Multi-Chip Bitaxe Designs](multi-chip-bitaxe-designs.md).

## Naming and numbering

Each model has a name and a board number series. The OSMU wiki titles its pages with a round number, such as Bitaxe 100 'Max' and Bitaxe 600 'Gamma'. The bitaxeorg miner list writes the same series as 10x, 20x, 40x and 60x. Individual board revisions sit inside a series: the Ultra README talks about Bitaxe Ultra 204, and the Gamma README about BitaxeGamma 600.

The OSMU wiki has a models page that presents every generation of the miner in order. Bitaxe.org describes the miner as quiet, cool and low power, something you can run at home, and labels it open source and standalone.

## Comparison

| Model | Series | ASIC | Chip comes from | Stated hashrate | Stated power |
|-------|--------|------|-----------------|-----------------|--------------|
| Max | 100 (10x) | 1x BM1397 | Antminer S17 and T17 | 250-450 giga hashes per second (OSMU wiki); in excess of 400 GH/s with cgminer on a separate computer (README) | up to 15 watts (OSMU wiki) |
| Ultra | 200 (20x) | 1x BM1366 | Antminer S19XP | 300-600 gigahashes per second (OSMU wiki) | up to 15 watts (OSMU wiki) |
| Supra | 400 (40x) | 1x BM1368 | Antminer S21 | not stated in these sources | supply should be capable of over 15W (README) |
| Gamma | 600 (60x) | 1x BM1370 | Antminer S21 Pro | about 1.2 TH/s (README) | supply must deliver in excess of 4A (20W) (README) |

The Gamma figure is an estimate in the README. It divides the Antminer S21 Pro's nominal 234 TH/s by its 195 chips. The README adds that the Gamma uses more power than earlier models and overheats more easily on the stock heatsink and fan.

Details on the chips themselves are in [Bitmain Mining ASIC Chips](mining-asic-chips.md).

## Which revision is which

The sources do not agree on how to count major revisions.

> **Status: Disputed**
> Ultra: bitaxe.org calls it the 2nd major revision; the bitaxeUltra README calls it the 3rd.
> Supra: bitaxe.org calls it the 3rd major revision; the OSMU wiki and the bitaxeSupra README call it the 4th.
> Gamma: bitaxe.org calls it the 4th major revision; the bitaxeGamma README calls it the 5th; the OSMU wiki calls it the 6th.

Bitaxe.org lists Gamma, Supra, Ultra and UltraHex under the year 2024.

## Shared board design

The Max, Ultra and Supra READMEs list almost the same parts:

- ESP32-S3-WROOM-1 Wi-Fi microcontroller.
- TI TPS40305 buck regulator that steps down the 5V input for the ASIC.
- Maxim DS4432U+ current DAC that sets the core voltage, from `0.04V` to `2.4V`.
- TI INA260 power meter for input voltage and current.
- Microchip EMC2101 for fan control and tach monitoring. On the Max it also reads the chip's internal temperature diode. The Ultra README says the BM1366 does not support die temperature, so the part is placed very close to the ASIC and its own internal sensor is used.
- A 0.91 inch SSD1306 OLED display on I2C.

The OSMU wiki describes what the Ultra's display shows across three screens: hashing speed, efficiency, accepted and rejected shares and best difficulty; fan speed, temperature, power, voltage and current; and free memory, ASIC voltage, IP address and AxeOS version.

## Power, cooling and programming

- All four READMEs call for a 5V supply. From the Ultra onward the READMEs warn that anything other than 5V DC will damage the board.
- The Max connects power with spade-style connectors. The Ultra and Supra READMEs specify a 5.5x2.5mm, center-positive barrel jack. The Gamma README specifies 5.5x2.1mm, center-positive, and says 5.5x2.5mm plugs have been known to work.
- The Gamma README says you often need a supply rated for 25-30W to hold 5V under load.
- Active cooling is mandatory. The READMEs suggest a 40x40mm heatsink with a 5V fan, a 4-pin PWM fan connector, and good thermal compound. The Gamma README warns that 12V fans spin slowly on 5V and let the board overheat.
- The Max needs an ESP-Prog programmer and a Tag Connect cable to program the ESP32. As of the Ultra, programming is done over USB-C.

## Status notes from the READMEs

- Max: v2.2 hardware has been built and tested. The README calls it an advanced build from the project's early days.
- Ultra: Bitaxe Ultra 204 hardware has been verified. The OSMU wiki calls the Ultra the currently most used model.
- Supra: the README says Bitaxe Supra 400 parts and PCBs were ordered but nothing was verified, and that the firmware did not yet support the BM1368. The README does not record a later state. Its goals and features lists still name the BM1366 in places, which looks like text carried over from the Ultra README.
- Gamma: BitaxeGamma 600 is working well and has been released, with BM1370 support added to the firmware.

The OSMU wiki notes that the Gamma has a registered GTIN-13 number, 8720892478016.

All of these boards run [AxeOS / ESP-Miner](axeos-esp-miner-firmware.md). The READMEs call each a build for experienced people and suggest buying a pre-assembled unit otherwise. See [Buying a Bitaxe](buying-a-bitaxe.md) and [Building a Bitaxe](building-a-bitaxe.md).

## See Also

- [Bitaxe and Open Source Miners United](bitaxe-and-osmu.md)
- [Multi-Chip Bitaxe Designs](multi-chip-bitaxe-designs.md)
- [Bitmain Mining ASIC Chips](mining-asic-chips.md)
- [AxeOS / ESP-Miner Firmware](axeos-esp-miner-firmware.md)
- [Buying a Bitaxe](buying-a-bitaxe.md)
- [Building a Bitaxe](building-a-bitaxe.md)
