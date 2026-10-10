# bitaxeorg/ESP-Miner issue #989: Support 207

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/989
> Collected: 2026-10-07
> Published: 2025-05-31

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 989
- State: closed
- Author: mutatrum
- Opened: 2025-05-31
- Closed: 2025-06-10
- Labels: none

## Description

Also add support for NVS overrides for possible alternative hardware configurations

## Comments

### ghost on 2025-05-31

The 207 is like the 601/2 design wise.

I got no other info on it.

https://github.com/bitaxeorg/bitaxeUltra/tree/ultra-207/Manufacturing%20Files

![Image](https://github.com/user-attachments/assets/16822ffc-bb85-4d81-bc44-7d11d9548ff0)

![Image](https://github.com/user-attachments/assets/601b9236-aef6-402b-a7d7-faa2040d7f0e)

### mutatrum on 2025-05-31

```
{
  .board_version = "207",
  .family = FAMILY_ULTRA,
  .EMC2101 = true,
  .TPS546 = true,
  .power_consumption_target = 12,
},
```
