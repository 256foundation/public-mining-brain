# 256foundation/emberone00-pcb issue #21: change full scale range resistor on DS4432U

> Source: https://github.com/256foundation/emberone00-pcb/issues/21
> Collected: 2026-10-07
> Published: 2025-02-28

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 21
- State: closed
- Author: skot
- Opened: 2025-02-28
- Closed: 2025-04-09
- Labels: enhancement

## Description

The S19j Pro comes with the APW121215 PSU which can output a range of 12-15V. with 42 voltage domains per hashboard, this means that each chip will receive from 285mV to 357mV. 

We need to adjust the full scale range on the DS4432U in order to better cover this core voltage range.

Setting the R_FS resistor, aka R11 on the emberOne to 39kOhms, this give us an adjustable range of 239mV to 360mV for each of the 12 ASICs.

## Comments

### skot on 2025-04-09

fixed in v3
