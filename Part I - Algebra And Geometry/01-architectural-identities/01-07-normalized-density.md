# 1.7 — Probability density, CDF, quantiles, and arcsine coordinate

Because $f(x)\,dx=\tfrac12S\,du$ and $\int_{\mathbb R}\mathrm{sech}(ru)\,du=\pi/r$, the mass is $\int_0^\infty f\,dx=\pi/(2r)$.

**[E]** The probability density and CDF are

```math
\rho(x;r,c)=\frac{2r}{\pi}f(x;r,c),\qquad F(x;r,c)=\frac2\pi\arctan\!\left((x/c)^r\right).
```

The derivative of the displayed CDF equals $\rho$; its limits at $0$ and infinity are $0$ and $1$. Hence the quantile function is

```math
F^{-1}(v)=c\,\tan^{1/r}\left(\frac{\pi v}{2}\right),\qquad 0<v<1,
```

and the median is $c$. The centered logarithmic variable $U=\log(X/c)$ has density $r\mathrm{sech}(ru)/\pi$ and is symmetric.

The alternative Gudermannian form, with principal $\arctan\in(-\pi/2,\pi/2)$, is

```math
F(x)=\frac12+\frac1\pi\arctan(\sinh(ru)).
```

No branch jump occurs for real $u$.

**Arcsine pushforward [E].** Put $Z=W(X)=\tanh(rU)$. Since $dZ/du=r(1-Z^2)$,

```math
p_Z(z)=\frac{1}{\pi\sqrt{1-z^2}},\qquad -1<z<1.
```

Equivalently $P=(1+Z)/2\sim\mathrm{Beta}(1/2,1/2)$, not a uniform distribution. Another canonical pushforward, $T=(X/c)^r$, has standard half-Cauchy density $2/[\pi(1+T^2)]$.

**Moment domain.** For complex $a$ satisfying $|\Re a|<r$, the power moment is

```math
\mathbb E[X^a]=c^a\sec\!\left(\frac{\pi a}{2r}\right).
```

Values of the meromorphic continuation outside the strip are **not** probabilistic moments.

## Two exact antiderivatives and the Gudermannian identity

The earlier notes explicitly computed the primitive; it is useful to keep both forms, including their **different additive constants**.

**Step 1: power substitution.** Set $T=(x/c)^r$. Differentiation gives $dT=(r/c^r)x^{r-1}dx$, and the original density simplifies:

```math
f(x;r,c)\,dx=\frac1r\frac{dT}{1+T^2}.
```

**Step 2: integrate.** Using the principal real branch of $\arctan$ on positive $T$,

```math
A(x):=\frac1r\arctan((x/c)^r),\qquad A_x(x)=f(x;r,c),\qquad A(0^+)=0.
```

**Step 3: logarithmic substitution.** Put $u=\log(x/c)$, $z=ru$, so that $dx=x\,du$ and $dz=r\,du$. Then

```math
f(x;r,c)\,dx=\frac{1}{2r}\mathrm{sech}(z)\,dz.
```

**Step 4: integrate the hyperbolic secant.** Since $d\,\arctan(\sinh z)/dz=\cosh z/(1+\sinh^2z)=\mathrm{sech}(z)$,

```math
B(x):=\frac{1}{2r}\arctan(\sinh(r\log(x/c))),\qquad B_x(x)=f(x;r,c),\qquad B(c)=0.
```

**Step 5: compare constants.** The Gudermannian identity on real $z$ is $2\arctan(e^z)=\arctan(\sinh z)+\pi/2$. It holds because both sides have derivative $\mathrm{sech}(z)$ and agree at $z=0$. Consequently,

```math
A(x)=B(x)+\frac{\pi}{4r}.
```

**Step 6: compute the CDF.** The normalized integral from $0$ to $x$ is

```math
F(x;r,c)=\frac{2r}{\pi}[A(x)-A(0^+)]=\frac2\pi\arctan((x/c)^r).
```

As $x\to\infty$, $A(x)\to\pi/(2r)$, proving the total-mass identity without an unverified appeal to an antiderivative. The same computation gives $F(c)=1/2$. The historical constant-free statements “$A=B$” would be false; **their derivatives**, not their chosen zero values, agree.
