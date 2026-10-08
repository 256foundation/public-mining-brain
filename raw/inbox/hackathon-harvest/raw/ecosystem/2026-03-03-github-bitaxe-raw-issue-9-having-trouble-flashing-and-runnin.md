# bitaxeorg/bitaxe-raw issue #9: Having trouble flashing and running bitaxe-raw

> Source: https://github.com/bitaxeorg/bitaxe-raw/issues/9
> Collected: 2026-10-07
> Published: 2026-03-03

- Repository: bitaxeorg/bitaxe-raw
- Type: issue
- Number: 9
- State: closed
- Author: jayrmotta
- Opened: 2026-03-03
- Closed: 2026-07-28
- Labels: none

## Description

Hi!

It's my second time flashing bitaxe-raw, the first time I had an issue with the app descriptor not found running the main branch but an LLM helped me workaround it by creating a C file and making some changes to the code which I unfortunately discarded. That version is working well on my first BitAxe, but I got a new BitAxe and I can't get it to work with bitaxe-raw.

I'm running branch `esp-hal-update` which doesn't fail with the app descriptor missing.

## Tooling

`cargo & rustc 1.92.0-nightly`
`espflash 4.3.0`

## Flashing

```bash
▪ cargo espflash flash --release --chip esp32s3
✔ Use serial port '/dev/ttyACM0' - USB JTAG/serial debug unit? · yes
✔ Remember this serial port for future use? · no
[2026-03-03T19:37:49Z INFO ] Serial port: '/dev/ttyACM0'
[2026-03-03T19:37:49Z INFO ] Connecting...
[2026-03-03T19:37:49Z INFO ] Using flash stub
    Finished `release` profile [optimized + debuginfo] target(s) in 0.09s
[2026-03-03T19:37:49Z WARN ] Monitor options were provided, but `--monitor/-M` flag isn't set. These options will be ignored.
Chip type:         esp32s3 (revision v0.2)
Crystal frequency: 40 MHz
Flash size:        16MB
Features:          WiFi, BLE, Embedded Flash
MAC address:       30:ed:a0:a6:e5:54
App/part. size:    152,992/16,384,000 bytes, 0.93%
[00:00:00] [========================================]      14/14      0x0      Verifying... OK!                         
[00:00:00] [========================================]       1/1       0x8000   Verifying... OK!                         
[00:00:01] [========================================]      64/64      0x10000  Verifying... OK!                         
[2026-03-03T19:37:51Z INFO ] Flashing has completed!
```

Then I check the serial ports, press and release RESET on the BitAxe:

```bash
▪ ls /dev/ttyACM* 2>/dev/null
/dev/ttyACM0
▪ ls /dev/ttyACM* 2>/dev/null
/dev/ttyACM0  /dev/ttyACM1
```

Looks promising, proceed to run Mujina:

