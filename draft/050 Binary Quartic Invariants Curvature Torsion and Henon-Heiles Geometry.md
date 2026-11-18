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

## 8. Hénon–Heiles as a separate two-degree-of-freedom Hamiltonian [K,D]

Take a real two-dimensional natural Hamiltonian with distinct mechanical coordinates $`q_1,q_2`$ and momenta $`p_1,p_2`$:

```math
\mathcal H_{\rm HH}(q,p)=\frac12(p_1^2+p_2^2)+V(q_1,q_2).
```

For the generalized cubic Hénon–Heiles family choose the convention

```math
V(q_1,q_2)=\frac12(Aq_1^2+Bq_2^2)+\lambda(q_1^2q_2+\beta q_2^3).
```

The parameters $`A,B,\lambda,\beta`$ of this mechanical problem are **not** the Gram envelope's $`A,B,C`$ or the Master resolution and center $`r,c`$. The cubic Hénon–Heiles Hamiltonian used in the Eisenhart example is not the same as the **quartic Hénon–Heiles coupling forms** labeled $`Q_{168},Q_{1216}`$ in the archived invariant-theory investigation.

The Lagrangian is

```math
L(q,\dot q)=\frac12(\dot q_1^2+\dot q_2^2)-V(q_1,q_2).
```

Euler–Lagrange gives a coupled second-order ODE:

```math
\ddot q_1=-Aq_1-2\lambda q_1q_2,\qquad\ddot q_2=-Bq_2-\lambda(q_1^2+3\beta q_2^2).
```

The first integral is

```math
\mathcal E=\frac12(\dot q_1^2+\dot q_2^2)+V(q_1,q_2).
```

For generic parameters there need not be a second independent integral giving Liouville integrability. The classical Sawada–Kotera, KdV and Kaup–Kupershmidt integrable cases impose special relations among couplings and harmonic terms. None of those integrability conditions is implied by the mere presence of a flat or curved connection in an auxiliary manifold.

The potential gradient and Hessian, which drive two distinct geometric representations below, are

```math
\nabla V=\begin{pmatrix}Aq_1+2\lambda q_1q_2\\Bq_2+\lambda q_1^2+3\beta\lambda q_2^2\end{pmatrix},\qquad \mathrm{Hess}\,V=\begin{pmatrix}A+2\lambda q_2&2\lambda q_1\\2\lambda q_1&B+6\beta\lambda q_2\end{pmatrix}.
```

This is the **same second-order mechanical system** that can now be lifted to several inequivalent geometrical data sets.

## 9. Eisenhart–Duval lift: Hamiltonian trajectories as null geodesics [K,D,V]

Add two coordinates $`t`$ and $`s`$ to the configuration space, and consider the four-dimensional Lorentzian Brinkmann metric

```math
g_E=dq_1^2+dq_2^2+2dt\,ds-2V(q_1,q_2)\,dt^2.
```

It has one negative and three positive directions. The vector field $`\partial_s`$ is null and covariantly constant for its Levi-Civita connection. This is the standard scalar-potential Eisenhart–Duval or Bargmann lift [K].

The geodesic Lagrangian is

```math
L_E=\frac12(\dot q_1^2+\dot q_2^2)+\dot t\dot s-V(q)\dot t^2.
```

The $`s`$-coordinate is cyclic and its conserved conjugate momentum is

```math
p_s=\frac{\partial L_E}{\partial\dot s}=\dot t=\kappa.
```

For $`\kappa\ne0`$, reparametrize the affine geodesic so $`\dot t=1`$. Euler–Lagrange in $`q_i`$ then gives

```math
\frac d{dt}\frac{\partial L_E}{\partial\dot q_i}-\frac{\partial L_E}{\partial q_i}=0\quad\Longrightarrow\quad\ddot q_i+\partial_iV=0.
```

This is **exactly** the original mechanical equation. For a null geodesic with $`\dot t=1`$, the condition $`L_E=0`$ gives

```math
\dot s=V-\frac12|\dot q|^2=2V-\mathcal E.
```

Thus the extra null coordinate recovers the mechanical action along the trajectory, up to the conventional energy term and integration constant.

**Converse and scope.** A mechanical solution at fixed $`\mathcal E`$, together with $`s(t)`$ obtained by integration, lifts locally to a null geodesic. The correspondence needs $`\dot t\ne0`$; global completeness and periodicity of $`s`$ are separate. A null geodesic is a geodesic of a chosen auxiliary metric, not a declaration of physical spacetime dynamics.

## 10. Levi-Civita curvature of the Eisenhart metric is the potential Hessian [D,V]

In coordinate order $`(t,s,q_1,q_2)`$, the metric and inverse matrices are

```math
(g_{\alpha\beta})=\begin{pmatrix}-2V&1&0&0\\1&0&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad (g^{\alpha\beta})=\begin{pmatrix}0&1&0&0\\1&2V&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}.
```

For a time-independent potential, the only nonzero Levi-Civita Christoffel symbols, up to lower-index symmetry, are

```math
\mathring\Gamma^i{}_{tt}=\partial_iV,\qquad\mathring\Gamma^s{}_{ti}=-\partial_iV,\qquad i=1,2.
```

**Direct derivation.** Differentiate $`g_{tt}=-2V`$. All other metric components are constant. Substitution into the Levi-Civita metric formula yields the displayed terms; no metric field equation is used.

Fix the Riemann sign convention for the remainder by

```math
R^\alpha{}_{\beta\mu\nu}=\partial_\mu\Gamma^\alpha{}_{\nu\beta}-\partial_\nu\Gamma^\alpha{}_{\mu\beta}+\Gamma^\alpha{}_{\mu\gamma}\Gamma^\gamma{}_{\nu\beta}-\Gamma^\alpha{}_{\nu\gamma}\Gamma^\gamma{}_{\mu\beta}.
```

**Theorem 10.1 [D,V] (Hessian–tidal curvature).** The only independent nonzero covariant Riemann components are

```math
\mathring R_{titj}=\partial_i\partial_jV,\qquad i,j\in\{1,2\}.
```

Taking the Ricci trace gives

```math
\mathring R_{tt}=\partial_1^2V+\partial_2^2V=\Delta_{\mathbb R^2}V,\qquad\mathring{\mathcal R}=0.
```

**Proof, step by step.**

1. The nonzero connection coefficient $`\mathring\Gamma^i{}_{tt}`$ differentiates in the transverse coordinates to give $`\partial_j\partial_iV`$.
2. The remaining connection terms can be checked directly from the sparse Christoffel list; the independent curvature components are those in the theorem.
3. Contracting $`i,j`$ with the transverse Euclidean inverse metric gives $`\mathring R_{tt}=\Delta V`$.
4. The inverse metric has $`g^{tt}=0`$, so the scalar trace vanishes even when $`\mathring R_{tt}`$ is nonzero.

The *full Hessian*, not merely its trace or a scalar curvature invariant, survives in the curvature tensor. The third derivatives of $`V`$ would control covariant derivatives of this curvature.

### 10.1 Jacobi geodesic deviation is precisely mechanical linearization

