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
