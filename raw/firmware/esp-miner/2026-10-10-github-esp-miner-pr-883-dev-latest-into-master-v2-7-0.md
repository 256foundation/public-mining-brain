# ESP-Miner PR #883: Dev latest into master v2.7.0

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/883
> Collected: 2026-10-10
> Published: 2025-05-02
> Registry ID: esp-miner

State: closed | Merged: 2025-05-02 | Author: WantClue | +2175/-1510 | Labels: -

## Body

(no body)

## Files changed

- `main/http_server/axe-os/package-lock.json` (+709/-784) — AxeOS web UI
- `main/http_server/axe-os/src/app/components/edit/edit.component.ts` (+98/-145) — AxeOS Angular UI
- `components/connect/connect.c` (+140/-59) — C source
- `main/thermal/PID.c` (+155/-0) — thermal/fan control
- `main/http_server/axe-os/api/system/asic_settings.c` (+147/-0) — AxeOS web UI
- `main/screen.c` (+71/-54) — display screen rendering
- `main/http_server/axe-os/src/app/components/home/home.component.html` (+42/-51) — AxeOS Angular UI
- `main/main.c` (+11/-66) — main app
- `main/http_server/axe-os/src/app/components/home/home.component.ts` (+36/-36) — AxeOS Angular UI
- `main/http_server/openapi.yaml` (+59/-10) — OpenAPI spec
- `main/tasks/power_management_task.c` (+32/-36) — firmware task module
- `main/thermal/PID.h` (+66/-0) — thermal/fan control
- `main/http_server/axe-os/src/app/components/swarm/swarm.component.scss` (+39/-13) — AxeOS Angular UI
- `main/logo.c` (+43/-4) — main app
- `main/http_server/axe-os/src/app/services/pools/ck-pool.service.ts` (+45/-0) — AxeOS Angular service
- `main/http_server/axe-os/src/app/services/quicklink.service.ts` (+42/-0) — AxeOS Angular service
- `main/nvs_config.c` (+37/-0) — NVS settings schema/keys
- `main/http_server/axe-os/src/app/components/design/theme-config.component.ts` (+24/-7) — AxeOS Angular UI
- `main/http_server/axe-os/src/assets/share-rejection-explanations.json` (+31/-0) — AxeOS web UI
- `components/connect/include/connect.h` (+5/-25) — C header
- `main/http_server/axe-os/src/app/services/share-rejection-explanation.service.spec.ts` (+30/-0) — AxeOS Angular service
- `components/asic/bm1397.c` (+14/-14) — C source
- `main/display.c` (+26/-2) — OLED/display rendering
- `main/http_server/http_server.c` (+23/-5) — HTTP server + REST API handlers
- `main/http_server/axe-os/src/app/components/edit/edit.component.html` (+17/-7) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/services/system.service.ts` (+23/-1) — AxeOS Angular service
- `main/system.c` (+7/-17) — main app
- `main/http_server/axe-os/src/app/layout/service/app.layout.service.ts` (+0/-23) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/components/design/design-component.scss` (+21/-0) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/services/share-rejection-explanation.service.ts` (+19/-0) — AxeOS Angular service
- `main/power/power.c` (+13/-6) — main app
- `main/thermal/EMC2101.c` (+14/-3) — thermal/fan control
- `components/asic/include/bm1397.h` (+2/-14) — C header
- `main/screen.h` (+0/-16) — display screen rendering
- `main/http_server/axe-os/add-pool.md` (+14/-0) — AxeOS web UI
- `main/http_server/axe-os/src/app/components/settings/settings.component.html` (+8/-6) — AxeOS Angular UI
- `main/http_server/axe-os/api/system/asic_settings.h` (+13/-0) — AxeOS web UI
- `main/tasks/stratum_task.c` (+10/-2) — firmware task module
- `main/http_server/axe-os/src/app/components/swarm/swarm.component.html` (+5/-4) — AxeOS Angular UI
- `main/thermal/EMC2103.c` (+3/-6) — thermal/fan control
- `main/http_server/axe-os/src/app/components/settings/settings.component.ts` (+5/-3) — AxeOS Angular UI
- `main/self_test/self_test.c` (+6/-2) — factory self-test module
- `main/thermal/thermal.c` (+4/-4) — thermal/fan control
- `components/asic/include/bm1370.h` (+1/-6) — C header
- `main/global_state.h` (+2/-5) — shared global state structs/flags
- `.github/workflows/release-factory-beta.yml` (+3/-3) — CI workflow
- `.github/workflows/release-factory.yml` (+3/-3) — CI workflow
- `components/asic/include/serial.h` (+6/-0) — C header
- `main/http_server/theme_api.c` (+0/-6) — HTTP server + REST API handlers
- `main/nvs_config.h` (+4/-2) — NVS settings schema/keys

… 44 more changed files (mostly ., .devcontainer, .github/workflows, components/asic, components/asic/include, components/asic/test):
`main/nvs_device.c`, `components/asic/include/bm1366.h`, `components/asic/include/bm1368.h`, `components/connect/CMakeLists.txt`, `.github/workflows/build.yml`, `.github/workflows/release-beta.yml`, `.github/workflows/release.yml`, `.gitignore`, `components/asic/serial.c`, `main/http_server/axe-os/package.json`, `main/http_server/axe-os/src/app/components/pool/pool.component.ts`, `main/http_server/axe-os/src/app/layout/styles/layout/_content.scss`, `main/http_server/axe-os/src/app/layout/styles/layout/_utils.scss`, `main/http_server/axe-os/tsconfig.json`, `main/main.h`, `main/CMakeLists.txt`, `main/http_server/axe-os/src/models/ISystemInfo.ts`, `.devcontainer/Dockerfile`, `.github/workflows/unittest.yml`, `components/dns_server/dns_server.c`, `main/http_server/axe-os/src/app/components/logs/logs.component.html`, `main/http_server/axe-os/src/app/components/pool/pool.component.html`, `main/http_server/axe-os/src/app/services/theme.service.ts`, `main/thermal/EMC2101.h`, `main/thermal/EMC2103.h`, `main/thermal/thermal.h`, `components/asic/test/test_job_command.c`, `config-102.cvs`, `config-201.cvs`, `config-202.cvs`, `config-203.cvs`, `config-204.cvs`, `config-205.cvs`, `config-401.cvs`, `config-402.cvs`, `config-403.cvs`, `config-601.cvs`, `config-602.cvs`, `config-800x.cvs`, `config.cvs.example`, `main/display.h`, `main/power/vcore.c`, `main/tasks/asic_result_task.c`, `main/tasks/asic_task.c`

## Key excerpts

### `.github/workflows/release-factory-beta.yml` `@@ -34,14 +34,14 @@ jobs:`

```diff
       - name: esp-idf build
         uses: espressif/esp-idf-ci-action@v1
         with:
-          esp_idf_version: v5.4
+          esp_idf_version: v5.4.1
           target: esp32s3
           command: GITHUB_ACTIONS="true" idf.py build
           path: '.'
       - name: "esp-idf build factory config for ${{ matrix.build_type }}"
         uses: espressif/esp-idf-ci-action@v1
         with:
-          esp_idf_version: v5.4
+          esp_idf_version: v5.4.1
           target: esp32s3
           command: /opt/esp/idf/components/nvs_flash/nvs_partition_generator/nvs_partition_gen.py generate config-${{ matrix.build_type }}.cvs config.bin 0x6000
           path: '.'
```

### `.github/workflows/release-factory.yml` `@@ -34,14 +34,14 @@ jobs:`

```diff
       - name: esp-idf build
         uses: espressif/esp-idf-ci-action@v1
         with:
-          esp_idf_version: v5.4
+          esp_idf_version: v5.4.1
           target: esp32s3
           command: GITHUB_ACTIONS="true" idf.py build
           path: '.'
       - name: "esp-idf build factory config for ${{ matrix.build_type }}"
         uses: espressif/esp-idf-ci-action@v1
         with:
-          esp_idf_version: v5.4
+          esp_idf_version: v5.4.1
           target: esp32s3
           command: /opt/esp/idf/components/nvs_flash/nvs_partition_generator/nvs_partition_gen.py generate config-${{ matrix.build_type }}.cvs config.bin 0x6000
           path: '.'
```

### `.github/workflows/release-beta.yml` `@@ -20,7 +20,7 @@ jobs:`

```diff
     - name: Setup Node.js
       uses: actions/setup-node@v4
       with:
-        node-version: '22.12.0'
+        node-version: '22.15.0'
     - name: Build web dist
       working-directory: ./main/http_server/axe-os
       run: |
```

### `.github/workflows/release.yml` `@@ -20,7 +20,7 @@ jobs:`

```diff
     - name: Setup Node.js
       uses: actions/setup-node@v4
       with:
-        node-version: '22.12.0'
+        node-version: '22.15.0'
     - name: Build web dist
       working-directory: ./main/http_server/axe-os
       run: |
```
