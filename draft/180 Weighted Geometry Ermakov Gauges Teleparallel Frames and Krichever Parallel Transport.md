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
s(u+iv)=-r\coth\left(\frac{r(u+iv)}2\right),\qquad E(u+iv)=-r^2\coth^2\left(\frac{r(u+iv)}2\right).
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
H_a^2=\frac{r^2}4\left(1-\frac{\mu}{a^4}\right)+\frac{\varepsilon_N}4a^4.
```

(This identity is mathematical notation, not a statement about physical cosmological matter.) Direct differentiation, or Theorem 12.1, gives

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

## 18. Sato Grassmannian: the historical framework already has an EXACT rank-one point [H136,D,K]

The historical ZIP's sato-grassmannian.md distinguishes three inputs: a **soliton Grassmannian point**, a **decorated Krichever curve point**, and a **verified Master-to-KdV reduction**. Their existence is not a universal assertion about every differential equation or all level-$\ell$ hierarchies.

Let $k_{\rm S}$ be a formal **Sato spectral coordinate**, distinct from physical wave number $k_{\rm sc}$ and the Riemann modulus $k_R$. Fix a gluing parameter $\mathfrak a>0$. The archive defines the rank-one subspace

```math
\mathscr W_{r,\mathfrak a}=\left\{\frac{F(k_{\rm S})}{k_{\rm S}+r}:F\in\mathbb C[k_{\rm S}],\quad F(r)=-\mathfrak a^{-1}F(-r)\right\}.
```

An explicit normalized basis is

```math
w_n(k_{\rm S})=k_{\rm S}^n-\frac{2\mathfrak a}{1+\mathfrak a}\frac{r^{n+1}}{k_{\rm S}+r},\qquad n=0,1,\ldots.
```

The coefficient matrix of negative powers of $k_{\rm S}$ has rank one. Moreover

```math
k_{\rm S}^2\mathscr W_{r,\mathfrak a}\subseteq\mathscr W_{r,\mathfrak a}
```

because $k_{\rm S}^2$ takes the same value at the two gluing points $\pm r$: this is the **KdV two-reduction condition** for the selected Grassmannian point. Its polynomial stabilizer is

```math
\mathbb C[k_{\rm S}^2,k_{\rm S}(k_{\rm S}^2-r^2)].
```

The nodal cubic is recovered by setting the coordinate functions

```math
\lambda_{\rm S}=-k_{\rm S}^2,\qquad \nu_{\rm S}=ik_{\rm S}(k_{\rm S}^2-r^2),\qquad \nu_{\rm S}^2=\lambda_{\rm S}(\lambda_{\rm S}+r^2)^2.
```

This last sign convention is a **quadratic twist** of the real Lax–Novikov curve convention of draft 170 ($\nu^2=-\lambda(\lambda+r^2)^2$). The curve structures become isomorphic over $\mathbb C$ after a corresponding factor of $i$, but their chosen real slices must not be silently identified.

### 18.1 The exact Sato tau and Baker function

For independent hierarchy times $\mathbf t=(t_1,t_3,t_5,\ldots)$, the archival one-soliton tau is

```math
\tau_{\rm S}(\mathbf t)=1+\mathfrak a\exp\left(2\sum_{j\ge0}r^{2j+1}t_{2j+1}\right).
```

On the **chosen** slice $t_1=u$, $t_3=-4T$, $\mathfrak a=e^{-2ru_0}$, one gets

```math
2\partial_u^2\log\tau_{\rm S}=2r^2\mathrm{sech}^2[r(u-4r^2T-u_0)].
```

The associated Baker/Jost function at $T=0$ is

```math
\psi_{\rm BA}(u,k_{\rm S})=e^{k_{\rm S}u}\frac{k_{\rm S}-rW(u)}{k_{\rm S}+r},\qquad(\partial_u^2+2r^2S^2)\psi_{\rm BA}=k_{\rm S}^2\psi_{\rm BA}.
```

**Theorem 18.1 [H136,V] (actual verified integrable closure).** For this selected Grassmannian point, the tau, finite-rank Baker function, PT spectral operator, nodal cubic, and two-reduction condition are explicitly compatible. The archive checks them, including the Schur/Plücker hook-coordinate rule. This is a genuine algebro-geometric origin of the proliferation of determinant identities; **it is not an unconstructed generic KP interpretation**.

### 18.2 The Master reduction to the KdV stationary equation

For a general positive real solution of the cubic Master equation with first integral $\varepsilon_N$, put

```math
Q=2\mu r^2y^2,\qquad c_1=4\mu r^2\varepsilon_N.
```

Direct differentiation, using the Master energy, gives the historical H136 identities

```math
Q_{uu}=4r^2Q-3Q^2+c_1,\quad Q_{uuu}+6QQ_u-4r^2Q_u=0.
```

With the **separate KdV time** $T$ the chosen travelling field $\mathcal U(\xi,T)=Q(\xi-4r^2T)$ solves $\mathcal U_T+6\mathcal U\mathcal U_\xi+\mathcal U_{\xi\xi\xi}=0$.

The operator $\mathscr L=-\partial_u^2-Q$ and a selected third-order $\mathscr A$ commute, with a Burchnall–Chaundy cubic (H136); the **linearized Master Hessian** is a *different* Lamé index-two or shifted PT operator. One must not swap the integrable Lax operator with the variational Hessian without an actual intertwiner.

## 19. The Krichever construction needs MORE than a smooth curve or equal j [K,C]

A Krichever/Baker–Akhiezer construction starts from **decorated algebraic data**, typically

```math
(\Gamma,P_\infty,k_\infty^{-1},\mathcal D,\text{framing/normalization},\text{chosen hierarchy times}),
```

where $\Gamma$ is a smooth spectral curve, $P_\infty$ a marked point, $k_\infty^{-1}$ a local coordinate, and $\mathcal D$ a nonspecial divisor or corresponding line bundle of the required degree. A Baker–Akhiezer function is characterized by its meromorphic divisor and its specified exponential asymptotic at the marked point.

The finite-gap Baker function has the theta schematic form

```math
\psi_{\rm BA}(P,u)=e^{u\Omega(P)}\frac{\Theta(A(P)+u\mathbf U+\mathbf Z)}{\Theta(A(P)+\mathbf Z)}\,C(P,u),
```

where $\Omega$ is an Abelian integral with a prescribed principal part and $C$ enforces the chosen normalization. Under the **KdV two-reduction** and appropriate spectral data it satisfies a **second-order** equation $L\psi_{\rm BA}=E(P)\psi_{\rm BA}$. A general KP Grassmannian point, however, is associated to a pseudodifferential Lax operator and does **not automatically** provide a scalar second-order self-adjoint SL problem. Self-adjointness further requires a compatible real structure, potential, interval and Hilbert domain.

### 19.1 What the new Lamé–Riemann curve map actually supplies

Draft 170 constructs the selected real elliptic isomorphism

```math
m_{\rm ell}=(1+\lambda_R^2)^{-1},\quad k_R=\lambda_R^{-1}-\lambda_R,\quad D_R=\lambda_R+\lambda_R^{-1},
```

```math
g_R=-k_R-\frac{D_R}{r^2}E,\qquad y_R=\frac{D_R^{3/2}}{r^3}\eta,\qquad \frac{dg_R}{y_R}=-\frac r{\sqrt{D_R}}\frac{dE}{\eta}.
```

It identifies a **selected one-gap Lamé spectral curve** with the elliptic curve of the Riemann minimal example, including the marked holomorphic differential up to explicit scale. The associated Gauss–Manin period connections are related by a known explicit gauge (draft 170 §23), with an invariant symplectic period determinant. This is a precise functorial **transport of elliptic cohomology data**. It does not automatically determine a Krichever divisor or equate the spectral second-kind quasimomentum with the geometric holomorphic height form.

The newly identified elliptic curve can support **both** (i) spectral BA data with a marked point at spectral infinity and (ii) minimal immersion Weierstrass data with punctures and a Gauss map. These are different **decorations of the same underlying curve**. The marked pole divisors and homology period constraints decide which portions of the two constructions can be transported.

## 20. Gauss map, Hopf bundle, and Berry curvature: a genuine topological calculation [D,V,K]

For any meromorphic Gauss map $g:\Sigma\to\mathbb{CP}^1$ on a Riemann surface $\Sigma$, choose on the affine chart the unit spinor and local Hopf connection

```math
\eta_g=\frac{(1,g)}{\sqrt{1+|g|^2}},\qquad \mathcal A_g=-i\,\eta_g^\dagger d\eta_g=\frac{\bar g\,dg-g\,d\bar g}{2i(1+|g|^2)}.
```

The curvature is

```math
\mathcal F_g=d\mathcal A_g=\frac{i\,dg\wedge d\bar g}{(1+|g|^2)^2}=\frac12g^*\omega_{S^2},
```

where $\omega_{S^2}$ is the oriented unit round-sphere area form, total area $4\pi$. On the compactified domain and using the necessary second gauge patch at $g=\infty$,

```math
\frac1{2\pi}\int_\Sigma\mathcal F_g=\deg(g).
```

**Theorem 20.1 [D,K] (Chern degree of the selected minimal-surface Gauss map).** The catenoid Gauss map $g_C=-t$ on the compactification $\Sigma_C=\mathbb{CP}^1$ has degree one, while the archived Riemann minimal-example Gauss map $g_R$ on its compactified elliptic curve $E_R$ has degree **two**, since the projection

```math
E_R:\quad y_R^2=g_R^3+k_Rg_R^2-g_R\quad\longrightarrow\quad\mathbb{CP}^1,\qquad (g_R,y_R)\mapsto g_R
```

has two generic points in each fiber. Therefore

```math
c_1(g_C^*\mathrm{Hopf})=1,\qquad c_1(g_R^*\mathrm{Hopf})=2.
```

The corresponding total Gaussian curvatures over the respective complete finite-total-curvature fundamental surfaces/quotients are

```math
\int_C K_C\,dA_C=-4\pi,\qquad\int_{R/{\rm period}}K_R\,dA_R=-8\pi.
```

The last equalities follow from the area-degree formula of the meromorphic minimal-surface Gauss map, with the punctures having measure zero on the compactification. They depend on the chosen **fundamental quotient** for the singly periodic Riemann surface.

**Important limitation:** These Chern numbers concern a **selected Hopf pullback** and the full compactified complex surface. They do not imply that an EP scalar amplitude is the Hopf *horizontal lift*, or that every Berry loop phase is an integer. A Berry holonomy along a loop is $\oint\mathcal A_g$ modulo $2\pi$ and generally depends continuously on the loop.

### 20.1 Real projective SL ratio is not the Hopf fiber

The scalar SL ratio or Riccati variable is a *base projective coordinate* on $\mathbb{CP}^1$ after complexification. A Hopf lift requires an independent choice of normalized spinor and its common $U(1)$ gauge phase. For the **real** Sato slice $z=e^{ru}>0$ the normalized spinor $(1,z)/\sqrt{1+z^2}$ has real coordinates and its local Berry one-form along the meridian is zero. The full two-dimensional Hopf curvature becomes nontrivial only after extending to a complex/projective coordinate such as $z=e^{r(u+iv)}$ and defining a genuine two-dimensional base.

**No-go [C]:** The meromorphic Riemann Gauss coordinate $g_R(E)$ is constant as $u$ evolves at fixed spectral energy $E$, whereas a nontrivial SL Riccati solution generally varies in $u$. Thus the identity $g_R=-k_R-D_RE/r^2$ does not, by itself, project a nontrivial SL Riccati flow into a Hopf horizontal lift. That would require an explicitly specified **moving spectral point**, an eigenvector line bundle, and a connection-preserving map.

## 21. Bonnet rotation and Berry holonomy are distinct U(1) operations [D,C]

For fixed minimal-surface Weierstrass data $(g,dh)$, the **Bonnet/associate family** multiplies the immersion triple of holomorphic/meromorphic 1-forms by a constant phase $e^{i\delta}$:

```math
\boldsymbol\Phi_\delta=e^{i\delta}\boldsymbol\Phi_0,\qquad X_\delta=\mathrm{Re}\int\boldsymbol\Phi_\delta.
```

The Gauss map $g$ is unchanged, and therefore the Hopf curvature $\mathcal F_g$ and its Chern degree are unchanged. Nevertheless the **real immersion periods** rotate:

```math
\mathrm{Re}\oint_\gamma\boldsymbol\Phi_\delta=\cos\delta\,\mathrm{Re}\oint_\gamma\boldsymbol\Phi_0-\sin\delta\,\mathrm{Im}\oint_\gamma\boldsymbol\Phi_0.
```

For the catenoid, $\oint\boldsymbol\Phi_0=(0,0,2\pi i/r)$, so

```math
\mathrm{Re}\oint\boldsymbol\Phi_\delta=(0,0,-2\pi\sin\delta/r).
```

At $\delta=0$ the immersion closes on the punctured plane; at the conjugate helicoid value $\delta=\pi/2$ a nonzero real vertical translation appears, requiring the angular universal cover or a translation quotient.

**Corollary 21.1 [D].** A constant **Bonnet phase** changes real immersion periods without changing the Gauss map's pulled-back Hopf Chern number. A **Berry phase** is connection holonomy along a specified path. Their common notation as a complex $U(1)$ phase does not make them identical geometric quantities.

## 22. Enneper–Weierstrass immersion AS FLAT AFFINE TRANSPORT (qualified) [D,K]

Let $\Sigma^\circ$ be a punctured Riemann surface with meromorphic Weierstrass triple $\boldsymbol\Phi=(\Phi_1,\Phi_2,\Phi_3)$ satisfying the algebraic nullity condition

```math
\Phi_1^2+\Phi_2^2+\Phi_3^2=0,\qquad d\Phi_j=0\quad\text{away from poles}.
```

The immersion on the universal cover is

```math
X(p)=X(p_0)+\mathrm{Re}\int_{p_0}^p\boldsymbol\Phi,\qquad dX=\mathrm{Re}\boldsymbol\Phi.
```

**Theorem 22.1 [D] (flat translation/period holonomy).** The 1-form $dX$ defines a **flat abelian translation connection** on the trivial affine $\mathbb R^3$ bundle over $\Sigma^\circ$. Its translational holonomy around a closed loop $\gamma$ is exactly

```math
\mathrm{Hol}_{\rm trans}(\gamma)=\mathrm{Re}\oint_\gamma\boldsymbol\Phi\in\mathbb R^3.
```

**Proof.** Since each $\Phi_j$ is closed off its poles, $d(dX)=0$. On the universal cover integration defines a single-valued $X$; changing the integration path by $\gamma$ changes $X$ by $\mathrm{Re}\oint_\gamma\boldsymbol\Phi$. A global immersion into Euclidean space requires these real translations to vanish; an immersion into a translation quotient permits a selected lattice.

This gives a precise meaning to “the Weierstrass immersion is parallel transport”: it is *affine translation integration in flat ambient $\mathbb R^3$*, not Levi–Civita parallel transport of a tangent vector (which would be governed by the induced nonzero surface curvature). A *moving adapted orthonormal frame* satisfies its own Euclidean Maurer–Cartan equations; its tangent LC part has nonzero curvature and the normal shape operator supplies Gauss–Codazzi.

### 22.1 Four different parallel transport loops on one selected elliptic curve

Even if the Lamé spectral elliptic curve is isomorphic to the Riemann immersion elliptic curve, one can put on it four genuinely different transport constructions: (a) the SL solution matrix varying $u$ at fixed spectral point; (b) the Gauss–Manin system varying the elliptic modulus with transported cycles; (c) the Hopf $U(1)$ connection pulled back along $g_R$ on the fixed elliptic surface; and (d) the flat affine $\mathbb R^3$ connection whose holonomy is the real Weierstrass period vector. **Their monodromies need not agree and act on different fibers.** An exact spectral-curve isomorphism gives a common base for constructing these data; it does not make them one connection.

## 23. The exact Gauss–Manin period gauge is NOT Levi–Civita parallel transport [D,H,K]

In the selected smooth one-gap Lamé and Riemann elliptic families of draft 170, define spectral curve differential periods on a marked cycle $\gamma_{\rm sp}$:

```math
I_0(m_{\rm ell})=\oint_{\gamma_{\rm sp}}\frac{dE}{\eta},\qquad I_1(m_{\rm ell})=\oint_{\gamma_{\rm sp}}\frac{E\,dE}{\eta}.
```

Transport the cycle in the Gauss–Manin local system as the **modulus** $m_{\rm ell}$ varies. Draft 170 derives and checks the explicit rational first-order system

```math
\frac d{dm_{\rm ell}}\binom{I_0}{I_1}=\frac1{2m_{\rm ell}(1-m_{\rm ell})}\begin{pmatrix}2m_{\rm ell}-1&r^{-2}\\-r^2(1-m_{\rm ell}+m_{\rm ell}^2)&1-2m_{\rm ell}\end{pmatrix}\binom{I_0}{I_1}.
```

Its connection matrix has **trace zero**, so the determinant of two independent marked period vectors is constant. In the specified oriented branch-cut basis of draft 170,

```math
I_{0,\alpha}I_{1,\beta}-I_{0,\beta}I_{1,\alpha}=-8\pi i.
```

The affine Lamé–Riemann isomorphism induces a gauge transformation of this connection with an explicit matrix of determinant $-1$, transporting the period pairing to the archived Riemann Gauss–Manin system. This is a **legitimate parallel-transport correspondence of de Rham periods**. It is not the LC curvature of the embedded Riemann surface, the Euclidean affine translation holonomy of its immersion, or the spectral SL carrier matrix (which evolves in $u$ at fixed $E$).

### 23.1 Independent connection and differential markings

The Riemann immersion one-forms reduce, modulo exact meromorphic differentials, to the holomorphic and second-kind period span of $dg_R/y_R$ and $g_Rdg_R/y_R$. Through the selected spectral curve isomorphism these become the span of $dE/\eta$ and $E\,dE/\eta$; **periods are transported with explicit scale factors**. The Lamé spectral quasimomentum is another specifically normalized *second-kind differential*, with a pole at spectral infinity; it is not the Riemann holomorphic height differential. The Baker–Akhiezer function depends on yet another divisor/line-bundle marking.

**Theorem 23.1 [D,H] (typed simultaneous realization).** The same smooth elliptic curve can carry at least three independent compatible structures: a finite-gap spectral pair $(L,A)$ with a marked BA divisor; a flat Gauss–Manin period local system varying with the curve modulus; and a meromorphic Weierstrass immersion triple on a punctured curve. An explicit elliptic curve isomorphism transports the specified **curve and differential** data, but it does not by itself equate the respective connection one-forms, carrier evolution variables, operator spectra, or Euclidean immersion period-closing conditions.

## 24. Conditional weighted SL–EP–geometry correspondence theorem [D,K,H,C]

**Theorem 24.1 (foundation-to-realization interface).** Fix the canonical $r,c,\mu>0$ and a positive-coefficient scalar SL expression. The following arrows hold, under the stated independent hypotheses.

**Layer I: weighted metric and local algebra.** The data $(p,w,q_0)$ define a weighted one-manifold $(g=w\,dx^2/p,d\nu=w\,dx)$, Green identity and constrained variational Hessian. A Liouville half-density transforms its scalar equation locally to a Schrödinger carrier, and carries weighted $L^2$ and Wronskians exactly. A *real* carrier with chosen positive Gram form produces Riccati, a positive EP amplitude with constant Wronskian strength, and the exact Schwarzian clock transformation of §6.

**Layer II: selected surface geometry.** Upon independently choosing an oriented **two-dimensional** immersion and coframe, the LC and teleparallel connections are related by contortion; on the catenoid the torsion coefficient $rSW$ reconstructs $K_C=-r^2S^4$. A Killing symmetry produces a separated **weighted** SL Jacobi equation. This does not make the 1D Darboux factorization a torsion identity.

**Layer III: selected integrable/spectral completion.** For the archived Sato rank-one point or a properly decorated smooth Krichever curve, a Baker function solves the selected Lax eigenproblem and a tau/determinant encodes the potential. The one-gap Lamé spectral elliptic curve is explicitly isomorphic, after a specified modulus match and real form, to the Riemann elliptic curve, and its marked period differentials are transported by a Gauss–Manin gauge. Neither construction supplies a self-adjoint Hilbert domain or a meromorphic minimal immersion automatically.

**Layer III geometric realization.** If one separately chooses compatible Weierstrass data, the immersion is the flat affine integral $\mathrm{Re}\int\boldsymbol\Phi$; **real period closing** is a global constraint. On the catenoid/helicoid associate family, the Bonnet angle rotates these periods while leaving the Hopf Chern degree unchanged. The Riemann Gauss map has degree two, catenoid degree one, giving different topological Hopf pullbacks.

**Layer IV typed model equations.** The Lewis–Riesenfeld invariant and the time-dependent harmonic-trap Schrödinger lens map follow from an **independently selected oscillator Hamiltonian** and EP clock. Critical-power or tuned-coupling conditions are needed for a fixed-coefficient Gross–Pitaevskii transform. PDM supplies an SL kinetic principal symbol but retains the von Roos ordering potential. The FRW constraint is a reciprocal first integral on the Master separatrix, and Keller–Miksis becomes EP only after the stated conservative Sundman and polytropic-exponent reductions.

**Proof.** §§2–6 derive the weighted and projective equivalences; §§7–11 compute the actual connection and factorization distinctions; §§12–17 derive the selected application transformations; §§18–23 give the archived Grassmannian/finite-gap data, the explicit Hopf and affine transport, and the marked Gauss–Manin theorem. Global self-adjointness, positivity, curve decorations, surface completeness and period constraints are **separate hypotheses**, not conclusions of local differential algebra.

**Status of the theorem:** A rigorous **conditional dictionary with checked component identities**, not a universal equivalence between all nonlinear ODEs, all spatial Hilbert operators, all teleparallel geometries or all minimal surfaces. Its strength is that every arrow has specified source, target and preserved datum.

## 25. Complete r=2 and c-preserving regression [D,V]

Set $r=2$, leave $c,\mu>0$, and keep independent temporal, angular and spectral variables separate. The canonical rational forms are

```math
u=\ln(x/c),\qquad S_2=\frac{2c^2x^2}{x^4+c^4},\quad W_2=\frac{x^4-c^4}{x^4+c^4},\quad f_\mu(x;2,c)=\frac{c^2x}{\sqrt\mu(x^4+c^4)}.
```

Weighted metric/measure and exact half-split are

```math
g=x^{-2}dx^2=du^2,\quad d\nu=x\,dx=x^2du,\quad\|f_\mu\|^2_{L^2(xdx)}=\frac1{4\mu}.
```

```math
\int_0^c f_\mu\,dx=\int_c^\infty f_\mu\,dx=\frac{\pi}{8\sqrt\mu}.
```

The canonical reciprocal positive separatrix and its algebraic FRW constraint are

```math
a=\mu^{1/4}\sqrt{\cosh(2u)},\quad a_{uu}=a+\mu a^{-3},\quad H_a=a_u/a=\tanh(2u),\quad H_a^2=1-\mu/a^4.
```

At finite Master energy $\varepsilon_N$, the exact correction is

```math
a_{uu}=a+\mu a^{-3}+\frac{3\varepsilon_N}4a^5,\qquad H_a^2=1-\mu/a^4+\frac{\varepsilon_N}4a^4.
```

The catenoid metric/teleparallel torsion/LC curvature are

```math
g_C=\cosh^2(2u)(du^2+dv^2),\qquad t_2=2S_2W_2,\qquad K_C=-4S_2^4.
```

The Riccati Darboux factorization instead gives

```math
A=\partial_u+2W_2,\qquad A^\dagger A=-\partial_u^2+4-8S_2^2.
```

They are **different identities**. For the same catenoid $g_C$ the pulled-back Hopf Chern class has $c_1=1$, and the marked height period is $\oint dh_C=\pi i$; the helicoid Bonnet associate has real period $-\pi$. For the separately selected Riemann elliptic example with Gauss-coordinate degree two one has $c_1=2$, while real immersion periods still depend on $\lambda_R,A_R$ and cycles.

At $\lambda_R=1$ the selected smooth one-gap Lamé elliptic parameter is $m_{\rm ell}=1/2$, its spectral branch values are $(-2,0,2)$, and its algebraic map to the symmetric Riemann elliptic fiber is

```math
g_R=-E/2,\qquad y_R=\frac{\sqrt2}{4}\eta,\qquad\frac{dg_R}{w_R}=-\sqrt2\frac{dE}{\eta}.
```

The distinct specializations $m_{\rm ell}\to1$ and $m_{\rm ell}\to0$ yield respectively the catenoid logarithmic height differential and the original arctangent primitive on rational nodal normalizations (draft 170). They do **not** identify the SL spatial variable $u$ with the elliptic spectral energy $E$ as one isospectral flow.

## 26. Verification register, source provenance, and remaining problems

### 26.1 Direct mathematical checks

1. **Weighted SL:** using $g=w/p$ and $\rho=\sqrt{pw}$, direct coordinate divergence gives $\Delta_{g,\rho}=w^{-1}(p\partial_x)_x$; Green's identity and constrained Euler–Lagrange variation reproduce SL exactly.
2. **Liouville half-density:** $t_x=\sqrt{w/p}$ and $\chi=(pw)^{1/4}$ preserve the norm and Wronskian, mapping the canonical $(p,w,q_0)=(x^3,x,(r^2-1)x)$ to $-\partial_u^2+r^2$.
3. **Conformal cylinder and radial PDE:** $x=ce^u$ gives the punctured Euclidean conformal cylinder. Direct differentiation of $F=y/x$ in 4D yields $\Delta F=x^{-3}(y_{uu}-y)$ and the exact $r$-dependent inverse-square correction.
4. **Geometric separation:** catenoid angular Fourier modes produce a weighted Jacobi SL equation with weight $R^2$, while its genuine unitary conjugate has leading coefficient $S^2$. Its zero equation alone does not determine its complete spectrum.
5. **EP clock and Schwarzian:** independent differentiation gives $y_{uu}+\omega^2y=\rho^{-3}(Y_{\tau\tau}+k_{\rm EP}Y)$ and $\{\tau,u\}=-2\rho_{uu}/\rho$.
6. **Two connections:** from $\theta^1=Rdu,\theta^2=Rdv$, $d\theta^2=rSW\,\theta^1\wedge\theta^2$ and $\omega^{LC}{}^1{}_2=-rWdv$, symbolic differentiation gives $K_C=-e_1(t_2)-t_2^2=-r^2S^4$ exactly.
7. **Bochner versus Darboux:** expansion of $A^\dagger A$ gives $-\partial_u^2+h^2-h_u$; 1D torsion vanishes identically. The Bochner–Weitzenböck curvature term acts on forms/bundles, not a generic scalar Riccati potential.
8. **Reciprocal Duffing:** the substitution $a=y^{-1/2}$ with the full Master energy gives $a_{uu}=\frac14r^2a+\frac14\mu r^2a^{-3}+\frac34\varepsilon_Na^5$, verified by SymPy with symbolic derivatives. The finite-energy FRW constraint and its derivative follow without dividing by a vanishing $a$.
9. **Lewis and harmonic lens:** differentiating $Q=q/\rho$, $P=\rho p-\rho_tq$ gives $Q_t=P/\rho^2$, $P_t=-\omega_0^2Q/\rho^2$ and conserved $I_{\rm EL}$. The time-dependent Schrödinger lens is the associated unitary dilation/chirp.
10. **GP critical exponent:** the lens scaling of $|\Psi|^{2\sigma}\Psi$ produces coupling $g(t)\rho^{2-d\sigma}$; it stays constant without tuning exactly for $d\sigma=2$.
11. **PDM ordering:** expansion of both von Roos terms yields the exact scalar ordering difference of §16; the BenDaniel–Duke principal part remains a weighted SL expression.
12. **Keller–Miksis limit:** direct Sundman differentiation of $Y=X^{3/2}$ and $d\tau/dt=1/X$ gives the reduced pressure ODE. A selected polytropic index $\gamma=2$ is required for the inverse-cubic Pinney term.
13. **Sato/Krichever:** the actual H136 archived Grassmannian gluing condition, rank-one basis, stabilizer, tau and Baker function were inspected. The historical KdV reduction and finite-gap operator conclusions retain their verified or quoted status, not a new universal theorem.
14. **Hopf:** direct differentiation of $\eta_g=(1,g)/\sqrt{1+|g|^2}$ gives $\mathcal A_g$, $\mathcal F_g$ and $\int\mathcal F_g/(2\pi)=\deg g$. The catenoid Gauss map has degree one and the Riemann elliptic coordinate projection degree two.
15. **Bonnet and affine periods:** $e^{i\delta}$ rotates the real/imaginary immersion periods without changing $g$; $\mathrm{Re}\oint\boldsymbol\Phi$ is the exact holonomy of a flat affine translation connection.
16. **Parameter separation:** the elliptic coordinate $g_R(E)$ is constant along spatial SL evolution at fixed $E$. A chosen surface parametrization $t(s)=e^{r\zeta}$ entails a moving $s(\zeta)$ and therefore a moving spectral coordinate, so cannot be called the original isospectral carrier flow.
17. **Resolution test:** for $r=2$, the canonical rational profile, weighted norm, EP/FRW forms, teleparallel curvature, Darboux operator, catenoid height period and symmetric elliptic differential scales were checked against the formulas of drafts 130–170.

### 26.2 Historical ZIP references, with scope

- H136, 04-follow-ups/sato-grassmannian.md: verified rank-one Grassmannian point, KdV reduction, tau and BA function; general Segal–Wilson/Krichever statements remain classical quoted inputs. The higher-level defect formula explicitly prevents declaring generic level-nine evolution a straight one-point Jacobian flow.
- H73/H100/H299 and 00-meta/INTEGRABLE.md: checked PT Darboux/shape-invariant and Lax–Novikov operator identities; they are **not** the Bochner–Weitzenböck formula.
- 04-follow-ups/friedmann-reciprocal-envelope.md: verified reciprocal EP plus *finite-energy quintic*, kinematic FRW constraint, multiple clock/curve distinctions and conditional warped-metric realization.
- H376, 04-follow-ups/bpst-yamabe-eguchi-hanson.md and the Complete Reference §25: controlled Keller–Miksis to Rayleigh–Plesset/Sundman/EP path, including caveats about compressibility, forcing and gas-law exponents.
- H466–H470 and drafts 150–170: Riemann Weierstrass, Gauss–Manin and marked period data, explicit one-gap Lamé elliptic isomorphism, and distinct nodal catenoid and original arctangent differentials.

### 26.3 Independent external references consulted

- Standard Bochner–Weitzenböck formula for forms and the Levi–Civita Laplacian: https://math.bu.edu/people/sr/articles/book.pdf .
- Teleparallel/contortion versus Levi–Civita curvature: https://pmc.ncbi.nlm.nih.gov/articles/PMC5080365/ .
- Stäckel/Robertson separation conditions for Schrödinger/Laplace–Beltrami: https://www.sciencedirect.com/science/article/pii/S0375960113007135 ; https://harvest.aps.org/v2/journals/articles/10.1103/RevModPhys.86.1283/fulltext .
- Krichever data, BA function and the map to the Sato Grassmannian: https://www.math.columbia.edu/department/krichever/Igor60/pdfs/2005-2009/2006-ILEATRP.pdf ; https://doi.org/10.4213/im9533e .
- Lewis–Riesenfeld exact time-dependent oscillator invariant: https://inspirehep.net/literature/52790 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC9778280/ .
- Nonlinear GP/NLS harmonic-lens mapping and coupling condition: https://journals.aps.org/pra/abstract/10.1103/PhysRevA.67.063610 .
- PDM ordering ambiguity: https://doi.org/10.1103/PhysRevB.27.7547 ; https://www.scielo.br/j/rbef/a/8gHrhh3Yr4s7ymwZZ3TsBkj/?format=html .
- Keller–Miksis equation including compressibility and pressure derivatives: https://pmc.ncbi.nlm.nih.gov/articles/PMC8050038/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC6364854/ .
- Riemann minimal examples and global Gauss/period geometry: https://arxiv.org/abs/1609.05660 .

### 26.4 Next mathematical tasks

1. **Teleparallel Hodge operator:** explicitly compute the LC Hodge–de Rham Laplacian on catenoid one-forms and its decomposition using teleparallel contortion and torsion. Only then test a genuine relation to a first-order Dirac/SUSY factorization.
2. **Spectral versus bundle lift:** construct a natural normalized BA eigenvector line bundle over the selected Lamé spectral curve and calculate its Hermitian/Berry connection. Compare its pole divisor and curvature with the pullback Hopf connection of the Riemann Gauss map, instead of identifying them by projective analogy.
3. **Riemann Jacobi separation:** derive the exact induced metric, global quotient and separated stability operator for Riemann minimal examples; compare its spectral curve, if any, with the chosen Lamé index-one Lax curve. Same elliptic base alone does not imply equality of Jacobi and finite-gap operators.
4. **Stäckel/Killing-tensor classification:** determine which of the framework's separations are generated by genuine commuting geometric differential operators and which require additional nonorthogonal or conformal separation factors.
5. **Full EP–Schwarzian domain:** classify positive Gram gauges through zeros, turning points, poles and real singular endpoints; identify which gauges extend to global self-adjoint unitary equivalences and which are only local.
6. **Krichever divisor from inverse scattering:** match the H136 rank-one gluing parameter with the complete PT norming data of draft 150 and track it through the smooth Lamé-to-nodal degeneration. Curve isomorphism alone cannot determine the gluing divisor.
7. **PDM operator ordering:** test whether the von Roos scalar corrections can be realized as curvature or density-potential terms for a **declared higher-dimensional or bundle geometry**, avoiding the false claim of 1D torsion.
8. **Master finite-energy envelope:** classify the quintic-deformed reciprocal EP equation, its Hamiltonian, phase-space period and binary quartic/elliptic quotient; retain the explicit $\varepsilon_Na^5$ term.
9. **Geometric Hopf degree:** prove the Riemann Gauss map degree-two Chern formula including precise patch transitions at its planar ends, and compute independent Berry holonomy along real cycles. The Chern class alone does not fix those holonomies.
10. **Time-dependent GP:** characterize the precisely tuned noncritical coupling $g(t)$ and domain regularity needed for the oscillator lens map to extend globally in time, and separate bounded EP envelopes from finite-time envelope blow-up.

**Final structural boundary.** There is a mathematically rigorous weighted geometric source of SL and a local EP clock/projective lift. A chosen 2D coframe supplies a separate LC–teleparallel torsion/curvature dictionary. Sato/Krichever supplies a selected integrable curve/operator/BA dictionary; explicit marked elliptic curve maps supply a separate Gauss–Manin and Weierstrass period correspondence; a Hopf lift has its own degree and connection. Applications require their own Hamiltonian, measure, pressure law, nonlinear coupling or metric. The unifying principle is **typed maps preserving declared invariants**, not one universal physical model or one globally identical connection.
