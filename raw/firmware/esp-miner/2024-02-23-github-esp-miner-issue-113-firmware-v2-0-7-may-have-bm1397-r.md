# bitaxeorg/ESP-Miner issue #113: Firmware V2.0.7 may have BM1397 regression

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/113
> Collected: 2026-10-07
> Published: 2024-02-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 113
- State: closed
- Author: xXAsystolieXx
- Opened: 2024-02-23
- Closed: 2024-03-15
- Labels: bug

## Description

Hi everyone, as described in the title, I updated to firmware 2.0.7. Now I only get a 1 with shares accepted but nothing else happens to. I downgrade again to 2.0.6 everything works as it should🤷🏼‍♂️. 

![PXL_20240223_091024847](https://github.com/skot/ESP-Miner/assets/161015184/3cb95f15-7057-458d-b780-d09bed3aced8)

Low Voltage is shown in the picture because I connected the Bitaxe via USB cable. With the right power cable, this is no longer there. I hope you can help me and I can do the whole thing because I am an absolute beginner and I googled everything I've done so far🤣

## Comments

### xXAsystolieXx on 2024-02-23

![PXL_20240223_092837015](https://github.com/skot/ESP-Miner/assets/161015184/d64cf0b2-3116-4da9-9346-c19456dfc31f)

This is what it looks like with a downgrade after a few seconds 


### xXAsystolieXx on 2024-02-23

![PXL_20240223_095230786 MP](https://github.com/skot/ESP-Miner/assets/161015184/1c378766-a5c2-46ad-8838-2ae3469731da)

And this is what the realtime log looks like on version 2.0.7

### xXAsystolieXx on 2024-02-23

![PXL_20240223_095421549](https://github.com/skot/ESP-Miner/assets/161015184/a45561be-f4dc-4c58-ac83-e277ca717fc3)

12 Minuten auf Version 2.0.7  und eine Hashrate von 0

### jddebug on 2024-02-23

Have you tried stock voltage (1200) and stock frequency (485)? I suspect it might work well on 2.0.7 if you do.

### xXAsystolieXx on 2024-02-23

Yes, I've already tried it but without success

### xXAsystolieXx on 2024-02-23

The Stock value for bm1397 is 1400

### jddebug on 2024-02-23

I have BM1366. It will not work over 60C. Could this be a similar issue with yours?

### skot on 2024-02-23

Which hardware do you have? You say 1366, but the AxeOS says 1397. If that's true it's not going to work.

### jddebug on 2024-02-23

OP said he has the 1397. I have the 1366. I didn't realize the OP had a different hardware than I do.

### xXAsystolieXx on 2024-02-23

I have the BM1397. It has been 60 ° and more since I got the Bitaxe

### xXAsystolieXx on 2024-02-23

Why? Does 2.0.7 not work with the BM1397?

### pinokio240 on 2024-02-28

> bm1397

I also have a problem with it (bm1397), now it’s just like that, it’s a waste of money, I tried rolling back to the old firmware to no avail

### xXAsystolieXx on 2024-02-28

@pinokio240 How did you make the rollback? 

### pinokio240 on 2024-02-28

@xXAsystolieXx 
> @pinokio240 How did you make the rollback?

I flashed earlier firmware with the programmer

### xXAsystolieXx on 2024-02-28

Ok that's strange. I also flashed it over the terminal and it works for me: /

### xXAsystolieXx on 2024-02-28

B But I don't get 2.0.7 to work ... 

### pinokio240 on 2024-02-28

@xXAsystolieXx 
And earlier firmwares do not work correctly with pools or there is a problem with a power supply error, like yours. $100 down the drain. There was no need to update the firmware(((

### pinokio240 on 2024-02-28

@xXAsystolieXx  It falls in love with me, but constantly the nutrition error flies away at the same time as a post -pushing to the network, and nourish from the labator power supply and especially the voltage even up to 5.2 volts lifted it - it did not fall. Not correctly working

### xXAsystolieXx on 2024-02-28

@pinokio240 That sounds like a defective circuit board to me. With 2.0.6 I have no problems with the pool

### qubyt3 on 2024-02-28

@xXAsystolieXx  Can you take a picture of your board, and tell us what steps you took to upgrade the firmware? 

### xXAsystolieXx on 2024-02-28

@

> @xXAsystolieXx Can you take a picture of your board, and tell us what steps you took to upgrade the firmware?

I can only take a photo later, I'm still on the way. But I connected my board to my PC via USB and with the Bitaxetool command I then flashed the firmware

### xXAsystolieXx on 2024-02-28

bitaxetool --config ./config.cvs --firmware ./esp-miner-factory-v2.0.7.bin



### xXAsystolieXx on 2024-02-28

key,type,encoding,value
main,namespace,,
asicfrequency,data,u16,475
asicvoltage,data,u16,1400
asicmodel,data,string,BM1397
devicemodel,data,string,max
boardversion,data,string,2.2

These are the parameters I am in theconfig.cvshave deposited                                                                

### FragOmatig on 2024-02-28

Hey 👋 
 
 same Problem with my Bitaxe Ultra 1366 😭
Board 204
Firmware v2.0.7 
Chip: BM1366AL 

Voltage is good, no warning. Temp 35 crad.

only 1 share no hash …..
firmware new flashed, but nothing same Problem.
Canot rollback…



### xXAsystolieXx on 2024-02-28

Then I can be happy that I could flash back to 2.0.6 🫤 But good to know that I'm not the only one with this problem 

### qubyt3 on 2024-02-28

@xXAsystolieXx No problem when you get back, send a picture of your device (front/back). 

Instead of using bitaxetool to update your Bitaxe can you try upgrading with Wantclue new web flasher instead: 

https://wantclue.github.io/bitaxe-web-flasher/. (follow the easy instructions)

Note: Once you are done, disconnect the usb cable. Go to your wifi networks, connect to Bitaxe_XXXX, and re-enter your wifi ssid/password, stratum url/ port/ user/ password. 
Click Save then click reboot. 



### xXAsystolieXx on 2024-02-28

@qubyt3 I've already tried the web flasher, but this was also unsuccessful😅

### qubyt3 on 2024-02-28

@xXAsystolieXx  sorry to hear that, still curious to see the pictures of the Bitaxe when you get back to confirm the board version you have, and what's compatible. 

In any case another observation from your first screen shot, the wattage is to low (0.18 mV) and amperage seems way off (81,879 mA).
I'm wondering maybe if the power supply has an issue? Have you tried another 5v, 4amp PSU?



### pinokio240 on 2024-02-28




> @xXAsystolieXx No problem when you get back, send a picture of your device (front/back).
> 
> Instead of using bitaxetool to update your Bitaxe can you try upgrading with Wantclue new web flasher instead:
> 
> https://wantclue.github.io/bitaxe-web-flasher/. (follow the easy instructions)
> 
> Note: Once you are done, disconnect the usb cable. Go to your wifi networks, connect to Bitaxe_XXXX, and re-enter your wifi ssid/password, stratum url/ port/ user/ password. Click Save then click reboot.

Didn't help https://wantclue.github.io/bitaxe-web-flasher/

### FragOmatig on 2024-02-28

I tried another power supply and web flasher. No way… 

### xXAsystolieXx on 2024-02-28

@qubyt3 The 0.18 watts were only displayed because I had the Bitaxe for flashing via USB on the PC. There was no power plug connected only the USB cable. 

### pinokio240 on 2024-02-28

![ver_win](https://github.com/skot/ESP-Miner/assets/37944152/4ab50daa-9428-486a-ad81-34dddf8aa50e)
I've finished everything. Probably the power chip has died completely. And what microcircuit should I look for now? Power supply included

### qubyt3 on 2024-02-28

@pinokio240 In your case I think you just din't load the firmware correctly based on the version being displayed. Don't lose hope just yet :P 

### MyOwn2C on 2024-02-28

> ![ver_win](https://private-user-images.githubusercontent.com/37944152/308673600-4ab50daa-9428-486a-ad81-34dddf8aa50e.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDkxNDYyNTIsIm5iZiI6MTcwOTE0NTk1MiwicGF0aCI6Ii8zNzk0NDE1Mi8zMDg2NzM2MDAtNGFiNTBkYWEtOTQyOC00ODZhLWFkODEtMzRkZGRmOGFhNTBlLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjI4VDE4NDU1MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWRlYmQ1N2RhOGY2ODE0MmUzYjhiZTc0OGRjYjY1ZGE2MjFhYTFiYjdlZDMwMTQ1ODJlOTM3NzQxZjVkYTc4ODQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.a3V_WCOaQFGIgH58H8eq6g2Su8DWyljaCrbI2ji8oRI) I've finished everything. Probably the power chip has died completely. And what microcircuit should I look for now? Power supply included

Before you replace anything, try shorting J7 if you have U8 installed. 
<img width="387" alt="image" src="https://github.com/skot/ESP-Miner/assets/158797249/7a7a5ae3-370c-4f60-b202-c33f6ec5aaba">



### qubyt3 on 2024-02-28

For the other folks its time to gather some logs and share it here. 

Open Wantclue Bitaxe web installer, select your device and connect. https://wantclue.github.io/bitaxe-web-flasher/
Click on Logs & Console
Click on Reset Device
Copy paste everything below, until an error appears or whatever loop it's stuck in: 
Example: 
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0x15 (USB_UART_CHIP_RESET),boot:0x2a (SPI_FAST_FLASH_BOOT)
....etc! 

### xXAsystolieXx on 2024-02-28

![PXL_20240228_184652221 MP](https://github.com/skot/ESP-Miner/assets/161015184/5b06669f-d320-4dfe-be4b-aba5791b5f6e)
![PXL_20240228_184735622](https://github.com/skot/ESP-Miner/assets/161015184/c60097b1-2c46-4620-9f97-733b3660432d)



### pinokio240 on 2024-02-28

> @pinokio240 В вашем случае, я думаю, вы просто неправильно загрузили прошивку в зависимости от отображаемой версии. Пока не теряйте надежды: P

Honestly, I'm already tired. Now there is another problem: after flashing the miner when the power is turned off, the miner does not start. Shows the network to connect to and the PC does not connect to it.
  Okay, I'll try to look and jump if there is a takach microcircuit

### qubyt3 on 2024-02-28

@pinokio240 your Bitaxe firmware is not loaded correctly, don't jump anything. 
Don't for forget you need to hold and press the BOOT button on your Bitaxe, before plugging it in, in order to enable the flash mode. Then connect and follow the rest of the steps to update. 

Once you are done, you need to connect to the Bitaxe wifi (Bitaxe_XXXX), and re-enter your wifi ssid/password, stratum url/ port/ user/ password. Save and restart. Connect back to your wifi and then you can access to AxeOS web page.


### xXAsystolieXx on 2024-02-28

₿ (93777) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e571c1","30754f29d0feabf790a01894936f5dbcf9eae316000002790000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703b4b30c5075626c69632d506f6f6c","ffffffff02625e362900000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9ed447c55d487ca079f6106d09d44e943bb0d83f4b4590d4ccfaa81c66232db20c000000000",["1f2b5c5747883c21f8e1d12065f3c43f7638a6f1466c8b5b331d5fccf26709e4","f0c39f75b987c8854579d1ca079bbbe24965f1ebd11c6db0bb3801521f815ce5","5a0581d87c3139bc5f08a33aa48555186b4ab1f5698eb4509b9fbd50f0167861","f0fc867115edf5b17127444024e6d4b81f6eb9a245ff38cbf3db3bfdd29321f2","81229b0e848b2f8475806d2eb37d38cf4d3a3678996015229d9ebca97630016c","7a76119b219e4c9361b196023fca93696e0a3c71eca8c5b090efdd2218b19496","9182a2ff8c7d802a3a96b13606bd1c0017735ded457ca4eec5b93b6d541737cd","d27fb4b11c3a7c607548255a301aa75eeb75c9db68d79c660a466587b3e56aa7","65e6a5083eb402e16a9c6d6ea0335ef6e3268bad478481552becfa2d8e9a5cb7","6f14ea48f7ea342d1a80f00c985581613d4968c6101090d9e2b74f6106ce034d","ccd993e781d6b8e4b0749bdfc299468894418ee9d6c1437231820a85d306bdec"],"20000000","170371b1","65df84a1",false]}
₿ (93887) create_jobs_task: New Work Dequeued e571c1
₿ (124197) bm1397Module: return null
₿ (125207) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[8]}
₿ (125217) stratum_task: Set stratum difficulty: 8
₿ (125617) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e575fc","30754f29d0feabf790a01894936f5dbcf9eae316000002790000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703b4b30c5075626c69632d506f6f6c","ffffffff02625e362900000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9ed447c55d487ca079f6106d09d44e943bb0d83f4b4590d4ccfaa81c66232db20c000000000",["1f2b5c5747883c21f8e1d12065f3c43f7638a6f1466c8b5b331d5fccf26709e4","f0c39f75b987c8854579d1ca079bbbe24965f1ebd11c6db0bb3801521f815ce5","5a0581d87c3139bc5f08a33aa48555186b4ab1f5698eb4509b9fbd50f0167861","f0fc867115edf5b17127444024e6d4b81f6eb9a245ff38cbf3db3bfdd29321f2","81229b0e848b2f8475806d2eb37d38cf4d3a3678996015229d9ebca97630016c","7a76119b219e4c9361b196023fca93696e0a3c71eca8c5b090efdd2218b19496","9182a2ff8c7d802a3a96b13606bd1c0017735ded457ca4eec5b93b6d541737cd","d27fb4b11c3a7c607548255a301aa75eeb75c9db68d79c660a466587b3e56aa7","65e6a5083eb402e16a9c6d6ea0335ef6e3268bad478481552becfa2d8e9a5cb7","6f14ea48f7ea342d1a80f00c985581613d4968c6101090d9e2b74f6106ce034d","ccd993e781d6b8e4b0749bdfc299468894418ee9d6c1437231820a85d306bdec"],"20000000","170371b1","65df84a1",false]}
₿ (125727) create_jobs_task: New Work Dequeued e575fc
₿ (125857) bm1397Module: Setting job ASIC mask to 7
₿ (154807) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e57613","30754f29d0feabf790a01894936f5dbcf9eae316000002790000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703b4b30c5075626c69632d506f6f6c","ffffffff02625e362900000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9ed447c55d487ca079f6106d09d44e943bb0d83f4b4590d4ccfaa81c66232db20c000000000",["1f2b5c5747883c21f8e1d12065f3c43f7638a6f1466c8b5b331d5fccf26709e4","f0c39f75b987c8854579d1ca079bbbe24965f1ebd11c6db0bb3801521f815ce5","5a0581d87c3139bc5f08a33aa48555186b4ab1f5698eb4509b9fbd50f0167861","f0fc867115edf5b17127444024e6d4b81f6eb9a245ff38cbf3db3bfdd29321f2","81229b0e848b2f8475806d2eb37d38cf4d3a3678996015229d9ebca97630016c","7a76119b219e4c9361b196023fca93696e0a3c71eca8c5b090efdd2218b19496","9182a2ff8c7d802a3a96b13606bd1c0017735ded457ca4eec5b93b6d541737cd","d27fb4b11c3a7c607548255a301aa75eeb75c9db68d79c660a466587b3e56aa7","65e6a5083eb402e16a9c6d6ea0335ef6e3268bad478481552becfa2d8e9a5cb7","6f14ea48f7ea342d1a80f00c985581613d4968c6101090d9e2b74f6106ce034d","ccd993e781d6b8e4b0749bdfc299468894418ee9d6c1437231820a85d306bdec"],"20000000","170371b1","65df84dd",false]}
₿ (154917) create_jobs_task: New Work Dequeued e57613
₿ (184197) bm1397Module: return null
₿ (185217) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[1]}
₿ (185217) stratum_task: Set stratum difficulty: 1
₿ (185627) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e57a50","30754f29d0feabf790a01894936f5dbcf9eae316000002790000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703b4b30c5075626c69632d506f6f6c","ffffffff02625e362900000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9ed447c55d487ca079f6106d09d44e943bb0d83f4b4590d4ccfaa81c66232db20c000000000",["1f2b5c5747883c21f8e1d12065f3c43f7638a6f1466c8b5b331d5fccf26709e4","f0c39f75b987c8854579d1ca079bbbe24965f1ebd11c6db0bb3801521f815ce5","5a0581d87c3139bc5f08a33aa48555186b4ab1f5698eb4509b9fbd50f0167861","f0fc867115edf5b17127444024e6d4b81f6eb9a245ff38cbf3db3bfdd29321f2","81229b0e848b2f8475806d2eb37d38cf4d3a3678996015229d9ebca97630016c","7a76119b219e4c9361b196023fca93696e0a3c71eca8c5b090efdd2218b19496","9182a2ff8c7d802a3a96b13606bd1c0017735ded457ca4eec5b93b6d541737cd","d27fb4b11c3a7c607548255a301aa75eeb75c9db68d79c660a466587b3e56aa7","65e6a5083eb402e16a9c6d6ea0335ef6e3268bad478481552becfa2d8e9a5cb7","6f14ea48f7ea342d1a80f00c985581613d4968c6101090d9e2b74f6106ce034d","ccd993e781d6b8e4b0749bdfc299468894418ee9d6c1437231820a85d306bdec"],"20000000","170371b1","65df84dd",false]}
₿ (185737) create_jobs_task: New Work Dequeued e57a50
₿ (185867) bm1397Module: Setting job ASIC mask to 0
₿ (213787) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e57a61","30754f29d0feabf790a01894936f5dbcf9eae316000002790000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703b4b30c5075626c69632d506f6f6c","ffffffff02625e362900000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9ed447c55d487ca079f6106d09d44e943bb0d83f4b4590d4ccfaa81c66232db20c000000000",["1f2b5c5747883c21f8e1d12065f3c43f7638a6f1466c8b5b331d5fccf26709e4","f0c39f75b987c8854579d1ca079bbbe24965f1ebd11c6db0bb3801521f815ce5","5a0581d87c3139bc5f08a33aa48555186b4ab1f5698eb4509b9fbd50f0167861","f0fc867115edf5b17127444024e6d4b81f6eb9a245ff38cbf3db3bfdd29321f2","81229b0e848b2f8475806d2eb37d38cf4d3a3678996015229d9ebca97630016c","7a76119b219e4c9361b196023fca93696e0a3c71eca8c5b090efdd2218b19496","9182a2ff8c7d802a3a96b13606bd1c0017735ded457ca4eec5b93b6d541737cd","d27fb4b11c3a7c607548255a301aa75eeb75c9db68d79c660a466587b3e56aa7","65e6a5083eb402e16a9c6d6ea0335ef6e3268bad478481552becfa2d8e9a5cb7","6f14ea48f7ea342d1a80f00c985581613d4968c6101090d9e2b74f6106ce034d","ccd993e781d6b8e4b0749bdfc299468894418ee9d6c1437231820a85d306bdec"],"20000000","170371b1","65df8519",false]}
₿ (213897) create_jobs_task: New Work Dequeued e57a61

### xXAsystolieXx on 2024-02-28

there is my log with Firmware 2.0.7

### xXAsystolieXx on 2024-02-28

@qubyt3 

### pinokio240 on 2024-02-28

> @pinokio240 your Bitaxe firmware is not loaded correctly, don't jump anything. Don't for forget you need to hold and press the BOOT button on your Bitaxe, before plugging it in, in order to enable the flash mode. Then connect and follow the rest of the steps.

I don’t have this button, I’m flashing it through the ESPprog programmer. I'll send you photos
![y8nMogE5k3E](https://github.com/skot/ESP-Miner/assets/37944152/7eda862e-2c0a-4054-829f-c93907122b4b)
![Z-GZ3ZWpSSw](https://github.com/skot/ESP-Miner/assets/37944152/0e83c6e1-63f5-4dbf-9092-b9111354c22c)

https://wantclue.github.io/bitaxe-web-flasher/
The device does not respond to reset.
Select your Bitaxe-Model: Bitaxe Max
e: In EFUSE_BLK2__DATA4_REG is used 8 bits starting with 21 bit
D (679) efuse: In EFUSE_BLK2__DATA4_REG is used 3 bits starting with 29 bit
D (686) efuse: In EFUSE_BLK2__DATA5_REG is used 3 bits starting with 0 bit
D (693) efuse: In EFUSE_BLK2__DATA5_REG is used 6 bits starting with 3 bit
D (700) efuse: In EFUSE_BLK2__DATA5_REG is used 6 bits starting with 9 bit
D (707) efuse: In EFUSE_BLK2__DATA4_REG is used 2 bits starting with 0 bit
D (714) efuse: In EFUSE_BLK2__DATA4_REG is used 8 bits starting with 21 bit
D (721) efuse: In EFUSE_BLK2__DATA4_REG is used 3 bits starting with 29 bit
D (728) efuse: In EFUSE_BLK2__DATA5_REG is used 3 bits starting with 0 bit
Terminal disconnected: BufferOverrunError: Buffer overrun


j7 included:

pscreen 2
D (1804) nvs: nvs_close 13
D (1804) nvs: nvs_open_from_partition main 0
D (1804) nvs: nvs_get invertscreen 2
I (1814) wifi station: ESP_WIFI_MODE_STA
I (1814) SystemModule: OLED init success!
D (1824) esp_netif_objects: esp_netif_add_to_list 0x3fcb34f0
D (1824) esp_netif_objects: esp_netif_add_to_list netif added successfully (total netifs: 2)
Guru Meditation Error: Core  0 panic'ed (LoadProhibited). Exception was unhandled.

Core  0 register dump:
PC      : 0x4005544e  PS      : 0x00060f30  A0      : 0x8203b43f  A1      : 0x3fca8ba0  
A2      : 0x3c0b7250  A3      : 0x00000000  A4      : 0x00000200  A5      : 0x3fc9e574  
Terminal disconnected: BufferOverrunError: Buffer overrun

### qubyt3 on 2024-02-28

@xXAsystolieXx  Interesting, can you copy/paste the log when the Bitaxe initialize until it first attempts to hash?



### qubyt3 on 2024-02-28

> **[pinokio240](/pinokio240) ** c

Oh I thought you had another board version, then try and flash it again with 2.0.7. 

### xXAsystolieXx on 2024-02-28

@qubyt3 That is the problem, he stays in this loop. The bitaxe does not start to hash

### pinokio240 on 2024-02-28

@qubyt3  @19201003080114 

[esp-web-tools-logs.txt](https://github.com/skot/ESP-Miner/files/14439125/esp-web-tools-logs.txt)
This is a log with the latest firmware version v2.0.7. Jumper j7 is enabled, the miner reboots itself

### xXAsystolieXx on 2024-02-28

![PXL_20240228_193003132](https://github.com/skot/ESP-Miner/assets/161015184/033fb644-0606-43d5-86ee-1731a6c3739d)


### qubyt3 on 2024-02-28

@pinokio240 Wonder why its dropping the socket...hmmm. 

Can you try connecting to solo.ckpool.org port 3333 or public-pool.io port 21496? 

### qubyt3 on 2024-02-28

@xXAsystolieXx okay, from the log and screen you sent we're curious to see what the logs says when it initializes.
Open Wantclue Bitaxe web installer, https://wantclue.github.io/bitaxe-web-flasher/ . 
select your device and connect. 
Click on Logs & Console
Click on Reset Device

Start the copy/paste from the first line of the initialization: line 1 = ESP-ROM:esp32s3-20210327

### pinokio240 on 2024-02-28

> @pinokio240 Wonder why its dropping the socket...hmmm.
> 
> Can you try connecting to solo.ckpool.org port 3333 or public-pool.io port 21496?

sha256.auto.nicehash.com port 9200  

### qubyt3 on 2024-02-28

@pinokio240 I can see you try and connect to sha256.auto.nicehash.com port 9200, try connecting to public-pool.io port 21496 and see if the issue follows

### xXAsystolieXx on 2024-02-28

I (27137) wifi:bcn_timeout,ap_probe_send_start
I (36187) wifi:bcn_timeout,ap_probe_send_start
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0x15 (USB_UART_CHIP_RESET),boot:0x2a (SPI_FAST_FLASH_BOOT)
Saved PC:0x4037b8b2
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce3818,len:0x16e0
load:0x403c9700,len:0x4
load:0x403c9704,len:0xc00
load:0x403cc700,len:0x2eb0
entry 0x403c9908
I (27) boot: ESP-IDF v5.1 2nd stage bootloader
I (27) boot: compile time Jan 20 2024 20:00:30
I (27) boot: Multicore bootloader
I (30) boot: chip revision: v0.2
I (34) boot.esp32s3: Boot SPI Speed : 80MHz
I (38) boot.esp32s3: SPI Mode       : DIO
I (43) boot.esp32s3: SPI Flash Size : 16MB
I (48) boot: Enabling RNG early entropy source...
I (53) boot: Partition Table:
I (57) boot: ## Label            Usage          Type ST Offset   Length
I (64) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (72) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (79) boot:  2 factory          factory app      00 00 00010000 00400000
I (87) boot:  3 www              Unknown data     01 82 00410000 00300000
I (94) boot:  4 ota_0            OTA app          00 10 00710000 00400000
I (101) boot:  5 ota_1            OTA app          00 11 00b10000 00400000
I (109) boot:  6 otadata          OTA data         01 00 00f10000 00002000
I (117) boot:  7 coredump         Unknown data     01 03 00f12000 00010000
I (124) boot: End of partition table
I (128) boot: Defaulting to factory image
I (133) esp_image: segment 0: paddr=00010020 vaddr=3c0b0020 size=29e94h (171668) map
I (172) esp_image: segment 1: paddr=00039ebc vaddr=3fc98100 size=04bbch ( 19388) load
I (177) esp_image: segment 2: paddr=0003ea80 vaddr=40374000 size=01598h (  5528) load
I (180) esp_image: segment 3: paddr=00040020 vaddr=42000020 size=a62e0h (680672) map
I (309) esp_image: segment 4: paddr=000e6308 vaddr=40375598 size=12b54h ( 76628) load
I (335) boot: Loaded app from partition at offset 0x10000
I (335) boot: Disabling RNG early entropy source...
I (346) cpu_start: Multicore app
I (347) cpu_start: Pro cpu up.
I (347) cpu_start: Starting app cpu, entry point is 0x40375584
I (0) cpu_start: App cpu up.
I (365) cpu_start: Pro cpu start user code
I (365) cpu_start: cpu freq: 160000000 Hz
I (365) cpu_start: Application information:
I (368) cpu_start: Project name:     esp-miner
I (373) cpu_start: App version:      v2.0.7
I (378) cpu_start: Compile time:     Jan 20 2024 19:59:47
I (384) cpu_start: ELF file SHA256:  c148b21719898fc7...
I (390) cpu_start: ESP-IDF:          v5.1
I (395) cpu_start: Min chip rev:     v0.0
I (399) cpu_start: Max chip rev:     v0.99 
I (404) cpu_start: Chip rev:         v0.2
I (409) heap_init: Initializing. RAM available for dynamic allocation:
I (416) heap_init: At 3FCA2050 len 000476C0 (285 KiB): DRAM
I (422) heap_init: At 3FCE9710 len 00005724 (21 KiB): STACK/DRAM
I (429) heap_init: At 3FCF0000 len 00008000 (32 KiB): DRAM
I (435) heap_init: At 600FE010 len 00001FF0 (7 KiB): RTCRAM
I (442) spi_flash: detected chip: gd
I (446) spi_flash: flash io: dio
W (450) ADC: legacy driver is deprecated, please migrate to `esp_adc/adc_oneshot.h`
I (458) sleep: Configure to isolate all GPIO pins in sleep state
I (465) sleep: Enable automatic switching of GPIO sleep configuration
I (472) app_start: Starting scheduler on CPU0
I (477) app_start: Starting scheduler on CPU1
I (477) main_task: Started on CPU0
I (487) main_task: Calling app_main()
I (527) miner: NVS_CONFIG_ASIC_FREQ 475.000000
I (527) miner: ASIC: BM1397
I (527) miner: Welcome to the bitaxe!
I (527) SystemModule: I2C initialized successfully
I (537) DS4432U.c: Set BM1397 voltage = 1.400V [0x90]
I (537) DS4432U.c: Writing 0x90
I (547) pp: pp rom version: e7ae62f
I (547) net80211: net80211 rom version: e7ae62f
I (557) wifi:wifi driver task: 3fcad598, prio:23, stack:6656, core=0
I (577) wifi:wifi firmware version: b2f1f86
I (577) wifi:wifi certification version: v7.0
I (577) wifi:config NVS flash: enabled
I (577) wifi:config nano formating: disabled
I (577) wifi:Init data frame dynamic rx buffer num: 32
I (587) wifi:Init management frame dynamic rx buffer num: 32
I (587) wifi:Init management short buffer num: 32
I (597) wifi:Init dynamic tx buffer num: 32
I (597) wifi:Init static tx FG buffer num: 2
I (607) wifi:Init static rx buffer size: 1600
I (607) wifi:Init static rx buffer num: 10
I (607) wifi:Init dynamic rx buffer num: 32
I (617) wifi_init: rx ba win: 6
I (617) wifi_init: tcpip mbox: 32
I (627) wifi_init: udp mbox: 6
I (627) wifi_init: tcp mbox: 6
I (627) wifi_init: tcp tx win: 5744
I (637) wifi_init: tcp rx win: 5744
I (637) wifi_init: tcp mss: 1440
I (637) wifi_init: WiFi IRAM OP enabled
I (647) wifi_init: WiFi RX IRAM OP enabled
I (657) wifi station: ESP_WIFI Access Point On
W (657) wifi:Affected by the ESP-NOW encrypt num, set the max connection num to 10
I (667) wifi station: ESP_WIFI_MODE_STA
I (667) wifi station: wifi_init_sta finished.
I (677) phy_init: phy_version 601,fe52df4,May 10 2023,17:26:54
I (717) wifi:mode : sta (84:fc:e6:6c:90:dc) + softAP (84:fc:e6:6c:90:dd)
I (717) wifi:enable tsf
I (717) wifi:Total power save buffer number: 16
I (717) wifi:Init max length of beacon: 752/752
I (727) wifi:Init max length of beacon: 752/752
I (727) wifi station: wifi_init_sta finished.
I (727) esp_netif_lwip: DHCP server started on interface WIFI_AP_DEF with IP: 192.168.4.1
I (747) wifi:ap channel adjust o:1,1 n:6,2
I (747) wifi:new:<6,0>, old:<1,1>, ap:<6,2>, sta:<6,0>, prof:1
I (747) wifi:state: init -> auth (b0)
I (767) wifi:state: auth -> assoc (0)
I (777) wifi:state: assoc -> run (10)
I (817) wifi:connected with First_Class_Crew, aid = 1, channel 6, BW20, bssid = 44:4e:6d:14:7f:a6
I (817) wifi:security: WPA2-PSK, phy: bgn, rssi: -63
I (867) wifi:pm start, type: 1

I (867) wifi:set rx beacon pti, rx_bcn_pti: 0, bcn_timeout: 25000, mt_pti: 0, mt_time: 10000
I (867) wifi:AP's beacon interval = 102400 us, DTIM period = 1
I (1047) http_server: Partition size: total: 2884241, used: 635532
I (1057) SystemModule: OLED init success!
I (1057) http_server: Starting HTTP Server
I (1057) wifi:<ba-add>idx:0 (ifx:0, 44:4e:6d:14:7f:a6), tid:6, ssn:2, winSize:64
I (1067) example_dns_redirect_server: Socket created
I (1067) example_dns_redirect_server: Socket bound, port 53
I (1077) example_dns_redirect_server: Waiting for data
I (2047) wifi station: Bitaxe ip:192.168.178.76
I (2047) esp_netif_handlers: sta ip: 192.168.178.76, mask: 255.255.255.0, gw: 192.168.178.1
I (2047) miner: Connected to SSID: First_Class_Crew
I (2057) gpio: GPIO[12]| InputEn: 1| OutputEn: 0| OpenDrain: 0| Pullup: 0| Pulldown: 0| Intr:0 
I (2057) wifi station: ESP_WIFI Access Point Off
I (2067) wifi:mode : sta (84:fc:e6:6c:90:dc)
I (2077) serial: Initializing serial
I (2077) bm1397Module: Initializing BM1397
I (2297) bm1397Module: Setting job ASIC mask to 255
I (2347) bm1397Module: Setting Frequency to 475.00MHz (475.00)
I (2347) stratum_task: Get IP for URL: public-pool.io

I (2347) bm1397Module: Setting max baud of 3125000
I (2347) main_task: Returned from app_main()
I (2347) wifi:<ba-add>idx:1 (ifx:0, 44:4e:6d:14:7f:a6), tid:0, ssn:0, winSize:64
I (2357) serial: Changing UART baud to 3125000
I (2367) stratum_task: Connecting to: stratum+tcp://public-pool.io:21496 (68.235.52.36)

I (2367) ASIC_task: ASIC Ready!
I (2377) stratum_task: Socket created, connecting to 68.235.52.36:21496
I (2547) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe/BM1397"]}

I (2787) stratum_api: Received result {"id":1,"error":null,"result":[[["mining.notify","81146af8"]],"81146af8",4]}
I (2787) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}

I (2997) stratum_api: Received result {"id":2,"error":null,"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"}}
I (2997) stratum_api: Set version mask: 1fffe000
I (2997) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [512]}

I (3017) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "x"]}

I (3197) stratum_task: rx: {"id":3,"method":"mining.set_difficulty","params":[512]}
I (3197) stratum_task: Set stratum difficulty: 512
I (3507) stratum_task: rx: {"id":4,"error":null,"result":true}
I (3507) stratum_task: message result accepted
I (3917) stratum_task: rx: {"id":null,"method":"mining.notify","params":["eab552","7c498c18c41512ff2535c7fc36607e57fa694e5f0000f6540000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703b9b30c5075626c69632d506f6f6c","ffffffff02b0f99b2800000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9edb5a27171995d5cc96e02fd4612f93797feece2cde4a87b76abbd2f7f870f3d7400000000",["7b705739c2bbe4dd9a2bebc13eb7111eef6c36e1cc38bb0e41c565c75580aeed","17f97459993807e2106d003ad54af8a8726b2166f65a96468542b5707adb757e","ed72583ad42f86613bb01fc950b11d495687579192e227e7d6d136c0932b7ef5","ba6501611d262f405fe75fcc2b728a7cfadf0be0f846e05d3a75e293d196ae6f","7fde5556b4d387441da90d27d8a0179d329974373dfe397451f51dfbee1f1c9b","658adcd0460d5b7f1140725ea05e02e2c2f746cc7025ae778340292974e85168","d4225312a1114322011c82d29e6f10f066d66dd9b53542ec8bd2a676b2398e46","48b80bd64bf15513c5230fb841c6fd7ef139243985872d3f7b9b7392d2223f23","8a0b5771ab41cada8f8e6287b2ee62d6473c21fbfdc7a3378395827bb9c208bf","62ba8b5c8a0a5ad99f07f3ef2d9e42480c955ce3f1e12c911f3a6940b2fe8b07","17d76f604549c537a754016c94fb90dadd632be7176603af55041ea548edb745","ebceb3493b1a2712105e2bd0c8b8e6abfd134b6037443ea51098e5eb97918401"],"20000000","170371b1","65df8ce9",false]}
I (4017) SystemModule: Syncing clock
I (4017) create_jobs_task: New Work Dequeued eab552
I (4027) bm1397Module: Setting job ASIC mask to 511
I (5107) bm1397Module: Setting Frequency to 61.07MHz (61.67)
I (5107) power_management: target 61.071426, Freq 61.071426, Temp 46.625000, Power 0.000000
I (32487) stratum_task: rx: {"id":null,"method":"mining.notify","params":["eab55f","7c498c18c41512ff2535c7fc36607e57fa694e5f0000f6540000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703b9b30c5075626c69632d506f6f6c","ffffffff02b0f99b2800000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9edb5a27171995d5cc96e02fd4612f93797feece2cde4a87b76abbd2f7f870f3d7400000000",["7b705739c2bbe4dd9a2bebc13eb7111eef6c36e1cc38bb0e41c565c75580aeed","17f97459993807e2106d003ad54af8a8726b2166f65a96468542b5707adb757e","ed72583ad42f86613bb01fc950b11d495687579192e227e7d6d136c0932b7ef5","ba6501611d262f405fe75fcc2b728a7cfadf0be0f846e05d3a75e293d196ae6f","7fde5556b4d387441da90d27d8a0179d329974373dfe397451f51dfbee1f1c9b","658adcd0460d5b7f1140725ea05e02e2c2f746cc7025ae778340292974e85168","d4225312a1114322011c82d29e6f10f066d66dd9b53542ec8bd2a676b2398e46","48b80bd64bf15513c5230fb841c6fd7ef139243985872d3f7b9b7392d2223f23","8a0b5771ab41cada8f8e6287b2ee62d6473c21fbfdc7a3378395827bb9c208bf","62ba8b5c8a0a5ad99f07f3ef2d9e42480c955ce3f1e12c911f3a6940b2fe8b07","17d76f604549c537a754016c94fb90dadd632be7176603af55041ea548edb745","ebceb3493b1a2712105e2bd0c8b8e6abfd134b6037443ea51098e5eb97918401"],"20000000","170371b1","65df8d25",false]}
I (32597) create_jobs_task: New Work Dequeued eab55f

### xXAsystolieXx on 2024-02-28

@qubyt3 Is it enough to only connect to the USB cable or should I also connect the power plug?

### FragOmatig on 2024-02-28

my logs on web GUI

webflash logs are clear 

₿ (63612) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[64]}
₿ (63612) stratum_task: Set stratum difficulty: 64
₿ (64132) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e61a60","81ff09bd5762678dd8fbbb63b19e3c2ba14d172200007eed0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703bab30c5075626c69632d506f6f6c","ffffffff02296d7428000000001976a91462e907b15cbf27d5425399ebf6f0fb50ebb88f1888ac0000000000000000266a24aa21a9ed571f858728aa19cb1541efeba867b599c8c3aea6bd4cfeb3b28973cb4b7d30bf00000000",["e5e9a018d52ec5ddd3303cb65fb34a8fd50d214b1944b41b26a2e6c3c369963d","6798da06d42ba6a1fd32774e2b0a62dc7df4ce87a944e99da25b3553398a9a32","c050d791c88d069cd4b2a1e0e4db005f024a0fd8a0f269359bf8356bf81713a0","f6a3fc85052ac2253299c941e1ab11a46fb1d2d2e55cdf85090519431d3d4880","f0b1c51ab5d54f3158f4be46fc4ff059a73c1c058deece94f6c641b7ec31e84f","50a3ca6de90dbc95d1ddc6cd27072a96bb8e3cffc9f90158fc63c91e62991e2e","c3da3f16c0d8b99921af18e636895177af93abed9ad4a77141d029744640b975","ca748e9152b7bf0a7c8cbe36192bcbd4f8316a35df0b5982c976891cb728d7c3","548cf9bbe496db324e53d62c01fbb161c8530fc0015348f63a4a1e4e1063def1","cce0d1bd6465719e3625a8474e47faf341a04d3ef8748dc0a938301e980fadd5","424cf99b1e746552db802f0b94540bf98740565de8b3df52a901bd42fa91c382","cd20662959785da4f29a0d0ac7858dde99732f194c355ed7c0ec5346d4e386b5"],"20000000","170371b1","65df8d57",true]}
₿ (64232) stratum_task: abandoning work
₿ (64232) create_jobs_task: New Work Dequeued e61a60
₿ (123612) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[8]}
₿ (123612) stratum_task: Set stratum difficulty: 8
₿ (124132) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e61a81","81ff09bd5762678dd8fbbb63b19e3c2ba14d172200007eed0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703bab30c5075626c69632d506f6f6c","ffffffff02296d7428000000001976a91462e907b15cbf27d5425399ebf6f0fb50ebb88f1888ac0000000000000000266a24aa21a9ed571f858728aa19cb1541efeba867b599c8c3aea6bd4cfeb3b28973cb4b7d30bf00000000",["e5e9a018d52ec5ddd3303cb65fb34a8fd50d214b1944b41b26a2e6c3c369963d","6798da06d42ba6a1fd32774e2b0a62dc7df4ce87a944e99da25b3553398a9a32","c050d791c88d069cd4b2a1e0e4db005f024a0fd8a0f269359bf8356bf81713a0","f6a3fc85052ac2253299c941e1ab11a46fb1d2d2e55cdf85090519431d3d4880","f0b1c51ab5d54f3158f4be46fc4ff059a73c1c058deece94f6c641b7ec31e84f","50a3ca6de90dbc95d1ddc6cd27072a96bb8e3cffc9f90158fc63c91e62991e2e","c3da3f16c0d8b99921af18e636895177af93abed9ad4a77141d029744640b975","ca748e9152b7bf0a7c8cbe36192bcbd4f8316a35df0b5982c976891cb728d7c3","548cf9bbe496db324e53d62c01fbb161c8530fc0015348f63a4a1e4e1063def1","cce0d1bd6465719e3625a8474e47faf341a04d3ef8748dc0a938301e980fadd5","424cf99b1e746552db802f0b94540bf98740565de8b3df52a901bd42fa91c382","cd20662959785da4f29a0d0ac7858dde99732f194c355ed7c0ec5346d4e386b5"],"20000000","170371b1","65df8d57",true]}
₿ (124242) stratum_task: abandoning work
₿ (124242) create_jobs_task: New Work Dequeued e61a81
₿ (130182) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e61a87","81ff09bd5762678dd8fbbb63b19e3c2ba14d172200007eed0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703bab30c5075626c69632d506f6f6c","ffffffff02296d7428000000001976a91462e907b15cbf27d5425399ebf6f0fb50ebb88f1888ac0000000000000000266a24aa21a9ed571f858728aa19cb1541efeba867b599c8c3aea6bd4cfeb3b28973cb4b7d30bf00000000",["e5e9a018d52ec5ddd3303cb65fb34a8fd50d214b1944b41b26a2e6c3c369963d","6798da06d42ba6a1fd32774e2b0a62dc7df4ce87a944e99da25b3553398a9a32","c050d791c88d069cd4b2a1e0e4db005f024a0fd8a0f269359bf8356bf81713a0","f6a3fc85052ac2253299c941e1ab11a46fb1d2d2e55cdf85090519431d3d4880","f0b1c51ab5d54f3158f4be46fc4ff059a73c1c058deece94f6c641b7ec31e84f","50a3ca6de90dbc95d1ddc6cd27072a96bb8e3cffc9f90158fc63c91e62991e2e","c3da3f16c0d8b99921af18e636895177af93abed9ad4a77141d029744640b975","ca748e9152b7bf0a7c8cbe36192bcbd4f8316a35df0b5982c976891cb728d7c3","548cf9bbe496db324e53d62c01fbb161c8530fc0015348f63a4a1e4e1063def1","cce0d1bd6465719e3625a8474e47faf341a04d3ef8748dc0a938301e980fadd5","424cf99b1e746552db802f0b94540bf98740565de8b3df52a901bd42fa91c382","cd20662959785da4f29a0d0ac7858dde99732f194c355ed7c0ec5346d4e386b5"],"20000000","170371b1","65df8dc5",false]}
₿ (131732) create_jobs_task: New Work Dequeued e61a87
₿ (183692) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[1]}
₿ (183692) stratum_task: Set stratum difficulty: 1
₿ (184112) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e61ecb","81ff09bd5762678dd8fbbb63b19e3c2ba14d172200007eed0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703bab30c5075626c69632d506f6f6c","ffffffff02296d7428000000001976a91462e907b15cbf27d5425399ebf6f0fb50ebb88f1888ac0000000000000000266a24aa21a9ed571f858728aa19cb1541efeba867b599c8c3aea6bd4cfeb3b28973cb4b7d30bf00000000",["e5e9a018d52ec5ddd3303cb65fb34a8fd50d214b1944b41b26a2e6c3c369963d","6798da06d42ba6a1fd32774e2b0a62dc7df4ce87a944e99da25b3553398a9a32","c050d791c88d069cd4b2a1e0e4db005f024a0fd8a0f269359bf8356bf81713a0","f6a3fc85052ac2253299c941e1ab11a46fb1d2d2e55cdf85090519431d3d4880","f0b1c51ab5d54f3158f4be46fc4ff059a73c1c058deece94f6c641b7ec31e84f","50a3ca6de90dbc95d1ddc6cd27072a96bb8e3cffc9f90158fc63c91e62991e2e","c3da3f16c0d8b99921af18e636895177af93abed9ad4a77141d029744640b975","ca748e9152b7bf0a7c8cbe36192bcbd4f8316a35df0b5982c976891cb728d7c3","548cf9bbe496db324e53d62c01fbb161c8530fc0015348f63a4a1e4e1063def1","cce0d1bd6465719e3625a8474e47faf341a04d3ef8748dc0a938301e980fadd5","424cf99b1e746552db802f0b94540bf98740565de8b3df52a901bd42fa91c382","cd20662959785da4f29a0d0ac7858dde99732f194c355ed7c0ec5346d4e386b5"],"20000000","170371b1","65df8dc5",false]}
₿ (184982) create_jobs_task: New Work Dequeued e61ecb
₿ (190142) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e61ed3","81ff09bd5762678dd8fbbb63b19e3c2ba14d172200007eed0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703bab30c5075626c69632d506f6f6c","ffffffff02296d7428000000001976a91462e907b15cbf27d5425399ebf6f0fb50ebb88f1888ac0000000000000000266a24aa21a9ed571f858728aa19cb1541efeba867b599c8c3aea6bd4cfeb3b28973cb4b7d30bf00000000",["e5e9a018d52ec5ddd3303cb65fb34a8fd50d214b1944b41b26a2e6c3c369963d","6798da06d42ba6a1fd32774e2b0a62dc7df4ce87a944e99da25b3553398a9a32","c050d791c88d069cd4b2a1e0e4db005f024a0fd8a0f269359bf8356bf81713a0","f6a3fc85052ac2253299c941e1ab11a46fb1d2d2e55cdf85090519431d3d4880","f0b1c51ab5d54f3158f4be46fc4ff059a73c1c058deece94f6c641b7ec31e84f","50a3ca6de90dbc95d1ddc6cd27072a96bb8e3cffc9f90158fc63c91e62991e2e","c3da3f16c0d8b99921af18e636895177af93abed9ad4a77141d029744640b975","ca748e9152b7bf0a7c8cbe36192bcbd4f8316a35df0b5982c976891cb728d7c3","548cf9bbe496db324e53d62c01fbb161c8530fc0015348f63a4a1e4e1063def1","cce0d1bd6465719e3625a8474e47faf341a04d3ef8748dc0a938301e980fadd5","424cf99b1e746552db802f0b94540bf98740565de8b3df52a901bd42fa91c382","cd20662959785da4f29a0d0ac7858dde99732f194c355ed7c0ec5346d4e386b5"],"20000000","170371b1","65df8e01",false]}
₿ (191372) create_jobs_task: New Work Dequeued e61ed3
₿ (243632) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[0.16]}
₿ (243632) stratum_task: Set stratum difficulty: 0
₿ (244152) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e62313","81ff09bd5762678dd8fbbb63b19e3c2ba14d172200007eed0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703bab30c5075626c69632d506f6f6c","ffffffff02296d7428000000001976a91462e907b15cbf27d5425399ebf6f0fb50ebb88f1888ac0000000000000000266a24aa21a9ed571f858728aa19cb1541efeba867b599c8c3aea6bd4cfeb3b28973cb4b7d30bf00000000",["e5e9a018d52ec5ddd3303cb65fb34a8fd50d214b1944b41b26a2e6c3c369963d","6798da06d42ba6a1fd32774e2b0a62dc7df4ce87a944e99da25b3553398a9a32","c050d791c88d069cd4b2a1e0e4db005f024a0fd8a0f269359bf8356bf81713a0","f6a3fc85052ac2253299c941e1ab11a46fb1d2d2e55cdf85090519431d3d4880","f0b1c51ab5d54f3158f4be46fc4ff059a73c1c058deece94f6c641b7ec31e84f","50a3ca6de90dbc95d1ddc6cd27072a96bb8e3cffc9f90158fc63c91e62991e2e","c3da3f16c0d8b99921af18e636895177af93abed9ad4a77141d029744640b975","ca748e9152b7bf0a7c8cbe36192bcbd4f8316a35df0b5982c976891cb728d7c3","548cf9bbe496db324e53d62c01fbb161c8530fc0015348f63a4a1e4e1063def1","cce0d1bd6465719e3625a8474e47faf341a04d3ef8748dc0a938301e980fadd5","424cf99b1e746552db802f0b94540bf98740565de8b3df52a901bd42fa91c382","cd20662959785da4f29a0d0ac7858dde99732f194c355ed7c0ec5346d4e386b5"],"20000000","170371b1","65df8e01",false]}
₿ (244622) create_jobs_task: New Work Dequeued e62313
₿ (250192) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e62319","81ff09bd5762678dd8fbbb63b19e3c2ba14d172200007eed0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703bab30c5075626c69632d506f6f6c","ffffffff02296d7428000000001976a91462e907b15cbf27d5425399ebf6f0fb50ebb88f1888ac0000000000000000266a24aa21a9ed571f858728aa19cb1541efeba867b599c8c3aea6bd4cfeb3b28973cb4b7d30bf00000000",["e5e9a018d52ec5ddd3303cb65fb34a8fd50d214b1944b41b26a2e6c3c369963d","6798da06d42ba6a1fd32774e2b0a62dc7df4ce87a944e99da25b3553398a9a32","c050d791c88d069cd4b2a1e0e4db005f024a0fd8a0f269359bf8356bf81713a0","f6a3fc85052ac2253299c941e1ab11a46fb1d2d2e55cdf85090519431d3d4880","f0b1c51ab5d54f3158f4be46fc4ff059a73c1c058deece94f6c641b7ec31e84f","50a3ca6de90dbc95d1ddc6cd27072a96bb8e3cffc9f90158fc63c91e62991e2e","c3da3f16c0d8b99921af18e636895177af93abed9ad4a77141d029744640b975","ca748e9152b7bf0a7c8cbe36192bcbd4f8316a35df0b5982c976891cb728d7c3","548cf9bbe496db324e53d62c01fbb161c8530fc0015348f63a4a1e4e1063def1","cce0d1bd6465719e3625a8474e47faf341a04d3ef8748dc0a938301e980fadd5","424cf99b1e746552db802f0b94540bf98740565de8b3df52a901bd42fa91c382","cd20662959785da4f29a0d0ac7858dde99732f194c355ed7c0ec5346d4e386b5"],"20000000","170371b1","65df8e3d",false]}
₿ (251012) create_jobs_task: New Work Dequeued e62319

### qubyt3 on 2024-02-28

@xXAsystolieXx  I always say power supply ( I think you can have both)... but doesn't hurt to try with power supply only and see what happens. 

I don't think it will change anything though... 

I'm wondering why the Frequency is downgraded to 61.07MHz "I (5107) bm1397Module: Setting Frequency to 61.07MHz (61.67)" when its clearly set at boot up at: I (2347) bm1397Module: Setting Frequency to 475.00MHz (475.00)

hmmm maybe @skot can help here? 

### FragOmatig on 2024-02-28

![IMG_3007](https://github.com/skot/ESP-Miner/assets/161623595/43cecfe7-01db-4a19-9895-d00602fa19d4)


### FragOmatig on 2024-02-28

![IMG_3009](https://github.com/skot/ESP-Miner/assets/161623595/cea0da7a-fc74-4b87-bdd1-6ca4bd7dbc21)


### qubyt3 on 2024-02-28

@FragOmatig Check the log example that xXAsystolieXx posted above, that's what I'm looking for. 
It seems you might have the same issue, just want to confirm. 

Your board version is wrong, it should be 0.11 by the way, not "204". Seems you may have changed that in the config.cvs file by accident. 

### pinokio240 on 2024-02-28

@qubyt3 
![ver_win](https://github.com/skot/ESP-Miner/assets/37944152/21be7af6-b788-4370-9de0-95b4e03e2b34)
What should cconfig.cvs look like for my miner? And what is the firmware version?

### qubyt3 on 2024-02-28

@pinokio240 it should be: 

asicfrequency,data,u16,475
asicvoltage,data,u16,1400
asicmodel,data,string,BM1397
devicemodel,data,string,max
boardversion,data,string,2.2

and your showing a firmware version of v.2.0.7 which I think is what you were trying to do :) 

### FragOmatig on 2024-02-28

@qubyt3

ok thats shit.... i buy the miner with V2.0.7 an not work. 
what can i do? 

### pinokio240 on 2024-02-28

> @pinokio240 it should be:
> 
> asicfrequency,data,u16,475 asicvoltage,data,u16,1400 asicmodel,data,string,BM1397 devicemodel,data,string,max boardversion,data,string,2.2
> 
> and your showing a firmware version of v.2.0.7 which I think is what you were trying to do :)

but there is more:
key,type,encoding,value
main,namespace,,
........
flipscreen,data,u16,1
invertfanpol,data,u16,1
autofanspeed,data,u16,1
fanspeed,data,u16,100
Are they optional?


### qubyt3 on 2024-02-28

@pinokio240  yes, leave as is. 

### xXAsystolieXx on 2024-02-28

ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0x15 (USB_UART_CHIP_RESET),boot:0x2a (SPI_FAST_FLASH_BOOT)
Saved PC:0x4037b8b2
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce3818,len:0x16e0
load:0x403c9700,len:0x4
load:0x403c9704,len:0xc00
load:0x403cc700,len:0x2eb0
entry 0x403c9908
I (27) boot: ESP-IDF v5.1 2nd stage bootloader
I (27) boot: compile time Jan 20 2024 20:00:30
I (27) boot: Multicore bootloader
I (30) boot: chip revision: v0.2
I (34) boot.esp32s3: Boot SPI Speed : 80MHz
I (38) boot.esp32s3: SPI Mode       : DIO
I (43) boot.esp32s3: SPI Flash Size : 16MB
I (48) boot: Enabling RNG early entropy source...
I (53) boot: Partition Table:
I (57) boot: ## Label            Usage          Type ST Offset   Length
I (64) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (72) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (79) boot:  2 factory          factory app      00 00 00010000 00400000
I (87) boot:  3 www              Unknown data     01 82 00410000 00300000
I (94) boot:  4 ota_0            OTA app          00 10 00710000 00400000
I (101) boot:  5 ota_1            OTA app          00 11 00b10000 00400000
I (109) boot:  6 otadata          OTA data         01 00 00f10000 00002000
I (117) boot:  7 coredump         Unknown data     01 03 00f12000 00010000
I (124) boot: End of partition table
I (128) boot: Defaulting to factory image
I (133) esp_image: segment 0: paddr=00010020 vaddr=3c0b0020 size=29e94h (171668) map
I (172) esp_image: segment 1: paddr=00039ebc vaddr=3fc98100 size=04bbch ( 19388) load
I (177) esp_image: segment 2: paddr=0003ea80 vaddr=40374000 size=01598h (  5528) load
I (180) esp_image: segment 3: paddr=00040020 vaddr=42000020 size=a62e0h (680672) map
I (309) esp_image: segment 4: paddr=000e6308 vaddr=40375598 size=12b54h ( 76628) load
I (335) boot: Loaded app from partition at offset 0x10000
I (335) boot: Disabling RNG early entropy source...
I (346) cpu_start: Multicore app
I (347) cpu_start: Pro cpu up.
I (347) cpu_start: Starting app cpu, entry point is 0x40375584
I (0) cpu_start: App cpu up.
I (365) cpu_start: Pro cpu start user code
I (365) cpu_start: cpu freq: 160000000 Hz
I (365) cpu_start: Application information:
I (368) cpu_start: Project name:     esp-miner
I (373) cpu_start: App version:      v2.0.7
I (378) cpu_start: Compile time:     Jan 20 2024 19:59:47
I (384) cpu_start: ELF file SHA256:  c148b21719898fc7...
I (390) cpu_start: ESP-IDF:          v5.1
I (395) cpu_start: Min chip rev:     v0.0
I (399) cpu_start: Max chip rev:     v0.99 
I (404) cpu_start: Chip rev:         v0.2
I (409) heap_init: Initializing. RAM available for dynamic allocation:
I (416) heap_init: At 3FCA2050 len 000476C0 (285 KiB): DRAM
I (422) heap_init: At 3FCE9710 len 00005724 (21 KiB): STACK/DRAM
I (429) heap_init: At 3FCF0000 len 00008000 (32 KiB): DRAM
I (435) heap_init: At 600FE010 len 00001FF0 (7 KiB): RTCRAM
I (442) spi_flash: detected chip: gd
I (446) spi_flash: flash io: dio
W (450) ADC: legacy driver is deprecated, please migrate to `esp_adc/adc_oneshot.h`
I (458) sleep: Configure to isolate all GPIO pins in sleep state
I (465) sleep: Enable automatic switching of GPIO sleep configuration
I (472) app_start: Starting scheduler on CPU0
I (477) app_start: Starting scheduler on CPU1
I (477) main_task: Started on CPU0
I (487) main_task: Calling app_main()
I (527) miner: NVS_CONFIG_ASIC_FREQ 475.000000
I (527) miner: ASIC: BM1397
I (527) miner: Welcome to the bitaxe!
I (527) SystemModule: I2C initialized successfully
I (537) DS4432U.c: Set BM1397 voltage = 1.400V [0x90]
I (537) DS4432U.c: Writing 0x90
I (547) pp: pp rom version: e7ae62f
I (547) net80211: net80211 rom version: e7ae62f
I (557) wifi:wifi driver task: 3fcad598, prio:23, stack:6656, core=0
I (577) wifi:wifi firmware version: b2f1f86
I (577) wifi:wifi certification version: v7.0
I (577) wifi:config NVS flash: enabled
I (577) wifi:config nano formating: disabled
I (577) wifi:Init data frame dynamic rx buffer num: 32
I (587) wifi:Init management frame dynamic rx buffer num: 32
I (587) wifi:Init management short buffer num: 32
I (597) wifi:Init dynamic tx buffer num: 32
I (597) wifi:Init static tx FG buffer num: 2
I (607) wifi:Init static rx buffer size: 1600
I (607) wifi:Init static rx buffer num: 10
I (607) wifi:Init dynamic rx buffer num: 32
I (617) wifi_init: rx ba win: 6
I (617) wifi_init: tcpip mbox: 32
I (627) wifi_init: udp mbox: 6
I (627) wifi_init: tcp mbox: 6
I (627) wifi_init: tcp tx win: 5744
I (637) wifi_init: tcp rx win: 5744
I (637) wifi_init: tcp mss: 1440
I (637) wifi_init: WiFi IRAM OP enabled
I (647) wifi_init: WiFi RX IRAM OP enabled
I (657) wifi station: ESP_WIFI Access Point On
W (657) wifi:Affected by the ESP-NOW encrypt num, set the max connection num to 10
I (667) wifi station: ESP_WIFI_MODE_STA
I (667) wifi station: wifi_init_sta finished.
I (677) phy_init: phy_version 601,fe52df4,May 10 2023,17:26:54
I (717) wifi:mode : sta (84:fc:e6:6c:90:dc) + softAP (84:fc:e6:6c:90:dd)
I (717) wifi:enable tsf
I (717) wifi:Total power save buffer number: 16
I (717) wifi:Init max length of beacon: 752/752
I (717) wifi:Init max length of beacon: 752/752
I (727) wifi station: wifi_init_sta finished.
I (727) esp_netif_lwip: DHCP server started on interface WIFI_AP_DEF with IP: 192.168.4.1
I (747) wifi:ap channel adjust o:1,1 n:6,2
I (747) wifi:new:<6,0>, old:<1,1>, ap:<6,2>, sta:<6,0>, prof:1
I (747) wifi:state: init -> auth (b0)
I (757) wifi:state: auth -> init (8a0)
I (757) wifi:new:<6,0>, old:<6,0>, ap:<6,2>, sta:<6,0>, prof:1
I (1017) http_server: Partition size: total: 2884241, used: 635532
I (1017) http_server: Starting HTTP Server
I (1027) example_dns_redirect_server: Socket created
I (1027) example_dns_redirect_server: Socket bound, port 53
I (1037) example_dns_redirect_server: Waiting for data
I (1037) SystemModule: OLED init success!
I (1767) wifi station: Retrying WiFi connection...
I (5597) wifi station: Retrying WiFi connection...
I (5617) wifi:new:<6,2>, old:<6,0>, ap:<6,2>, sta:<6,0>, prof:1
I (5617) wifi:state: init -> auth (b0)
I (5627) wifi:state: auth -> assoc (0)
I (5637) wifi:state: assoc -> run (10)
I (5667) wifi:connected with First_Class_Crew, aid = 1, channel 6, BW20, bssid = 44:4e:6d:14:7f:a6
I (5667) wifi:security: WPA2-PSK, phy: bgn, rssi: -61
I (5667) wifi:pm start, type: 1

I (5677) wifi:set rx beacon pti, rx_bcn_pti: 0, bcn_timeout: 25000, mt_pti: 0, mt_time: 10000
I (5687) wifi:<ba-add>idx:0 (ifx:0, 44:4e:6d:14:7f:a6), tid:6, ssn:2, winSize:64
I (5717) wifi:AP's beacon interval = 102400 us, DTIM period = 1
I (6677) wifi station: Bitaxe ip:192.168.178.76
I (6677) esp_netif_handlers: sta ip: 192.168.178.76, mask: 255.255.255.0, gw: 192.168.178.1
I (6677) miner: Connected to SSID: First_Class_Crew
I (6687) wifi station: ESP_WIFI Access Point Off
I (6687) gpio: GPIO[12]| InputEn: 1| OutputEn: 0| OpenDrain: 0| Pullup: 0| Pulldown: 0| Intr:0 
I (6697) wifi:mode : sta (84:fc:e6:6c:90:dc)
I (6707) serial: Initializing serial
I (6707) bm1397Module: Initializing BM1397
I (6927) bm1397Module: Setting job ASIC mask to 255
I (6977) bm1397Module: Setting Frequency to 475.00MHz (475.00)
I (6977) stratum_task: Get IP for URL: public-pool.io

I (6977) bm1397Module: Setting max baud of 3125000
I (6977) main_task: Returned from app_main()
I (6987) serial: Changing UART baud to 3125000
I (6987) ASIC_task: ASIC Ready!
I (7007) wifi:<ba-add>idx:1 (ifx:0, 44:4e:6d:14:7f:a6), tid:0, ssn:0, winSize:64
I (7007) stratum_task: Connecting to: stratum+tcp://public-pool.io:21496 (68.235.52.36)

I (7017) stratum_task: Socket created, connecting to 68.235.52.36:21496
I (7247) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe/BM1397"]}

I (7457) stratum_api: Received result {"id":1,"error":null,"result":[[["mining.notify","5b591e76"]],"5b591e76",4]}
I (7457) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}

I (7657) stratum_api: Received result {"id":2,"error":null,"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"}}
I (7667) stratum_api: Set version mask: 1fffe000
I (7667) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [512]}

I (7677) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "x"]}

