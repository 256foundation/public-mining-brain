# 256foundation/mujina pull request #33: feat(bitaxe): add PI-based fan speed controller

> Source: https://github.com/256foundation/mujina/pull/33
> Collected: 2026-10-07
> Published: 2026-03-03

- Repository: 256foundation/mujina
- Type: pull request
- Number: 33
- State: open
- Author: jayrmotta
- Opened: 2026-03-03
- Closed: n/a
- Labels: none

## Description

# Summary

Currently the fan controller available on Mujina sets the fan speed to 100% as the system initializes, it sits at that value through the entire firmware lifecycle. Issue #9 describes this behavior and points to esp-miner's implementation of a PID controller to control the temperature.

## Changes

- Add fan control for Bitaxe boards
- Introduce temperature filtering to smooth sensor readings
- Integrate cooling control into existing Bitaxe board lifecycle

## Goal

Improve thermal management and protect Bitaxe hardware under sustained load by actively controlling the fan based on filtered temperature readings. 

# Testing

- Verified that the temperature filter accepts realistic readings into a bounded sliding window while rejecting values that fall outside the reasonable operating range;
- Checked that sudden, unrealistic jumps in temperature are treated as noise and discarded, without preventing subsequent, more plausible readings from being used;
- Confirmed that the control loop combines proportional and integral terms correctly, accumulating error over time while keeping that accumulated value within sensible bounds to avoid runaway behavior;  
- Ensured the controller can be reset between runs so that past error does not leak into new control cycles;  
- Tested that no fan speed changes are requested until a valid temperature reading is actually available;  
- Verified that, once a valid temperature is present, the controller periodically computes and publishes fan speed updates based on the difference between the current temperature and the configured target.

Fixes: #9

## Comments

### rkuester on 2026-03-12

> This may be unrelated but I can run much higher frequencies on ESP-Miner with the same hardware.

I'd be quite interested in getting to the bottom of any differences like this between Mujina and esp-miner. Do you mean esp-miner runs a lot cooler than Mujina for the same frequency? If so, have you compared the chip voltage in both cases?

