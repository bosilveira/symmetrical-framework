---
id: SF-DRAFT-160
title: Marked Spectral Nodes, Weierstrass Periods, and SL–EP Geometry
status: provisional
created: 2026-11-19
proposed_layers: [I, II, III]
depends_on: [SF-I-020, SF-DRAFT-030, SF-DRAFT-040, SF-DRAFT-090, SF-DRAFT-100, SF-DRAFT-120, SF-DRAFT-130, SF-DRAFT-140, SF-DRAFT-150]
related_claims: [H100, H169, H172, H177, H183, H299, H391, H421, H424, H466, H467, H468, H469, H470, H471, H472]
---

# 160 Marked Spectral Nodes, Weierstrass Periods, and SL–EP Geometry

**Status:** Provisional mathematical investigation, not promoted into CLAIMS or foundational chapters. [D] proved here; [V] checked by symbolic/numerical computation; [K] classical theorem with hypotheses; [H] verified historical result with its original scope; [C] correction or obstruction; [O] open problem. No physical interpretation follows from an equality of differential equations alone.

**Research goal.** Continue the inverse spectral reconstruction of the existing draft 150 and the SL–EP/Lax–Novikov closure of drafts 130–140, testing whether the *marked differentials* of reflectionless spectral curves can be identified with catenoid, helicoid, and Riemann minimal-example Weierstrass data. Keep all independent variables, scales, periods, domains, and norming conventions visible.

**Principal findings.** The order-one nodal spectral curve has a rational normalization with two marked node preimages. A Möbius coordinate carries their **logarithmic dualizing differential** exactly to the catenoid height differential. Both horizontal Weierstrass forms have rational primitives; the height form alone has nonzero imaginary period, explaining catenoid closing and helicoid translational nonclosing. At arbitrary integer spectral depth there are several such node-pair channels, but they do not assemble automatically into one surface descending to the singular spectral curve. For the *different smooth genus-one curve* of the centered Pinney mechanical energy, the degree-two isogeny to the symmetric Riemann elliptic fiber (first established in draft 150) yields explicit pullbacks of **all** immersion forms, a degree-weighted Hodge norm identity and a finite beta-period integral. Riemann–Hurwitz obstructs a nonconstant algebraic map from the **rational spectral normalization** to the smooth Riemann elliptic curve. An elliptic modular or spectral coincidence alone is not period closing.

**Sources read.** Live GitHub drafts 130, 140, 150, the draft index and the November 18 repository ZIP, in particular the exact Riemann-period module in 04-follow-ups/riemann-marked-periods-gauss-manin-x04.md (H466–H470), the inverse scattering/marked curves modules and the Lax–Novikov identity register H100/H299. Independent external minimal-surface references are listed in the bibliography. Draft 150 presently contains its own provisional inverse-Marchenko and Pinney isogeny results; this draft extends but does not overwrite it.

## 1. Typed variables and explicit parameter changes

Fix the canonical original scales, function and logarithmic chart:

```math
r,c,\mu,x>0,\quad u=\ln(x/c),\quad x=ce^u,\quad S=\mathrm{sech}(ru),\quad W=\tanh(ru),\quad f_\mu(x;r,c)=\frac{S}{2\sqrt\mu\,x}.
```

For inverse scattering relative to a *declared* laboratory center $c_{\rm ref}>0$, write

```math
v_{\rm lab}=\ln(x/c_{\rm ref}),\quad u_0=\ln(c/c_{\rm ref}),\quad u=v_{\rm lab}-u_0.
```

An independent surface angle $v_{\rm ang}$ defines $\zeta=u+iv_{\rm ang}$; only on the catenoid is $v_{\rm ang}$ identified modulo $2\pi/r$. Do not confuse the laboratory coordinate $v_{\rm lab}$ with this angle.

Let $n$ be Pöschl–Teller well depth, $\kappa_j=jr$ the bound-state decay exponents, $k_{\rm sc}$ a real scattering wave number, $\Lambda=k_{\rm sc}^2$ the unshifted spectral energy, and $s$ the complex coordinate on the **normalization** of the spectral curve. The Riemann minimal-example family has distinct modulus $\lambda_R>0$, Gauss-coordinate $g_R$, and parameter $k_R=\lambda_R^{-1}-\lambda_R$; its immersion scale is $A_R>0$. The Pinney amplitude is $a(u)$, **not** $A_R$. The resolution $r$ and amplitude $\mu$ are independent of $\lambda_R$.

