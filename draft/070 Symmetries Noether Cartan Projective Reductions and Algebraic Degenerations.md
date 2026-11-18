---
id: SF-DRAFT-070
title: Symmetries, Noether, Cartan, Projective Reductions, and Algebraic Degenerations
status: provisional
created: 2026-11-18
proposed_layers: [I, II, III, IV]
depends_on: [SF-I-000, SF-I-010, SF-I-020, SF-DRAFT-010, SF-DRAFT-020, SF-DRAFT-030, SF-DRAFT-040, SF-DRAFT-050, SF-DRAFT-060]
related_claims: [F04, F08, S02, S09, H173, H174, H175, H176, H320, H321, H322, H323, H324, H325, H326, H327, H328, H352, H353, H403, H421, H424, H427, H429]
---

# 070 Symmetries, Noether, Cartan, Projective Reductions, and Algebraic Degenerations

**Research status:** Provisional mathematical investigation. This draft does not assert that one mathematical formalism physically realizes another. [D] denotes an explicit derivation, [V] independent symbolic verification, [K] established mathematics, [H] an archived project result retaining its recorded verification level, [C] a correction or counterexample, and [O] an open question. The aim is to identify **typed mathematical maps** rather than infer identities from repeated names, curves or symmetry groups.

**Source provenance:** The user's current attachment, Pasted text(20261118-185303).txt (368 lines), was inspected directly and used as a collection of proposed insights; its assertions were **not presumed verified**. Current GitHub main branch: SF-I-020 and drafts 020, 030, 040, 050, 060, plus the draft index. Historical uploaded ZIP symmetrical-framework-update-2026-11-18-bu.zip: 04-follow-ups/spinning-tops-henon-heiles-double-wells.md (H320–H328), coupled-oscillator-and-modular-clock.md (H307–H312), binary-quartic-pencils.md (H352–H358), fundamental-forms-willmore-hopf.md (H421–H428), conformal-and-probabilistic-readings.md (H173–H176), its 00-meta claims register and the verification scripts. External mathematical references and separate new computations are identified below. The ZIP is a historical snapshot, not the current GitHub layout.

**Main conclusion:** The foundational framework is best organized by a **typed, information-aware algebro-geometric interface**: first specify manifold, metric, connections, bundle, action, symmetry, differential operator, energy surface and clock; then apply exact operations such as curvature/contorsion reconstruction, Noether reduction, Cartan development, projectivization, Hopf/symplectic quotient, elliptic-curve normalization, and stochastic ground-state conjugacy. These operations may deliver the same ordinary differential expression in different settings **without** making the settings, boundary data, physical models or variational principles equivalent. In particular, the attachment's universal trichotomies and automatic identifications of torsion, I/J quartics and stochastic conserved charges have counterexamples.

## 1. The mathematical meaning of “the map is not the territory”

An equation is not an application, and an application is not its geometric realization. A useful correspondence must state:

1. **Source object:** metric and dimension, or symplectic manifold/Hamiltonian, or operator domain, or probability space/generator, etc.
2. **Target object:** a scalar ODE, energy curve, projected Gauss map, Lie algebra orbit, conformal metric, stochastic diffusion, etc.
3. **Map:** a change of coordinate, projectivization, gauge change, time reparametrization, symplectic quotient, affine connection change, or conjugacy of operators.
4. **Preserved data:** curvature tensor, symplectic form, first integral, scalar differential expression, root cross-ratio, period, stationary measure, etc.
5. **Lost/changed data:** global topology, marked periods, real slice, time variable, analytic domain, bundle, source matter, noise, physical interpretation.
6. **Converse conditions:** whether the original object can be reconstructed, and what boundary/gauge/normalization must be supplied.

Equal second-order equations or equal elliptic modular invariants do not generally imply equal geometries or equal applications. Conversely two different connections can provide equally valid descriptions of a selected metric once their contorsion is stated.

The classical Kepler/oscillator example is an apt analogy: planar Levi-Civita and three-dimensional Kustaanheimo–Stiefel regularizations relate selected **energy-restricted** Kepler trajectories to harmonic-oscillator trajectories through a dimension-changing transformation, a fiber constraint, and a time change. In the hydrogen Schrödinger problem, related oscillator formulations also carry quantum constraints and operator-domain data. This is a precise correspondence, not an identification of the Kepler problem, a laboratory oscillator and the hydrogen atom as the same physical object. See §21 for the formal checklist.

## 2. Canonical framework data and the distinction between source and auxiliary clocks

Keep all canonical parameters explicit:

```math
r>0,\qquad c>0,\qquad\mu>0,\qquad x>0,\qquad u=\ln(x/c),\qquad\theta=ru.
```

The canonical scalar fields are

```math
S=\mathrm{sech}(ru),\qquad W=\tanh(ru),\qquad R=\cosh(ru),\qquad S_u=-rSW,\qquad W_u=rS^2,\qquad S^2+W^2=1.
```

The original normalized Master field is

```math
y=2xf_\mu=S/\sqrt{\mu},\qquad y_{uu}=r^2y-2\mu r^2y^3.
```

The conserved nonlinear energy is

```math
\varepsilon_N=y_u^2-r^2y^2+\mu r^2y^4,\qquad e=\mu\varepsilon_N/r^2.
```

The associated normalized energy curve is

```math
z_u^2=r^2(e+z^2-z^4),\qquad z=\sqrt\mu\,y.
```

Use different symbols for separate mechanical time $t$, stochastic time $s$, a surface complex coordinate $\zeta=u+iv$ and a three-dimensional spatial curvature $K_3$. Equating any of those variables with $u$ requires an explicit pullback. For autonomous systems the constant resolution $r$ can scale a clock, but this does not preserve every physical or probabilistic normalization.

## 3. Second order does not intrinsically mean nonzero curvature or torsion [D,C]

The supplied attachment proposes that the connection underlying a second derivative is “completely determined by curvature and torsion”, and that nearly every second-order equation directly measures one of those quantities. Both assertions are too strong.

