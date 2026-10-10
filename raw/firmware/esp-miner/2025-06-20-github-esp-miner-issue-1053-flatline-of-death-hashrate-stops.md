# bitaxeorg/ESP-Miner issue #1053: "Flatline of Death" - hashrate stops changing, no new shares are found. Pool is still alive and sending work

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1053
> Collected: 2026-10-07
> Published: 2025-06-20

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1053
- State: open
- Author: homecryptominer
- Opened: 2025-06-20
- Closed: n/a
- Labels: bug, accepted, hashing, critical

## Description

Sometimes Bitaxes will crash and not show any initials signs of it. The hashrate still shows it's hashing, but does not change and no new shares are found. On the AxeOS graph, this shows as a flatline (hence people calling it the Flatline of Death).  

Sometimes it can crash in minutes, sometimes hours and occasionally days for this to occur. A restart will typically fix it.

It would be good if the firmware could detect this crash and recover from it automatically.

Thank you again amazing team!
Steve :-)

## Comments

### mutatrum on 2025-06-20

This should be covered in #272 

### skot on 2025-06-20

Any idea what's happening here? @homecryptominer what hardware do you have?

### homecryptominer on 2025-06-22

I have no idea why it just stops hashing. There are not telltale signs as to why, but the graph looks like this:

![Image](https://github.com/user-attachments/assets/8d1d40af-e0ce-4d1b-a28b-3edeb9795cd7)

Clicking the RESTART button on AxeOS will often resolve it. 

### skot on 2025-06-22

What hardware version is this?

### komeana on 2025-06-22

Flatline of Death is also seen in Bitaxe Gamma 601.

### komeana on 2025-06-22

This situation occurs within 24 hours.

### skot on 2025-06-23

Is it a GekkoScience Gamma 601?

### komeana on 2025-06-23

Yeap.

### homecryptominer on 2025-06-23

Mine is a Gamma 601. Happens both when OCd, but also when running on default settings too. There are quite a few people on Reddit with same issue. I have tried going back to default PSU, default heatsink & fan, re-applied thermal paste, re-flashed to 2.6.x and also 2.8.x - but the issue persists.

### skot on 2025-06-23

> Mine is a Gamma 601. Happens both when OCd, but also when running on default settings too. There are quite a few people on Reddit with same issue. I have tried going back to default PSU, default heatsink & fan, re-applied thermal paste, re-flashed to 2.6.x and also 2.8.x - but the issue persists.

Is yours a GekkoScience Bitaxe?

### homecryptominer on 2025-06-26

No idea @skot - these units are from AliExpress. 

### Proximity-BBQ on 2025-07-03

One of mine Gamma 601 suffers from the same issue and I have to restart it  every 1-2 days to temporary fix it. Once it stops hashing I see over and over again in the log the following type of messages and nothing else:
₿ (33971084) stratum_api: rx: {"params":["680955b1000849d1","76a8b1abf6115e6d457ebc0fc8369cbd0519b3c0000233580000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff270360ca0d0004471a6668040d345e110c","0a7c70617261736974657cffffffff0300e1f505000000001600149e09fbdb3c9c821171b78631e9dde2e06daf0d00718af10c00000000160014b2329f07e76346be62aeb1d30813028eb460d3960000000000000000266a24aa21a9ed2279bc8aa350ed51fd195daa012ddd9ae6ff1260ef3f8c3e91cf6bcd72cd669c00000000",["f356cb5f930945a6cc7a2adcd87c1e13e438ff63922f9b11547aa756a355ff7a","3fd7e2a9a1d4e88c9654890a242f6e18dffe987ad9849a85a863e4d6bba030f3","9bb5c5f623f2a242a3f22e67d25debb8edcddb14f1b8f3dad5947095d45ba293","946da8fac7c17c273e547ea295ed6905743ff0d0e3d1893857f2156eae9646fd","6cef1b79b8ad7e5c0d05ae83623045cb72c04af4d7aa88e9ab4480125bdb9c1c","8438674a8e94b2e206cb737b89e902720b2e0b6bea4fe61572a01678c2251562","f6af088dfcec6a51f738d7008a224353a549a2d54de16aae0afde4e36c2e38f9","8cbe02ed5510c9247e461c14baaca11956b679571ef71e645aa5d74e6d6c292a","eec3e5f0e2a870cf7158da7e04aaca96b8e0a006fcf7029b18620aeb3866389e","ba03929386a9a6a3e7a6b98cfaa090248e29609fa29d65539d9370e017c39ba5","72fada62f1f4bd41630fbca97dcb970fe5225ae17c69022735537dca33c0aa94","2f5b960bfe689b821db9411ecaf6340efd22149d6f4490f81bb8b104be20a956"],"20000000","17026816","68661a47",false],"id":null,"method":"mining.notify"}
₿ (33971280) create_jobs_task: New Work Dequeued 680955b1000849d1

### skot on 2025-07-03

I still have not been able to reproduce this bug. Is your HW a GekkoScience gamma 601?

### skot on 2025-07-03

From your log snippet it looks like you are getting mining.notify from the pool, so network is good. You just aren't getting nonces from the ASIC... ie it's not hashing.

@Proximity-BBQ @homecryptominer and @komeana next time this happens can you get a screen shot from AxeOS dashboard showing the power values and post here?

### Proximity-BBQ on 2025-07-03

I really don’t know if it’s GekkoScience or not. What I do know is that both Gammas 601 are from the same vendor (both looks identical) but only one suffers from that issue.

### skot on 2025-07-03

> I really don’t know if it’s GekkoScience or not. What I do know is that both Gammas 601 are from the same vendor (both looks identical) but only one suffers from that issue.

GekkoScience HW says GekkoScience on the front. I think usually in the bottom left corner. Sounds like yours prolly isn't one.

When you get a chance if you could get that screenshot we can try and track this issue down further.

### Proximity-BBQ on 2025-07-04

This is how it looks like after less than 24 hours from the last restart. The logs are as reported yesterday.

![Image](https://github.com/user-attachments/assets/cde413c4-b969-455d-9dde-e8b720dcd6e3)
![Image](https://github.com/user-attachments/assets/cf2c0e2c-bab0-4092-8a0a-eda22948014d)

### mutatrum on 2025-07-04

Did you even catch the logs around the moment that it happened? One way to do this is to connect the miner to USB and cat the logs into a file.

### skot on 2025-07-04

> This is how it looks like after less than 24 hours from the last restart. The logs are as reported yesterday.

Thank you! This is perfect. @homecryptominer and @komeana can y'all grab some screenshots like this? 

### skot on 2025-07-04

> Did you even catch the logs around the moment that it happened? One way to do this is to connect the miner to USB and cat the logs into a file.

From the logs posted above it seems like the ASIC has just stopped sending shares. Network is still good. Hard to know if this is an ASIC problem or a problem with the esp-miner task that handles responses.

I really wish I could reproduce this!

### mikaelfrost on 2025-07-04

Hi there, my two units are doing this too. Both are from the "Minerfixes" seller on Aliexp , but should not be the "clones", as the ESP chips are the same as my third unit from solosatoshi (which is working correctly). Seller didn't helped at all. Meanwhile I swapped default cooler with Pi52 Low profile + A6x15, added small heatsinks on the back (cooled with A4x25). Used ARCTIC MX-6 thermal paste. Also using MW LRS200-5V as the PSU for all of them.

Below is my screenshot. Unfortunately I don't have the logs for now. I was running the benchmark script again so I am also attaching the output.

<img width="2290" height="1537" alt="Image" src="https://github.com/user-attachments/assets/dc321e29-998e-4520-95bb-207ebca91975" />

<img width="1168" height="1266" alt="Image" src="https://github.com/user-attachments/assets/21ff22a4-7b55-4310-8dac-13f7d2e2b255" />


Edit: I catched some logs:
[flatline-logs-20250704.txt](https://github.com/user-attachments/files/21074194/flatline-logs-20250704.txt)
[flatline-logs-20250704_2.txt](https://github.com/user-attachments/files/21074195/flatline-logs-20250704_2.txt)

Edit2: adding info about the miner:


```
Device Model: | Gamma (BM1370)
Uptime: | 2 hours, 46 minutes, 14 seconds
Wi-Fi Status: | Connected!
Wi-Fi RSSI: | -28 dBm
MAC Address: | <REDACTED>
Free Heap Memory: | 8400040
Firmware Version: | v2.9.0
AxeOS Version: | v2.9.0
ESP-IDF Version: | v5.4.1
Board Version: | 601
``` 



### Proximity-BBQ on 2025-07-05

@skot, please see the attached log. It seems that the ASIC simply has stopped at around (3785391).
[bitaxe_log.zip](https://github.com/user-attachments/files/21072268/bitaxe_log.zip)

### Proximity-BBQ on 2025-07-05

This seems abnormal:
` (3788777) stratum_task: Stratum response time: 3630705.67 ms `

### Chuth-ul on 2025-07-05

after 2 days it has now also occurred again for me

![Image](https://github.com/user-attachments/assets/61efd261-4513-4d8b-a7ce-211b4ec2ec16)

### dsaukou on 2025-07-08

Hello, I have the same problem with my Bitaxe 601 Gamma ("Flatline of Death" - hashrate stops changing, no new shares are found ). I get it from the "Minerfixes" seller on Aliexpress too(...

### skot on 2025-07-10

I'm still trying to reproduce this. I have four 60x running for weeks and still nothing.

From the logs and your descriptions it really seems like the esp-miner mining task is stopping. But why isn't it happening on any of my Bitaxes?

### dsaukou on 2025-07-10

I'm also have two BitAxe Gamma 601 from different sellers in Aliexpress. And one working absolutely normal from the first day, but the second device did'nt(...I don't know how explain this(... But you can see that the many people have the same problem with BitAxe 601, absolutely randomly.

### skot on 2025-07-10

> I'm also have two BitAxe Gamma 601 from different sellers in Aliexpress. And one working absolutely normal from the first day, but the second device did'nt(...I don't know how explain this(... But you can see that the many people have the same problem with BitAxe 601, absolutely randomly.

The build quality on many of the AliExpress Bitaxe hardware is bad. Can you see any obvious differences between your Bitaxe hardware that gets flatline of death and the one that does not?

### komeana on 2025-07-10

Can you put this in even if it's temporary?

<img width="516" height="64" alt="Image" src="https://github.com/user-attachments/assets/95c16ff5-9972-4516-acdc-dd492a5169cd" />

### komeana on 2025-07-10

It's burdensome to restart automatically for a long time with python.

### Chuth-ul on 2025-07-10

my Bitaxe comes from a german online shop, had it since 21.05, only have one and can't compare.
i have now tested v2.9.x, 2.8.x and 2.7.x, after a maximum of 2.5 days the problem occurs again
I am now back on v2.9.0 and have set a different pool to test this(Uptime 1 day, 3 hours, 37 minutes)

### nymkappa on 2025-07-12

Hi! I also have the same issue. I first assumed it was a bug with my self hosted public-pool, but the issue also reproduced on solock pool. I got my device from Plebstyle store in Germany.

I have a screenshot and the websocket logs

```
I (225713485) asic_result: ID: 6849364900016aa0, ver: 23D32000 Nonce 0E9401D0 diff 291191.8 of 4096.
I (225713489) stratum_api: tx: {"id": 2942, "method": "mining.submit", "params": ["REDACTED", "6849364900016aa0", "3100000000dbce3f", "6871b10c", "0e9401d0", "03d32000"]}
I (225713512) bm1370: Job ID: 70, Core: 23/0, Ver: 03E20000
I (225713518) asic_result: ID: 6849364900016aa0, ver: 23E20000 Nonce 2B31002E diff 2602.6 of 4096.
I (225713620) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 66.3% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225713684) stratum_api: rx: {"result":true,"error":null,"id":2942}
I (225713685) stratum_task: message result accepted
I (225714032) bm1370: Job ID: 08, Core: 119/0, Ver: 046A0000
I (225714034) asic_result: ID: 6849364900016aa0, ver: 246A0000 Nonce C25603EE diff 508.8 of 4096.
I (225715427) power_management: Temp: 62.2°C, SetPoint: 62.0°C, Output: 70.6% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225716983) bm1370: Job ID: 18, Core: 25/4, Ver: 03D08000
I (225716984) asic_result: ID: 6849364900016aa0, ver: 23D08000 Nonce 27A80232 diff 639.2 of 4096.
I (225717233) power_management: Temp: 61.9°C, SetPoint: 62.0°C, Output: 63.8% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225717624) bm1370: Job ID: 30, Core: 81/7, Ver: 058AE000
I (225717625) asic_result: ID: 6849364900016aa0, ver: 258AE000 Nonce 8D9501A2 diff 2077.3 of 4096.
I (225719040) power_management: Temp: 61.9°C, SetPoint: 62.0°C, Output: 64.4% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225719681) bm1370: Job ID: 28, Core: 106/15, Ver: 0021E000
I (225719682) asic_result: ID: 6849364900016aa1, ver: 2021E000 Nonce 459F00D4 diff 598.3 of 4096.
I (225720266) bm1370: Job ID: 40, Core: 73/14, Ver: 012BC000
I (225720267) asic_result: ID: 6849364900016aa1, ver: 212BC000 Nonce 11C80392 diff 317.9 of 4096.
I (225720377) bm1370: Job ID: 40, Core: 65/9, Ver: 02852000
I (225720378) asic_result: ID: 6849364900016aa1, ver: 22852000 Nonce DF420282 diff 579.1 of 4096.
I (225720846) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 66.5% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225720993) bm1370: Job ID: 58, Core: 1/15, Ver: 03F1E000
I (225720995) asic_result: ID: 6849364900016aa1, ver: 23F1E000 Nonce EC480602 diff 271.2 of 4096.
I (225721436) bm1370: Job ID: 70, Core: 110/2, Ver: 033E4000
I (225721437) asic_result: ID: 6849364900016aa1, ver: 233E4000 Nonce 96C702DC diff 1259.2 of 4096.
I (225721601) bm1370: Job ID: 70, Core: 122/0, Ver: 05400000
I (225721602) asic_result: ID: 6849364900016aa1, ver: 25400000 Nonce 1E4406F4 diff 335.8 of 4096.
I (225722329) bm1370: Job ID: 20, Core: 8/4, Ver: 01F08000
I (225722331) asic_result: ID: 6849364900016aa1, ver: 21F08000 Nonce 94030110 diff 1209.0 of 4096.
I (225722652) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 66.3% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225724461) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 66.3% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225726267) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 66.3% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225728074) power_management: Temp: 61.9°C, SetPoint: 62.0°C, Output: 64.2% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225729881) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 66.5% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225731688) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 66.3% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225733495) power_management: Temp: 61.9°C, SetPoint: 62.0°C, Output: 64.1% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225735301) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 66.4% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225737107) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 66.2% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225738913) power_management: Temp: 61.9°C, SetPoint: 62.0°C, Output: 64.1% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225740720) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 66.4% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225742526) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 66.2% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225743142) stratum_task: Stratum response time: 13438924.67 ms
I (225743143) stratum_api: rx: {"params":["6849364900016aa2","ecf556b5f84cb936a8bac6a564389fcddccfedf20000037a0000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3503c6cf0d000448b1716804bf12aa060c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff037f7e58120000000017a914a51a96e59fdaec87627cb3ef00bb1abcff881e1487c9d85f000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9ed09353a957dd5700cba9a551ce10e439553e3582facefed1dba3e200a069f36e500000000",["92166790e0ded05ce5399e2cd747898756795311cee5cf7376adf0184785131a","eed83a53261c17d8a36c5432cf6e1d23f71fc9c9998c5e1366481138154b3940","5f87e9546c58a5bea81f5dd549e0bbd96222ea5cd9fba340c407495937dc8f6d","19700b72e2dd5fbff673f87bc9a5482ed653a23e4f27a4d60d64bd8ad088b724","d8df0995b9ee8bef0e5a579b1c2cbdadc63f078aa3fb49068da58fa369bfda49","4ddfea6d9ef1d70b0e98b73f0961471ef4563f8559209e36621ad52f900be1a6","f3fb4a6f21507d2d12b87416fd6bf9d28c603b5263a34652ce66324ceb2224f4","90bc40ab146d73882245a7b2d4b66bd67542db9003a706e07736acd239bafa0d","b9b463c0a87c57fadd0100f3dd8c2bbe62c21089a799db130df8c271b51fdd93","e2a50cbfad1be90069fecdf8f86b5c8644475ddbabfaa8e6f8217a101e63e9c6","10a49875bd195c14fde12637e758175b0264c110cc58b8cfd1a7d847f9791973","56544b097891d381ccef34cdd02d37bdc4258b03948e068fb904259a5dda2824"],"20000000","17026816","6871b148",false],"id":null,"method":"mining.notify"}
I (225743331) create_jobs_task: New Work Dequeued 6849364900016aa2
I (225744332) power_management: Temp: 62.1°C, SetPoint: 62.0°C, Output: 68.3% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225746139) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 66.0% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225747945) power_management: Temp: 61.9°C, SetPoint: 62.0°C, Output: 64.1% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225749753) power_management: Temp: 62.2°C, SetPoint: 62.0°C, Output: 70.6% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225751560) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 65.8% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225753367) power_management: Temp: 62.1°C, SetPoint: 62.0°C, Output: 68.4% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225755173) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 66.1% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225756979) power_management: Temp: 61.9°C, SetPoint: 62.0°C, Output: 64.2% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225758785) power_management: Temp: 61.9°C, SetPoint: 62.0°C, Output: 64.3% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225760592) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 66.4% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225762398) power_management: Temp: 61.9°C, SetPoint: 62.0°C, Output: 64.1% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225764204) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 66.4% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225766011) power_management: Temp: 61.9°C, SetPoint: 62.0°C, Output: 64.0% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225767817) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 66.3% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225769623) power_management: Temp: 62.1°C, SetPoint: 62.0°C, Output: 68.2% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225771429) power_management: Temp: 62.1°C, SetPoint: 62.0°C, Output: 68.1% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225773129) stratum_api: rx: {"params":["6849364900016aa3","ecf556b5f84cb936a8bac6a564389fcddccfedf20000037a0000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3503c6cf0d000466b1716804d881ff050c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff03bdc759120000000017a914a51a96e59fdaec87627cb3ef00bb1abcff881e148781df5f000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9ed427943f1f555ff19331bbbbf32661c9a937dab873a2a3fe45d21c8da00eaf57c00000000",["92166790e0ded05ce5399e2cd747898756795311cee5cf7376adf0184785131a","eed83a53261c17d8a36c5432cf6e1d23f71fc9c9998c5e1366481138154b3940","08c80c7f581dbaae3efd041e7ad0563d168714e3326648c54b2d63c5df4ef61f","d0ad63acc8fc30c66569ab0e4648d5bf0aeaaf5b9c0f70bbb6d6d621d2023dba","8b2011e8b1e717df6fae5187ef460befc54d72ffc5def04f12adbb072f9ea9e1","28f05be232979c69305d0ecdd4b3a01dcbbf120a9bba72c2d780afd7b783e81b","8f99e6a0d402d4d1c5d4037f285d81f01b6ef7a7f8eedb9efc1fea4dc28b3e63","dadac9c2b97d6b10d4e82ff96c7a87d8a1b25d2b26245b64794d31b327797727","0b12887907c8b685a06e5c31709ef3f550d6cdbe05b0a5b4c647c2093708a070","f3c59a81560154b69429de7b88c973a180c0744cffdd3716eac5c8e8336ae3e3","d575842b9bd8ae529bd2dd85add2847d555b0b37d3baf8d2807c3dc598dbd887","99d3e0004a1bf136ce95eb4eb4170355567fcae613205897fe423ddcf4ece492"],"20000000","17026816","6871b166",false],"id":null,"method":"mining.notify"}
I (225773235) power_management: Temp: 62.2°C, SetPoint: 62.0°C, Output: 70.3% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225773300) create_jobs_task: New Work Dequeued 6849364900016aa3
I (225775059) power_management: Temp: 62.2°C, SetPoint: 62.0°C, Output: 70.1% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225776866) power_management: Temp: 61.9°C, SetPoint: 62.0°C, Output: 63.8% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225778672) power_management: Temp: 62.1°C, SetPoint: 62.0°C, Output: 68.7% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225780479) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 66.2% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225782286) power_management: Temp: 61.9°C, SetPoint: 62.0°C, Output: 64.3% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225784092) power_management: Temp: 62.1°C, SetPoint: 62.0°C, Output: 68.7% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225785898) power_management: Temp: 61.9°C, SetPoint: 62.0°C, Output: 64.1% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225787704) power_management: Temp: 62.0°C, SetPoint: 62.0°C, Output: 66.6% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225789510) power_management: Temp: 62.1°C, SetPoint: 62.0°C, Output: 68.5% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225791316) power_management: Temp: 61.9°C, SetPoint: 62.0°C, Output: 64.1% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225793122) power_management: Temp: 62.1°C, SetPoint: 62.0°C, Output: 68.7% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225794928) power_management: Temp: 62.1°C, SetPoint: 62.0°C, Output: 68.3% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225796735) power_management: Temp: 62.1°C, SetPoint: 62.0°C, Output: 68.4% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225798541) power_management: Temp: 61.9°C, SetPoint: 62.0°C, Output: 64.1% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225800347) power_management: Temp: 61.8°C, SetPoint: 62.0°C, Output: 62.4% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225802154) power_management: Temp: 62.1°C, SetPoint: 62.0°C, Output: 68.9% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225803124) stratum_api: rx: {"params":["6849364900016aa4","ecf556b5f84cb936a8bac6a564389fcddccfedf20000037a0000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3503c6cf0d000484b1716804f051bf050c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff0335c05a120000000017a914a51a96e59fdaec87627cb3ef00bb1abcff881e148793e45f000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9eda4b2232c882329a03eedb48295dcbe0a343c0161598f06de4bcc7d505977586600000000",["92166790e0ded05ce5399e2cd747898756795311cee5cf7376adf0184785131a","7c966427653bc22ee3c70a05f1533952252f1a24c9c7615b4f4f44ccda39d471","2eeb918a8a3fdab667375d5ffc04234cc84262b07ca52646e8d608078ca5c3df","e19284a66d390ed7ba02deb2132057ca8e13397c922cd62571dec41f2bb089aa","54dd7b7d85bf19dec3cfc5d1a00d8921f3d39eb09ba7eae8a6355b5c63adb037","6318902a6082e00a480f3ad18085012833f2e9b6857faeaa9abc30fb1959e558","cd5a58aec06242d74d6cf5d62b5d136983c5c7da73696438e982c7b711b30d62","5a934da1e4cbbb4b50cf213c4d64364181bf3b766ef51d0555878e8bc89922a5","9cd9a2bcd0e204cd4f14c82c48ab07fb671679587455c82c235460d2204bd173","62a48858aaf626f9cbf072163900e850126577f878ba56299f54a0681f5ca290","86a06bab61eabe8d2653d3a8b1835ef69c2a89c9e721cf10324a58bfdb760159","d79850eb4c5b5aa539861d382e91feb157a4184c4afb1b59832f383ca7877966"],"20000000","17026816","6871b184",false],"id":null,"method":"mining.notify"}
I (225803264) create_jobs_task: New Work Dequeued 6849364900016aa4
I (225803962) power_management: Temp: 61.9°C, SetPoint: 62.0°C, Output: 64.1% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (225805768) power_management: Temp: 61.9°C, SetPoint: 62.0°C, Output: 64.4% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
```

Similar to what was reported by someone else, this log in particular is suspicious

```
I (225743142) stratum_task: Stratum response time: 13438924.67 ms
```

After that, the Bitaxe does just stops mining.

I was running at 650MHz / 1150 Core Voltage. Temps are good (target 62 degrees). All power measures seemed nominal.

<img width="838" height="835" alt="Image" src="https://github.com/user-attachments/assets/d9f2241f-a4fb-4716-85a8-6a28f5476f05" />

### Suggestion

When the measured "Stratum response time" is higher than say 30000 ms, disconnect and reconnect to the stratum server (or switch to the failover pool), so that the mining process can be "reset".

### Temporary workaround

For now I'm just going to reboot the bitaxe every couple of hours. Is it okay to do that or not?

```
watch -n7200 curl 'http://192.168.1.37/api/system/restart' -X POST
```


### skot on 2025-07-12

I'm thinking this is hardware related somehow. Can you give me all the details of your setup? Bitaxe HW version number, heatsink, fan, case. Power supply make and model, etc. Where you purchased the Bitaxe. Pictures are good.

### dsaukou on 2025-07-12

I suggesting simply rebooting automatically Bitaxe 601 in this case to solve this problem (if this possible to do with modification the firmware). And don't deeply thinking about this)

### nymkappa on 2025-07-12

> I'm thinking this is hardware related somehow. Can you give me all the details of your setup? Bitaxe HW version number, heatsink, fan, case. Power supply make and model, etc. Where you purchased the Bitaxe. Pictures are good.

https://pleb.style/en-fr/products/bitaxe-gamma-v601-1-3th-s-silent-made-in-germany-incl-power-supply-stand

```
Device Model: | Gamma  (BM1370)
Uptime: | 29 minutes, 18 seconds
Wi-Fi Status: | Connected!
Wi-Fi RSSI: | -62 dBm
MAC Address: | REDACTED
Free Heap Memory: | 8399752
Firmware Version: | v2.9.0
AxeOS Version: | v2.9.0
ESP-IDF Version: | v5.4.1
Board Version: | 601
```

### Chuth-ul on 2025-07-13

short update: after changing the pool to eusolo.ckpool.org i now have an uptime of 4 days and still no problems.
was previously parasite, what was noticeable here was a bad ping of about 150 from germany.

![Image](https://github.com/user-attachments/assets/e8466fc0-96f2-438b-83b3-78e8d5174785)

### skot on 2025-07-13

Whoa, very interesting discovery. Thanks @Chuth-ul I'll try this with parasite and see if I can reproduce. @komeana @homecryptominer @Proximity-BBQ @dsaukou what pools are you using when you see this problem?

### dsaukou on 2025-07-13

In my case, I used many different pools, such as:  Braiins.com, Unmineable.com,  Public-pool.io, eusolo.ckpool.org and others. During the work with different pools this problem appears in time from 3-5 minutes to 1-2 days(. So, there's no difference what was pool(

### nymkappa on 2025-07-13

In the mean time, I wrote this quick nodejs script to automatically restart the Bitaxe if it does not find any shares for more than 5 minutes. It's barely tested so feel free to adjust it to your need.

No deps required.

```javascript
import { setTimeout as sleep } from 'timers/promises';
import http from 'http';

const RESTART_THRESHOLD_SECONDS = 300; // Restart if the Bitaxe did not find any shares for more than 5 minutes

const args = process.argv;
if (!args[2]) {
  console.error(`Usage: node ./bitaxe-monitor.js BITAXE_IP_ADDRESS`);
  process.exit(1);
}

const optionsGetSystemInfo = {
  hostname: args[2],
  port: 80,
  path: '/api/system/info',
  method: 'GET',
};

const optionsRestart = {
  hostname: args[2],
  port: 80,
  path: '/api/system/restart',
  method: 'POST',
};

async function run() {
  let lastAcceptedShareCount = 0;
  let lastShareChangeTimestamp = new Date().getTime() / 1000;

  while ("tick tock next block") {
    try {
      await sleep(5000);

      const systemInfoJSON = await queryBitaxeAPI(optionsGetSystemInfo);
      if (!systemInfoJSON) {
        console.info(`[${getFormattedTime()}] Unable to query http://${args[2]}/api/system/info`);
        continue;
      }

      const systemInfoObject = JSON.parse(systemInfoJSON);
      if (!systemInfoObject) {
        console.info(`[${getFormattedTime()}] Unable to parse response from http://${args[2]}/api/system/info`);
        continue;
      }

      if (systemInfoObject.sharesAccepted === undefined) {
        console.info(`[${getFormattedTime()}] Missing "systemInfoObject.sharesAccepted" in response from http://${args[2]}/api/system/info`);
        continue;
      }

      let accepetedShareChange = systemInfoObject.sharesAccepted - lastAcceptedShareCount;
      console.info(`[${getFormattedTime()}] ${systemInfoObject.sharesAccepted} accepted shares (+${accepetedShareChange} | Diff: ${systemInfoObject.bestSessionDiff} | Best: ${systemInfoObject.bestDiff})`);
      if (accepetedShareChange > 0) {
        lastAcceptedShareCount = systemInfoObject.sharesAccepted;
        lastShareChangeTimestamp = new Date().getTime() / 1000;
      } else {
        const now = new Date().getTime() / 1000;
        const timeSinceLastShareChange = Math.round(now - lastShareChangeTimestamp);
        if (timeSinceLastShareChange > RESTART_THRESHOLD_SECONDS) { // No share found for 5 minutes, restart the Bitaxe
          console.info(`[${getFormattedTime()}] No share found for ${timeSinceLastShareChange} seconds, restarting Bitaxe`);
          await queryBitaxeAPI(optionsRestart);

          // "Restart" the loop with inital conditions after we gave enough time for the Bitaxe to reboot and start mining
          await sleep(60000);
          lastAcceptedShareCount = 0;
          lastShareChangeTimestamp = new Date().getTime() / 1000;
        }
      }

    } catch (e) {
      console.error(`[${getFormattedTime()}] Exception ${e} (message: ${e.message} / code: ${e.code})`);
    }
  }
}

async function queryBitaxeAPI(options) {
  return new Promise((resolve, reject) => {
    const req = http.request(options, (res) => {
      let data = '';

      // A chunk of data has been received.
      res.on('data', (chunk) => {
        data += chunk;
      });

      // The whole response has been received.
      res.on('end', () => {
        resolve(data);
      });
    });

    // Handle any errors
    req.on('error', (error) => {
      console.error(`[${getFormattedTime()}] Query error:`, error);
      resolve(null);
    });

    // End the request
    req.end();
  });
}

function getFormattedTime() {
  const now = new Date();
  return now.toISOString().replace('T', ' ').substring(0, 19); // Format: YYYY-MM-DD HH:MM:SS
}

run();
```

Example output

```
$ node bitaxe-monitor.js 192.168.1.37
[2025-07-13 18:13:06] 91 accepted shares (+91 | Diff: 176.63k | Best: 387.66M)
[2025-07-13 18:13:11] 91 accepted shares (+0 | Diff: 176.63k | Best: 387.66M)
[2025-07-13 18:13:16] 91 accepted shares (+0 | Diff: 176.63k | Best: 387.66M)
[2025-07-13 18:13:21] 92 accepted shares (+1 | Diff: 176.63k | Best: 387.66M)
[2025-07-13 18:13:26] 92 accepted shares (+0 | Diff: 176.63k | Best: 387.66M)
[2025-07-13 18:13:31] 92 accepted shares (+0 | Diff: 176.63k | Best: 387.66M)
[2025-07-13 18:13:37] 93 accepted shares (+1 | Diff: 176.63k | Best: 387.66M)
[2025-07-13 18:13:42] 93 accepted shares (+0 | Diff: 176.63k | Best: 387.66M)
...
```

### skot on 2025-07-14

I wasn't able to reproduce the Flatline of Death over the last week on 5 bitaxeGamma 601. @komeana @homecryptominer @Proximity-BBQ @dsaukou would one of you (or anyone else) be willing to send me your failing bitaxe (and power supply)? Ideally this is someone in the US. I'll give you a code for a free bitaxeGamma 601 from SoloSatoshi to replace it.

Being able to reproduce the problem easily on my desk is the fastest way I can think of to address this issue...

### jpx13 on 2025-07-15

Hello,
I have seen all this thread is about Gamma 601, but I can confirm the same issue with a Supra 402 from DTV Electronics.
It wasn't doing this when I bought it, and since a few weeks, it sometimes hangs (no hashing) though reporting a hash rate in a flat line of death.
Don't know if it could be upgrade related, but I am running 2.9.0
Happened on Parasite, but also I think at least one time on Braiins (I switched some days ago to test) I am not 100% sure for Braiins though, so I will keep monitoring it. It happened also with a Max 1397 on Parasite.
I have also a Nerdaxe that hashes on Parasite, it is up since more than 2 weeks without issue.
Hope this can help

### skot on 2025-07-17

I think I have reproduced this issue! On a Bitaxe Ultra 204. We had a power outage (or maybe a brownout) at my office overnight. When I looked at my Bitaxes in the morning, most of them were back on and working fine, but 3-4 of them had a power fault warning in AxeOS, and this one 204 had a flatline of death!

<img width="635" height="427" alt="Image" src="https://github.com/user-attachments/assets/5f0bd818-5473-4e56-be47-7949b633d1a6" />

The logs show that the pool (public-pool) is still alive and sending new work. The fan control task is still working too. Just no new shares from the ASIC.

I carefully measured the ASIC voltage manually, and confirmed it's on, 1.2V.

I connected my logic analyzer to the ASIC data pins and confirmed esp-miner is indeed still sending new work to the ASIC. Just no responses from the ASIC.

There does seem to be some noise on the RST pin. I need to look at this on the 'scope.

### dsaukou on 2025-07-17

Exactly, as on my BitAxe 601 Gamma (as in your picture)....

### skot on 2025-07-17

> There does seem to be some noise on the RST pin. I need to look at this on the 'scope.

Looks like this was a loose connection on the Logic Analyzer. Not seeing any noise on the RST pin on the scope.



### Proximity-BBQ on 2025-07-20

> Not seeing any noise on the RST pin on the scope.

Does it means it's a hardware issue?

Not sure if it's related, but my problematic Gamma is rock solid for more than 10 days after re-flashed via the web flasher.

### skot on 2025-07-20

My guess is there was a power fault that is causing the ASIC to reset. So now the ASIC needs to be initialized, but esp-miner is just sending work like nothing happened.

This points to the need for that status task to be a watchdog for ASIC shares. I'll see if I can put that together for a future esp-miner release.


### nymkappa on 2025-07-20

> My guess is there was a power fault that is causing the ASIC to reset. So now the ASIC needs to be initialized, but esp-miner is just sending work like nothing happened.
> 
> This points to the need for that status task to be a watchdog for ASIC shares. I'll see if I can put that together for a future esp-miner release.

My apartment power does not seem very stable (just by looking at the lights lol) so that might be it indeed

### FLBeach on 2025-07-25

So I have a Gamma 601 and have been fighting with this for a week since I received it. Got it from UltraMinerX on Amazon. I have just been restarting it whenever I am home and notice it is not hashing. I solo pool on Braiins.  I also have an Avalon Nano 3s on the same pool and wifi with no issues. 

I was first logging in with my laptop to set everything up and it kept flatlining sometime between 30 minutes and 4 hours or so and showing inactive on the pool. I then used my phone to access the setting. Eureka! it worked all day. Decided to go down to the woods (no cell service) and when I came back it was flatlining again. 

I figured out that whenever I left the house with the laptop it would drop. Same thing when the laptop would go to sleep after 4 hours. Does this require to have a pc/phone connected at all times to keep it running? Use chrome for phone and laptop. 

Tried airplane mode and could not recreate it. I'm stumped. 

### dsaukou on 2025-07-31

@skot , did you have any good news for us (about problem)?

### FLBeach on 2025-07-31

I received a replacement from the seller and decided to run them side by side before I returned the other one. I restarted them at the same time with the same settings and surprisingly, they have both been running for 2 days now. Maybe the Gamma was just lonely and needed a friend .... 

### skot on 2025-07-31

> [@skot](https://github.com/skot) , did you have any good news for us (about problem)?

no, i'm flying blind without a miner that can reproduce this problem.

### ghost on 2025-08-01

7 devices here - not able to reproduce this issue from the first day it was reported here (June 20th).

### b68074068-sudo on 2025-08-07

since i get my bitaxe gammas all went well for 3-6 weeks with standard settings. 
than i used V 2.9.0 on all 3 bitaxe gammas and begun slighly to go a bit over the standard settings.
all good for 1-2 weeks.

have recently updated the coolingsystem of all 3 to Noctua fan + 52Pi Low profile heatsink + Thermal Grizzly with normal dc adapter.
now i begun to overclock them, max temp ASCII 58/59 degrees. Max. VRC 75 degree.
2 of them no issues , since 2 days one of them gets the FoD.
It happens quite fast after 1-3 (sometimes longer 10) minutes and with differet settings:

<img width="1867" height="895" alt="Image" src="https://github.com/user-attachments/assets/a6355e36-a083-430d-b02b-601fe741228a" /> 

<img width="1632" height="897" alt="Image" src="https://github.com/user-attachments/assets/dfa1add2-914c-4168-84c2-3f9b030394b4" />

<img width="1851" height="894" alt="Image" src="https://github.com/user-attachments/assets/142dba47-a302-49e8-b980-9966ff73ce04" />

<img width="1597" height="861" alt="Image" src="https://github.com/user-attachments/assets/366dd45f-e8d2-45f0-956f-4deaa17b1f39" />

<img width="1495" height="509" alt="Image" src="https://github.com/user-attachments/assets/e4f17ca4-85b1-4838-9641-e3d7e5d76bef" />

<img width="759" height="385" alt="Image" src="https://github.com/user-attachments/assets/52dd9a76-a749-4575-9d9e-3e8f73407370" />
<img width="1485" height="391" alt="Image" src="https://github.com/user-attachments/assets/9f6f4e2c-07e4-4564-b475-43829876dc7b" />
<img width="462" height="60" alt="Image" src="https://github.com/user-attachments/assets/619dd34b-feac-4fbc-addc-5cc6e688aa62" />

### b68074068-sudo on 2025-08-09

perhaps its really the missing voltage at some point, will try with meanwell dc unit.

### joaoramalho on 2025-08-13

I'm having this exact same issue but with my Bitaxe Supra.

It was working fine, until I made a small incremental overclock.

After that I'm experiencing all these symptoms. It works fine for some minutes, and then freezes.

I'm forced to restart the Bitaxe and then starts working again for a couple more minutes.


I tried using a different power supply, undervolt the asic, move the Bitaxe to a cooler room/better wifi, but no success.

Something that I noticed though, even though the UI freezes, the asic temp stays around 60C, so maybe is doing something that we cannot see?

As someone pointed out in an above comment, it might be some sort of discrepancy between the ESP and what the ASIC is doing.

Some screenshots:

<img width="1351" height="833" alt="Image" src="https://github.com/user-attachments/assets/5bf6c7b2-54ac-4178-94ee-5ac5c5d3a39a" />

<img width="675" height="346" alt="Image" src="https://github.com/user-attachments/assets/05488aba-3eac-4567-9cbc-2b82470f53fe" />

<img width="1336" height="778" alt="Image" src="https://github.com/user-attachments/assets/eb8957d6-0229-4810-9b80-2923c9e5b39b" />


At this point I thought I fried something on the board when I upgraded the heatsink with a Noctua fan and thermal paste.

### dsaukou on 2025-08-14

Have the same problem a long time...Noctua and another thermal paste or another power supply  didn't solve this problem(((

### b68074068-sudo on 2025-08-20

since i changed to Version 2.7.1 no FoD anymore...

<img width="1741" height="824" alt="Image" src="https://github.com/user-attachments/assets/ada34a48-72a4-4de7-ba2a-ec74a78124e0" />

<img width="1778" height="545" alt="Image" src="https://github.com/user-attachments/assets/dc3b5f42-88fd-405d-8588-26387300cf1d" />

### dsaukou on 2025-08-20

Working 5 h 44 min only? Or much  more time? May be It's  very small period to draw conclusions...My Bitaxe 601 working time to FoD from 2-3min to 1-2 days(...But I'm don't  remember which exactly version of firmware was in Bitaxe in this periods (but they was a different)        

### joaoramalho on 2025-08-20

Tested on my Supra, it's FoDing even on 2.7.1. 

Sometimes almost immediately, or after 10 or 20 minutes.

### dsaukou on 2025-08-21

Exactly. 

### b68074068-sudo on 2025-08-21

you are right guys, sadly it has nothing to do with the version, FoD also returns on 2.7.1:

<img width="1887" height="1033" alt="Image" src="https://github.com/user-attachments/assets/2922b4ab-fb3b-4b8b-97a1-ddfefb3f3d5d" />
<img width="1587" height="843" alt="Image" src="https://github.com/user-attachments/assets/a9ddc99c-8794-44c0-8202-346936172fc5" />

### skot on 2025-09-23

In order to stay focused on reproducing this issue, please use this space only for reporting flatline hashrate where the stratum pool is still alive. You can confirm that by looking at the logs in AxeOS for lines that start with `stratum_api: rx: {...`

### skot on 2025-09-23

I received a Bitaxe (and PSU) in the mail from a user that was reporting regular FoD. It has been running for almost 2 weeks straight in my office with no sign of the issue.

I'm starting to wonder if this bug is because of an AC Power quality issue _before_ the PSU.

### joaoramalho on 2025-09-23

> I received a Bitaxe (and PSU) in the mail from a user that was reporting regular FoD. It has been running for almost 2 weeks straight in my office with no sign of the issue.
> 
> I'm starting to wonder if this bug is because of an AC Power quality issue _before_ the PSU.

In my case my Supra is still FoD even when I tried another PSU. 
It is connected in the same socket where my other gammas and they are fine.
Also tried plugging it in a different room, same result.
It works for the first 5 minutes then dies.

### BTChodlinon on 2025-10-12

I have a Gamma 601 getting the FOD. Somtimes within a minute of reboot, sometimes it will run for a week. Running 2.10.0              I've also tried wiping it and resetting it up from new. It happens to public pool & Kano both. Mine is a SoloSatoshi btw.

### ghost on 2025-10-13

> I have a Gamma 601 getting the FOD. Somtimes within a minute of reboot, sometimes it will run for a week. Running 2.10.0 I've also tried wiping it and resetting it up from new. It happens to public pool & Kano both. Mine is a SoloSatoshi btw.

What other pools have you tried, and do you get the same result on those ?
*I tested one of my Gamma's on those two pools for a week each, could not reproduce the issue.*

### BTChodlinon on 2025-10-13

<img width="2360" height="1640" alt="Image" src="https://github.com/user-attachments/assets/b4f21854-4c2c-4200-bf1a-cad62bc51932" />
Public Pool & Kano are the only two I've tried, both did it. I also upgraded the PS to a Mean Well hoping it was a power issue.

### BTChodlinon on 2025-10-21

I ordered a NerdQaxe++, so we'll see if it's hardware or environment related. I'll update after I've got it up and running for a couple of weeks. 

### BTChodlinon on 2025-10-22

So, got the NerdQaxe++ up and running to Public pool along with the Gamma. After about 2 hours, the Gamma flatlined and the NerdQaxe is still hashing away. Seems to have ruled out pool/network connection etc. I'm guessing it's hardware related. 
I did have 2 different days last week where the Gamma flatlined for an hour or two, then came back online.

<img width="1180" height="820" alt="Image" src="https://github.com/user-attachments/assets/8d5060ac-f744-46bf-af91-9b360473ea3e" />
<img width="1398" height="645" alt="Image" src="https://github.com/user-attachments/assets/8fcf18f6-f186-4352-aad9-06167bcd95d1" />

### ghost on 2025-10-23

Hmm !  

No share count shown in your screenshot (1st screenshot).  

### WantClue on 2025-11-03

@BTChodlinon is it possible that we arrange a more in depth logging for this device? With just these pictures it's not possible to debug the potential issue. Would be interesting to see what exactly is causing this and maybe there are some hints in the logs

### EricDimitri on 2025-11-03

Hi!! I have 2 Gamma 601, and one of them has the "Flat Line" Issue... both are conencted to the same Power SOurce. 

<img width="917" height="848" alt="Image" src="https://github.com/user-attachments/assets/c612f30d-40d1-420e-94df-efe9ac27f5e2" />

IT happens more or less every hour. I did some coding to restart when it happens, that's why It keeps running... Do you need me to provide you mor einfo?

Thanks for all your work!!!

  Eric

IT just happened again at the time of sending this:

<img width="913" height="911" alt="Image" src="https://github.com/user-attachments/assets/163c77fb-ed48-4ad7-bd40-17bdbefcd0c5" />

... and again... 

<img width="899" height="851" alt="Image" src="https://github.com/user-attachments/assets/03d0f286-f115-4e8c-ba06-a4e3c511ad3a" />

### WantClue on 2025-11-03

can you please track the logs via usb serial? it's really important that we see what happens exactly at that flatline event 




### EricDimitri on 2025-11-03

@WantClue,    since I saw that a potential issue could be the "power" provided to the units, and since i had mines connected to a "Low Quality" Ups, I disconnected both, and connected directly the PSU to the power outlet of the wall... IT has been 43 minutes already, and still no FlatLine. Lets see what happens... lets wait several hours.... but looks promising...

*** UPDATE *** IT happened again, so tell me what exactly you need me to do :)

### EricDimitri on 2025-11-03

LEt me add something, since I know how important in this scenarios is, to gather as much info as possible from an environment whenre the issue is replicable, even if the change of connecting the PSU directly to the power putlet and taking away the UPS solves the issue, I am more than glad to help you gather all the info that might help you to solve this. LEts see how this cointinues, and then if it is solved for me, we know at least in my case what the problem was, and also lets check whatever you want to see how that is affecting the Gamma 601, and what coud be one to fix it

### EricDimitri on 2025-11-03

> can you please track the logs via usb serial? it's really important that we see what happens exactly at that flatline event

Can you tell me exactly how to do that? Thanks!!

## UPDATE ##
Sorry for the spam hahaha I managed to grab log with putty thru usb cable. WHat I dont like is that it doesn have a timestamp so, It might be hard to find moment when it started the flatline, but lets see how it goes... As soon as i have one, will let you know.

Thanks again!!

### skot on 2025-11-03

> > can you please track the logs via usb serial? it's really important that we see what happens exactly at that flatline event
> 
> Can you tell me exactly how to do that? Thanks!!
> 
> ## UPDATE
> 
> Sorry for the spam hahaha I managed to grab log with putty thru usb cable. WHat I dont like is that it doesn have a timestamp so, It might be hard to find moment when it started the flatline, but lets see how it goes... As soon as i have one, will let you know.
> 
> Thanks again!!

We know that when the FoD starts the ASIC will stop sending shares, which you can see (the lack of) in the USB logs.

### EricDimitri on 2025-11-03

### UPDATE ###

@skot 

Ok, here is the log... IT was ok, like this:

```
[0;32mI (21799533) bm1370: Job ID: 70, Core: 116/14, Ver: 0617C000[0m
[0;32mI (21799534) asic_result: ID: 546f6d5, ver: 2617C000 Nonce 9BAD04E8 diff 829.2 of 8192.[0m
[0;32mI (21799624) bm1370: Job ID: 08, Core: 112/14, Ver: 0119C000[0m
[0;32mI (21799625) asic_result: ID: 546f6d5, ver: 2119C000 Nonce 0B0504E0 diff 293.5 of 8192.[0m
[0;32mI (21799983) bm1370: Job ID: 08, Core: 74/4, Ver: 05788000[0m
[0;32mI (21799983) asic_result: ID: 546f6d5, ver: 25788000 Nonce 1EF20494 diff 672.3 of 8192.[0m
[0;32mI (21800574) bm1370: Job ID: 38, Core: 49/11, Ver: 007B6000[0m
[0;32mI (21800575) asic_result: ID: 546f6d5, ver: 207B6000 Nonce B5BA0462 diff 773.3 of 8192.[0m
[0;32mI (21800798) bm1370: Job ID: 38, Core: 98/8, Ver: 03370000[0m
[0;32mI (21800799) asic_result: ID: 546f6d5, ver: 23370000 Nonce C14D06C4 diff 1472.4 of 8192.[0m
[0;32mI (21801485) bm1370: Job ID: 50, Core: 126/9, Ver: 05812000[0m
[0;32mI (21801485) asic_result: ID: 546f6d5, ver: 25812000 Nonce 927000FC diff 1223.7 of 8192.[0m
[0;32mI (21801500) bm1370: Job ID: 50, Core: 7/11, Ver: 05AF6000[0m
[0;32mI (21801500) asic_result: ID: 546f6d5, ver: 25AF6000 Nonce 01E9030E diff 338.3 of 8192.[0m
[0;32mI (21802092) bm1370: Job ID: 00, Core: 78/7, Ver: 00B4E000[0m
[0;32mI (21802093) asic_result: ID: 546f6d5, ver: 20B4E000 Nonce 3FA7029C diff 260.0 of 8192.[0m
[0;32mI (21804255) bm1370: Job ID: 60, Core: 49/4, Ver: 02B28000[0m
[0;32mI (21804256) asic_result: ID: 546f6d5, ver: 22B28000 Nonce 56340262 diff 957.4 of 8192.[0m
[0;32mI (21804573) bm1370: Job ID: 78, Core: 39/7, Ver: 0078E000[0m
[0;32mI (21804574) asic_result: ID: 546f6d5, ver: 2078E000 Nonce 5EFC044E diff 397.0 of 8192.[0m
[0;32mI (21807730) bm1370: Job ID: 08, Core: 18/4, Ver: 02648000[0m
[0;32mI (21807731) asic_result: ID: 546f6d5, ver: 22648000 Nonce 85DB0124 diff 663.5 of 8192.[0m
[0;32mI (21808037) bm1370: Job ID: 20, Core: 77/10, Ver: 00094000[0m
[0;32mI (21808038) asic_result: ID: 546f6d5, ver: 20094000 Nonce 1BFA049A diff 273.5 of 8192.[0m
[0;32mI (21808697) bm1370: Job ID: 38, Core: 115/8, Ver: 01FB0000[0m
[0;32mI (21808697) asic_result: ID: 546f6d5, ver: 21FB0000 Nonce 47BC03E6 diff 476.7 of 8192.[0m
[0;32mI (21809331) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
```
Then it started to repeat  de diff, Job Id, Core Ver:
```
[0;32mI (21808697) asic_result: ID: 546f6d5, ver: 21FB0000 Nonce 47BC03E6 diff 476.7 of 8192.[0m
[0;32mI (21809331) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21809332) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
[0;32mI (21809378) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21809379) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
[0;32mI (21809426) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21809426) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
[0;32mI (21809473) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21809474) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
[0;32mI (21809520) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21809521) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
[0;32mI (21809568) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21809568) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
[0;32mI (21809615) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21809616) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
[0;32mI (21809662) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21809663) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
[0;32mI (21809709) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21809710) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
[0;32mI (21809757) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21809758) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
[0;32mI (21809804) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21809805) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
[0;32mI (21809851) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21809852) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
[0;32mI (21809899) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21809899) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
[0;32mI (21809946) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21809947) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
[0;32mI (21809993) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21809994) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
```
and then this:  
```
[0;32mI (21816852) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21816853) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
[0;32mI (21816899) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21816900) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
[0;32mI (21816946) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21816947) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
[0;32mI (21816994) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21816995) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.[0m
[0;32mI (21817041) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21817042) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.[0m
[0;32mI (21817088) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21817089) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.[0m
[0;32mI (21817136) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21817136) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.[0m
[0;32mI (21817183) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21817184) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.[0m
[0;32mI (21817230) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21817231) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.[0m
[0;32mI (21817278) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21817278) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.[0m
[0;32mI (21817325) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21817326) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.[0m
[0;32mI (21817372) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21817373) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.[0m
[0;32mI (21817419) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21817420) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.[0m
[0;32mI (21817467) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000[0m
[0;32mI (21817468) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.[0m
```
Diff went to 0

And stays like that forever, until you restart it.

Any thoughts? 

   Eric







### BTChodlinon on 2025-11-04

So the NerdQaxe++ has worked flawlessly since getting it almost 2 weeks ago. The Gamma was hashing for about 5-10 minutes, then flatlining. I ended up unplugging it instead of rebooting through the UI and it's been up since. It will flatline occasionally for an hour but then starts back on it's own. As someone above said, it would also occasionally freeze and the web page wouldn't load or anything. 

### EricDimitri on 2025-11-04

IT happened again now, different behaviour:

```
I (696909) stratum_api: rx: {"id":null,"method":"mining.notify","params":["55c4e24","5a6663f8e38a22c68938ab4e40ac0655a0722a590000b6ae0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170306120e5075626c69632d506f6f6c","ffffffff02f2a8bd12000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9edbff3e1dded23e47a885a0cebd0bc456459d8112c99ccea075269a4421771b57b00000000",["d32df1b7fb709e906b73e75eb9c95a47f1d0b59efac11997e889a2df89d812c3","7bc45c6eeb40552d4e6d85bd45cc9224d4db251ec259f442c6efbac5fff1966f","6f6f96eb2d4629f33e34852db28013ee4acf90e2774e4f1e39a960f5e47217fc","c2e8d94e47fb83d6b62521ead5c27472979a32247eb04ce11b700c25aeae47b1","684fa43c6f5324412c0204b97100192550bd8246a03fe106d3a39c71b43a4a75","fc9e339097f83b642faf5109c93b07b67b568cd2efce3ca610f397abefaaa51c","d656a3978580c041f672c95ec1473d40577976110c3307a7b1286dee7b089bb8","13deac9e26254e51de2fb4e523f4b8d3db94f6f20dc700149643cc91a3731c28","04b1c11ddc799b68d586bab0b3bb6f8650eb64774f1d19452db94b6bb8953080","ca756edae2c530056197e5c531b5bb70dbe8c0d851850e45d772dc58e47c3ee1","d702e391156c4d2c4cb2d24ecadb4d446ea3f965bf46888c0f836aa9a071267e","02ec49fe75516a3163843dcc2bacbba6d374604de2ad7421567161373bc33df1"],"20000000","1701cdfb","690942e2",false]}
I (697090) create_jobs_task: New Work Dequeued 55c4e24
I (757102) stratum_api: rx: {"id":null,"method":"mining.notify","params":["55c613c","5a6663f8e38a22c68938ab4e40ac0655a0722a590000b6ae0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170306120e5075626c69632d506f6f6c","ffffffff02a15cc112000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9edbd95349f98c83762dc4bfa6d2c76b677a1b841f8f9c6bb7e7f439a3d76193b1d00000000",["f5aa0f84d5d8dce93fe0c7986e36ea037725e64046627ca271231487da77249b","434f4a881caf27fb9638242a71f2565ba8b4a10a718f02c5383ce0451c4ba3d4","784b0daacd70a09b6021e8299b4d5305462fdc6f79068a094a8002a6a49da2a0","4debbcc9656efa2a3422bd8d987a334650ab3e4d724f699c15105a4330472933","154c9a1adba7a95cdee7cb6664abd5774a463873bd13b4dec43dccf7ed4806cb","8ba437d972bded57d6b93b94db2040784c276337c04015af34b517ebe2d2238c","89dbfa8e83526c5ea27365d093f9d9ea71292a044b8e28d0b3b35006c125c397","98a7c37daf88cb7887447715fa260213944dae5d9d7a6ce6762f448b0026d50c","c3999d3694918198b52d4e88bd8487b8c6fe9baf70c214e94db3c76bc7df592f","5b51cc90b6301ab0a0051e7f8308c88b9f0766558cdcc5f2eeebe1dbb7833802","4d1b72e00c6beb69c4799a2e4d65afdadd35598a4bb2ffb602fda00e9633c518","ad0cebbce62ff134a936fb5a8e90d7dc9dbe080b3dd734b5992b53bb32f18ffc"],"20000000","1701cdfb","6909431e",false]}
I (757215) create_jobs_task: New Work Dequeued 55c613c
I (816958) stratum_api: rx: {"id":null,"method":"mining.notify","params":["55c745e","5a6663f8e38a22c68938ab4e40ac0655a0722a590000b6ae0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170306120e5075626c69632d506f6f6c","ffffffff0265d1c312000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9edfaed6b4a61284f78059b0e4e144fb2dc7e7746fd7bf52e74ac62332b2600000600000000",["f5aa0f84d5d8dce93fe0c7986e36ea037725e64046627ca271231487da77249b","434f4a881caf27fb9638242a71f2565ba8b4a10a718f02c5383ce0451c4ba3d4","784b0daacd70a09b6021e8299b4d5305462fdc6f79068a094a8002a6a49da2a0","288037b0aafdb46c3abde38e114f16084b25fea63ecb9884bcf4b40120927c7c","4e19569fa1bc0759927c1e61706d7bcec768f05b0e9fd3ae5a4d824ed16f841b","7db61b3c953184eb12c4fd81888c96a2455c88f3cf48e8831b2921be8bc3cb88","c5454ff0f0f73bf1153c89bdec49bee1fc337173418aab3ce6c47859354b5eda","592905f23b7e4d15dfb3c5a2458c88dbc991116a6779c9b98d8e21f1e01d8327","a9f42aced5ef5159b70a2362bd8ff817d163145dcdb1c63b756c3460156e7c6c","9d4f6cfd85d3907e17b583ee96c76267afc04e571dec218fa2778c7b9e34c1f9","c57a7e1af26ab18c7bd5742a7af47e1ae58ea916b237f30e9eb950f60273b1da","f986aaaa992b0086496e1d2a4569326f1a57811ea0ee94719b4ca09a0894810a"],"20000000","1701cdfb","6909435a",false]}
I (817135) create_jobs_task: New Work Dequeued 55c745e
```
and keeps giving this lines.....

Any setting you want me to set, tobetter troubleshoot?


### EricDimitri on 2025-11-04

IT happened again...:
```
[0;32mI (1102400) bm1370: Job ID: 78, Core: 22/15, Ver: 027DE000[0m
[0;32mI (1102401) asic_result: ID: 54e18ec, ver: 227DE000 Nonce 7FC7062C diff 696.1 of 16384.[0m
[0;32mI (1103769) bm1370: Job ID: 40, Core: 13/9, Ver: 00E32000[0m
[0;32mI (1103770) asic_result: ID: 54e18ec, ver: 20E32000 Nonce 9FD4061A diff 5851.1 of 16384.[0m
[0;32mI (1104683) bm1370: Job ID: 58, Core: 78/14, Ver: 05F1C000[0m
[0;32mI (1104684) asic_result: ID: 54e18ec, ver: 25F1C000 Nonce 0493049C diff 532.2 of 16384.[0m
[0;32mI (1105081) bm1370: Job ID: 70, Core: 104/5, Ver: 04B0A000[0m
[0;32mI (1105081) asic_result: ID: 54e18ec, ver: 24B0A000 Nonce C27204D0 diff 436.4 of 16384.[0m
[0;32mI (1105297) bm1370: Job ID: 08, Core: 1/9, Ver: 013B2000[0m
[0;32mI (1105298) asic_result: ID: 54e18ec, ver: 213B2000 Nonce F6A40602 diff 373.9 of 16384.[0m
[0;32mI (1148497) websocket: WebSocket client disconnected, fd: 42[0m
[0;32mI (1156271) stratum_api: rx: {"id":null,"method":"mining.notify","params":["54e2c12","4edd537fcf7c35b7b73bed71b603212ad36aab2e000051af0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170308120e5075626c69632d506f6f6c","ffffffff02d6c5c112000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9ed40c5d6f1ec945f0e57214a7cecc80b0db733795686b2b70c0b5beb0c606521ac00000000",["cc840a27f61f6e05b89d764217acbf97933ea88db31c63dea1b133f7b4eedd14","b3943afa5a58cfbcc636f223c5d068adb25c9f97184c5e09e18bd9a752e34cec","7077142179f5fd6829522c6bb34cab444fbcf750c3cb36f530aec96e883de23b","6b8f3f7f07cd5e3462572b36b7625d52aeb6899290ec1e483d88bb9315a8d370","30e59780d4853467d511ebf5e476697e415ed6c244b4dc0e56a9a48abdcd85d5","8a3225ce6d6b90b7bf58c4bed1e852f562d0cc7b1902013f6d42a389e91335fb","f14fe537aff8f4df01bcb1d5de7a0e4c90398f80507aaf7b6d2d1d26ffcc3639","506dbfd325e7b98a4e20a2483d3be2ac193618708fda3e43a17782cbcf2e086e","4fa59a8d1961f6b6df1b08d7162f9014c4801b08ca5599f8828e4574619385a1","969e75d9416ee677b893dcff39c0def53aa7c64dae515c8e9b56e98f6d845106","c9d5d6ce66f67b5ff0bc88641857a1c81044267a434b71009a6798d2074b1e57","5b246cb1fb61d3c0814266795fe5880577ecb9f0ed03228ae569b1aff827590b"],"20000000","1701cdfb","6909485d",false]}[0m
[0;32mI (1156393) create_jobs_task: New Work Dequeued 54e2c12[0m
[0;32mI (1217037) stratum_api: rx: {"id":null,"method":"mining.notify","params":["54e3f2f","4edd537fcf7c35b7b73bed71b603212ad36aab2e000051af0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170308120e5075626c69632d506f6f6c","ffffffff0238fcc312000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9ed083b7cbe2d0fad5726d0262c578d0f1fe12278a490c1ec3e042f1565eb22be5a00000000",["cc840a27f61f6e05b89d764217acbf97933ea88db31c63dea1b133f7b4eedd14","b3943afa5a58cfbcc636f223c5d068adb25c9f97184c5e09e18bd9a752e34cec","7077142179f5fd6829522c6bb34cab444fbcf750c3cb36f530aec96e883de23b","69fc28bccd97d9c0db4b4d4f0cecc8188b8e287e543952cb310d4eda6024cfde","71b52e43ef5878fd273da8648b6ecbe1506a5e90d5ac22276f383b9e2f4259ef","8fd5206773f8e9d2438f1d56cb0defd3492523a1f6cfbf6780666c0ce582404c","5dce217362be553263e76f3cae02a740d5d2376a5e6b81783a2d99f56a8e3d65","a2894ebd3c5e852fefb1f8704fa20305a1350ab725e16e161c1ce5b7deb6be1a","2093231577c8fcb0b6eb90ed774fb5c93bb7ef90e822fe11a07528cea29fda41","2307d385ad851c4dedd5a3568d7e5c3710151b9b44a919311aad418c42e7b81b","ba449aaf5f4a6bd8067a851d1fc823fdbfe04f6ec5855347a14f80dcd1e9bc22","282cf8dccc4e196fc32795ba1cd39e35c46c00aa2f47fd5d20b4aedde26fa527"],"20000000","1701cdfb","69094899",false]}[0m
[0;32mI (1217214) create_jobs_task: New Work Dequeued 54e3f2f[0m
[0;32mI (1276752) stratum_api: rx: {"id":null,"method":"mining.notify","params":["54e524c","4edd537fcf7c35b7b73bed71b603212ad36aab2e000051af0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170308120e5075626c69632d506f6f6c","ffffffff026716c612000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9ed8a4072c663f6b117ea1ba76c53615b7ae538a82e01d12b21028477378d2a295c00000000",["cc840a27f61f6e05b89d764217acbf97933ea88db31c63dea1b133f7b4eedd14","b3943afa5a58cfbcc636f223c5d068adb25c9f97184c5e09e18bd9a752e34cec","7077142179f5fd6829522c6bb34cab444fbcf750c3cb36f530aec96e883de23b","37d757e8bf9f50de928351815b2a603858307bbd0fdd68954a1c26caa330df3f","d90a32dd8431b4722c0a7275e163e68dac121dcbe1ecf03899bf972ea69031be","85d50798498365f87ed0c6f91eb5946141c93e48acb4ad777c29d7ce0e049add","b296cb242534950da94e0fea041693d5dbb32da8726eb856374e23998a6cc1de","fb18f26a881abf79fae972b9859322b94575a23f5fd815a79a20d3ffc8d5a241","2b456c324b3cb18c8fde1fddfa2c12a6a81fa9ac647cfa2401496bc74f105b6e","b718be1144091b0c71ebaa2b78660bd746bcd5cf2a27e984262fc5e5250fb9e9","6efdcba54c8c7b5e7855afef94e415ded227010043d4f8069a543bc4eeaa92bb","aa5047b6d61d2c2a4f99cc7d5f99a309d4b8f9fb508760bfd7eb65bb7c85b465"],"20000000","1701cdfb","690948d5",false]}[0m
[0;32mI (1276935) create_jobs_task: New Work Dequeued 54e524c[0m
[0;32mI (1336986) stratum_api: rx: {"id":null,"method":"mining.notify","params":["54e6567","4edd537fcf7c35b7b73bed71b603212ad36aab2e000051af0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170308120e5075626c69632d506f6f6c","ffffffff02aff7c812000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9ed266a2046e33057be62424289fa73cd78a47ac4c2b2a597939f13e21aec3dfe6300000000",["cc840a27f61f6e05b89d764217acbf97933ea88db31c63dea1b133f7b4eedd14","b3943afa5a58cfbcc636f223c5d068adb25c9f97184c5e09e18bd9a752e34cec","604f5633b269ffcf776ba04a2159e3b26862086b9c5229d6e5392c1b0e53ad98","edc2f70f484d17657ac2779562e448fa7b9d3e82a8e0e4d8d1f04668c1ef4d77","2b7d5e505caf04752034fe80f86f06f7d9c756689fcdbe974d0fd2419294ddec","94b005131e5649b27af2e4e90bdc560c6b0c9a54fc5a9d8d63b54d749bf95bcf","046d8c04aa8e2b8901f3491b9e6c5944df47e5162357a912f6f20b3842a0fcf4","b2b52dc7881cde9089e4a1e04c69677275ffc7ebb480640dee2d7707ee08c45e","3f3501996fc81f684c320118a0a7cd279a0b0efff89865ef06959d89657cd697","763840e86f133fb2df98b0c62087e64caa3a72340086cece84406f7e1538415d","b980c4a19154cc5d90ee2d37f969924b2446f8541f43214ebfe97afc9ab0d555","1da85c1dd487aa0ab1fdba485532fd82dded70515dce21687dbb26c5a3ecf212"],"20000000","1701cdfb","69094911",false]}[0m
[0;32mI (1337155) create_jobs_task: New Work Dequeued 54e6567[0m
```

### mutatrum on 2025-11-04

I put the logs between backticks (` ``` `) for readability. 

### skot on 2025-11-04

> ### UPDATE
> 
> [@skot](https://github.com/skot)
> 
> Ok, here is the log... IT was ok, like this:
> 
> ```
> �[0;32mI (21799533) bm1370: Job ID: 70, Core: 116/14, Ver: 0617C000�[0m
> �[0;32mI (21799534) asic_result: ID: 546f6d5, ver: 2617C000 Nonce 9BAD04E8 diff 829.2 of 8192.�[0m
> �[0;32mI (21799624) bm1370: Job ID: 08, Core: 112/14, Ver: 0119C000�[0m
> �[0;32mI (21799625) asic_result: ID: 546f6d5, ver: 2119C000 Nonce 0B0504E0 diff 293.5 of 8192.�[0m
> �[0;32mI (21799983) bm1370: Job ID: 08, Core: 74/4, Ver: 05788000�[0m
> �[0;32mI (21799983) asic_result: ID: 546f6d5, ver: 25788000 Nonce 1EF20494 diff 672.3 of 8192.�[0m
> �[0;32mI (21800574) bm1370: Job ID: 38, Core: 49/11, Ver: 007B6000�[0m
> �[0;32mI (21800575) asic_result: ID: 546f6d5, ver: 207B6000 Nonce B5BA0462 diff 773.3 of 8192.�[0m
> �[0;32mI (21800798) bm1370: Job ID: 38, Core: 98/8, Ver: 03370000�[0m
> �[0;32mI (21800799) asic_result: ID: 546f6d5, ver: 23370000 Nonce C14D06C4 diff 1472.4 of 8192.�[0m
> �[0;32mI (21801485) bm1370: Job ID: 50, Core: 126/9, Ver: 05812000�[0m
> �[0;32mI (21801485) asic_result: ID: 546f6d5, ver: 25812000 Nonce 927000FC diff 1223.7 of 8192.�[0m
> �[0;32mI (21801500) bm1370: Job ID: 50, Core: 7/11, Ver: 05AF6000�[0m
> �[0;32mI (21801500) asic_result: ID: 546f6d5, ver: 25AF6000 Nonce 01E9030E diff 338.3 of 8192.�[0m
> �[0;32mI (21802092) bm1370: Job ID: 00, Core: 78/7, Ver: 00B4E000�[0m
> �[0;32mI (21802093) asic_result: ID: 546f6d5, ver: 20B4E000 Nonce 3FA7029C diff 260.0 of 8192.�[0m
> �[0;32mI (21804255) bm1370: Job ID: 60, Core: 49/4, Ver: 02B28000�[0m
> �[0;32mI (21804256) asic_result: ID: 546f6d5, ver: 22B28000 Nonce 56340262 diff 957.4 of 8192.�[0m
> �[0;32mI (21804573) bm1370: Job ID: 78, Core: 39/7, Ver: 0078E000�[0m
> �[0;32mI (21804574) asic_result: ID: 546f6d5, ver: 2078E000 Nonce 5EFC044E diff 397.0 of 8192.�[0m
> �[0;32mI (21807730) bm1370: Job ID: 08, Core: 18/4, Ver: 02648000�[0m
> �[0;32mI (21807731) asic_result: ID: 546f6d5, ver: 22648000 Nonce 85DB0124 diff 663.5 of 8192.�[0m
> �[0;32mI (21808037) bm1370: Job ID: 20, Core: 77/10, Ver: 00094000�[0m
> �[0;32mI (21808038) asic_result: ID: 546f6d5, ver: 20094000 Nonce 1BFA049A diff 273.5 of 8192.�[0m
> �[0;32mI (21808697) bm1370: Job ID: 38, Core: 115/8, Ver: 01FB0000�[0m
> �[0;32mI (21808697) asic_result: ID: 546f6d5, ver: 21FB0000 Nonce 47BC03E6 diff 476.7 of 8192.�[0m
> �[0;32mI (21809331) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> ```
> 
> Then it started to repeat de diff, Job Id, Core Ver:
> 
> ```
> �[0;32mI (21808697) asic_result: ID: 546f6d5, ver: 21FB0000 Nonce 47BC03E6 diff 476.7 of 8192.�[0m
> �[0;32mI (21809331) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21809332) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> �[0;32mI (21809378) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21809379) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> �[0;32mI (21809426) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21809426) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> �[0;32mI (21809473) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21809474) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> �[0;32mI (21809520) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21809521) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> �[0;32mI (21809568) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21809568) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> �[0;32mI (21809615) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21809616) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> �[0;32mI (21809662) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21809663) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> �[0;32mI (21809709) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21809710) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> �[0;32mI (21809757) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21809758) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> �[0;32mI (21809804) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21809805) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> �[0;32mI (21809851) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21809852) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> �[0;32mI (21809899) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21809899) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> �[0;32mI (21809946) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21809947) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> �[0;32mI (21809993) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21809994) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> ```
> 
> and then this:
> 
> ```
> [0;32mI (21816852) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21816853) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> �[0;32mI (21816899) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21816900) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> �[0;32mI (21816946) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21816947) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> �[0;32mI (21816994) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21816995) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 257.5 of 8192.�[0m
> �[0;32mI (21817041) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21817042) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.�[0m
> �[0;32mI (21817088) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21817089) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.�[0m
> �[0;32mI (21817136) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21817136) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.�[0m
> �[0;32mI (21817183) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21817184) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.�[0m
> �[0;32mI (21817230) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21817231) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.�[0m
> �[0;32mI (21817278) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21817278) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.�[0m
> �[0;32mI (21817325) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21817326) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.�[0m
> �[0;32mI (21817372) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21817373) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.�[0m
> �[0;32mI (21817419) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21817420) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.�[0m
> �[0;32mI (21817467) bm1370: Job ID: 50, Core: 30/13, Ver: 0393A000�[0m
> �[0;32mI (21817468) asic_result: ID: 546f6d5, ver: 2393A000 Nonce B5F72E3C diff 0.0 of 8192.�[0m
> ```
> 
> Diff went to 0
> 
> And stays like that forever, until you restart it.
> 
> Any thoughts?
> 
> Eric

This one is really interesting; I don't think we've seen this failure mode before, where the ASIC is just sending back duplicate nonces. My guess would be that either this is a faulty ASIC chip, or that some power disruption "crashed" it. If you can get this one to happen again it would be interesting to see a screenshot of your AxeOS dashboard showing the voltage.

### EricDimitri on 2025-11-04

Moree.......

```
I (4595009) bm1370: Job ID: 48, Core: 10/11, Ver: 00716000
I (4595010) asic_result: ID: 5b3b995, ver: 20716000 Nonce C2BD0014 diff 873.3 of 8192.
I (4595303) bm1370: Job ID: 48, Core: 56/5, Ver: 0406A000
I (4595304) asic_result: ID: 5b3b995, ver: 2406A000 Nonce FC350570 diff 1376.0 of 8192.
I (4596828) bm1370: Job ID: 10, Core: 8/1, Ver: 04522000
I (4596828) asic_result: ID: 5b3b995, ver: 24522000 Nonce 663C0610 diff 288.8 of 8192.
I (4597213) bm1370: Job ID: 28, Core: 12/2, Ver: 02EE4000
I (4597214) asic_result: ID: 5b3b995, ver: 22EE4000 Nonce 397F0118 diff 2218.3 of 8192.
I (4612587) stratum_api: rx: {"id":null,"method":"mining.notify","params":["5b3cd16","243354e92741d6fe465ba7c4085b6439fe8b01d20001b5130000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170370120e5075626c69632d506f6f6c","ffffffff02354bc512000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9ed2af934f773b6f7657738cf71275685b6f7253078c625d6d60b539ea69b89a34300000000",["ba438fd505792b38b7fbb9dff1c75ac0bbd41dd280a6e720c9d199455d2aadda","694887f100ff8c2ff2b7209851e509e702b64a864a0ea30c6113d163e0c72a54","00bcfec725cb1527bf1d2bc37edf839518d15804583c30bb93e5e35101769976","eb01a609c4069968e644652f05f8f5cc26be474a7bdd36129ee5da04f17c8d5a","0db7a8a46e368716db2211001d3f4503f9e4857dba50c6df86e891970eb4469c","cd4cfdaf135c519f4d6de89b11c52a04f35107ce0896c35315ffc0d5c32737b4","0ce01fa0d4c21d8501feca36eb348ad879444ab5d78c27e9dc2a13d8f834a778","17a3b440ecd6c16fa25a027beb63ee13a1d99cda2beb2c10e61129a036663b83","1f74e1dcaae3e56f85cc19db1ea890ea6df9b72cf1e42840f36babe3ebdec6ba","665dbf9cfcef125e4aedd6932de1abc0105b6f029ad7aad5ae2d5e026ee08525","28e9e5c21be1aa55ed537f2604ea02b8115ef63facd4c96e0167e340e1548dc9","329e2f4abcea0262a12a3ad159a186f73dac9323644dd00c0dc7c8f41ba494f5"],"20000000","1701cdfb","690a4612",true]}
I (4612691) stratum_task: Clean Jobs: clearing queue
I (4612788) create_jobs_task: New Work Dequeued 5b3cd16
I (4620853) websocket: WebSocket client disconnected, fd: 42
I (4620875) websocket: WebSocket client disconnected, fd: 43
I (4627701) websocket: WebSocket client disconnected, fd: 42
I (4630809) websocket: WebSocket client disconnected, fd: 42
I (4636729) websocket: WebSocket client disconnected, fd: 42
I (4674736) stratum_api: rx: {"id":null,"method":"mining.notify","params":["5b3e089","243354e92741d6fe465ba7c4085b6439fe8b01d20001b5130000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170370120e5075626c69632d506f6f6c","ffffffff021aaac912000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9ed61d98a9a9a7b86ab8021c929febbaf62356f2b38930a96947ced872ab3a7243f00000000",["ba438fd505792b38b7fbb9dff1c75ac0bbd41dd280a6e720c9d199455d2aadda","64a4a8b2c9acaa6ca81732068dca71c188ab2c64979e4e9d5510e19578ae6ecd","132d5504b74175454e17b08f80c243c541ac61708f116d116abb9e2eb6175775","2c31cc3fdd17eae1e5262ae466f25f7626031569640b1cfa24fa5a40cacc2a4e","84d9218ba640b7ee9ac940ea73f592ba4c35baf57607f90b55f8bde4d9f06ff3","37b1cdf84ed0165f212e2485eee7416d8eb3ff0de71411b96001c4e7818505da","7276cad16c910c2839505fd2c0f2ca5132a44e4f03800485919f8e8c93adcad6","a50b1f27bc76ef4852cf9db8e7ad484e4aba4a9ce2168b8ffb9978602d5b5f2e","42d56dac664f7a9541c4c4f812b4e9d1353ab3107207af40997f66780af789d1","343efc93487104736eced984a9fdced9a75b2149426b754f0f5cfb858ee33944","373bb63568d569909e095295e78ad74f8f054d3c09d3a0b3e3d976d0607808db","d786476f2be8144c21825daec77de48590ead78620bc248d419475e161c9c097"],"20000000","1701cdfb","690a4650",false]}
I (4674928) create_jobs_task: New Work Dequeued 5b3e089
I (4722904) stratum_api: rx: {"id":null,"method":"mining.notify","params":["5b3f3ed","3e6d1be16f19b83809e6e2d8d8ed8d18bf356ee50000ee380000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170371120e5075626c69632d506f6f6c","ffffffff023d2ab412000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9eda244d6da65233905712498d01bf6e6b19bda36aa861ba7167423fa2441fa182700000000",["d6945e7700fafe2b0313bddb94ff90d40796de807d1b11239c02cad0c814a982","8b6a10ca84915d3ae179b24f2e7ebc96f1b40847074041d502128982c986420f","5f3b488f60f5385d6b48f500b907eb738f495e2420759f6e0d2777bfabf91120","4571f1f76159b26f61d1462ddf4a276c6f221d04fcc939b2211ad098aa05379b","2a3b75a9f4cf491b1d8c0603949a4e2b8947e40ba6117d55940450e5dc04ab67","181a7e51e167707a3680557f6a09f75ffcadff7102f55f33f81eb7c72d22529e","7094c44a261830b8057936f8f57dcdcae82c87df83f314d289cdd536d4bcf0cf","1d12e0d96aef3f48dd2bf2b3c63a870ac26377262d794c599400f9cb86b8f73a","a73019dce97794a54ad6b12e6580f1521bcebffb46c3ef6bf8ec2e9e2ef9b86a","90d6ecee53b7bcfe5f898056cd22c93c0d77fb605f1cfb05d2198b863588442c","15d6a293f2758bd8aaf2bb446b33918f613dc4741cb538d17a5a320402f78a3b"],"20000000","1701cdfb","690a4681",true]}
I (4723002) stratum_task: Clean Jobs: clearing queue
I (4723026) create_jobs_task: New Work Dequeued 5b3f3ed
I (4776048) websocket: WebSocket client disconnected, fd: 42
I (4776083) websocket: WebSocket client disconnected, fd: 43
I (4784289) stratum_api: rx: {"id":null,"method":"mining.notify","params":["5b40763","3e6d1be16f19b83809e6e2d8d8ed8d18bf356ee50000ee380000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170371120e5075626c69632d506f6f6c","ffffffff027aa0be12000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9ed190f7d5afcde2afbf9feaf35c4b97daf5f276e9c0d8e331410194ef7f9a641cf00000000",["df394abd97231a82547938cc87fc807b775f8fb701627166dd7b2719801ef92f","fb14c87407689138bd63985687510f57c275452432bd2bf8d665961b440df65f","1c0786c94ed280e8617179c045b75355757b9c6fae3d085561bc373dd3752a32","cb6ccb35c25f30d0dba2d2c9ec38caca82991f306d43b0337c254ea026d78d01","d7b4275a1d86ba535c2d486cfb6afab448b1d587926b617984f539bc2776d90f","ac7de842b67037488bc64c3c19e10f59bba94c8a48d011b352449a52cd20a252","fe10e51d513dc20cc70e89bb2656cc326f2e42fd9891735029bfe009b5b81933","a44fef50fea3f08b95063f9cb88da602d7aba2e07124a5ae7367a2b7b63a2041","9c93bdf0978b289dcb6e47cfc20892b4ff644d4db9fdbac882142cbad65f8ad1","8f78b09e21479b8633c6d4b1af63cf63f08260b648064aab67e396a59c34e85c","d43bbb1c95abeeedb5472eddb64b5a077d87ff0f98fc7c49765365a694d3d233","7504b6badb755eb8cd1754574d7923b9a611d02044924e97b78ea4537a5c4275"],"20000000","1701cdfb","690a46be",false]}
I (4784462) create_jobs_task: New Work Dequeued 5b40763
I (4844710) stratum_api: rx: {"id":null,"method":"mining.notify","params":["5b41aef","3e6d1be16f19b83809e6e2d8d8ed8d18bf356ee50000ee380000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170371120e5075626c69632d506f6f6c","ffffffff02cbb3c312000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9ed95bf1a173b5bc94ed50be33ba1811af59680487046ce58618fd4d6262909c7ab00000000",["df394abd97231a82547938cc87fc807b775f8fb701627166dd7b2719801ef92f","fb14c87407689138bd63985687510f57c275452432bd2bf8d665961b440df65f","2df8972813539e6f9981d3795300f130f6cc1b9e5589e78f43c2dd26a42eb1ff","5139780d0bedd6b659648604e4daca218924d1048dcf6f4a01790e884781f15d","f391518719c0ef5180f25b9b655b350baf1f8c2e65b1e9486e3ad473f1124e2e","1c94afe6e3a37175165d08536110749a54ef8c5e8d0456e224cbf559956e0c71","05da4e0dfe451fb7375d186a854e31c870417401a1a2163343e41844e0bc505d","49d78216f769fea114cdd073aa125432e84670ad6ef39ddc94df8dc16a57fe93","c27d7c2f705eba50364890988a73ba0ce30c6282b59379a6b7b87a657d038b45","5ea8166ccac5cd2c6fb78e7627cc12ae93b5f934e56831da9a948228f5cce232","528b649a5aa3d206ed33da0bfb12f9c0d963a4b85c1c66f1e2fa0e7dd0b87f39","bbf2ee81d5ba35c799fd20a4062faae8dd904dffd5025e311b5812c2ff4eebf4"],"20000000","1701cdfb","690a46fa",false]}
I (4844885) create_jobs_task: New Work Dequeued 5b41aef
I (4904398) stratum_api: rx: {"id":null,"method":"mining.notify","params":["5b42e7a","3e6d1be16f19b83809e6e2d8d8ed8d18bf356ee50000ee380000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170371120e5075626c69632d506f6f6c","ffffffff02c9cece12000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9eddcda7392a14ed6566eecf65e960808ffb973c7436741646a4d92e1ad9552108700000000",["6fa969c264b5c73c10805569efddd4e3888d3214ad89964c7bc6649e729bbf59","62206334ad5eb78b17149d55ec9f664619ed203f89a4bccbc91342d4fd578eb9","8a9b2e6a43b1d39099d4a746b42078dc650bed94b5ff8f447c7a33c0348491aa","6ee946172dbe6662cf57a1d7841c61af70d107a6459c61bf510f7bda36fdd3b1","871c3507ebe3d51b8e8091b3336fc52cbf95c5d1df7ef3bf866cd6e05ce85e48","581c3d6637b4bc1f74178ac4bec19d6ccda4261105a8ca337e468b7eec5092a3","3a3c490b71769d9164a381a0b7924fceecd79013c89e7578b9bd1a3bdaf142dc","6effc0581fd4ba51da493248bff7a4a5802a33c284db8cf43cf6f976d7b956bb","bea47dd89aa79b1db5d60b43f9e4e7eae5ffb7dc8f1a44489ea25bfc3ee33c67","0104fcddde0ba6f9ae1ad7afce59b042f861c4e7c6b3eec62a20cabda39aa92c","39c52a767f692a1741b43c22dadc7035946bf58e2c18457819b4b942ffa81b52","15acd5e4a678afdf96022c00b6f906fc7f6b42f06b9bf947f81f20a4afa5dfa0"],"20000000","1701cdfb","690a4736",false]}
I (4904505) create_jobs_task: New Work Dequeued 5b42e7a
```

<img width="725" height="800" alt="Image" src="https://github.com/user-attachments/assets/3a44f616-0e13-4f85-817b-c3480d5b75dc" />



### EricDimitri on 2025-11-04

Again...

```
I (2206853) bm1370: Job ID: 00, Core: 32/0, Ver: 01640000
I (2206853) asic_result: ID: 5c0feea, ver: 21640000 Nonce D7360440 diff 273.6 of 8192.
I (2207050) bm1370: Job ID: 00, Core: 72/0, Ver: 03CC0000
I (2207051) asic_result: ID: 5c0feea, ver: 23CC0000 Nonce 24F80590 diff 423.0 of 8192.
I (2208667) bm1370: Job ID: 48, Core: 104/6, Ver: 053CC000
I (2208668) asic_result: ID: 5c0feea, ver: 253CC000 Nonce 695505D0 diff 1837.2 of 8192.
I (2210753) bm1370: Job ID: 40, Core: 81/4, Ver: 002C8000
I (2210754) asic_result: ID: 5c0feea, ver: 202C8000 Nonce F47A03A2 diff 330.1 of 8192.
I (2210767) bm1370: Job ID: 40, Core: 46/12, Ver: 005B8000
I (2210768) asic_result: ID: 5c0feea, ver: 205B8000 Nonce B410005C diff 383.5 of 8192.
I (2213486) bm1370: Job ID: 38, Core: 41/9, Ver: 03052000
I (2213486) asic_result: ID: 5c0feea, ver: 23052000 Nonce CFEA0252 diff 648.4 of 8192.
I (2214259) bm1370: Job ID: 68, Core: 5/7, Ver: 0040E000
I (2214260) asic_result: ID: 5c0feea, ver: 2040E000 Nonce 5455000A diff 699.7 of 8192.
I (2243176) stratum_api: rx: {"id":null,"method":"mining.notify","params":["5c11190","fa862fb036c46e38292c7a94f85503922a26582d0000dc1e0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170374120e5075626c69632d506f6f6c","ffffffff02eb0fdf12000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9edf9e77529a510568e0711287f1fbc06b723e9d7992650d8e7d02d9c2a36789f9400000000",["6f7043510715a4adb585c1d5c366cfc23dea04c706d3a106371f231c9e59b0f5","21bc7c3a2c58dff1458a1bbeebb2185c27fc7e9ec8b6375457fef1cad0ea51aa","95cc060d9b4e25b19d35fd3463f2419b0305d5d2254c6f0eda28d2681c21623a","5bc095dca4c1edda1fbc4dcd3477293786668f21e3e804024643e5774ab26149","d6ac0dc3563b93a8881402afbeb0588e6b7e6de274c0e91a7f748c0cc94e0951","fc12c71bfeeb4cc88a28b922b3646d756768b6e6b8386117bf8b83bcb81e0f61","1e95cf271f381d8a06c1e307fd3caec044cdce5435d42347818d0bd135897843","ea0a738f755104511acec2a72bd878db07b78ebb6b20504190f3e8d59ef0d32a","b031db461050cc886c8b5c6d6d95f67a3a2dfae6d1f5a16759cd354ce8c30b4f","70c084b48b4519a73bf501ccd7b44e304fe3b0eb97ffe7a93fc1b50ee81243d3","2416af3908b1eed9a44ce0fe96006cfcd23bb4729d57d1d90f223f874d51a940","10b8675bcfec499037788274f06e26911db1c933ae28764225bb46093cdc237f"],"20000000","1701cdfb","690a5073",false]}
I (2243328) create_jobs_task: New Work Dequeued 5c11190
I (2300575) stratum_api: rx: {"id":null,"method":"mining.notify","params":["5c12421","fa862fb036c46e38292c7a94f85503922a26582d0000dc1e0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170374120e5075626c69632d506f6f6c","ffffffff0264b2e312000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9ed31208c5105700ae5785ebf12845be640a00bdf236be059d71d55434e1dc905df00000000",["1d7b9b0851d929158ddfd1b83831c3c85c74e10ed07e27829751156082a2893d","b729137c0d63f7e338a7610146024d82fe14296827c65f5e5a81723186c9b0ec","0369f9e192a904eaab2f0141bd8cee9fe869ed5e6ee9d24c2ce348d2d3e01d49","1d23db2948a536723de642bcf23e33f4b5e4019a845f92e9e84ffab08b712c4f","bdc49c09c1f22f391800203f83f8c741e4aba50fad742e3283b7c71ac36fd40f","012af783e77d8569acfb84f6752bf041e98a0eabde33ca8e848aaafbdc45a698","9fb6728fc4642b739d05a9601159263167658a3e391180887234297873f03fda","60a26351252001085dfcb3e0c6ca896cace42d171f02a41e2a00f5095f5171c2","2d0f44affa9bbbceb73ed1f7c48c0e77cc66977a5fb24c82392b0deb2fecfaa7","99e3471d53721d010ebf2ca9d2570cc3bccddc01b4e6e2ea9ed278311d046640","62cc8c5936d61e0e21491b03edcf2787d588df5111f10e15384a2f545879a2f4","d004071c11da5243ad9d468aa57a96156c7010598eb642d25e8c9f70e2cdd8c0"],"20000000","1701cdfb","690a50af",false]}
I (2300743) create_jobs_task: New Work Dequeued 5c12421
I (2362204) stratum_api: rx: {"id":null,"method":"mining.notify","params":["5c136b0","fa862fb036c46e38292c7a94f85503922a26582d0000dc1e0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170374120e5075626c69632d506f6f6c","ffffffff02080ee612000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9ed21b99f1645a9f754209285adda1259babd91b55da94b886009148c11da3f1e8400000000",["1d7b9b0851d929158ddfd1b83831c3c85c74e10ed07e27829751156082a2893d","b729137c0d63f7e338a7610146024d82fe14296827c65f5e5a81723186c9b0ec","0369f9e192a904eaab2f0141bd8cee9fe869ed5e6ee9d24c2ce348d2d3e01d49","1d23db2948a536723de642bcf23e33f4b5e4019a845f92e9e84ffab08b712c4f","bdc49c09c1f22f391800203f83f8c741e4aba50fad742e3283b7c71ac36fd40f","871a203d330130c24f67906796f8cc46c01451dc31b6833d1e1d18d26bc178dd","18da92de2719690da882b6a075604ec0e07219951eb53d0a3930bdd3df64b0a4","deb1210e87010e896b8d6a0114063b837cacf4e021180d52ca411d8615763b88","7667a55e9fc3743cb793912a8f4cf34f12cce61dbdbc6bc8d80212652cca7acb","6777c0f2f37f909ca8d9d5fd5900fe8c2a016226e402169e4439360d3d1345e7","aa59b4fa7f3433d73cc35de0dcb05a633ca5583300bb415f8dd2d543c66dad85","8ad96c3e3f22c20f9dba92bb254ddf7d56f5ef79624a1ddca2202540c85b359d"],"20000000","1701cdfb","690a50ec",false]}
I (2362367) create_jobs_task: New Work Dequeued 5c136b0
I (2421604) stratum_api: rx: {"id":null,"method":"mining.notify","params":["5c1493f","fa862fb036c46e38292c7a94f85503922a26582d0000dc1e0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170374120e5075626c69632d506f6f6c","ffffffff024323e812000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9ed9590ecc8dedf1cbf92db15ca465a5a134cc60ff83a72233431ad421dd59f087a00000000",["1d7b9b0851d929158ddfd1b83831c3c85c74e10ed07e27829751156082a2893d","b729137c0d63f7e338a7610146024d82fe14296827c65f5e5a81723186c9b0ec","0369f9e192a904eaab2f0141bd8cee9fe869ed5e6ee9d24c2ce348d2d3e01d49","1d23db2948a536723de642bcf23e33f4b5e4019a845f92e9e84ffab08b712c4f","911511d176e9aaa93405f2e44a325ad34337c4db40f0fee835855e46b29c9a03","5439e0be7ac1580b909e19961eb07d5f4653f114a6b3d38a23ee2c5fab91f4c0","df3b3bc476330a91dcde3460537e5bd60505cb1f2b6e73dabb9d8c0ebb6ed31f","8a80359b24c98c66bc06028ca979ac8bb59a9b6de8ef9ce3f954f334253c9c1b","536ee1ccba9d419fd5fe9b76facdc8e943a43b9731726fb42e4d3573fb2c8eb3","d2801b7604a119cf9ea2555d66c5f8dfa5b95791b5ac0adcb200f08e6ae62d11","598bc1d1b2c8a31aa4a74793508b8cfd68f74860f45a14a9989bc9b099bfaeb2","e694074444f9b61a7102ace851669b093434676559db3aea2a369a379db17754","1c136fa02cb929c82e9dfd48f894b0050dcfa4fb7f74116b7530cfa70361b865"],"20000000","1701cdfb","690a5128",false]}
I (2421789) create_jobs_task: New Work Dequeued 5c1493f
I (2480879) stratum_api: rx: {"id":null,"method":"mining.notify","params":["5c15bdd","fa862fb036c46e38292c7a94f85503922a26582d0000dc1e0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170374120e5075626c69632d506f6f6c","ffffffff020519ea12000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9ed45775f8d5ffe1b6cd7694a7e0a67cd630f275aff717b7052a9ae7cb314b54a4e00000000",["1d7b9b0851d929158ddfd1b83831c3c85c74e10ed07e27829751156082a2893d","b729137c0d63f7e338a7610146024d82fe14296827c65f5e5a81723186c9b0ec","0369f9e192a904eaab2f0141bd8cee9fe869ed5e6ee9d24c2ce348d2d3e01d49","1d23db2948a536723de642bcf23e33f4b5e4019a845f92e9e84ffab08b712c4f","f7a04018baa54d24163be0df4e782645e0d2c032df368bb02add7217c85a3472","3360167d88ce9fc2d24fbdba5873724049f3c66cc66070cc9bbf5557115947e9","e15db9908f95ace8222974d12bc241260013d507f86c592898467118e7af05e2","996fe56f548a6f9d2930773d17936515068efc683dbabfa76c5126d1ef7bdf5d","e097afab270f43740cecbf9fda6c7b0f3abbdb4cd5f012398054de1183142673","57d146166110e39c02465dc07450aa399b96dffe0a68b62b38ddaf1aa897448d","04c9501751b9990ae7caf61583b752dc2472c7913ef1571a1aa66d2a261b2563","50a56545e3398a66e3d35a7f0a2d691b24bc7b7f72dc55a1c6226a3914fcd6d5","4b336073b8cb9fdc78f7c11d6dc6e4dfb22c1a6e5cd895353c25ace1dc828880"],"20000000","1701cdfb","690a5164",false]}
I (2481009) create_jobs_task: New Work Dequeued 5c15bdd
I (2514589) websocket: WebSocket client disconnected, fd: 42
I (2514610) websocket: WebSocket client disconnected, fd: 43
I (2519773) websocket: WebSocket client disconnected, fd: 42
I (2540890) stratum_api: rx: {"id":null,"method":"mining.notify","params":["5c16e96","fa862fb036c46e38292c7a94f85503922a26582d0000dc1e0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170374120e5075626c69632d506f6f6c","ffffffff02bd05ed12000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9edc94608a0b207ed59f3f792c6d5df57ed7f60e2fd468f9f86f3c8261ca3d7f44600000000",["1d7b9b0851d929158ddfd1b83831c3c85c74e10ed07e27829751156082a2893d","82211af44abdf8678dcd5c7502565113d984d2deb21687a6b6dd85429baecefc","c36a1134393d0b7692536a247077a81704005bfa633615bb3f8d8ff68696db3c","639f1f168d686eab52ea9c9adeefbefd76ecef121139aee363a24a63fbf6a5e3","260c48eeea54b24a4610da626a40a6aaa67352fac4dfb3819b5725d1033d609d","3b007413b003a5f25136fb91186ef78d40d8e06b92d799fcb330f9e1becfdd43","e923e34d1fb8716c7751b5b25311028304b9a71898ce3dbf92ef80d83278aa68","4f76e3ff64fd52264d222e370d8fe976c1cb7b74a6c34f5542b33478224f5710","003d8897d9dd594fc0c1540a460e1fc67cec939bffddd4db3d53cdbaa3269ee1","8da5fa2713964203afb009f64b334fc95a2ef26be97b8838dccdf5c94a9251ba","5826482197fffc920a56dc3150f5020e8bf10d8206dc9964193896f7e098c219","870361340ba225dfcccc3a6ca8719c3bc1139fdccceed4588e62e47dc57c0e22","334cd6974e228433d532e536ea22ba2e9b13100267250e170fb6d58491b1c221"],"20000000","1701cdfb","690a51a0",false]}
I (2541032) create_jobs_task: New Work Dequeued 5c16e96
```

<img width="709" height="821" alt="Image" src="https://github.com/user-attachments/assets/88678938-a3eb-42ea-8a3c-dc6d6768d4fe" />


### skot on 2025-11-04

> Again...
> 
> ```
> I (2206853) bm1370: Job ID: 00, Core: 32/0, Ver: 01640000
> I (2206853) asic_result: ID: 5c0feea, ver: 21640000 Nonce D7360440 diff 273.6 of 8192.
> I (2207050) bm1370: Job ID: 00, Core: 72/0, Ver: 03CC0000
> I (2207051) asic_result: ID: 5c0feea, ver: 23CC0000 Nonce 24F80590 diff 423.0 of 8192.
> I (2208667) bm1370: Job ID: 48, Core: 104/6, Ver: 053CC000
> I (2208668) asic_result: ID: 5c0feea, ver: 253CC000 Nonce 695505D0 diff 1837.2 of 8192.
> I (2210753) bm1370: Job ID: 40, Core: 81/4, Ver: 002C8000
> I (2210754) asic_result: ID: 5c0feea, ver: 202C8000 Nonce F47A03A2 diff 330.1 of 8192.
> I (2210767) bm1370: Job ID: 40, Core: 46/12, Ver: 005B8000
> I (2210768) asic_result: ID: 5c0feea, ver: 205B8000 Nonce B410005C diff 383.5 of 8192.
> I (2213486) bm1370: Job ID: 38, Core: 41/9, Ver: 03052000
> I (2213486) asic_result: ID: 5c0feea, ver: 23052000 Nonce CFEA0252 diff 648.4 of 8192.
> I (2214259) bm1370: Job ID: 68, Core: 5/7, Ver: 0040E000
> I (2214260) asic_result: ID: 5c0feea, ver: 2040E000 Nonce 5455000A diff 699.7 of 8192.
> I (2243176) stratum_api: rx: {"id":null,"method":"mining.notify","params":["5c11190","fa862fb036c46e38292c7a94f85503922a26582d0000dc1e0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170374120e5075626c69632d506f6f6c","ffffffff02eb0fdf12000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9edf9e77529a510568e0711287f1fbc06b723e9d7992650d8e7d02d9c2a36789f9400000000",["6f7043510715a4adb585c1d5c366cfc23dea04c706d3a106371f231c9e59b0f5","21bc7c3a2c58dff1458a1bbeebb2185c27fc7e9ec8b6375457fef1cad0ea51aa","95cc060d9b4e25b19d35fd3463f2419b0305d5d2254c6f0eda28d2681c21623a","5bc095dca4c1edda1fbc4dcd3477293786668f21e3e804024643e5774ab26149","d6ac0dc3563b93a8881402afbeb0588e6b7e6de274c0e91a7f748c0cc94e0951","fc12c71bfeeb4cc88a28b922b3646d756768b6e6b8386117bf8b83bcb81e0f61","1e95cf271f381d8a06c1e307fd3caec044cdce5435d42347818d0bd135897843","ea0a738f755104511acec2a72bd878db07b78ebb6b20504190f3e8d59ef0d32a","b031db461050cc886c8b5c6d6d95f67a3a2dfae6d1f5a16759cd354ce8c30b4f","70c084b48b4519a73bf501ccd7b44e304fe3b0eb97ffe7a93fc1b50ee81243d3","2416af3908b1eed9a44ce0fe96006cfcd23bb4729d57d1d90f223f874d51a940","10b8675bcfec499037788274f06e26911db1c933ae28764225bb46093cdc237f"],"20000000","1701cdfb","690a5073",false]}
> I (2243328) create_jobs_task: New Work Dequeued 5c11190
> I (2300575) stratum_api: rx: {"id":null,"method":"mining.notify","params":["5c12421","fa862fb036c46e38292c7a94f85503922a26582d0000dc1e0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170374120e5075626c69632d506f6f6c","ffffffff0264b2e312000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9ed31208c5105700ae5785ebf12845be640a00bdf236be059d71d55434e1dc905df00000000",["1d7b9b0851d929158ddfd1b83831c3c85c74e10ed07e27829751156082a2893d","b729137c0d63f7e338a7610146024d82fe14296827c65f5e5a81723186c9b0ec","0369f9e192a904eaab2f0141bd8cee9fe869ed5e6ee9d24c2ce348d2d3e01d49","1d23db2948a536723de642bcf23e33f4b5e4019a845f92e9e84ffab08b712c4f","bdc49c09c1f22f391800203f83f8c741e4aba50fad742e3283b7c71ac36fd40f","012af783e77d8569acfb84f6752bf041e98a0eabde33ca8e848aaafbdc45a698","9fb6728fc4642b739d05a9601159263167658a3e391180887234297873f03fda","60a26351252001085dfcb3e0c6ca896cace42d171f02a41e2a00f5095f5171c2","2d0f44affa9bbbceb73ed1f7c48c0e77cc66977a5fb24c82392b0deb2fecfaa7","99e3471d53721d010ebf2ca9d2570cc3bccddc01b4e6e2ea9ed278311d046640","62cc8c5936d61e0e21491b03edcf2787d588df5111f10e15384a2f545879a2f4","d004071c11da5243ad9d468aa57a96156c7010598eb642d25e8c9f70e2cdd8c0"],"20000000","1701cdfb","690a50af",false]}
> I (2300743) create_jobs_task: New Work Dequeued 5c12421
> I (2362204) stratum_api: rx: {"id":null,"method":"mining.notify","params":["5c136b0","fa862fb036c46e38292c7a94f85503922a26582d0000dc1e0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170374120e5075626c69632d506f6f6c","ffffffff02080ee612000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9ed21b99f1645a9f754209285adda1259babd91b55da94b886009148c11da3f1e8400000000",["1d7b9b0851d929158ddfd1b83831c3c85c74e10ed07e27829751156082a2893d","b729137c0d63f7e338a7610146024d82fe14296827c65f5e5a81723186c9b0ec","0369f9e192a904eaab2f0141bd8cee9fe869ed5e6ee9d24c2ce348d2d3e01d49","1d23db2948a536723de642bcf23e33f4b5e4019a845f92e9e84ffab08b712c4f","bdc49c09c1f22f391800203f83f8c741e4aba50fad742e3283b7c71ac36fd40f","871a203d330130c24f67906796f8cc46c01451dc31b6833d1e1d18d26bc178dd","18da92de2719690da882b6a075604ec0e07219951eb53d0a3930bdd3df64b0a4","deb1210e87010e896b8d6a0114063b837cacf4e021180d52ca411d8615763b88","7667a55e9fc3743cb793912a8f4cf34f12cce61dbdbc6bc8d80212652cca7acb","6777c0f2f37f909ca8d9d5fd5900fe8c2a016226e402169e4439360d3d1345e7","aa59b4fa7f3433d73cc35de0dcb05a633ca5583300bb415f8dd2d543c66dad85","8ad96c3e3f22c20f9dba92bb254ddf7d56f5ef79624a1ddca2202540c85b359d"],"20000000","1701cdfb","690a50ec",false]}
> I (2362367) create_jobs_task: New Work Dequeued 5c136b0
> I (2421604) stratum_api: rx: {"id":null,"method":"mining.notify","params":["5c1493f","fa862fb036c46e38292c7a94f85503922a26582d0000dc1e0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170374120e5075626c69632d506f6f6c","ffffffff024323e812000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9ed9590ecc8dedf1cbf92db15ca465a5a134cc60ff83a72233431ad421dd59f087a00000000",["1d7b9b0851d929158ddfd1b83831c3c85c74e10ed07e27829751156082a2893d","b729137c0d63f7e338a7610146024d82fe14296827c65f5e5a81723186c9b0ec","0369f9e192a904eaab2f0141bd8cee9fe869ed5e6ee9d24c2ce348d2d3e01d49","1d23db2948a536723de642bcf23e33f4b5e4019a845f92e9e84ffab08b712c4f","911511d176e9aaa93405f2e44a325ad34337c4db40f0fee835855e46b29c9a03","5439e0be7ac1580b909e19961eb07d5f4653f114a6b3d38a23ee2c5fab91f4c0","df3b3bc476330a91dcde3460537e5bd60505cb1f2b6e73dabb9d8c0ebb6ed31f","8a80359b24c98c66bc06028ca979ac8bb59a9b6de8ef9ce3f954f334253c9c1b","536ee1ccba9d419fd5fe9b76facdc8e943a43b9731726fb42e4d3573fb2c8eb3","d2801b7604a119cf9ea2555d66c5f8dfa5b95791b5ac0adcb200f08e6ae62d11","598bc1d1b2c8a31aa4a74793508b8cfd68f74860f45a14a9989bc9b099bfaeb2","e694074444f9b61a7102ace851669b093434676559db3aea2a369a379db17754","1c136fa02cb929c82e9dfd48f894b0050dcfa4fb7f74116b7530cfa70361b865"],"20000000","1701cdfb","690a5128",false]}
> I (2421789) create_jobs_task: New Work Dequeued 5c1493f
> I (2480879) stratum_api: rx: {"id":null,"method":"mining.notify","params":["5c15bdd","fa862fb036c46e38292c7a94f85503922a26582d0000dc1e0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170374120e5075626c69632d506f6f6c","ffffffff020519ea12000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9ed45775f8d5ffe1b6cd7694a7e0a67cd630f275aff717b7052a9ae7cb314b54a4e00000000",["1d7b9b0851d929158ddfd1b83831c3c85c74e10ed07e27829751156082a2893d","b729137c0d63f7e338a7610146024d82fe14296827c65f5e5a81723186c9b0ec","0369f9e192a904eaab2f0141bd8cee9fe869ed5e6ee9d24c2ce348d2d3e01d49","1d23db2948a536723de642bcf23e33f4b5e4019a845f92e9e84ffab08b712c4f","f7a04018baa54d24163be0df4e782645e0d2c032df368bb02add7217c85a3472","3360167d88ce9fc2d24fbdba5873724049f3c66cc66070cc9bbf5557115947e9","e15db9908f95ace8222974d12bc241260013d507f86c592898467118e7af05e2","996fe56f548a6f9d2930773d17936515068efc683dbabfa76c5126d1ef7bdf5d","e097afab270f43740cecbf9fda6c7b0f3abbdb4cd5f012398054de1183142673","57d146166110e39c02465dc07450aa399b96dffe0a68b62b38ddaf1aa897448d","04c9501751b9990ae7caf61583b752dc2472c7913ef1571a1aa66d2a261b2563","50a56545e3398a66e3d35a7f0a2d691b24bc7b7f72dc55a1c6226a3914fcd6d5","4b336073b8cb9fdc78f7c11d6dc6e4dfb22c1a6e5cd895353c25ace1dc828880"],"20000000","1701cdfb","690a5164",false]}
> I (2481009) create_jobs_task: New Work Dequeued 5c15bdd
> I (2514589) websocket: WebSocket client disconnected, fd: 42
> I (2514610) websocket: WebSocket client disconnected, fd: 43
> I (2519773) websocket: WebSocket client disconnected, fd: 42
> I (2540890) stratum_api: rx: {"id":null,"method":"mining.notify","params":["5c16e96","fa862fb036c46e38292c7a94f85503922a26582d0000dc1e0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170374120e5075626c69632d506f6f6c","ffffffff02bd05ed12000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9edc94608a0b207ed59f3f792c6d5df57ed7f60e2fd468f9f86f3c8261ca3d7f44600000000",["1d7b9b0851d929158ddfd1b83831c3c85c74e10ed07e27829751156082a2893d","82211af44abdf8678dcd5c7502565113d984d2deb21687a6b6dd85429baecefc","c36a1134393d0b7692536a247077a81704005bfa633615bb3f8d8ff68696db3c","639f1f168d686eab52ea9c9adeefbefd76ecef121139aee363a24a63fbf6a5e3","260c48eeea54b24a4610da626a40a6aaa67352fac4dfb3819b5725d1033d609d","3b007413b003a5f25136fb91186ef78d40d8e06b92d799fcb330f9e1becfdd43","e923e34d1fb8716c7751b5b25311028304b9a71898ce3dbf92ef80d83278aa68","4f76e3ff64fd52264d222e370d8fe976c1cb7b74a6c34f5542b33478224f5710","003d8897d9dd594fc0c1540a460e1fc67cec939bffddd4db3d53cdbaa3269ee1","8da5fa2713964203afb009f64b334fc95a2ef26be97b8838dccdf5c94a9251ba","5826482197fffc920a56dc3150f5020e8bf10d8206dc9964193896f7e098c219","870361340ba225dfcccc3a6ca8719c3bc1139fdccceed4588e62e47dc57c0e22","334cd6974e228433d532e536ea22ba2e9b13100267250e170fb6d58491b1c221"],"20000000","1701cdfb","690a51a0",false]}
> I (2541032) create_jobs_task: New Work Dequeued 5c16e96
> ```
> 
> <img alt="Image" width="709" height="821" src="https://private-user-images.githubusercontent.com/31411449/509767311-88678938-a3eb-42ea-8a3c-dc6d6768d4fe.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjIyOTQyNjksIm5iZiI6MTc2MjI5Mzk2OSwicGF0aCI6Ii8zMTQxMTQ0OS81MDk3NjczMTEtODg2Nzg5MzgtYTNlYi00MmVhLThhM2MtZGM2ZDY3NjhkNGZlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTExMDQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMTA0VDIyMDYwOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTk4MDBlYmI0OTVmNmQ3MWJmMTRlY2FhYWVmNTI3Mzg1NTA4MjY3NGI3MDEyMDhiODg2NTY5YWZiNjQzOWI1YzAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.IMON_TGwGmUk2l-mx3O_NIl6SXXzNrgvTSa4odhPHko">

nice catch! that's it!

Can you give me some details about your hardware? ideally a photo of the front of the bitaxe and what PSU you are using. What is the PSU plugged into (power strip, etc). What esp-miner firmware version are you running?

What pool are you connected to?

I'll create a debug firmware for you soon that you can load and maybe we cen get some more detailed info from the logs.

### skot on 2025-11-04

<img width="322" height="70" alt="Image" src="https://github.com/user-attachments/assets/85da258f-18e4-4148-8c43-38f07a78deec" />

I suspect this problem happens more frequently because you're overclocked. But we should be able to handle errors like this more gracefully than FoD

### EricDimitri on 2025-11-04

I went to default values, and happened anyway... there must be something else there.... Half an hour ago, i reapplied thermal paste, and didnt screw very tight, to be sure the Asic was not pressed too hard, and overclocked a little bit more, and so far so good... will keep you posted...

<img width="698" height="623" alt="Image" src="https://github.com/user-attachments/assets/10b9b321-9f35-48ad-8a35-81f30cbd3be6" />

### EricDimitri on 2025-11-05

@skot 

Someting New to add:

1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25681394) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25681429) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25681430) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25681475) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25681476) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25681521) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25681522) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25681567) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25681568) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25681613) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25681614) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25681659) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25681660) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25681705) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25681706) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25681751) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25681752) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25681797) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25681798) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25681843) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25681844) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25681889) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25681890) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25681935) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25681936) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25681981) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25681982) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682027) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682028) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682073) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682074) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682119) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682120) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682165) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682166) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682211) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682212) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682257) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682258) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682303) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682304) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682349) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682350) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682395) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682396) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682441) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682442) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682487) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682488) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682534) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682535) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682579) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682580) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682625) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682627) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682672) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682673) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682718) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682719) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682764) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682765) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682810) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682811) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682856) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682857) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682902) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682903) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682948) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682949) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25682994) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25682995) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683040) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683041) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683086) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683087) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683132) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683133) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683178) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683179) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683224) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683225) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683270) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683271) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683316) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683317) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683362) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683363) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683408) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683409) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683454) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683455) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683500) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683501) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683546) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683547) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683592) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683593) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683638) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683639) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683684) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683685) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683730) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683731) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683776) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683777) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683822) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683823) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683868) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683869) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683914) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683915) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25683960) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25683961) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25684006) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25684007) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25684052) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25684053) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25684098) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25684099) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25684144) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25684145) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25684190) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25684191) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25684236) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25684237) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25684282) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25684283) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25684328) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25684329) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25684374) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25684375) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25684420) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000
₿ (25684421) asic_result: ID: 6360955, ver: 20192000 Nonce ED3441BB diff 0.0 of 16384.
₿ (25684466) bm1370: Job ID: 08, Core: 93/9, Ver: 00192000

