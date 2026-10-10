# Mujina-Antminer

> Source: https://forum.256foundation.org/t/mujina-antminer/39
> Collected: 2026-10-07
> Published: 2026-05-11

skot | 2026-05-11 14:39:43 UTC | #1

Bitmain Antminer controlboards run linux and are perfectly capable of running Mujina firmware. Mujina on Antminers represents an incredible opportunity for increased performance, customization and of course freedom for these machines.

Initial proof-of-concept has been completed: Mujina running on a S19j Pro with a stock amlogic controlboard works.

So far, building Mujina and loading on Amlogic controlboards is a very manual process. This topic is for tracking progress.

-------------------------

ixtech.xyz | 2026-05-28 02:45:58 UTC | #2

I mean, it would be nice to support bitmain antminer and a key feature would be to have a PSU bypass so we don’t have to use loki kits or sort of the half-ass solution from some of the other third-party firmwares. Is the thought to just add support for Bitaxe Antminer miners on a per-case basis, or create a framework so you could add it if you wanted to support a particular miner?

-------------------------

ryan | 2026-05-29 16:12:29 UTC | #3

[quote="ixtech.xyz, post:2, topic:39"]
Is the thought to just add support for Bitaxe Antminer miners on a per-case basis, or create a framework so you could add it if you wanted to support a particular miner?

[/quote]

It’s both, really. Internally, we’re trying to build Mujina as a framework of modular components: ASIC chips, power supplies, fan controllers, temp sensors, and so on. Then we build particular miners out of those pieces. A “supported miner” is just a built-in recipe for how one system composes them together.

The goal is that supporting a new miner is something you can do mostly by describing how it wires the existing pieces together. And when a piece is missing, you add it: a new ASIC gets a chip driver, a new PSU or fan controller gets a peripheral driver, and it all slots into the same framework for the next person to reuse.

-------------------------

AgentP | 2026-05-30 02:45:08 UTC | #4

Mujina is working on my S19XP with amlogic control board (LuxOS preinstalled).

Remaining issues:

UART is stuck at 115200, advancing this to 3M caused us to loose contact with the chips.  Not sure why, but it’s hashing happily at 110MHz.
This relied on LuxOS to handle the secure boot exploit.  Eventually it may be nice to not need LuxOS at all.  

Code is here:  https://github.com/keegreil/mujina

Let me know if/how you’d like this packaged up into a PR.  Cheers!

* AgentP

-------------------------

AgentP | 2026-06-17 12:39:56 UTC | #5

Has anyone cracked the code on getting Mujina to persist on the Amlogic board across power cycles?

So far I’ve just been hot loading it, but I’d like the install to be a little more permanant for some undervolt testing I’m doing.

-------------------------

skot | 2026-06-17 13:34:55 UTC | #6

Yes, you need to make the filesystem writeable. Stock Bitmain firmware is not. The easiest way to do this is install LuxOS or Braiins. I have been working on doing this from scratch with the Mujina-loader (https://github.com/skot/mujina-loader/). It works, but needs some cleanup to be a quick tool.

Also the deamonc exploit that LuxOS (and I assume Braiins) use to get root access on stock Bitmain firmware was blocked with a firmware update sometime mid-2025. Also very recent LuxOS turned off root access.

If you have a controlboard with recent stock firmware installed you’ll need to use the “usb burn” method to take it back to early-2025 stock firmware. I haven’t been able to get a Mujina image with a writeable filesystem working with usb burn yet…

-------------------------

AgentP | 2026-06-17 13:51:07 UTC | #7

Thanks!  Yeah right after I posted I got working, on my older LuxOS board.  Currently running an 19XP board at 10.9V…um.. for science

-------------------------
