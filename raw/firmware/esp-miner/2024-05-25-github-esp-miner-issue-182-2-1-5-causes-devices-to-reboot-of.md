# bitaxeorg/ESP-Miner issue #182: 2.1.5 causes devices to reboot often with no obvious errors

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/182
> Collected: 2026-10-07
> Published: 2024-05-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 182
- State: closed
- Author: HypeLaser
- Opened: 2024-05-25
- Closed: 2024-06-04
- Labels: none

## Description

I upgraded from 2.1.4 to 2.1.5 this afternoon when I noticed a message on Reddit about the new firmware. Things seemed fine, until I checked all devices together on the Swam page. Even though all 4 BitAxes were powered off and on again by one plug socket after they were updated, so they all booted at the same time, they all showed different "uptimes" on the swarm page after an hour or so. It was clear that devices were stopping (logs stopped displaying) and the devices were rebooting (uptime changed to "now").


**To Reproduce**

To replicate, upgrade several devices on the same network, and keep an eye on the Swarm function to see which ones have shorter or reset uptimes. Is the device rebooting after each time it re-connects to the wifi?


**Expected behaviour**
The devices should not be rebooting unless there is fault or manual intervention. Rolling back to 2.1.4 has stopped the issue.

**Hardware (please complete the following information):**
 - Bitaxe HW version: 1x Ultra 204, 3x Supra 401
 - ESP-Miner FW version: 2.1.5
 - Hash Frequency: stock
 - Voltage: stock


**Additional context**
I opened up 4x browsers and monitored the logs of all 4 devices at the same time. There were no obvious errors in the log outputs, no warnings or errors. The log just stops scrolling. When I then check the Swarm page, the device has shown to have reset. Refreshing the browser for that device then brings up the new log, with no new details on it.

As a side note, the "Stop Scrolling" button doesn't seem to do as advertised. As new information appears in the serial log, the text continues to scroll.


## Comments

### Shen on 2024-05-26

I also have reboot-problems with my two Supras (400/401) and FW version 2.1.5. (but maybe also 2.1.4)
I tried different frequency and voltage.

I connected with https://wantclue.github.io/bitaxe-web-flasher/ and observed the logs. i get the following message before every reboot without doing anything:
http_server: Restarting System because of API Request

I downgraded to 2.1.0 and it seems to work now.

### github-block on 2024-05-26

Bitaxe 202 here, and also getting the same issue, rebooting continuously every 30-45 seconds:

₿ (45999) http_server: Restarting System because of API Request

Downgraded to 2.1.1 and it is working again 


### Alanllopart93 on 2024-05-26

Me pasa lo mismo con 3 Bitaxe Ultra se reinician 

### solobito on 2024-05-26

It also occurs to me. I can't find a pattern, it restarts every few hours or minutes. 

I have managed to capture a reboot using the screen command via USB.

Before reboot it shows the following:

`***ERROR*** A stack overflow in task httpd has been detected.`

This is the part of the log before the reboot:

```
[32mI (863498) stratum_task: rx: {"params":["6485163800102eac","b1b7dbb9c37206e42854a5fb323246b0d5ad69370002d54d0000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff35039ce50c00046efb52660423e9f50a0c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff03c8c01713000000001600142169afb89eba1511bd503418f3cfd73bc2889f4b04c063000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9edab55bc1198952b92d42494130b1b1ae19238921383421237ea0f074890c2d2f900000000",["ddfbef77ece20a25b442d1d496374df0a06cd49ce54ecc4762937d913e49c75c","a38c3a3bdbbf65099f40222b9a55bc68268880dd56cdc361307c670b9cf6b311","ada6e302f28cb03aa9adfbd70f2e22b507e873e418d453bc240bf1b380f63a3e","2e2859389f90dd5f8ddcc99b3a3223a96d8f21832744170b7915c20200ec5355","5f73e436f21bc8f70f342e4125be7099d75658a376a0eb346ff55f756d306df4","51da028bff002206c651ce8bff18840950277b5bf7c688b466ee8179700b7212","4909d04ab859ebce607697ccebbc36972fad96767ae96e69698674f51e755c42","1320f84834ffeb2ac86f262e2946816f13a72def98868e15103de6f4efa6ae61","e94daaa79de5003c2a6eade51298c5ae6d082a4f73604b3102540acacca7c545","b4c6c5dbe4af555ee968507bca459cd8c415a9a90fb5c075b3a3f9bb2c34cbac","6ce0409ce80cf83614631f86cb8b01eb21a759d2e1f32a829737c8b89c516e08","c975523f986ff40111db1f364f8f285c397ebbbddb69ae56ddb6b0064e325f9e","8679cc435dca4b3f9df39ea823b6549a1d06cc4597dc16419c250182f60ef5b9"],"20000000","170355f0","6652fb6e",false],"id":null,"method":"mining.notify"}[39m
[32mI (863638) create_jobs_task: New Work Dequeued 6485163800102eac[39m
[32mI (864808) bm1368Module: Job ID: D5[39m
[32mI (864808) bm1368Module: RX Job ID: 68[39m
[32mI (864808) asic_result: Nonce difficulty 564.61 of 535.[39m
[32mI (864818) stratum_api: tx: {"id": 178, "method": "mining.submit", "params": ["bc1qy956lwy7hg23r02sxsv08n7h80pg386t6gwh3k.bitaxe", "6485163800102eac", "6700000000000000", "6652fb6e", "aaec4874", "0000a000"]}
[39m

[32mI (864988) stratum_task: rx: {"result":true,"error":null,"id":178}[39m
[32mI (864988) stratum_task: message result accepted[39m
[32mI (865308) bm1368Module: Job ID: 63[39m
[32mI (865308) bm1368Module: RX Job ID: 30[39m
[32mI (865318) asic_result: Nonce difficulty 370.14 of 535.[39m
[32mI (867678) bm1368Module: Job ID: A2[39m
[32mI (867678) bm1368Module: RX Job ID: 50[39m
[32mI (867678) asic_result: Nonce difficulty 2911.99 of 535.[39m
[32mI (867688) stratum_api: tx: {"id": 179, "method": "mining.submit", "params": ["bc1qy956lwy7hg23r02sxsv08n7h80pg386t6gwh3k.bitaxe", "6485163800102eac", "8601000000000000", "6652fb6e", "0a5a4322", "00004000"]}
[39m

[32mI (867808) stratum_task: rx: {"result":true,"error":null,"id":179}[39m
[32mI (867818) stratum_task: message result accepted[39m
[33mW (868778) httpd_txrx: httpd_sock_err: error in recv : 104[39m
[33mW (868778) httpd_txrx: httpd_sock_err: error in send : 104[39m
[33mW (868778) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (868788) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (868788) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (868798) httpd_txrx: httpd_sock_err: error in send : 128[39m

***ERROR*** A stack overflow in task httpd has been detected.


Backtrace: 0x40375b42:0x3fcbc2f0 0x4037d4a1:0x3fcbc310 0x4037e45a:0x3fcbc330 0x4037f88b:0x3fcbc3b0 0x4037e520:0x3fcbc3d0 0x4037e516:0x3fcbc3f0 0x3fca4895:0x00060f23 |<-CORRUPTED




ELF file SHA256: aba1889a2

Rebooting...
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0xc (RTC_SW_CPU_RST),boot:0x2a (SPI_FAST_FLASH_BOOT)
Saved PC:0x40375ab8
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce3810,len:0x178c
load:0x403c9700,len:0x4
load:0x403c9704,len:0xcbc
load:0x403cc700,len:0x2da0
entry 0x403c9914
[32mI (26) boot: ESP-IDF v5.2.1 2nd stage bootloader[39m
[32mI (26) boot: compile time May 24 2024 20:02:33[39m
[32mI (26) boot: Multicore bootloader[39m
[32mI (29) boot: chip revision: v0.2[39m
[32mI (33) boot.esp32s3: Boot SPI Speed : 80MHz[39m
[32mI (38) boot.esp32s3: SPI Mode       : DIO[39m
[32mI (43) boot.esp32s3: SPI Flash Size : 16MB[39m

```



### adadnc on 2024-05-26

I've a Supra here with PCB 400 on the Silkscreen, but the UI shows 401. With the FW 2.1.5 I had two reboots within 8h over night.

### solobito on 2024-05-26

It is possible to view the logs by connecting the USB cable directly to the PC or Mac. This way you can see more information in the logs. https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/establish-serial-connection.html

On MacOS
```
ls /dev/cu.*
screen /dev/cu.device_name 115200
```

To save the logs to a file you can use this command:

```
script -a -t 0 screen-output.log screen /dev/cu.device_name 115200
```

### HypeLaser on 2024-05-26

> It is possible to view the logs by connecting the USB cable directly to the PC or Mac. This way you can see more information in the logs. https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/establish-serial-connection.html
> 
> On MacOS
> 
> ```
> ls /dev/cu.*
> screen /dev/cu.device_name 115200
> ```
> 
> To save the logs to a file you can use this command:
> 
> ```
> script -a -t 0 screen-output.log screen /dev/cu.device_name 115200
> ```

Thank you for this, I expected the "realtime log" via the web interface to show the same data. Mine are installed in the attic, so not something I want to be going up and checking often. I made the assumption the data appearing on the realtime logs was the same info. A lesson learned.

### cpowell220 on 2024-05-26

I downgraded back to 2.1.3 because out of 13x Supra v401's I had 6 randomly rebooting regardless of clock speeds/etc. a few of them couldn't run for more than a minute before rebooting. I had a few random little issues with some of them on 2.1.4 as well.

### benjamin-wilson on 2024-05-26

> I downgraded back to 2.1.3 because out of 13x Supra v401's I had 6 randomly rebooting regardless of clock speeds/etc. a few of them couldn't run for more than a minute before rebooting. I had a few random little issues with some of them on 2.1.4 as well.

What pool are you using? Are you monitoring them via axeOS when they reboot? 

### benjamin-wilson on 2024-05-26

I am working on reproducing the issue but so far no luck 

### cpowell220 on 2024-05-26

> > I downgraded back to 2.1.3 because out of 13x Supra v401's I had 6 randomly rebooting regardless of clock speeds/etc. a few of them couldn't run for more than a minute before rebooting. I had a few random little issues with some of them on 2.1.4 as well.
> 
> What pool are you using? Are you monitoring them via axeOS when they reboot?

It did it on Kano/CKpool. I will try to replicate later on others.  I initially was seeing it on Swarm (but I know sometimes it does weird things), then direct connect to the IP and sure enough under Logs it would be at 1 minute uptime.

Some of them were completely fine, and the other ones no matter what I did they would have the same issue. Though when looking at Unifi's wifi stuff on all the devices (none of them are reconnecting) so the reboots its doing it fast enough where none of the devices are reporting downtime.  In fact it's funny because temps/hashrate/etc were all normal it was just the constant reboots while the others had been 5-6 hours each.

### benjamin-wilson on 2024-05-26

https://github.com/skot/ESP-Miner/releases/tag/v2.1.6

If someone could try this release and let me know if the issue persists (ideally with logs) 

### adadnc on 2024-05-26

> https://github.com/skot/ESP-Miner/releases/tag/v2.1.6
> 
> If someone could try this release and let me know if the issue persists (ideally with logs)

I've just upgraded to v2.1.6 and it reboots more often than with 2.1.5. I had it running for 3minutes, than for 6minutes.

### solobito on 2024-05-26

I just installed the **esp-miner-factory-401-v2.1.6.bin** file and it has restarted again.

I see the logs in two ways:

- Using the screen command (via USB connection)
- Using a websocket connection (I use a Python script) (There is no great information here.)

