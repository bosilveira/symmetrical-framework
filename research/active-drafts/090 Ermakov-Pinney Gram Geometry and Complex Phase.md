---
id: SF-DRAFT-090
title: Ermakov-Pinney, Gram Geometry, and Complex Phase
status: provisional
created: 2026-11-18
proposed_layers: [I, II, III]
depends_on: [SF-I-020, SF-DRAFT-040, SF-DRAFT-060, SF-DRAFT-070, SF-DRAFT-080]
related_claims: [F04, F08, H112, H173, H177, H179, H313, H314, H315, H371, H373, H376]
---

# 090 Ermakov–Pinney, Gram Geometry, and Complex Phase

**Status:** Extensive provisional mathematics. [D] directly derived; [V] exact independently checked; [K] classical source with stated hypotheses; [H] prior archival result; [C] false/conflated assertion corrected; [O] open. Terms such as “Friedmann”, “instanton”, and “phase” are mathematical descriptors when used here; they do not install a physical system.

**Principal result:** The positive Pinney envelope $`a=\mu^{1/4}\sqrt{\cosh(ru)}`$ is the **modulus of one complex solution** of the linear half-rate backbone $`\Phi''=(r^2/4)\Phi`$. Its phase is exactly $`\mathrm{gd}(ru)/2`$, and the complex logarithmic derivative is $`(r/2)(W+iS)`$. The canonical soliton, kink, arctangent primitive, circle, Riccati equation, conserved Wronskian, Ermakov–Lewis invariant, Pinney quadratic determinant and Schwarzian are therefore explicit projections of one exact construction. The inverse exists after a positive determinant, phase choice and suitable domain; it is not an unqualified algebraic involution.

**Source basis:** GitHub SF-I-020 and drafts 040, 060, 070, 080. The historical ZIP `04-follow-ups/bernoulli-riccati.md`, `binary-quartic-and-spectral-curves.md`, `conformal-and-probabilistic-readings.md`, `bpst-yamabe-eguchi-hanson.md`, `friedmann-reciprocal-envelope.md`, the `00-meta/CLAIMS.md` entries H112/H177/H313–H315/H373, and the large 2026-11-16_v2 reference. Classical Pinney/Ermakov theory and DLMF Gudermannian are cited in §23. The new explicit complex phase factorization is checked separately, while no priority claim is made.

## 1. Canonical variables and a necessary naming distinction

For real $`x>0`$ preserve the project parameters

```math
u=\ln(x/c),\qquad c>0,\quad r>0,\quad\mu>0,\quad\theta=ru,\quad S=\mathrm{sech}\theta,\quad W=\tanh\theta.
```

Use $`a(u)>0`$ for a Pinney envelope, $`J(u)=a(u)^2`$ for its squared amplitude, $`\Phi`$ for a complex **linear solution**, $`\vartheta`$ for a **real phase**, and $`z(u)=\sqrt\mu/J`$ for the normalized nonlinear Master pulse. The letter $`J`$ in this document is **not** the raw cubic invariant $`J_{\rm quartic}`$ of a binary quartic. Distinguish the geometric Gram determinant $`\delta_G=AB-C^2`$ from a quartic discriminant $`\Delta_4`$ and from spatial curvature $`K`$.

## 2. Pinney's nonlinear equation and its linear carrier [K,D]

Let $`\Omega(u)^2`$ be a real, locally integrable coefficient on an interval and let $`\phi_1,\phi_2`$ be independent real solutions of

```math
\phi''+\Omega(u)^2\phi=0.
```

Their Wronskian $`\mathscr W=\phi_1\phi_2'-\phi_1'\phi_2`$ is constant. For real constants $`A,B,C`$ form

```math
J=A\phi_1^2+2C\phi_1\phi_2+B\phi_2^2,\qquad \delta_G=AB-C^2.
```

Where $`J>0`$, set $`a=\sqrt J`$. Then the **Pinney nonlinear-superposition identity** is

```math
a''+\Omega(u)^2a=\frac{k}{a^3},\qquad k=\mathscr W^2\delta_G.
```

**Derivation by the Gram determinant.** Let $`\phi=(\phi_1,\phi_2)^T`$ and $`G=\begin{pmatrix}A&C\\C&B\end{pmatrix}`$. Then $`J=\phi^TG\phi`$ and, because $`\phi''=-\Omega^2\phi`$,

