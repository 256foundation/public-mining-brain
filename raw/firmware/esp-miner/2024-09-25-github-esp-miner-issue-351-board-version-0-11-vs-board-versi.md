# bitaxeorg/ESP-Miner issue #351: Board Version: 0.11 vs. Board Version: 204

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/351
> Collected: 2026-10-07
> Published: 2024-09-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 351
- State: closed
- Author: unclasp
- Opened: 2024-09-25
- Closed: 2024-10-10
- Labels: none

## Description


![ww](https://github.com/user-attachments/assets/72ae8bd9-2be5-42ea-a9b1-37383d71312a)


With board version 204, only software 2.1.8 works for me. Is that the case with you too? No matter what frequency or current.




## Comments

### MyOwn2C on 2024-09-25

I have 204 and v2.1.10 works for me. 
I had v2.1.8 before and v2.1.10 works better. 

### skot on 2024-09-25

I've got v2.2.2 on a 102, 201, 202, 204, 401, 402 and 600. So far so good. But I'll keep an eye on it.

### sstativa on 2024-09-27

I don't know if there were any changes on the Pool side or if it was due to the firmware reflash, but 2.1.10 works fine for me now.

First, I tried to install 2.1.10 via the WebUI a month ago, attempting multiple times without success. In the end, I rolled back to 2.1.8.

However, I recently installed 2.2.2, which broke the board (204). I had to reflash the board using a serial console with esp-miner-factory-204-v2.1.10.bin. Not only did I manage to fix the board, but 2.1.10 is also now working for me.

### skot on 2024-09-27

This sounds like the AxeOS based firmware update isn't going so well. Can you tell me more about how you're doing it?

v2.2.2 is working well on my 204

### unclasp on 2024-10-02

I bought the boards on AliExpress. The versions mentioned. They call themselves LuckyMiner 6. I only ever flashed via the web interface. The boards have no connection.

![grafik](https://github.com/user-attachments/assets/aa4b3969-b3c8-4f4f-8d13-8cc706253106)


### stealth2600 on 2024-10-02

@unclasp Unfortunately LuckyMiners are knockoff devices and are NOT authentic Bitaxes. You are likely going to need to contact the manufacturer of LuckyMiners or the reseller your purchased them from for support. LuckyMiner essentially stole the work of the Bitaxe project and turned into their own closed source product that's not associated with the Bitaxe project in any way.
