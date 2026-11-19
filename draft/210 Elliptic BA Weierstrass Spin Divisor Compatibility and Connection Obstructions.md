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

## 5. Explicit Weierstrass uniformization and the sigma-function spinor [D,V,K]

The selected Riemann elliptic model is

```math
y_R^2=g_R^3+k_Rg_R^2-g_R.
```

Translate to the standard Weierstrass model by

```math
X_W=g_R+\frac{k_R}{3},\qquad Y_W=2y_R.
```

Then

```math
Y_W^2=4X_W^3-G_2X_W-G_3,\quad G_2=4\left(1+\frac{k_R^2}{3}\right),\quad G_3=-4\left(\frac{k_R}{3}+\frac{2k_R^3}{27}\right).
```

Let $\Lambda_R$ be the period lattice for these Weierstrass invariants and define the Abel coordinate $z$ with

```math
dz=\frac{dg_R}{2y_R},\quad P_\infty\longleftrightarrow z=0,\quad g_R(z)=\wp(z;G_2,G_3)-e_0,\quad e_0=\frac{k_R}{3}.
```

The point $P_0$ corresponds to a **nonzero half-period** $a$ satisfying

```math
\wp(a)=e_0,\qquad 2a\in\Lambda_R,\qquad a\notin\Lambda_R.
```

A standard sigma addition identity is

```math
\wp(z)-\wp(a)=-\frac{\sigma(z+a)\sigma(z-a)}{\sigma(z)^2\sigma(a)^2}.
```

For the half-period $a$, sigma quasi-periodicity reduces this to the **exact square** of a quasi-periodic spinor section:

```math
h_a(z)=\frac{\sigma(z-a)}{\sigma(z)\sigma(a)}\exp\big(\zeta(a)z\big),\qquad h_a(z)^2=\wp(z)-e_0=g_R(z).
```

The symbol $\zeta$ in the exponential is the **Weierstrass zeta function**, NOT the framework's surface conformal coordinate; the independent Abel variable here is $z$.

**Proof of the square identity.** Since $2a$ is a period, $\sigma(z+a)=-e^{2\zeta(a)z}\sigma(z-a)$ (with the chosen half-period representative and standard sigma normalization). Substitute into the preceding addition formula.

The spinor section has a simple zero at $P_0$ and a simple pole at $P_\infty$ on the uniformizing plane. Its multipliers under $z\mapsto z+\lambda$, $\lambda\in\Lambda_R$, are $\pm1$ (not all $+1$): $h_a$ is a **meromorphic section of a nontrivial flat 2-torsion line**, not an elliptic meromorphic scalar function.

### 5.1 Explicit global WE spinor pair in the correct theta characteristic

The Riemann height differential is

```math
dh_R=A_R\frac{dg_R}{w_R}=\beta_R\,dz,\qquad \beta_R=\frac{2A_R}{\sqrt{\lambda_R}}>0.
```

Choose a square root $\sqrt{\beta_R}$ and define, on the universal covering plane with the correct half-period sign multipliers,

```math
p_R(z)=\frac{\sqrt{\beta_R}}{h_a(z)},\qquad q_R(z)=\sqrt{\beta_R}\,h_a(z).
```

They satisfy

```math
p_R^2dz=\frac{dh_R}{g_R},\quad q_R^2dz=g_R\,dh_R,\quad q_R/p_R=g_R,\quad p_Rq_R=\beta_R.
```

The local divisors (interpreted as meromorphic sections of their nontrivial spin line) are

```math
\operatorname{div}(p_R)=P_\infty-P_0,\quad\operatorname{div}(q_R)=P_0-P_\infty.
```

The common bundle class is $S_R=\mathcal O(P_0-P_\infty)$ because the two divisors differ by the **principal** divisor $\operatorname{div}(g_R)=2P_0-2P_\infty$.

**Theorem 5.1 [D,V,K] (explicit meromorphic elliptic WE spinor).** The sigma ratio $h_a$, with its half-period multipliers, is an explicit uniformization of the selected nontrivial WE spin structure. Its squared components reproduce all of the archived Riemann WE forms, with $A_R,\lambda_R$ retained. This is a constructive version of the abstract line-class identity of §3.

### 5.2 The Wronskian and natural Schwarzian carrier are ALSO explicit

Since $g_R=h_a^2$,

```math
p_R(q_R)_z-(p_R)_zq_R=\beta_R\frac{(g_R)_z}{g_R}=\beta_R\frac{\wp'(z)}{\wp(z)-e_0}.
```

The surface Hopf quadratic differential is

```math
\Theta_R=\frac{dg_R}{g_R}dh_R=\beta_R\frac{\wp'(z)}{\wp(z)-e_0}\,dz^2.
```

In the convention of draft 200, $Q_{H,R}=-\Theta_R/2$. On patches where $\Theta_R$ is nonzero and finite, the natural coordinate

```math
d\xi=\sqrt{\Theta_R}=\sqrt{\beta_R\frac{\wp'(z)}{\wp(z)-e_0}}\,dz
```

normalizes the WE spinor Wronskian to one and yields the projective carrier $\psi_{\xi\xi}+\frac12\{g_R,\xi\}\psi=0$. Its potential is generally **not** the real spatial one-gap Lamé potential. The natural coordinate may branch at zeros/poles of $\Theta_R$ and does not generally descend to a single global affine coordinate on $E_R$.

## 6. Exact one-gap Lamé moving Dirichlet divisor [D,V,K]

For the real selected shifted Lamé potential and band edges of §2, define the **moving gap coordinate**

```math
\gamma(u)=r^2\left(1-m-m\,\mathrm{sn}^2(ru\mid m)\right).
```

Since $0\le\mathrm{sn}^2(ru|m)\le1$ for real $u$,

```math
E_1\le\gamma(u)\le E_2,\qquad\gamma(0)=E_2,\qquad \gamma(K(m)/r)=E_1.
```

At the endpoints the gap point reaches the finite branch points on $\Gamma_m$; for generic real $u$ it lies **inside the finite forbidden gap**, not on the allowed finite band $[E_0,E_1]$.

Choose the sheet of $\Gamma_m$ along this real motion with

```math
\eta_\gamma(u)=mr^3\,\mathrm{sn}(ru)\mathrm{cn}(ru)\mathrm{dn}(ru).
```

The usual Jacobi differentiation identities give the exact **Dubrovin equation**

```math
\gamma_u=-2mr^3\,\mathrm{sn}(ru)\mathrm{cn}(ru)\mathrm{dn}(ru)=-2\eta_\gamma.
```

**Theorem 6.1 [D,V] (one-gap Dirichlet divisor trajectory).** The marked moving gap point $(\gamma(u),\eta_\gamma(u))\in\Gamma_m$ has the exact displayed Jacobi parametrization. It meets the **particular** Riemann branch point $P_0$ (corresponding to Lamé $E_1$) precisely at

```math
u_*=K(m)/r\pmod{2K(m)/r}.
```

In original multiplicative coordinates the distinguished centers are

```math
x_*=c\,e^{K(m)/r}\,e^{2jK(m)/r},\qquad j\in\mathbb Z.
```

At $u=0\pmod{2K/r}$ the point instead meets $E_2$ (the Riemann branch $g_R=-1/\lambda_R$); at generic $u$ it is not a branch point. A shifted Lamé potential $V_m(u-u_0)$ shifts both distinguished sets by $u_0$.

### 6.1 Exactly which divisor class matches the Riemann spin structure

Let $\mathcal D(u)=\mathcal O_{\Gamma_m}(\gamma(u)-P_\infty)$ be the **degree-zero class of the moving Dirichlet point**, with $\gamma(u)$ understood as a point ON the spectral curve, not just its energy coordinate. Transfer it across the exact real affine curve map to $E_R$.

Then Abel's theorem for a genus-one curve gives

```math
\mathcal D(u)\simeq S_R\quad\Longleftrightarrow\quad \gamma(u)=P_0.
```

The equality is an isomorphism of degree-zero holomorphic lines; it does **not** identify a chosen normalized BA meromorphic connection or its essential singularity. For real Lamé evolution the condition holds at the discrete positions $u_*$ of Theorem 6.1, and not for generic $u$.

**Important correction to the attachment [C].** The claim that the one-gap Dirichlet point is "automatically" at a branch point for every origin of a real self-adjoint Lamé potential is false. Reality confines the point to a real gap oval; it does not freeze it at a half-period. Moving the spatial origin changes its Abel phase continuously.

## 7. Exact Drach squared-eigenfunction certificate [D,V]

Let $R(u,E)=E-\gamma(u)$. Its derivatives satisfy the **third-order linear squared-eigenfunction equation**

