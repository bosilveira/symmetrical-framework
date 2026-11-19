---
id: SF-DRAFT-190
title: Fibration Holography and Holonomy-Aware Symmetry Reduction
status: provisional
created: 2026-11-19
proposed_layers: [I, II, III]
depends_on: [SF-I-020, SF-DRAFT-030, SF-DRAFT-120, SF-DRAFT-140, SF-DRAFT-150, SF-DRAFT-160, SF-DRAFT-170, SF-DRAFT-180]
related_claims: [H46, H95, H100, H136, H169, H299, H391, H424, H466, H467, H468, H470]
---

# 190 Fibration Holography and Holonomy-Aware Symmetry Reduction

**Status:** Provisional mathematical investigation. [D] proved directly; [V] independently checked; [K] established result with hypotheses; [H] archived verified claim retaining original scope; [C] correction/counterexample; [O] open.

**Question:** Does higher-dimensional parallel transport survive projection to a lower-dimensional base? What information is actually preserved by symmetry reduction, and which additional bundle, connection, representation, residue and period data are needed to reconstruct the higher-dimensional structure? How do the canonical logarithmic coordinate, catenoid, Hopf map, Sturm–Liouville, Ermakov–Pinney, and Lamé–Riemann marked periods participate?

**Principal conclusion:** Ordinary invariant scalar reduction can lose fiber topology and holonomy. A connection-aware reduction that retains **all fiber charges as sections of associated bundles**, together with their transition maps and the fiber metric, gives an exact reconstruction of the higher-dimensional scalar Laplacian. This is the precise conditional content of the proposed *fibration holography*. It is **not** an AdS/CFT-type bulk/boundary duality, nor an assertion that any scalar one-dimensional ODE uniquely determines its higher-dimensional geometry.

**Sources inspected:** The November 18 historical project ZIP, including ARCHITECTURE.md (which explicitly leaves the Hopf lift outside the old foundational theorem), sato-grassmannian.md (H136), Riemann marked-period/Gauss–Manin notes and CLAIMS; live GitHub drafts 140–180, especially draft 180 on typed parallel transports and Hopf Chern degrees. Standard external Riemannian submersion, circle-bundle Fourier/Bochner and differential-cohomology literature is cited in §22.

## 1. Terminology: projection, reduction, transport and reconstruction

A principal circle fibration is a bundle $\pi:P^{d+1}\to B^d$ with fiber $U(1)$ and a transition cocycle. A connection specifies a horizontal complement to the vertical tangent space. These are four **different** operations:

1. **Point projection:** the map $\pi:P\to B$, which forgets fiber position.
2. **Neutral or invariant reduction:** retain only scalar functions constant along circle fibers.
3. **Charge-graded reduction:** retain every Fourier mode $n\in\mathbb Z$, globally interpreted as a section of an associated line bundle $L^n$ on $B$.
4. **Reconstruction:** retain the base, the bundle/transition data, the connection, the fiber metric and the full representation-graded reduced operators.

**Correction [C].** A bundle base is **not generally a boundary** of the total space. The Hopf map $S^3\to S^2$ has a closed total space and closed base. A base has dimension $\dim P-\dim F$, not necessarily $\dim P-1$. Thus the proposed phrase *holography* is a programmatic comparison, not yet a physical or mathematical boundary duality.

## 2. Holonomic is NOT the same as holonomy-aware [D,C]

In a local circle gauge write

```math
\vartheta=d\theta+A,\qquad F=dA,\qquad X^H=X-A(X)\partial_\theta.
```

For horizontal lifts,

```math
[X^H,Y^H]^V=-F(X,Y)\partial_\theta.
```

Hence horizontal planes are **integrable/holonomic iff $F=0$ locally**. The standard Hopf connection has nonzero curvature: its horizontal distribution is **nonholonomic**. The accurate name for the proposed scheme is *Holonomy-Aware Symmetry Reduction*, not holonomic reduction unless integrability is specifically assumed.

For a contractible base loop $\gamma=\partial\Sigma$,

```math
\operatorname{Hol}_A(\gamma)=\exp\left(-i\oint_\gamma A\right)=\exp\left(-i\int_\Sigma F\right)
```

under the stated sign convention. Flat connections can still have nontrivial holonomy around noncontractible loops, so curvature alone does not exhaust the connection data.

## 3. Kaluza–Klein metric: the fiber can be reconstructed from enriched base data [D,K]

Fix an oriented Riemannian base $(B^d,h)$, principal circle bundle $P\to B$, a principal connection $\vartheta$ normalized for a $2\pi$ fiber and a smooth positive basic fiber radius $\phi:B\to(0,\infty)$. Define

```math
g_P=\pi^*h+(\phi\circ\pi)^2\vartheta^2.
```

In a local trivialization,

