# bitaxeorg/ESP-Miner issue #1587: esp-miner is unable to handle difficulty change following with "mining.notify" when `cleanJob` set to false

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1587
> Collected: 2026-10-07
> Published: 2026-03-02

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1587
- State: closed
- Author: blackmennewstyle
- Opened: 2026-03-02
- Closed: 2026-06-02
- Labels: bug, accepted

## Description

Hello beautiful dev(s),

Why is `esp-miner` unable to handle properly the following scenario:

- The stratum sends a `mining.set_difficulty` following with `mining.notify`  with the`cleanJob` indicator set to `false`.

`esp-miner` then starts to send duplicate shares, the same solution with the same `nonce`, over and over again until the stratum sends another `mining.notify` with the `cleanJob` indicator set to `true`.

The behavior is clearly visible in my attachment file.

It is way more easy to reproduce that behavior on BTC `testnet4` by the way.
```
2026-03-02 16:52:49.4134] [I] [btc1] [0HNJOFCT4H9CS] VarDiff update to 9427.961
[2026-03-02 16:52:49.4134] [D] [btc1] [0HNJOFCT4H9CS] Sending: {"jsonrpc":"2.0","method":"mining.set_difficulty","params":[9427.960695338843],"id":null} 
[2026-03-02 16:52:49.4134] [D] [btc1] [0HNJOFCT4H9CS] Sending: {"jsonrpc":"2.0","method":"mining.notify","params":["00000006","61579a01acc1daa4da7e43b1a67de71112b9133d44fc8e2d0784e99700000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff32033ee60104febfa56900","1f4d696e696e67636f72652f436564726963204352495350494e2f61735f544800000000020000000000000000266a24aa21a9ede4c58cf54dd9bf607f7c904968305679ab9226e3e338418e24a7245d3e8554a89a33312a010000001976a914b39a791bdaa16ec039fbabe4e46efb7cab150c5388ac00000000",["2aeff42e83cf2fa7a271c9e600923458e5b44d3cc086b68fd5e1bd2f8fb2c2f4","8d88f91b9c3d3748e2e5c3b324db6825c4e9fd5051c5617de6a271da2b4b8b87","7ab6d88c0da99231f817a1a588ccf941ded398e24ec1510745dd23459444770c","bd52c7bdc423945a8a9bafaa0738c7a0edd32792506743acd39c9593cf964d43","c076078e0fc41fbc4ef1e8ed3368516bde09b8d98cf13246a1f63bd25c902099","0467ec38d4df01dc161f2aec3ef865832d8d1689067bb155d5aa359b0433de55"],"20000000","190336be","69a5c579",false],"id":null}
[2026-03-02 16:53:19.4715] [D] [btc1] [0HNJOFCT4H9CS] [NET] Received data: {"id":21,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.janus","00000006","3b000000","69a5c579","ad910248","02cc2000"]}
[2026-03-02 16:53:19.4715] [D] [btc1] [0HNJOFCT4H9CS] [PIPE] Received data: {"id":21,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.janus","00000006","3b000000","69a5c579","ad910248","02cc2000"]}
[2026-03-02 16:53:19.4715] [D] [btc1] [0HNJOFCT4H9CS] Dispatching request 'mining.submit' [21] 
[2026-03-02 16:53:19.4715] [I] [btc1] [0HNJOFCT4H9CS] Share rejected: duplicate share [bitaxe/BM1370/v2.13.0] 
[2026-03-02 16:53:19.4725] [D] [btc1] [0HNJOFCT4H9CS] Sending: {"result":false,"error":{"code":22,"message":"duplicate share","data":null},"id":21} 
[2026-03-02 16:53:58.8370] [D] [btc1] [0HNJOFCT4H9CS] [NET] Received data: {"id":22,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.janus","00000006","89000000","69a5c579","debe0186","0555e000"]}
[2026-03-02 16:53:58.8370] [D] [btc1] [0HNJOFCT4H9CS] [PIPE] Received data: {"id":22,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.janus","00000006","89000000","69a5c579","debe0186","0555e000"]}
[2026-03-02 16:53:58.8370] [D] [btc1] [0HNJOFCT4H9CS] Dispatching request 'mining.submit' [22] 
[2026-03-02 16:53:58.8370] [I] [btc1] [0HNJOFCT4H9CS] Share rejected: duplicate share [bitaxe/BM1370/v2.13.0] 
[2026-03-02 16:53:58.8370] [D] [btc1] [0HNJOFCT4H9CS] Sending: {"result":false,"error":{"code":22,"message":"duplicate share","data":null},"id":22} 
[2026-03-02 16:54:04.4307] [D] [btc1] [0HNJOFCT4H9CS] [NET] Received data: {"id":23,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.janus","00000006","95000000","69a5c579","5d110336","00218000"]}
[2026-03-02 16:54:04.4307] [D] [btc1] [0HNJOFCT4H9CS] [PIPE] Received data: {"id":23,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.janus","00000006","95000000","69a5c579","5d110336","00218000"]}
[2026-03-02 16:54:04.4307] [D] [btc1] [0HNJOFCT4H9CS] Dispatching request 'mining.submit' [23] 
[2026-03-02 16:54:04.4307] [I] [btc1] [0HNJOFCT4H9CS] Share rejected: duplicate share [bitaxe/BM1370/v2.13.0]
[2026-03-02 16:54:04.4307] [D] [btc1] [0HNJOFCT4H9CS] Sending: {"result":false,"error":{"code":22,"message":"duplicate share","data":null},"id":23}
[2026-03-02 16:54:28.8262] [D] [btc1] [0HNJOFCT4H9CS] [PIPE] Received data: {"id":24,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.janus","00000006","c5000000","69a5c579","0f870304","03c8e000"]}
[2026-03-02 16:54:28.8262] [D] [btc1] [0HNJOFCT4H9CS] Dispatching request 'mining.submit' [24] 
[2026-03-02 16:54:28.8262] [I] [btc1] [0HNJOFCT4H9CS] Share rejected: duplicate share [bitaxe/BM1370/v2.13.0] 
[2026-03-02 16:54:28.8262] [D] [btc1] [0HNJOFCT4H9CS] Sending: {"result":false,"error":{"code":22,"message":"duplicate share","data":null},"id":24} 
[2026-03-02 16:54:37.1131] [I] [btc1] Detected new transaction(s) for block 124479 [ZMQ] 
[2026-03-02 16:54:37.1131] [I] [btc1] Broadcasting job 00000007 
[2026-03-02 16:54:37.1131] [D] [btc1] [0HNJOFCT4H9CS] Sending: {"jsonrpc":"2.0","method":"mining.notify","params":["00000007","e1341f7cd8871844a42e8081a93a9ca2ee4207f8278e6e850b69744100000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff32033fe60104cdc0a56900","1f4d696e696e67636f72652f436564726963204352495350494e2f61735f544800000000020000000000000000266a24aa21a9ed826036f770667aea70eb70f91f50d1ac60245c20725d93dbec42a41711e4ba6762023a2a010000001976a914b39a791bdaa16ec039fbabe4e46efb7cab150c5388ac00000000",["2aeff42e83cf2fa7a271c9e600923458e5b44d3cc086b68fd5e1bd2f8fb2c2f4","5913bd4a1332e085c975e851375027ce57c2b66a865eb11085ab1b26fa59ea55","7ab6d88c0da99231f817a1a588ccf941ded398e24ec1510745dd23459444770c","bd52c7bdc423945a8a9bafaa0738c7a0edd32792506743acd39c9593cf964d43","c076078e0fc41fbc4ef1e8ed3368516bde09b8d98cf13246a1f63bd25c902099","0467ec38d4df01dc161f2aec3ef865832d8d1689067bb155d5aa359b0433de55"],"20000000","190336be","69a5ca29",true],"id":null} 
```

