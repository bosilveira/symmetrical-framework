---
id: SF-DRAFT-180
title: Weighted Geometry, Ermakov Gauges, Teleparallel Frames, and Krichever Parallel Transport
status: provisional
created: 2026-11-19
proposed_layers: [I, II, III, IV]
depends_on: [SF-I-020, SF-DRAFT-030, SF-DRAFT-080, SF-DRAFT-090, SF-DRAFT-100, SF-DRAFT-120, SF-DRAFT-130, SF-DRAFT-140, SF-DRAFT-150, SF-DRAFT-160, SF-DRAFT-170]
related_claims: [H73, H74, H76, H95, H100, H102, H136, H169, H299, H311, H312, H376, H391, H421, H424, H466, H467, H468, H469, H470]
---

# 180 Weighted Geometry, Ermakov Gauges, Teleparallel Frames, and Krichever Parallel Transport

**Status:** Provisional mathematical investigation for the draft folder. [D] direct proof; [V] independent symbolic check; [K] classical mathematics with hypotheses; [H] prior verified archive claim retaining its original scope; [C] correction or no-go; [O] open. No physical realization is inferred from equality of differential equations.

**Main question.** Does a single differential-geometric mechanism organize weighted Sturm–Liouville, local Riccati/Schwarzian, positive Ermakov–Pinney, Levi–Civita/Weitzenböck frames, Darboux, Sato–Krichever, conformal cylinders and catenoid/helicoid/Riemann minimal examples? Which maps survive as actual unitary intertwiners, connection identities and period-preserving morphisms, and which proposed arrows require additional data?

**Source audit:** The actual historical ZIP dated November 18 was reopened, especially 04-follow-ups/sato-grassmannian.md (H136), friedmann-reciprocal-envelope.md, bpst-yamabe-eguchi-hanson.md, the Riemann marked-period and Lamé modules, 00-meta/INTEGRABLE.md, NOTATION.md and CLAIMS.md. Live GitHub drafts 130–170, including the conditional theorem of draft 170, were reopened. Independent differential calculations are given below; classical sources are identified in §26.

**Core answer.** (I) Every scalar positive-coefficient Sturm–Liouville expression is a Laplace–Beltrami operator on a **weighted one-manifold**, with both metric and measure, and its self-adjoint domain remains extra data. (II) A positive EP amplitude supplies a **local constant-frequency scale/clock gauge**, whose projective expression is the exact Schwarzian chain rule. (III) Darboux factorization is a Riccati/supersymmetric factorization, NOT the Bochner–Weitzenböck identity or nonzero torsion in one dimension. (IV) On a separately chosen **two-dimensional** catenoid, teleparallel torsion reconstructs LC Gaussian curvature exactly, while angular symmetry produces a weighted Jacobi SL problem. (V) The historical rank-one Sato point and the newly proved Lamé–Riemann marked elliptic isomorphism admit a compatible dictionary with **different** spatial, spectral and moduli connections. (VI) Further Hamiltonian, Gross–Pitaevskii, PDM, FRW and Keller–Miksis equations are **typed realizations under explicit restrictions**, not one physical theory.

## 1. Canonical symbols and distinct clocks

```math
x,c,r,\mu>0,\quad u=\ln(x/c),\quad x=ce^u,\quad S=\mathrm{sech}(ru),\quad W=\tanh(ru),\quad R=\cosh(ru).
```

```math
f_\mu(x;r,c)=\frac{c^rx^{r-1}}{\sqrt\mu(c^{2r}+x^{2r})}=\frac{S}{2\sqrt\mu\,x},\quad y(u)=2xf_\mu(x)=\frac{S}{\sqrt\mu}.
```

Use $p(x),w(x),q_0(x)$ for SL coefficients, $t$ for a general Liouville coordinate, $a(t)>0$ for a Pinney amplitude, $\tau$ for its reparametrized clock, and $k_{\rm EP}$ for its inverse-cubic strength. Reserve $E$ for a selected Lamé spectral energy, $m_{\rm ell}$ for its Jacobi parameter, and $\lambda_R,k_R,A_R,g_R$ for the distinct Riemann minimal-example modulus, base coordinate, immersion scale and Gauss map. A surface angle $v$ is independent of $u$; a hierarchy time $T$ is independent of all of these. The letter $W$ is the hyperbolic kink, while a Riccati superpotential is denoted $h$ to avoid confusion. Connections $\nabla^{LC}$, $\nabla^{W}$, $\nabla^{\rm Hopf}$ and the SL carrier connection are DIFFERENT objects.

## 2. A weighted one-manifold is the exact geometric SL source [D,K]

Let $p,w>0$ be smooth on an interval $I$ and $q_0$ real. Define

```math
\mathcal Lf=\frac1w[-(pf_x)_x+q_0f],\quad\mathcal H=L^2(I,w\,dx),\quad g_{xx}=\frac wp,\quad \rho=\sqrt{pw},\quad d\nu=\rho\,d\mathrm{vol}_g=w\,dx.
```

**Theorem 2.1 [D] (metric plus measure).** The weighted Laplace–Beltrami operator for $(g,\rho)$ is

