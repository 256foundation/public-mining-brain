# bitaxeorg/ESP-Miner issue #1310: Add components and types to system page

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1310
> Collected: 2026-10-07
> Published: 2025-10-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1310
- State: open
- Author: mutatrum
- Opened: 2025-10-30
- Closed: n/a
- Labels: enhancement

## Description

List all i2c devices on the system page, with vendor id and device variant information if available.

## Comments

### skot on 2025-11-07

[i2cdetect](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/v3.1.2/tools/i2cdetect.c) on linux does this.. I believe it just sends an i2c read to the whole 7bit address space and looks for an ACK. as far as determining what device is responding, that's a bit harder. afaik there is not standard register for manufacturer ID.

### mutatrum on 2025-11-17

Relevant: https://github.com/bitaxeorg/ESP-Miner/pull/1333#issuecomment-3500031999
