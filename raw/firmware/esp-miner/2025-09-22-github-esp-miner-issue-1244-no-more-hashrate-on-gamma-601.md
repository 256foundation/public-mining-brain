# bitaxeorg/ESP-Miner issue #1244: No more hashrate on gamma 601

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1244
> Collected: 2026-10-07
> Published: 2025-09-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1244
- State: closed
- Author: moljordi
- Opened: 2025-09-22
- Closed: 2025-11-18
- Labels: none

## Description

Hi guys, 

i have been running 2 gamma's and 1 supra for quite some time without any problems. Today i switched from bitcoin core to knots. After i switched i saw that my 2 gamma's which are running in my own public pool didn't hash anymore. I tried to alter the pool adjustments, different pools, different btc adresses, everything. Nothing worked. They just died after the switch. They are both were running 2.09. After they died i updated them with 2.10, trying to resolve it that way. No luck.
Any ideas?

<img width="802" height="674" alt="Image" src="https://github.com/user-attachments/assets/0496f4c2-37ae-4885-ac24-bdb3267c548c" />

## Comments

### moljordi on 2025-09-22

<img width="1047" height="856" alt="Image" src="https://github.com/user-attachments/assets/68cdd7fc-24ec-445e-bfd0-c53dfbb2bee7" />

### mutatrum on 2025-09-22

If you restart them with a cold boot (e.g. unplug the power cord), do they start hashing for a while, or not at all? Would be interesting to see the boot logs, try to capture them as early as possible.

### moljordi on 2025-09-22

I've unplugged the power cord for about 10 minutes, still not working. I was rebooting my Umbrell Node then it started hashing again.... .But... on a fixed Th/s. One keeps running at 1,5 TH/s the other at 1,38 th/s. It's so weird....

<img width="1168" height="1122" alt="Image" src="https://github.com/user-attachments/assets/dcc00683-5a6d-484e-b5e7-04877076da3e" />

This is at startup:

<img width="891" height="1081" alt="Image" src="https://github.com/user-attachments/assets/1ea46927-5414-40e8-adbb-590e7bab6527" />

### mutatrum on 2025-09-22

Looks like #1053. Can you set the frequency and voltage back to default and try again? It's possible you're pushing them too hard. Not sure if that's different with 2.9.0.

### LightBridge16 on 2025-10-07

I had this problem also. I had too reflash the factory firmware and disconnected the power for a minute. 

### WantClue on 2025-11-18

Closing because of high probability of too high overclocking. Users seems not to report any further updates on this issue
