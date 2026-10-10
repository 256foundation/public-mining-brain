# bitaxeorg/ESP-Miner issue #1975: Gamma 601 (BM1370): ASIC silently stops returning nonces mid-session, no error logged, restart required

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1975
> Collected: 2026-10-07
> Published: 2026-09-14

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1975
- State: open
- Author: diesmia-cell
- Opened: 2026-09-14
- Closed: n/a
- Labels: none

## Description



	•	Device Model: Gamma, Board 601
	•	ASIC: BM1370
	•	Firmware: v2.15.1 (ESP-IDF v6.0.2)
	•	Frequency/Voltage: stock (525 MHz at time of failure)
	•	Prior uptime before first occurrence: ~60 days stable, interrupted by an inadvertent power cycle

To Reproduce
No known reliable repro steps. Observed twice in one session: once requiring a restart after boot, once after ~75 minutes of normal runtime (59°C ASIC temp at last good reading, no thermal event).

Expected behavior
ASIC continues returning nonces indefinitely under normal operation, or failing that, some error/watchdog entry is logged when it stops.

Evidence
Log excerpt spanning the failure — job 6a72bdc00001dfcf dequeued, ~24s of fan_controller ticks on both sides, zero asic_result lines, no errors of any kind (no checksum failure, no preamble mismatch):
there are no asic_results in the realtime log. I grabbed a slug of processing between temperature checks….Inthink this will make sense. this slug should so results, I think:

₿ (6552463) fan_controller: Temp: 59.9°C, SetPoint: 60.0°C, Output: 49.2%
₿ (6554465) fan_controller: Temp: 60.0°C, SetPoint: 60.0°C, Output: 48.5%
₿ (6556462) fan_controller: Temp: 60.0°C, SetPoint: 60.0°C, Output: 50.4%
₿ (6558466) fan_controller: Temp: 59.9°C, SetPoint: 60.0°C, Output: 49.8%
₿ (6560462) fan_controller: Temp: 60.0°C, SetPoint: 60.0°C, Output: 49.8%
₿ (6562462) fan_controller: Temp: 59.9°C, SetPoint: 60.0°C, Output: 50.4%
₿ (6563453) stratum_api: rx: {"params":["6a72bdc00001dfcf","dae04ba4ed94c6d1498600da2b976323842df04a000105250000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff370368c10e0004b645a86a04bff630010c","0a636b706f6f6c1375772f736f6c6f2e636b706f6f6c2e6f72672ffffffffe03421758120000000017a914f39b4ef0a3643cacf67cc2a6a36b8a8a271672be87add65f000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9edb2dc83af8c003471d04865fa27058e2e81141ca579924e20f24844426e7b352867c10e00",["9817d41b09d84a39b196f20397b03af9bc02326b3feee5555553ffeda87b7d07","ab8513f66d22991f6c379d47a136ab84773791c91526af48c68f16587e049565","e4bb72b78bcd10dee3da63ca13c028a772428cd5d3f3889e85d1e2a862e9597e","63bb45f8292cde3d1913ce7c3aac1cf99c16a4f535ddd666d0df61fc9d6d42b0","e08e5f771d857fb88a5f9a01b7363a9e1fa8181fe44e300a0592317bc759ba26","cceb47b92c104f84fbb4a8f4d5d5402c6f2350b31076259d10f82730c9011e39","cf4c0cccd06cf717df5506e0073fbc4a569653132598dbb97cf9ef356d4e8eaa","624a356932bfdfc5df53c00f8b25edac5801d5db49d9d9c94d829d375dce71bb","dbe15f52833ca2609d11e516f5ebfea107b698028a43a67820327017ec1a2099","12eb8b90c728df11b72a9b5ba0907dae579dbbc27522b3d4081f7954a7872374","22570cf5e2519d6f980fcdf2a4016d5c10300d70322129327a5c32122ffb0108","904f6782b7662850bbdec0bba9adc89d24cb29a05ef250c700c4fa757db27eb0"],"20000000","1702355e","6aa845b6",false],"id":null,"method":"mining.notify"}
₿ (6563455) create_jobs_task: New Work Dequeued 6a72bdc00001dfcf
₿ (6563457) stratum_v1_task: BIP-54 signaling detected
₿ (6563457) stratum_v1_task: Scriptsig: ...E.j...0...ckpool.uw/solo.ckpool.org/
₿ (6563457) stratum_v1_task: Coinbase outputs: 3, total value: 314043887 sats
₿ (6563457) stratum_v1_task: Output 0: 3Pu6BAxepEWaxF4HFmq9aQ8sAM4sW6KnaL (307763010 sat) (Your payout address)
₿ (6563458) stratum_v1_task: Output 1: bc1q28kkr5hk4gnqe3evma6runjrd2pvqyp8fpwfzu (6280877 sat)
₿ (6563458) stratum_v1_task: Output 2: OP_RETURN: .!........4q.He.'.......y.N .HDBn{5(
₿ (6564462) fan_controller: Temp: 60.0°C, SetPoint: 60.0°C, Output: 51.0%
₿ (6566462) fan_controller: Temp: 60.0°C, SetPoint: 60.0°C, Output: 49.1%
₿ (6568462) fan_controller: Temp: 59.9°C, SetPoint: 60.0°C, Output: 48.5%
₿ (6570462) fan_controller: Temp: 60.0°C, SetPoint: 60.0°C, Output: 49.7%
₿ (6572462) fan_controller: Temp: 59.9°C, SetPoint: 60.0°C, Output: 49.1%
₿ (6574462) fan_controller: Temp: 60.0°C, SetPoint: 60.0°C, Output: 49.1%
₿ (6576462) fan_controller: Temp: 60.0°C, SetPoint: 60.0°C, Output: 50.3%
₿ (6578462) fan_controller: Temp: 59.9°C, SetPoint: 60.0°C, Output: 48.4%
₿ (6580462) fan_controller: Temp: 60.0°C, SetPoint: 60.0°C, Output: 49.0%
₿ (6582473) fan_controller: Temp: 60.1°C, SetPoint: 60.0°C, Output: 50.9%
₿ (6584471) fan_controller: Temp: 59.9°C, SetPoint: 60.0°C, Output: 49.0%
₿ (6586466) fan_controller: Temp: 59.9°C, SetPoint: 60.0°C, Output: 48.4%


