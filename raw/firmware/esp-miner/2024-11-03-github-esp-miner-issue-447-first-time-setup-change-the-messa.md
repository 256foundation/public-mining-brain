# bitaxeorg/ESP-Miner issue #447: First time setup - Change the message on OLED

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/447
> Collected: 2026-10-07
> Published: 2024-11-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 447
- State: closed
- Author: ghost
- Opened: 2024-11-03
- Closed: 2025-04-01
- Labels: none

## Description

First Time Setup (this includes if the end user has "factory reset" their device).

**OLED Display**
Replace the SSID "myssid" to display a different message here to inform the end user that the device needs to be set up with their WiFi info from their WiFi router.

ie

"Connect to the SSID below to setup WiFi settings from your WiFi router !" 

or

"Network setup REQUIRED, connect to SSID below via cell phone !"

_Image example enclosed_

![FactoryState](https://github.com/user-attachments/assets/eaed27f6-46e7-4e0d-b058-bb3192301491)


## Comments

### skot on 2024-11-03

I like this. We'll have to work on the wording a bit to get it to fit.

We can use SSID == MYSSID as the condition for this mode.

### ghost on 2024-11-03

Here you go 

All the  .cvs    files for the board versions.... 

401 example below

''key,type,encoding,value
main,namespace,,
hostname,data,string,bitaxe
wifissid,data,string,WiFi SETUP REQUIRED
wifipass,data,string,password
stratumurl,data,string,public-pool.io
stratumport,data,u16,21496
stratumuser,data,string,bc1qnp980s5fpp8l94p5cvttmtdqy8rvrq74qly2yrfmzkdsntqzlc5qkc4rkq.bitaxe
stratumpass,data,string,x
fbstratumurl,data,string,solo.ckpool.org
fbstratumport,data,u16,3333
fbstratumuser,data,string,bc1qnp980s5fpp8l94p5cvttmtdqy8rvrq74qly2yrfmzkdsntqzlc5qkc4rkq.bitaxe
fbstratumpass,data,string,x
asicfrequency,data,u16,490
asicvoltage,data,u16,1166
asicmodel,data,string,BM1368
devicemodel,data,string,supra
boardversion,data,string,401
flipscreen,data,u16,1
invertfanpol,data,u16,1
autofanspeed,data,u16,1
fanspeed,data,u16,100
selftest,data,u16,1
overheat_mode,data,u16,0"


![FactoryState2](https://github.com/user-attachments/assets/c5513bd4-7812-443f-871b-2122978f3a9b)


### skot on 2024-11-03

Wow, yes that's a nice simple way to do it!

I still think we might want to have a "Initial Setup Mode" screen to make this even easier for the first-timers

### mutatrum on 2024-12-12

This is fixed with #539.

https://github.com/skot/ESP-Miner/blob/ba6be3c3bbb827df471e22bf2ecc54112d3fd82c/main/screen.c#L114-L123

### ghost on 2025-01-27

See https://github.com/skot/ESP-Miner/pull/623
