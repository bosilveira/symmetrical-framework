# 1.7 — Probability density, CDF, quantiles, and arcsine coordinate

Because $f(x)\,dx=\tfrac12S\,du$ and $\int_{\mathbb R}\operatorname{sech}(ru)\,du=\pi/r$, the mass is $\int_0^\infty f\,dx=\pi/(2r)$.

**[E]** The probability density and CDF are
$$
\rho(x;r,c)=\frac{2r}{\pi}f(x;r,c),\qquad
F(x;r,c)=\frac2\pi\arctan\!\left((x/c)^r\right).
$$
The derivative of the displayed CDF equals $\rho$; its limits at $0$ and infinity are $0$ and $1$. Hence the quantile function is
$$
F^{-1}(v)=c\,\tan^{1/r}\left(\frac{\pi v}{2}\right),\qquad 0<v<1,
$$
and the median is $c$. The centered logarithmic variable $U=\log(X/c)$ has density $r\operatorname{sech}(ru)/\pi$ and is symmetric.

The alternative Gudermannian form, with principal $\arctan\in(-\pi/2,\pi/2)$, is
$$
F(x)=\frac12+\frac1\pi\arctan(\sinh(ru)).
$$
No branch jump occurs for real $u$.

**Arcsine pushforward [E].** Put $Z=W(X)=\tanh(rU)$. Since $dZ/du=r(1-Z^2)$,
$$
p_Z(z)=\frac{1}{\pi\sqrt{1-z^2}},\qquad -1<z<1.
$$
Equivalently $P=(1+Z)/2\sim\mathrm{Beta}(1/2,1/2)$, not a uniform distribution. Another canonical pushforward, $T=(X/c)^r$, has standard half-Cauchy density $2/[\pi(1+T^2)]$.

**Moment domain.** For complex $a$ satisfying $|\Re a|<r$, the power moment is
$$
\mathbb E[X^a]=c^a\sec\!\left(\frac{\pi a}{2r}\right).
$$
Values of the meromorphic continuation outside the strip are **not** probabilistic moments.