# 2.14 — Fisher-information geometry of the normalized family

**Status [E/K].** The probability laws $`\rho(x;r,c)\,dx`$ form a two-dimensional statistical family. Once the Fisher information is **defined** as the integral of products of score functions, its intrinsic metric can be computed exactly. This is the usual location-scale geometry of a hyperbolic-secant distribution after taking logarithms; it is **not** a new physical spacetime metric.

## Coordinates and score functions

Fix a positive reference scale $`x_*`$ so all logarithms are dimensionless. Let $`Z=\log(X/x_*)`$, $`\alpha=\log(c/x_*)`$, $`r>0`$, and $`v=r(Z-\alpha)`$. The density of $`Z`$ is

```math
q_{\alpha,r}(z)=\frac r\pi\,\mathrm{sech}\bigl(r(z-\alpha)\bigr),\qquad -\infty<z<\infty.
```

The Jacobian from $`X`$ to $`Z`$ is independent of the parameters, so computing the Fisher information in this logarithmic coordinate is legitimate.

**Step 1.** Differentiate the log density at fixed observed $`z`$:

```math
s_\alpha:=\partial_\alpha\log q_{\alpha,r}=r\tanh v,\qquad s_r:=\partial_r\log q_{\alpha,r}=\frac1r-(z-\alpha)\tanh v=\frac{1-v\tanh v}{r}.
```

**Step 2.** By definition, the Fisher metric coefficients are $`I_{ij}=\mathbb E[s_i s_j]`$. The variable $`v`$ has parameter-free density $`\mathrm{sech}v/\pi`$, which is even.

## The required exact integrals

Let $`V`$ have density $`\mathrm{sech}v/\pi`$ and write $`T=\tanh V`$.

**Step 3.** The variable $`T`$ is arcsine-distributed by Chapter 1, giving $`\mathbb E[T]=0`$ and $`\mathbb E[T^2]=1/2`$.

**Step 4.** Integration by parts using $`(\mathrm{sech}v)'=-\mathrm{sech}v\tanh v`$ gives

```math
\mathbb E[V\tanh V]=-\frac1\pi\int_{\mathbb R}v\,d(\mathrm{sech}v)=\frac1\pi\int_{\mathbb R}\mathrm{sech}v\,dv=1.
```

**Step 5.** The classical Fourier integral $`\int_{\mathbb R}\mathrm{sech}v\,e^{i\omega v}\,dv=\pi\mathrm{sech}(\pi\omega/2)`$ gives

```math
\mathbb E[V^2]=-\left.\frac{d^2}{d\omega^2}\mathrm{sech}(\pi\omega/2)\right|_{\omega=0}=\frac{\pi^2}{4}.
```

**Step 6.** Differentiating $`\mathrm{sech}v\tanh v`$ and integrating by parts twice yields the related Fourier identity

```math
\int_{\mathbb R}\mathrm{sech}^3v\,e^{i\omega v}\,dv=\frac{1+\omega^2}{2}\int_{\mathbb R}\mathrm{sech}v\,e^{i\omega v}\,dv.
```

Twice differentiating this equation at $`\omega=0`$ now gives

```math
\mathbb E[V^2\mathrm{sech}^2 V]=-\frac1\pi\left.\frac{d^2}{d\omega^2}\left[\frac{\pi(1+\omega^2)}2\mathrm{sech}(\pi\omega/2)\right]\right|_{\omega=0}=\frac{\pi^2}{8}-1.
```

Hence, because $`\tanh^2 V=1-\mathrm{sech}^2V`$,

```math
\mathbb E[V^2\tanh^2V]=1+\frac{\pi^2}{8},\qquad \mathbb E[(1-V\tanh V)^2]=\frac{\pi^2}{8}.
```

All integrations and derivative interchanges are justified by exponential tails of $`\mathrm{sech}v`$.

## The exact Fisher metric

**Step 7.** The mixed coefficient vanishes by parity: $`s_\alpha`$ is odd in $`v`$, whereas $`s_r`$ is even. The other two coefficients are fixed by the integrals above:

```math
I_{\alpha\alpha}=\frac{r^2}{2},\qquad I_{\alpha r}=0,\qquad I_{rr}=\frac{\pi^2}{8r^2}.
```

Thus, with the standard Fisher convention (no additional scalar prefactor), the information line element is

```math
ds_F^2=\frac{r^2}{2}\,d\alpha^2+\frac{\pi^2}{8r^2}\,dr^2.
```

**Step 8.** Put $`t=1/r>0`$ and $`\beta=2\alpha/\pi`$. Since $`dr=-dt/t^2`$, the metric becomes

```math
ds_F^2=\frac{\pi^2}{8}\frac{d\beta^2+dt^2}{t^2}.
```

This is a constant multiple of the Poincaré metric on the upper half-plane. Its **Gaussian curvature** and two-dimensional scalar curvature are therefore

```math
K_F=-\frac{8}{\pi^2},\qquad R_F=2K_F=-\frac{16}{\pi^2}.
```

The transformation is global on the parameter domain $`(\alpha,r)\in\mathbb R\times(0,\infty)`$. Negative curvature is a theorem for this **chosen Fisher metric**; it does not follow for unrelated metrics on the framework's conformal charts.

## Compare the profile Hilbert metric

The weighted-overlap construction of [§2.13](02-13-weighted-overlap.md), restricted to fixed $`r`$, gives infinitesimal squared distance $`(r^2/3)d\alpha^2`$. The Fisher coefficient at fixed $`r`$ is $`(r^2/2)d\alpha^2`$. These differ because the first geometry uses the normalized **profile** $`f`$ in $`L^2(x\,dx)`$, whereas the second uses score functions of the normalized **probability density** $`\rho`$.