```bash
▪ RUST_LOG=mujina_miner=trace cargo run
   Compiling mujina-miner v0.1.0 (<path to>/mujina/mujina-miner)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 5.55s
     Running `target/debug/mujina-minerd`
16:42:07 INFO  daemon: Using dummy job source (set MUJINA_POOL_URL to use Stratum v1)
16:42:07 INFO  daemon: Started.
16:42:07 INFO  daemon: For debugging, set RUST_LOG=mujina_miner=debug or trace.
16:42:07 DEBUG job_source::dummy: Emitting initial job
               job_id=dummy-0
16:42:07 DEBUG scheduler: Source registered
               source_id=DefaultKey(1v1), name=dummy
16:42:07 DEBUG scheduler: UpdateJob received
               source=dummy, job_id=dummy-0
16:42:07 DEBUG scheduler: No threads yet, job cached for later
               source=dummy
16:42:07 INFO  api::server: API server listening.
               url=http://127.0.0.1:7785
16:42:07 INFO  backplane: Hash board connected via USB.
               board=Bitaxe Gamma, vid=c0de, pid=cafe, manufacturer=OSMU, product=Bitaxe, serial=819c1976
16:42:07 DEBUG board::bitaxe: Opening Bitaxe Gamma serial ports
               serial=819c1976, control=/dev/ttyACM0, data=/dev/ttyACM1
16:42:07 TRACE board::bitaxe: Holding ASIC in reset during power initialization
16:42:07 DEBUG mgmt_protocol::bitaxe_raw::gpio: GPIO write
               pin=0, value=Low
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=0, page=GPIO, cmd=0x00, data=00, frame=07 00 00 00 06 00 00
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=0, status=OK, data=00, frame=01 00 00 00
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=1, page=I2C, cmd=0x10, data=a0 86 01 00, frame=0a 00 01 00 05 10 a0 86 01 00
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=1, status=OK, data=a0 86 01 00, frame=04 00 01 a0 86 01 00
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=2, page=I2C, cmd=0x40, data=4c fe 01, frame=09 00 02 00 05 40 4c fe 01
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=2, status=OK, data=5d, frame=01 00 02 5d
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=3, page=I2C, cmd=0x40, data=4c fd 01, frame=09 00 03 00 05 40 4c fd 01
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=3, status=OK, data=28, frame=01 00 03 28
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=4, page=I2C, cmd=0x40, data=4c ff 01, frame=09 00 04 00 05 40 4c ff 01
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=4, status=OK, data=01, frame=01 00 04 01
16:42:07 DEBUG peripheral::emc2101: Detected EMC2101 variant
               mfg_id=0x5d, product_id=0x28, revision=0x01
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=5, page=I2C, cmd=0x40, data=4c 03 01, frame=09 00 05 00 05 40 4c 03 01
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=5, status=OK, data=00, frame=01 00 05 00
16:42:07 TRACE peripheral::emc2101: Current CONFIG register: 0x00
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=6, page=I2C, cmd=0x20, data=4c 03 04, frame=09 00 06 00 05 20 4c 03 04
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=6, status=OK, data=02, frame=01 00 06 02
16:42:07 TRACE peripheral::emc2101: Updated CONFIG register to: 0x04
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=7, page=I2C, cmd=0x20, data=4c 4a 23, frame=09 00 07 00 05 20 4c 4a 23
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=7, status=OK, data=02, frame=01 00 07 02
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=8, page=I2C, cmd=0x20, data=4c 4c 3f, frame=09 00 08 00 05 20 4c 4c 3f
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=8, status=OK, data=02, frame=01 00 08 02
16:42:07 DEBUG board::bitaxe: Fan speed set to 100%
16:42:07 DEBUG peripheral::tps546: Initializing TPS546D24A power regulator
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=9, page=I2C, cmd=0x40, data=24 ad 07, frame=09 00 09 00 05 40 24 ad 07
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=9, status=OK, data=06 54 49 54 6d 24 62, frame=07 00 09 06 54 49 54 6d 24 62
16:42:07 DEBUG peripheral::tps546: Device ID: 54 49 54 6D 24 62
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=10, page=I2C, cmd=0x20, data=24 01 00, frame=09 00 0a 00 05 20 24 01 00
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=10, status=OK, data=02, frame=01 00 0a 02
16:42:07 DEBUG peripheral::tps546: Power output turned off
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=11, page=I2C, cmd=0x20, data=24 02 1f, frame=09 00 0b 00 05 20 24 02 1f
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=11, status=OK, data=02, frame=01 00 0b 02
16:42:07 DEBUG peripheral::tps546: ON_OFF_CONFIG set to 0x1F (PowerUp from CONTROL, OPERATION cmd enabled, CONTROL pin present, Active high, Turn-off delay enabled)
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=12, page=I2C, cmd=0x40, data=24 20 01, frame=09 00 0c 00 05 40 24 20 01
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=12, status=OK, data=97, frame=01 00 0c 97
16:42:07 DEBUG peripheral::tps546: VOUT_MODE: 0x97
16:42:07 TRACE peripheral::tps546: ---Writing new config values to TPS546---
16:42:07 TRACE peripheral::tps546: Setting PHASE: 00
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=13, page=I2C, cmd=0x20, data=24 04 00, frame=09 00 0d 00 05 20 24 04 00
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=13, status=OK, data=02, frame=01 00 0d 02
16:42:07 TRACE peripheral::tps546: Setting FREQUENCY: 650kHz
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=14, page=I2C, cmd=0x20, data=24 33 8a 02, frame=0a 00 0e 00 05 20 24 33 8a 02
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=14, status=OK, data=03, frame=01 00 0e 03
16:42:07 TRACE peripheral::tps546: Setting VIN_ON: 4.80V
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=15, page=I2C, cmd=0x20, data=24 35 66 ca, frame=0a 00 0f 00 05 20 24 35 66 ca
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=15, status=OK, data=03, frame=01 00 0f 03
16:42:07 TRACE peripheral::tps546: Setting VIN_OFF: 4.50V
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=16, page=I2C, cmd=0x20, data=24 36 40 ca, frame=0a 00 10 00 05 20 24 36 40 ca
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=16, status=OK, data=03, frame=01 00 10 03
16:42:07 TRACE peripheral::tps546: Setting VIN_OV_FAULT_LIMIT: 6.50V
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=17, page=I2C, cmd=0x20, data=24 55 40 cb, frame=0a 00 11 00 05 20 24 55 40 cb
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=17, status=OK, data=03, frame=01 00 11 03
16:42:07 TRACE peripheral::tps546: Setting VIN_OV_FAULT_RESPONSE: 0xB7
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=18, page=I2C, cmd=0x20, data=24 56 b7, frame=09 00 12 00 05 20 24 56 b7
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=18, status=OK, data=02, frame=01 00 12 02
16:42:07 TRACE peripheral::tps546: Setting VOUT SCALE: 0.25
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=19, page=I2C, cmd=0x20, data=24 29 00 aa, frame=0a 00 13 00 05 20 24 29 00 aa
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=19, status=OK, data=03, frame=01 00 13 03
16:42:07 TRACE peripheral::tps546: Setting VOUT_COMMAND: 1.15V
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=20, page=I2C, cmd=0x40, data=24 20 01, frame=09 00 14 00 05 40 24 20 01
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=20, status=OK, data=97, frame=01 00 14 97
16:42:07 DEBUG peripheral::tps546: Cached VOUT_MODE: 0x97
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=21, page=I2C, cmd=0x20, data=24 21 4d 02, frame=0a 00 15 00 05 20 24 21 4d 02
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=21, status=OK, data=03, frame=01 00 15 03
16:42:07 TRACE peripheral::tps546: Setting VOUT_MAX: 2.00V
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=22, page=I2C, cmd=0x20, data=24 24 00 04, frame=0a 00 16 00 05 20 24 24 00 04
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=22, status=OK, data=03, frame=01 00 16 03
16:42:07 TRACE peripheral::tps546: Setting VOUT_MIN: 1.00V
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=23, page=I2C, cmd=0x20, data=24 2b 00 02, frame=0a 00 17 00 05 20 24 2b 00 02
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=23, status=OK, data=03, frame=01 00 17 03
16:42:07 TRACE peripheral::tps546: Setting VOUT_OV_FAULT_LIMIT: 1.25
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=24, page=I2C, cmd=0x20, data=24 40 80 02, frame=0a 00 18 00 05 20 24 40 80 02
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=24, status=OK, data=03, frame=01 00 18 03
16:42:07 TRACE peripheral::tps546: Setting VOUT_OV_WARN_LIMIT: 1.16
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=25, page=I2C, cmd=0x20, data=24 42 52 02, frame=0a 00 19 00 05 20 24 42 52 02
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=25, status=OK, data=03, frame=01 00 19 03
16:42:07 TRACE peripheral::tps546: Setting VOUT_MARGIN_HIGH: 1.10
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=26, page=I2C, cmd=0x20, data=24 25 33 02, frame=0a 00 1a 00 05 20 24 25 33 02
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=26, status=OK, data=03, frame=01 00 1a 03
16:42:07 TRACE peripheral::tps546: Setting VOUT_MARGIN_LOW: 0.90
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=27, page=I2C, cmd=0x20, data=24 26 cd 01, frame=0a 00 1b 00 05 20 24 26 cd 01
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=27, status=OK, data=03, frame=01 00 1b 03
16:42:07 TRACE peripheral::tps546: Setting VOUT_UV_WARN_LIMIT: 0.90
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=28, page=I2C, cmd=0x20, data=24 43 cd 01, frame=0a 00 1c 00 05 20 24 43 cd 01
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=28, status=OK, data=03, frame=01 00 1c 03
16:42:07 TRACE peripheral::tps546: Setting VOUT_UV_FAULT_LIMIT: 0.75
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=29, page=I2C, cmd=0x20, data=24 44 80 01, frame=0a 00 1d 00 05 20 24 44 80 01
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=29, status=OK, data=03, frame=01 00 1d 03
16:42:07 TRACE peripheral::tps546: ----- IOUT
16:42:07 TRACE peripheral::tps546: Setting IOUT_OC_WARN_LIMIT: 25.00A
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=30, page=I2C, cmd=0x20, data=24 4a 20 db, frame=0a 00 1e 00 05 20 24 4a 20 db
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=30, status=OK, data=03, frame=01 00 1e 03
16:42:07 TRACE peripheral::tps546: Setting IOUT_OC_FAULT_LIMIT: 30.00A
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=31, page=I2C, cmd=0x20, data=24 46 c0 db, frame=0a 00 1f 00 05 20 24 46 c0 db
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=31, status=OK, data=03, frame=01 00 1f 03
16:42:07 TRACE peripheral::tps546: Setting IOUT_OC_FAULT_RESPONSE: 0xC0
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=32, page=I2C, cmd=0x20, data=24 47 c0, frame=09 00 20 00 05 20 24 47 c0
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=32, status=OK, data=02, frame=01 00 20 02
16:42:07 TRACE peripheral::tps546: ----- TEMPERATURE
16:42:07 TRACE peripheral::tps546: Setting OT_WARN_LIMIT: 105 degC
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=33, page=I2C, cmd=0x20, data=24 51 48 eb, frame=0a 00 21 00 05 20 24 51 48 eb
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=33, status=OK, data=03, frame=01 00 21 03
16:42:07 TRACE peripheral::tps546: Setting OT_FAULT_LIMIT: 145 degC
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=34, page=I2C, cmd=0x20, data=24 4f 44 f2, frame=0a 00 22 00 05 20 24 4f 44 f2
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=34, status=OK, data=03, frame=01 00 22 03
16:42:07 TRACE peripheral::tps546: Setting OT_FAULT_RESPONSE: 0xFF
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=35, page=I2C, cmd=0x20, data=24 50 ff, frame=09 00 23 00 05 20 24 50 ff
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=35, status=OK, data=02, frame=01 00 23 02
16:42:07 TRACE peripheral::tps546: ----- TIMING
16:42:07 TRACE peripheral::tps546: Setting TON_DELAY: 0ms
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=36, page=I2C, cmd=0x20, data=24 60 00 00, frame=0a 00 24 00 05 20 24 60 00 00
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=36, status=OK, data=03, frame=01 00 24 03
16:42:07 TRACE peripheral::tps546: Setting TON_RISE: 3ms
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=37, page=I2C, cmd=0x20, data=24 61 00 c3, frame=0a 00 25 00 05 20 24 61 00 c3
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=37, status=OK, data=03, frame=01 00 25 03
16:42:07 TRACE peripheral::tps546: Setting TON_MAX_FAULT_LIMIT: 0ms
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=38, page=I2C, cmd=0x20, data=24 62 00 00, frame=0a 00 26 00 05 20 24 62 00 00
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=38, status=OK, data=03, frame=01 00 26 03
16:42:07 TRACE peripheral::tps546: Setting TON_MAX_FAULT_RESPONSE: 0x3B
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=39, page=I2C, cmd=0x20, data=24 63 3b, frame=09 00 27 00 05 20 24 63 3b
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=39, status=OK, data=02, frame=01 00 27 02
16:42:07 TRACE peripheral::tps546: Setting TOFF_DELAY: 0ms
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=40, page=I2C, cmd=0x20, data=24 64 00 00, frame=0a 00 28 00 05 20 24 64 00 00
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=40, status=OK, data=03, frame=01 00 28 03
16:42:07 TRACE peripheral::tps546: Setting TOFF_FALL: 0ms
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=41, page=I2C, cmd=0x20, data=24 65 00 00, frame=0a 00 29 00 05 20 24 65 00 00
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=41, status=OK, data=03, frame=01 00 29 03
16:42:07 TRACE peripheral::tps546: Setting PIN_DETECT_OVERRIDE: 0xFFFF
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=42, page=I2C, cmd=0x20, data=24 ee ff ff, frame=0a 00 2a 00 05 20 24 ee ff ff
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=42, status=OK, data=03, frame=01 00 2a 03
16:42:07 DEBUG peripheral::tps546: TPS546 configuration written successfully
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=43, page=I2C, cmd=0x40, data=24 79 02, frame=09 00 2b 00 05 40 24 79 02
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=43, status=OK, data=40 08, frame=02 00 2b 40 08
16:42:07 DEBUG peripheral::tps546: STATUS_WORD after config: 0x0840 (PGOOD, OFF)
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=44, page=I2C, cmd=0x20, data=24 21 4d 02, frame=0a 00 2c 00 05 20 24 21 4d 02
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=44, status=OK, data=03, frame=01 00 2c 03
16:42:07 DEBUG peripheral::tps546: Output voltage set to 1.15V
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=45, page=I2C, cmd=0x20, data=24 03, frame=08 00 2d 00 05 20 24 03
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=45, status=OK, data=01, frame=01 00 2d 01
16:42:07 DEBUG peripheral::tps546: Cleared faults before turn-on
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=46, page=I2C, cmd=0x20, data=24 01 80, frame=09 00 2e 00 05 20 24 01 80
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=46, status=OK, data=02, frame=01 00 2e 02
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=47, page=I2C, cmd=0x40, data=24 01 01, frame=09 00 2f 00 05 40 24 01 01
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=47, status=OK, data=80, frame=01 00 2f 80
16:42:07 DEBUG peripheral::tps546: Power turned ON successfully, OPERATION = 0x80
16:42:07 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=48, page=I2C, cmd=0x40, data=24 79 02, frame=09 00 30 00 05 40 24 79 02
16:42:07 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=48, status=OK, data=00 08, frame=02 00 30 00 08
16:42:07 DEBUG peripheral::tps546: Power is ON, STATUS_WORD = 0x0800
16:42:07 DEBUG board::bitaxe: Core voltage set to 1.15V
16:42:08 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=49, page=I2C, cmd=0x40, data=24 8b 02, frame=09 00 31 00 05 40 24 8b 02
16:42:09 WARN  board::bitaxe: Failed to read core voltage: I2C error: I2C error: WriteRead failed: Control command timeout
16:42:09 DEBUG peripheral::tps546: === TPS546D24A Configuration Dump ===
16:42:09 DEBUG peripheral::tps546: --- Voltage Configuration ---
16:42:09 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=50, page=I2C, cmd=0x40, data=24 35 02, frame=09 00 32 00 05 40 24 35 02
16:42:09 WARN  board::bitaxe: Failed to dump TPS546 configuration: I2C error: I2C error: WriteRead failed: Unknown error code: 0x49
16:42:09 DEBUG board::bitaxe: Releasing ASIC from reset for discovery
16:42:09 DEBUG board::bitaxe: De-asserting ASIC nRST (GPIO 0 = high)
16:42:09 DEBUG mgmt_protocol::bitaxe_raw::gpio: GPIO write
               pin=0, value=High
16:42:09 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=51, page=GPIO, cmd=0x00, data=01, frame=07 00 33 00 06 00 01
16:42:09 ERROR backplane: Failed to create board
               board=Bitaxe Gamma, error=Hardware error: Failed to initialize board: Hardware control error: Failed to de-assert reset: I/O error: Control stream closed
```

