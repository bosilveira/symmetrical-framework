---
id: SF-DRAFT-110
title: Linearity, Nonlinear Envelopes, Operator Calculus, and Application Boundaries
status: provisional
created: 2026-11-18
proposed_layers: [I, II, III, IV]
depends_on: [SF-I-020, SF-DRAFT-040, SF-DRAFT-050, SF-DRAFT-060, SF-DRAFT-070, SF-DRAFT-080, SF-DRAFT-090, SF-DRAFT-100]
related_claims: [F04, F08, H100, H107, H112, H169, H171, H172, H173, H177, H178, H183, H265, H313, H314, H315, H371, H373, H429, H430, H431, H432]
---

# 110 Linearity, Nonlinear Envelopes, Operator Calculus, and Application Boundaries

**Research status:** Provisional mathematical investigation, not a promoted foundational theorem. [D] explicit derivation; [V] independently checked by algebra/SymPy; [K] classical theorem with hypotheses; [H] historical project claim retaining its original scope; [C] corrected implication or counterexample; [O] open. No physical realization follows from formal correspondences alone.

**Question:** A self-adjoint Sturm–Liouville operator is linear, while Ermakov–Pinney contains an inverse-cubic nonlinearity. Does that exclude operator, spectral and variational methods on the Pinney side? Which Hessian, Hamiltonian, Jacobian, Lagrangian, Laplacian, Wronskian, Routhian, Schwarzian, Riccati, Casimir, Green, Rayleigh, Darboux, Dirac and Liouvillian constructions provide actual bridges? How do PDM ordering, Gross–Pitaevskii, Duffing, Rayleigh–Plesset and Keller–Miksis fit, keeping each model's data separate?

**Principal finding:** Nonlinear Pinney is a well-defined *nonlinear differential operator*, not a standard linear eigenoperator. Nevertheless its Fréchet derivative and action Hessian are linear second-order operators; its squared envelope satisfies a linear third-order symmetric-square equation plus one invariant-level constraint; and its positive amplitude/phase reconstruct a linear carrier. A diagonal Sturm–Liouville Green function also satisfies the same symmetric-square identity, usually at a **negative** Pinney invariant level. These are exact typed correspondences, not a universal equation of physical systems.

**Project sources examined:** GitHub foundational SF-I-020 and full drafts 040, 050, 060, 070, 080, 090, 100; the uploaded November 18 historical ZIP, especially its spectral-calculus, bernoulli-riccati, friedmann-reciprocal-envelope, conformal-and-probabilistic-readings and Hardy/Master/Lamé investigations and CLAIMS ledger. External PDM, GPE and Keller–Miksis sources are independently attributed in §29; the archive is not claimed to have verified those applications.

## 1. Variables and four senses of linearity

Keep canonical parameters and coordinate explicit:

```math
r>0,\qquad c>0,\qquad\mu>0,\qquad x>0,\qquad u=\ln(x/c),\qquad \theta=ru,\qquad S=\mathrm{sech}(ru),\qquad W=\tanh(ru).
```

Primes in §§2–17 denote differentiation in $u$ unless stated. The canonical cubic equation is

```math
y''=r^2y-2\mu r^2y^3,\qquad y_{\rm sep}=\mu^{-1/2}S,\qquad f_\mu(x;r,c)=\frac{S}{2\sqrt\mu\,x}.
```

Application variables: mechanical/evolution time $t$, physical spatial variable $z$, bubble radius $\rho(t)$, liquid density $\rho_L$, acoustic speed $c_L$, viscosity $\eta_L$, surface tension $\sigma$, PDM mass $m(z)$, and GPE chemical potential $\nu$. The acoustic $c_L$ is **not** the original center $c$, and liquid viscosity is **not** the Master parameter $\mu$.

Four logically separate concepts: linearity of a differential *expression*; linearity of its domain/realized *operator*; superposition of its solution set; and linearity of a coordinate/pullback construction. Self-adjointness is a property of an **operator plus domain**, not of “second order” or formal linearity alone.

## 2. Sturm–Liouville is linear, but self-adjointness requires endpoint data [K,D]

For real $p,w>0$ and $q_0$ on an interval $(a,b)$,

```math
-(p(z)\phi_z)_z+q_0(z)\phi=\lambda w(z)\phi,\qquad L_{\rm SL}=w^{-1}[-(p\partial_z)_z+q_0].
```

The natural space is $L^2((a,b),w\,dz)$. Integration by parts gives the exact boundary identity

```math
\langle f,L_{\rm SL}g\rangle_w-\langle L_{\rm SL}f,g\rangle_w=[p(\bar f_zg-\bar f g_z)]_a^b.
```

A self-adjoint realization requires a suitable dense domain annihilating this boundary form. Singular endpoints can be limit-point or limit-circle. Continuous spectrum is possible; not every Sturm–Liouville realization has a discrete eigenbasis.

With appropriate form-domain assumptions its Rayleigh quotient is

```math
\mathcal R[\phi]=\frac{\int_a^b(p|\phi_z|^2+q_0|\phi|^2)\,dz+\mathrm{boundary\ contributions}}{\int_a^b w|\phi|^2\,dz}.
```

When the spectral bottom is an isolated eigenvalue, it can be obtained by minimax. Without compactness the infimum may be a continuous-spectrum threshold.

### 2.1 The exact logarithmic Liouville coordinate of the framework

The linear part of the original Master equation is

```math
x^2f_{xx}+3xf_x+(1-r^2)f=0.
```

Multiplying by $-x$ produces the weighted expression

```math
-(x^3f_x)_x+(r^2-1)xf=0,\qquad p=x^3,\quad w=x,\quad q_0=(r^2-1)x.
```

Its Liouville coordinate and unitary amplitude are

```math
u=\int^x\sqrt{w/p}\,ds=\ln(x/c),\qquad\psi=(pw)^{1/4}f=xf.
```

Consequently the linear *expression* is unitarily converted into

```math
-\psi''+r^2\psi=\lambda\psi.
```

At $\lambda=0$ the carrier has exponential solutions $e^{\pm ru}$. The nonlinear localized Master solution is **not** an eigenfunction of this constant-potential operator: its cubic term has not vanished. The nonlinear solution's Hessian gives a *different* spectral operator (§10).

## 3. Ermakov–Pinney defines a nonlinear operator, and a linearized one [D,V]

Use general carrier convention $Q\in C^1$:

```math
a''=Q(u)a+k a^{-3},\qquad a>0,\qquad \mathcal N_{Q,k}[a]=a''-Qa-ka^{-3}.
```

For $k\ne0$ superposition of positive solutions fails. Nevertheless $\mathcal N$ is a nonlinear differential operator on a positive subset of an appropriate Sobolev space, for example $H^2$ functions bounded away from zero on a finite interval. For any positive $C^2$ solution $a$, its Fréchet derivative is the linear Jacobi expression

```math
D\mathcal N[a](\eta)=\eta''-Q\eta+3ka^{-4}\eta.
```

**Proof.** Differentiate $(a+\varepsilon\eta)^{-3}$ at $\varepsilon=0$; its derivative is $-3a^{-4}\eta$. A nonlinear eigenvalue problem can certainly be posed by including a parameter in $\mathcal N$, but this is not a standard linear spectral problem with a spectral theorem on a vector-space eigenspace.

## 4. Lagrangian, Hessian, Hamiltonian and Jacobian [D,V]

The action with fixed-endpoint variations

```math
\mathcal A[a]=\int\left[\frac12(a')^2+\frac12Q(u)a^2-\frac{k}{2a^2}\right]du
```

has Euler–Lagrange equation $a''-Qa-ka^{-3}=0$. Its second variation is

```math
\delta^2\mathcal A[a](\eta,\eta)=\int[\eta'^2+(Q-3ka^{-4})\eta^2]\,du.
```

The formal self-adjoint Hessian is

```math
\mathcal H_a=-\partial_u^2+Q(u)-3ka^{-4}.
```

Its realization requires boundary conditions; its potential depends on the **chosen nonlinear solution**. The Hamiltonian and canonical momentum are

```math
p_a=a',\qquad H_{\rm EP}(a,p_a,u)=\frac12p_a^2-\frac12Q(u)a^2+\frac{k}{2a^2}.
```

Along solutions $dH_{\rm EP}/du=-Q'(u)a^2/2$, so energy is conserved for constant $Q$. The phase-flow vector field and its Jacobian matrix are

```math
\binom{a}{p_a}'=\binom{p_a}{Qa+ka^{-3}},\qquad D_{(a,p_a)}X_H=\begin{pmatrix}0&1\\Q-3ka^{-4}&0\end{pmatrix}.
```

The **Jacobian** is a matrix derivative; the **Jacobi operator** is the second-order variational differential expression; the **Hessian** is a second variation. They are related but are not the same object.

## 5. A nonlinear equation as a linear third-order equation plus a quadratic invariant [D,V]

Put $J=a^2>0$ and differentiate:

```math
J'=2aa',\qquad J''=2(a')^2+2QJ+2k/J.
```

**Theorem 5.1.** Every Pinney solution satisfies

```math
J'''-4QJ'-2Q'J=0,\qquad \mathcal C[J]=2JJ''-(J')^2-4QJ^2=4k.
```

