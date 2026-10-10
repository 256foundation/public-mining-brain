# bitaxeorg/ESP-Miner issue #85: BitAxe Ultra - Random Restarts

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/85
> Collected: 2026-10-07
> Published: 2024-01-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 85
- State: closed
- Author: StarGateMiner
- Opened: 2024-01-11
- Closed: 2024-01-13
- Labels: none

## Description

Hi all, 

I recently got a BitAxe Ultra Miner (Version 201) - although I feel little cheated as seller did not mention it be a 201 version, does worry me that 201 versions may not be 100percent stable.

I have noticed that I cannot get a stable uptime at all - with random restarts throughout the day.

1) Device is next to a wireless router - so wifi connection should not be a issue
2) Have not attempted to overclock at all - only change the fan to a Noctua NF-A4x10
3) I have tried to change from default public-pool to ckpool pool to see if it make a difference as the public-pool not been to stable these few months. 

Details below, any ideas what the issue can be??, is there a way we can include "restarts" in the debug log.
Perhaps we can color code the log output so its much easier to see and understand what is going on.



```
Model: | BM1366
Uptime: | 16 minutes
WiFi Status: | Connected!
Free Heap Memory: | 178212
Version: | v2.0.5-2-g174ef21-dirty

Power Consumption: | 11.55 W
Input Voltage: | 5,016 mV
Input Current: | 2,301 mA
Frequency: | 485 Mhz
Core Voltage: | 1200 mV
Measured Core Voltage: | 1196 mV
Fan Speed: | 2558 RPM
Chip Temperature: | 54 C

Hash Rate: | 431.38 Gh/s
Efficiency: | 26.03 W/Th
```



## Comments

### benjamin-wilson on 2024-01-11

What seller did you get it from? Unless you can capture a restart in the logs it's going to be different to determine what's going on. 201 version has proven to be very reliable.

### benjamin-wilson on 2024-01-13

Resolved on Discord?

### StarGateMiner on 2024-01-16

@benjamin-wilson I was not able to capture yet but I noticed today my wifi was retrying out the blue - no changes to my setup, this is the log output but tells me little

> ₿ (88269240) asic_result: Nonce difficulty 18434.62 of 1024.
₿ (88269260) stratum_api: tx: {"id": 9377, "method": "mining.submit", "params": ["bc1q29ckfn03jvlgndpl9sq0fpvz5v2jh2ymcwmef3", "dce8db", "04000000", "65a69770", "b2e6005c", "024c4000"]}
₿ (88270150) stratum_task: rx: {"id":9377,"error":null,"result":true}
₿ (88270150) stratum_task: message result accepted
₿ (88270410) asic_result: Nonce difficulty 7963.58 of 1024.
₿ (88270420) stratum_api: tx: {"id": 9378, "method": "mining.submit", "params": ["bc1q29ckfn03jvlgndpl9sq0fpvz5v2jh2ymcwmef3", "dce8db", "04000000", "65a69770", "eb20015a", "0cb1e000"]}
₿ (88270560) asic_result: Nonce difficulty 2361.17 of 1024.
₿ (88270570) stratum_api: tx: {"id": 9379, "method": "mining.submit", "params": ["bc1q29ckfn03jvlgndpl9sq0fpvz5v2jh2ymcwmef3", "dce8db", "04000000", "65a69770", "cb580078", "0e02c000"]}
₿ (88270810) stratum_task: rx: {"id":9378,"error":null,"result":true}
₿ (88270810) stratum_task: message result accepted
₿ (88271300) stratum_task: rx: {"id":9379,"error":null,"result":true}
₿ (88271310) stratum_task: message result accepted
₿ (88272060) asic_result: Nonce difficulty 431.74 of 1024.
₿ 80)
₿ a, newchan=2, o
₿
₿ 90)
₿ a, newchan=2, o
₿
₿ 90)
₿ a, newchan=2, o
₿
₿ 10)
₿ a, newchan=2, o
₿ 

Had to manually reboot and after manually rebooting all is fine again
