# bitaxeorg/bitaxeGamma issue #10: BOM change U7

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/10
> Collected: 2026-10-07
> Published: 2024-10-24

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 10
- State: closed
- Author: BitMaker-hub
- Opened: 2024-10-24
- Closed: 2025-03-03
- Labels: none

## Description

Hi Skot,

Seems previously used crystal 25,0-JO32-B-1V3-1-T1-LF is out of voltage range currently used in GAMMA. 
BOM still says 25,0-JO32-B-1V3-1-T1-LF ofr U7.

Can you change it to SX3M25.000E20F30THN, to avoid others mistake?




## Comments

### skot on 2024-10-24

This is a really unfortunate CSV parsing error. I've fixed it in the 600 release already. I think it might still need to be fixed in the unreleased branches
