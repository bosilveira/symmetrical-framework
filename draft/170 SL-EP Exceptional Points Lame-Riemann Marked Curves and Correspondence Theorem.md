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

**Question.** Which parts of the SL–Riccati–EP, binary-quartic, finite-gap, Darboux–Crum, catenoid/helicoid, Riemann-minimal-example and weighted-Hilbert frameworks can be organized into a precise theorem? When is a Jordan block an operator exceptional point? Are the two possible spectral-gap degenerations the same? Can the one-gap Lamé spectral curve be mapped with marked differentials to the **whole real Riemann elliptic family**, rather than only to the symmetric $`j=1728`$ Pinney member?

**Principal answers.** The local SL–Riccati–EP correspondence is an exact finite-dimensional Lie–Hamilton/symmetric-square system for a *prescribed real* linear carrier. Self-adjointness is a separate global Hilbert-domain condition. A nontrivial Jordan **transfer** matrix need not be an operator defect; conversely a genuine non-self-adjoint periodic eigenvalue defect can be constructed explicitly from Bessel monodromy. For the one-gap Lamé family there are two **different** nodal endpoints: a gap closes at $`m=0`$ with semisimple free monodromy, while an allowed band collapses at $`m=1`$ to the reflectionless PT bound state. The new selected modulus assignment $`m=(1+\lambda_R^2)^{-1}`$ gives a real **affine isomorphism of smooth elliptic curves** between the Lamé spectral curve (with a declared sign convention) and the real Riemann-minimal-example elliptic curve for every $`\lambda_R>0`$. It pulls back the full meromorphic Weierstrass triple into the two-dimensional span of marked spectral differentials, *without asserting that the physical quasimomentum differential and the geometric height differential automatically coincide*. The order-one spectral-node catenoid/helicoid map from draft 160 is recovered at the soliton endpoint.

**Project sources actually reviewed:** November 18 backup ZIP, including the verified H100/H299 Lax–Novikov identities, H466–H472 Riemann Gauss–Manin/Weierstrass/period formulas, and the Lamé special-loci reference; GitHub drafts 120, 130, 140, 150, and 160. External Hill, Gasymov/Bessel, Lamé and Riemann-minimal-surface literature is listed in §27. The affine elliptic curve map, branch-point correspondence, $`j`$ identity and differential pullbacks were verified with exact SymPy polynomial arithmetic.

## 1. Typed objects: five different monodromies and spectra

| Object | Data | Mathematical content |
|---|---|---|
| Instantaneous matrix $`A(u)`$ | linear carrier at a specified $`u`$ | local elliptic/hyperbolic/nilpotent type |
| Spatial transfer matrix $`M(\lambda)`$ | transport over a given interval | Floquet multipliers, eigenvalue characteristic determinant and transfer Jordan form |
| Hilbert operator $`L_{\mathcal D}`$ | differential expression plus weight, interval and domain | self-adjointness, operator eigenvalue Jordan chains, resolvent poles |
| Gauss–Manin/Picard–Lefschetz monodromy | analytic continuation in a curve modulus | degeneration of marked homology cycles and logarithmic periods |
| Nodal spectral curve | a polynomial $`\eta^2=P(E)`$ with collided roots | algebraic singularities and generalized Jacobian, not automatically an operator defect |

The phrase **spectral exceptional point** is reserved for an *isolated non-semisimple eigenvalue of a specified closed operator*. A Jordan transfer matrix, a node of an auxiliary spectral curve, and a Gauss–Manin unipotent matrix are different mathematical properties.

## 2. Coordinates and parameters must remain typed

Fix the canonical Symmetrical Framework variables

```math
x,r,c,\mu>0,\quad u=\ln(x/c),\quad x=ce^u,\quad S=\mathrm{sech}(ru),\quad W=\tanh(ru),\quad f_\mu=\frac{S}{2\sqrt\mu\,x}.
```

For general Sturm–Liouville use $`p(x),w(x)>0`$, real $`q_0(x)`$, a **spectral** parameter $`\lambda`$, and an **operator domain** $`\mathcal D`$. For Ermakov–Pinney use a positive amplitude $`a(t)`$ and strength $`k_{\rm EP}`$, neither of which is an eigenvalue. For the one-gap Lamé curve use elliptic parameter $`m\in(0,1)`$ and **spectral energy** $`E`$. For the Riemann minimal-example family use geometric modulus $`\lambda_R>0`$, $`k_R=\lambda_R^{-1}-\lambda_R`$, Gauss coordinate $`g_R`$, and immersion scale $`A_R>0`$. The Riemann modulus $`\lambda_R`$, spectral $`E`$, scattering $`k_{\rm sc}`$, original amplitude $`\mu`$ and independent coordinate $`u`$ are never interchangeable.

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

**Proof.** Substitute $`\psi=\chi y`$, cancel the first derivative by the selected $`\chi`$, and use $`\chi^2dt=\sqrt{pw}\sqrt{w/p}\,dx=w\,dx`$. The determinant identity follows by the same cancellation. To conclude **unitary operator equivalence**, the self-adjoint domain must also be transported.

For the original carrier,

```math
p=x^3,\quad w=x,\quad q_0=(r^2-1)x,\quad t=u=\ln(x/c),\quad\chi=x,
```

giving

```math
U_cf=xf(x),\qquad U_c\tau_xU_c^{-1}=-\partial_u^2+r^2,\qquad\|f\|^2_{L^2(xdx)}=\|U_cf\|^2_{L^2(du)}.
```

The full-line free carrier is self-adjoint with purely continuous spectrum $`[r^2,\infty)`$. The localized nonlinear original profile is **not** a zero eigenfunction of this positive free carrier.

## 4. Local Riccati, positive Pinney, and symmetric-square equivalence [D,K]

For a **prescribed real** $`V(t)`$ and a **real spectral parameter** $`\lambda`$, let

```math
-\phi_{tt}+V(t)\phi=\lambda\phi,\qquad Q(t)=V(t)-\lambda.
```

If a complex carrier $`\Phi=a e^{i\theta}`$ never vanishes and $`a>0`$, its current is constant:

```math
j=\mathrm{Im}(\bar\Phi\Phi_t)=a^2\theta_t,\quad j_t=0,\quad a_{tt}=Qa+j^2a^{-3}.
```

Thus the **scattering- or carrier-normalized Pinney strength** is $`k_{\rm EP}=j^2`$. More generally, for independent real carrier solutions $`\phi_1,\phi_2`$ with constant Wronskian $`\mathscr W`$ and a constant symmetric Gram matrix $`G`$,

```math
J=a^2=A\phi_1^2+2C\phi_1\phi_2+B\phi_2^2,\qquad k_{\rm EP}=(AB-C^2)\mathscr W^2.
```

If $`G`$ is **positive definite**, then $`J>0`$ globally on the common interval because independent carrier solutions never vanish simultaneously. A merely positive determinant without a positive quadratic form is not enough to select a positive real envelope.

The *linear* third-order symmetric-square system and its conserved invariant are

```math
J_{ttt}-4QJ_t-2Q_tJ=0,\qquad 2JJ_{tt}-J_t^2-4QJ^2=4k_{\rm EP}.
```

On nonvanishing charts the logarithmic derivative $`z=\Phi_t/\Phi`$ satisfies

```math
z_t+z^2=Q,\qquad z=a_t/a+ij/a^2.
```

**Scope [C].** This equivalence concerns one *selected nonlinear envelope equation* and a real rank-two carrier. It does **not** linearize arbitrary nonlinear differential equations, fix a global spectral domain, or make the Pinney equation a linear operator eigenvalue problem.

## 5. A finite Lie–Hamilton closure is present, but the potential needs separate data [D,H]

On the phase plane $`(a,p_a)`$ with $`\{a,p_a\}=1`$ define

```math
H_0=(p_a^2+k_{\rm EP}a^{-2})/2,\quad D=ap_a/2,\quad K=a^2/2,\quad H(t)=H_0+(\lambda-V(t))K.
```

Then

```math
\{D,H_0\}=H_0,\quad\{D,K\}=-K,\quad\{K,H_0\}=2D,\quad H_0K-D^2=k_{\rm EP}/4.
```

The three generators close under the Poisson bracket and give the exact $`\mathfrak{sl}_2`$ Lie–Hamilton/symmetric-square dynamics of drafts 100/130. For an **arbitrary prescribed** coefficient $`V(t)`$ this remains a nonautonomous finite Lie system. It does **not** supply a universal autonomous finite-dimensional differential equation for $`V`$. The selected Pöschl–Teller potential satisfies one, or a stationary-KdV/finite-gap reduction can be imposed as an additional spectral constraint.

## 6. Self-adjointness is determined by operator domain, not by Pinney positivity [D,C]

For $`\tau=w^{-1}[-(p\partial_x)'+q_0]`$ the exact Green boundary form is

```math
\langle y,\tau z\rangle_w-\langle\tau y,z\rangle_w=[p(\bar y_xz-\bar yz_x)]_{\partial I}.
```

A real formally symmetric expression need not be self-adjoint until its domain is specified; a complex boundary parameter can destroy symmetry without altering the interior equation or its real Pinney family. Conversely a real self-adjoint operator can have negative eigenvalues, scattering flux, and a defective **transfer matrix**.

The canonical inversion $`x\mapsto c^2/x`$ becomes parity $`u\mapsto-u`$. In the original coordinate the even/odd half-line boundary conditions are

```math
cf_x(c)+f(c)=0\quad(\mathrm{even}),\qquad f(c)=0\quad(\mathrm{odd}),
```

provided a parity-preserving self-adjoint realization and a half-line restriction have been declared. The equal halves of the original improper integral come from an even positive density, **not** from this spectral domain choice.

## 7. Genuine exceptional eigenvalues and resolvent poles [D,K]

Let $`L_{\mathcal D}`$ be a closed Hilbert operator with compact resolvent and isolated eigenvalue $`\lambda_0`$. A nontrivial operator Jordan chain consists of

```math
(L_{\mathcal D}-\lambda_0)\psi_0=0,\quad(L_{\mathcal D}-\lambda_0)\psi_1=\psi_0,\quad\psi_0\ne0,\quad\psi_0,\psi_1\in\mathrm{Dom}(L_{\mathcal D}).
```

The resolvent pole order at $`\lambda_0`$ equals the **maximal Jordan-chain length** on the finite-dimensional Riesz spectral subspace. A length-two chain with no longer chain gives a double pole. A **semisimple** eigenvalue of algebraic multiplicity two has a rank-two spectral projection but only a simple pole.

For a self-adjoint operator no such chain can exist, since

```math
\|\psi_0\|^2=\langle(L-\lambda_0)\psi_1,\psi_0\rangle=\langle\psi_1,(L-\lambda_0)\psi_0\rangle=0.
```

Thus a truly defective isolated eigenvalue is incompatible with self-adjointness; this says nothing about the Jordan form of a *spatial transfer matrix*.