## 2. The inverse-scattering data determine a marked center only in a fixed laboratory chart [H,K,C]

For integer $n\ge1$ the translated real reflectionless well is

```math
V_{n,r,u_0}(v_{\rm lab})=-n(n+1)r^2\mathrm{sech}^2[r(v_{\rm lab}-u_0)].
```

Its transmission factor and bound poles are

```math
T_n(k_{\rm sc})=\prod_{j=1}^n\frac{k_{\rm sc}+ijr}{k_{\rm sc}-ijr},\quad \kappa_j=jr,\quad E_j=-j^2r^2.
```

Within the *declared* integer family, the pole locations determine $n$ and $r$, but not the translation $u_0$. Following the fixed right-tail convention of draft 150, let $\alpha_{n,j}$ be the positive squared tail normalization in the centered chart and $\beta_j$ the corresponding value in the laboratory chart:

```math
\alpha_{n,j}^2=\frac{rj(n+j)!}{(j!)^2(n-j)!},\quad \beta_j^2=\alpha_{n,j}^2e^{2jr u_0},\quad u_0=\frac1{2jr}\ln\frac{\beta_j^2}{\alpha_{n,j}^2},\quad c=c_{\rm ref}e^{u_0}.
```

All $j$ must give the same $u_0$. The Marchenko uniqueness theorem then characterizes the translated integer-well slice among real reflectionless potentials with the same discrete levels. Scattering by itself does **not** determine the original profile amplitude $\mu$, which enters only after the additional normalization

```math
\|f_\mu\|^2_{L^2(x\,dx)}=\frac1{2r\mu},\qquad \mu=\frac1{2r\|f_\mu\|^2_{L^2(x\,dx)}}.
```

**Distinction:** $c$ is a marking relative to $c_{\rm ref}$, not an intrinsic shape invariant of an unmarked complete catenoid. By contrast, the chosen geometric catenoid realization has neck radius $1/r$.

## 3. The nodal reflectionless spectral curve and its regular dualizing differentials [D,H,K]

For depth $n$ the archived Burchnall–Chaundy polynomial defines

```math
\mathcal C_n:\quad\nu^2=-\Lambda\prod_{j=1}^n(\Lambda+\kappa_j^2)^2,\qquad \kappa_j=jr.
```

Normalize it by the rational coordinate $s$:

```math
\Lambda=-s^2,\qquad \nu=s\prod_{j=1}^n(\kappa_j^2-s^2).
```

Each node $\Lambda=-\kappa_j^2$ has two preimages $s=\pm\kappa_j$. The normalization is $\mathbb P^1$ with geometric genus zero; the irreducible nodal curve has arithmetic genus $n$. For each marked pair, the logarithmic third-kind differential is

```math
\Omega_j=d\log\frac{s-\kappa_j}{s+\kappa_j}=\left(\frac1{s-\kappa_j}-\frac1{s+\kappa_j}\right)ds.
```

The residues $+1,-1$ at the paired preimages are exactly the opposite-residue condition for a regular section of the **dualizing sheaf of the nodal curve**. These are meromorphic differentials on the normalization, not holomorphic differentials on $\mathbb P^1$; the generalized Jacobian is $(\mathbb C^\times)^n$, not a smooth compact genus-$n$ Jacobian.

## 4. The order-one node becomes the catenoid's marked height differential [D,V]

At $n=1$, the curve and normalization are

```math
\nu^2=-\Lambda(\Lambda+r^2)^2,\qquad\Lambda=-s^2,\quad \nu=s(r^2-s^2).
```

Introduce an **exact Möbius coordinate** on its normalization:

```math
t=\frac{s-r}{s+r},\qquad s=r\frac{1+t}{1-t}.
```

Then $s=r$ and $s=-r$ map to $t=0,\infty$, and

```math
d\log t=\frac{ds}{s-r}-\frac{ds}{s+r}.
```

**Theorem 4.1 [D,V] (marked catenoid map).** On the twice-punctured normalization choose the meromorphic Weierstrass data

