# 1.9 — Asymptotics, derivatives, and integrability strips

Let $t=x/c$. For $0<t<1$ the convergent geometric series gives

```math
f(x)=c^{-r}x^{r-1}\sum_{n=0}^{\infty}(-1)^n(x/c)^{2rn}.
```

For $t>1$ it gives

```math
f(x)=c^rx^{-r-1}\sum_{n=0}^{\infty}(-1)^n(c/x)^{2rn}.
```

Hence $f\sim c^{-r}x^{r-1}$ at $0^+$ and $f\sim c^rx^{-r-1}$ at $\infty$ (asymptotic equivalences, **not** equalities of limits to variable expressions).

**Derivative qualifications.** If $r\ne1$, $f'(x)\sim (r-1)c^{-r}x^{r-2}$ as $x\to0^+$. For $r=1$ the leading derivative coefficient vanishes and instead $f'(x;1,c)=-2cx/(c^2+x^2)^2$. Analogous cancellations must be checked before differentiating a leading-term asymptotic.

For $p>0$ and real or complex $a$, the integral

```math
I_p(a)=\int_0^\infty x^{a-1}f(x)^p\,dx
```

converges absolutely precisely when

```math
p(1-r)<\Re a<p(1+r).
```

The Beta substitution $z=(x/c)^{2r}$ yields **[E]**

```math
I_p(a)=\frac{c^{a-p}}{2r} B\!\left(\frac p2+\frac{a-p}{2r}, \frac p2-\frac{a-p}{2r}\right).
```

For $p=1$ this is the Mellin transform with $a=s$; for $p=2,a=2$ it is the weighted square norm $1/(2r)$.

## Rigorous endpoint-limit proof and a rejected shortcut

The earlier notes obtained the right endpoint classes but sometimes wrote a **limit equal to a nonconstant power of $x$**. Asymptotic equivalence should instead be proved by ratios.

**Step 1: near the origin.** Divide by the proposed leading term:

```math
\frac{f(x;r,c)}{c^{-r}x^{r-1}}=\frac{1}{1+(x/c)^{2r}}\longrightarrow1\qquad(x\to0^+).
```

**Step 2: at infinity.** Divide by the right-hand leading term:

```math
\frac{f(x;r,c)}{c^rx^{-r-1}}=\frac{1}{1+(c/x)^{2r}}\longrightarrow1\qquad(x\to\infty).
```

**Step 3: take actual limits.** The first ratio, together with the sign of $r-1$, yields

```math
\lim_{x\to0^+}f(x;r,c)=\begin{cases}+\infty,&0<r<1,\\1/c,&r=1,\\0,&r>1,\end{cases}\qquad \lim_{x\to\infty}f(x;r,c)=0.
```

**Step 4: infer integrability, not merely boundedness.** The mass integral always converges because the left exponent $r-1>-1$ and the right exponent $-r-1<-1$. By contrast, the $p$-th-power moment with weight $x^{a-1}$ converges only in the strict open strip stated above.

The leading asymptotic may be differentiated for $r\ne1$ using the explicitly convergent power series, but not by a blanket rule for all $r$: at $r=1$ the nominal leading derivative coefficient is zero and the next term must be used.
