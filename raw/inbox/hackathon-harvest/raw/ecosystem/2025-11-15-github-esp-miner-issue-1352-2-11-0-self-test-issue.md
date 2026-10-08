# bitaxeorg/ESP-Miner issue #1352: 2.11.0 Self Test Issue

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1352
> Collected: 2026-10-07
> Published: 2025-11-15

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1352
- State: closed
- Author: MidwestChris
- Opened: 2025-11-15
- Closed: 2025-12-02
- Labels: question

## Description

Updating new devices that past self test in 2.10.1 up to 2.11.0 using VScode.  Devices are now failing on "Powerfail" during self test.  If i roll them back to 2.10.1 and then update to 2.11.0 via dashboard devices work fine with no apparent issues.  

Gamma 601
TPS546D24A

I have included the logs for a single device that is exhibiting this behavior however every gamma so far that I have attempted to update (3) is having the same issue 

[2.10.1 Self Test Log Pass.txt](https://github.com/user-attachments/files/23562142/2.10.1.Self.Test.Log.Pass.txt)

[2.11.0 Running Log After Update from 2.10.1 on dashboard.txt](https://github.com/user-attachments/files/23562144/2.11.0.Running.Log.After.Update.from.2.10.1.on.dashboard.txt)

[2.11.0 Self Test Log Fail.txt](https://github.com/user-attachments/files/23562151/2.11.0.Self.Test.Log.Fail.txt)




## Comments

### WantClue on 2025-11-29

Has this been resolved @MidwestChris or is this still happening ? 

### MidwestChris on 2025-11-30

Still seeing the issue


### powerminingfarm on 2025-12-02

Also noticed this issue.
@WantClue any idea what could be causing this?
Except ours is 602.

### mutatrum on 2025-12-02

I think if the power draw is below the expected value, and the hasrate is achieved, it should be a pass.

```
I (16950) self_test: Power: 14.907349
E (16953) self_test: Power Draw Failed, target 19.00
I (16969) vcore: Set ASIC voltage = 0.000V
I (16969) self_test: SELF-TEST FAIL! -- Hold BOOT button for 2 seconds to cancel self-test, or press RESET to run self-test again.
```

### ghost on 2025-12-02

Not sure if this is related... but adding it here.

I can reproduce this (normal mode) when a 5v 6amp PSU is used, but not the self test issue reported here, the self tests pass.

I have 3 5v 6amp PSU's, when two of them are used, the Gamma's throw power fault (firmware v2.11.x).

<img width="1908" height="583" alt="Image" src="https://github.com/user-attachments/assets/7e12a592-db96-47b2-905f-5a263792d715" />

When I use the LRS-350-5 PSU this issue/error does not show.

Waiting for some new PSU's to arrive this week to do more tests with.

This below is what is in the logs when the 5v 6amp PSU's are used.

```[0;32mI (15698) power_management: Temp: 30.2 Â°C, SetPoint: 54.0 Â°C, Output: 25.0% (P:15.0 I:0.2 D_val:20.0 D_start_val:20.0)[0m
[0;32mI (15702) create_jobs_task: New Work Dequeued 63bbf[0m
[0;31mE (15714) TPS546: Status: 0x0840[0m
[0;32mI (15719) create_jobs_task: New pool difficulty 65536[0m
[0;31mE (15722) TPS546: The voltage regulator is turned off[0m
[0;32mI (15728) create_jobs_task: Set chip version rolls 65535[0m```
