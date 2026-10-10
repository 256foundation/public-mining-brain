# 256foundation/asic-rs pull request #295: feat(timezone): get / set / list miner timezone

> Source: https://github.com/256foundation/asic-rs/pull/295
> Collected: 2026-10-07
> Published: 2026-06-23

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 295
- State: closed
- Author: pos-ei-don
- Opened: 2026-06-23
- Closed: 2026-09-08
- Labels: none

## Description

**Why I need this:** on **VNish** the timezone is a fixed UTC offset with no DST handling, so it has to be switched **by hand twice a year** (summer/winter) — and that gets forgotten, leaving the miner's clock (and its logs/timestamps) an hour off for months. Keeping a device's clock correct across DST is exactly the kind of thing a controller like Home Assistant should own, so I want to be able to read and set the timezone from there instead of remembering to do it on each miner.

This adds a `SetTimezone` capability (get / set / list + supports) so a consumer can do that:

- New `SetTimezone` trait (default: unsupported), added to the `Miner` supertrait + blanket impl; all backends implement it (trivial except the two below).
- **BraiinsOS** 26.04: named zones via `bos.timezone` / `timezoneList` / `setTimezone` — once a named zone is set, BOS handles DST itself.
- **VNish**: a fixed UTC offset via `/settings` `regional.timezone` (read-modify-write); since VNish has no DST awareness, the consumer (re)applies the correct offset at each DST change.
- Python: `get_timezone` / `list_timezones` / `set_timezone` + `supports_set_timezone`.

CI-green; live write-test pending on my fleet. Happy to shape the API (e.g. a typed timezone, or naming) to your preference.


## Comments

### pos-ei-don on 2026-06-23

Re the list (your follow-up): agreed — I'll use the miner's own list where it has one and fall back to a built-in default list otherwise, no `chrono` needed.

Re moving it under `SupportsConfigs`: makes sense, I'll refactor into the config model as `get_timezone_config`/`set_timezone_config` to match the other configs (same shape as the temperature config). I'll push that rework.

For context on the end goal: this is so Home Assistant can keep a miner's timezone correct across the DST changeover automatically — VNish has no DST handling, so by hand it just gets forgotten.


### pos-ei-don on 2026-08-30

Rebased onto v0.8.0 — only the generated .pyi needed a merge; kept the upstream set_tuning_config signature; added an empty SupportsTimezoneConfig impl for the new elphapex backend. cargo check is green.

### b-rowan on 2026-08-31

Couple comments to address from my old review.

### pos-ei-don on 2026-08-31

Rebased onto current master. The conflict came from #291 landing earlier today: both PRs add a trait to the `Miner` supertrait and an empty impl to the same backends, so every collision was mechanical — both sides kept, nothing dropped.

**`skip_from_py_object` / the hand-written converter** — both done in `24c4806`. `TimezoneConfig` now has the same shape as `config/scaling.rs`: `from_py_object` + `py_pydantic_model`, manual `py_new` kept, no manual `FromPyObject`.

**Real timezone objects instead of strings** — I'd like to push back on this one, because the string isn't laziness. VNish doesn't have named zones at all: it stores a fixed UTC offset under `/regional/timezone` as `"GMT+2"`, doesn't track DST, and has no list endpoint (hence the hardcoded fallback list). BraiinsOS does give you real IANA zones via `timezoneList`. So `chrono-tz` would type the Braiins side properly and leave VNish with nowhere to go — the `String` is the common denominator of two firmwares, not a shortcut.

If you want the type safety anyway, the honest shape is probably an enum rather than a single string — something like `Named(String)` for IANA zones and `Offset(i8)` for VNish-style fixed offsets, so the two can't be confused and each backend declares which it speaks. Happy to build that if you like it; it changes the public type, so I'd rather have your call than guess.

**Copying the impl to every Braiins version** — I'd like to check something first. Right now only `v26_04` has the real implementation; `v21_09`/`v25_03`/`v25_05`/`v25_07` carry empty impls. Copying it is easy, but each also needs a `ConfigField::Timezone` location and a `send_graphql_command` call, which today only `v26_04` uses. Do the older BOS releases actually serve `bos { setTimezone }` and `timezone`/`timezoneList`? I can only test against BraiinsOS on one machine here, so if I copy it blind I'd be declaring `supports_timezone_config() == true` on four backends I can't verify — which is the sort of thing that reads as supported and then silently isn't.

### b-rowan on 2026-08-31

