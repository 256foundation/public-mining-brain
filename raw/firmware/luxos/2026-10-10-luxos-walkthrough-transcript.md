# LuxOS Firmware Full Demo: Install, Optimize, and Manage Your Bitcoin ASICs with Ease — auto-caption transcript

> Registry ID: luxos-video-demo
> Source: https://www.youtube.com/watch?v=ivHBlP3duRg (auto-caption track `en`, downloaded via yt-dlp 2026.08.19)
> Collected: 2026-10-10
> Published: 2025-07-24 (video upload date, YouTube microformat)
> Posture: extract (auto-caption transcript)
> As-Of: 2026-10-10

Provenance notes:

- Machine-generated YouTube auto-captions (ASR), single `en` track; not human-authored subtitles. Expect ASR errors in proper nouns, units, and numbers; numbers are kept exactly as the captions render them.
- One narrator throughout (a product walkthrough). Per the video's own description the presenter is "Trey, one of our Luxor Firmware Engineers"; no speaker labels are added to the transcript — refer to the voice as "the walkthrough".
- Converted from the raw `.vtt` (kept alongside as `luxos-walkthrough.en.vtt`): inline timing tags stripped, rolling-caption duplicate lines removed, re-paragraphed at sentence boundaries. `[mm:ss]` markers are cue start times, approximate.
- Video runtime 21:37 (1297 s), channel "Luxor Technology", ~1,000 views at collection.

---

[00:00:04] Hi, I'm Trey, one of the firmware deployment engineers. I typically help out with remote installations and occasionally do a few site visits. It's time for the Luxos demo everyone has been waiting for. First, let's talk about getting Lux OS onto your machine. You're going to download Commander. It's our installation and configuration tool. It'll look like this when you first download it. What you'll want to do is put in your network, which generally consists of either a range, single IP, or a cider subnet for the miners that you want to install.

[00:00:25] So, you hit configure networks. You'll see I already have a number here. Mine's already selected, but if you needed to select one, you would just select a network that you have added in. I'm going to deselect that because I already have my other network selected. And then you'll hit scan networks. It'll go out and it'll try to get every IP address in either the range or the cider or uh the single IP that you put in.

[00:00:48] It'll try to reach those miners and come back and give you some basic information on the minor available for install. You'll be able to select the minor and then a new button will show up here and it'll say install minor or install Lux OS. So you'll hit that install Lux OS and once complete you end up at a screen that looks like this. This will be what your minor looks like after Lux OS install.

[00:01:12] Now, obviously, mine's been up for a day or so, so yours will be ramping when you see it the first time, but you'll end up at a screen that looks very similar to this. On the dashboard, you pretty much get uh all of your basic information, hash rate, power consumption, estimated efficiency, uptime. Uh you do get a little graph here that shows you some temperatures and your hash rate over time, your fan output and various metrics here for different ways to uh look at your hash rate averages.

[00:01:45] So 24 hours, 15 minutes, and 1 minute. Some pool information and your tuner status. Note that this is not a button. This doesn't do anything. It is just there to let you know if the tuner is on or off. And then your pool status. Up at the top here, we have this little drop down menu in the corner. And here is where you can turn uh autotuner on or off.

[00:02:06] You can also do things like blink your LEDs, put the minor to sleep, reboot the minor, or restart the mining process. Down below that, you have your three hashboards. Uh each one of these shows you your voltage, your frequency, hash rates, chip health. We have three statuses for chip health. Uh healthy means that all chips are are reading and acting appropriately. Unknown typically means that the minor is in transit.

[00:02:35] So it is going from one profile to another or it's adjusting voltage or it's doing a health check. Something about the chips are in transition from one state to another. Uh and then unhealthy. Unhealthy means that we can read the chip but it is not hashing at a rate that we would expect or it's not accepting the new frequency. Um, but you can end up with chips in the unhealthy state while the miner is still hashing.

[00:03:04] And then you get your four temperatures, one or four for each hash board. Note that these probably do look cooler or lower than what you're used to seeing on Bitmain, but Bitmain gives you an estimated temperature at the chip level. We give you from this view a actual board level chip temp or board level temperature because we don't want to estimate the chip temperature. um we would just rather give you the data that we can actually verify.

[00:03:31] So down here you get the uh exhaust top and bottom and intake top and bottom. Same for each other hashboard. And then you get your basic pool information down here. We do have the ability to restart and shut down hashboards here. So if depending on your configuration, you'll be able to restart the hashboard or shut it down completely. Uh typically you'll use that for uh reboots of hashboards.

