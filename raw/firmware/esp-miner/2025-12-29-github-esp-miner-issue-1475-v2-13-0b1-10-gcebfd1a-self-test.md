# bitaxeorg/ESP-Miner issue #1475: v2.13.0b1-10-gcebfd1a - Self Test fails

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1475
> Collected: 2026-10-07
> Published: 2025-12-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1475
- State: closed
- Author: ghost
- Opened: 2025-12-29
- Closed: 2026-01-03
- Labels: none

## Description

Self test failing ....

v2.13.0b1-10-gcebfd1a-dirty 

Locally built factory firmware .... logs

[self-test-log-v2.13.0b1-10.txt](https://github.com/user-attachments/files/24375471/self-test-log-v2.13.0b1-10.txt)

Factory firmware pulled from the repo .... (master - https://github.com/bitaxeorg/ESP-Miner/actions/runs/20494003909)

Logs....

[self-test-log2-v2.13.0b1-10.txt](https://github.com/user-attachments/files/24375574/self-test-log2-v2.13.0b1-10.txt)

Bitaxetool was used to flash the factory firmware to the device along with the correct .cvs file with the self test enabled.

`selftest,data,u16,1`

This also happens on the Ultra's (205, 207), Supra's (401) I have here.

## Comments

### ghost on 2026-01-02

0aa4935  tested, issue resolved.

*No PR for this fix @benjamin-wilson *  

### ghost on 2026-01-03

Resolved except for a PR on the fix.
