---
id: SF-DRAFT-040
title: Weitzenbock and Levi-Civita Friedmann Dictionaries
status: provisional
created: 2026-11-18
proposed_layers: [I, II, III]
depends_on: [SF-I-000, SF-I-010, SF-I-020, SF-DRAFT-010, SF-DRAFT-020, SF-DRAFT-030]
related_claims: [F04, F08, I03, S07, S08, L01, L07, H313, H314, H315, H316, H317, H318, H319, H421, H424, H473, H538]
---

# 040 Weitzenbock and Levi-Civita Friedmann Dictionaries

**Editorial status:** Extensive provisional investigation; no claim of historical novelty or physical realization. Results are distinguished as [D] derived step-by-step, [V] checked independently with symbolic algebra, [K] classical cited theory, [H] historical ledger material with its recorded scope, [C] corrected proposition or counterexample, and [O] open. Consolidation into the main mathematical layers requires separate review.

**Question:** Starting from the canonical Symmetrical Framework reciprocal Ermakov-Pinney envelope, can one give a rigorous dictionary between Levi-Civita curvature and a metric-compatible, flat, torsionful Weitzenbock connection? Does this explain the algebraic kinematic Friedmann constraint and its formal phantom, Rindler or Milne labels without invoking an actual cosmological source?

**Main conclusion:** Yes, in a specified four-dimensional warped metric and a specified spatially flat tetrad. The standard scalar identity between Levi-Civita curvature, teleparallel quadratic torsion and a boundary divergence becomes explicit. On the canonical separatrix the two teleparallel invariants lie on the affine line B = T + 3r² and the chosen warped metric has constant scalar curvature 3r², though it is not an Einstein metric. The connection dictionary is geometric; no modified-gravity field equations, healthy phantom matter or universal Rindler correction follows from it.

**Sources checked:** Current main-branch reference SF-I-000, SF-I-010, SF-I-020, and drafts SF-DRAFT-010, SF-DRAFT-020, SF-DRAFT-030. The uploaded symmetrical-framework-update-2026-11-18-bu.zip includes 04-follow-ups/friedmann-reciprocal-envelope.md, 02-essays/kinematic-friedmann/README.md, verification/friedmann.py, historical foundational-paper-draft-v0.3.md, 00-meta/CLAIMS.md and PROOF-STATUS.md. In the ZIP, H313–H319 summarize 47 tagged checks, with exact derivations, numerical tests, classical citations and unexamined items explicitly distinguished. The attached Pasted text(20261118-170932).txt is an agenda to audit, not independent mathematical evidence. External references are given at the end.

## 1. Domains and the distinction between kinematic and dynamical equations

Throughout the foundational calculation fix $`x,c,r,\mu>0`$ and the logarithmic coordinate

```math
u=\ln(x/c),\qquad x=ce^u,\qquad y(u)=2xf(x).
```

On the positive cubic separatrix,

```math
y=\mu^{-1/2}\mathrm{sech}(ru),\qquad y_{uu}=r^2y-2\mu r^2y^3.
```

The original problem is an autonomous ODE on the logarithmic line. In this investigation the very same $`u`$ is *optionally assigned* the role of proper time in a chosen four-dimensional warped-product metric. This adds geometrical data; it is not a claim that the original function constructed a physical cosmology. A dot denotes differentiation in $`u`$ after making that choice.

The mathematical objects of the dictionary are: (i) scalar first integrals and reciprocal envelopes, (ii) a metric $`g`$, (iii) its torsion-free Levi-Civita connection, (iv) a selected tetrad and metric-compatible flat Weitzenbock connection, (v) a boundary divergence and the resulting scalar curvature identity. An Einstein or modified-teleparallel field equation requires an additional *action, matter and boundary* choice.

Use signature $`(-,+,+,+)`$. Write $`\mathring{\mathcal R}`$ for the Levi-Civita scalar curvature and $`\mathbb T`$ for the torsion scalar; do not confuse the latter with the original project's exponential coordinate $`T=e^{ru}`$. Let $`K`$ be a three-dimensional spatial sectional curvature and $`\delta_G`$ the Gram invariant defined below. They are independent unless an identification is declared.

## 2. The canonical reciprocal Ermakov-Pinney solution [D,V,H313]

On zero energy, put $`J=1/y`$, $`a=\sqrt J`$. The positive centered branch is

```math
J=\sqrt{\mu}\cosh(ru),\qquad a=\mu^{1/4}\sqrt{\cosh(ru)}.
```

The backbone conservation identity and the logarithmic rate are

```math
J_{uu}=r^2J,\qquad J^2-J_u^2/r^2=\mu,\qquad H=\dot a/a=J_u/(2J)=r\tanh(ru)/2.
```

**Proposition 2.1.** The amplitude and its logarithmic rate satisfy

```math
a_{uu}=\frac{r^2}{4}a+\frac{\mu r^2}{4a^3}.
```

```math
H^2=\frac{r^2}{4}\left(1-\frac{\mu}{a^4}\right),\qquad \dot H=\frac{r^2}{2}-2H^2=\frac{\mu r^2}{2a^4}.
```

**Proof, step by step.**

1. From $`a^2=J`$, obtain $`a_u=J_u/(2a)`$ and $`a_{uu}=J_{uu}/(2a)-J_u^2/(4a^3)`$.
2. Substituting the two backbone identities gives the Ermakov-Pinney equation.
3. Dividing $`a_u^2=J_u^2/(4J)`$ by $`a^2=J`$ gives the first-order constraint.
4. Differentiating $`H=J_u/(2J)`$ gives $`\dot H=r^2/2-2H^2`$ without dividing by $`H`$, so the equation remains valid at the turning point.

The corresponding warped-profile bounce is regular: $`a_{\min}=\mu^{1/4}`$ at $`u=0`$, $`H(0)=0`$ and $`\dot H(0)=r^2/2`$. The words Friedmann and Hubble here refer to this differential-algebraic identity alone.

## 3. Shifted Gram envelopes and finite energy [D,V,H313]

Let $`A,B,C`$ be real constants and define the **zero-energy quadratic envelope**

```math
J_0=Ae^{ru}+2C+Be^{-ru},\qquad \delta_G=4(AB-C^2).
```

The source calls this invariant kappa; $`\delta_G`$ avoids confusion with spatial curvature. On any interval $`J_0>0`$, define $`a=\sqrt{J_0}`$.

Differentiation and the difference of squares yield

```math
J_{0,uu}=r^2(J_0-2C),\qquad J_{0,u}^2=r^2(J_0^2-4CJ_0-\delta_G).
```

Consequently,

```math
a_{uu}=\frac{r^2}{4}a+\frac{\delta_G r^2}{4a^3},\qquad H^2=\frac{r^2}{4}-\frac{Cr^2}{a^2}-\frac{\delta_G r^2}{4a^4}.
```

