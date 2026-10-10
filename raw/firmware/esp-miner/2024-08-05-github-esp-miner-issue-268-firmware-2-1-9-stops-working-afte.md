# bitaxeorg/ESP-Miner issue #268: Firmware 2.1.9 stops working after several hours with "Serial RX Invalid 11" error

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/268
> Collected: 2026-10-07
> Published: 2024-08-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 268
- State: closed
- Author: HypeLaser
- Opened: 2024-08-05
- Closed: 2024-08-14
- Labels: none

## Description

After updating to 2.1.9, devices seemed to settle after an hour, running at or above their target hash.

However, at 8hrs in I noticed three of my four devices had dramatically dropped hash rates (80GHz or so) and the following error messages:

₿ (37720852) bm1366Module: Serial RX invalid 11
₿ (37720852) bm1366Module: 35 3e 3d 8f aa 55 8a 01 f3 6f 02 
₿ (37722862) bm1366Module: Serial RX invalid 11
₿ (37722862) bm1366Module: 43 69 13 82 aa 55 52 02 ba 55 01

All three of these devices were connected to the Public Pool address. The fourth, which is still running, is connected to Dutch.nl and seems fine.

Rebooting the devices has stopped the error, and the device operate as normal. I await the 8hr mark to see if the errors appear again, or if they appear on my fourth and last device.



## Comments

### skot on 2024-08-05

which hardware version is this? what power supply are you using?

### HypeLaser on 2024-08-05

1x Max, Board 204, Model BM1366
2x Supra, Board 401, Model BM1368

Using the power supplies that shipped with the devices. 

### HypeLaser on 2024-08-05

It took 38 minutes for the error to show again on one of the Supra's, and now I can also see the hash rate on the Max is wildly over...

<img width="864" alt="Screenshot 2024-08-05 at 23 41 58" src="https://github.com/user-attachments/assets/ce42caa5-2dae-4684-a3b4-432381db8db8">


### skot on 2024-08-05

there are many different power supplies depending on when and where you got your Bitaxe... can you give me some more details? I think this may be a power issue.

### skot on 2024-08-05

maybe you could also post a screenshot of the dashboard from all your devices when this problem is happening.


### HypeLaser on 2024-08-05

Power supply failures on three devices on the same day seems unlikely, but worth investigating for sure. All devices were bought from Bitcoin Merch, the Ultra (not Max!)  in Feb 2024 and the Supra's in March 2024.

### skot on 2024-08-05

(fwiw 204 is an ultra). How did you update the firmware on all these Bitaxe?

### HypeLaser on 2024-08-05

Thank you for letting me know it is an Ultra. It is confusing keeping across what the devices are.

I manually clicked the GitHub links on the devices internal page, on the Settings page. I updated the firmware and the website from the files that downloaded from GitHub.

<img width="1156" alt="Screenshot 2024-08-05 at 23 54 47" src="https://github.com/user-attachments/assets/1b62c771-d880-4512-a569-286f91b9ca58">


### skot on 2024-08-05

ok, you said only the public-pool.io pointed Bitaxe were giving you trouble. maybe this is related to a bug in handling pool outages (of which there were a couple today). I'll set up a 204 and 401 pointed to PP and see if I can reproduce this.

### HypeLaser on 2024-08-06

Just an overnight update.

The Dutch.nl Bitaxe is still running with no issues since upgrading to 2.1.9, and the three Public Pool have also run overnight since the reset with no issues.

I'm now suspecting the PP outage is what caused this, as you mentioned.

Out of curiosity, when PP came back online, should the devices have reconnected by themselves? 

### Georges760 on 2024-08-06

seeing the aa 55 in the middle of the frame, look like there was a desync of the framing.

### WantClue on 2024-08-06

I'll check on the last commits maybe some commit changes something unintentionally 

### HypeLaser on 2024-08-06

Two of the Public Pool devices have stopped hashing, same as before.

attached are the Dashboards, as requested. Same error "Serial RX invalid 11". These are both Supra's, board 401.

