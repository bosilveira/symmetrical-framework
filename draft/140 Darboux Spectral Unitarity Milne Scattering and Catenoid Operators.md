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

## 6. Normalized Jost waves reconstruct exact positive Pinney envelopes [D,V,K]

For real $k>0$ define the two distinct products

```math
\mathcal D_n(k)=\prod_{j=1}^n(jr-ik),\qquad D_n(k^2)=|\mathcal D_n(k)|^2=\prod_{j=1}^n(k^2+j^2r^2).
```

The normalized right Jost solution is obtained by applying the **adjoint Darboux chain** to the free plane wave:

```math
\Psi_{n,k}(u)=\frac{Q_n^\dagger e^{iku}}{\mathcal D_n(k)}.
```

It solves

```math
h_n\Psi_{n,k}=k^2\Psi_{n,k},\qquad \Psi_{n,k}(u)\sim e^{iku}\quad(u\to+\infty).
```

Since $W\to-1$ as $u\to-\infty$, the same solution has left asymptotic

```math
\Psi_{n,k}(u)\sim \mathcal D_n(k)^{-1}\prod_{j=1}^n(-jr-ik)e^{iku}\quad(u\to-\infty).
```

No $e^{-iku}$ component appears: **the reflection coefficient is identically zero**. The unit-modulus transmission amplitude is

```math
T_n(k)=\prod_{j=1}^n\frac{k+ijr}{k-ijr},\qquad |T_n(k)|=1,\qquad k>0.
```

This is the classical integer reflectionless Pöschl–Teller scattering formula; the present proof is simply the explicit Darboux action and its asymptotics. Its phase is a *scattering phase*, not a Berry holonomy.

### 6.1 Wronskian normalization fixes the Pinney strength

Let $\Psi_{n,k}=a_{n,k}e^{i\theta_{n,k}}$, with the positive modulus $a_{n,k}=|\Psi_{n,k}|$. Its current is

```math
j_{n,k}=\mathrm{Im}(\bar\Psi_{n,k}\Psi_{n,k,u})=a_{n,k}^2\theta_{n,k,u}.
```

The potential and $k^2$ are real, so $j_{n,k}$ is constant. At $u\to+\infty$, $\Psi_{n,k}\sim e^{iku}$, hence **exactly**

```math
j_{n,k}=k,\qquad \theta_{n,k,u}=\frac{k}{a_{n,k}^2}.
```

The real part of the complex carrier equation therefore proves

```math
a_{n,k,uu}=(V_n-k^2)a_{n,k}+k^2a_{n,k}^{-3},\qquad V_n=-n(n+1)r^2S^2.
```

**Theorem 6.1 [D,V].** Every integer Pöschl–Teller reflectionless scattering wave at $k>0$ determines a **globally positive Ermakov–Pinney amplitude** with a universal *scattering-normalized* Pinney strength $k_{\rm EP}=k^2$, independently of the depth $n$ and the original Master amplitude parameter $\mu$.

The coefficient $k^2$ is not a universal law for arbitrary normalizations: multiplying the scattering wave by a constant $\alpha$ changes the current by $|\alpha|^2$ and the Pinney strength by $|\alpha|^4$. It is precisely the **unit incident-wave normalization** that fixes $k_{\rm EP}=k^2$.

## 7. The squared Jost modulus is the Gel'fand–Dikii polynomial [D,V]

Let the unnormalized Darboux wave be

```math
Q_n^\dagger e^{iku}=e^{iku}B_n(k,W),\qquad B_n(k,W)=e^{-iku}Q_n^\dagger e^{iku}.
```

Since the Darboux coefficients are real, for real $k,W$ the product

```math
F_n(k^2,u)=B_n(k,W)\overline{B_n(k,W)}
```

is a real polynomial in $k^2$ and $W$. For $n=1,2$, the direct calculations are exactly the squared-eigenfunction polynomials of draft 130. The equality for general integer $n$ follows from the Darboux recursion and normalization at infinity, up to the chosen leading coefficient.

The normalized scattering amplitude becomes

```math
a_{n,k}^2=\frac{F_n(k^2,u)}{D_n(k^2)}.
```

The unnormalized Gel'fand–Dikii invariant is

```math
\mathscr R_n(k^2)=-4k^2D_n(k^2)^2.
```

Dividing $F_n$ by the positive constant $D_n$ converts the invariant to

```math
2(a_{n,k}^2)(a_{n,k}^2)_{uu}-[(a_{n,k}^2)_u]^2-4(V_n-k^2)(a_{n,k}^2)^2=4k^2.
```

