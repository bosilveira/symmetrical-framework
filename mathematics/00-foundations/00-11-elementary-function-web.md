# 00.11 — Typed elementary-function web: hyperbolic, circular, Gudermannian and logarithmic charts

**Status:** exact identities of *selected* canonical fields, with domains and parameter/coordinate maps. This is a foundational **dictionary**, not a claim that all elementary functions satisfy one universal ODE, nor that the more advanced constructions follow uniquely. The arithmetic/derivative base is [§00.06](00-06-variable-parameter-derivatives.md); the first-/second-order systems are [§00.07](00-07-differential-algebra-oscillator-hierarchy.md) and [§00.08](00-08-projective-conics-gudermannian.md). Historical source anchors: Complete Reference 2026-11-16 v2 §§1, F, 21, 27–28 and the November 21 ZIP `04-follow-ups/profile-web.md`, `04-follow-ups/bernoulli-riccati.md`, and `05-companion/hopf-villarceau-atlas/hopf-villarceau-notes.md`.

## 1. The independent parameters must remain visible

Declare the real domain $`x,c,r>0`$. In the original $`(x,c,r)`$ chart,

```math
u=\log(x/c),\qquad \theta=ru,\qquad T=e^\theta=(x/c)^r,\qquad \eta=\mathrm{gd}(\theta)=2\arctan T-\frac{\pi}{2}.
```

The maps $`x=ce^u`$, $`T=e^{ru}`$, and $`\theta=\mathrm{arsinh}(\tan\eta)`$ are mutually invertible on their stated real open domains. **Do not identify** the dimensionless multiplicative coordinate $`x/c`$ with the canonical logarithmic $`u`$, or $`\eta`$ with the Gram rapidity $`\eta_G`$.

| Coordinate chart | Forward map | Inverse, with retained parameters | Differential/Jacobian |
|---|---|---|---|
| $`(x,c,r) \to (u,c,r)`$ | $`u=\log(x/c)`$ | $`x=ce^u`$ | $`du=dx/x-dc/c`$ |
| $`(u,c,r) \to (\theta,c,r)`$ | $`\theta=ru`$ | $`u=\theta/r`$ | $`d\theta=r\,du+u\,dr`$ |
| $`(\theta,c,r) \to (T,c,r)`$ | $`T=e^\theta`$ | $`\theta=\log T`$, $`T>0`$ | $`dT=T\,d\theta`$ |
| $`(\theta,c,r) \to (\eta,c,r)`$ | $`\eta=\mathrm{gd}\theta`$ | $`\theta=\mathrm{arsinh}(\tan\eta)`$ | $`d\eta=S\,d\theta`$, $`-\pi/2<\eta<\pi/2`$ |

The universal differential identities, with no parameter suppressed, are

```math
d\theta=r\left(\frac{dx}{x}-\frac{dc}{c}\right)+u\,dr,\qquad d\eta=S\,d\theta.
```

For any argument-only $`C^1`$ field $`F(\theta)`$, write $`F_\theta=dF/d\theta`$. In the $`(x,c,r)`$ chart,

```math
F_x=\frac r xF_\theta,\qquad F_c=-\frac r cF_\theta,\qquad F_r=uF_\theta.
```

These partials hold the other two chart coordinates fixed. For second derivatives and parameter-dependent prefactors, consult [§00.09](00-09-second-derivative-charts.md).

## 2. Six hyperbolic functions of $`\theta`$ and six circular functions of $`\eta`$

Set $`S=\mathrm{sech}\theta`$, $`W=\tanh\theta`$, $`R=\cosh\theta`$, $`b=\sinh\theta`$, and $`H:=H_2=S^2`$ **only as a table-local alias**. The cross-chapter squared field is $`\mathcal B=S^2`$, and the Gram coefficient $`B`$ remains unrelated.