## Comments

### skot on 2026-03-02

looking at your log files, it doesn't seem like these are actually duplicate shares. Are you getting the mining.submit JobID and nonce fields mixed up?

### mutatrum on 2026-03-02

This might be related: https://github.com/bitaxeorg/ESP-Miner/pull/420#issuecomment-3984181621. My suspicion is that the `mining.notify` doesn't trigger the `queue_dequeue_timeout` in the `create_jobs_task`, but I haven't figured it out completely yet.

### blackmennewstyle on 2026-03-03

> looking at your log files, it doesn't seem like these are actually duplicate shares. Are you getting the mining.submit JobID and nonce fields mixed up?

Thanks for your answer.
But it is definitely not mixed up inside `miningcore` (stratum software), `jobId` is not involved during the job hashing process only prior in order to find the correct job class/object.

Here the code which checks for duplicate shares, it is tied to each job class/object, stored inside a `dictionnary`:
```
    protected bool RegisterSubmit(string extraNonce1, string extraNonce2, string nTime, string nonce)
    {
        var key = new StringBuilder()
            .Append(extraNonce1)
            .Append(extraNonce2)
            .Append(nTime)
            .Append(nonce)
            .ToString();

        return submissions.TryAdd(key, true);
    }
```
You can analyze the `mining.submit`:
```
{"id":21,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.janus","00000006","3b000000","69a5c579","ad910248","02cc2000"]}
```
index 0: `worker`
index 1: `jobId`
index 2: `extranonce2`
index 3: `nTime`
index 4: `nonce`
(optional index 5: `versionBits`)

`extranonce1` is only known by the stratum and each worker has an unique one until a specific number based on the `extranonce1 size`, here 4 bits.

It's a very odd issue i agree but the fact it is always triggered by a `mining.set_difficulty` following by a `mining.notify` with a `cleanJob` set to `false`, points definitely toward a little glitch in the mining software.

@mutatrum I think you might be on something.

### skot on 2026-03-03

> > looking at your log files, it doesn't seem like these are actually duplicate shares. Are you getting the mining.submit JobID and nonce fields mixed up?
> 
> Thanks for your answer.
> But it is definitely not mixed up inside `miningcore` (stratum software), `jobId` is not involved during the job hashing process only prior in order to find the correct job class/object.
> 
> Here the code which checks for duplicate shares, it is tied to each job class/object, stored inside a `dictionnary`:
> ```
>     protected bool RegisterSubmit(string extraNonce1, string extraNonce2, string nTime, string nonce)
>     {
>         var key = new StringBuilder()
>             .Append(extraNonce1)
>             .Append(extraNonce2)
>             .Append(nTime)
>             .Append(nonce)
>             .ToString();
> 
>         return submissions.TryAdd(key, true);
>     }
> ```
> You can analyze the `mining.submit`:
> ```
> {"id":21,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.janus","00000006","3b000000","69a5c579","ad910248","02cc2000"]}
> ```
> index 0: `worker`
> index 1: `jobId`
> index 2: `extranonce2`
> index 3: `nTime`
> index 4: `nonce`
> (optional index 5: `versionBits`)
> 
> `extranonce1` is only known by the stratum and each worker has an unique one until a specific number based on the `extranonce1 size`, here 4 bits.
> 
> It's a very odd issue i agree but the fact it is always triggered by a `mining.set_difficulty` following by a `mining.notify` with a `cleanJob` set to `false`, points definitely toward a little glitch in the mining software.
> 
> @mutatrum I think you might be on something.

Look at your log. These aren't duplicate shares.

### mutatrum on 2026-03-04

I didn't read the logs complete, but that's right. Each `mining.submit` has a different `extranonce2`, `nonce` and `versionBits` field:
```
{"id":21,"method":"mining.submit","params":["...","00000006","3b000000","69a5c579","ad910248","02cc2000"]}
{"id":22,"method":"mining.submit","params":["...","00000006","89000000","69a5c579","debe0186","0555e000"]}
{"id":23,"method":"mining.submit","params":["...","00000006","95000000","69a5c579","5d110336","00218000"]}
{"id":24,"method":"mining.submit","params":["...","00000006","c5000000","69a5c579","0f870304","03c8e000"]}
```

### blackmennewstyle on 2026-03-05

I don't quite understand your counter-argument here.

The way it works guys, if these combos of `extranonce1`, `extranonce2`, `nonce` & `nTime` have already been registered previously in the dictionnary, they will will be rejected if they are submitted again.

```
// extract params
var workerValue = (submitParams[0] as string)?.Trim();
var jobId = submitParams[1] as string;
var extraNonce2 = submitParams[2] as string;
var nTime = submitParams[3] as string;
var nonce = submitParams[4] as string;
var versionBits = context.VersionRollingMask.HasValue ? submitParams[5] as string : null;
```

Let's refer to documentation: https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2.tryadd?view=net-6.0

**Remarks**

Unlike the [Add](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2.add?view=net-6.0) method, this method doesn't throw an exception if the element with the given key exists in the dictionary. Unlike the Dictionary indexer, TryAdd doesn't override the element if the element with the given key exists in the dictionary. If the key already exists, **TryAdd** does nothing and returns false.

In simple terms again, those combos were all submitted already. You have unfortunately a glitch in your code.

### DankMiner on 2026-03-05

This looks like a client-side nonce tracking issue.

When `mining.set_difficulty` is followed by `mining.notify` with `cleanJob=false`, ESP-Miner doesn't reset its nonce state or re-feed the ASIC with the updated job. So the ASIC keeps scanning the same nonce space and resubmits solutions the pool already saw, hence the duplicate rejections.

The fix should be: on any `mining.notify` (regardless of `cleanJob`), reset the submitted-nonce tracking and update the ASIC work params with the new job ID. The `cleanJob=false` flag means "don't abandon valid in-progress work," not "ignore this job entirely."

The reset logic clearly exists already since `cleanJob=true` works fine, it just needs to also trigger the nonce/job-ID refresh on the `false` path.