```math
R_{uuu}-4(V_m-E)R_u-2(V_m)_u R=0.
```

The following quadratic invariant is independent of $u$:

```math
R_u^2-2RR_{uu}+4(V_m-E)R^2=4\eta(E)^2=-4(E-E_0)(E-E_1)(E-E_2).
```

**Theorem 7.1 [D,V] (finite-gap certificate).** Both identities hold as exact polynomials in the independent variables $E,r,m,t$, with $t=\mathrm{sn}^2(ru|m)$. They certify that $\gamma(u)$ is the natural one-gap Dirichlet coordinate for the chosen Lamé carrier and that $\Gamma_m$ is its actual stationary spectral cubic.

**Proof.** Use

```math
t_u^2=4r^2t(1-t)(1-mt),\quad t_{uu}=2r^2[1-2(1+m)t+3mt^2].
```

Substitute $\gamma=r^2(1-m-mt)$, $R=E-\gamma$, and $V_m=2mr^2t-2mr^2$. Direct expansion yields zero for the third-order equation and the exact factorized cubic for the invariant. Both residuals were independently evaluated by SymPy and simplified identically to zero.

For generic spectral $P=(E,\eta)\in\Gamma_m$ and on intervals avoiding $R(u,E)=0$, the corresponding normalized local Floquet/Baker-type solutions may be expressed as

```math
\psi_\pm(u,P)=\sqrt{R(u,E)}\exp\left(\pm\eta(P)\int_{u_0}^u\frac{ds}{R(s,E)}\right)
```

up to a spectral normalization factor and local square-root branch. They satisfy

```math
-\psi_{\pm,uu}+V_m(u)\psi_\pm=E\psi_\pm,\qquad \mathscr W_u(\psi_+,\psi_-)=\mp2\eta(P)
```

with the Wronskian sign depending on the ordered pair. The zero of $R(u,E)$ at $E=\gamma(u)$ is the moving Dirichlet point; a **standard global BA function** can also be normalized with a *fixed pole divisor* and moving zeros. Choosing one normalization is necessary before calling $\mathcal D(u)$ "the BA eigenline".

## 8. Explicit Picard/Jacobian transport: the missing all-modulus bridge [D,V]

Set the Abel integral on $\Gamma_m$ using the holomorphic form $dE/\eta$, with base point $P_\infty$:

```math
\mathcal A_{\rm sp}(P)=\int_{P_\infty}^{P}\frac{dE}{\eta}\pmod{\Lambda_{\rm sp}}.
```

Along the **moving Dirichlet point**, Dubrovin's equation gives

```math
\frac{d}{du}\mathcal A_{\rm sp}(\gamma(u))=\frac{\gamma_u}{\eta_\gamma}=-2.
```

Thus the evolution of the degree-zero Dirichlet class in $\operatorname{Pic}^0(\Gamma_m)$ is **exactly linear** in the canonical logarithmic coordinate:

```math
\mathcal A_{\rm sp}(\gamma(u))=\mathcal A_{\rm sp}(\gamma(u_*))-2(u-u_*)\pmod{\Lambda_{\rm sp}}.
```

Under draft 170's curve map, use the normalized Riemann Weierstrass coordinate $z_R$ of §5:

```math
dz_R=\frac{dg_R}{2y_R}=-\frac{r}{2\sqrt{D_R}}\frac{dE}{\eta}.
```

Combining the two identities yields the **new exact all-modulus Abel–Jacobi transport slope**

```math
\frac{dz_R(\gamma(u))}{du}=\frac{r}{\sqrt{D_R}},\qquad z_R(\gamma(u))=a+\frac{r}{\sqrt{D_R}}(u-u_*)\pmod{\Lambda_R}.
```

**Theorem 8.1 [D,V] (selected spectral-to-Riemann Picard flow).** For the entire smooth real matched family $0<m<1$, the moving one-gap Dirichlet divisor class traverses the Riemann elliptic Picard torus along an explicit affine straight line, with slope $r/\sqrt{D_R}$. It hits the **selected WE theta characteristic** $S_R=\mathcal O(P_0-P_\infty)$ exactly at the distinguished Lamé half-period positions.

This result identifies a **precise relationship between the spatial SL flow and a line-bundle class on the Riemann elliptic curve**. It is NOT the claim that the Riemann Gauss-map coordinate $g_R(E)$ moves with $u$ under the original fixed-$E$ SL equation: here the point $P=\gamma(u)$ is explicitly selected to MOVE on the spectral curve.

### 8.1 A genuinely global compatibility criterion

A degree-zero line on an elliptic curve is spin iff it is 2-torsion. Therefore

```math
\mathcal D(u)^{\otimes2}\simeq\mathcal O\quad\Longleftrightarrow\quad \gamma(u)\in\{P_\infty,P_0,P_+,P_-\}.
```

On the **real gap branch** of the chosen Lamé potential, only the endpoints $E_1$ and $E_2$ are reached; the selected Riemann WE spin is $P_0=E_1$, not the other endpoint. This is the exact mathematical content hidden in the proposal's branch-point intuition.

## 9. Exact sigma–theta half-period versus moving BA divisor [D,K,C]

The WE spin structure in §5 is determined by a **fixed** half-period $a=z_R(P_0)$. The moving Dirichlet point of §8 instead has Abel coordinate

```math
z_\gamma(u)\equiv a+\frac{r}{\sqrt{D_R}}(u-u_*)\pmod{\Lambda_R}.
```

Thus a convenient representative of the moving degree-zero class is

```math
D(u)=\mathcal O_{E_R}\big(P_{z_\gamma(u)}-P_\infty\big),
```

where $P_z$ denotes the point with Abel coordinate $z$.

The abstract identity with the fixed spin class is

```math
D(u)\otimes S_R^{-1}\simeq\mathcal O_{E_R}\big(P_{z_\gamma(u)}-P_a\big)\in\operatorname{Pic}^0(E_R).
```

The right side is the **Jacobian translation** by $r(u-u_*)/\sqrt{D_R}$. It is trivial precisely when that translation lies in the period lattice. This gives a complete answer to the attached proposed BA/spin matching **at the level of the moving Dirichlet divisor class**.

One can express a meromorphic section of $\mathcal O(P_b-P_a)$ through a standard sigma quotient with exponential correction: for Abel representatives $a,b$,

```math
\frac{\sigma(z-b)}{\sigma(z-a)}\,\exp\big((\zeta(b)-\zeta(a))z\big),
```

with quasi-period multipliers determined by $a-b$. In general this is not a globally elliptic *function* unless $a-b$ is a period; it is a local representation of a section of the **nontrivial degree-zero line** and its multipliers. This theta/sigma distinction is essential: a nonprincipal divisor class cannot be turned into a principal divisor merely by writing a theta quotient.

**Theorem 9.1 [D,K] (all-modulus Picard compatibility).** After choosing a specific normalized moving Dirichlet divisor convention, the relationship between the selected WE spin class and the evolving one-gap spectral divisor is a **nonconstant straight-line translation in $\operatorname{Pic}^0(E_R)$**. At distinguished spatial phases this translation vanishes, yielding the exact degree-zero holomorphic line isomorphism of §6; away from them it does not.

### 9.1 Fixed Baker–Akhiezer poles must not be identified with moving zeros

In the standard algebro-geometric BA construction one initially chooses a nonspecial **fixed pole divisor** $D_*$ of degree $g=1$, a point at infinity, a local spectral parameter and a normalization. The BA function has an essential exponential at infinity and permitted poles at the **fixed $D_*$**. As spatial $u$ varies, its spectral zeros and its corresponding Dirichlet data may move. A different normalization can trade moving zeros for moving poles, but this must be written explicitly.

Consequently the formula $D(u)=\mathcal O(\gamma(u)-P_\infty)$ is **not, without an extra convention, the fixed Baker–Akhiezer pole bundle**. This audit prevents a nominal equality of line-bundle symbols from masquerading as a theorem about the actual eigenline and its spectral connection.

## 10. Irregular spectral singularity: an exact principal-part obstruction [D,V,C]

In the selected Lamé elliptic curve, introduce a local coordinate at spectral infinity

```math
t=E^{-1/2},\qquad E=t^{-2},\qquad\eta\sim i\,t^{-3}.
```

Then

```math
\frac{dE}{\eta}=2i\,dt+O(t^2)\,dt.
```

The Riemann holomorphic height differential transported in draft 170 is

```math
dh_R=-A_Rr\sqrt m\,\frac{dE}{\eta}=-2iA_Rr\sqrt m\,dt+O(t^2)\,dt.
```

By contrast, the **normalized spectral quasimomentum differential of the second kind** constructed in draft 170 §23 has the form

