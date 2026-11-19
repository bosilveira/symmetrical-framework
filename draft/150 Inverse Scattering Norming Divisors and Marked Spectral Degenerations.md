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

**Goal.** Extend the SL–EP/Gel'fand–Dikii–Darboux closures of drafts 130–140 to *inverse* spectral reconstruction. Determine exactly what recovers resolution $`r`$, center $`c`$, and integer well depth $`n`$; write the complete reflectionless Marchenko determinant; show how KdV moves norming/divisor coordinates without changing the spectral curve; and distinguish this nodal curve's generalized Jacobian from the marked periods of the Riemann minimal-example family. Continue to carry the original weighted $`L^2`$ and resolution-doubling maps.

**Source audit.** The current live GitHub draft 140 was reopened (Darboux spectral unitarity, Jost/Pinney strength, Weyl logarithmic derivatives, catenoid surface operator); draft 130 and historical ZIP modules including inverse-wronski-l3.md, binary-quartic-and-spectral-curves.md, period-hierarchy.md, marchenko-legendre.md, and the verified H100/H299 Lax–Novikov identities were consulted. External Marchenko/Gel'fand–Levitan inverse scattering, norming constants, and KdV references are distinguished in §22. This draft's new algebra is separately verified: a full binomial determinant identity at depths $`1\le n\le6`$ using exact rational arithmetic, and selected explicit trace and translation formulas.

## 1. Coordinate and parameter dictionary

Maintain $`r,c,\mu,x>0`$, and let the canonical logarithmic variable always be

```math
u=\ln(x/c),\qquad x=ce^u,\qquad S=\mathrm{sech}(ru),\qquad W=\tanh(ru),\qquad f_\mu(x;r,c)=\frac{S}{2\sqrt\mu\,x}.
```

Inverse scattering, however, requires a **fixed observation coordinate**. Fix an independent reference scale $`c_{\rm ref}>0`$ and define

```math
v=\ln(x/c_{\rm ref}),\qquad u=v-u_0,\qquad u_0=\ln(c/c_{\rm ref}),\qquad c=c_{\rm ref}e^{u_0}.
```

Here $`r`$ is the hyperbolic resolution, $`\mu`$ the nonlinear Master amplitude, $`n\ge1`$ the integer Pöschl–Teller well depth, $`j=1,\ldots,n`$ the discrete mode label, $`\kappa_j=jr`$ its *positive decay exponent*, $`k>0`$ a real continuum wave number, $`\lambda=k^2`$ an unshifted Schrödinger spectral energy, and $`\tau`$ a **separate KdV evolution parameter**. None of $`j,k,\kappa_j,n,\tau`$ means the original center $`c`$.

The centered reflectionless operator in $`v`$ is

```math
h_{n,r,u_0}=-\partial_v^2+V_{n,r,u_0}(v),\qquad V_{n,r,u_0}(v)=-n(n+1)r^2\mathrm{sech}^2(r(v-u_0)).
```

On $`L^2(\mathbb R,dv)`$ it has the natural self-adjoint $`H^2`$ realization. The original cubic Master Hessian is $`h_{2,r,0}+r^2`$ in its **canonical centered** $`u`$ coordinate; the catenoid angular mode involves $`h_1`$ only in a weighted, zero-equation sense (draft 140). These are different operator realizations even when the same profile occurs.

## 2. What the transmission coefficient can and cannot reconstruct [D,K,C]

For the integer reflectionless well, the Jost/Darboux construction in draft 140 gives the full-line transmission factor

```math
T_n(k)=\prod_{j=1}^n\frac{k+i\kappa_j}{k-i\kappa_j},\qquad R_{\rm refl}(k)=0,\qquad \kappa_j=jr.
```

Translation $`v\mapsto v-u_0`$ multiplies the right Jost solution by a compensating plane-wave phase when normalized at $`v\to+\infty`$, but it leaves $`T_n(k)`$ unchanged. Its poles (for the displayed convention) occur at $`k=i\kappa_j`$, and the discrete spectrum is

```math
E_j=-\kappa_j^2=-j^2r^2,\qquad j=1,\ldots,n.
```

**Theorem 2.1 [D,K] (spectral rigidity inside the centered integer family).** Within the declared family, the number of bound levels gives $`n`$ and their positive decay exponents are the *consecutive multiples* $`r,2r,\ldots,nr`$. Hence

```math
n=\#\sigma_{\rm disc}(h_n),\qquad r=\min_j\kappa_j.
```

The continuous transmission factor and bound energies do **not** recover $`u_0`$ or $`c`$. This is not failure of inverse scattering: the full reflectionless data include **positive bound-state norming constants**, and those change under translation.

**Counterexample [C].** Every $`u_0\in\mathbb R`$ produces a distinct translated potential on the fixed $`v`$ line, but the *same* meromorphic $`T_n(k)`$ and the *same* discrete spectrum. Therefore the assertion “the transmission phase identifies the original center $`c`$” is false unless an external origin/gauge or additional data are specified. If one instead builds the scattering coordinate as $`u=\ln(x/c)`$ using the **unknown** center, then $`u_0`$ has already been set to zero by the coordinate definition, so it cannot be independently reconstructed from that centered representation.

## 3. Exactly normalized bound eigenfunctions and their tails [D,V,K]

The integer Pöschl–Teller equation at $`E_j=-j^2r^2`$ reduces, under $`z=\tanh[r(v-u_0)]`$, to the associated Legendre equation. With the conventional Condon–Shortley phase, the normalized bound mode may be chosen as

```math
\varphi_{n,j}(v)=N_{n,j}P_n^j(\tanh(r(v-u_0))),\qquad N_{n,j}^2=\frac{rj(n-j)!}{(n+j)!}.
```

The normalization follows from $`dv=dz/[r(1-z^2)]`$ and the associated-Legendre integral

```math
\int_{-1}^1\frac{[P_n^j(z)]^2}{1-z^2}\,dz=\frac{(n+j)!}{j(n-j)!},\qquad 1\le j\le n.
```

For $`v\to+\infty`$, use $`1-z^2=\mathrm{sech}^2[r(v-u_0)]\sim4e^{-2r(v-u_0)}`$ and

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

**Important normalization:** $`\alpha_{n,j}`$ is the coefficient of the $`L^2(dv)`$-**normalized bound state** at the right end. Other authors use the reciprocal, its square, a left norming constant, or a residue of a Jost coefficient. A claimed translation law without fixing this convention is ambiguous.

### 3.1 Check at n=1 and n=2

