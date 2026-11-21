# 05.04 — Hopf–Villarceau as a selected lift of the conic fields

**Status:** a mathematically specified **additional geometric construction** on the foundational circle $`S^2+W^2=1`$. The algebraic identities below follow from the chosen phases, the Hopf map and stereographic projection. The scalar kernel and the cubic Master **do not uniquely determine** the phases, a circle bundle connection, an embedding or a physical model. Source: November 21 ZIP `05-companion/hopf-villarceau-atlas/hopf-villarceau-notes.md` §§1–5 and the companion README/validation record. The source's cited external papers were not independently examined for this chapter.

## 1. Domain, notation and the independent phase data

Fix $`r,c>0`$ and a point $`x>c`$, so $`\theta=r\log(x/c)>0`$. Define

```math
S=\mathrm{sech}\theta,\quad W=\tanh\theta,\quad R=\cosh\theta,\quad b=\sinh\theta,\quad \eta=\mathrm{gd}(\theta)=\arctan b,\quad S^2+W^2=1.
```

The restricted domain $`\theta>0`$ ensures $`S,W>0`$ and gives a nondegenerate two-torus. Negative $`\theta`$ can be handled by absorbing the sign of $`W`$ into a phase; at $`\theta=0`$ the torus degenerates. Let $`\alpha,\beta\in\mathbb R/(2\pi\mathbb Z)`$ be **independent, newly chosen** phases, and set

```math
\Psi(\alpha,\beta)=\begin{pmatrix}Se^{i\alpha}\\We^{i\beta}\end{pmatrix}\in S^3\subset\mathbb C^2,\qquad U(\Psi)=\begin{pmatrix}Se^{i\alpha}&-We^{-i\beta}\\We^{i\beta}&Se^{-i\alpha}\end{pmatrix}\in SU(2).
```

The determinant is $`S^2+W^2=1`$. For fixed $`\theta`$ this defines the product torus $`T_\theta=S^1(S)\times S^1(W)`$ inside the round unit three-sphere. This is the precise additional datum behind the Hopf–Villarceau discussion.

## 2. Compare three inequivalent projections

Write $`\Psi=(a+ia_0,z+id)`$, so $`a=S\cos\alpha`$, $`a_0=S\sin\alpha`$, $`z=W\cos\beta`$, $`d=W\sin\beta`$. Choose the north pole $`N=(0,0,0,1)`$ of $`S^3`$ and set $`\delta=\beta-\alpha`$.

| Map | Explicit expression | Image of $`T_\theta`$ | Information lost / retained |
|---|---|---|---|
| Stereographic $`\sigma_N`$ | $`(a,a_0,z)/(1-d)`$ | Ring torus in $`\mathbb R^3`$ | Conformal diffeomorphism on $`S^3\setminus\{N\}`$; no points of $`T_\theta`$ at $`N`$ |
| Orthogonal $`\pi_d`$ | $`(a,a_0,z)`$ | Cylinder lateral surface $`\rho=S,\ -W\le z\le W`$ | Generically two preimages; boundary folds |
| Hopf quotient $`h`$ | $`(2\mathrm{Re}(\bar z_1z_2),2\mathrm{Im}(\bar z_1z_2),\lvert z_1\rvert^2-\lvert z_2\rvert^2)`$ | Latitude circle in $`S^2`$ | Collapses common-phase $`S^1`$ fibres |

In stereographic coordinates $`(X,Y,Z)`$,

```math
(X,Y,Z)=\frac{(S\cos\alpha,S\sin\alpha,W\cos\beta)}{1-W\sin\beta},\qquad \rho=\sqrt{X^2+Y^2}.
```

The image satisfies the **Euclidean ring-torus equation**

```math
(\rho-R)^2+Z^2=b^2,\qquad R^2-b^2=1.
```

For fixed $`\theta>0`$ the denominator is positive because $`0<W<1`$. The major and minor radii are $`R=1/S`$ and $`b=W/S`$; their appearance is a consequence of this particular stereographic pole and normalization, not a claim about arbitrary projections.

## 3. Hopf fibres, the two Villarceau rulings and angles

The chosen Hopf map and the phase difference give

```math
h(\Psi)=n=(2SW\cos\delta,2SW\sin\delta,S^2-W^2)=(\sin(2\eta)\cos\delta,\sin(2\eta)\sin\delta,\cos(2\eta)).
```

Thus the selected torus projects to a latitude on $`S^2`$, and **common phase shift** $`(\alpha,\beta)\mapsto(\alpha+t,\beta+t)`$ follows a single Hopf fibre. The opposite diagonal $`(\alpha,\beta)\mapsto(\alpha+t,\beta-t)`$ is a circle of the *opposite* Villarceau ruling, not generally a fibre of the same chosen Hopf quotient.