| Hyperbolic function of $`\theta`$ | Expression using the canonical fields | Circular function of $`\eta`$ | Same value on the real branch |
|---|---|---|---|
| $`\sinh\theta`$ | $`b=(T-T^{-1})/2`$ | $`\tan\eta`$ | $`b`$ |
| $`\cosh\theta`$ | $`R=(T+T^{-1})/2`$ | $`\sec\eta`$ | $`R`$ |
| $`\tanh\theta`$ | $`W=b/R=(T^2-1)/(T^2+1)`$ | $`\sin\eta`$ | $`W`$ |
| $`\mathrm{sech}\theta`$ | $`S=1/R=2T/(1+T^2)`$ | $`\cos\eta`$ | $`S`$ |
| $`\coth\theta`$ | $`R/b=1/W`$ | $`\csc\eta`$ | $`1/W`$ |
| $`\mathrm{csch}\theta`$ | $`1/b=S/W`$ | $`\cot\eta`$ | $`1/b`$ |

The last two rows require **$`\theta\ne0`$**, equivalently $`x\ne c`$. They have poles at the canonical symmetry point, whereas $`S,W,R,b`$ remain regular. On the real branch, the angular endpoints $`\eta=\pm\pi/2`$ occur only as $`u\to\pm\infty`$, not at finite $`x`$.

This table is one *six-function web in two clocks*: the circular variable is $`\eta=\mathrm{gd}(\theta)`$, **not** $`\theta`$. Circular functions $`\sin\theta,\cos\theta,\tan\theta,\ldots`$ also exist but belong to a separate real-oscillatory extension (§6).

## 3. The algebraic, differential and projective skeleton

Every function in the six hyperbolic rows is rational (or Laurent-rational) in $`T>0`$ and inherits the derivation

```math
D_u=rT\,\frac{d}{dT},\qquad D_\theta=T\,\frac{d}{dT}\quad (r,c\ \mathrm{fixed}).
```

The circle and hyperbola obey $`S^2+W^2=1`$, $`R^2-b^2=1`$, with the projective representation

```math
[R:b:1]=[1:W:S]=[T^2+1:T^2-1:2T].
```

The projective half-angle coordinate $`t=\tan(\eta/2)=\tanh(\theta/2)=(T-1)/(T+1)`$ yields

```math
W=\frac{2t}{1+t^2},\qquad S=\frac{1-t^2}{1+t^2},\qquad b=\frac{2t}{1-t^2},\qquad R=\frac{1+t^2}{1-t^2}.
```

Here $`-1<t<1`$ for the canonical real branch. These formulas give an **invertible** rational parameterization on the chosen open arc; the quadratic projection $`(S,W)\mapsto(P,H)`$ with $`P=(1+W)/2`$, $`H=S^2=4P(1-P)`$ is a *different* map that forgets the sign of $`S`$ on the full circle.

## 4. Gudermannian, complex logarithm and Cayley transform

The unit-circle-valued scalar

```math
C(\theta)=S+iW=e^{i\eta}=-i\frac{1+iT}{1-iT}
```

is regular for every real $`\theta`$. Since $`S>0`$ and $`-\pi/2<\eta<\pi/2`$, the **principal** complex logarithm has no branch crossing on the selected real orbit:

```math
\mathrm{Log}\,C=i\eta,\qquad \frac{C_\theta}{C}=iS,\qquad \frac{C_u}{C}=irS.
```

The Cayley expression is a rational function of $`T`$, while its logarithm recovers the transcendental angular coordinate $`\eta`$. The complex-plane poles at $`T=\pm i`$ occur off the positive-real parameter ray and underlie the arctangent logarithm; analytic continuation must specify logarithm branches.

The original kernel includes the spatial prefactor $`f(x;r,c)=S/(2x)`$. Its primitive has two identical forms:

```math
f(x;r,c)\,dx=\frac12S\,du=\frac{d\eta}{2r}=\frac{d(\arctan T)}r,\qquad \int f\,dx=\frac{\eta}{2r}+C_0=\frac{\arctan T}{r}+\widetilde C_0.
```

