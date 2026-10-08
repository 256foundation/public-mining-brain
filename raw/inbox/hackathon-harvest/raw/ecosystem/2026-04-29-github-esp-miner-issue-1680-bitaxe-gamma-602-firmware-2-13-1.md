# bitaxeorg/ESP-Miner issue #1680: bitaxe gamma 602, firmware 2.13.1: from time to time it goes back to hotspot mode, wifi password need to be set again

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1680
> Collected: 2026-10-07
> Published: 2026-04-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1680
- State: open
- Author: gilav
- Opened: 2026-04-29
- Closed: n/a
- Labels: bug

## Description

Hello

From time to time I find my bitaxe602 in hotspot mode.
When I access it, the wifi network name is ok, I just enter the password, do save/restart and it goes mining as normal.

bitaxe is very close to the router and displays an excellent wifi level on his display.

Is it possible that it loses the wifi password in case of wifi disturbance/lost connection?

This on:
bitaxe gamma 602
firmware 2.13.1

Thanks

## Comments

### JAndrew77 on 2026-05-01

Hi, I also found my Bitaxe in this state after the night. Could it be caused by the router’s nightly reboot, during which the SSID is unreachable for a few seconds? 

This on:
bitaxe gamma 602
firmware 2.13.1

Thanks.

### ghost on 2026-05-01

Wi-Fi router

Do you have WPA2 or WPA3 set in your Wi-Fi router for 2.4G ? 

<img width="1115" height="608" alt="Image" src="https://github.com/user-attachments/assets/99521ff0-17b1-4551-9425-356ca6523692" />

### JAndrew77 on 2026-05-01

Tonight I tried switching from WPA2 to WPA/WPA2, and the Bitaxe automatically obtained a new IP without any issues (after restarting the router), continuing to work normally. Now I’ll switch back to WPA2 only and check again tomorrow to see whether the issue might be related to this configuration. 

### JAndrew77 on 2026-05-05

Update - 1:

Even after switching the Wi-Fi to WPA2-only, the issue has not reoccurred for at least three days. One change I made is assigning a static IP via DHCP based on the Bitaxe’s MAC address, although I’m not sure whether this is related to the improvement. 

### mutatrum on 2026-05-05

Any update on this? Did the Wi-Fi settings help?

### JAndrew77 on 2026-05-05

Update - 2   

After a power outage that stopped the router for more than 5 minutes, the Bitaxe—still powered by a UPS—ended up back in SSID setup mode even after Wi-Fi and internet connectivity were restored. Simply pressing the device’s reset button brought it back to normal operation. However, it does not automatically restart after detecting a Wi-Fi connection issue once that issue has been resolved. 

### WantClue on 2026-05-30

the bitaxe doesn't look again for a wifi to connect to if it can't find one in the first place, good issue thanks will work on this

### ghost on 2026-06-11

> Update - 2
> 
> After a power outage that stopped the router for more than 5 minutes, the Bitaxe—still powered by a UPS—ended up back in SSID setup mode even after Wi-Fi and internet connectivity were restored. Simply pressing the device’s reset button brought it back to normal operation. However, it does not automatically restart after detecting a Wi-Fi connection issue once that issue has been resolved.

I've been testing here for this, I can't reproduce the issue.

Steps
1/ Device connected to the router.
2/ Router turned off to simulate a power outage and left turned off for 20 mins plus.
3/ Bitaxe stayed powered, AP shows on the screen.
4/ After 20 minutes or more the router is turned back on.
5/ The Bitaxe sees the Wi-Fi and continues as if nothing is wrong.

v2.13.1 - Router was turned off, waited 20 mins and then turned the router back on.
  

<img width="1903" height="837" alt="Image" src="https://github.com/user-attachments/assets/a6f4ec18-06cc-496f-b1ec-45b17ce299f7" />

  
Device reconnected to the Wi-Fi router after turning the Wi-Fi router back on after 20 mins plus.
  

<img width="1904" height="778" alt="Image" src="https://github.com/user-attachments/assets/46b6e06a-ea5a-4427-809e-172fb697fa00" />
  

<img width="691" height="688" alt="Image" src="https://github.com/user-attachments/assets/386e2669-2fbb-45dd-8b6b-23cbd3925930" />

Note
Also tested with v2.14.0

### JAndrew77 on 2026-06-11

Pending a firmware fix, if you have a Shelly Plug S Gen3, I found this workaround:

[Solar-Aware Bitaxe 602 Mining Automation with Shelly Plug S Gen3 (Watchdog Reboot Script)](https://community.shelly.cloud/topic/14641-solar-aware-bitaxe-602-mining-automation-with-shelly-plug-s-gen3-watchdog-reboot-script)

This solution uses a watchdog reboot script on the Shelly Plug S Gen3 to automatically recover the Bitaxe if it becomes unresponsive.

### mutatrum on 2026-06-11

> Pending a firmware fix

At this moment it's unclear what to fix, as its not reproducible. It almost sounds like a failure of the flash memory. Does it retain other configuration settings?

Other option, but that might be tricky is to capture the logs around this event. So go.from a connected bitaxe to one that forgot the Wi-Fi settings. The download logs button on 2.14 should help with that, as it makes to possible to retrieve historical logs over some time.

### ghost on 2026-06-11

Provide more info about the Wi-Fi router that is being used....

Brand
Model
Firmware
Wi-Fi settings within it etc

Due to not being able to reproduce your issue there is nothing more to do at this stage.
