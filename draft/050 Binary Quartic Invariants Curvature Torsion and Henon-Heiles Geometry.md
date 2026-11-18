---
id: SF-DRAFT-050
title: Binary Quartic Invariants, Curvature, Torsion, and Henon-Heiles Geometry
status: provisional
created: 2026-11-18
proposed_layers: [I, II, III]
depends_on: [SF-I-000, SF-I-010, SF-I-020, SF-DRAFT-010, SF-DRAFT-020, SF-DRAFT-030, SF-DRAFT-040]
related_claims: [H312, H313, H314, H352, H353, H354, H403, H404, H405, H406, H408, H409, H410, H411, H412, H414, H421, H424]
---

# 050 Binary Quartic Invariants, Curvature, Torsion, and Henon-Heiles Geometry

**Status:** Provisional foundational investigation. It is not a new physical model and does not confer verified or novel theorem status on the wider program. Evidence labels distinguish derivations [D], independent symbolic verification [V], established mathematics [K], archived project claims with their original scope [H], corrected or disproved proposed assertions [C], and open or conditional extensions [O].

**Research question:** How do binary quartic invariants I and J, modular elliptic curves, Hénon–Heiles systems, Levi-Civita curvature and Weitzenbock torsion meet? Is there a mathematically precise mechanism behind these connections, and which similarities arise only because several different mathematical objects belong to the same representation space?

**Main conclusion:** There are **three sharply different quartics** and an additional optional Cartan quartic:
1. A **surface fundamental-form quartic**, constructed from the first and second fundamental forms, whose I and J depend explicitly on mean curvature H and Gaussian curvature K. The catenoid/helicoid give the smooth harmonic case J=0, j=1728.
2. An **energy/spectral quartic** from the nonlinear Master and the archived Hénon–Heiles quartic pencil, with generally nonzero I, J, discriminant and elliptic modulus. The archived H403 equivalence is an exact projective algebraic identity, not identity of all mechanical Hamiltonians.
3. A **Weyl-spinor/Petrov quartic** of a four-dimensional Lorentzian metric. The standard Eisenhart–Duval lift of any scalar-potential two-degree-of-freedom mechanical system is a Brinkmann pp-wave with Weyl quartic Petrov type N (or O), so its Weyl I and J vanish **for all potentials**, including generic integrable and nonintegrable Hénon–Heiles systems. A preferred flat metric-compatible Weitzenbock connection on the same lift has torsion determined by the potential gradient but vanishing *quadratic torsion scalar*. Levi-Civita curvature recovers the potential Hessian from contorsion derivatives.
4. The Cartan harmonic binary quartic of a (2,3,5)-distribution is a fourth *possible* representation-theoretic construction only if such a distribution is explicitly supplied. It does not automatically coincide with the Weyl or energy quartic.

**Evidence base:** Current GitHub main branch SF-I-000/010/020 and drafts SF-DRAFT-010/020/030/040. Uploaded ZIP symmetrical-framework-update-2026-11-18-bu.zip: 04-follow-ups/binary-quartic-and-spectral-curves.md, binary-quartic-pencils.md, binary-quartics-hessian-hh-s4.md, fundamental-forms-willmore-hopf.md, friedmann-reciprocal-envelope.md, 00-meta/CLAIMS.md and verification modules binpencil.py, quartic2.py, fundforms.py, friedmann.py. Relevant archival IDs include H352–H358, H403–H410, H421 and H424. The attached Pasted text(20261118-174925).txt provides exploratory suggestions; its asserted automatic identities between curvature, torsion, the different I/J quartics, and mechanical integrability are tested here rather than assumed. External literature is given in §21.

## 1. Canonical variables, symbols and type distinctions

For the original framework keep independent $`x,c,r,\mu>0`$ and

```math
u=\ln(x/c),\qquad x=ce^u,\qquad \theta=ru,\qquad S=\mathrm{sech}(ru),\qquad W=\tanh(ru),\qquad R=\cosh(ru).
```

The canonical function and cubic Master field are

```math
f_\mu=\frac{S}{2\sqrt{\mu}\,x},\qquad y=2xf_\mu,\qquad y_{uu}=r^2y-2\mu r^2y^3.
```

Write $`\varepsilon_N`$ for the nonlinear first integral and $`e=\mu\varepsilon_N/r^2`$ for normalized energy. The corresponding energy quartic has coordinate $`z=\sqrt{\mu}\,y`$, so

```math
z_u^2=r^2(e+z^2-z^4).
```

For Hénon–Heiles mechanical dynamics use **different** configuration coordinates $`q_1,q_2`$ and mechanical time $`t`$; do not identify those with $`x`$ or $`u`$ unless a map and clock conversion are specified. Use $`s`$ as the extra null coordinate of the Eisenhart lift. The geometric height/energy parameter will be called $`\mathcal E`$ to avoid conflation with $`e`$.