### Logs from the USB (it restarts after sowing "A stack overflow in task httpd has been detected.")
```
[32mI (326961) bm1368Module: Job ID: C3[39m
[32mI (327011) bm1368Module: RX Job ID: 60[39m
[32mI (327011) asic_result: Nonce difficulty 66737.97 of 10000.[39m
[32mI (327011) stratum_api: tx: {"id": 11, "method": "mining.submit", "params": ["bc1qu032m2wuvtachz8ds5ew9zx3mmk2l9l40zfkl2.bitaxe", "64851638001033a5", "c00b000000000000", "665388c3", "026b114a", "00006000"]}
[39m

[32mI (327021) create_jobs_task: New Work Dequeued 64851638001033a6[39m
[32mI (327181) stratum_task: rx: {"result":true,"error":null,"id":11}[39m
[32mI (327181) stratum_task: message result accepted[39m
[32mI (328431) bm1368Module: Job ID: 5E[39m
[32mI (328441) bm1368Module: RX Job ID: 28[39m
[32mI (328441) asic_result: Nonce difficulty 271.32 of 10000.[39m
[32mI (328771) bm1368Module: Job ID: BB[39m
[32mI (328781) bm1368Module: RX Job ID: 58[39m
[32mI (328781) asic_result: Nonce difficulty 1081.81 of 10000.[39m
[32mI (334741) bm1368Module: Job ID: 74[39m
[32mI (334741) bm1368Module: RX Job ID: 38[39m
[32mI (334741) asic_result: Nonce difficulty 347.67 of 10000.[39m
[32mI (337131) bm1368Module: Job ID: 75[39m
[32mI (337141) bm1368Module: RX Job ID: 38[39m
[32mI (337141) asic_result: Nonce difficulty 651.15 of 10000.[39m
[32mI (340971) bm1368Module: Job ID: 7D[39m
[32mI (340971) bm1368Module: RX Job ID: 38[39m
[32mI (340981) asic_result: Nonce difficulty 1439.21 of 10000.[39m
[32mI (342321) bm1368Module: Job ID: C7[39m
[32mI (342321) bm1368Module: RX Job ID: 60[39m
[32mI (342331) asic_result: Nonce difficulty 1144.79 of 10000.[39m
[32mI (342441) bm1368Module: Job ID: DD[39m
[32mI (342441) bm1368Module: RX Job ID: 68[39m
[32mI (342441) asic_result: Nonce difficulty 305.74 of 10000.[39m
[33mW (347231) httpd_txrx: httpd_sock_err: error in recv : 104[39m
[33mW (347231) httpd_txrx: httpd_sock_err: error in send : 104[39m
[33mW (347231) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (347241) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (347241) httpd_txrx: httpd_sock_err: error in send : 128[39m

***ERROR*** A stack overflow in task httpd has been detected.


Backtrace: 0x40375b42:0x3fcbbbc0 0x4037d4a1:0x3fcbbbe0 0x4037e45a:0x3fcbbc00 0x4037f88b:0x3fcbbc80 0x4037e520:0x3fcbbca0 0x4037e516:0x3fcbbc24 |<-CORRUPTED




ELF file SHA256: aa00b2217

Rebooting...
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0xc (RTC_SW_CPU_RST),boot:0x2a (SPI_FAST_FLASH_BOOT)
Saved PC:0x40375ab8
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce3810,len:0x178c
load:0x403c9700,len:0x4
load:0x403c9704,len:0xcbc
load:0x403cc700,len:0x2da0
entry 0x403c9914
[32mI (26) boot: ESP-IDF v5.2.1 2nd stage bootloader[39m
[32mI (26) boot: compile time May 26 2024 14:45:13[39m
[32mI (26) boot: Multicore bootloader[39m
[32mI (29) boot: chip revision: v0.2[39m
[32mI (33) boot.esp32s3: Boot SPI Speed : 80MHz[39m
[32mI (38) boot.esp32s3: SPI Mode       : DIO[39m
[32mI (43) boot.esp32s3: SPI Flash Size : 16MB[39m
[32mI (47) boot: Enabling RNG early entropy source...[39m
[32mI (53) boot: Partition Table:[39m
[32mI (56) boot: ## Label            Usage          Type ST Offset   Length[39m
[32mI (64) boot:  0 nvs              WiFi data        01 02 00009000 00006000[39m
[32mI (71) boot:  1 phy_init         RF data          01 01 0000f000 00001000[39m
[32mI (79) boot:  2 factory          factory app      00 00 00010000 00400000[39m
[32mI (86) boot:  3 www              Unknown data     01 82 00410000 00300000[39m
[32mI (94) boot:  4 ota_0            OTA app          00 10 00710000 00400000[39m
[32mI (101) boot:  5 ota_1            OTA app          00 11 00b10000 00400000[39m
[32mI (109) boot:  6 otadata          OTA data         01 00 00f10000 00002000[39m
[32mI (116) boot:  7 coredump         Unknown data     01 03 00f12000 00010000[39m
[32mI (124) boot: End of partition table[39m
[32mI (128) boot: Defaulting to factory image[39m
[32mI (133) esp_image: segment 0: paddr=00010020 vaddr=3c0b0020 size=2ca08h (182792) map[39m
[32mI (174) esp_image: segment 1: paddr=0003ca30 vaddr=3fc99500 size=035e8h ( 13800) load[39m
[32mI (177) esp_image: segment 2: paddr=00040020 vaddr=42000020 size=aaf60h (700256) map[39m
[32mI (305) esp_image: segment 3: paddr=000eaf88 vaddr=3fc9cae8 size=01818h (  6168) load[39m
[32mI (307) esp_image: segment 4: paddr=000ec7a8 vaddr=40374000 size=15414h ( 87060) load[39m
[32mI (339) boot: Loaded app from partition at offset 0x10000[39m
[32mI (339) boot: Disabling RNG early entropy source...[39m
[32mI (350) cpu_start: Multicore app[39m
[32mI (360) cpu_start: Pro cpu start user code[39m
[32mI (360) cpu_start: cpu freq: 160000000 Hz[39m
[32mI (360) cpu_start: Application information:[39m
[32mI (363) cpu_start: Project name:     esp-miner[39m
[32mI (368) cpu_start: App version:      v2.1.6[39m
[32mI (373) cpu_start: Compile time:     May 26 2024 14:44:58[39m
[32mI (379) cpu_start: ELF file SHA256:  aa00b2217...[39m
[32mI (385) cpu_start: ESP-IDF:          v5.2.1[39m
[32mI (389) cpu_start: Min chip rev:     v0.0[39m
[32mI (394) cpu_start: Max chip rev:     v0.99 [39m
[32mI (399) cpu_start: Chip rev:         v0.2[39m
[32mI (404) heap_init: Initializing. RAM available for dynamic allocation:[39m
[32mI (411) heap_init: At 3FCA3B70 len 00045BA0 (278 KiB): RAM[39m
[32mI (417) heap_init: At 3FCE9710 len 00005724 (21 KiB): RAM[39m
[32mI (423) heap_init: At 3FCF0000 len 00008000 (32 KiB): DRAM[39m
[32mI (429) heap_init: At 600FE010 len 00001FD8 (7 KiB): RTCRAM[39m
[32mI (437) spi_flash: detected chip: gd[39m
[32mI (440) spi_flash: flash io: dio[39m
[33mW (444) i2c: This driver is an old driver, please migrate your application code to adapt `driver/i2c_master.h`[39m
[33mW (455) ADC: legacy driver is deprecated, please migrate to `esp_adc/adc_oneshot.h`[39m
[32mI (463) sleep: Configure to isolate all GPIO pins in sleep state[39m
[32mI (470) sleep: Enable automatic switching of GPIO sleep configuration[39m
[32mI (477) main_task: Started on CPU0[39m
[32mI (487) main_task: Calling app_main()[39m
[32mI (527) miner: NVS_CONFIG_ASIC_FREQ 490.000000[39m
[32mI (527) miner: ASIC: BM1368[39m
[32mI (527) miner: Welcome to the bitaxe![39m

```

**For some strange reason in my Python script I get the error (cannot decode )for Job ID: C3, then it restarts again.** I'm not sure if this is related, but I've seen it happen a couple of times and then it restarts.

```
2024-05-26 21:09:18: [0;32mI (324031) asic_result: Nonce difficulty 571.76 of 10000.[0m

2024-05-26 21:09:19: [0;32mI (324941) bm1368Module: Job ID: EF[0m

2024-05-26 21:09:19: [0;32mI (324941) bm1368Module: RX Job ID: 70[0m

2024-05-26 21:09:19: [0;32mI (324951) asic_result: Nonce difficulty 319.38 of 10000.[0m

2024-05-26 21:09:21: cannot decode: b'\x81~\x05\xd6\x1b[0;32mI (326961) bm1368Module: Job ID: C3\x1b'
2024-05-26 21:10:12: Opened connection
2024-05-26 21:10:13: [0;32mI (31267) bm1368Module: Job ID: 5F[0m

2024-05-26 21:10:13: [0;32mI (31277) bm1368Module: RX Job ID: 28[0m

2024-05-26 21:10:13: [0;32mI (31277) asic_result: Nonce difficulty 387.71 of 8192.[0m
```

### tdb3 on 2024-05-28

Similar log messages seen here https://github.com/jomjol/AI-on-the-edge-device/issues/1869

May or may not be related.

### tdb3 on 2024-05-28

I don't have BitAxe hardware to test on, but some ideas:
 
While not a solution, perhaps a band-aid to try might be to play with stack_size used by httpd.  

See https://docs.espressif.com/projects/esp-idf/en/v5.2.1/esp32s3/api-reference/protocols/esp_http_server.html#overview
 > The task priority and stack size are configurable during server instance creation by passing httpd_config_t structure to httpd_start()
   
https://github.com/skot/ESP-Miner/blob/00d5a7386f259967c6fdccfcd0cb432d2008e756/main/http_server/http_server.c#L586-L591
   
Could maybe find the default `stack_size` in `config` and adjust to a reasonably larger value.  This isn't a full-on solution, but might might make the stack overflow less likely.

For example:
```diff
diff --git a/main/http_server/http_server.c b/main/http_server/http_server.c
index 7dd07c9..ebe17b5 100644
--- a/main/http_server/http_server.c
+++ b/main/http_server/http_server.c
@@ -586,6 +586,8 @@ esp_err_t start_rest_server(void * pvParameters)
     httpd_config_t config = HTTPD_DEFAULT_CONFIG();
     config.uri_match_fn = httpd_uri_match_wildcard;
     config.max_uri_handlers = 20;
+    ESP_LOGI(TAG, "HTTP config.stack_size=%d", config.stack_size);
+    config.stack_size = <reasonably larger value>;
 
     ESP_LOGI(TAG, "Starting HTTP Server");
     REST_CHECK(httpd_start(&server, &config) == ESP_OK, "Start server failed", err_start);
```

Of course, I could be way off on this, and I'm new to the project, but it seems like it might be related.



### benjamin-wilson on 2024-05-28

I've been able to reproduce the problem although it's intermittent which makes it hard. The httpx error is unrelated and fixed already. I'll be rolling back checkins to narrow it down but it's going to take awhile 

### Shen on 2024-05-28

I updated to 2.1.6. There are still often reboots. I monitored with Putty:


```
I (508539) stratum_task: rx: {"result":true,"error":null,"id":74}
I (508539) stratum_task: message result accepted
I (508649) bm1368Module: Job ID: 75
I (508649) bm1368Module: RX Job ID: 38
I (508649) asic_result: Nonce difficulty 367.17 of 280.
I (508659) stratum_api: tx: {"id": 76, "method": "mining.submit", "params": ["BC_ADRESS", "64851638001045e6", "7601000000000000", "6655949c", "ff942968", "0000a000"]}

Guru Meditation Error: Core  0 panic'ed (Interrupt wdt timeout on CPU0).

Core  0 register dump:
PC      : 0x40377637  PS      : 0x00050434  A0      : 0x3fcc7c90  A1      : 0x3fc9bd90
A2      : 0x00021001  A3      : 0x00039041  A4      : 0x000637ff  A5      : 0x3fc9bd50
A6      : 0x3fcaa788  A7      : 0x0000cdcd  A8      : 0x00000000  A9      : 0x4037e496
A10     : 0x00000008  A11     : 0x00000000  A12     : 0x00000000  A13     : 0x60013000
A14     : 0x00060223  A15     : 0x00000003  SAR     : 0x00000007  EXCCAUSE: 0x00000005
EXCVADDR: 0x00000000  LBEG    : 0x40056f5c  LEND    : 0x40056f72  LCOUNT  : 0x00000000
Core  0 was running in ISR context:
EPC1    : 0x420a1edb  EPC2    : 0x40377c47  EPC3    : 0x00000000  EPC4    : 0x40377637


Backtrace: 0x40377634:0x3fc9bd90 0x3fcc7c8d:0x3fcc7d50 |<-CORRUPTED


Core  1 register dump:
PC      : 0x4037acee  PS      : 0x00060f34  A0      : 0x82005025  A1      : 0x3fca8770
A2      : 0x00000000  A3      : 0x00000001  A4      : 0x8037e412  A5      : 0x3fcbd660
A6      : 0x00060023  A7      : 0x00000003  A8      : 0x82021022  A9      : 0x3fca8730
A10     : 0x00000000  A11     : 0x00000001  A12     : 0x8037e412  A13     : 0x3fcc5700
A14     : 0x00060023  A15     : 0x3fca8938  SAR     : 0x00000000  EXCCAUSE: 0x00000005
EXCVADDR: 0x00000000  LBEG    : 0x00000000  LEND    : 0x00000000  LCOUNT  : 0x00000000


Backtrace: 0x4037aceb:0x3fca8770 0x42005022:0x3fca8790 0x4037f279:0x3fca87b0 0x4037e069:0x3fca87d0




ELF file SHA256: aa00b2217

Rebooting...
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0xc (RTC_SW_CPU_RST),boot:0x2a (SPI_FAST_FLASH_BOOT)
Saved PC:0x40375ab8
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce3818,len:0x16e0
load:0x403c9700,len:0x4
load:0x403c9704,len:0xc00
load:0x403cc700,len:0x2eb0
entry 0x403c9908
I (26) boot: ESP-IDF v5.1 2nd stage bootloader
I (26) boot: compile time Mar  3 2024 19:55:36
I (27) boot: Multicore bootloader
I (29) boot: chip revision: v0.2
I (33) boot.esp32s3: Boot SPI Speed : 80MHz
I (38) boot.esp32s3: SPI Mode       : DIO
I (43) boot.esp32s3: SPI Flash Size : 16MB
I (47) boot: Enabling RNG early entropy source...
I (53) boot: Partition Table:
I (56) boot: ## Label            Usage          Type ST Offset   Length
I (64) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (71) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (79) boot:  2 factory          factory app      00 00 00010000 00400000
I (86) boot:  3 www              Unknown data     01 82 00410000 00300000
I (93) boot:  4 ota_0            OTA app          00 10 00710000 00400000
I (101) boot:  5 ota_1            OTA app          00 11 00b10000 00400000
I (108) boot:  6 otadata          OTA data         01 00 00f10000 00002000
I (116) boot:  7 coredump         Unknown data     01 03 00f12000 00010000
I (124) boot: End of partition table
I (128) esp_image: segment 0: paddr=00710020 vaddr=3c0b0020 size=2ca08h (182792) map
I (169) esp_image: segment 1: paddr=0073ca30 vaddr=3fc99500 size=035e8h ( 13800) load
I (173) esp_image: segment 2: paddr=00740020 vaddr=42000020 size=aaf60h (700256) map
I (301) esp_image: segment 3: paddr=007eaf88 vaddr=3fc9cae8 size=01818h (  6168) load
I (303) esp_image: segment 4: paddr=007ec7a8 vaddr=40374000 size=15414h ( 87060) load
I (335) boot: Loaded app from partition at offset 0x710000
I (335) boot: Disabling RNG early entropy source...
I (346) cpu_start: Multicore app
I (356) cpu_start: Pro cpu start user code
I (356) cpu_start: cpu freq: 160000000 Hz
I (357) cpu_start: Application information:
I (359) cpu_start: Project name:     esp-miner
I (364) cpu_start: App version:      v2.1.6
I (369) cpu_start: Compile time:     May 26 2024 14:44:58
I (375) cpu_start: ELF file SHA256:  aa00b2217...
I (381) cpu_start: ESP-IDF:          v5.2.1
I (386) cpu_start: Min chip rev:     v0.0
I (390) cpu_start: Max chip rev:     v0.99
I (395) cpu_start: Chip rev:         v0.2
I (400) heap_init: Initializing. RAM available for dynamic allocation:
I (407) heap_init: At 3FCA3B70 len 00045BA0 (278 KiB): RAM
I (413) heap_init: At 3FCE9710 len 00005724 (21 KiB): RAM
I (419) heap_init: At 3FCF0000 len 00008000 (32 KiB): DRAM
I (426) heap_init: At 600FE010 len 00001FD8 (7 KiB): RTCRAM
I (433) spi_flash: detected chip: gd
I (436) spi_flash: flash io: dio
W (440) i2c: This driver is an old driver, please migrate your application code to adapt `driver/i2c_master.h`
W (451) ADC: legacy driver is deprecated, please migrate to `esp_adc/adc_oneshot.h`
I (459) sleep: Configure to isolate all GPIO pins in sleep state
I (466) sleep: Enable automatic switching of GPIO sleep configuration
I (473) main_task: Started on CPU0
I (483) main_task: Calling app_main()
I (523) miner: NVS_CONFIG_ASIC_FREQ 490.000000
I (523) miner: ASIC: BM1368
I (523) miner: Welcome to the bitaxe!
I (523) SystemModule: I2C initialized successfully
I (533) DS4432U.c: Set ASIC voltage = 1.200V [0xC6]
I (533) DS4432U.c: Writing 0xC6
I (543) pp: pp rom version: e7ae62f
I (543) net80211: net80211 rom version: e7ae62f
I (553) wifi:wifi driver task: 3fcaf2c8, prio:23, stack:6656, core=0
I (573) wifi:wifi firmware version: a9f5b59
I (573) wifi:wifi certification version: v7.0
I (573) wifi:config NVS flash: enabled
I (573) wifi:config nano formating: disabled
I (573) wifi:Init data frame dynamic rx buffer num: 32
I (583) wifi:Init static rx mgmt buffer num: 5
I (583) wifi:Init management short buffer num: 32
I (593) wifi:Init dynamic tx buffer num: 32
I (593) wifi:Init static tx FG buffer num: 2
I (603) wifi:Init static rx buffer size: 1600
I (603) wifi:Init static rx buffer num: 10
I (603) wifi:Init dynamic rx buffer num: 32
I (613) wifi_init: rx ba win: 6
I (613) wifi_init: tcpip mbox: 32
I (623) wifi_init: udp mbox: 6
I (623) wifi_init: tcp mbox: 6
I (623) wifi_init: tcp tx win: 5760
I (633) wifi_init: tcp rx win: 5760
I (633) wifi_init: tcp mss: 1440
I (643) wifi_init: WiFi IRAM OP enabled
I (643) wifi_init: WiFi RX IRAM OP enabled
I (663) wifi station: ESP_WIFI Access Point On
W (663) wifi:Affected by the ESP-NOW encrypt num, set the max connection num to 10
I (663) wifi station: ESP_WIFI_MODE_STA
I (663) wifi station: wifi_init_sta finished.
I (673) phy_init: phy_version 640,cd64a1a,Jan 24 2024,17:28:12
I (713) wifi:mode : sta (dc:da:0c:3a:51:ac) + softAP (dc:da:0c:3a:51:ad)
I (713) wifi:enable tsf
I (713) wifi:Total power save buffer number: 16
I (713) wifi:Init max length of beacon: 752/752
I (723) wifi:Init max length of beacon: 752/752
I (723) esp_netif_lwip: DHCP server started on interface WIFI_AP_DEF with IP: 192.168.4.1
I (733) wifi station: ESP_WIFI setting hostname to: espressif
I (743) wifi station: wifi_init_sta finished.
I (743) wifi:new:<1,1>, old:<1,1>, ap:<1,1>, sta:<1,0>, prof:1
I (753) wifi:state: init -> auth (b0)
I (1123) SystemModule: OLED init success!
I (1393) http_server: Partition size: total: 2884241, used: 664397
I (1393) http_server: Starting HTTP Server
I (1393) example_dns_redirect_server: Socket created
I (1403) example_dns_redirect_server: Socket bound, port 53
I (1403) example_dns_redirect_server: Waiting for data
I (5113) wifi:state: auth -> init (200)
I (5123) wifi:new:<1,0>, old:<1,1>, ap:<1,1>, sta:<1,0>, prof:1
I (7623) wifi station: Retrying WiFi connection...
I (9133) wifi:ap channel adjust o:1,1 n:11,2
I (9133) wifi:new:<11,0>, old:<1,0>, ap:<11,2>, sta:<11,0>, prof:1
I (9143) wifi:state: init -> auth (b0)
I (9923) wifi:state: auth -> assoc (0)
I (9933) wifi:state: assoc -> run (10)
I (9953) wifi:connected with WLAN, aid = 2, channel 11, BW20, bssid = d4:24:dd:12:16:5d
I (9963) wifi:security: WPA3-SAE, phy: bgn, rssi: -43
I (9973) wifi:pm start, type: 1

I (9973) wifi:dp: 1, bi: 102400, li: 3, scale listen interval from 307200 us to 307200 us
I (9983) wifi:set rx beacon pti, rx_bcn_pti: 0, bcn_timeout: 25000, mt_pti: 0, mt_time: 10000
I (9983) wifi:AP's beacon interval = 102400 us, DTIM period = 1
I (10003) wifi:<ba-add>idx:0 (ifx:0, d4:24:dd:12:16:5d), tid:0, ssn:0, winSize:64
I (10993) wifi station: Bitaxe ip:192.168.XX.XX
I (10993) esp_netif_handlers: sta ip: 192.168.XX.XX, mask: 255.255.255.0, gw: 192.168.0.1
I (10993) miner: Connected to SSID: WLAN
I (11003) gpio: GPIO[12]| InputEn: 1| OutputEn: 0| OpenDrain: 0| Pullup: 0| Pulldown: 0| Intr:0
I (10993) wifi station: ESP_WIFI Access Point Off
I (11013) wifi:mode : sta (dc:da:0c:3a:51:ac)
I (11023) serial: Initializing serial
I (11023) bm1368Module: Initializing BM1368
I (12223) bm1368Module: 1 chip(s) detected on the chain
final refdiv: 2, fbdiv: 235, postdiv1: 6, postdiv2: 1, min diff value: 0.416656
I (18723) bm1368Module: Setting Frequency to 490.00MHz (0.01)
I (18723) bm1368Module: Setting max baud of 1000000
I (18723) serial: Changing UART baud to 1000000
I (18733) stratum_task: Get IP for URL: solo.ckpool.org

I (18743) ASIC_task: ASIC Ready!
I (18743) main_task: Returned from app_main()
I (18773) stratum_task: Connecting to: stratum+tcp://solo.ckpool.org:3333 (51.81.56.15)

I (18773) stratum_task: Socket created, connecting to 51.81.56.15:3333
I (19083) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe/BM1368"]}

I (19293) stratum_api: Received result {"result":[[["mining.notify","7405c2c5"]],"4f659b70",8],"id":1,"error":null}
I (19293) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}

I (19313) stratum_api: Received result {"params":[10000],"id":null,"method":"mining.set_difficulty"}
configure_version result null
I (19323) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [1000]}

I (19333) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["BC_ADRESS", "x"]}

I (19503) stratum_task: rx: {"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"},"id":2,"error":null}
I (19503) stratum_task: Set version mask: 1fffe000
I (19703) stratum_task: rx: {"params":["64851638001045e6","93894616f2a42f31c3d5cf16edddcfc7307c69210000c8b60000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3503aee60c00049c94556604a140a10f0c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff030e38da12000000002200201bc038ee5f8759ad75eb703c00d860de2ac75fdb6c2852424845ee1998927da4887e62000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9ed0a33b78255e81cd96cdfd725af8df00965251b6d9c8514b90b9639247d58c36500000000",["80d2e5875a1668106b0f03780b2d998ede122a18f8c082e6f32380b504d82f16","1e851e876ad19703c1304e4dc0fb4487bb27c1c32add434ea196f76c6caac682","3db8b1220abc844459946979bac99a691b43405473e7f63dff29eca085b5f21e","123262a915664aad405c13fc08e09022b719c761ca1a5f2a80842f25f0963e1f","87b08f7bb975d6a8f9c2f47c923db552907725672985637cba7d82b77275f5bb","45ff0578fdc119bf325130d53afc528d613e831c6427c4e82a1a5e953e056567","a8d9ce4903b54b62b4d9fdca4323713b60185408f3bce41501e270748f84d9d0","d5dc5ad4d5b760828667f7281ebae20a6eebe7e6806ec051f847cda3b74d9ae4","d7fdb9c48c63167465e0fbda1cf9b24b8be5dbed96172e1c518ef48f22326237","cf63376e10098f363ef0be1015a346579ef417a8ea4cec9afb3d89189b247a50","ea453211af2b5623c3425f78115edbf9961fb6361072570e49626bb2f4801894","8209c8f966947b98b6f1bcd663c20c6a7aec0ec10a9133f2a9881ce0cb7eca1f","c40963475010373bdaed2d703c6211566e73392b89081fd06cb9052e3af89aad"],"20000000","170355f0","6655949c",true],"id":null,"method":"mining.notify"}
I (19823) SystemModule: Syncing clock
I (19833) create_jobs_task: New Work Dequeued 64851638001045e6
I (19833) stratum_task: rx: {"params":[10000],"id":null,"method":"mining.set_difficulty"}
I (19843) stratum_task: Set stratum difficulty: 10000
I (19853) stratum_task: rx: {"result":true,"error":null,"id":4}
I (19853) stratum_task: message result accepted
I (21113) bm1368Module: Job ID: 03
I (21113) bm1368Module: RX Job ID: 00
I (21113) asic_result: Nonce difficulty 546.97 of 8192.
```