The formulas give

```math
n=1:\quad \alpha_{1,1}^2=2r;\qquad n=2:\quad (\alpha_{2,1}^2,\alpha_{2,2}^2)=(6r,12r).
```

They agree with the exact bound modes of draft 140: $`\sqrt{r/2}S`$, $`\sqrt{3r/2}SW`$, and $`\sqrt{3r/4}S^2`$, respectively. In particular the general factorial theorem recovers both previously isolated cases, with **no change in the original scale $`c`$**, which enters via $`u_0`$ only.

## 4. Translation law and recovery of the multiplicative center [D,V]

Express each bound eigenfunction on the **fixed reference coordinate $`v`$**, so its right tail has the form $`\beta_j e^{-\kappa_jv}`$. From §3,

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

Conversely these positive ratios and the spectral exponents recover a common real center $`u_0`$ by the displayed formula. Deviations of the ratios from a common power law are evidence that a generic reflectionless $`n`$-soliton potential is **not merely a translate of the symmetric Pöschl–Teller profile**.

**Qualification:** Recovering $`c`$ requires an externally fixed reference $`c_{\rm ref}`$ and a *labelled $`x`$-coordinate*. The abstract spectral operator in a translation-invariant $`v`$ line determines the center only up to the choice of the origin. Moreover the nonlinear amplitude parameter $`\mu`$ does not occur in $`h_n`$ and cannot be recovered from its scattering data: it requires the original normalized function or another independent amplitude datum.

## 5. The Marchenko determinant with every normalization visible [K,D]

For distinct $`\kappa_j>0`$ and right norming coefficients $`\beta_j>0`$, the finite reflectionless Marchenko/Kay–Moses matrix is

```math
C_{ij}(v)=\frac{\beta_i\beta_j}{\kappa_i+\kappa_j}e^{-(\kappa_i+\kappa_j)v},\qquad 1\le i,j\le n.
```

Define the tau determinant and recovered potential

```math
\tau_n(v)=\det(I_n+C(v)),\qquad V(v)=-2\partial_v^2\log\tau_n(v).
```

These formulas are classical inverse scattering for real reflectionless integrable potentials; specifying the *right norming coefficient convention* is necessary. The $`C`$ matrix is positive semidefinite for positive norming coefficients and distinct positive $`\kappa_j`$ (a Cauchy Gram matrix), so $`\tau_n>0`$ on the real line.

### 5.1 Explicit sum over subsets

Expand the determinant into principal minors. The Cauchy determinant formula yields

```math
\tau_n(v)=\sum_{I\subseteq\{1,\ldots,n\}}\left[\prod_{j\in I}\frac{\beta_j^2}{2\kappa_j}e^{-2\kappa_jv}\right]\left[\prod_{\substack{i<j\\i,j\in I}}\left(\frac{\kappa_j-\kappa_i}{\kappa_j+\kappa_i}\right)^2\right].
```

All coefficients are nonnegative, and the empty subset contributes $`1`$. This finite polynomial/exponential sum is an exact **linear-algebraic inverse map**, not a conjectural infinite series. Translation changes only the positive factors $`\beta_j^2e^{-2\kappa_jv}`$; the pairwise Cauchy interaction factors remain fixed.

For the canonical family choose $`\kappa_j=jr`$ and $`\beta_j^2=\alpha_{n,j}^2e^{2jr u_0}`$ from §4, with $`u=v-u_0`$.

## 6. Exact binomial Marchenko determinant for the entire integer ladder [D,V,K]

Set $`\kappa_j=jr`$, use the canonical centered norming constants from §3, put $`u=v-u_0`$, and write $`z=e^{-2ru}`$. The matrix of §5 is finite-dimensional but its determinant has degree

```math
N=\sum_{j=1}^n j=\frac{n(n+1)}2
```

in $`z`$, *not* degree $`n`$. Nevertheless it collapses to a single power.

**Theorem 6.1 [D,V,K] (exact binomial tau identity).**

```math
\det\left[\delta_{ij}+\frac{\alpha_{n,i}\alpha_{n,j}}{(i+j)r}e^{-(i+j)ru}\right]_{i,j=1}^n=(1+e^{-2ru})^{n(n+1)/2}.
```

The recovered potential is consequently

```math
-2\partial_u^2\log\tau_n(u)=-n(n+1)r^2\mathrm{sech}^2(ru)=V_n(u).
```

**Mathematical proof with declared classical input.** The associated-Legendre modes in §3 determine *all* the negative eigenvalues and the right norming constants of the explicitly reflectionless integer Pöschl–Teller operator. Reflectionlessness follows from the Darboux chain of draft 140. The standard uniqueness theorem for the finite real reflectionless Marchenko inverse problem therefore says that its determinant reconstructs exactly this $`V_n`$. Independently,

```math
-2\partial_u^2\log(1+e^{-2ru})^N=-2Nr^2\mathrm{sech}^2(ru)=-n(n+1)r^2S^2.
```

Two tau functions producing the same potential can differ by $`e^{au+b}`$. Both approach $`1`$ as $`u\to+\infty`$, forcing $`a=b=0`$; hence the determinant is the displayed binomial. The proof thus depends on the **stated classical Marchenko uniqueness theorem**, not an unproved inference from matching a few coefficients.

**Independent symbolic certificate [V].** Expanding the Cauchy principal-minor formula of §5 in exact rational arithmetic, with the factorial constants of §3, gives zero polynomial residual for **every** integer depth $`1\le n\le6`$ (degree $`1,3,6,10,15,21`$ respectively). This check is supplementary to the theorem, not its proof for all $`n`$.

### 6.1 Fully explicit low-depth cases

At depth one,

```math
\kappa_1=r,\quad\alpha_{1,1}^2=2r,\quad\tau_1=1+z,\quad V_1=-2r^2S^2.
```

At depth two,

```math
(\kappa_1,\kappa_2)=(r,2r),\quad(\alpha_{2,1}^2,\alpha_{2,2}^2)=(6r,12r).
```

The $`2\times2`$ Cauchy determinant is

```math
\tau_2=1+3z+3z^2+z^3=(1+z)^3,\quad V_2=-6r^2S^2.
```

At depth three, the coefficient sequence becomes

```math
(\alpha_{3,1}^2,\alpha_{3,2}^2,\alpha_{3,3}^2)=(12r,60r,60r),\quad\tau_3=(1+z)^6.
```

