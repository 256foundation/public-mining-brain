# bitaxeorg/ESP-Miner issue #1970: Fan RPM display will not move from 960RPM after clearing overheat error.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1970
> Collected: 2026-10-07
> Published: 2026-09-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1970
- State: open
- Author: perfguy2
- Opened: 2026-09-12
- Closed: n/a
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
If the device overheats, the fan RPM shows as 960 RPM. If you clear the overheat alert, the RPM stays that way even as the fan speeds up. The fan % does change, however. Changing firmware or even even doing a clean web flash without saving configuration does not change RPM, nor does trying an older firmware such as 2.13 or 2.14. Changing frequency does not fix the issue. 

**To Reproduce**
Steps to reproduce the behavior:
1. Overheat device
2. Look at the RPM on dashboard, It will be set at 960
3. Clear overheat error and reboot and RPM stays the same even while fan % changes and freq is moved to default

**Expected behavior**
The fan RPM display should change after the overheat alert is cleared and the device rebooted & freq moved to default. 

**Screenshots & Photos**
<img width="531" height="132" alt="Image" src="https://github.com/user-attachments/assets/73cdbc8a-d94c-4744-8339-2f12771be310" />

**Hardware (please complete the following information):**
 - Bitaxe 801 Turbo
 - Ali Express (yysluping)
 - ESP-Miner FW version: 2.15.0
 - Hash Frequency: 525Mhz
 - Voltage: 1125mv
 - Pool URL, Port, User: public-pool.io: 3333

**Additional context**
This only starting happening after overheat protection kicked in. 



## Comments

### awi81 on 2026-09-25

960 RPM is most likely not a stuck display value. It's what the EMC2103 driver reports when the fan controller sees no tach pulses at all. The EMC2103 is fitted on the Gamma Turbo (801), Naja Duo (1201) and Gamma Hex (1300).

`EMC2103_get_fan_speed()` computes `RPM = 7864320 / reading`, with `reading` being the 13-bit tach count. With no tach signal the count sits at its maximum of 8191, and 7864320 / 8191 = **960**. The "fan stopped" check below it (`if (RPM == 82) return 0;`) was written for the EMC2101, where a stalled fan gives 5400000 / 65535 = 82. On the EMC2103 the smallest possible value is 960, so that check can never trigger and a stopped fan shows up as 960 RPM.

That fits what you describe. The PWM side works (fan % changes), but no speed signal comes back, whatever firmware you flash. I'd check the fan itself and its tach wire and connector. A fan that stopped spinning would also explain the overheat in the first place.

Two firmware consequences worth fixing:
- The driver should return 0 for a saturated count (≥ 8191 after the shift) instead of 960, so the dashboard shows the fan as stopped.
- `self_test_fan_target_rpm` is 500 on these boards, so a dead fan reading 960 passes the self-test.

It's a one-line change in `EMC2103.c`; I can open a PR if that helps.
