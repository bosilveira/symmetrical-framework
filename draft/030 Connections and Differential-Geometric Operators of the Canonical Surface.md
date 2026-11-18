---
id: SF-DRAFT-030
title: Connections and Differential-Geometric Operators of the Canonical Surface
status: provisional
created: 2026-11-18
proposed_layers: [I, II, III]
depends_on: [SF-I-000, SF-I-010, SF-I-020, SF-DRAFT-010, SF-DRAFT-020]
related_claims: [H100, H114, H117, H248, H300, H421, H424, H466, H467, H468, H473, H474, H490, H516, H538]
---

# 030 Connections and Differential-Geometric Operators of the Canonical Surface

**Status:** Complete provisional mathematical investigation. No assertion of historical novelty; individual results require review before migration into canonical chapters.

**Question:** Do Gauss-Codazzi, Levi-Civita, Weitzenböck, Maurer-Cartan, Kähler, catenoid–helicoid–Riemann minimal examples, Weierstrass, Gudermannian, Riccati, Möbius, Schwarzian, gradient, Jacobian, Hessian, Laplacian, Hamiltonian, Lagrangian, Routhian and Wronskian belong to a single consistent system of typed differential-geometric maps?

**Answer:** They form a coherent **network** of constructions with shared data, but neither a unique mechanism nor a universal equivalence of second-order ODEs/PDEs/SDEs. In particular: the flat ambient adapted-frame Maurer-Cartan connection, curved intrinsic Levi-Civita connection, and flat torsionful tangent Weitzenböck connection are three different structures; the covariant Hessian, complex Hessian and vertical Lagrangian Hessian are distinct; and the Routhian for catenoid geodesics is not the catenoid surface-area functional. Each exact arrow below specifies its additional assumptions.

**Sources:** Current main branch: SF-I-000, SF-I-010, SF-I-020, draft SF-DRAFT-010 and draft SF-DRAFT-020. Earlier ZIP symmetrical-framework-update-2026-11-18-bu.zip: 00-meta/CLAIMS.md and NOTATION.md; historical foundational-paper-draft-v0.3.md; follow-ups/fundamental-forms-willmore-hopf.md, riemann-marked-periods-gauss-manin-x04.md, lame-complement-special-loci-riemann-master.md; selected verification records, notably H421–H428, H466–H474, H490, H516, H538. The attached Pasted text(20261118-164335).txt is a **research suggestion**, not independent verification. External sources are recorded in §18. The ZIP reflects an older project layout, not the current main-branch navigation.

**Evidence:** [K] established classical theorem; [D] derived step by step in this document; [V] independently checked by exact symbolic substitution; [H] archived claim requiring its own evidence scope; [C] correction to the suggestion; [O] open.

## 1. Typed architecture and parameter convention

The following are distinct inputs: scalar fields, a linear solution space, a Riemannian metric, a chosen orthonormal frame, an immersion with its second fundamental form, a complex structure, a variational functional and an operator domain. A transformation between them may be a pullback, gauge, projection, reduction or noninvertible quotient; these operations are not interchangeable.

| Input | Operation | Output | Required additional data |
|---|---|---|---|
| Scalar backbone | derivative, first integral | Riccati and nonlinear Master ODE | energy and nonzero-domain hypotheses |
| Two-dimensional solution space | projectivization | Riccati and Schwarzian | chosen solution basis/projective chart |
| Immersion | Jacobian metric pullback | first fundamental form | ambient metric |
| Metric | Levi-Civita construction | torsion-free covariant derivatives and curvature | none beyond differentiability/nondegeneracy |
| Metric plus frame | teleparallelization | flat Weitzenböck connection and torsion | chosen orthonormal parallel frame |
| Metric plus symmetric second form | Gauss-Codazzi | local immersed surface | ambient space form, compatibility, topology |
| Holomorphic Gauss data | Weierstrass integration | minimal/maximal immersion | real structure, nondegeneracy, periods |
| Complex structure plus Kähler metric | complex Hessian | local Kähler potential | potential gauge |
| Lagrangian | Euler-Lagrange/Legendre | second-order flow/Hamiltonian | regularity and chosen time |
| Metric plus cyclic symmetry | Routh reduction | reduced Lagrangian | fixed conserved momentum |
| Metric plus differential operator | trace/adjoint | Laplacian, Hessian, Green pairing | domain and boundary conditions for spectral use |
| Metric plus stochastic data | generator/Itô rule | diffusion or SDE | noise, drift, stochastic convention |

The fundamental layer is the **objects and their exact maps**. Familiar theories in the outer layers are named only when a specific valid map has been constructed.

## 2. Canonical scalar backbone [D]

Fix the independent parameters and coordinates:

```math
x>0,\quad r>0,\quad c>0,\quad \mu>0,\qquad u=\ln(x/c),\qquad x=ce^u,\qquad \theta=ru.
```

Introduce a new real surface coordinate $`v`$, a complex coordinate $`\zeta=u+iv`$, and the centered scalar functions

```math
S=\mathrm{sech}(ru),\quad W=\tanh(ru),\quad R=\cosh(ru),\quad h=\ln R.
```

Their identities are

```math
S_u=-rSW,\qquad W_u=rS^2,\qquad R_u=rRW,\qquad S^2+W^2=1,\qquad R S=1.
```

Consequently,

```math
h_u=rW,\qquad h_{uu}=r^2S^2,\qquad h_u^2+r^2e^{-2h}=r^2.
```

The original function is

```math
f_\mu(x;r,c)=\frac{S}{2\sqrt{\mu}\,x},\qquad y(u)=2xf_\mu(x;r,c)=\mu^{-1/2}S.
```

