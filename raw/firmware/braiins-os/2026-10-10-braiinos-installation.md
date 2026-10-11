# Installation — Braiins OS (Braiins Academy)

> Registry ID: braiins-os
> Source: https://academy.braiins.com/braiins-os/installation/install (markdown captured via /braiins-os/installation/install.md llms route)
> Collected: 2026-10-10
> Published: n/d (docs site build 2026-10-02, sitemap lastmod 2026-10-04)
> Posture: verbatim
> As-Of: 2026-10-10

# Installation

## Install Braiins OS on S21 or S19 Series

### Installation via Braiins Toolbox

The preferred method for installing Braiins OS is by using the [Braiins Toolbox](/braiins-toolbox/introduction/index.md). This tool allows for remote batch installations on all the Antminer S21 and S19 series control boards: Zynq/Xilinx, Amlogic, BeagleBone Black, and Cvitek/CV1835.

### SD Card Installation

Braiins OS can be also run on Antminers from the S19 series using **Zynq**(Xilinx) or **BeagleBone Black** control boards with a flashed SD card. You will require a Micro SD card with a minimum capacity of 128 MB. Please avoid using cards with capacities greater than 8 GB. The speed or class of the SD card is not relevant.

- [Download](https://drive.google.com/drive/folders/1BNnomhiHJgcGqdMSnoFdPs18pozsVKWW) the provided SD image.

- Flash the image from a PC (with [`BalenaEtcher`](https://www.balena.io/etcher/), [`Rufus`](https://rufus.ie/en/), or `dd`)


_Note: Simple copy to SD card will not work. The SD card has to be flashed!_

- Insert the SD card into the miner. The miner can be powered-on while doing this.

- After inserting the SD card, power-up or reboot the miner. The miner will automatically boot Braiins OS from the SD card.


_Note: The internal memory is kept intact and Braiins OS does not alter it in any way. After the SD card is removed,
the stock firmware will boot, with all the previous settings._

- Enter the miner with a web browser (search its IP with `AngryIP` or `Nmap`)

## Install Braiins OS on S17 Series

In order to use Braiins OS, you will need Micro SD card with at least 128 MB capacity. Do not use cards with capacity greater than 8 GB. The speed / class of the SD card is irrelevant.

- Download the provided SD image: [x17 Zynq/Xilinx/7007 (23.01)](https://drive.google.com/drive/folders/1a3Oz-8UqSuKxx3Rv2NrEtBwkgShR3mFi)
- Flash the image from a PC (with [`BalenaEtcher`](https://www.balena.io/etcher/), [`Rufus`](https://rufus.ie/en/), or `dd`)


_Note: Simple copy to SD card will not work. The SD card has to be flashed!_

- Insert the SD card into the miner. The miner can be powered-on while doing this.

- After inserting the SD card, power-up or reboot the miner. The miner will automatically boot Braiins OS from the SD card.


_Note: The internal memory is kept intact and Braiins OS does not alter it in any way. After the SD card is removed,
the stock firmware will boot, with all the previous settings._

- Enter the miner with a web browser (search its IP with `AngryIP` or `Nmap`)

### Install to NAND (Optional)

- Install to NAND from (System > Status >) System > Install to NAND (Only v23.01 or earlier with x17 control boards).

## Install Braiins OS on S9, S9i, S9j

### Run From SD card

![S9 jumpers](/static/image/S9-Jumpers.783ae0f2af.png)
In order to use Braiins OS, you will need Micro SD card with at least 128 MB capacity. Do not use cards with capacity greater than 8 GB. The speed / class of the SD card is irrelevant.

- Download the provided SD image: [S9, S9j, S9i Zynq/Xilinx (22.08.1)](https://drive.google.com/drive/folders/1HSWCoHGiV81ASeOtdmrZhL9fIG85YdeR)
- Flash the image from a PC (with [`BalenaEtcher`](https://www.balena.io/etcher/), [`Rufus`](https://rufus.ie/en/), or `dd`)


_Note: Simple copy to SD card will not work. The SD card has to be flashed!_

- Change the jumper to the **BOOT FROM SD** mode to boot from SD

- Insert the SD card into the miner. The miner can be powered-on while doing this.

- After inserting the SD card the miner will automatically boot Braiins OS from the SD card.


_Note: The internal memory is kept intact and Braiins OS does not alter it in any way. After the SD card is removed,
the stock firmware will boot, with all the previous settings._

- Enter the miner with a web browser (search its IP with `AngryIP` or `Nmap`)

### Install to NAND (Optional)

- Download the provided SD image: [S9, S9j, S9i Zynq/Xilinx (22.08.1)](https://drive.google.com/drive/folders/1HSWCoHGiV81ASeOtdmrZhL9fIG85YdeR)
- Flash the image from a PC (with [`BalenaEtcher`](https://www.balena.io/etcher/), [`Rufus`](https://rufus.ie/en/), or `dd`)


_Note: Simple copy to SD card will not work. The SD card has to be flashed!_

- Change the jumper to the **BOOT FROM SD** mode to boot from SD
- Insert the SD card into the miner. The miner can be powered-on while doing this.
- After inserting the SD card the miner will automatically boot Braiins OS from the SD card.


_Note: The internal memory is kept intact and Braiins OS does not alter it in any way. After the SD card is removed,
the stock firmware will boot, with all the previous settings._

- Navigate to menu System > Install the current system to NAND

- Wait for the process to be completed

- Turn off the device and revert back the jumper to the **BOOT FROM NAND** mode and take out the sd card.

- Turn on the device.

- Enter the miner with a web browser (search its IP with `AngryIP` or `Nmap`)


---

Was this helpful?

Yes, thanks!Sort of, thanks!Not really

Talk to us!