## 8. Floquet discriminant and the exact missing condition [D,K,C]

For a periodic Hill equation $`-\phi''+V\phi=\lambda\phi`$, let $`M(\lambda)\in SL(2,\mathbb C)`$ transport Cauchy data over one spatial period $`L`$, and $`\Delta(\lambda)=\mathrm{tr}\,M(\lambda)`$.

For a periodic ($`\sigma=+1`$) or antiperiodic ($`\sigma=-1`$) Hilbert realization on $`[0,L]`$, the characteristic determinant is

```math
D_\sigma(\lambda)=\det(M(\lambda)-\sigma I)=2-\sigma\Delta(\lambda).
```

A root obeys $`\Delta(\lambda_0)=2\sigma`$. A **double** root additionally obeys $`\Delta'(\lambda_0)=0`$, but this is not sufficient for a defective operator eigenvalue: one must know the geometric eigenspace and the operator Jordan chain.

The boundary correction in the Green function uses

```math
(M-\sigma I)^{-1}=\frac{\mathrm{adj}(M-\sigma I)}{2-\sigma\Delta(\lambda)}.
```

If the denominator vanishes quadratically but $`M(\lambda_0)=\sigma I`$, the adjugate vanishes too; a **semisimple** double eigenvalue can have only a simple resolvent pole. If $`M(\lambda_0)\ne\sigma I`$ is Jordan and the characteristic zero is **exactly** double, the adjugate is nonzero and the regular boundary operator has a true double resolvent pole.

**Counterpoint:** For quasiperiodic multiplier $`e^{i\vartheta}`$ the characteristic equation is $`\Delta=2\cos\vartheta`$, not necessarily $`\pm2`$. For separated Robin or other domains the characteristic determinant is different again. Hence the proposed equalities $`\Delta=\pm2`$, $`\Delta'=0`$ are neither a universal necessary condition nor a universal sufficient condition for an operator exceptional point.

## 9. First exact counterexample: free SELF-ADJOINT Hill operator [D,V,C]

On $`L^2([0,L])`$, let $`L_0=-\partial_u^2`$ with standard real periodic or antiperiodic $`H^2`$ domain. At spectral value $`\lambda`$ the transfer matrix and discriminant are

```math
M_0(\lambda)=\begin{pmatrix}\cos(\sqrt\lambda L)&\sin(\sqrt\lambda L)/\sqrt\lambda\\-\sqrt\lambda\sin(\sqrt\lambda L)&\cos(\sqrt\lambda L)\end{pmatrix},\qquad\Delta_0(\lambda)=2\cos(\sqrt\lambda L).
```

At the bottom point $`\lambda=0`$,

```math
M_0(0)=\begin{pmatrix}1&L\\0&1\end{pmatrix},\qquad\Delta_0(0)=2,\qquad\Delta_0'(0)=-L^2\ne0.
```

The spatial matrix has a nontrivial Jordan block, but the periodic operator is self-adjoint and its zero eigenvalue is **simple**. The resolvent pole is simple.

At every positive free band-edge value $`\lambda_n=(n\pi/L)^2`$ ($`n\ge1`$),

```math
M_0(\lambda_n)=(-1)^nI,\qquad\Delta_0(\lambda_n)=2(-1)^n,\qquad\Delta_0'(\lambda_n)=0.
```

The corresponding *periodic* ($`n`$ even) or *antiperiodic* ($`n`$ odd) eigenvalue has geometric multiplicity **two**, spanned by $`\sin(n\pi u/L)`$ and $`\cos(n\pi u/L)`$. It is **semisimple**, and its resolvent still has only a simple pole.

**Theorem 9.1 [D,V,C].** Neither a Jordan spatial transfer matrix alone, nor a double root of $`\Delta-2\sigma`$ alone, implies a spectral exceptional point. The first fails at $`\lambda=0`$; the second fails at every positive $`\lambda_n`$.

For the free period $`L=\pi/r`$, the $`n=1`$ **antiperiodic** level at $`\lambda=r^2`$ has $`M=-I`$ and $`\Delta'=0`$. Yet the real nodeless Pinney envelope $`a=1`$, from the complex linear carrier $`\Phi=e^{iru}`$, satisfies

```math
a_{uu}=-r^2a+r^2a^{-3},\qquad j=r,\qquad k_{\rm EP}=r^2.
```

It is not a homoclinic separatrix: it is a stationary positive envelope of an oscillatory linear carrier. This explicitly refutes the idea that Pinney positivity alone detects a unique spectral boundary between periodic and hyperbolic dynamics.

## 10. Second exact counterexample: a TRUE non-self-adjoint periodic exceptional point [D,K,V]

Choose the **complex periodic** potential $`V_\alpha(u)=\alpha e^{2iu}`$, $`\alpha>0`$, on the fixed interval $`u\in[0,2\pi]`$, and the periodic domain

```math
L_\alpha=-\partial_u^2+\alpha e^{2iu},\quad \mathcal D_{\rm per}=\{y\in H^2(0,2\pi):y(2\pi)=y(0),\ y_u(2\pi)=y_u(0)\}.
```

This operator is **not self-adjoint**, because its potential is nonreal for generic real $`u`$. It has compact resolvent, so isolated periodic eigenvalues have finite algebraic multiplicity.

Set the complex Bessel argument and order

```math
z=\sqrt\alpha\,e^{iu},\qquad \nu^2=\lambda.
```

The spectral equation reduces by exact differentiation to

```math
z^2Y_{zz}+zY_z+(z^2-\nu^2)Y=0.
```

Therefore the fundamental solutions are Bessel functions $`J_\nu(z),J_{-\nu}(z)`$ for noninteger $`\nu`$; analytic continuation as $`u`$ increases from $`0`$ to $`2\pi`$ rotates $`z`$ once about zero. The two Floquet multipliers are $`e^{\pm2\pi i\nu}`$, giving the exact discriminant

```math
\Delta_\alpha(\lambda)=2\cos(2\pi\sqrt\lambda).
```

This is the **same discriminant as a free operator on a circle of length $`2\pi`$**, but the operator eigenvector structure need not agree.

### 10.1 Integer spectral order produces a genuine Jordan block

At every $`\lambda_n=n^2`$ with $`n=1,2,\ldots`$, the periodic Bessel function $`J_n(z)`$ is a genuine eigenfunction. The second integer-order solution $`Y_n(z)`$ obeys the classical Bessel analytic continuation formula

```math
Y_n(ze^{2\pi i})=Y_n(z)+4iJ_n(z).
```

Thus, in the local fundamental basis $`(J_n,Y_n)`$,

```math
M_\alpha(n^2)\sim\begin{pmatrix}1&4i\\0&1\end{pmatrix},\qquad M_\alpha(n^2)\ne I,\qquad (M_\alpha(n^2)-I)^2=0.
```

Meanwhile the characteristic zero is **exactly double**:

```math
2-\Delta_\alpha(\lambda)=\frac{\pi^2}{n^2}(\lambda-n^2)^2+O((\lambda-n^2)^3).
```

Since the monodromy's periodic eigenfunction space is one-dimensional but the characteristic algebraic multiplicity is two, the periodic operator has a nontrivial length-two Jordan chain. Its resolvent has a **double pole** at $`\lambda_n=n^2`$.

**Theorem 10.1 [D,K,V].** The complex exponential Hill potential provides an explicit *true spectral exceptional point* in the specified finite-interval periodic operator, contrasted with the semisimple free operator having the **same** Floquet discriminant. The Bessel branch formula is DLMF §10.11.6; the operator conclusion follows from regular boundary-value characteristic multiplicities.

### 10.2 Even a complex non-self-adjoint potential need not be defective at every double discriminant root

For $`\lambda=(n+\tfrac12)^2`$, $`n\ge0`$, the Bessel orders $`\nu=n+\tfrac12`$ and $`-\nu`$ are independent. Both acquire multiplier $`-1`$ under the $`2\pi`$ continuation, so

```math
M_\alpha((n+\tfrac12)^2)=-I,\quad\Delta_\alpha=-2,\quad\Delta_\alpha'=0.
```

The antiperiodic eigenvalue is **semisimple of multiplicity two**, notwithstanding the complex potential. This is an especially sharp reason not to identify the scalar equalities $`\Delta=\pm2`$, $`\Delta'=0`$ with a resolvent double pole.

### 10.3 The non-self-adjoint whole-line operator is a different realization

The complex potential is $`\pi`$-periodic; its extension to a Hill operator on the full real line defines **another** spectral realization, with essential/continuous spectral phenomena. The finite-interval periodic eigenvalue Jordan calculation does not imply that the whole-line operator has an isolated resolvent pole at $`n^2`$. One must name the operator and domain each time.

## 11. Complex potentials modify the Pinney phase-current equation [D,C]

For a possibly complex $`V`$ and $`\lambda`$, write a nonvanishing complex solution $`\Phi=a e^{i\theta}`$ with $`a>0`$, real $`\theta`$, and $`j=a^2\theta_u`$. Separating the real and imaginary parts of $`\Phi_{uu}=(V-\lambda)\Phi`$ gives

```math
a_{uu}=(\mathrm{Re}\,V-\mathrm{Re}\,\lambda)a+j^2a^{-3},\qquad j_u=(\mathrm{Im}\,V-\mathrm{Im}\,\lambda)a^2.
```

This coupled nonlinear real system is not an ordinary constant-strength EP equation **unless $`j_u=0`$**. In the complex Bessel example with real $`\lambda`$,

```math
j_u=\alpha\sin(2u)a^2.
```

The current need not be constant, even though the local second-order ODE remains linear and projectivizable. Conversely, one can destroy **Hilbert-domain self-adjointness** using complex Robin boundary conditions while keeping $`V`$ real; then $`j_u=0`$ for every real spectral parameter in the interior. Hence:

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

The Crum operator $`Q_n`$ and odd Lax–Novikov operator $`P_n`$ satisfy the historically verified identities

```math
Q_nh_n=h_0Q_n,\qquad P_n^2=-h_n\prod_{j=1}^n(h_n+j^2r^2)^2,\qquad [P_n,h_n]=0.
```

The auxiliary spectral curve is nodal:

```math
\nu^2=-E\prod_{j=1}^n(E+j^2r^2)^2.
```

Its repeated roots $`E=-j^2r^2`$ record the solitonic degeneration of a higher-order finite-gap **algebraic curve**, not a nonreal exceptional eigenvalue. The normalized spectral curve is rational, its generalized Jacobian has multiplicative gluing coordinates, and the discrete norming constants cannot be reconstructed from the spectral polynomial alone (draft 150).

The polar Darboux map is unitary only on the **absolutely continuous subspace**, leaving the $`n`$ bound states as an explicit kernel/defect (draft 140). The weighted Fourier–Mellin resolution in the original $`x`$ coordinate must retain those finitely many discrete terms.

