# QAxe Installtion

> Source: https://osmu.wiki/qaxe/installation/
> Collected: 2026-10-07
> Published: Unknown

# QAxe Installtion

# Installation

[Section titled “Installation”](https://osmu.wiki#installation)

The QAxe does use a STM32 and requires an external computer to run the [PyMiner Software](https://github.com/shufps/piaxe-miner).

# Compilation

[Section titled “Compilation”](https://osmu.wiki#compilation)

# Installation via USB Bootloader on board with BOOT button

[Section titled “Installation via USB Bootloader on board with BOOT button”](https://osmu.wiki#installation-via-usb-bootloader-on-board-with-boot-button)

The STM32L072CB variant has an integrated DFU Bootloader that starts when pressing the BOOT button during reset.

Afterwards the firmware can be flashed via dfu-utils:

# Flashing

[Section titled “Flashing”](https://osmu.wiki#flashing)

After the source was compiled it is flashed by:

## Deprecated

[Section titled “Deprecated”](https://osmu.wiki#deprecated)

### Installation via CMSIS-DAP Programmer

[Section titled “Installation via CMSIS-DAP Programmer”](https://osmu.wiki#installation-via-cmsis-dap-programmer)

note: Using CMSIS-DAP and PicoProbe has been turned out to be quite a hassle for people who just want to flash the STM32 once, it’s suggested to use the USB bootloader with the STM32 L072CB variant.

As programming/debug adapter the Picoprobe firmware running on a Raspi Pico works best:
[https://github.com/rp-rs/rp2040-project-template/blob/main/debug\_probes.md](https://github.com/rp-rs/rp2040-project-template/blob/main/debug_probes.md) / [https://github.com/raspberrypi/picoprobe/releases/tag/picoprobe-cmsis-v1.0.3](https://github.com/raspberrypi/picoprobe/releases/tag/picoprobe-cmsis-v1.0.3)

There also is a little board with only 3 parts that gives a nice low-cost solution to flash the Qaxe:
[https://github.com/shufps/raspi-pico-dap](https://github.com/shufps/raspi-pico-dap)

On rev3 there should be the option to boot the stm32 (by pressing the boot-button on reset) into DFU-Bootloader mode what makes flashing via USB and without CMSIS-DAP programmer possible.