Let $`q(t,\epsilon)`$ be a smooth family of mechanical trajectories and $`\xi^i=\partial_\epsilon q^i|_{\epsilon=0}`$. Differentiate the original equations:

```math
\ddot\xi^i+\sum_j(\partial_i\partial_jV)(q(t))\,\xi^j=0.
```

This is a matrix-valued second-order Jacobi/variational equation. It is also the transverse null-geodesic deviation equation of the Eisenhart metric, with the same Hessian matrix $`\mathring R_{titj}`$.

This is a **precise geometric mechanism** for recovering a second-order differential equation and its perturbation theory. It neither presupposes integrability nor automatically separates the matrix system into two scalar Sturm–Liouville equations. A time-dependent orthogonal eigenbasis of the Hessian introduces additional first-derivative coupling terms.

## 11. Weyl curvature and Petrov degeneracy of the scalar-potential lift [D,V,K]

Because the scalar curvature is zero and the Ricci tensor has only the null $`tt`$ component, the Weyl tensor is the trace-free part of the transverse Hessian:

```math
C_{titj}=V_{ij}-\frac12\delta_{ij}\Delta V.
```

All other independent Weyl components vanish, up to tensor symmetries. Introduce the trace-free Hessian matrix

```math
\mathsf A=\begin{pmatrix}D/2&G\\G&-D/2\end{pmatrix},\qquad D=V_{11}-V_{22},\qquad G=V_{12}.
```

**Theorem 11.1 [D,V,K].** On the subset where $`\mathsf A\ne0`$, the Eisenhart Weyl tensor is Petrov type N with repeated null direction $`\partial_s`$. Where $`\mathsf A=0`$, it is Petrov type O. In either case its Weyl-spinor quartic invariants satisfy

```math
I_{\rm W}=0,\qquad J_{\rm W}=0.
```

**Proof, step by step.**

1. The parallel null vector $`\partial_s`$ and the above Weyl component pattern place all nonzero curvature components in the same aligned null transverse sector of a Brinkmann pp-wave.
2. Choose a null spin dyad/tetrad adapted to $`\partial_s`$. The only potentially nonzero Weyl scalar is one extreme component $`\Psi_0`$ or $`\Psi_4`$, depending on which null vector is designated first.
3. The associated binary quartic is a pure fourth power of one linear form, for instance

```math
Q_{\rm W}(\xi,\eta)=\Psi_4\,\eta^4.
```

4. The raw or binomial quartic invariants vanish because all mixed coefficient products are zero. The quartic has a quadruple root when $`\Psi_4\ne0`$ (type N), and vanishes identically when $`\Psi_4=0`$ (type O).

**Important: these vanishing invariants do not imply that the Levi-Civita curvature tensor vanishes.** The Riemann Hessian components may remain nonzero, and the Ricci tensor may remain nonzero even in the conformally flat type-O case.

The same aligned null-index property forces scalar polynomial contractions of the pp-wave curvature to vanish, including $`\mathring{\mathcal R}`$, $`\mathring R_{\mu\nu}\mathring R^{\mu\nu}`$, $`C_{\alpha\beta\gamma\delta}C^{\alpha\beta\gamma\delta}`$ and the Kretschmann scalar. These are weaker diagnostic data than the nonzero Cartan/frame curvature components.

### 11.1 Exact Hénon–Heiles Petrov coefficient

For the chosen cubic potential in §8,

```math
D=A-B+2\lambda(1-3\beta)q_2,\qquad G=2\lambda q_1.
```

Consequently,

```math
\mathsf A=\begin{pmatrix}\frac12[A-B+2\lambda(1-3\beta)q_2]&2\lambda q_1\\2\lambda q_1&-\frac12[A-B+2\lambda(1-3\beta)q_2]\end{pmatrix}.
```

In a standard adapted null tetrad, the nonzero extreme Weyl coefficient is proportional (up to orientation and normalization) to

```math
\Psi_4\ \sim\ D+2iG=A-B+2\lambda(1-3\beta)q_2+4i\lambda q_1.
```

Thus the Weyl tensor is type O precisely at points where

```math
2\lambda q_1=0,\qquad A-B+2\lambda(1-3\beta)q_2=0.
```

Away from that algebraic locus it is type N. These formulas make no reference to the special Liouville-integrable Hénon–Heiles ratios; Petrov N is automatic for the **whole scalar-potential Eisenhart class**.

**Counterexample to an attached claim.** Harmonic potential does not imply type O: $`V=q_1^2-q_2^2`$ has $`\Delta V=0`$ (Ricci-flat lift) but $`\mathsf A=\mathrm{diag}(2,-2)\ne0`$ (type N). Conversely an isotropic quadratic potential $`V=\alpha(q_1^2+q_2^2)/2`$ has $`\mathsf A=0`$ (type O) but $`\Delta V=2\alpha`$ and generally nonzero Ricci tensor.

## 12. An exact Weitzenbock connection of the Eisenhart lift [D,V]

Use the *null* coframe

```math
\vartheta^+=dt,\qquad\vartheta^-=ds-V(q)\,dt,\qquad\vartheta^1=dq_1,\qquad\vartheta^2=dq_2.
```

Its constant frame bilinear form is

```math
g_E=2\vartheta^+\vartheta^-+(\vartheta^1)^2+(\vartheta^2)^2.
```

Declare this null frame parallel for a flat metric-compatible connection $`\widetilde\nabla`$, with zero connection one-forms in the chosen frame. Its torsion two-forms are

```math
\mathcal T^+=0,\qquad\mathcal T^-=-V_1\,dq_1\wedge dt-V_2\,dq_2\wedge dt,\qquad\mathcal T^1=\mathcal T^2=0.
```

**Coordinate proof.** The coordinate coframe component is $`\vartheta^-_t=-V`$. With the same connection convention as SF-DRAFT-040, the only nonzero torsion components are

```math
\mathcal T^s{}_{it}=-V_i,\qquad \mathcal T^s{}_{ti}=V_i.
```

Thus the chosen **torsion tensor records the first derivatives of $`V`$**, while the Levi-Civita curvature records its second derivatives. Contorsion is the exact differential/algebraic bridge from one to the other (§7).

### 12.1 The quadratic torsion scalar vanishes despite nonzero torsion

With the trace convention $`v_\mu=\mathcal T^\nu{}_{\nu\mu}`$, direct inspection of the null components gives

```math
v_\mu=0.
```

Using exactly the quadratic scalar convention of SF-DRAFT-040,

```math
\mathbb T=\frac14\mathcal T_{\rho\mu\nu}\mathcal T^{\rho\mu\nu}+\frac12\mathcal T_{\rho\mu\nu}\mathcal T^{\nu\mu\rho}-v_\rho v^\rho,
```

each individual quadratic contraction vanishes:

```math
\mathcal T_{\rho\mu\nu}\mathcal T^{\rho\mu\nu}=0,\qquad\mathcal T_{\rho\mu\nu}\mathcal T^{\nu\mu\rho}=0,\qquad v_\rho v^\rho=0.
```

The reason is the **null index structure**: raising the first null index pairs it with the complementary null direction, whose relevant torsion components are zero. Hence

```math
\mathbb T=0.
```

