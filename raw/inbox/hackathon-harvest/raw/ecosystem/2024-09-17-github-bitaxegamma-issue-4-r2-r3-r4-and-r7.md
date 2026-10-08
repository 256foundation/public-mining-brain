# bitaxeorg/bitaxeGamma issue #4: R2, R3, R4 and R7

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/4
> Collected: 2026-10-07
> Published: 2024-09-17

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 4
- State: closed
- Author: Alexgtc
- Opened: 2024-09-17
- Closed: 2024-09-19
- Labels: none

## Description

Does anyone know why the list of materials does not show the resistances r2, r3, r4 and r7 and in the gerbers yes? Can the plate be mounted leaving those resistors unmounted?

## Comments

### marplukiwi on 2024-09-19

According to the circuit diagram, the resistors are not needed
<img width="580" alt="Bildschirmfoto 2024-09-19 um 09 18 41" src="https://github.com/user-attachments/assets/86a11758-915c-4bb5-84e3-75351352876c">


### marplukiwi on 2024-09-19

According to the circuit diagram, the R18 is not needed either
<img width="261" alt="Bildschirmfoto 2024-09-19 um 09 37 45" src="https://github.com/user-attachments/assets/9c4d67a3-5691-4aa0-8767-d63ab674b3e3">


### Alexgtc on 2024-09-19

Ok, so leaving those resistors without mounting, the gamma bitaxe should work without problems, right?

### marplukiwi on 2024-09-19

If the documentation, i.e. the circuit diagram, is correct then yes. But I cannot confirm this.

### Alexgtc on 2024-09-19

Ok, I'll try to mount it without those resistances to see if it works. Thank you for the help.

### yellowpi on 2024-09-19

@skot dear skot, what do you say about this?

### skot on 2024-09-19

@marplukiwi is correct, R2, R3, R4 and R7 are DNP meaning "Do Not Place". 

### marplukiwi on 2024-09-20

@skot and R18 DNP or not? R18 is in the BOM but crossed out in the circuit diagram.

### skot on 2024-09-20

The red X in KiCad means DNP
