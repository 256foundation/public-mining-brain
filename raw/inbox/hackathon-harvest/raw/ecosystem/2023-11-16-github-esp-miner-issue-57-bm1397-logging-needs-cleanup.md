# bitaxeorg/ESP-Miner issue #57: BM1397 logging needs cleanup

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/57
> Collected: 2026-10-07
> Published: 2023-11-16

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 57
- State: closed
- Author: johnny9
- Opened: 2023-11-16
- Closed: 2023-11-30
- Labels: none

## Description

Users continue to think "return null" is an issue and for good reason. The bm1397 module could use a cleanup of the logs to make sure we aren't sending anything thats not necessary to report to the uses monitoring the console log.