## 13. The one-gap Lamé family has TWO inequivalent nodal limits [D,V,K]

Choose the *selected* real one-gap Lamé family

```math
L_m=-\partial_u^2+2mr^2\mathrm{sn}^2(ru\mid m)-2mr^2,\qquad 0<m<1,\quad r>0.
```

The potential's primitive spatial period is $`T_m=2K(m)/r`$, with $`K`$ the complete elliptic integral of parameter $`m`$. Its three explicitly checked Lamé edge functions and energies are

```math
\mathrm{dn}(ru\mid m):\ E_0=-mr^2,\quad\mathrm{cn}(ru\mid m):\ E_1=(1-2m)r^2,\quad\mathrm{sn}(ru\mid m):\ E_2=(1-m)r^2.
```

These follow from the Jacobi derivative identities and the three one-gap Lamé eigenvalue equations. For $`0<m<1`$,

```math
E_0<E_1<E_2,\qquad \sigma(L_m)=[E_0,E_1]\cup[E_2,\infty).
```

The **finite forbidden gap** is $`(E_1,E_2)`$, and the lower *allowed* band is $`[E_0,E_1]`$. Introduce the spectral cubic with a declared real quadratic twist:

```math
\Gamma_m:\quad\eta^2=-(E-E_0)(E-E_1)(E-E_2).
```

It is a **smooth elliptic curve** for $`0<m<1`$ and has Legendre $`j`$-invariant

```math
j_m=256\frac{(1-m+m^2)^3}{m^2(1-m)^2}.
```

### 13.1 Closing a gap: m tends to zero

The Jacobi function becomes $`\mathrm{sn}(ru\mid0)=\sin(ru)`$, so $`L_m\to-\partial_u^2`$ and $`T_m\to\pi/r`$. The edge values become

```math
(E_0,E_1,E_2)\longrightarrow(0,r^2,r^2),\qquad \eta^2\longrightarrow -E(E-r^2)^2.
```

The **open forbidden gap** $`(E_1,E_2)`$ closes to the point $`E=r^2`$. Its limiting free monodromy at $`E=r^2`$ over the period $`\pi/r`$ is

```math
M_{\rm free}(r^2)=-I,\qquad\Delta_{\rm free}(r^2)=-2,\qquad\Delta_{\rm free}'(r^2)=0.
```

This is a **semisimple closed gap** of a self-adjoint periodic operator, even though the cubic acquires a node.

### 13.2 Collapsing an allowed band: m tends to one

The elementary limit $`\mathrm{sn}(ru\mid1)=\tanh(ru)`$ gives

```math
L_m\longrightarrow-\partial_u^2-2r^2\mathrm{sech}^2(ru)=h_1,\qquad T_m\longrightarrow\infty.
```

The edge values instead become

```math
(E_0,E_1,E_2)\longrightarrow(-r^2,-r^2,0),\qquad \eta^2\longrightarrow -E(E+r^2)^2.
```

Now the **lower allowed band** $`[E_0,E_1]`$ collapses to the single bound state $`E=-r^2`$, while the continuum starts at $`E=0`$. The forbidden interval between bound state and continuum survives, but the potential ceases to be periodic on a fixed finite spatial cell. The diverging primitive period means there is **no automatic finite-period Floquet transfer matrix at this endpoint** to which one can ascribe a Jordan block.

**Theorem 13.1 [D,V,K] (two distinct nodal mechanisms).** The same smooth genus-one Lamé spectral family has (i) a **gap-closing/free** degeneration at $`m\to0`$ with semisimple band-edge monodromy, and (ii) an **allowed-band-collapse/reflectionless-soliton** degeneration at $`m\to1`$ with a spatial period diverging to infinity. Algebraic nodes arise in both but do not encode a universal operator exceptional point.

These two limiting cubics are distinguished by the location of their repeated root relative to the operator's bound/continuum spectrum. The original claim “PT is a closed spectral gap while Riemann has open spectral gaps” requires correction: PT is a **decaying whole-line** operator, not a periodic Floquet spectrum. A Riemann minimal example is a surface, not automatically a periodic Hill operator; selecting a Lamé operator with the same elliptic modulus is an additional explicit construction.

## 14. The Riemann elliptic family has exactly the same modular parameter m, once SELECTED [H466,H469,D]

The historically verified Riemann minimal-example family has meromorphic Gauss coordinate $`g_R`$ on

```math
w_R^2=g_R(g_R-\lambda_R)(\lambda_Rg_R+1),\qquad\lambda_R>0.
```

Write

```math
k_R=\lambda_R^{-1}-\lambda_R,\qquad D_R=\lambda_R+\lambda_R^{-1}>0,\qquad y_R=w_R/\sqrt{\lambda_R}.
```

Then

```math
E_R:\quad y_R^2=g_R^3+k_Rg_R^2-g_R=g_R(g_R-\lambda_R)(g_R+\lambda_R^{-1}).
```

The three finite branch points, in increasing **real** order, are $`-\lambda_R^{-1}<0<\lambda_R`$. The corresponding cross-ratio parameter with this ordering is

```math
m_R=\frac{1}{1+\lambda_R^2}=\frac12\left(1+\frac{k_R}{\sqrt{k_R^2+4}}\right)\in(0,1).
```

This formula and the associated modular invariant are recorded in the archival H466/H469 audit:

```math
j(E_R)=256\frac{(k_R^2+3)^3}{k_R^2+4}=256\frac{(1-m_R+m_R^2)^3}{m_R^2(1-m_R)^2}.
```

The equality $`j(E_R)=j(\Gamma_m)`$ upon setting $`m=m_R`$ suggests an elliptic curve isomorphism, but equality of $`j`$ alone leaves an unspecified algebraic coordinate change, real structure and differential. The next theorem supplies all three.

## 15. Main new bridge: a REAL ISOMORPHISM of Lamé spectral and Riemann elliptic curves [D,V]

Choose the one-gap Lamé family of §13 with the explicit **selected parameter match**

```math
m=m_R=(1+\lambda_R^2)^{-1},\quad k_R=\lambda_R^{-1}-\lambda_R,\quad D_R=\lambda_R+\lambda_R^{-1},\quad D_R^2=k_R^2+4.
```

Recall the smooth real spectral model

```math
\Gamma_m:\quad\eta^2=-(E-E_0)(E-E_1)(E-E_2),\quad E_0=-mr^2,\quad E_1=(1-2m)r^2,\quad E_2=(1-m)r^2.
```

**Theorem 15.1 [D,V] (explicit all-modulus elliptic isomorphism).** The affine formulas

```math
g_R=-k_R-\frac{D_R}{r^2}E,\qquad y_R=\frac{D_R^{3/2}}{r^3}\eta
```

define a real algebraic isomorphism of smooth affine elliptic curves (extending over their projective points at infinity) from $`\Gamma_m`$ to the normalized Riemann elliptic curve

```math
E_R:\quad y_R^2=g_R^3+k_Rg_R^2-g_R.
```

They carry the three spectral branch points to the three Riemann branch points **in the declared order**:

```math
E_0\mapsto g_R=\lambda_R,\qquad E_1\mapsto g_R=0,\qquad E_2\mapsto g_R=-\lambda_R^{-1}.
```

**Proof with all factors visible.** The affine slope is $`a_E=-D_R/r^2<0`$, so

```math
g_R-\lambda_R=a_E(E-E_0),\quad g_R=a_E(E-E_1),\quad g_R+\lambda_R^{-1}=a_E(E-E_2).
```

Multiply and use $`a_E^3=-D_R^3/r^6`$:

```math
g_R(g_R-\lambda_R)(g_R+\lambda_R^{-1})=-\frac{D_R^3}{r^6}(E-E_0)(E-E_1)(E-E_2)=\frac{D_R^3}{r^6}\eta^2=y_R^2.
```

The map has explicit inverse $`E=-(r^2/D_R)(g_R+k_R)`$ and $`\eta=(r^3/D_R^{3/2})y_R`$. Both coefficients are real and nonzero for $`\lambda_R,r>0`$, so it is an **isomorphism of real** smooth elliptic curves. The degree is **one**, not the degree-two isogeny of the centered Pinney energy curve in drafts 150–160.

**Independent exact verification [V]:** The polynomial residual in $`(E,r,\lambda_R)`$ vanishes identically in SymPy, the three branch-image identities simplify to $`(\lambda_R,0,-1/\lambda_R)`$, and the two rational $`j`$ expressions simplify to exactly the same rational function of $`\lambda_R`$.

### 15.1 Why the negative spectral cubic sign matters

The chosen spectral curve has $`\eta^2=-\prod(E-E_j)`$ rather than $`+\prod(E-E_j)`$. Because the branch-point map reverses real order, that minus sign is precisely what permits the isomorphism **over the reals** using the positive scale $`D_R^{3/2}/r^3`$. Using the opposite sign gives a complex quadratic twist: an isomorphism then requires an additional factor $`i`$ in the fiber coordinate, and the real-period interpretation changes.

In commuting-operator conventions the Burchnall–Chaundy spectral equation naturally carries a minus sign (as in the archived $`P_n^2=-h_n\prod(h_n+j^2r^2)^2`$), so the chosen real form is also consistent with the solitonic endpoint.

## 16. The complete marked holomorphic differential and Hodge correspondence [D,V]

The normalized Riemann holomorphic differential is $`\omega_R=dg_R/y_R`$. Differentiate the affine map of §15:

```math
dg_R=-\frac{D_R}{r^2}dE,\qquad \frac{dg_R}{y_R}=-\frac{r}{\sqrt{D_R}}\frac{dE}{\eta}.
```

**Theorem 16.1 [D,V] (marked differential scaling).** The map transports the distinguished holomorphic differential exactly:

```math
\Phi_m^*\omega_R=-\frac{r}{\sqrt{D_R}}\omega_{\rm sp},\qquad\omega_{\rm sp}=\frac{dE}{\eta}.
```

The original **physical Riemann** holomorphic height form is $`dg_R/w_R`$, where $`w_R=\sqrt{\lambda_R}y_R`$. Its pullback simplifies further:

```math
\Phi_m^*\left(\frac{dg_R}{w_R}\right)=-\frac{r}{\sqrt{\lambda_RD_R}}\frac{dE}{\eta}=-r\sqrt m\,\frac{dE}{\eta}.
```

Here the exact identity $`\lambda_RD_R=1+\lambda_R^2=1/m`$ has been used. No factor of $`r`$, the immersion modulus, or the square root has been suppressed.

### 16.1 Hodge metric: a genuine degree-one isometric scaling

For a smooth compact elliptic curve and holomorphic one-form, use

```math
\|\omega\|_{\rm Hodge}^2=\frac{i}{2}\int_E\omega\wedge\bar\omega.
```

Because the map $`\Phi_m`$ has **degree one**, its pulled-back Hodge integral gives

