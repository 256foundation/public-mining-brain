# bitaxeorg/bitaxeGamma issue #31: UVLO Voltage divider it set wrong for 5V input

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/31
> Collected: 2026-10-07
> Published: 2025-03-17

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 31
- State: closed
- Author: skot
- Opened: 2025-03-17
- Closed: 2025-03-18
- Labels: bug

## Description

The TPS546D24A UVLO threshold is 2.5V. For this to trigger at about 4.5VIN, R8 should by 15k (not 3.74k)

## Comments

### skot on 2025-03-18

Er, maybe not. I think I was looking at the wrong threshold (there are several). The ENuvlo threshold is actually 1.05V, making the UVLO for our current voltage divider set at 4.36V
