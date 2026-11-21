# 2.4 — Reciprocal closure of the normalized law

Let $`X`$ have density $`\rho(x;r,c)=(2r/\pi)f(x;r,c)`$ on $`(0,\infty)`$. For $`Y=1/X`$,

```math
p_Y(y)=\rho(1/y;r,c)\frac1{y^2}.
```

Direct algebra using $`f(x;r,c)=c^r x^{r-1}/(c^{2r}+x^{2r})`$ gives

```math
p_Y(y)=\rho(y;r,c^{-1}),\qquad y>0.
```

This is the exact reciprocal-closure theorem **[E]**. The transformed variable is measured in reciprocal units: if $`c`$ has the units of $`X`$, then $`c^{-1}`$ has the units of $`Y`$.

A different, fixed-parameter involution is

```math
X\longmapsto\frac{c^2}{X}.
```

It leaves the law $`\rho(\,\cdot\,;r,c)`$ invariant, because its log-coordinate $`U=\log(X/c)`$ has a symmetric density and transforms to $`-U`$.

**Distributional consequence.** For all real $`a`$ with $`|a|<r`$,

```math
\mathbb E[X^a]=c^a\sec\left(\frac{\pi a}{2r}\right), \qquad \mathbb E[(c^2/X)^a]=\mathbb E[X^a].
```

There is no independent random variable involved in these deterministic transformations.

## Proof directly in the logarithmic coordinate

Fix a positive reference unit $`x_*`$. Set $`Z=\log(X/x_*)`$ and $`\alpha=\log(c/x_*)`$. From the Jacobian $`dx=x\,dz`$, the density of $`Z`$ is

```math
q_{r,\alpha}(z)=\frac r\pi\,\mathrm{sech}(r(z-\alpha)).
```

For the reciprocal variable $`Y=1/X`$ choose the reciprocal reference unit $`y_*=1/x_*`$. Then $`\log(Y/y_*)=-Z`$ has density $`q_{r,-\alpha}`$, because $`\mathrm{sech}`$ is even. Its center is $`-\alpha=\log((1/c)/y_*)`$, so exponentiating proves $`1/X\sim\rho(\cdot;r,1/c)`$ without redoing the quotient algebra.

## Reciprocal moments and an exact self-dual relation

For $`|\Re s|<r`$, the Mellin formula of Chapter 1 gives

```math
\mathbb E[X^s]=c^s\sec\left(\frac{\pi s}{2r}\right),\qquad \mathbb E[X^s]=c^{2s}\mathbb E[X^{-s}].
```

Here $`X^s`$ means $`\exp(s\log X)`$, unambiguous for positive real $`X`$. The second identity follows from $`\mathbb E[(c^2/X)^s]=\mathbb E[X^s]`$. It is equivalent to the Mellin reflection law, **not** a statement that all positive-order moments exist: the strict strip is indispensable.

As a separate consequence, $`\mathbb E[\log X]=\log c`$, since the logarithmic density is even and has exponential tails. Thus $`c`$ is simultaneously the median and the geometric mean of $`X`$; neither claim says that $`\mathbb E[X]`$ exists when $`r\le1`$.

## Direct reciprocal Jacobian proof retained from the draft

The logarithmic reflection argument gives the conceptual reason for closure. For an independent check, the source also uses the explicit algebraic density.

**Step 1.** With $`Y=1/X`$, take $`x=1/y`$ and $`|dx/dy|=1/y^2`$.

**Step 2.** Substitute $`x=1/y`$ into the density and multiply the fraction by $`y^{2r}/y^{2r}`$:

```math
p_Y(y)=\frac{2r}{\pi}\frac{c^ry^{1-r}}{c^{2r}+y^{-2r}}\frac1{y^2}=\frac{2r}{\pi}\frac{c^ry^{r-1}}{1+c^{2r}y^{2r}}.
```

**Step 3.** Divide numerator and denominator by $`c^{2r}`$:

```math
p_Y(y)=\frac{2r}{\pi}\frac{c^{-r}y^{r-1}}{c^{-2r}+y^{2r}}=\rho(y;r,c^{-1}).
```

This argument explicitly retains the **absolute** Jacobian and proves closure of the normalized probability *measure*, not pointwise invariance of the density.

The centered displacement $`Z-\alpha=\log(X/c)`$ remains dimensionless, and using $`y_*=1/x_*`$ keeps the reciprocal coordinate dimensionless as well.
