# Production Ready Hydronic Boiler.....maybe

> Source: https://forum.heatpunks.org/t/production-ready-hydronic-boiler-maybe/212
> Collected: 2026-10-10
> Published: 2025-11-03
> Registry ID: heatpunks-forum

Cody | 2025-11-03 13:33:34 UTC | #1

I [posted](https://heatpunks.org/t/new-old-school-boiler-control-idea/55) a while ago about simplifying my control setup on my hydronic boiler.  I have made those changes and in this post will walk through the improvements and drawbacks of my new approach.

[![signal-2025-11-01-072607](https://forum.heatpunks.org/uploads/default/optimized/1X/577937dc058290aa74402de6e40e72e2b7538039_2_375x500.jpeg)signal-2025-11-01-0726071536×2048 279 KB](https://forum.heatpunks.org/uploads/default/original/1X/577937dc058290aa74402de6e40e72e2b7538039.jpeg)

[![signal-2025-11-02-060612](https://forum.heatpunks.org/uploads/default/optimized/1X/bfcac970eb8796e4e995215b5883cb0aec75dc13_2_375x500.jpeg)signal-2025-11-02-0606121536×2048 324 KB](https://forum.heatpunks.org/uploads/default/original/1X/bfcac970eb8796e4e995215b5883cb0aec75dc13.jpeg)

[![signal-2025-11-02-060600](https://forum.heatpunks.org/uploads/default/optimized/1X/b217e25623cf4865312fe022b3e2ead06d541f6b_2_375x500.jpeg)signal-2025-11-02-0606001536×2048 362 KB](https://forum.heatpunks.org/uploads/default/original/1X/b217e25623cf4865312fe022b3e2ead06d541f6b.jpeg)

The systems(3 installed) are all pretty basic on the hydronic end, they range from 1 to 3 zones.  None of them are using mixing valves and i’m targeting a fluid temp of ~103F on the glycol side.

The “boilers” are [Hashrate House](https://www.hashratehouse.com/) tanks with S19jpros eqipped with [Epic Control Boards](https://altairtech.io/product/epic-umc-universal-mining-control-board/).  I have made a custom 24v contactor box to turn the whole tank on and off(Bang Bang) from a simple wall thermostat input.

[![contactor](https://forum.heatpunks.org/uploads/default/optimized/1X/54d4fbf75a3e09335166117706a06bd37cb37de1_2_375x500.jpeg)contactor1536×2048 263 KB](https://forum.heatpunks.org/uploads/default/original/1X/54d4fbf75a3e09335166117706a06bd37cb37de1.jpeg)

So the order of operations is as follows:     Client turns up wall thermostat > thermostat signals Contactor to turn on > Tank+miners turn on and begin hashing > once desired oil temp is reached the control board starts scaling the miners > when the space is heated the thermostat signals the contactor and power is cut to Tank/miners.

Pros:

Simple

Reliable

System is completely off and using no power when not in use

Native modulation seems more reliable than HA/server type modulation

Cons:

Bang Bang may not be good for miners long term

Control Boards maintain boiler/temp within a ~7F range which would be too broad for certain applications.

Here is an example of the boiler temp(oil side) being modulated over the course of a night of heating

[![Screenshot 2025-11-01 at 7.11.26 AM](https://forum.heatpunks.org/uploads/default/optimized/1X/b6dcf1a8d54c73dff00e1360ee90ea5a85b25493_2_690x225.png)Screenshot 2025-11-01 at 7.11.26 AM2490×812 96.5 KB](https://forum.heatpunks.org/uploads/default/original/1X/b6dcf1a8d54c73dff00e1360ee90ea5a85b25493.png)

The small bumps indicate when the miners are throttling down.  Epic control boards are super fast to scale down and start hashing again.

Here is a chart of the miner scaling up just after being turned on.

[![Screenshot 2025-11-03 at 6.29.09 AM](https://forum.heatpunks.org/uploads/default/optimized/1X/8476f30a5fdb51ff4f774f4e113d23adec0fbef0_2_690x196.png)Screenshot 2025-11-03 at 6.29.09 AM2976×848 234 KB](https://forum.heatpunks.org/uploads/default/original/1X/8476f30a5fdb51ff4f774f4e113d23adec0fbef0.png)

The miner completes 4 up scales in the course of 12 minutes

Overall I’m very happy with this setup, I haven’t had any calls from clients and the systems seems to work very well so far.

Let me know what you guys think!

-------------------------

HashrateHouse | 2025-11-03 15:39:33 UTC | #2

Wonderful work you have done, and glad to hear you have some happy clients!

Have ran for a few years like this an haven’t seen any detrimental effects of the bang on and off this far, especially with the ePic boards scaling working so well in immersion as you pointed out.

I have a system designed specifically for heating hot tubs and it’s almost the same implementation with a slight tweak, I have ran the pump continuously so it keeps the oil at temp and the scaling up/down more consistent (oil already at temp) and when tank is located outside (less thermal barrier/insulation) it keeps the oil viscosity low enough (when warm) as well as don’t need to worry about cold starting the miner (using more power than required to just heat the chips initially aka killing j/th) with ecm pumps this is a pretty low power draw as well (40w or so)

Just another way to run the system, great work you have done And clean setups!
