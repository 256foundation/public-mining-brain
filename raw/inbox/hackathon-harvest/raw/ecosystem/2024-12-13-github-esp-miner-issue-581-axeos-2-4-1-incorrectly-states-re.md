# bitaxeorg/ESP-Miner issue #581: AxeOS 2.4.1 incorrectly states restart is needed to change hostname

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/581
> Collected: 2026-10-07
> Published: 2024-12-13

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 581
- State: closed
- Author: alltheseas
- Opened: 2024-12-13
- Closed: 2026-05-29
- Labels: enhancement, good first issue

## Description

_what happens_
1) change hostname
2) AxeOS displays restart required for changes to take effect
3) I observe that the hostname name is updated in Swarm view without a restart

![restartfalsealarm](https://github.com/user-attachments/assets/cbb03102-0dd7-4cf8-9685-fabb4031befe)

_suggestion_

Consider removing the "restart needed" in case of hostname change

## Comments

### skot on 2024-12-13

I think you'll find that if you change the hostname and the WiFi details you _will_ need a restart for either of them to take effect..

### alltheseas on 2024-12-13

> I think you'll find that if you change the hostname and the WiFi details you will need a restart for either of them to take effect..

Does the following logic work:

1. if hostname only is changed, then do not prompt for a restart
2. if wifi info is changed, then prompt for a restart

### skot on 2024-12-13

> Does the following logic work:
> 
> 1. if hostname only is changed, then do not prompt for a restart
> 2. if wifi info is changed, then prompt for a restart

Yes, I think that could work! We probably have this same situation on the settings tab too. Fan speed comes to mind. @mrv777 what do you think? How possible is this to have some logic in there to determine if a restart is actually needed?

### mrv777 on 2024-12-22

@skot Yeah, I can do that.  I'm not sure which list is shorter, but so we have a list of what changes REQUIRE a restart and/or what changes DON'T REQUIRE a restart?

### WantClue on 2026-05-29

The hostname is live being reported on the api but the actualy hostname change does not happen until a wifi reconnect as the esp-idf docs show. So technically a restart is still needed. I'm looking into that

### alltheseas on 2026-05-29

Thanks for the fix gents. Make bitaxe great again!