The cubic Master ODE and its energy are

```math
y_{uu}=r^2y-2\mu r^2y^3,\qquad \varepsilon_N=y_u^2-r^2y^2+\mu r^2y^4.
```

The geometry below is a *chosen* realization with new coordinate $`v`$. It does not follow uniquely from the scalar function.

## 3. Catenoid: Jacobian, metric, shape and curvature [D,V,H424]

Let $`v`$ be periodic with period $`2\pi/r`$ when discussing the global catenoid. Define

```math
X(u,v)=\left(\frac{R}r\cos(rv),\frac{R}r\sin(rv),u\right).
```

Differentiate:

```math
X_u=(\sinh(ru)\cos(rv),\sinh(ru)\sin(rv),1),\qquad X_v=(-R\sin(rv),R\cos(rv),0).
```

The $`3\times 2`$ Jacobian $`DX=[X_u\ \ X_v]`$ gives the pullback metric:

```math
(DX)^T DX=R^2\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad I=X^*g_{\mathbb R^3}=R^2(du^2+dv^2),\qquad dA_I=R^2\,du\,dv.
```

The oriented normal from $`X_u\times X_v`$ is

```math
N=(-S\cos(rv),-S\sin(rv),W).
```

Pairing the second derivatives of $`X`$ with $`N`$ yields

```math
II_{uu}=-r,\qquad II_{uv}=0,\qquad II_{vv}=r,\qquad II=-r\,du^2+r\,dv^2.
```

Therefore the shape operator, mean curvature and Gaussian curvature are

```math
B=I^{-1}II=\mathrm{diag}(-rS^2,rS^2),\qquad H_m=0,\qquad K_I=-r^2S^4.
```

**Gauss-Codazzi verification.** With the conformal factor $`I=e^{2h}(du^2+dv^2)`$, intrinsic curvature is $`K_I=-e^{-2h}\Delta_0h`$ with $`\Delta_0=\partial_u^2+\partial_v^2`$. Thus

```math
K_I=-R^{-2}h_{uu}=-r^2S^4=\det B.
```

The Hopf quadratic differential is constant, so the Codazzi equation holds:

```math
Q_H\,d\zeta^2=-\frac r2\,d\zeta^2,\qquad \partial_{\bar\zeta}Q_H=0.
```

The local fundamental theorem of surface theory [K] reconstructs a compatible immersion on a simply connected patch; it does not automatically solve a global period or embedding problem.

## 4. Three distinct connections [D]

Let $`E_1=X_u/R`$, $`E_2=X_v/R`$, and $`F=(E_1,E_2,N)`$ be the oriented ambient adapted frame. Its matrix-valued Maurer-Cartan form is

```math
\Omega=F^{-1}dF=\begin{pmatrix}0&-rW\,dv&rS\,du\\rW\,dv&0&-rS\,dv\\-rS\,du&rS\,dv&0\end{pmatrix}.
```

It satisfies

```math
d\Omega+\Omega\wedge\Omega=0.
```

The $`(1,2)`$ component is, explicitly,

```math
d(-rW\,dv)+(rS\,du)\wedge(rS\,dv)=-r^2S^2\,du\wedge dv+r^2S^2\,du\wedge dv=0.
```

This zero-curvature equation concerns the **full ambient $`SO(3)`$ frame**. Its tangent block is a generally curved Levi-Civita connection, while the off-diagonal blocks hold extrinsic data. A new connection that declares the tangent frame parallel is the separate Weitzenböck construction of §6. The statement “all three are the same flat connection” is false.

## 5. Levi-Civita connection and geodesic equations [D,V]

For $`g=R^2(du^2+dv^2)`$, the nonzero Levi-Civita coefficients are

```math
\Gamma^u_{uu}=h_u,\qquad \Gamma^u_{vv}=-h_u,\qquad \Gamma^v_{uv}=\Gamma^v_{vu}=h_u,\qquad h_u=rW.
```

These follow from the metric formula

```math
\Gamma^k_{ij}=\frac12 g^{k\ell}(\partial_i g_{\ell j}+\partial_jg_{\ell i}-\partial_\ell g_{ij}).
```

For a curve $`\gamma(t)=(u(t),v(t))`$, the geodesic equation $`\nabla^{LC}_{\dot\gamma}\dot\gamma=0`$ reads

```math
\ddot u+h_u(\dot u^2-\dot v^2)=0,\qquad \ddot v+2h_u\dot u\dot v=0.
```

Choose the oriented orthonormal coframe

```math
\vartheta^1=R\,du,\qquad \vartheta^2=R\,dv,\qquad e_1=R^{-1}\partial_u,\qquad e_2=R^{-1}\partial_v.
```

In the same tangent-frame convention as SF-DRAFT-010, the Levi-Civita connection form and its curvature are

```math
\omega^{LC}_{12}=-h_u\,dv=-rW\,dv,\qquad d\omega^{LC}_{12}=-h_{uu}\,du\wedge dv=K_I\,\vartheta^1\wedge\vartheta^2.
```

This connection is torsion-free and metric-compatible, with **nonzero Gaussian curvature**.

## 6. Tangent Weitzenböck connection and an exact curvature–torsion relation [D,V]

The open catenoid cylinder is parallelizable. Choose the above orthonormal tangent frame and **define a different connection** $`\widetilde\nabla`$ by making $`e_1,e_2`$ parallel:

```math
\widetilde\nabla e_1=0,\qquad \widetilde\nabla e_2=0.
```

