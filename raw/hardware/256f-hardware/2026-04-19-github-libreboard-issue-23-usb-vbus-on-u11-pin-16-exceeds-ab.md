# 256foundation/libreboard issue #23: USB_VBUS on U11 pin 16 exceeds absolute maximum

> Source: https://github.com/256foundation/libreboard/issues/23
> Collected: 2026-10-07
> Published: 2026-04-19

- Repository: 256foundation/libreboard
- Type: issue
- Number: 23
- State: open
- Author: rkuester
- Opened: 2026-04-19
- Closed: n/a
- Labels: none

## Description

On rev 1, USB_VBUS, U11 pin 16, meant for detecting the ready state of VBUS, is tied directly to the 5V VBUS, violating the absolute maximum of 1.4V specified in section 7.1 of the [datasheet].

The pin function table in section 6 and implementation note in figure 26 recommends a voltage divider to keep the pin 16 input within the 1.15V maximum recommended in section 7.3.

[datasheet]: https://www.ti.com/lit/ds/symlink/tusb4041i.pdf