```math
g_C=-t,\qquad dh_C=\frac1r\,d\log t=\frac1r\left(\frac{ds}{s-r}-\frac{ds}{s+r}\right).
```

They are the standard Euclidean catenoid Gauss map and height form, with neck radius $1/r$. The height residues are

```math
\mathrm{Res}_{s=r}dh_C=1/r,\qquad \mathrm{Res}_{s=-r}dh_C=-1/r.
```

**Proof.** Möbius differentiation proves the differential identity. On the universal cover set $t=e^{r\zeta}$, $\zeta=u+iv_{\rm ang}$, so $dh_C=d\zeta$ and $g_C=-e^{r\zeta}$. The Weierstrass reconstruction in §5 integrates exactly to the scaled catenoid.

**Non-descent warning [C]:** The rational Gauss map $g_C=-t$ has limiting values $0$ and $\infty$ at the two normalization points **identified** to make the spectral node. It therefore does **not** descend as a morphism from the nodal spectral curve; the equality is on the **marked normalization**. The height differential does have the opposite-residue dualizing property at the node. These distinctions prevent a false global isomorphism claim.

## 5. Full catenoid Weierstrass one-forms and their exact period [D,V,K]

Use the fixed Weierstrass convention

```math
\boldsymbol\Phi_C=(\Phi_1,\Phi_2,\Phi_3)=\left(\frac12(g_C^{-1}-g_C),\frac i2(g_C^{-1}+g_C),1\right)dh_C,\qquad X_C=\mathrm{Re}\int\boldsymbol\Phi_C.
```

For $g_C=-t$ and $dh_C=dt/(rt)$, both horizontal forms have rational primitives:

```math
\Phi_1=d\frac{t+t^{-1}}{2r},\qquad\Phi_2=d\frac{-i(t-t^{-1})}{2r},\qquad\Phi_3=\frac{dt}{rt}.
```

Their nullity $\Phi_1^2+\Phi_2^2+\Phi_3^2=0$ is an algebraic identity. With $t=e^{r(u+iv_{\rm ang})}$ the real immersion and first fundamental form are

```math
X_C=\left(\frac{\cosh(ru)}r\cos(rv_{\rm ang}),\frac{\cosh(ru)}r\sin(rv_{\rm ang}),u\right),\quad I_C=\cosh^2(ru)(du^2+dv_{\rm ang}^2).
```

**Theorem 5.1 [D,V] (marked height period and flux).** For a positively oriented loop about $t=0$,

```math
\oint\boldsymbol\Phi_C=(0,0,2\pi i/r),\qquad\mathrm{Re}\oint\boldsymbol\Phi_C=0,\qquad\mathrm{Im}\oint\boldsymbol\Phi_C=(0,0,2\pi/r).
```

**Proof.** The first two forms are rational exact derivatives with zero residues; the third has residue $1/r$. The real period vanishes, so the immersion closes on the punctured plane, while the imaginary period is the vertical flux in the declared convention.

In the **specified** geometric realization, the inverse-spectral positive bound exponent $r$ therefore fixes both neck radius $1/r$ and vertical marked flux $2\pi/r$. This is an exact and nontrivial bridge between the normalized spectral node and minimal immersion periods, not merely a shared hyperbolic profile.

## 6. Helicoid associate: the SAME node, DIFFERENT real period [D,V,K]

The locally isometric Bonnet associate family multiplies all Weierstrass forms by $e^{i\delta}$:

```math
\boldsymbol\Phi_\delta=e^{i\delta}\boldsymbol\Phi_C,\qquad X_\delta=\mathrm{Re}\int\boldsymbol\Phi_\delta.
```

Its marked period is

```math
\oint\boldsymbol\Phi_\delta=(0,0,2\pi i e^{i\delta}/r).
```

Thus

```math
\mathrm{Re}\oint\boldsymbol\Phi_\delta=(0,0,-2\pi\sin\delta/r),\qquad\mathrm{Im}\oint\boldsymbol\Phi_\delta=(0,0,2\pi\cos\delta/r).
```

