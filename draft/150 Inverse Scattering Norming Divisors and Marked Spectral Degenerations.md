---
id: SF-DRAFT-150
title: Inverse Scattering, Norming Divisors, and Marked Spectral Degenerations
status: provisional
created: 2026-11-19
proposed_layers: [I, II, III]
depends_on: [SF-I-020, SF-DRAFT-080, SF-DRAFT-090, SF-DRAFT-100, SF-DRAFT-110, SF-DRAFT-120, SF-DRAFT-130, SF-DRAFT-140]
related_claims: [H95, H100, H122, H164, H169, H172, H177, H178, H179, H183, H299, H340, H391, H466]
---

# 150 Inverse Scattering, Norming Divisors, and Marked Spectral Degenerations

**Status:** Provisional independent mathematical investigation. Labels: [D] explicit proof/derivation; [V] exact symbolic check; [K] classical theorem used with stated hypotheses; [H] archival, retaining its prior verification status; [C] correction/non-equivalence; [O] open. No physical realization, novelty or global geometric isomorphism is inferred from matching expressions.

**Goal.** Extend the SL–EP/Gel'fand–Dikii–Darboux closures of drafts 130–140 to *inverse* spectral reconstruction. Determine exactly what recovers resolution $r$, center $c$, and integer well depth $n$; write the complete reflectionless Marchenko determinant; show how KdV moves norming/divisor coordinates without changing the spectral curve; and distinguish this nodal curve's generalized Jacobian from the marked periods of the Riemann minimal-example family. Continue to carry the original weighted $L^2$ and resolution-doubling maps.

**Source audit.** The current live GitHub draft 140 was reopened (Darboux spectral unitarity, Jost/Pinney strength, Weyl logarithmic derivatives, catenoid surface operator); draft 130 and historical ZIP modules including inverse-wronski-l3.md, binary-quartic-and-spectral-curves.md, period-hierarchy.md, marchenko-legendre.md, and the verified H100/H299 Lax–Novikov identities were consulted. External Marchenko/Gel'fand–Levitan inverse scattering, norming constants, and KdV references are distinguished in §22. This draft's new algebra is separately verified: a full binomial determinant identity at depths $1\le n\le6$ using exact rational arithmetic, and selected explicit trace and translation formulas.

## 1. Coordinate and parameter dictionary

Maintain $r,c,\mu,x>0$, and let the canonical logarithmic variable always be

```math
u=\ln(x/c),\qquad x=ce^u,\qquad S=\mathrm{sech}(ru),\qquad W=\tanh(ru),\qquad f_\mu(x;r,c)=\frac{S}{2\sqrt\mu\,x}.
```

Inverse scattering, however, requires a **fixed observation coordinate**. Fix an independent reference scale $c_{\rm ref}>0$ and define

```math
v=\ln(x/c_{\rm ref}),\qquad u=v-u_0,\qquad u_0=\ln(c/c_{\rm ref}),\qquad c=c_{\rm ref}e^{u_0}.
```

Here $r$ is the hyperbolic resolution, $\mu$ the nonlinear Master amplitude, $n\ge1$ the integer Pöschl–Teller well depth, $j=1,\ldots,n$ the discrete mode label, $\kappa_j=jr$ its *positive decay exponent*, $k>0$ a real continuum wave number, $\lambda=k^2$ an unshifted Schrödinger spectral energy, and $\tau$ a **separate KdV evolution parameter**. None of $j,k,\kappa_j,n,\tau$ means the original center $c$.

The centered reflectionless operator in $v$ is

```math
h_{n,r,u_0}=-\partial_v^2+V_{n,r,u_0}(v),\qquad V_{n,r,u_0}(v)=-n(n+1)r^2\mathrm{sech}^2(r(v-u_0)).
```

On $L^2(\mathbb R,dv)$ it has the natural self-adjoint $H^2$ realization. The original cubic Master Hessian is $h_{2,r,0}+r^2$ in its **canonical centered** $u$ coordinate; the catenoid angular mode involves $h_1$ only in a weighted, zero-equation sense (draft 140). These are different operator realizations even when the same profile occurs.

## 2. What the transmission coefficient can and cannot reconstruct [D,K,C]

For the integer reflectionless well, the Jost/Darboux construction in draft 140 gives the full-line transmission factor

```math
T_n(k)=\prod_{j=1}^n\frac{k+i\kappa_j}{k-i\kappa_j},\qquad R_{\rm refl}(k)=0,\qquad \kappa_j=jr.
```

