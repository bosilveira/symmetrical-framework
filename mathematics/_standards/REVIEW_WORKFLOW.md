# Recursive Mathematical Review Protocol

**Goal:** a correction in one definition should produce a *targeted review queue*, never an automatic rewrite of all descendants or a sweeping assertion that the whole framework has changed.

## Dependency sequence

1. **Locate the exact source claim** and its corrections, not just a summary or a chat recollection.
2. **Bind notation:** independent/dependent variables; log coordinate $`u=\log(x/c)`$; $`r,c,\mu`$; any source-local coefficient or integration constant.
3. **Select the primary mathematical layer:** foundations → Master/classification → calculus/norms → transforms → probability → differential geometry → secondary constructions → applications.
4. **Verify the statement:** algebra, hypotheses, boundaries, proof, and counterexamples; check norm and transform conventions.
5. **Register the map:** source/target object IDs, coordinate Jacobian, derivative transformation, parameter change, preserved invariants and information lost. Use [the existing Atlas](../../reference/atlas/README.md) rather than creating another parameter registry.
6. **Inspect dependent IDs** using the Atlas impact checker. Dependence means “review,” not “automatically alter.”
7. **Publish one corrected primary proof**, then update its local proof audit and linked claim status. Leave historical source text unchanged.
8. **Validate** Markdown, equations, links, tests and exact Git diff. Preserve older branch heads as backups.

## Three graphs must remain separate

| Graph | Edge meaning | May contain cycles? | Used for |
|---|---|---|---|
| Derivation graph | One definition or theorem uses another | No, for the selected derivation dependency order | Impact and safe review order |
| Transformation graph | Defined map, quotient, change of variable, or specialization | Yes | Contracts, inverse, and loss of data |
| Evidence graph | Claim ↔ proof/test/source/erratum | Yes | Status, corrections and provenance |

Never confuse a theorem's logical converse with inversion of a **function**. The reciprocal $`J=1/y`$ is pointwise invertible on a nonvanishing interval, whereas the assertion $`J_{uu}=r^2J`$ requires the specific **zero-energy** Master branch.

## Review labels

- **Definition:** an explicitly made choice.
- **Proved:** a complete argument under the listed hypotheses.
- **Derived locally:** exact construction with a specified chart.
- **Literature theorem:** externally established with matching assumptions.
- **Computationally checked:** finite symbolic/numeric verification, not a universal proof.
- **Provisional:** plausible or source-only claim awaiting full proof.
- **Refuted/superseded:** contradicted or replaced, with the reason preserved.

A named theory (Ermakov–Pinney, Friedmann, Yang–Mills, Moonshine, etc.) is never a status label. If the mathematical object exists only after choosing additional structure, it belongs in the secondary or application layer.

## Release gates for a chapter

The chapter must have: notation table or link with stable parameter IDs; one main theorem/definition per anchored section; source citations to **exact paths**; nontrivial variable changes with Jacobians; restrictions and boundary cases; tests when appropriate; and a list of *unreviewed* material still outside the chapter.

Only then may the chapter be marked **reviewed**. A chapter-level status cannot silently promote all statements inherited from an older research source.
