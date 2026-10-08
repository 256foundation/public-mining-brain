# bitaxeorg/ESP-Miner issue #998: Feature Suggestion

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/998
> Collected: 2026-10-07
> Published: 2025-06-02

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 998
- State: closed
- Author: carliartger
- Opened: 2025-06-02
- Closed: 2025-06-27
- Labels: none

## Description

Please integrate the following Features:

Generell:
- Remote Access / Control to the webinterface or App / Bitaxe Gamma 601 
-  With allert function for overheating 
- Fallback WLAN Network 

Webinterface / 
- Option for shut down / deactivate / Power off / Power on Button 

Trank you 


## Comments

### MyOwn2C on 2025-06-02

Remote access:
Easier and more secure if you setup VPN. A login page with weak/no security will only give you false sense of security and open invitation to hackers. 

Alert for overheating:
I think this is already available in API? If yes, then just make API call at interval to check

Fallback WAN:
Unless users has fallback 2.4 GHz WiFi, not very useful. If ESP32 supports 5 GHz, then it would be useful. 

Shutdown:
This could be useful. 

### skot on 2025-06-02

We do not have the hardware capability to completely shutdown the bitaxe. We can stop mining and go into a lower power state though -- I think there is a PR for this.

### carliartger on 2025-06-02

VPN Check 

Heat Check 

Regarding WLAN fallback:
It Would be helpfull when my Home Route is down, the Axe hat’s Fall possilitiy to Switch to another mobile Network Like my Smartphone .

Somtimes some Provider have issues to deliver solid a Network Connection and it would be Great when there is a second Option to automaticly Connect (Like the Pool Fall back ) in this case with for example an iPhone or something else. 

Regarding power Off.
Yes ist would be Great when there is a sleep Mode with low Energy and work load . 

Trank you for your Support , the Bitaxe is very Great ! 

### mutatrum on 2025-06-02

Start/stop mining PR is #927. This doesn't power down the whole device, it leaves the controller running, but should drop the power usage to low single digit watt.

As for fallback WLAN: the simplest option is to have your phone hotspot have the same SSID/password as your home network. This is what I do as well, but it's mainly for connecting my laptop or other devices on the go, so they all just seamlessly connect. And IMO this is outside the scope of AxeOS. Secondary internet connections are for datacenter operations, not home consumer things. If you really want it, you can have a secondary internet provider (f.e. with a sim card) in your home router.

Can you elaborate on the alert, how would you want to be alerted? The tricky thing here is that the Bitaxe doesn't connect to any other service other that the mining pool. The only exception is to do a version check to GitHub, but that's only on the users request. So if you want an alert, that would have to be a secondary service that fetches data from the Bitaxe devices, not the Bitaxe devices reaching out.

### carliartger on 2025-06-03

Right I Understand! Great Suggestion with Same WLAN SSID and PW. It works.

Regarding the alert:
I just wanted some Info and Control if i am on travelling and the Heat is over 80 (depents on the weather - Room teperature ) , so that I can Change the Settings Parameter of the Bitaxe from Remote. 

My goal is to run the axe 24/7 . 365 days with Max uptime and best conditions. But there are some possobilitys that can influce this.

I will Check wich information a secondary service could get from the axe .

Thank you all Great Support . 



### WantClue on 2025-06-27

This Issue will be closed, if more discussion is needed feel free to open a [discussion](https://github.com/bitaxeorg/ESP-Miner/discussions)
