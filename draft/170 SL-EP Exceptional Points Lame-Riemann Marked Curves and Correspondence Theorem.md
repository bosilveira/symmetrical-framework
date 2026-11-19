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

## 9. First exact counterexample: free SELF-ADJOINT Hill operator [D,V,C]

On $L^2([0,L])$, let $L_0=-\partial_u^2$ with standard real periodic or antiperiodic $H^2$ domain. At spectral value $\lambda$ the transfer matrix and discriminant are

```math
M_0(\lambda)=\begin{pmatrix}\cos(\sqrt\lambda L)&\sin(\sqrt\lambda L)/\sqrt\lambda\\-\sqrt\lambda\sin(\sqrt\lambda L)&\cos(\sqrt\lambda L)\end{pmatrix},\qquad\Delta_0(\lambda)=2\cos(\sqrt\lambda L).
```

At the bottom point $\lambda=0$,

```math
M_0(0)=\begin{pmatrix}1&L\\0&1\end{pmatrix},\qquad\Delta_0(0)=2,\qquad\Delta_0'(0)=-L^2\ne0.
```

The spatial matrix has a nontrivial Jordan block, but the periodic operator is self-adjoint and its zero eigenvalue is **simple**. The resolvent pole is simple.

At every positive free band-edge value $\lambda_n=(n\pi/L)^2$ ($n\ge1$),

```math
M_0(\lambda_n)=(-1)^nI,\qquad\Delta_0(\lambda_n)=2(-1)^n,\qquad\Delta_0'(\lambda_n)=0.
```

The corresponding *periodic* ($n$ even) or *antiperiodic* ($n$ odd) eigenvalue has geometric multiplicity **two**, spanned by $\sin(n\pi u/L)$ and $\cos(n\pi u/L)$. It is **semisimple**, and its resolvent still has only a simple pole.

**Theorem 9.1 [D,V,C].** Neither a Jordan spatial transfer matrix alone, nor a double root of $\Delta-2\sigma$ alone, implies a spectral exceptional point. The first fails at $\lambda=0$; the second fails at every positive $\lambda_n$.

For the free period $L=\pi/r$, the $n=1$ **antiperiodic** level at $\lambda=r^2$ has $M=-I$ and $\Delta'=0$. Yet the real nodeless Pinney envelope $a=1$, from the complex linear carrier $\Phi=e^{iru}$, satisfies

```math
a_{uu}=-r^2a+r^2a^{-3},\qquad j=r,\qquad k_{\rm EP}=r^2.
```

It is not a homoclinic separatrix: it is a stationary positive envelope of an oscillatory linear carrier. This explicitly refutes the idea that Pinney positivity alone detects a unique spectral boundary between periodic and hyperbolic dynamics.

## 10. Second exact counterexample: a TRUE non-self-adjoint periodic exceptional point [D,K,V]

Choose the **complex periodic** potential $V_\alpha(u)=\alpha e^{2iu}$, $\alpha>0$, on the fixed interval $u\in[0,2\pi]$, and the periodic domain

```math
L_\alpha=-\partial_u^2+\alpha e^{2iu},\quad \mathcal D_{\rm per}=\{y\in H^2(0,2\pi):y(2\pi)=y(0),\ y_u(2\pi)=y_u(0)\}.
```

This operator is **not self-adjoint**, because its potential is nonreal for generic real $u$. It has compact resolvent, so isolated periodic eigenvalues have finite algebraic multiplicity.

Set the complex Bessel argument and order

```math
z=\sqrt\alpha\,e^{iu},\qquad \nu^2=\lambda.
```

The spectral equation reduces by exact differentiation to

```math
z^2Y_{zz}+zY_z+(z^2-\nu^2)Y=0.
```

Therefore the fundamental solutions are Bessel functions $J_\nu(z),J_{-\nu}(z)$ for noninteger $\nu$; analytic continuation as $u$ increases from $0$ to $2\pi$ rotates $z$ once about zero. The two Floquet multipliers are $e^{\pm2\pi i\nu}$, giving the exact discriminant

```math
\Delta_\alpha(\lambda)=2\cos(2\pi\sqrt\lambda).
```

This is the **same discriminant as a free operator on a circle of length $2\pi$**, but the operator eigenvector structure need not agree.

### 10.1 Integer spectral order produces a genuine Jordan block

At every $\lambda_n=n^2$ with $n=1,2,\ldots$, the periodic Bessel function $J_n(z)$ is a genuine eigenfunction. The second integer-order solution $Y_n(z)$ obeys the classical Bessel analytic continuation formula

```math
Y_n(ze^{2\pi i})=Y_n(z)+4iJ_n(z).
```