**Theorem 6.1 [D,V].** The associate immersion descends as a *single-valued Euclidean immersion on the same punctured-plane quotient* precisely when $\sin\delta=0$. At $\delta=0$ it gives the catenoid. At $\delta=\pi/2$ (helicoid) its real height period is $-2\pi/r$: the immersion is defined on the angular universal cover or in a specified quotient by vertical translation, but **not** as the same single-valued immersion on $\mathbb C^\times$.

The local Gauss map, induced metric and Jacobi expression alone do not detect this global obstruction. **Marked Weierstrass real periods do.**

## 7. Every spectral node defines its own catenoid residue channel [D,V,C]

For the depth-$n$ normalization of §3, select a **single** decay exponent $\kappa_j=jr$. Define

```math
t_j=\frac{s-\kappa_j}{s+\kappa_j},\qquad g_j=-t_j,\qquad dh_j=\frac1{\kappa_j}d\log t_j.
```

The identical Weierstrass calculation of §§4–6 produces a local catenoid channel, with

```math
\mathrm{neck\ radius}_j=\frac1{\kappa_j}=\frac1{jr},\qquad\oint dh_j=\frac{2\pi i}{jr},\qquad \mathrm{vertical\ flux}_j=\frac{2\pi}{jr}.
```

**Theorem 7.1 [D,V].** Each marked node pair defines a meromorphic third-kind height differential on the normalization whose residue and period scale is determined by its inverse-scattering decay exponent. The associated local minimal immersion is a catenoid on the twice-punctured normalization (or a helicoid on its angular universal cover).

**Limit of the construction [C].** For $n\ge2$ the chosen $t_j$ does *not* make the other node pairs simultaneously descend. Indeed for $\ell\ne j$,

```math
t_j(\kappa_\ell)=\frac{\kappa_\ell-\kappa_j}{\kappa_\ell+\kappa_j},\qquad t_j(-\kappa_\ell)=\frac{\kappa_\ell+\kappa_j}{\kappa_\ell-\kappa_j}=\frac1{t_j(\kappa_\ell)}.
```

The two values are generally different; at its own node, $t_j$ has the incompatible values $0,\infty$. Thus the Gauss map is rational on the **normalization**, but is not a globally well-defined function on the multiply nodal curve after the node identifications. There are $n$ individually marked **channels**, not a unique $n$-neck embedded minimal surface forced by the reflectionless spectral polynomial.

The node differential $\Omega_j$ remains a regular *dualizing* form at the selected node because its paired residues cancel. A full minimal immersion also needs the two horizontal forms, their residues and all real periods on the actual domain. A spectral-curve node is not itself a physical or geometric neck without this added Weierstrass data.

## 8. A no-go theorem: the nodal spectral curve cannot map nontrivially to a smooth elliptic Riemann fiber [D,K,C]

Let $E$ be any smooth complex elliptic curve, including any nonsingular fiber of the archived Riemann family. The normalization of the reflectionless curve $\mathcal C_n$ is $\mathbb P^1$.

**Theorem 8.1 [D,K] (Riemann–Hurwitz obstruction).** Every holomorphic map $F:\mathbb P^1\to E$ is constant. Therefore every morphism $\mathcal C_n\to E$ is constant as well.

**Proof.** If $F$ were nonconstant of degree $d>0$, Riemann–Hurwitz would give

```math
2g(\mathbb P^1)-2=d(2g(E)-2)+\deg\mathrm{Ram}(F),\qquad -2=0+\deg\mathrm{Ram}(F).
```

The right-hand side is nonnegative, a contradiction. Any morphism from the irreducible nodal curve to $E$ composed with its surjective normalization would yield such a map, so it too must be constant.

**What this does NOT forbid.** It does not prohibit an algebraic **correspondence**, a map from a positive-genus *cover*, a singular degeneration of a family of smooth curves, an isogeny involving a **different** elliptic curve such as the Pinney mechanical energy curve, or a mapping of meromorphic forms on a punctured rational normalization to meromorphic catenoid data. The no-go result is specifically against the unqualified direct spectral-nodal-to-smooth-elliptic **morphism** claim.

This algebraic obstruction explains why the *spectral* completion and the *Riemann elliptic surface* period completion are not automatically the same global space, even though they are connected by a common local SL–EP/symmetric-square formalism.

## 9. The OTHER curve: centered Pinney mechanical energy is smooth elliptic [H,D,V]