```math
J'=2\phi^TG\phi',\qquad J''=2\phi'^TG\phi'-2\Omega^2 J.
```

The two-dimensional Gram determinant identity is

```math
(\phi^TG\phi)(\phi'^TG\phi')-(\phi^TG\phi')^2=(\det G)(\phi_1\phi_2'-\phi_1'\phi_2)^2=k.
```

Consequently,

```math
2JJ''-(J')^2+4\Omega^2J^2=4k.
```

Since $`a''=J''/(2a)-(J')^2/(4a^3)`$, dividing the identity by $`4a^3`$ yields Pinney's equation. This proof holds for any real $`\Omega(u)^2`$ and any zero-free positive interval, not just the constant canonical backbone.

### 2.1 The symmetry-square linear equation

Differentiate the identity in §2 (using $`k`$ constant) or use the three products $`\phi_1^2,\phi_1\phi_2,\phi_2^2`$ to obtain the third-order **linear** equation satisfied by $`J=a^2`$:

```math
J'''+4\Omega^2J'+2(\Omega^2)'J=0.
```

**Proof.** From the Pinney first integral $`2JJ''-(J')^2+4\Omega^2J^2=4k`$, differentiation gives $`2J[J'''+4\Omega^2J'+2(\Omega^2)'J]=0`$; $`J>0`$ allows division. The three quadratic products of a fundamental pair span the symmetric-square solution space, so every such $`J`$ is described by the quadratic Gram construction, locally.

This **symmetric-square linearizability** is stronger and more accurate than calling the nonlinear Pinney equation itself a Riccati equation. The Pinney solution is a positive square root of an element of $`\mathrm{Sym}^2`$ of a linear solution space, constrained by one quadratic determinant.

## 3. The constant inverted-oscillator carrier of the framework [D,V]

Choose the exact coefficient

```math
\Omega^2=-r^2/4,\qquad \phi_+(u)=e^{ru/2},\qquad \phi_-(u)=e^{-ru/2},\qquad \mathscr W=-r.
```

Then

```math
J(u)=Ae^{ru}+2C+Be^{-ru},\qquad k=r^2(AB-C^2)=r^2\delta_G.
```

Its exact differential identities are

```math
J''=r^2(J-2C),\qquad (J')^2=r^2(J^2-4CJ-4\delta_G),\qquad J'''=r^2J'.
```

Substitute into §2 to get

```math
a''=\frac{r^2}{4}a+\frac{r^2\delta_G}{a^3}.
```

Three separate parameters have distinct meanings: $`c`$ selects the logarithmic center, $`r`$ sets the rate, and $`\delta_G`$ sets the strength of the inverse-cube term. The extra Gram coefficient $`C`$ does **not** change the Pinney ODE: it changes its conserved energy and its positive solution branch.

### 3.1 Positive-definite, semidefinite and indefinite Gram regimes

If $`\delta_G>0`$ and $`G`$ is positive definite, $`J(u)>0`$ globally for nonzero $`\phi(u)`$ and a global real Pinney envelope exists. If $`\delta_G=0`$, the quadratic form may be a square, giving a zero-inverse-cube Pinney equation with zeros depending on the branch. If $`\delta_G<0`$, the quadratic form is indefinite and the square root is available only on intervals where $`J>0`$. These signs classify a *Gram form*, not the Levi-Civita curvature sign or a binary-quartic elliptic root pattern.

## 4. Centered canonical envelope and exact Pinney solution [D,V]

Set

```math
A=B=\sqrt\mu/2,\qquad C=0,\qquad\delta_G=\mu/4,\qquad k=\mu r^2/4.
```

Then

```math
J=\sqrt\mu\cosh(ru),\qquad a=\mu^{1/4}\sqrt{\cosh(ru)},\qquad a''=\frac{r^2}{4}a+\frac{\mu r^2}{4a^3}.
```

The squared envelope and its first integral obey

```math
J''=r^2J,\qquad J^2-(J'/r)^2=\mu,\qquad a'^2=\frac{r^2}{4}(a^2-\mu/a^2).
```

