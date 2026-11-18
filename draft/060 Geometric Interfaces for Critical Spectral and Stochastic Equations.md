---
id: SF-DRAFT-060
title: Geometric Interfaces for Critical, Spectral, and Stochastic Equations
status: provisional
created: 2026-11-18
proposed_layers: [I, II, III, IV]
depends_on: [SF-I-000, SF-I-010, SF-I-020, SF-DRAFT-010, SF-DRAFT-020, SF-DRAFT-030, SF-DRAFT-040, SF-DRAFT-050]
related_claims: [H127, H173, H174, H371, H372, H373, H374, H375, H376, H421, H429, H430, H431, H432, H433, H434, H435, H436, H437, H438, H443, H446]
---

# 060 Geometric Interfaces for Critical, Spectral, and Stochastic Equations

**Status:** Provisional, extensive mathematical investigation. Do not promote results automatically into a foundational theorem chapter. [D] denotes a derivation with its hypotheses, [V] an independent symbolic verification, [K] known mathematics, [H] an archived claim with its original checking scope, [C] a corrected or refuted statement in the accompanying suggestion, and [O] an open problem.

**Question:** Can the Levi-Civita/Weitzenbock geometrical mechanism and binary-quartic invariants be an algebro-geometric interface to Sturm–Liouville, Ermakov–Pinney, Hardy–Sobolev, Yamabe, Aubin–Talenti, Monge–Ampere, Eguchi–Hanson, BPST, Pöschl–Teller, Itô/Fokker–Planck and Ornstein–Uhlenbeck systems? Are these theories “classified” by one universal triple of curvature, torsion and quartic invariants?

**Answer:** There is a substantial **network of exact, typed and testable correspondences**, but not a universal classification by three scalars. The strongest common mechanisms are: (i) Wronskian/Gram-to-Pinney reduction; (ii) conformal curvature-to-critical Yamabe PDE and its local flat-frame teleparallel reformulation; (iii) the cylinder/Emden–Fowler reduction to the Master family, then its Jacobi/Pöschl–Teller spectral Hessians; (iv) radial complex Monge–Ampere Ricci-flat Kähler reduction and its separate Ermakov–Pinney profile; (v) SU(2) BPST self-duality and a logistic/Beta charge coordinate; (vi) radial **real** Monge–Ampere transport of that charge; (vii) reversible Itô diffusion, ground-state transformation into a Pöschl–Teller Schrödinger operator and a controlled Ornstein–Uhlenbeck limit. Binary-quartic moduli classify particular *specified elliptic energy curves*, not all these spaces, operators, measures and boundary-value problems.

**Sources actually inspected:** The uploaded *Pasted text(20261118-182029).txt* was read as exploratory suggestions and subjected to explicit checks. The current GitHub main foundational chapters and drafts 010–050 were checked. The historical ZIP symmetrical-framework-update-2026-11-18-bu.zip was reopened: 04-follow-ups/bpst-yamabe-eguchi-hanson.md (H371–H376), hardy-master-lame-genus-two.md (H429–H447), conformal-and-probabilistic-readings.md (H173–H176), integer-q-hierarchy.md, spectral-calculus.md, l5-modular-structure.md, and the archived claim registry. The locally mounted *Symmetrical_Framework_Complete_Reference_2026-11-16_v2.md* supplied the consolidated §§21–24 equations, retaining its provisional status. Key equations were independently checked with SymPy; literature sources are recorded near the end.

## 1. A criterion for a mathematical “classification”

A proposed classifier must specify a class of objects, an equivalence relation, an invariant assignment and its discriminating power. A binary quartic with a chosen SL(2) action admits polynomial invariants I,J. A Riemannian metric supplies Levi-Civita curvature. A chosen flat metric-compatible connection supplies a torsion tensor. The three outputs are not automatically equivalent or complete.

| Object class | Natural input and invariant | What may be reconstructed | What is not determined |
|---|---|---|---|
| Rank-two linear ODE | Wronskian and projective connection | Riccati/Schwarzian; Pinney envelopes after a Gram form | spectral self-adjoint domain |
| Autonomous cubic energy | specified binary quartic, I,J, discriminant | smooth elliptic curve and complex j on nonsingular locus | full PDE, amplitude center, real time cycle |
| Conformal Riemannian metric | LC scalar curvature, chosen flat-frame torsion | conformal Yamabe equation via a conformal factor | any universal elliptic quartic |
| Minimal/CMC surface | I, II, Gauss–Codazzi, Hopf differential | local immersed surface | global period and stability |
| Kähler radial potential | complex Hessian and Ricci form | Monge–Ampere radial ODE | gauge self-duality |
| SU(2) connection | nonabelian curvature, Chern class | Yang–Mills self-duality with explicit ansatz | a flat Weitzenbock spin connection |
| Symmetric differential operator | coefficient functions, weight and domain | Sturm–Liouville form and sometimes PT/Lamé curves | full spectrum from an elliptic j alone |
| Diffusion | metric, drift, noise, time and domain | generator, reversible measure, Doob transform | recurrence or invariant law from torsion/curvature alone |

The **interface** is a set of *typed maps* between these rows, not a theorem asserting all solutions share the same moduli.

## 2. Canonical coordinates and level conventions [H,D]

Fix the canonical resolution, scale and amplitude parameters

```math
r>0,\qquad c>0,\qquad\mu>0,\qquad x>0,\qquad u=\ln(x/c),\qquad\theta=ru.
```

The original function, circle fields, and normalized Master variable are

```math
f_\mu(x;r,c)=\frac{\mathrm{sech}(ru)}{2\sqrt\mu\,x},\qquad S=\mathrm{sech}(ru),\qquad W=\tanh(ru),\qquad R=\cosh(ru),\qquad z=\sqrt\mu\,2xf_\mu=S.
```

The fundamental differential relations are

```math
S_u=-rSW,\qquad W_u=rS^2,\qquad S^2+W^2=1.
```

The cubic Master equation is

```math
z_{uu}=r^2z-2r^2z^3,\qquad z_u^2=r^2(e+z^2-z^4),\qquad e=\mu\varepsilon_N/r^2.
```

For an integer dimension $D\ge3$ use the critical exponent parameter

```math
q=\frac{D-2}{2}>0,\qquad D=2q+2,\qquad 2^*=\frac{2D}{D-2}=2+\frac2q.
```

The archival level convention $l=2q+1$ gives $D=l+1$. These are **chosen parameter dictionaries**, not claims that all such dimensions have the same spinor or binary-quartic geometry.

The general zero-energy power profile in the dimensionless cylinder is proportional to $S^q$. Use the normalized amplitude

```math
Y_q(u)=\left(\frac{S}{2\sqrt\mu}\right)^q.
```

Then, in the same logarithmic coordinate,

```math
Y_{q,uu}=q^2r^2Y_q-4\mu q(q+1)r^2Y_q^{1+2/q}.
```

This follows by differentiating $S^q$, applying $W^2=1-S^2$, and noting $Y_q^{2/q}=S^2/(4\mu)$.

## 3. Ermakov–Pinney begins with a binary quadratic, not the elliptic binary quartic [D,V,K]

The normal-form linear backbone is

```math
\psi_{uu}-\frac{r^2}{4}\psi=0,\qquad \psi_+=e^{ru/2},\qquad\psi_-=e^{-ru/2}.
```

Its Wronskian, in the stated order, is

```math
\mathscr W=\psi_+\psi_-'-\psi_+'\psi_-=-r.
```

Let $A,B,C\in\mathbb R$ and define a quadratic Gram form and positive envelope where possible:

```math
G(X,Z)=AX^2+2CXZ+BZ^2,\qquad\Delta_G=AB-C^2.
```

```math
Y(u)^2=G(\psi_+,\psi_-)=Ae^{ru}+2C+Be^{-ru},\qquad Y>0.
```

**Theorem 3.1 [D,V,K] (Pinney from Wronskian and Gram determinant).** On any interval where $Y>0$,

```math
Y_{uu}=\frac{r^2}{4}Y+r^2\Delta_GY^{-3}.
```

**Proof, step by step.** Put $J=Y^2$. The two exponential functions satisfy $J_{uu}=r^2(J-2C)$ and

```math
J_u^2=r^2(J^2-4CJ-4\Delta_G).
```

Differentiate $Y=\sqrt J$:

```math
Y_{uu}=\frac{J_{uu}}{2Y}-\frac{J_u^2}{4Y^3}=\frac{r^2}{4}Y+\frac{r^2\Delta_G}{Y^3}.
```

This is Pinney's nonlinear superposition principle, whose general coefficient is $(AB-C^2)\mathscr W^2$ for an arbitrary fundamental pair of the same linear equation. The determinant is an invariant of the chosen **binary quadratic**, not the elliptic energy curve's $I$.

### 3.1 An exact invariant-theoretic comparison

Square the Gram polynomial to obtain a binary quartic $F_G=G^2$. In the archived **raw quartic** convention,

```math
I(F)=12af-3bd+c_2^2,\qquad J(F)=72ac_2f+9bc_2d-27ad^2-27fb^2-2c_2^3
```

for $F=aX^4+bX^3Z+c_2X^2Z^2+dXZ^3+fZ^4$.

**Theorem 3.2 [D,V] (the Gram-square quartic is always singular).**

```math
I(F_G)=16\Delta_G^2,\qquad J(F_G)=128\Delta_G^3,\qquad\Delta(F_G)=\frac{4I(F_G)^3-J(F_G)^2}{27}=0.
```

**Proof.** Expand

```math
G^2=A^2X^4+4ACX^3Z+(2AB+4C^2)X^2Z^2+4BCXZ^3+B^2Z^4.
```

