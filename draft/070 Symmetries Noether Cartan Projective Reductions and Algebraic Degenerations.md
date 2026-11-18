---
id: SF-DRAFT-070
title: Symmetries, Noether, Cartan, Projective Reductions, and Algebraic Degenerations
status: provisional
created: 2026-11-18
proposed_layers: [I, II, III, IV]
depends_on: [SF-I-000, SF-I-010, SF-I-020, SF-DRAFT-010, SF-DRAFT-020, SF-DRAFT-030, SF-DRAFT-040, SF-DRAFT-050, SF-DRAFT-060]
related_claims: [F04, F08, S02, S09, H173, H174, H175, H176, H320, H321, H322, H323, H324, H325, H326, H327, H328, H352, H353, H403, H421, H424, H427, H429]
---

# 070 Symmetries, Noether, Cartan, Projective Reductions, and Algebraic Degenerations

**Research status:** Provisional mathematical investigation. This draft does not assert that one mathematical formalism physically realizes another. [D] denotes an explicit derivation, [V] independent symbolic verification, [K] established mathematics, [H] an archived project result retaining its recorded verification level, [C] a correction or counterexample, and [O] an open question. The aim is to identify **typed mathematical maps** rather than infer identities from repeated names, curves or symmetry groups.

**Source provenance:** The user's current attachment, Pasted text(20261118-185303).txt (368 lines), was inspected directly and used as a collection of proposed insights; its assertions were **not presumed verified**. Current GitHub main branch: SF-I-020 and drafts 020, 030, 040, 050, 060, plus the draft index. Historical uploaded ZIP symmetrical-framework-update-2026-11-18-bu.zip: 04-follow-ups/spinning-tops-henon-heiles-double-wells.md (H320–H328), coupled-oscillator-and-modular-clock.md (H307–H312), binary-quartic-pencils.md (H352–H358), fundamental-forms-willmore-hopf.md (H421–H428), conformal-and-probabilistic-readings.md (H173–H176), its 00-meta claims register and the verification scripts. External mathematical references and separate new computations are identified below. The ZIP is a historical snapshot, not the current GitHub layout.

**Main conclusion:** The foundational framework is best organized by a **typed, information-aware algebro-geometric interface**: first specify manifold, metric, connections, bundle, action, symmetry, differential operator, energy surface and clock; then apply exact operations such as curvature/contorsion reconstruction, Noether reduction, Cartan development, projectivization, Hopf/symplectic quotient, elliptic-curve normalization, and stochastic ground-state conjugacy. These operations may deliver the same ordinary differential expression in different settings **without** making the settings, boundary data, physical models or variational principles equivalent. In particular, the attachment's universal trichotomies and automatic identifications of torsion, I/J quartics and stochastic conserved charges have counterexamples.

## 1. The mathematical meaning of “the map is not the territory”

An equation is not an application, and an application is not its geometric realization. A useful correspondence must state:

1. **Source object:** metric and dimension, or symplectic manifold/Hamiltonian, or operator domain, or probability space/generator, etc.
2. **Target object:** a scalar ODE, energy curve, projected Gauss map, Lie algebra orbit, conformal metric, stochastic diffusion, etc.
3. **Map:** a change of coordinate, projectivization, gauge change, time reparametrization, symplectic quotient, affine connection change, or conjugacy of operators.
4. **Preserved data:** curvature tensor, symplectic form, first integral, scalar differential expression, root cross-ratio, period, stationary measure, etc.
5. **Lost/changed data:** global topology, marked periods, real slice, time variable, analytic domain, bundle, source matter, noise, physical interpretation.
6. **Converse conditions:** whether the original object can be reconstructed, and what boundary/gauge/normalization must be supplied.

Equal second-order equations or equal elliptic modular invariants do not generally imply equal geometries or equal applications. Conversely two different connections can provide equally valid descriptions of a selected metric once their contorsion is stated.

The classical Kepler/oscillator example is an apt analogy: planar Levi-Civita and three-dimensional Kustaanheimo–Stiefel regularizations relate selected **energy-restricted** Kepler trajectories to harmonic-oscillator trajectories through a dimension-changing transformation, a fiber constraint, and a time change. In the hydrogen Schrödinger problem, related oscillator formulations also carry quantum constraints and operator-domain data. This is a precise correspondence, not an identification of the Kepler problem, a laboratory oscillator and the hydrogen atom as the same physical object. See §21 for the formal checklist.

## 2. Canonical framework data and the distinction between source and auxiliary clocks

Keep all canonical parameters explicit:

```math
r>0,\qquad c>0,\qquad\mu>0,\qquad x>0,\qquad u=\ln(x/c),\qquad\theta=ru.
```

The canonical scalar fields are

```math
S=\mathrm{sech}(ru),\qquad W=\tanh(ru),\qquad R=\cosh(ru),\qquad S_u=-rSW,\qquad W_u=rS^2,\qquad S^2+W^2=1.
```

The original normalized Master field is

```math
y=2xf_\mu=S/\sqrt{\mu},\qquad y_{uu}=r^2y-2\mu r^2y^3.
```

The conserved nonlinear energy is

```math
\varepsilon_N=y_u^2-r^2y^2+\mu r^2y^4,\qquad e=\mu\varepsilon_N/r^2.
```

The associated normalized energy curve is

```math
z_u^2=r^2(e+z^2-z^4),\qquad z=\sqrt\mu\,y.
```

Use different symbols for separate mechanical time $t$, stochastic time $s$, a surface complex coordinate $\zeta=u+iv$ and a three-dimensional spatial curvature $K_3$. Equating any of those variables with $u$ requires an explicit pullback. For autonomous systems the constant resolution $r$ can scale a clock, but this does not preserve every physical or probabilistic normalization.

## 3. Second order does not intrinsically mean nonzero curvature or torsion [D,C]

The supplied attachment proposes that the connection underlying a second derivative is “completely determined by curvature and torsion”, and that nearly every second-order equation directly measures one of those quantities. Both assertions are too strong.

An affine connection $\nabla$ provides a covariant Hessian and acceleration, but **connection coefficients are additional local data**. Its curvature and torsion are derived tensors. In particular, for any connection on a one-dimensional manifold, curvature and torsion are identically zero by antisymmetry, yet one may pose arbitrarily different nonlinear ODEs on the same flat line:

```math
\ddot q+\omega^2q=0,\qquad \ddot q-\alpha q+\beta q^3=0,\qquad \omega,\alpha,\beta>0.
```

Neither equation has its restoring force determined by a nonzero Levi-Civita curvature or torsion. An external potential, an action, a prescribed vector field or another constitutive law must be added. Even on a higher-dimensional flat manifold, distinct smooth potentials generate arbitrarily different second-order equations with the **same** metric curvature and the same chosen zero-torsion connection.

### 3.1 The exact two-connection difference

Given a metric $g$ and a chosen flat metric-compatible Weitzenbock connection $\widetilde\nabla$, let $\mathring\nabla$ be its Levi-Civita connection and define contorsion in the explicit convention

```math
C(X,Y)=\widetilde\nabla_XY-\mathring\nabla_XY,\qquad \widetilde\nabla=\mathring\nabla+C.
```

The tensorial curvature identity is

```math
0=R(\widetilde\nabla)=R(\mathring\nabla)+D_{\mathring\nabla}C+C\wedge C.
```

A kinetic-energy extremal is a Levi-Civita geodesic, so in the alternate connection it satisfies

```math
\mathring\nabla_{\dot\gamma}\dot\gamma=0\quad\Longleftrightarrow\quad\widetilde\nabla_{\dot\gamma}\dot\gamma=C(\dot\gamma,\dot\gamma).
```

The torsion tensor is antisymmetric in its two input vectors and therefore

```math
\mathcal T(\dot\gamma,\dot\gamma)=0.
```

**Correction [C]:** It is false that the geodesic “torsion force” can generally be written $\mathcal T^k{}_{ij}\dot x^i\dot x^j$; that expression is identically zero. The correct velocity-quadratic correction is the **symmetric-in-the-two-velocities part of contorsion**, including its dependence on the full torsion tensor. Standard kinetic Euler–Lagrange equations select $\mathring\nabla$, while autoparallels of $\widetilde\nabla$ require an additional modeling rule or a different variational principle.

### 3.2 Curvature and torsion are not gauge labels for unrelated theories

The zero curvature of $\widetilde\nabla$ is an identity of **that chosen connection**. It does not make the independent Levi-Civita curvature of the same metric zero. Conversely the same metric can admit multiple flat compatible connections and inequivalent torsion tensors. The local coframe, flat spin connection, and their simultaneous frame transformations must be tracked.

For the actual canonical catenoid, draft 030 proves the selected tangent teleparallel frame identity

```math
K_{\rm cat}=-e_1(t_2)-t_2^2=-r^2S^4,\qquad t_2=rSW.
```

This is a precise, nontrivial **specific geometric instance**, not a theorem that any ODE can be read from torsion alone.