The $`n=3`$ determinant is **degree six** despite the $`3\times3`$ matrix. The powers of $`z`$ come from sums of distinct decay exponents. This is a concrete algebraic realization of the framework's level/recursion web.

## 7. The ratio of norming constants is a spectral test of a centered PT slice [D,V]

With $`\beta_j^2`$ defined relative to the reference coordinate $`v`$, write

```math
\rho_j=\left(\frac{\beta_j^2}{\alpha_{n,j}^2}\right)^{1/j}.
```

For an exactly translated centered Pöschl–Teller well, §4 proves

```math
\rho_1=\rho_2=\cdots=\rho_n=e^{2ru_0}=(c/c_{\rm ref})^{2r}.
```

Conversely, among reflectionless potentials with exactly the integer spectrum $`\{-j^2r^2\}`$ and positive right norming constants, this condition is **sufficient** to reconstruct the translated integer PT profile by the uniqueness of the Marchenko problem and Theorem 6.1.

**Theorem 7.1 [D,K] (inverse-spectral characterization).** A real reflectionless $`n`$-bound-state potential with $`\kappa_j=jr`$ belongs to the one-translation-parameter family $`V_{n,r,u_0}`$ if and only if its positive right norming constants obey the displayed common-ratio condition.

This gives a strict test for whether an arbitrary reflectionless $`n`$-soliton potential lies on the *special PT slice* of its full $`n`$-parameter isospectral manifold. For $`n=1`$, all positive norming data can be absorbed into a translation; for $`n\ge2`$, $`(n-1)`$ independent ratio constraints are nontrivial.

## 8. KdV flow proves that the n≥2 PT slice is not stationary under the first flow [D,K]

Use the same KdV sign convention as draft 130:

```math
V_\tau=6VV_v-V_{vvv},\qquad L(\tau)=-\partial_v^2+V(v,\tau).
```

For rapidly decaying real reflectionless data, the bound exponents $`\kappa_j`$ and the transmission coefficient remain fixed, while the **right squared norming coefficients** evolve as

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

For $`n=1`$, $`\kappa_1=r`$ and $`\beta_1^2(0)=2r\,e^{2ru_0}`$. Then

```math
\tau_1(v,\tau)=1+e^{-2r(v-u_0-4r^2\tau)}
```

and

```math
V_1(v,\tau)=-2r^2\mathrm{sech}^2[r(v-u_0-4r^2\tau)].
```

Thus the $`n=1`$ first KdV flow translates the centered well at speed $`4r^2`$ and exactly preserves its functional shape.

### 8.2 Two or more levels separate their norming phases

For $`n\ge2`$, starting from the centered PT data,

```math
\left(\frac{\beta_j^2(\tau)}{\alpha_{n,j}^2}\right)^{1/j}=e^{2ru_0+8j^2r^3\tau}.
```

This depends on $`j`$ as soon as $`\tau\ne0`$. Hence the centered PT norming-ratio condition of §7 is broken at every nonzero first-KdV time:

**Theorem 8.1 [D].** For $`n\ge2`$, the standard first KdV flow leaving the eigenvalues $`\{-j^2r^2\}`$ fixed generally moves the potential **off the translated PT family**, although it stays reflectionless and in the finite-dimensional $`n`$-soliton isospectral class.

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

**Proof.** Use $`\int S^2du=2/r`$, $`\int S^4du=4/(3r)`$ and $`\sum_{j=1}^n j=n(n+1)/2`$, $`\sum_{j=1}^n j^3=[n(n+1)/2]^2`$. The equalities on the right are the familiar reflectionless trace identities, verified here in the special integer family.

**Theorem 9.1 [D,V] (resolution from two integrals).** For the PT family, the resolution is exactly

```math
r=\frac{3I_2}{I_1^2},\qquad n(n+1)=-\frac{I_1}{2r}=-\frac{I_1^3}{6I_2}.
```

Both integrals are invariant under the first decaying KdV flow. Indeed,

```math
\frac{dI_1}{d\tau}=0,\qquad \frac{dI_2}{d\tau}=2\int V(6VV_v-V_{vvv})dv=0
```

by integration by parts and decay. Consequently the scalar combination $`3I_2/I_1^2`$ stays equal to the original $`r`$ **through the entire KdV deformation**, even when the profile ceases to be a translated PT well. It becomes a preserved spectral **resolution proxy**, not a theorem that every later profile still has precisely the single-well shape $`\mathrm{sech}^2(rv)`$.

**Correction of potential overreach:** These two moments do not determine the translation center, the full function, or a general scattering reflection coefficient. They recover $`r`$ and $`n`$ only **within the stated reflectionless integer-spectrum/PT-origin class**.

## 10. A second inverse route: the potential's logarithmic barycenter [D,V]

For the translated symmetric potential $`V_{n,r,u_0}`$, the first logarithmic moment is

```math
I_{1,v}:=\int_{\mathbb R}vV_{n,r,u_0}(v)\,dv=u_0 I_1.
```

Hence on a **fixed reference coordinate** $`v=\ln(x/c_{\rm ref})`$,

```math
u_0=\frac{\int vV(v)\,dv}{\int V(v)\,dv},\qquad c=c_{\rm ref}\exp\left(\frac{\int vV(v)\,dv}{\int V(v)\,dv}\right).
```

This agrees exactly with the norming-constant center of §4. Under KdV, the moment obeys

```math
\frac{d}{d\tau}\int_{\mathbb R}vV(v,\tau)\,dv=-3I_2.
```

**Proof.** Integrate $`v(6VV_v-V_{vvv})`$ by parts. The cubic derivative contributes zero; $`\int vVV_v=-\frac12\int V^2`$, giving $`-3I_2`$.

Thus the potential's weighted barycenter moves at the exact constant velocity

```math
\frac{d}{d\tau}\frac{\int vV\,dv}{\int V\,dv}=-\frac{3I_2}{I_1}=2n(n+1)r^2
```

for a KdV flow originating from the integer PT data. For $`n=1`$ this equals the individual soliton speed $`4r^2`$; for $`n\ge2`$ it is a **moment centroid speed**, not the speed of a single translated PT profile. This gives an independent exact check of the norming/divisor dynamics.

## 11. The original weighted L2 norm completes a three-parameter reconstruction [D,V]

The spectral potential does **not** contain the original Master amplitude $`\mu`$. The original function does:

```math
f_\mu(x;r,c)=\frac{\mathrm{sech}(r\ln(x/c))}{2\sqrt\mu\,x}.
```

Its natural Sturm–Liouville weighted norm, already verified in drafts 120–140, is

