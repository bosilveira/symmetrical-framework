# 2.2 — Inversion, oriented forms and measures

Define $I_c(x)=c^2/x$, an involution of $(0,\infty)$ with fixed point $c$. It acts on $u=\log(x/c)$ as $u\mapsto-u$. Since $S$ is even,

```math
f(I_c(x);r,c)=\frac{x^2}{c^2}f(x;r,c).\tag{2.2a}
```

This is a **weight-two covariance** of the pointwise function, not pointwise evenness.

**Oriented one-form [E].** Since $dI_c(x)=-c^2\,dx/x^2$,

```math
f(I_c(x))\,dI_c(x)=-f(x)\,dx.\tag{2.2b}
```

For the corresponding **unsigned** positive measure, the absolute Jacobian gives

```math
f(I_c(x))\,|I_c'(x)|\,dx=f(x)\,dx.
```

Thus the probability distribution with density $\rho=2rf/\pi$ is fixed by $X\mapsto c^2/X$.

**Distinguish Haar measure.** The multiplicative Haar measure transforms by $I_c^*(dx/x)=-dx/x$, but the density relative to Haar measure is $xf(x)=S/2$. The older formula

```math
f(I_c(x))\,\frac{dI_c(x)}{I_c(x)}=-f(x)\,\frac{dx}{x}
```

is **false** in general; it omits a weight factor. The correct expression on the left is $-(x^2/c^2)f(x)\,dx/x$.

**Half split.** By (2.2b), the positive integrals on $(0,c)$ and $(c,\infty)$ are equal, each $\pi/(4r)$. Inversion covariance by itself does not single out $f$: any $h(u)$ even gives $x^{-1}h(\log(x/c))$ with the same transformation law.