Distinct scalar families are denoted $`I_{\mathrm{alg}},J_{\mathrm{alg}}`$ for a projective binary quartic, $`I_{\mathrm W},J_{\mathrm W}`$ for a Weyl spinor, $`H_m,K_G`$ for surface mean/Gaussian curvature, and $`\mathcal T`$ for a torsion tensor. Neither $`J`$ (a cubic quartic invariant) nor $`j`$ (a weight-zero elliptic modulus) is the framework's reciprocal $`J=1/y`$; that scalar will be written $`J_{\rm env}`$ if needed.

## 2. Binary quartic algebra and the two normalization systems [D,V,K]

Let

```math
F(X,Z)=aX^4+bX^3Z+c_2X^2Z^2+dXZ^3+fZ^4.
```

The historical ZIP uses the **raw unweighted** classical invariants

```math
I_{\rm raw}=12af-3bd+c_2^2,\qquad J_{\rm raw}=72ac_2f+9bc_2d-27ad^2-27fb^2-2c_2^3.
```

Its standard polynomial discriminant and smooth elliptic modulus are

```math
\Delta_F=\frac{4I_{\rm raw}^3-J_{\rm raw}^2}{27},\qquad j_F=\frac{256I_{\rm raw}^3}{\Delta_F}=\frac{1728\cdot4I_{\rm raw}^3}{4I_{\rm raw}^3-J_{\rm raw}^2}\quad(\Delta_F\ne0).
```

These conventions are exactly those employed in H352, H403 and the associated verification modules. The sign of the discriminant here is **not** reversed as in a line of the supplied suggestion. A quartic with repeated roots has $`\Delta_F=0`$, and a smooth elliptic $`j_F`$ is then not defined from that singular quartic.

The binomial/spinorial form uses coefficients

```math
F(X,Z)=\psi_0X^4+4\psi_1X^3Z+6\psi_2X^2Z^2+4\psi_3XZ^3+\psi_4Z^4.
```

Define

```math
I_b=\psi_0\psi_4-4\psi_1\psi_3+3\psi_2^2,\qquad J_b=\det\begin{pmatrix}\psi_0&\psi_1&\psi_2\\\psi_1&\psi_2&\psi_3\\\psi_2&\psi_3&\psi_4\end{pmatrix}.
```

Direct substitution of $`(a,b,c_2,d,f)=(\psi_0,4\psi_1,6\psi_2,4\psi_3,\psi_4)`$ gives

```math
I_{\rm raw}=12I_b,\qquad J_{\rm raw}=432J_b,\qquad \Delta_F=256(I_b^3-27J_b^2).
```

Hence on the smooth locus

```math
j_F=\frac{1728I_b^3}{I_b^3-27J_b^2}.
```

The conversion factors $`12`$ and $`432`$ are indispensable when comparing an archived Master quartic and a Petrov Weyl-spinor quartic. A symbol $`I`$ written without its representation and normalization is insufficient to compare two mathematical objects.

**Representation statement [K].** Over characteristic zero, binary quartics live in $`\mathrm{Sym}^4((\mathbb C^2)^*)`$; their algebraic invariant ring under the appropriate $`SL_2`$ action is generated by the degree-two $`I`$ and degree-three $`J`$. This does not provide a canonical embedding of *every* geometrical quantity into that representation.

## 3. First explicit curvature quartic: the surface fundamental forms [D,V,H421]

Let $`(M^2,g)`$ be an oriented Riemannian surface immersed in Euclidean three-space, with principal curvatures $`k_1,k_2`$. Put

```math
H_m=\frac{k_1+k_2}{2},\qquad K_G=k_1k_2.
```

Following the **explicit construction verified in archived H421**, form the binary quartic

```math
F_{\rm surf}(X,Z)=(X^2+Z^2)(k_1X^2+k_2Z^2)=k_1X^4+2H_mX^2Z^2+k_2Z^4.
```

This depends on the chosen immersion/shape operator; the metric alone fixes $`K_G`$ but not the *extrinsic* $`H_m`$.

**Theorem 3.1 [D,V,H421].** The classical quartic invariants are

```math
I_{\rm surf}=4H_m^2+12K_G,\qquad J_{\rm surf}=16H_m(9K_G-H_m^2).
```

The polynomial discriminant and elliptic modulus are

```math
\Delta_{\rm surf}=256K_G(H_m^2-K_G)^2,\qquad j_{\rm surf}=\frac{64(H_m^2+3K_G)^3}{K_G(H_m^2-K_G)^2}
```

whenever the discriminant is nonzero.

**Proof, step by step.**

1. This is an even quartic with coefficients $`a=k_1`$, $`c_2=k_1+k_2=2H_m`$, $`f=k_2`$ and $`b=d=0`$.
2. Substitute into the raw invariant definitions:

```math
I_{\rm surf}=c_2^2+12af=4H_m^2+12K_G,\qquad J_{\rm surf}=2c_2(36af-c_2^2)=16H_m(9K_G-H_m^2).
```

3. Its discriminant is that of $`aX^4+c_2X^2Z^2+fZ^4`$:

```math
\Delta_{\rm surf}=16af(c_2^2-4af)^2=256K_G(H_m^2-K_G)^2.
```

4. Substitute into $`j=256I_{\rm surf}^3/\Delta_{\rm surf}`$ and simplify to the stated expression.

**Root interpretation.** The factor $`X^2+Z^2`$ encodes two fixed projective roots $`\pm i`$. The remaining principal-curvature quadratic supplies two further roots. Degeneracy occurs when $`K_G=0`$ or $`H_m^2=K_G`$ (the latter is an umbilic condition, since $`H_m^2-K_G=(k_1-k_2)^2/4`$). Hence this specific quartic is smooth exactly at nonparabolic, nonumbilic points.

The parameter $`\rho=H_m^2/K_G`$ gives the source's degree-three modular expression

```math
j_{\rm surf}=64\frac{(\rho+3)^3}{(\rho-1)^2},\qquad \rho\ne1,\quad K_G\ne0.
```

It is a genuine binary-quartic-to-elliptic-curve construction. It does not mean the immersion is itself an elliptic curve or that $`\rho`$ provides a dynamical time.

## 4. Catenoid and helicoid: a smooth harmonic quartic [D,V,H424]

For the canonical catenoid and its Euclidean helicoid associate, the common induced metric and principal curvatures are

```math
I=R^2(du^2+dv^2),\qquad k_1=-rS^2,\qquad k_2=rS^2,\qquad H_m=0,\qquad K_G=-r^2S^4.
```

Consequently,

```math
F_{\rm cat}(X,Z)=rS^2(Z^4-X^4).
```

Its invariants are

```math
I_{\rm cat}=-12r^2S^4,\qquad J_{\rm cat}=0,\qquad \Delta_{\rm cat}=-256r^6S^{12}\ne0.
```

Thus the associated smooth elliptic double cover has

```math
j_{\rm cat}=1728.
```

**Derivation.** The minimality condition $`H_m=0`$ makes the cubic invariant vanish. For a nonflat minimal point $`K_G<0`$, we have $`I_{\rm surf}=12K_G`$, $`\Delta_{\rm surf}=256K_G^3`$, so $`j=256(12K_G)^3/(256K_G^3)=1728`$.

This is a **pointwise normalized binary quartic** obtained from extrinsic principal-curvature data. Its coefficient scale varies with $`u`$, but its projective root configuration and $`j`$ do not. The catenoid and helicoid share it because their principal curvatures are the same at corresponding points; their second forms differ by a rotation in tangent frames.

This is a direct, independently checked connection between **Levi-Civita/Gauss-Codazzi curvature and quartic I,J**. It is not a Petrov classification: a two-dimensional surface does not possess an independent four-dimensional Weyl spinor.

## 5. Weitzenbock torsion reconstructs this curvature quartic only with extra data [D,V,H421]

The chosen orthonormal catenoid coframe of SF-DRAFT-030 is

```math
\vartheta^1=Rdu,\qquad\vartheta^2=Rdv,\qquad e_1=R^{-1}\partial_u,\qquad e_2=R^{-1}\partial_v.
```

Declaring this *selected* tangent frame parallel defines a flat metric-compatible Weitzenbock connection with torsion coefficient

```math
t_2=R_u/R^2=rSW,\qquad T(e_1,e_2)=t_2e_2.
```

The exact curvature-from-torsion identity is

```math
K_G=-e_1(t_2)-t_2^2=-r^2S^4.
```

**Corollary 5.1 [D,V].** For the *additional minimal immersion data* $`H_m=0`$, the extrinsic surface-quartic invariants can be expressed through the selected Weitzenbock torsion coefficient:

```math
I_{\rm surf}=-12[e_1(t_2)+t_2^2],\qquad J_{\rm surf}=0,\qquad \Delta_{\rm surf}=-256[e_1(t_2)+t_2^2]^3.
```

At a nonflat point its elliptic modulus is still $`1728`$.

**Proof.** Substitute the torsion reconstruction of Gaussian curvature into the surface-quartic formulas at $`H_m=0`$.

**Critical qualification:** Torsion by itself does not determine the immersion's mean curvature $`H_m`$, and changing the chosen teleparallel frame changes its components. The identity is a *specific reconstruction with a specified metric, chosen tangent frame and given minimal immersion*, not an equality between arbitrary torsion tensors and quartic coefficients. For general nonminimal surfaces $`I_{\rm surf}`$ and $`J_{\rm surf}`$ also require $`H_m`$.