The positive canonical Pinney amplitude solves

```math
a_{uu}=\frac{r^2}{4}a+\frac{\mu r^2}{4a^3},\qquad a^2=\sqrt\mu\cosh(ru).
```

Its **centered zero-energy mechanical curve** is the smooth quartic

```math
\mathcal P_{r,\mu}:\quad Y^2=\frac{r^2}{4}(a^4-\mu),\qquad Y=a\,a_u,\qquad j(\mathcal P_{r,\mu})=1728.
```

This is an elliptic *energy curve* of the Pinney envelope, **not** the nodal reflectionless spectral curve $\mathcal C_n$. The quartic has two points over infinity in its smooth projective compactification and the holomorphic one-form

```math
\omega_{\mathcal P}=\frac{da}{Y}.
```

The Riemann-minimal-example family from the actual historical ZIP is

```math
w_R^2=g_R(g_R-\lambda_R)(\lambda_Rg_R+1),\quad\lambda_R>0,\qquad y_R=\frac{w_R}{\sqrt{\lambda_R}},\quad k_R=\lambda_R^{-1}-\lambda_R.
```

In its normalized cubic chart

```math
E_{k_R}:\quad y_R^2=g_R^3+k_Rg_R^2-g_R,\qquad j_R(k_R)=256\frac{(k_R^2+3)^3}{k_R^2+4}.
```

At the real **symmetric modulus** $\lambda_R=1$ (so $k_R=0$), this becomes

```math
E_0:\quad y_R^2=g_R^3-g_R,\qquad j_R(0)=1728.
```

Draft 150 proves the following explicit *degree-two isogeny between two smooth elliptic curves*, distinct from the spectral normalization map:

```math
\Phi:\mathcal P_{r,\mu}\longrightarrow E_0,\qquad g_R=\frac{a^2}{\sqrt\mu},\qquad y_R=\frac{2aY}{r\mu^{3/4}}.
```

Indeed,

```math
y_R^2=\frac{a^2(a^4-\mu)}{\mu^{3/2}}=g_R^3-g_R,\qquad \Phi^*\left(\frac{dg_R}{y_R}\right)=r\mu^{1/4}\frac{da}{Y}.
```

This formula defines a degree-two unramified morphism on smooth complex projective compactifications; after choosing elliptic origins it is a 2-isogeny. Its deck involution is $(a,Y)\mapsto(-a,-Y)$. The quartic's *different* involution $(a,Y)\mapsto(-a,Y)$ yields the genus-zero quotient for the **Pinney time differential** $a\,da/Y$.

## 10. Explicit pullback of ALL symmetric Riemann immersion forms [D,V,H466]

The historical Riemann Weierstrass data, in its convention, are

```math
\boldsymbol\Phi_R=(\Phi_{R1},\Phi_{R2},\Phi_{R3})=\left(\frac{A_R}{2}(g_R^{-1}-g_R),\frac{iA_R}{2}(g_R^{-1}+g_R),A_R\right)\frac{dg_R}{w_R}.
```

At $\lambda_R=1$ one has $w_R=y_R$ and $A_R>0$. For the isogeny $\Phi$ of §9, direct substitution gives the three **exact pullback forms**

```math
\Phi^*\Phi_{R1}=\frac{A_Rr}{2}\left(\frac{\mu^{3/4}}{a^2}-\frac{a^2}{\mu^{1/4}}\right)\frac{da}{Y}.
```

```math
\Phi^*\Phi_{R2}=\frac{iA_Rr}{2}\left(\frac{\mu^{3/4}}{a^2}+\frac{a^2}{\mu^{1/4}}\right)\frac{da}{Y}.
```

```math
\Phi^*\Phi_{R3}=A_Rr\mu^{1/4}\frac{da}{Y}.
```

**Theorem 10.1 [D,V].** The centered Pinney-to-Riemann isogeny transports the **entire meromorphic Weierstrass triple** by the displayed formulas, not merely the elliptic $j$-invariant or a single holomorphic period. These are equalities of meromorphic 1-forms on the corresponding punctured projective curves, and preserve their full periods under the induced homology map; they do not automatically solve all real immersion-period closing conditions.

