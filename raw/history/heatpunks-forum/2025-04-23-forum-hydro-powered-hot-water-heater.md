# Hydro powered hot water heater

> Source: https://forum.heatpunks.org/t/hydro-powered-hot-water-heater/56
> Collected: 2026-10-10
> Published: 2025-04-23
> Registry ID: heatpunks-forum

josh | 2025-04-23 14:46:30 UTC | #1

Here’s my domestic hot water heater setup. The core component is the CryoByte water plates and a brazed plate heat exchanger. This lets me heat up my hot water tank (and preheat new incoming cold water) using hashrate. My goal was to keep it as simple as possible in terms of control (no home assistant etc.). I like the hydro approach vs immersion in this case since it takes up very little space.

Big thanks to folks like Schnitzel, RevHodl for the inspiration to tinker and to Ryan at CryoByte Labs for making the hardware that makes this possible.

[![Installing CryoBlock](https://forum.heatpunks.org/uploads/default/optimized/1X/ed76e4e460f6fb55caede6aa14921e544485837f_2_281x375.jpeg)Installing CryoBlock1920×2560 643 KB](https://forum.heatpunks.org/uploads/default/original/1X/ed76e4e460f6fb55caede6aa14921e544485837f.jpeg)
[![Water heater plumbing](https://forum.heatpunks.org/uploads/default/optimized/1X/0c0831969cb47b0eed49b2add03d2bd63417284d_2_281x375.jpeg)Water heater plumbing1920×2560 580 KB](https://forum.heatpunks.org/uploads/default/original/1X/0c0831969cb47b0eed49b2add03d2bd63417284d.jpeg)
[![Miner](https://forum.heatpunks.org/uploads/default/optimized/1X/e8c49bc11576e5b9ffd90024478a96434e4030b1_2_281x375.jpeg)Miner1920×2560 336 KB](https://forum.heatpunks.org/uploads/default/original/1X/e8c49bc11576e5b9ffd90024478a96434e4030b1.jpeg)

Miner side (distilled water):

- S19J Pro

    - CryoByte Labs cold plates

    - Modified power supply 140mm fan/duct for noise reduction

    - Luxor firmware with ATM

- Aluminum reservoir

- Generic hot water circulation pump

- 30-plate brazed plate heat exchanger

- 360mm radiator + quiet fans

- EPDM tubing

- Misc fittings

- Corrosion inhibitor in distilled water

Water side:

- 40 gallon domestic gas hot water heater

- Add pex pipe to water heater drain valve

- Generic hot water circulation pump

- Check valve and tee at the heat exchanger input

    - Tee with cold supply in

- Thermometer to set target temp and control pump

Control/Logic:

- Thermostat: If water temp < 140f, run water circ pump

- WiFi smart plug: If between 4pm - 9pm, turn off pump ($$$ electricity rates)

    - Water heater gas knob is set to 115f so showers between these times (or long showers) will be powered by gas

- Cron job on home server: If between 4pm-9pm, curtail mining

- Luxor firmware ATM over/underclocks automatically based on demand

Initial observations/thoughts after running for a few weeks:

1. A radiator, heat dump, or using the miner fans is necessary if you want to get the HWH up to 140f in a reasonable time. You can go from 110 → 130 no problem but after that the differential is too small and boards overheat unless you dump some excess

2. I’m running a cron job to sleep the miner during peak power times and at night. It turns back on in the morning so it’s ready for showers, laundry etc.. . I like this approach more than a home assistant setup since it is way simpler

3. Luxor ATM feature scales up and down very nicely as the HWH calls for heat. I set the ATM timing to 1 minute and it adjusts quickly. If someone’s having a long shower it can overclock like a champ as the cold water comes into the tank

4. Luxor doesn’t let you shut down individual boards via API if you’re using ATM (ytho?). It would be nice to cut down to one board once the HWH temp is getting close to/at target (135f-140f). More efficient to have one board at about 400mhz vs 3 boards at 100mhz.

5. We don’t use enough hot water to justify the full 3kw. This unit could easily provide heat to half of my house in addition to the HWH. It could be a “central heat mine” and have branches to radiator in the HVAC, pool, etc..

6. Pex and pipe insulation is cheap - you don’t need the miner to be next to the HWH if you can run pipes from wherever you have the power

7. Need to insulate the components (tubing, HX, reservoir) otherwise the room will get pretty warm (unless you want that)

-------------------------

tronsington | 2025-04-23 19:57:13 UTC | #2

This is so cool. How often is the miner actually running? I’m curious if you could add some logic for it to turn on when you know hot water demand is coming (shower, dishwasher, washing machine, whatever else at at regular times). What size reservoir are you using for this set up?

-------------------------

willsabc | 2025-04-23 20:10:43 UTC | #3

This is great! Thanks for the details. This is similar to the setup I want to do at our new place that has an electric HWH. I might be bugging you for advice here soon

-------------------------

SoftwarmLLC | 2025-04-23 23:31:27 UTC | #4

What kind of chip temperatures are you pushing the jPro to, and whats your efficiency when it gets hot?

-------------------------

josh | 2025-04-25 21:14:48 UTC | #5

Right now i have it on constantly from 4am - 4pm but it really depends on the weather. It’s too hard in my case to plan out usage (not much around here happens on a regular schedule :slight_smile: ). This is on a 45 gallon tank so the gas does kick on if someone has an extra long shower. It really works great for laundry etc. throughout the day since it takes a while to “recharge” the tank after using compared to the gas.

Since the radiator in the loop vents into a cold area of the house I was able to replace a loki space heater with the radiator so that worked out well for heating season.  Its getting warmer now so I’m figuring out the best way to either curtail when water is at temp or dump the heat somewhere else since when we have excess solar coming in.

I’ve been trying to keep the system as “dumb” as possible and stay away from home assistant but might have to go down that road if I want finer control…

-------------------------

josh | 2025-04-25 21:23:20 UTC | #6

I’m setting Luxor ATM to target 62c so if there’s demand for hot water it will crank up and be somewhere around 27-28J/T, a little worse if it has enough time to overclock. When it’s up to temp and idling though ATM drops it way down to 100MHz which destroys efficiency (Lux reports 55J/T).

When it was cold I could turn the fans on the radiator all the way up and let it cook but now it’s too hot in the house to do that…

I’ve been playing around with disabling boards during the day when nobodys using water which lets me keep one board going at a much better efficiency but then I have to micromanage…

-------------------------

josh | 2025-05-07 14:25:01 UTC | #7

Followup:
I have caved and started using home assistant to more intelligently control the water heater. Now that it’s getting warm here I don’t need the extra heat in the room.

Since the thermostat on the pump is not network enabled, I am using a wifi plug with a built in power meter for the thermostat/pump to detect when the tank is calling for heat. If the tank is at target temp, the pump is off and the plug reads low wattage and I can curtail mining. Otherwise if the wattage is >50w, the pump is running (tank is calling for heat) so start mining.

Still going to try to run pipe out to the hot tub or pool to use excess solar once I am motivated enough to crawl under the house…

-------------------------

HashrateHouse | 2025-05-07 15:17:07 UTC | #8

I love this great writeup! I’m curious on the heat exchanger your using…

I’m just starting to test with these hydro systems and for a long time a huge Benefit I saw with immersion v hydro is the presence of galvanic corrosion or not…

In an immersion build the fluid is non conductive so you can mix all sorts of metals in the system without much issues, where as with hydro, water itself is conductive so you could end up with some interesting corrosion points (even with inhibitors due to the aluminum heat blocks on hydro systems) if you don’t match up the metals aka the copper brazing on the SS heat exchanger is cathodic and will corrode the AL heat block (anodic) over time…

Could possibly use deionized water with the inhibitors to help mitigate this… But would need to monitor this as it can become conductive over time.

However this is all “in best practice” and theory on my end so would love to hear how this holds up. Keep us posted on the build!

-------------------------

HashrateHouse | 2025-05-07 15:27:32 UTC | #9

Could also skate a fair amount of this with using “slightly” cheaper than TI, Nickel-brazed stainless steel plate heat exchangers, although still much more than copper brazing they work in more corrosion sensitive applications (will be testing on on my build and keep you posted)

-------------------------

josh | 2025-05-07 19:03:26 UTC | #10

I had considered using [something like this](https://www.amazon.com/dp/B0CYSDYGJB) since it’s AL but in my case I used a regular (copper brazed) stainless.  Also have to assume the exchanger will be exposed to various metals on the water side as well (I have copper plumbing) so an AL exchanger would then be the thing being corroded.

I was thinking that since the tubing runs between the aluminum and the heat exchanger are pretty long and plastic that would help but that could be completely made up. At this stage I’m willing to be a beta tester and see how long I can run before things start failing. :slight_smile:

Curious if anyone has gone down the jet ski oil cooler route…
