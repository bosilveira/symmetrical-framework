# Symmetrical Framework — New Mathematical Reference

**Editorial stage:** new parallel structure, established 21 November 2026. This directory is the **future review surface**, not a replacement for [reference/](../reference/README.md) or [research/](../research/README.md). All older files remain where they are. The purpose is to promote reviewed mathematical claims **in dependency order**.

The project has many more sources than a reader should encounter at once. Read the **mathematical foundation before its realizations**. A source file's age, mathematical vocabulary, or [V] check status does not determine whether it is canonical. Every proposition carries domain, notation, proof status and a precise provenance path.

## Reading order

| Stage | Directory | Mathematical scope | Promotion criterion |
|---|---|---|---|
| 0 | [00-foundations/](00-foundations/README.md) | Variables, parameters, primitive functions, conics, logarithmic and other pullbacks, transformations, algebraic identities | Explicit typed definitions and checked algebra |
| 1 | [01-master-equation/](01-master-equation/README.md) | The *second-order* Master, its conserved energy and the global finite-norm Classification Theorem; general levels | Full proof, global hypotheses and norm identity |
| 2 | [02-calculus-norms/](02-calculus-norms/README.md) | Derivatives, primitives, weighted and unweighted norms, integration measures and Hilbert spaces | Convergence conditions and measure/Jacobian checks |
| 3 | [03-transforms-special-functions/](03-transforms-special-functions/README.md) | Mellin, Fourier, Parseval/Plancherel, Laplace, Stieltjes, Hilbert and other transforms | Kernels, conventions, domains and boundaries |
| 4 | [04-probability-statistics/](04-probability-statistics/README.md) | Normalized kernel, distributions, moments, information measures and statistics | Probability normalization and explicit pushforwards |
| 5 | [05-differential-geometry/](05-differential-geometry/README.md) | Geometric dictionary, metric pullbacks, fundamental forms, Gauss–Codazzi, canonical-surface charts | All additional geometry and global qualifications typed |
| 6 | [06-secondary-theories/](06-secondary-theories/README.md) | Sturm–Liouville, Ermakov–Pinney, Euler–Lagrange, Jacobi/Lamé, Lax/Miura and other *constructed* second-order theories | Proved map from foundation to specified external structure |
| 7 | [07-applications/](07-applications/README.md) | Models, number theory, broader modular geometry, and physical interpretations | Independent assumptions, sources and concrete claimed consequences |

Stages 0–5 are **mathematical foundation and its directly specified structures**. They are not assertions that a surface or Hilbert space is uniquely forced by a scalar kernel. Secondary theories and applications are explicitly marked as **conditional constructions**.

## Mandatory dependency rule

The first obligation for a transformation is **variable and parameter binding**. This includes source and target coordinate, independent/dependent variables, Jacobian, coupling, normalization, conserved energy, domain/branch, and any information lost. The [typed registry](../reference/atlas/README.md) already provides object, parameter and map IDs; this new tree **reuses those IDs**, rather than generating a conflicting second database. See [transformation contract standard](_standards/TRANSFORMATION_TEMPLATE.md).

**Do not duplicate source-of-truth formulas unnecessarily.** Put the primary proof in the appropriate numbered chapter, then link its stable claim ID from related chapters. If a concept appears in multiple layers, preserve one primary definition and provide typed pullbacks or derived references.

## Existing source baseline

- [Foundational paper v0.3](../research/source-snapshots/2026-11-21/README.md) — theorem §§3–4 and general-level §4.1; original draft supplied as a Project source.
- [Current mathematical reference](../reference/README.md) — revised algebra/geometry Chapters 1–4, with correction ledgers.
- [Canonical surface differential-geometry draft](../research/active-drafts/030%20Connections%20and%20Differential-Geometric%20Operators%20of%20the%20Canonical%20Surface.md) — provisional but detailed typed pullback/connection derivations.
- [Latest source crosswalk](../reference/atlas/SOURCE_CROSSWALK_2026-11-21.md) — November 16 ↔ November 21 notation, energy and level conversions.
- [Review and promotion workflow](_standards/REVIEW_WORKFLOW.md) and [source map](SOURCE_MAP.md).

**Migration policy:** start with additive Markdown files; leave older documents and backup branches intact. No automatic recursive text edits. After each batch: validate formulas, compute dependent review queue, update links and claim status, then commit.
