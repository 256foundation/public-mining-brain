# 256foundation/asic-rs pull request #65: feature: add python bindings

> Source: https://github.com/256foundation/asic-rs/pull/65
> Collected: 2026-10-07
> Published: 2025-09-19

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 65
- State: closed
- Author: b-rowan
- Opened: 2025-09-19
- Closed: 2025-09-19
- Labels: none

## Description

Adds python bindings using `pyo3`.  You can test these bindings by - 

- Creating a python virtual environment in the project (`python3 -m venv .venv`)
- Activating the virtual environment (now located in `.venv`)
- Running `pip install maturin` to install the build tools
- Running `maturin develop` to create a debug build
- Importing and using functionality from `pyasic_rs`, such as `from pyasic_rs.factory import MinerFactory`

This is a hybrid of pyo3 python bindings which give access to the underlying python control functions, and a python library which overlays the functions for better type hinting and pydantic support.