Something is definitely wrong, run again:

```bash
▪ RUST_LOG=mujina_miner=trace cargo run
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.08s
     Running `target/debug/mujina-minerd`
16:42:59 INFO  daemon: Using dummy job source (set MUJINA_POOL_URL to use Stratum v1)
16:42:59 INFO  daemon: Started.
16:42:59 INFO  daemon: For debugging, set RUST_LOG=mujina_miner=debug or trace.
16:42:59 DEBUG job_source::dummy: Emitting initial job
               job_id=dummy-0
16:42:59 DEBUG scheduler: Source registered
               source_id=DefaultKey(1v1), name=dummy
16:42:59 DEBUG scheduler: UpdateJob received
               source=dummy, job_id=dummy-0
16:42:59 DEBUG scheduler: No threads yet, job cached for later
               source=dummy
16:42:59 INFO  api::server: API server listening.
               url=http://127.0.0.1:7785
16:42:59 INFO  backplane: Hash board connected via USB.
               board=Bitaxe Gamma, vid=c0de, pid=cafe, manufacturer=OSMU, product=Bitaxe, serial=819c1976
16:42:59 DEBUG board::bitaxe: Opening Bitaxe Gamma serial ports
               serial=819c1976, control=/dev/ttyACM0, data=/dev/ttyACM1
16:42:59 TRACE board::bitaxe: Holding ASIC in reset during power initialization
16:42:59 DEBUG mgmt_protocol::bitaxe_raw::gpio: GPIO write
               pin=0, value=Low
16:42:59 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=0, page=GPIO, cmd=0x00, data=00, frame=07 00 00 00 06 00 00
16:42:59 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=0, status=OK, data=00, frame=01 00 00 00
16:42:59 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=1, page=I2C, cmd=0x10, data=a0 86 01 00, frame=0a 00 01 00 05 10 a0 86 01 00
16:42:59 TRACE mgmt_protocol::bitaxe_raw: RX control
               id=1, status=OK, data=a0 86 01 00, frame=04 00 01 a0 86 01 00
16:42:59 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=2, page=I2C, cmd=0x40, data=4c fe 01, frame=09 00 02 00 05 40 4c fe 01
16:43:00 WARN  board::bitaxe: Failed to initialize EMC2101 fan controller: I2C error: I2C error: WriteRead failed: Control command timeout
16:43:00 DEBUG peripheral::tps546: Initializing TPS546D24A power regulator
16:43:00 TRACE mgmt_protocol::bitaxe_raw: TX control
               id=3, page=I2C, cmd=0x40, data=24 ad 07, frame=09 00 03 00 05 40 24 ad 07
16:43:00 ERROR board::bitaxe: Failed to initialize TPS546D24A power controller: I2C error: I2C error: WriteRead failed: Unknown error code: 0x49
16:43:00 ERROR backplane: Failed to create board
               board=Bitaxe Gamma, error=Hardware error: Failed to initialize board: Board initialization failed: Power controller init failed: I2C error: I2C error: WriteRead failed: Unknown error code: 0x49
```

