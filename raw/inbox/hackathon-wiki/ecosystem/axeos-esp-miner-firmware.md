# AxeOS / ESP-Miner Firmware

> Sources: Open Source Miners United (osmu.wiki, About AxeOS (ESP-Miner)), collected 2026-10-07; Open Source Miners United (osmu.wiki, How to Build AxeOS from Source), collected 2026-10-07; Open Source Miners United (osmu.wiki, How to install AxeOS on a BitAxe), collected 2026-10-07; bitaxeorg (ESP-Miner README), collected 2026-10-07; bitaxeorg (bitaxe-web-flasher README), collected 2026-10-07
> Raw: [About AxeOS](../../raw/ecosystem/osmu-wiki-axeos-about.md); [Build AxeOS from Source](../../raw/ecosystem/osmu-wiki-axeos-compile.md); [Install AxeOS on a BitAxe](../../raw/ecosystem/osmu-wiki-axeos-install-onto-bitaxe.md); [ESP-Miner README](../../raw/ecosystem/github-bitaxeorg-esp-miner.md); [bitaxe-web-flasher README](../../raw/ecosystem/github-bitaxeorg-bitaxe-web-flasher.md)
> Updated: 2026-10-07

## Overview

ESP-Miner is the open-source ESP32 firmware that runs the Bitaxe. Its web interface is called AxeOS, and the OSMU wiki uses the name AxeOS for the whole package. The firmware tells the ESP microcontroller how to talk to the mining ASIC and hosts a configuration page on the device, so the miner is controlled and monitored from a web browser. It is maintained by OSMU. This article covers what it is, how to install it, and how to build it. Its HTTP interface is in [AxeOS API](axeos-api.md).

## What it runs on

The OSMU wiki says the firmware is designed for a Bitaxe v2+. The README adds a hardware limit: only the ESP32-S3-WROOM-1 module of type N16R8 is supported. Modules without PSRAM, or with Quad SPI PSRAM, do not work with the normal firmware.

Forks exist for other boards, such as the Nerd family and the Hex boards. See [The Nerd Miner Family](nerd-miner-family.md) and [Multi-Chip Bitaxe Designs](multi-chip-bitaxe-designs.md).

## Installing

There are three routes in the sources.

**Prebuilt images.** The ESP-Miner releases page holds premade images. A factory image resets the board to factory settings, and it must match the hardware version.

**Bitaxetool.** A command line Python tool for flashing a Bitaxe and updating its config. It installs through pip.

- It requires Python 3.4 or later and pip.
- It does not work properly with esptool v5.x.x. The README says esptool v4.9.0 or earlier is required, and that Bitaxetool v0.6.1 is locked to esptool v4.9.0.
- It can flash a factory image, flash only the NVS config, or flash both. Settings in the config file overwrite the config baked into the factory image.

**Web flasher.** The Bitaxe Web Flasher is an open-source tool for flashing a factory file from the browser. You connect the device, select the model and board version, and click flash. It can also be built and run locally with Docker.

### Steps in the OSMU wiki guide

1. Connect the Bitaxe to a PC by USB. Boards without USB need a serial link through a JTAG ESP-Prog device or a USB-to-UART bridge.
2. Install Bitaxetool with pip.
3. Prepare a config file. Starting with v2.0.0, the firmware needs basic manufacturing data flashed into the NVS partition. The values to set are `asicfrequency`, `asicvoltage`, `asicmodel`, `devicemodel` and `boardversion`. All values must be present for the flash to work.
4. Download the latest firmware from the releases page, or compile it, and flash it together with the config file.

The wiki names the config file `config.cvs`. The README uses `.csv` files from a `configs` directory, one per hardware version, plus `configs/config-custom.csv` for a custom board. A custom board must be based on an existing `devicemodel` and `asicmodel`.

### Linux flashing errors

The wiki lists `Permission denied`, `Failed to connect`, `The port is busy or doesn't exist` and `bitaxetool: command not found`. If the tool lacks permission to open the port, run it with `sudo`. If `sudo` then cannot find the command, the tool is probably installed in a virtual environment, and the current environment's PATH has to be passed through to `sudo`.

### Other install notes from the README

- Some Bitaxe versions cannot connect directly to a USB-C port. A USB-A adapter is the workaround.
- Inside a dev container, run Bitaxetool from outside the container, or the device is not found.

## Building from source

**Requirements.** The ESP-IDF toolchain, plus nodejs/npm for the web interface. The ESP-IDF extension for VSCode is optional in the README and part of the wiki's Windows route. The project uses git submodules, so clone with `--recursive`.

**OSMU wiki route.** The guide has Windows, MacOS and Linux sections; the MacOS section is empty. On Windows: install the Espressif tool, Visual Studio Code and the Espressif IDF extension, clone ESP-Miner, set the device target to `esp32s3`, then build. On Linux: install the distribution's packages, clone ESP-IDF into `~/esp/esp-idf`, install its tools, and set the environment variables with its export script. The guide builds the web interface first, from the `/main/http_server/axe-os/` folder, then the firmware from the project root. The result is a `build` directory with `www.bin` and `esp-miner.bin`.

**README route.** Run `idf.py build` at the root, then the `merge_bin.sh` script. The script merges the bootloader, partition table and application binary into a single file.

**Docker route.** The repository has a dev container. You build a Docker image once, then compile inside it, so the ESP-IDF toolchain does not have to be installed on the computer.

## Unified firmware

The README describes a change the wiki guide does not mention. Starting with the unified firmware releases, the AxeOS frontend is compiled, gzipped and embedded in the application binary `esp-miner.bin`. A separate `www.bin` is no longer needed for standard use.

- A custom frontend is still possible. Enable the custom web UI option in settings and upload a `www.bin`. It is served from the SPIFFS partition and takes priority over the built-in interface.
- If a device is stuck on an old custom frontend, disable it from the recovery page or by setting `useCustomWWW` to 0 through the API.
- Rolling back to pre-unified firmware leaves the `www` partition untouched. The old firmware serves whatever is in it, so a mismatched interface may need a matching `www.bin` flashed by hand.

## Administration

- The firmware hosts a small web server on port 80. Reach it at the device's LAN IP address, or at `http://bitaxe` if the network supports mDNS.
- A recovery page lives at `/recovery`, for when the normal interface is unreachable, for example after a failed custom web UI update.
- The input fields for ASIC frequency and core voltage are locked by default. Appending `?oc` to the settings tab URL unlocks them. The README warns that overclocking without extra cooling can overheat or damage the Bitaxe.

## mDNS discovery

The firmware registers itself on the local network so devices can be found without knowing their IP address.

- The hostname is registered as `<hostname>.local`. The default hostname is `bitaxe`.
- The HTTP service is advertised as `_http._tcp`, with an AxeOS subtype `_axeos._sub._http._tcp` for finding AxeOS devices specifically.
- TXT records carry board version, family, ASIC model, ASIC count and firmware version.
- If two devices want the same hostname, a suffix derived from the MAC address is appended.
- Swarm mode accepts both IP addresses and `.local` hostnames.

## Wi-Fi routers that block mining

The README says some routers block mining, naming ASUS routers and some TP-Link routers. If the miner shows no hash rate, check the router settings and disable AiProtection and IoT. If that does not help, check the Stratum host and port on the Bitaxe.

## See Also

- [AxeOS API](axeos-api.md)
- [Bitaxe Model Lineup](bitaxe-models.md)
- [Building a Bitaxe](building-a-bitaxe.md)
- [Mujina Firmware](../mujina/mujina-firmware.md)