An affine connection $\nabla$ provides a covariant Hessian and acceleration, but **connection coefficients are additional local data**. Its curvature and torsion are derived tensors. In particular, for any connection on a one-dimensional manifold, curvature and torsion are identically zero by antisymmetry, yet one may pose arbitrarily different nonlinear ODEs on the same flat line:

```math
\ddot q+\omega^2q=0,\qquad \ddot q-\alpha q+\beta q^3=0,\qquad \omega,\alpha,\beta>0.
```

Neither equation has its restoring force determined by a nonzero Levi-Civita curvature or torsion. An external potential, an action, a prescribed vector field or another constitutive law must be added. Even on a higher-dimensional flat manifold, distinct smooth potentials generate arbitrarily different second-order equations with the **same** metric curvature and the same chosen zero-torsion connection.

### 3.1 The exact two-connection difference

Given a metric $g$ and a chosen flat metric-compatible Weitzenbock connection $\widetilde\nabla$, let $\mathring\nabla$ be its Levi-Civita connection and define contorsion in the explicit convention

```math
C(X,Y)=\widetilde\nabla_XY-\mathring\nabla_XY,\qquad \widetilde\nabla=\mathring\nabla+C.
```

The tensorial curvature identity is

```math
0=R(\widetilde\nabla)=R(\mathring\nabla)+D_{\mathring\nabla}C+C\wedge C.
```

A kinetic-energy extremal is a Levi-Civita geodesic, so in the alternate connection it satisfies

```math
\mathring\nabla_{\dot\gamma}\dot\gamma=0\quad\Longleftrightarrow\quad\widetilde\nabla_{\dot\gamma}\dot\gamma=C(\dot\gamma,\dot\gamma).
```

The torsion tensor is antisymmetric in its two input vectors and therefore

```math
\mathcal T(\dot\gamma,\dot\gamma)=0.
```

**Correction [C]:** It is false that the geodesic “torsion force” can generally be written $\mathcal T^k{}_{ij}\dot x^i\dot x^j$; that expression is identically zero. The correct velocity-quadratic correction is the **symmetric-in-the-two-velocities part of contorsion**, including its dependence on the full torsion tensor. Standard kinetic Euler–Lagrange equations select $\mathring\nabla$, while autoparallels of $\widetilde\nabla$ require an additional modeling rule or a different variational principle.

### 3.2 Curvature and torsion are not gauge labels for unrelated theories

The zero curvature of $\widetilde\nabla$ is an identity of **that chosen connection**. It does not make the independent Levi-Civita curvature of the same metric zero. Conversely the same metric can admit multiple flat compatible connections and inequivalent torsion tensors. The local coframe, flat spin connection, and their simultaneous frame transformations must be tracked.

For the actual canonical catenoid, draft 030 proves the selected tangent teleparallel frame identity

```math
K_{\rm cat}=-e_1(t_2)-t_2^2=-r^2S^4,\qquad t_2=rSW.
```

This is a precise, nontrivial **specific geometric instance**, not a theorem that any ODE can be read from torsion alone.

## 4. The geometric Noether theorem and its scope [K,D]

Suppose an ordinary differentiable action has Lagrangian $L(q,\dot q,t)$, momenta $p_i=\partial L/\partial\dot q^i$, and admits a continuous symmetry with infinitesimal generator $(\delta t,\delta q)$ whose Lagrangian variation is a total derivative $dF/dt$. Noether's theorem gives a conserved expression on Euler–Lagrange solutions:

```math
Q=\sum_i p_i\delta q^i-\left(\sum_i p_i\dot q^i-L\right)\delta t-F.
```

This is a conditional variational theorem: a metric Killing vector, a preserved differential operator, a topological Chern number and a stochastic martingale are **not automatically the same kind of charge**. Their conservation arguments and required assumptions differ.

### 4.1 Geodesic Killing momenta

For the metric kinetic Lagrangian $L_g=\tfrac12 g(\dot\gamma,\dot\gamma)$ and a Killing vector $K$ with $\mathcal L_Kg=0$, define

```math
Q_K=g(\dot\gamma,K).
```

Along an affinely parametrized Levi-Civita geodesic,

```math
\frac{dQ_K}{dt}=g(\mathring\nabla_{\dot\gamma}\dot\gamma,K)+\frac12(\mathcal L_Kg)(\dot\gamma,\dot\gamma)=0.
```

For a natural mechanical Lagrangian $L_g-V$, the same charge is conserved **only if** $K(V)=0$:

```math
\frac{dQ_K}{dt}=-K(V).
```

This distinction already disproves the attachment's implication that a metric isometry alone preserves the same momentum for **all** added forces. In a chosen teleparallel frame the equality can be rewritten through contorsion; that rewriting does not create an independent Noether symmetry.

## 5. Wronskians are symplectic boundary currents, not universally metric charges [D,K]

Consider the scalar Sturm–Liouville equation for a fixed real $\lambda$,

```math
-(py')'+q_0y=\lambda wy,\qquad p>0,\quad w>0.
```

Let $y_1,y_2$ be two solutions of the **same** equation and spectral parameter. Multiply the first equation by $y_2$, the second by $y_1$, subtract and integrate once:

```math
\frac d{dx}\left[p(y_1y_2'-y_1'y_2)\right]=0.
```

Thus the weighted Wronskian

```math
\mathscr W_p=p(y_1y_2'-y_1'y_2)
```

is constant on a common regularity interval.

### 5.1 Canonical symplectic interpretation

Define $P=py'$ and the phase vector $Z=(y,P)^T$. It satisfies a traceless first-order system

```math
Z'=\begin{pmatrix}0&p^{-1}\\q_0-\lambda w&0\end{pmatrix}Z.
```

For two solution vectors $Z_1,Z_2$ the symplectic area is

```math
Z_1^TJZ_2=y_1P_2-P_1y_2=\mathscr W_p,\qquad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
```

The coefficient matrix obeys $A^TJ+JA=0$, so its fundamental matrices preserve the alternating bilinear form. This is the concrete source of Wronskian conservation.

