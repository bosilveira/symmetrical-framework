---
id: SF-DRAFT-010
title: Gauss-Codazzi Equations and Canonical Surface Geometry
status: provisional
created: 2026-11-18
proposed_layers: [I, II]
depends_on: [SF-I-000, SF-I-010, SF-I-020]
related_claims: [H421, H424, H473, H474, H490, H509, H538]
---

# 010 Gauss-Codazzi Equations and Canonical Surface Geometry

**Status:** Complete provisional mathematical investigation; **not** a canonical theorem chapter and **not** a claim of novelty. Statements require individual audit before migration to the foundational reference.

**Objective:** Derive the precise relationships among the canonical $S,W,R$ fields, Gauss-Codazzi compatibility, fundamental forms, Levi-Civita connections, Maurer-Cartan equations, Darboux data, minimal surfaces in space forms, Kähler geometry, the Hopf bundle, and binary quartics. Particular emphasis is placed on a converse: **under which explicitly stated ansatz can Gauss-Codazzi itself recover the cubic Master energy equation?**

**Sources:** Live GitHub chapters **SF-I-000**, **SF-I-010**, **SF-I-020**; uploaded historical ZIP **symmetrical-framework-update-2026-11-18-bu.zip**, particularly its **00-meta/CLAIMS.md** and **04-follow-ups/fundamental-forms-willmore-hopf.md**, **04-follow-ups/riemann-marked-periods-gauss-manin-x04.md**; accompanying discussions on geometric layers, moving frames, Schwarzian reconstruction, Kähler potential, and Sturm-Liouville theory. The old ZIP contains a different repository layout from the live main branch. Refer to historical claims **H421**, **H424**, **H473**, **H474**, **H490**, **H509**, **H538**, especially the sign and global-holonomy corrections.

**Evidence conventions:** **[K]** classical literature result; **[D]** derived step by step here; **[V]** independently checked by exact symbolic substitution; **[O]** unresolved or conditional. "Derived here" does not assert historical novelty.

## 1. Canonical definitions and mathematical boundaries

Assume

```math
x>0,\qquad c>0,\qquad r>0,\qquad \mu>0,\qquad u=\ln(x/c),\qquad \theta=ru.
```

The original function, amplitude, and centered scalar fields are

```math
f_\mu(x;r,c)=\frac{c^r x^{r-1}}{\sqrt{\mu}(c^{2r}+x^{2r})},\qquad y(u)=2xf_\mu(x;r,c),\qquad S=\mathrm{sech}(ru),\quad W=\tanh(ru),\quad R=\cosh(ru).
```

The centered separatrix has $y=\mu^{-1/2}S$. Its differential algebra is

```math
S_u=-rSW,\qquad W_u=rS^2,\qquad R_u=rRW,\qquad S^2+W^2=1,\qquad SR=1.
```

Let $\kappa=\ln R$. Then

```math
\kappa_u=rW,\qquad \kappa_{uu}=r^2S^2=r^2e^{-2\kappa},\qquad \kappa_u^2+r^2e^{-2\kappa}=r^2.
```

The *new* real coordinate $v$ and complex coordinate $\zeta=u+iv$ are **additional geometric data**, not extra variables of the original function. For the canonical angular cylinder, impose $v\sim v+2\pi/r$. Local surface theory initially works on any simply connected coordinate domain without imposing that identification.

Use $H_m$ for mean curvature, $K_I$ for intrinsic Gaussian curvature, $B$ for the shape operator, $Q_H$ for the coefficient of the Hopf quadratic differential, and $k_0$ for ambient sectional curvature. Distinguish $k_0$ from the scalar generating function $\kappa$ and from the nonlinear Master energy.

**Fundamental methodological distinction:** An identity of scalar functions is not by itself a unique metric, immersion, symplectic form, stochastic process, or physical model. The exact geometric ansatz will be supplied and checked below.

## 2. Classical Gauss-Weingarten, Gauss-Codazzi, and the reconstruction theorem [K]

Let an oriented surface $X:U\to M^3(k_0)$ be immersed into a three-dimensional space form of constant sectional curvature $k_0$. Choose a unit normal $N$ and coordinates $(t^1,t^2)$. Define

```math
I=g_{ij}\,dt^i dt^j,\qquad g_{ij}=\langle X_i,X_j\rangle,\qquad II=b_{ij}\,dt^i dt^j,\qquad b_{ij}=\langle\nabla^{\mathrm{amb}}_{X_i}X_j,N\rangle.
```

With $\nabla_X^{\mathrm{amb}}N=-BX$ and $B^i{}_j=g^{ik}b_{kj}$, the Gauss and Codazzi equations are

```math
K_I=k_0+\det B,\qquad (\nabla_i b)_{jk}=(\nabla_j b)_{ik}.
```

