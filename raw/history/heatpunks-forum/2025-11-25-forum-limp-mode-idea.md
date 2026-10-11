# "Limp Mode" Idea

> Source: https://forum.heatpunks.org/t/limp-mode-idea/223
> Collected: 2026-10-10
> Published: 2025-11-25
> Registry ID: heatpunks-forum

Cody | 2025-11-25 01:13:55 UTC | #1

One minor problem with installing hashrate heating systems in non technical user’s homes is the issue of an internet outage.

At first glance this is solved pretty easily by using something like drain:// (braiins) to keep the miner hashing when the miner loses connection to the pool.  Epic UMC OS and Luxor have similar settings fyi.

But in the real world what happens if the rando person I installed a system for has a network switch die, or an ethernet cable come unplugged?  How long will it take to realize that the machines have been hashing(heating like normal) but producing no valid work/no sats?

My idea is simple.  In my systems I’m using two miners, so I plan to set only one to hash without internet.   This will put the boiler into a “Limp Mode” (50% capacity) in which it will still be able to heat the house to some extent, but not as good as normal. This should hopefully prompt the homeowner to realize something might be wrong.

This is a pretty unlikely edge case, but I do think it could go undetected for…….who knows how long lol.

-------------------------

tylerkstevens | 2025-12-06 00:13:58 UTC | #2

If you were using home assistant for the thermostatic control and hashrate monitoring you could set up some notification automations to send them a message? Or what if that notification was sent to you? Then you could reach out? I know you aren’t bullish on HA. It could even be a web scrape of their hashrate from their worker address that you monitor. We’re building something like that for Exergy. Then it’s our duty to keep the customer in the loop. Which makes the case for a small hashrate split IMO.

-------------------------

Cardiac | 2025-12-08 02:21:50 UTC | #3

Who in this scenario is the party liable for the sats? If you’re installing this as a service, do you not have visibility into hashrate of your installations?

Phrased differently, who’s the one who will notice the missing sats? Seems like that will dictate where in the system to build in monitoring.

-------------------------

Cody | 2025-12-12 00:08:53 UTC | #4

The homeowner in my situation is responsible for their sats.  One thing i could do is watch their ocean account if they want to share that info with me.  But as fortune would have it, i had a miner die in a clients boiler and they figured it out real fast lol.

-------------------------

Cardiac | 2025-12-12 12:20:21 UTC | #5

You could vibe code a web scraper for ocean that sends alerts out via various mechanisms.

-------------------------

Cody | 2025-12-16 01:13:28 UTC | #6

no I couldn’t lol

But that is a great idea and I can find someone capable of doing that.

I guess the only issue would be that in the spring and fall the machines would be turned off because of warm days and the scraper might be giving you false alarms.

I like where this is going though

-------------------------

Cardiac | 2025-12-16 01:47:17 UTC | #7

There are a lot of ideas around this. Hashrate is all a guessing game anyway. If you’re using a local proxy you can measure your own hashrate without the pool being connected.

-------------------------

SoftwarmLLC | 2026-01-03 05:12:21 UTC | #8

This is the main reason I like Braiins Pool for my customers -

- There is an app with an easy interface for them to understand, which shows current hashrate and revenue earned.

- The pool settings allow you to automatically split the production at a specified ratio.

- The pool sends an email if the hashrate dips below normal.

I suggested to Luke Dashjr that they make some type of function like this for Ocean, but he wasnt very receptive. I would use Ocean if I could get these same features.

-------------------------

Cardiac | 2026-01-04 12:40:55 UTC | #9

This site seems borked but Claude could probably fix it.

[https://telehashpirate.com](https://telehashpirate.com)

[github.com](https://github.com/EthnTuttle/ocean-srrrvey)

### [GitHub - EthnTuttle/ocean-srrrvey: 🏴‍☠️ Ocean Mining Pool Monitor & Nostr Reporter -...](https://github.com/EthnTuttle/ocean-srrrvey)

🏴‍☠️ Ocean Mining Pool Monitor & Nostr Reporter - Pirating the Ocean for Bitcoin mining data! 🌊⛏️

Grok analyzed this one:
The application, named “ocean-srrrvey,” is a Bitcoin mining pool monitoring tool that fetches and analyzes data from the Ocean.xyz mining pool API. It displays real-time mining statistics such as worker stats, hashrates, and pool information for a given Bitcoin address. Additionally, it performs temporal delta analysis to track changes over time, enables community comparisons with other users, and automatically reports findings to the Nostr decentralized social network using the #telehash-pirate hashtag.

Data flow in the application:

- The user enters a Bitcoin address via the web interface.

- The application queries the Ocean.xyz API (using a CORS proxy in production) to fetch associated mining data.

- The fetched data is processed to extract real-time statistics, including worker details, hashrates, and pool information.

- Temporal delta analysis is computed to identify changes in mining activity over time.

- Community comparison logic is applied to benchmark the user’s data against other addresses.

- Processed results, trends, and comparisons are displayed in the responsive UI dashboard.

- Survey findings are automatically published as events to the Nostr network, tagged with #telehash-pirate for community visibility.

-------------------------

SoftwarmLLC | 2026-07-02 17:54:36 UTC | #10

Thats pretty cool - I wish it was an app that grandma could download and operate.