```math
\Delta_{g,\rho}f=\rho^{-1}\mathrm{div}_g(\rho\nabla_gf)=\frac1w(pf_x)_x,\qquad\mathcal L=-\Delta_{g,\rho}+q_0/w.
```

**Proof.** In 1D, $\sqrt g=\sqrt{w/p}$ and $g^{xx}=p/w$, hence $\rho\sqrt g=w$, $\rho\sqrt g\,g^{xx}=p$. Substitute in the coordinate divergence.

The integration-by-parts identity and quadratic form are

```math
\langle f,\mathcal Lz\rangle_w-\langle\mathcal Lf,z\rangle_w=[p(f_x^*z-f^*z_x)]_{\partial I},\qquad \mathfrak q[f]=\int_I(p|f_x|^2+q_0|f|^2)\,dx.
```

The constrained Euler–Lagrange equation of $\mathfrak q[f]-\lambda\int w|f|^2dx$ is precisely $-(pf_x)_x+q_0f=\lambda wf$. For a nonlinear variational background $f_*$, its Hessian gives a new *linearized* SL expression only after the functional, boundary conditions and background are fixed.

**Structural boundary [C].** A one-dimensional manifold has identically zero intrinsic torsion two-form and intrinsic Riemann curvature two-form: both are antisymmetric in two tangent directions, of which 1D has only one. A nonconstant SL potential or Riccati function is therefore **not** intrinsic 1D Weitzenböck torsion or Gaussian curvature.

## 3. The Liouville half-density is both a metric and Hilbert transform [D,K]

Introduce

```math
t=\int_{x_*}^{x}\sqrt{w/p}\,ds,\qquad \chi=(pw)^{1/4},\qquad\psi(t)=\chi(x)f(x).
```

Then

```math
-\psi_{tt}+\left(q_0/w+\chi_{tt}/\chi\right)\psi=\lambda\psi,\quad \int_I|f|^2w\,dx=\int_{t(I)}|\psi|^2dt.
```

The SL weighted Wronskian becomes the ordinary Wronskian:

```math
p(f_1f_{2,x}-f_{1,x}f_2)=\psi_1\psi_{2,t}-\psi_{1,t}\psi_2.
```

The map is a unitary operator equivalence **only if the self-adjoint domains are also transported**. Equality of local differential expressions alone does not choose the domain.

### 3.1 Canonical logarithmic metric and density

For the original framework,

```math
p=x^3,\quad w=x,\quad q_0=(r^2-1)x,\quad t=u=\ln(x/c),\quad\chi=x.
```

Thus

```math
g_{xx}=x^{-2},\quad g=du^2,\quad d\mathrm{vol}_g=du,\quad\rho=x^2=c^2e^{2u}.
```

On the *unconjugated* function $f(ce^u)$,

```math
\Delta_{g,\rho}=\partial_u^2+2\partial_u,\qquad\mathcal L=-\partial_u^2-2\partial_u+r^2-1.
```

The multiplier $U_cf=xf$ removes the drift:

```math
U_c\mathcal L U_c^{-1}=-\partial_u^2+r^2,\qquad\|f\|_{L^2(xdx)}=\|xf\|_{L^2(du)}.
```

Write $\rho=e^{-\varphi}$: $\varphi=-2u-2\ln c$, and $\mathrm{Hess}_g\varphi=0$. This example has nonzero weighted drift but zero 1D Bakry–Émery curvature. The $+1$ generated by the half-density is a scalar gauge effect, **not torsion**.

## 4. The punctured Euclidean manifold is conformally cylindrical [D,K]

For the punctured plane, $x=ce^u$ and $\theta\sim\theta+2\pi$ give

```math
dx^2+x^2d\theta^2=c^2e^{2u}(du^2+d\theta^2).
```

For any $d\ge2$ the punctured Euclidean metric is

```math
g_{\mathbb R^d\setminus0}=c^2e^{2u}(du^2+g_{S^{d-1}}).
```

It is **conformal**, not isometric, to the cylinder. Its angular separated equations involve Laplacian eigenfunctions on $S^{d-1}$ and the radial Sturm–Liouville equation, with spherical harmonic eigenvalues $\ell(\ell+d-2)$.

### 4.1 Critical four-dimensional Master–Yamabe identity

For radial $F(x)=y(u)/x$ in $\mathbb R^4$,

```math
\Delta_{\mathbb R^4}^{\rm rad}F=\frac1{x^3}(y_{uu}-y).
```

Since the normalized Master satisfies

```math
y_{uu}=r^2y-2\mu r^2y^3,\qquad y=2xf,
```

the exact radial PDE is

```math
-\Delta_{\mathbb R^4}^{\rm rad}F=\frac{1-r^2}{x^2}F+2\mu r^2F^3,\qquad F=2f.
```

Only at $r=1$ does the Hardy inverse-square term vanish, leaving the familiar critical cubic equation. Retaining $r$ is necessary to track the actual transformation rather than accidentally replacing the family with its special unit-resolution member.

## 5. Separation of variables is a selected geometric structure [D,K]

The Laplace–Beltrami formula is