```math
ds_P^2=h_{ij}(b)db^i db^j+\phi(b)^2(d\theta+A_i(b)db^i)^2.
```

Its determinant and inverse blocks are

```math
\det g_P=\phi^2\det h,\quad g^{ij}=h^{ij},\quad g^{i\theta}=-h^{ij}A_j,\quad g^{\theta\theta}=\phi^{-2}+h^{ij}A_iA_j.
```

The volume form is

```math
d\mathrm{vol}_{g_P}=\phi(b)d\mathrm{vol}_h(b)\,d\theta.
```

**Theorem 3.1 [D].** These data determine a globally defined invariant metric on the chosen principal bundle. On overlaps, $\theta_\beta=\theta_\alpha+\chi_{\alpha\beta}$ and $A_\beta=A_\alpha-d\chi_{\alpha\beta}$ leave $d\theta+A$ and the global metric invariant. The resulting metric is uniquely determined by the **specified** enriched data, not by the base metric alone.

## 4. Exact charge-graded Fourier/Laplace reduction theorem [D,K,V]

Locally express the $n$-th fiber representation sector as

```math
\Psi_n(b,\theta)=(2\pi)^{-1/2}e^{in\theta}f_n(b),\qquad n\in\mathbb Z,\quad D_i^{(n)}=\partial_i-inA_i.
```

Under the gauge overlap above, the coefficient transforms as $f_{n,\beta}=e^{-in\chi_{\alpha\beta}}f_{n,\alpha}$: it is **globally a section of $L^n$**.

**Theorem 4.1 [D,K,V] (complete circle Fourier decomposition).** With $\Delta=\mathrm{div}\nabla$,

```math
\Delta_{g_P}\Psi_n=(2\pi)^{-1/2}e^{in\theta}\left[\frac1{\phi\sqrt{|h|}}D_i^{(n)}\left(\phi\sqrt{|h|}h^{ij}D_j^{(n)}f_n\right)-\frac{n^2}{\phi^2}f_n\right].
```

The total scalar Hilbert space decomposes unitarily as

```math
L^2(P,d\mathrm{vol}_{g_P})\cong\widehat{\bigoplus}_{n\in\mathbb Z}L^2(B,L^n;\phi\,d\mathrm{vol}_h).
```

Thus the positive total Laplacian restricts on charge $n$ to

```math
\mathcal H_n=-\frac1{\phi\sqrt{|h|}}D_i^{(n)}\left(\phi\sqrt{|h|}h^{ij}D_j^{(n)}\right)+\frac{n^2}{\phi^2}.
```

The first term is the weighted **magnetic/Bochner Laplacian**, understood acting on sections; globally natural self-adjoint domains are transported from the complete/compact total Laplacian.

**Proof.** Insert the inverse metric and determinant from §3 into the coordinate Laplace–Beltrami formula. The vertical derivative $\partial_\theta$ becomes $in$ and horizontal derivatives $\partial_i-A_i\partial_\theta$ become $D_i^{(n)}$. Orthogonality of Fourier characters and the fiber volume produce the Hilbert direct sum; gauge transition factors glue the operators.

### 4.1 Neutral mode and the half-density

At $n=0$, the connection $A$ disappears:

```math
\mathcal H_0=-\phi^{-1}\mathrm{div}_h(\phi\nabla_h),\qquad\|\Psi_0\|_{L^2(P)}^2=\int_B|f_0|^2\phi\,d\mathrm{vol}_h.
```

The unitary multiplier $U_\phi f=\sqrt\phi f$ maps the neutral weighted space to $L^2(B,d\mathrm{vol}_h)$ and gives

```math
U_\phi\mathcal H_0U_\phi^{-1}=-\Delta_h+\frac{\Delta_h\sqrt\phi}{\sqrt\phi}.
```

The same half-density in a charged sector gives the covariant Bochner Laplacian plus the displayed density potential and $n^2/\phi^2$. **The scalar invariant reduction remembers the fiber radius as a weight but forgets the connection and its topology.**

## 5. A rigorous counterexample: same invariant operator, different total topology [D,K,C]

On the same round base $(B,h)=(S^2,g_{\rm round})$, fix a **constant** fiber radius $\phi=\ell>0$. Compare two principal circle bundles:

- $P_0=S^2\times S^1$, whose first Chern class is zero and whose connection may be flat.
- $P_1=S^3\to S^2$ (Hopf), whose first Chern class is one and whose natural connection has nonzero curvature.

Equip both with the invariant metric of §3 using their respective connections. The total spaces are topologically different, but their neutral scalar Hilbert operators are identical:

```math
\mathcal H_0^{P_0}=\mathcal H_0^{P_1}=-\Delta_{S^2},\qquad \|f_0\|^2=\ell\int_{S^2}|f_0|^2\,dA_h.
```

