# bitaxeorg/ESP-Miner issue #599: Device Overheat Warning: Automatic Fan Control

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/599
> Collected: 2026-10-07
> Published: 2024-12-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 599
- State: closed
- Author: crimsonleaf363
- Opened: 2024-12-26
- Closed: 2026-06-02
- Labels: none

## Description

**Describe the bug**
When Automatic Fan Control is enabled in the AxeOS settings, The miner displays an unexpected message: "DEVICE OVERHEAT! Power, frequency and fan configurations have been reset. Go to AxeOS to reconfigure device." However, upon a inspection of the AxeOS, it appears that the miner is hashing as normal, with no signs of overheating or increased power consumption.

**To Reproduce**
Steps to reproduce the behavior:
1. Enable Automatic Fan Control in AxeOS settings.
2. Monitor the miner's screen for the message

**Expected behavior**
When Automatic Fan Control is enabled in AxeOS settings, the miner should automatically adjust fan speeds and cooling configurations as needed to maintain the optimal temperature. The miner should continue to hash without requesting a manual intervention. 

**Hardware (please complete the following information):**
 - Bitaxe HW version: Ultra 204
 - ESP-Miner FW version: 2.4.2
 - Hash Frequency:  46 Gh/s
 - Voltage:
 - Pool URL, Port, User: Solo


## Comments

### MyOwn2C on 2024-12-26

No issue here. 
Your device did indeed overheated. Hashing at only 46 Gh/s is proof of that. 
You will find that it is set at 50 hz and 1 volt to protect itself from damage. 
it is doing what overheat mode is supposed to do. 
You need to disable overheat message and adjust the freq and volt. 


### leandroalbero on 2024-12-27

https://github.com/skot/ESP-Miner/blob/052b8bfda6b93e2c840cbc6245c82d1bcb60af2b/main/tasks/power_management_task.c#L18

Looks like 75 degrees is a pretty conservative value, maybe adding it as a param to tune it would be worth a try. Not all chips are that sensitive 😄 

### skot on 2024-12-27

We do not have any datasheets... it's a guess. Do you have evidence that it should be higher?

### leandroalbero on 2024-12-28

Based on this page it looks like the maximum temperature is closer to what a normal silicon chip at that manufacturing process is around, take a look at `chip_max` values:
https://support.bitmain.com/hc/en-us/articles/360005088914-Miner-Normal-Operating-Temperature-Range

### leandroalbero on 2024-12-28

I'll also leave this thread over Bitcointalk:
https://bitcointalk.org/index.php?topic=5264464.0
```
Below shows the normal temperature of the miners:

Antminer 	Temperature in degree Celsius
S9 series excl. S9i, S9j, S9-Hydro              

Range: 65 - 115

Chip max. 135

PCB max. 90
```
I know the thread is old and those are S9s, but should be of some reference. 
In any case, maybe @crimsonleaf363 could try using better thermal paste to get a few degrees lower and get rid of the problem

### Barnminer on 2024-12-28

Not a Shitmain or expert on hardware. I do know that the VNISH guys like to target 75C. I think Braiins is lower. This was pre S21 where there were not many temp sensors and the data was rather inconsistent. Not well versed on the latest & greatest. I want to say Asic.to (VNISH) says max operating is probs 90C. We can always ask them & maybe the LuxOS guys. Sure their may be some lurking in git or OSMU. Or reach out to some repair homies. 

### crimsonleaf363 on 2025-01-12

> No issue here. Your device did indeed overheated. Hashing at only 46 Gh/s is proof of that. You will find that it is set at 50 hz and 1 volt to protect itself from damage. it is doing what overheat mode is supposed to do. You need to disable overheat message and adjust the freq and volt.

I ran this setting for about two weeks. Do you think the miner is damaged? I reverted back to the defaults and the fan speed is at 35%.

### MyOwn2C on 2025-01-12


> I ran this setting for about two weeks. Do you think the miner is damaged? I reverted back to the defaults and the fan speed is at 35%.

Unit is not damaged. 
35% fan is too low, thus you overheated. 
use auto fan instead 

### crimsonleaf363 on 2025-01-17

> > I ran this setting for about two weeks. Do you think the miner is damaged? I reverted back to the defaults and the fan speed is at 35%.
> 
> Unit is not damaged. 35% fan is too low, thus you overheated. use auto fan instead

I think auto fan is what caused it to overheat.

### MyOwn2C on 2025-01-17


> I think auto fan is what caused it to overheat.

If auto fan causes overheating, then your cooling is poor. 



### leandroalbero on 2025-01-17

Cooling is poor or auto-fan is not reactive/agressive enough :)

### MyOwn2C on 2025-01-17

> Cooling is poor or auto-fan is not reactive/agressive enough :)

If auto fan is at 100% and unit still overheats, then it is 100% poor cooling. 
Software cannot override laws of physics 😂

### leandroalbero on 2025-01-17

> > Cooling is poor or auto-fan is not reactive/agressive enough :)
> 
> If auto fan is at 100% and unit still overheats, then it is 100% poor cooling. 
> Software cannot override laws of physics 😂

That's what happened to me too, it overheated on auto and dindn't on manual cooling. That's why my comment 🤣
I changed the thermal paste and problemo solved

### crimsonleaf363 on 2025-03-08

> > > Cooling is poor or auto-fan is not reactive/agressive enough :)
> > 
> > 
> > If auto fan is at 100% and unit still overheats, then it is 100% poor cooling.
> > Software cannot override laws of physics 😂
> 
> That's what happened to me too, it overheated on auto and dindn't on manual cooling. That's why my comment 🤣 I changed the thermal paste and problemo solved

I also replaced the thermal paste, but the overheat warning persists even after multiple shutdowns. Did your message disappear?

### mutatrum on 2026-06-02

Fixed by #1304
