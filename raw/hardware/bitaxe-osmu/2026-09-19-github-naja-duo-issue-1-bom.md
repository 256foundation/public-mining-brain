# bitaxeorg/naja-duo issue #1: BOM

> Source: https://github.com/bitaxeorg/naja-duo/issues/1
> Collected: 2026-10-07
> Published: 2026-09-19

- Repository: bitaxeorg/naja-duo
- Type: issue
- Number: 1
- State: open
- Author: f1nch87
- Opened: 2026-09-19
- Closed: n/a
- Labels: none

## Description

Hey.
I have some issues wit the bom.


1. C4,C16,C21,C27,C44,C45,C48 
partno is wrong. I tells 0402 footprint but the parts are 0603.
 
2. C104, C106
Theres no partno listed and i dont find a fitting one.


Maybe someone could update the kicad footprint and bom.
Thanks

## Comments

### Zayno on 2026-09-19

Hi @f1nch87 , I'm building a miner with a single BM1373. Would you please review my files too? I will update my repo soon with the latest.

### f1nch87 on 2026-09-19

> Hi @f1nch87 , I'm building a miner with a single BM1373. Would you please review my files too? I will update my repo soon with the latest.

Oh i can try. But im not good in this. Its my first bitaxe build

### Zayno on 2026-09-19

@f1nch87 message me on discord "majorduke." thanks

### f1nch87 on 2026-09-19

> Hey. I have some issues wit the bom.
> 
> 1. C4,C16,C21,C27,C44,C45,C48
>    partno is wrong. I tells 0402 footprint but the parts are 0603.
> 2. C104, C106
>    Theres no partno listed and i dont find a fitting one.
> 
> Maybe someone could update the kicad footprint and bom. Thanks

Ok i did found out that:

C4,C16,C21,C27,C44,C45,C48 has the wrong PARTNO in Kicad but the real Datasheet. Thats why the footprint mismatches. The real partno is **EMK105BJ105MV-F**

L2,L3 in the BOM is very difficult to get anywhere. So i changed it to **DFE201612E-1R5M=P2**

Still dunno what 120uf cap i choose for c104,106.
Maybe this Panasonic C6 20SVPF120M?
Its named as panasonic c6 in the footprint editor.
