# The Symmetrical Framework

*A mathematical research reference for a kernel on the positive multiplicative line.*

**Start at [REFERENCE_INDEX.md](REFERENCE_INDEX.md).** For other ChatGPT conversations or code assistants, read [AGENTS.md](AGENTS.md) and the notation/claim registry linked there. This repository is designed to be useful **without relying on a previous chat window's memory**.

## Defining object

For $`x,c,r>0`$, define

```math
f(x;r,c)=\frac{c^r x^{r-1}}{c^{2r}+x^{2r}}=\frac{1}{2x}\mathrm{sech}(r\log(x/c)).
```

The center $`x=c`$ exactly half-splits the positive integral:

```math
\int_0^c f(x;r,c)\,dx=\int_c^\infty f(x;r,c)\,dx=\frac{\pi}{4r}.
```

**Non-uniqueness warning:** a positive continuous function is **not** uniquely characterized by half-splitting alone. Uniqueness statements require additional equations, regularity, normalization or global hypotheses. The canonical logarithmic variable is always $`u=\log(x/c)`$, with $`r`$ and $`c`$ explicit.

## Three repositories of knowledge — one branch

| Directory | Editorial role | What to expect |
|---|---|---|
| [reference/](reference/README.md) | **Mathematical reference** | Stable introductory definitions, mathematically revised Chapter 1–4 proofs, notation and a claim registry; status belongs to individual statements |
| [research/](research/README.md) | **Provisional investigations** | Current numbered mathematical drafts, historical Parts II–VI/VIII, and older identity/theorem compilations to audit |
| [archive/](archive/README.md) | **Historical or over-interpreted sources** | The former Part VII moonshine/K3/phenomenology collection, preserved intact but not accepted as derived mathematics |

The old branches, including [feat/part-i-rigorous-revision](MIGRATION.md) and other development lines, remain unchanged as backups. The active source of truth and entry point is now the default **main** branch.

## Begin studying the mathematics

Read [Foundational scope and warning on uniqueness](reference/foundations/000%20Introduction%20and%20Scope.md), [variables and normalizations](reference/foundations/010%20Variables%20and%20Normalizations.md), and [linear exponential backbone](reference/foundations/020%20The%20Linear%20Exponential%20Backbone.md) first. These foundational documents retain their **draft** metadata.

Then continue with the [Algebra and Geometry guide](reference/algebra-geometry/README.md): algebraic identities, inversions and probability, the nonlinear Master and Jacobi energy families, and carefully specified geometric constructions. The earlier Part I proof and correction ledgers are preserved.

The [Claim Registry](reference/CLAIM_REGISTRY.md) maps selected formulas to their proofs. [Canonical notation](reference/NOTATION.md) separates $`u`$, $`\xi=x/c`$, $`\theta=ru`$, the coupling $`\mu`$, and the conserved Master energy.

## Editorial standard and provenance

Follow [MARKDOWN_STYLE.md](MARKDOWN_STYLE.md) for GitHub-compatible inline dollar-backtick math and unindented, single-line displayed equations. The [migration record](MIGRATION.md) documents old paths, backup commits and the move policy.

This is a mature **research program with an explicit evidence protocol**, not a claim that every historical exploration is true, novel, or physically realized. A correspondence with solitons, K3 surfaces, modular forms or other mathematical structures is accepted only after its independent definitions and hypotheses are proved.

**New ChatGPT conversation?** Provide this repository URL and ask the assistant to read `REFERENCE_INDEX.md` and `AGENTS.md` on `main` first. The files do not automatically enter a new conversation unless the assistant can access the repository.

## Mathematical object and transformation atlas

The [Foundational Atlas](reference/atlas/README.md) is the growing machine-readable dictionary of mathematical objects, **scoped variables and parameters**, and typed transformations extracted from the November 16 complete reference. Each transformation records its source and target coordinates, parameter rules, Jacobian or time-differential rule, domain, invertibility, and information loss. It can be reviewed incrementally without automatically rewriting unrelated proofs.
