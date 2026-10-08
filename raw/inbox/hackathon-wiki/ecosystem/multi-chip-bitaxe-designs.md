# Multi-Chip Bitaxe Designs

> Sources: Open Source Miners United (osmu.wiki, Bitaxe 300 'Hex'), collected 2026-10-07; Open Source Miners United (osmu.wiki, Bitaxe 650 'Gamma Duo'), collected 2026-10-07; Open Source Miners United (osmu.wiki, Bitaxe 801 'Gamma Turbo'), collected 2026-10-07; bitaxeorg (ultraHex README), collected 2026-10-07; bitaxeorg (BitaxeGT README), collected 2026-10-07; bitaxeorg (BitaxeGammaHex README), collected 2026-10-07; bitaxeorg (bitaxeNaja README), collected 2026-10-07; bitaxeorg (naja-duo README), collected 2026-10-07; bitaxeorg (foss-miner-list README), collected 2026-10-07; Bitaxe.org (hardware page), collected 2026-10-07
> Raw: [Bitaxe 300 'Hex'](../../raw/ecosystem/osmu-wiki-bitaxe-300.md); [Bitaxe 650 'Gamma Duo'](../../raw/ecosystem/osmu-wiki-bitaxe-650.md); [Bitaxe 801 'Gamma Turbo'](../../raw/ecosystem/osmu-wiki-bitaxe-801.md); [ultraHex README](../../raw/ecosystem/github-bitaxeorg-ultrahex.md); [BitaxeGT README](../../raw/ecosystem/github-bitaxeorg-bitaxegt.md); [BitaxeGammaHex README](../../raw/ecosystem/github-bitaxeorg-bitaxegammahex.md); [bitaxeNaja README](../../raw/ecosystem/github-bitaxeorg-bitaxenaja.md); [naja-duo README](../../raw/ecosystem/github-bitaxeorg-naja-duo.md); [foss-miner-list README](../../raw/ecosystem/github-bitaxeorg-foss-miner-list.md); [bitaxe.org hardware](../../raw/ecosystem/bitaxe-org-hardware.md)
> Updated: 2026-10-07

## Overview

Several Bitaxe designs put more than one ASIC on a board. They range from two chips (Gamma Duo, Gamma Turbo, Naja) to six (the Hex boards). They keep the ESP32-S3 controller and run ESP-Miner or a fork of it, but most move from a 5V input to 12V. Some are released, some are unfinished, and the Naja boards are untested prototypes. The single-chip models are covered in [Bitaxe Model Lineup](bitaxe-models.md).

## Summary

| Design | Series | Chips | State in the sources |
|--------|--------|-------|----------------------|
| Hex / UltraHex | 300 (30x) | 6x BM1366 | unfinished; one revision is described as working |
| Gamma Duo | 650 (65x) | two chips from the S21 lineup | described as a revision of the Gamma |
| Gamma Turbo (GT) | 801 (80x) | 2x BM1370 | first release |
| Gamma Hex | 130x | 6x BM1370 | design published |
| Naja | not given | dual BM1340 | untested prototype |
| Naja Duo | not given | dual BM1373 | untested prototype |

## Hex / UltraHex

The Hex puts six BM1366 chips from the Antminer S19XP on one board. Bitaxe.org calls it a multichip revision of the Bitaxe Ultra. The OSMU wiki calls it a prototype concept and gives a hashrate of roughly 2.7 ~ 3 TH/s.

> **Status: Disputed**
> Power: the OSMU wiki gives a wall power consumption of roughly about 60 watts. The ultraHex README says power draw is around 50W @12V. The two may be measured at different points.

Hardware in the README:

- ESP32-S3-WROOM-1 controller.
- TI TPS546D24ARVFR buck regulator that steps the 12V input down for the chain of chips.
- TMP1075 sensors for inlet and outlet board temperature.
- Microchip EMC2302 controlling dual fans.
- 12V DC input on screw terminals. The supply should be capable of 100W.
- At least one 80x80mm 12V 4-pin fan, and an enclosure that forces air through the heatsink.

The README opens with a warning that the board is unfinished and may have hardware and firmware bugs. Its revision list:

- V300 and V301 do not work. Both have power supply faults.
- V302 is described as the current working version.
- v303 improves the layout.
- v304 is the latest revision but has too little bulk capacitance on the Vcore regulator output. The workaround is to add a couple of 180 uF capacitors.

Two more notes from the README: overclocking does not raise the hash rate on this board, it only adds heat; and a pre-release board should be ordered with 2 oz. copper on internal and external layers. The README says anyone without board-building experience should build a single-chip Bitaxe first.

Firmware is ESP-Miner-multichip, a fork of ESP-Miner for boards with several ASICs.

## Gamma Duo

The OSMU wiki describes the Gamma Duo as a revision of the Bitaxe Gamma that reuses low-performing chips from the S21 lineup instead of discarding them.

> **Status: Disputed**
> Chip name: the OSMU wiki page describes the chip as the BM1370. The bitaxeorg miner list gives the Gamma Duo as 2x BM1370XP.

## Gamma Turbo (GT)

The Gamma Turbo is a dual BM1370 board. The README says its first release marks the version 801, and that it is the first dual-chip variant and the first multi-chip device with modern ASIC hardware. Listed features:

- Dual BM1370 ASIC and dual TPS546 regulators.
- A 12V accessory port (BAP).
- EMC2103 fan controller.
- Improved mounting hole selection.

It is licensed under CERN-OHL-2-S.

## Gamma Hex

The bitaxeorg Gamma Hex, named Bitaxe Gamma Hex 1300 in its README, uses six BM1370 chips. Listed features:

- A 1.9 inch color LCD for mining stats.
- ESP32-S3 controller with full ESP-Miner support.
- 12V input on a 6-pin molex connector.
- The six chips arranged as 2 domains of 3 ASICs each.
- A four phase TPS546D24S voltage regulator with adjustable output and live telemetry.
- A 12V Bitaxe Accessory Port.
- EMC2103 fan controller and dual ASIC temperature monitor.

It is designed in KiCad and licensed under CERN-OHL-2-S.

The bitaxeorg miner list also names two six-chip boards from TinyChipHub in a 70x series: a Supra Hex with 6x BM1368 and a Gamma Hex with 6x BM1370. They use their own firmware, ESP-Miner-TCH.

## Naja and Naja Duo

Both are dual-chip boards using ESP-Miner, built around chips linked to the Antminer S23 series.

- BitaxeNaja uses two BM1340 chips. The README says the BM1340 is suspected to be a prototype version of the S23 chip.
- BitaxeNajaDuo uses two BM1373 chips, suspected to be the chip used in the S23 series.

Both READMEs say the board is an untested prototype and should not be built expecting it to work. The Naja Duo README states the CERN Open Hardware Licence Version 2 - Strongly Reciprocal.

## See Also

- [Bitaxe Model Lineup](bitaxe-models.md)
- [Bitmain Mining ASIC Chips](mining-asic-chips.md)
- [Intel BZM2 Designs: BIRDS and Bonanza](intel-bzm2-designs.md)
- [AxeOS / ESP-Miner Firmware](axeos-esp-miner-firmware.md)
- [Open Mining Tools and Bitaxe Accessories](tools-and-accessories.md)
