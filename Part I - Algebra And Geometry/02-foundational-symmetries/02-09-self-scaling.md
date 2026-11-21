# 2.9 — Self-similar scaling versus fixed-$`c`$ dilation

For $`\lambda>0`$, direct substitution proves

```math
f(\lambda x;r,c)=\lambda^{-1}f(x;r,c/\lambda).
```

This is equivalent to $`f(\lambda x;r,\lambda c)=\lambda^{-1}f(x;r,c)`$, with the parameter $`r`$ unchanged.

At fixed $`c`$, $`x\mapsto\lambda x`$ translates the canonical coordinate:

```math
\log(\lambda x/c)=u+\log\lambda.
```

In general the function $`x\mapsto f(\lambda x;r,c)`$ is **not** $`\lambda^{-1}f(x;r,c)`$: the shift is compensated only by the scale change $`c\mapsto c/\lambda`$.

Differentiate the scaling identity at $`\lambda=1`$ to recover

```math
x\partial_x f=-f-c\partial_c f.
```

No fractal structure or renormalization-group flow follows from this ordinary homogeneity relation alone. Such interpretations would need an independent dynamical or iterative construction.

## Parameter flow versus pointwise invariance

Let $`\alpha=\log c`$ and $`\ell=\log\lambda`$. The coordinate dilation $`x\mapsto\lambda x`$ at fixed $`c`$ sends the center displacement $`u`$ to $`u+\ell`$, but the **simultaneous** transformation $`(x,c)\mapsto(\lambda x,\lambda c)`$ leaves $`u`$ unchanged.

The exact infinitesimal response at fixed $`r`$ is

```math
\left.\frac{d}{d\ell}\log f(e^\ell x;r,c)\right|_{\ell=0}=-(1+rW(x;r,c)).
```

On the other hand, moving the scale alone at fixed $`x`$ produces

```math
\left.\frac{d}{d\ell}\log f(x;r,e^\ell c)\right|_{\ell=0}=rW(x;r,c).
```

The sum of these responses is $`-1`$, precisely the degree of Euler homogeneity. The two deformations are not interchangeable unless both the coordinate and the parameter update are included.

## Composition of power transports

The general closure theorem from [§2.5](02-05-power-transformation.md) is stable under composition. Start with a distribution centered at $`c`$ and apply first $`Y=d(X/c)^a`$, then $`Z=e(Y/d)^b`$ with nonzero real $`a,b`$. Direct substitution gives

```math
Z=e(X/c)^{ab},\qquad r_Z=\frac{r}{|ab|}.
```

Thus nonzero power transports in log coordinates compose by multiplication of exponents, and their inverses use $`a^{-1}`$. The parameters $`c,d,e`$ specify the current centers; ignoring those updates leads to dimensionally incorrect transformations. This is a deterministic equivalence of probability families, not an autonomously evolving renormalization-group trajectory.
