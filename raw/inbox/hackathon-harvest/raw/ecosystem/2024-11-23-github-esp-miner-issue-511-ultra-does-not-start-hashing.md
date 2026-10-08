# bitaxeorg/ESP-Miner issue #511: Ultra does not start hashing

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/511
> Collected: 2026-10-07
> Published: 2024-11-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 511
- State: closed
- Author: ghost
- Opened: 2024-11-23
- Closed: 2024-12-01
- Labels: none

## Description

Release firmware v2.4.0 - 205 works fine.

Firmware built 11/21/24 (locally) onwards with recent updates / PR's that have been merged to the master branch are causing issues with the Ultra 205, issues are not seen on Supra (401) or Gamma (601).

1/ Visual issue with Dashboard
2/ Low hash rate (hash rate not seen poolside either from what I could see).
3/ Power readings all are wrong (Power & Input Voltage).
4/ ASIC Temp low, like it's not hashing.

Logs enclosed (startup) for both firmware builds from the 205 board show no issues that I can see.

Releasefirmware-v2.4.0.txt - (Works fine)

Firmware built 11/21/24 with latest updates that day. ("esp-miner.bin" & "www.bin")
PreRelease-11.21.2022.txt  (v2.4.0-7-g4100402-dirty)  (typo in the filename)

Screenshot of visual issues (and more) of the Dashboard from the Ultra 205 enclosed.

[Releasefirmware-v2.4.0.txt](https://github.com/user-attachments/files/17878146/Releasefirmware-v2.4.0.txt)

[PreRelease-11.21.2022.txt](https://github.com/user-attachments/files/17878147/PreRelease-11.21.2022.txt)

![205-masterbranch-11-21-2022-2](https://github.com/user-attachments/assets/7a98cdcf-0b6b-4031-a0ce-b02b5dfa0a6c)

I only noticed this today after building the firmware ("esp-miner.bin" & "www.bin") today with the latest additions and flashed the files to all the devices I have here to test.

Reverted back to the release build on the Ultra 205.

![image](https://github.com/user-attachments/assets/98126a75-1659-401a-9c52-40332494dea8)



## Comments

### ghost on 2024-11-23

Typo's in report (year), sorry about that. 

### ghost on 2024-11-23

Pulled the repo down fresh and re-built the firmware to rule that out, flashed both files to the Ultra 205, no change.

![205 v2 4 0-12-g29a543d-dirty](https://github.com/user-attachments/assets/81d44a03-4c94-4a2f-aa29-cd284e15c26c)




### eandersson on 2024-11-23

What happens if you change the frequency?

### ghost on 2024-11-23

Nothing changes with how it performs, voltage readings and temps show wrong along with hash rate.

ASIC Frequency updates on the Dashboard as does the Measured ASIC Voltage when changed in the Settings page.

Something that's been merged to the master branch after v2.4.0 was released is causing an issue with the 205 I have here. 




### eandersson on 2024-11-23

Can you try to comment out this line to see if it makes a difference? might be some weird race condition
https://github.com/skot/ESP-Miner/blob/master/components/asic/serial.c#L51

### mutatrum on 2024-11-24

Can you zoom in on the actual commit by doing a `git bisect`?

### skot on 2024-11-27

this happens on my 204

### skot on 2024-11-27

Narrowing it down: problem does not happen in 17873069a2a5237f4e8910e3fd500018d9ea25c9 and happens in 41004029901a0127b626c6070495f9e0af7046d0



### skot on 2024-11-27

Well that is surprising; it's caused by the uart_wait_tx_done() on this line... https://github.com/skot/ESP-Miner/blob/29a543da76ba5fd19e07f43da87214613d67455a/components/asic/serial.c#L51

from PR #503 

this smells like a sneaky timing problem.

### eandersson on 2024-11-27

> Well that is surprising; it's caused by the uart_wait_tx_done() on this line...
> 
> https://github.com/skot/ESP-Miner/blob/29a543da76ba5fd19e07f43da87214613d67455a/components/asic/serial.c#L51
> 
> from PR #503
> 
> this smells like a sneaky timing problem.

Yep - this is what I was asking about in the firmware testing channel. It's a really sneaky problem, but has been difficult for me to troubleshoot as I unfortunately don't have any of the older devices.

### eandersson on 2024-11-27

btw during my testing I found that after changing the baud it left the device unable to communicate with the ASIC due to some sort of race condition on the Supra. This feels like the same issue, but different timing issue.

The original issue I was solving was basically if we were a few CPU cycle faster (e.g. removing a single log line before BAUD is setup) it would break the ASIC startup.

I wish we had some sort of sanity check after all setup is done, for my testing I just used the ASIC count check to verify that we could still communicated. 

```
11/23/2024 07:25:11 PM E (26772) MAIN: BAUD RATE set to 115201
11/23/2024 07:25:16 PM E (26772) MAIN: Number of ASIC: 1 (Setup successful)
```

### WantClue on 2024-12-01

fixed in #532
