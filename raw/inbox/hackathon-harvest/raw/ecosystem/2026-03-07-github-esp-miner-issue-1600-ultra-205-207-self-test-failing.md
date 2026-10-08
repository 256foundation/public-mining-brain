# bitaxeorg/ESP-Miner issue #1600: Ultra 205 / 207 - Self Test failing since v2.12.2 of the firmware

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1600
> Collected: 2026-10-07
> Published: 2026-03-07

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1600
- State: closed
- Author: ghost
- Opened: 2026-03-07
- Closed: 2026-03-26
- Labels: none

## Description

The devices I have here (Ultra 205 / 207)

Firmware v2.12.2 onwards
Ultra 205 - The self test - Sometimes it fails on this device.

Ultra 207 - The self test - Fails most of the time.

Firmware v2.12.0 
Both devices pass every time with this firmware version.

Firmware V2.13.2 (Pre-release)
The self test on these devices also fails with the introduction of #1596 (v2.13.2 Pre-release).

Self test with this version of the firmware will either pass or fail (rare) with the Ultra 205, it's hit or miss with the fail.

Self test with this version of the firmware always fails on the Ultra 207 (logs enclosed), the result here is the same with the Ultra 205 when it fails.

[207-self-test-fail.txt](https://github.com/user-attachments/files/25816561/207-self-test-fail.txt)

Self test - v2.12.2 - Ultra 205, sometimes it passes and sometimes it don't.  Ultra 207 - fails every time.

<img width="784" height="296" alt="Image" src="https://github.com/user-attachments/assets/fa8cbdbf-f6ad-4349-889d-db7d2f8eab0b" />

## Comments

### mutatrum on 2026-03-07

Maybe the `hashrate_test_percentage_target` should be 80% for the Ultra as well, instead of 85%.

Although in the logfile its 88%, so it should succeed? Is there a specific register failure condition that's not logged?

### ghost on 2026-03-07

I can't get the Ultra 205 to fail all the time, it's a rare event, this is the logs from it where the test passes with v2.13.2.

[205-self-test-pass.txt](https://github.com/user-attachments/files/25818237/205-self-test-pass.txt)



### ghost on 2026-03-07

Extra info - new 205 log, it stalled like the 207 does, but this time it passed the self test, normally it fails the test when it stalls.

[205-self-test-run2.txt](https://github.com/user-attachments/files/25818711/205-self-test-run2.txt)

<img width="779" height="732" alt="Image" src="https://github.com/user-attachments/assets/ef8cf9ce-8446-438b-b2ed-5a17db71d30f" />

### ghost on 2026-03-08

Extra info - 205 logs - Managed to capture the fail, sometimes the end of the test shows like the 207 does where the domains do not show (see image below for the 207), the last two captures within these logs show the 205 passing the test while other times it fails.

[205-self-test-fail.txt](https://github.com/user-attachments/files/25821182/205-self-test-fail.txt)


207
<img width="1107" height="178" alt="Image" src="https://github.com/user-attachments/assets/d31e656e-4a8a-4e75-86c6-f0354a29d3f6" />



### ghost on 2026-03-08

Nope - this is a fail - Supra 401 that I tested this on a few days ago passed, today with the same Supra 401 it fails.

In-house build of the firmware

[401-self-test-pass.txt](https://github.com/user-attachments/files/25825242/401-self-test-pass.txt)

[401-self-test-fail.txt](https://github.com/user-attachments/files/25825243/401-self-test-fail.txt)


Firmware downloaded from the repo (v2.13.2 Pre-release).

[401-self-test-fail.txt](https://github.com/user-attachments/files/25825257/401-self-test-fail.txt)



### ghost on 2026-03-20

Resolved with #1615 

### mutatrum on 2026-03-20

I think actually #1610 fixed it (bumping the acceptable temperature to 62C), that was merged into #1615.

### ghost on 2026-03-20

#1610 on it's own was a no go on all 5 devices here (2x Ultra (205 / 207), 3x Supra (401)).
