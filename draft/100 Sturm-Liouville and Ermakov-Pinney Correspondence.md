---
id: SF-DRAFT-100
title: Sturm-Liouville and Ermakov-Pinney Correspondence
status: provisional
created: 2026-11-18
proposed_layers: [I, II, III]
depends_on: [SF-I-020, SF-DRAFT-040, SF-DRAFT-050, SF-DRAFT-060, SF-DRAFT-070, SF-DRAFT-080, SF-DRAFT-090]
related_claims: [F04, F08, H100, H107, H112, H169, H171, H172, H177, H178, H179, H183, H313, H314, H315, H373, H429, H430, H432]
---

# 100 Sturm–Liouville and Ermakov–Pinney Correspondence

**Status:** Provisional, extensive mathematical synthesis, not a canonical theorem chapter. [D] direct proof, [V] exact symbolic verification, [K] established mathematics, [H] archived source statement with its own evidence status, [C] corrected assertion, [O] open. Its “duality” language is **explicitly scoped** and does not imply an involutive equivalence of complete spectral problems, nonlinear flows, geometries or physical models.

**Central answer:** Yes, Sturm–Liouville and Ermakov–Pinney possess a deep **conditional amplitude–phase / symplectic / symmetric-square correspondence**. A linear Sturm–Liouville equation together with a nondegenerate Wronskian and a chosen Gram quadratic produces a Pinney amplitude. A positive Pinney amplitude with a fixed positive determinant reconstructs a zero-free complex linear solution through its Milne/Gudermannian phase. The squared envelope lies in the symmetric square of the linear solution space, and its reciprocal yields the original cubic Master separatrix under an additional zero-energy/zero-shift constraint. This is not a bijection between all self-adjoint Sturm–Liouville operators and all Ermakov–Pinney initial value problems, because the maps have essential domain, phase, Gram and energy data.

**Sources checked:** Main GitHub foundational SF-I-020, drafts 040, 050, 060, 070 and companion drafts 080 and 090; historical ZIP's `spectral-calculus.md`, `bernoulli-riccati.md`, `binary-quartic-and-spectral-curves.md`, `modular-riccati.md`, `bpst-yamabe-eguchi-hanson.md`, `friedmann-reciprocal-envelope.md`, and CLAIMS IDs H100/H107/H112/H169–H172/H177–H183/H313–H315/H373/H429–H432. The separate original source's canonical center $`c`$ and resolution $`r`$ are always kept in the equations. External classical references appear in §24.

## 1. Data types and the proposed duality diagram

Fix

```math
x,c,r,\mu>0,\qquad u=\ln(x/c),\qquad\theta=ru,\qquad S=\mathrm{sech}(ru),\qquad W=\tanh(ru).
```

The two starting differential equations are **different**:

```math
\mathrm{SL}:\quad\phi''+\Omega^2(u)\phi=0;\qquad \mathrm{EP}:\quad a''+\Omega^2(u)a=k a^{-3}.
```

The first is linear in $`\phi`$; the second is nonlinear in the positive amplitude $`a`$. For the canonical half-rate carrier, $`\Omega^2=-r^2/4`$. Their exact correspondence uses a two-dimensional real solution space $`V`$ with symplectic Wronskian and a symmetric quadratic form $`G`$:

```math
(V,\mathscr W,G)\ \xrightarrow{\mathrm{quadratic\ envelope}}\ a^2=\phi^TG\phi\ \xrightarrow{\mathrm{positive\ square\ root}}\ a\ \xrightarrow{\mathrm{phase\ reconstruction}}\ \Phi=a e^{i\vartheta}.
```

When $`k=\mathscr W^2\det G>0`$ and $`a>0`$, the phase derivative is $`\vartheta'=\sqrt{k}/a^2`$. The correspondence preserves the **differential expression** and the Wronskian determinant after its data are specified; it forgets an initial phase and basis representation unless those are tracked.

## 2. The universal two-way theorem for variable coefficients [D,K]

**Theorem 2.1 (Pinney–Milne reconstruction).** Let $`\Omega^2(u)`$ be a continuous real function on an interval. Let $`\phi_1,\phi_2`$ form a real fundamental pair of $`\phi''+\Omega^2\phi=0`$, with nonzero Wronskian $`\mathscr W`$. Given a symmetric real matrix $`G`$ with $`k=\mathscr W^2\det G`$, on a subinterval where $`a=(\phi^TG\phi)^{1/2}>0`$ one has