It can also be obtained as the **presymplectic current** of the quadratic variational problem, comparing two linearized solutions, but should not be described without qualification as a Noether charge of an arbitrary global $SL(2,\mathbb R)$ *symmetry of the background potential*. The space of solutions carries an alternating symplectic pairing; the underlying variable-coefficient operator need not have a three-dimensional Lie algebra of physical symmetries.

### 5.2 Ermakov–Pinney's quadratic determinant is another invariant

For the linear pair $\psi_\pm=e^{\pm ru/2}$ with Wronskian $\mathscr W=-r$, choose a Gram quadratic $G=AX^2+2CXZ+BZ^2$ and set $Y^2=G(\psi_+,\psi_-)$. As in draft 060,

```math
Y_{uu}=\frac{r^2}{4}Y+r^2(AB-C^2)Y^{-3}.
```

The quadratic determinant $\Delta_G=AB-C^2$ is not the binary-quartic $I,J$ of the Master energy. The artificial quartic $G^2$ has nonzero raw $I,J$ for $\Delta_G\ne0$ but **discriminant zero for every** Gram form. The associated Pinney energy in the centered autonomous case is

```math
E_{\rm EP}=\frac12Y_u^2-\frac{r^2}{8}Y^2+\frac{r^2(AB-C^2)}{2Y^2}=-\frac{r^2}{2}C.
```

The equality follows from the Gram first integral and shows exactly how a quadratic invariant and a dynamical energy enter distinct algebraic roles.

## 6. Minimal-surface flux is an exact geometric Noether current [D,K,H421,H424]

Let $X:\Sigma\to\mathbb R^3$ be a conformal minimal immersion and take the Hodge star of its induced oriented metric. The coordinate functions of $X$ are harmonic:

```math
\Delta_\Sigma X=0,\qquad d(*dX)=0.
```

The vector-valued closed one-form $*dX$ therefore determines a period/flux homomorphism on closed curves:

```math
\mathrm{Flux}([\gamma])=\oint_\gamma *dX\in\mathbb R^3.
```

The value is invariant under homology of cycles in the regular domain; it is also the translation Noether flux associated with stationarity of the area functional. The corresponding rotational currents involve additional factors of the immersion $X$. These fluxes are not generally equal to the complex elliptic period lattice of a Gauss-map quartic, although particular Weierstrass representations relate them.

### 6.1 Exact catenoid neck flux in the canonical scale

Use the catenoid immersion with real angular coordinate $v$ of period $2\pi/r$:

```math
X(u,v)=\left(r^{-1}\cosh(ru)\cos(rv),\,r^{-1}\cosh(ru)\sin(rv),\,u\right),\qquad v\sim v+2\pi/r.
```

Its coordinate tangent fields satisfy

```math
|X_u|^2=|X_v|^2=R^2,\qquad X_u\cdot X_v=0,\qquad I=R^2(du^2+dv^2),\qquad R=\cosh(ru).
```

With orientation $du\wedge dv$, $*du=dv$ and $*dv=-du$, hence

```math
*dX=X_u\,dv-X_v\,du.
```

At fixed $u$, integrate over one full neck:

```math
\oint_{v=0}^{2\pi/r}*dX=\left(0,0,\frac{2\pi}{r}\right).
```

**Proof.** $X_u=(\sinh(ru)\cos(rv),\sinh(ru)\sin(rv),1)$; its first two components integrate to zero over a period, and the last integrates to $2\pi/r$. The result is independent of the chosen $u$, as it must be because $d*dX=0$.

This exact flux is determined by the chosen immersion scale and orientation. It illustrates a genuinely conserved **surface current** that is different from the Wronskian, the Master energy and a gauge Chern number.

### 6.2 Bonnet rotation is not a curvature-to-torsion exchange

The catenoid and helicoid are locally isometric minimal associates. On a simply connected parameter domain, their Weierstrass data can share the meromorphic Gauss map while rotating the height differential by a complex phase. Their first fundamental forms coincide, and the second fundamental forms rotate in tangent coordinates.

Therefore it is wrong to call one “curvature only” and the other “torsion only”: the two have the **same nonzero Gaussian curvature** and each admits both Levi-Civita and selected teleparallel descriptions. Their periods, embeddedness and global quotients can differ.

## 7. Critical Yamabe, dilation and Pohozaev: symmetry does not fix bubble scale [D,K,H173]

The Euclidean critical Yamabe equation in dimension $D>2$ is

```math
-\Delta U=\kappa U^p,\qquad p=\frac{D+2}{D-2},\qquad \kappa>0.
```

Under sufficient decay, multiply by $U$ and integrate by parts:

```math
\int_{\mathbb R^D}|\nabla U|^2\,dX=\kappa\int_{\mathbb R^D}U^{p+1}\,dX.
```

The Pohozaev identity for a sufficiently regular decaying whole-space solution is

```math
\frac{D-2}{2}\int|\nabla U|^2\,dX=\frac{D\kappa}{p+1}\int U^{p+1}\,dX.
```

But at the critical exponent

```math
\frac D{p+1}=\frac{D-2}{2}.
```

Thus the two integral equations coincide identically: the Pohozaev constraint is compatible with the **entire continuous scale orbit**, not an equation selecting one bubble size.

### 7.1 An explicit counterexample to “Pohozaev locks the bubble scale”

Choose an Aubin–Talenti family normalized to the equation:

```math
U_{\lambda,X_0}(X)=\left[\frac{D(D-2)}{\kappa}\right]^{(D-2)/4}\left(\frac{\lambda}{1+\lambda^2|X-X_0|^2}\right)^{(D-2)/2},\qquad\lambda>0.
```

Each positive member solves the same critical equation and satisfies the same Pohozaev integral equality. Changing $\lambda$ does not violate either identity. The scale is a modulus of the conformal symmetry, not a number pinned down by a universal Noether charge.

