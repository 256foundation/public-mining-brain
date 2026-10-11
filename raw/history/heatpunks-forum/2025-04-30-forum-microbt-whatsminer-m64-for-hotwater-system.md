# MicroBT WhatsMiner M64 for hotwater system

> Source: https://forum.heatpunks.org/t/microbt-whatsminer-m64-for-hotwater-system/109
> Collected: 2026-10-10
> Published: 2025-04-30
> Registry ID: heatpunks-forum

Satoshi | 2025-04-30 14:32:10 UTC | #1

I´ve recently bought the new **MicroBT WhatsMiner M64** and trying to find the best/most efficient Liquid cooling/heating Solution.

**The main (expensive) idea is:**
using only stainless steel components. steel pump, pex pipes, uv-light (anti-bacteria), heat exchanger (fully steel as well) to connect to existing heating system.

*The purpose is to deliver 80 degrees hot water for daily usage.*

**Second (cheaper) idea** is to use cheaper components like normal 100$ pump and copper heat exchanger.

The liquid will be distilled water with anti corrosion fluid anyway.
what do you think about these two ideas?

or is it necessary to get a **hydro server rack** like *HeatCore HS05* which has everything integrated already?

cheers!

Satoshi Nakamoto

-------------------------

BitHeat | 2025-05-02 23:09:49 UTC | #2

I’m pretty sure those require 3phase input though. I’m pretty this what the rep said in Nashville last year. From what he said it would be able to operate fine at 80C output with only like a 70C input and be stable. Imagine though you’d need a pretty good flow rate to achieve this. They are the hottest running water cooled rigs that I’ve found.

I have not ran them myself though may consider it if I get a pool I need to heat because they take like 5kw. Currently working on a offgrid living box and I’m pretty sure I’ll be going with a 3 phase setup though I’d go broke buying the panels to run it lol.

-------------------------

Satoshi | 2025-05-05 08:00:23 UTC | #3

Thanks for your reply!

We got the normal 220V model one phase actually.
let’s see how it will work. we will probably built our own system to test and use this one.

cheers

-------------------------

power2bit | 2025-05-06 15:44:21 UTC | #4

Has anyone successfully powered a M64 using a 20A C19 PDU outlet?

Thinking about how to best power this thing up without a specialized cooling cabinet.

-------------------------

tylerkstevens | 2025-05-06 16:09:53 UTC | #5

You could definitely build your own solution with the right pump and heat exchanger. I think the beauty of the HeatCore H series is the complete package is already setup for this use case.

What I’m curious about is how the system ramps down power or cycles on and off to match your heat demand.

For example, in a hot water heater setup, as the tank heats up, the miner MUST reduce it’s wattage or total heat delivery (on vs off time) or else it will start to choke, as the heat can no longer be absorbed by the tank.

I’ve been thinking about trying this heat radiator with an integrated pump to use the M64 in an air based heating system.