Thus, in the local fundamental basis $(J_n,Y_n)$,

```math
M_\alpha(n^2)\sim\begin{pmatrix}1&4i\\0&1\end{pmatrix},\qquad M_\alpha(n^2)\ne I,\qquad (M_\alpha(n^2)-I)^2=0.
```

Meanwhile the characteristic zero is **exactly double**:

```math
2-\Delta_\alpha(\lambda)=\frac{\pi^2}{n^2}(\lambda-n^2)^2+O((\lambda-n^2)^3).
```

Since the monodromy's periodic eigenfunction space is one-dimensional but the characteristic algebraic multiplicity is two, the periodic operator has a nontrivial length-two Jordan chain. Its resolvent has a **double pole** at $\lambda_n=n^2$.

**Theorem 10.1 [D,K,V].** The complex exponential Hill potential provides an explicit *true spectral exceptional point* in the specified finite-interval periodic operator, contrasted with the semisimple free operator having the **same** Floquet discriminant. The Bessel branch formula is DLMF §10.11.6; the operator conclusion follows from regular boundary-value characteristic multiplicities.

### 10.2 Even a complex non-self-adjoint potential need not be defective at every double discriminant root

For $\lambda=(n+\tfrac12)^2$, $n\ge0$, the Bessel orders $\nu=n+\tfrac12$ and $-\nu$ are independent. Both acquire multiplier $-1$ under the $2\pi$ continuation, so

```math
M_\alpha((n+\tfrac12)^2)=-I,\quad\Delta_\alpha=-2,\quad\Delta_\alpha'=0.
```

The antiperiodic eigenvalue is **semisimple of multiplicity two**, notwithstanding the complex potential. This is an especially sharp reason not to identify the scalar equalities $\Delta=\pm2$, $\Delta'=0$ with a resolvent double pole.

### 10.3 The non-self-adjoint whole-line operator is a different realization

The complex potential is $\pi$-periodic; its extension to a Hill operator on the full real line defines **another** spectral realization, with essential/continuous spectral phenomena. The finite-interval periodic eigenvalue Jordan calculation does not imply that the whole-line operator has an isolated resolvent pole at $n^2$. One must name the operator and domain each time.

## 11. Complex potentials modify the Pinney phase-current equation [D,C]

For a possibly complex $V$ and $\lambda$, write a nonvanishing complex solution $\Phi=a e^{i\theta}$ with $a>0$, real $\theta$, and $j=a^2\theta_u$. Separating the real and imaginary parts of $\Phi_{uu}=(V-\lambda)\Phi$ gives

```math
a_{uu}=(\mathrm{Re}\,V-\mathrm{Re}\,\lambda)a+j^2a^{-3},\qquad j_u=(\mathrm{Im}\,V-\mathrm{Im}\,\lambda)a^2.
```

This coupled nonlinear real system is not an ordinary constant-strength EP equation **unless $j_u=0$**. In the complex Bessel example with real $\lambda$,

```math
j_u=\alpha\sin(2u)a^2.
```

The current need not be constant, even though the local second-order ODE remains linear and projectivizable. Conversely, one can destroy **Hilbert-domain self-adjointness** using complex Robin boundary conditions while keeping $V$ real; then $j_u=0$ for every real spectral parameter in the interior. Hence:

**Theorem 11.1 [D,C].** EP current conservation is a **local real-coefficient property**, not a sufficient or necessary test for self-adjointness of a chosen global operator realization. Strict positivity of a selected EP amplitude similarly does not imply unbroken self-adjointness, a real discrete spectrum, or a specific Floquet band/gap regime.

## 12. The canonical integer Pöschl–Teller hierarchy remains fully self-adjoint [H100,H299,D]

The archived reflectionless operators are

```math
h_n=-\partial_u^2-n(n+1)r^2S^2,\qquad n=1,2,\ldots,\qquad \mathrm{Dom}(h_n)=H^2(\mathbb R).
```

They are self-adjoint real bounded-potential Schrödinger operators with

```math
\sigma_{\rm disc}(h_n)=\{-j^2r^2:j=1,\ldots,n\},\qquad \sigma_{\rm ac}(h_n)=[0,\infty).
```

The Crum operator $Q_n$ and odd Lax–Novikov operator $P_n$ satisfy the historically verified identities

```math
Q_nh_n=h_0Q_n,\qquad P_n^2=-h_n\prod_{j=1}^n(h_n+j^2r^2)^2,\qquad [P_n,h_n]=0.
```

The auxiliary spectral curve is nodal:

```math
\nu^2=-E\prod_{j=1}^n(E+j^2r^2)^2.
```

