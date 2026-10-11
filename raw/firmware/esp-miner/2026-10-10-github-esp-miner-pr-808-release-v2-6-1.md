# ESP-Miner PR #808: release v2.6.1

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/808
> Collected: 2026-10-10
> Published: 2025-03-31
> Registry ID: esp-miner

State: closed | Merged: 2025-03-31 | Author: WantClue | +7970/-4389 | Labels: -

## Body

merges dev-latest into master

## Files changed

- `main/http_server/axe-os/package-lock.json` (+2890/-1968) — AxeOS web UI
- `main/power/TPS546.c` (+1086/-0) — main app
- `main/TPS546.c` (+0/-784) — main app
- `main/http_server/openapi.yaml` (+508/-0) — OpenAPI spec
- `components/asic/asic.c` (+255/-0) — C source
- `main/tasks/power_management_task.c` (+56/-197) — firmware task module
- `main/http_server/http_server.c` (+153/-59) — HTTP server + REST API handlers
- `components/asic/bm1370.c` (+78/-126) — C source
- `main/power/TPS546.h` (+191/-0) — main app
- `main/power/power.c` (+191/-0) — main app
- `components/connect/connect.c` (+148/-37) — C source
- `main/power/vcore.c` (+183/-0) — main app
- `main/thermal/EMC2103.c` (+158/-0) — thermal/fan control
- `components/asic/bm1368.c` (+31/-120) — C source
- `components/asic/bm1366.c` (+31/-97) — C source
- `main/http_server/axe-os/src/app/components/edit/edit.component.ts` (+71/-52) — AxeOS Angular UI
- `main/nvs_device.c` (+7/-103) — main app
- `main/http_server/axe-os/src/app/components/pool/pool.component.ts` (+108/-0) — AxeOS Angular UI
- `main/screen.c` (+76/-31) — display screen rendering
- `main/vcore.c` (+0/-106) — main app
- `main/self_test/self_test.c` (+65/-40) — factory self-test module
- `components/asic/common.c` (+101/-0) — C source
- `main/system.c` (+55/-43) — main app
- `main/http_server/axe-os/src/app/components/home/home.component.html` (+69/-27) — AxeOS Angular UI
- `main/tasks/stratum_task.c` (+67/-25) — firmware task module
- `components/asic/bm1397.c` (+25/-66) — C source
- `main/TPS546.h` (+0/-86) — main app
- `main/http_server/axe-os/src/app/components/edit/edit.component.html` (+13/-70) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/components/pool/pool.component.html` (+83/-0) — AxeOS Angular UI
- `main/thermal/thermal.c` (+83/-0) — thermal/fan control
- `main/http_server/axe-os/src/app/components/swarm/swarm.component.html` (+67/-12) — AxeOS Angular UI
- `main/http_server/recovery_page.h` (+0/-79) — HTTP server + REST API handlers
- `main/http_server/recovery_page.html` (+74/-0) — HTTP server + REST API handlers
- `main/http_server/axe-os/src/app/components/home/home.component.ts` (+38/-35) — AxeOS Angular UI
- `main/thermal/EMC2103.h` (+73/-0) — thermal/fan control
- `main/http_server/axe-os/src/app/components/network-edit/network.edit.component.ts` (+64/-3) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/services/dialog.service.ts` (+58/-0) — AxeOS Angular service
- `components/asic/frequency_transition_bmXX.c` (+56/-0) — C source
- `main/http_server/axe-os/src/app/services/theme.service.ts` (+54/-2) — AxeOS Angular service
- `main/main.c` (+34/-16) — main app
- `components/stratum/stratum_api.c` (+20/-27) — stratum protocol component
- `main/global_state.h` (+32/-13) — shared global state structs/flags
- `main/http_server/axe-os/src/app/components/swarm/swarm.component.ts` (+42/-2) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/components/design/theme-config.component.ts` (+34/-2) — AxeOS Angular UI
- `main/power/DS4432U.c` (+35/-0) — main app
- `.github/workflows/unittest.yml` (+34/-0) — CI workflow
- `main/http_server/axe-os/package.json` (+18/-14) — AxeOS web UI
- `components/asic/include/frequency_transition_bmXX.h` (+31/-0) — C header
- `main/http_server/axe-os/src/app/components/swarm/swarm.component.scss` (+27/-2) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/components/settings/settings.component.html` (+10/-16) — AxeOS Angular UI

