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

## Full nonzero-power closure theorem

The reciprocal and half-Cauchy changes of variables are two cases of a more general exact closure law.

**Theorem [E].** Let $X\sim\rho(\cdot;r,c)$, let $a\in\mathbb R\setminus\{0\}$ and $d>0$, and set

```math
Y=d\left(\frac Xc\right)^a,\qquad r'=\frac r{|a|}.
```

Then $Y$ is positive and

```math
Y\sim\rho(\cdot;r',d).
```

**Proof.** The logarithmic variable $U=\log(X/c)$ has density $r\mathrm{sech}(ru)/\pi$. The new centered logarithmic variable is $V=\log(Y/d)=aU$. By the one-dimensional change-of-variables formula,

```math
p_V(v)=\frac1{|a|}\frac r\pi\mathrm{sech}\left(\frac{rv}{a}\right)=\frac{r'}\pi\mathrm{sech}(r'v).
```

Evenness of $\mathrm{sech}$ is needed when $a<0$. Converting $V$ back to $Y$ using $dy=y\,dv$ proves the claim. The corresponding **unnormalized** measure identity includes the total-mass ratio:

```math
\left[d(x/c)^a\right]_*(f(x;r,c)\,dx)=\frac1{|a|}f(y;r',d)\,dy.
```

The pushforward symbol means transport of a positive measure, not composition of scalar functions. For $a=-1,d=1/c$, the map is $Y=1/X$; for $a=-1,d=c$, it is $Y=c^2/X$; for $a=r,d=1$, it gives the half-Cauchy law with $r'=1$.

**Scope.** An arbitrary nonzero power changes $r$ unless $|a|=1$. This is closure **of the whole two-parameter family**, not invariance of an individual function or of its total unnormalized mass.

## Direct half-Cauchy calculation recovered from the draft

The more general power-closure theorem above already implies this result. The source's independent Jacobian calculation is retained because it displays every cancellation.

**Step 1.** Put $t=(x/c)^r$, so $x=ct^{1/r}$ and $dx/dt=(c/r)t^{1/r-1}$.

**Step 2.** Insert $x=ct^{1/r}$ in the normalized density:

```math
\rho(ct^{1/r};r,c)=\frac{2r}{\pi}\frac{c^r(ct^{1/r})^{r-1}}{c^{2r}+(ct^{1/r})^{2r}}=\frac{2r}{\pi c}\frac{t^{1-1/r}}{1+t^2}.
```

**Step 3.** Multiply by the Jacobian and cancel the exponents:

```math
p_T(t)=\rho(ct^{1/r};r,c)\frac c r t^{1/r-1}=\frac{2}{\pi(1+t^2)},\qquad t>0.
```

The appearance of the half-Cauchy distribution holds for **every** $r,c>0$, without an approximation or a limit. The positive variable $T$ is not a signed full Cauchy variable.
