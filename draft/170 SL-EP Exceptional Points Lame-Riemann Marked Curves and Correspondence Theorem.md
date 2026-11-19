---
id: SF-DRAFT-170
title: SL–EP Exceptional Points, Lamé–Riemann Marked Curves, and a Correspondence Theorem
status: provisional
created: 2026-11-19
proposed_layers: [I, II, III]
depends_on: [SF-I-020, SF-DRAFT-080, SF-DRAFT-090, SF-DRAFT-100, SF-DRAFT-110, SF-DRAFT-120, SF-DRAFT-130, SF-DRAFT-140, SF-DRAFT-150, SF-DRAFT-160]
related_claims: [H95, H100, H102, H169, H172, H177, H183, H299, H391, H421, H424, H466, H467, H468, H469, H470, H471, H472]
---

# 170 SL–EP Exceptional Points, Lamé–Riemann Marked Curves, and a Correspondence Theorem

**Status:** Provisional research manuscript, not incorporated into canonical CLAIMS. [D] proved in this draft; [V] exact symbolic/numerical verification; [K] established theorem with stated assumptions; [H] archived result retaining its source verification level; [C] correction/counterexample; [O] open. No physical implementation or historical novelty is inferred from equations alone.

**Question.** Which parts of the SL–Riccati–EP, binary-quartic, finite-gap, Darboux–Crum, catenoid/helicoid, Riemann-minimal-example and weighted-Hilbert frameworks can be organized into a precise theorem? When is a Jordan block an operator exceptional point? Are the two possible spectral-gap degenerations the same? Can the one-gap Lamé spectral curve be mapped with marked differentials to the **whole real Riemann elliptic family**, rather than only to the symmetric $j=1728$ Pinney member?

**Principal answers.** The local SL–Riccati–EP correspondence is an exact finite-dimensional Lie–Hamilton/symmetric-square system for a *prescribed real* linear carrier. Self-adjointness is a separate global Hilbert-domain condition. A nontrivial Jordan **transfer** matrix need not be an operator defect; conversely a genuine non-self-adjoint periodic eigenvalue defect can be constructed explicitly from Bessel monodromy. For the one-gap Lamé family there are two **different** nodal endpoints: a gap closes at $m=0$ with semisimple free monodromy, while an allowed band collapses at $m=1$ to the reflectionless PT bound state. The new selected modulus assignment $m=(1+\lambda_R^2)^{-1}$ gives a real **affine isomorphism of smooth elliptic curves** between the Lamé spectral curve (with a declared sign convention) and the real Riemann-minimal-example elliptic curve for every $\lambda_R>0$. It pulls back the full meromorphic Weierstrass triple into the two-dimensional span of marked spectral differentials, *without asserting that the physical quasimomentum differential and the geometric height differential automatically coincide*. The order-one spectral-node catenoid/helicoid map from draft 160 is recovered at the soliton endpoint.

**Project sources actually reviewed:** November 18 backup ZIP, including the verified H100/H299 Lax–Novikov identities, H466–H472 Riemann Gauss–Manin/Weierstrass/period formulas, and the Lamé special-loci reference; GitHub drafts 120, 130, 140, 150, and 160. External Hill, Gasymov/Bessel, Lamé and Riemann-minimal-surface literature is listed in §27. The affine elliptic curve map, branch-point correspondence, $j$ identity and differential pullbacks were verified with exact SymPy polynomial arithmetic.

## 1. Typed objects: five different monodromies and spectra

| Object | Data | Mathematical content |
|---|---|---|
| Instantaneous matrix $A(u)$ | linear carrier at a specified $u$ | local elliptic/hyperbolic/nilpotent type |
| Spatial transfer matrix $M(\lambda)$ | transport over a given interval | Floquet multipliers, eigenvalue characteristic determinant and transfer Jordan form |
| Hilbert operator $L_{\mathcal D}$ | differential expression plus weight, interval and domain | self-adjointness, operator eigenvalue Jordan chains, resolvent poles |
| Gauss–Manin/Picard–Lefschetz monodromy | analytic continuation in a curve modulus | degeneration of marked homology cycles and logarithmic periods |
| Nodal spectral curve | a polynomial $\eta^2=P(E)$ with collided roots | algebraic singularities and generalized Jacobian, not automatically an operator defect |

The phrase **spectral exceptional point** is reserved for an *isolated non-semisimple eigenvalue of a specified closed operator*. A Jordan transfer matrix, a node of an auxiliary spectral curve, and a Gauss–Manin unipotent matrix are different mathematical properties.

## 2. Coordinates and parameters must remain typed

Fix the canonical Symmetrical Framework variables

```math
x,r,c,\mu>0,\quad u=\ln(x/c),\quad x=ce^u,\quad S=\mathrm{sech}(ru),\quad W=\tanh(ru),\quad f_\mu=\frac{S}{2\sqrt\mu\,x}.
```