[Zeus Mining](https://www.zeusbtc.com/ASIC-Miner-Repair/Parts-Tools-Details.asp?ID=3047)

### [Lianli ASIC water cooling row 8KW](https://www.zeusbtc.com/ASIC-Miner-Repair/Parts-Tools-Details.asp?ID=3047)

Lian Li 8KW ASIC water cooling row is used for overclocking ASIC miners to achieve efficient heat dissipation.

Price: USD Get Quote

-------------------------

power2bit | 2025-05-06 17:24:28 UTC | #6

> **tylerkstevens:**
>
> > I’ve been thinking about trying this heat radiator with an integrated pump to use the M64 in an air based heating system.
> >
> > [Lianli ASIC water cooling row 8KW | Zeus Mining](https://www.zeusbtc.com/ASIC-Miner-Repair/Parts-Tools-Details.asp?ID=3047)

Seems like a pretty affordable way to test. You can only control the fan speed though. To get consistent 80C output (for research & testing) some kind of thermal regulation would be needed.

I think the HS05 has this, but its pretty expensive just for testing.

-------------------------

HashrateHouse | 2025-05-07 14:53:30 UTC | #7

Just got my hands on a M64 as well and looking to build out the integrated solution… Didn’t know you could get your hands on a HS05 yet? What was the price point your seeing?

I would say you would be fine with a plastic hot water pump for the hydro loop as for heat exchangers yes no copper is the word on the street, trying to find a good solution to this apart from TI…

Tyler hits the nail on the head with all these solutions is how do the control work to maximize heat and profit with minimizing mining with no heat demand…

-------------------------

HashrateHouse | 2025-05-07 14:54:34 UTC | #8

If you don’t have a PDU with the SA2-30 plug I think your only option is to splice in a c20 plug… Haven’t found a c20 to sa2-30 converter yet could be another option!

-------------------------

Satoshi | 2025-05-12 07:25:57 UTC | #9

Thank you guys for all the replies!

we didn’t try the C20 to sa2-30 converter yet but this is probably the way to go!

the hashrate demand/power usage is still pretty interesting (also the whole software and device). We will see and let you know once we tested.

maybe someone else is faster :slight_smile:

looking forward to see this bad boy finally in action

cheers

-------------------------

power2bit | 2025-05-12 09:44:17 UTC | #10

C20 is typically rated for 16A (CEE) and max 20A.
The M64 is labeled for up to 25A, which seems high.
Our PDUs safely deliver 20A, giving us ~4600W peak — should be enough, but not 100% sure why the M64 is rated that high, given its peak power is 4099W.
Hopefully, splicing in our own adapter will work — let’s see.

-------------------------

power2bit | 2025-06-05 10:18:48 UTC | #11

**Initial M64 Hydro Test – 80–90°C Outlet Water Achieved**

We ran initial tests on the M64, and results are promising. Hitting 80°C outlet water temperature was easy, and even 90°C was briefly reached without issues. We didn’t sustain those temps long-term, but it’s impressive to see the system handle them.

One downside: the *Upfreq* process is noticeably slower than on Bitmain devices. Our small water reservoir reached high temps quickly—before the unit hit full 200TH. In early tests, we didn’t observe major differences between low, normal, and high power modes. Interestingly, we achieved 200TH on low power mode during the first run (took about 25min of upfreq).

**Conclusion**: 80°C operation is clearly feasible. For longer tests and real-world simulation we’ll have to integrate a dry cooler or other cooling source to stabilize temps and simulate customer environments more effectively.

[![image](https://forum.heatpunks.org/uploads/default/optimized/1X/fd8c80b31ba1dc03a44edc35b6608b761696d1a0_2_603x500.jpeg)image1842×1526 263 KB](https://forum.heatpunks.org/uploads/default/original/1X/fd8c80b31ba1dc03a44edc35b6608b761696d1a0.jpeg)

[![image](https://forum.heatpunks.org/uploads/default/optimized/1X/fd8c80b31ba1dc03a44edc35b6608b761696d1a0_2_603x500.jpeg)image1842×1526 263 KB](https://forum.heatpunks.org/uploads/default/original/1X/fd8c80b31ba1dc03a44edc35b6608b761696d1a0.jpeg)

-------------------------

power2bit | 2025-06-05 10:25:38 UTC | #12

**Power Setup**

For testing, we connected two 16A C19 outlets from our PDU to the M64’s 25A input.
**Important:** Both connections must come from the *same phase* (e.g., L1). Using different phases risks a 400V potential difference — which can seriously damage the miner.

[![image](https://forum.heatpunks.org/uploads/default/optimized/1X/4495c03ad5e1bf2497d37721fb505ef42bfcbfe6_2_666x500.jpeg)image1280×960 153 KB](https://forum.heatpunks.org/uploads/default/original/1X/4495c03ad5e1bf2497d37721fb505ef42bfcbfe6.jpeg)

**To ensure safe deployment in a production or customer environment**, I designed a simple wiring concept that our electrician will now build. It allows the M64 to operate safely using either a PDU or two standard 230V outlets — as long as both are on the same phase.

**Why this design?**
The setup combines two 230V/16A inputs (same phase) to deliver a single 25A output. Since one input alone can’t supply enough current, both are required. Relay logic ensures that the output is only enabled if *both* inputs are present. If either input fails, the circuit shuts down entirely — preventing overload and ensuring safe operation.

[![image](https://forum.heatpunks.org/uploads/default/optimized/1X/3327a3cc24c2420174b08cf22b587aa513376520_2_416x500.png)image878×1054 43.7 KB](https://forum.heatpunks.org/uploads/default/original/1X/3327a3cc24c2420174b08cf22b587aa513376520.png)

-------------------------

power2bit | 2025-06-06 17:00:36 UTC | #13

Update: Even though MicroBT labeled our M64 as 4099W I have observed it going all the way up to 4800W. Definitely too much for 16A or even 20A at 230V.

-------------------------

thak777 | 2025-06-06 23:14:19 UTC | #14

This is one of my biggest frustrations with these miners. They run so far outside of specifications based on environment that it’s hard to plan for things until you have the exact device(s) in hand.

My S21 machines were widely variable: some were right at spec, but most were easily 10+% higher wattage/amperage depending on heat/humidity.

Super glad I had PDUs with breakers and readouts to show me when things started getting scary.