### mutatrum on 2026-03-05

Is this with m45core, or which stratum implementation? As I'm a bit confused with the context now. F.e. ckpool has vardiff, and I haven't seen duplicate shares there.

Can you share the logs from the miner side, where you see it send a share, receive the diff adjustment, and resend the same share? It's really difficult to reason with logs from the other side.

Which firmware is running on the miner, and what device is it?

### blackmennewstyle on 2026-03-05

> Is this with m45core, or which stratum implementation? As I'm a bit confused with the context now. F.e. ckpool has vardiff, and I haven't seen duplicate shares there.
> 
> Can you share the logs from the miner side, where you see it send a share, receive the diff adjustment, and resend the same share? It's really difficult to reason with logs from the other side.
> 
> Which firmware is running on the miner, and what device is it?

Stratum software is `miningcore` written in C#, devices are BitAxe 601 (Gamma?), on latest firmware.

I put one of my BitAxe on CKPool all afternoon  and i am getting rejected shares, they are of type unknown, sadly the log feature is quite limited so i can not see the rejected shares. If there is a way please feel free to share.

One thing i noticed however, the `varDiff` on CKPool is very very slow, which generally means, it is configured to mitigate as much as possible most issues.

### mutatrum on 2026-03-05

> When `mining.set_difficulty` is followed by `mining.notify` with `cleanJob=false`, ESP-Miner doesn't reset its nonce state or re-feed the ASIC with the updated job. So the ASIC keeps scanning the same nonce space and resubmits solutions the pool already saw, hence the duplicate rejections.

This is by design. There is a 500ms timeout on single chip devices, and if `cleanJob=false`, the job will only be cycled after this timeout. On a Gamma, the nonce space currently takes about 2.8 seconds IIRC, so it should not cause duplicates.

I think there's something else going on here, but I don't know what, yet. The unknown rejects from ckpool is fixed by #1586, and is most likely Stale, and not Duplicate, but we can only know this for sure if you would test it with that PR in the firmware.

One way would be to connect the miner to USB, and capture the serial logging directly to a file. That, or capture the log websocket and store it to a file. Either way should give you infinite log retention.

### blackmennewstyle on 2026-03-08