And a second one:

```
I (7061534) bm1368Module: Job ID: 71
I (7061534) bm1368Module: RX Job ID: 38
I (7061534) asic_result: Nonce difficulty 486.56 of 533.
I (7061684) stratum_task: rx: {"result":true,"error":null,"id":1825}
I (7061694) stratum_task: message result accepted
I (7062324) bm1368Module: Job ID: 44
I (7062324) bm1368Module: RX Job ID: 20
I (7062324) asic_result: Nonce difficulty 365.81 of 533.
I (7062814) bm1368Module: Job ID: A4
I (7062814) bm1368Module: RX Job ID: 50
I (7062814) asic_result: Nonce difficulty 1162.28 of 533.
I (7062814) stratum_api: tx: {"id": 1826, "method": "mining.submit", "params": ["BC_ADRESS", "6485163800104703", "410a000000000000", "6655b4f8", "3b9e0716", "00008000"]}

I (7063024) stratum_task: rx: {"result":true,"error":null,"id":1826}
I (7063024) stratum_task: message result accepted
I (7065474) bm1368Module: Job ID: 89
I (7065474) bm1368Module: RX Job ID: 40
I (7065474) asic_result: Nonce difficulty 1415.29 of 533.
I (7065484) stratum_api: tx: {"id": 1827, "method": "mining.submit", "params": ["BC_ADRESS", "6485163800104703", "4b0b000000000000", "6655b4f8", "06c71f80", "00012000"]}

Guru Meditation Error: Core  0 panic'ed (Interrupt wdt timeout on CPU0).

Core  0 register dump:
PC      : 0x40377c54  PS      : 0x00050e34  A0      : 0x4037767c  A1      : 0x3fc9bd50
A2      : 0x3fcaa80c  A3      : 0x3fcc7fcc  A4      : 0x80380662  A5      : 0x4037e496
A6      : 0x00000008  A7      : 0x00000000  A8      : 0x00000000  A9      : 0x60013000
A10     : 0x3fc9e82c  A11     : 0x00000001  A12     : 0x3fc9bd54  A13     : 0x00000000
A14     : 0x00000000  A15     : 0x3fcaa920  SAR     : 0x00000015  EXCCAUSE: 0x00000005
EXCVADDR: 0x00000000  LBEG    : 0x40056f5c  LEND    : 0x40056f72  LCOUNT  : 0xffffffff
Core  0 was running in ISR context:
EPC1    : 0x420a1edb  EPC2    : 0x40377ca8  EPC3    : 0x00000000  EPC4    : 0x40377c54


Backtrace: 0x40377c51:0x3fc9bd50 0x40377679:0x3fc9bd90 0x40377e53:0x3fcc7c50 0x4037e40f:0x3fcc7c60 0x4037da23:0x3fcc7c80 0x420037ad:0x3fcc7cc0 0x4200c3c2:0x3fcc7ce0 0x4200c968:0x3fcc7d00 0x4037e069:0x3fcc7e60


Core  1 register dump:
PC      : 0x4037acee  PS      : 0x00060334  A0      : 0x82005025  A1      : 0x3fca8770
A2      : 0x00000000  A3      : 0x00000001  A4      : 0x8037e412  A5      : 0x3fcbcb20
A6      : 0x00060023  A7      : 0x00000003  A8      : 0x82021022  A9      : 0x3fca8730
A10     : 0x00000000  A11     : 0x00000001  A12     : 0x8037e412  A13     : 0x3fcc7a90
A14     : 0x00060023  A15     : 0x3fca8938  SAR     : 0x00000000  EXCCAUSE: 0x00000005
EXCVADDR: 0x00000000  LBEG    : 0x00000000  LEND    : 0x00000000  LCOUNT  : 0x00000000


Backtrace: 0x4037aceb:0x3fca8770 0x42005022:0x3fca8790 0x4037f279:0x3fca87b0 0x4037e069:0x3fca87d0




ELF file SHA256: aa00b2217

Rebooting...
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0xc (RTC_SW_CPU_RST),boot:0x2a (SPI_FAST_FLASH_BOOT)
Saved PC:0x40375ab8
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce3818,len:0x16e0
load:0x403c9700,len:0x4
load:0x403c9704,len:0xc00
load:0x403cc700,len:0x2eb0
entry 0x403c9908
I (26) boot: ESP-IDF v5.1 2nd stage bootloader
I (26) boot: compile time Mar  3 2024 19:55:36
I (26) boot: Multicore bootloader
I (29) boot: chip revision: v0.2
I (33) boot.esp32s3: Boot SPI Speed : 80MHz
I (38) boot.esp32s3: SPI Mode       : DIO
I (43) boot.esp32s3: SPI Flash Size : 16MB
I (47) boot: Enabling RNG early entropy source...
I (53) boot: Partition Table:
I (56) boot: ## Label            Usage          Type ST Offset   Length
I (64) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (71) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (79) boot:  2 factory          factory app      00 00 00010000 00400000
I (86) boot:  3 www              Unknown data     01 82 00410000 00300000
I (93) boot:  4 ota_0            OTA app          00 10 00710000 00400000
I (101) boot:  5 ota_1            OTA app          00 11 00b10000 00400000
I (109) boot:  6 otadata          OTA data         01 00 00f10000 00002000
I (116) boot:  7 coredump         Unknown data     01 03 00f12000 00010000
I (124) boot: End of partition table
I (128) esp_image: segment 0: paddr=00710020 vaddr=3c0b0020 size=2ca08h (182792) map
I (169) esp_image: segment 1: paddr=0073ca30 vaddr=3fc99500 size=035e8h ( 13800) load
I (173) esp_image: segment 2: paddr=00740020 vaddr=42000020 size=aaf60h (700256) map
I (301) esp_image: segment 3: paddr=007eaf88 vaddr=3fc9cae8 size=01818h (  6168) load
I (302) esp_image: segment 4: paddr=007ec7a8 vaddr=40374000 size=15414h ( 87060) load
I (335) boot: Loaded app from partition at offset 0x710000
I (335) boot: Disabling RNG early entropy source...
I (346) cpu_start: Multicore app
I (356) cpu_start: Pro cpu start user code
I (356) cpu_start: cpu freq: 160000000 Hz
I (357) cpu_start: Application information:
I (359) cpu_start: Project name:     esp-miner
I (364) cpu_start: App version:      v2.1.6
I (369) cpu_start: Compile time:     May 26 2024 14:44:58
I (375) cpu_start: ELF file SHA256:  aa00b2217...
I (381) cpu_start: ESP-IDF:          v5.2.1
I (386) cpu_start: Min chip rev:     v0.0
I (390) cpu_start: Max chip rev:     v0.99
I (395) cpu_start: Chip rev:         v0.2
I (400) heap_init: Initializing. RAM available for dynamic allocation:
I (407) heap_init: At 3FCA3B70 len 00045BA0 (278 KiB): RAM
I (413) heap_init: At 3FCE9710 len 00005724 (21 KiB): RAM
I (419) heap_init: At 3FCF0000 len 00008000 (32 KiB): DRAM
I (426) heap_init: At 600FE010 len 00001FD8 (7 KiB): RTCRAM
I (433) spi_flash: detected chip: gd
I (436) spi_flash: flash io: dio
W (440) i2c: This driver is an old driver, please migrate your application code to adapt `driver/i2c_master.h`
W (451) ADC: legacy driver is deprecated, please migrate to `esp_adc/adc_oneshot.h`
I (459) sleep: Configure to isolate all GPIO pins in sleep state
I (466) sleep: Enable automatic switching of GPIO sleep configuration
I (473) main_task: Started on CPU0
I (483) main_task: Calling app_main()
I (523) miner: NVS_CONFIG_ASIC_FREQ 490.000000
I (523) miner: ASIC: BM1368
I (523) miner: Welcome to the bitaxe!
I (523) SystemModule: I2C initialized successfully
I (533) DS4432U.c: Set ASIC voltage = 1.200V [0xC6]
I (533) DS4432U.c: Writing 0xC6
I (543) pp: pp rom version: e7ae62f
I (543) net80211: net80211 rom version: e7ae62f
I (563) wifi:wifi driver task: 3fcaf2c8, prio:23, stack:6656, core=0
I (573) wifi:wifi firmware version: a9f5b59
I (583) wifi:wifi certification version: v7.0
I (583) wifi:config NVS flash: enabled
I (583) wifi:config nano formating: disabled
I (583) wifi:Init data frame dynamic rx buffer num: 32
I (583) wifi:Init static rx mgmt buffer num: 5
I (593) wifi:Init management short buffer num: 32
I (593) wifi:Init dynamic tx buffer num: 32
I (603) wifi:Init static tx FG buffer num: 2
I (603) wifi:Init static rx buffer size: 1600
I (613) wifi:Init static rx buffer num: 10
I (613) wifi:Init dynamic rx buffer num: 32
I (613) wifi_init: rx ba win: 6
I (623) wifi_init: tcpip mbox: 32
I (623) wifi_init: udp mbox: 6
I (623) wifi_init: tcp mbox: 6
I (633) wifi_init: tcp tx win: 5760
I (633) wifi_init: tcp rx win: 5760
I (643) wifi_init: tcp mss: 1440
I (643) wifi_init: WiFi IRAM OP enabled
I (643) wifi_init: WiFi RX IRAM OP enabled
I (663) wifi station: ESP_WIFI Access Point On
W (663) wifi:Affected by the ESP-NOW encrypt num, set the max connection num to 10
I (663) wifi station: ESP_WIFI_MODE_STA
I (673) wifi station: wifi_init_sta finished.
I (673) phy_init: phy_version 640,cd64a1a,Jan 24 2024,17:28:12
I (713) wifi:mode : sta (dc:da:0c:3a:51:ac) + softAP (dc:da:0c:3a:51:ad)
I (723) wifi:enable tsf
I (723) wifi:Total power save buffer number: 16
I (723) wifi:Init max length of beacon: 752/752
I (723) wifi:Init max length of beacon: 752/752
I (733) esp_netif_lwip: DHCP server started on interface WIFI_AP_DEF with IP: 192.168.4.1
I (733) wifi:ap channel adjust o:1,1 n:11,2
I (743) wifi:new:<11,0>, old:<1,1>, ap:<11,2>, sta:<11,0>, prof:1
I (743) wifi:state: init -> auth (b0)
I (753) wifi station: ESP_WIFI setting hostname to: espressif
I (763) wifi station: wifi_init_sta finished.
I (1143) SystemModule: OLED init success!
I (1603) wifi:state: auth -> assoc (0)
I (1613) wifi:Association refused temporarily, comeback time 1000 (TUs)
I (1713) http_server: Partition size: total: 2884241, used: 664397
I (1713) http_server: Starting HTTP Server
I (1723) example_dns_redirect_server: Socket created
I (1723) example_dns_redirect_server: Socket bound, port 53
I (1733) example_dns_redirect_server: Waiting for data
I (2643) wifi:state: assoc -> assoc (0)
I (2653) wifi:state: assoc -> init (6c0)
I (2653) wifi:new:<11,0>, old:<11,0>, ap:<11,2>, sta:<11,0>, prof:1
I (5153) wifi station: Retrying WiFi connection...
I (5303) wifi:ap channel adjust o:11,2 n:1,1
I (5303) wifi:new:<1,0>, old:<11,0>, ap:<1,1>, sta:<1,0>, prof:1
I (5313) wifi:state: init -> auth (b0)
I (6503) wifi:state: auth -> assoc (0)
I (6503) wifi:state: assoc -> run (10)
I (6543) wifi:connected with W-LAN, aid = 2, channel 1, BW20, bssid = 3c:37:12:59:c7:05
I (6543) wifi:security: WPA3-SAE, phy: bgn, rssi: -78
I (6553) wifi:pm start, type: 1

I (6553) wifi:dp: 1, bi: 102400, li: 3, scale listen interval from 307200 us to 307200 us
I (6553) wifi:set rx beacon pti, rx_bcn_pti: 0, bcn_timeout: 25000, mt_pti: 0, mt_time: 10000
I (6583) wifi:<ba-add>idx:0 (ifx:0, 3c:37:12:59:c7:05), tid:6, ssn:3, winSize:64
I (6623) wifi:<ba-add>idx:1 (ifx:0, 3c:37:12:59:c7:05), tid:0, ssn:0, winSize:64
I (6633) wifi:AP's beacon interval = 102400 us, DTIM period = 1
I (7563) wifi station: Bitaxe ip:192.168.XX.XX
I (7563) esp_netif_handlers: sta ip: 192.168.XX.XX, mask: 255.255.255.0, gw: 192.168.0.1
I (7563) miner: Connected to SSID: W-LAN
I (7573) gpio: GPIO[12]| InputEn: 1| OutputEn: 0| OpenDrain: 0| Pullup: 0| Pulldown: 0| Intr:0
I (7563) wifi station: ESP_WIFI Access Point Off
I (7583) wifi:mode : sta (dc:da:0c:3a:51:ac)
I (7593) serial: Initializing serial
I (7593) bm1368Module: Initializing BM1368
I (8793) bm1368Module: 1 chip(s) detected on the chain
final refdiv: 2, fbdiv: 235, postdiv1: 6, postdiv2: 1, min diff value: 0.416656
I (15293) bm1368Module: Setting Frequency to 490.00MHz (0.01)
I (15293) bm1368Module: Setting max baud of 1000000
I (15293) serial: Changing UART baud to 1000000
I (15303) stratum_task: Get IP for URL: solo.ckpool.org

I (15333) stratum_task: Connecting to: stratum+tcp://solo.ckpool.org:3333 (51.81.56.15)

I (15343) stratum_task: Socket created, connecting to 51.81.56.15:3333
I (15343) ASIC_task: ASIC Ready!
I (15343) main_task: Returned from app_main()
I (15543) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe/BM1368"]}

I (15753) stratum_api: Received result {"result":[[["mining.notify","7407aaac"]],"a9ae9c70",8],"id":1,"error":null}
I (15753) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}

I (15773) stratum_api: Received result {"params":[10000],"id":null,"method":"mining.set_difficulty"}
configure_version result null
I (15783) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [1000]}

I (15793) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["BC_ADRESS", "x"]}

I (15903) stratum_task: rx: {"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"},"id":2,"error":null}
I (15903) stratum_task: Set version mask: 1fffe000
I (16063) stratum_task: rx: {"params":["6485163800104704","e7b7d0c2cfa4a5466ef8601789da2f9877839c960002c41c0000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3503b8e60c000416b555660494c5570f0c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff03ec90fa12000000002200201bc038ee5f8759ad75eb703c00d860de2ac75fdb6c2852424845ee1998927da4872763000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9ed1fca9bec260972322099b8f4cb407237487fafa7cf7c7783fe2a95baf67487fc00000000",["d40508d8da19a2cdfacbd9d513780a0f0093edf7fbf842d4b6ddbdbd8879ab83","0d90b5b5cfd1c608fba1a576ac176f81a72ab094eb46c5827439f63d6ace613f","35caa426bf8bcd368606d3ac15d552ed2703dd9b26d7a3b16eac05d31aa4d908","46d0561ecbf61b7d4a71511cbefc656f634bc01177f9634951788c5c387d6760","6d820d2131ab675e0c630993a87997e1dc600402af3f1e6b8cd4baec155adf46","3594939115245391f6a9ded249f5f2cf727491ac7906b4a5684411a348b7b967","25816b5722619f9bd8b019d9f3b1986ee371a70204f7c64fd6667701ca78716b","da2bf9a4d70a0c025100414dacd971ca758124cca14db90c2e4bfb0a439c3af6","09c8a8db4c1b2c119f544d577c0e3de48eaf30d724f1a38ba71d1382448b4944","9cf18c468633ba7002336d28494ffb3789e10efc996670e73ea34f434c7fbc53","9490fe76b36d534633c77a5c323d6f489531af110ff213c80547215c186f3793"],"20000000","170355f0","6655b516",true],"id":null,"method":"mining.notify"}
I (16173) SystemModule: Syncing clock
I (16173) create_jobs_task: New Work Dequeued 6485163800104704
I (16173) stratum_task: rx: {"params":[10000],"id":null,"method":"mining.set_difficulty"}
I (16193) stratum_task: Set stratum difficulty: 10000
I (16193) stratum_task: rx: {"result":true,"error":null,"id":4}
I (16203) stratum_task: message result accepted
I (20083) bm1368Module: Job ID: 5E
I (20083) bm1368Module: RX Job ID: 28
I (20083) asic_result: Nonce difficulty 370.82 of 8192.
I (20883) bm1368Module: Job ID: 5E
I (20883) bm1368Module: RX Job ID: 28
I (20883) asic_result: Nonce difficulty 10868.53 of 8192.
I (20883) stratum_api: tx: {"id": 5, "method": "mining.submit", "params": ["BC_ADRESS", "6485163800104704", "d601000000000000", "6655b516", "ee031164", "0001c000"]}

I (21083) stratum_task: rx: {"result":true,"error":null,"id":5}
I (21083) stratum_task: message result accepted
I (23133) bm1368Module: Job ID: 8A
I (23133) bm1368Module: RX Job ID: 40
I (23133) asic_result: Nonce difficulty 350.24 of 8192.
I (23363) bm1368Module: Job ID: AE
I (23363) bm1368Module: RX Job ID: 50
I (23363) asic_result: Nonce difficulty 630.68 of 8192.
I (25133) bm1368Module: Job ID: 04
I (25133) bm1368Module: RX Job ID: 00
I (25133) asic_result: Nonce difficulty 806.51 of 8192.
I (28413) bm1368Module: Job ID: 8A
I (28413) bm1368Module: RX Job ID: 40
I (28413) asic_result: Nonce difficulty 638.06 of 8192.

```