[00:03:59] It's unlikely that you'll very often at least shut down a hashboard. Uh but if you need to, the capability is there. So under preset profiles, what you get here is a drop down starting at zero or default uh of the different preset profiles that you can use with Lux OS. We pre-built out 16 underclock profiles and eight overclock profiles. You'll notice that each profile is effectively 25 MHz down or up.

[00:04:26] So from 590 to 565 or from 590 to 615, 25 MHz either way. And we have a uh predetermined voltage based on some internal algorithms as to where we'll start on that that particular frequency and profile before autotuner begins to uh adjust things. But out of the box, these are there for you to use. We typically recommend that people use things uh for testing purposes between minus 6 and plus two.

[00:04:59] That's a pretty good range to see a variety of profiles and efficiency ranges uh before you get into uh really low underclocks or really heavy overclocks. But you'll start at the the default profile. And uh that's where we're at right now, I believe. Check. Yep, default profile right now. Down below, you'll get a couple of different visual outputs. These are the health scores of the chips. Uh, higher number means healthier chips.

[00:05:27] Lower number means unhealthier chips. No number means either the the chips are, like I said before, transitioning from one thing to another. Maybe it's one profile or a different voltage. If the chip is unreadable, then it just won't show up here. It'll be grayed out. Uh, you see here the the little unknown color. You can also adjust uh this to see frequency or hash rate on miners that support chip temperature.

[00:05:57] You'll see another uh option here for chip temperature. No action to be taken here on this particular screen. This is help you just this just helps you figure out what your particular what a particular board is doing or a particular chip. You also get some indication as to the placement of the chip based on your air exhaust. So, if I'm looking at the hashboard uh with it laying down on a table in front of me, I know that the left side is my exhaust side and the right side is my air intake side.

[00:06:27] And I can tell a technician, hey, I saw a chip bottom corner of the exhaust side was not hashing appropriately or had gone into an unknown state. You get the same thing for the other two hash boards. But like I said, no action to take here. No buttons to click. Uh just this visual. And then you have the profile change options up above. One quick note on profiles.

[00:06:51] You can create custom profiles. I don't have any created right now, but to create one, you would just give it a name and then a voltage and frequency combo. One note on that though is that autotuner does not work on custom profiles because you've explicitly stated what frequency and voltage you want. And there may be a reason that you want that frequency and voltage. So we're not going to adjust it.

[00:07:17] Now we know about profiles. We know what profiles are. A combination of frequency and voltage. Now we can use profiles to help us manage things like temperature. And how we do that depends on thresholds and a few configuration settings. To start with, let's talk about the thresholds. target temperature. This temperature defines at what point, what threshold or what temperature the minor will kick the fans up to 100% and keep them there.

[00:07:48] Anything under this temperature, the minor's fans will modulate based on on what we think is needed. But at 45° in my configuration, the fans go to 100%. You can verify that here. My fans are at 100%. And my highest temperature is above 45. So, a board sensor has gone above 45 and my target temperature is 45. Therefore, fans kick to 100%. Hot temperature is when the minor will underclock one profile.

[00:08:22] So, if any board sensor hits 65°, the minor is going to underclock one profile and then wait for a minute or so and then re-evaluate temperature again. If the minor is still too warm, still at 65 on the hottest sensor, it may underclock again. So this is your threshold for underclocking. And then dangerous temperature. This is when the minor is going to shut down. Again, this is a board temperature.

[00:08:51] So what we're stating is that if a board sensor gets to 70°, that means that the chips are significantly hotter and likely getting close to 90 95°. So at 70, we're going to turn off by default. You can increase that to 75, but most of the time 70 works just fine. Now, knowing these three thresholds, when our fans go to 100%, when we underclock, and when we turn off, we can use one of the Luxos flagship features, feature called advanced thermal management, or ATM for short, to manage how we we operate with these thresholds.

[00:09:24] Effectively, ATM wants to underclock the minor when it gets too warm and then bring the minor back up to uh a predefined uh limit when the minor cools off. So, imagine during the day when temperatures are warm, your miners all underclock just enough in order to maintain temperature. And then at night when temperatures cool off, the miners come back up to their original hash rate levels and stay there until the day comes and they get warm again.