The corresponding radial Emden–Fowler critical profile leads, after the framework's explicit logarithmic substitution $u=\ln(x/c)$ and a normalization, to a $\mathrm{sech}^{q}$ profile and a Pöschl–Teller Hessian (draft 060). This is a proved reduction with specified dimension and clock, not an automatic consequence of every surface or quartic.

## 8. BPST and Eguchi–Hanson: topological characteristic classes are not Noether charges of a flat frame [K,D,C]

For a **specified nonflat** Lie-algebra-valued SU(2) connection $A$, its curvature is

```math
F_A=dA+A\wedge A.
```

On a compact oriented four-manifold with appropriate bundle and trace normalization, the second Chern number is

```math
k=-\frac{1}{8\pi^2}\int\mathrm{tr}(F_A\wedge F_A)\in\mathbb Z.
```

The value is topological and invariant under smooth continuous deformations of the connection that preserve the bundle and boundary data. It is obtained through Chern–Weil theory, **not** from every local continuous isometry's Noether theorem. On noncompact domains, finite-action and asymptotic trivialization hypotheses are needed to interpret boundary integrals.

The BPST solution has $F_A\ne0$ and is (anti-)self-dual after choosing an orientation. A pure-gauge SU(2) Maurer–Cartan connection $A=g^{-1}dg$ has $F_A=0$ locally. A flat Lorentz Weitzenbock spin connection also has **zero connection curvature**, but may have a nonzero torsion tensor once a coframe is chosen. These are three different bundle/connection data types.

Eguchi–Hanson is a Ricci-flat nonflat hyperkähler metric whose characteristic numbers are computed from its Riemannian curvature and global topology. It cannot be assigned the same gauge Chern number as BPST merely because both possess a self-duality statement or because their radial formulas share a hyperbolic function. Its local complex Monge–Ampere/Pinney reduction was proved separately in draft 060.

### 8.1 The exact density correspondence that really survives

For the matched four-dimensional stereographic Aubin–Talenti bubble and BPST connection,

```math
U(\rho)=\frac{c}{\sqrt\mu(\rho^2+c^2)},\qquad |F_{\rm BPST}|^2=\frac{192c^4}{(\rho^2+c^2)^4}=192\mu^2U^4.
```

This is an **equality of scalar densities after specifying coordinate, normalization and scale**, not an equality of their connections, bundle curvatures, field equations or action functionals. Draft 060 separately derives the shared charge polynomial $3P^2-2P^3$ and its real Monge–Ampere mass-transport interpretation.

## 9. Euler–Lagrange, Palatini and action equivalence [K,D,C]

The user attachment correctly emphasizes that a variational functional supplies a crucial missing arrow between geometric data and an equation. Its suggestion that *all* metric, Palatini and tetrad variations form one universally equivalent calculus is too broad.

### 9.1 Ordinary kinetic action

For a metric $g$, the functional

```math
\mathcal A[\gamma]=\frac12\int g_{\gamma(t)}(\dot\gamma,\dot\gamma)\,dt
```

has Euler–Lagrange equation $\mathring\nabla_{\dot\gamma}\dot\gamma=0$, with fixed endpoints. This is independent of whether one later chooses a different flat torsionful connection on the same metric. Section 3 gives the exact contorsion rewrite.

### 9.2 The projective subtlety in unconstrained Einstein–Hilbert–Palatini variation

Consider an independent metric and a **completely general** affine connection in a Palatini action linear in the connection's Ricci scalar. In the conventional zero-hypermomentum vacuum setting, the stationary connections are not necessarily uniquely Levi-Civita: the action is projectively invariant.

In our coordinate convention $\nabla_{\partial_\mu}\partial_\nu=\Gamma^\lambda{}_{\mu\nu}\partial_\lambda$, one projective family can be written

```math
\Gamma^\lambda{}_{\mu\nu}=\mathring\Gamma^\lambda{}_{\mu\nu}+\delta^\lambda_\nu A_\mu.
```

The curvature changes by a term proportional to the exact two-form $dA$, so the scalar Ricci contraction remains unchanged. The induced torsion is generally nonzero:

```math
\mathcal T^\lambda{}_{\mu\nu}=\delta^\lambda_\nu A_\mu-\delta^\lambda_\mu A_\nu.
```

Thus *unconstrained* Palatini variation does not simply “force torsion to vanish” or select a unique connection. Imposing torsion-free symmetry in advance, fixing projective gauge or changing matter couplings alters the solution statement. The precise nonuniqueness is an established result; see the literature references in §22.

### 9.3 Linear teleparallel versus nonlinear actions

With a chosen coframe and flat compatible Lorentz spin connection, the **linear** teleparallel scalar density differs from the Levi-Civita scalar density by a total divergence:

```math
\mathring{\mathcal R}=-\mathbb T+\mathbb B.
```

This yields the usual linear bulk variational equivalence under compatible boundary assumptions. Nonlinear functionals $f(\mathbb T)$, $f(\mathbb T,\mathbb B)$ and $f(\mathring{\mathcal R})$ generally have distinct Euler–Lagrange operators unless a specific functional identity and boundary conditions are imposed. Nor does Einstein–Hilbert variation by itself derive the Yamabe, Monge–Ampere, BPST and Fokker–Planck equations: these require **their own** scalar, Kähler, gauge or stochastic functionals.

## 10. Two meanings of “Cartan flat”: constant-curvature model versus teleparallelism [K,D,C]

Let $(M,g)$ be a torsion-free pseudo-Riemannian space form with sectional curvature $k$. In an orthonormal coframe $\vartheta^a$ and its Levi-Civita spin connection $\omega^a{}_b$, the Cartan structure equations are

```math
T^a=d\vartheta^a+\omega^a{}_b\wedge\vartheta^b=0,\qquad R^{ab}(\omega)=k\,\vartheta^a\wedge\vartheta^b.
```

In a reductive Cartan geometry modeled on the appropriate homogeneous de Sitter or anti-de Sitter space, combine the spin connection and the coframe into a **larger-group** Cartan connection. With a convention depending on the sign of $k$, its Lorentz part has curvature

