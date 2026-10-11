# Modify a PCB in order to be able to fix a CPU waterblock?

> Source: https://osmu.xyz/t/modify-a-pcb-in-order-to-be-able-to-fix-a-cpu-waterblock/38
> Collected: 2026-10-10
> Published: 2026-06-10
> Registry ID: osmu-forum

Guepi | 2026-06-10 12:07:58 UTC | #1

I’ve seen many things about the bitaxe, and I’m reading a lot before getting started with it.

Right now, as an old overclocker, I’m thinking about the cooling of the BM : I’ve had a look to some CPU cooler, on AliExpress or on other CPU cooler.

But I’m thinking about fixing those CPU cooler on the bitaxe PCB, but the 50mm * 50mm is not a standard CPU fitting.

So I’m thinking about modifying the PCB in order to set it to a more standard size, like 54mm * 90mm.

So I imagine modyfing the PCB like this :

![modifying-bitaxegt-pcb](https://osmu.xyz/uploads/default/original/1X/e3a784f3c47e9f4317dad96879245a803be47ad9.png)

Yellow : cpu cooler fixation

Green pcb support fixation

Orange : increase of the size of the PCB

Here are my questions :

1. How to be sure that moving the holes to the new yellow position upper the BM has no incidence on the layers beyond ? Is there a tool in kicad to check this ?
2. Is it ok to move the pcb support holes to the new position in green ? (yet, no printed support)
3. Is it ok to increase the size of the PCB without any other change than the size (and of course, the price of the PCB)
4. Did you see any other component, on this side of the bitaxe Gamma Turbo, that would be pleased to be under a CPU cooler / waterblock ?

-------------------------

skot | 2026-06-10 12:14:45 UTC | #2

I think this is a good idea. It should be relatively easy to do.

1. moving the heatsink mounting holes should be no problem as they are not electrical. Kicad has a Design Rule Check (DRC) function that you can run to make sure you have not created electrical problems.
2. moving the PCB mounting holes to the locations you have in green could cause problems with traces in that location. I’d suggest moving them outside the current bitaxe borders.
3. the only thing you need to worry about with making the PCB bigger is that you do not add metal layers around the ESP32 antenna. “empty” fiberglass PCB around the antenna should be ok.
4. The backside of the TPS546D24 voltage regulator would benefit from active cooling. It’s always a challenge though because it needs to be the exact same z-axis height.

-------------------------

Guepi | 2026-06-11 12:38:21 UTC | #3

Thank you @skot for your answer.

I’m trying to find the antenna on the PCB, but did’nt find it yet.

-------------------------

skot | 2026-06-18 22:26:30 UTC | #4

The antenna is the black tab on the ESP32 module. in your board layout the blue rectangle in the upper left is the keepout box.