```math
\mathcal N:=\int_0^\infty x|f_\mu(x;r,c)|^2dx=\frac{1}{2r\mu}.
```

Therefore

```math
\mu=\frac{1}{2r\mathcal N}.
```

Fix the reference scale $`c_{\rm ref}`$ as in §1. The same positive weighted density reconstructs the logarithmic center through its first moment:

```math
\frac{\int_0^\infty x|f_\mu|^2\ln(x/c_{\rm ref})dx}{\int_0^\infty x|f_\mu|^2dx}=\ln(c/c_{\rm ref})=u_0.
```

**Proof.** Set $`v=\ln(x/c_{\rm ref})`$, $`u=v-u_0`$. The measure $`x|f_\mu|^2dx=(4\mu)^{-1}\mathrm{sech}^2(ru)du`$ is even about $`u=0`$ and has finite first moment. Its mean in the coordinate $`v`$ is $`u_0`$.

### 11.1 Three independently meaningful reconstructions

Within this **explicit** family, with a fixed reference $`x`$-coordinate, the same center is recovered by

```math
u_0=\frac{\int vV(v)dv}{\int V(v)dv}=\frac{\int_0^\infty x|f_\mu|^2\ln(x/c_{\rm ref})dx}{\int_0^\infty x|f_\mu|^2dx}=\frac{1}{2jr}\ln\frac{\beta_j^2}{\alpha_{n,j}^2}.
```

These are respectively the potential's logarithmic barycenter, the canonical weighted-Hilbert barycenter, and the right bound-state norming datum. Their equality follows because all three have been evaluated for the **same centered potential/profile pair** in the same fixed coordinate; it is not a generic identity for unrelated Sturm–Liouville functions or arbitrary scattering potentials.

**Reconstruction theorem [D].** Given the integer-spectrum reflectionless potential *together with* its right norming constants and an original normalized canonical function $`f_\mu`$ in the fixed $`x`$-coordinate, the triple $`(r,c,\mu)`$ is recoverable: $`r`$ from eigenvalue spacings (or the trace formula within the class), $`c`$ from a norming/moment center plus $`c_{\rm ref}`$, and $`\mu`$ from the weighted norm.

A translation-free spectral curve alone lacks the marked coordinate needed for $`c`$; and no spectral datum of $`h_n`$ alone fixes the independent amplitude $`\mu`$.

## 12. Direct reconstruction in the original rational x coordinate [D,V]

For the matched center and resolution,

```math
z=(x/c)^{-2r}=(c/x)^{2r},\qquad \tau_n(x)=(1+z)^{n(n+1)/2}.
```

The log-coordinate derivative becomes the dilation operator

```math
\partial_v=x\partial_x,\qquad V_n(x)=-2(x\partial_x)^2\log\tau_n(x).
```

Therefore

```math
V_n(x)=-4n(n+1)r^2\frac{c^{2r}x^{2r}}{(x^{2r}+c^{2r})^2}.
```

This is rational in $`x`$ whenever $`r`$ is a positive integer, and rational in the monomial $`x^r`$ for arbitrary positive real $`r`$.

The exact weighted spectral operator in the original coordinate, as defined in draft 140, is

```math
\tau_{x,n}f=\frac1x[-(x^3f_x)_x+(r^2-1+V_n(\ln(x/c)))xf],\qquad U_c\tau_{x,n}U_c^{-1}=h_n+r^2.
```

The potential's position-dependent term is **added data** to the original linear Master expression. No change of the original Master equation is silently assumed. The $`x=c`$ point is the reflection fixed point, not automatically a Dirichlet, Neumann or interface boundary; a self-adjoint domain is transported separately.

## 13. A nodal spectral curve has a rational normalization [D,K,C]

Drafts 130–140 proved that the Lax–Novikov and Gel'fand–Dikii spectral polynomials agree up to an explicit factor of four. The spectral curve at integer depth $`n`$ is

```math
\mathcal C_n:\quad \nu^2=-\lambda\prod_{j=1}^n(\lambda+\kappa_j^2)^2,\qquad \kappa_j=jr.
```

For pairwise distinct positive $`\kappa_j`$, the curve has ordinary nodes at the $`n`$ finite points $`\lambda=-\kappa_j^2,\nu=0`$. Its **arithmetic genus** is $`n`$ (the hyperelliptic polynomial has odd degree $`2n+1`$), while the normalization has genus zero.

Indeed set

```math
\lambda=-s^2,\qquad \nu=s\prod_{j=1}^n(\kappa_j^2-s^2).
```

This is an explicit rational parametrization of the normalized curve by $`s\in\mathbb P^1`$. The preimages $`s=\pm\kappa_j`$ map to the **same node**. Thus the spectral curve's normalization is $`\mathbb P^1`$, and its apparent higher genus is carried by $`n`$ node identifications.

This distinction prevents a common overstatement: the degree-five polynomial when $`n=2`$ has arithmetic genus two, but this **singular** spectral model is not a smooth genus-two hyperelliptic curve with an ordinary two-dimensional principally polarized Jacobian.

## 14. The generalized Jacobian explains where the missing norming data belong [K,D]

For an irreducible projective rational curve with $`n`$ ordinary nodes and no other singularities, the generalized Jacobian is algebraically

```math
\mathrm{Jac}(\mathcal C_n)\simeq(\mathbb C^\times)^n.
```

Each node is obtained by identifying $`s=+\kappa_j`$ and $`s=-\kappa_j`$ on the normalized $`\mathbb P^1`$. A line bundle on the singular curve corresponds to line-bundle data on the normalization **plus a nonzero gluing scalar** identifying fibers at each such pair. This makes the generalized Jacobian a natural home for **multiplicative spectral divisor coordinates**.

An explicit logarithmic differential on the normalized curve is

```math
\Omega_j=d\log\left(\frac{s-\kappa_j}{s+\kappa_j}\right)=\left(\frac1{s-\kappa_j}-\frac1{s+\kappa_j}\right)ds.
```

It has residues $`+1`$ at $`+\kappa_j`$ and $`-1`$ at $`-\kappa_j`$, the paired preimages of one node. Its local closed contour integrals are multiples of $`2\pi i`$; it is a **third-kind logarithmic differential**, not a globally holomorphic differential on the normalized sphere.

The scattering theory supplies positive real multiplicative norming coordinates $`\beta_j^2`$, whose KdV evolution is diagonal exponential scaling. **In the usual Baker–Akhiezer/gluing normalization**, such coordinates parametrize a positive-real slice of the generalized-Jacobian picture. The precise identification of a chosen normalized bound-state tail coefficient with a particular algebro-geometric gluing scalar depends on the Baker–Akhiezer frame and node-marking convention; equality of their bare numerical values is **not** asserted without that additional construction.

