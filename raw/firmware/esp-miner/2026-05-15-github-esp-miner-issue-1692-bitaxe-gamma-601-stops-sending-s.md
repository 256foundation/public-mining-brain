# bitaxeorg/ESP-Miner issue #1692: Bitaxe Gamma 601 stops sending shares, weird things inside log, hashrate/error rate flat lines or goes to 0.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1692
> Collected: 2026-10-07
> Published: 2026-05-15

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1692
- State: open
- Author: IdotMaster1
- Opened: 2026-05-15
- Closed: n/a
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
Bitaxe Gamma 601 mines for a certain period, then either stops sending shares and flatlines, or starts attempting to use the same nonce over and over or the hashrate crashes to 0.
It is running the latest firmware.

**To Reproduce**
Steps to reproduce the behavior:
?, I am not sure this can be reproduced on other Bitaxe Gamma's.

**Expected behavior**
It is expected that the Gamma keeps hashing as it should.

**Screenshots & Photos**
Attached to issue.

<img width="738" height="717" alt="Image" src="https://github.com/user-attachments/assets/a92cf25d-8ae7-426d-94ba-5a383e2c23a0" />
<img width="1341" height="337" alt="Image" src="https://github.com/user-attachments/assets/f27570b5-6491-4cba-99ca-fca2f8c0f282" />
<img width="1322" height="667" alt="Image" src="https://github.com/user-attachments/assets/2cca21bd-e348-496e-b77f-6c410c0d32cc" />
<img width="1362" height="916" alt="Image" src="https://github.com/user-attachments/assets/337df89d-9e7f-4dc5-8b9d-d69072c1434a" />
<img width="447" height="216" alt="Image" src="https://github.com/user-attachments/assets/f1f02b59-81fb-4e38-bbb9-44c1b738e767" />

**Additional context**
Lowering the voltage and frequency makes it stable for longer. At 1100/400 it stayed stable for 30 minutes until issues started.
This issue was made by the request of adamwest1__0 on the OSMU Discord.

## Comments

### IdotMaster1 on 2026-05-15

Firmware Version	v2.13.1
AxeOS Version	v2.13.1
ESP-IDF Version	v5.5.2

### mutatrum on 2026-05-15

Related #1053 

### mutatrum on 2026-05-15

Does this also happen on default frequency and  voltage?

### IdotMaster1 on 2026-05-15

At the default frequency and voltage it failed earlier. I tested setting the voltage higher but to no avail. When I lowered it to  1100/400 it worked for around 30 minutes, then failed again.

### IdotMaster1 on 2026-05-15

I have attempted to use a modded ATX PSU but it eventually flat lined too.
