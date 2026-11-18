---
id: SF-DRAFT-000
title: Lagrange Inversion of Canonical Coordinates and Level Turning Points
status: provisional
created: 2026-11-18
proposed_layers: [01-foundational, 03-correspondences]
related_claims: [H147, H148, H151]
---

# 000 Lagrange Inversion of Canonical Coordinates and Level Turning Points

**Editorial status:** Complete research working draft, NOT a canonical theorem chapter. Each finding must receive independent claim-by-claim audit before incorporation in the four layers. Classical results are identified as such; no novelty is assumed.

**Scope:** Lagrange–Bürmann inversion; Catalan reconstruction of the canonical hyperbolic fields; Gudermannian/arctangent primitive; the entire real-positive $`q`$ level hierarchy; inverse turning-point branches, reciprocity, discriminants and singularities; all-orders period expansion at equilibrium; literature and verification boundaries.

**Canonical conventions:** $`x,c,r,\mu>0`$, $`u=\ln(x/c)`$, $`q=(l-1)/2>0`$, $`S=\mathrm{sech}(ru)`$, $`W=\tanh(ru)`$. A prime denotes differentiation in $`u`$ unless explicitly specified; $`s=ru`$ is used for dimensionless oscillator time. Scale $`c`$ remains explicit in all coordinate reconstructions.

**Source provenance:** The preceding Lagrange-inversion investigation; the user's archived 'symmetrical-framework-update-2026-11-17-ah.zip', notably '04-follow-ups/fox-h-reading.md' and '04-follow-ups/period-hierarchy.md'; and the supplied 'CLAIMS(6).md', particularly H147–H148 and H151. These historical files are sources to audit, not automatically accepted chapters in the new repository.

## 1. Evidence and mathematical dependencies

- **[K] Classical:** Lagrange–Bürmann inversion, Catalan and generalized Fuss–Catalan coefficients, Cauchy residues, Stirling asymptotics, analytic inverse function theorem.
- **[D] Derived step by step here:** canonical coordinate and primitive reconstruction; exact turning-point inversion for every real $`q>0`$; the inner Puiseux branch; reciprocal roots; equilibrium fold and coefficient asymptotics; convergent *all-orders local period expansion*.
- **[V] Independently checked:** symbolic coefficient extraction and exact specializations $`q=1,2`$; numerical roots and period quadrature for $`q=1/2,1,\sqrt2,2,3,4`$.
- **Open:** full complex continuation, global period-series radius, complete Picard–Fuchs/monodromy classification, prior-art novelty review.

The governing idea is to invert *specified analytic maps with specified branches*. Lagrange inversion alone does not assert complete solvability of the nonlinear ODE or identify its global monodromy.

## 2. Lagrange–Bürmann coefficient extraction

**Theorem 2.1 (classical).** Suppose $`z=z(w)`$ is analytic near $`w=0`$ and satisfies $`z=w\Phi(z)`$, where $`\Phi`$ is analytic and $`\Phi(0)\ne0`$. For every analytic $`H`$ and every $`n\ge1`$,

```math
[w^n]H(z(w))=\frac1n[t^{n-1}]H'(t)\Phi(t)^n.
```

In particular,

```math
[w^n]z(w)=\frac1n[t^{n-1}]\Phi(t)^n.
```

**Proof.**

1. Since $`w=z/\Phi(z)`$ has nonzero derivative at zero, the analytic inverse exists locally.
2. By Cauchy's coefficient formula, the desired coefficient is the residue of $`H(z(w))w^{-n-1}\,dw`$ at $`w=0`$.
3. Substitute $`w=z/\Phi(z)`$, so $`dw=(\Phi-z\Phi')\Phi^{-2}\,dz`$. The residue is

```math
\mathrm{Res}_{z=0}H(z)\left(\frac{\Phi(z)^n}{z^{n+1}}-\frac{\Phi(z)^{n-1}\Phi'(z)}{z^n}\right)\,dz.
```

4. The residue of the total derivative $`d(H(z)\Phi(z)^nz^{-n})/dz`$ is zero. Rearranging yields

```math
\frac1n\mathrm{Res}_{z=0}\frac{H'(z)\Phi(z)^n}{z^n}\,dz=\frac1n[z^{n-1}]H'(z)\Phi(z)^n.
```

This proves the theorem. Here $`[w^n]`$ means Taylor coefficient extraction.

## 3. Catalan inversion of the canonical fields

Define the multiplicative coordinate

```math
z=e^{ru}=(x/c)^r,\quad S=\frac{2z}{1+z^2},\quad W=\frac{z^2-1}{z^2+1},\quad S^2+W^2=1.
```

Set $`w=S/2`$ and choose the sheet $`u\le0`$, so $`0<z\le1`$. Then

```math
w=\frac{z}{1+z^2}\quad\Longleftrightarrow\quad z=w(1+z^2).
```

### Theorem 3.1 — Catalan coordinate series

On $`0<x<c`$,

```math
e^{r\ln(x/c)}=\sum_{n=0}^{\infty}C_n\left(\frac{S(x)}2\right)^{2n+1},\qquad C_n=\frac1{n+1}\binom{2n}{n}.
```

It extends continuously to $`x=c`$, where $`S=1`$. On the full positive $`x`$ axis,