### 14.1 Translation and KdV are distinct torus directions

At a translated canonical PT point, the positive norming coordinates transform as

```math
\beta_j^2\longmapsto\beta_j^2e^{2\kappa_j a}\quad\mathrm{under}\quad v\longmapsto v-a.
```

Under the first KdV time flow they transform instead as

```math
\beta_j^2(\tau)=\beta_j^2(0)e^{8\kappa_j^3\tau}.
```

In logarithmic divisor coordinates, translation and KdV follow the **two linear vectors** $`(2\kappa_j)_j`$ and $`(8\kappa_j^3)_j`$. For one node they are proportional; for two or more distinct exponents they are not. This is a geometric reformulation of the exact off-PT result of §8.

The nodal spectral curve is unchanged by either motion; the **marked divisor/gluing data move**. Hence the full spectral inverse problem requires both curve (eigenvalues) and divisor-like norming information, not just the former.

## 15. A NEW explicit marked 2-isogeny from the centered Pinney quartic to the symmetric Riemann elliptic curve [D,V,H]

The previous sections concern a **nodal spectral curve**. There is, separately, an exact bridge to a **smooth elliptic curve** already present in the archived Riemann-minimal-example period family. This bridge uses the *centered canonical Pinney mechanical energy curve*, not the Lax–Novikov spectral curve. Keeping them distinct is essential.

For the canonical constant-coefficient Pinney equation, let the positive amplitude be $`A(u)=a(u)`$, with

```math
a_{uu}=\frac{r^2}{4}a+\frac{\mu r^2}{4a^3},\qquad a^2=\sqrt\mu\cosh(ru),\qquad r,\mu>0.
```

Its zero-energy first integral gives the **smooth quartic genus-one curve**

```math
C_{\rm EP}:\quad Y^2=\frac{r^2}{4}(A^4-\mu),\qquad Y=Aa_u,\qquad \Delta(C_{\rm EP})\ne0,\qquad j(C_{\rm EP})=1728.
```

The archived Riemann minimal-example elliptic family has (with the distinct family parameter $`k_R=\lambda_R^{-1}-\lambda_R`$)

```math
E_{k_R}:\quad y_R^2=g^3+k_Rg^2-g,\qquad \lambda_R>0.
```

Its smooth-fiber discriminant and modular invariant are

```math
\Delta_{\rm cubic}=k_R^2+4,\qquad j_R(k_R)=256\frac{(k_R^2+3)^3}{k_R^2+4}.
```

At the symmetric Riemann parameter $`\lambda_R=1`$ (hence $`k_R=0`$), the fiber becomes

```math
E_0:\quad y_R^2=g^3-g,\qquad j(E_0)=1728.
```

The equality of $`j`$ values suggests a comparison. The following **explicit algebraic map** is stronger than that numerical coincidence.

### 15.1 Exact isogeny theorem

**Theorem 15.1 [D,V] (marked quartic-to-Riemann 2-isogeny).** The rational formulas

```math
g=\frac{A^2}{\sqrt\mu},\qquad y_R=\frac{2AY}{r\mu^{3/4}}
```

define a morphism of degree two between the smooth projective models of $`C_{\rm EP}`$ and $`E_0`$. On the affine chart they obey identically

```math
y_R^2=\frac{4A^2Y^2}{r^2\mu^{3/2}}=\frac{A^2(A^4-\mu)}{\mu^{3/2}}=g^3-g.
```

**Proof.** Substitute the quartic relation $`Y^2=r^2(A^4-\mu)/4`$; the equation above follows algebraically. A generic $`(g,y_R)`$ has two preimages $`(A,Y)`$ and $`(-A,-Y)`$, proving degree two. Both compactifications are smooth genus-one curves for $`\mu,r>0`$. By Riemann–Hurwitz, any nonconstant degree-two morphism between them is unramified, and after choosing origins the morphism is a **2-isogeny**. The polynomial identity and the differential formula below were independently verified with exact symbolic algebra.

### 15.2 Holomorphic differential pullback is EXACT

On the quartic, the holomorphic differential is $`dA/Y`$; on the symmetric Riemann elliptic curve it is $`dg/y_R`$. The map preserves their one-dimensional Hodge spaces **up to an explicit nonzero scalar**:

```math
\Phi^*\left(\frac{dg}{y_R}\right)=r\mu^{1/4}\frac{dA}{Y}.
```

**Proof.** Since $`dg=2A\,dA/\sqrt\mu`$ and $`y_R=2AY/(r\mu^{3/4})`$, their ratio simplifies exactly to $`r\mu^{1/4}dA/Y`$.

Thus the comparison is not merely “both have $`j=1728`$”: it is an **explicit algebraic isogeny with a proved marked holomorphic-differential scaling**. However the map does **not** specify an immersion height differential, a real homology marking or the closing periods of the complete Riemann minimal surface.

## 16. The V4 involutions reveal why the Pinney TIME differential does not descend along that isogeny [D,V]

The same centered Pinney quartic carries three elementary involutions:

```math
\sigma:(A,Y)\mapsto(-A,Y),\qquad\iota:(A,Y)\mapsto(-A,-Y),\qquad h:(A,Y)\mapsto(A,-Y).
```

They satisfy

```math
\sigma^2=\iota^2=h^2=1,\qquad\sigma\iota=\iota\sigma=h,\qquad\langle\sigma,\iota\rangle\cong V_4.
```

The involution $`\iota`$ is the **deck transformation of the degree-two elliptic isogeny** of §15; $`\sigma`$ is a *different* involution, producing the **genus-zero Pinney time quotient** already found in draft 120.

### 16.1 The Pinney time differential is invariant under sigma

From $`Y=Aa_u`$ one has

```math
du=\frac{A\,dA}{Y}.
```

Under $`\sigma`$, both $`A`$ and $`dA`$ change sign, so their product does not:

```math
\sigma^*(A\,dA/Y)=A\,dA/Y.
```

The quotient coordinates are

```math
J=A^2,\qquad Y^2=\frac{r^2}{4}(J^2-\mu),\qquad du=\frac{dJ}{2Y}.
```

This quotient is a **smooth conic** and the marked time differential descends. That is why the positive Pinney amplitude evolves via elementary hyperbolic functions despite the smooth genus-one quartic's nontrivial holomorphic period structure.