**Theorem 5.1 [D,K] (non-faithfulness of uncharged reduction).** A reduced invariant SL/Laplace equation together with its **weighted measure and full neutral spectrum** does not determine the total bundle's Chern class, connection, or total topology.

For each $k\in\mathbb Z$ there is a principal circle bundle $P_k\to S^2$ with $c_1=k$; all can carry the *same* base metric and constant radius $\ell$ and therefore the **same $\mathcal H_0$**. For $k\ne0$ their total spaces include lens-space types, whereas $k=0$ is the product.

### 5.1 What the charged sectors retain

For the bundle $P_k$, the $n$-th reduced coefficient is a section of an associated bundle of Chern number

```math
c_1(L^n)=n\,c_1(P_k)=nk.
```

Its covariant derivative contains $nA$, and its Bochner Laplacian knows the curvature through commutators

```math
[D_i^{(n)},D_j^{(n)}]=-inF_{ij}.
```

This gives a precise **positive reconstruction statement for the operator decomposition**, not a theorem that *unlabeled eigenvalue sets alone* determine all bundle topology: isospectral or gauge-equivalent situations require careful distinction. The full charge-graded spaces, transition maps and covariant operators carry more information than the neutral scalar spectrum.

## 6. Curvature, Chern class and holonomy are not identical [D,K,C]

On a principal $U(1)$ bundle, $F=dA$ represents the **real** first Chern class with the chosen sign:

```math
\frac1{2\pi}\int_\Sigma F=\langle c_1(P),[\Sigma]\rangle\in\mathbb Z
```

for a smooth oriented closed base two-cycle $\Sigma$. Principal circle bundles over a paracompact base are classified by their **integral** Chern classes in $H^2(B,\mathbb Z)$, not just by the de Rham class of $F$.

Two independent obstructions to reconstruction from **curvature alone** are:

1. Torsion classes in integral $H^2(B,\mathbb Z)$ have zero real image, so de Rham curvature can miss torsion topology.
2. Flat connections can have nontrivial holonomy on noncontractible loops even when $F=0$.

The standard full invariant of a circle bundle **with connection** is the corresponding degree-two differential-cohomology/differential-character class: it keeps integral Chern data, curvature and compatible holonomy, and is defined without choosing a global gauge potential $A$.

**Theorem 6.1 [K,C].** Base metric $h$, radius $\phi$ and curvature form $F$ do not generally reconstruct a bundle with connection. The enriched data $(P,\vartheta,h,\phi)$ do reconstruct the KK metric and its charge-graded scalar Laplacian. One may specify $(P,\vartheta)$ equivalently by suitable global differential-cohomology cocycle/holonomy data.

## 7. An elementary FLAT connection with nontrivial global holonomy [D,V]

Take a base circle $\beta\sim\beta+2\pi$ of radius $R_B>0$, a trivial fiber circle $\theta\sim\theta+2\pi$ of radius $\ell>0$, and a constant $\alpha\in\mathbb R$:

```math
g_P=R_B^2d\beta^2+\ell^2(d\theta+\alpha\,d\beta)^2,\qquad A=\alpha\,d\beta,\quad F=0.
```

Its holonomy around the base loop is

```math
\operatorname{Hol}(\beta\text{-loop})=e^{-2\pi i\alpha}.
```

The exact Laplacian eigenvalues on globally single-valued functions $e^{ik\beta+in\theta}$, $k,n\in\mathbb Z$, are

```math
-\Delta_{g_P}e^{ik\beta+in\theta}=\left[\frac{(k-n\alpha)^2}{R_B^2}+\frac{n^2}{\ell^2}\right]e^{ik\beta+in\theta}.
```

**Theorem 7.1 [D,V].** The neutral $n=0$ spectrum is independent of the *nontrivial flat holonomy* parameter $\alpha$, while charged $n\ne0$ sectors contain the gauge-covariant shift $k-n\alpha$. Shifting $\alpha\mapsto\alpha+j$ with $j\in\mathbb Z$ produces the same gauge class after relabeling $k$.

This is the simplest exact example in which connection holonomy exists **without any local curvature** and is lost under uncharged symmetry reduction.

## 8. The catenoid as an EXACT circle reduction over a one-dimensional base [D,V,H]

Fix the canonical variables with explicit scales

```math
u=\ln(x/c),\quad x=ce^u,\quad r,c>0,\quad R=\cosh(ru),\quad S=R^{-1},\quad W=\tanh(ru).
```

The canonical Euclidean catenoid immersion from drafts 130–180 is

```math
X_C(u,v)=\left(\frac{R(u)}r\cos(rv),\frac{R(u)}r\sin(rv),u\right),\qquad v\sim v+\frac{2\pi}r.
```

Set the true $2\pi$-periodic fiber angle $\theta=rv$, and the **base meridian arclength**