In Euclidean space $k_0=0$; in a curved ambient space the extra $k_0$ must remain. The Weingarten and Gauss formulas in Euclidean coordinates are

```math
\partial_iX_j=\Gamma^k_{ij}X_k+b_{ij}N,\qquad \partial_iN=-b_i{}^kX_k.
```

**Theorem 2.1 [K] (fundamental theorem of surface theory).** Positive-definite sufficiently regular $I$ and symmetric $II$ on a simply connected domain, satisfying the Gauss-Codazzi equations for a selected space form, determine a local immersion into that space form, uniquely up to ambient isometry with the orientation conventions fixed.

**Reason.** Compatibility of the mixed derivatives of the Gauss-Weingarten system is exactly Gauss-Codazzi. Conversely, this compatibility allows the frame equations to be solved and the coframe integrated. The result is *local*. Completeness, an embedding rather than an immersion, and closure of the immersion on a multiply connected quotient require separate arguments.

In higher codimension the normal connection and the **Ricci equation** enter as additional compatibility data; the surface equations used here must not be asserted as a complete arbitrary-codimension theory.

## 3. Conformal Gauss-Codazzi and its exact normalization [D]

Let

```math
I=e^{2\omega}(du^2+dv^2),\qquad II=L\,du^2+2M\,du\,dv+N_2\,dv^2.
```

Here $N_2$ names a coefficient, not the normal vector. Define

```math
H_m=\frac{L+N_2}{2e^{2\omega}},\qquad Q_H=\frac{L-N_2-2iM}{4},\qquad \partial_\zeta=\frac12(\partial_u-i\partial_v).
```

Then

```math
II=H_me^{2\omega}|d\zeta|^2+2\mathrm{Re}(Q_H\,d\zeta^2),\qquad \det B=H_m^2-4|Q_H|^2e^{-4\omega}.
```

The conformal metric has curvature

```math
K_I=-e^{-2\omega}\Delta_0\omega,\qquad \Delta_0=\partial_u^2+\partial_v^2.
```

**Proposition 3.1 [D].** In these conventions, Gauss-Codazzi is

```math
\Delta_0\omega+(k_0+H_m^2)e^{2\omega}-4|Q_H|^2e^{-2\omega}=0.
```

```math
\partial_{\bar\zeta}Q_H=\frac12e^{2\omega}\partial_\zeta H_m.
```

**Proof, step by step.**

1. The inverse metric is $e^{-2\omega}$ times the identity. Taking the trace and determinant of $B=e^{-2\omega}\begin{psmallmatrix}L&M\\M&N_2\end{psmallmatrix}$ gives the displayed expressions for $H_m$ and $\det B$.
2. Substitute the determinant into $-e^{-2\omega}\Delta_0\omega=k_0+\det B$ and multiply by $e^{2\omega}$.
3. The real Codazzi equations read $L_v-M_u=\omega_v(L+N_2)$ and $N_{2,u}-M_v=\omega_u(L+N_2)$.
4. Substitute $L=H_me^{2\omega}+2\mathrm{Re}\,Q_H$, $N_2=H_me^{2\omega}-2\mathrm{Re}\,Q_H$, and $M=-2\mathrm{Im}\,Q_H$. The two real relations combine into the second displayed complex equation.

For a *minimal* immersion $H_m=0$, Codazzi says $\partial_{\bar\zeta}Q_H=0$, i.e. the Hopf quadratic differential is holomorphic. **Constant Hopf coefficient** is an additional particular choice, not a property of every minimal surface.

## 4. The canonical scalar equation is the Euclidean Gauss equation [D]

Choose the following surface data from the canonical fields:

```math
I_C=R^2(du^2+dv^2)=e^{2\kappa}|d\zeta|^2,\qquad II_C=-r(du^2-dv^2),\qquad Q_H=-r/2,\qquad H_m=0.
```

Codazzi holds because $Q_H$ is constant. The Euclidean Gauss equation becomes

```math
\Delta_0\kappa=4|Q_H|^2e^{-2\kappa}=r^2e^{-2\kappa}.
```

But this is precisely $\kappa_{uu}=r^2S^2$, since $\kappa$ depends only on $u$ and $e^{-\kappa}=S$. Therefore the compatible intrinsic and extrinsic curvatures are

```math
K_C=-r^2S^4,\qquad k_1=-rS^2,\qquad k_2=+rS^2,\qquad H_m=0.
```

**Conclusion [D].** The scalar Riccati system, *together with a specified conformal metric and constant Hopf differential*, reconstructs a Euclidean minimal-surface Gauss-Codazzi system. The ansatz is part of the mathematical claim.

## 5. Verify the explicit catenoid immersion [D,V]

Put $\phi=rv$ and define

```math
X_C(u,v)=\left(\frac{R}{r}\cos\phi,\frac{R}{r}\sin\phi,u\right).
```

