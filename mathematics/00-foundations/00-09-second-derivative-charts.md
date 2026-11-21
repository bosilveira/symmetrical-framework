# 00.09 — Second derivatives across logarithmic, parameter and Gudermannian charts

**Status:** exact chain-rule identities for the specified canonical profiles. This chapter extends [§00.06](00-06-variable-parameter-derivatives.md) and the [conic comparison table](00-08-projective-conics-gudermannian.md); it does not classify solutions of the corresponding free second-order equations. The original kernel, Gram envelopes, and off-separatrix Master fields retain their separate definitions.

## 1. Coordinate convention and a local plain-letter alias

On the open domain $`x,c,r>0`$, put $`u=\log(x/c)`$, $`\theta=ru`$, $`T=e^\theta`$ and $`\eta=\mathrm{gd}(\theta)=\arctan(\sinh\theta)`$. The symbol $`H:=H_2=S^2=\mathcal B`$ is a **chapter-local** plain uppercase alias for the squared profile. It is justified by the existing family $`H_q=S^q`$. It is **not** the Hamiltonian $`H_M`$, the Friedmann-style $`H=Y_u/Y`$, the constant Gram coefficient $`B`$, or a new permanent Atlas parameter. Outside this local table, the established $`\mathcal B`$ notation remains valid.

Primes in the following table mean differentiation in $`u`$ at fixed $`c,r`$; a subscript $`\theta`$ means differentiation in the independent argument $`\theta`$. The parameter derivatives below, unless specified otherwise, refer to the chart $`(x,c,r)`$ and hold its remaining coordinates fixed.

## 2. The entire second-derivative comparison in a single table

Define $`a_F=F_\theta`$ and $`d_F=F_{\theta\theta}`$. The table gives **argument derivatives**, so its last two columns are dimensionless and do not silently remove the factor $`r`$ from $`u`$ derivatives.

| Field $`F(\theta)`$ | Definition | $`a_F=F_\theta`$ | $`d_F=F_{\theta\theta}`$ | $`F_{uu}=r^2d_F`$ |
|---|---|---|---|---|
| $`S`$ | $`\mathrm{sech}\theta`$ | $`-SW`$ | $`S(2W^2-1)=S-2S^3`$ | $`r^2S-2r^2S^3`$ |
| $`W`$ | $`\tanh\theta`$ | $`H`$ | $`-2HW`$ | $`-2r^2W+2r^2W^3`$ |
| $`R`$ | $`\cosh\theta`$ | $`b`$ | $`R`$ | $`r^2R`$ |
| $`b`$ | $`\sinh\theta`$ | $`R`$ | $`b`$ | $`r^2b`$ |
| $`P`$ | $`(1+W)/2`$ | $`H/2`$ | $`-HW`$ | $`4r^2P(1-P)(1-2P)`$ |
| $`H`$ | $`S^2=4P(1-P)`$ | $`-2HW`$ | $`4H-6H^2`$ | $`4r^2H-6r^2H^2`$ |
| $`\eta`$ | $`\mathrm{gd}(\theta)`$ | $`S`$ | $`-SW`$ | $`-r^2SW`$ |
| $`T`$ | $`e^\theta`$ | $`T`$ | $`T`$ | $`r^2T`$ |

This is a table of selected profiles, not a family of mutually equivalent unrestricted ODEs. In particular, $`H=S^2`$ is the $`q=2`$ member of the distinguished power-profile family; the intrinsic $`\ell=5`$ equation has other nonzero-energy orbits.

## 3. Universal Hessian in the three physical/parameter variables

**Proposition (second-order pullback).** For a $`C^2`$ function $`F(\theta)`$, define $`a=F_\theta`$ and $`d=F_{\theta\theta}`$, evaluated at $`\theta=r\log(x/c)`$. Then, in the ordered chart $`(x,c,r)`$,

```math
F_x=\frac{r}{x}a,\qquad F_c=-\frac{r}{c}a,\qquad F_r=ua.
```

Its *full symmetric Hessian* is

