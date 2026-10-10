# bitaxeorg/ESP-Miner issue #1379: Reduced hash rate and increased temperature v2.11.0

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1379
> Collected: 2026-10-07
> Published: 2025-11-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1379
- State: closed
- Author: rtslol
- Opened: 2025-11-23
- Closed: 2026-02-08
- Labels: question

## Description

I recently updated my Bitaxe Gamma 602 from the stock firmware that came with it from Solosatoshi (v2.5.1) to the latest version (v2.11.0)

Since updating I’ve noticed two things:

1. It consistently hashes at 1.05Th/s, whereas before it would generally hover around 1.15-1.2Th/s and spike anywhere up to 1.4Th/s.

2. It runs slightly warmer. The ASIC used to run at about 48 degrees consistently without modifying the fan speed settings. Now I find it runs at about 52 degrees at the default fan speed settings. It appears this is due to changes to the way the fan / heat curve works. I’ve had to manually increase the fan speed to 40% for it to maintain 49-50 degrees now. VRM is at 48 degrees with a rear 40mm Noctua fan on it, whereas before it was slightly less as well.

I made a post on Reddit (https://www.reddit.com/r/BitAxe/comments/1p3xwx2/latest_firmware_gamma_602/) regarding these issues and the very same issues have been confirmed by others as well.

What has changed in v2.11.0 (or even v2.10.0 as reported by someone in the Reddit thread) that is negatively impacting both the hash rate and temperature? It would be great if these issues are investigated and a fix deployed so I don't have to go through the effort to roll-back the firmware.

## Comments

### mutatrum on 2025-11-24

There are no direct change to the fan controller or temperature management between v2.10 and v2.11. However, there are several changes in the vicinity, maybe something changed there?

Do you know what the stock firmware was, as we did change the fan controller a way back, for example #947, but that's way back in v2.8, or going back further to #800 in v2.6.4.

I've also seen one report of a similar rise in temperature, but that got fixed by cleaning the fan and re-applying thermal paste. Not that I want to rule out that a change in software caused it, but how long have you had the device running, as it could be beneficial to occasionally (depending on environmental temperature and dust levels and such) either clean the fan and/or re-apply thermal paste.

### rtslol on 2025-11-24

> There are no direct change to the fan controller or temperature management between v2.10 and v2.11. However, there are several changes in the vicinity, maybe something changed there?
> 
> Do you know what the stock firmware was, as we did change the fan controller a way back, for example [#947](https://github.com/bitaxeorg/ESP-Miner/pull/947), but that's way back in v2.8, or going back further to [#800](https://github.com/bitaxeorg/ESP-Miner/pull/800) in v2.6.4.
> 
> I've also seen one report of a similar rise in temperature, but that got fixed by cleaning the fan and re-applying thermal paste. Not that I want to rule out that a change in software caused it, but how long have you had the device running, as it could be beneficial to occasionally (depending on environmental temperature and dust levels and such) either clean the fan and/or re-apply thermal paste.

The stock firmware which came with the Gamma 602 was v2.5.1.

I’ve had the device for approximately 4 weeks. It’s definitely clean and environmental temperature is about the same. Increasing the fan speed by 5% drops the temperature by about 2-3 degrees.

Other than the temperature, what is causing the reduced hash rate? That’s more of a concern.

### mutatrum on 2025-11-24

The way the hashrate is measured is a recent change, and should be spot on what the expected hashrate shows. The previous method of calculating the hashrate had a much larger variance, both above and below the expected hashrate. However, those spike were basically random noise, by lack of better measurements.

Example, this is a gamma running at stock 525 Mhz, 1150 mV (ignore the efficiency, that's broken in this build):
<img width="1910" height="1195" alt="Image" src="https://github.com/user-attachments/assets/2217c660-f8a4-4cb0-a1f2-afdc81075517" />

There's still some variance, but it's between 1.00 and 1.14Th/s, exactly around the expected hashrate of 1.071 T/hs. (The expected hashrate is a theoretical hashrate calculated on the selected frequency and the number and type of chips.) This build also has #1348 added, so you get some longer term averages, which all line up exactly to what the expected hashrate is. What could help is to let the device run for a bit (a few hours at least) and post a screenshot of the whole dashboard. That makes it easier to see if it's hashing fine or not.

With the previous hashrate registers, this fluctuated somewhere around 0.7 Th/s and 1.4 Th/s, but on average it was the same, but this was difficult to see due to that large variance. See also #1249 for more information.

As for the temperature, that's a bit more difficult. Large parts of the firmware have been completely rewritten between v2.5.1 and v2.11. I did scan through the release notes, but didn't see anything pop out immediately that would point at a change. 

Do you run the fan manually or automatic? Try to aim at 60 C, sub 50 C is quite cold and difficult to achieve on stock hardware, unless you are in a cold environment. Too cold is also not good, the ASIC is happiest around 60 C.

### rtslol on 2025-11-26

The hashrate behavior you described lines up exactly with what I’m seeing on my end. If the newer firmware is simply reporting hashrate more accurately and reducing the variance compared to older builds, then everything looks normal.

I’m running the fan on automatic. The minimum speed is set to 40%, with a temperature target of 55 °C. The Darkhorse heatsink keeps the ASIC itself running quite cool; it tends to sit well below the target. I also have a rear 40 mm fan aimed at the VRMs, which keeps them in the 45-48 °C range.