```math
\|\omega_R\|_{\rm Hodge}^2=\frac{r^2}{D_R}\|\omega_{\rm sp}\|_{\rm Hodge}^2,\qquad\left\|\frac{dg_R}{w_R}\right\|_{\rm Hodge}^2=r^2m\|\omega_{\rm sp}\|_{\rm Hodge}^2.
```

These are exact **metric glue on spaces of holomorphic differentials**, with the correct degree and normalization. They are *not yet* an intertwining map from the original scalar weighted Hilbert space $`L^2((0,\infty),x\,dx)`$ to the elliptic Hodge space: such a map would require an additional operator/measure construction.

## 17. The full Weierstrass immersion triple is transported for EVERY real Riemann modulus [D,V,H466]

The archived Weierstrass one-forms, with the convention and scale used in H466, are

```math
\boldsymbol\Phi_R=\left(\frac{A_R}{2}(g_R^{-1}-g_R),\frac{iA_R}{2}(g_R^{-1}+g_R),A_R\right)\frac{dg_R}{w_R},\qquad A_R>0.
```

Let the **affine spectral marking** be the explicit function

```math
g(E)=-k_R-\frac{D_R}{r^2}E.
```

**Theorem 17.1 [D,V] (entire marked Weierstrass triple).** On the smooth Lamé spectral curve $`\Gamma_m`$, the real elliptic isomorphism of §15 pulls back all three meromorphic immersion differentials as

```math
\Phi_m^*\boldsymbol\Phi_R=-A_Rr\sqrt m\left(\frac12(g(E)^{-1}-g(E)),\frac i2(g(E)^{-1}+g(E)),1\right)\frac{dE}{\eta}.
```

**Proof.** Pull back the Gauss-coordinate multiplier by $`g_R=g(E)`$ and the common height factor by $`\Phi_m^*(dg_R/w_R)=-r\sqrt m\,dE/\eta`$. The meromorphic factors are well-defined away from the two planar-end punctures $`g=0,\infty`$; their polar structures are preserved by the algebraic isomorphism.

This result **improves the earlier centered $`j=1728`$ comparison**: it is an explicit differential-preserving isomorphism for the entire **selected** smooth real family $`\lambda_R>0`$, not just the point $`\lambda_R=1`$. But it does not say that an arbitrary SL–EP equation canonically selects the Riemann family, or that a Lamé wave function itself is a surface immersion.

### 17.1 Reduction to exactly two spectral periods

The historical exactness identity is

```math
d(w_R/g_R)=\frac{\lambda_R}{2}(g_R+g_R^{-1})\frac{dg_R}{w_R}.
```

Therefore

```math
\Phi_{R2}=\frac{iA_R}{\lambda_R}d(w_R/g_R),\quad \Phi_{R1}=\frac{A_R}{\lambda_R}d(w_R/g_R)-A_Rg_R\frac{dg_R}{w_R},\quad \Phi_{R3}=A_R\frac{dg_R}{w_R}.
```

For any marked closed cycle $`\gamma_{\rm sp}`$ on $`\Gamma_m`$ let

```math
I_0(\gamma_{\rm sp})=\oint_{\gamma_{\rm sp}}\frac{dE}{\eta},\qquad I_1(\gamma_{\rm sp})=\oint_{\gamma_{\rm sp}}\frac{E\,dE}{\eta}.
```

The image cycle $`\gamma_R=\Phi_{m*}\gamma_{\rm sp}`$ has periods

```math
\Omega_R(\gamma_R)=\oint_{\gamma_R}\frac{dg_R}{w_R}=-r\sqrt m\,I_0(\gamma_{\rm sp}).
```

```math
N_R(\gamma_R)=\oint_{\gamma_R}g_R\frac{dg_R}{w_R}=r\sqrt m\left(k_RI_0(\gamma_{\rm sp})+\frac{D_R}{r^2}I_1(\gamma_{\rm sp})\right).
```

Hence the complete complex immersion-period vector is

```math
\oint_{\gamma_R}\boldsymbol\Phi_R=A_R\left(-N_R(\gamma_R),\,0,\,\Omega_R(\gamma_R)\right).
```

This is an exact **spectral-period to immersion-period formula**. It preserves the whole two-dimensional de Rham period span; closing in $`\mathbb R^3`$ requires separately checking the real parts of these periods against the desired translation lattice.

### 17.2 Which spectral intervals map to which Riemann cycles?

The real branch-point order of §15 reverses the spectral energy order:

```math
[E_0,E_1]\longmapsto[g_R=\lambda_R,\,g_R=0],\qquad [E_1,E_2]\longmapsto[g_R=0,\,g_R=-\lambda_R^{-1}].
```

Thus the **lower allowed Lamé spectral band** maps to the Riemann $`\alpha`$-type branch cut, and the **finite forbidden Lamé spectral gap** maps to its $`\beta`$-type cut (up to orientations and standard doubled-cycle conventions). The archive's real Riemann translation and flux periods can therefore be written directly as integrals of $`dE/\eta`$ and $`E\,dE/\eta`$ along the correspondingly marked Lamé cycles.

This is a precise, new **marked real-cycle dictionary**. It does *not* say that the Floquet spectral quasimomentum equals $`dg_R/w_R`$; the quasimomentum is a **specific normalized meromorphic differential of the second kind**, whose normalization and asymptotics must be imposed separately.

## 18. Quasimomentum, spectral energy, and geometric height have different normalizations [D,K,C]

On a smooth one-gap spectral elliptic curve, a finite-gap Bloch/Floquet **quasimomentum differential** $`dp_{\rm qm}`$ is defined by its prescribed singular principal part at the point over $`E=\infty`$ and a chosen cycle normalization (e.g. zero $`a`$-period). Its cohomology class lies in the span of

```math
\omega_0=dE/\eta,\qquad\omega_1=E\,dE/\eta,
```

but the actual coefficients and cycle normalization depend on the spectral convention. The pullback in §17 identifies the Riemann holomorphic height form with $`\omega_0`$ and its horizontal period with a specific linear combination of $`\omega_0,\omega_1`$.

The existence of this common two-dimensional differential span is a **real algebro-geometric interface**. The further assertion

```math
dp_{\rm qm}=\mathrm{constant}\cdot\Phi^*(dg_R/w_R)
```

does **not** follow: the quasimomentum generally has a second-kind pole at spectral infinity while the Riemann height form is holomorphic on its compact elliptic curve. Their pole divisors differ, so they cannot be equal as meromorphic differentials unless the defining normalization is radically changed. This is an explicit obstruction to collapsing the spectral and geometric periods into one untyped scalar.

A smooth real isomorphism of spectral and Riemann elliptic curves is not the same thing as equality of the **chosen Schrödinger operator**, a surface **Jacobi operator**, their Hilbert domains, or global minimal-surface embeddedness.

## 19. At the two singular endpoints, the SAME elliptic holomorphic differential produces TWO foundational rational primitives [D,V]

This is a stronger synthesis than merely identifying the nodal spectral polynomial. Work with the **same family of marked holomorphic differentials**

```math
\omega_m=\frac{dE}{\eta},\qquad \eta^2=-(E-E_0)(E-E_1)(E-E_2),\qquad0<m<1.
```

In each **separate normalized nodal limit**, choose the same rational coordinate convention $`E=-s^2`$. The $`s`$-sphere is the normalization of the corresponding limiting curve; it is **not** the smooth genus-one curve for interior $`m`$.

### 19.1 Soliton endpoint m tends to one: logarithmic catenoid height

As $`m\to1`$ the cubic becomes

```math
\eta^2=-E(E+r^2)^2,\qquad E=-s^2,\qquad\eta=s(r^2-s^2).
```

Directly,

```math
\lim_{m\to1}\omega_m=\frac{-2s\,ds}{s(r^2-s^2)}=\frac{2\,ds}{s^2-r^2}=\frac1r\,d\log\frac{s-r}{s+r}.
```

**Theorem 19.1 [D,V] (soliton-node differential = catenoid height).** In this specified normalization, the limiting holomorphic spectral differential is exactly the marked catenoid height form of draft 160:

```math
\omega_{\rm sol}=\frac{2\,ds}{s^2-r^2}=dh_C,\quad t=\frac{s-r}{s+r},\quad g_C=-t,\quad \oint_{s=r}dh_C=\frac{2\pi i}{r}.
```

The positive-node residue is $`1/r`$, the negative-node residue $`-1/r`$, and the real part of the loop period vanishes. Together with the **chosen** Gauss map $`g_C=-t`$ and the standard Weierstrass triple, this yields the canonical catenoid immersion. Multiplying the triple by $`i`$ yields the conjugate helicoid with real translation period $`-2\pi/r`$, so it requires the angular universal cover.

**Meaning:** The spectral-node/catenoid identification of draft 160 is not an unrelated Möbius trick: it is exactly the **limiting differential of the smooth one-gap Lamé elliptic spectral family**. This has now been proved by an explicit degeneration.

### 19.2 Free, closed-gap endpoint m tends to zero: the arctangent primitive

As $`m\to0`$, the spectral cubic instead becomes

```math
\eta^2=-E(E-r^2)^2,\qquad E=-s^2,\qquad\eta=s(s^2+r^2).
```

Hence

```math
\lim_{m\to0}\omega_m=\frac{-2s\,ds}{s(s^2+r^2)}=-\frac{2\,ds}{s^2+r^2}.
```

Draft 160 independently expresses the original Symmetrical Function **one-form** using the same projective rational coordinate identification:

```math
t=\frac{s-r}{s+r}=(x/c)^r\quad\mathrm{on\ the\ real\ meridian},\qquad f_\mu(x;r,c)\,dx=\frac{ds}{\sqrt\mu(s^2+r^2)}.
```

**Theorem 19.2 [D,V] (free closed-gap differential = arctangent primitive).** With this explicitly fixed identification of the rational-normalization coordinates,

```math
f_\mu(x;r,c)\,dx=-\frac1{2\sqrt\mu}\,\omega_{\rm free},\qquad \omega_{\rm free}=-\frac{2\,ds}{s^2+r^2}.
```

This recovers the original primitive and half-split:

```math
\int_0^c f_\mu\,dx=\int_c^\infty f_\mu\,dx=\frac{\pi}{4r\sqrt\mu}.
```

The **free spectral node** has preimages $`s=\pm ir`$ (because its repeated energy is $`E=r^2=-s^2`$). Those are exactly the **poles of the original arctangent differential** on the same normalized $`s`$-sphere, whereas the soliton node has preimages $`\pm r`$ and gives the logarithmic catenoid differential.

### 19.3 The exact complex-rotation relation and its limit

The two limiting rational forms are

```math
\omega_{\rm sol}(s)=\frac{2\,ds}{s^2-r^2},\qquad\omega_{\rm free}(s)=-\frac{2\,ds}{s^2+r^2}.
```