```math
e^{-r|\ln(x/c)|}=\sum_{n=0}^{\infty}C_n\left(\frac{\mathrm{sech}(r\ln(x/c))}{2}\right)^{2n+1}.
```

**Proof.** Apply Theorem 2.1 with $`\Phi(z)=1+z^2`$ and $`H(z)=z`$. Only powers $`w^{2n+1}`$ occur, with coefficient

```math
[w^{2n+1}]z(w)=\frac1{2n+1}\binom{2n+1}{n}=\frac1{n+1}\binom{2n}{n}=C_n.
```

Thus $`z=w+w^3+2w^5+5w^7+14w^9+\cdots`$. Since $`C_n\sim4^n/(\sqrt\pi\,n^{3/2})`$, the boundary $`w=1/2`$ converges to $`z=1`$. For $`u>0`$ replace $`z`$ by $`z^{-1}`$, using $`S(u)=S(-u)`$. This establishes both formulas.

### 3.2 Logistic variable

Write $`p=(1+W)/2`$. Since $`p=z^2/(1+z^2)=wz`$ and $`z=wC(w^2)`$,

```math
p=w^2C(w^2)=\sum_{n=0}^\infty C_n(S/2)^{2n+2}=\frac{1-\sqrt{1-S^2}}2\qquad (u\le0).
```

On $`u\ge0`$ the correct branch is the complement $`p=(1+\sqrt{1-S^2})/2`$. Thus $`S^2=4p(1-p)`$ and, by the original hyperbolic definitions, $`p'=2rp(1-p)`$. Catalan inversion reconstructs the *logistic chart* of the circle $`S^2+W^2=1`$.

### 3.3 Recover the logarithmic distance

For the Catalan function $`C(t)=1+tC(t)^2`$, set $`D=C-1=t(1+D)^2`$. Apply Theorem 2.1 to $`H(D)=\ln(1+D)`$:

```math
[t^n]\ln C(t)=\frac1n[t^{n-1}](1+t)^{2n-1}=\frac1{2n}\binom{2n}{n}.
```

Because $`z=wC(w^2)`$, on $`u\le0`$,

```math
ru=\ln(S/2)+\sum_{n=1}^\infty\frac1{2n}\binom{2n}{n}(S/2)^{2n}.
```

Combining the two sheets gives

```math
r|\ln(x/c)|=-\ln(S/2)-\sum_{n=1}^\infty\frac1{2n}\binom{2n}{n}(S/2)^{2n}.
```

The series converges for $`0<S\le1`$; differentiation with respect to $`S`$ is singular at $`S=1`$, the fold where the two sheets $`u\gtrless0`$ merge.

### 3.4 Arctangent, Gudermannian, and the half-split

Take $`H(z)=2\arctan z`$. Since $`H'(z)=2/(1+z^2)`$, Lagrange–Bürmann gives

```math
[w^{2n+1}]2\arctan z(w)=\frac2{2n+1}\binom{2n}{n}.
```

Therefore, on $`u\le0`$,

```math
2\arctan(e^{ru})=\sum_{n=0}^\infty\frac2{2n+1}\binom{2n}{n}(S/2)^{2n+1}=\arcsin S.
```

The final equality also follows from $`\sin(2\arctan z)=2z/(1+z^2)=S`$ and the selected angular branch. On $`u\ge0`$, the angle is $`\pi-\arcsin S`$.

Recall the canonical symmetrical function and its primitive:

```math
f_\mu(x;r,c)=\frac{\mathrm{sech}(r\ln(x/c))}{2\sqrt\mu\,x},\qquad\int_0^x f_\mu(t;r,c)\,dt=\frac{\arctan((x/c)^r)}{r\sqrt\mu}.
```

Thus $`\int_0^x f_\mu`$ equals $`\arcsin S(x)/(2r\sqrt\mu)`$ for $`x\le c`$ and $`\pi/(2r\sqrt\mu)-\arcsin S(x)/(2r\sqrt\mu)`$ for $`x\ge c`$. At $`x=c`$ both give $`\pi/(4r\sqrt\mu)`$, the canonical half-split.

For the Gudermannian angle $`\gamma(u)=2\arctan(e^{ru})-\pi/2`$,

```math
\cos\gamma=S,\qquad \sin\gamma=W,\qquad \gamma'=rS.
```

This is an exact coordinate construction, not an additional physical interpretation.

## 4. Nonlinear level family and the turning-point map

For $`q=(l-1)/2>0`$ the archived family is

```math
U_q''=q^2r^2U_q-4\mu q(q+1)r^2U_q^{1+2/q},\qquad U_q>0.
```

The centered separatrix is

```math
U_q=(4\mu)^{-q/2}\,\mathrm{sech}^{\,q}(ru).
```

**Convention warning:** $`U_1=xf_\mu`$, whereas the earlier cubic Master amplitude is $`y=2xf_\mu=2U_1`$. The corresponding energy constants differ by normalization.

### Proposition 4.1 — Conservation and turning points

Every positive classical solution has conserved energy

```math
\varepsilon=(U_q')^2-q^2r^2U_q^2+4\mu q^2r^2U_q^{2+2/q}.
```

**Proof.** Direct differentiation gives

```math
\varepsilon'=2U_q'[U_q''-q^2r^2U_q+4\mu q(q+1)r^2U_q^{1+2/q}]=0.
```