```math
\Delta_g=(\sqrt{|g|})^{-1}\partial_i(\sqrt{|g|}g^{ij}\partial_j).
```

The possibility of separation depends on the metric, chosen potential, orthogonal foliations, Killing vectors and/or higher Killing–Stäckel tensors, together with quantum/Robertson conditions when relevant. **Not every manifold is separable**, and a Killing vector is a sufficient mechanism in many examples but is not universally necessary.

### 5.1 Exact catenoid separation

With an independent angular coordinate $v\sim v+2\pi/r$, the catenoid has

```math
X_C(u,v)=\left(\frac{R}{r}\cos(rv),\frac{R}{r}\sin(rv),u\right),\quad g_C=R^2(du^2+dv^2),\quad K_C=-r^2S^4.
```

Its axial Killing vector $\partial_v$ permits $f(u,v)=\phi_m(u)e^{imrv}$, $m\in\mathbb Z$. The negative Jacobi expression $B_C=-(\Delta_{g_C}+|A_C|^2)$ yields

```math
B_m\phi_m=R^{-2}[-\phi_{m,uu}+(m^2r^2-2r^2S^2)\phi_m].
```

Thus the **zero** equation is a flat Pöschl–Teller ODE after multiplication by $R^2$, but the **spectral** equation is the weighted SL problem

```math
-\phi_{m,uu}+(m^2r^2-2r^2S^2)\phi_m=\lambda_JR^2\phi_m.
```

The natural radial Hilbert space is $L^2(R^2du)$; it is not the flat $L^2(du)$ of the standard PT operator. Its exact unitary half-density conjugation from draft 140 is

```math
R B_m R^{-1}=-\partial_u(S^2\partial_u)+(m^2-1)r^2S^2.
```

## 6. Ermakov–Pinney is the local scale-and-clock flattening of a linear carrier [D,V]

For real $\omega(u)^2$ and a positive Pinney amplitude $\rho(u)$ let

```math
y_{uu}+\omega(u)^2y=0,\qquad\rho_{uu}+\omega(u)^2\rho=k_{\rm EP}\rho^{-3},\qquad \tau_u=\rho^{-2}>0.
```

**Theorem 6.1 [D,V] (exact local EP clock).** With $y(u)=\rho(u)Y(\tau(u))$,

```math
y_{uu}+\omega^2y=\rho^{-3}(Y_{\tau\tau}+k_{\rm EP}Y).
```

**Proof.** Differentiate twice: the cross terms in $Y_\tau$ cancel exactly because $\tau_u=\rho^{-2}$, leaving $y_{uu}=\rho_{uu}Y+\rho^{-3}Y_{\tau\tau}$.

The resulting constant-coefficient carrier is elliptic for $k_{\rm EP}>0$, free for $k_{\rm EP}=0$, and hyperbolic for $k_{\rm EP}<0$. This is a local transformation of an ODE and its projective connection; **it does not remove Gaussian curvature from an arbitrary two-dimensional metric**.

### 6.1 The exact Schwarzian formulation

Since $\tau_u=\rho^{-2}$,

```math
\{\tau,u\}=-2\rho_{uu}/\rho,\qquad\omega^2=k_{\rm EP}(\tau_u)^2+\frac12\{\tau,u\}.
```

For $k_{\rm EP}>0$, define the projective developing coordinate $z=\tan(\sqrt{k_{\rm EP}}\,\tau)$. The Schwarzian chain rule gives

```math
\{z,u\}=2k_{\rm EP}\tau_u^2+\{\tau,u\}=2\omega^2.
```

This is an exact **SL ↔ Riccati ↔ EP ↔ Schwarzian** correspondence on a chosen positive envelope chart.

### 6.2 Gram determinant and conserved current

For independent real carrier solutions $\phi_1,\phi_2$, positive definite symmetric Gram matrix $G=\begin{pmatrix}A&C\\C&B\end{pmatrix}$ and constant Wronskian $\mathscr W$,

```math
\rho^2=A\phi_1^2+2C\phi_1\phi_2+B\phi_2^2,\qquad k_{\rm EP}=(AB-C^2)\mathscr W^2.
```

An equivalent complex carrier $\Phi=\rho e^{i\vartheta}$ has constant current $j=\rho^2\vartheta_u=\sqrt{k_{\rm EP}}$. Positivity is a property of the chosen Gram form; it does NOT imply self-adjointness of a global operator domain, a separatrix energy, or a conserved Hilbert $L^2$ norm.

## 7. Levi–Civita and teleparallel connections are DIFFERENT constructions [D,V,K]

Let $(M^2,g)$ be an oriented Riemannian surface equipped with a **chosen local orthonormal coframe** $\theta^1,\theta^2$. Levi–Civita is the unique metric-compatible torsion-free connection, with connection form $\omega^1{}_2=-\omega^2{}_1$ satisfying Cartan's first structure equations

```math
d\theta^a+\omega^a{}_b\wedge\theta^b=0,\qquad\Omega^{LC}{}^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b.
```

A **teleparallel/Weitzenböck frame connection** on the same framed patch can instead be defined by requiring the selected frame to be parallel: $\omega^W{}^a{}_b=0$ *in that frame*. Its connection curvature vanishes, but its torsion can be nonzero:

```math
\Omega^W{}^a{}_b=0,\qquad T_W^a=d\theta^a+\omega^W{}^a{}_b\wedge\theta^b=d\theta^a.
```

Their difference is a contortion one-form $K^a{}_b=\omega^W{}^a{}_b-\omega^{LC}{}^a{}_b$ and the curvature/contortion relation is

```math
\Omega^{LC}=-D^W K+K\wedge K
```

when the sign convention $K=\omega^W-\omega^{LC}$ is used (the formula is the expansion of $\Omega^W=\Omega^{LC}+D^{LC}K+K\wedge K=0$, equivalently $\Omega^{LC}=-D^WK+K\wedge K$).

**Scope [C].** Flat teleparallel connection does not mean the Riemannian metric is flat; the nonzero Levi–Civita curvature is encoded in contortion and torsion derivatives. Choosing a frame is additional gauge data. Existence of one globally parallel frame is a topological restriction (for example, $S^2$ is not globally parallelizable), whereas the open catenoid cylinder is parallelizable.

### 7.1 An explicit catenoid connection and torsion computation

For the canonical catenoid of §5 take

```math
\theta^1=R\,du,\quad\theta^2=R\,dv,\qquad e_1=S\partial_u,\quad e_2=S\partial_v.
```

Direct differentiation gives

```math
d\theta^1=0,\qquad d\theta^2=R_u\,du\wedge dv=rSW\,\theta^1\wedge\theta^2.
```

Thus the chosen teleparallel frame connection has the exact nonzero torsion coefficient

```math
T_W^1=0,\qquad T_W^2=t_2\,\theta^1\wedge\theta^2,\qquad t_2=rSW.
```

The Levi–Civita form in the chosen sign convention is

```math
\omega^{LC}{}^1{}_2=-rW\,dv,\qquad d\omega^{LC}{}^1{}_2=-r^2S^2du\wedge dv=K_C\,\theta^1\wedge\theta^2.
```

Since $K_C=-r^2S^4$, the two descriptions satisfy a **verified exact curvature–torsion identity**

```math
K_C=-e_1(t_2)-t_2^2=-r^2S^4.
```

**Proof.** Differentiate $t_2=rSW$ using $S_u=-rSW$ and $W_u=rS^2$; then $e_1=S\partial_u$ and $W^2+S^2=1$ give $e_1(t_2)+t_2^2=r^2S^4$.

This identity is the mathematical content of the “Levi–Civita / Weitzenböck dictionary” on this **specified** two-dimensional metric. It is not the Riccati equation of the one-dimensional SL carrier, although the same elementary $S,W$ generate its coefficients.

## 8. Bochner–Weitzenböck is NOT Darboux–Riccati factorization [C,K,D]

The classical *Bochner–Weitzenböck formula* is a **tensorial identity for Laplacians on forms or bundles**. On one-forms of a Riemannian manifold,

```math
\Delta_H=d\delta+\delta d=\nabla^{LC*}\nabla^{LC}+\mathrm{Ric}^{\sharp}
```

under the standard nonnegative Laplacian convention; in two dimensions $\mathrm{Ric}^{\sharp}=K_G\,\mathrm{Id}$ on one-forms. The curvature correction acts on a bundle. On scalar zero-forms the analogous curvature correction is absent. The connection used on the right is **Levi–Civita**, not automatically the flat teleparallel connection of §7.

By contrast, for a selected smooth real **Riccati superpotential** $h(u)$,

```math
A=\partial_u+h,\qquad A^\dagger=-\partial_u+h,\qquad A^\dagger A=-\partial_u^2+h^2-h_u.
```

Writing $V=h^2-h_u$ is a **factorization of a chosen scalar Schrödinger differential expression**. It uses the formal $L^2(du)$ adjoint and requires a zero-mode/factorization energy; it does not construct torsion or prove a Bochner–Weitzenböck identity.

For the canonical choice $h=rW$,

```math
h^2-h_u=r^2-2r^2S^2,\qquad A^\dagger A=h_1+r^2,\quad h_1=-\partial_u^2-2r^2S^2.
```

The related partner is $AA^\dagger=-\partial_u^2+r^2$, and $A h_1=h_0A$ after removing the common constant. This is the Darboux/shape-invariant ladder recorded in H73/H100, **not teleparallel transport**.

### 8.1 The correct common generalization is a Dirac-type square

On a doubled Hilbert space define a formal graded first-order operator

```math
\mathcal D=\begin{pmatrix}0&A^\dagger\\A&0\end{pmatrix},\qquad\mathcal D^2=\begin{pmatrix}A^\dagger A&0\\0&AA^\dagger\end{pmatrix}.
```

This **supersymmetric Dirac-factorization identity** resembles a Bochner decomposition in that a first-order operator is squared to give a second-order operator plus zeroth-order data. An actual **geometric Dirac or Hodge–de Rham operator** requires a Clifford/differential-form bundle, compatible connection, spin/Hodge structure, and the corresponding curvature term. Without those additional data, identifying $\mathcal D^2$ with a teleparallel torsion scalar or with a surface Hodge Laplacian is unjustified.

