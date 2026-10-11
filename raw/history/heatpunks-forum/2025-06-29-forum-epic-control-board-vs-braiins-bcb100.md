# Epic Control Board vs Braiins BCB100

> Source: https://forum.heatpunks.org/t/epic-control-board-vs-braiins-bcb100/148
> Collected: 2026-10-10
> Published: 2025-06-29
> Registry ID: heatpunks-forum

Cody | 2025-06-29 01:42:33 UTC | #1

I recently purchased an Epic control board from [altairtech.io](http://altairtech.io) and am very impressed!!  The speed at which it modulates the miner up and down according to chip temp is amazing.  For me this has single handedly obsoleted Home Assistant.  Next winter I will be running serverless, with power modulation all being done natively from the control board.

I am wondering if anyone has used the DPS on the BCB100 for up and down scaling?  I tried it briefly last year and I remember thinking it was slow to scale up.

The Epic board operates in a 10C temp window, which for my uses is acceptable.  When downscaling and upscaling the changes take less than 60 seconds.

Curious about thoughts on both of these boards

-------------------------

skot | 2025-06-29 18:55:07 UTC | #2

Is this changing the hash frequency or the fan speed? Or both? I assume this is on a Antminer?

-------------------------

Cody | 2025-06-30 00:41:26 UTC | #3

yeah this is on an S19jpro.  It is changing the frequency for sure, not sure about the fan speed as this miner is a hydro conversion(Cryobyte).  I’ll run it tomorrow and attach some pics of what I’m seeing.

-------------------------

josh | 2025-06-30 13:23:03 UTC | #4

Does it scale all the way to zero and then resume when temp allows? That would be a game changer for me.

-------------------------

skot | 2025-06-30 17:31:08 UTC | #5

I am very curious if they have made some advancements in how quickly they can change the hash frequency and ASIC core voltage. Last time I looked at this (over a year ago) LuxOS took several minutes to change the hash frequency. BraiinsOS did a full restart of the machine.

Being able to quickly change the hashrate, and the resulting miner power, would be huge for heat reuse and stranded energy mining.

-------------------------

Cody | 2025-07-01 00:57:53 UTC | #6

It would be worth a test, from what I’ve seen it is taking less than a minute, and the chart that shows hashrate doesn’t plummet to 0 like it does on Lux or Braiins.  And i agree, having this time reduced is super helpful.  For me helps reduce the overcorrection pendulum that can happen when hashboards shut down for too long between events.

-------------------------

Cody | 2025-07-01 00:59:37 UTC | #7

It will scale down as low as you want to go I think, I don’t think its smart to go all the way to 0(very inefficient past a point).  But if your situation demands it, I think the board will do it.

-------------------------

thak777 | 2025-07-04 19:24:58 UTC | #8

I’ll second the endorsement on the ePIC boards. I’ve been extremely impressed with them. LuxOS is a reasonably close second, but, as Cody said, seems to be slower to adjust.

-------------------------

power2bit | 2025-07-07 07:24:03 UTC | #9

> **Cody:**
>
> > am wondering if anyone has used the DPS on the BCB100 for up and down scaling? I tried it briefly last year and I remember thinking it was slow to scale up

Yes using it all the time. It has recently gotten more aggressive with DPS boost mode on newer releases.