When $`C=0`$ and $`\delta_G=4AB=\mu`$, this is the reciprocal of the original cubic Master separatrix. When $`C\ne0`$, the reciprocal generally solves a **shifted quadratic-cubic nonlinear equation**, not the unshifted Master equation. In particular $`C`$ is not an extra force in the Ermakov-Pinney equation: it becomes an energy-like integration constant.

The historical H313 extension instead specifies the more general nonlinear first integral

```math
y_u^2=\varepsilon+r^2y^2-4Cr^2y^3-\delta_G r^2y^4.
```

For $`\varepsilon\ne0`$, $`J=1/y`$ does **not** remain the elementary exponential $`J_0`$. It satisfies

```math
J_u^2=\varepsilon J^4+r^2J^2-4Cr^2J-\delta_G r^2,\qquad J_{uu}=r^2(J-2C)+2\varepsilon J^3.
```

With $`a=\sqrt J`$ the reciprocal equation and first integral are

```math
a_{uu}=\frac{r^2}{4}a+\frac{\delta_G r^2}{4a^3}+\frac{3\varepsilon}{4}a^5.
```

```math
a_u^2=\frac{r^2}{4}a^2-Cr^2-\frac{\delta_G r^2}{4a^2}+\frac{\varepsilon}{4}a^6.
```

Therefore the complete kinematic constraint is

```math
H^2=\frac{r^2}{4}-\frac{Cr^2}{a^2}-\frac{\delta_G r^2}{4a^4}+\frac{\varepsilon}{4}a^4.
```

Differentiating with the independent second-order equation to extend through turning points yields

```math
\dot H=\frac{Cr^2}{a^2}+\frac{\delta_G r^2}{2a^4}+\frac{\varepsilon}{2}a^4,\qquad\frac{\ddot a}{a}=\frac{r^2}{4}+\frac{\delta_G r^2}{4a^4}+\frac{3\varepsilon}{4}a^4.
```

This is an exact, nonlinear change-of-variable dictionary. The finite-energy term and the shift $`C`$ are independent data. The transformation is not automatically canonical symplectic; the archived H313 calculation supplies a conformally symplectic multiplier.

## 4. A separate warped-product metric [K,D]

Choose a Lorentzian metric, not implied by the original one-dimensional ODE:

```math
g_4=-du^2+a(u)^2h_K.
```

Here $`h_K`$ is a Riemannian three-metric of constant sectional curvature $`K`$. An optional historical identification is $`K=Cr^2`$, so the $`-Cr^2/a^2`$ term becomes the spatial-curvature term of the usual Friedmann notation. This is a *metric choice*, not an identity determined by an ODE.

For spatially flat sections $`K=0`$, in local Cartesian coordinates $`q^i`$ write

```math
g_4=-du^2+a^2\sum_{i=1}^3(dq^i)^2,\qquad \vartheta^0=du,\qquad\vartheta^i=a\,dq^i.
```

The coframe is orthonormal for $`\eta=\mathrm{diag}(-1,1,1,1)`$ and has dual $`e_0=\partial_u`$, $`e_i=a^{-1}\partial_{q^i}`$. This is a **special tetrad**, rather than the unique frame selected by the metric.

## 5. Levi-Civita and hypersurface Gauss-Codazzi [D,V,K]

For the flat warped metric, the nonzero Levi-Civita Christoffel coefficients are

```math
\mathring\Gamma^0{}_{ij}=a\dot a\,\delta_{ij}=Hg_{ij},\qquad\mathring\Gamma^i{}_{0j}=\mathring\Gamma^i{}_{j0}=H\delta^i{}_j.
```

The Ricci tensor and scalar curvature are

```math
\mathring R_{00}=-3(\dot H+H^2),\qquad\mathring R_{ij}=(\dot H+3H^2)g_{ij},\qquad\mathring{\mathcal R}_0=6(\dot H+2H^2).
```

The corresponding Einstein tensor is

```math
\mathring G_{00}=3H^2,\qquad\mathring G_{ij}=-(2\dot H+3H^2)g_{ij}.
```

**Derivation.** Since $`\partial_0 g_{ij}=2a\dot a\delta_{ij}`$ and the spatial derivatives vanish, the Christoffel formula leaves only the two displayed types. Substitute these into the Ricci definition, use $`\ddot a/a=\dot H+H^2`$, and contract with the inverse metric. This computation uses geometry alone, not $`\mathring G_{\mu\nu}=`$ matter.

For general $`K`$, the Levi-Civita identities become

```math
\mathring{\mathcal R}_K=6(\dot H+2H^2+K/a^2),\qquad \mathring G_{00}=3(H^2+K/a^2).
```

**Gauss-Codazzi interpretation.** On the spatial hypersurfaces $`u=\mathrm{constant}`$, the induced metric $`\gamma_{ij}=a^2h_{K,ij}`$ and the convention $`\mathsf K_{ij}=\tfrac12\partial_u\gamma_{ij}`$ give

```math
\mathsf K_{ij}=H\gamma_{ij},\qquad \mathsf K=3H,\qquad \mathsf K_{ij}\mathsf K^{ij}=3H^2.
```

Homogeneity gives the spatial Codazzi equation $`D_i\mathsf K_{jk}-D_j\mathsf K_{ik}=0`$. The hypersurface Gauss constraint is the geometric identity

```math
2\mathring G_{00}={}^{(3)}\mathcal R+\mathsf K^2-\mathsf K_{ij}\mathsf K^{ij}=6(K/a^2+H^2),\qquad {}^{(3)}\mathcal R=6K/a^2.
```

The quadratic form $`\mathsf K^2-\mathsf K_{ij}\mathsf K^{ij}=6H^2`$ will reappear as the torsion scalar in one explicitly specified Weitzenbock gauge. This is the first exact bridge between the hypersurface and teleparallel dictionaries.

## 6. The preferred Weitzenbock connection on the same metric [D,V]

For the flat-slice coframe in §4, choose the Weitzenbock gauge in which the **flat Lorentz spin connection is zero** and the orthonormal frame is parallel for a new connection $`\widetilde\nabla`$. Then

```math
\widetilde\nabla e_A=0,\qquad \widetilde R^A{}_B=0,\qquad \widetilde\nabla g_4=0.
```

With coordinate convention $`\widetilde\nabla_{\partial_\mu}\partial_\nu=\widetilde\Gamma^\lambda{}_{\mu\nu}\partial_\lambda`$,

```math
\widetilde\Gamma^\lambda{}_{\mu\nu}=e_A{}^\lambda\partial_\mu\vartheta^A{}_\nu,\qquad \widetilde\Gamma^i{}_{0j}=H\delta^i{}_j.
```

All other components vanish. The torsion tensor with explicitly fixed sign convention is

```math
\mathcal T^\lambda{}_{\mu\nu}=\widetilde\Gamma^\lambda{}_{\mu\nu}-\widetilde\Gamma^\lambda{}_{\nu\mu},\qquad\mathcal T^i{}_{0j}=H\delta^i{}_j,\qquad\mathcal T^i{}_{j0}=-H\delta^i{}_j.
```

In exterior-form language the same result is

