# 00 — Foundational mathematical objects

**Layer:** primitive definitions, exact algebra and typed transformations. Nothing in this directory implies that a physical model or geometric realization is uniquely determined by the kernel.

Read in order: [variables and parameters](00-01-variables-parameters.md) → [functions and conics](00-02-functions-conics.md) → [Gram and projective envelopes](00-03-gram-projective.md) → [pullbacks and transformations](00-04-pullbacks-transformations.md) → [identity register](00-05-identities.md).

The extended machine-readable object/parameter/contract register already lives in [reference/atlas](../../reference/atlas/README.md). This chapter gives **human-readable proofs and notation**, not a competing registry.

## Scope boundaries

The functions $`f,S,W,R,b,P`$ and their algebraic or first-derivative identities are here. The **Master second-order ODE and its Classification Theorem** are in [01-master-equation](../01-master-equation/README.md), because a selected profile solving an ODE does not define all solutions of that ODE. Norms and measures receive their own [chapter 02](../02-calculus-norms/README.md). The selected canonical-surface immersion is in [chapter 05](../05-differential-geometry/README.md), with clearly stated additional geometric inputs.

**Evidence:** [Foundation 010](../../reference/foundations/010%20Variables%20and%20Normalizations.md), [Foundation 020](../../reference/foundations/020%20The%20Linear%20Exponential%20Backbone.md), revised [Part I Chapters 1–2](../../reference/algebra-geometry/README.md), and Complete Reference v2 §F.1–F.4.

**Active parameters:** $`r`$ and $`c`$ may be differentiation variables. The [multivariable calculus and Gudermannian charts](00-06-variable-parameter-derivatives.md) record the held-fixed coordinate, parameter and Jacobian conventions.

**Differential closure and oscillator hierarchy:** [§00.07](00-07-differential-algebra-oscillator-hierarchy.md) derives the exact second-order equations of $`S,W,R,b,P,\mathcal B,J_0,J_G`$ from the common exponential differential field, the continuous `H_q=S^q` separatrix ladder and the beta-normalized cumulatives `Q_q=I_P(q,q)`. This is an algebraic hierarchy; all-energy Master orbits are discussed separately in [§01.04](../01-master-equation/01-04-log-derivative-companion.md).

**New detailed conic atlas:** [§00.08 — Circle, hyperbola, parabola and Gudermannian](00-08-projective-conics-gudermannian.md) reproduces the requested four-row coupled-oscillator table, with $`\mathcal B=S^2`$ replacing the screenshot's local $`B=S^2`$. The latter conflicts with the stable Gram coefficient $`B`$ (Atlas `SF-P-009`). The paper's local alternative $`B_0=S^2`$ is documented, not promoted as a global symbol.
