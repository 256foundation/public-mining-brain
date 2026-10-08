# bitaxeorg/ESP-Miner issue #246: Exclude pre releases of updated check

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/246
> Collected: 2026-10-07
> Published: 2024-07-02

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 246
- State: closed
- Author: WantClue
- Opened: 2024-07-02
- Closed: 2024-08-19
- Labels: enhancement

## Description

With the latest pre-release which has been removed now we had experienced the issue, that certain people updated.
In order to fight this issue of not downloading pre-releases I suggest an change to the github-update.service.ts

The change would be as followed:
```
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

interface GithubRelease {
  tag_name: string;
  prerelease: boolean;
}

@Injectable({
  providedIn: 'root'
})
export class GithubUpdateService {

  constructor(
    private httpClient: HttpClient
  ) { }

  public getReleases(): Observable<GithubRelease[]> {
    return this.httpClient.get<GithubRelease[]>(
      'https://api.github.com/repos/skot/esp-miner/releases?per_page=100'
    );
  }

  public getLatestStableRelease(): Observable<GithubRelease | null> {
    return this.getReleases().pipe(
      map(releases => releases.find(release => !release.prerelease) || null)
    );
  }
}
```

in settings.components.ts:

`this.latestRelease$ = this.githubUpdateService.getLatestStableRelease();`




## Comments

### skot on 2024-07-02

This would be amazing. I think pre-releases are a good way to roll out firmware to more experienced users who are willing to beta test new firmware.


### WantClue on 2024-08-19

Done in PR #285
