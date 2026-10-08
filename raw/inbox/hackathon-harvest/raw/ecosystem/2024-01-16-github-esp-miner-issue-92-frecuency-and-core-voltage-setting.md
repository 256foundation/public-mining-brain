# bitaxeorg/ESP-Miner issue #92: Frecuency and Core Voltage settings lost after random reboots

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/92
> Collected: 2026-10-07
> Published: 2024-01-16

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 92
- State: closed
- Author: github-block
- Opened: 2024-01-16
- Closed: 2024-02-25
- Labels: none

## Description

Time to time, there are random reboots and the settings for Frequency and Core Voltage go to blank. Then the bitaxe lower the power consumption to 2-3w and the hashing stops. 

When it happens, I'm able to set the values again and reset it and then everything start working again.

## Comments

### github-block on 2024-01-16

I'm using version 2.04 on board 202. I'll flash 206 and check as you suggested. Also, as I mentioned, the issue occurs randomly and it could take some days to happen again.

### benjamin-wilson on 2024-01-16

It is going into overheating protection mode. What do you have for frequency and voltage settings? What are your temperatures?

### github-block on 2024-01-16

The one that failed this morning is usually about 51 in temp and default/default. Generic/Chinese fan.Source Leicke 4A/20W

### benjamin-wilson on 2024-01-16

Who is the manufacturer?

### github-block on 2024-01-16

I currently have 3 devices from 2 manufacturers and the issue happens in all of them time to time:
rgzen.com (Spain)
silexperience.company.site (France)

### StarGateMiner on 2024-01-16

See here its similar issue: https://github.com/skot/ESP-Miner/issues/85
But I do not get on mine the loss of values.

Chip Temp reaches about 55- not sure what temp it has to be to cause a restart

### benjamin-wilson on 2024-01-16

Could you take a clear, closeup picture of U7 component on the back?

### github-block on 2024-01-16

![photo1705430168](https://github.com/skot/ESP-Miner/assets/155159549/2824b962-ceec-48a2-9560-88e07a4a00a8)


### benjamin-wilson on 2024-01-16

![image](https://github.com/skot/ESP-Miner/assets/1399163/e4c17c56-cf00-4695-8b4c-6bf0b2a93236)

It's possible these might be counterfeit IC's I'll have to contact the manufacturers 

### benjamin-wilson on 2024-01-16

Hmm manufacturers get them from DK, so nothing of particular interest there. Lets leave this issue open to gather more data.

### CaptainCodeman on 2024-01-17

Just had the same thing happen - the auto fan control had also turned off and was set to max (the fan noise is what alerted me). It also had some message about "S19".

I restarted and it seems fine, I don't _think_ temps where high (it's normally 55-59 range) but I'll make a note if it happens again.

I'm already running v2.0.6

### github-block on 2024-01-17

@CaptainCodeman , exactly.. I forgot to mention that the auto fan control also got turned off

### skot on 2024-02-16

this really sounds like over temp mode. can one of you get a screenshot of the whole AxeOS dashboard page after this happens?

### benjamin-wilson on 2024-02-25

Closing, no response, seems to be over temp.

### CaptainCodeman on 2024-02-29

Sorry, whenever this happened I restarted it and forgot about the screenshot!

I did take the heatsink off both of mine and cleaned off and re-applied thermal paste and they have been fine since. There was an ungodly amount of paste on there which I don't think was helping - it would have been way too much even for a big Intel CPU.

Something to check if you come across this issue.