Define $`X=4\mu U_q^{2/q}`$ and $`U_q^2=(X/(4\mu))^q`$. At a turning point $`U_q'=0`$,

```math
X^q(1-X)=a,\qquad a=-\frac{(4\mu)^q\varepsilon}{q^2r^2}.
```

Introduce the critical constant and dimensionless level

```math
c_q=\frac{q^q}{(q+1)^{q+1}},\qquad v=\frac a{c_q}.
```

The turning-point equation is

```math
P_q(X)=X^q(1-X)=c_qv.
```

Since

```math
P_q'(X)=X^{q-1}(q-(q+1)X),\qquad X_*=\frac q{q+1},\qquad P_q(X_*)=c_q,
```

there are precisely two positive turning points $`0<X_{q,-}<X_*<X_{q,+}<1`$ for $`0<v<1`$. The separatrix is the limiting level $`v=0`$ and the equilibrium the merger at $`v=1`$.

## 5. Universal outer turning-point inversion

Define $`C_q(t)`$ near $`t=0`$ as the unique analytic solution of

```math
C_q(t)=1+tC_q(t)^{q+1},\qquad C_q(0)=1.
```

For noninteger $`q`$ the power uses the analytic branch near $`C=1`$.

### Theorem 5.1 — Fuss–Catalan reconstruction

For every fixed real $`q>0`$,

```math
C_q(t)=\sum_{n=0}^{\infty}A_n(q)t^n,\qquad A_n(q)=\frac1{qn+1}\binom{(q+1)n}{n}.
```

The larger turning point is

```math
X_{q,+}(v)=\frac1{C_q(c_qv)}.
```

**Proof.**

1. Select the inverse root $`X\to1`$ as $`t=X^q(1-X)\to0`$.
2. Put $`C=1/X`$. Then $`t=(C-1)/C^{q+1}`$, so $`C=1+tC^{q+1}`$.
3. Put $`D=C-1`$, so $`D=t(1+D)^{q+1}`$.
4. Lagrange–Bürmann gives

```math
[t^n]D(t)=\frac1n[z^{n-1}](1+z)^{(q+1)n}=\frac1n\binom{(q+1)n}{n-1}=\frac1{qn+1}\binom{(q+1)n}{n}.
```

5. Since $`X=1/C`$, the stated branch is reconstructed. Exact convergence and endpoint results follow in Section 7.

These are ordinary Fuss–Catalan coefficients for positive integer $`q`$, and analytic generalized binomial coefficients for arbitrary real $`q>0`$.

| $`q`$ | $`l`$ | First coefficients $`A_0,A_1,A_2,A_3,A_4`$ |
|---:|---:|---|
| $`1/2`$ | $`2`$ | $`1,1,3/2,21/8,5`$ |
| $`1`$ | $`3`$ | $`1,1,2,5,14`$ |
| $`2`$ | $`5`$ | $`1,1,3,12,55`$ |
| $`3`$ | $`7`$ | $`1,1,4,22,140`$ |
| $`4`$ | $`9`$ | $`1,1,5,35,285`$ |

**Correction:** The earlier discussion incorrectly listed $`3`$ as the coefficient of $`t^3`$ at $`q=1/2`$. It is $`21/8`$.

### 5.2 Universal coefficient formula for observables

For fixed $`\alpha\in\mathbb C`$, Lagrange–Bürmann applied to $`H(D)=(1+D)^\alpha`$ yields

```math
[t^n]C_q(t)^\alpha=\frac{\alpha}{n}\binom{(q+1)n+\alpha-1}{n-1}\qquad(n\ge1).
```

At $`\alpha=-1`$ this recovers the outer-root expansion

```math
X_{q,+}=1-t-qt^2-\frac{q(3q+1)}2t^3+O(t^4),\qquad t=c_qv.
```

Differentiating the coefficient identity with respect to $`\alpha`$ at zero gives

```math
\ln C_q(t)=\sum_{n=1}^{\infty}\frac1n\binom{(q+1)n-1}{n-1}t^n.
```

The central-binomial logarithm of Section 3 is the specialization $`q=1`$.

### 5.3 Differential identity of the inverse

Differentiating $`C=1+tC^{q+1}`$ and eliminating $`t=(C-1)/C^{q+1}`$ gives

```math
C_q'(t)=\frac{C_q(t)^{q+2}}{q+1-qC_q(t)}.
```

On the real outer branch $`C_q'>0`$ until $`C_q=(q+1)/q`$, where the inverse derivative diverges.

## 6. Inner turning point and reciprocal-parameter inversion

The smaller root tends to zero when $`v\to0`$. It is generally a Puiseux series, not an ordinary Taylor series in $`v`$.

Put $`t=c_qv`$ and $`s=t^{1/q}`$. The turning-point equation can be rearranged as

```math
X=s(1-X)^{-1/q}.
```

Lagrange–Bürmann gives the exact local inverse branch

```math
X_{q,-}(v)=\sum_{n=1}^{\infty}\frac1n\binom{n/q+n-2}{n-1}s^n,\qquad s=(c_qv)^{1/q}.
```

The first terms are

```math
X_{q,-}=s+\frac1q s^2+\frac{q+3}{2q^2}s^3+O(s^4).
```

This converges as an analytic series in $`s`$ near zero. For $`q=2`$, its powers correspond to half-integer powers of $`v`$; for $`q=4`$, they correspond to quarter-integer powers.

