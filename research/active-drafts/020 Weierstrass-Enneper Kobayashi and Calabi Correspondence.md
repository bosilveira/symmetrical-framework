---
id: SF-DRAFT-020
title: Weierstrass-Enneper, Kobayashi, and Calabi Correspondence
status: provisional
created: 2026-11-18
proposed_layers: [I, II, III]
depends_on: [SF-I-000, SF-I-010, SF-I-020, SF-DRAFT-010]
related_claims: [H114, H117, H421, H423, H424, H466, H467, H468, H469, H473, H474, H490, H503]
---

# 020 Weierstrass-Enneper, Kobayashi, and Calabi Correspondence

**Status:** Complete provisional mathematical investigation for the foundational and geometric layers, not a canonical theorem chapter. All proposed consequences require claim-by-claim consolidation. Classical constructions are not asserted to be new.

**Question:** Are the canonical Gauss-Codazzi, Kähler, Levi-Civita, catenoid–helicoid and Riemann-minimal-example constructions pointing toward a precise bridge between the Euclidean Weierstrass-Enneper representation and Kobayashi's Lorentzian representation, via Gudermannian, logarithmic derivatives, Calabi's correspondence and a complex “Wick rotation”?

**Principal conclusion:** Yes. The same *holomorphic null data* yield Euclidean minimal and Lorentz-Minkowski spacelike maximal surfaces through an explicit complex-linear quadratic-form transformation. Calabi's *real* graph duality gives the corresponding catenoid/helicoid pair through a different, exact mechanism. The canonical Gudermannian and a complex half-period shift explain the elementary hyperbolic formulas. These are three related **but nonidentical** operations. Their global periods, singularities and induced signatures are indispensable.

**Source provenance:** Current main-branch reference SF-I-000, SF-I-010, SF-I-020 and provisional SF-DRAFT-010; uploaded historical ZIP symmetrical-framework-update-2026-11-18-bu.zip, including 00-meta/CLAIMS.md, 00-meta/NOTATION.md, 04-follow-ups/fundamental-forms-willmore-hopf.md (H421–H428), 04-follow-ups/riemann-marked-periods-gauss-manin-x04.md (H466–H479, H490, H503), 04-follow-ups/lame-complement-special-loci-riemann-master.md, foundational-paper-draft-v0.3.md and historical verification modules; independently checked external sources listed at the end. The ZIP records an older layout and is not the current main-branch structure.

**Evidence:** [K] classical established result; [D] direct derivation in this document; [V] independent exact symbolic verification; [H] archived claim with its own evidence scope; [O] unresolved or conditional. No novelty is presumed.

## 1. Canonical data, coordinates, and geometry types

Keep $`x>0`$, $`r>0`$, $`c>0`$, $`\mu>0`$, with the canonical logarithmic coordinate

```math
u=\ln(x/c),\qquad x=ce^u,\qquad \theta=ru,\qquad \zeta=u+iv.
```

The additional real coordinate $`v`$ and the complex coordinate $`\zeta`$ are choices needed to build a two-dimensional surface. Unless explicitly identified modulo $`2\pi/r`$, the complex parameter domain is simply connected.

Define the scalar fields and their logarithmic potential:

```math
S=\mathrm{sech}(ru),\qquad W=\tanh(ru),\qquad R=\cosh(ru),\qquad \kappa=\ln R.
```

Differentiation gives

```math
S_u=-rSW,\quad W_u=rS^2,\quad R_u=rRW,\quad S^2+W^2=1,\quad \kappa_u=rW,\quad \kappa_{uu}=r^2S^2.
```

The original symmetrical function with amplitude normalization is $`f_\mu=S/(2\sqrt{\mu}\,x)`$; its Master field is $`y=2xf_\mu=S/\sqrt{\mu}`$. The surface normalizations below use $`r`$ and the centered coordinate; the positive amplitude parameter $`\mu`$ remains separately tracked and does not enter their fixed normalized metrics.

Use the ambient bilinear forms

```math
\langle a,b\rangle_E=a_1b_1+a_2b_2+a_3b_3,\qquad \langle a,b\rangle_L=a_1b_1+a_2b_2-a_3b_3.
```

**Crucial distinction:** A Euclidean minimal surface has Riemannian *ambient* geometry. A Kobayashi maximal **spacelike** surface has Lorentzian ambient geometry but **Riemannian induced surface metric**. A timelike surface has an indefinite induced metric and requires another representation theory. “Pseudo-Riemannian” should be qualified by whether it refers to the ambient three-space or the two-dimensional surface.

## 2. Two holomorphic null representations [K,D]

Let $`\Sigma`$ be a simply connected Riemann surface with local coordinate $`\zeta`$. Let $`g`$ be meromorphic and $`\omega`$ holomorphic such that the following coordinate one-forms extend holomorphically and do not vanish simultaneously.

Fix the Euclidean Weierstrass-Enneper convention:

```math
\Phi_E=\left(\frac{1-g^2}{2},\frac{i(1+g^2)}{2},g\right)\omega.
```

**Proposition 2.1 [D].** This differential vector is Euclidean complex-null.

```math
\Phi_{E,1}^2+\Phi_{E,2}^2+\Phi_{E,3}^2=\left(\frac{(1-g^2)^2-(1+g^2)^2}{4}+g^2\right)\omega^2=0.
```

**Proof.** Expand the squares: $`(1-g^2)^2-(1+g^2)^2=-4g^2`$, which cancels the last term. The real part of a holomorphic integral $`X_E=\mathrm{Re}\int\Phi_E`$ has harmonic coordinates. Nullity implies conformality; when the metric is positive the immersion has mean curvature zero.

Its first fundamental form is

```math
I_E=\frac12\sum_{j=1}^3|\Phi_{E,j}|^2=\frac{(1+|g|^2)^2}{4}|\omega|^2.
```

**Theorem 2.2 [K,D] (compatible Kobayashi representation).** Let $`D=\mathrm{diag}(1,1,-i)`$ and define

```math
\Phi_L=D\Phi_E,\qquad X_L=\mathrm{Re}\int\Phi_L.
```

Then

```math
\Phi_{L,1}^2+\Phi_{L,2}^2-\Phi_{L,3}^2=\Phi_{E,1}^2+\Phi_{E,2}^2+\Phi_{E,3}^2=0.
```

The induced Lorentzian first form is

```math
I_L=\frac12\left(|\Phi_{L,1}|^2+|\Phi_{L,2}|^2-|\Phi_{L,3}|^2\right)=\frac{(1-|g|^2)^2}{4}|\omega|^2.
```

**Proof, step by step.**

1. The complex matrix satisfies $`D^T\mathrm{diag}(1,1,-1)D=I_3`$. Thus a Euclidean complex-null differential becomes Lorentzian complex-null.
2. The real part of the holomorphic integral remains harmonic in conformal coordinates; the Lorentz null condition makes it conformal.
3. Compute $`|\Phi_{L,1}|^2+|\Phi_{L,2}|^2-|\Phi_{L,3}|^2=\{(1+|g|^4)/2-|g|^2\}|\omega|^2=(1-|g|^2)^2|\omega|^2/2`$.
4. If $`\omega`$ is regular/nonzero and $`|g|\ne1`$, the metric is positive definite and the immersion is spacelike maximal, i.e. its mean curvature is zero.
5. Where $`|g|=1`$ the induced metric degenerates; this is **not** a regular spacelike immersion. On nonsimply-connected surfaces, new real-period constraints must be imposed.

The exact metric ratio is

```math
\frac{I_L}{I_E}=\left(\frac{1-|g|^2}{1+|g|^2}\right)^2.
```

This is a complexified quadratic-form construction, not a real ambient isometry or a universal physical Wick rotation. It is equivalent to a standard version of Kobayashi's 1983 maximal-surface representation after choosing signs and scaling.

## 3. Canonical catenoid–helicoid Weierstrass data [D,V,H424]

The canonical choice of holomorphic data is

```math
g(\zeta)=-e^{r\zeta},\qquad \omega=-e^{-r\zeta}\,d\zeta.
```

Substitute in the three Weierstrass components:

```math
\Phi_E=(\sinh(r\zeta),-i\cosh(r\zeta),1)\,d\zeta.
```

A holomorphic primitive is

```math
F_E(\zeta)=\left(\frac{\cosh(r\zeta)}r,-\frac{i\sinh(r\zeta)}r,\zeta\right).
```

The Euclidean catenoid and its conjugate helicoid are

```math
X_C=\mathrm{Re}F_E=\left(\frac{\cosh(ru)}r\cos(rv),\frac{\cosh(ru)}r\sin(rv),u\right).
```

```math
X_H=\mathrm{Im}F_E=\left(\frac{\sinh(ru)}r\sin(rv),-\frac{\sinh(ru)}r\cos(rv),v\right).
```

**Proof of isometry.** For either immersion, take the partial derivatives with respect to $`u,v`$. The squared lengths are $`\cosh^2(ru)`$, the cross term is zero. Consequently

```math
I_C=I_H=\cosh^2(ru)(du^2+dv^2),\qquad K_E=-r^2\mathrm{sech}^4(ru).
```

With the normal orientation determined by $`X_u\times X_v`$, the corresponding second fundamental forms are

```math
II_C=-r(du^2-dv^2),\qquad II_H=-2r\,du\,dv.
```

The associated family $`X_\alpha=\mathrm{Re}(e^{-i\alpha}F_E)`$ has the same first form and

```math
II_\alpha=-r\,\mathrm{Re}\left(e^{-i\alpha}(du+i\,dv)^2\right).
```

Its constant Hopf quadratic differential satisfies Codazzi. The Gauss equation reduces to $`\kappa_{uu}=r^2e^{-2\kappa}`$, the scalar identity already established in SF-DRAFT-010.

