# bitaxeorg/bitaxeGamma issue #49: BOM List J1 DC Power Jack Incompatible

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/49
> Collected: 2026-10-07
> Published: 2025-10-07

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 49
- State: open
- Author: lrstolk
- Opened: 2025-10-07
- Closed: n/a
- Labels: none

## Description

I found out the advised J1 - DC Power Jack does actually not meet the requirements. 

The CSV BOM list tells me to use LCSC part C431534. This is max 30V 2A. While the README tells me I need a power supply of 5V with 4A, this exceeds the power of what the DC Power Jack can hold. 

Any advice of what to do? I already placed a pick and placed order on LCSC. 

 

## Comments

### skot on 2025-10-07

Uuf, sorry I didn't notice this before. The DigiKey part number is rated for 5.5A I've removed the LCSC part number from the BOM.

Maybe you can contact JLCPCB and have them DNP this part on your build?

### lrstolk on 2025-10-08

> Uuf, sorry I didn't notice this before. The DigiKey part number is rated for 5.5A I've removed the LCSC part number from the BOM.
> 
> Maybe you can contact JLCPCB and have them DNP this part on your build?

No worries, they've already shipped it and I've ordered the ones from DigiKey. The rest of the BOM is fine right?
