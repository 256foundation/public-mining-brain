# bitaxeorg/ESP-Miner issue #1361: Hashrate spike on graph

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1361
> Collected: 2026-10-07
> Published: 2025-11-17

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1361
- State: closed
- Author: mutatrum
- Opened: 2025-11-17
- Closed: 2026-04-24
- Labels: bug

## Description

As reported on [Discord](https://discord.com/channels/1091348375301013615/1094385604982210633/1439805589310930945):

<img width="2181" height="855" alt="Image" src="https://github.com/user-attachments/assets/98d0a76b-6e4c-48bc-900d-3c43805ba64b" />

## Comments

### jns-codeworks on 2025-11-18

These spikes seem to occure when the internet connection is lost.

<img width="2186" height="958" alt="Image" src="https://github.com/user-attachments/assets/1805c156-eacb-4459-8946-2087bd5c42c4" />

### mutatrum on 2025-11-18

Oh, that's an interesting find. It's weird, as I would think the chip just continues to hash, so not sure how that affects the hashrate metric. Would be very interesting to see the logs when it happened. And was it an ISP glitch, or local Wi-Fi?

### jns-codeworks on 2025-11-18

I'm facing regular connection interruptions, because of the ISP. 
According to the logs, the chip continues hashing and submitting results but the pool is, obviously, not answering. 

### WantClue on 2025-12-12

> These spikes seem to occure when the internet connection is lost.
> 
> <img alt="Image" width="2000" height="958" src="https://private-user-images.githubusercontent.com/28293626/515893584-1805c156-eacb-4459-8946-2087bd5c42c4.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjU1NTU4MjQsIm5iZiI6MTc2NTU1NTUyNCwicGF0aCI6Ii8yODI5MzYyNi81MTU4OTM1ODQtMTgwNWMxNTYtZWFjYi00NDU5LTg5NDYtMjA4N2JkNWM0MmM0LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEyMTIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMjEyVDE2MDUyNFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWExOGFjM2I3YjMxMjY3ZDBkNWRiNDhlYWY4MTNmYTRmYzg5NDU5ODJjODA0YzhmNWNmNmNhYTgwMmFhOTU0MTcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.pBA9q99s5JcutLD6nh7b7veKfwFa2gluxUxCivrvqXg">

I cannot confirm that, I've seen them at random occasions as well

### jns-codeworks on 2025-12-12

I have seen it also on other occasions recently, but only after upgrading to firmware v2.12.0