```math
ds=R\,du,\qquad s=\frac1r\sinh(ru),\qquad\phi(s)=\frac{R(u)}r=\frac1r\sqrt{1+r^2s^2}.
```

The catenoid metric is **exactly** a warped circle bundle with a trivial connection:

```math
g_C=R^2(du^2+dv^2)=ds^2+\phi(s)^2d\theta^2,\qquad A=0,\quad F=0.
```

Its volume element and neutral scalar Laplace reduction are

```math
dA_C=\phi(s)\,ds\,d\theta,\qquad \Delta_C^{(0)}f=\phi^{-1}\partial_s(\phi\,\partial_s f)=R^{-2}f_{uu}.
```

This is a **weighted one-dimensional SL equation** on the meridian; in $s$ the weight and leading coefficient are $p=w=\phi$, while in $u$ (up to a constant normalization) they are $p=1$, $w=R^2$.

### 8.1 Curvature is recoverable from the base AND radius, not the neutral connection

For a warped metric $ds^2+\phi(s)^2d\theta^2$, its Gaussian curvature is

```math
K_C=-\frac{\phi_{ss}}{\phi}=-\frac{r^2}{(1+r^2s^2)^2}=-r^2S^4.
```

**Theorem 8.1 [D,V].** The reduced catenoid metric data $(ds^2,\phi(s))$ reconstruct the entire intrinsic metric and its negative Gaussian curvature, despite the fact that the principal circle connection is **flat** ($F=0$) and the total circle bundle is **topologically trivial**.

This is a key warning: intrinsic Levi–Civita Gaussian curvature of a *warped* total surface is **not** the same as curvature $F$ of its selected principal circle connection.

### 8.2 Exact catenoid Jacobi reduction

For $f(u,v)=e^{inrv}h(u)$, $n\in\mathbb Z$, the negative minimal-surface Jacobi operator $B_C=-(\Delta_C+|A_C|^2)$, with $|A_C|^2=2r^2S^4$, becomes

```math
B_{C,n}h=R^{-2}\left[-h_{uu}+(n^2r^2-2r^2S^2)h\right].
```

Its spectral eigenvalue equation is therefore

```math
-h_{uu}+(n^2r^2-2r^2S^2)h=\lambda_JR^2h.
```

The actual Hilbert weight is $R^2du$; multiplying by $R^2$ to obtain a Pöschl–Teller **zero** equation is not a unitary operator conjugation. The genuine unitary half-density yields the different SL expression

```math
R B_{C,n}R^{-1}=-\partial_u(S^2\partial_u)+(n^2-1)r^2S^2.
```

This is exactly the existing operator-domain distinction of draft 140, now derived as a **fiber-mode reduction** of the two-dimensional surface geometry.

### 8.3 The original center and resolution are typed

The scale $r$ determines neck radius $1/r$, angular period $2\pi/r$ and curvature profile; the center $c$ marks where $u=\ln(x/c)=0$. Changing $c$ with the *same intrinsic catenoid* changes the multiplicative chart, not its topology. The amplitude $\mu$ of the canonical original Symmetrical Function is **not** an independent parameter of this chosen catenoid metric.

## 9. Levi–Civita curvature and teleparallel torsion on the catenoid [D,H,C]

The coframe from draft 180 is

```math
e^1=R\,du,\quad e^2=R\,dv,\qquad T_W^1=0,\quad T_W^2=rSW\,e^1\wedge e^2.
```

Set $t_2=rSW$ and $e_1=S\partial_u$. Then

```math
K_C=-e_1(t_2)-t_2^2=-r^2S^4.
```

This **frame-dependent teleparallel reconstruction** is compatible with the warped fiber-radius formula $K_C=-\phi_{ss}/\phi$. The two computations encode the *same intrinsic surface metric* using different auxiliary data. Neither identifies the Riccati factorization $-\partial_u^2+h^2-h_u$ with the Bochner–Weitzenböck tensor identity or the connection curvature $F=dA$ of the rotational circle bundle (which is zero here).

**Four distinct connections can coexist on this example:** the nonflat surface tangent Levi–Civita connection, the flat chosen teleparallel frame connection with torsion, the flat rotational bundle connection $d\theta$, and the nonflat pullback Hopf connection of the *Gauss map*. Their curvatures, torsions and holonomies must be typed separately.

## 10. The Gauss-map Hopf bundle is NOT the catenoid rotational bundle [D,H,K]

For a meromorphic Gauss map $g:\Sigma\to\mathbb{CP}^1$ on a **compactified Riemann surface**, choose the local normalized spinor

```math
\eta_g=\frac{(1,g)}{\sqrt{1+|g|^2}},\qquad A_g=-i\eta_g^\dagger d\eta_g=\frac{\bar g\,dg-g\,d\bar g}{2i(1+|g|^2)}.
```

