# 256foundation/emberone00-pcb issue #22: NRST signals should have pulldowns when crossing voltage domains

> Source: https://github.com/256foundation/emberone00-pcb/issues/22
> Collected: 2026-10-07
> Published: 2025-03-05

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 22
- State: closed
- Author: skot
- Opened: 2025-03-05
- Closed: 2025-04-09
- Labels: bug

## Description

Looking at the S19j Pro hashboard it looks like every NRST line has a 2k pulldown. I did not see any of the 33ohm series resistors that the other signals have.

## Comments

### skot on 2025-03-05

on further inspection it looks like NRST signals _that cross voltage domains_ do have 33ohm series resistors.

furthermore, the NRST pulldown is connected to GND on the **NRSTO** side.

### skot on 2025-04-09

fixed in v3
