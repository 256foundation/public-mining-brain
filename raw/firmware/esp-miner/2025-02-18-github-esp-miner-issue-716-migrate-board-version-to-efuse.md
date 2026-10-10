# bitaxeorg/ESP-Miner issue #716: Migrate board version to eFuse

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/716
> Collected: 2026-10-07
> Published: 2025-02-18

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 716
- State: open
- Author: mutatrum
- Opened: 2025-02-18
- Closed: n/a
- Labels: enhancement

## Description

### Current situation

A new build needs a specific config file to be flashed, so the firmware knows what board version it's running on, and by extension what the name of the board is, the type of ASIC, how many ASICs, what voltage regulator and temperature sensors are on this board. At the moment there are 3 configuration values, which need to be set in NVS: `asicmodel`, `devicemodel` and `boardversion`.

### Proposed changes

This issue proposes to move `boardversion` to eFuse storage. This is a small single write unmodifyable storage, which keeps it's data even after a full flash wipe. Based on the board version, all other values can be derived, such as device model, asic model, default frequency, etc.

All other values in the firmware configs are default values. Second proposal is to move all these default settings to the firmware, e.g. if a new device is created, a standard firmware is flashed, the board version is burned into the eFuse, and from there it boots up. When a user changes any of the configuration settings, these can be stored in NVS, the same as happens now. One way of storing these defaults is to have a partition that has all the current config files for each board version. These can be read on boot.

The benefit of moving this to eFuse is that there are no longer different firmware images per board version needed. The second benefit is that a factory reset can now be performed by software, by clearing the NVS storage. This results in everything going back to factory defaults.

### Backwards compatibility

Currently, the board verson is stored in NVS. Backwards compatibility can be achieved by detecting at boot if the eFuse has been set, and at the end of a normal boot cycle, when it's clear that the device is running properly, burn the board version in eFuse. Then on the next boot, the value can be picked up from the eFuse.

### Device manufacturer tools

We have to document how a device manufacturer can burn the board version into the eFuse. It is possible to test these with a virtual eFuse, so device manufacturers cando a dry run, see if the device properly boots, before burning the eFuses. This is a ony-time action, so this must be properly documented.

Alternatively, we could reserve a backup spot in the eFuse in case someone made a mistake, but I would be reluctant to do this. Burning the eFuse is of the same importance as properly soldering a device, it just has to be right.

It is possible a manufacturer wants to deviate from the default values. I don't know if this is actually needed.

### Steps to achieve goal

* read boardversion from eFuse
* implement backwards compatibility
  * read boardversion from eFuse
  * if not there, read boardversion from NVS
  * wait until boot is finished to make sure the device is working
  * burn boardversion eFuse in eFuse
* derive `devicemodel` and `asicmodel` from `boardversion`
  * device model should only be used for display purposes
* move all other default values into firmware
  * add a file partition with all current `config-###.csv` files
  * read board version config file, use the default values if a configuration is not in NVS
* implement firmware reset through api and/or AxeOS
* remove firmware specific builds
* document or make a tool for manufacturers to burn eFuse
  * this can be either with esptool or an manufacturers webflasher version

## Comments

### mutatrum on 2025-02-18

There is one block of 256 bits available for user data (`EFUSE_BLK3`), I think it's prudent to only use bits sparingly. Currently, board version goes to 800, where the 100s are the general board type, and remainder is the board revision. It might make sense to split this into two parts of 8 bits. This will result in 256 board type, with 256 revisions each, using 16 bits of the eFuse bits.

From the documentation:

> ESP32-S3 has 11 eFuse blocks each containing 256 bits (not all bits can be used for user parameters):
> 
>  * EFUSE_BLK0 is used entirely for system parameters
>  * EFUSE_BLK1 is used entirely for system parameters
>  * EFUSE_BLK2 is used entirely for system parameters
>  * EFUSE_BLK3 (also named EFUSE_BLK_USER_DATA) can be used for user parameters
>  * EFUSE_BLK4 to EFUSE_BLK8 (also named EFUSE_BLK_KEY0 to EFUSE_BLK_KEY4) can be used to store keys for Secure Boot or Flash Encryption. If both features are unused, these blocks can be used for user parameters.
>  * EFUSE_BLK9 (also named EFUSE_BLK_KEY5) can be used for any purpose except for Flash Encryption (due to a HW errata);
>  * EFUSE_BLK10 (also named EFUSE_BLK_SYS_DATA_PART2) is reserved for system parameters.

As we're not using secure boot or flash encryption, there might be more blocks available in the future.

### mutatrum on 2025-02-18

Another idea would be to add a manufacturer ID. Currently there is nothing in the firmware that can use this, so initially it will be for display purposes only. This would need a central manufacturer ID registry.

This could in the future also be used to have manufacturer dependent default overrides, which more tightly couples it to the base firmware. Benefit is that if a manufacturer proposed a PR specific for them, they can still use the base firmware and infrastructure directly. Downside is extra maintenance load on reviewers.

With 256 board types, manufacturers could also claim their own board type, and add a PR for their configuration defaults. This might be a cleaner solution.

As a manufacturer this means giving up a bit of control to OSMU (e.g. specific manufacturers support can be yanked from the firmware, disconnecting them from the base firmware).

### skot on 2025-02-18

This sounds great to me! I suggest adding a "make" or "brand" field to identify Bitaxe or otherwise.

Also whatever the default eFuse state is (0x00 or 0xFF?) should be reserved.

### mutatrum on 2025-02-18

eFuse bits are 0 at default, and any single bit can only be burned to 1, once. So any value with all 0's might be interpreted as uninitialised, and all 1's (0xFF) would be to mark something as invalid.

One idea is to apply type/value encoding to the eFuse bits. F.e. use a few bits (6?) as field type, and then have a predefined (per type) number of bits as value. This way, a value can be made invalid by burning it to all 1's, and a new field value could be burned.

But this might be over-complicated.

### mutatrum on 2025-02-19

Is brand something else than manufacturer?

### skot on 2025-02-19

> Is brand something else than manufacturer?

Yeah, brand is like Bitaxe or NerdAxe, which could be made by the same manufacturer.

### BitMaker-hub on 2025-02-20

First of all thanks for this very well explained proposal, this looks very good to me too.
On the other hand this can be problematic for those who DIY their own bitaxes if it's not enough easy as the current webflasher.

I just had an small previous experience with efuses, using flash encryption and secure boot.
The process is not difficult, can be done using espefuse.py tool at the end of the flash process.



### johnny9 on 2025-07-12

Concept ACK

I think we should go down this route especially now that we have clear products/boardversions.