I (7867) stratum_task: rx: {"id":3,"method":"mining.set_difficulty","params":[512]}
I (7867) stratum_task: Set stratum difficulty: 512
I (8067) stratum_task: rx: {"id":4,"error":null,"result":true}
I (8067) stratum_task: message result accepted
I (8477) stratum_task: rx: {"id":null,"method":"mining.notify","params":["eaaef5","dac8a9d1f03f707e706b83c92c51fa6e2eadbaa20001cc4a0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703bcb30c5075626c69632d506f6f6c","ffffffff02f5b2492800000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9eddddf9a631e8f5ffc73dddab53a25cd7cadd09c3fb4753c218f43fbbc284c892f00000000",["81dae03ee49a185cc53e80c9bff8b73b97a6ca5dcdc73d717d319410811df188","4db6b2cecfa1eb71c2e49c05c6f30496c5efc8839c5cb0835e5b15e6d8d96c4e","d3e9ff525ed76a92c0558cb17f88af1067c488412b904b2e70c7f52888e28ed3","8344348f310b3649b42b6617e9d91e5b72dbf51abbf436468e3fc03f9c3cd3c6","20d22ca8ebee49c9673f033ab18d0d3cadcbe1ff43c58803887a015449fab31c","7c661293d9fc8fcc22a24ebe8e9d7c82865b19d41d5e0efc5765939f49584e8c","b6cde26ada3cf8be1a5437183e4dd15ed5733c7de8b8f27cee7fc113c96317e1","ce6bede94f471c9e384ce91b0067ca03f5319f7a93f120776cc52355edda0b58","c906211d3806ed5dbd50aa35e65162b8628d0c0810ce7ce2e53d1f1d5e2d27cc","29f2a776d17746fe18dc0a8708a09c274660fcbc836d48f939a1a95c33d536c1","d6ca2f15e15805d463dbf3cb7501cf12d9adfcefb9f7767cc0fa9f6fafa862de","d135b06f1c215d4dee3dd2d13b14b9d28461447751d5cbc4dc3a3d890e1ff2ed","6d12b155e3e404e18c929c74b55a74997b6adfd76a4f0b51d9a840e39d95c0fc"],"20000000","170371b1","65df9225",false]}
I (8587) SystemModule: Syncing clock
I (8597) create_jobs_task: New Work Dequeued eaaef5
I (8607) bm1397Module: Setting job ASIC mask to 511
I (11037) stratum_task: rx: {"id":null,"method":"mining.notify","params":["eaaeff","dac8a9d1f03f707e706b83c92c51fa6e2eadbaa20001cc4a0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703bcb30c5075626c69632d506f6f6c","ffffffff02f5b2492800000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9eddddf9a631e8f5ffc73dddab53a25cd7cadd09c3fb4753c218f43fbbc284c892f00000000",["81dae03ee49a185cc53e80c9bff8b73b97a6ca5dcdc73d717d319410811df188","4db6b2cecfa1eb71c2e49c05c6f30496c5efc8839c5cb0835e5b15e6d8d96c4e","d3e9ff525ed76a92c0558cb17f88af1067c488412b904b2e70c7f52888e28ed3","8344348f310b3649b42b6617e9d91e5b72dbf51abbf436468e3fc03f9c3cd3c6","20d22ca8ebee49c9673f033ab18d0d3cadcbe1ff43c58803887a015449fab31c","7c661293d9fc8fcc22a24ebe8e9d7c82865b19d41d5e0efc5765939f49584e8c","b6cde26ada3cf8be1a5437183e4dd15ed5733c7de8b8f27cee7fc113c96317e1","ce6bede94f471c9e384ce91b0067ca03f5319f7a93f120776cc52355edda0b58","c906211d3806ed5dbd50aa35e65162b8628d0c0810ce7ce2e53d1f1d5e2d27cc","29f2a776d17746fe18dc0a8708a09c274660fcbc836d48f939a1a95c33d536c1","d6ca2f15e15805d463dbf3cb7501cf12d9adfcefb9f7767cc0fa9f6fafa862de","d135b06f1c215d4dee3dd2d13b14b9d28461447751d5cbc4dc3a3d890e1ff2ed","6d12b155e3e404e18c929c74b55a74997b6adfd76a4f0b51d9a840e39d95c0fc"],"20000000","170371b1","65df9261",false]}
I (11167) create_jobs_task: New Work Dequeued eaaeff
I (66977) bm1397Module: return null
I (68077) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[64]}
I (68077) stratum_task: Set stratum difficulty: 64
I (68487) stratum_task: rx: {"id":null,"method":"mining.notify","params":["eab371","dac8a9d1f03f707e706b83c92c51fa6e2eadbaa20001cc4a0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703bcb30c5075626c69632d506f6f6c","ffffffff02f5b2492800000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9eddddf9a631e8f5ffc73dddab53a25cd7cadd09c3fb4753c218f43fbbc284c892f00000000",["81dae03ee49a185cc53e80c9bff8b73b97a6ca5dcdc73d717d319410811df188","4db6b2cecfa1eb71c2e49c05c6f30496c5efc8839c5cb0835e5b15e6d8d96c4e","d3e9ff525ed76a92c0558cb17f88af1067c488412b904b2e70c7f52888e28ed3","8344348f310b3649b42b6617e9d91e5b72dbf51abbf436468e3fc03f9c3cd3c6","20d22ca8ebee49c9673f033ab18d0d3cadcbe1ff43c58803887a015449fab31c","7c661293d9fc8fcc22a24ebe8e9d7c82865b19d41d5e0efc5765939f49584e8c","b6cde26ada3cf8be1a5437183e4dd15ed5733c7de8b8f27cee7fc113c96317e1","ce6bede94f471c9e384ce91b0067ca03f5319f7a93f120776cc52355edda0b58","c906211d3806ed5dbd50aa35e65162b8628d0c0810ce7ce2e53d1f1d5e2d27cc","29f2a776d17746fe18dc0a8708a09c274660fcbc836d48f939a1a95c33d536c1","d6ca2f15e15805d463dbf3cb7501cf12d9adfcefb9f7767cc0fa9f6fafa862de","d135b06f1c215d4dee3dd2d13b14b9d28461447751d5cbc4dc3a3d890e1ff2ed","6d12b155e3e404e18c929c74b55a74997b6adfd76a4f0b51d9a840e39d95c0fc"],"20000000","170371b1","65df9261",false]}
I (68607) create_jobs_task: New Work Dequeued eab371
I (68737) bm1397Module: Setting job ASIC mask to 63
I (71047) stratum_task: rx: {"id":null,"method":"mining.notify","params":["eab375","dac8a9d1f03f707e706b83c92c51fa6e2eadbaa20001cc4a0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703bcb30c5075626c69632d506f6f6c","ffffffff02f5b2492800000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9eddddf9a631e8f5ffc73dddab53a25cd7cadd09c3fb4753c218f43fbbc284c892f00000000",["81dae03ee49a185cc53e80c9bff8b73b97a6ca5dcdc73d717d319410811df188","4db6b2cecfa1eb71c2e49c05c6f30496c5efc8839c5cb0835e5b15e6d8d96c4e","d3e9ff525ed76a92c0558cb17f88af1067c488412b904b2e70c7f52888e28ed3","8344348f310b3649b42b6617e9d91e5b72dbf51abbf436468e3fc03f9c3cd3c6","20d22ca8ebee49c9673f033ab18d0d3cadcbe1ff43c58803887a015449fab31c","7c661293d9fc8fcc22a24ebe8e9d7c82865b19d41d5e0efc5765939f49584e8c","b6cde26ada3cf8be1a5437183e4dd15ed5733c7de8b8f27cee7fc113c96317e1","ce6bede94f471c9e384ce91b0067ca03f5319f7a93f120776cc52355edda0b58","c906211d3806ed5dbd50aa35e65162b8628d0c0810ce7ce2e53d1f1d5e2d27cc","29f2a776d17746fe18dc0a8708a09c274660fcbc836d48f939a1a95c33d536c1","d6ca2f15e15805d463dbf3cb7501cf12d9adfcefb9f7767cc0fa9f6fafa862de","d135b06f1c215d4dee3dd2d13b14b9d28461447751d5cbc4dc3a3d890e1ff2ed","6d12b155e3e404e18c929c74b55a74997b6adfd76a4f0b51d9a840e39d95c0fc"],"20000000","170371b1","65df929d",false]}
I (71167) create_jobs_task: New Work Dequeued eab375
I (126977) bm1397Module: return null
I (128087) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[8]}
I (128087) stratum_task: Set stratum difficulty: 8
I (128497) stratum_task: rx: {"id":null,"method":"mining.notify","params":["eab7eb","dac8a9d1f03f707e706b83c92c51fa6e2eadbaa20001cc4a0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703bcb30c5075626c69632d506f6f6c","ffffffff02f5b2492800000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9eddddf9a631e8f5ffc73dddab53a25cd7cadd09c3fb4753c218f43fbbc284c892f00000000",["81dae03ee49a185cc53e80c9bff8b73b97a6ca5dcdc73d717d319410811df188","4db6b2cecfa1eb71c2e49c05c6f30496c5efc8839c5cb0835e5b15e6d8d96c4e","d3e9ff525ed76a92c0558cb17f88af1067c488412b904b2e70c7f52888e28ed3","8344348f310b3649b42b6617e9d91e5b72dbf51abbf436468e3fc03f9c3cd3c6","20d22ca8ebee49c9673f033ab18d0d3cadcbe1ff43c58803887a015449fab31c","7c661293d9fc8fcc22a24ebe8e9d7c82865b19d41d5e0efc5765939f49584e8c","b6cde26ada3cf8be1a5437183e4dd15ed5733c7de8b8f27cee7fc113c96317e1","ce6bede94f471c9e384ce91b0067ca03f5319f7a93f120776cc52355edda0b58","c906211d3806ed5dbd50aa35e65162b8628d0c0810ce7ce2e53d1f1d5e2d27cc","29f2a776d17746fe18dc0a8708a09c274660fcbc836d48f939a1a95c33d536c1","d6ca2f15e15805d463dbf3cb7501cf12d9adfcefb9f7767cc0fa9f6fafa862de","d135b06f1c215d4dee3dd2d13b14b9d28461447751d5cbc4dc3a3d890e1ff2ed","6d12b155e3e404e18c929c74b55a74997b6adfd76a4f0b51d9a840e39d95c0fc"],"20000000","170371b1","65df929d",false]}
I (128617) create_jobs_task: New Work Dequeued eab7eb
I (128747) bm1397Module: Setting job ASIC mask to 7
I (131667) stratum_task: rx: {"id":null,"method":"mining.notify","params":["eab7ef","dac8a9d1f03f707e706b83c92c51fa6e2eadbaa20001cc4a0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703bcb30c5075626c69632d506f6f6c","ffffffff02f5b2492800000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9eddddf9a631e8f5ffc73dddab53a25cd7cadd09c3fb4753c218f43fbbc284c892f00000000",["81dae03ee49a185cc53e80c9bff8b73b97a6ca5dcdc73d717d319410811df188","4db6b2cecfa1eb71c2e49c05c6f30496c5efc8839c5cb0835e5b15e6d8d96c4e","d3e9ff525ed76a92c0558cb17f88af1067c488412b904b2e70c7f52888e28ed3","8344348f310b3649b42b6617e9d91e5b72dbf51abbf436468e3fc03f9c3cd3c6","20d22ca8ebee49c9673f033ab18d0d3cadcbe1ff43c58803887a015449fab31c","7c661293d9fc8fcc22a24ebe8e9d7c82865b19d41d5e0efc5765939f49584e8c","b6cde26ada3cf8be1a5437183e4dd15ed5733c7de8b8f27cee7fc113c96317e1","ce6bede94f471c9e384ce91b0067ca03f5319f7a93f120776cc52355edda0b58","c906211d3806ed5dbd50aa35e65162b8628d0c0810ce7ce2e53d1f1d5e2d27cc","29f2a776d17746fe18dc0a8708a09c274660fcbc836d48f939a1a95c33d536c1","d6ca2f15e15805d463dbf3cb7501cf12d9adfcefb9f7767cc0fa9f6fafa862de","d135b06f1c215d4dee3dd2d13b14b9d28461447751d5cbc4dc3a3d890e1ff2ed","6d12b155e3e404e18c929c74b55a74997b6adfd76a4f0b51d9a840e39d95c0fc"],"20000000","170371b1","65df92d9",false]}
I (131787) create_jobs_task: New Work Dequeued eab7ef