### solobito on 2024-05-28

In my case, it still shows a "stack overflow" error. I tried changing the stack size, but it only delayed the overflow, resulting in more `httpd_txrx: httpd_sock_err:` **It looks different from the one @Shen shows.**

I have tried with older versions, and the same error occurs. Yesterday, I let it run without monitoring the logs, and it ran for 16 hours without restarting. However, when I connected via USB, websockets and HTTP Get every 5 seconds, the system restarted a few minutes later with the stack overflow error. **That is, it seems that if I don't monitor the logs, it doesn't restart.**

I've tried various stack_size values, but they don't solve the problem. For example, I set `config.stack_size = 8192*4;` added in line 589 of `http_server.c` but it still keeps rebooting.

```
[32m[0m
[39m
[32mI (57821786) stratum_task: rx: {"result":true,"error":null,"id":17201}[39m
[0;32mI (57821786) stratum_task: message result accepted
[33mW (57823166) httpd_txrx: httpd_sock_err: error in recv : 04[39m
[33mW (57823166) httpd_txrx: httpd_sock_err: error in send : 04[39m
[0;33mW (57823176) httpd_txrx: httpd_sock_err: error in send : 128
[33mW (57823176) httpd_txrx: httpd_sock_err: error in send : 128[39m
[0;33mW (57823186) httpd_txrx: httpd_sock_err: error in send : 128
[33mW (57823186) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823196) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823206) httpd_txrx: httpd_sock_err: error in send : 128[39m
[0;33mW (57823206) httpd_txrx: httpd_sock_err: error in send : 128
[33mW (57823216) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823226) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823226) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823236) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823246) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823246) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823256) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823256) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823266) httpd_txrx: httpd_sock_err: error in send : 128[39m
[0;33mW (57823276) httpd_txrx: httpd_sock_err: error in send : 128
[33mW (57823276) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823286) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823296) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823296) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823306) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823316) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823316) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823326) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823326) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823336) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823346) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823346) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823356) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823366) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823366) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823376) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823386) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823386) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823396) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823396) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823406) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823416) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823416) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823426) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823436) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823436) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823446) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823446) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823456) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823466) httpd_txrx: httpd_sock_err: error in send : 128[39m
[0;33mW (57823466) httpd_txrx: httpd_sock_err: error in send : 128
[33mW (57823476) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823486) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823486) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823496) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823506) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823506) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823516) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823516) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823526) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823536) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823536) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823546) httpd_txrx: httpd_sock_err: error in send : 128[39m
[0;33mW (57823556) httpd_txrx: httpd_sock_err: error in send : 128
[0;33mW (57823556) httpd_txrx: httpd_sock_err: error in send : 128
[33mW (57823566) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823576) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823576) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823586) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823586) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823596) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823606) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823606) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823616) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823626) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823626) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823636) httpd_txrx: httpd_sock_err: error in send : 128[39m
[0;33mW (57823636) httpd_txrx: httpd_sock_err: error in send : 128
[0;33mW (57823646) httpd_txrx: httpd_sock_err: error in send : 128
[33mW (57823656) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823656) httpd_txrx: httpd_sock_err: error in send : 128[39m
[0;33mW (57823666) httpd_txrx: httpd_sock_err: error in send : 128
[0;33mW (57823676) httpd_txrx: httpd_sock_err: error in send : 128
[33mW (57823676) httpd_txrx: httpd_sock_err: error in send : 128[39m
[0;33mW (57823686) httpd_txrx: httpd_sock_err: error in send : 128
[0;33mW (57823696) httpd_txrx: httpd_sock_err: error in send : 128
[33mW (57823696) httpd_txrx: httpd_sock_err: error in send : 128[39m
[0;33mW (57823706) httpd_txrx: httpd_sock_err: error in send : 128
[33mW (57823706) httpd_txrx: httpd_sock_err: error in send : 128[39m
[33mW (57823716) httpd_txrx: httpd_sock_err: error in send : 128[39m
[0;33mW (57823726) httpd_txrx: httpd_sock_err: error in send : 128

***ERROR*** A stack overflow in task httpd has been detected.

Backtrace: 0x40375c42:0x3fcbd170 0x4037d835:0x3fcbd190 0x407e7ee:0x3fcbd1b0 0x4037fcb3:0x3fcbd230 0x4037e8b4:0x3fcbd250 0x037e8aa:0x00000000 |<-CORRUPTED




ELF file SHA256: e4865dbe1

Rebooting...
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0xc (RTC_SW_CPU_RST),boot:0x28 (SPI_FAST_FLASH_BOOT)
Saved PC:0x40375b7c
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce2810,len:0x178c
load:0x403c8700,len:0x4
load:0x403c8704,len:0xcb8
load:0x403cb700,len:0x2d9c
entry 0x403c8914
[32mI (26) boot: ESP-IDF v5.4-dev-421-g4523f2d674 2nd stage bootloader[39m
[32mI (26) boot: compile time May 27 2024 21:22:26[39m
[32mI (27) boot: Multicore bootloader[39m
[32mI (31) boot: chip revision: v0.2[39m
[0;32mI (35) boot.esp32s3: Boot SPI Speed : 80MHz
[32mI (39) boot.esp32s3: SPI Mode       : DIO[39m
[32mI (44) boot.esp32s3: SPI Flash Size : 16MB[39m
[32mI (49) boot: Enabling RNG early entropy source...[39m
[32mI (54) boot: Partition Table:[39m
[32mI (58) boot: ## Label            Usage          Type ST Offset   Length[39m
[32mI (65) boot:  0 nvs              WiFi data        01 02 00009000 00006000[39m
[0;32mI (73) boot:  1 phy_init         RF data          01 01 0[32mI (80) boot:  2 factory          factory app      00 00 00010000 00400000[39m
[0;32mI (88) boot:  3 www              Unknown data     01 82 0410000 00300000
[0;32mI (95) boot:  4 ota_0            OTA app          00 10 00710000 00400000
[0;32mI (103) boot:  5 ota_1            OTA app          00 11 0b10000 00400000
[0;32mI (110) boot:  6 otadata          OTA data         01 00 00f10000 00002000
[0;32mI (118) boot:  7 coredump         Unknown data     01 03 00f12000 00010000
[32mI (125) boot: End of partition table[39m
[0;32mI (130) boot: Defaulting to factory image
[0;32mI (134) esp_image: segment 0: paddr=00010020 vaddr=3c0b000 size=2a704h (173828) map
[32mI (174) esp_image: segment 1: paddr=0003a72c vaddr=3fc9a500 size=05008h ( 20488) load[39m
[32mI (179) esp_image: segment 2: paddr=0003f73c vaddr=40374000 size=008dch (  2268) load[39m
[0;32mI (180) esp_image: segment 3: paddr=00040020 vaddr=4200000 size=ac538h (705848) map
[32mI (315) esp_image: segment 4: paddr=000ec560 vaddr=403748c size=15bb8h ( 89016) load[39m
[32mI (344) boot: Loaded app from partition at offset 0x10000[39m
[0;32mI (344) boot: Disabling RNG early entropy source...
[32mI (355) cpu_start: Multicore app[39m
[0;32mI (365) cpu_start: Pro cpu start user code
[32mI (365) cpu_start: cpu freq: 160000000 Hz[39m
[32mI (365) app_init: Application information:[39m
[32mI (368) app_init: Project name:     esp-miner[39m
[32mI (373) app_init: App version:      v2.1.6-dirty[39m
[32mI (378) app_init: Compile time:     May 27 2024 23:16:25m
[39m
[32m[0;32mI (384) app_init: ELF file SHA256:  e4865dbe1...[39m
[0;32mI (390) app_init: ESP-IDF:          v5.4-dev-421-g4523f2d674
[32mI (396) efuse_init: Min chip rev:     v0.0[39m
[32mI (401) efuse_init: Max chip rev:     v0.99 [39m
[32mI (406) efuse_init: Chip rev:         v0.2[39m
[32mI (411) heap_init: Initializing. RAM available for dynamic allocation:[39m
[32mI (418) heap_init: At 3FCA4ED8 len 00044838 (274 KiB): RAM[39m
[32mI (424) heap_init: At 3FCE9710 len 00005724 (21 KiB): RAM[39m
[32mI (430) heap_init: At 3FCF0000 len 00008000 (32 KiB): DRAM[39m
[32mI (436) heap_init: At 600FE100 len 00001EE8 (7 KiB): RTCRAM[39m
[32mI (443) spi_flash: detected chip: gd[39m
[32mI (447) spi_flash: flash io: dio[39m
e your application code to adapt `driver/i2c_master.h`
[0;33mW (462) ADC: legacy driver is deprecated, please migrate to `esp_adc/adc_oneshot.h`
[32mI (470) sleep: Configure to isolate all GPIO pins in sleep state[39m
[32mI (477) sleep: Enable automatic switching of GPIO sleep configuration[39m
[32mI (484) main_task: Started on CPU0[39m
[32mI (494) main_task: Calling app_main()[39m
[32mI (524) miner: NVS_CONFIG_ASIC_FREQ 490.000000[39m
[32mI (524) miner: ASIC: BM1368[39m
[32mI (524) SystemModule: I2C initialized successfully[39m
[32mI (524) DS4432U.c: Set ASIC voltage = 1.200V [0xC6][39m
[32mI (534) DS4432U.c: Writing 0xC6[39m
[32mI (534) miner: Welcome to the bitaxe![39m

```

