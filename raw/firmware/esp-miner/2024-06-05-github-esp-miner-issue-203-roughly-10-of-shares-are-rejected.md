# bitaxeorg/ESP-Miner issue #203: roughly 10% of shares are rejected on public-pool

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/203
> Collected: 2026-10-07
> Published: 2024-06-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 203
- State: closed
- Author: skot
- Opened: 2024-06-05
- Closed: 2024-12-01
- Labels: bug

## Description

Now that we have rejected shares showing properly, it seems like public-pool is rejecting more bitaxe shares than is ideal.

## Comments

### ghost on 2024-06-05

Logs using 2.1.7 with public-pool.io Board Ver: 400  (think this is what you are looking for?) 
 
```
₿ (133052174) asic_result: Nonce difficulty 1233.39 of 4096.
₿ (133052804) bm1368Module: Job ID: E8
₿ (133052814) bm1368Module: RX Job ID: 70
₿ (133052814) asic_result: Nonce difficulty 2788.13 of 4096.
₿ (133053864) bm1368Module: Job ID: C5
₿ (133053864) bm1368Module: RX Job ID: 60
₿ (133053864) asic_result: Nonce difficulty 313.66 of 4096.
₿ (133054304) stratum_task: rx: {"id":null,"method":"mining.notify","params":["35e135","9e81c964520c42f237a10b2ad1141c5e38eaf83a0002224a0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170336eb0c5075626c69632d506f6f6c","ffffffff02191b3216000000001600141306387a39a499354aece772a39a092d92a646710000000000000000266a24aa21a9ed3fe01a2a8d08c92a0d50e3b728999c382d33bea270427f693754abd69b37357c00000000",["2df1376591e9b9cea71a7ec9b982c2f25ab8d392756cb2894bfbb3a029e2a98f","f21ef37e8d0cbfbf7ccb5acbc7a6cc8ed37beb2ee7f4fd9b9aeda71b951da0b3","e0eb0ecfc6b48c51c943504cdbe27ba56d8b430c7f87833e30b1f95b6aabc644","b17769948ea339a972679389d542c74d908e93217aa33a0115692d958aeabfa8","07cb0494881f1afa173ae816b4d24989ba6600bbf8d46d557a2da2123757469a","9e6b6b528eb1de6b09fc9ff5324168e7438dc0278e6822e90da7667826242298","4484104b018f350044e24fc55a19b0abb46e3c24736dca703384e4b9a01b01c9","ab875ed68d10ca96f0cfe9895b6ba1dca44568388e13b4c09c7c21d1f7407704","6911dd03aae7486bb889220ff5a5418499235debab87bbff8aacca97d0c67821","36352cc43eb32d2a881e67ab57d5bb4afce1647d09dcbc4ec6a194d9c2e392be","cc1cc9661f10f351cfc5bce2dd5214cbb674b61deb1a47e76a225528a491a894","0ecf8684b3068f1aebd07b1b009f6b8426fcf8a728a9f2640de07b131a3c9177","46fbc4f2f50b595bbe36bfec7d9c159b8948a604f1af9982e093b1a1b09efcb0"],"20000000","170355f0","66609adc",true]}
₿ (133054424) stratum_task: abandoning work
₿ (133054424) create_jobs_task: New Work Dequeued 35e135
₿ (133054714) stratum_task: rx: {"id":5011,"result":null,"error":[21,"Job not found",""]}
₿ (133054714) stratum_task: message result rejected
₿ (133054714) stratum_task: rx: {"id":5012,"result":null,"error":[21,"Job not found",""]}
₿ (133054724) stratum_task: message result rejected
₿ (133054734) stratum_task: rx: {"id":5013,"result":null,"error":[21,"Job not found",""]}
₿ (133054744) stratum_task: message result rejected
₿ (133054744) stratum_task: rx: {"id":null,"method":"mining.notify","params":["35e672","9e81c964520c42f237a10b2ad1141c5e38eaf83a0002224a0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170336eb0c5075626c69632d506f6f6c","ffffffff02191b3216000000001600141306387a39a499354aece772a39a092d92a646710000000000000000266a24aa21a9ed3fe01a2a8d08c92a0d50e3b728999c382d33bea270427f693754abd69b37357c00000000",["2df1376591e9b9cea71a7ec9b982c2f25ab8d392756cb2894bfbb3a029e2a98f","f21ef37e8d0cbfbf7ccb5acbc7a6cc8ed37beb2ee7f4fd9b9aeda71b951da0b3","e0eb0ecfc6b48c51c943504cdbe27ba56d8b430c7f87833e30b1f95b6aabc644","b17769948ea339a972679389d542c74d908e93217aa33a0115692d958aeabfa8","07cb0494881f1afa173ae816b4d24989ba6600bbf8d46d557a2da2123757469a","9e6b6b528eb1de6b09fc9ff5324168e7438dc0278e6822e90da7667826242298","4484104b018f350044e24fc55a19b0abb46e3c24736dca703384e4b9a01b01c9","ab875ed68d10ca96f0cfe9895b6ba1dca44568388e13b4c09c7c21d1f7407704","6911dd03aae7486bb889220ff5a5418499235debab87bbff8aacca97d0c67821","36352cc43eb32d2a881e67ab57d5bb4afce1647d09dcbc4ec6a194d9c2e392be","cc1cc9661f10f351cfc5bce2dd5214cbb674b61deb1a47e76a225528a491a894","0ecf8684b3068f1aebd07b1b009f6b8426fcf8a728a9f2640de07b131a3c9177","46fbc4f2f50b595bbe36bfec7d9c159b8948a604f1af9982e093b1a1b09efcb0"],"20000000","170355f0","66609b3f",false]}
₿ (133054864) stratum_task: rx: {"id":5014,"result":null,"error":[21,"Job not found",""]}
₿ (133054874) create_jobs_task: New Work Dequeued 35e672
₿ (133054874) stratum_task: message result rejected
₿ (133054884) stratum_task: rx: {"id":5015,"result":null,"error":[21,"Job not found",""]}
₿ (133054894) stratum_task: message result rejected
₿ (133054894) stratum_task: rx: {"id":5016,"result":null,"error":[21,"Job not found",""]}
₿ (133054904) stratum_task: message result rejected
₿ (133054914) stratum_task: rx: {"id":null,"method":"mining.notify","params":["35eba0","9e81c964520c42f237a10b2ad1141c5e38eaf83a0002224a0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170336eb0c5075626c69632d506f6f6c","ffffffff02191b3216000000001600141306387a39a499354aece772a39a092d92a646710000000000000000266a24aa21a9ed3fe01a2a8d08c92a0d50e3b728999c382d33bea270427f693754abd69b37357c00000000",["2df1376591e9b9cea71a7ec9b982c2f25ab8d392756cb2894bfbb3a029e2a98f","f21ef37e8d0cbfbf7ccb5acbc7a6cc8ed37beb2ee7f4fd9b9aeda71b951da0b3","e0eb0ecfc6b48c51c943504cdbe27ba56d8b430c7f87833e30b1f95b6aabc644","b17769948ea339a972679389d542c74d908e93217aa33a0115692d958aeabfa8","07cb0494881f1afa173ae816b4d24989ba6600bbf8d46d557a2da2123757469a","9e6b6b528eb1de6b09fc9ff5324168e7438dc0278e6822e90da7667826242298","4484104b018f350044e24fc55a19b0abb46e3c24736dca703384e4b9a01b01c9","ab875ed68d10ca96f0cfe9895b6ba1dca44568388e13b4c09c7c21d1f7407704","6911dd03aae7486bb889220ff5a5418499235debab87bbff8aacca97d0c67821","36352cc43eb32d2a881e67ab57d5bb4afce1647d09dcbc4ec6a194d9c2e392be","cc1cc9661f10f351cfc5bce2dd5214cbb674b61deb1a47e76a225528a491a894","0ecf8684b3068f1aebd07b1b009f6b8426fcf8a728a9f2640de07b131a3c9177","46fbc4f2f50b595bbe36bfec7d9c159b8948a604f1af9982e093b1a1b09efcb0"],"20000000","170355f0","66609b7b",false]}
```