Its derivatives and oriented unit normal are

```math
X_u=(\sinh(ru)\cos\phi,\sinh(ru)\sin\phi,1),\qquad X_v=(-R\sin\phi,R\cos\phi,0),\qquad N=(-S\cos\phi,-S\sin\phi,W).
```

Step 1. Direct scalar products give the coefficients of the first fundamental form:

```math
E=\langle X_u,X_u\rangle=R^2,\qquad F=\langle X_u,X_v\rangle=0,\qquad G=\langle X_v,X_v\rangle=R^2.
```

Step 2. Differentiate again and take normal components:

```math
L=\langle X_{uu},N\rangle=-r,\qquad M=\langle X_{uv},N\rangle=0,\qquad N_2=\langle X_{vv},N\rangle=+r.
```

Step 3. Consequently, $I=I_C$, $II=II_C$, the mean curvature vanishes, and the Gaussian curvature is $-r^2S^4$ as required by Gauss.

This proves the immersion claim independently of the abstract existence theorem. For $u\in\mathbb R$ and $v$ mod $2\pi/r$, the map describes the complete embedded catenoid of neck radius $1/r$. The logarithmic center $x=c$ maps to its neck $u=0$. This is an **explicit chosen geometric realization**, not a canonical embedding of the original multiplicative line.

## 6. Maurer-Cartan flatness reconstructs the Riccati equations [D,V]

Let

```math
E_1=X_u/R,\qquad E_2=X_v/R,\qquad F=(E_1,E_2,N)\in SO(3).
```

The full moving-frame one-form is

```math
\Omega=F^{-1}dF=\begin{pmatrix}0&-rW\,dv&rS\,du\\rW\,dv&0&-rS\,dv\\-rS\,du&rS\,dv&0\end{pmatrix}.
```

Decompose $\Omega=U\,du+V\,dv$:

```math
U=\begin{pmatrix}0&0&rS\\0&0&0\\-rS&0&0\end{pmatrix},\qquad V=\begin{pmatrix}0&-rW&0\\rW&0&-rS\\0&rS&0\end{pmatrix}.
```

Without assuming the canonical differential identities, calculate the curvature of this prescribed connection:

```math
\partial_uV-\partial_vU+[U,V]=\begin{pmatrix}0&r(rS^2-W_u)&0\\r(W_u-rS^2)&0&-r(S_u+rSW)\\0&r(S_u+rSW)&0\end{pmatrix}.
```

**Theorem 6.1 [D,V].** Flatness $d\Omega+\Omega\wedge\Omega=0$ of this explicit $\mathfrak{so}(3)$ ansatz is *equivalent* to

```math
W_u=rS^2,\qquad S_u=-rSW.
```

**Proof.** The $(1,2)$ matrix entry vanishes exactly when the first differential identity holds; the $(2,3)$ entry vanishes exactly when the second holds. The other off-diagonal entries are their skew-symmetric partners.

The identities conserve the circle quantity:

```math
\frac{d}{du}(S^2+W^2)=2S(-rSW)+2W(rS^2)=0.
```

The value **one** is an initial normalization, not a necessary consequence of zero curvature alone. On the normalized positive centered branch, the equations recover $S=\mathrm{sech}(ru)$ and $W=\tanh(ru)$.

Taking the coframe $\vartheta^1=R\,du$, $\vartheta^2=R\,dv$, the relation $R_u=rWR$ also supplies the torsion-free structure equations. Hence $F(\vartheta^1,\vartheta^2,0)^T$ is locally exact and can be integrated to an immersion. This explains precisely how the scalar data, flat frame, and surface construction fit together.

## 7. Levi-Civita curvature, Gauss cancellation, and Darboux frames [D,V]

The tangent connection in the chosen frame is

```math
\omega_C=\Omega_{12}=-rW\,dv=-\kappa_u\,dv.
```

Its curvature is

```math
d\omega_C=-r^2S^2\,du\wedge dv=K_C\,dA_C,\qquad dA_C=R^2\,du\wedge dv.
```

The $(1,2)$ component of Maurer-Cartan gives an exact cancellation:

```math
d\omega_C+\Omega_{13}\wedge\Omega_{32}=-r^2S^2\,du\wedge dv+r^2S^2\,du\wedge dv=0.
```

Thus the **full ambient Euclidean frame form is flat**, while the **induced tangent Levi-Civita connection is curved**. Gauss-Codazzi states the compatibility between these assertions, not their equality.

Along a meridian ($v$ constant) the geodesic curvature and geodesic torsion vanish, while the signed normal curvature is $-rS^2$. Along a parallel ($u$ constant), the signed normal curvature is $+rS^2$, the geodesic curvature is $\pm rSW$ according to conormal orientation, and the geodesic torsion vanishes. The ambient curvature magnitude of the parallel is $rS$, by $S^2+W^2=1$.

