# bitaxeorg/bitaxeGamma issue #25: Add pullup resistors on I2C/SMBus pins

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/25
> Collected: 2026-10-07
> Published: 2025-03-04

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 25
- State: open
- Author: skot
- Opened: 2025-03-04
- Closed: n/a
- Labels: bug

## Description

SDA and SCL data pins need a pullup resistor to 3.3V. The TPS546 SMB_ALRT should also have this. 4.7k should be good.

## Comments

### sz4bi on 2025-05-14

I can not find the SMB_ALRT resistor anywhere in the modified files. Are we talking about the TPS546 PMB_ALRT pin on the schematics?
