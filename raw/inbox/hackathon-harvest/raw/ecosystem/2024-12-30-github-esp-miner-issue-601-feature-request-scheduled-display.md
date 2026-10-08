# bitaxeorg/ESP-Miner issue #601: [Feature Request] Scheduled Display Off

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/601
> Collected: 2026-10-07
> Published: 2024-12-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 601
- State: open
- Author: vinxp97
- Opened: 2024-12-30
- Closed: n/a
- Labels: none

## Description

Not sure if this should be grouped/merged with #515 (as that is related to toggling the screen on/off with a button), but it would be nice if the devices screen could turn off automatically at certain times during the day. 

For instance, have a customizable schedule in which the display turns off at 11:59PM and back on at 8:00AM. This would prove beneficial for devices kept in bedrooms, theaters, or near TVs/screens.

I know this isn't high priority, but it would be a nice QOL feature that I don't think would be too tough to do.

## Comments

### mutatrum on 2025-01-02

Bitaxe has no concept of what time it is. There is also no RTC module that can keep time over reboots, and calling out to a timeservice is probably not desired. There is already #525 which has some discussion on this as well.

### skot on 2025-01-02

we have the block template ntime.. Not super precise though.

### skot on 2025-01-02

we've have to add the users timezone to nvs too...  

### mutatrum on 2025-01-03

User timezone can be fetched from the browser, IIRC?

### 0xf0xx0 on 2025-01-04

if you use a chromium browser yes, firefox returns utc. wouldn't that also require the user to visit the webui after each reflash?

### ffrediani on 2025-01-08

Hi @mutatrum what would be the issue to call call a timeservice ? The lack of a RTC doesn't seem a concern since the time used for turn off display doesn't need to be super precise but just rough.

One thing I would also add to this feature if developed, to add an Toggle On/Off button someone to allow doing it manually if desired as well.

### mutatrum on 2025-01-08

For privacy, the Bitaxe should only contact the pool and nothing else. AFAIK this is a hard requirement, but maybe others can chime in.

### MyOwn2C on 2025-01-08

> For privacy, the Bitaxe should only contact the pool and nothing else. AFAIK this is a hard requirement, but maybe others can chime in.

I agree 100%

To have unnecessary contact to external time server just for dimming/turning off the screen is not worth it. 

Instead, I think an API call to turn on/off the screen and let user control it that way is much cleaner and easier. 

### ffrediani on 2025-01-08

It can well be a local NTP server as well. Yes it is not a major feature, but it isn't a big deal as well.

If this doesn't get implemented due to this reason, at least having a Toggle On/Off button can do as well.

### MyOwn2C on 2025-01-09

> It can well be a local NTP server as well. Yes it is not a major feature, but it isn't a big deal as well.
> 
> If this doesn't get implemented due to this reason, at least having a Toggle On/Off button can do as well.

Is then a local NTP server a requirement for future ESP-Miner? That seems a bit silly.

Toggle ON/OFF: I can foresee more users complaining “My screen is not working” increasing. Unless this toggle is revert to ON during restart

### ffrediani on 2025-01-09

It has never been and remains not being a requirement. Why by having a feature it is a must use ? 

Regarding Toggle On/Off is pretty straight forward thing. Doesn't need to complicate of make up problems that don't exist.
Agree toggle should be reverted to On after restart.

### MyOwn2C on 2025-01-09

> It has never been and remains not being a requirement. Why by having a feature it is a must use ?
> 
To have any scheduling function requires either RTC or a source for time (ie, NTP server). 

There is no RTC from ESP32, nor do we want to add more hardware cost to add RTC just to have scheduling for the display.

As @mutatrum stated, for privacy ESP-Miner should only contact the pool for mining, nothing else. To contact external NTP, or having the need to run a local NTP to feed ESP-Miner time data so a schedule can be setup to turn off display would defeat that intent.

A sticky note that you put over the display to dim it when you need to is very easy to do, and it requires zero code change....


### ffrediani on 2025-01-09

Don't need to over complicate things. If you want to find problems for not do to something there will always be.
As mentioned it doesn't seem any major or very needed feature really, but it has been well justified initially. Just trying to look at the positive side.

If it doesn't get implemented because it is not worth fine, but at least a Toggle On/Off button is worth, simpler and doesn't need to don't need to resort to makeshift solutions like stick note.

### vinxp97 on 2025-01-09

Forgive my ignorance, but does the Bitaxe not receive metadata from the last found block or current block time during its calculations? Or could it not see the date/time metadata of the most recent transaction on the block to make a rough estimate of when the current time is?

The time the display turns on and off wouldn't need to be exact. Just have it trigger when the time identified using the logic would fall within the range.