<img width="1112" alt="a" src="https://github.com/user-attachments/assets/fed38023-cd04-4d2c-bacf-e628ab2dcad9">
<img width="1125" alt="Screenshot 2024-08-06 at 19 17 40" src="https://github.com/user-attachments/assets/33f0d650-d21a-40f9-86cb-0766a418fc82">


Also. Clicking the RESTART button doesn't restart. The device goes offline and I cannot access it again without turning the power off and on again.



### Poncelas on 2024-08-07

Same issue here with the device in Public Pool. After some hours is showing 5234GH/s and not working. Restarted and worked again. Happened twice. Just bought it 1 day ago and updated to 2.1.9 

### jddebug on 2024-08-07

> Same issue here with the device in Public Pool. After some hours is showing 5234GH/s and not working. Restarted and worked again. Happened twice. Just bought it 1 day ago and updated to 2.1.9 

Same happening to me on my 6 devices 2.1.9

### skot on 2024-08-07

this just happened to me! BitaxeUltra 202 running v2.1.9 firmware. I have a suspicion that it happened with a public-pool outage overnight, but it's hard to know for sure. 2 other Bitaxes still running fine.

### skot on 2024-08-07

<img width="372" alt="image" src="https://github.com/user-attachments/assets/3762ef34-7a14-4c7c-9a88-6f71fd225e20">
this is the only indication from the dashboard, all other stats look good. Log shows tons of `Serial RX invalid 11`

```
₿ (149651229) bm1366Module: 9e aa 55 a8 00 51 94 02 55 05 dd
₿ (149651719) bm1366Module: Serial RX invalid 11
₿ (149651729) bm1366Module: 91 aa 55 08 00 68 4c 00 53 29 23
₿ (149653189) bm1366Module: Serial RX invalid 11
₿ (149653189) bm1366Module: 90 aa 55 70 02 0d 82 01 59 03 21
₿ (149653249) stratum_task: rx: {"id":null,"method":"mining.notify","params":["da1e63","4d9862332c27aaf3293856481f2ac7f71d6762c50001848e0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703ea0e0d5075626c69632d506f6f6c","ffffffff021d7df51200000000160014c64b1b9283ba1ea86bb9e7b696b0c8f68dad04000000000000000000266a24aa21a9ed4ca029d391eb165ea7dc0a0d4280ac260fd2ce2f86d678ff70640eeadeae0fed00000000",["f1cb32c85599d2c5a793b6ad6b11497f12c242e9055e3a312ebf1b62142d4e3a","e7d63762b78730203129046f64e1be4e4c077c67ad635fd7320306cdbfef9c23","1f7615138e4cc031c3d3139445a8f212b7e5c1c0c6d20d322b03fca02a404b63","cad7df613660d2b5c56650e1403e91d0fd96986fd7582b86bb7ed081b95ae7d9","3113d0a63c3ea791dcecbf6b46740341149f420aa1fc4fd4be49f8a21c8f026d","91167e0fb95a1638aa931b3de009a796417f835bc20899d792af0dca40348f99","109e75786424c730d25a3c58b1e431d0b7690dac7a55d2d5fd253a82f0d04be3","87a92f67ac5d54d85ffe7736e79812c7f761d7bbbde94907696bb2041fe7ef19","46fbd352426e8ff685452d9e7b1cb73e3ca9237d26b00727ff233305d714b27e","7b316f1cd2190e56cc885565ac56b76f3a25a283c8e45f6d378a9af8a2c3c857","b1caa3283a158982b4dd91e566ade8c6f36202a1e68ffdc28c25880d19898d14","afb0a547b132fdddc420539161ef884d941533032e7ca2f57bb5b4c20e97a99f"],"20000000","17031abe","66b39a61",false]}
₿ (149655149) create_jobs_task: New Work Dequeued da1e63
₿ (149656409) bm1366Module: Serial RX invalid 11
₿ (149656409) bm1366Module: 85 aa 55 c8 00 ef ce 00 66 5a 16
₿ (149660479) bm1366Module: Serial RX invalid 11
₿ (149660489) bm1366Module: 94 aa 55 74 00 9a ea 01 77 5f 77
₿ (149662859) bm1366Module: Serial RX invalid 11
₿ (149662859) bm1366Module: 96 aa 55 40 02 9f 4e 01 7d 7a 75
₿ (149663089) bm1366Module: Serial RX invalid 11
₿ (149663089) bm1366Module: 93 aa 55 32 01 d2 ae 02 7d 8a 75
₿ (149666159) bm1366Module: Serial RX invalid 11
₿ (149666159) bm1366Module: 81 aa 55 bc 03 2d 2d 02 0d 48 2d
₿ (149668049) bm1366Module: Serial RX invalid 11
₿ (149668049) bm1366Module: 97 aa 55 ca 02 6d 22 01 10 40 28
```



