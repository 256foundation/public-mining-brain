# 256foundation/libreboard issue #21: Consider wiring the USB hub in a per-port power switched configuration

> Source: https://github.com/256foundation/libreboard/issues/21
> Collected: 2026-10-07
> Published: 2026-03-19

- Repository: 256foundation/libreboard
- Type: issue
- Number: 21
- State: open
- Author: rkuester
- Opened: 2026-03-19
- Closed: n/a
- Labels: none

## Description

Per the [datasheet] section 5, the TUSB4041I usb hub supports per-port or ganged power switching; however, it is currently wired up in a ganged configuration. Per-port power switching would enable Mujina to affect a better reset of connected hash boards. See 256foundation/emberone00-pcb#57.

[datasheet]: https://www.ti.com/lit/ds/symlink/tusb4041i.pdf
