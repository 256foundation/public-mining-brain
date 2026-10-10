# bitaxeorg/ESP-Miner issue #311: IntegerDivideByZero Error when no chip detected

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/311
> Collected: 2026-10-07
> Published: 2024-08-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 311
- State: closed
- Author: CyberSensei1
- Opened: 2024-08-29
- Closed: 2025-03-27
- Labels: accepted

## Description

If there is no chip or not good sholdered chip you will get error below:

```

I (3191) bm1366Module: 0 chip(s) detected on the chain, expected 1
Guru Meditation Error: Core  0 panic'ed (IntegerDivideByZero). Exception was unhandled.

Core  0 register dump:
PC      : 0x42012b66  PS      : 0x00060f30  A0      : 0x82012dae  A1      : 0x3fca74a0  
A2      : 0x00000000  A3      : 0x00000000  A4      : 0x00000001  A5      : 0x3fc9ffd0  
A6      : 0x0000000b  A7      : 0x0000000b  A8      : 0x00000100  A9      : 0x3fca7470  
A10     : 0x3fca74e3  A11     : 0x0000000b  A12     : 0x0000000a  A13     : 0x3fca74ee  
A14     : 0x00000000  A15     : 0x3fcb8608  SAR     : 0x0000001d  EXCCAUSE: 0x00000006  
EXCVADDR: 0x00000000  LBEG    : 0x40056f5c  LEND    : 0x40056f72  LCOUNT  : 0xffffffff  


Backtrace: 0x42012b63:0x3fca74a0 0x42012dab:0x3fca7590 0x4200b60c:0x3fca75b0 0x420acebb:0x3fca7600 0x4037e15d:0x3fca7630




ELF file SHA256: 4c08c16e4

Rebooting...
```

## Comments

### CyberSensei1 on 2024-08-29

Maybe we can check it with >0 but i dont think there will be negative integer return as detected chip count

### skot on 2025-02-24

@axisray do we need to open this back up? is it still occuring?

### AxisRay on 2025-02-25

> [@AxisRay](https://github.com/AxisRay) do we need to open this back up? is it still occuring?

In my opinion, this issue should be fixed. Currently, the system keeps restarting repeatedly, and users might not understand what is happening.
we should halt  and display an error message on the screen.
