# The Nerd Miner Family

> Sources: Open Source Miners United (osmu.wiki, About Nerdminer), collected 2026-10-07; Open Source Miners United (osmu.wiki, About NerdNOS), collected 2026-10-07; Open Source Miners United (osmu.wiki, About NerdAxe), collected 2026-10-07; Open Source Miners United (osmu.wiki, About NerdQAxe+), collected 2026-10-07; Open Source Miners United (osmu.wiki, About NerdQAxe++), collected 2026-10-07; bitaxeorg (foss-miner-list README), collected 2026-10-07
> Raw: [About Nerdminer](../../raw/ecosystem/osmu-wiki-nerdminer-about.md); [About NerdNOS](../../raw/ecosystem/osmu-wiki-nerdnos-about.md); [About NerdAxe](../../raw/ecosystem/osmu-wiki-nerdaxe-about.md); [About NerdQAxe+](../../raw/ecosystem/osmu-wiki-nerdqaxeplus-about.md); [About NerdQAxe++](../../raw/ecosystem/osmu-wiki-nerdqaxeplusplus-about.md); [foss-miner-list README](../../raw/ecosystem/github-bitaxeorg-foss-miner-list.md)
> Updated: 2026-10-07

## Overview

The Nerd projects are a family of small open-source miners with a screen. They start with the Nerdminer, which mines on a bare ESP32, and grow into boards that pair the Nerdminer display with Bitaxe-style ASIC hardware. The OSMU wiki gives each one the same stated goal: a free and open source project that lets you try to reach a bitcoin block with a small piece of hardware, learn about mining, and have a nice object on your desk.

## Comparison

| Project | Chips | Stated hashrate | Stated power | Built on |
|---------|-------|-----------------|--------------|----------|
| Nerdminer | none; the ESP32 itself mines | not given | not given | HAN Miner |
| NerdNOS | BM1397 | up to 150~200 GH/s | about 8W | attachment board for the Nerdminer |
| NerdAxe | BM1366 | up to 500GH/s | not given | Bitaxe Ultra |
| NerdQAxe+ | four chips; see below | up to 2.5TH/s | not given | QAxe+ board |
| NerdQAxe++ | four BM1370 | up to 4.8 TH/s | approximately 60 watts | QAxe++ board |

## Nerdminer

Nerdminer is an implementation of the Stratum protocol for the ESP32, made to mine on a solo pool. By default it points at [Public Pool](public-pool.md), and this can be changed. It was first developed on the ESP32-S3 and now supports other boards too.

- Settings are changed through WifiManager and saved on the device.
- It uses both cores to mine, with several threads handling stratum work and Wi-Fi.
- When a new stratum job arrives it switches to the new work, so it does not create stale shares.
- It has three screens: one for its own mining data, a clock, and one for global mining stats.

## NerdNOS

NerdNOS is an attachment board that adds a BM1397, the chip known from the Bitaxe Max, to a Nerdminer. The chip is heavily underclocked to keep the power draw low.

Setup, in short:

1. Power it from a USB port and wait for the Wi-Fi message on the display.
2. Join the device's own Wi-Fi network from a phone or PC. A WiFiManager page opens.
3. Choose your Wi-Fi network, enter your on-chain Bitcoin address in place of the placeholder text, set the time zone offset, and save.
4. Check the connection by looking up your address on the pool.

Button 1 switches screens on a short press, lets you change existing entries if held while plugging in power, and resets all saved entries if held for 5 seconds. Button 2 turns the display on and off while mining continues. The firmware can be installed with the Bitaxe web flasher.

## NerdAxe

NerdAxe combines the Nerdminer display with the Bitaxe Ultra. It uses a Lilygo T-Display S3 and a modified Bitaxe Ultra board, and talks to the ASIC over the GPIO pins. It runs a modified version of AxeOS called ESP-Miner-NerdAxe. The bitaxeorg miner list names two variants, a NerdAxe Ultra with 1x BM1366 and a NerdAxe Gamma with 1x BM1370.

## NerdQAxe+ and NerdQAxe++

Both use the Lilygo T-Display S3 with a modified four-chip QAxe board, and both run ESP-Miner-NerdQAxePlus, a modified version of AxeOS.

The NerdQAxe++ uses four BM1370 chips from the Antminer S21 series. The wiki describes it as compact, quiet and one of the most energy-efficient home miners available.

> **Status: Disputed**
> NerdQAxe+ chip: the OSMU wiki says the NerdQAxe+ uses four BM1366 chips. The bitaxeorg miner list gives the NerdQAxe+ as 4x BM1368, and lists a separate NerdQAxe with 4x BM1366.

## Larger variants in the miner list

The bitaxeorg miner list adds entries the wiki does not cover:

- NerdQAxe++ rev.7, also 4x BM1370.
- NerdOCTAXE-Plus with 8x BM1368.
- NerdOCTAXE-Gamma with 8x BM1370.

The list says ESP-Miner-NerdQAxePlus targets the NerdQAxe+, NerdQAxe++ and the Octaxe boards.

## See Also

- [Public Pool](public-pool.md)
- [PiAxe, QAxe and BitForge Nano](other-open-miners.md)
- [AxeOS / ESP-Miner Firmware](axeos-esp-miner-firmware.md)
- [Bitaxe Model Lineup](bitaxe-models.md)
