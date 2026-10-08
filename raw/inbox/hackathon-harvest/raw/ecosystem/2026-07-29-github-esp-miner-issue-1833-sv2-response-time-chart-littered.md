# bitaxeorg/ESP-Miner issue #1833: SV2 response time chart littered with batch timing

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1833
> Collected: 2026-10-07
> Published: 2026-07-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1833
- State: open
- Author: martint379
- Opened: 2026-07-29
- Closed: n/a
- Labels: none

## Description



**Describe the bug**
Using v2.14.2 on Bitaxe 601.  SV2 response time chart is not constantly showing submit round trip time. It seems to be littered with batch timing.

When Response time is selected for SV2 extended it appears to work correctly until a specific condition is hit:  
accepted.count = 1 which usually occurs just prior to a new job.  In this case the response time can be anywhere from ~20ms to ~16000+ms.  I believe I am looking at 2 different timings. The short one is the recent batch submit ack time.  The long one I guess is from when the initial share was found until the submit ack time.  I do realize this 
is mostly cosmetic but helpful to monitor system & network performance. 

Perhaps there should be 2 different selectable response times: 1) submit response time, 2) batch creation + submit response time.  I hope you find this helpful. This was my first ever bug report.  Also, thank you for all your hard work.

**To Reproduce**
Steps to reproduce the behavior:
1. Connect miner to mining support host using SV2 extended 
2. On the chart select response time
3. Wait and monitor the chart. You should see the occasional significant spikes up that’s crushes the resolution of the round trip response time.

**Expected behavior**
Chart consistently showing round trip response time without batch timing.

**Screenshots & Photos**
Screen shoot attached below.

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601    BM1370
 - Bitaxe HW vendor: ?
 - ESP-Miner FW version: v5.5.3
 - Hash Frequency: 1040
 - Voltage: 1320
 - Pool URL, Port, User:  sv2solo.ckpool.org, 3336, …

<img width="2048" height="1536" alt="Image" src="https://github.com/user-attachments/assets/5b9d8db5-e75c-41d9-b8b6-dafb1608f74d" />

**Additional context**
Add any other context about the problem here.