This already answers an important part of the research question more directly than any field-theoretic analogy: in the canonical catenoid, the same Gaussian curvature appears as a Levi-Civita invariant, as a chosen teleparallel torsion-derivative expression, and as a coefficient of the explicitly constructed **surface** binary quartic.

## 6. Four-dimensional Weyl-spinor quartics: a different source of I and J [K,D]

Suppose a time-oriented oriented four-dimensional Lorentzian spin manifold has Levi-Civita connection $`\mathring\nabla`$. On its complex rank-two spin bundle, the self-dual Weyl curvature is represented by a totally symmetric spinor $`\Psi_{ABCD}`$.

Choose a local spin dyad and define its binary quartic

```math
Q_{\rm Weyl}(\xi,\eta)=\Psi_0\xi^4+4\Psi_1\xi^3\eta+6\Psi_2\xi^2\eta^2+4\Psi_3\xi\eta^3+\Psi_4\eta^4.
```

Its Petrov invariants, with binomial normalization, are

```math
I_{\rm W}=\Psi_0\Psi_4-4\Psi_1\Psi_3+3\Psi_2^2,\qquad J_{\rm W}=\det\begin{pmatrix}\Psi_0&\Psi_1&\Psi_2\\\Psi_1&\Psi_2&\Psi_3\\\Psi_2&\Psi_3&\Psi_4\end{pmatrix}.
```

These are scalar polynomials in **Weyl curvature**, invariant under local proper spin-frame changes. Their discriminant is proportional to $`I_{\rm W}^3-27J_{\rm W}^2`$.

The algebraic Petrov root types are I (four simple), II (one double), D (two double), III (one triple), N (one quadruple), and O (zero Weyl spinor). When $`I_{\rm W}=J_{\rm W}=0`$, the possibilities include III, N and O; **those equations alone do not prove type N**. The full spinor/root pattern is necessary.

**Notational pitfall:** If $`Q_{\rm Weyl}`$ is a singular quartic (as for types II/D/III/N), it has no smooth genus-one double cover and no finite elliptic $`j`$ attached to that singular polynomial. In particular $`I_{\rm W}=J_{\rm W}=0`$ is an indeterminate $`0/0`$ in $`1728I^3/(I^3-27J^2)`$, **not** the equianharmonic elliptic value $`j=0`$.

The pointwise quartic of §3 is made from **principal curvatures of a surface**; this one is made from the **Weyl spinor of a four-manifold**. The invariant polynomials are represented by the same abstract $`\mathrm{Sym}^4`$ algebra, but an explicit map of the underlying geometric data is required to relate them.

## 7. Curvature and torsion: the exact derivative bridge [D,K]

Let $`\widetilde\nabla`$ be a chosen flat, metric-compatible Weitzenbock connection on the same metric as Levi-Civita $`\mathring\nabla`$, and let $`\mathsf C=\widetilde\nabla-\mathring\nabla`$ denote their contorsion tensor. In connection-one-form notation,

```math
\widetilde\Omega=\mathring\Omega+\mathsf C,\qquad R(\widetilde\nabla)=0.
```

Expanding the curvature yields the exact tensorial identity

```math
0=R(\mathring\nabla)+D_{\mathring\nabla}\mathsf C+\mathsf C\wedge\mathsf C.
```

Equivalently, by writing $`\mathring\Omega=\widetilde\Omega-\mathsf C`$,

```math
R(\mathring\nabla)=-D_{\widetilde\nabla}\mathsf C+\mathsf C\wedge\mathsf C.
```

Contorsion is algebraic in the full torsion tensor because the two connections are metric-compatible. Hence the *Levi-Civita curvature* is reconstructed from **derivatives and quadratic expressions of torsion/contorsion**.

Only after applying the trace-free Weyl projection to this four-index tensor and, in four dimensions with a spin structure, converting to $`\Psi_{ABCD}`$ do the Weyl quartic and its $`I_{\rm W},J_{\rm W}`$ emerge.

The important negative controls are:

- The Weitzenbock **curvature** is zero. Taking *its own* Weyl tensor would give zero; one must reconstruct the Levi-Civita Weyl tensor using contorsion.
- A quadratic **torsion scalar** alone generally loses enough information that it cannot reconstruct the full Levi-Civita Weyl tensor, its spinor, or its $`I,J`$.
- A general torsion tensor is a vector-valued two-form, **not canonically a binary quartic**. A binary quartic requires the Weyl projection/2-spinor data or a separately specified Cartan-geometric harmonic representation.
- The scalar identity $`\mathring{\mathcal R}=-\mathbb T+\mathbb B`$ from SF-DRAFT-040 is only a trace of this full tensor relation. It does not determine Weyl curvature.

The next sections give a complete worked example where these distinctions are unavoidable.
