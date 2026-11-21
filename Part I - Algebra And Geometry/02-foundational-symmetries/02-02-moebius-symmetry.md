# 2.2 — Inversion, oriented forms and measures

Define $`I_c(x)=c^2/x`$, an involution of $`(0,\infty)`$ with fixed point $`c`$. It acts on $`u=\log(x/c)`$ as $`u\mapsto-u`$. Since $`S`$ is even,

```math
f(I_c(x);r,c)=\frac{x^2}{c^2}f(x;r,c).\tag{2.2a}
```

This is a **weight-two covariance** of the pointwise function, not pointwise evenness.

**Oriented one-form [E].** Since $`dI_c(x)=-c^2\,dx/x^2`$,

```math
f(I_c(x))\,dI_c(x)=-f(x)\,dx.\tag{2.2b}
```

For the corresponding **unsigned** positive measure, the absolute Jacobian gives

```math
f(I_c(x))\,|I_c'(x)|\,dx=f(x)\,dx.
```

Thus the probability distribution with density $`\rho=2rf/\pi`$ is fixed by $`X\mapsto c^2/X`$.

**Distinguish Haar measure.** The multiplicative Haar measure transforms by $`I_c^*(dx/x)=-dx/x`$, but the density relative to Haar measure is $`xf(x)=S/2`$. The older formula

```math
f(I_c(x))\,\frac{dI_c(x)}{I_c(x)}=-f(x)\,\frac{dx}{x}
```

is **false** in general; it omits a weight factor. The correct expression on the left is $`-(x^2/c^2)f(x)\,dx/x`$.

**Half split.** By (2.2b), the positive integrals on $`(0,c)`$ and $`(c,\infty)`$ are equal, each $`\pi/(4r)`$. Inversion covariance by itself does not single out $`f`$: any $`h(u)`$ even gives $`x^{-1}h(\log(x/c))`$ with the same transformation law.

## Inversion as reflection in logarithmic coordinates

The conjugacy of multiplicative inversion to reflection is exact. Write $`L_c(x)=\log(x/c)`$ and $`R(u)=-u`$; then

```math
I_c=L_c^{-1}\circ R\circ L_c,\qquad I_c(I_c(x))=x,\qquad I_c(c)=c.
```

In particular, $`I_c`$ is a Möbius transformation of the positive coordinate $`x`$ (a fractional-linear map), but **not every Möbius map** preserves the positive half-line or the normalized family.

## Classification of invariant one-dimensional densities

Suppose $`h`$ is measurable and nonnegative on $`\mathbb R`$ and define $`q_h(x)=h(\log(x/c))/x`$.

**Step 1.** Substituting $`I_c(x)=c^2/x`$ gives $`L_c(I_c(x))=-L_c(x)`$.

**Step 2.** Multiply $`q_h(I_c(x))`$ by the absolute Jacobian $`|I_c'(x)|=c^2/x^2`$:

```math
q_h(I_c(x))|I_c'(x)|=\frac{h(-u)}{x}.
```

**Step 3.** It follows that $`q_h(x)\,dx`$ is invariant as a positive measure **if and only if** $`h(-u)=h(u)`$ almost everywhere. If $`\int_{\mathbb R}h(u)\,du=1`$, the resulting measure is a probability measure with median $`c`$ whenever $`h`$ is positive almost everywhere.

The framework picks the specific even function $`h(u)=\frac12\mathrm{sech}(ru)`$ before normalization; inversion covariance alone does not distinguish it from infinitely many other even profiles.

## Distributional reflection and quantiles

Let $`F`$ be the normalized CDF and $`Q=F^{-1}`$. The invariance of the law implies

```math
F(c^2/x)=1-F(x),\qquad Q(1-v)=\frac{c^2}{Q(v)},\qquad 0<v<1.
```

The first identity also follows from $`\arctan a+\arctan(1/a)=\pi/2`$ for $`a>0`$. It is a strong consistency check between inversion, probability normalization and quantile geometry. The same equality extends to any strictly increasing continuous CDF whose log-density is even.