**Global period check.** Under $`\zeta\mapsto\zeta+2\pi i/r`$, only the third component of $`F_E`$ changes, by $`2\pi i/r`$. Thus

```math
X_\alpha(u,v+2\pi/r)-X_\alpha(u,v)=\left(0,0,\frac{2\pi\sin\alpha}{r}\right).
```

The catenoid closes on the angular cylinder. The helicoid generally does not close there; it lives on a universal cover or modulo a prescribed translation. Equality of local first forms does not solve the period problem.

## 4. The two Lorentzian maximal counterparts [D,V]

Apply $`D=\mathrm{diag}(1,1,-i)`$ to the Euclidean data. The resulting pair interchanges the geometric type “catenoid/helicoid”.

**Euclidean catenoid to Lorentzian helicoid.** From $`D\Phi_E`$, take the real primitive:

```math
Y_H=\mathrm{Re}\int D\Phi_E=\left(\frac{\cosh(ru)}r\cos(rv),\frac{\cosh(ru)}r\sin(rv),v\right).
```

It is locally the graph $`t=\arg(X+iY)/r`$ over the planar exterior $`\rho>1/r`$, after an angular branch is chosen.

**Euclidean helicoid to Lorentzian catenoid.** The Euclidean helicoid uses associated differential $`-i\Phi_E`$. Apply $`D`$:

```math
Y_C=\mathrm{Re}\int D(-i\Phi_E)=\left(\frac{\sinh(ru)}r\sin(rv),-\frac{\sinh(ru)}r\cos(rv),-u\right).
```

It is a rotational maximal graph on $`\rho=|\sinh(ru)|/r>0`$, on an appropriate branch.

**Exact metric verification.** For $`Y_H`$, the $`u`$-tangent is horizontal of squared norm $`\sinh^2(ru)`$; the $`v`$-tangent has squared horizontal norm $`\cosh^2(ru)`$ and time derivative $`1`$. Hence its Lorentz squared norm is $`\cosh^2(ru)-1=\sinh^2(ru)`$. For $`Y_C`$ the two squared Lorentz tangent lengths are also $`\sinh^2(ru)`$ and their mixed product is zero.

```math
I_{L,H}=I_{L,C}=\sinh^2(ru)(du^2+dv^2).
```

The Gaussian curvature follows directly from the conformal formula:

```math
K_L=-\sinh^{-2}(ru)\frac{d^2}{du^2}\ln|\sinh(ru)|=r^2\mathrm{csch}^4(ru)>0.
```

With a timelike unit normal, the Lorentz Gauss equation in flat ambient space reads $`K_L=-\det B`$. The mean curvature is zero and the principal curvatures are $`\pm r\,\mathrm{csch}^2(ru)`$, up to normal orientation.

**Critical domain restriction.** The Lorentzian induced metric degenerates at $`u=0`$, corresponding to $`|g|=1`$. A meridian has finite length to this locus:

```math
\int_0^\epsilon\sinh(ru)\,du=\frac{\cosh(r\epsilon)-1}{r}<\infty.
```

Thus the regular maximal branches are incomplete at that singular boundary. The Calabi-Bernstein global theorem says that complete spacelike maximal surfaces in flat Minkowski three-space are planes under its usual hypotheses; our nonplanar examples have no conflict with it.

The operations $`D`$ and associate-phase multiplication commute on **complex holomorphic forms**:

```math
D(e^{-i\alpha}\Phi_E)=e^{-i\alpha}D\Phi_E.
```

Their real immersions may have different periods and singular sets, so the commutation is an exact algebraic identity, not a global bijection of surface moduli.

## 5. Calabi's real minimal/maximal graph duality [K,D]

This is a **different** construction from the complex matrix $`D`$. Let $`\Omega\subset\mathbb R^2`$ be simply connected and $`f\in C^2(\Omega)`$ solve the Euclidean minimal graph equation. Define

```math
Q_f=\sqrt{1+f_x^2+f_y^2},\qquad \partial_x(f_x/Q_f)+\partial_y(f_y/Q_f)=0.
```

Set

```math
\beta_f=-\frac{f_y}{Q_f}\,dx+\frac{f_x}{Q_f}\,dy.
```

**Theorem 5.1 [K,D] (Calabi correspondence).** The graph equation is equivalent to $`d\beta_f=0`$, and hence $`\beta_f=dh`$ for some local function $`h`$ on a simply connected domain. The graph $`(x,y,h(x,y))`$ is spacelike maximal in Minkowski three-space. Conversely, every $`C^2`$ spacelike maximal graph determines a Euclidean minimal graph locally by the inverse rotated-gradient rule.

**Proof, step by step.**

1. Compute $`d\beta_f=[\partial_x(f_x/Q_f)+\partial_y(f_y/Q_f)]dx\wedge dy=0`$.
2. On a simply connected domain, exactness yields

```math
h_x=-f_y/Q_f,\qquad h_y=f_x/Q_f.
```

3. Then