### skot on 2024-06-05

Wow, this is not what I was expecting. @benjamin-wilson any thoughts about those (unsolicited?) "job not found" messages?

### benjamin-wilson on 2024-06-05

Stale jobs

### skot on 2024-06-05

> Stale jobs

I don't see any stratum tx with jobs being submitted is the strange thing..

### benjamin-wilson on 2024-06-05

Its possible this is a symptom of bandwidth restrictions on the server 

### skot on 2024-06-05

here is a stale share from my 401 log
```
I (65896) stratum_task: rx: {"id":null,"method":"mining.notify","params":["4128eb","6b91c7a7863952b8c411ed9ec589e6f9224b5d3b000072820000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170343eb0c5075626c69632d506f6f6c","ffffffff024ae9b114000000001600144e28940485d09e0d7d6cb94a1c7259c176e1710c0000000000000000266a24aa21a9ed0bb5411a720b1b7ad6b9f9dcae330b05aff60884c6cda8409fef38db8cfe116200000000",["89bda920ffe13e641e72008d3954f5e9dbba4aa040401627680bd2d882556f13","ecdab93a820299971d429857f9af643defc5e5d5a1487427793525404f636416","a18bf2019c89d1408643f0bbc8a8a66c8afc419bda038c923c44bc6f8ab8d19d","96bd9b5aa07de2a67231a8ff2b6b1fe2c3e4cc2688d11e6c2f480904bdb48aa6","34ccf6b8d401bfc45e56092accfc52e4dbd2f2f017d03ed8fbd2d390eb9816d4","27d5ee327710f5a7e8e3c370667147f2eab1d93b8f1ff50b7d39dc9e8a28a998","713b3554bcd1d2c65d0a63d6f96effd126afbd1091f49d69b61247daf800e3e3","758f3ff541e3c383362b95c6aebb6866d80d0238cb79d43c5b6dd0f788c93261","10579827b14bd2b596512884e69bba9612006c4eb29a96aa10d62679543e079a","cbb1e962dfeab4db85cef6a110791200ea5e025bdadd2eaf3c1e02f1dd8dc6d9","62ef8b3405b7699f7872bade5d62a3cd58ccca2c3297da2dee1d45a8eb700ce7","4f2909b6f9c8f105c314cabafc351c81c45431068dccabd6f92f8415374c0ab2"],"20000000","170355f0","6660d070",true]}
I (65976) bm1368Module: Job ID: 10
I (66006) bm1368Module: RX Job ID: 08
I (66006) asic_result: Nonce difficulty 377228.07 of 1000.
I (66016) stratum_api: tx: {"id": 15, "method": "mining.submit", "params": ["bc1qfc5fgpy96z0q6ltvh99pcujec9mwzugv3zcste.bitaxe", "411c73", "aa150000", "6660d03d", "dc013502", "00000000"]}

I (66006) stratum_task: abandoning work
I (66036) create_jobs_task: New Work Dequeued 4128eb
I (66306) stratum_task: rx: {"id":15,"result":null,"error":[21,"Job not found",""]}
E (66306) stratum_task: message result rejected
```