```math
dp_{\rm sp}=\frac i2(E-b)\frac{dE}{\eta},
```

where $b$ is chosen by a zero marked period. Its leading local expansion is

```math
dp_{\rm sp}=-\frac{dt}{t^2}+O(1)\,dt.
```

**Theorem 10.1 [D,V,C] (no holomorphic-height cancellation of the irregular type).** For every finite scalar constant $C$,

```math
dp_{\rm sp}-C\,dh_R=-\frac{dt}{t^2}+O(1)\,dt.
```

Thus subtracting a first-kind Riemann height form cannot strip the spectral quasimomentum's double pole. This directly **falsifies** the attached suggestion that a combination $dp-Cdh$ becomes regular or logarithmic automatically.

The BA exponential has an essential factor of type $\exp(\pm u/t)$ at spectral infinity for nonzero spatial $u$. A local gauge of type $\exp(\mp u/t)$ can remove this *local irregular exponential*, but it is **not a meromorphic gauge at the compactified point**; global normalization, monodromy and bundle/connection classes remain to be matched. A genuine meromorphic gauge cannot erase the formal irregular type.

### 10.1 A meromorphic connection is extra spectral data

The BA eigenfunction is initially a meromorphic/exponentially singular function of a **spectral point**, depending parametrically on the spatial coordinate. The $u$-direction Lax equation is a different transport equation. To speak of a connection in the **spectral-curve direction**, one must define its normalization, e.g. a chosen meromorphic differential $d_P\log\psi$ or a spectral line connection with prescribed irregular type and divisor poles. It is not already the unitary Hopf Chern connection of the Gauss map.

## 11. Holomorphic line isomorphism does NOT preserve the natural connections [D,K,C]

On the selected compact elliptic curve, the nontrivial order-two spin line $S_R$ supports a flat unitary connection with $\pm1$ holonomy around suitable cycles and

```math
F_{\mathrm{spin,flat}}=0.
```

The Gauss-pulled Hopf/Berry connection is instead obtained by normalizing the Gauss-projective spinor:

```math
\eta_g=\frac{(1,g_R)}{\sqrt{1+|g_R|^2}},\qquad A_B=-i\eta_g^\dagger d\eta_g.
```

On the affine patch it has

```math
F_B=dA_B=\frac{i\,dg_R\wedge d\bar g_R}{(1+|g_R|^2)^2}.
```

This form is nonzero on generic open patches because $g_R$ is nonconstant, and its total Berry flux in the stated convention is

```math
\frac1{2\pi}\int_{E_R}F_B=\deg(g_R)=2.
```

The standard *holomorphic* tautological line $H_R=g_R^*\mathcal O(-1)$ has degree $-2$; the sign difference is because the Berry convention $-i\eta^\dagger d\eta$ and the mathematicians' Chern normalization for the tautological bundle use opposite curvature-to-degree conventions. Their absolute topological charge is two.

**Theorem 11.1 [D,K,C] (curvature and singularity obstruction).** No gauge transformation identifying **the natural flat spin connection** with **the Gauss-pulled Hopf Chern connection** can preserve connection curvature on any open region where $dg_R\ne0$. Likewise a flat meromorphic BA spectral connection off its singularities cannot be directly gauge equivalent to the nonflat Berry connection there. Furthermore, at spectral infinity a meromorphic gauge cannot remove the BA irregular principal part of §10.

**Important qualified possibility.** Twisting by $\mathcal O(P_0+P_\infty)$ changes bundle degree and introduces an additional **chosen Hermitian metric and connection**. One may choose its curvature to compensate the Hopf Chern curvature in the tensor product (and match the flat 2-torsion holonomy with further flat data). That constructs a **new, connection-enriched twisted comparison**; it does not make the original two natural connections automatically identical. Any claim of a canonical such twist must explicitly give its Hermitian metric, Chern connection, transition maps and residual periods.

### 11.1 Three distinct global invariants on the same elliptic curve

- **Divisor class / Abel–Jacobi point:** a holomorphic line-bundle isomorphism class, completely captured on a genus-one curve by degree and a Picard coordinate.
- **Flat/irregular monodromy:** path-ordered or abelian monodromy of a selected meromorphic connection, and at infinity its irregular/Stokes data when present.
- **Hermitian Chern curvature / Berry holonomy:** a unitary connection of a selected metric, whose curvature is a smooth $(1,1)$ form and whose holonomy around cycles depends on that connection.

These are *different typed invariants*. Equality of the first, even via the exact twist of §4, does not imply equality of the second or third.

## 12. Direct spinor construction of the Riemann WE triple versus the BA carrier [D,H,C]

The explicit sigma spinors $p_R,q_R$ in §5 satisfy

```math
p_R^2dz=\frac{dh_R}{g_R},\qquad q_R^2dz=g_Rdh_R,\qquad \frac{q_R}{p_R}=g_R.
```

Their WE 1-form triple

```math
\boldsymbol\Phi_R=\left(\frac{p_R^2-q_R^2}{2},\frac{i(p_R^2+q_R^2)}2,p_Rq_R\right)dz
```

is meromorphic on the Riemann curve and has marked **real immersion periods**

```math
\mathrm{Per}_R(\gamma)=\mathrm{Re}\oint_{\gamma}\boldsymbol\Phi_R\in\mathbb R^3.
```

The period condition required for a closed Euclidean immersion is $\mathrm{Per}_R(\gamma)=0$ on required cycles, or membership in a selected ambient translation lattice. This is a **flat affine translation holonomy** of the WE immersion, not the same as the BA spatial transfer matrix or the BA spectral irregular connection.

The BA function solves the fixed-energy SL eigenproblem

```math
L_m\psi(u,P)=E(P)\psi(u,P),
```

where the **spectral point is fixed as $u$ varies**. The WE map $g_R(P)$ is a *function of that spectral point*; it does not evolve under the same fixed-$E$ carrier. To compare it with the moving Dirichlet point one explicitly chooses the path $P=\gamma(u)$, which is an additional map constructed in §6, not the original stationary spectral-eigenvalue equation.

Therefore, the rigorously proved relationship at present is a **selected Abel–Jacobi transport of line classes plus an exact WE spinor reconstruction on the same elliptic curve**. A globally connection-preserving BA-to-WE identification remains an open, stricter theorem.

## 13. Same holomorphic spinors, two REAL FORMS: Euclidean Weierstrass and Lorentzian Kobayashi [D,V,K]

Let $p(z),q(z)$ be a local pair of holomorphic spinor coefficients as above. The Euclidean WE holomorphic null triple is

```math
\boldsymbol\Phi_E=\left(\frac{p^2-q^2}{2},\frac{i(p^2+q^2)}2,pq\right)dz,\qquad \Phi_{E,1}^2+\Phi_{E,2}^2+\Phi_{E,3}^2=0.
```

For the Lorentz–Minkowski form of signature $(+,+,-)$ choose the corresponding Kobayashi-type holomorphic null triple

```math
\boldsymbol\Phi_L=\left(\frac{p^2+q^2}{2},\frac{i(p^2-q^2)}2,pq\right)dz,\qquad \Phi_{L,1}^2+\Phi_{L,2}^2-\Phi_{L,3}^2=0.
```

They are related by the **explicit complex linear map**

```math
\boldsymbol\Phi_L=T\boldsymbol\Phi_E,\quad T=\begin{pmatrix}0&-i&0\\i&0&0\\0&0&1\end{pmatrix},\quad T^{\mathsf T}\operatorname{diag}(1,1,-1)T=-I_3.
```

**Theorem 13.1 [D,V] (shared holomorphic null structure with different real forms).** The two triples are algebraically null for their respective complexified quadratic forms and are closed wherever $p,q$ are holomorphic. Their real primitives are therefore local conformal zero-mean-curvature immersions of the corresponding real types **where the induced metric is nondegenerate**. The transformation is a complex null-cone correspondence, not a real Euclidean isometry or an automatic globally regular Wick rotation.

The two positive/indefinite Hermitian quadratic combinations yield different induced metrics:

```math
I_E=\frac14(|p|^2+|q|^2)^2|dz|^2,\qquad I_L=\frac14(|p|^2-|q|^2)^2|dz|^2.
```

The Lorentz immersion is spacelike when $|p|\ne|q|$ and has a degeneracy locus when $|p|=|q|$, equivalently $|g|=1$. This is precisely the familiar regular/maxface distinction in Kobayashi-type representations.

### 13.1 What "the same first-order condition" actually means

Both constructions use a **holomorphic structure**

```math
\bar\partial p=\bar\partial q=0
```

on local spinor coefficients, and their complex null one-forms integrate because holomorphic 1-forms in one complex dimension are closed. This is a first-order representation of the minimal/maximal surface equations.