**Proof.** Differentiate $g_R=a^2/\sqrt\mu$ and insert the formula for $y_R$:

```math
\Phi^*(dg_R/y_R)=r\mu^{1/4}da/Y,\quad \Phi^*(g_R\,dg_R/y_R)=r\mu^{-1/4}a^2da/Y.
```

```math
\Phi^*(g_R^{-1}dg_R/y_R)=r\mu^{3/4}a^{-2}da/Y.
```

Taking the appropriate linear combinations proves the three claims.

### 10.1 The exact-differential reduction is preserved

For $E_0:y_R^2=g_R^3-g_R$, direct differentiation gives the archival relation

```math
d(y_R/g_R)=\frac12(g_R+g_R^{-1})\frac{dg_R}{y_R}.
```

Therefore

```math
\Phi_{R2}=iA_R\,d(y_R/g_R)
```

is exact meromorphic, and

```math
\Phi_{R1}=A_R\,d(y_R/g_R)-A_R\,g_R\,dg_R/y_R,\qquad \Phi_{R3}=A_R\,dg_R/y_R.
```

Only the two marked periods of $\omega_R=dg_R/y_R$ and $\eta_R=g_Rdg_R/y_R$ contribute to the closed-cycle immersion periods:

```math
\oint_\gamma\boldsymbol\Phi_R=A_R\left(-N_\gamma,\,0,\,\Omega_\gamma\right),\quad \Omega_\gamma=\oint_\gamma\omega_R,\quad N_\gamma=\oint_\gamma\eta_R.
```

This formula holds on cycles avoiding the punctures; the exact derivative has no closed periods. The pullback makes the two relevant Pinney quartic differentials *explicit*, but a real-period closing test still needs a chosen homology basis, the real slice and the immersion translation lattice.

## 11. Marked homology and an exact Hodge-metric glue for the two smooth elliptic curves [D,V,K]

Let $\omega_{\mathcal P}=da/Y$ on the smooth Pinney quartic, and $\omega_R=dg_R/y_R$ on $E_0$. The isogeny has degree two and satisfies

```math
\Phi^*\omega_R=q\,\omega_{\mathcal P},\qquad q=r\mu^{1/4}.
```

For any holomorphic one-form $\omega$ on a smooth compact complex curve, define the positive Hodge pairing

```math
\|\omega\|_{\mathrm{Hodge}}^2=\frac i2\int_E\omega\wedge\overline\omega.
```

**Theorem 11.1 [D,V] (degree-weighted Hodge isometry formula).**

```math
r^2\sqrt\mu\,\|\omega_{\mathcal P}\|_{\mathrm{Hodge}}^2=2\|\omega_R\|_{\mathrm{Hodge}}^2.
```

**Proof.** Pullback and complex conjugation commute, so

```math
\int_{\mathcal P}\Phi^*(\omega_R\wedge\overline{\omega_R})=q\bar q\int_{\mathcal P}\omega_{\mathcal P}\wedge\overline{\omega_{\mathcal P}}.
```

Because $\Phi$ is an unramified degree-two map between compact oriented surfaces, the left integral is twice the corresponding integral over $E_0$. This yields the displayed identity with $|q|^2=r^2\sqrt\mu$.

**This is a literal geometric metric identity, not a scalar coincidence of numerical norms.** It joins the Hodge $L^2$ spaces of *two smooth elliptic curves* through an explicitly given degree-two map. It is **not** yet an isometry from the original weighted scalar Sturm–Liouville Hilbert space $L^2((0,\infty),x\,dx)$ to either compact Hodge space; that additional functional-analytic intertwiner has not been constructed.

### 11.1 The homology marking has index two

Choose integer symplectic cycle bases $\delta_1,\delta_2$ for the Pinney quartic and $\gamma_1,\gamma_2$ for $E_0$. For some integer matrix $M$,

```math
\Phi_*\binom{\delta_1}{\delta_2}=M\binom{\gamma_1}{\gamma_2},\qquad |\det M|=2.
```

The periods obey

```math
q\binom{\oint_{\delta_1}\omega_{\mathcal P}}{\oint_{\delta_2}\omega_{\mathcal P}}=M\binom{\oint_{\gamma_1}\omega_R}{\oint_{\gamma_2}\omega_R}.
```