### xXAsystolieXx on 2024-02-28

now with power supply ;)

### qubyt3 on 2024-02-28

@xXAsystolieXx  so with the power supply plugged in, it din't bring down the Frequency after bootup. Is it hashing? 

### xXAsystolieXx on 2024-02-28

@qubyt3  No, unfortunately not

### pinokio240 on 2024-02-28

@qubyt3 
![ver_win](https://github.com/skot/ESP-Miner/assets/37944152/82493f19-765d-4f9f-884c-4f239bbd6c28)
An endless reboot begins
[esp-web-tools-logs.txt](https://github.com/skot/ESP-Miner/files/14439586/esp-web-tools-logs.txt)
Goodbye, I'm off to bed, it's night time

### qubyt3 on 2024-02-28

@xXAsystolieXx  argh .. how fun .. It could be your ASIC chip that gave out... have you overclocked it in the past? 

You could try another pool to see if it follows? solo.ckpool.org port 3333 but I have a feeling it will.

I'm not sure why its not hashing... based on the pool, its slowly reducing the difficulty in the hope to get shares from you in a timely manner.  

### xXAsystolieXx on 2024-02-28

@qubyt3 No, didn't overclocked him. The strange thing is, if I flashing back to version 2.0.6 now, my bitaxe starts to hash🤣

### benjamin-wilson on 2024-02-28

@pinokio240 did yours ever work? You're missing 6 resistors at the top.

### benjamin-wilson on 2024-02-28

Ah that was a cheap one off AliExpress. I'm not surprised. Buy them off this list for high quality units with retailers that will stand behind the product and offer a warranty. 
https://bitaxe.org/legit.html

### xXAsystolieXx on 2024-02-28

I (178360) asic_result: Nonce difficulty 580.56 of 1000.ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0x15 (USB_UART_CHIP_RESET),boot:0x28 (SPI_FAST_FLASH_BOOT)
Saved PC:0x4037b8a2
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce3818,len:0x16f0
load:0x403c9700,len:0x4
load:0x403c9704,len:0xc00
load:0x403cc700,len:0x2eb0
entry 0x403c9908
I (27) boot: ESP-IDF v5.1-564-g8d2dbd461f 2nd stage bootloader
I (27) boot: compile time Jan 12 2024 14:00:52
I (27) boot: Multicore bootloader
I (31) boot: chip revision: v0.2
I (35) boot.esp32s3: Boot SPI Speed : 80MHz
I (40) boot.esp32s3: SPI Mode       : DIO
I (44) boot.esp32s3: SPI Flash Size : 16MB
I (49) boot: Enabling RNG early entropy source...
I (55) boot: Partition Table:
I (58) boot: ## Label            Usage          Type ST Offset   Length
I (66) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (73) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (80) boot:  2 factory          factory app      00 00 00010000 00400000
I (88) boot:  3 www              Unknown data     01 82 00410000 00300000
I (95) boot:  4 ota_0            OTA app          00 10 00710000 00400000
I (103) boot:  5 ota_1            OTA app          00 11 00b10000 00400000
I (110) boot:  6 otadata          OTA data         01 00 00f10000 00002000
I (118) boot:  7 coredump         Unknown data     01 03 00f12000 00010000
I (126) boot: End of partition table
I (130) boot: Defaulting to factory image
I (134) esp_image: segment 0: paddr=00010020 vaddr=3c0b0020 size=29ee0h (171744) map
I (174) esp_image: segment 1: paddr=00039f08 vaddr=3fc98400 size=04ba4h ( 19364) load
I (178) esp_image: segment 2: paddr=0003eab4 vaddr=40374000 size=01564h (  5476) load
I (181) esp_image: segment 3: paddr=00040020 vaddr=42000020 size=a6320h (680736) map
I (310) esp_image: segment 4: paddr=000e6348 vaddr=40375564 size=12e00h ( 77312) load
I (336) boot: Loaded app from partition at offset 0x10000
I (337) boot: Disabling RNG early entropy source...
I (348) cpu_start: Multicore app
I (348) cpu_start: Pro cpu up.
I (348) cpu_start: Starting app cpu, entry point is 0x4037558c
I (0) cpu_start: App cpu up.
I (366) cpu_start: Pro cpu start user code
I (366) cpu_start: cpu freq: 160000000 Hz
I (367) cpu_start: Application information:
I (369) cpu_start: Project name:     esp-miner
I (375) cpu_start: App version:      v2.0.6
I (379) cpu_start: Compile time:     Jan 12 2024 14:00:45
I (386) cpu_start: ELF file SHA256:  d01bbe994f06fd40...
I (391) cpu_start: ESP-IDF:          v5.1-564-g8d2dbd461f
I (398) cpu_start: Min chip rev:     v0.0
I (402) cpu_start: Max chip rev:     v0.99 
I (407) cpu_start: Chip rev:         v0.2
I (412) heap_init: Initializing. RAM available for dynamic allocation:
I (419) heap_init: At 3FCA2350 len 000473C0 (284 KiB): DRAM
I (425) heap_init: At 3FCE9710 len 00005724 (21 KiB): STACK/DRAM
I (432) heap_init: At 3FCF0000 len 00008000 (32 KiB): DRAM
I (438) heap_init: At 600FE010 len 00001FD8 (7 KiB): RTCRAM
I (445) spi_flash: detected chip: gd
I (449) spi_flash: flash io: dio
W (453) ADC: legacy driver is deprecated, please migrate to `esp_adc/adc_oneshot.h`
I (461) sleep: Configure to isolate all GPIO pins in sleep state
I (468) sleep: Enable automatic switching of GPIO sleep configuration
I (475) app_start: Starting scheduler on CPU0
I (480) app_start: Starting scheduler on CPU1
I (480) main_task: Started on CPU0
I (490) main_task: Calling app_main()
I (530) miner: NVS_CONFIG_ASIC_FREQ 475.000000
I (530) miner: ASIC: BM1397
I (530) miner: Welcome to the bitaxe!
I (530) SystemModule: I2C initialized successfully
I (530) DS4432U.c: Set BM1397 voltage = 1.400V [0x90]
I (540) DS4432U.c: Writing 0x90
I (550) pp: pp rom version: e7ae62f
I (550) net80211: net80211 rom version: e7ae62f
I (560) wifi:wifi driver task: 3fcad868, prio:23, stack:6656, core=0
I (580) wifi:wifi firmware version: ce9244d
I (580) wifi:wifi certification version: v7.0
I (580) wifi:config NVS flash: enabled
I (580) wifi:config nano formating: disabled
I (580) wifi:Init data frame dynamic rx buffer num: 32
I (590) wifi:Init management frame dynamic rx buffer num: 32
I (590) wifi:Init management short buffer num: 32
I (600) wifi:Init dynamic tx buffer num: 32
I (600) wifi:Init static tx FG buffer num: 2
I (600) wifi:Init static rx buffer size: 1600
I (610) wifi:Init static rx buffer num: 10
I (610) wifi:Init dynamic rx buffer num: 32
I (620) wifi_init: rx ba win: 6
I (620) wifi_init: tcpip mbox: 32
I (620) wifi_init: udp mbox: 6
I (630) wifi_init: tcp mbox: 6
I (630) wifi_init: tcp tx win: 5744
I (640) wifi_init: tcp rx win: 5744
I (640) wifi_init: tcp mss: 1440
I (640) wifi_init: WiFi IRAM OP enabled
I (650) wifi_init: WiFi RX IRAM OP enabled
I (660) wifi station: ESP_WIFI Access Point On
W (660) wifi:Affected by the ESP-NOW encrypt num, set the max connection num to 10
I (670) wifi station: ESP_WIFI_MODE_STA
I (670) wifi station: wifi_init_sta finished.
I (680) phy_init: phy_version 601,98f2a71,Jun 29 2023,09:58:12
I (720) wifi:mode : sta (84:fc:e6:6c:90:dc) + softAP (84:fc:e6:6c:90:dd)
I (720) wifi:enable tsf
I (720) wifi:Total power save buffer number: 16
I (720) wifi:Init max length of beacon: 752/752
I (720) wifi:Init max length of beacon: 752/752
I (730) wifi station: wifi_init_sta finished.
I (730) esp_netif_lwip: DHCP server started on interface WIFI_AP_DEF with IP: 192.168.4.1
I (750) wifi:ap channel adjust o:1,1 n:6,2
I (750) wifi:new:<6,0>, old:<1,1>, ap:<6,2>, sta:<6,0>, prof:1
I (750) wifi:state: init -> auth (b0)
I (760) wifi:state: auth -> init (8a0)
I (760) wifi:new:<6,0>, old:<6,0>, ap:<6,2>, sta:<6,0>, prof:1
I (1010) http_server: Partition size: total: 2884241, used: 635030
I (1020) http_server: Starting HTTP Server
I (1020) example_dns_redirect_server: Socket created
I (1020) example_dns_redirect_server: Socket bound, port 53
I (1030) example_dns_redirect_server: Waiting for data
I (1040) SystemModule: OLED init success!
I (1760) wifi station: Retrying WiFi connection...
I (5590) wifi station: Retrying WiFi connection...
I (5600) wifi:new:<6,2>, old:<6,0>, ap:<6,2>, sta:<6,0>, prof:1
I (5600) wifi:state: init -> auth (b0)
I (5610) wifi:state: auth -> assoc (0)
I (5620) wifi:state: assoc -> run (10)
I (5650) wifi:connected with First_Class_Crew, aid = 1, channel 6, BW20, bssid = 44:4e:6d:14:7f:a6
I (5650) wifi:security: WPA2-PSK, phy: bgn, rssi: -66
I (5660) wifi:pm start, type: 1

I (5660) wifi:set rx beacon pti, rx_bcn_pti: 0, bcn_timeout: 25000, mt_pti: 0, mt_time: 10000
I (5670) wifi:AP's beacon interval = 102400 us, DTIM period = 1
I (5680) wifi:<ba-add>idx:0 (ifx:0, 44:4e:6d:14:7f:a6), tid:6, ssn:2, winSize:64
I (6670) wifi station: Bitaxe ip:192.168.178.76
I (6670) esp_netif_handlers: sta ip: 192.168.178.76, mask: 255.255.255.0, gw: 192.168.178.1
I (6670) miner: Connected to SSID: First_Class_Crew
I (6680) wifi station: ESP_WIFI Access Point Off
I (6680) wifi:mode : sta (84:fc:e6:6c:90:dc)
I (6690) serial: Initializing serial
I (6690) bm1397Module: Initializing BM1397
I (6910) bm1397Module: Setting job ASIC mask to 255
I (6960) bm1397Module: Setting Frequency to 475.00MHz (475.00)
I (6960) stratum_task: Get IP for URL: public-pool.io

I (6960) wifi:<ba-add>idx:1 (ifx:0, 44:4e:6d:14:7f:a6), tid:0, ssn:1, winSize:64
I (6970) stratum_task: Connecting to: stratum+tcp://public-pool.io:21496 (68.235.52.36)

I (6970) stratum_task: Socket created, connecting to 68.235.52.36:21496
I (6980) bm1397Module: Setting max baud of 3125000
I (6990) main_task: Returned from app_main()
I (7000) serial: Changing UART baud to 3125000
I (7000) ASIC_task: ASIC Ready!
I (7200) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe BM1397"]}

I (7400) stratum_api: Received result {"id":1,"error":null,"result":[[["mining.notify","703d5a17"]],"703d5a17",4]}
I (7400) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}

I (7570) stratum_api: Received result {"id":2,"error":null,"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"}}
I (7570) stratum_api: Set version mask: 1fffe000
I (7580) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [1000]}

