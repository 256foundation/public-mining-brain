# bitaxeorg/bitaxe-raw pull request #2: docs: clarify how GPIO command values map to pins

> Source: https://github.com/bitaxeorg/bitaxe-raw/pull/2
> Collected: 2026-10-07
> Published: 2025-04-19

- Repository: bitaxeorg/bitaxe-raw
- Type: pull request
- Number: 2
- State: closed
- Author: rkuester
- Opened: 2025-04-19
- Closed: 2025-04-22
- Labels: none

## Description

Document the GPIO command values as a map of pin names to values instead of implying the value corresponds to a pin number. This better matches the current implementation, which uses a discrete list of GPIOs (at this time, containing only RST_N), and uses the command value to index into that list.

Note, there's some room for confusion about RST_N. At the processor, the signal is named RST, but at the ASIC (after a level shifter) it's named RST_N. Use RST_N in the documentation to make the signal's active-low behavior clear.

## Comments

### korbin on 2025-04-22

Thanks for the add. The discrete list was intentional to allow for MCU swaps, etc. but can be changed if folks desire.
