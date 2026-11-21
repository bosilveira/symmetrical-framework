# 2.5 — Power map and the half-Cauchy reference law

**Theorem [E].** If $X\sim\rho(x;r,c)\,dx$ and $T=(X/c)^r$, then

```math
p_T(t)=\frac{2}{\pi(1+t^2)},\qquad t>0.
```

Indeed $x=ct^{1/r}$ and $dx/dt=(c/r)t^{1/r-1}$; substitution into $\rho(x)\,dx$ cancels the powers of $c$ and $t$. Therefore $T$ is standard half-Cauchy and $X^r$ is half-Cauchy with scale $c^r$.

**Sampling.** If $V$ is uniform on $(0,1)$ and $T=\tan(\pi V/2)$, then

```math
X=c\,T^{1/r}
```

has density $\rho$. This is the inverse-CDF method, with no numerical root finding.

**Transformed variables.** $U=\log(X/c)=r^{-1}\log T$ has hyperbolic-secant density $r\mathrm{sech}(ru)/\pi$. The logistic variable $P=T^2/(1+T^2)$ is **arcsine**:

```math
P\sim\mathrm{Beta}\!\left(\tfrac12,\tfrac12\right).
```

The CDF value $F(X)$ is uniform by the probability integral transform; it is distinct from $P$.

The power map depends explicitly on $r$. It is not a fixed, parameter-independent group automorphism acting on all members of the family at once.