### skot on 2024-08-07

Got it! I blocked all network traffic to my bitaxe 401.. it kept hashing on generated work in the queue for a while, until the ASIC just stopped sending nonces. I re-enabled network traffic to the Bitaxe, and it started mining for a while, but then got borked. Here is right where it stopped working (raw rx bytes shown);
```
rx: [AA 55 52 00 30 25 00 91 00 B1 93]

I (62437861) bm1368Module: Job ID: 48, Core: 41/1, Ver: 00162000
I (62437861) asic_result: Ver: 20162000 Nonce 25300052 diff 0.0 of 1000.
rx: [AA 55 7A 01 76 B4 00 8B 0B DB 9A]

I (62437871) bm1368Module: Job ID: 40, Core: 61/11, Ver: 017B6000
I (62437881) asic_result: Ver: 217B6000 Nonce B476017A diff 0.0 of 1000.
rx: [53 04 5E 1B 2E 8F AA 55 6C 00 75]

I (62437891) bm1368Module: Serial RX invalid 11
I (62437901) bm1368Module: 53 04 5e 1b 2e 8f aa 55 6c 00 75 
rx: [CA 00 46 0C D6 86 AA 55 92 01 D2]

I (62437911) bm1368Module: Serial RX invalid 11
I (62437911) bm1368Module: ca 00 46 0c d6 86 aa 55 92 01 d2 
rx: [66 02 0C 28 20 9D AA 55 7A 02 EE]

I (62437921) bm1368Module: Serial RX invalid 11
I (62437931) bm1368Module: 66 02 0c 28 20 9d aa 55 7a 02 ee 
```

now the hashrate has gone wild; 
<img width="369" alt="image" src="https://github.com/user-attachments/assets/82f0731a-3401-4e88-9074-06e538d1785e">


### WantClue on 2024-08-07

So this might be cause by the dns lookup and missing handling 🤔

### Georges760 on 2024-08-08

