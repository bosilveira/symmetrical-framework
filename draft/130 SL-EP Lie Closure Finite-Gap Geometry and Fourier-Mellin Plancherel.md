---
id: SF-DRAFT-130
title: SL–EP Lie Closure, Finite-Gap Geometry, and Fourier–Mellin Plancherel
status: provisional
created: 2026-11-18
proposed_layers: [I, II, III, IV]
depends_on: [SF-I-020, SF-DRAFT-020, SF-DRAFT-030, SF-DRAFT-040, SF-DRAFT-050, SF-DRAFT-060, SF-DRAFT-080, SF-DRAFT-090, SF-DRAFT-100, SF-DRAFT-110, SF-DRAFT-120]
related_claims: [H95, H100, H112, H153, H162, H163, H164, H169, H170, H171, H172, H177, H178, H179, H183, H313, H314, H315, H391, H392, H393, H394, H395, H396, H421, H424, H466, H467, H468, H469, H470, H471, H472, H477]
---

# 130 SL–EP Lie Closure, Finite-Gap Geometry, and Fourier–Mellin Plancherel

**Status:** Extensive provisional mathematical investigation. [D] direct derivation; [V] independent exact symbolic verification; [K] established mathematics under stated hypotheses; [H] archived result retaining its checking status; [C] correction/counterexample; [O] open. No physical interpretation is inferred from sharing a differential equation.

**Research question.** Does the Symmetrical Framework already contain a finite-dimensional closed Sturm–Liouville–Ermakov–Pinney (SL–EP) mechanism? How do projective Jordan blocks, Virasoro coadjoint orbits, finite-gap KdV potentials, minimal-surface period constraints, and Berry/Chern quantization relate? Does the weighted $L^2$ metric supply a common Fourier–Mellin/Sobolev language?

**Central answer.** A **finite-dimensional nonautonomous Lie–Hamilton closure** exists exactly: the same rank-two linear carrier, its Riccati flow, symmetric-square quadratic envelope and Pinney Hamiltonian evolve in $\mathfrak{sl}_2(\mathbb R)$ with a fixed Casimir. This is true for *arbitrary externally prescribed real* frequency, but it does not automatically close the frequency itself as a dynamical variable. There is a **stronger selected spectral closure** for the framework's Pöschl–Teller integer wells: polynomial solutions of that *same* symmetric-square equation have conserved polynomials factoring into the known continuum threshold and bound-state levels. Period constraints and Chern quantization are further typed constructions requiring global geometric data. The canonical logarithmic weighted $L^2$ metric is exactly Fourier–Mellin unitary, but does not alone determine an elliptic period lattice or Berry holonomy.

**Sources actually inspected:** The user's Jordan-block image and typed proposal; the live GitHub foundational chapter SF-I-020 and drafts 020, 030, 040, 050, 060, 080–120; the historical ZIP's spectral-calculus, plancherel-elastica-modular, mellin-beta-heun-lame, binary-quartic-and-spectral-curves, modular-riccati, and riemann-marked-periods-gauss-manin-x04 investigations (H162–H183, H391–H396, H466 onward). External Virasoro, finite-gap, Berry and Mellin sources appear in the references. The polynomial finite-gap certificates below were independently checked with exact symbolic differentiation.

## 1. Four inequivalent notions of closure

| Closure | Mathematical carrier | What actually closes | What is still needed |
|---|---|---|---|
| Lie–Hamilton [D] | a real linear carrier, $\mathfrak{sl}_2$, symmetric square and Casimir | Riccati/projective flow and positive Pinney envelope | prescribed frequency and operator domain |
| Spectral/finite-gap [D,K] | stationary KdV-restricted Schrödinger potential | polynomial squared eigenfunctions and hyperelliptic spectral curve | stationary KdV constraints, spectral parameter and marked cycles |
| Global surface/period [H,K] | meromorphic Weierstrass data, Gauss–Manin connection | periods and some real closing conditions | cycles, immersion differential, topology and embeddedness |
| Bundle/topological [H,K] | normalized spinor and $U(1)$ connection | integral first Chern class and global flux | two-dimensional compact base and patching |

The same elementary hyperbolic functions may populate several rows. They do not make the resulting geometric objects isomorphic without specifying the maps and what those maps preserve.

## 2. Canonical symbols, parameters and distinct clocks

Fix

```math
r>0,\quad c>0,\quad\mu>0,\quad x>0,\quad u=\ln(x/c),\quad x=ce^u,\quad S=\mathrm{sech}(ru),\quad W=\tanh(ru),\quad R=\cosh(ru).
```

The normalized original rational function is