Because $`\mathring{\mathcal R}=0`$ and $`\mathring{\mathcal R}=-\mathbb T+\mathbb B`$, the boundary divergence also vanishes:

```math
\mathbb B=0.
```

These equations hold for **every** smooth scalar potential $`V(q_1,q_2)`$ in the chosen Eisenhart null coframe, including highly nonlinear Hénon–Heiles potentials. Nevertheless $`\mathcal T^-\ne0`$ where $`\nabla V\ne0`$, and $`\mathring R_{titj}=V_{ij}`$ may be nonzero.

**New exact negative control:** the pair of scalar teleparallel invariants $`(\mathbb T,\mathbb B)=(0,0)`$ and the Weyl pair $`(I_{\rm W},J_{\rm W})=(0,0)`$ are insufficient to reconstruct either the Hénon–Heiles potential, its integrability class, or its nonzero tidal curvature. Scalar-only identification loses the essential differential data.

This is an explicit example of why the **tensorial** Levi-Civita/Weitzenbock dictionary is stronger than the scalar curvature–torsion–boundary identity. It is not an argument that the torsion *tensor* carries no information.

### 12.2 Exact curvature hierarchy of the lift

The same selected data give a graded chain of objects:

```math
V\ \xrightarrow{\ d\ }\ \nabla V\ \xrightarrow{\ \mathrm{coframe}\ }\ \mathcal T\ \xrightarrow{\ \nabla+\mathcal T^2\ }\ \mathring R\ \xrightarrow{\ \mathrm{tracefree}\ }\ C\ \xrightarrow{\ \mathrm{spinor}\ }\ Q_{\rm W}.
```

At successive steps information may be projected away: $`V`$ is determined by $`\nabla V`$ only up to an additive constant, $`\mathring R`$ sees the Hessian rather than the absolute gradient, the Weyl tensor loses the Hessian trace, and the binary quartic invariants lose nilpotent Petrov-N information. Conversely, reconstructing the full $`V`$ from one of the final scalar invariants is impossible without extra differential and boundary data.

## 13. A constructed tidal-Hessian quartic: nonzero invariants despite Petrov N [D,V]

The lift's curvature matrix $`\mathsf M=(\mathring R_{titj})=(V_{ij})`$ is a real symmetric $`2\times2`$ matrix. Because the transverse plane carries a chosen Euclidean kinetic metric, its eigenvalues $`\lambda_1,\lambda_2`$ are invariant under **orthonormal changes of transverse coordinates**.

We can construct from this data a quartic of **exactly the same type as the archived surface fundamental-form quartic**, but this time the second quadratic form is the mechanical Hessian, not a surface second fundamental form:

```math
F_{\rm tidal}(X,Z)=(X^2+Z^2)(\lambda_1X^2+\lambda_2Z^2).
```

Let $`\tau=\mathrm{tr}\,\mathsf M=\Delta V`$ and $`d=\det\mathsf M`$. The eigenvalue sum and product are $`\tau,d`$.

**Theorem 13.1 [D,V] (tidal quartic invariants).** The constructed quartic has

```math
I_{\rm tidal}=\tau^2+12d,\qquad J_{\rm tidal}=2\tau(36d-\tau^2),\qquad\Delta_{\rm tidal}=16d(\tau^2-4d)^2.
```

On the smooth locus its elliptic modulus is

```math
j_{\rm tidal}=\frac{16(\tau^2+12d)^3}{d(\tau^2-4d)^2}.
```

**Proof.** In the eigenbasis the unweighted coefficients are $`a=\lambda_1`$, $`c_2=\lambda_1+\lambda_2=\tau`$, $`f=\lambda_2`$, with $`b=d_{\rm cubic}=0`$. Substitute into the definitions of §2, and use $`\tau^2-4d=(\lambda_1-\lambda_2)^2`$.

This construction is **canonical relative to the chosen Euclidean transverse kinetic metric and Hessian tensor**, up to an interchange of eigenvalues that does not alter the stated invariants. It is not canonically a Petrov Weyl-spinor quartic; the map from a symmetric $`2\times2`$ tidal tensor to a binary quartic is an **additional polynomial construction**.

### 13.1 Exact expression in the cubic Hénon–Heiles parameters

For the cubic potential of §8, define

```math
\tau=A+B+2\lambda(1+3\beta)q_2,\qquad d=(A+2\lambda q_2)(B+6\beta\lambda q_2)-4\lambda^2q_1^2.
```

Then $`I_{\rm tidal}`$ and $`J_{\rm tidal}`$ above are explicit polynomials in $`(q_1,q_2;A,B,\lambda,\beta)`$, and

```math
\tau^2-4d=[A-B+2\lambda(1-3\beta)q_2]^2+16\lambda^2q_1^2.
```

Thus

```math
\Delta_{\rm tidal}=16d\left([A-B+2\lambda(1-3\beta)q_2]^2+16\lambda^2q_1^2\right)^2.
```

Over the real transverse plane, this quartic is singular precisely when $`\det\mathsf M=0`$ or $`\mathsf M`$ is isotropic ($`\lambda_1=\lambda_2`$). At the latter points the **Weyl tensor** vanishes (type O). Elsewhere the Weyl type is N, irrespective of whether the tidal quartic is smooth or singular.

### 13.2 A simple exact counterexample to conflating the two invariant pairs

Choose a local quadratic potential $`V=(q_1^2+2q_2^2)/2`$. Then

```math
\mathsf M=\begin{pmatrix}1&0\\0&2\end{pmatrix},\qquad \tau=3,\qquad d=2.
```

The tidal quartic is

```math
F_{\rm tidal}=(X^2+Z^2)(X^2+2Z^2)=X^4+3X^2Z^2+2Z^4.
```

Its invariants are

```math
I_{\rm tidal}=33,\qquad J_{\rm tidal}=378,\qquad\Delta_{\rm tidal}=32,\qquad j_{\rm tidal}=287496.
```

But the **very same** potential's Eisenhart Weyl-spinor quartic is type N, so

```math
I_{\rm W}=J_{\rm W}=0.
```

It is impossible to identify these two invariant pairs as scalars of one unnamed “quartic”. The number $`287496`$ also occurs in the archived quartic Hénon–Heiles pencil at its parameter $`t=0`$, but that numerical match alone is **not** a constructed equivalence of dynamical Hamiltonians.

### 13.3 Recovering the tidal quartic from a torsion derivative

In the chosen Eisenhart Weitzenbock coframe of §12,

```math
\mathcal T^s{}_{it}=-V_i,\qquad M_{ij}=-\partial_j\mathcal T^s{}_{it}=V_{ij}.
```

Therefore $`\tau`$ and $`d`$, hence the constructed $`I_{\rm tidal}`$ and $`J_{\rm tidal}`$, are polynomials in **first derivatives of the full torsion tensor in this preferred chart**. This is a genuine torsion-to-invariant construction, but it does not depend on the vanishing scalar $`\mathbb T`$. The preferred-frame and coordinate qualifications must be retained; a general covariant formulation uses the full contorsion identity rather than bare partial derivatives.

This result is potentially useful for an eventual Layer II theorem: it gives two separate, explicitly typed paths to the *same mechanical tidal matrix*, one through Levi-Civita curvature and one through a specified teleparallel torsion derivative.