[00:09:56] Then we repeat the process. It's almost if you watch your fleet breathe as time goes on. Knowing that the way ATM functions is you end up with a window. You end up with a minimum profile that you're willing to accept the minor to run at and a maximum profile that you're willing to run at. The minimum profile states that this is as low as the minor will go to try to maintain temperature while still generating hash rate.

[00:10:20] We typically recommend you set that to no profile. The max profile is the opposite. Max profile said, "What's the highest profile you're willing to go to if the minor is underneath its cool range?" And in most cases, default is fine. You could very easily set this to an overclock. You could set this to plus two overclock. And if the minor is cool enough, it will get up into that plus two range.

[00:10:46] And one thing we want to avoid is the minor getting too warm, cooling off, dropping down one profile, and then one minute later when it checks again, oh, the minor's cooled off. let me go back up a profile and then come back up. That would create this bouncing effect and and you don't want that. We don't want uh a lot of changes on the minor if we can prevent it.

[00:11:05] So, we give you a buffer. Uh what this buffer says is that if the minor is within 5° of our underclock temperature, oops, our underclock temperature, do nothing. Don't underclock. Don't overclock. So, this is our safe buffer. This is when we feel that the minor is happy and safe at its current temperature. Don't do anything if you're within that buffer. So for me, anything between 59 and 64, the minor won't turn off if that's the highest reading on all of my board sensors, or excuse me, the minor won't underclock if that's the highest reading between all of my board sensors.

[00:11:41] You can change this to plus seven or excuse me, to 7, 8, uh, three. Depends on your goals. There's some performance characteristics depending on how you change this, but you can definitely change it and experiment within your fleet to see what gets you the best results. But we have the top or the high side, the max profile, the bottom or the low side, the min profile, and the buffer that keeps you from bouncing too much if you're at a place where the miner's warming up and cooling off quickly during profile changes.

[00:12:14] Startup time. This defines after boot. How soon do you want advanced thermal management to start evaluating temperature again? So after boot within one minute or right after the one minute mark the minor is going to start or ATM is going to start evaluating temperature. Same thing for post ramping time except this is after we've already done some type of change. It could have been a voltage change.

[00:12:38] It could have been a profile change. It could have been a frequency change. How soon after a change do you want ATM to come back in and reread uh the temperatures to make adjustments? Typically 1 minute is where you want it. But if you want less variation or less changes between profiles throughout the day, you could ex uh you can make this post ramping time bigger, say 5 minutes or 7 minutes, so the minor only gets checked every so often for temperature changes.

[00:13:02] Typically that works well when uptime is your goal and uh you know your miners are in a safe range from a temperature perspective but maybe slightly warmer um than than the the 5° window something like that. Down below we have immersion mode. If you turn this on it'll turn the fans off. Don't turn this on before you put the minor into immersion fluid. uh put the minor in into immersion fluid uh before you enable this because as soon as you enable this the fans turn off and we ignore them.

[00:13:36] Temperature is going to go way up if you're not in immersion fluid. Uh fans, you can set those to uh manual if you want to. Most of the time we recommend setting to automatic. But if you do set it to manual, you can come here and define a power or a speed. So right now my fans are running at 100%. So it's pre-populated at 100, but I could easily set it to manual and come in here and change this to 50 or 80, too.

[00:14:07] So yeah, fan speed pools pretty much what you expect here. Um, you put your pool information in. You could have multiple pools. Uh, you put in another pool and it'll fail over if it needs to. If if this pool were unreachable, it could fail over to a different pool. If you'd like to have a different worker name when it fails over, you could have a different worker name there.

[00:14:31] You can also split your hash rate depending upon quota or percentage. So if you wanted to split it, say you're in a hosting environment and you want to split some percentage of the hash rate, you could do that here between two different pools. You could also have three, four, five pools if you wanted more failover pools. And there's some characteristics that you can change to define how this will treat failovers.

[00:14:51] We can talk about that here in just a sec. But pools, that's what you got. On the log side, uh we try to do a good job of providing logs that are both valuable and readable. Um you'll see here my minor's been up for a little while. So I'm getting status logs, things like temperature, ASIC summaries, so my my board summaries, what's my frequencies, what's my my hash rates over various periods of time.

[00:15:21] But you can filter this out for info, warning, or error. You can export your logs. You can see logs from the past. So I can go back previous times and see or download my logs as needed. And I can also increase my logging level, which we we'll see here in just a second. One thing with our logs, we do have in our documentation section here, you can see docs.luxor.te.

