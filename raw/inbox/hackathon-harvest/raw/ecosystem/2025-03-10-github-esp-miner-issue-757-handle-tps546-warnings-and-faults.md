# bitaxeorg/ESP-Miner issue #757: Handle TPS546 warnings and faults

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/757
> Collected: 2026-10-07
> Published: 2025-03-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 757
- State: closed
- Author: skot
- Opened: 2025-03-10
- Closed: 2025-03-27
- Labels: enhancement, help wanted, critical

## Description

The [TPS546](https://www.ti.com/lit/ds/symlink/tps546d24a.pdf) has a built in set of monitors for things like VIN overvoltage, undervoltage, VOUT overvoltage, undervoltage, overcurrent and regulator overtemp. There are also some less severe warning like communication errors.

Most of these conditions have two levels of severity; "warn" and "fault". The thresholds for all of these values are configurable over I2C. It is also configurable what happens when these conditions are met, ranging from "ignore" to "restart" to "shutdown"

We should utilize this functionality to alert users (via AxeOS and maybe the OLED) that a fault has been detected and something needs to be done.

The partial implementation of these features is believed to be the cause of #588 

## Comments

### skot on 2025-03-10

There is a TI silicon bug in `VIN_UV_WARN_LIMIT` where it cannot be set to any value between around 2.5V to 8V, so it's useless for 5V Bitaxe. In this case set to 0V to disable.

### skot on 2025-03-13

I think we should go into fault mode on any of these:

- VOUT_OV
- VOUT_UV
- IOUT_OC
- VIN_UV
- TEMP

If any of the other ones happen we can print it to the log, but don;t need to go into vreg shutdown and fault mode.

### WantClue on 2025-03-20

@skot I think this can be closed