(FWIW, I'm working up a larger review of this PR.)

### rkuester on 2026-03-13

Thanks for working on this, Jayr! It sounds like you guys are getting the PI controller math and the temperature filter dialed in. I have some architectural feedback that I think will make this simpler and easier to build on.

The core job here is: read temperature, compute fan speed, set fan speed. That's a sequential operation, but right now the PR spreads it across four async tasks—fan worker dispatch loop, temperature reader, PI controller, and fan speed listener—connected by five channels. That's a lot of moving parts. Let me walk through what I'd suggest instead.

### Remove fan worker actor

The `FanWorkerCommand` enum, oneshot response channels, dispatch loop, and `fan_worker_request` helper add up to ~150 lines that serialize access to the EMC2101. But look at how the TPS546 voltage regulator is handled a few fields away in the same struct:

```rust
regulator: Option<Arc<Mutex<Tps546<BitaxeRawI2c>>>>,
```

The regulator is shared between the stats monitor and the board lifecycle with a simple `Arc<Mutex<>>`.

But actually, we can do even better. Instead of sharing the EMC2101 behind a mutex, let's give it a single owner.

### One owner for the EMC2101

The stats monitor needs temperature, fan setpoint, and RPM. The fan controller needs temperature. Both need the EMC2101. Rather than sharing it, let one task own it exclusively and publish a cached snapshot for everyone else:

```rust
/// Cached readings, published via watch channel.
struct ThermalReadings {
    temperature: Option<f32>,
    fan_percent: Option<u8>,
    fan_rpm: Option<u32>,
}
```

That single task does everything in one loop:

```rust
loop {
    // Read hardware (only task that touches the EMC2101)
    let temp = emc2101.get_external_temperature().await.ok();
    let rpm = emc2101.get_rpm().await.ok();
    let pct = emc2101.get_fan_speed().await.ok().map(u8::from);

    // Run control math, set speed
    if let Some(temp) = temp {
        if let Some(speed) = controller.update(temp, dt) {
            emc2101.set_fan_speed(speed).await;
        }
    }

    // Publish snapshot for stats monitor
    snapshot_tx.send(ThermalReadings { temp, pct, rpm });

    sleep(interval).await;
}
```

The stats monitor holds a `watch::Receiver<ThermalReadings>` and calls `.borrow()` whenever it needs the latest readings—it can call it as often as it likes, it just gets a read-only snapshot of whatever the thermal task last published. No I2C, no contention.

This loop lives in a single spawned task—similar to how `spawn_stats_monitor` works today—replacing the current four. Shutdown is straightforward: cancel the one task, and set the fan to a safe speed.

This also leaves room for a future API override of the fan speed. The thermal task is the single writer to the EMC2101, so an API "hold fan at X%" command could just tell that task to pause the PI controller and hold a fixed speed until the API releases the constraint.

### The fan controller should be a plain object

The PI controller and temperature filter are pure math—they don't need to be async, and they don't need channels. A synchronous `update` method makes them composable by any caller:

```rust
pub struct FanController {
    filter: TemperatureFilter,
    pi: PiController,
    target_temp: f32,
}

impl FanController {
    /// Feed a raw sensor reading; get back a fan speed if the
    /// reading passes the noise filter.
    /// `dt` is the time since the last call. The integral term
    /// needs reasonably stable intervals, but that's a given
    /// since the caller runs on a `time::interval`.
    pub fn update(
        &mut self,
        reading: f32,
        dt: Duration,
    ) -> Option<Percent> {
        let temp = self.filter.consider(reading)?;
        let error = temp - self.target_temp;
        let output = self.pi.update(error, dt);
        let speed = (MIN + output).clamp(MIN, MAX);
        Some(Percent::new_clamped(speed as u8))
    }
}
```

The caller provides a temperature, gets back a fan speed. That's the whole interface. The board decides how and when to read the sensor and how to apply the result.

The PI gains are tuned assuming a roughly stable tick interval, so `dt` matters for tuning; but since the caller runs on a fixed timer, it's stable in practice. The target temperature and PI gains (Kp, Ki, integral bounds) should be constructor parameters rather than module-level constants, so different boards can tune for their own thermal characteristics. Something like:

```rust
pub struct FanControllerConfig {
    pub target_temp: f32,
    pub kp: f32,
    pub ki: f32,
    pub integral_bounds: (f32, f32),
}

impl FanController {
    pub fn new(config: FanControllerConfig) -> Self { ... }
}
```

### Where things should live

For now, keeping the fan controller in `board/bitaxe/` is good. Once it's a synchronous object with no bitaxe-specific dependencies, it'll be easy to lift into a shared module later if another board needs something similar.

The temperature filter is an implementation detail of the controller—I'd fold it into `fan_controller.rs` rather than giving it a separate module.

### Summary

1. Drop the fan worker actor. One task owns the EMC2101, reads it periodically, runs the fan controller, and publishes a `ThermalReadings` via watch channel.
2. Make `FanController` synchronous. A plain `update(temp, dt) -> Option<Percent>` method, composing the filter and PI math internally. No channels, no async.
3. Refactor the stats monitor read to the snapshot. Just `.borrow()` on the watch receiver. No I2C access needed.

This should cut the non-test code size significantly and be easier to follow and extend. The PI tuning, filter, logic, and test coverage you've built are good—it's really just the plumbing around them that I'd like to see simplified.

I may be oversimplifying in places; if you encounter details I'm glossing over, let's talk through it. Reaching too eagerly for tasks and channels is a common anti-pattern in async Rust. The right idea is usually to start with synchronous code and only introduce concurrency when you have a concrete reason.


### rkuester on 2026-03-13

Because this is still a work in progress, I've marked it as a draft PR.

### johnnyasantoss on 2026-03-13

> I'd be quite interested in getting to the bottom of any differences like this between Mujina and esp-miner.

@rkuester continuing it here: https://github.com/256foundation/mujina/discussions/50

### jayrmotta on 2026-03-16

Indeed that's a lot simpler @rkuester, please take a look when you got the time

### Nickamoto on 2026-03-18

Tested the revised architecture on a Bitaxe Gamma 601 (BM1370) running bitaxe-raw over USB — combined with PR #39 locally for macOS IOKit discovery. ~30 minute run: discovery → ASIC init → pool connect → shares submitted → thermal control active throughout. Fan settled at 47% (~4,600 RPM) with ASIC stable at 70°C. The single-task EMC2101 owner + watch channel approach works well in practice.

A few things I noticed that weren't covered in the earlier discussion:

Panic if EMC2101 init fails

init_fan_controller handles a failed fan.init() with a warning and Ok(()), leaving self.fan as None. Then spawn_thermal_task calls .expect("Fan controller must be initialized before spawning thermal monitor") on it. If the hardware isn't there, that's a panic rather than a graceful degradation. Might be worth either propagating the error or skipping the thermal task spawn when self.fan is None, depending on whether the fan is considered required.

Dangling doc reference on FanPIController

Line 104: "See module-level documentation for rationale." The module doc just describes what the controller does — the rationale for omitting the derivative term (noise amplification from thermal diodes) isn't actually written down anywhere. It's a good reason and worth capturing; right now the reference just points to nothing.

No unit tests for FanPIController

TemperatureFilter has solid coverage. If the PI update logic, windup clamping, and output clamping ever get touched during a future tuning pass, having a few fixed-input tests there would help catch regressions.

### jayrmotta on 2026-03-18

Hey @Nickamoto, I appreciate the review, tests, and feedback :muscle: 

I re-added the `FanPiController` tests, I had removed them recently because of the [Test Behaviors, Not Implementation Details TEST.behavior](https://github.com/256foundation/mujina/blob/main/CODING_GUIDELINES.md#TEST.behavior) coding guideline. I couldn't come up with a way to test its logic without tying the test to the implementation since it's a math heavy construct. Do you think it makes sense to keep it?

I also added an early return to the thermal task, so if the fan fails to initialize the firmware won't panic. But on the other hand it might also not set the fan to 100% speed, which could potentially risk the hw? I've observed that bitaxe-raw is intermittent with booting with the fan on/off.

Thanks for the shout with the docs as well, it slipped my mind, I think it's okay now.

### Nickamoto on 2026-03-19

> Hey @Nickamoto, I appreciate the review, tests, and feedback 💪
> 
> I re-added the `FanPiController` tests, I had removed them recently because of the [Test Behaviors, Not Implementation Details TEST.behavior](https://github.com/256foundation/mujina/blob/main/CODING_GUIDELINES.md#TEST.behavior) coding guideline. I couldn't come up with a way to test its logic without tying the test to the implementation since it's a math heavy construct. Do you think it makes sense to keep it?
> 
> I also added an early return to the thermal task, so if the fan fails to initialize the firmware won't panic. But on the other hand it might also not set the fan to 100% speed, which could potentially risk the hw? I've observed that bitaxe-raw is intermittent with booting with the fan on/off.
> 
> Thanks for the shout with the docs as well, it slipped my mind, I think it's okay now.

On the test question, I think the guideline is on your side for keeping them. TEST.behavior is aimed at tests that break when you refactor internals while preserving the contract, like asserting a hardcoded specificity score. A PI controller is a pure function: given an error and a timestep, you get a control output. Testing that relationship is testing the behavioral contract, not the implementation. If you swap out the math for a different approach someday and the output changes, the test should catch that. I'd keep them.

On the fan init failure, the early return fixes the panic. This is good, but I'm not sure Ok(()) is the right outcome when thermal protection can't start. The miner continues hashing with no fan control, and the fan stays at whatever state the hardware defaulted to rather than a known safe speed. For a Bitaxe at 70°C that might be fine, but as this code path gets reused on higher-power boards it becomes riskier. Worth considering whether a failed fan init should be a hard error that stops the board from starting rather than a silent degradation. The intermittent boot behavior on bitaxe-raw is worth noting, but I wouldn't let hardware quirks drive the error handling strategy for all boards.

### jayrmotta on 2026-03-22

> On the fan init failure, the early return fixes the panic. This is good, but I'm not sure Ok(()) is the right outcome when thermal protection can't start. The miner continues hashing with no fan control, and the fan stays at whatever state the hardware defaulted to rather than a known safe speed. For a Bitaxe at 70°C that might be fine, but as this code path gets reused on higher-power boards it becomes riskier. Worth considering whether a failed fan init should be a hard error that stops the board from starting rather than a silent degradation. The intermittent boot behavior on bitaxe-raw is worth noting, but I wouldn't let hardware quirks drive the error handling strategy for all boards.

Any thoughts on this @rkuester ? Would this be a case worth panicking?

### rkuester on 2026-03-25

I rebased this on top of the latest main.

### rkuester on 2026-03-26

> Any thoughts on this @rkuester ? Would this be a case worth panicking?

Good question. Not a panic, no. We want to avoid panics wherever possible. A panic takes down the whole process (or at minimum the task), leaving the system in an unknown state. If there's a reasonable chance something can fail, we should handle it with a proper error path.

But I also don't think we should silently continue. The concern isn't controlling the fan per se, it's that if we can't reach a peripheral on the board, that's a sign something is wrong at a lower level and we probably shouldn't push forward. I'd return an error from `initialize()` and let the board fail to start.

I notice there are several `expect()`s elsewhere in bitaxe.rs that could also panic on hardware failures. Those should be cleaned up too, but that's a separate effort. I've opened #52 for that.

### jayrmotta on 2026-03-31

Spiced it up a little @rkuester, I wasn't happy with the `spawn_thermal_task` function once I merged the initialize into it as it became too much, so I decided to introduce a `ThermalTask` in a way that would be (arguably) easier to reason/understand while also keeping it testable (dependency injection).

I'm happy to undo and just have it all plain in the original function, but I think it looks better like this and I feel better knowing we have test coverage for that as well.

### jayrmotta on 2026-04-09

> esp-miner doesn't do any filtering, if I recall correctly

Did some digging on ESP-miner and found out they actually do filter values (check here https://github.com/bitaxeorg/ESP-Miner/blob/master/main/tasks/fan_controller_task.c#L92-L99).

They use an [EMA filter](https://en.wikipedia.org/wiki/Exponential_smoothing) in contrast to the rolling window + threshold filter I introduced. So I decided to run an experiment with a plausible time series against the two implementations.


<img width="320" alt="ema filter" src="https://github.com/user-attachments/assets/70df60a7-efb5-403b-9c2b-3cc56682d141" />

<img width="320" alt="rwt filter" src="https://github.com/user-attachments/assets/834cb1d1-e024-437c-8dae-ef91bc125e84" />

<details>
<summary>Time series</summary>

```json
[
  39.374863, 40.091479, 37.147465, 42.988044, 38.013364, 39.616776, 41.809599, 39.363224, 39.820107, 40.219403,
  42.585975, 45.372985, 42.172862, 40.609544, 43.270899, 41.743951, 42.785375, 44.752452, 42.044023, 43.355246,
  42.200426, 43.458816, 44.254202, 42.562058, 43.712873, 44.042709, 43.616382, 42.967325, 42.792797, 44.870260,
  44.872796, 48.799311, 41.975989, 45.973110, 46.535566, 48.195230, 47.084444, 45.241217, 46.683432, 47.672825,
  46.564914, 48.367573, 44.584799, 50.159591, 49.940210, 47.411057, 49.007463, 48.338288, 47.198508, 48.749656,
  50.294519, 48.398210, 48.582225, 49.209902, 50.147732, 51.590936, 48.897227, 50.787720, 50.525179, 47.588966,
  49.923789, 50.530150, 50.845167, 51.569407, 48.195797, 51.501544, 50.591527, 49.624761, 52.746244, 53.238598,
  51.331682, 53.751122, 52.091042, 52.938929, 51.366967, 55.567685, 49.377660, 53.405535, 54.761272, 50.844273,
  122.989222, 54.130403, 55.659165, 56.470309, 54.168031, 52.872971, 57.176481, 57.128336, 54.784379, 56.179599,
  121.399732, 56.854438, 56.487216, 58.466828, 53.925724, 58.269779, 57.455130, 56.734599, 58.996478, 53.896656,
  126.136026, 58.342936, 56.239999, 58.765217, 57.835328, 62.345279, 61.396215, 59.480130, 57.916094, 58.295732,
  123.706837, 58.682261, 58.345123, 58.987913, 59.635982, 59.450805, 59.354125, 59.184552, 64.579426, 58.719888,
  122.036921, 61.930001, 60.971916, 62.268903, 63.007815, 63.878845, 63.288751, 60.846042, 64.176278, 60.041066,
  62.692690, 62.292940, 61.624882, 64.279460, 63.292954, 65.273501, 61.695900, 65.364945, 65.018267, 64.636992,
  62.494900, 64.421334, 62.654862, 62.026776, 70.246251, 66.958805, 68.367281, 65.210751, 67.074448, 67.252155,
  67.284183, 66.563278, 66.391297, 63.805129, 68.000643, 67.896552, 69.114016, 67.201702, 70.401663, 67.293573,
  66.257563, 69.723828, 67.789943, 66.786261, 69.031457, 70.154854, 69.558139, 70.117998, 75.710778, 70.955299,
  72.197138, 67.096608, 70.798837, 71.588259, 70.056296, 69.464925, 71.549554, 70.658727, 70.415899, 73.206663,
  73.661641, 72.288115, 71.328708, 72.957486, 73.605997, 73.483621, 70.533521, 72.382421, 73.604027, 74.174537,
  74.858258, 74.730520, 72.067366, 72.883592, 72.288459, 77.003197, 74.742977, 75.477988, 76.373664, 74.506496
]
```

</details>

In my eyes the performance is similar and the trade-offs are mostly conceptual versus implementation complexity. I believe EMA's implementation is simpler but the concept is more complex and vice-versa with the RW+T filter.

Which one you think we should go for @rkuester ? EMA, RW+T, or none?

### rkuester on 2026-04-09

> Did some digging on ESP-miner and found out they actually do filter values (check here https://github.com/bitaxeorg/ESP-Miner/blob/master/main/tasks/fan_controller_task.c#L92-L99).

Interesting. That's quite a recent addition (bitaxeorg/ESP-miner#1640)—about one week ago! Well, if it's good for them it's good for us. Be sure to think through the effect of any differences in filter constants and sampling rate. Looks like you've got a good handle on it with your modeling there.

I'm a fan 🤦‍♂️ of EMA, it being simpler.

### jayrmotta on 2026-06-08

Hey @rkuester, would you please review it once more?

### rkuester on 2026-06-08

> Hey @rkuester, would you please review it once more?

Yessir. 🫡

### jayrmotta on 2026-09-15

Hey @rkuester, just rebased this to keep it fresh for review and merge. Would you please give it a look?