Substitute these five coefficients into the raw formulas and factor the result. Independently, $G^2$ has repeated projective roots even when $G$ has two distinct roots, so its polynomial discriminant must vanish. The exact powers above record how its $I,J$ remember the *quadratic* determinant while **failing** to provide a smooth elliptic curve.

Thus Ermakov–Pinney's determinant can be expressed using quartic invariant polynomials after a chosen squaring map, but it is **not** an elliptic binary quartic modulus. The interface explicitly distinguishes Gram determinants, Master energy quartics and Weyl-spinor quartics (draft 050).

## 4. A genuine elliptic quartic arises from a specified nonlinear first integral [D,V,H429]

The normalized cubic Master energy polynomial is

```math
F_e(X,Z)=-X^4+X^2Z^2+eZ^4.
```

Its raw invariants, discriminant and smooth $j$ are

```math
I_e=1-12e,\qquad J_e=-2(1+36e),\qquad \Delta_e=-16e(1+4e)^2.
```

```math
j_e=-16\frac{(1-12e)^3}{e(1+4e)^2},\qquad e\notin\{0,-1/4\}.
```

These formulas are independently checked and recorded in archival H429. For $e\ne0,-1/4$, the affine energy curve $p^2=e+z^2-z^4$ is generically an elliptic curve. At $e=0$ its separatrix gives $z=S$, and the polynomial is singular. At $e=-1/4$ the roots merge differently (the equilibrium energy). The limits $j_e\to\infty$ at singular energies are statements about elliptic degeneration, not general curvatures of all accompanying geometries.

**Negative control:** The canonical catenoid's *fundamental-form* quartic has $j=1728$ and **nonzero** discriminant at every finite nonflat point (draft 050), while the very same profile's cubic **energy** quartic at $e=0$ has **zero** discriminant. Consequently the slogan “every localized profile has $\Delta=0$” is false without specifying the quartic being classified.

## 5. Sturm–Liouville is a weighted differential expression plus its operator domain [D,K]

A scalar regular or singular Sturm–Liouville differential expression has

```math
-(p(x)y')'+q_0(x)y=\lambda w(x)y,\qquad p>0,\quad w>0.
```

This is not the same object as the Master power parameter $q$: here $q_0$ is an arbitrary coefficient. Set

```math
t=\int^x\sqrt{w(s)/p(s)}\,ds,\qquad \rho=(pw)^{1/4},\qquad \psi(t)=\rho(x)y(x).
```

Direct differentiation gives the Liouville normal form

```math
-\psi_{tt}+\left(\frac{q_0}{w}+\frac{\rho_{tt}}{\rho}\right)\psi=\lambda\psi.
```

The positive weight defines the formal Hilbert-space norm $\int |y|^2w\,dx=\int|\psi|^2dt$ on corresponding intervals. Boundary conditions, limit-point/limit-circle endpoints and self-adjoint realization must still be specified. The transformation alone does not classify the spectrum.

For the normal form $\psi_{tt}=(V-\lambda)\psi$ and nonvanishing $\psi$, the logarithmic derivative $h=\psi_t/\psi$ satisfies

```math
h_t+h^2=V-\lambda.
```

For two independent solutions with projective ratio $F=\psi_1/\psi_2$,

```math
\{F,t\}=2(\lambda-V),\qquad \mathscr W=\psi_1\psi_{2,t}-\psi_{1,t}\psi_2=\mathrm{constant}.
```

The Riccati/Schwarzian interface holds for every normal-form scalar equation. **An elliptic quartic arises only when additional potential or first-integral structure makes one appear**, e.g. Lamé curves—not from Sturm–Liouville self-adjointness itself.

## 6. From the critical Sobolev PDE to the Master cylinder [D,V,H371,H429]

Let $D=2q+2$ be an integer at least three, $\rho>0$ the Euclidean radial coordinate, and $c>0$ its scale. Put $u=\ln(\rho/c)$ in this **radial realization** and define

```math
U_{q,r,c,\mu}(\rho)=(4\mu)^{-q/2}\rho^{-q}\mathrm{sech}^{q}(r\ln(\rho/c)).
```

**Theorem 6.1 [D,V] (critical Hardy–Sobolev equation).** The profile solves

```math
-\Delta_{\mathbb R^D}U+\frac{q^2(r^2-1)}{\rho^2}U=4\mu q(q+1)r^2U^{1+2/q}.
```

The power $1+2/q=(D+2)/(D-2)$ is the critical Yamabe exponent.

**Proof, step by step.** Set $v(u)=\rho^qU(\rho)$, with $u=\ln(\rho/c)$. For a radial field in $D=2q+2$,

```math
\Delta_{\mathbb R^D}U=U_{\rho\rho}+\frac{D-1}{\rho}U_\rho=\rho^{-q-2}(v_{uu}-q^2v).
```

Multiply the proposed PDE by $\rho^{q+2}$; its left side is $-v_{uu}+q^2r^2v$. The right side becomes $4\mu q(q+1)r^2v^{1+2/q}$ because $\rho^{q+2}(\rho^{-q})^{1+2/q}=1$. The claimed equation is exactly the identity for $Y_q=v$ in §2.

**Scope:** The value $r=1$ removes the inverse-square Hardy term. For $r\ne1$ this is a weighted/Hardy critical equation, not the same Euclidean Yamabe equation after a harmless change of notation. The singular coefficient and its operator domain require separate analysis, especially at $\rho=0$. At $r>1$, even where the displayed positive radial critical point exists it need not be the unrestricted sharp minimizer; the archive explicitly warns against equating a stationary profile with the global Hardy–Sobolev extremal.

### 6.1 Aubin–Talenti and the stereographic metric

At $r=1$, use $\mathrm{sech}\ln(\rho/c)=2c\rho/(\rho^2+c^2)$ to obtain

```math
U_{q,1,c,\mu}(\rho)=\left(\frac{c}{\sqrt\mu(\rho^2+c^2)}\right)^q.
```

This is the Aubin–Talenti positive bubble up to the normalization fixed by $\mu$, with the translation orbit obtained by replacing $\rho=|X|$ by $|X-X_0|$. Its exponent $q=(D-2)/2$ is forced by conformal covariance.

Define the conformal metric on the Euclidean chart

```math
g_U=U^{4/(D-2)}g_{\mathrm{Euc}}=U^{2/q}g_{\mathrm{Euc}}=e^{2h}g_{\mathrm{Euc}},\qquad h=\frac1q\ln U.
```

At $r=1$ its conformal coefficient is

```math
e^h=\frac{c}{\sqrt\mu(\rho^2+c^2)}.
```

The round $D$-sphere of radius $a_0=1/(2\sqrt\mu)$ has stereographic metric $g_{S^D_{a_0}}=[2a_0^2/(\rho^2+c^2)]^2$ after the corresponding coordinate dilation. The displayed metric is isometric to that round metric under an appropriate stereographic chart rescaling, and its scalar curvature is $4\mu D(D-1)$.

**Caveat about global geometry:** A stereographic conformal factor is a metric on a chart; the round compactification requires the regular conformal continuation across the missing point. At $r\ne1$, the conical/Hardy singular structure generally obstructs this same smooth round compactification.

## 7. An explicit Yamabe–Levi-Civita–Weitzenbock theorem [D,V,K]

Consider an arbitrary *local* conformally flat metric of dimension $D\ge2$, Riemannian or with a fixed constant background signature,

```math
g=e^{2h(X)}\eta_{ij}\,dX^idX^j.
```

Write $\nabla_0,\Delta_0,|\nabla_0h|^2$ for the flat background derivatives and norm with the chosen constant bilinear form $\eta$. With the Levi-Civita connection, the standard scalar curvature formula is

```math
\mathring{\mathcal R}[g]=e^{-2h}\left[-2(D-1)\Delta_0h-(D-1)(D-2)|\nabla_0h|^2\right].
```

Select **an additional local orthonormal coframe**, $\vartheta^a=e^h dX^a$, and declare this frame parallel for a flat metric-compatible Weitzenbock connection with zero spin connection in that frame.

**Theorem 7.1 [D,V] (exact conformal teleparallel dictionary).** Its torsion components, torsion trace, quadratic torsion scalar and boundary divergence in the convention of draft 040 are

```math
\mathcal T^k{}_{ij}=h_i\delta^k{}_j-h_j\delta^k{}_i,\qquad v_i=\mathcal T^j{}_{ji}=-(D-1)h_i.
```

```math
\mathbb T=-(D-1)(D-2)e^{-2h}|\nabla_0h|^2.
```

```math
\mathbb B=2\mathring\nabla_iv^i=-2(D-1)e^{-2h}\left[\Delta_0h+(D-2)|\nabla_0h|^2\right].
```

Thus, identically,

```math
\mathring{\mathcal R}=-\mathbb T+\mathbb B.
```

**Proof, step by step.**

1. The chosen Weitzenbock coordinate coefficients are $\widetilde\Gamma^k{}_{ij}=h_i\delta^k{}_j$. Antisymmetrizing gives the torsion displayed, and contracting its first and second indices gives the trace $-(D-1)h_i$.
2. Insert that vector-type torsion into the three quadratic contractions defining the torsion scalar in draft 040. Its contraction reduces to $-(D-1)(D-2)|\nabla h|_g^2$, where $|\nabla h|_g^2=e^{-2h}|\nabla_0h|^2$.
3. Calculate the divergence using $\sqrt{|\det g|}=e^{Dh}\sqrt{|\det\eta|}$ and $v^i=-(D-1)e^{-2h}\eta^{ij}h_j$.
4. Subtract $\mathbb T$ from $\mathbb B$; the coefficients combine into the standard conformal scalar-curvature formula.

**Important interpretation:** The two connections are different. The metric alone does not canonically determine this Weitzenbock frame or its torsion; the Levi-Civita scalar is intrinsic. On a nonparallelizable compactification (e.g. the round four-sphere), the **single coordinate tetrad** need not extend globally. The displayed identities are local, fully rigorous and sufficient for the proposed foundational interface.