These are Darboux/Frenet projections of the *same* frame geometry rather than independent differential models.

## 8. Catenoid-helicoid associated family and the global period obstruction [D,K]

Consider the holomorphic null curve

```math
\mathcal F(\zeta)=\left(\frac{\cosh(r\zeta)}r,-\frac{i\sinh(r\zeta)}r,\zeta\right).
```

Its derivative satisfies

```math
\mathcal F_\zeta=(\sinh(r\zeta),-i\cosh(r\zeta),1),\qquad \mathcal F_\zeta\cdot\mathcal F_\zeta=\sinh^2(r\zeta)-\cosh^2(r\zeta)+1=0.
```

The real part is $X_C$. The imaginary part is its conjugate helicoid:

```math
X_H=\mathrm{Im}\,\mathcal F=\left(\frac{\sinh(ru)}r\sin(rv),-\frac{\sinh(ru)}r\cos(rv),v\right).
```

For any real $\alpha$ define

```math
X_\alpha=\mathrm{Re}(e^{-i\alpha}\mathcal F)=\cos\alpha\,X_C+\sin\alpha\,X_H.
```

The resulting metric is always $I_C$, while the Hopf coefficient and the second form are

```math
Q_{H,\alpha}=-(r/2)e^{-i\alpha},\qquad II_\alpha=-r\cos\alpha(du^2-dv^2)-2r\sin\alpha\,du\,dv.
```

**Proof.** Multiplication of the null differential by a unit complex phase preserves its induced metric. The Hopf differential rotates by the same phase. Its absolute value stays $r/2$ and it remains holomorphic; hence the Gauss and Codazzi equations remain valid. In particular, $II_0=II_C$ and $II_{\pi/2}=-2r\,du\,dv$ with our normal.

**Global qualification.** The catenoid is periodic in $v$, but the helicoid changes height by $2\pi/r$ on one angular turn. More generally,

```math
X_\alpha(u,v+2\pi/r)-X_\alpha(u,v)=(0,0,(2\pi/r)\sin\alpha).
```

Only $\sin\alpha=0$ closes as a surface in $\mathbb R^3$ on the original angular cylinder without another quotient. **Local Gauss-Codazzi is not a global closing theorem.**

## 9. Main theorem: the cubic Master energy is the ambient sectional curvature [D,V]

For any real $C^2$ solution of the cubic Master ODE, let

```math
y_{uu}=r^2y-2\mu r^2y^3,\qquad \varepsilon_N=y_u^2-r^2y^2+\mu r^2y^4,\qquad z=\sqrt{\mu}\,y,\qquad e=\mu\varepsilon_N/r^2.
```

Then

```math
z_{uu}=r^2(z-2z^3),\qquad z_u^2=r^2(e+z^2-z^4).
```

**Theorem 9.1 [D,V] (local all-energy Gauss-Codazzi realization).** On every simply connected coordinate patch where $z>0$, choose

```math
I_e=z^{-2}(du^2+dv^2),\qquad II_e=-r(du^2-dv^2),\qquad H_m=0,\qquad Q_H=-r/2.
```

These forms satisfy Gauss-Codazzi for the constant ambient curvature

```math
k_0=-r^2e=-\mu\varepsilon_N.
```

Thus a local minimal immersion exists in the simply connected space form $M^3(k_0)$.

**Proof, step by step.**

1. The conformal factor is $e^{2\omega}=z^{-2}$, $\omega=-\ln z$. Therefore

```math
K_{I_e}=-z^2\omega_{uu}=zz_{uu}-z_u^2.
```

2. Insert both normalized Master identities:

```math
K_{I_e}=r^2(z^2-2z^4)-r^2(e+z^2-z^4)=-r^2(e+z^4).
```

3. The shape operator has principal curvatures $-rz^2$ and $+rz^2$:

```math
\det B=-r^2z^4,\qquad H_m=0.
```

4. Their difference is exactly constant:

```math
K_{I_e}-\det B=-r^2(e+z^4)+r^2z^4=-r^2e=k_0.
```

5. Codazzi holds because $H_m=0$ and $Q_H=-r/2$ is holomorphic and constant. Apply Theorem 2.1.

**Geometric energy table:**

| Energy | Ambient $k_0$ | Type | Positive-real-orbit qualification |
|---|---:|---|---|
| $-1/4<e<0$ | positive | spherical | positive nonconstant periodic solutions |
| $e=-1/4$ | $r^2/4$ | spherical | constant equilibrium $z=1/\sqrt2$ |
| $e=0$ | zero | Euclidean | positive separatrix $z=S$ |
| $e>0$ | negative | hyperbolic | positive subintervals; zeros prevent a regular metric continuation of the displayed ansatz |