## 14. The archived Hénon–Heiles quartic pencil and the Master quartic [D,V,H352,H353,H403]

The uploaded ZIP contains an independent, extensive algebraic identification concerning **quartic Hénon–Heiles coupling forms**. This must be imported accurately, rather than attributed to the generic cubic mechanical potential of §8.

The two historical quartic coupling forms are

```math
Q_{168}=X^4+6X^2Z^2+8Z^4,\qquad Q_{1216}=X^4+12X^2Z^2+16Z^4.
```

Their projective pencil with affine coordinate $`t`$ is

```math
P_t=(1+t)X^4+6(1+2t)X^2Z^2+8(1+2t)Z^4.
```

The normalized Master energy quartic, in homogeneous notation, is

```math
Q_e(X,Z)=-X^4+X^2Z^2+eZ^4.
```

**Theorem 14.1 [H403,D,V] (exact projective equivalence away from the exceptional member).** Set

```math
e(t)=-\frac{2(t+1)}{9(2t+1)}.
```

For $`2t+1\ne0`$, the exact polynomial identity is

```math
P_t(X,Z)=-\frac{2t+1}{2}Q_{e(t)}(2iZ,\sqrt3X).
```

**Direct proof, step by step.**

1. Substitute $`(X_Q,Z_Q)=(2iZ,\sqrt3X)`$ into $`Q_e`$.
2. The terms are $`-(2iZ)^4=-16Z^4`$, $`(2iZ)^2(\sqrt3X)^2=-12X^2Z^2`$, and $`e(\sqrt3X)^4=9eX^4`$.
3. Multiply by $`-(2t+1)/2`$; the $`Z^4`$ and $`X^2Z^2`$ coefficients become $`8(2t+1)`$ and $`6(2t+1)`$.
4. Insert $`9e(t)=-2(t+1)/(2t+1)`$; the $`X^4`$ coefficient becomes $`1+t`$. This is exactly $`P_t`$.

The coordinate transformation is invertible over $`\mathbb C`$ and the overall scaling is nonzero for $`t\ne-1/2`$. **This is projective equivalence of binary quartic families**. The complex coefficient $`i`$ and the parameter-dependent scale matter: it is not automatically an equivalence over $`\mathbb R`$ of the full mechanical Hénon–Heiles equations, energy surfaces, canonical symplectic forms or their real-time dynamics.

At $`t=-1/2`$ the projective pencil has a singular fourth-power member and $`e(t)`$ is infinite. The formula with a finite Master energy does not apply without projective compactification.

### 14.1 Raw I, J and discriminant of the Hénon–Heiles pencil

An even quartic $`aX^4+c_2X^2Z^2+fZ^4`$ has $`I=c_2^2+12af`$, $`J=2c_2(36af-c_2^2)`$. Substituting the coefficients of $`P_t`$ yields

```math
I_P=12(2t+1)(14t+11),\qquad J_P=432(2t+1)^2(6t+7).
```

Its polynomial discriminant is

```math
\Delta_P=2048(t+1)(2t+1)^3(10t+1)^2.
```

The smooth modulus is

```math
j_P(t)=216\frac{(11+14t)^3}{(1+t)(1+10t)^2}.
```

For the Master quartic,

```math
I_M=1-12e,\qquad J_M=-2-72e,\qquad\Delta_M=-16e(1+4e)^2.
```

Its modulus is

```math
j_M(e)=-16\frac{(1-12e)^3}{e(1+4e)^2}.
```

**Verification of compatibility:** Direct substitution of $`e=e(t)`$ into $`j_M(e)`$ simplifies to $`j_P(t)`$. The archived discriminant identity is likewise verified:

```math
\Delta_P=6^6(2t+1)^6\,\Delta_M(e(t)).
```

The singular members occur at $`t=-1`$ with multiplicity one, $`t=-1/10`$ with multiplicity two, and $`t=-1/2`$ with multiplicity three. They correspond to root-collision partitions $`(2,1,1)`$, $`(2,2)`$, and $`(4)`$ respectively (H403).

### 14.2 The two special modular values

At $`t=-7/6`$, one obtains $`e=-1/36`$ and $`j_P=1728`$. At $`t=7/2`$, one obtains $`e=-1/8`$ and $`j_P=8000`$:

```math
j_P(-7/6)=1728,\qquad j_P(7/2)=8000.
```

At $`j=1728`$ the smooth Master/Hénon–Heiles elliptic curve has the same abstract complex elliptic modulus as the catenoid's fundamental-form quartic of §4. Over $`\mathbb C`$ smooth elliptic curves with equal $`j`$ are abstractly isomorphic. **However, this equality at a selected parameter does not supply a canonical map between the catenoid immersion, the Hénon–Heiles Hamiltonian, their cycles, or their time differentials.** An explicit realization would require those extra data and belongs in [O3].

At $`e=-1/8`$, the elliptic energy curve has $`j=8000`$ and nonzero discriminant, as in H406. The same value is not a Weyl-spinor Petrov invariant of the associated Eisenhart lift, because its Weyl quartic remains singular type N with $`I_{\rm W}=J_{\rm W}=0`$.

## 15. The Hessian pencil, modular curves and what the connections do not imply [H404,H405,H406]

The archived H404 computation defines a binary-quartic Hessian covariant using ordinary polynomial partial derivatives:

```math
\mathcal H(F)=\frac{F_{XX}F_{ZZ}-F_{XZ}^2}{144}.
```

From a quartic $`F`$ one forms a projective pencil $`F+t\mathcal H(F)`$. The archive verifies its invariant and discriminant syzygies, including a squared cubic factor of the pencil discriminant and its roots at the reciprocals of the associated elliptic curve's two-torsion coordinates.

The important classification is **algebraic**: the polynomial Hessian covariant is an $`SL_2`$-equivariant construction on $`\mathrm{Sym}^4(\mathbb C^2)`$, not the Riemannian covariant Hessian $`\nabla df`$ of a surface potential and not the Hessian of the mechanical Hénon–Heiles potential $`V(q_1,q_2)`$.

The standard normal form recorded in H405 is

```math
F_k(X,Z)=X^4+6kX^2Z^2+Z^4.
```

Its invariant moduli are

```math
I_k=12(3k^2+1),\qquad J_k=432k(1-k^2),\qquad \Delta_k=256(9k^2-1)^2.
```

and

```math
j_k=1728\frac{(3k^2+1)^3}{(9k^2-1)^2}.
```

The archival $`S_3`$ action on $`k`$, the degree-six map to $`j`$, the Fricke involution at level two, and the Hessian self-map all belong to the **elliptic quartic-pencil** problem. H405 explicitly corrects the tempting false claim that taking the Hessian preserves $`j`$; generically it does not.

No Levi-Civita connection, Weitzenbock frame, Hénon–Heiles lift or spin structure is necessary to state those algebraic invariant formulas. Geometric connections can realize such quartics only through a separately specified construction like §§3, 6, 13 or 14.

### 15.1 A clear independence test

