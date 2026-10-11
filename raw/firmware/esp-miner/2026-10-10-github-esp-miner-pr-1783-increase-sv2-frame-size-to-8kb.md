# ESP-Miner PR #1783: Increase SV2 frame size to 8kb

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/1783
> Collected: 2026-10-10
> Published: 2026-06-22
> Registry ID: esp-miner

State: closed | Merged: 2026-06-24 | Author: mutatrum | +28/-9 | Labels: bug, enhancement

## Body

Allocate in PSRAM instead of stack.

Should fix this issue:

<img width="2508" height="1312" alt="image" src="https://github.com/user-attachments/assets/1b264547-3d04-4139-abba-a9585d69e85d" />

## Files changed

- `main/tasks/stratum_v2_task.c` (+28/-9) — Stratum V2 protocol task

## Key excerpts

### `main/tasks/stratum_v2_task.c` `@@ -581,6 +582,20 @@ void stratum_v2_task(void *pvParameters)`

```diff
     }
     GLOBAL_STATE->sv2_conn = conn;
 
+    uint8_t *frame_buf = heap_caps_malloc(SV2_MAX_FRAME_SIZE, MALLOC_CAP_SPIRAM);
+    uint8_t *recv_buf = heap_caps_malloc(SV2_MAX_FRAME_SIZE, MALLOC_CAP_SPIRAM);
+
+    if (!frame_buf || !recv_buf) {
+        ESP_LOGE(TAG, "Failed to allocate frame buffers");
+        free(frame_buf);
+        free(recv_buf);
+        free(conn);
+        GLOBAL_STATE->sv2_conn = NULL;
+        protocol_coordinator_notify_failure();
+        vTaskDelete(NULL);
+        return;
+    }
+
     int retry_attempts = 0;
     bool use_fallback = GLOBAL_STATE->SYSTEM_MODULE.is_using_fallback;
 
```

### `main/tasks/stratum_v2_task.c` `@@ -796,11 +813,11 @@ void stratum_v2_task(void *pvParameters)`

```diff
 
             if (channel_type == SV2_CHANNEL_EXTENDED) {
                 ESP_LOGI(TAG, "Opening extended mining channel (user=%s)", user ? user : "(empty)");
-                frame_len = sv2_build_open_extended_mining_channel(frame_buf, sizeof(frame_buf),
+                frame_len = sv2_build_open_extended_mining_channel(frame_buf, SV2_MAX_FRAME_SIZE,
                                                                     1, user ? user : "", hash_rate, 6);
             } else {
                 ESP_LOGI(TAG, "Opening standard mining channel (user=%s)", user ? user : "(empty)");
-                frame_len = sv2_build_open_standard_mining_channel(frame_buf, sizeof(frame_buf),
+                frame_len = sv2_build_open_standard_mining_channel(frame_buf, SV2_MAX_FRAME_SIZE,
                                                                     1, user ? user : "", hash_rate);
             }
 
```
