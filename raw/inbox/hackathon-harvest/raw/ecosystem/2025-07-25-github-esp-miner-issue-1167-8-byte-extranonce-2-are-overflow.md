# bitaxeorg/ESP-Miner issue #1167: 8 byte extranonce_2 are overflowing the uint32_t data type

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1167
> Collected: 2026-10-07
> Published: 2025-07-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1167
- State: closed
- Author: skot
- Opened: 2025-07-25
- Closed: 2025-08-15
- Labels: bug

## Description

the extranonce_2 variable throughout esp-miner is a uint32_t.. this will cause the extranonce_2 to include some random bytes if the extranonce_2_len is anything more than 4. 8 is very common. Maybe more.

note: this does not affect mining! Just creates some strange extranonces.

https://github.com/bitaxeorg/ESP-Miner/blob/0958185217f324c8fe786cd6ef05f22e117f616d/components/stratum/mining.c#L113-L124

## Comments

### skot on 2025-07-25

just changing extranonce_2 to uint64_t fixes the common case where the length is 8 bytes.. but maybe we should handle even longer extranonce2's