```math
a''+\Omega^2a=k/a^3.
```

If $`k>0`$, define $`\vartheta(u)=\vartheta(u_0)+\sqrt{k}\int_{u_0}^u a(s)^{-2}ds`$. Then $`\Phi=a e^{i\vartheta}`$ solves $`\Phi''+\Omega^2\Phi=0`$ with $`\mathscr W(\Phi,\bar\Phi)=-2i\sqrt{k}`$.

**Proof.** The Gram determinant identity yields

```math
2(a^2)(a^2)''-[(a^2)']^2+4\Omega^2(a^2)^2=4\mathscr W^2\det G.
```

Divide by $`4a^3`$ to obtain Pinney. For $`\Phi=a e^{i\vartheta}`$, the imaginary part of $`\Phi''+\Omega^2\Phi`$ is proportional to $`(a^2\vartheta')'`$ and vanishes; the real part is $`a''+\Omega^2a-a(\vartheta')^2=k/a^3-k/a^3=0`$. The Wronskian follows from the polar formula.

**Conversely:** For every positive solution of EP with fixed $`k>0`$ on a simply connected real interval, the constructed $`\Phi`$ is a zero-free complex solution and its real and imaginary parts are independent because their Wronskian has magnitude $`\sqrt k`$. A constant rotation of $`\Phi`$ preserves the same amplitude $`a`$. This **U(1) phase ambiguity** prevents the envelope alone from determining a unique linear solution pair.

## 3. A genuine symmetric-square mechanism, not an accidental coefficient match [D,V]

For $`\Omega^2=-r^2/4`$ the linear carrier is

```math
\phi_+=e^{ru/2},\qquad\phi_-=e^{-ru/2},\qquad \mathscr W(\phi_+,\phi_-)=-r.
```

Its quadratic products span a three-dimensional vector space:

```math
\mathrm{Sym}^2V=\mathrm{span}\{e^{ru},1,e^{-ru}\}.
```

Every Gram square $`J=a^2=Ae^{ru}+2C+Be^{-ru}`$ satisfies the third-order linear equation

```math
J'''-r^2J'=0.
```

The **full-rate** second-order backbone $`J''=r^2J`$ is the codimension-one subfamily $`C=0`$. This explains the apparent factor-of-two tension between the original framework's linear equation and the Pinney equation: **the original $`J`$ is quadratic in solutions of the half-rate linear equation**.

### 3.1 The Gram invariant and Pinney strength

For a general real Gram matrix $`G=\begin{pmatrix}A&C\\C&B\end{pmatrix}`$,

```math
k=r^2(AB-C^2),\qquad J'^2=r^2(J^2-4CJ-4(AB-C^2)).
```

The full-rate quadratic constraint $`J^2-(J'/r)^2=\mu`$ holds for the canonical centered choice $`C=0`$, $`AB=\mu/4`$. If $`C\ne0`$, the invariant is replaced by

```math
J^2-(J'/r)^2-4CJ=4(AB-C^2),
```

with $`C`$ additionally encoding the autonomous Pinney energy $`E_{\rm EP}=-r^2C/2`$. The squared-envelope third-order system is linear even though its positive square root satisfies a nonlinear second-order ODE.

## 4. Full canonical reconstruction from a single complex solution [D,V]

Choose

```math
A=B=\sqrt\mu/2,\qquad C=0,\qquad k=\mu r^2/4.
```

Then

```math
J=\sqrt\mu\cosh(ru),\quad a=\mu^{1/4}\sqrt{\cosh(ru)},\quad \Phi=\mu^{1/4}[\cosh(ru/2)+i\sinh(ru/2)].
```

All of the following exact expressions refer to **the same selected solution**:

```math
\Phi''=r^2\Phi/4,\qquad |\Phi|=a,\qquad\Phi^2=\sqrt\mu[1+i\sinh(ru)],\qquad\arg\Phi=\mathrm{gd}(ru)/2.
```

The complex logarithm identity is

```math
\mathrm{Log}[1+i\sinh(ru)]=\ln\cosh(ru)+i\mathrm{gd}(ru),\qquad u\in\mathbb R.
```

Hence the complex logarithmic derivative is

```math
Q:=\frac{\Phi'}{\Phi}=\frac r2[W+iS],\qquad Q'+Q^2=r^2/4.
```

The **real** original field follows by taking the inverse squared amplitude:

```math
y(u)=\frac1{a^2}=\frac{S}{\sqrt\mu}=2xf_\mu(x;r,c),\qquad y''=r^2y-2\mu r^2y^3.
```

This is the sought Sturm–Liouville–Pinney–Master *commuting reconstruction*, with all normalization factors visible.

## 5. A new canonical Riccati pair and its real/imaginary dynamics [D,V]

Write the complex Riccati variable as $`Q=H+iB`$, where

```math
H(u)=\frac12\partial_u\ln J=\frac r2W,\qquad B(u)=\frac12\partial_u\mathrm{gd}(ru)=\frac r2S.
```

**Theorem 5.1 (canonical amplitude–phase circle).** The pair $`(H,B)`$ satisfies the closed autonomous system

```math
H'=2B^2,\qquad B'=-2HB,\qquad H^2+B^2=r^2/4.
```

**Proof.** Split the scalar complex Riccati identity $`Q'+Q^2=r^2/4`$ into real and imaginary parts, use $`W'=rS^2`$, $`S'=-rSW`$, and insert the invariant $`S^2+W^2=1`$. The real equation $`H'=r^2/4-H^2+B^2`$ becomes $`H'=2B^2`$ precisely because the circle invariant is preserved.

**Reconstruction:** Choosing $`B>0`$ gives $`B=\sqrt{r^2/4-H^2}`$, $`W=2H/r`$, $`S=2B/r`$ and

```math
\vartheta'=B,\qquad a'/a=H,\qquad y=\frac{2B}{r\sqrt\mu}.
```

The last identity follows because $`y=S/\sqrt\mu`$. Thus one positive semicircular solution of a **complex Riccati equation** determines both the nonlinear pulse and the Pinney envelope, up to the expected integration constants and normalization.

### 5.1 The logistic flow is the real projection

Under $`W=2H/r`$, the first real equation reduces to

```math
W'=r(1-W^2).
```

Set $`P=(1+W)/2`$; then

```math
P'=2rP(1-P),\qquad P=\frac{(x/c)^{2r}}{1+(x/c)^{2r}}.
```

This is the canonical logistic equation as a projective variable of the same linear carrier. It is also the coordinate from which BPST cumulative-charge and Beta/Jacobi diffusion formulas are constructed in draft 060, *after their own data are supplied*. No stochastic or gauge interpretation follows from $`P`$ alone.

## 6. Schwarzian and Cayley reconstruction [D,V]

The projective ratio of $`\Phi`$ and $`\bar\Phi`$ is

```math
Z=\Phi/\bar\Phi=e^{i\mathrm{gd}(ru)}=S+iW=i\frac{e^{ru}-i}{e^{ru}+i}.
```

It is a Möbius transform of the exponential ratio of the two real half-rate basis solutions. Thus

```math
\{Z,u\}=-r^2/2,
```

which is precisely the Schwarzian projective connection associated with $`\Phi''-r^2\Phi/4=0`$.

The *general* phase identity from draft 090 is

```math
\{\vartheta,u\}=-2a''/a,\qquad \{e^{2i\vartheta},u\}=\{\vartheta,u\}+2(\vartheta')^2=2\Omega^2.
```

The inverse-cube Pinney term cancels in the Schwarzian of the full complex developing map. This explains how a nonlinear phase-amplitude system yields the same projective curvature as its underlying linear equation. It is **not** an identity between the Schwarzian and an arbitrary Levi-Civita scalar curvature without a separately chosen metric.

## 7. The Gudermannian primitive is a canonical action angle [D,V]

The original symmetrical profile is

```math
f_\mu(x;r,c)=\frac{S}{2\sqrt\mu x},\qquad dx/x=du.
```

Therefore

```math
\vartheta(x)=r\sqrt\mu\int_c^x f_\mu(s;r,c)ds=\frac12\mathrm{gd}(r\ln(x/c)).
```

This is not only an arctangent primitive: it is the phase demanded by Wronskian conservation in Pinney reconstruction. Indeed

```math
a^2\vartheta'=\sqrt k=r\sqrt\mu/2,
```

so the phase advance is an **inverse-square-amplitude integral**. In the more general $`a>0`$, $`k>0`$ case the corresponding Milne phase is $`\vartheta(u)=\sqrt{k}\int^u a(s)^{-2}ds`$. The Gudermannian occurs because $`a^2\propto\cosh(ru)`$, not because all Ermakov–Pinney solutions have Gudermannian phase.

## 8. Symplectic and Noether structures: three inequivalent invariants [D,K]