At $`u=0`$, $`a=\mu^{1/4}`$ and $`a'=0`$; the envelope is everywhere positive. The familiar kinematic Friedmann form is the **logarithmic derivative** of the same exact identity:

```math
H=\frac{a'}{a}=\frac r2W,\qquad H^2=\frac{r^2}{4}\left(1-\frac\mu{a^4}\right).
```

As shown in draft 040, this is an algebraic first integral. A four-dimensional warped metric and source field equation would be *additional* choices, not consequences of the name Friedmann.

## 5. Autonomous Pinney Lagrangian, energy and Gram coefficient C [D]

The constant-coefficient Pinney equation in §3 is the Euler–Lagrange equation for the ordinary one-dimensional action with Lagrangian

```math
L(a,a')=\frac12(a')^2+\frac{r^2}{8}a^2-\frac{k}{2a^2}.
```

Its conserved energy is

```math
E_{\rm EP}=\frac12(a')^2-\frac{r^2}{8}a^2+\frac{k}{2a^2}.
```

**Theorem 5.1.** For $`J=Ae^{ru}+2C+Be^{-ru}`$ and $`k=r^2\delta_G`$,

```math
E_{\rm EP}=-\frac{r^2C}{2}.
```

**Proof.** Insert $`a'^2=(J')^2/(4J)`$ and use $`(J')^2=r^2(J^2-4CJ-4\delta_G)`$. The $`J`$ and $`\delta_G/J`$ terms cancel, leaving $`-r^2C/2`$.

Thus the selected centered branch $`C=0`$ has zero Pinney energy. It is crucial **not** to identify that number automatically with the normalized nonlinear Master energy $`e`$ or with the quartic $`J`$ invariant.

## 6. The complex-amplitude theorem [D,V,K]

For the general real equation $`\phi''+\Omega^2\phi=0`$, let $`a>0`$ solve $`a''+\Omega^2a=k/a^3`$ with $`k>0`$. Choose the phase by

```math
\vartheta'(u)=\frac{\sqrt k}{a(u)^2},\qquad\Phi(u)=a(u)e^{i\vartheta(u)}.
```

**Theorem 6.1 (amplitude-phase reconstruction).** The complex function $`\Phi`$ solves the **original linear equation** and has constant Wronskian with its complex conjugate:

```math
\Phi''+\Omega^2\Phi=0,\qquad \mathscr W(\Phi,\overline\Phi)=-2i\sqrt k.
```

**Proof, step by step.** Differentiate the complex polar form:

```math
\Phi''=e^{i\vartheta}\bigl[a''-a(\vartheta')^2+i(2a'\vartheta'+a\vartheta'')\bigr].
```

The imaginary term vanishes because $`(a^2\vartheta')'=0`$. The real term satisfies $`a''-a(\vartheta')^2+\Omega^2a=k/a^3-k/a^3=0`$. Finally

```math
\Phi\overline\Phi'-\Phi'\overline\Phi=-2ia^2\vartheta'=-2i\sqrt k.
```

Conversely, any zero-free complex linear solution with nonzero Wronskian with its conjugate yields a positive Pinney envelope $`a=|\Phi|`$ and $`k=|\mathscr W(\Phi,\bar\Phi)|^2/4>0`$. This is an equivalence of *amplitude plus phase-rotation data*, not an equality between linear and nonlinear equation solution spaces without qualifications.

### 6.1 Negative determinant: a real hyperbolic analogue

If $`k<0`$ on an interval where $`a>0`$, set $`\sigma'=\sqrt{-k}/a^2`$. Then the two real functions $`a e^{\sigma}`$ and $`a e^{-\sigma}`$ solve $`\phi''+\Omega^2\phi=0`$, since their cross terms cancel and $`a''+a(\sigma')^2+\Omega^2a=0`$. The $`k=0`$ case is degenerate and does not yield a nonzero phase Wronskian. These are the determinant-sign regimes of a **specific Pinney quadratic**, not an automatic KAN/curvature/torsion classification of arbitrary manifolds.

## 7. The canonical complex solution in elementary closed form [D,V]

For the positive canonical envelope in §4, define

```math
\Phi(u)=\mu^{1/4}[\cosh(ru/2)+i\sinh(ru/2)].
```

