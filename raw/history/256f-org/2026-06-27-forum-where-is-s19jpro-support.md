# Where is s19jpro support?

> Source: https://forum.256foundation.org/t/where-is-s19jpro-support/62
> Collected: 2026-10-07
> Published: 2026-06-27

ixtech.xyz | 2026-06-27 21:12:41 UTC | #1

Hey,

I caught the osmu town hall comment that S19j Pro is supported, but I’m not seeing it in the repo and want to make sure I’m not looking at the wrong place.

In main the README still has the S19 series under “near-term targets,” not “working now.” mujina-miner/src/board/ only has bitaxe.rs, emberone00.rs, and cpu.rs — no S19 module. I can see the BM1362 work in asic/bm13xx/, but that looks like it’s feeding EmberOne00, not a stock S19 control board.

A few questions:

* Is there a branch, fork, or PR with the S19j Pro board driver that hasn’t merged yet?
* How is it being run — flashed onto the stock Zynq control board, swapped for a Libreboard, or something else?
* Is there an install image or build recipe somewhere I can try on my unit?

-------------------------

ryan | 2026-06-29 13:43:23 UTC | #2

Hey @ixtech.xyz ,

You’re correct. It’s not merged into the main repo yet. It’s coming soon; we’re working on cleaning that up and merging it right now. For the prototype version, start with [this other post](https://forum.256foundation.org/t/mujina-antminer/39) and  [discussion #51](https://github.com/256foundation/mujina/discussions/51#discussioncomment-16209394) in GitHub.

I’d regret not reminding everyone to keep a watchful eye on your miner as you experiment. We’re at a point where Mujina isn’t completely fail-safe in all cases on S19s, won’t necessarily detect and protect you from an insufficient power supply situation, etc. I’d definitely start with only one hashboard connected, for example.

It’ll be more production-worthy soon.

-------------------------
