---
id: SF-DRAFT-210
title: Elliptic BA–Weierstrass Spin Divisor Compatibility and Connection Obstructions
status: provisional
created: 2026-11-19
proposed_layers: [I, II, III]
depends_on: [SF-DRAFT-150, SF-DRAFT-160, SF-DRAFT-170, SF-DRAFT-180, SF-DRAFT-190, SF-DRAFT-200]
related_claims: [H95, H100, H136, H299, H329, H332, H421, H466, H467, H468, H469, H470]
---

# 210 Elliptic Baker–Akhiezer, Weierstrass Spin Divisors, and Connection Obstructions

**Status:** Provisional mathematical investigation; not promoted to CLAIMS.md or foundational paper. Tags: [D] proved directly, [V] independently symbolically checked, [K] established theorem under hypotheses, [H] prior archive, [C] correction/counterexample, [O] open. Historical priority is not asserted.

**Research question.** The selected smooth one-gap Lamé spectral elliptic curve is already explicitly real-isomorphic (draft 170) to the conformal elliptic curve supporting Riemann's minimal examples. Can the Lamé Baker–Akhiezer eigenline, the Kusner–Schmitt Weierstrass spin line, and the Gauss-pulled Hopf line be related **globally**, and can their natural connections be identified? Is the Euclidean–Lorentzian Weierstrass/Kobayashi comparison a change of real form of the same holomorphic spinor data?

**Primary results.** (1) The Riemann Gauss function has divisor $2P_0-2P_\infty$ and **forces the nontrivial 2-torsion WE spin line** $S_R=\mathcal O(P_0-P_\infty)$; the Gauss-pulled tautological line $H_R=\mathcal O(-2P_\infty)$ obeys an exact degree-correcting divisor twist. (2) The selected one-gap Lamé moving Dirichlet point $\gamma(u)$ has an **explicit Jacobi elliptic formula**, its squared eigenfunction obeys the Drach third-order equation and a cubic first integral, and its Abel coordinate moves linearly. (3) The degree-zero **Dirichlet divisor class** equals the selected WE spin class only at **distinguished half-period phases**, not for generic real spatial $u$. (4) The spin line admits a **fully explicit Weierstrass sigma/half-period uniformization**; it is not globally the trivial scalar square root of the Gauss function. (5) The spectral second-kind irregular singularity and the smooth nonzero Chern curvature of the Gauss Hopf connection prohibit the claimed automatic **connection-preserving** equivalence. (6) Euclidean WE and Lorentz–Minkowski Kobayashi representations share holomorphic null-spinor algebra, but their **different real forms and metric signs** can turn a regular Euclidean surface into a singular Lorentzian maximal surface.

**Source provenance.** Attached Pasted text(20261119-054845).txt inspected in full, especially its proposed exact divisor ladder, automatic branch-point assertion, and claimed removal of a quasimomentum double pole by a holomorphic differential. The actual November 18 GitHub project ZIP was reopened (Lamé complementary loci, Riemann marked periods, H136 Sato–Grassmannian, fundamental forms/Hopf). Live drafts 170, 180, 190, 200 reopened. Independent literature: Kusner–Schmitt spinors, Kobayashi maximal surfaces, Dubrovin/Krichever finite-gap BA and DLMF Weierstrass functions (see §25).

## 1. Separate three curve/bundle categories before making identifications

Fix $0<m<1$ and $r,c,\mu>0$; $u=\ln(x/c)$ is the canonical logarithmic coordinate. The real one-gap Lamé operator is a **selected additional spectral problem**

```math
L_m=-\partial_u^2+V_m(u),\qquad V_m=2mr^2\mathrm{sn}^2(ru\mid m)-2mr^2.
```

It is distinct from the canonical free linear Master carrier $-\partial_u^2+r^2$ and from the quadratic-projective WE spinor carrier (draft 200). Its spectral variable $E$ is held fixed as $u$ evolves.

The smooth elliptic Lamé spectral curve $\Gamma_m$ is not the two-dimensional Euclidean ambient space, nor is a point $P\in\Gamma_m$ the spatial coordinate $u$. The independently decorated Riemann elliptic conformal curve $E_R$ is **isomorphic as a real algebraic curve** to this selected $\Gamma_m$, but the isomorphism does not automatically equate the spatial SL connection, BA divisor normalization, WE spin structures or Hopf Chern connection.

**Line-bundle terminology [C].** A degree-one **fixed pole-divisor line** of a traditional Baker–Akhiezer normalization, the **moving Dirichlet zero divisor** from a squared eigenfunction, and the **eigenline** of a chosen 2-by-2 polynomial Lax matrix are not definitionally identical. They are related through chosen normalizations and duality conventions; this manuscript explicitly compares the **moving divisor class** $D(u)=\mathcal O(\gamma(u)-P_\infty)$ and states any BA interpretation conditionally. The attached proposal uses the name "BA eigenline" for several of these distinct objects.

## 2. Exact matched spectral and Riemann elliptic curves [H170,D]

For Lamé define band edges and the spectral cubic

```math
E_0=-mr^2,\qquad E_1=(1-2m)r^2,\qquad E_2=(1-m)r^2,
```

```math
\Gamma_m:\quad\eta^2=-(E-E_0)(E-E_1)(E-E_2),\qquad E_0<E_1<E_2.
```

The band spectrum of the periodic real operator is $[E_0,E_1]\cup[E_2,\infty)$, with the single finite *forbidden gap* $(E_1,E_2)$. Its two gap endpoints correspond to the Jacobi edge eigenfunctions $\mathrm{cn}$ and $\mathrm{sn}$.

