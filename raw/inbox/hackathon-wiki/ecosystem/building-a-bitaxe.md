# Building a Bitaxe: PCBs, Assembly and FAQ

> Sources: Open Source Miners United (osmu.wiki, Building PCBs), collected 2026-10-07; Open Source Miners United (osmu.wiki, Assembly), collected 2026-10-07; Open Source Miners United (osmu.wiki, FAQ), collected 2026-10-07; bitaxeorg (bitaxeGamma README), collected 2026-10-07; Open Source Miners United (osmu.wiki, Bitaxe 100 'Max'), collected 2026-10-07
> Raw: [Building PCBs](../../raw/ecosystem/osmu-wiki-tips-building-pcbs.md); [Assembly](../../raw/ecosystem/osmu-wiki-tips-assembly.md); [FAQ](../../raw/ecosystem/osmu-wiki-tips-faq.md); [bitaxeGamma README](../../raw/ecosystem/github-bitaxeorg-bitaxegamma.md); [Bitaxe 100 'Max'](../../raw/ecosystem/osmu-wiki-bitaxe-100.md)
> Updated: 2026-10-07

## Overview

Because the design files are public, you can have Bitaxe boards made and solder them yourself. The OSMU wiki has three pages of practical help: how to produce the files a PCB shop needs, how to reflow a board in a toaster oven, and a short FAQ on hashrate problems, overclocking and safe operating ranges. The same pages are the reference for other OSMU boards such as the PiAxe and QAxe. Building takes much longer than buying and needs strong SMD soldering skills. To buy one instead, see [Buying a Bitaxe](buying-a-bitaxe.md).

## Getting PCBs made

A PCB manufacturer usually needs two things: Gerbers and drill files. If a shop will also assemble the boards, it needs a bill of materials and a centroid (XY) file as well.

Gerbers are a set of files in a standard format, usually one per board layer. The wiki uses KiCad because it is open source and free, and walks through the export in KiCad v6:

1. Open the design and switch to the PCB editor.
2. Choose File, Fabrication Outputs, Gerbers.
3. Tick the layers to include: front and back copper, the two inner copper layers, front and back paste, front and back silkscreen, front and back soldermask, and the edge cuts layer that defines the board outline.
4. Generate the drill files from the same plot screen, using the options the PCB shop asks for.

The paste layers are only for making solder paste stencils. They are not needed to manufacture the board itself. The wiki recommends ordering stencils. The section on files for assembly houses is still marked TBD.

The Gamma README adds ordering details for that board:

- PCBs are 4-layer, with 6mil trace/space and 0.3mm holes. 1oz outer and 0.5oz inner copper works well.
- Gerbers are in the repository's manufacturing files directory.
- Order stencils, one for the top and one for the bottom.
- Every part except the ASIC is available from DigiKey and others.

## Reflow assembly in a toaster oven

The assembly page describes a hand method.

**Equipment**

- A convection toaster oven. Never use it for food afterwards.
- A thermocouple thermometer whose probe can go to ~300C.
- Sn63/Pb37 no-clean leaded solder paste, kept in the refrigerator. It stencils better cold. Wash your hands after handling it.
- Tweezers, and a microscope for inspection.

**Steps**

1. Stencil the paste. Take your time. If it goes wrong, wipe it off with IPA and try again.
2. Place all parts on the pasted board with tweezers.
3. Put the board in the oven with the thermocouple held just above it.
4. Soak: heat on the convection bake setting until the thermometer reads 140C, then hold 140-150C for 2 minutes.
5. Reflow: turn the heat to high. When it reaches 200C, start a timer for 30 seconds and keep the temperature between 200 and 220C. The paste should all melt.
6. Turn the oven off, open the door and let the boards cool.
7. Inspect under a microscope for dry pads and bridges. Fix them with paste flux, solder braid and a soldering iron.

For a board with parts on both sides, repeat the steps for the second side. Surface tension almost always holds the first side's parts in place while upside down. Use a small metal stand to keep them off the oven rack.

## Extra hardware for a complete miner

From the Gamma README: a heatsink and a 5V fan, good thermal compound, an OLED display, a 5V power supply and a stand. Active cooling is required; the heatsink alone is not enough. Model-by-model details are in [Bitaxe Model Lineup](bitaxe-models.md).

## FAQ

### The Bitaxe is not hashing at the expected rate

The wiki's steps, in order:

1. Physically disconnect and reconnect power. A restart through the UI is not enough.
2. Check for overheating. Firmware v2.3 or later shows temperature warnings.
3. Check the frequency and voltage settings, and reset them to defaults if needed.
4. Confirm the input voltage is in range.
5. If overclocking, the voltage may need to rise to match the frequency.
6. As a last resort, reflash the firmware.

### Safe operating ranges

| Measure | Range |
|---------|-------|
| Input voltage | 4.8-5.3v |
| ASIC temperature | Below 70°C |
| Voltage regulator | Below 90°C |

### Overclocking

The wiki warns that overclocking can permanently damage the device. If you do it:

- Watch the dashboard values and stay inside the ranges above.
- Leave a safety margin for changes in room temperature.
- Make sure the power supply is adequate. Input voltage dropping below the range means insufficient power, and a higher-rated supply may be needed.
- Upgrade the heatsink and thermal paste first.

### Firmware across boards

The same update cannot be used on a Bitaxe, a Hex and a TinyChip board. Each has its own repository and updates. See [AxeOS / ESP-Miner Firmware](axeos-esp-miner-firmware.md).

### Where to get help

The wiki points to the OSMU Discord.

## See Also

- [Bitaxe Model Lineup](bitaxe-models.md)
- [Buying a Bitaxe](buying-a-bitaxe.md)
- [AxeOS / ESP-Miner Firmware](axeos-esp-miner-firmware.md)
- [PiAxe, QAxe and BitForge Nano](other-open-miners.md)
