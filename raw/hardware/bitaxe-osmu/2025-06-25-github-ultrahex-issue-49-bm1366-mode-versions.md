# bitaxeorg/ultraHex issue #49: BM1366 mode versions

> Source: https://github.com/bitaxeorg/ultraHex/issues/49
> Collected: 2026-10-07
> Published: 2025-06-25

- Repository: bitaxeorg/ultraHex
- Type: issue
- Number: 49
- State: open
- Author: VoltMike
- Opened: 2025-06-25
- Closed: n/a
- Labels: none

## Description

Hello all, 

what is the difference between the BM1366_mode0 and BM1366_mode1 ASICs in the BOM list?
The schematic shows completely diffrent pinouts for the both chip versions.

Is the difference in the difference given in the parts label AL and AG? If yes which one is mode_0 and mode_1?

Thx in advance.

BR
Mike

## Comments

### skot on 2025-06-25

The PIN_MODE pin controls which signals are on which pins. It essentially controls which side of the chip the inputs and outputs are on. We have different schematic symbols for the two modes so that the pin names match up

### VoltMike on 2025-06-26

Hi skot, 
thx for your fast answer.
So it means it makes no difference for the placed ASIC component we can use 6 times the same IC? 
Backround of my question is, that we have produced three 303 PCBAs but every Bitaxe 303 is only hashing with one ASIC. 
In the terminal every board detects only 5 of 6 ASICs.

Following the link where i refere to that issue. Could you have a short look on it? 

https://github.com/TinyChipHub/ESP-Miner-TCH/issues/12

Do you have any idea where the failer could be?

Best regards
Mike

### skot on 2025-06-26

That's correct, it is the same ASIC for both modes.

The ultraHex design is correct, afaik.

My guess is this is a soldering issue (less likely because you have the same problem on 3 units), a BOM issue, or a firmware issue.

Doubly check the actual parts placed with the BOM. 

As far as the firmware goes, I haven't been following the TCH fork of esp-miner, so not much I can offer you there.