The real energy is bounded below by $-1/4$, since $e=z_\theta^2+z^4-z^2$ and $z^4-z^2\ge-1/4$. The classification is of **specified local immersions**, not complete global surfaces at arbitrary energy.

### 9.1 The equilibrium is an explicit Clifford torus [D,V,K]

At $e=-1/4$, $z^2=1/2$ is constant, and

```math
I_{-1/4}=2(du^2+dv^2),\qquad II_{-1/4}=-r(du^2-dv^2),\qquad k_0=r^2/4.
```

The ambient round sphere has radius $2/r$. An explicit immersed Clifford torus in $\mathbb R^4$ is

```math
X_{\mathrm{Cl}}(u,v)=\frac{\sqrt2}{r}\big(\cos(ru),\sin(ru),\cos(rv),\sin(rv)\big).
```

It lies on the sphere of radius $2/r$, has $I=2(du^2+dv^2)$, and with normal $2^{-1/2}(\cos ru,\sin ru,-\cos rv,-\sin rv)$ has $II=-r(du^2-dv^2)$. Its principal curvatures in the sphere are $\pm r/2$ and its intrinsic curvature is zero.

This is a concrete identification of the **cubic equilibrium** with the flat minimal Clifford torus. It does not prove that nearby periodic orbits close globally as embedded spherical tori.

## 10. Converse: Gauss-Codazzi reconstructs the cubic energy quartic [D]

The converse is an important logical distinction. Start with **geometric data**, not with the Master ODE: prescribe $I=z^{-2}|d\zeta|^2$, $II=-r(du^2-dv^2)$ for some smooth positive $z(u)$, and suppose Gauss-Codazzi holds in a constant-curvature space form $k_0$.

The Codazzi equation is automatic. Put $\omega=-\ln z$ in the Gauss equation:

```math
\omega_{uu}=-k_0e^{2\omega}+r^2e^{-2\omega}.
```

**Proposition 10.1 [D].** This geometric equation has the first integral

```math
\omega_u^2=C_0-k_0e^{2\omega}-r^2e^{-2\omega}
```

for some real constant $C_0$, and therefore

```math
z_u^2=C_0z^2-r^2z^4-k_0.
```

**Proof, step by step.** Multiply the Gauss equation by $2\omega_u$. The left side is $(\omega_u^2)_u$. Integrating the right side gives $-k_0e^{2\omega}-r^2e^{-2\omega}+C_0$. Finally substitute $\omega_u=-z_u/z$ and multiply by $z^2$. This proof requires no division by $z_u$, so it covers ordinary turning points and the constant equilibrium.

The *additional canonical normalization* is $C_0=r^2$. Setting $e=-k_0/r^2$ produces

```math
z_u^2=r^2(e+z^2-z^4).
```

On nonconstant branches, differentiation followed by continuation through smooth ordinary turning points gives

```math
z_{uu}=r^2z-2r^2z^3.
```

**Logical boundary:** A first-order energy identity by itself can admit spurious constant/plateau solutions; our converse assumes the *second-order Gauss equation* from the beginning. The integration constant $C_0$ is independent of the ambient curvature and must be fixed before identifying the canonical Master normalization.

**Theorem-level conclusion:** Gauss-Codazzi within this precisely specified one-variable minimal-surface ansatz reconstructs the **cubic** Master energy equation, with $k_0=-r^2e$. This is not an assertion that every second-order equation is generated by Gauss-Codazzi, nor an assertion that the Master equation prescribes a unique immersion.

### 10.1 The unreduced geometric PDE

Keeping $\omega=\omega(u,v)$ instead of imposing independence of $v$, the equations give

```math
\Delta_0\omega+k_0e^{2\omega}-r^2e^{-2\omega}=0.
```

For $k_0>0$, the shift $\varphi=2\omega-\ln(r/\sqrt{k_0})$ gives an elliptic sinh-Gordon equation

```math
\Delta_0\varphi+4r\sqrt{k_0}\sinh\varphi=0.
```

For $k_0<0$, the analogous real shift produces an elliptic cosh-Gordon equation. At $k_0=0$, the equation is of Liouville type. The normalized one-variable cubic Master equation is a **reduction** of this two-variable Gauss-Codazzi PDE, not a general classification of its solutions.

## 11. Curvature of the third fundamental form: exact energy defect [D,V]

For invertible $B$, the third fundamental form is

```math
III_e(X,Y)=I_e(BX,BY)=r^2z^2(du^2+dv^2).
```

Its curvature is

```math
K_{III_e}=-\frac{(\ln z)_{uu}}{r^2z^2}.
```

Use the normalized Master equation and first integral to obtain

```math
(\ln z)_{uu}=\frac{zz_{uu}-z_u^2}{z^2}=-r^2\left(z^2+\frac{e}{z^2}\right).
```

