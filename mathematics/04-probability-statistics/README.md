# 04 — Probability and statistics derived from the kernel

**Scope:** the probability distribution is an **explicit normalization** of the original positive kernel; statistical moments and information geometry require that probability measure and the correct parameter derivatives. They do not follow from an unnormalized cubic Master orbit without further assumptions.

Start with [normalized density and pushforward laws](04-01-distribution.md). Higher-order cumulants, entropy, Fisher metrics, products/convolutions and statistical transforms are currently reviewed **source-by-source**, using [legacy Part III](../../research/legacy-parts/Part%20III%20-%20Probability%20and%20Statistical%20Mechanics/07-statistical-information/12-01-logarithmic-cumulants.md), and are not automatically accepted.

For a statistical parameter $`c`$ estimated from data, the distinction between “$`c`$ held fixed in $`\partial_x`$” and “$`c`$ differentiated in a score” is indispensable. Likewise, the Fisher log-location $`\xi_F=\log(c/c_{\rm ref})`$ is not the original spatial ratio $`\xi_x=x/c`$.

**Foundations:** [integration](../02-calculus-norms/02-02-primitives.md), [norms](../02-calculus-norms/02-03-norms.md), and the [parameter register](../../reference/atlas/registry.json).

**Conic/Gudermannian probability dictionary:** [§04.02](04-02-gudermannian-conic-laws.md) derives a uniform Gudermannian angle under the normalized original kernel, its arcsine/Cauchy/half-Cauchy pushforwards, and the beta-law hierarchy for squared profiles. The **logarithmic pushforward** of the original-kernel measure is exactly the $`q=1/2`$ specialization of the normalized $`S^{2q}`$ family; the classification-norm measure corresponds to $`q=1`$. The squared field is $`\mathcal B=S^2`$, **not** the backbone coefficient $`B`$.