```math
\mathcal F^{ab}=R^{ab}(\omega)-k\,\vartheta^a\wedge\vartheta^b,\qquad \mathcal F^a=T^a.
```

The homogeneous space-form model has **flat Cartan curvature** $\mathcal F=0$, even though the *Lorentz subconnection* has nonzero curvature $R^{ab}=k\vartheta^a\wedge\vartheta^b$ and zero torsion.

**Important correction:** Flatness of this **larger-group Cartan connection** is **not** the definition of a Weitzenbock connection. A Weitzenbock affine/Lorentz connection is flat with respect to its own smaller structure group and typically has nonzero torsion from a chosen coframe. The two zero-curvature statements refer to **different connections and bundles**.

### 10.1 Exact four-dimensional space-form scalar checks

For de Sitter space in its flat expanding chart with $H=1/L$ constant, the preferred diagonal Weitzenbock tetrad of draft 040 has

```math
\mathring{\mathcal R}_{\mathrm{dS}}=12/L^2,\qquad \mathbb T_{\mathrm{dS}}=6/L^2,\qquad \mathbb B_{\mathrm{dS}}=18/L^2.
```

For anti-de Sitter space in a Poincare chart, choose the local conformal coframe $g=(L^2/z^2)\eta$ with spacelike $z>0$ and flat zero-spin Weitzenbock gauge. The conformal formula in draft 060 gives

```math
\mathring{\mathcal R}_{\mathrm{AdS}}=-12/L^2,\qquad \mathbb T_{\mathrm{AdS}}=-6/L^2,\qquad \mathbb B_{\mathrm{AdS}}=-18/L^2.
```

**Verification.** For AdS $h=\ln(L/z)$, so $e^{-2h}|\nabla_0h|^2=1/L^2$. Use the four-dimensional conformal teleparallel formulas and $\mathring{\mathcal R}=-\mathbb T+\mathbb B$. For de Sitter use constant $H=1/L$ in the flat-warped formulas. These are **local frame choices** on different coordinate patches, and neither requires a gravitational field equation.

They show exactly why the three labels “curvature only”, “mixed”, “torsion only” cannot be identified with dS/AdS/Minkowski: the same dS or AdS metric admits a torsion-free Levi-Civita representation and the chosen flat torsionful teleparallel representation. Minkowski in a Cartesian coframe has both curvature and torsion zero, while an accelerated Rindler zero-spin coframe can have torsion components nonzero even with vanishing Levi-Civita curvature (draft 040).

## 11. The exact sl(2) elliptic/hyperbolic/parabolic trichotomy—and what it does not classify [D,V,K]

Let $A$ be a **constant** real traceless two-by-two matrix:

```math
A=\begin{pmatrix}a&b\\c&-a\end{pmatrix},\qquad \det A=-a^2-bc,\qquad A^2=-\det(A)\,\mathbf1.
```

Its characteristic polynomial is $\lambda^2+\det A$. By the Cayley–Hamilton identity, the exponential is a linear combination of $\mathbf1$ and $A$ and has three distinct real cases.

- **Elliptic:** $\det A=\omega^2>0$. Then $A^2=-\omega^2\mathbf1$ and

```math
e^{tA}=\cos(\omega t)\mathbf1+\frac{\sin(\omega t)}{\omega}A.
```

- **Hyperbolic:** $\det A=-\lambda^2<0$. Then $A^2=\lambda^2\mathbf1$ and

```math
e^{tA}=\cosh(\lambda t)\mathbf1+\frac{\sinh(\lambda t)}{\lambda}A.
```

- **Parabolic/nilpotent:** $\det A=0$, $A\ne0$. Then $A^2=0$ and

```math
e^{tA}=\mathbf1+tA.
```

The **zero matrix** is a separate orbit, not the nonzero nilpotent orbit. For nonconstant $A(t)$ the solution requires a path-ordered fundamental matrix; a pointwise determinant sign is insufficient to give the global solution or a monodromy classification.

### 11.1 Why this trichotomy does not equal “curvature only / mixed / torsion only”

All three choices above can occur for **linear ODE systems on the flat line**, where both affine curvature and torsion vanish identically. Conversely the same curved metric may be equipped with either the Levi-Civita or a chosen Weitzenbock connection without changing the associated *constant* projective coefficient matrix of an independently selected ODE.

Therefore the assertion that elliptic equals Levi-Civita-only, hyperbolic equals mixed curvature/torsion, and parabolic equals Weitzenbock-only is refuted by elementary examples. These are different, equally useful classification axes.

### 11.2 Riccati projectivization is the actual bridge

Let $\Psi' = A(u)\Psi$ for $A(u)=\begin{pmatrix}a&b\\c&-a\end{pmatrix}$. On a chart with $\psi_2\ne0$, define $g=\psi_1/\psi_2$. Direct differentiation gives

```math
g_u=b+2ag-cg^2.
```

A constant diagonal matrix $A=\mathrm{diag}(r/2,-r/2)$ gives $g_u=rg$ and $g(u)=g_0e^{ru}$. A nilpotent matrix $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ gives $g_u=1$ and $g=u+g_0$.

For the hyperbolic exponential ratio,

```math
\{g,u\}=-r^2/2,\qquad g=e^{ru}.
```

For the parabolic ratio $g=u$, $\{g,u\}=0$. This is a **projective Schwarzian statement** about the chosen rank-two system, not a statement that one metric has nonzero torsion and the other has none.

The Gudermannian identity $\mathrm{gd}(s)=2\arctan(e^s)-\pi/2$ relates particular real hyperbolic and circular coordinate functions, but is **not** a universal conjugation between arbitrary elliptic and hyperbolic matrices or their global spectra.

## 12. The quartic discriminant and the sl(2) nilpotent cone are different algebraic varieties [D,V,K,C]

The current repository uses the **raw binary quartic** form

```math
F(X,Z)=aX^4+bX^3Z+c_2X^2Z^2+dXZ^3+fZ^4.
```

Its raw invariants and discriminant are

