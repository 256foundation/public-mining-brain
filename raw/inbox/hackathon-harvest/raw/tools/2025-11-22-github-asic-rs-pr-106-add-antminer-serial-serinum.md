# 256foundation/asic-rs pull request #106: Add/antminer-serial-serinum

> Source: https://github.com/256foundation/asic-rs/pull/106
> Collected: 2026-10-07
> Published: 2025-11-22

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 106
- State: closed
- Author: glitchpixelz
- Opened: 2025-11-22
- Closed: 2025-11-25
- Labels: none

## Description

## Summary

This PR adds a second `SerialNumber` extractor for Antminer devices to support firmware that exposes the serial as `serinum` instead of `serial_no`.

The `DataField::SerialNumber` mapping now includes both:

- `/serial_no` (existing behavior)
- `/serinum` (new, for firmware such as S21 2025)

## Motivation

On Antminer S21 (2025 firmware), the `serial_number` field in `MinerData` is always `null`.  
The `get_system_info` endpoint on these units returns the serial in the `serinum` field, not `serial_no`.

By adding a second extractor using the existing fallback mechanism in `extract_field`, we can support both formats.

## Implementation
            DataField::SerialNumber => vec![(
                system_info_cmd.clone(),
                DataExtractor {
                    func: get_by_pointer,
                    key: Some("/serial_no"), // Cant find on 2022 firmware, does exist on 2025 firmware for XP
                    tag: None,
                },
            ),
                (
                system_info_cmd.clone(),
                DataExtractor {
                    func: get_by_pointer,
                    key: Some("/serinum"), // exist on 2025 firmware for s21
                    tag: None,
                },
            )],
            
**Testing**

Tested locally against an Antminer S21 (2025 firmware).

Confirmed that MinerData.serial_number is now populated correctly.

Existing /serial_no path is preserved and should continue to work, but it would be great if you could verify this on units that still expose serial_no.

## Comments

### b-rowan on 2025-11-22

Sweet, will review when I have a chance.
