# RHAP (Raw Hardware Access Protocol)

> Sources: 256foundation/rhap and rhapd-bitaxe-gamma READMEs (captured 2026-10-07); bitaxeorg/bitaxe-raw README, issues and PRs, 2025-04 → 2026-09; 256foundation/emberone-usbserial-fw README and PRs, 2025-03 → 2026-03; 256foundation/mujina docs and PRs, 2026-08 → 2026-10; Assembling Freedom newsletter, 2025-05-05
> Raw: [256foundation/rhap README](../../raw/protocols/harvest/github-256foundation-rhap.md); [rhapd-bitaxe-gamma README](../../raw/protocols/harvest/github-256foundation-rhapd-bitaxe-gamma.md); [bitaxe-raw README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxe-raw.md); [emberone-usbserial-fw README](../../raw/hardware/256f-hardware/github-256foundation-emberone-usbserial-fw.md); [Mujina: bitaxe-raw PROTOCOL.md](../../raw/firmware/mujina/github-mujina-mujina-miner-src-mgmt-protocol-bitaxe-raw-prot.md); [Mujina PR #107](../../raw/firmware/mujina/2026-08-30-github-mujina-pr-107-feat-bitaxe-support-the-rhap-d-firmware.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

RHAP, the Raw Hardware Access Protocol, lets a host program drive a mining board's hardware directly over USB. Firmware on the board's microcontroller takes the device role, called **RHAP-D**. It does no mining of its own. It passes the ASIC serial bus, I2C, GPIO and ADC through two USB serial ports, and a host such as [Mujina](../firmware/mujina.md) does the work: it schedules jobs, reads sensors and sets voltages and fans ([rhap README](../../raw/protocols/harvest/github-256foundation-rhap.md); [rhapd-bitaxe-gamma README](../../raw/protocols/harvest/github-256foundation-rhapd-bitaxe-gamma.md)). This is how a Bitaxe Gamma or an Ember One works as a "dumb" USB hashboard under a Linux miner. The protocol started in April 2025 as **bitaxe-raw**, a research firmware for the Bitaxe's ESP32-S3. The Ember One's RP2040 firmware (**emberone-usbserial-fw**) uses the same framing. In September 2026 the Bitaxe Gamma implementation moved to **rhapd-bitaxe-gamma** under the RHAP name. The RHAP repository holds client libraries and is MPL 2.0 licensed. As of the 2026-10-07 capture its formal specification was not yet written, and the rhapd-bitaxe-gamma README serves as the reference ([rhap README](../../raw/protocols/harvest/github-256foundation-rhap.md)).

## Implementations

| Role | Implementation | Runs on | Notes |
|---|---|---|---|
| Device (RHAP-D) | rhapd-bitaxe-gamma | Bitaxe Gamma ESP32-S3 | Successor to bitaxe-raw. Covers one board only ([rhapd README](../../raw/protocols/harvest/github-256foundation-rhapd-bitaxe-gamma.md)) |
| Device (RHAP-D) | emberone-usbserial-fw | Ember One RP2040 board-management controller | Adds an LED page ([emberone-usbserial-fw README](../../raw/hardware/256f-hardware/github-256foundation-emberone-usbserial-fw.md)) |
| Device (predecessor) | bitaxe-raw | ESP32-S3 on Bitaxe-series boards | Deprecated for the Gamma. The `bitaxeProto` and `bonanza` board branches remain active ([bitaxe-raw PR #19](../../raw/hardware/bitaxe-osmu/2026-09-26-github-bitaxe-raw-pr-19-docs-retire-main-in-favor-of-rhapd-b.md)) |
| Host | Mujina | Linux, macOS, Windows | Drives both bitaxe-raw and RHAP-D boards ([Mujina Bitaxe Gamma doc](../../raw/firmware/mujina/github-mujina-mujina-miner-src-board-bitaxe-gamma.md)) |
| Host | emberone-miner | Python | Miner for Ember One testing ([rhap README](../../raw/protocols/harvest/github-256foundation-rhap.md)) |
| Host | emberone-test-scripts | Python | Ember One bring-up and test scripts ([rhap README](../../raw/protocols/harvest/github-256foundation-rhap.md)) |

Some features stay on the host side by design. When a Stratum V2 grantee offered to integrate SV2 into the Ember One USB firmware in January 2025, he concluded that it belonged in Mujina, because the USB firmware only serves the hashboard ([emberone-usbserial-fw #1](../../raw/hardware/256f-hardware/2025-01-30-github-emberone-usbserial-fw-issue-1-stratum-v2.md)).

## USB layout: two CDC ACM ports

Every RHAP-D board enumerates as a composite USB device with two CDC ACM serial ports:

- **Control serial** is the first port, normally `/dev/ttyACM0`. It carries framed packets for I2C, GPIO and ADC, plus LED and System commands where supported. Its baud rate does not matter.
- **Data serial** is the second port, normally `/dev/ttyACM1`. It passes the ASIC UART through raw in both directions. The board mirrors whatever baud rate the host sets on the USB side onto the physical UART ([rhapd README](../../raw/protocols/harvest/github-256foundation-rhapd-bitaxe-gamma.md); [Mujina Bitaxe Gamma doc](../../raw/firmware/mujina/github-mujina-mujina-miner-src-board-bitaxe-gamma.md)).

Mujina finds and claims both ports itself, so users never open them by hand ([mujina.org: set up a Bitaxe Gamma](../../raw/firmware/mujina/github-mujina-website-howto-set-up-a-bitaxe-gamma.md)). The Bonanza Bridge is an exception to the baud mirroring: the physical link from the ESP32 to the Bridge stays at a fixed 2 Mbaud while USB clients may set any baud rate. A client setting of 5 Mbaud worked ([bitaxe-raw PR #18](../../raw/hardware/bitaxe-osmu/2026-07-25-github-bitaxe-raw-pr-18-update-bitaxebonanza-raw-for-bridge.md)).

### USB identifiers

Hosts tell boards and protocol versions apart by VID:PID, product string and bcdDevice:

| Firmware | VID:PID | Product / manufacturer | Source |
|---|---|---|---|
| bitaxe-raw (Gamma) | `c0de:cafe` | "Bitaxe" / "OSMU" | [bitaxe-raw #14](../../raw/hardware/bitaxe-osmu/2026-07-01-github-bitaxe-raw-issue-14-control-cdc-acm-endpoint-not-drai.md) |
| bitaxe-raw (Bonanza branch) | — | `BitaxeBonanza` | [bitaxe-raw PR #18](../../raw/hardware/bitaxe-osmu/2026-07-25-github-bitaxe-raw-pr-18-update-bitaxebonanza-raw-for-bridge.md) |
| rhapd-bitaxe-gamma | `1209:6102` (the Bitaxe project's pid.codes allocation) | "Bitaxe Gamma RHAP-D" | [Mujina PR #107](../../raw/firmware/mujina/2026-08-30-github-mujina-pr-107-feat-bitaxe-support-the-rhap-d-firmware.md) |
| emberone-usbserial-fw | `1209:256f` (pid.codes allocation to the Ember One project; replaced the `0xc0de:0xcafe` placeholder, merged 2026-02-18) | — | [emberone-usbserial-fw PR #16](../../raw/hardware/256f-hardware/2026-02-06-github-emberone-usbserial-fw-pr-16-feat-usb-use-pid-codes-vi.md) |
| Stock AxeOS (ESP-Miner), for contrast | `303a:1001` | "USB JTAG/serial debug unit" by Espressif | [Mujina PR #39](../../raw/firmware/mujina/2026-03-07-github-mujina-pr-39-feat-transport-implement-macos-usb-disco.md) |

- **Windows:** Windows reports "Microsoft" as the manufacturer for CDC ACM devices, so Mujina's Windows port matches Bitaxes by VID:PID instead ([Mujina PR #75](../../raw/firmware/mujina/2026-06-15-github-mujina-pr-75-feat-transport-add-native-windows-suppor.md)).
- **Ember One bcdDevice:** the major number is the hardware revision. Minor.patch is the firmware version, which restarts with each hardware revision (v5.0.0 for hardware revision 5). This lets Mujina tell v4, v5 and later boards apart. The PR was merged 2026-03-20 ([emberone-usbserial-fw PR #15](../../raw/hardware/256f-hardware/2026-01-18-github-emberone-usbserial-fw-pr-15-feat-usb-set-bcddevice-to.md)).
- **Ember One serial numbers:** these now come from the flash chip's per-chip unique ID (command 0x4B). The JEDEC ID used before gave every board with the same flash part the same serial number ([emberone-usbserial-fw PR #19](../../raw/hardware/256f-hardware/2026-03-19-github-emberone-usbserial-fw-pr-19-fix-usb-derive-serial-num.md)).
- **Bonanza:** bitaxe-raw renamed its USB product so the Bitaxe Bonanza appears different from standard Bitaxes ([bitaxe-raw PR #12](../../raw/hardware/bitaxe-osmu/2026-05-26-github-bitaxe-raw-pr-12-rename-usb-product-string-to-bitaxeb.md)).

## Control packet format

All three device firmwares share the same request framing ([rhapd README](../../raw/protocols/harvest/github-256foundation-rhapd-bitaxe-gamma.md); [bitaxe-raw README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxe-raw.md); [emberone-usbserial-fw README](../../raw/hardware/256f-hardware/github-256foundation-emberone-usbserial-fw.md)):

| Byte | 0 | 1 | 2 | 3 | 4 | 5 | 6… |
|---|---|---|---|---|---|---|---|
| Field | LEN LO | LEN HI | ID | BUS | PAGE | CMD | DATA |

- **LEN** is a little-endian u16 that counts the whole packet, including the length bytes themselves.
- **ID** can be any byte. The device echoes it in the response so the host can match responses to requests.
- **BUS** is always `0x00`.
- **PAGE** selects the command family (see the table below). **CMD** is a command within that page. **DATA** has a variable length. Mujina's notes say the payload is in practice limited by the 4KB USB buffer ([Mujina bitaxe-raw PROTOCOL.md](../../raw/firmware/mujina/github-mujina-mujina-miner-src-mgmt-protocol-bitaxe-raw-prot.md)).

### Pages and commands

| Page | Code | Commands | bitaxe-raw | rhapd-bitaxe-gamma | emberone-usbserial-fw |
|---|---|---|---|---|---|
| I2C | `0x05` | write `0x20`, read `0x30`, readwrite `0x40`. Data = [address, bytes to write, number of bytes to read] | yes | yes | yes |
| GPIO | `0x06` | Bitaxe: `0x00` RST_N (ASIC reset, active low). Ember One: `0x00` ASIC reset (active low), `0x01` ASIC power enable, `0x02` ASIC IO power enable. Data = [level]; leave out the data to read the level (Ember One) | yes | yes | yes |
| ADC | `0x07` | read VDD `0x50`, read VIN `0x51` | yes | yes | yes |
| LED | `0x08` | set colour `0x10`, data [R, G, B] | — | — | yes |
| System | `0x09` | reboot `0x01` (magic `DE AD BE EF`), reboot to bootloader `0x02` (magic `B0 07 10 AD`) | — | yes | proposed (PR #18) |

Worked examples from the READMEs:

- Write `0xDE` to I2C address `0x4F`: `08 00 01 00 05 20 4F DE`
- Readwrite two bytes from address `0x32`, register `0xFE`: `09 00 01 00 05 40 32 FE 02`
- Read the VDD pin: `06 00 00 00 07 50`
- Set the Ember One LED to magenta: `09 00 00 00 08 10 FF 00 FF`
- Reboot an RHAP-D into its bootloader: `0A 00 00 00 09 02 B0 07 10 AD`

**GPIO values are indices, not pin numbers.** A GPIO command value indexes a fixed list of named signals. At first that list held only RST_N. The design allows the microcontroller to be swapped without changing the protocol. The reset signal is called RST at the processor and RST_N (active low) at the ASIC, after the level shifter ([bitaxe-raw PR #2](../../raw/hardware/bitaxe-osmu/2025-04-19-github-bitaxe-raw-pr-2-docs-clarify-how-gpio-command-values.md)). Mujina's own notes describe the GPIO command byte as "the pin number" and give pin 0 as ASIC reset on Bitaxe boards. Both readings give the same result for RST_N ([Mujina bitaxe-raw PROTOCOL.md](../../raw/firmware/mujina/github-mujina-mujina-miner-src-mgmt-protocol-bitaxe-raw-prot.md)). The Bonanza branch added `0x04` = VR_EN (ESP32 GPIO10) and `0x05` = VR_PGOOD (GPIO11) ([bitaxe-raw PR #13](../../raw/hardware/bitaxe-osmu/2026-05-31-github-bitaxe-raw-pr-13-fixes-for-bitaxebonanza-raw.md)).

**System commands** need a 4-byte magic payload so that line noise or a framing desync cannot cause an accidental reboot. They send no response. The host detects success when the USB device re-enumerates, or on the RP2040 when a UF2 device appears. On the Ember One, reboot-to-bootloader calls the RP2040 ROM function that does the same as holding BOOTSEL ([rhapd README](../../raw/protocols/harvest/github-256foundation-rhapd-bitaxe-gamma.md); [emberone-usbserial-fw PR #18](../../raw/hardware/256f-hardware/2026-03-19-github-emberone-usbserial-fw-pr-18-feat-reboot-add-system-re.md)). This command lets `just flash` reflash a running RHAP-D board without anyone pressing a button.

## Response frames: v0 (bitaxe-raw) vs v1 (RHAP-D)

There are two incompatible response formats, and a host has to know which one a board uses:

| | v0 (bitaxe-raw, original Ember One firmware) | v1 (rhapd-bitaxe-gamma, unified Ember One frame) |
|---|---|---|
| Layout | `LEN(2) ID DATA…` | `LEN(2) ID CODE DATA…` |
| Length field | Success responses count only the data payload, not the length or ID bytes. Error responses count the whole packet | Always the total packet length, the same convention as commands |
| Success vs error | Error responses carry a `0xFF` marker and then an error code in the position where data would be. On the wire, the code cannot be told apart from a first data byte | Status byte at offset 3: `0x00` success, `0x10` timeout, `0x11` invalid command, `0x12` buffer overflow, `0xFF` error with ASCII message |
| Unparseable request | — | ID is returned as `0xFF` |
| Sources | [Mujina bitaxe-raw PROTOCOL.md](../../raw/firmware/mujina/github-mujina-mujina-miner-src-mgmt-protocol-bitaxe-raw-prot.md); [emberone-usbserial-fw PR #20](../../raw/hardware/256f-hardware/2026-03-28-github-emberone-usbserial-fw-pr-20-fix-control-unify-respons.md) | [rhapd README](../../raw/protocols/harvest/github-256foundation-rhapd-bitaxe-gamma.md) |

- **v0 minimum size:** a v0 response is at least 3 bytes (2 length bytes plus the ID), even when it has no data. The data field is at most 256 bytes ([Mujina bitaxe-raw PROTOCOL.md](../../raw/firmware/mujina/github-mujina-mujina-miner-src-mgmt-protocol-bitaxe-raw-prot.md)).
- **System commands** send no response in either format.
- **The breaking change:** emberone-usbserial-fw PR #20, opened 2026-03-28, adds the status byte, makes the length field always mean total length, and bumps the firmware to v5.1.0. The new version number lets the host tell protocol versions apart through bcdDevice ([emberone-usbserial-fw PR #20](../../raw/hardware/256f-hardware/2026-03-28-github-emberone-usbserial-fw-pr-20-fix-control-unify-respons.md)).
- **How Mujina picks a format:** Mujina's RHAP-D support (PR #107, merged 2026-08-30) uses a second USB descriptor that picks the frame format by product string. Boards that say "Bitaxe Gamma RHAP-D" get v1, which PR #107 describes as the frame "the EmberOne firmware also uses". bitaxe-raw boards keep the v0 frame. Both were verified on a Bitaxe Gamma running each firmware ([Mujina PR #107](../../raw/firmware/mujina/2026-08-30-github-mujina-pr-107-feat-bitaxe-support-the-rhap-d-firmware.md)).
- **Naming:** Mujina's bitaxe-raw protocol document and modules keep their names until the RHAP specification is published. The RHAP name came up on the "20260831" dev call (31 August 2026) ([Mujina PR #112](../../raw/firmware/mujina/2026-09-26-github-mujina-pr-112-docs-point-bitaxe-users-at-rhapd-bitaxe.md)).

## Safe startup and board behaviour

- **ASIC held in reset at power-up.** bitaxe-raw PR #1 (2025-04-19) made RST_N default low so the ASIC stays in reset, keeping heat and power down until a host connects. An Ember One reviewer noted the same idea helps boards with sensitive power-enable sequences ([bitaxe-raw PR #1](../../raw/hardware/bitaxe-osmu/2025-04-19-github-bitaxe-raw-pr-1-fix-leave-the-asic-in-reset-after-sta.md)). rhapd-bitaxe-gamma goes further: it also turns off the TPS546 core-voltage rail at startup. Its display shows the firmware name, the build commit and the serial number ([rhapd README](../../raw/protocols/harvest/github-256foundation-rhapd-bitaxe-gamma.md)).
- **Why the core rail also matters.** Even with reset held low, a Gamma's ASIC drew about 2 W, enough to heat a fanless 40mm heatsink to an estimated 60-degC/140-degF ([bitaxe-raw #10](../../raw/hardware/bitaxe-osmu/2026-03-19-github-bitaxe-raw-issue-10-fan-default-behavior-seems-interm.md)).
- **The fan is not a safety net.** bitaxe-raw makes no attempt to start the fan and relies on the hardware default. The Gamma fan does not reliably start at power-up. Full-on at startup through the R24 5.6k pull-up only happens on the EMC2101-R variant, and even that was intermittent. Only one of three Gamma 601s had the -R part that the BOM calls for ([bitaxe-raw #10](../../raw/hardware/bitaxe-osmu/2026-03-19-github-bitaxe-raw-issue-10-fan-default-behavior-seems-interm.md)).
- **Field report.** A Gamma 601 on bitaxe-raw got extremely hot with the fan off after power came back from an outage with no host script running ([bitaxe-raw #15](../../raw/hardware/bitaxe-osmu/2026-07-01-github-bitaxe-raw-issue-15-fan-not-running-by-default.md)).
- **Bonanza Bridge safety lease** (protocol 1, 2026-07-25). The Bridge firmware requires a safety lease before it will enable 5 V, release ASIC reset or drop the fan below 100%. The raw firmware owns and renews the lease, so host clients are unchanged. Closing the control port or any Bridge error asserts reset, disables 5 V, forces the fan to 100% and disarms the lease. In testing, BIRDS `bzmd` detected all four ASICs and finished power-on in 4 seconds ([bitaxe-raw PR #18](../../raw/hardware/bitaxe-osmu/2026-07-25-github-bitaxe-raw-pr-18-update-bitaxebonanza-raw-for-bridge.md)).
- **Resets.** Restarting Mujina does not reset the Bitaxe, and the RESET button resets only the ESP32, not the voltage regulator. For a clean run, pull the plug for a hard power cycle ([bitaxe-raw #9](../../raw/hardware/bitaxe-osmu/2026-03-03-github-bitaxe-raw-issue-9-having-trouble-flashing-and-runnin.md)).

## Flashing and toolchain notes

**rhapd-bitaxe-gamma (current Bitaxe Gamma path):**

1. Install rustup and `just`, then run `just setup-tools`. It installs espup, the `esp` Rust toolchain with the Xtensa backend, and espflash. A `rust-toolchain.toml` selects the esp toolchain only inside the repository, and a linker wrapper in `tools/` finds the Xtensa GCC, so no shell setup is needed ([rhapd README](../../raw/protocols/harvest/github-256foundation-rhapd-bitaxe-gamma.md)).
2. First flash: hold BOOT while attaching power, then run `just flash`. Later flashes need no button, because the recipe sends the System reboot-to-bootloader command first. To go back to stock ESP-Miner, hold BOOT at power-up again ([mujina.org: set up a Bitaxe Gamma](../../raw/firmware/mujina/github-mujina-website-howto-set-up-a-bitaxe-gamma.md)).
3. On Debian/Ubuntu, add yourself to the `dialout` group. The flash recipe also needs Python 3 ([mujina.org: set up a Bitaxe Gamma](../../raw/firmware/mujina/github-mujina-website-howto-set-up-a-bitaxe-gamma.md)).
4. Known limitation, reported 2026-09-08: `tools/board` finds ports by globbing Linux sysfs, so `just flash` fails on macOS with "no RHAP-D or ROM bootloader on USB". The proposed fix parses the IOKit registry ([rhapd-bitaxe-gamma #1](../../raw/protocols/harvest/2026-09-08-github-rhapd-bitaxe-gamma-issue-1-bug-tools-board-is-linux-o.md)).

**bitaxe-raw (legacy):**

- Flash with `cargo espflash flash --release --chip esp32s3`, then press RESET, because espflash does not restart the ESP32. Re-entering the bootloader needs BOOT held at power-up ([bitaxe-raw README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxe-raw.md)).
- **Toolchain regression:** esp toolchains 1.94.0.0 through 1.95.0.0 (LLVM 21) fail release builds with `Cannot select ... XtensaISD::PCREL_WRAPPER`. The workaround is to pin 1.93.0.0 (LLVM 20.1.1) with `espup install --toolchain-version 1.93.0.0` ([bitaxe-raw #16](../../raw/hardware/bitaxe-osmu/2026-07-02-github-bitaxe-raw-issue-16-build-release-build-fails-on-esp.md)). The pinning PR was closed rather than merged on 2026-09-26, because rhapd-bitaxe-gamma builds without the fix ([bitaxe-raw PR #17](../../raw/hardware/bitaxe-osmu/2026-07-02-github-bitaxe-raw-pr-17-build-pin-esp-toolchain-to-1-93-0-0.md)).
- **`cargo flash` (probe-rs) gotchas:**
  - It panicked with `CoreDisabled(1)` on a board in boot mode, while `espflash` worked reliably. A board held in BOOT enumerates as "Espressif USB JTAG/serial debug unit" ([bitaxe-raw #3](../../raw/hardware/bitaxe-osmu/2025-04-19-github-bitaxe-raw-issue-3-flashing-via-the-instructions-in-r.md)).
  - On other setups it produced a boot loop with "Image requires efuse blk rev >= v103.31, but chip is v1.3" ([bitaxe-raw #7](../../raw/hardware/bitaxe-osmu/2026-01-12-github-bitaxe-raw-issue-7-image-requires-efuse-blk-rev-v103.md)).
  - It also failed with a missing "ESP-IDF App Descriptor" error ([bitaxe-raw #11](../../raw/hardware/bitaxe-osmu/2026-04-02-github-bitaxe-raw-issue-11-error-failed-to-format-as-esp-idf.md)).
  - The fix for all three is to use `cargo espflash`.
- **Early bring-up bug:** data sent to the data serial port never reached the ASIC, and CI sat at its 1.2 V idle level. The RX and TX pins were swapped against the schematic, which PR #5 fixed ([bitaxe-raw #4](../../raw/hardware/bitaxe-osmu/2025-04-19-github-bitaxe-raw-issue-4-data-sent-to-data-serial-is-not-ap.md); [bitaxe-raw PR #5](../../raw/hardware/bitaxe-osmu/2025-04-21-github-bitaxe-raw-pr-5-fix-data-serial-by-correcting-rx-and.md)).

**emberone-usbserial-fw (RP2040):** build for `thumbv6m-none-eabi`. Flash over SWD with probe-rs (`cargo flash --release --chip RP2040`), or convert the ELF to a UF2 image with `elf2uf2-rs` and copy it to a mounted RP2040 ([emberone-usbserial-fw README](../../raw/hardware/256f-hardware/github-256foundation-emberone-usbserial-fw.md)).

## Host-side pitfalls

- **WSL2 + usbipd:** writes to the control CDC ACM port hung (a 4096-byte write timed out after 2 s), while the ASIC UART port drained 4096 bytes in about 340 ms. On native Linux the same reproducer drained and got an answer ([bitaxe-raw #14](../../raw/hardware/bitaxe-osmu/2026-07-01-github-bitaxe-raw-issue-14-control-cdc-acm-endpoint-not-drai.md)).
  - The reporter concluded that Bitaxe + Mujina on Windows was a no-go. The maintainer warned that a host that fails to read responses on one channel can also wedge the write direction, even on Linux.
  - Mujina later shipped a native Windows transport that avoids WSL (see [Mujina](../firmware/mujina.md)).
- **What does not need host changes:** no hardware change from Gamma 601 to 602 should require firmware changes (skot, 2026-03-09) ([bitaxe-raw #9](../../raw/hardware/bitaxe-osmu/2026-03-03-github-bitaxe-raw-issue-9-having-trouble-flashing-and-runnin.md)).
- **bitaxe-raw is a developer tool.** It is meant for control from a host PC and is not the standard AxeOS firmware. End-user feature requests such as PID fan modes belong with ESP-Miner ([bitaxe-raw #6](../../raw/hardware/bitaxe-osmu/2025-08-01-github-bitaxe-raw-issue-6-want-experimental-pid-fan-mode-for.md)).

## Beyond Mujina: factory testing

On 2026-09-04 skot proposed that ESP-Miner's test mode should become a bitaxe-raw compatible USB interface, implemented in C. Factories already plug in over USB to flash the firmware, so they could run any test suite from a PC right after flashing. He noted that the 256 Foundation has been working to standardize the protocol as RHAP-D, which he spelled "RAHP-D" ([ESP-Miner #1950](../../raw/firmware/esp-miner/2026-09-04-github-esp-miner-issue-1950-feature-replace-test-mode-with-b.md)).

## History

| Date | Event |
|---|---|
| 2025-01-30 | SV2 integration offer for the Ember One USB firmware is redirected to Mujina ([emberone-usbserial-fw #1](../../raw/hardware/256f-hardware/2025-01-30-github-emberone-usbserial-fw-issue-1-stratum-v2.md)) |
| 2025-03 | emberone-usbserial-fw gains DMA NeoPixel (LED) and ADC commands ([PR #3](../../raw/hardware/256f-hardware/2025-03-15-github-emberone-usbserial-fw-pr-3-add-dma-neopixel-command.md); [PR #4](../../raw/hardware/256f-hardware/2025-03-15-github-emberone-usbserial-fw-pr-4-add-adc-command.md)) |
| April 8, 2025 | @k1ix publishes bitaxe-raw. The 256 Foundation uses it so a Bitaxe can stand in for an Ember One during early Mujina development ([Assembling Freedom, 2025-05-05](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md)) |
| 2025-04-19 → 2025-04-22 | Mujina's developer contributes reset-at-startup, GPIO docs and data-serial pin fixes to bitaxe-raw (PRs #1, #2, #5) |
| 2025-04-30 | emberOne/00 v3, the first official hashboard release, is confirmed working with emberone-usbserial-fw loaded ([emberOne/00 releases](../../raw/hardware/256f-hardware/github-emberone00-pcb-releases.md)) |
| 2026-02-18 | Ember One firmware moves to the pid.codes VID:PID `1209:256f` ([PR #16](../../raw/hardware/256f-hardware/2026-02-06-github-emberone-usbserial-fw-pr-16-feat-usb-use-pid-codes-vi.md)) |
| 2026-03-19 / 2026-03-20 | Unique USB serial numbers and bcdDevice hardware/firmware versioning merged for the Ember One ([PR #19](../../raw/hardware/256f-hardware/2026-03-19-github-emberone-usbserial-fw-pr-19-fix-usb-derive-serial-num.md); [PR #15](../../raw/hardware/256f-hardware/2026-01-18-github-emberone-usbserial-fw-pr-15-feat-usb-set-bcddevice-to.md)) |
| 2026-03-28 | Unified v1 response frame proposed for the Ember One (v5.1.0, breaking) ([PR #20](../../raw/hardware/256f-hardware/2026-03-28-github-emberone-usbserial-fw-pr-20-fix-control-unify-respons.md)) |
| 2026-05-26 → 2026-07-25 | bitaxe-raw `bonanza` branch: BitaxeBonanza product string, VR GPIOs, Bridge protocol 1 safety lease ([PR #12](../../raw/hardware/bitaxe-osmu/2026-05-26-github-bitaxe-raw-pr-12-rename-usb-product-string-to-bitaxeb.md); [PR #18](../../raw/hardware/bitaxe-osmu/2026-07-25-github-bitaxe-raw-pr-18-update-bitaxebonanza-raw-for-bridge.md)) |
| 2026-07-02 | esp toolchain LLVM 21 regression is found, and pinning to 1.93.0.0 becomes the workaround ([bitaxe-raw #16](../../raw/hardware/bitaxe-osmu/2026-07-02-github-bitaxe-raw-issue-16-build-release-build-fails-on-esp.md)) |
| 2026-08-30 | Mujina merges RHAP-D support: `1209:6102`, v1 frames, and continued bitaxe-raw compatibility ([Mujina PR #107](../../raw/firmware/mujina/2026-08-30-github-mujina-pr-107-feat-bitaxe-support-the-rhap-d-firmware.md)) |
| 2026-09-26 | bitaxe-raw PR #19 proposes replacing `main` with a pointer to rhapd-bitaxe-gamma (still open at capture). Mujina docs PR #112 is closed 2026-10-05 after pointing users at rhapd-bitaxe-gamma ([bitaxe-raw PR #19](../../raw/hardware/bitaxe-osmu/2026-09-26-github-bitaxe-raw-pr-19-docs-retire-main-in-favor-of-rhapd-b.md); [Mujina PR #112](../../raw/firmware/mujina/2026-09-26-github-mujina-pr-112-docs-point-bitaxe-users-at-rhapd-bitaxe.md)) |

## Contradictions & Open Questions

- **Is v1 shipped on the Ember One?** Mujina PR #107 (2026-08-30) says RHAP-D answers with "the v1 response frame the EmberOne firmware also uses". In the 2026-10-07 capture, however, emberone-usbserial-fw PR #20, which introduces that frame, and PR #18, which adds the System reboot commands, are both still open. PR #18 was waiting on #20. Best assessment: v1 is the agreed RHAP direction and is live on rhapd-bitaxe-gamma. Whether a released Ember One firmware speaks it should be checked against the board's bcdDevice: v5.1.0 or later means v1 ([Mujina PR #107](../../raw/firmware/mujina/2026-08-30-github-mujina-pr-107-feat-bitaxe-support-the-rhap-d-firmware.md); [emberone-usbserial-fw PR #20](../../raw/hardware/256f-hardware/2026-03-28-github-emberone-usbserial-fw-pr-20-fix-control-unify-respons.md); [emberone-usbserial-fw PR #18](../../raw/hardware/256f-hardware/2026-03-19-github-emberone-usbserial-fw-pr-18-feat-reboot-add-system-re.md)).
- **Missing spec.** The RHAP specification document had not been written as of the capture. The packet tables above are compiled from the device READMEs and Mujina's reverse-engineered notes ([rhap README](../../raw/protocols/harvest/github-256foundation-rhap.md)).
- **Open requests on the Ember One firmware:** a static `device_type` command, so a control board can detect what features a board has, and support for several attached boards. Two Ember Ones on a Mac showed only one set of serial ports ([emberone-usbserial-fw #13](../../raw/hardware/256f-hardware/2025-04-18-github-emberone-usbserial-fw-issue-13-add-static-device-type.md); [emberone-usbserial-fw #14](../../raw/hardware/256f-hardware/2025-04-18-github-emberone-usbserial-fw-issue-14-support-multiple-usb.md)).

## See Also

- [Mujina](../firmware/mujina.md), the main RHAP host
- [Ember One & the BZM2 Hardware Stack](../hardware/ember-one-bzm2.md)
- [Bitaxe Models](../hardware/bitaxe-models.md)
- [Bitaxe Board Design & Errata](../hardware/bitaxe-board-design-and-errata.md)
- [ESP-Miner / AxeOS](../firmware/esp-miner-axeos.md), the stock Bitaxe firmware that RHAP-D replaces
- [Bitaxe Troubleshooting](../getting-started/bitaxe-troubleshooting.md)
- [Libre Board & Control Boards](../hardware/libre-board-and-control-boards.md)
- Same topic: [Stratum in Practice](stratum-in-practice.md)