### benjamin-wilson on 2024-06-05

Why did it 
`I (66006) stratum_task: abandoning work`
Are there some logs missing?

### skot on 2024-06-05

> Why did it `I (66006) stratum_task: abandoning work` Are there some logs missing?

the first `mining.notify` is a clean_jobs=true

### benjamin-wilson on 2024-06-05

Oh, yep. Looks like it submitted old work 

### skot on 2024-06-05

Yes, mine submitted old work, you can see the `I (66016) stratum_api: tx:` messages. But I don't think @VictoriaKayak 's submitted any work..

### ghost on 2024-06-06

@skot ...another set of logs using the test address (bc1qfc5fgpy96z0q6ltvh99pcujec9mwzugv3zcste.test).   Same setup using 2.1.7 with public-pool.io Board Ver: 400.  Still about 10% rejected but I notice they come in "bursts" (none then a bunch at a time). 


(13439284) bm1368Module: RX Job ID: 10
₿ (13439284) asic_result: Nonce difficulty 501.44 of 4096.
₿ (13441304) bm1368Module: Job ID: 38
₿ (13441304) bm1368Module: RX Job ID: 18
₿ (13441304) asic_result: Nonce difficulty 5196.93 of 4096.
₿ (13441314) stratum_api: tx: {"id": 350, "method": "mining.submit", "params": ["bc1qfc5fgpy96z0q6ltvh99pcujec9mwzugv3zcste.test", "453761", "64ab0000", "6661060d", "ac9b187c", "00010000"]}
₿ (13441834) bm1368Module: Job ID: 26
₿ (13441834) bm1368Module: RX Job ID: 10
₿ (13441834) asic_result: Nonce difficulty 677.60 of 4096.
₿ (13442414) bm1368Module: Job ID: 0A
₿ (13442414) bm1368Module: RX Job ID: 00
₿ (13442414) asic_result: Nonce difficulty 914.99 of 4096.
₿ (13444274) bm1368Module: Job ID: EC
₿ (13444284) bm1368Module: RX Job ID: 70
₿ (13444284) asic_result: Nonce difficulty 279.65 of 4096.
₿ (13444514) bm1368Module: Job ID: 6A
₿ (13444514) bm1368Module: RX Job ID: 30
₿ (13444514) asic_result: Nonce difficulty 361.78 of 4096.
₿ (13446134) bm1368Module: Job ID: 93
₿ (13446134) bm1368Module: RX Job ID: 48
₿ (13446134) asic_result: Nonce difficulty 774.81 of 4096.
₿ (13446214) bm1368Module: Job ID: 4E
₿ (13446214) bm1368Module: RX Job ID: 20
₿ (13446214) asic_result: Nonce difficulty 490.31 of 4096.
₿ (13451274) bm1368Module: Job ID: 23
₿ (13451284) bm1368Module: RX Job ID: 10
₿ (13451284) asic_result: Nonce difficulty 836.20 of 4096.
₿ (13451944) bm1368Module: Job ID: BB
₿ (13451944) bm1368Module: RX Job ID: 58
₿ (13451944) asic_result: Nonce difficulty 364.30 of 4096.
₿ (13452744) bm1368Module: Job ID: B9
₿ (13452754) bm1368Module: RX Job ID: 58
₿ (13452754) asic_result: Nonce difficulty 63663.16 of 4096.
₿ (13452754) stratum_api: tx: {"id": 351, "method": "mining.submit", "params": ["bc1qfc5fgpy96z0q6ltvh99pcujec9mwzugv3zcste.test", "453761", "dcaf0000", "6661060d", "3e314080", "00012000"]}
₿ (13453214) bm1368Module: Job ID: 8B
₿ (13453214) bm1368Module: RX Job ID: 40
₿ (13453224) asic_result: Nonce difficulty 316.36 of 4096.
₿ (13453874) stratum_task: rx: {"id":null,"method":"mining.notify","params":["453ced","0f905d563ac60486afeb835cf8c40d46acdaaf1600032b910000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170358eb0c5075626c69632d506f6f6c","ffffffff029a9ab215000000001600144e28940485d09e0d7d6cb94a1c7259c176e1710c0000000000000000266a24aa21a9ed330c4457d7cc5a089843273490f191dfbbf3cd9ffcc5553030380d92c741fabb00000000",["2fdd3998d4a54d7687fcd5e30b510329c161c4ddd7939d00a3ba2b05ccbe8aed","cb649e687f4b8105516e78c59c607ca9d8906ad74d4b2d20868248a227c0c17b","ba4a4709aa9b8c3cb6d820396b57890e9915ca0ed87bedeb1f6a792b55b81116","9b265b88b2f95144f50112b248408a13525658ce217a59387119ef92adbf7bf9","7cd2bd7c4e03c3b1539d4854ac7c5ccb3d15a261193d9f5f32382b8208c704c5","64a2481d12351cc462c83fc9d7641ca770ea18b6b057513c83a57600eb66828b","1d410a409503b9c00ecf3bec4c4fc85eb04693777112cb2cf738083d89156873","06acdc6fa4c462d90ab2aec73d9869c0cbef9dae430aed94f7ac6b2d7e6b73d9","1e25724973a95a9fcca257013c1721bff3ef2ff5bef37046eb1499ddb2ad8e61","dac8ecb86f402058314eea0129a9309f058811eff7cd0829ee2a358e714e86a5","461b345c646af388d00dde2817f33638219951f4cf1981c464e7586a95e873cc","627d572b3a6e3892434048ce5955d2fd1d472c50898b5bbcf9566c74c840eb63","b659ccdcdafccfc817287f203a8a63ae118600bd9294b0387e46e1857c8c4cef"],"20000000","170355f0","6661062c",true]}
₿ (13453984) stratum_task: abandoning work
₿ (13453984) create_jobs_task: New Work Dequeued 453ced
₿ (13454284) stratum_task: rx: {"id":341,"result":null,"error":[21,"Job not found",""]}
₿ (13454284) stratum_task: message result rejected
₿ (13454294) stratum_task: rx: {"id":342,"result":null,"error":[21,"Job not found",""]}
₿ (13454304) stratum_task: message result rejected
₿ (13454304) stratum_task: rx: {"id":343,"result":null,"error":[21,"Job not found",""]}
₿ (13454314) stratum_task: message result rejected
₿ (13454314) stratum_task: rx: {"id":344,"result":null,"error":[21,"Job not found",""]}
₿ (13454324) stratum_task: message result rejected
₿ (13454334) stratum_task: rx: {"id":null,"method":"mining.notify","params":["45428b","0f905d563ac60486afeb835cf8c40d46acdaaf1600032b910000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170358eb0c5075626c69632d506f6f6c","ffffffff029a9ab215000000001600144e28940485d09e0d7d6cb94a1c7259c176e1710c0000000000000000266a24aa21a9ed330c4457d7cc5a089843273490f191dfbbf3cd9ffcc5553030380d92c741fabb00000000",["2fdd3998d4a54d7687fcd5e30b510329c161c4ddd7939d00a3ba2b05ccbe8aed","cb649e687f4b8105516e78c59c607ca9d8906ad74d4b2d20868248a227c0c17b","ba4a4709aa9b8c3cb6d820396b57890e9915ca0ed87bedeb1f6a792b55b81116","9b265b88b2f95144f50112b248408a13525658ce217a59387119ef92adbf7bf9","7cd2bd7c4e03c3b1539d4854ac7c5ccb3d15a261193d9f5f32382b8208c704c5","64a2481d12351cc462c83fc9d7641ca770ea18b6b057513c83a57600eb66828b","1d410a409503b9c00ecf3bec4c4fc85eb04693777112cb2cf738083d89156873","06acdc6fa4c462d90ab2aec73d9869c0cbef9dae430aed94f7ac6b2d7e6b73d9","1e25724973a95a9fcca257013c1721bff3ef2ff5bef37046eb1499ddb2ad8e61","dac8ecb86f402058314eea0129a9309f058811eff7cd0829ee2a358e714e86a5","461b345c646af388d00dde2817f33638219951f4cf1981c464e7586a95e873cc","627d572b3a6e3892434048ce5955d2fd1d472c50898b5bbcf9566c74c840eb63","b659ccdcdafccfc817287f203a8a63ae118600bd9294b0387e46e1857c8c4cef"],"20000000","170355f0","66610685",false]}
₿ (13454384) bm1368Module: Job ID: 79
₿ (13454454) bm1368Module: RX Job ID: 38
₿ (13454464) create_jobs_task: New Work Dequeued 45428b
₿ (13454464) asic_result: Nonce difficulty 283.23 of 4096.
₿ (13454454) stratum_task: rx: {"id":345,"result":null,"error":[21,"Job not found",""]}
₿ (13454484) stratum_task: message result rejected
₿ (13454694) stratum_task: rx: {"id":null,"method":"mining.notify","params":["45483b","0f905d563ac60486afeb835cf8c40d46acdaaf1600032b910000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff170358eb0c5075626c69632d506f6f6c","ffffffff029a9ab215000000001600144e28940485d09e0d7d6cb94a1c7259c176e1710c0000000000000000266a24aa21a9ed330c4457d7cc5a089843273490f191dfbbf3cd9ffcc5553030380d92c741fabb00000000",["2fdd3998d4a54d7687fcd5e30b510329c161c4ddd7939d00a3ba2b05ccbe8aed","cb649e687f4b8105516e78c59c607ca9d8906ad74d4b2d20868248a227c0c17b","ba4a4709aa9b8c3cb6d820396b57890e9915ca0ed87bedeb1f6a792b55b81116","9b265b88b2f95144f50112b248408a13525658ce217a59387119ef92adbf7bf9","7cd2bd7c4e03c3b1539d4854ac7c5ccb3d15a261193d9f5f32382b8208c704c5","64a2481d12351cc462c83fc9d7641ca770ea18b6b057513c83a57600eb66828b","1d410a409503b9c00ecf3bec4c4fc85eb04693777112cb2cf738083d89156873","06acdc6fa4c462d90ab2aec73d9869c0cbef9dae430aed94f7ac6b2d7e6b73d9","1e25724973a95a9fcca257013c1721bff3ef2ff5bef37046eb1499ddb2ad8e61","dac8ecb86f402058314eea0129a9309f058811eff7cd0829ee2a358e714e86a5","461b345c646af388d00dde2817f33638219951f4cf1981c464e7586a95e873cc","627d572b3a6e3892434048ce5955d2fd1d472c50898b5bbcf9566c74c840eb63","b659ccdcdafccfc817287f203a8a63ae118600bd9294b0387e46e1857c8c4cef"],"20000000","170355f0","666106c1",false]}
₿ (13739794) bm1368Module: Job ID: EC
₿ (13739804) bm1368Module: RX Job ID: 70
₿ (13739804) asic_result: Nonce difficulty 8072.42 of 4096.
₿ (13739804) stratum_api: tx: {"id": 365, "method": "mining.submit", "params": ["bc1qfc5fgpy96z0q6ltvh99pcujec9mwzugv3zcste.test", "457a4c", "b5060000", "666108dd", "69ee3e6c", "00018000"]}
₿ (13741934) bm1368Module: Job ID: D1
₿ (13741934) bm1368Module: RX Job ID: 68
₿ (13741934) asic_result: Nonce difficulty 719.68 of 4096.
₿ (13743234) bm1368Module: Job ID: 6D
₿ (13743234) bm1368Module: RX Job ID: 30
₿ (13743234) asic_result: Nonce difficulty 6805.31 of 4096.
₿ (13743244) stratum_api: tx: {"id": 366, "method": "mining.submit", "params": ["bc1qfc5fgpy96z0q6ltvh99pcujec9mwzugv3zcste.test", "457a4c", "0d080000", "666108dd", "7202188a", "0001a000"]}
₿ (13746894) bm1368Module: Job ID: 0D
₿ (13746904) bm1368Module: RX Job ID: 00
₿ (13746904) asic_result: Nonce difficulty 467.57 of 4096.