I (7590) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "x"]}

I (7600) stratum_task: Extranonce: 703d5a17
I (7610) stratum_task: Extranonce 2 length: 4
I (7810) stratum_task: rx: {"id":3,"method":"mining.set_difficulty","params":[1000]}
I (7810) stratum_task: Set stratum difficulty: 1000
I (8020) stratum_task: rx: {"id":4,"error":null,"result":true}
I (8020) stratum_task: message result accepted
I (8430) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e6ea06","3204a2ea032aaf8354021061c384673ad0f13fd5000232170000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703bfb30c5075626c69632d506f6f6c","ffffffff02f145542800000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9ede21e9ded7894f76fb0077b58c72c75f2319cc349bb7929c8f8dff5f73cdbc1dc00000000",["f2de1cd0805037e591285086dccf4eb76b892ed3876a37e194d64c8a6023f01d","42b2e7ef0ec15bf6fab3dd9254845be6fe885da9ea6113ddfc69031af624cb9d","97a37b03b98f40e4bda35c9d835a3a2bac2f498946946b8830226cc596e38b6a","9f30e107fa015ad845828a7d399c39b1b3388a32646fcabf55616c8834ee1a14","bb798bf8f60cbfdc58b47ec5ff16028c21ffe6c116084831bb1e39f6f9dd7b70","1f2c676736d07e2bce84a6cccb524c6c928e1b02ab14fc905df9435bce7da587","6efea5ff739a3b52361a3d41a87e07639d11dbd56686281ea4c72b74eed2ea76","3817c8a8e3d192fa545c2375c565fdffc0e0d365ed831a7b3e22c9c4f70ca3a8","e983e47ce9da3d9a646dfd9e4da4d989fbc37a8ef62ba33b216c106484b0014a","912322be72d589219b8fb7aca62738023cfa8f73f86b5f20fbe6b1e73f74bfae","514d03370ed3c2a84a0b0c6f34a472d98b359b34f58553946931136fa933ac7c","d7fbfb87bfb0d0f65d02ff23525b976dd5df2e16a796b75dff70a2dca692454c"],"20000000","170371b1","65df9900",false]}
I (8530) SystemModule: Syncing clock
I (8530) create_jobs_task: New Work Dequeued e6ea06
I (8540) bm1397Module: Setting job ASIC mask to 511
I (46830) asic_result: Nonce difficulty 1419.66 of 1000.
I (46840) stratum_api: tx: {"id": 5, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ea06", "f50e0000", "65df9900", "0fd587d0", "00002000"]}

I (47130) stratum_task: rx: {"id":5,"error":null,"result":true}
I (47130) stratum_task: message result accepted
I (62190) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e6ee4a","3204a2ea032aaf8354021061c384673ad0f13fd5000232170000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703bfb30c5075626c69632d506f6f6c","ffffffff02f145542800000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9ede21e9ded7894f76fb0077b58c72c75f2319cc349bb7929c8f8dff5f73cdbc1dc00000000",["f2de1cd0805037e591285086dccf4eb76b892ed3876a37e194d64c8a6023f01d","42b2e7ef0ec15bf6fab3dd9254845be6fe885da9ea6113ddfc69031af624cb9d","97a37b03b98f40e4bda35c9d835a3a2bac2f498946946b8830226cc596e38b6a","9f30e107fa015ad845828a7d399c39b1b3388a32646fcabf55616c8834ee1a14","bb798bf8f60cbfdc58b47ec5ff16028c21ffe6c116084831bb1e39f6f9dd7b70","1f2c676736d07e2bce84a6cccb524c6c928e1b02ab14fc905df9435bce7da587","6efea5ff739a3b52361a3d41a87e07639d11dbd56686281ea4c72b74eed2ea76","3817c8a8e3d192fa545c2375c565fdffc0e0d365ed831a7b3e22c9c4f70ca3a8","e983e47ce9da3d9a646dfd9e4da4d989fbc37a8ef62ba33b216c106484b0014a","912322be72d589219b8fb7aca62738023cfa8f73f86b5f20fbe6b1e73f74bfae","514d03370ed3c2a84a0b0c6f34a472d98b359b34f58553946931136fa933ac7c","d7fbfb87bfb0d0f65d02ff23525b976dd5df2e16a796b75dff70a2dca692454c"],"20000000","170371b1","65df993c",false]}
I (62300) create_jobs_task: New Work Dequeued e6ee4a
I (68020) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[128]}
I (68020) stratum_task: Set stratum difficulty: 128
I (68430) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e6ee53","3204a2ea032aaf8354021061c384673ad0f13fd5000232170000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703bfb30c5075626c69632d506f6f6c","ffffffff02f145542800000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9ede21e9ded7894f76fb0077b58c72c75f2319cc349bb7929c8f8dff5f73cdbc1dc00000000",["f2de1cd0805037e591285086dccf4eb76b892ed3876a37e194d64c8a6023f01d","42b2e7ef0ec15bf6fab3dd9254845be6fe885da9ea6113ddfc69031af624cb9d","97a37b03b98f40e4bda35c9d835a3a2bac2f498946946b8830226cc596e38b6a","9f30e107fa015ad845828a7d399c39b1b3388a32646fcabf55616c8834ee1a14","bb798bf8f60cbfdc58b47ec5ff16028c21ffe6c116084831bb1e39f6f9dd7b70","1f2c676736d07e2bce84a6cccb524c6c928e1b02ab14fc905df9435bce7da587","6efea5ff739a3b52361a3d41a87e07639d11dbd56686281ea4c72b74eed2ea76","3817c8a8e3d192fa545c2375c565fdffc0e0d365ed831a7b3e22c9c4f70ca3a8","e983e47ce9da3d9a646dfd9e4da4d989fbc37a8ef62ba33b216c106484b0014a","912322be72d589219b8fb7aca62738023cfa8f73f86b5f20fbe6b1e73f74bfae","514d03370ed3c2a84a0b0c6f34a472d98b359b34f58553946931136fa933ac7c","d7fbfb87bfb0d0f65d02ff23525b976dd5df2e16a796b75dff70a2dca692454c"],"20000000","170371b1","65df993c",false]}
I (68550) create_jobs_task: New Work Dequeued e6ee53
I (68610) asic_result: Nonce difficulty 2451.03 of 1000.
I (68620) stratum_api: tx: {"id": 6, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee4a", "6a020000", "65df993c", "bbda0b90", "00000000"]}

I (68680) bm1397Module: Setting job ASIC mask to 127
I (68840) stratum_task: rx: {"id":6,"error":null,"result":true}
I (68840) stratum_task: message result accepted
I (69050) asic_result: Nonce difficulty 263.33 of 128.
I (69060) stratum_api: tx: {"id": 7, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "25000000", "65df993c", "8d8dc3b5", "00006000"]}