### 7.1 Recover the critical Yamabe equation from this identity

For Riemannian flat background, set $g=U^{4/(D-2)}\delta$, $U>0$, so $h=2\ln U/(D-2)$. The curvature formula simplifies to

```math
\mathring{\mathcal R}[g]=-\frac{4(D-1)}{D-2}U^{-(D+2)/(D-2)}\Delta_{\mathbb R^D}U.
```

Therefore the requirement that $g$ have a **specified constant** scalar curvature $R_0$ is exactly the Yamabe equation

```math
-\frac{4(D-1)}{D-2}\Delta U=R_0U^{(D+2)/(D-2)}.
```

Using the selected Weitzenbock frame, the same equation can be written $\mathbb B-\mathbb T=R_0$. This is an algebraic/differential rewriting of a **given metric equation**, not a separately postulated teleparallel field equation.

### 7.2 Evaluate both invariants on the Aubin–Talenti sphere

For the exact $r=1$ bubble, $h=\ln[c/(\sqrt\mu(\rho^2+c^2))]$, one finds

```math
h_\rho=-\frac{2\rho}{\rho^2+c^2},\qquad e^{-2h}=\frac{\mu(\rho^2+c^2)^2}{c^2}.
```

**Corollary 7.2 [D,V].** The preferred flat-frame torsion and divergence are

```math
\mathbb T=-4\mu(D-1)(D-2)\frac{\rho^2}{c^2}.
```

```math
\mathbb B=4\mu D(D-1)-4\mu(D-1)(D-2)\frac{\rho^2}{c^2}.
```

Their difference is the constant scalar curvature

```math
\mathring{\mathcal R}=\mathbb B-\mathbb T=4\mu D(D-1).
```

**Proof.** Insert $h_\rho$ into Theorem 7.1. For a radial Euclidean function $\Delta_0h=h_{\rho\rho}+(D-1)h_\rho/\rho$, and the algebra simplifies exactly to the displayed expressions.

**Consequences:** The same round metric has constant Levi-Civita scalar curvature but an **unbounded** torsion scalar in this stereographic *choice of parallel frame*. It is false that a single torsion scalar value can classify the round metric independently of frame/connection choice. The divergence compensates the torsion variation pointwise.

### 7.3 A general-resolution curvature defect

For $r>0$ keep $U_{q,r,c,\mu}$ of §6 and $g_U=U^{2/q}\delta$. The conformal scalar curvature is

```math
\mathring{\mathcal R}[g_U]=8\mu(2q+1)\left[(q+1)r^2-q(r^2-1)\mathrm{sech}^{-2}(ru)\right].
```

**Proof.** Combine Theorem 6.1 with the conformal curvature identity and note $\rho^{-2}U^{-2/q}=4\mu\mathrm{sech}^{-2}(ru)$. At $r=1$ the position-dependent term vanishes; away from that value the inverse-square Hardy defect survives in the scalar curvature. Thus the original resolution dial has a genuine conformal-geometric effect in this chosen radial realization, rather than being a harmless coordinate gauge.

### 7.4 The exact preferred torsion scalar at arbitrary resolution

For the general radial conformal metric induced by the Hardy critical profile $U_{q,r,c,\mu}$, the conformal exponent is

```math
h(\rho)=\ln\left[\frac{\mathrm{sech}(r\ln(\rho/c))}{2\sqrt\mu\,\rho}\right],\qquad h_\rho=-\frac{1+rW}{\rho}.
```

Theorem 7.1 gives, for the **chosen flat coordinate coframe**,

```math
\mathbb T_{q,r}=-4\mu(D-1)(D-2)\frac{(1+rW)^2}{S^2},\qquad D=2q+2.
```

The boundary scalar is then obtained exactly from the curvature formula in §7.3:

```math
\mathbb B_{q,r}=\mathbb T_{q,r}+8\mu(2q+1)[(q+1)r^2-q(r^2-1)S^{-2}].
```

This is a **nontrivial all-resolution Levi-Civita–Weitzenbock dictionary** for the chosen conformal metric. The scale $c$ enters through $u=\ln(\rho/c)$; the parameter $\mu$ sets the overall metric scale. At $r=1$,

```math
(1+W)^2/S^2=(\rho/c)^2,\qquad\mathbb T_{q,1}=-4\mu(D-1)(D-2)\rho^2/c^2,
```

recovering the round-chart formula. Neither the $\rho$-dependence of the selected torsion scalar nor its singular behavior at a chart boundary is a frame-independent invariant of the round compactification.

## 8. Critical linearization yields the Pöschl–Teller hierarchy [D,V,H429–H431]

On the logarithmic cylinder $\mathbb R_u\times S^{D-1}$, the critical radial equation for $U=\rho^{-q}v$ becomes

```math
-\partial_u^2v-\Delta_{S^{D-1}}v+q^2r^2v=4\mu q(q+1)r^2v^{1+2/q}.
```

Its centered positive solution is $v_0=(S/(2\sqrt\mu))^q$. Linearize at $v_0$ in the direction $\xi$.

**Theorem 8.1 [D,V] (exact cylinder Hessian).**

```math
\mathcal L_{q,r}=-\partial_u^2-\Delta_{S^{D-1}}+q^2r^2-(q+1)(q+2)r^2S^2.
```

**Proof.** The derivative of $v^{1+2/q}$ at $v_0$ is $(1+2/q)v_0^{2/q}$, with $v_0^{2/q}=S^2/(4\mu)$. Multiply by $4\mu q(q+1)r^2$ to obtain $(q+1)(q+2)r^2S^2$. Bring this linear term to the left.

In spherical harmonic order $\ell$, where $-\Delta_{S^{D-1}}Y_\ell=\ell(\ell+D-2)Y_\ell$,

```math
\mathcal L_{q,r}^{(\ell)}=-\frac{d^2}{du^2}+\ell(\ell+2q)+q^2r^2-(q+1)(q+2)r^2S^2.
```

This is the hyperbolic Pöschl–Teller form with well parameter $\nu=q+1$. At integer $q$ the well has an integer reflectionless parameter; at noninteger $q$ the potential is solvable in hypergeometric functions but is **not generically reflectionless**.

For integer $q$ the formal separated bound-state eigenvalues are

```math
\lambda_{\ell,j}=\ell(\ell+2q)+r^2[q^2-(q+1-j)^2],\qquad j=0,1,\ldots,q.
```

The lowest angular branch vanishes at

```math
r_{D,\ell}^2=\frac{\ell(\ell+D-2)}{D-1},\qquad r_{D,1}=1.
```

A Hessian zero mode is necessary for a bifurcation, not sufficient to infer a nonlinear branch or a global minimizer; transversality, symmetry, and the operator domain still matter.

### 8.1 Distinguish two separate geometric Hessians

The Euclidean catenoid Jacobi operator from draft 030, after Fourier decomposition, contains a Pöschl–Teller well of order **one**, namely $-2r^2S^2$. The $D=4$ critical Yamabe scalar Hessian has well coefficient $-6r^2S^2$ and order **two**. They share the same elementary profile, but are not the same operator; an explicit Darboux factorization accounts for their relation.

## 9. Nonzero energy: Lamé and higher-genus spectral curves are not universal quartics [H436–H447]

For the cubic Master trajectory at $-1/4<e<0$, the positive real periodic orbit is

```math
z(u)=\frac1{\sqrt{2-m}}\mathrm{dn}\left(\frac{ru}{\sqrt{2-m}}\mid m\right),\qquad e=-\frac{1-m}{(2-m)^2},\quad0<m<1.
```

The full $D=4$ cylinder Hessian now contains the potential $-6r^2z^2$. Its reduced form is Lamé degree two, whose **spectral** hyperelliptic curve has genus two in the generic finite-gap realization, while the **nonlinear orbit energy curve** has genus one. They are different algebraic curves attached to the same solution.

For level $l=5$, the intrinsic variable $B$ obeys, in dimensionless $\theta=ru$ clock,

```math
B_{\theta\theta}=4B-6B^2,\qquad B_\theta^2=4(e_5+B^2-B^3).
```

The elliptic orbit admits

```math
X=1/3-B,\qquad X_\theta^2=4X^3-\frac43X+\frac8{27}+4e_5.
```

Thus

```math
g_2=4/3,\qquad g_3=-8/27-4e_5,\qquad\Delta=-16e_5(27e_5+4),\qquad j=-\frac{256}{e_5(27e_5+4)}.
```

But the intrinsic level-five scalar Hessian becomes Lamé degree **three**, whose generic spectral curve has genus three rather than the orbit's genus one. At the separatrix $e_5=0$, the elliptic curve degenerates and the hyperbolic Pöschl–Teller potential returns. Its reflectionless property follows from the **integer** Pöschl–Teller order, not merely from the equation $\Delta=0$.

The archive also records a genus-two Lamé curve with degree-three elliptic subcovers, and a smooth level-nine genus-two **nonlinear** curve whose sextic invariant distinguishes it from that Lamé spectral curve. Therefore binary-quartic $I,J$ and elliptic $j$ cannot classify all spectral levels, because higher-genus curves need further invariants and marked periods.

## 10. A precise spectral negative control: j does not determine an operator

A fixed elliptic curve with modulus $j$ admits many distinct differential operators, spectral parameters and line bundles. Even on a fixed real circle, replacing $V(u)$ by $V(u)+a$ shifts all eigenvalues without changing the underlying complex elliptic period lattice. Boundary conditions (periodic, antiperiodic, Dirichlet, singular extensions) can change spectra while the same potential curve remains.

Thus the invariant of an underlying quartic does not determine the Sturm–Liouville or Lamé spectrum. A complete spectral datum additionally includes the operator coefficients, real interval/cycle, marked Floquet multiplier and self-adjoint domain.