But $\bar\partial\Psi=0$ by itself is **not a complete flat $\mathrm{SU}(2)$ or $\mathrm{SU}(1,1)$ moving-frame connection**. A real adapted frame also depends on the Hermitian metric/reality form and on derivatives in both $z,\bar z$; its projected $U(1)$ connection can have nonzero curvature. A *spectral-parameter family* of flat Lax connections needed for a Sym–Tafel formula is further additional data. Thus the first-order holomorphic null construction is shared, but the global spin/frame/monodromy package is not automatically identical.

### 13.2 Rigorous real-form sign classification

The Euclidean spin geometry uses compact $\mathrm{SU}(2)\to\mathrm{SO}(3)$ for its real orthonormal frames; Lorentzian spin geometry uses a noncompact real form $\mathrm{SU}(1,1)\cong\mathrm{SL}(2,\mathbb R)$ (up to the conventional conjugacy of matrix realization) covering the connected Lorentz-frame group. The two real forms are not unitarily gauge-equivalent. Their complexification to $\mathrm{SL}(2,\mathbb C)$ is common, but the choice of Hermitian structure and regularity conditions is independent, as shown by $I_E$ versus $I_L$.

## 14. Explicit catenoid example: its Lorentzian counterpart DEGENERATES at the waist [D,V,C]

Take the canonical WE spinors from draft 200, preserving $r,c>0$ and $\zeta=u+iv$:

```math
p=i e^{-r\zeta/2},\qquad q=-i e^{r\zeta/2},\qquad u=\ln(x/c).
```

Then

```math
|p|^2=e^{-ru},\quad |q|^2=e^{ru},\qquad I_E=\cosh^2(ru)|d\zeta|^2.
```

The corresponding Kobayashi-type Lorentz metric is instead

```math
I_L=\sinh^2(ru)|d\zeta|^2.
```

It degenerates along the **entire waist $u=0$, equivalently $x=c$**.

The Lorentz null triple for these spinors is

```math
\boldsymbol\Phi_L=(-\cosh(r\zeta),\,i\sinh(r\zeta),\,1)\,d\zeta.
```

Its real primitive is

```math
X_L(u,v)=\left(-\frac{\sinh(ru)\cos(rv)}r,-\frac{\sinh(ru)\sin(rv)}r,u\right).
```

**Theorem 14.1 [D,V,C].** The same holomorphic spinor pair and Wronskian generate (i) the smooth Euclidean catenoid and (ii) a Lorentzian maximal-surface parametrization that loses spacelike regularity at the canonical symmetry center $u=0$. Thus the shared first-order null-spinor algebra **does not imply a common globally regular surface**, common induced metric, or common self-adjoint Hilbert operator.

The same issue is unavoidable somewhere on the **full compactified Riemann elliptic curve** with nonconstant degree-two meromorphic Gauss map: it is surjective onto the Gauss sphere, hence the preimage of the unit circle $|g_R|=1$ is nonempty. The Lorentzian metric built from the identical spinors degenerates along that locus. Spacelike maximal patches can be studied on chosen components after removing the degeneracy set, but the entire punctured Riemann domain cannot be silently promoted to one globally regular spacelike Kobayashi immersion by a real-form switch.

## 15. The BPST/self-duality comparison is outside the proved bundle result [C,K]

The four-dimensional self-duality equation for a connection $A$ is $F_A=\star F_A$ (or $F_A=-\star F_A$). It is a first-order equation on a connection whose curvature is a two-form in a **chosen oriented four-dimensional metric**. Holomorphic structures, twistor methods and symmetry reductions can relate special self-dual gauge fields to lower-dimensional systems, but the mere presence of $\mathrm{SL}(2,\mathbb C)$ spinor data or a genus-one curve does not imply a BPST instanton.

The selected WE minimal/maximal surface representation is a first-order **closed null 1-form construction** on a complex one-dimensional domain. Its algebra and reality conditions differ from the 4D Yang–Mills Hodge-star condition. The framework may retain both as separate typed constructions for future study; this manuscript makes **no** identity between their gauge bundles or self-duality equations.

## 16. The actual global reconstruction problem is now explicit [D,K,O]

The selected **holomorphic** divisor ladder is

```math
H_R\otimes\mathcal O(P_0+P_\infty)\simeq S_R,\qquad D(u_*)\simeq S_R
```

with $D(u_*)=\mathcal O(\gamma(u_*)-P_\infty)$ at the Lamé half-period $u_*=K(m)/r$.

This is a genuine geometric compatibility at a **selected spatial phase**, but a full global *connection-preserving reconstruction* would still need:

1. **Precise eigenline convention.** Specify the actual Krichever fixed pole divisor $D_*$, the moving Dirichlet zero divisor $\gamma(u)$, the Bloch eigenline and their dual/twist identifications, including the sign of the spectral Wronskian.
2. **Explicit line isomorphism.** Use the sigma half-period construction of §5 and a theta/prime-form representation for the selected BA divisor. Prove the isomorphism over **all points** of the elliptic curve as holomorphic lines, not merely equality of abstract degree.
3. **Connection comparison.** Specify the BA spectral connection and its irregular type, the flat 2-torsion spin connection, and the Hopf Chern connection, together with the extra twist curvature needed to compare them. A meromorphic gauge cannot cancel the BA irregular type with $dh_R$.
4. **Marked periods.** Compare the BA quasimomentum $a/b$ periods with the Riemann WE translation/flux periods and the Berry holonomies, using the exact draft-170 Gauss–Manin gauge. A period determinant being constant does not make the individual period vectors equal.
5. **Reality and operator domain.** Track real forms, spin signs, self-adjoint domains, and (if using a maximal surface) the locus $|g_R|=1$, at which the induced metric is singular.
6. **Integrable extended frame.** A Sym–Tafel immersion needs an additional two-variable spectral-parameter Lax pair and reality reduction; a fixed-energy spatial SL equation alone does not produce a unique immersed surface.

**Candidate theorem that survives the audit:** *Selected One-Gap Lamé–Riemann Elliptic Picard Transport and Half-Period Spin Compatibility*, together with the sigma uniformization and a **connection-obstruction theorem**. A stronger global BA/Hopf/WE connection-preserving equivalence remains an open, precisely formulated research problem.

## 17. NEW EXACT BRIDGE: Riemann's Gauss map produces a Lamé band-edge eigenfunction [D,V,K]

Return to the **Abelian** elliptic coordinate $z$ of §5, not the canonical real SL spatial coordinate $u$. Write $g=g_R(z)$, $k=k_R$, and recall the cubic

```math
y_R^2=g^3+kg^2-g,\qquad g_z=2y_R.
```

By differentiation,

```math
g_z^2=4g(g^2+kg-1),\qquad g_{zz}=6g^2+4kg-2.
```

On a simply connected chart with $g\ne0,\infty$ choose $\chi(z)=\sqrt{g(z)}$ (as a local representative of the nontrivial spin line). Let its logarithmic derivative be the **Riccati superpotential**

```math
H(z)=\frac{\chi_z}{\chi}=\frac{g_z}{2g}=\frac{y_R}{g}=\frac{w_R}{\sqrt{\lambda_R}\,g}.
```

The curve equations imply directly

```math
H^2=\frac{g_z^2}{4g^2}=g+k-\frac1g,
```

```math
H_z=\frac{g_{zz}}{2g}-\frac{g_z^2}{2g^2}=g+\frac1g.
```

Thus the **two Riccati combinations** are

```math
H^2+H_z=2g+k,\qquad H^2-H_z=k-\frac2g.
```

**Theorem 17.1 [D,V] (Riemann Gauss-map Lamé eigenfunction).** The square-root Gauss spinor $\chi=\sqrt g$ satisfies

```math
\chi_{zz}=(2g+k)\chi,\qquad(-\partial_z^2+2g)\chi=-k\chi.
```

Since $g(z)=\wp(z)-k/3$, this is precisely the **one-gap Weierstrass Lamé equation**

```math
(-\partial_z^2+2\wp(z))\chi=-\frac{k}{3}\chi.
```

The sigma-function section $h_a$ from §5 is its exact **half-period/band-edge Hermite–Halphen Baker-type solution**. This directly realizes a selected Lamé spectral eigenfunction as a Riemann WE spinor factor. It is a classical elliptic-function mechanism, verified here in the framework's **Riemann normalization**.

**Proof.** The two displayed Riccati identities give $\chi_{zz}/\chi=H_z+H^2=2g+k$. Substitute $g=\wp-k/3$.

### 17.1 The archived Riemann horizontal exactness identity IS the Riccati derivative

The historical claim H466 uses the normalized Riemann curve with

