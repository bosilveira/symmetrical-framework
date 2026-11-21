# 03.01 — Mellin, Fourier, Parseval and Plancherel with exact measures

**Conventions:** $`x,c,r>0`$, $`u=\log(x/c)`$, $`g(u)=xf(ce^u)=\tfrac12\mathrm{sech}(ru)`$. The Mellin transform is defined on its absolute-convergence strip by

```math
\mathcal M[f](s)=\int_0^\infty x^{s-1}f(x)\,dx.
```

The additive Fourier transform is $`\widehat g(k)=\int_{\mathbb R}e^{-iku}g(u)\,du`$; its inverse uses $`(2\pi)^{-1}\int e^{iku}\widehat g(k)\,dk`$.

## Mellin calculation

By $`dx=x\,du`$, $`f(x)dx=\tfrac12\mathrm{sech}(ru)\,du`$, hence

```math
\mathcal M[f](s)=\frac{c^{s-1}}2\int_{\mathbb R}e^{(s-1)u}\mathrm{sech}(ru)\,du=\frac{\pi c^{s-1}}{2r}\sec\!\left(\frac{\pi(s-1)}{2r}\right).
```

The **initial integral strip** is

```math
1-r<\Re s<1+r.
```

The meromorphic secant formula extends analytically outside this strip, but the resulting function is not the absolutely convergent integral there. The scale $`c^{s-1}`$ must never be discarded.

## Fourier transform in the logarithmic coordinate

For $`g(u)=S(u)/2`$,

```math
\widehat g(k)=\frac{\pi}{2r}\mathrm{sech}\!\left(\frac{\pi k}{2r}\right).
```

The vertical Mellin transform is related by

```math
\mathcal M[f](1+it)=c^{it}\widehat g(-t).
```

This is a **specific** Mellin–Fourier bridge for the chosen pullback and transform sign. If the Fourier transform is instead taken directly in $`x`$, it is a different object.

## Plancherel and Parseval, including weights

The standard Fourier identity is

```math
\int_{\mathbb R}|g(u)|^2\,du=\frac1{2\pi}\int_{\mathbb R}|\widehat g(k)|^2\,dk=\frac1{2r}.
```

The general Mellin vertical-line Plancherel theorem, with $`\sigma\in\mathbb R`$ and sufficient weighted square integrability, is

```math
\int_0^\infty |F(x)|^2x^{2\sigma-1}\,dx=\frac1{2\pi}\int_{\mathbb R}|\mathcal M[F](\sigma+it)|^2\,dt.
```

For the original $`f`$ and **$`\sigma=1`$** this gives exactly the classification norm $`1/(2r)`$; for the coupled $`f_\mu`$ it is $`1/(2r\mu)`$. More generally, the weight $`x^{2\sigma-1}`$ and the associated convergence strip are part of the theorem. For $`f`$, the weighted square integral exists precisely for $`1-r<\sigma<1+r`$.

**No unsupported duality:** Fourier self-reciprocity of the hyperbolic secant is a statement **after** the logarithmic coordinate and frequency scales are specified. It does not imply all other transforms are self-dual or that a generic Master orbit has a closed secant transform.

**Sources:** Complete Reference v2 F.8 and [legacy Plancherel sources](../../research/legacy-parts/Part%20II%20-%20Calculus%20and%20Special%20Functions/08-plancherel-parseval/08-03-multiplicative-plancherel.md). Norm hypotheses: [§02.03](../02-calculus-norms/02-03-norms.md).