**No-go [C]:** Since intrinsic 1D torsion vanishes, the nontrivial $h^2-h_u$ factorization cannot literally be a nonzero one-dimensional torsion-curvature duality. The valid catenoid torsion identity and the valid PT Darboux factorization must remain two separately typed arrows linked by their common scalar hyperbolic field.

## 9. The geometry of the Schwarzian, SL carrier transport and holonomy [D,K,C]

For $-\phi_{uu}+V(u)\phi=\lambda\phi$, put the rank-two state and connection matrix

```math
\mathbf v=\binom{\phi}{\phi_u},\qquad \mathbf v_u=\mathsf A(u,E)\mathbf v,\qquad \mathsf A=\begin{pmatrix}0&1\\V(u)-E&0\end{pmatrix}\in\mathfrak{sl}_2.
```

Parallel transport of the **carrier state** means solving this first-order linear system; the connection $\nabla^{SL}=d-\mathsf A\,du$ is automatically flat as a 1D connection, since there is no nonzero local two-form on the $u$ line. Its nontrivial transfer/monodromy can arise from **global periodic identification or singularities**, not from a local 1D curvature two-form.

The Riccati coordinate $z=\phi_u/\phi$ obeys

```math
z_u=V(u)-E-z^2
```

where $\phi\ne0$. For two linearly independent solutions, the projective ratio $F=\phi_1/\phi_2$ has

```math
\{F,u\}=2(E-V(u)).
```

The projective carrier state transforms under the $SL_2$ transport. A ratio $F$ is a coordinate on $\mathbb{RP}^1$ or its complexification $\mathbb{CP}^1$; it is **NOT** the choice of a normalized complex two-spinor or an $S^1$ Hopf-fiber phase.

### 9.1 Three parallel-transport problems that cannot be substituted for one another

| Transport | Base/independent variable | Fiber and connection | Conserved datum |
|---|---|---|---|
| SL carrier | spatial $u$, fixed spectral $E$ | rank-two linear states, $\mathfrak{sl}_2$ | Wronskian |
| Lamé/Riemann Gauss–Manin | elliptic modulus $m_{\rm ell}$ or $k_R$ | marked $H_1$ homology or period cohomology | intersection/symplectic period pairing |
| Hopf/Berry | a chosen path in the Gauss sphere | principal $U(1)$ fiber in $S^3$ | holonomy modulo $2\pi$; global Chern class on a 2-cycle |

The explicit Lamé–Riemann affine map of draft 170 is a map **of spectral elliptic curve coordinates**, and its Gauss–Manin gauge compares two period connections. It does not turn the spatial Riccati flow (which varies $u$ at fixed $E$) into the Hopf connection (which transports phases along a path in $\mathbb{CP}^1$).

## 10. A crucial map-of-spaces correction for the Lamé–Riemann identification [D,C]

Draft 170 proves the selected real isomorphism for $0<m_{\rm ell}<1$:

```math
m_{\rm ell}=(1+\lambda_R^2)^{-1},\quad k_R=\lambda_R^{-1}-\lambda_R,\quad D_R=\lambda_R+\lambda_R^{-1},
```

```math
g_R(E)=-k_R-\frac{D_R}{r^2}E,\qquad y_R=\frac{D_R^{3/2}}{r^3}\eta,\qquad \frac{dg_R}{y_R}=-\frac r{\sqrt{D_R}}\frac{dE}{\eta}.
```

This is an exact **fiberwise elliptic curve isomorphism with marked holomorphic differential**. It is NOT itself a horizontal-lift equation on a bundle of Schrödinger eigenvectors: in the Schrödinger equation the spectral parameter $E$ is **held fixed as $u$ evolves**, so $g_R(E)$ is also fixed, while the Riccati ratio $\phi_u/\phi$ typically varies.

At the PT nodal limit, the choice of catenoid coordinate in draft 160,

```math
t(s)=\frac{s-r}{s+r}=e^{r(u+iv)},\qquad E=-s^2,
```

is therefore a **chosen parametrization of the spectral normalization by a surface coordinate**; it imposes a variable spectral projection

```math
s(u+iv)=r\coth\left(\frac{r(u+iv)}2\right),\qquad E(u+iv)=-r^2\coth^2\left(\frac{r(u+iv)}2\right).
```

It is not an **isospectral** SL flow, since $E$ changes along the chosen surface parametrization. What is exact is the map of **marked differential forms**, not equality of independent-variable dynamics. This is an important condition for a future foundational theorem: a point of a spectral curve can be used as a surface coordinate after a declared map, but the Baker–Akhiezer eigenfunction at **fixed** spectral point has a different evolution variable.

## 11. Teleparallel and Rindler-like charts require additional Lorentzian structure [D,C]

A Rindler wedge of flat Minkowski space can be parametrized with constants $\kappa_R>0$ by

```math
ds^2=-\kappa_R^2X^2dt^2+dX^2,\qquad X>0.
```

Putting $X=X_0e^u$ gives

```math
ds^2=X_0^2e^{2u}(-\kappa_R^2dt^2+du^2).
```