Translation $v\mapsto v-u_0$ multiplies the right Jost solution by a compensating plane-wave phase when normalized at $v\to+\infty$, but it leaves $T_n(k)$ unchanged. Its poles (for the displayed convention) occur at $k=i\kappa_j$, and the discrete spectrum is

```math
E_j=-\kappa_j^2=-j^2r^2,\qquad j=1,\ldots,n.
```

**Theorem 2.1 [D,K] (spectral rigidity inside the centered integer family).** Within the declared family, the number of bound levels gives $n$ and their positive decay exponents are the *consecutive multiples* $r,2r,\ldots,nr$. Hence

```math
n=\#\sigma_{\rm disc}(h_n),\qquad r=\min_j\kappa_j.
```

The continuous transmission factor and bound energies do **not** recover $u_0$ or $c$. This is not failure of inverse scattering: the full reflectionless data include **positive bound-state norming constants**, and those change under translation.

**Counterexample [C].** Every $u_0\in\mathbb R$ produces a distinct translated potential on the fixed $v$ line, but the *same* meromorphic $T_n(k)$ and the *same* discrete spectrum. Therefore the assertion “the transmission phase identifies the original center $c$” is false unless an external origin/gauge or additional data are specified. If one instead builds the scattering coordinate as $u=\ln(x/c)$ using the **unknown** center, then $u_0$ has already been set to zero by the coordinate definition, so it cannot be independently reconstructed from that centered representation.

## 3. Exactly normalized bound eigenfunctions and their tails [D,V,K]

The integer Pöschl–Teller equation at $E_j=-j^2r^2$ reduces, under $z=\tanh[r(v-u_0)]$, to the associated Legendre equation. With the conventional Condon–Shortley phase, the normalized bound mode may be chosen as

```math
\varphi_{n,j}(v)=N_{n,j}P_n^j(\tanh(r(v-u_0))),\qquad N_{n,j}^2=\frac{rj(n-j)!}{(n+j)!}.
```

The normalization follows from $dv=dz/[r(1-z^2)]$ and the associated-Legendre integral

```math
\int_{-1}^1\frac{[P_n^j(z)]^2}{1-z^2}\,dz=\frac{(n+j)!}{j(n-j)!},\qquad 1\le j\le n.
```

For $v\to+\infty$, use $1-z^2=\mathrm{sech}^2[r(v-u_0)]\sim4e^{-2jr(v-u_0)/j}$ and

```math
\frac{d^j}{dz^j}P_n(1)=\frac{(n+j)!}{2^jj!(n-j)!},\qquad P_n^j(z)=(-1)^j(1-z^2)^{j/2}\frac{d^jP_n}{dz^j}.
```

Thus the **positive squared right asymptotic coefficient** (our explicitly fixed norming convention) is

```math
\varphi_{n,j}(v)\sim(-1)^j\alpha_{n,j}e^{-\kappa_j(v-u_0)},\qquad \alpha_{n,j}^2=\frac{rj(n+j)!}{(j!)^2(n-j)!}.
```

Equivalent factorial form:

```math
\alpha_{n,j}^2=r\frac{(n+j)!}{j!(j-1)!(n-j)!}=2jr\prod_{\substack{\ell=1\\\ell\ne j}}^n\left|\frac{j+\ell}{j-\ell}\right|.
```

**Important normalization:** $\alpha_{n,j}$ is the coefficient of the $L^2(dv)$-**normalized bound state** at the right end. Other authors use the reciprocal, its square, a left norming constant, or a residue of a Jost coefficient. A claimed translation law without fixing this convention is ambiguous.

### 3.1 Check at n=1 and n=2

The formulas give

```math
n=1:\quad \alpha_{1,1}^2=2r;\qquad n=2:\quad (\alpha_{2,1}^2,\alpha_{2,2}^2)=(6r,12r).
```

They agree with the exact bound modes of draft 140: $\sqrt{r/2}S$, $\sqrt{3r/2}SW$, and $\sqrt{3r/4}S^2$, respectively. In particular the general factorial theorem recovers both previously isolated cases, with **no change in the original scale $c$**, which enters via $u_0$ only.

## 4. Translation law and recovery of the multiplicative center [D,V]

Express each bound eigenfunction on the **fixed reference coordinate $v$**, so its right tail has the form $\beta_j e^{-\kappa_jv}$. From §3,

```math
\beta_j^2=\alpha_{n,j}^2e^{2\kappa_j u_0}=\alpha_{n,j}^2(c/c_{\rm ref})^{2jr}.
```

Therefore every bound mode separately reconstructs the same center:

```math
u_0=\frac1{2jr}\ln\left(\frac{\beta_j^2}{\alpha_{n,j}^2}\right),\qquad c=c_{\rm ref}\left(\frac{\beta_j^2}{\alpha_{n,j}^2}\right)^{1/(2jr)}.
```

**Theorem 4.1 [D,V] (norming consistency and center reconstruction).** Within the translated integer Pöschl–Teller family, the collection of right norming constants satisfies

```math
\left(\frac{\beta_j^2}{\alpha_{n,j}^2}\right)^{1/j}=\left(\frac{c}{c_{\rm ref}}\right)^{2r}\quad\text{for every}\quad j=1,\ldots,n.
```

Conversely these positive ratios and the spectral exponents recover a common real center $u_0$ by the displayed formula. Deviations of the ratios from a common power law are evidence that a generic reflectionless $n$-soliton potential is **not merely a translate of the symmetric Pöschl–Teller profile**.

**Qualification:** Recovering $c$ requires an externally fixed reference $c_{\rm ref}$ and a *labelled $x$-coordinate*. The abstract spectral operator in a translation-invariant $v$ line determines the center only up to the choice of the origin. Moreover the nonlinear amplitude parameter $\mu$ does not occur in $h_n$ and cannot be recovered from its scattering data: it requires the original normalized function or another independent amplitude datum.

## 5. The Marchenko determinant with every normalization visible [K,D]

For distinct $\kappa_j>0$ and right norming coefficients $\beta_j>0$, the finite reflectionless Marchenko/Kay–Moses matrix is

```math
C_{ij}(v)=\frac{\beta_i\beta_j}{\kappa_i+\kappa_j}e^{-(\kappa_i+\kappa_j)v},\qquad 1\le i,j\le n.
```

Define the tau determinant and recovered potential

```math
\tau_n(v)=\det(I_n+C(v)),\qquad V(v)=-2\partial_v^2\log\tau_n(v).
```

These formulas are classical inverse scattering for real reflectionless integrable potentials; specifying the *right norming coefficient convention* is necessary. The $C$ matrix is positive semidefinite for positive norming coefficients and distinct positive $\kappa_j$ (a Cauchy Gram matrix), so $\tau_n>0$ on the real line.

### 5.1 Explicit sum over subsets

Expand the determinant into principal minors. The Cauchy determinant formula yields

```math
\tau_n(v)=\sum_{I\subseteq\{1,\ldots,n\}}\left[\prod_{j\in I}\frac{\beta_j^2}{2\kappa_j}e^{-2\kappa_jv}\right]\left[\prod_{\substack{i<j\\i,j\in I}}\left(\frac{\kappa_j-\kappa_i}{\kappa_j+\kappa_i}\right)^2\right].
```

All coefficients are nonnegative, and the empty subset contributes $1$. This finite polynomial/exponential sum is an exact **linear-algebraic inverse map**, not a conjectural infinite series. Translation changes only the positive factors $\beta_j^2e^{-2\kappa_jv}$; the pairwise Cauchy interaction factors remain fixed.

For the canonical family choose $\kappa_j=jr$ and $\beta_j^2=\alpha_{n,j}^2e^{2jr u_0}$ from §4, with $u=v-u_0$.

## 6. Exact binomial Marchenko determinant for the entire integer ladder [D,V,K]

Set $\kappa_j=jr$, use the canonical centered norming constants from §3, put $u=v-u_0$, and write $z=e^{-2ru}$. The matrix of §5 is finite-dimensional but its determinant has degree

```math
N=\sum_{j=1}^n j=\frac{n(n+1)}2
```

in $z$, *not* degree $n$. Nevertheless it collapses to a single power.

**Theorem 6.1 [D,V,K] (exact binomial tau identity).**

```math
\det\left[\delta_{ij}+\frac{\alpha_{n,i}\alpha_{n,j}}{(i+j)r}e^{-(i+j)ru}\right]_{i,j=1}^n=(1+e^{-2ru})^{n(n+1)/2}.
```

The recovered potential is consequently

```math
-2\partial_u^2\log\tau_n(u)=-n(n+1)r^2\mathrm{sech}^2(ru)=V_n(u).
```

**Mathematical proof with declared classical input.** The associated-Legendre modes in §3 determine *all* the negative eigenvalues and the right norming constants of the explicitly reflectionless integer Pöschl–Teller operator. Reflectionlessness follows from the Darboux chain of draft 140. The standard uniqueness theorem for the finite real reflectionless Marchenko inverse problem therefore says that its determinant reconstructs exactly this $V_n$. Independently,

