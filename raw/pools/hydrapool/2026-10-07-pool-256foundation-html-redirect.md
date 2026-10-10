# pool.256foundation.org HTML is a 301, not the dashboard

> Source: https://pool.256foundation.org/ fetched 2026-10-07T21:40:46Z without following redirects; https://dash.256f.org/ fetched the same second
> Collected: 2026-10-07
> Published: 2026-10-07

Correction to `raw/hydrapool/2026-10-07-pool-256foundation-operator.md`. That file's Prometheus queries still stand. Its HTML paragraph does not.

A no-follow `GET https://pool.256foundation.org/` is HTTP 301. Headers: `server: nginx/1.24.0 (Ubuntu)`, `content-type: text/html`, `content-length: 178`, `location: https://dash.256f.org/`. Body is the stock nginx page:

```
<html>
<head><title>301 Moved Permanently</title></head>
<body>
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx/1.24.0 (Ubuntu)</center>
</body>
</html>
```

That 178-byte body contains the word "stratum" 0 times and the phrase "one-click" 0 times. It is not a pool homepage.

The 184805-byte HTML, 38 "stratum", and 0 "one-click" counts in the operator file are from the page after following the redirect. A follow of the same URL on 2026-10-07T21:40:47Z landed on `https://dash.256f.org/` with HTTP 200, 184938 bytes, `etag: "0bd2c8d8e21e41a0975bb65c4cda7423"`, `last-modified: Wed, 30 Sep 2026 16:58:58 GMT`, `server: Vercel`. A direct `GET https://dash.256f.org/` the same second returned the same bytes and the same etag. In that dashboard HTML, "stratum" appears 38 times and "one-click" appears 0 times.

The operator file also says `dash.256f.org` was not queried. The HTML it counted is that dashboard. Visible-text extract of the dashboard already lives at `raw/foundation/dash-256f-org-home.md`.

The live operator API remains `https://pool.256foundation.org/api/v1/query`. That path does not 301. Prometheus numbers belong in the operator file. Dashboard word counts belong here and in the dash extract.
