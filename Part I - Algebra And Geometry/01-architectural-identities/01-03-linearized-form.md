# 1.3 — Three logarithmic objects, distinguished precisely

Let $x=ce^u$ with $c>0$, so that $dx=x\,du$ and $dx/x=du$.

1. **Pointwise pullback**:

```math
g(u;r,c):=f(ce^u;r,c)=\frac{e^{-u}}{2c}\mathrm{sech}(ru).
```

   This is generally **not** even and is not a probability density with respect to $du$.

2. **Pushforward of the normalized probability law**: let

```math
\rho(x;r,c)=\frac{2r}{\pi}f(x;r,c).
```

   For $U=\log(X/c)$ and $X\sim\rho(x)\,dx$, the density of $U$ is

```math
p(u;r)=x\rho(x;r,c)\big|_{x=ce^u} =\frac r\pi\mathrm{sech}(ru).
```

   This integrates to one and is even. Its formula has no $c$ because the coordinate $U$ itself depends on $c$.

3. **Hyperbolic phase**:

```math
W(u;r)=\tanh(ru),\qquad W_u=r(1-W^2).
```

   This is an odd, dimensionless coordinate, not a probability density.

**Haar versus ordinary density.** The invariant multiplicative Haar measure is $dx/x$. The unnormalized measure $f(x)\,dx$ has density $xf(x)=S/2$ relative to Haar measure:

```math
f(x)\,dx=(xf(x))\frac{dx}{x}=\frac12S(u)\,du.
```

Thus the functions $f(ce^u)$, $xf(x)$ and $p(u)$ are different, even though they arise from the same kernel.

**Weighted $L^2$ isometry.** Setting $y(u)=2xf(x)$,

```math
\int_0^\infty x|f(x)|^2\,dx=\frac14\int_{\mathbb R}|y(u)|^2\,du.
```

This equality is a change-of-measure theorem, and later underlies the finite-norm Master classification.

## The exact Jacobian relation and logarithmic score

The original derivation introduced the direct pullback and the pushforward density separately. Their relationship can be written explicitly without suppressing $c$.

**Step 1.** The probability density of $X$ is $\rho(x;r,c)=(2r/\pi)f(x;r,c)$.

**Step 2.** For $U=\log(X/c)$, the Jacobian of $x=ce^u$ is $dx/du=ce^u=x$. Thus $p(u;r)=x\rho(x;r,c)$ at $x=ce^u$.

**Step 3.** Solve this relation for the *pointwise* pullback $g(u;r,c)=f(ce^u;r,c)$:

```math
g(u;r,c)=\frac{\pi}{2rce^u}p(u;r)=\frac{\pi}{2rc}e^{-u}p(u;r).
```

The factor $e^{-u}$ is essential: substituting $f(ce^u)$ without the Jacobian does **not** produce $p(u)$.

**Step 4.** Differentiate the even logarithmic density, using $d\,\mathrm{sech}(ru)/du=-r\,\mathrm{sech}(ru)\tanh(ru)$:

```math
p_u=-rpW,\qquad W=-\frac{1}{r}\frac{p_u}{p}=-\frac{1}{r}\frac{d}{du}\log p.
```

The division is valid globally because $p(u;r)>0$ for every real $u$. This identity is a *logarithmic score* of a deterministic function, not evidence of time-dependent probability transport.

**Step 5.** Substitute $S=\pi p/r$ into $S^2+W^2=1$:

```math
\left(\frac{\pi p}{r}\right)^2+W^2=1,\qquad p=\frac{r}{\pi}\sqrt{1-W^2}.
```

The sign of $W$ is **not** determined by the value of $p$ alone; its logarithmic derivative restores the sign. The pair $(\pi p/r,W)$ traverses the right half of the unit circle as $u$ increases from $-\infty$ to $\infty$.
