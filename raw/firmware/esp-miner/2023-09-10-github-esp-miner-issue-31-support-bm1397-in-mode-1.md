# bitaxeorg/ESP-Miner issue #31: Support bm1397 in mode_1

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/31
> Collected: 2026-10-07
> Published: 2023-09-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 31
- State: closed
- Author: BONIIXS
- Opened: 2023-09-10
- Closed: 2023-09-24
- Labels: none

## Description

Hey there I just wanted to ask if it was possible to use the firmware with a custom miner with the same hardware but the BM1397 will be in mode 1, is it possible?

## Comments

### skot on 2023-09-10

Yes, definitely! AFAIK esp-miner doesn't care what mode the ASIC is in.

### johnny9 on 2023-09-10

What does mode 1 refer to?

### skot on 2023-09-10

"Mode" in this context is a pin on the ASIC that reverses the side the data input and output pins are on. It dramatically simplifies PCB routing. 

### BONIIXS on 2023-09-10

Thanks for the answer but does it also support chaining(multiple asic chips in series)

### skot on 2023-09-11

we have added theoretical support for multiple ASICs to esp-miner. But until one of the hex designs is done it's untested.

### BONIIXS on 2023-09-11

I think I can make one