The Riemann minimal-example elliptic curve uses an independent positive modulus $\lambda_R>0$:

```math
E_R:\quad w_R^2=g_R(g_R-\lambda_R)(\lambda_Rg_R+1),\qquad y_R=w_R/\sqrt{\lambda_R}.
```

Set

```math
m=\frac1{1+\lambda_R^2},\quad k_R=\lambda_R^{-1}-\lambda_R,\quad D_R=\lambda_R+\lambda_R^{-1}.
```

The checked draft-170 real affine curve isomorphism is

```math
g_R=-k_R-\frac{D_R}{r^2}E,\qquad y_R=\frac{D_R^{3/2}}{r^3}\eta,\qquad \frac{dg_R}{y_R}=-\frac{r}{\sqrt{D_R}}\frac{dE}{\eta}.
```

It maps the Lamé branch points $E_0,E_1,E_2$ to $\lambda_R,0,-\lambda_R^{-1}$, respectively. Let $P_\infty$ be the unique point at infinity and $P_0$ the branch point above $g_R=0$ (equivalently $E=E_1$). Let $P_+$ and $P_-$ denote the other finite branch points above $\lambda_R$ and $-1/\lambda_R$. All three finite branch points are nontrivial elliptic 2-torsion points when $P_\infty$ is the group origin.

## 3. The Gauss map selects one exact spin structure [D,V,K]

Since $g_R$ has degree two on the compactified elliptic curve, with double zero at $P_0$ and double pole at infinity,

```math
\operatorname{div}(g_R)=2P_0-2P_\infty,\qquad 2(P_0-P_\infty)\sim0.
```

The difference $P_0-P_\infty$ is **nonprincipal**: it is nonzero 2-torsion, because $P_0\ne P_\infty$ on a smooth elliptic curve. The global differential

```math
\omega_R=\frac{dg_R}{y_R}
```

is holomorphic and nowhere vanishing; hence $K_{E_R}\simeq\mathcal O_{E_R}$. There are four spin structures (2-torsion classes); the *specific* WE data will pick one.

For the archived height normalization

```math
dh_R=A_R\frac{dg_R}{w_R}=\frac{A_R}{\sqrt{\lambda_R}}\omega_R,\qquad A_R>0,
```

the WE spinor squares require

```math
p^2=\frac{dh_R/dz}{g_R},\qquad q^2=g_R(dh_R/dz),\qquad q/p=g_R
```

in a local nonvanishing holomorphic differential chart $dz$. The divisors of the squared half-differentials are

```math
\operatorname{div}(p^2\,dz)=2P_\infty-2P_0,\qquad\operatorname{div}(q^2\,dz)=2P_0-2P_\infty.
```

Their compatible **half-divisors** are $P_\infty-P_0$ and $P_0-P_\infty$, which represent the same 2-torsion class. Thus the actual Riemann Weierstrass data select

```math
\boxed{\quad S_R\simeq\mathcal O_{E_R}(P_0-P_\infty),\qquad S_R^{\otimes2}\simeq K_{E_R}\simeq\mathcal O.\quad}
```

**Theorem 3.1 [D,V] (unique selected 2-torsion WE spin class).** Given the specified $g_R,dh_R$ with the above double-zero/double-pole divisors, their local square-root WE spinors globalize as *meromorphic sections of the nontrivial spin class* $S_R$. They cannot be globally meromorphic scalar square roots of $g_R$ on the torus, because $P_0-P_\infty$ is not principal.

**Key caveat.** A nontrivial degree-zero line bundle on a compact elliptic curve has no nonzero **holomorphic global sections**. These spinors are **meromorphic with allowed poles at punctures** (the planar ends), as in Kusner–Schmitt; a globally holomorphic scalar spinor pair on the entire compact elliptic curve is not being claimed.

## 4. The Gauss-pulled Hopf tautological line has an EXACT divisor relation [D,V]

Let $H_R=g_R^*\mathcal O_{\mathbb P^1}(-1)$, the **holomorphic tautological line** of degree $-2$. Since the inverse image of the point at infinity is the divisor $2P_\infty$,

```math
H_R\simeq\mathcal O_{E_R}(-2P_\infty),\qquad H_R^\vee\simeq\mathcal O_{E_R}(2P_\infty).
```

Now compare with the selected spin class:

```math
S_R\otimes\mathcal O(-P_0-P_\infty)=\mathcal O(-2P_\infty)\simeq H_R.
```

**Theorem 4.1 [D,V] (the exact WE/Hopf divisor twist).**

```math
\boxed{\quad H_R\otimes\mathcal O(P_0+P_\infty)\simeq S_R.\quad}
```

This is a **true global holomorphic line-bundle isomorphism** once the GAUSS-MAP-SELECTED spin structure is specified. It does not identify the natural Hermitian **connections**: $H_R$ has nonzero Chern curvature, and the degree-zero spin structure permits a flat finite-holonomy connection. A divisor twist is an isomorphism of underlying holomorphic line bundles, not an automatic connection-preserving gauge.

The convention $A_B=-i\eta^\dagger d\eta$ for a normalized Hopf/Berry spinor gives a positive sphere-area curvature and physicists' Berry Chern number $+2$. In standard holomorphic mathematics the tautological $\mathcal O(-1)$ has $c_1=-1$. These are **opposite sign conventions for the curvature-to-Chern conversion**: the underlying absolute degree is two; distinguish $H_R$ from its dual and the convention used to pair curvature with $c_1$.