For general Sturm–Liouville use $p(x),w(x)>0$, real $q_0(x)$, a **spectral** parameter $\lambda$, and an **operator domain** $\mathcal D$. For Ermakov–Pinney use a positive amplitude $a(t)$ and strength $k_{\rm EP}$, neither of which is an eigenvalue. For the one-gap Lamé curve use elliptic parameter $m\in(0,1)$ and **spectral energy** $E$. For the Riemann minimal-example family use geometric modulus $\lambda_R>0$, $k_R=\lambda_R^{-1}-\lambda_R$, Gauss coordinate $g_R$, and immersion scale $A_R>0$. The Riemann modulus $\lambda_R$, spectral $E$, scattering $k_{\rm sc}$, original amplitude $\mu$ and independent coordinate $u$ are never interchangeable.

## 3. The universal weighted Liouville equivalence [D,K]

For the real scalar expression

```math
-(p y_x)_x+q_0y=\lambda wy,\qquad p,w>0,
```

introduce the coordinate and half-density

```math
t=\int_{x_*}^x\sqrt{\frac{w(s)}{p(s)}}ds,\quad\chi(x)=(pw)^{1/4},\quad\psi(t)=\chi(x)y(x).
```

**Theorem 3.1 [D,K].** For sufficiently regular coefficients,

```math
-\psi_{tt}+V_L(t)\psi=\lambda\psi,\quad V_L(t)=q_0/w+\chi_{tt}/\chi,\quad\int|y|^2w\,dx=\int|\psi|^2dt.
```

The weighted Wronskian is conserved and transported exactly:

```math
p(y_1y_{2,x}-y_{1,x}y_2)=\psi_1\psi_{2,t}-\psi_{1,t}\psi_2.
```

**Proof.** Substitute $\psi=\chi y$, cancel the first derivative by the selected $\chi$, and use $\chi^2dt=\sqrt{pw}\sqrt{w/p}\,dx=w\,dx$. The determinant identity follows by the same cancellation. To conclude **unitary operator equivalence**, the self-adjoint domain must also be transported.

For the original carrier,

```math
p=x^3,\quad w=x,\quad q_0=(r^2-1)x,\quad t=u=\ln(x/c),\quad\chi=x,
```

giving

```math
U_cf=xf(x),\qquad U_c\tau_xU_c^{-1}=-\partial_u^2+r^2,\qquad\|f\|^2_{L^2(xdx)}=\|U_cf\|^2_{L^2(du)}.
```

The full-line free carrier is self-adjoint with purely continuous spectrum $[r^2,\infty)$. The localized nonlinear original profile is **not** a zero eigenfunction of this positive free carrier.

## 4. Local Riccati, positive Pinney, and symmetric-square equivalence [D,K]

For a **prescribed real** $V(t)$, let

```math
-\phi_{tt}+V(t)\phi=\lambda\phi,\qquad Q(t)=V(t)-\lambda.
```

If a complex carrier $\Phi=a e^{i\theta}$ never vanishes and $a>0$, its current is constant:

```math
j=\mathrm{Im}(\bar\Phi\Phi_t)=a^2\theta_t,\quad j_t=0,\quad a_{tt}=Qa+j^2a^{-3}.
```

Thus the **scattering- or carrier-normalized Pinney strength** is $k_{\rm EP}=j^2$. More generally, for independent real carrier solutions $\phi_1,\phi_2$ with constant Wronskian $\mathscr W$ and a constant symmetric Gram matrix $G$,

```math
J=a^2=A\phi_1^2+2C\phi_1\phi_2+B\phi_2^2,\qquad k_{\rm EP}=(AB-C^2)\mathscr W^2.
```

If $G$ is **positive definite**, then $J>0$ globally on the common interval because independent carrier solutions never vanish simultaneously. A merely positive determinant without a positive quadratic form is not enough to select a positive real envelope.

The *linear* third-order symmetric-square system and its conserved invariant are

```math
J_{ttt}-4QJ_t-2Q_tJ=0,\qquad 2JJ_{tt}-J_t^2-4QJ^2=4k_{\rm EP}.
```

On nonvanishing charts the logarithmic derivative $z=\Phi_t/\Phi$ satisfies

```math
z_t+z^2=Q,\qquad z=a_t/a+ij/a^2.
```

**Scope [C].** This equivalence concerns one *selected nonlinear envelope equation* and a real rank-two carrier. It does **not** linearize arbitrary nonlinear differential equations, fix a global spectral domain, or make the Pinney equation a linear operator eigenvalue problem.

## 5. A finite Lie–Hamilton closure is present, but the potential needs separate data [D,H]

On the phase plane $(a,p_a)$ with $\{a,p_a\}=1$ define

```math
H_0=(p_a^2+k_{\rm EP}a^{-2})/2,\quad D=ap_a/2,\quad K=a^2/2,\quad H(t)=H_0+(\lambda-V(t))K.
```

