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
