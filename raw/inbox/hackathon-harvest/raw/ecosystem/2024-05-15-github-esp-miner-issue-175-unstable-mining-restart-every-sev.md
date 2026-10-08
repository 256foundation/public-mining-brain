# bitaxeorg/ESP-Miner issue #175: Unstable mining, restart every several hours

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/175
> Collected: 2026-10-07
> Published: 2024-05-15

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 175
- State: closed
- Author: mutatrum
- Opened: 2024-05-15
- Closed: 2024-05-24
- Labels: none

## Description

**Describe the bug**
I'm running a BitAxe 400 (Supra), and experience unstable mining. It restarts frequently, and on several occasions it doesn't start mining again, running idle, either because it didn't restart accepting shares, or because it reverted to the factory wifi.

**Expected behaviour**
Less frequent restarts, and resume mining when it happens.

**Screenshots & Photos**
I have captured system/info every minute for an extended period of time, and created the following chart (shares on left y-axis, uptime in hours on right y-axis):

![chart (9)](https://github.com/skot/ESP-Miner/assets/56344102/24a6456e-ae56-4cc3-ac87-260fc079e5f8)

There are 3 noticeable things:

1) Most times it restarts after several hours. However, sometimes there are periods with very frequent restarts. For example, on the 18th it had 7 restarts in ~90 minutes (just above the 2024 of the first date label on the x-axis).
2) In some cases it restarts, connects to the wifi and no shares are accepted. These are the two large blue slopes. Unfortunately, it never restarts by itself when this happens. I think this is caused by #100 
3) In some occasions, after a restart it comes up with the factory wifi setup. In the graph these are shows with 0 uptime, once is visible at the end of the graph. I have seen this happen twice. Power cycling fixes this, so maybe it's a race condition on reading the configuration?

**Hardware (please complete the following information):**
 - Bitaxe HW version: Supra 400
 - Bitaxe HW vendor: Silexperience
 - ESP-Miner FW version: v2.1.3
 - Hash Frequency: 550
 - Voltage: 1250
 - Pool URL, Port, User: solo.d-central.tech

**Additional context**
Initially I had the UI open, and after reading some information it hinted that this could be a trigger. However, closing down the UI it didn't make a difference. The only use of the webserver is the polling of system/info once a minute.

Any additional logging/debugging pointers would also be helpful.

## Comments

### benjamin-wilson on 2024-05-16

Change the frequency to the default 490 mhz or under and see if the issue persists 

### mutatrum on 2024-05-16

Set it to 490, will report back in a day or so. For the record, it came with 550 set, I thought that was the default. I didn't change any settings other that the pool settings.

### benjamin-wilson on 2024-05-24

Closing (assumed resolved)

### mutatrum on 2024-05-27

Unfortunately it's not resolved yet. After setting the frequency to 490, it is a lot more stable, but still resets after ~ 8 hours.

![image](https://github.com/skot/ESP-Miner/assets/56344102/99b20761-c19b-4fb9-aed8-3d4d4dc4cd74)
Left y-axis is uptime (hr), right y-axis is shares.

In two cases, it didn't start mining, where the shares stay at 0, one is just right of center, second is the large spike at the end. It doesn't automatically reset when this happens, I power cycle it to get it to resume so there is something in the mining process that triggers the reset. I initially though it was related to the connectivity, but that doesn't seem the case as the machine is perfectly reachable all the time.

### mutatrum on 2024-05-31

Upgraded firmware to 2.1.6 and capturing logs, hopefully that will bring something #179.

### benjamin-wilson on 2024-05-31

We're aware of a restart bug affecting 2.1.4+ and have a fix, it should be ready soon. 

### mutatrum on 2024-06-11

Running 2.1.8, and as long as I don't open the websocket connection it is stable, crossed the 24h mark just now.

### solobito on 2024-06-11

> Running 2.1.8, and as long as I don't open the websocket connection it is stable, crossed the 24h mark just now.

Please, if you can, test this. Just to confirm that it restarts with that script. https://github.com/skot/ESP-Miner/issues/199#issuecomment-2149171200
