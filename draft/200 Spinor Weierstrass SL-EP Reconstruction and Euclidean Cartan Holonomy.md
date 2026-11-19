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

Under the standard Hopf convention $Q_H=-\Theta$ for the stated Weierstrass data (some geometric normalizations insert a constant factor), one obtains

```math
\mathscr W_z(p,q)\,dz^2=\Theta=-Q_H.
```

**Theorem 5.1 [D,V] (Wronskian–Hopf identity).** The Wronskian of the **Weierstrass spinor pair** is exactly the coefficient of the extrinsic Hopf quadratic differential, up to a declared sign. It is not constant in an arbitrary conformal coordinate.

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