```math
|\nabla h|^2=\frac{|\nabla f|^2}{1+|\nabla f|^2}<1,\qquad \sqrt{1-|\nabla h|^2}=\frac1{Q_f}.
```

4. Therefore the maximal graph equation simplifies to an equality of mixed derivatives:

```math
\partial_x\left(\frac{h_x}{\sqrt{1-|\nabla h|^2}}\right)+\partial_y\left(\frac{h_y}{\sqrt{1-|\nabla h|^2}}\right)=-f_{yx}+f_{xy}=0.
```

5. For the converse, start from spacelike maximal $`h`$ and define

```math
f_x=\frac{h_y}{\sqrt{1-|\nabla h|^2}},\qquad f_y=-\frac{h_x}{\sqrt{1-|\nabla h|^2}}.
```

The maximal equation ensures that this one-form is closed, and its primitive satisfies the minimal graph equation. All claims depend on the stated regularity and local topology.

This is a Hodge-star-type rotation of a normalized gradient on the *planar base*, not a direct replacement of a real coordinate by an imaginary one.

### 5.1 Catenoid sheet maps to Lorentzian helicoid

On an upper Euclidean catenoid sheet, with polar radius $`\rho>1/r`$,

```math
f(\rho)=r^{-1}\mathrm{arcosh}(r\rho),\qquad f_\rho=(r^2\rho^2-1)^{-1/2}.
```

The normalized radial derivative is

```math
f_\rho/\sqrt{1+f_\rho^2}=1/(r\rho).
```

Calabi rotation changes the radial derivative into an angular one:

```math
dh=d\varphi/r,\qquad h=\varphi/r+\mathrm{constant}.
```

This is the Lorentzian helicoid $`Y_H`$. Since $`\varphi`$ is multivalued on the entire annulus, its height is single-valued only on an angular cut or appropriate covering.

### 5.2 Euclidean helicoid maps to Lorentzian catenoid

The Euclidean helicoid is locally the graph $`f(\rho,\varphi)=\varphi/r`$ on a cut domain. Consequently $`|\nabla f|=1/(r\rho)`$ and the Calabi-rotated gradient is inward radial:

```math
h_\rho=-1/\sqrt{1+r^2\rho^2}.
```

Integrate:

```math
h(\rho)=-r^{-1}\mathrm{arsinh}(r\rho)+\mathrm{constant}.
```

This agrees with $`Y_C`$, where $`\rho=\sinh(ru)/r`$ on $`u>0`$ and $`h=-u`$.

Thus the two constructions—holomorphic null-data transformation and real closed-one-form Calabi duality—recover the **same canonical examples** with the chosen signs, but are not definitions of one another in all generality.

## 6. Gudermannian: the exact real chart joining the conformal factors [D,V]

For the canonical $`g=-e^{r\zeta}`$, the metric ratio in §2 is

```math
I_L/I_E=\left(\frac{1-e^{2ru}}{1+e^{2ru}}\right)^2=\tanh^2(ru)=W^2.
```

Let $`\eta=\mathrm{gd}(ru)`$, normalized by $`\eta(0)=0`$ and $`\eta_u=r\mathrm{sech}(ru)`$. Then

```math
\sin\eta=W,\qquad \cos\eta=S,\qquad \tan\eta=\sinh(ru).
```

In these variables,

```math
e^{h_E}=\cosh(ru)=\sec\eta,\qquad e^{h_L}=|\sinh(ru)|=|\tan\eta|,\qquad e^{h_L}/e^{h_E}=|\sin\eta|.
```

This is a **coordinate identity**, not a rule automatically changing the signature of a real ambient metric.

### 6.1 The Riccati inversion

Define the two logarithmic derivatives

```math
V_E=r^{-1}\partial_u\ln\cosh(ru)=\tanh(ru),\qquad V_L=r^{-1}\partial_u\ln|\sinh(ru)|=\coth(ru).
```

They obey

```math
(V_E)_u=r(1-V_E^2),\qquad (V_L)_u=r(1-V_L^2),\qquad V_EV_L=1.
```

The second Riccati equation is checked by differentiating $`V_L=1/V_E`$. The two conic identities are

```math
\tanh^2(ru)+\mathrm{sech}^2(ru)=1,\qquad \coth^2(ru)-\mathrm{csch}^2(ru)=1.
```

Thus the compact circle and noncompact hyperbola are explicit real forms of a complexified projective algebraic relationship.

### 6.2 Exact complex half-period continuation

For $`u\ne0`$, complexify $`u`$ and use the imaginary half-period $`i\pi/(2r)`$:

```math
\cosh(ru+i\pi/2)=i\sinh(ru),\qquad \tanh(ru+i\pi/2)=\coth(ru),\qquad \mathrm{sech}(ru+i\pi/2)=-i\,\mathrm{csch}(ru).
```

On $`u>0`$ with a consistent logarithm branch,

```math
\ln\cosh(ru+i\pi/2)=\ln\sinh(ru)+i\pi/2.
```