```math
\mathrm{Hess}_{(x,c,r)}F=\begin{pmatrix}(r^2d-ra)/x^2&-r^2d/(xc)&(a+ru\,d)/x\\-r^2d/(xc)&(r^2d+ra)/c^2&-(a+ru\,d)/c\\(a+ru\,d)/x&-(a+ru\,d)/c&u^2d\end{pmatrix}.
```

**Proof.** The first and second argument derivatives are $`\theta_x=r/x`$, $`\theta_c=-r/c`$, $`\theta_r=u`$, $`\theta_{xx}=-r/x^2`$, $`\theta_{cc}=r/c^2`$, $`\theta_{xr}=1/x`$ and $`\theta_{cr}=-1/c`$; $`\theta_{xc}=\theta_{rr}=0`$. For every pair $`i,j`$ use $`F_{ij}=d\,\theta_i\theta_j+a\,\theta_{ij}`$. This also proves equality of the mixed partials.

A compact comparison of parameter-only derivatives follows:

| Field | $`F_{rr}`$ (fixed $`x,c`$) | $`F_{cc}`$ (fixed $`x,r`$) |
|---|---|---|
| $`S`$ | $`u^2S(2W^2-1)`$ | $`[r^2S(2W^2-1)-rSW]/c^2`$ |
| $`W`$ | $`-2u^2HW`$ | $`[rH-2r^2HW]/c^2`$ |
| $`R`$ | $`u^2R`$ | $`[r^2R+rb]/c^2`$ |
| $`b`$ | $`u^2b`$ | $`[r^2b+rR]/c^2`$ |
| $`P`$ | $`-u^2HW`$ | $`[rH/2-r^2HW]/c^2`$ |
| $`H`$ | $`u^2(4H-6H^2)`$ | $`[r^2(4H-6H^2)-2rHW]/c^2`$ |
| $`\eta`$ | $`-u^2SW`$ | $`[rS-r^2SW]/c^2`$ |

The **mixed** derivative is not an additional calculation: substitute each row's $`a,d`$ into $`F_{rc}=-(a+ru\,d)/c`$. Likewise, $`F_{xr}=(a+ru\,d)/x`$, $`F_{xc}=-r^2d/(xc)`$ and $`F_{xx}=(r^2d-ra)/x^2`$. These identities are more reliable than independently differentiating each displayed special function.

## 4. Compare the three coordinate charts

Let $`F`$ be one of the fields in §2, with no *additional explicit* $`r,c`$ factors. At fixed $`(u,c,r)`$, $`\theta=ru`$, and at fixed $`(\eta,c,r)`$, $`\theta=\mathrm{arsinh}(\tan\eta)`$.

| Derivative/constraint | $`(x,c,r)`$ chart | $`(u,c,r)`$ chart | $`(\eta,c,r)`$ chart |
|---|---|---|---|
| $`\partial_r F`$ | $`ua`$, fixed $`x,c`$ | $`ua`$, fixed $`u,c`$ | $`0`$, fixed $`\eta,c`$ |
| $`\partial_c F`$ | $`-ra/c`$, fixed $`x,r`$ | $`0`$, fixed $`u,r`$ | $`0`$, fixed $`\eta,r`$ |
| $`\partial_r^2F`$ | $`u^2d`$ | $`u^2d`$ | $`0`$ |
| $`\partial_c^2F`$ | $`(r^2d+ra)/c^2`$ | $`0`$ | $`0`$ |
| $`\partial_u^2F`$ | not a chart coordinate | $`r^2d`$ | not a chart coordinate |
| $`\partial_\eta^2F`$ | not a chart coordinate | not a chart coordinate | $`R^2d+Rb\,a`$ |

The last equality uses $`d\theta/d\eta=R`$ and $`d^2\theta/d\eta^2=Rb`$. The $`\eta`$-clock second derivatives are

| Object | $`F_{\eta\eta}`$ | Type of selected equation |
|---|---|---|
| $`S,W`$ | $`-S,\ -W`$ | Harmonic pair |
| $`R,b`$ | $`2R^3-R,\ 2b^3+2b`$ | Cubic pair |
| $`P`$ | $`1/2-P`$ | Forced linear |
| $`H`$ | $`2-4H`$ | Forced linear |
| $`\eta`$ | $`0`$ | Independent coordinate itself |

Thus identical **values** of a field do not imply identical **parameter partial derivatives** in different charts.

## 5. The original kernel carries an additional explicit factor

For $`f(x;r,c)=S/(2x)`$ the preceding Hessian applies to $`S`$, but not unchanged to the full $`f`$ when a derivative varies $`x`$. Its fixed-spatial-coordinate parameter derivatives are

```math
f_{rr}=u^2f(2W^2-1),\quad f_{cc}=\frac{f}{c^2}[r^2(2W^2-1)-rW],\quad f_{rc}=\frac{f}{c}[W+ru(1-2W^2)].
```

The spatial second derivative and the fixed-log-coordinate second derivatives are

```math
f_{xx}=\frac f{x^2}[2+3rW+r^2(2W^2-1)],\quad \widetilde f_{uu}=\widetilde f[1+2rW+r^2(2W^2-1)],\quad \widetilde f_{cc}|_{u,r}=\frac{2\widetilde f}{c^2}.
```

Finally, for $`f_\eta=\cos\eta\exp[-\mathrm{arsinh}(\tan\eta)/r]/(2c)`$ on $`-\pi/2<\eta<\pi/2`$, with $`u=\mathrm{arsinh}(\tan\eta)/r`$,

```math
(f_\eta)_{\eta\eta}=f_\eta\left[-1+\frac{bR}{r}+\frac{R^2}{r^2}\right],\quad (f_\eta)_{rr}|_{\eta,c}=\frac{u^2-2u}{r^2}f_\eta,\quad (f_\eta)_{cc}|_{\eta,r}=\frac{2f_\eta}{c^2}.
```

This is a useful counterexample to treating $`f`$ as a pure argument-function in every coordinate chart.

## 6. Logarithmic derivative: an explicit $`r`$ prevents naive reuse of the table

For the centered linear backbone $`J_0=R=\cosh(ru)`$, its logarithmic slope is $`q_0=(J_0)_u/J_0=rW`$. It obeys $`(q_0)_u=r^2H`$ and $`(q_0)_{uu}=-2r^3HW`$. When the **resolution is varied**, the explicit factor $`r`$ contributes:

```math
(q_0)_r|_{x,c}=W+ruH,\qquad (q_0)_c|_{x,r}=-\frac{r^2H}{c},\qquad (q_0)_{rr}|_{x,c}=2uH-2ru^2HW.
```

```math
(q_0)_{cc}|_{x,r}=\frac{r^2H-2r^3HW}{c^2},\qquad (q_0)_{rc}|_x=\frac{-2rH+2r^2uHW}{c},\qquad (q_0)_{\eta\eta}|_{c,r}=-rW.
```

For an *unshifted general* envelope $`J_0=Ae^{ru}+Be^{-ru}`$ with fixed $`A,B>0`$, the slope equals $`r\tanh[r(u-u_0)]`$ where $`u_0=\log(B/A)/(2r)`$. One must differentiate the **ratio** with $`A,B`$ held fixed, not silently hold the $`r`$-dependent center $`u_0`$ fixed. For a shifted Gram envelope $`J_G=J_0+2C`$, $`(J_G)_u/J_G`$ satisfies a different Riccati-type defect (see [§00.07](00-07-differential-algebra-oscillator-hierarchy.md)); it is not $`rW`$ in general.

## 7. The beta cumulative and power hierarchy share the same calculus

At fixed $`q>0`$, $`H_q=S^q`$ has $`(H_q)_\theta=-qWH_q`$ and $`(H_q)_{\theta\theta}=q^2H_q-q(q+1)H_q^{1+2/q}`$. The normalized cumulative $`Q_q=I_{P}(q,q)`$ has

```math
(Q_q)_\theta=\frac{S^{2q}}{\mathrm B(1/2,q)},\qquad (Q_q)_{\theta\theta}=-\frac{2qWS^{2q}}{\mathrm B(1/2,q)}.
```

Both inherit the same universal Hessian in §3 after their two argument derivatives are substituted. This connection is an **exact derivative/pushforward fact**, not an identification of the full intrinsic-level Master solution spaces.

## 8. Symmetry point and reproducibility

At the **evaluation point** $`x=c`$, one has $`u=W=b=0`$, $`S=R=H=1`$ and $`P=1/2`$. For argument-only fields, $`F_r=F_{rr}=0`$ at this point **with $`x,c`$ fixed**; this does not imply the function family is independent of $`r`$. For example $`H_{cc}|_{x=c}=-2r^2/c^2`$ and $`f_{xx}(c;r,c)=(2-r^2)/(2c^3)`$. Moving along $`x=c`$ produces a different total derivative.

A targeted symbolic check of the $`(x,c,r)`$ Hessian for $`S,W,R,b,P,H,\eta`$, the kernel parameter Hessian, and the Hopf-base clock is recorded separately in [the companion verification program](../_standards/verify_field_hessians_hopf.py).

**Provenance:** Complete Reference v2 §§F.1, 1, 27–28 and November 21 ZIP `00-meta/NOTATION`, `04-follow-ups/profile-web`; earlier [§00.06](00-06-variable-parameter-derivatives.md) gives the first parameter derivatives. The systematic second-order Hessian table is a direct chain-rule extension checked independently here. No literature priority or physical realization is claimed.

## 9. Universal determinant of the $`(u,r)`$ Hessian

The full $`(x,c,r)`$ Hessian of §3 is **not** interchangeable with the smaller, coordinate-dependent Hessian in $`(u,r)`$. At fixed $`c`$, for $`F(u,r)=\phi(ru)`$ with $`a=\phi_\theta`$ and $`d=\phi_{\theta\theta}`$,

```math
\mathrm{Hess}_{(u,r)}F=\begin{pmatrix}r^2d&a+\theta d\\a+\theta d&u^2d\end{pmatrix},\qquad \det\mathrm{Hess}_{(u,r)}F=-a^2-2\theta ad=-\frac{d}{d\theta}\left(\theta a^2\right).
```

The mixed entry is $`F_{ur}=a+\theta d=(\theta a)_\theta`$. Notice that $`\theta\partial_\theta`$ generates **dilation in $`\theta`$**, whereas the existing exponential-coordinate differential operator is $`\partial_\theta=T\partial_T`$.

| Field | Determinant of the $`(u,r)`$ Hessian |
|---|---|
| $`W=\tanh\theta`$ | $`H^2(4\theta W-1)`$ |
| $`\eta=\mathrm{gd}\theta`$ | $`H(2\theta W-1)`$ |
| $`R=\cosh\theta`$ | $`-b^2-2\theta bR`$ |
| $`S=\mathrm{sech}\theta`$ | $`-HW^2+2\theta HW(2W^2-1)`$ |
| $`H=S^2`$ | $`-4H^2W^2+8\theta H^2W(2-3H)`$ |

The Hessian determinant of $`W`$ changes sign at the two curves $`ru=\pm\theta_*`$, where $`\theta_*\tanh\theta_*=1/4`$ and $`\theta_*\approx0.5218134478`$; its Hessian is indefinite between the curves, negative definite for $`ru>\theta_*`$ and positive definite for $`ru<-\theta_*`$. This is an exact signature classification. The related source comparison, Lorentz null-cone sections, Gudermannian/Milne phase normalization and catenoid Jacobi **mode restrictions** are proved in [§00.10](00-10-symmetric-square-lorentz-hessian.md).

**Status:** direct chain-rule proof and independent [symbolic checks](../_standards/verify_sym2_hessian.py). The signature of $`\mathrm{Hess}_{(u,r)}\theta`$ is Lorentzian, but that does **not** force the Hessian of every $`F(ru)`$ to remain indefinite, and no ordinary Hessian determinant is claimed invariant under the nonlinear change $`u=\log(x/c)`$.
