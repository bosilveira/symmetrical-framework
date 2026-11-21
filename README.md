# The Symmetrical Framework

*A mathematical investigation of a conformal algebraic kernel on the positive multiplicative half-line.*

**Start with the [Reference Index and Research Protocol](REFERENCE_INDEX.md).** Future assistants should also consult [AGENTS.md](AGENTS.md) and the [GitHub mathematics conventions](MARKDOWN_STYLE.md) before using this repository as a source.

The original object is defined for $`x,c,r>0`$ by

```math
f(x;r,c)=\frac{c^r x^{r-1}}{c^{2r}+x^{2r}}=\frac{1}{2x}\mathrm{sech}\!\left(r\log(x/c)\right).
```

Its positive integral is split equally at $`x=c`$:

```math
\int_0^c f(x;r,c)\,dx=\int_c^\infty f(x;r,c)\,dx=\frac{\pi}{4r}.
```

**Qualification:** this half-splitting property **does not uniquely characterize the function** among positive continuous integrable functions. Additional equations, normalization and/or global hypotheses are required for uniqueness claims. This distinction is proved and discussed in the foundational series.

## Two complementary research branches

- **`main` (default):** [numbered foundational reference](01-foundational/000%20Introduction%20and%20Scope.md), [variables and normalization](01-foundational/010%20Variables%20and%20Normalizations.md), [exponential linear backbone](01-foundational/020%20The%20Linear%20Exponential%20Backbone.md), and the [draft investigation archive](draft/README.md). These chapters presently identify themselves as **draft**.
- **`feat/part-i-rigorous-revision`:** the [broader eight-part research tree](https://github.com/bosilveira/symmetrical-framework/tree/feat/part-i-rigorous-revision) and the extensively revised [Part I reader's guide](https://github.com/bosilveira/symmetrical-framework/blob/feat/part-i-rigorous-revision/Part%20I%20-%20Algebra%20And%20Geometry/README.md). This branch is **not** merged into `main`; its later Parts and historical summaries have varying verification status.

The intended long-term organization is **DLMF-inspired**: stable mathematical identifiers, precise assumptions, numbered formulas and proofs, linkable sources, verification and errata, and a separate research archive. The [Reference Index](REFERENCE_INDEX.md) explains the staged migration without breaking existing links.

This is mathematical research and an evolving reference, **not** an assertion that every exploratory interpretation is proved or novel.
