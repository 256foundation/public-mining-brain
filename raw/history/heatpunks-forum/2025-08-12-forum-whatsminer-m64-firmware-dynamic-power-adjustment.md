# Whatsminer M64 Firmware - Dynamic Power Adjustment?

> Source: https://forum.heatpunks.org/t/whatsminer-m64-firmware-dynamic-power-adjustment/161
> Collected: 2026-10-10
> Published: 2025-08-12
> Registry ID: heatpunks-forum

tylerkstevens | 2025-08-12 16:05:54 UTC | #1

Figured I’d finally start a forum thread to get to the bottom of this. We’ve all heard that the M64 (single phase power hydro miner) from MicroBT only has [High, Med, Low] power modes.

But the API has a variable to set a custom power limit. And I was told by the Heat Core (basically Whatsminer) team that dynamic power adjustments are possible.

Does anyone have actual experience with this? I haven’t been able to figure it out with our M64 test unit and HS05 boiler/dry cooler. See this topic → [Heat Core HS05 - Combined Boiler + Dry Cooler Unit (M64 Based)](https://heatpunks.org/t/heat-core-hs05-combined-boiler-dry-cooler-unit-m64-based/160)

It seems like the M64 is just missing this ONE FEATURE. 80C? Great. 220 V 30 A? Yes.

Ability to match mining power to heat demand? No?

-------------------------

Satoshi | 2025-09-08 10:04:13 UTC | #2

Hi Tyler,

you can adjust power (not really dynamic) over the whatsminer windows tool.

there is an option to lower the power limit by percentage. Like a own Power Modus beside Low/Normal/High. It needs some time to readjust and complete the upfreq. But currently not running stable mostly more power usage and less Terahash sadly.

So it will be necessary to tell the miner with custom code over the API what Profile or how much Power (and limit) to use for the current heat which is needed.

still playing with that.

cheers

Satoshi

-------------------------

tylerkstevens | 2025-09-08 14:41:13 UTC | #3

Can you post a screenshot of the whatsminer tool function where this is possible? I’m pretty confident our firmware / tool combo does not have this functionality. That’s what drives me crazy about these OEM miners. They don’t document anything.

-------------------------

Satoshi | 2025-09-15 08:46:45 UTC | #4

Yes same not much docs or informations.

Just use WhatsMiner Tool here you can see it

It’s Windows only

cheers

[![tool](https://forum.heatpunks.org/uploads/default/optimized/1X/a4d53a2c904c526978f46b4be853dc4fbd4590a8_2_690x391.jpeg)tool1920×1090 137 KB](https://forum.heatpunks.org/uploads/default/original/1X/a4d53a2c904c526978f46b4be853dc4fbd4590a8.jpeg)

-------------------------

tylerkstevens | 2025-09-15 13:40:19 UTC | #5

@tronsington can you help me understand here? We couldn’t seem to get power setting working.

Or is the actual problem that we need to be able to control it via an API command?

-------------------------

Satoshi | 2025-09-15 14:14:40 UTC | #6

no

this is the desktop windows software from whatsminer (whatsminer tool) you can control it while scanning the network through ip, find the ip from the M64 than use Remote Ctrl.

There are much more options than in the Dashboard. All these Ctrl can be also pushed trough the API but it’s not necessary with this software.

-------------------------

tylerkstevens | 2025-09-17 21:20:33 UTC | #7

our whatsminer tool doesn’t have the second row of setting options. wtf

-------------------------

Satoshi | 2025-09-23 16:12:26 UTC | #8

which software are you running?
there was an spring 25 update maybe your device was produced before.

we’re running on 20250403.17.REL from april 2025

you can check on WEB UI in Status –> Overview

cheers

-------------------------

Satoshi | 2025-12-18 11:24:09 UTC | #9

one more info: there is a setting to change the compact mode (close) to complete mode and get all settings.

-------------------------

Cardiac | 2025-12-31 13:35:28 UTC | #10

This references stock firmware, I assume. Do we know what aftermarket or open source firmware works with Whatsminer M64?

-------------------------

tylerkstevens | 2025-12-31 14:50:23 UTC | #11

None that I am aware of.

-------------------------

Satoshi | 2026-01-26 09:45:16 UTC | #12

always stock yes. till now there is no custom firmware as we know. it would also make not much difference since the stock firmware is already really good and stable.
