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

## 11. Exact half-line boundary Riccati/Weyl data at the symmetry center [D,V]

The logarithmic center $x=c$ is exactly $u=0$. For the right-decaying Weyl solution at negative energy, or the outgoing Jost solution for positive energy, use the boundary **logarithmic derivative**

```math
m_{+,n}(k)=\frac{\Psi_{n,k,u}(0)}{\Psi_{n,k}(0)}.
```

This is a Riccati boundary coordinate for the **chosen right-normalized solution**. At a zero of $\Psi_{n,k}(0)$ it has a pole: the projective chart fails, while the original linear differential equation remains regular. The notation $m_+$ is meaningful as a Weyl–Titchmarsh function only after the complex energy branch and the right half-line domain are specified.

### 11.1 First well: an explicit rational boundary function

For $\Psi_{1,k}\propto(rW-ik)e^{iku}$, use $W(0)=0$ and $W_u(0)=r$:

```math
m_{+,1}(k)=ik+\frac{r^2}{-ik}=i\frac{k^2+r^2}{k}.
```

For an $L^2$ right-decaying solution at negative energy, analytically continue $k=i\kappa$, $\kappa>0$:

```math
m_{+,1}(i\kappa)=-\kappa+\frac{r^2}{\kappa}.
```

It vanishes at $\kappa=r$, exactly the **even/Neumann** bound level $E=-r^2$ of $h_1$. This is a spectral boundary statement, unlike a claim that the Riccati circle by itself tests self-adjointness.

### 11.2 Second well: one Neumann zero and one Dirichlet pole

For the polynomial of §9, evaluate at the center:

```math
B_2(k,0)=-(k^2+r^2),\qquad (B_2)_u(k,0)=-3ikr^2.
```

Therefore

```math
m_{+,2}(k)=ik\frac{k^2+4r^2}{k^2+r^2}.
```

After $k=i\kappa$,

```math
m_{+,2}(i\kappa)=-\kappa\frac{4r^2-\kappa^2}{r^2-\kappa^2}.
```

The **zero at $\kappa=2r$** is the even/Neumann bound state $E=-4r^2$; the **pole at $\kappa=r$** corresponds to the odd/Dirichlet bound state $E=-r^2$. These are exactly the two bound levels encoded by the double factors of the spectral polynomial in draft 130.

**Important qualification:** These formulas are rational in the *wave number $k$*, while the spectral parameter is $\lambda=k^2$. The square-root branch of $k$ matters for analytic continuation and the Herglotz property. One cannot treat the rational formula as a single-valued meromorphic function of all complex $\lambda$ without specifying its spectral sheet.

### 11.3 Back to the original rational x-coordinate

For a transformed solution $\psi(u)=xf(x)$, the boundary logarithmic derivatives obey

```math
\frac{cf_x(c)}{f(c)}=\frac{\psi_u(0)}{\psi(0)}-1=m_{+,n}(k)-1.
```

Thus the even sector's original weighted Robin condition $cf_x(c)+f(c)=0$ becomes $m_{+,n}=0$, whereas the odd sector's Dirichlet condition is a pole of the projective ratio. The resolution $r$ controls the rational spectral coefficients, while $c$ selects the multiplicative location of the boundary.

## 12. A genuinely unitary distorted Fourier transform [D,V,K]

By the polar-unitary theorem of §5, the continuous spectral basis can be obtained by sending free Fourier plane waves **back** through the adjoint polar isometry. Define generalized eigenfunctions for real $k$ by

```math
\chi_{n,k}(u)=\frac{Q_n^\dagger e^{iku}}{\sqrt{2\pi D_n(k^2)}},\qquad D_n(k^2)=\prod_{j=1}^n(k^2+j^2r^2).
```

They solve $h_n\chi_{n,k}=k^2\chi_{n,k}$ and have the correct delta normalization on the absolutely continuous subspace, in the generalized-eigenfunction sense. The associated spectral transform is

```math
(\mathscr F_n\psi)(k)=\int_{\mathbb R}\overline{\chi_{n,k}(u)}\psi(u)\,du.
```

Its inverse reconstructs only the continuous part:

```math
(P_{\rm ac}\psi)(u)=\int_{\mathbb R}\chi_{n,k}(u)(\mathscr F_n\psi)(k)\,dk.
```

**Theorem 12.1 [D,K] (continuous plus bound-state Plancherel).** For $\psi\in L^2(\mathbb R)$,

