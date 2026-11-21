# 1.6 — Dimensionless kernel, scaling, and Euler identity

Set $\xi=x/c$ and $k(\xi;r)=\xi^{r-1}/(1+\xi^{2r})$. Then

```math
f(x;r,c)=c^{-1}k(x/c;r).
```

This is the exact scale–shape decomposition, valid for arbitrary real $r>0$. Joint scaling gives

```math
f(\lambda x;r,\lambda c)=\lambda^{-1}f(x;r,c),\quad (x\partial_x+c\partial_c)f=-f.
```

It is a homogeneity statement at **fixed $r$**; it is not the claim that $f$ is pointwise independent of $c$.

For any integrable weight $a$ and power $p>0$,

```math
\int_0^\infty x^{a-1}f(x;r,c)^p\,dx =c^{a-p}\int_0^\infty \xi^{a-1}k(\xi;r)^p\,d\xi,
```

whenever the integral converges. Thus dimensional analysis gives the entire dependence on $c$, while $r$ governs integrability.

**Parameter differentiation.** At fixed $x$ and $c$ with $u=\log(x/c)$,

```math
\partial_r f=-uWf,\qquad \partial_c f=\frac{rW}{c}f.
```

At fixed $u$, $\partial_c f(ce^u;r,c)=-f(ce^u;r,c)/c$ instead. The phrase “differentiate at fixed coordinate” must specify which coordinate is held fixed.

## Detailed algebraic proof of the scale decomposition

The former notes contained a useful explicit calculation, which is short enough to retain in full.

**Step 1.** Substitute $x=c\xi$, with $\xi>0$, into the original definition:

```math
f(c\xi;r,c)=\frac{c^r(c\xi)^{r-1}}{c^{2r}+(c\xi)^{2r}}.
```

**Step 2.** Factor the powers of $c$ separately in numerator and denominator:

```math
f(c\xi;r,c)=\frac{c^{2r-1}\xi^{r-1}}{c^{2r}(1+\xi^{2r})}.
```

**Step 3.** Cancel the common factor:

```math
f(c\xi;r,c)=\frac1c\frac{\xi^{r-1}}{1+\xi^{2r}}=\frac1c k(\xi;r).
```

**Step 4.** Scaling both positive arguments by $\lambda$ leaves $\xi=x/c$ unchanged; differentiating $f(\lambda x;r,\lambda c)=\lambda^{-1}f(x;r,c)$ at $\lambda=1$ yields the Euler PDE quoted above. This computation does not impose an algebraic or integrality restriction on $r$.