```math
\mathcal T^0=0,\qquad\mathcal T^i=d\vartheta^i=H\,\vartheta^0\wedge\vartheta^i.
```

**Proof of flatness and metric compatibility.** The frame is everywhere orthonormal and declared parallel, so the connection preserves $`\eta_{AB}`$ and hence the metric. Its matrix coefficients vanish in that frame, so curvature vanishes. It does *not* follow that the intrinsic Levi-Civita curvature vanishes, because $`\widetilde\nabla\ne\mathring\nabla`$.

The connection difference (the contorsion tensor in this convention) is

```math
\mathsf C^\lambda{}_{\mu\nu}=\widetilde\Gamma^\lambda{}_{\mu\nu}-\mathring\Gamma^\lambda{}_{\mu\nu},\qquad\mathsf C^0{}_{ij}=-a\dot a\,\delta_{ij},\qquad\mathsf C^i{}_{j0}=-H\delta^i{}_j.
```

Other independent components of $`\mathsf C`$ vanish. This gives the exact relation between covariant accelerations:

```math
\nabla^{LC}_{\dot\gamma}\dot\gamma=0\quad\Longleftrightarrow\quad\widetilde\nabla_{\dot\gamma}\dot\gamma=\mathsf C(\dot\gamma,\dot\gamma).
```

The antisymmetric torsion alone cannot be used in place of $`\mathsf C`$ because $`\mathcal T^\lambda{}_{\mu\nu}\dot x^\mu\dot x^\nu=0`$ identically. This corrects a proposed torsion-force formula in the supplied suggestion.

**Gauss-Codazzi link:** In this special flat homogeneous frame,

```math
\mathcal T^i{}_{0j}=\mathsf K^i{}_j=H\delta^i{}_j.
```

It is a slice- and frame-dependent component equality, not a statement that any Weitzenbock torsion tensor equals a hypersurface shape operator.

## 7. The quadratic torsion scalar is exactly six times H squared [D,V]

Define the torsion-trace vector by

```math
v_\mu=\mathcal T^\nu{}_{\nu\mu}.
```

For the preferred flat-slice tetrad,

```math
v_0=-3H,\qquad v_i=0,\qquad v^0=3H.
```

Choose the following quadratic torsion scalar, with our signature $`(-,+,+,+)`$:

```math
\mathbb T=\frac14\mathcal T_{\rho\mu\nu}\mathcal T^{\rho\mu\nu}+\frac12\mathcal T_{\rho\mu\nu}\mathcal T^{\nu\mu\rho}-v_\rho v^\rho.
```

**Theorem 7.1 [D,V].** With these conventions and this tetrad,

```math
\mathbb T=6H^2=\mathsf K^2-\mathsf K_{ij}\mathsf K^{ij}=2\mathring G_{00}.
```

**Proof by the three tensor contractions.** The components $`\mathcal T^i{}_{0j}=H\delta^i{}_j`$, their antisymmetric partners and the trace above give

```math
\frac14\mathcal T_{\rho\mu\nu}\mathcal T^{\rho\mu\nu}=-\frac32H^2,\qquad\frac12\mathcal T_{\rho\mu\nu}\mathcal T^{\nu\mu\rho}=-\frac32H^2,\qquad v_\rho v^\rho=-9H^2.
```

Subtracting the last term yields $`\mathbb T=-3H^2+9H^2=6H^2`$. The hypersurface equality is exactly §5. The equality to $`2\mathring G_{00}`$ **requires spatial flatness**; for $`K\ne0`$, the extra $`3K/a^2`$ is present in $`\mathring G_{00}`$.

The literature also contains the convention $`T_{\rm alt}=-6H^2`$. The sign of the torsion scalar, the sign of the Ricci scalar and the boundary identity must be transformed *together*, not copied individually from incompatible conventions. The present calculation agrees with the convention used in the HTML sources listed at the end.

## 8. Levi-Civita curvature equals boundary divergence minus torsion [K,D,V]

Expanding the curvature of $`\widetilde\nabla=\mathring\nabla+\mathsf C`$ and using $`\widetilde R=0`$ yields the standard teleparallel contraction identity

```math
\mathring{\mathcal R}=-\mathbb T+\mathbb B,\qquad\mathbb B=2\mathring\nabla_\mu v^\mu.
```

The boundary term is an exact divergence:

```math
\mathbb B=\frac2{\sqrt{-g_4}}\partial_\mu(\sqrt{-g_4}\,v^\mu).
```

Since $`\sqrt{-g_4}=a^3`$ per unit spatial coordinate volume and $`v^0=3H`$,

```math
\mathbb B=\frac2{a^3}\frac d{du}(3a^3H)=6(\dot H+3H^2).
```

Subtract the scalar from §7:

```math
\mathbb B-\mathbb T=6(\dot H+3H^2)-6H^2=6(\dot H+2H^2)=\mathring{\mathcal R}_0.
```

The two connections therefore give **the same metric's invariants in different differential variables**, without introducing any field equations.

### 8.1 A complete minisuperspace total-derivative proof

Write $`\sqrt{-g_4}=a^3`$ in the homogeneous Cartesian chart. Since $`\dot H=\ddot a/a-H^2`$,

```math
a^3\mathring{\mathcal R}=6(a^2\ddot a+a\dot a^2).
```

Now integrate the exact derivative $`d(a^2\dot a)/du`$ algebraically:

```math
6(a^2\ddot a+a\dot a^2)=6\frac d{du}(a^2\dot a)-6a\dot a^2.
```

But $`6a\dot a^2=a^3\mathbb T`$, so

```math
a^3\mathring{\mathcal R}=-a^3\mathbb T+\frac d{du}(6a^2\dot a),\qquad a^3\mathbb B=\frac d{du}(6a^2\dot a).
```

This is the exact local source of the action-level boundary equivalence of **linear** curvature and torsion Lagrangians. Equivalence of variational problems also requires appropriate matching boundary terms and boundary conditions. No nonlinear function $`f(\mathbb T)`$ can be replaced by $`f(\mathring{\mathcal R})`$ simply because their arguments differ by a divergence.

### 8.2 The curved-slice obstruction

The Levi-Civita identities of §5 remain valid for $`K\ne0`$, especially

```math
\mathring{\mathcal R}_K=6(\dot H+2H^2+K/a^2).
```

But one cannot simply paste the **flat** tetrad formulas $`\mathbb T=6H^2`$, $`\mathbb B=6(\dot H+3H^2)`$ into this expression. The coframe on a curved spatial slice has spatial structure coefficients and may require a nonzero flat inertial spin connection for an admissible covariant teleparallel representation. Constructing $`\mathbb T_K`$ and $`\mathbb B_K`$ consistently is [O1], not a theorem obtained from the Cartesian tetrad.

## 9. General reciprocal energy in the two flat-slice invariants [D,V,H313,H318]

Insert the exact general constraint and derivative from §3:

```math
H^2=\frac{r^2}{4}-\frac{Cr^2}{a^2}-\frac{\delta_G r^2}{4a^4}+\frac{\varepsilon}{4}a^4,\qquad\dot H=\frac{Cr^2}{a^2}+\frac{\delta_G r^2}{2a^4}+\frac{\varepsilon}{2}a^4.
```

