# Ocean Mining Pool API

> Source: https://forum.heatpunks.org/t/ocean-mining-pool-api/238
> Collected: 2026-10-10
> Published: 2026-01-03
> Registry ID: heatpunks-forum

tylerkstevens | 2026-01-03 18:59:12 UTC | #1

Check out this GitHub Repo for the Ocean Mining Pool API.

[github.com/Djobleezy/DeepSea-Dashboard](https://github.com/Djobleezy/DeepSea-Dashboard/blob/main/docs/ocean-api-integration.md)

#### [docs/ocean-api-integration.md](https://github.com/Djobleezy/DeepSea-Dashboard/blob/main/docs/ocean-api-integration.md)

main

```md
# Ocean.xyz API Integration

This application integrates with the [Ocean.xyz](https://ocean.xyz) mining pool API to retrieve user hashrates, payout data, and other mining stats.

Base URL:
https://api.ocean.xyz/v1

Example Request:
https://api.ocean.xyz/v1/user_hashrate/3QomtEj5nfzEkxPXoVD3hvxgJDzA6M6evt

---

## API Endpoints Used

| Endpoint | Description | Arguments | Returns |
|----------|-------------|-----------|---------|
| /ping | Server status test | None | "PONG" |
| /statsnap/{username} | Latest TIDES snapshot for a user or worker | username[.workername] | Hashrate, shares, earnings estimation |
| /pool_stat | Pool-wide stats (hashrate, workers, blocks) | None | Stats snapshot of active users, workers, and blocks found |
| /pool_hashrate | Pool-wide hashrate info | None | Hashrate averages over 60s and 300s |

```

show original

Could certainly vibe code a mobile app to have all the features you’d want for your customers. @SoftwarmLLC , what would you say are the main requirements for a simple monitoring app for home and business owners?

-------------------------

SoftwarmLLC | 2026-01-03 19:50:35 UTC | #2

I think Braiins is on point with their app, with the exception of being able to monitor multiple pools and a few other things.

Current and 2 day historical hashrate

Current states of workers with expandable view

Current pool account value and historical earnings

Manual electric price, time of use input, and setting of outside temperature which constitutes a need for heat for that particular person.

BTC price and hashprice

Graphical pofitibility output on the real time basis of hashprice, electric cost, and temp threshhold setting

Estimated daily reward

Pool Statistics
