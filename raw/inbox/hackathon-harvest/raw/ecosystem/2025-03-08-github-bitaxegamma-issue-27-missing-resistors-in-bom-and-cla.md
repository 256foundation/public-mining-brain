# bitaxeorg/bitaxeGamma issue #27: Missing Resistors in BOM and Clarification on DNP Components

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/27
> Collected: 2026-10-07
> Published: 2025-03-08

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 27
- State: closed
- Author: loden-nodeway
- Opened: 2025-03-08
- Closed: 2025-03-16
- Labels: none

## Description

To whom it may concern,

I noticed that the BOM list is missing several resistors: R2, R3, R4, R7, R18, R20, R22, and R23. After checking the schematic, I found that R2, R3, R4, and R7 are marked as DNP (Do Not Place). However, R18, R20, R22, and R23 do not appear to be DNP.

Could you please confirm if my observation is correct? Also, I would appreciate it if you could provide the component names for these resistors.

Thank you for your attention to this matter.

Best regards,
Loden. 

## Comments

### Marcocanc on 2025-03-16

+1

### skot on 2025-03-16

R2, R3, R4, R7, R18 are DNP on the schematic.
R20 doesn't exist
R22 & R23 are on the BOM: https://github.com/bitaxeorg/bitaxeGamma/blob/a325117698b93c3a2e064ae0e7f2b570a8666134/Manufacturing%20Files/bitaxeGamma-BOM.csv#L32