A linear equation $`\phi''+\Omega^2\phi=0`$ has a constant antisymmetric Wronskian pairing on its real two-dimensional solution space. A Gram quadratic $`G`$ has the determinant $`\delta_G`$; their invariant product $`k=\mathscr W^2\delta_G`$ is the Pinney inverse-cube coefficient. For a positive Pinney solution, any real linear solution $`y`$ carries the Ermakov–Lewis quadratic integral

```math
I_{\rm EL}=\frac12[(ay'-a'y)^2+k(y/a)^2].
```

Each is conserved, but for different reasons: the Wronskian is a symplectic solution-space pairing, $`k`$ is a fixed Gram determinant contraction, and $`I_{\rm EL}`$ is a quadratic expression coupling a *chosen* amplitude and linear solution. The autonomous Pinney energy

```math
E_{\rm EP}=\frac12(a')^2-\frac{r^2}{8}a^2+\frac{k}{2a^2}=-r^2C/2
```

is a fourth quantity; it comes from translation symmetry of the constant-coefficient Pinney Lagrangian and is not simply the Wronskian itself.

### 8.1 The angular-momentum interpretation is mathematical

The complex linear solution $`\Phi=a e^{i\vartheta}`$ may be identified with the real planar pair $`(\mathrm{Re}\Phi,\mathrm{Im}\Phi)`$. Its constant oriented area speed is

```math
\mathrm{Im}(\bar\Phi\Phi')=a^2\vartheta'=\sqrt k.
```

The radial equation of the linear planar system is Pinney, with the inverse-cube term arising from fixed angular momentum of this **auxiliary plane**. This is a legitimate mechanical interpretation of the mathematical equations, not proof that the original Symmetrical Function describes a physical central-force system.

## 9. The full-rate logarithmic Riccati and its half-rate complex factor [D,V]

The full-rate backbone $`J''=r^2J`$ has real Riccati logarithmic derivative

```math
h_J:=J'/J=rW,\qquad h_J'+h_J^2=r^2.
```

The half-rate complex carrier has $`Q=(r/2)(W+iS)`$ with $`Q'+Q^2=r^2/4`$. Their relationship is

```math
h_J=2\mathrm{Re}\,Q,\qquad \frac{\sqrt\mu}{J}=\frac{2\mathrm{Im}\,Q}{r}.
```

The two Riccati equations are *not the same equation* with a symbol renamed: the full-rate $`J`$ is the **squared modulus of the half-rate complex solution**. This is the precise symmetric-square explanation of the framework's apparently self-referential Riccati web.

## 10. Riccati to Miura, Darboux and the canonical Pöschl–Teller Hessian [D,V]

For a nonvanishing linear solution $`\psi`$, the logarithmic derivative $`q=\psi'/\psi`$ factors its corresponding scalar operator:

```math
(-\partial_u-q)(\partial_u-q)=-\partial_u^2+q'+q^2.
```

For the canonical complex $`q=Q`$, this gives a **complex coefficient factorization** of $`-\partial_u^2+r^2/4`$. It is not a self-adjoint factorization using the Hilbert adjoint $`q^*`$ unless the coefficients are real.

The canonical **real** Master Hessian is separately

```math
\mathcal L_r=-\partial_u^2+r^2-6r^2S^2=A_2^\dagger A_2-3r^2,\qquad A_2=\partial_u+2rW.
```

Its zero mode is proportional to $`SW`$; its negative mode is $`S^2`$. The factorization follows from $`W'=rS^2`$ and $`S^2+W^2=1`$. This Darboux/Miura structure belongs to the *linearization of the nonlinear Master profile*, not directly to the carrier $`-\partial_u^2+r^2/4`$ or to a unique physical Schrödinger system.

## 11. A new direct bridge to the chosen curvature/torsion scalar pair [D,V,H313]

Draft 040 selected a **separate** spatially flat warped Lorentzian metric with scale $`a`$ and logarithmic rate $`H=a'/a`$. For the canonical solution, the Riccati pair of §5 gives $`H'=2B^2`$, $`H^2+B^2=r^2/4`$. Therefore its selected local Weitzenbock quadratic torsion scalar and Levi-Civita scalar curvature can be written directly in terms of *the same complex Riccati solution*:

```math
\mathbb T=6H^2=6(\mathrm{Re}\,Q)^2,\qquad \mathring{\mathcal R}=6(H'+2H^2)=12|Q|^2=3r^2.
```

