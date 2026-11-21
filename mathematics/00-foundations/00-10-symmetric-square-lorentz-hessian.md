# 00.10 — Symmetric-square Lorentz cone, parameter Hessian determinant and Riccati clocks

**Status:** the null-cone sections, scalar Hessian determinant and Riccati identities are exact algebraic/differential statements under the hypotheses below. The catenoid Gauss map and Jacobi operator require a **specified immersion and metric**; they are not uniquely determined by the kernel. This page evaluates a November 21 discussion against the actual November 16 reference and November 21 ZIP; it neither asserts novelty nor promotes the ZIP wholesale.

**Coordinates:** $`x,c,r>0`$, $`u=\log(x/c)`$, $`\theta=ru`$, $`T=e^\theta`$. Let $`S=\mathrm{sech}\theta`$, $`W=\tanh\theta`$, $`R=\cosh\theta`$, $`b=\sinh\theta`$, $`P=(1+W)/2`$ and, *only in this comparison*, $`H:=H_2=S^2=\mathcal B`$. Here the plain $`H`$ is **not** the Hamiltonian or the Friedmann-style logarithmic slope. Unless specified otherwise, the $`(u,r)`$ Hessian takes $`c`$ as fixed.

## 1. The symmetric-square cone: three genuine affine sections

Let the two-component exponential carrier be $`\psi=(e^{\theta/2},e^{-\theta/2})`$, so $`\psi_{\theta\theta}=\psi/4`$. Its symmetric square is

```math
(Y_1,Y_2,Y_3)=(\psi_1^2,\psi_1\psi_2,\psi_2^2)=(e^\theta,1,e^{-\theta}),\qquad Y_1Y_3-Y_2^2=0.
```

Introduce *Lorentz coordinates* $`X=(Y_1+Y_3)/2`$, $`Y=(Y_1-Y_3)/2`$ and $`Z=Y_2`$. The homogeneous equation becomes the light cone

```math
Q(X,Y,Z)=X^2-Y^2-Z^2=0,\qquad (X,Y,Z)=(R,b,1).
```

The following are genuine **affine-plane sections of the same cone**. In the table, $`Q\vert_{\mathrm{dir}}`$ is the restriction of the Lorentz quadratic form to the *translation directions of the affine plane*, with the plane's constant term omitted.

| Plane in $`\mathbb R^{2,1}`$ | Slice equation and affine coordinates | $`Q\vert_{\mathrm{dir}}`$ | Type |
|---|---|---|---|
| $`Z=1`$ | $`X^2-Y^2=1`$ | $`dX^2-dY^2`$ | Hyperbola; restricted determinant negative |
| $`X=1`$ | $`Y^2+Z^2=1`$ | $`-dY^2-dZ^2`$ | Circle/ellipse; restricted determinant positive |
| $`X-Y=1`$ | $`X+Y=Z^2`$ | $`-dZ^2`$ | Parabola; restricted determinant zero |

The first two charts represent the **same projective conic point**: normalize $`(R,b,1)`$ by $`R`$ to obtain $`(1,W,S)`$. The third plane is null (its direction restriction has rank one), but its canonical parameter there is $`Z/(X-Y)=e^\theta=T`$, **not** $`W`$.

For the familiar *canonical logistic parabola* $`H=4P(1-P)`$, another null-plane parametrization is obtained by putting $`t=W`$ in

```math
(\widehat Y_1,\widehat Y_2,\widehat Y_3)=(t^2,t,1),\qquad \widehat Y_1\widehat Y_3=\widehat Y_2^2,\qquad P=\frac{1+t}{2},\qquad H=1-t^2.
```

Here $`t=(T^2-1)/(T^2+1)`$ is a **degree-two rational function of the original exponential projective parameter** $`T`$. Consequently, the displayed canonical map $`(S,W)\mapsto(P,H)`$ is quadratic and loses the sign of $`S`$ on the full circle. It is **not** the same kind of invertible projective recharting as the circle–hyperbola transition.

### 1.1. The Gram discriminant needs a declared duality

The ZIP source `04-follow-ups/fibration-holography-gram-poisson.md` uses the **source-local** Gram matrix and determinant