… 80 more changed files (mostly ., .devcontainer, .github/workflows, components/asic, components/asic/include, components/connect/include):
`test-ci/main/unit_test_all.c`, `components/asic/include/asic.h`, `config-800x.cvs`, `main/http_server/axe-os/src/app/app-routing.module.ts`, `main/http_server/axe-os/src/app/app.module.ts`, `main/http_server/axe-os/src/app/guards/ap-mode.guard.ts`, `main/CMakeLists.txt`, `main/http_server/axe-os/src/app/components/settings/settings.component.ts`, `main/power/power.h`, `main/tasks/asic_result_task.c`, `main/thermal/thermal.h`, `components/asic/include/bm1397.h`, `main/http_server/axe-os/src/models/ISystemInfo.ts`, `components/stratum/include/stratum_api.h`, `main/i2c_bitaxe.c`, `components/asic/include/bm1368.h`, `components/connect/include/connect.h`, `main/http_server/axe-os/src/app/components/design/design.component.ts`, `main/http_server/axe-os/src/app/components/network-edit/network.edit.component.html`, `main/tasks/create_jobs_task.c`, `components/asic/include/bm1370.h`, `readme.md`, `.devcontainer/Dockerfile`, `components/asic/include/bm1366.h`, `components/asic/include/common.h`, `.github/workflows/release-beta.yml`, `.github/workflows/release-factory-beta.yml`, `.github/workflows/release-factory.yml`, `.github/workflows/release.yml`, `components/asic/include/serial.h`, `main/http_server/axe-os/src/app/components/pool/pool.component.scss`, `main/system.h`, `main/tasks/asic_task.c`, `components/asic/CMakeLists.txt`, `components/stratum/test/test_mining.c`, `config-102.cvs`, `config-201.cvs`, `config-202.cvs`, `config-203.cvs`, `config-204.cvs`, `config-205.cvs`, `config-401.cvs`, `config-402.cvs`, `config-403.cvs`, `config-601.cvs`, `flashing.md`, `main/http_server/axe-os/src/app/components/design/design.component.html`, `main/http_server/axe-os/src/app/layout/app.layout.component.html`, `main/http_server/axe-os/src/app/layout/app.layout.component.ts`, `main/http_server/axe-os/src/app/layout/app.menu.component.ts`, `main/http_server/axe-os/src/app/layout/app.topbar.component.ts`, `main/http_server/axe-os/src/app/services/github-update.service.ts`, `main/http_server/axe-os/src/app/services/system.service.ts`, `main/power/vcore.h`, `main/http_server/axe-os/angular.json`, `main/screen.h`, `SECURITY.md`, `components/asic/crc.c`, `components/stratum/mining.c`, `components/stratum/utils.c` …

## Key excerpts

### `.github/workflows/release-beta.yml` `@@ -4,6 +4,11 @@ on:`

```diff
   release:
     types: [prereleased]
 
+permissions:
+  checks: write
+  pull-requests: write
+  contents: write
+
 jobs:
   build:
     runs-on: ubuntu-latest
```

### `.github/workflows/release-factory-beta.yml` `@@ -4,6 +4,11 @@ on:`

```diff
   release:
     types: [prereleased]
 
+permissions:
+  checks: write
+  pull-requests: write
+  contents: write
+
 jobs:
   build:
     runs-on: ubuntu-latest
```

### `.github/workflows/release-factory.yml` `@@ -4,6 +4,11 @@ on:`

```diff
   release:
     types: [released]
 
+permissions:
+  checks: write
+  pull-requests: write
+  contents: write
+
 jobs:
   build:
     runs-on: ubuntu-latest
```

### `.github/workflows/release.yml` `@@ -4,6 +4,11 @@ on:`

```diff
   release:
     types: [released]
 
+permissions:
+  checks: write
+  pull-requests: write
+  contents: write
+
 jobs:
   build:
     runs-on: ubuntu-latest
```