Consider the original cubic Master at $`e=1/12`$. Then $`I_M=0`$, $`J_M=-8`$, and $`\Delta_M\ne0`$; therefore $`j_M=0`$, the smooth equianharmonic modulus. Its associated scalar-potential Eisenhart Weyl quartic would still have $`I_{\rm W}=J_{\rm W}=0`$, for which no smooth elliptic $`j`$ is defined. The two statements have the **same algebraic symbol zero** but radically different geometric meanings.

At $`e=-1/36`$, the smooth Master quartic has $`J_M=0`$, $`I_M\ne0`$ and $`j=1728`$. This is the same abstract harmonic quartic locus as the nonflat minimal-surface construction, but is not produced by it without an explicit map.

## 16. Jacobi–Maupertuis geometry: an independent Riemannian realization [K,D,V]

The Eisenhart lift is Lorentzian and uses an extra null coordinate. At a fixed mechanical energy $`\mathcal E`$, a **different** geometric construction is available: the Jacobi–Maupertuis metric on the Hill region where $`\mathcal E>V`$:

```math
g_J=2(\mathcal E-V(q_1,q_2))(dq_1^2+dq_2^2)=\Lambda^2(dq_1^2+dq_2^2),\qquad \Lambda=\sqrt{2(\mathcal E-V)}.
```

Mechanical trajectories at energy $`\mathcal E`$ are reparametrized geodesics of this metric on its regular region. The Jacobi arclength and mechanical clock obey

```math
\frac{ds_J}{dt}=2(\mathcal E-V(q(t))).
```

**Proof.** The kinetic energy is $`|\dot q|^2/2=\mathcal E-V`$. Thus the speed in $`g_J`$ is $`\Lambda|\dot q|=2(\mathcal E-V)`$. Maupertuis' variational principle then identifies fixed-energy unparametrized mechanical paths with geodesics.

Introduce the conformal factor $`h=\ln\Lambda=\frac12\ln[2(\mathcal E-V)]`$. The Gaussian curvature formula is

```math
K_J=-\Lambda^{-2}(\partial_1^2h+\partial_2^2h).
```

**Theorem 16.1 [D,V] (Jacobi curvature from gradient and Hessian).** On the Hill region,

```math
K_J=\frac{\Delta V}{4(\mathcal E-V)^2}+\frac{|\nabla V|^2}{4(\mathcal E-V)^3}.
```

**Proof, step by step.**

1. Differentiate $`h`$:

```math
\partial_i h=-\frac{V_i}{2(\mathcal E-V)}.
```

2. Differentiate again and take the Euclidean trace:

```math
\Delta h=-\frac{\Delta V}{2(\mathcal E-V)}-\frac{|\nabla V|^2}{2(\mathcal E-V)^2}.
```

3. Multiply by $`-\Lambda^{-2}=-[2(\mathcal E-V)]^{-1}`$ and simplify. This gives the formula in the theorem.

The **scalar Jacobi curvature** depends on both the Hessian trace and the squared gradient. It differs from the trace-free Hessian controlling the Eisenhart Weyl tensor. In particular, Jacobi curvature can diverge at a Hill boundary $`\mathcal E=V`$ where the chosen metric degenerates; that is not automatically a curvature singularity of the smooth four-dimensional Eisenhart lift.

### 16.1 A chosen Weitzenbock connection of the Jacobi metric

Use the orthonormal coframe

```math
\vartheta^1=\Lambda\,dq_1,\qquad \vartheta^2=\Lambda\,dq_2.
```

Declare it parallel for a chosen flat metric-compatible tangent connection. Its torsion two-forms are

```math
\mathcal T^1=d\vartheta^1=-\Lambda_2\,dq_1\wedge dq_2,\qquad \mathcal T^2=d\vartheta^2=\Lambda_1\,dq_1\wedge dq_2.
```

Using $`\Lambda_i=-V_i/\Lambda`$, write them explicitly as

```math
\mathcal T^1=\frac{V_2}{\Lambda}\,dq_1\wedge dq_2,\qquad\mathcal T^2=-\frac{V_1}{\Lambda}\,dq_1\wedge dq_2.
```

The Levi-Civita connection one-form in the same oriented tangent-frame convention as SF-DRAFT-030 is

```math
\omega_{12}^{LC}=h_2\,dq_1-h_1\,dq_2=\frac{-V_2\,dq_1+V_1\,dq_2}{2(\mathcal E-V)}.
```

Its curvature two-form is

```math
d\omega_{12}^{LC}=-(\Delta h)\,dq_1\wedge dq_2=K_J\,\vartheta^1\wedge\vartheta^2.
```

This is an exact **second curvature–torsion dictionary** for the same mechanical system, different from the null Eisenhart lift: the chosen two-dimensional torsion encodes first derivatives of the conformal Jacobi factor, and its Levi-Civita curvature follows by differentiation.

### 16.2 Fundamental limitations of Jacobi geometry

The metric depends on the chosen energy $`\mathcal E`$. It is defined only where $`\mathcal E-V>0`$. The curve parameter changes, so temporal growth rates and Lyapunov exponents require careful clock conversion. Neither the scalar curvature of $`g_J`$ nor its teleparallel torsion scalar uniquely determines whether the original two-degree-of-freedom Hénon–Heiles Hamiltonian is Liouville integrable.

## 17. A third geometric comparison: conformally flat Friedmann versus type-N Eisenhart [D,H313]

Draft SF-DRAFT-040 constructs a **different** four-dimensional Lorentzian warped metric from the reciprocal Master envelope:

```math
g_F=-du^2+a(u)^2[(dq^1)^2+(dq^2)^2+(dq^3)^2],\qquad a(u)=\mu^{1/4}\sqrt{\cosh(ru)}.
```

This spatially flat FLRW-type metric is conformally flat for **any** scale factor $`a(u)`$, so its Levi-Civita Weyl tensor is identically zero:

```math
C[g_F]=0,\qquad I_{\rm W}[g_F]=J_{\rm W}[g_F]=0,\qquad \mathrm{Petrov\ type\ O}.
```

The chosen homogeneous Weitzenbock scalar and boundary divergence are nonetheless nontrivial:

```math
\mathbb T[g_F]=6H^2=\frac{3r^2}{2}W^2,\qquad\mathbb B[g_F]=\mathbb T[g_F]+3r^2,\qquad\mathring{\mathcal R}[g_F]=3r^2.
```

Compare with the Hénon–Heiles Eisenhart metric:

```math
I_{\rm W}[g_E]=J_{\rm W}[g_E]=0,\qquad\mathrm{Petrov\ type\ N\ generically},\qquad\mathbb T[g_E]=\mathbb B[g_E]=\mathring{\mathcal R}[g_E]=0.
```

The **same Weyl invariant pair $`(0,0)`$ occurs in geometries of different Petrov types and very different torsion/curvature behavior**. Therefore the mere coincidence of quartic invariants cannot establish a geometric identification, a conformal equivalence, or an equivalence between their respective second-order differential systems.

## 18. Cartan's (2,3,5) quartic: a possible additional bridge, not an automatic consequence [K,O]

In classical Cartan geometry, a rank-two distribution $`D\subset TM^5`$ with growth vector $`(2,3,5)`$ has a canonical parabolic geometry. Its fundamental harmonic curvature is a binary quartic section

