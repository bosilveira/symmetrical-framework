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