Its second derivative is $`\Phi''=(r^2/4)\Phi`$ immediately. Squaring it gives an unexpectedly simple expression:

```math
\Phi(u)^2=\sqrt\mu[1+i\sinh(ru)].
```

Taking its modulus,

```math
|\Phi|^2=\sqrt\mu\cosh(ru)=a^2.
```

The argument on the real $`u`$ line is the **half-Gudermannian**:

```math
\vartheta(u)=\arg\Phi(u)=\frac12\arctan(\sinh(ru))=\frac12\mathrm{gd}(ru),\qquad\vartheta'=\frac r2S.
```

It also obeys the phase-amplitude identity $`a^2\vartheta'=r\sqrt\mu/2=\sqrt k`$ exactly. This is a direct realization of Theorem 6.1 with no elliptic or hypergeometric integral remaining.

## 8. The complex logarithm unifies amplitude and Gudermannian [D,V]

For real $`u`$, the complex number $`1+i\sinh(ru)`$ has positive real part, so its principal complex logarithm is continuous and unambiguous on the whole real line. Its modulus is $`\cosh(ru)`$ and argument $`\mathrm{gd}(ru)`$:

```math
\mathrm{Log}[1+i\sinh(ru)]=\ln\cosh(ru)+i\,\mathrm{gd}(ru).
```

Equivalently,

```math
\mathrm{Log}\,\Phi=\frac14\ln\mu+\frac12\ln\cosh(ru)+\frac i2\,\mathrm{gd}(ru).
```

This is **one complex logarithm** encoding the real reciprocal envelope and its angular phase. It is not just a coincidence of primitive formulas. In particular

```math
2\mathrm{Re}(\Phi'/\Phi)=\partial_u\ln J,\qquad2\mathrm{Im}(\Phi'/\Phi)=\partial_u\,\mathrm{gd}(ru).
```

If $`x`$ is allowed to be complex, one must choose a branch of $`u=\mathrm{Log}(x/c)`$ and avoid zeros of the analytic carrier $`\Phi`$; the real-argument identity alone does not define a global single-valued complex solution on all of $`\mathbb C^\times`$. Around the origin, $`u`$ changes by $`2\pi i`$; for noninteger $`r`$, $`e^{ru}`$ also acquires monodromy. A conjugate solution on the **real** line is not a holomorphic conjugation in the complex $`u`$-plane.

## 9. One complex Riccati equation, two canonical real fields [D,V]

Differentiate the logarithm in §8:

```math
Q(u)=\frac{\Phi'}{\Phi}=\frac r2[W(u)+iS(u)].
```

Because $`\Phi''=(r^2/4)\Phi`$,

```math
Q'+Q^2=\frac{r^2}{4}.
```

The nontrivial geometric constraint is

```math
|Q(u)|^2=\frac{r^2}{4}(W^2+S^2)=\frac{r^2}{4}.
```

Thus $`Q`$ evolves along the **upper semicircle** of radius $`r/2`$ in the complex Riccati plane, with endpoints $`-r/2`$ and $`+r/2`$ as $`u\to\mp\infty`$. Its real and imaginary parts are not separately solutions of the same scalar Riccati equation. In fact for $`Q=a_0+ib_0`$,

```math
a_0'+a_0^2-b_0^2=r^2/4,\qquad b_0'+2a_0b_0=0,\qquad a_0=rW/2,\quad b_0=rS/2.
```

The imaginary part supplies exactly the correction that makes the *complex* logarithmic derivative a constant-potential Riccati solution. Omitting that part makes the real rate $`rW/2`$ fail the same constant Riccati equation.

## 10. Projective ratio, Cayley transform and Schwarzian [D,V]

On real $`u`$, form the ratio of the two independent complex solutions $`\Phi`$ and $`\bar\Phi`$:

```math
Z(u)=\frac{\Phi(u)}{\overline\Phi(u)}=e^{2i\vartheta(u)}=e^{i\mathrm{gd}(ru)}=S+iW.
```

With $`t=e^{ru}=(x/c)^r>0`$, a direct algebraic reduction gives the explicit **Cayley-type Möbius map**

```math
Z=i\frac{t-i}{t+i}=\frac{2t+i(t^2-1)}{t^2+1}.
```