```math
\|\psi\|_2^2=\sum_{j=1}^n|\langle\varphi_{n,j},\psi\rangle|^2+\int_{\mathbb R}|(\mathscr F_n\psi)(k)|^2\,dk.
```

**Proof.** Apply the ordinary unitary Fourier transform to $\mathcal U_nP_{\rm ac}\psi$ and use the orthogonal decomposition in §5. The generalized integral formula is interpreted distributionally or initially on a dense scattering-test-function space before completion. Neither the continuum Jost wave nor a scattering amplitude belongs to the ordinary $L^2$ eigenfunction domain.

### 12.1 Exact normalized bound modes for n=1,2

The discrete subspaces are particularly elementary:

```math
\varphi_{1,1}(u)=\sqrt{\frac r2}\,S,\qquad h_1\varphi_{1,1}=-r^2\varphi_{1,1}.
```

```math
\varphi_{2,2}(u)=\sqrt{\frac{3r}{4}}\,S^2,\qquad h_2\varphi_{2,2}=-4r^2\varphi_{2,2}.
```

```math
\varphi_{2,1}(u)=\sqrt{\frac{3r}{2}}\,SW,\qquad h_2\varphi_{2,1}=-r^2\varphi_{2,1}.
```

Their norms follow from $\int S^2du=2/r$, $\int S^4du=4/(3r)$ and $\int S^2W^2du=2/(3r)$. Even/odd parity matches the half-line Riccati boundary data of §11. With the constant shift $r^2$, the original Master Hessian has eigenvalues $-3r^2$ and $0$ and essential threshold $r^2$.

## 13. Transport the ENTIRE distorted spectral resolution back to the original x [D,V]

Define the exact original-variable weighted Sturm–Liouville operator with a **chosen** reflectionless potential added:

```math
(\tau_{x,n}f)(x)=\frac1x\left[-(x^3f_x)_x+\big(r^2-1+V_n(\ln(x/c))\big)xf\right].
```

The transformation of §1 gives

```math
U_c\tau_{x,n}U_c^{-1}=h_n+r^2.
```

This equation defines a precise **new weighted SL realization** with the same original measure $x\,dx$ and all scale parameters. It is not the same expression as the original linear Master carrier when $n>0$; its extra potential is an explicitly selected pullback.

Define the continuum modes and discrete modes in the original variable:

```math
\chi^x_{n,k}(x)=\frac{\chi_{n,k}(\ln(x/c))}{x},\qquad \varphi^x_{n,j}(x)=\frac{\varphi_{n,j}(\ln(x/c))}{x}.
```

These satisfy

```math
\tau_{x,n}\chi^x_{n,k}=(r^2+k^2)\chi^x_{n,k},\qquad\tau_{x,n}\varphi^x_{n,j}=(r^2-j^2r^2)\varphi^x_{n,j}.
```

**Theorem 13.1 [D,V] (distorted multiplicative Plancherel).** With the domain transported by $U_c$, every $f\in L^2((0,\infty),x\,dx)$ has the exact norm decomposition

```math
\|f\|_{L^2(xdx)}^2=\sum_{j=1}^n\left|\int_0^\infty\overline{\varphi^x_{n,j}(x)}f(x)\,x\,dx\right|^2+\int_{\mathbb R}\left|\int_0^\infty\overline{\chi^x_{n,k}(x)}f(x)\,x\,dx\right|^2dk.
```

**Proof.** The map $f\mapsto xf$ is unitary. Apply Theorem 12.1 to $\psi=xf$. Each scalar product changes exactly by the weight $x\,dx$, including the factor $1/x$ in each normalized mode.

The free case $n=0$ reduces to the canonical *unitary Mellin–Fourier transform* of draft 130. For $n=1,2$, the ordinary Mellin kernel is replaced by a finite Darboux polynomial in $W=\tanh(r\ln(x/c))$ times the character $(x/c)^{ik}$; the discrete corrections are finitely many weighted bound-state coefficients.

**New synthesis:** This is a complete unitary **SL–Darboux–Fourier/Mellin spectral dictionary** on the original weighted Hilbert space, including the discrete defect that a naive statement of full free-unitarity would discard.

### 13.1 The scattering states are multiplicative generalized eigenfunctions

Because $e^{iku}=(x/c)^{ik}$, the continuum wave has the structure

```math
\chi^x_{n,k}(x)=\frac{(x/c)^{ik}}{x\sqrt{2\pi D_n(k^2)}}B_n\left(k,\tanh(r\ln(x/c))\right).
```

