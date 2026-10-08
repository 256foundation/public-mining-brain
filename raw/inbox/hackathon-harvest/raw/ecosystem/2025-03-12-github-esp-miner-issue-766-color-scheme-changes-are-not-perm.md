# bitaxeorg/ESP-Miner issue #766: Color scheme changes are not permanent

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/766
> Collected: 2026-10-07
> Published: 2025-03-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 766
- State: closed
- Author: etkaar
- Opened: 2025-03-12
- Closed: 2025-03-13
- Labels: none

## Description

Color scheme changes do not survive reboots:

![Image](https://github.com/user-attachments/assets/929adef1-7668-4ec2-867c-513f2ccb22d1)

## Comments

### WantClue on 2025-03-13

they do maybe you need to clear your browser cash

### etkaar on 2025-03-13

Please reopen, as this bug hasn't been fixed yet. It doesn't have anything to do with _not_ clearing the browser cache.

### MyOwn2C on 2025-03-13

> Please reopen, as this bug hasn't been fixed yet. It doesn't have anything to do with _not_ clearing the browser cache.

I can confirm that color change CAN survive reboots. 

So issue is 100% on your side. 

### etkaar on 2025-03-13

It seems not the reboot is the reason. I tested it both in Google Chrome and Mozilla Firefox:

- Change color scheme from _Dark_ to _Light_.
- Press `[F5]` one or multiple times. The setting will change back to _Dark_, though the _Light_ color scheme will be applied.
- Press `[CTRL]+[F5]`. The color scheme will be reset to _Dark_.

Where are these settings stored? Server-side? I can't find any cookies.

### MyOwn2C on 2025-03-14

> It seems not the reboot is the reason. I tested it both in Google Chrome and Mozilla Firefox:
> 
> * Change color scheme from _Dark_ to _Light_.
> * Press `[F5]` one or multiple times. The setting will change back to _Dark_, though the _Light_ color scheme will be applied.
> * Press `[CTRL]+[F5]`. The color scheme will be reset to _Dark_.
> 
> Where are these settings stored? Server-side? I can't find any cookies.

Issue still on your side.

I duplicate your steps using Chrome. My scheme stayed no matter F5 refresh or Ctrl-F5 refresh.




### etkaar on 2025-03-14

Where are these settings stored?

### etkaar on 2025-03-25

See https://github.com/bitaxeorg/ESP-Miner/issues/781