<img width="900" height="727" alt="Image" src="https://github.com/user-attachments/assets/0f944783-98de-4611-bb43-d21146e17ea6" />


### EricDimitri on 2025-11-05

@skot  , A new interesting one:


₿ (644814) httpd_ws: httpd_ws_send_frame_async: Failed to send WS header
₿ (644814) httpd_txrx: httpd_sock_err: error in send : 128
₿ (644817) websocket: WebSocket client disconnected, fd: 46
₿ (644823) httpd_ws: httpd_ws_send_frame_async: Failed to send WS header
₿ (644829) websocket: Removed WebSocket client, fd: 46, slot: 0
₿ (644932) websocket: Added WebSocket client, fd: 46, slot: 0
₿ (644933) websocket: WebSocket handshake successful, fd: 46
₿ (656707) stratum_api: rx: {"id":null,"method":"mining.notify","params":["641b817","61d09c3ffd1073d73cdf71dce32720761cc6eaec00008d180000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170312130e5075626c69632d506f6f6c","ffffffff020823fe12000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9ed9b4a04b07b3083913c87f191e59747d53f9baf5f840ee3d417bb83158555fa5700000000",["9e6ffe772d8d6d50b0f00bbb6520e157394f6aead6c27ac7ef3786f55f72c499","e945c08a307966f1b491689d5283a274165ee0514feacbeb002dbbf70cb20648","e9dab6b7bd7f3fbdf767246b6312c6bcd47bd2d0ed51d046a1f5078c6e33c8fd","933296b8b7023cb5a2d2f1e60c17ba850abbb26c3faceb57dd52d1ab097e3702","3cd025137528b13060f5a15d6eb9385b7a2288f2c48277ba28307b50d62a4cb3","89afd1cae469c1f361bfdccdd640cd797ac7eb7c513df61a1b5620b77697864c","26d69084e56f3852a1a2b32c43c6e4453990c0a22b1ea475be9890ca401a8c39","d9a8347270604b9e7f3a59c10c428eed19533c0e90509ada84e0fa17d7d718c3","7dfbacde7b0d60645bca2b757208a831af6b9d6d716bfc9f59989105be66ae25","7d8b1f87e8470c93347690c92d21d24689599cf3dca1e4942d6d58a21445b0b9","e8b8804e4839310709efbc0585717d5d277f25bae108cda4e399e3466ca8d147","1dc6a48b80a7fa8ebad7c43c54ffe1da510a1610bc6ac60dd4140e21054d4fe9"],"20000000","1701cdfb","690be1b2",false]}
₿ (656849) create_jobs_task: New Work Dequeued 641b817
₿ (681951) websocket: WebSocket client disconnected, fd: 44
₿ (692214) httpd_txrx: httpd_sock_err: error in recv : 104
₿ (692215) websocket: WebSocket client disconnected, fd: 44
₿ (717364) stratum_api: rx: {"id":null,"method":"mining.notify","params":["641cc84","61d09c3ffd1073d73cdf71dce32720761cc6eaec00008d180000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170312130e5075626c69632d506f6f6c","ffffffff022489ff12000000001976a9149f678f2f0366fe0edddf36ae7b715542be030d3d88ac0000000000000000266a24aa21a9ed6c7825d582557f2cc11b85b998410dc8cda30bd7323a0a63ab977d96c936790f00000000",["9e6ffe772d8d6d50b0f00bbb6520e157394f6aead6c27ac7ef3786f55f72c499","e945c08a307966f1b491689d5283a274165ee0514feacbeb002dbbf70cb20648","865465276272a22d7ec0fab6b62d4ec35f80359ebe3a160a5dd44e1f37918808","933296b8b7023cb5a2d2f1e60c17ba850abbb26c3faceb57dd52d1ab097e3702","3cd025137528b13060f5a15d6eb9385b7a2288f2c48277ba28307b50d62a4cb3","8fdfb7ef7323fae9c55c194288c35f3214aef8eac9984284ddb92abee14a7a62","8a98f653242f3acb3a0af48a141741947faf9b8d5784add3a5ddfdd24b68359a","8381175f684b1db764109bb234e5ab0695f75de24d0d2199173ffd84f1a3c39b","814ed3a1181732c9c90e442f6920ecddbbba1d4fd0659a9886d6abea6bc416c3","a1847fb2f0bdbed52b6501e814e1649725b2b6cde19ef0137a380a1c08348890","79b1ef22ae0661dae0fbe4f4463ceaf5e767bee2104df967417a699dfa7cd737","cc656acde1bd3fc212e49ebbb2c8129a93e03e01fb417d65bdd8d1f6ca83cdcb"],"20000000","1701cdfb","690be1ee",false]}
₿ (717474) create_jobs_task: New Work Dequeued 641cc84