Thus

```math
K_{III_e}=1+\frac{e}{z^4},\qquad K_{III_e}-1=\frac{e}{z^4}.
```

At zero energy, the third fundamental form has constant curvature $+1$ and is the pullback of the unit-sphere metric by the Euclidean Gauss map. At **nonzero** energy, $III_e$ generally does **not** have curvature $1$: a third fundamental form in a nonflat ambient space is not automatically a Euclidean Gauss-map sphere metric.

A corresponding potential defect is

```math
\omega_{uu}-r^2z^2=\frac{r^2e}{z^2},\qquad \omega=-\ln z.
```

These formulas precisely quantify how the zero-energy reciprocal Kähler/Gauss-map correspondence deforms away from the separatrix.

## 12. Reciprocal Kähler potentials, Gauss map, and projective structure [D]

On the separatrix $z=S$ we have the catenoid metric $g_C=R^2|d\zeta|^2$ and the spherical metric

```math
g_S=r^2S^2|d\zeta|^2=-K_Cg_C.
```

The stereographic Gauss-map coordinate can be chosen as

```math
g(\zeta)=-e^{r\zeta},\qquad g^*g_{S^2}=\frac{4|g_\zeta|^2}{(1+|g|^2)^2}|d\zeta|^2=r^2S^2|d\zeta|^2.
```

Both are locally Kähler metrics. In the convention where $g=4\partial_\zeta\partial_{\bar\zeta}\mathcal K\,|d\zeta|^2$, they have the explicit local potentials

```math
\mathcal K_C(u)=\frac{u^2}{4}+\frac{\cosh(2ru)}{8r^2},\qquad \mathcal K_S(u)=\ln\cosh(ru).
```

Their second derivatives satisfy

```math
(\mathcal K_C)_{uu}=R^2,\qquad (\mathcal K_S)_{uu}=r^2S^2,\qquad (\mathcal K_C)_{uu}(\mathcal K_S)_{uu}=r^2.
```

This is a **reciprocal-Hessian identity in a fixed coordinate**, not a Legendre transform, which would also transform its independent variable.

The centered sphere potential differs from $\ln(1+|g|^2)$ by $-ru-\ln2$, a local Kähler-gauge term. The same projective coordinate has Schwarzian

```math
\{g,\zeta\}=-r^2/2.
```

The Schwarzian defines a local projective connection coefficient; a choice of projective connection does **not** uniquely determine the sign or scale of a Riemannian metric.

## 13. Hopf curvature, Levi-Civita connections, and global holonomy [D,V]

Let $\phi=rv$. The spherical Kähler form is

```math
\omega_S=r^2S^2\,du\wedge dv=dW\wedge d\phi.
```

Thus $W$ is, up to sign convention, the moment-map coordinate for the circle action. Choose a local real Hopf connection

```math
A_H=\frac r2(1+W)\,dv,\qquad F_H=dA_H=\frac{r^2}{2}S^2\,du\wedge dv=\frac12\omega_S.
```

The catenoid and spherical Levi-Civita connection forms, with the conformal frames adopted here, are

```math
\omega_C=-rW\,dv,\qquad \omega_S^{\mathrm{LC}}=+rW\,dv.
```

Therefore

```math
A_H=\frac12\omega_S^{\mathrm{LC}}+\frac r2\,dv=-\frac12\omega_C+\frac r2\,dv.
```

The difference is closed locally, but the angular circuit gives

```math
\oint\frac r2\,dv=\pi,\qquad \exp\!\left(i\oint\frac r2\,dv\right)=-1.
```

Hence this closed difference is **not** removable by a globally single-valued $U(1)$ gauge transformation on the original angular cylinder. This agrees with the later correction H538 to the historical Hopf/Levi-Civita discussion.

In the orientation $du\wedge dv>0$, compactifying the sphere coordinate gives

```math
\int_{S^2}F_H=2\pi,\qquad \frac1{2\pi}\int_{S^2}F_H=1,\qquad \int_CK_C\,dA_C=-4\pi.
```

The connection potential is necessarily local: two gauge charts and a transition function are needed at the sphere poles. Opposite orientation or bundle-sign conventions reverse the Chern sign; the chosen local equations and integrals fix our conventions. The exterior spherical Gauss-map orientation must also be distinguished from the complex orientation of its stereographic chart.

## 14. Exact limitation across the general $q$ hierarchy [D,V]

For $q=(l-1)/2>0$, use dimensionless time $\theta=ru$ and the normalized level system

```math
A_{q,\theta\theta}=q^2A_q-q(q+1)A_q^{1+2/q},\qquad A_{q,\theta}^2=q^2(e_q+A_q^2-A_q^{2+2/q}).
```

