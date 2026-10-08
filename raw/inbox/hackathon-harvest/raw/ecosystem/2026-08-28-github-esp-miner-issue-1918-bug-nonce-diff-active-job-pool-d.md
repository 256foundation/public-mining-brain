# bitaxeorg/ESP-Miner issue #1918: Bug: nonce_diff >= active_job->pool_diff does not handle pool_diff == 0

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1918
> Collected: 2026-10-07
> Published: 2026-08-28

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1918
- State: closed
- Author: seby1302
- Opened: 2026-08-28
- Closed: 2026-09-09
- Labels: none

## Description

In asic_result.c, the share submission check currently uses:

`if (nonce_diff >= active_job->pool_diff)
`
without checking whether active_job->pool_diff is actually valid.

When pool_diff == 0 (e.g. briefly during job initialization), every positive nonce_diff satisfies the condition:

`nonce_diff >= 0
`
This can cause the miner to submit large numbers of low-difficulty shares before the actual pool difficulty has been received, potentially resulting in unnecessary share spam.

A safer check would be:

`if (active_job->pool_diff > 0.0 &&  nonce_diff >= active_job->pool_diff)`

Optionally, a separate high-difficulty fallback could be used to avoid losing an exceptionally good share while pool_diff is still unavailable.

This appears to be an initialization/edge-case issue in the share submission logic.
Example:


```
uint32_t version_bits = asic_result->rolled_version ^ active_job->version;
		bool submit_share = false;
		
        if(active_job->pool_diff > 0.0 && nonce_diff >= active_job->pool_diff)
        {
			submit_share = true;
        }
		else if (nonce_diff >= 1e6)
		{
			submit_share = true; //Fallback
		}
		
		
		if (submit_share)
		{
			 if (GLOBAL_STATE->stratum_protocol == STRATUM_PROTOCOL_V2) 
			 {
                // SV2: submit with binary protocol
                int ret;
                uint32_t sv2_job_id = (uint32_t)strtoul(active_job->jobid, NULL, 10);

                if (stratum_v2_is_extended_channel(GLOBAL_STATE)) {
                    sv2_conn_t *conn = GLOBAL_STATE->sv2_conn;
.....
......
```