The curvature and Chern number of this **different circle bundle** are

```math
F_g=dA_g=\frac{i\,dg\wedge d\bar g}{(1+|g|^2)^2}=\frac12g^*\omega_{S^2},\qquad\frac1{2\pi}\int_\Sigma F_g=\deg(g).
```

The local potential must be patched at $g=\infty$; it is not a globally defined one-form when the Chern number is nonzero.

The compactified **catenoid Gauss map** $g_C=-t$ on $\mathbb{CP}^1$ has degree one. The **Riemann minimal-example** Gauss projection from its compactified elliptic curve,

```math
E_R:\quad y_R^2=g_R^3+k_Rg_R^2-g_R,\qquad (g_R,y_R)\mapsto g_R,
```

has degree two. The existing calculation in draft 180 therefore gives

```math
c_1(g_C^*\mathrm{Hopf})=1,\qquad c_1(g_R^*\mathrm{Hopf})=2.
```

**Theorem 10.1 [D,H].** In the corresponding charge-$n$ associated bundles, the first Chern numbers are $n$ for the catenoid Gauss-map pullback and $2n$ for the Riemann Gauss-map pullback. Their **uncharged** scalar sections are topologically trivial, but the charged sectors carry the distinction.

**Essential distinction:** The catenoid rotational fibration $C\simeq\mathbb R\times S^1\to\mathbb R$ is **trivial with flat principal circle connection**. The *different* Gauss-map Hopf pullback extends over the compactified conformal sphere with $c_1=1$. These can coexist because they are bundles over **different bases** with different projection maps. One cannot infer the Hopf class from the rotational scalar SL equation alone.

## 11. O'Neill curvature is the correct bridge for a Riemannian submersion [D,K]

For the KK metric of §3 with **constant** fiber radius $\phi=\ell$, the principal connection's curvature appears in the horizontal O'Neill tensor. For orthonormal horizontal lifts of base orthonormal vectors $X,Y$,

```math
\mathsf A_{X^H}Y^H=\frac12[X^H,Y^H]^V=-\frac12F(X,Y)\,\partial_\theta,\quad\|\mathsf A_{X^H}Y^H\|^2=\frac{\ell^2}{4}F(X,Y)^2.
```

The O'Neill sectional-curvature formula is

```math
K_B(X,Y)=K_P(X^H,Y^H)+3\|\mathsf A_{X^H}Y^H\|^2=K_P(X^H,Y^H)+\frac{3\ell^2}{4}F(X,Y)^2.
```

