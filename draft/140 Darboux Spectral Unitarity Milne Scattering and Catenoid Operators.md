---
id: SF-DRAFT-140
title: Darboux Spectral Unitarity, Milne Scattering, and Catenoid Operators
status: provisional
created: 2026-11-18
proposed_layers: [I, II, III]
depends_on: [SF-I-020, SF-DRAFT-030, SF-DRAFT-050, SF-DRAFT-080, SF-DRAFT-090, SF-DRAFT-100, SF-DRAFT-110, SF-DRAFT-120, SF-DRAFT-130]
related_claims: [H95, H100, H169, H170, H171, H172, H177, H178, H179, H183, H299, H391, H392, H393, H421, H424]
---

# 140 Darboux Spectral Unitarity, Milne Scattering, and Catenoid Operators

**Research status:** Provisional, rigorous mathematical investigation. [D] direct proof; [V] independently checked symbolic algebra; [K] established classical result under hypotheses; [H] historical verified claim with original scope; [C] correction; [O] open. No physical realization is inferred from shared equations.

**Question:** Can the spectral SL–EP closure of draft 130 be strengthened to an actual operator intertwiner, exact scattering phase/Pinney amplitude, and an operator-domain-safe catenoid map? Track the center $c$, resolution $r$, amplitude $\mu$, scattering parameter $k$, spectral parameter $\lambda$, well depth $n$, and surface Fourier index $m$.

**Source audit:** The historical uploaded ZIP (November 18 backup) already verifies the Lax–Novikov and Burchnall–Chaundy differential-operator identities for $n=1,\ldots,4$, under claim IDs H100/H299 and verification/audit4/audit4_lax_novikov.py, with passing log. The present draft **does not rediscover those identities**: it starts from them and develops a polar-unitary continuous-spectrum equivalence, normalized Jost–Milne amplitudes, exact phase shifts and half-line logarithmic derivatives, an original-$x$ weighted distorted Fourier–Mellin transform, and a catenoid Jacobi-operator conjugation. The latest live draft 130 (especially §§9–14 and §33), drafts 100, 110, 120, the foundational source and original ZIP were reopened. Relevant classical references are listed at the end.

## 1. Canonical dictionary

Keep the original scales:

```math
r,c,\mu,x>0,\qquad u=\ln(x/c),\qquad x=ce^u,\qquad S=\mathrm{sech}(ru),\qquad W=\tanh(ru),\qquad S^2+W^2=1.
```

The original function and weighted Hilbert transform are

```math
f_\mu(x;r,c)=\frac{S}{2\sqrt\mu\,x},\qquad (U_cf)(u)=xf(ce^u),\qquad \|f\|^2_{L^2(x\,dx)}=\|U_cf\|^2_{L^2(du)}.
```

Let $n=0,1,\ldots$ denote **Pöschl–Teller well depth**, $m\in\mathbb Z$ an unrelated **catenoid angular index**, $k>0$ a real **scattering wave number**, and $\lambda=k^2$ the unshifted real spectral energy. Do not confuse $\lambda$ with the Riemann surface family modulus, the resolution $r$, or the Master amplitude $\mu$.

Define

```math
h_n=-\partial_u^2-n(n+1)r^2S^2,\qquad h_0=-\partial_u^2,\qquad H_{\rm Master}=h_2+r^2.
```

These bounded-real-potential Schrödinger expressions have natural self-adjoint $H^2(\mathbb R)$ realizations. The surface catenoid Jacobi operator is a **different** geometric operator; §15 derives its exact unitary representation.

## 2. Darboux factorization and entire ladder [D,V,H100,H299]

Let

```math
A_j=\partial_u+jrW,\qquad A_j^\dagger=-\partial_u+jrW,\qquad j=1,2,\ldots.
```

Using $W_u=rS^2$ and $W^2=1-S^2$ gives

```math
A_j^\dagger A_j=h_j+j^2r^2,\qquad A_jA_j^\dagger=h_{j-1}+j^2r^2.
```

Therefore

```math
A_jh_j=h_{j-1}A_j,\qquad h_jA_j^\dagger=A_j^\dagger h_{j-1}.
```

Define the ordered Crum operator and polynomial

```math
Q_n=A_1A_2\cdots A_n,\quad Q_n^\dagger=A_n^\dagger\cdots A_1^\dagger,\quad\Pi_n(z)=\prod_{j=1}^n(z+j^2r^2).
```

**Theorem 2.1 [D,V,H299].** On the common smooth test-function core,

```math
Q_nh_n=h_0Q_n,\qquad h_nQ_n^\dagger=Q_n^\dagger h_0.
```

