# 4.7 — $r=2$: a lemniscatic substitution is not an elliptic reduction

At $r=2$, the dimensionless kernel and its derivative are

```math
k_2(t)=\frac{t}{1+t^4},\qquad k_2'(t)=\frac{1-3t^4}{(1+t^4)^2}.
```

Thus its graph length is

```math
L_2(0,1)=\int_0^1 \frac{\sqrt{(1+t^4)^4+(1-3t^4)^2}}{(1+t^4)^2}\,dt.
```

The *lemniscatic curve* $v^2=1-t^4$ is elliptic (nonsingular quartic). On its real branch let

```math
s=\int_0^t\frac{d\xi}{\sqrt{1-\xi^4}},\quad t=\operatorname{sl}(s),\quad \varpi=\int_0^1\frac{dt}{\sqrt{1-t^4}}.
```

Then $dt=\sqrt{1-t^4}\,ds$, so the **correct** transformed arc integral is

```math
L_2(0,1)=\int_0^{\varpi} \frac{\sqrt{(1-t(s)^4)\left[(1+t(s)^4)^4+(1-3t(s)^4)^2\right]}} {(1+t(s)^4)^2}\,ds.
```

The old draft mistakenly inserted another factor of $(1-t^4)$ into the second term of the radicand.

**What is established:** this is an exact reparametrization by a lemniscatic coordinate. **What is not established:** that the graph-length differential is the pullback of a differential on the genus-one curve $v^2=1-t^4$, or is expressible solely via Legendre elliptic integrals. The extra square root in the arc integrand is a separate algebraic extension, and must be analyzed independently.

For comparison, the original integral of $f(x;2,c)$ is elementary:

```math
\int f(x;2,c)\,dx=\frac12\arctan((x/c)^2)+C.
```

This arctangent primitive and the lemniscatic period $\varpi$ are distinct objects; a quartic denominator alone does not identify them.
