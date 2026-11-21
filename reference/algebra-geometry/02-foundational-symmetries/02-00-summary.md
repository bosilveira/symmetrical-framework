# Chapter 2 — Foundational symmetries

**Expanded mathematical reference · 20 November 2026.** Fix $`x,c,r>0`$, $`u=\log(x/c)`$, $`S=\mathrm{sech}(ru)`$, $`W=\tanh(ru)`$ and $`\rho(x;r,c)=2rf(x;r,c)/\pi`$. All statements marked [E] are exact identities under their specified hypotheses; standard Fourier, spectral and information-geometric results are marked [K].

## Logical structure

The starting symmetry is inversion $`I_c(x)=c^2/x`$, equivalent to reflection $`u\mapsto-u`$. Its **pointwise weight** and its **measure invariance** are different assertions:

```math
f(c^2/x;r,c)=\frac{x^2}{c^2}f(x;r,c),\qquad I_{c*}(f(x;r,c)\,dx)=f(x;r,c)\,dx.
```

As oriented one-forms, $`f(I_c(x))\,dI_c(x)=-f(x)\,dx`$; the older claim that $`f(x)\,dx/x`$ is invariant is false. Invariance alone characterizes a broad family of even log-densities, not the specific hyperbolic kernel.

The compatible scale law at fixed $`r`$ is

```math
f(\lambda x;r,\lambda c)=\lambda^{-1}f(x;r,c),\qquad (x\partial_x+c\partial_c)f=-f.
```

The original distribution maps to a half-Cauchy law under $`(X/c)^r`$, and the **whole** normalized family is closed under the larger log-affine transformations $`z\mapsto az+b`$ with $`a\ne0`$. Resolution changes by $`r\mapsto r/|a|`$; ordinary reciprocal closure is the $`a=-1`$ case.

Two- and three-scale product identities follow from hyperbolic addition. The **weighted overlap** of two profiles with equal $`r`$ has a new exact expression in the revised exposition, with $`\delta=r\log(c_2/c_1)`$:

```math
\int_0^\infty x f(x;r,c_1)f(x;r,c_2)\,dx=\frac{1}{2r}\frac{\delta}{\sinh\delta}.
```

The normalized overlap is a strictly positive-definite kernel, furnishing a Hilbert geometry on the scale parameter. This is not the same as the **Fisher-information metric** of the normalized probability family, which is exactly hyperbolic. In coordinates $`\alpha=\log(c/x_*)`$ and $`t=1/r`$:

```math
ds_F^2=\frac{1}{2t^2}\,d\alpha^2+\frac{\pi^2}{8t^2}\,dt^2,\qquad K_F=-\frac{8}{\pi^2}.
```

The superpotential section distinguishes the spatial and logarithmic conventions and derives both Darboux partners, the unique $`L^2`$ zero mode, and reflectionless scattering of the selected one-soliton Schrödinger operator.

**Two CDF compositions must remain distinct.** Arctangent-angle addition gives a **partial associative operation** when the resulting CDF value is below $`1`$; it is *not* a group on finite positive coordinates. Multiplication of tangent coordinates yields a **global abelian group** on $`(0,1)`$. The logistic phase and the hyperbolic tangent give two further charts for the same global group. None computes an independent-variable convolution.

## Contents and reading order

1. [2.1 Center jets and exceptional inflection](02-01-symmetry-point.md)
2. [2.2 Inversion and invariant positive measures](02-02-moebius-symmetry.md)
3. [2.3 Euler homogeneity and commuting actions](02-03-euler-homogeneity.md)
4. [2.4 Reciprocal closure and Mellin reflection](02-04-reciprocal-closure.md)
5. [2.5 Half-Cauchy and nonzero-power closure](02-05-power-transformation.md)
6. [2.6 Two-scale products and scale exchange](02-06-hyperbolic-double.md)
7. [2.7 Multi-scale product-to-sum identities](02-07-hyperbolic-triple.md)
8. [2.8 Superpotential and Darboux partners](02-08-superpotential-antisymmetry.md)
9. [2.9 Scaling flows and power composition](02-09-self-scaling.md)
10. [2.10 Partial arctangent CDF addition](02-10-cdf-addition.md)
11. [2.11 Global multiplicative CDF, phase and logistic groups](02-11-cdf-product.md)
12. [2.12 Full log-affine group and family equivariance](02-12-log-affine-group.md)
13. [2.13 Weighted overlap and positive-definite kernel](02-13-weighted-overlap.md)
14. [2.14 Fisher-information geometry](02-14-fisher-information.md)

See the [Chapter 2 verification register](02-99-notes.md), the [Part I guide](../README.md), and [Markdown conventions](../../../MARKDOWN_STYLE.md). The earlier Gemini Chapter 2 notes were reviewed, source-supported derivations have been incorporated into the numbered sections, and the redundant `02-gemini.md` has been removed from the active branch. See the [integration audit](02-99-notes.md); Git history preserves the original draft.
