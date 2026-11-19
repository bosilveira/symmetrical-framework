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
