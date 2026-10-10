# bitaxeorg/ESP-Miner issue #286: After mining for a while without pool sending work, ASIC serial stalls

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/286
> Collected: 2026-10-07
> Published: 2024-08-13

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 286
- State: closed
- Author: skot
- Opened: 2024-08-13
- Closed: 2026-05-29
- Labels: bug

## Description

If I block all network traffic between the pool and esp-miner (from my router) so that no work is received, the bitaxe continues to mine.

The problem is after 10 minutes or so, we stop getting nonces from the ASIC. I can see the esp32 serial buffer filling up, so the ASIC is still sending bytes, we just aren't checking the RX queue.

At some point later something will happen and esp-miner will read all of the nonces from the serial queue all at once, throwing the hashrate calculation out of whack.

```
[network is blocked, but we're still mining from the work queue. that's OK]
I (2859508) create_jobs_task: Queued 10: 1940fcf (EN2: 5716)
I (2859628) bm1368Module: Job ID: 20, Core: 5/0, Ver: 02C60000
I (2859628) asic_result: Ver: 22C60000 Nonce 62D7010A diff 274.8 of 2048.
I (2859968) bm1368Module: Send Job: 38
I (2860008) create_jobs_task: Queued 10: 1940fcf (EN2: 5717)
I (2860468) bm1368Module: Send Job: 50
I (2860508) create_jobs_task: Queued 10: 1940fcf (EN2: 5718)
I (2860818) bm1368Module: Job ID: 50, Core: 48/13, Ver: 060BA000
I (2860818) asic_result: Ver: 260BA000 Nonce C05D0160 diff 738.4 of 2048.
I (2860968) bm1368Module: Send Job: 68
I (2861008) create_jobs_task: Queued 10: 1940fcf (EN2: 5719)
I (2861468) bm1368Module: Send Job: 00
I (2861508) create_jobs_task: Queued 10: 1940fcf (EN2: 5720)
I (2861518) bm1368Module: Job ID: 00, Core: 62/3, Ver: 00EC6000
I (2861518) asic_result: Ver: 20EC6000 Nonce 2DD9027C diff 1062.8 of 2048.
I (2861968) bm1368Module: Send Job: 18
I (2862008) create_jobs_task: Queued 10: 1940fcf (EN2: 5721)
I (2862468) bm1368Module: Send Job: 30
I (2862508) create_jobs_task: Queued 10: 1940fcf (EN2: 5722)
I (2862968) bm1368Module: Send Job: 48
I (2863008) create_jobs_task: Queued 10: 1940fcf (EN2: 5723)
I (2863368) bm1368Module: Job ID: 48, Core: 6/1, Ver: 06E42000
I (2863368) asic_result: Ver: 26E42000 Nonce A4E2010C diff 2094.3 of 2048.
I (2863368) stratum_api: tx: {"id": 215, "method": "mining.submit", "params": ["bc1qqkredrrxc0pqjpcyp8ku3ry46e40tp40zrf0k0.bitaxe", "1940fcf", "51160000", "66ba9110", "a4e2010c", "06e42000"]}
I (2863468) bm1368Module: Send Job: 60
I (2863508) create_jobs_task: Queued 10: 1940fcf (EN2: 5724)
[we stop getting nonces here from the ASIC serial, bad]
I (2863968) bm1368Module: Send Job: 78
I (2864008) create_jobs_task: Queued 10: 1940fcf (EN2: 5725)
I (2864468) bm1368Module: Send Job: 10
I (2864508) create_jobs_task: Queued 10: 1940fcf (EN2: 5726)
I (2864968) bm1368Module: Send Job: 28
I (2865008) create_jobs_task: Queued 10: 1940fcf (EN2: 5727)
I (2865468) bm1368Module: Send Job: 40
I (2865508) create_jobs_task: Queued 10: 1940fcf (EN2: 5728)
I (2865968) bm1368Module: Send Job: 58
I (2866008) create_jobs_task: Queued 10: 1940fcf (EN2: 5729)
I (2866468) bm1368Module: Send Job: 70
I (2866508) create_jobs_task: Queued 10: 1940fcf (EN2: 5730)
I (2866968) bm1368Module: Send Job: 08
I (2867008) create_jobs_task: Queued 10: 1940fcf (EN2: 5731)
[this continues for a long time]
...
[network is back on, and shortly after that we get A LOT of nonces (prolly from the big ESP32 serial buffer)]
I (3220208) create_jobs_task: Queued 10: 1946060 (EN2: 6444)
I (3220618) bm1368Module: Send Job: 00
I (3220708) create_jobs_task: Queued 10: 1946060 (EN2: 6445)
I (3221118) bm1368Module: Send Job: 18
I (3221208) create_jobs_task: Queued 10: 1946060 (EN2: 6446)
I (3221618) bm1368Module: Send Job: 30
I (3221708) create_jobs_task: Queued 10: 1946060 (EN2: 6447)
I (3222118) bm1368Module: Send Job: 48
I (3222208) create_jobs_task: Queued 10: 1946060 (EN2: 6448)
I (3222618) bm1368Module: Send Job: 60
I (3222708) create_jobs_task: Queued 10: 1946060 (EN2: 6449)
I (3222848) stratum_task: rx: {"id":180,"error":null,"result":true}
I (3222848) stratum_task: message result accepted
I (3222858) bm1368Module: Job ID: 28, Core: 68/9, Ver: 042F2000
I (3222858) asic_result: Ver: 242F2000 Nonce 5ABD0288 diff 0.0 of 2048.
I (3222878) bm1368Module: Job ID: 70, Core: 38/5, Ver: 0674A000
I (3222878) asic_result: Ver: 2674A000 Nonce 9D6B004C diff 0.0 of 2048.
I (3222898) bm1368Module: Job ID: 08, Core: 46/15, Ver: 00EBE000
I (3222898) asic_result: Ver: 20EBE000 Nonce 1144035C diff 0.0 of 2048.
I (3222918) bm1368Module: Job ID: 30, Core: 41/15, Ver: 0191E000
I (3222918) asic_result: Ver: 2191E000 Nonce AFB70252 diff 0.0 of 2048.
I (3222938) bm1368Module: Job ID: 10, Core: 36/13, Ver: 0329A000
I (3222938) asic_result: Ver: 2329A000 Nonce 94040248 diff 0.0 of 2048.
I (3222958) bm1368Module: Job ID: 28, Core: 3/9, Ver: 02FD2000
I (3222958) asic_result: Ver: 22FD2000 Nonce B81F0106 diff 0.0 of 2048.
I (3222978) bm1368Module: Job ID: 60, Core: 8/2, Ver: 001C4000
I (3222978) asic_result: Ver: 201C4000 Nonce A13F0310 diff 0.0 of 2048.
I (3222998) bm1368Module: Job ID: 60, Core: 34/11, Ver: 02456000
I (3222998) asic_result: Ver: 22456000 Nonce 896F0044 diff 0.0 of 2048.
I (3223018) bm1368Module: Job ID: 28, Core: 51/9, Ver: 07312000
I (3223018) asic_result: Ver: 27312000 Nonce D1F40166 diff 0.0 of 2048.
I (3223038) bm1368Module: Job ID: 28, Core: 8/4, Ver: 08728000
I (3223038) asic_result: Ver: 28728000 Nonce 90180210 diff 0.0 of 2048.
I (3223058) bm1368Module: Job ID: 58, Core: 38/6, Ver: 0686C000
I (3223058) asic_result: Ver: 2686C000 Nonce 6FD7004C diff 0.0 of 2048.
I (3223078) bm1368Module: Job ID: 60, Core: 47/5, Ver: 0760A000
I (3223078) asic_result: Ver: 2760A000 Nonce D418035E diff 0.0 of 2048.
I (3223088) bm1368Module: Job ID: 58, Core: 21/8, Ver: 02810000
I (3223088) asic_result: Ver: 22810000 Nonce 74B5022A diff 0.0 of 2048.
I (3223098) bm1368Module: Job ID: 00, Core: 53/8, Ver: 076D0000
I (3223098) asic_result: Ver: 276D0000 Nonce A81C016A diff 0.0 of 2048.
I (3223118) bm1368Module: Job ID: 78, Core: 56/2, Ver: 07664000
I (3223118) asic_result: Ver: 27664000 Nonce 1A7C0270 diff 0.0 of 2048.
I (3223118) bm1368Module: Send Job: 78
I (3223128) bm1368Module: Job ID: 58, Core: 17/5, Ver: 0582A000
I (3223128) asic_result: Ver: 2582A000 Nonce 77E50222 diff 0.0 of 2048.
I (3223148) bm1368Module: Job ID: 70, Core: 25/7, Ver: 031EE000
I (3223148) asic_result: Ver: 231EE000 Nonce 2BDB0132 diff 0.0 of 2048.
I (3223148) stratum_task: rx: {"id":181,"error":null,"result":true}
I (3223158) stratum_task: message result accepted
I (3223158) bm1368Module: Job ID: 08, Core: 62/9, Ver: 07D92000
I (3223168) asic_result: Ver: 27D92000 Nonce E4CE017C diff 0.0 of 2048.
I (3223188) bm1368Module: Job ID: 00, Core: 29/5, Ver: 083EA000
I (3223188) asic_result: Ver: 283EA000 Nonce 88F9013A diff 0.0 of 2048.
I (3223198) bm1368Module: Job ID: 30, Core: 1/15, Ver: 0779E000
I (3223198) asic_result: Ver: 2779E000 Nonce F9CA0002 diff 0.0 of 2048.
I (3223208) create_jobs_task: Queued 10: 1946060 (EN2: 6450)
I (3223218) bm1368Module: Job ID: 78, Core: 3/6, Ver: 0318C000
I (3223218) asic_result: Ver: 2318C000 Nonce 3E790106 diff 0.0 of 2048.
I (3223238) bm1368Module: Job ID: 28, Core: 48/10, Ver: 03FD4000
I (3223238) asic_result: Ver: 23FD4000 Nonce B9C20060 diff 0.0 of 2048.
I (3223248) bm1368Module: Job ID: 20, Core: 52/15, Ver: 0585E000
I (3223248) asic_result: Ver: 2585E000 Nonce 28280268 diff 0.0 of 2048.
I (3223258) bm1368Module: Job ID: 68, Core: 20/2, Ver: 074A4000
I (3223258) asic_result: Ver: 274A4000 Nonce BF540128 diff 0.0 of 2048.
I (3223278) bm1368Module: Job ID: 00, Core: 65/8, Ver: 03570000
I (3223278) asic_result: Ver: 23570000 Nonce 5F840082 diff 0.0 of 2048.
I (3223288) bm1368Module: Job ID: 78, Core: 55/6, Ver: 0840C000
I (3223288) asic_result: Ver: 2840C000 Nonce CC88016E diff 0.0 of 2048.
I (3223298) bm1368Module: Job ID: 28, Core: 26/10, Ver: 04F94000
I (3223308) asic_result: Ver: 24F94000 Nonce 2CCB0134 diff 0.0 of 2048.
I (3223318) bm1368Module: Job ID: 28, Core: 13/11, Ver: 05DF6000
I (3223318) asic_result: Ver: 25DF6000 Nonce 71FD001A diff 0.0 of 2048.
I (3223328) bm1368Module: Job ID: 40, Core: 48/15, Ver: 0475E000
I (3223328) asic_result: Ver: 2475E000 Nonce BE2E0060 diff 0.0 of 2048.
I (3223348) bm1368Module: Job ID: 58, Core: 4/14, Ver: 046DC000
I (3223348) asic_result: Ver: 246DC000 Nonce E9530208 diff 0.0 of 2048.
I (3223358) stratum_task: rx: {"id":182,"error":null,"result":true}
I (3223358) bm1368Module: Job ID: 08, Core: 51/12, Ver: 04950000
I (3223368) asic_result: Ver: 24950000 Nonce 13B60066 diff 0.0 of 2048.
I (3223368) stratum_task: message result accepted
I (3223378) bm1368Module: Job ID: 20, Core: 34/4, Ver: 011C8000
I (3223388) asic_result: Ver: 211C8000 Nonce 39C60044 diff 0.0 of 2048.
I (3223388) stratum_task: rx: {"id":183,"error":null,"result":true}
I (3223398) stratum_task: message result accepted
I (3223398) bm1368Module: Job ID: 50, Core: 37/1, Ver: 07542000
I (3223408) asic_result: Ver: 27542000 Nonce 8D70004A diff 0.0 of 2048.
I (3223408) stratum_task: rx: {"id":184,"error":null,"result":true}
I (3223428) stratum_task: message result accepted
I (3223428) bm1368Module: Job ID: 78, Core: 41/8, Ver: 027F0000
I (3223438) asic_result: Ver: 227F0000 Nonce 20030252 diff 0.0 of 2048.
I (3223438) stratum_task: rx: {"id":185,"error":null,"result":true}
I (3223448) stratum_task: message result accepted
I (3223448) bm1368Module: Job ID: 28, Core: 37/5, Ver: 065CA000
I (3223458) asic_result: Ver: 265CA000 Nonce 9B54024A diff 0.0 of 2048.
I (3223468) stratum_task: rx: {"id":186,"error":null,"result":true}
I (3223478) stratum_task: message result accepted
I (3223478) bm1368Module: Job ID: 58, Core: 12/4, Ver: 07B68000
I (3223488) asic_result: Ver: 27B68000 Nonce 60610118 diff 0.0 of 2048.
I (3223488) stratum_task: rx: {"id":187,"error":null,"result":true}
I (3223498) stratum_task: message result accepted
I (3223508) bm1368Module: Job ID: 08, Core: 63/9, Ver: 03B92000
I (3223518) asic_result: Ver: 23B92000 Nonce 1C6B017E diff 0.0 of 2048.
I (3223518) stratum_task: rx: {"id":188,"error":null,"result":true}
I (3223528) stratum_task: message result accepted
I (3223528) bm1368Module: Job ID: 20, Core: 76/7, Ver: 00E6E000
I (3223538) asic_result: Ver: 20E6E000 Nonce 6EDC0298 diff 0.0 of 2048.
I (3223558) stratum_task: rx: {"id":189,"error":null,"result":true}
I (3223558) bm1368Module: Job ID: 50, Core: 12/3, Ver: 064A6000
I (3223558) stratum_task: message result accepted
I (3223558) asic_result: Ver: 264A6000 Nonce FC2D0018 diff 0.0 of 2048.
I (3223588) bm1368Module: Job ID: 68, Core: 46/9, Ver: 01FF2000
I (3223588) asic_result: Ver: 21FF2000 Nonce DA4A025C diff 0.0 of 2048.
I (3223588) stratum_task: rx: {"id":190,"error":null,"result":true}
I (3223598) stratum_task: message result accepted
I (3223598) bm1368Module: Job ID: 48, Core: 24/0, Ver: 02860000
I (3223608) asic_result: Ver: 22860000 Nonce 706C0130 diff 0.0 of 2048.
I (3223618) bm1368Module: Send Job: 10
I (3223608) stratum_task: rx: {"id":191,"error":null,"result":true}
I (3223628) bm1368Module: Job ID: 40, Core: 33/15, Ver: 02F7E000
I (3223638) stratum_task: message result accepted
I (3223638) asic_result: Ver: 22F7E000 Nonce 5DDC0142 diff 0.0 of 2048.
I (3223658) bm1368Module: Job ID: 58, Core: 45/12, Ver: 07B78000
I (3223658) asic_result: Ver: 27B78000 Nonce 6DF7025A diff 0.0 of 2048.
I (3223658) stratum_task: rx: {"id":192,"error":null,"result":true}
I (3223668) stratum_task: message result accepted
I (3223668) bm1368Module: Job ID: 68, Core: 40/0, Ver: 05E00000
I (3223678) asic_result: Ver: 25E00000 Nonce E7E60150 diff 0.0 of 2048.
I (3223698) bm1368Module: Job ID: 00, Core: 10/2, Ver: 00F04000
I (3223698) stratum_task: rx: {"id":193,"error":null,"result":true}
I (3223698) asic_result: Ver: 20F04000 Nonce 86630214 diff 0.0 of 2048.
I (3223708) create_jobs_task: Queued 10: 1946060 (EN2: 6451)
I (3223708) stratum_task: message result accepted
I (3223718) bm1368Module: Job ID: 00, Core: 38/10, Ver: 065B4000
I (3223728) asic_result: Ver: 265B4000 Nonce 1E45024C diff 0.0 of 2048.
I (3223728) stratum_task: rx: {"id":194,"error":null,"result":true}
I (3223738) stratum_task: message result accepted
I (3223748) bm1368Module: Job ID: 18, Core: 11/11, Ver: 086B6000
I (3223758) asic_result: Ver: 286B6000 Nonce 45490116 diff 0.0 of 2048.
I (3223768) bm1368Module: Job ID: 10, Core: 16/11, Ver: 00D56000
I (3223768) stratum_task: rx: {"id":195,"error":null,"result":true}
I (3223768) asic_result: Ver: 20D56000 Nonce 25EC0120 diff 0.0 of 2048.
I (3223778) stratum_task: message result accepted
I (3223788) bm1368Module: Job ID: 28, Core: 50/9, Ver: 02D92000
I (3223798) asic_result: Ver: 22D92000 Nonce C01D0264 diff 0.0 of 2048.
I (3223798) stratum_task: rx: {"id":196,"error":null,"result":true}
I (3223808) stratum_task: message result accepted
I (3223808) bm1368Module: Job ID: 58, Core: 35/10, Ver: 01334000
I (3223818) stratum_task: rx: {"id":197,"error":null,"result":true}
I (3223818) asic_result: Ver: 21334000 Nonce B3400346 diff 0.0 of 2048.
I (3223828) stratum_task: message result accepted
I (3223848) bm1368Module: Job ID: 00, Core: 66/9, Ver: 07A12000
I (3223848) asic_result: Ver: 27A12000 Nonce 32560084 diff 0.0 of 2048.
I (3223848) stratum_task: rx: {"id":198,"error":null,"result":true}
I (3223858) stratum_task: message result accepted
I (3223858) bm1368Module: Job ID: 18, Core: 16/8, Ver: 01F50000
I (3223868) asic_result: Ver: 21F50000 Nonce 3EC70120 diff 0.0 of 2048.
I (3223878) stratum_task: rx: {"id":199,"error":null,"result":true}
I (3223888) stratum_task: message result accepted
I (3223888) bm1368Module: Job ID: 48, Core: 48/6, Ver: 0872C000
I (3223898) asic_result: Ver: 2872C000 Nonce 2B5F0160 diff 0.0 of 2048.
I (3223908) stratum_task: rx: {"id":200,"error":null,"result":true}
I (3223918) stratum_task: message result accepted
I (3223918) bm1368Module: Job ID: 78, Core: 64/10, Ver: 049D4000
I (3223928) asic_result: Ver: 249D4000 Nonce 38AC0280 diff 0.0 of 2048.
I (3223928) stratum_task: rx: {"id":201,"error":null,"result":true}
I (3223938) stratum_task: message result accepted
I (3223938) bm1368Module: Job ID: 58, Core: 33/6, Ver: 0216C000
I (3223948) asic_result: Ver: 2216C000 Nonce 03F40042 diff 0.0 of 2048.
I (3223958) stratum_task: rx: {"id":202,"error":null,"result":true}
I (3223968) stratum_task: message result accepted
I (3223968) bm1368Module: Job ID: 60, Core: 7/11, Ver: 004F6000
I (3223978) asic_result: Ver: 204F6000 Nonce 003D000E diff 0.0 of 2048.
I (3223988) stratum_task: rx: {"id":203,"error":null,"result":true}
I (3223988) stratum_task: message result accepted
I (3223998) bm1368Module: Job ID: 10, Core: 13/13, Ver: 05A9A000
I (3224008) asic_result: Ver: 25A9A000 Nonce BACC011A diff 0.0 of 2048.
I (3224008) stratum_task: rx: {"id":204,"error":null,"result":true}
I (3224018) stratum_task: message result accepted
I (3224018) bm1368Module: Job ID: 28, Core: 75/12, Ver: 000D8000
I (3224028) stratum_task: rx: {"id":205,"error":null,"result":true}
I (3224028) asic_result: Ver: 200D8000 Nonce 98100396 diff 0.0 of 2048.
I (3224048) stratum_task: message result accepted
I (3224058) bm1368Module: Job ID: 40, Core: 28/0, Ver: 013E0000
I (3224058) asic_result: Ver: 213E0000 Nonce 6B390338 diff 0.0 of 2048.
I (3224058) stratum_task: rx: {"id":206,"error":null,"result":true}
I (3224068) stratum_task: message result accepted
I (3224078) bm1368Module: Job ID: 70, Core: 15/3, Ver: 04686000
I (3224078) asic_result: Ver: 24686000 Nonce 2535001E diff 0.0 of 2048.
I (3224088) stratum_task: rx: {"id":207,"error":null,"result":true}
I (3224098) stratum_task: message result accepted
I (3224098) bm1368Module: Job ID: 70, Core: 17/12, Ver: 060B8000
I (3224108) asic_result: Ver: 260B8000 Nonce 90890022 diff 0.0 of 2048.
I (3224118) create_jobs_task: Queued 10: 1946060 (EN2: 6452)
I (3224118) bm1368Module: Send Job: 28
I (3224128) bm1368Module: Job ID: 38, Core: 53/7, Ver: 04DAE000
I (3224128) stratum_task: rx: {"id":208,"error":null,"result":true}
I (3224138) asic_result: Ver: 24DAE000 Nonce EA1D016A diff 0.0 of 2048.
I (3224148) stratum_task: message result accepted
I (3224158) bm1368Module: Job ID: 00, Core: 4/4, Ver: 05048000
I (3224158) asic_result: Ver: 25048000 Nonce 96900108 diff 0.0 of 2048.
I (3224168) stratum_task: rx: {"id":209,"error":null,"result":true}
I (3224178) stratum_task: message result accepted
I (3224178) bm1368Module: Job ID: 18, Core: 53/4, Ver: 060A8000
I (3224188) asic_result: Ver: 260A8000 Nonce 9C5D026A diff 0.0 of 2048.
I (3224198) bm1368Module: Job ID: 58, Core: 65/15, Ver: 0533E000
I (3224198) stratum_task: rx: {"id":210,"error":null,"result":true}
I (3224208) asic_result: Ver: 2533E000 Nonce EB720082 diff 0.0 of 2048.
I (3224218) stratum_task: message result accepted
I (3224218) bm1368Module: Job ID: 68, Core: 61/1, Ver: 06B42000
I (3224228) asic_result: Ver: 26B42000 Nonce C731027A diff 0.0 of 2048.
I (3224228) stratum_task: rx: {"id":211,"error":null,"result":true}
I (3224238) stratum_task: message result accepted
I (3224238) bm1368Module: Job ID: 30, Core: 13/7, Ver: 009AE000
I (3224248) asic_result: Ver: 209AE000 Nonce 24ED011A diff 0.0 of 2048.
I (3224268) stratum_task: rx: {"id":212,"error":null,"result":true}
I (3224268) stratum_task: message result accepted
I (3224268) bm1368Module: Job ID: 30, Core: 56/0, Ver: 080E0000
I (3224278) asic_result: Ver: 280E0000 Nonce F2320070 diff 0.0 of 2048.
I (3224278) stratum_task: rx: {"id":213,"error":null,"result":true}
I (3224288) stratum_task: message result accepted
I (3224298) bm1368Module: Job ID: 10, Core: 43/12, Ver: 077B8000
I (3224308) asic_result: Ver: 277B8000 Nonce BAE60256 diff 0.0 of 2048.
I (3224308) stratum_task: rx: {"id":214,"error":null,"result":true}
I (3224318) stratum_task: message result accepted
I (3224318) bm1368Module: Job ID: 28, Core: 52/1, Ver: 05D42000
I (3224328) asic_result: Ver: 25D42000 Nonce A1730168 diff 0.0 of 2048.
I (3224338) stratum_task: rx: {"id":215,"error":null,"result":true}
I (3224348) stratum_task: message result accepted
I (3224348) bm1368Module: Job ID: 70, Core: 55/5, Ver: 01DCA000
I (3224358) asic_result: Ver: 21DCA000 Nonce 9E89006E diff 0.0 of 2048.
I (3224378) bm1368Module: Job ID: 20, Core: 20/9, Ver: 01B52000
I (3224378) asic_result: Ver: 21B52000 Nonce 32DF0128 diff 0.0 of 2048.
I (3224388) bm1368Module: Job ID: 30, Core: 6/14, Ver: 0843C000
I (3224388) asic_result: Ver: 2843C000 Nonce 1602030C diff 0.0 of 2048.
I (3224398) bm1368Module: Job ID: 60, Core: 37/1, Ver: 02182000
I (3224398) asic_result: Ver: 22182000 Nonce 79CD004A diff 0.0 of 2048.
I (3224418) bm1368Module: Job ID: 40, Core: 8/13, Ver: 0513A000
I (3224418) asic_result: Ver: 2513A000 Nonce 3D4D0310 diff 0.0 of 2048.
I (3224428) bm1368Module: Job ID: 50, Core: 63/1, Ver: 05182000
I (3224428) asic_result: Ver: 25182000 Nonce DFF4027E diff 0.0 of 2048.
I (3224438) bm1368Module: Job ID: 00, Core: 8/2, Ver: 075E4000
I (3224448) asic_result: Ver: 275E4000 Nonce D71A0010 diff 0.0 of 2048.
I (3224458) bm1368Module: Job ID: 78, Core: 68/2, Ver: 04644000
I (3224458) asic_result: Ver: 24644000 Nonce D5C90288 diff 0.0 of 2048.
I (3224468) bm1368Module: Job ID: 58, Core: 23/14, Ver: 016BC000
I (3224468) asic_result: Ver: 216BC000 Nonce 52C7002E diff 0.0 of 2048.
I (3224488) bm1368Module: Job ID: 30, Core: 34/10, Ver: 04134000
I (3224488) asic_result: Ver: 24134000 Nonce B68A0144 diff 0.0 of 2048.
I (3224498) bm1368Module: Job ID: 60, Core: 63/13, Ver: 044DA000
I (3224498) asic_result: Ver: 244DA000 Nonce 8C68027E diff 0.0 of 2048.
I (3224508) bm1368Module: Job ID: 78, Core: 70/2, Ver: 01044000
I (3224518) asic_result: Ver: 21044000 Nonce 2661038C diff 0.0 of 2048.
I (3224528) bm1368Module: Job ID: 38, Core: 31/8, Ver: 05010000
I (3224528) asic_result: Ver: 25010000 Nonce 9310033E diff 0.0 of 2048.
I (3224538) bm1368Module: Job ID: 38, Core: 60/10, Ver: 05F94000
I (3224538) asic_result: Ver: 25F94000 Nonce AAB70178 diff 0.0 of 2048.
I (3224558) bm1368Module: Job ID: 10, Core: 45/1, Ver: 072C2000
I (3224558) asic_result: Ver: 272C2000 Nonce 150F015A diff 0.0 of 2048.
I (3224568) bm1368Module: Job ID: 28, Core: 45/0, Ver: 02320000
I (3224568) asic_result: Ver: 22320000 Nonce BFCC005A diff 0.0 of 2048.
I (3224578) bm1368Module: Job ID: 28, Core: 11/15, Ver: 06D1E000
I (3224588) asic_result: Ver: 26D1E000 Nonce E4290016 diff 0.0 of 2048.
I (3224598) bm1368Module: Job ID: 38, Core: 39/8, Ver: 06B30000
I (3224598) asic_result: Ver: 26B30000 Nonce B795014E diff 0.0 of 2048.
I (3224608) bm1368Module: Job ID: 38, Core: 43/11, Ver: 08516000
I (3224608) asic_result: Ver: 28516000 Nonce 0DCA0156 diff 0.0 of 2048.
I (3224628) bm1368Module: Send Job: 40
I (3224628) bm1368Module: Job ID: 00, Core: 14/11, Ver: 03B36000
I (3224628) asic_result: Ver: 23B36000 Nonce 6152001C diff 0.0 of 2048.
I (3224638) bm1368Module: Job ID: 78, Core: 21/5, Ver: 00C0A000
I (3224638) asic_result: Ver: 20C0A000 Nonce 624A032A diff 0.0 of 2048.
I (3224658) bm1368Module: Job ID: 50, Core: 10/1, Ver: 08902000
I (3224658) asic_result: Ver: 28902000 Nonce F9D20014 diff 0.0 of 2048.
I (3224668) bm1368Module: Job ID: 30, Core: 41/1, Ver: 033A2000
I (3224668) asic_result: Ver: 233A2000 Nonce BFF40052 diff 0.0 of 2048.
I (3224688) bm1368Module: Job ID: 40, Core: 49/7, Ver: 082EE000
I (3224688) asic_result: Ver: 282EE000 Nonce D51D0062 diff 0.0 of 2048.
I (3224698) bm1368Module: Job ID: 20, Core: 20/7, Ver: 081AE000
I (3224698) asic_result: Ver: 281AE000 Nonce FC1F0228 diff 0.0 of 2048.
I (3224708) bm1368Module: Job ID: 38, Core: 42/13, Ver: 0311A000
I (3224708) asic_result: Ver: 2311A000 Nonce 82100054 diff 0.0 of 2048.
I (3224718) create_jobs_task: Queued 10: 1946060 (EN2: 6453)
I (3224728) bm1368Module: Job ID: 78, Core: 28/6, Ver: 0154C000
I (3224728) asic_result: Ver: 2154C000 Nonce 5C660238 diff 0.0 of 2048.
I (3224748) bm1368Module: Job ID: 70, Core: 77/9, Ver: 077B2000
I (3224748) asic_result: Ver: 277B2000 Nonce 003F019A diff 0.0 of 2048.
I (3224758) bm1368Module: Job ID: 20, Core: 17/2, Ver: 03F24000
I (3224758) asic_result: Ver: 23F24000 Nonce 6F480222 diff 0.0 of 2048.
I (3224778) bm1368Module: Job ID: 38, Core: 0/9, Ver: 00CD2000
I (3224778) asic_result: Ver: 20CD2000 Nonce 147C0000 diff 0.0 of 2048.
I (3224788) bm1368Module: Job ID: 38, Core: 67/15, Ver: 0103E000
I (3224788) asic_result: Ver: 2103E000 Nonce 74110286 diff 0.0 of 2048.
I (3224798) bm1368Module: Job ID: 38, Core: 78/0, Ver: 025A0000
I (3224798) asic_result: Ver: 225A0000 Nonce 9B06009C diff 0.0 of 2048.
I (3224818) bm1368Module: Job ID: 38, Core: 42/10, Ver: 08734000
I (3224818) asic_result: Ver: 28734000 Nonce 6CFA0254 diff 0.0 of 2048.
I (3224828) bm1368Module: Job ID: 18, Core: 9/5, Ver: 06D6A000
I (3224828) asic_result: Ver: 26D6A000 Nonce 761E0212 diff 0.0 of 2048.
I (3224838) bm1368Module: Job ID: 48, Core: 24/10, Ver: 01094000
I (3224848) asic_result: Ver: 21094000 Nonce B4930030 diff 0.0 of 2048.
I (3224858) bm1368Module: Job ID: 78, Core: 23/2, Ver: 01864000
I (3224858) asic_result: Ver: 21864000 Nonce D5F3002E diff 0.0 of 2048.
I (3224868) bm1368Module: Job ID: 20, Core: 13/0, Ver: 05260000
I (3224868) asic_result: Ver: 25260000 Nonce DA3E001A diff 0.0 of 2048.
I (3224888) bm1368Module: Job ID: 38, Core: 65/13, Ver: 03C9A000
I (3224888) asic_result: Ver: 23C9A000 Nonce 59160182 diff 0.0 of 2048.
I (3224898) bm1368Module: Job ID: 50, Core: 39/2, Ver: 07C24000
I (3224898) asic_result: Ver: 27C24000 Nonce F698014E diff 0.0 of 2048.
I (3224908) bm1368Module: Job ID: 40, Core: 8/12, Ver: 01FB8000
I (3224918) asic_result: Ver: 21FB8000 Nonce 63760010 diff 0.0 of 2048.
I (3224928) bm1368Module: Job ID: 40, Core: 26/11, Ver: 05836000
I (3224928) asic_result: Ver: 25836000 Nonce 06290034 diff 0.0 of 2048.
I (3224938) bm1368Module: Job ID: 70, Core: 59/14, Ver: 003DC000
I (3224938) asic_result: Ver: 203DC000 Nonce FF410076 diff 0.0 of 2048.
I (3224958) bm1368Module: Job ID: 08, Core: 31/6, Ver: 087EC000
I (3224958) asic_result: Ver: 287EC000 Nonce A62F003E diff 0.0 of 2048.
I (3224968) bm1368Module: Job ID: 50, Core: 2/7, Ver: 07DAE000
I (3224968) asic_result: Ver: 27DAE000 Nonce 42310204 diff 0.0 of 2048.
I (3224978) bm1368Module: Job ID: 00, Core: 61/7, Ver: 064EE000
I (3224988) asic_result: Ver: 264EE000 Nonce CD52027A diff 0.0 of 2048.
I (3224998) bm1368Module: Job ID: 70, Core: 73/14, Ver: 01C7C000
I (3224998) asic_result: Ver: 21C7C000 Nonce FE5D0392 diff 0.0 of 2048.
I (3225008) bm1368Module: Job ID: 08, Core: 49/3, Ver: 03BE6000
I (3225008) asic_result: Ver: 23BE6000 Nonce 0EA60162 diff 0.0 of 2048.
I (3225028) bm1368Module: Job ID: 50, Core: 14/12, Ver: 081F8000
I (3225028) asic_result: Ver: 281F8000 Nonce 3079001C diff 0.0 of 2048.
I (3225038) bm1368Module: Job ID: 68, Core: 31/13, Ver: 008DA000
I (3225038) asic_result: Ver: 208DA000 Nonce 99F4023E diff 0.0 of 2048.
I (3225048) bm1368Module: Job ID: 18, Core: 21/12, Ver: 04818000
I (3225048) asic_result: Ver: 24818000 Nonce 8DFB022A diff 0.0 of 2048.
I (3225068) bm1368Module: Job ID: 30, Core: 33/4, Ver: 04408000
I (3225068) asic_result: Ver: 24408000 Nonce 28760242 diff 0.0 of 2048.
I (3225078) bm1368Module: Job ID: 58, Core: 51/13, Ver: 02F9A000
I (3225078) asic_result: Ver: 22F9A000 Nonce 1C390266 diff 0.0 of 2048.
I (3225098) bm1368Module: Job ID: 68, Core: 8/3, Ver: 00586000
I (3225098) asic_result: Ver: 20586000 Nonce EF820210 diff 0.0 of 2048.
I (3225108) bm1368Module: Job ID: 60, Core: 2/0, Ver: 041E0000
I (3225108) asic_result: Ver: 241E0000 Nonce 30480104 diff 0.0 of 2048.
I (3225118) bm1368Module: Job ID: 60, Core: 14/5, Ver: 0554A000
I (3225118) asic_result: Ver: 2554A000 Nonce 3D07001C diff 0.0 of 2048.
I (3225128) bm1368Module: Send Job: 58
I (3225138) bm1368Module: Job ID: 78, Core: 76/4, Ver: 06728000
I (3225138) asic_result: Ver: 26728000 Nonce 59630398 diff 0.0 of 2048.
I (3225158) bm1368Module: Job ID: 70, Core: 41/13, Ver: 02B3A000
I (3225158) asic_result: Ver: 22B3A000 Nonce D0130252 diff 0.0 of 2048.
I (3225168) bm1368Module: Job ID: 20, Core: 52/0, Ver: 04C40000
I (3225168) asic_result: Ver: 24C40000 Nonce A4920168 diff 0.0 of 2048.
I (3225178) bm1368Module: Job ID: 68, Core: 28/3, Ver: 049EE000
I (3225178) asic_result: Ver: 249EE000 Nonce EFE80038 diff 0.0 of 2048.
I (3225198) bm1368Module: Job ID: 18, Core: 65/10, Ver: 00D2C000
I (3225198) asic_result: Ver: 20D2C000 Nonce 80090382 diff 0.0 of 2048.
I (3225208) bm1368Module: Job ID: 30, Core: 30/5, Ver: 0556A000
I (3225208) asic_result: Ver: 2556A000 Nonce D5F0003C diff 0.0 of 2048.
I (3225218) create_jobs_task: Queued 10: 1946060 (EN2: 6454)
I (3225228) bm1368Module: Job ID: 28, Core: 68/11, Ver: 029F6000
I (3225228) asic_result: Ver: 229F6000 Nonce E19C0188 diff 0.0 of 2048.
I (3225248) bm1368Module: Job ID: 28, Core: 35/15, Ver: 055DE000
I (3225248) asic_result: Ver: 255DE000 Nonce EE5F0346 diff 0.0 of 2048.
I (3225258) bm1368Module: Job ID: 68, Core: 12/14, Ver: 03A9C000
I (3225258) asic_result: Ver: 23A9C000 Nonce 7D0E0118 diff 0.0 of 2048.
I (3225268) bm1368Module: Job ID: 00, Core: 61/6, Ver: 03B2C000
I (3225268) asic_result: Ver: 23B2C000 Nonce AF63027A diff 0.0 of 2048.
I (3225288) bm1368Module: Job ID: 40, Core: 23/10, Ver: 02BB4000
I (3225288) asic_result: Ver: 22BB4000 Nonce 98CA022E diff 0.0 of 2048.
I (3225298) bm1368Module: Job ID: 58, Core: 13/9, Ver: 06FD2000
I (3225298) asic_result: Ver: 26FD2000 Nonce 999A011A diff 0.0 of 2048.
I (3225308) bm1368Module: Job ID: 30, Core: 57/12, Ver: 06D98000
I (3225318) asic_result: Ver: 26D98000 Nonce 82F10272 diff 0.0 of 2048.
I (3225328) bm1368Module: Job ID: 28, Core: 15/6, Ver: 0134C000
I (3225328) asic_result: Ver: 2134C000 Nonce 6727001E diff 0.0 of 2048.
I (3225338) bm1368Module: Job ID: 58, Core: 4/6, Ver: 0218C000
I (3225338) asic_result: Ver: 2218C000 Nonce 57E70108 diff 0.0 of 2048.
I (3225358) bm1368Module: Job ID: 70, Core: 60/10, Ver: 02914000
I (3225358) asic_result: Ver: 22914000 Nonce A4030178 diff 0.0 of 2048.
I (3225368) bm1368Module: Job ID: 28, Core: 8/2, Ver: 025E4000
I (3225368) asic_result: Ver: 225E4000 Nonce 304A0310 diff 0.0 of 2048.
I (3225378) bm1368Module: Job ID: 70, Core: 39/8, Ver: 05EF0000
I (3225388) asic_result: Ver: 25EF0000 Nonce ECDB014E diff 0.0 of 2048.
I (3225398) bm1368Module: Job ID: 08, Core: 37/7, Ver: 0094E000
I (3225398) asic_result: Ver: 2094E000 Nonce D950004A diff 0.0 of 2048.
I (3225408) bm1368Module: Job ID: 20, Core: 68/15, Ver: 075DE000
I (3225408) asic_result: Ver: 275DE000 Nonce B93A0188 diff 0.0 of 2048.
I (3225428) bm1368Module: Job ID: 50, Core: 51/15, Ver: 036BE000
I (3225428) asic_result: Ver: 236BE000 Nonce 33710166 diff 0.0 of 2048.
I (3225438) bm1368Module: Job ID: 18, Core: 75/12, Ver: 031B8000
I (3225438) asic_result: Ver: 231B8000 Nonce E6270096 diff 0.0 of 2048.
I (3225448) bm1368Module: Job ID: 40, Core: 48/10, Ver: 049F4000
I (3225448) asic_result: Ver: 249F4000 Nonce 3A070160 diff 0.0 of 2048.
I (3225468) bm1368Module: Job ID: 58, Core: 54/14, Ver: 04CDC000
I (3225468) asic_result: Ver: 24CDC000 Nonce 3BA7006C diff 0.0 of 2048.
I (3225478) bm1368Module: Job ID: 50, Core: 68/0, Ver: 01040000
I (3225478) asic_result: Ver: 21040000 Nonce E0DC0088 diff 0.0 of 2048.
I (3225498) bm1368Module: Job ID: 00, Core: 61/10, Ver: 04C34000
I (3225498) asic_result: Ver: 24C34000 Nonce 6327017A diff 0.0 of 2048.
I (3225508) bm1368Module: Job ID: 48, Core: 58/6, Ver: 024CC000
I (3225508) asic_result: Ver: 224CC000 Nonce D7A40274 diff 0.0 of 2048.
I (3225518) bm1368Module: Job ID: 48, Core: 15/14, Ver: 0311C000
I (3225518) asic_result: Ver: 2311C000 Nonce 92D4021E diff 0.0 of 2048.
I (3225538) bm1368Module: Job ID: 78, Core: 56/11, Ver: 036B6000
I (3225538) asic_result: Ver: 236B6000 Nonce 459F0270 diff 0.0 of 2048.
I (3225548) bm1368Module: Job ID: 20, Core: 6/3, Ver: 011E6000
I (3225548) asic_result: Ver: 211E6000 Nonce F354010C diff 0.0 of 2048.
I (3225568) bm1368Module: Job ID: 38, Core: 35/2, Ver: 06D24000
I (3225568) asic_result: Ver: 26D24000 Nonce 127A0046 diff 0.0 of 2048.
I (3225578) bm1368Module: Job ID: 28, Core: 15/6, Ver: 022CC000
I (3225578) asic_result: Ver: 222CC000 Nonce 5ADC011E diff 0.0 of 2048.
I (3225588) bm1368Module: Job ID: 00, Core: 23/6, Ver: 04E6C000
I (3225588) asic_result: Ver: 24E6C000 Nonce 90D1002E diff 0.0 of 2048.
I (3225608) bm1368Module: Job ID: 48, Core: 68/10, Ver: 00D74000
I (3225608) asic_result: Ver: 20D74000 Nonce F9530288 diff 0.0 of 2048.
I (3225618) bm1368Module: Job ID: 78, Core: 44/15, Ver: 0817E000
I (3225618) asic_result: Ver: 2817E000 Nonce 34490358 diff 0.0 of 2048.
I (3225628) bm1368Module: Send Job: 70
I (3225638) bm1368Module: Job ID: 40, Core: 23/3, Ver: 04B06000
I (3225638) asic_result: Ver: 24B06000 Nonce 02C2022E diff 0.0 of 2048.
I (3225648) bm1368Module: Job ID: 70, Core: 6/7, Ver: 07DEE000
I (3225648) asic_result: Ver: 27DEE000 Nonce 5D50010C diff 0.0 of 2048.
I (3225668) bm1368Module: Job ID: 00, Core: 43/7, Ver: 00A6E000
I (3225668) asic_result: Ver: 20A6E000 Nonce 2C550156 diff 0.0 of 2048.
I (3225678) bm1368Module: Job ID: 30, Core: 3/7, Ver: 0164E000
I (3225678) asic_result: Ver: 2164E000 Nonce 14570206 diff 0.0 of 2048.
I (3225698) bm1368Module: Job ID: 30, Core: 54/0, Ver: 028C0000
I (3225698) asic_result: Ver: 228C0000 Nonce 01FE016C diff 0.0 of 2048.
I (3225708) bm1368Module: Job ID: 48, Core: 35/5, Ver: 042AA000
I (3225708) asic_result: Ver: 242AA000 Nonce A1250346 diff 0.0 of 2048.
I (3225718) create_jobs_task: Queued 10: 1946060 (EN2: 6455)
I (3225718) bm1368Module: Job ID: 60, Core: 55/9, Ver: 04432000
I (3225728) asic_result: Ver: 24432000 Nonce 1B63036E diff 0.0 of 2048.
I (3225738) bm1368Module: Job ID: 28, Core: 71/8, Ver: 06310000
I (3225738) asic_result: Ver: 26310000 Nonce FD25028E diff 0.0 of 2048.
I (3225758) bm1368Module: Job ID: 40, Core: 54/14, Ver: 0327C000
I (3225758) asic_result: Ver: 2327C000 Nonce 31D2006C diff 0.0 of 2048.
I (3225768) bm1368Module: Job ID: 68, Core: 69/6, Ver: 0184C000
I (3225768) asic_result: Ver: 2184C000 Nonce 1560028A diff 0.0 of 2048.
I (3225778) bm1368Module: Job ID: 00, Core: 24/12, Ver: 06338000
I (3225788) asic_result: Ver: 26338000 Nonce 48770030 diff 0.0 of 2048.
I (3225798) bm1368Module: Job ID: 48, Core: 12/4, Ver: 033E8000
I (3225798) asic_result: Ver: 233E8000 Nonce 24390218 diff 0.0 of 2048.
I (3225808) bm1368Module: Job ID: 78, Core: 62/4, Ver: 02AC8000
I (3225818) asic_result: Ver: 22AC8000 Nonce 4F0F007C diff 0.0 of 2048.
I (3225828) bm1368Module: Job ID: 70, Core: 27/7, Ver: 0664E000
I (3225828) asic_result: Ver: 2664E000 Nonce 1E400036 diff 0.0 of 2048.
I (3225838) bm1368Module: Job ID: 00, Core: 66/4, Ver: 03588000
I (3225838) asic_result: Ver: 23588000 Nonce 3FB00184 diff 0.0 of 2048.
I (3225848) bm1368Module: Job ID: 00, Core: 61/12, Ver: 03998000
I (3225858) asic_result: Ver: 23998000 Nonce 8CB9017A diff 0.0 of 2048.
I (3225868) bm1368Module: Job ID: 48, Core: 64/2, Ver: 008A4000
I (3225868) asic_result: Ver: 208A4000 Nonce 9DEC0080 diff 0.0 of 2048.
I (3225878) bm1368Module: Job ID: 60, Core: 60/5, Ver: 0436A000
I (3225878) asic_result: Ver: 2436A000 Nonce 38DB0178 diff 0.0 of 2048.
I (3225898) bm1368Module: Job ID: 58, Core: 41/10, Ver: 01A34000
I (3225898) asic_result: Ver: 21A34000 Nonce 72420152 diff 0.0 of 2048.
I (3225908) bm1368Module: Job ID: 58, Core: 12/6, Ver: 04B0C000
I (3225908) asic_result: Ver: 24B0C000 Nonce 74FC0118 diff 0.0 of 2048.
I (3225918) bm1368Module: Job ID: 70, Core: 36/11, Ver: 00AF6000
I (3225918) asic_result: Ver: 20AF6000 Nonce 3F9D0248 diff 0.0 of 2048.
I (3225938) bm1368Module: Job ID: 70, Core: 38/15, Ver: 079BE000
I (3225938) asic_result: Ver: 279BE000 Nonce 9DD7024C diff 0.0 of 2048.
I (3225948) bm1368Module: Job ID: 08, Core: 69/9, Ver: 03172000
I (3225948) asic_result: Ver: 23172000 Nonce 0803028A diff 0.0 of 2048.
I (3225968) bm1368Module: Job ID: 50, Core: 47/0, Ver: 02FC0000
I (3225968) asic_result: Ver: 22FC0000 Nonce A1D3005E diff 0.0 of 2048.
I (3225978) bm1368Module: Job ID: 48, Core: 54/3, Ver: 06BA6000
I (3225978) asic_result: Ver: 26BA6000 Nonce 922E016C diff 0.0 of 2048.
I (3225988) bm1368Module: Job ID: 78, Core: 0/7, Ver: 0034E000
I (3225988) asic_result: Ver: 2034E000 Nonce A7EE0000 diff 0.0 of 2048.
I (3226008) bm1368Module: Job ID: 68, Core: 57/3, Ver: 02D46000
I (3226008) asic_result: Ver: 22D46000 Nonce 16880072 diff 0.0 of 2048.
E (3226018) bm1368Module: Serial RX invalid 11
I (3226018) bm1368Module: 81 00 7d 1a 6d 9a aa 55 2e 02 01 <- we recover from serial misalignment now! good.
I (3226128) bm1368Module: Send Job: 08
I (3226218) create_jobs_task: Queued 10: 1946060 (EN2: 6456)
I (3226228) bm1368Module: Job ID: 08, Core: 71/7, Ver: 01AEE000
I (3226228) asic_result: Ver: 21AEE000 Nonce 1C68028E diff 309.8 of 2048.
I (3226628) bm1368Module: Send Job: 20
I (3226718) create_jobs_task: Queued 10: 1946060 (EN2: 6457)
I (3227118) bm1368Module: Job ID: 20, Core: 9/0, Ver: 088A0000
I (3227128) asic_result: Ver: 288A0000 Nonce 9F1D0312 diff 939.6 of 2048.
I (3227128) bm1368Module: Send Job: 38
I (3227218) create_jobs_task: Queued 10: 1946060 (EN2: 6458)
I (3227628) bm1368Module: Send Job: 50
I (3227718) create_jobs_task: Queued 10: 1946060 (EN2: 6459)
I (3228128) bm1368Module: Send Job: 68
I (3228218) create_jobs_task: Queued 10: 1946060 (EN2: 6460)
I (3228388) bm1368Module: Job ID: 68, Core: 67/9, Ver: 04712000
I (3228388) asic_result: Ver: 24712000 Nonce 0F700186 diff 259.4 of 2048.
I (3228628) bm1368Module: Send Job: 00
I (3228718) create_jobs_task: Queued 10: 1946060 (EN2: 6461)
I (3228718) bm1368Module: Job ID: 00, Core: 23/10, Ver: 01A34000
I (3228718) asic_result: Ver: 21A34000 Nonce D047012E diff 743.5 of 2048.

## Comments

### skot on 2024-08-13

full log for your enjoyment. from v2.1.9-11-g65586d0-dirty
[mining stops.txt](https://github.com/user-attachments/files/16603278/mining.stops.txt)