```math
-2\partial_u^2\log(1+e^{-2ru})^N=-2Nr^2\mathrm{sech}^2(ru)=-n(n+1)r^2S^2.
```

Two tau functions producing the same potential can differ by $e^{au+b}$. Both approach $1$ as $u\to+\infty$, forcing $a=b=0$; hence the determinant is the displayed binomial. The proof thus depends on the **stated classical Marchenko uniqueness theorem**, not an unproved inference from matching a few coefficients.

**Independent symbolic certificate [V].** Expanding the Cauchy principal-minor formula of §5 in exact rational arithmetic, with the factorial constants of §3, gives zero polynomial residual for **every** integer depth $1\le n\le6$ (degree $1,3,6,10,15,21$ respectively). This check is supplementary to the theorem, not its proof for all $n$.

### 6.1 Fully explicit low-depth cases

At depth one,

```math
\kappa_1=r,\quad\alpha_{1,1}^2=2r,\quad\tau_1=1+z,\quad V_1=-2r^2S^2.
```

At depth two,

```math
(\kappa_1,\kappa_2)=(r,2r),\quad(\alpha_{2,1}^2,\alpha_{2,2}^2)=(6r,12r).
```

The $2\times2$ Cauchy determinant is

```math
\tau_2=1+3z+3z^2+z^3=(1+z)^3,\quad V_2=-6r^2S^2.
```

At depth three, the coefficient sequence becomes

```math
(\alpha_{3,1}^2,\alpha_{3,2}^2,\alpha_{3,3}^2)=(12r,60r,60r),\quad\tau_3=(1+z)^6.
```

The $n=3$ determinant is **degree six** despite the $3\times3$ matrix. The powers of $z$ come from sums of distinct decay exponents. This is a concrete algebraic realization of the framework's level/recursion web.

## 7. The ratio of norming constants is a spectral test of a centered PT slice [D,V]

With $\beta_j^2$ defined relative to the reference coordinate $v$, write

```math
\rho_j=\left(\frac{\beta_j^2}{\alpha_{n,j}^2}\right)^{1/j}.
```

For an exactly translated centered Pöschl–Teller well, §4 proves

```math
\rho_1=\rho_2=\cdots=\rho_n=e^{2ru_0}=(c/c_{\rm ref})^{2r}.
```

Conversely, among reflectionless potentials with exactly the integer spectrum $\{-j^2r^2\}$ and positive right norming constants, this condition is **sufficient** to reconstruct the translated integer PT profile by the uniqueness of the Marchenko problem and Theorem 6.1.

**Theorem 7.1 [D,K] (inverse-spectral characterization).** A real reflectionless $n$-bound-state potential with $\kappa_j=jr$ belongs to the one-translation-parameter family $V_{n,r,u_0}$ if and only if its positive right norming constants obey the displayed common-ratio condition.

This gives a strict test for whether an arbitrary reflectionless $n$-soliton potential lies on the *special PT slice* of its full $n$-parameter isospectral manifold. For $n=1$, all positive norming data can be absorbed into a translation; for $n\ge2$, $(n-1)$ independent ratio constraints are nontrivial.

## 8. KdV flow proves that the n≥2 PT slice is not stationary under the first flow [D,K]

Use the same KdV sign convention as draft 130:

```math
V_\tau=6VV_v-V_{vvv},\qquad L(\tau)=-\partial_v^2+V(v,\tau).
```

For rapidly decaying real reflectionless data, the bound exponents $\kappa_j$ and the transmission coefficient remain fixed, while the **right squared norming coefficients** evolve as

```math
\beta_j^2(\tau)=\beta_j^2(0)e^{8\kappa_j^3\tau}.
```

This is the standard inverse-scattering/KdV time law in the explicit right-tail convention of §3. Substitution into the Marchenko matrix yields the finite-dimensional tau evolution

```math
C_{ij}(v,\tau)=\frac{\beta_i(0)\beta_j(0)}{\kappa_i+\kappa_j}e^{-(\kappa_i+\kappa_j)v+4(\kappa_i^3+\kappa_j^3)\tau}.
```

```math
V(v,\tau)=-2\partial_v^2\log\det(I_n+C(v,\tau)).
```

### 8.1 One bound level is a pure translation

For $n=1$, $\kappa_1=r$ and $\beta_1^2(0)=2r\,e^{2ru_0}$. Then

```math
\tau_1(v,\tau)=1+e^{-2r(v-u_0-4r^2\tau)}
```