This is a conformal Lorentzian cylinder/wedge chart on **flat** spacetime, and its appearance of a logarithmic coordinate resembles the canonical $u=\ln(x/c)$. But Rindler time is an independent Lorentzian Killing coordinate; the wedge and its horizon are **additional data**. Neither the catenoid's Riemannian teleparallel torsion nor its scalar Darboux factorization automatically produces a Lorentzian horizon or a particular FRW/Rindler geometry.

## 12. Duffing to reciprocal EP: exact only on the zero-energy shell [D,V,H]

The general normalized cubic Master/Duffing equation is

```math
y_{uu}=r^2y-2\mu r^2y^3,\quad \varepsilon_N=y_u^2-r^2y^2+\mu r^2y^4.
```

On an interval where $y>0$, define the reciprocal square-root field

```math
a=y^{-1/2},\qquad y=a^{-2}.
```

**Theorem 12.1 [D,V] (complete finite-energy reciprocal equation).** On every positive solution interval,

```math
a_{uu}=\frac{r^2}4a+\frac{\mu r^2}{4a^3}+\frac{3\varepsilon_N}4a^5.
```

**Proof.** Differentiate $a=y^{-1/2}$ twice:

```math
a_{uu}=\frac34y^{-5/2}y_u^2-\frac12y^{-3/2}y_{uu}.
```

Insert $y_u^2=r^2y^2-\mu r^2y^4+\varepsilon_N$ and $y_{uu}=r^2y-2\mu r^2y^3$, then collect powers $y^{-1/2}=a$, $y^{3/2}=a^{-3}$, $y^{-5/2}=a^5$.

**Corollary 12.2 [D].** The reciprocal is a **standard constant-strength EP equation precisely on the separatrix $\varepsilon_N=0$**, unless the chosen solution is a special degenerate constant where the added term can be absorbed into a redefined coefficient. At arbitrary energy, a genuine *quintic* correction survives. The historical ZIP's friedmann-reciprocal-envelope module already records this finite-energy correction; the formula here restores it in the canonical variables and emphasizes its domain restriction.

For the centered positive separatrix $y=S/\sqrt\mu$,

```math
a(u)=\mu^{1/4}\sqrt{\cosh(ru)},\qquad a_{uu}=\frac{r^2}4a+\frac{\mu r^2}{4a^3}.
```

The sign of the linear coefficient is **hyperbolic**: this is a real Pinney oscillator with $\omega^2=-r^2/4$, not an oscillatory harmonic trap unless a different real clock/potential or analytical continuation is selected.

### 12.1 Why this is not a canonical symplectic transformation without added momentum data

The point transformation $y=a^{-2}$ changes the natural phase momentum: $p_y=y_u=-2a^{-3}a_u$. At fixed clock $u$,

```math
dy\wedge dp_y=4a^{-6}\,da\wedge d(a_u).
```

Thus the raw map $(y,y_u)\mapsto(a,a_u)$ is **conformally symplectic**, not canonical. To obtain a canonical transformation one must take the cotangent-lifted momentum $P_a=p_y\,dy/da=-2a^{-3}p_y=4a^{-6}a_u$ and transform the Hamiltonian accordingly. The two natural unit-mass mechanical Hamiltonians are not simply identical off their selected energy shells.

## 13. The kinematic Friedmann constraint is exactly the reciprocal first integral [D,V,H]

From the same reciprocal substitution, define the **logarithmic derivative**

```math
H_a=\frac{a_u}{a}.
```

The finite-energy first integral becomes

```math
\boxed{\quad H_a^2=\frac{r^2}4\left(1-\frac{\mu}{a^4}\right)+\frac{\varepsilon_N}4a^4.\quad}
```

(Here the boxed formula is mathematical notation, not a statement about physical cosmological matter.) Direct differentiation, or Theorem 12.1, gives

```math
(H_a)_u=\frac{\mu r^2}{2a^4}+\frac{\varepsilon_N}{2}a^4.
```

**Theorem 13.1 [D,V] (algebraic Friedmann–EP dictionary).** On the zero-energy positive Master branch,

```math
H_a^2=\frac{r^2}4(1-\mu a^{-4}),\qquad (H_a)_u=\frac{\mu r^2}{2a^4},\qquad H_a=\frac r2\tanh(ru).
```

The first equation is a **kinematic Friedmann-type constraint**. It is not, without a selected Lorentzian metric, proper time, gravitational field equations and matter stress tensor, a physical FLRW solution. The negative $a^{-4}$ term in the separatrix is a *negative radiation-like coefficient* if one elects to compare to standard four-dimensional FLRW scaling; the positive $\varepsilon_N a^4$ term at finite energy would correspond to a formal effective $w=-7/3$ power-law component. Those labels are **different algebraic terms** and must not be conflated into a claim of physical phantom energy.

### 13.1 Optional Lorentzian warped-product realization

Only after choosing dimension three, a constant-curvature spatial metric $h_K$ and Lorentzian proper-time coordinate $T$ does one obtain

```math
ds^2=-dT^2+a(T)^2h_K,\qquad \mathrm{Scal}=6\left(\frac{a_{TT}}a+\left(\frac{a_T}a\right)^2+\frac K{a^2}\right).
```