The preferred flat-slice Weitzenbock scalar is

```math
\mathbb T=\frac{3r^2}{2}-\frac{6Cr^2}{a^2}-\frac{3\delta_G r^2}{2a^4}+\frac{3\varepsilon}{2}a^4.
```

Its boundary divergence is

```math
\mathbb B=\frac{9r^2}{2}-\frac{12Cr^2}{a^2}-\frac{3\delta_G r^2}{2a^4}+\frac{15\varepsilon}{2}a^4.
```

Subtracting gives an exact Levi-Civita scalar formula:

```math
\mathring{\mathcal R}_0=\mathbb B-\mathbb T=3r^2-\frac{6Cr^2}{a^2}+6\varepsilon a^4.
```

**Verification.** Insert the two expressions for $`H^2,\dot H`$ into $`6H^2`$, $`6(\dot H+3H^2)`$ and $`6(\dot H+2H^2)`$, and collect coefficients of $`a^0,a^{-2},a^{-4},a^4`$. The $`a^{-4}`$ coefficient cancels in the scalar curvature. This holds for any real regular branch on which the reciprocal $`a`$ is defined.

If one instead chooses the **different**, spatially curved warped metric with $`K=Cr^2`$, its Levi-Civita scalar is

```math
\mathring{\mathcal R}_K=6(\dot H+2H^2+K/a^2)=3r^2+6\varepsilon a^4.
```

This is precisely the optional warped-curvature formula documented under H318. It does **not** imply the same formula for the flat-slice torsion scalar when $`K\ne0`$: the two selected four-metrics are different. The Gram parameter $`\delta_G`$ cancels from both Levi-Civita scalar traces, but remains present in the full Ricci tensor.

## 10. The canonical separatrix: an affine invariant plane [D,V]

Select the original positive branch $`C=0`$, $`\delta_G=\mu`$, $`\varepsilon=0`$. With

```math
S=\mathrm{sech}(ru),\qquad W=\tanh(ru),\qquad a=\mu^{1/4}\sqrt{\cosh(ru)},\qquad H=\frac r2 W,
```

we have

```math
\dot H=\frac{r^2}{2}S^2,\qquad \mathbb T=\frac{3r^2}{2}W^2,\qquad \mathbb B=3r^2+\frac{3r^2}{2}W^2.
```

**Theorem 10.1 [D,V].** On this explicit warped metric and preferred tetrad,

```math
\mathbb B=\mathbb T+3r^2,\qquad\mathring{\mathcal R}=3r^2.
```

**Proof.** Substitute the last formulas. The difference is $`3r^2`$ by $`S^2+W^2=1`$. This is the same circle invariant that originally characterizes the canonical separatrix. The geometry now makes the circle identity into an affine relation between torsion and boundary scalars.

**Nonuniqueness warning:** $`\mathring{\mathcal R}=3r^2`$ does **not** make this metric Einstein or constant-sectional-curvature. The trace-free Ricci tensor is nonzero, as calculated in §11. No identification of the metric with a physical de Sitter solution has been made.

### 10.1 Torsion forgets the expansion sign

Because $`\mathbb T=6H^2`$, it determines $`|H|`$ but not the sign of $`H`$. The separatrix passes smoothly through $`H(0)=0`$ with $`\dot H(0)=r^2/2>0`$, so the torsion scalar alone loses the distinction between contracting and expanding halves.

From the canonical Riccati equation,

```math
\dot H=\frac{r^2}{2}-2H^2=\frac{r^2}{2}-\frac{\mathbb T}{3}.
```

Hence

```math
\dot{\mathbb T}=2H(3r^2-2\mathbb T),\qquad(\dot{\mathbb T})^2=\frac23\mathbb T(3r^2-2\mathbb T)^2.
```

The squared scalar equation has two time orientations; neither the pointwise torsion scalar nor the curvature-boundary identity restores the lost sign without a chosen branch, clock and tetrad.

## 11. Constant scalar curvature does not mean constant sectional curvature [D,V]

For any spatially flat warped metric, the mixed-index Ricci eigenvalues are

```math
\mathring R^0{}_0=3(\dot H+H^2),\qquad \mathring R^i{}_i=\dot H+3H^2.
```

Define the trace-free Ricci tensor $`\mathring S^\mu{}_\nu=\mathring R^\mu{}_\nu-\delta^\mu{}_\nu\mathring{\mathcal R}/4`$. Its eigenvalues are

```math
\mathring S^0{}_0=\frac32\dot H,\qquad\mathring S^i{}_i=-\frac12\dot H.
```

On the canonical separatrix, $`\dot H=r^2S^2/2`$. Therefore

```math
\mathring S^0{}_0=\frac{3r^2}{4}S^2,\qquad\mathring S^i{}_i=-\frac{r^2}{4}S^2.
```

Their invariant square is

```math
\mathring S_{\mu\nu}\mathring S^{\mu\nu}=3\dot H^2=\frac{3r^4}{4}S^4.
```

At every finite $`u`$, this is strictly positive, although $`\mathring{\mathcal R}=3r^2`$ is constant. Hence the four-metric is **not Einstein** at any finite $`u`$ and does not have constant four-dimensional sectional curvature. This prevents an unjustified identification with a de Sitter metric merely because the Ricci scalar is constant.

The FLRW Weyl tensor vanishes. Its Kretschmann invariant, derived from the two independent sectional-curvature combinations, is

```math
\mathcal K_4=12[(\dot H+H^2)^2+H^4]=\frac{3r^4}{2}(1+S^4).
```

The curvature is finite at the bounce $`u=0`$. In fact the flat-slice canonical geometry has $`\mathbb T(0)=0`$, $`\mathbb B(0)=3r^2`$, $`\mathring{\mathcal R}(0)=3r^2`$. Vanishing of the selected torsion scalar at one instant says neither that the metric is locally flat nor that the full torsion tensor vanishes throughout a neighborhood.

## 12. Connection with the two-dimensional catenoid torsion geometry [D,V,H421,H424]

Draft SF-DRAFT-030 derives a **different** Weitzenbock connection on the intrinsic two-dimensional catenoid cylinder, with metric

```math
I_{\mathrm{cat}}=R^2(du^2+dv^2),\qquad R=\cosh(ru).
```

Its frame-dependent torsion coefficient and Gaussian curvature are

```math
t_2=\frac{R_u}{R^2}=rSW,\qquad K_{\mathrm{cat}}=-e_1(t_2)-t_2^2=-r^2S^4,\qquad e_1=R^{-1}\partial_u.
```

In the **separately chosen four-dimensional flat warped** realization, the very same scalar profile has

```math
H=\frac r2W,\qquad \mathbb T_4=6H^2=\frac{3r^2}{2}W^2.
```

The two geometries are not isometric (nor even of equal dimension), but the common scalar coordinates imply exact cross-realization identities:

```math
t_2=2SH,\qquad K_{\mathrm{cat}}=-r^2\left(1-\frac{2\mathbb T_4}{3r^2}\right)^2.
```

Moreover,

```math
\mathring S_{\mu\nu}\mathring S^{\mu\nu}=-\frac{3r^2}{4}K_{\mathrm{cat}}.
```

**Proof, step by step.**

1. From $`\mathbb T_4=(3r^2/2)W^2`$, obtain $`S^2=1-W^2=1-2\mathbb T_4/(3r^2)`$.
2. Insert that expression in $`K_{\mathrm{cat}}=-r^2S^4`$.
3. Insert $`K_{\mathrm{cat}}=-r^2S^4`$ in the trace-free Ricci square from §11, to obtain the last equality.

These are valid equalities of **selected functions evaluated at the same logarithmic coordinate**, not pullback identities between the two manifolds without a map. They show how the same differential-algebraic backbone can organize multiple geometries while preserving their distinct definitions.

## 13. An optional effective-fluid dictionary and the historical “phantom” label [D,H318]

A Friedmann-type equation becomes a matter equation only after imposing a source field equation. Without doing so, introduce a positive *bookkeeping* constant $`\mathfrak g`$ and define formal effective functions using the Einstein tensor of the optional **curved-slice** metric with $`K=Cr^2`$:

```math
\mathfrak g\,\rho_{\rm eff}=3(H^2+K/a^2),\qquad\mathfrak g\,p_{\rm eff}=-(2\dot H+3H^2+K/a^2).
```

This is a pair of **definitions**. Differentiating them gives the formal continuity equation

```math
\dot\rho_{\rm eff}+3H(\rho_{\rm eff}+p_{\rm eff})=0.
```

**Proof.** Compute $`\mathfrak g\dot\rho_{\rm eff}=6H\dot H-6KH/a^2`$, while $`3H\mathfrak g(\rho_{\rm eff}+p_{\rm eff})=-6H\dot H+6KH/a^2`$. They cancel for every smooth positive $`a`$.

Insert the source's complete reciprocal-envelope constraint to obtain

```math
\mathfrak g\,\rho_{\rm eff}=\frac{3r^2}{4}-\frac{3\delta_G r^2}{4a^4}+\frac{3\varepsilon}{4}a^4.
```

```math
\mathfrak g\,p_{\rm eff}=-\frac{3r^2}{4}-\frac{\delta_G r^2}{4a^4}-\frac{7\varepsilon}{4}a^4.
```

Therefore,

```math
\mathfrak g(\rho_{\rm eff}+p_{\rm eff})=-\frac{\delta_G r^2}{a^4}-\varepsilon a^4=-2(\dot H-K/a^2).
```

The component proportional to $`a^{-4}`$ has the **formal** exponent $`w=1/3`$ but a negative density coefficient when $`\delta_G>0`$. The $`\varepsilon a^4`$ component has formal exponent $`w=-7/3`$ when it is assigned the usual conserved-fluid power law. No matter fields have been deduced by these exponent names.

### 13.1 Phantom behavior on the zero-energy separatrix

For the unshifted case $`C=0`$, $`\delta_G=\mu>0`$, $`\varepsilon=0`$ with flat slices,

```math
\mathfrak g\rho_{\rm eff}=\frac{3r^2}{4}W^2,\qquad\mathfrak g p_{\rm eff}=-\frac{r^2}{4}(3+S^2).
```

Where $`H\ne0`$, their quotient is

```math
w_{\rm eff}=-1-\frac{4S^2}{3W^2}=-1-\frac{4}{3\sinh^2(ru)}.
```

This lies below $`-1`$ on either side of the bounce and tends to $`-1`$ as $`u\to\pm\infty`$. At $`u=0`$ it is **undefined**, since $`\rho_{\rm eff}=0`$ and $`p_{\rm eff}=-r^2/\mathfrak g`$. This is not a paradox: the quotient ceases to be a valid variable at the zero of its denominator.

The regular scale function $`a=\mu^{1/4}\sqrt{\cosh(ru)}`$ has no finite-time blow-up and the warped metric has finite curvature there. An effective ratio below $`-1`$ **does not imply** a wrong-sign fundamental scalar, a ghost, a physical Big Rip, or any observational conclusion.

### 13.2 An explicit *optional* negative-kinetic scalar reconstruction

If one deliberately chooses $`\mathfrak g=1`$ and a scalar-field ansatz with formal negative kinetic sign,

```math
\rho_\phi=-\frac12\dot\phi^2+V,\qquad p_\phi=-\frac12\dot\phi^2-V,
```

then the canonical separatrix can be reproduced by

```math
\dot\phi^2=2\dot H=r^2S^2,\qquad\phi(u)=\mathrm{gd}(ru)+\phi_0.
```

With $`W=\sin(\phi-\phi_0)`$, the corresponding potential is

```math
V=3H^2+\dot H=\frac{r^2}{4}[2+\sin^2(\phi-\phi_0)].
```

Direct differentiation checks the formally reconstructed field equation

```math
\ddot\phi+3H\dot\phi=\partial_\phi V.
```

This is the Gudermannian reconstruction recorded in the historical H318 investigation. It is an **additional matter ansatz**, not a result of the Levi-Civita/Weitzenbock scalar dictionary alone. Its physical viability is neither established nor presumed.

### 13.3 The general-level exponent ladder and its clock

The historical reciprocal-envelope hierarchy has a term proportional to $`e_q a^{4q}`$ for $`q=(l-1)/2>0`$. Within **this particular logarithmic-time warped-metric and continuity** convention, a component $`\rho\propto a^\beta`$ has

```math
w_\beta=-1-\frac{\beta}{3}.
```

Thus

```math
\beta_q=4q=2(l-1),\qquad w_l=-1-\frac{4q}{3}=-\frac{2l+1}{3}.
```

This is not the framework's other, conformal-time Friedmann dictionary (different time and amplitude variables). The two power-law assignments must not be identified without an explicit clock transformation.

### 13.4 Positive energy and a finite-time singular branch

At large $`a`$, if $`\varepsilon>0`$ and the solution is expanding, the leading first integral is $`\dot a\sim\sqrt\varepsilon a^3/2`$. Integration gives

```math
a(u)\sim\varepsilon^{-1/4}(u_*-u)^{-1/2},\qquad \mathring{\mathcal R}_K\sim6(u_*-u)^{-2}.
```

This is the actual source of the archived label Big Rip in the **optional warped geometry**. The singularity is absent when $`\varepsilon=0`$. The term's sign and the chosen real branch are indispensable.

## 14. The Milne limit is a separate geometric construction [D,V,H318]

The ZIP records a singular Gram-parameter limit that is easily confused with Rindler. Use the historical shift parameter $`k=2C/\sqrt{\mu}`$. Choose $`k=-1`$ and scale $`\sqrt\mu=2/r^2`$. Then

```math
C=-r^{-2},\qquad \delta_G=0,\qquad J=\frac{2}{r^2}[\cosh(ru)-1]=\frac4{r^2}\sinh^2(ru/2).
```