Because $`Z`$ is a Möbius transformation of $`e^{ru}`$, its Schwarzian is

```math
\{Z,u\}=\{e^{ru},u\}=-\frac{r^2}{2}.
```

The projective map lies on the right semicircle $`\mathrm{Re}\,Z=S>0`$, and its argument is the Gudermannian. This is a rigorous connection among **Riccati projectivization, complex logarithm, the Gudermannian and the Schwarzian**.

### 10.1 Phase Schwarzian identity for arbitrary positive Pinney envelopes

For any positive Pinney amplitude with $`k>0`$ and $`\vartheta'=\sqrt k/a^2`$, differentiation of its logarithmic derivative yields

```math
\{\vartheta,u\}=-2\frac{a''}{a}=2\Omega^2-\frac{2k}{a^4}.
```

Since the Schwarzian chain rule for $`e^{2i\vartheta}`$ adds $`2(\vartheta')^2=2k/a^4`$,

```math
\{e^{2i\vartheta},u\}=\{\vartheta,u\}+2(\vartheta')^2=2\Omega^2.
```

**Proof.** From $`\vartheta'=\sqrt k/a^2`$, one has $`\vartheta''/\vartheta'=-2a'/a`$. Substitute into the definition of the Schwarzian to obtain $`-2a''/a`$. The chain-rule term cancels the inverse-cube Pinney contribution exactly. This *is* the projective carrier equation recovered from the nonlinear amplitude-phase data.

## 11. The arctangent primitive is the Pinney phase [D,V,H112]

The canonical original amplitude-normalized function is

```math
f_\mu(x;r,c)=\frac1{2\sqrt\mu\,x}\mathrm{sech}(r\ln(x/c)).
```

Since $`dx/x=du`$ and $`\partial_u\mathrm{gd}(ru)=rS`$,

```math
\int f_\mu(x;r,c)\,dx=\frac{\mathrm{gd}(ru)}{2r\sqrt\mu}+C_0.
```

The Pinney phase is therefore

```math
\vartheta(u)=r\sqrt\mu\left[\int^x f_\mu(s;r,c)\,ds-\int^c f_\mu(s;r,c)\,ds\right]=\frac12\mathrm{gd}(ru).
```

The $`C_0`$ integration choice fixes $`\vartheta(c)=0`$. This is the precise link to the framework's arctangent/Hopf–Villarceau primitive: the *same* integral is the phase required to reconstruct the underlying linear solution from its Pinney modulus. This observation is algebraic and does not automatically identify an SU(2) gauge field, a surface immersion or a physical fluxon.

## 12. The Ermakov–Lewis invariant is a quadratic conserved form on solutions [D,K]

For arbitrary real $`\Omega^2(u)`$, $`k>0`$, let $`a>0`$ solve Pinney and let $`y`$ be any **real** solution of the underlying linear equation. Define

```math
I_{\rm EL}[y;a]=\frac12\left[(ay'-a'y)^2+k(y/a)^2\right].
```

**Theorem 12.1.** The derivative of $`I_{\rm EL}`$ vanishes.

**Proof.** Let $`Z=ay'-a'y`$. Then $`Z'=ay''-a''y=-ky/a^3`$ by the linear and Pinney equations. Therefore

```math
\frac{dI_{\rm EL}}{du}=ZZ'+k\frac ya\left(\frac ya\right)'=-\frac{kZy}{a^3}+\frac{k y}{a}\frac{ay'-a'y}{a^2}=0.
```

The invariant is a positive quadratic form on the two-dimensional real linear solution space when $`k>0`$. It is not an additional independent constant for an arbitrary nonlinear energy curve unless the corresponding linear/Pinney carrier has been specified.

### 12.1 Angle-action coordinates

The Pinney polar decomposition supplies for every real linear solution the representation

```math
y(u)=a(u)[A_0\cos\vartheta(u)+B_0\sin\vartheta(u)],\qquad\vartheta'=\sqrt k/a^2.
```

The coefficients $`A_0,B_0`$ are constants, and the invariant is

```math
I_{\rm EL}=\frac k2(A_0^2+B_0^2).
```

The phase advance and amplitude may be recovered from a chosen zero-free complex solution. But amplitude alone **forgets** its initial complex phase and the normalization of the underlying Wronskian.