I (69250) stratum_task: rx: {"id":7,"error":null,"result":true}
I (69250) stratum_task: message result accepted
I (69790) asic_result: Nonce difficulty 261.66 of 128.
I (69800) stratum_api: tx: {"id": 8, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "6f000000", "65df993c", "4fa305bb", "00000000"]}

I (70070) stratum_task: rx: {"id":8,"error":null,"result":true}
I (70070) stratum_task: message result accepted
I (71220) asic_result: Nonce difficulty 148.55 of 128.
I (71230) stratum_api: tx: {"id": 9, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "fe000000", "65df993c", "106584d3", "00000000"]}

I (71610) stratum_task: rx: {"id":9,"error":null,"result":true}
I (71610) stratum_task: message result accepted
I (74800) asic_result: Nonce difficulty 275.81 of 128.
I (74810) stratum_api: tx: {"id": 10, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "64020000", "65df993c", "dc8c8b87", "00002000"]}

I (74860) asic_result: Nonce difficulty 2451.03 of 128.
I (74870) stratum_api: tx: {"id": 11, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "6a020000", "65df993c", "bbda0b90", "00000000"]}

I (75090) stratum_task: rx: {"id":10,"error":null,"result":true}
I (75090) stratum_task: message result accepted
I (75290) stratum_task: rx: {"id":11,"error":null,"result":true}
I (75290) stratum_task: message result accepted
I (77610) asic_result: Nonce difficulty 159.87 of 128.
I (77620) stratum_api: tx: {"id": 12, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "7d030000", "65df993c", "8f1ec597", "00000000"]}