The map in the original multiplicative coordinate is $`x\mapsto xe^{i\pi/(2r)}`$, holding the real scale $`c`$ fixed; it is no longer a map of the positive real half-line into itself.

**Three distinct operations:** (a) $`D`$ on complex null data; (b) imaginary shift in logarithmic coordinate; (c) Calabi's real rotated-gradient duality. They have overlapping consequences for the canonical profile but are not universal synonyms for “Wick rotation”.

## 7. Signature-correct Gauss-Codazzi produces two quartic signs [D,V]

Extend SF-DRAFT-010 without changing its normalization. Prescribe a positive conformal factor $`z(u)>0`$ and a fixed trace-free second fundamental form:

```math
I=z^{-2}(du^2+dv^2),\qquad II_\alpha=r\{\cos\alpha(du^2-dv^2)-2\sin\alpha\,du\,dv\}.
```

The shape operator has trace zero and determinant

```math
\mathrm{tr}B=0,\qquad \det B=-r^2z^4.
```

The Gaussian curvature is

```math
K_I=zz_{uu}-z_u^2.
```

For Euclidean normal square $`+1`$, the Gauss equation is $`K_I=k_0+\det B`$. For a timelike unit normal of square $`-1`$ in Lorentzian ambient space it is $`K_I=k_0-\det B`$.

```math
K_I=k_0-r^2z^4\quad(\mathrm{Euclidean}),\qquad K_I=k_0+r^2z^4\quad(\mathrm{spacelike\ Lorentzian}).
```

Constant Hopf coefficient makes Codazzi automatic in this conformal ansatz.

**Theorem 7.1 [D] (the two first integrals).** Put $`\sigma=-1`$ in the Euclidean case and $`\sigma=+1`$ in the Lorentzian spacelike case. The common Gauss equation is

```math
zz_{uu}-z_u^2=k_0+\sigma r^2z^4.
```

On a nonconstant branch let $`H(z)=z_u^2`$. Since $`z_{uu}=H'(z)/2`$,

```math
\frac z2H'(z)-H(z)=k_0+\sigma r^2z^4,\qquad \frac d{dz}(H/z^2)=2k_0/z^3+2\sigma r^2z.
```

Integrating,

```math
z_u^2=C_0z^2+\sigma r^2z^4-k_0.
```

Differentiating away from turning points yields

```math
z_{uu}=C_0z+2\sigma r^2z^3.
```

The integration constant $`C_0`$ is **not fixed by Gauss-Codazzi alone**. Select the canonical $`C_0=r^2`$, and for flat ambient space $`k_0=0`$ obtain the two exact separatrix equations

```math
z_{E,u}^2=r^2(z_E^2-z_E^4),\qquad z_{E,uu}=r^2z_E-2r^2z_E^3,\qquad z_E=\mathrm{sech}(ru),
```

```math
z_{L,u}^2=r^2(z_L^2+z_L^4),\qquad z_{L,uu}=r^2z_L+2r^2z_L^3,\qquad z_L=\mathrm{csch}(ru)\quad(u>0).
```

The Euclidean equation is the cubic Master separatrix in normalized amplitude. The Lorentzian equation has the opposite cubic sign and a pole at the would-be symmetry center. It is **not** another globally finite-norm real Master solution.

For nonzero space-form curvature, fixing $`C_0=r^2`$ gives the normalized quartic $`z_u^2=r^2(z^2+\sigma z^4)-k_0`$. In the Euclidean case $`e=-k_0/r^2`$ is precisely the Master energy of SF-DRAFT-010. The Lorentzian family instead uses a positive quartic coefficient; a complex algebraic rotation does not by itself prove equivalence of the real period problems.

### 7.1 Unreduced surface PDEs

For $`I=e^{2h(u,v)}|d\zeta|^2`$ and constant Hopf coefficient of magnitude $`r/2`$, the two Gauss equations read

```math
\Delta_0h=-k_0e^{2h}+r^2e^{-2h}\quad(\mathrm{Euclidean}),\qquad \Delta_0h=-k_0e^{2h}-r^2e^{-2h}\quad(\mathrm{spacelike\ Lorentzian}).
```

Here $`\Delta_0=\partial_u^2+\partial_v^2`$. The one-variable equations are special reductions. A general two-variable solution, a nonconstant holomorphic Hopf differential, or a non-space-form ambient three-manifold requires additional geometry.

## 8. Levi-Civita and Kähler structures in both signatures [D,V]

Let $`h_E=\ln\cosh(ru)`$ and $`h_L=\ln|\sinh(ru)|`$. For consistently oriented orthonormal tangent coframes of $`e^{2h}(du^2+dv^2)`$, the Levi-Civita connection form may be written $`\omega_{12}=-h_u\,dv`$. Thus

```math
\omega_E=-r\tanh(ru)\,dv=-rW\,dv,\qquad \omega_L=-r\coth(ru)\,dv=-rW^{-1}dv.
```

