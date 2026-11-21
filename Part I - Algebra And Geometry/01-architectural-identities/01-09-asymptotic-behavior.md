# 1.9 — Asymptotics, derivatives, and integrability strips

Let $t=x/c$. For $0<t<1$ the convergent geometric series gives
$$
f(x)=c^{-r}x^{r-1}\sum_{n=0}^{\infty}(-1)^n(x/c)^{2rn}.
$$
For $t>1$ it gives
$$
f(x)=c^rx^{-r-1}\sum_{n=0}^{\infty}(-1)^n(c/x)^{2rn}.
$$
Hence $f\sim c^{-r}x^{r-1}$ at $0^+$ and $f\sim c^rx^{-r-1}$ at $\infty$ (asymptotic equivalences, **not** equalities of limits to variable expressions).

**Derivative qualifications.** If $r\ne1$, $f'(x)\sim (r-1)c^{-r}x^{r-2}$ as $x\to0^+$. For $r=1$ the leading derivative coefficient vanishes and instead $f'(x;1,c)=-2cx/(c^2+x^2)^2$. Analogous cancellations must be checked before differentiating a leading-term asymptotic.

For $p>0$ and real or complex $a$, the integral
$$
I_p(a)=\int_0^\infty x^{a-1}f(x)^p\,dx
$$
converges absolutely precisely when
$$
p(1-r)<\Re a<p(1+r).
$$
The Beta substitution $z=(x/c)^{2r}$ yields **[E]**
$$
I_p(a)=\frac{c^{a-p}}{2r}
B\!\left(\frac p2+\frac{a-p}{2r},
         \frac p2-\frac{a-p}{2r}\right).
$$
For $p=1$ this is the Mellin transform with $a=s$; for $p=2,a=2$ it is the weighted square norm $1/(2r)$.