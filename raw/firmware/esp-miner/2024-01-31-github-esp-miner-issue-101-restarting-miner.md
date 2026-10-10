# bitaxeorg/ESP-Miner issue #101: Restarting miner

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/101
> Collected: 2026-10-07
> Published: 2024-01-31

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 101
- State: closed
- Author: dani6877
- Opened: 2024-01-31
- Closed: 2024-03-15
- Labels: none

## Description

Hi to all

i have a bitaxe 1397 miner, software 2.0.4, Wifi conection is ok all the time, when i launch the miner everything is ok, but after about one hours or a little more, i have to restart the miner in order that he mine again. And same, after a while, temperature and power consumption fall again ! By pressing restart each time he work again for a while, strange !  Any idea ? 

Thanks

## Comments

### skot on 2024-01-31

can you post the following to help us narrow down this issue?
- which Bitaxe HW version do you have? Where did you get it?
- screenshot of the AxeOS dashboard showing which pool you are using and the miner stats. Both before and after the error.
- ideally a log showing when the error occurs.

thanks!

### dani6877 on 2024-02-01

Hi, thanks, soft version = 2.0.4
Here are 2 pictures, the first one when everythings seems to be ok, power consumption about 14 Watt. This state last about one  hours. Second picture when the miner seems to be paused, power consumption 2.75 W ! He doestn't get out of this state, i need to restart again, and again...

![while working](https://github.com/skot/ESP-Miner/assets/158298942/1732a555-ad43-4ce7-b662-7081c00c2a10)
![Working or not](https://github.com/skot/ESP-Miner/assets/158298942/7ce74ec8-44d2-434a-b246-d07609022dbd)
 


### monster4866 on 2024-02-01

same as here:
https://github.com/skot/bitaxe/issues/118

https://github.com/skot/bitaxe/issues/118#issuecomment-1904615683

ur power supply is crap, u need +5000mv, thats why the miner is crashing/underhashing

https://www.amazon.de/dp/B01HRR9GY4?psc=1&ref=ppx_yo2ov_dt_b_product_details

i think ur fan is also crap and cheap 

and ur core voltage of 1450 is too high, default is 485/1200

### dani6877 on 2024-02-02

OK thanks, i will fix that, or eventually buy an other one :-)

### thalpius on 2024-02-07

@dani6877 Update the version of the OS and firmware as well. I'm not sure if it will fix it, but in version 2.0.5 they lowered the voltage danger warning threshold which you have as well and it can't hurt to update anyway. Just download the 2 files (www .bin and esp-miner.bin) and update using the UI. Here's the latest release:

https://github.com/skot/ESP-Miner/releases

### skot on 2024-02-16

Was this a power supply issue?

### dani6877 on 2024-02-17

Definitively no, it was an overheating, i put the miner in a much more colder room and now it work without problem. Temperatur before was at 60 degres (Celsius) and now at the colder place it exceed not 50 degres. So we can say that as soon the temperature approach 60 degres, the miner stop with working. Maybe a good thing would be to replace the fan with a better one.

### skot on 2024-02-17

In my experience cheapo fans are fine -- just loud. If it's overheating I think you have another problem somewhere.

- do you have good thermal paste?
- are you overclocking?
- do you have a 5V fan?
