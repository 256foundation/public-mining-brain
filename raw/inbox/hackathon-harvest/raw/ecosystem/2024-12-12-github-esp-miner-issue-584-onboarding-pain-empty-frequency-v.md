# bitaxeorg/ESP-Miner issue #584: Onboarding pain: empty frequency value

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/584
> Collected: 2026-10-07
> Published: 2024-12-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 584
- State: closed
- Author: alltheseas
- Opened: 2024-12-12
- Closed: 2025-01-07
- Labels: none

## Description

_What happpened_

New 601 gamma bitaxe was not hashing. After too many moments of trying to figure out what is broken, it turned out the 'Frequency' value was null. I did not set this to null. 

It could be that overheating protection triggered this null value, or value was null by default. 

_Suggestion_

In order to reduce onboarding friction, consider including a UI signifier that clearly communicates to a non-technical newbie that a Frequency value is required in order for the miner to hash.

Consider that the newbie onboarding to Bitaxe will not know what is going on, and may not be in the settings menu. Therefore consider UI signifier/warning/error message if/should be displayed on all AxeOS screens (not only on the settings submenu). 

Consider also displaying on the Bitaxe hardware display: e.g. "Bitaxe frequency is null; miner not hashing".

### Mockup

![axe freq](https://github.com/user-attachments/assets/82d88584-bff8-488f-a089-7d1c55fbf199)


## Comments

### mrv777 on 2024-12-12

Hmm, I'm not sure all of the cases of this or how it got to null, but we could maybe add an alert on the dashboard if the frequency is below maybe 400 (that includes null)

### alltheseas on 2024-12-12

That would have prevented me one hour of head banging, sounds great.

Out of curiosity, what unhappy paths would cause AxeOS to set a frequency value 400 or lower (non-null)?

### mrv777 on 2024-12-12

I know overheat mode will set it low, not sure if its null or something like 50, not sure about other ways

### eandersson on 2024-12-12

It's likely not set to null, but rather 50 does not exist in the drop down so it does not know what to map it too. The same is seen when overclocking as well.

### alltheseas on 2024-12-12

> It's likely not set to null, but rather 50 does not exist in the drop down so it does not know what to map it too. The same is seen when overclocking as well.

Why is that hashrate was zero? Does anything below some value (e.g. 400) not produce hashrate?

### eandersson on 2024-12-12

> > It's likely not set to null, but rather 50 does not exist in the drop down so it does not know what to map it too. The same is seen when overclocking as well.
> 
> Why is that hashrate was zero? Does anything below some value (e.g. 400) not produce hashrate?

It should still produce some hashrate. If it wasn't something else was likely wrong as well (e.g. statup process failed), and I don't believe the code could handle a zero or null value without crashing at startup.

### alltheseas on 2025-01-30

![Image](https://github.com/user-attachments/assets/22896a3b-c3eb-4482-8656-55f19a058f51) 

confirming on v2.5.1 "custom" value is 50. 

I don't know what "custom" means though. 

Maybe "failsafe", or "overheat protection" brings more clarity.


### MyOwn2C on 2025-01-30

> ![Image](https://github.com/user-attachments/assets/22896a3b-c3eb-4482-8656-55f19a058f51)
> 
> confirming on v2.5.1 "custom" value is 50.
> 
> I don't know what "custom" means though.
> 
> Maybe "failsafe", or "overheat protection" brings more clarity.

If freq is 50, it overheated. 

### alltheseas on 2025-01-30

> If freq is 50, it overheated.

Thanks for confirming. In this case, consider changing "custom" to "miner overheated" or similar
