---
id: SF-DRAFT-220
title: Tzitzéica Centro-Affine SL(3) Frames, Symmetric-Square SL(2), and Affine-Sphere Integrability
status: provisional
created: 2026-11-19
proposed_layers: [I, II, III]
depends_on: [SF-DRAFT-170, SF-DRAFT-180, SF-DRAFT-190, SF-DRAFT-200, SF-DRAFT-210]
related_claims: [H73, H100, H136, H153, H154, H421, H466, H470]
---

# 220 Tzitzéica Curves and Surfaces: The Centro-Affine SL(3) Lift and Its Intersection with the SL–EP Web

**Status:** Provisional mathematics. [D] derived with proof; [V] independently symbolically checked; [K] classical theorem with hypotheses; [H] prior framework result, unchanged scope; [C] correction or counterexample; [O] open. Tzitzéica, Ţiţeica and Tzitzeica denote the same mathematical name. No forced physical interpretation.

**Question.** Does the Tzitzéica curve invariant τ/d² furnish a rank-three Wronskian/jerk lift of the rank-two SL–EP web? How does the projective Wilczyński cubic extend the Schwarzian? Do affine spheres supply a genuine two-dimensional flat SL(3) integrability system, and can the resulting geometry be compared to the canonical catenoid/helicoid/Riemann minimal-surface bundle without conflation?