<img width="904" height="734" alt="Image" src="https://github.com/user-attachments/assets/81a6960a-0901-4469-9290-89363ba18be2" />


### ThymeKeeper on 2025-11-09

i have this problem.. but my workaround is to have my Pi node tell the bitaxe to reboot every 30 minutes..

```
#!/bin/bash

# Restart ckpool
sudo systemctl restart ckpool.service

# Reboot BitAxe
curl -X POST http://192.168.1.126/api/system/restart
```

<img width="2880" height="1800" alt="Image" src="https://github.com/user-attachments/assets/76cbae02-e041-4232-8a81-3521de9569b9" />

### EricDimitri on 2025-11-09

Yep, I did some Automation that checks If HashRate is exactly the same after N times, restart the bitaxe, but I would prefer to have it running as it should 8-D

### ThymeKeeper on 2025-11-09

may i ask how you did that? that sounds better than a blind 30 minute reboot

### EricDimitri on 2025-11-09

> may i ask how you did that? that sounds better than a blind 30 minute reboot

Checking "http://192.168.x.x/api/system/info" and checking "hashrate" and if same for N times, then "http://192.168.x.x/api/system/restart" to resart. 

### ThymeKeeper on 2025-11-10

awesome, thank you. i think this is working:

```
#!/bin/bash

BITAXE_IP="192.168.1.126"
HISTORY_FILE="/tmp/hashrate_history.txt"
LOG_FILE="/home/ubuntu/smart-restart.log"
MAX_LOG_LINES=50  # Keep only last 50 log entries

# Function to add to log with rotation
log_message() {
    echo "$1" >> $LOG_FILE
    # Keep only last MAX_LOG_LINES
    tail -n $MAX_LOG_LINES $LOG_FILE > /tmp/temp_log && mv /tmp/temp_log $LOG_FILE
}

# Get hashrate from API
CURRENT_HASH=$(curl -s http://${BITAXE_IP}/api/system/info 2>/dev/null | grep -oP '"hashRate":\s*[0-9.]+' | grep -oP '[0-9.]+$')

# If we can't get hashrate, exit
if [ -z "$CURRENT_HASH" ]; then
    log_message "$(date): Failed to get hashrate"
    exit 1
fi

# Round to 1 decimal place
CURRENT_HASH=$(printf "%.1f" $CURRENT_HASH)

# Add to history file
echo "$CURRENT_HASH" >> $HISTORY_FILE

# Keep only last 5 readings
tail -5 $HISTORY_FILE > /tmp/temp_hash && mv /tmp/temp_hash $HISTORY_FILE

# Count how many readings we have
LINE_COUNT=$(wc -l < $HISTORY_FILE)

# Need at least 3 readings to compare
if [ $LINE_COUNT -ge 3 ]; then
    # Check if all values are identical
    UNIQUE_COUNT=$(sort -u $HISTORY_FILE | wc -l)
    
    if [ $UNIQUE_COUNT -eq 1 ]; then
        log_message "$(date): Flatline detected! Last $LINE_COUNT readings all show $CURRENT_HASH GH/s. Restarting..."
        
        # Restart both
        sudo systemctl restart ckpool.service
        curl -X POST http://${BITAXE_IP}/api/system/restart
        
        # Clear history after restart
        > $HISTORY_FILE
        
        log_message "$(date): Restart complete"
    fi
fi
```

