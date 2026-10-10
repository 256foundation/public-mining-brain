# bitaxeorg/ESP-Miner issue #781: Color scheme changes back to `Dark` from `Light`

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/781
> Collected: 2026-10-07
> Published: 2025-03-19

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 781
- State: closed
- Author: etkaar
- Opened: 2025-03-19
- Closed: 2025-03-20
- Labels: none

## Description

1. Change color scheme from _Dark_ to _Light_.
2. Press `[F5]` one or multiple times. The setting will change back to _Dark_, though the _Light_ color scheme will be applied.
3. Press `[CTRL]+[F5]`. The color scheme will be reset to _Dark_, sometimes multiple `[CTRL]+[F5]` are required.

I tested it both in Google Chrome and Mozilla Firefox. I can confirm 2. also for on an iPhone with iOS 18.3.2.

## Comments

### etkaar on 2025-03-20

@WantClue Why did you close this issue? Was the bug fixed?

### etkaar on 2025-03-21

Sorry to say, but I think it's really unprofessional that bug reports are repeatedly being ignored by WantClue. This even is reproducable on an iPhone. Instead of using `[F5]` you can set the color scheme, then click on Dashboard and then open the settings by right-click or directly open http://YOUR-BITAXE-IP/#/settings. Something is definitely going on wrong here. 

It makes seven (7) GET requests to http://YOUR-BITAXE-IP/api/theme and two (2) POST requests to http://YOUR-BITAXE-IP/api/theme. Is even that normal?

@skot @johnny9 @benjamin-wilson @eandersson 

### etkaar on 2025-03-23

Hello? What is this rude behavior?

### MyOwn2C on 2025-03-25

Nothing to fix if no one else can duplicate your issue. 
I followed your steps and everything worked as expected. 
So issue is likely on your side, as I already said previously on the other post. 

### etkaar on 2025-03-25

Thank you for your answer. If the issue is immediately closed, there is no time for others to try to replicate it. Many users will keep the dark color scheme so will never encounter this issue. I would kindly ask you to check if you can confirm [this](https://github.com/bitaxeorg/ESP-Miner/issues/794) issue.

I tested it so many times on different operating systems and even on an iPhone. Since this could lead to settings accidentally being changed without the user even knowing it should be investigated what the reason for this odd behaviour is.

### NilByte on 2025-03-31

I can duplicate this issue.

Same behavior for me on Win 11 Edge or Chrome browser as well as Android 14 Chrome browser.

### etkaar on 2025-04-04

Issue is present in v2.6.2 as well.

### etkaar on 2025-04-08

Issue is now addressed in https://github.com/bitaxeorg/ESP-Miner/issues/794.
