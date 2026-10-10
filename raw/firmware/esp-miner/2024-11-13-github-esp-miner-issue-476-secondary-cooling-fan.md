# bitaxeorg/ESP-Miner issue #476: Secondary cooling fan

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/476
> Collected: 2026-10-07
> Published: 2024-11-13

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 476
- State: closed
- Author: zcht
- Opened: 2024-11-13
- Closed: 2025-10-21
- Labels: none

## Description

Since the Supra and especially with the Gamma, more and more two-fan solutions are being implemented by many in the community. 

As is well known, the back of the PCB is extremely hot, especially the v. regulators. 

Here it would be cool if we could implement a second controller for a second fan in the AxeOS. For example, a 40mm fan can turn faster where a 60mm fan can turn slower on the back. This serves to optimize cooling, but also possibly to reduce noise. 

It would also be great if both fan parameters could be displayed in the dashboard. 

I don't know what the hardware side is like, some dealers only probe one fan connection, some two, and I have two Gammas where there are three connections. Of course, it would be desirable to be able to design 2 x 4-pin connections on the PCB and set this as a kind of standard. 

## Comments

### mrv777 on 2024-11-14

There actually is two fan points, but usually just one has the port solder on.  I wonder what would happen if you solder on both ports and use both of them

### mrv777 on 2024-11-14

On another note, the Noctua fans come with a splitter making it easy to have the old stock fan on the back and power both with one plug.

### skot on 2024-11-14

the two fan connectors on the gamma are just tied together, so this would be the same as the Noctua splitter, afaik

### zcht on 2024-11-16

The splitter of the Noctua is only an alternative solution. What if I don't use Noctua fans, the splitter would have to be bought separately. But that is not the point. 

It would be cooler if we simply had a two dedicated fan line, where you can set the speed for the second fan and the second fan is displayed in the dashboard. 

Let's say we use a cheap fan for the back, which is sufficient if it rotates at 3000 RPM, by copying it to a line, the ASIC fan rotates at 5000 RPM. This signal is passed on to the second fan, which also turns at 5000 RPM, although it doesn't have to. 

I simply want to have an additional second fan connector that can also be set and monitored separately. 

the Noctua splitter solution is just ugly without end, you have various long cables hanging around the bitaxe that have to be wrapped somehow so that it looks halfway decent.

### MyOwn2C on 2024-11-16

If there are 2 fans, then we need to specify which fan connector is for ASIC and which fan connector is for AUX. 
With beginners' luck someone will always connect the wrong fan. 
Having 2 fans with dedicated PWM increases complexity. 
It is not as easy as you say that one fan "passes" the PWM to the next fan.
If you look at Noctua spilt cables, one fan gets all 4 pins, with tachometer and PWM. The other fan only gets PMW. So both fans run off the same PWM, but only the first fan RPM is fed back to the controller. 
If you really want a second fan with full PWM control, you are free to take the schematic and add another EMC2101 to ESP32. You will also need to write your own software for it. 
Note that ESP32 isn’t very powerful. The less work it needs to do, the better. 
You can also build a separate circuit with temp monitoring and with as many fans as you want, using API output from Bitaxe.


### zcht on 2024-11-17

Hmm, I actually see it a bit more pragmatically. Let's say we have two 4-pin fan connectors. One for the ASIC, which is labeled on the PCB, and a second, which is described as AUX. In the dashboard, you would be able to see which 4-pin fan connector has a PWM fan if you had grabbed the wrong connector. And even if you only have one fan and one connection, you will see it in the dashboard and can adjust it in the settings. 

We have to learn a few things from the PC market. To say that users are too stupid to connect a second fan is a bit short-sighted. As with any hardware, you have to deal with the device and possibly read documentation. A hair dryer, for example, also has several stages. If someone wonders why only one comes out with so much less air than with five, you have to take a quick look at the manual. I hope you understand what I mean. 

I wouldn't increase the complexity by creating more and more forks of the firmware. At some point we will have a forest of firmwares, each one can do something different, but never holistically what can actually be considered standard. The fact is, we are running into overheating problems , which will lead to even more problems in the future. A two-fan interface would be a quick win for many. Whether you build your own case and can control a second fan through it, or whether the fan is attached to the PCB holder. 

That would just be a very nice feature, which would certainly be used by many. Completely separate from aftermarket products like the Noctua splitter. 

### sidehack-gekko on 2024-11-17

Haven't dug into it too much but EMC2104 appears to support two fans from a single chip.

### WantClue on 2025-10-21

with the component config adding more i2c devices is trivial and this issue will be closed as solved.
Devices with an additional emc2101 can easily be supported