### EricDimitri on 2025-11-10

Nice!

### nymkappa on 2025-11-11

Just wanted to mention that I did not get this issue for 3+ months now
I'm running latest release.

### dsaukou on 2025-11-11

In my case, the problem has remained the same. On any firmware release, including the latest one. Nothing has changed.

### mutatrum on 2025-11-11

> In my case, the problem has remained the same. On any firmware release, including the latest one. Nothing has changed.

Can you try with the latest beta: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.11.0b6

There's quite a bit more information on the dashboard, and the way the hashrate is measured is different. This might give us more information on what's happening.

### EricDimitri on 2025-11-11

Hi!! My case is incredible. I moved the bitaxes in the desktop, to a different position, and "magically" stopped geting Flat Line... I am thinking that could be related to some sort of Wi-Fi interference? may be because it was between 2 laptops, a desktop and 2 monitors, now they are just between 2 monitors?  I cant think of any other reason, since everything is exacxtly the same. :S

### EricDimitri on 2025-11-11

@mutatrum,   Which files should I download? I downloaded esp-miner.bin and www.bin, and I see same dashboard, and version looks the same... 
### UPDATE ###
Not sure why, but tried again, and now i see beta version. LEts see how it goes... let me know if you want something from my logs.
Thanks!!!
### UPDATE ###
Good to see extra info!!!
What I dont like is that the Uptime is gone!? IT was really useful to see that. IS it too much to keep showing it?
Thanks again!!!
    Eric