> **Copying the impl to every Braiins version** — I'd like to check something first. Right now only `v26_04` has the real implementation; `v21_09`/`v25_03`/`v25_05`/`v25_07` carry empty impls. Copying it is easy, but each also needs a `ConfigField::Timezone` location and a `send_graphql_command` call, which today only `v26_04` uses. Do the older BOS releases actually serve `bos { setTimezone }` and `timezone`/`timezoneList`? I can only test against BraiinsOS on one machine here, so if I copy it blind I'd be declaring `supports_timezone_config() == true` on four backends I can't verify — which is the sort of thing that reads as supported and then silently isn't.

This is what the `meta/` directory is for (https://github.com/256foundation/asic-rs/tree/master/meta/braiins)

The graphql schema should be pretty consistent across versions, but you can check against that OR the openapi schema, but they should all work in theory with the same implementation, this specific surface hasn't really changed.

### pos-ei-don on 2026-09-05

Pushed the Braiins copy in `2982385` — CI is green (Cargo Test, Cargo Assist, Conventional Commits, Python Test).

### What I checked before copying

You pointed me at `meta/`, so I went through the schemas there rather than copying blind:

| version | schema in `meta/braiins/` | `setTimezone` | `timezoneList` |
|---|---|:--:|:--:|
| 21.09 | `schema.graphql` | — | — |
| 24.09 | `schema.graphql` | ✔ | ✔ |
| 25.03 | `schema.graphql` | ✔ | ✔ |
| 25.05.1 | `schema.graphql` | ✔ | ✔ |
| 25.07 | `openapi.json` | n/a | n/a |
| 26.04 | `openapi.json` | n/a | n/a |

You were right that the surface is stable wherever it exists — with two wrinkles:

- **21.09 doesn't have it at all.** Neither the mutation nor the list is in its schema, so I left `v21_09` on the empty impl. Declaring `supports_timezone_config() == true` there would report support the firmware doesn't have.
- **25.07 and 26.04 only ship `openapi.json` in `meta/`,** which doesn't describe the GraphQL surface — you can see that from 26.04 scoring zero there while actually carrying the working implementation. So the schema can't confirm 25.07 either way. I copied it anyway on the strength of 26.04 working, but I'd rather label that inferred than verified. If you'd prefer `v25_07` stay empty until someone can test it against real hardware, say the word and I'll pull it back out.

Net: `v25_03` and `v25_05` are schema-covered, `v25_07` is inferred, `v21_09` stays empty. The impl in all three is byte-identical to the `v26_04` one — same query, same parse, same mutation.

### Still needs your call: the timezone type

This is the last open point, and I don't want to guess at it because it changes the public type.

Recap: `String` here isn't laziness, it's the common denominator. BraiinsOS gives real IANA zones via `timezoneList`; VNish has no named zones at all — it stores a fixed UTC offset as `"GMT+2"`, doesn't track DST, and has no list endpoint. So `chrono-tz` would type the Braiins side nicely and leave VNish with nowhere to go.

If you want the type safety anyway, the honest shape is probably an enum rather than one string:

```rust
pub enum Timezone {
    Named(String),   // IANA, e.g. "Europe/Vienna" — BraiinsOS
    Offset(i8),      // fixed UTC offset — VNish
}
```

so the two can't be confused and each backend declares which it speaks. Happy to build that, or to leave `String` as-is — either is fine by me, I just don't want to pick a public type on your behalf.

### b-rowan on 2026-09-05

> 25.07 and 26.04 only ship openapi.json in meta/, which doesn't describe the GraphQL surface — you can see that from 26.04 scoring zero there while actually carrying the working implementation. So the schema can't confirm 25.07 either way. I copied it anyway on the strength of 26.04 working, but I'd rather label that inferred than verified. If you'd prefer v25_07 stay empty until someone can test it against real hardware, say the word and I'll pull it back out.

This is fine, GraphQL was sort of "deprecated", they don't work on it anymore AFAIK, but the UI still uses it, so it should just be backwards compatible.

### b-rowan on 2026-09-05

> Recap: String here isn't laziness, it's the common denominator. BraiinsOS gives real IANA zones via timezoneList; VNish has no named zones at all — it stores a fixed UTC offset as "GMT+2", doesn't track DST, and has no list endpoint. So chrono-tz would type the Braiins side nicely and leave VNish with nowhere to go.

I think you might have my idea a bit confused here.  I'm saying "what if we use a pre-existing schema to represent the time zones inside asic-rs, so a user has a consistent format to pass into the functions", and we handle conversion.  I imagine something like chrono has timezone objects (haven't looked), which we can convert to and from "GMT-7" EG for VNish.  This means that the user always knows what they are getting, and we handle the weird abstraction to any miner specific types.

