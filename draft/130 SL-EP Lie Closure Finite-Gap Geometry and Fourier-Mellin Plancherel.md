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

## 8. Virasoro projective connections: a true extension, not a finite orbit [K,C]

For the real Hill equation $\phi_{uu}+q(u)\phi=0$, the ratio $F=\phi_1/\phi_2$ of independent solutions obeys the projective identity

```math
\{F,u\}=2q(u).
```

Under a monotone smooth coordinate change $u=\chi(s)$, the **Schwarzian chain rule** gives

```math
\{F\circ\chi,s\}=\chi_s^2\{F,u\}\circ\chi+\{\chi,s\}.
```

Consequently the transformed projective coefficient is

```math
\widetilde q(s)=\chi_s^2q(\chi(s))+\frac12\{\chi,s\}.
```

The inhomogeneous Schwarzian is the projective cocycle underlying the Virasoro coadjoint action once $q$ is defined on an oriented circle with the appropriate density/central-charge convention. **The full Virasoro algebra and the generic coadjoint orbit are infinite-dimensional**: the finite-dimensional $\mathfrak{sl}_2$ in §4 is a distinguished subalgebra/representation, not a claim that the whole orbit is a three-dimensional Poisson manifold. This distinguishes the finite-dimensional Lie–Hamilton closure from the larger group of reparametrizations.

On a circle, the projective developing map and lifted monodromy have their own global orbit invariants, including winding/degree information beyond the matrix conjugacy class. None of this determines a self-adjoint Hilbert-space domain automatically. A general coordinate reparametrization of a Hill coefficient is not automatically a unitary equivalence of self-adjoint operators unless the amplitude, measure and boundary conditions are also transported.

### 8.1 The Schwarzian has an exact canonical value

For the framework's half-rate ratio $F=e^{ru}$, the projective coefficient is $q=-r^2/4$:

```math
\{e^{ru},u\}=-r^2/2=2q.
```

This is a constant projective connection with a hyperbolic real developing map on the logarithmic line. To obtain a *periodic Hill/Virasoro* problem one must separately choose a circle quotient, projective monodromy and compatible potential; the full real line does not become a circle simply because its Riccati flow lies in $SL_2$.

## 9. Finite-gap closure starts from the SAME symmetric-square identity [D,K]

Introduce a real Schrödinger potential $V(u)$ and a spectral parameter $\lambda$:

```math
L_V=-\partial_u^2+V(u),\qquad L_V\phi=\lambda\phi,\qquad \phi_{uu}=(V-\lambda)\phi.
```

For a product of two linear carrier solutions or any symmetric-square solution $F(\lambda,u)$, the third-order differential equation is

```math
F_{uuu}-4(V-\lambda)F_u-2V_uF=0.
```

Differentiate the expression

```math
\mathscr R(\lambda)=-2FF_{uu}+F_u^2+4(V-\lambda)F^2.
```

One obtains

```math
\partial_u\mathscr R=-2F[F_{uuu}-4(V-\lambda)F_u-2V_uF]=0.
```

Thus $\mathscr R$ is independent of $u$. For $F>0$, the envelope $a=\sqrt F$ satisfies

```math
a_{uu}=(V-\lambda)a+k_{\rm EP}(\lambda)a^{-3},\qquad k_{\rm EP}(\lambda)=-\mathscr R(\lambda)/4.
```

**Theorem 9.1 [D,V].** The Gel'fand–Dikii squared-eigenfunction equation, the Pinney symmetric-square equation and their invariant are literally the **same differential system**, after setting $\omega^2=\lambda-V$ and $J=F$. This identifies their algebraic mechanisms without identifying an arbitrary Pinney amplitude with the diagonal resolvent of a self-adjoint operator.

### 9.1 The special polynomial ansatz

A potential is stationary finite-gap/algebro-geometric when suitable additional conditions permit a polynomial

```math
F_g(\lambda,u)=\lambda^g+f_{g-1}(u)\lambda^{g-1}+\cdots+f_0(u)
```

to satisfy the third-order equation for every $\lambda$. Its conserved polynomial $\mathscr R_g(\lambda)$ generically has degree $2g+1$ and defines an auxiliary hyperelliptic spectral curve

```math
\nu^2=\mathscr R_g(\lambda).
```

At a smooth finite-gap curve of genus $g$, the marked spectral data/periods are genuine higher-genus objects. When roots of $\mathscr R_g$ collide, the curve becomes singular and a solitonic/reflectionless limit may result. For the canonical hyperbolic Pöschl–Teller wells below, **the curves are degenerate**, not smooth genus-one or genus-two spectral curves.

The polynomial condition is a **new restriction on $V$**. It cannot be inferred from the mere existence of the Lie–Hamilton closure of §4, which holds for arbitrary prescribed coefficients.

## 10. KdV supplies a spectral potential evolution, but not a generic finite ODE [K,C]

For a time-dependent potential $V(u,\tau)$, the KdV Lax pair uses

```math
L=-\partial_u^2+V,\qquad P=-4\partial_u^3+6V\partial_u+3V_u.
```

The Lax equation $L_\tau=[P,L]$ gives the selected KdV sign convention

```math
V_\tau=6VV_u-V_{uuu}.
```

The isospectral property requires suitable spatial operator domains, decay or periodic hypotheses. KdV is a nonlinear PDE on an infinite-dimensional function space in general. Restricting it to a **finite-gap invariant manifold** with specified smooth spectral curve and divisor leads to finite-dimensional Abelian motion on a Jacobian. This is the spectral closure route; it is *not* a theorem that every Sturm–Liouville potential evolves in a finite-dimensional closed ODE.

The canonical order-one $\mathrm{sech}^2$ well can be inserted into a travelling KdV soliton. Higher integer Pöschl–Teller wells belong to the stationary higher-flow/soliton-degeneration hierarchy; they need not be stationary under the *first* KdV time without a suitable evolution of their scattering data.

## 11. A computational certificate for spectral closure [D,V]

Set $W=\tanh(ru)$, $S^2=1-W^2$. Differentiation in $u$ becomes a polynomial derivation on functions of $W$:

```math
\frac d{du}=r(1-W^2)\frac d{dW}.
```

