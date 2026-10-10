# bitaxeorg/ultraHex issue #17: Provide 3.3V to TPS546 for configuration

> Source: https://github.com/bitaxeorg/ultraHex/issues/17
> Collected: 2026-10-07
> Published: 2024-02-04

- Repository: bitaxeorg/ultraHex
- Type: issue
- Number: 17
- State: closed
- Author: macphyter
- Opened: 2024-02-04
- Closed: 2024-03-22
- Labels: none

## Description

The TPS546 regulator will run on 3.3V without trying to start regulation.  This mode is used for configuring the registers in the chip.  If we route 3.3V over to AVIN on the TPS546, then we can use USB only to power up boards to flash the ESP32, and then reboot to allow the ESP32 to configure the TPS546 registers before applying main 12V power.  Probably need a diode to prevent backfeed from the 12V rail.

## Comments

### macphyter on 2024-03-22

Since we are removing the USB 5V supply and diode, this will no longer be possible.  Its not a big deal, the TPS546 can still be configured using main power.  Closing this issue.