Differentiating,

```math
d\omega_E=-r^2\mathrm{sech}^2(ru)\,du\wedge dv=K_E\,dA_E,\qquad d\omega_L=r^2\mathrm{csch}^2(ru)\,du\wedge dv=K_L\,dA_L.
```

The ambient moving-frame algebra is $`\mathfrak{so}(3)`$ in Euclidean space and $`\mathfrak{so}(2,1)`$ in Lorentz-Minkowski space. In both cases, the full adapted frame satisfies its Maurer-Cartan flatness equation in the flat ambient space, but the induced tangent Levi-Civita connection is generally curved.

**Two intrinsic Kähler potentials.** Both immersed surfaces, *including the Lorentzian ambient example because it is spacelike*, have an intrinsically Riemannian two-dimensional metric, compatible complex structure and a local Kähler potential. In the convention $`g=\mathcal K_{uu}|d\zeta|^2`$ for a potential depending only on $`u`$, set

```math
\mathcal K_E(u)=u^2/4+\cosh(2ru)/(8r^2),\qquad \mathcal K_L(u)=-u^2/4+\cosh(2ru)/(8r^2).
```

A direct second derivative gives

```math
(\mathcal K_E)_{uu}=\cosh^2(ru),\qquad (\mathcal K_L)_{uu}=\sinh^2(ru),\qquad \mathcal K_E-\mathcal K_L=u^2/2.
```

In particular,

```math
(\mathcal K_E)_{uu}-(\mathcal K_L)_{uu}=1.
```

This is an exact **chart-dependent difference of metric Hessians**, not a global Kähler-gauge equivalence: their metrics, curvatures and regular domains differ.

### 8.1 The spherical and hyperbolic Gauss targets

The Euclidean minimal Gauss map takes values in the round sphere $`S^2\simeq\mathbb{CP}^1`$:

```math
III_E=\frac{4|dg|^2}{(1+|g|^2)^2}=r^2\mathrm{sech}^2(ru)|d\zeta|^2=(-K_E)I_E.
```

The future timelike unit normal of a spacelike maximal surface takes values in hyperbolic space $`H^2`$, modeled by the unit disk on the $`|g|<1`$ chart:

```math
III_L=\frac{4|dg|^2}{(1-|g|^2)^2}=r^2\mathrm{csch}^2(ru)|d\zeta|^2=K_LI_L.
```

On the $`u>0`$ branch one uses the reciprocal disk chart $`g^{-1}`$ and accounts for orientation. The relevant Gauss-target Kähler potentials are

```math
\mathcal K_{S^2}=\ln(1+|g|^2),\qquad \mathcal K_{H^2}=-\ln(1-|g|^2)\quad(|g|<1).
```

**Do not confuse these target potentials with the induced surface potentials $`\mathcal K_E,\mathcal K_L`$.** The two target metrics have constant Gaussian curvature $`+1`$ and $`-1`$ respectively. The hyperbolic potential becomes singular at $`|g|=1`$.

Writing $`a_E=\cosh^2(ru)`$ and $`a_L=\sinh^2(ru)`$ for the induced metric coefficients and $`b_E=r^2\mathrm{sech}^2(ru)`$, $`b_L=r^2\mathrm{csch}^2(ru)`$ for the target Gauss metric coefficients, we obtain the paired identities

```math
a_Eb_E=r^2,\qquad a_Lb_L=r^2.
```

These are exact first/third fundamental-form reciprocal identities, not an assertion that the two surfaces are isometric.

## 9. Riemann minimal examples and the Lorentzian marked-period obstruction [H466–H469,D]

The uploaded archive contains substantially richer source material than merely an analogy with Riemann's minimal examples. It gives an explicit elliptic curve, Euclidean Weierstrass forms, marked periods and a Gauss-Manin system. We preserve that structure.

For $`\lambda>0`$ consider

```math
\mathcal E_\lambda:\quad w^2=P_\lambda(g),\qquad P_\lambda(g)=g(g-\lambda)(\lambda g+1).
```

With $`A>0`$, use the height differential $`dh=A\,dg/w`$ and archived Weierstrass forms

```math
\Phi_{E,1}=\frac A2(g^{-1}-g)\frac{dg}w,\qquad \Phi_{E,2}=\frac{iA}{2}(g^{-1}+g)\frac{dg}w,\qquad \Phi_{E,3}=A\frac{dg}w.
```

They are precisely the §2 convention after setting $`\omega=dh/g`$, and their complex Euclidean quadratic form vanishes.

### 9.1 The exact-coordinate primitive

Differentiate $`w/g`$ using $`w^2=P_\lambda(g)`$:

```math
d(w/g)=\frac{gP_\lambda'(g)-2P_\lambda(g)}{2g^2w}\,dg=\frac{\lambda}{2}(g+g^{-1})\frac{dg}w.
```

Hence

```math
\Phi_{E,2}=\frac{iA}{\lambda}\,d(w/g).
```

