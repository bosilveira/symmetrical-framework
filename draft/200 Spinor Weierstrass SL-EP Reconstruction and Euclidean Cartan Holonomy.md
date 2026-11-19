---
id: SF-DRAFT-200
title: Spinor–Weierstrass SL–EP Reconstruction and Euclidean Cartan Holonomy
status: provisional
created: 2026-11-19
proposed_layers: [I, II, III]
depends_on: [SF-DRAFT-140, SF-DRAFT-150, SF-DRAFT-160, SF-DRAFT-170, SF-DRAFT-180, SF-DRAFT-190]
related_claims: [H73, H95, H100, H136, H299, H329, H332, H421, H466, H467, H468, H470]
---

# 200 Spinor–Weierstrass SL–EP Reconstruction and Euclidean Cartan Holonomy

**Status:** Provisional mathematical manuscript for the staging folder; not yet incorporated into canonical claims. [D] direct proof; [V] independent symbolic check; [K] classical mathematical theorem with hypotheses; [H] prior archival result retaining its verification status; [C] correction/counterexample; [O] open. A shared differential equation is not a claim of common physical realization.

**Question.** Does the rank-two SL–Riccati–EP web reconstruct an oriented Euclidean moving frame and minimal immersion? What is the global bundle, how does the missing spatial dimension reappear, and which data preserve spinor, Hopf, Euclidean affine and spectral holonomies? Is the selected Lamé–Riemann elliptic spectral curve isomorphism sufficient to promote the entire web into a flat spinor/Euclidean connection?

**Principal result.** On a nonumbilic patch of any Euclidean conformal minimal immersion with Weierstrass Gauss map $g$ and height differential $dh$, the quadratic spinor representation has Wronskian equal to the Hopf quadratic-differential coefficient. In the natural coordinate of that differential the Wronskian is constant and the two spinors solve one scalar second-order equation with the Schwarzian potential $-\tfrac12\{g,\xi\}$. Their quadratic products give the full three-dimensional Weierstrass immersion. For the canonical catenoid this construction supplies a real SL carrier of half-rate $r/2$, a positive Pinney Gram envelope, the exact induced surface metric and a normalized Hopf spinor, all with explicit $r,c,\mu$ bookkeeping. Globally these pieces require additional spin structures, reality data, zero/pole analysis and real immersion periods. They are a selected reconstruction mechanism, not a universal identification of all spectral SL operators with minimal-surface operators.

**Provenance:** The November 18 historical ZIP was reopened, especially the fundamental-forms/Willmore/Hopf module (H421–H428), Riemann marked periods (H466–H470), Lorentz Gram/Hopf module (H329–H332) and Sato Grassmannian (H136). The latest live drafts 160–190 were compared. External research sources appear in §22.

## 1. Four different bases and three dimensions

An immersed minimal surface has a real two-dimensional conformal domain $\Sigma$, equivalently a Riemann surface of complex dimension one. Its ambient target is $\mathbb R^3$. A finite-gap SL **spectral curve** $\Gamma$ also has complex dimension one, but a spectral point $P\in\Gamma$ is held fixed as the spatial SL coordinate $u$ varies. A chosen real oval is real one-dimensional. A quotient by an actual one-parameter surface-isometry group can have a one-dimensional orbit space.

None of the following equalities is automatic:

```math
\text{real symmetry orbit space}=\text{conformal surface}=\text{spectral curve}=\text{SL spatial line}.
```

The Riemann minimal-example conformal elliptic curve is **selected** to be isomorphic to the one-gap Lamé spectral elliptic curve by draft 170; this identifies the algebraic curves but does not identify a spatial SL trajectory with motion of the Gauss point. Minimality is the Euler–Lagrange equation for the area of a two-dimensional immersion in ambient three-space, not a three-dimensional volume variational problem.

## 2. The correct frame/translation groups [D,C]

A positively oriented orthonormal frame and an ambient position are an element of

```math
\mathrm{SE}(3)=\mathrm{SO}(3)\ltimes\mathbb R^3.
```

Its spin double cover is $\mathrm{SU}(2)\ltimes_{\mathrm{Ad}}\mathbb R^3$. The complexified spin Euclidean group can be expressed as

