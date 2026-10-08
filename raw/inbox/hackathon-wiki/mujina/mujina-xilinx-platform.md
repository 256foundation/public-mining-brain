# Mujina Xilinx Platform

> Sources: 256 Foundation (mujina-xilinx-platform GitHub README), collected 2026-10-07; 256 Foundation (mujina GitHub README), collected 2026-10-07; Mujina project (mujina.org status page, current as of July 2026), collected 2026-10-07; 256 Foundation forum (Mujina-Antminer), 2026-05-11
> Raw: [mujina-xilinx-platform README](../../raw/mujina/github-256foundation-mujina-xilinx-platform.md); [mujina README](../../raw/mujina/github-256foundation-mujina.md); [mujina.org status](../../raw/mujina/mujina-org-explanation-status.md); [Mujina-Antminer thread](../../raw/mujina/2026-05-11-forum-mujina-antminer.md)
> Updated: 2026-10-07

## Overview

mujina-xilinx-platform is a 256 Foundation repository that packages [Mujina](mujina-firmware.md) for Bitmain miners whose control board uses a Xilinx Zynq-7007S. These boards lock the bootloader and kernel with RSA keys burned into eFuses, so neither can be replaced. The repo works around this by keeping the stock kernel and swapping only the ramdisk, which the bootloader checks with a plain SHA256 hash. It is a Buildroot project. The mining software itself stays in the main mujina repository.

## The constraint

Xilinx control boards have RSA authentication permanently enabled in eFuses. The consequence is that BOOT.bin (the bootloader) and the kernel cannot be replaced. Only the ramdisk can be customized.

## The workaround

The boot chain is FSBL, FPGA bitstream, U-Boot, kernel, then ramdisk. The first four are RSA verified. The ramdisk is verified by SHA256 only, against a signature partition named mtd3. If both the ramdisk and its stored hash are updated, custom firmware boots.

The README notes that no private RSA key is needed, and that other open-source miner firmware projects use the same method.

## NAND flash layout

| Partition | Size | Content | What the install does |
|-----------|------|---------|-----------------------|
| mtd0 | 40MB | BOOT.bin and kernel | Preserved |
| mtd1 | 32MB | ramdisk.itb | Replaced |
| mtd2 | 8MB | configs | Untouched |
| mtd3 | 2MB | signatures | Patched |
| mtd4 | 171MB | reserve | Untouched |

Inside mtd3, offset 0-1023 holds the kernel signature (RSA, not modified). Offset 1024 to 1279 holds the ramdisk signature, which is the part updated.

## Install steps

The script `scripts/bitmain_ramdisk_install.sh` automates a first install from Bitmain firmware:

1. Compute the SHA256 hash of the custom ramdisk.
2. Build a 256-byte signature: the SHA256 (32 bytes) plus zero padding (224 bytes).
3. Upload the ramdisk, signature and NAND tools to the miner.
4. Erase mtd1 and write the custom ramdisk.
5. Dump mtd3, patch bytes 1024 to 1279, and write it back.
6. Verify with MD5 checksums.
7. Reboot.

The script's comments say it unlocks sudo via daemonc first. A second script, `scripts/mujina_ramdisk_update.sh`, updates an existing Mujina install and assumes root access is already set up.

> **Status: Disputed**
> The mujina-xilinx-platform README describes a first-time install that "Unlocks sudo via daemonc". In the Mujina-Antminer forum thread (2026-06-17), Skot wrote that the daemonc exploit used to get root on stock Bitmain firmware "was blocked with a firmware update sometime mid-2025". Skot was writing about Amlogic control boards, and the README is undated, so it is not clear whether the Xilinx install still works on recent stock firmware.

## Building the image

- The build system is Buildroot, used through a BR2_EXTERNAL tree, with mainline Buildroot as a git submodule.
- `make xilinx_ramdisk_defconfig` then `make` produces `buildroot/output/images/ramdisk.itb`, a FIT image of about 10MB.
- A first build takes 15-30 minutes on a 16-core desktop.
- By default the build downloads a pre-built `mujina` binary from GitHub Releases. The other option builds from a local mujina checkout and needs the Rust toolchain.
- `make mujina-rebuild` rebuilds only the mujina package.

Key build settings:

- Architecture: ARM Cortex-A9.
- Toolchain: Linaro GCC 7.2-2017.11, chosen for ABI compatibility with the stock kernel.
- Kernel headers: 4.6.x, for kernel module compatibility.
- Optimized for size, with LTO enabled.
- Root filesystem: ext2, 32MB max, gzip compressed, wrapped in a FIT image.
- Packages are minimal: busybox, dropbear, i2c-tools, mtd-utils and gdb.
- One patch disables `getrandom()` in Dropbear to avoid blocking at boot.

## Stock kernel modules

The stock kernel is 4.6.0-xilinx-g03c746f7 and is RSA-signed. Custom modules cannot be compiled without an exact match of kernel source and toolchain, so two modules are extracted from stock firmware:

- `bitmain_axi.ko` gives FPGA register access through `/dev/axi_fpga_dev`.
- `fpga_mem_driver.ko` gives FPGA memory mapping through `/dev/fpga_mem`.

An init script, `S10modules`, runs early in boot. It detects the RAM size (256MB or 512MB) and loads the modules with the matching memory offset.

## Serial console

The console needs a USB-to-TTL adapter at 3.3V logic. The README warns not to use 5V and not to connect the VCC pin. Wire GND to GND and cross RX and TX. Settings are 115200 baud, 8N1, no flow control.

## How this fits the rest of Mujina

Pull requests for packaging go to this repo. Pull requests for mining software (ASIC communication, mining protocol, hardware control, pool connectivity) go to the mujina repo.

> **Status: Disputed**
> The mujina-xilinx-platform README calls itself a "Production packaging system" and by default downloads a pre-built `mujina` binary from GitHub Releases. Its post-install steps run `mujina --version` and `mujina start`. The mujina.org status page (current as of July 2026) says "There are no prebuilt images" and that installing on a stock control board "is an unsettled problem". The main mujina README names the binaries `mujina-minerd` and `mujina-cli`, not `mujina`. The Xilinx README is undated and may describe an earlier or planned state.

The README does not name any miner model. The forum work on S19 machines so far has been on Amlogic control boards. See [Porting Mujina to Other Miners](porting-mujina-to-other-miners.md).

## See Also

- [Mujina Firmware](mujina-firmware.md)
- [Porting Mujina to Other Miners](porting-mujina-to-other-miners.md)
- [Mujina Hardware Compatibility](hardware-compatibility.md)
- [Libre Board](../hardware/libre-board.md)