### Theorem 6.1 — Exact turning-point reciprocity

For all real $`q>0`$,

```math
c_{1/q}^{\,q}=c_q.
```

For $`0<v<1`$, the real root branches satisfy

```math
X_{q,-}(v)=1-X_{1/q,+}(v^{1/q}),\qquad X_{q,+}(v)=1-X_{1/q,-}(v^{1/q}).
```

Equivalently,

```math
X_{q,-}(v)=1-\frac1{C_{1/q}(c_{1/q}v^{1/q})}.
```

**Proof.**

1. Compute directly $`c_{1/q}^{\,q}=q^q/(q+1)^{q+1}`$.
2. Introduce $`Y=1-X`$ and take the positive $`q`$-th root of $`X^q(1-X)=c_qv`$:

```math
Y^{1/q}(1-Y)=c_{1/q}v^{1/q}.
```

3. This is exactly the normalized turning-point equation for parameter $`1/q`$ and level $`v^{1/q}`$.
4. The map $`X\mapsto1-X`$ reverses the order of the two roots, so small and large branches are interchanged.
5. Substitute Theorem 5.1 for the reciprocal outer root to obtain the last formula.

At $`q=1`$ this reduces to $`X_{1,-}(v)+X_{1,+}(v)=1`$. At $`q=2`$ it pairs the branches with those at $`q=1/2`$. The theorem concerns the selected positive real inverse branches; it is not by itself a statement about complex monodromy or Jacobians.

## 7. Convergence boundary, fold singularity, and asymptotics

### Proposition 7.1 — Turning-point coalescence

As $`v\uparrow1`$, let $`\delta=1-v`$. Then

```math
X_{q,\pm}(v)=\frac q{q+1}\ \pm\sqrt{\frac{2q}{(q+1)^3}}\sqrt\delta-\frac{2(q-1)}{3(q+1)^2}\delta+O(\delta^{3/2}).
```

**Proof.**

1. At $`X_*=q/(q+1)`$, the derivatives of $`P_q(X)=X^q(1-X)`$ are

```math
P_q'(X_*)=0,\qquad P_q''(X_*)=-qX_*^{q-2}<0,\qquad P_q'''(X_*)=-2q(q-1)X_*^{q-3}.
```

2. Substitute $`X=X_*+a\delta^{1/2}+b\delta+O(\delta^{3/2})`$ into $`P_q(X)=c_q(1-\delta)`$.
3. Comparing coefficients of $`\delta`$ gives

```math
\frac12P_q''(X_*)a^2=-c_q\quad\Longrightarrow\quad a^2=\frac{2q}{(q+1)^3}.
```

4. Comparing coefficients of $`\delta^{3/2}`$ gives

```math
P_q''(X_*)ab+\frac16P_q'''(X_*)a^3=0\quad\Longrightarrow\quad b=-\frac{2(q-1)}{3(q+1)^2}.
```

5. Choose the positive sign of $`a`$ for $`X_{q,+}`$ and the negative sign for $`X_{q,-}`$.

Implicit differentiation further gives

```math
\frac{dX_{q,\pm}}{dv}=\frac{c_q}{P_q'(X_{q,\pm})}.
```

Thus the slopes of both inverse branches diverge in magnitude like $`(1-v)^{-1/2}`$. This is the ordinary analytic fold produced by the merger of two simple roots.

### Proposition 7.2 — Exact radius of the generalized Catalan series

For each fixed real $`q>0`$,

```math
A_n(q)=\frac1{qn+1}\binom{(q+1)n}{n}\sim\frac{\sqrt{q+1}}{\sqrt{2\pi}\,q^{3/2}}\,n^{-3/2}c_q^{-n}.
```

**Proof.**

1. Write the binomial coefficient as a ratio of Gamma functions,

```math
\binom{(q+1)n}{n}=\frac{\Gamma((q+1)n+1)}{\Gamma(n+1)\Gamma(qn+1)}.
```

2. Apply Stirling's formula separately to the three Gamma factors.
3. Their exponential ratio is $`((q+1)^{q+1}/q^q)^n=c_q^{-n}`$; the remaining power and prefactor are precisely $`n^{-3/2}\sqrt{q+1}/(\sqrt{2\pi}\,q^{3/2})`$.
4. The root test therefore yields radius of convergence exactly $`c_q`$ for $`C_q(t)`$.
5. At the positive boundary $`t=c_q`$, the asymptotic $`n^{-3/2}`$ is summable, so the series converges there. Its value on the continuous real branch is

```math
C_q(c_q)=\frac{q+1}{q},\qquad X_{q,+}(1)=\frac q{q+1}.
```

The denominator of $`C_q'(t)`$ in Section 5.3 vanishes at this value. Consequently the turning-point fold, the square-root singularity, the coefficient asymptotics, and the inverse-series radius are all descriptions of the same critical event.

**Do not conflate radii.** This radius $`c_q`$ belongs to the series for $`C_q`$ about $`t=0`$. It says nothing immediate about the global radius of the period series about $`v=1`$.

## 8. The real period integral and historical reciprocity

Using $`X=4\mu U_q^{2/q}`$ in the energy integral gives

```math
(X')^2=4r^2X^{2-q}\big[X^q(1-X)-c_qv\big].
```

