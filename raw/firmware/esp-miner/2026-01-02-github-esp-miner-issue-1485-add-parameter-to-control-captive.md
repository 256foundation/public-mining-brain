# bitaxeorg/ESP-Miner issue #1485: Add parameter to control captive portal feature in CVS

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1485
> Collected: 2026-10-07
> Published: 2026-01-02

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1485
- State: closed
- Author: casualmine
- Opened: 2026-01-02
- Closed: 2026-02-08
- Labels: none

## Description

I would like to request the addition of a parameter in CVS to control whether the captive portal feature is enabled or disabled. Currently, the captive portal appears automatically in certain scenarios, but there are use cases where users may prefer to disable this feature for better control over network behavior or to avoid unintended interruptions.

## Comments

### casualmine on 2026-01-02

https://github.com/bitaxeorg/ESP-Miner/pull/1484

### mutatrum on 2026-01-05

To prevent users from painting themselves into the corner, which cases should the captive portal not be used? Because it's quite easy to make the device unreachable without this, and forces the user to do a factory reset.

### casualmine on 2026-01-05

I built an app that uses the ESP-Miner API to configure and tune system parameters. In this context, a forced pop-up would only confuse users.
The captive portal stays on by default; only in rare edge cases would someone flash the device to disable it. For the vast majority, the experience is completely seamless and unobtrusive.

### mutatrum on 2026-01-06

I don't follow, what do you mean with forced pop-up? And why would a tuning app be hindered by the captive portal? Can you explain the use-case of disabling it?

### casualmine on 2026-01-06

I've developed an application specifically designed to simplify the Bitaxe configuration process. The core goal of this app is to allow users to complete all configuration operations directly within the application without needing to switch to a browser, thereby providing a smoother user experience.
However, in actual use, I've encountered an issue that affects user experience: when users first configure their device and connect to the Bitaxe WiFi, if Bitaxe has the captive portal feature enabled, the system forcibly opens a browser window. This interrupts the user's workflow within the app and contradicts the integrated experience I'm hoping to provide.
Therefore, I'd like to ask whether it would be possible to provide an optional parameter during flashing that would allow Bitaxe manufacturers to choose to disable the captive portal functionality. This would enable users who are using dedicated configuration apps to have a better experience.
My motivation for developing this application is to lower the barrier to entry for Bitaxe and make it easy for non-technical users to get started. For example, users no longer need to use a computer for configuration, nor do they need to switch between different websites to generate wallet addresses—the app has built-in address generation functionality (for security reasons, we don't store users' seed phrases).
I hope this suggestion can be taken into consideration. If you need more technical details or explanation of usage scenarios, I'd be happy to discuss further.
Thank you very much for your time!

### WantClue on 2026-02-08

This doesn't seem like a good idea and might add confusion why for some it's utilising the captive portal and for others not. Also we're not tying this fw to a specific use case of a singular manufacturer or app creator.
