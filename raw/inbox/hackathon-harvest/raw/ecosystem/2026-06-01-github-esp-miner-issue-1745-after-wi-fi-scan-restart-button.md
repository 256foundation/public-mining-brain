# bitaxeorg/ESP-Miner issue #1745: After Wi-Fi scan restart button is not enabled

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1745
> Collected: 2026-10-07
> Published: 2026-06-01

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1745
- State: closed
- Author: ghost
- Opened: 2026-06-01
- Closed: 2026-06-03
- Labels: none

## Description

When changing to a new Wi-Fi SSID the Restart button is not clickable.

<img width="1046" height="522" alt="Image" src="https://github.com/user-attachments/assets/1d893965-4b2a-429f-9162-3594d37f4265" />

New Wi-Fi SSID selected, the Restart button can not be clicked on.

<img width="1684" height="817" alt="Image" src="https://github.com/user-attachments/assets/5f203b21-2ec7-48fe-a3bb-6e1ce0e7d816" />

Note
Wi-Fi password is the same for both Wi-Fi routers so left that field alone. 


## Comments

### mutatrum on 2026-06-01

Is that when you use the Scan button and Select Wi-Fi Network modal, or also if you type in the new name?

### ghost on 2026-06-01

Yes, if someone changes their Wi-Fi router out for a new one and they use the same password in the new router, all they do here is select the new Wi-Fi SSID and save the change and reboot the Bitaxe before taking their old router offline for example, or they are using a Wi-Fi extender and the password is the same as before, no need to update the password field in this example. 


### mutatrum on 2026-06-02

This is probably not specific for 2.14.0b4.

### ghost on 2026-06-02

The workaround for now is to click the Restart icon top right. 

<img width="1913" height="913" alt="Image" src="https://github.com/user-attachments/assets/d96440e5-67bd-44bc-9d94-e2e83bc93530" />

### WantClue on 2026-06-03

fix here: https://github.com/bitaxeorg/ESP-Miner/pull/1751
