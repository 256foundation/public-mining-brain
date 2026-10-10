# bitaxeorg/BitaxeGT issue #17: SYNC_FAULT with TPS546D24A

> Source: https://github.com/bitaxeorg/BitaxeGT/issues/17
> Collected: 2026-10-07
> Published: 2025-09-29

- Repository: bitaxeorg/BitaxeGT
- Type: issue
- Number: 17
- State: open
- Author: skot
- Opened: 2025-09-29
- Closed: n/a
- Labels: bug

## Description

There appears to be an undocumented silicon-level issue with the TPS546D24**A** variant voltage regulator in a multi-phase setup that results in a SYNC_FAULT shutdown after ~20 minutes of use. The issue does not occur with an otherwise identical PSU, PCB, firmware config but with the newer TPS546D24**S** fitted. TPS546D24**S** based BitaxeGT builds have run without fault for weeks.

I have not been able to find any combination of TPS546D24 register config register settings that solves this issue with the TPS546D24**A**. Texas Instruments support suggested that this might be a noise issue on the VSHARE, SYNC and/or BCX signals connecting the two phases. Being as this issue does not occur on an identical build with the TPS546D24**S** (and the noise is not significant anyways) this points to a specific issue with the TPS546D24**A**.
