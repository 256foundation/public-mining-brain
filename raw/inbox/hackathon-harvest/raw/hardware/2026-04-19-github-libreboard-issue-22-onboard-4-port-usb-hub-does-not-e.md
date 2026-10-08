# 256foundation/libreboard issue #22: Onboard 4-port USB hub does not enumerate

> Source: https://github.com/256foundation/libreboard/issues/22
> Collected: 2026-10-07
> Published: 2026-04-19

- Repository: 256foundation/libreboard
- Type: issue
- Number: 22
- State: open
- Author: rkuester
- Opened: 2026-04-19
- Closed: n/a
- Labels: none

## Description

On rev 1, the 4-port USB hub U11 never enumerates upstream. `lsusb` shows only the root hubs, and the kernel log contains zero connect events on any root port.

There are a few suspicious datasheet violations, filed here as sub-issues. If rework confirms any to be a cause, I will note it.

The hub did work for at least several hours prior to exhibiting this issue dependably. That in itself may be relevant.
