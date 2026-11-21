# Chapter 2 — Mathematical verification, source review and scope

**Expanded audit · 20 November 2026.** Chapter 2 retains the original topics (§§2.1–2.11), adds three independent extensions (§§2.12–2.14), and makes previously implicit assumptions, measures, transformation parameters and domains explicit.

## Verified source-derived assertions

The former 182-line `02-gemini.md` source was fully reviewed before deletion. It covered center jets, joint and fixed-scale homogeneity, reciprocal and half-Cauchy closure, and the two-scale product; each source-supported result is established in the numbered sections, with useful additional algebraic steps preserved. The deleted file remains recoverable from [the preceding Git revision](https://github.com/bosilveira/symmetrical-framework/blob/6312bf40e8e99c84e141cdc96bd83d0e3df05251/Part%20I%20-%20Algebra%20And%20Geometry/02-foundational-symmetries/02-gemini.md). The source does **not** establish the log-affine action, weighted overlap, Fisher geometry, or Darboux scattering; these are independent mathematical extensions, not claims attributed to Gemini.

| Assertion | Status | Location |
|---|---|---|
| $f(c)=1/(2c)$, $f_x(c)=-1/(2c^2)$, $f_{xx}(c)=(2-r^2)/(2c^3)$ | [E], exact | [§2.1](02-01-symmetry-point.md) |
| Exceptional $r=\sqrt2$ center inflection, because $f_{xxx}(c)=3/c^4$ | [E], additional derivation | [§2.1](02-01-symmetry-point.md) |
| Inversion covariance and correct oriented versus unsigned measure | [E] | [§2.2](02-02-moebius-symmetry.md) |
| Joint scaling, Euler equation and commuting group actions | [E] | [§2.3](02-03-euler-homogeneity.md) |
| $1/X$ has scale $1/c$; $c^2/X$ preserves the law; reflected Mellin moments | [E] in their convergence strip | [§2.4](02-04-reciprocal-closure.md) |
| Half-Cauchy reduction and full $a\ne0$ power closure $r\mapsto r/|a|$ | [E], generalized transformation | [§2.5](02-05-power-transformation.md) |
| Two-scale, mixed-resolution and $n$-scale product-to-sum identities | [E] | [§2.6](02-06-hyperbolic-double.md), [§2.7](02-07-hyperbolic-triple.md) |
| Two distinct $Q$ conventions; Darboux zero mode and reflectionless partner | [E/K] under stated operator domains | [§2.8](02-08-superpotential-antisymmetry.md) |
| Fixed-center scaling versus joint scaling and power-composition law | [E] | [§2.9](02-09-self-scaling.md) |
| Restricted CDF-angle addition is **partial**, not a group | [E] | [§2.10](02-10-cdf-addition.md) |
| Global multiplicative CDF, phase and logistic group charts | [E] | [§2.11](02-11-cdf-product.md) |
| Log-affine action on normalized family | [E/K], new section | [§2.12](02-12-log-affine-group.md) |
| Exact weighted overlap and strictly positive-definite kernel | [E/K], new section | [§2.13](02-13-weighted-overlap.md) |
| Fisher metric with $K_F=-8/\pi^2$ | [E/K], new section | [§2.14](02-14-fisher-information.md) |

## Main corrections and caveats

1. The **unsigned** measure $f(x)\,dx$ is preserved by inversion using the absolute Jacobian; the **oriented** form changes sign; $f(x)\,dx/x$ is not invariant. Each assertion is formulated separately.
2. The normalized profile $S(u)$ is even, but the pointwise function $f(x)$ is not. The function $f$ has an interior maximum only for $r>1$, generally away from $c$.
3. The value $f_{xx}(c)$ is a second derivative, **not** the signed Euclidean curvature of the numerical graph $(x,f(x))$, which would include the factor $(1+f_x^2)^{-3/2}$.
4. The historical phrase “interaction identity” means an algebraic **product**, not coupling of independently evolving solutions.
5. The arctangent-angle CDF operation has a boundary at $F=1$; it is not globally closed and has no finite positive identity. The group law in §2.11 is a different operation with a different coordinate construction.
6. The spatial superpotential $Q_x$ and logarithmic $Q_u$ differ by both coordinate transformation and normalization; their Schrödinger operators must not be conflated.
7. The log-affine symmetry transports the **normalized probability family**, changing the resolution under nonunit powers. It does not assert pointwise invariance of an individual function.
8. The weighted overlap is computed in $L^2((0,\infty),x\,dx)$, not ordinary $L^2(dx)$. The Fisher metric is computed from the **normalized law**, not from profile overlap; their scale coefficients differ.
9. The hyperbolic Fisher metric is a classical location-scale phenomenon. A curvature statement always needs its own explicit metric, and none of these constructions forces a gravitational, octonionic or higher-dimensional geometric interpretation.

## Mathematical derivations and reproducibility

The [Chapter 2 verification script](../verify_chapter2.py) checks representative symbolic identities and numerical values, including the weighted overlap for unequal scales, the Fisher integrals, covariance under power maps, group laws and Darboux factorization. Like every computational test, it is evidence for its stated cases, not a substitute for the proofs supplied in the chapter.

**Dependencies:** Chapter 1 supplies $S$, $W$, the Mellin transform, normalization and the canonical coordinate. Chapter 3 develops the nonlinear Master and the auxiliary reciprocal; Chapter 4 classifies global inflection points. The new Chapter 2 results refer to the specific positive kernel or its normalized law, not arbitrary nonzero-energy Master solutions.

## Open questions, stated separately

- Analyze extensions of the weighted overlap to **unequal** resolutions $r_1\ne r_2$; the general product identity is known, but the simple $\delta/\sinh\delta$ formula requires equal $r$.
- Determine which additional functional identities arise from the positive-definite kernel under scale mixtures while maintaining explicit normalization and convergence hypotheses.
- Compare Fisher, Hellinger and weighted-Hilbert metrics under a single declared coordinate chart; their distinct coefficients must be preserved rather than identified.

No claim of novelty follows merely from recording these exact identities.

## Completed Gemini-source integration and deletion

The discarded draft's internal numbering was “Theorem 4.1–4.6”; those labels have **not** been copied into Chapter 2 because its existing numbering already has a consistent structure. Mathematical source coverage is:

| Draft theorem | Verified outcome and disposition |
|---|---|
| 4.1 Center value, slope and “curvature” | Direct quotient rule and Taylor proof retained in [§2.1](02-01-symmetry-point.md); “curvature” corrected to $f_{xx}(c)$, not Euclidean graph curvature |
| 4.2 Euler homogeneity | Direct factorization and infinitesimal equation retained in [§2.3](02-03-euler-homogeneity.md) |
| 4.3 Self-similar scaling | Fixed-$c$ argument and the necessary $c\mapsto c/\lambda$ parameter update retained in [§2.3](02-03-euler-homogeneity.md) and [§2.9](02-09-self-scaling.md) |
| 4.4 Reciprocal closure | Full change-of-variables Jacobian proof retained in [§2.4](02-04-reciprocal-closure.md) |
| 4.5 Half-Cauchy power transform | Full Jacobian cancellation retained in [§2.5](02-05-power-transformation.md), alongside the stronger all-nonzero-powers theorem |
| 4.6 Two-scale product | Explicit sum/difference of the two hyperbolic arguments retained in [§2.6](02-06-hyperbolic-double.md); its quoted triple product was already proved in [§2.7](02-07-hyperbolic-triple.md) |

The source's explanatory phrase “multiplicative interaction” has been retained only as a label for ordinary pointwise multiplication, **not** as evidence for a physical coupling. Its unqualified statement that every curve has a common tangency point is valid only **with $c$ fixed**. The draft’s Taylor expansion was made mathematically precise at fixed $r,c$ using big-$O$ remainders. These qualifications and the separate new findings are recorded in this audit, so deleting the redundant working file does not discard the proof trajectory.

**Provenance:** the complete draft is preserved in Git history at the preceding commit. Its deletion is a cleanup of the active mathematical reference, not an assertion that the earlier authoring process supplied novel results.
