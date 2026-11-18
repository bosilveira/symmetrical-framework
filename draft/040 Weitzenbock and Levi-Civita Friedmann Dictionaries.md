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