## 13. Reciprocal Pinney map to the original Master equation [D,V]

Set $`y=1/a^2=1/J`$ with the general exponential Gram envelope $`J=Ae^{ru}+2C+Be^{-ru}`$. Exact differentiation gives

```math
y''=r^2y-6Cr^2y^2-8\delta_G r^2y^3.
```

Its first integral is

```math
(y')^2=r^2(y^2-4Cy^3-4\delta_Gy^4).
```

**Proof.** Start from $`y'=-J'/J^2`$, $`y''=2(J')^2/J^3-J''/J^2`$ and substitute both identities in §3. No approximation or suppressed parameter is involved.

For the canonical $`C=0`$, $`\delta_G=\mu/4`$,

```math
y''=r^2y-2\mu r^2y^3,\qquad y=\frac{S}{\sqrt\mu}=2xf_\mu.
```

Thus **the canonical nonlinear Master separatrix is the reciprocal square of a positive Pinney solution**. For $`C\ne0`$, an extra quadratic term appears, so a generic Pinney solution does **not** map to the unshifted cubic Master equation. The named reciprocal map has a clear image and a clear limitation.

## 14. The general finite-energy extension must not be silently conflated [H313,D]

The historical H313 extension introduces a *different* energy integral

```math
(y')^2=\varepsilon+r^2y^2-4Cr^2y^3-\delta_G r^2y^4.
```

In that historical convention the quartic coefficient differs from the $`\delta_G`$ used in §13 by a factor of four. Writing $`\delta_{\rm H313}=4\delta_G`$ in the historical equation removes ambiguity. With $`J=1/y`$ and $`a=\sqrt J`$ one obtains

```math
J'^2=\varepsilon J^4+r^2J^2-4Cr^2J-4\delta_Gr^2,\qquad J''=2\varepsilon J^3+r^2(J-2C).
```

and, on zero-free branches,

```math
a''=\frac{r^2}{4}a+\frac{\delta_G r^2}{a^3}+\frac{3\varepsilon}{4}a^5.
```

This **quintic deformation** is no longer the pure Ermakov–Pinney equation when $`\varepsilon\ne0`$. Therefore the elliptic Master energy curve away from the separatrix does not automatically remain representable by the same elementary two-exponential Pinney envelope.

## 15. The Gram-square quartic is singular even when Pinney k is positive [D,V]

The underlying quadratic form $`G(X,Z)=AX^2+2CXZ+BZ^2`$ has determinant $`\delta_G`$. If one constructs its square as a binary quartic $`F=G^2`$, the raw invariants are

```math
I(F)=16\delta_G^2,\qquad J_{\rm quartic}(F)=128\delta_G^3,\qquad\Delta_4(F)=0.
```

The last equality holds identically because squaring a quadratic doubles each of its roots. This is **not** the same quartic as the generic nonsingular nonlinear Master energy curve or the curvature quartic of an immersed catenoid. In particular the Pinney $`k>0`$ branch is not characterized by a nonzero *quartic* discriminant.

## 16. A geometric Pinney reconstruction without forcing a physical model [D,K]

The ODE $`a''=(r^2/4)a+k/a^3`$ may be used as a positive scalar radial function in a chosen warped geometry, as an amplitude for a linear Jacobi field, or in a Kähler radial coordinate. Those are **separately declared realizations**. Draft 040 derives a specific Lorentzian flat-slice metric $`g=-du^2+a(u)^2\delta_{ij}dq^idq^j`$ and its Levi-Civita/Weitzenbock scalar identity. Draft 060 derives a separate complex Monge–Ampere radial profile $`a_{\rm EH}\sqrt{\cosh(r\xi)}`$. The underlying scalar ODE is shared; the metric, dimension, connection, topology and clock are not.

## 17. Half-angle, Gudermannian and rational recursions at r=2 [D,V]

Set $`r=2`$ but retain $`c,\mu>0`$ and $`u=\ln(x/c)`$. The canonical positive envelope becomes

```math
J=\sqrt\mu\cosh(2u)=\sqrt\mu\frac{x^4+c^4}{2c^2x^2},\qquad a=\mu^{1/4}\sqrt{\frac{x^4+c^4}{2c^2x^2}}.
```