For $n=1$, $B_1=rW-ik$; for $n=2$, $B_2=r^2(3W^2-1)-k^2-3ikrW$. They are not square-integrable in $x\,dx$ at real scattering energies, just as Fourier characters are not in $L^2(du)$. The completeness assertion uses a generalized spectral transform, not a discrete countable eigenbasis.

## 14. The scattering spectrum does not determine a physical clock or Riemann period [C]

The real parameter $k$ is conjugate to the canonical logarithmic coordinate $u=\ln(x/c)$ in the **weighted spectral Hilbert space**. Its squared value $\lambda=k^2$ is the Schrödinger spectral energy relative to the unshifted $h_n$ operator. It is not the mechanical energy of the original nonlinear Duffing separatrix, not the Riemann family parameter $\lambda_R$ of draft 130, and not the oscillatory time frequency of a separately selected physical system.

The scattering phase $\delta_n(k)$ is obtained from a spatial Jost normalization, while the Milne–Gudermannian phase of the canonical half-rate carrier has $u$ as its **linear-carrier independent variable**. Their common Riccati amplitude–phase equations produce explicit pullbacks, not an automatic equality of their phase increments. Likewise the Lax–Novikov spectral curve is a singular spectral-operator curve, not the smooth elliptic Riemann minimal-example curve with marked height differential and immersion periods.

## 15. The actual catenoid Jacobi operator needs its own Hilbert metric [D,K,V]

On the complete canonical Euclidean catenoid let $\zeta=u+iv$, $v\sim v+2\pi/r$, and

```math
X(u,v)=\left(\frac{\cosh(ru)}r\cos(rv),\,\frac{\cosh(ru)}r\sin(rv),\,u\right),\qquad R=\cosh(ru)=S^{-1}.
```

Its induced metric and area element are

```math
g_C=R^2(du^2+dv^2),\qquad dA_C=R^2\,du\,dv.
```

The Gaussian curvature and squared second-fundamental-form norm are

```math
K_C=-r^2S^4,\qquad |A_C|^2=2r^2S^4.
```

With $\Delta_{g_C}=R^{-2}(\partial_u^2+\partial_v^2)$, choose the **negative** of the minimal-surface Jacobi differential expression

```math
B_C=-(\Delta_{g_C}+|A_C|^2).
```

On the normalized angular mode $e^{imrv}$, $m\in\mathbb Z$, it acts on a radial profile $h(u)$ as

```math
(B_mh)(u)=R^{-2}\left[-h_{uu}+(m^2r^2-2r^2S^2)h\right]=R^{-2}(h_1+m^2r^2)h.
```

**Critical qualification:** The expression $h_1+m^2r^2$ appears only **after multiplying the Jacobi equation by $R^2$**. That multiplication changes the natural measure and is not a unitary conjugation of $B_m$ on the surface's radial $L^2(R^2du)$ space.

## 16. An exact UNITARY catenoid Jacobi conjugation [D,V]

The radial Hilbert space for a normalized angular mode is

```math
\mathcal H_C^{(m)}=L^2(\mathbb R,R(u)^2du).
```

Multiplication by $R$ is the natural unitary map

```math
(U_Ch)(u)=R(u)h(u),\qquad U_C:\mathcal H_C^{(m)}\longrightarrow L^2(\mathbb R,du).
```

**Theorem 16.1 [D,V] (exact transformed catenoid operator).** On a common smooth core,

```math
U_CB_mU_C^{-1}=-\partial_u(S^2\partial_u)+(m^2-1)r^2S^2=:\widetilde B_m.
```

**Proof, step by step.** For $\psi=R h$ set $a=R_u/R=rW$. Then $h=\psi/R$ and

```math
h_{uu}=R^{-1}[\psi_{uu}-2a\psi_u+(a^2-a_u)\psi].
```

Substitute into $R B_m(\psi/R)$ and use $R^{-2}=S^2$, $a_u=r^2S^2$, and $W^2+S^2=1$:

```math
R B_m(\psi/R)=S^2[-\psi_{uu}+2rW\psi_u+(m^2-1)r^2\psi].
```

Because $(S^2)_u=-2rWS^2$, the first two terms are exactly $-\partial_u(S^2\partial_u\psi)$. This proves the stated **unitary** conjugation, independently verified by symbolic differentiation for $m=0,1,2$.

