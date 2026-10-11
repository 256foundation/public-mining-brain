# ESP-Miner PR #2001: Firmware checksum integrity

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/2001
> Collected: 2026-10-10
> Published: 2026-09-26
> Registry ID: esp-miner

State: closed | Merged: 2026-10-04 | Author: WantClue | +417/-25 | Labels: enhancement

## Body

<img width="516" height="347" alt="image" src="https://github.com/user-attachments/assets/2999d5d9-be88-47aa-84aa-d88245fdf7c6" />

## Files changed

- `main/firmware_checksum.c` (+92/-0) — main app
- `main/http_server/axe-os/src/app/components/update/update.component.ts` (+64/-4) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/components/update/update.component.html` (+47/-16) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/components/update/update.component.spec.ts` (+55/-1) — AxeOS Angular UI
- `main/http_server/http_server.c` (+47/-1) — HTTP server + REST API handlers
- `main/http_server/openapi.yaml` (+40/-0) — OpenAPI spec
- `main/http_server/axe-os/src/app/services/system.service.ts` (+19/-1) — AxeOS Angular service
- `main/firmware_checksum.h` (+19/-0) — main app
- `main/http_server/axe-os/src/app/services/github-update.service.ts` (+16/-1) — AxeOS Angular service
- `.github/workflows/release.yml` (+15/-1) — CI workflow
- `main/CMakeLists.txt` (+3/-0) — main app

## Key excerpts

### `main/http_server/http_server.c` `@@ -1563,6 +1565,41 @@ static esp_err_t POST_system_boot(httpd_req_t *req)`

```diff
     return send_res;
 }
 
+static esp_err_t GET_system_firmware_checksum(httpd_req_t *req)
+{
+    if (is_network_allowed(req) != ESP_OK) {
+        return httpd_resp_send_err(req, HTTPD_401_UNAUTHORIZED, "Unauthorized");
+    }
    …
+    httpd_resp_set_type(req, "application/json");
+
+    // Set CORS headers
+    if (set_cors_headers(req) != ESP_OK) {
+        httpd_resp_send_500(req);
+        return ESP_OK;
+    }
+
+    const esp_partition_t *running = esp_ota_get_running_partition();
+    const char *sha256_hex = NULL;
+    uint32_t image_len = 0;
+    if (running == NULL || firmware_checksum_get_running(&sha256_hex, &image_len) != ESP_OK) {
+        return httpd_resp_send_err(req, HTTPD_500_INTERNAL_SERVER_ERROR, "Failed to compute firmware checksum");
+    }
+
+    const esp_app_desc_t *app_desc = esp_app_get_description();
+
+    cJSON *root = cJSON_CreateObject();
+    cJSON_AddStringToObject(root, "partition", running->label);
+    cJSON_AddStringToObject(root, "version", app_desc->version);
[… hunk truncated: showing head + densest window of 41 diff lines]
```

### `main/firmware_checksum.c` `@@ -0,0 +1,92 @@`

```diff
+#include <stdio.h>
+#include <stdlib.h>
+#include <sys/param.h>
+#include "esp_log.h"
+#include "esp_ota_ops.h"
+#include "esp_partition.h"
+#include "esp_image_format.h"
+#include "psa/crypto.h"
    …
+#include "firmware_checksum.h"
+
+#define HASH_CHUNK_SIZE 4096
+#define SHA256_LEN 32
+
+static const char *TAG = "firmware_checksum";
+
+static char cached_sha256_hex[SHA256_LEN * 2 + 1] = {0};
+static uint32_t cached_image_len = 0;
+
+static esp_err_t compute_app_sha256(const esp_partition_t *partition, uint8_t digest[SHA256_LEN], uint32_t *image_len)
+{
+    esp_partition_pos_t part_pos = {
+        .offset = partition->address,
+        .size = partition->size,
+    };
+    esp_image_metadata_t metadata;
+    esp_err_t err = esp_image_get_metadata(&part_pos, &metadata);
+    if (err != ESP_OK) {
+        return err;
[… hunk truncated: showing head + densest window of 92 diff lines]
```

### `main/http_server/axe-os/src/app/components/update/update.component.spec.ts` `@@ -77,6 +80,57 @@ describe('UpdateComponent', () => {`

```diff
       expect(msg).toBe('Write Error (Device: 192.168.1.10)');
     });
   });
-});
 
+  describe('verifyFirmware', () => {
+    const sha = 'ab'.repeat(32);
+    let githubService: GithubUpdateService;
    …
+
+    const release = (digest?: string | null): GithubRelease => ({
+      id: 1,
+      tag_name: 'v2.13.0',
+      name: 'v2.13.0',
+      html_url: 'https://github.com/bitaxeorg/esp-miner/releases/tag/v2.13.0',
+      prerelease: false,
+      assets: [{ name: 'esp-miner.bin', browser_download_url: '', digest }]
+    });
+
+    beforeEach(() => {
+      spyOn(TestBed.inject(SystemApiService), 'getFirmwareChecksum').and.returnValue(
+        of({ partition: 'ota_0', version: 'v2.13.0', size: 1024, sha256: sha })
+      );
+      githubService = TestBed.inject(GithubUpdateService);
+    });
+
+    it('should report a match when the release digest equals the device checksum', () => {
+      const spy = spyOn(githubService, 'getReleaseByTag').and.returnValue(of(release(`sha256:${sha.toUpperCase()}`)));
+      component.verifyFirmware();
[… hunk truncated: showing head + densest window of 58 diff lines]
```

### `main/http_server/axe-os/src/app/components/update/update.component.html` `@@ -49,6 +33,53 @@ <h3>Latest Release:`

```diff
           }
         }
 
+        <div class="mt-4 pt-3 border-t border-white/10">
+          <h5 class="mb-2">Firmware Integrity: <button class="btn text-sm ml-2" [disabled]="verifyStatus === 'checking'" (click)="handleFirmwareVerify()">Verify</button></h5>
+          <small class="text-secondary block">Compares the SHA-256 of the running firmware with the official esp-miner.bin of the same release.</small>
+
+          @switch (verifyStatus) {
    …
+            @case ('checking') {
+              <div class="mt-2">Computing checksum...</div>
+            }
+            @case ('match') {
+              <div class="mt-2 text-green-500 flex items-center gap-2"><i class="pi pi-check-circle"></i>Matches the official <a class="underline" target="_blank" [href]="verifyReleaseUrl">{{ deviceChecksum?.version }}</a> release</div>
+            }
+            @case ('mismatch') {
+              <div class="mt-2 text-red-500 flex items-center gap-2"><i class="pi pi-times-circle"></i>Does not match the official <a class="underline" target="_blank" [href]="verifyReleaseUrl">{{ deviceChecksum?.version }}</a> release</div>
+            }
+            @case ('no-release') {
+              <div class="mt-2 text-orange-500">No official release found for {{ deviceChecksum?.version }}. This is likely a development or custom build.</div>
+            }
+            @case ('no-digest') {
+              <div class="mt-2 text-orange-500">The {{ deviceChecksum?.version }} release does not provide a checksum for esp-miner.bin.</div>
+            }
+          }
+
+          @if (deviceChecksum) {
+            <div class="mt-2 text-xs font-mono break-all">
+              <div><span class="text-secondary">Device ({{ deviceChecksum.partition }}):</span> {{ deviceChecksum.sha256 }}</div>
[… hunk truncated: showing head + densest window of 53 diff lines]
```