## 11. Complex Monge–Ampere, Ricci curvature and the Eguchi–Hanson profile [D,V,H373]

The complex Monge–Ampere branch is a **Kähler Ricci-curvature equation**, not the same determinant as the real optimal-transport equation of §14. Let $z=(z_1,\ldots,z_m)\in\mathbb C^m$ and set

```math
s=\sum_{i=1}^{m}|z_i|^2>0,\qquad \mathcal K=\mathcal K(s),\qquad P(s)=s\mathcal K_s.
```

The Kähler metric of the local potential is

```math
g_{i\bar j}=\partial_i\partial_{\bar j}\mathcal K=\mathcal K_s\delta_{ij}+\mathcal K_{ss}\bar z_i z_j.
```

The Hermitian matrix has tangential eigenvalue $\mathcal K_s=P/s$ with multiplicity $m-1$, and radial eigenvalue $\mathcal K_s+s\mathcal K_{ss}=P_s$.

**Theorem 11.1 [D,V] (radial complex Monge–Ampere).** Its determinant and Ricci form satisfy

```math
\det(g_{i\bar j})=(P/s)^{m-1}P_s,\qquad \mathrm{Ric}=-i\,\partial\bar\partial\ln\det(g_{i\bar j}).
```

Imposing the special Ricci-flat volume normalization $\det g=1$ leads exactly to

```math
(P^m)_s=m s^{m-1},\qquad P^m=s^m+a^{2m},
```

where the integration constant $a^{2m}>0$ has been chosen positive.

**Proof.** Diagonalize the rank-one perturbation of $\mathcal K_s I$: $m-1$ eigenvectors orthogonal to $z$ have eigenvalue $P/s$, while the radial vector $z$ has eigenvalue $P_s$. Multiply. Setting the determinant to one gives $P^{m-1}P_s=s^{m-1}$; integrate. Locally a constant determinant gives a zero Ricci form. Other prescribed determinants lead to other complex Monge–Ampere equations.

### 11.1 Eguchi–Hanson at complex dimension two

Set $m=2$, so that the real dimension is four. Then

```math
P(s)=\sqrt{s^2+a^4},\qquad \det g=(P/s)P_s=1.
```

An explicit local Kähler potential, up to an additive constant, is

```math
\mathcal K(s)=\sqrt{s^2+a^4}+a^2\ln\left(\frac{s}{a^2+\sqrt{s^2+a^4}}\right).
```

A direct derivative gives $\mathcal K_s=P/s$, confirming the radial determinant equation.

To exhibit the Pinney correspondence, introduce a **new** radial chart variable $\xi$, with a separately chosen positive parameter $r$:

```math
s=a^2\sinh(r\xi),\qquad \xi>0,\qquad P=a^2\cosh(r\xi),\qquad R(\xi)=\sqrt P=a\sqrt{\cosh(r\xi)}.
```

**Proposition 11.2 [D,V].** This radial function satisfies

```math
R_{\xi\xi}=\frac{r^2}{4}R+\frac{r^2a^4}{4R^3},\qquad R_\xi^2=\frac{r^2}{4}(R^2-a^4R^{-2}).
```

**Proof.** $R^2=a^2\cosh(r\xi)$ has quadratic invariant $(R^2)^2-[(R^2)_\xi/r]^2=a^4$. Apply Theorem 3.1 to the centered two-exponential envelope, or differentiate explicitly.

This is an exact **local algebraic correspondence** with the canonical positive Pinney envelope. The coordinate $\xi=r^{-1}\operatorname{arsinh}(s/a^2)$ is not automatically the original canonical $u=\ln(x/c)$; equating them requires the explicit radial pullback $s=a^2\sinh(r\ln(x/c))$ with domain $x>c$.

The Eguchi–Hanson complete four-dimensional metric arises after a suitable angular identification/resolution of the local radial Kähler solution. Its hyperkähler/Ricci-flat, ALE and nonflat character is classical [K]. The local determinant calculation alone does **not** prove the topology, completeness, orientation of self-duality or regularity of the compact exceptional divisor; those require the standard global construction.

### 11.2 Two different algebraic curves can be written for the same radial construction

The fundamental radial Monge–Ampere integral is the **conic**

```math
P^2-s^2=a^4.
```

One can separately construct the binary quartic $F_a(X,Z)=X^4-a^4Z^4$ from the common cohomogeneity-one metric coefficient. Its raw invariants are

```math
I(F_a)=-12a^4,\qquad J(F_a)=0,\qquad\Delta(F_a)=-256a^{12},\qquad j(F_a)=1728\quad(a>0).
```

**Scope:** This is a smooth *constructed quartic* and a legitimate harmonic elliptic double cover. The original radial complex Monge–Ampere determinant equation is a conic rather than this elliptic curve. The existence of a natural quartic expression in another coordinate does not prove that its periods or elliptic $j$ classify the Eguchi–Hanson metric, its moduli or its self-duality.

### 11.3 Complex Hessian, LC curvature and teleparallel connection must remain distinct

Ricci-flatness here follows from a complex Hermitian determinant/Levi-Civita Ricci form. A local orthonormal frame can be used to build a flat metric-compatible Weitzenbock connection **where a frame exists**, but that is a **different connection** from the Kähler Levi-Civita connection and depends on the chosen frame. Ricci-flatness of the Levi-Civita connection does not imply zero Riemann curvature or zero Weitzenbock torsion.

The self-dual/anti-self-dual decomposition of the four-dimensional Riemann tensor depends on orientation and the Hodge star. It is not a binary-quartic classification determined by a single putative teleparallel torsion scalar.

## 12. BPST: a nonflat SU(2) gauge connection, not flat teleparallel torsion [D,H371,H374]

On flat Euclidean $\mathbb R^4$, fix a center $X_0$, a size $c>0$, radial distance $\rho=|X-X_0|$, and a convention of self-dual 't Hooft symbols $\eta^a_{\mu\nu}$. The classical BPST regular-gauge connection and curvature can be normalized as

```math
A_\mu^a=\frac{2\eta^a_{\mu\nu}(X-X_0)^\nu}{\rho^2+c^2},\qquad F_{\mu\nu}^a=-\frac{4c^2\eta^a_{\mu\nu}}{(\rho^2+c^2)^2}.
```

Its squared curvature density in the convention used in the project archive is

```math
F_{\mu\nu}^aF_{\mu\nu}^a=\frac{192c^4}{(\rho^2+c^2)^4}.
```

Its self-duality $F=*F$ is a condition on an **SU(2) gauge curvature**, not on the torsion tensor of a flat Weitzenbock connection. The pure Maurer–Cartan form $g^{-1}dg$ has zero gauge curvature; the BPST ansatz multiplies it by a *nonconstant radial function*, producing nonzero curvature. Thus “the BPST instanton is pure Weitzenbock torsion” is false without a new, explicit, nonstandard construction and proof.

### 12.1 The exact logistic and BPST charge identities

Use the physical radial logarithmic coordinate $u=\ln(\rho/c)$, corresponding to **$r=1$** in the canonical radius $\rho$:

```math
P(\rho)=\frac{\rho^2}{\rho^2+c^2}=\frac{1+\tanh u}{2}=\frac{1+W}{2},\qquad P_u=2P(1-P).
```

The normalized cumulative charge is the polynomial

```math
Q(\rho)=3P^2-2P^3=\frac12+\frac34W-\frac14W^3.
```

Differentiate and use $W_u=S^2$:

```math
\frac{dQ}{du}=\frac34S^4=\frac34\mathrm{sech}^4u.
```

In the framework's rescaled radial chart $\rho=c(x/c)^r$, this reads

```math
\frac{dQ}{du}=\frac{3r}{4}\mathrm{sech}^4(ru),\qquad u=\ln(x/c),\qquad\theta=\ln(\rho/c)=ru.
```

The parameter $r$ here changes the *pullback coordinate* of the physical BPST radius, not the instanton's topological charge or an independent family of flat-space BPST solutions with arbitrary power-law radial profiles.

### 12.2 The action density and its integral are separate data

The four-dimensional radial integral is

```math
\int_{\mathbb R^4}\frac{d^4X}{(\rho^2+c^2)^4}=\frac{\pi^2}{6c^4}.
```

Therefore the ordinary self-dual charge-one BPST configuration has, for the specified normalization,

```math
\frac1{4g^2}\int F_{\mu\nu}^aF_{\mu\nu}^a\,d^4X=\frac{8\pi^2}{g^2}.
```

This is a gauge-theoretic variational and topological result after supplying the connection and normalization. The radial scalar coefficient $S^2$ by itself is not a full gauge field; many unrelated mathematical problems can contain $S^2$ without possessing a second Chern number.

## 13. The exact stereographic Aubin–Talenti/BPST density bridge [D,V,H371,H374]

At $D=4$, the $r=1$ Aubin–Talenti/Yamabe bubble is

```math
U_{\mathrm{AT}}(\rho)=\frac{c}{\sqrt\mu(\rho^2+c^2)}.
```

The round four-sphere metric stereographic factor is, up to the stated radius normalization, the **square** of this bubble. Its volume density has the fourth power of the conformal factor:

```math
d\mathrm{vol}_{g_U}=U_{\mathrm{AT}}^4\,d^4X=\frac{c^4}{\mu^2(\rho^2+c^2)^4}\,d^4X.
```

The BPST squared-curvature density is proportional to the *same* rational function:

```math
|F_{\rm BPST}|^2=\frac{192c^4}{(\rho^2+c^2)^4}.
```

Hence, for this matched size, center and flat four-dimensional coordinate,

```math
|F_{\rm BPST}|^2=192\mu^2\,\frac{d\mathrm{vol}_{g_U}}{d^4X}.
```