```math
\mathcal C\in\Gamma(\mathrm{Sym}^4D^*).
```

Its projective root type is often described using Petrov-like labels. This is a **genuine** curvature-quartic appearance in a geometry not built from a four-dimensional Lorentzian Weyl spinor. Modern work also relates certain Cartan quartics to Weyl quartics of specifically constructed para-Kähler–Einstein twistor geometries.

However, a generic pair of second-order Hénon–Heiles ODEs is **not automatically** a specified (2,3,5)-distribution or an almost-Grassmannian geometry. To claim a Cartan quartic from it, one must provide the five-manifold, rank-two distribution, derived flag, appropriate Cartan connection and explicit harmonic-curvature coefficients. There is no established theorem in the uploaded sources identifying this quartic with the Master/Hénon–Heiles energy quartic.

Thus this is a legitimate **open research path**, not a proved universal equivalence or a mechanism that distinguishes integrable and chaotic parameter values merely by the symbols I and J.

## 19. Integrability survives the lift as Killing tensors, not as Weyl I and J [D,K,V]

The Eisenhart construction does more than reproduce the second-order equations. Its geodesic Hamiltonian makes the fate of **polynomial mechanical first integrals** explicit.

From the inverse metric of §10, the cotangent geodesic Hamiltonian is

```math
\mathcal H_E=\frac12(p_1^2+p_2^2)+p_t p_s+V(q_1,q_2)p_s^2.
```

The momenta $`p_s`$ and $`p_t`$ are conserved. On the null shell $`\mathcal H_E=0`$ with $`p_s=1`$, identify

```math
p_t=-\mathcal E,\qquad\frac12(p_1^2+p_2^2)+V=\mathcal E.
```

Now suppose the mechanical Hamiltonian $`\mathcal H_{\rm HH}=\frac12(p_1^2+p_2^2)+V`$ has a first integral $`F(q,p_1,p_2)`$ that is polynomial in the mechanical momenta of degree at most $`m`$, with coefficients independent of $`t`$.

**Theorem 19.1 [D,K] (homogenized Killing-tensor lift).** On $`p_s\ne0`$, set

```math
\widetilde F(q,p_1,p_2,p_s)=p_s^mF(q,p_1/p_s,p_2/p_s).
```

Then $`\widetilde F`$ is a homogeneous polynomial of total degree $`m`$ in the lift momenta and is conserved by the Eisenhart geodesic Hamiltonian:

```math
\{\widetilde F,\mathcal H_E\}_{\mathrm{can}}=0.
```

Accordingly, its symmetric homogeneous momentum coefficients define a rank-$`m`$ Killing tensor of the lift metric (modulo the usual reductions when the polynomial has lower effective rank).

**Proof, step by step.**

1. Since $`F`$ is a polynomial of degree at most $`m`$, multiplying by $`p_s^m`$ cancels the denominators and produces a homogeneous polynomial in $`(p_1,p_2,p_s)`$.
2. Since $`V`$ and $`F`$ are independent of $`t,s`$, the terms involving $`p_t`$ and their canonical derivatives vanish in the Poisson bracket.
3. Write $`P_i=p_i/p_s`$; then

```math
\partial_{q_i}\widetilde F=p_s^mF_{q_i}(q,P),\qquad\partial_{p_i}\widetilde F=p_s^{m-1}F_{P_i}(q,P).
```

4. Insert these derivatives and $`\partial_{p_i}\mathcal H_E=p_i=p_sP_i`$, $`\partial_{q_i}\mathcal H_E=p_s^2V_{q_i}`$ into the canonical bracket:

```math
\{\widetilde F,\mathcal H_E\}=p_s^{m+1}\sum_{i=1}^2\left(P_iF_{q_i}-V_{q_i}F_{P_i}\right)=p_s^{m+1}\{F,\mathcal H_{\rm HH}\}=0.
```

5. The vanishing bracket of a symmetric homogeneous momentum polynomial with the geodesic Hamiltonian is precisely the Killing-tensor condition on its coefficient field.

**Immediate example.** The mechanical energy itself homogenizes to the quadratic tensor integral

```math
\widetilde{\mathcal H}_{\rm mech}=\frac12(p_1^2+p_2^2)+V p_s^2,\qquad \mathcal H_E=\widetilde{\mathcal H}_{\rm mech}+p_tp_s.
```

Its bracket vanishes identically. An additional independent polynomial integral in a special integrable Hénon–Heiles case yields an additional nontrivial Killing tensor. Generic nonintegrable parameter choices do not acquire such a tensor merely because the lift has Petrov type N.

**This is the correct geometric discriminator:** the integrability distinctions within the ordinary scalar-potential lift are encoded in special Killing tensors, separability, Lax/ spectral structures and algebraic curves—not in the universally vanishing Weyl-spinor pair $`I_{\rm W},J_{\rm W}`$.

**Scope:** This theorem concerns first integrals polynomial in momenta, independent of time, and the chosen scalar-potential Eisenhart lift. Integrals rational in momenta, time-dependent, defined only on a fixed-energy shell, or involving magnetic terms require additional homogenization or lift arguments.

## 20. A dictionary of four quartics and the information each retains [D,H]

| Quartic | Input object | Coefficients obtained from | Generic invariant behavior | What it does not determine |
|---|---|---|---|---|
| Surface fundamental-form $`F_{\rm surf}`$ | Immersed Euclidean surface $`(I,II)`$ | principal curvatures $`k_1,k_2`$ | $`I=4H_m^2+12K_G`$, $`J=16H_m(9K_G-H_m^2)`$ | entire immersion, period closing, torsion gauge |
| Master/Hénon–Heiles pencil $`Q_e,P_t`$ | Algebraic first integral or coupling-form pencil | polynomial coefficients and explicit projective map | generally $`\Delta\ne0`$, nonconstant elliptic $`j`$ | full HH mechanical integrability or spacetime Weyl type |
| Eisenhart Weyl-spinor $`Q_{\rm W}`$ | Four-dimensional Levi-Civita Weyl curvature | trace-free Hessian of $`V`$, spin dyad | type N/O, $`I_{\rm W}=J_{\rm W}=0`$ | potential Hessian trace, mechanical integrability, modulus of another quartic |
| Constructed tidal Hessian $`F_{\rm tidal}`$ | Euclidean configuration metric and Hessian $`V_{ij}`$ | eigenvalues of Hessian | generally nonzero $`I,J,\Delta`$ with $`j`$ given in §13 | full potential, trajectory clock, Weyl Petrov type |
| Cartan $`(2,3,5)`$ quartic | Explicit rank-two distribution plus canonical Cartan connection | harmonic curvature of distribution | depends on selected distribution | generic ODE or HH data without a specified construction |

The common abstract representation $`\mathrm{Sym}^4(\mathbb C^2)`$ **explains why identical invariant polynomials and root-degeneration types recur**. The source-to-quartic maps are different. There is no theorem saying that two objects with numerical equal $`j`$ or both with vanishing $`I,J`$ must be geometrically the same, unless the appropriate smoothness and reconstruction hypotheses are met.

### 20.1 Typed diagram for the two genuinely coupled connections