A different error on the second execution. In some of my attempts with different branches, downgraded espflash, cargo flash, and trying to manually introduce the app descriptor on the main branch, it resulted in failure to flash due to app descriptor missing or it succeeded and resulted in the errors above. In one attempt I also saw a "packet too large" along the "control stream closed".

If anyone knows a deterministic path to building and flashing this so I can run Mujina with the BitAxe please share.

## Comments

### skot on 2026-03-05

It seems like everything is working well up until the point mujina enables the Bitaxe TPS546 voltage regulator. @rkuester any ideas?

### skot on 2026-03-05

I see from your comments in https://github.com/256foundation/mujina/pull/33 that everything was working on the first Bitaxe, but this problem seems unique to the second Bitaxe? That suggests a HW issue with the second Bitaxe. Is there any difference in the hardware between the two Bitaxe? Are they both Bitaxe Gamma 601? 

### jayrmotta on 2026-03-05

> I see from your comments in [256foundation/mujina#33](https://github.com/256foundation/mujina/pull/33) that everything was working on the first Bitaxe, but this problem seems unique to the second Bitaxe? That suggests a HW issue with the second Bitaxe. Is there any difference in the hardware between the two Bitaxe? Are they both Bitaxe Gamma 601?

The first is a 601 and the second is a 602.

A few minutes ago I just flashed the SV2 branch of ESP-miner I've been playing with onto the 602 and it worked fine, so that should discard the HW issue hypothesis. Then I flashed bitaxe-raw again, ran mujina and got to the same errors described in the issue.

### skot on 2026-03-06

I wonder if there is a change from 601 -> 602 that is not reflected in Mujina (but is in esp-miner). I'll take a look at the changes

### skot on 2026-03-09

I don't see any hardware changes from 601 -> 602 that should require any firmware changes.

I did see some errors like your log shows when using my Bitaxe 601 running bitaxe-raw with Mujina. It seems like the Mujina control serial buffer was somehow out of sync with the Bitaxe. I was going to look into it more, but when I restarted by bitaxe and Mujina, the problem went away 😳

### jayrmotta on 2026-03-10

Earlier today I had a session with @majoal0 and we sucessfully flashed his 602 then ran Mujina as expected. Also heard from @johnnyasantoss the same, I believe his might be a 601.

I honestly have no clue why it doesn't work on this new 602 I got, since it seems to run ESP-miner normally then I'm running out of clues. I will continue to experiment and see if I can figure what's wrong.

### rkuester on 2026-03-11

The first log seems to show I2C IO failing and perhaps even USB IO failing[^1] right after regulator output powering the ASIC was turned on. The second log shows I2C not working right from the start.

I wondered if this was some kind of brownout or other hardware issue when turning the regulator on, but if the board is working with esp-miner, it must not that simple.

It's worth pointing out that restarting Mujina doesn't take the entire system back to square one. The Bitaxe's microcontroller running bitaxe-raw remains powered on and not reset, and the peripherals like the regulator remain powered on and thus maintain some state too. Perhaps Mujina could and should do more to reset the Bitaxe, but for now, assume it's not doing much. If you really want a clean second run, at least reset the Bitaxe with its pushbutton, and perhaps even cycle its power to reset the regulator.

Is this a mainline build of Mujina or a Mujina with your local modifications, @jayrmotta? 

I'm at a bit of a loss at the moment too.

[^1]: See the "Control stream closed" message, although that might be secondary; e.g., a race during the teardown after the board failed to initialize.

### skot on 2026-03-11

> If you really want a clean second run, at least reset the Bitaxe with its pushbutton, and perhaps even cycle its power to reset the regulator.

I recommend doing a hard power cycle by pulling the plug. The reset button just resets the ESP32 and won't necessarily reset state in the voltage regulator, especially if you are running bitaxe-raw 


### jayrmotta on 2026-03-19

Well, I'm happy to informe the problem is gone, just don't ask me how. At some point I flashed the 602 again and it simply worked.

I won't dare speculating why yet, but I'll keep an eye 👀
