# 256foundation/libreboard issue #26: TEST U11 pin 17 left floating

> Source: https://github.com/256foundation/libreboard/issues/26
> Collected: 2026-10-07
> Published: 2026-04-19

- Repository: 256foundation/libreboard
- Type: issue
- Number: 26
- State: open
- Author: rkuester
- Opened: 2026-04-19
- Closed: n/a
- Labels: none

## Description

On rev 1, U11 pin 17 TEST is left floating. This probably works, the [datasheet] pin function table in section 6 indicates pin 17 TEST is internally pulled down; however, their Figure 32 has this pin pulled down externally through 4.7k. Since we're experiencing a yet-unexplained failure of U11 to boot, it may be advisable to follow their application example and pull TEST down externally for good measure.

[datasheet]: https://www.ti.com/lit/ds/symlink/tusb4041i.pdf
