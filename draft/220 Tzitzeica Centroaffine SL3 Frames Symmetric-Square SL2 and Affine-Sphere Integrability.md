---
id: SF-DRAFT-220
title: Tzitzéica Centro-Affine SL(3) Frames, Symmetric-Square SL(2), and Affine-Sphere Integrability
status: provisional
created: 2026-11-19
proposed_layers: [I, II, III]
depends_on: [SF-DRAFT-170, SF-DRAFT-180, SF-DRAFT-190, SF-DRAFT-200, SF-DRAFT-210]
related_claims: [H73, H100, H136, H153, H154, H421, H466, H470]
---

# 220 Tzitzéica Curves and Surfaces: The Centro-Affine SL(3) Lift and Its Intersection with the SL–EP Web

**Status:** Provisional mathematics. [D] derived with proof; [V] independently symbolically checked; [K] classical theorem with hypotheses; [H] prior framework result, unchanged scope; [C] correction or counterexample; [O] open. Tzitzéica, Ţiţeica and Tzitzeica denote the same mathematical name. No forced physical interpretation.

**Question.** Does the Tzitzéica curve invariant τ/d² furnish a rank-three Wronskian/jerk lift of the rank-two SL–EP web? How does the projective Wilczyński cubic extend the Schwarzian? Do affine spheres supply a genuine two-dimensional flat SL(3) integrability system, and can the resulting geometry be compared to the canonical catenoid/helicoid/Riemann minimal-surface bundle without conflation?