The scalar curvature of this **chosen metric** may then be calculated from the selected function $a(T)$. It is separate from the original **weighted 1D SL** metric $du^2$ and from the catenoid Gaussian curvature $-r^2S^4$. A Friedmann equation is a field equation only after specifying stress energy and gravitational dynamics, whereas here it is obtained from an ODE first integral.

## 14. The Ermakov–Lewis invariant is a true Hamiltonian construction [D,K]

Choose an independent oscillator time $t$ and a real frequency function $\omega(t)^2$. The classical oscillator Hamiltonian is

```math
H_{\rm osc}(q,p,t)=\frac12[p^2+\omega(t)^2q^2],\qquad q_t=p,\quad p_t=-\omega^2q.
```

Let $\rho(t)>0$ solve $\rho_{tt}+\omega^2\rho=\omega_0^2\rho^{-3}$ with **fixed** $\omega_0>0$. Define canonical phase variables

```math
Q=q/\rho,\qquad P=\rho p-\rho_tq.
```

The Ermakov–Lewis quantity is

```math
I_{\rm EL}=\frac12[P^2+\omega_0^2Q^2]=\frac12[(\rho p-\rho_tq)^2+\omega_0^2(q/\rho)^2].
```

**Theorem 14.1 [D,K].** Along every oscillator solution $dI_{\rm EL}/dt=0$.

**Proof.** Differentiate and use the two oscillator equations and the Pinney equation. One obtains $Q_t=P/\rho^2$ and $P_t=-\omega_0^2Q/\rho^2$, so $dI_{\rm EL}/dt=P(-\omega_0^2Q/\rho^2)+\omega_0^2Q(P/\rho^2)=0$.

The map $(q,p)\to(Q,P)$ is symplectic at each fixed time, since $dQ\wedge dP=dq\wedge dp$, but is **time-dependent**. The new clock $\tau_t=\rho^{-2}$ makes $(Q,P)$ a standard constant-frequency oscillator.

### 14.1 Quantum Lewis–Riesenfeld invariant requires an actual Schrödinger Hilbert realization

For the separately chosen quantum harmonic oscillator, setting $\hbar=1$ and particle mass $1$,

```math
i\partial_t\Psi=\widehat H(t)\Psi,\quad \widehat H(t)=\frac12[-\partial_q^2+\omega(t)^2q^2],
```

the operator

```math
\widehat I(t)=\frac12\left[(\rho\widehat p-\rho_tq)^2+\omega_0^2(q/\rho)^2\right]
```

satisfies the Lewis–Riesenfeld invariant equation $\partial_t\widehat I+i[\widehat H,\widehat I]=0$ on suitable common operator domains. This is a **specific quantization and unitary evolution**, not an automatic consequence of the original spatial SL operator or of the word “Hamiltonian.” Invariant eigenstates acquire additional Lewis–Riesenfeld phases; that phase is not automatically the Hopf Berry holonomy of the Gauss map.

## 15. Harmonic-trap Schrödinger and Gross–Pitaevskii lens maps [D,K]

For the time-dependent quantum oscillator of §14 define

```math
X=q/\rho(t),\qquad \tau_t=\rho^{-2},\qquad\Psi(q,t)=\rho^{-1/2}e^{i\rho_tq^2/(2\rho)}\chi(X,\tau).
```

A direct chain-rule calculation gives

```math
i\partial_\tau\chi=\frac12[-\partial_X^2+\omega_0^2X^2]\chi.
```

This is a **unitary time-dependent dilation and quadratic phase** with the EP clock, on the correct $L^2(dq)$ and $L^2(dX)$ spaces. The phase and the factor $\rho^{-1/2}$ are necessary; changing only $q\mapsto q/\rho$ does not preserve the Schrödinger equation.

### 15.1 Exact semilinear trap scaling in dimension d

Consider a separately chosen $d$-dimensional semilinear Schrödinger/Gross–Pitaevskii equation

```math
i\partial_t\Psi=-\frac12\Delta_{\mathbf x}\Psi+\frac{\omega(t)^2}2|\mathbf x|^2\Psi+g(t)|\Psi|^{2\sigma}\Psi.
```

Let $\rho$ solve the same scalar EP, and use the $d$-dimensional lens ansatz

```math
\Psi(\mathbf x,t)=\rho^{-d/2}\exp\left(\frac{i\rho_t}{2\rho}|\mathbf x|^2\right)\chi(\mathbf X,\tau),\quad \mathbf X=\mathbf x/\rho,\quad\tau_t=\rho^{-2}.
```

Then the transformed equation has constant harmonic-trap term but a **possibly time-dependent nonlinear coupling**

```math
i\partial_\tau\chi=-\frac12\Delta_{\mathbf X}\chi+\frac{\omega_0^2}2|\mathbf X|^2\chi+g(t(\tau))\rho^{2-d\sigma}|\chi|^{2\sigma}\chi.
```

