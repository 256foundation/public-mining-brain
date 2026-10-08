# 256foundation/emberone00-pcb issue #2: LM25119 output voltage drops with load > 9A

> Source: https://github.com/256foundation/emberone00-pcb/issues/2
> Collected: 2026-10-07
> Published: 2024-10-29

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 2
- State: closed
- Author: skot
- Opened: 2024-10-29
- Closed: 2024-10-29
- Labels: bug

## Description

LM25119 output voltage stays right about the 3.6V setpoint until the current exceeds 9A then it falls to 1.6V, and there is some audible regulator whine.

## Comments

### skot on 2024-10-29

this happens at lower currents with lower input voltage and at higher currents with higher input voltages..

### skot on 2024-10-29

Also a PICNIC error with my lab PSU settings 😅
