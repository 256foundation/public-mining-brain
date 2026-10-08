# bitaxeorg/ESP-Miner issue #1954: Self-test: PWM=0 should not block startup

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1954
> Collected: 2026-10-07
> Published: 2026-09-08

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1954
- State: open
- Author: seby1302
- Opened: 2026-09-08
- Closed: n/a
- Labels: none

## Description

The current self-test treats `PWM = 0` as a critical failure and can block the user from accessing the miner.

I think this check should be removed or changed to a non-blocking warning.

The self-test already checks the ASIC temperature, which is the relevant safety condition. A PWM value of `0` does not necessarily mean that the ASIC is running without cooling.

There are several valid setups where PWM can intentionally be `0`, for example:

* External fan control
* Water cooling
* External temperature-controlled cooling
* Other cooling solutions not controlled by the miner PWM output

In these cases the ASIC can be cooled correctly while the internal PWM output remains at `0`.

The current behavior can therefore lock a user out of an otherwise technically valid and safe configuration. In the worst case, the user may have to temporarily rebuild or reconnect the original fan setup just to pass the self-test and regain access.

### Suggested behavior

`PWM = 0` should not cause the self-test to fail.

The existing ASIC temperature check should remain the primary safety check.

Optionally, `PWM = 0` could produce a warning such as:

`Fan PWM is 0. Make sure external cooling is active.`

But it should not block access or prevent normal startup when ASIC temperature is within the allowed range.


<img width="1640" height="190" alt="Image" src="https://github.com/user-attachments/assets/33038f4f-a4fc-4f21-8f75-aa09d11f228b" />

<img width="457" height="481" alt="Image" src="https://github.com/user-attachments/assets/996864dc-1a3f-4558-9846-fee7ad2398da" />


## Comments

### mutatrum on 2026-09-08

The self-test is mainly for manufacturers to validate new machines. If you run a custom PWM setup, you can probably work around the self-test failing on the missing PWM sensor reading.

How is someone blocked when this happens? As you can always flash a config with `selftest=0` which should boot the device normally.

### seby1302 on 2026-09-08

That's generally true for a brand-new device, where the expected fan/PWM setup is still connected.

The problematic case is when the self-test gets triggered again later. An NVS reset is one example — this actually happened to me — but settings can also be lost or reset for other reasons. At that point the machine may already have been modified for external fan control, water cooling, or another cooling setup, and the original fan connection may no longer be easily accessible.

Of course, `selftest=0` can be used as a workaround if you can flash the appropriate configuration. But that still leaves the question of why PWM=0 needs to be a hard failure at all.

PWM itself is not the safety target — ASIC temperature is. A machine can have PWM=0 and still be perfectly and safely cooled by an external system.

So I think PWM=0 should at most generate a warning during self-test. If the ASIC temperature is within the required limits, the self-test should be allowed to continue. This would keep the manufacturer validation useful without unnecessarily blocking valid custom cooling configurations.



### seby1302 on 2026-09-13

I made my own adjustments to the self-test, and these changes resolve the issues I encountered with my setup.

The changes address four problems:

* **Hash domain limit:** The previous 380 GH/s upper limit was too restrictive and could cause false failures with higher-performing domains. I increased the limit to **500 GH/s**. A domain reporting a higher but still plausible hash rate should not automatically be treated as faulty.

* **Missing fan/tachometer:** The fan RPM test could fail on modified systems using external or water cooling, even though ASIC temperatures were completely safe. I removed the fan RPM test for my setup. In this case, the actual ASIC temperature remains the relevant safety criterion rather than the presence of a tachometer signal.

* **Cooling too effective:** With good external cooling, the ASIC may never reach the 55°C warm-up target, causing the self-test to remain in the warm-up loop indefinitely. This can happen precisely because the cooling solution is working well, so failing or blocking the test for this reason does not seem useful. I added a **60-second warm-up timeout**, after which the actual test continues.

* **Total hash-rate threshold:** The calculated theoretical hash rate is useful as a reference and diagnostic value, but I do not think it should be used as a strict pass/fail threshold. An ASIC that does not reach the theoretical performance at the predefined self-test operating point is not necessarily defective.

  I have a practical example of this in my own hardware: one ASIC performs poorly at lower settings and would be rejected by the conventional self-test as defective. However, when operated at **1,2 V and 700 MHz**, the same ASIC runs well and is actually more efficient than some of my other ASICs.

  This demonstrates an important distinction between **failing to meet a predefined performance profile** and **being defective hardware**. ASIC characteristics can vary, and the optimal operating point of one chip does not necessarily have to be the optimal operating point of another. Voltage, frequency, cooling, silicon characteristics, and manual tuning can all influence the resulting performance and efficiency.

  A self-test should therefore primarily detect hardware that cannot operate reliably, rather than discard an otherwise usable ASIC simply because it does not achieve the theoretical target at one predefined operating point.

  For this reason, I added a **500 GH/s minimum total hash-rate threshold** for the self-test. The theoretical expected hash rate is still calculated and displayed as useful diagnostic information, but it is no longer used directly as the pass/fail criterion.

  For example, a device measuring around **516 GH/s** while the calculated theoretical target is around **910 GH/s** should not automatically be classified as defective if it is otherwise operating correctly and producing valid nonces.

I also added percentage/progress information to the display so it is easier to see what the self-test is currently doing.

During warm-up, for example:

`WARM 45% 42.6/55.0C`

and during the actual hash-rate test:

`TEST 33% 1200G 43.0C 20s`

This makes the current stage and progress immediately visible instead of making the device appear to be stuck.

I will upload my modified `self_test.c` as a reference. Feel free to use or adapt any parts of it that may be useful for the project.

The intention of these changes is to make the self-test distinguish more clearly between an **actual hardware fault** and an ASIC that simply operates outside the predefined performance profile but may still perform reliably — or even very efficiently — after appropriate tuning.

This is intended as a suggestion/reference. For my setup, the issues are resolved and this can be closed.

Thanks!

[self_test.zip](https://github.com/user-attachments/files/32239275/self_test.zip)
