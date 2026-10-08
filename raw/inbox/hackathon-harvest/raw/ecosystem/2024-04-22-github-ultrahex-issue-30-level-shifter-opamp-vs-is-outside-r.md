# bitaxeorg/ultraHex issue #30: Level shifter Opamp Vs is outside recommended operating range

> Source: https://github.com/bitaxeorg/ultraHex/issues/30
> Collected: 2026-10-07
> Published: 2024-04-22

- Repository: bitaxeorg/ultraHex
- Type: issue
- Number: 30
- State: closed
- Author: skot
- Opened: 2024-04-22
- Closed: 2024-05-24
- Labels: bug

## Description

The [TLV3544](https://www.ti.com/lit/ds/symlink/tlv3544.pdf) used as the cross-domain level shifter is powered by VDD and -VDD which is most cases is 2.4V. The TLV3544 says the min Vs is 2.5V. (Although max operating doesn't have a min).
<img width="335" alt="image" src="https://github.com/skot/bitaxeHex/assets/140785/19baa0b6-8603-4a51-b9ed-79f29640a2f9">

<img width="928" alt="image" src="https://github.com/skot/bitaxeHex/assets/140785/01520946-379d-4a6f-b69f-93a2c471ddcf">
<img width="932" alt="image" src="https://github.com/skot/bitaxeHex/assets/140785/6b60da29-a018-4eef-80ae-99bb3fe117ab">

pmaxuw recommends setting Vs to 5V. This should be checked against the datasheet and/or tested.


## Comments

### shufps on 2024-04-23

OP should be powered with 5V and GND. Seems Nine9Seven already tested it and confirmed that the level shifting still works.

### macphyter on 2024-05-24

Fixed on schematic and layout on v304
