# Power cable sizing for singleboard S19/S21/T21

> Source: https://forum.heatpunks.org/t/power-cable-sizing-for-singleboard-s19-s21-t21/219
> Collected: 2026-10-10
> Published: 2025-11-18
> Registry ID: heatpunks-forum

418Mining | 2025-11-18 15:52:00 UTC | #1

I’ve been using 6 gauge battery cables, doubled, to replace the power wires on the APW3++ to a singleboard Mine4Heat or Bitchimney hashboard. (So two black, two red.)

Based on my research that’s the “correct” size but based on what I’ve seen others do it may be overkill.

So my question is, what’s the best gauge wire for replacing the wire harness on the PSU? And more to the point, what evidence can anyone provide that the smaller gauge wires aren’t generating heat? Has anyone checked them with an IR camera?

I’m looking at possibly making some more of these to give to other people - I’m comfortable running this stuff at my house because I know how to keep an eye on it but I can’t exactly hand someone a hashrate heater if I’m not completely confident nothing I’ve done to modify it is unsafe.

But if I can, I’d rather not buy, cut, and terminate another load of 6 gauge cable, and it makes the thing look like a mad scientist’s project. Which I like aesthetically for my house, but…

-------------------------

Cody | 2025-11-18 20:09:47 UTC | #2

I don’t have any experience with these, but one additional problem is how much current you plan to actually run.  You could run it at 800w or at 1400w.  A single 8 gauge wire might be enough for 800 but nowhere near enough for 1400.

I think tailoring the wire to the expected wattage makes the most sense.  I usually have run air cooled miners “underclocked” to keep the noise down.  So if i was building one, I would probably target ~800w and use one 8gauge wire and a fuse to protect the wire in case someone tries to overclock.

TLDR:  Maybe these should have fuses because of the possibility of the user overclocking them?

I think this is the wrong size fuse for 8gauge, but you get the idea

[amazon.com](https://www.amazon.com/RENOGY-60A-ANL-Fuse-Holder/dp/B01M0P45C3)

### [Amazon.com: Renogy 60A ANL Fuse Set With ANL Fuse Holder : Automotive](https://www.amazon.com/RENOGY-60A-ANL-Fuse-Holder/dp/B01M0P45C3)

The Renogy ANL fuse will protect your controller, wire, and battery from overcurrent. This product is composed of alloy and brass copper and comes with a clear protective non-conductive resistant cover. This fuse set is ideal for custom installation.

**$12.99**

-------------------------

418Mining | 2025-11-18 20:31:01 UTC | #3

If I’m going to build something for someone else, and it’s either for-sure or even possibly never going to be touched by me again, I’m going to assume it will be operated as wrongly as possible.

I’m in IT. I’ve seen what end users do.

So because the APW3++ is capable of pumping out 1400w, the cabling needs to be able to support it. The miner will be preconfigured by me to run significantly south of that, but I want the cables to not convert the unit into a smoke machine if they decide they want to turn it up.

Realistically the upper limit of what a singleboard set-up can do *should* be short of 1400w, and if I mod the output to 14v we save some amps along the way, but when it comes to electrical fire I want a healthy margin of… health.

Fuses are a good idea - I’ll look for ways to include them. But if the cables can handle the max output of the PSU, I can rely on the fuse built into the PSU.
