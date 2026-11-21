# 04.02 — Gudermannian pushforwards: uniform, Cauchy, arcsine and beta laws

**Status:** exact probability-measure pushforwards of the foundational conic chart, with distinct normalizations kept explicit. The original positive kernel is $`f(x;r,c)=\mathrm{sech}(r\log(x/c))/(2x)`$ with $`x,c,r>0`$ and logarithmic coordinate $`u=\log(x/c)`$. See [the canonical conic/Gudermannian dictionary](../00-foundations/00-08-projective-conics-gudermannian.md) and [the primary kernel probability definition](04-01-distribution.md).

## 1. Two measures that must NOT be conflated

### A. Original-kernel probability measure

With respect to $`dx`$, define

```math
d\mathbf P_{\rm ker}(x)=\rho_X(x;r,c)\,dx=\frac{2r}{\pi}f(x;r,c)\,dx,\qquad \int_0^\infty d\mathbf P_{\rm ker}=1.
```

The transformation $`x=ce^u`$ gives $`f\,dx=\frac12S\,du`$; the Gudermannian angle $`\eta=\mathrm{gd}(ru)`$ satisfies $`d\eta=rS\,du`$. Therefore

```math
\rho_X(ce^u;r,c)\,ce^u\,du=\frac r\pi S\,du=\frac{d\eta}{\pi},\qquad -\frac\pi2<\eta<\frac\pi2.
```

**Theorem (uniform Gudermannian angle):** the pushforward of the normalized original kernel measure under $`x\mapsto\eta=\mathrm{gd}(r\log(x/c))`$ is the **uniform distribution on $`(-\pi/2,\pi/2)`$**. In the angle coordinate the dependence on $`r,c`$ disappears because they have been absorbed into the random-variable transformation; this does not mean the original $`X`$-distribution is parameter-free.

### B. General normalized *squared-profile* measure

For every real $`q>0`$ define the **different** probability measure on the logarithmic line:

```math
d\mathbf P_q(u)=\frac{r\,\mathrm{sech}^{2q}(ru)}{B(\frac12,q)}\,du.
```

The beta integral proves normalization. In the Gudermannian chart it becomes

```math
d\mathbf P_q(\eta)=\frac{\cos^{2q-1}\eta}{B(\frac12,q)}\,d\eta.
```

For general $`q`$ this is a **power-weighted squared-profile measure**, not automatically the original $`f(x)\,dx`$ measure. There is, however, an important **exact specialization**:

```math
(u=\log(x/c))_*\mathbf P_{\rm ker}=\mathbf P_{1/2},\qquad B\left(\frac12,\frac12\right)=\pi,\qquad \rho_X(ce^u;r,c)\,ce^u\,du=\frac r\pi S\,du=\frac{rS^{2(1/2)}}{B(1/2,1/2)}\,du.
```

Thus the **logarithmic pushforward** of the original kernel is the $`q=1/2`$ member of the power-density hierarchy, whereas the normalized **classification-norm density** is the $`q=1`$ member. Their beta laws differ precisely because their power exponents differ. The pushforward by $`P=(1+\sin\eta)/2`$ has law $`\mathrm{Beta}(q,q)`$ for every real $`q>0`$.

## 2. Exact distributions of the conic coordinates under the ORIGINAL kernel measure

Let the original random variable be $`X>0`$ with law $`d\mathbf P_{\rm ker}`$, and define the derived random variables

```math
U=\log(X/c),\quad\eta=\mathrm{gd}(rU),\quad W=\sin\eta,\quad P=\frac{1+W}2,\quad \mathcal B=\cos^2\eta,\quad b=\tan\eta,\quad R=\sec\eta,\quad T=e^{rU}.
```

The variables $`B`$ (backbone/Gram coefficient) and $`\mathcal B=S^2`$ (squared profile) are **not** interchangeable. Moreover $`B(a,b)`$ in the normalization formulas denotes Euler's **beta function** $`\mathrm B(a,b)`$, not the Gram coefficient. These three meanings must be distinguished by type and arguments.

| Random variable | Support | Pushforward density / law |
|---|---|---|
| $`\eta`$ | $`(-\pi/2,\pi/2)`$ | Uniform density $`1/\pi`$ |
| $`W=\sin\eta`$ | $`(-1,1)`$ | Arcsine density $`1/(\pi\sqrt{1-W^2})`$ |
| $`P=(1+W)/2`$ | $`(0,1)`$ | $`\mathrm{Beta}(1/2,1/2)`$: density $`1/(\pi\sqrt{P(1-P)})`$ |
| $`\mathcal B=1-W^2=\cos^2\eta`$ | $`(0,1)`$ (value $`1`$ possible only at one angle) | $`\mathrm{Beta}(1/2,1/2)`$: density $`1/(\pi\sqrt{\mathcal B(1-\mathcal B)})`$ |
| $`b=\tan\eta`$ | $`\mathbb R`$ | Standard Cauchy density $`1/[\pi(1+b^2)]`$ |
| $`R=\sec\eta=\sqrt{1+b^2}`$ | $`[1,\infty)`$ | Density $`2/[\pi R\sqrt{R^2-1}]`$ for $`R>1`$ |
| $`T=e^{rU}=R+b`$ | $`(0,\infty)`$ | Half-Cauchy density $`2/[\pi(1+T^2)]`$ |