Thus this one-form has zero periods on cycles avoiding its poles, with the usual meromorphic interpretation. This is the archived H466 identity, now directly reproducible.

### 9.2 How the period conditions change

For a closed cycle $`\gamma`$ in the punctured elliptic curve, let

```math
\Pi_E(\gamma)=\oint_\gamma\Phi_E=(\Pi_1,\Pi_2,\Pi_3).
```

A Euclidean closed immersion requires $`\mathrm{Re}\Pi_E(\gamma)=0`$ for each relevant homology cycle, or a prescribed translation lattice in a singly periodic realization.

After $`D=\mathrm{diag}(1,1,-i)`$,

```math
\Pi_L=(\Pi_1,\Pi_2,-i\Pi_3),\qquad \mathrm{Re}\Pi_L=(\mathrm{Re}\Pi_1,\mathrm{Re}\Pi_2,\mathrm{Im}\Pi_3).
```

The Euclidean vertical condition $`\mathrm{Re}\Pi_3=0`$ is **not** the Lorentzian condition $`\mathrm{Im}\Pi_3=0`$. In the archive's normalization $`\Pi_3=A\oint_\gamma dg/w`$: the Lorentzian obstruction is a different real component of a marked elliptic period.

The archived H467–H469 calculations of $`\omega_\alpha,\omega_\beta`$, flux, Legendre's relation, Gauss-Manin and $`X_0(4)`$ can therefore be brought to bear, but they do **not** automatically solve the Lorentzian closure problem.

### 9.3 Spacelike components and singularity locus

The Lorentzian induced metric on the elliptic parameter curve is

```math
I_L=\frac{(1-|g|^2)^2}{4}\left|\frac{A\,dg}{g\,w}\right|^2.
```

Its regular spacelike locus excludes $`|g|=1`$ (unless a separate local cancellation/singularity analysis changes the chart). Because $`g`$ is meromorphic on the compact elliptic curve, a global smooth spacelike maximal immersion is not obtained by formal continuation alone. The branch-point, end, flux and monodromy data must be revisited.

**Proposed exact research tasks:** determine the topology of the preimage of $`|g|=1`$; compute $`\mathrm{Re}\Pi_L`$ in the archived marked homology basis; classify any surviving Lorentzian period lattices and singularities; and test any claims of a globally complete nonplanar maximal surface against Calabi-Bernstein. No global closure is claimed here.

## 10. Distinguish three “Wick” operations and the timelike case

The word “Wick rotation” can misleadingly collapse three mathematical operations:

- **Null-data complex transformation** $`D=\mathrm{diag}(1,1,-i)`$: changes the ambient complex bilinear null condition and is used before taking the real part of a holomorphic primitive. This is the clean Weierstrass–Kobayashi bridge.
- **Imaginary half-period shift** $`u\mapsto u+i\pi/(2r)`$: changes the scalar hyperbolic Riccati branch; it may encounter poles and is not a real diffeomorphism of $`x>0`$.
- **Real Calabi duality** $`dh=(-f_y\,dx+f_x\,dy)/\sqrt{1+|\nabla f|^2}`$: changes a real minimal graph to a real spacelike maximal graph, using a closed differential form. It does not require imaginary coordinates.

A literal replacement $`v\mapsto iv`$ changes the induced parameter signature. Timelike zero-mean-curvature surfaces have **Lorentzian induced metric** and are treated via real null coordinates or split-complex/para-complex versions of Weierstrass representation. They are **not** simply the spacelike maximal surfaces covered by Kobayashi's holomorphic construction.

The Schwartzians of the shared projective exponential also do not change automatically when one changes the target metric: the projective connection alone cannot determine the sign of the ambient or intrinsic curvature. The sphere/disk choice and its real structure supply that information.

## 11. Verification register and precise limitations

**Independent symbolic checks performed for this investigation:**

1. The canonical $`(g,\omega)`$ simplifies $`\Phi_E`$ to $`(\sinh(r\zeta),-i\cosh(r\zeta),1)d\zeta`$, and its complex Euclidean norm is zero.
2. The complex $`D`$ transformation makes the Minkowski complex quadratic form vanish.
3. The parametric $`Y_C`$ has Lorentzian first-form coefficients both $`\sinh^2(ru)`$, mixed coefficient zero, and a timelike unit normal away from $`u=0`$.
4. The Euclidean catenoid fundamental forms and the related Clifford-torus checks were independently verified while preparing SF-DRAFT-010.
5. Both normalized quartic integrals hold identically for $`z_E=\mathrm{sech}(ru)`$ and $`z_L=\mathrm{csch}(ru)`$.
6. The Gaussian curvatures and the Kähler-potential second derivatives simplify exactly, including $`\mathcal K_E-\mathcal K_L=u^2/2`$.
7. The Riemann differential identity for $`d(w/g)`$ is exact polynomial differentiation (also archived as H466).
8. The Calabi formulas are verified by differentiation and the minimal/maximal divergence equations; no numerical integration is needed for the rotational examples.