```math
G_{\mathrm{src}}=\begin{pmatrix}A_{\mathrm{src}}&B_{\mathrm{src}}\\B_{\mathrm{src}}&C_{\mathrm{src}}\end{pmatrix},\qquad \delta_{\mathrm{src}}=A_{\mathrm{src}}C_{\mathrm{src}}-B_{\mathrm{src}}^2.
```

**Do not conflate this notation with the canonical Atlas convention** $`G_{\mathrm{canon}}=\begin{pmatrix}A&C\\C&B\end{pmatrix}`$, $`\Delta_G=AB-C^2`$. The two determinants describe the same kind of quadratic-form discriminant **only after relabeling the coefficients**.

In source-local Lorentz coordinates $`t_G=(A_{\mathrm{src}}+C_{\mathrm{src}})/2`$, $`v_G=(A_{\mathrm{src}}-C_{\mathrm{src}})/2`$ and $`w_G=B_{\mathrm{src}}`$,

```math
\delta_{\mathrm{src}}=t_G^2-v_G^2-w_G^2.
```

Thus $`\delta_{\mathrm{src}}>0`$, $`\delta_{\mathrm{src}}<0`$ and $`\delta_{\mathrm{src}}=0`$ classify timelike, spacelike and null **dual normals**. For a nonzero-offset affine plane defined using the *specified Lorentz polar pairing* with one of these normals, the corresponding nondegenerate real cone sections have elliptic, hyperbolic and parabolic types, respectively (where the chosen plane intersects the real cone). Do not identify arbitrary planar coefficients with a positive Gram matrix without this polar pairing. The domain of positive definite Gram matrices is the positive timelike sheet up to scale; its hyperbolic metric is additional declared geometry.

## 2. Gudermannian half-angle and correctly signed Riccati variables

On the canonical real branch $`-\pi/2<\eta=\mathrm{gd}(\theta)<\pi/2`$ one has

```math
S=\cos\eta,\qquad W=\sin\eta,\qquad R=\sec\eta,\qquad b=\tan\eta,\qquad \frac{d\eta}{d\theta}=S.
```

With $`t=\tan(\eta/2)`$, the half-angle correspondence is a Möbius coordinate change on the exponential parameter followed by rational parametrization:

```math
t=\tan\left(\frac\eta2\right)=\tanh\left(\frac\theta2\right)=\frac{T-1}{T+1},\qquad W=\frac{2t}{1+t^2},\qquad S=\frac{1-t^2}{1+t^2}.
```

In particular the rational conic coordinate is $`t`$, while $`\eta=\mathrm{gd}(\theta)`$ is a non-algebraic change between the real *independent variables* $`\theta`$ and $`\eta`$.

**Logarithmic derivatives require the named numerator:**

| Field being differentiated in $`u`$ | Logarithmic slope | Riccati / factorization consequence |
|---|---|---|
| $`R=\cosh\theta`$ | $`q_R=R_u/R=rW`$ | $`(q_R)_u+q_R^2=r^2`$ |
| $`S=\mathrm{sech}\theta`$ | $`q_S=S_u/S=-rW=-q_R`$ | $`(q_S)_u+q_S^2=r^2-2r^2H`$ |
| $`b=\sinh\theta`$, where $`b\ne0`$ | $`q_b=b_u/b=rR/b=r/W`$ | $`(q_b)_u+q_b^2=r^2`$ |

This matches the distinctions in the ZIP's `04-follow-ups/profile-web.md` §§1–3 and `bernoulli-riccati.md`, and the pre-existing [log-derivative chapter](../01-master-equation/01-04-log-derivative-companion.md). A general Gram shift $`J_G=Ae^{ru}+2C+Be^{-ru}`$ does **not** satisfy the unshifted Riccati relation.

## 3. The universal two-variable Hessian determinant

For a real $`C^2`$ function $`F(u,r)=\phi(\theta)`$, with $`\theta=ru`$, put $`a=\phi_\theta`$ and $`d=\phi_{\theta\theta}`$. At fixed $`c`$, the symmetric Hessian in the **affine coordinate chart $`(u,r)`$** is

```math
\mathrm{Hess}_{(u,r)}F=\begin{pmatrix}r^2d&a+\theta d\\a+\theta d&u^2d\end{pmatrix},\qquad F_{ur}=a+\theta d=(\theta a)_\theta.
```

Its determinant has the **exact total-derivative form**

