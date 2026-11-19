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