On a positive branch set $z=A_q^{1/q}$. Algebra gives

```math
z_u^2=r^2(e_qz^{2-2q}+z^2-z^4),\qquad z_{uu}=r^2((1-q)e_qz^{1-2q}+z-2z^3).
```

Retain **the same** metric and constant Hopf ansatz as in Section 9:

```math
I=z^{-2}|d\zeta|^2,\qquad II=-r(du^2-dv^2),\qquad K_I=-r^2(qe_qz^{2-2q}+z^4).
```

Gauss therefore *requires*

```math
k_{0,\mathrm{required}}=K_I-\det B=-qr^2e_qz^{2-2q}.
```

**Proposition 14.1 [D,V].** For a nonconstant positive solution with $e_q\ne0$, $k_{0,\mathrm{required}}$ is constant within this specific ansatz **if and only if** $q=1$.

**Proof.** Since $q>0$ and $e_q\ne0$, the displayed function is constant along nonconstant $z>0$ exactly when the exponent $2-2q$ vanishes. Thus $q=1$.

This does **not** preclude higher-level geometric realizations with a different metric, nonconstant holomorphic Hopf differential, dependence on both coordinates, or a non-space-form ambient metric. This distinction is the archived problem **O382**.

### 14.1 Every level still has a Clifford equilibrium

The positive constant level solution satisfies

```math
z_{q,*}^2=\frac{q}{q+1},\qquad e_{q,*}=-\frac{q^q}{(q+1)^{q+1}}.
```

For this constant orbit, the same forms have $K_I=0$ and the required spherical curvature is

```math
k_{0,q}=r^2z_{q,*}^4=\left(\frac{qr}{q+1}\right)^2.
```

Thus **all levels admit an equilibrium Clifford-torus realization** under the chosen constant-form ansatz, even though the nonconstant all-energy space-form family is singled out at $q=1$. The equality at equilibrium does not establish a nonconstant higher-level family.

## 15. Binary quartics: two algebraic objects that must not be conflated [D,V]

In an $I$-orthonormal principal tangent frame with coordinates $(\xi,\eta)$, consider the product quartic of the two fundamental forms:

```math
Q_{\mathrm{ff}}(\xi,\eta)=(\xi^2+\eta^2)(k_1\xi^2+k_2\eta^2).
```

For the minimal family, $k_1=-rz^2$, $k_2=rz^2$, so

```math
Q_{\mathrm{ff}}=-rz^2(\xi^4-\eta^4).
```

The unweighted binary quartic invariants are

```math
I(Q_{\mathrm{ff}})=-12r^2z^4,\qquad J(Q_{\mathrm{ff}})=0,\qquad \mathrm{Disc}(Q_{\mathrm{ff}})=-256r^6z^{12},\qquad j(Q_{\mathrm{ff}})=1728.
```

For $z>0$ this quartic is nonsingular, and its moduli do not vary within the associated minimal family.

The **distinct** cubic Master energy quartic is

```math
F_e(X,Y)=-X^4+X^2Y^2+eY^4,\qquad \mathrm{Disc}(F_e)=-16e(1+4e)^2.
```

The energy quartic is singular at $e=0$ and $e=-1/4$ and otherwise defines a smooth genus-one double cover. It is **not** the same curve as $Q_{\mathrm{ff}}$, whose $j$ is always $1728$. In non-Euclidean ambients, formulas involving principal-curvature products use the *extrinsic* quantity $\det B=K_I-k_0$, not automatically the intrinsic $K_I$.

This makes the previous fundamental-form quartic investigation H421 part of Layer I/II algebraic geometry, with a typed relationship to but no automatic identification with the energy curve.

## 16. Outside the foundational layers: exact maps, extra choices

The purpose of the current investigation is the foundational geometry, not an unqualified identification with all ODE/PDE/SDE theories.

- A metric plus its integration measure, boundary pairing, and operator domain yields Laplace-Beltrami or weighted Sturm-Liouville realizations. The catenoid zero-mode area Jacobi equation reduces to an order-one Poschl-Teller expression, but the *general eigenvalue problem* retains its metric weight.
- The rank-two exponential system and a specified positive Gram envelope yield an Ermakov-Pinney amplitude. For the zero-energy centered potential, $\rho=\mu^{1/4}e^{\kappa/2}$ satisfies $\rho_{uu}=r^2\rho/4+\mu r^2/(4\rho^3)$. Not every Kähler metric uniquely prescribes this amplitude.
- Variational, stochastic, diffusion, and geometric-flow equations require an action, operator/domain, metric/noise covariance, evolution law, or boundary data not fixed by Gauss-Codazzi alone.
- Contact geometry can encode arbitrary smooth scalar second-order ODEs, while Gauss-Codazzi, Kähler, and projective geometry give **stronger** structures only under additional compatibility hypotheses.

