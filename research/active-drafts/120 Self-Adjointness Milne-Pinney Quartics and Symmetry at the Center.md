---
id: SF-DRAFT-120
title: Self-Adjointness, Milne–Pinney Quartics, and Symmetry at the Center
status: provisional
created: 2026-11-18
proposed_layers: [I, II, III]
depends_on: [SF-I-020, SF-DRAFT-020, SF-DRAFT-030, SF-DRAFT-040, SF-DRAFT-050, SF-DRAFT-060, SF-DRAFT-080, SF-DRAFT-090, SF-DRAFT-100, SF-DRAFT-110]
related_claims: [F04, F08, H100, H112, H169, H170, H171, H172, H173, H176, H177, H178, H179, H183, H313, H314, H315, H352, H421, H424, H429, H430]
---

# 120 Self-Adjointness, Milne–Pinney Quartics, and Symmetry at the Center

**Status:** Extensive *provisional* mathematical audit; do not promote it into a canonical theorem chapter or CLAIMS without a separate review. [D] denotes a directly derived result; [V] a checked algebraic identity; [K] established literature with stated hypotheses; [H] historical archive evidence (retain its original verification level); [C] a corrected interpretation or counterexample; [O] an open problem.

**Research question:** Does Ermakov–Pinney “measure” Sturm–Liouville self-adjointness? Can a supposed loss of self-adjointness correspond to a Higgs-like double well, centrifugal well, or tunneling? What exactly do Milne–Pinney amplitude/phase, the Riccati/projective/Hopf web, and the canonical half-integral at $x=c$ preserve? How do the three distinct binary-quartic constructions behave?

**Main answer:** Sturm–Liouville self-adjointness is determined by the formal differential expression *together with an operator domain and boundary/transmission conditions*. Ermakov–Pinney does **not** measure it; its Pinney determinant measures the Wronskian/phase current of a **chosen** linear solution pair. For real coefficients that current is locally conserved whether the selected operator realization is self-adjoint or not. Loss of self-adjointness can be created by complex boundary conditions without changing the differential equation or Pinney envelope. Conversely a real self-adjoint barrier has genuine tunneling and can have nonzero generalized-eigenfunction flux. The canonical positive Pinney amplitude has an inverse-square barrier but **not** a Higgs double well. An exact quartic/conic quotient explains why its energy curve can look elliptic while its distinguished time evolution is elementary. Reflection across $u=0$ defines a genuine self-adjoint interval decomposition, while the original integral halves because of an independent (but compatible) invariant measure.

**Source basis:** Current GitHub main branch SF-I-020 and provisional drafts 020, 030, 040, 050, 060, 080, 090, 100, 110; historical ZIP symmetrical-framework-update-2026-11-18-bu.zip, especially 04-follow-ups/spectral-calculus.md (H169–H172, reviewed directly), bernoulli-riccati.md, friedmann-reciprocal-envelope.md, fundamental-forms-willmore-hopf.md and conformal-and-probabilistic-readings.md. External sources on Weyl endpoint classification, Milne phase, self-adjoint point interactions and tunneling are listed in §30. The source archive's half-split statements are differentiated from this draft's new quartic quotient and explicit non-self-adjoint counterexamples.

## 1. Typed quantities: the independent coordinate is not the spectral parameter

Fix the canonical positive parameters and logarithmic coordinate:

```math
x,c,r,\mu>0,\qquad u=\ln(x/c),\qquad x=ce^u,\qquad S=\mathrm{sech}(ru),\quad W=\tanh(ru),\quad R=\cosh(ru).
```

The original rational function, including its amplitude normalization, is

```math
f_\mu(x;r,c)=\frac{c^rx^{r-1}}{\sqrt\mu(c^{2r}+x^{2r})}=\frac{\mathrm{sech}(ru)}{2\sqrt\mu\,x}.
```

With $\mu=1$ this is precisely the original Symmetrical Function. In a Sturm–Liouville problem denote a *spectral parameter* by $\lambda$; do not confuse it with resolution $r$, Pinney strength $k$, its nonlinear energy $\mathcal E_a$, the Master energy $\varepsilon_N$, or the eigenvalue of an *unrelated* surface Jacobi operator.

The normalized original Master equation and separatrix read

```math
y=2xf_\mu,\qquad y_{uu}=r^2y-2\mu r^2y^3,\qquad y_{\rm sep}=\mu^{-1/2}S.
```

The **distinct half-rate linear carrier** used by the Pinney construction is

```math
\phi''=\frac{r^2}{4}\phi,\qquad H_{\frac12}=-\partial_u^2+\frac{r^2}{4}.
```

This is *not* the direct linear part $H_{\rm lin}=-\partial_u^2+r^2$ of the Master equation. The relationship is the symmetric-square half-rate/full-rate map of drafts 090–110.

## 2. What self-adjointness actually says [D,K]

For a real scalar Sturm–Liouville expression on $(a,b)$,

```math
\tau f=w^{-1}\big[-(pf')'+q_0f\big],\qquad p>0,\quad w>0,\quad q_0\in\mathbb R,
```

the natural Hilbert space is $\mathcal H=L^2((a,b),w(x)\,dx)$. Formal symmetry is the integration-by-parts property. Self-adjointness is the *operator equality*

```math
T=T^*,\qquad \mathrm{Dom}(T)=\mathrm{Dom}(T^*).
```

Here $T$ is a realization of $\tau$ with a specified dense domain. The last **domain equality** is essential: a real differential expression with missing or incompatible boundary conditions need not be self-adjoint.

The precise Lagrange/Green identity is

```math
\langle f,\tau g\rangle_w-\langle\tau f,g\rangle_w=[p(\bar f'g-\bar f g')]_a^b.
```

If the bracket is zero for all pairs in the chosen domain, $T$ is symmetric. Under appropriate maximality and endpoint conditions it is self-adjoint. The spectral theorem then provides a real spectrum and spectral projection-valued resolution, including a continuous spectral part where applicable. This does **not** assert that every self-adjoint Sturm–Liouville problem has a discrete eigenbasis.

### 2.1 Regular and singular endpoints

At a regular finite endpoint, a boundary condition such as real Robin, Dirichlet or Neumann is normally required. At a singular endpoint Weyl's *limit-point/limit-circle* alternative determines whether a boundary condition is needed. Limit-point endpoints require no freely selected scalar boundary condition; limit-circle endpoints require an appropriate condition to specify an extension. More general coupled boundary conditions can be expressed as maximal Lagrangian subspaces of the boundary-data symplectic space.

### 2.2 The boundary symplectic form is the actual invariant

