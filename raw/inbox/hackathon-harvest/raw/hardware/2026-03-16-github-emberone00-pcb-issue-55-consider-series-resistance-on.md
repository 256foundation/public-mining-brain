# 256foundation/emberone00-pcb issue #55: Consider series resistance on cross-domain signals

> Source: https://github.com/256foundation/emberone00-pcb/issues/55
> Collected: 2026-10-07
> Published: 2026-03-16

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 55
- State: open
- Author: rkuester
- Opened: 2026-03-16
- Closed: n/a
- Labels: none

## Description

When VIN is present without USB power (or vice versa), signals that cross between the two power domains can back-drive into unpowered ICs. Consider adding series resistance on cross-domain signals like EN, PGOOD, ALERT, and SCL/SDA to limit the current.

Hardware version: v5 (9f75f0c)
