# 05.01 — Canonical surface: a chosen catenoid immersion

**Source:** SF-DRAFT-030 §§2–3, with the exact parametric formulas reproduced here as a **selected construction**. Nothing in $`f(x;r,c)`$ uniquely determines this Euclidean immersion.

## Variables and new geometric data

Let $`x,c,r>0`$, $`u=\log(x/c)`$, $`R(u)=\cosh(ru)`$, $`S=1/R`$, $`W=\tanh(ru)`$. Introduce an **independent** surface coordinate $`v`$; for the global catenoid take $`v\sim v+2\pi/r`$.

Choose the map into Euclidean three-space (in fixed numerical coordinate units)

```math
X(u,v)=\left(\frac{R(u)}r\cos(rv),\frac{R(u)}r\sin(rv),u\right).
```

The new coordinate $`v`$ and the ambient Euclidean metric are *additional inputs*, not transformations of the original one-dimensional spatial coordinate $`x`$.

## Jacobian and metric pullback

Differentiate with respect to the declared independent variables:

```math
X_u=(\sinh(ru)\cos(rv),\sinh(ru)\sin(rv),1),\qquad X_v=(-R\sin(rv),R\cos(rv),0).
```

The Euclidean metric pullback is

```math
I=X^*g_{\mathbb R^3}=R^2(du^2+dv^2),\qquad dA_I=R^2\,du\,dv.
```

This area form is **not** the original one-dimensional probability measure $`f(x)\,dx`$ or weighted classification norm $`xF^2\,dx`$; a claimed relationship requires a separate integration/pullback map.

## Second fundamental form and curvature

Choose the oriented normal $`N=(-S\cos(rv),-S\sin(rv),W)`$. The second form and shape map are

```math
II=-r\,du^2+r\,dv^2,\qquad B=I^{-1}II=\mathrm{diag}(-rS^2,rS^2).
```

Hence

```math
H=\frac12\mathrm{tr}B=0,\qquad K=\det B=-r^2S^4.
```

The intrinsic expression agrees independently: with $`h(u)=\log R(u)`$,

```math
K=-R^{-2}h_{uu}=-r^2S^4,\qquad h_u=rW,\qquad h_{uu}=r^2S^2.
```

Thus the same scalar pair $`S,W`$ provides a convenient chart for **this** minimal immersion, but it is not a uniqueness theorem over all immersions.

**Source status:** SF-DRAFT-030 has stepwise derivations and internal checks but remains a *provisional research source* for its broader network of geometric correspondences. See the [geometric-dictionary source](../../research/active-drafts/030%20Connections%20and%20Differential-Geometric%20Operators%20of%20the%20Canonical%20Surface.md) §§3–6 for precise frame conventions.
