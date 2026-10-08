# bitaxeorg/ESP-Miner issue #583: add toast upon successful firmware update; website update

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/583
> Collected: 2026-10-07
> Published: 2024-12-13

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 583
- State: closed
- Author: alltheseas
- Opened: 2024-12-13
- Closed: 2024-12-27
- Labels: none

## Description

_What happens_

![Screenshot from 2024-12-13 08-32-23](https://github.com/user-attachments/assets/9cdc57bb-5c59-4871-b904-c84623806603)

upon

1) updating firmware bin to latest, and/or
2) updating website bin to latest

there is no indication after the "Working" message disappears that the process was successful.

_Suggestion_

Consider adding a toast that indicates a successful update to the latest firmware, and/or website. You could use the same UI element, as when updating values in settings. 

![toastupdatefirmware](https://github.com/user-attachments/assets/2badb137-0de7-48ba-b78e-a6630fd87e01)


## Comments

### alltheseas on 2024-12-13

@skot advises

> I think we have added this
> What we don’t have is any way to tell what version axeOS is


STSMiner advises:

> Version 2.4.0 or lower will not show that, version 2.4.1 onwards does for each update file (esp-miner.bin & www.bin) in the settings page.


### alltheseas on 2024-12-13

- [ ] @alltheseas to test next update from 2.4.1 to later version when released to confirm



### mrv777 on 2024-12-22

Yeah, this should have been fixed with this PR: https://github.com/skot/ESP-Miner/pull/521