[00:15:51] You'd see we have a knowledge base and in this knowledge base we try to match up log entries with explanations. So we have a bunch of different event codes which you can see and some explanations on those. We also have things like this. When you have an error you can come here and find problem and solution. And there's a few different ones right under settings. Most of these are uh going to be pulled from Bitmain.

[00:16:16] So things like your network configuration that's pulled from Bitmain as well as your pool configuration and such. That way the minor looks just like it did before after the Luxos install. Firmware updates are straightforward as clicking this button and then having cup of coffee and coming back. 5 10 minutes the update downloads, installs, minor comes back up and starts hashing. Same pool, same IP address. You can turn automatic updates on.

[00:16:42] That's up to you. Typically on a large fleet, we don't recommend it. On a small fleet, shouldn't be a problem. Then on advanced settings, here's where you can change your logging level. This is one of the few places where if you change it, it requires a restart of the Lux Minor to take effect. So up here, you just restart Lux Minor in order for that to take effect.

[00:17:07] This section defines uh how we treat failover pools, things of that nature. Uh most of the time these at default are acceptable. If they're not, you can come in here and change these values uh to meet whatever criteria you have. Auto updates. Again, if you have a large fleet, we typically don't really need to mess with this too much. One thing about this though is that if you come back up to firmware updates, what whenever you click this button, whatever you have listed here is what's going to be downloaded.

[00:17:41] We have three different uh sources of installs. We have testing for uh really new features, things that we haven't rolled out to production yet. We have preview, which is kind of uh the things that we plan on releasing out to a production release, but we're still testing them. We may ask you to update to a preview release for a special feature or for a bug fix if you're working with us.

[00:18:03] If you need to do that, you'll just come here and select testing update and then go back here and uh click your update button. Otherwise, the rest of this stuff under auto updates, you can typically leave alone. Uh temperature control, we only require one temperature sensor per board to be functioning in order for the minor to run. And then these two kind of define how we determine if a uh sensor is bad.

[00:18:30] Fan control, power off speed. So this one matters if the minor goes into curtailment or for whatever reason stops hashing. What percentage do you want your fans to run at? A lot of places might have problems with back pressure where if a machine goes offline, the fans don't operate at, you know, 100% anymore. They're operating at 20%. So hot airs might be allowed or be forced back through that minor and then that enters the cold aisle inside of the the container or inside of the mining room uh which increases the temperature of miners you know next to it.

[00:19:03] So if you want a higher fan speed when the miner is not hashing you can change this to 40% 60% whatever percent makes sense to you up to 100. And then two big ones are no pick hashboard protection and overtemp auto recovery. No pick hashboard protection when enabled means that if the machine doesn't have a pick, if one board fails, all three boards will shut down. Uh this is a safety feature.

[00:19:30] If you have a machine with a board that fails out and you want to run it temporarily with just two boards, you come set this to false and hit update and that machine will be able to run on less than three hash boards. Then overtemp auto recovery. Uh this is what happens when a board overheats. Well, we will let that board go down and then come back up.

[00:19:49] If it's still too warm, take it down again, wait a few minutes, bring it back up. If it's still too warm, take it down again, double the wait time, bring it back up. It'll do this five times. Each time, evaluating temperature. If temperature is too high on that board, shut it down again. Uh when that occurs after the fifth time, the minor or the board will stay down and require user intervention in order for you to come back and start hashing again.

[00:20:14] Turn this off for immersion machines because immersion machines have a shared environment, a shared fluid, and you don't want a machine that's already overheating, continuously rebooting and warming the rest of that fluid up. Aircooled machines, you pretty much leave it at true. And then last but not least, the uninstall button. Now, I hope that everyone installs Lux OS. I hope you don't need to uninstall Luxos. But in the event that you do, for troubleshooting, for testing, you can just hit the uninstall button here.

[00:20:44] And when you hit uninstall, the machine will revert back to Bitmain with its previous configuration, same pools, same IP addresses, and come back up and start hashing again. Takes about 5 minutes or so, and uh your machine will be back online running Bitmate. But that's Lux OS in a nutshell. There's lots of little corner cases that we can get into and tuning that we can do to try to make your experience the best it can be.

[00:21:10] But for the average person just installing it for Luxo, just installing Lux OS for the first time, this is kind of where you're going to start. If you have any questions, feel free to reach out to support and me or one of my colleagues will be happy to help you out. Thank you.