These are the logs I obtained with Visual Studio Code.

```
I (445464) stratum_task: rx: {"result":true,"error":null,"id":54}
I (445474) stratum_task: message result accepted
W (450304) httpd_txrx: httpd_sock_err: error in recv : 104
W (450314) httpd_txrx: httpd_sock_err: error in send : 104
W (450314) httpd_txrx: httpd_sock_err: error in send : 128
W (450314) httpd_txrx: httpd_sock_err: error in send : 128
W (450324) httpd_txrx: httpd_sock_err: error in send : 128
W (450334) httpd_txrx: httpd_sock_err: error in send : 128
W (450334) httpd_txrx: httpd_sock_err: error in send : 128
W (450344) httpd_txrx: httpd_sock_err: error in send : 128
W (450344) httpd_txrx: httpd_sock_err: error in send : 128
W (450354) httpd_txrx: httpd_sock_err: error in send : 128
W (450364) httpd_txrx: httpd_sock_err: error in send : 128
W (450364) httpd_txrx: httpd_sock_err: error in send : 128
W (450374) httpd_txrx: httpd_sock_err: error in send : 128
W (450384) httpd_txrx: httpd_sock_err: error in send : 128
W (450384) httpd_txrx: httpd_sock_err: error in send : 128
W (450394) httpd_txrx: httpd_sock_err: error in send : 128
W (450394) httpd_txrx: httpd_sock_err: error in send : 128

***ERROR*** A stack overflow in task httpd has been detected.


Backtrace: 0x40375c42:0x3fcbd140 0x4037d835:0x3fcbd160 0x4037e7ee:0x3fcbd180 0x4037fcb3:0x3fcbd200 0x4037e8b4:0x3fcbd220 0x4037e8aa:0x00000000 |<-CORRUPTED
0x40375c42: panic_abort at /Users/user/esp/esp-idf/components/esp_system/panic.c:463
0x4037d835: esp_system_abort at /Users/user/esp/esp-idf/components/esp_system/port/esp_system_chip.c:92
0x4037e7ee: vApplicationStackOverflowHook at /Users/user/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/xtensa/port.c:553
0x4037fcb3: vTaskSwitchContext at /Users/user/esp/esp-idf/components/freertos/FreeRTOS-Kernel/tasks.c:3667 (discriminator 7)
0x4037e8b4: _frxt_dispatch at /Users/user/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/xtensa/portasm.S:451
0x4037e8aa: _frxt_int_exit at /Users/user/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/xtensa/portasm.S:246





ELF file SHA256: bb06be8d9

Rebooting...
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0xc (RTC_SW_CPU_RST),boot:0x28 (SPI_FAST_FLASH_BOOT)
Saved PC:0x40375b7c
0x40375b7c: esp_restart_noos at /Users/user/esp/esp-idf/components/esp_system/port/soc/esp32s3/system_internal.c:158

SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce2810,len:0x178c
load:0x403c8700,len:0x4
load:0x403c8704,len:0xcb8
load:0x403cb700,len:0x2d9c
entry 0x403c8914
```

I am continuing to test to try to gather more details about the error.


### solobito on 2024-05-29

I have erased and flashed using older versions, even 2.1.0 and sooner or later I have reboots with the same cause. I'm starting to think something is wrong with my ESP32...

### Shen on 2024-05-29

> I have erased and flashed using older versions, even 2.1.0 and sooner or later I have reboots with the same cause. I'm starting to think something is wrong with my ESP32...

I also tried to use older versions and get the same error, here V2.1.0:

```
I (1865848) stratum_task: rx: {"result":true,"error":null,"id":512}
I (1865848) stratum_task: message result accepted
I (1866168) bm1368Module: RX Job ID: 28
I (1866168) asic_result: Nonce difficulty 436.11 of 464.
I (1869748) stratum_task: rx: {"params":["648516380010520e","baed161993897b13a8d55be2608be65d01cf302b000249460000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff350339e70c00046ef156660462733f0d0c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff0399080914000000002200201bc038ee5f8759ad75eb703c00d860de2ac75fdb6c2852424845ee1998927da495ac68000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9edf44cff46f9692a46cfa21fc46990c497f4db831e29e1e016d496da1a8f7e266200000000",["b00e613005d059d61fbd06532feb210e4ade34be355a7417b1e35ebfabfa0d51","ed8d20fa9e7277962ba7e67529c828afd0134006cc0626db89398fe9d7fe27d1","a1e89de2cbafe76d956db7208eb39e08d5bf2d973463a040188403b3811d5103","b38eee9ebdee47852bec52958a062af134254517899b4aebcf403dd24c779160","b3ed73a910326c84f8d0367cc9922835e5a0262adba64f5daf2dbd72659d0378","0adf27edb8beb2de011d002d743085b3e6a5c671d24b03d4be08feb2339009b6","5e07cb2a94ee5dc73b0238219eb555e6671abf36710e202a703567745c6d51d3","014e7874a026026a7bec6ed27b33a76712303bed973ddaa35d258a926d6866d6","9580e7e4d02f9b50de13d683c357869f0b4601ef36cd8eee20aaec3492396860","1abb21f83241a2fd358bec7144c2726c2fdb21efada94bca1d54e72d3404da24","e5bcec3501d70241ff3d89221e3f62510ffee79d31bfe96058b9ca0183010aee","82e2424d2d5740a7d9f780d4320d2e9ee92f56bdf420159f0b39d9299576ecb8","a6231472b4f963b6767eefc9567f382c2a69aa4d339a25cedddc552987c8f260"],"20000000","170355f0","6656f16e",false],"id":null,"method":"mining.notify"}
I (1869878) create_jobs_task: New Work Dequeued 648516380010520e
I (1871498) bm1368Module: RX Job ID: 20
I (1871498) asic_result: Nonce difficulty 1197.93 of 464.
I (1871508) stratum_api: tx: {"id": 513, "method": "mining.submit", "params": ["BC_ADRESS", "648516380010520e", "9500000000000000", "6656f16e", "ebef354e", "00008000"]}

Guru Meditation Error: Core  0 panic'ed (Interrupt wdt timeout on CPU0).

Core  0 register dump:
PC      : 0x40377c3a  PS      : 0x00050e34  A0      : 0x4037710c  A1      : 0x3fc9a730
A2      : 0x3fca8c88  A3      : 0x00000000  A4      : 0x00000000  A5      : 0x40380b46
A6      : 0x00000000  A7      : 0x3fc9d4f4  A8      : 0x00000000  A9      : 0x60013000
A10     : 0x00000000  A11     : 0x00000000  A12     : 0x3fc9a734  A13     : 0x00000000
A14     : 0x3fca8d9c  A15     : 0x00000000  SAR     : 0x0000001a  EXCCAUSE: 0x00000005
EXCVADDR: 0x00000000  LBEG    : 0x40056f5c  LEND    : 0x40056f72  LCOUNT  : 0xffffffff
Core  0 was running in ISR context:
EPC1    : 0x420a0603  EPC2    : 0x40377cdc  EPC3    : 0x00000000  EPC4    : 0x40377c3a


Backtrace: 0x40377c37:0x3fc9a730 0x40377109:0x3fc9a770 0x40377e4f:0x3fcc64c0 0x4200c4d4:0x3fcc64e0 0x40380791:0x3fcc6640


Core  1 register dump:
PC      : 0x4037b8b2  PS      : 0x00060b34  A0      : 0x82004ef5  A1      : 0x3fca6f50
A2      : 0x00000000  A3      : 0x00000000  A4      : 0x80380a7a  A5      : 0x3fca6e80
A6      : 0x00060023  A7      : 0x00000003  A8      : 0x82020066  A9      : 0x3fca6f10
A10     : 0x00000000  A11     : 0x00000000  A12     : 0x80380a7a  A13     : 0x3fcc6120
A14     : 0x00060023  A15     : 0x00000003  SAR     : 0x00000000  EXCCAUSE: 0x00000005
EXCVADDR: 0x00000000  LBEG    : 0x00000000  LEND    : 0x00000000  LCOUNT  : 0x00000000


Backtrace: 0x4037b8af:0x3fca6f50 0x42004ef2:0x3fca6f70 0x4037ef85:0x3fca6f90 0x40380791:0x3fca6fb0




ELF file SHA256: 9b1e3cabceff5618

Rebooting...
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0x3 (RTC_SW_SYS_RST),boot:0x28 (SPI_FAST_FLASH_BOOT)
Saved PC:0x40375950
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce3818,len:0x16e0
load:0x403c9700,len:0x4
load:0x403c9704,len:0xc00
load:0x403cc700,len:0x2eb0
entry 0x403c9908
I (26) boot: ESP-IDF v5.1 2nd stage bootloader
I (26) boot: compile time Mar  3 2024 19:55:36
I (27) boot: Multicore bootloader
I (29) boot: chip revision: v0.2
I (33) boot.esp32s3: Boot SPI Speed : 80MHz
I (38) boot.esp32s3: SPI Mode       : DIO
I (43) boot.esp32s3: SPI Flash Size : 16MB
I (47) boot: Enabling RNG early entropy source...
I (53) boot: Partition Table:
I (56) boot: ## Label            Usage          Type ST Offset   Length
I (64) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (71) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (79) boot:  2 factory          factory app      00 00 00010000 00400000
I (86) boot:  3 www              Unknown data     01 82 00410000 00300000
I (93) boot:  4 ota_0            OTA app          00 10 00710000 00400000
I (101) boot:  5 ota_1            OTA app          00 11 00b10000 00400000
I (108) boot:  6 otadata          OTA data         01 00 00f10000 00002000
I (116) boot:  7 coredump         Unknown data     01 03 00f12000 00010000
I (124) boot: End of partition table
I (128) boot: Defaulting to factory image
I (133) esp_image: segment 0: paddr=00010020 vaddr=3c0b0020 size=2a194h (172436) map
I (172) esp_image: segment 1: paddr=0003a1bc vaddr=3fc98100 size=04bbch ( 19388) load
I (177) esp_image: segment 2: paddr=0003ed80 vaddr=40374000 size=01298h (  4760) load
I (179) esp_image: segment 3: paddr=00040020 vaddr=42000020 size=a6d20h (683296) map
I (309) esp_image: segment 4: paddr=000e6d48 vaddr=40375298 size=12e54h ( 77396) load
I (335) boot: Loaded app from partition at offset 0x10000
I (336) boot: Disabling RNG early entropy source...
I (347) cpu_start: Multicore app
I (347) cpu_start: Pro cpu up.
I (347) cpu_start: Starting app cpu, entry point is 0x40375584
I (0) cpu_start: App cpu up.
I (365) cpu_start: Pro cpu start user code
I (365) cpu_start: cpu freq: 160000000 Hz
I (366) cpu_start: Application information:
I (368) cpu_start: Project name:     esp-miner
I (374) cpu_start: App version:      v2.1.0
I (378) cpu_start: Compile time:     Mar  3 2024 19:54:36
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
I (465) sleep: Enable automatic switching of GPIO sleep configuration
I (473) app_start: Starting scheduler on CPU0
I (478) app_start: Starting scheduler on CPU1
I (478) main_task: Started on CPU0
I (488) main_task: Calling app_main()
I (528) miner: NVS_CONFIG_ASIC_FREQ 490.000000
I (528) miner: ASIC: BM1368
I (528) miner: Welcome to the bitaxe!
I (528) SystemModule: I2C initialized successfully
I (538) DS4432U.c: Set BM1397 voltage = 1.200V [0xC6]
I (538) DS4432U.c: Writing 0xC6
I (548) pp: pp rom version: e7ae62f
I (548) net80211: net80211 rom version: e7ae62f
I (568) wifi:wifi driver task: 3fcad938, prio:23, stack:6656, core=0
I (578) wifi:wifi firmware version: b2f1f86
I (578) wifi:wifi certification version: v7.0
I (588) wifi:config NVS flash: enabled
I (588) wifi:config nano formating: disabled
I (588) wifi:Init data frame dynamic rx buffer num: 32
I (588) wifi:Init management frame dynamic rx buffer num: 32
I (598) wifi:Init management short buffer num: 32
I (598) wifi:Init dynamic tx buffer num: 32
I (608) wifi:Init static tx FG buffer num: 2
I (608) wifi:Init static rx buffer size: 1600
I (618) wifi:Init static rx buffer num: 10
I (618) wifi:Init dynamic rx buffer num: 32
I (618) wifi_init: rx ba win: 6
I (628) wifi_init: tcpip mbox: 32
I (628) wifi_init: udp mbox: 6
I (628) wifi_init: tcp mbox: 6
I (638) wifi_init: tcp tx win: 5744
I (638) wifi_init: tcp rx win: 5744
I (648) wifi_init: tcp mss: 1440
I (648) wifi_init: WiFi IRAM OP enabled
I (658) wifi_init: WiFi RX IRAM OP enabled
I (668) wifi station: ESP_WIFI Access Point On
W (668) wifi:Affected by the ESP-NOW encrypt num, set the max connection num to 10
I (668) wifi station: ESP_WIFI_MODE_STA
I (678) wifi station: wifi_init_sta finished.
I (678) phy_init: phy_version 601,fe52df4,May 10 2023,17:26:54
I (718) wifi:mode : sta (dc:da:0c:3a:51:ac) + softAP (dc:da:0c:3a:51:ad)
I (718) wifi:enable tsf
I (728) wifi:Total power save buffer number: 16
I (728) wifi:Init max length of beacon: 752/752
I (728) wifi:Init max length of beacon: 752/752
I (738) wifi station: wifi_init_sta finished.
I (738) esp_netif_lwip: DHCP server started on interface WIFI_AP_DEF with IP: 192.168.4.1
I (738) wifi:new:<1,1>, old:<1,1>, ap:<1,1>, sta:<1,0>, prof:1
I (748) wifi:state: init -> auth (b0)
I (1188) SystemModule: OLED init success!
I (1368) http_server: Partition size: total: 2884241, used: 664397
I (1368) http_server: Starting HTTP Server
I (1378) example_dns_redirect_server: Socket created
I (1378) example_dns_redirect_server: Socket bound, port 53
I (1388) example_dns_redirect_server: Waiting for data
I (5098) wifi:state: auth -> init (200)
I (5098) wifi:new:<1,0>, old:<1,1>, ap:<1,1>, sta:<1,0>, prof:1
I (6108) wifi station: Retrying WiFi connection...
I (6868) wifi:ap channel adjust o:1,1 n:6,2
I (6868) wifi:new:<6,0>, old:<1,0>, ap:<6,2>, sta:<6,0>, prof:1
I (6868) wifi:state: init -> auth (b0)
I (7608) wifi:state: auth -> assoc (0)
I (7618) wifi:state: assoc -> run (10)
I (7638) wifi:connected with WLAN, aid = 4, channel 6, BW20, bssid = d4:24:dd:12:16:5d
I (7638) wifi:security: WPA3-SAE, phy: bgn, rssi: -50
I (7648) wifi:pm start, type: 1

I (7648) wifi:set rx beacon pti, rx_bcn_pti: 0, bcn_timeout: 25000, mt_pti: 0, mt_time: 10000
I (7658) wifi:<ba-add>idx:0 (ifx:0, d4:24:dd:12:16:5d), tid:0, ssn:0, winSize:64
I (7708) wifi:AP's beacon interval = 102400 us, DTIM period = 1
I (8648) wifi station: Bitaxe ip:192.168.XX.XX
I (8648) esp_netif_handlers: sta ip: 192.168.XX.XX, mask: 255.255.255.0, gw: 192.168.0.1
I (8648) miner: Connected to SSID: WLAN
I (8658) gpio: GPIO[12]| InputEn: 1| OutputEn: 0| OpenDrain: 0| Pullup: 0| Pulldown: 0| Intr:0
I (8658) wifi station: ESP_WIFI Access Point Off
I (8668) wifi:mode : sta (dc:da:0c:3a:51:ac)
I (8678) serial: Initializing serial
I (8678) bm1368Module: Initializing BM1368
final refdiv: 2, fbdiv: 235, postdiv1: 6, postdiv2: 1, min diff value: 0.416656
I (15378) bm1368Module: Setting Frequency to 490.00MHz (0.01)
I (15378) stratum_task: Get IP for URL: solo.ckpool.org

I (15388) bm1368Module: Setting max baud of 1000000
I (15388) main_task: Returned from app_main()
I (15398) serial: Changing UART baud to 1000000
I (15398) ASIC_task: ASIC Ready!
I (16928) stratum_task: Connecting to: stratum+tcp://solo.ckpool.org:3333 (51.81.56.15)

I (16928) stratum_task: Socket created, connecting to 51.81.56.15:3333
I (17128) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe/BM1368"]}

I (17338) stratum_api: Received result {"result":[[["mining.notify","741a6ad4"]],"f544a970",8],"id":1,"error":null}
I (17338) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}

I (17348) stratum_api: Received result {"params":[10000],"id":null,"method":"mining.set_difficulty"}
configure_version result null
I (17368) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [512]}

I (17378) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["BC_ADRESS", "x"]}

I (17538) stratum_task: rx: {"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"},"id":2,"error":null}
I (17548) stratum_task: Set version mask: 1fffe000
I (17648) stratum_task: rx: {"params":["648516380010520e","baed161993897b13a8d55be2608be65d01cf302b000249460000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff350339e70c00046ef156660462733f0d0c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff0399080914000000002200201bc038ee5f8759ad75eb703c00d860de2ac75fdb6c2852424845ee1998927da495ac68000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9edf44cff46f9692a46cfa21fc46990c497f4db831e29e1e016d496da1a8f7e266200000000",["b00e613005d059d61fbd06532feb210e4ade34be355a7417b1e35ebfabfa0d51","ed8d20fa9e7277962ba7e67529c828afd0134006cc0626db89398fe9d7fe27d1","a1e89de2cbafe76d956db7208eb39e08d5bf2d973463a040188403b3811d5103","b38eee9ebdee47852bec52958a062af134254517899b4aebcf403dd24c779160","b3ed73a910326c84f8d0367cc9922835e5a0262adba64f5daf2dbd72659d0378","0adf27edb8beb2de011d002d743085b3e6a5c671d24b03d4be08feb2339009b6","5e07cb2a94ee5dc73b0238219eb555e6671abf36710e202a703567745c6d51d3","014e7874a026026a7bec6ed27b33a76712303bed973ddaa35d258a926d6866d6","9580e7e4d02f9b50de13d683c357869f0b4601ef36cd8eee20aaec3492396860","1abb21f83241a2fd358bec7144c2726c2fdb21efada94bca1d54e72d3404da24","e5bcec3501d70241ff3d89221e3f62510ffee79d31bfe96058b9ca0183010aee","82e2424d2d5740a7d9f780d4320d2e9ee92f56bdf420159f0b39d9299576ecb8","a6231472b4f963b6767eefc9567f382c2a69aa4d339a25cedddc552987c8f260"],"20000000","170355f0","6656f16e",true],"id":null,"method":"mining.notify"}
I (17768) SystemModule: Syncing clock
I (17768) create_jobs_task: New Work Dequeued 648516380010520e
I (17768) stratum_task: rx: {"params":[10000],"id":null,"method":"mining.set_difficulty"}
I (17788) stratum_task: Set stratum difficulty: 10000
I (17798) stratum_task: rx: {"result":true,"error":null,"id":4}
I (17798) stratum_task: message result accepted

```

### solobito on 2024-05-29

Ok, I just reproduced the `Guru Meditation Error: Core  0 panic'ed (Interrupt wdt timeout on CPU0).` as it happens to @Shen

That is, there are at least 2 types of errors before rebooting in V2.1.6, although I don't know if they are related:

- A stack overflow in task httpd has been detected. (httpd_txrx: httpd_sock_err:)
- Guru Meditation Error: Core  0 panic'ed (Interrupt wdt timeout on CPU0).

