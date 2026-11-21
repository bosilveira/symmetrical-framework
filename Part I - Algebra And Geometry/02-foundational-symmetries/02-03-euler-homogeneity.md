# 2.3 — Euler homogeneity in $x$ and $c$

For fixed $r>0$, $f(x;r,c)=c^{-1}k(x/c;r)$ implies
$$
\boxed{f(\lambda x;r,\lambda c)=\lambda^{-1}f(x;r,c)}
\qquad(\lambda>0).
$$
Differentiate at $\lambda=1$ to obtain Euler's identity **[E]**:
$$
\boxed{(x\partial_x+c\partial_c+1)f=0.}
$$
Conversely, on the connected positive quadrant, a differentiable solution of this PDE has the form $c^{-1}k(x/c)$ for some function $k$, by characteristics. This converse does not select the framework's specific $k$.

**Commutation with inversion.** Inversions respect joint scaling:
$$
I_{\lambda c}(\lambda x)=\lambda I_c(x).
$$
Hence scale covariance and inversion covariance are compatible but logically separate conditions.

**Scale transport of integrals.** With $x=c\xi$,
$$
\int_0^\infty x^{a-1}f(x;r,c)^p\,dx
=c^{a-p} \int_0^\infty \xi^{a-1}k(\xi;r)^p\,d\xi,
$$
in its convergence domain. This furnishes a clean, falsifiable dimensional check for every claimed integral identity.

**Derivative conventions.** The Euler vector field $x\partial_x+c\partial_c$ keeps the ratio $x/c$ fixed. It is **not** the same as the operator $D_x=x\partial_x$ with $c$ fixed; the latter equals $\partial_u$ in the logarithmic chart.