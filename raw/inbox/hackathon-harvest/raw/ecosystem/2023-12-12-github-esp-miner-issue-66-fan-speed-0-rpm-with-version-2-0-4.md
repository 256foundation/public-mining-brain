# bitaxeorg/ESP-Miner issue #66: Fan speed 0 rpm with version 2.0.4

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/66
> Collected: 2026-10-07
> Published: 2023-12-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 66
- State: closed
- Author: CoanLuciano
- Opened: 2023-12-12
- Closed: 2023-12-15
- Labels: none

## Description

After upgrade, fan speed always 0rpm. Even after Invert Fan Polarity and disable Automatic Fan Control.
Hardware BM1397 v2.2

## Comments

### d6n13l0l1v3r on 2023-12-13

Same issue happen to me with model  BM1366

Power Consumption:	11.66 W
Input Voltage:	5,380 mV
Input Current:	2,169 mA
Frequency:	485 Mhz
Core Voltage:	1200 mV
Measured Core Voltage:	1204 mV
Fan Speed:	0 RPM
Chip Temperature:	46 C




### cmelius on 2023-12-15

I have the same problem with 2.0.4. BM1366
Fan: 0 RPM
Termp: 37.0 C
Pwr: 12,210 W
4847mV: 2530 mA
vCore: 1222 mV

### skot on 2023-12-15

Is the fan actually spinning? What fan do you have installed? How many wires does the fan have?

What did it say the fan speed was before the upgrade?

### cmelius on 2023-12-15

Yes, my fan is spinning. I can't tell which fan is installed currently. I am the guy you retweeted on twitter yesterday with the D-Central Minibit - case. Probably some no name stuff. 
Noctua fan is on it's way to get it more livingroom compatible. Will keep you updated once that is installed. probably tuesday.

edit after [d6n13l0l1v3r](https://github.com/d6n13l0l1v3r) comment: also just 3 cables
the noctua one will be 4-pin.
I also immediately upgraded to 2.0.4 and don't know what it said before. 

### d6n13l0l1v3r on 2023-12-15

answered below:

 iIs the fan actually spinning?    YES
 What fan do you have installed?  capture 1
How many wires does the fan have? 3  capture 2

![IMG_5315](https://github.com/skot/ESP-Miner/assets/25048143/7e8225e1-32d1-4e8c-a61e-95639fe5ac72)


![IMG_5316](https://github.com/skot/ESP-Miner/assets/25048143/a4f5189e-9806-493b-86b2-e2f1ce4fe4d2)

in the setting I have 

Invert Fan Polarity:  checked
Automatic Fan Control: checked 


What did it say the fan speed was before the upgrade? I don't have previous version 



### CoanLuciano on 2023-12-15

Actually now I'm running 2.0.1, the fan is spinning and I can read its speed.
![image](https://github.com/skot/ESP-Miner/assets/98968954/ab862459-a7c0-44c4-800e-81a350c63923)


### d6n13l0l1v3r on 2023-12-15

> Actually now I'm running 2.0.1, the fan is spinning and I can read its speed. ![image](https://private-user-images.githubusercontent.com/98968954/290842029-ab862459-a7c0-44c4-800e-81a350c63923.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDI2NDk1NDQsIm5iZiI6MTcwMjY0OTI0NCwicGF0aCI6Ii85ODk2ODk1NC8yOTA4NDIwMjktYWI4NjI0NTktYTdjMC00NGM0LTgwMGUtODFhMzUwYzYzOTIzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzEyMTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMjE1VDE0MDcyNFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWRiODlhMzY0YWUwMGVmMjI0YTQ4MzcyMjVmYzI3YTg0YWZiNGE4MGJjZmEzNTNmODdiNDYyNjVhZTY0OTVjYzImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.BI5jxqVtCKavevJPaP7URl8JLivq-fKRzBUgfzuJJPk)

what fan do you have ? how many wire? 



### CoanLuciano on 2023-12-15

3 wire fan. Same as  [d6n13l0l1v3r](https://github.com/d6n13l0l1v3r) has

### benjamin-wilson on 2023-12-15

That Chinese fan doesn't actually have a sense wire, the sense wire is connected to ground. The reading is correct.

### CoanLuciano on 2023-12-18

So please answer me. Why does it read the fan speed using an old version (2.0.1) The info is not real??

### cmelius on 2023-12-21

update: installed Noctua NF-A4x10 PWM and everything works now. 
Fan speed is displayed, RPM is controlled and I am really surprised by the silence. 
I can't tell that the fan is spinning just by the sound of it! The old noname fan was really loud im comparison. 
Highly recommended upgrade!

I had to cut some plastic from the 4-pin connector as it wouldn't fit in the socket. 

### skot on 2023-12-21

> So please answer me. Why does it read the fan speed using an old version (2.0.1) The info is not real??

As Ben said, those fans do not have speed sensors. Previous FW versions displayed an incorrect fan speed in these cases.
