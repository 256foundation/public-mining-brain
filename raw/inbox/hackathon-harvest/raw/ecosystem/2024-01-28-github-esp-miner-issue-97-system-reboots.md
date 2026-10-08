# bitaxeorg/ESP-Miner issue #97: System reboots

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/97
> Collected: 2026-10-07
> Published: 2024-01-28

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 97
- State: closed
- Author: Sledge0001
- Opened: 2024-01-28
- Closed: 2024-02-07
- Labels: none

## Description

System reboots unexpectedly between 4-10 hours using stock settings on firmware v2.0.7 

Issue does not occur on firmware 2.0 4.

## Comments

### n0rthranger on 2024-01-29

I do have the same issue. But it reboots after 23 hours. Link for context https://damus.io/note1wkgnm62hy55n68h5ccypxajce4z9jvppt3ew4cpj6tcp64s8ffrqsvd5ml

### skot on 2024-01-29

> System reboots unexpectedly between 4-10 hours using stock settings on firmware v2.0.7 
> 
> 
> 
> Issue does not occur on firmware 2.0 4.

Is this with Ocean pool also?

### Sledge0001 on 2024-01-29

CK's pool.

### qubyt3 on 2024-01-29

> CK's pool.

Odd I've let one of my Bitaxe 1366 with firmware v.2.0.7 run on CK pool for the last 3 days straight no problem. 

Were you able to capture the log when your device reboots? 

### Sledge0001 on 2024-01-29

Unfortunately I did not. But it seems to happen only on 2.0.7 it's very stable going back to 2.0.4

### n0rthranger on 2024-01-30

Also just switched from ocean to the https://solo.ckpool.org and it's like restarting every 15 minutes none stop. I tried to re flash the latest firmware again but same issue 

### n0rthranger on 2024-01-31

> Also just switched from ocean to the https://solo.ckpool.org and it's like restarting every 15 minutes none stop. I tried to re flash the latest firmware again but same issue 