I (77850) stratum_task: rx: {"id":12,"error":null,"result":true}
I (77850) stratum_task: message result accepted
I (78260) asic_result: Nonce difficulty 1036.99 of 128.
I (78270) stratum_api: tx: {"id": 13, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "bd030000", "65df993c", "5e7a9146", "00000000"]}

I (78470) stratum_task: rx: {"id":13,"error":null,"result":true}
I (78470) stratum_task: message result accepted
I (78730) asic_result: Nonce difficulty 165.55 of 128.
I (78740) stratum_api: tx: {"id": 14, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "ed030000", "65df993c", "10e4c71c", "00006000"]}

I (78980) stratum_task: rx: {"id":14,"error":null,"result":true}
I (78980) stratum_task: message result accepted
I (79010) asic_result: Nonce difficulty 311.70 of 128.
I (79020) stratum_api: tx: {"id": 15, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "09040000", "65df993c", "ff7d8624", "00006000"]}

I (79290) stratum_task: rx: {"id":15,"error":null,"result":true}
I (79290) stratum_task: message result accepted
I (79700) asic_result: Nonce difficulty 210.72 of 128.
I (79710) stratum_api: tx: {"id": 16, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "4e040000", "65df993c", "0dbb0a8c", "00006000"]}

I (79900) stratum_task: rx: {"id":16,"error":null,"result":true}
I (79900) stratum_task: message result accepted
I (87280) asic_result: Nonce difficulty 130.14 of 128.
I (87290) stratum_api: tx: {"id": 17, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "44070000", "65df993c", "e813c53b", "00002000"]}

I (87480) stratum_task: rx: {"id":17,"error":null,"result":true}
I (87480) stratum_task: message result accepted
I (88520) asic_result: Nonce difficulty 342.13 of 128.
I (88530) stratum_api: tx: {"id": 18, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "c0070000", "65df993c", "6edacb28", "00002000"]}

I (88810) stratum_task: rx: {"id":18,"error":null,"result":true}
I (88810) stratum_task: message result accepted
I (90850) asic_result: Nonce difficulty 172.97 of 128.
I (90860) stratum_api: tx: {"id": 19, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "a9080000", "65df993c", "a4730bac", "00006000"]}

I (91060) stratum_task: rx: {"id":19,"error":null,"result":true}
I (91060) stratum_task: message result accepted
I (99860) asic_result: Nonce difficulty 318.70 of 128.
I (99870) stratum_api: tx: {"id": 20, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "2e0c0000", "65df993c", "2ab4c240", "00002000"]}

I (100070) stratum_task: rx: {"id":20,"error":null,"result":true}
I (100070) stratum_task: message result accepted
I (102970) asic_result: Nonce difficulty 201.05 of 128.
I (102980) stratum_api: tx: {"id": 21, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "650d0000", "65df993c", "985e8a51", "00002000"]}

I (102990) asic_result: Nonce difficulty 504.55 of 128.
I (103000) stratum_api: tx: {"id": 22, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "650d0000", "65df993c", "0465114d", "00000000"]}

I (103250) stratum_task: rx: {"id":21,"error":null,"result":true}
I (103250) stratum_task: message result accepted
I (103450) stratum_task: rx: {"id":22,"error":null,"result":true}
I (103450) stratum_task: message result accepted
I (105510) asic_result: Nonce difficulty 138.14 of 128.
I (105520) stratum_api: tx: {"id": 23, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "630e0000", "65df993c", "ea0f4b11", "00004000"]}

I (105700) stratum_task: rx: {"id":23,"error":null,"result":true}
I (105710) stratum_task: message result accepted
I (105910) asic_result: Nonce difficulty 498.42 of 128.
I (105920) stratum_api: tx: {"id": 24, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "8b0e0000", "65df993c", "01840e90", "00004000"]}

I (106260) asic_result: Nonce difficulty 522.67 of 128.
I (106270) stratum_api: tx: {"id": 25, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "ae0e0000", "65df993c", "5ebf0742", "00002000"]}

I (106370) stratum_task: rx: {"id":24,"error":null,"result":true}
I (106370) stratum_task: message result accepted
I (106530) asic_result: Nonce difficulty 458.34 of 128.
I (106540) stratum_api: tx: {"id": 26, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "c90e0000", "65df993c", "f2514ab2", "00006000"]}

I (106730) stratum_task: rx: {"id":25,"error":null,"result":true}
I (106730) stratum_task: message result accepted
I (106800) asic_result: Nonce difficulty 262.90 of 128.
I (106810) stratum_api: tx: {"id": 27, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "e30e0000", "65df993c", "1b8a51b1", "00002000"]}

I (106850) asic_result: Nonce difficulty 1063.56 of 128.
I (106860) stratum_api: tx: {"id": 28, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "e90e0000", "65df993c", "2843430f", "00006000"]}

I (106930) stratum_task: rx: {"id":26,"error":null,"result":true}
I (106940) stratum_task: message result accepted
I (107140) stratum_task: rx: {"id":27,"error":null,"result":true}
I (107140) stratum_task: message result accepted
I (107450) stratum_task: rx: {"id":28,"error":null,"result":true}
I (107450) stratum_task: message result accepted
I (108150) asic_result: Nonce difficulty 661.18 of 128.
I (108150) stratum_api: tx: {"id": 29, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "6b0f0000", "65df993c", "2dca862d", "00004000"]}

I (108370) stratum_task: rx: {"id":29,"error":null,"result":true}
I (108370) stratum_task: message result accepted
I (111000) asic_result: Nonce difficulty 146.86 of 128.
I (111010) stratum_api: tx: {"id": 30, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "88100000", "65df993c", "02908e94", "00004000"]}

I (111340) stratum_task: rx: {"id":30,"error":null,"result":true}
I (111340) stratum_task: message result accepted
I (111450) asic_result: Nonce difficulty 180.07 of 128.
I (111450) stratum_api: tx: {"id": 31, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "b5100000", "65df993c", "d44bc4b8", "00000000"]}

I (111560) asic_result: Nonce difficulty 855.01 of 128.
I (111560) stratum_api: tx: {"id": 32, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "c0100000", "65df993c", "0f354084", "00004000"]}

I (111750) stratum_task: rx: {"id":31,"error":null,"result":true}
I (111750) stratum_task: message result accepted
I (111950) stratum_task: rx: {"id":32,"error":null,"result":true}
I (111950) stratum_task: message result accepted
I (112910) asic_result: Nonce difficulty 405.50 of 128.
I (112910) stratum_api: tx: {"id": 33, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "47110000", "65df993c", "e147c4cc", "00002000"]}

I (113070) asic_result: Nonce difficulty 178.84 of 128.
I (113070) stratum_api: tx: {"id": 34, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "57110000", "65df993c", "d9f38791", "00004000"]}

I (113180) stratum_task: rx: {"id":33,"error":null,"result":true}
I (113180) stratum_task: message result accepted
I (113380) stratum_task: rx: {"id":34,"error":null,"result":true}
I (113390) stratum_task: message result accepted
I (115530) asic_result: Nonce difficulty 177.74 of 128.
I (115530) stratum_api: tx: {"id": 35, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "4d120000", "65df993c", "d7db4298", "00002000"]}

I (115740) stratum_task: rx: {"id":35,"error":null,"result":true}
I (115740) stratum_task: message result accepted
I (120400) asic_result: Nonce difficulty 155.47 of 128.
I (120400) stratum_api: tx: {"id": 36, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "33140000", "65df993c", "7b52d103", "00006000"]}

