# 04.01 — Kernel probability law and exact coordinate pushforwards

Fix $`x,c,r>0`$ and define the normalized density with respect to **$`dx`$** by

```math
\rho_X(x;r,c)=\frac{2r}{\pi}f(x;r,c),\qquad \int_0^\infty\rho_X(x;r,c)\,dx=1.
```

## Logarithmic variable

Let the random variable $`U=\log(X/c)`$. Its density with respect to **$`du`$** is

```math
\rho_U(u)=\rho_X(ce^u)\frac{dx}{du}=\frac r\pi\mathrm{sech}(ru).
```

This density is even, so the center $`x=c`$ is the median of $`X`$ (not generally its mean). Its Fourier-characteristic function follows from the explicitly normalized sech transform:

```math
\mathbb E[e^{ikU}]=\mathrm{sech}\!\left(\frac{\pi k}{2r}\right),\qquad \mathbb E[U]=0,\qquad \mathrm{Var}(U)=\frac{\pi^2}{4r^2}.
```

## Power-coordinate half-Cauchy law

For $`T=(X/c)^r=e^{rU}>0`$ and $`dT/du=rT`$,

```math
\rho_T(t)=\frac2{\pi(1+t^2)}\quad(t>0),\qquad F_X(x)=\frac2\pi\arctan\!\left((x/c)^r\right).
```

This is the standard **half-Cauchy law** in the power coordinate, not a full signed Cauchy distribution on $`\mathbb R`$.

## Power moments and their exact convergence interval

For a real exponent $`a`$,

```math
\mathbb E[X^a]=c^a\sec\!\left(\frac{\pi a}{2r}\right),\qquad -r<a<r.
```

The expression comes from the Mellin transform at $`s=a+1`$. In particular, $`\mathbb E[X]`$ exists only if $`r>1`$; $`c`$ is not automatically the arithmetic mean. Outside the stated interval the original moment integral diverges, even if the secant's meromorphic continuation has a finite value.

The log-coordinate law depends on $`r`$ and not on $`c`$ once the random coordinate $`U`$ itself is defined using $`c`$. This **does not** mean $`c`$ is unidentifiable in the original $`X`$ distribution.

**Sources:** [Part I §2 power closure](../../reference/algebra-geometry/02-foundational-symmetries/02-05-power-transformation.md), [probability source files](../../research/legacy-parts/Part%20III%20-%20Probability%20and%20Statistical%20Mechanics/07-statistical-information/12-02-statistical-moments.md), [Mellin transform](../03-transforms-special-functions/03-01-mellin-fourier-plancherel.md).
