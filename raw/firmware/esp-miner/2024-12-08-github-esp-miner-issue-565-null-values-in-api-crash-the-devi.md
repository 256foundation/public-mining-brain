# bitaxeorg/ESP-Miner issue #565: null values in API crash the device

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/565
> Collected: 2026-10-07
> Published: 2024-12-08

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 565
- State: closed
- Author: w3irdrobot
- Opened: 2024-12-08
- Closed: 2025-06-11
- Labels: bug

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**

When updating settings through the API at `PATCH /api/system`, if any values are explicitly `null`, it seems to crash the entire device.

**To Reproduce**
Steps to reproduce the behavior:
1. Have a Bitaxe.
2. Dance because you own a Bitaxe, and that's awesome.
3. Get device IP
4. Run the command `curl -v -X PATCH -d '{"wifiPass":null}' http://<DEVICE_IP>/api/system`
5. Notice that the device restarts itself (fans spin down, Uptime in web app resets)
6. Cry

**Expected behavior**

I would expect it to be ignored or an error be thrown to let me know I screwed up the request body.

**Screenshots & Photos**
If applicable, add AxeOS screenshots and/or photos of your Bitaxe to help explain your problem.

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: Solo Satoshi
 - ESP-Miner FW version: v2.4.0 
 - Hash Frequency: 525
 - Voltage: 1150
 - Pool URL, Port, User: Braiins.....

**Additional context**

I checked all the settings and it appeared these ones being set to `null` are when the issues turn up. The others seem to just treat it as `false`.

```
hostname
ssid
wifiPass
stratumURL
stratumUser
stratumPassword
fallbackStratumURL
fallbackStratumUser
fallbackStratumPassword
```


## Comments

### w3irdrobot on 2025-02-21

anyone actually working on this yet? if not, i can work on it.

### mutatrum on 2025-06-11

Fixed by #748