I (120660) stratum_task: rx: {"id":36,"error":null,"result":true}
I (120660) stratum_task: message result accepted
I (121670) asic_result: Nonce difficulty 294.51 of 128.
I (121670) stratum_api: tx: {"id": 37, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6ee53", "b3140000", "65df993c", "5327c386", "00006000"]}

I (122090) stratum_task: rx: {"id":37,"error":null,"result":true}
I (122090) stratum_task: message result accepted
I (122400) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e6f296","3204a2ea032aaf8354021061c384673ad0f13fd5000232170000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703bfb30c5075626c69632d506f6f6c","ffffffff02f145542800000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9ede21e9ded7894f76fb0077b58c72c75f2319cc349bb7929c8f8dff5f73cdbc1dc00000000",["f2de1cd0805037e591285086dccf4eb76b892ed3876a37e194d64c8a6023f01d","42b2e7ef0ec15bf6fab3dd9254845be6fe885da9ea6113ddfc69031af624cb9d","97a37b03b98f40e4bda35c9d835a3a2bac2f498946946b8830226cc596e38b6a","9f30e107fa015ad845828a7d399c39b1b3388a32646fcabf55616c8834ee1a14","bb798bf8f60cbfdc58b47ec5ff16028c21ffe6c116084831bb1e39f6f9dd7b70","1f2c676736d07e2bce84a6cccb524c6c928e1b02ab14fc905df9435bce7da587","6efea5ff739a3b52361a3d41a87e07639d11dbd56686281ea4c72b74eed2ea76","3817c8a8e3d192fa545c2375c565fdffc0e0d365ed831a7b3e22c9c4f70ca3a8","e983e47ce9da3d9a646dfd9e4da4d989fbc37a8ef62ba33b216c106484b0014a","912322be72d589219b8fb7aca62738023cfa8f73f86b5f20fbe6b1e73f74bfae","514d03370ed3c2a84a0b0c6f34a472d98b359b34f58553946931136fa933ac7c","d7fbfb87bfb0d0f65d02ff23525b976dd5df2e16a796b75dff70a2dca692454c"],"20000000","170371b1","65df9978",false]}
I (122510) create_jobs_task: New Work Dequeued e6f296
I (123520) asic_result: Nonce difficulty 541.23 of 128.
I (123520) stratum_api: tx: {"id": 38, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6f296", "58000000", "65df9978", "16d24821", "00006000"]}

I (123730) stratum_task: rx: {"id":38,"error":null,"result":true}
I (123730) stratum_task: message result accepted
I (126640) asic_result: Nonce difficulty 586.63 of 128.
I (126640) stratum_api: tx: {"id": 39, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6f296", "90010000", "65df9978", "4a76048d", "00006000"]}

I (126660) asic_result: Nonce difficulty 2117.23 of 128.
I (126670) stratum_api: tx: {"id": 40, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6f296", "92010000", "65df9978", "3349ceb5", "00000000"]}

I (126900) stratum_task: rx: {"id":39,"error":null,"result":true}
I (126900) stratum_task: message result accepted
I (127110) stratum_task: rx: {"id":40,"error":null,"result":true}
I (127110) stratum_task: message result accepted
I (128030) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[512]}
I (128030) stratum_task: Set stratum difficulty: 512
I (128440) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e6f2a5","3204a2ea032aaf8354021061c384673ad0f13fd5000232170000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703bfb30c5075626c69632d506f6f6c","ffffffff02f145542800000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9ede21e9ded7894f76fb0077b58c72c75f2319cc349bb7929c8f8dff5f73cdbc1dc00000000",["f2de1cd0805037e591285086dccf4eb76b892ed3876a37e194d64c8a6023f01d","42b2e7ef0ec15bf6fab3dd9254845be6fe885da9ea6113ddfc69031af624cb9d","97a37b03b98f40e4bda35c9d835a3a2bac2f498946946b8830226cc596e38b6a","9f30e107fa015ad845828a7d399c39b1b3388a32646fcabf55616c8834ee1a14","bb798bf8f60cbfdc58b47ec5ff16028c21ffe6c116084831bb1e39f6f9dd7b70","1f2c676736d07e2bce84a6cccb524c6c928e1b02ab14fc905df9435bce7da587","6efea5ff739a3b52361a3d41a87e07639d11dbd56686281ea4c72b74eed2ea76","3817c8a8e3d192fa545c2375c565fdffc0e0d365ed831a7b3e22c9c4f70ca3a8","e983e47ce9da3d9a646dfd9e4da4d989fbc37a8ef62ba33b216c106484b0014a","912322be72d589219b8fb7aca62738023cfa8f73f86b5f20fbe6b1e73f74bfae","514d03370ed3c2a84a0b0c6f34a472d98b359b34f58553946931136fa933ac7c","d7fbfb87bfb0d0f65d02ff23525b976dd5df2e16a796b75dff70a2dca692454c"],"20000000","170371b1","65df9978",false]}
I (128550) create_jobs_task: New Work Dequeued e6f2a5
I (128610) asic_result: Nonce difficulty 137.06 of 128.
I (128620) stratum_api: tx: {"id": 41, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6f296", "55020000", "65df9978", "6140ce51", "00002000"]}

I (128680) bm1397Module: Setting job ASIC mask to 511
I (128850) stratum_task: rx: {"id":41,"result":null,"error":[23,"Difficulty too low",""]}
I (129560) asic_result: Nonce difficulty 541.23 of 512.
I (129570) stratum_api: tx: {"id": 42, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6f2a5", "58000000", "65df9978", "16d24821", "00006000"]}

I (129770) stratum_task: rx: {"id":42,"error":null,"result":true}
I (129770) stratum_task: message result accepted
I (132680) asic_result: Nonce difficulty 586.63 of 512.
I (132690) stratum_api: tx: {"id": 43, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6f2a5", "90010000", "65df9978", "4a76048d", "00006000"]}

I (132940) stratum_task: rx: {"id":43,"error":null,"result":true}
I (132940) stratum_task: message result accepted
I (141780) asic_result: Nonce difficulty 1193.19 of 512.
I (141790) stratum_api: tx: {"id": 44, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6f2a5", "1e050000", "65df9978", "08afcab3", "00000000"]}

I (142060) stratum_task: rx: {"id":44,"error":null,"result":true}
I (142060) stratum_task: message result accepted
I (148210) asic_result: Nonce difficulty 3630.34 of 512.
I (148220) stratum_api: tx: {"id": 45, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6f2a5", "a1070000", "65df9978", "6956cfb8", "00002000"]}

I (148510) stratum_task: rx: {"id":45,"error":null,"result":true}
I (148510) stratum_task: message result accepted
I (149880) asic_result: Nonce difficulty 546.89 of 512.
I (149890) stratum_api: tx: {"id": 46, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6f2a5", "47080000", "65df9978", "7c5d9134", "00002000"]}

I (150150) stratum_task: rx: {"id":46,"error":null,"result":true}
I (150150) stratum_task: message result accepted
I (158170) asic_result: Nonce difficulty 1283.78 of 512.
I (158180) stratum_api: tx: {"id": 47, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6f2a5", "850b0000", "65df9978", "ddb00dc3", "00006000"]}

I (158440) stratum_task: rx: {"id":47,"error":null,"result":true}
I (158440) stratum_task: message result accepted
I (160160) asic_result: Nonce difficulty 13950.16 of 512.
I (160190) SystemModule: Network diff: 81725299822043.218750
I (160190) stratum_api: tx: {"id": 48, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6f2a5", "4c0c0000", "65df9978", "fa448fcf", "00006000"]}

I (160390) stratum_task: rx: {"id":48,"error":null,"result":true}
I (160390) stratum_task: message result accepted
I (167170) asic_result: Nonce difficulty 1590.99 of 512.
I (167170) stratum_api: tx: {"id": 49, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6f2a5", "090f0000", "65df9978", "368b474c", "00000000"]}

I (167450) stratum_task: rx: {"id":49,"error":null,"result":true}
I (167450) stratum_task: message result accepted
I (171380) asic_result: Nonce difficulty 1069.36 of 512.
I (171380) stratum_api: tx: {"id": 50, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6f2a5", "ae100000", "65df9978", "4d89440e", "00004000"]}

I (171590) asic_result: Nonce difficulty 3254.02 of 512.
I (171590) stratum_api: tx: {"id": 51, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6f2a5", "c3100000", "65df9978", "1c040b4f", "00006000"]}

I (171750) stratum_task: rx: {"id":50,"error":null,"result":true}
I (171750) stratum_task: message result accepted
I (171960) stratum_task: rx: {"id":51,"error":null,"result":true}
I (171960) stratum_task: message result accepted
I (176640) asic_result: Nonce difficulty 1343.47 of 512.
I (176640) stratum_api: tx: {"id": 52, "method": "mining.submit", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "e6f2a5", "bc120000", "65df9978", "35b64d32", "00000000"]}

### xXAsystolieXx on 2024-02-28

Only for comparison, this log is with version 2.0.6 and my Bitaxe starts to Hashen 

### FragOmatig on 2024-02-28

> 
> Your board version is wrong, it should be 0.11 by the way, not "204". Seems you may have changed that in the config.cvs file by accident.

can anyone help me plz? 


### qubyt3 on 2024-02-28

@FragOmatig you can try something else if the web flasher dint work for you. 
Go to AxeOS Settings tab
Under Latest Release: V2.0.7 click esp-miner.bin and www.bin to download the two files.
Then under Update Firmware click on chose file and select the esp-miner.bin you just downloaded. Wait for the flash to complete and reboot.
Then do the same under Update Website and select the www.bin file you just downloaded. 

If that doesn't work, please open another issue in GIT for your problem and we'll troubleshoot further there. 


### xXAsystolieXx on 2024-02-28

> > Your board version is wrong, it should be 0.11 by the way, not "204". Seems you may have changed that in the config.cvs file by accident.
> 
> can anyone help me plz

How do you flash your bitaxe? 

### FragOmatig on 2024-02-28

with https://wantclue.github.io/bitaxe-web-flasher/ 

i dont now what the last user do with it.


### FragOmatig on 2024-02-28

thx i try it :)

### xXAsystolieXx on 2024-02-28

@FragOmatig Have you ever tried the terminal in Linux? 

### FragOmatig on 2024-02-28

no i have a laptop with ubuntu, thats a good idea. 

### xXAsystolieXx on 2024-02-28

I just don't know if Windows alone works with the PowerShell. I just don't know why you should have board version 0.11 instead of 204, I can't get a version number on your board

### FragOmatig on 2024-02-28

thats the riddle. 
on ubuntu i must install bitaxetool for the console?

### xXAsystolieXx on 2024-02-28

> thats the riddle. on ubuntu i must install bitaxetool for the console?

Yes

### qubyt3 on 2024-02-28

powershell works, or he can use vs code and use the terminal there. 

In any case I din't say it would fix anything, just that a configuration was sent to the BitAxe with board version 204. 

The Bitaxe GIT repot recommends a configuration for the BM1366 that the board version (not the firmware version) is noted as: boardversion,data,string,0.11 (version 0.11). 

I din't say it would fix his issue, just pointing that someone may have played with the config.cvs file and that maybe reinstalling his firmware and getting him back to factory would get him mining again.

### xXAsystolieXx on 2024-02-28

@qubyt3  Ok, I understand I'm trying to explain it to him as I did it. Maybe I can help him like that👌🏻

### FragOmatig on 2024-02-28

i try esp-miner.bin and www.bin in web Gui. On screen Show Working for any minutes an close. 
no error or succsess text are showing. not mining. F***ing up :D  

lets try ubuntu console. installing python3-pip....

### qubyt3 on 2024-02-28

Did you hit the button restart after? Still not hashing? :)

Alternatively, I see you bought it from D-Central, you can reach out to them and they might be able to help (warranty if applicable). 

### xXAsystolieXx on 2024-02-28

@FragOmatig I had bought the first Bitaxe and updated the firmware to version 2.0.4 via the web interface. Suddenly my bitaxe didn't work anymore and I had no idea how to get it to work again but I laboriously googled everything together and it worked, Although I had absolutely no idea about Terminal and Linux🤣🤣

### FragOmatig on 2024-02-28

@xXAsystolieXx 

ha ha :D 
this miner let me grow grey hair^^ im still google every time. not my first time with esp32. but this thing are creazy shit  :P

### FragOmatig on 2024-02-28

yes i hit the button restart 

### pinokio240 on 2024-02-29

> @pinokio240 did yours ever work? You're missing 6 resistors at the top.

Yes, sure. When I wanted to try another pool, problems began with solving the problem. I updated the firmware to the latest and “miracles” began

### WantClue on 2024-03-05

please consider updating to 2.1.0 and tell back if this behaviour still persists

### xXAsystolieXx on 2024-03-05

Log from Firmware 2.1.0. but unfortunately my problems still exist and my bitaxe still has 0 GH/s :( 

I (346768) stratum_task: rx: {"id":null,"method":"mining.I (406958) stratum_task: rx: {"id":null,"method":"mining.notify","params":["749d47","55217045e923809198db99506f4e93d76e970a3f000022b70000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff17030bb70c5075626c69632d506f6f6c","ffffffff02d152332900000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9ed85b62dbe01d9276d64148ff95b3d5f94e4798789766a2771106b5aaa6a99f75700000000",["d55f517f7a35133599c753bb5d6aea189902ca4468827cc2ea84f31d4797d9d0","4071d6d13aef3cff598c181dc4bf105b0a4d5b9dce91f5cb6535ccd4a9bb94cd","a92e65655c42b6553732d1903c9e7423077f4225ab16ecb7d0a91cfd0b90fa90","88a08e3572535ec59960ebff067aeb5b234842bbbb1511568cc65c9687b97123","bb7a3c9ae8091ce4ab56fb03a91effbc8fc83506243fa69d54d29c80066d0f4f","0e7ee4965093aeb17d828e18be0a623791cad72ab9a64fad371b56e047a32689","ee823051687a13f5de11022b4fa9b2a61215ef9da5b91998eb5944b281a59ac6","15735ebfdca2594910cbe905c2ea03842eca56c9c5766f9124a3d23858854b4f","f08097d79c30b650bdf539921811a17a4183b4df1b44072cce657abe8c0aa72f","d9d441d7172404db6845a886d549ed5c9b2d22d9e26b4d8741b4056ba043f7d5","b9e5353dded51be418617db44385ea92a0615e075061bcfa5d408236e7de0297","4f90ff46bc4139765ddabbebb96b8f31e9a634b12008af67f71f4858abfc33b3"],"20000000","17038c12","65e75aa6",false]}
I (407068) create_jobs_task: New Work Dequeued 749d47
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0x15 (USB_UART_CHIP_RESET),boot:0x28 (SPI_FAST_FLASH_BOOT)
Saved PC:0x4037b8b2
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce3818,len:0x16e0
load:0x403c9700,len:0x4
load:0x403c9704,len:0xc00
load:0x403cc700,len:0x2eb0
entry 0x403c9908
I (27) boot: ESP-IDF v5.1 2nd stage bootloader
I (27) boot: compile time Mar  3 2024 19:55:36
I (27) boot: Multicore bootloader
I (30) boot: chip revision: v0.2
I (34) boot.esp32s3: Boot SPI Speed : 80MHz
I (38) boot.esp32s3: SPI Mode       : DIO
I (43) boot.esp32s3: SPI Flash Size : 16MB
I (48) boot: Enabling RNG early entropy source...
I (53) boot: Partition Table:
I (57) boot: ## Label            Usage          Type ST Offset   Length
I (64) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (72) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (79) boot:  2 factory          factory app      00 00 00010000 00400000
I (87) boot:  3 www              Unknown data     01 82 00410000 00300000
I (94) boot:  4 ota_0            OTA app          00 10 00710000 00400000
I (101) boot:  5 ota_1            OTA app          00 11 00b10000 00400000
I (109) boot:  6 otadata          OTA data         01 00 00f10000 00002000
I (117) boot:  7 coredump         Unknown data     01 03 00f12000 00010000
I (124) boot: End of partition table
I (128) boot: Defaulting to factory image
I (133) esp_image: segment 0: paddr=00010020 vaddr=3c0b0020 size=2a194h (172436) map
I (173) esp_image: segment 1: paddr=0003a1bc vaddr=3fc98100 size=04bbch ( 19388) load
I (177) esp_image: segment 2: paddr=0003ed80 vaddr=40374000 size=01298h (  4760) load
I (179) esp_image: segment 3: paddr=00040020 vaddr=42000020 size=a6d20h (683296) map
I (309) esp_image: segment 4: paddr=000e6d48 vaddr=40375298 size=12e54h ( 77396) load
I (335) boot: Loaded app from partition at offset 0x10000
I (336) boot: Disabling RNG early entropy source...
I (347) cpu_start: Multicore app
I (347) cpu_start: Pro cpu up.
I (347) cpu_start: Starting app cpu, entry point is 0x40375584
I (0) cpu_start: App cpu up.
I (366) cpu_start: Pro cpu start user code
I (366) cpu_start: cpu freq: 160000000 Hz
I (366) cpu_start: Application information:
I (369) cpu_start: Project name:     esp-miner
I (374) cpu_start: App version:      v2.1.0
I (379) cpu_start: Compile time:     Mar  3 2024 19:54:36
I (385) cpu_start: ELF file SHA256:  9b1e3cabceff5618...
I (391) cpu_start: ESP-IDF:          v5.1
I (395) cpu_start: Min chip rev:     v0.0
I (400) cpu_start: Max chip rev:     v0.99 
I (405) cpu_start: Chip rev:         v0.2
I (410) heap_init: Initializing. RAM available for dynamic allocation:
I (417) heap_init: At 3FCA2460 len 000472B0 (284 KiB): DRAM
I (423) heap_init: At 3FCE9710 len 00005724 (21 KiB): STACK/DRAM
I (430) heap_init: At 3FCF0000 len 00008000 (32 KiB): DRAM
I (436) heap_init: At 600FE010 len 00001FF0 (7 KiB): RTCRAM
I (443) spi_flash: detected chip: gd
I (446) spi_flash: flash io: dio
W (451) ADC: legacy driver is deprecated, please migrate to `esp_adc/adc_oneshot.h`
I (459) sleep: Configure to isolate all GPIO pins in sleep state
I (466) sleep: Enable automatic switching of GPIO sleep configuration
I (473) app_start: Starting scheduler on CPU0
I (478) app_start: Starting scheduler on CPU1
I (478) main_task: Started on CPU0
I (488) main_task: Calling app_main()
I (528) miner: NVS_CONFIG_ASIC_FREQ 475.000000
I (528) miner: ASIC: BM1397
I (528) miner: Welcome to the bitaxe!
I (528) SystemModule: I2C initialized successfully
I (538) DS4432U.c: Set BM1397 voltage = 1.400V [0x90]
I (538) DS4432U.c: Writing 0x90
I (548) pp: pp rom version: e7ae62f
I (548) net80211: net80211 rom version: e7ae62f
I (558) wifi:wifi driver task: 3fcad9a8, prio:23, stack:6656, core=0
I (578) wifi:wifi firmware version: b2f1f86
I (578) wifi:wifi certification version: v7.0
I (578) wifi:config NVS flash: enabled
I (578) wifi:config nano formating: disabled
I (578) wifi:Init data frame dynamic rx buffer num: 32
I (588) wifi:Init management frame dynamic rx buffer num: 32
I (588) wifi:Init management short buffer num: 32
I (598) wifi:Init dynamic tx buffer num: 32
I (598) wifi:Init static tx FG buffer num: 2
I (608) wifi:Init static rx buffer size: 1600
I (608) wifi:Init static rx buffer num: 10
I (608) wifi:Init dynamic rx buffer num: 32
I (618) wifi_init: rx ba win: 6
I (618) wifi_init: tcpip mbox: 32
I (628) wifi_init: udp mbox: 6
I (628) wifi_init: tcp mbox: 6
I (628) wifi_init: tcp tx win: 5744
I (638) wifi_init: tcp rx win: 5744
I (638) wifi_init: tcp mss: 1440
I (638) wifi_init: WiFi IRAM OP enabled
I (648) wifi_init: WiFi RX IRAM OP enabled
I (658) wifi station: ESP_WIFI Access Point On
W (658) wifi:Affected by the ESP-NOW encrypt num, set the max connection num to 10
I (668) wifi station: ESP_WIFI_MODE_STA
I (668) wifi station: wifi_init_sta finished.
I (678) phy_init: phy_version 601,fe52df4,May 10 2023,17:26:54
I (718) wifi:mode : sta (84:fc:e6:6c:90:dc) + softAP (84:fc:e6:6c:90:dd)
I (718) wifi:enable tsf
I (718) wifi:Total power save buffer number: 16
I (718) wifi:Init max length of beacon: 752/752
I (718) wifi:Init max length of beacon: 752/752
I (728) wifi station: wifi_init_sta finished.
I (728) esp_netif_lwip: DHCP server started on interface WIFI_AP_DEF with IP: 192.168.4.1
I (738) wifi:new:<1,1>, old:<1,1>, ap:<1,1>, sta:<1,0>, prof:1
I (748) wifi:state: init -> auth (b0)
I (748) wifi:state: auth -> init (8a0)
I (758) wifi:new:<1,0>, old:<1,1>, ap:<1,1>, sta:<1,0>, prof:1
I (1018) http_server: Partition size: total: 2884241, used: 664397
I (1028) http_server: Starting HTTP Server
I (1028) example_dns_redirect_server: Socket created
I (1028) example_dns_redirect_server: Socket bound, port 53
I (1038) example_dns_redirect_server: Waiting for data
I (1038) SystemModule: OLED init success!
I (1758) wifi station: Retrying WiFi connection...
I (1768) wifi:new:<1,1>, old:<1,0>, ap:<1,1>, sta:<1,0>, prof:1
I (1768) wifi:state: init -> auth (b0)
I (1768) wifi:state: auth -> assoc (0)
I (1808) wifi:state: assoc -> run (10)
I (1838) wifi:connected with First_Class_Crew, aid = 2, channel 1, BW20, bssid = 44:4e:6d:14:7f:a6
I (1838) wifi:security: WPA2-PSK, phy: bgn, rssi: -64
I (1848) wifi:pm start, type: 1

I (1848) wifi:set rx beacon pti, rx_bcn_pti: 0, bcn_timeout: 25000, mt_pti: 0, mt_time: 10000
I (1858) wifi:<ba-add>idx:0 (ifx:0, 44:4e:6d:14:7f:a6), tid:6, ssn:2, winSize:64
I (1868) wifi:AP's beacon interval = 102400 us, DTIM period = 1
I (2858) wifi station: Bitaxe ip:192.168.178.76
I (2858) esp_netif_handlers: sta ip: 192.168.178.76, mask: 255.255.255.0, gw: 192.168.178.1
I (2858) miner: Connected to SSID: First_Class_Crew
I (2868) gpio: GPIO[12]| InputEn: 1| OutputEn: 0| OpenDrain: 0| Pullup: 0| Pulldown: 0| Intr:0 
I (2878) wifi station: ESP_WIFI Access Point Off
I (2878) wifi:mode : sta (84:fc:e6:6c:90:dc)
I (2888) serial: Initializing serial
I (2888) bm1397Module: Initializing BM1397
I (3108) bm1397Module: Setting job ASIC mask to 255
I (3158) bm1397Module: Setting Frequency to 475.00MHz (475.00)
I (3158) stratum_task: Get IP for URL: public-pool.io

I (3158) bm1397Module: Setting max baud of 3125000
I (3158) main_task: Returned from app_main()
I (3168) serial: Changing UART baud to 3125000
I (3168) ASIC_task: ASIC Ready!
I (3178) wifi:<ba-add>idx:1 (ifx:0, 44:4e:6d:14:7f:a6), tid:0, ssn:0, winSize:64
I (3178) stratum_task: Connecting to: stratum+tcp://public-pool.io:21496 (68.235.52.36)

I (3188) stratum_task: Socket created, connecting to 68.235.52.36:21496
I (3408) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe/BM1397"]}

I (3568) stratum_api: Received result {"id":1,"error":null,"result":[[["mining.notify","165411d9"]],"165411d9",4]}
I (3568) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}

I (3818) stratum_api: Received result {"id":2,"error":null,"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"}}
I (3818) stratum_api: Set version mask: 1fffe000
I (3828) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [512]}

I (3838) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["bc1qacyyrr9495tlvyaku4rxkdmd2muttjr73ly6h0.tobisbitaxe", "x"]}

I (4018) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[512]}
I (4028) stratum_task: Set stratum difficulty: 512
I (4228) stratum_task: rx: {"id":4,"error":null,"result":true}
I (4228) stratum_task: message result accepted
I (4638) stratum_task: rx: {"id":null,"method":"mining.notify","params":["72d309","55217045e923809198db99506f4e93d76e970a3f000022b70000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff17030bb70c5075626c69632d506f6f6c","ffffffff02d152332900000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9ed85b62dbe01d9276d64148ff95b3d5f94e4798789766a2771106b5aaa6a99f75700000000",["d55f517f7a35133599c753bb5d6aea189902ca4468827cc2ea84f31d4797d9d0","4071d6d13aef3cff598c181dc4bf105b0a4d5b9dce91f5cb6535ccd4a9bb94cd","a92e65655c42b6553732d1903c9e7423077f4225ab16ecb7d0a91cfd0b90fa90","88a08e3572535ec59960ebff067aeb5b234842bbbb1511568cc65c9687b97123","bb7a3c9ae8091ce4ab56fb03a91effbc8fc83506243fa69d54d29c80066d0f4f","0e7ee4965093aeb17d828e18be0a623791cad72ab9a64fad371b56e047a32689","ee823051687a13f5de11022b4fa9b2a61215ef9da5b91998eb5944b281a59ac6","15735ebfdca2594910cbe905c2ea03842eca56c9c5766f9124a3d23858854b4f","f08097d79c30b650bdf539921811a17a4183b4df1b44072cce657abe8c0aa72f","d9d441d7172404db6845a886d549ed5c9b2d22d9e26b4d8741b4056ba043f7d5","b9e5353dded51be418617db44385ea92a0615e075061bcfa5d408236e7de0297","4f90ff46bc4139765ddabbebb96b8f31e9a634b12008af67f71f4858abfc33b3"],"20000000","17038c12","65e75a81",false]}
I (4738) SystemModule: Syncing clock
I (4748) create_jobs_task: New Work Dequeued 72d309
I (4758) bm1397Module: Setting job ASIC mask to 511
I (18768) stratum_task: rx: {"id":null,"method":"mining.notify","params":["72d313","55217045e923809198db99506f4e93d76e970a3f000022b70000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff17030bb70c5075626c69632d506f6f6c","ffffffff02d152332900000000160014ee08418cb52d17f613b6e5466b376d56f8b5c87e0000000000000000266a24aa21a9ed85b62dbe01d9276d64148ff95b3d5f94e4798789766a2771106b5aaa6a99f75700000000",["d55f517f7a35133599c753bb5d6aea189902ca4468827cc2ea84f31d4797d9d0","4071d6d13aef3cff598c181dc4bf105b0a4d5b9dce91f5cb6535ccd4a9bb94cd","a92e65655c42b6553732d1903c9e7423077f4225ab16ecb7d0a91cfd0b90fa90","88a08e3572535ec59960ebff067aeb5b234842bbbb1511568cc65c9687b97123","bb7a3c9ae8091ce4ab56fb03a91effbc8fc83506243fa69d54d29c80066d0f4f","0e7ee4965093aeb17d828e18be0a623791cad72ab9a64fad371b56e047a32689","ee823051687a13f5de11022b4fa9b2a61215ef9da5b91998eb5944b281a59ac6","15735ebfdca2594910cbe905c2ea03842eca56c9c5766f9124a3d23858854b4f","f08097d79c30b650bdf539921811a17a4183b4df1b44072cce657abe8c0aa72f","d9d441d7172404db6845a886d549ed5c9b2d22d9e26b4d8741b4056ba043f7d5","b9e5353dded51be418617db44385ea92a0615e075061bcfa5d408236e7de0297","4f90ff46bc4139765ddabbebb96b8f31e9a634b12008af67f71f4858abfc33b3"],"20000000","17038c12","65e75abd",false]}
I (18888) create_jobs_task: New Work Dequeued 72d313

### xXAsystolieXx on 2024-03-05

@WantClue 


### xXAsystolieXx on 2024-03-05

![Bildschirmfoto vom 2024-03-05 18-57-13](https://github.com/skot/ESP-Miner/assets/161015184/dcd0c3fe-df4d-44b8-b001-a701507de255)


### xXAsystolieXx on 2024-03-05

![Bildschirmfoto vom 2024-03-05 19-09-51](https://github.com/skot/ESP-Miner/assets/161015184/abf93c06-8c3b-4714-a479-80e05f103ac3)
![Bildschirmfoto vom 2024-03-05 19-09-58](https://github.com/skot/ESP-Miner/assets/161015184/fa3d93e1-9b77-4b3b-a0f0-b187b2f9d16b)
![Bildschirmfoto vom 2024-03-05 19-10-57](https://github.com/skot/ESP-Miner/assets/161015184/f35c40f0-a00f-4523-86ab-df12ed5c8fa5)


### pinokio240 on 2024-03-05

Still, my chip died along the way :(. There are still problems with the power supply, I’ll try tomorrow. I don’t have time today

### xXAsystolieXx on 2024-03-05

@WantClue Can it be related to the fact that my esptool is still on 4.6.2? I saw that version 4.7.0 already exists. Unfortunately the new version does not want to install😅

### xXAsystolieXx on 2024-03-06

ESPTOOL 4.7.0 is now installed but also with it I get the BITAXE firmware 2.0.7 and the new 2.1.0 not on the BM1397. Playing back to version 2.0.6 is still possible and the Bitaxe begins to mine.

### Peichan83 on 2024-03-06

Bonjour, un peu hors sujet mais...

Suite à une panne de wifi de mon opérateur et pendant une mise à jour du esp-miner.bin, mon bitaxe ne s'allume plus.

Il est détecté par mon réseau wifi, mais dès que je le sélectionne, cela me mets en échec de connexion.

Le Ventilateur tourne est après un passage à la loupe aucun composant ne semble cramé.

Comment puis-je faire un hard reset ou comment puis-je le reconfigurer svp.

Merci d'avance.

### xXAsystolieXx on 2024-03-08

> Bonjour, un peu hors sujet mais...
> 
> Suite à une panne de wifi de mon opérateur et pendant une mise à jour du esp-miner.bin, mon bitaxe ne s'allume plus.
> 
> Il est détecté par mon réseau wifi, mais dès que je le sélectionne, cela me mets en échec de connexion.
> 
> Le Ventilateur tourne est après un passage à la loupe aucun composant ne semble cramé.
> 
> Comment puis-je faire un hard reset ou comment puis-je le reconfigurer svp.
> 
> Merci d'avance.

Configure you have to do it on your computer. Visual Studio Code and install Bitaxetool on it

### WantClue on 2024-03-08

> @WantClue Can it be related to the fact that my esptool is still on 4.6.2? I saw that version 4.7.0 already exists. Unfortunately the new version does not want to install😅

This should not be an issue.
It appears to me either two options.
1. it might be that you have solder issues with your asic chip
2. there must be a major bug we don't know of.

I think you already tried the web flasher so therefore I think it must be related to the asic chip itself. 
Instead of esp idf 4.7 upgrade to 5.x and report back.
4.7 should be deprecated and could also cause issues 

### xXAsystolieXx on 2024-03-09

> > @WantClue Can it be related to the fact that my esptool is still on 4.6.2? I saw that version 4.7.0 already exists. Unfortunately the new version does not want to install😅
> 
> This should not be an issue. It appears to me either two options.
> 
> 1. it might be that you have solder issues with your asic chip
> 2. there must be a major bug we don't know of.
> 
> I think you already tried the web flasher so therefore I think it must be related to the asic chip itself. Instead of esp idf 4.7 upgrade to 5.x and report back. 4.7 should be deprecated and could also cause issues

No, it still doesn't work. I exclude a soldering problem because my Bitaxe with version 2.0.0-2.0.6 works wonderfully. 

### xXAsystolieXx on 2024-03-09

It would also be nice to hear if there are people where the BM1397 runs with version 2.0.7 and 2.1.0. With information from board or whether you did anything else with the update 

### xXAsystolieXx on 2024-03-10

![Screenshot_20240310-231635~2](https://github.com/skot/ESP-Miner/assets/161015184/b0d36a0b-5621-4b1e-b79a-aa7b68d08616)

I noticed when examining the logo that an ID was assigned here as shown in the picture and my worker ID with BTC address. With the logs of 2.0.7 and 2.1.0 I have neither an ID nor is my worker ID and BTC address entered.I therefore think that the problem is with the versions, which is why I had no hashrate rate. 


### xXAsystolieXx on 2024-03-10

The only question now is why😅 

### benjamin-wilson on 2024-03-15

Fixed in v2.1.1

### xXAsystolieXx on 2024-03-15

Yes it works💪🏻

### ymongo on 2024-07-24

I there, running a BM1397 on 2.16 too that seems not working: 

```₿ (7819238) create_jobs_task: New Work Dequeued a17bd7
₿ (7862368) bm1397Module: return null
₿ (7879228) stratum_task: rx: {"id":null,"method":"mining.notify","params":["a181af","fca879b347a9fae7441272dd4726ec71793e1a6900006e100000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703cf060d5075626c69632d506f6f6c","ffffffff02cb13201300000000160014c7468ba251bf7a2ea8c7c9d063245c510ddd840f0000000000000000266a24aa21a9edea7f6b955b2a0ad702ecca7c03c67d81a6fe80ceafa393a929b5af68a51e012200000000",["3c19d2dd939bd18a714e37803c72b6fad38511ec0a287b8e59a7d4f58934b044","235057eda61ffe41604e05d0a51bf792ed4749817c377c108eae74dfe2fe0ecf","85139231133d9e91a72bcf2dce7c39f921617262d5ef2077d766216ba73cf4f6","a4038d8f9b57e056f1c0cdd586dec3a1daa466356f809e1808c7fc95aa354452","0157a2ebadf348c7855a32e6be0dd741b20ba580a149089cca99451da68a170d","62a2edfaaaadadeb2a635069615678893c44e12f36885f94d156464e7a27ed55","36be25c83b3e77c544ab61a3e38165de780074a39264268ec515a6dfd040c2d6","609661924bb8494f3700c633cc90d72e6f748352b6ae9054c32dffe69f75fc58","272c3d309e4f5d716c78647ad5cec1543b103c5632553e42393a15bebfcf65e7","9824e3f7019a87c1d0c1d17136e161d7c38e1f5dc39d2d72668d8fe153b76336","3517b1ba3d734356c8ee99a2459cb925a0d765c87b49e65cc2261a0aa5c82cce","61a22c3d98c58cd97dc261ab174244284c142c8f33ab01bf22c38de5d081b6cf"],"20000000","17036e3a","66a0f2dd",false]}
```

I'll try downgrade to 2.1.1 to see

### ymongo on 2024-07-24

BM1397 on 2.1.1: shares are increasing but hashrate stays at 0? I'll wait a few hours to see how it's going

### ymongo on 2024-07-25

Seems like it's leavind dead... anyone can tell me something about these logs? https://pastebin.com/QZYD2BiG
And app settings say this, CPU 70 C, is it cooking? cooked?


![image](https://github.com/user-attachments/assets/89f8f336-4912-4003-b553-4801fe4113d7)





























































































### xXAsystolieXx on 2024-07-26

@ymongo  78 degrees is really too hot. Maybe change the thermal paste and then try again. 



### MyOwn2C on 2024-07-26

> Seems like it's leavind dead... anyone can tell me something about these logs? https://pastebin.com/QZYD2BiG And app settings say this, CPU 70 C, is it cooking? cooked?
> 
> ![image](https://private-user-images.githubusercontent.com/28120333/351993413-89f8f336-4912-4003-b553-4801fe4113d7.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjIwMTM2MjgsIm5iZiI6MTcyMjAxMzMyOCwicGF0aCI6Ii8yODEyMDMzMy8zNTE5OTM0MTMtODlmOGYzMzYtNDkxMi00MDAzLWI1NTMtNDgwMWZlNDExM2Q3LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MjYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzI2VDE3MDIwOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTJhNGRjNTUwZDg4YmVlYzgyMzk0Mjc2MGIzYmY1MDFjOWE5MGY1OTc5MmExYWU3OWRhOWZlYWEyYTU5ODU3MmQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.BP3Z0MwmmIEAbQ1OshZHgEHsWc9lxqSsMHs9JBHTSqc)

You need a lot better cooling and power supply before it can hash properly. 

### ymongo on 2024-07-29

Thanks for all your replies! I've got a Noctua fan, now I need the thermal paste, I'll tell you how it goes later 

### ymongo on 2024-08-25

Thermal paste replaced, Noctua 40x40 fan updated, BM1397now hashing at the tremenduous rate of 65 Gh/s
Any tips on ideal configuration? (freq 425 and voltage 1200 currently)

![image](https://github.com/user-attachments/assets/c8725d0c-8d4d-491c-868d-fe03682686da)

### ymongo on 2024-08-25

(sorry for spamming old issue, ill look for the discord)

### xXAsystolieXx on 2024-08-25

> Thermal paste replaced, Noctua 40x40 fan updated, BM1397now hashing at the tremenduous rate of 65 Gh/s Any tips on ideal configuration? (freq 425 and voltage 1200 currently)
> 
> I have my bitaxe on 475 and 1400. But why your temperature is so high will probably be a soldering error 

### xXAsystolieXx on 2024-08-25

Which heat sink do you have on it? I installed a bigger one. 

Aabcooling NB Cooler 1 - heat sink on aluminum for Northbridge cooling, mini passive cooler, heatsink, cooler, aluminum VGA cooler, mounting for the 40mm fanhttps://amzn.eu/d/cBBe3Mm 

I installed it together with the Noctua Fan and came to 60-65 degrees                                                                                                                                                                               

### ymongo on 2024-08-26

> https://amzn.eu/d/cBBe3Mm

I have the default heatsink but I just found this one today!!! I'm gonna buy it and see, right now 've rolled back to 2.1.1 and temp has dramatically falled to 60 degrees, at freq  485 and core voltage 1.2  (still lagging below 100GH/s though)

### xXAsystolieXx on 2024-08-26

That's a step forward :) do 485 at 1400 maybe that's better