```math
d\left(\frac{w_R}{g_R}\right)=\frac{\lambda_R}{2}\left(g_R+\frac1{g_R}\right)\frac{dg_R}{w_R}.
```

Our logarithmic derivative is $w_R/g_R=\sqrt{\lambda_R}\,H$, while

```math
\frac{dg_R}{w_R}=\frac{2}{\sqrt{\lambda_R}}\,dz.
```

Therefore both sides of H466 are **exactly**

```math
\sqrt{\lambda_R}\,H_z\,dz=\sqrt{\lambda_R}\left(g_R+\frac1{g_R}\right)dz.
```

**Corollary 17.2 [D,V,H466].** The previously archived exact-differential reduction of the horizontal Weierstrass periods is *literally the Riccati derivative identity* for the Riemann Gauss spinor's logarithmic derivative. This is a direct and nontrivial algebraic meeting point of the framework's Riemann minimal-surface data, Riccati, Lamé, and WE representations.

## 18. The two WE spinor factors are exact DARBOUX partner zero modes [D,V,K]

Define the formal first-order factors on the complex Abel coordinate,

```math
D=\partial_z-H,\qquad D^\sharp=-\partial_z-H.
```

The symbol $\sharp$ means **formal transpose** in the complex $z$ variable, NOT a Hilbert adjoint unless a compatible real contour, positive measure and real coefficients are separately chosen.

From §17,

```math
D^\sharp D=-\partial_z^2+H^2+H_z=-\partial_z^2+2g+k,
```

```math
DD^\sharp=-\partial_z^2+H^2-H_z=-\partial_z^2+k-\frac2g.
```

Let

```math
L_+=-\partial_z^2+2g(z),\qquad L_-=-\partial_z^2-\frac2{g(z)}.
```

Then the exact Darboux factorization and intertwining are

```math
L_++k=D^\sharp D,\qquad L_-+k=DD^\sharp,\qquad D L_+=L_- D.
```

The two Riemann WE spinor coefficients of §5 are **reciprocal**:

```math
q_R=\sqrt{\beta_R}\chi,\quad p_R=\sqrt{\beta_R}\chi^{-1},\qquad Dq_R=0,\quad D^\sharp p_R=0.
```

**Theorem 18.1 [D,V] (reciprocal WE spinor = Darboux pair).** In the **Abelian elliptic coordinate**, the Riemann WE spinor components are distinguished zero modes of a first-order Darboux partner pair. They do **not** solve the same scalar second-order differential operator in that coordinate, since their ordinary Wronskian $2\beta_RH(z)$ is generally nonconstant.

By contrast, in the **Hopf natural coordinate** $d\xi^2=\Theta_R=2\beta_RH(z)\,dz^2$, the spinors are transported as half-densities and their Wronskian becomes one; they then solve the **same** Schwarzian projective SL equation (draft 200). Hence we have two explicitly compatible forms of the same WE data:

- Abel chart $z$: a pair of **Darboux-partner** scalar equations and a nonconstant Wronskian.
- Hopf-natural chart $\xi$: one common **Schwarzian SL carrier** and constant Wronskian.

These are different exact gauge/coordinate representations of the selected holomorphic spinor data, not proof that a generic spectral SL operator is unitarily equivalent to a minimal-surface Jacobi operator.

## 19. A 2-TORSION ELLIPTIC TRANSLATION implements the Darboux partner [D,V,K]

Let $a$ be the half-period corresponding to the branch point $P_0$ of the Riemann Gauss map, $g(a)=0$. Consider the map of the normalized Riemann curve

```math
T:(g,y_R)\longmapsto\left(-\frac1g,\frac{y_R}{g^2}\right).
```

Since $y_R^2=g^3+kg^2-g$, direct algebra yields

```math
\left(\frac{y_R}{g^2}\right)^2=\left(-\frac1g\right)^3+k\left(-\frac1g\right)^2-\left(-\frac1g\right).
```

Also

```math
T^*\left(\frac{dg}{y_R}\right)=\frac{d(-1/g)}{y_R/g^2}=\frac{dg}{y_R},\qquad T^2=\mathrm{id}.
```

The map extends through the apparent coordinate poles to an elliptic curve automorphism. It sends the group origin $P_\infty$ to the nontrivial 2-torsion point $P_0$. Since it preserves the holomorphic differential and has order two, it is **translation by $P_0$**, not negation of the group law.

**Theorem 19.1 [D,V] (half-period Gauss-map reciprocal involution).**

```math
g_R(z+a)=-\frac1{g_R(z)},\qquad 2a\in\Lambda_R.
```

Therefore the Darboux partner of §18 is literally the **half-period translate of the same elliptic Lamé potential**:

```math
L_-=-\partial_z^2+2g_R(z+a),\qquad D L_+(z)=L_+(z+a)D.
```

This is the classical phenomenon of a Lamé **Darboux displacement**, here deduced directly from the Riemann minimal-example Gauss-map equation. The *same* 2-torsion point $P_0$ both selects the WE spin structure and implements the operator displacement.

### 19.1 The two WE spinors themselves are shifted copies of one band-edge function

By Theorem 19.1, $\chi(z+a)^2=g(z+a)=-1/g(z)$. Hence on any simply connected patch away from poles,

```math
\chi(z+a)=\pm i\,\chi(z)^{-1},\qquad p_R(z)=\mp i\,q_R(z+a),
```

with the sign fixed by the chosen local spinor trivialization. Thus the two WE spinors are a **half-period-translated** Hermite–Halphen Lamé band-edge section and its reciprocal.

**Global caveat:** For the real family, the branch $P_0$ corresponding to the *middle* root of the Weierstrass cubic generally has a **non-real half-period** $a$. The translation is then an exact **complex elliptic** Darboux displacement; it is not a unitary shift on the original real spatial Lamé line. The Riemann Abel variable $z$ is also not the original canonical $u$ without the separate marked spectral/divisor map of §8. These distinctions keep the proved theorem genuinely algebraic rather than forcing spectral or physical equivalence.

## 20. The two exact bridges form a COMMUTATIVE-TYPE DICTIONARY, not a universal identity [D,H]

The framework now has two concrete ways to pass between the same chosen genus-one surface curve and linear second-order structures.

**Bridge A: spectral Dirichlet/Picard transport.** Starting with the real periodic Lamé equation in the original logarithmic spatial coordinate $u$, its moving gap point $\gamma(u)$ lies on the spectral elliptic curve and satisfies $\gamma_u=-2\eta_\gamma$. Under the exact real affine Lamé–Riemann curve isomorphism, the point moves on the Riemann Picard torus with slope $r/\sqrt{D_R}$ and meets the selected WE spin class at $u=K(m)/r$ modulo the period.

**Bridge B: WE Gauss-spinor/Darboux displacement.** Starting instead with the meromorphic Riemann Gauss map $g_R(z)$ on its **elliptic Abel coordinate**, the local square root $\sqrt{g_R}$ is a half-period Lamé eigenfunction, its logarithmic derivative obeys the two rational Riccati identities, and its reciprocal spinor is a Darboux partner obtained by elliptic translation by $P_0$. In the Hopf-natural quadratic-differential coordinate the two WE spinors form a common Schwarzian carrier.

The bridges share the **same explicitly identified elliptic curve, branch point $P_0$, 2-torsion spin class and marked differential**. Their spatial/Abelian evolution coordinates, operators, Hilbert realizations and connections remain different until an actual intertwiner is supplied.

**This is the strongest currently established algebraic version of the user's “whole web” idea:** the individual links are exact, and their types are explicit; one should not substitute a universal scalar ODE or one $\mathrm{SL}(2,\mathbb C)$ connection for the full decorated geometry.

## 21. CONDITIONAL ELLIPTIC PICARD–SPIN–DARBOUX RECONSTRUCTION THEOREM [D,V,K,H]

**Theorem 21.1 (selected one-gap global HOLomorphic compatibility).** Fix the real Lamé parameter $0<m<1$, canonical resolution $r>0$, and the Riemann modulus $\lambda_R>0$ related by $m=(1+\lambda_R^2)^{-1}$. Let $\Gamma_m$ and $E_R$ be the smooth compact elliptic curves of §2, identified by the exact affine isomorphism from draft 170. Let $P_\infty$ be the group origin and $P_0$ the point $g_R=0$.

Then:

1. **Unique selected WE spin class.** The Riemann meromorphic WE data $(g_R,dh_R)$ determine the nontrivial theta characteristic $S_R=\mathcal O(P_0-P_\infty)$ by the divisor of $dh_R/g_R$; the compatible meromorphic spinors are uniformized by the half-period sigma section $h_a$ of §5.
2. **Hopf holomorphic compatibility.** The Gauss-pulled tautological line $H_R=g_R^*\mathcal O(-1)$ satisfies the exact global twist $H_R\otimes\mathcal O(P_0+P_\infty)\simeq S_R$.
3. **Moving spectral divisor class.** The Dirichlet coordinate $\gamma(u)=r^2(1-m-m\mathrm{sn}^2(ru|m))$ satisfies the Dubrovin equation and the squared-eigenfunction Drach cubic; its Abel image on the same Riemann elliptic curve is $z_\gamma(u)=a+\frac r{\sqrt{D_R}}(u-u_*)$ modulo periods.
4. **Distinguished Picard matching.** The class $D(u)=\mathcal O(\gamma(u)-P_\infty)$ is isomorphic to $S_R$ precisely at the spatial half-periods $u_*=K(m)/r$ modulo $2K(m)/r$ on the chosen real orbit. Generically the class differs by the nontrivial Jacobian translation $\mathcal O(P_{z_\gamma(u)}-P_a)$.
5. **Band-edge Lamé spinor and displacement.** In the *different* Riemann Abel coordinate $z$, the square-root spinor $\chi=\sqrt{g_R}$ is a meromorphic one-gap Lamé band-edge eigenfunction, its logarithmic derivative produces the reciprocal Darboux pair, and the partner is a translation by the SAME 2-torsion half-period $a$. The historical Riemann horizontal period exactness is its Riccati derivative identity.

**Proof.** (1) follows from $\operatorname{div}(g_R)=2P_0-2P_\infty$, the nowhere-zero holomorphic height form and the explicit sigma square root §§3/5. (2) is §4. (3) follows from Jacobi differentiation, polynomial Drach identity and transported elliptic holomorphic differential §§6–8. (4) is Abel's theorem on the compact elliptic curve, with the real gap endpoints computed in §6. (5) follows directly from the cubic curve's differential equation, Riccati factorization, the exact 2-torsion reciprocal involution and H466 §§17–19.

**What the theorem does NOT assert.** It does not equate the fixed-pole BA normalization, moving Dirichlet divisor and Lax eigenline without extra choices; does not construct a globally connection-preserving intertwiner; does not give a real unitary map between original periodic Lamé $L_m$ and the meromorphic Abel-coordinate $L_+$; and does not derive Euclidean or Lorentzian immersion periods from a lone SL spectrum.

**Theorem 21.2 (connection obstruction).** For the **natural choices** (flat 2-torsion spin connection, Gauss Hopf Chern connection, and selected BA spectral meromorphic irregular connection), no gauge equivalence preserving these connections is implied by Theorem 21.1: their curvatures differ on generic patches and the BA irregular double pole at $P_\infty$ cannot be cancelled by adding a multiple of the holomorphic WE height differential.

**Proof.** Curvature invariance under gauge and the principal-part calculation of §§10–11. A new *twisted* metric/connection may be built after supplying additional curvature and flat-holonomy data, but that is a new object requiring proof.

**Interpretation:** This is a strong conditional **global line-class / half-period Darboux compatibility theorem** plus an equally important no-go for automatic connection matching. It is a genuine step from projective local spinor formulas toward global algebro-geometric organization.

## 22. Explicit r=2, c, mu, and Riemann symmetric modulus regression [D,V]

Set the framework's resolution $r=2$; keep its original multiplicative center $c>0$ and field amplitude $\mu>0$ as *independent constants*. On the selected symmetric elliptic fiber choose $\lambda_R=1$, so

```math
m=\frac12,\quad k_R=0,\quad D_R=2,\quad (E_0,E_1,E_2)=(-2,0,2).
```

The spectral and Riemann curves, with the verified affine map, become

```math
\Gamma_{1/2}:\ \eta^2=-(E+2)E(E-2),\qquad E_R:\ y_R^2=g_R^3-g_R,\qquad g_R=-E/2.
```

Their Riemann Weierstrass uniformization is

```math
g_R(z)=\wp(z;4,0),\qquad z=\int\frac{dg_R}{2y_R},\qquad \wp(a)=0,\quad 2a\in\Lambda_R.
```

The selected WE spin structure is $S_R=\mathcal O(P_0-P_\infty)$, with $P_0$ the branch above $g=0$. Its sigma section satisfies $h_a(z)^2=\wp(z)$ and the exact reciprocal half-period shift

```math
\wp(z+a)=-1/\wp(z).
```

The WE spinors in the *Riemann Abel variable* are

```math
\beta_R=2A_R,\qquad p_R(z)=\sqrt{2A_R}/h_a(z),\qquad q_R(z)=\sqrt{2A_R}\,h_a(z).
```

The **separate canonical real Lamé spatial problem** has moving gap point

```math
\gamma(u)=2\,\mathrm{cn}^2(2u\mid \tfrac12),\qquad\eta_\gamma=4\,\mathrm{sn}(2u)\mathrm{cn}(2u)\mathrm{dn}(2u).
```

It evolves by $\gamma_u=-2\eta_\gamma$, crossing the WE branch $E_1=0$ at

```math
u_*=\frac12K(\tfrac12)\pmod{K(\tfrac12)},\qquad x_*=c\exp\left(\frac12K(\tfrac12)\right)\exp\left(jK(\tfrac12)\right).
```

The exact **Riemann Abel/Picard slope** is

```math
\frac{dz_\gamma}{du}=\sqrt2,\qquad z_\gamma(u)=a+\sqrt2(u-u_*)\pmod{\Lambda_R}.
```

The meromorphic Abel-coordinate Riccati superpotential is

```math
H=\frac12\frac{\wp'}{\wp},\qquad H_z=\wp+\frac1{\wp},\quad H^2=\wp-\frac1{\wp}.
```

Its Darboux partners are

```math
D^\sharp D=-\partial_z^2+2\wp(z),\qquad DD^\sharp=-\partial_z^2-\frac2{\wp(z)}=-\partial_z^2+2\wp(z+a).
```

The selected nontrivial spinor $q_R$ solves the band-edge equation $(-\partial_z^2+2\wp)q_R=0$; its reciprocal $p_R$ solves the shifted partner zero equation. **These are Abel-coordinate equations**, not a claim that the original spatial operator $L_{1/2}=-\partial_u^2+4\,\mathrm{sn}^2(2u|1/2)-4$ equals either of them without a selected complex coordinate change and domain map.

The original Symmetrical Function remains

```math
f_\mu(x;2,c)=\frac{c^2x}{\sqrt\mu(x^4+c^4)},\qquad \|f_\mu\|^2_{L^2(xdx)}=\frac1{4\mu}.
```

It has the earlier zero-energy EP/catenoid spinor identification of draft 200, but $\mu$ is NOT a modulus, Riemann immersion scale or BA divisor phase. This regression separates the algebraic $r$ resolution, multiplicative origin $c$, field normalization $\mu$, elliptic modulus and marked immersion amplitude $A_R$.

## 23. The attached conjectural "exact divisor ladder": audited verdict [D,C]

| Statement in the attachment | Audit result |
|---|---|
| $g_R$ has divisor $2P_0-2P_\infty$. | **Exact.** It has a double zero at the branch $g=0$ and double pole at infinity. |
| The WE data select an elliptic 2-torsion spin bundle. | **Exact**, specifically $S_R=\mathcal O(P_0-P_\infty)$; spinors must be **meromorphic** at the planar ends. |
| The Hopf line is $\mathcal O(-2P_\infty)$ and can be twisted into the WE spin line. | **Exact holomorphic bundle identity**, with $\mathcal O(P_0+P_\infty)$ as twist. Does not automatically compare natural connections. |
| A real one-gap BA/Dirichlet divisor always lies at a branch point. | **False generically.** The exact moving Dirichlet point travels through the gap $(E_1,E_2)$; it reaches $P_0$ only at special half-period positions. |
| The moving degree-zero Dirichlet class can equal the WE spin class. | **True at selected spatial phases**, precisely the corresponding point equality on the elliptic curve. |
| The BA eigenline and moving Dirichlet divisor are definitionally the same object. | **Requires normalization:** standard Krichever pole divisor can be fixed while Dirichlet zeros move. |
| A global theta/sigma expression can be written. | **Yes:** the half-period sigma section $h_a$ is given explicitly and is a section of a 2-torsion spin line, not a global scalar elliptic square root. |
| Subtracting $C\,dh_R$ from the spectral second-kind $dp$ cancels its double pole. | **False for all finite $C$** because $dh_R$ is holomorphic at spectral infinity while $dp$ has a double pole. |
| The spin/Hopf/BA connections become gauge-identical automatically after the divisor twist. | **False.** Chern curvature and irregular type differ under the natural choices. An enriched twisted connection is additional data. |
| The same holomorphic spinors can describe Euclidean minimal and Lorentz maximal surfaces. | **Exact locally with distinct real forms**, but the induced metric sign causes a singular set when $|p|=|q|$. |
| The Riemann WE spinor square root is a Lamé band-edge Baker-type solution. | **Exact** in the Abel elliptic coordinate; its reciprocal is the Darboux-partner zero mode. |
| The two Darboux potentials are related by a 2-torsion half-period translation. | **Exact** on the Riemann elliptic curve, by $g(z+a)=-1/g(z)$. |
| The Riemann horizontal WE exact differential is its Riccati derivative. | **Exact** in the archived normalization H466. |
| This proves a universal isomorphism of all SL–EP/minimal-surface operator domains. | **No.** Spatial, spectral, projective, Hermitian and affine connection/period data remain separately typed. |

