# bitaxeorg/ESP-Miner issue #1851: Bug Report: XMC Flash Chip XM25QH128AHIG Not Recognized by Bootloader

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1851
> Collected: 2026-10-07
> Published: 2026-08-06

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1851
- State: closed
- Author: arcsin3x
- Opened: 2026-08-06
- Closed: 2026-08-06
- Labels: none

## Description

**Background**
During a firmware flash operation on my ESP32-S3-WROOM-1 module, the process was unexpectedly interrupted, which caused the original flash chip to become corrupted/unusable. The original flash chip was:

Original Chip: XM25UH128D (128M-bit, 16MB, 3.3V)

After replacing the damaged chip with a new one, I encountered a boot failure. The replacement chip is:

Replacement Chip: XM25QH128AHIG (128M-bit, 16MB, 3.3V)

**Description**
The ESP32-S3 bootloader fails to initialize the replacement XMC flash chip XM25QH128AHIG, causing a continuous reboot loop. The bootloader detects the chip but does not recognize it as a valid XMC device, leading to a startup failure.

Note: The original XM25UH128D chip worked without any issues before it was damaged. The problem only appeared after replacing it with the XM25QH128AHIG.

**Environment**
ESP-IDF Version: v5.5.5

Target Chip: ESP32-S3

Module: ESP32-S3-WROOM-1 (16MB Flash, 8MB Octal PSRAM)

Flash Chip (Replacement): XM25QH128AHIG (16MB, 3.3V)

Project: ESP-Miner (bitaxeorg/ESP-Miner)

**Log Output**
text
I (29) boot: ESP-IDF v5.5.5 2nd stage bootloader
I (29) boot: compile time Aug  5 2026 20:42:27
I (29) boot: Multicore bootloader
I (29) bootloader_flash: XM25QHxxC startup flow
E (36) bootloader_flash: XMC flash startup fail
E (38) boot.esp32s3: failed when running XMC startup flow, reboot!
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0x3 (RTC_SW_SYS_RST),boot:0x28 (SPI_FAST_FLASH_BOOT)
Saved PC:0x403cd28d
SPIWP:0xee
mode:DIO, clock div:1
**esptool.py Detection**
**The chip is detected correctly by esptool.py:**

**text**
esptool.py --port COM14 flash_id
Manufacturer: 20
Device: 7018
Detected flash size: 16MB
**Root Cause Analysis**
In bootloader_flash.c, the function is_xmc_chip_strict() uses a whitelist of device IDs to identify XMC chips:

c
static IRAM_ATTR bool is_xmc_chip_strict(uint32_t rdid)
{
    uint32_t vendor_id = BYTESHIFT(rdid, 2);
    uint32_t mfid = BYTESHIFT(rdid, 1);
    uint32_t cpid = BYTESHIFT(rdid, 0);

    if (vendor_id != XMC_VENDOR_ID_1) {
        return false;
    }

    bool matched = false;
    if (mfid == 0x40) {
        if (cpid >= 0x13 && cpid <= 0x20) {
            matched = true;
        }
    } else if (mfid == 0x41) {
        if (cpid >= 0x17 && cpid <= 0x20) {
            matched = true;
        }
    } else if (mfid == 0x50) {
        if (cpid >= 0x15 && cpid <= 0x16) {
            matched =  true;
        }
    }
    return matched;
}
The XM25QH128AHIG has a Manufacturer ID of 0x70, which is not included in this list. As a result, the bootloader fails to recognize it as a valid XMC chip and aborts the startup flow.

**Why This Is a Problem**
The original chip (XM25UH128D, MFID 0x41) worked perfectly because it was in the whitelist.

The replacement chip (XM25QH128AHIG, MFID 0x70) is from the same XMC family and should be compatible, but the bootloader refuses to initialize it.

esptool.py can communicate with the chip, so the hardware connection is not the issue.

This prevents users from replacing damaged flash chips with readily available alternatives from the same manufacturer.

**Workaround / Fix**
Modify the is_xmc_chip_strict() function to include Manufacturer ID 0x70:

c
static IRAM_ATTR bool is_xmc_chip_strict(uint32_t rdid)
{
    uint32_t vendor_id = BYTESHIFT(rdid, 2);
    uint32_t mfid = BYTESHIFT(rdid, 1);
    uint32_t cpid = BYTESHIFT(rdid, 0);

    if (vendor_id != XMC_VENDOR_ID_1) {
        return false;
    }

    bool matched = false;
    if (mfid == 0x40) {
        if (cpid >= 0x13 && cpid <= 0x20) {
            matched = true;
        }
    } else if (mfid == 0x41 || mfid == 0x70) {  // Added 0x70 for XM25QH128AHIG
        if (cpid >= 0x17 && cpid <= 0x20) {
            matched = true;
        }
    } else if (mfid == 0x50) {
        if (cpid >= 0x15 && cpid <= 0x16) {
            matched =  true;
        }
    }
    return matched;
}
**Additional Notes**
The chip XM25QH128AHIG is detected correctly by esptool.py and can be flashed successfully.

The issue occurs specifically in the bootloader's XMC startup flow.

A similar workaround was previously used for other XMC chips with different Manufacturer IDs (e.g., 0x41).

**Suggested Fix**
Add 0x70 to the list of recognized XMC Manufacturer IDs in is_xmc_chip_strict().

**Related Files**
components/bootloader_support/bootloader_flash/src/bootloader_flash.c



## Comments

### WantClue on 2026-08-06

This would be an issue directly for espressif, we don't want to mess with allowed vendor id's in the bootloader whitelist.
