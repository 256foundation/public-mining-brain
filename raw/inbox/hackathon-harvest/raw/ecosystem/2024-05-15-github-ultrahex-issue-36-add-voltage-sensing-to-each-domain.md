# bitaxeorg/ultraHex issue #36: Add voltage sensing to each domain in order to check voltage balance

> Source: https://github.com/bitaxeorg/ultraHex/issues/36
> Collected: 2026-10-07
> Published: 2024-05-15

- Repository: bitaxeorg/ultraHex
- Type: issue
- Number: 36
- State: closed
- Author: macphyter
- Opened: 2024-05-15
- Closed: 2024-05-25
- Labels: none

## Description

Add a voltage divider on each domain core voltage, and feed it back into the ESP32 so the firmware can measure the domain voltage balance and report it to the GUI.

## Comments

### macphyter on 2024-05-25

This has been added on the schematic and layout for v304
