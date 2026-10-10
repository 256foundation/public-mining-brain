# bitaxeorg/ESP-Miner issue #568: When configuring network, UI should only show network configuration page.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/568
> Collected: 2026-10-07
> Published: 2024-12-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 568
- State: closed
- Author: mutatrum
- Opened: 2024-12-10
- Closed: 2026-06-02
- Labels: enhancement, help wanted

## Description

If there's no SSID configured, it starts the AP to the user can configure the network. However, the landing page goes to the dashboard. It should go to the network configuration.

## Comments

### skot on 2024-12-11

I like this idea. But we should do it anytime the user is connected to the Bitaxe AP.. aka "setup mode"

### cyphercosmo on 2025-01-12

Maybe AxeOS could have a captive portal when people join the Bitaxe AP, then it could be a nice little onboarding flow ending with an instruction for the user to return to their wi-fi.

### skot on 2025-01-12

we do have a captive portal! But yes, a better onboarding flow would be great

### mutatrum on 2026-06-02

Fixed by #624