Conversely, a strictly positive $J$ solving the linear third-order equation with $\mathcal C[J]=4k$ yields $a=\sqrt J$, a solution of Pinney.

**Proof.** Differentiate $J''$, substitute $a''=Qa+ka^{-3}$ and cancel inverse powers; this gives the third-order equation. Separately $2JJ''-(J')^2=4a^3a''=4QJ^2+4k$. Conversely reverse the latter calculation. The invariant's derivative is

```math
\mathcal C'[J]=2J(J'''-4QJ'-2Q'J)=0.
```

**Crucial distinction:** The third-order solution space is *linear*, but imposing a fixed $\mathcal C=4k$ and selecting $J>0$ yields a nonlinear surface inside it. There is no global superposition of Pinney amplitudes.

## 6. Wronskian, Gram determinant and binary-quartic separation [D,K,V]

For two linear carrier solutions $\phi_i''=Q\phi_i$, the Wronskian $\mathscr W=\phi_1\phi_2'-\phi_1'\phi_2$ is constant. The quadratic envelope

```math
J=A\phi_1^2+2C\phi_1\phi_2+B\phi_2^2>0
```

gives a Pinney solution with

```math
k=(AB-C^2)\mathscr W^2.
```

This Gram invariant is **quadratic-form data**, not the $I,J$ of the generic elliptic Master energy quartic. Squaring $G(X,Z)=AX^2+2CXZ+BZ^2$ gives a *singular quartic* with

```math
I(G^2)=16(AB-C^2)^2,\qquad J_{\rm raw}(G^2)=128(AB-C^2)^3,\qquad \Delta(G^2)=0.
```

Its quartic discriminant vanishes **at every Gram determinant**, not just at the localized separatrix. The different quartic interpretations are distinguished in drafts 050, 060 and 100.

## 7. Green functions: the diagonal resolvent is a nonlinear symmetric-square object [D,V,K]

Put a one-dimensional Schrödinger equation in normal form

```math
-\phi''+V(u)\phi=z\phi,\qquad \phi''=Q(u,z)\phi,\qquad Q=V-z.
```

Let $v_1,v_2$ be independent solutions and $G=v_1v_2$. Their Wronskian $\mathscr W=v_1v_2'-v_1'v_2$ is constant.

**Theorem 7.1 [D,V] (Gel'fand–Dikii / diagonal Green identity).** The product satisfies

```math
G'''-4QG'-2Q'G=0
```

and the first integral

```math
-2GG''+(G')^2+4QG^2=\mathscr W^2.
```

**Proof.** $G'=v_1'v_2+v_1v_2'$ and $G''=2QG+2v_1'v_2'$. Hence

```math
2GG''-(G')^2-4QG^2=4v_1v_2v_1'v_2'-(v_1'v_2+v_1v_2')^2=-\mathscr W^2.
```

Differentiation yields the linear third-order equation. This is *exactly the same symmetric-square equation* as the Pinney square in §5.

### 7.1 Why the Green function produces a negative Pinney constant

Where $G>0$, write $a=\sqrt G$. Its invariant is

```math
a''=Qa-\frac{\mathscr W^2}{4a^3}.
```

The Pinney coefficient is $k=-\mathscr W^2/4$ for a product of two **real** independent solutions. This is *negative*, unlike the canonical positive Gram determinant. The distinction is essential.

For a self-adjoint Schrödinger operator and $z$ in its resolvent set, choose endpoint-adapted left/right solutions $v_-,v_+$. If their Wronskian is normalized as above, the Green kernel of $L-z$ has, with this convention,

```math
G_z(u,v)=-\frac{v_-(\min(u,v))v_+(\max(u,v))}{\mathscr W}.
```

Its diagonal $R_z(u)=G_z(u,u)$ satisfies the **normalized** identity

```math
-2R_zR_z''+(R_z')^2+4Q R_z^2=1.
```

This requires existence of the resolvent and regular diagonal values. A diagonal resolvent is **not** the same object as an arbitrary positive Pinney envelope and is not automatically well-defined at a spectral pole, in the continuum or with an arbitrary choice of boundary solutions. For energies below a lower-bounded spectrum, its diagonal can be positive; then $\sqrt{R_z}$ solves Pinney with $k=-1/4$, again not the canonical $k>0$.

**Structural result:** one linear symmetric-square operator supports many invariant levels; Green/resolvent products occupy a negative level, while complex conjugate amplitudes with nonzero flux occupy positive levels. The common operator does not erase the determinant sign.

## 8. Complex logarithm, Riccati, Schwarzian, and the Ermakov phase [D,K,V]

For any locally nonzero solution of $\phi''=Q\phi$, the logarithmic derivative

```math
h=\frac{\phi'}{\phi}=(\mathrm{Log}\,\phi)',\qquad h'+h^2=Q
```

is a Riccati solution. Its poles at zeros of $\phi$ are affine chart singularities of a projective rank-two system; around a complex zero, the integral of $\phi'/\phi$ records winding and requires branch choices.

Given two independent solutions, their projective ratio $F=\phi_1/\phi_2$ has Schwarzian

```math
\{F,u\}=\frac{F'''}{F'}-\frac32\left(\frac{F''}{F'}\right)^2=-2Q.
```

For a **positive** Pinney envelope with $k>0$, choose $\theta'=\sqrt{k}/a^2$ and define

```math
\Phi=a e^{i\theta}.
```

The real/imaginary parts of $\Phi''=Q\Phi$ are precisely $a''=Qa+k a^{-3}$ and $(a^2\theta')'=0$. Hence the nonlinear envelope plus its specified phase reconstructs a zero-free **complex linear** carrier.

Its complex logarithmic derivative decomposes into amplitude and phase:

```math
\frac{\Phi'}{\Phi}=\frac{a'}a+i\frac{\sqrt{k}}{a^2}.
```

This is an exact map, but it is not a global bijection without the phase constant, sign, positivity and monodromy information. A real positive Pinney envelope need not itself lie in the $L^2$ domain of a self-adjoint Sturm–Liouville problem.

## 9. Routhian reduction, Hamiltonian moment maps and the sl(2) Casimir [D,V,K]

Consider a two-dimensional Euclidean oscillator with radial coordinate $a>0$ and angle $\theta$ in a time-dependent quadratic potential:

```math
L_{2D}=\frac12(a'^2+a^2\theta'^2)+\frac12Q(u)a^2.
```

The cyclic angle has momentum $\ell=a^2\theta'$. Holding this value fixed and performing **Routh reduction** (subtract $\ell\theta'$ before eliminating $\theta'$) gives

```math
L_{\rm Routh}=\frac12a'^2+\frac12Q a^2-\frac{\ell^2}{2a^2}.
```

Its radial Euler–Lagrange equation is Pinney with $k=\ell^2\ge0$. This is an exact nonlinearity arising by reduction of a *linear* two-dimensional system: the inverse-cubic force is the centrifugal barrier. For $k<0$, no real Euclidean angular momentum has $\ell^2=k$; a different indefinite-signature or algebraic construction would be necessary.

### 9.1 An explicit quadratic Casimir

On the canonical phase plane $\{a,p\}=1$ and for fixed $k$, set

```math
K=\frac12a^2,\qquad D=\frac12ap,\qquad H_0=\frac12\left(p^2+\frac{k}{a^2}\right).
```

The direct canonical Poisson brackets are

```math
\{D,H_0\}=H_0,\qquad\{D,K\}=-K,\qquad\{K,H_0\}=2D.
```

These are the $\mathfrak{sl}_2$ conformal-mechanics brackets in the displayed convention, with quadratic Casimir

```math
H_0K-D^2=\frac{k}{4}.
```

**Proof.** Expand $H_0K-D^2=(p^2+k/a^2)a^2/4-a^2p^2/4=k/4$. The bracket formulas follow directly from $\{a,p\}=1$.

The full Pinney Hamiltonian is $H_{\rm EP}=H_0-Q(u)K$. This is a time-dependent linear combination of these three generators. The Casimir remains fixed even when $Q$ varies; the energy $H_{\rm EP}$ need not be conserved.

This is a **precise Lie-algebraic classification by a quadratic Casimir**, not an identification with the binary-quartic elliptic $I,J$ or a spacetime curvature/torsion scalar.

## 10. Two different Pöschl–Teller Hessians on the canonical separatrix [D,V]

For the **positive** canonical Pinney envelope use

```math
Q=r^2/4,\qquad k=\mu r^2/4,\qquad a(u)=\mu^{1/4}\sqrt{\cosh(ru)}.
```

Since $k/a^4=(r^2/4)S^2$, the Pinney Hessian of §4 is

```math
\mathcal H_{\rm EP}=-\partial_u^2+\frac{r^2}{4}-\frac{3r^2}{4}S^2.
```

**Theorem 10.1 [D,V] (half-integer Pöschl–Teller factorization).** Let

```math
A_{1/2}=\partial_u+\frac r2 W,\qquad A_{1/2}^\dagger=-\partial_u+\frac r2W.
```

Then

```math
\mathcal H_{\rm EP}=A_{1/2}^\dagger A_{1/2},\qquad A_{1/2}(S^{1/2})=0.
```

**Proof.** Multiply the first-order operators and use $W'=rS^2$, $W^2=1-S^2$. The ground-state factor is annihilated because $(\ln S^{1/2})'=-rW/2$.

On the natural $L^2(\mathbb R,du)$ realization, $\mathcal H_{\rm EP}$ has exactly one bound state at eigenvalue zero, with eigenfunction proportional to $S^{1/2}$; its essential spectrum starts at $r^2/4$. The well has parameter $\nu=1/2$, so it is **not generically reflectionless**. The translation derivative $a'$ is another formal Jacobi-field solution at zero but is not square-integrable; do not confuse it with the normalizable ground mode.

By contrast the original **cubic Master** Hessian at $y=\mu^{-1/2}S$ is

```math
\mathcal H_{\rm Master}=-\partial_u^2+r^2-6r^2S^2=A_2^\dagger A_2-3r^2,\qquad A_2=\partial_u+2rW.
```

This order-two well has $L^2$ eigenvalues $-3r^2$ and $0$, with continuum threshold $r^2$. Its zero mode is the derivative of the Master separatrix.

**Consequence:** The reciprocal map $y=a^{-2}$ relates two nonlinear *solutions*, but **does not identify their unconstrained Hessian spectra**. The first has a nonnegative factored Hessian; the second has a negative direction. A nonlinear reciprocal variable transformation preserving only a constrained family need not be a unitary equivalence of the independent variational problems.

## 11. Darboux, Miura and a Dirac-type square root [D,K]

For the hyperbolic profile define, for real $n>0$,

```math
A_n=\partial_u+nrW,\qquad A_n^\dagger=-\partial_u+nrW.
```

The partner Schrödinger expressions are

```math
A_n^\dagger A_n=-\partial_u^2+n^2r^2-n(n+1)r^2S^2,\qquad A_nA_n^\dagger=-\partial_u^2+n^2r^2-n(n-1)r^2S^2.
```

These are Darboux/SUSY partner expressions, with the Riccati/Miura identity $V_\pm=(nrW)^2\mp(nrW)'$. At positive integer $n$ the corresponding Pöschl–Teller family has the standard integer reflectionless structure; the Pinney value $n=1/2$ does not inherit that property.

A chosen **first-order Dirac-type block operator** is

```math
\mathcal D_n=\begin{pmatrix}0&A_n^\dagger\\A_n&0\end{pmatrix},\qquad \mathcal D_n^2=\begin{pmatrix}A_n^\dagger A_n&0\\0&A_nA_n^\dagger\end{pmatrix}.
```

With compatible operator domains, this is a self-adjoint first-order square root of the partner system. It is **not automatically** the intrinsic spin Dirac operator of the canonical catenoid or a physical relativistic fermion equation; it is a specified supersymmetric/block factorization of one-dimensional differential operators.

## 12. “Liouvillian” has three different mathematical meanings [C,K]

1. **Differential-algebraic Liouvillian solutions:** built from rational/algebraic functions by exponential, algebraic extensions and indefinite integration, as studied by differential Galois theory/Kovacic methods for second-order equations.
2. **Classical Liouville operator:** the Hamiltonian transport derivation $\mathscr L_Hf=\{f,H\}$ on phase-space densities/observables. It is linear in $f$ even when $H$ generates nonlinear trajectories; it is not a quantum Schrödinger eigenoperator.
3. **Open-system Liouvillian:** a chosen linear operator on density matrices, often a Lindblad generator after providing dissipators. It is not implied by Pinney or by deterministic Sturm–Liouville data.

The Pinney symmetric-square/phase reconstruction says that if the linear carrier has Liouvillian fundamental solutions, then suitable positive quadratic envelopes are expressible using algebraic operations and radicals. With a fixed positive $k$, the phase requires the additional quadrature $\int a^{-2}du$. The existence of a linear *third-order* equation does not guarantee elementary solutions for arbitrary variable coefficient $Q(u)$; nor is every Sturm–Liouville spectral problem Liouvillian.

## 13. A cross-operator taxonomy: which constructions are truly shared?

| Construction | Linear Sturm–Liouville | Nonlinear Pinney | Nature and obstruction |
|---|---|---|---|
| Gradient / Euler–Lagrange | first variation of quadratic functional | first variation of nonlinear inverse-square action | exact variational maps with different functionals |
| Hessian / Jacobi | original operator if quadratic | background-dependent $\mathcal H_a$ | linear in perturbation, not the original nonlinear solution |
| Hamiltonian / Lagrangian | phase-space matrix and quadratic energy | inverse-square classical Hamiltonian and Routhian | carrier and reduced dynamics; fixed angular charge |
| Jacobian | fundamental solution matrix | Jacobian of nonlinear Hamiltonian flow | tangent systems differ from nonlinear maps |
| Wronskian | conserved alternating form of two carrier solutions | coefficient of Gram quadratic via $\mathscr W^2$ | exact determinant mechanism |
| Laplacian | source of separated scalar SL expressions | can provide nonlinear radial reductions | dimension, weight and radial boundary essential |
| Riccati / Schwarzian | projective linear carrier | complex-log phase of amplitude | needs chart and nonvanishing solution |
| Casimir | matrix symplectic determinant | $H_0K-D^2=k/4$ | algebraic invariant, not spectral Rayleigh quotient |
| Green | resolvent kernel if spectral parameter is resolvent | diagonal product obeys symmetric-square Pinney constraint | typically **negative** $k$ for a real Green product |
| Rayleigh quotient | self-adjoint linear variational eigenvalue | quotient of **linearized Hessian**, or nonlinear constrained functional | no automatic eigenvalue quotient for Pinney itself |
| Darboux / Dirac | factorized first-order partners | acts on the *Hessian* at a background | no standard spin geometry inferred |
| Liouvillian | differential Galois/phase-space meanings | inherits solvability of carrier with extra constraints | distinct definitions must not be conflated |

## 14. Position-dependent mass: an authentic Sturm–Liouville operator with an ordering choice [D,K,V]

Consider a one-dimensional stationary effective-mass Schrödinger model in an independent spatial coordinate $z$, with **positive** prescribed effective mass $m(z)>0$, an energy-independent real potential $V(z)$, and Planck parameter $\hbar>0$. The BenDaniel–Duke (BDD) ordering is

```math
\widehat H_{\rm BDD}=-\frac{\hbar^2}{2}\partial_z\left(\frac1{m(z)}\partial_z\right)+V(z).
```

This is a Sturm–Liouville *differential expression*, with

```math
p(z)=\frac{\hbar^2}{2m(z)},\qquad q_0(z)=V(z),\qquad w(z)=1,\qquad\widehat H_{\rm BDD}\psi=E\psi.
```

It may be given a self-adjoint realization on $L^2(dz)$ after specifying endpoints, interface matching and a suitable domain. Hermitian-looking algebra is not enough to make every discontinuous-mass Hamiltonian self-adjoint. For simple piecewise smooth BDD data with no point interactions, the natural transmission conditions at an interface are continuity of $\psi$ and of $m^{-1}\psi_z$; more general self-adjoint interface conditions can be posed.

A PDM Hamiltonian is thus a **specified application of Sturm–Liouville theory**, not evidence that Sturm–Liouville *requires* a spatially variable physical mass. The source differential expression admits many other realizations.

## 15. The von Roos ambiguity: exact operator expansion [D,V,K]

For smooth $m(z)>0$, the one-dimensional von Roos family is

```math
\widehat T_{\alpha\beta\gamma}=\frac14[m^\alpha\widehat p\,m^\beta\widehat p\,m^\gamma+m^\gamma\widehat p\,m^\beta\widehat p\,m^\alpha],\qquad \widehat p=-i\hbar\partial_z,\quad \alpha+\beta+\gamma=-1.
```

**Theorem 15.1 [D,V] (all ordering effects are an effective potential for smooth mass).** On compactly supported smooth test functions,

```math
\widehat T_{\alpha\beta\gamma}=-\frac{\hbar^2}{2}\partial_z(m^{-1}\partial_z)+V_{\rm ord}(z)
```

with

```math
V_{\rm ord}=-\frac{\hbar^2}{4}(\alpha+\gamma)\frac{m''}{m^2}+\frac{\hbar^2}{2}(\alpha\gamma+\alpha+\gamma)\frac{(m')^2}{m^3}.
```

**Proof, step by step.** Apply the product rule twice to $m^\alpha\partial_z[m^\beta\partial_z(m^\gamma\psi)]$ and to the term with $\alpha,\gamma$ exchanged. The coefficient of $\psi''$ is $m^{-1}$, the combined coefficient of $\psi'$ is $-m'/m^2$ in the derivative expression, and the remaining multiplication terms simplify using $\alpha+\beta+\gamma=-1$. The identity was independently verified symbolically.

Two familiar choices are:

- BDD: $(\alpha,\beta,\gamma)=(0,-1,0)$, giving $V_{\rm ord}=0$.
- Zhu–Kroemer: $(-1/2,0,-1/2)$, giving

```math
V_{\rm ZK}=\frac{\hbar^2}{4}\frac{m''}{m^2}-\frac{3\hbar^2}{8}\frac{(m')^2}{m^3}.
```

An **ordering ambiguity is an operator-choice ambiguity**, not an Ermakov–Pinney nonlinearity. For discontinuous mass, $m''$ and $(m')^2$ can become distributionally singular or undefined; formal smooth-mass equivalence does not settle the interface problem. Different orderings with the **same written bare potential** are generally different operators and need not be isospectral.

## 16. Levi-Civita geometry selects one PDM ordering after fixing a measure [D,V,C]

A classical one-dimensional position-dependent kinetic metric is

```math
g=m(z)\,dz^2.
```

Intrinsic one-dimensional Levi-Civita curvature is identically zero even when $m'(z)\ne0$; a nonconstant metric coefficient is not itself nonzero curvature. The natural Riemannian volume is $\sqrt m\,dz$, and the Laplace–Beltrami operator is

```math
\Delta_g=m^{-1/2}\partial_z(m^{-1/2}\partial_z).
```

Its kinetic operator $-\hbar^2\Delta_g/2$ is symmetric in $L^2(\sqrt m\,dz)$. To compare on the BDD Hilbert space $L^2(dz)$, apply the **unitary** multiplication $U_g\psi=m^{1/4}\psi$. A direct differentiation yields

```math
U_g(-\hbar^2\Delta_g/2)U_g^{-1}=-\frac{\hbar^2}{2}\partial_z(m^{-1}\partial_z)+\frac{\hbar^2}{8}\frac{m''}{m^2}-\frac{7\hbar^2}{32}\frac{(m')^2}{m^3}.
```

**Theorem 16.1 [D,V].** This is precisely the smooth-mass von Roos ordering

```math
(\alpha,\beta,\gamma)=(-1/4,-1/2,-1/4).
```

**Proof.** Insert these parameters in $V_{\rm ord}$ from §15 and simplify. Direct calculation of the unitary conjugation produces the same result.

This is an exact **metric/measure-to-ordering dictionary**, but does **not** prove that nature universally selects it over BDD or another material-dependent effective model. Different measures, boundary/interface conditions and microscopic reductions can produce different valid operators. Flat one-dimensional curvature does not fix the entire effective quantum Hamiltonian.

## 17. The logarithmic framework as a special PDM Liouville coordinate [D,V]

For BDD let $p(z)=\hbar^2/[2m(z)]$, $w=1$. Its Liouville coordinate $\xi$ and amplitude multiplier are

```math
\xi=\int^z\frac{\sqrt{2m(s)}}{\hbar}\,ds,\qquad \rho(z)=p(z)^{1/4},\qquad \varphi(\xi)=\rho(z)\psi(z).
```

The transformed eigenvalue equation is

```math
-\varphi_{\xi\xi}+\left[V(z(\xi))+\frac{\rho_{\xi\xi}}{\rho}\right]\varphi=E\varphi.
```

Now choose the **explicit positive power-law mass**, on $z>0$,

```math
m(z)=m_0(z/c)^{-2},\qquad m_0>0,\qquad c>0.
```

Then

```math
\xi=\frac{c\sqrt{2m_0}}{\hbar}\ln(z/c),\qquad \rho(z)=\left(\frac{\hbar^2}{2m_0}\right)^{1/4}(z/c)^{1/2}.
```

Therefore the Liouville coordinate is a constant multiple of the **canonical logarithmic coordinate** $u=\ln(z/c)$, and its quantum geometric correction is a constant:

```math
\frac{\rho_{\xi\xi}}{\rho}=\frac{\hbar^2}{8m_0c^2}.
```

The transformed equation becomes

```math
-\varphi_{\xi\xi}+\left[V(c\,e^{\hbar\xi/(c\sqrt{2m_0})})+\frac{\hbar^2}{8m_0c^2}\right]\varphi=E\varphi.
```

This is an **exact** PDM-to-logarithmic-Liouville correspondence with $m_0,c,\hbar$ retained. The framework resolution $r$ may independently enter a chosen potential $V(z;r,c)$, but does not follow from the mass profile's exponent by itself. The original Master weighted operator has $p=x^3,w=x$, not the BDD pair $p=\hbar^2/(2m),w=1$; identical Liouville coordinates do **not** make their original Hilbert-space operators identical.

## 18. Duffing, Pinney and the singular reciprocal substitution [D,H,C]

The autonomous Duffing equation is

```math
y''=r^2y-2\mu r^2y^3,\qquad E_D=\frac12y'^2-\frac{r^2}{2}y^2+\frac{\mu r^2}{2}y^4.
```

It is nonlinear and its variational Hessian at the canonical separatrix is the order-two Pöschl–Teller operator of §10. Its first integral gives the binary quartic with

```math
z'^2=r^2(e+z^2-z^4),\quad z=\sqrt\mu\,y,\quad e=2\mu E_D/r^2,\qquad \Delta_{\rm quartic}=-16e(1+4e)^2.
```

For the Pinney envelope $a$ in §10 and $y=a^{-2}$, the exact reciprocal calculation gives the same cubic Duffing equation **only under the proper zero-shift constraint**. More generally, with

```math
a^2=Ae^{ru}+2C+Be^{-ru},\qquad k=r^2(AB-C^2),\qquad Q=r^2/4,
```

one obtains

```math
y''=r^2y-6Cr^2y^2-8r^2(AB-C^2)y^3.
```

**Proof.** From $y=a^{-2}$ compute $y''=6a^{-4}(a')^2-2a^{-3}a''$; insert Pinney and its constant Hamiltonian $H_{\rm EP}=-Cr^2/2$. The resulting quadratic term vanishes **iff** $C=0$.

Thus Duffing and Pinney are exactly linked along selected reciprocal families, but are **not the same nonlinear differential operator** for arbitrary initial data, finite Master energy or nonzero Gram shift. Their Hessians are not unitarily equivalent (§10).

## 19. Gross–Pitaevskii as a nonlinear spectral problem [K,D,C]

In $d$ Euclidean spatial dimensions, a standard dimensionless cubic Gross–Pitaevskii equation with a time-dependent isotropic harmonic trap is

```math
i\partial_t\Psi=-\frac12\Delta\Psi+\frac12\Omega(t)^2|X|^2\Psi+g(t)|\Psi|^2\Psi.
```

A stationary mode $\Psi(t,X)=e^{-i\nu t}\Phi(X)$ under constant parameters obeys

```math
\left[-\frac12\Delta+\frac12\Omega^2|X|^2+g|\Phi|^2\right]\Phi=\nu\Phi.
```

This is a mathematically well-defined **nonlinear eigenvalue problem**, often with a mass constraint; it does not satisfy linear superposition. Its second-variation/Bogoliubov–de Gennes operators nevertheless form a linear spectral system.

For a real stationary $\Phi$, write $\Psi=e^{-i\nu t}[\Phi+a+ib]$ with small real perturbations. To first order,

```math
\partial_t\binom{a}{b}=\begin{pmatrix}0&L_-\\-L_+&0\end{pmatrix}\binom{a}{b},\quad L_-=-\frac12\Delta+V+g\Phi^2-\nu,\quad L_+=-\frac12\Delta+V+3g\Phi^2-\nu.
```

The underlying Laplacian, operator domains and sign of $g$ matter for existence/stability. A scalar localized profile shared with the Master ODE is not proof that the full GPE realizes the same Hamiltonian, mass norm or physical medium.

## 20. Exact GPE lens scaling produces Pinney under a specified coupling law [D,K,V]

Let $\Phi(Y)$ solve a stationary reference equation with fixed constants $\omega_0,g_0,\nu$:

```math
-\frac12\Delta_Y\Phi+\frac12\omega_0^2|Y|^2\Phi+g_0|\Phi|^2\Phi=\nu\Phi.
```

Choose a positive scale $b(t)$ and a new clock $\tau'(t)=b(t)^{-2}$. Define the **explicit ansatz**

```math
\Psi(t,X)=b(t)^{-d/2}\exp\left[i\frac{\dot b(t)}{2b(t)}|X|^2-i\nu\tau(t)\right]\Phi(X/b(t)).
```

**Theorem 20.1 [D,K].** This solves the time-dependent GPE of §19 exactly if

```math
\ddot b+\Omega(t)^2b=\omega_0^2b^{-3},\qquad g(t)=g_0b(t)^{d-2}.
```

**Proof sketch with decisive coefficients.** Put $Y=X/b$, differentiate the scaling amplitude and quadratic phase, and evaluate the Laplacian. The transport terms cancel when the phase coefficient is $\dot b/(2b)$; the residual quadratic terms require $\ddot b+\Omega^2b=\omega_0^2/b^3$; the nonlinear cubic term carries a relative factor $g(t)b^{2-d}$ after the kinetic scaling, requiring $g(t)b^{2-d}=g_0$. The scalar phase is canceled by $\tau'=b^{-2}$.

For the **mass-critical cubic dimension $d=2$**, the coupling remains constant $g(t)=g_0$. For $d\ne2$ a time-dependent coupling must be imposed (unless the nonlinear term vanishes), or the simple ansatz is not exact. This is a genuinely qualified Pinney reduction, independent of the original $x$-coordinate and the Master parameter $\mu$. The lens scale $b(t)$ is not automatically the framework envelope $a(u)$: an identification requires $\Omega(t)$, $\omega_0$, a clock map $t\leftrightarrow u$ and a chosen reference state.

## 21. Keller–Miksis: the nonlinear bubble-radius equation is not generically Pinney [D,K,C]

Use a physical bubble radius $R_b(t)>0$ in a liquid of density $\rho_L>0$ and sound speed $c_L>0$. To first order in a wall Mach number, one common Keller–Miksis (KM) convention is

```math
\left(1-\frac{\dot R_b}{c_L}\right)R_b\ddot R_b+\frac32\left(1-\frac{\dot R_b}{3c_L}\right)\dot R_b^2=\frac1{\rho_L}\left[\left(1+\frac{\dot R_b}{c_L}\right)P+\frac{R_b}{c_L}\frac{dP}{dt}\right].
```

Here $P$ is a specified wall-pressure difference. For a common uncoated model it is

```math
P=p_g(R_b)-p_\infty(t)-\frac{2\sigma}{R_b}-\frac{4\eta_L\dot R_b}{R_b}.
```

The gas law, excitation, surface tension, viscosity and compressibility convention are **constitutive/model choices**; different published Keller–Miksis variants reorganize the terms. Because $P$ may depend on $\dot R_b$, its total derivative can contain $\ddot R_b$, and one must collect acceleration terms before treating the model as an explicit ODE.

There is **no general mathematical identification** of this equation with Pinney $a''=Qa+k/a^3$: KM has nonlinear acceleration coefficients, quadratic wall velocity, external forcing, possibly damping/radiation and a constitutive pressure law. A second-order *nonlinear* equation is not thereby an EP equation.

## 22. A constructive exact Rayleigh–Plesset-to-Pinney reduction [D,V]

Take the incompressible limit $c_L\to\infty$ in the stated model and, first, set aside explicit viscous dependence. The Rayleigh–Plesset equation becomes

```math
R_b\ddot R_b+\frac32\dot R_b^2=\frac{P(R_b,t)}{\rho_L}.
```

**Theorem 22.1 [D,V] (precise mass-flattening coordinate).** On every interval where $R_b>0$, put

```math
b(t)=R_b(t)^{5/2}.
```

Then Rayleigh–Plesset is *exactly* equivalent to

```math
\ddot b=\frac{5}{2\rho_L}\,b^{1/5}P(b^{2/5},t).
```

**Proof.** Differentiate twice:

```math
\ddot b=\frac52R_b^{1/2}\left(R_b\ddot R_b+\frac32\dot R_b^2\right).
```

Substitute the Rayleigh–Plesset equation and use $R_b^{1/2}=b^{1/5}$. No approximation is involved *after the incompressible model is chosen*.

### 22.1 An explicitly engineered pressure law gives an exact Pinney equation

**Corollary 22.2 [D,V].** Choose the mathematical pressure constitutive function

```math
P(R_b,t)=\frac{2\rho_L}{5}\left[-\Omega(t)^2R_b^2+kR_b^{-8}\right].
```

Then

```math
\ddot b+\Omega(t)^2b=kb^{-3},\qquad b=R_b^{5/2}.
```

**Proof.** Multiply the pressure by $(5/2\rho_L)R_b^{1/2}$ in Theorem 22.1. The two powers become $R_b^{5/2}=b$ and $R_b^{-15/2}=b^{-3}$ respectively.

The exponent $R_b^{-8}$ is *mathematically forced* by the $\rho^{-3}$ Pinney term under this mass-flattening map. This constructed pressure is **not a generic Keller–Miksis constitutive law**, nor is it proof of a laboratory fluid realizing a Pinney system. For ordinary polytropic gas $p_g\propto R_b^{-3\gamma_g}$, the special inverse-eighth power would require the nonstandard index $\gamma_g=8/3$ even before accounting for ambient pressure, surface tension, radiation and viscosity.

At $k>0$ the Pinney term is repulsive near $b=0$ in a conservative constant-frequency model; “nonlinear radial collapse” is not automatically reproduced by *positive* Pinney strength. Negative $k$, external energy input, a singular time-dependent coefficient or a different pressure law changes the question and can invalidate positivity/completeness assumptions.

### 22.2 Connection to position-dependent mass and a Routhian-style kinetic flattening

For an inviscid incompressible exterior flow, the radial kinetic energy is proportional to

```math
T_{\rm rad}=\frac12 m_{\rm eff}(R_b)\dot R_b^2,\qquad m_{\rm eff}(R_b)=4\pi\rho_LR_b^3.
```

Define a new coordinate by its configuration-space metric arclength:

```math
q(R_b)=\int^{R_b}\sqrt{m_{\rm eff}(s)}\,ds=\frac{4\sqrt{\pi\rho_L}}5R_b^{5/2}.
```

Then $T_{\rm rad}=\dot q^2/2$; the exponent $5/2$ used above is precisely the **position-dependent kinetic-mass flattening** coordinate. If $P=P(R_b,t)$ is independent of $\dot R_b$, the reduced Lagrangian is

```math
L_{\rm rad}=\frac12m_{\rm eff}(R_b)\dot R_b^2-U(R_b,t),\qquad \partial_{R_b}U=-4\pi R_b^2P(R_b,t).
```

Its Euler–Lagrange equation is Rayleigh–Plesset:

```math
R_b\ddot R_b+\frac32\dot R_b^2=P/\rho_L.
```

This provides an exact **classical PDM–Rayleigh–Plesset–Pinney dictionary in a selected conservative model**. It is separate from the quantum von Roos operator ordering, for which no canonical conclusion follows from the classical mass coordinate alone.

## 23. Small-amplitude bubble resonance yields a linear Sturm–Liouville-type problem [D,K,C]

Take $P=p_{g0}(R_0/R_b)^{3\gamma_g}-p_{\infty,0}-2\sigma/R_b-4\eta_L\dot R_b/R_b-p_{\rm ac}(t)$ in Rayleigh–Plesset, with equilibrium $R_0>0$ and

```math
p_{g0}=p_{\infty,0}+2\sigma/R_0.
```

Put $R_b(t)=R_0+\epsilon(t)$ with small $\epsilon$, and keep only linear terms. Then

```math
\ddot\epsilon+\Gamma_b\dot\epsilon+\omega_b^2\epsilon=-\frac{p_{\rm ac}(t)}{\rho_LR_0},
```

where the *incompressible-model* coefficients are

```math
\Gamma_b=\frac{4\eta_L}{\rho_LR_0^2},\qquad\omega_b^2=\frac{3\gamma_g p_{g0}-2\sigma/R_0}{\rho_LR_0^2}.
```

**Proof.** Expand $p_g(R_b)=p_{g0}[1-3\gamma_g\epsilon/R_0]+O(\epsilon^2)$, $-2\sigma/R_b=-2\sigma/R_0+2\sigma\epsilon/R_0^2+O(\epsilon^2)$ and $-4\eta_L\dot R_b/R_b=-4\eta_L\dot\epsilon/R_0+O(\epsilon^2)$. On the left $R_b\ddot R_b=R_0\ddot\epsilon+O(\epsilon^2)$, while $\dot R_b^2$ is second order. Divide by $\rho_LR_0$.

For negligible damping and surface tension, $\omega_b^2=3\gamma_g p_{\infty,0}/(\rho_LR_0^2)$ is the standard Minnaert-type small-oscillation value. Compressibility adds radiation effects and can shift frequency/damping; a full Keller–Miksis linearization has extra coefficients.

In homogeneous constant-coefficient form, the damped equation is transformed by $\epsilon=e^{-\Gamma_b t/2}v$ into

```math
\ddot v+\left(\omega_b^2-\frac{\Gamma_b^2}{4}\right)v=0.
```

This is a *linear* second-order equation. A true self-adjoint Sturm–Liouville eigenproblem requires specifying which **spatial** or temporal interval, weight and boundary conditions are intended. A damped open system is not automatically a self-adjoint normal-mode problem.

## 24. Spatial acoustic matching, shape modes and non-self-adjoint resonances [K,D]

For a separated scalar acoustic wave field in a spherical geometry, let the angular factor be a spherical harmonic $Y_{\ell m}$ with eigenvalue $\ell(\ell+1)$ under $-\Delta_{S^2}$. The radial Helmholtz equation in a homogeneous fluid is

```math
-(\rho^2h_\rho)_\rho+\ell(\ell+1)h=\frac{\omega^2}{c_L^2}\rho^2h.
```

This is a Sturm–Liouville *expression* on its chosen radial interval with

```math
p(\rho)=\rho^2,\qquad q_\ell=\ell(\ell+1),\qquad w(\rho)=\rho^2.
```

On a finite closed cavity with real energy-conserving boundary conditions it can give a self-adjoint spectrum. Coupling the boundary to a moving bubble typically adds a **frequency-dependent dynamic boundary condition**; outgoing radiation at infinity instead leads to a *non-self-adjoint resonance/scattering problem*. It is mathematically incorrect to cite the real self-adjoint Sturm–Liouville theorem for complex radiating resonances without a suitable extension.

A separate ideal inviscid surface-tension model of **nonspherical** shape perturbations has capillary modes with angular indices $\ell\ge2$ and classical leading frequencies

```math
\omega_\ell^2=\frac{(\ell-1)(\ell+1)(\ell+2)\sigma}{\rho_L R_0^3}.
```

This is a **specific model** and angular decomposition, not the same eigenproblem as the $\ell=0$ radial Keller–Miksis oscillator. Bubble interface conditions, gas density, compressibility, viscosity and flow coupling can change the formula.

**Conclusion for the bubble branch:** the nonlinear radius dynamics and its linearized perturbation/wave-matching operators can be studied simultaneously, but no universal transformation KM $\leftrightarrow$ EP $\leftrightarrow$ self-adjoint SL exists without the explicitly stated pressure law, limiting regime and boundary conditions.

## 25. A new exact weighted PDM–GPE–Pinney–Duffing amplitude/phase theorem [D,V]

There is a single *mathematical* equation that unifies the polar-amplitude mechanisms behind several of the named theories—without identifying their physical interpretations.

Let $p(z)>0$ be a smooth weight in an independent spatial coordinate $z$; let $V(z)$ be real, $g\in\mathbb R$, and let $E$ be a real stationary parameter. Consider the **specified nonlinear stationary Sturm–Liouville-type equation**

```math
-(p(z)\Psi_z)_z+[V(z)+g|\Psi|^2]\Psi=E\Psi.
```

The linear case is $g=0$. BDD PDM corresponds to $p(z)=\hbar^2/[2m(z)]$; smooth von Roos ordering changes $V$ to $V+V_{\rm ord}$. Ordinary stationary cubic GPE has constant $p=1/2$ in its dimensionless normalization.

Assume a nonzero complex solution on an interval, and write

```math
\Psi(z)=a(z)e^{i\theta(z)},\qquad a(z)>0.
```

**Theorem 25.1 [D,V] (weighted Duffing–Pinney polar decomposition).** Its real and imaginary equations are equivalent to

```math
\frac{d}{dz}[p a^2\theta_z]=0,\qquad \mathcal J=p a^2\theta_z=\mathrm{constant},
```

and

```math
(p a_z)_z=(V-E)a+g a^3+\frac{\mathcal J^2}{p a^3}.
```

**Proof, step by step.**

1. Differentiate $\Psi=a e^{i\theta}$ once and twice. The imaginary part of $-(p\Psi_z)_z+[V+g|\Psi|^2-E]\Psi=0$ gives $(p a^2\theta_z)_z=0$.
2. Thus $\theta_z=\mathcal J/(p a^2)$. The real part gives

```math
(p a_z)_z=p a\theta_z^2+(V-E)a+g a^3.
```

3. Replace $\theta_z^2$ with $\mathcal J^2/(p^2a^4)$ to obtain the displayed weighted inverse-cubic term. Reversing the steps reconstructs the original complex solution up to a constant phase.

The charge $\mathcal J$ is a Wronskian/current invariant of the **chosen stationary complex equation**. It is not automatically the Pinney Gram determinant, a Noether charge of an arbitrary time-dependent GPE, or a Chern number.

### 25.1 A third coordinate: the phase-flattening variable is not the Liouville spectral coordinate

Define

```math
\xi=\int^z\frac{ds}{p(s)}.
```

Since $p a_z=a_\xi$ and $(p a_z)_z=a_{\xi\xi}/p$, the amplitude equation is

```math
a_{\xi\xi}=p(z(\xi))[V(z(\xi))-E]a+p(z(\xi))g a^3+\mathcal J^2a^{-3}.
```

When $g=0$ this is exactly a **variable-coefficient Ermakov–Pinney equation**, with constant inverse-cubic coefficient $\mathcal J^2$. When $\mathcal J=0$ it is a stationary nonlinear cubic/weighted Duffing equation. If both are nonzero it contains both nonlinearities.

Note the two different coordinate differentials for BDD with $w=1$:

```math
d\xi=\frac{dz}{p(z)},\qquad d\tau=\frac{dz}{\sqrt{p(z)}}.
```

The first flattens the **phase-current/amplitude equation**; the second is the **self-adjoint Sturm–Liouville Liouville coordinate** (§17). They coincide only in special cases or after an explicit further map. This is an important clock distinction for all proposed PDM–Pinney correspondences.

### 25.2 Constant-coefficient stationary GPE: an elliptic cubic emerges

For dimensionless $p=1/2$, constant $V$ and $g$, define $j=\theta_z$ times $a^2$, so $j=a^2\theta_z=2\mathcal J$. Then

```math
a_{zz}=2(V-E)a+2g a^3+j^2a^{-3}.
```

Multiply by $a_z$ and integrate to obtain the exact first integral, with constant $C_E$,

```math
a_z^2=2(V-E)a^2+g a^4-j^2a^{-2}+C_E.
```

Put $J=a^2$. It follows that

```math
J_z^2=4gJ^3+8(V-E)J^2+4C_EJ-4j^2.
```

This is generically a smooth **elliptic cubic** when $g\ne0$ and its discriminant is nonzero. If $g=0$ the polynomial degree drops to at most two, the Pinney/conic case. The collision of roots and real positivity of $J$ must be studied separately; not every value of the cubic parameters gives a physical normalizable GPE state.

**Exact canonical specialization.** Choose the *independently specified spatial chart* $z=u=\ln(x/c)$, zero current $j=0$, and parameters

```math
V-E=r^2/2,\qquad g=-\mu r^2,\qquad C_E=0.
```

The amplitude equation becomes

```math
a_{uu}=r^2a-2\mu r^2a^3,
```

whose positive localized solution is $a=\mu^{-1/2}\mathrm{sech}(ru)$. This is a literal equality of **chosen stationary differential expressions**, not an assertion that the original Symmetrical Function represents a condensate. A nonzero stationary current adds an inverse-cubic Pinney barrier and destroys the exact original zero-current Duffing equation.

**This is the main application-level bridge:** linear SL corresponds to $g=0$; a fixed flux gives Pinney; a cubic stationary nonlinearity gives Duffing; both give a combined Duffing–Pinney equation. The entire statement is derived from one complex polar decomposition with all coefficients and currents explicit.

## 26. Canonical resolution r=2: the entire operator network at once [D,V,H]

Return explicitly to the original $u=\ln(x/c)$, retain $\mu,c>0$, and choose the *resolution* $r=2$ (independent of physical mass or acoustic parameters). The elementary profiles become rational:

```math
S_2=\mathrm{sech}(2u)=\frac{2c^2x^2}{x^4+c^4},\qquad W_2=\tanh(2u)=\frac{x^4-c^4}{x^4+c^4}.
```

The double-angle recursions are

```math
W_2=\frac{2W_1}{1+W_1^2},\qquad S_2=\frac{S_1^2}{2-S_1^2},\qquad W_2^2+S_2^2=1.
```

The canonical field, squared envelope and Pinney amplitude are

```math
f_\mu(x;2,c)=\frac{c^2x}{\sqrt\mu(x^4+c^4)},\qquad J_2=\sqrt\mu\cosh(2u)=\frac{\sqrt\mu(x^4+c^4)}{2c^2x^2},\qquad a_2=\sqrt{J_2}.
```

The **nonlinear envelope equation**, **linear symmetric-square equation**, and **fixed determinant constraint** simultaneously become

```math
a_2''=a_2+\mu a_2^{-3},\qquad J_2'''-4J_2'=0,\qquad 2J_2J_2''-(J_2')^2-4J_2^2=4\mu.
```

Choose the complex linear half-rate solution and its logarithmic derivative:

```math
\Phi_2=\mu^{1/4}(\cosh u+i\sinh u),\qquad \Phi_2''=\Phi_2,\qquad \Phi_2'/\Phi_2=W_2+iS_2.
```

Its modulus and phase are

```math
|\Phi_2|=a_2,\qquad \arg\Phi_2=\frac12\mathrm{gd}(2u),\qquad \theta_2'=S_2.
```

The two different self-adjoint **linearized** operators are

```math
\mathcal H_{\rm EP,2}=-\partial_u^2+1-3S_2^2,\qquad \mathcal H_{\rm Master,2}=-\partial_u^2+4-24S_2^2.
```

On the full real line the first has zero ground eigenvalue and essential spectrum starting at $1$, while the second has eigenvalues $-12$ and $0$ with continuum threshold $4$. These statements depend on the full-line $L^2(du)$ realizations and must not be transferred blindly to truncated $x$-domains.

### 26.1 The constant-potential Green function is *not* the positive canonical envelope

For the linear carrier Schrödinger operator

```math
L_0=-\partial_u^2+\frac{r^2}{4}
```

on $L^2(\mathbb R)$, the resolvent at zero energy exists for $r>0$ and has kernel

```math
G_0(u,v)=\frac1r\exp\left[-\frac r2|u-v|\right],\qquad G_0(u,u)=\frac1r.
```

The positive diagonal $R_0=1/r$ is constant and its square root solves the **negative-strength** Pinney equation

```math
a_G''=\frac{r^2}{4}a_G-\frac1{4a_G^3},\qquad a_G=r^{-1/2}.
```

At $r=2$, $a_G=1/\sqrt2$ is constant, while the framework's positive-determinant envelope $a_2=\mu^{1/4}\sqrt{\cosh(2u)}$ is nonconstant. Both are attached to the **same linear carrier**, but have **opposite determinant levels** in the symmetric-square invariant. This is a fully explicit counterexample to identifying the Green-diagonal and canonical Pinney amplitudes as the same function.

### 26.2 Resolution as a variable in other application equations

To obtain a matching hyperbolic PDM potential in the logarithmic coordinate, one must **choose** an external potential with argument $r\ln(z/c)$ and keep the PDM coordinate scale $\xi=(c\sqrt{2m_0}/\hbar)\ln(z/c)$ visible. At $r=2$, its Pöschl–Teller well becomes a rational function of $z^4+c^4$; its spectral energies additionally depend on $m_0,\hbar$ and the potential prefactor.

Likewise an exact GPE lens scale $b(t)$ can be chosen to share the Pinney equation $b''=b+\mu b^{-3}$ only when the trap coefficient and reference scale parameter are set to $\Omega(t)^2=-1$, $\omega_0^2=\mu$ and the clock is identified. This is a mathematically allowed *inverted* quadratic trap parameter but not a claim of a stable conventional confining condensate. Keller–Miksis would require the explicitly engineered pressure of §22 with the corresponding $\Omega^2$ sign and a separate physical time $t$.

## 27. Distinct nonlinear and linear “eigenvalue” problems [D,K,C]

There are at least four mathematically legitimate but distinct meanings of an eigenvalue-like parameter in this web:

1. **Linear Sturm–Liouville:** find $\phi\ne0$ in a fixed linear domain such that $L\phi=\lambda\phi$, with spectral theorem when $L$ is self-adjoint.
2. **Nonlinear stationary GPE:** find $(\Phi,\nu)$ with a fixed norm (or another constraint), satisfying $(-\frac12\Delta+V+g|\Phi|^2)\Phi=\nu\Phi$; $\nu$ is a Lagrange multiplier/nonlinear spectral parameter, not a linear eigenvalue with a vector-space eigenspace.
3. **Pinney boundary-value shooting:** for fixed $k$ and specified positive boundary data, ask for which $\lambda$ the nonlinear equation $a''=[V(z)-\lambda]a+k/a^3$ is solvable. This is a valid nonlinear parameter spectrum but has no ordinary linear superposition or general linear orthogonality theorem.
4. **Stability spectrum:** fix one nonlinear solution and study the self-adjoint (or coupled non-self-adjoint) Hessian/BdG operator on its chosen domain; its eigenvalues describe linear perturbations, not the original nonlinear solution set.

A Rayleigh quotient for the *linearized* Hessian has the usual quadratic-form interpretation. A nonlinear constrained energy has its own minimax/critical-point theory, not the unmodified Sturm–Liouville Rayleigh quotient. Confusing these four notions is the main mathematical source of the claim that nonlinear Ermakov–Pinney “cannot have an eigenvalue problem at all”.

## 28. The weighted Wronskian-current and nonlinear Riccati closure test [D,V]

Return to the general complex stationary equation of §25,

```math
-(p\Psi')'+(V+g|\Psi|^2)\Psi=E\Psi,\qquad p>0,\qquad V,g,E\ \mathrm{real}.
```

Take the complex conjugate of this **single equation**, multiply the original by $\bar\Psi$, multiply its conjugate by $\Psi$ and subtract. The nonlinear term cancels because $g|\Psi|^2$ is real:

```math
\frac d{dz}[p(\bar\Psi\Psi'-\bar\Psi'\Psi)]=0.
```

Consequently the current of the polar decomposition equals exactly the weighted self-conjugate Wronskian:

```math
\mathscr W_p(\bar\Psi,\Psi)=p(\bar\Psi\Psi'-\bar\Psi'\Psi)=2i\,p a^2\theta'=2i\mathcal J.
```

**Important distinction:** For a *linear* SL equation, the weighted Wronskian of **any two** solutions at the same spectral parameter is constant. For this **nonlinear** stationary equation, the Wronskian of two **different** solutions is generally not constant because their effective potentials depend on their respective amplitudes. The special conjugate-pair conservation follows from the global phase symmetry and the reality of the nonlinearity, not from unrestricted superposition.

### 28.1 Riccati does not automatically linearize GPE

On a nonzero complex stationary solution set

```math
h=p\frac{\Psi'}{\Psi}.
```

Direct differentiation gives

```math
h'=V-E+g|\Psi|^2-\frac{h^2}{p}.
```

When $g=0$ this is a closed complex Riccati equation and is projectively linearizable. When $g\ne0$, the term $|\Psi|^2$ is *not determined by the holomorphic coordinate $h$ alone as a prescribed coefficient*; the Riccati expression is coupled to the amplitude equation. Calling the full nonlinear GPE “Riccati and therefore always linearizable” would be false. The weighted polar equations provide the correct coupled system.

For the PDM BDD case, $\mathcal J$ is the conserved one-dimensional probability current **up to the physical normalization of $\hbar$**, and its interface continuity is related to the BDD flux boundary conditions. No flux should be identified with the BPST Chern number or a metric torsion scalar on the basis of the shared word “charge”.

## 29. A typed comparison of the operators, models and preserved data

| Source | Exact mathematical output | Required extra data | Lost information / non-equivalence |
|---|---|---|---|
| Regular/singular SL | linear expression and operator domain; weighted Wronskian | interval, $p,q,w$, endpoint conditions | formal expression alone does not fix the spectrum |
| Linear second-order carrier | Riccati, Schwarzian, symmetric-square third-order | nonzero fundamental pair, projective chart | poles of log derivative are solution zeros, not coefficient singularities |
| Pinney $a''=Qa+ka^{-3}$ | nonlinear envelope and its self-adjoint variational Hessian | $k$, positive interval, action and domain | nonlinear solution set not a linear eigenspace |
| Symmetric-square $J=a^2$ | linear third-order equation, fixed quadratic Casimir | positivity and invariant level $\mathcal C=4k$ | third-order equation alone does not fix $k$ |
| SL diagonal Green resolvent | product of two endpoint-adapted solutions | spectral parameter in resolvent set | its real Pinney strength is negative, unlike the canonical positive envelope |
| Routh reduction of 2D oscillator | Pinney with $k=\ell^2$ | cyclic angle and fixed moment-map value | reduced radial dynamics loses angle |
| Darboux/Dirac block | factored *linear* Hessians | superpotential, Hilbert domain | not an automatic spin Dirac operator or original nonlinear spectrum |
| PDM quantum Hamiltonian | weighted SL with chosen ordering | positive mass, $V,\hbar$, ordering/interface data | geometry/weight alone does not select material Hamiltonian |
| Stationary GPE | nonlinear eigenstate and BdG linearization | interaction sign/coupling, trap, norm | chemical potential not linear eigenvalue |
| Stationary weighted complex profile | Duffing + Pinney in polar equation | $p,V,g,E$, conserved current | not a single universal PDE or a linear Riccati for $g\ne0$ |
| GPE lens scaling | Pinney scale ODE | quadratic trap and $g(t)=g_0b^{d-2}$ | scale not full condensate field; dimensions matter |
| Incompressible Rayleigh–Plesset | variable-mass radial Lagrangian and $b=R^{5/2}$ | pressure law $P(R,t)$ | generic forcing/damping not Pinney |
| Keller–Miksis | compressible radius ODE | $c_L,\rho_L$, constitutive pressure, forcing | radiation/viscosity and nonlinear acceleration remain |
| Bubble acoustic modes | linear SL-type radial wave equation | angular order, acoustic boundary and radiation condition | open outgoing problem generally non-self-adjoint |
| Cubic Master at fixed $r,c,\mu$ | Duffing profile, quartic energy and PT Hessian | logarithmic chart and energy level | not an assertion of any specific PDM/GPE/bubble realization |

The algebro-geometric interface is therefore a **diagram of exact partial maps**, not a claim that a single global linear or nonlinear operator classifies all the rows.

## 30. Independent algebraic checks, corrections and scope [V,C]

The following identities were independently verified with exact symbolic calculations or by elementary differential expansions during this investigation:

1. **von Roos expansion:** the full ordered two-term kinetic expression equals BDD plus $V_{\rm ord}$ in §15, using only $\alpha+\beta+\gamma=-1$.
2. **Geometric PDM ordering:** unitary conjugation of $-\hbar^2\Delta_g/2$ from $L^2(\sqrt m\,dz)$ into $L^2(dz)$ yields the exact $(-1/4,-1/2,-1/4)$ terms in §16; direct subtraction simplifies identically to zero.
3. **PDM logarithmic mass:** $m(z)=m_0(z/c)^{-2}$ makes the Liouville spectral coordinate proportional to $\ln(z/c)$ and produces the constant correction $\hbar^2/(8m_0c^2)$.
4. **Pinney symmetric square:** for $J=Ae^{ru}+2C+Be^{-ru}$, verify both $J'''-r^2J'=0$ and $\mathcal C[J]=4r^2(AB-C^2)$.
5. **Pinney Green relation:** for two carrier solutions, direct differentiation gives the negative-Wronskian Gel'fand–Dikii identity of §7; normalized diagonal Green gives right-hand side $1$.
6. **Routhian Casimir:** the canonical brackets and $H_0K-D^2=k/4$ follow by direct Poisson differentiation.
7. **Canonical Hessians:** direct differentiation of the EP and Duffing equations gives the PT potentials and first-order factorizations in §10; the full-line bound-state assertions use standard PT spectral theory with the specified $L^2$ domain.
8. **Rayleigh–Plesset coordinate:** direct differentiation confirms $\ddot b=(5/2)R_b^{1/2}(R_b\ddot R_b+\tfrac32\dot R_b^2)$; the pressure powers $R_b^2,R_b^{-8}$ become $b,b^{-3}$.
9. **Classical kinetic mass:** $m_{\rm eff}(R_b)=4\pi\rho_LR_b^3$ is flattened by $q=(4/5)\sqrt{\pi\rho_L}R_b^{5/2}$.
10. **Small bubble linearization:** Taylor expansion of the pressure and radial kinematics gives $\Gamma_b$ and $\omega_b^2$ in §23; Keller–Miksis compressible corrections are *not* silently discarded when claiming the final physical frequency.
11. **Weighted polar decomposition:** substituting $\Psi=a e^{i\theta}$ in the nonlinear real-coefficient stationary equation proves both the current and weighted Duffing–Pinney amplitude equation.
12. **Constant-coefficient stationary GPE cubic:** multiplying the amplitude equation by $a_z$ and using $J=a^2$ gives the elliptic cubic polynomial in §25.
13. **Canonical $r=2$ entire web:** the rational $S_2,W_2$, complex solution, PT Hessians, Pinney constraint and constant diagonal Green kernel follow by direct differentiation.

**Scope of the checks:** Exact algebra does **not** certify every global functional-analytic theorem or physical approximation. In particular, global GPE solution existence and instability, nonlinear Pinney boundary value problems, physical validity of the engineered RP pressure, quantum PDM interface models, or Keller–Miksis resonance spectra require their own hypotheses and independent analysis.

### 30.1 Especially tempting overstatements to reject

- “Because Pinney is nonlinear, operators, eigenvalues, Green identities or Rayleigh quotients cannot appear in its theory.” **False**: nonlinear operators, Fréchet Hessians, constrained nonlinear spectra, and the symmetric-square/Green identities are well-defined.
- “Because a differential expression is formally Sturm–Liouville, its spectrum is automatically real and discrete.” **False** without a specified self-adjoint realization and compactness.
- “The symmetric-square linearization makes every Pinney solution a linear SL eigenfunction.” **False**: positivity and the quadratic Casimir level remain nonlinear constraints.
- “PDM geometry uniquely proves the BDD kinetic ordering.” **False**: the geometric Laplace–Beltrami ordering gives a different exact von Roos set on a chosen measure.
- “The Gross–Pitaevskii equation is equivalent to Pinney for arbitrary dimension and coupling.” **False**: the lens map has the explicit law $g(t)=g_0b^{d-2}$, and the stationary polar equation contains a cubic term unless $g=0$.
- “Keller–Miksis bubble collapse is always an inverse-cubic oscillator.” **False**: only an engineered pressure after the stated Rayleigh–Plesset limit yields that special form.
- “A shared PT potential, Riccati coordinate, or elliptic $j$ identifies the physical realizations.” **False**: functions, spectra, dimensions, clocks, measures and boundary conditions must be retained.

## 31. Research questions for the next foundational audit [O]

1. **Inverse spectral/PDM:** For $m=m_0(z/c)^{-2}$ and a PT potential $V\propto\mathrm{sech}^2(r\ln(z/c))$, determine explicit spectral maps and interface scattering data for each von Roos ordering, including the scale parameters $c,m_0,\hbar$.
2. **Green and Pinney discriminant:** Investigate the complexified diagonal resolvent's Gram determinant as $z$ crosses spectral gaps and poles, paying attention to the positivity of the diagonal and the branch of its square root.
3. **Ermakov–Lewis/Routhian:** Determine all self-adjoint boundary realizations of the half-integer PT Hessian naturally compatible with a positive Pinney amplitude on finite and half-infinite intervals; compare with the order-two Master Hessian.
4. **GPE invariant curve:** Classify the discriminant and real ovals of the stationary constant-potential cubic in §25 as functions of $(g,V-E,C_E,j)$; determine the genuine genus-one-to-separatrix degeneration and the marked phase differential $j\,dz/J$.
5. **Nonlinear current versus weighted SL Wronskian:** Establish a boundary-form theorem for the stationary nonlinear equation with the self-conjugate pair $\bar\Psi,\Psi$ across piecewise smooth PDM interfaces.
6. **Two-dimensional scaling:** Review precise global well-posedness and domain conditions of the critical $d=2$ GPE lens transform; test whether any framework $r$-family provides genuine integrable scaled solutions of a specific trap rather than simply matched ODE coefficients.
7. **Bubble radial mass:** For physically common gas polytropic exponents, classify the monomial powers after $b=R^{5/2}$ and determine when a generalized Emden–Fowler or generalized Pinney system, rather than standard EP, is obtained.
8. **KM acoustic boundaries:** Construct the correct coupled bubble-fluid energy Hilbert space in a *closed, lossless* geometry and determine which wave matching conditions make the linearized operator self-adjoint; compare its complex radiating resonance formulation.
9. **Operator algebras:** Distinguish spectral Darboux, Liouville transport and nonlinear Hamiltonian Casimir claims in the existing CLAIMS register, and propose exact regression tests before promoting any statement.

## 32. Literature and project attribution

**Internal project material:** Current foundational SF-I-020 (linear exponential backbone, canonical $u=\ln(x/c)$); provisional drafts 080, 090, 100 (SL projectivization, Pinney complex phase and conditional amplitude–phase duality), 040 (connection/warped metric dictionary), 050 (separate binary quartics), 060 (Sobolev/Yamabe/PT/OU/GPE-adjacent profiles), 070 (Noether/Routhian and invariant classification). The November 18 ZIP contains spectral calculus, Riccati, Pinney/Gram, quartic and Duffing analyses. No claim is made that the ZIP pre-verified the PDM, stationary GPE or Keller–Miksis reductions developed here.

**Classical Sturm–Liouville / special functions:**
- NIST DLMF §1.13, Liouville transformation and special-function second-order ODEs: https://dlmf.nist.gov/1.13
- NIST DLMF §1.18, self-adjoint SL, Green functions and spectral theory: https://dlmf.nist.gov/1.18
- Encyclopedia of Mathematics, Sturm–Liouville theory: https://encyclopediaofmath.org/wiki/Sturm-Liouville_theory

**PDM and ordering, checked externally:**
- Classical and quantum systems with position-dependent mass, Brazilian Journal of Physics Education (2023): https://www.scielo.br/j/rbef/a/8gHrhh3Yr4s7ymwZZ3TsBkj/?format=html
- A novel approach for constructing kinetic energy operators with position dependent mass: https://www.sciencedirect.com/science/article/pii/S2211379719303055
- BenDaniel–Duke matching and operator boundary form: https://mochizuki-tus.github.io/QM_Textbook_EN/ch11_finite_well.html

**Gross–Pitaevskii and Pinney scaling:**
- From Feshbach-resonance managed Bose–Einstein condensates to anisotropic universes: Applications of the Ermakov–Pinney equation with time-dependent nonlinearity, Physics Letters A (2007): https://www.sciencedirect.com/science/article/pii/S0375960107003362 . This is a literature precedent for conditional EP/moment reductions, not evidence that every GPE solution is of lens form.
- For the GPE lens theorem in §20, the precise $b(t)$ and $g(t)$ laws are derived algebraically in the text rather than inferred from a physical analogy.

**Keller–Miksis and bubble acoustic models:**
- Bubble Dynamics in Soft and Biological Matter, Annual Review of Fluid Mechanics: https://doi.org/10.1146/annurev-fluid-010518-040352
- Experimental/theoretical pressure dependence of bubbly-media sound speed and attenuation: https://pmc.ncbi.nlm.nih.gov/articles/PMC11487347/
- Rayleigh–Plesset and Keller–Miksis formula comparison: https://www.tandfonline.com/doi/full/10.1080/19942060.2023.2210193
- Acoustic bubble shape and radial linearizations: https://pmc.ncbi.nlm.nih.gov/articles/PMC2818980/

**Gel'fand–Dikii / diagonal Green link:** The core identity is proved in §7 from the product of two fundamental solutions; source literature includes one-dimensional diagonal-resolvent and Gel'fand–Dikii treatments (for example JHEP 2009 source indexed in the bibliography of the project investigation). Do not transfer its normalization or spectral interpretation without the resolvent-domain hypotheses.

**Final mathematical statement:** Standard linear Sturm–Liouville theory, nonlinear Ermakov–Pinney dynamics, and specific PDM/GPE/bubble equations intersect through *explicit differential constructions*: a weighted Wronskian, a nonlinear amplitude-phase equation, symmetric-square invariant levels, Routh reduction, a stability Hessian and selected mass/clock changes. Their identical-looking functions or operators can be shared without equating their Hilbert spaces, actions, boundary conditions or applications. The role of the framework is to record these typed maps, not to collapse them into one universal physical theory.
