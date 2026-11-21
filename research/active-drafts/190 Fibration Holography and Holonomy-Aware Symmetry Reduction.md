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

A principal circle fibration is a bundle $`\pi:P^{d+1}\to B^d`$ with fiber $`U(1)`$ and a transition cocycle. A connection specifies a horizontal complement to the vertical tangent space. These are four **different** operations:

1. **Point projection:** the map $`\pi:P\to B`$, which forgets fiber position.
2. **Neutral or invariant reduction:** retain only scalar functions constant along circle fibers.
3. **Charge-graded reduction:** retain every Fourier mode $`n\in\mathbb Z`$, globally interpreted as a section of an associated line bundle $`L^n`$ on $`B`$.
4. **Reconstruction:** retain the base, the bundle/transition data, the connection, the fiber metric and the full representation-graded reduced operators.

**Correction [C].** A bundle base is **not generally a boundary** of the total space. The Hopf map $`S^3\to S^2`$ has a closed total space and closed base. A base has dimension $`\dim P-\dim F`$, not necessarily $`\dim P-1`$. Thus the proposed phrase *holography* is a programmatic comparison, not yet a physical or mathematical boundary duality.

## 2. Holonomic is NOT the same as holonomy-aware [D,C]

In a local circle gauge write

```math
\vartheta=d\theta+A,\qquad F=dA,\qquad X^H=X-A(X)\partial_\theta.
```

For horizontal lifts,

```math
[X^H,Y^H]^V=-F(X,Y)\partial_\theta.
```

Hence horizontal planes are **integrable/holonomic iff $`F=0`$ locally**. The standard Hopf connection has nonzero curvature: its horizontal distribution is **nonholonomic**. The accurate name for the proposed scheme is *Holonomy-Aware Symmetry Reduction*, not holonomic reduction unless integrability is specifically assumed.

For a contractible base loop $`\gamma=\partial\Sigma`$,

```math
\mathrm{Hol}_A(\gamma)=\exp\left(-i\oint_\gamma A\right)=\exp\left(-i\int_\Sigma F\right)
```

under the stated sign convention. Flat connections can still have nontrivial holonomy around noncontractible loops, so curvature alone does not exhaust the connection data.

## 3. Kaluza–Klein metric: the fiber can be reconstructed from enriched base data [D,K]

Fix an oriented Riemannian base $`(B^d,h)`$, principal circle bundle $`P\to B`$, a principal connection $`\vartheta`$ normalized for a $`2\pi`$ fiber and a smooth positive basic fiber radius $`\phi:B\to(0,\infty)`$. Define

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

**Theorem 3.1 [D].** These data determine a globally defined invariant metric on the chosen principal bundle. On overlaps, $`\theta_\beta=\theta_\alpha+\chi_{\alpha\beta}`$ and $`A_\beta=A_\alpha-d\chi_{\alpha\beta}`$ leave $`d\theta+A`$ and the global metric invariant. The resulting metric is uniquely determined by the **specified** enriched data, not by the base metric alone.

## 4. Exact charge-graded Fourier/Laplace reduction theorem [D,K,V]

Locally express the $`n`$-th fiber representation sector as

```math
\Psi_n(b,\theta)=(2\pi)^{-1/2}e^{in\theta}f_n(b),\qquad n\in\mathbb Z,\quad D_i^{(n)}=\partial_i-inA_i.
```

Under the gauge overlap above, the coefficient transforms as $`f_{n,\beta}=e^{-in\chi_{\alpha\beta}}f_{n,\alpha}`$: it is **globally a section of $`L^n`$**.

**Theorem 4.1 [D,K,V] (complete circle Fourier decomposition).** With $`\Delta=\mathrm{div}\nabla`$,

```math
\Delta_{g_P}\Psi_n=(2\pi)^{-1/2}e^{in\theta}\left[\frac1{\phi\sqrt{|h|}}D_i^{(n)}\left(\phi\sqrt{|h|}h^{ij}D_j^{(n)}f_n\right)-\frac{n^2}{\phi^2}f_n\right].
```

The total scalar Hilbert space decomposes unitarily as

```math
L^2(P,d\mathrm{vol}_{g_P})\cong\widehat{\bigoplus}_{n\in\mathbb Z}L^2(B,L^n;\phi\,d\mathrm{vol}_h).
```

Thus the positive total Laplacian restricts on charge $`n`$ to

```math
\mathcal H_n=-\frac1{\phi\sqrt{|h|}}D_i^{(n)}\left(\phi\sqrt{|h|}h^{ij}D_j^{(n)}\right)+\frac{n^2}{\phi^2}.
```

The first term is the weighted **magnetic/Bochner Laplacian**, understood acting on sections; globally natural self-adjoint domains are transported from the complete/compact total Laplacian.

**Proof.** Insert the inverse metric and determinant from §3 into the coordinate Laplace–Beltrami formula. The vertical derivative $`\partial_\theta`$ becomes $`in`$ and horizontal derivatives $`\partial_i-A_i\partial_\theta`$ become $`D_i^{(n)}`$. Orthogonality of Fourier characters and the fiber volume produce the Hilbert direct sum; gauge transition factors glue the operators.

### 4.1 Neutral mode and the half-density

At $`n=0`$, the connection $`A`$ disappears:

```math
\mathcal H_0=-\phi^{-1}\mathrm{div}_h(\phi\nabla_h),\qquad\|\Psi_0\|_{L^2(P)}^2=\int_B|f_0|^2\phi\,d\mathrm{vol}_h.
```

The unitary multiplier $`U_\phi f=\sqrt\phi f`$ maps the neutral weighted space to $`L^2(B,d\mathrm{vol}_h)`$ and gives

```math
U_\phi\mathcal H_0U_\phi^{-1}=-\Delta_h+\frac{\Delta_h\sqrt\phi}{\sqrt\phi}.
```

The same half-density in a charged sector gives the covariant Bochner Laplacian plus the displayed density potential and $`n^2/\phi^2`$. **The scalar invariant reduction remembers the fiber radius as a weight but forgets the connection and its topology.**

## 5. A rigorous counterexample: same invariant operator, different total topology [D,K,C]

On the same round base $`(B,h)=(S^2,g_{\rm round})`$, fix a **constant** fiber radius $`\phi=\ell>0`$. Compare two principal circle bundles:

- $`P_0=S^2\times S^1`$, whose first Chern class is zero and whose connection may be flat.
- $`P_1=S^3\to S^2`$ (Hopf), whose first Chern class is one and whose natural connection has nonzero curvature.

Equip both with the invariant metric of §3 using their respective connections. The total spaces are topologically different, but their neutral scalar Hilbert operators are identical:

```math
\mathcal H_0^{P_0}=\mathcal H_0^{P_1}=-\Delta_{S^2},\qquad \|f_0\|^2=\ell\int_{S^2}|f_0|^2\,dA_h.
```

