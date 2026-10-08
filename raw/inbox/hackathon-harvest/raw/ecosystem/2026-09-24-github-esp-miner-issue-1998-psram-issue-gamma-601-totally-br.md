# bitaxeorg/ESP-Miner issue #1998: PSRAM issue? - Gamma 601 totally bricked after installing 2.15.3 - I have to upload esp-miner-factory-601-v2.4.5.bin but esp-miner-factory-601-v2.5.0.bin or more recent firmware do not work

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1998
> Collected: 2026-10-07
> Published: 2026-09-24

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1998
- State: closed
- Author: cezane822
- Opened: 2026-09-24
- Closed: 2026-09-28
- Labels: none

## Description

After updating the firmware by using the internal html page of bitaxe to v 2.15.3, my gamma 601 become irresponsive. My bitaxe was on a very old firmware. I have tried to flash a few factory firmware both using the bitaxe webpage and using the python commands as described at https://github.com/bitaxeorg/ESP-Miner.
No success. When I give power, the fan start running, but the display is totally blank and no wifi is available.

I am adding some logs obtained from the bitaxe flashing webpage: 
[bitaxe-logs-2026-09-24T19-35-50-059Z.txt](https://github.com/user-attachments/files/32630505/bitaxe-logs-2026-09-24T19-35-50-059Z.txt)
[bitaxe-logs-2026-09-24T19-42-11-764Z.txt](https://github.com/user-attachments/files/32630504/bitaxe-logs-2026-09-24T19-42-11-764Z.txt)
Does anyone can help me restoring my bitaxe to life? Thanks!

------------------------- More on this ---------------------
After several installations, I am able to install and run esp-miner-factory-601-v2.4.5.bin
When I try to install esp-miner-factory-601-v2.5.0.bin, the device becomes irresponsive apart for the fan spinning.
The same for more recent firmware.
It may be something to do with enabling PSRAM when my ESP chip does not have it?
Could someone fix it please?

## Comments

### mutatrum on 2026-09-26

Can you share what's written on the ESP32 module? It looks indeed like your device has an ESP module without PSRAM, then the latest version you can run is ~v2.4.5 if memory serves me right.~ my memory was not right, see below.

Alternative is to find someone in your area with a soldering iron and replace the ESP32 module, they're only a few bucks.

### cezane822 on 2026-09-27

Hi Mutatrum,
thanks for your reply. On my ESP32 chip: ESP32-S3-WROOM-1.
Yes I am running 2.4.5. As a home user-hobbist, do I miss something critical not updating?
Doing the substitution by soldering is not something I am able to do. Paying someone or learning and buying the equipment for soldering does not make sense given the effort/cost. 
Best,
cezanne822

### mutatrum on 2026-09-27

> On my ESP32 chip: ESP32-S3-WROOM-1.

Just to make 100% sure, are there any other markings on the module? 

This is an example of the correct one, with `MCN16R8` on the bottom:
<img width="406" alt="Image" src="https://github.com/user-attachments/assets/bc603dce-1412-4e2e-8897-188b78450719" />


This is a known wrong version, with `M0N16`. You can also see it's missing quite a lot of other markings, which most likely is a counterfeit module:
<img width="406" alt="Image" src="https://github.com/user-attachments/assets/dac67484-e0b1-4e38-ac83-fb42cab6b728" />

> Yes I am running 2.4.5. As a home user-hobbist, do I miss something critical not updating?

If it's hashing, it's hashing. We've added a lot of features to the firmware, but in the core that version is fine. Only do a module replacement if you can do it for cheap, either by a friend or a local repair-cafe or something like that.

### 1837Wine on 2026-09-28

@cezane822 

If your device has the MON16 variant of the ESP32-S3 IC you will be limited to v2.9.0 of the firmware, anything after that will cause problems as the MON16 variant does not have PSRAM.

### mutatrum on 2026-09-28

> If your device has the MON16 variant of the ESP32-S3 IC you will be limited to v2.9.0 of the firmware, anything after that will cause problems as the MON16 variant does not have PSRAM.

Yes, you are correct. Not sure why my brain got stuck on v2.4.5. You can indeed run v2.9.0, as long as you disable data logging on the settings tab:

<img width="461" height="205" alt="Image" src="https://github.com/user-attachments/assets/d8e9fe79-bc8a-4215-9cb4-4230abb19c19" />

### cezane822 on 2026-09-28

@mutatrum @1837Wine 
thanks for the useful info. I have discovered today that I have the ESP32 'counterfeit/wrong version' the one with the MON 16 label and missing marks. My chip is exactly as the image of the wrong version you posted. 
I bought from a recommended vendor by bitaxe, sigh



### mutatrum on 2026-09-29

> [@mutatrum](https://github.com/mutatrum) [@1837Wine](https://github.com/1837Wine) thanks for the useful info. I have discovered today that I have the ESP32 'counterfeit/wrong version' the one with the MON 16 label and missing marks. My chip is exactly as the image of the wrong version you posted. I bought from a recommended vendor by bitaxe, sigh

Contact the vendor. There was one small batch early on by bitronics where they accidentally used the wrong modules. If you got it from them please contact them. They have been helpful in fixing the issue for other people in the past. It's been a while now, so no guarantee but can't hurt to try.

### cezane822 on 2026-10-01

@mutatrum thanks for the suggestion to contact the seller. You are correct on their identity. So their first reply has been of denial. Their support service claims that the Bitaxe 601 can only work with firmware up to 2.4.5.  This reply happens even though I pointed them to this conversation on github. After having paid the Bitaxe 601 more than 250 Euros, the reply has been disappointing.
I have then requested they substitute their fault  Bitaxe 601 according to the 2 year EU consumer policy on faulty electronics. 
I hope the same experience does not happen to other Bitaxer fellows... 

Two days later - No reply from the vendor that is still listed as trusted on bitaxe web page...

Got a reply and a mail exchange over the weekend with the vendor: they are not available to replace the product even though it was built by them with a not compliant chipset.