### dsaukou on 2025-11-12


> Can you try with the latest beta: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.11.0b6
> 
> There's quite a bit more information on the dashboard, and the way the hashrate is measured is different. This might give us more information on what's happening.

OK. I'll try this version. And write about the results later....

### dsaukou on 2025-11-12

Interface of new firmware looks more useful and Interesting. But after 5-10 minutes of working I get the error again, and FoD line too...

![Image](https://github.com/user-attachments/assets/17b1057a-e931-4079-93bc-9320644bd9aa)
![Image](https://github.com/user-attachments/assets/0138841d-7f24-408a-9ae0-14e5b5b400f8)

Return to version 2.10.1

### mutatrum on 2025-12-01

New report with latest beta, Gamma at 750 Mhz/1250 mV:
```
I (2658539) asic_result: ID: 2066, ASIC nr: 0, ver: 20208000 Nonce 68D80418 diff 1502.4 of 4096.
I (2659987) power_management: Temp: 48.1 °C, SetPoint: 60.0 °C, Output: 50.0% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (2661791) power_management: Temp: 48.4 °C, SetPoint: 60.0 °C, Output: 50.0% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (2662393) bm1370: Job ID: 38, Asic nr: 0, Core: 96/11, Ver: 04776000
I (2662394) asic_result: ID: 2066, ASIC nr: 0, ver: 24776000 Nonce 5CA404C0 diff 314.1 of 4096.
I (2662670) bm1370: Job ID: 50, Asic nr: 0, Core: 17/2, Ver: 01BE4000
I (2662671) asic_result: ID: 2066, ASIC nr: 0, ver: 21BE4000 Nonce 0EFD0322 diff 267.6 of 4096.
I (2662847) bm1370: Job ID: 50, Asic nr: 0, Core: 58/13, Ver: 03E7A000
I (2662848) asic_result: ID: 2066, ASIC nr: 0, ver: 23E7A000 Nonce E9250574 diff 903.2 of 4096.
I (2663595) power_management: Temp: 48.4 °C, SetPoint: 60.0 °C, Output: 50.0% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (2664526) bm1370: Job ID: 18, Asic nr: 0, Core: 47/4, Ver: 06188000
I (2664527) asic_result: ID: 2066, ASIC nr: 0, ver: 26188000 Nonce 2395015E diff 1246.2 of 4096.
I (2665399) power_management: Temp: 48.2 °C, SetPoint: 60.0 °C, Output: 50.0% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (2666042) bm1370: Job ID: 78, Asic nr: 0, Core: 29/5, Ver: 002EA000
I (2666043) asic_result: ID: 2066, ASIC nr: 0, ver: 202EA000 Nonce AA92023A diff 407.2 of 4096.
I (2667204) power_management: Temp: 48.6 °C, SetPoint: 60.0 °C, Output: 50.0% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (2667366) bm1370: Job ID: 28, Asic nr: 0, Core: 46/8, Ver: 04210000
I (2667367) asic_result: ID: 2066, ASIC nr: 0, ver: 24210000 Nonce DC40075C diff 536.9 of 4096.
I (2667932) bm1370: Job ID: 40, Asic nr: 0, Core: 34/3, Ver: 046E6000
I (2667933) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2667977) bm1370: Job ID: 40, Asic nr: 0, Core: 34/3, Ver: 046E6000
I (2667978) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2668022) bm1370: Job ID: 40, Asic nr: 0, Core: 34/3, Ver: 046E6000
I (2668023) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2668067) bm1370: Job ID: 40, Asic nr: 0, Core: 34/3, Ver: 046E6000
I (2668067) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2668111) bm1370: Job ID: 40, Asic nr: 0, Core: 34/3, Ver: 046E6000
I (2668112) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2668156) bm1370: Job ID: 40, Asic nr: 0, Core: 34/3, Ver: 046E6000
I (2668157) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2668201) bm1370: Job ID: 40, Asic nr: 0, Core: 34/3, Ver: 046E6000
I (2668201) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2668245) bm1370: Job ID: 40, Asic nr: 0, Core: 34/3, Ver: 046E6000
I (2668246) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2668290) bm1370: Job ID: 40, Asic nr: 0, Core: 34/3, Ver: 046E6000
I (2668291) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2668335) bm1370: Job ID: 40, Asic nr: 0, Core: 34/3, Ver: 046E6000
I (2668336) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
```
Last mining.notify was ~58 seconds before flatline, it got first sent to the asic ~47 seconds before flatline. 

All `asic_result` log entries from that job:
```
I (2621015) asic_result: ID: 2066, ASIC nr: 0, ver: 25F06000 Nonce D4C10242 diff 652.9 of 4096.
I (2622900) asic_result: ID: 2066, ASIC nr: 0, ver: 2488C000 Nonce AF1D0738 diff 319.6 of 4096.
I (2623299) asic_result: ID: 2066, ASIC nr: 0, ver: 234C8000 Nonce C9430608 diff 442.4 of 4096.
I (2623853) asic_result: ID: 2066, ASIC nr: 0, ver: 23F6A000 Nonce 7BDE02B8 diff 850.0 of 4096.
I (2624564) asic_result: ID: 2066, ASIC nr: 0, ver: 206EE000 Nonce BF0D06E2 diff 642.7 of 4096.
I (2626382) asic_result: ID: 2066, ASIC nr: 0, ver: 2453E000 Nonce A4D100FA diff 526.6 of 4096.
I (2627146) asic_result: ID: 2066, ASIC nr: 0, ver: 21702000 Nonce F9F90330 diff 65618.0 of 4096.
I (2627176) asic_result: ID: 2066, ASIC nr: 0, ver: 21972000 Nonce 8BD40470 diff 546.3 of 4096.
I (2627210) asic_result: ID: 2066, ASIC nr: 0, ver: 221E4000 Nonce 34E60230 diff 391.4 of 4096.
I (2627941) asic_result: ID: 2066, ASIC nr: 0, ver: 250B0000 Nonce C6E9027A diff 282.5 of 4096.
I (2628342) asic_result: ID: 2066, ASIC nr: 0, ver: 23D38000 Nonce 76CF0556 diff 270.5 of 4096.
I (2628920) asic_result: ID: 2066, ASIC nr: 0, ver: 24C6A000 Nonce 022D035A diff 263.8 of 4096.
I (2629580) asic_result: ID: 2066, ASIC nr: 0, ver: 20A1C000 Nonce A53F0586 diff 521.0 of 4096.
I (2630309) asic_result: ID: 2066, ASIC nr: 0, ver: 236C8000 Nonce ED7406AA diff 330.2 of 4096.
I (2630376) asic_result: ID: 2066, ASIC nr: 0, ver: 243FC000 Nonce 06F90004 diff 2730.7 of 4096.
I (2631390) asic_result: ID: 2066, ASIC nr: 0, ver: 246B0000 Nonce FA6200D0 diff 1728.0 of 4096.
I (2631402) asic_result: ID: 2066, ASIC nr: 0, ver: 247EE000 Nonce 0FAA034C diff 539.9 of 4096.
I (2633086) asic_result: ID: 2066, ASIC nr: 0, ver: 20B3C000 Nonce 6D1206D0 diff 1684.2 of 4096.
I (2633848) asic_result: ID: 2066, ASIC nr: 0, ver: 23E7E000 Nonce 5FC80104 diff 1538.1 of 4096.
I (2634878) asic_result: ID: 2066, ASIC nr: 0, ver: 2445E000 Nonce D1440424 diff 372.0 of 4096.
I (2635077) asic_result: ID: 2066, ASIC nr: 0, ver: 2096C000 Nonce F52D0466 diff 1004.4 of 4096.
I (2635332) asic_result: ID: 2066, ASIC nr: 0, ver: 23B64000 Nonce 91C900C4 diff 662.5 of 4096.
I (2635529) asic_result: ID: 2066, ASIC nr: 0, ver: 20022000 Nonce 2D70022C diff 386.8 of 4096.
I (2635740) asic_result: ID: 2066, ASIC nr: 0, ver: 22948000 Nonce 353104BA diff 3788.4 of 4096.
I (2635884) asic_result: ID: 2066, ASIC nr: 0, ver: 2456C000 Nonce F55C0440 diff 1515.2 of 4096.
I (2636030) asic_result: ID: 2066, ASIC nr: 0, ver: 2005C000 Nonce BDAA01CA diff 258.8 of 4096.
I (2638098) asic_result: ID: 2066, ASIC nr: 0, ver: 20D9C000 Nonce E33C03B2 diff 277.8 of 4096.
I (2638135) asic_result: ID: 2066, ASIC nr: 0, ver: 214F2000 Nonce 5C78045C diff 575.3 of 4096.
I (2639821) asic_result: ID: 2066, ASIC nr: 0, ver: 23932000 Nonce E589009E diff 329.3 of 4096.
I (2640599) asic_result: ID: 2066, ASIC nr: 0, ver: 20DDE000 Nonce 38BC0022 diff 491.7 of 4096.
I (2642639) asic_result: ID: 2066, ASIC nr: 0, ver: 21598000 Nonce CD8C0490 diff 320.7 of 4096.
I (2643857) asic_result: ID: 2066, ASIC nr: 0, ver: 24054000 Nonce F3780250 diff 487.1 of 4096.
I (2644768) asic_result: ID: 2066, ASIC nr: 0, ver: 22EFC000 Nonce C79701E6 diff 812.1 of 4096.
I (2646138) asic_result: ID: 2066, ASIC nr: 0, ver: 2157C000 Nonce 1E2A02EC diff 2800.1 of 4096.
I (2647674) asic_result: ID: 2066, ASIC nr: 0, ver: 21C8E000 Nonce EED50252 diff 342.3 of 4096.
I (2648158) asic_result: ID: 2066, ASIC nr: 0, ver: 2197E000 Nonce A295047E diff 704.5 of 4096.
I (2648268) asic_result: ID: 2066, ASIC nr: 0, ver: 22EEE000 Nonce 1E960116 diff 273.9 of 4096.
I (2648281) asic_result: ID: 2066, ASIC nr: 0, ver: 23156000 Nonce D64007C6 diff 835.3 of 4096.
I (2649494) asic_result: ID: 2066, ASIC nr: 0, ver: 25B16000 Nonce 0FA0000E diff 1757.9 of 4096.
I (2650213) asic_result: ID: 2066, ASIC nr: 0, ver: 22408000 Nonce 866204E8 diff 601.7 of 4096.
I (2650792) asic_result: ID: 2066, ASIC nr: 0, ver: 23362000 Nonce A8E805A6 diff 317.5 of 4096.
I (2651672) asic_result: ID: 2066, ASIC nr: 0, ver: 21C08000 Nonce 31F7022C diff 2249.1 of 4096.
I (2652596) asic_result: ID: 2066, ASIC nr: 0, ver: 20D52000 Nonce 00FD00AA diff 273.4 of 4096.
I (2652987) asic_result: ID: 2066, ASIC nr: 0, ver: 259B2000 Nonce 75AE0344 diff 313.8 of 4096.
I (2653051) asic_result: ID: 2066, ASIC nr: 0, ver: 20490000 Nonce 32620362 diff 332.1 of 4096.
I (2653209) asic_result: ID: 2066, ASIC nr: 0, ver: 22348000 Nonce 082B0798 diff 367.7 of 4096.
I (2653636) asic_result: ID: 2066, ASIC nr: 0, ver: 21502000 Nonce FBEB02DA diff 1818.4 of 4096.
I (2654205) asic_result: ID: 2066, ASIC nr: 0, ver: 2226E000 Nonce 635A0484 diff 296.0 of 4096.
I (2654807) asic_result: ID: 2066, ASIC nr: 0, ver: 23674000 Nonce 61C10334 diff 326.2 of 4096.
I (2656024) asic_result: ID: 2066, ASIC nr: 0, ver: 260C4000 Nonce 6C930610 diff 273.6 of 4096.
I (2657093) asic_result: ID: 2066, ASIC nr: 0, ver: 20CAE000 Nonce 064205D0 diff 272.0 of 4096.
I (2657210) asic_result: ID: 2066, ASIC nr: 0, ver: 2236C000 Nonce 18FD0502 diff 2245.8 of 4096.
I (2657284) asic_result: ID: 2066, ASIC nr: 0, ver: 231F8000 Nonce 4FE503E2 diff 3012.4 of 4096.
I (2658539) asic_result: ID: 2066, ASIC nr: 0, ver: 20208000 Nonce 68D80418 diff 1502.4 of 4096.
I (2662394) asic_result: ID: 2066, ASIC nr: 0, ver: 24776000 Nonce 5CA404C0 diff 314.1 of 4096.
I (2662671) asic_result: ID: 2066, ASIC nr: 0, ver: 21BE4000 Nonce 0EFD0322 diff 267.6 of 4096.
I (2662848) asic_result: ID: 2066, ASIC nr: 0, ver: 23E7A000 Nonce E9250574 diff 903.2 of 4096.
I (2664527) asic_result: ID: 2066, ASIC nr: 0, ver: 26188000 Nonce 2395015E diff 1246.2 of 4096.
I (2666043) asic_result: ID: 2066, ASIC nr: 0, ver: 202EA000 Nonce AA92023A diff 407.2 of 4096.
I (2667367) asic_result: ID: 2066, ASIC nr: 0, ver: 24210000 Nonce DC40075C diff 536.9 of 4096.
I (2667933) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2667978) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2668023) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2668067) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2668112) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2668157) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2668201) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2668246) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2668291) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2668336) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2668380) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
I (2668425) asic_result: ID: 2066, ASIC nr: 0, ver: 246E6000 Nonce 6736E345 diff 474.7 of 4096.
```

I don't know how to troubleshoot this, or what logging to add. 

### mutatrum on 2026-03-31

To all here: is this still an issue?

### danv8472-cell on 2026-03-31

Mine stopped being an issue a while back already. Thanks for looking into
it. I do not know what the fix was. It just seemed to stop having the
problem.

On Tue, Mar 31, 2026 at 1:38 AM mutatrum ***@***.***> wrote:

> *mutatrum* left a comment (bitaxeorg/ESP-Miner#1053)
> <https://github.com/bitaxeorg/ESP-Miner/issues/1053#issuecomment-4160566223>
>
> To all here: is this still an issue?
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/bitaxeorg/ESP-Miner/issues/1053?email_source=notifications&email_token=BXVXF3ZAYWGR3VPVLUW5MZT4TNYXZA5CNFSNUABFM5UWIORPF5TWS5BNNB2WEL2JONZXKZKDN5WW2ZLOOQXTIMJWGA2TMNRSGIZ2M4TFMFZW63VHMNXW23LFNZ2KKZLWMVXHJLDGN5XXIZLSL5RWY2LDNM#issuecomment-4160566223>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/BXVXF3ZOQLJMQ77ZHULQPK34TNYXZAVCNFSM6AAAAAB7XPOQTGVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHM2DCNRQGU3DMMRSGM>
> .
> You are receiving this because you commented.Message ID:
> ***@***.***>
>


### AngryDragonflyStudios on 2026-04-28

i have this issue myself with my gamma 601 running latest beta 2.14.0b1 happens to me within 15 minutes. reboot temp resolves.

### IdotMaster1 on 2026-05-15

I do wonder if this is some sort of hardware failure, as it cant be easily reproduced it seems.

### IdotMaster1 on 2026-05-17

I have been trying to debug this for awhile but it seems that if I connect the USB to a power brick or computer and then power up the Bitaxe, it doesn't flatline.
Without the USB, it eventually flatlines.

### kerenskybr on 2026-08-10

Still present on **v2.14.2**. Adding a measurement that may help narrow where the hang is, since I had 30-second telemetry logging across three occurrences today.

**The key detail: `hashRate_1m` freezes to the exact decimal while the sensors keep updating.**

That distinguishes three possibilities. If the ASIC had stopped, the 1-minute rolling average would decay toward zero over the following minute. If the whole system had hung, temperature and fan readings would freeze too. Neither happened — the average stopped being *computed* at its last value, while everything else stayed live.

### Occurrence 1

```
time(UTC)   hashRate   hashRate_1m   power   temp      fan    sharesAccepted
14:16:57     1299.2        1218.1    16.5W   60.125    3239         14761
14:17:27        0.0        1213.9    16.5W    59.75    3231         14764   <- stops
14:17:57        0.0        1213.9    16.5W   59.875    3262         14764
14:18:28        0.0        1213.9    16.5W    60.25    3193         14764
14:18:58        0.0        1213.9    16.5W    60.25    3262         14764
14:19:28        0.0        1213.9    16.5W       60    3327         14764
14:19:58        0.0        1213.9    16.5W   60.125    3318         14764
14:20:28        0.0        1213.9    16.5W       60    3318         14764
14:20:58        0.0        1213.9    16.5W    59.75    3254         14764
14:21:28        0.0        1213.9    16.5W   59.875    3208         14764
14:21:59        0.0        1213.9    16.5W    60.25    3270         14764
14:22:29        0.0        1213.9    16.5W    59.75    3247         14764   <- restart issued
14:22:59     1260.6        1243.7    15.9W     54.5    1510             3   <- recovered
```

Across the 11 stalled samples: `hashRate_1m` has exactly **one** distinct value (`1213.9`), while `temp` takes **five** distinct values (59.75 / 59.875 / 60 / 60.125 / 60.25) and `fanrpm` ranges 3193–3327. So the sensor and fan-control tasks were running normally the whole time. `power` stayed pinned at 16.5 W, i.e. the ASIC was still drawing full load and generating full heat.

Occurrence 2 was identical in shape: 5 stalled samples, `hashRate_1m` frozen at exactly `1199.8`, temps again spanning four distinct values.

So the ASIC keeps hashing and the system keeps running — only the result/accounting path stops. `sharesAccepted` freezes at the same instant.

### Ruled out by direct measurement

| Suspect | Measurement during the stall |
|---|---|
| Thermal | 60.0 °C ASIC / 49 °C VR, on target. The **coldest** run failed **fastest** (see below) |
| PSU sag | Input 5468.8 mV during the stall vs 5460.9 mV baseline — steadier, not sagging |
| Heap exhaustion | `freeHeap` 7,664,732 / internal 64,347 during the stall vs 7,664,228 / 63,515 at 14 h uptime — flat |
| WiFi | RSSI −49/−50 dBm, unchanged throughout |
| Pool | `isUsingFallbackStratum: 0` throughout, no reconnect in the log |

On thermal specifically: I raised `minFanSpeed` to 40%, which brought the ASIC from 60 °C to 56 °C and the VR from 49 °C to 43 °C. The next failure came *sooner*, not later:

| Occurrence | Uptime before failure | ASIC temp | Fan |
|---|---|---|---|
| 1 | 16 h 54 m | 60 °C | ~3250 rpm |
| 2 | 3 h 28 m | 60 °C | ~4200 rpm |
| 3 | ~25 m | **56 °C** | 4986 rpm |

### Possibly related: duplicate `asic_result`

I see a low-grade version of #1820 on this unit. Over a 22.6-minute log window:

- 1554 `asic_result` lines / 1502 unique nonces → mean repeat 1.03×, max 3×
- 374 `mining.submit` / 350 unique → 6.4% duplicate submissions
- 1 `Checksum failed`, 0 `Preamble mismatch`, 0 I2C errors

Nothing like the ~197× bursts and heavy UART corruption in #1820, so I don't think I have that fault. But the duplicates come from the same result-handling path that goes silent during a flatline, and my pool reports every single reject as a duplicate (38/38). Mentioning it in case a race in that path explains both.

Caught in the log — one nonce submitted twice, 56 ms apart:

```
I (187024) stratum_api: tx: {"id":29,"method":"mining.submit","params":["<addr>.bitaxe","b2042f6800000000","3600000000000000","6a7a103b","a3dada71","00090000"]}
I (187032) asic_result: Processing time: 1.8 ms
I (187037) asic_result: ID: b2042f6800000000, ASIC nr: 0, Core: 56/8, ver: 20090000 Nonce A3DADA71 diff 7565.7 of 2048.
I (187080) stratum_api: tx: {"id":30,"method":"mining.submit","params":["<addr>.bitaxe","b2042f6800000000","3600000000000000","6a7a103b","a3dada71","00090000"]}
```

Same job, same extranonce2, same ntime, same version, same nonce.

### Recovery

`POST /api/system/restart` clears it reliably — hashing resumes ~30 s later. The device stays fully responsive to HTTP throughout the stall, which is consistent with only the mining/result task being stuck.

### Environment

- Bitaxe Gamma, board version 601, BM1370
- Firmware v2.14.2 / AxeOS v2.14.2 / ESP-IDF v5.5.3
- 600 MHz / 1150 mV, `overclockEnabled: 0` (stock)
- Pool difficulty 1024–2048 (low, so duplicates reach the pool)
- PSU: 5V/6A - 30w -50/60hz
- WiFi RSSI −49 dBm

### Note on detection

Per the original request in this issue for automatic recovery: detecting this is straightforward and doesn't need firmware changes. Polling `/api/system/info` every 30 s and restarting after `hashRate` sits below ~25% of `expectedHashrate` for 2 minutes catches it with no false positives so far. The unambiguous signature is `hashRate_1m` not changing at all while `temp` continues to vary — a genuine ramp-down never holds the average constant to the decimal. Happy to share the script if it's useful to anyone.

I have full 30-second telemetry (hashrate, temps, power, fan, shares, RSSI, uptime) across all three occurrences plus firmware log captures taken at the moment of failure. Glad to provide them or run any diagnostics/test builds.


### Biohazmatt on 2026-09-24

Gday , ive experienced this issue with the last few versions and ive just stuck with 2.11.4 ever since , recently i was doing some digging on the TCH ( TinyChipHub ) repo and saw someone mention this , which is a potential cause and fix 

https://github.com/TinyChipHub/ESP-Miner-TCH/issues/27#issuecomment-5653061741

### awi81 on 2026-09-25

Two observations from running an auto-recovery for this on four Gamma 601s (a fork of v2.15.0rc1), in case they help whoever builds the upstream fix:

**1. Check counters, not the rolling averages.** @kerenskybr's data shows it: on a hang, `hashRate_1m`/`_10m` don't drop, they freeze at the last healthy value. Our first watchdog triggered on `hashrate_10m == 0` and therefore never fired on a real hang. A check like the TCH `check_hashrate_anomaly` (below 82 % of expected) would miss it too if it reads the average. What works is progress of a counter over a window: `sharesAccepted`, or better a chip-side counter (below).

**2. There are two flatlines that look the same from outside,** and they need different fixes:
- **Chip/result path stops.** No `asic_result` lines, shares frozen, power still at full load. Only re-init/restart helps. This is kerenskybr's case and #1975.
- **Pool stops answering one session.** Shares frozen too, but the chip keeps producing nonces. On one miner we logged 55–86 valid nonces/min and a `mining.notify` every 30 s for 20 min without a single reply to its `mining.submit`s (public-pool, 2026-09-23). Other miners on the same pool were answered normally. A restart "fixed" it, but only because it reconnected, and that makes the two cases easy to confuse.

What we do now: `asic_result` counts every nonce with diff ≥ the chip's ticket difficulty (the chip's own proof of work, independent of the pool).
- Shares silent for 10 min, and no ≥ 10 such nonces in 5 min → restart after another 10 min. At most 3 tries, budget restored after an hour of healthy mining, and not within 30 min of boot.
- Nonces flowing, jobs arriving, shares silent → reconnect stratum with back-off (0/15/45/105/225 min, then every 4 h) instead of restarting.

The restart has fired correctly on a dead chip in the field, with the earlier shares-only check. The nonce counter and the pool-side reconnect are newer and haven't been triggered yet. I can turn the counter + distinction into a PR against master if that would be useful. It touches `asic_result` and the stratum task, so I'd rather ask first.
