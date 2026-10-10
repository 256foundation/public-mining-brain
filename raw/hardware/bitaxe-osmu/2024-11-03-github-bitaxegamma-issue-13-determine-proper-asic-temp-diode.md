# bitaxeorg/bitaxeGamma issue #13: Determine proper ASIC temp diode series resistance

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/13
> Collected: 2026-10-07
> Published: 2024-11-03

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 13
- State: open
- Author: skot
- Opened: 2024-11-03
- Closed: n/a
- Labels: bug

## Description

<img width="804" alt="image" src="https://github.com/user-attachments/assets/dbf0b1df-9965-455d-ab8f-bd3a69ca4cf4">

R22 and R23 are series resistors inline with the ASIC temp diode, used for measuring the ASIC die temp.

The [EMC2101 datasheet](https://ww1.microchip.com/downloads/aemDocuments/documents/MSLD/ProductDocuments/DataSheets/EMC2101-Data-Sheet-DS20006703.pdf) says;

> Parasitic resistance in series with the external diodes will limit the accuracy obtainable from temperature measurement devices. The voltage developed across this resistance by the switching diode currents cause the temperature measurement to read higher than the true temperature. Contributors to series resistance are Printed Circuit Board (PCB) trace resistance, on die (i.e. on the processor) metal resistance, bulk resistance in the base and emitter of the temperature transistor. Typically, the error caused by series resistance is +0.7°C per ohm. Temperature errors caused by up to 100Ω of series resistance are automatically corrected.

Is 100 Ohms in series the right call? Maybe we don't need _any_ series resistance here? Does this have something to do with #12 ?