**Scope limitations:**

- A first-order null differential identity is not a theorem about regularity or global periods.
- Spacelike means a positive *induced* metric; the relevant ambient is Lorentzian.
- The manifold's nonzero second fundamental form and the signature of its unit normal must be tracked in the Gauss equation.
- The all-energy Master curvature result of SF-DRAFT-010 depends on a specified conformal and constant-Hopf ansatz and a separately fixed integration constant.
- The imaginary shift does not preserve the real $`x>0`$ coordinate domain.
- The Riemann-example global maximal-surface construction remains **open** here.
- Literature prior-art review for any claimed novelty has not been completed; the named representations and Calabi duality are classical.

## 12. Proposed consolidation and open problems

**Layer I candidates:** the logarithmic/exponential coordinate dictionary; exact Riccati inversion $`W\mapsto W^{-1}`$; Gudermannian identities; complex-null quadratic-form algebra; projective ratio and Schwarzian.

**Layer II candidates:** Euclidean/Lorentzian Gauss-Codazzi with unit-normal signature; the two Weierstrass constructions; Calabi graph correspondence; the canonical catenoid/helicoid and maximal partners; Gauss-map target $`S^2/H^2`$ and their Kähler metrics; Levi-Civita curvature; the regular/singular domain dictionary.

**Layer III deferred problems:** marked elliptic periods of Lorentzian Riemann partners; global monodromy/closing conditions; spectral and variational comparison of Euclidean minimal versus Lorentzian maximal surfaces; para-complex timelike branch.

**Open statements:**

1. [O] Classify the $`|g|=1`$ locus and maxface singularity type for the exact Riemann elliptic data, including punctures and branch points.
2. [O] Solve or delimit the new real-period equations $`\mathrm{Im}\oint A\,dg/w=0`$ in the marked basis, and decide if any nontrivial global Lorentzian Riemann surface closes.
3. [O] Extend the Euclidean/Lorentzian first-integral comparison from the separatrix to nonzero-energy elliptic trajectories with rigorous real-structure and branch hypotheses.
4. [O] Determine which other members of the general-$`q`$ hierarchy admit a two-dimensional minimal/maximal immersion with nonconstant Hopf differential or non-space-form ambient geometry; do not extrapolate outside the SF-DRAFT-010 ansatz.
5. [O] Treat timelike immersions via para-complex representation rather than via the spacelike Kobayashi formula.
6. [O] Establish prior-art equivalence and correct global moduli identifications before promoting new mathematical claims.

## 13. External literature and archive references

- O. Kobayashi, “Maximal surfaces in the 3-dimensional Minkowski space L3,” *Tokyo Journal of Mathematics* **6** (1983), 297–309. Primary source: https://ir.library.osaka-u.ac.jp/repo/ouka/all/26352/?lang=1 .
- E. Calabi, “Examples of Bernstein problems for some nonlinear equations,” *Proceedings of Symposia in Pure Mathematics* **15** (1970), 223–230. Historical source of the graph-duality construction.
- L. J. Alías and B. Palmer, “A duality result between the minimal surface equation and the maximal surface equation,” *Anais da Academia Brasileira de Ciências* (2001): https://www.scielo.br/j/aabc/a/VvtR8d5zC7wcdgBpvtLTXXf/?lang=en .
- M. Pember, “Weierstrass-type representations,” *Geometriae Dedicata* **204** (2020), 299–309; online 2019: https://link.springer.com/article/10.1007/s10711-019-00456-y . Places Euclidean/Lorentzian representations in a broader geometric transformation setting.
- “How many maximal surfaces do correspond to one minimal surface?”, *Mathematical Proceedings of the Cambridge Philosophical Society* **146** (2009), 165–175: https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/how-many-maximal-surfaces-do-correspond-to-one-minimal-surface/CF905F5D8CD8A3598C88AB76E8ACB9FD . Shows that correspondence classes and surface congruence require care.
- “Riemann Minimal Examples,” MathWorld: https://mathworld.wolfram.com/RiemannMinimalExamples.html . Background only; the explicit elliptic forms and marked-period formulas in §9 are taken from, and checked against, the uploaded ZIP.
- Current repository: [SF-I-020](../01-foundational/020%20The%20Linear%20Exponential%20Backbone.md), [SF-DRAFT-010](010%20Gauss-Codazzi%20Equations%20and%20Canonical%20Surface%20Geometry.md). Historical source registry: H421, H424, H466–H469, H473–H474, H490, H503.

**Concluding boundary:** The canonical $`S,W,R`$ fields make the Euclidean and spacelike Lorentzian representations unusually explicit. The precise correspondence is a network of holomorphic null-data transformations, signature-correct Gauss-Codazzi equations, real Calabi graph duality, and analytic Gudermannian/Riccati identities. It is not a proof of global equivalence, a complete classification of Riemann example maxfaces, or a universal mechanism generating every ODE/PDE/SDE.
