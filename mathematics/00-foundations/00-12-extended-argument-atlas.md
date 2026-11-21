# 00.12 — Extended argument atlas: product logarithms, reciprocal charts and Wick continuation

**Status:** verified local coordinate calculations and pullback identities for *selected composed fields*. This is a companion to [§00.11](00-11-elementary-function-web.md), not a replacement of the canonical variable $`u=\log(x/c)`$ or of the Master Classification Theorem. The twelve paired functions may be evaluated at many arguments, but distinct formulas do **not** automatically provide different global solution spaces or new underlying geometric dimensions.

## 1. Domain and the required reference scale

Fix the real parameter domain $`x,c,r>0`$. To discuss the **product of two quantities with dimensions of length**, introduce a *fixed* positive reference length $`\ell>0`$, held fixed unless explicitly varied. Define the two logarithmic coordinates

```math
u=\log(x/c),\qquad v=\log(xc/\ell^2)=u+2\log(c/\ell),\qquad \theta_-=ru,\qquad \theta_+=rv.
```

Both $`u`$ and $`v`$ are dimensionless. The formal expression $`\log(xc)`$ is meaningful without a new reference only if $`x,c`$ were already dimensionless. Setting $`\ell=c`$ **while varying $`c`$** would simply reduce the product coordinate to $`u`$, so it is not an independent product-family definition.

Set $`c^\vee=\ell^2/c`$. The exact center-reflection identity is

```math
v=\log(x/c^\vee),\qquad c^\vee=\ell^2/c,\qquad (c^\vee)^\vee=c,\qquad \log(c^\vee/\ell)=-\log(c/\ell).
```

Consequently, for every function $`F`$ defined on the specified real argument range, $`F(r\log(xc/\ell^2))=F(r\log(x/c^\vee))`$. This is an **existing log-profile family with a transformed center**. It is not an independent oscillator classification. If $`\ell`$ is also varied, it becomes a fourth independent parameter and contributes $`-2r\,d\ell/\ell`$ to $`d\theta_+`$.

## 2. The chart count is not finite

The existing four-row table records a *preferred chain*, not four exhaustive charts. On appropriate domains, the following give valid coordinates of the same **three-dimensional manifold** $`(x,c,r)`$ when paired with retained $`c,r`$ (and fixed $`\ell`$ where used).

| Chart coordinate $`z`$ | Inverse for $`x`$ | Range / branch | $`\partial_x z`$ at fixed other parameters |
|---|---|---|---|
| $`u=\log(x/c)`$ | $`ce^u`$ | $`u\in\mathbb R`$ | $`1/x`$ |
| $`\theta=ru`$ | $`ce^{\theta/r}`$ | $`\theta\in\mathbb R`$ | $`r/x`$ |
| $`T=e^\theta`$ | $`cT^{1/r}`$ | $`T>0`$ | $`rT/x`$ |
| $`\eta=\mathrm{gd}\theta`$ | $`c\exp[\mathrm{arsinh}(\tan\eta)/r]`$ | $`-\pi/2<\eta<\pi/2`$ | $`rS/x`$ |
| $`t=\tanh(\theta/2)`$ | $`c[(1+t)/(1-t)]^{1/r}`$ | $`-1<t<1`$ | $`r(1-t^2)/(2x)`$ |
| $`W=\tanh\theta`$ | $`c\exp[\mathrm{arctanh}(W)/r]`$ | $`-1<W<1`$ | $`r(1-W^2)/x`$ |
| $`P=(1+W)/2`$ | $`c[P/(1-P)]^{1/(2r)}`$ | $`0<P<1`$ | $`2rP(1-P)/x`$ |
| $`b=\sinh\theta`$ | $`c\exp[\mathrm{arsinh}(b)/r]`$ | $`b\in\mathbb R`$ | $`rR/x`$ |
| $`v=\log(xc/\ell^2)`$ | $`\ell^2e^v/c`$ | $`v\in\mathbb R`$ | $`1/x`$ |
| $`\theta_+=rv`$ | $`\ell^2e^{\theta_+/r}/c`$ | $`\theta_+\in\mathbb R`$ | $`r/x`$ |
| $`z_1=r/u`$ | $`c\exp(r/z_1)`$ | two branches $`u\ne0`$ | $`-r/(xu^2)`$ |
| $`z_2=1/(ru)`$ | $`c\exp[1/(r^2z_2)]`$ | two branches $`u\ne0`$ | $`-1/(rxu^2)`$ |

Here $`R=\cosh\theta>0`$ and $`S=\mathrm{sech}\theta>0`$ are **argument fields**, not new independent parameters. Neither $`S`$ nor $`R`$ is globally an injective real chart because both are even in $`\theta`$; each can be used only with a sign sheet or on one half-line. The complex phase $`S+iW=e^{i\eta}`$ embeds the same one-dimensional circle arc but is not by itself an additional complex dimension.

### 2.1. Full active-parameter differentials for the six motivating arguments

