# What is the best miner for bedroom heat?

> Source: https://forum.heatpunks.org/t/what-is-the-best-miner-for-bedroom-heat/216
> Collected: 2026-10-10
> Published: 2025-11-14
> Registry ID: heatpunks-forum

Cody | 2025-11-14 15:56:23 UTC | #1

I am wrapping up a mega remodel of an amazing hashrate heated house in Wyoming(for sale soon!!) and have two bedrooms that need heat.  If i wasn’t a heatpunk i would just buy resistance cove heaters and be done with it but…..The rest of the house hashes, so these bedrooms should too.

My initial thoughts are the Cannan Mini 3 or the HeatBit Maxi.

Are there other small options “commercially” availible?

Does anyone sell single board slim S19’s?

-------------------------

tronsington | 2025-11-14 16:07:48 UTC | #2

Food for thought:
[![image](https://forum.heatpunks.org/uploads/default/optimized/1X/a3bd9f1ef5dcec19136ac7d5feb29f302c40d592_2_375x375.png)image1080×1080 119 KB](https://forum.heatpunks.org/uploads/default/original/1X/a3bd9f1ef5dcec19136ac7d5feb29f302c40d592.png)

This would put the Maxi at about 38.43 $/TH, but it also produces more heat than a Mini 3 (1200W vs 850W). Mini 3 can be incorporated via API into other systems while the Heatbit machines cannot.

Altair sells Bitchimneys (single boards) and Urlachers (120V versions of S19 models).

-------------------------

Cody | 2025-11-14 17:33:26 UTC | #3

Thanks, this helps a lot.  @Rowdy mentioned these [S19kpro Slims](https://plebsource.com/products/s19k-pro-slim) that would probably be great but are out of stock :(.

One thing that drives me crazy about ALL of these models is the noise!  Even HeatBit is 45db.  When I used to heat my house with an s9 rocket miner i was always shooting for <30db.  45db is pretty noisy.  Maybe this is where the Cryobyte single board machines could shine?

-------------------------

tronsington | 2025-11-14 20:05:29 UTC | #4

I have two Mini 3s running at my house and they’re very quiet, even in Super mode. In Eco mode, you can hardly tell they’re running. I get the occasional rattle noise when in Mining/Super mode when the fan ramps up. Wife approved!

-------------------------

Rowdy | 2025-11-15 00:32:06 UTC | #5

The mini 3 would be my first choice. I’d rather build though. I’ve built 5 heaters for the price of the mini 3 and I have spare parts :grin:. The mini 3 seems like the best option, for purchasing a heater. They are really nice.

-------------------------

thak777 | 2025-11-18 18:45:59 UTC | #6

It’s important to note that the Bitchimney also comes in a 19k variant, which is a much better deal.

Assuming “Normal” mode–like in the graphic above based on the S21 variant…
$850 for 31TH @ 750W ($27.41/TH - 24J/TH)

Also, getting a 19k board down to 22J/TH with LuxOS is quite doable.

-------------------------

Cody | 2025-11-18 19:51:31 UTC | #7

My concern with the BitChimney is the noise.  49db is pretty high.  I don’t think I’ve seen one running.  Do you have one?

-------------------------

thak777 | 2025-11-18 20:51:21 UTC | #8

We’d already printed a bunch of single-board units, but bought a BitChimney to test out last winter.

When my boss saw it, she immediately decided she wanted it at home. She wants as much hashrate as possible; her husband wants it quiet. The compromise: she turns it up when they’re not home and then turns it down when they get home after work and he wants to watch TV. (Towards the end of the winter, I think she ended up moving it to another room further away so she could run it at the higher speeds all the time.)

As long as you’re running in a “recommended” state, it’s not too bad, but it’s certainly louder than the Avalon machines by default.

I have not tried running them with noise-optimized aftermarket fans: I would imagine that would improve the noise signature (perhaps significantly).

-------------------------

Atreyu | 2025-11-19 04:35:04 UTC | #9

Been using the mini 3s and they’re basically inaudible when using night mode and silent mode while producing some solid heat.

-------------------------

Atreyu | 2025-11-19 04:35:39 UTC | #10

How did the end result come out for you with api config?