```math
\mathrm{SL}(2,\mathbb C)\ltimes_{\mathrm{Ad}}\mathfrak{sl}_2(\mathbb C),
```

with the complex translation representation $\mathbb C^3\cong\mathfrak{sl}_2(\mathbb C)$. The proposed unqualified $\mathrm{ISO}(3)\ltimes\mathrm{SL}(2)$ is not a canonical replacement: it double-counts rotations unless a specific action and quotient are prescribed. $\mathrm{SL}(2,\mathbb C)$ alone is not a unitary Euclidean rotation group; the real frame reduction is $\mathrm{SU}(2)$.

## 3. Flat ambient Cartan does not mean flat intrinsic tangent geometry [D,K]

On a simply connected minimal-surface patch choose an adapted Euclidean frame $F=(e_1,e_2,n)\in\mathrm{SO}(3)$ and position $X\in\mathbb R^3$. Put

```math
\Omega=F^{-1}dF,\quad e=F^{-1}dX,\qquad d\Omega+\Omega\wedge\Omega=0,\quad de+\Omega\wedge e=0.
```

The full Euclidean Cartan system is flat. The surface tangent block of $\Omega$ is its Levi–Civita connection, and the normal/tangent blocks encode the second fundamental form. Splitting the flat equations gives Gauss–Codazzi; the tangent curvature can still satisfy

```math
d\omega^{LC}=K_G\,\theta^1\wedge\theta^2,\quad K_G\ne0.
```

**Theorem 3.1 [K].** A positive first fundamental form and symmetric second form satisfying Gauss–Codazzi determine a local Euclidean immersion on a simply connected chart up to rigid motion, under standard regularity assumptions. This reconstructs the surface from $(I,II)$; it does not reconstruct $(I,II)$ from an unspecified scalar SL equation.

## 4. The exact Weierstrass spinor-square representation [D,K]

Let $(g,dh)$ be regular meromorphic Weierstrass data on a punctured Riemann surface $\Sigma^\circ$, with the archived convention

```math
\boldsymbol\Phi=\left(\frac12(g^{-1}-g),\frac i2(g^{-1}+g),1\right)dh,\qquad X=\mathrm{Re}\int\boldsymbol\Phi.
```

On a simply connected local complex coordinate chart $z$, choose holomorphic spinor coefficients $p(z),q(z)$ with appropriate local square roots and

```math
p^2\,dz=\frac{dh}{g},\qquad q=gp,\qquad q^2\,dz=g\,dh.
```

The same immersion differentials become the quadratic spinor forms

```math
\boldsymbol\Phi=\left(\frac{p^2-q^2}{2},\frac{i(p^2+q^2)}2,pq\right)dz.
```

Their complex Euclidean nullity is an algebraic identity:

```math
\Phi_1^2+\Phi_2^2+\Phi_3^2=\frac14[(p^2-q^2)^2-(p^2+q^2)^2]+p^2q^2=0.
```

**Theorem 4.1 [D,K] (local quadratic reconstruction).** The selected Weierstrass minimal immersion is exactly a quadratic construction from a pair of holomorphic spinor *half-differentials*. Conversely a locally nondegenerate holomorphic spinor pair defines closed null Weierstrass one-forms and hence a local conformal minimal immersion, with global real period and completeness conditions still required.

**Global restriction.** On a nonsimply-connected domain, $p,q$ are not necessarily global scalar functions. They are local coefficients of spinor half-differentials, patched by a chosen square root of the canonical bundle or its appropriate punctured variant. Signs and monodromy must be tracked. The global Gauss map $g=q/p$ can be single-valued even when each spinor changes sign.

## 5. CENTRAL IDENTITY: the Weierstrass spinor Wronskian is the Hopf quadratic differential [D,V]

Write $dh=h_z\,dz$ and $g_z=dg/dz$. From $q=gp$,

```math
\mathscr W_z(p,q):=pq_z-p_zq=p^2g_z=\frac{h_zg_z}{g}.
```

Define the quadratic differential

```math
\Theta=\frac{dg}{g}\,dh=\frac{h_zg_z}{g}\,dz^2.
```

Under the framework's convention $II=2\mathrm{Re}(Q_H)$ for the complex quadratic differential and with the selected surface-normal orientation, $Q_H=-\Theta/2$; consequently

```math
\mathscr W_z(p,q)\,dz^2=\Theta=-2Q_H.
```

**Theorem 5.1 [D,V] (Wronskian–Hopf identity).** The Wronskian of the **Weierstrass spinor pair** is exactly the coefficient of twice the extrinsic Hopf quadratic differential with the declared sign. It is not constant in an arbitrary conformal coordinate.

**Proof.** The $p_z$ terms cancel in $pq_z-p_zq$; substitute $p^2=h_z/g$. Under $z=z(\xi)$ the spinor coefficients change as $p_\xi=p_z\sqrt{dz/d\xi}$ and $q_\xi=q_z\sqrt{dz/d\xi}$, so

```math
\mathscr W_\xi=(dz/d\xi)^2\mathscr W_z.
```

The Wronskian transforms as a quadratic differential: this is why the constancy of the familiar SL Wronskian requires an additional coordinate/gauge normalization. The identity is a **geometric correspondence for a specially constructed spinor pair**, not for any arbitrarily selected pair of weighted SL eigenfunctions.

## 6. The Hopf-natural coordinate produces an actual Schwarzian SL carrier [D,V,K]

On a simply connected patch avoiding zeros and poles of $\Theta$, choose a branch of its square root and define

```math
d\xi=\sqrt{\Theta},\qquad\Theta=d\xi^2.
```

In the $\xi$ coordinate, the transformed half-differential coefficients $P(\xi),Q(\xi)$ obey

```math
PQ_\xi-P_\xi Q=1,\qquad g=Q/P.
```

Consequently, wherever $g_\xi\ne0$, a common sign choice gives

```math
P=\frac1{\sqrt{g_\xi}},\qquad Q=\frac g{\sqrt{g_\xi}}.
```

**Theorem 6.1 [D,V] (projective spinor-to-SL reconstruction).** Both coefficients solve the SAME complex second-order Sturm–Liouville-type equation without a first derivative:

```math
\psi_{\xi\xi}+\frac12\{g,\xi\}\psi=0,\qquad\{g,\xi\}=\frac{g_{\xi\xi\xi}}{g_\xi}-\frac32\left(\frac{g_{\xi\xi}}{g_\xi}\right)^2.
```

**Proof.** For $P=g_\xi^{-1/2}$,

```math
\frac{P_{\xi\xi}}P=-\frac12\{g,\xi\}.
```

Since $Q=gP$ and $PQ_\xi-P_\xi Q=1$ is constant, the identity $PQ_{\xi\xi}-P_{\xi\xi}Q=0$ implies $Q_{\xi\xi}/Q=P_{\xi\xi}/P$ wherever both are nonzero, continuing meromorphically. The displayed equation follows.

In the same coordinate, the entire Weierstrass triple is

```math
\boldsymbol\Phi=\frac{1}{2g_\xi}(1-g^2,\ i(1+g^2),\ 2g)\,d\xi.
```

Hence **the projective ratio $g$, the fixed Wronskian normalization, and the chosen natural coordinate reconstruct the null immersion one-forms explicitly**.

### 6.1 A coordinate-free version avoids choosing a multivalued natural parameter

In an arbitrary conformal chart $z$, let $\theta(z)=h_zg_z/g$ so $\Theta=\theta(z)dz^2$. The *normalized* projective pair

```math
P_z=(g_z)^{-1/2},\qquad Q_z=g(g_z)^{-1/2},\qquad\mathscr W_z(P_z,Q_z)=1
```

satisfies the Schwarzian equation

```math
\psi_{zz}+\frac12\{g,z\}\psi=0.
```

The original Weierstrass forms then carry an extra scalar factor:

```math
\boldsymbol\Phi=\theta(z)\left(\frac{P_z^2-Q_z^2}{2},\frac{i(P_z^2+Q_z^2)}2,P_zQ_z\right)dz.
```

This is the **weighted quadratic lift**: ordinary projective SL spinors determine the Gauss map, but the additional Hopf coefficient $\theta$ determines the actual scale and second fundamental form. **Without $\theta$ one cannot reconstruct a unique Euclidean immersion.**

## 7. The spinor Hermitian norm is the surface CONFORMAL FACTOR [D,V]

Let $\rho(z,\bar z)^2=|p(z)|^2+|q(z)|^2$, with $p,q$ the actual Weierstrass spinors of §4. For $X=\mathrm{Re}\int\boldsymbol\Phi$,

```math
ds_\Sigma^2=\frac12\sum_{j=1}^3|\Phi_j/dz|^2|dz|^2=\frac14(|p|^2+|q|^2)^2|dz|^2.
```

**Theorem 7.1 [D,V] (spinor-norm metric reconstruction).** The positive spinor norm determines the induced conformal factor exactly:

```math
e^{2\omega}=\frac{\rho^4}{4},\qquad e^\omega=\frac{\rho^2}{2}.
```

**Proof.** A direct quadratic calculation gives

```math
\left|\frac{p^2-q^2}{2}\right|^2+\left|\frac{i(p^2+q^2)}2\right|^2+|pq|^2=\frac12(|p|^2+|q|^2)^2.
```

The induced metric for $X=\mathrm{Re}\int\Phi$ is half the squared Hermitian norm of its complex null differential.

**Important restriction.** This $\rho(z,\bar z)$ is initially a **two-real-variable** positive function on a conformal surface, not automatically the solution of a one-dimensional real Pinney ODE. A one-dimensional EP theorem requires a declared real slice or continuous-symmetry reduction and a common *real-coefficient* carrier for the restricted spinors. The catenoid meets those conditions explicitly; a generic minimal surface does not.

## 8. FULL CANONICAL EXAMPLE: the catenoid WE spinors satisfy the half-rate linear carrier [D,V]

Keep $r,c,\mu>0$ and the canonical coordinate

```math
u=\ln(x/c),\qquad \zeta=u+iv,\qquad v\sim v+\frac{2\pi}{r}.
```

Choose the historical catenoid Weierstrass data

```math
g_C(\zeta)=-e^{r\zeta},\qquad dh_C=d\zeta.
```

An explicit compatible pair of holomorphic spinor coefficients is

```math
p(\zeta)=i\,e^{-r\zeta/2},\qquad q(\zeta)=-i\,e^{r\zeta/2}.
```

Direct substitution gives

```math
g_C=q/p,\qquad p^2=1/g_C,\qquad q^2=g_C,\qquad pq=1,\qquad pq_\zeta-p_\zeta q=r.
```

Their quadratic Weierstrass triple is precisely

```math
\boldsymbol\Phi_C=(\sinh(r\zeta),-i\cosh(r\zeta),1)\,d\zeta.
```

Its real primitive recovers the catenoid, with no untracked scale:

```math
X_C(u,v)=\left(\frac{\cosh(ru)\cos(rv)}r,\frac{\cosh(ru)\sin(rv)}r,u\right).
```

### 8.1 Exact rate-halving and symmetric-square hierarchy

The two spinor components satisfy the SAME constant-coefficient linear differential equation

```math
p_{\zeta\zeta}=\frac{r^2}{4}p,\qquad q_{\zeta\zeta}=\frac{r^2}{4}q.
```

The projective Gauss map has

```math
\{g_C,\zeta\}=-\frac{r^2}{2},\qquad -\partial_\zeta^2+\frac{r^2}{4}
```

as its associated zero-energy projective carrier expression. The Weierstrass **quadratic** forms $p^2,pq,q^2$ lie in the three-dimensional symmetric-square solution space with exponential rates $-r,0,+r$; their real combinations produce $R=\cosh(ru)$ and $b=\sinh(ru)$.

**Theorem 8.1 [D,V] (spinor half-rate).** The catenoid's rate-$r$ hyperbolic fields are quadratic expressions in a flat rank-two carrier with rates $\pm r/2$. The original canonical weighted SL free carrier of drafts 120/180, under $U_cf=xf$, is instead $-\partial_u^2+r^2$. Its coefficient is **four times the spinor carrier's coefficient** at fixed $u$; they are related by symmetric-square/rate multiplication, not literally the same differential operator.

### 8.2 The WE spinor Gram norm is an Ermakov–Pinney amplitude

Along the real meridian,

```math
\rho(u)^2=|p(u)|^2+|q(u)|^2=e^{-ru}+e^{ru}=2R(u).
```

The two real independent solutions $\phi_1=e^{-ru/2}$, $\phi_2=e^{ru/2}$ have Wronskian $\mathscr W=r$ and positive Gram matrix $I_2$. Therefore

```math
\rho_{uu}=\frac{r^2}{4}\rho+\frac{r^2}{\rho^3},\qquad \rho=\sqrt{2\cosh(ru)}.
```

This is a TRUE constant-strength Pinney equation for the selected real carrier, with inverse-cubic strength $k_{\rm EP}=r^2$ and hyperbolic linear part $\omega^2=-r^2/4$.

The original framework's reciprocal envelope is

```math
a(u)=\mu^{1/4}\sqrt{R(u)},\qquad \rho=\sqrt2\,\mu^{-1/4}a.
```

Its scaled equation is exactly the historical separatrix EP form

```math
a_{uu}=\frac{r^2}{4}a+\frac{\mu r^2}{4a^3}.
```

**Theorem 8.2 [D,V] (exact WE–EP scale identification).** On this selected catenoid, the **positive Hermitian norm of the Weierstrass spinor pair is, up to the explicit $\mu$ scaling, precisely the canonical EP envelope**. The induced metric is recovered as

```math
ds_C^2=\frac{\rho^4}{4}|d\zeta|^2=R(u)^2(du^2+dv^2).
```

This explains the appearance of EP's quadratic Gram expression in the local geometry. It is stronger than matching a few similar differential equations, but it holds for this **selected real one-variable reduction**, not automatically for arbitrary finite-energy Duffing trajectories or generic minimal surfaces.

### 8.3 The Hopf quadratic differential calibration

The Wronskian–Hopf identity gives

```math
\Theta_C=\frac{dg_C}{g_C}\,dh_C=r\,d\zeta^2,\qquad Q_{H,C}=-\frac r2d\zeta^2
```

with the paper's convention $II=2\mathrm{Re}(Q_H)$. This independently verifies the factor of $1/2$, the spinor Wronskian, and the canonical constant Hopf differential of the catenoid.

## 9. From the WE spinor to the Hopf map: EXACT normalization, but an independent phase [D,V]

Normalize the catenoid Weierstrass spinor pointwise:

```math
\eta(\zeta)=\frac1{\rho(u)}\binom{p(\zeta)}{q(\zeta)}\in S^3\subset\mathbb C^2.
```

Its stereographic Hopf projection is

```math
g_C=q/p=-e^{r\zeta}\in\mathbb{CP}^1\cong S^2.
```

On a simply connected chart, the normalized spinor defines a **local** $\mathrm{SU}(2)$ frame by

```math
U_\eta=\begin{pmatrix}\eta_1&-\bar\eta_2\\ \eta_2&\bar\eta_1\end{pmatrix},\qquad U_\eta^\dagger U_\eta=I,\quad\det U_\eta=1.
```

However the **Hopf horizontal lift** along a path is not determined merely by normalizing the length $\rho$. The connection is the independently specified Hermitian one-form

```math
A_{\rm Hopf}=-i\,\eta^\dagger d\eta.
```

For the explicit catenoid spinor the real meridian and angular components are

```math
(A_{\rm Hopf})_u=0,\qquad (A_{\rm Hopf})_v=\frac r2\tanh(ru)=\frac r2W.
```

Thus the chosen lift is horizontal along meridians but **not** along generic angular paths. A horizontal lift of a prescribed path requires an additional compensating phase determined by integrating $A_{\rm Hopf}$; its existence along a path is not the same as EP amplitude positivity.

### 9.1 Connection curvature and catenoid Levi–Civita curvature

Differentiate the Hopf potential to get

```math
F_{\rm Hopf}=dA_{\rm Hopf}=\frac{r^2}{2}S^2du\wedge dv.
```

The catenoid's Levi–Civita tangent curvature form in the same orientation is

```math
d\omega_C^{LC}=-r^2S^2du\wedge dv.
```

Hence the exact selected connection relation is

```math
F_{\rm Hopf}=-\frac12d\omega_C^{LC}.
```

This is a genuine **connection-curvature correspondence**, inherited from the Gauss map and the selected immersed geometry. It is not an identification of the independent spatial SL rank-two carrier matrix with the $U(1)$ Hopf connection.

### 9.2 A global spin-sign obstruction even on the catenoid

Under one full catenoid angular circuit $v\mapsto v+2\pi/r$,

```math
p\mapsto-p,\qquad q\mapsto-q,\qquad g_C\mapsto g_C,\qquad U_\eta\mapsto-U_\eta.
```

The $\mathrm{SO}(3)$ moving frame and Gauss map descend even though this particular local $\mathrm{SU}(2)$ spin lift picks up the nontrivial central sign. A globally single-valued spinor representative requires a different patching/double-cover choice. **This is a real global obstruction which the one-dimensional EP ODE does not resolve**.

For comparison, the standard north-chart Hopf spinor $(1,g_C)/\sqrt{1+|g_C|^2}$ has angular potential $\frac r2(1+W)\,dv$; it differs from the locally displayed WE-spinor potential by $\frac r2dv$, a change of spinor gauge whose angular phase is not single-valued after one circuit. Holonomy must incorporate that patch transition.

## 10. Riemann minimal examples: Hopf factor is nonconstant and the natural SL coordinate branches [D,H,C]

The historical Riemann minimal-example elliptic data are

```math
w_R^2=g_R(g_R-\lambda_R)(\lambda_Rg_R+1),\qquad \lambda_R>0,\qquad dh_R=A_R\,\frac{dg_R}{w_R},\quad A_R>0.
```

Choose a local holomorphic Abelian coordinate

```math
d\zeta=\frac{dg_R}{w_R},\qquad (g_R)_\zeta=w_R,\qquad (h_R)_\zeta=A_R.
```

The spinor Wronskian/Hopf coefficient is now

```math
\theta_R(\zeta)=\frac{(h_R)_\zeta(g_R)_\zeta}{g_R}=A_R\frac{w_R}{g_R},\qquad \Theta_R=A_R\frac{w_R}{g_R}\,d\zeta^2.
```

**Theorem 10.1 [D,H] (Riemann surface spinor carrier).** On any simply connected patch avoiding zeros/poles of $\Theta_R$, the square-root coordinate

```math
d\xi=\sqrt{\Theta_R}=\sqrt{\frac{A_R}{g_Rw_R}}\,dg_R
```

normalizes the Weierstrass spinor Wronskian to one. The corresponding normalized spinors solve $\psi_{\xi\xi}+\frac12\{g_R,\xi\}\psi=0$ and reproduce **the complete Riemann Weierstrass triple** by the quadratic construction of §6.

Unlike the catenoid case, $\theta_R$ is generally nonconstant, and $\xi$ is only locally single-valued. In particular, at a simple finite branch point where $w_R=0$ and $g_R\ne0$, the Abelian coordinate $\zeta$ is regular while $\theta_R$ vanishes to first order. Locally $\xi-\xi_0\sim(\zeta-\zeta_0)^{3/2}$ and $g_R-g_0\sim(\xi-\xi_0)^{4/3}$; therefore the normalized Schwarzian has the singular leading behavior

```math
\{g_R,\xi\}\sim-\frac7{18}(\xi-\xi_0)^{-2}.
```

This branching is the natural-coordinate singularity at an **umbilic/zero of the Hopf differential**. The immersed surface itself can remain smooth there. It is precisely why a globally regular single-variable SL carrier over the whole compact elliptic curve does not follow from the local natural-coordinate theorem.

## 11. Riemann circular foliations do NOT generally define a rotational Killing quotient [C,D,K]

Every horizontal plane intersects a Riemann minimal example in a circle or line; this does NOT mean all those circles are orbits of a *common* one-parameter Euclidean isometry. The circle centers generally move between horizontal planes.

A generic circle-foliated surface has a local parametrization

```math
X(z,\theta)=(a(z)+R(z)\cos\theta,\ b(z)+R(z)\sin\theta,\ z).
```

Its metric coefficients include

```math
g_{z\theta}=R(-a'(z)\sin\theta+b'(z)\cos\theta)
```

and

```math
g_{zz}=1+a'^2+b'^2+R'^2+2R'(a'\cos\theta+b'\sin\theta).
```

Unless the center derivatives satisfy additional restrictions, these coefficients depend on $\theta$. The vector field $\partial_\theta$ is **not Killing**, so Fourier modes in $\theta$ are coupled by the geometric Laplacian and cannot automatically be used to obtain independent one-dimensional SL operators.

**Theorem 11.1 [D,C] (foliation is weaker than symmetry).** Circular cross-sections do not imply an isometric $U(1)$ action. A separation into independent fiber charges is justified only after establishing an actual invariant metric/connection or a different proven separation ansatz. This is why the genus-one Riemann Weierstrass/period construction must not be described as simply the same axial reduction used for the catenoid.

A helicoid similarly has a **screw** one-parameter isometry with generally noncompact orbits, not the same compact rotational circle quotient as the catenoid. A screw quotient requires tracking translational/rotational monodromy and a different global domain.

## 12. The Euclidean normal direction survives as WE Gauss data and a METRIC-WEIGHTED potential [D,V]

For a Euclidean minimal immersion with first fundamental metric $g_\Sigma$ and Gauss curvature $K_G\le0$, the squared norm of its second fundamental form is

```math
|A_\Sigma|^2=-2K_G.
```

The nonnegative-Laplacian-sign **negative Jacobi expression** is

```math
B_\Sigma=-(\Delta_\Sigma+|A_\Sigma|^2)=-\Delta_\Sigma+2K_G.
```

In conformal coordinates $ds_\Sigma^2=e^{2\omega}(du^2+dv^2)$, this is

```math
B_\Sigma=e^{-2\omega}(-\partial_u^2-\partial_v^2)+2K_G.
```

Multiplication of its **zero equation** by the positive conformal factor produces the flat-leading differential expression

```math
e^{2\omega}B_\Sigma=-\partial_u^2-\partial_v^2+2e^{2\omega}K_G.
```

**Theorem 12.1 [D,K].** The extrinsic normal geometry enters the Jacobi equation as $2K_G$, but the corresponding conformally flattened potential is **$2e^{2\omega}K_G$**, not $2K_G$. This difference is essential under surface-to-ODE reduction.

### 12.1 Exact Gauss-map formula for the conformal Jacobi potential

For the WE data $(g,dh)$, with $dh=h_z\,dz$,

```math
e^{2\omega}=\frac{(1+|g|^2)^2}{4|g|^2}|h_z|^2.
```

The Gauss-map pullback of the round metric is

```math
III=\frac{4|g_z|^2}{(1+|g|^2)^2}|dz|^2=-K_G\,I.
```

Therefore

```math
K_G=-\frac{16|g|^2|g_z|^2}{(1+|g|^2)^4|h_z|^2},\qquad 2e^{2\omega}K_G=-\frac{8|g_z|^2}{(1+|g|^2)^2}.
```

The last expression is independent of the overall amplitude $h_z$, as expected for the conformally multiplied zero-Jacobi equation. But it usually depends on **both real surface coordinates** through $g(z)$ and $\bar g(\bar z)$.

For the catenoid $g=-e^{r(u+iv)}$,

```math
2e^{2\omega}K_C=-2r^2\mathrm{sech}^2(ru).
```

Only because this coefficient is independent of $v$ does angular separation give the familiar PT equation.

### 12.2 Exact Riemann counterexample to the universal Lamé-potential claim

In the archived Riemann Abelian coordinate $d\zeta=dg_R/w_R$, one has $g_{R,\zeta}=w_R$, so

```math
2e^{2\omega_R}K_R=-\frac{8|w_R|^2}{(1+|g_R|^2)^2}.
```

This is the exact *conformal Jacobi potential* of the selected Riemann immersion. It is not, as a function on the full real two-dimensional conformal domain, automatically equal to the real one-gap Lamé spectral potential

```math
V_{\rm Lame}(u)=2m r^2\mathrm{sn}^2(ru\mid m)-2mr^2.
```

The smooth spectral elliptic-curve isomorphism of draft 170 is real and exact, but it does **not** turn the Riemann surface Jacobi operator into the one-gap Lamé differential operator. Equality of the underlying compact elliptic curves is weaker than equality of these two differential operators, their weights and their domains.

## 13. The selected Lamé–Riemann elliptic isomorphism transports a PROJECTIVE STRUCTURE, but not spatial SL flow [D,H,C]

The selected real smooth curve isomorphism of draft 170 is

```math
m=(1+\lambda_R^2)^{-1},\quad k_R=\lambda_R^{-1}-\lambda_R,\quad D_R=\lambda_R+\lambda_R^{-1},
```

```math
g_R=-k_R-\frac{D_R}{r^2}E,\qquad y_R=\frac{D_R^{3/2}}{r^3}\eta,\qquad w_R=\sqrt{\lambda_R}y_R.
```

Its Weierstrass height differential pulls back to the **spectral elliptic curve** as

```math
dh_R=A_R\frac{dg_R}{w_R}=-A_Rr\sqrt m\,\frac{dE}{\eta}.
```

The corresponding Hopf quadratic differential is a **marked meromorphic form on the smooth spectral curve**:

```math
\Theta_R=\frac{dg_R}{g_R}\,dh_R=\frac{A_RD_R\sqrt m}{r\,g_R(E)}\,\frac{dE^2}{\eta}.
```

A local natural coordinate may be defined by $d\xi^2=\Theta_R$, away from zeros and poles. The explicit affine relation $g_R(E)=aE+b$ is Möbius with vanishing Schwarzian in the energy chart:

```math
\{g_R,E\}=0.
```

By the Schwarzian chain rule one then obtains the exact identity

```math
\{g_R(E(\xi)),\xi\}=\{E(\xi),\xi\}.
```

**Theorem 13.1 [D,H] (selected projective-curve transport).** The affine Lamé–Riemann curve map identifies the Gauss-map Schwarzian projective structure with the Schwarzian of the **spectral coordinate regarded as a function of the natural surface coordinate $\xi$**. This is a rigorous curve-coordinate/projective result, but it does **not** identify the real Lamé spatial ODE with the surface spinor ODE: the Lamé carrier evolves in $u$ at fixed $E$, whereas here $E(\xi)$ is necessarily **moving along the spectral curve**.

This is the precise extra arrow that the blanket “SL Riccati parallel transports the Riemann Gauss map” assertion is missing.

## 14. The sign of the energy and the actual degenerations matter [D,H,C]

Drafts 160–170 distinguish:

- The nodal spectral normalization of a real PT soliton operator, with $E=-s^2$, catenoid height differential $dh_C=2ds/(s^2-r^2)$, and an independent Gauss map choice $g_C=-(s-r)/(s+r)$.
- The smooth selected one-gap Lamé spectral curve, isomorphic to the Riemann minimal-example elliptic curve for $0<m<1$, with three branch points and full marked Weierstrass forms.
- Two distinct nodal limits $m\to1$ (collapsed allowed band/PT bound level) and $m\to0$ (closed forbidden gap/free), with limiting logarithmic and arctangent differentials respectively.

The fact that **the catenoid height differential emerges at the PT spectral node** is an exact differential pullback. But this **alone** does not choose the needed Gauss map, spin structure, conformal metric, Hermitian real form, self-adjoint operator domain or global immersion periods. Those are new, independently typed data.

The rational spectral-normalization coordinate $s$ can be related to a surface coordinate by $t=(s-r)/(s+r)=e^{r\zeta}$, which means

```math
s(\zeta)=r\,\frac{1+e^{r\zeta}}{1-e^{r\zeta}}=-r\coth(r\zeta/2),\qquad E(\zeta)=-s(\zeta)^2.
```

Thus the spectral energy *varies* along this selected surface parametrization. It is not an isospectral trajectory of the original PT eigenvalue equation.