**Theorem 5.1 [D,K] (non-faithfulness of uncharged reduction).** A reduced invariant SL/Laplace equation together with its **weighted measure and full neutral spectrum** does not determine the total bundle's Chern class, connection, or total topology.

For each $`k\in\mathbb Z`$ there is a principal circle bundle $`P_k\to S^2`$ with $`c_1=k`$; all can carry the *same* base metric and constant radius $`\ell`$ and therefore the **same $`\mathcal H_0`$**. For $`k\ne0`$ their total spaces include lens-space types, whereas $`k=0`$ is the product.

### 5.1 What the charged sectors retain

For the bundle $`P_k`$, the $`n`$-th reduced coefficient is a section of an associated bundle of Chern number

```math
c_1(L^n)=n\,c_1(P_k)=nk.
```

Its covariant derivative contains $`nA`$, and its Bochner Laplacian knows the curvature through commutators

```math
[D_i^{(n)},D_j^{(n)}]=-inF_{ij}.
```

This gives a precise **positive reconstruction statement for the operator decomposition**, not a theorem that *unlabeled eigenvalue sets alone* determine all bundle topology: isospectral or gauge-equivalent situations require careful distinction. The full charge-graded spaces, transition maps and covariant operators carry more information than the neutral scalar spectrum.

## 6. Curvature, Chern class and holonomy are not identical [D,K,C]

On a principal $`U(1)`$ bundle, $`F=dA`$ represents the **real** first Chern class with the chosen sign:

```math
\frac1{2\pi}\int_\Sigma F=\langle c_1(P),[\Sigma]\rangle\in\mathbb Z
```

for a smooth oriented closed base two-cycle $`\Sigma`$. Principal circle bundles over a paracompact base are classified by their **integral** Chern classes in $`H^2(B,\mathbb Z)`$, not just by the de Rham class of $`F`$.

Two independent obstructions to reconstruction from **curvature alone** are:

1. Torsion classes in integral $`H^2(B,\mathbb Z)`$ have zero real image, so de Rham curvature can miss torsion topology.
2. Flat connections can have nontrivial holonomy on noncontractible loops even when $`F=0`$.

The standard full invariant of a circle bundle **with connection** is the corresponding degree-two differential-cohomology/differential-character class: it keeps integral Chern data, curvature and compatible holonomy, and is defined without choosing a global gauge potential $`A`$.

**Theorem 6.1 [K,C].** Base metric $`h`$, radius $`\phi`$ and curvature form $`F`$ do not generally reconstruct a bundle with connection. The enriched data $`(P,\vartheta,h,\phi)`$ do reconstruct the KK metric and its charge-graded scalar Laplacian. One may specify $`(P,\vartheta)`$ equivalently by suitable global differential-cohomology cocycle/holonomy data.

## 7. An elementary FLAT connection with nontrivial global holonomy [D,V]

Take a base circle $`\beta\sim\beta+2\pi`$ of radius $`R_B>0`$, a trivial fiber circle $`\theta\sim\theta+2\pi`$ of radius $`\ell>0`$, and a constant $`\alpha\in\mathbb R`$:

```math
g_P=R_B^2d\beta^2+\ell^2(d\theta+\alpha\,d\beta)^2,\qquad A=\alpha\,d\beta,\quad F=0.
```

Its holonomy around the base loop is

```math
\mathrm{Hol}(\beta\text{-loop})=e^{-2\pi i\alpha}.
```

The exact Laplacian eigenvalues on globally single-valued functions $`e^{ik\beta+in\theta}`$, $`k,n\in\mathbb Z`$, are

```math
-\Delta_{g_P}e^{ik\beta+in\theta}=\left[\frac{(k-n\alpha)^2}{R_B^2}+\frac{n^2}{\ell^2}\right]e^{ik\beta+in\theta}.
```

**Theorem 7.1 [D,V].** The neutral $`n=0`$ spectrum is independent of the *nontrivial flat holonomy* parameter $`\alpha`$, while charged $`n\ne0`$ sectors contain the gauge-covariant shift $`k-n\alpha`$. Shifting $`\alpha\mapsto\alpha+j`$ with $`j\in\mathbb Z`$ produces the same gauge class after relabeling $`k`$.

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

Set the true $`2\pi`$-periodic fiber angle $`\theta=rv`$, and the **base meridian arclength**

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

This is a **weighted one-dimensional SL equation** on the meridian; in $`s`$ the weight and leading coefficient are $`p=w=\phi`$, while in $`u`$ (up to a constant normalization) they are $`p=1`$, $`w=R^2`$.

### 8.1 Curvature is recoverable from the base AND radius, not the neutral connection

For a warped metric $`ds^2+\phi(s)^2d\theta^2`$, its Gaussian curvature is

```math
K_C=-\frac{\phi_{ss}}{\phi}=-\frac{r^2}{(1+r^2s^2)^2}=-r^2S^4.
```

**Theorem 8.1 [D,V].** The reduced catenoid metric data $`(ds^2,\phi(s))`$ reconstruct the entire intrinsic metric and its negative Gaussian curvature, despite the fact that the principal circle connection is **flat** ($`F=0`$) and the total circle bundle is **topologically trivial**.

This is a key warning: intrinsic Levi–Civita Gaussian curvature of a *warped* total surface is **not** the same as curvature $`F`$ of its selected principal circle connection.

### 8.2 Exact catenoid Jacobi reduction

For $`f(u,v)=e^{inrv}h(u)`$, $`n\in\mathbb Z`$, the negative minimal-surface Jacobi operator $`B_C=-(\Delta_C+|A_C|^2)`$, with $`|A_C|^2=2r^2S^4`$, becomes

```math
B_{C,n}h=R^{-2}\left[-h_{uu}+(n^2r^2-2r^2S^2)h\right].
```

Its spectral eigenvalue equation is therefore

```math
-h_{uu}+(n^2r^2-2r^2S^2)h=\lambda_JR^2h.
```

The actual Hilbert weight is $`R^2du`$; multiplying by $`R^2`$ to obtain a Pöschl–Teller **zero** equation is not a unitary operator conjugation. The genuine unitary half-density yields the different SL expression

```math
R B_{C,n}R^{-1}=-\partial_u(S^2\partial_u)+(n^2-1)r^2S^2.
```

This is exactly the existing operator-domain distinction of draft 140, now derived as a **fiber-mode reduction** of the two-dimensional surface geometry.

### 8.3 The original center and resolution are typed

The scale $`r`$ determines neck radius $`1/r`$, angular period $`2\pi/r`$ and curvature profile; the center $`c`$ marks where $`u=\ln(x/c)=0`$. Changing $`c`$ with the *same intrinsic catenoid* changes the multiplicative chart, not its topology. The amplitude $`\mu`$ of the canonical original Symmetrical Function is **not** an independent parameter of this chosen catenoid metric.