In the coordinate convention $`\widetilde\nabla_{\partial_i}\partial_j=\widetilde\Gamma^k{}_{ij}\partial_k`$,

```math
\widetilde\Gamma^k{}_{ij}=e_a{}^k\,\partial_i\vartheta^a{}_j=h_i\delta^k{}_j.
```

Only two coefficients are nonzero:

```math
\widetilde\Gamma^u{}_{uu}=h_u,\qquad\widetilde\Gamma^v{}_{uv}=h_u.
```

**Metric compatibility proof.** Since $`\partial_i g_{jk}=2h_i g_{jk}`$, we find

```math
(\widetilde\nabla_i g)_{jk}=2h_i g_{jk}-\widetilde\Gamma^\ell{}_{ij}g_{\ell k}-\widetilde\Gamma^\ell{}_{ik}g_{j\ell}=0.
```

**Flatness proof.** The connection matrices are $`(\widetilde\Gamma_i)^k{}_j=h_i\delta^k{}_j`$, so they commute, and $`\partial_i h_j-\partial_j h_i=0`$. Thus $`\widetilde R=0`$.

**Torsion.** With $`T(X,Y)=\widetilde\nabla_XY-\widetilde\nabla_YX-[X,Y]`$,

```math
T^k{}_{ij}=h_i\delta^k{}_j-h_j\delta^k{}_i,\qquad T^v{}_{uv}=h_u=rW.
```

The oriented orthonormal frame has

```math
[e_1,e_2]=-\frac{h_u}{R}e_2,\qquad T(e_1,e_2)=t\,e_2,\qquad t=\frac{h_u}{R}=rSW.
```

**Theorem 6.1 (curvature from the chosen teleparallel torsion).** For any positive conformal factor $`R(u)`$ in this one-variable metric and this frame, the intrinsic Gaussian curvature obeys

```math
K_I=-e_1(t)-t^2=-\frac1R\frac{dt}{du}-t^2,\qquad t=\frac{R'}{R^2}.
```

**Proof, step by step.**

1. Compute the coframe exterior derivatives:

```math
d\vartheta^1=0,\qquad d\vartheta^2=R'\,du\wedge dv=t\,\vartheta^1\wedge\vartheta^2.
```

2. The torsion-free Levi-Civita connection form is $`\omega_{12}^{LC}=-t\vartheta^2`$.
3. Differentiate:

```math
d\omega_{12}^{LC}=-dt\wedge\vartheta^2-t\,d\vartheta^2=-(e_1(t)+t^2)\vartheta^1\wedge\vartheta^2.
```

4. Compare with $`d\omega_{12}^{LC}=K_I\,\vartheta^1\wedge\vartheta^2`$.
5. For $`R=\cosh(ru)`$, substitute $`t=rSW`$ and use the canonical derivatives:

```math
e_1(t)=r^2(S^4-S^2W^2),\qquad t^2=r^2S^2W^2,\qquad K_I=-r^2S^4.
```

This exact local identity depends on the **selected frame and associated teleparallel connection**. The metric does not canonically select a unique flat Weitzenböck connection, and the same construction cannot always be globally implemented on a nonparallelizable surface.

### 6.1 Geodesics use contorsion, not antisymmetric torsion itself

Define the tensor $`C=\widetilde\nabla-\nabla^{LC}`$. Then

```math
\nabla^{LC}_{\dot\gamma}\dot\gamma=0\quad\Longleftrightarrow\quad\widetilde\nabla_{\dot\gamma}\dot\gamma=C(\dot\gamma,\dot\gamma).
```

The independent nonzero coordinate components are

```math
C^u{}_{vv}=h_u,\qquad C^v{}_{vu}=-h_u.
```

Raw torsion cannot be contracted twice with one velocity to produce this term because

```math
T^k{}_{ij}\dot x^i\dot x^j=0
```

by antisymmetry. This explicitly corrects the suggested “torsion-force” formula. Teleparallel autoparallels and Levi-Civita geodesics are not generically the same curves without the appropriate contorsion relation.

### 6.2 Total curvature check and the boundary

The surface area form gives

```math
K_I\,dA_I=-r^2S^2\,du\,dv=-h_{uu}\,du\,dv.
```

For the finite cylinder $`[-U,U]\times S^1`$ with angular period $`2\pi/r`$,

```math
\int K_I\,dA_I=-\frac{2\pi}{r}[h_u(U)-h_u(-U)]=-4\pi\tanh(rU).
```

Taking $`U\to\infty`$ yields

```math
\int_{\mathrm{catenoid}}K_I\,dA_I=-4\pi.
```

The catenoid is noncompact; one must include boundary terms when using Gauss-Bonnet on finite truncated cylinders. The value $`-4\pi`$ is not obtained by incorrectly applying the closed-surface Gauss-Bonnet theorem.

## 7. Projectivization, Möbius maps and the precise Riccati clocks [D,V,H516]

Consider the linear pair

```math
\psi_{uu}=\frac{r^2}{4}\psi,\qquad \psi_+=e^{ru/2},\quad \psi_-=e^{-ru/2}.
```

For a general $`2\times 2`$ first-order system $`\Psi'=A\Psi`$ with $`\Psi=(a,b)^T`$ and $`F=a/b`$ where $`b\ne0`$,

```math
F'=A_{12}+(A_{11}-A_{22})F-A_{21}F^2.
```

This is a Riccati equation, the local expression of projectivizing the linear connection. Its coefficients depend on the chosen connection and gauge; a general spinor quotient is not automatically a uniquely determined Gauss map.

For our diagonal pair,

```math
F=\psi_+/\psi_-=e^{ru},\qquad F_u=rF.
```

