# bitaxeorg/bitaxeGamma issue #47: TPS546D24x BCX & SYNC pins should be grounded for single phase

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/47
> Collected: 2026-10-07
> Published: 2025-09-02

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 47
- State: open
- Author: skot
- Opened: 2025-09-02
- Closed: n/a
- Labels: bug, enhancement

## Description

according to the TPS546D24A datasheet, when used in standalone mode, single phase mode (like we have on the Gamma) the BCX pins should be connected to ground.

<img width="1557" height="684" alt="Image" src="https://github.com/user-attachments/assets/f33b2434-f960-4905-8311-675915b8ac31" />

We currently have them floating. Doesn't _seem_ like this is causing any problems...

## Comments

### skot on 2025-09-03

Looks like in single phase operation the BCX pins _can_ be floating, but SYNC should definitely be grounded.