My logs here:
```
I (684078) bm1368Module: Job ID: 5D
I (684078) bm1368Module: RX Job ID: 28
I (684078) asic_result: Nonce difficulty 317.19 of 343.
I (684218) stratum_task: rx: {"result":true,"error":null,"id":78}
I (684218) stratum_task: message result accepted
I (684438) bm1368Module: Job ID: 78
I (684448) bm1368Module: RX Job ID: 38
I (684448) asic_result: Nonce difficulty 972.89 of 343.
I (684448) stratum_api: tx: {"id": 79, "method": "mining.submit", "params": ["bc1qu032m2wuvtachz8ds5ew9zx3mmk2l9l40zfkl2.bitaxe", "64851638001052ac", "2900000000000000", "66570352", "57fd367c", "00010000"]}

Guru Meditation Error: Core  0 panic'ed (Interrupt wdt timeout on CPU0). 

Core  0 register dump:
PC      : 0x40377e56  PS      : 0x00050a34  A0      : 0x4037767c  A1      : 0x3fc9bd50  
A2      : 0x3fcaa704  A3      : 0x0000cdcd  A4      : 0x00000000  A5      : 0x4037e496  
A6      : 0x00000008  A7      : 0x00000000  A8      : 0x00000000  A9      : 0x60013000  
A10     : 0x3fc9e82c  A11     : 0x00000001  A12     : 0x3fc9bd54  A13     : 0x00060023  
A14     : 0x00000000  A15     : 0x0000cdcd  SAR     : 0x0000000b  EXCCAUSE: 0x00000005  
EXCVADDR: 0x00000000  LBEG    : 0x40056f5c  LEND    : 0x40056f72  LCOUNT  : 0xffffffff  
Core  0 was running in ISR context:
EPC1    : 0x420a1edb  EPC2    : 0x40377668  EPC3    : 0x00000000  EPC4    : 0x40377e56


Backtrace: 0x40377e53:0x3fc9bd50 0x40377679:0x3fc9bd90 0x40377e53:0x3fcc8340 0x4037e40f:0x3fcc8350 0x4038328e:0x3fcc8370 0x4038323d:0x3fcc8390 0x403762fa:0x3fcc83b0 0x4038513d:0x3fcc83d0 0x4200c971:0x3fcc83f0 0x4037e069:0x3fcc8550


Core  1 register dump:
PC      : 0x4037acee  PS      : 0x00060b34  A0      : 0x82005025  A1      : 0x3fca8770  
A2      : 0x00000000  A3      : 0x00000001  A4      : 0x8037e412  A5      : 0x3fcc8180  
A6      : 0x00060023  A7      : 0x00000003  A8      : 0x82021022  A9      : 0x3fca8730  
A10     : 0x00000000  A11     : 0x00000001  A12     : 0x00000000  A13     : 0x00060f23  
A14     : 0x8037e06c  A15     : 0x3fca8938  SAR     : 0x00000000  EXCCAUSE: 0x00000005  
EXCVADDR: 0x00000000  LBEG    : 0x00000000  LEND    : 0x00000000  LCOUNT  : 0x00000000  


Backtrace: 0x4037aceb:0x3fca8770 0x42005022:0x3fca8790 0x4037f279:0x3fca87b0 0x4037e069:0x3fca87d0




ELF file SHA256: aa00b2217

Rebooting...
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0xc (RTC_SW_CPU_RST),boot:0x28 (SPI_FAST_FLASH_BOOT)
Saved PC:0x40375ab8
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce3810,len:0x178c
load:0x403c9700,len:0x4
load:0x403c9704,len:0xcbc
load:0x403cc700,len:0x2da0
entry 0x403c9914
I (26) boot: ESP-IDF v5.2.1 2nd stage bootloader
I (26) boot: compile time May 26 2024 14:45:13
I (26) boot: Multicore bootloader
I (29) boot: chip revision: v0.2
I (33) boot.esp32s3: Boot SPI Speed : 80MHz
I (38) boot.esp32s3: SPI Mode       : DIO
I (43) boot.esp32s3: SPI Flash Size : 16MB
I (47) boot: Enabling RNG early entropy source...
I (53) boot: Partition Table:
I (56) boot: ## Label            Usage          Type ST Offset   Length
I (64) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (71) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (79) boot:  2 factory          factory app      00 00 00010000 00400000
I (86) boot:  3 www              Unknown data     01 82 00410000 00300000
I (94) boot:  4 ota_0            OTA app          00 10 00710000 00400000
I (101) boot:  5 ota_1            OTA app          00 11 00b10000 00400000
I (109) boot:  6 otadata          OTA data         01 00 00f10000 00002000
I (116) boot:  7 coredump         Unknown data     01 03 00f12000 00010000
I (124) boot: End of partition table
I (128) boot: Defaulting to factory image
I (133) esp_image: segment 0: paddr=00010020 vaddr=3c0b0020 size=2ca08h (182792) map
I (174) esp_image: segment 1: paddr=0003ca30 vaddr=3fc99500 size=035e8h ( 13800) load
I (177) esp_image: segment 2: paddr=00040020 vaddr=42000020 size=aaf60h (700256) map
I (305) esp_image: segment 3: paddr=000eaf88 vaddr=3fc9cae8 size=01818h (  6168) load
I (307) esp_image: segment 4: paddr=000ec7a8 vaddr=40374000 size=15414h ( 87060) load
I (339) boot: Loaded app from partition at offset 0x10000
I (339) boot: Disabling RNG early entropy source...
I (350) cpu_start: Multicore app
I (360) cpu_start: Pro cpu start user code
I (360) cpu_start: cpu freq: 160000000 Hz
I (360) cpu_start: Application information:
I (363) cpu_start: Project name:     esp-miner
I (368) cpu_start: App version:      v2.1.6
I (373) cpu_start: Compile time:     May 26 2024 14:44:58
I (379) cpu_start: ELF file SHA256:  aa00b2217...
I (385) cpu_start: ESP-IDF:          v5.2.1
I (389) cpu_start: Min chip rev:     v0.0
I (394) cpu_start: Max chip rev:     v0.99 
I (399) cpu_start: Chip rev:         v0.2
I (404) heap_init: Initializing. RAM available for dynamic allocation:
I (411) heap_init: At 3FCA3B70 len 00045BA0 (278 KiB): RAM
I (417) heap_init: At 3FCE9710 len 00005724 (21 KiB): RAM
I (423) heap_init: At 3FCF0000 len 00008000 (32 KiB): DRAM
I (429) heap_init: At 600FE010 len 00001FD8 (7 KiB): RTCRAM
I (437) spi_flash: detected chip: gd
I (440) spi_flash: flash io: dio
W (444) i2c: This driver is an old driver, please migrate your application code to adapt `driver/i2c_master.h`
W (455) ADC: legacy driver is deprecated, please migrate to `esp_adc/adc_oneshot.h`
I (463) sleep: Configure to isolate all GPIO pins in sleep state
I (470) sleep: Enable automatic switching of GPIO sleep configuration
I (477) main_task: Started on CPU0
I (487) main_task: Calling app_main()
I (527) miner: NVS_CONFIG_ASIC_FREQ 490.000000
I (527) miner: ASIC: BM1368
I (527) miner: Welcome to the bitaxe!
```

### solobito on 2024-05-29

Ok.. I've realized that `A stack overflow in task httpd has been detected.` after `httpd_txrx: httpd_sock_err: error in ...` is due to the loss of Wi-Fi connection. The proof is that every time I disconnect the router, it shows the HTTP error. Therefore, these restarts are more related to this issue. My Wifi signal is fine, but for some reason, it loses connection, and this error is not handled correctly. This issue has already been addressed in https://github.com/skot/ESP-Miner/issues/105#issuecomment-1948424186, although it has not yet been resolved. Therefore, although this causes restarts, it is a different bug from `Guru Meditation Error: Core 0 panic'ed (Interrupt wdt timeout on CPU0).`

It restarts after losing the Wifi signal. Logs:
```
I (648648) asic_result: Nonce difficulty 265.51 of 364.
I (649148) wifi:bcn_timeout,ap_probe_send_start
I (651658) wifi:ap_probe_send over, resett wifi status to disassoc
I (651658) wifi:state: run -> init (0xc800)
I (651658) wifi:pm stop, total sleep time: 458159160 us / 642723369 us

I (651668) wifi:<ba-del>idx:1, tid:0
I (651668) wifi:<ba-del>idx:0, tid:5
I (651668) wifi:new:<4,0>, old:<4,1>, ap:<255,255>, sta:<4,0>, prof:1, snd_ch_cfg:0x0
I (654178) wifi station: Retrying WiFi connection...
W (654178) httpd_txrx: httpd_sock_err: error in recv : 113
E (654178) stratum_api: recv
W (654178) httpd_txrx: httpd_sock_err: error in send : 113
W (654188) httpd_txrx: httpd_sock_err: error in send : 128
W (654178) httpd_txrx: httpd_sock_err: error in send : 128
W (654188) httpd_txrx: httpd_sock_err: error in send : 128
W (654208) httpd_txrx: httpd_sock_err: error in send : 128

***ERROR*** A stack overflow in task httpd has been detected.


Backtrace: 0x40375c42:0x3fcbd070 0x4037d835:0x3fcbd090 0x4037e7ee:0x3fcbd0b0 0x4037fcb3:0x3fcbd130 0x4037e8b4:0x3fcbd150 0x4037e8aa:0x00000000 |<-CORRUPTED
0x40375c42: panic_abort at /Users/user/esp/esp-idf/components/esp_system/panic.c:463
0x4037d835: esp_system_abort at /Users/user/esp/esp-idf/components/esp_system/port/esp_system_chip.c:92
0x4037e7ee: vApplicationStackOverflowHook at /Users/user/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/xtensa/port.c:553
0x4037fcb3: vTaskSwitchContext at /Users/user/esp/esp-idf/components/freertos/FreeRTOS-Kernel/tasks.c:3667 (discriminator 7)
0x4037e8b4: _frxt_dispatch at /Users/user/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/xtensa/portasm.S:451
0x4037e8aa: _frxt_int_exit at /Users/user/esp/esp-idf/components/freertos/FreeRTOS-Kernel/portable/xtensa/portasm.S:246





ELF file SHA256: 17cd032ee

Rebooting...
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0xc (RTC_SW_CPU_RST),boot:0x2a (SPI_FAST_FLASH_BOOT)
Saved PC:0x40375b7c
0x40375b7c: esp_restart_noos at /Users/user/esp/esp-idf/components/esp_system/port/soc/esp32s3/system_internal.c:158

SPIWP:0xee

```



### solobito on 2024-06-02

I continue to experience reboots and get the same errors: `httpd_txrx: httpd_sock_err` or `Guru Meditation Error: Core 0 panic'ed`. I have tried several versions of espidf and it happens with all of them. I have also tried older versions like 2.1.1 and it still occurs.

I have noticed that if I don't establish any WebSocket connection with the Bitaxe, it doesn't reboot. I had it running perfectly for a couple of days. It seems that the problem is with WebSockets. I am now using the latest release of espipf v5.3-beta1.

Maybe there is a big watchlog timeout? It could be that `httpd_ws_send_frame_async` is blocking or taking too long to execute. https://github.com/skot/ESP-Miner/blob/00d5a7386f259967c6fdccfcd0cb432d2008e756/main/http_server/http_server.c#L535

Does it make sense to add an `vTaskDelay()` here? or maybe send it in chunks?



### solobito on 2024-06-02

Ok... `vTaskDelay()` blocks other processes and does not solve the problem. There also doesn't seem to be an issue with frame size or timeout.

**In order to replicate the issue**, I establish a continuous WebSockets connection. I use this Python script [BitaxeLogger](https://github.com/solobito/BitaxeLogger) to save the logs to a file (the code may not look great, but it gets the job done). Once the script is started, it can take minutes or even tens of minutes, but eventually, the Bitaxe restarts. I use ckpool.

To prevent it from restarting after the error, I commented out this line: https://github.com/skot/ESP-Miner/blob/4bda726f38060e2ce839fdfa222d342b32cdcebc/main/http_server/http_server.c#L553

This way, the logs are again printed using vprintf. Then, logs are only available through the USB connection.

### benjamin-wilson on 2024-06-02

Hey, sorry I forgot to update this issue but we've identified the problem and will have a release soon.

### solobito on 2024-06-04

> Hey, sorry I forgot to update this issue but we've identified the problem and will have a release soon.

I don’t know if it’s easy to give a hint about where the error is so we can get an idea of how to solve it for now. I notice that I also get reboots if I make requests every 5 seconds via http apiserver/info (although many hours, or even a day, can pass without reboots). This is unlike a websocket connection, which tends to cause a reboot within a few minutes or hours. I’m trying to capture data to save and analyze later, and I suppose a normal user wouldn’t experience this as often. I haven’t been able to monitor all the reboots, but they seem to be caused by the same issue, something related to httpd.

*If you are going to publish the changes soon, then forget this comment 🙂

### benjamin-wilson on 2024-06-04

2.1.7 has been released which contains the latest fixes

### solobito on 2024-06-04

Thank you for the update. However, in my case, it does not resolve the restarts caused by httpd errors when constantly monitoring the logs.

### seepv on 2024-07-17

@solobito @skot
After replacing an Half-Defective-Chinese-Fan (The Fan-Sound has Changed and the Airflow was massively reduced) with an Noctua-Fan (NF-A4x20) the
Error:
```
stratum_api: Error: recv
stratum_api: Restarting System because of Error: recv
```
is gone and
the Bitaxe is running like a charm again (many hours not just minutes).

I assume some interference is causing the bitaxe to restart.
What do you think is it possible that the Bitaxe restarts caused by electric or/and magnetic interference?

```
"version":	"v2.1.8", "boardVersion":	"204",
"temp":	48 (Half-Defective-Chinese-Fan)
"temp":	58 (Noctua-Fan)
```

### solobito on 2024-07-21

@seepv I don't think so; I would rather say it is a multitasking and overflow problem. This always happens with the Python script discussed in #199 

### seepv on 2024-07-21

@solobito After the Fan-Replacement the Logs are always available - With the other fan, after some hours, the Logs are gone.
Does your Bitaxe have an Noctua-Fan ?
Does the Logs always show up in the AxeOS-WebUI ?

### solobito on 2024-07-21

Hi @seepv! I use a Nocturna fan and it also happens to me with a regular fan. Have you tried running the python script? It's hard for the Bitaxe to restart by looking at the logs on the web (AxeOS), but running the script usually causes a restart in a relatively short time.

### seepv on 2024-07-21

@solobito I have a Node-Red-Script that restarts the Bitaxe if sharesAccepted is Min == Max in e.g. 600s.
But with the Noctua-Fan the Bitaxe is running quite stable until the Wlan-Router restarts.
How long does it take for the python script to restart the Bitaxe ?

### solobito on 2024-07-25

Hi @seepv When a few minutes pass, it usually restarts, although sometimes it can take tens of minutes, but it ends up restarting in a relatively short time. This always happens when I run that script which is making HTTP requests while having an established WebSocket connection. If I don't run the script, I can have the Bitaxe on for weeks without it restarting.

Now I am using the master branch and the Bitaxe also restarts.