The teleparallel boundary divergence is

```math
\mathbb B=6(H'+3H^2)=\mathbb T+3r^2.
```

**Proof.** Substitute $`H'=2B^2`$ and the circle $`H^2+B^2=r^2/4`$ into the definition of the three geometric scalars. No gravitational field equation is used.

**Scope:** These expressions require the **declared warped metric and preferred tetrad**. The real and imaginary parts of a generic Sturm–Liouville logarithmic derivative do *not* generate a constant-curvature warped geometry without those choices. The identity clarifies the foundational algebro-geometric interface rather than producing a physical source model.

## 12. A new simultaneous bridge to the catenoid and its surface quartic [D,V,H421]

The selected catenoid immersion of drafts 030/050 has Gaussian curvature

```math
K_{\rm cat}=-r^2S^4.
```

Using $`B=(r/2)S`$ from the same canonical complex Riccati carrier,

```math
K_{\rm cat}=-\frac{16}{r^2}B^4.
```

Its surface fundamental-form quartic at minimal points satisfies

```math
I_{\rm surf}=12K_{\rm cat}=-\frac{192}{r^2}B^4,\quad J_{\rm surf}=0,\quad \Delta_{\rm surf}=256K_{\rm cat}^3\ne0,\quad j_{\rm surf}=1728.
```

The trace-free Ricci square of the **different four-dimensional warped geometry** in draft 040 is

```math
\mathring S_{\alpha\beta}\mathring S^{\alpha\beta}=\frac{3r^4}{4}S^4=12B^4=-\frac{3r^2}{4}K_{\rm cat}.
```

These are equalities of explicitly assigned scalar functions at the same canonical logarithmic coordinate. They are **not** isometries or bundle maps between the two- and four-dimensional manifolds. They show exactly how one projective/polar linear carrier can be read through several separate geometric interfaces.

## 13. A negative control: the Master energy quartic is singular on this branch [D,V]

The separatrix Master energy polynomial is $`P_0(z)=z^2-z^4`$, with a double root at zero. Its raw quartic discriminant vanishes:

```math
I_0=1,\qquad J_0=-2,\qquad\Delta_{\rm Master}=0.
```

But the surface fundamental-form quartic of §12 is nonsingular for finite $`u`$ and has $`j_{\rm surf}=1728`$. The Pinney Gram-square quartic also has vanishing discriminant for **every** Gram coefficient choice, even when $`k>0`$. These are **three distinct quartics**, and their degenerations do not classify each other automatically. A universal identification between the Master energy, Pinney Gram and catenoid curvature quartics is disproved by their explicit discriminants.

## 14. What remains true for a general Sturm–Liouville operator [D,K]

After the unitary Liouville transformation, a general weighted Sturm–Liouville problem becomes a scalar real Schrödinger-type equation $`\phi''+\Omega^2(u;\lambda)\phi=0`$. At **each chosen spectral parameter $`\lambda`$**, a real fundamental pair has a Wronskian and its quadratic forms generate local Pinney solutions, with $`k`$ determined by the Gram determinant.

However, choosing a different $`\lambda`$ changes the linear carrier, its oscillation theory, the Weyl solution and the phase function. The resulting Pinney amplitude is a nonlinear auxiliary solution **depending on $`\lambda`$ and the Gram choice**, not a spectral eigenfunction and not an autonomous function with an invariant universal modulus $`j`$.

A self-adjoint Sturm–Liouville operator additionally requires its Hilbert space, endpoint classification and boundary conditions. The EP nonlinear ODE plus an amplitude does not reconstruct those choices. The precise “duality” pertains to **solutions of the differential expression**, not to the completed spectral operator category.

## 15. Complex phases and limit-point/limit-circle boundaries [D,C]

A complex solution normalized by its imaginary Wronskian is zero-free on a real interval when its real and imaginary parts have nonzero constant Wronskian. This gives a smooth Pinney amplitude. Yet it need not be square integrable at either endpoint. Conversely a Weyl–Titchmarsh solution selected by an $`L^2`$ condition at a singular endpoint carries an analytic spectral boundary function $`m(\lambda)`$, not an arbitrary fixed Gram phase.

The correspondence consequently has three levels of data:

1. **Local ODE**: rank-two linear solution pair $`\leftrightarrow`$ positive Pinney amplitude plus phase.
2. **Global differential geometry**: continuation and monodromy of the phase/projective developing map, with possible branch or coordinate obstructions.
3. **Spectral operator**: endpoint domains and self-adjoint extensions, preserved only if an explicit unitary or appropriate boundary transformation is supplied.