For each integer $n>0$ introduce the unshifted hyperbolic potential

```math
V_n(u)=-n(n+1)r^2S^2.
```

The archive already describes the order-one catenoid Jacobi and order-two Master Hessian Pöschl–Teller wells, and their connection to Lamé degenerations. The following **explicit polynomial squared-eigenfunctions and factored conserved polynomials** make their finite-dimensional spectral closure completely transparent. They were independently checked exactly using the polynomial derivation above.

## 12. Exact order-one closure: the catenoid Pöschl–Teller well [D,V]

Let

```math
V_1=-2r^2S^2,\qquad F_1(\lambda,u)=\lambda+r^2W^2.
```

**Theorem 12.1 [D,V].** For every spectral parameter $\lambda$,

```math
(F_1)_{uuu}-4(V_1-\lambda)(F_1)_u-2(V_1)_uF_1=0.
```

Its conserved spectral polynomial is exactly

```math
\mathscr R_1(\lambda)=-2F_1(F_1)_{uu}+(F_1)_u^2+4(V_1-\lambda)F_1^2=-4\lambda(\lambda+r^2)^2.
```

**Proof.** Set $D_W=r(1-W^2)\partial_W$ and substitute $V_1=-2r^2(1-W^2)$, $F_1=\lambda+r^2W^2$ into the two polynomial expressions. Their differences from zero and the claimed $\mathscr R_1$ respectively factor identically to zero. The second identity can also be checked at $u\to+\infty$, where $V_1\to0$, $F_1\to\lambda+r^2$ and all derivatives of $F_1$ vanish.

The singular spectral curve is

```math
\nu^2=-4\lambda(\lambda+r^2)^2.
```

Its simple root at $\lambda=0$ is the continuum threshold of $L_1=-\partial_u^2+V_1$, and the double factor at $\lambda=-r^2$ records its one bound level. The double root is a **singular spectral-curve degeneration**, not a Jordan defect of the self-adjoint Schrödinger operator.

### 12.1 A family of positive Pinney amplitudes generated by the spectral polynomial

For $\lambda>0$, $F_1>0$ for all real $u$, and the squared-eigenfunction identity gives

```math
a_{1,\lambda}=\sqrt{\lambda+r^2W^2},\qquad (a_{1,\lambda})_{uu}=(V_1-\lambda)a_{1,\lambda}+\lambda(\lambda+r^2)^2a_{1,\lambda}^{-3}.
```

This is an **exact spectral-parameter-dependent Ermakov–Pinney family** tied to the order-one Pöschl–Teller potential. The new strength is $k_1(\lambda)=\lambda(\lambda+r^2)^2$. The positivity restriction $\lambda>0$ matters: at a spectral branch point the chosen square root may vanish, so the real positive-amplitude reconstruction cannot be continued across it without additional data.

## 13. Exact order-two closure: the original Master Hessian well [D,V]

Let

```math
V_2=-6r^2S^2.
```

The polynomial of degree two in the spectral parameter is

```math
F_2(\lambda,u)=\lambda^2+r^2(3W^2+2)\lambda+r^4(3W^2-1)^2.
```

**Theorem 13.1 [D,V].** For every $\lambda$, its symmetric-square equation closes identically:

```math
(F_2)_{uuu}-4(V_2-\lambda)(F_2)_u-2(V_2)_uF_2=0.
```

Its exact conserved polynomial is

```math
\mathscr R_2(\lambda)=-4\lambda(\lambda+r^2)^2(\lambda+4r^2)^2.
```

**Proof.** Apply $D_W=r(1-W^2)\partial_W$ three times to the displayed polynomial; substitution into the symmetric-square equation gives zero as a polynomial in $(W,\lambda,r)$. Applying the same derivation to $\mathscr R_2=-2F_2F_{2,uu}+F_{2,u}^2+4(V_2-\lambda)F_2^2$ yields the factored polynomial, independently of $W$. This check was performed with exact symbolic arithmetic.

Thus the singular spectral curve is

```math
\nu^2=-4\lambda(\lambda+r^2)^2(\lambda+4r^2)^2.
```

The two double roots at $\lambda=-r^2$ and $\lambda=-4r^2$ encode the two bound levels of $L_2=-\partial_u^2-6r^2S^2$, while $\lambda=0$ is the continuum threshold.

### 13.1 The original Master Hessian has an additional constant shift

The normalized nonlinear Master separatrix $y=\mu^{-1/2}S$ has the linearized **self-adjoint** Hessian

```math
H_{\rm Master}=-\partial_u^2+r^2-6r^2S^2=L_2+r^2.
```

If $E$ denotes its *physical spectral eigenvalue* and $\lambda=E-r^2$ the unshifted parameter above, the two double roots become

```math
\lambda=-4r^2\ \Longleftrightarrow\ E=-3r^2,\qquad\lambda=-r^2\ \Longleftrightarrow\ E=0.
```

The simple root $\lambda=0$ corresponds to $E=r^2$, the essential-spectrum threshold. **This is an exact algebraic encoding of the entire discrete Master Hessian spectrum and its threshold inside the conserved symmetric-square polynomial.** It is substantially stronger than recognizing a Pöschl–Teller potential by inspection.

### 13.2 The associated Pinney family also closes

For $\lambda>0$, $F_2$ is strictly positive because it is a sum of positive terms plus $r^4(3W^2-1)^2\ge0$. Hence

```math
a_{2,\lambda}=\sqrt{F_2(\lambda,u)},\quad (a_{2,\lambda})_{uu}=(V_2-\lambda)a_{2,\lambda}+\lambda(\lambda+r^2)^2(\lambda+4r^2)^2a_{2,\lambda}^{-3}.
```

So $k_2(\lambda)=\lambda(\lambda+r^2)^2(\lambda+4r^2)^2$ is a **spectral Pinney Casimir polynomial**. It is not the same parameter as the original positive canonical envelope strength $\mu r^2/4$: the two constructions involve different linear carriers and different Gram choices.

## 14. The spectral polynomial is a finite-dimensional closure certificate [D,V,K]

