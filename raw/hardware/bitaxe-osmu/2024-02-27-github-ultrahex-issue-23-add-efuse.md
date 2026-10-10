# bitaxeorg/ultraHex issue #23: Add Efuse

> Source: https://github.com/bitaxeorg/ultraHex/issues/23
> Collected: 2026-10-07
> Published: 2024-02-27

- Repository: bitaxeorg/ultraHex
- Type: issue
- Number: 23
- State: closed
- Author: benjamin-wilson
- Opened: 2024-02-27
- Closed: 2024-06-06
- Labels: none

## Description

For power monitoring and safety 

## Comments

### macphyter on 2024-03-24

This is not so easy to do, given the limited amount of space around the main power input.  We'll have to think about this one.

### nguyentruong190 on 2024-03-28

It is not really necessary, if needed, a fuse can be used in series with the wire
![2dd2d9e22e3f9a380e8b21e9e97e772acb681a87_original](https://github.com/skot/bitaxeHex/assets/61081470/53d33885-29ac-479c-9011-7f54ba812a37)


### macphyter on 2024-06-06

It was decided that the eFuse is too much of a burden at this point, since the TPS core voltage regulator already has shutdown capability for overcurrent and overvoltage.
