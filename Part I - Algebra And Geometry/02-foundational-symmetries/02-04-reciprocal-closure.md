# 2.4 — Reciprocal closure of the normalized law

Let $X$ have density $\rho(x;r,c)=(2r/\pi)f(x;r,c)$ on $(0,\infty)$. For $Y=1/X$,

```math
p_Y(y)=\rho(1/y;r,c)\frac1{y^2}.
```

Direct algebra using $f(x;r,c)=c^r x^{r-1}/(c^{2r}+x^{2r})$ gives

```math
p_Y(y)=\rho(y;r,c^{-1}),\qquad y>0.
```

This is the exact reciprocal-closure theorem **[E]**. The transformed variable is measured in reciprocal units: if $c$ has the units of $X$, then $c^{-1}$ has the units of $Y$.

A different, fixed-parameter involution is

```math
X\longmapsto\frac{c^2}{X}.
```

It leaves the law $\rho(\,\cdot\,;r,c)$ invariant, because its log-coordinate $U=\log(X/c)$ has a symmetric density and transforms to $-U$.

**Distributional consequence.** For all real $a$ with $|a|<r$,

```math
\mathbb E[X^a]=c^a\sec\left(\frac{\pi a}{2r}\right), \qquad \mathbb E[(c^2/X)^a]=\mathbb E[X^a].
```

There is no independent random variable involved in these deterministic transformations.
