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
