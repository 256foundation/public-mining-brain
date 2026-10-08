# bitaxeorg/ultraHex issue #42: ADC inputs for domain voltage sense need dividers

> Source: https://github.com/bitaxeorg/ultraHex/issues/42
> Collected: 2026-10-07
> Published: 2024-06-06

- Repository: bitaxeorg/ultraHex
- Type: issue
- Number: 42
- State: closed
- Author: macphyter
- Opened: 2024-06-06
- Closed: 2024-06-09
- Labels: none

## Description

The domain voltage sense line on the top domain could go as high as 3.6V or higher.  Need to add resistor dividers to the domain voltage sense to keep them in the range of the ESP32 ADC inputs.

## Comments

### macphyter on 2024-06-09

Added resistor dividers to domain voltage sense signals to both schematic and PCB layout.
Fixed on v304.
