# ESP-Miner PR #1890: Add BM1372/BM1373 ASIC driver support

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/1890
> Collected: 2026-10-10
> Published: 2026-08-17
> Registry ID: esp-miner

State: closed | Merged: 2026-08-22 | Author: benjamin-wilson | +630/-5 | Labels: -

## Body

## Summary

- add BM1372 and BM1373 ASIC model support
- add the BM1373 ASIC driver and register initialization
- add device and API configuration support for the new ASIC models

This is the foundation PR for the Naja Duo 1201 series. It contains no board-specific display or self-test code.

## Validation

- full ESP-IDF 6.0.2 firmware builds pass on both downstream integration branches
- `git diff --check` passes
- regular hashrate-monitor calculations are unchanged

## Files changed

- `components/asic/bm1373.c` (+549/-0) — C source
- `components/asic/include/bm1373.h` (+36/-0) — C header
- `components/asic/asic.c` (+23/-0) — C source
- `components/asic/asic_common.c` (+12/-3) — C source
- `main/device_config.h` (+6/-1) — main app
- `components/asic/serial.c` (+1/-1) — C source
- `components/asic/CMakeLists.txt` (+1/-0) — changed file
- `components/asic/include/asic_common.h` (+1/-0) — C header
- `main/http_server/openapi.yaml` (+1/-0) — OpenAPI spec

## Key excerpts

### `components/asic/include/bm1373.h` `@@ -0,0 +1,36 @@`

```diff
+#ifndef BM1373_H_
+#define BM1373_H_
+
+#include "asic_common.h"
+
+typedef struct GlobalState GlobalState;
+typedef struct bm_job bm_job;
+
    …
+{
+    uint8_t job_id;
+    uint8_t num_midstates;
+    uint8_t starting_nonce[4];
+    uint8_t nbits[4];
+    uint8_t ntime[4];
+    uint8_t merkle_root[32];
+    uint8_t prev_block_hash[32];
+    uint8_t version[4];
+} BM1373_job;
+
+uint8_t BM1373_init(GlobalState * GLOBAL_STATE);
+void BM1373_send_work(GlobalState * GLOBAL_STATE, bm_job * next_bm_job);
+void BM1373_set_version_mask(uint32_t version_mask);
+int BM1373_set_max_baud(void);
+int BM1373_set_default_baud(void);
+float BM1373_send_hash_frequency(float frequency);
+task_result * BM1373_process_work(GlobalState * GLOBAL_STATE);
+void BM1373_read_registers(void);
+void BM1373_set_nonce_space(double nonce_percent, float frequency, uint16_t asic_count, uint16_t cores);
[… hunk truncated: showing head + densest window of 36 diff lines]
```

### `components/asic/bm1373.c` `@@ -0,0 +1,549 @@`

```diff
+#include "bm1373.h"
+
+#include "crc.h"
+#include "global_state.h"
+#include "mining.h"
+#include "serial.h"
+#include "utils.h"
+
    …
+#define BM1372_SOFT_RESET_FAST 0xF00701F0
+#define BM1372_RNO_ENABLE 0xFF00C100
+#define BM1372_CRR_DISABLE 0x00000000
+#define BM1372_CLOCK_SELECT 0x00
+#define BM1372_CLOCK_DELAY_PWTH6_CCDLY2 0x5A
+#define BM1372_CORE_ENABLE 0xAA
+#define BM1372_NONCE_BIN_OVERFLOW_DISABLE 0x04
+#define BM1372_IO_DRIVER_STRENGTH_DEFAULT 0x00011111
+#define BM1372_IO_DRIVER_STRENGTH_DOMAIN_END 0x0001F111
+#define BM1372_ROSC_PAD_DISABLE 0x5AA55AA5
+#define BM1372_ANALOG_MUX_TEMPERATURE_DIODE 0x00000002
+#define BM1372_AUTO_WORK_CONFIGURATION 0x00000000
+#define BM1372_FAST_UART_3M 0x80000000
+
+#define BM1372_ASIC_BAUD 3000000
+#define BM1372_WRITE_RETRIES 3
+#define BM1372_WRITE_RETRY_DELAY_MS 50
+#define BM1372_INIT_STEP_DELAY_MS 10
+#define BM1372_FAST_RESET_DELAY_MS 20
+#define BM1372_SET_ADDRESS_STRIDE 0x10
[… hunk truncated: showing head + densest window of 549 diff lines]
```

### `components/asic/CMakeLists.txt` `@@ -1,5 +1,6 @@`

```diff
 idf_component_register(
 SRCS 
+    "bm1373.c"
     "bm1370.c"
     "bm1368.c"
     "bm1366.c"
```

### `components/asic/include/asic_common.h` `@@ -42,6 +42,7 @@ int _next_power_of_two(int num);`

```diff
 void clear_asic_chain_error(void);
 const char *get_asic_chain_error(void);
 int count_asic_chips(uint16_t asic_count, uint16_t chip_id, int chip_id_response_length);
+int count_asic_chips_with_id_alias(uint16_t asic_count, uint16_t chip_id, uint16_t chip_id_alias, int chip_id_response_length);
 esp_err_t receive_work(uint8_t * buffer, int buffer_size, uint64_t *out_timestamp_us);
 void get_difficulty_mask(double difficulty, uint8_t *job_difficulty_mask);
 double calculate_bm_timeout_ms(float frequency_mhz, size_t asic_count, size_t small_cores, size_t cores, size_t version_size, float timeout_percent, double default_time_ms);
```
