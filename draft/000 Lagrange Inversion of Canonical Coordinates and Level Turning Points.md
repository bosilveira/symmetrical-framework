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