The Möbius image **at half-angle** is

```math
T=\frac{F-1}{F+1}=\tanh(ru/2),\qquad T_u=\frac r2(1-T^2).
```

The canonical full-angle $`W=\tanh(ru)`$ is instead

```math
W=\frac{F^2-1}{F^2+1}=\frac{2T}{1+T^2},\qquad W_u=r(1-W^2).
```

**Correction:** $`W`$ is Möbius in $`F^2`$, not Möbius in $`F`$. This affects Schwarzian normalization and the exact meaning of a Cayley transform.

The Gudermannian angle $`\eta=\mathrm{gd}(ru)`$ satisfies

```math
\sin\eta=W,\quad \cos\eta=S,\quad \tan\eta=\sinh(ru),\quad \tan(\eta/2)=T.
```

These are real chart identities. A sphere and hyperbolic disk are not globally isometric by this angle substitution; they have different Gaussian curvature.

## 8. Schwarzian, Wronskian and separate Hopf data [D,V]

The Schwarzian of a locally univalent $`F`$ is

```math
\{F,u\}=\frac{F_{uuu}}{F_u}-\frac32\left(\frac{F_{uu}}{F_u}\right)^2.
```

Exact differentiations give

```math
\{e^{ru},u\}=-\frac{r^2}{2},\qquad \{T,u\}=-\frac{r^2}{2},\qquad \{W,u\}=-2r^2.
```

Thus the half-angle Möbius pair shares a Schwarzian; the full-angle pair has a factor four different.

For a normal-form linear equation $`\psi''+Q\psi=0`$ with two independent solutions $`\psi_1,\psi_2`$ and our Wronskian sign convention,

```math
\mathscr W=\psi_1\psi_2'-\psi_1'\psi_2,\qquad \mathscr W'=0,\qquad (\psi_1/\psi_2)'=-\mathscr W/\psi_2^2.
```

Hence

```math
\{\psi_1/\psi_2,u\}=2Q.
```

The Wronskian is the conserved symplectic area of two phase-space solution vectors $`(\psi,\psi')`$. It is not automatically a differential form on the cotangent bundle of the catenoid; such an identification requires a specified phase-space map.

### The Gauss map's Schwarzian does not uniquely determine bending

The catenoid's holomorphic stereographic Gauss map and Weierstrass one-form can be taken as

```math
G(\zeta)=-e^{r\zeta},\qquad\omega=-e^{-r\zeta}\,d\zeta.
```

The projective Schwarzian is

```math
\{G,\zeta\}=-r^2/2.
```

Its Hopf differential, in the Weierstrass convention of SF-DRAFT-020, is

```math
Q_H=-\frac12\omega\,dG=-\frac r2\,d\zeta^2.
```

**Counterexample to a proposed universal identification.** Replace $`\omega`$ by $`a\omega`$ for any $`a>0`$, keeping $`G`$ fixed. The Schwarzian is unchanged, but $`Q_H`$ is multiplied by $`a`$ and the induced first form by $`a^2`$. Thus the Schwarzian does not by itself recover $`II`$; the complete Weierstrass or additional geometric data are essential.

## 9. Kähler potential, covariant Hessian, gradient and Laplacian [D,V]

The logarithmic conformal factor $`h=\ln R`$ is **not** a Kähler potential for the catenoid induced metric in the chosen coordinates. The correct local potential satisfying $`\mathcal K_{C,uu}=R^2`$ is

```math
\mathcal K_C(u)=u^2/4+\cosh(2ru)/(8r^2),\qquad \mathcal K_{C,uu}=\cosh^2(ru)=R^2.
```

In the convention $`g=4\partial_\zeta\partial_{\bar\zeta}\mathcal K\,|d\zeta|^2`$, this produces $`I`$.

On the other hand, $`h`$ is a local Kähler potential for the **round spherical Gauss-map pullback metric**:

```math
4\partial_\zeta\partial_{\bar\zeta}h=h_{uu}=r^2S^2,\qquad G^*g_{S^2}=r^2S^2|d\zeta|^2=(-K_I)I.
```

The scalar Riemannian covariant Hessian is a different object:

```math
(\mathrm{Hess}_I f)_{ij}=\partial_i\partial_j f-\Gamma^k{}_{ij}\partial_k f,\qquad \Delta_I f=\mathrm{tr}_I\mathrm{Hess}_I f.
```

For $`f=h=\ln R`$ the Christoffel symbols give

```math
(\mathrm{Hess}_I h)_{uu}=h_{uu}-h_u^2=r^2(S^2-W^2),\qquad (\mathrm{Hess}_Ih)_{vv}=h_u^2=r^2W^2.
```

Tracing produces the useful identity

```math
\Delta_Ih=R^{-2}h_{uu}=r^2S^4=-K_I.
```

The metric gradient (the inverse-metric lift of $`dh`$) is

```math
\mathrm{grad}_Ih=R^{-2}h_u\partial_u=rS^2W\,\partial_u.
```

The scalar Laplace-Beltrami operator is

```math
\Delta_I=R^{-2}(\partial_u^2+\partial_v^2).
```

This conformal simplification is specifically two-dimensional. A real Hessian metric in affine coordinates, a complex Kähler Hessian and the **velocity-fibre Hessian** of a Lagrangian are different constructions even if all feature two derivatives.

### The Hopf connection and a global holonomy caveat [H538]

For the spherical Gauss map, choose the local Hopf connection

```math
A_H=\frac r2(1+W)\,dv,\qquad F_H=dA_H=\frac{r^2}{2}S^2\,du\wedge dv.
```

