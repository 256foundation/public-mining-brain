# bitaxeorg/ESP-Miner issue #67: verbindung bricht ab, factory flash geht nicht

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/67
> Collected: 2026-10-07
> Published: 2023-12-16

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 67
- State: closed
- Author: Lollo76
- Opened: 2023-12-16
- Closed: 2024-03-15
- Labels: none

## Description

Hello,

I get the normal firmware ﬂashed, but I have the problem that after a few 30 seconds, it writes underwolting that the power supply is the one from bitconmerch and has a constant 5.2xv, I wanted to flash the factory file and it doesn't work because it keeps restarting the flash breaks off after 27%. The problem is that it restarts from the beginning without any settings after 10 minutes or 3 hours.... now nothing shows in the log file in settings... does anyone have an idea?
The model with USB type C FW 2.01 was installed


## Comments

### skot on 2023-12-16

Make sure you have the barrel power connector inserted all the way. 

### Lollo76 on 2023-12-16

The plug is in as far as it will go, it just jumps from the picture where it says shares accepted to the wifi
<img width="1055" alt="Unbenannt PNG4" src="https://github.com/skot/ESP-Miner/assets/98686265/58e74ab7-cd64-4451-a2e3-5c3edf7e8553">


### Lollo76 on 2023-12-16

<img width="938" alt="5" src="https://github.com/skot/ESP-Miner/assets/98686265/47ff2e3a-874b-4d19-8531-ab59ff6d7324">


### benjamin-wilson on 2023-12-18

You need to fix the restarting issue first, can you post the realtime logs when it happens 

### Lollo76 on 2023-12-18

hi it showed me this data when booting, then I updated the web.bin, the connection was interrupted due to the undervolting, now I can no longer access the website, but I can under USB ESP tool (website). to access it... the data he showed me...

The display on the miner is also dead after the web.bin flash was aborted

thanks for help 
dx:0,
₿
₿
₿ dx:1 (ifx:0, 48:5d:35:ab:7f:bd), tid:1, ssn:0, winSi
₿
₿
₿ dx:0 (ifx:0, 48:5d:35:ab:7f:bd), tid:0, ssn:58, winSi
₿
₿
₿ dx:0,
₿
₿
₿ dx:1,
₿
₿
₿ dx:0 (ifx:0, 48:5d:35:ab:7f:bd), tid:0, ssn:60, winSi
₿
₿
₿ dx:1 (ifx:0, 48:5d:35:ab:7f:bd), tid:1, ssn:0, winSi
₿
₿
₿ dx:1,
₿
₿
₿ dx:1 (ifx:0, 48:5d:35:ab:7f:bd), tid:1, ssn:0, winSi
₿
₿
₿ dx:1,
₿
₿
₿ dx:1 (ifx:0, 48:5d:35:ab:7f:bd), tid:1, ssn:0, winSi
₿


### Lollo76 on 2023-12-18

<img width="598" alt="esp" src="https://github.com/skot/ESP-Miner/assets/98686265/2cb27bcf-023e-4b08-9b97-2921876cf56d">


### benjamin-wilson on 2024-03-15

Closing inactivity
