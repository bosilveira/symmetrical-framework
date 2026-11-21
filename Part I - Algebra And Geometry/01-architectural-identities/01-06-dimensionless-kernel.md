# 1.6 — Dimensionless kernel, scaling, and Euler identity

Set $\xi=x/c$ and $k(\xi;r)=\xi^{r-1}/(1+\xi^{2r})$. Then
$$
\boxed{f(x;r,c)=c^{-1}k(x/c;r)}.
$$
This is the exact scale–shape decomposition, valid for arbitrary real $r>0$. Joint scaling gives
$$
f(\lambda x;r,\lambda c)=\lambda^{-1}f(x;r,c),\quad
(x\partial_x+c\partial_c)f=-f.
$$
It is a homogeneity statement at **fixed $r$**; it is not the claim that $f$ is pointwise independent of $c$.

For any integrable weight $a$ and power $p>0$,
$$
\int_0^\infty x^{a-1}f(x;r,c)^p\,dx
=c^{a-p}\int_0^\infty \xi^{a-1}k(\xi;r)^p\,d\xi,
$$
whenever the integral converges. Thus dimensional analysis gives the entire dependence on $c$, while $r$ governs integrability.

**Parameter differentiation.** At fixed $x$ and $c$ with $u=\log(x/c)$,
$$
\partial_r f=-uWf,\qquad
\partial_c f=\frac{rW}{c}f.
$$
At fixed $u$, $\partial_c f(ce^u;r,c)=-f(ce^u;r,c)/c$ instead. The phrase “differentiate at fixed coordinate” must specify which coordinate is held fixed.