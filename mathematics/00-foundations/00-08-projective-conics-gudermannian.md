# 00.08 — Circle, hyperbola, parabola and the Gudermannian change of clock

**Status:** verified foundational identities, with explicit coordinate and parameter scopes. This chapter includes the four-row oscillator table requested in the 21 November 2026 project conversation, **correcting only its ambiguous field name**. It expands the source investigation `04-follow-ups/profile-web.md` §§1–3 (November 21 ZIP, H127) and Complete Reference 2026-11-16 v2 §§1, F.1–F.3. See [§00.07](00-07-differential-algebra-oscillator-hierarchy.md) for the broader rational differential algebra.

**Canonical independent coordinates:** $`x,c,r>0`$, $`u=\log(x/c)`$, $`\theta=ru`$, $`T=e^\theta`$; derivatives denoted by a prime in the **first table** are $`D_u=d/du`$ at fixed $`r,c`$. The Gudermannian angle is the **alternative** coordinate $`\eta_{\rm GD}=\mathrm{gd}(\theta)`$, not the Gram rapidity that also appears as $`eta`$ in older sources.

## 1. A crucial distinction: the different meanings of B

The screenshot's $`B=S^2`$ is a useful *local alias*, but the source `00-meta/NOTATION.md` §III.2 and §III.10 expressly reserve uppercase $`B`$ for the **constant coefficient** of the linear/Gram backbone,

```math
J_0(u)=Ae^{ru}+Be^{-ru},\qquad J_G(u)=Ae^{ru}+2C+Be^{-ru},\qquad A,B>0.
```

Complete Reference v2 §F uses $`B_0=S^2`$ locally; other source subprojects reuse $`B`$ for unrelated modular/oscillator coefficients. To avoid collisions in this foundational chapter we **define the squared profile as a field**

```math
\mathcal B(u):=S(u)^2=\mathrm{sech}^2(ru).
```

Thus $`B`$ (Gram coefficient, $`D_uB=0`$) is **not** $`\mathcal B`$ (dependent field, $`D_u\mathcal B=-2r\mathcal BW`$). The **table-local plain-uppercase alias** $`H:=H_2=S^2=\mathcal B`$ reuses the existing $`H_q=S^q`$ hierarchy. The alias is not a global replacement: Hamiltonians and the Friedmann-type field also use $`H`$. Whenever copying the screenshot's $`B=S^2`$, interpret that row as $`\mathcal B=S^2`$. Also keep lower-case $`b=\sinh(ru)`$ separate from the coefficient $`B`$. The standard Euler **beta function** $`\mathrm B(a,b)`$ (often written $`B(a,b)`$ in existing sources) is a third mathematical object, unrelated to both the coefficient and squared field.

## 2. Complete four-row coupled-equation table

Let $`S=\mathrm{sech}\theta`$, $`W=\tanh\theta`$, $`R=\cosh\theta`$, $`b=\sinh\theta`$ and $`P=(1+W)/2`$. Every displayed second-order equation is for the *specified canonical orbit*.

| Objects (scope) | Coupled first-order equations (prime $`D_u`$) | Second-order equations (prime $`D_u`$) |
|---|---|---|
| $`S=\mathrm{sech}\theta,\quad W=\tanh\theta`$ | $`S'=-rSW;\quad W'=rS^2`$ | $`S''=r^2S-2r^2S^3;\quad W''=-2r^2W+2r^2W^3`$ |
| $`R=\cosh\theta,\quad b=\sinh\theta`$ | $`R'=rb;\quad b'=rR`$ | $`R''=r^2R;\quad b''=r^2b`$ |
| $`P=(1+W)/2`$ | $`P'=2rP(1-P)=rH/2`$ | $`P''=4r^2P(1-P)(1-2P)`$ |
| $`H:=H_2=S^2=\mathcal B`$ (local alias) | $`H'=-2rHW;\quad W'=rH`$ | $`H''=4r^2H-6r^2H^2`$ |

The three corresponding constraints are

```math
S^2+W^2=1,\qquad R^2-b^2=1,\qquad \mathcal B=4P(1-P).
```

**Derivations:** $`S'=-rSW`$, $`W'=rS^2`$, $`R'=rb`$ and $`b'=rR`$ follow from the chain rule. Differentiating $`P=(1+W)/2`$ gives $`P'=rS^2/2=2rP(1-P)`$. Differentiating $`\mathcal B=S^2`$ gives $`\mathcal B'=-2r\mathcal BW`$ and then

```math
\mathcal B''=-2r(\mathcal B'W+\mathcal BW')=4r^2\mathcal BW^2-2r^2\mathcal B^2=4r^2\mathcal B-6r^2\mathcal B^2.
```

The last equality uses **the canonical circle constraint** $`W^2=1-\mathcal B`$. Without that constraint, the coupled first-order system has a family of shifted parabolic invariants (see §6).

## 3. The circle and hyperbola are TWO AFFINE CHARTS of ONE projective conic

The exact source identity in `04-follow-ups/profile-web.md` §1 is

```math
[X:Y:Z]=[R:b:1]=[1:W:S]=[1+T^2:T^2-1:2T], \qquad X^2=Y^2+Z^2.
```

This is a *single real projective conic* with two different affine normalizations:

- The chart $`Z=1`$ gives $`(X,Y)=(R,b)`$ and $`R^2-b^2=1`$ (right hyperbola branch $`R>0`$).
- The chart $`X=1`$ gives $`(Y,Z)=(W,S)`$ and $`W^2+S^2=1`$ (upper/right semicircle $`S>0`$, according to axis order).

Equivalently,

```math
S=\frac1R,\quad W=\frac bR,\qquad R=\frac1S,\quad b=\frac WS.
```

The map is **projective**, not a global metric isometry; it excludes the $`S=0`$ endpoints from the finite hyperbolic chart. The projective parameter $`T>0`$ produces the rational formulas

```math
S=\frac{2T}{1+T^2},\quad W=\frac{T^2-1}{T^2+1},\quad R=\frac{T+T^{-1}}2,\quad b=\frac{T-T^{-1}}2.
```

The multiplicative parameter records both the center and the resolution: $`T=(x/c)^r`$. It is not a coordinate independent of $`x,c,r`$.

## 4. The parabola is a quadratic image, not the same affine chart

Since $`P=(1+W)/2`$ and $`\mathcal B=S^2`$,

```math
\mathcal B=1-W^2=4P(1-P)=1-4\left(P-\frac12\right)^2.
```

This is the downward-opening parabola in the **chosen Euclidean affine plane $`(P,\mathcal B)`$**. The canonical trajectory has $`0<P<1`$, $`0<\mathcal B\le1`$, and vertex $`(P,\mathcal B)=(1/2,1)`$ at $`x=c`$. As $`u\to\pm\infty`$, it tends to $`(0,0)`$ and $`(1,0)`$, respectively.

The map

```math
(S,W)\longmapsto\left(P=\frac{1+W}2,\ \mathcal B=S^2\right)
```

is **quadratic in the circle coordinate** $`S`$. On the selected branch $`S>0`$, the inverse is $`W=2P-1`$, $`S=\sqrt{\mathcal B}`$. On the full unit circle it loses the sign of $`S`$; therefore this displayed parabola map is **not** an invertible projective change of affine chart like §3.

For a homogeneous description of the quadratic map, use $`[X:Y:Z]=[R:b:1]`$. With target coordinates $`[\mathsf P:\mathsf B:\mathsf Z]`$ it is

```math
[\mathsf P:\mathsf B:\mathsf Z]=\left[\frac{X(X+Y)}2:Z^2:X^2\right], \qquad \mathsf B\mathsf Z=4\mathsf P(\mathsf Z-\mathsf P).
```

The equation follows from $`X^2-Y^2=Z^2`$. In the affine target $`\mathsf Z=1`$ this is exactly $`\mathcal B=4P(1-P)`$. Notice the quadratic map identifies the two projective points related by $`Z\mapsto-Z`$ at generic locations; retaining the canonical $`S>0`$ selects the real positive branch.

## 5. Gudermannian: an exact exchange of the differential clock

Let $`\eta=\mathrm{gd}(\theta)=2\arctan(e^\theta)-\pi/2`$ on the real branch $`-\pi/2<\eta<\pi/2`$. Then

```math
\sin\eta=W,\quad\cos\eta=S,\quad\tan\eta=b,\quad\sec\eta=R,\quad T=\sec\eta+\tan\eta=\tan\left(\frac\pi4+\frac\eta2\right).
```

Hence $`d\eta/d\theta=S=1/R`$. On a smooth field restricted to this particular canonical orbit,

```math
\frac{d}{du}=rT\frac{d}{dT}=r(1-W^2)\frac{d}{dW}=2rP(1-P)\frac{d}{dP}=rS\frac{d}{d\eta}.
```

The last three operator equalities are **tangential derivatives along the specified orbit** (with $`r,c`$ fixed), not independent partial-derivative identities on an ambient multivariable space.

Now primes in the following **second table** are replaced by subscript $`\eta`$:

| Objects | First derivatives with respect to $`\eta`$ | Second derivatives with respect to $`\eta`$ |
|---|---|---|
| Circle $`S=\cos\eta,\ W=\sin\eta`$ | $`S_\eta=-W;\quad W_\eta=S`$ | $`S_{\eta\eta}=-S;\quad W_{\eta\eta}=-W`$ |
| Hyperbola $`R=\sec\eta,\ b=\tan\eta`$ | $`R_\eta=Rb;\quad b_\eta=R^2`$ | $`R_{\eta\eta}=2R^3-R;\quad b_{\eta\eta}=2b^3+2b`$ |
| Parabola coordinate $`P=(1+\sin\eta)/2`$ | $`P_\eta=S/2`$ | $`P_{\eta\eta}=\frac12-P`$ |
| Squared profile $`\mathcal B=\cos^2\eta`$ | $`\mathcal B_\eta=-2SW=-\sin(2\eta)`$ | $`\mathcal B_{\eta\eta}=2-4\mathcal B`$ |

**Key mathematical finding (also noticed in the source's §2):** in logarithmic time $`u`$ the hyperbolic pair $`R,b`$ is linear and the circle pair $`S,W`$ obeys cubic equations; in the Gudermannian clock $`\eta`$, **the circle pair becomes the linear harmonic oscillator**, while $`R,b`$ obey cubic equations. Even the logistic field becomes the *forced linear oscillator* $`P_{\eta\eta}+P=\frac12`$, and the squared profile becomes $`\mathcal B_{\eta\eta}+4\mathcal B=2`$. None of these equations has the same **independent variable** as its logarithmic-time counterpart.

The Gudermannian coordinate itself satisfies the pendulum-form equation

```math
\eta_{uu}=-(r^2/2)\sin(2\eta),\qquad \eta_u=r\cos\eta.
```

No physical pendulum model is implied by these identities.

## 6. An entire *family* of invariant parabolas

The canonical pair $`(P,\mathcal B)`$ satisfies the polynomial autonomous system

```math
P_u=\frac r2\mathcal B,\qquad \mathcal B_u=2r\mathcal B(1-2P).
```

It admits the exact first integral

```math
K_{\rm par}=\mathcal B-4P(1-P),\qquad (K_{\rm par})_u=0.
```

Thus the canonical parabola is the **specific zero-invariant leaf** $`K_{\rm par}=0`$ of a larger planar vector field. For arbitrary initial data, every nonstationary orbit lies on a translated parabola

```math
\mathcal B=4P(1-P)+K_{\rm par},
```

and obeys

```math
P_{uu}=r^2\bigl[4P(1-P)+K_{\rm par}\bigr](1-2P),\qquad \mathcal B_{uu}=4r^2(1+K_{\rm par})\mathcal B-6r^2\mathcal B^2.
```

These expressions reduce to the first table **only when $`K_{\rm par}=0`$**. The complete polynomial flow also contains the invariant equilibrium line $`\mathcal B=0`$; global orbit claims must not be inferred from the selected positive sigmoid.

This provides a precise interpretation of “coupled oscillators”: the **first-order flow plus its invariant leaf** produces the second-order profile. The scalar second-order equation alone is not the entire constrained dynamics.

### 6.1. The one-parameter boost and its nonlinear projections

At fixed $`r,c>0`$, a log-coordinate translation $`u\mapsto u+\delta`$ acts on the linear pair by the $`SO^+(1,1)`$ matrix

```math
\begin{pmatrix}R(u+\delta)\\ b(u+\delta)\end{pmatrix}=\begin{pmatrix}\cosh(r\delta)&\sinh(r\delta)\\ \sinh(r\delta)&\cosh(r\delta)\end{pmatrix}\begin{pmatrix}R(u)\\b(u)\end{pmatrix}.
```

The same translation becomes the Möbius flow and logistic odds multiplication

```math
W(u+\delta)=\frac{W(u)+\tanh(r\delta)}{1+W(u)\tanh(r\delta)},\qquad \frac{P(u+\delta)}{1-P(u+\delta)}=e^{2r\delta}\frac{P(u)}{1-P(u)}.
```

The squared profile is reconstructed by $`\mathcal B(u+\delta)=4P(u+\delta)[1-P(u+\delta)]`$. Finally, the Gudermannian angle transforms by the **non-additive** half-angle relation

```math
\tan\left(\frac\pi4+\frac{\eta(u+\delta)}2\right)=e^{r\delta}\tan\left(\frac\pi4+\frac{\eta(u)}2\right).
```

This is a common **one-parameter group action**, represented linearly in the hyperbolic chart and rationally in the Riccati/logistic charts. It does not turn other invariant leaves into the same flow.

The canonical spatial inversion at fixed $`c,r`$ is $`x\mapsto c^2/x`$, hence $`u\mapsto-u`$ and

```math
(S,W)\mapsto(S,-W),\qquad (R,b)\mapsto(R,-b),\qquad (P,\mathcal B)\mapsto(1-P,\mathcal B),\qquad \eta\mapsto-\eta.
```

Thus the involution exchanges the endpoints of the same parabolic arc and fixes its vertex $`(P,\mathcal B)=(1/2,1)`$. It is a symmetry of the canonical conic dictionary, not a claim that all parameter-rescaling operations are the same.

## 7. Geometry of the clocks and arc lengths

The projective curve carries different **chosen metrics** in its affine realizations. Direct differentiation gives the exact differentials

```math
dS^2+dW^2=d\eta^2=S^2d\theta^2,\qquad db^2-dR^2=d\theta^2=r^2du^2.
```

Here $`dS^2`$ abbreviates $`(dS)^2`$, etc.; the second expression is the **Minkowski** line element on the hyperbola, not a Euclidean squared length. Hence $`\theta`$ is the proper-length parameter on the hyperbola, whereas $`\eta`$ is the Euclidean arc-length angle along the unit circle. The two clocks are related by

```math
\frac{d\eta}{d\theta}=S=\frac1R,\qquad \frac{d\theta}{d\eta}=R=\sec\eta.
```

The Euclidean curvature of the circle is $`1`$; that of the affine hyperbola $`(R,b)`$ is $`(R^2+b^2)^{-3/2}`$, and that of $`(P,\mathcal B)=(p,4p(1-p))`$ is $`8[1+16(1-2p)^2]^{-3/2}`$. These curvatures differ because the affine embeddings and metrics differ. A projective equivalence is **not an isometry**.

## 8. Parameters and measure: what the conics do NOT forget

The equations of the three **loci** contain neither $`r`$ nor $`c`$, but their **parametrizations** do:

```math
T=(x/c)^r,\qquad \eta=\mathrm{gd}\!\left(r\log(x/c)\right),\qquad \eta_x\big|_{c,r}=\frac{rS}{x},\quad \eta_r\big|_{x,c}=uS,\quad \eta_c\big|_{x,r}=-\frac{rS}{c}.
```

For the squared-profile field, the active-parameter derivatives (holding $`x`$ and the other parameter fixed) are

```math
\mathcal B_r\big|_{x,c}=-2u\mathcal BW,\qquad \mathcal B_c\big|_{x,r}=\frac{2r}{c}\mathcal BW.
```

The map $`(x,c,r)\mapsto(P,\mathcal B)`$ without carrying $`c,r`$ would lose the family parameters. Every source-to-target map in the framework must state which parameters are retained.

An immediate *measure* identity is

```math
f(x;r,c)\,dx=\frac12S\,du=\frac{d\eta}{2r},\qquad \frac{2r}{\pi}f(x;r,c)\,dx=\frac{d\eta}{\pi}.
```

Thus the **Gudermannian angle is uniform** on $`(-\pi/2,\pi/2)`$ under the *normalized original kernel measure*. This is not the **squared-profile/weighted-$`L^2`$** measure: see [§04.02](../04-probability-statistics/04-02-gudermannian-conic-laws.md) for the distinct arcsine and beta distributions.

## 9. Exact links to J, without conflating the Gram coefficient

For $`J_0=Ae^{ru}+Be^{-ru}`$, $`\mu_0=4AB>0`$ and $`u_0=\log(B/A)/(2r)`$, define the **centered normalized** linear pair

```math
R_0=\frac{J_0}{\sqrt{\mu_0}}=\cosh(r(u-u_0)),\qquad b_0=\frac{(J_0)_u}{r\sqrt{\mu_0}}=\sinh(r(u-u_0)).
```

All conic formulas of §§3–5 then hold with $`u`$ replaced by $`u-u_0`$, so the effective spatial center is $`x_0=ce^{u_0}`$. The fixed source coefficient $`B`$ only appears in $`\mu_0`$ and $`u_0`$; it is **not** $`\mathcal B_0=\mathrm{sech}^2(r(u-u_0))`$.

The generic shifted Gram envelope $`J_G=J_0+2C`$ satisfies $`J_G''=r^2(J_G-2C)`$, not $`J_G''=r^2J_G`$ when $`C\ne0`$. No blanket identification of its reciprocal with the unit-circle or cubic Master equations is valid without a dedicated normalization and restricted sector.

## 10. Evidence scope

The project sources already establish the circle/hyperbola shared projective point, Gudermannian derivative clock and Riccati/logistic correspondences. The screenshot's four rows were independently checked with symbolic differentiation, correcting the $`B`$ collision. The **parabolic invariant**, its off-leaf equations, curvature formulas, and probability pushforward distinctions are direct derivations in this chapter, with independent symbolic/numerical checks in [verify_conic_gudermannian.py](../_standards/verify_conic_gudermannian.py).

No claim of mathematical novelty, independent peer review, or forced geometric/physical interpretation is made. The new conic dictionary is a foundational *algebraic and chart* construction; further immersions, connections and bundles require additional data.

**Source files read:** `Symmetrical_Framework_Complete_Reference_2026-11-16_v2.md` §1/F; November 21 ZIP internal `00-meta/NOTATION.md` §§III.1–III.3, `04-follow-ups/profile-web.md` §§1–3, and `04-follow-ups/coupled-oscillator-and-modular-clock.md` (which uses $`B`$ for *yet other* coefficients and modular forms). This reinforces the scoped notation rule.

## 11. Comparison of parameter and Gudermannian second derivatives

For any selected argument field $`F(\theta)`$, set $`a=F_\theta`$ and $`d=F_{\theta\theta}`$. With $`\theta=r\log(x/c)`$ and $`u=\log(x/c)`$, the $`(x,c,r)`$ Hessian has

```math
F_{rr}=u^2d,\qquad F_{cc}=(r^2d+ra)/c^2,\qquad F_{rc}=-(a+ru\,d)/c.
```

| Object | $`F_{rr}|_{x,c}`$ | $`F_{cc}|_{x,r}`$ | $`F_{\eta\eta}|_{c,r}`$ |
|---|---|---|---|
| $`S`$ | $`u^2S(2W^2-1)`$ | $`[r^2S(2W^2-1)-rSW]/c^2`$ | $`-S`$ |
| $`W`$ | $`-2u^2HW`$ | $`[rH-2r^2HW]/c^2`$ | $`-W`$ |
| $`R`$ | $`u^2R`$ | $`[r^2R+rb]/c^2`$ | $`2R^3-R`$ |
| $`b`$ | $`u^2b`$ | $`[r^2b+rR]/c^2`$ | $`2b^3+2b`$ |
| $`P`$ | $`-u^2HW`$ | $`[rH/2-r^2HW]/c^2`$ | $`1/2-P`$ |
| $`H=S^2`$ | $`u^2(4H-6H^2)`$ | $`[r^2(4H-6H^2)-2rHW]/c^2`$ | $`2-4H`$ |
| $`\eta=\mathrm{gd}(\theta)`$ | $`-u^2SW`$ | $`[rS-r^2SW]/c^2`$ | $`0`$ |

Each column specifies what stays fixed. See the [full second-derivative chapter §00.09](00-09-second-derivative-charts.md) for all six Hessian entries, the $`f=S/(2x)`$ prefactor, the cumulative $`Q_q`$, and the resolution-explicit logarithmic slope $`q_0=rW`$.

## 12. Hopf–Villarceau as a companion chosen lift

For $`\theta>0`$, *independently chosen* phases $`\alpha,\beta`$ define $`\Psi=(Se^{i\alpha},We^{i\beta})\in S^3`$. Fix $`\delta=\beta-\alpha`$. Its chosen Hopf quotient is

```math
n=(2SW\cos\delta,2SW\sin\delta,S^2-W^2)=(\sin(2\eta)\cos\delta,\sin(2\eta)\sin\delta,\cos(2\eta)).
```

Consequently $`n_{\eta\eta}=-4n`$ at fixed $`\delta`$. The double-angle dependence follows from the chosen Hopf map; it is **not** a replacement $`r\mapsto2r`$. See [§05.04 — the selected Hopf–Villarceau construction](../05-differential-geometry/05-04-hopf-villarceau-selected-lift.md) for stereographic versus orthogonal versus Hopf projections, Villarceau circles, and marked modulus. Primary source: ZIP `05-companion/hopf-villarceau-atlas/hopf-villarceau-notes.md`.
