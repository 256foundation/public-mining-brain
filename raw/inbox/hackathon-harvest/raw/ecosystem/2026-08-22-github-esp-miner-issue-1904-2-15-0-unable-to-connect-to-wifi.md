# bitaxeorg/ESP-Miner issue #1904: 2.15.0 : Unable to connect to WiFi

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1904
> Collected: 2026-10-07
> Published: 2026-08-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1904
- State: closed
- Author: Freeben666
- Opened: 2026-08-22
- Closed: 2026-08-25
- Labels: bug

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
Ever since the 2.15.0 update, my Bitaxe won't connect to WiFi. I even re-did the setup, but keep getting the same error: "IE differs in 4-way handshake (Error 17. Retry #xx)"

**To Reproduce**
Steps to reproduce the behavior:
1. Upgrade to 2.15.0
2. Reboot
3. Miner won't connect anymore

**Expected behavior**
The miner should reconnect properly to the WiFi AP after the update

**Screenshots & Photos**

<img width="1440" height="1920" alt="Image" src="https://github.com/user-attachments/assets/db5b3b01-1ead-44fa-8351-2d08f2ee6e18" />

**Hardware (please complete the following information):**
 - Bitaxe HW version: 601
 - ESP-Miner FW version: 2.15.0


## Comments

### mutatrum on 2026-08-23

Can you tell us something about your router and Wi-Fi setup? Do you have any of the following:
 * Mesh network
 * WPA2/WPA3 Mixed
 * 802.11w PMF (Protected Management Frames)
 * 802.11r / Fast BSS Transition

It seems when the firmware upgraded to be built on ESP-IDF 6.0.2, some things in the underlying Wi-Fi stack have been made more stringent.

### Freeben666 on 2026-08-23

Only thing of notice is my WiFi network has a mixed WPA2/WPA3 compatibility mode (single AP that is also the router and modem).
I have many devices connected to this WiFI network, some over a decade old, some very recent, none has a problem connecting. Neither did my Bitaxe prior to the latest update.

### WantClue on 2026-08-23

> Only thing of notice is my WiFi network has a mixed WPA2/WPA3 compatibility mode (single AP that is also the router and modem). I have many devices connected to this WiFI network, some over a decade old, some very recent, none has a problem connecting. Neither did my Bitaxe prior to the latest update.

Are you on our discord server so we could investigate this a bit further with you together and share a test binary to see if this resolves your issue? github doesn't allow the upload of binaries in comments. I could also create a branch for you and you download the binary from the artifacts if you prefer that

### bonifacio123 on 2026-08-23

I have a mix of Bitaxe (4) and NerdAxe (3) devices on WPA2, my Asus router has the option of WPA2/WPA3 so I changed to that to offer some feedback. All devices reconnected without issues. For Protected Management Pages, it's set to Capable out of (disabled, capable, required). Not on a mesh and don't see option 802.11r / Fast BSS Transition


### Freeben666 on 2026-08-23

> > Only thing of notice is my WiFi network has a mixed WPA2/WPA3 compatibility mode (single AP that is also the router and modem). I have many devices connected to this WiFI network, some over a decade old, some very recent, none has a problem connecting. Neither did my Bitaxe prior to the latest update.
> 
> Are you on our discord server so we could investigate this a bit further with you together and share a test binary to see if this resolves your issue? github doesn't allow the upload of binaries in comments. I could also create a branch for you and you download the binary from the artifacts if you prefer that

I initially tried going to https://osmu.bitaxe.org/ to go to the project's Discord, but the website seems to not exist anymore. And the Discord link on osmu.wiki leads to an expired Discord invite.

If you can give me a working link to the Discord, I'll gladly join you there :)

### WantClue on 2026-08-24

> > > Only thing of notice is my WiFi network has a mixed WPA2/WPA3 compatibility mode (single AP that is also the router and modem). I have many devices connected to this WiFI network, some over a decade old, some very recent, none has a problem connecting. Neither did my Bitaxe prior to the latest update.
> > 
> > 
> > Are you on our discord server so we could investigate this a bit further with you together and share a test binary to see if this resolves your issue? github doesn't allow the upload of binaries in comments. I could also create a branch for you and you download the binary from the artifacts if you prefer that
> 
> I initially tried going to https://osmu.bitaxe.org/ to go to the project's Discord, but the website seems to not exist anymore. And the Discord link on osmu.wiki leads to an expired Discord invite.
> 
> If you can give me a working link to the Discord, I'll gladly join you there :)

yes unfortunately this link expired. This one should work: https://discord.gg/hRk6cSyMm

### Freeben666 on 2026-08-24

Thanks, the link worked. I'm "Freeben"  on Discord. I'm in the CEST timezone (UTC+2), so 11:45PM right now. I'll be available most of the day tomorrow.