```math
I_{\rm raw}=12af-3bd+c_2^2,\qquad J_{\rm raw}=72ac_2f+9bc_2d-27ad^2-27fb^2-2c_2^3,\qquad \Delta_F=(4I_{\rm raw}^3-J_{\rm raw}^2)/27.
```

In binomial/spinor coordinates $F=\psi_0X^4+4\psi_1X^3Z+6\psi_2X^2Z^2+4\psi_3XZ^3+\psi_4Z^4$, the corresponding scalings are

```math
I_{\rm raw}=12I_b,\qquad J_{\rm raw}=432J_b,\qquad \Delta_F=256(I_b^3-27J_b^2).
```

For a **binary quartic**, $\Delta_F=0$ is the algebraic locus of a repeated projective root. The **GIT null cone** $I_b=J_b=0$ is a smaller locus; its nonzero quartics have a root of multiplicity at least three. The quartic discriminant variety and the two-dimensional matrix nilpotent cone $\det A=0$ are **not canonically the same variety**.

### 12.1 Three explicit root-pattern controls

- A quartic with two double roots,

```math
F_1=X^2Z^2,\qquad I_{\rm raw}(F_1)=1,\qquad J_{\rm raw}(F_1)=-2,\qquad \Delta(F_1)=0.
```

- A quartic with one triple and one simple root,

```math
F_2=X^3Z,\qquad I_{\rm raw}(F_2)=J_{\rm raw}(F_2)=0,\qquad \Delta(F_2)=0.
```

- A quartic with four distinct complex roots and smooth elliptic modulus,

```math
F_3=X^4+Z^4,\qquad I_{\rm raw}(F_3)=12,\qquad J_{\rm raw}(F_3)=0,\qquad \Delta(F_3)=256,\qquad j(F_3)=1728.
```

These examples show that $\Delta=0$ neither forces four equal roots nor implies $I=J=0$, and $I=J=0$ does not force a **quadruple** root (the triple-root example suffices).

A smooth elliptic curve has $j=0$ when the appropriate $I$ vanishes **but the discriminant remains nonzero**, typically $I=0,J\ne0$; the pair $I=J=0$ cannot be inserted into the smooth elliptic $j$ formula. Drafts 050 and 060 make the same distinction for Weyl Petrov quartics and Gram-squared quartics.

### 12.2 Degree-three polynomial and its singular parameter are not a Jordan form

For the normalized Master energy,

```math
p^2=e+z^2-z^4,\qquad I_e=1-12e,\qquad J_e=-2(1+36e),\qquad\Delta_e=-16e(1+4e)^2.
```

At $e=0$ this is a singular energy curve admitting the homoclinic separatrix $z=\mathrm{sech}(ru)$; at generic nonzero energy it is a smooth genus-one curve. This is an exact *energy-curve* degeneration. It does not mean the associated Levi-Civita or Weitzenbock connection changes from elliptic to a nilpotent matrix orbit.

## 13. The double-well Duffing quartic: complete invariant correction [D,V,H320–H324]

The supplied text correctly identifies the double-well energy quartic, but mixes the quartic invariant normalizations and supplies an incorrect discriminant coefficient. Let

```math
L=\frac12\dot q^2+\frac{\alpha}{2}q^2-\frac{\beta}{4}q^4,\qquad \alpha,\beta>0.
```

Its Euler–Lagrange equation and conserved energy are

```math
\ddot q-\alpha q+\beta q^3=0,\qquad E=\frac12\dot q^2-\frac{\alpha}{2}q^2+\frac{\beta}{4}q^4.
```

Therefore the quartic energy curve is

```math
\dot q^2=P_E(q)=2E+\alpha q^2-\frac{\beta}{2}q^4,\qquad F_E(X,Z)=-\frac{\beta}{2}X^4+\alpha X^2Z^2+2EZ^4.
```

### 13.1 Raw quartic invariants and discriminant

**Theorem 13.1 [D,V].** In the raw coefficient normalization of §12,

```math
I_{\rm raw}=\alpha^2-12\beta E,\qquad J_{\rm raw}=-2\alpha^3-72\alpha\beta E.
```

```math
\Delta_{\rm raw}=-16\beta E(\alpha^2+4\beta E)^2.
```

In the binomial/spinorial normalization of the attachment, the corresponding quantities are

```math
I_b=\alpha^2/12-\beta E,\qquad J_b=-\alpha^3/216-\alpha\beta E/6,\qquad I_b^3-27J_b^2=-\beta E(\alpha^2+4\beta E)^2/16.
```

**Proof, step by step.**

1. The raw quartic coefficients are $a=-\beta/2$, $b=0$, $c_2=\alpha$, $d=0$, $f=2E$.
2. Substitute into $I_{\rm raw}=12af+c_2^2$ and $J_{\rm raw}=72ac_2f-2c_2^3$.
3. Expand $(4I_{\rm raw}^3-J_{\rm raw}^2)/27$ and factor:

```math
\Delta_{\rm raw}=-16\beta E(4\beta E+\alpha^2)^2.
```

4. Divide $I_{\rm raw}$ by 12 and $J_{\rm raw}$ by 432 for binomial normalization. The discriminant relation of §12 yields the displayed $1/16$ factor.

**Correction [C]:** The attachment's equation $\Delta=-\beta^2E(\alpha^2+4\beta E)^2/4$ is **not** the classical discriminant in either of these two stated normalizations.

### 13.2 Complete real energy regimes

The potential is $V(q)=-\alpha q^2/2+\beta q^4/4$, with local maxima at $q=0$ and minima at

```math
q_\pm=\pm\sqrt{\alpha/\beta},\qquad E_{\min}=-\frac{\alpha^2}{4\beta}.
```

On $E_{\min}<E<0$ the quartic has four distinct real roots and admits periodic oscillations in a chosen well. At $E=0$ it has a double root at $q=0$; the homoclinic separatrix is

```math
q_{\rm sep}(t)=\pm\sqrt{\frac{2\alpha}{\beta}}\,\mathrm{sech}(\sqrt\alpha(t-t_0)).
```

