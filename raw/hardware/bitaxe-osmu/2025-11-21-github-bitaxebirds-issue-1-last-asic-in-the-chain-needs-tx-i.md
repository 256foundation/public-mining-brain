# bitaxeorg/bitaxeBIRDS issue #1: last ASIC in the chain needs TX_IN pulled up.

> Source: https://github.com/bitaxeorg/bitaxeBIRDS/issues/1
> Collected: 2026-10-07
> Published: 2025-11-21

- Repository: bitaxeorg/bitaxeBIRDS
- Type: issue
- Number: 1
- State: closed
- Author: skot
- Opened: 2025-11-21
- Closed: 2026-02-10
- Labels: none

## Description

Need a 1k pullup resistor on TX_IN (pin 17) for the last asic in the chain. Also prolly a 10k pulldown on TRIP_IN (pin 18)

## Comments

### penguin359 on 2025-11-30

According to my notes, both pins should have an internal pull-up and the 1K on TX_IN should be optional. It is actually marked as DNP on my schematic. The TRIP_IN pull-down is included and probably a good idea, however, if you don't have it on the boards you made, I believe it should be software configurable to enable internal pull-downs on it.
