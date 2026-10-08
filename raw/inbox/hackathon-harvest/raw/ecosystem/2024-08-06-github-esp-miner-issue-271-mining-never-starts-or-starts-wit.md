# bitaxeorg/ESP-Miner issue #271: Mining never starts, or starts with serial RX errors

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/271
> Collected: 2026-10-07
> Published: 2024-08-06

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 271
- State: closed
- Author: skot
- Opened: 2024-08-06
- Closed: 2024-08-10
- Labels: bug

## Description

Two seemingly related issues;
- Hashrate stays at 0 GH/s and the ASIC never returns any nonces
- Hashrate is above 0 but very low. Log shows lots of Serial RX errors

## Comments

### skot on 2024-08-06

It seems that sometimes it takes a while for mining to get started. Here is an example from a 401 running v2.1.9

mining should have started at 10540 when the first mining.notify happened. But it didn't start until 55280 after the second mining.notify happened.
```
I (10030) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe/BM1368 (v2.1.9)"]}
I (10040) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}
I (10050) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [1000]}
I (10060) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["bc1qqkredrrxc0pqjpcyp8ku3ry46e40tp40zrf0k0.bitaxe", "x"]}
I (10230) stratum_task: rx: {"id":1,"error":null,"result":[[["mining.notify","f55d67b1"]],"f55d67b1",4]}
I (10230) stratum_api: extranonce_str: f55d67b1
I (10240) stratum_api: extranonce_2_len: 4
I (10350) stratum_task: rx: {"id":2,"error":null,"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"}}
I (10360) stratum_api: Set version mask: 1fffe000
I (10360) stratum_task: Set version mask: 1fffe000
I (10370) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[1000]}
I (10380) stratum_task: Set stratum difficulty: 1000
I (10380) stratum_task: rx: {"id":4,"error":null,"result":true}
I (10390) stratum_task: setup message accepted
I (10540) stratum_task: rx: {"id":null,"method":"mining.notify","params":["acfcb8","039e010eb4aa9eac6baf08dc3172d5b3cddb2e56000189940000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703850e0d5075626c69632d506f6f6c","ffffffff02680a0d13000000001600140587968c66c3c209070409edc88c95d66af586af0000000000000000266a24aa21a9edd282288bdb14100769522f6792a8cc2090c35736c06314f84195d8fc23b0306900000000",["1337f7e87429be2e71d51f842cbc5497f196b415d9310e67555d06cd9029fc6e","897a5f8e3464449533f46c163445db290b6f4417598ee2fc854d63915c25a3dc","951ba50198bc6ed7af3b9a58e467c7bc6deb2490d9c1b98c4e1f275f283f7127","d9bfdf79264784079514703a78542ee207b02b8f24f5e29a2af5fd89c517328c","1d6b321c3cef68636aca58a36091c00fc59aadf777af9a6687d9d29ccf73d154","13fc7b82bc6871902b24a48145a4765147d8c34f4e4915969144e8237930f50a","661edc0665c08cbc3bc474ffc7000959ea4be0349bd6e2c1fea6484cf5352835","573872313c500193b34f9ec07aa734c30a27d8a3a5ede329c77a935287f02b49","3715d2b9b8f87cc7ef88dc5dfcdebf34f250dc0f951f18ad1bdef6e7d7f46a5a","bb2c1f0be5798076a12e2bfa08981bafd99a572dc4fc8602e8b72b597911a29f","9e24a6402c5af777adadf396454bdec2f8004e87abb5aa1ab1cc53ea8622f6e2","45b174ed61bd238a5a3f92300c4724957b1d2789adc76c4707ac85bbb8375bae"],"20000000","17031abe","66b27bb8",true]}
--> should start here: I (10640) SystemModule: Syncing clock
I (10640) create_jobs_task: New Work Dequeued acfcb8
I (54670) stratum_task: rx: {"id":null,"method":"mining.notify","params":["acfcce","039e010eb4aa9eac6baf08dc3172d5b3cddb2e56000189940000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703850e0d5075626c69632d506f6f6c","ffffffff02143b0f13000000001600140587968c66c3c209070409edc88c95d66af586af0000000000000000266a24aa21a9ed8c5ba80094f32426bdfb7a1038b900e83a25d1d2d0c95aa6176301fbd8b36ed700000000",["1337f7e87429be2e71d51f842cbc5497f196b415d9310e67555d06cd9029fc6e","897a5f8e3464449533f46c163445db290b6f4417598ee2fc854d63915c25a3dc","951ba50198bc6ed7af3b9a58e467c7bc6deb2490d9c1b98c4e1f275f283f7127","d9bfdf79264784079514703a78542ee207b02b8f24f5e29a2af5fd89c517328c","9617ce5afe571ef1efbb57559305abd944614b5420b8517f4fbd9c845475d948","cca8204ef859e3482063b0c0bd3b211f4205bfaca361116528c6b552c02cd9b9","08da108a75e062a14093915141b655d5a163006bfc8d10b57b7d3b802d04fb7f","bd59e5f5b782b245c1c5593ec0231145faa90e01f3c9e4ae7425e75237e570b2","29fefa80e9f441f0507eab3b9d093506c38addd999ff5743f69f4d6a35c21898","e31733516bb40c8680bbc5dfd1378a11348af4bcb09124294f9c323a44f8350e","b7d2fd5c8f71f07284905c02a8ec689a794ca4aef8860269be54c284cfd5aeac","42997b9c747c1ed9f5f31faeccbadf7cbaf0b927b37ad9551649d57583793531"],"20000000","17031abe","66b27bf4",false]}
I (54770) create_jobs_task: New Work Dequeued acfcce
I (54780) ASIC_task: New pool difficulty 1000
I (55280) bm1368Module: Job ID: 48, Core: 28/11, Ver: 00056000
--> actually started here: I (55280) asic_result: Ver: 20056000 Nonce 22060038 diff 356.3 of 1000.
```

