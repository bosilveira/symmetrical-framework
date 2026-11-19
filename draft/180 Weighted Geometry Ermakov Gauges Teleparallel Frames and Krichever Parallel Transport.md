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
