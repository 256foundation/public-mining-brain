# bitaxeorg/ESP-Miner issue #258: BM1366 init() possible problem

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/258
> Collected: 2026-10-07
> Published: 2024-07-18

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 258
- State: closed
- Author: Georges760
- Opened: 2024-07-18
- Closed: 2024-09-11
- Labels: none

## Description

This [line](https://github.com/skot/ESP-Miner/blob/master/components/bm1397/bm1366.c#L465C61-L465C71) in the BM1366 init() change the UART baudrate of the Chip to a higher one. So all command after this line should be ignored by the ASIC because of baudrate mismatch...

I don't understand how it is functional with this line !


## Comments

### WantClue on 2024-07-25

have you tried to match it and see what happens ? :D