### 16.2 The holomorphic differential is invariant under iota instead

For the elliptic isogeny deck transformation,

```math
\iota^*(dA/Y)=dA/Y,\qquad \iota^*(A\,dA/Y)=-A\,dA/Y.
```

Thus the **holomorphic** differential descends (as in §15), but the **time** differential is anti-invariant and cannot descend as a differential on $`E_0`$ under the same quotient. Meanwhile $`\sigma^*(dA/Y)=-dA/Y`$, so the holomorphic differential does not descend along the conic quotient.

**Theorem 16.1 [D,V] (two complementary quotients).** The centered Pinney genus-one quartic supports a $`V_4`$ of exact involutions in which

- $`\sigma`$ produces a genus-zero quotient preserving the Pinney **time** differential;
- $`\iota`$ produces a genus-one **2-isogeny** preserving the holomorphic differential up to the scale $`r\mu^{1/4}`$;
- the two marked differential types are distinguished algebraically by opposite involution characters.

This is a rigorous geometric explanation for the simultaneous occurrence of **elementary Pinney time**, **elliptic binary-quartic invariants** and an **elliptic Riemann-fiber isogeny**. It does not conflate the original Master energy quartic, the nodal spectral curve, or any of their spectral operators.

### 16.3 Why the V4 quotient is not a proof of minimal-surface period closing

The archived Riemann family equips its elliptic fiber with *other* meromorphic Weierstrass data and marked real periods. Preserving $`dg/y_R`$ up to scale does not imply that all meromorphic immersion one-forms or their period lattices pull back compatibly. Moreover the source Pinney real positive-amplitude branch covers only part of the real quartic; the projective complex isogeny must be interpreted on its **full smooth algebraic compactification**.

A future period-level comparison must supply (i) a chosen homology basis, (ii) the Riemann height differential and Gauss map, (iii) the image/pullback of those forms, and (iv) their real period-closing equations. Without all four, no global minimal-surface identification is claimed.

## 17. The elliptic isogeny transfers periods and Hodge norms—with a marked index-two lattice [D,V,K]

The map $`\Phi:C_{\rm EP}\to E_0`$ of §15 is an unramified covering of degree two. Therefore $`\Phi_*H_1(C_{\rm EP},\mathbb Z)`$ is an **index-two sublattice** of $`H_1(E_0,\mathbb Z)`$, once compatible basepoints are fixed. For *every* closed cycle $`\gamma`$ on the Pinney quartic,

```math
\int_{\Phi_*\gamma}\frac{dg}{y_R}=r\mu^{1/4}\int_\gamma\frac{dA}{Y}.
```

This gives an exact **period-pullback formula**, with its full resolution/amplitude normalization. It is considerably more informative than equality of the two $`j`$ invariants.

There is also a precise relation between the Hodge pairings of these **finite-dimensional spaces of holomorphic differentials**. Write $`\omega_C=dA/Y`$, $`\omega_E=dg/y_R`$. Since $`\deg\Phi=2`$ and $`\Phi^*\omega_E=r\mu^{1/4}\omega_C`$,

```math
r^2\sqrt\mu\,\frac i2\int_{C_{\rm EP}}\omega_C\wedge\overline{\omega_C}=2\,\frac i2\int_{E_0}\omega_E\wedge\overline{\omega_E}.
```

**Proof.** Integrate the wedge product of the pulled-back differential over the compact source curve and use the degree formula for an orientation-preserving holomorphic covering. The scaling is $`|r\mu^{1/4}|^2=r^2\sqrt\mu`$.

**This IS a genuine marked elliptic Hodge-metric correspondence.** However it is a relationship between one-dimensional holomorphic-differential spaces on smooth complex curves, **not** a unitary identification of the original $`L^2((0,\infty),x\,dx)`$ of functions with the Hilbert space of Riemann-minimal-surface Jacobi modes. The latter requires a separate intertwiner, measure and domain.

### 17.1 The canonical real orbit on the symmetric elliptic fiber

Along the centered positive Pinney solution,

```math
A(u)=\mu^{1/4}\sqrt{\cosh(ru)},\qquad Y(u)=\frac{r\sqrt\mu}{2}\sinh(ru).
```

The isogeny image is the explicit real curve path

```math
g(u)=\cosh(ru),\qquad y_R(u)=\sqrt{\cosh(ru)}\,\sinh(ru),\qquad y_R^2=g^3-g.
```

This is not a closed elliptic period: $`g(u)\ge1`$ and tends to infinity at both ends. It is an exact *open real arc* on the symmetric Riemann elliptic fiber. In particular the existence of an explicit elementary real parametrization of **this arc with a non-Abelian clock** does not make the elliptic curve rational.

The time differential remains

```math
du=A\,dA/Y=\frac{\sqrt g}{r}\,\Phi^*(dg/y_R),
```

with the square-root factor living naturally on the degree-two source curve. This is another direct proof that the Pinney mechanical clock is not the Riemann holomorphic-period clock.

## 18. A precise three-curve map rather than a universal period equality [D,H,C]

Three separate algebraic varieties now have explicit roles:

| Curve | Equation | Genus and marking | Correct relation |
|---|---|---|---|
| $`\mathcal C_n`$ (Lax spectral) | $`\nu^2=-\lambda\prod(\lambda+\kappa_j^2)^2`$ | arithmetic genus $`n`$, **nodal**, normalization $`\mathbb P^1`$, paired-node gluing data | generalized Jacobian $`(\mathbb C^\times)^n`$, scattering/KdV norming coordinates after BA choice |
| $`C_{\rm EP}`$ (centered Pinney energy) | $`Y^2=(r^2/4)(A^4-\mu)`$ | smooth genus one; **time** differential $`A\,dA/Y`$ and **holomorphic** differential $`dA/Y`$ distinct | conic time quotient plus elliptic 2-isogeny |
| $`E_0`$ (symmetric Riemann elliptic fiber) | $`y_R^2=g^3-g`$ | smooth genus one; chosen holomorphic differential $`dg/y_R`$ | explicit index-two period-lattice relation with $`C_{\rm EP}`$ (§17) |

**Do not infer:** The nodal spectral curve $`\mathcal C_1`$ is not the same smooth elliptic curve as $`C_{\rm EP}`$ or $`E_0`$. A generalized Jacobian of a nodal rational spectral curve is not, without a smoothing and chosen degeneration, the same complex torus as a smooth elliptic Jacobian.

