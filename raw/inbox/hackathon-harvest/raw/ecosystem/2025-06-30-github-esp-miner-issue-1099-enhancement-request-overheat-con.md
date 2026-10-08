# bitaxeorg/ESP-Miner issue #1099: Enhancement request: overheat control to lower settings till temperature stabilizes

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1099
> Collected: 2026-10-07
> Published: 2025-06-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1099
- State: closed
- Author: plmarin
- Opened: 2025-06-30
- Closed: 2025-11-02
- Labels: enhancement

## Description

It's absolutely annoying to be checking the device status time to time, restore parameters and restart  every time overheat is enabled. Please allow us OC in our devices. 

Thanks.

## Comments

### mutatrum on 2025-06-30

#987 should help a bit. And I think it could be done without a restart as well, with #734. But overheat protection is there for a reason, if that's disabled, the result is a fried chip. And we don't want fire in your house 😉 

Currently it's 75 °C for the ASIC and 105 °C for the voltage regulator (TPS546).

### plmarin on 2025-06-30

OK, good point — I definitely don’t want my house on fire! But… I have a couple of suggestions that might be worth considering:

If overheat mode is enabled, is there any chance the settings could automatically revert to their previous configuration once temperatures return to normal?

Could you add more fine-tuned control? For example, manual input boxes for Frequency and Core Voltage, and also for the overheat threshold. The idea would be to tweak performance within a safe range, increasing or decreasing slightly while being careful with those changes. Would that be possible?

Many thanks!

### KillerInk on 2025-07-01

i made autoclock for my miners. you can set the max fanspeed or powerlimit. and with rising temps it starts to throttle and when it gets cooler it ramp up. runs here stable now for a week and room temps are between 16-34°C^^ i hate summer....
https://github.com/KillerInk/ESP-Miner/tree/autoclock

### skot on 2025-07-01


> If overheat mode is enabled, is there any chance the settings could automatically revert to their previous configuration once temperatures return to normal?

This is tough. What if the Bitaxe is overheating at defaults? (This can happen very quickly if the fan stops or the heatsink isn't right)



### plmarin on 2025-07-02


> This is tough. What if the Bitaxe is overheating at defaults? (This can happen very quickly if the fan stops or the heatsink isn't right)

This could be addressed by enabling a dynamic threshold setting for the thermal protection trigger.

### skot on 2025-07-02

I'm not sure I follow.. are you proposing making the overheat temp threshold adjustable? Why would you want it lower than the max?

### KillerInk on 2025-07-04

@plmarin you need auto tune. overheat is fine as it is. its the last protection bevor you burn you house.

![Image](https://github.com/user-attachments/assets/d657ac0f-c837-4165-8f2b-d331ddb82a14)

### plmarin on 2025-07-04

> [@plmarin](https://github.com/plmarin) you need auto tune. overheat is fine as it is. its the last protection bevor you burn you house.

And how exactly does autotune work? It's not implemented yet, is it?



### KillerInk on 2025-07-04

its more or less based on what the pid controller does. 
you have two limits. one is the fan speed and the other the power in w.
lets say you set fan to 75% and wattage to 15w. the miner will then increase voltage and frequency till it hit one of that limits.
if fan goes to 80% it will reduce frequency and voltage. so with rising rooms temps the fan will excceed the 80% and keep throttle till fan is back below 75%.
if default settings on boot are already to high for the room temp it will start throttle immediatly till voltage 1000 and frequency 400.
if it gets cooler we are then back below the 75% fan speed and it ramp up till watt limit got hit or fan limit again

there is not yet a pr. i do play still alot with the code itself. but its overall working. miners are up now for 4 days and survived 16-32°c room temp without overheating.
some dropped below 800ghs , but its better then overheating^^