Its repeated roots $E=-j^2r^2$ record the solitonic degeneration of a higher-order finite-gap **algebraic curve**, not a nonreal exceptional eigenvalue. The normalized spectral curve is rational, its generalized Jacobian has multiplicative gluing coordinates, and the discrete norming constants cannot be reconstructed from the spectral polynomial alone (draft 150).

The polar Darboux map is unitary only on the **absolutely continuous subspace**, leaving the $n$ bound states as an explicit kernel/defect (draft 140). The weighted Fourier–Mellin resolution in the original $x$ coordinate must retain those finitely many discrete terms.

## 13. The one-gap Lamé family has TWO inequivalent nodal limits [D,V,K]

Choose the *selected* real one-gap Lamé family

```math
L_m=-\partial_u^2+2mr^2\mathrm{sn}^2(ru\mid m)-2mr^2,\qquad 0<m<1,\quad r>0.
```

The potential's primitive spatial period is $T_m=2K(m)/r$, with $K$ the complete elliptic integral of parameter $m$. Its three explicitly checked Lamé edge functions and energies are

```math
\mathrm{dn}(ru\mid m):\ E_0=-mr^2,\quad\mathrm{cn}(ru\mid m):\ E_1=(1-2m)r^2,\quad\mathrm{sn}(ru\mid m):\ E_2=(1-m)r^2.
```

These follow from the Jacobi derivative identities and the three one-gap Lamé eigenvalue equations. For $0<m<1$,

```math
E_0<E_1<E_2,\qquad \sigma(L_m)=[E_0,E_1]\cup[E_2,\infty).
```

The **finite forbidden gap** is $(E_1,E_2)$, and the lower *allowed* band is $[E_0,E_1]$. Introduce the spectral cubic with a declared real quadratic twist:

```math
\Gamma_m:\quad\eta^2=-(E-E_0)(E-E_1)(E-E_2).
```

It is a **smooth elliptic curve** for $0<m<1$ and has Legendre $j$-invariant

```math
j_m=256\frac{(1-m+m^2)^3}{m^2(1-m)^2}.
```

### 13.1 Closing a gap: m tends to zero

The Jacobi function becomes $\mathrm{sn}(ru\mid0)=\sin(ru)$, so $L_m\to-\partial_u^2$ and $T_m\to\pi/r$. The edge values become

```math
(E_0,E_1,E_2)\longrightarrow(0,r^2,r^2),\qquad \eta^2\longrightarrow -E(E-r^2)^2.
```

The **open forbidden gap** $(E_1,E_2)$ closes to the point $E=r^2$. Its limiting free monodromy at $E=r^2$ over the period $\pi/r$ is

```math
M_{\rm free}(r^2)=-I,\qquad\Delta_{\rm free}(r^2)=-2,\qquad\Delta_{\rm free}'(r^2)=0.
```

This is a **semisimple closed gap** of a self-adjoint periodic operator, even though the cubic acquires a node.

### 13.2 Collapsing an allowed band: m tends to one

The elementary limit $\mathrm{sn}(ru\mid1)=\tanh(ru)$ gives

```math
L_m\longrightarrow-\partial_u^2-2r^2\mathrm{sech}^2(ru)=h_1,\qquad T_m\longrightarrow\infty.
```

The edge values instead become

```math
(E_0,E_1,E_2)\longrightarrow(-r^2,-r^2,0),\qquad \eta^2\longrightarrow -E(E+r^2)^2.
```

Now the **lower allowed band** $[E_0,E_1]$ collapses to the single bound state $E=-r^2$, while the continuum starts at $E=0$. The forbidden interval between bound state and continuum survives, but the potential ceases to be periodic on a fixed finite spatial cell. The diverging primitive period means there is **no automatic finite-period Floquet transfer matrix at this endpoint** to which one can ascribe a Jordan block.

**Theorem 13.1 [D,V,K] (two distinct nodal mechanisms).** The same smooth genus-one Lamé spectral family has (i) a **gap-closing/free** degeneration at $m\to0$ with semisimple band-edge monodromy, and (ii) an **allowed-band-collapse/reflectionless-soliton** degeneration at $m\to1$ with a spatial period diverging to infinity. Algebraic nodes arise in both but do not encode a universal operator exceptional point.

These two limiting cubics are distinguished by the location of their repeated root relative to the operator's bound/continuum spectrum. The original claim “PT is a closed spectral gap while Riemann has open spectral gaps” requires correction: PT is a **decaying whole-line** operator, not a periodic Floquet spectrum. A Riemann minimal example is a surface, not automatically a periodic Hill operator; selecting a Lamé operator with the same elliptic modulus is an additional explicit construction.
