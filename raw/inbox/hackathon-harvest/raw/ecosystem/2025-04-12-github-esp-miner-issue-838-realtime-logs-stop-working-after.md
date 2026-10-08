# bitaxeorg/ESP-Miner issue #838: Realtime Logs stop working after a short period of time

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/838
> Collected: 2026-10-07
> Published: 2025-04-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 838
- State: closed
- Author: d4r1as
- Opened: 2025-04-12
- Closed: 2025-04-13
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
Realtime Logs stop working after a short period of time (stuck - no updates from websocket)

**To Reproduce**
Steps to reproduce the behavior:
1. Go to 'Logs'
2. Click on 'Show Logs'
3. Observe logs for 30 seconds - 1 minute
4. After a while, logs are not updated - you need to 'Hide Logs' and 'Show Logs' to see the latest logs. After a while, same thing happens.

**Expected behavior**
I should be able to see the Real Time logs - without having to refresh or click on 'Hide Logs' and 'Show Logs'

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: GoBrrr
 - ESP-Miner FW version: 2.6.3
 - Hash Frequency: 695
 - Voltage: 1150
 - Pool URL, Port, User: Local

**Additional context**
N/A


## Comments

### ghost on 2025-04-13

I can not reproduce this, the only difference here is I'm not mining to my own node as I don't run one.

### d4r1as on 2025-04-13

> I can not reproduce this, the only difference here is I'm not mining to my own node.

Hmm, I hadn’t considered testing that scenario. I’ll try mining with public pool shortly to see if the issue is related to the pool.

### d4r1as on 2025-04-13

> > I can not reproduce this, the only difference here is I'm not mining to my own node.
> 
> Hmm, I hadn’t considered testing that scenario. I’ll try mining with public pool shortly to see if the issue is related to the pool.


Tested with public-pool, same issue.

TBH, I don't see how the pool can influence the real time logs (_i did not check the code yet ..._)


### ghost on 2025-04-13

I'm not able to reproduce the issue here, tested on 401 and 601. 

601 with your settings btw except for where it's mining. 


### d4r1as on 2025-04-13

> I'm not able to reproduce the issue here, tested on 401 and 601. 
> 
> 601 with your settings btw except for where it's mining. 
> 

Thanks for confirming. I will flash an older version to see if the issue persists.

### ghost on 2025-04-13

Do an external log capture in VS Code via the USB cable at the same time as within AxeOS to see if you can catch the issue there as well. 

### ghost on 2025-04-13

@d4r1as 

Just to note, I'm using Chrome browser here when accessing the device for AxeOS to view / watch the logs, left the windows for both open overnight, logs was still scrolling on both in AxeOS. 

### d4r1as on 2025-04-13

> Do an external log capture in VS Code via the USB cable at the same time as within AxeOS to see if you can catch the issue there as well.

@STSMiner1 

Here is the result. Clearly something is wrong with the UI. Log capturing via VSCode works as expected. I will check the UI, maybe something is wrong with the `websocket` connection

https://github.com/user-attachments/assets/61f07738-d5e4-441d-8a19-9dfed5c94643

### ghost on 2025-04-13

Yeah, something is wrong there, the logs in AxeOS should not stall / stop, not able to reproduce that here on my device with 2.6.3 or dev-latest. 

### d4r1as on 2025-04-13

> > Do an external log capture in VS Code via the USB cable at the same time as within AxeOS to see if you can catch the issue there as well.
> 
> [@STSMiner1](https://github.com/STSMiner1)
> 
> Here is the result. Clearly something is wrong with the UI. Log capturing via VSCode works as expected. I will check the UI, maybe something is wrong with the `websocket` connection
> 
>  1.mov

If you look at the video below - it appears that the `websocket` connection dies - you can clearly see the `I (1112397) http_server: Handshake done, the new connection was opened` message popping up - at the same exact time when the Real Time logs stop working in the UI.

https://github.com/user-attachments/assets/c5625df0-a51c-4ae0-b6f9-f839c238cf9f

### ghost on 2025-04-13

Rolled back to 2.6.3 to retest, 11 mins in, not seeing this issue or with dev-latest.

![Image](https://github.com/user-attachments/assets/10e9ef57-2263-46d8-868d-47559abce663)

Update
25 mins in, still working.

### ghost on 2025-04-13

`dev-latest` built locally. 

![Image](https://github.com/user-attachments/assets/d79303a3-77ce-4fd9-913d-26a18de3a07c)

### d4r1as on 2025-04-13

@STSMiner1 

I found the problem.

I have a network script which connects via `ws` to all my bitaxes and parses the logs and stores some data in InfluxDB. Once I stopped that script - everything works.

Any idea why this problem happens when there are 2 `ws` connections?

### ghost on 2025-04-13

Hmm, not sure.

Your ESP-IDF - did you modify it ?  (-dirty) 

If not, might want to recheck that, using the release version here.

### d4r1as on 2025-04-13

> Hmm, not sure.
> 
> Your ESP-IDF - did you modify it ?  (-dirty) 
> 
> If not, might want to recheck that, using the release version here.

No, didn't modify it, just build and deployed.

Anyway, do you know if anyone is working on adding support for InfluxDB? Otherwise, I will start implementing it ...

### ghost on 2025-04-13

ESP-IDF version

![Image](https://github.com/user-attachments/assets/6af60291-1e42-48f4-b07e-986bfe28fda9)

This is all I've seen on that topic (InfluxDB).
https://github.com/bitaxeorg/ESP-Miner/issues/614



### d4r1as on 2025-04-13

> ESP-IDF version
> 
> ![Image](https://github.com/user-attachments/assets/6af60291-1e42-48f4-b07e-986bfe28fda9)
> 
> This is all I've seen on that topic (InfluxDB).
> https://github.com/bitaxeorg/ESP-Miner/issues/614
> 
> 

Thanks. I will give it a try then.

Regarding the ESP-IDF version, I don't know why is dirty, didn't changed anything.

Thank you!