### skot on 2024-08-06

it looks like we aren't sending any work to the ASIC until the second mining.notify? here is the log with ASIC serial comms printed;

```
I (9799) stratum_task: Connecting to: stratum+tcp://public-pool.io:21496 (68.235.52.36)
I (9799) stratum_task: Socket created, connecting to 68.235.52.36:21496
I (9809) ASIC_task: ASIC Job Interval: 500.00 ms
I (9809) ASIC_task: ASIC Ready!
I (9819) main_task: Returned from app_main()
I (10079) stratum_api: Resetting stratum uid
I (10079) stratum_task: Clean Jobs: clearing queue
I (10079) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe/BM1368 (v2.1.9-dirty)"]}
I (10089) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}
I (10099) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [1000]}
I (10109) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["bc1qqkredrrxc0pqjpcyp8ku3ry46e40tp40zrf0k0.bitaxe", "x"]}
I (10289) stratum_task: rx: {"id":1,"error":null,"result":[[["mining.notify","63add300"]],"63add300",4]}
I (10289) stratum_api: extranonce_str: 63add300
I (10289) stratum_api: extranonce_2_len: 4
I (10489) stratum_task: rx: {"id":2,"error":null,"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"}}
I (10489) stratum_api: Set version mask: 1fffe000
I (10489) stratum_task: Set version mask: 1fffe000
I (10499) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[1000]}
I (10509) stratum_task: Set stratum difficulty: 1000
I (10509) stratum_task: rx: {"id":4,"error":null,"result":true}
I (10519) stratum_task: setup message accepted
I (10529) stratum_task: rx: {"id":null,"method":"mining.notify","params":["c08ec8","6e7c486ad616f3d3a3bcfb3c4bab533cd65d7cac0001cf7f0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703900e0d5075626c69632d506f6f6c","ffffffff02c5bd3b13000000001600140587968c66c3c209070409edc88c95d66af586af0000000000000000266a24aa21a9ed29525f0239e7663d32eeca1ad6d9593ea896cc23394fffc61f8f1e4e1f789fa100000000",["1536e598386753672dd90eb2b63d953a4da59a396387669f69488c359cbd9ded","6595163d204e7417888913eef0156650f424a60d59678e9e1c653c99081f93d9","a7179204f2df5b679613410271e9e84fae800d3a6e200919610724021d2b7460","8a991e96d7835fd50e6f60bcfb7c0e369a900d5892137110d6843bbf2294dd06","ec6fa64658d4d889b2215b24854ae81f5064dc268ea803010bc20cfd3f127a2e","6b2921789bccf1f0760d97c50af655f15f5bf11f74b75629eed4006ecf8d39ab","e6ccc9f351774d16486b3a90aad3b074193d7b1cc33dc0361f13e461825a93f1","7a9171a31d143e5ed519cbf24f93f2b395bbbe9c19ae5baf106cbbe8adef3608","182c77b31a375ed2932d6b7b8a37ce9be41a0caa1f4a2a358601413d040ed0fa","82755dcf1872d7a75384fc7b62487762784a13a14daa2dcbaf7115fe47d5091a","fe90474fd0392135f871220d8b2aa6a55e5ecfe81a11de87a1f96ef023a1ca09","0a70404f6e4c4882e47952b5d838927602ad4380e5fc34bcd4386af9a4c5ca8c"],"20000000","17031abe","66b29996",true]}
I (10639) SystemModule: Syncing clock
I (10639) create_jobs_task: New Work Dequeued c08ec8
I (40079) stratum_task: rx: {"id":null,"method":"mining.notify","params":["c08ed2","6e7c486ad616f3d3a3bcfb3c4bab533cd65d7cac0001cf7f0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703900e0d5075626c69632d506f6f6c","ffffffff0220813e13000000001600140587968c66c3c209070409edc88c95d66af586af0000000000000000266a24aa21a9ed67cd52f858da4a173d659b6e17c18ea5d948741b357111a64a33f509d8f410c700000000",["1536e598386753672dd90eb2b63d953a4da59a396387669f69488c359cbd9ded","ccfcafe5fbb744c196f0ef53dd770470dc07e4500428cd2bac478c4b95471ab8","846b642d9b2da00369e9591f928a5f4942db03035df93653d30e7092d5deb243","5b89db9f79d397f08678b5ad505ace68d8547deecc497ec5c377d975b49e5e12","992340b0a7d2c7238d4c562958897cdd0238fa6ed7c128ceb27ddf23c6f67d6c","afdc3cd53bb35243ba4dd5a23e2eb88f091081d4ab39e94b2b6fef278f67d86f","ef3eb77fb61ed7e5df5f2dd338d2fc2cf6671d33e2fda1905cab64bcbd0334aa","f70bf01bfacf74b1b249d999178441a4ada17e0f9f119fb82e585ff676c4b4c1","38d2ffdc14aa36e6c689384a714c39326cedc5b04b803855a2a4700416a51427","f8d654d07d3dd82d306909da8669cf62f05090db8df99dec23be0ff82dd538ae","0edc293913779ba371346711b275de6024743606e90d35a63794de2ae465f49d","88855b8871bf4dcb4e6bbf7d38b6868d3639bae91c0b848ec3a059c1c85257be"],"20000000","17031abe","66b299d2",false]}
I (40179) create_jobs_task: New Work Dequeued c08ed2
I (40189) ASIC_task: New pool difficulty 1000
tx: [55 AA 21 56 18 01 00 00 00 00 BE 1A 03 17 D2 99 B2 66 36 E2 5E CF 14 3F 5D 48 A7 CC 4A AF F8 90 3A 78 19 7A 7C 95 A6 9C 67 7E E9 66 98 92 CF AA 18 5B 00 00 00 00 00 00 00 00 7F CF 01 00 AC 7C 5D D6 3C 53 AB 4B 3C FB BC A3 D3 F3 16 D6 6A 48 7C 6E 00 00 00 20 66 57]

tx: [55 AA 21 56 30 01 00 00 00 00 BE 1A 03 17 D2 99 B2 66 21 4D 77 F3 D4 F6 A9 0E E0 3C 9F 79 63 8E 4C 2E 3D 59 0B 80 E6 69 46 67 29 13 49 C3 E1 0F 12 E0 00 00 00 00 00 00 00 00 7F CF 01 00 AC 7C 5D D6 3C 53 AB 4B 3C FB BC A3 D3 F3 16 D6 6A 48 7C 6E 00 00 00 20 5E 86]

tx: [55 AA 21 56 48 01 00 00 00 00 BE 1A 03 17 D2 99 B2 66 E8 14 9D 18 EA 48 AE DC 31 0D 46 A8 57 FD 99 B0 16 03 55 0E 7B 7B 3B 07 DA 59 40 3F D3 8A 95 AB 00 00 00 00 00 00 00 00 7F CF 01 00 AC 7C 5D D6 3C 53 AB 4B 3C FB BC A3 D3 F3 16 D6 6A 48 7C 6E 00 00 00 20 24 C3]

tx: [55 AA 21 56 60 01 00 00 00 00 BE 1A 03 17 D2 99 B2 66 10 B0 34 8F 0D 40 67 5E 01 46 94 10 9D C6 4F CA 94 48 49 25 4D E2 A6 4D 67 2E 81 B9 DF 91 A1 3F 00 00 00 00 00 00 00 00 7F CF 01 00 AC 7C 5D D6 3C 53 AB 4B 3C FB BC A3 D3 F3 16 D6 6A 48 7C 6E 00 00 00 20 37 9E]

tx: [55 AA 21 56 78 01 00 00 00 00 BE 1A 03 17 D2 99 B2 66 9A C5 31 A9 FC E7 C9 9B 24 8B EE 40 B7 E3 ED 4B FA 8F 3C DD F6 CC 52 2F B4 5D 45 F0 60 9E 29 FA 00 00 00 00 00 00 00 00 7F CF 01 00 AC 7C 5D D6 3C 53 AB 4B 3C FB BC A3 D3 F3 16 D6 6A 48 7C 6E 00 00 00 20 C4 E1]

rx: [AA 55 66 00 CB 32 02 F9 23 39 91]

I (42029) bm1368Module: Job ID: 78, Core: 51/9, Ver: 04672000
I (42029) asic_result: Ver: 24672000 Nonce 32CB0066 diff 514.8 of 1000.
```

### skot on 2024-08-07

this seems very related to #268 

### skot on 2024-08-10

closing as duplicate of #268