In both cases one has a polynomial $F_n$ in the spectral parameter and an invariant $\mathscr R_n(\lambda)$ independent of the spatial coordinate. The mapping

```math
(L_n,\lambda,F_n)\longmapsto\left(\nu^2=\mathscr R_n(\lambda),\quad a_{n,\lambda}=\sqrt{F_n},\quad k_n=-\mathscr R_n/4\right)
```

is a precise, checkable **spectral-to-Pinney dictionary** for $\lambda>0$.

The two curves are singular (double roots), and the integer Pöschl–Teller wells are reflectionless/solitonic limits of finite-gap families. The spectral-curve normalization of a generic smooth periodic Lamé operator requires **marked Abelian periods**, a real slice and appropriate boundary/Floquet data; simply using $\mathrm{sech}^2$ does not construct those smooth periodic curves.

### 14.1 Why this also answers the Jordan question

A repeated root of $\mathscr R_n(\lambda)$ describes a degeneration of an *auxiliary hyperelliptic spectral curve*. It is not equivalent to a defective transfer matrix and does not imply non-self-adjointness. In this canonical example the operators $L_n$ and $H_{\rm Master}$ are self-adjoint on the standard full-line $H^2$ domain and have real discrete levels precisely at the repeated spectral factors.

The same word “degeneration” thus has at least three separate typed meanings: an algebraic curve's repeated branch root; a transfer matrix's Jordan form; and a Hilbert-space operator's non-self-adjoint exceptional point. They require different diagnostics.

## 15. Three curves in the framework must not share an untyped “period” [H,D,C]

The prior investigations attach **different** algebraic curves to one elementary hyperbolic profile:

1. The nonlinear Master energy curve $p^2=e+z^2-z^4$ has raw binary-quartic invariants $I=1-12e$, $J=-2-72e$ and discriminant $-16e(1+4e)^2$. Its zero-energy separatrix is **singular**, and at generic $e$ it is a smooth elliptic curve.
2. The Pinney **energy** quartic $Y^2=Q_0a^4+2\mathcal E_a a^2-k_{\rm EP}$ is generically a **smooth** genus-one curve; at the centered canonical parameters it has $j=1728$, but its *distinguished time differential* descends through $a^2$ to a genus-zero conic (draft 120).
3. The **spectral** squared-eigenfunction curves of §§12–13 are $ \nu^2=\mathscr R_1(\lambda)$ and $\nu^2=\mathscr R_2(\lambda)$, singular solitonic degenerations recording two different Pöschl–Teller Schrödinger operators.

The formal genus, singular locus, period lattice and marked differential are not interchangeable. A quartic $j$ invariant cannot decide whether two different differential operators are isospectral, nor whether a minimal surface's real immersion periods close.

### 15.1 The archive contains genuine higher-genus extensions

The historical ZIP's mellin-beta-heun-lame and binary-quartic-and-spectral-curves investigations distinguish nonlinear orbit curves from Lamé spectral curves. The integer Pöschl–Teller potentials in §§12–13 are the **degenerate endpoints** of certain elliptic/finite-gap constructions; for smooth generic Lamé cases one needs a genuine genus-$g$ spectral curve and marked cycles. The level-five archive includes degree-three Lamé and genus-three generic spectral data, while level-nine nonlinear curves require genus-two invariants. The fact that the central SL–EP Lie algebra has dimension three does **not** constrain all these auxiliary spectral curves to genus one.

## 16. The catenoid and helicoid: an exact local geometric avatar [D,V,H421]

Extend $u=\ln(x/c)$ to an independent complex surface coordinate $\zeta=u+iv$, with $v$ angular of period $2\pi/r$ for the catenoid. The immersion

```math
X(u,v)=\left(\frac{\cosh(ru)}r\cos(rv),\,\frac{\cosh(ru)}r\sin(rv),\,u\right)
```

has induced metric, Gaussian curvature and Hopf differential (in a fixed normal orientation)

```math
I=R^2|d\zeta|^2,\qquad K_G=-r^2S^4,\qquad Q_H=-\frac r2\,d\zeta^2.
```

The meromorphic stereographic Gauss map and the induced round-sphere metric are

```math
G(\zeta)=-e^{r\zeta},\qquad III=G^*g_{S^2}=r^2S^2|d\zeta|^2=-K_GI.
```

These satisfy the Gauss–Codazzi equation with $H=0$. The corresponding catenoid Jacobi equation, after angular Fourier separation, contains the order-one Pöschl–Teller well $V_1$ of §12. This supplies the **exact** local bridge between a minimal immersion and the first factored spectral polynomial.

### 16.1 The Milne phase determines the Gauss conformal factor

For the selected positive Pinney envelope of §6, let $\vartheta=\arg\Phi$, so $\vartheta_u=(r/2)S$ and $a^4=\mu R^2$. Then

```math
III=4\vartheta_u^2|d\zeta|^2=\frac{\mu r^2}{a^4}|d\zeta|^2.
```

The catenoid metric is simultaneously $I=a^4|d\zeta|^2/\mu$. Therefore the pair of reciprocal conformal factors is generated by the same Pinney modulus/phase, *after choosing this particular immersion*. That is a real differential-geometric dictionary, not a proof that all Pinney solutions produce the same catenoid or that the sphere and catenoid are isometric.

### 16.2 The Levi-Civita/Weitzenböck entry remains separately typed

In the selected oriented tangent teleparallel frame of draft 030, the torsion coefficient is $t_2=rSW$ and the curvature reconstructs as

```math
K_G=-e_1(t_2)-t_2^2=-r^2S^4,\qquad e_1=S\,\partial_u.
```

This is an identity between the Levi-Civita curvature of a *specified surface metric* and derivatives of a torsion coefficient of a *specified flat frame connection*. It is **not** the same Casimir as $H_0K-D^2=k_{\rm EP}/4$ nor the same $\mathscr R_n(\lambda)$ as the spectral curve.

The catenoid and helicoid are local Bonnet-associated minimal immersions sharing their conformal metric and local Jacobi differential expression after matching coordinates. Their **global** angular topology/periods can be different, so a local PT operator does not identify their complete self-adjoint spectral realizations.

## 17. Riemann minimal examples: the archival marked-period closure [H,K]