**What IS established:** There is an explicit 2-isogeny between the *two smooth elliptic curves* at the symmetric Riemann modulus, and a separate inverse-spectral normalized gluing picture on the singular spectral curve. Connecting the latter to the former would require a specified family of curves, differential, vanishing cycles, and gluing/period limiting map—not just a coinciding invariant.

## 19. The complete r=2 test, including inverse data and both elliptic involutions [D,V]

Set $`r=2`$, keeping $`\mu,c,c_{\rm ref}>0`$. In the original $`x`$ variable,

```math
u=\ln(x/c),\qquad S_2=\frac{2c^2x^2}{x^4+c^4},\qquad f_\mu(x;2,c)=\frac{c^2x}{\sqrt\mu(x^4+c^4)}.
```

The first two reflectionless potentials become the explicit rational functions

```math
V_1(x)=-32\frac{c^4x^4}{(x^4+c^4)^2},\qquad V_2(x)=-96\frac{c^4x^4}{(x^4+c^4)^2}.
```

The spectral and norming data are

```math
n=1:\quad \kappa_1=2,\quad\alpha_{1,1}^2=4;\qquad n=2:\quad (\kappa_1,\kappa_2)=(2,4),\quad(\alpha_{2,1}^2,\alpha_{2,2}^2)=(12,24).
```

For $`n=2`$ the full Marchenko tau is

```math
\tau_2(x)=\left(1+(c/x)^4\right)^3=1+3(c/x)^4+3(c/x)^8+(c/x)^{12}.
```

In the fixed reference coordinate $`v=\ln(x/c_{\rm ref})`$, the two squared tail coefficients are

```math
\beta_1^2=12(c/c_{\rm ref})^4,\qquad\beta_2^2=24(c/c_{\rm ref})^8.
```

Both independently give $`c=c_{\rm ref}(\beta_1^2/12)^{1/4}=c_{\rm ref}(\beta_2^2/24)^{1/8}`$. The original weighted norm is

```math
\int_0^\infty x|f_\mu|^2dx=\frac1{4\mu}.
```

The trace ratio recovers $`r=2`$ and the centered potential $`\int V^2`$ and $`\int V`$ satisfy $`3I_2/I_1^2=2`$ at **both** integer depths.

### 19.1 At r=2 the Pinney quartic and Riemann 2-isogeny simplify

The canonical centered Pinney quartic becomes

```math
C_{\rm EP}:\quad Y^2=A^4-\mu,\qquad A=\mu^{1/4}\sqrt{\cosh(2u)},\qquad Y=A A_u.
```

The explicit degree-two map to the symmetric Riemann curve is

```math
g=A^2/\sqrt\mu,\qquad y_R=AY/\mu^{3/4},\qquad y_R^2=g^3-g.
```

Its holomorphic-differential relation is

```math
\Phi^*(dg/y_R)=2\mu^{1/4}\,dA/Y.
```

The involution $`\sigma:(A,Y)\mapsto(-A,Y)`$ preserves the Pinney **time** differential and produces the conic quotient; $`\iota:(A,Y)\mapsto(-A,-Y)`$ preserves the **holomorphic** differential and produces the elliptic 2-isogeny. The $`V_4`$ distinctions survive the resolution specialization without changing the center $`c`$.

## 20. Verification protocol and exact algebraic regression data [V]

**Exact nonnumeric regression:** For $`1\le n\le6`$ construct the factorial numbers

```math
a_{n,j}=\frac{\alpha_{n,j}^2}{2jr}=\frac{(n+j)!}{2(j!)^2(n-j)!}
```

and expand

```math
\tau_n(z)=\sum_{I\subseteq\{1,\ldots,n\}}\left(\prod_{j\in I}a_{n,j}\right)\left(\prod_{i<j\in I}\frac{(j-i)^2}{(j+i)^2}\right)z^{\sum_{j\in I}j}.
```

Using Python's SymPy exact Rational arithmetic, subtraction of $`(1+z)^{n(n+1)/2}`$ gives the **zero polynomial for all six depths**, not merely a small floating-point residual. The degrees checked are $`1,3,6,10,15,21`$. The general theorem is supported separately by Marchenko inverse uniqueness and the known PT scattering data (§6).

**Further symbolic checks:**
1. Substitute the centered quartic $`Y^2=r^2(A^4-\mu)/4`$ into $`y_R^2-(g^3-g)`$ with $`g=A^2/\sqrt\mu`$, $`y_R=2AY/(r\mu^{3/4})`$: the residual is identically zero.
2. Simplify $`(dg/dA)Y/y_R`$: the result is exactly $`r\mu^{1/4}`$.
3. Calculate $`j`$ for the Riemann fiber $`y_R^2=g^3+k_Rg^2-g`$: it is $`256(k_R^2+3)^3/(k_R^2+4)`$, with $`j(0)=1728`$.
4. Verify directly that $`V_n=-2\partial_v^2\log(1+e^{-2r(v-u_0)})^{n(n+1)/2}`$ and that the potential traces satisfy $`r=3I_2/I_1^2`$.
5. Check the center norming ratios, the KdV exponents $`8j^3r^3\tau`$, and the barycenter velocity $`2n(n+1)r^2`$ at $`n=1,2,3`$.
6. On the smooth Pinney quartic, verify that $`\sigma^*(A\,dA/Y)=A\,dA/Y`$ while $`\iota^*(A\,dA/Y)=-A\,dA/Y`$, and that $`\iota^*(dA/Y)=dA/Y`$.
7. Check that the isogeny pullback of the holomorphic 1-form is scaled by $`r\mu^{1/4}`$; the Hodge norm relation then follows by the **topological degree-two integration theorem**, not numerical period-fitting.

**Scope:** These tests do not prove a unique spectral reconstruction from a bare transmission coefficient; full norming data and a fixed coordinate are needed. They do not prove that the physical surface's meromorphic **immersion** periods close, that all KdV solutions remain translated PT profiles, or that the logarithmic scalar Hilbert space is canonically isometric to a smooth elliptic curve's Hodge cohomology.

## 21. Audit of the proposed arrows

