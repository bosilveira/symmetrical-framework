# Ordered recursive review queue

**Status:** initial mathematical consolidation. No claim that all historical sources have been peer-reviewed or proved by their location in the new tree.

| Batch | Scope | First target | Review gate |
|---|---|---|---|
| A | Foundational objects | [variables](00-foundations/00-01-variables-parameters.md), [kernel](00-foundations/00-02-functions-conics.md), [Gram](00-foundations/00-03-gram-projective.md) | Scoped parameter IDs, center and coupling collisions |
| B | Master / classification | [Master](01-master-equation/01-01-operator-energy.md), [Theorems 4.1–4.2](01-master-equation/01-02-classification.md), [general level](01-master-equation/01-03-general-levels.md) | Global real C², weighted norms, all parameter signs, first-order plateau |
| C | Calculus / norms | [calculus](02-calculus-norms/README.md), [norm identity](02-calculus-norms/02-03-norms.md) | Correct Jacobians and convergence endpoints; different Hilbert measures |
| D | Integral transforms | [Mellin/Fourier/Plancherel](03-transforms-special-functions/03-01-mellin-fourier-plancherel.md), [other transforms](03-transforms-special-functions/03-02-transform-registry.md) | Consistent kernels, strips, boundary conventions and inverses |
| E | Probability | [normalized law](04-probability-statistics/04-01-distribution.md) | Density pushforwards, moments and statistical parameter scopes |
| F | Differential geometry | [metric pullback](05-differential-geometry/05-01-canonical-surface.md), [forms](05-differential-geometry/05-02-fundamental-forms.md), [connections](05-differential-geometry/05-03-connections-operators.md) | Independent immersion data and local/global qualifications |
| G | Secondary theories | [secondary index](06-secondary-theories/README.md) | Operator domains, spectral/variational choices, conditional maps |
| H | Applications | [outer layer](07-applications/README.md) | Independently specified models and external verification |

## Safe update algorithm

Freeze the current `main` commit; open the exact primary source and its errata; bind all independent and dependent variables, parameters and energy constants; prove or test the specific identity; run the [Atlas impact report](../reference/atlas/README.md) as a **review queue**; update the new chapter and its source record; check Markdown, links, and the diff; commit a narrow change. Do not automatically rewrite the older `reference/`, `research/`, or `archive/` corpora.

## Important collisions

The paper shorthand `u=ln(x)` needs a reference unit and a center, while our canonical `u=log(x/c)` is dimensionless. Older ZIP sources also used `u=x^q f` for a **dependent field** (later clarified to `U_q`). The cubic energies `epsilon_N`, `epsilon_H` and `epsilon_U` have different conventions. The norm-power family differs from the intrinsic level family unless its shape rate and amplitude are converted. The canonical-surface Maurer–Cartan, Levi-Civita and Weitzenböck connections are not the same connection.

## Latest mathematical review targets

- **Algebraic closure and named oscillators:** [§00.07](00-foundations/00-07-differential-algebra-oscillator-hierarchy.md), including the general normalized incomplete-beta cumulative `Q_q` and its recurrence (proof-bearing direct calculus).
- **Master at arbitrary energy:** [§01.04](01-master-equation/01-04-log-derivative-companion.md), including the logarithmic-derivative Duffing equation, its energy relationship, sign/zero restrictions and the degree-two quotient's time differential (foundational paper Proposition 9.7(a)).
- **Parameter ID review:** name clashes of `Q` among cumulative, spectral potential, charge, quartic and logarithmic slope must be resolved with **scope** before a new stable ID is assigned. Do not treat all external correspondences or entire source chapters as automatically approved.
