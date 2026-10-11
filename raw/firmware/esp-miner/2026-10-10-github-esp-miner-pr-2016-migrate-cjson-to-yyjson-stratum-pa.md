# ESP-Miner PR #2016: Migrate cJSON to yyjson (stratum parsing and statistics)

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/2016
> Collected: 2026-10-10
> Published: 2026-10-04
> Registry ID: esp-miner

State: closed | Merged: 2026-10-08 | Author: mutatrum | +362/-211 | Labels: -

## Body

This PR migrates part of the API from cJSON to yyjson. Reason for this is performance, cJSON allocates memory _per field_ so with 720 points this is thousands of allocations. In contract, yyjson has one memory pool, so no heap churn. Not everything has been converted yet, this is the first step.

Some metrics. I also experimented with a no-library version of the statistics endpoint, just `sprintf` calls , that's a little bit faster even but unwieldy in code. :

|  | Stock cJSON | sprintf | yyjson |
| :--- | :--- | :--- | :--- |
| Time to First Byte (TTFB) | ~316 ms | ~36 ms | ~61 ms |
| Total Response Time | ~357 - 400 ms | ~61 - 75 ms | ~105 - 131 ms |
| Transferred Payload Size | 56.8 KB | 38.0 KB | 37.8 KB |

Specifically for the statistics it uses ``YYJSON_WRITE_FP_TO_FIXED(2)` which cuts down on the payload size. As these points are only used for the charts, more precision is not needed anyways.

This is very noticaly on first load of the dashboard, and on return to an open dashboard to fill in any gaps.

## Files changed

- `components/stratum/stratum_api.c` (+184/-153) — stratum protocol component
- `main/http_server/http_server.c` (+77/-55) — HTTP server + REST API handlers
- `components/yyjson/yyjson_psram.c` (+41/-0) — C source
- `components/stratum/test/test_stratum_json.c` (+27/-1) — stratum protocol component
- `components/yyjson/include/yyjson_psram.h` (+17/-0) — C header
- `components/yyjson/CMakeLists.txt` (+9/-0) — changed file
- `.gitmodules` (+3/-0) — changed file
- `readme.md` (+1/-1) — documentation
- `components/stratum/CMakeLists.txt` (+1/-0) — stratum protocol component
- `components/stratum/idf_component.yml` (+0/-1) — stratum protocol component
- `components/yyjson/yyjson` (+1/-0) — changed file
- `main/CMakeLists.txt` (+1/-0) — main app

## Key excerpts

### `components/stratum/stratum_api.c` `@@ -705,48 +715,69 @@ bool STRATUM_V1_parse(StratumApiV1Message *message, const char *stratum_json, mi`

```diff
     ESP_LOGD(TAG, "rx: %.*s%s", (int)MIN(json_length, 512U), stratum_json,
              json_length > 512U ? "..." : "");
 
-    cJSON *json = cJSON_ParseWithOpts(stratum_json, NULL, true);
-    if (!cJSON_IsObject(json)) {
+    yyjson_doc *doc = yyjson_read(stratum_json, json_length, YYJSON_READ_NOFLAG);
+    if (!doc) {
+        ESP_LOGE(TAG, "JSON-RPC message is not valid JSON: %s", stratum_json);
    …
-            id_json->valuedouble != (double)id_json->valueint) {
+    yyjson_val *id_json = yyjson_obj_get(root, "id");
+    if (id_json && !yyjson_is_null(id_json)) {
+        if (!yyjson_is_int(id_json)) {
             ESP_LOGE(TAG, "Invalid JSON-RPC message id");
-            cJSON_Delete(json);
+            yyjson_doc_free(doc);
             return false;
         }
-        message->message_id = id_json->valueint;
+        if (yyjson_is_sint(id_json)) {
+            int64_t sval = yyjson_get_sint(id_json);
+            if (sval < 0 || sval > INT_MAX) {
+                ESP_LOGE(TAG, "Invalid JSON-RPC message id");
+                yyjson_doc_free(doc);
+                return false;
+            }
+            message->message_id = (int)sval;
+        } else if (yyjson_is_uint(id_json)) {
+            uint64_t uval = yyjson_get_uint(id_json);
[… hunk truncated: showing head + densest window of 85 diff lines]
```

### `main/http_server/http_server.c` `@@ -1648,66 +1650,86 @@ static esp_err_t GET_system_statistics(httpd_req_t * req)`

```diff
         }
     }
 
-    // Create object for statistics
-    cJSON * root = cJSON_CreateObject();
-    cJSON_AddNumberToObject(root, "currentTimestamp", (esp_timer_get_time() / 1000));
-
-    cJSON * labelArray = cJSON_CreateArray();
    …
+    yyjson_mut_val *labelArray = yyjson_mut_obj_add_arr(doc, root, "labels");
+    if (dataSelection[SRC_HASHRATE]) { yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_HASHRATE); }
+    if (dataSelection[SRC_HASHRATE_1m]) { yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_HASHRATE_1m); }
+    if (dataSelection[SRC_HASHRATE_10m]) { yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_HASHRATE_10m); }
+    if (dataSelection[SRC_HASHRATE_1h]) { yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_HASHRATE_1h); }
+    if (dataSelection[SRC_ERROR_PERCENTAGE]) { yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_ERROR_PERCENTAGE); }
+    if (dataSelection[SRC_ASIC_TEMP]) { yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_ASIC_TEMP); }
+    if (dataSelection[SRC_ASIC_TEMP2]) { yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_ASIC_TEMP2); }
+    if (dataSelection[SRC_VR_TEMP]) { yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_VR_TEMP); }
+    if (dataSelection[SRC_ASIC_VOLTAGE]) { yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_ASIC_VOLTAGE); }
+    if (dataSelection[SRC_VOLTAGE]) { yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_VOLTAGE); }
+    if (dataSelection[SRC_POWER]) { yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_POWER); }
+    if (dataSelection[SRC_CURRENT]) { yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_CURRENT); }
+    if (dataSelection[SRC_FAN_SPEED]) { yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_FAN_SPEED); }
+    if (dataSelection[SRC_FAN_RPM]) { yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_FAN_RPM); }
+    if (dataSelection[SRC_FAN2_RPM]) { yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_FAN2_RPM); }
+    if (dataSelection[SRC_WIFI_RSSI]) { yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_WIFI_RSSI); }
+    if (dataSelection[SRC_FREE_HEAP]) { yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_FREE_HEAP); }
+    if (dataSelection[SRC_RESPONSE_TIME]) { yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_RESPONSE_TIME); }
+    yyjson_mut_arr_add_str(doc, labelArray, STATS_LABEL_TIMESTAMP);
[… hunk truncated: showing head + densest window of 140 diff lines]
```

### `components/yyjson/yyjson_psram.c` `@@ -0,0 +1,41 @@`

```diff
+#include "yyjson_psram.h"
+#include <esp_heap_caps.h>
+
+static void *psram_malloc(void *ctx, size_t size)
+{
+    return heap_caps_malloc(size, MALLOC_CAP_SPIRAM | MALLOC_CAP_8BIT);
+}
+
    …