The determinant-two constraint follows because a degree-two unramified covering identifies a sublattice of index two in $H_1(E_0,\mathbb Z)$. **The specific entries of $M$ require a cycle marking**, not merely an affine equation or equality of $j$ values. A numerical or symbolic period comparison that omits $M$ is insufficient to claim an immersion-period correspondence.

## 12. The canonical positive Pinney trajectory parametrizes a real Riemann elliptic arc [D,V]

On the positive real centered Pinney orbit,

```math
a(u)=\mu^{1/4}\sqrt{\cosh(ru)},\qquad Y(u)=a a_u=\frac{r\sqrt\mu}{2}\sinh(ru).
```

Under the isogeny of §9, these give the remarkably simple real Riemann-curve coordinates

```math
g_R(u)=\cosh(ru),\qquad y_R(u)=\sqrt{\cosh(ru)}\sinh(ru).
```

They satisfy $y_R^2=g_R^3-g_R$ identically. For $u>0$ the branch has $g_R\ge1$, $y_R\ge0$; the sign of $y_R$ reverses on $u<0$. At the turning point $u=0$, $g_R=1$ and $y_R=0$.

**Theorem 12.1 [D,V] (exact holomorphic period density).** Along this real arc, the Riemann holomorphic differential is

```math
\frac{dg_R}{y_R}=\frac{r\,du}{\sqrt{\cosh(ru)}}.
```

**Proof.** Differentiate $g_R=\cosh(ru)$ and divide by $y_R=\sinh(ru)\sqrt{\cosh(ru)}$ for $u>0$. At the endpoint the expression extends regularly in a local square-root uniformizer.

The interval $u\in[0,\infty)$ maps to the elliptic arc $g_R\in[1,\infty)$, and its integral is **finite**:

```math
\int_1^\infty\frac{dg_R}{\sqrt{g_R^3-g_R}}=\int_0^\infty\frac{r\,du}{\sqrt{\cosh(ru)}}=\frac12B\left(\frac14,\frac12\right).
```

Substitute $t=ru$, then $z=\tanh t$ and $w=z^2$ to obtain the beta integral; it is independent of $r$ and $\mu$ because the elliptic fiber itself was normalized.

Numerically, the value of the open arc is

```math
\frac12B(1/4,1/2)=2.62205755429211981046\ldots.
```

The archived real Riemann period at $\lambda_R=1$ is $\Omega_\beta=4K(1/2)/\sqrt2=B(1/4,1/2)$, **twice** this arc integral with the compatible standard cycle orientation.

### 12.1 What the height forms actually do at the ends

The Riemann vertical height differential pulls back to

```math
\Phi^*\Phi_{R3}=A_R\frac{r\,du}{\sqrt{\cosh(ru)}}.
```

Along the real arc from the branch point to the planar end, its real height increment is finite:

```math
\Delta X_{R3}= \frac{A_R}{2}B(1/4,1/2).
```

The catenoid height form along its real meridian is instead $dh_C=du$, giving an **infinite** height interval as $u\to+\infty$. Therefore the exact Pinney-to-Riemann elliptic *curve map* does **not** identify the catenoid and Riemann minimal surfaces as isometric immersions. In particular, the parameter $u$ is **not** an affine/arc-length parameter for the elliptic differential: the density $r/\sqrt{\cosh(ru)}$ matters.

The second-kind form $g_R\,dg_R/y_R$ behaves along this open arc as $r\sqrt{\cosh(ru)}\,du$ and its primitive diverges at the planar end. That is compatible with horizontal planar-end behavior and explains why comparing only the finite holomorphic period would omit immersion data.

## 13. The unique real j=1728 fiber, and a precise boundary on the isogeny claim [D,V,C]

For $k_R\in\mathbb R$ the Riemann $j$ invariant satisfies the exact identity

```math
j_R(k_R)-1728=\frac{64k_R^2(2k_R^2+9)^2}{k_R^2+4}.
```

**Theorem 13.1 [D,V].** On the **real** Riemann modulus line, $j_R(k_R)=1728$ if and only if $k_R=0$, equivalently $\lambda_R=1$.