The November 18 historical ZIP has a much stronger result than a generic “Riemann surfaces are elliptic” analogy. Its marked-period investigation H466–H470 starts from an explicit family

```math
w_R^2=g(g-\lambda_R)(\lambda_Rg+1),\qquad \lambda_R>0.
```

Introduce $y_R=w_R/\sqrt{\lambda_R}$ and the distinct base parameter $k_R=\lambda_R^{-1}-\lambda_R$. Then

```math
y_R^2=g^3+k_Rg^2-g.
```

For a chosen homology cycle define the **marked period vector**

```math
\Omega(k_R)=\oint\frac{dg}{y_R},\qquad N(k_R)=\oint\frac{g\,dg}{y_R}.
```

The archive derives the Gauss–Manin first-order system

```math
\frac d{dk_R}\binom{\Omega}{N}=\frac1{k_R^2+4}\begin{pmatrix}-k_R/2&-1\\-1&k_R/2\end{pmatrix}\binom{\Omega}{N}.
```

**Key dictionary:** This is also a traceless $2\times2$ first-order matrix equation, but its independent variable is **the family modulus $k_R$**, not the original spatial logarithm $u=\ln(x/c)$. It acts on *periods of elliptic differentials*, not on the canonical pair $(\phi,\phi_u)$ of the half-rate oscillator. Equality of matrix size and structure group does not identify their two connections or their monodromies.

### 17.1 Picard–Fuchs and projective geometry

Eliminating $N$ gives the archived scalar Picard–Fuchs equation

```math
(k_R^2+4)\Omega_{k_Rk_R}+2k_R\Omega_{k_R}+\frac14\Omega=0.
```

Its projective period ratio obeys a Schwarzian equation, so the same **formal second-order/projective mechanism** reappears in Gauss–Manin theory. This is a legitimate bridge to the SL/Riccati dictionary, now with a *marked parameter change* and a *different meaning* for the solutions.

The archive additionally identifies a modular $X_0(4)$ coordinate for this elliptic family, with explicit $j$ and eta/Hauptmodul formulas, and supplies numerical monodromy verification. Those results belong to the **chosen Riemann family**; they are not a consequence of the one-dimensional weighted $L^2$ norm of the original Symmetrical Function.

### 17.2 What actual immersion-period closing requires

A Weierstrass–Enneper immersion $X=\mathrm{Re}\int\boldsymbol\Phi$ is constructed from three meromorphic one-forms on the punctured elliptic curve satisfying their nullity relation. To descend to a surface in $\mathbb R^3$, the **real parts of periods** on all relevant cycles must vanish; for a singly periodic surface they must belong to a **specified translation lattice** instead. The imaginary parts record flux.

The archived Riemann family computes translation and flux vectors $T_R,F_R$ from the two basic elliptic periods and verifies a nontrivial determinant identity involving their scale $A_R>0$:

```math
(T_R)_1(F_R)_3-(T_R)_3(F_R)_1=\frac{8\pi A_R^2}{\lambda_R}.
```

This is a legitimate **global symplectic period constraint**. It does not follow just from the half-rate Pinney Casimir or from a local Riccati coordinate. Embeddedness, completeness and limit surfaces need further global analysis. This is precisely why the period-closing layer is separate from the finite Lie–Hamilton layer.

## 18. Berry phase and Chern quantization require the global Hopf lift [D,K,H170]

Specify a two-component unit spinor on a local Hopf chart, with $\varphi=rv$ and $W=\tanh(ru)$:

```math
\eta(u,\varphi)=\left(\sqrt{\frac{1-W}{2}},\,e^{i\varphi}\sqrt{\frac{1+W}{2}}\right),\qquad \|\eta\|_{\mathbb C^2}=1.
```

Its projective ratio is

```math
\frac{\eta_2}{\eta_1}=e^{ru+i\varphi}=e^{r(u+iv)}=-G(\zeta).
```

Thus the **same** exponential projective coordinate extends the real SL ratio to the complex Gauss-map coordinate of the catenoid, after explicitly adding the independent angular variable $v$. The Hopf fiber consists of multiplying both components by a common phase.

### 18.1 Exact local connection and globally quantized curvature

In the stated spinor gauge, the local $U(1)$ connection and its curvature are

```math
\mathcal A=-i\eta^\dagger d\eta=\frac{1+W}{2}\,d\varphi,\qquad\mathcal F=d\mathcal A=\frac12dW\wedge d\varphi.
```

After completing the base by the two poles $W=\pm1$ and patching the local gauge, one obtains

```math
\frac1{2\pi}\int_{S^2}\mathcal F=1.
```

**This integer is the first Chern class** of the selected Hopf line bundle. It requires a global compact base and compatible gauge patches; the real one-dimensional $u$ line alone has no nontrivial two-cycle for such a Chern-number integral.

### 18.2 Individual Berry holonomies are not generally integer-quantized

For a latitude loop with fixed $W$, $0\le\varphi\le2\pi$, the holonomy angle in the selected patch is

```math
\gamma(W)=\oint\mathcal A=\pi(1+W)\pmod{2\pi}.
```

It varies continuously with $W$. At the original center $x=c$ one has $u=W=0$ and $\gamma=\pi$; away from the equator it generally is neither zero nor $\pi$. **What is quantized is the integral curvature over the closed two-sphere**, not the Berry phase around every possible loop.

The scalar Milne/Gudermannian phase $\vartheta(u)$ has an exact proportionality to the original arctangent primitive, but is not *automatically* this Berry holonomy. The two phases require a separate connection-preserving map before being called equal.

## 19. Hodge L2 metrics on elliptic curves: a second, different notion of metric glue [K,D]

On a compact oriented elliptic curve $E=\mathbb C/(\mathbb Z\omega_1+\mathbb Z\omega_2)$ with $\mathrm{Im}(\omega_2/\omega_1)>0$, choose a holomorphic one-form $dz$. Its Hodge $L^2$ pairing is

```math
\|dz\|_{\rm Hodge}^2=\frac i2\int_E dz\wedge d\bar z=\mathrm{Im}(\bar\omega_1\omega_2).
```