## 4. The geometric Noether theorem and its scope [K,D]

Suppose an ordinary differentiable action has Lagrangian $L(q,\dot q,t)$, momenta $p_i=\partial L/\partial\dot q^i$, and admits a continuous symmetry with infinitesimal generator $(\delta t,\delta q)$ whose Lagrangian variation is a total derivative $dF/dt$. Noether's theorem gives a conserved expression on Euler–Lagrange solutions:

```math
Q=\sum_i p_i\delta q^i-\left(\sum_i p_i\dot q^i-L\right)\delta t-F.
```

This is a conditional variational theorem: a metric Killing vector, a preserved differential operator, a topological Chern number and a stochastic martingale are **not automatically the same kind of charge**. Their conservation arguments and required assumptions differ.

### 4.1 Geodesic Killing momenta

For the metric kinetic Lagrangian $L_g=\tfrac12 g(\dot\gamma,\dot\gamma)$ and a Killing vector $K$ with $\mathcal L_Kg=0$, define

```math
Q_K=g(\dot\gamma,K).
```

Along an affinely parametrized Levi-Civita geodesic,

```math
\frac{dQ_K}{dt}=g(\mathring\nabla_{\dot\gamma}\dot\gamma,K)+\frac12(\mathcal L_Kg)(\dot\gamma,\dot\gamma)=0.
```

For a natural mechanical Lagrangian $L_g-V$, the same charge is conserved **only if** $K(V)=0$:

```math
\frac{dQ_K}{dt}=-K(V).
```

This distinction already disproves the attachment's implication that a metric isometry alone preserves the same momentum for **all** added forces. In a chosen teleparallel frame the equality can be rewritten through contorsion; that rewriting does not create an independent Noether symmetry.

## 5. Wronskians are symplectic boundary currents, not universally metric charges [D,K]

Consider the scalar Sturm–Liouville equation for a fixed real $\lambda$,

```math
-(py')'+q_0y=\lambda wy,\qquad p>0,\quad w>0.
```

Let $y_1,y_2$ be two solutions of the **same** equation and spectral parameter. Multiply the first equation by $y_2$, the second by $y_1$, subtract and integrate once:

```math
\frac d{dx}\left[p(y_1y_2'-y_1'y_2)\right]=0.
```

Thus the weighted Wronskian

```math
\mathscr W_p=p(y_1y_2'-y_1'y_2)
```

is constant on a common regularity interval.

### 5.1 Canonical symplectic interpretation

Define $P=py'$ and the phase vector $Z=(y,P)^T$. It satisfies a traceless first-order system

```math
Z'=\begin{pmatrix}0&p^{-1}\\q_0-\lambda w&0\end{pmatrix}Z.
```

For two solution vectors $Z_1,Z_2$ the symplectic area is

```math
Z_1^TJZ_2=y_1P_2-P_1y_2=\mathscr W_p,\qquad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
```

The coefficient matrix obeys $A^TJ+JA=0$, so its fundamental matrices preserve the alternating bilinear form. This is the concrete source of Wronskian conservation.

It can also be obtained as the **presymplectic current** of the quadratic variational problem, comparing two linearized solutions, but should not be described without qualification as a Noether charge of an arbitrary global $SL(2,\mathbb R)$ *symmetry of the background potential*. The space of solutions carries an alternating symplectic pairing; the underlying variable-coefficient operator need not have a three-dimensional Lie algebra of physical symmetries.

### 5.2 Ermakov–Pinney's quadratic determinant is another invariant

For the linear pair $\psi_\pm=e^{\pm ru/2}$ with Wronskian $\mathscr W=-r$, choose a Gram quadratic $G=AX^2+2CXZ+BZ^2$ and set $Y^2=G(\psi_+,\psi_-)$. As in draft 060,

```math
Y_{uu}=\frac{r^2}{4}Y+r^2(AB-C^2)Y^{-3}.
```

The quadratic determinant $\Delta_G=AB-C^2$ is not the binary-quartic $I,J$ of the Master energy. The artificial quartic $G^2$ has nonzero raw $I,J$ for $\Delta_G\ne0$ but **discriminant zero for every** Gram form. The associated Pinney energy in the centered autonomous case is

```math
E_{\rm EP}=\frac12Y_u^2-\frac{r^2}{8}Y^2+\frac{r^2(AB-C^2)}{2Y^2}=-\frac{r^2}{2}C.
```

The equality follows from the Gram first integral and shows exactly how a quadratic invariant and a dynamical energy enter distinct algebraic roles.