With $`\ell`$ fixed, all derivatives in the table are partials in **$`(x,c,r)`$**, holding the other two members fixed.

| Argument $`z(x,c,r)`$ | $`z_x`$ | $`z_c`$ | $`z_r`$ | Excluded center |
|---|---|---|---|---|
| $`ru`$ | $`r/x`$ | $`-r/c`$ | $`u`$ | none |
| $`rv`$ | $`r/x`$ | $`r/c`$ | $`v`$ | none |
| $`r/u`$ | $`-r/(xu^2)`$ | $`r/(cu^2)`$ | $`1/u`$ | $`x=c`$ |
| $`1/(ru)`$ | $`-1/(rxu^2)`$ | $`1/(rcu^2)`$ | $`-1/(r^2u)`$ | $`x=c`$ |
| $`r/v`$ | $`-r/(xv^2)`$ | $`-r/(cv^2)`$ | $`1/v`$ | $`x=\ell^2/c`$ |
| $`1/(rv)`$ | $`-1/(rxv^2)`$ | $`-1/(rcv^2)`$ | $`-1/(r^2v)`$ | $`x=\ell^2/c`$ |

Notice that $`r/u=r^2/(ru)`$: at **fixed $`r`$** the first reciprocal argument is a scaled inverse of $`\theta=ru`$, but when **$`r`$ varies** it is different from $`1/(ru)`$. The two reciprocal product arguments obey the analogous distinction. An extension in which $`\ell`$ varies also requires its own $`z_\ell`$.

## 3. A universal second-order pullback, independent of the chosen function

Let $`z=z(x;c,r,\ell)`$ be $`C^2`$ on an open interval where $`z_x\ne0`$. A selected scalar profile $`Y(x)=F(z(x))`$ has

```math
Y_x=F_z z_x,\qquad Y_{xx}=F_{zz}z_x^2+F_z z_{xx}.
```

Thus the **general pullback theorem** is

```math
Y_{xx}-\frac{z_{xx}}{z_x}Y_x=z_x^2F_{zz}.
```

In particular, for the sech profile $`F(z)=\mathrm{sech}z`$, satisfying $`F_{zz}=F-2F^3`$, one obtains

```math
Y_{xx}-\frac{z_{xx}}{z_x}Y_x=z_x^2(Y-2Y^3).
```

The same calculation applied to the nonvanishing cosh field $`R_z=\cosh z`$ yields the *pulled-back logarithmic derivative*. Writing $`q(x)=\partial_x\log\cosh(z(x))=z_x\tanh z`$,

```math
q_x+q^2-\frac{z_{xx}}{z_x}q=z_x^2.
```

For the canonical argument $`z=r\log(x/c)`$, $`z_x=r/x`$ and $`z_{xx}/z_x=-1/x`$, so the selected sech satisfies

```math
x^2Y_{xx}+xY_x=r^2(Y-2Y^3).
```

For the reciprocal argument $`z=r/u`$ on $`u\ne0`$, $`z_u=-r/u^2`$ and $`z_{uu}/z_u=-2/u`$. Thus the **same composed sech field** satisfies

```math
Y_{uu}+\frac2uY_u=\frac{r^2}{u^4}(Y-2Y^3).
```

In the original positive spatial coordinate this reads

```math
Y_{xx}+\frac{u+2}{xu}Y_x=\frac{r^2}{x^2u^4}(Y-2Y^3),\qquad u=\log(x/c)\ne0.
```

The operator $`\partial_u^2+2u^{-1}\partial_u`$ is formally radial in three dimensions, **but the potential/nonlinearity has acquired a nonconstant weight**. This is a chain-rule reduction, not a theorem reconstructing a three-dimensional geometry or an identification with the constant-coefficient Master ODE.

## 4. The unexpected common Schwarzian

For $`z_x\ne0`$ define the one-dimensional Schwarzian derivative

```math
\{z,x\}=\frac{z_{xxx}}{z_x}-\frac32\left(\frac{z_{xx}}{z_x}\right)^2.
```

Every one of the six real arguments in §2.1 is an affine or fractional-linear function of either $`u=\log(x/c)`$ or $`v=\log(xc/\ell^2)`$ when $`c,r,\ell`$ are fixed. The Schwarzian chain rule and the fractional-linear invariance yield

```math
\{M\circ u,x\}=\{u,x\}=\frac1{2x^2},\qquad \{M\circ v,x\}=\{v,x\}=\frac1{2x^2}.
```

This holds wherever the Möbius map $`M(t)=(at+b)/(dt+e)`$ has nonzero determinant $`ae-bd\ne0`$ and finite value. Its coefficients may depend on **held-fixed** $`r,c,\ell`$ but must be constant in $`x`$ for this derivative.

Therefore $`ru`$, $`rv`$, $`r/u`$, $`1/(ru)`$, $`r/v`$, and $`1/(rv)`$ share the exact invariant $`\{z,x\}=1/(2x^2)`$ **on their respective branches**. This is a *projective derivative invariant*, not an assertion that their pulled-back Duffing equations or global norms coincide. It supplies a mathematically precise interface to later Sturm–Liouville/Schwarzian chapters while leaving those extra structures unclaimed.

