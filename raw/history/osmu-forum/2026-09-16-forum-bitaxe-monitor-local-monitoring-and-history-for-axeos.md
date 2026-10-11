# Bitaxe Monitor – local monitoring and history for AxeOS

> Source: https://osmu.xyz/t/bitaxe-monitor-local-monitoring-and-history-for-axeos/98
> Collected: 2026-10-10
> Published: 2026-09-16
> Registry ID: osmu-forum

magicmikemirror | 2026-09-16 22:38:40 UTC | #1

Hi everyone,

I built a small open-source monitoring dashboard for Bitaxe/AxeOS miners after I wanted more persistent historical data than what I could get directly from my miner.

It polls the local AxeOS API and stores metrics locally, so hashrate, temperatures, power, voltage, shares, best difficulty and events remain available independently of the miner itself.

It runs in Docker and is packaged for ZimaOS, but the goal is to keep it lightweight and usable on any Docker host.

The project is privacy-first and does not require any cloud service.

I’d be very interested in feedback from other Bitaxe users, especially regarding additional AxeOS metrics or events that would be useful to monitor.

[github.com](https://github.com/MagicMikeMirror/bitaxe-monitor)

![image](https://osmu.xyz/uploads/default/optimized/1X/15ce8f1099f06d2b49bad9e680ffec7d6b72e090_2_690x344.png)

### [GitHub - MagicMikeMirror/bitaxe-monitor: Privacy-first local dashboard for Bitaxe and AxeOS...](https://github.com/MagicMikeMirror/bitaxe-monitor)

Privacy-first local dashboard for Bitaxe and AxeOS miners, packaged as a ZimaOS app.

thank you in advance
