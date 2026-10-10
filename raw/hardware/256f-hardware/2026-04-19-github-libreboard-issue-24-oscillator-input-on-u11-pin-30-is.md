# 256foundation/libreboard issue #24: Oscillator input on U11 pin 30 is driven at 3.3V but requires 1.8V

> Source: https://github.com/256foundation/libreboard/issues/24
> Collected: 2026-10-07
> Published: 2026-04-19

- Repository: 256foundation/libreboard
- Type: issue
- Number: 24
- State: open
- Author: rkuester
- Opened: 2026-04-19
- Closed: n/a
- Labels: none

## Description

Y1 outputs a 3.3V clock which directly drives XI, U11 pin 30, violating the absolute maximum input voltage of 2.45V specified in [datasheet] section 7.1.

Section 8.3.6 requires a 1.8V clock source.

[datasheet]: https://www.ti.com/lit/ds/symlink/tusb4041i.pdf
