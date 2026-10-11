# Hashrate House system to electrify oil-fired hydronic system

> Source: https://forum.heatpunks.org/t/hashrate-house-system-to-electrify-oil-fired-hydronic-system/116
> Collected: 2026-10-10
> Published: 2025-05-07
> Registry ID: heatpunks-forum

josh | 2025-05-07 16:26:28 UTC | #1

Recently got a @HashrateHouse immersion system set up to provide electric heat to an existing diesel-fired hydronic heating system.

## Existing Hydronic system

Provides domestic hot water as well as heating to the house. Main components:

- 75 Gallon oil-fired water tank

    - Four ports: cold in, hot out, hydronic supply, hydronic return

    - Always-on circulation pump between hydronic supply and cold in ports

- Three air handlers, each with their own thermostat and hot water coil/pump

## Hashrate House system

- Immersion tank for two miners

    - Built-in brazed plate heat exchanger

- Dry cooler with temp controlled EC fan

## Modifications to hydronic system

### Bypass loop

[![Screenshot 2025-05-07 at 9.19.41 AM](https://forum.heatpunks.org/uploads/default/original/1X/8243cad82cf4d41bdc62759e9cbd296d48781976.jpeg)Screenshot 2025-05-07 at 9.19.41 AM904×728 33.1 KB](https://forum.heatpunks.org/uploads/default/original/1X/8243cad82cf4d41bdc62759e9cbd296d48781976.jpeg)
[![Screenshot 2025-05-07 at 9.20.09 AM](https://forum.heatpunks.org/uploads/default/optimized/1X/26ac296fce3bbe5749d105dc3067615b4c1459fe_2_450x500.jpeg)Screenshot 2025-05-07 at 9.20.09 AM918×1020 65.5 KB](https://forum.heatpunks.org/uploads/default/original/1X/26ac296fce3bbe5749d105dc3067615b4c1459fe.jpeg)

To connect the existing hydronic to the Hashrate House heat exchanger it was just a matter of adding a bypass loop before the cold input port on the tank and hooking up to the heat exchanger ports. That way new water coming into the tank as well as the water already in the tank will be passed through the exchanger.

### Circulation pump logic

Since I wanted a way to set the temp for the hydronic tank (other than the built in aquastat for the oil burner), I added a [thermostat controlled plug](https://www.amazon.com/Inkbird-Temperature-Controller-Controlling-Fermentation/dp/B07PVBG8K1). I plugged the pump into this and attached the probe to the tank under the insulation and set the desired temp (140f). That way the pump will run when below the setpoint and stop once its up to temp. You could probably do something more advanced with home assistant but trying to keep it simple.

## Hashrate House config

[![Screenshot 2025-05-07 at 9.20.46 AM](https://forum.heatpunks.org/uploads/default/optimized/1X/5a28022b8b95b56218559c539c8d35f841e08d48_2_322x500.jpeg)Screenshot 2025-05-07 at 9.20.46 AM930×1442 70.7 KB](https://forum.heatpunks.org/uploads/default/original/1X/5a28022b8b95b56218559c539c8d35f841e08d48.jpeg)

I had to add a power outlet for the system but other than that, everything was ready to go out of the box. I had to put some holes through the wall to get the dry cooler where I wanted it (in the garage). Other than that it was just a matter of prepping the miners and dunking them.

I set the dry cooler temp to 50c so that I could capture the heat into the hydronic system. This means the miners are running a little hot but I’m still messing around with finding the sweet spot. If i kept it at the default of 40c i found I wasn’t making enough heat to get the tank up to temp before dumping to the dry cooler.

## Thoughts

I am really happy with the build quality of the Hashrate House system and components (sturdy hoses/fittings/etc.). I had great support from the Hashrate House folks throughout the entire design process and beyond. For my system I should have opted for a larger heat exchanger off the bat but more on that in a later post…

It took a while to get used to the idea that the miners aren’t in control of their temps anymore (the dry cooler is) but things are humming now.

In terms of future plans, I’d like to figure out a way to dynamically scale mining power for the months when I don’t want to heat the garage with the dry cooler. Maybe a bang-bang switch for the whole hashrate house system controlled by the thermostat… I’m also hoping to add another loop to use the heat for a hot tub or pool when we don’t need it for domestic heating.

-------------------------

Cody | 2025-05-07 23:56:43 UTC | #2

Super Cool!!!

Keeping it simple is key.  I just recently had a HomeAssistant “upgrade” mess with some of my settings without me knowing and I had 150F oil temp in my tank!

I’m going to be trying the bang-bang whole system w/ power scaling soon.  I think that is the best compromise to get scalable heat that doesn’t need a dry cooler.
