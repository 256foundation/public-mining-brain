# bitaxeorg/ESP-Miner issue #142: BitAxe 201 updated from v2.0.7 to v2.1.3 now bricked?

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/142
> Collected: 2026-10-07
> Published: 2024-03-19

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 142
- State: closed
- Author: plittlefield
- Opened: 2024-03-19
- Closed: 2024-04-05
- Labels: none

## Description

I used the web gui on v2.0.7 to restart and then update the main firmware and then web firmware on my 201 - but after waiting 15 minutes I had to power cycle the device.

However, when the power was restored it now shows NO output on the screen and I cannot ping the device.

I had previously updated from v2.0.3 to v2.0.7 with no issues.

What can I do to rescue it?

Thanks,

Paully

## Comments

### MyOwn2C on 2024-03-19

Use Bitaxe web flasher

https://wantclue.github.io/bitaxe-web-flasher/

### plittlefield on 2024-03-19

I did that, it seemed to complete, but I've plugged the power in again and it's not responsive :(

I'm probably doing it wrong!

Is there a YouTube anywhere for this or step by step instructions please?

### plittlefield on 2024-03-19

I watched this video - https://www.youtube.com/watch?v=e37tbrXdAtY - and followed the instructions for my BitAxe 201 as 'All models' and it still remains dead :(

![2024-03-19_13-57](https://github.com/skot/ESP-Miner/assets/8265704/a45eb186-b385-45f0-b4e4-eaf938ac1931)

![2024-03-19_13-57_1](https://github.com/skot/ESP-Miner/assets/8265704/4c5552cd-b9ba-4205-b6a1-d08fb23d1c79)

![2024-03-19_13-58](https://github.com/skot/ESP-Miner/assets/8265704/8a7276ed-8875-4a42-a4cf-f5dbcf32a30e)

![2024-03-19_13-58_1](https://github.com/skot/ESP-Miner/assets/8265704/138513f7-fa82-49f5-bf78-b66d9ffa60e9)

[esp-web-tools-logs.txt](https://github.com/skot/ESP-Miner/files/14651557/esp-web-tools-logs.txt)

I fear the worst :-(

### plittlefield on 2024-03-19

FYI, I was able to copy and paste some logs the other day when it crashed ...

```
₿ (49901807) bm1366Module: Serial RX invalid 11
₿ (49901817) bm1366Module: 90 aa 55 3a 02 d5 e3 01 10 79 c8
₿ (49904227) bm1366Module: Serial RX invalid 11
₿ (49904227) bm1366Module: 9f aa 55 76 02 c6 2e 00 1e 8d f6
₿ (49904297) bm1366Module: Serial RX invalid 11
₿ (49904297) bm1366Module: 8c aa 55 34 02 ee b1 01 1b 93 5b
```

... don't know if that's relevant to this but it did keep crashing on v2.0.7 when mining to Braiins Pool.

Paully


### MyOwn2C on 2024-03-19

Try using ESPTool online to erase the flash completely.
https://espressif.github.io/esptool-js/
Make sure you get to Bootloader mode first.
After erasing flash using ESPTool, flash again using Bitaxe web flasher

### plittlefield on 2024-03-19

Thanks.  I've had a quick look at that page.  Is there some documentation for that?

### MyOwn2C on 2024-03-19

> Thanks. I've had a quick look at that page. Is there some documentation for that?

https://youtu.be/3oEvXhgHZHo

### plittlefield on 2024-03-19

Thanks.  The erase on the ESPTool was successful.  I then powered off, went back to the bitaxe-web-flasher tool and did exactly the same procedure as before, but alas - the device has no display and it does not boot  :(

### MyOwn2C on 2024-03-19

You can try using the ESPTool that worked and manually flash the factory bin at 0x0 address

if you can, use v2.1.1. It is the last stable version before self test was added. 

### plittlefield on 2024-03-19

YES that worked!

Many thanks :-)

### mroxso on 2024-03-26

Had the same issue with my 202 board today. Had to flash it manually with the bitaxetool to fix it. I don't know what's wrong with the new version yet.

### MyOwn2C on 2024-03-26

> Had the same issue with my 202 board today. Had to flash it manually with the bitaxetool to fix it. I don't know what's wrong with the new version yet.

Just use v2.1.1 for now

### skot on 2024-04-05

I'm glad you were able to resurrect your bitaxe, and thanks @19201003080114 for the excellent tip.
