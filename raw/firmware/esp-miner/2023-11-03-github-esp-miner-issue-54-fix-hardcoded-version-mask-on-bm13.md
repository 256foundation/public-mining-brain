# bitaxeorg/ESP-Miner issue #54: fix hardcoded version mask on BM1366

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/54
> Collected: 2026-10-07
> Published: 2023-11-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 54
- State: closed
- Author: skot
- Opened: 2023-11-03
- Closed: 2024-10-10
- Labels: bug

## Description

Currently esp-miner always uses the BM1366 default(?) `0x1fffe000` as the version mask. Technically esp-miner should configure the BM1366 to use the version mask the stratum server & client negotiate, even if most of the time it's `0x1fffe000`

## Comments

### johnny9 on 2023-11-08

Likely just need to write the mask to register A4

Here is our understanding of A4

![version_rolling](https://github.com/skot/ESP-Miner/assets/985648/83cc9d28-9d4b-4f7e-a76f-5e8948e6efdb)