## 24. What "fibration holography" would mean AFTER this result [D,O]

The strongest tested phenomenon here is not that a codimension-one asymptotic boundary may be discarded in every setting. Rather, the **same elliptic curve with carefully marked line/divisor, connection and differential data** supports:

- a Lamé finite-gap spectral operator and its moving Dirichlet/Picard coordinates;
- a selected Riemann WE immersion and its meromorphic spinors;
- a 2-torsion Gauss-map reciprocal involution implementing a Darboux displacement;
- a pulled-back Hopf Hermitian line with nontrivial Chern curvature;
- real Euclidean and Lorentzian null-spinor constructions with different metric positivity domains;
- period and affine-translation obstructions to a global immersion.

The projective real-one-variable SL–EP reduction is one **exactly constructed local/selected real slice** of this network, not an all-purpose functor preserving arbitrary bulk topology.

The programmatic extension *Fibration Holography* can ask whether a **decorated base curve** and its collection of equivariant connections/periods reconstruct an ambient Euclidean or pseudo-Riemannian geometry in a faithful category. Such a theorem would require an explicit definition of the objects, their morphisms, and a proof of inverse faithfulness. The current work supplies **several actual construction maps and non-equivalence tests**. It does not assert a physical holographic duality, a common 4D Yang–Mills gauge bundle, or complete reconstruction from one scalar equation.

## 25. Verification register, project provenance, and independent sources

### 25.1 Exact calculations independently checked

