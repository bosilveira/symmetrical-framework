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

For an integer dimension $`D\ge3`$ use the critical exponent parameter

```math
q=\frac{D-2}{2}>0,\qquad D=2q+2,\qquad 2^*=\frac{2D}{D-2}=2+\frac2q.
```

The archival level convention $`l=2q+1`$ gives $`D=l+1`$. These are **chosen parameter dictionaries**, not claims that all such dimensions have the same spinor or binary-quartic geometry.

The general zero-energy power profile in the dimensionless cylinder is proportional to $`S^q`$. Use the normalized amplitude

```math
Y_q(u)=\left(\frac{S}{2\sqrt\mu}\right)^q.
```

Then, in the same logarithmic coordinate,

```math
Y_{q,uu}=q^2r^2Y_q-4\mu q(q+1)r^2Y_q^{1+2/q}.
```

This follows by differentiating $`S^q`$, applying $`W^2=1-S^2`$, and noting $`Y_q^{2/q}=S^2/(4\mu)`$.

## 3. Ermakov–Pinney begins with a binary quadratic, not the elliptic binary quartic [D,V,K]

The normal-form linear backbone is

```math
\psi_{uu}-\frac{r^2}{4}\psi=0,\qquad \psi_+=e^{ru/2},\qquad\psi_-=e^{-ru/2}.
```

Its Wronskian, in the stated order, is

```math
\mathscr W=\psi_+\psi_-'-\psi_+'\psi_-=-r.
```

Let $`A,B,C\in\mathbb R`$ and define a quadratic Gram form and positive envelope where possible:

```math
G(X,Z)=AX^2+2CXZ+BZ^2,\qquad\Delta_G=AB-C^2.
```

```math
Y(u)^2=G(\psi_+,\psi_-)=Ae^{ru}+2C+Be^{-ru},\qquad Y>0.
```

**Theorem 3.1 [D,V,K] (Pinney from Wronskian and Gram determinant).** On any interval where $`Y>0`$,

```math
Y_{uu}=\frac{r^2}{4}Y+r^2\Delta_GY^{-3}.
```

**Proof, step by step.** Put $`J=Y^2`$. The two exponential functions satisfy $`J_{uu}=r^2(J-2C)`$ and

```math
J_u^2=r^2(J^2-4CJ-4\Delta_G).
```

Differentiate $`Y=\sqrt J`$:

```math
Y_{uu}=\frac{J_{uu}}{2Y}-\frac{J_u^2}{4Y^3}=\frac{r^2}{4}Y+\frac{r^2\Delta_G}{Y^3}.
```

This is Pinney's nonlinear superposition principle, whose general coefficient is $`(AB-C^2)\mathscr W^2`$ for an arbitrary fundamental pair of the same linear equation. The determinant is an invariant of the chosen **binary quadratic**, not the elliptic energy curve's $`I`$.

### 3.1 An exact invariant-theoretic comparison

Square the Gram polynomial to obtain a binary quartic $`F_G=G^2`$. In the archived **raw quartic** convention,

```math
I(F)=12af-3bd+c_2^2,\qquad J(F)=72ac_2f+9bc_2d-27ad^2-27fb^2-2c_2^3
```

for $`F=aX^4+bX^3Z+c_2X^2Z^2+dXZ^3+fZ^4`$.

**Theorem 3.2 [D,V] (the Gram-square quartic is always singular).**

```math
I(F_G)=16\Delta_G^2,\qquad J(F_G)=128\Delta_G^3,\qquad\Delta(F_G)=\frac{4I(F_G)^3-J(F_G)^2}{27}=0.
```

**Proof.** Expand

```math
G^2=A^2X^4+4ACX^3Z+(2AB+4C^2)X^2Z^2+4BCXZ^3+B^2Z^4.
```

Substitute these five coefficients into the raw formulas and factor the result. Independently, $`G^2`$ has repeated projective roots even when $`G`$ has two distinct roots, so its polynomial discriminant must vanish. The exact powers above record how its $`I,J`$ remember the *quadratic* determinant while **failing** to provide a smooth elliptic curve.

Thus Ermakov–Pinney's determinant can be expressed using quartic invariant polynomials after a chosen squaring map, but it is **not** an elliptic binary quartic modulus. The interface explicitly distinguishes Gram determinants, Master energy quartics and Weyl-spinor quartics (draft 050).

## 4. A genuine elliptic quartic arises from a specified nonlinear first integral [D,V,H429]

The normalized cubic Master energy polynomial is

```math
F_e(X,Z)=-X^4+X^2Z^2+eZ^4.
```

Its raw invariants, discriminant and smooth $`j`$ are

```math
I_e=1-12e,\qquad J_e=-2(1+36e),\qquad \Delta_e=-16e(1+4e)^2.
```

```math
j_e=-16\frac{(1-12e)^3}{e(1+4e)^2},\qquad e\notin\{0,-1/4\}.
```

These formulas are independently checked and recorded in archival H429. For $`e\ne0,-1/4`$, the affine energy curve $`p^2=e+z^2-z^4`$ is generically an elliptic curve. At $`e=0`$ its separatrix gives $`z=S`$, and the polynomial is singular. At $`e=-1/4`$ the roots merge differently (the equilibrium energy). The limits $`j_e\to\infty`$ at singular energies are statements about elliptic degeneration, not general curvatures of all accompanying geometries.

**Negative control:** The canonical catenoid's *fundamental-form* quartic has $`j=1728`$ and **nonzero** discriminant at every finite nonflat point (draft 050), while the very same profile's cubic **energy** quartic at $`e=0`$ has **zero** discriminant. Consequently the slogan “every localized profile has $`\Delta=0`$” is false without specifying the quartic being classified.

## 5. Sturm–Liouville is a weighted differential expression plus its operator domain [D,K]

A scalar regular or singular Sturm–Liouville differential expression has

```math
-(p(x)y')'+q_0(x)y=\lambda w(x)y,\qquad p>0,\quad w>0.
```

This is not the same object as the Master power parameter $`q`$: here $`q_0`$ is an arbitrary coefficient. Set

```math
t=\int^x\sqrt{w(s)/p(s)}\,ds,\qquad \rho=(pw)^{1/4},\qquad \psi(t)=\rho(x)y(x).
```

Direct differentiation gives the Liouville normal form

```math
-\psi_{tt}+\left(\frac{q_0}{w}+\frac{\rho_{tt}}{\rho}\right)\psi=\lambda\psi.
```

The positive weight defines the formal Hilbert-space norm $`\int |y|^2w\,dx=\int|\psi|^2dt`$ on corresponding intervals. Boundary conditions, limit-point/limit-circle endpoints and self-adjoint realization must still be specified. The transformation alone does not classify the spectrum.

For the normal form $`\psi_{tt}=(V-\lambda)\psi`$ and nonvanishing $`\psi`$, the logarithmic derivative $`h=\psi_t/\psi`$ satisfies

```math
h_t+h^2=V-\lambda.
```

For two independent solutions with projective ratio $`F=\psi_1/\psi_2`$,

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
