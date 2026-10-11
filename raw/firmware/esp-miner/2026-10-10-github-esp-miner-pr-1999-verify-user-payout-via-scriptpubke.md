# ESP-Miner PR #1999: Verify user payout via scriptPubKey and handle account based pools

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/1999
> Collected: 2026-10-10
> Published: 2026-09-25
> Registry ID: esp-miner

State: open | Merged: no | Author: mutatrum | +1245/-78 | Labels: enhancement

## Body

This PR flips the user payout address verification. Instead of converting coinbase tx outputs to addresses and comparing this against the user field of the pool settings, this tries to find valid addresses in the user field, and converts these to `scriptPubKey`. This has several advantages:

 * Comparison on scriptPubKey is a cheap `memcpy`. Instead of having to convert every coinbase tx output an address on every new mining job, this conversion only needs to happen once;
 * If there's no address found in the user field, it disables the warning. On account based pools the user is not expected to have a direct payout;
 * It can detect network, something that was not possible in the old system. The network is kept to make it possible to still visualise payouts;
 * It only converts coinbase tx outputs back to addresses for the ones that are shown in the dashboard, based on the initially detected network;
 * It should also work with the sri template system, see #1993.

Note: if we remove the display of addresses, we can eliminate about 150 lines of code. But I kinda like that bit on the dashboard. It allows the user to actually verify the address, instead of having to trust the firmware saying they have a payout.

## Files changed

- `components/stratum/test/test_coinbase_decoder.c` (+626/-1) — stratum protocol component
- `components/stratum/coinbase_decoder.c` (+337/-19) — stratum protocol component
- `main/http_server/axe-os/src/app/components/home/home.component.spec.ts` (+97/-0) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/pipes/address.pipe.spec.ts` (+66/-1) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/components/home/home.component.ts` (+10/-41) — AxeOS Angular UI
- `components/stratum/include/coinbase_decoder.h` (+50/-0) — stratum protocol component
- `main/http_server/axe-os/src/app/pipes/address.pipe.ts` (+38/-9) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/components/home/home.component.html` (+5/-5) — AxeOS Angular UI
- `main/http_server/openapi.yaml` (+9/-0) — OpenAPI spec
- `main/system.c` (+4/-0) — main app
- `main/http_server/system_api_json.c` (+1/-2) — HTTP server + REST API handlers
- `main/global_state.h` (+1/-0) — shared global state structs/flags
- `main/http_server/axe-os/src/app/services/system.service.ts` (+1/-0) — AxeOS Angular service

## Key excerpts

### `main/http_server/axe-os/src/app/components/home/home.component.spec.ts` `@@ -258,6 +259,33 @@ describe('HomeComponent', () => {`

```diff
     expect(component.messages.some(message => message.type === 'FREQUENCY_LOW')).toBeFalse();
   });
 