Define the flux vector $Z_f=(f,pf')^T$. The sesquilinear boundary pairing is

```math
\mathsf B(f,g)=p(\bar f'g-\bar f g')=\bar Z_{f,2}Z_{g,1}-\bar Z_{f,1}Z_{g,2}.
```

The endpoint conditions, not the sign of a quartic discriminant or the value of a Pinney determinant, select the vanishing boundary form. A family of domain choices can yield a family of distinct self-adjoint operators for *the same* formally symmetric expression.

## 3. The original weighted problem is unitarily a constant-potential Schrödinger operator [D,V,H]

Start from the linear part of the original Master equation:

```math
x^2f_{xx}+3xf_x+(1-r^2)f=0.
```

Its weighted Sturm–Liouville expression on $x>0$ is

```math
\tau_x f=\frac1x\big[-(x^3f_x)_x+(r^2-1)xf\big],\qquad p(x)=x^3,\quad w(x)=x,\quad q_0(x)=(r^2-1)x.
```

The **exact unitary Liouville transform** is

```math
(U_cf)(u)=x f(x),\qquad x=ce^u,\qquad \int_0^\infty|f(x)|^2x\,dx=\int_{-\infty}^\infty|(U_cf)(u)|^2\,du.
```

**Theorem 3.1 [D,V].** As differential expressions, and as self-adjoint operators after transporting their domains,

```math
U_c\tau_xU_c^{-1}=-\partial_u^2+r^2=:H_{\rm lin}.
```

**Proof.** Put $\psi=xf$, so $f=\psi/x$. Then

```math
f_x=\frac{\psi_u-\psi}{x^2},\qquad (x^3f_x)_x=(x(\psi_u-\psi))_x=\psi_{uu}-\psi.
```

Substitute in $\tau_x$ and multiply by $x$ to obtain $-\psi_{uu}+r^2\psi$. The norm calculation follows because $dx=x\,du$. The scale $c$ is the origin of the logarithmic chart: it remains explicit in $x=ce^u$ and in the parity map below.

### 3.1 The weighted boundary form is preserved exactly

For $f=\psi/x$, $g=\chi/x$, direct substitution gives

```math
x^3(\bar f_x g-\bar f g_x)=\bar\psi_u\chi-\bar\psi\chi_u.
```

Thus the Liouville transformation preserves the Lagrange boundary pairing. **Self-adjointness is carried by a unitary map only when the domain is carried along**; simply changing the formula of the differential operator while forgetting the domain is insufficient.

### 3.2 Full-line spectrum and two singular endpoints

On $L^2(\mathbb R,du)$, $H_{\rm lin}=-\partial_u^2+r^2$ is essentially self-adjoint on $C_c^\infty(\mathbb R)$, with

```math
\sigma(H_{\rm lin})=[r^2,\infty)
```

purely absolutely continuous. In the original $x$ chart, the endpoints $x\downarrow0$ and $x\uparrow\infty$ correspond to $u\to-\infty,+\infty$ and are both **limit-point** for this expression. There is no separate boundary condition at the symmetry point $x=c$ when the full-line operator is retained without an inserted interface.

### 3.3 The localized nonlinear field is not a linear carrier eigenfunction

The transformed original nonlinear function is $\psi_{\rm loc}=x f_\mu=S/(2\sqrt\mu)$. It is square-integrable in $du$ and smooth, but substituting it into the **linear** operator gives

```math
H_{\rm lin}\psi_{\rm loc}=(-\partial_u^2+r^2)\frac{S}{2\sqrt\mu}=\frac{r^2}{\sqrt\mu}S^3\ne0.
```

This term is canceled only by the *nonlinear* cubic part of the Master equation. By contrast, the **half-rate** complex Pinney carrier $\Phi$ satisfies $H_{\frac12}\Phi=0$ as a formal differential equation but is not in the full-line $L^2$ domain because it grows at the ends.

Therefore neither the localized nonlinear solution nor the complex Pinney carrier furnishes a spurious zero-energy eigenfunction of the positive self-adjoint constant-potential operators. Their roles are respectively a nonlinear localized profile and a non-$L^2$ linear fundamental solution.

## 4. The symmetry point x=c is interior, not a singular endpoint [D,V,H169]

The exact interval dictionary is

| Original $x$ interval | Logarithmic $u$ interval | Role of $x=c$ |
|---|---|---|
| $(0,\infty)$ | $\mathbb R$ | ordinary interior point $u=0$ |
| $(0,c]$ | $(-\infty,0]$ | regular right endpoint if separated |
| $[c,\infty)$ | $[0,\infty)$ | regular left endpoint if separated |
| $[ce^{-L},ce^L]$, $L>0$ | $[-L,L]$ | middle of a finite interval |
| $[c,c e^L]$ | $[0,L]$ | left boundary of one half |
| $[c e^{-L},c]$ | $[-L,0]$ | right boundary of the other half |

The full Sturm–Liouville problem and the two separated half-problems have different operator domains, even though the differential coefficients are unchanged. A particular symmetry of the *measure* or *solution* does not automatically impose a new boundary condition on the unrestricted full-line operator.

### 4.1 Reflection is an exact unitary involution in the original coordinate

The reflection $\mathfrak P:\psi(u)\mapsto\psi(-u)$ becomes

```math
(\mathfrak R_cf)(x)=\frac{c^2}{x^2}f(c^2/x).
```

On $L^2((0,\infty),x\,dx)$,

```math
\mathfrak R_c^2=1,\qquad \mathfrak R_c^*=\mathfrak R_c,\qquad [\tau_x,\mathfrak R_c]=0
```

for the canonical full-line realization, because $U_c\mathfrak R_cU_c^{-1}=\mathfrak P$ and $H_{\rm lin}$ commutes with parity.

The canonical localized profile is reflection-even **in the transformed variable**:

```math
(U_cf_\mu)(u)=\frac{S}{2\sqrt\mu}=(U_cf_\mu)(-u),\qquad \mathfrak R_cf_\mu=f_\mu.
```

This does **not** say $f_\mu(c e^u)=f_\mu(c e^{-u})$ as ordinary function values: the original factor $1/x$ transforms with a weight.

## 5. Even/odd half-line boundary conditions in both coordinates [D,V,H169,H172]

For smooth functions at $u=0$, parity implies the usual conditions:

```math
\psi\ \mathrm{even}\ \Longrightarrow\ \psi_u(0)=0,\qquad \psi\ \mathrm{odd}\ \Longrightarrow\ \psi(0)=0.
```

Transport them to the original variable using $\psi=xf$:

```math
\psi_u(0)=c f(c)+c^2f_x(c).
```

Hence the precise **Neumann-for-even** and **Dirichlet-for-odd** conditions are

```math
\mathrm{even:}\quad c f_x(c)+f(c)=0,\qquad \mathrm{odd:}\quad f(c)=0.
```

For the canonical $f_\mu$ one checks $f_x(c)=-f(c)/c$. In the original unweighted $f$ chart, the even condition is therefore a **Robin condition**, not $f_x(c)=0$.

**Conclusion:** The framework's reflection gives a genuine spectral direct-sum decomposition (even/Neumann versus odd/Dirichlet), but the two half-line operators need not be isospectral. This is distinct from merely splitting a symmetric definite integral in half.

## 6. Splitting and reconnecting the two intervals: self-adjoint transmission [D,K]

For the freely connected full-line problem, continuity of $\psi$ and $\psi_u$ at $u=0$ is the natural transmission condition. In the original coordinate this is continuity of $f$ and its Sturm–Liouville flux $x^3f_x$ at $x=c$.

An illustrative **real delta interaction** at the center is defined by

```math
\psi(0+)=\psi(0-),\qquad \psi_u(0+)-\psi_u(0-)=\alpha\psi(0),\qquad \alpha\in\mathbb R.
```

This defines a self-adjoint interface for a real regular Schrödinger expression with the standard domain. In the $x$ chart its flux jump is

```math
[x^3 f_x]_{c-}^{c+}=\alpha c^2f(c).
```

A real delta interaction changes the spectrum or scattering **without breaking self-adjointness**. A *complex* interface strength in this standard model generally fails to be symmetric. The operator is then non-self-adjoint even though the differential expression on each open interval is unchanged.

The two decoupled half-lines with separate real Robin/Dirichlet conditions constitute another self-adjoint realization, usually different from the freely connected one. Splitting a measure into equal halves does not choose among these domains.

## 7. The original integral and its weighted L2 norm half-split exactly [D,V,H169]

For $\mu>0$ the original rational function has the elementary primitive

```math
\int f_\mu(x;r,c)\,dx=\frac1{r\sqrt\mu}\arctan((x/c)^r)+\mathrm{constant}.
```

Consequently

```math
\int_0^c f_\mu\,dx=\int_c^\infty f_\mu\,dx=\frac{\pi}{4r\sqrt\mu},\qquad \int_0^\infty f_\mu\,dx=\frac{\pi}{2r\sqrt\mu}.
```

This is the **half-splitting of the unweighted original integral**, independent of any choice of Sturm–Liouville operator domain.

The canonical weighted Hilbert norm has a different density but is equally split:

```math
\int_0^c x|f_\mu|^2dx=\int_c^\infty x|f_\mu|^2dx=\frac1{4r\mu},\qquad \|f_\mu\|_{L^2(xdx)}^2=\frac1{2r\mu}.
```

Proof: substitute $dx=x\,du$, $f_\mu=S/(2\sqrt\mu x)$, and integrate $S^2$ on each half-line. This is exactly the norm preserved by the Liouville unitary map of §3.

### 7.1 A full Mellin-type moment family that splits at c

For every real exponent $s>0$,

```math
M_s:=\int_0^\infty x^{s-1}f_\mu(x;r,c)^s\,dx=\frac1{r(2\sqrt\mu)^s}B\left(\frac{s}{2},\frac12\right).
```

Moreover,

```math
\int_0^c x^{s-1}f_\mu^s\,dx=\int_c^\infty x^{s-1}f_\mu^s\,dx=\frac{M_s}{2}.
```

**Proof.** The weighted integrand becomes $(2\sqrt\mu)^{-s}S(u)^sdu$, even in $u$; its full-line integral is $r^{-1}B(s/2,1/2)$. Alternatively inversion $x\mapsto c^2/x$ carries the differential measure $x^{s-1}f_\mu^s dx$ into itself. At $s=1$ this is the original integral; at $s=2$ it is the weighted SL norm.

**Important correction:** None of these integral identities, by itself, proves that $x=c$ is a reflecting/absorbing boundary for a dynamical equation. The midpoint is selected by an invariant density and reflection involution; spectral boundary or transmission conditions are a further declaration.

## 8. A precise self-adjoint finite-interval spectral control [D,V]

Take the **finite truncated interval** $x\in[ce^{-L},ce^L]$, $L>0$, with Dirichlet conditions at its two outer endpoints. After the unitary map, the linear carrier operator is

```math
H_L=-\partial_u^2+r^2,\qquad u\in[-L,L],\qquad\psi(-L)=\psi(L)=0.
```

Its exact eigenvalues are

```math
\lambda_n=r^2+\left(\frac{n\pi}{2L}\right)^2,\qquad n=1,2,\ldots.
```

For $n$ odd the eigenfunction is **even** and satisfies a Neumann condition at $u=0$; for $n$ even it is **odd** and satisfies Dirichlet at $u=0$. The two parity sectors therefore reconstruct one and the same self-adjoint full-interval spectrum **only with the correct joining rule**.

The same expression on $\mathbb R$ instead has continuous spectrum $[r^2,\infty)$ and no $L^2$ eigenfunction. The point $u=0$ has not moved, and the parameters $r,c$ have not changed: the **interval/domain** has changed, and that alone explains the different spectral claims.

## 9. What the Wronskian current measures—and what it cannot measure [D,K,C]

For an arbitrary real Sturm–Liouville equation at spectral parameter $\lambda$,

```math
-(p\psi')'+q_0\psi=\lambda w\psi,
```

define the weighted current of a complex local solution

```math
j_\psi=\mathrm{Im}(\bar\psi\,p\psi').
```

**Theorem 9.1 [D].** For real $p,w$ and possibly complex $q_0,\lambda$, its current satisfies

```math
j_\psi'=[\mathrm{Im}\,q_0-(\mathrm{Im}\,\lambda)w]|\psi|^2.
```

**Proof.** Differentiate $\bar\psi p\psi'$ and take the imaginary part. The term $p|\psi'|^2$ is real. Use $(p\psi')'=(q_0-\lambda w)\psi$ for the remaining term.

For real coefficients and **real** $\lambda$, $j_\psi$ is constant locally. This is an ODE identity, requiring **no self-adjoint operator domain**. Conversely, at complex $\lambda$ the current changes even if the chosen Sturm–Liouville operator is perfectly self-adjoint: complex $\lambda$ can simply be a resolvent parameter. Hence current conservation cannot be promoted to a binary self-adjointness test.

### 9.1 At a self-adjoint separated boundary, an actual eigenfunction has zero current

At a regular endpoint with real separated Robin condition $p\psi'=h\psi$, $h\in\mathbb R$, the current is zero there. It is also zero at Dirichlet and Neumann endpoints. If the coefficients and eigenvalue are real, the current is constant, and therefore vanishes throughout the interval for an eigenfunction satisfying such a boundary condition.

A **complex carrier** $\Phi=a e^{i\theta}$ with positive Milne current $j=a^2\theta'\ne0$ can still be constructed from two independent real solutions of the **same local ODE**, but this particular carrier generally does **not** satisfy the original real separated boundary conditions. It is not the normalized bound-state eigenfunction.

On the whole line, self-adjoint Schrödinger operators also admit **generalized scattering solutions** with nonzero constant current. They need not belong to $L^2$ and are not counterexamples to self-adjointness. The operator domain controls spectral/flux boundary pairings; the current attached to a selected carrier is extra solution data.

## 10. Explicit broken self-adjointness with no change at all to Pinney [D,C]

Consider the *same half-rate real carrier expression* on the right half-line $u>0$,

```math
H_{\frac12}=-\partial_u^2+\frac{r^2}{4}.
```

Give it a regular Robin condition at $u=0$,

```math
\psi_u(0)=h\psi(0).
```

If $h\in\mathbb R$, the corresponding standard Robin realization is self-adjoint. If $h=-1+i$, it is not symmetric. Indeed the decaying function

```math
\psi(u)=e^{(-1+i)u}
```

belongs to its natural $H^2$ domain and is an eigenfunction with **nonreal** eigenvalue

```math
H_{\frac12}\psi=\left(\frac{r^2}{4}+2i\right)\psi.
```

The differential equation on every interior point is still $\phi''=(r^2/4-\lambda)\phi$. At the **fixed local Pinney carrier parameter $\lambda=0**$ (considered independently of the boundary-selected eigenvalues), the centered positive amplitude remains

```math
a(u)=\mu^{1/4}\sqrt{\cosh(ru)},\qquad a''=\frac{r^2}{4}a+\frac{\mu r^2}{4a^3}.
```

This amplitude exists identically on the half-line for *both* real and complex Robin boundary choices. It does not “detect” the change of domain or the nonreal eigenvalue. An operator realization and a local Pinney solution occupy different levels of the mathematical dictionary.

**Corrected terminology [C]:** In this explicit setting “broken self-adjointness” means a non-self-adjoint **operator domain**. It is unrelated to spontaneous breaking of a $y\mapsto-y$ symmetry in a quartic potential. Breaking parity while keeping real admissible boundary conditions can also preserve self-adjointness.

## 11. Milne–Pinney: the exact amplitude–phase reconstruction [D,K,V]

Let $Q(u)$ be real and continuous on an interval, and choose a nonvanishing complex carrier solution

```math
\Phi''=Q(u)\Phi,\qquad \Phi=a e^{i\theta},\qquad a>0.
```

The imaginary and real parts give respectively

```math
(a^2\theta')'=0,\qquad a''=Qa+a(\theta')^2.
```

Set the conserved phase current to $j=a^2\theta'$. Then the envelope equation is

```math
a''=Qa+\frac{j^2}{a^3},\qquad\theta'=\frac{j}{a^2},\qquad k=j^2\ge0.
```

This is the Milne/Ermakov–Pinney amplitude–phase correspondence. For a positive $a$ solving Pinney with $k>0$, integrating $\theta'= \sqrt{k}/a^2$ reconstructs a zero-free complex linear solution. Its amplitude is nonlinear but its real and imaginary parts are **linear** carrier solutions.

This theorem is conditional: it requires real $Q$, positive amplitude, a choice of phase-current sign, an integration constant and a chart without zeros. It is not an equivalence between all self-adjoint spectral realizations and all Pinney boundary-value problems.

### 11.1 The complex logarithmic derivative is the exact coupled Riccati system

Write

```math
Z(u)=\frac{\Phi'}{\Phi}=(\mathrm{Log}\,\Phi)'=H(u)+iB(u),\qquad H=\frac{a'}a,\quad B=\frac{j}{a^2}.
```

The complex Riccati identity $Z'+Z^2=Q$ splits into

```math
H'+H^2-B^2=Q,\qquad B'+2HB=0.
```

Equivalently,

```math
H'=Q-H^2+B^2,\qquad B'=-2HB.
```

The *imaginary Riccati component is the Milne phase current density*, whereas the real component is the envelope's logarithmic growth rate. These equations follow from a **linear carrier** and hold irrespective of whether a selected spectral domain is self-adjoint.

## 12. The canonical complex solution, Gudermannian and integral phase [D,V,H112]

For the framework's centered positive Pinney envelope define

```math
\Phi(u)=\mu^{1/4}\left[\cosh\left(\frac{ru}{2}\right)+i\sinh\left(\frac{ru}{2}\right)\right].
```

It satisfies

```math
\Phi''=\frac{r^2}{4}\Phi,\qquad |\Phi|^2=\sqrt\mu\cosh(ru)=a^2,\qquad j=\mathrm{Im}(\bar\Phi\Phi')=\frac{r\sqrt\mu}{2}.
```

Its phase, logarithmic derivative and Riccati identity are

```math
\theta(u)=\arg\Phi=\frac12\mathrm{gd}(ru)=\arctan(e^{ru})-\frac\pi4,\qquad \theta'=\frac r2S.
```

```math
\frac{\Phi'}{\Phi}=\frac r2(W+iS),\qquad\left(\frac{\Phi'}{\Phi}\right)'+\left(\frac{\Phi'}{\Phi}\right)^2=\frac{r^2}{4}.
```

This supplies the *same explicit* $S,W$ as the original framework. Its Riccati components lie on a circle,

```math
H=\frac r2W,\qquad B=\frac r2S,\qquad H^2+B^2=\frac{r^2}{4}.
```

The circular relation is a **particular centered, zero-auxiliary-energy identity**, not a condition for self-adjointness of an arbitrary Sturm–Liouville realization.

### 12.1 The exact original integral is a Milne phase increment

Since $x=ce^u$,

```math
f_\mu(x;r,c)\,dx=\frac{S}{2\sqrt\mu}\,du=\frac1{r\sqrt\mu}\,d\theta.
```

Thus the ordinary integral is an **integrated phase current divided by the fixed normalization**:

```math
\int_{x_1}^{x_2}f_\mu(x;r,c)\,dx=\frac{\theta(\ln(x_2/c))-\theta(\ln(x_1/c))}{r\sqrt\mu}.
```

At the midpoint $x=c$ ($u=0$), $\theta=0$; at the two improper endpoints,

```math
\theta(-\infty)=-\frac\pi4,\qquad\theta(0)=0,\qquad\theta(+\infty)=\frac\pi4.
```

The two phase increments are equal to $\pi/4$, reproducing the exact half integrals. This is a genuine **arithmetical identity between the original half-integral and the selected Milne phase**, not a spectral quantization statement.

## 13. Phase increments and interval quantization are different constructions [D,K]

A positive Milne amplitude can be used to build **real** solutions of the same linear equation:

```math
\psi_{\delta}(u)=a(u)\sin(\theta(u)+\delta).
```

For a fixed real spectral parameter and selected amplitude, imposing Dirichlet at two regular endpoints $u_-,u_+$ requires a phase difference

```math
\theta(u_+)-\theta(u_-)=n\pi,\qquad n\in\mathbb Z_{\ge1}
```

whenever a nonzero Dirichlet eigenfunction is obtained with monotone $\theta$ and appropriate phase choice. However $a$ and $\theta$ typically **depend on the spectral parameter**: the equation is an implicit quantization rule, not a new eigenvalue formula without that dependence.

For the *canonical half-rate carrier at spectral value zero*, the phase difference across all $\mathbb R$ is only $\pi/2$. It cannot satisfy a positive-integer Dirichlet phase condition across a finite pair of endpoints. This agrees with the fact that the constant-potential half-rate operator has spectral bottom $r^2/4>0$ and no zero-energy eigenfunction on such a Dirichlet interval.

For an oscillatory carrier $Q=-\kappa^2$ with $\kappa>0$, choose $a=1$, $\theta=\kappa u$, $k=\kappa^2$. Dirichlet on $[-L,L]$ instead gives

```math
2\kappa L=n\pi,\qquad\lambda_n=\frac{r^2}{4}+\left(\frac{n\pi}{2L}\right)^2
```

for the half-rate Schrödinger operator $H_{\frac12}$, as expected. **Self-adjointness** entered through the boundary conditions, not through the positive Pinney coefficient $k$.

## 14. Riccati projectivization, Schwarzian and the Cayley circle [D,V]

For the half-rate linear equation $\phi''=r^2\phi/4$ choose

```math
\phi_+=e^{ru/2},\qquad\phi_-=e^{-ru/2},\qquad t(u)=\frac{\phi_+}{\phi_-}=e^{ru}=(x/c)^r.
```

The ratio $t$ is a coordinate on the real projective solution line, while its Schwarzian is

```math
\{t,u\}=-\frac{r^2}{2}.
```

Its Cayley transform gives exactly the canonical complex Riccati circle:

```math
\frac{t+i}{t-i}=\frac{t^2-1+2it}{t^2+1}=W+iS,\qquad \frac{\Phi'}{\Phi}=\frac r2\frac{t+i}{t-i}.
```

This is the precise **projective Rosetta Stone**: a linear rank-two carrier supplies a projective ratio; a Möbius/Cayley transformation produces the circle chart; its logarithmic derivative is Riccati; integrating its imaginary part gives half the Gudermannian and the original primitive. This is an exact algebraic web, with the half-rate $r/2$ tracked throughout.

Riccati equations are *locally* linearizable by an associated rank-two system. A particular Riccati solution can have poles when the denominator of its projective chart vanishes; global monodromy and real/complex boundary conditions are independent data. A Riccati coordinate is not itself an invariant test of self-adjointness.

## 15. The Hopf fibration is related to projectivization, but is not identical to a scalar Riccati equation [D,K,H170,H176]

The abstract projectivization of a nonzero complex vector $(z_1,z_2)\in\mathbb C^2$ is a point of $\mathbb{CP}^1$. Restrict to the unit sphere $|z_1|^2+|z_2|^2=1$ and quotient by common phase $U(1)$ to obtain the Hopf fibration

```math
S^1\longrightarrow S^3\longrightarrow\mathbb{CP}^1\cong S^2.
```

For the *real positive* half-rate carrier vector define the explicitly normalized spinor

```math
\eta(u)=\frac{(e^{ru/2},e^{-ru/2})}{\sqrt{2\cosh(ru)}}=\left(\sqrt{\frac{1+W}{2}},\sqrt{\frac{1-W}{2}}\right).
```

It satisfies

```math
|\eta_1|^2+|\eta_2|^2=1,\quad \frac{\eta_1}{\eta_2}=e^{ru}=t,\quad |\eta_1|^2-|\eta_2|^2=W,\quad 2\eta_1\eta_2=S.
```

Thus $W,S$ are *precisely* the Bloch/Hopf-base coordinates for this normalized projective curve. Multiplying $\eta$ by an arbitrary common phase produces its full Hopf fiber. This makes the relation concrete rather than metaphorical.

**Boundary of the identification:** The complex scalar $\Phi=a e^{i\theta}$ of §12 has its own polar $U(1)$ phase and its own Wronskian current. That scalar phase is not **automatically** the vertical Hopf-bundle phase of the normalized *two-component* vector $\eta$. The Riccati ratio $t$ lives on the Hopf **base**; the Hopf fiber appears only after the normalized lift and its common phase have been specified.

## 16. The canonical Pinney potential is not a Higgs-like double well [D,V,C]

For a **constant real carrier coefficient** $Q_0$, the positive-amplitude Pinney equation

```math
a''=Q_0a+ka^{-3},\qquad a>0
```

has conserved Hamiltonian energy

```math
\mathcal E_a=\frac12(a')^2+V_{\rm EP}(a),\qquad V_{\rm EP}(a)=-\frac{Q_0}{2}a^2+\frac{k}{2a^2}.
```

The physical terminology here is only a name for the **graph of a mathematical potential**. The sign of $Q_0$, the sign of $k$, and the permitted half-line $a>0$ determine the shape.

### 16.1 Positive inverted carrier Q0>0, positive Pinney strength k>0

This is the **canonical framework regime**:

```math
Q_0=\frac{r^2}{4}>0,\qquad k=\frac{\mu r^2}{4}>0,\qquad V_{\rm EP}(a)=-\frac{r^2a^2}{8}+\frac{\mu r^2}{8a^2}.
```

Its derivative is strictly negative:

```math
V_{\rm EP}'(a)=-Q_0a-ka^{-3}<0\qquad(a>0).
```

It diverges to $+\infty$ near the forbidden amplitude $a=0$ and to $-\infty$ as $a\to+\infty$; **there is no local minimum and no double well**. The centered solution $a=\mu^{1/4}\sqrt{\cosh(ru)}$ has a positive *turning point* at $u=0$ (its kinetic energy vanishes there), not a stable equilibrium of the effective one-dimensional potential.

### 16.2 Oscillatory carrier Q0=-omega²<0, k>0: the centrifugal/isotonic well

With $Q_0=-\omega^2$, $\omega>0$,

```math
V_{\rm iso}(a)=\frac{\omega^2a^2}{2}+\frac{k}{2a^2}.
```

This has a **single** positive minimum,

```math
a_0=(k/\omega^2)^{1/4},\qquad V_{\rm iso}(a_0)=\omega\sqrt{k},\qquad V_{\rm iso}''(a_0)=4\omega^2.
```

Small oscillations around that minimum have frequency $2\omega$. If the signed coordinate $a\ne0$ is artificially allowed, the singular barrier divides two disconnected half-lines with one minimum each. That appearance is **not** a smooth Higgs double well: trajectories cannot cross $a=0$ at finite positive $k$, and positive Pinney amplitudes live on only one side.

### 16.3 Other signs

At $k=0$, Pinney reduces to the linear carrier equation and the inverse-square barrier disappears. At $k<0$, the singular term is attractive; positivity can fail, and finite-time collapse to $a=0$ may occur. At $Q_0>0,k<0$ there is a **local maximum**, not a confining double minimum. Thus neither nonlinearity alone nor self-adjointness of an associated SL operator dictates the effective-well topology.

## 17. The distinct smooth Duffing/Higgs-like double well [D,V,C]

The original cubic Master equation for the **signed** field $y$,

```math
y''=r^2y-2\mu r^2y^3,
```

has a different mechanical energy function

```math
E_D=\frac12(y')^2+V_D(y),\qquad V_D(y)=-\frac{r^2}{2}y^2+\frac{\mu r^2}{2}y^4.
```

Its critical points are

```math
y=0\quad(\mathrm{maximum}),\qquad y_\pm=\pm(2\mu)^{-1/2}\quad(\mathrm{minima}),\qquad V_D(y_\pm)=-\frac{r^2}{8\mu}.
```

This is indeed a **smooth symmetric quartic double well** on the entire signed real line, and the familiar “Higgs-like” label can be used as a *formal potential-shape analogy*. The separatrix

```math
y_{\rm sep}(u)=\mu^{-1/2}\mathrm{sech}(ru)
```

is homoclinic to the unstable critical point $y=0$ at energy $E_D=0$; it is **not** a tunneling trajectory joining the two minima. There is also a negative homoclinic branch.

The map $y=a^{-2}$ from the positive canonical Pinney amplitude produces only $y>0$ and only selected zero-energy branches of the signed cubic Master system; it does not extend as a global dynamical equivalence between the two potential landscapes. Neither potential shape determines self-adjointness of a spectral operator, and a negative direction of a self-adjoint variational Hessian is not “broken self-adjointness”.

## 18. The Pinney energy curve is a quartic—and its time evolution descends to a conic [D,V]

This section distinguishes **three algebraic quartics** that have been conflated in informal descriptions: (i) the square of the Pinney Gram quadratic, (ii) the Pinney **energy** quartic, and (iii) the cubic Master/Duffing energy quartic.

For constant $Q_0$ and fixed Pinney energy $\mathcal E_a$, solve the first integral of §16:

```math
(a')^2=2\mathcal E_a+Q_0a^2-ka^{-2}.
```

Introduce the auxiliary algebraic coordinate $Y=aa'$. Then

```math
Y^2=Q_0a^4+2\mathcal E_a a^2-k.
```

Homogenizing yields the **smooth, generically genus-one Pinney energy quartic**

```math
F_{\rm EP}(A,Z)=Q_0A^4+2\mathcal E_a A^2Z^2-kZ^4.
```

### 18.1 Exact binary quartic I, J and discriminant

Use the repository's **raw** quartic normalization $I=12af-3bd+c_2^2$, $J=72ac_2f+9bc_2d-27ad^2-27fb^2-2c_2^3$, $\Delta=(4I^3-J^2)/27$.

**Theorem 18.1 [D,V].** The Pinney energy quartic has

```math
I_{\rm EP}=4\mathcal E_a^2-12Q_0k,\qquad J_{\rm EP}=-16\mathcal E_a^3-144Q_0k\mathcal E_a.
```

```math
\Delta_{\rm EP}=-256Q_0k(\mathcal E_a^2+Q_0k)^2.
```

Where $\Delta_{\rm EP}\ne0$, its complex elliptic modulus is

```math
j_{\rm EP}=-64\frac{(\mathcal E_a^2-3Q_0k)^3}{Q_0k(\mathcal E_a^2+Q_0k)^2}.
```

**Proof.** The even quartic coefficients are $a=Q_0$, $c_2=2\mathcal E_a$, $f=-k$, $b=d=0$. Substitute into $I=c_2^2+12af$ and $J=2c_2(36af-c_2^2)$; factor the discriminant and simplify $j=256I^3/\Delta$.

For the **canonical** $Q_0=r^2/4>0$, $k=\mu r^2/4>0$, and centered Pinney energy $\mathcal E_a=0$, the quartic is smooth:

```math
F_{\rm EP,0}(A,Z)=\frac{r^2}{4}(A^4-\mu Z^4),\qquad \Delta_{\rm EP,0}\ne0,\qquad J_{\rm EP,0}=0,\qquad j_{\rm EP,0}=1728.
```

This is an exact nontrivial **harmonic elliptic quartic** attached to the Pinney energy representation, even though the framework's **Master separatrix energy quartic** is singular. Equal source profiles do not identify those different algebraic curves.

### 18.2 Why the Pinney motion is nevertheless elementary

Set $J=a^2>0$ (the envelope variable, not the raw quartic invariant $J_{\rm EP}$). Then $J'=2aa'=2Y$ and the energy curve descends to

```math
Y^2=Q_0J^2+2\mathcal E_a J-k.
```

This is a **conic**, hence genus zero when smooth. The map

```math
(a,Y)\longmapsto(J,Y)=(a^2,Y)
```

is a degree-two algebraic quotient of the generic smooth elliptic quartic by the involution $(a,Y)\mapsto(-a,Y)$.

The distinguished **physical/mathematical time differential** descends as

```math
du=\frac{da}{a'}=\frac{a\,da}{Y}=\frac{dJ}{2Y}.
```

The last expression is a rational/conic quadrature, giving exponential or trigonometric Pinney envelopes. Thus *smooth elliptic quartic geometry does not force elliptic-function time evolution when the marked differential descends through a genus-zero quotient*. This is a fundamental “curve versus differential” example within the framework.

The ordinary holomorphic elliptic differential $da/Y$ is **not** the physical time differential $a\,da/Y$. Interchanging them silently produces a false assertion of elliptic time dependence.

### 18.3 Canonical conic and its resolution/scale dependence

For the centered envelope $J=\sqrt\mu\cosh(ru)$, we have

```math
Q_0=\frac{r^2}{4},\quad k=\frac{\mu r^2}{4},\quad\mathcal E_a=0,\quad J'^2=r^2(J^2-\mu).
```

Its two conic branches $J=\sqrt\mu\cosh[r(u-u_0)]$ are explicitly elementary. Translating $u$ corresponds to changing the center parameter of the envelope; to stay centered at the original $x=c$, take $u_0=0$.

### 18.4 Two further quartics have incompatible discriminant types

The **Gram-square quartic** $(AX^2+2CXZ+BZ^2)^2$ has discriminant zero **for every Gram determinant**; it is not $F_{\rm EP}$. The **normalized Master energy quartic**

```math
F_{\rm M}(Z,T)=-Z^4+Z^2T^2+eT^4,\qquad e=\mu\varepsilon_N/r^2,
```

has

```math
I_{\rm M}=1-12e,\qquad J_{\rm M}=-2-72e,\qquad\Delta_{\rm M}=-16e(1+4e)^2.
```

It is singular at the canonical homoclinic energy $e=0$ and generally elliptic at finite $e\ne0,-1/4$. Therefore the **same canonical solution** supports: a singular Gram-square quartic, a smooth $j=1728$ Pinney-energy quartic, and a singular Master separatrix quartic. None is “the universal quartic” of self-adjointness.

## 19. Real-branch implications of the Pinney energy quartic [D,V]

The sign regimes have a concrete root interpretation.

**Canonical inverted carrier:** $Q_0>0$, $k>0$ imply

```math
\Delta_{\rm EP}=-256Q_0k(\mathcal E_a^2+Q_0k)^2<0
```

for every real $\mathcal E_a$. Thus the corresponding *projective complex* quartic is smooth at every real energy, although the admissible real trajectory $a(u)>0$ has a turning point and grows without bound in both temporal directions. No double-well bifurcation is marked by its discriminant.

**Stable centrifugal carrier:** with $Q_0=-\omega^2<0$ and $k>0$, the energy minimum $\mathcal E_a=\omega\sqrt k$ is exactly the real degeneracy locus $\mathcal E_a^2+Q_0k=0$. At energies above this minimum the amplitude oscillates between two positive turning radii; the inverse-square barrier still prevents crossing zero. The discriminant degeneration records an **equilibrium energy/root collision**, not non-self-adjointness of the associated linear carrier.

**Distinguish amplitude sign:** Positive Milne amplitude $a>0$ occupies one connected component of a signed-coordinate quartic picture. Extending the algebraic coordinate to negative $a$ does not create an ordinary smooth double-well dynamical crossing through the inverse-square singularity.

## 20. “Tunneling Sturm–Liouville” is genuine, but does not mean loss of self-adjointness [D,K,C]

Consider a separate, explicitly chosen **self-adjoint** one-dimensional Schrödinger operator on the whole spatial line $\xi\in\mathbb R$:

```math
H_{\rm bar}=-\frac{d^2}{d\xi^2}+V_{\rm bar}(\xi),\quad V_{\rm bar}=V_0\,\mathbf 1_{(0,L)}(\xi),\quad V_0>0,\quad L>0.
```

Here $V_0>0$ is the barrier height. Let the scattering energy satisfy $0<E<V_0$ and put

```math
k_{\rm ext}=\sqrt E,\qquad\kappa=\sqrt{V_0-E}>0.
```

Inside the barrier the linear carrier is

```math
\psi_{\xi\xi}=\kappa^2\psi,\qquad \psi=Ae^{\kappa\xi}+Be^{-\kappa\xi}.
```

Thus the local carrier is **hyperbolic**, but the full Schrödinger operator is still self-adjoint on its natural $H^2(\mathbb R)$ domain (the potential is real and bounded).

### 20.1 An explicit positive Pinney amplitude inside the forbidden interval

Choose the local complex carrier

```math
\Phi_{\rm bar}(\xi)=\cosh(\kappa\xi)+i\sinh(\kappa\xi).
```

Then

```math
|\Phi_{\rm bar}|^2=\cosh(2\kappa\xi),\qquad j_{\rm bar}=\kappa,\qquad a_{\rm bar}''=\kappa^2a_{\rm bar}+\kappa^2a_{\rm bar}^{-3}.
```

This is the same *mathematical Pinney normal form* as the canonical framework with $r=2\kappa$ and $\mu=1$ after the local coordinate identification $u=\xi$. The barrier region, however, has its own $V_0,E,L$ and scattering boundary matching; the equality of local ODEs does not imply equality of physical systems or spectra.

### 20.2 Exact transfer matrix and transmission coefficient

The interior Cauchy-data transfer matrix is

```math
\binom{\psi(L)}{\psi'(L)}=\begin{pmatrix}\cosh(\kappa L)&\sinh(\kappa L)/\kappa\\\kappa\sinh(\kappa L)&\cosh(\kappa L)\end{pmatrix}\binom{\psi(0)}{\psi'(0)}.
```

Its determinant is exactly one, preserving the Wronskian/symplectic current. Matching to plane waves on the exterior regions yields the classical real-barrier transmission probability

```math
\mathsf T(E)=\left[1+\frac{V_0^2\sinh^2(\kappa L)}{4E(V_0-E)}\right]^{-1}.
```

For a thick barrier, $\mathsf T(E)$ is exponentially small but nonzero. **The existence of this tunneling effect is completely compatible with self-adjointness**. It depends on *global matching to exterior oscillatory modes*, not merely on the local Pinney amplitude or its invariant level.

The word “tunneling” is therefore legitimate only after a concrete spectral barrier, energy range and matching problem are specified. There is no universal identity “EP equals broken-self-adjoint tunneling SL”.

## 21. Broken parity, negative modes, complex spectra and tunnels are four different phenomena [C]

The following four mathematically distinct constructions should never be collapsed:

1. **Parity or symmetry breaking:** replace an even real potential by an asymmetric real potential or impose different real boundary choices. The associated operator can remain self-adjoint.
2. **Instability/negative Hessian eigenvalue:** a self-adjoint Hessian may possess negative spectrum, indicating a negative second variation. This does **not** destroy self-adjointness.
3. **Non-self-adjoint spectral realization:** introduce complex coefficients or boundary/interface conditions that violate the symmetric boundary form; complex eigenvalues and nonnormality can arise.
4. **Barrier tunneling:** in a *real self-adjoint* operator, evanescent modes in classically forbidden regions couple through flux-preserving matching to oscillatory modes.

The canonical positive Pinney inverse-square wall is a barrier in **amplitude configuration space**. The double-well Duffing potential is a function of a **signed field variable**. The spectral barrier of §20 is a potential in an **independent spatial coordinate**. Their graphs can resemble one another under transformations, but their variable types and boundary conditions differ.

## 22. Weyl–Titchmarsh boundary data: the exact spectral interface at u=0 [D,K,H169]

For a real Schrödinger expression $H=-\partial_u^2+V(u)$ on the full line, assume the left/right endpoints are limit-point. For a spectral value $\lambda$ away from half-line spectral poles, let $\psi_-(u;\lambda)$ be the solution square integrable as $u\to-\infty$, and $\psi_+(u;\lambda)$ the solution square integrable as $u\to+\infty$, both unique up to scale.

Their Wronskian is independent of $u$ and gives the full-line bound-state matching equation

```math
\mathscr W(\lambda)=\psi_-(0;\lambda)\psi_+'(0;\lambda)-\psi_-'(0;\lambda)\psi_+(0;\lambda).
```

**Theorem 22.1 [D,H169] (reflection factorization).** If $V(u)=V(-u)$ and the two Weyl solutions are normalized compatibly by reflection, $\psi_-(u;\lambda)=\psi_+(-u;\lambda)$, then

```math
\mathscr W(\lambda)=2\psi_+(0;\lambda)\psi_+'(0;\lambda).
```

**Proof.** Reflection gives $\psi_-(0)=\psi_+(0)$ and $\psi_-'(0)=-\psi_+'(0)$. Substitute into the Wronskian formula.

A genuine full-line $L^2$ eigenvalue therefore satisfies at least one of the two half-line conditions

```math
\psi_+(0;\lambda)=0\quad(\mathrm{odd/Dirichlet}),\qquad \psi_+'(0;\lambda)=0\quad(\mathrm{even/Neumann}).
```

This factorization is **spectral**; it requires the relevant Weyl solutions and their endpoint behavior. It should not be confused with the *integral's* equal halves, although both use the same reflection involution.

### 22.1 The boundary logarithmic derivative is a spectral Riccati coordinate

If $\psi_+(0;\lambda)\ne0$, define the right half-line Weyl function

```math
m_+(\lambda)=\frac{\psi_+'(0;\lambda)}{\psi_+(0;\lambda)}.
```

This is the boundary value of a logarithmic derivative of the Weyl solution and satisfies an interior Riccati equation. For an appropriate self-adjoint half-line realization its dependence on $\lambda$ is a Herglotz/Nevanlinna function (with the sign convention determined by which endpoint orientation is chosen); this analytic positivity, unlike local Pinney current conservation, retains substantive spectral-domain information.

For the canonical full-rate carrier $H_{\rm lin}=-\partial_u^2+r^2$, choose the square root $\kappa_\lambda=\sqrt{r^2-\lambda}$ with $\mathrm{Re}\kappa_\lambda>0$. Then

```math
\psi_+(u;\lambda)=e^{-\kappa_\lambda u},\qquad m_+(\lambda)=-\kappa_\lambda.
```

This gives an exact, parameter-dependent *boundary* Riccati datum; the constant $r$ sets the spectral threshold and the scale $c$ sets the coordinate location $x=c$ of the boundary chart.

### 22.2 An explicit self-adjoint point interaction shifts the spectrum

For the full-line constant carrier $H_{\rm lin}$, add the real delta jump of §6 with strength $\alpha<0$. The even bound state is

```math
\psi_\alpha(u)=e^{\alpha|u|/2},\qquad \lambda_\alpha=r^2-\frac{\alpha^2}{4}.
```

The operator with this real transmission condition is self-adjoint and has one simple discrete eigenvalue below the continuum $[r^2,\infty)$, even though the **local** differential expression and its constant-carrier Pinney construction away from $u=0$ are unchanged. This is a direct counterexample to the proposal that the local Pinney amplitude uniquely determines the spectral bound states or self-adjoint extension.

## 23. The canonical Master Hessian: parity, negative mode and zero mode [D,V,H172]

Linearize the *original nonlinear Master equation* around $y_{\rm sep}=\mu^{-1/2}S$. In the $u$ variable the self-adjoint full-line differential expression is

```math
H_{\rm M}=-\partial_u^2+r^2-6r^2S^2.
```

It is a Pöschl–Teller well of order two, not the constant-potential carrier of §3 and not the half-rate Pinney Hessian of draft 110.

**Theorem 23.1 [D,V,H172].** Two exact $L^2(\mathbb R)$ eigenfunctions are

```math
H_{\rm M}(S^2)=-3r^2S^2,\qquad H_{\rm M}(SW)=0.
```

The first is **even** and satisfies Neumann at $u=0$; the second is **odd** and satisfies Dirichlet there. Their eigenvalues are $-3r^2$ and $0$, and the essential spectrum is $[r^2,\infty)$.

**Proof.** Differentiate $S^2$ and $SW$ twice using $S'=-rSW$, $W'=rS^2$; substitute into the differential expression. These are the standard two square-integrable bound states of the order-two Pöschl–Teller well; its factorization and oscillation theorem exclude additional bound states.

The **negative eigenvalue does not break self-adjointness**. It identifies a negative mode of this specified real self-adjoint Hessian (for an appropriately interpreted second variation); the translation-related zero mode records a continuous family of centered profiles. This is precisely the even/odd half-line split of the archived H172 analysis.

### 23.1 The distinct Pinney Hessian

On the canonical Pinney envelope $a=\mu^{1/4}\sqrt R$, its variational Hessian is

```math
H_{\rm EP}=-\partial_u^2+\frac{r^2}{4}-\frac{3r^2}{4}S^2.
```

This half-integer Pöschl–Teller operator is nonnegative on its full-line $L^2$ realization and has a zero ground mode $S^{1/2}$. The Master operator has an additional negative mode and a different threshold. The reciprocal **solution** map $y=a^{-2}$ is not a unitary transformation of the two unconstrained Hessian operators.

## 24. Catenoid and helicoid: a third, geometrically derived Jacobi operator [D,V,K,H421,H424]

Introduce the independent surface coordinate $v$ with period $2\pi/r$, and the complex conformal coordinate $\zeta=u+iv$. The canonical catenoid immersion is

```math
X(u,v)=\left(r^{-1}R\cos(rv),\,r^{-1}R\sin(rv),\,u\right),\qquad R=\cosh(ru).
```

Its induced metric, Gaussian curvature and squared second-fundamental-form norm are

```math
g_C=R^2(du^2+dv^2),\qquad K_C=-r^2S^4,\qquad |A_C|^2=-2K_C=2r^2S^4.
```

The normal Jacobi differential expression of the minimal immersion is $J_C=\Delta_{g_C}+|A_C|^2$ in one common sign convention. Since the conformal Laplacian is $\Delta_{g_C}=R^{-2}(\partial_u^2+\partial_v^2)$,

```math
R^2J_C=\partial_u^2+\partial_v^2+2r^2S^2.
```

On an angular Fourier mode $e^{inrv}$ ($n\in\mathbb Z$), the zero-Jacobi equation reduces to

```math
\left[-\partial_u^2-2r^2S^2\right]h_n=-(nr)^2h_n.
```

**This is the order-one Pöschl–Teller well**, distinct from both the original Master Hessian (order two) and the Pinney Hessian (half-integer order). As one exact check,

```math
\left[-\partial_u^2-2r^2S^2\right]S=-r^2S.
```

The local catenoid and helicoid are minimal Bonnet associates, sharing the same induced metric and pointwise $|A|^2$ after the appropriate local identification. Therefore they have the same **local** Jacobi differential expression in matching conformal coordinates, while their global parameter domains differ: a catenoid has a periodic angular coordinate, whereas a complete helicoid is simply connected with an unwrapped angular direction.

**Consequently their global spectral domains need not be the same.** The formal differential expression, its allowed Fourier modes, the $L^2$ surface measure $R^2du\,dv$, completeness and the boundary/period conditions must all be declared before asserting a spectral equivalence.

## 25. The Pinney complex phase reconstructs the catenoid and Gauss-sphere conformal factors [D,V]

The exact canonical Pinney amplitude and phase of §12 are

```math
a^2=\sqrt\mu R,\qquad \theta'=\frac r2S,\qquad j=a^2\theta'=\frac{r\sqrt\mu}{2}.
```

Thus the catenoid conformal metric is

```math
g_C=\frac{a^4}{\mu}|d\zeta|^2.
```

The stereographic Gauss map of the catenoid may be taken as $G(\zeta)=-e^{r\zeta}$. The pulled-back round sphere metric (the third fundamental form) is

```math
g_G=\frac{4|G_\zeta|^2}{(1+|G|^2)^2}|d\zeta|^2=r^2S^2|d\zeta|^2.
```

**Theorem 25.1 [D,V] (Pinney phase–Gauss metric identity).**

```math
g_G=4(\theta')^2|d\zeta|^2=\frac{4j^2}{a^4}|d\zeta|^2=\frac{\mu r^2}{a^4}|d\zeta|^2.
```

**Proof.** From the positive Pinney amplitude $a^4=\mu R^2$, and $S^2=1/R^2$, obtain $\mu r^2/a^4=r^2S^2$. From the Milne phase $\theta'=(r/2)S$ obtain $4\theta'^2=r^2S^2$. The Gauss stereographic formula gives the same coefficient directly.

This is an exact *two-metric* relation between the minimal immersion, the selected positive Pinney envelope and its Gudermannian phase. It explains why the curvature and Riccati structures appear in the same foundational layer. It is **not** a claim that the catenoid and sphere are isometric or that every Pinney solution reconstructs this particular minimal immersion.

### 25.1 The symmetry midpoint is also the Gauss-sphere equator

Let $\phi=rv$ and $W=\tanh(ru)$. The Gauss-sphere area form is

```math
\omega_G=r^2S^2\,du\wedge dv=dW\wedge d\phi.
```

For $v$ of period $2\pi/r$,

```math
\int_{-\infty}^0\int_0^{2\pi/r}\omega_G=2\pi,\qquad \int_0^\infty\int_0^{2\pi/r}\omega_G=2\pi.
```

Thus $u=0$ is the sphere's equator and separates two equal-area hemispheres. For a standard Hopf connection with curvature $F_H=\tfrac12\omega_G$, each hemisphere has flux $\pi$. These **geometric** halves and the original function's integral halves share the same logarithmic reflection, but they are integrals of **different measures** and with different normalizations: $\pi$ for Hopf curvature, $\pi/(4r\sqrt\mu)$ for each original half-integral, and $1/(4r\mu)$ for each weighted-norm half.

### 25.2 A harmonic quartic is attached to the catenoid, but it is not a spectral boundary condition

From the two fundamental forms, draft 050 constructs a separate binary quartic with

```math
I_{\rm surf}=-12r^2S^4,\qquad J_{\rm surf}=0,\qquad j_{\rm surf}=1728.
```

This abstract complex elliptic modulus coincides numerically with the **centered Pinney energy quartic** $j_{\rm EP}=1728$ from §18. That is an equality of a selected invariant after two different constructions. It does not supply a canonical identification of their marked differentials, surface periods, real ovals or self-adjoint boundary conditions.

## 26. Riemann minimal examples: elliptic Weierstrass periods and operator domains [K,H,O]

Riemann's classical minimal examples are constructed from selected meromorphic Weierstrass–Enneper data on elliptic curves with real period-closing conditions. A genus-one curve and its $j$ invariant may encode the complex structure of the underlying data, but reconstructing the immersion also requires a Gauss map, height differential, integration paths, real periods and geometric identification of the ends.

The associated surface Jacobi operator remains an intrinsic/extrinsic geometric differential expression built from $\Delta_g+|A|^2$. In a quotient by a geometric period one must specify periodic, antiperiodic or Floquet boundary data; on the complete noncompact surface, its $L^2$ realization and end behavior matter. A degeneration of an **elliptic curve** toward a catenoid or helicoid does not automatically identify the global Jacobi spectra, because the domains, topology and limiting one-forms can also degenerate.

The projective Riccati ratio, Milne phase, Gauss map and Hopf fibration are all available as **distinct** mathematical objects once the correct linear equation, meromorphic differential or bundle has been supplied. Their recurring appearance is mathematically meaningful; their numerical invariants alone do not classify the complete surface or its spectral operator.

## 27. The half-split moment hierarchy is a Beta CDF and a Dirichlet minimizer [D,V,H169]

The complete positive-moment family introduced in §7 is more structured than equal halves alone. For $s>0$, define

```math
w_s(x)=x^{s-1}f_\mu(x;r,c)^s,\qquad M_s=\int_0^\infty w_s(x)\,dx.
```

Its cumulative function is $C_s(x)=M_s^{-1}\int_0^xw_s(t)\,dt$. The canonical logistic coordinate is

```math
P(u)=\frac{1+W}{2}=\frac{(x/c)^{2r}}{1+(x/c)^{2r}}.
```

**Theorem 27.1 [D,V] (symmetric Beta coordinate).**

```math
C_s(x)=I_{P(u)}\left(\frac{s}{2},\frac{s}{2}\right),\qquad C_s(c)=\frac12,\qquad C_s(c^2/x)=1-C_s(x).
```

Here $I_P(a,b)$ is the regularized incomplete Beta function.

**Proof.** In the logarithmic coordinate $w_s(x)\,dx=(2\sqrt\mu)^{-s}S^sdu$. With $P=(1+W)/2$ one has $P_u=2rP(1-P)$ and $S^2=4P(1-P)$; therefore

```math
S^sdu=\frac{2^{s-1}}rP^{s/2-1}(1-P)^{s/2-1}dP.
```

Normalize by the complete symmetric Beta integral. This proves the CDF formula and midpoint symmetry. The two most important cases are

```math
s=1:\quad C_1(x)=\frac2\pi\arctan((x/c)^r),\qquad w_1=f_\mu.
```

```math
s=2:\quad C_2(x)=P=\frac{1+W}{2},\qquad w_2=xf_\mu^2.
```

Thus the original **arctangent primitive** and the canonical **logistic coordinate** are two members of a single Beta-moment hierarchy. This connects the original integral, the weighted SL Hilbert measure, and the Hopf/Gauss-sphere latitude coordinate without identifying their uses.

### 27.1 The weighted Dirichlet principle has the same midpoint

For an absolutely continuous $F$ with $F(0)=0$, $F(\infty)=1$, define the quadratic energy

```math
\mathcal D_s[F]=\int_0^\infty\frac{F_x^2}{w_s(x)}\,dx.
```

**Theorem 27.2 [D,V,H169].** Under the standard finite-energy endpoint assumptions,

```math
\mathcal D_s[F]\ge\frac1{M_s}
```

with equality exactly at $F=C_s$.

**Proof.** The Cauchy–Schwarz inequality gives

```math
1=\left(\int_0^\infty F_x\,dx\right)^2\le\left(\int_0^\infty\frac{F_x^2}{w_s}\,dx\right)\left(\int_0^\infty w_s\,dx\right)=M_s\mathcal D_s[F].
```

Equality requires $F_x$ proportional to $w_s$, with the normalization fixing $F=C_s$ uniquely. If an interface value $b=F(c)$ is prescribed, the half-interval energies satisfy

```math
\mathcal D_s^-\ge\frac{b^2}{M_s/2},\qquad\mathcal D_s^+\ge\frac{(1-b)^2}{M_s/2}.
```

The sum is minimized at $b=1/2$, where each half contributes $1/(2M_s)$. The Euler–Lagrange equation of the minimizing conductivity problem is

```math
-\frac d{dx}\left(w_s^{-1}F_x\right)=0.
```

**Crucial qualification:** This is a **different** weighted SL-type differential expression from the original $p=x^3,w=x$ carrier. Its *Dirichlet energy principle* is not the assertion that the canonical eigenfunction must satisfy $f(c)=0$. The equal midpoint is the common reflection of a positive measure, while a spectral boundary condition is separately selected.

At $s=1$, $\min\mathcal D_s=2r\sqrt\mu/\pi$; at $s=2$, $\min\mathcal D_s=2r\mu$. Their half-interval contributions are respectively $r\sqrt\mu/\pi$ and $r\mu$.

## 28. The complete r=2 web with c and mu retained [D,V]

Fix $r=2$ and keep $u=\ln(x/c)$, $c>0$ and $\mu>0$. The rational double-angle fields are

```math
S_2=\frac{2c^2x^2}{x^4+c^4},\qquad W_2=\frac{x^4-c^4}{x^4+c^4},\qquad S_2^2+W_2^2=1.
```

Relative to the $r=1$ fields, their recursions are

```math
W_2=\frac{2W_1}{1+W_1^2},\qquad S_2=\frac{S_1^2}{2-S_1^2}.
```

The rational function, primitive and improper half-integrals become

```math
f_\mu(x;2,c)=\frac{c^2x}{\sqrt\mu(x^4+c^4)},\qquad\int f_\mu\,dx=\frac1{2\sqrt\mu}\arctan((x/c)^2)+C.
```

```math
\int_0^c f_\mu\,dx=\int_c^\infty f_\mu\,dx=\frac{\pi}{8\sqrt\mu},\qquad\int_0^c xf_\mu^2dx=\int_c^\infty xf_\mu^2dx=\frac1{8\mu}.
```

The centered Pinney amplitude, complex linear carrier and Riccati variable read

```math
a^2=\sqrt\mu\cosh(2u)=\frac{\sqrt\mu(x^4+c^4)}{2c^2x^2},\qquad\Phi=\mu^{1/4}(\cosh u+i\sinh u).
```

```math
a''=a+\mu a^{-3},\qquad\Phi''=\Phi,\qquad\frac{\Phi'}{\Phi}=W_2+iS_2,\qquad\theta=\arctan((x/c)^2)-\frac\pi4.
```

The centered **Pinney energy quartic** is smooth with $j=1728$:

```math
Y^2=A^4-\mu,\qquad A=a,\qquad Y=aa'.
```

The normalized **Master separatrix energy quartic** is $p^2=z^2-z^4$ with $\Delta_{\rm M}=0$. The Gram-square quartic is likewise singular but is a third construction.

### 28.1 Four distinct r=2 operators

The original linear carrier of the Master equation is

```math
H_{\rm lin,2}=-\partial_u^2+4,\qquad\sigma(H_{\rm lin,2})=[4,\infty).
```

The half-rate carrier used by Pinney/Riccati is

```math
H_{\frac12,2}=-\partial_u^2+1,\qquad\sigma(H_{\frac12,2})=[1,\infty).
```

The **Pinney variational Hessian** and the **Master separatrix Hessian** are respectively

```math
H_{\rm EP,2}=-\partial_u^2+1-3S_2^2,\qquad H_{\rm M,2}=-\partial_u^2+4-24S_2^2.
```

On the natural full-line $L^2(du)$ realizations, $H_{\rm EP,2}$ has a zero ground eigenvalue and essential threshold $1$, whereas $H_{\rm M,2}$ has discrete eigenvalues $-12,0$ and essential threshold $4$. Both are self-adjoint real Schrödinger operators despite the difference in their lowest eigenvalue signs.

The **further catenoid Jacobi** separated expression from §24 is

```math
H_{\rm cat,2}=-\partial_u^2-8S_2^2.
```

As an abstract full-line Schrödinger operator, it has a bound level at $-4$; converting that observation to a claim about the *surface* Jacobi spectrum also requires the angular mode and surface-domain conditions.

### 28.2 Center-preserving inversion and boundary data

For every resolution, including $r=2$, the involution is

```math
x\mapsto c^2/x,\qquad u\mapsto-u,\qquad f(x)\mapsto(c^2/x^2)f(c^2/x).
```

Even modes satisfy $cf_x(c)+f(c)=0$, and odd modes $f(c)=0$. The resolution $r$ changes the rational profile and potential coefficients; $c$ locates the symmetry point and the logarithmic origin.

## 29. Evidence classification, counterexamples and candidate foundational theorems

| Proposed claim | Mathematical verdict |
|---|---|
| EP measures whether a Sturm–Liouville operator is self-adjoint. | **False.** Pinney strength/current is solution-space data; self-adjointness depends on the operator domain and boundary form. The complex-Robin counterexample is explicit (§10). |
| Wronskian conservation implies self-adjointness. | **False.** It follows locally for real coefficients and real $\lambda$, even before specifying an operator domain (§9). |
| Nonzero Milne phase current means self-adjointness is broken. | **False.** Real self-adjoint operators have current-carrying generalized scattering states (§20). |
| A nonreal spectral *parameter* means a real operator is not self-adjoint. | **False.** Self-adjoint resolvents are evaluated at complex parameters; nonreal *eigenvalues* are a different issue (§9). |
| The canonical Pinney effective potential is a double well. | **False.** For $Q_0,k>0$ it is strictly decreasing on $a>0$; for $Q_0=-\omega^2,k>0$ it has a single centrifugal minimum (§16). |
| The signed Duffing/Master potential is a smooth quartic double well. | **True**, but its $\mathrm{sech}$ pulse is a homoclinic to the barrier equilibrium, not a tunneling trajectory between the two minima (§17). |
| Negative eigenvalues of a Hessian imply non-self-adjointness. | **False.** The real Master Hessian is self-adjoint and has a negative bound state (§23). |
| Every quartic attached to Pinney is singular. | **False.** The Gram-square quartic is always singular, but the *Pinney energy quartic* is smooth in the canonical regime (§18). |
| A smooth elliptic energy quartic always requires elliptic time evolution. | **False.** The Pinney *time differential* descends through a degree-two quotient to a conic (§18.2). |
| Tunneling requires an operator with a complex spectrum. | **False.** A real finite barrier admits a self-adjoint operator and exact nonzero transmission (§20). |
| Reflection at $x=c$ forces a new boundary of the original full-line operator. | **False.** It is a regular interior point; boundary or interface conditions are an additional domain choice (§§4–6). |
| Reflection gives Neumann/Dirichlet sectors. | **True** for a parity-preserving self-adjoint realization, with the even sector becoming Robin in the original weighted $f$ variable (§5). |
| The original half-integral is a spectral boundary condition. | **False.** It is a symmetry of a positive measure; spectral conditions are separate (§§7,27). |
| The original integral equals a scaled Gudermannian phase change. | **True for the specified canonical carrier**, with factor $1/(r\sqrt\mu)$ (§12). |
| Riccati ratio automatically equals the Hopf fiber. | **False.** It is the projective base coordinate; a normalized spinor and common phase produce the Hopf bundle (§15). |
| All minimal-surface Jacobi operators have the canonical Master spectrum. | **False.** Catenoid, Pinney and Master use PT wells of different orders, and global surface domains are further data (§§23–26). |

### 29.1 Candidate theorem statements for the foundational-layer audit

**A — Domain-safe Liouville/parity theorem [D,V].** The original weighted carrier with $p=x^3,w=x$ is unitarily $-\partial_u^2+r^2$ with transported domains; the involution $x\mapsto c^2/x$ becomes parity and yields exact even/odd half-line Robin/Dirichlet conditions at $x=c$. Proof: §§3–6.

**B — Milne–primitive theorem [D,V].** The argument of the selected half-rate complex carrier is $\theta=\mathrm{gd}(ru)/2$, with $d\theta=r\sqrt\mu f_\mu\,dx$, giving equal half-integral phase increments. Proof: §§7, 11–12.

**C — Pinney energy quartic/conic quotient theorem [D,V].** The constant-carrier Pinney energy quartic has the invariant formulas of §18, while the distinguished time differential descends under $(a,Y)\mapsto(a^2,Y)$ to a genus-zero conic. The canonical centered smooth quartic has $j=1728$. This observation is classical algebraic geometry reorganized within the framework, not a novelty claim.

**D — Phase–Gauss metric theorem [D,V].** The catenoid round Gauss-map metric has conformal factor $4(\theta')^2=4j^2/a^4$ for the specified canonical Pinney amplitude and Milne phase; its equator is $x=c$. Proof: §25.

**E — Reflection and Beta-moment theorem [D,V,H169].** The whole weighted moment family has an exact symmetric Beta CDF with median $x=c$ and a minimizer of its own inverse-weight Dirichlet energy. It does not dictate the self-adjoint domain of the original operator. Proof: §§7,27.

**F — Self-adjoint tunneling counterexample [D,K].** A finite real rectangular barrier has an interior hyperbolic Pinney envelope and exterior flux-preserving matching with nonzero transmission; its full Schrödinger operator is still self-adjoint. Proof: §20.

## 30. Independent verification, literature and research agenda

### 30.1 Algebraic and analytic checks

The following identities were verified by independent symbolic differentiation or direct elementary integration when preparing this draft:

1. The unitary map $f\mapsto xf$ sends the original weighted expression to $-\partial_u^2+r^2$ and carries its exact boundary pairing to the ordinary Wronskian.
2. Inversion $\mathfrak R_cf=(c^2/x^2)f(c^2/x)$ becomes parity, and the even-sector original-variable condition is $cf_x(c)+f(c)=0$.
3. The unweighted original integral and the weighted SL norm have exact halves $\pi/(4r\sqrt\mu)$ and $1/(4r\mu)$ respectively.
4. The general moment $M_s=B(s/2,1/2)/[r(2\sqrt\mu)^s]$ pushes to the symmetric Beta$(s/2,s/2)$ law in $P=(1+W)/2$.
5. The chosen complex carrier $\Phi=\mu^{1/4}(\cosh(ru/2)+i\sinh(ru/2))$ solves $\Phi''=r^2\Phi/4$, has current $r\sqrt\mu/2$, and gives logarithmic derivative $(r/2)(W+iS)$.
6. The local SL current law is $j'=[\mathrm{Im}q_0-(\mathrm{Im}\lambda)w]|\psi|^2$, independently of the operator domain.
7. The non-self-adjoint half-line Robin domain with $h=-1+i$ has the explicit nonreal eigenvalue $r^2/4+2i$.
8. The Pinney energy quartic has $I=4\mathcal E_a^2-12Q_0k$, $J=-16\mathcal E_a^3-144Q_0k\mathcal E_a$, and $\Delta=-256Q_0k(\mathcal E_a^2+Q_0k)^2$ in the repository's raw convention; these were checked with exact SymPy polynomial operations.
9. At the centered positive canonical parameters the Pinney energy quartic is smooth with $j=1728$; the Gram-square and Master separatrix quartics instead have zero discriminant.
10. The quotient $J=a^2$ satisfies the conic $Y^2=Q_0J^2+2\mathcal E_a J-k$ and time form $du=dJ/(2Y)$.
11. The Master Hessian eigenrelations $H_{\rm M}S^2=-3r^2S^2$ and $H_{\rm M}(SW)=0$, and the catenoid Jacobi order-one eigenrelation, were checked by differentiation.
12. The catenoid Gauss metric equality $g_G=4(\theta')^2|d\zeta|^2$ and both equal hemisphere area integrals follow from the explicit Gauss map.
13. The rectangular barrier transfer matrix has determinant one; matching it to exterior waves gives the standard transmission coefficient.
14. For $r=2$ the exact rational expressions, Pinney equation, operator eigenvalue scalings and half-integrals were recalculated.

These are checks of the stated algebraic/differential identities and ordinary explicit operators. They do not certify every global minimal-surface period, all self-adjoint extensions of general singular operators, or any new universal classification theorem.

### 30.2 Existing framework sources

- The live foundational linear-exponential chapter SF-I-020 and provisional research drafts 020, 030, 040, 050, 060, 080, 090, 100 and 110.
- Historical ZIP: 04-follow-ups/spectral-calculus.md (H169–H172: reflection, half-splitting, Weyl–Wronskian factorization, weighted Dirichlet principle and Hopf flux), directly reopened and compared in this investigation.
- Historical ZIP: 04-follow-ups/bernoulli-riccati.md, friedmann-reciprocal-envelope.md, fundamental-forms-willmore-hopf.md, and conformal-and-probabilistic-readings.md.
- The 2026-11-16_v2 complete reference retains its own claim-by-claim evidence levels; the present additional quartic-conic quotient and boundary counterexamples are **new derived additions to the provisional record**.

### 30.3 External classical sources and exact scope

- Sturm–Liouville operator domains, Weyl alternative and boundary spectral functions: https://encyclopediaofmath.org/wiki/Sturm-Liouville_theory ; https://diana.mat.univie.ac.at/~gerald/students/krueger_dipl.pdf .
- Singular self-adjoint extensions and boundary triples: https://arxiv.org/abs/1910.13117 ; https://www.sciencedirect.com/science/article/am/pii/S0022039623001833 .
- Self-adjoint multi-interval and point-interaction transmission conditions: https://www.mat.univie.ac.at/~gerald/ftp/articles/MeasureSL.pdf ; https://www.sciencedirect.com/science/article/pii/S0024379509000196 .
- Milne amplitude-phase analysis and Ermakov invariant in spectral/scattering theory: https://journals.aps.org/pra/abstract/10.1103/PhysRevA.63.012103 ; https://journals.aps.org/pra/abstract/10.1103/PhysRevA.97.022701 .
- Barrier scattering using amplitude-phase methods: https://doi.org/10.1088/0305-4470/38/1/017 ; https://www.mdpi.com/2218-2004/14/8/71 .
- Minimal-surface Jacobi fields and the catenoid/helicoid: https://pmc.ncbi.nlm.nih.gov/articles/PMC7428034/ .
- Classical binary-quartic invariant normalization: https://link.springer.com/article/10.1007/s40993-022-00376-z . **Normalization warning:** The project's raw *polynomial discriminant* is $\Delta=(4I^3-J^2)/27$; some classical invariant-theory sources call $16\Delta$ the binary quartic discriminant. Ratios $j$ and the zero locus are unchanged by this naming choice, but numerical discriminants must not be mixed.

### 30.4 Open mathematical problems

1. **Boundary-triple continuation:** derive a precise rank-one resolvent relation between the free full-line carrier and its real point-interaction family at $x=c$, and express both half-line Weyl functions in the original weighted coordinate.
2. **Marked quartic correspondence:** convert the smooth Pinney energy quartic to a Weierstrass cubic and exhibit explicitly the degree-two conic quotient and its marked time differential; test whether the $j=1728$ catenoid surface quartic is isomorphic in a way preserving *any selected differential*.
3. **Scattering phases:** compute Milne phase shifts, transmission and resonance data for the order-two Master Pöschl–Teller well with different parity/interface extensions, tracking spectral and physical energy normalization.
4. **Beta Dirichlet-to-Neumann:** determine boundary operators associated with the entire $s>0$ inverse-weight Beta moment family; compare with the archived level-$q$ Hopf and Legendre constructions while distinguishing the two shape exponents.
5. **Global minimal-surface limits:** compare catenoid and helicoid Jacobi-operator domains with Riemann minimal example period data, including Floquet and noncompact-end conditions.
6. **Hopf phase versus Milne phase:** construct an explicit bundle map and connection pullback relating the selected Hopf base coordinate $t=e^{ru}$ to the nonconstant Milne phase; identify where their holonomies/normalizations differ.
7. **Quartic classification:** track simultaneously the Gram-square, Pinney-energy and Master-energy quartics under $r$ doubling, and determine which marked differentials—not merely $I,J$—intertwine.
8. **Self-adjointness boundary tests:** analyze complex Robin and non-Hermitian/PT-symmetric extensions on the two half-intervals without conflating non-real boundary parameters with nonlinear potential instability.

**Closing mathematical statement.** Self-adjointness, a Pinney determinant, a Riccati chart, a phase current, a binary-quartic discriminant, a quartic double well, and a tunneling coefficient are different kinds of data. The Symmetrical Framework supplies precise transformations between selected instances of them: a unitary logarithmic Liouville map, a symmetric-square/Pinney envelope, a projective Cayley–Gudermannian phase, a marked elliptic-to-conic quotient, and a catenoid Gauss-map realization. The fixed point $x=c$ is simultaneously the original measure's half-split, a spectral parity center after declaring the correct domain, and the Gauss sphere's equator—but those observations do not identify the distinct measures, spectra, connections, or physical interpretations.