| Proposed statement | Result |
|---|---|
| Discrete eigenvalues and transmission alone recover the translation center | **False.** Norming coefficients and a reference origin are needed (§§2–4). |
| The complete positive reflectionless data reconstruct the integer PT well | **True**, with the Marchenko convention fixed (§§5–7). |
| The Marchenko determinant equals one binomial power | **True**, with a classical uniqueness proof and exact symbolic checks through depth six (§6). |
| First KdV time preserves every centered PT shape up to translation | **False for depth at least two**; separate norming phases destroy the PT ratios (§8). |
| Two trace integrals recover the initial resolution | **True** for the declared PT-origin isospectral family (§9). |
| The potential and original weighted profile have the same logarithmic center | **True in the matched canonical family** (§11). |
| The smooth Pinney mechanical quartic equals the nodal Lax spectral curve | **False**: their normalizations and marked data differ (§§13–18). |
| The centered Pinney quartic maps to the symmetric Riemann elliptic fiber | **True** via an explicitly verified degree-two isogeny (§15). |
| This isogeny preserves the holomorphic differential | **True up to exactly r times the fourth root of mu** (§15). |
| The same isogeny preserves Pinney time | **False**: the time differential is anti-invariant under its deck involution (§16). |
| The elliptic isogeny transfers a period sublattice and Hodge norm | **True**, with image lattice index two and exact scale (§17). |
| The elliptic correspondence proves immersion-period closing | **Not established**; the three Weierstrass forms and real cycles are still missing. |
| The original weighted SL norm equals a curve Hodge norm as Hilbert spaces | **Not established** by the scalar identities; an operator-domain-compatible map is required. |

## 22. Sources and reproducibility

### Historical framework material inspected

The November 18 ZIP includes the inverse-Wronski ell=3 module (H340–H344), binary-quartic and spectral-curve module (H177–H183), period hierarchy (H132, H145, H146), marchenko-legendre module and archived H100/H299 Lax–Novikov checks. The live GitHub drafts 120, 130 and 140 supply the Pinney energy curve and time quotient, finite-gap squared-eigenfunction polynomials, and normalized Darboux–Jost/Pinney spectral data. They are used as prior sources, not treated as new discoveries here.

### External established mathematics

- Reflectionless inverse scattering, right norming data and reconstruction uniqueness: Grunert–Teschl, *Inverse scattering for reflectionless Schrödinger operators with integrable potentials and generalized soliton solutions for the KdV equation*: https://er.ucu.edu.ua/server/api/core/bitstreams/143e517a-facd-4d33-931b-2328842714d0/content . This reference was located through source excerpts rather than freshly audited in full.
- Worked one-pole Marchenko normalization and exact KdV time law: https://integrable.org/nonlinear-waves/kdv-lax-and-reconstruction/ .
- Jost wave and norming convention audit: https://integrable.org/foundations/jost-solutions-and-scattering-data/ .
- Spectral scattering/soliton limits of finite-gap curves and marked divisor: https://academic.oup.com/integrablesystems/article/4/1/xyz006/5543069 .
- Generalized Jacobian, nodal line bundles and fiber gluing scalars: https://doi.org/10.1016%2FS0040-9383%2802%2900025-3 and https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/stability-conditions-for-line-bundles-on-nodal-curves/12D3D0D22563D6F54893676DFCD638F4 .
- The particular elliptic Riemann family and Gauss–Manin periods are from the historical project H466 onward, not inferred from the scattering literature.
- The explicit degree-two Pinney–Riemann isogeny and V4 differential character computation are derived in §§15–17 by polynomial substitution, pullback of one-forms, and the standard degree formula for a covering of elliptic curves.

### Independent exact checks

The Cauchy principal-minor subset expansion, evaluated using exact rational factorials, agrees with the binomial power for n=1,2,3,4,5,6, with degrees 1,3,6,10,15,21 and zero polynomial residual in each case. The all-depth proof invokes the stated classical uniqueness of the finite reflectionless inverse problem.

The Pinney–Riemann map was independently checked with exact symbolic substitution:

```math
g=A^2/\sqrt\mu,\quad y_R=2AY/(r\mu^{3/4}),\quad Y^2=r^2(A^4-\mu)/4\quad\Longrightarrow\quad y_R^2-g^3+g=0.
```

A separate differential simplification gives exactly the pullback factor r times the fourth root of mu. The Riemann cubic invariant was independently expanded as j=256(k_R^2+3)^3/(k_R^2+4). The V4 involution characters, trace integrals, KdV moment derivative and r=2 rational specialization were checked algebraically.

**Scope:** Local polynomial identities and the classical real reflectionless inverse theorem do not automatically prove an isometry between the original weighted SL operator and any elliptic Hodge Laplacian, or closure of the actual Riemann minimal-surface immersion periods.

## 23. Next mathematical targets

1. Give a fully elementary Cauchy determinant proof of the binomial tau identity without appealing to inverse-scattering uniqueness.
2. Mark a symplectic homology basis on the centered Pinney quartic and compute the integer matrix of its degree-two map to the Riemann symmetric elliptic fiber; compare periods at k_R=0 with the archived Gauss–Manin solution.
3. Pull back **all three** Riemann Weierstrass immersion forms through the isogeny and test their real periods, flux, and period-lattice closing. Preserve their poles and residues.
4. Smooth the nodal Lax spectral curve while retaining a chosen meromorphic differential and vanishing cycles; compare the degeneration to the smooth Pinney and Riemann elliptic data without presupposing equality.
5. Construct an exact half-line spectral inverse map in the original x-coordinate, including the center c, endpoint conditions and norming convention.
6. Classify how higher KdV time directions on the positive generalized Jacobian intersect the translated PT submanifold for depths n at least two.
7. Derive the higher trace invariants from the logarithmic derivative of transmission and the factorial spectrum; test resolution multiplication r to 2r.
8. Examine whether the V4 involutions of the Pinney quartic intertwine with the existing tetrahedral chart actions and clarify which act on holomorphic versus time differentials.
9. Develop a genuine Hilbert-operator intertwiner, if possible, between the weighted SL realization and a specifically marked elliptic geometric operator; numerical equality of norms is not enough.
10. Extend the normalized positive Pinney envelope and Jost phase dictionary along the explicit Marchenko/KdV time-dependent tau family, keeping the evolution parameter separate from canonical u=ln(x/c).

**Conclusion:** Complete real reflectionless data recover r and the log-center once a reference coordinate is fixed; the original weighted norm independently fixes mu. The integer Pöschl–Teller Marchenko determinant is a single binomial power, while KdV changes the node-gluing/norming data without changing its singular spectral curve. Separately, the smooth centered Pinney energy quartic has a proved degree-two holomorphic isogeny to the symmetric Riemann elliptic fiber, and its V4 involutions precisely distinguish elementary mechanical time from elliptic holomorphic periods. These are compatible but differently marked mathematical realizations—not one unqualified universal period or physical model.
