# bitaxeorg/ESP-Miner issue #1347: Strange behavior when surrounding temperature drops

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1347
> Collected: 2026-10-07
> Published: 2025-11-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1347
- State: open
- Author: kukulle-hood
- Opened: 2025-11-12
- Closed: n/a
- Labels: none

## Description

Hello Folks,

I am running a bitaxe 602 with the latest pre-release v2.11.0b6 firmware and from the hardware side I have a setup from "bitcooler" with a BIG heatsink on the front but with a different, much stronger cooler on the rear side of the system.
This gives me the posibility to let the system run stable easily on 1100MHz and 1,320V since the last 2 month.

I have to admid, that the system is loud and that is why I placed it in another room at the windowsill recently.
Here I of course have to open the window from time to time to get fresh air and here I also noticed a strange behaviour.

Due to winter time colder air comes in and the fans and system are cooling down the bitaxe to around 5°C general colder.
From the graph in my browser view I can see, that as soon as the system (in this case especially the voltage regulator on the backside , VR Temp) drops from standard 65°C to 60°C, but parallel also the Hashrate goes down.
I have checked this several times and always the same bahaviour what I find a bit strange.
Is this "normal"? I always thought to have the system colder is better (at least at around 55°C)
So does this mean that it is better to have the VR running a bit hotter?

What are your experiences on your systems?

BTW, ...on the latest Firmware after approx 1,5 hours the hashrate registers heatmap shows Errors but I think this is already known.

Thanx for some feedback and Ideas

<img width="2878" height="2475" alt="Image" src="https://github.com/user-attachments/assets/73827edd-1eb0-4e5b-98b4-286591d9a399" />

Robert


## Comments

### mutatrum on 2025-11-12

Can you expand on the errors? That could hint at why you're dropping hashrate, seems the chip is not happy at the lower temperatures and calculations fail. Maybe you have to change the core voltage slightly, but I have no idea what you're running at now.

Running latest beta (v2.11.0b6) improves how the error percentage is reported, and you can put the Error percentage on the graph as well. Maybe try installing that?

### kukulle-hood on 2025-11-13

Hello @mutatrum , Thank you for your reply and thoughts.

I have restarted the system and also deleted the cache from the browser.
NOTE: The image with this behavior above was already with the v2.11.0b6.

Since the restart and cache clearance I do not have any Hashrate Registers Errors indication in the down-right position of the dashboard any more (even after 3 hours). I only have a "3 Low difficulty share (0.08 %)" indication in the Shares section (top-middle position), but this is more linked to the pool I think.

But behaviour is still the same, ...as soon as it gets colder, the average Hasrate drops around 100 per 5°.
Not a big thing, its simply strange. 
Unfortunately it seems to me, when I look in the pools, at the reseller and  in the aftermarket, there are not many people using the bitaxe 602. Maybe it is a typical 602 behaviour and the 601 is "normal".

Robert

### KillerInk on 2025-11-21

from my findings, every asic has a different comfortable temperature. most of my miners dont like to run below 60°C also above 65°C they start dropping. vr temp seems not to affect it.

### WantClue on 2026-06-01

is there any update or additional information you feel needs to be added? otherwise i think we can close this issue
