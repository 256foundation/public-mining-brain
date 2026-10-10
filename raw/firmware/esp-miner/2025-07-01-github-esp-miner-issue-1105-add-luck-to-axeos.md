# bitaxeorg/ESP-Miner issue #1105: Add luck to AxeOS

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1105
> Collected: 2026-10-07
> Published: 2025-07-01

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1105
- State: open
- Author: skot
- Opened: 2025-07-01
- Closed: n/a
- Labels: enhancement, help wanted, good first issue

## Description

Mining "luck" is a metric to indicate if the difficulty shares you have found are above or below average for your hashrate and the time you have been mining.

This would be pretty slick to add to the AxeOS dashboard.

## Comments

### Travetown on 2025-08-15

People often talk on Discord about how frustrating it is when there's no change in session difficulty. It's kind of boring when nothing changes for days on end. It's all totally understandable from a math perspective. But not everyone is a nerd who can figure that out. Then there's stuff like “it's always better after a restart” and so on. 
A few days ago, I took a screenshot in OSMU Discord. But I can't find it anymore. Never mind. 
How about integrating a similar graphic into the dashboard as an option? Maybe the high score for every 2 or 4 hours of runtime per worker (last 24h). It's probably not very complicated, since all the data is already available. 
I think it would calm some people down a lot. 

<img width="432" height="327" alt="Image" src="https://github.com/user-attachments/assets/83c24111-8e48-4020-998a-64e78d00c901" />

### skot on 2025-08-17

I think luck would be a really useful and fun stat to show on the main AxeOS dashboard.

### adammwest on 2025-08-18


This will be a good feature

Definition 
Expected hashrate = small cores * frequency 
Luck = hashrate / expected hashrate

There is a gotcha 
Like hashrate luck is based on a difficulty level 
So it could be chip luck or pool luck. Or any specific difficulty level.

There is a decision to be made of which luck.

Finally most chips are not 100% luck so a warning or tooltip for the user explaining that it should be in a range, rather than a specific value.

### skot on 2025-08-18

Shouldn't miner luck be;

Expected time to best share diff / actual time to best share diff

Expected time to share diff should be calculated using the miner's actual hashrate?

### Travetown on 2025-08-19

This is what I always do in my private experiments (for fun):
The time since the last reboot is known. This can be used to calculate the theoretical difficulty at the current hashrate.  Of course, the exact time at startup is taken into account. It is only suppressed here.
I have always used the expected hashrate. This seems to be amazingly accurate and also corresponds very well with the hashrate calculated by CK-Pool. The average is often a little too high (at least for me).


<img width="584" height="143" alt="Image" src="https://github.com/user-attachments/assets/83549d7f-c661-463e-84d7-1ba49aab7678" />

### adammwest on 2025-08-20

> Shouldn't miner luck be;
> 
> Expected time to best share diff / actual time to best share diff
> 
> Expected time to share diff should be calculated using the miner's actual hashrate?

I think these are all the same 
My definition was
Luck = Hashrate / expected hashrate 
 = (Shares* diff * 2^32 / elapsed time)/ Expected hashrate

The best diff defenition
Best diff luck = Expected time to best share diff / actual time to best share diff

Expected time to best share diff = best diff * 2^32 / expected hashrate
Actual time is just elapsed time 

Best diff luck = (best diff *2^32 / expected hashrate )/ elapsed time

They are equivalent when diff = best diff and shares = 1
