# bitaxeorg/ESP-Miner issue #1585: `unknown` share reject reason on ckpool

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1585
> Collected: 2026-10-07
> Published: 2026-03-02

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1585
- State: closed
- Author: mutatrum
- Opened: 2026-03-02
- Closed: 2026-03-06
- Labels: none

## Description

ckpool changes the format of the share rejection reason error message:
`{"result":false,"error":"Stale","id":618}`
The code doesn't parse this at the moment, and only shows `unknown`.

Caused-by: https://bitbucket.org/ckolivas/ckpool/commits/eaab0b78a2c7f2e0fac15ba737e2080f9316fb7c