Indeed, $`X'/X=(2/q)U_q'/U_q`$; insert the first integral from Proposition 4.1 and simplify. A full positive oscillation goes from the lower turning point to the upper one and back. Hence its period with respect to $`u=\ln(x/c)`$ is

```math
T_q(v)=\frac1r\mathfrak p_q(v),\qquad\mathfrak p_q(v)=\int_{X_{q,-}(v)}^{X_{q,+}(v)}\frac{X^{q/2-1}\,dX}{\sqrt{X^q(1-X)-c_qv}}.
```

The singularities at the two endpoints are integrable for $`0<v<1`$.

The archived H147–H148 investigations record the exact Mellin transform

```math
\int_0^1v^{s-1}\mathfrak p_q(v)\,dv=c_q^{-s}\sqrt\pi\,\frac{\Gamma(s)\Gamma(qs)}{\Gamma((q+1)s+1/2)}
```

in its appropriate convergence region, together with the real-branch reciprocity

```math
\mathfrak p_q(v)=\frac1q\mathfrak p_{1/q}(v^{1/q}).
```

These are historical source claims to preserve and re-audit before promotion. The turning-point reciprocity in Section 6 is an independent algebraic counterpart, but it does not by itself imply the period relation for arbitrary complex periods.

Linearization at the positive equilibrium immediately predicts the limiting real period

```math
\mathfrak p_q(1)=\pi\sqrt{\frac2q}.
```

The following construction gives a stronger result: the complete local expansion around this limit.

## 9. Lagrange inversion produces the full near-equilibrium period series

### 9.1 A local analytic coordinate at the fold

Put

```math
X=X_*(1+h),\qquad X_*=\frac q{q+1}.
```

There is an *exact* normalized identity

```math
\frac{P_q(X)}{c_q}=(1+h)^q(1-qh).
```

Define a function with a removable zero-over-zero singularity,

```math
g_q(h)=\frac{1-(1+h)^q(1-qh)}{h^2}.
```

Expanding the binomial series yields

```math
g_q(h)=q(q+1)\sum_{k=0}^\infty\frac1{k+2}\binom{q-1}{k}h^k,\qquad g_0:=g_q(0)=\frac{q(q+1)}2.
```

An alternative exact integral representation is

```math
g_q(h)=q(q+1)\int_0^1t(1+th)^{q-1}\,dt.
```

**Derivation:** Integrate the binomial series for $`(1+th)^{q-1}`$ term by term against $`t\,dt`$. This gives precisely the coefficients $`\binom{q-1}{k}/(k+2)`$. It also proves $`g_q(h)>0`$ for real $`h>-1`$ and $`q>0`$.

Choose the analytic square root near $`h=0`$ satisfying $`\sqrt{g_q(0)}>0`$ and set

```math
z=h\sqrt{g_q(h)}.
```

Then

```math
1-\frac{P_q(X)}{c_q}=h^2g_q(h)=z^2,\qquad h=z\,g_q(h)^{-1/2}.
```

The second relation is another Lagrange inversion equation. Since its linear coefficient is nonzero, it has a unique analytic inverse $`h=h(z)`$ near zero. At the normalized level $`v=1-\delta`$, the two turning points correspond exactly to $`z=\pm\sqrt\delta`$ inside this local chart.

For every analytic observable $`H`$, Theorem 2.1 gives the general inverse-series algorithm

```math
[z^n]H(h(z))=\frac1n[h^{n-1}]H'(h)g_q(h)^{-n/2}\qquad(n\ge1).
```

### 9.2 Transform the period integral

The substitution $`X=X_*(1+h(z))`$ gives

```math
\frac{X^{q/2-1}\,dX}{\sqrt{P_q(X)-c_qv}}=\sqrt{q+1}\frac{(1+h(z))^{q/2-1}h'(z)}{\sqrt{\delta-z^2}}\,dz.
```

The factor $`\sqrt{q+1}`$ follows from the exact identity $`X_*^{q/2}/\sqrt{c_q}=\sqrt{q+1}`$. Thus

```math
\mathfrak p_q(1-\delta)=\sqrt{q+1}\int_{-\sqrt\delta}^{\sqrt\delta}\frac{(1+h(z))^{q/2-1}h'(z)}{\sqrt{\delta-z^2}}\,dz.
```

The moments of the fixed square-root kernel are

```math
\int_{-\sqrt\delta}^{\sqrt\delta}\frac{z^{2n}\,dz}{\sqrt{\delta-z^2}}=\pi\frac{\binom{2n}{n}}{4^n}\delta^n.
```

Odd moments vanish by symmetry.

### Theorem 9.1 — An all-orders analytic period expansion

For every fixed $`q>0`$, there is a positive radius $`R_q>0`$ for which the real period admits the *convergent* Taylor series

```math
\mathfrak p_q(1-\delta)=\pi\sqrt{\frac2q}\sum_{n=0}^\infty\beta_n(q)\delta^n,\qquad \beta_0(q)=1,\qquad |\delta|<R_q.
```

Its coefficients are explicitly and finitely computable:

```math
\beta_n(q)=\frac{\binom{2n}{n}}{4^n}\,g_0^{-n}\,[h^{2n}]\left\{(1+h)^{q/2-1}\left(\frac{g_q(h)}{g_0}\right)^{-n-1/2}\right\},\qquad g_0=\frac{q(q+1)}2.
```

**Proof, with all transformations shown.**

