# bitaxeorg/ultraHex issue #18: Need diode on 5V regulator output

> Source: https://github.com/bitaxeorg/ultraHex/issues/18
> Collected: 2026-10-07
> Published: 2024-02-12

- Repository: bitaxeorg/ultraHex
- Type: issue
- Number: 18
- State: closed
- Author: macphyter
- Opened: 2024-02-12
- Closed: 2024-03-23
- Labels: none

## Description

When USB is plugged in without the main power supply attached, 5V gets fed back through the 5V regulator to VIN.  This results in the 12V fans being powered by the USB 5V.  The 5V regulator should have a diode after the output caps to prevent this.

## Comments

### benjamin-wilson on 2024-02-12

On the 205 we just removed the USB power, it also removes a part. 

### macphyter on 2024-03-23

Removed USB power.
