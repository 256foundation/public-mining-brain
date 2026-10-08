# bitaxeorg/bitaxe-raw pull request #1: fix: leave the ASIC in reset after startup

> Source: https://github.com/bitaxeorg/bitaxe-raw/pull/1
> Collected: 2026-10-07
> Published: 2025-04-19

- Repository: bitaxeorg/bitaxe-raw
- Type: pull request
- Number: 1
- State: closed
- Author: rkuester
- Opened: 2025-04-19
- Closed: 2025-04-22
- Labels: none

## Description

Leave the ASIC in reset after startup by defaulting the RST_N GPIO to LO. This minimizes heat and power until the host device is connected and begins to use the ASIC.

## Comments

### korbin on 2025-04-22

Great idea, thanks for the commit. This has broader applicability to other boards with different/more sensitive power supply enable sequences, etc.
