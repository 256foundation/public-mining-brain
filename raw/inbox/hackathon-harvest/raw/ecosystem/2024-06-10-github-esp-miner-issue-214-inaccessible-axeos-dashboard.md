# bitaxeorg/ESP-Miner issue #214: Inaccessible AxeOS Dashboard

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/214
> Collected: 2026-10-07
> Published: 2024-06-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 214
- State: closed
- Author: crimsonleaf363
- Opened: 2024-06-10
- Closed: 2024-06-11
- Labels: none

## Description

**Describe the bug**
The AxeOS dashboard is currently inaccessible from the local IP address displayed on the Bitaxe screen. The connection attempt fails.

**To Reproduce**
Steps to reproduce the behavior:
1. Ensure the Bitaxe device is powered on and functioning correctly.
2. Observe the local IP address displayed on the Bitaxe screen.
3. Attempt to access the AxeOS dashboard using the local IP address.

**Expected behavior**
The user should be able to access the AxeOS dashboard from the local IP address displayed on the Bitaxe screen.

**Hardware (please complete the following information):**
 - Bitaxe HW version: Ultra 204
 - ESP-Miner FW version: 2.1.6
 - Hash Frequency: N/A (I don't know how to determine the hash frequency.)
 - Voltage: N/A (I don't know how to determine the voltage.)
 - Pool URL, Port, User: Default

## Comments

### MyOwn2C on 2024-06-10

Does your router settings allow local network traffic between devices?
If you connect Bitaxe to the “Guest” network, you won’t be able to access its IP. 
I can access my Bitaxe local IP without issues. 

### crimsonleaf363 on 2024-06-10

> Does your router settings allow local network traffic between devices? If you connect Bitaxe to the “Guest” network, you won’t be able to access its IP. I can access my Bitaxe local IP without issues.

I'm able to access other local IPs between different devices.

### seangrant82 on 2024-06-11

you could try and turn off your router then power it on. Once it cant find your wifi, it will broadcast its own AP. Connect your comp to that and see if you can see it. If so, update FW to 2.1.8 and ✅✅ pool settings. I messed up my pool settings and it wouldn't let me access it until i fixed it.

### crimsonleaf363 on 2024-06-11

> you could try and turn off your router then power it on. Once it cant find your wifi, it will broadcast its own AP. Connect your comp to that and see if you can see it. If so, update FW to 2.1.8 and ✅✅ pool settings. I messed up my pool settings and it wouldn't let me access it until i fixed it.

This didn't fix my issue. 

### crimsonleaf363 on 2024-06-11

> Does your router settings allow local network traffic between devices? If you connect Bitaxe to the “Guest” network, you won’t be able to access its IP. I can access my Bitaxe local IP without issues.

I updated my firmware to 2.1.8, but that did not fix the issue. After I switched the Bitaxe to a non-guest Wi-Fi, the problem was solved. I'm able to access the AxeOS dashboard without a problem. Thank you.

### skot on 2024-06-11

ok that makes sense. Guest WiFi doesn't usually let clients communicate with each other