The exact Eisenhart part can be organized as a commuting *reconstruction* chain, with a caveat that the arrows to scalars discard information:

```math
V\ \xrightarrow{d}\ (V_i)\ \xrightarrow{\mathrm{null\ coframe}}\ \mathcal T^s{}_{it}=-V_i\ \xrightarrow{-\partial_j}\ M_{ij}=V_{ij}.
```

```math
V\ \xrightarrow{\mathrm{Eisenhart}}\ g_E\ \xrightarrow{\mathring\nabla}\ \mathring R_{titj}=M_{ij}\ \xrightarrow{\mathrm{tracefree}}\ C_{titj}=M_{ij}-\frac12(\mathrm{tr}\,M)\delta_{ij}.
```

From $`M_{ij}`$ one may construct $`F_{\rm tidal}`$, with generally nonzero invariants. From the Weyl projection one obtains $`Q_{\rm W}`$, always type N/O for this lift. Both constructions use the same $`M`$, yet the outputs are **not** the same quartic.

The Jacobi metric supplies a further map at fixed energy:

```math
(V,\mathcal E)\ \xrightarrow{\mathcal E>V}\ g_J=2(\mathcal E-V)\delta\ \xrightarrow{\mathrm{LC}}\ K_J=\frac{\Delta V}{4(\mathcal E-V)^2}+\frac{|\nabla V|^2}{4(\mathcal E-V)^3}.
```

A chosen tangent Weitzenbock frame of $`g_J`$ recovers this curvature from its own torsion, while the four-dimensional Eisenhart teleparallel scalar is identically zero. These are consistent, **different geometric realizations**.

### 20.2 Connection to the framework's foundational layers

- **Layer I, algebraic:** Master energy quartic, Hessian covariant of a binary form, $`I_{\rm raw},J_{\rm raw},\Delta,j`$, modular transforms and discriminant loci; real/complex normalization and parameter clocks.
- **Layer II, geometry:** fundamental-form quartic, Levi-Civita versus chosen Weitzenbock connections, explicit Eisenhart and Jacobi metrics, curvature/torsion tensor relationship, Weyl/Petrov quartic, Cartan distribution if actually built.
- **Layer III, correspondences:** Hénon–Heiles Hamiltonian to geodesics, polynomial integrals to Killing tensors, fixed-energy Maupertuis reparametrization, archived quartic-pencil equivalence with its projective constraints, Gauss–Manin and Picard–Fuchs after an actual family of curves is chosen.
- **Layer IV, applications:** specific mechanical, stochastic, or physical-gravity models only after Hamiltonians, action principles, boundary conditions and stability assumptions are imposed.

No physical prediction is inferred by any of the foundational identities.

## 21. Independent verification record [V]

The following independent calculations were executed symbolically with SymPy and reviewed against the ZIP's corresponding formulas:

1. **Eisenhart inverse metric:** The matrix of §10 multiplies by its proposed inverse to the identity for symbolic $`V`$.
2. **Levi-Civita coefficients:** For the full cubic Hénon–Heiles potential, the only independent nonzero coefficients are $`\mathring\Gamma^i{}_{tt}=V_i`$, $`\mathring\Gamma^s{}_{ti}=-V_i`$, with $`t`$-independent $`V`$.
3. **Riemann and Ricci:** Direct four-index curvature calculation gives $`\mathring R_{titj}=V_{ij}`$, $`\mathring R_{tt}=\Delta V`$ and scalar $`\mathring{\mathcal R}=0`$.
4. **Weyl Hessian:** Direct trace subtraction gives $`C_{titj}=V_{ij}-(\Delta V)\delta_{ij}/2`$ and the explicit Hénon–Heiles formulas of §11.1.
5. **Preferred null teleparallel coframe:** All independent torsion components equal $`\mathcal T^s{}_{it}=-V_i`$ or their antisymmetric partners. The torsion trace and **both distinct quadratic contractions** vanish identically as symbolic expressions; therefore $`\mathbb T=\mathbb B=0`$.
6. **Jacobi metric:** Exact symbolic differentiation proves $`K_J=\Delta V/[4(\mathcal E-V)^2]+|\nabla V|^2/[4(\mathcal E-V)^3]`$.
7. **Master quartic:** $`\Delta_M=-16e(4e+1)^2`$ and $`(4I_M^3-J_M^2)/27=\Delta_M`$.
8. **Archived Hénon–Heiles quartic pencil:** Direct polynomial substitution confirms $`P_t=-(2t+1)Q_{e(t)}(2iZ,\sqrt3X)/2`$ as an algebraic identity, and its discriminant is $`2048(t+1)(2t+1)^3(10t+1)^2`$.
9. **Invariant normalization:** The binomial-to-raw conversions $`I_{\rm raw}=12I_b`$ and $`J_{\rm raw}=432J_b`$ follow by substitution; the quoted discriminant and elliptic $`j`$ formulas are consistent.
10. **Constructed tidal quartic:** For $`\lambda_1=1,\lambda_2=2`$, direct substitution yields $`I=33`$, $`J=378`$, $`\Delta=32`$, $`j=287496`$, while the Eisenhart Weyl invariants remain zero.
11. **Homogeneous-integral lift:** The Poisson-bracket identity of §19 was checked for the mechanical energy example using the full cubic Hénon–Heiles potential; the general polynomial argument is proved algebraically in the text.

These computations are **exact checks of the displayed polynomial/differential identities**, not experimental proof of any proposed new globally integrable Hénon–Heiles coupling or existence of a special global spin structure.

### 21.1 Minimal reproducibility recipe

Take the coordinate order $`(t,s,q_1,q_2)`$, metric matrix in §10, and $`V=(Aq_1^2+Bq_2^2)/2+\lambda(q_1^2q_2+\beta q_2^3)`$. Compute the inverse, Christoffels, Riemann tensor with the sign convention in §10, and Weyl tensor by removing the Ricci trace. For the preferred teleparallel connection use $`\vartheta^+=dt`$, $`\vartheta^-=ds-Vdt`$, $`\vartheta^i=dq_i`$, and raise/lower torsion indices with the **null** metric rather than a diagonal Euclidean form; otherwise the vanishing torsion scalar is missed.

For the quartic algebra use $`I=12af-3bd+c_2^2`$, $`J=72ac_2f+9bc_2d-27ad^2-27fb^2-2c_2^3`$. For $`P_t`$ use a complex coefficient $`i`$ in the projective coordinate map and retain the exceptional $`t=-1/2`$ separately.

## 22. Corrections to the suggested text and precise research limits [C,O]