1. The function $`g_q`$ is analytic and nonzero near zero. Thus $`h(z)`$ and its derivative are analytic in some disk $`|z|<\rho`$.
2. Define $`F(z)=(1+h(z))^{q/2-1}h'(z)`$, likewise analytic for sufficiently small $`|z|`$.
3. For $`0<\delta<\rho^2`$ expand $`F(z)=\sum_{m\ge0}f_mz^m`$ uniformly on $`[-\sqrt\delta,\sqrt\delta]`$. Integrate term by term using the moments in Section 9.2:

```math
\mathfrak p_q(1-\delta)=\pi\sqrt{q+1}\sum_{n=0}^\infty f_{2n}\frac{\binom{2n}{n}}{4^n}\delta^n.
```

4. Set $`H(h)=(1+h)^{q/2}`$. Then $`\frac{d}{dz}H(h(z))=(q/2)F(z)`$.
5. By the Lagrange–Bürmann formula, for every $`n\ge0`$,

```math
[z^{2n+1}]H(h(z))=\frac{q/2}{2n+1}[h^{2n}](1+h)^{q/2-1}g_q(h)^{-(2n+1)/2}.
```

6. Differentiate coefficientwise in $`z`$, multiply by $`2/q`$, and conclude

```math
f_{2n}=[h^{2n}](1+h)^{q/2-1}g_q(h)^{-n-1/2}.
```

7. Substitute this coefficient into the period series. Since $`\sqrt{q+1}/\sqrt{g_0}=\sqrt{2/q}`$, the result is exactly the displayed formula for $`\beta_n(q)`$.
8. The analytic expansion of $`F(z)`$ and the even-moment integration prove a positive local radius of convergence in $`\delta`$, rather than merely a formal asymptotic expansion.

**Algorithmic consequence:** To compute $`\beta_n(q)`$, it suffices to know the Taylor coefficients of $`g_q(h)`$ through $`h^{2n}`$. In particular, the method never requires the global nonlinear solution $`U_q`$.

### 9.3 Explicit first and second coefficients

Performing the coefficient extraction at $`n=1`$ yields

```math
\beta_1(q)=\frac{(q+2)(2q+1)}{24q(q+1)}.
```

At $`n=2`$, finite algebra gives

```math
\beta_2(q)=\frac{(q+2)(2q+1)(50q^2+53q+2)}{2304q^2(q+1)^2}.
```

Consequently,

```math
\mathfrak p_q(v)=\pi\sqrt{\frac2q}\left(1+\frac{(q+2)(2q+1)}{24q(q+1)}(1-v)+\frac{(q+2)(2q+1)(50q^2+53q+2)}{2304q^2(q+1)^2}(1-v)^2+O((1-v)^3)\right).
```

The preceding conversational investigation had derived only the $`\beta_1`$ formula. The all-orders extraction and explicit $`\beta_2`$ are the principal extensions in this revised draft. These calculations are *not* claimed to be historically new without literature comparison.

### 9.4 Independent checks from known periods

The archived H147 formulas give

```math
\mathfrak p_1(v)=\pi\sqrt2\,{}_2F_1(1/4,3/4;1;1-v),\qquad \mathfrak p_2(v)=\pi\,{}_2F_1(1/6,5/6;1;1-v).
```

Their standard Gauss Taylor coefficients imply

```math
\beta_1(1)=\frac3{16},\quad \beta_2(1)=\frac{105}{1024};\qquad \beta_1(2)=\frac5{36},\quad\beta_2(2)=\frac{385}{5184}.
```

All four values agree *exactly* with Theorem 9.1.

The archived real-period reciprocity gives a second structural test. Since

```math
1-v^{1/q}=\frac{\delta}{q}+\frac{q-1}{2q^2}\delta^2+O(\delta^3),\qquad \delta=1-v,
```

the normalized coefficients must satisfy

```math
\beta_1(q)=\frac1q\beta_1(1/q),\qquad \beta_2(q)=\frac{\beta_2(1/q)}{q^2}+\frac{q-1}{2q^2}\beta_1(1/q).
```

Substitution and symbolic simplification of the rational expressions for $`\beta_1`$ and $`\beta_2`$ gives zero for both differences.

### 9.5 Independent nonlinear-oscillator derivation of the first coefficient

Set $`s=ru`$ and perturb the positive equilibrium $`U_*=(q/(4\mu(q+1)))^{q/2}`$ by $`U_q=U_*(1+h)`$. Expansion of the ODE gives

```math
\ddot h+2qh+(q+2)h^2+\frac{(q+2)(2-q)}{3q}h^3+O(h^4)=0.
```

For $`\ddot h+\omega_0^2h+ah^2+bh^3=0`$, the Poincaré–Lindstedt calculation gives the leading harmonic-amplitude period correction

```math
\frac{T_s}{2\pi/\omega_0}=1+\left(\frac{5a^2}{12\omega_0^4}-\frac{3b}{8\omega_0^2}\right)A^2+O(A^3).
```

Here $`\omega_0^2=2q`$, $`a=q+2`$ and $`b=(q+2)(2-q)/(3q)`$. From the turning-point fold of Section 7,

```math
A^2=\frac{q}{2(q+1)}(1-v)+O((1-v)^{3/2}).
```

The resulting first correction equals $`\beta_1(q)`$ above. The more exact *analytic normal-form proof* in Theorem 9.1 is needed to establish the integer-power series and all its higher coefficients.

