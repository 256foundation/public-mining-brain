# How to install AxeOS on a BitAxe

> Source: https://osmu.wiki/axeos/install-onto-bitaxe/
> Collected: 2026-10-07
> Published: Unknown

# How to install AxeOS on a BitAxe

This page will guide you through the process of installing AxeOS onto your Bitaxe.

## 1. Connect your BitAxe to your PC

[Section titled “1. Connect your BitAxe to your PC”](https://osmu.wiki#1-connect-your-bitaxe-to-your-pc)

If you don’t have a BitAxe with USB connectivity make sure to establish a serial connection with either a JTAG ESP-Prog device or a USB-to-UART bridge.

Otherwise, just plug your BitAxe into your PC with a USB-cable

## 2. BitAxeTool

[Section titled “2. BitAxeTool”](https://osmu.wiki#2-bitaxetool)

OSMU built [BitAxeTool](https://github.com/johnny9/bitaxetool) to make the installation process very easy. You can install it onto your system through pip. If you do not have pip installed, check this [guide](https://pip.pypa.io/en/stable/installation/).

Run in your terminal:

## 3. Pre-Configuration

[Section titled “3. Pre-Configuration”](https://osmu.wiki#3-pre-configuration)

Starting with v2.0.0, the AxeOS firmware requires some basic manufacturing data to be flashed in the NVS partition.

Create a file called `config.cvs` and copy the content of [this file](https://github.com/bitaxeorg/ESP-Miner/blob/master/config.cvs.example) into it. You have to modify

- `asicfrequency`
- `asicvoltage`
- `asicmodel`
- `devicemodel`
- and `boardversion`.

The following are recommendations but you must have all values in your `config.cvs` file to flash properly.

Save the file, we need it in the next step.

## 4. Flash

[Section titled “4. Flash”](https://osmu.wiki#4-flash)

Download the latest firmware from the [release page](https://github.com/bitaxeorg/ESP-Miner/releases) or [compile it yourself](https://osmu.wiki/axeos/compile). It should look like `esp-miner-factory-vX.X.X.bin`. Now you can finally flash your BitAxe! To do so type into a system terminal:

before executing the command replace

- `{path-to-config}` with the path to the config file from the [previous step](https://osmu.wiki#3-pre-configuration)
- `{path-to-firmware}` with the path to the firmware you downloaded or compiled

BitAxeTool should now flash your BitAxe successfully.

## 5. Linux Troubleshooting

[Section titled “5. Linux Troubleshooting”](https://osmu.wiki#5-linux-troubleshooting)

On Linux, you may encounter a few errors when trying to flash with BitAxeTool, depending on how you installed the tool. These include:

- `Permission denied`
- `Failed to connect`
- `The port is busy or doesn't exist`
- `bitaxetool: command not found`

Example command:

Example output:

In the above scenario, BitAxeTool does not have permission to access the port. To fix this, run the command again with `sudo`, e.g.:

BitAxeTool should now flash your BitAxe successfully.

If you encounter the error `sudo: bitaxetool: command not found`, it’s likely that you have installed BitAxeTool in a virtual environment, using Conda, etc. The root (sudo) user may not find your command because the PATH environment variable for the root does not include the directory where BitAxeTool is located.

To resolve this, you can specify that you want to use the current environment’s ‘PATH’ with sudo:

Example command:

Output example of successful flash:
