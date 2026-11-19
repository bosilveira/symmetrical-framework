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

## 15. Decisive NO-GO: projective SL + positive EP norm do not determine global immersion [D,V,C]

Given Weierstrass data $(g,dh)$, let the Bonnet/associate family be obtained by

```math
dh_\delta=e^{i\delta}dh,\quad g_\delta=g,\quad\boldsymbol\Phi_\delta=e^{i\delta}\boldsymbol\Phi.
```

The compatible WE spinors transform by a **common phase**

```math
p_\delta=e^{i\delta/2}p,\qquad q_\delta=e^{i\delta/2}q.
```

Therefore

```math
q_\delta/p_\delta=g,\qquad |p_\delta|^2+|q_\delta|^2=|p|^2+|q|^2.
```

Their Schwarzian projective potential $\frac12\{g,z\}$ and positive norm are **unchanged** in a fixed conformal coordinate, and so is the induced metric. But the Wronskian/Hopf quadratic differential and the real immersion periods change:

```math
\mathscr W_\delta=e^{i\delta}\mathscr W,\quad \Theta_\delta=e^{i\delta}\Theta,\quad\mathrm{Re}\oint_\gamma\boldsymbol\Phi_\delta=\cos\delta\,\mathrm{Re}\oint_\gamma\boldsymbol\Phi-\sin\delta\,\mathrm{Im}\oint_\gamma\boldsymbol\Phi.
```

**Theorem 15.1 [D,C] (Bonnet ambiguity of the SL–EP reconstruction).** Knowledge of the projective ratio $g$, its Schwarzian ODE, the Hermitian spinor norm and the resulting conformal surface metric is insufficient to reconstruct the **global Euclidean immersion**: the Bonnet phase and the complete real period homomorphism remain independent data. The same local intrinsic geometry can have different global immersion periods.

### 15.1 The canonical explicit counterexample

The catenoid WE period is

```math
\oint_{\gamma}\boldsymbol\Phi_C=(0,0,2\pi i/r),\qquad\mathrm{Re}\oint_\gamma\boldsymbol\Phi_C=0.
```

Its conjugate helicoid at $\delta=\pi/2$ has exactly the same $g$, projective Schwarzian and positive spinor Gram norm, but

```math
\mathrm{Re}\oint_\gamma i\boldsymbol\Phi_C=(0,0,-2\pi/r)\ne0.
```

Thus the catenoid immersion descends to the punctured-plane conformal quotient, whereas the helicoid needs the angular universal cover (or a specified translation quotient). The **Spin(3) normalized frame** and its local Hopf projection still do not remove this translation-period defect.

This is a rigorous counterexample to any overstrong theorem claiming that the SL–EP equations alone already encode and preserve *all* ambient $\mathrm{ISO}(3)$ holonomies.

### 15.2 Scale ambiguity even before periods

Keeping $g$ fixed but replacing $dh$ by $\Lambda dh$ for real $\Lambda>0$ multiplies the induced metric by $\Lambda^2$, while leaving the Gauss-map Schwarzian unchanged. Its WE spinors scale by $\sqrt\Lambda$ and their Hermitian norm by $\Lambda$. Hence the **projective SL operator alone** does not determine even the metric scale: a Hopf quadratic differential/Weierstrass height normalization is an extra datum.

## 16. Four actual holonomies on the same chosen conformal/spectral curve [D,H,C]

| Connection or integral | Base path or evolution | Fiber/data | Holonomy or conserved quantity |
|---|---|---|---|
| Spatial SL transfer | $u$ varies with spectral point $E$ FIXED | solution vector in $\mathbb C^2$ | Wronskian and transfer matrix |
| Gauss–Manin period transport | elliptic modulus varies, cycles marked | $H_1$ / cohomology local system | intersection matrix / period monodromy |
| Hopf/Berry principal connection | a path in the Gauss sphere (pulled back along $g$) | normalized $U(1)$ phase | Berry phase and first Chern class |
| WE affine translation | a cycle on punctured conformal surface | affine $\mathbb R^3$ position | $\mathrm{Re}\oint\boldsymbol\Phi$ |
| Ambient adapted Euclidean Cartan | path on immersed surface | $\mathrm{SE}(3)$ frames/positions | rotational spin sign and translational monodromy, subject to global frame choices |

Their underlying spaces, path variables, connection groups and reality conditions differ. An exact isomorphism of two elliptic curves identifies corresponding **meromorphic differentials and cycles when those are explicitly transported**, but it does not automatically conjugate all five connections.

The correct global reconstruction criteria are (at least): existence of a compatible global spin structure or spin-cover patching, globally valid meromorphic WE forms and immersion regularity, reality conditions for a Euclidean immersion, and vanishing of the required real periods (or membership in a specified translation lattice). Neither a local Wronskian nor the scalar weighted $L^2$ norm imposes all these conditions.

## 17. Enneper–Weierstrass is flat AFFINE reconstruction; Sym–Tafel is an ADDITIONAL loop-frame construction [D,K,C]

The standard WE immersion is

```math
X(p)=X(p_0)+\mathrm{Re}\int_{p_0}^p\boldsymbol\Phi,\qquad d\boldsymbol\Phi=0\ \text{away from poles}.
```

This is flat **affine translation integration** in the Euclidean ambient target; its translational monodromy is $\mathrm{Re}\oint_\gamma\boldsymbol\Phi$.

The Sym–Tafel construction, by contrast, requires a **separately supplied spectral-parameter family of flat matrix connections**. For example if

```math
d\Psi(z,\bar z;\lambda)=U(z,\bar z;\lambda)\Psi,\quad dU-U\wedge U=0
```

under the left-frame sign convention and suitable reality conditions, define the Lie-algebra-valued immersion candidate

```math
X_{\rm ST}=\Psi^{-1}\partial_\lambda\Psi.
```

Differentiating gives the exact formula

```math
dX_{\rm ST}=\Psi^{-1}(\partial_\lambda U)\Psi.
```

A real $\mathfrak{su}(2)\cong\mathbb R^3$ surface is obtained only with the appropriate loop-group real form, regularity, normalization and a value of $\lambda$. **Theorem 17.1 [D,C].** The WE construction does not require any spectral-parameter family. The Sym–Tafel construction does. These two immersion formulas can be gauge-equivalent **for selected integrable extended frames**, but they are not automatically the same reconstruction for every flat rank-two carrier.

Likewise a generic *single-variable* SL system has a formally flat one-form $A(u,E)du$; to obtain a nontrivial **two-variable zero-curvature/Lax pair**, one must supply a second operator/coordinate and verify compatibility. Flatness in one dimension is automatic and cannot by itself prove the minimal-surface Gauss–Codazzi equations.

## 18. The precise extent of the classical minimal-surface classification [K,C]

A deep established classification theorem says that **connected properly embedded minimal planar domains** in $\mathbb R^3$ are the plane, catenoid, helicoid, and Riemann minimal examples under the classical proper-embeddedness hypotheses (Meeks–Pérez–Ros; see sources). The Riemann examples are notable for foliations by circles and lines in parallel planes; the statement is not a classification of all minimal surfaces by spectral genus.

**Correction [C].** It is false that the catenoid, helicoid and Riemann examples exhaust *all* genus-zero/genus-one WE or SL–EP realizations. For instance, the Enneper surface is a classical immersed genus-zero minimal surface not in the properly embedded list; Scherk, Costa, and many other minimal surfaces satisfy different global topology or embeddedness hypotheses. Moreover “genus of the compactified conformal domain,” “genus of the Lax spectral curve,” and “genus of a quotient by translations” are three distinct invariants.

The classification result is valuable precisely **because it is restricted and global**. It should not be promoted to a universal classification of every spectral elliptic curve or every local second-order carrier.

## 19. The package that really does reconstruct a minimal surface [D,K]

**Theorem 19.1 (typed spinor–projective–Weierstrass reconstruction, local).** Fix a simply connected complex coordinate patch $U$ on a Riemann surface. Let $g:U\to\mathbb{CP}^1$ be nonconstant meromorphic and let $\Theta$ be a holomorphic quadratic differential such that

```math
dh=\frac{g\,\Theta}{dg}
```

defines meromorphic WE height data whose triple $\boldsymbol\Phi=(\frac12(g^{-1}-g),\frac i2(g^{-1}+g),1)dh$ is regular and nondegenerate on the intended immersion patch. Suppose local compatible spinor square roots exist.

Then:

1. The local pair $p^2dz=dh/g$, $q=gp$ reconstructs all three WE forms quadratically, satisfying the nullity condition.
2. Its Wronskian obeys $\mathscr W_z(p,q)dz^2=\Theta$, and its Hermitian norm determines the metric $ds^2=\frac14(|p|^2+|q|^2)^2|dz|^2$.
3. Wherever $\Theta\ne0$ a natural coordinate $\xi$ with $d\xi^2=\Theta$ makes the Wronskian one, and the spinors solve the common projective equation $\psi_{\xi\xi}+\frac12\{g,\xi\}\psi=0$.
4. The complex null WE forms integrate to a real local conformal minimal immersion in $\mathbb R^3$, unique up to translation for fixed WE forms, and therefore to an adapted flat Euclidean Cartan frame with the corresponding Gauss–Codazzi data.

**Proof.** Items 1–3 are the algebraic identities of §§4–7 and local square-root/natural-coordinate theory. Item 4 is the classical WE representation, verified by holomorphic closedness, complex nullity and the nondegenerate metric; the fundamental theorem of surface theory gives the adapted frame.

**Theorem 19.2 (global period qualification).** On a punctured non-simply-connected surface, the local immersion descends to a global immersion into $\mathbb R^3$ exactly when all required real translation periods $\mathrm{Re}\oint_\gamma\boldsymbol\Phi$ vanish, and the data obey the needed global regularity/patching conditions. More general translation quotients permit periods lying in a specified lattice. A global $\mathrm{SU}(2)$ lift needs separate spin-bundle patching; it does not follow merely from the WE Gauss map.

**Status.** This is a theorem of a **specific decorated category** (Riemann surface, meromorphic Gauss map, Hopf differential, compatible spinors and periods), not a theorem that the original weighted SL carrier uniquely determines those decorations. It supplies a concrete exact reconstruction mechanism which the proposed “fiber holography” program can test against spectral data and genuine symmetry reductions.

## 20. THE LOCAL METRIC–CURVATURE–WRONSKIAN IDENTITY [D,V,K]

Let $p,q$ be the genuine local WE spinors of §4, with

```math
\rho^2=|p|^2+|q|^2,\qquad \vartheta(z)=pq_z-p_zq,\qquad\Theta=\vartheta(z)\,dz^2.
```

From the spinor metric formula,

```math
I=\frac{\rho^4}{4}|dz|^2.
```

The Gauss-map pullback of the unit spherical metric is

```math
III=\frac{4|g_z|^2}{(1+|g|^2)^2}|dz|^2.
```

Since $g=q/p$ and $g_z=\vartheta/p^2$, while $\rho^2=|p|^2(1+|g|^2)$, one gets directly

```math
III=\frac{4|\vartheta|^2}{\rho^4}|dz|^2.
```

For a Euclidean minimal surface the third fundamental form obeys $III=-K_G I$. Therefore

```math
K_G=-\frac{16|\vartheta|^2}{\rho^8}.
```

**Theorem 20.1 [D,V] (local first/third forms and curvature reconstructed from two spinorial scalar invariants).** For any regular nonumbilic WE minimal immersion, the positive Hermitian Gram norm $\rho$ and the WE spinor Wronskian $\vartheta$ determine the entire **conformal factors** of $I$ and $III$, and the Gaussian curvature $K_G$, through the exact three formulas above. The Hopf quadratic differential determines the trace-free second form by $Q_H=-\Theta/2$; with these data the Gauss–Codazzi fundamental theorem reconstructs the immersion up to Euclidean rigid motion on a simply connected chart.

Equivalently, if $I=e^{2\omega}|dz|^2$ and $III=e^{2\widetilde\omega}|dz|^2$, then

```math
e^{2\omega}e^{2\widetilde\omega}=|\vartheta|^2,\qquad -K_G e^{4\omega}=|\vartheta|^2.
```

This is a coordinate-normalization-sensitive identity: under holomorphic chart changes the right side transforms with the correct quadratic-differential weight. It is NOT equality of intrinsic **metrics** $I=III$.

### 20.1 The exact reciprocal metric pair in natural Hopf coordinates

In the $\xi$ coordinate where $\Theta=d\xi^2$, $\vartheta_\xi=1$. Therefore

```math
I=\frac{\rho_\xi^4}{4}|d\xi|^2,\qquad III=\frac4{\rho_\xi^4}|d\xi|^2,\qquad K_G=-\frac{16}{\rho_\xi^8}.
```

The two conformal factors are **reciprocal**. This is a precise differential-geometric mechanism behind the framework's frequent reciprocal envelopes: it is true for a selected nonumbilic minimal WE patch in its natural quadratic-differential coordinate, independently of any physical interpretation.

### 20.2 Independent r and mu calibration on the catenoid

In the canonical catenoid $\zeta$ coordinate,

```math
\vartheta_\zeta=r,\quad\rho_\zeta^2=2R,\quad I=R^2|d\zeta|^2,\quad III=r^2S^2|d\zeta|^2,\quad K_G=-r^2S^4.
```

In its natural coordinate $\xi=\sqrt r\,\zeta$ the transformed spinor norm is

```math
\rho_\xi^2=\frac{2R}{\sqrt r},\qquad K_G=-\frac{16}{\rho_\xi^8}=-r^2S^4.
```

The original framework's EP scale $a=\mu^{1/4}\sqrt R$ yields another exact expression, with its own declared normalization:

```math
K_C=-\frac{\mu^2r^2}{a^8}.
```

The amplitude $\mu$ cancels after substituting $a^8=\mu^2R^4$, so the intrinsic catenoid geometry is independent of the arbitrary field normalization. This is a valid **mathematical dictionary**, not a new physical curvature law.

## 21. On a REAL projective oval the EP clock is half the spherical Gauss angle [D,V]

The natural-coordinate spinor equation of §6 becomes a **real** SL-type carrier when the selected real slice has real monotone $g=g(\xi)$ and real Schwarzian, with $g_\xi\ne0$. Choose a real independent solution pair with Wronskian $+1$; for $g_\xi>0$, one may take

```math
P=\frac1{\sqrt{g_\xi}},\qquad Q=\frac g{\sqrt{g_\xi}},\qquad PQ_\xi-P_\xi Q=1.
```

The positive Gram amplitude has the closed form

```math
\rho^2=P^2+Q^2=\frac{1+g^2}{g_\xi}.
```

Since both solutions satisfy $y_{\xi\xi}+\frac12\{g,\xi\}y=0$, the Pinney theorem gives

```math
\rho_{\xi\xi}+\frac12\{g,\xi\}\rho=\rho^{-3}.
```

Define its EP clock by $\tau_\xi=\rho^{-2}$. Then

```math
\tau_\xi=\frac{g_\xi}{1+g^2},\qquad \tau=\arctan g+\mathrm{constant}.
```

The standard spherical arc-length along the stereographic **real meridian** is $d\ell_{S^2}=2\,dg/(1+g^2)$ for $dg>0$, so

```math
d\ell_{S^2}=2\,d\tau.
```

**Theorem 21.1 [D,V] (projective real-slice EP/Gauss half-angle).** On a real monotone Gauss-map slice in a natural Hopf coordinate, the normalized Pinney phase/clock is exactly **half the signed spherical Gauss-map meridian angle**, up to an additive constant. This follows from the linear projective pair and its Wronskian; it is a precise local relation between Riccati projectivization, the EP phase and the $S^2\simeq\mathbb{CP}^1$ Gauss geometry.

For $g_\xi<0$, orient the real coordinate or reverse the ordered solution pair so that the current/clock is positive; then the signed half-angle has the corresponding orientation reversal. For a generic complex-valued Gauss map no one-dimensional real meridian or real Pinney carrier is implied.

### 21.1 The Gudermannian emerges at the exact canonical catenoid scale

Along the catenoid meridian choose the real projective ratio $\widetilde g=e^{ru}=-g_C$, a fixed Möbius transformation of the Gauss coordinate. In the natural coordinate $\xi=\sqrt r\,u$, $\widetilde g_\xi=\sqrt r\,e^{ru}>0$, giving

```math
\rho_\xi^2=\frac{2\cosh(ru)}{\sqrt r},\qquad \frac{d\tau}{d\xi}=\frac{\sqrt r}{2\cosh(ru)}.
```

Integration gives the exact familiar primitive

```math
\tau(u)=\arctan(e^{ru})=\frac{\pi}{4}+\frac12\operatorname{gd}(ru),
```

where $\operatorname{gd}(s)=2\arctan(e^s)-\pi/2$. Thus the original arctangent/Gudermannian phase is not merely analogous to the spinor geometry: **it is the exact normalized real EP clock and half spherical Gauss-meridian angle of the canonical catenoid**.

**Global boundary.** This half-angle identity does **not** identify the EP clock with the independent Bonnet associate angle, or make a normalized spinor horizontal for the Hopf connection along every two-dimensional path. The angular Hopf potential of §9 remains nonzero; closed-loop Berry holonomy and puncture monodromy require the connection and patch transitions independently.

## 22. Three algebraic curves and THREE DIFFERENT line-bundle degrees [D,H,C]

The proposed single globally canonical spinor bundle must pass a straightforward **degree test** on the compactified symmetric or nonsymmetric Riemann elliptic curve $E_R$.

### 22.1 The spinor, BA, and Hopf bundles are not automatically one line bundle

On a smooth compact elliptic curve $E_R$ the canonical bundle $K_{E_R}$ has degree zero. A spin structure $S$ with $S^{\otimes2}=K_{E_R}$ has

```math
\deg S=0.
```

A generic **genus-one Krichever/BA construction** uses a nonspecial divisor $D_{\rm BA}$ of degree one (with its chosen spectral marked point and normalization), giving a corresponding line bundle

```math
\deg\mathcal O(D_{\rm BA})=1.
```

The Gauss map $g_R:E_R\to\mathbb{CP}^1$ has degree two. The pulled-back Hopf/tautological complex line (in the standard holomorphic convention) satisfies

```math
\deg(g_R^*\mathcal O(-1))=-2,\qquad \deg(g_R^*\mathcal O(1))=2.
```

**Theorem 22.1 [D,K,C] (topological nonidentification).** The bare spin structure, a generic degree-one BA divisor line, and the degree-two Gauss-pulled positive Hopf line have different degrees, so they cannot be mutually isomorphic as holomorphic line bundles **without additional divisor twists, duals or coverings**. There is no automatic globally canonical single line bundle carrying all three constructions.

The WE spinors here are **meromorphic** sections of a spinor bundle with allowed end divisors, so this degree calculation does **not** rule out a carefully constructed *twisted* correspondence. It makes the required twist a concrete, checkable datum rather than an assumed equivalence.

The sign of the Chern number in a unitary Hopf connection convention may be opposite to the holomorphic tautological $c_1$; the invariant point is the absolute degree two and the need to specify the dual/orientation.

### 22.2 A different j-invariant is already attached to the second fundamental form

The historical forms module H421 constructs the **product binary quartic** of the two principal fundamental forms. At a nonumbilic Euclidean minimal point $k_1=-k_2=k\ne0$ it is

```math
Q_{\rm form}(X,Z)=k(X^4-Z^4).
```

Its classical invariants are

```math
I(Q_{\rm form})=-12k^2,\qquad J(Q_{\rm form})=0,\qquad j_{\rm form}=1728.
```

By contrast, the selected one-gap Lamé spectral curve / Riemann elliptic conformal curve has

```math
j_{\rm spectral}(m)=256\frac{(1-m+m^2)^3}{m^2(1-m)^2},
```

which varies with the chosen modulus and equals $1728$ on the positive real family only at the symmetric point $m=1/2$.

**Corollary 22.2 [D,H,C].** The pointwise **binary-quartic elliptic curve of the fundamental forms** and the global **Lamé/Riemann elliptic spectral-conformal curve** are distinct algebro-geometric constructions, even on the same minimal surface. Matching the number $1728$ at a selected modulus does not identify their marked divisors, periods, spin bundles or global immersions.

This is another reason the “entire web encodes one universal canonical spectral/fiber bundle” claim is too strong without a precisely constructed functor between these differently typed objects.

## 23. Full r=2, c-and-mu-preserving regression [D,V]

Set $r=2$ while keeping $c,\mu>0$ explicit. The canonical variables, functions and profile are

```math
u=\ln(x/c),\quad R=\cosh(2u),\quad S=\mathrm{sech}(2u),\quad W=\tanh(2u),\quad f_\mu(x;2,c)=\frac{c^2x}{\sqrt\mu(x^4+c^4)}.
```

The catenoid WE spinors and their Wronskian are

```math
p=i e^{-\zeta},\quad q=-i e^\zeta,\quad g=-e^{2\zeta},\quad dh=d\zeta,\quad\mathscr W_\zeta=2.
```

Their quadratic forms integrate to

```math
X_C(u,v)=\left(\frac{\cosh(2u)\cos(2v)}2,\frac{\cosh(2u)\sin(2v)}2,u\right),\qquad v\sim v+\pi.
```

The spinor linear carrier, squared norm and EP equation are

```math
p_{\zeta\zeta}=p,\quad q_{\zeta\zeta}=q,\quad \rho^2=2\cosh(2u),\quad \rho_{uu}=\rho+4\rho^{-3}.
```

The canonical $\mu$-normalized envelope instead is

```math
a=\mu^{1/4}\sqrt{\cosh(2u)},\quad a_{uu}=a+\mu a^{-3},\quad \rho=\sqrt2\,\mu^{-1/4}a.
```

The induced metric, third form, Hopf differential and Gaussian curvature are

```math
I=R^2|d\zeta|^2,\qquad III=4S^2|d\zeta|^2,\qquad Q_H=-d\zeta^2,\qquad K_C=-4S^4.
```

The reciprocal spinor metric/curvature formula gives the same $K_C=-16|\mathscr W_\zeta|^2/\rho^8=-4S^4$ identically. The Hopf and LC curvature forms satisfy

```math
F_{\rm Hopf}=2S^2\,du\wedge dv,\qquad d\omega_C^{LC}=-4S^2\,du\wedge dv,\qquad F_{\rm Hopf}=-\frac12d\omega_C^{LC}.
```

The projective real-slice natural-coordinate EP clock is

```math
\xi=\sqrt2\,u,\qquad\tau=\arctan(e^{2u})=\frac\pi4+\frac12\operatorname{gd}(2u).
```

The catenoid height loop period is $\oint dh_C=\pi i$; the helicoid Bonnet conjugate has real height period $-\pi$. Both have the same projective Gauss map, spinor norm and local induced metric.

The underlying original weighted SL carrier remains

```math
U_c\mathcal L_xU_c^{-1}=-\partial_u^2+4,
```

whereas the surface spinor carrier along $u$ is $-\partial_u^2+1$ at zero energy. This **exact factor-four shift** demonstrates why one must keep the spinor symmetric-square representation distinct from the original weighted carrier.

Finally, at the symmetric Riemann modulus $\lambda_R=1$, the selected **smooth** one-gap Lamé spectral curve has branch energies $(-2,0,2)$ and the affine Gauss coordinate $g_R=-E/2$ (draft 170). Its *local projective surface carrier* is computed in a different natural coordinate $\xi$ and is generally not the same as the real Lamé spatial operator $-\partial_u^2+2mr^2\mathrm{sn}^2(ru|m)-2mr^2$.

## 24. Verification register and source limits

1. **WE spinor algebra [V]:** using $p=i e^{-r\zeta/2}$, $q=-i e^{r\zeta/2}$, SymPy verifies $pq=1$, $g=q/p=-e^{r\zeta}$, $\mathscr W=r$, and $\boldsymbol\Phi=(\sinh r\zeta,-i\cosh r\zeta,1)d\zeta$.
2. **Schwarzian [V]:** $\{-e^{r\zeta},\zeta\}=-r^2/2$; both half-rate spinors satisfy $\psi_{\zeta\zeta}-r^2\psi/4=0$. For generic $g$, direct differentiation of $g_\xi^{-1/2}$ gives $\psi_{\xi\xi}=-\frac12\{g,\xi\}\psi$.
3. **Hopf factor [V]:** the canonical WE Hopf normalization is $Q_H=-\Theta/2$, not $-\Theta$; its catenoid value is $Q_H=-r\,d\zeta^2/2$, matching the archived first/second form module.
4. **Metric identity [V]:** direct expansion of the three spinor bilinears gives $\sum|\phi_j|^2=\frac12(|p|^2+|q|^2)^2$; thus $ds^2=\rho^4|dz|^2/4$.
5. **Curvature identity [V]:** combining the Gauss spherical derivative $4|g_z|^2/(1+|g|^2)^2$ with $\mathscr W=p^2g_z$ gives $III=4|\mathscr W|^2\rho^{-4}|dz|^2$ and $K=-16|\mathscr W|^2\rho^{-8}$. Independent substitution of $\rho^2=2R$ and $\mathscr W=r$ reproduces $K_C=-r^2S^4$ symbolically.
6. **EP calibration [V]:** SymPy differentiation gives $\rho_{uu}=(r^2/4)\rho+r^2\rho^{-3}$ for $\rho=\sqrt{2\cosh(ru)}$; scaling by $\rho=\sqrt2\mu^{-1/4}a$ yields the original $\mu$-normalized EP equation exactly.
7. **Hopf horizontal qualification [V]:** for the explicit normalized spinor, $-i\eta^\dagger d\eta=(rW/2)dv$, so the spinor is not horizontal along generic angular curves. Differentiation gives $F_{\rm Hopf}=r^2S^2du\wedge dv/2=-d\omega_C^{LC}/2$.
8. **Spin monodromy [D]:** the half-exponential spinors acquire sign $-1$ around the catenoid angular circle, while the projective Gauss map is periodic; thus spin lifting needs an actual spin structure/patch transition.
9. **Riemann [D,H]:** $dg_R/d\zeta=w_R$, $dh_R/d\zeta=A_R$ imply $\Theta_R=A_Rw_Rd\zeta^2/g_R$, which generally vanishes at finite branch points and makes the natural coordinate branch. Near simple nonzero branch points, $g-g_0\sim(\xi-\xi_0)^{4/3}$ and $\{g,\xi\}\sim-7/[18(\xi-\xi_0)^2]$.
10. **Circular foliation [D,K]:** direct differentiation of a circle-centered surface shows explicit $\theta$ dependence when centers move. This precludes assuming a global rotational Killing quotient for generic Riemann examples.
11. **Conformal Jacobi [D,V]:** $B=-\Delta+2K$ becomes $-\Delta_0+2e^{2\omega}K$ after multiplying by $e^{2\omega}$. Direct substitution of WE data yields $2e^{2\omega}K=-8|g_z|^2/(1+|g|^2)^2$; catenoid gives the selected PT potential, while generic Riemann data remain genuinely two-variable.
12. **Lamé/Riemann [H]:** the affine elliptic isomorphism and complete WE pullbacks are already verified in draft 170; the added identity $\{g_R(E(\xi)),\xi\}=\{E(\xi),\xi\}$ follows from the Schwarzian chain rule for an affine map. It is not a claimed operator conjugation.
13. **Bonnet obstruction [V]:** $dh\mapsto e^{i\delta}dh$ multiplies the WE spinors by $e^{i\delta/2}$, leaves $g$ and their Hermitian norm unchanged, but rotates real immersion periods. The catenoid/helicoid vertical periods $0$ and $-2\pi/r$ are direct calculations.
14. **Bundle degrees [D,K]:** elliptic spin bundles have degree zero, a generic genus-one BA divisor line has degree one, and the Gauss-pulled tautological line has degree $-2$; no unqualified holomorphic line bundle isomorphism exists without twisting.
15. **Binary quartics [H]:** the H421 principal-form product quartic has $J=0$ and pointwise $j=1728$ on every nonumbilic minimal surface, whereas the Riemann/Lamé spectral elliptic $j$ varies with $m$. The two curves are different types.
16. **Domain and completeness [C]:** no claim here promotes a general complex projective spinor ODE to a self-adjoint real Hilbert SL operator. The WE immersion needs real periods; the spin lift needs separate signs/patches; Krichever requires spectral divisor data; and none of these follows from the existence of a nodal curve alone.
