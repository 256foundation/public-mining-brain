# Hardware Compatibility | Mujina

> Source: https://mujina.org/reference/hardware-compatibility
> Collected: 2026-10-07
> Published: Unknown

# Hardware Compatibility [](https://mujina.org#hardware-compatibility)

Mujina aims to run any hashboard from any vendor. Mujina is not ported to a board: a driver for the board is added to Mujina, and the shared core does the rest. Drivers arrive board by board. Some live outside the main repository, in forks. This matrix records where each board stands.

Status vocabulary, used consistently below:

- **Working**: runs in mainline Mujina today.
- **In progress**: code exists, but support is incomplete.
- **In a fork**: works, but in a fork that mainline may diverge from.

Fork support is usually on its way to mainline: either its author is refining it for merging, or that refining waits for someone to take it up.

## Matrix [](https://mujina.org#matrix)

| Hardware | Status | Where the code lives | Guide | 
|---|---|---|---|
| Bitaxe Gamma | Working | [mainline](https://github.com/256foundation/mujina) | [setup guide](https://mujina.org/howto/set-up-a-bitaxe-gamma) | 
| CPU backend (no hardware) | Working | [mainline](https://github.com/256foundation/mujina) | [the tutorial](https://mujina.org/tutorial/first-run) | 
| EmberOne/00 | Working | [mainline](https://github.com/256foundation/mujina) | none yet | 
| Antminer S19j Pro, S19k Pro | In a fork | [Schnitzel's fork](https://github.com/Schnitzel/mujina) | none yet | 
| Intel BZM2 boards | In progress | [johnny9's fork](https://github.com/johnny9/mujina/tree/bonanza) | none yet | 

## Board notes [](https://mujina.org#board-notes)

### Bitaxe Gamma [](https://mujina.org#bitaxe-gamma)

One BM1370 ASIC, about 1 TH/s at stock settings. Mining, hardware monitoring, and the REST API are functional. The board's ESP32 runs the [rhapd-bitaxe-gamma](https://github.com/256foundation/rhapd-bitaxe-gamma) firmware, which passes the ASIC's serial bus through USB. Mujina also drives a board that still runs [bitaxe-raw](https://github.com/bitaxeorg/bitaxe-raw), the deprecated firmware rhapd-bitaxe-gamma replaces. [Set Up a Bitaxe Gamma](https://mujina.org/howto/set-up-a-bitaxe-gamma) covers flashing the firmware and starting the miner.

For a newcomer who wants real hardware, this is the board to start with: open source, single chip, cheap, and the one mainline development happens on.

### CPU backend [](https://mujina.org#cpu-backend)

A virtual board: software SHA-256 hashing at a few MH/s per thread, for development and testing. Enabled by environment variable; see [Environment Variables](https://mujina.org/reference/environment-variables).

### EmberOne/00 [](https://mujina.org#emberone-00)

Twelve BM1362 ASICs. The 256 Foundation's open source hashboard, a sister project to Mujina. The board's USB interface runs the [EmberOne USB-serial](https://github.com/256foundation/emberone-usbserial-fw) firmware. Mainline support works today. The driver is being reworked and under active development.

### Antminer S19j Pro, S19k Pro [](https://mujina.org#antminer-s19j-pro-s19k-pro)

BM1362-family ASICs. Support lives in [Schnitzel's fork](https://github.com/Schnitzel/mujina), where it powers RY3T Nova prototypes on S19 hardware; it has not been merged into mainline. Getting Mujina onto an S19's stock control board also takes a loader; approaches are collected in [this forum thread](https://forum.256foundation.org/t/best-practices-for-hacking-mujina-onto-other-miners/48).

Bringing this work into mainline and making it product-grade is a current focus. Until then, running Mujina on an S19 means prototype software and an unsettled install path, not a replacement for stock firmware.

### Intel BZM2 [](https://mujina.org#intel-bzm2)

Bonanza Mine 2 ASICs. Driver work is in progress in [johnny9's fork](https://github.com/johnny9/mujina/tree/bonanza), on the `bonanza` branch; nothing has merged into mainline.

## Corrections [](https://mujina.org#corrections)

This page is current as of July 2026. Rows describe work by several authors, and the authors know it best: if you maintain a fork or a driver and your row is missing or wrong, [edit this page](https://github.com/256foundation/mujina-website) or say so in the [Telegram group](https://t.me/the256foundation).