```math
f_\mu(x;r,c)=\frac{S}{2\sqrt\mu\,x},\qquad S^2+W^2=1,\qquad S_u=-rSW,\qquad W_u=rS^2.
```

For general SL–EP use a real coefficient $\omega^2(u)$ (which may take *negative* values) and an independent Pinney strength $k_{\rm EP}$:

```math
\phi_{uu}+\omega^2(u)\phi=0,\qquad a_{uu}+\omega^2(u)a=k_{\rm EP}a^{-3},\quad a>0.
```

Let $\lambda$ be a spectral parameter, $\tau$ a KdV deformation time, $\zeta=u+iv$ a surface coordinate, $\lambda_R>0$ a Riemann minimal-example modulus and $k_R=\lambda_R^{-1}-\lambda_R$ its base coordinate. Their roles do not collapse. The **half-rate** canonical carrier uses

```math
\omega^2=-r^2/4,\quad \phi_\pm=e^{\pm ru/2},\quad k_{\rm EP}=\mu r^2/4.
```

The **full-rate** linear part of the Master equation instead gives $-\partial_u^2+r^2$. Their link is the *symmetric square*, not a common eigenfunction or a change of physical interpretation.

## 3. A Jordan transfer matrix is not broken self-adjointness [C,V]

For $\phi_{uu}+\omega^2(u)\phi=0$, introduce the first-order matrix

```math
\binom{\phi}{\phi_u}_u=A(u)\binom{\phi}{\phi_u},\qquad A(u)=\begin{pmatrix}0&1\\-\omega^2(u)&0\end{pmatrix}\in\mathfrak{sl}_2(\mathbb R).
```

If $\omega^2$ is constant, then

```math
A^2=-\omega^2I,\qquad \det A=\omega^2,\qquad \mathrm{tr}\,A=0.
```

Positive $\omega^2$ gives an elliptic rotation generator, negative $\omega^2$ a hyperbolic generator, and zero a nonzero nilpotent shear. For a *variable* coefficient, the fundamental matrix is a time-ordered exponential. A turning point $\omega^2(u_0)=0$ makes $A(u_0)$ instantaneously nilpotent, but says neither that the entire monodromy is defective nor that the Hilbert-space operator is non-self-adjoint. Local Airy behavior is the generic simple-turning-point normal form.

**Explicit counterexample.** The self-adjoint operator $H=-d^2/du^2$ on a circle of circumference $L>0$ with periodic $H^2$ domain has eigenvalue $\lambda=0$. Its transfer matrix at this eigenvalue is

```math
M(0)=\begin{pmatrix}1&L\\0&1\end{pmatrix},\quad \det M=1,\quad [M(0)-I]^2=0,\quad M(0)\ne I.
```

It has a genuine $2\times2$ Jordan block while $H=H^*$ remains true. A defective **transfer/monodromy matrix** at a self-adjoint band edge is not a defective **Hilbert-space eigenoperator**.

For a real periodic Hill operator, the global Floquet discriminant $\mathfrak D(\lambda)=\mathrm{tr}\,M(\lambda)$ has regimes $|\mathfrak D|<2$ (elliptic), $|\mathfrak D|>2$ (hyperbolic), and $|\mathfrak D|=2$ (parabolic Jordan *or* $\pm I$). These are real **transfer dynamics**, not tests for broken self-adjointness. For complex $SL_2(\mathbb C)$ monodromies the real three-type classification requires further qualification.

## 4. The exact finite Lie–Hamilton algebra of Pinney [D,V,K]

On a canonical phase plane $(a,p)$ with $\{a,p\}=1$ and $p=a_u$, define

```math
H_0=\frac12(p^2+k_{\rm EP}a^{-2}),\qquad D=\frac12ap,\qquad K=\frac12a^2.
```

The Poisson brackets **close** with three generators:

```math
\{D,H_0\}=H_0,\qquad\{D,K\}=-K,\qquad\{K,H_0\}=2D.
```

This is the $\mathfrak{sl}_2(\mathbb R)$ conformal/Ermakov Lie–Hamilton algebra. The time-dependent Pinney Hamiltonian is

```math
H_{\rm EP}(u)=H_0+\omega^2(u)K=\frac{p^2}2+\frac{k_{\rm EP}}{2a^2}+\frac{\omega^2(u)}2a^2.
```

Its **quadratic Casimir level** is exactly

```math
\mathcal C=H_0K-D^2=k_{\rm EP}/4.
```

Differentiate $K,D,H_0$ using the Poisson brackets to obtain a *closed linear* three-dimensional system:

```math
K_u=2D,\qquad D_u=H_0-\omega^2K,\qquad(H_0)_u=-2\omega^2D.
```

```math
\frac d{du}\begin{pmatrix}K\\D\\H_0\end{pmatrix}=\begin{pmatrix}0&2&0\\-\omega^2&0&1\\0&-2\omega^2&0\end{pmatrix}\begin{pmatrix}K\\D\\H_0\end{pmatrix}.
```

**Theorem 4.1 [D,V].** This system conserves $\mathcal C$ and reconstructs a positive Pinney amplitude by $a=\sqrt{2K}$ wherever $K>0$. It closes for any **given** real coefficient function $\omega^2(u)$, with no derivative tower in the dynamical variables $(K,D,H_0)$.

### 4.1 The symmetric-square invariant

Put $J=a^2=2K$. The three-dimensional system implies

```math
J_{uuu}+4\omega^2J_u+2(\omega^2)_uJ=0
```

and the **fixed** Pinney constraint

```math
2JJ_{uu}-J_u^2+4\omega^2J^2=4k_{\rm EP}.
```

If $\phi_1,\phi_2$ form a fundamental pair of the linear carrier, its symmetric-square general solution is

```math
J=A_G\phi_1^2+2C_G\phi_1\phi_2+B_G\phi_2^2,\qquad k_{\rm EP}=(A_GB_G-C_G^2)\mathscr W^2.
```

Here $\mathscr W=\phi_1\phi_{2,u}-\phi_{1,u}\phi_2$ is the carrier Wronskian. Thus **rank-two SL, projective Riccati, symmetric-square rank-three, and nonlinear EP** are one finite Lie–Hamilton diagram once a real carrier is supplied. The determinant is the Gram quadratic invariant, not automatically a smooth elliptic binary-quartic invariant.

## 5. The remaining obstacle: the frequency does not evolve by itself [C]

The Lie closure of §4 is **nonautonomous**. An arbitrary smooth $\omega^2(u)$ is an external coefficient, not an equation of motion for the frequency. Adding it as another unknown without an evolution law leaves an underdetermined system; differentiating an arbitrary function brings its arbitrarily high jets. No universal finite-dimensional autonomous closure for all smooth potentials follows. A constant-frequency restriction, a separately chosen algebraic differential equation, or a stationary finite-gap KdV condition provides additional closure **by assumption and proof**.

## 6. The canonical closed hyperbolic subnetwork [D,V]

For the actual framework choose $\omega^2=-r^2/4$, $k_{\rm EP}=\mu r^2/4$ and the centered positive envelope

```math
a^2=J=\sqrt\mu\cosh(ru),\qquad J_{uu}=r^2J,\qquad J_u^2=r^2(J^2-\mu).
```

The fields $S,W$ satisfy the polynomial differential system $S_u=-rSW$, $W_u=rS^2$ with invariant $S^2+W^2=1$. Thus the canonical special-function field is finite-generated as a differential algebraic field, though the vector space of its arbitrary rational expressions is not finite-dimensional.

The complex carrier

```math
\Phi=\mu^{1/4}\left[\cosh(ru/2)+i\sinh(ru/2)\right],\qquad\Phi_{uu}=\frac{r^2}{4}\Phi,\qquad|\Phi|^2=J
```

has the exact Riccati logarithmic derivative

```math
\frac{\Phi_u}{\Phi}=\frac r2(W+iS),\qquad \left(\frac{\Phi_u}{\Phi}\right)_u+\left(\frac{\Phi_u}{\Phi}\right)^2=\frac{r^2}{4}.
```

With $\vartheta=\arg\Phi$, its imaginary part is the Milne phase speed and its integral is the Gudermannian:

```math
\vartheta_u=\frac r2S,\qquad \vartheta(u)=\arctan(e^{ru})-\frac\pi4=\frac12\mathrm{gd}(ru).
```

## 7. Projectivization, Cayley, and the Hopf base [D,K]

The half-rate real carrier gives the projective coordinate

```math
t(u)=\phi_+/\phi_-=e^{ru}=(x/c)^r,\qquad\{t,u\}=-r^2/2.
```

Its Cayley transform is the canonical circle

```math
\frac{t+i}{t-i}=W+iS,\qquad S^2+W^2=1.
```

The real projective line $\mathbb{RP}^1$ is topologically a circle, while its complexification $\mathbb{CP}^1$ is a two-sphere. The projective ratio lives on the **base** of the Hopf fibration. An actual Hopf $S^1$ fiber requires a separately chosen normalized complex two-component spinor and common phase. The complex scalar Milne phase $\arg\Phi$ is likewise not automatically the Berry connection's fiber holonomy.
