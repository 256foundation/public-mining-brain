# bitaxeorg/ESP-Miner issue #302: Possible Memory Corruption

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/302
> Collected: 2026-10-07
> Published: 2024-08-17

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 302
- State: closed
- Author: shufps
- Opened: 2024-08-17
- Closed: 2024-11-28
- Labels: bug

## Description

The `hex2bin` len parameter takes the destination length that is `HASH_SIZE` and not the source length.

https://github.com/skot/ESP-Miner/blob/80e72cc87443b22ba5920f775a97da69621b5975/components/stratum/stratum_api.c#L238

The last hex string converted overwrites 32 bytes of memory not allocated