A calculation valid at level 1 cannot be silently promoted to levels 2 or 3.

## 16. Finite nonlinear energy is an obstruction to elementary Pinney reciprocity [D,H313]

For a general Gram form with $`C\ne0`$, the reciprocal $`y=1/J`$ obeys

```math
y''=r^2y-6Cr^2y^2-8(AB-C^2)r^2y^3.
```

Thus the **unshifted cubic Master equation** is recovered only at $`C=0`$ and $`(AB-C^2)=\mu/4`$. For the *different* finite nonlinear energy extension with $`\varepsilon\ne0`$, the reciprocal envelope acquires a quintic term:

```math
a''=r^2a/4+\delta_Gr^2a^{-3}+3\varepsilon a^5/4.
```

This is no longer pure Pinney. Periodic dn branches of the nonlinear Master equation produce genuine smooth elliptic curves, whereas the elementary positive Gram/Pinney carrier describes the centered zero-energy separatrix. Any “duality across all energies” needs a new, explicit transformation and cannot follow from the old zero-energy identity alone.

## 17. Resolution r=2: all branches of the diagram at once [D,V]

Fix $`r=2`$, $`c>0`$, $`\mu>0`$, and $`u=\ln(x/c)`$. The linear half-rate carrier and complex logarithm are

```math
\Phi=\mu^{1/4}[\cosh u+i\sinh u],\qquad\Phi''=\Phi,\qquad\Phi^2=\sqrt\mu[1+i\sinh(2u)].
```

Its squared modulus and Pinney equation are

```math
J=\sqrt\mu\cosh(2u),\qquad a=\sqrt J,\qquad a''=a+\mu/a^3.
```

The complex Riccati pair and scalar identity become

```math
Q=\Phi'/\Phi=W_2+iS_2,\qquad Q'+Q^2=1,\qquad H'=2B^2,\quad B'=-2HB,\quad H^2+B^2=1.
```

Here $`H=W_2`$, $`B=S_2`$, and with the *original* $`x`$ variable

```math
S_2=\frac{2c^2x^2}{x^4+c^4},\qquad W_2=\frac{x^4-c^4}{x^4+c^4},\qquad f_\mu(x;2,c)=\frac{c^2x}{\sqrt\mu(c^4+x^4)}.
```

The phase, the source primitive and the normalized nonlinear pulse are

```math
\vartheta=\arctan(x^2/c^2)-\pi/4,\qquad \int f_\mu dx=\frac{1}{2\sqrt\mu}\arctan(x^2/c^2)+C_0,\qquad y=S_2/\sqrt\mu.
```

The nonlinear pulse satisfies

```math
y''=4y-8\mu y^3,\qquad (y')^2=4(y^2-\mu y^4).
```

The Master Hessian, after the *separate* Liouville transformation of $`p=x^3,w=x`$, is

```math
\mathcal L_2=-\partial_u^2+4-24\mathrm{sech}^2(2u),\qquad\sigma_{\rm disc}=\{-12,0\},\qquad\sigma_{\rm ess}=[4,\infty).
```

The chosen four-dimensional warped metric's scalars are $`\mathbb T=6W_2^2`$, $`\mathbb B=\mathbb T+12`$ and $`\mathring{\mathcal R}=12`$. The different catenoid surface has $`K_{\rm cat}=-4S_2^4`$. Every equality is a separate interpretation of **the same algebraic fields**, with the dimension and geometric construction stated. None is a physical identity between a spectral operator, a surface, a spacetime and a stochastic process.

## 18. Doubling and higher-resolution recursion without losing c [D,V]

Let $`t=x/c>0`$. For every integer $`m\ge1`$ define

```math
S_m=\frac{2t^m}{1+t^{2m}},\qquad W_m=\frac{t^{2m}-1}{t^{2m}+1}.
```

For doubling,

```math
S_{2m}=\frac{S_m^2}{2-S_m^2},\qquad W_{2m}=\frac{2W_m}{1+W_m^2}.
```

The corresponding envelope and complex linear carrier are

```math
a_m^2=\sqrt\mu\cosh(m\ln(x/c)),\qquad\Phi_m=\mu^{1/4}[\cosh(mu/2)+i\sinh(mu/2)].
```