For contrast, log excerpt from immediately after a restart showing normal operation (asic_results firing every 1-2s as expected):
8307) fan_controller: Temp: 57.7°C, SetPoint: 60.0°C, Output: 34.4%
₿ (38558) asic_result: ID: 6a72bdc00001dfda, ASIC nr: 0, Core: 100/2, ver: 200A4000 Nonce 7E2CDFC9 diff 3083.9 of 10000.
₿ (38839) asic_result: ID: 6a72bdc00001dfda, ASIC nr: 0, Core: 82/13, ver: 2005A000 Nonce 5620F3A4 diff 646.7 of 10000.
₿ (39784) stratum_api: rx: {"params":["6a72bdc00001dfdb","265bd51c33dbee20c1b885ad502b3b3061d1083a000188ae0000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff370369c10e0004f746a86a04911bd4000c","0a636b706f6f6c1375772f736f6c6f2e636b706f6f6c2e6f72672ffffffffe03c8774f120000000017a914f39b4ef0a3643cacf67cc2a6a36b8a8a271672be87a0a95f000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9edfd1f5b389a05739bb22d76997426b17b53ffbbb89d691db37825f76204233bdf68c10e00",["25340181ae4838aef3d87b1c248525c557842289eccefc0b35c2e17b7a8c96b2","08d6a88719e2360d78f730caaad194fbc468a14b8da35b628e39ffa98906e09d","44cde3e2ebc686313543aff84c56735f9fff7913d7aad63f6cea416b14e05159","802b4fd4f651a296413f0ec5528796eb8a14ebfb500daaeaf6d8c0a231dcd76d","808c7b2546f98a683e23d08bc18f8123f6a4595d3daeaeaf2b8541b3d6e0574e","1f8ac4f3091f36281b17cd59aee7a9ef3d1b5214715533dce8578b030647ab82","ed3cfdced5d0980fdf5d2cee0dd2c94c9393c253c11751b14a67e470c47f5fe8","a2b61f151cff2f8d4f8c893d1378ec0e4a8cc0b05624b073f324f4578fbb85f2","5dc97352ce976259837fc40cc534f97d3652e14b06073858fce63b989c21e61b","97927f12c44ac7715d7e3ba046ac7309e913ad6d3ee54283b67885d23d7138dc","e777718ba2bf8ca0bbc8c603544175642705208349658ea5bb81128eb9b7797a"],"20000000","1702355e","6aa846f7",false],"id":null,"method":"mining.notify"}
₿ (39787) create_jobs_task: New Work Dequeued 6a72bdc00001dfdb
₿ (39788) create_jobs_task: New pool difficulty 1000.00
₿ (39791) stratum_v1_task: BIP-54 signaling detected
₿ (39792) stratum_v1_task: Coinbase outputs: 3, total value: 313467240 sats
₿ (39792) stratum_v1_task: Output 0: 3Pu6BAxepEWaxF4HFmq9aQ8sAM4sW6KnaL (307197896 sat) (Your payout address)
₿ (39792) stratum_v1_task: Output 1: bc1q28kkr5hk4gnqe3evma6runjrd2pvqyp8fpwfzu (6269344 sat)
₿ (39792) stratum_v1_task: Output 2: OP_RETURN: .!....[8..s..-v.t&.{S....i..x%.b.#;.
₿ (40308) fan_controller: Temp: 57.9°C, SetPoint: 60.0°C, Output: 35.8%
₿ (40866) asic_result: ID: 6a72bdc00001dfdb, ASIC nr: 0, Core: 12/11, ver: 20056000 Nonce B5B26A19 diff 705.0 of 1000.
₿ (41240) asic_result: ID: 6a72bdc00001dfdb, ASIC nr: 0, Core: 64/5, ver: 2000A000 Nonce D8E06781 diff 803.8 of 1000.
₿ (41471) asic_result: ID: 6a72bdc00001dfdb, ASIC nr: 0, Core: 6/11, ver: 20096000 Nonce B632A70C diff 873.6 of 1000.
₿ (41770) asic_result: ID: 6a72bdc00001dfdb, ASIC nr: 0, Core: 100/0, ver: 20020000 Nonce E73249C8 diff 505.2 of 1000.
₿ (41905) httpd_txrx: httpd_sock_err: error in recv : 104
₿ (42119) asic_result: ID: 6a72bdc00001dfdb, ASIC nr: 0, Core: 65/9, ver: 200D2000 Nonce 8B7E3983 diff 441.8 of 1000.
₿ (42307) fan_controller: Temp: 58.1°C, SetPoint: 60.0°C, Output: 36.1%
₿ (43031) asic_result: ID: 6a72bdc00001dfdb, ASIC nr: 0, Core: 95/12, ver: 200B8000 Nonce 3DC156BE diff 279.9 of 1000.
₿ (44024) asic_result: ID: 6a72bdc00001dfdb, ASIC nr: 0, Core: 112/14, ver: 2009C000 Nonce BC58FCE1 diff 547.1 of 1000.
₿ (44307) fan_controller: Temp: 58.4°C, SetPoint: 60.0°C, Output: 37.6%
₿ (46307) fan_controller: Temp: 58.5°C, SetPoint: 60.0°C, Output: 37.9%
₿ (46416) asic_result: ID: 6a72bdc00001dfdb, ASIC nr: 0, Core: 117/0, ver: 20060000 Nonce E49A47EA diff 330.3 of 1000.
₿ (46540) stratum_api: tx: {"id":5,"method":"mining.submit","params":["3Pu6BAxepEWaxF4HFmq9aQ8sAM4sW6KnaL","6a72bdc00001dfdb","0c00000000000000","6aa846f7","9ae5186c","000ba000"]}
₿ (46540) asic_result: Processing time: 2.5 ms
₿ (46541) asic_result: ID: 6a72bdc00001dfdb, ASIC nr: 0, Core: 54/13, ver: 200BA000 Nonce 9AE5186C diff 1313.4 of 1000.
₿ (46620) stratum_api: rx: {"result":true,"error":null,"id":5}
₿ (46621) stratum_api: Result success
₿ (46621) stratum_v1_task: message result accepted
₿ (46622) stratum_v1_task: Stratum response time: 80.4 ms
₿ (46773) asic_result: ID: 6a72bdc00001dfdb, ASIC nr: 0, Core: 73/9, ver: 20012000 Nonce DC94BE93 diff 361.1 of 1000.
₿ (48307) fan_controller: Temp: 58.7°C, SetPoint: 60.0°C, Output: 38.3%
₿ (49120) asic_result: ID: 6a72bdc00001dfdb, ASIC nr: 0, Core: 61/12, ver: 200D8000 Nonce 71935A7A diff 465.6 of 1000.
₿ (50307) fan_controller: Temp: 58.9°C, SetPoint: 60.0°C, Output: 39.3%
₿ (50597) asic_result: ID: 6a72bdc00001dfdb, ASIC nr: 0, Core: 13/4, ver: 200A8000 Nonce AC89721B diff 371.5 of 1000.
₿ (51995) stratum_api: tx: {"id":6,"method":"mining.submit","params":["3Pu6BAxepEWaxF4HFmq9aQ8sAM4sW6KnaL","6a72bdc00001dfdb","1700000000000000","6aa846f7","9dd50206","00092000"]}
₿ (51996) asic_result: Processing time: 2.4 ms
₿ (51996) asic_result: ID: 6a72bdc00001dfdb, ASIC nr: 0, Core: 3/9, ver: 20092000 Nonce 9DD50206 diff 5571.3 of 1000.
₿ (52096) stratum_api: rx: {"result":true,"error":null,"id":6}
₿ (52097) stratum_api: Result success
₿ (52098) stratum_v1_task: message result accepted
₿ (52098) stratum_v1_task: Stratum response time: 101.3 ms
₿ (52176) asic_result: ID: 6a72bdc00001dfdb, ASIC nr: 0, Core: 29/12, ver: 200D8000 Nonce E351BC3B diff 505.1 of 1000.
₿ (52307) fan_controller: Temp: 59.0°C, SetPoint: 60.0°C, Output: 39.1%
₿ (52482) stratum_api: tx: {"id":7,"method":"mining.submit","params":["3Pu6BAxepEWaxF4HFmq9aQ8sAM4sW6KnaL","6a72bdc00001dfdb","1800000000000000","6aa846f7","8a0e8acd","0006a000"]}
₿ (52482) asic_result: Processing time: 2.3 ms
₿ (52484) asic_result: ID: 6a72bdc00001dfdb, ASIC nr: 0, Core: 102/5, ver: 2006A000 Nonce 8A0E8ACD diff 1014.2 of 1000.
₿ (52555) stratum_api: rx: {"result":true,"error":null,"id":7}
₿ (52556) stratum_api: Result success
₿ (52557) stratum_v1_task: message result accepted
₿ (52557) stratum_v1_task: Stratum response time: 73.4 ms
₿ (54307) fan_controller: Temp: 59.2°C, SetPoint: 60.0°C, Output: 39.5%
₿ (55891) asic_result: ID: 6a72bdc00001dfdb, ASIC nr: 0, Core: 102/15, ver: 2005E000 Nonce B6D551CC diff 649.6 of 1000.

Happy to provide more if useful — I have full logs from both the failure and post-restart recovery.


## Comments

### mutatrum on 2026-09-15

This looks like #1053. What's the reported Input Voltage?

### diesmia-cell on 2026-09-16

hey, there. 5V reported. btw, I unplugged it and let it sit for a few hours, fired it back up, and it have been running non-stop. not sure if that is useful or not. Feels to ke like a timing issue/race condition that fully shutting down resolved. will update if it happens again.