> > When `mining.set_difficulty` is followed by `mining.notify` with `cleanJob=false`, ESP-Miner doesn't reset its nonce state or re-feed the ASIC with the updated job. So the ASIC keeps scanning the same nonce space and resubmits solutions the pool already saw, hence the duplicate rejections.
> 
> This is by design. There is a 500ms timeout on single chip devices, and if `cleanJob=false`, the job will only be cycled after this timeout. On a Gamma, the nonce space currently takes about 2.8 seconds IIRC, so it should not cause duplicates.
> 
> I think there's something else going on here, but I don't know what, yet. The unknown rejects from ckpool is fixed by [#1586](https://github.com/bitaxeorg/ESP-Miner/pull/1586), and is most likely Stale, and not Duplicate, but we can only know this for sure if you would test it with that PR in the firmware.
> 
> One way would be to connect the miner to USB, and capture the serial logging directly to a file. That, or capture the log websocket and store it to a file. Either way should give you infinite log retention.

Well,

I tried to build the firmware here and i can not pass that step:
```
[1574/1627] Linking CXX static library...ssif__esp_lvgl_port/liblvgl_port_lib.a
FAILED: openapi_generate.stamp /workspace/build/openapi_generate.stamp 
cd /workspace/main/http_server/axe-os && /usr/bin/npm i && /usr/bin/npm run generate:api && /opt/esp/tools/cmake/3.30.2/bin/cmake -E touch /workspace/build/openapi_generate.stamp
ninja: build stopped: subcommand failed.
ninja failed with exit code 1, output of the command is in the /workspace/build/log/idf_py_stderr_output_506 and /workspace/build/log/idf_py_stdout_output_506
```

### blackmennewstyle on 2026-03-09

The code change pushed by @DankMiner seems to have made a little difference.

After the difficulty change, the miner only sends a single duplicate share:

```
[2026-03-09 22:15:47.6068] [I] [btc1] Detected new transaction(s) for block 125426 [POLL] 
[2026-03-09 22:15:47.6068] [I] [btc1] Broadcasting job 00000004 
[2026-03-09 22:15:47.6068] [D] [btc1] [0HNJU531GL5HV] Sending: {"jsonrpc":"2.0","method":"mining.notify","params":["00000004","380766bd7f5c07aa228793f52dd3a3bcedc956337b246a3c0005244300000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3203f2e901049346af6900","1f4d696e696e67636f72652f436564726963204352495350494e2f61735f544800000000020000000000000000266a24aa21a9ed023607654daef82ab7ebd25935d165d02a0b25cca316d34015c1f9301907fc2f1255172a010000001976a914b39a791bdaa16ec039fbabe4e46efb7cab150c5388ac00000000",["62b7d095e97b004ea73e6d15a501b1a167d8e895820450d0be260e419ed0396c","4cdb5855d4b20acc8337b7fd597b62fc1a68fccf74d1ce1b2611bcdab912bb04","d794b42447af4662cfb6a8027796d23e6a7f454faf5f0ee5d96c82ffa39eca61","359a414ef868b93d00b569f5051d0adfb69febf4a9aa9b3065fb2e72d9e0e85f"],"20000000","190327c4","69af4879",true],"id":null} 
[2026-03-09 22:15:52.5619] [D] [btc1] Vardiff Idle Update pass begins 
[2026-03-09 22:15:52.5619] [D] [btc1] [0HNJU531GL5HV] Updating VarDiff [IDLE] 
[2026-03-09 22:15:52.5619] [D] [btc1] Vardiff Idle Update pass ends 
[2026-03-09 22:16:34.6608] [D] [btc1] [0HNJU531GL5HV] [NET] Received data: {"id":10,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000004","5d000000","69af4879","67ea0196","034b4000"]}
 
[2026-03-09 22:16:34.6608] [D] [btc1] [0HNJU531GL5HV] [NET] Waiting for data ... 
[2026-03-09 22:16:34.6608] [D] [btc1] [0HNJU531GL5HV] [PIPE] Received data: {"id":10,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000004","5d000000","69af4879","67ea0196","034b4000"]}
 
[2026-03-09 22:16:34.6608] [D] [btc1] [0HNJU531GL5HV] Dispatching request 'mining.submit' [10] 
[2026-03-09 22:16:34.6608] [I] [btc1] [0HNJU531GL5HV] Share accepted: D=8192 
[2026-03-09 22:16:34.6608] [D] [btc1] [0HNJU531GL5HV] Updating VarDiff 
[2026-03-09 22:16:34.6608] [D] [btc1] [0HNJU531GL5HV] Sending: {"jsonrpc":"2.0","result":true,"id":10,"error":null} 
[2026-03-09 22:16:34.6608] [I] [btc1] [0HNJU531GL5HV] VarDiff update to 4585.288 
[2026-03-09 22:16:34.6608] [D] [btc1] [0HNJU531GL5HV] [PIPE] Waiting for data ... 
[2026-03-09 22:16:34.6608] [D] [btc1] [0HNJU531GL5HV] Sending: {"jsonrpc":"2.0","method":"mining.set_difficulty","params":[4585.288492389524],"id":null} 
[2026-03-09 22:16:34.6608] [D] [btc1] [0HNJU531GL5HV] Sending: {"jsonrpc":"2.0","method":"mining.notify","params":["00000004","380766bd7f5c07aa228793f52dd3a3bcedc956337b246a3c0005244300000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3203f2e901049346af6900","1f4d696e696e67636f72652f436564726963204352495350494e2f61735f544800000000020000000000000000266a24aa21a9ed023607654daef82ab7ebd25935d165d02a0b25cca316d34015c1f9301907fc2f1255172a010000001976a914b39a791bdaa16ec039fbabe4e46efb7cab150c5388ac00000000",["62b7d095e97b004ea73e6d15a501b1a167d8e895820450d0be260e419ed0396c","4cdb5855d4b20acc8337b7fd597b62fc1a68fccf74d1ce1b2611bcdab912bb04","d794b42447af4662cfb6a8027796d23e6a7f454faf5f0ee5d96c82ffa39eca61","359a414ef868b93d00b569f5051d0adfb69febf4a9aa9b3065fb2e72d9e0e85f"],"20000000","190327c4","69af4879",false],"id":null} 
[2026-03-09 22:17:21.6807] [D] [btc1] [0HNJU531GL5HV] [NET] Received data: {"id":11,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000004","5d000000","69af4879","67ea0196","034b4000"]}
 
[2026-03-09 22:17:21.6807] [D] [btc1] [0HNJU531GL5HV] [NET] Waiting for data ... 
[2026-03-09 22:17:21.6807] [D] [btc1] [0HNJU531GL5HV] [PIPE] Received data: {"id":11,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000004","5d000000","69af4879","67ea0196","034b4000"]}
 
[2026-03-09 22:17:21.6807] [D] [btc1] [0HNJU531GL5HV] Dispatching request 'mining.submit' [11] 
[2026-03-09 22:17:21.6807] [I] [btc1] [0HNJU531GL5HV] Share rejected: duplicate share [bitaxe/BM1370/v2.13.2-1-g5d268fb-dirty] 
[2026-03-09 22:17:21.6807] [D] [btc1] [0HNJU531GL5HV] [PIPE] Waiting for data ... 
[2026-03-09 22:17:21.6856] [D] [btc1] [0HNJU531GL5HV] Sending: {"jsonrpc":"2.0","method":"mining.submit","result":false,"error":{"code":22,"message":"duplicate share","data":null},"id":11} 
[2026-03-09 22:17:51.1859] [D] [btc1] [0HNJU531GL5HV] [NET] Received data: {"id":12,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000004","98000000","69af4879","b81303b4","02944000"]}
 
[2026-03-09 22:17:51.1859] [D] [btc1] [0HNJU531GL5HV] [NET] Waiting for data ... 
[2026-03-09 22:17:51.1859] [D] [btc1] [0HNJU531GL5HV] [PIPE] Received data: {"id":12,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000004","98000000","69af4879","b81303b4","02944000"]}
 
[2026-03-09 22:17:51.1859] [D] [btc1] [0HNJU531GL5HV] Dispatching request 'mining.submit' [12] 
[2026-03-09 22:17:51.1859] [I] [btc1] [0HNJU531GL5HV] Share accepted: D=4585.288 
[2026-03-09 22:17:51.1859] [D] [btc1] [0HNJU531GL5HV] Updating VarDiff 
[2026-03-09 22:17:51.1859] [D] [btc1] [0HNJU531GL5HV] Sending: {"jsonrpc":"2.0","result":true,"id":12,"error":null} 
```

### blackmennewstyle on 2026-03-09

I think i identified the issue or real culprit. You guys doesn't take in account the `extranonce2` sent by the pool.

```
[2026-03-09 22:31:08.0118] [I] [btc1] [0HNJU5E2UA0H8] Accepting connection from ::ffff:10.10.3.4:55113 ... 
[2026-03-09 22:31:08.0122] [I] [btc1] [0HNJU5E2UA0H8] Connection from ::ffff:10.10.3.4:55113 accepted on port 4544 
[2026-03-09 22:31:08.0122] [D] [btc1] [0HNJU5E2UA0H8] [NET] Waiting for data ... 
[2026-03-09 22:31:08.0122] [D] [btc1] [0HNJU5E2UA0H8] [PIPE] Waiting for data ... 
[2026-03-09 22:31:08.0270] [D] [btc1] [0HNJU5E2UA0H8] [NET] Received data: {"id":1,"method":"mining.configure","params":[["version-rolling"],{"version-rolling.mask":"ffffffff"}]}
 
[2026-03-09 22:31:08.0270] [D] [btc1] [0HNJU5E2UA0H8] [NET] Waiting for data ... 
[2026-03-09 22:31:08.0270] [D] [btc1] [0HNJU5E2UA0H8] [PIPE] Received data: {"id":1,"method":"mining.configure","params":[["version-rolling"],{"version-rolling.mask":"ffffffff"}]}
 
[2026-03-09 22:31:08.0270] [D] [btc1] [0HNJU5E2UA0H8] Dispatching request 'mining.configure' [1] 
[2026-03-09 22:31:08.0319] [I] [btc1] [0HNJU5E2UA0H8] Using version-rolling mask 1fffe000 
[2026-03-09 22:31:08.0319] [D] [btc1] [0HNJU5E2UA0H8] [PIPE] Waiting for data ... 
[2026-03-09 22:31:08.0325] [D] [btc1] [0HNJU5E2UA0H8] Sending: {"jsonrpc":"2.0","result":{"version-rolling":true,"version-rolling.mask":"1fffe000"},"id":1,"error":null} 
[2026-03-09 22:31:08.0420] [D] [btc1] [0HNJU5E2UA0H8] [NET] Received data: {"id":2,"method":"mining.subscribe","params":["bitaxe/BM1370/v2.13.2-1-g5d268fb-dirty"]}
 
[2026-03-09 22:31:08.0420] [D] [btc1] [0HNJU5E2UA0H8] [NET] Waiting for data ... 
[2026-03-09 22:31:08.0420] [D] [btc1] [0HNJU5E2UA0H8] [PIPE] Received data: {"id":2,"method":"mining.subscribe","params":["bitaxe/BM1370/v2.13.2-1-g5d268fb-dirty"]}
 
[2026-03-09 22:31:08.0420] [D] [btc1] [0HNJU5E2UA0H8] Dispatching request 'mining.subscribe' [2] 
[2026-03-09 22:31:08.0420] [D] [btc1] [0HNJU5E2UA0H8] [PIPE] Waiting for data ... 
[2026-03-09 22:31:08.0420] [D] [btc1] [0HNJU5E2UA0H8] Sending: {"jsonrpc":"2.0","result":[[["mining.set_difficulty","0HNJU5E2UA0H8"],["mining.notify","0HNJU5E2UA0H8"]],"50000002",4],"id":2,"error":null} 
[2026-03-09 22:31:08.0420] [D] [btc1] [0HNJU5E2UA0H8] Sending: {"jsonrpc":"2.0","method":"mining.set_difficulty","params":[8192.0],"id":null} 
[2026-03-09 22:31:08.0420] [D] [btc1] [0HNJU5E2UA0H8] Sending: {"jsonrpc":"2.0","method":"mining.notify","params":["00000001","7674ac18811fee70d1fb69665ba15041b881ce9d0f5f255d0000f38100000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3203f5e90104144aaf6900","1f4d696e696e67636f72652f436564726963204352495350494e2f61735f544800000000020000000000000000266a24aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf900f2052a010000001976a914b39a791bdaa16ec039fbabe4e46efb7cab150c5388ac00000000",[],"20000000","190327c4","69af4f32",true],"id":null} 
[2026-03-09 22:31:08.0513] [D] [btc1] [0HNJU5E2UA0H8] [NET] Received data: {"id":3,"method":"mining.authorize","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","x"]}
```

The pool tells you that your `extranonce2` is: `50000002`
```
[[["mining.set_difficulty","0HNJU5E2UA0H8"],["mining.notify","0HNJU5E2UA0H8"]],"50000002",4],"id":2,"error":null} 
```

If you pay attention to all `mining.submit`, the `extranonce2` is `DIFFERENT`.

### mutatrum on 2026-03-10

> The pool tells you that your `extranonce2` is: `50000002`
> 
> ```
> [[["mining.set_difficulty","0HNJU5E2UA0H8"],["mining.notify","0HNJU5E2UA0H8"]],"50000002",4],"id":2,"error":null} 
> ```
> 
> If you pay attention to all `mining.submit`, the `extranonce2` is `DIFFERENT`.

This is not `extranonce2`, `50000002` is the extranonce1. The miner is allowed to change extranonce2. The only thing the pool says is how many bytes the extranonce2 has to be, which is `4` in this case.

<img width="1437" height="447" alt="Image" src="https://github.com/user-attachments/assets/6b826c71-dc7e-4796-8e1f-4559a98f15df" />

### blackmennewstyle on 2026-03-10

> > The pool tells you that your `extranonce2` is: `50000002`
> > ```
> > [[["mining.set_difficulty","0HNJU5E2UA0H8"],["mining.notify","0HNJU5E2UA0H8"]],"50000002",4],"id":2,"error":null} 
> > ```
> > 
> > 
> >     
> >       
> >     
> > 
> >       
> >     
> > 
> >     
> >   
> > If you pay attention to all `mining.submit`, the `extranonce2` is `DIFFERENT`.
> 
> This is not `extranonce2`, `50000002` is the extranonce1. The miner is allowed to change extranonce2. The only thing the pool says is how many bytes the extranonce2 has to be, which is `4` in this case.
> <img alt="Image" width="1437" height="447" src="https://private-user-images.githubusercontent.com/56344102/560801137-6b826c71-dc7e-4796-8e1f-4559a98f15df.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzMxNTUyNTQsIm5iZiI6MTc3MzE1NDk1NCwicGF0aCI6Ii81NjM0NDEwMi81NjA4MDExMzctNmI4MjZjNzEtZGM3ZS00Nzk2LThlMWYtNDU1OWE5OGYxNWRmLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAzMTAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMzEwVDE1MDIzNFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWI5YjgzYjFhN2ExYjRkODk5NDY1YjI1NjBjZmU4NDQ3ZmQ1ZmJlYjIwNzcxYzMwMmE2N2RhMmE0YWIzOGNkOGMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.pMRM1V1XLVHneDCCXrlqUycQOtzX9TsIscf6vMl984o">

Sorry, i actually meant to write `extranonce1` in first place, my bad.


It does not matter anyway, i identified where the issue is after i was able to access the whole log. I had some errors about some RPC message not being taken in account. Now it fixed.

```
₿ (2988094) stratum_task: Clean Jobs: clearing queue
₿ (2988094) stratum_api: tx: {"id":1,"method":"mining.configure","params":[["version-rolling"],{"version-rolling.mask":"ffffffff"}]}
₿ (2988108) stratum_api: tx: {"id":2,"method":"mining.subscribe","params":["bitaxe/BM1370/v2.13.2-1-g5d268fb-dirty"]}
₿ (2988119) stratum_api: tx: {"id":3,"method":"mining.authorize","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","x"]}
₿ (2988134) stratum_api: rx: {"jsonrpc":"2.0","result":{"version-rolling":true,"version-rolling.mask":"1fffe000"},"id":1,"error":null}
₿ (2988143) stratum_task: Set version mask: 1fffe000
₿ (2988149) stratum_api: rx: {"jsonrpc":"2.0","result":[[["mining.set_difficulty","0HNJUMEU1NQGL"],["mining.notify","0HNJUMEU1NQGL"]],"40000002",4],"id":2,"error":null}
₿ (2988165) stratum_task: Set extranonce: 40000002, extranonce_2_len: 4
₿ (2988172) stratum_api: rx: {"jsonrpc":"2.0","method":"mining.set_difficulty","params":[8192.0],"id":null}
₿ (2988182) stratum_task: Set pool difficulty: 8192
```
The amount of rejected shares is now way more reasonable within a margin of `+0.1%` (all exclusively duplicated shares).

The same little glitch though sometimes like here:
```
[2026-03-10 14:58:49.0648] [D] [btc1] [0HNJUMEU1NQGL] [PIPE] Received data: {"id":21,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000027","7a000000","69b0316b","44800108","01210000"]}
 
[2026-03-10 14:58:49.0648] [D] [btc1] [0HNJUMEU1NQGL] Dispatching request 'mining.submit' [21] 
[2026-03-10 14:58:49.0648] [I] [btc1] [0HNJUMEU1NQGL] Share accepted: D=6306.066 
[2026-03-10 14:58:49.0648] [D] [btc1] [0HNJUMEU1NQGL] Sending: {"jsonrpc":"2.0","result":true,"id":21,"error":null} 
[2026-03-10 14:58:49.0648] [D] [btc1] [0HNJUMEU1NQGL] Updating VarDiff 
[2026-03-10 14:58:49.0648] [I] [btc1] [0HNJUMEU1NQGL] VarDiff update to 3755.505 
2026-03-10 14:58:49.0648] [D] [btc1] [0HNJUMEU1NQGL] Sending: {"jsonrpc":"2.0","method":"mining.set_difficulty","params":[3755.5054340299434],"id":null} 
[2026-03-10 14:58:49.0648] [D] [btc1] [0HNJUMEU1NQGL] Sending: {"jsonrpc":"2.0","method":"mining.notify","params":["00000027","4541c5ccfcfb9bfe12fa52947236970d116bbaa3d5a41d310007338000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff32032dea01046b31b06900","1f4d696e696e67636f72652f436564726963204352495350494e2f61735f544800000000020000000000000000266a24aa21a9edf2555e0a67b91bfd2c6b972b2709c3bf220945c06ef77950228aac55c5d70a6a345f062a010000001976a914b39a791bdaa16ec039fbabe4e46efb7cab150c5388ac00000000",["a11b752ac5753a6a4d76a3bc0236e36c25b290130f62a405d9b1c3710119422f","8aaeda435bc4759f580c718cad1a05184cab0342a6dbb753d6ee26311dfabca9","65e6d9d3dfae69fc78bdc99dfae3cc7f3f9af815f13aa91180b3d9b90b603ed3","08f0b6a6f1f04a5b0983606c3c8271c095d74ed54e6abf5b4843a74ab82df833","f9de5434e6c47d584d7d09d799b6fcf10d3ed859761513947296999fbb5e9276","e2faa95e565fd81521e46641c117f2cfc458b76a80421922c4540851b10c83b6"],"20000000","190327c4","69b0316b",false],"id":null}
[2026-03-10 14:59:50.5591] [D] [btc1] [0HNJUMEU1NQGL] [PIPE] Received data: {"id":22,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000027","7a000000","69b0316b","44800108","01210000"]}
 
[2026-03-10 14:59:50.5591] [D] [btc1] [0HNJUMEU1NQGL] Dispatching request 'mining.submit' [22] 
[2026-03-10 14:59:50.5591] [I] [btc1] [0HNJUMEU1NQGL] Share rejected: duplicate share [bitaxe/BM1370/v2.13.2-1-g5d268fb-dirty] 
```
Right after a `varDiff` change, the exact same solution sent again. Perfectly flagrant here.

It just happens once now and the following solutions are all accepted.

Probably that latency you were talking about if i recall correctly.

### blackmennewstyle on 2026-03-11

You have definitely a glitch in your code. Look here:
```
[2026-03-11 01:30:16.6969] [D] [btc1] [0HNJV0SGU7487] Sending: {"jsonrpc":"2.0","method":"mining.notify","params":["00000038","d00b00389a7e0bf8c2472a73dac9457fec4739b274276b300000b2a100000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff32035eea0104a8c5b06900","1f4d696e696e67636f72652f436564726963204352495350494e2f61735f544800000000020000000000000000266a24aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf900f2052a010000001976a914b39a791bdaa16ec039fbabe4e46efb7cab150c5388ac00000000",[],"20000000","190327c4","69b0d391",true],"id":null} 
[2026-03-11 01:30:17.8633] [D] [btc1] [0HNJV0SGU7487] [NET] Received data: {"id":113,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000038","02000000","69b0d391","eab30158","00fde000"]}
 
[2026-03-11 01:30:17.8633] [D] [btc1] [0HNJV0SGU7487] [NET] Waiting for data ... 
[2026-03-11 01:30:17.8633] [D] [btc1] [0HNJV0SGU7487] [PIPE] Received data: {"id":113,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000038","02000000","69b0d391","eab30158","00fde000"]}
 
[2026-03-11 01:30:17.8633] [D] [btc1] [0HNJV0SGU7487] Dispatching request 'mining.submit' [113] 
[2026-03-11 01:30:17.8633] [I] [btc1] [0HNJV0SGU7487] Share accepted: D=4171.842 
[2026-03-11 01:30:17.8633] [D] [btc1] [0HNJV0SGU7487] Sending: {"jsonrpc":"2.0","result":true,"id":113,"error":null} 
[2026-03-11 01:30:17.8633] [D] [btc1] [0HNJV0SGU7487] Updating VarDiff 
[2026-03-11 01:30:17.8633] [D] [btc1] [0HNJV0SGU7487] [PIPE] Waiting for data ... 
[2026-03-11 01:30:20.1351] [D] [btc1] [0HNJV0SGU7487] [NET] Received data: {"id":114,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000038","06000000","69b0d391","03c001c2","0449e000"]}
 
[2026-03-11 01:30:20.1351] [D] [btc1] [0HNJV0SGU7487] [NET] Waiting for data ... 
[2026-03-11 01:30:20.1351] [D] [btc1] [0HNJV0SGU7487] [PIPE] Received data: {"id":114,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000038","06000000","69b0d391","03c001c2","0449e000"]}
 
[2026-03-11 01:30:20.1351] [D] [btc1] [0HNJV0SGU7487] Dispatching request 'mining.submit' [114] 
[2026-03-11 01:30:20.1351] [I] [btc1] [0HNJV0SGU7487] Share accepted: D=4171.842 
[2026-03-11 01:30:20.1351] [D] [btc1] [0HNJV0SGU7487] Updating VarDiff 
[2026-03-11 01:30:20.1351] [D] [btc1] [0HNJV0SGU7487] [PIPE] Waiting for data ... 
[2026-03-11 01:30:20.1351] [D] [btc1] [0HNJV0SGU7487] Sending: {"jsonrpc":"2.0","result":true,"id":114,"error":null} 
[2026-03-11 01:30:22.2295] [D] [btc1] [0HNJV0SGU7487] [NET] Received data: {"id":115,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000038","0a000000","69b0d391","6df600ca","05612000"]}
 
[2026-03-11 01:30:22.2295] [D] [btc1] [0HNJV0SGU7487] [NET] Waiting for data ... 
[2026-03-11 01:30:22.2295] [D] [btc1] [0HNJV0SGU7487] [PIPE] Received data: {"id":115,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000038","0a000000","69b0d391","6df600ca","05612000"]}
 
[2026-03-11 01:30:22.2295] [D] [btc1] [0HNJV0SGU7487] Dispatching request 'mining.submit' [115] 
[2026-03-11 01:30:22.2295] [I] [btc1] [0HNJV0SGU7487] Share accepted: D=4171.842 
[2026-03-11 01:30:22.2295] [D] [btc1] [0HNJV0SGU7487] Sending: {"jsonrpc":"2.0","result":true,"id":115,"error":null} 
[2026-03-11 01:30:22.2295] [D] [btc1] [0HNJV0SGU7487] Updating VarDiff 
[2026-03-11 01:30:22.2295] [D] [btc1] [0HNJV0SGU7487] [PIPE] Waiting for data ... 
[2026-03-11 01:30:35.9086] [D] [btc1] [0HNJV0SGU7487] [NET] Received data: {"id":116,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000038","26000000","69b0d391","e7c80130","010fa000"]}
 
[2026-03-11 01:30:35.9086] [D] [btc1] [0HNJV0SGU7487] [NET] Waiting for data ... 
[2026-03-11 01:30:35.9086] [D] [btc1] [0HNJV0SGU7487] [PIPE] Received data: {"id":116,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000038","26000000","69b0d391","e7c80130","010fa000"]}
 
[2026-03-11 01:30:35.9086] [D] [btc1] [0HNJV0SGU7487] Dispatching request 'mining.submit' [116] 
[2026-03-11 01:30:35.9086] [I] [btc1] [0HNJV0SGU7487] Share accepted: D=4171.842 
[2026-03-11 01:30:35.9086] [D] [btc1] [0HNJV0SGU7487] Updating VarDiff 
[2026-03-11 01:30:35.9086] [D] [btc1] [0HNJV0SGU7487] Sending: {"jsonrpc":"2.0","result":true,"id":116,"error":null} 
[2026-03-11 01:30:35.9086] [D] [btc1] [0HNJV0SGU7487] [PIPE] Waiting for data ... 
[2026-03-11 01:31:23.4765] [D] [btc1] [0HNJV0SGU7487] [NET] Received data: {"id":117,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000038","85000000","69b0d391","89530384","00b28000"]}
 
[2026-03-11 01:31:23.4765] [D] [btc1] [0HNJV0SGU7487] [NET] Waiting for data ... 
[2026-03-11 01:31:23.4765] [D] [btc1] [0HNJV0SGU7487] [PIPE] Received data: {"id":117,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000038","85000000","69b0d391","89530384","00b28000"]}
 
[2026-03-11 01:31:23.4765] [D] [btc1] [0HNJV0SGU7487] Dispatching request 'mining.submit' [117] 
[2026-03-11 01:31:23.4765] [I] [btc1] [0HNJV0SGU7487] Share accepted: D=4171.842 
[2026-03-11 01:31:23.4765] [D] [btc1] [0HNJV0SGU7487] Sending: {"jsonrpc":"2.0","result":true,"id":117,"error":null} 
[2026-03-11 01:31:23.4765] [D] [btc1] [0HNJV0SGU7487] Updating VarDiff 
[2026-03-11 01:31:23.4765] [D] [btc1] [0HNJV0SGU7487] [PIPE] Waiting for data ... 
[2026-03-11 01:32:47.4307] [D] [btc1] [0HNJV0SGU7487] [NET] Received data: {"id":118,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000038","2c010000","69b0d391","4b980278","042dc000"]}
 
[2026-03-11 01:32:47.4307] [D] [btc1] [0HNJV0SGU7487] [NET] Waiting for data ... 
[2026-03-11 01:32:47.4307] [D] [btc1] [0HNJV0SGU7487] [PIPE] Received data: {"id":118,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000038","2c010000","69b0d391","4b980278","042dc000"]}
 
[2026-03-11 01:32:47.4307] [D] [btc1] [0HNJV0SGU7487] Dispatching request 'mining.submit' [118] 
[2026-03-11 01:32:47.4307] [I] [btc1] [0HNJV0SGU7487] Share accepted: D=4171.842 
[2026-03-11 01:32:47.4307] [D] [btc1] [0HNJV0SGU7487] Sending: {"jsonrpc":"2.0","result":true,"id":118,"error":null} 
[2026-03-11 01:32:47.4307] [D] [btc1] [0HNJV0SGU7487] Updating VarDiff 
[2026-03-11 01:32:47.4307] [I] [btc1] [0HNJV0SGU7487] VarDiff update to 2879.715 
[2026-03-11 01:32:47.4307] [D] [btc1] [0HNJV0SGU7487] [PIPE] Waiting for data ... 
[2026-03-11 01:32:47.4307] [D] [btc1] [0HNJV0SGU7487] Sending: {"jsonrpc":"2.0","method":"mining.set_difficulty","params":[2879.714532229609],"id":null} 
[2026-03-11 01:32:47.4307] [D] [btc1] [0HNJV0SGU7487] Sending: {"jsonrpc":"2.0","method":"mining.notify","params":["00000038","d00b00389a7e0bf8c2472a73dac9457fec4739b274276b300000b2a100000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff32035eea0104a8c5b06900","1f4d696e696e67636f72652f436564726963204352495350494e2f61735f544800000000020000000000000000266a24aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf900f2052a010000001976a914b39a791bdaa16ec039fbabe4e46efb7cab150c5388ac00000000",[],"20000000","190327c4","69b0d391",false],"id":null} 
[2026-03-11 01:32:48.6918] [D] [btc1] [0HNJV0SGU7487] [NET] Received data: {"id":119,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000038","02000000","69b0d391","eab30158","00fde000"]}
 
[2026-03-11 01:32:48.6918] [D] [btc1] [0HNJV0SGU7487] [NET] Waiting for data ... 
[2026-03-11 01:32:48.6918] [D] [btc1] [0HNJV0SGU7487] [PIPE] Received data: {"id":119,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000038","02000000","69b0d391","eab30158","00fde000"]}
 
[2026-03-11 01:32:48.6922] [D] [btc1] [0HNJV0SGU7487] Dispatching request 'mining.submit' [119] 
[2026-03-11 01:32:48.6922] [I] [btc1] [0HNJV0SGU7487] Share rejected: duplicate share [bitaxe/BM1370/v2.13.1] 
[2026-03-11 01:32:48.6922] [D] [btc1] [0HNJV0SGU7487] [PIPE] Waiting for data ... 
[2026-03-11 01:32:48.6922] [D] [btc1] [0HNJV0SGU7487] Sending: {"jsonrpc":"2.0","error":{"code":22,"message":"duplicate share","data":null},"id":119} 
[2026-03-11 01:32:50.9657] [D] [btc1] [0HNJV0SGU7487] [NET] Received data: {"id":120,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000038","06000000","69b0d391","03c001c2","0449e000"]}
 
[2026-03-11 01:32:50.9657] [D] [btc1] [0HNJV0SGU7487] [NET] Waiting for data ... 
[2026-03-11 01:32:50.9657] [D] [btc1] [0HNJV0SGU7487] [PIPE] Received data: {"id":120,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000038","06000000","69b0d391","03c001c2","0449e000"]}
 
[2026-03-11 01:32:50.9657] [D] [btc1] [0HNJV0SGU7487] Dispatching request 'mining.submit' [120] 
[2026-03-11 01:32:50.9657] [I] [btc1] [0HNJV0SGU7487] Share rejected: duplicate share [bitaxe/BM1370/v2.13.1] 
[2026-03-11 01:32:50.9657] [D] [btc1] [0HNJV0SGU7487] [PIPE] Waiting for data ... 
[2026-03-11 01:32:50.9657] [D] [btc1] [0HNJV0SGU7487] Sending: {"jsonrpc":"2.0","error":{"code":22,"message":"duplicate share","data":null},"id":120} 
[2026-03-11 01:32:53.0594] [D] [btc1] [0HNJV0SGU7487] [NET] Received data: {"id":121,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000038","0a000000","69b0d391","6df600ca","05612000"]}
 
[2026-03-11 01:32:53.0594] [D] [btc1] [0HNJV0SGU7487] [NET] Waiting for data ... 
[2026-03-11 01:32:53.0594] [D] [btc1] [0HNJV0SGU7487] [PIPE] Received data: {"id":121,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000038","0a000000","69b0d391","6df600ca","05612000"]}
```

See here after that difficulty change, resent literally the same solution already sent previously. Crystal clear.


Also i noticed with version `[bitaxe/BM1370/v2.13.1]`
```
₿ (8023450) stratum_api: tx: {"id":318,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","00000084","01000000","69b0e5c5","53900254","025c8000"]}
₿ (8023469) bm1370: Job ID: 30, Asic nr: 0, Core: 83/15, Ver: 026BE000
₿ (8023472) stratum_api: rx: {"jsonrpc":"2.0","error":{"code":22,"message":"duplicate share","data":null},"id":318}
```
Those rejected shares are not added anymore as `unknown` They are not even taken in account. Is it intentional?

### blackmennewstyle on 2026-03-11

I fixed the issue here locally 🍾 

Your current code is naively designed at that point: https://github.com/bitaxeorg/ESP-Miner/blob/4bfdccd993da82f07559a04c59469aa75f121639/main/tasks/create_jobs_task.c#L66

What should be done especially when you only clear your queue of jobs when `clean_jobs == true` here: https://github.com/bitaxeorg/ESP-Miner/blob/4bfdccd993da82f07559a04c59469aa75f121639/main/tasks/stratum_task.c#L568

Replace the following lines inside `main/tasks/create_jobs_task.c`
```
            extranonce_2 = 0;

            if (!current_mining_notification->clean_jobs) {
                continue;
            }
```
With the following:
```
            // reset extranonce2 only if clean_jobs == true
            // avoid a cosmic festival of duplicated shares
            if (current_mining_notification->clean_jobs) {
                extranonce_2 = 0;
            }
```
Duplicated shares are all gone 👍🏽 
```
[2026-03-11 06:22:00.5218] [D] [btc1] [0HNJV0SGU748D] Updating VarDiff 
[2026-03-11 06:22:00.5218] [I] [btc1] [0HNJV0SGU748D] VarDiff update to 6055.738 
[2026-03-11 06:22:00.5218] [D] [btc1] [0HNJV0SGU748D] [PIPE] Waiting for data ... 
[2026-03-11 06:22:00.5218] [D] [btc1] [0HNJV0SGU748D] Sending: {"jsonrpc":"2.0","method":"mining.set_difficulty","params":[6055.737623487953],"id":null} 
[2026-03-11 06:22:00.5218] [D] [btc1] [0HNJV0SGU748D] Sending: {"jsonrpc":"2.0","method":"mining.notify","params":["0000018b","67cdb08af7a2bea37e6aee554e8be79dd568b3a33ddaba230007282a00000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff320375ea01048a09b16900","1f4d696e696e67636f72652f436564726963204352495350494e2f61735f544800000000020000000000000000266a24aa21a9ed6d99a414cf81ecd5b704e41feabaeb27dfb952fdb7f792572cbc520823c4ea16d90d062a010000001976a914b39a791bdaa16ec039fbabe4e46efb7cab150c5388ac00000000",["6fc3ffde7282d9df33c31b803363740ab76b35f7182c42c05f0609328862221a","c31fa7972175cee30d928cf2e2febf670cfe155d81626e82fbe42631231afd46","ebec767d231061cdfe553b9196fd4b51025cb295691e825df0aac647dc9fd963","ccfe618cfdee1f72c9a2c986cf7e990695861155a7be7900db7295e004a2761f"],"20000000","190327c4","69b10a5e",false],"id":null} 
[2026-03-11 06:22:06.1500] [D] [DefaultHttpClientFactory] Starting HttpMessageHandler cleanup cycle with 1 items 
[2026-03-11 06:22:06.1500] [D] [DefaultHttpClientFactory] Ending HttpMessageHandler cleanup cycle after 0.0013ms - processed: 0 items - remaining: 1 items 
[2026-03-11 06:22:11.5795] [D] [btc1] [0HNJV0SGU748D] [NET] Received data: {"id":13,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","0000018b","12010000","69b10a5e","9aa00194","04a6c000"]}
 
[2026-03-11 06:22:11.5795] [D] [btc1] [0HNJV0SGU748D] [NET] Waiting for data ... 
[2026-03-11 06:22:11.5795] [D] [btc1] [0HNJV0SGU748D] [PIPE] Received data: {"id":13,"method":"mining.submit","params":["tb1qtl9daftpqser8lt7uqdrg82ztn7kxw2t4rsgaj.portia","0000018b","12010000","69b10a5e","9aa00194","04a6c000"]}
 
[2026-03-11 06:22:11.5795] [D] [btc1] [0HNJV0SGU748D] Dispatching request 'mining.submit' [13] 
[2026-03-11 06:22:11.5802] [I] [btc1] [0HNJV0SGU748D] Share accepted: D=6055.738 
[2026-03-11 06:22:11.5802] [D] [btc1] [0HNJV0SGU748D] Sending: {"jsonrpc":"2.0","result":true,"id":13,"error":null} 

```

Do you guys want a PR?

### mutatrum on 2026-03-11

> Do you guys want a PR?

Yes please.

### blackmennewstyle on 2026-03-11

Done.

https://github.com/bitaxeorg/ESP-Miner/pull/1603

### mutatrum on 2026-05-04

Is it possible to share the stratum connection? As for me it's still not clear why this is happening, and for me it's not reproducible on the pools I'm testing. It's also unclear if #1595 or #1603 are actually necessary, or if something else is going wrong.

### blackmennewstyle on 2026-05-05

> Is it possible to share the stratum connection? As for me it's still not clear why this is happening, and for me it's not reproducible on the pools I'm testing. It's also unclear if [#1595](https://github.com/bitaxeorg/ESP-Miner/pull/1595) or [#1603](https://github.com/bitaxeorg/ESP-Miner/pull/1603) are actually necessary, or if something else is going wrong.

https://github.com/bitaxeorg/ESP-Miner/pull/1595 does not fix the issue. Only https://github.com/bitaxeorg/ESP-Miner/pull/1603 fixes it.

You can test it out on my stratum pool. Stratum connection is all explained here:
https://bitcoin.cedric-crispin.com/start-mining/

**Stratum Host:** bitcoin.cedric-crispin.com
**Stratum Port (without SSL):** 4544

You will face the duplicated shares fairly quickly without my fix.

### blackmennewstyle on 2026-06-02

Resolved with (https://github.com/bitaxeorg/ESP-Miner/pull/1731)