For the normalized form $\alpha=dz/\omega_1$ with periods $(1,\tau)$, $\tau=\omega_2/\omega_1$,

```math
\|\alpha\|_{\rm Hodge}^2=\mathrm{Im}\,\tau.
```

This is an exact relation between **holomorphic period data** and an $L^2$ metric on differential forms, via the Riemann bilinear relations. It resembles the weighted $L^2$ pairing of the canonical SL carrier in the broad sense that both are positive Hilbert metrics, but they live on **different spaces with different measures**: one-dimensional weighted functions on $(0,\infty)$ versus harmonic one-forms on a compact complex curve.

**Important boundary:** The scalar norm $\|f_\mu\|_{L^2(xdx)}$ alone does not determine $\omega_1,\omega_2$, their ratio $\tau$, the Gauss–Manin connection or a surface's immersion-period closing. An actual intertwiner/pullback of the relevant differential and measure, plus a marked cycle and normalization, would be required. This is a concrete answer to the proposed “exact metric glue” interpretation.

## 20. The weighted Sturm–Liouville Hilbert space IS exactly logarithmic L2 [D,V,H169]

Return to the original **weighted** differential expression on $x>0$:

```math
\tau_x f=\frac1x\left[-(x^3f_x)_x+(r^2-1)xf\right],\qquad p=x^3,\quad w=x,\quad q_0=(r^2-1)x.
```

Its Hilbert space is $\mathcal H_x=L^2((0,\infty),x\,dx)$. Define the transform with the original center explicit:

```math
(U_cf)(u)=x f(x),\qquad x=ce^u.
```

**Theorem 20.1 [D,V] (exact unitary Hilbert dictionary).**

```math
\int_0^\infty|f(x)|^2x\,dx=\int_{-\infty}^{\infty}|(U_cf)(u)|^2\,du,\qquad U_c\tau_xU_c^{-1}=-\partial_u^2+r^2.
```

**Proof.** Because $dx=xdu$, the left norm is $\int|xf|^2du$. For $\psi=xf$ one has $f_x=(\psi_u-\psi)/x^2$ and $(x^3f_x)_x=\psi_{uu}-\psi$; substitution gives the Schrödinger expression. This is a unitary equivalence **only if domains are transported**. The original point $x=c$ corresponds to the interior coordinate $u=0$.

The full-line self-adjoint carrier $-\partial_u^2+r^2$ has spectrum $[r^2,\infty)$, purely absolutely continuous, and the weight transformation alone does not create a bound state. The nonlinear localized profile is not a zero-energy eigenfunction of this free positive carrier.

### 20.1 Weighted Sobolev/Dirichlet form dictionary

For smooth functions with sufficient endpoint decay, the original quadratic form becomes

```math
\mathfrak q_x[f]=\int_0^\infty[x^3|f_x|^2+(r^2-1)x|f|^2]\,dx=\int_{\mathbb R}[|\psi_u|^2+r^2|\psi|^2]\,du.
```

Indeed, $x^3|f_x|^2dx=|\psi_u-\psi|^2du$; the cross term integrates to the vanishing endpoint value $-[|\psi|^2]_{-\infty}^{+\infty}$. The *form domain* is the pullback of $H^1(\mathbb R)$ for the full-line realization. One obtains a legitimate **weighted Sobolev space** in $x$ isometric to the standard $H^1$ form in the logarithmic coordinate.

**Caution:** The quadratic form may involve a negative coefficient $(r^2-1)x$ for $0<r<1$, yet its complete transformed form is nonnegative and bounded below by $r^2\|\psi\|^2$ after the cross term is treated correctly. An isolated negative coefficient in one coordinate is not a negative self-adjoint eigenvalue.

## 21. Exact H1 and H2 norms of the canonical profile [D,V]

For the actual normalized Symmetrical Function put

```math
\psi_\mu(u)=(U_cf_\mu)(u)=\frac1{2\sqrt\mu}\mathrm{sech}(ru).
```

Its fundamental Hilbert norm and derivative Sobolev seminorm are

```math
\|\psi_\mu\|_2^2=\frac1{2r\mu},\qquad\|\partial_u\psi_\mu\|_2^2=\frac r{6\mu}.
```

A second differentiation gives the exact higher seminorm

```math
\|\partial_u^2\psi_\mu\|_2^2=\frac{7r^3}{30\mu}.
```

**Proof.** Use $\psi_u=-rSW/(2\sqrt\mu)$ and $\psi_{uu}=r^2(S-2S^3)/(2\sqrt\mu)$ with

```math
\int_{\mathbb R}S^2du=\frac2r,\qquad\int_{\mathbb R}S^4du=\frac4{3r},\qquad\int_{\mathbb R}S^6du=\frac{16}{15r}.
```

The cross terms simplify by $W^2=1-S^2$. Consequently the canonical weighted quadratic form is

```math
\mathfrak q_x[f_\mu]=\frac{2r}{3\mu},\qquad\frac{\mathfrak q_x[f_\mu]}{\|f_\mu\|^2_{L^2(xdx)}}=\frac{4r^2}{3}.
```

This Rayleigh quotient is an expectation value of the free linear carrier in the **nonlinear** localized test profile, not an eigenvalue of that free carrier. It exceeds the spectral threshold $r^2$, as it must.

## 22. Mellin is literally the Fourier transform in the canonical logarithmic coordinate [D,K,H391]

Define the ordinary Mellin transform of the original profile (with an amplitude factor $\mu^{-1/2}$) by

```math
\mathcal M[f_\mu](s)=\int_0^\infty x^{s-1}f_\mu(x;r,c)\,dx.
```

The exact evaluation on its open convergence strip is

```math
\mathcal M[f_\mu](s)=\frac{\pi c^{s-1}}{2r\sqrt\mu}\sec\left(\frac{\pi(s-1)}{2r}\right),\qquad1-r<\mathrm{Re}\,s<1+r.
```

**Proof.** Substitute $x=ce^u$ so that $f_\mu dx=(2\sqrt\mu)^{-1}Sdu$ and $x^{s-1}=c^{s-1}e^{(s-1)u}$, then use the Euler integral of $\mathrm{sech}(ru)$. The strip follows from the two exponential tails. In particular the Mellin reflection identity is