1. **Riemann Gauss divisor [D].** The cubic branch $g=0$ has local coordinate $\sqrt g$, yielding $\operatorname{ord}_{P_0}g=2$; the unique cubic infinity has $\operatorname{ord}_{P_\infty}g=-2$. The nonprincipal half-divisor $P_0-P_\infty$ has order two in the elliptic group.
2. **Holomorphic WE spin [D].** The Riemann height differential $dg_R/w_R$ is nowhere zero on the compact elliptic curve. The WE spinor squares have divisors $\pm2(P_0-P_\infty)$, selecting the nontrivial two-torsion spin class. Nonzero holomorphic sections of this degree-zero nontrivial line do not exist; the actual sections are meromorphic at the punctures.
3. **Hopf divisor [D].** Pulling back the point infinity on $\mathbb{CP}^1$ gives $2P_\infty$, so $H_R=\mathcal O(-2P_\infty)$ and its exact tensor twist by $\mathcal O(P_0+P_\infty)$ gives $S_R$.
4. **Weierstrass elliptic uniformization [V].** The translation $X=g+k_R/3$ produces $Y^2=4X^3-G_2X-G_3$ with $G_2=4(1+k_R^2/3)$, $G_3=-4(k_R/3+2k_R^3/27)$. The point $P_0$ has value $X=k_R/3$, a nontrivial half-period root.
5. **Sigma square root [K,D].** The classical addition identity and half-period quasi-periodicity give $h_a(z)^2=\wp(z)-\wp(a)$. Its sign multipliers over period loops make it a 2-torsion section, not a global elliptic scalar square root.
6. **Moving Lamé gap point [V].** With $\gamma=r^2(1-m-mt)$ and $t=\mathrm{sn}^2(ru|m)$, direct Jacobi differentiation gives $\gamma_u=-2mr^3\mathrm{sn\,cn\,dn}=-2\eta_\gamma$. It moves between $E_2$ (at $\mathrm{sn}=0$) and $E_1$ (at $\mathrm{sn}^2=1$).
7. **Drach certificate [V].** SymPy polynomial simplification returned exactly zero for both $R'''-4(V-E)R'-2V'R$ and $R'^2-2RR''+4(V-E)R^2-4\eta(E)^2$ with $R=E-\gamma$, treating $E,m,r,t$ symbolically and using the Jacobi differential identities.
8. **Abel/Picard slope [V].** The ratio $\gamma_u/\eta_\gamma=-2$, together with the archived real affine differential scale, proves $dz_R(\gamma(u))/du=r/\sqrt{D_R}$ for all smooth real moduli; the Riemann WE half-period $a$ is hit at $u=K(m)/r$ modulo $2K(m)/r$.
9. **Quasimomentum pole [D].** With $t=E^{-1/2}$, $\eta\sim it^{-3}$ and $dE/\eta\sim2i\,dt$, the normalized $dp_{\rm sp}\sim-dt/t^2$ while $dh_R=O(1)\,dt$. No finite multiple of $dh_R$ cancels its double pole.
10. **Lorentzian real-form check [V].** SymPy gives $\Phi_{L,1}^2+\Phi_{L,2}^2-\Phi_{L,3}^2=0$ and $T^{\mathsf T}\mathrm{diag}(1,1,-1)T=-I$. The canonical catenoid spinor produces $I_E=\cosh^2(ru)|d\zeta|^2$ and $I_L=\sinh^2(ru)|d\zeta|^2$, with Lorentzian degeneration at $u=0$.
11. **Riemann Riccati [V].** The normalized cubic gives $g_z^2=4g(g^2+kg-1)$ and $g_{zz}=6g^2+4kg-2$. Symbolic simplification yields $H_z=g+1/g$, $H^2=g+k-1/g$ and Darboux partner potentials $2g+k$ versus $k-2/g$.
12. **H466 exactness [V,H466].** The archived differential $d(w_R/g_R)=\frac{\lambda_R}{2}(g_R+1/g_R)dg_R/w_R$ is exactly $\sqrt{\lambda_R}\,dH$ when $H=g_z/(2g)$, $w_R=\sqrt{\lambda_R}g_z/2$.
13. **Elliptic half-period automorphism [V].** The transformation $(g,y)\mapsto(-1/g,y/g^2)$ preserves the cubic equation and differential $dg/y$, squares to the identity and maps infinity to the nontrivial 2-torsion point $P_0$, proving $g(z+a)=-1/g(z)$.
14. **Darboux partners [V].** Direct operator multiplication gives $D^\sharp D=-\partial_z^2+2g+k$ and $DD^\sharp=-\partial_z^2+k-2/g$; by the half-period identity the second is a translate of the first. The reciprocal WE spinors are the respective factorization zero modes.
15. **Resolution test [V].** At $r=2,\lambda_R=1$, $(E_0,E_1,E_2)=(-2,0,2)$, $\gamma=2\,\mathrm{cn}^2(2u|1/2)$, $z_\gamma'=\sqrt2$, $G_2=4$, $G_3=0$, and $\wp(z+a)=-1/\wp(z)$ exactly.

### 25.2 Historical ZIP and live project provenance

- The actual November 18 ZIP Riemann marked-periods module, H466–H470, contains the elliptic WE data, horizontal derivative exactness, marked periods, Gauss–Manin and modular coordinates. The Riemann horizontal derivative is a **pre-existing checked identity** whose Riccati interpretation has now been derived.
- The ZIP Lamé complementary/special-loci module and H95 contain earlier Lamé spectral-modular relationships, but not the complete moving Dirichlet/selected WE spin compatibility of this draft.
- The ZIP Sato–Grassmannian module H136 constructs the selected rank-one nodal soliton Baker function and tau; it does not equate the smooth elliptic BA divisor, spin line and Hopf Chern connection.
- The ZIP fundamental-forms/Willmore/Hopf module H421–H428 and draft 200 establish the projective WE spinor framework. The present work derives additional **global divisor and half-period identities** but preserves the previous source claims.
- Live draft 170 supplies the smooth one-gap Lamé–Riemann real affine curve isomorphism, marked spectral quasimomentum and Gauss–Manin gauge. Live drafts 180–200 supply the connection taxonomy and local WE–SL–EP reconstruction.

### 25.3 Classical literature and precisely relevant uses

- Kusner–Schmitt, *The Spinor Representation of Surfaces in Space*: https://arxiv.org/abs/dg-ga/9610005 . Meromorphic WE spinors, global sign/period and spin-bundle data.
- Osamu Kobayashi, *Maximal Surfaces in the 3-Dimensional Minkowski Space L3*, Tokyo Journal of Mathematics 6 (1983), 297–309: https://ir.library.osaka-u.ac.jp/repo/ouka/all/26352/?lang=1 . The Lorentzian maximal-surface Weierstrass representation.
- Krichever–Takhtadzhyan, *Algebraic de Rham Theorem and Baker–Akhiezer Function*, Izvestiya Mathematics 88 (2024), 506–514: https://doi.org/10.4213/im9533e . Degree-$g$ divisors, Picard flow, Dubrovin equations and Baker–Akhiezer functions.
- Dubrovin, *Theta Functions and Nonlinear Equations*, lecture notes: https://people.sissa.it/~dubrovin/rsnleq_web.pdf . Elliptic BA sigma formulas and distinction between chosen pole divisors and moving spectral data.
- NIST DLMF, Weierstrass $\wp$, sigma, zeta, half-period and addition identities: https://dlmf.nist.gov/23.2 ; https://dlmf.nist.gov/23.6 ; https://dlmf.nist.gov/23.10 .
- *The phenomenon of Darboux displacements*, Physics Letters A 281 (2001): https://www.sciencedirect.com/science/article/abs/pii/S0375960101008398 . The half-period/self-isospectral Darboux-displacement mechanism is classical.
- One-gap Lamé half-period Darboux partners in an integrable-system realization: https://journals.aps.org/prd/abstract/10.1103/PhysRevD.98.065013 . This external example is used solely for the already known Darboux mathematics, not its physical model.
- NIST DLMF, Lamé equation and spectral band-edge functions: https://dlmf.nist.gov/29 .

**Evidence boundary.** This draft derives an exact *selected mathematical dictionary*. It neither claims priority for Weierstrass spinors, Baker–Akhiezer functions or Darboux displacement, nor promotes line-class compatibility into a global natural-connection equality without the missing data.

## 26. Open global bundle problems, theorem status and mathematical conclusion

### 26.1 The next tests that could upgrade the result

1. **Fixed-pole BA normalization.** Construct the normalized global Baker–Akhiezer function for the *specific* real one-gap shifted Jacobi potential, with fixed degree-one divisor, spectral marked point $P_\infty$ and selected quasimomentum. Determine explicitly how its fixed pole and moving Dirichlet zero correspond to the eigenline of a chosen stationary KdV 2-by-2 Lax matrix. Do not identify all three line constructions by notation.
2. **Theta/eigenline matching.** Express the chosen BA function as a sigma/theta ratio with its correct quasimomentum factor and compare its divisor and multipliers to $h_a(z)$ at the distinguished $u_*$. Track the selected dual, normalization and possible phase.
3. **Darboux operator/domain transfer.** Compute the **complex** elliptic coordinate shift mapping the Abel-coordinate operator $-\partial_z^2+2g_R(z)$ to the original real Jacobi shifted Lamé $L_m$, including energy shifts, real contour and self-adjoint domain. The abstract curve isomorphism alone cannot supply this.
4. **Natural twisted connection.** Construct a Hermitian metric/connection on $T=\mathcal O(P_0+P_\infty)$ whose Chern curvature compensates the natural Gauss tautological curvature, and compute its residual flat holonomies. Determine whether WE immersion periods canonically normalize that choice.
5. **Irregular BA spectral connection.** Calculate formal type, actual periods and possible Stokes factors of the normalized Baker function near $P_\infty$. A local essential exponential twist can remove a formal principal term only in a broader irregular-connection category; no meromorphic gauge over $P_\infty$ does so.
6. **Marked modular transport.** Combine the exact Riemann Gauss–Manin period gauge of draft 170 with the Picard slope $r/\sqrt{D_R}$ to track the chosen 2-torsion spin class under loops in the elliptic modulus. Determine the theta-characteristic monodromy rather than equating the *matrix* of the spatial transfer operator with Gauss–Manin.
7. **Weierstrass real period map.** Apply the 2-torsion translation $g\mapsto-1/g$ to the **full three-component WE triple**, and calculate its effect on real translation/flux periods and on the Bonnet associate angle. The Darboux displacement identity alone does not imply global immersion period closure.
8. **Lorentzian regularity and geometry.** Analyze $|g_R|=1$ on the compactified Riemann curve, the connected spacelike components after removal, and possible global maxface periods; test a real SL/EP reduction only when a real coordinate and self-adjoint domain exist.
9. **EP from the elliptic band-edge spinor.** Restrict the sigma spinor to a suitable *real* Abel contour and compute a genuinely positive Gram amplitude, constant real Wronskian and Pinney equation. The complex meromorphic Darboux pair of §§17–19 is not automatically a real EP system.
10. **Two singular limits.** Follow the distinguished elliptic 2-torsion point, the spin theta characteristic, the reciprocal Gauss involution and the BA divisor as $m\to0$ (free closed gap) or $m\to1$ (PT soliton). The limits can yield different generalized spin structures on nodal curves; compare to the marked catenoid height and original arctangent differentials of draft 170.
11. **Higher-genus BA and WE.** For the framework's selected genus-two and higher spectral curves, compute the degree-$g$ BA divisor, spin parity and Gauss divisor class, then test which theta characteristics can be matched under actual meromorphic maps to selected surface data.
12. **Fibration holography as inverse theorem.** Define a category of decorated base curves with spinors, BA eigenlines, irregular/flat/unitary connections, holomorphic forms, real immersion periods and self-adjoint Hilbert domains; require a faithful reconstruction functor before claiming the base encodes the total ambient geometry. This is separate from asymptotic codimension-one boundary duality.

### 26.2 Why this is genuinely a WHOLE-WEB result

The diagram of rigorous arrows in this selected genus-one family is:

- **Real Lamé SL**, in $u=\ln(x/c)$, gives a third-order squared-eigenfunction equation, an algebraic cubic spectral curve and a **moving Dirichlet divisor**.
- **Dubrovin** gives $\gamma_u=-2\eta_\gamma$, and the exact affine Lamé–Riemann elliptic map gives **linear Picard transport** to the Riemann curve.
- The Riemann **Weierstrass Gauss map** selects the nontrivial 2-torsion spin class $\mathcal O(P_0-P_\infty)$ and admits an explicit sigma-function square-root spinor.
- The sigma spinor is itself a **one-gap Lamé band-edge eigenfunction** in the separate elliptic Abel coordinate; its logarithmic derivative generates two exact **Darboux partners**.
- The partners are exchanged by **translation by the same 2-torsion point $P_0$**, and the archived Riemann horizontal WE differential identity is the same Riccati derivative.
- The full WE spinor quadratic forms reconstruct a Euclidean minimal immersion with separate **real translation periods**; changing the real form gives a locally maximal Lorentzian null construction, but can create metric degeneracies.
- The **Hopf** Chern connection and **BA irregular** connection are different extra structures; selected holomorphic divisor matches do not identify their natural curvatures and singularity types.
- On the canonical real catenoid separatrix (draft 200), a spinor Gram norm also gives the **positive EP envelope and Gudermannian half-angle**. No corresponding statement is made here for arbitrary elliptic BA slices without constructing their real Gram gauge.

This is a **typed, explicitly calculable system** of differential-algebraic, projective, elliptic and geometric transformations. It is not merely an analogy, but neither is it one universal flat connection or one universal self-adjoint operator.

### 26.3 Proposed theorem for eventual foundational consolidation

**Selected Elliptic Picard–Spin–Darboux Correspondence (conditional).** For each $0<m<1$ with its matched positive real Riemann modulus and fixed resolution $r$, the smooth one-gap Lamé spectral curve and Riemann elliptic conformal curve are isomorphic with their declared holomorphic differential scale. The moving Dirichlet divisor defines a linear Abel–Jacobi flow that hits the Riemann WE 2-torsion spin structure at explicit spatial half-periods. The Riemann sigma WE spinor at that selected branch point is simultaneously a Lamé band-edge Hermite function in the elliptic Abel coordinate, and its reciprocal spinor is a Darboux partner related by the identical 2-torsion half-period translation. The WE horizontal exact differential is its Riccati derivative. The identities hold **as specified algebraic/meromorphic/holomorphic data**; extension to global connection-preserving and real self-adjoint operator equivalence requires additional hypotheses and is not claimed.

**Status:** The component identities, divisor classes and transformation formulas were proved or algebraically checked here. The theorem is a provisional **selected correspondence**, not a classification of all minimal/maximal surfaces or all SL–EP theories. It belongs in the draft staging folder pending the additional global BA normalization and connection audit.
