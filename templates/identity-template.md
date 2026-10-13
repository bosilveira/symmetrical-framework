---
id: X00                # must match an ID in verification/checks.py if status contains V
title: short title
status: [V]            # one or more of T, V, K, I
depends_on: []         # IDs of identities this one uses
section: paper s?.?    # where it is used
script: verification/checks.py::X00
---

## Statement

State the identity exactly, with parameters, domain and regime
(for example: r > 0, mu > 0, x in (0, infinity)).

## Derivation or reference

- If [T]: the proof (or a pointer to the paper section).
- If [V]: a one-paragraph description of what the script checks and with what tolerance.
- If [K]: the reference (see literature/BIBLIOGRAPHY.md) and what was and was not checked.
- If [I]: label every sentence as interpretation; nothing here may be used in a proof.

## Regime and limits

Where the identity holds and where it fails (signs of s, kappa, epsilon; r = 1; mu = 0 ...).

## Notes

Corrections go to 00-meta/ERRATA.md.