Hence a constant $g$ stays constant automatically only at **mass-critical power $\sigma=2/d$**. Otherwise the nonlinear equation is not generally conjugate to a constant-coefficient GP equation unless $g(t)$ is chosen to compensate the factor. This is an exact mathematical restriction and makes clear why the cubic GP equation behaves differently in dimensions $1,2,3$.

## 16. PDM and the von Roos ordering: SL does NOT fix a quantum ordering [D,K]

Let $M(x)>0$ be a separately specified position-dependent mass and set $\hbar>0$. The **BenDaniel–Duke** kinetic expression is

```math
H_{\rm BDD}=-\frac{\hbar^2}2\partial_x(M^{-1}\partial_x)+V(x).
```

It is a Sturm–Liouville expression on $L^2(dx)$ with

```math
p(x)=\frac{\hbar^2}{2M(x)},\qquad w(x)=1,\qquad q_0(x)=V(x).
```

For the more general formal **von Roos** ordering choose real $\alpha,\beta,\gamma$ satisfying $\alpha+\beta+\gamma=-1$:

```math
H_{\alpha\beta\gamma}=-\frac{\hbar^2}4\left[M^\alpha\partial_xM^\beta\partial_xM^\gamma+M^\gamma\partial_xM^\beta\partial_xM^\alpha\right]+V.
```

**Theorem 16.1 [D,V] (exact ordering potential).** For smooth $M>0$ the difference from BenDaniel–Duke is a **scalar multiplication potential**

```math
H_{\alpha\beta\gamma}=H_{\rm BDD}+U_{\alpha\gamma},\quad U_{\alpha\gamma}=-\frac{\hbar^2}4\left[(\alpha+\gamma)\frac{M_{xx}}{M^2}-2(\alpha+\gamma+\alpha\gamma)\frac{M_x^2}{M^3}\right].
```

**Proof.** Expand both ordered products using Leibniz's rule. Their second-derivative term is $-{\hbar^2}\psi_{xx}/(2M)$ and the first-derivative term is $\hbar^2M_x\psi_x/(2M^2)$ for every allowed ordering. The remaining zeroth-order terms combine into the displayed $U_{\alpha\gamma}$.

Thus the weighted metric from the principal symbol fixes a second-order differential expression **up to scalar ordering potential and domain data**; the geometry does not uniquely resolve the von Roos ambiguity. At mass jumps, interface conditions and distributions require separate analysis; the smooth expansion cannot be applied blindly across discontinuities.

The exact Liouville coordinate and half-density for BDD are

```math
t(x)=\int_{x_*}^x\sqrt{\frac{2M(s)}{\hbar^2}}ds,\qquad\chi(x)=\left(\frac{\hbar^2}{2M(x)}\right)^{1/4}.
```

This identifies PDM as a legitimate **weighted SL/operator** realization, not a unique physical consequence of the canonical Symmetrical Function.

## 17. Keller–Miksis: EP appears only in a controlled conservative reduction [D,H,K,C]

Let $R_b(t)>0$ be a bubble-radius variable, $R_0>0$ a reference scale, $\rho_L>0$ a liquid density and $c_s>0$ a sound speed. One common form of the full Keller–Miksis equation, with $M_b=\dot R_b/c_s$, is

```math
(1-M_b)R_b\ddot R_b+\frac32(1-M_b/3)\dot R_b^2=\frac{1+M_b}{\rho_L}P+\frac{R_b}{\rho_Lc_s}\dot P.
```

The wall pressure $P$ can depend on $R_b,\dot R_b,t$, surface tension, viscosity and forcing; therefore the **full equation is generally not a conservative Pinney ODE**.

In the controlled incompressible, inviscid and autonomous radius-only limit one gets Rayleigh–Plesset,

```math
R_b\ddot R_b+\frac32\dot R_b^2=P(R_b)/\rho_L.
```

Define the *new clock* and amplitude (neither is the original canonical $u$ or EP field $a$)

```math
X=R_b/R_0>0,\qquad Y=X^{3/2},\qquad d\tau/dt=X^{-1}.
```

**Theorem 17.1 [D,V,H376] (Sundman reduction).**

```math
Y_{\tau\tau}=\frac3{2\rho_LR_0^2}Y\,P(R_0Y^{2/3}).
```

For a selected autonomous polytropic pressure $P=p_0X^{-3\gamma}-p_\infty$, the exact transformed equation is

```math
Y_{\tau\tau}=-\omega_b^2Y+\beta_bY^{1-2\gamma},\quad\omega_b^2=\frac{3p_\infty}{2\rho_LR_0^2},\quad\beta_b=\frac{3p_0}{2\rho_LR_0^2}.
```

It is **exactly EP only for $\gamma=2$** (and under the reductions just stated). The original physical radius and time reconstruct as $R_b=R_0Y^{2/3}$ and $dt=Y^{2/3}d\tau$. Other gas laws, compressibility, damping and forcing reintroduce different powers or time dependence.

The historical ZIP's Keller–Miksis section derives the same Sundman/pressure-law condition and also gives a compressible energy-drift identity; it expressly does not identify the full dissipative model with EP. Treating the reduced equation as an exact **ODE dictionary** is rigorous; claiming a universal liquid bubble realization from the framework would not be.
