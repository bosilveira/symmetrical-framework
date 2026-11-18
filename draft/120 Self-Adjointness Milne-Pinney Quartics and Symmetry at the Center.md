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
T=T^*,\qquad \operatorname{Dom}(T)=\operatorname{Dom}(T^*).
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