```math
\mathcal M[f_\mu](s)=c^{2s-2}\mathcal M[f_\mu](2-s).
```

This expresses the original center-preserving inversion $x\mapsto c^2/x$ in Mellin form; the dependence on $c$ is essential.

### 22.1 The unitary multiplicative Plancherel transform

For $f\in L^2((0,\infty),x\,dx)$ define the Mellin-frequency transform

```math
(\mathscr M_cf)(k)=\frac1{\sqrt{2\pi}}\int_0^\infty x f(x)(x/c)^{-ik}\frac{dx}{x}.
```

Equivalently, $\mathscr M_cf$ is the standard Fourier transform of $\psi=U_cf$:

```math
(\mathscr M_cf)(k)=\frac1{\sqrt{2\pi}}\int_{\mathbb R}\psi(u)e^{-iku}\,du=\widehat\psi(k).
```

Hence exact Plancherel gives

```math
\int_0^\infty x|f(x)|^2dx=\int_{\mathbb R}|\widehat\psi(k)|^2dk.
```

This is not just a formal Mellin–Fourier analogy: it is an **explicit unitary equivalence** of Hilbert spaces with all factors accounted for.

For the original canonical profile one obtains the elementary spectral amplitude

```math
\widehat\psi_\mu(k)=\frac{\pi}{2r\sqrt{2\pi\mu}}\mathrm{sech}\left(\frac{\pi k}{2r}\right).
```

The center $c$ cancels from this **centered** Fourier–Mellin amplitude because the character $(x/c)^{-ik}$ uses the original logarithmic origin. If ordinary Mellin characters $x^{-ik}$ are used instead, the corresponding factor $c^{-ik}$ or $c^{ik}$ must be tracked according to transform orientation.

## 23. Fourier–Sobolev and the exact uncertainty invariant [D,V]

Parseval for derivatives gives the spectral Sobolev norm

```math
\int_{\mathbb R}|\partial_u^m\psi|^2du=\int_{\mathbb R}k^{2m}|\widehat\psi(k)|^2dk,\qquad m=0,1,2,\ldots,
```

for appropriate Sobolev-domain functions. On the original weighted space, the self-adjoint *dilation generator* is

```math
D_x=U_c^{-1}(-i\partial_u)U_c=-i(x\partial_x+1).
```

The generator of dilations, not the ordinary momentum $-i\partial_x$, is diagonalized by the Mellin characters under this weighted Hilbert realization. Its domain must be specified as the transported $H^1$ domain.

Normalize the canonical position density and spectral density:

```math
\rho_u(u)=\frac{|\psi_\mu(u)|^2}{\|\psi_\mu\|_2^2}=\frac r2\mathrm{sech}^2(ru).
```

```math
\rho_k(k)=\frac{|\widehat\psi_\mu(k)|^2}{\|\widehat\psi_\mu\|_2^2}=\frac{\pi}{4r}\mathrm{sech}^2\left(\frac{\pi k}{2r}\right).
```

Both are centered logistic distributions. Direct integration or expansion of their characteristic functions gives

```math
\sigma_u^2=\frac{\pi^2}{12r^2},\qquad\sigma_k^2=\frac{r^2}{3},\qquad\sigma_u\sigma_k=\frac\pi6.
```

The product is resolution-independent but **not** an equality case of the ordinary Heisenberg lower bound ($\sigma_u\sigma_k\ge1/2$). It is a special, exactly computable uncertainty invariant of this profile. The scale $c$ shifts the original $x$ chart, while $\mu$ cancels after normalization; neither changes the displayed product.

## 24. Ordinary Fourier versus multiplicative Plancherel: different norms and thresholds [D,V]

Extend $f_\mu(x)$ by zero to the negative real line and define its **ordinary** Fourier transform in the *original additive coordinate* $x$:

```math
\widehat f_{\rm add}(\xi)=\frac1{\sqrt{2\pi}}\int_0^\infty f_\mu(x;r,c)e^{-i\xi x}\,dx.
```

The ordinary additive Plancherel identity requires $f_\mu\in L^2(dx)$. The behavior $f_\mu(x)\sim x^{r-1}/(\sqrt\mu\,c^r)$ near zero shows this is equivalent to $r>1/2$. Under this condition,

```math
\int_{\mathbb R}|\widehat f_{\rm add}(\xi)|^2d\xi=\int_0^\infty|f_\mu(x)|^2dx=\frac{\pi}{4\mu r^2c\sin(\pi/(2r))}.
```

This is **not the same** as the canonical weighted norm $\|f_\mu\|_{L^2(xdx)}^2=1/(2r\mu)$; the additive Fourier basis diagonalizes translations in $x$, while the Mellin basis diagonalizes multiplicative dilations in $x$.

### 24.1 The complete shifted-weight Mellin–Plancherel family

For real $b$ with $|b|<2r$, define

```math
\mathcal N_b=\int_0^\infty x^{1-b}|f_\mu(x)|^2dx.
```

The exact general norm is

```math
\mathcal N_b=\frac{\pi b}{4\mu r^2c^b\sin(\pi b/(2r))},\qquad \mathcal N_0=\frac1{2r\mu}\ \mathrm{(continuous\ limit)}.
```

Its shifted Mellin Plancherel formula is

```math
\mathcal N_b=\frac1{2\pi}\int_{-\infty}^{\infty}\left|\mathcal M[f_\mu]\left(1-\frac b2+ik\right)\right|^2dk.
```

**Proof.** Let $g_b(u)=x^{1-b/2}f_\mu(x)$, so $\|g_b\|_{L^2(du)}^2=\mathcal N_b$. Its Fourier transform is a phase times the Mellin transform on the vertical line $\mathrm{Re}\,s=1-b/2$. Parseval proves the identity. The closed form follows from the Gamma reflection identity. Its convergence strip yields exactly $|b|<2r$.

For $b=0$ this is canonical **weighted SL** Plancherel. For $b=1$ it is **ordinary additive $L^2(dx)$ norm** expressed using Mellin frequencies (available only when $r>1/2$). For $b=2$ it is $\|f_\mu\|^2_{L^2(dx/x)}$, available only when $r>1$.