## 5. Reciprocal involutions, singularities and norms

To regard the reciprocal argument as another **canonical argument with the same $`r,c`$**, define the induced spatial maps on each branch $`u\ne0`$:

```math
z_1=\frac r u=ru^\vee,\quad u^\vee=\frac1u,\quad x^\vee=c\exp(1/u),\quad (u^\vee)^\vee=u.
```

For $`z_2=1/(ru)`$ the analogous map is $`u^\vee=1/(r^2u)`$, with fixed $`r`$ and $`c`$. Its nonzero fixed points are $`u=\pm1/r`$; those of $`u\mapsto1/u`$ are $`u=\pm1`$. These are different parameter-dependent involutions.

For $`Y(u)=\mathrm{sech}(r/u)`$, the positive function approaches $`1`$ as $`u\to\pm\infty`$. Its $`L^2(\mathbb R,du)`$ norm therefore diverges. However, as $`u\to0^\pm`$, $`Y(u)\sim2e^{-r/|u|}`$, and assigning $`Y(0)=0`$ gives a smooth **flat** real extension at the center. By contrast, $`\tanh(r/u)`$ has opposite one-sided limits $`\pm1`$ at $`u=0`$ and cannot be continuously extended there.

The original separatrix's finite classification norm **does not transfer** under reciprocal reparametrization without a transformed measure and/or altered admissibility class. The inversion changes the integral Jacobian:

```math
z=\frac r u,\qquad du=-\frac r{z^2}\,dz\quad\text{on each oriented half-line}.
```

The singular point becomes an infinite argument endpoint. Consequently, the formula reparametrization is exact locally, while the global Hilbert-space interpretation is not preserved automatically.

## 6. Wick continuation and the Gudermannian branch

For any real argument $`z`$, analytic continuation **of the argument** gives the six exact identities

| Hyperbolic function evaluated at $`iz`$ | Circular counterpart | Domain warning |
|---|---|---|
| $`\sinh(iz)`$ | $`i\sin z`$ | entire |
| $`\cosh(iz)`$ | $`\cos z`$ | entire |
| $`\tanh(iz)`$ | $`i\tan z`$ | exclude zeros of $`\cos z`$ |
| $`\coth(iz)`$ | $`-i\cot z`$ | exclude zeros of $`\sin z`$ |
| $`\mathrm{sech}(iz)`$ | $`\sec z`$ | exclude zeros of $`\cos z`$ |
| $`\mathrm{csch}(iz)`$ | $`-i\csc z`$ | exclude zeros of $`\sin z`$ |

For the canonical $`z=\theta=ru`$, the parameter $`r>0`$ is **still real**; complexifying $`z`$ is a different operation from silently setting $`r\mapsto ir`$ on an unchanged real domain. The Gudermannian has the local real-branch continuation

```math
\mathrm{gd}(iz)=i\,\mathrm{arsinh}(\tan z)=i\,\mathrm{arctanh}(\sin z),\qquad -\pi/2<z<\pi/2.
```

Outside that interval, inverse-function and logarithmic branches must be specified; periodic trigonometric functions do not make the Gudermannian globally single-valued as an inverse clock. For example, at fixed $`r,c`$, the literal function $`\tan(ru)`$ has poles at $`x=c\exp[(n+1/2)\pi/r]`$, while $`\tanh(ru)`$ has none on the real $`x>0`$ axis.

## 7. Editorial classification: more charts do not imply more independent fields

| Transformation class | Representative operation | New mathematical data needed | Retained or lost structure |
|---|---|---|---|
| Center reflection | $`c\mapsto\ell^2/c`$ | fixed reference $`\ell`$ | same canonical profile family, different active-parameter direction |
| Monotone real recharting | $`\theta\mapsto\eta,W,P,b,t`$ | inverse domain and Jacobian | same one-dimensional argument information |
| Sign-losing field projection | $`\theta\mapsto S`$ or $`R`$ | sign sheet / branch choice | loses $`\mathrm{sgn}(\theta)`$ globally |
| Reciprocal/Möbius | $`u\mapsto1/u`$ | excluded centers, transformed measures | locally invertible; new endpoint and norm behavior |
| Wick argument continuation | $`z\mapsto iz`$ | complex domain and log branches | changes real slice and introduces real poles |
| Chosen geometry | Hopf phase lift | independent phases/metric/marking | additional fibre and connection data |

**Conclusion:** there are infinitely many admissible reparametrizations on suitable intervals. The productive problem is to classify their **equivalence classes and invariants** (Schwarzian, argument derivative, domains, norms, and parameter transformations), rather than count all compositions as new objects. The six reciprocals/product examples are explicitly verified in [the targeted calculation](../_standards/verify_extended_argument_atlas.py), and the original kernel's amplitude prefactor remains defined only in its original canonical contract.
