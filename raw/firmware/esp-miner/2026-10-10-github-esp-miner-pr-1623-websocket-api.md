# ESP-Miner PR #1623: Websocket api

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/1623
> Collected: 2026-10-10
> Published: 2026-03-21
> Registry ID: esp-miner

State: closed | Merged: 2026-05-19 | Author: mutatrum | +1400/-766 | Labels: enhancement

## Body

This adds a new websocket endpoint: `/api/ws/live`. It streams partial updates in the format of the `/api/system/info` endpoint. The frontend is completely switched over to use this stream, so all fields are updated as soon as they are available. To improve this experience, the following things have also been changed:

 * There is only one websocket connection that's used on all screens, so no longer multiple calls to the info endpoint;
 * Share submit and the block header cards now have a blinking up and down arrow icon, similar as on the display (#1212);
 * Device disconnect is smoother now, and reconnects quicker when the device comes online again;
 * The hashrate registers now poll every second and have smooth color transitions, so they pulsate;
 * The vertical axis has been stabilised, the scale should now jump around a lot less;
 * Average efficiency is now calculated on 1m hashrate and current power, instead of front-end datapoints;
 * The websocket log handler is unified into the same code;
 * Switching axis on the chart is now almost instant, without redrawing the complete chart;
 * The chart also has a smarter way of handling historical data. The chart always starts filling with 1 second data, and slowly reduce datapoints to the statistics setting.

A recording of loading the dashboard while the device is still starting:

[Screencast from 2026-03-21 23-32-44.webm](https://github.com/user-attachments/assets/111eed6f-f454-4599-931b-6dc9deae2c34)

You can see the frequency ramp-up, settle into hashrate, receive work and submit shares.

## Files changed

- `main/http_server/axe-os/src/app/components/home/home.component.ts` (+310/-230) — AxeOS Angular UI
- `main/http_server/http_server.c` (+40/-292) — HTTP server + REST API handlers
- `main/http_server/system_api_json.c` (+314/-0) — HTTP server + REST API handlers
- `main/http_server/websocket.c` (+106/-118) — HTTP server + REST API handlers
- `main/http_server/websocket_api.c` (+129/-0) — HTTP server + REST API handlers
- `main/http_server/axe-os/src/app/services/live-data.service.ts` (+111/-0) — AxeOS Angular service
- `main/tasks/statistics_task.c` (+61/-22) — firmware task module
- `main/http_server/websocket_log.c` (+60/-0) — HTTP server + REST API handlers
- `main/http_server/cjson_utils.c` (+55/-0) — HTTP server + REST API handlers
- `main/http_server/axe-os/src/app/components/logs/logs.component.ts` (+31/-21) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/components/home/home.component.html` (+17/-13) — AxeOS Angular UI
- `main/http_server/cjson_utils.h` (+26/-0) — HTTP server + REST API handlers
- `main/http_server/axe-os/src/app/components/system/system.component.ts` (+10/-13) — AxeOS Angular UI
- `main/http_server/system_api_json.h` (+22/-0) — HTTP server + REST API handlers
- `main/http_server/websocket.h` (+17/-2) — HTTP server + REST API handlers
- `main/http_server/axe-os/src/app/components/edit/edit.component.ts` (+9/-5) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/layout/app.menu.component.ts` (+7/-6) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/services/loading.service.ts` (+8/-5) — AxeOS Angular service
- `readme.md` (+11/-0) — documentation
- `main/http_server/axe-os/src/app/components/pool/pool.component.ts` (+5/-5) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/components/update/update.component.ts` (+4/-6) — AxeOS Angular UI
- `main/tasks/power_management_task.c` (+1/-9) — firmware task module
- `main/http_server/axe-os/src/app/guards/ap-mode.guard.ts` (+5/-4) — AxeOS Angular UI
- `main/http_server/websocket_log.h` (+9/-0) — HTTP server + REST API handlers
- `main/http_server/axe-os/src/app/layout/app.topbar.component.ts` (+5/-3) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/components/network-edit/network.edit.component.ts` (+5/-2) — AxeOS Angular UI
- `main/http_server/websocket_api.h` (+7/-0) — HTTP server + REST API handlers
- `main/CMakeLists.txt` (+4/-0) — main app
- `main/http_server/openapi.yaml` (+4/-0) — OpenAPI spec
- `components/asic/bm1370.c` (+0/-3) — C source
- `main/main.c` (+1/-2) — main app
- `main/tasks/statistics_task.h` (+3/-0) — firmware task module
- `main/http_server/axe-os/src/app/components/edit/edit.component.html` (+1/-1) — AxeOS Angular UI
- `main/tasks/hashrate_monitor_task.c` (+1/-1) — firmware task module
- `components/asic/include/frequency_transition_bmXX.h` (+0/-1) — C header
- `components/connect/connect.c` (+0/-1) — C source
- `main/http_server/axe-os/src/app/services/system.service.ts` (+1/-0) — AxeOS Angular service
- `main/nvs_config.c` (+0/-1) — NVS settings schema/keys

## Key excerpts

### `main/http_server/websocket.c` `@@ -54,150 +74,118 @@ static esp_err_t add_client(int fd)`

```diff
     return ret;
 }
 
-static void remove_client(int fd)
+void websocket_remove_client(int fd)
 {
     if (xSemaphoreTake(clients_mutex, pdMS_TO_TICKS(100)) != pdTRUE) {
         ESP_LOGE(TAG, "Failed to acquire mutex for removing client");
    …
+    for (int i = 0; i < MAX_WEBSOCKET_CLIENTS; i++) {
+        if (clients[i].fd != -1 && (clients[i].type == type)) {
+            websocket_send_to_client(clients[i].fd, pkt);
+        }
+    }
+}
+
 void websocket_close_fn(httpd_handle_t hd, int fd)
 {
-    ESP_LOGI(TAG, "WebSocket client disconnected, fd: %d", fd);
-    remove_client(fd);
+    websocket_remove_client(fd);
     close(fd);
 }
 
-esp_err_t websocket_handler(httpd_req_t *req)
+void websocket_init(httpd_handle_t server)
 {
-    if (is_network_allowed(req) != ESP_OK) {
-        return httpd_resp_send_err(req, HTTPD_401_UNAUTHORIZED, "Unauthorized");
[… hunk truncated: showing head + densest window of 221 diff lines]
```

### `main/http_server/websocket.h` `@@ -6,13 +6,28 @@`

```diff
 #include <stdbool.h>
 #include "freertos/FreeRTOS.h"
 #include "freertos/queue.h"
+#include "freertos/task.h"
+
+void websocket_set_log_task_handle(TaskHandle_t task_handle);
 
 #define MESSAGE_QUEUE_SIZE (128)
 #define MAX_WEBSOCKET_CLIENTS (10)
 #define LOG_BUFFER_SIZE  (512 * 1024)  /* 512 KB */
 
-esp_err_t websocket_handler(httpd_req_t * req);
-void websocket_task(void * pvParameters);
+typedef enum {
+    WS_TYPE_LOGS,
+    WS_TYPE_API,
+    WS_TYPE_MAX
+} WebSocketClientType;
+
+esp_err_t websocket_add_client(int fd, WebSocketClientType type);
+void websocket_remove_client(int fd);
+void websocket_broadcast(WebSocketClientType type, httpd_ws_frame_t *pkt);
+void websocket_send_to_client(int fd, httpd_ws_frame_t *pkt);
+int websocket_get_active_client_count(WebSocketClientType type);
+void websocket_init(httpd_handle_t server);
+esp_err_t websocket_handler(httpd_req_t *req);
+
 void websocket_close_fn(httpd_handle_t hd, int sockfd);
 
 /**
```

### `main/http_server/websocket_api.c` `@@ -0,0 +1,129 @@`

```diff
+#include <string.h>
+#include <unistd.h>
+#include "freertos/FreeRTOS.h"
+#include "freertos/task.h"
+#include "esp_log.h"
+#include "esp_http_server.h"
+#include "cJSON.h"
+#include "websocket_api.h"
    …
+                if (fd == -1) {
+                    websocket_broadcast(WS_TYPE_API, &ws_pkt);
+                } else {
+                    websocket_send_to_client(fd, &ws_pkt);
+                }
+                free((void *)json_str);
+            }
+            cJSON_Delete(msg);
+        } else {
+            cJSON_Delete(diff);
+        }
+    }
+
+    return current_full;
+}
+
+void websocket_api_on_connect(int fd)
+{
+    if (GLOBAL_STATE == NULL) {
+        ESP_LOGW(TAG, "Cannot send initial state, GLOBAL_STATE not yet initialized");
[… hunk truncated: showing head + densest window of 129 diff lines]
```

### `main/http_server/http_server.c` `@@ -1688,11 +1419,20 @@ esp_err_t start_rest_server(void * pvParameters)`

```diff
         .uri = "/api/ws", 
         .method = HTTP_GET, 
         .handler = websocket_handler, 
-        .user_ctx = NULL, 
+        .user_ctx = (void *)WS_TYPE_LOGS, 
         .is_websocket = true
     };
     httpd_register_uri_handler(server, &ws);
 
+    httpd_uri_t ws_live = {
+        .uri = "/api/ws/live", 
+        .method = HTTP_GET, 
+        .handler = websocket_handler, 
+        .user_ctx = (void *)WS_TYPE_API, 
+        .is_websocket = true
+    };
+    httpd_register_uri_handler(server, &ws_live);
+
     if (!GLOBAL_STATE->filesystem_is_available) {
         /* Make default route serve Recovery */
         httpd_uri_t recovery_implicit_get_uri = {
```