This option doesn't need to be enabled by default -- I don't see how folks would think their screen isn't working if a schedule is enabled. Bitaxe is an enthusiast tier product and I think most folks purchasing one would probably be able to do basic troubleshooting, not to give the general public too much credit.

### vinxp97 on 2025-01-09

> we have the block template ntime.. Not super precise though.

I think this is what I'm getting at -- sorry for the double reply.

This would be more than sufficient (precision-wise). So the solution would essentially require:

1) Time Zone Dropdown/Choice
2) Display off & Display on time(s)

> For privacy, the Bitaxe should only contact the pool and nothing else. AFAIK this is a hard requirement, but maybe others can chime in.

3) Calculate Latest/Last Block Time: whatever reoccurring time is available without additional queries/server calls. This is where my knowledge has a gap (as far as how the Bitaxe runs). Assume precision isn't necessary - at what point could the Bitaxe know for certain based on the network that time has passed during its normal course of operation?

4) Convert block time to user selected timezone
5) trigger display/lower brightness if within range of time(s)

While a toggle button would be nice, folks with existing hardware wouldn't be able to take advantage of it. And having to do it yourself daily is also a chore. I personally think this is a well worth feature (that on paper doesn't sound complicated), but maybe I'm in the minority.

While a sticky note sounds great in practice, in reality it's the same issue as a toggle -- why do I need to do it manually when there are definitely ways to feasibly do it automatically?

### ffrediani on 2025-01-09

> 1. Time Zone Dropdown/Choice
> 2. Display off & Display on time(s)
> 3. Calculate Latest/Last Block Time: whatever reoccurring time is available without additional queries/server calls. This is where my knowledge has a gap (as far as how the Bitaxe runs). Assume precision isn't necessary - at what point could the Bitaxe know for certain based on the network that time has passed during its normal course of operation?
> 4. Convert block time to user selected timezone
> 5. trigger display/lower brightness if within range of time(s)

Seems to make sense in my view.

### m4rquez on 2025-01-09

Wouldn't it be sufficient if there is an API Endpoint like http://YOUR-BITAXE-IP/api/system/toggleDisplay
You could call it from any other device in your network or even use a schedule.

### MyOwn2C on 2025-01-09

> Wouldn't it be sufficient if there is an API Endpoint like http://YOUR-BITAXE-IP/api/system/toggleDisplay You could call it from any other device in your network or even use a schedule.

API to turn screen on/off is much easier to implement and more elegant. 


### vinxp97 on 2025-01-09

> > Wouldn't it be sufficient if there is an API Endpoint like http://YOUR-BITAXE-IP/api/system/toggleDisplay You could call it from any other device in your network or even use a schedule.
> 
> 
> 
> API to turn screen on/off is much easier to implement and more elegant. 
> 
> 

My only issue/concern with this is that it requires a secondary service to trigger this? I'm trying to think of feature usability from the perspective of a layperson.

### MyOwn2C on 2025-01-10

> > > Wouldn't it be sufficient if there is an API Endpoint like http://YOUR-BITAXE-IP/api/system/toggleDisplay You could call it from any other device in your network or even use a schedule.
> > 
> > 
> > API to turn screen on/off is much easier to implement and more elegant.
> 
> My only issue/concern with this is that it requires a secondary service to trigger this? I'm trying to think of feature usability from the perspective of a layperson.

RTC hardware adds costs. 
Block time + time zone + calculations complicates the code. 
API on/off needs external processors. 

There is no “freebie” for this (in my opinion) low importance and non critical feature. 

API at least is easier to implement by code. 

If you have a laptop, RPi or other home automation on the same network, they can run the API on schedule. 


### ffrediani on 2025-01-10

It doesn't seems to me that only critical features should be developed. If it is something relatively simple and someone is willing to write the code rather than a more complex one why have barriers ?

It doesn't seem also that anyome is considering the need of a RTC for something like a Bitaxe.

So Blocktime + timezone seems a more reasonable solution. It will not influence others parts of the code that would have to be reworked and will only be used for the Display off feature so far, so any code complexity is a matter for whoever is writing the code.

API only I don't think is sufficient. At minimal if this gets developed a simple button on the web interface is a good start with maybe a checkbox for the reset on reboot option too.

### mutatrum on 2025-01-10

There's also #515/#525 and #567 that are in the same area, and are simpler to implement. IMO it would make sense to first add those, as most use-cases can be tackled then, in order of simple to more complex:
 * Screen too bright -> dim it
 * Screen timeout after x hours, button press to wake-up.

 Maybe after those, this issue could be revisited to see if it's still needed.
