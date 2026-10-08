# bitaxeorg/ESP-Miner issue #274: Free Heap Memory continues to decrease in 2.1.9

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/274
> Collected: 2026-10-07
> Published: 2024-08-08

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 274
- State: closed
- Author: seiuryuu
- Opened: 2024-08-08
- Closed: 2024-08-11
- Labels: none

## Description

After upgrading to the 2.1.9 release and running for about 2 days, I found that the Free Heap Memory continues to decrease until reboot. I did a factory flash to see if it can be resolved but the phenomenon still exists.

In axe-os Logs page, I can see the Free Heap Memory drops about 150 every time the web auto refreshes.

Have tested on Ultra 204/205, Supra 402, this problem can be reproduced stably.

## Comments

### seiuryuu on 2024-08-09

After downgrading the firmware to commit **30b9f29** on **Jul 13, 2024** to compile, I found that the free heap seems to stop decreasing when axe-os is closed.

### seiuryuu on 2024-08-09

#278 

### skot on 2024-08-10

I added this in with a couple other suspected memory leak fixes in https://github.com/skot/ESP-Miner/tree/219-leak_hunting

[esp-miner.bin.zip](https://github.com/user-attachments/files/16568474/esp-miner.bin.zip)


### seiuryuu on 2024-08-10

Nice! I'm about to give it a try. I will close this issue and the associated PR once it tests well.

### seiuryuu on 2024-08-11

So far so good