Then

```math
\{D,H_0\}=H_0,\quad\{D,K\}=-K,\quad\{K,H_0\}=2D,\quad H_0K-D^2=k_{\rm EP}/4.
```

The three generators close under the Poisson bracket and give the exact $\mathfrak{sl}_2$ Lie–Hamilton/symmetric-square dynamics of drafts 100/130. For an **arbitrary prescribed** coefficient $V(t)$ this remains a nonautonomous finite Lie system. It does **not** supply a universal autonomous finite-dimensional differential equation for $V$. The selected Pöschl–Teller potential satisfies one, or a stationary-KdV/finite-gap reduction can be imposed as an additional spectral constraint.

## 6. Self-adjointness is determined by operator domain, not by Pinney positivity [D,C]

For $\tau=w^{-1}[-(p\partial_x)'+q_0]$ the exact Green boundary form is

```math
\langle y,\tau z\rangle_w-\langle\tau y,z\rangle_w=[p(\bar y_xz-\bar yz_x)]_{\partial I}.
```

A real formally symmetric expression need not be self-adjoint until its domain is specified; a complex boundary parameter can destroy symmetry without altering the interior equation or its real Pinney family. Conversely a real self-adjoint operator can have negative eigenvalues, scattering flux, and a defective **transfer matrix**.

The canonical inversion $x\mapsto c^2/x$ becomes parity $u\mapsto-u$. In the original coordinate the even/odd half-line boundary conditions are

```math
cf_x(c)+f(c)=0\quad(\mathrm{even}),\qquad f(c)=0\quad(\mathrm{odd}),
```

provided a parity-preserving self-adjoint realization and a half-line restriction have been declared. The equal halves of the original improper integral come from an even positive density, **not** from this spectral domain choice.

## 7. Genuine exceptional eigenvalues and resolvent poles [D,K]

Let $L_{\mathcal D}$ be a closed Hilbert operator with compact resolvent and isolated eigenvalue $\lambda_0$. A nontrivial operator Jordan chain consists of

```math
(L_{\mathcal D}-\lambda_0)\psi_0=0,\quad(L_{\mathcal D}-\lambda_0)\psi_1=\psi_0,\quad\psi_0\ne0,\quad\psi_0,\psi_1\in\mathrm{Dom}(L_{\mathcal D}).
```

The resolvent pole order at $\lambda_0$ equals the **maximal Jordan-chain length** on the finite-dimensional Riesz spectral subspace. A length-two chain with no longer chain gives a double pole. A **semisimple** eigenvalue of algebraic multiplicity two has a rank-two spectral projection but only a simple pole.

For a self-adjoint operator no such chain can exist, since

```math
\|\psi_0\|^2=\langle(L-\lambda_0)\psi_1,\psi_0\rangle=\langle\psi_1,(L-\lambda_0)\psi_0\rangle=0.
```

Thus a truly defective isolated eigenvalue is incompatible with self-adjointness; this says nothing about the Jordan form of a *spatial transfer matrix*.

## 8. Floquet discriminant and the exact missing condition [D,K,C]

For a periodic Hill equation $-\phi''+V\phi=\lambda\phi$, let $M(\lambda)\in SL(2,\mathbb C)$ transport Cauchy data over one spatial period $L$, and $\Delta(\lambda)=\mathrm{tr}\,M(\lambda)$.

For a periodic ($\sigma=+1$) or antiperiodic ($\sigma=-1$) Hilbert realization on $[0,L]$, the characteristic determinant is

```math
D_\sigma(\lambda)=\det(M(\lambda)-\sigma I)=2-\sigma\Delta(\lambda).
```

A root obeys $\Delta(\lambda_0)=2\sigma$. A **double** root additionally obeys $\Delta'(\lambda_0)=0$, but this is not sufficient for a defective operator eigenvalue: one must know the geometric eigenspace and the operator Jordan chain.

The boundary correction in the Green function uses

```math
(M-\sigma I)^{-1}=\frac{\mathrm{adj}(M-\sigma I)}{2-\sigma\Delta(\lambda)}.
```

If the denominator vanishes quadratically but $M(\lambda_0)=\sigma I$, the adjugate vanishes too; a **semisimple** double eigenvalue can have only a simple resolvent pole. If $M(\lambda_0)\ne\sigma I$ is Jordan and the characteristic zero is **exactly** double, the adjugate is nonzero and the regular boundary operator has a true double resolvent pole.

**Counterpoint:** For quasiperiodic multiplier $e^{i\vartheta}$ the characteristic equation is $\Delta=2\cos\vartheta$, not necessarily $\pm2$. For separated Robin or other domains the characteristic determinant is different again. Hence the proposed equalities $\Delta=\pm2$, $\Delta'=0$ are neither a universal necessary condition nor a universal sufficient condition for an operator exceptional point.