> <img alt="image" width="372" src="https://private-user-images.githubusercontent.com/140785/355892720-3762ef34-7a14-4c7c-9a88-6f71fd225e20.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjMxMDc0MzIsIm5iZiI6MTcyMzEwNzEzMiwicGF0aCI6Ii8xNDA3ODUvMzU1ODkyNzIwLTM3NjJlZjM0LTdhMTQtNGM3Yy05YTg4LTZmNzFmZDIyNWUyMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwODA4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDgwOFQwODUyMTJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xMDI4MGJmY2EyNTg5ODEwMGUwM2I3NDY0YWZiYWVmMDJiOTk5ZjZkNWYxZDQ4MWFkMjIzYTg5YTBiMjQ3OTMzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.2D2H8uhxPEfbClaLFwr-vSHeSk0BbFTX1pRDE8Ks0wc"> this is the only indication from the dashboard, all other stats look good. Log shows tons of `Serial RX invalid 11`
> ```
> ₿ (149651229) bm1366Module: 9e aa 55 a8 00 51 94 02 55 05 dd
> ₿ (149651719) bm1366Module: Serial RX invalid 11
> ₿ (149651729) bm1366Module: 91 aa 55 08 00 68 4c 00 53 29 23
> ₿ (149653189) bm1366Module: Serial RX invalid 11
> ₿ (149653189) bm1366Module: 90 aa 55 70 02 0d 82 01 59 03 21
> ₿ (149653249) stratum_task: rx: {"id":null,"method":"mining.notify","params":["da1e63","4d9862332c27aaf3293856481f2ac7f71d6762c50001848e0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703ea0e0d5075626c69632d506f6f6c","ffffffff021d7df51200000000160014c64b1b9283ba1ea86bb9e7b696b0c8f68dad04000000000000000000266a24aa21a9ed4ca029d391eb165ea7dc0a0d4280ac260fd2ce2f86d678ff70640eeadeae0fed00000000",["f1cb32c85599d2c5a793b6ad6b11497f12c242e9055e3a312ebf1b62142d4e3a","e7d63762b78730203129046f64e1be4e4c077c67ad635fd7320306cdbfef9c23","1f7615138e4cc031c3d3139445a8f212b7e5c1c0c6d20d322b03fca02a404b63","cad7df613660d2b5c56650e1403e91d0fd96986fd7582b86bb7ed081b95ae7d9","3113d0a63c3ea791dcecbf6b46740341149f420aa1fc4fd4be49f8a21c8f026d","91167e0fb95a1638aa931b3de009a796417f835bc20899d792af0dca40348f99","109e75786424c730d25a3c58b1e431d0b7690dac7a55d2d5fd253a82f0d04be3","87a92f67ac5d54d85ffe7736e79812c7f761d7bbbde94907696bb2041fe7ef19","46fbd352426e8ff685452d9e7b1cb73e3ca9237d26b00727ff233305d714b27e","7b316f1cd2190e56cc885565ac56b76f3a25a283c8e45f6d378a9af8a2c3c857","b1caa3283a158982b4dd91e566ade8c6f36202a1e68ffdc28c25880d19898d14","afb0a547b132fdddc420539161ef884d941533032e7ca2f57bb5b4c20e97a99f"],"20000000","17031abe","66b39a61",false]}
> ₿ (149655149) create_jobs_task: New Work Dequeued da1e63
> ₿ (149656409) bm1366Module: Serial RX invalid 11
> ₿ (149656409) bm1366Module: 85 aa 55 c8 00 ef ce 00 66 5a 16
> ₿ (149660479) bm1366Module: Serial RX invalid 11
> ₿ (149660489) bm1366Module: 94 aa 55 74 00 9a ea 01 77 5f 77
> ₿ (149662859) bm1366Module: Serial RX invalid 11
> ₿ (149662859) bm1366Module: 96 aa 55 40 02 9f 4e 01 7d 7a 75
> ₿ (149663089) bm1366Module: Serial RX invalid 11
> ₿ (149663089) bm1366Module: 93 aa 55 32 01 d2 ae 02 7d 8a 75
> ₿ (149666159) bm1366Module: Serial RX invalid 11
> ₿ (149666159) bm1366Module: 81 aa 55 bc 03 2d 2d 02 0d 48 2d
> ₿ (149668049) bm1366Module: Serial RX invalid 11
> ₿ (149668049) bm1366Module: 97 aa 55 ca 02 6d 22 01 10 40 28
> ```

here the aa 55 that should be at the begining of the frame is sifted by 1

### Georges760 on 2024-08-08

