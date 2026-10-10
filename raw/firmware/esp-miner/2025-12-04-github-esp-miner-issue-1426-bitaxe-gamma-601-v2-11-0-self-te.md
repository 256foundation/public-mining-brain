# bitaxeorg/ESP-Miner issue #1426: BitAxe Gamma 601 - v2.11.0 Self-Test fails due to a little lower than expected minimum power consumption

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1426
> Collected: 2026-10-07
> Published: 2025-12-04

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1426
- State: closed
- Author: v1ckxy
- Opened: 2025-12-04
- Closed: 2025-12-04
- Labels: none

## Description

**Describe the bug**
Self-Test fails as the power consumption is below 16W (around ~15.something watts) in the following two cases:
- With version 2.11.0 flashed, after a cold boot.
- Or after flashing version 2.11.0

**To Reproduce**
You have two ways to trigger the issue:
1. From a cold start ( == after disconnecting and reconnecting power supply)
Start the device pressing reset, then boot to enter self-test mode.
Self test will fail with a power draw a little under <16W (15.something watts):

<img width="939" height="201" alt="Image" src="https://github.com/user-attachments/assets/8e9c4e0a-7f50-462a-a71e-27dcb757939a" />

1. Flashing the device via web-flasher with version 2.11.0
After restart, the behaviour will be the same as a before: 
Will crash with a power consumption of 15.something watts.

**However, if you fully power up the device and then restart it, the power consumption will be in the 16.*W range**, so self-test will pass:

<img width="937" height="293" alt="Image" src="https://github.com/user-attachments/assets/50970bce-f15b-44a7-b708-573268badb57" />


**Expected behavior**
Not failing?
I'm not sure about power consumption, vendor says 18W, not 19W as written on device_config.h:
https://github.com/bitaxeorg/ESP-Miner/blob/master/main/device_config.h#L135

Upon boot works without any issue at around 1.0~1.2TH/s with default configuration and a power consumption of around 18W at default ASIC Frequency (525Mhz@1.14V)

**Screenshots & Photos**
<check screenshots below>

**Hardware (please complete the following information):**
 - Bitaxe Gamma 601
 - Bitaxe HW vendor: yysluping mining
 - ESP-Miner FW version: 2.11.0 (latest)
 - Hash Frequency: N/A (1.0~1.2TH/s @ 525Mhz)
 - Voltage: Default (1.14V)
 - Pool URL, Port, User: N/A

**Additional context**
v2.10.0 has a different self-test, so it doesn't fail.

Test after flashing/cold boot:
<img width="940" height="298" alt="Image" src="https://github.com/user-attachments/assets/8d5aac63-7614-4bc7-9564-566c875873f1" />

Test after restart:
<img width="938" height="276" alt="Image" src="https://github.com/user-attachments/assets/11f6db1b-133e-4d17-acbc-149de83c6271" />
Notice that power consumption is a little higher than after a cold boot/reflash.

// To connect to the device in Windows, I'm using simply serial https://github.com/fasteddy516/SimplySerial
```ss.exe -com:7```

// Either my device its a little too efficient or the test needs to push the ASIC even more.

## Comments

### v1ckxy on 2025-12-04

So I tested in another device of the same vendor (white pcb instead of black) and even on cold boot, power consumption during self-test is ~16W, so it doesn't trigger the alarm.

After just restarting both of them and set an ASIC Frequency of 550Mhz @ 1150milivolts, efficiency tends to be a little higher in the one that is failing the self test on cold boot (17.52 J/Th vs 17.32 J/Th)

### mutatrum on 2025-12-04

Fixed by #1415, can you try v2.12 (which will be released very soon)?

### v1ckxy on 2025-12-04

Same device, same psu, but with 6 hours of nonstop mining...  
<img width="833" height="258" alt="Image" src="https://github.com/user-attachments/assets/0c667686-0ebd-4caa-8904-8f303bcdf9d6" />

🤣 I had to leave it disconnected for a while to cool down and replicate the issue:
<img width="860" height="235" alt="Image" src="https://github.com/user-attachments/assets/f6b60671-2ff2-459f-bfcf-83d711080d90" />

And... fixed! Thank you!

### mutatrum on 2025-12-04

Thank you for reporting back!