Thus the **same** positive Pinney strength can be read as (i) squared normalized scattering current, (ii) normalized Gram/Wronskian determinant, or (iii) the rescaled Gel'fand–Dikii polynomial. These are different descriptions of one *specified* spectral solution, not invariants of unrelated physical applications.

## 8. Closed order-one Jost and Milne formulas [D,V]

For $n=1$, one Darboux step gives

```math
B_1(k,W)=rW-ik,\qquad F_1(k^2,u)=k^2+r^2W^2.
```

The normalized wave and envelope are

```math
\Psi_{1,k}=\frac{rW-ik}{r-ik}e^{iku},\qquad a_{1,k}^2=\frac{k^2+r^2W^2}{k^2+r^2}.
```

The **exact Pinney equation** and phase velocity are

```math
a_{1,k,uu}=(-2r^2S^2-k^2)a_{1,k}+k^2a_{1,k}^{-3}.
```

```math
\theta_{1,k,u}=k\frac{k^2+r^2}{k^2+r^2W^2}.
```

This is a localized deformation of the free amplitude $a=1$: it tends to $1$ at both ends, while the phase velocity differs from $k$ in the interior. Notice that this scattering-normalized Pinney family is **not** the centered unbounded canonical envelope $a=\mu^{1/4}\sqrt{\cosh(ru)}$ of the half-rate carrier; they solve different carrier equations and occupy different invariant levels.

## 9. Closed order-two Jost and Milne formulas [D,V]

For $n=2$, apply $A_2^\dagger A_1^\dagger$ to $e^{iku}$. Exact differentiation gives

```math
B_2(k,W)=r^2(3W^2-1)-k^2-3ikrW.
```

Its squared modulus is the polynomial of draft 130:

```math
F_2(k^2,u)=k^4+r^2(3W^2+2)k^2+r^4(3W^2-1)^2.
```

The normalization denominator is

```math
D_2(k^2)=(k^2+r^2)(k^2+4r^2).
```

Consequently

```math
\Psi_{2,k}=\frac{B_2(k,W)e^{iku}}{(r-ik)(2r-ik)},\qquad a_{2,k}^2=\frac{F_2(k^2,u)}{(k^2+r^2)(k^2+4r^2)}.
```

The exact nonlinear and phase equations are

```math
a_{2,k,uu}=(-6r^2S^2-k^2)a_{2,k}+k^2a_{2,k}^{-3}.
```

```math
\theta_{2,k,u}=k\frac{(k^2+r^2)(k^2+4r^2)}{k^4+r^2(3W^2+2)k^2+r^4(3W^2-1)^2}.
```

For $k>0$ the denominator is strictly positive. The same real $u$-dependent profile that gives the **Master Hessian** therefore also supports an entire positive *scattering* Pinney family, with spectral parameter-dependent current but no claim of non-self-adjointness.

## 10. The Milne excess phase is exactly the transmission phase [D,V,K]

A continuous unwrapped phase may be chosen so that $\theta_{n,k}(u)-ku\to0$ as $u\to+\infty$. The Jost asymptotics then imply

```math
\int_{-\infty}^{\infty}\left[\theta_{n,k,u}-k\right]du=\mathrm{arg}\,T_n(k)
```

with a continuous branch matched to the scattering normalization. Since

```math
T_n(k)=\prod_{j=1}^n\frac{k+ijr}{k-ijr},
```

its unwrapped phase is

```math
\delta_n(k)=2\sum_{j=1}^n\arctan\left(\frac{jr}{k}\right),\qquad k>0.
```

**Theorem 10.1 [D,V] (scattering phase as Pinney excess phase).**

```math
\int_{-\infty}^{\infty}k\left[\frac{D_n(k^2)}{F_n(k^2,u)}-1\right]du=2\sum_{j=1}^n\arctan\left(\frac{jr}{k}\right).
```

This is an exact **integral identity** combining the nonlinear Pinney amplitude, the spectral polynomial and the linear scattering transmission amplitude. It is a useful new consolidated theorem in the framework, distinct from the canonical arctangent primitive of the original Symmetrical Function.

### 10.1 Direct elementary check for n=1

For the first well,

```math
\theta_{1,k,u}-k=\frac{kr^2S^2}{k^2+r^2W^2}.
```

Set $w=W(u)$, $dw=rS^2du$. Then

```math
\int_{\mathbb R}(\theta_{1,k,u}-k)du=kr\int_{-1}^{1}\frac{dw}{k^2+r^2w^2}=2\arctan(r/k).
```

This independently confirms the phase formula without invoking an abstract scattering theorem.

**Endpoint caveat:** As $k\downarrow0$, the unwrapped phase tends to $n\pi$; at a bound-state or threshold spectral value the normalized positive-amplitude formula can degenerate. The scattering phase is not an automatically quantized Berry phase or a topological Chern integral.