| Phase restriction | Curve on the torus | Stereographic circle family |
|---|---|---|
| $`\alpha=\alpha_0`$ | First phase fixed | Meridian |
| $`\beta=\beta_0`$ | Second phase fixed | Parallel |
| $`\beta-\alpha=\delta`$ | Common phase evolves | Chosen Hopf/Villarceau ruling |
| $`\beta+\alpha=\delta`$ | Opposite phases evolve | Opposite Villarceau ruling |

For the first Villarceau ruling, write $`\alpha=t`$ and $`\beta=t+\delta`$. Its stereographic image lies in a plane and on a Euclidean circle:

```math
Z=b(X\cos\delta-Y\sin\delta),\qquad (X-b\sin\delta)^2+(Y-b\cos\delta)^2+Z^2=R^2.
```

In particular the circle has radius $`R`$ and center $`(b\sin\delta,b\cos\delta,0)`$. These identities follow by direct substitution using $`S^2+W^2=1`$. Two opposite rulings have an oriented crossing angle $`\chi=2\eta`$; the smaller unoriented crossing angle is $`\min(\chi,\pi-\chi)`$. The Clifford torus occurs at $`S=W=1/\sqrt2`$, i.e. $`\theta=\log(1+\sqrt2)`$, with perpendicular rulings.

## 4. Gudermannian derivatives: harmonic double-angle on the base

The fields $`S=\cos\eta`$ and $`W=\sin\eta`$ satisfy $`S_{\eta\eta}=-S`$ and $`W_{\eta\eta}=-W`$. Holding $`\delta`$ fixed gives the exact **base-sphere comparison**

```math
n_\eta=2(\cos(2\eta)\cos\delta,\cos(2\eta)\sin\delta,-\sin(2\eta)),\qquad n_{\eta\eta}=-4n,\qquad |n_\eta|=2.
```

This frequency doubling is the Hopf quotient's double-angle map, **not** a doubling of the resolution parameter $`r`$ in the original spatial family. Since $`\eta_u=rS`$, the speed along this base meridian is $`|n_u|=2rS`$. If the phases are constant when $`x,c,r`$ vary, then

```math
|n_r|_{x,c}=2|u|S,\qquad |n_c|_{x,r}=\frac{2rS}{c},\qquad |n_x|_{c,r}=\frac{2rS}{x}.
```

The full second parameter derivatives of each Cartesian component of $`n`$ follow from the universal Hessian in [§00.09](../00-foundations/00-09-second-derivative-charts.md), using $`F(\theta)=n_j(\mathrm{gd}\theta,\delta)`$ with fixed $`\delta`$. If $`\delta`$ is itself parameter dependent, additional chain-rule terms appear; there is no canonical choice of such a dependence.

The change in the three-sphere with **fixed** phases is also exact:

```math
\Psi_\eta=(-We^{i\alpha},Se^{i\beta}),\qquad \Psi_{\eta\eta}=-\Psi,\qquad \|\Psi_u\|=rS.
```

This curve changes the amplitude ratio and traverses a great-circle arc in $`S^3`$. It is **not** the same as varying the common phase at fixed $`\theta`$, which traverses a Hopf fibre. Thus the two mathematically distinct great-circle constructions must be named separately.

## 5. Metric and modular comparison (with marking)

The induced metric of the **round three-sphere** on the product torus is

```math
g_0=S^2d\alpha^2+W^2d\beta^2.
```

On the stereographic image the Euclidean first fundamental form is

```math
g_E=\frac{S^2d\alpha^2+W^2d\beta^2}{(1-W\sin\beta)^2}.
```

Consequently, for the **marked** rectangular lattice with periods $`2\pi S`$ and $`2\pi iW`$, the torus conformal modulus is

```math
\tau_T=i\frac WS=ib=i\sinh\!\left(r\log(x/c)\right).
```

This modulus belongs to this chosen marked Hopf torus. It is not automatically the period ratio of a generic Master quartic, a Lamé curve, or any Calabi–Yau construction. At fixed $`x,c`$ it satisfies $`(\tau_T)_r=iuR`$, $`(\tau_T)_{rr}=iu^2b`$; at fixed $`x,r`$, $`(\tau_T)_c=-irR/c`$ and $`(\tau_T)_{cc}=i(r^2b+rR)/c^2`$. At **fixed $`\eta`$**, $`\tau_T=i\tan\eta`$ has vanishing $`r,c`$ derivatives.

## 6. Source checks and scope of verification

The ZIP companion notes supply the parametrizations, planes, metrics, conformal modulus and projection distinctions. Its `validation.json` reports a maximum sampled numerical identity residual of about $`3.85\times10^{-13}`$ and a numerically evaluated Gauss linking integral of $`1`$; those figures are **historical source-reported checks**, not freshly established universal theorems. The ring-torus equation and Villarceau plane/circle identities were independently simplified symbolically for this chapter. The selected $`\eta`$ derivatives above follow by ordinary differentiation.