The integration constants may differ. This connects the arctangent primitive to the Hopf angle without identifying the integral with an automatically chosen Hopf connection.

## 5. Logarithmic derivatives form different Riccati charts

The following *logarithmic derivatives* all differentiate with respect to $`u`$ at fixed $`r,c`$:

| Nonzero field | Logarithmic slope | Domain | First-order relation |
|---|---|---|---|
| $`R=\cosh\theta`$ | $`R_u/R=rW`$ | $`u\in\mathbb R`$ | $`q_R'+q_R^2=r^2`$ |
| $`S=\mathrm{sech}\theta`$ | $`S_u/S=-rW`$ | $`u\in\mathbb R`$ | $`q_S'+q_S^2=r^2-2r^2S^2`$ |
| $`b=\sinh\theta`$ | $`b_u/b=r\coth\theta=r/W`$ | $`u\ne0`$ | $`q_b'+q_b^2=r^2`$ |
| $`C=S+iW`$ | $`C_u/C=irS`$ | $`u\in\mathbb R`$ | $`(\mathrm{Log}C)_u=irS`$ |
| $`f=S/(2x)`$ | $`(\log f)_u=-1-rW`$ | $`u\in\mathbb R`$ | Explicit spatial weight $`x^{-1}`$ retained |

Thus the tanh and coth solutions belong to different **nonvanishing intervals** of the same unshifted Riccati equation. The reciprocal branch has a pole at $`u=0`$. Neither should be silently identified with the shifted Gram logarithmic derivative, which has a different equation for generic cross coefficient.

## 6. Literal circular functions of $`\theta`$ and analytic continuation

The six *literal* functions $`\sin\theta,\cos\theta,\tan\theta,\cot\theta,\sec\theta,\csc\theta`$ depend on the same argument $`\theta=r\log(x/c)`$, but **do not generally lie in the rational differential field $`\mathbb C(T)`$** generated by $`T=e^\theta`$. On the specified positive real branch $`T>0`$,

```math
e^{i\theta}=T^i=\exp(i\log T),\qquad \cos\theta=\frac{T^i+T^{-i}}2,\qquad \sin\theta=\frac{T^i-T^{-i}}{2i}.
```

Equivalently, by analytic continuation in the **argument**,

```math
\cos\theta=\cosh(i\theta),\qquad \sin\theta=-i\sinh(i\theta),\qquad \tan\theta=-i\tanh(i\theta).
```

This is not permission to silently replace the canonical real resolution $`r>0`$ by a complex parameter: argument continuation and parameter variation are different mathematical operations. Literal $`\tan\theta`$ and $`\sec\theta`$ possess real pole sets absent from $`W`$ and $`S`$, and $`\cot\theta,\csc\theta`$ have their own pole sets. Every differentiable chart is restricted to a pole-free interval.

## 7. Chebyshev multiplication and the resolution action

For an integer $`n\ge1`$, at **fixed $`x,c`$**, the change $`r\mapsto nr`$ sends $`\theta\mapsto n\theta`$ without changing $`u`$. The classical polynomial identities are

```math
\cosh(n\theta)=T_n(R),\qquad \sinh(n\theta)=b\,U_{n-1}(R).
```

Here $`T_n`$ and $`U_{n-1}`$ are Chebyshev polynomials of the first and second kind, **not** the exponential coordinate $`T=e^\theta`$. Define the finite polynomials $`E_n(W)=\sum_{j\ \mathrm{even}}\binom nj W^j`$ and $`O_n(W)=\sum_{j\ \mathrm{odd}}\binom nj W^j`$. Then

```math
\tanh(n\theta)=\frac{O_n(W)}{E_n(W)},\qquad \mathrm{sech}(n\theta)=\frac{S^n}{E_n(W)},\qquad E_n(W)>0\quad (|W|<1).
```

The corresponding Gudermannian angle is $`\eta_n=\mathrm{gd}(n\theta)`$; its projective half-angle parameter is $`\tan(\pi/4+\eta_n/2)=T^n`$. This is a **new member of the same profile family at resolution $`nr`$**, not the assertion that a generic nonzero-energy Master orbit follows a Chebyshev recurrence.