Under the complex rotation $`\rho(s)=is`$, one finds

```math
\rho^*\omega_{\rm sol}=i\,\omega_{\rm free}.
```

This is a **complex algebraic relation of differently marked third-kind differentials**, resembling a Wick rotation. It is *not* a real operator unitary map, a real isometry of the free and PT Schrödinger operators, or an equality of their Floquet spectra.

**Main theorem 19.3 [D,V] (two-end marked-differential closure).** The selected one-gap Lamé spectral elliptic family has two rational nodal degenerations which yield **exactly two foundational Symmetrical Framework one-forms** under separately specified normalization maps: at $`m\to1`$, the catenoid logarithmic height $`dh_C`$; at $`m\to0`$, the original arctangent primitive $`f_\mu dx`$, up to the fixed amplitude factor $`-1/(2\sqrt\mu)`$. Their distinct residue/pole divisors and the complex rotation $`s\mapsto is`$ explain their relationship without conflating the distinct underlying real operator families.

## 20. Picard–Lefschetz Jordan monodromy is NOT Floquet Jordan monodromy [D,K,C]

Both endpoint cubics in §19 are nodal. In a family of **smooth elliptic curves** approaching a simple node, select a vanishing homology cycle $`a`$ and a transversal cycle $`b`$ with intersection number one. After encircling the nodal value in the **complex modulus plane**, the Picard–Lefschetz action is, up to orientations,

```math
a\longmapsto a,\qquad b\longmapsto b+a,\qquad M_{\rm PL}\sim\begin{pmatrix}1&1\\0&1\end{pmatrix}.
```

This is a genuine unipotent Jordan matrix acting on the **homology/period local system**, and the dual period typically acquires a logarithmic singularity. But it is **not** the Cauchy-data transfer matrix of $`-\partial_u^2+V_m(u)`$ over its real spatial period.

Indeed at $`m\to0`$, the **same nodal spectral degeneration** has

```math
M_{\rm PL}\ \mathrm{unipotent\ Jordan},\qquad M_{\rm spatial}(E=r^2)=-I\ \mathrm{semisimple}.
```

This is a direct counterexample to the statement “pinching a handle into a node forces Jordan $`2\times2`$ spatial monodromy.” The Jordan structure occurs in **modulus continuation**, whereas the spatial transfer at the closed free gap is **diagonalizable**.

The archived Riemann family likewise has its independently verified Gauss–Manin monodromy: around complex $`k_R=\pm2i`$ there are trace-$`2`$ unipotents, and at the modular cusp $`k_R=\infty`$ there is a trace-$`(-2)`$ matrix equal to minus a unipotent of width four (H470). Those matrices act on **marked elliptic periods**. They do not diagnose whether a Sturm–Liouville Hilbert operator is self-adjoint.

### 20.1 Degenerating periods do not force vanishing numerical periods

A geometrically vanishing homology cycle may have a **nonzero limiting integral** of a family of holomorphic forms when the forms themselves develop a logarithmic pole in the nodal limit. In §19 the limiting form has opposite residues at the two node preimages, and a small loop acquires period $`2\pi i/r`$. The complementary cycle has a logarithmic period divergence in appropriate normalized coordinates. The *cycle topology* and the *normalization of the differential* must both be tracked before asserting a numerical period limit.

## 21. The centered Pinney elliptic curve is a DEGREE-TWO neighbour of the symmetric Lamé spectral curve [D,V,H]

Drafts 150–160 establish the smooth centered Pinney mechanical energy quartic

```math
\mathcal P_{r,\mu}:\quad Y^2=\frac{r^2}{4}(a^4-\mu),\quad Y=a\,a_u,\quad j(\mathcal P_{r,\mu})=1728.
```

Its explicit degree-two isogeny to the symmetric Riemann elliptic fiber $`\lambda_R=1`$ is

```math
g_R=\frac{a^2}{\sqrt\mu},\qquad y_R=\frac{2aY}{r\mu^{3/4}},\qquad E_0^{(R)}:\ y_R^2=g_R^3-g_R.
```

At $`\lambda_R=1`$, $`m=1/2`$, $`D_R=2`$, $`k_R=0`$. The **new degree-one** Lamé-to-Riemann map of §15 becomes

```math
g_R=-\frac{2E}{r^2},\qquad y_R=\frac{2\sqrt2}{r^3}\eta,\qquad \Gamma_{1/2}:\quad\eta^2=-\left(E+\frac{r^2}{2}\right)E\left(E-\frac{r^2}{2}\right).
```

Composing the Pinney isogeny with the inverse Lamé–Riemann isomorphism gives a **direct algebraic degree-two map**

```math
\Psi:\mathcal P_{r,\mu}\longrightarrow\Gamma_{1/2},\qquad E=-\frac{r^2a^2}{2\sqrt\mu},\qquad \eta=\frac{r^2aY}{\sqrt2\,\mu^{3/4}}.
```

**Theorem 21.1 [D,V] (Pinney quartic to smooth Lamé spectral elliptic curve).** The displayed map is a degree-two unramified isogeny after selecting elliptic origins. Its holomorphic differential pullback is

```math
\Psi^*\left(\frac{dE}{\eta}\right)=-\sqrt2\,\mu^{1/4}\frac{da}{Y}.
```

**Proof.** Substitute $`Y^2=r^2(a^4-\mu)/4`$ into the cubic spectral equation, or compose the already proved smooth elliptic maps. Differentiating $`E=-r^2a^2/(2\sqrt\mu)`$ and dividing by $`\eta`$ yields the differential identity. Its generic fiber has two points related by the Pinney quartic involution $`(a,Y)\mapsto(-a,-Y)`$; the covering of smooth compact elliptic curves is unramified.

### 21.1 A three-space Hodge norm consistency check

The degree-one Lamé–Riemann map gives

```math
\left\|\frac{dg_R}{y_R}\right\|_{\rm Hodge}^2=\frac{r^2}{2}\left\|\frac{dE}{\eta}\right\|_{\rm Hodge}^2
```

at $`\lambda_R=1`$. The degree-two Pinney–Riemann map gives

```math
\left\|\frac{dg_R}{y_R}\right\|_{\rm Hodge}^2=\frac{r^2\sqrt\mu}{2}\left\|\frac{da}{Y}\right\|_{\rm Hodge}^2.
```

Combining them yields the exact consistency relation

```math
\left\|\frac{dE}{\eta}\right\|_{\rm Hodge}^2=\sqrt\mu\left\|\frac{da}{Y}\right\|_{\rm Hodge}^2,
```

which also follows directly from the degree-two pullback factor of Theorem 21.1.

The **marked Pinney time differential** $`a\,da/Y`$, however, descends through the *different genus-zero quotient* $`a\mapsto a^2`$. It is not the holomorphic elliptic differential $`da/Y`$, and it does not become the Lamé spectral quasimomentum or the Riemann height simply by composing this isogeny. The V4 involution characters from draft 150 remain essential.

## 22. Catenoid, helicoid, and Riemann minimal examples: a domain- and period-safe comparison [D,H,K,C]

The order-one PT soliton endpoint of §19 carries the marked rational coordinate

```math
t=\frac{s-r}{s+r}=e^{r(u+iv_{\rm ang})},\qquad g_C=-t,\qquad dh_C=\frac1r\,d\log t.
```

The Euclidean catenoid Weierstrass triple is

```math
\boldsymbol\Phi_C=\left(\frac12(g_C^{-1}-g_C),\frac i2(g_C^{-1}+g_C),1\right)dh_C,\qquad X_C=\mathrm{Re}\int\boldsymbol\Phi_C.
```

The first two forms are meromorphic exact derivatives and the height form has a pure imaginary loop period,

```math
\oint\boldsymbol\Phi_C=(0,0,2\pi i/r),\qquad \mathrm{Re}\oint\boldsymbol\Phi_C=0.
```

Thus the catenoid immersion closes on the punctured-plane conformal domain. The Bonnet associate $`e^{i\delta}\boldsymbol\Phi_C`$ has **real** period $`(0,0,-2\pi\sin\delta/r)`$, so the helicoid $`\delta=\pi/2`$ is defined on the unwrapped angular cover rather than the same punctured-plane quotient.

For Riemann minimal examples, the curve is instead **smooth elliptic** for every $`\lambda_R>0`$ and the actual real translation/flux vectors are given in the verified H467 register. Theorem 17.1 transports the entire marked Riemann Weierstrass differential triple to **the selected smooth Lamé spectral curve**, but the real period-closing equations still require the chosen cycles and the immersion translation lattice.

At the soliton endpoint $`\lambda_R\to0`$ one has $`m\to1`$ and the smooth elliptic curve degenerates to a node. After appropriate geometric rescaling, Riemann minimal examples can have **catenoidal** limits; at the opposite end $`\lambda_R\to\infty`$ they can have **helicoidal** limits (Meeks–Pérez–Ros). The finite-parameter algebraic isomorphism of §15 has coefficients diverging at these endpoints, so passing to a *geometric immersion limit* requires simultaneously rescaling the Weierstrass forms and controlling their real periods. Algebraic convergence of the spectral cubic alone is not a proof of a globally embedded limiting surface.

### 22.1 The catenoid surface Jacobi operator is still a different Hilbert operator

For the induced metric $`I_C=R(u)^2(du^2+dv_{\rm ang}^2)`$, the negative Jacobi expression on angular mode $`e^{im_{\rm ang}rv_{\rm ang}}`$ is

```math
B_{m_{\rm ang}}=R^{-2}\left[-\partial_u^2+(m_{\rm ang}^2r^2-2r^2S^2)\right].
```

On the natural surface radial Hilbert space $`L^2(R^2du)`$, the **actual unitary** half-density conjugation produces

```math
R B_{m_{\rm ang}}R^{-1}=-\partial_u(S^2\partial_u)+(m_{\rm ang}^2-1)r^2S^2.
```

This is not globally unitarily identical to the flat-measure $`h_1=-\partial_u^2-2r^2S^2`$ merely because their **zero equations** coincide after multiplication by $`R^2`$. The complete catenoid and helicoid also have different global angular domain topologies.

This distinction is central to the proposed theory: **equality of local ODEs, isomorphism of marked spectral curves, and unitary equivalence of global operators are three different mathematical arrows**.

## 23. The exact spectral Gauss–Manin system is the Riemann period system in a different gauge [D,V,H468]

The spectral-to-Riemann map is more than a pointwise identification of elliptic fibers. The archived Riemann Gauss–Manin system is

```math
\frac d{dk_R}\binom{\Omega_y}{N_y}=\frac1{k_R^2+4}\begin{pmatrix}-k_R/2&-1\\-1&k_R/2\end{pmatrix}\binom{\Omega_y}{N_y},
```

where the **normalized-cubic** periods are

```math
\Omega_y=\oint dg_R/y_R,\qquad N_y=\oint g_R\,dg_R/y_R.
```