```math
\det\mathrm{Hess}_{(u,r)}F=\theta^2d^2-(a+\theta d)^2=-a^2-2\theta ad=-\frac{d}{d\theta}\left(\theta a^2\right).
```

**Proof.** Use $`F_u=ra`$ and $`F_r=ua`$. Then $`F_{uu}=r^2d`$, $`F_{rr}=u^2d`$, and $`F_{ur}=a+ru\,d`$. Expanding the determinant cancels the two $`\theta^2d^2`$ contributions. This requires no solution of a differential equation and no positivity assumption on $`\phi`$.

A compact fieldwise comparison, with $`H=S^2`$ and all quantities evaluated at $`\theta=ru`$, is:

| Field $`F`$ | $`\det\mathrm{Hess}_{(u,r)}F`$ |
|---|---|
| $`S`$ | $`-HW^2+2\theta HW(2W^2-1)`$ |
| $`W`$ | $`H^2(4\theta W-1)`$ |
| $`R`$ | $`-b^2-2\theta bR`$ |
| $`b`$ | $`-R^2-2\theta bR`$ |
| $`H=S^2`$ | $`-4H^2W^2+8\theta H^2W(2-3H)`$ |
| $`P=(1+W)/2`$ | $`H^2(4\theta W-1)/4`$ |
| $`\eta=\mathrm{gd}\theta`$ | $`H(2\theta W-1)`$ |

### 3.1. Signature change for the logistic/Riccati field

For $`W=\tanh\theta`$,

```math
\det\mathrm{Hess}_{(u,r)}W=H^2(4\theta\tanh\theta-1).
```

The function $`\theta\tanh\theta`$ is even and strictly increasing for $`\theta>0`$. Hence there is exactly one positive solution $`\theta_*`$ of $`\theta_*\tanh\theta_*=1/4`$, numerically $`\theta_*\approx0.521813447795769`$. The determinant is **negative** on $`|\theta|<\theta_*`$, **zero** at $`\theta=\pm\theta_*`$, and **positive** on the two exterior regions. Because the trace is $`(r^2+u^2)W_{\theta\theta}=-2(r^2+u^2)HW`$, the Hessian is negative definite for $`\theta>\theta_*`$ and positive definite for $`\theta<-\theta_*`$.

For comparison, the Gudermannian Hessian determinant vanishes where $`\theta\tanh\theta=1/2`$, at $`|\theta|\approx0.771702319209104`$. The equations for these thresholds are exact; the printed decimals are numerical evaluations.

### 3.2. Product-coordinate Lorentz form and its limitation

The **Hessian of the argument** $`\theta=ur`$ is the constant bilinear form

```math
\mathrm{Hess}_{(u,r)}\theta=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad h=du\otimes dr+dr\otimes du,\qquad h(v,v)=2\,du(v)\,dr(v).
```

It has Lorentz signature $`(1,1)`$ and is preserved by $`(u,r)\mapsto(su,r/s)`$ for $`s>0`$. Its Killing generator $`V=u\partial_u-r\partial_r`$ satisfies $`V\theta=0`$. On each fixed nonzero $`\theta`$ fibre with $`r>0`$, these boosts act transitively.

However, the **Hessian of a nonlinear $`F(ur)`$ need not retain that signature**; the example of $`W`$ explicitly changes type. Further, ordinary Hessians depend on the *affine coordinate system* and do not transform tensorially under the nonlinear change $`u=\log(x/c)`$. Neither the Lorentz form nor a differential-geometric fibration is canonically forced on the original $`(x,c,r)`$ family by this calculation.

Finally, $`F_{ur}=(\theta F_\theta)_\theta`$ involves the Euler dilation operator $`\theta\partial_\theta`$. On a positive half-line it is associated with Mellin scaling in **$`\theta`$**, but it must not be confused with the framework's exponential-coordinate operator $`T\partial_T=\partial_\theta`$; indeed $`\theta\partial_\theta=(\log T)T\partial_T`$.

## 4. Differential-geometry companion: Gauss arclength and Jacobi modes

The following statements use the **additional standard catenoid immersion**, with an independent positive length scale $`a_0>0`$ and angular coordinate $`\varphi\in\mathbb R/(2\pi\mathbb Z)`$:

```math
\mathbf X(\theta,\varphi)=a_0(R\cos\varphi,R\sin\varphi,\theta),\qquad g=a_0^2R^2(d\theta^2+d\varphi^2).
```