**Principal findings.** The curve condition is an exact third-order determinant equation, equivalent in centro-affine arclength to an SL(3,R) first-order companion frame with **constant coefficient of X**. The symmetric-square of any carrier ψ''=Qψ satisfies X'''=4QX'+2Q'X and yields the Tzitzéica invariant Q'/W³ in the unnormalized spinor-square coordinates. Hence the intersection with nonzero-constant Tzitzéica curves is exactly the selected **affine-linear/Airy** potentials; constant, Pöschl–Teller and generic Lamé Q do not automatically qualify. A genuine rank-three Tzitzéica curve with nonzero projective cubic is exhibited on the affine sphere xyz=1. The Tzitzéica **surface** PDE has a separate explicit 2D SL(3) zero-curvature Lax pair; a one-variable reduction produces a cubic elliptic first integral and an exact nodal Riccati degeneration. These are typed bridges, not identifications of all previous Euclidean and spectral geometries.

**Project sources inspected.** Actual November 18 ZIP: sato-grassmannian (H136, Drach and Lamé), fundamental-forms-willmore-hopf (H421–H428), riemann-marked-periods (H466–H470), foundational paper v0.3 (Ramanujan/Chazy/Darboux–Halphen). Live drafts 170–210 were checked, especially draft 210's squared eigenfunction. Independent sources: Bîlă on the determinant equation, Terng on affine-sphere SL3 Lax, Ovsienko–Tabachnikov on projective curves, and Tzitzéica surfaces (citations in §25).

## 1. Four different categories must not be conflated [C]

A **Tzitzéica space curve** X(t) in Euclidean 3-space satisfies an origin-dependent constant ratio of Euclidean torsion to squared osculating-plane distance. Its **centro-affine** reformulation eliminates metric factors and is invariant under unimodular linear transformations fixing the origin.

A **Tzitzéica surface** satisfies the distinct condition Gaussian curvature divided by the fourth power of tangent-plane distance is constant; properly centered affine spheres are classical cases. This is not the condition of Euclidean mean curvature zero.

A **projective plane curve** [X] in RP² remembers a line, not an absolute lift X; its Wilczyński invariant is a cubic differential and differs from the origin-referenced centro-affine torsion/distance constant.

A **moving affine frame** has group SL(3,R), not SO(3). Its volume-preserving frame structure is not by itself the Euclidean orthonormal moving-frame bundle of drafts 180/200.

## 2. Exact Tzitzéica curve equation: third-order Wronskian [D,K,V]

Let X:I→R³ be C³ with X'×X''≠0, and let D(t)=det(X,X',X'')≠0. The signed Euclidean torsion and positive distance to the osculating plane through X are

```math
\tau=\frac{\det(X',X'',X''')}{\|X'\times X''\|^2},\qquad d=\frac{|\det(X,X',X'')|}{\|X'\times X''\|}.
```

The Euclidean factors cancel EXACTLY:

```math
\mathcal T_X:=\frac{\tau}{d^2}=\frac{\det(X',X'',X''')}{\det(X,X',X'')^2}.
```

**Theorem 2.1 [D,V,K].** X is a Tzitzéica curve with fixed nonzero constant α precisely when

```math
\det(X',X'',X''')=\alpha\,\det(X,X',X'')^2,\qquad\alpha\ne0.
```

This is the Wronskian-type third-order equation described by N. Bîlă, Applied Mathematics E-Notes 23 (2023), 300–308. It is one scalar condition for three coordinate functions, not yet a uniquely specified third-order *vector* equation.

### 2.1 The exact transformation law

For any constant A∈GL(3,R) fixing the origin, the numerator scales by det A and the denominator by (det A)²:

```math
\mathcal T_{AX}=\frac{\mathcal T_X}{\det A}.
```

Therefore the numerical invariant is preserved under SL(3,R) and rescales under arbitrary GL(3,R); a general translation of the origin is NOT a symmetry. Under a smooth reparametrization s=s(t), the determinant D scales by (ds/dt)³ and the numerator by (ds/dt)⁶, so the ratio is parameter independent.

### 2.2 The centro-affine clock

On an interval where D≠0, choose the real signed cube-root clock

```math
\frac{ds}{dt}=D(t)^{1/3},\qquad\det(X,X_s,X_{ss})=1.
```

This is **centro-affine arclength**, not Euclidean arclength, not generally u=ln(x/c). The orientation-reversing case is handled by the signed real cube root.

## 3. Exact SL(3,R) companion frame and first-order condition [D,V]

Differentiate det(X,X_s,X_ss)=1 to obtain det(X,X_s,X_sss)=0. Thus for unique α(s),β(s),

```math
X_{sss}=\alpha(s)X+\beta(s)X_s.
```

Taking determinants gives

```math
\alpha(s)=\det(X_s,X_{ss},X_{sss})=\mathcal T_X,\qquad \beta(s)=-\det(X,X_{ss},X_{sss}).
```

**Theorem 3.1 [D,V] (the precise first-order Tzitzéica frame).** The curve condition τ/d²=α₀≠0 is equivalent, after centro-affine arclength normalization, to

```math
X_{sss}=\alpha_0 X+\beta(s)X_s,\qquad \alpha_0\in\mathbb R\setminus\{0\}.
```

Writing F=(X,X_s,X_ss) gives the trace-zero first-order matrix connection

```math
F_s=F A_3,\qquad A_3=\begin{pmatrix}0&0&\alpha_0\\1&0&\beta(s)\\0&1&0\end{pmatrix},\qquad F\in\mathrm{SL}(3,\mathbb R).
```

The free function β shows the Tzitzéica condition is **not a unique scalar second-order equation**. Flatness of A₃ ds on a one-dimensional base is automatic; a 2D Gauss–Codazzi/zero-curvature condition is strictly stronger.

## 4. The projective Wilczyński cubic versus the rank-two Schwarzian [D,K,C]

Every component of the lift satisfies the Laguerre–Forsyth-form third-order scalar ODE

```math
\phi_{sss}-\beta(s)\phi_s-\alpha(s)\phi=0.
```

For an operator D³+pD+q, the classical projective Wilczyński cubic coefficient is, up to a conventional sign, q−p_s/2. In the chosen sign convention set

```math
\mathcal W_3=\alpha-\frac12\beta_s.
```

Under allowable projective reparametrizations it is a cubic differential, not an ordinary scalar Schwarzian of a single affine coordinate. Its vanishing characterizes the local **symmetric-square/conic** reduction.

**Theorem 4.1 [D,K].** The normalized third-order equation is the symmetric square of ψ_ss=Qψ iff

```math
\mathcal W_3=0\quad\Longleftrightarrow\quad\alpha=\frac12\beta_s,\qquad Q=\frac{\beta}{4}.
```

The projected curve then lies on a projective conic (the Veronese image RP¹→RP²). Tzitzéica instead imposes α=constant≠0; generally W₃≠0. The two conditions have a **proper, explicitly testable intersection**.

**Historical caution.** Halphen's classical work on differential/projective invariants is conceptually relevant to Wilczyński and Ovsienko–Tabachnikov. The independently archived **Darboux–Halphen modular system** (H153–H155) is another object; the shared surname does not identify their operators or clocks.

## 5. EXACT Sym²(SL2) lift: the Drach equation in geometric form [D,V,H136]

Let ψ₁,ψ₂ be independent solutions of

```math
\psi_{ss}=Q(s)\psi,\qquad \mathscr W=\psi_1\psi_{2,s}-\psi_{1,s}\psi_2\ne0.
```

Form the quadratic triple

```math
Y=\big(\psi_1^2,\ \psi_1\psi_2,\ \psi_2^2\big)^{\mathsf T}.
```

Direct differentiation gives the **third-order squared-eigenfunction equation**

```math
Y_{sss}=4QY_s+2Q_sY.
```

Its projectivized image lies on the conic Y₁Y₃−Y₂²=0, and the exact 3×3 Wronskian is

```math
\det(Y,Y_s,Y_{ss})=2\mathscr W^3.
```

The derivative Wronskian is

```math
\det(Y_s,Y_{ss},Y_{sss})=4Q_s\mathscr W^3.
```

**Theorem 5.1 [D,V] (Tzitzéica invariant of SL2 quadratic products).**

```math
\frac{\tau_Y}{d_Y^2}=\frac{Q_s}{\mathscr W^3}.
```

After determinant-one normalization X=(2W³)^(-1/3)Y, its equation becomes

```math
X_{sss}=2Q_s X+4Q X_s,\qquad\frac{\tau_X}{d_X^2}=2Q_s.
```

**Corollary 5.2 [D,V].** For a selected fixed SL independent parameter and a nonzero constant Wronskian, the symmetric-square curve is Tzitzéica with NONZERO invariant iff Q_s is a NONZERO constant: Q(s)=as+b, a≠0. Such second-order carriers are affine-linear potential/Airy equations. A generic SL, PT or Lamé carrier has the same rank-three Drach connection but does NOT satisfy this stronger Tzitzéica condition.

**Representation boundary.** The map Sym²:SL(2)→SL(3) has a three-dimensional subgroup image preserving a conic, not all of SL(3). A genuine centro-affine frame with W₃≠0 cannot be identified with this subgroup by the displayed gauge alone.

## 6. Airy: explicit nonzero Tzitzéica curves inside Sym²(SL2) [D,V,K]

Take the selected linear carrier potential

```math
Q(s)=a s+b,\qquad a\ne0.
```

With the real cube root, define

```math
\xi(s)=\frac{as+b}{a^{2/3}},\qquad \psi_1(s)=\mathrm{Ai}(\xi(s)),\quad\psi_2(s)=\mathrm{Bi}(\xi(s)).
```

Airy's equation $\mathrm{Ai}''(\xi)=\xi\mathrm{Ai}(\xi)$, and likewise for Bi, gives $\psi_{ss}=(as+b)\psi$. The classical Airy Wronskian is $W_\xi(\mathrm{Ai},\mathrm{Bi})=1/\pi$, so

```math
\mathscr W_s=\frac{a^{1/3}}{\pi},\qquad \mathscr W_s^3=\frac a{\pi^3}.
```

**Theorem 6.1 [D,V,K] (Airy/Tzitzéica intersection).** The raw symmetric-square curve

```math
Y(s)=\big(\mathrm{Ai}(\xi)^2,\mathrm{Ai}(\xi)\mathrm{Bi}(\xi),\mathrm{Bi}(\xi)^2\big)
```

has the exact nonzero constant centro-affine invariant

```math
\frac{\tau_Y}{d_Y^2}=\frac{a}{\mathscr W_s^3}=\pi^3.
```

After scaling to determinant-one arclength $X=(2\mathscr W_s^3)^{-1/3}Y$, the constant becomes $\tau_X/d_X^2=2a$. The original Airy family of Tzitzéica curves is known (Bîlă, 2023); this is a particularly transparent **Sym²(SL2) derivation** preserving the Wronskian normalization and its exact constant.

The curve lies in the projective conic $Y_1Y_3=Y_2^2$, so its Wilczyński cubic is zero. It is a genuine *intersection* of two distinct geometric conditions, not the typical Tzitzéica curve.

## 7. The exact framework Drach, PT, and Lamé classification [D,V,H136,C]

The project archive already records the squared-eigenfunction/Drach third-order equation for the stationary KdV operator. For

```math
L=-\partial_u^2+V(u),\qquad L\psi=E\psi,\qquad Q(u)=V(u)-E,
```

the SL symmetric square gives

```math
Y_{uuu}=4(V-E)Y_u+2V_uY.
```

In the normalized centro-affine frame its Tzitzéica coefficient is

```math
\alpha_{\mathrm{sym}^2}(u)=2V_u(u).
```

**Theorem 7.1 [D,V,H136] (conditional Tzitzéica criterion for Drach).** The squared-eigenfunction curve associated with any fixed real SL potential $V$ is a Tzitzéica curve with nonzero constant ratio **if and only if $V_u$ is a nonzero constant** in the selected independent coordinate. This is independent of the spectral energy E, because E disappears after differentiation.

### 7.1 Original free carrier

The canonical weighted framework SL expression under the declared unitary $U_cf(u)=xf(ce^u)$ becomes the constant potential operator

```math
U_c\mathcal L_xU_c^{-1}=-\partial_u^2+r^2,\qquad u=\ln(x/c).
```

Thus $V_u=0$, so its symmetric-square curve has **zero** Tzitzéica invariant. In the zero-energy exponential basis $\psi_\pm=e^{\pm ru}$, the symmetric-square curve lies in an **affine plane** (the middle component is constant). It is not a nonzero-torsion Tzitzéica curve. The half-rate WE spinor carrier of the catenoid similarly has constant potential $r^2/4$ and the same vanishing conclusion.

### 7.2 Reflectionless Pöschl–Teller

For the selected one-soliton PT spectral potential

```math
V_{\rm PT}(u)=-2r^2\mathrm{sech}^2(ru),\qquad (V_{\rm PT})_u=4r^3\mathrm{sech}^2(ru)\tanh(ru),
```

the normalized symmetric-square centro-affine coefficient is

```math
\alpha_{\rm PT}(u)=8r^3\mathrm{sech}^2(ru)\tanh(ru).
```

It is odd, vanishes at the framework's symmetry center $u=0$, and is not nonzero constant. For the selected Hessian PT expression $V_H=4r^2-6r^2\mathrm{sech}^2(ru)$ the corresponding coefficient is $24r^3\mathrm{sech}^2(ru)\tanh(ru)$, likewise nonconstant.

### 7.3 One-gap Jacobi Lamé

For the selected shifted one-gap Lamé operator from draft 210,

```math
V_m(u)=2mr^2\mathrm{sn}^2(ru\mid m)-2mr^2,
```

the symmetric-square centro-affine coefficient is

```math
\alpha_m(u)=2(V_m)_u=8mr^3\mathrm{sn}(ru\mid m)\mathrm{cn}(ru\mid m)\mathrm{dn}(ru\mid m).
```

It varies and vanishes at Jacobi turning points. The archived exact Lamé Drach equation is therefore an **SL3 symmetric-square** system, but not a nonzero-constant Tzitzéica curve in the original canonical spatial coordinate.

**Parameter boundary.** The centro-affine parameter s is an independent construction. A nonlinear reparametrization can change the displayed potential and frame; assertions about a *selected symmetric-square construction* must retain the chosen coordinate and its Wronskian gauge. No theorem here says these spectral curves are forbidden from supporting **other**, separately constructed Tzitzéica curves.

## 8. A genuine rank-three Tzitzéica curve NOT of symmetric-square type [D,V]

Consider the explicitly real analytic space curve

```math
Y(s)=\big(e^s,e^{2s},e^{-3s}\big).
```

Its three coordinate exponents are the distinct roots of the depressed cubic

```math
\lambda^3-7\lambda+6=(\lambda-1)(\lambda-2)(\lambda+3).
```

Hence

```math
Y_{sss}=7Y_s-6Y.
```

Direct determinant calculation gives

```math
\det(Y,Y_s,Y_{ss})=20,\qquad\det(Y_s,Y_{ss},Y_{sss})=-120.
```

Its unnormalized Tzitzéica invariant is

```math
\frac{\tau_Y}{d_Y^2}=-\frac3{10}\ne0.
```

Define the centro-affine normalized curve $X=20^{-1/3}Y$, for which

```math
\det(X,X_s,X_{ss})=1,\qquad X_{sss}=7X_s-6X,\qquad \frac{\tau_X}{d_X^2}=-6.
```

**Theorem 8.1 [D,V] (non-conic genuine SL3 example).** This is a Tzitzéica curve with constant nonzero invariant, and it is **not** the symmetric square of a common rank-two SL carrier in the same determinant-one parameter. Indeed its Wilczyński cubic is

```math
\mathcal W_3=\alpha-\beta_s/2=-6\ne0.
```

Equivalently, no homogeneous quadratic equation in $(Y_1,Y_2,Y_3)$ vanishes identically: the six exponential weights $2,3,-2,4,-1,-6$ appearing in a general quadratic form are distinct. Its projective image is not a conic.

This explicit counterexample proves that Tzitzéica's centro-affine SL3 family is **strictly larger** than the Sym²(SL2) squared-eigenfunction subsystem.

## 9. The SAME curve lies on an ACTUAL Tzitzéica affine sphere [D,V,K]

The curve of §8 satisfies

```math
Y_1Y_2Y_3=e^{s+2s-3s}=1.
```

It is therefore a one-parameter orbit on the positive component of the classical proper affine sphere

```math
\mathscr S:\quad xyz=1,\qquad x,y,z>0.
```

Locally write $z=h(x,y)=1/(xy)$, with $x,y>0$. Its Hessian has

```math
h_{xx}=\frac2{x^3y},\quad h_{xy}=\frac1{x^2y^2},\quad h_{yy}=\frac2{xy^3},\quad\det D^2h=\frac3{x^4y^4}.
```

The support-plane numerator is

```math
h-xh_x-yh_y=\frac3{xy}.
```

Consequently the centro-affine surface invariant is exactly

```math
\frac{K_G}{d_{\rm tan}^4}=\frac{\det D^2h}{(h-xh_x-yh_y)^4}=\frac1{27}.
```

**Theorem 9.1 [D,V] (explicit curve-inside-affine-sphere compatibility).** The classic surface $xyz=1$ is a Tzitzéica surface of constant $1/27$ in the displayed origin/scale, and the unnormalized $Y(s)=(e^s,e^{2s},e^{-3s})$ is simultaneously a genuine nonzero-constant Tzitzéica curve on that surface.

The *normalized* curve $X=20^{-1/3}Y$ instead lies on the homothetic surface $xyz=1/20$, with the appropriate rescaled surface invariant $400/27$. Both changes are dictated by the determinant weights; they are not contradictory constants.

### 9.1 This is a genuine affine symmetry reduction, not an analogy

The two-dimensional subgroup

```math
G_{a,b}=\operatorname{diag}(e^a,e^b,e^{-a-b})\in\mathrm{SL}(3,\mathbb R)
```

acts transitively on the positive affine sphere $xyz=1$. Restricting the group parameters to the line $(a,b)=(s,2s)$ yields EXACTLY $Y(s)$. Thus a **two-dimensional affine-sphere geometry** has been reduced to a **one-dimensional group orbit**, and its preserved origin-dependent centro-affine structures are explicit.

The surface $xyz=1$ is strictly locally convex on the positive component (its Euclidean Gaussian curvature is positive). There are no real asymptotic directions there. Consequently this Tzitzéica curve-on-Tzitzéica-surface example is **not** an asymptotic curve on a negative-curvature affine sphere. Different affine-sphere real forms must not be conflated.

## 10. Sym²(SL2) preserves a split quadratic form and loses the spin sign [D,V,K,H210]

The rank-two action of $M\in\mathrm{SL}(2,\mathbb R)$ on homogeneous binary quadratics induces its three-dimensional symmetric-square action. The discriminant of a quadratic polynomial

```math
aX^2+2bXY+cY^2,\qquad \Delta_2=b^2-ac
```

is preserved under this action. The quadratic form $\Delta_2$ has signature $(2,1)$, so

```math
\mathrm{Sym}^2(\mathrm{SL}(2,\mathbb R))=\mathrm{SO}^+(2,1)\subset\mathrm{SL}(3,\mathbb R)
```

as an isomorphism of the **quotient PSL(2,R)** with the identity component of the split orthogonal group; the kernel of the displayed symmetric-square group homomorphism is $\{+I,-I\}$.

**Theorem 10.1 [D,K] (rank-two spin → rank-three projective conic).** The $\mathrm{SL}(2)$ rank-three lift preserves a split-signature discriminant and has projectivized conic image. It is a **proper subgroup** of the full centro-affine $\mathrm{SL}(3)$ frame group, and its central sign is invisible in rank three.

This has an exact relationship to the selected order-two Weierstrass spin class of draft 210: a nontrivial meromorphic spinor pair may acquire a simultaneous $-1$ multiplier along an elliptic period while its **quadratic** Weierstrass forms and symmetric-square frame remain single-valued. Hence the rank-three system does not, by itself, reconstruct the underlying spin structure. A **two-torsion marking** is additional global information.

The same split orthogonal subgroup $\mathrm{SO}(2,1)$ occurs in the classical affine-sphere Tzitzéica integrable geometry as the isotropy subgroup of the symmetric space $\mathrm{SL}(3,\mathbb R)/\mathrm{SO}(2,1)$ (Terng, §3.9). This is an EXACT Lie-group relation. It does **not** imply the generic Tzitzéica 2D Lax connection takes values in $\mathfrak{so}(2,1)$ or is gauge-equivalent to the original $\mathfrak{sl}_2$ carrier.

## 11. Classical cylindrical Tzitzéica curve: forced oscillator and RICCATI [D,K,V]

The earlier mathematical literature contains another very useful exact reduction. Consider the nondegenerate cylindrical curve

```math
X(t)=(\cos t,\sin t,f(t)).
```

Direct determinant calculation gives

```math
D(t)=\det(X,X',X'')=f(t)+f''(t),\qquad \det(X',X'',X''')=f'(t)+f'''(t)=D'(t).
```

The Tzitzéica condition is therefore

```math
\frac{\tau}{d^2}=\frac{D'}{D^2}=\alpha_0\ne0,\qquad D'=\alpha_0D^2.
```

This is a **scalar Riccati equation** (pure quadratic term) for the osculating-plane determinant, solved by

```math
D(t)=-\frac1{\alpha_0t+C_0}
```

on a connected interval avoiding its pole. The remaining coordinate satisfies the **forced second-order harmonic-oscillator equation**

```math
f''(t)+f(t)=-\frac1{\alpha_0t+C_0}.
```

**Theorem 11.1 [D,V,K] (cylindrical Tzitzéica–Riccati–forced SL dictionary).** For the specified cylindrical ansatz and nonzero osculating-plane determinant, the nonlinear third-order curve condition reduces EXACTLY to a first-order Riccati equation for $D=f+f''$, and thence to a forced linear second-order ODE for $f$.

For initial data at $t_0$ the solution is the standard Green-function convolution

```math
f(t)=f(t_0)\cos(t-t_0)+f'(t_0)\sin(t-t_0)-\int_{t_0}^t\frac{\sin(t-s)}{\alpha_0s+C_0}\,ds.
```

This is classical (see M. Crâşmăreanu, Tzitzéica cylindrical curves), not a novel general Riccati theorem. It is a second **exact** illustration of the project's theme: a geometric third-order Wronskian constraint becomes a first-order Riccati equation and a second-order forced SL carrier **after a declared geometric ansatz**.

**No conflation:** $D$ is the osculating-plane determinant, not the positive Ermakov–Pinney amplitude, and this forced oscillator does not automatically contain a Pinney inverse-cubic term or a self-adjoint spectral problem.

## 12. Tzitzéica SURFACES: exact Gaussian-curvature/plane-distance invariant [D,K]

Let a surface in Euclidean 3-space be locally the graph $(x,y,h(x,y))$, with nonvanishing regular tangent-plane distance from the origin. The Gauss curvature and support-plane distance are

```math
K_G=\frac{\det D^2h}{(1+h_x^2+h_y^2)^2},\qquad d_{\rm tan}=\frac{|h-xh_x-yh_y|}{\sqrt{1+h_x^2+h_y^2}}.
```

Hence the centro-affine ratio is

```math
\frac{K_G}{d_{\rm tan}^4}=\frac{\det D^2h}{(h-xh_x-yh_y)^4}.
```

**Theorem 12.1 [D,K] (Monge–Ampère graph characterization).** The nondegenerate graph is a Tzitzéica surface with constant $\kappa_T$ iff it satisfies the exact **Monge–Ampère equation**

```math
h_{xx}h_{yy}-h_{xy}^2=\kappa_T\,(h-xh_x-yh_y)^4.
```

The surface equation is **second-order**, nonlinear in the Hessian determinant. Its first-order affine-frame formulation is a different package that includes a transversal affine normal and integrability equations.

Under a fixed centro-affine map $A\in GL(3,R)$ the surface constant scales with $(\det A)^{-2}$; it is invariant under $SL(3,R)$ transformations fixing the origin. Under a pure dilation $X\mapsto aX$, the ratio scales by $a^{-6}$ (consistent with the graph example in §9).

### 12.1 Distinction from the Euclidean minimal-surface Euler–Lagrange PDE

A Euclidean minimal graph satisfies

```math
\mathrm{div}\left(\frac{\nabla h}{\sqrt{1+|\nabla h|^2}}\right)=0.
```

The Tzitzéica Monge–Ampère equation instead fixes the ratio $K_G/d_{\rm tan}^4$. Their differential operators, invariance groups, variational geometries and real forms are **different**. A surface may be Tzitzéica without being minimal, or minimal without being Tzitzéica.

## 13. A concrete no-go: the CANONICAL CATENOID is not a Tzitzéica surface [D,V,C]

Use the canonical Euclidean catenoid with $r>0$, $u=\ln(x/c)$ and angular variable $\theta=rv$:

```math
X_C(u,\theta)=\left(\frac{\cosh(ru)}r\cos\theta,\frac{\cosh(ru)}r\sin\theta,u\right).
```

Choose its unit normal

```math
N_C=(-\mathrm{sech}(ru)\cos\theta,-\mathrm{sech}(ru)\sin\theta,\tanh(ru)).
```

The origin-to-tangent-plane signed support is

```math
X_C\cdot N_C=-\frac1r+u\tanh(ru),
```

while the Gaussian curvature is

```math
K_C=-r^2\mathrm{sech}^4(ru).
```

Therefore, where the plane distance is nonzero,

```math
\frac{K_C}{d_{\rm tan}^4}=\frac{-r^2\mathrm{sech}^4(ru)}{(u\tanh(ru)-1/r)^4},
```

which is **not constant**. Indeed the support vanishes at a finite positive root $u\tanh(ru)=1/r$, while the curvature stays nonzero. The meridian at fixed $\theta$ is a planar curve with zero Euclidean torsion, so it is not a nonzero-constant Tzitzéica space curve either.

**Corollary 13.1 [D,C].** Even the canonical catenoid—despite its fundamental first-order WE spinor construction and SL–EP/Wronskian dictionary—is not automatically an affine Tzitzéica surface in the displayed center/origin. The analogous conclusion for a general Riemann minimal example or its curve foliation cannot be asserted without calculating its actual centro-affine invariants.

## 14. Affine Gauss–Codazzi and the actual Tzitzéica 2D Lax frame [K,D,V]

A proper **indefinite affine sphere** admits suitable asymptotic coordinates $(a,b)$ and a scalar potential $w(a,b)$ with a Blaschke affine metric proportional to $e^{w}\,da\,db$. In one standard sign/normalization, its structural integrability condition is the **Tzitzéica/Bullough–Dodd equation**

```math
w_{ab}=e^w-e^{-2w}.
```

Here $a,b$ are **surface coordinates** and must not be confused with the canonical logarithmic variable $u$, Riemann elliptic modulus $\lambda_R$, or the Tzitzéica curve constant $\alpha_0$.

For any nonzero independent Lax spectral parameter $\lambda_T$, define matrices

```math
A_T=\begin{pmatrix}w_a&0&\lambda_T\\\lambda_T&-w_a&0\\0&\lambda_T&0\end{pmatrix},\qquad B_T=\begin{pmatrix}0&\lambda_T^{-1}e^{-2w}&0\\0&0&\lambda_T^{-1}e^{w}\\\lambda_T^{-1}e^{w}&0&0\end{pmatrix}.
```

Set $\Omega_T=A_T\,da+B_T\,db\in\mathfrak{sl}_3(\mathbb R)$. Its Maurer–Cartan curvature is

```math
d\Omega_T+\Omega_T\wedge\Omega_T=\begin{pmatrix}-\mathcal E_T&0&0\\0&\mathcal E_T&0\\0&0&0\end{pmatrix}da\wedge db,\qquad \mathcal E_T=w_{ab}-e^w+e^{-2w}.
```

**Theorem 14.1 [D,V,K] (explicit affine-sphere zero curvature).**

```math
d\Omega_T+\Omega_T\wedge\Omega_T=0\quad\Longleftrightarrow\quad w_{ab}=e^w-e^{-2w}.
```

**Proof.** Write $\Omega_T=A_Tda+B_Tdb$ and expand $-A_{T,b}+B_{T,a}+[A_T,B_T]$. Every off-diagonal entry cancels identically and the two nonzero diagonal entries are $\mp\mathcal E_T$. This was independently checked using symbolic 3×3 matrix multiplication.

For simply connected domains the flatness integrates a frame $G(a,b;\lambda_T)\in SL(3,R)$, $G^{-1}dG=\Omega_T$. Under the conventional affine-sphere frame normalization, a designated column of $G$ gives the immersion in $\mathbb R^3$ (see Chuu-Lian Terng, Geometry and Symmetries of Soliton Equations, affine sphere section). This is **affine** geometry using the Blaschke normal and cubic form, not automatically the Euclidean mean-curvature-zero WE immersion.

### 14.1 A real geometric distinction: two equations both called Tzitzéica

The **curve** condition $\tau/d^2=\alpha_0$ is a 1D third-order determinant identity. The **affine-sphere surface** condition is a 2D Monge–Ampère/Gauss–Codazzi system, which under a selected indefinite affine-normal gauge yields the scalar PDE above. There is no general equivalence between an arbitrary solution of the first and an arbitrary solution of the second. They can meet when the curve is a selected asymptotic line or group orbit on a relevant affine sphere, subject to extra restrictions.

## 15. The symmetric space bridge and the twisted integrable algebra [K,D,C]

The Tzitzéica/Bullough–Dodd equation has a classical twisted affine-integrable structure of type $A_2^{(2)}$. The 3×3 Lax matrices are $\mathfrak{sl}_3$-valued and include the spectral parameter $\lambda_T$ and its inverse. Terng's affine-sphere formulation also identifies a related harmonic-map/symmetric-space structure with real symmetric-space quotient

```math
\mathrm{SL}(3,\mathbb R)/\mathrm{SO}(2,1).
```

Recall §10: the symmetric-square of real rank-two SL2 is the subgroup $\mathrm{SO}^+(2,1)$ (up to the central ±I quotient). Thus the same split orthogonal group is both the image of the framework's **Sym² real projective representation** and an **isotropy subgroup** in the affine-sphere geometric setting.

**Theorem 15.1 [D,K] (exact group-level intersection).** The rank-two projective SL–Riccati carrier admits a precise lift into the split-orthogonal subgroup of $\mathrm{SL}(3)$, while Tzitzéica's full affine-sphere connection takes values in the ambient $\mathfrak{sl}_3$. The shared subgroup is exact group theory, but **a reduction of the full 2D Lax pair to the SO(2,1) subgroup is an additional strong condition**, not a consequence of sharing the quotient notation.

This is a particularly promising structural explanation for why two- and three-component linear problems can coexist in the framework. It neither identifies $\mathrm{SU}(2)$ with $\mathrm{SO}(2,1)$ (different real forms) nor implies a four-dimensional Yang–Mills instanton.

## 16. The 1D reduction of the 2D affine-sphere PDE [D,V]

Assume the **declared traveling/diagonal reduction**

```math
w(a,b)=h(s),\qquad s=a+b.
```

The affine-sphere compatibility equation becomes a one-variable nonlinear ODE

```math
h_{ss}=e^h-e^{-2h}.
```

Multiplying by $2h_s$ and integrating gives the exact conserved first integral

```math
(h_s)^2=2e^h+e^{-2h}+\varepsilon_T,
```

where $\varepsilon_T$ is an arbitrary real integration constant, NOT the framework's energy $\varepsilon_N$, elliptic modulus $m$ or multiplicative center $c$.

Put $v=e^h>0$; then

```math
v_s^2=2v^3+\varepsilon_Tv^2+1.
```

**Theorem 16.1 [D,V] (exact elliptic reduction).** The one-dimensional reduction of the two-dimensional Tzitzéica affine-sphere equation carries the algebraic cubic curve

```math
\mathcal E_T:\quad y^2=2v^3+\varepsilon_Tv^2+1,
```

with the physical real solutions restricted to its portions with $v>0$. It is generically a smooth genus-one curve over $\mathbb C$ and degenerates at its algebraic discriminant zeros. This elliptic spectral-energy mechanism is analogous in **type** to the framework's cubic Master/Duffing reductions, but the cubic polynomials and geometric normalizations are not automatically equal.

### 16.1 Exact Weierstrass invariants and the j-function

Set $X=v+\varepsilon_T/6$ and $Y=\sqrt2\,v_s$. The cubic takes Weierstrass form

```math
Y^2=4X^3-g_2X-g_3,\qquad g_2=\frac{\varepsilon_T^2}{3},\quad g_3=-\frac{\varepsilon_T^3}{27}-2.
```

Its discriminant and modular invariant are

```math
\Delta_T=g_2^3-27g_3^2=-4(\varepsilon_T^3+27),\qquad j_T=-\frac{16\varepsilon_T^6}{\varepsilon_T^3+27}.
```

The **nodal limit** occurs at $\varepsilon_T=-3$, where

```math
2v^3-3v^2+1=(v-1)^2(2v+1).
```

At $\varepsilon_T=0$ the smooth cubic is equianharmonic ($j=0$), and at the special real energy $\varepsilon_T=-\sqrt[3]{54}$ it is lemniscatic ($g_3=0$, $j=1728$). This matches the abstract **complex elliptic j** of the selected symmetric one-gap Lamé/Riemann fiber $m=1/2$ (drafts 170/210), but does **not** fix a real-marked differential, spin class or spectral operator map.

The exact relation

```math
j_T-1728=-\frac{16(\varepsilon_T^3+54)^2}{\varepsilon_T^3+27}
```

shows that for $\varepsilon_T<-3$ (three distinct real branch roots) one has $j_T\ge1728$, with equality precisely at $\varepsilon_T=-\sqrt[3]{54}$. This provides a genuine **modular comparison locus**, not evidence of a universal elliptic-curve identification.

## 17. Nodal Tzitzéica reduction becomes the SAME TYPE of Riccati flow [D,V,H,C]

On the nodal energy $\varepsilon_T=-3$, the positive coordinate $v=e^h$ obeys

```math
v_s^2=(v-1)^2(2v+1).
```

On a monotone nonconstant branch let $Z=\sqrt{2v+1}>1$. Since $Z Z_s=v_s$, one has

```math
Z_s=\pm\frac{Z^2-3}{2}.
```

Equivalently, with $W_T=Z/\sqrt3$,

```math
(W_T)_s=\pm\frac{\sqrt3}{2}(W_T^2-1).
```

**Theorem 17.1 [D,V] (exact nodal Riccati mechanism).** A one-dimensional reduction of the affine-sphere Tzitzéica PDE has an exact **Riccati** degeneration at its nodal elliptic cubic, after the explicit positive square-root substitution. With an orientation reversal its right-hand side has the canonical logistic/hyperbolic form $\omega(1-W_T^2)$ at rate $\omega=\sqrt3/2$.

This is the **same algebraic Riccati normal form** encountered in the canonical framework's $rW$ equation and in nodal Lamé/catenoid limits, but the coordinate $s$, energy $\varepsilon_T$, half-period markings, and actual surface immersion are different. Equality of Riccati normal forms after declared substitutions is **not** equality of all their original ODE/PDE solution spaces.

The equilibrium $h=0$ corresponds to the double root $v=1$, $Z=\sqrt3$. Real branches with $v>0$ may be restricted intervals; no global periodicity or completeness is asserted from the nodal algebra alone.

## 18. Explicit real j=1728 isomorphism to the SYMMETRIC Riemann elliptic curve [D,V,H170]

The modular coincidence at $\varepsilon_T=-\sqrt[3]{54}$ from §16 can be made into an actual algebraic isomorphism, provided we declare exactly which **curves** and **differentials** are compared.

At this value,

```math
g_{3,T}=0,\quad g_{2,T}=\frac{\varepsilon_T^2}{3}>0,\qquad \mathcal E_T:\quad Y_T^2=4X_T^3-g_{2,T}X_T.
```

The framework's matched symmetric Riemann elliptic curve at $\lambda_R=1$, equivalently $m=1/2$ (drafts 170/210), is

```math
E_R:\quad Y_R^2=4X_R^3-4X_R,\qquad X_R=g_R,\quad Y_R=2y_R.
```

Define the positive constant $\sigma$ by

```math
\sigma^4=\frac{g_{2,T}}4=\frac{\varepsilon_T^2}{12},\qquad \sigma>0.
```

**Theorem 18.1 [D,V] (selected real unmarked elliptic isomorphism).** The explicit real algebraic map

```math
X_T=\sigma^2X_R,\qquad Y_T=\sigma^3Y_R
```

is an isomorphism between the two **smooth real elliptic curves**, with a holomorphic-differential scale

```math
\frac{dX_T}{Y_T}=\sigma^{-1}\frac{dX_R}{Y_R}.
```

Since $X_T=v+\varepsilon_T/6$, this also gives an explicit affine relation $v=\sigma^2g_R-\varepsilon_T/6$ between the Tzitzéica reduction's *cubic coordinate* and the Riemann elliptic Gauss coordinate at this one marked modulus.

**Strict boundary [C].** The real Tzitzéica physical branch has $v=e^h>0$, the Riemann elliptic curve has a WE height differential and spin bundle, and the original Lamé operator uses an independent spatial coordinate $u=\ln(x/c)$. The displayed curve isomorphism does **not** identify their differential equations, periodic solution intervals, BA eigenline, spin connection, real immersion periods or self-adjoint domains. It is an exact, *explicitly selected* curve-and-differential isomorphism, no stronger.

## 19. Projectivizing the third-order scalar companion gives a coupled RICCATI system [D,V]

The scalar ODE

```math
\psi_{sss}=\beta(s)\psi_s+\alpha(s)\psi
```

has first-order vector state $(\psi,\psi_s,\psi_{ss})^{\mathsf T}$ satisfying

```math
\frac d{ds}\begin{pmatrix}\psi\\\psi_s\\\psi_{ss}\end{pmatrix}=\begin{pmatrix}0&1&0\\0&0&1\\\alpha&\beta&0\end{pmatrix}\begin{pmatrix}\psi\\\psi_s\\\psi_{ss}\end{pmatrix}.
```

On a chart where $\psi\ne0$ define two projective coordinates

```math
p=\frac{\psi_s}{\psi},\qquad q=\frac{\psi_{ss}}{\psi}.
```

Their induced projective dynamics is the explicit first-order **coupled Riccati system**

```math
p_s=q-p^2,\qquad q_s=\alpha+\beta p-pq.
```

Eliminating $q=p_s+p^2$ yields the second-order nonlinear *projective jerk* equation

```math
p_{ss}+3pp_s+p^3-\beta p-\alpha=0.
```

**Theorem 19.1 [D,V] (RP² Riccati/projective reduction).** The third-order linear centro-affine carrier and the coupled first-order projective Riccati system on a chart of $\mathbb{RP}^2$ are locally equivalent away from zeros of $\psi$. The one-dimensional scalar projective coordinate $p$ obeys the displayed second-order nonlinear equation.

This is the exact higher-rank counterpart of the framework's $\mathrm{SL}(2)$ ratio Riccati equation $h_s=Q-h^2$. A projective plane requires **two** affine chart coordinates; its geometry is not exhausted by one Schwarzian of a ratio.

### 19.1 The pure-square rank-two Riccati submanifold

For the special symmetric-square solution $\psi=\varphi^2$ with $\varphi_{ss}=Q\varphi$, let $h=\varphi_s/\varphi$. Then

```math
p=2h,\qquad q=2(Q+h^2)=2Q+\frac12p^2,\qquad p_s=2Q-\frac12p^2.
```

The coupled $\mathbb{RP}^2$ Riccati flow restricts to the declared rank-two pure-square relationship. This is a representation-theoretic **subsystem**: a generic third-order solution is an arbitrary linear combination of the three squared products, not itself the square of one carrier solution.

## 20. Holonomy, Wronskians, spin signs, and global descent [D,K,C]

On a one-dimensional interval a chosen initial centro-affine frame and companion coefficient reconstruct a unique curve:

```math
F(s)=F(s_0)\,\mathcal P\exp\left(\int_{s_0}^s A_3(t)\,dt\right),\qquad X(s)=F(s)e_1.
```

If $\beta(s)$ is periodic of period $L$ and $\alpha$ constant, the transport matrix is a monodromy $M_3\in SL(3,R)$ after choosing a frame convention. An actual *closed framed curve* requires the appropriate global frame periodicity (for a fully periodic normalized frame, $M_3=I$); a weaker projective closure of $[X]$ does not impose Euclidean/affine position closure.

For a carrier rank-two monodromy $M_2\in SL(2,R)$, its symmetric-square monodromy is

```math
M_3=\mathrm{Sym}^2(M_2)\in\mathrm{SO}^+(2,1).
```

The kernel is the central sign:

```math
\mathrm{Sym}^2(-M_2)=\mathrm{Sym}^2(M_2).
```

**Theorem 20.1 [D,K] (global spin information is NOT recoverable from Sym² alone).** The symmetric-square rank-three transport retains the rank-two projective monodromy but cannot distinguish the two spin lifts $M_2$ and $-M_2$. This is the same mathematical loss of a $\mathbb Z_2$ marking that appears in the framework's Riemann WE 2-torsion spin line (draft 210). Recovering the original spinor bundle requires a **chosen lift or theta-characteristic marking**.

An arbitrary centro-affine $\mathrm{SL}(3)$ monodromy need not lie in the symmetric-square subgroup and need not admit such an $\mathrm{SL}(2)$ lift. Thus even retaining the complete rank-three first-order connection does not yield a *universal* canonical WE spin bundle without additional structure.

## 21. Curvature, affine cubic forms, and binary quartics: TYPE CHECK [D,H,C]

The framework already contains at least four independent invariant constructions:

1. **Binary quadratic discriminant** $\Delta_2=b^2-ac$, preserved by the real symmetric-square $\mathrm{SL}(2)$ action on three-dimensional quadratic-form space. Its signature $(2,1)$ determines the embedded split orthogonal subgroup.
2. **Wilczyński cubic coefficient** $\mathcal W_3=\alpha-\beta_s/2$ of a projective $\mathbb{RP}^2$ curve. Its vanishing characterizes the conic/symmetric-square reduction. It is a *differential invariant*, not the discriminant of a binary cubic or a modular form by definition.
3. **Affine-sphere Fubini–Pick cubic form**, an intrinsically two-dimensional tensor on an affine sphere, entering its affine Gauss–Codazzi equations and $\mathfrak{sl}_3$ Lax representation. It is not the space-curve torsion, although selected asymptotic curves may link the structures.
4. **Framework binary quartic invariants** $(I,J,\Delta)$ and pointwise fundamental-form product quartics (H421). They are algebraic invariants of a declared binary *degree-four* form. They do not canonically equal the projective Wilczyński cubic, the affine Fubini–Pick form or the quadratic discriminant.

The **elliptic j-invariant** of the reduced Tzitzéica cubic in §16 is a fifth object: it is constructed from a particular *first integral*, and its special $1728$ locus supplies a selected elliptic curve isomorphism (§18). Conflating these typed invariants would defeat the goal of understanding the origin of the equations.

**Potential future map [O].** One can seek a *marked algebraic functor* from the affine-sphere cubic-form/flat-Lax data to a selected spectral elliptic curve or to the framework's binary-quartic pencil, but a common degree or modular value alone is not enough. Periods, discriminants, spin structures and real forms must be transported explicitly.

## 22. Gauss–Codazzi in two geometries, and what fibration reconstruction actually preserves [D,K,C]

The **Euclidean minimal-surface** mechanism of drafts 180/200 uses a metric $I$, second form $II$, a unit Euclidean normal, zero mean curvature and an adapted **flat Euclidean-motion Cartan connection** with structure group $\mathrm{SE}(3)$ (spin cover $\mathrm{SU}(2)\ltimes\mathbb R^3$). Its WE spinor forms are holomorphic, and global immersion periods are real translations.

The **Tzitzéica affine-sphere** mechanism uses a Blaschke affine metric, affine normal, Fubini–Pick cubic and an **$\mathrm{SL}(3,R)$ affine frame**. Its Gauss–Codazzi compatibility is the Tzitzéica equation in the selected indefinite affine normalization. Their connections and variational functionals are different despite a common three-dimensional ambient set.

The two mechanisms admit **exact 1D reductions**, but those reductions preserve only declared data:

- Sym²(SL2)→SL3 preserves a Wronskian-derived volume determinant and a quadratic discriminant, while losing the central spin sign.
- A centro-affine Tzitzéica curve preserves $\alpha=\tau/d^2$ under its SL3 frame action but still needs initial frame and monodromy data to reconstruct a closed curve.
- Restricting the 2D diagonal group orbit on $xyz=1$ to a 1D subgroup gives an actual algebraically explicit curve-on-surface reduction.
- A Tzitzéica PDE one-variable reduction preserves its declared elliptic first integral; its nodal limit is Riccati, but a separate map is needed to compare it to the canonical framework's SL/EP clock, weighted norm, WE spin line or Gauss–Manin periods.

This is a useful higher-rank **test case** for the proposed fibration-holography program: one has an exact connection-aware reconstruction *inside a specified geometric category*, not a theorem that every 1D carrier uniquely remembers every 3D immersion.