Let $`P_{\rm sp}=(I_0,I_1)^T`$ be the two Lamé spectral periods of §17 along the **same transported cycle**. The affine isomorphism gives an explicit **gauge matrix**

```math
\binom{\Omega_y}{N_y}=G(k_R)\binom{I_0}{I_1},\qquad G=\frac r{\sqrt{D_R}}\begin{pmatrix}-1&0\\k_R&D_R/r^2\end{pmatrix}.
```

**Theorem 23.1 [D,V] (degree-one period gauge).**

```math
\det G=-1,\qquad \frac{dm}{dk_R}=\frac2{D_R^3},\qquad D_R=\sqrt{k_R^2+4}=\frac1{\sqrt{m(1-m)}}.
```

The two spectral periods satisfy the following exact first-order **traceless, rational** connection in the Lamé elliptic parameter:

```math
\frac d{dm}\binom{I_0}{I_1}=\frac1{2m(1-m)}\begin{pmatrix}2m-1&r^{-2}\\-r^2(1-m+m^2)&1-2m\end{pmatrix}\binom{I_0}{I_1}.
```

**Proof.** Differentiate $`P_y=G P_{\rm sp}`$ with respect to $`k_R`$, use the archival Gauss–Manin connection $`P_y'=A_R P_y`$, and isolate the spectral vector:

```math
\frac{dP_{\rm sp}}{dk_R}=(G^{-1}A_RG-G^{-1}G')P_{\rm sp}.
```

Direct symbolic simplification gives the explicit intermediate matrix

```math
G^{-1}A_RG-G^{-1}G'=\begin{pmatrix}k_R/D_R^2&(r^2D_R)^{-1}\\-r^2(k_R^2+3)/D_R^3&-k_R/D_R^2\end{pmatrix}.
```

Multiply by $`dk_R/dm=D_R^3/2`$ and use $`k_R=(2m-1)D_R`$, $`D_R^2=1/[m(1-m)]`$ to obtain the boxed rational connection. The determinant identity follows by multiplying the two-by-two matrices; its value is **exactly $`-1`$**, independent of $`m,r`$.

**Independent check [V]:** At $`m=1/4,1/2,7/10`$ the derivative of direct quadratures for $`I_0,I_1`$ agreed with this rational matrix to high precision, with numerical residuals near $`10^{-21}`$ in a 40-digit quadrature. The connection is therefore supported by two independently defined calculations, not simply a restatement of equal modular invariants.

### 23.1 Closed complete-elliptic-integral periods of the Lamé curve

Choose the natural doubled branch-cut cycles $`\beta_{\rm sp}`$ over $`[E_1,E_2]`$ and $`\alpha_{\rm sp}`$ over $`[E_0,E_1]`$ with the explicit orientations for which $`I_0(\beta)`$ is positive real and $`I_0(\alpha)`$ negative imaginary. Direct substitutions in the cubic quadratures give

```math
I_{0,\beta}=\frac4rK(m),\qquad I_{1,\beta}=4r[\mathsf E(m)-mK(m)].
```

```math
I_{0,\alpha}=-\frac{4i}{r}K(1-m),\qquad I_{1,\alpha}=4ir[\mathsf E(1-m)-(1-m)K(1-m)].
```

Here $`K(m)`$ and $`\mathsf E(m)`$ denote complete elliptic integrals of the first and second kind with **parameter $`m`$**, not the geometric energy $`E`$. The formulas may be derived by putting $`E=E_1+(E_2-E_1)t`$ on the $`\beta`$ cut and similarly on the $`\alpha`$ cut; the second-kind integral reduces to $`\mathsf E`$ by differentiation of $`K`$.

### 23.2 The exact constant spectral period determinant

Using the four formulas above and Legendre's relation

```math
K(m)\mathsf E(1-m)+K(1-m)\mathsf E(m)-K(m)K(1-m)=\frac\pi2,
```

one obtains

```math
I_{0,\alpha}I_{1,\beta}-I_{0,\beta}I_{1,\alpha}=-8\pi i.
```

**Theorem 23.2 [D,V,K] (spectral symplectic period identity).** The determinant of the two marked Lamé spectral periods is a nonzero **constant independent of $`m`$ and $`r`$**. Its sign depends on orientations; in the explicitly oriented branch-cut cycles above it is $`-8\pi i`$.

This is the same determinant structure as the archived Riemann period invariant; under the **transported** cycle marking, $`\det G=-1`$ reverses its sign, while taking the modulus and the intersection pairing gives the identical symplectic geometry. This is a rigorous period-level “metric glue” distinct from the original scalar Plancherel norm.

### 23.3 A normalized spectral second-kind period from the same determinant

For a chosen $`\alpha`$ cycle with $`I_{0,\alpha}\ne0`$, define a second-kind differential

```math
dp_{\rm sp}=\frac i2(E-b)\frac{dE}{\eta},\qquad b=\frac{I_{1,\alpha}}{I_{0,\alpha}}.
```

This has zero $`\alpha`$ period; on the sheet with $`\eta\sim iE^{3/2}`$ it has the standard high-energy principal asymptotic $`dp_{\rm sp}\sim dE/(2\sqrt E)`$.

Its $`\beta`$ period follows *exactly* from the determinant:

```math
\oint_{\beta}dp_{\rm sp}=\frac i2\frac{I_{0,\alpha}I_{1,\beta}-I_{0,\beta}I_{1,\alpha}}{I_{0,\alpha}}=\frac{4\pi}{I_{0,\alpha}}=\frac{i\pi r}{K(1-m)}.
```

This is the precise relation between a **normalized spectral second-kind differential** and the two marked periods that also determine Riemann's immersion forms. It does **not** identify $`dp_{\rm sp}`$ itself with the Riemann **holomorphic** height form; the former has a prescribed pole at spectral infinity, while the latter does not.

## 24. Conditional Sturm–Liouville–Ermakov–Pinney correspondence and geometric realization theorem [D,K,H]

**Theorem 24.1 (typed SL–EP correspondence and selected geometric realization).** Fix $`r,c,\mu>0`$. Consider any real SL expression with $`p,w>0`$ and sufficient regularity, and declare its weighted Hilbert space, interval and domain. Under the additional choices stated below, the following statements hold.

**(I) Local Liouville–Riccati–Pinney equivalence.** The scalar SL equation is locally mapped by a Liouville half-density to a Schrödinger carrier; a nonvanishing complex carrier has a Riccati logarithmic derivative, positive Milne amplitude, conserved current and an EP equation; the symmetric-square envelope obeys a third-order **linear** equation and fixed quadratic invariant. These assertions do not require an operator spectral theorem.

**(II) Weighted Hilbert/domain compatibility.** A Liouville map extends to an exact unitary equivalence of selected self-adjoint realizations **when the domains are carried along**. For the original profile this map is $`f\mapsto xf`$ with $`u=\ln(x/c)`$ and measure $`x\,dx`$. For the integer PT well, the Crum polar isometry intertwines only the absolutely continuous subspace with the free operator; bound states constitute a finite-dimensional kernel and must be included in distorted Fourier–Mellin Plancherel.

**(III) Selected algebro-geometric spectral closure.** For integer PT the verified Lax–Novikov/Burchnall–Chaundy polynomial yields a **nodal** spectral curve. For the separately selected one-gap Lamé periodic family $`L_m`$, $`0<m<1`$, the corresponding spectral curve $`\Gamma_m`$ is smooth elliptic, and the two nodal endpoints $`m\to0,1`$ have different operator interpretations (§13).

**(IV) Selected exact surface realization.** If one further chooses $`\lambda_R>0`$ and sets $`m=(1+\lambda_R^2)^{-1}`$, the **explicit degree-one real isomorphism** of Theorem 15.1 identifies $`\Gamma_m`$ with the real Riemann elliptic fiber. It transports the entire meromorphic Weierstrass triple and marked period vectors by Theorems 16–17 and 23. The resulting surface is the selected Riemann immersion **provided** its specified real period/translation-lattice closing equations are imposed. The finite-gap *quasimomentum* remains a different meromorphic differential from the geometric holomorphic height.

**(V) Two singular primitive realizations.** At $`m\to1`$, the limiting smooth elliptic holomorphic spectral differential becomes the **catenoid logarithmic height form** on the marked rational normalization, with an imaginary closing period; its Bonnet conjugate helicoid has a real nonclosing height period on the same punctured-plane quotient. At $`m\to0`$, the other nodal limit becomes the **original arctangent primitive** after the specified real projective identification and amplitude factor. These are statements about *normalized curves with marked forms*, not a universal isometry between the free, PT, Riemann, and minimal-surface Jacobi operators.

**(VI) Non-equivalences.** None of (I)–(V) asserts that a Jordan **transfer** matrix means broken Hilbert self-adjointness; that every local EP amplitude is a separatrix; that a node forces a spatial Jordan block; that every nonlinear equation is linearizable; or that a scalar weighted $`L^2`$ norm alone determines a Riemann period lattice, a Berry/Chern number, or physical dynamics.

**Proof.** (I) is the direct derivation in §§3–5; (II) is §3 together with the operator-theoretic Darboux results audited in drafts 120/140; (III) is §§12–13 and H100/H299; (IV) is the explicitly invertible affine curve map and full meromorphic pullbacks in §§14–18/23; (V) is the exact limiting calculation of §19 and the period formulas in drafts 160/§22; (VI) follows from the constructed counterexamples §§9–11, the two distinct spectral degenerations §13, and Riemann–Hurwitz/differential pole divisors. All arrows have named source objects and explicit additional hypotheses.

**Status qualification:** This is a **conditional theorem schema with proved component identities** and classical analytic inputs, not a universal classification of all Sturm–Liouville operators or all minimal surfaces. The bundle/Hodge, operator-domain and real-period conditions are not erased by the existence of the common differential-algebraic core. It is suitable for a future audited foundational proposition, not automatic promotion to the main paper.

## 25. The Hilbert-space and spectral-analysis consequences must be typed [D,K,C]

### 25.1 What the original weighted metric guarantees

The canonical unitary map is

```math
U_cf(u)=xf(ce^u),\qquad\|f\|^2_{L^2(xdx)}=\|U_cf\|^2_{L^2(du)}.
```

For the canonical profile,

```math
U_cf_\mu=\frac{S}{2\sqrt\mu},\quad\|f_\mu\|^2_{L^2(xdx)}=\frac1{2r\mu},\quad\widehat{U_cf_\mu}(k)=\frac{\pi}{2r\sqrt{2\pi\mu}}\mathrm{sech}\left(\frac{\pi k}{2r}\right).
```

Thus ordinary Fourier–Plancherel in $`u`$ is multiplicative Fourier–Mellin Plancherel in $`x`$. Weighted Sobolev spaces and the self-adjoint dilation generator follow by transporting domains. The uncertainty product $`\sigma_u\sigma_k=\pi/6`$ is a **specific profile invariant**, not a universal minimum or a surface period.

