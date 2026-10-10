# bitaxeorg/ESP-Miner issue #148: Is 'power_management->HAS_POWER_EN' and 'power_management->HAS_PLUG_SENSE' also valid for board version 205 ?

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/148
> Collected: 2026-10-07
> Published: 2024-03-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 148
- State: closed
- Author: MoellerDi
- Opened: 2024-03-21
- Closed: 2024-03-25
- Labels: none

## Description

**Describe the bug**
As per the code at 'main/tasks/power_management_task.c', power_management->HAS_POWER_EN and 'power_management->HAS_PLUG_SENSE' only being enabled for board version < 205.

https://github.com/skot/ESP-Miner/blob/a5daff7b015fbe5331d759ef612bda937e4ab0ad/main/tasks/power_management_task.c#L45-L48

I wonder if board version 205 also got such functionality and it was just forgotten to enable it in the code.
Happy to raise a PR once one of the devs confirmed it's actually kind of a bug.

**To Reproduce**
No error detected, I was just reading the code and noticed it

**Expected behavior**
board version 205 seems being the successor of 204 and it might have at least the same/similar (maybe improved) functionality. As per the hardware design at https://github.com/skot/bitaxe/compare/204...205 just some changes in layout were made, like moving USB around, etc.

**Screenshots & Photos**
n/a

**Hardware (please complete the following information):**
 - Bitaxe HW version: Ultra 205
 - Bitaxe HW vendor: eBay
 - ESP-Miner FW version: 2.1.3
 - Hash Frequency: 550
 - Voltage: 1300
 - Pool URL, Port, User: public-pool.io


## Comments

### skot on 2024-03-21

Thanks for this report, and nice catch!
We were going to use the barrel plug "plug sense" pin to detect if the 5V power was applied or not. Mostly to prevent people from trying to power the Bitaxe off USB only (it'll work, but poorly). Then we had a crisis with barrel plug part availability and decided to just DNP the USB 5V diode, effectively disconnecting USB from 5V all together. I think this is working pretty well, so we can probably eliminate this PLUG_SENSE code.

### MoellerDi on 2024-03-22

Thanks Skot, as older board rev. still exist, this PLUG_SENSE code might be still needed (to prevent people from trying to power older board rev. off USB only). I just made PR #149 to add latest board version 205 until the devs are ready to eliminate the PLUG_SENSE code ;-)
