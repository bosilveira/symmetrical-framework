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
\frac{\sigma(z-a)}{\sigma(z-b)}\,\exp\big((\zeta(a)-\zeta(b))z\big),
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
