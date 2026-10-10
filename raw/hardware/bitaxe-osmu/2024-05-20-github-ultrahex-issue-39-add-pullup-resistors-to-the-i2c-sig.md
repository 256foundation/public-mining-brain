# bitaxeorg/ultraHex issue #39: Add pullup resistors to the I2C signals

> Source: https://github.com/bitaxeorg/ultraHex/issues/39
> Collected: 2026-10-07
> Published: 2024-05-20

- Repository: bitaxeorg/ultraHex
- Type: issue
- Number: 39
- State: closed
- Author: macphyter
- Opened: 2024-05-20
- Closed: 2024-06-04
- Labels: none

## Description

It appears that the I2C signals from the ESP32 might already have pullups, but they are extremely weak.  We should add our own pullups because the I2C signal goes across the entire board from end to end.  Also, the PMBus spec calls out stronger pullups.

## Comments

### macphyter on 2024-05-20

Added to v304 schematic, still needs to be added to PCB layout.

### macphyter on 2024-06-04

Finished I2C pullup resistors on PCB layout
Fixed on v304