and

```math
V_1(v,\tau)=-2r^2\mathrm{sech}^2[r(v-u_0-4r^2\tau)].
```

Thus the $n=1$ first KdV flow translates the centered well at speed $4r^2$ and exactly preserves its functional shape.

### 8.2 Two or more levels separate their norming phases

For $n\ge2$, starting from the centered PT data,

```math
\left(\frac{\beta_j^2(\tau)}{\alpha_{n,j}^2}\right)^{1/j}=e^{2ru_0+8j^2r^3\tau}.
```

This depends on $j$ as soon as $\tau\ne0$. Hence the centered PT norming-ratio condition of §7 is broken at every nonzero first-KdV time:

**Theorem 8.1 [D].** For $n\ge2$, the standard first KdV flow leaving the eigenvalues $\{-j^2r^2\}$ fixed generally moves the potential **off the translated PT family**, although it stays reflectionless and in the finite-dimensional $n$-soliton isospectral class.

This is an exact example of a finite spectral closure with **nontrivial divisor motion**. It also explains why the higher integer PT potential is not simply a one-soliton travelling solution of the first KdV equation.

## 9. Two spectral trace invariants reconstruct the resolution r [D,V,K]

The centered PT potential is negative and rapidly decaying. Direct integration yields

```math
I_1:=\int_{\mathbb R}V_n(v)\,dv=-2n(n+1)r=-4\sum_{j=1}^n\kappa_j.
```

Similarly,

```math
I_2:=\int_{\mathbb R}V_n(v)^2\,dv=\frac43n^2(n+1)^2r^3=\frac{16}{3}\sum_{j=1}^n\kappa_j^3.
```

**Proof.** Use $\int S^2du=2/r$, $\int S^4du=4/(3r)$ and $\sum_{j=1}^n j=n(n+1)/2$, $\sum_{j=1}^n j^3=[n(n+1)/2]^2$. The equalities on the right are the familiar reflectionless trace identities, verified here in the special integer family.

**Theorem 9.1 [D,V] (resolution from two integrals).** For the PT family, the resolution is exactly

```math
r=\frac{3I_2}{I_1^2},\qquad n(n+1)=-\frac{I_1}{2r}=-\frac{I_1^3}{6I_2}.
```

Both integrals are invariant under the first decaying KdV flow. Indeed,

```math
\frac{dI_1}{d\tau}=0,\qquad \frac{dI_2}{d\tau}=2\int V(6VV_v-V_{vvv})dv=0
```

by integration by parts and decay. Consequently the scalar combination $3I_2/I_1^2$ stays equal to the original $r$ **through the entire KdV deformation**, even when the profile ceases to be a translated PT well. It becomes a preserved spectral **resolution proxy**, not a theorem that every later profile still has precisely the single-well shape $\mathrm{sech}^2(rv)$.

**Correction of potential overreach:** These two moments do not determine the translation center, the full function, or a general scattering reflection coefficient. They recover $r$ and $n$ only **within the stated reflectionless integer-spectrum/PT-origin class**.

## 10. A second inverse route: the potential's logarithmic barycenter [D,V]

For the translated symmetric potential $V_{n,r,u_0}$, the first logarithmic moment is

```math
I_{1,v}:=\int_{\mathbb R}vV_{n,r,u_0}(v)\,dv=u_0 I_1.
```

Hence on a **fixed reference coordinate** $v=\ln(x/c_{\rm ref})$,

```math
u_0=\frac{\int vV(v)\,dv}{\int V(v)\,dv},\qquad c=c_{\rm ref}\exp\left(\frac{\int vV(v)\,dv}{\int V(v)\,dv}\right).
```

This agrees exactly with the norming-constant center of §4. Under KdV, the moment obeys

```math
\frac{d}{d\tau}\int_{\mathbb R}vV(v,\tau)\,dv=-3I_2.
```

**Proof.** Integrate $v(6VV_v-V_{vvv})$ by parts. The cubic derivative contributes zero; $\int vVV_v=-\frac12\int V^2$, giving $-3I_2$.

Thus the potential's weighted barycenter moves at the exact constant velocity

```math
\frac{d}{d\tau}\frac{\int vV\,dv}{\int V\,dv}=-\frac{3I_2}{I_1}=2n(n+1)r^2
```

for a KdV flow originating from the integer PT data. For $n=1$ this equals the individual soliton speed $4r^2$; for $n\ge2$ it is a **moment centroid speed**, not the speed of a single translated PT profile. This gives an independent exact check of the norming/divisor dynamics.