The transformed operator has *degenerate leading coefficient* $p(u)=S^2\to0$ at both infinite ends. It is a different Sturm–Liouville operator from $h_1+m^2r^2$ and the original free constant-potential carrier; no equality of their full spectra follows from their common zero-Jacobi equation.

### 16.1 A form-theoretic distinction between angular sectors

For compactly supported smooth $\psi$, the transformed quadratic form is

```math
\langle\psi,\widetilde B_m\psi\rangle=\int_{\mathbb R}S^2\left(|\psi_u|^2+(m^2-1)r^2|\psi|^2\right)du.
```

For $|m|\ge1$ this form is nonnegative. For $m=0$ there is an explicit negative direction: take a compactly supported cutoff $\psi_L$ equal to $1$ on $[-L,L]$, tapering only where $|u|$ is large. The derivative contribution is exponentially small as $L\to\infty$ because it is weighted by $S^2$; the negative potential contribution approaches $-r^2\int_{\mathbb R}S^2du=-2r$. Thus the complete geometric Jacobi problem has a negative quadratic direction in the rotationally symmetric sector, without any loss of self-adjointness.

This argument gives a **sector sign statement**, not a complete Morse-index theorem for arbitrary boundary or quotient geometries.

## 17. Darboux solutions produce actual catenoid Jacobi fields [D,V]

The zero-Jacobi equation in angular mode $m$ is

```math
(h_1+m^2r^2)h=0.
```

Two familiar exact $m=0$ solutions of $h_1h=0$ are

```math
h_{0,\mathrm{odd}}(u)=W,\qquad h_{0,\mathrm{even}}(u)=1-ruW.
```

Their parities and geometric interpretations match axial translation and scale/deformation Jacobi directions; direct differentiation checks both equations. In the $|m|=1$ angular sector,

```math
(h_1+r^2)S=0,
```

so $h(u,v)=S(u)e^{\pm irv}$ gives the complexified pair corresponding to real horizontal-translation Jacobi fields.

These are **formal global Jacobi solutions**, not automatically square-integrable eigenfunctions in the catenoid surface Hilbert space. In particular,

```math
\int_{\mathbb R}R^2S^2du=\int_{\mathbb R}du=\infty.
```

Thus the $m=1$ geometric Jacobi field $S$ is not in $L^2(C,dA_C)$, even though the **same scalar function** $S$ is a normalized bound state of $h_1$ in the *different* flat measure $du$. This is an exact, instructive counterexample to identifying two spectra from a common differential expression at spectral value zero.

The helicoid is locally Bonnet-associated to the catenoid and shares the local Jacobi expression, but its global angular coordinate is not periodically identified in the same way. The catenoid's normalized angular constant mode and the Fourier index lattice $m\in\mathbb Z$ cannot simply be transported to the helicoid's unwrapped angular line.

## 18. A direct metric diagram from original weighted L2 to the catenoid [D,V]

The canonical weighted Hilbert map of draft 130 is

```math
U_cf(u)=xf(x),\qquad x=ce^u,\qquad\|f\|_{L^2(xdx)}=\|U_cf\|_{L^2(du)}.
```

Compose with the inverse catenoid half-density map $U_C^{-1}$ and the normalized angular constant $h_0(v)=\sqrt{r/(2\pi)}$:

```math
(\mathcal I_{c,r}f)(u,v)=\sqrt{\frac{r}{2\pi}}\frac{x f(x)}{R(u)}.
```

It is an isometry into the angularly constant sector of $L^2(C,dA_C)$, but its **operator pullback** is explicitly

```math
\mathcal I_{c,r}^{-1}B_C\mathcal I_{c,r}\quad\stackrel{U_c}{\longleftrightarrow}\quad\widetilde B_0=-\partial_u(S^2\partial_u)-r^2S^2.
```

The original weighted free carrier instead corresponds to

```math
U_c\tau_xU_c^{-1}=-\partial_u^2+r^2.
```

Hence an exact Hilbert-space isometry does **not** intertwine these two naturally defined differential operators. The present calculation makes the obstruction explicit: one has a variable leading coefficient $S^2$ and a negative localized potential, the other a constant leading coefficient and positive constant potential.

There is nevertheless a **different** operator intertwiner available for the flat $h_1$ spectral problem, namely the Darboux polar-unitary map $\mathcal U_1$ of §5. The distinctions between *isometry of function spaces*, *equality of local zero equations*, and *unitary operator intertwining* are fully visible.

## 19. The original localized function: a bound state for n=1, mixed spectrum for n=2 [D,V]