It obeys

```math
A_H=\frac r2\,dv-\frac12\omega_{12}^{LC},\qquad F_H=-\frac12d\omega_{12}^{LC}.
```

The difference is locally closed but has circulation $`\pi`$ along the angular cylinder:

```math
\oint_{v\sim v+2\pi/r}\left(A_H+\frac12\omega_{12}^{LC}\right)=\int_0^{2\pi/r}\frac r2\,dv=\pi.
```

Thus its $`U(1)`$ holonomy is $`-1`$, not globally removable by a single-valued periodic gauge on that circle. This is the archived correction H538. The local differential identity and global holonomy are distinct pieces of data.

## 10. Lagrangian, Hamiltonian and Routhian of catenoid geodesics [D,V]

For a curve $`\gamma(t)=(u(t),v(t))`$ on the catenoid, choose the kinetic Lagrangian

```math
L_g=\frac12R(u)^2(\dot u^2+\dot v^2).
```

The fibre Legendre map and its vertical Hessian are

```math
p_u=R^2\dot u,\qquad p_v=R^2\dot v,\qquad \frac{\partial^2L_g}{\partial\dot q^i\partial\dot q^j}=g_{ij}.
```

The Hamiltonian and canonical cotangent symplectic form are

```math
H_g=\frac{p_u^2+p_v^2}{2R^2},\qquad \omega_{\mathrm{can}}=du\wedge dp_u+dv\wedge dp_v.
```

Hamilton's equations are

```math
\dot u=p_u/R^2,\quad \dot v=p_v/R^2,\quad \dot p_u=(R'/R^3)(p_u^2+p_v^2),\quad \dot p_v=0.
```

They reproduce the Levi-Civita geodesic equations of §5. The angular coordinate $`v`$ is cyclic because $`\partial_v`$ is Killing, so $`p_v=\ell`$ is constant.

The **Routhian** is the partial Legendre transform in the cyclic velocity, with convention $`L_R=L_g-\ell\dot v`$:

```math
L_R(u,\dot u;\ell)=\frac12R^2\dot u^2-\frac{\ell^2}{2R^2}.
```

Its Euler-Lagrange equation is

```math
R^2\ddot u+RR'\dot u^2-\frac{\ell^2 R'}{R^3}=0.
```

The conserved reduced energy is

```math
E=\frac12R^2\dot u^2+\frac{\ell^2}{2R^2}.
```

This is the actual Routh reduction of **geodesics in the induced metric**. It must not be conflated with a different variational problem that constructs the catenoid itself.

### The catenoid area functional is not the geodesic Routhian

A rotational surface $`\rho=\rho(z)`$ has area functional

```math
\mathcal A[\rho]=2\pi\int \rho\sqrt{1+\rho_z^2}\,dz.
```

The profile Lagrangian $`L_A=\rho\sqrt{1+\rho_z^2}`$ is independent of $`z`$, so its Beltrami first integral is

```math
L_A-\rho_z\frac{\partial L_A}{\partial\rho_z}=\frac{\rho}{\sqrt{1+\rho_z^2}}=a>0.
```

Thus $`\rho_z^2=\rho^2/a^2-1`$, and integration yields

```math
\rho(z)=a\cosh((z-z_0)/a).
```

Set $`a=1/r`$, $`z-z_0=u`$ to recover the catenoid meridian. This is **Noether/Beltrami conservation for surface area**, not the reduced geodesic angular momentum. The two Lagrangians describe different variational tasks.

The Hamilton-Jacobi equation for geodesics separates by $`\mathcal S(u,v)=U(u)+\ell v`$:

```math
(U')^2=2ER^2-\ell^2.
```

An explicit Stäckel matrix is

```math
\begin{pmatrix}p_u^2\\p_v^2\end{pmatrix}=\begin{pmatrix}R^2&-1\\0&1\end{pmatrix}\begin{pmatrix}2E\\\ell^2\end{pmatrix}.
```

Thus Killing symmetry, Routh reduction and Stäckel separation agree **for this metric and chosen variational problem**.

## 11. Minimal-surface Laplacian, Jacobi Hessian and weighted Sturm-Liouville [D,H424]

For an isothermal immersion in $`\mathbb R^3`$, mean curvature zero implies $`\Delta_I X=0`$. Directly for our $`X`$,

```math
\Delta_I X=R^{-2}(X_{uu}+X_{vv})=0.
```

The squared norm of the shape operator is

```math
|B|^2=2r^2S^4.
```

The Euclidean minimal-surface second-variation/Jacobi operator is

```math
\mathcal J=-\Delta_I-|B|^2=R^{-2}[-\partial_u^2-\partial_v^2-2r^2S^2].
```

For zero modes separated as $`\Psi=\phi_m(u)e^{imrv}`$, $`m\in\mathbb Z`$,

```math
-\phi_m''+[m^2r^2-2r^2S^2]\phi_m=0.
```

This is an order-one Pöschl-Teller potential. It is not the same linear operator as the cubic Master Hessian (which has an order-two Pöschl-Teller potential), though an exact Darboux intertwiner relates the corresponding one-dimensional expressions.

For a general Jacobi spectral eigenvalue $`\lambda`$ the right-hand side is weighted:

```math
-\phi_m''+[m^2r^2-2r^2S^2]\phi_m=\lambda R^2\phi_m.
```

This is a *weighted* Sturm-Liouville problem. Merely multiplying by $`R^2`$ does not give a unitary spectral equivalence in the same Hilbert space. Boundary domains, limit-point/limit-circle behavior and self-adjoint extensions are separate outer-layer choices.

