# bitaxeorg/bitaxe-raw issue #4: Data sent to data serial is not appearing on the ASIC's serial input, signal CI

> Source: https://github.com/bitaxeorg/bitaxe-raw/issues/4
> Collected: 2026-10-07
> Published: 2025-04-19

- Repository: bitaxeorg/bitaxe-raw
- Type: issue
- Number: 4
- State: closed
- Author: rkuester
- Opened: 2025-04-19
- Closed: 2025-04-22
- Labels: none

## Description

Data sent to data serial is not passed through to the ASIC's serial input, signal CI. Signal CI is steady at its HI value (1.2 V).

Control serial manipulation of RST_N *is* working.

## Comments

### rkuester on 2025-04-19

So far I've tried various baud rates, various lengths of data, terminating my data with "\n", and delaying for 1s after sending before closing the USB port on the host side, all to no effect.
