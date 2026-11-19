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