> Got it! I blocked all network traffic to my bitaxe 401.. it kept hashing on generated work in the queue for a while, until the ASIC just stopped sending nonces. I re-enabled network traffic to the Bitaxe, and it started mining for a while, but then got borked. Here is right where it stopped working (raw rx bytes shown);
> 
> ```
> rx: [AA 55 52 00 30 25 00 91 00 B1 93]
> 
> I (62437861) bm1368Module: Job ID: 48, Core: 41/1, Ver: 00162000
> I (62437861) asic_result: Ver: 20162000 Nonce 25300052 diff 0.0 of 1000.
> rx: [AA 55 7A 01 76 B4 00 8B 0B DB 9A]
> 
> I (62437871) bm1368Module: Job ID: 40, Core: 61/11, Ver: 017B6000
> I (62437881) asic_result: Ver: 217B6000 Nonce B476017A diff 0.0 of 1000.
> rx: [53 04 5E 1B 2E 8F AA 55 6C 00 75]
> 
> I (62437891) bm1368Module: Serial RX invalid 11
> I (62437901) bm1368Module: 53 04 5e 1b 2e 8f aa 55 6c 00 75 
> rx: [CA 00 46 0C D6 86 AA 55 92 01 D2]
> 
> I (62437911) bm1368Module: Serial RX invalid 11
> I (62437911) bm1368Module: ca 00 46 0c d6 86 aa 55 92 01 d2 
> rx: [66 02 0C 28 20 9D AA 55 7A 02 EE]
> 
> I (62437921) bm1368Module: Serial RX invalid 11
> I (62437931) bm1368Module: 66 02 0c 28 20 9d aa 55 7a 02 ee 
> ```
> 
> now the hashrate has gone wild; <img alt="image" width="369" src="https://private-user-images.githubusercontent.com/140785/355906795-82f0731a-3401-4e88-9074-06e538d1785e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjMxMDc0MzIsIm5iZiI6MTcyMzEwNzEzMiwicGF0aCI6Ii8xNDA3ODUvMzU1OTA2Nzk1LTgyZjA3MzFhLTM0MDEtNGU4OC05MDc0LTA2ZTUzOGQxNzg1ZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwODA4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDgwOFQwODUyMTJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01MDc1MjIyYmE3ZDdlM2NhZmMwYTAzNDI1YTdmOGFjZTU1ZjZjY2RlY2FhY2E5OTA3YmU0ZjFhYjRmYThlY2M5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.9MPIRmbl2qoNCvslu_ZZtIO1I1UoEYC7xUderxI7Pm8">

and here shifted by 6

### Georges760 on 2024-08-08

from a random Saleae Captre of a BM1368 (thanks for the yesterday donator!) I can see this kind of Nonce sent by the chip

![image](https://github.com/user-attachments/assets/2108df79-3e87-4eed-bf6b-b556ebcbecc1)

For whatever reason chip randomly sent a frame with 1 extra byte (all other 10k+ nonce frame have the good lenght)

So if this happen, current ESP-Miner which is framing the RX with a fixed size of frame, will never resync to the aa 55.




### skot on 2024-08-08

I made a change to the serial parser in BM1366.c and BM1368.c so that it flushes the buffer after any invalid serial RX (ie doesn't start with AA 55). From my testing so far it seems to be working. https://github.com/skot/ESP-Miner/tree/serialrx11_fix

I also have been keeping an eye on the size of the serial buffer. it seems like at some point esp-miner stops emptying the ESP32 serial RX buffer.. need to figure out why that happens.

### skot on 2024-08-10

I added a fix for this and some other memory leaks in https://github.com/skot/ESP-Miner/tree/219-leak_hunting

[esp-miner.bin.zip](https://github.com/user-attachments/files/16568476/esp-miner.bin.zip)

give it a try and see how it holds up!

### HypeLaser on 2024-08-10

> I added a fix for this and some other memory leaks in https://github.com/skot/ESP-Miner/tree/219-leak_hunting
> 
> [esp-miner.bin.zip](https://github.com/user-attachments/files/16568476/esp-miner.bin.zip)
> 
> give it a try and see how it holds up!

Thank you for your efforts. I have updated the firmware to your version above, and will keep an eye and see what happens.

### HypeLaser on 2024-08-11

Update: So far run for 24hrs with no reboots and no Serial RX errors.

### HypeLaser on 2024-08-12

Further update: The three devices connected to Public Pool are still running, however the one connected to Dutch.nl has got stuck and I had to reset it . The logs only show "http_server: Handshake done, the new connection was opened".

Also, as a side note, the three Public Pool devices have been running solidly for over two days. But I've noticed they're not hitting difficulties any higher than 44 million. Nonce issue?