Return to the original centered rational function, keeping $\mu,c$ explicit:

```math
f_\mu(x;r,c)=\frac{S}{2\sqrt\mu\,x},\qquad \psi_\mu(u)=U_cf_\mu=\frac{S}{2\sqrt\mu},\qquad\|\psi_\mu\|_2^2=\frac1{2r\mu}.
```

### 19.1 Order-one well: the full canonical norm is discrete

Since $h_1S=-r^2S$, the normalized ground mode is $\varphi_{1,1}=\sqrt{r/2}\,S$. Therefore

```math
\psi_\mu=\frac1{\sqrt{2r\mu}}\varphi_{1,1}.
```

Equivalently,

```math
h_1\psi_\mu=-r^2\psi_\mu,\qquad (h_1+r^2)\psi_\mu=0,\qquad Q_1\psi_\mu=0.
```

So the entire canonical weighted $L^2$ norm is concentrated in the **single discrete bound state** of this *chosen modified operator*. This does **not** make $\psi_\mu$ a zero eigenfunction of the original free carrier $-\partial_u^2+r^2$; the latter has no $L^2$ bound state.

### 19.2 Order-two well: exactly computable discrete/continuous splitting

For the Master Hessian well $h_2$, $\psi_\mu$ is even, so its projection on the odd bound state $\varphi_{2,1}\propto SW$ vanishes. Its overlap with the even bound state $\varphi_{2,2}=\sqrt{3r/4}\,S^2$ is

```math
\langle\varphi_{2,2},\psi_\mu\rangle=\frac{\sqrt{3r/4}}{2\sqrt\mu}\int_{\mathbb R}S^3du=\frac{\pi\sqrt3}{8\sqrt{r\mu}}.
```

The equality uses the exact integral $\int_{\mathbb R}S^3du=\pi/(2r)$. Therefore

```math
\|P_{\rm bound}^{(2)}\psi_\mu\|_2^2=\frac{3\pi^2}{64r\mu},\qquad \frac{\|P_{\rm bound}^{(2)}\psi_\mu\|_2^2}{\|\psi_\mu\|_2^2}=\frac{3\pi^2}{32}.
```

The **remaining fraction** $1-3\pi^2/32>0$ lies in the absolutely continuous subspace. This is an exact spectral statement for an explicitly chosen function and operator, not a generic claim that every nonlinear Master separatrix carries this spectral fraction.

### 19.3 The transformed continuous coefficient is elementary

The order-two Crum operator acts on the original profile as

```math
Q_2S=A_1A_2S=r^2S^3.
```

Using the known Fourier integral

```math
\int_{\mathbb R}e^{-iku}S^3du=\frac{\pi(k^2+r^2)}{2r^3}\,\mathrm{sech}\left(\frac{\pi k}{2r}\right),
```

the distorted Fourier transform of $\psi_\mu$ from §12 is

```math
(\mathscr F_2\psi_\mu)(k)=\frac{\pi}{4r\sqrt{2\pi\mu}}\sqrt{\frac{k^2+r^2}{k^2+4r^2}}\,\mathrm{sech}\left(\frac{\pi k}{2r}\right).
```

This formula was checked by applying the exact adjoint Crum operator and comparing normalizations; it is a genuine **Darboux-deformed multiplicative Fourier amplitude** of the original Symmetrical Function.

### 19.4 A definite integral follows from the discrete/continuous Plancherel split

Parseval gives

```math
\frac1{2r\mu}=\frac{3\pi^2}{64r\mu}+\int_{\mathbb R}|(\mathscr F_2\psi_\mu)(k)|^2dk.
```

Substituting the exact coefficient and simplifying yields the **parameter-dependent definite integral**

```math
\int_{-\infty}^{\infty}\frac{k^2+r^2}{k^2+4r^2}\,\mathrm{sech}^2\left(\frac{\pi k}{2r}\right)dk=\frac{r(32-3\pi^2)}{2\pi}.
```

The identity was independently numerically checked at $r=1/2,1,2$ with errors at floating-point roundoff. It can also be evaluated by contour or Fourier methods; the conceptual derivation here is **Plancherel plus the Darboux discrete kernel**.

**This is a particularly sharp example of the requested whole-system algebra:** the original rational profile, the weighted Hilbert metric, the rank-two scattering carrier, the Crum intertwiner, the Pinney/spectral closure and an exact transcendental integral all participate in one compatible calculation.
