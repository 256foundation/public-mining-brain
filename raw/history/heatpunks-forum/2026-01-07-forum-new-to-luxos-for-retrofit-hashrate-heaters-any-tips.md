# New to LuxOS for retrofit hashrate heaters. Any tips?

> Source: https://forum.heatpunks.org/t/new-to-luxos-for-retrofit-hashrate-heaters-any-tips/240
> Collected: 2026-10-10
> Published: 2026-01-07
> Registry ID: heatpunks-forum

tylerkstevens | 2026-01-07 20:18:16 UTC | #1

Hey All,

@tronsington and I are new owners of a beautiful Stealth Miner from @Satstackingpleb

Looking for tips on optimizing heating power while balancing noise, the offset from chip temp in ATM to actual air exhaust temp, and efficiency tuning.

Long story short, we are total novices when it comes to LuxOS. We primarily have experience with Braiins OS and DPS, and even more so, have been focusing on the Canaan Avalon Home miners that don’t use aftermarket industrial firmware jailbreaks.

If you have any useful information when it comes to dialing in LuxOS for hashrate heating, please reply here! I think @Toine is a big user as well.

-------------------------

m0ntan1 | 2026-01-08 05:22:12 UTC | #2

The documentation is the best I have seen. I think SSP sets fan targets, I usually just mess around with the presets set the temp and let it tune until it hits a happy chip zone. Fan settings are going to let you move heat more efficiently.  The spaces I am heating are pretty small, so I don’t need to get crazy.

I am dumb as hell and haven’t been able to fry any hardware with Lux yet.

-------------------------

Satstackingpleb | 2026-01-08 15:32:22 UTC | #3

ATM is like DPS, except better because LuxOS doesn’t restart mining with every adjustment like BOS+ does. better fan algo for auto… and a little birdie told me we might get alternate PSU control in the fw in the next release so bolo for that. when that drops, loki kits as extra hardware are nullified by fw setting finally.

-------------------------

josh | 2026-01-08 15:39:36 UTC | #4

The best way I’ve found is to manually set the fan to the percent for your desired noise level and enable ATM. I typically bump Hot Temperature up to 68, and in ATM:

- Hot Temp Buffer: 5

- Max Profile: 420Mhz (usually the max I can do with APW3++. Higher if using APW12 and good fans).

- Startup Time: 5 minutes

- Post ramping time: 1 - 5 minutes depending on the situation

-------------------------

tylerkstevens | 2026-01-08 15:51:22 UTC | #5

Thank’s for all the replies. We’re building a home assistant integration for 120 V LuxOS miners, so this is super helpful.

-------------------------

HeatJack | 2026-02-06 17:22:05 UTC | #6

Here’s a helpful fan setting I found in LuxOS (Settings Tab > Advanced Settings - scroll down):

[![LuxOS_Power_Off_Speed](https://forum.heatpunks.org/uploads/default/optimized/1X/61d6099a248a196a0d64fc18ec00c88dd7d304ee_2_690x108.png)LuxOS_Power_Off_Speed1550×243 12.6 KB](https://forum.heatpunks.org/uploads/default/original/1X/61d6099a248a196a0d64fc18ec00c88dd7d304ee.png)

Adjusting this can help your miner cool down when it’s powering off or in sleep mode:

[`power_off_speed`](https://docs.luxor.tech/firmware/api/luxminer/fanset)`-`*Optional.* A `0-100` value that defines the fan speed when miner goes in power-off.

Make sure the power off speed is set to 50% (or higher?), the default setting of 20% could overheat the miner.

-------------------------

thak777 | 2026-02-16 19:51:15 UTC | #7

If you think that LuxOS is good for heaters now…just wait. David & co are *killing it* for forced air heater applications.
