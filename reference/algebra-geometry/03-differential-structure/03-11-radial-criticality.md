# 3.11 — Four-dimensional radial equation, Hardy term and Kelvin invariance

**Status [E/K].** The particular coefficient $`3x f_x`$ of the spatial Master has a precise mathematical interpretation as the radial Laplacian in dimension four. This is an identity of differential operators; no gauge-theoretic or cosmological model is assumed.

## The exact radial equation

Let $`F(x)=f_\mu(x;r,c)`$ for $`x>0`$. Divide the nonlinear Master by $`x^2`$:

```math
F_{xx}+\frac3xF_x+\frac{1-r^2}{x^2}F+8\mu r^2F^3=0.
```

**Step 1.** For a radial function on $`\mathbb R^4\setminus\{0\}`$, the Euclidean Laplacian is $`\Delta_4F=F_{xx}+3F_x/x`$.

**Step 2.** Rearrangement gives the semilinear Hardy-type equation

```math
-\Delta_4F+\frac{r^2-1}{x^2}F=8\mu r^2F^3.
```

For $`r=1`$ the inverse-square term vanishes and the equation is the critical semilinear equation $`-\Delta_4F=8\mu F^3`$. In four dimensions the Sobolev critical exponent is $`(4+2)/(4-2)=3`$, exactly the cubic power here. For $`r\ne1`$ the Hardy potential is present and must not be suppressed.

**Step 3.** At $`r=1`$, the distinguished positive solution is

```math
F(x)=\frac{c}{\sqrt\mu(c^2+x^2)}.
```

Substituting its first two derivatives verifies $`-\Delta_4F=8\mu F^3`$. Up to standard rescalings it is a radial critical Sobolev bubble. Calling it a BPST field or an instanton requires additional gauge data not contained in the scalar equation.

## Kelvin transform in dimension four

For a fixed positive inversion radius $`a`$, define the Kelvin transform of a radial function by

```math
(\mathcal K_aF)(x)=\frac{a^2}{x^2}F\left(\frac{a^2}{x}\right).
```

**Step 1.** Set $`s=a^2/x`$. The chain rule gives

```math
(\mathcal K_aF)_x=-\frac{2a^2}{x^3}F(s)-\frac{a^4}{x^4}F_s(s).
```

**Step 2.** Differentiate again and add $`3(\mathcal K_aF)_x/x`$; terms proportional to $`F(s)`$ cancel:

```math
\left(\partial_x^2+\frac3x\partial_x\right)\mathcal K_aF=\frac{a^6}{x^6}\left(F_{ss}+\frac3sF_s\right)\!(s).
```

**Step 3.** The inverse-square and cubic terms obey the same transformation weight:

```math
\frac1{x^2}\mathcal K_aF(x)=\frac{a^6}{x^6}\frac{F(s)}{s^2},\qquad (\mathcal K_aF(x))^3=\frac{a^6}{x^6}F(s)^3.
```

**Step 4.** Combining these three identities shows that the **entire** radial Hardy–cubic equation is covariant under $`\mathcal K_a`$, for every fixed $`r,\mu>0`$. The critical cubic exponent is essential for the common weight $`a^6/x^6`$.

## Fixed-point property of the distinguished kernel

The inversion identity from Chapter 2 implies, for the inversion radius chosen as the scale $`a=c`$,

```math
(\mathcal K_cf_\mu)(x)=\frac{c^2}{x^2}f_\mu(c^2/x;r,c)=f_\mu(x;r,c).
```

Thus every resolution parameter $`r>0`$ produces a distinguished **Kelvin-fixed radial solution** of the Hardy–cubic equation. This fixed-point identity is stronger than ordinary scalar evenness, and it holds because the Kelvin conformal weight is exactly two in dimension four.

## Radial variational functional

The semilinear equation is the Euler–Lagrange equation, on radial test functions supported away from the origin, of

```math
\mathcal E[F]=\int_{\mathbb R^4}\left[\frac12|\nabla F|^2+\frac{r^2-1}{2|x|^2}F^2-2\mu r^2F^4\right]\,d^4x.
```

The coordinate $`|x|`$ in this functional is the Euclidean radius, not the canonical logarithmic variable $`u`$. The Hardy coefficient is $`r^2-1>-1`$, above the negative four-dimensional Hardy threshold. This furnishes a precise mathematical criticality explanation for the radial coefficient without asserting a forced physical interpretation.
