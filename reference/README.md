# Mathematical Reference

This directory contains the **canonical reading path** for the Symmetrical Framework on `main`. A directory's placement does not certify every sentence: consult each theorem's hypotheses, proof, verification notes and dependencies.

## Foundational documents

| Source | Current status | Coverage |
|---|---|---|
| [000 Introduction and Scope](foundations/000%20Introduction%20and%20Scope.md) | Foundational **draft**, individually proved statements | Scope, kernel, non-uniqueness of half splitting, evidence protocol |
| [010 Variables and Normalizations](foundations/010%20Variables%20and%20Normalizations.md) | Foundational **draft** | Log-coordinate, Jacobians, inversion, parameters and reference units |
| [020 Linear Exponential Backbone](foundations/020%20The%20Linear%20Exponential%20Backbone.md) | Foundational **draft** | Two-dimensional linear solution space, Gram invariant, Riccati and separatrix |
| [Algebra and Geometry reader's guide](algebra-geometry/README.md) | Revised mathematics with proof and correction ledgers | Four extended chapters |

The numbered foundational documents retain their existing stable `SF-I-` identifiers. The revised algebra-and-geometry materials are separately numbered and must not be silently assumed to share the same chapter IDs.

## The four reviewed algebra-and-geometry chapters

1. [Architectural identities](algebra-geometry/01-architectural-identities/01-00-summary.md) — exact kernel, logarithmic charts, Mellin links and auxiliary linearization.
2. [Foundational symmetries](algebra-geometry/02-foundational-symmetries/02-00-summary.md) — inversion, log-affine closure, weighted overlaps, information metric, group operations and Darboux partners.
3. [Differential structure](algebra-geometry/03-differential-structure/03-00-summary.md) — first-order constraint versus second-order Master, Jacobi elliptic families, reciprocal defects, Pinney, Kelvin, stationary KdV.
4. [Geometric properties](algebra-geometry/04-geometric-properties/04-00-summary.md) — critical points, arc length, genus, inversion, and constructed metrics/surfaces.

Consult the local `*-99-notes.md` proof/correction registers and [cross-chapter revision notes](algebra-geometry/PART_I_REVISION_NOTES.md). The evidence labels used in older files are not uniform; see [Claim Registry](CLAIM_REGISTRY.md).

## Shared navigation and mathematical conventions

- [Reference Index](../REFERENCE_INDEX.md): first entry point and all-subject navigation
- [Notation](NOTATION.md): canonical coordinates, dependent variables, energy, derivative conventions
- [Claim Registry](CLAIM_REGISTRY.md): selected statement identifiers and proof locations
- [AGENTS.md](../AGENTS.md): source-recovery instructions for future assistant sessions
- [MARKDOWN_STYLE.md](../MARKDOWN_STYLE.md): required GitHub dollar-backtick inline math and display-fence layout

## Reproducibility and limitations

The moved Part I includes `verify_part_i.py`, `verify_chapter2.py`, `verify_chapter3.py`, and `check_markdown_style.py` inside `algebra-geometry/`. These scripts test particular formulas and code conventions; a passing run is not a proof of every statement in a research program.

For material that has **not** been reviewed claim by claim, use [Research](../research/README.md); for legacy interpretations that should not be treated as valid deductions, use [Archive](../archive/README.md).

**No forced interpretations:** a geometric realization, physical analogy or modular construction requires independent definitions and hypotheses; an elementary kernel does not determine all such structures uniquely.

## Dependency-based recursive review

The [Foundational Atlas](atlas/README.md) supplies a versioned object/parameter dictionary and typed transformation contracts. The [review protocol](atlas/REVIEW_PROTOCOL.md) and [read-only impact checker](atlas/validate_registry.py) permit iterative correction: inspect one definition, evaluate the downstream dependency graph, recheck only affected contracts and proofs, then update the claim registry. This atlas is an initial source extraction and is not a substitute for the numbered proofs.
