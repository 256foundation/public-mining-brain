# bitaxeorg/ESP-Miner issue #589: Fan speed - Percentages do not match the speed.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/589
> Collected: 2026-10-07
> Published: 2024-12-18

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 589
- State: open
- Author: BTCDACH21
- Opened: 2024-12-18
- Closed: n/a
- Labels: none

## Description

**Describe the bug**
The percentage of the fan speed does not correspond to the maximum speed of the fan.
From ~73% the maximum speed of ~5000 rpm is reached.
There are problems when selecting the automatic function, as the system no longer has any reserves and would overheat from ~73% as no further cooling can come from the fan.

**To Reproduce**
Steps to reproduce the behavior:
1. Change the fan speed from Automatic to Manual 75%.
2. Check the speed before and after.
3. Change the fan speed from 75% to 100%.
4. Check the speed before and after.
5. See error.

**Expected behavior**
The percentage is intended to serve as an indication of how much reserve you have for overclocking. In the automatic function, the Bitaxe would overheat at around 73%, as there would no longer be any cooling effect.

If different coolers have different speeds, you should perhaps be able to set this manually under settings or choose from a selection of most fan models.

**Screenshots & Photos**
Manual and 75% and 5099 U/min
![1](https://github.com/user-attachments/assets/85f28231-b73e-440d-8a6e-10b3b76995de)

Auto and 58% with 4400 U/min
![2](https://github.com/user-attachments/assets/8a75a066-81b9-4728-b93b-19d1d376f5c3)

Manual and 100% and 5079 U/min
![3](https://github.com/user-attachments/assets/399f1a54-76df-413b-a776-d739e3acec92)

**Hardware**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: d-central.tech
 - ESP-Miner FW version: 2.4.2
 - Hash Frequency: 880
 - Voltage: 1250
 - Pool URL, Port, User: public-pool.io

**Additional context**
Argon THRML 60mm Radiator Cooler (max. ~5000 U/min)




## Comments

### MyOwn2C on 2024-12-18

Fan speed % and actual RPM are estimates, and no direct relationships. 
Different fans have different RPM mapping to same PWM %
If you have 50% fan at 1000 RPM, that doesn’t always mean 100% gets you 2000 RPM. 

### skot on 2024-12-18

The RPM measurement _should_ be pretty accurate. It would be interesting to get the fan PWM pin on a scope and see what the EMC2101 fan controller is outputing for a given percentage setting. (and/or check the datasheet and make sure we're using it correctly)

### BTCDACH21 on 2024-12-20

If the signal on the PWM pin of different fans is always different, then the following solution would be preferable.

"Default" setting as the current situation and add a field to enter the maximum RPM of your fan according to the data sheet so that the percentage matches RPM +/-. That would be an approach, right?

PS: Unfortunately, I can only contribute ideas, not coding parameters.

### MyOwn2C on 2024-12-22

> "Default" setting as the current situation and add a field to enter the maximum RPM of your fan according to the data sheet so that the percentage matches RPM +/-. That would be an approach, right?

That will not work.
1. Fan RPM vs PWM is not always linear
2. Fan won't start spinning until it reaches a certain minimum PWM%. Each fan is different. Here is an example. 
 
<img width="502" alt="image" src="https://github.com/user-attachments/assets/117defde-592c-49e1-96f0-17120da7be9c" />

If you look at most PC motherboard manufacturers, none of them require users to specify fan type or parameters into their BIOS. They program a minimum PWM% (to make sure fans will spin at a lowest set PWM%), and it ramps up to 100% depending on the temperature reading. Fan RPM is only to display for user to see or monitor, it is not used as part of the fan control logic. 

You can read this 2005 Intel paper about their requirements for PWM fans.

- If PWM < 30%, min fan speed
- If PWM = 30%, min fan speed
- If PWM = 100%, max fan speed

https://www.intel.com/content/dam/support/us/en/documents/intel-nuc/intel-4wire-pwm-fans-specs.pdf


### BTCDACH21 on 2024-12-23

So is it not possible to decouple the logic shown, which the user sees with speed and percentage, from the logic of the control, where percentage and current pulses play a role? 

Should actually be possible, since the user and the control only have one common parameter (here percentage). Parameter A (speed) can have a different rule/logic for percentage information than parameter B (current pulse). 

Have my thoughts been communicated clearly? 

PS: Here is the data for the fan on the Argon cooler: https://www.yccfan.com/productdetail/106.html 

Here is a picture of the fan: https://x.com/BTCDACH21/status/1870956475117637712?t=mYB3GztGVPVY_GFQBs8hFw&s=19

### MyOwn2C on 2024-12-23

TL;DR: there is really not much you can improve or add to the logic for  PWM % and fan RPM. There is no predetermine relationship from PWM% to RPM. Each fan is different.

Here are the known facts (using YDH6010X05 as example):

<img width="775" alt="image" src="https://github.com/user-attachments/assets/344e9a31-e6c9-4045-a980-b4f15011fcd8" />

- Min PWM% is 30%
- At PWM = 30%, fan RPM is minimum (What is minimum fan RPM? Only manufacturer knows)
- At PWM = 100%, YDH6010X05 spins at 5000 RPM

For example you could program the below logic to the fan controller:

- If temp < 50C, PWM% = 35% (min PWM%)
- If temp =  70C, PWM% = 100%
- You can add more points between 50C and 70C.

Using PWM% , the fan will spin at whatever RPM it was programmed to. You don't know what RPM it will be if it is less than 100%. Only RPM you know is 100% PWM which for case of YDH6010X05 is 5000 RPM.

Also to note: RPM is the least important performance numbers for any fans.

For best performance, you look at the fan's CFM and air pressure. Engineers will take a fan with the lowest RPM but with highest CFM or air pressure any day. Lower RPM mean less power draw, less vibration and less wear on bearings, etc.

It is fan CFM and air pressure that does the actual cooling, not fan RPM. 

Referring to your original thread, your fan is programmed to spin at max RPM from 75% to 100%. There is nothing ESP-Miner can really do about that.

If I am not addressing your question, post a logic flow diagram to show what you are trying to do with temperature, PWM% and fan RPM.


### BTCDACH21 on 2025-01-05

First of all, thank you for the detailed explanation.

I asked myself the question: If the RPM is specified in the OS, but is wrong according to this version, then we don't have to provide this information, right?

Then it would make more sense to specify the required power in amps, wouldn't it?

The approach I had above was that if every fan is different according to your version, the user can enter in a separate field what their fan's theoretical maximum RPM is. From these values ​​you could then calculate the steps 100% 70% 50% 30% in RPM.

Otherwise I really have to question the added value of the speed specification, as it can then be omitted.

### MyOwn2C on 2025-01-05

The most important thing to keep in mind is that fans are only rated at maximum RPM. PWM% to RPM has no direct relationship. 

Only certain is that at 100% PWM fan will work at max RPM. Other than that, nothing is else is certain. 

Even if you let user enter max RPM for the fan used, that is also pointless as again there is no direct relationship from PWM% to RPM. 

For example, the OG fan you first posted reaches max RPM at 75%. This is evident since your RPM at 75% and 100% is the same.  

if 100% is say 5000 RPM, that does NOT mean 50% is 2500 RPM. 

There is also no point in using power as reference, as no 2 ASICs will draw the same power. 

PWM% is useful for those who want to specify a fix fan speed. 

OEM have more control since they know the performances of their chips, fans and heatsink. 

For something like Bitaxe where the user can use anything they want, it is impossible to make any software optimization between fan RPM, PWM% and ASIC temperature. 



### BTCDACH21 on 2025-01-06

Understood, but after this implementation, the "automatic fan function" makes no sense and could be removed to streamline the dashboard. 

If the temperature has reached a critical value in the ASIC and is constantly demanding more from the fan, but the maximum is reached at 75%, the information content is not given because the system and the user think there are still reserves.

After this implementation, it would be more logical to let the fan run at 100% in the base and manually throttle it down by the user to reduce the noise, but here the user will automatically be more sensitive to the setting than if they blindly trust the "automatic function".

Then, in my opinion, the OS interface should be cleaned up and only the relevant conditions should be available if others do not add any value and rather only provide false information.