## 8. The amplitude-exchange involution and the Clifford point

Restrict to $`x>c`$ (so $`\theta>0`$, $`T>1`$, $`S,W>0`$). Define the *new dimensionless argument*, at fixed $`r,c`$,

```math
\gamma=\log\coth\left(\frac\theta2\right)>0,\qquad T^\vee=e^\gamma=\frac{T+1}{T-1},\qquad \gamma_\theta=-\frac1b.
```

This is an involution: $`(T^\vee)^\vee=T`$. The elementary fields exchange as

```math
\mathrm{sech}\gamma=W(\theta),\qquad \tanh\gamma=S(\theta),\qquad \sinh\gamma=\frac1b,\qquad \cosh\gamma=\frac Rb.
```

Thus $`(S,W)\mapsto(W,S)`$, $`\eta\mapsto\pi/2-\eta`$, and $`b\mapsto1/b`$. The fixed point is $`T_*=1+\sqrt2`$, $`\theta_*=\mathrm{arsinh}(1)`$, where $`S=W=1/\sqrt2`$ and $`\eta=\pi/4`$.

To **lift** the argument involution to the original spatial chart without discarding $`r,c`$, one must specify what is held fixed. With $`r,c`$ fixed,

```math
x^\vee=c\exp(\gamma/r)=c\left(\frac{T+1}{T-1}\right)^{1/r},\qquad x>c,\qquad x^\vee>c,\qquad (x^\vee)^\vee=x.
```

If the original $`x`$ is fixed while $`r,c`$ vary, the new coordinate itself changes. In particular, using $`\gamma_r|_{x,c}=-u/b`$ and $`\gamma_c|_{x,r}=r/(cb)`$,

```math
\left.\partial_r\log x^\vee\right|_{x,c}=-\frac{u}{rb}-\frac{\gamma}{r^2},\qquad \left.\partial_c\log x^\vee\right|_{x,r}=\frac1c+\frac1{cb}.
```

These are parameter *derivatives of the mapped spatial point*, not derivatives of a fixed-$`x^\vee`$ field. At $`x=c`$ the involution is singular: it exchanges the finite center limit with the infinite-argument end.

## 9. Where the advanced correspondences enter

| Mathematical extension | Exact shared datum | Extra structure required | Primary chapter |
|---|---|---|---|
| Fourier self-reciprocity | $`S_r(u)=\mathrm{sech}(ru)`$ | Fourier convention, additive measure $`du`$, frequency scale | [§03.03](../03-transforms-special-functions/03-03-sech-fourier-langevin.md) |
| Kink energy / Sobolev | $`W=\tanh(ru)`$ | Chosen energy functional and finite-energy boundary class | [§06.01](../06-secondary-theories/06-01-kink-poschl-teller.md) |
| Pöschl–Teller / catenoid Jacobi | $`S,W,S^2`$ | Operator, domain, angular mode if using a surface | [§06.01](../06-secondary-theories/06-01-kink-poschl-teller.md) and [§00.10](00-10-symmetric-square-lorentz-hessian.md) |
| Langevin / dimension-indexed $`{}_0F_1`$ | $`R,b,\coth\theta`$ | Dimension-index parameter $`D>0`$ and regular solution normalization | [§03.03](../03-transforms-special-functions/03-03-sech-fourier-langevin.md) |
| Hopf–Villarceau | $`S,W,R,b,\eta`$ | Independent phase angles, Hopf map, torus marking | [§05.04](../05-differential-geometry/05-04-hopf-villarceau-selected-lift.md) |

**Interpretation boundary:** the equalities above **do not make the extra structures uniquely determined by the kernel**. The useful mathematics is a typed transformation network that records the new coordinates, retained parameter data, Jacobians, branch restrictions and any lost sign, phase, or marking. The deeper dimension-reduction conjectures remain outside this foundational claim.