The full companion plates, their image files, the GeoGebra instructions, and external bibliographic references remain with the November 21 ZIP in the ChatGPT Project source collection; they were **not imported** into the GitHub mathematical reference. See [the source snapshot record](../../research/source-snapshots/2026-11-21/README.md), [the conic atlas](../00-foundations/00-08-projective-conics-gudermannian.md), and [the targeted verification program](../_standards/verify_field_hessians_hopf.py).

**Separation of structures:** selected torus $`\ne`$ arbitrary immersion, Hopf fibre $`\ne`$ amplitude-varying great circle, stereographic projection $`\ne`$ orthogonal projection $`\ne`$ Hopf quotient, and marked torus modulus $`\ne`$ generic elliptic energy-curve modulus.

## 7. The amplitude-exchange involution and the marked torus

On the same restricted domain $`x>c`$, set $`\theta=ru>0`$ and introduce the **new argument** $`\gamma=\log\coth(\theta/2)>0`$, while retaining the original positive $`r,c`$. Its exponential map is

```math
e^\gamma=\frac{e^\theta+1}{e^\theta-1},\qquad \mathrm{sech}\gamma=\tanh\theta=W,\qquad \tanh\gamma=\mathrm{sech}\theta=S.
```

Thus the selected torus amplitudes swap. The corresponding hyperbolic radii and the Gudermannian angle transform as

```math
(R,b)\longmapsto(R/b,1/b),\qquad \eta\longmapsto\frac\pi2-\eta.
```

At the unique fixed argument $`\theta_*=\log(1+\sqrt2)`$, one has $`b=1`$, $`S=W=1/\sqrt2`$ and the square Clifford torus. If the torus cycles are **marked in the same ordered convention** after the amplitude swap, the modulus obeys

```math
\tau_T=ib\longmapsto\tau_T^\vee=\frac i b=-\frac1{\tau_T}.
```

This is the classical modular $`S`$-change of marking on this selected rectangular torus, **not** evidence that the elliptic curve of a generic Master energy level has the same modulus. The spatial lift at fixed $`r,c`$ is the nonlinear involution $`x^\vee=c[(T+1)/(T-1)]^{1/r}`$ from [§00.11](../00-foundations/00-11-elementary-function-web.md); the resolution parameter is **not** changed.

## 8. The chosen Hopf connection: curvature and Chern number

The torus amplitudes alone do not specify a one-form. For the **standard chosen Hopf connection** on the round unit $`S^3\subset\mathbb C^2`$, define the real one-form

```math
\mathcal A=\mathrm{Im}(\Psi^\dagger d\Psi)=S^2d\alpha+W^2d\beta,\qquad \delta=\beta-\alpha,\qquad \mathcal A=d\alpha+W^2d\delta.
```

Here the **phase coordinates are independently chosen**; differentiating them is not the same as differentiating the scalar kernel. With $`S=\cos\eta`$ and $`W=\sin\eta`$,

```math
\mathcal F=d\mathcal A=d(W^2)\wedge d\delta=2SW\,d\eta\wedge d\delta=\sin(2\eta)\,d\eta\wedge d\delta.
```

When $`\alpha,\delta`$ are independent of the original $`x,c,r`$ variations, the coordinate pullback is explicitly

```math
\mathcal F=2WS^2\left[r\left(\frac{dx}{x}-\frac{dc}{c}\right)+u\,dr\right]\wedge d\delta.
```

The **full Hopf base sphere** is obtained from **one** angular half-chart $`0\le\eta\le\pi/2`$ with $`0\le\delta<2\pi`$, including its degenerate torus endpoints $`W=0`$ and $`S=0`$. The phase chart is not globally regular at those endpoints, but the curvature extends smoothly. With the orientation $`d\eta\wedge d\delta`$,

```math
\frac1{2\pi}\int_{S^2}\mathcal F=\frac1{2\pi}\int_0^{2\pi}\int_0^{\pi/2}\sin(2\eta)\,d\eta\,d\delta=1.
```

This is the first Chern number in the stated connection/orientation convention; reversing orientations or bundle-sign conventions changes the reported sign. **Do not integrate over $`-\pi/2\le\eta\le\pi/2`$ as though it were one injective Hopf-base spherical chart:** allowing both signs of $`W`$ duplicates the base with phase identifications and would give a misleading cancellation.

This construction links the same $`S,W`$ functions to a connection and characteristic class **only after specifying the Hopf bundle, its circle action and phases**. It is not a physical gauge-field assertion or a consequence of the Master ODE alone. See the [typed elementary web](../00-foundations/00-11-elementary-function-web.md) and the [verification script](../_standards/verify_elementary_function_web.py).
