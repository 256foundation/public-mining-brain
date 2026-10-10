# How to Build AxeOS from Source

> Source: https://osmu.wiki/axeos/compile/
> Collected: 2026-10-07
> Published: Unknown

# How to Build AxeOS from Source

This guide shows you, how you can compile AxeOS yourself. It is split into three sections for the operating systems:

## Requirements

[Section titled “Requirements”](https://osmu.wiki#requirements)

- ESP IDF
- Espressif Tool VSCode
- This firmware is designed to run a Bitaxe v2+

## 💻 Windows

[Section titled “💻 Windows”](https://osmu.wiki#-windows)

### 1. Installation

[Section titled “1. Installation”](https://osmu.wiki#1-installation)

1. Install the Espressif tool from [here](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/windows-setup.html).
On this page, you will find a “Get Started” guide for installing this onto your machine.
2. Install [Visual Studio Code](https://code.visualstudio.com/).
3. Install the [Espressif IDF Extention](https://marketplace.visualstudio.com/items?itemName=espressif.esp-idf-extension) in VSCode.

### 2. Clone repository

[Section titled “2. Clone repository”](https://osmu.wiki#2-clone-repository)

Clone the [ESP-Miner](https://github.com/bitaxeorg/ESP-Miner) repository and open it in VSCode.

### 3. Configuration

[Section titled “3. Configuration”](https://osmu.wiki#3-configuration)

After you have installed everything we need to configure the Espressif Tool.

In Visual Studio Code go to `View` → `ESP-IDF: Device Configuration` → `Device Target` → `ESP-Miner` → `esp32s3` → `ESP-S3 via USB Bridge`

### 4. Build

[Section titled “4. Build”](https://osmu.wiki#4-build)

Open an ESP-IDF terminal and cd into the `/main/http_server/axe-os/` folder because we need to build the WebUI first with:

Because the firmware needs to be built from the root directory, cd back to it and then build the firmware with:

This will generate a `build` directory at the root of the project and there you will find the `www.bin`and the `esp-miner.bin` files. These will be uploaded to your Bitaxe.

## 🍏 MacOS

[Section titled “🍏 MacOS”](https://osmu.wiki#-macos)

## 🐧 Linux

[Section titled “🐧 Linux”](https://osmu.wiki#-linux)

### 1. Installation

[Section titled “1. Installation”](https://osmu.wiki#1-installation-1)

To compile using ESP-IDF, you need to get the following packages. The command to run depends on which distribution of Linux you are using:

### 2. Get ESP-IDF

[Section titled “2. Get ESP-IDF”](https://osmu.wiki#2-get-esp-idf)

To build applications for the ESP32, you need the software libraries provided by Espressif in [ESP-IDF repository](https://github.com/espressif/esp-idf).

To get ESP-IDF, navigate to your installation directory and clone the repository with `git clone`, following instructions below specific to your operating system.

Open Terminal, and run the following commands:

ESP-IDF is downloaded into `~/esp/esp-idf`.

### 3. Set up the Tools

[Section titled “3. Set up the Tools”](https://osmu.wiki#3-set-up-the-tools)

Aside from the ESP-IDF, you also need to install the tools used by ESP-IDF, such as the compiler, debugger, Python packages, etc, for projects supporting ESP32.

### 4. Setup Environments Variables

[Section titled “4. Setup Environments Variables”](https://osmu.wiki#4-setup-environments-variables)

The installed tools are not yet added to the PATH environment variable. To make the tools usable from the command line, some environment variables must be set. ESP-IDF provides another script that does that.

In the terminal where you are going to use ESP-IDF, run:

**Note the space between the leading dot and the path!**

If you plan to use ESP-IDF frequently, you can create an alias for executing `export.sh`:

1. Copy and paste the following command to your shell’s profile (`.profile`, `.bashrc`, `.zprofile`, etc.)

1. Refresh the configuration by restarting the terminal session or by running `source [path to profile]`, for example, `source ~/.bashrc`.

Now you can run `get_idf` to set up or refresh the ESP-IDF environment in any terminal session.

### Clone repository

[Section titled “Clone repository”](https://osmu.wiki#clone-repository)

Clone the [ESP-Miner](https://github.com/bitaxeorg/ESP-Miner) repository and open it in VSCode.