The weighted Wronskian for $`-(p\psi')'+q\psi=\lambda w\psi`$ is constant for two solutions of the **same** spectral equation:

```math
\mathscr W_p=p(\psi_1\psi_2'-\psi_1'\psi_2),\qquad \mathscr W_p'=0.
```

This follows by multiplying the two equations crosswise and subtracting, or from Green's identity.

## 12. Two meanings of Weitzenböck: teleparallel connection versus Bochner identity [K,D]

The **Weitzenböck connection** in §6 is a flat, torsionful connection constructed from a chosen frame.

The distinct **Bochner-Weitzenböck formula** for the Hodge Laplacian on one-forms involves the Levi-Civita connection:

```math
\Delta_H=d\delta+\delta d,\qquad \Delta_H\alpha=\nabla^{LC*}\nabla^{LC}\alpha+\mathrm{Ric}^{\sharp}(\alpha).
```

On a surface, $`\mathrm{Ric}^{\sharp}(\alpha)=K_I\alpha`$.

**Exact catenoid example.** The one-form $`du`$ is closed, and $`\delta du=-\Delta_Iu=0`$ because $`u`$ is harmonic. Hence

```math
\Delta_H(du)=0,\qquad \nabla^{LC*}\nabla^{LC}(du)=-K_I\,du=r^2S^4\,du.
```

This is a curvature identity involving the Hodge and rough Laplacians, not the teleparallel connection. On the full infinite cylinder, $`du`$ is not $`L^2`$ because $`|du|_I^2=R^{-2}`$ and $`dA_I=R^2du\,dv`$. Thus this differential identity does **not** automatically make $`du`$ an eigenvector in the domain of a chosen self-adjoint $`L^2`$ Hodge Laplacian.

## 13. Master Hamiltonian and geometric energy: keep phase spaces separate [D,H473]

The cubic Master ODE in autonomous time $`u`$ has the regular one-dimensional Lagrangian and Hamiltonian

```math
L_M(y,y_u)=\frac12y_u^2+\frac12r^2y^2-\frac12\mu r^2y^4,\qquad H_M(y,p)=\frac12p^2-\frac12r^2y^2+\frac12\mu r^2y^4.
```

The momentum is $`p=y_u`$, and the conserved nonlinear energy is

```math
\varepsilon_N=2H_M.
```

This Hamiltonian lives on the phase plane $`(y,p)`$ and is **not** the catenoid geodesic Hamiltonian $`H_g(u,v,p_u,p_v)`$ on $`T^*`$ of the surface.

The geometric result of SF-DRAFT-010 states that under a specific minimal-surface ansatz for $`z=\sqrt{\mu}y>0`$, with $`I=z^{-2}|d\zeta|^2`$ and constant Hopf coefficient, the cubic Master energy is

```math
k_0=-r^2e=-\mu\varepsilon_N,\qquad e=\mu\varepsilon_N/r^2,
```

where $`k_0`$ is ambient *space-form sectional curvature*. This is a typed reconstruction statement; it requires fixed integration constants and does not identify arbitrary Hamiltonians.

For general level $`q`$, the fixed constant-Hopf space-form ansatz produces $`k_{\mathrm{required}}=-q r^2 e_q z^{2-2q}`$; at nonzero energy and nonconstant profile it is constant within that ansatz only for $`q=1`$. This is a restriction of the ansatz, not a universal geometric no-go theorem.

## 14. Weierstrass-Enneper, Kobayashi and analytic continuation [D,H424]

For the canonical complex coordinate $`\zeta=u+iv`$, choose

```math
G=-e^{r\zeta},\qquad \omega=-e^{-r\zeta}d\zeta.
```

The Euclidean holomorphic null one-form is

```math
\Phi_E=\left(\frac{1-G^2}{2},\frac{i(1+G^2)}2,G\right)\omega=(\sinh(r\zeta),-i\cosh(r\zeta),1)d\zeta.
```

The catenoid is $`\mathrm{Re}\int\Phi_E`$, while the helicoid is the conjugate immersion $`\mathrm{Im}\int\Phi_E`$. Their induced metrics are identical locally but their global angular periods differ (SF-DRAFT-020).

The complex change of ambient null quadratic form

```math
D=\mathrm{diag}(1,1,-i),\qquad \Phi_L=D\Phi_E
```

gives Lorentz-Minkowski complex-null data. Their real integral is a **spacelike maximal** surface only where the Lorentzian induced metric is positive. In the canonical example,

```math
I_E=\cosh^2(ru)|d\zeta|^2,\qquad I_L=\sinh^2(ru)|d\zeta|^2,\qquad I_L/I_E=W^2.
```

The Lorentz metric degenerates at $`u=0`$. The ambient metric has signature $`(+,+,-)`$, but the regular spacelike induced metric is positive definite. Timelike zero-mean-curvature surfaces require different real-null/para-complex methods.

The scalar imaginary shift

```math
u\mapsto u+i\pi/(2r),\qquad \tanh(ru+i\pi/2)=\coth(ru),\qquad\mathrm{sech}(ru+i\pi/2)=-i\,\mathrm{csch}(ru)
```

is a valid meromorphic continuation but is **not itself** Calabi's real graph correspondence or a universal operation on immersed surfaces. The latter is a closed rotated-gradient map of minimal graphs to spacelike maximal graphs with its own topological domain restrictions.

## 15. Riemann minimal examples: the global-period and Gauss-Manin branch [H466–H469]

The old ZIP includes a marked family, not merely the name “Riemann minimal surfaces”. Retain its elliptic curve and Weierstrass forms:

```math
\mathcal E_\lambda:\quad w^2=g(g-\lambda)(\lambda g+1),\qquad dh=A\,dg/w,\qquad \lambda>0,\quad A>0.
```

```math
\Phi_1=\frac A2(g^{-1}-g)\frac{dg}{w},\qquad\Phi_2=\frac{iA}2(g^{-1}+g)\frac{dg}{w},\qquad\Phi_3=A\frac{dg}{w}.
```

The exact differential identity (archived H466) is

```math
d(w/g)=\frac\lambda2(g+g^{-1})\frac{dg}{w},\qquad\Phi_2=\frac{iA}{\lambda}d(w/g).
```

The nontrivial height and flux periods depend on cycles of the elliptic curve. With the archived parameter $`k=\lambda^{-1}-\lambda`$, the holomorphic period satisfies the Picard-Fuchs ODE

```math
(k^2+4)\Omega_{kk}+2k\Omega_k+\frac14\Omega=0.
```

This ODE differentiates with respect to **moduli parameter $`k`$**, not the original $`u`$ of the Master equation, and its Gauss-Manin monodromy is a different linear representation from tangent-frame holonomy.

Under the Lorentz null-data transformation, the vertical period condition changes from a real to an imaginary component. In general, $`\mathrm{Re}\oint\Phi_3=0`$ does **not** imply $`\mathrm{Im}\oint\Phi_3=0`$. Singularity loci $`|g|=1`$ and the global closing problem remain unresolved for arbitrary transformed Riemann examples. See SF-DRAFT-020.

## 16. A precisely qualified outer-layer example: Brownian generator [D]

A metric gives $`\Delta_I`$ but does not uniquely prescribe a stochastic model. If one **chooses** Brownian motion, its generator is $`\frac12\Delta_I`$. In the present surface coordinates,

```math
\frac12\Delta_I=\frac{1}{2R^2}(\partial_u^2+\partial_v^2).
```

A naive orthonormal-frame Stratonovich equation with zero drift is not generally Brownian. Indeed,

```math
e_1^2+e_2^2=R^{-2}(\partial_u^2+\partial_v^2)-\frac{h_u}{R^2}\partial_u.
```

The Levi-Civita frame drift is

```math
\nabla^{LC}_{e_1}e_1+\nabla^{LC}_{e_2}e_2=-\frac{h_u}{R^2}\partial_u.
```

Hence the corrected Stratonovich equation (with independent Wiener motions) is

```math
dX_t=\frac{h_u}{2R^2}\partial_u\,dt+e_1\circ dB_t^1+e_2\circ dB_t^2.
```

Its generator is exactly $`\frac12\Delta_I`$. Equivalently, on this chart the Itô coordinate system is

```math
du_t=R(u_t)^{-1}dB_t^1,\qquad dv_t=R(u_t)^{-1}dB_t^2.
```

This requires normal global stochastic/domain hypotheses to be treated as a global process. The stochastic derivative is first order in time; the **generator** is a second-order differential operator.

### A genuine stochastic Riccati calculation

Let $`\Psi_t=(X_t,Y_t)^T`$ solve a specified linear Itô equation

```math
d\Psi_t=A\Psi_t\,dt+B\Psi_t\,dB_t,\qquad A=(a_{ij}),\quad B=(b_{ij}).
```

Before $`Y_t`$ reaches zero define $`w_t=X_t/Y_t`$. Put

```math
F(w)=a_{12}+(a_{11}-a_{22})w-a_{21}w^2,\qquad G(w)=b_{12}+(b_{11}-b_{22})w-b_{21}w^2.
```

Itô's formula for $`X/Y`$, including the mixed derivative $`-Y^{-2}`$ and second $`Y`$ derivative $`2X/Y^3`$, gives

```math
dw_t=[F(w_t)-(b_{21}w_t+b_{22})G(w_t)]dt+G(w_t)\,dB_t.
```

The quadratic-variation correction is absent in the deterministic Riccati equation. This is a typed outer-layer construction, not evidence that an arbitrary nonlinear stochastic system is automatically linearly projectivizable.

For a general Itô diffusion $`dX^i=b^i dt+\sigma^i_a dB^a`$ and coordinate map $`F^\alpha(X)`$, the Jacobian and second derivatives appear explicitly:

```math
dF^\alpha(X)=\left[\partial_iF^\alpha b^i+\frac12a^{ij}\partial_i\partial_jF^\alpha\right]dt+\partial_iF^\alpha\sigma^i_a\,dB^a,\qquad a^{ij}=\sum_a\sigma^i_a\sigma^j_a.
```

This is the precise analytic link between Jacobian, Hessian and stochastic generator, after supplying noise and Itô convention.

## 17. Source-audit corrections and negative controls

The attached text is valuable for suggesting the architecture. The following statements must be corrected before they enter a foundational reference.

