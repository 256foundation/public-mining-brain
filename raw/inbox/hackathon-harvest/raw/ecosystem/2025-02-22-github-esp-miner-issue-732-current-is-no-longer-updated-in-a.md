# bitaxeorg/ESP-Miner issue #732: current is no longer updated in API

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/732
> Collected: 2026-10-07
> Published: 2025-02-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 732
- State: closed
- Author: 0xf0xx0
- Opened: 2025-02-22
- Closed: 2025-03-08
- Labels: bug, accepted, critical

## Description

**Describe the bug**
The `current` field in the api is 0, instead of the draw of the board. the offending commit is 7dcb69ebd.

**To Reproduce**
Steps to reproduce the behavior:
1. Build and flash v2.6.0b7
2. send a request to the `/api/system/info` endpoint
3. observe that `current` is `0`

**Expected behavior**
`current` should be the draw of the board.

**Hardware (please complete the following information):**
 - Bitaxe HW version: gamma (601 mod)
 - Bitaxe HW vendor: gekkoscience
 - ESP-Miner FW version: v2.6.0b7
 - Hash Frequency: irrelevant
 - Voltage: irrelevant
 - Pool URL, Port, User: irrelevant