+}
+
+static void psram_free(void *ctx, void *ptr)
+{
+    heap_caps_free(ptr);
+}
+
+static const yyjson_alc s_yyjson_psram_alc = {
+    .malloc = psram_malloc,
+    .realloc = psram_realloc,
+    .free = psram_free,
+    .ctx = NULL,
+};
+
+const yyjson_alc *yyjson_psram_alc(void)
+{
+    return &s_yyjson_psram_alc;
+}
+
+void yyjson_alc_free(const yyjson_alc *alc, void *ptr)
[… hunk truncated: showing head + densest window of 41 diff lines]
```

### `components/yyjson/include/yyjson_psram.h` `@@ -0,0 +1,17 @@`

```diff
+#ifndef YYJSON_PSRAM_H
+#define YYJSON_PSRAM_H
+
+#include "yyjson.h"
+
+/**
+ * Returns a pointer to a yyjson_alc configured to allocate from external PSRAM (SPIRAM).
+ */
+const yyjson_alc *yyjson_psram_alc(void);
+
+/**
+ * Convenience helper to free memory allocated by a yyjson_alc (e.g. from yyjson_mut_write_opts).
+ * Safely calls alc->free(alc->ctx, ptr) if alc and alc->free are set, otherwise calls standard free(ptr).
+ */
+void yyjson_alc_free(const yyjson_alc *alc, void *ptr);
+
+#endif // YYJSON_PSRAM_H
```
