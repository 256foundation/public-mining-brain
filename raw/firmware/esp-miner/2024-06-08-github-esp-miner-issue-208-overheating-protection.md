# bitaxeorg/ESP-Miner issue #208: Overheating protection

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/208
> Collected: 2026-10-07
> Published: 2024-06-08

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 208
- State: closed
- Author: Shen
- Opened: 2024-06-08
- Closed: 2024-06-08
- Labels: bug

## Description

I found this report. 

[https://primal.net/e/note18txy6y3c9wjshfqjutphyn4aqsg997r4vtszyrr33q84mqhy37uq3xwlm2](https://primal.net/e/note18txy6y3c9wjshfqjutphyn4aqsg997r4vtszyrr33q84mqhy37uq3xwlm2)

I didn't have this issue yet, but is there a proper overheating protection implemented?

## Comments

### solobito on 2024-06-08

It is possible that this might happen. I have noticed that in version 2.1.7, the fan stops working when the device is turned on if it is not connected to any Wi-Fi network. I think the fan should always be running to prevent these issues.

### ghost on 2024-06-08

Agreed fan should always be active as protection.  Should be no time the fan is off. 

### solobito on 2024-06-08

## Procedure to Stop the Fan:

1. **Set Up a Non-existent Wi-Fi Network:**
   - Configure the Bitaxe to connect to a Wi-Fi network that does not exist, or simply disconnect your Wi-Fi router.

2. **Reset and Disconnect Power Supply:**
   - Press the reset button and then disconnect the power supply. (Note: Just pressing the reset button won't work; you must disconnect the power completely.)

3. **Reconnect the Power Supply:**
   - Reconnect the power supply to turn on the Bitaxe. (The device will attempt to connect to the non-existent Wi-Fi network, causing the fan to turn off.)

4. **Maintaining the Off State:**
   - If you press the reset button again, the device will restart, and the fan will remain off.

## Other Method to Turn Off the Fan:

1. **Correct Wi-Fi Configuration:**
   - Configure the Bitaxe to connect correctly to a valid Wi-Fi network. Save these settings.

2. **Reset and Disconnect Power Supply:**
   - Press the reset button and disconnect the power supply. (Again, this won't work with just the reset button; you must disconnect the power completely.)

3. **Reconnect and Wait:**
   - Wait a few seconds, then reconnect the power supply. Allow time for the Bitaxe to connect to the Wi-Fi network.

4. **Temporary Fan Shutdown:**
   - The fan will turn off for a few seconds while the screen displays "0 hashes per second."

5. **Fan Resumes Normal Operation:**
   - After a few seconds, the fan will turn back on, and the Bitaxe will resume normal operation.

## Note:
It's unclear if turning off the fan also disables the overheating protection system. Both aspects should be reviewed to ensure proper operation.


### skot on 2024-06-08

You're right, having the fan off is not good. I'll look into this. In the mean time, do not let your bitaxe run without the fan spinning!

### skot on 2024-06-08

Please test with the new 2.1.8 release; https://github.com/skot/ESP-Miner/releases/tag/v2.1.8

### solobito on 2024-06-08

Fixed! In my Bitaxe, the fan no longer stops like it did before! Great!

### benjamin-wilson on 2024-06-08

Resolved