## 9. Levi–Civita curvature and teleparallel torsion on the catenoid [D,H,C]

The coframe from draft 180 is

```math
e^1=R\,du,\quad e^2=R\,dv,\qquad T_W^1=0,\quad T_W^2=rSW\,e^1\wedge e^2.
```

Set $`t_2=rSW`$ and $`e_1=S\partial_u`$. Then

```math
K_C=-e_1(t_2)-t_2^2=-r^2S^4.
```

This **frame-dependent teleparallel reconstruction** is compatible with the warped fiber-radius formula $`K_C=-\phi_{ss}/\phi`$. The two computations encode the *same intrinsic surface metric* using different auxiliary data. Neither identifies the Riccati factorization $`-\partial_u^2+h^2-h_u`$ with the Bochner–Weitzenböck tensor identity or the connection curvature $`F=dA`$ of the rotational circle bundle (which is zero here).

**Four distinct connections can coexist on this example:** the nonflat surface tangent Levi–Civita connection, the flat chosen teleparallel frame connection with torsion, the flat rotational bundle connection $`d\theta`$, and the nonflat pullback Hopf connection of the *Gauss map*. Their curvatures, torsions and holonomies must be typed separately.

## 10. The Gauss-map Hopf bundle is NOT the catenoid rotational bundle [D,H,K]

For a meromorphic Gauss map $`g:\Sigma\to\mathbb{CP}^1`$ on a **compactified Riemann surface**, choose the local normalized spinor

```math
\eta_g=\frac{(1,g)}{\sqrt{1+|g|^2}},\qquad A_g=-i\eta_g^\dagger d\eta_g=\frac{\bar g\,dg-g\,d\bar g}{2i(1+|g|^2)}.
```

The curvature and Chern number of this **different circle bundle** are

```math
F_g=dA_g=\frac{i\,dg\wedge d\bar g}{(1+|g|^2)^2}=\frac12g^*\omega_{S^2},\qquad\frac1{2\pi}\int_\Sigma F_g=\deg(g).
```

The local potential must be patched at $`g=\infty`$; it is not a globally defined one-form when the Chern number is nonzero.

The compactified **catenoid Gauss map** $`g_C=-t`$ on $`\mathbb{CP}^1`$ has degree one. The **Riemann minimal-example** Gauss projection from its compactified elliptic curve,

```math
E_R:\quad y_R^2=g_R^3+k_Rg_R^2-g_R,\qquad (g_R,y_R)\mapsto g_R,
```

has degree two. The existing calculation in draft 180 therefore gives

```math
c_1(g_C^*\mathrm{Hopf})=1,\qquad c_1(g_R^*\mathrm{Hopf})=2.
```

**Theorem 10.1 [D,H].** In the corresponding charge-$`n`$ associated bundles, the first Chern numbers are $`n`$ for the catenoid Gauss-map pullback and $`2n`$ for the Riemann Gauss-map pullback. Their **uncharged** scalar sections are topologically trivial, but the charged sectors carry the distinction.

**Essential distinction:** The catenoid rotational fibration $`C\simeq\mathbb R\times S^1\to\mathbb R`$ is **trivial with flat principal circle connection**. The *different* Gauss-map Hopf pullback extends over the compactified conformal sphere with $`c_1=1`$. These can coexist because they are bundles over **different bases** with different projection maps. One cannot infer the Hopf class from the rotational scalar SL equation alone.

## 11. O'Neill curvature is the correct bridge for a Riemannian submersion [D,K]

For the KK metric of §3 with **constant** fiber radius $`\phi=\ell`$, the principal connection's curvature appears in the horizontal O'Neill tensor. For orthonormal horizontal lifts of base orthonormal vectors $`X,Y`$,

```math
\mathsf A_{X^H}Y^H=\frac12[X^H,Y^H]^V=-\frac12F(X,Y)\,\partial_\theta,\quad\|\mathsf A_{X^H}Y^H\|^2=\frac{\ell^2}{4}F(X,Y)^2.
```

The O'Neill sectional-curvature formula is

```math
K_B(X,Y)=K_P(X^H,Y^H)+3\|\mathsf A_{X^H}Y^H\|^2=K_P(X^H,Y^H)+\frac{3\ell^2}{4}F(X,Y)^2.
```