The mathematical benefit of layering is to investigate these outer theories through *typed constructions* from an audited geometric foundation, while recording which arrows are reversible and what global information is lost.

## 17. Verification record, limitations, and open problems

**Independently symbolically checked [V] during this investigation:**

1. $X_C$ has $E=G=R^2$, $F=0$, $L=-r$, $M=0$, $N_2=+r$ and the corresponding normalized unit normal.
2. The explicit $3\times3$ Maurer-Cartan curvature matrix vanishes precisely for $W_u=rS^2$, $S_u=-rSW$.
3. For the cubic Master system, $K_I=-r^2(e+z^4)$ and $K_I-\det B=-r^2e$.
4. The third-form curvature is $K_{III}=1+e/z^4$.
5. The general-$q$ fixed-ansatz obstruction is $-qr^2e_qz^{2-2q}$.
6. The Clifford map at cubic equilibrium has precisely the required first and second forms.
7. The fundamental-form quartic has $J=0$, discriminant $-256r^6z^{12}$, and $j=1728$ when $z>0$.

These checks use exact algebra and differentiation, not a finite sample of parameter values. They do **not** establish global completeness and closing for nonzero energy, a uniqueness theorem outside the stated ansatz, or novelty.

**Open problems [O]:**

1. **Space-form closing:** Compute moving-frame holonomy, periods and possible immersed/embedded global completions of the spherical periodic solutions $-1/4<e<0$.
2. **Hyperbolic boundary:** Classify maximal positive branches and completeness behavior for $e>0$ near zeros of $z$.
3. **Higher levels:** Test other metric/Hopf ansätze, zeros of quadratic differentials, two-variable solutions, and ambient manifolds with variable curvature for $q\ne1$ (historical O382).
4. **Full elliptic Gauss-Codazzi:** Study regular nonseparable solutions of the $\sinh$-/cosh-Gordon reductions with explicit monodromy and period constraints.
5. **Algebraic geometry:** Seek proved maps or obstructions between the product-of-fundamental-forms quartic, Gram-square quartics, and the nonlinear Master energy quartic.
6. **Inverse reconstruction:** Identify the information lost by passing from an ambient flat frame to an intrinsic connection, from a projective Schwarzian to a metric, and from local compatibility to global immersion.

## 18. Proposed consolidation units and external references

| Candidate result | Evidence | Destination after audit |
|---|---|---|
| Conformal Gauss-Codazzi with explicit conventions | [D,K] | Layer II: surface compatibility |
| Riccati equations equivalent to a specified $\mathfrak{so}(3)$ Maurer-Cartan flatness system | [D,V] | Layer I/II interface |
| Catenoid forms, Levi-Civita curvature, and associated family | [D,V,K] | Layer II: canonical immersions |
| Cubic Master energy and ambient space-form curvature, plus normalized converse | [D,V,K] | Layer II: energy/geometry correspondence |
| Cubic and general-level Clifford equilibria | [D,V,K] | Layer II: spherical minimal surfaces |
| Third-form curvature and Kähler-potential defects | [D,V] | Layer II: Gauss and projective geometry |
| Specific higher-level $q\ne1$ fixed-ansatz obstruction | [D,V] | Layer I/II: limitations |
| Hopf connection, Chern number and half-holonomy | [D,V,K] | Layer II: symplectic and bundle geometry |
| Fundamental-form quartic versus energy quartic | [D,V] | Layer I/II: invariant theory |

**Primary project provenance:** The current GitHub **01-foundational/000**, **010**, **020** documents; archived **00-meta/CLAIMS.md** (H421, H424, H473, H474, H490, H509, H538); archived **04-follow-ups/fundamental-forms-willmore-hopf.md** and **04-follow-ups/riemann-marked-periods-gauss-manin-x04.md**, especially its sections 7 and 17.

**External classical background:** UCLA, *Math 120A lecture notes* (fundamental theorem of surfaces and Gauss-Codazzi), https://math.ucla.edu/~sucharit/120A-notes.html ; MathWorld, *Fundamental Theorem of Surface Theory*, https://mathworld.wolfram.com/FundamentalTheoremofSurfaceTheory.html ; S. Brendle, *Minimal surfaces in S3: a survey of recent results* (Clifford torus and the ambient Gauss equation), https://link.springer.com/article/10.1007/s13373-013-0034-2 .

**Conclusion.** The verified mathematical engine is not the assertion that every equation is Gauss-Codazzi. It is the more precise, bidirectionally checkable statement that *the canonical scalar fields and specified geometric data generate compatible first/second fundamental forms, and the one-variable minimal-surface Gauss equation reconstructs the cubic Master energy quartic after fixing its integration constant.* The distinction between scalar identities, geometric choices, local reconstruction, global periods, and outer differential-equation models is part of the result.