Update. 14 hours it's running none stop but I already have a first signs that restart is coming. I can't access dashboard via IP. I bought Bitaxe 204 from open source miner com. Attached photo of the board. Maybe will be helpful. ![image](https://github.com/skot/ESP-Miner/assets/62068896/0c36ee14-b3a0-4e72-8771-521cc4c7ef22)

### benjamin-wilson on 2024-01-31

Are you leaving the dashboard open on a computer?

Can you screenshot the whole AxeOS home page please. 
If you can capture the crash in the logs that would also be helpful 

### n0rthranger on 2024-01-31

No I don't leave it open. And can't access it right now: says that "Safari can't open the page because the network connection was lost" tried to turn on/off wifi on my phone and laptop same issue. 

### skot on 2024-01-31

this sounds like a networking issue maybe? Can you connect to your router and confirm the bitaxe has an IP on your network?

### benjamin-wilson on 2024-01-31

How far away is the bitaxe from your wireless access point?

### n0rthranger on 2024-01-31

Connected devices from router page. espressif is Bitaxe 
All good on my end ![image](https://github.com/skot/ESP-Miner/assets/62068896/4b7b2d37-2e2e-4534-a8d0-614109c23e8b)

### skot on 2024-01-31

and when you connect to it's IP in your browser, you get the error? I wonder if the bitaxe is restarting.

Can you connect the Bitaxe's USB port to your Mac and use a serial terminal program like CoolTerm to get the logs? use 115200 baud.

### Sledge0001 on 2024-01-31

So here's something interesting the 2 xBitAxe's I have from Opensourceminer.com are on 2.0.7 and are stable. The 1 got from altairtech has the issues with 2.0.7

### benjamin-wilson on 2024-01-31

> So here's something interesting the 2 xBitAxe's I have from Opensourceminer.com are on 2.0.7 and are stable. The 1 got from altairtech has the issues with 2.0.7

Well I made all of them ;) Can you screenshot the AxeOS dashboard on the one with issues?

### Sledge0001 on 2024-01-31

![20240131_112150](https://github.com/skot/ESP-Miner/assets/125903519/69e28557-6717-4ec2-9184-3d54cbf9f7bc)
![20240131_112218](https://github.com/skot/ESP-Miner/assets/125903519/64ae82b8-f15e-4e30-9c61-47f39593a5e5)


Here's the one that's acting odd on 2.0.7 :)

### benjamin-wilson on 2024-01-31

How did you update to 207? Please screenshot AxeOS

### Sledge0001 on 2024-01-31


![17067295812422223052997492265710](https://github.com/skot/ESP-Miner/assets/125903519/7df05fef-c48b-459f-884d-79251a6e61fe)
![17067295415858403048997014709002](https://github.com/skot/ESP-Miner/assets/125903519/05a270d8-90c3-4af1-8255-9438afe08aaf)

Firmware was updated via the AxeOS ui


### Sledge0001 on 2024-01-31

I'll try the firmware update again and see if I experience the issue again.

### benjamin-wilson on 2024-01-31

Ok, please screenshot the overview section again when it's updated

### Sledge0001 on 2024-01-31


![17067304057481232468430978432454](https://github.com/skot/ESP-Miner/assets/125903519/3ec65a5a-65dd-4c60-b606-346ac5369223)


### n0rthranger on 2024-01-31

I was late. It restarted again while I was figuring out how to use minicom. But seems like I found the error in log ![image](https://github.com/skot/ESP-Miner/assets/62068896/d9493ebb-62f9-4cb9-a2cc-391a48b3b390)

### Sledge0001 on 2024-01-31

![17067308225428597156168692981611](https://github.com/skot/ESP-Miner/assets/125903519/e1c3d9af-28a2-4d0d-8b77-75f542ff69c2)
And it just crashed. 

It states low voltage on the power side for just a few seconds during  the  reboot.

![20240131_115603](https://github.com/skot/ESP-Miner/assets/125903519/6cc0c867-a1d7-4257-ba31-0ea9de1bdf48)



### n0rthranger on 2024-01-31

> I was late. It restarted again while I was figuring out how to use minicom. But seems like I found the error in log ![image](https://github.com/skot/ESP-Miner/assets/62068896/d9493ebb-62f9-4cb9-a2cc-391a48b3b390)

![image](https://github.com/skot/ESP-Miner/assets/62068896/1b222426-928b-4606-9ed0-ea4e0331f6b0)

### benjamin-wilson on 2024-01-31

What is being used for power supplies? 

### benjamin-wilson on 2024-01-31

Oh @Sledge0001 change your vcore to 1200, this is the default. It looks like it changed in the update?

### Sledge0001 on 2024-01-31

> Oh @Sledge0001 change your vcore to 1200, this is the default. It looks like it changed in the update?

That's where it's set as per the ui.
![17067346664112091804107494252842](https://github.com/skot/ESP-Miner/assets/125903519/675d9b9f-5fec-4ef7-89e1-c7385e296667)


I've reset it lower, saved and rebooted. Then set it back to default saved and rebooted let's see what this does.

### monster4866 on 2024-02-01

u need a better power supply, i have 8 bitaxe, all came with a chep power supply, u need above +5000mv, good 5100-5300mv

https://github.com/skot/bitaxe/issues/118#issuecomment-1904615683

### n0rthranger on 2024-02-02

I heard that I can burn it if more powerful power supply  

### monster4866 on 2024-02-02

> I heard that I can burn it if more powerful power supply

thats why mr volta invented volt ;)

u should plug only a 5v supply in it

### Sledge0001 on 2024-02-02

Over 24 hours online with no rebooting!

### n0rthranger on 2024-02-03

24 hours another one reboot! Ordering this one power supply in hope that gonna fix the issue! https://a.co/d/5srOIj4

I received this one with Bitaxe: https://opensourceminer.com/products/5v-5a-power-supply

### n0rthranger on 2024-02-03

> 24 hours another one reboot! Ordering this one power supply in hope that gonna fix the issue! https://a.co/d/5srOIj4
> 
> I received this one with Bitaxe: https://opensourceminer.com/products/5v-5a-power-supply

I know Benjamin check this thread as well since he was active on here. Your website where I bought the Bitaxe can't be reached! In my email I simply asked to ship back the Bitaxe I bought from you to test it and here what is your website responding to me. ![image](https://github.com/skot/ESP-Miner/assets/62068896/af74ba26-557a-427e-89b8-59e20ddad502)

### benjamin-wilson on 2024-02-03

> > 24 hours another one reboot! Ordering this one power supply in hope that gonna fix the issue! https://a.co/d/5srOIj4
> > I received this one with Bitaxe: https://opensourceminer.com/products/5v-5a-power-supply
> 
> I know Benjamin check this thread as well since he was active on here. Your website where I bought the Bitaxe can't be reached! In my email I simply asked to ship back the Bitaxe I bought from you to test it and here what is your website responding to me. ![image](https://private-user-images.githubusercontent.com/62068896/302011957-af74ba26-557a-427e-89b8-59e20ddad502.jpeg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDY5MzQ0NzAsIm5iZiI6MTcwNjkzNDE3MCwicGF0aCI6Ii82MjA2ODg5Ni8zMDIwMTE5NTctYWY3NGJhMjYtNTU3YS00MjdlLTg5YjgtNTllMjBkZGFkNTAyLmpwZWc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIwM1QwNDIyNTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wZjEzYTM3MDhhNjcxYTdiOGE1Njc4NWQzMDYwMzA3YmNiMDYzMTZlZGZjNDJhODk5ZDY2YzA5MmYxOGVmMTQzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.F0hyxbpj-oi16p_8Ct72V3Fm7llHnoNpo6gqZprpb6A)

You can email me directly: admin@opensourceminer.com if you want to discuss any issues with your order.

### n0rthranger on 2024-02-05

Was able to cut the log file during restart. Here is log file.
[bitaxe log restarts.txt](https://github.com/skot/ESP-Miner/files/14159978/bitaxe.log.restarts.txt)


### n0rthranger on 2024-02-05

> Was able to cut the log file during restart. Here is log file.
> 
> [bitaxe log restarts.txt](https://github.com/skot/ESP-Miner/files/14159978/bitaxe.log.restarts.txt)
> 
> 

After another 17 hours it has restarted. According to the Ben I have wifi network connection issues. I doubt that this is the case. I did a restart of the modem, talked with the Comcast and everything is healthy. At some point the best difficulty stops going up and it restarts.    

### benjamin-wilson on 2024-02-05

I am also investigating a possible memory leak that might be causing this issue.

### n0rthranger on 2024-02-06

> > Was able to cut the log file during restart. Here is log file.
> > 
> > [bitaxe log restarts.txt](https://github.com/skot/ESP-Miner/files/14159978/bitaxe.log.restarts.txt)
> > 
> > 
> 
> After another 17 hours it has restarted. According to the Ben I have wifi network connection issues. I doubt that this is the case. I did a restart of the modem, talked with the Comcast and everything is healthy. At some point the best difficulty stops going up and it restarts.    

UPDATE! I have tried 2.0.7 and 2.0.6 versions of firmware and device is restarting within ~24 hours. 
After Ben's suggestion to roll back to 2.0.4 device isn't crashing and hashing over 24 hours now. 
The only conclusion what I can make now is that it's not my wifi network connection issue. Might be something with firmware and I am not only the one have this issue. ![image](https://github.com/skot/ESP-Miner/assets/62068896/3a940ea9-c693-43a4-8e88-33239cd1eb79)![image](https://github.com/skot/ESP-Miner/assets/62068896/3f26b373-0bf4-4a79-8ab1-579a840ed788)![image](https://github.com/skot/ESP-Miner/assets/62068896/ee1c0a8f-4e0c-41e2-81a6-269a951dd556)![image](https://github.com/skot/ESP-Miner/assets/62068896/27133add-ec21-416b-bf47-689bf0c6f0fc)![image](https://github.com/skot/ESP-Miner/assets/62068896/e7144581-9ff2-42e4-99c1-b610e6d46128)![image](https://github.com/skot/ESP-Miner/assets/62068896/d666a5f8-1842-4dbd-9522-dde4fed82f17)![image](https://github.com/skot/ESP-Miner/assets/62068896/b67e0886-3653-481b-b109-85d89a716149)![image](https://github.com/skot/ESP-Miner/assets/62068896/00c807d9-c943-4e04-90fb-7aabcc45480c)

### benjamin-wilson on 2024-02-06

![PXL_20240206_180034572](https://github.com/skot/ESP-Miner/assets/1399163/3123cfa3-e3ae-4058-ba6a-c0eed01c150d)
![PXL_20240206_180059840](https://github.com/skot/ESP-Miner/assets/1399163/b33d9a45-f112-4407-813b-cbb2e7ccc51c)
![PXL_20240206_180109486](https://github.com/skot/ESP-Miner/assets/1399163/bc0f3afa-ec85-4478-8e52-5aada42585ca)

2.0.7 Going strong, no memory leaks. 

### n0rthranger on 2024-02-06

Is this 204 board you have ? Wait few more hours 🤷‍♂️
Is it ok if I will just be running it on the old firmware? 
P.S. This guy got his Bitaxe from Dcentral few days ago and also had his device restarted on the latest firmware. 

https://damus.io/note15n2ymj3ym6lqjylrvpa5u25fjzkl4s2ru7e48f4j2p7qnkkxxj2q7dkmmc

### qubyt3 on 2024-02-06

I removed what I said based on @benjamin-wilson comment.

### n0rthranger on 2024-02-07

> @yeg0rpetrov I can't help but notice on your home screen the board version is missing... 
> 
> 
> 
> I'm wondering if with all your troubleshooting something went missing... 
> 
> 
> 
> Possibly flashing your device with some basic manufacturing data to the NVS partition with the correct firmware and a proper config.cvs file might solve your issue. 
> 
> 
> 
> 1. Download Skot ESB-Miner repo from Git to your downloads and unzip it. ./Downloads/ESP-Miner-207
> 
> 2. Download the esp-miner-factory-204-v2.0.7.bin and place in the ESP-Miner folder ./Downloads/ESP-Miner-207/
> 
> 3. Open VS Code, Copy and Paste config.cvs.example and rename the copied file to: config.cvs
> 
> 4. Open config.cvs file and edit the following fields: 
> 
> 
> 
> key,type,encoding,value
> 
> main,namespace,,
> 
> wifissid,data,string,**myssid**
> 
> wifipass,data,string,**mypass** 
> 
> stratumurl,data,string,**solo.ckpool.org**
> 
> stratumport,data,u16,**3333**
> 
> stratumuser,data,string,**mywallet ID+workername**
> 
> stratumpass,data,string,**x**
> 
> asicfrequency,data,u16,**485**
> 
> asicvoltage,data,u16,**1200**
> 
> asicmodel,data,string,**BM1366**
> 
> devicemodel,data,string,**ultra**
> 
> boardversion,data,string,**v2.0.4**
> 
> flipscreen,data,u16,1
> 
> invertfanpol,data,u16,1
> 
> autofanspeed,data,u16,1
> 
> fanspeed,data,u16,100
> 
> --> HIT CTRL-S and SAVE
> 
> 
> 
> 5. Connect your bitaxe
> 
> 6. Select the correct port it connected to (bottom left), select the workspace folder you're working from when prompt 
> 
> 
> 
> 7. Open a terminal and type: bitaxetool --port /dev/cu.usbmodem1101 (or wtv port your Bitaxe is connected to) --config ./config.cvs --firmware ./esp-miner-factory-204-v2.0.7.bin 
> 
> note: Bitaxetool need python version 3.11.7 or earlier, it will not work with the latest python v3.12
> 
> 
> 
> Your bitaxe will flash, reboot and start hashing again. Report back your finding. Take a particular attention the Heap memory: is it steadily going down, or hovering +- a couple 1000 bytes. 
> 
> 
> 
> I think WantClue has good tutorial on hes Youtube channel on how to do this, Bitaxe V2 a new update.
> 
> 
> 
> Hope this help, let us know if you have any questions. :) 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 

The board version probably missing cause I downgraded firmware to the 2.0.4 🤔 Seems like a hell of steps 😄Thank you, will try to do re flash in that way.

### benjamin-wilson on 2024-02-07

> > @yeg0rpetrov I can't help but notice on your home screen the board version is missing...
> > I'm wondering if with all your troubleshooting something went missing...
> > Possibly flashing your device with some basic manufacturing data to the NVS partition with the correct firmware and a proper config.cvs file might solve your issue.
> > 
> > 1. Download Skot ESB-Miner repo from Git to your downloads and unzip it. ./Downloads/ESP-Miner-207
> > 2. Download the esp-miner-factory-204-v2.0.7.bin and place in the ESP-Miner folder ./Downloads/ESP-Miner-207/
> > 3. Open VS Code, Copy and Paste config.cvs.example and rename the copied file to: config.cvs
> > 4. Open config.cvs file and edit the following fields:
> > 
> > key,type,encoding,value
> > main,namespace,,
> > wifissid,data,string,**myssid**
> > wifipass,data,string,**mypass**
> > stratumurl,data,string,**solo.ckpool.org**
> > stratumport,data,u16,**3333**
> > stratumuser,data,string,**mywallet ID+workername**
> > stratumpass,data,string,**x**
> > asicfrequency,data,u16,**485**
> > asicvoltage,data,u16,**1200**
> > asicmodel,data,string,**BM1366**
> > devicemodel,data,string,**ultra**
> > boardversion,data,string,**v2.0.4**
> > flipscreen,data,u16,1
> > invertfanpol,data,u16,1
> > autofanspeed,data,u16,1
> > fanspeed,data,u16,100
> > --> HIT CTRL-S and SAVE
> > 
> > 5. Connect your bitaxe
> > 6. Select the correct port it connected to (bottom left), select the workspace folder you're working from when prompt
> > 7. Open a terminal and type: bitaxetool --port /dev/cu.usbmodem1101 (or wtv port your Bitaxe is connected to) --config ./config.cvs --firmware ./esp-miner-factory-204-v2.0.7.bin
> > 
> > note: Bitaxetool need python version 3.11.7 or earlier, it will not work with the latest python v3.12
> > Your bitaxe will flash, reboot and start hashing again. Report back your finding. Take a particular attention the Heap memory: is it steadily going down, or hovering +- a couple 1000 bytes.
> > I think WantClue has good tutorial on hes Youtube channel on how to do this, Bitaxe V2 a new update.
> > Hope this help, let us know if you have any questions. :)
> 
> The board version probably missing cause I downgraded firmware to the 2.0.4 🤔 Seems like a hell of steps 😄Thank you, will try to do re flash in that way.

Please don't do that, it's incorrect 

### n0rthranger on 2024-02-07

Damn! 1 day and 8 hours it restarted again on 2.0.4 
I give up ![image](https://github.com/skot/ESP-Miner/assets/62068896/daddbb7b-89c0-4813-b9aa-ac69729ced2c)

### benjamin-wilson on 2024-02-07

Okay it seems conclusive now. This is a network/wireless radio issue. I'm closing the issue.
