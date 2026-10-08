# bitaxeorg/ESP-Miner issue #105: gracefully handle TCP reset.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/105
> Collected: 2026-10-07
> Published: 2024-02-09

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 105
- State: closed
- Author: CoanLuciano
- Opened: 2024-02-09
- Closed: 2024-11-18
- Labels: help wanted, good first issue

## Description

Hello, I was monitoring my Bitaxe BM1397, V2.0.7 and I got the error below:

I (212912) create_jobs_task: New Work Dequeued 375789
I (242472) bm1397Module: return null
I (242612) stratum_task: rx: {"id":null,"method":"mining.notify","params":["375792","55c17b88e1acafc2d1199e3a8c15bee97e21f673000135200000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff560305a90c194d696e656420627920416e74506f6f6c2000002806bcada723fabe6d6d79cfac63615b2eabbf44c4cf6506ab968ebe6f15e42d13aa8dc8263881a197d91000000000000000","ffffffff05220200000000000017a91442402a28dd61f2718a4b27ae72a4791d5bbdade7874a731e270000000017a9144b09d828dfc8baaba5d04ee77397e04b1050cc73870000000000000000266a24aa21a9ed478acbebb4d4957b971adae1507cbbce233aa44c2d3fdc7e26e020ec60a8e11600000000000000002f6a2d434f52450142fdeae88682a965939fee9b7b2bd5b99694ff645997be5a09d05bb9bac27ec60419d0b373f32b2000000000000000002b6a2952534b424c4f434b3a707efac61e484ac9f57a7c3737f544b6102b03d08e2c97d364d88d24005c99eb00000000",["0a01a44b337a06908c035e6b1649515d63e8ff7839429fc9ff6a692f83bcc9a6","6b6668d6640bbd13be06ca4b341ca07a49f23908b44e2917d116b51dcd272e44","1571db9702c6ef5f79d4119dc3f97ed84ba2865358fc0ec26d6c8bb945ad34aa","ce100a89dc5377d32712ca78c8f37061d0eaafbd2543881a56eb9686977a243d","72100aa8cff05fe72eb8c872d973b954d2b721a4180bead2471e8a5b63419cc9","4219770a598bfe80b6f4d7ca0df42a03af71c83704c456db302fe4314f86dadd","3bd423c70529fafe74ea5c318f2a232b46f86acdca7ca05a6b0380c9967381c5","601ac6dabbd7357b44b550854d548ae70fcd1a5fbe20b8506d8b466f992f259f","7cdf2634737d24e826ef99a5fa996636c61ee83036fc6aa071bda6c371e288a3","bc38fef65d96dda645271a069ddb66d9e31f2f08aea660bbb4ff7fa6b665bb88","e9ee78c173bc5fa4c5f569ba7dca8a25997081e58ec0d93cb56edd00058ac64e","0c93dd124034e5ba39f83e56c1a6613f0e6eb9929198490b9fda8ebf2d6758d9"],"20000000","1703ba5d","65c651df",false]}
**I (242762) create_jobs_task: New Work Dequeued 375792
W (250842) httpd_txrx: httpd_sock_err: error in recv : 104
W (250852) httpd_txrx: httpd_sock_err: error in send : 128
W (250852) httpd_txrx: httpd_sock_err: error in send : 128
W (250852) httpd_txrx: httpd_sock_err: error in send : 128
W (250862) httpd_txrx: httpd_sock_err: error in send : 128
W (250872) httpd_txrx: httpd_sock_err: error in send : 128

***ERROR*** A stack overflow in task httpd has been detected.**


Backtrace: 0x40375aca:0x3fcb9b30 0x4037dd35:0x3fcb9b50 0x40380ac2:0x3fcb9b70 0x4037f437:0x3fcb9bf0 0x40380bd0:0x3fcb9c10 0x40380bc6:0x00000000 |<-CORRUPTED


