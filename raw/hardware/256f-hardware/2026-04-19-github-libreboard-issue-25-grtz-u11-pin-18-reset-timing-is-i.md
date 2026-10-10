# 256foundation/libreboard issue #25: GRTz U11 pin 18 reset timing is insufficient

> Source: https://github.com/256foundation/libreboard/issues/25
> Collected: 2026-10-07
> Published: 2026-04-19

- Repository: 256foundation/libreboard
- Type: issue
- Number: 25
- State: open
- Author: rkuester
- Opened: 2026-04-19
- Closed: n/a
- Labels: none

## Description

On rev1, the U11 pin 18 GRTz reset pin is required by [datasheet] section 8.3.7 to be held for a minimum of 3ms after the U11 power inputs are stable. The step response of the current RC, 10k ohm * 100nF = 1ms, reaches the V_IH threshold (section 7.5) of 2V in less than 1 RC (3.3V * 0.63 = 2.08V), well under the required 3ms.

[datasheet]: https://www.ti.com/lit/ds/symlink/tusb4041i.pdf
