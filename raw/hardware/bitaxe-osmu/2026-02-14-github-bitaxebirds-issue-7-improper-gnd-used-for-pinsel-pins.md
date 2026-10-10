# bitaxeorg/bitaxeBIRDS issue #7: Improper GND used for Pinsel pins in Pre Bonanza Branch

> Source: https://github.com/bitaxeorg/bitaxeBIRDS/issues/7
> Collected: 2026-10-07
> Published: 2026-02-14

- Repository: bitaxeorg/bitaxeBIRDS
- Type: issue
- Number: 7
- State: closed
- Author: aadhi1014
- Opened: 2026-02-14
- Closed: 2026-02-15
- Labels: none

## Description

I observed that GND2 was used for PINSEL but the chip's VSS was at GND3 

<img width="546" height="484" alt="Image" src="https://github.com/user-attachments/assets/697392f5-4278-4463-99a7-2f439849812a" />

## Comments

### skot on 2026-02-15

good catch! I was just looking at this scratching my head

### skot on 2026-02-15

fwiw the pre-bonanza branch is now the [bitaxeBonanza 1002x](https://github.com/bitaxeorg/bitaxeBonanza/tree/1002x)
