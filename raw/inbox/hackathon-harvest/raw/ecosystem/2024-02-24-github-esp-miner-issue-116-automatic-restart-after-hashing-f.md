# bitaxeorg/ESP-Miner issue #116: Automatic restart after hashing failure or regular restart option

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/116
> Collected: 2026-10-07
> Published: 2024-02-24

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 116
- State: closed
- Author: plittlefield
- Opened: 2024-02-24
- Closed: 2024-03-15
- Labels: question

## Description

I have a 201 with BM1366 on v2.0.7 mining to Braiins Pool with good hash rate, but it will stop mining and almost crash about every 24 hours.

The miner is in a cool environment with a UPS battery attached to the good quality power supply and decent Unifi wifi.

I can log in to the web interface (this takes along time to load!) and when I press the Restart button it comes back and starts mining normally again.

Is there a way to add an automated 'restart on miner failure' or is there an API I can call using the web gui or SSH to restart it every night?

Thanks.

Regards,

Paully

**Detailed Information:-**

```
Model:	BM1366
Uptime:	6 hours
WiFi Status:	Connected!
Free Heap Memory:	175624
Version:	v2.0.7
Board Version:	0.11
Power Consumption:	11.60 W
Input Voltage:	5,224 mV
Input Current:	2,224 mA
Frequency:	485 Mhz
Core Voltage:	1200 mV
Measured Core Voltage:	1219 mV
Fan Speed:	5953 RPM
Chip Temperature:	56 C
Hash Rate:	474.86 Gh/s
Efficiency:	24.55 W/Th
Best Difficulty:	25.9M
```



## Comments

### benjamin-wilson on 2024-02-24

What do you have for a wireless router?

### plittlefield on 2024-02-24

Ubiquiti Unifi UAP-AC-Lite running latest firmware on 2.4GHz wifi about 7 feet away. This connects to my gigabit wired network with a Trooli Internet 300Mbps FTTP connection in to the house.  Rock, solid.

### skot on 2024-02-24

This sounds like something the pool is doing that we're not handling well. If you get a chance could you try and get the esp-miner log from when this happens?

### plittlefield on 2024-02-24

Sure, I’ll try.

### benjamin-wilson on 2024-03-15

Closing for inactivity