At $E>0$ it has two real roots and a complex-conjugate pair, corresponding to over-barrier oscillations. At $E=E_{\min}$ the two minima are equilibria and the quartic degenerates into two double roots. These root counts and real branch choices are stronger dynamical data than the complex elliptic $j$ alone.

### 13.3 Exact specialization to the original Master ODE

Set

```math
\alpha=r^2,\qquad \beta=2\mu r^2,\qquad t=u=\ln(x/c),\qquad q=y=2xf_\mu.
```

Then the Duffing equation is exactly the cubic Master equation and

```math
2E=y_u^2-r^2y^2+\mu r^2y^4=\varepsilon_N.
```

With $z=\sqrt\mu y$ and $e=\mu\varepsilon_N/r^2$, its quartic becomes the normalized Master curve of §12. This is a **literal identity of differential expressions under explicitly stated parameter identifications**; using the same Duffing equation elsewhere does not identify the separate physical application with the Symmetrical Function.

### 13.4 From the separatrix to a specific Pöschl–Teller linearization

Vary the trajectory as $q=q_{\rm sep}+\eta$. Linearizing gives

```math
\ddot\eta-\alpha\eta+3\beta q_{\rm sep}^2\eta=0.
```

With $s=\sqrt\alpha(t-t_0)$ and $q_{\rm sep}^2=(2\alpha/\beta)\mathrm{sech}^2s$,

```math
\eta_{ss}-\eta+6\mathrm{sech}^2s\,\eta=0.
```

Equivalently the zero mode of the shifted order-two Pöschl–Teller operator is

```math
[-\partial_s^2+1-6\mathrm{sech}^2s]\eta=0.
```

This is a direct, fully verified variational ODE connection. It does not classify every Pöschl–Teller Schrödinger operator or every stochastic Kramers problem by a single quartic discriminant.

## 14. Weierstrass data, Gauss maps and Riemann minimal examples: the missing marked differential [D,K,H421,H424]

On an oriented Euclidean minimal surface, a conformal parameter $\zeta$ makes the stereographic Gauss map $g(\zeta)$ meromorphic and the Weierstrass one-form data holomorphic/meromorphic in a compatible chart. The immersion is reconstructed by integrating a vector of one-forms and taking its real part. Both the Gauss map and a separately chosen height differential are necessary.

For a fixed convention, let $\eta$ be a meromorphic height differential. The Weierstrass one-forms can be written

```math
(\Phi_1,\Phi_2,\Phi_3)=\left(\frac12(g^{-1}-g)\eta,\,\frac{i}{2}(g^{-1}+g)\eta,\,\eta\right).
```

They satisfy the ambient null relation

```math
\Phi_1^2+\Phi_2^2+\Phi_3^2=0.
```

The immersion $X=\mathrm{Re}\int(\Phi_1,\Phi_2,\Phi_3)$ requires regularity and real-period closing conditions. Rotating $\eta$ by a unit complex phase generates the local associate family; the catenoid/helicoid conjugacy is one classical instance. The **same Gauss map** need not determine the same global immersed surface.

### 14.1 An elliptic model is not automatically the Gauss map ODE of every surface

A smooth genus-one double cover of the sphere can be specified by

```math
w^2=P_4(g),\qquad P_4(g)=g(g-a)(g+a^{-1}),\qquad a\in\mathbb C\setminus\{0\},
```

with a fourth branch point at infinity, provided the finite roots are distinct. Along the elliptic Abel parameter $\zeta=\int dg/w$, one then has $(dg/d\zeta)^2=P_4(g)$. This is an **explicit choice of differential** on a specific curve.

Not every meromorphic Gauss map on a minimal surface satisfies a first-order quartic autonomous equation in an arbitrary surface chart. One must specify the elliptic base, its degree-two meromorphic function, the Abel differential, and the immersion's height differential. The global Riemann minimal examples have additional real period and closing conditions reviewed in drafts 020 and 030.

### 14.2 The catenoid and helicoid are not “different Jordan or torsion phases”

In a common simply connected parameterization of a catenoid/helicoid associate family, the stereographic Gauss map can be normalized as $g=e^{r\zeta}$, with the phase of $\eta$ distinguishing the immersion. The associated projective relation is

```math
g_\zeta=rg,\qquad \{g,\zeta\}=-r^2/2.
```

This is hyperbolic projective evolution in the **chosen coordinate**, even though both surfaces have the same nonzero intrinsic Gaussian curvature. They cannot be classified respectively as “Levi-Civita-only curvature” and “Weitzenbock-only torsion”.

In a particular degeneration of a **specified marked elliptic family**, roots of $P_4$ may collide and the elliptic uniformization may become elementary. This does not alone imply global convergence to catenoid or helicoid: rescaling, Bonnet phase, real structure, period normalization and the immersion differential must also converge. A linear **pencil** of quartics $P_0+\lambda P_1$ is a further special structure, not a synonym for every nonlinearly parameterized family of branch points.

## 15. Euler's biquadratic correspondence and QRT curves [D,K,C,H352–H358]

A genuinely common source of **two** binary quartics is a smooth bidegree-(2,2) curve in $\mathbb P^1\times\mathbb P^1$:

```math
\mathcal C:\quad A_0(x)y^2+2A_1(x)y+A_2(x)=0,
```

where each $A_i(x)$ has degree at most two. Solving for $y$ gives

```math
y=\frac{-A_1(x)\pm\sqrt{A_1(x)^2-A_0(x)A_2(x)}}{A_0(x)}.
```

The discriminant of the **projection onto the x-line** is the quartic

```math
D_x(x)=A_1(x)^2-A_0(x)A_2(x).
```

Interchange $x,y$ and form $D_y(y)$ from the other projection. If $\mathcal C$ is smooth of bidegree (2,2), its genus is

```math
g(\mathcal C)=(2-1)(2-1)=1.
```

