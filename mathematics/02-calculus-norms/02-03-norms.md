# 02.03 — Norms, convergence and the Classification Theorem

**This is a primary mathematical page.** We explicitly distinguish $`dx`$, $`x\,dx`$, $`dx/x`$, and the general level weight $`x^{2q-1}\,dx`$. Write $`f=S/(2x)`$, $`f_\mu=f/\sqrt\mu`$, $`S=\mathrm{sech}(ru)`$, $`u=\log(x/c)`$.

## 1. The classification norm

For any real candidate Master field $`F`$, set $`y(u)=2xF(x)`$. Then, by $`dx=x\,du`$,

```math
N(F):=\int_0^\infty x|F(x)|^2\,dx=\frac14\int_{\mathbb R}|y(u)|^2\,du.
```

Thus the pullback $`F\mapsto 2xF`$ is an isometry **up to factor $`2`$**, not an unqualified unitary operator. For the distinguished finite-norm family,

```math
N(f_\mu)=\frac1{4\mu}\int_{\mathbb R}\mathrm{sech}^2(ru)\,du=\frac1{2r\mu}.
```

This is the **finite weighted norm hypothesis** of the [Classification Theorem](../01-master-equation/01-02-classification.md). The theorem is about $`F`$ solving a second-order equation, not about all functions in this Hilbert space.

## 2. Ordinary $`L^2(dx)`$ norm is different

For the unscaled kernel $`f`$, the ordinary norm squared is

```math
\int_0^\infty |f(x;r,c)|^2\,dx=\frac{\pi}{4cr^2\sin(\pi/(2r))},\qquad r>\frac12.
```

**Derivation:** substitute $`x=ce^u`$:

```math
\int_0^\infty f^2\,dx=\frac1{4c}\int_{\mathbb R}e^{-u}\mathrm{sech}^2(ru)\,du.
```

The bilateral exponential moment of $`\mathrm{sech}^2`$ yields the displayed result for $`|1/r|<2`$. For $`0<r\le1/2`$, the integral diverges at $`x=0`$. For $`f_\mu`$ multiply by $`\mu^{-1}`$.

This condition **does not constrain the classification theorem**, which uses $`x\,dx`$ and holds for every $`r>0`$.

## 3. Other weights and powers

The same amplitude pullback gives, for any $`\varpi>0`$ and real $`F`$,

```math
\int_0^\infty |F(x)|^\varpi x^{\varpi-1}\,dx=2^{-\varpi}\int_{\mathbb R}|y(u)|^\varpi\,du.
```

This is a **measure identity**, not a claim that the Classification Theorem has already been proved under every possible replacement norm. The foundational paper v0.3 Remark 4.3 discusses further $`L^\varpi`$ variants and their proof status separately.

For the general intrinsic level $`q=(\ell-1)/2>0`$, the natural norm is

```math
N_q(F)=\int_0^\infty x^{2q-1}|F(x)|^2\,dx=\int_{\mathbb R}|U_q(u)|^2\,du,\qquad U_q=x^qF.
```

For its distinguished profile $`U_q=(4\mu)^{-q/2}\mathrm{sech}^q(r(u-u_0))`$,

```math
N_q(F)=\frac{(4\mu)^{-q}}{r}B(q,1/2)=\frac{(4\mu)^{-q}}{r}\frac{\sqrt\pi\,\Gamma(q)}{\Gamma(q+1/2)}.
```

At $`q=1`$ this gives $`1/(2r\mu)`$, agreeing with the cubic norm.

## 4. A norm dictionary

| Quantity | Underlying measure | Value or convergence |
|---|---|---|
| $`\int f\,dx`$ | positive Lebesgue measure | $`\pi/(2r)`$ for every $`r>0`$ |
| $`\int \lvert f\rvert^2 x\,dx`$ | classification Hilbert measure | $`1/(2r)`$ for every $`r>0`$ |
| $`\int\lvert f_\mu\rvert^2 x\,dx`$ | same measure, coupled field | $`1/(2r\mu)`$ |
| $`\int\lvert f\rvert^2dx`$ | ordinary Lebesgue measure | finite only for $`r>1/2`$ |
| $`\int\lvert S\rvert^2du`$ | log-coordinate Lebesgue measure | $`2/r`$ |
| $`\int\lvert U_q\rvert^2du`$ | log-coordinate level measure | $`(4\mu)^{-q}B(q,1/2)/r`$ on the distinguished solution |

## 5. Parseval/Plancherel follows the measure

The Fourier transform of $`g(u)=x f(x)=S/2`$ is the correct additive Fourier image for the weighted classification norm. Its Parseval formula is **not** the same as applying the Fourier transform directly to $`f(x)`$ with measure $`dx`$. See [transform conventions](../03-transforms-special-functions/03-01-mellin-fourier-plancherel.md).

**Sources:** foundational paper §§2–4, theorem 4.5; [revised weighted classification](../../reference/algebra-geometry/03-differential-structure/03-05-linear-annihilator.md); [legacy norm calculations](../../research/legacy-parts/Part%20II%20-%20Calculus%20and%20Special%20Functions/05-integration-norms/05-00-integration-norms.md).