### 25.2 A chosen weighted Lamé operator has a different spectral transform

To transport the selected **unshifted** Lamé operator to the original weighted Hilbert space, define the new coefficient expression

```math
(\tau_{m,x}f)(x)=\frac1x\left[-(x^3f_x)_x+x\big(V_m(\ln(x/c))-1\big)f\right],\qquad V_m(u)=2mr^2\mathrm{sn}^2(ru\mid m)-2mr^2.
```

The $`-1`$ appears because the Liouville half-density contributes $`+1`$ to the Schrödinger potential. Consequently

```math
U_c\tau_{m,x}U_c^{-1}=-\partial_u^2+V_m(u)=L_m.
```

This $`\tau_{m,x}`$ is a **new selected weighted SL expression**, not the original free linear Master carrier. Its spectral variable is the Lamé energy $`E`$.

For $`0<m<1`$, the real periodic potential requires a **Bloch–Floquet direct-integral spectral transform** with bands and an open finite gap. Free Mellin characters alone do not diagonalize it. At $`m\to0`$ the transform reduces to ordinary Fourier–Mellin; at $`m\to1`$ the correct limit is the **Darboux-distorted Fourier–Mellin transform plus a discrete bound-state correction** from draft 140. This is the Hilbert-space counterpart of the two distinct nodal spectral limits.

### 25.3 The catenoid area metric produces yet another operator

The canonical catenoid has $`I_C=R^2(du^2+dv_{\rm ang}^2)`$ and $`dA_C=R^2du\,dv_{\rm ang}`$. Drafts 130/140 construct an isometric embedding of the original weighted $`L^2(xdx)`$ into its angularly constant scalar $`L^2`$ sector. But the genuine unitary transformed surface Jacobi operator on angular mode $`m_{\rm ang}`$ is

```math
\widetilde B_{m_{\rm ang}}=-\partial_u(S^2\partial_u)+(m_{\rm ang}^2-1)r^2S^2,
```

not the flat-measure PT Schrödinger operator. Equality of their **zero equations after multiplication by $`R^2`$** is not equality of global self-adjoint operator domains or spectral measures.

### 25.4 A positive EP envelope is not a conserved Hilbert norm

A real positive $`a(t)`$ is a **pointwise nonlinear envelope** of a carrier. Its Wronskian/Pinney invariant does not assert conservation of $`\int w|y|^2dx`$ under an unspecified dynamical evolution. Hilbert norm conservation requires separately specifying a unitary evolution. In general, a real positive EP amplitude can grow without bound and need not be square-integrable. The mathematical dictionary can be used for scattering, stability, and quantum-mechanical operators **after** an actual self-adjoint realization has been supplied, without forcing a physical implementation.

## 26. Complete r=2 regression with c and mu explicit [D,V]

Fix the framework's resolution at $`r=2`$ but retain $`c,\mu>0`$:

```math
u=\ln(x/c),\quad S_2=\frac{2c^2x^2}{x^4+c^4},\quad W_2=\frac{x^4-c^4}{x^4+c^4},\quad f_\mu(x;2,c)=\frac{c^2x}{\sqrt\mu(x^4+c^4)}.
```

The original norm, integral halves and catenoid vertical flux are

```math
\|f_\mu\|^2_{L^2(xdx)}=\frac1{4\mu},\quad\int_0^c f_\mu dx=\int_c^\infty f_\mu dx=\frac{\pi}{8\sqrt\mu},\quad F_{C,3}=\pi.
```

At $`\lambda_R=1`$ the elliptic modulus is $`m=1/2`$, with $`D_R=2`$ and $`k_R=0`$. The Lamé spectral curve is

```math
\Gamma_{1/2}:\quad\eta^2=-(E+2)E(E-2),\qquad(E_0,E_1,E_2)=(-2,0,2).
```

The Riemann elliptic isomorphism is

```math
g_R=-E/2,\qquad y_R=\frac{\sqrt2}{4}\eta,\qquad\frac{dg_R}{w_R}=-\sqrt2\,\frac{dE}{\eta}.
```

The spectral Gauss–Manin connection at $`m=1/2`$ becomes

```math
\left.\frac d{dm}\binom{I_0}{I_1}\right|_{m=1/2}=\begin{pmatrix}0&1/2\\-6&0\end{pmatrix}\binom{I_0}{I_1}.
```

Writing $`K_*=K(1/2)`$ and $`\mathsf E_*=\mathsf E(1/2)`$, the two marked spectral period pairs are

```math
I_{0,\beta}=2K_*,\quad I_{1,\beta}=8(\mathsf E_*-K_*/2),\quad I_{0,\alpha}=-2iK_*,\quad I_{1,\alpha}=8i(\mathsf E_*-K_*/2).
```

Their determinant is exactly $`-8\pi i`$ by Legendre's relation. The selected spectral second-kind differential's $`\beta`$ period is $`2\pi i/K_*`$ with the declared marking.

### 26.1 The centered Pinney 2-isogeny meets this same smooth Lamé spectral curve

At $`r=2`$ the Pinney mechanical quartic is

```math
Y^2=a^4-\mu,\qquad E=-2a^2/\sqrt\mu,\qquad\eta=2\sqrt2\,aY/\mu^{3/4}.
```

The holomorphic pullback is

```math
\Psi^*(dE/\eta)=-\sqrt2\,\mu^{1/4}da/Y.
```

### 26.2 Both singular primitive endpoints

At the $`m\to1`$ soliton endpoint,

```math
\eta^2=-E(E+4)^2,\quad E=-s^2,\quad\omega_{\rm sol}=\frac{2\,ds}{s^2-4},\quad\oint dh_C=\pi i.
```

At the $`m\to0`$ free closed-gap endpoint,

```math
\eta^2=-E(E-4)^2,\quad E=-s^2,\quad\omega_{\rm free}=-\frac{2\,ds}{s^2+4},\quad f_\mu(x;2,c)dx=-\omega_{\rm free}/(2\sqrt\mu).
```

At $`m\to0`$ the finite spatial period is $`\pi/2`$, and the self-adjoint free transfer at $`E=4`$ is **semisimple $`M=-I`$**. At $`m\to1`$ the primitive period diverges and the isolated PT bound state lies at $`E=-4`$. Throughout, $`c`$ is the log origin and $`\mu`$ the original amplitude/norm normalization: neither becomes the elliptic modulus or spectral energy.

## 27. Independent evidence, historical provenance and literature

### 27.1 Exact or independent checks in this investigation

1. **Free Hill discriminant:** its derivative at zero is $`-L^2`$, while at every positive free periodic/antiperiodic double level the derivative vanishes and the transfer matrix is $`\pm I`$. Both statements follow directly by expanding $`2\cos(L\sqrt\lambda)`$.
2. **Genuine complex-potential exceptional point:** the substitution $`z=\sqrt\alpha e^{iu}`$ converts the complex exponential Hill equation into Bessel's equation. DLMF's exact continuation formula makes $`Y_n`$ acquire $`4iJ_n`$ on one circuit. The finite-period characteristic determinant vanishes quadratically at $`\lambda=n^2`$, $`n\ge1`$, while the periodic eigenfunction space is one-dimensional. Antiperiodic half-integer-square eigenvalues remain semisimple even for the same nonreal potential.
3. **Domain distinction:** regular periodic Green-function boundary corrections contain the matrix inverse $`(M-\sigma I)^{-1}`$; its adjugate cancels a potential double pole at semisimple $`M=\sigma I`$, but not at a genuine Jordan $`M\ne\sigma I`$ with a quadratic characteristic root. This is not a claim about the whole-line nonselfadjoint spectrum.
4. **Complex Milne equations:** direct separation of real and imaginary parts gives the extra current derivative $`j'=(\mathrm{Im}V-\mathrm{Im}\lambda)a^2`$. The real constant-strength EP correspondence has **both** real potential and real spectral-parameter assumptions.
5. **Lamé band edges:** substitution of Jacobi $`\mathrm{dn},\mathrm{cn},\mathrm{sn}`$ in the shifted one-gap Lamé operator produces the three displayed energies $`E_0,E_1,E_2`$. Exact limits of those roots at $`m=0,1`$ give **different** nodes, respectively free closed gap and PT collapsed allowed band.
6. **Full Lamé–Riemann curve isomorphism:** exact SymPy polynomial reduction proves that $`g_R=-k_R-D_RE/r^2`$, $`y_R=D_R^{3/2}\eta/r^3`$ satisfy $`y_R^2=g_R(g_R-\lambda_R)(g_R+\lambda_R^{-1})`$. The branch images are exactly $`(\lambda_R,0,-1/\lambda_R)`$, and the two rational elliptic $`j`$ invariants agree identically after $`m=1/(1+\lambda_R^2)`$.
7. **Marked differentials:** differentiating the affine map proves $`dg_R/y_R=-(r/\sqrt{D_R})dE/\eta`$ and $`dg_R/w_R=-r\sqrt m\,dE/\eta`$, with the physical Riemann normalization $`w_R=\sqrt{\lambda_R}y_R`$. Pullback of the complete Weierstrass triple and its horizontal exact differential reproduces the existing H466 reduction.
8. **Full spectral period gauge:** the explicitly displayed Gauss–Manin gauge matrix $`G`$ has constant determinant $`-1`$. Symbolic differentiation and simplification produce the rational traceless two-by-two connection in §23. Direct high-precision spectral quadrature, differentiated at $`m=0.25,0.5,0.7`$ with $`r=1.3`$, agrees with this connection to around $`10^{-21}`$ in the quadrature setup.
9. **Marked spectral periods:** direct cubic quadratures yield the displayed complete $`K(m),\mathsf E(m)`$ formulas, and Legendre's relation gives the exactly constant determinant $`-8\pi i`$ in the declared branch-cut orientation. Other cycle orientations change its sign only.
10. **Distinct marked nodal differentials:** at $`m\to1`$, $`E=-s^2`$ gives $`dE/\eta=2ds/(s^2-r^2)`$, exactly the catenoid logarithmic height with residues $`\pm1/r`$. At $`m\to0`$ the other nodal normalization gives $`dE/\eta=-2ds/(s^2+r^2)`$, exactly $`-2\sqrt\mu\,f_\mu dx`$ under the independently verified projective identification of draft 160.
11. **Pinney-to-Lamé degree-two map:** the composed affine expressions $`E=-r^2a^2/(2\sqrt\mu)`$, $`\eta=r^2aY/(\sqrt2\mu^{3/4})`$ have identically vanishing elliptic cubic residual modulo the centered Pinney quartic, and holomorphic pullback factor $`-\sqrt2\mu^{1/4}`$. The degree-one/degree-two Hodge scalings agree.
12. **Complete r=2 regression:** the symmetric spectral branch points, normalized Riemann affine map, rational Gauss–Manin matrix, elliptic period determinant, both nodal rational primitives, catenoid flux, and original weighted norm were recalculated with $`c,\mu`$ explicit.