The linear carrier, its square and logarithmic derivative are

```math
\Phi=\mu^{1/4}(\cosh u+i\sinh u),\quad\Phi''=\Phi,\quad\Phi^2=\sqrt\mu[1+i\sinh(2u)],\quad\Phi'/\Phi=W_2+iS_2.
```

The phase is an explicit inverse tangent of the original monomial:

```math
\vartheta(u)=\frac12\mathrm{gd}(2u)=\arctan[(x/c)^2]-\pi/4,\qquad \vartheta_u=S_2.
```

The real fields have rational forms

```math
S_2=\frac{2c^2x^2}{x^4+c^4},\qquad W_2=\frac{x^4-c^4}{x^4+c^4},\qquad f_\mu(x;2,c)=\frac{c^2x}{\sqrt\mu(c^4+x^4)}.
```

Furthermore the original primitive is elementary:

```math
\int f_\mu(x;2,c)\,dx=\frac1{2\sqrt\mu}\arctan(x^2/c^2)+C_0,
```

consistent with the Gudermannian formula after choosing an additive constant.

### 17.1 Full-angle doubling from the half-rate complex solution

For $`t=e^u=x/c`$, define $`S_1=2t/(1+t^2)`$ and $`W_1=(t^2-1)/(t^2+1)`$. Then

```math
S_2=\frac{S_1^2}{2-S_1^2},\qquad W_2=\frac{2W_1}{1+W_1^2}.
```

The passage from $`r=1`$ to $`r=2`$ is generated algebraically by the Chebyshev/doubling map on the original exponential variable. It therefore acts simultaneously on the real Riccati field, the Pinney amplitude, the complex log, and the Master reciprocal profile. The **same doubled formulas** arise without identifying their separate geometric or stochastic realizations.

## 18. Möbius covariance and the sign of the Pinney constant [D,C]

Changing the basis of a rank-two linear solution space by an invertible matrix changes the coefficient matrix $`G`$ by congruence. The product $`(\det G)\mathscr W^2=k`$ remains invariant when the basis and Gram coefficients are transformed consistently. This is a *symplectic/representation-theoretic* covariance, not a physical conservation law for every realization.

For $`k>0`$, a positive-definite $`G`$ yields a globally smooth positive envelope on the canonical real line. Its phase gives a unit-circle projective quotient. For $`k<0`$, use the hyperbolic exponential pair of §6.1 where $`a>0`$. For $`k=0`$, the phase/Wronskian reconstruction degenerates. These three determinant regimes should not be assigned automatically to Levi-Civita curvature, Weitzenbock torsion, or nilpotent orbits of an unrelated quartic.

## 19. Branch cuts, poles and global obstructions [D,C]

The real expression $`\mathrm{Log}(1+i\sinh(ru))`$ is single-valued on the real axis because its argument stays in $`(-\pi/2,\pi/2)`$. When $`u`$ is complexified, zeros of the analytic carrier and the chosen branch cuts must be tracked. The complex Riccati logarithmic derivative has poles at zeros of $`\Phi`$, even though the linear solution itself is analytic there. The reciprocal $`y=1/a^2`$ is not defined at zeros of a general indefinite Gram envelope. These analytic issues cannot be bypassed by giving the variables the same formal name.

Global reconstruction of a phase on a periodic base may have nontrivial winding or Floquet monodromy. A real positive envelope need not itself be periodic even when the linear carrier has oscillatory coefficients. A positive Pinney envelope also need not belong to the Hilbert-space domain of the associated Sturm–Liouville spectral problem.

## 20. Three further exact identities [D,V]

**(i) Curvature of the amplitude log.** From $`\ln a=\tfrac14\ln\mu+\tfrac12\ln\cosh(ru)`$,

```math
(\ln a)''=\frac{r^2}{2}S^2,\qquad (\ln J)''=r^2S^2.
```

**(ii) Phase-density invariant.** The canonical phase speed is

```math
a^2\vartheta'=\frac{r\sqrt\mu}{2},\qquad \frac{\vartheta'}{r/2}=S=\frac{\sqrt\mu}{a^2}.
```

**(iii) Complex Riccati circle.** Writing $`Q=\Phi'/\Phi`$ and its two real parts explicitly,

