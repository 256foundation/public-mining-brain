# bitaxeorg/ESP-Miner issue #140: Firmware 2.1.2 Self Test on BM1397 Power is failed

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/140
> Collected: 2026-10-07
> Published: 2024-03-17

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 140
- State: closed
- Author: xXAsystolieXx
- Opened: 2024-03-17
- Closed: 2024-03-18
- Labels: none

## Description

After I updated to version 2.1.2, my Bitaxe fails the self test and shows me Power fail. I went back to 2.1.1 and it works again. Hope you can solve the problem :) 


## Comments

### MyOwn2C on 2024-03-17

Release notes say self-test doesn’t work on Max 1397. Please read link below.

https://github.com/skot/ESP-Miner/pull/139

![image](https://github.com/skot/ESP-Miner/assets/158797249/5f7713a7-c09a-4278-9e18-553921196925)


### benjamin-wilson on 2024-03-17

> After I updated to version 2.1.2, my Bitaxe fails the self test and shows me Power fail. I went back to 2.1.1 and it works again. Hope you can solve the problem :

> After I updated to version 2.1.2, my Bitaxe fails the self test and shows me Power fail. I went back to 2.1.1 and it works again. Hope you can solve the problem :)

You also need to reset the frequency and voltage to default before upgrading 

### xXAsystolieXx on 2024-03-18

> Release notes say self-test doesn’t work on Max 1397. Please read link below.
> 
> #139
> 
> ![image](https://private-user-images.githubusercontent.com/158797249/313510171-5f7713a7-c09a-4278-9e18-553921196925.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTA3MjE1MTcsIm5iZiI6MTcxMDcyMTIxNywicGF0aCI6Ii8xNTg3OTcyNDkvMzEzNTEwMTcxLTVmNzcxM2E3LWMwOWEtNDI3OC05ZTE4LTU1MzkyMTE5NjkyNS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMzE4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDMxOFQwMDIwMTdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jZmFiYTRjM2RhNzMzZmFhY2ZhNGY1ZmZmNjAyOGM2NjdjMjEzM2QwNWVjNmI5Mjc2MjhhYmQ3ZWNlNzI1ZmI2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.Qau0Br6wuRIHWSfsmS8_x7Ze9HW6xmmqUaAIMASdq9s)

my mistake, sorry ^^