| Suggestion | Mathematically defensible formulation |
|---|---|
| All second-order equations are the shadow of a single engine. | A research organization and many exact typed examples; **not** a universal classification or solvability theorem. |
| Weitzenböck flatness is the flatness of Gauss-Codazzi. | The former is on a chosen tangent frame, the latter on a full ambient adapted-frame connection; their bundles and torsion differ. |
| Torsion alone gives a force $`T^k{}_{ij}\dot x^i\dot x^j`$. | This expression is zero; the difference of geodesic and teleparallel covariant accelerations uses **contorsion**. |
| $`\ln\cosh(ru)`$ is the catenoid Kähler potential. | It is a potential for the **spherical Gauss-map metric**, not the catenoid metric in the stated chart. |
| Schwarzian of Gauss map determines Hopf $`II`$. | Requires independent height differential; scaling $`\omega`$ fixes the Schwarzian and changes $`II`$. |
| Riccati $`W`$ is a Möbius transform of $`e^{ru}`$. | $`\tanh(ru/2)`$ is Möbius of $`e^{ru}`$; $`W=\tanh(ru)`$ is Möbius of $`e^{2ru}`$. |
| Any zero-mean-curvature immersion globally minimizes area. | It is stationary; stability/global minimization are separate. |
| Catenoid area equation is its geodesic Routhian. | Different functionals; the area profile uses a Beltrami integral, geodesics have a Routhian. |
| Weitzenböck formula uses the Weitzenböck flat connection. | The Hodge/Bochner-Weitzenböck identity uses Levi-Civita curvature and rough Laplacian. |
| A driftless orthonormal-frame Stratonovich SDE always gives Brownian motion. | An appropriate Levi-Civita frame correction is generally needed. |
| All Lorentzian maximal surfaces have Lorentzian induced metric. | Standard Kobayashi maximal immersions are **spacelike**, with positive induced metric. |
| A passing claim-ledger check is a universally quantified theorem proof. | Distinguish exact symbolic identity, finite numerical experiment, quoted classical result, and fully proved general statement. |

## 18. Independent verification, references and open problems

### Verification performed [V]

Independent SymPy calculations, using $`r>0`$, verified: catenoid immersion derivatives; the first and second fundamental forms; four nonzero Levi-Civita Christoffel entries; teleparallel metric compatibility, curvature zero and torsion $`T^v{}_{uv}=h_u`$; contorsion; $`K_I=-e_1(t)-t^2`$; second derivatives of the two Kähler potentials; the covariant Hessian/Laplacian of $`h`$; the geodesic Routhian Euler-Lagrange equation; the catenoid area Beltrami identity; and the three distinct Schwarzian invariants of $`e^{ru}`$, $`\tanh(ru/2)`$ and $`\tanh(ru)`$. Derivations above make the checks reproducible without trusting the archived ledger. Riemann maximal period closure and global stochastic classifications were not established.

### Mathematical literature [K]

- Classical Gauss-Weingarten, fundamental theorem of surfaces, Cartan structure equations, Kähler and Hamiltonian geometry: standard theory; explicit conventions from live SF-DRAFT-010.
- D. Calegari, *Minimal surfaces*, lecture notes: https://math.uchicago.edu/~dannyc/courses/minimal_surfaces_2014/minimal_surfaces_notes.pdf .
- O. Kobayashi, *Maximal surfaces in the 3-dimensional Minkowski space L3*, Tokyo J. Math. 6 (1983), 297–309; see references in SF-DRAFT-020.
- E. Calabi, *Examples of Bernstein problems for some nonlinear equations* (1970): the classical real minimal/maximal graph duality.
- G. Mettler et al., *The Schwarzian derivative and the degree of a classical minimal surface*: https://arxiv.org/abs/2301.11700 . Projective invariants of minimal surfaces are studied independently; the Gaussian exponential's Schwarzian alone is not new.
- Teleparallel/contorsion background: https://pmc.ncbi.nlm.nih.gov/articles/PMC5080365/ .
- Bochner-Weitzenböck formula in geometric Hodge theory: https://math.univ-cotedazur.fr/~hoering/hodge2/hodge.pdf .
- Routh reduction and cyclic-coordinate geometry: https://www.aimsciences.org/article/doi/10.3934/jgm.2019002 .

### Proposed incorporation destinations and research tasks

**Layer I:** scalar identities; Wronskian and projectivization; Riccati clock and Schwarzian normalization; definition of Jacobian/gradient/Hessian and the data types they require.

**Layer II:** explicit connection atlas (ambient Maurer-Cartan, intrinsic Levi-Civita, frame-induced Weitzenböck), torsion/curvature, Gauss-Codazzi, Kähler potentials and holonomy, catenoid/helicoid, Riemann elliptic Weierstrass data.

**Layer III after audit:** variational geodesic/Routh and area reductions, Hodge and Jacobi spectral operators, Weierstrass/Calabi correspondences, Picard-Fuchs/monodromy. **Layer IV only after supplying a model:** diffusion, stochastic projectivization, boundary problems, external physics.

**Open questions:**

1. [O] Generalize the explicit torsion/curvature identity to $`h(u,v)`$ and classify its dependence on local $`SO(2)`$ rotations of the parallel frame.
2. [O] Compare teleparallel holonomy and the nontrivial Hopf/Levi-Civita angular holonomy (archived H538), distinguishing connection gauge and global triviality.
3. [O] Determine precisely which projective connections are compatible with prescribed Weierstrass Gauss map, Hopf differential and metric, avoiding a false uniqueness claim from Schwarzian data alone.
4. [O] Audit domains and self-adjoint realizations of the catenoid/helicoid Jacobi operators, including noncompact ends.
5. [O] Reconstruct the Riemann example's marked period conditions in the Lorentzian Kobayashi transform and classify $`|g|=1`$ singularities.
6. [O] Classify frame-covariant stochastic projectivizations and possible invariant measures based on the canonical $`S,W,R`$ profiles, with noise and conventions specified.

**Conclusion:** These objects form a mathematically consistent **web of typed differential-geometric constructions**, not a single equation under many names. The exact curvature-from-torsion identity, the distinction between the three connections, the precise projective clock, and the separate variational/Hodge/stochastic operators make the catenoid a useful foundational test case; each bridge to another theory must still retain its hypotheses, domain and lost information.