+  it('handles mining reward messages using coinbasePayoutStatus', () => {
+    const error = { duration: 0, startTime: null };
+    const baseInfo: ISystemInfo = {
+      ...mockSystemInfo,
+      coinbaseOutputs: [{ address: 'bc1qother', value: 50000 }],
    …
+      coinbaseValueTotalSatoshis: 50000,
+      coinbaseValueUserSatoshis: 0,
+    };
+
+    // When payout status is not_found and share warning is enabled, alert NO_MINING_REWARD
+    component.activePoolShareWarning = true;
+    component.handleSystemMessages({ ...baseInfo, coinbasePayoutStatus: 'not_found' }, error);
+    expect(component.messages.some(message => message.type === 'NO_MINING_REWARD')).toBeTrue();
+
+    // When payout status is not_applicable (account pool), NO_MINING_REWARD is not shown
+    component.handleSystemMessages({ ...baseInfo, coinbasePayoutStatus: 'not_applicable' }, error);
+    expect(component.messages.some(message => message.type === 'NO_MINING_REWARD')).toBeFalse();
+
+    // When payout status is verified, NO_MINING_REWARD is not shown
+    component.handleSystemMessages({
+      ...baseInfo,
+      coinbaseValueUserSatoshis: 50000,
+      coinbasePayoutStatus: 'verified'
+    }, error);
+    expect(component.messages.some(message => message.type === 'NO_MINING_REWARD')).toBeFalse();
[… hunk truncated: showing head + densest window of 33 diff lines]
```

### `components/stratum/include/coinbase_decoder.h` `@@ -22,6 +24,33 @@`

```diff
 #define OP_HASH160      0xa9
 #define OP_CHECKSIG     0xac
 
+/**
+ * @brief Convert user address string (address, address.worker, or hex script)
+ *        into canonical binary scriptPubKey bytes.
+ * 
+ * @param user User string from pool config (e.g. "bc1q...axe1", "1A1z..._w1", "0014...")
    …
+ * @param script_out Buffer to store binary scriptPubKey (min MAX_SCRIPTPUBKEY_LEN bytes)
+ * @param max_out Maximum capacity of script_out
+ * @return size_t Length of parsed scriptPubKey in bytes, or 0 if user is not a valid address/script
+ */
+size_t coinbase_address_to_scriptpubkey(const char *user, uint8_t *script_out, size_t max_out);
+
+/**
+ * @brief Parse user configuration string (which may contain up to MAX_USER_ADDRESSES
+ *        comma- or semicolon-separated addresses, each with optional worker suffix)
+ *        into canonical binary scriptPubKeys.
+ *
+ * @param user User string from pool config (e.g. "addr1.w1,addr2.w2" or "addr1")
+ * @param scripts_out 2D array [MAX_USER_ADDRESSES][MAX_SCRIPTPUBKEY_LEN]
+ * @param script_lens Array to store lengths of parsed scripts [MAX_USER_ADDRESSES]
+ * @param max_scripts Maximum number of scripts to parse (up to MAX_USER_ADDRESSES)
+ * @return int Number of successfully parsed scripts (0 to max_scripts)
+ */
+int coinbase_parse_user_scriptpubkeys(const char *user,
+                                      uint8_t scripts_out[][MAX_SCRIPTPUBKEY_LEN],
+                                      size_t script_lens[],
[… hunk truncated: showing head + densest window of 33 diff lines]
```

### `components/stratum/coinbase_decoder.c` `@@ -303,22 +595,30 @@ esp_err_t coinbase_process_miner_job(const miner_job_t *job,`

```diff
     result->user_value_satoshis = 0;
     result->others_count = 0;
     result->others_value_satoshis = 0;
+    result->payout_status = COINBASE_PAYOUT_UNKNOWN;
     result->decode_coinbase_tx = decode_coinbase_tx;
 
-    // Detect network from user address prefix for correct address encoding
     const char *bech32_hrp = "bc";
    …
     bool is_testnet = false;
-    if (user_address) {
-        if (strncmp(user_address, "bcrt1", 4) == 0) {
-            bech32_hrp = "bcrt";
-            is_testnet = true;
-        } else if (strncmp(user_address, "tb1", 3) == 0) {
-            bech32_hrp = "tb";
-            is_testnet = true;
-        } else if (user_address[0] == 'm' || user_address[0] == 'n' || user_address[0] == '2') {
-            bech32_hrp = "tb";
-            is_testnet = true;
+    int user_script_count = 0;
+
+    if (decode_coinbase_tx && user_address) {
+        if (!s_cache_valid || strcmp(user_address, s_cached_user) != 0) {
+            strncpy(s_cached_user, user_address, sizeof(s_cached_user) - 1);
+            s_cached_user[sizeof(s_cached_user) - 1] = '\0';
+
+            s_cached_script_count = coinbase_parse_user_scriptpubkeys(user_address,
+                                                                      s_cached_scripts,
[… hunk truncated: showing head + densest window of 41 diff lines]
```

### `main/http_server/openapi.yaml` `@@ -713,6 +714,14 @@ components:`

```diff
         coinbaseOthersValueSatoshis:
           type: integer
           description: Summed value in satoshis of the outputs counted in coinbaseOthersCount
+        coinbasePayoutStatus:
+          type: string
+          description: Verification status of user payout address against coinbase transaction
+          enum:
+            - verified
+            - not_found
+            - not_applicable
+            - unknown
         hashrateMonitor:
           type: object
           required:
```