### pos-ei-don on 2026-09-05

Pushed the implementation rather than describing it — easier to argue with a diff. CI is green.

The reasoning, briefly: the conversion isn't symmetric. Braiins gives named IANA zones with DST rules, VNish stores a fixed offset (`"GMT+2"`, no DST, no list endpoint). Named → fixed drops the DST rule, fixed → named is ambiguous. So `chrono_tz::Tz` works as one canonical type only if VNish is restricted to the `Etc/GMT*` zones — real IANA zones, fixed offset, no DST rules. Both firmwares then round-trip cleanly, and `available` is the same type everywhere.

One trap worth knowing about: `Etc/GMT+2` is UTC−2, so VNish `"GMT+2"` maps to `Etc/GMT-2`. There's a test asserting the actual offset in seconds rather than just the names, so a consistently inverted mapping can't pass.

This is a proposal, not a decision — any of it can change:

- **`chrono-tz` is a new dependency** in `asic-rs-core` (it pulls `phf`). Your call entirely; if you'd rather not take it, say so and I'll look for another way.
- `TimezoneConfig.timezone` stays a `String`, with the zone reached through `new(Tz)` / `from_tz` / `tz()`. A real `Option<Tz>` field would need a newtype plus changes in `asic-rs-pydantic(-macros)`, which hardcodes the type→getter/schema mappings. Happy to do that instead if you want the field itself typed.
- `Europe/Vienna` on a VNish miner errors and names the `Etc/GMT*` equivalent, rather than pinning to whatever offset applies today. Tell me if you'd rather it pin.
- `set_timezone_config` now raises from Python instead of returning `None` — otherwise that error is invisible there.

### b-rowan on 2026-09-05

> TimezoneConfig.timezone stays a String, with the zone reached through new(Tz) / from_tz / tz(). A real Option<Tz> field would need a newtype plus changes in asic-rs-pydantic(-macros), which hardcodes the type→getter/schema mappings. Happy to do that instead if you want the field itself typed.

As far as I know, chrono-tz is actually compatible with pyo3 directly.  If you enable the `chrono-tz` feature on pyo3, we can use it directly.  See https://docs.rs/pyo3/latest/pyo3/chrono_tz/index.html

If you do that, we should be able to use it directly rather than string, and avoid all the intermediate conversion.

### pos-ei-don on 2026-09-05

Done — you were right, pyo3's `chrono-tz` feature handles it. `TimezoneConfig.timezone` is `Option<Tz>` now and `available` is `Vec<Tz>`; the accessors and the `parse_iana` helper that only existed to bridge the string are gone. No pyo3 bump needed either — 0.28 already carries chrono-tz `>=0.10, <0.11` as an optional dependency and we're pinned at 0.10.4. CI is green, Python tests included.

Two small things that came with it:

- `asic-rs-pydantic` implements `PyPydanticType for Tz` along the `MacAddr` / `IpAddr` lines — schema `str`, accepts either a `ZoneInfo` or an IANA name, dumps the name. The macro's hint table needed an entry too (`Tz` → `tzinfo | str`); without one it falls through to `object`. No serializer-table entry, since `Tz` has a native `IntoPyObject` and a `String` mapping would put the hop straight back.
- Worth knowing rather than fixing: the getters hand out `zoneinfo.ZoneInfo(name)`, so a Python without tzdata for that key raises where a plain string never did. Fine on CI runners, just not free.

The VNish `GMT±N` ↔ `Etc/GMT∓N` mapping, the DST rejection and the Python raise are unchanged.

### pos-ei-don on 2026-09-05

Heads-up: I'm off on holiday from today, back in about three weeks.

I'd wanted to get this over the line before leaving — the last rounds went quickly and your review made the code better each time. But I'd rather not rush the decoupling on the way out the door.

Where it stands: everything else is done and CI is green. What's left is exactly your last comment, and it turns out to be a clean cut — `vnish_offset_to_tz`, `tz_to_vnish_offset(_now)`, `fixed_offset_hours`, `tz_from_offset_hours` and the private helpers under them (`utc_offset_at`, `noon_utc`, `etc_gmt_equivalent`, `describe_offset`) are used only by the two VNish backends; no Braiins backend touches any of them. So the whole block plus its tests can move into the vnish crate, and `config/timezone.rs` keeps just the type.

Entirely your call from here: if you'd rather make that move yourself and merge, please go ahead, no need to wait for me. If you'd rather it sits until I'm back, that's fine too — I'll pick it up then.