On the branch $`u>0`$,

```math
a=\sqrt J=\frac2r\sinh(ru/2),\qquad K=Cr^2=-1.
```

The logarithmic rate obeys

```math
H^2=\frac{r^2}{4}+\frac1{a^2},\qquad\dot H=-\frac1{a^2}.
```

Both independent sectional-curvature combinations of the **curved-slice warped metric** agree:

```math
\dot H+H^2=\frac{r^2}{4},\qquad H^2+\frac{K}{a^2}=\frac{r^2}{4}.
```

Thus for finite $`r>0`$ the metric is locally a positive constant-sectional-curvature four-dimensional space form in an open slicing, with $`\mathring{\mathcal R}=3r^2`$. Letting $`r\to0^+`$ at fixed $`u>0`$ gives

```math
a(u)\to u,\qquad g_4\to-du^2+u^2h_{-1}.
```

This is **Milne slicing** of a flat Minkowski region, not the same coordinate chart as Rindler. The limit requires a singular correlated scaling of Gram parameters and does not produce another finite-norm original Master profile. Spatial curvature $`K=-1`$ also means the flat-Cartesian torsion formula $`\mathbb T=6H^2`$ must **not** be transferred without a new covariant coframe/spin calculation.

## 15. Rindler as a negative control [D,V,C]

Let $`\alpha>0`$ and consider the Rindler wedge metric

```math
g_R=-\alpha^2\xi^2d\eta^2+d\xi^2+dy^2+dz^2,\qquad\xi>0.
```

The coordinate transformation

```math
T_M=\xi\sinh(\alpha\eta),\qquad X_M=\xi\cosh(\alpha\eta)
```

shows that this is exactly flat Minkowski space in accelerated coordinates. Its Levi-Civita Riemann tensor vanishes.

Choose an accelerated orthonormal coframe with **zero** spin connection,

```math
\vartheta^0=\alpha\xi\,d\eta,\qquad\vartheta^1=d\xi,\qquad\vartheta^2=dy,\qquad\vartheta^3=dz.
```

The corresponding Weitzenbock torsion is nonzero:

```math
\mathcal T^0=d\vartheta^0=\alpha\,d\xi\wedge d\eta,\qquad\mathcal T^\eta{}_{\xi\eta}=\xi^{-1}.
```

Nevertheless the quadratic torsion scalar vanishes exactly. Its three contractions, in the same convention as §7, are

```math
\frac14\mathcal T_{\rho\mu\nu}\mathcal T^{\rho\mu\nu}=\frac1{2\xi^2},\qquad \frac12\mathcal T_{\rho\mu\nu}\mathcal T^{\nu\mu\rho}=\frac1{2\xi^2},\qquad v_\rho v^\rho=\xi^{-2}.
```

Therefore

```math
\mathbb T_R=0,\qquad\mathbb B_R=0,\qquad\mathring{\mathcal R}_R=0.
```

**Counterexample:** An accelerated coframe can have nonzero torsion components but zero quadratic torsion scalar and zero curvature. One cannot infer a universal linear-$`H`$ term, effective dark energy, or nonzero spacetime curvature merely from Rindler-like acceleration.

A **different, covariantly inertial** choice supplies the flat Lorentz spin connection

```math
\omega^0{}_1=\alpha\,d\eta,\qquad\omega^1{}_0=\alpha\,d\eta.
```

Then

```math
\mathcal T^0=d\vartheta^0+\omega^0{}_1\wedge\vartheta^1=\alpha\,d\xi\wedge d\eta+\alpha\,d\eta\wedge d\xi=0.
```

All remaining torsion components vanish as well, and the spin connection is flat. The two coframe/connection pairs with the same metric are **different teleparallel connections**; holding the coframe fixed while changing the spin connection is not the simultaneous local Lorentz gauge transformation under which the torsion tensor transforms covariantly. This example cleanly separates geometry, inertial frame and torsion gauge.

## 16. Lapse and conformal-time consistency checks [D]

The same warped geometry may be expressed in a conformal coordinate $`\eta`$ defined by $`d\eta=du/a`$. Then

```math
g_4=a(\eta)^2[-d\eta^2+h_K],\qquad \mathcal H_c=\frac{a_\eta}{a}=aH,\qquad H=\frac{a_\eta}{a^2}.
```

For the generalized reciprocal-envelope first integral,

```math
a_\eta^2=a^4H^2=\frac{r^2}{4}a^4-Cr^2a^2-\frac{\delta_G r^2}{4}+\frac{\varepsilon}{4}a^8.
```

At $`\varepsilon=0`$ this is a quartic polynomial in $`a`$ (the elliptic conformal-time curve studied in H315 when nonsingular); at $`\varepsilon\ne0`$ the resulting degree-eight curve is generically of genus three, with the marked clocks and elliptic/hyperelliptic quotients analyzed in the archive. Those are **period problems**, not automatically torsion invariants.

The proper-time teleparallel scalar is

```math
\mathbb T=6H^2=6\frac{a_\eta^2}{a^4},
```

not $`6\mathcal H_c^2`$ unless an additional lapse factor has been properly included. A naive conformal-time substitution would therefore introduce a spurious factor of $`a^2`$. The torsion and scalar-curvature dictionary is coordinate invariant **when the coframe and its lapse are transformed consistently**.

## 17. What is—and is not—an action-dependent “teleparallel Friedmann equation” [K,D,C]

The scalar identity $`\mathring{\mathcal R}=-\mathbb T+\mathbb B`$ is geometric. To obtain a **field equation**, independently choose the action and the source. For example, in the sign convention of §7 consider the formal functional

```math
\mathcal S=\frac1{2\mathfrak g}\int d^4q\,\sqrt{-g}\,F(\mathbb T,\mathbb B)+\mathcal S_m,
```

where $`\mathfrak g>0`$ is a coupling normalization and $`\mathcal S_m`$ is a **separately specified** matter functional. The published flat-FLRW field-equation calculation, with the same sign of the torsion scalar and an admissible tetrad/spin pair, takes the form

```math
\mathfrak g\rho=-3H^2(3F_{\mathbb B}+2F_{\mathbb T})+3H\dot F_{\mathbb B}-3\dot H F_{\mathbb B}+\frac12F.
```

```math
-\mathfrak g p=-(3H^2+\dot H)(3F_{\mathbb B}+2F_{\mathbb T})-2H\dot F_{\mathbb T}+\ddot F_{\mathbb B}+\frac12F.
```

These equations are a **quoted, action-dependent result [K]**, not derived from the original Symmetrical Function. They are included to show exactly what data are missing from a merely kinematic Friedmann identification. Their overall signs and matter conventions must be retained with the action.

### 17.1 The linear action recovers the same Levi-Civita field equations

For the teleparallel equivalent choice $`F=-\mathbb T`$, we have $`F_{\mathbb T}=-1`$, $`F_{\mathbb B}=0`$ and $`\mathbb T=6H^2`$. Substitution in the two quoted equations yields