### 27.2 Historical project results retained rather than renamed

The verified historical ZIP claims H95 and H100/H299 record the integer Lamé spectral polynomials, PT soliton degenerations and exact Crum/Lax–Novikov/Burchnall–Chaundy operator identities. H466–H472 record Riemann minimal-example Weierstrass data, exact differential reduction, marked real translation/flux, Gauss–Manin/Picard–Fuchs, modular $`X_0(4)`$ coordinates and numerical monodromy checks. The Lamé complementary-loci module already reports the Legendre elliptic modulus $`m_R=1/(1+\lambda_R^2)`$ and equality of corresponding $`j`$ invariants.

Drafts 120, 130 and 140 respectively establish domain-safe weighted SL parity, the SL–EP symmetric-square/finite-gap dictionary, and Darboux spectral partial unitarity. Draft 150 develops reflectionless inverse norming and the centered Pinney-to-symmetric-Riemann 2-isogeny. Draft 160 supplies the rational nodal spectral-to-catenoid Weierstrass identification and catenoid/helicoid period distinction.

The **new explicit additions within this draft** are chiefly the domain-specific Bessel exceptional-point counterexample, the complete smooth **real affine spectral-energy map** to every Riemann elliptic fiber, the corresponding Gauss–Manin gauge, the **two distinct limiting rational spectral differentials** unifying the catenoid logarithmic height and the original arctangent primitive, and the composed Pinney-to-smooth-Lamé isogeny. Historical novelty is **not** asserted.

### 27.3 External sources and precise uses

- Bessel analytic continuation and its integer-order formula (DLMF 10.11.6): https://dlmf.nist.gov/10.11 .
- Non-self-adjoint Gasymov-type Hill potentials and spectral-domain qualifications: https://www.sciencedirect.com/science/article/pii/S0022247X1400907X ; https://www.aimsciences.org/article/doi/10.3934/cpaa.2017110 .
- Classical Lamé equations, periodic band edges and Jacobi functions: https://dlmf.nist.gov/29 ; https://www.sciencedirect.com/science/article/pii/S0393044024002237 .
- Real periodic Hill discriminants and closed-gap multiplicity: https://link.springer.com/article/10.1186/s13661-018-1111-y ; https://doi.org/10.1016/J.JDE.2014.09.004 .
- Finite-gap spectral curves and nodal solitonic limits: https://academic.oup.com/integrablesystems/article/4/1/xyz006/5543069 ; https://www.sciencedirect.com/science/article/pii/S0393044017301043 .
- Meeks, Pérez and Ros, Riemann minimal examples and their catenoid/helicoid limits under suitable normalization: https://annals.math.princeton.edu/2015/181-2/p02 ; https://arxiv.org/abs/1609.05660 .
- Complete elliptic integrals and the Legendre relation: https://dlmf.nist.gov/19 .
- General weighted self-adjoint Sturm–Liouville theory: https://encyclopediaofmath.org/wiki/Sturm-Liouville_theory .

**Evidence boundary:** Finite-gap Bloch theory, regular periodic operator algebraic multiplicities, and global embedded Riemann minimal-surface limits are standard mathematical inputs [K]; the displayed algebraic identities were independently derived. The archive's numerical modular/monodromy checks retain their original confidence labels. No operator exceptional point is claimed for a real self-adjoint PT well, and no universal global isometry is claimed merely from equality of local ODEs or curve invariants.

## 28. Final theorem audit and next mathematical targets

| Proposed universal statement | Precisely proved or corrected formulation |
|---|---|
| A Jordan transfer matrix means broken self-adjointness. | **False:** free self-adjoint periodic $`-\partial^2`$ has nontrivial Jordan transfer at zero; its operator eigenvalue is simple (§9). |
| $`\Delta=\pm2`$ and $`\Delta'=0`$ are sufficient for a double Green-resolvent pole. | **False:** at free closed gaps $`M=\pm I`$ and the double eigenvalue is semisimple (§9). A true pole of order two requires an actual operator Jordan chain (§7). |
| Genuine nonselfadjoint exceptional points with double poles can be built from scalar Hill equations. | **True:** the explicitly specified complex exponential potential, Bessel monodromy and periodic domain give one at every positive integer-square energy (§10). |
| The same Floquet discriminant determines whether the operator has Jordan eigenvectors. | **False:** the free and complex Bessel examples have the same $`\Delta`$ but different eigenvector geometry and resolvent pole orders (§§9–10). |
| Ermakov–Pinney positivity tests spectral stability or Hilbert-domain self-adjointness. | **False:** it is a property of chosen Gram and carrier solutions; constant positive EP amplitudes also occur at semisimple free band edges (§§4,9,11). |
| The nonlinear Pinney envelope is linear spectral geometry in disguise. | **Qualified true:** its positive amplitude is a quadratic form in linear carrier solutions with fixed Wronskian/Casimir, but it is not itself a linear self-adjoint eigenvalue operator (§§4–5). |
| All solitons correspond to closed gaps of periodic Hill operators. | **False as stated:** the selected PT soliton is obtained by collapse of a lower *allowed* band as its primitive period diverges; the **different** free limit closes a forbidden gap (§13). |
| A node or pinched elliptic handle forces a Jordan spatial transfer matrix. | **False:** the free closed-gap node has semisimple transfer $`-I`$ while its Picard–Lefschetz **modulus** monodromy is unipotent (§20). |
| PT nodal curves and smooth Riemann minimal example elliptic curves are globally the same algebraic curve. | **False:** their normalizations have different genera (draft 160); a nonconstant morphism from the rational normalization to a smooth elliptic curve is excluded by Riemann–Hurwitz. |
| Smooth one-gap Lamé spectral curves and Riemann elliptic fibers admit a selected exact map for every real modulus. | **True:** the explicit invertible real affine energy/curve map of §15 with $`m=(1+\lambda_R^2)^{-1}`$, preserving a marked holomorphic differential up to scale (§16). |
| The entire Riemann Weierstrass immersion triple transfers to the marked Lamé spectral curve. | **True**, after pulling back the chosen meromorphic Gauss coordinate and height form (§17); immersion-period closing remains a separately imposed global condition. |
| The Lamé spectral and Riemann Gauss–Manin connections are related. | **True:** an explicit gauge with determinant $`-1`$ and parameter change gives the rational spectral connection of §23. The period determinant is $`\pm8\pi i`$, independent of $`m,r`$. |
| Catenoid height and original arctangent come from one marked elliptic spectral family. | **True under the two distinct normalization maps:** $`m\to1`$ yields logarithmic catenoid height, while $`m\to0`$ yields the original rational primitive up to $`-1/(2\sqrt\mu)`$ (§19). |
| Spectral quasimomentum equals the Riemann holomorphic height differential. | **False:** one is normally meromorphic of the second kind at spectral infinity, while the other is holomorphic; the period span can be related, not their pole divisors (§§18,23). |
| A weighted scalar $`L^2`$ norm alone fixes elliptic periods or Berry/Chern integers. | **False:** unitary Liouville/Fourier–Mellin, Hodge period pairings and bundle holonomies are different typed constructions (§25; drafts 120–160). |
| A global SL–EP correspondence and geometric realization can be stated as a theorem. | **Yes, conditionally:** Theorem 24.1 has explicit hypotheses and separately specified maps for each of its local, global operator, finite-gap and geometric pieces. |

### 28.1 Specific follow-up investigations

1. Construct the smooth Lamé odd-order commuting operator **with the current affine spectral normalization**, prove its Burchnall–Chaundy relation on every fiber, and verify degeneration to the existing PT Lax–Novikov operator as $`m\to1`$.
2. Fix oriented integral cycles on the Lamé and Riemann curves and compute the actual integer homology action of the affine isomorphism, checking the curve-family monodromy against the archival $`X_0(4)`$ integral matrices.
3. Derive the normalized spectral quasimomentum directly from Floquet solutions, verify its prescribed principal part and $`a`$ period, then compare its exact $`b`$ period to the period determinant of §23.
4. Construct a **differential- and period-preserving** smoothing of the PT node and prove convergence of all three Weierstrass immersion forms, including the geometric rescaling necessary to obtain a catenoid from Riemann examples.
5. Treat the other free endpoint $`m\to0`$ in the same way, explicitly tracking the resulting arctangent differential, the complex-rotated node markings and the Riemann helicoid scaling.
6. Compare the Hilbert-space Bloch–Floquet transform for $`L_m`$ and the Darboux-distorted Fourier–Mellin transform of its PT limit, including convergence of continuous spectral measures and the isolated bound-state defect.
7. Extend the exact spectral Gauss–Manin gauge from one-gap curves to the genus-two and higher Lamé levels, and use Riemann–Hurwitz plus marked divisor/polarization data to distinguish possible morphisms, correspondences and no-go cases.
8. Construct a boundary-domain-sensitive spectral exceptional-point example in the original $`x`$ variable by transporting the complex Bessel Hill operator under $`u=\ln(x/c)`$, preserving all endpoint and periodic multipliers.
9. Attempt an explicitly defined weighted Hilbert-to-Hodge map for a chosen finite-dimensional subspace, tracking the quadratic form and spectral domain; do not infer one from scalar norm coincidences.
10. Audit every candidate statement in Theorem 24.1 against the repository's historical CLAIMS and the foundational paper, including the external assumptions needed for complex periodic operator Jordan multiplicities and minimal-surface global geometry.

### 28.2 Mathematical structural thesis

The most precise structural thesis supported by this investigation is:

**The Symmetrical Framework is an algebraically rigid but geometrically flexible system of explicitly typed correspondence maps.** Its local rank-two real SL carrier, Riccati projectivization, symmetric-square equation, Gram/Wronskian invariant and positive Pinney envelope form an exact differential-algebraic structure. **Selected** finite-gap potentials add algebraic spectral curves, commuting operators and marked differentials. The **selected one-gap Lamé family** now carries a directly constructed, all-real-modulus elliptic curve isomorphism to the Riemann minimal-example family, together with an exact two-component Gauss–Manin period gauge and two distinct rational nodal realizations: catenoid height and the original arctangent primitive. The global operator, Hilbert measure, spectral boundary conditions, meromorphic polar divisor, homology marking, immersion period lattice and physical interpretation remain **additional independent data**.

**Consequently, the correct equivalences are proved where a specific map preserves specific structures.** There is no unqualified global isomorphism of all SL operators, all EP nonlinear solutions, all soliton spectral curves and all minimal surfaces. Nor is a Jordan transfer matrix an automatic exceptional eigenvalue. The typed conditional Theorem 24.1 is a sound mathematical formulation for future foundational consolidation, with its component identities checked and its global analytic dependencies explicitly visible.
