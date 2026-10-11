# First Radiant System Design - Heating The Space in Denver - Any Feedback?

> Source: https://forum.heatpunks.org/t/first-radiant-system-design-heating-the-space-in-denver-any-feedback/141
> Collected: 2026-10-10
> Published: 2025-06-11
> Registry ID: heatpunks-forum

tylerkstevens | 2025-06-11 14:08:38 UTC | #1

Hey all,

I’m in progress of designing / installing the radiant flooring system for [The Space](https://denver.space) in Denver.

We’re going to test out a variety of hashrate heating boilers including @HashrateHouse immersion system, and the RY3T Mini and Heat Core HS05 that use a single M64.

Follow along with our testing on this thread: [https://heatpunks.org/t/ry3t-mini-heat-core-hs05-m64-based-boiler-testing/139/4](https://heatpunks.org/t/ry3t-mini-heat-core-hs05-m64-based-boiler-testing/139/4)

I’m curious if anyone on this forum would mind taking a look at my radiant system design. Is there anything obvious that I’m doing wrong here? Feedback appreciated. See image below.

[![signal-2025-05-15-223951_002](https://forum.heatpunks.org/uploads/default/optimized/1X/83f42450f7923f7cc9bec456268f1f6a5d6c431d_2_399x500.jpeg)signal-2025-05-15-223951_0021278×1600 127 KB](https://forum.heatpunks.org/uploads/default/original/1X/83f42450f7923f7cc9bec456268f1f6a5d6c431d.jpeg)

-------------------------

Jesse | 2025-06-14 18:05:54 UTC | #2

What diameter pex are you thinking about for the loops? The Space has a lot of floor surface area, you probably want to do more smaller diameter loops so that you are evenly heating vs having hot and cold spots.

-------------------------

tylerkstevens | 2025-06-14 18:20:46 UTC | #3

1/2 in PEX.

-------------------------

Jesse | 2025-06-14 20:16:28 UTC | #4

Careful with that floor, you don’t want problems with expansion or buckling. Anything over 80F at the floor is usually too hot for most types of flooring.

I think you might want more loops so that you can run at cooler temp. Pex and manifolds are cheap.

Double check my math, I might not be understanding the specs of the ry3t but I assume you want to run it at full throttle 24/7 basically the whole winter and then rely on on the existing heat system to supplement?

-------------------------

tylerkstevens | 2025-06-15 18:31:59 UTC | #5

Good call out. Shouldn’t we be able to modulate the floor temp with the mixing valve though? Balancing how much of the water goes back into the miner for heating - and how much bypasses the heating?

-------------------------

Jesse | 2025-06-16 01:30:37 UTC | #6

You can rely on a mixing valve. But I’m nudging you in the direction of not relying on it unless the miner is for some reason not tolerant of a big temperature difference between the cold water coming in and the hot coming out. I don’t think that’s a problem?

Typically, mixing valve are either used for when you are trying to use one heat source to heat to different temperatures - say to get your domestic hot water to 130 and your floor to 80. But in this case, you don’t really care about that, you just want to make sure that your floor isn’t too hot.

Another time thermostatic valves are used is for gas fired cast iron boilers which are very intolerant of cold water entering the heat exchanger due to condensation which very quickly rusts out the furnace. In that case the valve is there to make sure that the temperature difference between incoming and outgoing is small enough that condensation doesn’t form.

If you increase the total length of PEX or increase the diameter of the tubes or increase the rate of flow with a bigger circulator pump or or add a bunch of staple up heat plates, you can get to a point where you never even use the mixing valve. Build a big enough radiator and you’ll shed heat fast enough that your flooring will never even have the chance to get too hot. You might still want to plumb a valve in as an insurance policy or for future upgrades/testing.

Coincidentally, I have an extra 1in thermostatic valve you can have and probably some extra heat PEX. I’ll dm you when remember where I put that stuff.
