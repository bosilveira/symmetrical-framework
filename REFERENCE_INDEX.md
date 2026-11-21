# Reference Index — Symmetrical Framework

**Canonical source: [main](README.md).** This file is the read-first mathematical navigation and future-assistant handoff. It replaces the former two-branch index; the separate branches have been retained as backups, not adopted as competing authorities.

## First five links for a new research session

1. [AGENTS.md](AGENTS.md) — read protocol, current branch and source-priority rules.
2. [Canonical notation](reference/NOTATION.md) — definitions, coordinates, domains and distinct derivative variables.
3. [Claim registry](reference/CLAIM_REGISTRY.md) — selected claims, stable IDs, hypotheses and proof paths.
4. [Foundations](reference/README.md) — numbered foundational drafts, reviewed algebraic/differential chapters and correction registers.
5. [Research and archive policies](research/README.md) / [Archive](archive/README.md) — find exploratory sources without treating them as theorems.

## Mathematical map

| Topic / desired result | Source to inspect first | Status |
|---|---|---|
| Kernel and $`2xf=\mathrm{sech}(ru)`$ | [Reference Chapter 1](reference/algebra-geometry/01-architectural-identities/01-00-summary.md) | Revised algebra and proof |
| Exponential pair and Gram invariant | [Foundational 020](reference/foundations/020%20The%20Linear%20Exponential%20Backbone.md) | Foundational draft with theorem statements |
| Inversion, log-affine, weighted overlap, Fisher | [Reference Chapter 2](reference/algebra-geometry/02-foundational-symmetries/02-00-summary.md) | Revised algebra, derivations and local audit |
| Cubic Master, separatrix, dn/cn, Pinney, Kelvin | [Reference Chapter 3](reference/algebra-geometry/03-differential-structure/03-00-summary.md) | Revised rigorous differential exposition |
| Maxima, inflections, graph arc lengths, surfaces | [Reference Chapter 4](reference/algebra-geometry/04-geometric-properties/04-00-summary.md) | Revised geometric exposition |
| Mellin, Fourier, special functions, probability | [Research legacy Parts II and III](research/legacy-parts/README.md) | **Provisional** until independently reviewed |
| Sturm–Liouville, geometry, moving frames, spectral curves | [Active mathematical drafts](research/active-drafts/README.md) | **Provisional** investigations |
| Integrability, Hirota, Sato, modular and number theory | [Research materials](research/README.md) | **Provisional**; precise correspondence must be checked |
| K3, Mathieu, Leech, moonshine, CY3 claims in historical Part VII | [Archived legacy interpretations](archive/legacy-interpretations/README.md) | **Not accepted as deductions**; separate valid classical facts from unsupported identifications |

For the original research chronology and source paths, see [MIGRATION.md](MIGRATION.md). Do not assume a theorem is true because it appears in a particular folder; the actual status attaches to its statement, proof and hypotheses.

## Canonical variables and the two differential equations

Unless explicitly stated otherwise, $`x,c,r>0`$, $`u=\log(x/c)`$, and $`\theta=ru`$. If the coupled cubic equation is used, also assume $`\mu>0`$ and define $`y=2xf_\mu`$.

```math
S=\mathrm{sech}(ru),\qquad W=\tanh(ru),\qquad S^2+W^2=1.
```

```math
y_u^2-r^2y^2+\mu r^2y^4=0,\qquad y_{uu}=r^2y-2\mu r^2y^3.
```

The **first** equation is the zero-energy constraint, not the general second-order Master. Squaring an equation can introduce additional solutions. The **second** equation admits other energies and solutions; the linear reciprocal is only a zero-energy phenomenon. See [§3.3](reference/algebra-geometry/03-differential-structure/03-03-master-nonlinear.md) and [§3.8](reference/algebra-geometry/03-differential-structure/03-08-differential-interrelation.md).

## DLMF-inspired reference rules

Like the [NIST Digital Library of Mathematical Functions](https://dlmf.nist.gov/), the long-term organization uses topics, index entries, stable statement identifiers, explicit assumptions, derivations, inter-equation references, verification and errata. It does **not** copy DLMF chapter numbering or claim comparable independent editorial certification yet.

When adding or revising material, keep:

- **statement kind:** definition, proved identity, classical theorem, chosen construction, conditional correspondence, conjecture or model;
- **hypotheses:** domains, positivity, energy, regularity, branch and normalization, and necessary external data;
- **evidence:** full proof, finite symbolic/numerical check, counterexample, or named literature source;
- **logic:** distinguish implication from equivalence, local from global, and particular solution from general solution;
- **provenance:** stable claim ID, source file, original branch/commit, known corrections and source of externally imported mathematics.

**Beware historical label collision:** `[C]` meant “conjecture” in some materials and “selected construction” in others. Follow the local legend and migrate statuses to the unambiguous [claim registry](reference/CLAIM_REGISTRY.md). Avoid forced physics and speculative group/modular identifications.

## How to continue a mathematical investigation in another conversation

Ask for the **exact branch and source** to be opened, beginning at `REFERENCE_INDEX.md` and `AGENTS.md`. Search by claim ID, canonical formula and related topic; read the full relevant theorem and its local proof-audit notes. Report checked identities, corrections, open questions, and only then extend the algebra. Retain $`r`$ and $`c`$ explicitly, and cite the commit SHA for reproducibility.

A fresh chat will not automatically read these files. It needs access to GitHub through the available tools or a supplied file; the path and protocol provide the handoff, not a hidden shared memory.
