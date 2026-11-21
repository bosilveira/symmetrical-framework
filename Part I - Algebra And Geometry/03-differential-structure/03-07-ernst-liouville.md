# 3.7 — Radial Liouville identity and constant-curvature metric

Let $`\rho=|z|>0`$ be the radius in the punctured plane $`\mathbb C^\times`$, and put $`u=\log(\rho/c)`$. Define $`F(\rho)=f(\rho;r,c)>0`$. For a radial scalar $`\phi(\rho)`$ the Euclidean two-dimensional Laplacian is

```math
\Delta_2\phi=\phi_{\rho\rho}+\frac1\rho\phi_\rho =\frac1{\rho^2}\frac{d^2\phi}{du^2}.
```

Since $`\log F=-\log(2\rho)+\log\mathrm{sech}(ru)`$, we have

```math
\frac{d^2}{du^2}\log F=-r^2\mathrm{sech}^2(ru),
```

and therefore **[E]**

```math
\Delta_2\log F=-4r^2F^2.\tag{L}
```

This is a (negative-sign) Liouville equation for $`\phi=\log F`$: $`\Delta_2\phi=-4r^2e^{2\phi}`$.

**Geometric construction [K/E].** Declare the conformal metric

```math
g=F(\rho)^2(d\rho^2+\rho^2d\vartheta^2) =\tfrac14\mathrm{sech}^2(ru)(du^2+d\vartheta^2).
```

For a conformal planar metric $`g=e^{2\phi}g_{\rm Eucl}`$ its Gaussian curvature is $`K=-e^{-2\phi}\Delta_2\phi`$. By (L),

```math
K_g=4r^2.
```

With $`\vartheta\sim\vartheta+2\pi`$, its area is $`\pi/r`$. Near each end $`u\to\pm\infty`$ the completion is a cone with total angle $`2\pi r`$. In particular for $`r=1`$ the completion is a smooth round sphere of curvature $`4`$; for other $`r`$ the conical completion is not a globally smooth sphere with the standard angular period. The Gauss–Bonnet identity including two cone deficits reads

```math
(4r^2)\frac{\pi}{r}+2\,[2\pi(1-r)]=4\pi.
```

**Ernst qualification.** Static-axisymmetric vacuum Ernst reductions lead to harmonic potentials under their own ansatz and coordinates. Equation (L) has a nonzero source, so it does **not** prove that $`F`$ solves a vacuum Einstein system. The statement here is the exact radial Liouville calculation and the explicitly chosen constant-curvature metric.

## Direct spatial Liouville proof

The historical notes derive the same identity by differentiating $`\log f`$ directly in the original radial coordinate.

**Step 1.** The Euler relation yields

```math
(\log f)_\rho=-\frac{1+rW}{\rho}.
```

**Step 2.** Differentiate and substitute $`\rho W_\rho=rS^2`$:

```math
(\log f)_{\rho\rho}=\frac{1+rW-r^2S^2}{\rho^2}.
```

**Step 3.** Add the radial Laplacian term:

```math
(\log f)_{\rho\rho}+\frac{1}{\rho}(\log f)_\rho=-\frac{r^2S^2}{\rho^2}=-4r^2f(\rho)^2.
```

This is an exact scalar identity. It is not itself a derived physical energy-density equation.