**Theorem 11.1 [D,K].** Under these declared **constant-radius** conditions, the difference between horizontal sectional curvature in the total space and base curvature is an explicit quadratic function of the principal connection curvature $F$. This is the correct Riemannian-submersion curvature mechanism. With variable $\phi$, additional second-fundamental-form/mean-curvature (O'Neill $T$-tensor) terms enter other curvature components: do not extrapolate this formula unmodified.

**Check against catenoid:** Its base is one-dimensional, so there is no horizontal two-plane $X\wedge Y$ and no nonzero $F$. The catenoid's negative surface curvature is instead the **mixed vertical–horizontal warped curvature** $-\phi_{ss}/\phi$ of §8. The two identities describe complementary curvature components rather than competing explanations.

## 12. Marked meromorphic residues and periods are preserved only under DECLARED maps [D,K,C]

Let $f:\widetilde\Sigma\to\Sigma$ be a holomorphic map of Riemann surfaces and $\omega$ a meromorphic one-form near $q=f(p)$. If its local simple pole has residue $a$ and $f$ has ramification index $e_p$ at $p$, choose local coordinates $w=z^{e_p}$ (up to a nonzero unit). Then

```math
\omega\sim a\,\frac{dw}{w},\qquad f^*\omega\sim e_pa\,\frac{dz}{z},\qquad\operatorname{Res}_p(f^*\omega)=e_p\operatorname{Res}_q\omega.
```

Thus residues are **not literally unchanged by arbitrary projection/pullback**; they scale with local degree. Likewise the period identity is

```math
\int_{\widetilde\gamma}f^*\omega=\int_{f_*\widetilde\gamma}\omega,
```

where the pushforward cycle includes its winding/multiplicity. Real immersion period closing is a condition on the **real parts of the three marked Weierstrass periods**, not on an unspecified scalar holonomy.

### 12.1 Exact special case: framework resolution multiplication

In draft 160, with $t_r=e^{r\zeta}$, a resolution change $r\mapsto Mr$, $M\in\mathbb N$, sends $t_{Mr}=t_r^M$. For the marked catenoid logarithmic height differential,

```math
dh_r=\frac1r d\log t_r,\qquad (t\mapsto t^M)^*dh_{Mr}=\frac1{Mr}d\log(t_r^M)=dh_r.
```

The differential is preserved here **because the scale $1/(Mr)$ compensates the ramification degree $M$**. The source loop winds $M$ times around the target puncture. This is an explicit *selected period-preserving pullback*; it does not prove that arbitrary symmetry reductions preserve all holonomies and residues.

## 13. A type-safe distinction among three monodromies [D,C]

The project already uses monodromy in several precise, different ways:

| Mechanism | Path/base | Fiber and operator | Preserved data |
|---|---|---|---|
| Spatial SL carrier | $u$ over a selected interval or period, with fixed spectral energy $E$ | rank-two solution vectors / $\mathrm{SL}(2)$ | Wronskian; transfer matrix |
| Gauss–Manin | path in a modulus space, e.g. $m_{\rm ell}$ | marked homology/cohomology of elliptic fibers | intersection pairing / symplectic period determinant |
| Principal Hopf connection | loop on the Gauss sphere or its pullback surface | one-dimensional unitary fiber | Berry/Hopf holonomy, Chern class on closed 2-cycles |
| Euclidean Weierstrass affine integration | loop on punctured surface | translations of $\mathbb R^3$ | real immersion period vector |

A rank-two Riccati projective coordinate is a coordinate on a projective line, **not** itself the phase of a Hopf lift. A Gauss–Manin matrix acts on *cycles as a parameter moves*, not on the SL Cauchy vector at fixed spectral energy. The Weierstrass period translation is **abelian affine holonomy**, not the surface tangent LC holonomy.

**No-go [C].** There is no general theorem that quotienting by symmetry preserves all of these matrices or identifies their conjugacy classes. Each needs a specified induced connection/representation and a comparison map that transports the relevant paths and domains.

## 14. The selected Lamé–Riemann all-modulus curve isomorphism is still exact [H,D]

The archive and draft 170 establish a **selected smooth one-gap Lamé spectral curve** and its explicit real isomorphism to the Riemann minimal-example elliptic family. With all independent parameters typed,

```math
m_{\rm ell}=(1+\lambda_R^2)^{-1},\quad k_R=\lambda_R^{-1}-\lambda_R,\quad D_R=\lambda_R+\lambda_R^{-1},\quad r>0,
```

```math
\Gamma_m:\quad \eta^2=-(E+mr^2)(E-(1-2m)r^2)(E-(1-m)r^2),
```

```math
g_R=-k_R-\frac{D_R}{r^2}E,\qquad y_R=\frac{D_R^{3/2}}{r^3}\eta,\qquad\frac{dg_R}{y_R}=-\frac r{\sqrt{D_R}}\frac{dE}{\eta}.
```

The Riemann Weierstrass one-forms are transported as **meromorphic forms on the selected smooth elliptic curve**. The exact marked period gauge from draft 170 relates the Gauss–Manin systems and preserves a nonzero symplectic period determinant (up to orientation).

**What this map does NOT assert:** The map $g_R=g_R(E)$ is **constant along the SL spatial variable $u$ if the spectral point $E$ is held fixed**. It therefore does not convert the moving spatial Riccati ratio $\phi_u/\phi$ into a Hopf horizontal lift without an additional, explicitly defined moving-spectral-point construction. The curve's holomorphic height form also differs from the normalized spectral second-kind quasimomentum differential in pole divisor.

### 14.1 Why the catenoid and arctangent limits are nevertheless relevant

In the two *different nodal limits* of the smooth Lamé spectral curve, draft 170 proved

```math
m\to1:\quad \frac{dE}{\eta}\to\frac{2\,ds}{s^2-r^2}=\frac1r\,d\log\frac{s-r}{s+r}=dh_C.
```

```math
m\to0:\quad \frac{dE}{\eta}\to-\frac{2\,ds}{s^2+r^2}=-2\sqrt\mu\,f_\mu(x;r,c)\,dx
```

under the separately declared real/projective coordinate identifications of drafts 160–170. They are exact **marked differential degenerations**, not one common global operator or topological boundary projection.

## 15. Riccati–Pinney is parallel transport of a DIFFERENT rank-two bundle [D,H]

The general real scalar carrier can be written as a flat first-order connection along a one-dimensional independent coordinate:

```math
\frac d{du}\binom{y}{y_u}=\begin{pmatrix}0&1\\V(u)-E&0\end{pmatrix}\binom{y}{y_u},\qquad \nabla^{SL}=d-\mathsf A\,du.
```

Its Wronskian is constant because $\mathrm{tr}\mathsf A=0$. The projective coordinate $z=y_u/y$ obeys $z_u+z^2=V-E$. A selected positive Gram envelope $\rho$ of two independent carrier solutions satisfies an EP equation and a time/clock change

```math
\rho_{uu}+\omega(u)^2\rho=\kappa\rho^{-3},\qquad \tau_u=\rho^{-2}.
```

With $y=\rho Y(\tau)$, the linear carrier becomes the constant-coefficient equation

```math
Y_{\tau\tau}+\kappa Y=0,\qquad \omega^2=\kappa(\tau_u)^2+\frac12\{\tau,u\}.
```

This is an exact **gauge and reparametrization** of the rank-two local SL solution system. The phase/current $\vartheta_u=j/\rho^2$ with $j^2=\kappa$ is a scalar carrier phase, and for periodic $\rho$ its increment can encode a Floquet rotation number. Neither the Wronskian nor this phase by itself determines the curvature/Chern class of an independent Hopf circle bundle.

**Theorem 15.1 [D,H] (what the EP lift actually preserves).** The positive EP clock transforms the local real SL solution space, projective Schwarzian and its determinant/Wronskian invariant. Any relation to the **Hopf** Berry connection requires an additional normalized complex spinor, a Hermitian structure, and a specified map of base paths. None is automatically supplied by the scalar EP amplitude.

## 16. NEW EXACT LIFT: the canonical weighted Master SL carrier is the neutral sector of a hyperbolic cylinder [D,V]

There is a particularly strong, simple application of Theorem 4.1 to the original framework, distinct from the catenoid metric.

Recall the **original linear carrier** and weighted Hilbert space:

```math
\mathcal L_xf=-\frac1x(x^3f_x)_x+(r^2-1)f,\qquad \mathcal H_x=L^2((0,\infty),x\,dx).
```

Keep $u=\ln(x/c)$ and choose a **specific two-dimensional geometric lift**, with $2\pi$-periodic angle $\theta$ and strictly positive circle radius

```math
\phi_{\rm hyp}(u)=x^2=c^2e^{2u},\qquad g_{\rm hyp}=du^2+\phi_{\rm hyp}(u)^2d\theta^2=du^2+c^4e^{4u}d\theta^2.
```

This is a globally smooth metric on the cylinder $\mathbb R_u\times S^1_\theta$ (with fixed choice of dimensionless metric units). The principal rotational circle connection is trivial, $A=0$.

**Theorem 16.1 [D,V] (canonical weighted SL as hyperbolic neutral reduction).** On functions invariant under $\theta$, the lifted Laplacian and its natural measure satisfy

```math
\Delta_{\rm hyp}^{(0)}=\partial_u^2+2\partial_u,\qquad\phi_{\rm hyp}\,du=x^2du=x\,dx.
```

The original carrier is **exactly**

```math
\mathcal L_x=-\Delta_{\rm hyp}^{(0)}+(r^2-1)
```

on the identified neutral Hilbert space. Multiplication by the positive half-density $\sqrt{\phi_{\rm hyp}}=x$ is precisely the **canonical** Liouville unitary and gives

```math
U_c\mathcal L_xU_c^{-1}=-\partial_u^2+r^2,\qquad U_cf(u)=xf(ce^u).
```

**Proof.** The circle-volume factor gives $\Delta^{(0)}=\phi^{-1}\partial_u(\phi\partial_u)$, and $\phi_u/\phi=2$. The volume identity is $x\,dx=x^2du$. The conjugation can be checked by substituting $f=\psi/x$.

### 16.1 Exact constant negative Gaussian curvature

For any warped surface $g=du^2+\phi(u)^2d\theta^2$, $K=-\phi_{uu}/\phi$. Here

```math
K_{\rm hyp}=-\frac{\partial_u^2(c^2e^{2u})}{c^2e^{2u}}=-4.
```

To see completeness and the hyperbolic geometry explicitly, set

```math
y=e^{-2u}>0,\qquad z=2c^2\theta,\qquad g_{\rm hyp}=\frac{dy^2+dz^2}{4y^2},\quad z\sim z+4\pi c^2.
```

This is the constant-curvature-$-4$ upper-half-plane metric modulo a parabolic translation; it is complete and has a shrinking horocyclic circle end as $u\to-\infty$.

**Structural significance.** The canonical **one-dimensional weighted metric** $du^2$ is intrinsically flat, yet the neutral SL equation is exactly the invariant reduction of this **specified two-dimensional hyperbolic metric**. The negative curvature is encoded by the retained fiber radius $\phi=x^2$; it is invisible if one retains only the Liouville-conjugated free operator and throws away the positive half-density.

**Nonuniqueness caveat [C].** This does not imply the hyperbolic cylinder is the **unique** higher-dimensional geometry generating the original SL equation. Other choices of fiber, metric, density and extra potential can produce the same neutral scalar differential expression. The exact lift gives a constructive existence theorem, not a unique inverse-geometric reconstruction.

## 17. Charged modes of the same exact lift produce a Bessel/Mellin spectral hierarchy [D,V,K]

Retain all angular charges $n\in\mathbb Z$ in the hyperbolic metric of §16, still with the same scalar shift $(r^2-1)$. The full geometric operator is

```math
\mathscr L_{\rm hyp}=-\Delta_{g_{\rm hyp}}+(r^2-1).
```

On the $n$-th normalized angular mode its weighted one-dimensional expression is

```math
\mathscr L_{\rm hyp}^{(n)}=-\partial_u^2-2\partial_u+(r^2-1)+\frac{n^2}{c^4e^{4u}}.
```

After **the same unitary multiplier $x$ as for the original weighted SL**, every charged mode becomes

```math
U_c\mathscr L_{\rm hyp}^{(n)}U_c^{-1}=-\partial_u^2+r^2+\frac{n^2}{c^4e^{4u}}=-\partial_u^2+r^2+\frac{n^2}{x^4}.
```

This is a one-dimensional **exponential-wall Schrödinger operator**. It is not the reflectionless Pöschl–Teller potential of draft 140; it is a different exact spectral realization emerging from the same underlying weighted metric.

### 17.1 Exact modified-Bessel eigenfunctions

For nonzero $n$, set

```math
t=\frac{|n|}{2c^2}e^{-2u}=\frac{|n|}{2x^2},\qquad \lambda=r^2+k^2,\qquad k>0,\qquad \kappa=k/2.
```

Then the spectral equation becomes

```math
t^2\psi_{tt}+t\psi_t+(\kappa^2-t^2)\psi=0.
```

Its solution exponentially decaying toward the high exponential wall ($u\to-\infty$, $t\to\infty$) is the **modified Bessel/Macdonald function**

```math
\psi_{n,k}(u)=K_{i k/2}\left(\frac{|n|}{2c^2}e^{-2u}\right).
```

**Theorem 17.1 [D,V] (exact charged generalized eigenfunction).** Each charged sector has a complete modified-Bessel scattering basis (in generalized-eigenfunction sense) with continuum threshold $\lambda=r^2$, under the natural self-adjoint realization. The neutral sector $n=0$ instead has free Fourier characters $e^{iku}$: both arise from the **same 2D hyperbolic Laplacian**, separated by their circle representation charge.

### 17.2 Exact unit-modulus reflection coefficient

For $k>0$ the small-$t$ expansion of $K_{i\kappa}(t)$ is

```math
K_{i\kappa}(t)\sim\frac12\Gamma(i\kappa)(t/2)^{-i\kappa}+\frac12\Gamma(-i\kappa)(t/2)^{i\kappa}.
```

At $u\to+\infty$, where $t/2=(|n|/(4c^2))e^{-2u}$, the two terms are respectively outgoing $e^{+iku}$ and incident $e^{-iku}$ waves. Hence

```math
\mathcal R_n(k)=\frac{\Gamma(ik/2)}{\Gamma(-ik/2)}\left(\frac{|n|}{4c^2}\right)^{-ik},\qquad|\mathcal R_n(k)|=1.
```

This is **total reflection from an exponential wall**, not Pöschl–Teller reflectionlessness, which has zero reflection coefficient and nontrivial transmission. The $c$ dependence is a phase shift tied to the chosen logarithmic origin/metric scaling, not a claim that the intrinsic topological class depends on $c$.

### 17.3 The spectral Plancherel transform becomes Kontorovich–Lebedev

Let $F(t)=\psi(u(t))$ and form the classical Kontorovich–Lebedev transform

```math
\widehat F(\kappa)=\int_0^\infty K_{i\kappa}(t)F(t)\,\frac{dt}{t},\qquad \kappa>0.
```

On its standard dense domain the inversion and Plancherel identities are

```math
F(t)=\frac2{\pi^2}\int_0^\infty \kappa\sinh(\pi\kappa)K_{i\kappa}(t)\widehat F(\kappa)\,d\kappa.
```

```math
\int_0^\infty|F(t)|^2\frac{dt}{t}=\frac2{\pi^2}\int_0^\infty\kappa\sinh(\pi\kappa)|\widehat F(\kappa)|^2d\kappa.
```

Since $|du|=dt/(2t)$, the original flat logarithmic Hilbert norm is

```math
\int_{\mathbb R}|\psi(u)|^2du=\frac1{\pi^2}\int_0^\infty\kappa\sinh(\pi\kappa)|\widehat F(\kappa)|^2d\kappa.
```

**New exact synthesis:** The same canonical weighted space $L^2(x\,dx)$ can be realized geometrically so that **neutral modes use Fourier–Mellin Plancherel** and **charged modes use Kontorovich–Lebedev Plancherel**. The difference is a rigorous consequence of retaining, rather than discarding, the circle fiber representations. See NIST DLMF §10.43 and the classical Kontorovich–Lebedev inversion theory; the spectral transform formula requires its standard $L^2$ interpretation and generalized eigenfunction domains.