**Proof.** Substitute the displayed $U_{\mathrm{AT}}$ and the BPST curvature formula. This is exact dimensional algebra: in four dimensions the volume density of $g_U=U^2g_{\rm Euc}$ is $U^4$ and the BPST curvature coefficient is fourth power of the same denominator.

This does **not** make the Yang–Mills functional the Yamabe functional, equate their Euler–Lagrange operators or identify their variation spectra. It is a match of specific, properly normalized **density profiles** with the round $S^4$ stereographic measure.

The independent gauge and geometric topological data also differ: BPST uses the second Chern class of an SU(2) bundle over the compactified four-sphere; the Yamabe bubble is a positive scalar conformal factor. In particular, a nonflat Yang–Mills connection cannot be identified with a flat metric-compatible Weitzenbock spin connection merely through their common $S^2$ coefficient.

## 14. Real radial Monge–Ampere transports the same charge density [D,V,H374]

Now consider the **real** Monge–Ampere equation in $\mathbb R^D$ for a radial convex potential $\Phi(X)=\phi(\rho)$, $\rho=|X|$. The radial Hessian eigenvalue is $\phi''(\rho)$ and the tangential eigenvalue is $\phi'(\rho)/\rho$ with multiplicity $D-1$. Hence

```math
\det D^2\Phi=\phi''(\rho)\left(\frac{\phi'(\rho)}{\rho}\right)^{D-1}.
```

If $\det D^2\Phi=F(\rho)$ and $\phi'(0)=0$, multiply by $D\rho^{D-1}$ and integrate:

```math
\phi'(\rho)^D=D\int_0^\rho t^{D-1}F(t)\,dt.
```

This is a fully explicit second-order **PDE to one-dimensional first-integral** reduction that does not require any binary quartic.

### 14.1 The four-dimensional BPST charge as a transport radius

The normalized BPST/round-sphere probability density and unit four-ball density are respectively

```math
p_c(X)=\frac{6c^4}{\pi^2(\rho^2+c^2)^4},\qquad p_{\rm ball}=\frac2{\pi^2}.
```

A radial optimal-transport map to the uniform unit ball has target radius $T(\rho)=\phi'(\rho)$. The pushforward Jacobian equation is

```math
\det D^2\Phi=\frac{p_c}{p_{\rm ball}}=\frac{3c^4}{(\rho^2+c^2)^4}.
```

The radial first integral then gives

```math
\phi'(\rho)^4=Q(\rho)=\frac{\rho^4(\rho^2+3c^2)}{(\rho^2+c^2)^3}=3P(\rho)^2-2P(\rho)^3.
```

**Proof, step by step.** Differentiate $Q$ from §12.1 to find $Q'(\rho)=12\rho^3c^4/(\rho^2+c^2)^4$. Then $\phi'=Q^{1/4}$ gives

```math
\phi''(\phi'/\rho)^3=\frac{Q'}{4\rho^3}=\frac{3c^4}{(\rho^2+c^2)^4}.
```

Because the radial map is monotone and the potential is convex, it is the quadratic-cost Brenier transport in this finite-second-moment setting [K]. The **same cubic charge CDF** now appears as a radial Monge–Ampere transport mass coordinate, not a new gauge curvature.

For the $D$-dimensional critical stereographic probability density proportional to $c^D/(\rho^2+c^2)^D$, the variable $P=\rho^2/(\rho^2+c^2)$ has the Beta$(D/2,D/2)$ distribution; the uniform-$D$-ball target radius is $I_P(D/2,D/2)^{1/D}$. This is a family of exact mass-transport constructions, not an $I,J$-invariant elliptic classification.

## 15. Reversible Itô diffusion is a chosen outer-layer generator [D,V,H375]

Fix $\alpha>0$ and retain the canonical $u=\ln(x/c)$, $r>0$ and $W(u)=\tanh(ru)$. Define the normalized probability density

```math
\pi_{\alpha,r}(u)=\frac{r\,\Gamma((\alpha+1)/2)}{\sqrt\pi\,\Gamma(\alpha/2)}\mathrm{sech}^{\alpha}(ru).
```

The normalization follows from the Euler Beta integral. Let the confinement function be

```math
V_\alpha(u)=\alpha\ln\cosh(ru),\qquad V_\alpha'=\alpha rW,\qquad V_\alpha''=\alpha r^2S^2.
```

**Theorem 15.1 [D,V] (diffusion and reversible divergence form).** The generator

```math
\mathcal G_{\alpha,r}=\partial_u^2-\alpha rW\partial_u=\pi_{\alpha,r}^{-1}\partial_u(\pi_{\alpha,r}\partial_u)
```

corresponds to the Itô stochastic differential equation in **stochastic time $t$**, distinct from the spatial logarithmic coordinate $u$:

```math
dU_t=-\alpha r\tanh(rU_t)\,dt+\sqrt2\,dB_t.
```

The formal Fokker–Planck adjoint is

```math
\partial_t p=\partial_u^2p+\partial_u(\alpha rW p),
```

and $\pi_{\alpha,r}$ is its zero-current stationary density.

**Proof, step by step.** Since $(\ln\pi_{\alpha,r})'=-\alpha rW$, expand the divergence-form generator. An Itô diffusion with volatility $\sqrt2$ has generator $\tfrac12(2)\partial_u^2+b(u)\partial_u$. Set $b=-\alpha rW$. Integrating by parts under appropriate decay/no-flux boundary conditions gives

```math
\int f\mathcal G_{\alpha,r}g\,\pi_{\alpha,r}\,du=-\int f'g'\,\pi_{\alpha,r}\,du.
```

Thus the generator is formally symmetric, nonpositive and reversible with respect to its specified density. Statements about a unique global Markov semigroup, stationary uniqueness or spectral self-adjointness require their respective domain hypotheses.

### 15.1 What Itô's Hessian actually does

For a smooth coordinate function $F$, Itô's formula is

```math
dF(U_t)=[F''(U_t)-\alpha rW(U_t)F'(U_t)]\,dt+\sqrt2 F'(U_t)\,dB_t.
```

The second derivative is the quadratic-variation correction. A Levi-Civita connection can organize the Hessian covariantly on a manifold; a chosen Weitzenbock frame can also describe stochastic developments but requires the correct drift correction. **Neither connection alone specifies the noise or its drift.**

For example the original multiplicative coordinate $X_t=ce^{U_t}$ obeys

```math
dX_t=X_t[1-\alpha r\tanh(r\ln(X_t/c))]\,dt+\sqrt2 X_t\,dB_t.
```

The extra $+X_tdt$ comes exactly from Itô's second derivative, not from a curvature invariant. The invariant measure in the $x$ coordinate has density proportional to $\mathrm{sech}^\alpha(r\ln(x/c))\,dx/x$.

## 16. The exact ground-state transformation: diffusion to Pöschl–Teller [D,V,K,H375]

The unitary map from the diffusion Hilbert space $L^2(\pi_{\alpha,r}\,du)$ to ordinary $L^2(du)$ is multiplication by $\psi_0=\sqrt{\pi_{\alpha,r}}$, up to a harmless normalization. Define

```math
\mathcal H_{\alpha,r}=-\psi_0\mathcal G_{\alpha,r}\psi_0^{-1}.
```

**Theorem 16.1 [D,V] (Pöschl–Teller via a reversible ground state).**

```math
\mathcal H_{\alpha,r}=-\partial_u^2+\frac14(V_\alpha')^2-\frac12V_\alpha''.
```

```math
\mathcal H_{\alpha,r}=-\partial_u^2+\frac{\alpha^2r^2}{4}-\frac{\alpha(\alpha+2)r^2}{4}S^2.
```

It factorizes as

```math
\mathcal H_{\alpha,r}=A_n^\dagger A_n,\qquad A_n=\partial_u+nrW,\qquad A_n^\dagger=-\partial_u+nrW,\qquad n=\alpha/2.
```

The positive ground state is $\psi_0\propto S^n$, with eigenvalue zero.

**Proof, step by step.**

1. Write $\pi=e^{-V_\alpha}/Z$. Then $\psi_0=e^{-V_\alpha/2}/\sqrt Z$.
2. Substitute $f=e^{V_\alpha/2}\psi$ into $\mathcal G_{\alpha,r}f=f''-V_\alpha'f'$, and simplify:

```math
-\psi_0\mathcal G_{\alpha,r}(\psi_0^{-1}\psi)=-\psi''+\left[\frac{(V_\alpha')^2}{4}-\frac{V_\alpha''}{2}\right]\psi.
```