### 24.2 Product of ordinary and multiplicative L2 norms

For $r>1$, both $\mathcal N_1=\|f_\mu\|_{L^2(dx)}^2$ and $\mathcal N_2=\|f_\mu\|_{L^2(dx/x)}^2$ exist. The historical Plancherel archive studies their joint scalar products. With explicit amplitude and scale, they are

```math
\mathcal N_1=\frac{\pi}{4\mu r^2c\sin(\pi/(2r))},\qquad\mathcal N_2=\frac{\pi}{2\mu r^2c^2\sin(\pi/r)}.
```

```math
\mathcal N_1\mathcal N_2=\frac{\pi^2}{8\mu^2r^4c^3\sin(\pi/(2r))\sin(\pi/r)}.
```

The last expression is a **product of two distinct scalar norms**, not the automatic norm of a new “simultaneous one-variable Fourier and Mellin transform”. Such a joint transform needs either two independent coordinates or another explicitly constructed operator-theoretic framework.

## 25. An ACTUAL product transform: additive Fourier times multiplicative Mellin [D,V]

To combine two Fourier theories **simultaneously**, use two independent coordinates. Let $v\in\mathbb R$ be an additive coordinate and $x\in(0,\infty)$ a multiplicative coordinate, and put

```math
\mathcal H_{v,x}=L^2(\mathbb R_v\times(0,\infty)_x,\;dv\,x\,dx).
```

For a sufficiently regular field $F(v,x)$ define the mixed Fourier–Mellin transform

```math
(\mathscr T_cF)(\xi,k)=\frac1{2\pi}\int_{\mathbb R}e^{-i\xi v}\,dv\int_0^\infty F(v,x)(x/c)^{-ik}\,dx.
```

The apparently unweighted $dx$ in the transform is *intentional*: it comes from applying the canonical multiplier $xF$ and the multiplicative Haar measure $dx/x$.

**Theorem 25.1 [D,V] (tensor-product Plancherel).**

```math
\int_{\mathbb R}\int_0^\infty|F(v,x)|^2x\,dx\,dv=\int_{\mathbb R}\int_{\mathbb R}|\mathscr T_cF(\xi,k)|^2\,dk\,d\xi.
```

**Proof.** Set $u=\ln(x/c)$ and $\Psi(v,u)=xF(v,ce^u)$. Then the left side becomes $\int|\Psi|^2du\,dv$. The displayed mixed transform becomes precisely the product of ordinary **unitary Fourier transforms** in the two *independent* additive variables $(v,u)$. Apply the two-variable Plancherel theorem.

For separable $F(v,x)=g(v)f_\mu(x;r,c)$, the transform factorizes:

```math
\mathscr T_cF(\xi,k)=\widehat g(\xi)\widehat\psi_\mu(k),\qquad \|F\|_{\mathcal H_{v,x}}^2=\|g\|_{L^2(dv)}^2\frac1{2r\mu}.
```

**This is the precise meaning of an operator product “standard Fourier times multiplicative Fourier”.** It is a tensor-product unitary transform. It does not claim that ordinary translations in $x$ and multiplicative dilations in $x$ have a joint eigenbasis on the *same one-dimensional* Hilbert space: those generators do not commute in general.

## 26. A new exact isometric bridge from the weighted SL space into catenoid L2 [D,V]

This provides an unusually concrete answer to the proposed weighted-norm “metric glue”, using the *actual surface metric* rather than merely a similar profile.

The complete catenoid has coordinates $u\in\mathbb R$, $v\in[0,2\pi/r)$ and area measure

```math
dA_C=R(u)^2\,du\,dv,\qquad R(u)=\cosh(ru).
```

Let $h_0(v)=\sqrt{r/(2\pi)}$ be the **normalized angular constant mode**, so $\int_0^{2\pi/r}|h_0|^2dv=1$. Define a linear map on scalar functions

```math
(\mathscr I_{c,r}f)(u,v)=h_0(v)\frac{x f(x)}{R(u)},\qquad x=ce^u.
```

**Theorem 26.1 [D,V] (exact Hilbert-space isometry).**

```math
\|\mathscr I_{c,r}f\|_{L^2(C,dA_C)}^2=\int_0^\infty|f(x)|^2x\,dx.
```

**Proof.** Integrate the square:

```math
\int_{\mathbb R}\int_0^{2\pi/r}\left|h_0(v)\frac{xf(x)}{R(u)}\right|^2R(u)^2\,dv\,du=\int_{\mathbb R}|xf(ce^u)|^2du.
```

The angular normalization removes the circle length, the conformal half-density $R^{-1}$ cancels the catenoid area multiplier, and the logarithmic Liouville transform converts the last integral to $\int x|f|^2dx$.

**Meaning:** The original weighted Hilbert space has an exact **isometric embedding into the angularly constant scalar $L^2$ sector of the complete catenoid**, with $c,r$ explicitly preserved. This is a *new constructed Hilbert map* in the foundational dictionary, not a claim that the two natural differential operators are unitarily intertwined.

### 26.1 Why this does not automatically identify the spectra

The catenoid Laplacian is $\Delta_{g_C}=R^{-2}(\partial_u^2+\partial_v^2)$ and its Jacobi operator additionally contains $2r^2S^4$. The isometry $\mathscr I_{c,r}$ contains multiplication by $R^{-1}$, whose derivatives generate extra terms when differential operators are conjugated. Therefore

```math
\mathscr I_{c,r}\,\tau_x\,\mathscr I_{c,r}^{-1}\ne-\Delta_{g_C}-|A_C|^2
```

as bare equalities of differential operators; one must calculate any proposed intertwiner and transport the domains and angular modes. The fact that the corresponding scalar Hilbert spaces are isometric is strictly weaker than isospectrality.

For the **complete helicoid** the angular coordinate is unwrapped, so an angular constant is not in $L^2$ on the noncompact angular line. The displayed normalized-constant-mode embedding is tied to the catenoid's *global angular quotient*. This gives an exact place where topological/geometric information survives even though the local catenoid and helicoid metrics agree.

