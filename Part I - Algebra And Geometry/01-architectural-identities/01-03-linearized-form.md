# 1.3 — Three logarithmic objects, distinguished precisely

Let $x=ce^u$ with $c>0$, so that $dx=x\,du$ and $dx/x=du$.

1. **Pointwise pullback**:
   $$g(u;r,c):=f(ce^u;r,c)=\frac{e^{-u}}{2c}\operatorname{sech}(ru).$$
   This is generally **not** even and is not a probability density with respect to $du$.

2. **Pushforward of the normalized probability law**: let
   $$\rho(x;r,c)=\frac{2r}{\pi}f(x;r,c).$$
   For $U=\log(X/c)$ and $X\sim\rho(x)\,dx$, the density of $U$ is
   $$p(u;r)=x\rho(x;r,c)\big|_{x=ce^u}
           =\frac r\pi\operatorname{sech}(ru).$$
   This integrates to one and is even. Its formula has no $c$ because the coordinate $U$ itself depends on $c$.

3. **Hyperbolic phase**:
   $$W(u;r)=\tanh(ru),\qquad W_u=r(1-W^2).$$
   This is an odd, dimensionless coordinate, not a probability density.

**Haar versus ordinary density.** The invariant multiplicative Haar measure is $dx/x$. The unnormalized measure $f(x)\,dx$ has density $xf(x)=S/2$ relative to Haar measure:
$$
f(x)\,dx=(xf(x))\frac{dx}{x}=\frac12S(u)\,du.
$$
Thus the functions $f(ce^u)$, $xf(x)$ and $p(u)$ are different, even though they arise from the same kernel.

**Weighted $L^2$ isometry.** Setting $y(u)=2xf(x)$,
$$
\int_0^\infty x|f(x)|^2\,dx=\frac14\int_{\mathbb R}|y(u)|^2\,du.
$$
This equality is a change-of-measure theorem, and later underlies the finite-norm Master classification.