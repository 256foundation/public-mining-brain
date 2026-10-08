# bitaxeorg/ESP-Miner issue #178: Won't boot, screen blank after update to 2.14

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/178
> Collected: 2026-10-07
> Published: 2024-05-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 178
- State: closed
- Author: jddebug
- Opened: 2024-05-22
- Closed: 2024-05-23
- Labels: none

## Description

Won't boot, screen blank after update to 2.14

Updated 4 others with no problem. Any pointers on how to recover?

## Comments

### skot on 2024-05-22

are these updates through AxeOS? What bitaxe hw?

you might try using the bitaxe web flasher to go back and try again; https://wantclue.github.io/bitaxe-web-flasher/


### jddebug on 2024-05-22

Yes using AxeOS. Board version 0.11

I will take a look at that link.

### jddebug on 2024-05-22

ok, I installed the bitaxe-flasher. It appears I still have to do something after that to get the firmware installed? Flasher install was successful but not booting up as a miner. Is there a next step?

### jddebug on 2024-05-22

Nevermind. Did it twice and now all good. Thanks


### jddebug on 2024-05-23

Ok, it boots and looks like the web interface I am used to but it thinks the ASIC is at 127.75C and will not mine. I have the board version 0.11 and was not sure which bite model to choose from the list so I went with Bite Max since it didn't have a board version listed. I don't think it is setting things up correctly. This miner has been flawless until trying to update to 2.14.

Any guidance?

### jddebug on 2024-05-23

Ok, version 0.11 = version 204 It is mining again.

### skot on 2024-05-23

yeah, 0.11 is an Ultra before we switched to the current version scheme. The closest would be a 204. Glad you got it working again!

We're working on making these tools better.
