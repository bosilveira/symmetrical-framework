# 02.04 — Measures and Hilbert-space pullbacks

**Status:** direct measure theory and Hilbert-space constructions; distinguish a *defined* Hilbert space from a claim that a particular differential operator is self-adjoint on it.

## Spatial to logarithmic measure

At fixed $`c>0`$, $`u=\log(x/c)`$,

```math
dx=x\,du,\qquad \frac{dx}{x}=du,\qquad x\,dx=x^2\,du,\qquad x^{2q-1}dx=x^{2q}du.
```

Therefore the map $`\mathcal U_qF(u)=x^qF(ce^u)`$ defines an **isometry** between

```math
L^2((0,\infty),x^{2q-1}dx)\quad\mathrm{and}\quad L^2(\mathbb R,du)
```

for any real $`q`$ for which the spaces and fields are defined. The inverse is $`(\mathcal U_q^{-1}g)(x)=x^{-q}g(\log(x/c))`$. For $`q=1`$, the Master amplitude $`y=2xF`$ is exactly $`2\mathcal U_1F`$, so it multiplies the norm by $`2`$.

## Haar vs Lebesgue vs probability measure

The multiplicative Haar measure $`dx/x`$ is invariant under $`x\mapsto\lambda x`$ at fixed $`\lambda>0`$. The positive kernel measure $`f(x)\,dx`$ is a different measure: it is inversion-invariant about $`c`$ in the positive-measure sense, but it is **not** simply $`dx/x`$.

A probability measure is obtained by normalizing $`f\,dx`$: $`\rho(x)\,dx=(2r/\pi)f(x)\,dx`$. Its log-coordinate density is $`(r/\pi)\mathrm{sech}(ru)`$. See [probability](../04-probability-statistics/04-01-distribution.md).

## Operator domains are additional data

A differential expression such as $`-\partial_u^2+r^2`$ does not by itself specify a self-adjoint operator; one must declare the Hilbert space and operator domain/boundary conditions. Those are treated in [secondary theories](../06-secondary-theories/README.md). Norm identities proved here are independent of a speculative Sturm–Liouville or spectral interpretation.

**Related results:** [Mellin Plancherel](../03-transforms-special-functions/03-01-mellin-fourier-plancherel.md), [Classification Theorem](../01-master-equation/01-02-classification.md).