## 10. Special levels and algebraic curve models

### 10.1 Level $`l=9`$: the Bring quintic

For $`q=4`$, the critical constant is $`c_4=256/3125`$ and the turning-point equation is

```math
X^4(1-X)=\frac{256}{3125}v.
```

Choose $`\lambda>0`$ so that $`\lambda^4=c_4v`$ and set $`X=\lambda/\xi`$. Multiplication by $`\xi^5/\lambda^4`$ yields

```math
\xi^5-\xi+\lambda=0.
```

The root $`\xi\to0`$ when $`\lambda\to0`$ satisfies $`\xi=\lambda+\xi^5`$, hence $`\xi=\lambda C_4(\lambda^4)`$. The generalized Fuss–Catalan function can be written with hypergeometric fifths:

```math
C_4(c_4v)={}_4F_3\!\left(\begin{matrix}1/5,\,2/5,\,3/5,\,4/5\\1/2,\,3/4,\,5/4\end{matrix};v\right).
```

Consequently,

```math
X_{4,+}(v)=\left[{}_4F_3\!\left(\begin{matrix}1/5,\,2/5,\,3/5,\,4/5\\1/2,\,3/4,\,5/4\end{matrix};v\right)\right]^{-1}.
```

At $`v=1`$, $`C_4(c_4)=5/4`$ and $`X_{4,+}=4/5`$. This agrees with the historical H147 Bring-quintic result. The **fifths** parameters describe a quintic root. The distinct **tenths** parameters in archived period formulas describe Abelian periods. Their roles must not be conflated.

### 10.2 Genus of the integer-level period models

The period differential is

```math
\omega_q=\frac{X^{q/2-1}\,dX}{\sqrt{X^q(1-X)-c_qv}}.
```

If $`q=2k`$ is an even positive integer, the numerator power is $`X^{k-1}`$, and a natural period curve is

```math
Y^2=X^q(1-X)-c_qv,\qquad q=2k.
```

For $`0<v<1`$ its polynomial is square-free and of degree $`q+1=2k+1`$, so its genus is $`k`$.

If $`q=2k+1`$ is odd, absorb the additional half-power of $`X`$ into the square root:

```math
Y^2=X\left[X^q(1-X)-c_qv\right],\qquad \omega_q=\frac{X^k\,dX}{Y}.
```

This model has square-free polynomial of degree $`q+2=2k+3`$ at noncritical level, so its genus is $`k+1`$. In summary,

```math
g(q)=\left\lceil\frac q2\right\rceil,\qquad q\in\mathbb Z_{>0},\quad 0<v<1.
```

Thus $`q=1,2`$ give genus-one models; $`q=3,4`$ give genus-two models. The curves degenerate at $`v=0`$ and $`v=1`$, where this generic-genus statement does not apply. For irrational $`q`$, $`X^q`$ is not globally algebraic in $`X`$; the integer genus formula must not be extrapolated.

## 11. Symbolic checks and reproducibility

The following checks were completed independently of the narrative derivations:

1. Differentiate the $`q`$-energy and verify the conserved quantity.
2. Substitute $`C=1/X`$ and $`Y=1-X`$ into the turning-point equation.
3. Substitute the first three inverse-series coefficients back into the defining equations.
4. Expand the fold at equilibrium to verify the two Puiseux coefficients.
5. Derive the $`n^{-3/2}`$ Fuss–Catalan asymptotic from Stirling's formula.
6. Extract $`\beta_1(q)`$ and $`\beta_2(q)`$ symbolically from Theorem 9.1.
7. Verify exact agreement with the $`q=1,2`$ hypergeometric periods and reciprocal $`q\leftrightarrow1/q`$ coefficient identities.

A minimal independently executable SymPy check for the two period coefficients follows.

```python
import sympy as sp

q, h = sp.symbols("q h", positive=True)
g0 = q*(q+1)/2
g = q*(q+1)*sum(
    sp.binomial(q-1, k)*h**k/sp.Integer(k+2)
    for k in range(5)
)

def beta(n):
    expr = (1+h)**(q/2-1)*(g/g0)**(-sp.Rational(2*n+1, 2))
    coefficient = sp.series(expr, h, 0, 2*n+1).removeO().coeff(h, 2*n)
    return sp.factor(sp.binomial(2*n, n)/4**n*coefficient/g0**n)

b1 = (q+2)*(2*q+1)/(24*q*(q+1))
b2 = (q+2)*(2*q+1)*(50*q**2+53*q+2)/(2304*q**2*(q+1)**2)

assert sp.simplify(beta(0)-1) == 0
assert sp.simplify(beta(1)-b1) == 0
assert sp.simplify(beta(2)-b2) == 0
assert sp.simplify(b1-b1.subs(q, 1/q)/q) == 0
assert sp.simplify(
    b2-b2.subs(q, 1/q)/q**2-(q-1)*b1.subs(q, 1/q)/(2*q**2)
) == 0
print("symbolic checks passed")
```

High-precision turning-point comparisons at $`v=0.86`$ used $`q=1/2,1,\sqrt2,2,3,4`$. The outer $`C_q`$ series, truncated after 400 terms with 55-digit working precision, agreed with numerical roots to approximately $`10^{-30}`$. The inner reciprocal series converged more slowly at higher $`q`$ because the effective argument approaches its convergence boundary.