After few moments the board rebooted normally and goes back to work. But it´s happening often. Almost every hour. I have a good power source (5A capable) as we can see at the picture:
![image](https://github.com/skot/ESP-Miner/assets/98968954/64d252b4-56dc-447a-a1ca-eb57d8b75118)

I am using my board with Antpool. (ss.antpool.com:3333)

The problem does not happens when I use Public Pool. (public-pool.io:21496)

## Comments

### n0rthranger on 2024-02-10

Had something similar ![image](https://github.com/skot/ESP-Miner/assets/62068896/9006486e-c0b7-42ed-8102-ea9e668924e6)

### CoanLuciano on 2024-02-16

I realized that the ESP32 reboots every time it looses wi-fi connection.

I (395203) create_jobs_task: New Work Dequeued 2163854
I (401093) asic_result: Nonce difficulty 42857.12 of 16384.
I (401103) stratum_api: tx: {"id": 6, "method": "mining.submit", "params": ["Bitaxe-bitaxe", "2163854", "4002000000000000", "65cf65af",                                  "f8aa0bb7", "00004000"]}

I (401303) stratum_task: rx: {"error":null,"id":6,"result":true}
I (401303) stratum_task: message result accepted
I (403743) asic_result: Nonce difficulty 82788.32 of 16384.
I (403743) stratum_api: tx: {"id": 7, "method": "mining.submit", "params": ["Bitaxe-bitaxe", "2163854", "4903000000000000", "65cf65af",                                  "7a9d068e", "00006000"]}

I (403963) stratum_task: rx: {"error":null,"id":7,"result":true}
I (403963) stratum_task: message result accepted
I (409963) wifi:state: run -> init (2c0)
I (409963) wifi:pm stop, total sleep time: 347750115 us / 408988004 us

I (409963) wifi:<ba-del>idx:0, tid:0
I (409963) wifi:new:<3,0>, old:<3,1>, ap:<255,255>, sta:<3,1>, prof:1
I (410973) wifi station: Retrying WiFi connection...
recv: Software caused connection abort
I (410973) wifi:flush txq
I (410973) wifi:stop sw txq
I (410973) wifi:lmac stop hw txq
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0x3 (RTC_SW_SYS_RST),boot:0x28 (SPI_FAST_FLASH_BOOT)
Saved PC:0x4037b8a2
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce3818,len:0x16e0
load:0x403c9700,len:0x4
load:0x403c9704,len:0xc00
load:0x403cc700,len:0x2eb0
entry 0x403c9908
I (26) boot: ESP-IDF v5.1 2nd stage bootloader
I (26) boot: compile time Jan 20 2024 20:00:30
I (26) boot: Multicore bootloader
I (29) boot: chip revision: v0.2
I (33) boot.esp32s3: Boot SPI Speed : 80MHz
I (38) boot.esp32s3: SPI Mode       : DIO
I (43) boot.esp32s3: SPI Flash Size : 16MB
I (47) boot: Enabling RNG early entropy source...
I (53) boot: Partition Table:
I (56) boot: ## Label            Usage          Type

### skot on 2024-02-16

Perhaps inelegant, but definitely effective.

### skot on 2024-02-16

this seems related to #102 and could definitely use some attention!

### CoanLuciano on 2024-02-19

I have been debugging this question using my router tools. I have a Mikrotik AP providing wi-fi to my bitaxe.
I´ve been receiving this message every time bitaxe goes down:

84:FC:E6:6C:90:E8@wlan1: disconnected, received disassoc: sending station leaving (8), signal strength -30
In bitaxe I get the info posted above.

Bitaxe is pretty close to my AP. 2 meters away.
Signal strength varies (-20 to -40).

### CoanLuciano on 2024-02-21

I realized that the problem occurs when the pool server disconnects.
I was tcpdumping and I got a TCP RST from antpool server, then bitaxe rebooted! 

### skot on 2024-02-21

Wow! Good catch. Maybe Antpool is suggesting you use a better pool 😂

We should more gracefully handle TCP reset.
