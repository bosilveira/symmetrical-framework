# Chapter 2 — Foundational symmetries

**Current exposition; revised 20 November 2026.** The independent parameters are $r,c>0$; $u=\log(x/c)$ is the logarithmic coordinate. All formulas below are exact [E] unless otherwise marked.

The natural geometric involution is $I_c(x)=c^2/x$. It sends $u\mapsto-u$ and acts by

```math
f(I_c(x))=\frac{x^2}{c^2}f(x),\quad S(I_c(x))=S(x),\quad W(I_c(x))=-W(x).
```

As **positive measures**, $I_{c*}(f(x)\,dx)=f(x)\,dx$. This does **not** mean that $f(x)\,dx/x$ is invariant.

Joint scaling is $f(\lambda x;r,\lambda c)=\lambda^{-1}f(x;r,c)$, equivalent to $(x\partial_x+c\partial_c)f=-f$. The normalized probability law is closed under inversion $X\mapsto1/X$ with parameter $c\mapsto1/c$, and under the power map $(X/c)^r$ it becomes standard half-Cauchy.

The CDF $F(x)=2\arctan((x/c)^r)/\pi$ has two **different** composition laws: addition of arctangent angles (restricted to avoid branch jumps) and multiplication of tangent coordinates (a global associative law on $(0,1)$). These are algebraic group laws, not claims about adding independent random variables.

**Contents:** [2.1](02-01-symmetry-point.md), [2.2](02-02-moebius-symmetry.md), [2.3](02-03-euler-homogeneity.md), [2.4](02-04-reciprocal-closure.md), [2.5](02-05-power-transformation.md), [2.6](02-06-hyperbolic-double.md), [2.7](02-07-hyperbolic-triple.md), [2.8](02-08-superpotential-antisymmetry.md), [2.9](02-09-self-scaling.md), [2.10](02-10-cdf-addition.md), [2.11](02-11-cdf-product.md), [notes](02-99-notes.md).