**Derivation:** the uniform-angle density is $`d\eta/\pi`$; under $`W=\sin\eta`$, $`dW=\cos\eta\,d\eta=\sqrt{1-W^2}\,d\eta`$, giving the arcsine density. Rescale $`W=2P-1`$ to obtain the first beta density. For $`\mathcal B=1-W^2`$, account for both branches $`W=\pm\sqrt{1-\mathcal B}`$; they give the **same** beta density. For $`b=\tan\eta`$, $`d\eta/db=1/(1+b^2)`$. The laws of $`R=\sqrt{1+b^2}`$ and $`T=R+b`$ follow by the same Jacobian rule.

### Identical marginals do not imply independence

Under this one-dimensional distribution, $`P`$ and $`\mathcal B`$ each have marginal law $`\mathrm{Beta}(1/2,1/2)`$, but they are **completely dependent**:

```math
\mathcal B=4P(1-P)\quad\text{almost surely}.
```

Their **joint** law is supported on the parabola, not on an area-filling two-dimensional distribution. This is a direct measure-theoretic consequence of the constrained conic dictionary.

## 3. The SQUARED-profile beta hierarchy

For $`q>0`$, push $`d\mathbf P_q`$ forward through $`W=\tanh(ru)`$, using $`dW=r(1-W^2)\,du`$:

```math
d\mathbf P_q(W)=\frac{(1-W^2)^{q-1}}{B(\frac12,q)}\,dW,\qquad -1<W<1.
```

Now $`W=2P-1`$ and $`dW=2\,dP`$, so the beta duplication identity gives

```math
d\mathbf P_q(P)=\frac{P^{q-1}(1-P)^{q-1}}{B(q,q)}\,dP,\qquad 0<P<1.
```

Thus $`P\sim\mathrm{Beta}(q,q)`$ under the squared-profile measure. Its cumulative distribution function is

```math
Q_q(u)=\mathbf P_q((-\infty,u])=I_{P(u)}(q,q).
```

This is exactly the $`Q_q`$ of [the oscillator hierarchy](../00-foundations/00-07-differential-algebra-oscillator-hierarchy.md).

The squared profile itself has a second exact beta law. Since $`\mathcal B=1-W^2`$, the two preimages $`W=\pm\sqrt{1-\mathcal B}`$ contribute equally, giving

```math
\mathcal B\sim\mathrm{Beta}\left(q,\frac12\right),\qquad \rho_{\mathcal B}(z)=\frac{z^{q-1}(1-z)^{-1/2}}{B(q,1/2)},\quad 0<z<1.
```

The hyperbolic coordinate $`b=\tan\eta`$ also has a simple law:

```math
\rho_{b,q}(b)=\frac{(1+b^2)^{-q-1/2}}{B(1/2,q)},\qquad b\in\mathbb R.
```

In the special case $`q=1/2`$ this is the standard Cauchy law; for arbitrary $`q>0`$ it is a scaled Student-t-type density. Equivalently, $`T^2=e^{2ru}=P/(1-P)`$ has the beta-prime law with shape parameters $`(q,q)`$. These are exact changes of variables, not a claim that the different random variables are independent.

At $`q=1`$:

```math
d\mathbf P_1(u)=\frac r2S^2du,\qquad d\mathbf P_1(\eta)=\frac12\cos\eta\,d\eta,\qquad d\mathbf P_1(P)=dP,\qquad Q_1=P.
```

**Contrast:** under the **original kernel probability**, $`P\sim\mathrm{Beta}(1/2,1/2)`$; under the normalized **sech-squared norm**, $`P\sim\mathrm{Beta}(1,1)`$ (uniform). They are distinct specializations of the same **logarithmic-coordinate** density family: the kernel law pushes forward to $`\mathbf P_{1/2}`$, while the classification-norm law is $`\mathbf P_1`$. Their underlying fields $`S,W`$ are the same, but the measures differ.

The logistic flow equation $`P_u=2rP(1-P)`$ is an ODE along the coordinate $`u`$; by itself it says **nothing** about what probability measure was placed on $`u`$. The beta laws arise only after declaring the underlying density.

## 4. Norms and powers

The preceding distinction is compatible with the finite classification norm

```math
\int_0^\infty x f(x;r,c)^2\,dx=\frac{1}{2r},\qquad \int_{\mathbb R}S^{2q}\,du=\frac1r B\left(\frac12,q\right).
```

The first expression is a **squared norm**, not a probability until divided by its total mass. Its natural $`q=1`$ normalized measure is $`d\mathbf P_1(u)`$, not $`d\mathbf P_{\rm ker}(x)`$.

**Sources:** foundational [primitive and half-split](../02-calculus-norms/02-02-primitives.md), [weighted norms](../02-calculus-norms/02-03-norms.md), [original probability density](04-01-distribution.md), [conic/Gudermannian maps](../00-foundations/00-08-projective-conics-gudermannian.md), and the local verification script [verify_conic_gudermannian.py](../_standards/verify_conic_gudermannian.py). The uniform-angle and resulting conic pushforwards here are exact consequences of the stated Jacobians, not claims of a new probability distribution.