**Proof.** Factor the numerator as shown. For real $k_R$, the denominator and the factor $(2k_R^2+9)^2$ are strictly positive, so the right-hand side vanishes exactly at zero. Solve $\lambda_R^{-1}-\lambda_R=0$ for $\lambda_R>0$.

The centered Pinney mechanical curve remains $j=1728$ for all $r,\mu>0$, so merely varying $r$ or $\mu$ **cannot** reproduce the full real nonconstant $j_R(k_R)$ family by the same direct curve identification. The explicitly derived degree-two formulas in §9 land on the *symmetric* fiber only.

**Qualification:** This does *not* rule out other isogenies between the fixed $j=1728$ curve and isolated nonsymmetric Riemann fibers (complex multiplication isogeny classes contain curves with different $j$ values). It rules out claiming that the **same explicit marked degree-two formula** automatically identifies every Riemann fiber, and shows that equality of $j$ values on the real family is isolated.

### 13.1 Complex multiplication weights distinguish the two marked forms

On the symmetric elliptic curve $E_0:y_R^2=g_R^3-g_R$, the automorphism

```math
\rho(g_R,y_R)=(-g_R,i y_R)
```

has order four. Its action on the two marked differential types is

```math
\rho^*(dg_R/y_R)=i\,dg_R/y_R,\qquad \rho^*(g_R\,dg_R/y_R)=-i\,g_R\,dg_R/y_R.
```

**Proof.** Substitute $g_R\mapsto-g_R$, $y_R\mapsto i y_R$ and differentiate. The two differential types belong to *opposite* $i$-eigenspaces of this automorphism. The holomorphic period and the meromorphic horizontal/flux period are therefore **not interchangeable** even at the symmetric complex-multiplication point.

This provides an additional invariant check on any proposed surface-period-preserving map: matching $dg_R/y_R$ does not automatically match the independent meromorphic differential $g_R\,dg_R/y_R$ or its real period-closing conditions.

## 14. The archived Gauss–Manin system is a second SL/projective mechanism, with a DIFFERENT independent variable [H,K,D]

For the complete Riemann family, the historical source derives the marked periods

```math
\Omega(k_R)=\oint\frac{dg_R}{y_R},\qquad N(k_R)=\oint\frac{g_R\,dg_R}{y_R}.
```

Their Gauss–Manin evolution in the *modulus* $k_R$ is

```math
\frac{d}{dk_R}\binom{\Omega}{N}=\frac1{k_R^2+4}\begin{pmatrix}-k_R/2&-1\\-1&k_R/2\end{pmatrix}\binom{\Omega}{N}.
```

The holomorphic period satisfies the scalar Picard–Fuchs ODE

```math
(k_R^2+4)\Omega_{k_Rk_R}+2k_R\Omega_{k_R}+\frac14\Omega=0.
```

This is a traceless $2\times2$ first-order carrier, just as the SL–Riccati linear system is traceless. It has its own projectivization and Schwarzian:

```math
\left\{\frac{\Omega_1}{\Omega_2},k_R\right\}=\frac{k_R^2-12}{2(k_R^2+4)^2}.
```

**Dictionary boundary:** The *independent variable* here is $k_R$, moving across different elliptic fibers, while the scattering SL/EP carrier evolves in $u=\ln(x/c)$ along one differential equation. The entries $(\Omega,N)$ are marked *periods*, while $(\phi,\phi_u)$ are a function and its spatial derivative. Their matrix Lie algebra and projective constructions can be formally compared, but neither the chosen parameter nor the Hilbert space, polarization, period lattice or monodromy should be identified without an actual gauge/reparametrization intertwiner.

### 14.1 Determinant conservation is common; its meaning differs

The Gauss–Manin matrix has trace zero, so the determinant of any fundamental period matrix is constant. The archived symplectic period determinant is

```math
\Omega_\alpha N_\beta-\Omega_\beta N_\alpha=-8\pi i.
```

In a real SL carrier, the conserved Wronskian is likewise a determinant. In EP the square of that Wronskian multiplies the Gram determinant to yield the Pinney strength. Those facts are **structurally analogous and algebraically exact**, but the *objects whose determinants are preserved* are different. The fixed $-8\pi i$ comes from the Riemann family and its marked cycles, not from the original $L^2(xdx)$ norm or a universal Pinney constant.
