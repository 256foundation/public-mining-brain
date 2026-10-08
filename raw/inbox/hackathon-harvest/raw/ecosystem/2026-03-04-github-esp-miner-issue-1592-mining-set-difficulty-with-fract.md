# bitaxeorg/ESP-Miner issue #1592: mining.set_difficulty with fractional values are unsupported

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1592
> Collected: 2026-10-07
> Published: 2026-03-04

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1592
- State: closed
- Author: scottwalter
- Opened: 2026-03-04
- Closed: 2026-04-09
- Labels: none

## Description

Summary (v2.13.0, and below)

When a stratum host sends mining.set_difficulty with a fractional value (e.g., [0.001], [0.5], [2.5]), AxeOS truncates it to an integer because the entire difficulty pipeline uses uint32_t.

Affected code path:

Parsing (components/stratum/stratum_api.c:387):


uint32_t difficulty = cJSON_GetArrayItem(params, 0)->valueint;
Uses valueint (integer accessor) instead of valuedouble. A pool difficulty of 0.001 becomes 0.

Message struct (components/stratum/include/stratum_api.h:68):


uint32_t new_difficulty;
Global state (main/global_state.h:133):


uint32_t pool_difficulty;
Suggest difficulty (components/stratum/stratum_api.c:454):


int STRATUM_V1_suggest_difficulty(esp_transport_handle_t transport, int send_uid, uint32_t difficulty)
Formats with %ld — integer only.

NVS config (main/global_state.h:66):


uint16_t pool_difficulty;
Impact: Any pool that uses fractional difficulty values — common for BTC/BCH pools serving very low-hashrate miners like NerdMiner or small solo setups — will have difficulty truncated to 0 for sub-1 values, or lose the fractional component for values like 2.5 (becomes 2). A difficulty of 0 could cause undefined behavior or share rejection depending on how downstream code handles it.

Suggested fix: Change the difficulty type from uint32_t to double (or float) across the pipeline — parsing should use valuedouble from cJSON, the struct fields and global state should store as double, and formatting should use %f or %g.

## Comments

### mutatrum on 2026-03-04

esp-miner will not work below a diff of 256, the ASICs are hardcoded to a minimum diff of 256 which is already one share every second or so. A diff of 1 will be way too many shares for the serial line, and is also unneccesary.

Not sure why it would need to go below that.

### scottwalter on 2026-03-04

Hi Mutatrum, the issue is not about supporting sub 1 difficulties, perhaps the statement misled you. The real issue is that when the stratum host uses Floats for pool difficulties, such as 4096.123, AxeOS truncates that to 4096, so on occasion that is just enough of a precision change that AxeOS will send back a share that meets 4096 but not 4096.123, so the stratum host then rejects the share as "low diff".

### mutatrum on 2026-03-04

Which pool implementation is this? I've seen public pool do this, but that was with a malfunctioning development firmware where there were no shares submitted at all, so the pool kept lowering the difficulty. All implementations I know of use integer difficulty settings.

### scottwalter on 2026-03-05

Lots of pools use fractional difficulty levels, they do this to support the little, toy miners, like NerdMiner. MintSolo.com is a good example of this. They support sub 1 difficulty for pool diff to facilitate connections for MH/s type of miners. Now, will a sub 1 difficulty miner ever find a block? Not likely, but people like to try. :)

### mutatrum on 2026-03-05

> Lots of pools use fractional difficulty levels, they do this to support the little, toy miners, like NerdMiner. MintSolo.com is a good example of this. They support sub 1 difficulty for pool diff to facilitate connections for MH/s type of miners. Now, will a sub 1 difficulty miner ever find a block? Not likely, but people like to try. :)

But those miners dont run this firmware. If the minimum difficulty is 256, any fractional part is insignificant.

### scottwalter on 2026-03-05

The point is not about toy miners, the point is about ESP-Miner be able to operate with pools that offer a diverse range of pool difficulties. Canaan (e.g. Nano3s & AvalonQ), Antminer (S9, S19, T15, etc.) and generally most CGMiner 4.11.1 / ASIC based devices all support fractional difficulties. I love ESP-Miner (Bitaxe & NerdQaxe++, etc. - I own a bunch of them). By offering the same level of precision as the mainstream miners EPS-Miner will be at parity with most of the industry, that is my point, precision for the precise world of crypto mining. 

### blackmennewstyle on 2026-03-16

I'm surprised here because my stratum pool uses floating number in the `mining.set_difficulty` as you can see here: https://github.com/bitaxeorg/ESP-Miner/issues/1587#issuecomment-4027319750 and `ESP-miner` has no issue handling them 🤔

### scottwalter on 2026-03-16

ESP-Miner handles floating numbers - that was not the point. The point was, ESP-Miner, truncates/rounds them to Integer, thereby changing the precision slightly. If you run enough shares through ESP-Miner from a Stratum Host that send floats (in my case 4 decimal places) you will eventually hit one that will be low diff due to the precision differences.

Side note, I changed my pool code to handle this. For any diff >1 I just send an Integer. For pool diff <1 I send floats. This allows me to handle little NerdMiner devices and ESP-Miner (and Canaan, Antminer, etc.) without the precision issue.

### mutatrum on 2026-03-16

You can test with #1594. You're right, there's no clear protocol definition, but currently fractional parts for pool diff are tructated, which is incorrect behaviour. Even though it's unlikely for a Bitaxe to encounter this, it makes sense to properly support it.

### blackmennewstyle on 2026-03-16

> ESP-Miner handles floating numbers - that was not the point. The point was, ESP-Miner, truncates/rounds them to Integer, thereby changing the precision slightly. If you run enough shares through ESP-Miner from a Stratum Host that send floats (in my case 4 decimal places) you will eventually hit one that will be low diff due to the precision differences.
> 
> Side note, I changed my pool code to handle this. For any diff >1 I just send an Integer. For pool diff <1 I send floats. This allows me to handle little NerdMiner devices and ESP-Miner (and Canaan, Antminer, etc.) without the precision issue.

I actually understood your point. In my example you can see how far the precision goes.

And don't worry i am totally agree with you, ESP-Miner should handle floating number instead unsigned integer.

I'm just surprised to discover they were not using floating number for difficulty, that's all.
