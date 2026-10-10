# bitaxeorg/ESP-Miner issue #128: V2.1.1 GUI improvements

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/128
> Collected: 2026-10-07
> Published: 2024-03-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 128
- State: closed
- Author: MyOwn2C
- Opened: 2024-03-10
- Closed: 2024-04-05
- Labels: none

## Description

1. Rename "ASIC **_Voltage_** Requested" to "ASIC **_Current_** Requested"

2. Add new meter for Fan RPM, or add RPM reading under Fan %.

3. Fan % is always at 88% while I can hear the fan speed is being adjusted by software. Perhaps a bug?

<img width="924" alt="image" src="https://github.com/skot/ESP-Miner/assets/158797249/09bc076c-dd85-40be-a410-d25f97a52c55">


## Comments

### TheRockaXXX on 2024-03-10

I can confirm, that the percentage of the fan speed stucks.

### MyOwn2C on 2024-03-12

Renamed subject to V2.1.1 as the same GUI improvements / bugs still apply 

### skot on 2024-03-12

1. It should still be **voltage** requested. I think the units just need to change

### benjamin-wilson on 2024-03-15

Fixed the typo 4cb30a19a46fbefbdf52925e23244654979138c9

### MyOwn2C on 2024-03-15

I sketched some suggestions for GUI improvements.
I could not find icons that match the theme of the original, for Power, Heat and Performance.

<img width="1231" alt="image" src="https://github.com/skot/ESP-Miner/assets/158797249/bacbd535-ba49-4500-9dfa-965db4007e8f">



### thebullishbitcoiner on 2024-03-15

Is it possible to get some/all of the old power meters into the new GUI? I think the only one missing might be input current. That measurement really helped me figure out why my Bitaxe kept showing as offline in my Braiins dashboard.

I kept having to restart the Bitaxe for it to appear again (and then go offline moments later). I figured out that I didn't plug the power cable in all the way. It's been running stable (i.e. ~2200 mA) ever since.

![Screenshot 2024-03-06 235752](https://github.com/skot/ESP-Miner/assets/139607837/66d5a9c8-6ee2-4754-9ea9-50f93e9fd1ef)
