# The Symmetrical Framework

A classification of finite-norm solutions of the cubic Cauchy-Euler equation

$$x^2 f'' + 3x f' + (1-r^2) f + 8\mu r^2 x^2 f^3 = 0,\qquad x\in(0,\infty),$$

and a dictionary of exact identifications of its sech profile.

Status: **working draft v0.1**. Nothing here is peer reviewed.

## Scope and non-claims (draft wording, edit as you see fit)

- The repository presents a classification theorem and a dictionary of exact equivalences.
- Physical readings are labelled **[I]** and are never used in a proof.
- The classification itself is not claimed to be new (it is a one-dimensional proof of a known type of
  radial classification, see `literature/BIBLIOGRAPHY.md`). Novelty of any identity is decided by the
  literature check, not asserted.

## Status labels

| Label | Meaning |
|---|---|
| **[T]** | theorem or proposition proved in the text |
| **[V]** | verified by a symbolic or numerical computation in `verification/checks.py` |
| **[K]** | known result from the literature (see `literature/BIBLIOGRAPHY.md` for what was and was not checked) |
| **[I]** | interpretation, no proof claimed; never used in a proof |

## Layout

```
00-meta/            CLAIMS.md (generated ledger), ERRATA.md, OPEN.md, NOTATION.md
01-foundational-paper/   the paper (draft v0.1) and the plan for splitting it
02-essays/               Essay I (Euler top), II (BPST instanton), III (kinematic Friedmann)
03-q-family/             the one-parameter family y_q = J^{-q} (optional, follow-up)
04-follow-ups/           duality dial, Lie-system / Hamiltonian algebra, lattice-sum arithmetic
literature/              bibliography with verification levels
templates/               templates for identity files and essays
verification/            checks.py, run_all.py (the single source of truth for [V] claims)
```

## Reproducing the checks

```bash
pip install -r requirements.txt
python verification/run_all.py                  # runs all [V] checks (about 5 s)
python verification/run_all.py --write-ledger   # also regenerates 00-meta/CLAIMS.md
```

The same command runs in CI (`.github/workflows/verify.yml`). A failing check fails the build.

## Rules of the repository

1. **One source of truth.** A claim labelled [V] must have an ID in `verification/checks.py`.
   `00-meta/CLAIMS.md` is generated from the same registry; do not edit it by hand.
2. **Corrections are logged.** Every retraction or correction goes into `00-meta/ERRATA.md`
   with the place where the wrong statement appeared.
3. **Conventions are fixed once** (see `00-meta/NOTATION.md`): which equation is meant, regularity,
   domain, norm, counting of solutions, parameters.
4. **Essays state their dependencies** at the top ("Assumes from the foundational paper: IDs").
5. **Literature has three levels**: bibliographic data confirmed; theorem statement read in a primary
   source; application to this project checked. Only claims at the right level are cited as established.

## Suggested citation

See `CITATION.cff` (placeholders to be filled in).