Each degree-two projection makes the same genus-one curve a double cover of a projective line branched at four points (counting multiplicities). Therefore the two quartic double covers have the same **abstract complex elliptic** $j$-invariant, after compactification and the appropriate coordinate/leading-coefficient normalizations.

### 15.1 The crucial limitation: equal j does not force literal equal I and J

If a quartic is multiplied by a nonzero scalar $\lambda$, its raw invariants scale by

```math
I(\lambda F)=\lambda^2I(F),\qquad J(\lambda F)=\lambda^3J(F),\qquad\Delta(\lambda F)=\lambda^6\Delta(F),
```

while its elliptic $j$ remains the same. General projective variable changes introduce further determinant weights. Thus two double-cover presentations of one smooth genus-one curve can have **equal j but different numerical raw I and J**.

Nor does the algebraic relation $D_x=A_1^2-A_0A_2$ imply the **dynamical** relation $\dot x^2=D_x(x)$. A Hamiltonian flow, choice of clock and marked differential must be added. The attachment's assertion that any coupled oscillator with two integrals automatically yields a symmetric QRT biquadratic and phase locking is not a theorem.

The archived Hénon–Heiles/Master quartic pencil, its projective transformation and modular relations are specific algebraic constructions; draft 050 already makes explicit that a quartic-pencil equivalence does not identify all mechanical Hamiltonians.

## 16. Two complex modes: the exact SU(2)–CP1 quartic mechanism [D,V,K]

A rigorous projective phase-space reduction *does* exist for a specified two-mode complex Hamiltonian. Let $z_1,z_2$ be complex canonical variables with brackets

```math
\{z_i,\bar z_j\}=-i\delta_{ij},\qquad \{z_i,z_j\}=0,\qquad N=|z_1|^2+|z_2|^2>0.
```

Define the classical Schwinger variables

```math
S_x=\frac{\bar z_1z_2+\bar z_2z_1}{2},\qquad S_y=\frac{\bar z_1z_2-\bar z_2z_1}{2i},\qquad S_z=\frac{|z_1|^2-|z_2|^2}{2}.
```

They satisfy

```math
\{S_i,S_j\}=\epsilon_{ijk}S_k,\qquad S_x^2+S_y^2+S_z^2=(N/2)^2.
```

For fixed $N$, the norm sphere is $S^3$; quotienting its common phase $U(1)$ gives

```math
S^3/U(1)=\mathbb{CP}^1\cong S^2.
```

This is the symplectic quotient at a fixed nonzero moment-map level, not merely the quotient $(\mathbb C^2\setminus\{0\})/U(1)$, which still carries a radial coordinate.

### 16.1 Two-mode quartic from an actual Hamiltonian

Choose the real two-mode mean-field Hamiltonian with hopping parameter $\tau>0$ and interaction $U$:

```math
\mathcal H=-\tau(\bar z_1z_2+\bar z_2z_1)+\frac U2(|z_1|^4+|z_2|^4).
```

On the sphere of fixed norm $N$, this becomes

```math
\mathcal H=-2\tau S_x+US_z^2+\frac{UN^2}{4}.
```

Let the conserved **reduced energy** be $h=\mathcal H-UN^2/4$ and write $z=S_z$. Then

```math
h=-2\tau S_x+Uz^2,\qquad \dot z=\{S_z,\mathcal H\}=-2\tau S_y.
```

Eliminate $S_x$ using the reduced energy and $S_y$ using the sphere identity:

```math
S_x=\frac{Uz^2-h}{2\tau},\qquad \dot z^2=4\tau^2[(N/2)^2-z^2]-(Uz^2-h)^2.
```

**Theorem 16.1 [D,V] (two-mode energy quartic).** The population-imbalance variable satisfies

```math
\dot z^2=-U^2z^4+(2Uh-4\tau^2)z^2+\tau^2N^2-h^2.
```

The proof is substitution in the identity $S_x^2+S_y^2+S_z^2=N^2/4$, not a conjectural Lie-group analogy.

### 16.2 Its actual binary quartic discriminant

The raw quartic is

```math
F_h(X,Z)=-U^2X^4+(2Uh-4\tau^2)X^2Z^2+(\tau^2N^2-h^2)Z^4.
```

A direct invariant calculation yields

```math
I_h=4(-3N^2U^2\tau^2+4U^2h^2-4Uh\tau^2+4\tau^4).
```

```math
J_h=16(Uh-2\tau^2)(-9N^2U^2\tau^2+8U^2h^2+4Uh\tau^2-4\tau^4).
```

```math
\Delta_h=256U^2\tau^4(h^2-N^2\tau^2)(-N^2U^2+4Uh-4\tau^2)^2.
```

This **explicit** energy quartic gives precise discriminant loci for the selected nonlinear two-mode model. When $U=0$ or $\tau=0$ it is singular because the quartic loses degree or becomes a square, even though the original linear or decoupled evolution remains well-defined.

At the fixed point $z=0$ and relative phase $\pi$, $h=N\tau$. In the usual repulsive-interaction convention, the linear stability changes when $UN=2\tau$; this follows by Taylor expansion of the reduced Hamiltonian near that fixed point. The **macroscopic self-trapping of a given initial condition** also depends on energy and initial phase, not solely on that single threshold.

The fixed-$N$ mean-field quartic does not automatically describe the finite-particle quantum Bose–Hubbard spectrum, which requires quantization and additional Hilbert-space data.

### 16.3 Projective dynamics is nonlinear Riccati only under additional conditions

On the chart $z_2\ne0$ define $g=z_1/z_2$. Hamilton's equations for the selected complex amplitudes give

```math
i\dot g=\tau(g^2-1)+UN\,\frac{|g|^2-1}{1+|g|^2}\,g.
```

For $U=0$ this is a holomorphic Riccati equation induced by a linear two-component system. For $U\ne0$ it contains $\bar g$ through $|g|^2$, hence is a **real-Hamiltonian nonlinear projective flow**, not an ordinary holomorphic Riccati equation with coefficients depending only on time. This is another necessary distinction between the algebraic projective coordinate and the particular differential equation imposed on it.