**Principal findings.** The curve condition is an exact third-order determinant equation, equivalent in centro-affine arclength to an SL(3,R) first-order companion frame with **constant coefficient of X**. The symmetric-square of any carrier ψ''=Qψ satisfies X'''=4QX'+2Q'X and yields the Tzitzéica invariant Q'/W³ in the unnormalized spinor-square coordinates. Hence the intersection with nonzero-constant Tzitzéica curves is exactly the selected **affine-linear/Airy** potentials; constant, Pöschl–Teller and generic Lamé Q do not automatically qualify. A genuine rank-three Tzitzéica curve with nonzero projective cubic is exhibited on the affine sphere xyz=1. The Tzitzéica **surface** PDE has a separate explicit 2D SL(3) zero-curvature Lax pair; a one-variable reduction produces a cubic elliptic first integral and an exact nodal Riccati degeneration. These are typed bridges, not identifications of all previous Euclidean and spectral geometries.

**Project sources inspected.** Actual November 18 ZIP: sato-grassmannian (H136, Drach and Lamé), fundamental-forms-willmore-hopf (H421–H428), riemann-marked-periods (H466–H470), foundational paper v0.3 (Ramanujan/Chazy/Darboux–Halphen). Live drafts 170–210 were checked, especially draft 210's squared eigenfunction. Independent sources: Bîlă on the determinant equation, Terng on affine-sphere SL3 Lax, Ovsienko–Tabachnikov on projective curves, and Tzitzéica surfaces (citations in §25).

## 1. Four different categories must not be conflated [C]

A **Tzitzéica space curve** X(t) in Euclidean 3-space satisfies an origin-dependent constant ratio of Euclidean torsion to squared osculating-plane distance. Its **centro-affine** reformulation eliminates metric factors and is invariant under unimodular linear transformations fixing the origin.

A **Tzitzéica surface** satisfies the distinct condition Gaussian curvature divided by the fourth power of tangent-plane distance is constant; properly centered affine spheres are classical cases. This is not the condition of Euclidean mean curvature zero.

A **projective plane curve** [X] in RP² remembers a line, not an absolute lift X; its Wilczyński invariant is a cubic differential and differs from the origin-referenced centro-affine torsion/distance constant.

A **moving affine frame** has group SL(3,R), not SO(3). Its volume-preserving frame structure is not by itself the Euclidean orthonormal moving-frame bundle of drafts 180/200.

## 2. Exact Tzitzéica curve equation: third-order Wronskian [D,K,V]

Let X:I→R³ be C³ with X'×X''≠0, and let D(t)=det(X,X',X'')≠0. The signed Euclidean torsion and positive distance to the osculating plane through X are

```math
\tau=\frac{\det(X',X'',X''')}{\|X'\times X''\|^2},\qquad d=\frac{|\det(X,X',X'')|}{\|X'\times X''\|}.
```

The Euclidean factors cancel EXACTLY:

```math
\mathcal T_X:=\frac{\tau}{d^2}=\frac{\det(X',X'',X''')}{\det(X,X',X'')^2}.
```

**Theorem 2.1 [D,V,K].** X is a Tzitzéica curve with fixed nonzero constant α precisely when

```math
\det(X',X'',X''')=\alpha\,\det(X,X',X'')^2,\qquad\alpha\ne0.
```

This is the Wronskian-type third-order equation described by N. Bîlă, Applied Mathematics E-Notes 23 (2023), 300–308. It is one scalar condition for three coordinate functions, not yet a uniquely specified third-order *vector* equation.

### 2.1 The exact transformation law

For any constant A∈GL(3,R) fixing the origin, the numerator scales by det A and the denominator by (det A)²:

```math
\mathcal T_{AX}=\frac{\mathcal T_X}{\det A}.
```

Therefore the numerical invariant is preserved under SL(3,R) and rescales under arbitrary GL(3,R); a general translation of the origin is NOT a symmetry. Under a smooth reparametrization s=s(t), the determinant D scales by (ds/dt)³ and the numerator by (ds/dt)⁶, so the ratio is parameter independent.

### 2.2 The centro-affine clock

On an interval where D≠0, choose the real signed cube-root clock

```math
\frac{ds}{dt}=D(t)^{1/3},\qquad\det(X,X_s,X_{ss})=1.
```

This is **centro-affine arclength**, not Euclidean arclength, not generally u=ln(x/c). The orientation-reversing case is handled by the signed real cube root.

## 3. Exact SL(3,R) companion frame and first-order condition [D,V]

Differentiate det(X,X_s,X_ss)=1 to obtain det(X,X_s,X_sss)=0. Thus for unique α(s),β(s),

```math
X_{sss}=\alpha(s)X+\beta(s)X_s.
```

Taking determinants gives

```math
\alpha(s)=\det(X_s,X_{ss},X_{sss})=\mathcal T_X,\qquad \beta(s)=-\det(X,X_{ss},X_{sss}).
```

**Theorem 3.1 [D,V] (the precise first-order Tzitzéica frame).** The curve condition τ/d²=α₀≠0 is equivalent, after centro-affine arclength normalization, to

```math
X_{sss}=\alpha_0 X+\beta(s)X_s,\qquad \alpha_0\in\mathbb R\setminus\{0\}.
```

Writing F=(X,X_s,X_ss) gives the trace-zero first-order matrix connection

```math
F_s=F A_3,\qquad A_3=\begin{pmatrix}0&0&\alpha_0\\1&0&\beta(s)\\0&1&0\end{pmatrix},\qquad F\in\mathrm{SL}(3,\mathbb R).
```

The free function β shows the Tzitzéica condition is **not a unique scalar second-order equation**. Flatness of A₃ ds on a one-dimensional base is automatic; a 2D Gauss–Codazzi/zero-curvature condition is strictly stronger.

## 4. The projective Wilczyński cubic versus the rank-two Schwarzian [D,K,C]

Every component of the lift satisfies the Laguerre–Forsyth-form third-order scalar ODE

```math
\phi_{sss}-\beta(s)\phi_s-\alpha(s)\phi=0.
```

For an operator D³+pD+q, the classical projective Wilczyński cubic coefficient is, up to a conventional sign, q−p_s/2. In the chosen sign convention set

```math
\mathcal W_3=\alpha-\frac12\beta_s.
```

Under allowable projective reparametrizations it is a cubic differential, not an ordinary scalar Schwarzian of a single affine coordinate. Its vanishing characterizes the local **symmetric-square/conic** reduction.

**Theorem 4.1 [D,K].** The normalized third-order equation is the symmetric square of ψ_ss=Qψ iff

```math
\mathcal W_3=0\quad\Longleftrightarrow\quad\alpha=\frac12\beta_s,\qquad Q=\frac{\beta}{4}.
```

The projected curve then lies on a projective conic (the Veronese image RP¹→RP²). Tzitzéica instead imposes α=constant≠0; generally W₃≠0. The two conditions have a **proper, explicitly testable intersection**.

**Historical caution.** Halphen's classical work on differential/projective invariants is conceptually relevant to Wilczyński and Ovsienko–Tabachnikov. The independently archived **Darboux–Halphen modular system** (H153–H155) is another object; the shared surname does not identify their operators or clocks.

## 5. EXACT Sym²(SL2) lift: the Drach equation in geometric form [D,V,H136]

Let ψ₁,ψ₂ be independent solutions of

```math
\psi_{ss}=Q(s)\psi,\qquad \mathscr W=\psi_1\psi_{2,s}-\psi_{1,s}\psi_2\ne0.
```

Form the quadratic triple

```math
Y=\big(\psi_1^2,\ \psi_1\psi_2,\ \psi_2^2\big)^{\mathsf T}.
```

Direct differentiation gives the **third-order squared-eigenfunction equation**

```math
Y_{sss}=4QY_s+2Q_sY.
```

Its projectivized image lies on the conic Y₁Y₃−Y₂²=0, and the exact 3×3 Wronskian is

```math
\det(Y,Y_s,Y_{ss})=2\mathscr W^3.
```

The derivative Wronskian is

```math
\det(Y_s,Y_{ss},Y_{sss})=4Q_s\mathscr W^3.
```

**Theorem 5.1 [D,V] (Tzitzéica invariant of SL2 quadratic products).**

```math
\frac{\tau_Y}{d_Y^2}=\frac{Q_s}{\mathscr W^3}.
```

After determinant-one normalization X=(2W³)^(-1/3)Y, its equation becomes

```math
X_{sss}=2Q_s X+4Q X_s,\qquad\frac{\tau_X}{d_X^2}=2Q_s.
```

**Corollary 5.2 [D,V].** For a selected fixed SL independent parameter and a nonzero constant Wronskian, the symmetric-square curve is Tzitzéica with NONZERO invariant iff Q_s is a NONZERO constant: Q(s)=as+b, a≠0. Such second-order carriers are affine-linear potential/Airy equations. A generic SL, PT or Lamé carrier has the same rank-three Drach connection but does NOT satisfy this stronger Tzitzéica condition.

**Representation boundary.** The map Sym²:SL(2)→SL(3) has a three-dimensional subgroup image preserving a conic, not all of SL(3). A genuine centro-affine frame with W₃≠0 cannot be identified with this subgroup by the displayed gauge alone.