## 27. Angular Fourier series times radial Mellin: the natural catenoid product calculus [D,V]

For an arbitrary scalar field $\Phi(u,v)$ on the catenoid, define the unitary “flattened” field $G(u,v)=R(u)\Phi(u,v)$. Then

```math
\|\Phi\|^2_{L^2(C,dA_C)}=\int_{\mathbb R}\int_0^{2\pi/r}|G(u,v)|^2\,dv\,du.
```

Let the normalized angular modes be $h_n(v)=\sqrt{r/(2\pi)}e^{inrv}$ for $n\in\mathbb Z$. Define

```math
\widehat\Phi(n,k)=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-iku}\,du\int_0^{2\pi/r}\overline{h_n(v)}\,R(u)\Phi(u,v)\,dv.
```

Ordinary Fourier–series Plancherel in $v$ followed by Fourier–Mellin Plancherel in $u=\ln(x/c)$ gives the **exact surface norm decomposition**

```math
\|\Phi\|^2_{L^2(C,dA_C)}=\sum_{n\in\mathbb Z}\int_{-\infty}^{\infty}|\widehat\Phi(n,k)|^2\,dk.
```

This is the natural **discrete angular Fourier × continuous multiplicative Mellin** Hilbert dictionary for the catenoid. It incorporates $r$ through the angular lattice $nr$ and through $R=\cosh(ru)$; $c$ remains the log center of $x$.

But angular Fourier diagonalizes $\partial_v$, while **radial Fourier does not diagonalize the varying Pöschl–Teller potential** or the catenoid Jacobi operator automatically. The spectral transform of the latter uses its own scattering/eigenfunctions and matching conditions. The Plancherel identity is Hilbert-space compatibility, not a spectral equivalence theorem.

### 27.1 The two-dimensional metric has a second exact measure

The Gauss-sphere metric is $III=r^2S^2(du^2+dv^2)$, with volume $r^2S^2du\,dv$. The canonical weighted profile density is $|\psi_\mu|^2du=S^2du/(4\mu)$. After angular integration,

```math
\int_0^{2\pi/r}r^2S^2\,dv=2\pi rS^2.
```

Thus the Gauss-sphere marginal density in $u$ is proportional to the **same** normalized logistic law as $|\psi_\mu|^2du$, with different total normalization (sphere area $4\pi$ versus weighted SL norm $1/(2r\mu)$). This is an equality of normalized **pushforward measures** after specifying the Gauss map and angular range; it does not identify the scalar SL operator with the spherical Laplacian.

## 28. The r=2 case as a simultaneous regression test of all closure maps [D,V]

Set $r=2$ but **keep $c,\mu$ explicit**. Then

```math
S_2=\mathrm{sech}(2u)=\frac{2c^2x^2}{x^4+c^4},\qquad W_2=\tanh(2u)=\frac{x^4-c^4}{x^4+c^4},\qquad u=\ln(x/c).
```

The original function and the logarithmic Hilbert profile are

```math
f_\mu(x;2,c)=\frac{c^2x}{\sqrt\mu(x^4+c^4)},\qquad \psi_\mu(u)=\frac{S_2}{2\sqrt\mu}.
```

The original improper integral and its half-splits are

```math
\int_0^c f_\mu dx=\int_c^\infty f_\mu dx=\frac{\pi}{8\sqrt\mu},\qquad\|f_\mu\|_{L^2(xdx)}^2=\frac1{4\mu}.
```

The ordinary- and multiplicative-norm pair (when both defined) is

```math
\mathcal N_1=\frac{\pi}{8\sqrt2\mu c},\qquad\mathcal N_2=\frac{\pi}{8\mu c^2},\qquad\mathcal N_1\mathcal N_2=\frac{\pi^2}{64\sqrt2\mu^2c^3}.
```

The exact Mellin transform, its unitary log-Fourier restriction and Sobolev form are

```math
\mathcal M[f_\mu](s)=\frac{\pi c^{s-1}}{4\sqrt\mu}\sec\left(\frac{\pi(s-1)}4\right),\qquad\widehat\psi_\mu(k)=\frac{\pi}{4\sqrt{2\pi\mu}}\mathrm{sech}(\pi k/4).
```

```math
\|\psi_\mu\|_2^2=\frac1{4\mu},\qquad\|\psi_{\mu,u}\|_2^2=\frac1{3\mu},\qquad\mathfrak q_x[f_\mu]=\frac4{3\mu}.
```

The canonical Pinney/Riccati construction reads

```math
a^2=\sqrt\mu\cosh(2u),\qquad a_{uu}=a+\mu a^{-3},\qquad\frac{\Phi_u}{\Phi}=W_2+iS_2.
```

### 28.1 Both spectral closure polynomials at r=2

For the **catenoid order-one well** $V_1=-8S_2^2$,

```math
F_1(\lambda,u)=\lambda+4W_2^2,\qquad\mathscr R_1=-4\lambda(\lambda+4)^2.
```

For the **Master Hessian order-two well** $V_2=-24S_2^2$,

```math
F_2(\lambda,u)=\lambda^2+4(3W_2^2+2)\lambda+16(3W_2^2-1)^2.
```

```math
\mathscr R_2=-4\lambda(\lambda+4)^2(\lambda+16)^2.
```

The **shifted** Master Hessian is $-\partial_u^2+4-24S_2^2$, with eigenvalues $-12$ and $0$ and continuum starting at $4$. Its bound levels are encoded by the two repeated factors after the shift $E=\lambda+4$.

The Virasoro Schwarzian is $\{e^{2u},u\}=-2$; the Hopf base ratio is $e^{2u+i\varphi}$ with $\varphi=2v$; the catenoid angular period is $v\sim v+\pi$. The normalized Hilbert variance pair is $\sigma_u=\pi/(4\sqrt3)$, $\sigma_k=2/\sqrt3$, and $\sigma_u\sigma_k=\pi/6$.

**Every object is tracked:** the same $r=2$ changes the hyperbolic resolution, rational denominator, spectral wells, oscillator rates, Fourier bandwidth and angular period. The center $c$ remains the multiplicative inversion center and $\mu$ remains an amplitude/Hilbert normalization, not a spectral parameter.
