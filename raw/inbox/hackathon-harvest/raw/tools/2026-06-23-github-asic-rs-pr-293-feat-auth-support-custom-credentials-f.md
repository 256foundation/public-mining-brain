# 256foundation/asic-rs pull request #293: feat(auth): support custom credentials for authenticated actions

> Source: https://github.com/256foundation/asic-rs/pull/293
> Collected: 2026-10-07
> Published: 2026-06-23

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 293
- State: closed
- Author: pos-ei-don
- Opened: 2026-06-23
- Closed: 2026-06-24
- Labels: none

## Description

A number of actions need authentication (config/metadata reads, presets, throttle, power target, …). This lets a consumer supply **their own** credentials when they have them — for **VNish and BraiinsOS (BOS)** — but it changes **nothing unless they opt in**.

**If you supply no credentials, behaviour is identical to today**: the backend logs in with its built-in **default credentials**, exactly as before. No default is removed; the connection probe / default-password flow keeps working unchanged. Purely additive.

- `MinerAuth` already carries username/password; this adds an optional pre-issued **token** for firmwares that accept one (`new(user, pass)` unchanged, `with_token` builder).
- **VNish** (no username, password-only, also accepts a bearer token) and the **BraiinsOS (BOS)** HTTP API (bearer token): use whatever is supplied — a token directly if present, otherwise the password login, which **falls back to the built-in default** when nothing is given.
- Python `set_auth(username, password, token=None)` exposes it.

Happy to shape the API to your preference.


## Comments

### b-rowan on 2026-06-23

What is the reasoning behind this?  There isn't a tool that I'm aware of that uses this, and the code is all open source, so you don't have to worry about it stealing your passwords or something.  This just seems like a more complicated way to use a miner API...

### pos-ei-don on 2026-06-23

The reasoning is about how a system like Home Assistant should get access to a device. A token is the modern way to do that: I can grant HA scoped, revocable access without either handing it my own (plaintext) device password, or inventing a *second* password just for HA that I then have to remember — realistically only a password manager makes that workable. I'm genuinely glad VNish offers this, and I'd like to be able to use it.

It's not about distrusting the library — it's that I'd rather not be pushed toward *less* security than the firmware already allows. And since this is purely additive (a handful of lines, no change to how anyone else uses the API, nothing removed or constrained), I'd be really happy to see it included: it just gives token-capable firmwares a first-class path while leaving password auth exactly as it is.


### b-rowan on 2026-06-23

> And since this is purely additive (a handful of lines, no change to how anyone else uses the API, nothing removed or constrained), I'd be really happy to see it included: it just gives token-capable firmwares a first-class path while leaving password auth exactly as it is.

I can see a situation where this is useful, but it just doesn't feel very extensible...  I have some changes I want to propose to the shape of this which will change some other parts of the lib, but it should be possible.

Side note, I am not a fan of this mainly because of the use cases at scale, and it just complicates the API because less than 1% of 1% of 1% of miners will use this, but if it has any use case I suppose asic-rs should try to support it.

### pos-ei-don on 2026-06-24

Done — converted `MinerAuth` to the enum you sketched:

```rust
enum MinerAuth { UserAndPass(UserAndPassAuth), TokenAuth(SecretString) }
```

- `MinerAuth::new()` builds `UserAndPass`; `from_token()` builds `TokenAuth` (replaces `with_token`).
- VNish + BraiinsOS HTTP `ensure_authenticated()` now `match &self.auth` to use the token directly, or log in with username/password — as you suggested in `web.rs`.
- The username/password-only backends use small `username()` / `password()` accessors so the login call sites stay tidy; the token-vs-password decision is the `match`.

CI is green. You mentioned broader shape-changes that touch other parts of the lib — happy to go that way too. If you'd rather drive that shape, just outline it and I'll rework on top; this is a working first cut of the enum either way.

### b-rowan on 2026-06-24

Not much left now, just want to separate out the python calls and then it will be good to merge.

### pos-ei-don on 2026-06-24

Done in `d8339a4` — `set_auth(username, password)` is now user/pass only, and a separate `set_token(token)` sets a pre-issued bearer token (with a shared `apply_auth` helper). `.pyi` updated to match.

CI green (Cargo + Python). Should be good to merge now 👍
