# 06.01 — Kink variational class and the order-one Pöschl–Teller factorization

**Status:** classical variational completion-of-squares and spectral factorizations derived from the selected fields $`S=\mathrm{sech}(ru)`$ and $`W=\tanh(ru)`$. The functional and Schrödinger operator are **additional mathematical choices**; they must not be identified automatically with the full cubic Master or an arbitrary Sturm–Liouville boundary-value problem. Source: November 16 Complete Reference v2 §§F/14–16, November 21 ZIP `04-follow-ups/profile-web.md`, and the maintained [catenoid Jacobi-mode audit §00.10](../00-foundations/00-10-symmetric-square-lorentz-hessian.md).

Fix $`r,c>0`$, $`u=\log(x/c)`$, $`\theta=ru`$, and set $`H:=S^2`$ as a **local abbreviation** only. Derivatives throughout this chapter are in $`u`$ at fixed $`r,c`$, unless stated otherwise.

## 1. An explicit finite-energy kink problem

Choose the functional

```math
E_r[w]=\frac12\int_{\mathbb R}\left(w_u^2+r^2(1-w^2)^2\right)du.
```

The admissible topological class consists of real locally absolutely continuous $`w`$ with $`w_u\in L^2(\mathbb R)`$, $`1-w^2\in L^2(\mathbb R)`$, and endpoint limits $`w(-\infty)=-1`$, $`w(+\infty)=1`$. This is an *affine finite-energy Sobolev class*, **not** all of $`H^1(\mathbb R)`$: the kink itself is not square integrable.

Complete the square without omitting the boundary term:

```math
E_r[w]=\frac12\int_{\mathbb R}\left(w_u-r(1-w^2)\right)^2du+r\int_{\mathbb R}w_u(1-w^2)\,du.
```

The last integral is a primitive with the specified limits:

```math
\int_{\mathbb R}w_u(1-w^2)\,du=\left[w-\frac{w^3}{3}\right]_{-\infty}^{+\infty}=\frac43.
```

Hence

```math
E_r[w]\ge\frac{4r}{3},\qquad E_r[w]=\frac{4r}{3}\ \Longleftrightarrow\ w_u=r(1-w^2)\ \text{a.e.}
```

The monotone finite-energy equality profiles are $`w(u)=\tanh[r(u-u_0)]`$ with arbitrary $`u_0\in\mathbb R`$. The canonical centered profile is $`W=\tanh(ru)`$, with the center at $`x=c`$; a translated kink is centered at $`x_0=ce^{u_0}`$. Directly, $`W_u=rS^2`$ and $`E_r[W]=4r/3`$.

The Euler–Lagrange equation of this **chosen** functional is

```math
w_{uu}=2r^2w(w^2-1).
```

This is the familiar $`\phi^4`$ kink equation. The energy bound requires the specified boundary conditions; it is not a universal Sobolev embedding statement.

## 2. Spectral factorization and the soliton/kink pair

On a dense smooth test domain in $`L^2(\mathbb R,du)`$, set

```math
A_r=\partial_u+rW,\qquad A_r^\dagger=-\partial_u+rW.
```

The factorization follows by product differentiation and $`W_u=rS^2`$:

```math
A_r^\dagger A_r=-\partial_u^2+r^2-2r^2S^2,\qquad A_rA_r^\dagger=-\partial_u^2+r^2.
```

Define the selected Schrödinger operator $`L_r=-\partial_u^2-2r^2S^2`$ with its usual self-adjoint realization on $`H^2(\mathbb R)`$. Thus

```math
L_r=A_r^\dagger A_r-r^2,\qquad L_rS=-r^2S,\qquad L_rW=0.
```

The field $`S`$ is an $`L^2`$ eigenfunction, with $`\int_{\mathbb R}S^2du=2/r`$. The field $`W`$ is **bounded but not in $`L^2(\mathbb R)`$**; the equation $`L_rW=0`$ is a generalized zero-energy threshold/resonance relation, not a second discrete eigenstate. The factorization shows $`L_r\ge-r^2`$ in the quadratic-form sense. The partner $`A_rA_r^\dagger-r^2=-\partial_u^2`$ is free, establishing the usual order-one Pöschl–Teller/Darboux correspondence.

## 3. Surface Jacobi equations require angular-mode data

For the explicitly chosen catenoid $`\mathbf X(\theta,\varphi)=a_0(\cosh\theta\cos\varphi,\cosh\theta\sin\varphi,\theta)`$, the Jacobi operator from [§00.10](../00-foundations/00-10-symmetric-square-lorentz-hessian.md) reduces at angular Fourier mode $`n`$ to

```math
h_n''+(2\,\mathrm{sech}^2\theta-n^2)h_n=0.
```

Here the prime means **$`d/d\theta`$**, not $`d/du`$. The modes are distinct:

| Field | Angular mode | Equation in $`\theta`$ | Spectral classification |
|---|---|---|---|
| $`W=\tanh\theta`$ | $`n=0`$ | $`W_{\theta\theta}+2S^2W=0`$ | Bounded threshold profile |
| $`S=\mathrm{sech}\theta`$ | $`n=1`$ | $`S_{\theta\theta}+(2S^2-1)S=0`$ | Square-integrable bound profile |

Substitution $`\theta=ru`$ reinstates the factors of $`r^2`$ in the one-dimensional equations. The geometric identification is valid **for this operator and chosen immersion**, not for every surface with a conformal coordinate.

## 4. Editorial boundary

The same elementary profiles therefore participate in both a **chosen variational problem** and a **chosen spectral factorization**. Their identity as functions is exact; equality of the full solution spaces, an automatic reduction from a higher-dimensional PDE, and physical realization are **not** consequences of these formulas.

**Related:** [elementary-function web](../00-foundations/00-11-elementary-function-web.md), [Master separatrix/classification](../01-master-equation/01-02-classification.md), [norms](../02-calculus-norms/02-03-norms.md), [chosen Hopf–Villarceau lift](../05-differential-geometry/05-04-hopf-villarceau-selected-lift.md), and [verification](../_standards/verify_elementary_function_web.py).
