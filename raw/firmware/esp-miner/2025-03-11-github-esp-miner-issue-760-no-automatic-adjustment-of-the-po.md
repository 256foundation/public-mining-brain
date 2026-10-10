# bitaxeorg/ESP-Miner issue #760: No automatic adjustment of the pool difficulty

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/760
> Collected: 2026-10-07
> Published: 2025-03-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 760
- State: closed
- Author: matlen67
- Opened: 2025-03-11
- Closed: 2025-03-12
- Labels: none

## Description

With my Bitaxe Gamma I noticed that with version 2.6.0b8 the difficulty of 10000 is still set after 10 minutes and therefore hardly any or no shares are transferred to the pool. In V2.5.1, the difficulty is adjusted after 5 minutes at the latest. 

Pool: eusolo.ckpool.org
v2.6.0b8
![Image](https://github.com/user-attachments/assets/dfb1fd2d-4b0b-4e81-82ff-f44a014970db)

![Image](https://github.com/user-attachments/assets/8b986638-e4c3-42d5-aa76-efd04b75cebf)

v2.5.1
![Image](https://github.com/user-attachments/assets/19cf6188-c867-49d3-95b5-358acdb10344)

![Image](https://github.com/user-attachments/assets/26e3a6b7-4cb1-4259-bd94-bab907921d94)

## Comments

### skot on 2025-03-11

That stratum message called mining.set_difficulty comes from the pool. The bitaxe will adjust the difficulty to whatever the pool says.

Can you see anywhere in the logs where that command was sent and the Bitaxe didn't follow it?

### matlen67 on 2025-03-11

I make a putty log and find this on timestamp 289784


I (282664) asic_result: Ver: 23C08000 Nonce 9B9D045A diff 880.5 of 10000.
I (284904) bm1370Module: Job ID: 38, Core: 86/6, Ver: 00B0C000
I (284904) asic_result: Ver: 20B0C000 Nonce 57DC02AC diff 995.4 of 10000.
I (285344) primary_pool: rx: {"params":["679d5e020001c6f9","849ed206389cd524a8173614269cc3e639365c630000f13c0000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3503218a0d0004113bd06704b91d31120c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff03325f551200000000160014cf3815a968c8d3cd9e58facfdb7f85c3762159db79c85f000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9ed829d4c40d57260237c403ca4045aa6c2f1bd207d3765c6bed33797a61b7560e600000000",["8690767f6c7d304ab3d4ef01f991f132943fa878a3e17ae64fe2a72ca2680eab","9a052d9f2488a49120928c5b8ef5e0737d5b1777131066b03b4902ef92c62277","1fa7d68317461049f051c67809197a2b1210fcddb90dd1f5318c61577429c86f","41f0b8ad58e29dd4e07918a0482e251573e6827b27e2241ad829f3babe26b243","acc97cc3aad9e4b343247728d9f79d415eea1495f12ac7cf33299b222310704d","e9f535d64053f873373dfe903166fbaef36c2d68120b3f278b17a032f9c07528","520451a633c18028b207bf67d772e4c398b5751dc62363e103ab8569a96f3526","c453e521a04ccd461da30508488445f43aab086ea2f184d70fe56599c9ded681","714c7df9eeaed1a33a6fdbddb2a95c44e1f08a6061044e498f0e839d903f9dd8","39425129dae516db06d1c4d2dd93269d54c389e48523dcbb5a2ec1d203a58435","84ba18d62e52437e6664ed7483c02c6e440fb41e1ddaf1cc2ffea6ec5dc60757"],"20000000","17028281","67d03b11",false],"id":null,"method":"mining.notify"}
I (285344) bm1370Module: Job ID: 38, Core: 16/0, Ver: 06080000
I (285454) asic_result: Ver: 26080000 Nonce C14A0220 diff 277.9 of 10000.
I (285464) create_jobs_task: New Work Dequeued 679d5e020001c6f9
I (285994) bm1370Module: Job ID: 68, Core: 126/6, Ver: 01BCC000
I (285994) asic_result: Ver: 21BCC000 Nonce E0D703FC diff 3403.8 of 10000.
I (286554) secondary_pool: rx: {"params":["67444bb00004e683","849ed206389cd524a8173614269cc3e639365c630000f13c0000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3503218a0d0004123bd067046255810a0c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff034d7e551200000000160014cf3815a968c8d3cd9e58facfdb7f85c3762159db1bc95f000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9edb92134a90f5b99acdba4f57465f095234485888bf78af98286a9425b9f864a0100000000",["8690767f6c7d304ab3d4ef01f991f132943fa878a3e17ae64fe2a72ca2680eab","e4965f8623f9ed2a7dd93dacb0e5bd38709a6c591e540e7184d7d3ea192abe71","44b160f943f3b0476a2de7994fb665bfd65f235b60e763b7617c8a664d04c6d9","3a13d27b914676949dcca517750edafd4189adb9b1fd8d0fe18ae7bc47cef46f","da446902065a100551741677940cc91f80d2f284bb210fbc15d19b73afafe33c","c8478080f2b67cb19b07e1273335eedf558a8ad1ed3e8330018bdf8a6c1adff7","ec947b2be2987d436c793f27889a3b8a55b9d3f13b66200e6ed1ecde76de70a2","1f7d7fb0dc57337b91d640b4743e59760eabb0d929103a3ffac79171ca582b12","3a2dc9d9791751133eebe1790aa4487447eec76cea9a1aaef4536ab8407ad013","21b7df52eb4dfccf0c8978ebde1b60a6ff0480e65e6f7cbed674859f10574c5b","e1b4f248e44b71b2d665ecb708eb4bf2e29e238c8c43475357a6a8de1e855b88"],"20000000","17028281","67d03b12",false],"id":null,"method":"mining.notify"}
I (288884) bm1370Module: Job ID: 78, Core: 52/11, Ver: 00636000
I (288884) asic_result: Ver: 20636000 Nonce AEEF0368 diff 353.0 of 10000.
I (289404) bm1370Module: Job ID: 10, Core: 63/5, Ver: 00AAA000
I (289404) asic_result: Ver: 20AAA000 Nonce 0296027E diff 9696.9 of 10000.
I (289744) bm1370Module: Job ID: 10, Core: 43/6, Ver: 04C2C000
I (289744) asic_result: Ver: 24C2C000 Nonce F4E20456 diff 10763.9 of 10000.
I (289744) stratum_api: tx: {"id": 14, "method": "mining.submit", "params": ["bc1qeuupt2tgerfum8jclt8aklu9cdmzzkwml9lg7c.matlen67_3", "679d5e020001c6f8", "3a00000000d7ce3f", "67d03af3", "f4e20456", "04c2c000"]}
I (289784) primary_pool: rx: {"params":[1144],"id":null,"method":"mining.set_difficulty"}
I (289784) primary_pool: Set stratum difficulty: 1144
I (289784) primary_pool: rx: {"result":true,"error":null,"id":14}
I (289794) primary_pool: message result accepted
I (289854) ASIC_task: New pool difficulty 10000
I (298884) bm1370Module: Job ID: 58, Core: 99/2, Ver: 005E4000
I (298884) asic_result: Ver: 205E4000 Nonce 676C03C6 diff 569.8 of 10000.
I (299424) bm1370Module: Job ID: 70, Core: 35/5, Ver: 00D8A000
I (299424) asic_result: Ver: 20D8A000 Nonce D2D20246 diff 6574.4 of 10000.

### mutatrum on 2025-03-11

This is a bug in #717 which has been reverted after 2.6.0b8. We need to release a new beta.

### mutatrum on 2025-03-12

Can you try with [v2.6.0b9](https://github.com/skot/ESP-Miner/releases/tag/v2.6.0b9)?

### matlen67 on 2025-03-12

Just tested, works again with v2.6.0b9

₿ (14444) stratum_task: rx: {"params":[1000],"id":null,"method":"mining.set_difficulty"}
₿ (14454) stratum_task: Set stratum difficulty: 1000
...
...
...
₿ (42454) ASIC_task: New pool difficulty 1000
₿ (42484) bm1370Module: Job ID: 58, Core: 21/14, Ver: 0061C000
₿ (42484) asic_result: Ver: 2061C000 Nonce 7538002A diff 876.5 of 1000.

### mutatrum on 2025-03-12

Thank you, closing this as fixed.
