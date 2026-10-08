# Bitaxe 600 'Gamma'

> Source: https://osmu.wiki/bitaxe/600/
> Collected: 2026-10-07
> Published: Unknown

# Bitaxe 600 'Gamma'

## What is this?

[Section titled “What is this?”](https://osmu.wiki#what-is-this)

Gamma is the 6th major revision of the bitaxe that now includes the BM1370 ASIC from the Antminer S21Pro.

## 🛠️ Hardware

[Section titled “🛠️ Hardware”](https://osmu.wiki#️-hardware)

- The BM1370 is a undocumented SHA256 mining ASIC from Bitmain. It’s used in the Antminer S21Pro
- Bitmain claims the BM1370 has 15 J/TH efficiency
- The BM1370 is brand new and isn’t available anywhere yet.
- The BM1370 has a similar footprint and pinout from the BM1368 in previous bitaxe.

## Software

[Section titled “Software”](https://osmu.wiki#software)

1. Building your Software 
  - You can build your own binary files from the source code. For more details follow this [Build-Guide](https://osmu.wiki/axeos/compile).
2. Using a prebuild 
  - Every Bitaxe is controlled by the open source available [ESP-Miner](https://github.com/bitaxeorg/ESP-Miner) software. It features a WebUi for user friendly usage and controlablility.
  - In this repository you will also find a [releases](https://github.com/bitaxeorg/ESP-Miner/releases) page that will contain prebuild binary files to flash to your Bitaxe using the [Bitaxetool](https://github.com/johnny9/bitaxetool) created by [johnny9](https://github.com/johnny9).
3. Flashing Process 
  - The [ESP-Miner](https://github.com/bitaxeorg/ESP-Miner) Software can be flashed via a USB cable onto the Bitaxe. Therefore you need to follow the initial Guide in the repository.

The Bitaxe Gamma does have an officialy registerd GTIN-13 Number. The code is the following: 8720892478016.

The GTIN-13 Number Document can be viewed [here](https://osmu.wiki/doc-assets/bitaxe/GTIN-Gamma.pdf).
