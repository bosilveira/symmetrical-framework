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