For the period integral, the substitution

```math
X=X_-+(X_+-X_-)\sin^2\theta,\qquad 0\le\theta\le\pi/2
```

regularizes both endpoint square-root singularities. Quadrature at $`v=0.997`$ agreed with the second-order period expansion of Section 9.3 to relative errors around $`10^{-9}`$ for the six values above. Such checks are evidence, not a substitute for the analytic proof or certified interval bounds.

## 12. Claim-by-claim consolidation destinations

The table separates **the mathematical destination** from the **evidence review**. A draft is not canonical simply because it appears in this repository.

| Proposed result | Draft source | Historical provenance | Candidate layer and chapter | Review state |
|---|---|---|---|---|
| Catalan inverse of $`S`$ and logistic/logarithmic reconstruction | Section 3.1–3.3 | Canonical Riccati/conic fields | Layer I: Riccati and Conic Structures | Stepwise proof; independent audit pending |
| Arctangent/Gudermannian half-split reconstruction | Section 3.4 | Canonical primitive | Layer I: Integral Representations | Stepwise proof; independent audit pending |
| Generalized Fuss–Catalan outer turning point | Section 5 | H147 | Layer I: Level Hierarchy | Classical inversion mechanism, application proved |
| Puiseux inner branch and exact reciprocal turning points | Section 6 | H147–H148 | Layer I: Energy Classification | Stepwise proof; global continuation open |
| Critical fold and inverse-series convergence | Section 7 | H147 | Layer I: Energy Classification | Derivation and Stirling proof |
| Real period integral and reciprocal identity | Section 8 | H147–H148 | Layer III: Period Correspondences | Historical result cited; source audit recommended |
| **All-orders local period coefficient theorem** | Section 9 | H147–H148 plus extended derivation | Layer III: Period Correspondences | Stepwise proof plus independent symbolic checks |
| Bring-quintic and integer-level curve genus | Section 10 | H147 | Layer III: Algebraic Inversion and Period Curves | Algebraic derivation; geometric model audit recommended |

No new permanent CLAIMS ID has been allocated. The references H147, H148 and H151 identify *historical source records*, not automatic approvals. Assign final theorem and equation identifiers only when the individual statements are promoted into the authoritative DLMF-style sequence.

## 13. Corrections, caveats and next questions

1. **Coefficient correction.** At $`q=1/2`$ the coefficient of $`t^3`$ in $`C_q(t)`$ is $`21/8`$, not $`3`$.
2. **Different local variables.** The outer turning point has a Taylor series in $`v`$ around zero; the inner branch generally requires a series in $`v^{1/q}`$.
3. **Different radii of convergence.** The exact radius $`c_q`$ refers to the Fuss–Catalan turning-point series. The **global** radius of the period's Taylor series near $`v=1`$ is not determined here.
4. **Fold versus period regularity.** Turning-point derivatives diverge at $`v=1`$, while the period possesses an ordinary analytic expansion in $`1-v`$ there.
5. **Distinct hypergeometric roles.** At $`q=4`$, the fifths function in the Bring inverse and the tenths functions in the period representation are not the same object.
6. **Integer versus real parameters.** The local analytic inversion and period theorem hold for all $`q>0`$; the algebraic-curve genus models in Section 10 were established only for positive integers $`q`$.
7. **Reciprocal domains.** Real turning-point reciprocity is exact. It does not, without additional evidence, prove equality of complex monodromy groups or Jacobians.
8. **No forced physical interpretation.** The framework's ODE, periods, and coordinate maps are mathematical constructions. Physical terminology adds no hypotheses or conclusions to these proofs.
9. **Literature novelty remains open.** Lagrange–Bürmann, Fuss–Catalan inversion, analytic Morse coordinates, and oscillator-period expansions are established techniques. No claim of historical originality is made here for the resulting formulas.

**Recommended further work:** compute $`\beta_3(q)`$ from Theorem 9.1, obtain recurrence relations for $`\beta_n(q)`$, compare with action-angle/Birkhoff normal forms, determine the complex singularities controlling the period-series radius, and verify the precise birational maps to the archived Weierstrass/genus-two models. Then review each result in dependency order rather than attempting to publish the entire draft unchanged.

## 14. Reference sources

- [NIST DLMF, Section 1.10(vii): Inverse Functions](https://dlmf.nist.gov/1.10.vii), containing the classical inverse-function and Lagrange inversion framework.
- [Wolfram MathWorld: Lagrange Inversion Theorem](https://mathworld.wolfram.com/LagrangeInversionTheorem.html).
- Historical archive, '04-follow-ups/fox-h-reading.md', $`q=4`$ quintic and Mellin/period distinctions.
- Historical archive, '04-follow-ups/period-hierarchy.md', normalized period and reciprocal-parameter structure.
- User-supplied historical 'CLAIMS(6).md', particularly H147, H148, H151.
- [01-foundational/010 Variables and Normalizations](../01-foundational/010%20Variables%20and%20Normalizations.md).
- [01-foundational/020 The Linear Exponential Backbone](../01-foundational/020%20The%20Linear%20Exponential%20Backbone.md).
- [Draft folder policy and numbering](README.md).

**End of provisional investigation 000.** Preserve this complete derivation and its audit trail when migrating individual verified statements into their authoritative mathematical sections.
