# ESP-Miner PR #1050: Refactored settings component

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/1050
> Collected: 2026-10-10
> Published: 2025-06-19
> Registry ID: esp-miner

State: closed | Merged: 2025-06-21 | Author: duckaxe | +1/-135 | Labels: cleanup

## Body

Since the `settings` component is almost useless and only acts as a wrapper for the `edit` component, the component should be cleaned up.

There isn't much left.

## Files changed

- `main/http_server/axe-os/src/app/components/settings/settings.component.ts` (+1/-104) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/components/settings/settings.component.scss` (+0/-31) — AxeOS Angular UI

## Key excerpts

### `main/http_server/axe-os/src/app/components/settings/settings.component.ts` `@@ -1,112 +1,9 @@`

```diff
-import { HttpErrorResponse } from '@angular/common/http';
 import { Component } from '@angular/core';
-import { FormBuilder, FormGroup, Validators } from '@angular/forms';
-import { ToastrService } from 'ngx-toastr';
-import { Observable, shareReplay, startWith } from 'rxjs';
-import { GithubUpdateService } from 'src/app/services/github-update.service';
-import { LoadingService } from 'src/app/services/loading.service';
-import { SystemService } from 'src/app/services/system.service';
    …
-
-  constructor(
-    private fb: FormBuilder,
-    private systemService: SystemService,
-    private toastr: ToastrService,
-    private toastrService: ToastrService,
-    private loadingService: LoadingService,
-    private githubUpdateService: GithubUpdateService
-  ) {
-    this.info$ = this.systemService.getInfo().pipe(shareReplay({refCount: true, bufferSize: 1}))
-
-
-      this.info$.pipe(this.loadingService.lockUIUntilComplete())
-      .subscribe(info => {
-        this.ASICModel = info.ASICModel;
-        this.form = this.fb.group({
-          display: [info.display, [Validators.required]],
-          flipscreen: [info.flipscreen == 1],
-          invertscreen: [info.invertscreen == 1],
-          displayTimeout: [info.displayTimeout, [Validators.required]],
[… hunk truncated: showing head + densest window of 113 diff lines]
```

### `main/http_server/axe-os/src/app/components/settings/settings.component.scss` `@@ -1,31 +0,0 @@`

```diff
-input[type="text"],
-input[type="number"],
-input[type="password"],
-input[type="range"] {
-    min-width: 250px;
-    max-width: 90%;
-}
-
-select {
-    min-width: 268px;
-    max-width: 90%;
-}
-
-.restart {
-    margin-bottom: 1.5rem;
-
-}
-
-@media only screen and (min-width:900px) {
-
-    input[type="text"],
-    input[type="password"],
-    input[type="number"],
-    input[type="range"] {
-        min-width: 500px
-    }
-
-    select {
-        min-width: 518px
-    }
-}
```
