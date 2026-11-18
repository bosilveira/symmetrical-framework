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