```math
\mathfrak g\rho=3H^2,\qquad -\mathfrak g p=2\dot H+3H^2.
```

These are exactly the two corresponding flat-slice Levi-Civita Einstein equations. The equality also follows variationally because the linear densities differ by a total divergence (§8).

Thus there **is** a rigorous Levi-Civita–Weitzenbock Friedmann dictionary for this specified linear action, with the same source and boundary hypotheses. It is the classical teleparallel equivalence, not an independent physical prediction of the Symmetrical Framework.

### 17.2 Nonlinear actions require their own dynamics

For a general $`F(\mathbb T,\mathbb B)`$, derivatives $`\dot F_{\mathbb B}`$, $`\ddot F_{\mathbb B}`$ and $`\dot F_{\mathbb T}`$ appear in the field equations. If $`F=f(-\mathbb T+\mathbb B)`$, the action is exactly $`f(\mathring{\mathcal R})`$; that is a special restriction, often involving higher-order equations. General $`F`$ need not be equivalent to an $`f(\mathring{\mathcal R})`$ action, to Einstein theory, or to a theory with a single canonical scalar.

A formal effective tensor obtained by moving extra terms to one side of the field equations is not unique as a physical matter interpretation. In particular, a connection decomposition does **not** prove absence of ghosts, new degrees of freedom, acausality or singularities. Covariance under simultaneous local Lorentz transformations of the tetrad and **flat inertial spin connection** must be distinguished from dynamical health of an action.

## 18. A square-root counterexample to an automatic Rindler H term [D,C]

For the action restricted to $`F(\mathbb T)`$, the quoted first equation reduces to

```math
2\mathfrak g\rho=F(\mathbb T)-2\mathbb T F_{\mathbb T}(\mathbb T),\qquad \mathbb T=6H^2.
```

In the canonical sign convention the homogeneous reconstruction equation is $`F-2\mathbb T F_{\mathbb T}=0`$.

**Theorem 18.1 [D,C].** On any branch $`\mathbb T>0`$, a square-root term belongs to the exact homogeneous kernel:

```math
F_h(\mathbb T)=A\sqrt{\mathbb T},\qquad F_h-2\mathbb T(F_h)_{\mathbb T}=A\sqrt{\mathbb T}-2\mathbb T\frac A{2\sqrt{\mathbb T}}=0.
```

Therefore adding $`A\sqrt{\mathbb T}`$ to this background action does **not automatically** generate a linear $`H`$ correction to the first Friedmann constraint. In the alternate common notation $`\tau=-6H^2`$, the same kernel is $`A\sqrt{-\tau}`$. The suggestion that a square-root torsion term by itself universally produces $`H^2-\alpha H=`$ source is **false in this standard background equation**.

A general inhomogeneous reconstruction can be written as a first-order linear differential equation. If $`G(\mathbb T)=2\mathfrak g\rho(\mathbb T)`$ on a monotone branch,

```math
\frac d{d\mathbb T}\left(\frac{F}{\sqrt{\mathbb T}}\right)=-\frac{G(\mathbb T)}{2\mathbb T^{3/2}}.
```

Its solutions are

```math
F(\mathbb T)=\sqrt{\mathbb T}\left[C_0-\frac12\int^{\mathbb T}\frac{G(s)}{s^{3/2}}\,ds\right].
```

The integration constant multiplies the homogeneous square-root kernel. Moreover, the square root is not differentiable at $`\mathbb T=0`$, which is reached by the canonical bouncing profile. Requiring a smooth action across that point can exclude this ambiguity.

**Branch warning:** Even if $`\mathbb T(u)`$ is known, the sign of $`H`$ is lost, and the matter function $`\rho(\mathbb T)`$ may be multivalued on nonmonotone trajectories. Background reconstruction alone does not determine a unique covariant theory or verify the second field equation and perturbation spectrum.

## 19. All-level separatrix collapse of the teleparallel invariants [D,V,H317,H318]

The archive's general positive level has $`q=(l-1)/2>0`$ and a normalized reciprocal amplitude $`a_q`$. Its normalized first integral can be written

```math
H_q^2=\frac{r^2}{4}\left(1-a_q^{-4}+e_q a_q^{4q}\right),\qquad H_q=\dot a_q/a_q.
```

On nonstationary branches differentiate and extend through ordinary turning points using the second-order equation:

```math
\dot H_q=\frac{r^2}{2}\left(a_q^{-4}+q e_q a_q^{4q}\right).
```

The same **chosen spatially flat warped geometry and tetrad** produces

```math
\mathbb T_q=6H_q^2=\frac{3r^2}{2}\left(1-a_q^{-4}+e_q a_q^{4q}\right).
```

Its Levi-Civita scalar curvature and teleparallel boundary invariant are

```math
\mathring{\mathcal R}_q=6(\dot H_q+2H_q^2)=3r^2[1+(q+1)e_q a_q^{4q}],\qquad \mathbb B_q=\mathbb T_q+\mathring{\mathcal R}_q.
```

This rederives the historical general-level warped scalar formula in the *flat-slice, zero-Gram-shift normalization*, and simultaneously supplies its teleparallel counterpart.

**Theorem 19.1 [D,V] (separatrix collapse).** At the zero-energy separatrix $`e_q=0`$, every real level $`q>0`$ has the same normalized reciprocal envelope

```math
a_q(u)=\sqrt{\cosh(ru)}.
```

Consequently all such levels, when placed into this **same chosen warped metric ansatz**, share the invariant pair

```math
\mathbb T_q=\frac{3r^2}{2}\tanh^2(ru),\qquad \mathbb B_q=\mathbb T_q+3r^2,\qquad\mathring{\mathcal R}_q=3r^2.
```

**Proof.** The normalized separatrix field at level $`q`$ is $`\mathrm{sech}^{q}(ru)`$; raising it to the reciprocal power $`-1/(2q)`$ gives $`\sqrt{\cosh(ru)}`$. Its logarithmic derivative is $`(r/2)\tanh(ru)`$, independent of $`q`$, and substitution in the invariant formulas completes the proof.

**Consequence and limitation:** This four-dimensional geometric realization **cannot distinguish levels from their normalized zero-energy torsion/curvature scalars alone**. The nonlinear level information reappears away from the separatrix through the factor $`(q+1)e_q a_q^{4q}`$ and through the independent algebraic-curve/period data. The collapse is due to a declared normalization and an information-losing reciprocal map; it is not a claim that the underlying distinct level ODEs are identical.

## 20. Rigor audit, limitations and mathematical next steps

The supplied exploratory text includes several statements that are mathematically too strong. Record explicit corrections:

| Proposed claim | Correct mathematical status |
|---|---|
| Every kinematic Friedmann constraint is a Weitzenbock field equation. | A scalar first integral is only kinematic; an action and source are required to obtain field equations. |
| A metric uniquely selects a flat torsionful connection. | False: a Weitzenbock connection requires a chosen tetrad and compatible flat spin connection; global holonomy matters. |
| The scalar identity gives a unique map between arbitrary modified-curvature and modified-torsion theories. | False: linear bulk densities are boundary-equivalent; nonlinear functions differ and carry independent dynamics. |
| $`T=-6H^2`$ can be paired with any quoted $`R=-T+B`$ without changing conventions. | False: scalar-curvature and boundary signs must be transformed together. This draft uses $`\mathbb T=+6H^2`$ and $`\mathring{\mathcal R}=-\mathbb T+\mathbb B`$. |
| A Rindler tetrad's nonzero torsion necessarily gives nonzero torsion scalar or a linear-Hubble correction. | Explicit counterexample: §15 gives nonzero torsion components but $`\mathbb T_R=\mathbb B_R=0`$. |
| A $`\sqrt{|T|}`$ term automatically generates a new background Friedmann term linear in $`H`$. | Explicit counterexample: §18 gives an exact homogeneous-kernel cancellation in the standard first $`F(T)`$ background equation. |
| Apparent phantom exponents prove phantom matter or freedom from ghosts. | They are optional formal power-law bookkeeping; physical conclusions need a matter action and stability analysis. |
| A constant scalar curvature means the metric is a space form. | False on the basic separatrix: §11 derives nonzero trace-free Ricci tensor. |
| Milne and Rindler are the same geometric realization. | Both relate to Minkowski patches but have different natural slicings; the historical Milne profile arises in a singular Gram-limit with $`K=-1`$. |
| The Weitzenbock connection and the Bochner–Weitzenbock identity are identical. | The latter is a separate Hodge/Levi-Civita Laplacian formula, as established in SF-DRAFT-030. |

**Independent verification record [V].** New SymPy work checked: (i) the coordinate torsion contractions $`-3H^2/2,-3H^2/2,-9H^2`$, giving $`\mathbb T=6H^2`$; (ii) $`\dot H`$ and all general Gram/finite-energy invariant formulas; (iii) $`\mathring{\mathcal R}_K=3r^2+6\varepsilon a^4`$ with $`K=Cr^2`$; (iv) separatrix affine identity $`\mathbb B-\mathbb T=3r^2`$; (v) trace-free Ricci square and the catenoid cross-invariant; (vi) Rindler's nonzero torsion components but scalar $`\mathbb T_R=0`$; (vii) square-root homogeneous $`F(T)`$ kernel. Steps are given explicitly above for reproducibility. Source H313–H319 includes additional **numerical, quoted and unexamined** material not promoted here.

**Open problems:**

1. [O1] Construct a compatible flat spin connection/tetrad for $`K=Cr^2\ne0`$ and compute $`\mathbb T_K,\mathbb B_K`$ without importing Cartesian-flat formulas; compare spatial curvature, global frames and holonomy.
2. [O2] Classify flat metric-compatible connections sharing a warped metric, and distinguish tetrad/spin gauge transformations from genuinely different teleparallel connections.
3. [O3] Determine the algebraic curves in the $`(\mathbb T,\mathbb B)`$-plane generated by general $`q`$ at nonzero energy, and investigate branch points, discriminants and recoverability of $`q`$.
4. [O4] Compare complete-domain conditions, Jacobi operators, curvature singularities and spectral endpoints of the reciprocal envelopes with their torsion invariants.
5. [O5] Solve carefully specified variational reconstruction problems for $`F(\mathbb T)`$ or $`F(\mathbb T,\mathbb B)`$ with lapse, source and regularity hypotheses; test nonuniqueness of the background inverse problem.
6. [O6] Relate Milne and Rindler coframes through explicit local coordinate/boost maps while tracking inertial spin connections and the difference between zero curvature and zero torsion.
7. [O7] Compare the two-dimensional catenoid teleparallel frame with the four-dimensional warped frame only through declared maps or matching scalar evaluations; do not infer a dimensional equivalence.

## 21. Historical sources, external references and consolidation route

**Archive and live reference:** The principal archival source is the ZIP's 04-follow-ups/friedmann-reciprocal-envelope.md, specifically §§1–3 and §6, plus verification/friedmann.py. Its H313–H319 records contain 47 individually tagged checks. In H318, terms Milne, phantom, Big Rip and scalar reconstruction are historical algebraic/optional geometric descriptions, **not assertions of physical realization**. The live SF-I-020 fixes the two-exponential/Gram distinction, and drafts 010/020/030 distinguish ambient moving frames, intrinsic surface Weitzenbock geometry, Lorentzian immersions and variational operator domains.

**External references [K] for sign and action conventions:**

- Variational Principles in Teleparallel Gravity Theories, Universe 7 (2021), 114: https://www.mdpi.com/2218-1997/7/5/114 . Tetrads, flat spin connections, torsion and the distinction from nonmetricity.
- f(T, B) Cosmography for High Redshifts, Universe 7 (2021), 441: https://www.mdpi.com/2218-1997/7/11/441 . Flat homogeneous invariants $`\mathbb T=6H^2`$, $`\mathbb B=6(\dot H+3H^2)`$ and $`\mathring{\mathcal R}=-\mathbb T+\mathbb B`$ with consistent convention.
- Dynamical system analysis in teleparallel gravity with boundary term, European Physical Journal C 83 (2023): https://link.springer.com/article/10.1140/epjc/s10052-023-11937-6 . The action-dependent homogeneous $`F(T,B)`$ equations used only in §17.
- Holographic renormalization in teleparallel gravity, European Physical Journal C 77 (2017): https://link.springer.com/article/10.1140/epjc/s10052-017-4621-3 . Covariant inertial spin connections, contorsion, and boundary relations.
- Classical Ermakov-Pinney, Gauss-Codazzi and ADM hypersurface geometry are used with their stated hypotheses; the Friedmann–Pinney connection predates this investigation, as already acknowledged by the historical project archive.

**After audit, proposed destinations:** Layer I: reciprocal envelope, first integrals, energy/Gauss invariants, and normalized $`q`$-family. Layer II: explicit warped geometry, Levi-Civita–Weitzenbock connection dictionary, Gauss-Codazzi slicing, catenoid cross-model invariants, Rindler/Milne geometry and holonomy. Layer III: qualified Friedmann/Ermakov correspondences, optional formal-fluid and action-based $`F(T,B)`$ reconstruction. Layer IV: any physical cosmology, phantom model, horizon or observational interpretation *only if separately supplied with an actual model and evidence*.

**Closing mathematical statement:** The Symmetrical Framework does possess an exact Weitzenbock–Levi-Civita Friedmann dictionary, but it is a **typed geometric correspondence**, not a new universal theory of gravity. Its key identities are the reciprocal-envelope first integral, the induced warped metric, the preferred-frame torsion $`\mathbb T=6H^2`$, the divergence $`\mathbb B=6(\dot H+3H^2)`$, and $`\mathring{\mathcal R}=-\mathbb T+\mathbb B`$. The separatrix makes the invariant locus affine and constant-curvature-scalar; the nonzero-energy and general-level extensions expose the precise defects. These are powerful mathematical organizing results precisely because they require no forced physical interpretation.