| Statement suggested or tempting | Mathematical audit |
|---|---|
| Levi-Civita and Weitzenbock have unrelated curvature/torsion algebra. | False: the full contorsion identity exactly reconstructs LC curvature from a chosen flat metric-compatible connection. |
| Any torsion tensor is a binary quartic classified by I and J. | False: torsion is a vector-valued two-form; the Weyl spinor or a separately specified harmonic-curvature projection produces a quartic. |
| Weyl quartic and Master/Hénon–Heiles quartic must have equal I,J. | False: the standard HH Eisenhart Weyl invariants vanish for every scalar potential, while the energy-pencil invariants generally do not. |
| I=J=0 for a Weyl quartic proves Petrov N. | False alone: could be III, N or O; the pp-wave component pattern proves N/O here. |
| I=J=0 is elliptic j=0. | False: a zero or quadruple-root quartic is singular or identically zero, so the smooth elliptic modulus is undefined. |
| Harmonic potential implies conformally flat Eisenhart geometry. | False: harmonicity gives Ricci-flat lift but a nonzero trace-free Hessian can still yield type N. |
| Adding an arbitrary magnetic one-form to Brinkmann data generically produces Petrov type I, D or II. | Not justified; one must calculate curvature and holonomy of that specified metric. Many aligned-null/gyraton extensions remain algebraically special and have vanishing scalar invariants. |
| Cartan harmonic quartic of any coupled second-order ODE detects HH integrable ratios. | Not established: requires an actual Cartan distribution/construction and proof of its invariant/integrability implication. |
| The Hénon–Heiles quartic-pencil isomorphism proves a continuous family of integrable Hamiltonians. | False: the historical ZIP explicitly restricts it to algebraic quartic forms and their elliptic curve families. |
| Petrov I,J determine all LC curvature or the mechanical Hessian. | False: Weyl projection removes Ricci trace, and type N has vanishing scalar polynomial invariants despite nonzero tidal Hessian. |
| A flat Weitzenbock connection has zero torsion or no curvature information. | False: its torsion may be nonzero; differentiation/contorsion reconstruct LC curvature. |
| A j equality alone gives a canonical correspondence of flows and periods. | False: smooth elliptic isomorphism after selecting a complex curve does not identify mechanical clocks, one-forms, real structure or Hamiltonian symplectic data. |

### Open research questions

1. [O1] For the archived integrable **quartic** Hénon–Heiles Hamiltonians, construct their actual Eisenhart metric from each mechanical potential and compare its Killing-tensor hierarchy with H352/H403 elliptic-pencil data.
2. [O2] Determine whether the historical H403 projective quartic equivalence can be lifted to an explicit map of selected **separated** Hamiltonian subsystems and marked holomorphic time differentials, beyond an equality of $`j`$.
3. [O3] Investigate the special $`j=1728`$ meeting of the surface fundamental-form quartic and the Master/Hénon–Heiles quartic: identify an explicit isomorphism of smooth elliptic double covers, and rigorously test whether any geometric differential or period is preserved.
4. [O4] Determine whether a natural trace-free Hessian quadratic differential on the Jacobi surface has a global holomorphic extension for any integrable HH case; generic Hessian data are not holomorphic without extra equations.
5. [O5] Construct, if possible, a concrete rank-two $`(2,3,5)`$ distribution from a **specified** HH ODE or rank-three Pfaffian system, then compute the Cartan quartic. Do not equate it with the Weyl or spectral quartic before calculation.
6. [O6] Classify how the preferred null Weitzenbock torsion and the tidal quartic transform under local Lorentz/frame rotations accompanied by flat spin-connection transformations; distinguish covariant invariants from pure-coframe artifacts.
7. [O7] Study integrable HH Killing tensors and the associated symmetric-power/projective structures, including whether the archived quartic Hessian pencil admits a natural connection-theoretic realization with an explicit differential map.
8. [O8] Compare a generic Hénon–Heiles potential's Jacobi-metric teleparallel curvature relation with the canonical catenoid's torsion-curvature syzygy, retaining the fixed-energy Hill region and mechanical clock.
9. [O9] Investigate magnetic Eisenhart extensions **within their actual aligned-null metric class**, calculate their Petrov scalars and invariants first, and only then ask which alterations yield nonzero Weyl I,J.

## 23. External references and historical attribution

**Project ZIP:** The exact H403 coupling-form pencil, its Master map, discriminant and $`j`$ appear in 04-follow-ups/binary-quartics-hessian-hh-s4.md and are also cross-checked in 04-follow-ups/binary-quartic-pencils.md (H352–H358). The surface fundamental-form quartic is in 04-follow-ups/fundamental-forms-willmore-hopf.md (H421); its catenoid specialization and associate family are H424. The catenoid's teleparallel torsion-curvature identity, the gauge distinction, and four-dimensional warped scalar dictionary are in the recent live drafts 030 and 040. Historical ledger check status [V] is not a blanket proof of every physical or spectral interpretation.

**External mathematical literature [K]:**

- *Eisenhart lift of 2-dimensional mechanics*, European Physical Journal C **79** (2019): https://link.springer.com/article/10.1140/epjc/s10052-019-6812-6 . Includes the Hénon–Heiles potential, lifted metric and Brinkmann geometry.
- *Geometry of Hamiltonian Dynamics with Conformal Eisenhart Metric* (2011): https://onlinelibrary.wiley.com/doi/10.1155/2011/710274 . Eisenhart/Jacobi curvature and deviation methods in Hamiltonian dynamics.
- Classical invariant theory lecture notes: https://www.math.utoronto.ca/~ila/ClassicalInvariantTheory.pdf . Binary quartic invariant algebra and discriminant root classification.
- Petrov invariants and quartic spinor normalization: https://homepage.villanova.edu/robert.jantzen/research/articles/ijgmmp2022.pdf ; see also the standard Petrov literature.
- Generalized Hénon–Heiles integrability and algebraic geometry: https://www.sciencedirect.com/science/article/pii/S0393044014000059 ; https://arxiv.org/abs/nlin/0507011 . Genus-two/spectral structures belong to specific integrable Hamiltonians.
- Cartan harmonic quartic of $`(2,3,5)`$ distributions and its exceptional algebraic role: https://pmc.ncbi.nlm.nih.gov/articles/PMC6560648/ ; https://link.springer.com/article/10.1007/s10711-021-00665-4 . The latter treats a specific correspondence with Weyl quartics of constructed para-Kähler–Einstein twistor structures, not arbitrary mechanical systems.
- Teleparallel connection/contorsion geometry with covariant flat spin connections: https://www.mdpi.com/2218-1997/7/5/114 ; https://link.springer.com/article/10.1140/epjc/s10052-021-09944-6 .
- The current GitHub drafts [SF-DRAFT-030](030%20Connections%20and%20Differential-Geometric%20Operators%20of%20the%20Canonical%20Surface.md) and [SF-DRAFT-040](040%20Weitzenbock%20and%20Levi-Civita%20Friedmann%20Dictionaries.md) remain provisional source dependencies.

**Final mathematical result:** Levi-Civita curvature, Weitzenbock torsion, and binary quartic invariant theory are linked by **explicit constructions**, not by a universal equivalence of their scalar invariants. The canonical catenoid supplies a nontrivial smooth $`j=1728`$ surface quartic reconstructed from curvature or chosen torsion derivatives. The Hénon–Heiles Eisenhart lift supplies a different, type-N Weyl quartic with vanishing I and J despite a nonzero Hessian, and a constructed tidal quartic with generally nonzero invariants. The historical HH/Master pencil independently supplies a nonconstant elliptic $`j`$ and genuine projective equivalence. The new structural gain is understanding exactly which geometry creates each quartic, which derivatives and connection choices enter, and what information is lost under each projection.