**Theorem 11.1 [D,K].** Under these declared **constant-radius** conditions, the difference between horizontal sectional curvature in the total space and base curvature is an explicit quadratic function of the principal connection curvature $`F`$. This is the correct Riemannian-submersion curvature mechanism. With variable $`\phi`$, additional second-fundamental-form/mean-curvature (O'Neill $`T`$-tensor) terms enter other curvature components: do not extrapolate this formula unmodified.

**Check against catenoid:** Its base is one-dimensional, so there is no horizontal two-plane $`X\wedge Y`$ and no nonzero $`F`$. The catenoid's negative surface curvature is instead the **mixed vertical–horizontal warped curvature** $`-\phi_{ss}/\phi`$ of §8. The two identities describe complementary curvature components rather than competing explanations.

## 12. Marked meromorphic residues and periods are preserved only under DECLARED maps [D,K,C]

Let $`f:\widetilde\Sigma\to\Sigma`$ be a holomorphic map of Riemann surfaces and $`\omega`$ a meromorphic one-form near $`q=f(p)`$. If its local simple pole has residue $`a`$ and $`f`$ has ramification index $`e_p`$ at $`p`$, choose local coordinates $`w=z^{e_p}`$ (up to a nonzero unit). Then

```math
\omega\sim a\,\frac{dw}{w},\qquad f^*\omega\sim e_pa\,\frac{dz}{z},\qquad\mathrm{Res}_p(f^*\omega)=e_p\mathrm{Res}_q\omega.
```

Thus residues are **not literally unchanged by arbitrary projection/pullback**; they scale with local degree. Likewise the period identity is

```math
\int_{\widetilde\gamma}f^*\omega=\int_{f_*\widetilde\gamma}\omega,
```

where the pushforward cycle includes its winding/multiplicity. Real immersion period closing is a condition on the **real parts of the three marked Weierstrass periods**, not on an unspecified scalar holonomy.

### 12.1 Exact special case: framework resolution multiplication

In draft 160, with $`t_r=e^{r\zeta}`$, a resolution change $`r\mapsto Mr`$, $`M\in\mathbb N`$, sends $`t_{Mr}=t_r^M`$. For the marked catenoid logarithmic height differential,

```math
dh_r=\frac1r d\log t_r,\qquad (t\mapsto t^M)^*dh_{Mr}=\frac1{Mr}d\log(t_r^M)=dh_r.
```

The differential is preserved here **because the scale $`1/(Mr)`$ compensates the ramification degree $`M`$**. The source loop winds $`M`$ times around the target puncture. This is an explicit *selected period-preserving pullback*; it does not prove that arbitrary symmetry reductions preserve all holonomies and residues.

## 13. A type-safe distinction among three monodromies [D,C]

The project already uses monodromy in several precise, different ways:

| Mechanism | Path/base | Fiber and operator | Preserved data |
|---|---|---|---|
| Spatial SL carrier | $`u`$ over a selected interval or period, with fixed spectral energy $`E`$ | rank-two solution vectors / $`\mathrm{SL}(2)`$ | Wronskian; transfer matrix |
| Gauss–Manin | path in a modulus space, e.g. $`m_{\rm ell}`$ | marked homology/cohomology of elliptic fibers | intersection pairing / symplectic period determinant |
| Principal Hopf connection | loop on the Gauss sphere or its pullback surface | one-dimensional unitary fiber | Berry/Hopf holonomy, Chern class on closed 2-cycles |
| Euclidean Weierstrass affine integration | loop on punctured surface | translations of $`\mathbb R^3`$ | real immersion period vector |

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

**What this map does NOT assert:** The map $`g_R=g_R(E)`$ is **constant along the SL spatial variable $`u`$ if the spectral point $`E`$ is held fixed**. It therefore does not convert the moving spatial Riccati ratio $`\phi_u/\phi`$ into a Hopf horizontal lift without an additional, explicitly defined moving-spectral-point construction. The curve's holomorphic height form also differs from the normalized spectral second-kind quasimomentum differential in pole divisor.

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

Its Wronskian is constant because $`\mathrm{tr}\mathsf A=0`$. The projective coordinate $`z=y_u/y`$ obeys $`z_u+z^2=V-E`$. A selected positive Gram envelope $`\rho`$ of two independent carrier solutions satisfies an EP equation and a time/clock change

```math
\rho_{uu}+\omega(u)^2\rho=\kappa\rho^{-3},\qquad \tau_u=\rho^{-2}.
```

With $`y=\rho Y(\tau)`$, the linear carrier becomes the constant-coefficient equation

```math
Y_{\tau\tau}+\kappa Y=0,\qquad \omega^2=\kappa(\tau_u)^2+\frac12\{\tau,u\}.
```

This is an exact **gauge and reparametrization** of the rank-two local SL solution system. The phase/current $`\vartheta_u=j/\rho^2`$ with $`j^2=\kappa`$ is a scalar carrier phase, and for periodic $`\rho`$ its increment can encode a Floquet rotation number. Neither the Wronskian nor this phase by itself determines the curvature/Chern class of an independent Hopf circle bundle.

**Theorem 15.1 [D,H] (what the EP lift actually preserves).** The positive EP clock transforms the local real SL solution space, projective Schwarzian and its determinant/Wronskian invariant. Any relation to the **Hopf** Berry connection requires an additional normalized complex spinor, a Hermitian structure, and a specified map of base paths. None is automatically supplied by the scalar EP amplitude.

## 16. NEW EXACT LIFT: the canonical weighted Master SL carrier is the neutral sector of a hyperbolic cylinder [D,V]

There is a particularly strong, simple application of Theorem 4.1 to the original framework, distinct from the catenoid metric.

Recall the **original linear carrier** and weighted Hilbert space:

```math
\mathcal L_xf=-\frac1x(x^3f_x)_x+(r^2-1)f,\qquad \mathcal H_x=L^2((0,\infty),x\,dx).
```

Keep $`u=\ln(x/c)`$ and choose a **specific two-dimensional geometric lift**, with $`2\pi`$-periodic angle $`\theta`$ and strictly positive circle radius

```math
\phi_{\rm hyp}(u)=x^2=c^2e^{2u},\qquad g_{\rm hyp}=du^2+\phi_{\rm hyp}(u)^2d\theta^2=du^2+c^4e^{4u}d\theta^2.
```

This is a globally smooth metric on the cylinder $`\mathbb R_u\times S^1_\theta`$ (with fixed choice of dimensionless metric units). The principal rotational circle connection is trivial, $`A=0`$.

**Theorem 16.1 [D,V] (canonical weighted SL as hyperbolic neutral reduction).** On functions invariant under $`\theta`$, the lifted Laplacian and its natural measure satisfy

```math
\Delta_{\rm hyp}^{(0)}=\partial_u^2+2\partial_u,\qquad\phi_{\rm hyp}\,du=x^2du=x\,dx.
```

The original carrier is **exactly**

```math
\mathcal L_x=-\Delta_{\rm hyp}^{(0)}+(r^2-1)
```

on the identified neutral Hilbert space. Multiplication by the positive half-density $`\sqrt{\phi_{\rm hyp}}=x`$ is precisely the **canonical** Liouville unitary and gives

```math
U_c\mathcal L_xU_c^{-1}=-\partial_u^2+r^2,\qquad U_cf(u)=xf(ce^u).
```

**Proof.** The circle-volume factor gives $`\Delta^{(0)}=\phi^{-1}\partial_u(\phi\partial_u)`$, and $`\phi_u/\phi=2`$. The volume identity is $`x\,dx=x^2du`$. The conjugation can be checked by substituting $`f=\psi/x`$.

### 16.1 Exact constant negative Gaussian curvature

For any warped surface $`g=du^2+\phi(u)^2d\theta^2`$, $`K=-\phi_{uu}/\phi`$. Here

```math
K_{\rm hyp}=-\frac{\partial_u^2(c^2e^{2u})}{c^2e^{2u}}=-4.
```

To see completeness and the hyperbolic geometry explicitly, set

```math
y=e^{-2u}>0,\qquad z=2c^2\theta,\qquad g_{\rm hyp}=\frac{dy^2+dz^2}{4y^2},\quad z\sim z+4\pi c^2.
```

This is the constant-curvature-$`-4`$ upper-half-plane metric modulo a parabolic translation; it is complete and has a shrinking horocyclic circle end as $`u\to-\infty`$.

**Structural significance.** The canonical **one-dimensional weighted metric** $`du^2`$ is intrinsically flat, yet the neutral SL equation is exactly the invariant reduction of this **specified two-dimensional hyperbolic metric**. The negative curvature is encoded by the retained fiber radius $`\phi=x^2`$; it is invisible if one retains only the Liouville-conjugated free operator and throws away the positive half-density.

**Nonuniqueness caveat [C].** This does not imply the hyperbolic cylinder is the **unique** higher-dimensional geometry generating the original SL equation. Other choices of fiber, metric, density and extra potential can produce the same neutral scalar differential expression. The exact lift gives a constructive existence theorem, not a unique inverse-geometric reconstruction.

## 17. Charged modes of the same exact lift produce a Bessel/Mellin spectral hierarchy [D,V,K]

Retain all angular charges $`n\in\mathbb Z`$ in the hyperbolic metric of §16, still with the same scalar shift $`(r^2-1)`$. The full geometric operator is

```math
\mathscr L_{\rm hyp}=-\Delta_{g_{\rm hyp}}+(r^2-1).
```

On the $`n`$-th normalized angular mode its weighted one-dimensional expression is

```math
\mathscr L_{\rm hyp}^{(n)}=-\partial_u^2-2\partial_u+(r^2-1)+\frac{n^2}{c^4e^{4u}}.
```

After **the same unitary multiplier $`x`$ as for the original weighted SL**, every charged mode becomes

```math
U_c\mathscr L_{\rm hyp}^{(n)}U_c^{-1}=-\partial_u^2+r^2+\frac{n^2}{c^4e^{4u}}=-\partial_u^2+r^2+\frac{n^2}{x^4}.
```

This is a one-dimensional **exponential-wall Schrödinger operator**. It is not the reflectionless Pöschl–Teller potential of draft 140; it is a different exact spectral realization emerging from the same underlying weighted metric.

### 17.1 Exact modified-Bessel eigenfunctions

For nonzero $`n`$, set

```math
t=\frac{|n|}{2c^2}e^{-2u}=\frac{|n|}{2x^2},\qquad \lambda=r^2+k^2,\qquad k>0,\qquad \kappa=k/2.
```

Then the spectral equation becomes

```math
t^2\psi_{tt}+t\psi_t+(\kappa^2-t^2)\psi=0.
```

Its solution exponentially decaying toward the high exponential wall ($`u\to-\infty`$, $`t\to\infty`$) is the **modified Bessel/Macdonald function**

```math
\psi_{n,k}(u)=K_{i k/2}\left(\frac{|n|}{2c^2}e^{-2u}\right).
```

**Theorem 17.1 [D,V] (exact charged generalized eigenfunction).** Each charged sector has a complete modified-Bessel scattering basis (in generalized-eigenfunction sense) with continuum threshold $`\lambda=r^2`$, under the natural self-adjoint realization. The neutral sector $`n=0`$ instead has free Fourier characters $`e^{iku}`$: both arise from the **same 2D hyperbolic Laplacian**, separated by their circle representation charge.

### 17.2 Exact unit-modulus reflection coefficient

For $`k>0`$ the small-$`t`$ expansion of $`K_{i\kappa}(t)`$ is

```math
K_{i\kappa}(t)\sim\frac12\Gamma(i\kappa)(t/2)^{-i\kappa}+\frac12\Gamma(-i\kappa)(t/2)^{i\kappa}.
```

At $`u\to+\infty`$, where $`t/2=(|n|/(4c^2))e^{-2u}`$, the two terms are respectively outgoing $`e^{+iku}`$ and incident $`e^{-iku}`$ waves. Hence

```math
\mathcal R_n(k)=\frac{\Gamma(ik/2)}{\Gamma(-ik/2)}\left(\frac{|n|}{4c^2}\right)^{-ik},\qquad|\mathcal R_n(k)|=1.
```

This is **total reflection from an exponential wall**, not Pöschl–Teller reflectionlessness, which has zero reflection coefficient and nontrivial transmission. The $`c`$ dependence is a phase shift tied to the chosen logarithmic origin/metric scaling, not a claim that the intrinsic topological class depends on $`c`$.

### 17.3 The spectral Plancherel transform becomes Kontorovich–Lebedev

Let $`F(t)=\psi(u(t))`$ and form the classical Kontorovich–Lebedev transform

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

Since $`|du|=dt/(2t)`$, the original flat logarithmic Hilbert norm is

```math
\int_{\mathbb R}|\psi(u)|^2du=\frac1{\pi^2}\int_0^\infty\kappa\sinh(\pi\kappa)|\widehat F(\kappa)|^2d\kappa.
```

**New exact synthesis:** The same canonical weighted space $`L^2(x\,dx)`$ can be realized geometrically so that **neutral modes use Fourier–Mellin Plancherel** and **charged modes use Kontorovich–Lebedev Plancherel**. The difference is a rigorous consequence of retaining, rather than discarding, the circle fiber representations. See NIST DLMF §10.43 and the classical Kontorovich–Lebedev inversion theory; the spectral transform formula requires its standard $`L^2`$ interpretation and generalized eigenfunction domains.

## 18. General weighted Sturm–Liouville as an orbit-space operator [D,K]

The original §4 is not restricted to a circle of constant radius. For a one-dimensional base with arclength $`s`$ and positive fiber volume density $`\phi(s)`$, the neutral quotient of the Laplace–Beltrami operator is

```math
-\Delta_P^{(0)}=-\phi^{-1}\partial_s(\phi\partial_s).
```

This is a Sturm–Liouville differential expression with $`p(s)=w(s)=\phi(s)`$. In an arbitrary chart $`b`$ with base metric $`h_{bb}(b)>0`$, the corresponding coefficients are

```math
p(b)=\frac{\phi(b)}{\sqrt{h_{bb}(b)}},\qquad w(b)=\phi(b)\sqrt{h_{bb}(b)}.
```

Consequently

```math
\frac{w}{p}=h_{bb},\qquad \sqrt{pw}=\phi.
```

**Theorem 18.1 [D] (weighted SL data as metric and orbit-volume data).** Every scalar SL principal part with positive $`p,w`$ has a local realization as the neutral reduction of a circle metric with

```math
h_{bb}=\frac wp,\qquad\phi=\sqrt{pw},\qquad g_P=\frac wp\,db^2+pw\,d\theta^2.
```

Its fiber-integrated measure is exactly $`w\,db`$, and the corresponding neutral Laplacian is $`w^{-1}\partial_b(p\partial_b)`$. An arbitrary scalar potential $`q_0/w`$ may be **independently added** as a basic potential on the total space.

**Proof.** The circle-volume radius is $`\phi=\sqrt{pw}`$. The total volume density in the chart is $`\phi\sqrt{h_{bb}}=w`$, while $`g_P^{bb}=p/w`$. The scalar divergence formula gives $`w^{-1}\partial_b(p\partial_b)`$.

**A precise limitation on uniqueness:** A principal circle connection with a nonzero gauge field, a different fiber topology (when allowed by the base), or another higher-dimensional fiber can share this **same neutral SL operator**. The construction establishes the existence of an exact geometric **lift**, not that a one-dimensional ODE remembers its unique transverse manifold.

### 18.1 Reconstructing the canonical lift directly from p and w

With $`p=x^3`$ and $`w=x`$ from the original framework,

```math
h_{xx}=\frac1{x^2},\quad \phi(x)=x^2,\quad g_P=\frac{dx^2}{x^2}+x^4d\theta^2.
```

Put $`u=\ln(x/c)`$ to recover **precisely** the constant-curvature hyperbolic metric of §16. Its curvature is $`-4`$, while the original Liouville-invariant one-dimensional metric has zero curvature. The extra curvature is generated by the *retained transverse volume function* $`\phi=x^2`$.

### 18.2 A useful contrast with the catenoid lift

The catenoid is likewise a circle-warped metric, but its geometric base and fiber radius are

```math
g_C=ds^2+\phi_C(s)^2d\theta^2,\qquad\phi_C(s)=\frac1r\sqrt{1+r^2s^2}.
```

The canonical weighted SL hyperbolic lift has instead $`\phi_{\rm hyp}=c^2e^{2u}`$ and $`K=-4`$. Their neutral weighted operators are **different** unless an additional nontrivial change of coordinates/weights and potential is supplied. Shared circle structure and use of the same logarithmic coordinate do not make the two surfaces isometric.

## 19. The Weierstrass immersion is a different flat AFFINE holonomy [D,H]

On a punctured Riemann surface $`\Sigma^\circ`$, a meromorphic Weierstrass triple $`\boldsymbol\Phi=(\Phi_1,\Phi_2,\Phi_3)`$ satisfies

```math
\Phi_1^2+\Phi_2^2+\Phi_3^2=0,\qquad d\Phi_j=0\ \text{away from punctures}.
```

The immersion on the universal cover is

```math
X(p)=X(p_0)+\mathrm{Re}\int_{p_0}^p\boldsymbol\Phi.
```

Its **flat translation holonomy** along a closed cycle $`\gamma`$ is

```math
T_{\rm WE}(\gamma)=\mathrm{Re}\oint_\gamma\boldsymbol\Phi\in\mathbb R^3.
```

This is a legitimate form of **affine parallel transport**, not the Levi–Civita transport of tangent vectors or the Hopf circle-bundle holonomy. A global Euclidean immersion closes only if all required real periods vanish; immersion into a chosen translation quotient permits periods in its specified lattice.

### 19.1 The catenoid/helicoid real-period test

The nodal spectral-normalization construction of drafts 160–170 supplies catenoid data

```math
t=\frac{s-r}{s+r},\qquad g_C=-t,\qquad dh_C=\frac1r\,d\log t.
```

The Weierstrass vector has period $`(0,0,2\pi i/r)`$, so its **real** translation vanishes. A Bonnet/associate rotation $`e^{i\delta}`$ changes it to

```math
\mathrm{Re}\oint e^{i\delta}\boldsymbol\Phi_C=(0,0,-2\pi\sin\delta/r).
```

Thus the catenoid closes on the punctured-plane conformal quotient while the conjugate helicoid at $`\delta=\pi/2`$ requires its angular universal cover (or a vertical translation quotient). The Hopf curvature determined by the unchanged Gauss map does **not** change with the Bonnet angle.

### 19.2 Why minimal-surface period descent needs all three forms

The Riemann minimal-example elliptic curve of the archive has a degree-two Gauss map and independent marked holomorphic and meromorphic differentials. The explicit Lamé–Riemann elliptic isomorphism of draft 170 pulls back the **full Weierstrass triple**, but equality of the underlying smooth elliptic curves alone would not imply its period-closing equations. Different decorations of the same curve, or different choices of cycles, may have different real translation vectors.

## 20. Sato–Krichever BA transport and the base/fiber analogy [H,K,C]

The archived Sato rank-one construction H136 supplies a one-soliton tau, a Baker eigenfunction, an integer PT differential operator, and a nodal spectral normalization with gluing data. Smooth finite-gap/Krichever theory requires **decorated** input

```math
(\Gamma,P_\infty,\text{local coordinate},\text{line bundle/divisor},\text{normalization},\text{hierarchy times}).
```

The Baker–Akhiezer function evolves along the chosen hierarchy/space variables at a **fixed spectral point**. The Gauss–Manin connection transports marked periods as a **modulus changes**, and the Weierstrass Gauss map assigns a geometric coordinate to a chosen point of a spectral curve. These are again different parameter directions.

The analogy with the KK theorem is mathematically useful: the **bare curve** is insufficient; extra *line bundle/divisor, connection and period markings* retain information that a coarse projection forgets. But this is an analogy between two categories of enriched data. It is **not** a proof that a Baker–Akhiezer solution is already a Hopf-horizontal spinor, or that a Grassmannian tau is itself a metric on the surface.

A stronger proposed reconstruction theorem must explicitly construct a functor from **decorated spectral curves and BA line bundles** to the geometric Gauss-map Hopf bundle and prove that it intertwines connections and holonomies. This remains open.

## 21. The conditional HOLONOMY-AWARE REDUCTION AND RECONSTRUCTION THEOREM [D,K]

**Theorem 21.1 (exact circle-bundle spectral reduction/reconstruction).** Let $`\pi:P\to B`$ be a specified smooth principal $`U(1)`$ bundle, let $`h`$ be a smooth base Riemannian metric, $`\phi:B\to(0,\infty)`$ a basic radius, and $`\vartheta`$ a principal connection. Give $`P`$ the KK metric $`g_P=\pi^*h+\phi^2\vartheta^2`$ and choose the scalar Laplacian's natural self-adjoint realization (e.g. a compact complete boundaryless total space; for other cases transport the declared domains).

1. **Exact projection:** The $`U(1)`$-invariant scalar sector is unitarily identified with the weighted base space $`L^2(B,\phi\,d\mathrm{vol}_h)`$, with reduced operator $`-\phi^{-1}\mathrm{div}_h(\phi\nabla_h)`$. The fiber radius survives as a weight.
2. **Exact charged decomposition:** The full scalar $`L^2(P)`$ is the orthogonal direct sum over charges $`n\in\mathbb Z`$ of associated line-bundle sections. The reduced operators are the charge-$`n`$ weighted Bochner Laplacians plus vertical energy $`n^2/\phi^2`$ (Theorem 4.1).
3. **Curvature/topology retention:** In the charged sectors, the covariant derivatives have curvature $`-inF`$ and the associated Chern classes are $`n\,c_1(P)`$. Complete bundle-with-connection data, equivalently the appropriate differential-cohomology class, reconstruct the KK metric and this whole operator family up to the specified bundle/gauge equivalence.
4. **Limits of bare reduction:** The *neutral operator*, even together with its weighted measure and complete neutral spectrum, need not determine $`c_1(P)`$, flat holonomy, or total topology. The trivial/Hopf example is an explicit counterexample.
5. **Geometric SL realization:** A positive one-dimensional SL principal part admits a **selected** circle-warped lift with $`h_{xx}=w/p`$ and $`\phi=\sqrt{pw}`$ (Theorem 18.1), but that lift is not unique and does not automatically reproduce arbitrary geometric PDE potentials or boundary conditions.
6. **Additional transport:** Preserving residues, Gauss–Manin matrices, Hopf phases, spectral monodromy or Weierstrass periods requires separately specified morphisms of the appropriate punctured curves, bundles, connections, cycles and domains. These invariants do not survive an arbitrary scalar quotient automatically.

**Proof.** The metric reconstruction is §3, the explicit scalar Fourier/Laplacian and Hilbert decomposition is §4, the counterexample is §5, the circle-bundle classification and holonomy qualifications are §§6–7, the warped SL lift is §§8/16/18, and the nonidentities and selected period maps are §§9–15 and §§19–20. All global analytic self-adjointness claims depend on the specified complete/compact domain or transported boundary realization.

**Interpretation:** The theorem supplies a **mathematically exact prototype** for the proposed research thesis. Calling it *holography* is optional terminology; the demonstrated mechanism is representation-graded **Kaluza–Klein reduction and reconstruction**, not the claim that a lower-dimensional scalar field alone contains all information about its higher-dimensional total space. The apparently reduced description retains an **infinite tower** of charges and bundle gluing data—information has been reorganized, not magically compressed to one scalar degree of freedom.

## 22. What the word holography can and cannot mean here [C,O]

There are three levels of statement:

**(A) Proven differential geometry [D,K]:** For a principal circle bundle with a declared KK metric, fiber integration creates a weighted base Laplacian, and full equivariant Fourier decomposition gives covariant operators on associated bundles. Holonomy and Chern topology occur as data in the base-bundle connection and its charged sectors.

**(B) Constructive framework dictionary [D,H]:** The canonical $`u=\ln(x/c)`$ weighted SL expression has a particular complete hyperbolic circle lift (§16); the catenoid has a different exact circle lift (§8); the Hopf Gauss-map pullbacks have integer Chern degrees (§10); selected SL–EP, Lamé–Riemann, and Weierstrass maps preserve their declared projective, meromorphic and period data. These are individual rigorous arrows, not a single universal isomorphism.

**(C) Exploratory program [O]:** “Fibration Holography” could ask whether an appropriately enriched collection of reduced differential operators and marked monodromy/holonomy data yields a **faithful and computationally useful inverse reconstruction functor** for a wider class of curved, singular, soliton-bearing, or nonabelian fibered spaces. No such general theorem is established here. In particular, neither the phrase “base = boundary” nor “all reductions preserve topology” follows from the examples.

A more mathematically precise subtitle is: **A program in connection-aware spectral reduction, bundle reconstruction and marked period transport.**

## 23. Independent calculations, provenance and verification limitations

### 23.1 Calculations explicitly checked

1. **Bundle Laplacian:** the inverse block matrix of $`h+\phi^2(d\theta+A)^2`$, determinant $`\phi^2\det h`$, and the full charge-$`n`$ local divergence formula were independently expanded. The gauge overlap $`A_\beta=A_\alpha-d\chi`$, $`f_\beta=e^{-in\chi}f_\alpha`$ preserves $`D^{(n)}f`$.
2. **Weighted measure and half-density:** fiber integration gives $`\phi\,d\mathrm{vol}_h`$ and the exact neutral conjugation $`-\Delta_h+(\Delta_h\sqrt\phi)/\sqrt\phi`$.
3. **Trivial versus Hopf:** the neutral scalar operators on $`S^2`$ are identical for the same $`h`$ and constant $`\ell`$, while $`c_1=0`$ versus $`1`$ is different.
4. **Flat connection:** for the torus metric $`R_B^2d\beta^2+\ell^2(d\theta+\alpha d\beta)^2`$ the direct eigenvalue formula is $`(k-n\alpha)^2/R_B^2+n^2/\ell^2`$, with flat $`F=0`$ and a generally nontrivial global holonomy.
5. **Catenoid warped metric:** exact change $`s=\sinh(ru)/r`$ yields $`\phi_C=\sqrt{1+r^2s^2}/r`$. Differentiation gives $`K_C=-\phi_{ss}/\phi=-r^2S^4`$, matching draft 180 teleparallel curvature and the known Gauss equation.
6. **Catenoid Jacobi:** separating angular Fourier modes produces the weighted SL equation with $`w=R^2`$ and the unitary-conjugate variable-leading-coefficient operator of draft 140.
7. **Gauss-map Hopf topology:** the local Hopf connection differentiates to half the pullback round area form, with Chern degree equal to the meromorphic Gauss map degree. The catenoid compactified map has degree one; the Riemann elliptic map has degree two.
8. **O'Neill horizontal curvature:** for constant $`\ell`$, the vertical component of the horizontal bracket is $`-F(X,Y)\partial_\theta`$, with squared norm $`\ell^2F(X,Y)^2`$; the factor $`3/4`$ follows from the horizontal O'Neill tensor.
9. **Residue pullbacks:** the substitution $`w=z^e`$ gives $`f^*(a\,dw/w)=ea\,dz/z`$. The exact resolution-multiplication case has compensating height scale $`1/(Mr)`$.
10. **Canonical weighted SL lift:** the formula $`h_{xx}=w/p=x^{-2}`$ and $`\phi=\sqrt{pw}=x^2`$ yields $`g=dx^2/x^2+x^4d\theta^2`$. Its invariant divergence is $`-x^{-1}(x^3\partial_x)_x`$ and its fiber-integrated volume is exactly $`x\,dx`$.
11. **Hyperbolic curvature and completeness:** $`g=du^2+c^4e^{4u}d\theta^2`$ transforms to $`(dy^2+dz^2)/(4y^2)`$ with $`y=e^{-2u}`$ and $`z=2c^2\theta`$; this is a complete hyperbolic horocyclic quotient of curvature $`-4`$.
12. **Charged hyperbolic modes:** conjugation by $`x`$ produces the wall $`n^2/x^4`$. With $`t=|n|/(2x^2)`$, exact differentiation gives the modified Bessel equation of order $`ik/2`$. Numerical second differentiation of $`K_{ik/2}(t(u))`$ at $`(r,c,n,k)=(1.7,1.4,2,1.15)`$ gave an ODE residual of about $`1.6\times10^{-16}`$, limited by numerical differentiation, and the gamma-function reflection amplitude had modulus $`1`$.
13. **Kontorovich–Lebedev spectral measure:** the standard inversion/Plancherel formula in $`dt/t`$ was transported via $`|du|=dt/(2t)`$; the resulting factor $`1/\pi^2`$ is therefore exact. It applies to nonzero charged modes on their standard generalized-eigenfunction domains.
14. **Spectral curve map:** the Lamé–Riemann affine curve formula and its differential scaling are inherited from audited draft 170, not a new assertion of Hopf gauge equivalence. Spatial SL transport fixes $`E`$, whereas using $`E`$ as a moving surface coordinate is an additional parametrization.
15. **Global limitations:** none of the checks yields an arbitrary nonabelian inverse spectral uniqueness theorem, identifies the total bundle with a topological boundary, or guarantees preservation of untyped spectral/holonomy data under quotienting.

### 23.2 Historical-project provenance

- The November 18 ZIP ARCHITECTURE.md already describes the **Hopf fibration** as a later lift and explicitly marks it as not entering any foundational theorem then (O103). The present conditional bundle-reduction theorem does not retroactively certify older speculative Hopf identifications.
- Drafts 130/140 build the weighted Hilbert SL–EP/Darboux spectral bridge; draft 150 adds inverse norming; draft 160 proves the marked nodal spectral normalization to catenoid height, helicoid associate real period and elliptic Pinney-to-Riemann isogeny.
- Draft 170 proves the **selected** real smooth Lamé–Riemann elliptic curve map with marked differential and Gauss–Manin period gauge. Draft 180 distinguishes LC, teleparallel, spatial SL, Hopf and affine Weierstrass connections, and gives the degree-one/degree-two Gauss-map Chern calculation.
- The actual archived Sato Grassmannian module H136 contains the chosen rank-one point, Baker eigenfunction and KdV two-reduction. It does **not** prove a universal fibration or inverse-holography theorem.

### 23.3 Independent external references and precise roles

- J. Jung and S. Zelditch, *Boundedness of the Number of Nodal Domains for Eigenfunctions of Generic Kaluza–Klein 3-Folds*, Ann. Inst. Fourier 70 (2020), 971–1026: KK bundle metric, charge decomposition into associated line bundles and Bochner Laplacians. https://www.numdam.org/item/10.5802/aif.3329.pdf .
- C. Gordon, H. Ouyang and D. Schueth, *Distinguishing Isospectral Nilmanifolds by Bundle Laplacians*, Mathematical Research Letters **4** (1997), 23–33: identification of bundle sections with equivariant functions and horizontal Laplacian. https://intlpress.com/api/bgcloud-front/resource/pdf/volume/1806607262670024706-1806607262670024706-7f3867527eeef78c7c1291f1280fee3a.pdf .
- Principal $`U(1)`$ bundles and integral first Chern classification: https://ncatlab.org/nlab/show/principal%20U%281%29-bundle .
- Bundles with connection and differential cohomology: https://www.mdpi.com/2075-1680/13/1/60 and https://ncatlab.org/nlab/show/ordinary%2Bdifferential%2Bcohomology .
- O'Neill's Riemannian submersion curvature formula and the horizontal distribution: https://link.springer.com/article/10.1365/s13291-020-00225-x .
- NIST DLMF §10.43, Kontorovich–Lebedev transform: https://dlmf.nist.gov/10.43 ; related distributional orthogonality for $`K_{i\tau}`$: https://www.opuscula.agh.edu.pl/om-vol26iss1art12 .
- Historical project references cited above supply the framework-specific catenoid, SL/EP, Sato, Lamé/Riemann and Weierstrass-period formulas.

## 24. Next questions for a mathematically ambitious research program [O]

1. **Inverse faithfulness:** Characterize which classes of principal $`U(1)`$ KK metrics and connections are determined by their **entire charge-labeled covariant operator family** (not merely the spectra). Require an explicit equivalence notion including unitary intertwiners and compatibility with charge multiplication.
2. **Full spectral tower of the canonical hyperbolic lift:** Normalize the neutral Fourier–Mellin and charged Kontorovich–Lebedev kernels into a single spectral resolution of $`\mathscr L_{\rm hyp}`$, with the exact total $`L^2`$ measure and direct-sum Plancherel theorem.
3. **Riccati and EP for charged modes:** Calculate the Milne/Pinney squared eigenfunction for the modified-Bessel exponential-wall sector and its scattering phase; compare with the reflectionless PT Pinney family of draft 140, without equating their Hilbert operators.
4. **Conformal/warp classification:** Determine all smooth positive fiber-radius functions $`\phi(s)`$ giving constant Gauss curvature $`K_0`$ on a circle-warped cylinder; classify their induced neutral SL potentials after Liouville conjugation. The canonical $`\phi=x^2`$ is a single $`K_0=-4`$ example, while the catenoid has variable negative curvature.
5. **Nonabelian extension:** Prove the corresponding Peter–Weyl/associated-vector-bundle decomposition for a compact group $`G`$ under a chosen connection metric, retaining irreducible representation labels, vertical Casimir, global cocycles and appropriate operator domains.
6. **Spinorial Hopf lift:** Construct and explicitly compare a Hermitian eigenvector connection on the **selected** Lamé Baker–Akhiezer line bundle and the pullback Hopf connection of the Riemann Gauss map. State the topological obstruction (including their degree/first Chern class) before attempting a connection-preserving isomorphism.
7. **Riemann minimal example as a fibered surface:** Identify its actual circle or other group actions, when present, and test whether an SL reduction exists. Do not assume a smooth elliptic conformal domain implies an axial Killing field or a circle fibration with separable Jacobi operator.
8. **Residue and period functoriality:** Track the exact ramification indices, homology pushforwards, and real-period closing equations for the Lamé-to-nodal and resolution-multiplication maps of drafts 160–170.
9. **Curvature decomposition:** On a selected KK bundle compute the LC connection, teleparallel coframe (where globally available), torsion/contortion and O'Neill tensors, and compare *their actual formulas* with the reduced Riccati superpotential; reject any identification that lacks a defined connection map.
10. **Topological reconstruction through charged cohomology:** Test whether twisted de Rham complexes, not just scalar charged Laplacians, preserve additional fiber cohomology and monodromy, using the Gysin sequence for circle bundles.
11. **Boundary versus base:** If a genuinely holographic boundary statement is desired, define an actual boundary or asymptotic end, a boundary-to-interior operator (e.g. Dirichlet-to-Neumann or scattering map), and an inverse uniqueness theorem; do not rebrand a fiber quotient as a boundary by definition.
12. **The explicit constant-curvature lift as a testbed:** Compare the canonical hyperbolic cylinder's charged and neutral spectra, its cusp spectral theory, and the separately constructed catenoid Jacobi operator, keeping the center $`c`$, resolution $`r`$ and any choice of angular fiber scale visible in every transform.

**Final status.** The exact theorem established here is **holonomy-aware circle-bundle reduction and reconstruction with explicitly retained charge-graded data**. The framework's weighted SL calculus, hyperbolic neutral lift, catenoid warp, Hopf Chern calculations and selected elliptic Weierstrass pullbacks are concrete, independently typed examples. A broader *fibration holography* program is a worthwhile mathematical question, but its general inverse-reconstruction claims remain open; the base alone or a single invariant ODE does not determine all transverse topology, holonomy or periods.
