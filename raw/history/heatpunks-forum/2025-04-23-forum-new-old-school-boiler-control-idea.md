# New/Old School Boiler Control Idea

> Source: https://forum.heatpunks.org/t/new-old-school-boiler-control-idea/55
> Collected: 2026-10-10
> Published: 2025-04-23
> Registry ID: heatpunks-forum

Cody | 2025-04-23 14:20:16 UTC | #1

I have run my HashrateHouse “boiler” for two winters now using Home Assistant for what has been precise, but somewhat unreliable control of my miners.

I am considering moving to a system that doesn’t require running a separate server(HA) and also doesn’t require any external temp probe.

My plan is to simply bang bang the whole boiler in and off with a 50A contactor signaled from a regular 24v thermostat.

But to reduce the bang bang frequency I will have the miners scale down using native firmware like DPS or ATM(Luxor) this also increases efficiency as the miners scale down.

Instead of using any kind of external temp probes I will just use the miner’s onboard temp sensors.

Maintaining boiler temp can simply be done by playing with the chip temp/Boiler temp relationship and adjusting the scaling thresholds accordingly.

This does have major limitations in regard to other applications, but hydronic applications imo can have a wider operating temp range and also don’t kick on and off as much as other heating systems.  So I think this is a balanced control trade off that should be much more reliable than Home Assistant managed boilers.

Let me know what you think.

-------------------------

tylerkstevens | 2025-04-23 14:39:39 UTC | #2

I’m interested to hear how this goes. So if I understand correctly - the miner power scaling (DPS or ATM) will reduce the wattage as a control method **before** cycling the power off entirely?

Because you’re right - the temp tuning firmware features can only go down so low in % of max power.

But what about when you cycle them back on wit h the contractor? Will they turn on at 100%? Or turn on at a lower power level and then use temp tuning (DPS or ATM) to step back up in power?

I’m curious if this only works for ramping down gracefully.

-------------------------

josh | 2025-04-23 15:33:58 UTC | #3

I like this idea a lot.

In my experience with Luxor, it will ramp up gradually upon boot from the lowest setting and up to its most recently set value, regardless of whether you’re using ATM. When using ATM, after n minutes post boot (depending on your settings), ATM takes over and will scale up and down based on the range you set and your temps.

So if you can deal with the ramp up delay (a few minutes) then I think this would be a good solution since you have a decent “buffer” of heat in the fluids before things get too hot/cold.

Really interested to see if this works as it would let me delete the dry cooler from my own setup when i don’t need a shop heater in the summer…

-------------------------

Cody | 2025-04-23 18:42:44 UTC | #4

Sounds like at least with LuxOS it will boot into the last used setting (thanks @josh ). I would prefer it boot into the either a default (~3125w) or into the highest setting I want(~3700w).

But the beauty of Hydronic systems is that the n minutes delay really isn’t that big of a deal.  They are slow response systems in general so a few minutes wouldn’t even be noticeable.

I know Braiins DPS resets to the “default” wattage after a hard restart.  At least thats how it used to work.

-------------------------

SoftwarmLLC | 2025-04-23 23:44:39 UTC | #5

What is the design of your “boiler”?

-------------------------

Cody | 2025-04-23 23:49:01 UTC | #6

Its a HashRate House immersion tank with 2 S19Jpros and a 4x12 40 plate heat exchanger.  Currently running fully automated ramp up/down with Home Assistant.

-------------------------

SoftwarmLLC | 2025-04-24 00:07:04 UTC | #7

As I recall you don’t want to run it 24/7 right? Only on demand? The HX goes to a hydronic system for heat? Whats your trigger for the on/off bang bang? Outside temp?

I think you are on the right track with your plan. The DPS settings are really effective and the machines respond well to changes in thermal suck if you set them correctly.

-------------------------

Cody | 2025-04-24 01:58:48 UTC | #8

Yeah, exactly, the trigger will be 24V wall thermostats>Contactor.

-------------------------

Elmeri-BTCBoiler | 2025-04-24 06:30:51 UTC | #9

I have worked with immersion heating systems for 2 years now with my company. A normal temperature controlled relay works very well with immersion systems as long as the oil / chip temp doesn’t go too low so that the basic firmware temperature problem doesn’t kick in.

Im switching to hydro system now in the future for more easier install etc and better hashrate and output temps. Is there anyone who has tried to control hydro systems power in take according to water temp?This is my next step in my project for our BTC Boiler.

Ps what do you think about this ? :slight_smile:

[![image](https://forum.heatpunks.org/uploads/default/optimized/1X/6b1e40d116435b3e7bac3871c4d6c24336096e9e_2_257x500.jpeg)image277×537 27 KB](https://forum.heatpunks.org/uploads/default/original/1X/6b1e40d116435b3e7bac3871c4d6c24336096e9e.jpeg)
[![image](https://forum.heatpunks.org/uploads/default/optimized/1X/f801de50f266812e4bdb0f67db3462f11898ca16_2_220x500.jpeg)image240×544 19.1 KB](https://forum.heatpunks.org/uploads/default/original/1X/f801de50f266812e4bdb0f67db3462f11898ca16.jpeg)

-------------------------

patrick-patel | 2025-04-24 20:20:38 UTC | #10

Personally, I think I’d just size it so you can tune them down and leave it. In my opinion the dynamic tuning just adds unnecessary complexity.

If the goal is reducing on off cycles, ie maximize miner run time - undersize/downclock, but this comes with the downside of slower reheat times. (Added bonus this lowers time to ROI)

I guess if you start them at a high output and then lower it, you get a quicker reheat, but your utilization will be somewhere in the middle. (Higher time to ROI and more on off cycles)

Every choice has tradeoffs, guess it just depends what your priority is.

-------------------------

Cody | 2025-04-25 00:53:53 UTC | #11

I think in a hydronic system lowering the wattage down permanently would make the initial heat up time take drastically longer.  I guess the analogy is like heating up a cold house.  Waiting 2 min to scale isn’t perfect, but without max power it could take 15-20min longer to get the hydronic system up to ideal temp.  Balancing complexity is a trick for sure

-------------------------

SoftwarmLLC | 2025-04-25 04:13:17 UTC | #12

Yeah but where is your thermostat located? If its inside, maybe put it on the coldest part of your house? You are talking about the bang bang switch, so you probably dont want it to exercise all of the time.

-------------------------

SoftwarmLLC | 2025-04-26 02:20:33 UTC | #13

Hey Cody, another thing that may work well is to just set the miner on super low and vent the house with a thermostatically controlled fan.

You are probably going to need heat most of the time anyway, with the exception of mid summer. This is one reason i only run evaporative coolers and not standard AC. It takes all the heat out pretty quick. You live in a pretty dry climate.

-------------------------

Cody | 2025-04-26 13:09:28 UTC | #14

nah, dumping heat isn’t an option with my electricity prices, and even if it was i want this to be scalable to people who don’t have cheap power.

-------------------------

HashrateHouse | 2025-05-07 02:36:56 UTC | #15

Cody I love where your head is at with this and definitely think it’s on the right track, I’m testing a new PDU style that will be able to manage the miners bang on/off via Temperature to help reduce complexity of the whole system…

I wonder if you had the 24vac thermostat control a mixing valve right before the HX? Then you would be able to target the exact delta your hydronic system would need and the miners would just ramp down when the oil was too hot in the small tank loop (but then when heat is needed the valve would suck more out of the tank in turn cooling the oil and letting the miners clock back up?) could then be a standalone immersion/or hydro integration…

-------------------------

HashrateHouse | 2025-05-07 14:35:54 UTC | #16

Also should note this is how I have been running my jacuzzi now for about a year and it works incredible, just hardwired the miner to the heater terminals (disconnected the electric heater completely) and so all the logic of the jacuzzi stays the same and when it calls for heat the miner and pump “bangs on” at its set wattage then scales down to a point until the jacuzzi turns off once it’s at temp…

The amazing smart heater part of this is that it adapts to load so when your just one person it’s uses less wattage for the same temp, but if the covers off and it’s full of people the temp still stays the same but the miner scales up to meet the demand…

This specific scenario is nice because it’s a 1:1 in places with high energy prices where a heat dump is not viable people wouldn’t see their energy use increase but they would be DCA’ing Sats

-------------------------

Cody | 2025-05-07 19:51:41 UTC | #17

Good to know that the “bang on” doesn’t seem to have catastrophic effects on reliability.

But when you say that the “miner scales up to meet demand” you mean it just runs for more time right?  You’re not modulating the wattage of the miner to “scale up”.

-------------------------

HashrateHouse | 2025-05-14 19:07:58 UTC | #18

No it modulates up if the intake oil temp and chip temps are stable (working through ePIC control boards autotuning) and conversely scales down when the miners are not being “cooled” enough from the jacuzzi… So right now its rests at around 70th while heating normal but if the cover is completely off and have 4 people in it, it will get up to 100th (then either scale down when the miner gets too hot or jacuzzi will “bang off” once the temps up, whichever comes first.) Usually ends up scaling back down though and finding that happy medium while in use

-------------------------

HashrateHouse | 2025-05-14 19:10:56 UTC | #19

also noting that with this tuning algo and an s19 i find i run my jacuzzi at a lower 102-103 as apposed to the 104 i use to run with the S9 because the S9 couldn’t keep up with the demand as well so would settle more in the 102 range while in use… where this new single miner tank and s19 works at keeping the temp higher and more consistent while in use so at 104 i bake out a little quicker :stuck_out_tongue:

-------------------------

Cody | 2025-05-15 12:03:33 UTC | #20

Are you using an external “inlet temp” sensor? Or just the onboard temps sensors in the miner?  I like the idea of bying an epic control board vs paying 2.8% ongoing to LuxOS.

-------------------------

SoftwarmLLC | 2025-06-16 20:26:42 UTC | #21

I like this. Nice job.

-------------------------

Atreyu | 2025-09-25 15:24:58 UTC | #22

End up implementing this approach? Any results?

-------------------------

BitcoinHeatEric | 2025-10-11 03:32:12 UTC | #23

Hoping to hear how implementing this has worked for you now that we’re entering cooler weather.

-------------------------

Cody | 2025-10-11 04:38:15 UTC | #24

I’ve got three systems that will be fired up very soon, using the contactor/Epic Control Board setup.  I’ll post here when i get some data on how it works.