Thus the recurrence propagates through the pulse $`S_m`$, kink $`W_m`$, complex logarithmic derivative $`Q_m`$, squared Pinney envelope $`J_m`$, phase $`\vartheta_m`$ and reciprocal Master profile *simultaneously*. One may also use Chebyshev polynomials $`\cosh(2z)=2\cosh^2z-1`$ or the exponential Lucas recurrence.

**Caution:** A fixed $`r`$ changes the exponential monomial degree in $`x/c`$ and scales the spectral operator coefficients. Rescaling the logarithmic clock $`\theta=ru`$ makes many **local normalized equations** look identical, but generally does not preserve the original $`x`$-measure, boundary conditions, chosen real cycle or a physical time without further transformations.

## 19. A generating-function interpretation and the complex half-angle map [D]

Write $`T=(x/c)^{r/2}`$, so $`e^{ru}=T^2`$. The complex carrier can be represented as

```math
\Phi=\frac{\mu^{1/4}}2[(1+i)T+(1-i)T^{-1}],\qquad\bar\Phi=\frac{\mu^{1/4}}2[(1-i)T+(1+i)T^{-1}].
```

Their product is $`\sqrt\mu(T^2+T^{-2})/2=\sqrt\mu\cosh(ru)`$; their ratio is a Möbius transform of $`T^2`$. The half-angle carrier therefore provides an **algebraic square root of the full-rate hyperbola** in a rank-two complex linear representation. The same mechanism explains the involution $`u\mapsto-u`$: $`S`$ and $`a`$ are even, $`W`$ and $`\vartheta`$ odd, while $`\Phi(-u)=\bar\Phi(u)`$ on the real line. Those parity statements are consequences of the exact centered normalization, not generic properties of all Pinney solutions.

## 20. What the correspondence preserves and what it loses [D,C]

| Map | Preserved mathematical datum | Data that must be added or may be lost |
|---|---|---|
| Linear pair plus Gram $`\to a`$ | coefficient $`\Omega^2`$ and $`k=\mathscr W^2\det G`$ | basis, initial phase, sign, positivity interval |
| Positive $`a`$, $`k>0\to\Phi`$ | $`\Omega^2`$, Wronskian magnitude | arbitrary constant U(1) phase |
| $`\Phi\to Q=\Phi'/\Phi`$ | Riccati/projective differential expression | overall complex normalization, zeros/branch choice |
| $`Q\to Z=\Phi/\bar\Phi`$ | projective Schwarzian | absolute phase and real amplitude without additional normalization |
| $`a\to y=a^{-2}`$ | exact reciprocal differential identity | cubic Master only when $`C=0`$ and $`\delta_G=\mu/4`$ |
| Original $`x\to u=\ln(x/c)`$ | Liouville equivalence of specified formal SL coefficients | boundary domain and measure must be transformed |
| Selected $`a\to`$ warped metric | specified scale and its curvature/torsion scalars | spatial topology, tetrad, source and action not inherent |
| Nonlinear orbit $`\to`$ energy quartic | energy curve and its $`I,J,\Delta,j`$ | marked differential, real cycle, complete operator spectrum |

This table is the formal answer to the word **duality**: it is a network of reconstructible local structures with declared gauge and domain, not a universal replacement of one theory by another.

## 21. A mathematical obstruction: same Sturm–Liouville expression, different spectral problem [C]

Take the differential expression $`H=-\partial_u^2`$ on $`(0,\pi)`$ and compare Dirichlet and Neumann boundary conditions. They have the same Riccati, Wronskian and local Pinney construction for any chosen $`\lambda`$, yet their eigenvalue sequences are respectively

```math
\sigma_D=\{1,4,9,\ldots\},\qquad\sigma_N=\{0,1,4,9,\ldots\}.
```

The local EP envelope therefore cannot encode a unique **self-adjoint Sturm–Liouville operator** or recover boundary spectral multiplicities without the endpoint conditions. Likewise two linear solutions can produce several distinct positive Pinney amplitudes according to their Gram quadratic, and different complex phases can represent the same real amplitude up to gauge.

## 22. A second obstruction: different quartics from the same canonical profile [C]

At the separatrix the nonlinear Master energy curve has $`\Delta=0`$. The constructed Gram-square quartic has $`\Delta=0`$ **for all** Gram forms, while the catenoid's fundamental-form quartic has $`\Delta\ne0`$ and $`j=1728`$ for all finite nonflat points. The same $`\mathrm{sech}(ru)`$ profile participates in all three constructions because the **maps assigning quartics** are distinct. No unique binary quartic $`I,J`$ classifies every Sturm–Liouville, Ermakov–Pinney, surface and stochastic realization.

