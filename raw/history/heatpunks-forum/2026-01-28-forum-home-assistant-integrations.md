# Home Assistant Integrations

> Source: https://forum.heatpunks.org/t/home-assistant-integrations/244
> Collected: 2026-10-10
> Published: 2026-01-28
> Registry ID: heatpunks-forum

tronsington | 2026-01-28 00:07:29 UTC | #1

@Exergy has developed a few Home Assistant integrations for controlling and monitoring a few different miner models as well as monitoring different pools. Available on GitHub and easy to import into HACS. Instructions can be found in the respective READMEs or on [docs.exergyheat.com](http://docs.exergyheat.com)

Miners:
[Canaan Avalon Home](https://github.com/exergyheat/ha-integration-canaan-avalon-home)
[Bitaxe](https://github.com/exergyheat/ha-integration-bitaxe)
[Stealthminer](https://github.com/exergyheat/ha-integration-stealthminer)
[Whatsminer (Old Firmware)](https://github.com/exergyheat/ha-integration-whatsminer-OLD)

Pools:
[OCEAN](https://github.com/exergyheat/ha-integration-ocean-pool)
[DATUM](https://github.com/exergyheat/ha-integration-datum-gateway)
[Public Pool](https://github.com/exergyheat/ha-integration-public-pool)

Solar Inverter:
[AP Systems](https://github.com/exergyheat/ha-integration-ap-systems)

Please let me know if you have any feedback, good or bad.

-------------------------

HeatJack | 2026-02-02 21:29:44 UTC | #2

@tronsington & @tylerkstevens

Thanks for creating this HA integration! I’ve been using it and plan on posting what I’m currently doing with the entities and sensors that show up in Home Assistant thanks to your HA project. Here’s the latest dashboard I created with it last week:

[![HA Miner Stats](https://forum.heatpunks.org/uploads/default/original/1X/6fa4096966326979fb8f0b686a96d54a130d6e2a.png)HA Miner Stats750×309 33.7 KB](https://forum.heatpunks.org/uploads/default/original/1X/6fa4096966326979fb8f0b686a96d54a130d6e2a.png)

It displays my office room stats and my Loki rig’s real‑time data, using both the smart plug’s power readings and the BTC network. When I put all of that together, I can see the “heating rebate” I’m effectively getting at any given moment.

Some Feedback & Request:

During setup, it will prompt you for the miner’s IP address and port. I initially entered my miner’s IP with port 4028, but kept running into errors. Leaving the port at the default 8080 solved the issue immediately.

Fan control, is there was a way to implement LuxOS API fan settings? It would be nice to control the fans when they’re in auto made. Here’s some info from the LUXOS API guide: [https://docs.luxor.tech/firmware/api/luxminer/fanset](https://docs.luxor.tech/firmware/api/luxminer/fanset) - The end goal being able to make those API calls using HA to control the fans and set a range so they don’t fluctuate so rapidly in automatic mode.

-HeatJack

-------------------------

tronsington | 2026-02-02 21:45:16 UTC | #3

> **HeatJack:**
>
> > During setup, it will prompt you for the miner’s IP address and port. I initially entered my miner’s IP with port 4028, but kept running into errors. Leaving the port at the default 8080 solved the issue immediately.

Just out of curiosity, why did you try changing it to 4028?

> **HeatJack:**
>
> > Fan control, is there was a way to implement LuxOS API fan settings? It would be nice to control the fans when they’re in auto made. Here’s some info from the LUXOS API guide: [fanset](https://docs.luxor.tech/firmware/api/luxminer/fanset) - The end goal being able to make those API calls using HA to control the fans and set a range so they don’t fluctuate so rapidly in automatic mode.

For sure. Shouldn’t be too difficult to implement. I’ll add it to the list.

Thanks for the feedback!

-------------------------

HeatJack | 2026-02-02 22:01:59 UTC | #4

> Just out of curiosity, why did you try changing it to 4028?

I was following the Configuration steps from [Github](https://github.com/exergyheat/ha-integration-stealthminer?tab=readme-ov-file#configuration):

Go to Settings > Devices & Services
Click + Add Integration
Search for “Stealthminer”
Enter your miner’s IP address and port (default: 4028)
Click Submit

HA device setup:

[![SM_HA_Device](https://forum.heatpunks.org/uploads/default/original/1X/7ec09d4927322d74030e49cd32f87346474fe83c.png)SM_HA_Device481×416 8.82 KB](https://forum.heatpunks.org/uploads/default/original/1X/7ec09d4927322d74030e49cd32f87346474fe83c.png)

TLDR; The readme says to enter the miner’s IP and port (default 4028), so I thought that meant the integration needed that port and changed it. I’m still pretty new to Home Assistant :slight_smile:

-------------------------

tronsington | 2026-02-02 22:13:06 UTC | #5

nope, that’s on me haha. I’ll get the docs cleaned up.
