# Intel BZM2 Designs: BIRDS and Bonanza

> Sources: bitaxeorg (bitaxeBIRDS README), collected 2026-10-07; bitaxeorg (bitaxeBonanza README), collected 2026-10-07
> Raw: [bitaxeBIRDS README](../../raw/ecosystem/github-bitaxeorg-bitaxebirds.md); [bitaxeBonanza README](../../raw/ecosystem/github-bitaxeorg-bitaxebonanza.md)
> Updated: 2026-10-07

## Overview

Two bitaxeorg boards use Intel's BZM2 mining ASIC instead of a Bitmain chip. BIRDS is a four-chip board meant for BZM2 firmware development. Bonanza is an eight-chip board that its own README says does not work. Neither is a finished miner. Both are hardware experiments for people who want to work on the chip.

## BIRDS

BIRDS stands for Bitaxe Intel Reference Design System. The README calls it an untested prototype and says not to build it expecting it to work out of the box.

**Chips**

- Four Intel BZM2 ASICs, powered in series.
- Each BZM2 is nominally 0.7V, with approx 350 GH/s @ 1.15 GHz hash frequency.
- The chips have on-chip digital temperature and voltage sensors, and support ntime rolling.

**Power and cooling**

- 11-13V input on an XT30 connector.
- A TPS546D24S single-phase voltage regulator tuned for 2.8V output @ 20A. Its backside power plane is exposed, in the hope of bonding it thermally to the main heatsink.
- A new fan control strategy that drops the EMC2101 used on earlier Bitaxe boards.

**Controller**

- BIRDS does not use an ESP32. It is controlled by a Raspberry Pi Pico 2W, which has the RP2350 microcontroller and an Infineon CYW43439 Wi-Fi chip.
- The Pico's programmable IO handles the BZM2's serial link, which the README describes as 5Mbaud and 9bit.
- Preliminary firmware support comes from bitaxe-raw-pico, a branch of bitaxe-raw. It targets the RP2040 in the original Pico, which is pin compatible with the RP2350-based Pico 2.

**Licence and files**

The design is under an open hardware licence, with KiCad design files. Gerbers are deliberately not provided, to discourage low-quality copies. The author offers help generating them from KiCad.

## Bonanza

The Bonanza README is two lines. The board has eight Intel BZM2 ASICs. It notes that the design does not work because of one open issue in its repository, and might never work because of another.

## See Also

- [Multi-Chip Bitaxe Designs](multi-chip-bitaxe-designs.md)
- [Bitmain Mining ASIC Chips](mining-asic-chips.md)
- [Open Mining Tools and Bitaxe Accessories](tools-and-accessories.md)
