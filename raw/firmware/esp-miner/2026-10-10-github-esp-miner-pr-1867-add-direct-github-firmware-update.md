# ESP-Miner PR #1867: Add direct GitHub firmware update

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/1867
> Collected: 2026-10-10
> Published: 2026-08-10
> Registry ID: esp-miner

State: closed | Merged: no | Author: mutatrum | +921/-205 | Labels: -

## Body

(no body)

## Files changed

- `main/http_server/ota_api.c` (+610/-172) — HTTP server + REST API handlers
- `main/http_server/axe-os/src/app/components/update/update.component.ts` (+116/-5) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/components/update/update.component.html` (+79/-22) — AxeOS Angular UI
- `main/http_server/openapi.yaml` (+37/-0) — OpenAPI spec
- `main/http_server/axe-os/src/app/services/github-update.service.ts` (+17/-4) — AxeOS Angular service
- `main/nvs_config.c` (+15/-0) — NVS settings schema/keys
- `main/http_server/axe-os/src/app/utils/error-handler.ts` (+14/-0) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/services/system.service.ts` (+10/-0) — AxeOS Angular service
- `main/http_server/axe-os/src/app/layout/app.topbar.component.ts` (+7/-1) — AxeOS Angular UI
- `main/http_server/http_server.c` (+7/-1) — HTTP server + REST API handlers
- `main/http_server/ota_api.h` (+5/-0) — HTTP server + REST API handlers
- `main/CMakeLists.txt` (+2/-0) — main app
- `main/http_server/http_server.h` (+2/-0) — HTTP server + REST API handlers

## Key excerpts

### `main/http_server/ota_api.c` `@@ -384,20 +450,392 @@ esp_err_t POST_WWW_update(httpd_req_t *req)`

```diff
 
             chunks++;
             if (chunks % 4 == 0) {
-                vTaskDelay(10 / portTICK_PERIOD_MS);
+                vTaskDelay(pdMS_TO_TICKS(10));
             }
         }
     }
    …
+            free(ota_buf);
+            cleanup_github_ota_task(args, client, "Validation Error");
+            return;
+        }
+
+        snprintf(GLOBAL_STATE->SYSTEM_MODULE.firmware_update_status, 20, "Flashing (0%%)");
+        if (flash_buffer_to_ota_partition(ota_buf, content_length, ota_partition, GLOBAL_STATE) != ESP_OK) {
+            free(ota_buf);
+            cleanup_github_ota_task(args, client, "Flash Error");
+            return;
+        }
+
+        free(ota_buf);
+    } else {
+        // --- STREAMING FALLBACK PATH (PSRAM unavailable or malloc failed) ---
+        ESP_LOGI(TAG, "Starting Streaming GitHub OTA (PSRAM unavailable)");
+
+        esp_ota_handle_t ota_handle;
+        if (esp_ota_begin(ota_partition, content_length > 0 ? content_length : OTA_SIZE_UNKNOWN, &ota_handle) != ESP_OK) {
+            cleanup_github_ota_task(args, client, "Erase Error");
[… hunk truncated: showing head + densest window of 399 diff lines]
```

### `main/http_server/openapi.yaml` `@@ -1351,6 +1351,43 @@ paths:`

```diff
         '500':
           description: Internal server error
 
+  /api/system/OTA/github:
+    post:
+      summary: Update system firmware directly from GitHub
+      description: Downloads and installs firmware binary directly from an official GitHub release
+      operationId: updateFirmwareFromGithub
    …
+                url:
+                  type: string
+                  description: Optional explicit release asset URL (must be github.com/bitaxeorg/ESP-Miner)
+                tag:
+                  type: string
+                  description: Optional release tag version (e.g. v2.3.0)
+      responses:
+        '200':
+          description: Firmware update initiated
+          content:
+            application/json:
+              schema:
+                type: object
+                properties:
+                  status:
+                    type: string
+        '400':
+          description: Invalid or non-GitHub URL provided
+        '401':
+          description: Unauthorized - Client not in allowed network range
[… hunk truncated: showing head + densest window of 43 diff lines]
```

### `main/http_server/axe-os/src/app/components/update/update.component.html` `@@ -28,33 +28,87 @@ <h3>Latest Release: <button class="btn text-sm ml-2" (click)="handleReleaseCheck`

```diff
                 </ng-container>
 
                 <ng-template #afterCheck>
-                    <ng-container *ngIf="latestRelease$ | async as latestRelease">
-                        <h3>Latest Release:
-                            <a style="text-decoration: underline;" target="_blank"
-                            [href]="latestRelease.html_url">{{latestRelease.name}}</a>
-                        </h3>
    …
-
-                        <div class="text-orange-500 mb-3">Download both files for update!</div>
-
-                        <div *ngFor="let asset of latestRelease.assets">
-                            <div *ngIf="asset.name == 'esp-miner.bin'">
-                                <a style="text-decoration: underline;" target="_blank"
-                                    [href]="asset.browser_download_url">esp-miner.bin</a>
+                    <ng-container *ngIf="releases$ | async as releases; else loadingReleases">
+                        <ng-container *ngIf="releases.length > 0; else noReleases">
+                            <div class="flex items-center gap-2 mb-3">
+                                <app-checkbox
+                                    inputId="includePrereleases"
+                                    [binary]="true"
+                                    [ngModel]="includePrereleases"
+                                    (onChange)="togglePrereleases($event.checked)">
+                                </app-checkbox>
+                                <label for="includePrereleases" class="cursor-pointer text-sm font-medium">Include pre-releases (beta / RC)</label>
                             </div>
-                            <div *ngIf="asset.name == 'www.bin'">
-                                <a style="text-decoration: underline;" target="_blank"
[… hunk truncated: showing head + densest window of 109 diff lines]
```

### `main/http_server/axe-os/src/app/services/github-update.service.ts` `@@ -4,11 +4,20 @@ import { Observable } from 'rxjs';`

```diff
 import { map } from 'rxjs/operators';
 
 
-interface GithubRelease {
+export interface GithubReleaseAsset {
+  id: number;
+  name: string;
+  browser_download_url: string;
+}
+
+export interface GithubRelease {
   id: number;
   tag_name: string;
   name: string;
   prerelease: boolean;
+  html_url: string;
+  body: string;
+  assets: GithubReleaseAsset[];
 }
 
 @Injectable({
```