## 23. Further exact developments and open questions [O]

1. **General spectral parameter:** Determine when the positivity/phase representation of an $`m`$-function selected by half-line boundary conditions is compatible with a global positive Pinney envelope; track $`\lambda`$ and the Wronskian normalization throughout.
2. **General Gram circle:** For $`C\ne0`$ or a non-centered positive Gram form, find a canonical equation for the locus of $`Q=\Phi'/\Phi`$ in the complex Riccati plane, rather than assuming it always lies on $`|Q|=r/2`$.
3. **Monodromy and complex Log:** Compute analytic continuation of $`\Phi`$, $`\mathrm{gd}(r\mathrm{Log}(x/c))`$ and their projective Cayley map for integer and noninteger $`r`$; identify the branch and pole divisors.
4. **Periodic carriers and Lamé:** Extend the amplitude-phase/symmetric-square construction to a selected nonzero-energy Jacobi dn/Lamé operator and determine whether its Pinney Gram determinant can encode useful Floquet/period information. The Master energy curve and spectral curve remain typed separately.
5. **Geometric catenoid / warped metric interface:** Test whether the simultaneous scalar identities in §§11–12 arise from a natural functor between moving-frame bundles or are simply evaluations of common scalar fields. Do not infer isometry across dimensions.
6. **Higher-rank Jacobi fields:** Generalize the amplitude-phase construction to matrix Pinney/Riccati equations, preserving the required matrix noncommutativity and symplectic structure.
7. **Double-angle hierarchy:** Track whether resolution doubling induces a meaningful map on self-adjoint SL domains or only on local differential expressions and rational profile formulas.
8. **Noether/Lewis:** Compare the $`SL_2`$ moment map, Ermakov–Lewis integral, and projective Schwarzian in a single presymplectic variational formalism, with boundary terms and gauge normalization specified.

## 24. Sources, audit and mathematical conclusion

**Reproducibility.** The new algebraic equations were checked by exact derivatives of $`J=Ae^{ru}+2C+Be^{-ru}`$, $`\Phi=\mu^{1/4}[\cosh(ru/2)+i\sinh(ru/2)]`$, and $`Q=(r/2)(W+iS)`$. Explicit tests verify the Riccati pair, constant modulus, Schwarzian of the projective ratio, Gram/Pinney identity, reciprocal Master cubic, $`r=2`$ rational doubling, Pöschl–Teller translation zero mode and curvature/torsion scalar reductions. Operator spectrum and limit-point criteria rely on classical self-adjoint Sturm–Liouville theory with specified domains.

**External classics:** NIST DLMF https://dlmf.nist.gov/1.13 and https://dlmf.nist.gov/1.18 for Liouville and Weyl–Sturm–Liouville; https://dlmf.nist.gov/4.23 for Gudermannian; https://dlmf.nist.gov/22.19 for Jacobi/soliton forms; Ermakov–Pinney nonlinear superposition https://www.sciencedirect.com/science/article/pii/S0378475406002631 and Lewis invariant / Darboux correspondence https://www.sciencedirect.com/science/article/pii/S037596010300495X . Historical user research provenance is listed in the front matter and companion drafts 080 and 090; exploratory additions retain provisional status.

**Proposed consolidation:** Layer I: symmetric-square theorem, Gram/Wronskian constant and complex-log resolution hierarchy; Layer II: Riccati–Gudermannian–Schwarzian Cayley chart and explicitly chosen geometric metrics; Layer III: Liouville/Sturm–Liouville/Pinney two-way construction, nonlinear Master reciprocal and its Pöschl–Teller Hessian; Layer IV: additional spectral/stochastic/gauge implementations with independently declared domains, measures and actions.

**Final answer:** In the Symmetrical Framework, Sturm–Liouville and Ermakov–Pinney are connected by a **conditional nonlinear-superposition duality of solutions and phases**. The original full-rate exponential backbone is the symmetric square of a half-rate rank-two linear system; its centered positive Gram amplitude is Pinney; its reciprocal square is the cubic Master separatrix; and the Gudermannian is the polar phase of a single zero-free complex linear carrier. This is a coherent algebro-geometric interface, not an equivalence between every Sturm–Liouville spectrum, every Pinney initial-value problem or every external mathematical/physical realization.
