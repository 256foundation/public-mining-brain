# 256foundation/libreboard issue #8: Feature request: provision for graceful shutdown on power loss

> Source: https://github.com/256foundation/libreboard/issues/8
> Collected: 2026-10-07
> Published: 2025-05-03

- Repository: 256foundation/libreboard
- Type: issue
- Number: 8
- State: open
- Author: rkuester
- Opened: 2025-05-03
- Closed: n/a
- Labels: enhancement

## Description

Mujina OS would like the ability to gracefully shut down in the event of a power loss to shut down applications, write logs, avoid filesystem corruption, etc., but it needs a little help from the hardware. Perhaps supercaps or a small battery keeping the CM5 powered in the event of a power loss, and signaling for Linux to determine that the power has been lost. Having at least ten seconds of reserve would be ideal, but we might be able to make due with less.

## Comments

### Schnitzel on 2025-05-05

Ah great idea! Let me look what we could leverage from existing solutions, maybe there is a Raspberry PI HAT that already provides such a solution?

### zbomz on 2025-05-05

I love this idea, but I would caution to not take it lightly thinking it's and easy implementation. We had to implement a small backup battery on the Owlet base station to ensure we could alert the user of a power loss in order to meet FDA requirements. The most challenging part of implementing something like this is designing for the worst case scenario of having multiple asynchronous, bursty loads (wifi, hdmi, ethernet, compute, etc.) fire at the same time when operating from the battery before the loads can be disabled. Judging by the 3D renderings I've seen on X, it looks like a CR2032 primary coin cell is being used to supply the backup power (sorry for the ensuing rant if I'm wrong on this). 

While the capacity of the cell might be high enough to last for the requested 10 seconds, its internal impedance will be an issue. Primary coin cells have relatively high internal impedance that will cause the battery voltage to droop prohibitively low during short load bursts and result in a brown out. For example, the typical max "pulse current" for a lithium manganese CR2032 cell is 15mA. The idle power consumption of the CM5 is typically 400mA. The operating power consumption is typically 900mA. Add the possibility of Wifi transmitting when power is lost, and you're looking at over 1 amp of current draw. No single coin cell is going to be able to support that. You need something with low internal impedance. A small lithium polymer rechargeable battery with an accompanying charge controller IC is your best low-cost option for meeting the pulse current requirements, but it may not be suitable due to its sensitivity to temperatures above 70C. 

### rkuester on 2025-05-05

> [....] Judging by the 3D renderings I've seen on X, it looks like a CR2032 primary coin cell is being used to supply the backup power (sorry for the ensuing rant if I'm wrong on this). [....]

No sorry—your input is great! For what it's worth, the only purpose of the CR2032 in the current design is to power the real time clock. What I'm proposing isn't a part of the design yet. Yes, it'll take much more than a CR2032—a supercap or two, or a small battery, and due integration with the main supply power design.

### Schnitzel on 2025-05-05

what @rkuester said :)

### zbomz on 2025-05-05

Got it. Sorry for the rant about the coin cell! lol 

Out of curiosity, I started musing about what it would take to supply 1A at 5V for 10 seconds. I'm trying to think of the lowest cost way to do it. What kind of budget are you hoping to implement this for?
