# Heat Core HS05 - Combined Boiler + Dry Cooler Unit (M64 Based)

> Source: https://forum.heatpunks.org/t/heat-core-hs05-combined-boiler-dry-cooler-unit-m64-based/160
> Collected: 2026-10-10
> Published: 2025-08-11
> Registry ID: heatpunks-forum

tylerkstevens | 2025-08-11 22:18:29 UTC | #1

The [Exergy](https://exergyheat.com) team has started testing the HS05 residential heating unit we received from the Heat Core team at Bitcoin Las Vegas back in May. We’ll compile thoughts and information here.

[![IMG_0985](https://forum.heatpunks.org/uploads/default/optimized/1X/506d99fe8b18a51961fa19627d8d1c8e72a9b600_2_375x500.jpeg)IMG_09851920×2560 522 KB](https://forum.heatpunks.org/uploads/default/original/1X/506d99fe8b18a51961fa19627d8d1c8e72a9b600.jpeg)

**Info**:
Manufacturer - Heat Core
Model No - HS05
Miner Compatibility - M64
Power - Single Phase. 30A, 220V

**General Breakdown**:
It’s a pretty cool device. I like the simplicity. Here’s my best attempt at a simple description. Think of the HS05 as a boiler with an M64 inside of it. But instead of fancy logic to control the miner on and off or dynamically ramp up the power or change modes as a method of tweaking heat output - the HS05 just bleeds off any excess heat that the hydronic loop can’t take.

The heat flow process is as follows:
Electricity → Miner → Hot water leaves miner → hot water tries to heat up whatever flows through included heat exchanger. → if no heat is pulled away from miner in HX, then hot water is all bled out into the air via an included dry cooler.

The dry cooler is pretty quiet. I’m impressed. It dynamically ramps up and down to maintain the desired water inlet temperature to the M64 miner.

That’s another thing I like. The system is extremely simple. The only setting that needs to be configured at startup is the desired water return temp to the miner. The system then tries to send the heat to the HX, and if any is left, it’s bled in the dry cooler so the return temp to the miner is what you requested.

Essentially, if you don’t connect anything to the heat exchanger, the HS05 is essentially an HVAC furnace for air heating, based around a hydro miner.

Let me know if you have any questions. Happy to share more detail.

[![IMG_0987](https://forum.heatpunks.org/uploads/default/optimized/1X/e6098e463687e4fd22af3eb7651b9831f2bf20bf_2_375x500.jpeg)IMG_09871920×2560 511 KB](https://forum.heatpunks.org/uploads/default/original/1X/e6098e463687e4fd22af3eb7651b9831f2bf20bf.jpeg)
[![IMG_0988](https://forum.heatpunks.org/uploads/default/optimized/1X/6b10cb66c92925f8193ea4ad5e1460c3235b4d24_2_375x500.jpeg)IMG_09881920×2560 388 KB](https://forum.heatpunks.org/uploads/default/original/1X/6b10cb66c92925f8193ea4ad5e1460c3235b4d24.jpeg)
[![camphoto_1932422408](https://forum.heatpunks.org/uploads/default/optimized/1X/d6d3e29e6f8232eee93543d3159bd62e6fc35157_2_375x500.jpeg)camphoto_19324224081920×2560 261 KB](https://forum.heatpunks.org/uploads/default/original/1X/d6d3e29e6f8232eee93543d3159bd62e6fc35157.jpeg)

-------------------------

ActualLocke | 2025-08-13 01:34:37 UTC | #2

Super cool. Are you able to detach the dry cooler and put it outside while keeping everything else inside?

-------------------------

tylerkstevens | 2025-08-13 01:36:30 UTC | #3

Yep! Comes with extension tubes. 50 feet. Really slick simple design. Doesn’t come with an extension cable for the Dry Cool fan power though. I think we’ll splice them and make a longer cable.

-------------------------

Atreyu | 2025-08-18 03:31:03 UTC | #4

If I were to consider this for a residential unit - what’s the added monthly electric cost / power consumption?

Does Heat Core have support in the case of issues?

This seems like a great solution and easier setup for professionals that are traditionally trained in HVAC & plumbing? Is that the case?

-------------------------

tylerkstevens | 2025-08-18 17:14:01 UTC | #5

Hey. Good questions. Electric cost would go up. Heating fuel cost would go down. If you want a full breakdown of the economics and if you’re a good fit - check out [exergyheat.com](https://exergyheat.com)

We have some tools to size and estimate savings / roi.

Heat Core has support I think, but we haven’t had an issue with ours yet to test that out.

It’s most certainly a nice solution to replace a traditional boiler if sized correctly. We had our plumber involved with our install and they were curious and got the hang of it.

-------------------------

tylerkstevens | 2025-08-21 14:46:08 UTC | #6

Here’s a [link](https://x.com/tylerkstevens/status/1958282054686158971) to a video walkthrough of our first time using the Heat Core inside our radiant flooring loop at The Space.

System seems to work great. Dry cooler has never activated - meaning all the heat is being taken by the building floors.

-------------------------

Natio21 | 2025-08-30 09:03:53 UTC | #7

Thanks for the feedback. I have a question:

At any point, does the control system change any parameters inside the miner, or does the miner operate in a “static mode” unless the user manually adjusts something?

-------------------------

tylerkstevens | 2025-08-31 01:03:53 UTC | #8

The Heat Core does not change any mining parameters. We are adding a second layer of control using the API variables to step up and down the “high med low” power modes, and a third control layer with a smart PDU to shut the miner off completely.

This can be done with a raspberry pi + home assistant and a 220 V wifi PDU

-------------------------

kenb | 2025-09-07 19:46:33 UTC | #9

Hi

So I am very interested in if these systems are reliable enough to handle a Canadian winter. I would like to replace my oil boiler that runs my floor heating and indirect fired water heater with a system like this.

I have a friend who warned against it saying water cooled miners are problematic.

-------------------------

Atreyu | 2025-09-15 07:52:36 UTC | #10

Would you be able to share the user manual by chance? Want to review it with my HVAC team

-------------------------

Satoshi | 2025-09-15 08:50:47 UTC | #11

sadly there is no manual for it.
just API Documentation.

that’s why it’s sadly necessary to pilot test it yourself

-------------------------

tylerkstevens | 2025-09-15 13:41:01 UTC | #12

I think water cooled miners are more resilient than air and immersion cooled. Closed loops.

-------------------------

tylerkstevens | 2025-09-15 13:42:29 UTC | #13

We at Exergy have the spec sheet and install guide from Heat Core. Working on improving the documentation on our own forum page for the products and services we recommend.

Let me know if you have any specific questions about the product!

[Exergy Support – 5 Sep 25](https://support.exergyheat.com/t/heat-core-hs05-x-whatsminer-m64-setup-guide/32/1)

### [Heat Core HS05 x Whatsminer M64 Setup Guide](https://support.exergyheat.com/t/heat-core-hs05-x-whatsminer-m64-setup-guide/32/1)

Guides & How-To

Product Guides

Setup Guide for the Heat Core HS05 Boiler / Air Heating hybrid unit:  Please familiarize yourself with the manufacturer’s documentation before proceeding.        HS05 + M64 Home Bitcoin Mining Heater Setup Guide Introduction The Heat Core HS05...

-------------------------

Satoshi | 2025-09-15 14:11:59 UTC | #14

yes water and also immersion is much better than air cooled.

we have serval old s19 models which are running without any problems in immersion because it cools the whole machine perfectly

-------------------------

Atreyu | 2025-09-16 18:49:36 UTC | #15

In discussions with an hvac partner and after reviewing the spec, we wanted to get a user manual would be really helpful to get a clear gauge of implementation. Even schematics would be helpful.

When in discussions with Heat Core team, I did get their spec sheet as mentioned, but, they mentioned theyll only share the user manual once order is placed which I find odd.

That Setup Guide you guys have is super helpful from the looks of it and see the installation guide from Heat Core too. Thank you!

-------------------------

tylerkstevens | 2025-09-17 18:21:24 UTC | #16

Awesome. Keep us in the loop with the HVAC integration! I think the HS05 would work great for that. We haven’t tried it yet. Working on thermostatic control integration.