```math
Q_n^\dagger Q_n=\Pi_n(h_n),\qquad Q_nQ_n^\dagger=\Pi_n(h_0).
```

**Proof.** Compose successive factorizations, moving the spectral polynomials through each first-order Darboux operator by the intertwining identities. The fourth identity was independently checked here for $n=1,2,3$ with a generic symbolic exponential test function. Passing from formal differential expressions to closed operators requires the chosen Hilbert domains.

## 3. Lax–Novikov and Burchnall–Chaundy: archived theorem, not new novelty [H100,H299]

The historical verified odd-order commuting operator is

```math
P_n=Q_n^\dagger\partial_u Q_n,\qquad [P_n,h_n]=0,\qquad P_n^\dagger=-P_n\quad(\mathrm{formally}).
```

Its exact polynomial identity is

```math
P_n^2=-h_n\Pi_n(h_n)^2.
```

Thus the singular spectral curve of the operator pair $(h_n,P_n)$ is

```math
\nu^2=-\lambda\prod_{j=1}^n(\lambda+j^2r^2)^2.
```

The Gel'fand–Dikii invariant of draft 130 is

```math
\mathscr R_n(\lambda)=-4\lambda\prod_{j=1}^n(\lambda+j^2r^2)^2=4\nu^2.
```

This is the precise **factor-four** dictionary between the commuting-operator spectral curve and the squared-eigenfunction/Pinney spectral curve. Both models are singular soliton degenerations. They are separate from the **Master mechanical energy quartic**, the **Pinney mechanical energy quartic**, and the universally singular **Gram-square quartic**.

## 4. The Darboux kernel is exactly the discrete bound-state subspace [D,V,K]

For integer $n>0$, the bound-state energies are $-j^2r^2$ for $j=1,\ldots,n$, while the absolutely continuous spectrum is $[0,\infty)$. If $\varphi_{n,j}$ is a normalized bound eigenfunction,

```math
\|Q_n\varphi_{n,j}\|_2^2=\langle\varphi_{n,j},\Pi_n(h_n)\varphi_{n,j}\rangle=0.
```

Therefore $Q_n\varphi_{n,j}=0$. Conversely an order-$n$ differential operator has at most $n$ independent local zero modes, so the $n$ square-integrable modes exhaust its kernel:

```math
\ker_{L^2}Q_n=\mathrm{span}\{\varphi_{n,j}:j=1,\ldots,n\}.
```

Hence **all and only the discrete bound modes are removed by the intertwiner**. A global unitary equivalence $h_n\simeq h_0$ cannot hold because their discrete spectra differ. A unitary equivalence on the continuous subspace is nevertheless available.

## 5. Polar decomposition gives a genuine unitary spectral intertwiner [D,V,K]

Let $\mathcal H_{\rm ac}(h_n)$ denote the absolutely continuous subspace. On that subspace $\Pi_n(h_n)$ has a strictly positive spectral lower bound, since its real spectrum is evaluated at $\lambda\ge0$. Form the polar part

```math
\mathcal U_n=Q_n\Pi_n(h_n)^{-1/2}\quad\mathrm{on}\quad\mathcal H_{\rm ac}(h_n).
```

**Theorem 5.1 [D,V,K].** This has a unitary extension

```math
\mathcal U_n:\mathcal H_{\rm ac}(h_n)\longrightarrow L^2(\mathbb R,du)
```

intertwining the self-adjoint operators on compatible domains:

```math
\mathcal U_nh_n=h_0\mathcal U_n.
```

**Proof.** On the absolutely continuous subspace,

```math
\|\mathcal U_nf\|_2^2=\langle f,\Pi_n(h_n)^{-1/2}Q_n^\dagger Q_n\Pi_n(h_n)^{-1/2}f\rangle=\|f\|_2^2.
```

Its isometric range is closed. The identity $Q_nQ_n^\dagger=\Pi_n(h_0)$ and the strictly positive free lower bound $\Pi_n(h_0)\ge\prod_{j=1}^nj^2r^2$ imply $\ker Q_n^\dagger=\{0\}$ and dense range, hence surjectivity. The intertwining follows because $\Pi_n(h_n)^{-1/2}$ commutes with $h_n$ by functional calculus. The polar map is not an isometry **on the omitted bound-state space**, where $Q_n$ vanishes.

The full Hilbert space has an exact orthogonal decomposition

```math
L^2(\mathbb R,du)=\mathrm{span}\{\varphi_{n,1},\ldots,\varphi_{n,n}\}\oplus\mathcal H_{\rm ac}(h_n).
```

This is a **genuine spectral correspondence** rather than a mere coincidence of potential formulas: the continuous part is unitary to the free operator, while the discrete finite-dimensional defect is explicitly retained.
