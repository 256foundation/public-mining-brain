# 256foundation/emberone00-pcb issue #28: add TVS protection diodes on voltage regulator VIN and VOUT

> Source: https://github.com/256foundation/emberone00-pcb/issues/28
> Collected: 2026-10-07
> Published: 2025-04-18

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 28
- State: open
- Author: skot
- Opened: 2025-04-18
- Closed: n/a
- Labels: enhancement

## Description

- on VIN i'll try [SMCJ28A](https://www.digikey.com/en/products/detail/taiwan-semiconductor-corporation/SMCJ28A/1051842)
- on VOUT i'll try [SMBJP6KE6.8A-TP](https://www.digikey.com/en/products/detail/mcc-micro-commercial-components/SMBJP6KE6-8A-TP/2345608)

air wire them first, if that seems reasonable add them to the board

note: both of these are unidirectional variants. Orient them with the cathode (band) to VOUT (3.6 V) and anode to GND