```math
4|Q|^2=r^2,\qquad \mathrm{Re}\,Q=\frac12(\ln J)',\qquad \mathrm{Im}\,Q=\vartheta'.
```

These identities are invariant statements about *the chosen solution* of the half-rate linear equation. The last modulus is not constant for a generic complex Sturm–Liouville solution; it is a special property of this canonical centered solution.

## 21. Where the “duality” exists and where it does not [D,C]

Pinney permits an exact **two-way reconstruction with phase**:

```math
\mathrm{linear\ pair+Gram\ form}\longrightarrow a=\sqrt{\phi^TG\phi}\longrightarrow (a,\vartheta)\longrightarrow\Phi=ae^{i\vartheta}.
```

The inverse from a positive solution of a Pinney equation with $`k>0`$ recovers a zero-free complex linear solution up to a constant unit phase. The envelope alone is not an inverse to the original pair: it forgets the basis, orientation and initial phase. For $`k\le0`$, a distinct real/hyperbolic or degenerate reconstruction applies. Because no new physical interpretation is required, this is a rigorous **nonlinear-superposition and phase-amplitude correspondence**, not a categorical involutive duality between all Sturm–Liouville operators and all nonlinear Master trajectories.

## 22. Open mathematical investigations

1. Recover the canonical circle/Riccati web from a general positive $`SL_2`$ Gram form and determine how changing $`C`$ moves its complex phase curve off the fixed canonical circle $`|Q|=r/2`$.
2. Classify the complex branch points of $`\Phi(u)`$ and their images under $`u=\mathrm{Log}(x/c)`$ for integer and irrational $`r`$; track the monodromy of the Gudermannian phase.
3. Identify which self-adjoint Weyl–Titchmarsh boundary data admit a positive Pinney envelope built from the selected Weyl/Jost solutions, including singular endpoints and scattering regimes.
4. Compare the symmetric-square third-order operator with the Gauss–Manin connection of the archived level-five elliptic family, retaining the different clocks.
5. Determine which nonzero-energy nonlinear Master quartics can be represented by a generalized nonautonomous Pinney equation after an explicit time transformation. Do not infer this from the zero-energy separatrix alone.
6. Study the half-rate complex Riccati circle under $`r\mapsto2r`$ and its induced rational Chebyshev dynamics, in both real and complex logarithmic $`x`$-coordinates.

## 23. References, checks and consolidation

**Independent exact checks [V]:** The identity $`\Phi^2=\sqrt\mu(1+i\sinh ru)`$, complex Riccati equation, constant modulus $`|Q|=r/2`$, determinant first integral, zero-energy reciprocal cubic, r=2 rational/double-angle identities and Ermakov–Lewis derivative were checked symbolically with explicit simplifications and by direct differentiation. The general symmetric-square and phase reconstruction are proved in §§2 and 6 rather than inferred by analogy.

**External classical references:** Nonlinear superposition, Milne amplitude and polar phase: https://www.sciencedirect.com/science/article/pii/S0378475406002631 and https://www.sciencedirect.com/science/article/pii/S037596010300495X . NIST Gudermannian: https://dlmf.nist.gov/4.23 . Liouville/Sturm–Liouville: https://dlmf.nist.gov/1.13 . Internal archival provenance: H112 (Gudermannian), H177–H179 (projective/spectral curves), H313–H315 (reciprocal Gram/finite energy), H373 (Kähler Pinney).

**Proposed placement:** Layer I: Gram form, Pinney theorem, symmetric square, Wronskian, canonical complex log and doubling; Layer II: projective/Cayley/Schwarzian developing map and appropriately typed geometric realizations; Layer III: reciprocal Master, finite-energy obstruction and Ermakov–Lewis; Layer IV: optional systems with their own actions/domains only after a complete independent model is given.

**Conclusion:** The compact expression $`\Phi=\mu^{1/4}[\cosh(ru/2)+i\sinh(ru/2)]`$ is the unifying linear carrier of the framework's canonical Ermakov–Pinney amplitude, Gudermannian phase, complex logarithm and two real scalar fields. The mathematical relationship is exact but **typed**: it preserves a Wronskian/phase and forgets other data unless those are specified.
