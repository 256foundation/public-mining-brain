# 256foundation/asic-rs issue #104: Does not support S21eXP Hydro.

> Source: https://github.com/256foundation/asic-rs/issues/104
> Collected: 2026-10-07
> Published: 2025-11-21

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 104
- State: closed
- Author: moonbootspleb
- Opened: 2025-11-21
- Closed: 2025-12-04
- Labels: none

## Description

Notes from Mykel at Satokie 

“When trying to curtail the machines on foreman with the new FW, the following error is encountered:
 
"get bitmain-work-mode failed"
 
Manual testing on the miners confirmed that sleep mode can be successfully activated via the dashboard, indicating that the firmware inherently supports this functionality.
 
Analysis of the miner logs further revealed that the firmware utilizes:
 
"2025-11-11 14:07:57 cmd : set_miner_conf"
 
rather than the previously used endpoint:
 
"set_work_mode"”

## Comments

### b-rowan on 2025-11-25

What is the `minertype` reported at `/cgi-bin/get_system_info.cgi`?

### moonbootspleb on 2025-12-01

Standby...

### moonbootspleb on 2025-12-01

Minertype is "Antminer S21e XP Hyd."

### moonbootspleb on 2025-12-01

Board chip count is 166

### moonbootspleb on 2025-12-01

Correction 160
