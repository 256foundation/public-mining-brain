# bitaxeorg/ESP-Miner issue #1158: Bitaxe Supra does not hash

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1158
> Collected: 2026-10-07
> Published: 2025-07-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1158
- State: closed
- Author: PK92-Supra
- Opened: 2025-07-23
- Closed: 2025-07-23
- Labels: none

## Description

My device does not start hashing. 
I have powered it down a couple of times, I put the new software version on it, I changed the Stratum url. Nothing seems to work. I detected the issue when I could not reach the miner on the regular IP I always used, wich I had as a bookmark. I was in contact with some people of my local community, but they could not see the issue.

Underneath the Realtime logs, direct after a startup, after powering down the divice for 20 minutes: 

___

₿ (7591) bm1370: Setting Frequency to 100.00MHz (100.00)
₿ (7696) bm1370: Setting Frequency to 106.25MHz (106.25)
₿ (7798) bm1370: Setting Frequency to 112.50MHz (112.50)
₿ (7900) bm1370: Setting Frequency to 118.75MHz (119.05)
₿ (8002) bm1370: Setting Frequency to 125.00MHz (125.00)
₿ (8104) bm1370: Setting Frequency to 131.25MHz (131.55)
₿ (8206) bm1370: Setting Frequency to 137.50MHz (137.50)
₿ (8308) bm1370: Setting Frequency to 143.75MHz (143.75)
₿ (8390) power_management: Ignoring invalid temperature reading: -1.0°C
₿ (8410) bm1370: Setting Frequency to 150.00MHz (150.00)
₿ (8512) bm1370: Setting Frequency to 156.25MHz (156.25)
₿ (8614) bm1370: Setting Frequency to 162.50MHz (162.50)
₿ (8716) bm1370: Setting Frequency to 168.75MHz (168.75)
₿ (8818) bm1370: Setting Frequency to 175.00MHz (175.00)
₿ (8920) bm1370: Setting Frequency to 181.25MHz (181.25)
₿ (9022) bm1370: Setting Frequency to 187.50MHz (187.50)
₿ (9124) bm1370: Setting Frequency to 193.75MHz (193.75)
₿ (9226) bm1370: Setting Frequency to 200.00MHz (200.00)
₿ (9328) bm1370: Setting Frequency to 206.25MHz (206.25)
₿ (9430) bm1370: Setting Frequency to 212.50MHz (212.50)
₿ (9532) bm1370: Setting Frequency to 218.75MHz (218.75)
₿ (9634) bm1370: Setting Frequency to 225.00MHz (225.00)
₿ (9736) bm1370: Setting Frequency to 231.25MHz (231.25)
₿ (9838) bm1370: Setting Frequency to 237.50MHz (237.50)
₿ (9940) bm1370: Setting Frequency to 243.75MHz (243.75)
₿ (10042) bm1370: Setting Frequency to 250.00MHz (250.00)
₿ (10144) bm1370: Setting Frequency to 256.25MHz (256.25)
₿ (10195) power_management: Ignoring invalid temperature reading: -1.0°C
₿ (10246) bm1370: Setting Frequency to 262.50MHz (262.50)
₿ (10348) bm1370: Setting Frequency to 268.75MHz (268.75)
₿ (10450) bm1370: Setting Frequency to 275.00MHz (275.00)
₿ (10552) bm1370: Setting Frequency to 281.25MHz (281.25)
₿ (10654) bm1370: Setting Frequency to 287.50MHz (287.50)
₿ (10756) bm1370: Setting Frequency to 293.75MHz (294.64)
₿ (10858) bm1370: Setting Frequency to 300.00MHz (300.00)
₿ (10964) bm1370: Setting Frequency to 306.25MHz (307.14)
₿ (11068) bm1370: Setting Frequency to 312.50MHz (312.50)
₿ (11172) bm1370: Setting Frequency to 318.75MHz (319.64)
₿ (11274) bm1370: Setting Frequency to 325.00MHz (325.00)
₿ (11376) bm1370: Setting Frequency to 331.25MHz (332.14)
₿ (11478) bm1370: Setting Frequency to 337.50MHz (337.50)
₿ (11580) bm1370: Setting Frequency to 343.75MHz (344.64)
₿ (11682) bm1370: Setting Frequency to 350.00MHz (350.00)
₿ (11784) bm1370: Setting Frequency to 356.25MHz (357.14)
₿ (11886) bm1370: Setting Frequency to 362.50MHz (362.50)
₿ (11988) bm1370: Setting Frequency to 368.75MHz (369.64)
₿ (12000) power_management: Ignoring invalid temperature reading: -1.0°C
₿ (12090) bm1370: Setting Frequency to 375.00MHz (375.00)
₿ (12192) bm1370: Setting Frequency to 381.25MHz (382.14)
₿ (12294) bm1370: Setting Frequency to 387.50MHz (387.50)
₿ (12396) bm1370: Setting Frequency to 393.75MHz (394.64)
₿ (12498) bm1370: Setting Frequency to 400.00MHz (400.00)
₿ (12600) bm1370: Setting Frequency to 406.25MHz (407.14)
₿ (12702) bm1370: Setting Frequency to 412.50MHz (412.50)
₿ (12804) bm1370: Setting Frequency to 418.75MHz (419.64)
₿ (12906) bm1370: Setting Frequency to 425.00MHz (425.00)
₿ (13008) bm1370: Setting Frequency to 431.25MHz (431.25)
₿ (13110) bm1370: Setting Frequency to 437.50MHz (437.50)
₿ (13212) bm1370: Setting Frequency to 443.75MHz (443.75)
₿ (13314) bm1370: Setting Frequency to 450.00MHz (450.00)
₿ (13416) bm1370: Setting Frequency to 456.25MHz (456.25)
₿ (13518) bm1370: Setting Frequency to 462.50MHz (462.50)
₿ (13620) bm1370: Setting Frequency to 468.75MHz (468.75)
₿ (13722) bm1370: Setting Frequency to 475.00MHz (475.00)
₿ (13804) power_management: Ignoring invalid temperature reading: -1.0°C
₿ (13824) bm1370: Setting Frequency to 481.25MHz (481.25)
₿ (13926) bm1370: Setting Frequency to 487.50MHz (487.50)
₿ (14028) bm1370: Setting Frequency to 493.75MHz (493.75)
₿ (14130) bm1370: Setting Frequency to 500.00MHz (500.00)
₿ (14235) bm1370: Setting Frequency to 506.25MHz (506.25)
₿ (14338) bm1370: Setting Frequency to 512.50MHz (512.50)
₿ (14443) bm1370: Setting Frequency to 518.75MHz (518.75)
₿ (14548) bm1370: Setting Frequency to 525.00MHz (525.00)
₿ (14655) bm1370: Setting Frequency to 525.00MHz (525.00)
₿ (14657) frequency_transition: Successfully transitioned ASIC type 1370 to 525.00 MHz
₿ (14660) bm1370: Setting max baud of 1000000
₿ (14665) serial: Changing UART baud to 1000000
₿ (14670) stratum_task: Starting heartbeat thread for primary pool: pool.satoshiradio.nl:3333
₿ (14671) asic_task: ASIC Job Interval: 500.00 ms
₿ (14670) stratum_task: Opening connection to pool: pool.satoshiradio.nl:3333
₿ (14684) asic_task: ASIC Ready!
₿ (14671) statistics_task: Starting
₿ (14671) main_task: Returned from app_main()
₿ (14718) stratum_task: Connecting to: stratum+tcp://pool.satoshiradio.nl:3333 (144.76.73.244)
₿ (15019) stratum_task: Socket created, connecting to 144.76.73.244:3333
₿ (15037) stratum_task: Resetting stratum uid
₿ (15038) stratum_task: Clean Jobs: clearing queue
₿ (15039) stratum_api: tx: {"id": 1, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}
₿ (15052) stratum_api: tx: {"id": 2, "method": "mining.subscribe", "params": ["bitaxe/BM1370/v2.9.0"]}
₿ (15061) stratum_api: tx: {"id": 3, "method": "mining.authorize", "params": ["bc1quhvnwa70yv59g55h6dp9kmvptcurkw237hqv3n.Bitaxe_Gamma", "PKBitaxe601Gamma3125BTC"]}
₿ (15077) stratum_api: rx: {"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"},"id":1,"error":null}
₿ (15088) stratum_task: Set version mask: 1fffe000
₿ (15094) stratum_api: rx: {"result":[[["mining.notify","67f25062"]],"4c19f267",8],"id":2,"error":null}
₿ (15103) stratum_task: Set extranonce: 4c19f267, extranonce_2_len: 8
₿ (15110) stratum_api: rx: {"params":[1000],"id":null,"method":"mining.set_difficulty"}
₿ (15119) stratum_task: Set pool difficulty: 1000
₿ (15126) stratum_api: rx: {"params":["67ed085a000508ea","cb655f0b04ec1e8d96a8f2e2156a937bdb90f7ac000181fb0000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3c0330d60d000401a3806804d789261a0c","0a636b706f6f6c182f4d696e6564206279205361746f73686920526164696f2fffffffff0256cca61200000000160014e5d93777cf2328545297d3425b6d815e383b39510000000000000000266a24aa21a9ed6553113c406c2787aa657325f3f4be3c2a8f5770b05caf43222af5d4ba6dfc9200000000",["295860b15a203351849c1356c301db50a7c10651e9e2e0906b726de6a60091fa","d0fc227119c1ae1b45a559b0067b48cdfa62cbf6207763277218b569a084123d","38a25de7c2ee771be8c39fd0d0659ae0524423028246d39cc300bd26b53251fe","e7de1a6aad14eb7425ed142c8b53b14b4d87713469b03ee06ca4ab6e3d43ac4a","baf37e96ff70d885225448a31dd98626c66e844703e2294bca8aa9cb29744a60","71931271ff928811c7ce28754c49a1b020c080d16f33605d8e6e7b5473528308","e3dd75afd57b862bbf6decc44a877b6fbc0ebb099090fd076d126fc9014f209e","7e6a6b5540f07deafa86d7ad8af130e733ceec3d2fe3f9abd3f9be6c8b7af194","2ebb33b4f8ca24d4b242c14df9f8632633d2b015577e04c6ad3295a5d71a9969"],"20000000","17023aa6","6880a301",true],"id":null,"method":"mining.notify"}
₿ (15227) system: Syncing clock
₿ (15230) stratum_api: rx: {"params":[1000],"id":null,"method":"mining.set_difficulty"}
₿ (15230) create_jobs_task: New Work Dequeued 67ed085a000508ea
₿ (15239) stratum_task: Set pool difficulty: 1000
₿ (15245) create_jobs_task: New pool difficulty 1000
₿ (15251) stratum_api: rx: {"result":true,"error":null,"id":3}
₿ (15256) create_jobs_task: Set chip version rolls 65535
₿ (15263) stratum_task: setup message accepted
₿ (15274) stratum_api: tx: {"id": 4, "method": "mining.suggest_difficulty", "params": [1000]}
₿ (15609) power_management: PID startup hold phase: 1/3, holding D at: 20.0
₿ (15611) power_management: Temp: 25.2°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:20.0 D_start_val:20.0)
₿ (17421) power_management: PID startup hold phase: 2/3, holding D at: 20.0
₿ (17423) power_management: Temp: 25.1°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:20.0 D_start_val:20.0)
₿ (19234) power_management: PID startup hold phase: 3/3, holding D at: 20.0
₿ (19236) power_management: Temp: 24.9°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:20.0 D_start_val:20.0)
₿ (21046) power_management: PID startup ramp phase: 1/17 (Total cycle: 4), current D: 19.0
₿ (21048) power_management: Temp: 25.4°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:19.0 D_start_val:20.0)
₿ (22861) power_management: PID startup ramp phase: 2/17 (Total cycle: 5), current D: 18.0
₿ (22862) power_management: Temp: 25.2°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:18.0 D_start_val:20.0)
₿ (24377) stratum_task: Stratum response time: 9103.47 ms
₿ (24378) stratum_api: rx: {"params":["67ed085a000508eb","cb655f0b04ec1e8d96a8f2e2156a937bdb90f7ac000181fb0000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3c0330d60d000423a3806804eff5c1390c","0a636b706f6f6c182f4d696e6564206279205361746f73686920526164696f2fffffffff02ad34a81200000000160014e5d93777cf2328545297d3425b6d815e383b39510000000000000000266a24aa21a9ed5c5d74fa95e1a9a6bf70c574ef8f0a934f77fecc7ec434331f8aa590f4f2367c00000000",["295860b15a203351849c1356c301db50a7c10651e9e2e0906b726de6a60091fa","d0fc227119c1ae1b45a559b0067b48cdfa62cbf6207763277218b569a084123d","38a25de7c2ee771be8c39fd0d0659ae0524423028246d39cc300bd26b53251fe","e3681afc3b150850f6f7103d7857c0e0d3f5c33a26b3b7f3b6bb4103053e9f9b","0b9ead8c1cfec3daab3467c8042ffc931686fe718693f65df9c4bd75ee79255a","c389d3f894c209a5d24a18e081e9ac078fe56ae5c043bc7a0a03010bd99fb9c6","c2653237eb7a8cf93629f39ecaabdf9572db9ca65dd12728031b8b92a1044e7d","321657a0d4dd90b0468106b1e11264172eda12b58b18df12c93f9dd157a18eb9","304d17dd243b7de09c3fe5a436bf7cd8402e3679c3255554c21201e60711fcbb","ed484f689431c57a5ed8c3c59f4537b416c8f187e871793fb90f7c63db3fe38d"],"20000000","17023aa6","6880a323",false],"id":null,"method":"mining.notify"}
₿ (24505) create_jobs_task: New Work Dequeued 67ed085a000508eb
₿ (24676) power_management: PID startup ramp phase: 3/17 (Total cycle: 6), current D: 17.0
₿ (24677) power_management: Temp: 25.0°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:17.0 D_start_val:20.0)
₿ (26489) power_management: PID startup ramp phase: 4/17 (Total cycle: 7), current D: 16.0
₿ (26491) power_management: Temp: 25.2°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:16.0 D_start_val:20.0)
₿ (28304) power_management: PID startup ramp phase: 5/17 (Total cycle: 8), current D: 15.0
₿ (28306) power_management: Temp: 24.8°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:15.0 D_start_val:20.0)
₿ (30118) power_management: PID startup ramp phase: 6/17 (Total cycle: 9), current D: 14.0
₿ (30120) power_management: Temp: 25.0°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:14.0 D_start_val:20.0)
₿ (31933) power_management: PID startup ramp phase: 7/17 (Total cycle: 10), current D: 13.0
₿ (31934) power_management: Temp: 25.0°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:13.0 D_start_val:20.0)
₿ (33747) power_management: PID startup ramp phase: 8/17 (Total cycle: 11), current D: 12.0
₿ (33748) power_management: Temp: 25.1°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:12.0 D_start_val:20.0)
₿ (35560) power_management: PID startup ramp phase: 9/17 (Total cycle: 12), current D: 11.0
₿ (35562) power_management: Temp: 25.0°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:11.0 D_start_val:20.0)
₿ (37374) power_management: PID startup ramp phase: 10/17 (Total cycle: 13), current D: 10.0
₿ (37376) power_management: Temp: 24.8°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:10.0 D_start_val:20.0)
₿ (39188) power_management: PID startup ramp phase: 11/17 (Total cycle: 14), current D: 9.0
₿ (39190) power_management: Temp: 25.0°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:9.0 D_start_val:20.0)
₿ (41003) power_management: PID startup ramp phase: 12/17 (Total cycle: 15), current D: 8.0
₿ (41005) power_management: Temp: 24.6°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:8.0 D_start_val:20.0)
₿ (42817) power_management: PID startup ramp phase: 13/17 (Total cycle: 16), current D: 7.0
₿ (42819) power_management: Temp: 24.9°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:7.0 D_start_val:20.0)
₿ (44631) power_management: PID startup ramp phase: 14/17 (Total cycle: 17), current D: 6.0
₿ (44633) power_management: Temp: 24.8°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:6.0 D_start_val:20.0)
₿ (46446) power_management: PID startup ramp phase: 15/17 (Total cycle: 18), current D: 5.0
₿ (46448) power_management: Temp: 24.6°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:5.0 D_start_val:20.0)
₿ (48260) power_management: PID startup ramp phase: 16/17 (Total cycle: 19), current D: 4.0
₿ (48262) power_management: Temp: 25.0°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:4.0 D_start_val:20.0)
₿ (50074) power_management: PID startup phase complete, switching to normal D value: 3.0
₿ (50076) power_management: Temp: 24.5°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
₿ (51889) power_management: Temp: 24.6°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
₿ (53695) power_management: Temp: 24.6°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
₿ (54383) stratum_api: rx: {"params":["67ed085a000508ec","cb655f0b04ec1e8d96a8f2e2156a937bdb90f7ac000181fb0000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3c0330d60d000441a3806804e805223a0c","0a636b706f6f6c182f4d696e6564206279205361746f73686920526164696f2fffffffff023f56ab1200000000160014e5d93777cf2328545297d3425b6d815e383b39510000000000000000266a24aa21a9ed2a9a701c4313f3ee0acc78c2e721c547c5f8a5e83ffb660d9c87d2969979e4e400000000",["295860b15a203351849c1356c301db50a7c10651e9e2e0906b726de6a60091fa","d0fc227119c1ae1b45a559b0067b48cdfa62cbf6207763277218b569a084123d","5752b91c7286ed5e515871efabf285fa7d1569d3c883c3e4eefabcaea8b112cc","5e67391e41a183eef2245680bc6e5d5cf289ef1fd850411d5ef7fb226ebc8c11","68942b69d860f0bf657f5769d40d3ca3ee0b0af81d98eca59d6fa2dd8d4a08c4","26d5489eef121d52a2a8f585fce01607cf7fcf5d46540a5ac9bf2b16cbe74604","c637bcbe8a71765b269171af218b6d8693a092824e2182690fa83a681e3bae92","6002e1d5f62149d459e78bd7262c861ee62dac8448863c3d1dc2fbc1cdbf722c","e6e12f4cba98e477c14bc2354789797147a970e3da79733316c745070300ea2f","41cfb578b696d3939e6af8fdd19f6426ac6aab3680f9555faaaf2fa3e9d4b461"],"20000000","17023aa6","6880a341",false],"id":null,"method":"mining.notify"}
₿ (54567) create_jobs_task: New Work Dequeued 67ed085a000508ec
₿ (55501) power_management: Temp: 24.5°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
₿ (57307) power_management: Temp: 24.6°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
₿ (59113) power_management: Temp: 24.4°C, SetPoint: 60.0°C, Output: 25.0% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)

_____

Does anyone know what the issue could be and how I can fix this? 

I have a Bitaxe Supra with hardware version V2.9.0 
Supra 601

I anyone needs more info, please let me know. 

<img width="1540" height="1180" alt="Image" src="https://github.com/user-attachments/assets/3b75d254-b706-4056-a554-82ac714ae1b9" />




## Comments

### skot on 2025-07-23

Please reach out to the seller for help getting your firmware properly updated. And/or visit the OSMU Discord; https://discord.gg/osmu . Github issues are not for tech support.