3. Since $W^2=1-S^2$, replace $(V_\alpha')^2/4=\alpha^2r^2(1-S^2)/4$ and $V_\alpha''/2=\alpha r^2S^2/2$.
4. Multiplying out $A_n^\dagger A_n$ gives $-\partial_u^2+n^2r^2-n(n+1)r^2S^2$.

The bound-state formula is the classical hyperbolic Pöschl–Teller spectrum: for integers $0\le j<n$, the discrete eigenvalues of $\mathcal H_{\alpha,r}$ are

```math
\lambda_j=r^2j(\alpha-j),\qquad \sigma_{\rm ess}(\mathcal H_{\alpha,r})=[\alpha^2r^2/4,\infty).
```

The endpoint $j=n$ is normally a threshold resonance rather than an $L^2$ bound state when $n$ is an integer. In particular for $\alpha=4$ the eigenvalues are $0$ and $3r^2$; essential spectrum begins at $4r^2$. This radial expression is not the full multidimensional gauge-theory fluctuation spectrum of BPST.

## 17. A direct Yamabe–diffusion operator identity [D,V]

This is a particularly strong interface because it compares the **same differential operator coefficients** after making all geometry and probability choices explicit.

Let $q=(D-2)/2>0$ be the critical cylinder exponent from §8, and choose the **different** diffusion-shape parameter

```math
\alpha=2(q+1).
```

Then the ground-state Hamiltonian of §16 reads

```math
\mathcal H_{2(q+1),r}=-\partial_u^2+(q+1)^2r^2-(q+1)(q+2)r^2S^2.
```

Compare it with the angular sector of the critical Yamabe/Hardy Hessian from §8:

```math
\mathcal L_{q,r}^{(\ell)}=-\partial_u^2+\ell(\ell+2q)+q^2r^2-(q+1)(q+2)r^2S^2.
```

**Theorem 17.1 [D,V] (affine conjugacy of critical Hessian and reversible diffusion).**

```math
\mathcal L_{q,r}^{(\ell)}=\mathcal H_{2(q+1),r}+\ell(\ell+2q)-(2q+1)r^2.
```

**Proof.** Subtract the displayed operators. Their differential term and hyperbolic well coincide identically. The remaining scalar offset is $q^2-(q+1)^2=-(2q+1)$ multiplied by $r^2$, plus the angular eigenvalue $\ell(\ell+2q)$.

This exact differential-expression identity links three branches at once: critical Yamabe linearization, reversible diffusion, and the Pöschl–Teller Schrödinger operator. It does **not** equate their physical meanings, boundary conditions or natural Hilbert-space domains. It is independent of the nonlinear energy quartic's smooth elliptic $j$.

### 17.1 The dimension-four BPST/Bubble meeting

At $q=1$ (hence $D=4$), the diffusion parameter is $\alpha=4$, precisely the density $\pi_{4,r}\propto S^4$ appearing in the normalized BPST charge along the logarithmic radial line. The radial Hessian identity becomes

```math
\mathcal L_{1,r}^{(0)}=-\partial_u^2+r^2-6r^2S^2=\mathcal H_{4,r}-3r^2.
```

Thus the same hyperbolic well arises from the critical Yamabe scalar Hessian and the BPST charge **diffusion ground-state transform**, with a fixed energy shift. The archived radial BPST gauge Hessian is $\mathcal H_{4,1}=-\partial_u^2+4-6S^2$ in its physical $r=1$ clock.

At $q=2$ (dimension $D=6$), choosing $\alpha=6$ gives

```math
\mathcal L_{2,r}^{(0)}=-\partial_u^2+4r^2-12r^2S^2=\mathcal H_{6,r}-5r^2.
```

The level-five **scalar** separatrix Hessian has the same order-three well and is algebraically related by this shift. It is not the same as the level-five **radial Yang–Mills gauge** Hessian, which uses the order-two well. Distinguishing the two variations is essential.

## 18. Beta coordinates, Jacobi diffusion and the Ornstein–Uhlenbeck contraction [D,V,H375]

Let $w=\tanh(ru)$ and $P=(1+w)/2$. The exact derivatives are

```math
w_u=r(1-w^2),\qquad P_u=2rP(1-P),\qquad w_{uu}=-2r^2w(1-w^2).
```

### 18.1 Pushforward of the reversible measure

The normalized probability measure $\pi_{\alpha,r}(u)\,du$ has, in the variable $P$, a Beta distribution:

```math
P\sim\mathrm{Beta}(\alpha/2,\alpha/2),\qquad dP=2rP(1-P)\,du.
```

**Proof.** Since $S^2=1-w^2=4P(1-P)$, the transformed density is proportional to $[P(1-P)]^{\alpha/2-1}\,dP$.

In particular $\alpha=4$ gives Beta$(2,2)$ with cumulative distribution

```math
\mathrm{Pr}(P'\le P)=3P^2-2P^3,
```

exactly the BPST charge polynomial. The same polynomial thus occurs as a gauge charge, a probability CDF and a radial real Monge–Ampere transport mass coordinate, **after each of those independent constructions has been supplied**.

### 18.2 The transformed Itô generator

Applying the generator to functions of $w$ gives

```math
\mathcal G_{\alpha,r}^{(w)}=r^2(1-w^2)^2\partial_w^2-(\alpha+2)r^2w(1-w^2)\partial_w.
```

It is the generator of the Itô SDE

```math
dw_t=-(\alpha+2)r^2w_t(1-w_t^2)\,dt+\sqrt2 r(1-w_t^2)\,dB_t.
```

The state-dependent time change dividing the generator by $(1-w^2)$ gives

```math
\widehat{\mathcal G}_{\alpha,r}=r^2[(1-w^2)\partial_w^2-(\alpha+2)w\partial_w].
```

For integer $\alpha+2$, the differential expression is the polar-coordinate Jacobi/Gegenbauer generator associated with an isotropic sphere of that dimension. For noninteger $\alpha$ it remains a well-defined Jacobi diffusion expression, without literally being Brownian motion on a sphere of noninteger dimension. Its stationary density after this **new clock** is proportional to $(1-w^2)^{\alpha/2}$ rather than the old $(1-w^2)^{\alpha/2-1}$.

### 18.3 Exact Ornstein–Uhlenbeck scaling limit

Take the controlled simultaneous limit

```math
\alpha\to\infty,\qquad r\to0,\qquad \alpha r^2\to\kappa>0.
```

For fixed $u$,

```math
V_\alpha(u)=\alpha\ln\cosh(ru)\to\frac{\kappa u^2}{2},\qquad \alpha r\tanh(ru)\to\kappa u.
```

Consequently the diffusion generator and its invariant density converge at the level of local coefficients and normalized measures to

```math
\mathcal G_{\rm OU}=\partial_u^2-\kappa u\partial_u,\qquad \pi_{\rm OU}(u)=\sqrt{\frac{\kappa}{2\pi}}e^{-\kappa u^2/2}.
```

The conjugate Schrödinger potential converges to the harmonic oscillator:

```math
\mathcal H_{\rm OU}=-\partial_u^2+\frac{\kappa^2u^2}{4}-\frac{\kappa}{2}.
```

The fixed-index discrete eigenvalues satisfy $r^2j(\alpha-j)\to\kappa j$, while the Pöschl–Teller continuum threshold $\alpha^2r^2/4$ diverges.

**Scope:** Strong semigroup or norm-resolvent convergence is not implied by pointwise coefficient limits without a separate operator-domain argument. This OU limit changes $\alpha$ and $r$ simultaneously; it is **not** the same as keeping a fixed Sobolev dimension $D$ and taking the critical Yamabe value $r=1$. The Ornstein–Uhlenbeck process is not “classified by an elliptic binary-quartic discriminant”: it arises here through a probability/ground-state scaling, and its Gaussian invariant measure is supplied by the chosen drift and diffusion coefficient.

## 19. Sharp Sobolev integral check in dimension four [D,V,H429–H431]

For $D=4$, $q=1$, the exact Hardy–Sobolev radial profile is

```math
U_{r,c,\mu}(\rho)=\frac{\mathrm{sech}(r\ln(\rho/c))}{2\sqrt\mu\,\rho}.
```

Its three natural integrals over $\mathbb R^4$ are

```math
\int_{\mathbb R^4}U^4\,d^4X=\frac{\pi^2}{6\mu^2r},\qquad\int_{\mathbb R^4}\rho^{-2}U^2\,d^4X=\frac{\pi^2}{\mu r}.
```

```math
\int_{\mathbb R^4}|\nabla U|^2\,d^4X=\frac{\pi^2}{\mu}\left(\frac r3+\frac1r\right).
```

**Proof, step by step.**

1. Use the four-dimensional radial volume $d^4X=2\pi^2\rho^3d\rho=2\pi^2\rho^4du$ with $u=\ln(\rho/c)$.
2. Substitute $U=S/(2\sqrt\mu\,\rho)$ and use

```math
\int_{-\infty}^{\infty}S^2\,du=\frac2r,\qquad \int_{-\infty}^{\infty}S^4\,du=\frac4{3r},\qquad\int_{-\infty}^{\infty}S^2W^2\,du=\frac2{3r}.
```

3. Since $U_\rho=(S_u-S)/(2\sqrt\mu\,\rho^2)$, its gradient energy reduces to

```math
\int|\nabla U|^2\,d^4X=\frac{\pi^2}{2\mu}\int S^2(1+rW)^2du.
```

4. The cross term integrates to zero by parity. The remaining integrals give precisely the values above.

For the Hardy quadratic functional with coefficient $(r^2-1)/\rho^2$, its value is

```math
\mathcal E_r[U]=\int[|\nabla U|^2+(r^2-1)\rho^{-2}U^2]d^4X=\frac{4\pi^2r}{3\mu}.
```

The corresponding radial quotient is

```math
\frac{\mathcal E_r[U]}{(\int U^4d^4X)^{1/2}}=\frac{4\pi\sqrt6}{3}r^{3/2}.
```

At $r=1$, this equals the classical sharp Sobolev constant $S_4=4\pi\sqrt6/3$ in the normalization $\|\nabla U\|_2^2/\|U\|_4^2$. For other $r$, the displayed value is a **radial critical-point quotient**, not automatically the unrestricted sharp constant of the Hardy–Sobolev inequality. The user's archive explicitly records this distinction.

The integral identities are a quantitative bridge from the first-order hyperbolic profile to the variational second-order PDE. They do not require classifying the profile by binary-quartic moduli, even though the separatrix also sits on the degenerate energy quartic $e=0$.

## 20. Which constructions actually use I and J? [D,V,H]

A projective quartic and its invariant ring are useful **only after a specific quartic has been constructed**. Several sharply different uses already occur in the current project.

| Construction | Actual quartic or curve | Its status | Invariants and limits |
|---|---|---|---|
| Cubic Master energy | $p^2=e+z^2-z^4$ | smooth elliptic for $e\ne0,-1/4$ | raw $I=1-12e$, $J=-2(1+36e)$; separatrix $\Delta=0$ |
| Gram/Pinney | binary quadratic $G=A X^2+2CXZ+B Z^2$ | determinant is $AB-C^2$ | artificial quartic $G^2$ has $\Delta=0$ **always** |
| Catenoid surface fundamental forms | $(X^2+Z^2)(k_1X^2+k_2Z^2)$ | smooth at nonflat nonumbilic points | $H_m=0$, $J=0$, $j=1728$, $\Delta\ne0$ |
| Eguchi–Hanson radial Monge–Ampere | $P^2-s^2=a^4$ | a **conic** | separately constructed $R^4-a^4$ gives smooth $j=1728$ but not a universal EH moduli curve |
| Intrinsic level five | $B_\theta^2=4(e_5+B^2-B^3)$ | elliptic cubic | $j=-256/[e_5(27e_5+4)]$ |
| Periodic level-five Hessian | degree-three Lamé finite-gap operator | spectral genus three | needs more than elliptic $I,J$ |
| Riemann minimal examples | marked elliptic Weierstrass/Gauss data | genus one with period conditions | its j and Gauss–Manin data belong to the chosen family, not the catenoid surface quartic |
| Four-dimensional Weyl spinor | $\Psi_{ABCD}\zeta^A\zeta^B\zeta^C\zeta^D$ | Petrov classification | I,J are curvature-spinor scalars; not automatically nonlinear energy invariants |
| Stochastic reversible diffusion | generator $\mathcal G_{\alpha,r}$ | second-order parabolic operator | **no intrinsic elliptic quartic** required |
| Ornstein–Uhlenbeck contraction | Gaussian diffusion and oscillator | quadratic potential | **no intrinsic binary quartic discriminant** governing its recurrence |

Two especially useful tests:

**Test A:** The **same** catenoid separatrix has a smooth $j=1728$ surface fundamental-form quartic and a singular $\Delta=0$ nonlinear Master energy quartic. There is no contradiction because the source-to-quartic maps differ.

**Test B:** The ordinary Hénon–Heiles Eisenhart lift in draft 050 has Weyl-spinor $I_{\mathrm W}=J_{\mathrm W}=0$ for generic type N, while its separately constructed Hessian/tidal quartic can have nonzero discriminant. The same distinction extends to the present critical/spectral/stochastic interface.

### 20.1 Discriminant zero is not synonymous with every soliton or instanton

The separatrix degeneration of the cubic Master **energy curve** is exact. The claim that all Aubin–Talenti, Eguchi–Hanson, BPST, Pöschl–Teller and OU realizations have a *single common* binary quartic with $\Delta=0$ is false.

For example the constructed Eguchi–Hanson quartic $X^4-a^4Z^4$ has $\Delta=-256a^{12}\ne0$ at $a>0$, while the canonical Master separatrix quartic is singular. The Pöschl–Teller operator arises from linearization and its **particular** Lamé spectral degeneration, whereas the OU limit is a singular scaling of a reversible diffusion generator. These are distinct limiting constructions.

Likewise the statement “$I=J=0$ means all four roots coincide and $j=0$” is false. A smooth elliptic curve with $j=0$ has $I=0$ and $J\ne0$, while the zero pair corresponds to a singular/zero quartic with **no finite smooth elliptic $j$**. A Petrov type-N Weyl quartic may have quadruple-root pattern and both invariants zero, without supplying any elliptic curve.

### 20.2 Where the modular forms actually enter

On a **specified smooth elliptic curve** in Weierstrass normal form,

```math
Y^2=4X^3-g_2X-g_3,\qquad\Delta_{\rm W}=g_2^3-27g_3^2\ne0,\qquad j=1728g_2^3/\Delta_{\rm W}.
```

Choose a complex period lattice $\Omega(\mathbb Z+\tau\mathbb Z)$ with $\mathrm{Im}\,\tau>0$. Its classical Eisenstein-series normalizations give

```math
g_2=\frac{4\pi^4}{3\Omega^4}E_4(\tau),\qquad g_3=\frac{8\pi^6}{27\Omega^6}E_6(\tau).
```

The modular weights and the scaling $\Omega$ are indispensable. Thus binary-quartic $I,J$ can be translated to $E_4,E_6$ only **after** a specific quartic-to-Weierstrass conversion and an elliptic period normalization; one cannot simply assert $I=E_4$ or $J=E_6$ for arbitrary geometry.

In the archived intrinsic level-five normalization, $g_2=4/3$ is constant, giving

```math
\Omega^4=\pi^4E_4(\tau),\qquad e_5=-\frac2{27}\left(1+\frac{E_6(\tau)}{E_4(\tau)^{3/2}}\right)
```

on a branch with consistent square-root and period choices. If the curve is written in the physical/logarithmic coordinate $u$ instead of dimensionless $\theta=ru$, its Weierstrass invariants scale by $r^4$ and $r^6$ respectively. These modular identities classify the **chosen period lattice**, not the underlying BPST bundle, Aubin–Talenti optimizer or stochastic OU generator.

## 21. An explicit counterexample to a universal scalar classification [D,C]

Use the Euclidean line with the ordinary flat metric $g=du^2$, its flat Levi-Civita connection and the trivial coordinate Weitzenbock connection. Both curvature and torsion vanish. In any fixed four-dimensional flat extension the Weyl quartic also has $I_{\rm W}=J_{\rm W}=0$.

Now choose **two different** Itô diffusions on precisely the same geometry:

```math
dX_t=\sqrt2\,dB_t,\qquad dY_t=-\kappa Y_t\,dt+\sqrt2\,dB_t,\qquad \kappa>0.
```

Their generators are

```math
\mathcal G_{\rm B}=\partial_u^2,\qquad \mathcal G_{\rm OU}=\partial_u^2-\kappa u\partial_u.
```

Brownian motion on the full line has no invariant probability density; the OU diffusion has the centered Gaussian stationary density proportional to $e^{-\kappa u^2/2}$. Both share the same background Levi-Civita curvature, chosen Weitzenbock torsion and any fixed flat Weyl-quartic invariants.

**Conclusion [C]:** Those background scalar invariants cannot determine the stochastic dynamics, the invariant measure or recurrence class. The drift/noise, generator domain and stochastic time are genuinely additional data. This counterexample invalidates any assertion that quartic I,J are automatically martingales or determine a stochastic recurrence criterion.

A second counterexample is the source's stochastic projective idea: if the Master energy parameter is explicitly made stochastic, $de_t=b(e_t)dt+\sigma(e_t)dB_t$, then the raw quartic invariant $I_e=1-12e$ obeys

```math
dI_e=-12b(e_t)\,dt-12\sigma(e_t)\,dB_t.
```

It is a local martingale only under additional conditions, for example $b=0$ with appropriate integrability, while the nonlinear $j(e_t)$ generally acquires a nonzero Itô correction. No universal stochastic conservation law follows merely from algebraic invariant theory.

## 22. The actual geometric interface: a commuting family of typed maps

The verified mechanisms can be arranged as several explicit, **not globally interchangeable**, routes.

**Linear/Ermakov route.** A two-dimensional linear solution space plus a Gram quadratic leads to a Pinney envelope. Its Wronskian gives the determinant coefficient, while its chosen logarithmic derivative gives a Riccati equation. Squaring the Gram form produces a singular quartic whose discriminant is always zero, irrespective of the nonsingular nature of the original Gram quadratic.

**Conformal/critical route.** A flat Euclidean metric plus positive conformal factor $U$ gives a Levi-Civita metric, its scalar curvature and the Yamabe equation. On a chosen local parallel coframe, the same metric gives a flat metric-compatible Weitzenbock connection and the exact identity $\mathring{\mathcal R}=-\mathbb T+\mathbb B$. Under a radial Emden–Fowler pullback, the critical Euler–Lagrange PDE becomes the level-$q$ Master cylinder ODE, whose Hessian is Pöschl–Teller.

**Kähler route.** A complex Hessian $\partial\bar\partial\mathcal K$ and prescribed determinant produce complex Monge–Ampere. Under a radial unit-determinant ansatz, the resulting $P^m=s^m+a^{2m}$ specializes to the local Eguchi–Hanson radial potential at $m=2$, with an independently chosen $\cosh$ coordinate revealing Pinney. The local Kähler Ricci-flatness is a metric theorem, not a BPST gauge field or automatic teleparallel torsion identity.

**Gauge and transport route.** SU(2) self-duality for a *specified nonflat* BPST gauge connection gives a logistic coefficient and quartic curvature density. The normalized radial density pushes to a Beta$(2,2)$ law and has a cubic CDF $Q=3P^2-2P^3$. A separate real Monge–Ampere convex transport has radial target radius $Q^{1/4}$. The shared $Q$ is a constructed mass-coordinate identity, not a connection isomorphism.

**Spectral/stochastic route.** The critical Hessian and reversible diffusion ground-state transform yield the *same* hyperbolic Pöschl–Teller well up to a constant shift. The reversible diffusion pushes forward to a Beta law under the logistic chart and, after a separate state-dependent time change, to a Jacobi/Gegenbauer generator. A simultaneous parameter contraction yields the Ornstein–Uhlenbeck/harmonic-oscillator pair. None of these requires a common smooth elliptic quartic.

At every arrow, track: input manifold, radial/logarithmic clock, resolution $r$, scale $c$, amplitude $\mu$, dimension $D$, connection choice, functional or generator, discriminant/real branch where applicable, and analytic domain.

## 23. Independent verification and reproducibility [V]

The following checks were performed independently by exact SymPy manipulations and elementary derivative/integration proofs while drafting this file:

1. Expanding the Gram-square quartic gives $I=16(AB-C^2)^2$, $J=128(AB-C^2)^3$, and $\Delta=0$ identically.
2. The Master energy quartic has $I=1-12e$, $J=-2(1+36e)$ and $\Delta=-16e(1+4e)^2$.
3. The arbitrary-$q$ derivative of $S^q$ gives precisely $q^2r^2S^q-q(q+1)r^2S^{q+2}$.
4. The Pinney envelope satisfies $J_{uu}=r^2(J-2C)$ and $J_u^2=r^2(J^2-4CJ-4(AB-C^2))$.
5. The radial complex Monge–Ampere potential $\mathcal K(s)$ in §11 differentiates to $\mathcal K_s=\sqrt{s^2+a^4}/s$ and has determinant one.
6. The conformal flat-frame formulas for $\mathbb T$, $\mathbb B$ and $\mathring{\mathcal R}$ were checked algebraically; on the Aubin–Talenti factor they simplify to $\mathring{\mathcal R}=4\mu D(D-1)$ with the explicit position-dependent torsion of §7.2.
7. The derivative of the BPST charge $Q=3P^2-2P^3$ is $(3r/4)S^4$ in the appropriate radial pullback.
8. The real Monge–Ampere transport satisfies $Q'=12\rho^3c^4/(\rho^2+c^2)^4$ and $\det D^2\Phi=Q'/(4\rho^3)$.
9. The reversible ground-state conjugation gives the Pöschl–Teller potential $\alpha^2r^2/4-\alpha(\alpha+2)r^2S^2/4$ exactly.
10. Substituting $\alpha=2(q+1)$ reproduces the Yamabe Hessian well and gives the affine shift $\ell(\ell+2q)-(2q+1)r^2$.
11. The logistic coordinate change satisfies $P_u^2=4r^2P^2(1-P)^2$ and the Itô drift of §18.
12. The dimension-four sharp Sobolev integrals of §19 follow from the elementary definite integrals of $S^2$, $S^4$ and $S^2W^2$.

These are **equation checks**, not complete independent audits of every archived claim or global theorem. Especially, the archive's quoted spectral theorems, sharpness and compactification arguments still require their classical hypotheses. Operator domains, spectral self-adjoint extensions and stochastic semigroup convergence are not fully certified by the checks above.

### 23.1 Suggested minimal computational checks for subsequent review

Use exact symbolic parameters $r,\mu,c>0$, $q>0$, and the identity $\tanh^2+\mathrm{sech}^2=1$. Verify separately: Gram quartic coefficients before invoking the discriminant formula; the radial Laplacian after conjugation by $\rho^{-q}$; the complex Hessian determinant from its eigenvalues; the chosen teleparallel torsion contractions and divergence (not merely a guessed scalar curvature identity); the Pöschl–Teller operator coefficients; and the Itô transformation with volatility $\sqrt2$.

For high-confidence spectral results also specify which Hilbert space and boundary endpoints are being used, especially at the Hardy inverse-square singularity and the noncompact catenoid/Eguchi–Hanson ends. For geometric global claims check smooth extension, topology and frame parallelizability beyond one coordinate chart.

## 24. Proposed foundational theorem and consolidation agenda [O]

**Candidate theorem A:** For every local conformally flat metric $g=e^{2h}\eta$, the chosen flat-frame Weitzenbock connection has explicit vector-type torsion; its quadratic scalar and divergence reproduce the Levi-Civita conformal scalar curvature. For critical $r=1$ Aubin–Talenti bubbles the curvature is constant while the preferred torsion scalar is position-dependent. Proof: §7; verify sign conventions and global chart scope before promotion.

**Candidate theorem B:** The Gram-squared quartic has invariant pair $(16\Delta_G^2,128\Delta_G^3)$ but identically zero quartic discriminant. Proof: §3. This precisely separates Ermakov–Pinney's quadratic determinant from the smooth nonlinear energy elliptic moduli.

**Candidate theorem C:** Under the specified positive reversible density $\mathrm{sech}^{2(q+1)}(ru)\,du$, the diffusion's ground-state Schrödinger operator is the critical Yamabe cylinder Hessian in harmonic sector $\ell$, shifted by $\ell(\ell+2q)-(2q+1)r^2$. Proof: §§8, 16–17. The operator expression is exact; full spectral equivalence requires matching domains.

**Candidate theorem D:** The normalized BPST charge, the Beta$(2,2)$ CDF of the logarithmic radial density, and the real radial Monge–Ampere transport mass coordinate coincide as $Q(P)=3P^2-2P^3$. Proof: §§12, 14, 18. The interpretations and associated bundles remain separate.

**Candidate theorem E:** The radial complex Monge–Ampere determinant gives $P^m=s^m+a^{2m}$, and $m=2$ admits a local change of radial coordinate exposing the Pinney envelope. Proof: §11. The identification with the complete Eguchi–Hanson metric requires the separate classical smooth quotient/resolution.

**Further research tasks:**

1. Classify all *natural*, functorial assignments of a binary quartic to the canonical critical or Kähler data, and prove which maps retain the marked differential rather than just an abstract elliptic $j$.
2. Extend the conformal teleparallel formula to non-conformally-flat cohomogeneity-one Eguchi–Hanson frames with an explicitly fixed flat inertial connection; compute the full tensorial contorsion and LC curvature, avoiding an invented SU(2) gauge equivalence.
3. Determine how the exact Yamabe Hessian–diffusion ground-state transform interacts with angular decomposition, index theory and the known $r_{D,\ell}$ thresholds; account for distinct operator domains before claiming a full spectral isomorphism.
4. Analyze the time-changed Jacobi diffusion on the compact $w$ interval, its endpoint classification and global stochastic domain; establish precise semigroup convergence to OU if the scaling limit is to be promoted from formal/local to spectral.
5. Investigate the level-nine genus-two nonlinear curve and finite-energy spectral branching alongside the $l=5$ Lamé genus-three spectral curve; identify which higher-genus Siegel invariants, not quartic I,J alone, actually classify the selected families.
6. Compare the BPST gauge self-duality operator with the Yamabe scalar Hessian through an **actual intertwiner and bundle map**. A shared Pöschl–Teller radial coefficient or conformal density is not sufficient.
7. Develop boundary-sensitive Sturm–Liouville and Itô domains in the original multiplicative coordinate $x$, keeping $c,r$ visible in unitary changes and weighted measures.
8. Test whether the teleparallel torsion coefficients of the Aubin–Talenti conformal metric can be organized into a meaningful projective connection after specifying an explicit Cartan/Gauss-map lift; avoid assuming universal $I,J$ Casimirs.

### Proposed destinations after mathematical review

- **Layer I:** Gram/Pinney determinant versus quartic I,J; canonical levels, energy discriminants, Riccati/Schwarzian and clocks.
- **Layer II:** conformal Levi-Civita/Weitzenbock theorem, Kähler/complex Monge–Ampere geometry, gauge versus spin connections, and global frame/topology qualifications.
- **Layer III:** critical Hardy–Sobolev and Yamabe reductions, Aubin–Talenti profiles, real Monge–Ampere transport, Sturm–Liouville/PT/Lamé operators and marked spectral curves.
- **Layer IV:** chosen Itô/Fokker–Planck generators, Beta/Jacobi transformations, OU limit, optional physical gauge/gravitation interpretations only with independently specified actions and fields.

## 25. Sources and exact attribution

**Project sources:** The historical ZIP includes the detailed source-status table of H371–H376 in *bpst-yamabe-eguchi-hanson.md* (including checked radial complex MA, BPST charge, reversible diffusion, and unexamined global sharpness assumptions); H429–H447 in *hardy-master-lame-genus-two.md* (including the four-dimensional Hardy–Sobolev integral data, Lamé spectra and genus-two modular comparisons); H173–H176 in *conformal-and-probabilistic-readings.md*; and the 2026-11-16_v2 reference §§21–24, 32. The live main-branch drafts 030, 040 and 050 provide the typed connection and invariant-theory conventions. Earlier ledger verification flags have **different evidence levels**: exact symbolic checks do not automatically prove global analytic classification theorems.

**Classical and external mathematics:**

- Pinney nonlinear superposition and its Wronskian determinant: E. Pinney's classical result and https://mathworld.wolfram.com/ErmakovEquation.html .
- Aubin–Talenti sharp critical Sobolev extremals and stereographic Yamabe geometry: classical Aubin/Talenti/Yamabe theory; see also the archived H429–H431 proof register for the exact normalization and unrestricted-minimizer caveat.
- Radial Calabi–Eguchi–Hanson Ricci-flat Kähler construction: https://www.claymath.org/library/monographs/cmim04c.pdf and https://link.springer.com/article/10.1007/s00022-025-00763-8 . Global ALE completion is separate from local determinant-one calculus.
- BPST instanton as a nonflat SU(2) self-dual connection: standard BPST theory and https://www2.yukawa.kyoto-u.ac.jp/~katsushi.ito/summer2004.pdf .
- Ground-state transformation between Ornstein–Uhlenbeck diffusion and harmonic oscillator: https://repository.tudelft.nl/record/uuid%3A08ad4a94-483d-46db-8840-6f73c3e48a70 .
- Teleparallel torsion/contorsion, flat inertial spin connections and the curvature-boundary identity: https://www.mdpi.com/2218-1997/7/5/114 ; comparison with live SF-DRAFT-040.
- Pöschl–Teller and Lamé spectral calculations: historical H429–H447 and the classical exactly-solvable hypergeometric/finite-gap theory they cite. The identity in §17 is derived here algebraically; no claim is made that this general framework is novel.

**Final mathematical boundary:** Levi-Civita curvature, a chosen flat Weitzenbock connection and binary-form invariant theory form a useful **algebro-geometric interface** only after specifying the metric, coframe, quartic/curve, functional or operator, domain and clock. There is no complete universal classification of Yamabe, Eguchi–Hanson, BPST, Sturm–Liouville or Itô dynamics by a common $(I,J,\mathbb T)$ triple. The exact interfaces identified here are nonetheless strong enough to guide the organization of the foundational layers without imposing theoretical-physics interpretations.
