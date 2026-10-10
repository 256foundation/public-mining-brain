# bitaxeorg/ultraHex issue #11: change nominal TPS40305 output to 3.6V

> Source: https://github.com/bitaxeorg/ultraHex/issues/11
> Collected: 2026-10-07
> Published: 2023-11-25

- Repository: bitaxeorg/ultraHex
- Type: issue
- Number: 11
- State: closed
- Author: skot
- Opened: 2023-11-25
- Closed: 2023-12-17
- Labels: bug

## Description

the BM1366 wants 1.2V core voltage. for 3 in series this should be 3.6V.

the easy way to do this is change R10 from 1.54k -> 2k in the TPS40305 feedback circuit

## Comments

### macphyter on 2023-12-17

The new voltage regulator has been designed with a nominal output of 3.6V.