One orientation of its unit Gauss normal is $`N=(S\cos\varphi,S\sin\varphi,-W)`$. At fixed $`\varphi`$,

```math
|N_\theta|=S,\qquad \int_0^\theta|N_t|\,dt=\mathrm{gd}(\theta)=\eta.
```

This gives a precise *chosen-surface interpretation* of the Gudermannian as spherical arclength along a Gauss-image meridian. It is also a usual pendulum separatrix, since $`\eta_\theta=S=\cos\eta`$ and $`\eta_{\theta\theta}=-\tfrac12\sin(2\eta)`$. Other pendulum energies have elliptic-function descriptions, but are not automatically identical to the full Master level family.

The catenoid scalar Jacobi operator with the convention $`\mathcal J=\Delta_g+|A|^2`$ is

```math
\mathcal J=\frac1{a_0^2R^2}\left(\partial_\theta^2+\partial_\varphi^2+2S^2\right).
```

For a Fourier mode $`h_n(\theta)e^{in\varphi}`$ the zero-Jacobi equation becomes

```math
h_n''+(2S^2-n^2)h_n=0.
```

Its two particularly simple canonical solutions belong to **different angular modes**:

| Selected profile | Fourier mode | Exact meridional equation | Pöschl–Teller reading |
|---|---|---|---|
| $`W=\tanh\theta`$ | $`n=0`$ | $`W_{\theta\theta}+2S^2W=0`$ | Threshold bounded, not square-integrable on the line |
| $`S=\mathrm{sech}\theta`$ | $`n=1`$ | $`S_{\theta\theta}+(2S^2-1)S=0`$ | Square-integrable bound state of the $`\ell=1`$ well |

Equivalently, for the one-dimensional Schrödinger operator $`L=-\partial_\theta^2-2S^2`$, one has $`LW=0`$ and $`LS=-S`$. Pulling back to $`u`$ via $`\theta=ru`$ multiplies eigenvalues by $`r^2`$. The source's phrases “two Jacobi profiles” and “Pöschl–Teller order one” are therefore accurate **only with these angular/operator qualifications**.

### 4.1. Milne phase: a factor-two normalization to preserve

The ZIP's `04-follow-ups/fibration-holography-gram-poisson.md` uses the standard exponential carrier $`\psi_\pm(u)=e^{\pm ru/2}`$, the quadratic amplitude $`\rho^2=\psi_+^2+\psi_-^2=2\cosh(ru)`$ and Wronskian magnitude $`|{\cal W}|=r`$. Its Milne/Ermakov phase $`\gamma`$ satisfies

```math
\gamma_u=\frac{|{\cal W}|}{\rho^2}=\frac{r}{2\cosh(ru)}=\frac12\eta_u,\qquad \eta_u=rS.
```

Thus, with the same center normalization, $`\eta=2\gamma`$ up to an additive constant. Calling $`\eta`$ simply *the Milne phase* without stating the carrier/amplitude normalization would conceal this factor. The Gudermannian integral and Gauss arclength are exact independently of any Milne interpretation.

## 5. Provenance and release boundary

**Directly examined:** November 21 ZIP `04-follow-ups/profile-web.md` (conic, Riccati and Pöschl–Teller profiles); `04-follow-ups/lorentz-gram-hopf.md` (Gram Lorentz discriminant and hyperbolic-sheet choices); `04-follow-ups/fibration-holography-gram-poisson.md` (Milne phase carrier normalization); November 16 Complete Reference v2 (its section numbering is not interchangeable with historical §26 citations). Related maintained sources: [§00.08](00-08-projective-conics-gudermannian.md), [§00.09](00-09-second-derivative-charts.md), [§05.01](../05-differential-geometry/05-01-canonical-surface.md).

**Evidence categories:** the Lorentz null-cone, signature determinant and rational parametrizations have full algebraic proofs above; the oscillator/Jacobi identities are direct differential calculations for a *chosen* catenoid; the decimal signature thresholds are numerical checks; the phrases “fibration memory” or “bulk–boundary” are interpretations requiring additional structures. See [symbolic verification script](../_standards/verify_sym2_hessian.py). None of this establishes novelty or identifies distinct moduli/spectral theories merely because the same special functions appear.
