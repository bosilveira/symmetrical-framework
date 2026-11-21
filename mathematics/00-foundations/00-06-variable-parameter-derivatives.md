# 00.06 — Multivariable differentiation: coordinates, active parameters and Gudermannian angle

**Status:** algebraically derived identities, with explicit fixed-coordinate conventions. The canonical object and parameter registry is [the Foundational Atlas](../../reference/atlas/README.md), not an alternative set of symbols. The Gudermannian angle has stable ID `SF-P-056` and the chart transformation has stable ID `SF-M-019`.

## 1. The three-dimensional parameter-coordinate manifold

We regard the kernel as a smooth family on

```math
\mathcal M=\{(x,c,r)\in\mathbb R^3:x>0,\ c>0,\ r>0\}.
```

Here `x` is traditionally the **independent spatial variable** and `c,r` are traditionally **family parameters**; nevertheless `c,r` are genuine differentiation variables on `\mathcal M`. A derivative such as `\partial_c f` is meaningless without saying what other coordinates are held fixed.

Define

```math
u=\log(x/c),\quad \theta=ru,\quad S=\mathrm{sech}\theta,\quad W=\tanh\theta,\quad f=\frac{S}{2x}.
```

The three natural coordinate charts for the same interior points are `(x,c,r)`, `(u,c,r)` and `(\eta,c,r)`; their coordinates are **related**, not five independent coordinates. The angle `\eta=\mathrm{gd}(\theta)` uses the real Gudermannian branch. **Naming collision:** in the existing Atlas `SF-P-038` also uses the printed symbol `eta` for the *Gram rapidity* `\eta_G=\tfrac12\log(A/B)`. That is **not** this Gudermannian angle. Use `\eta_{\mathrm{GD}}` when both appear in one derivation.

## 2. Universal total differentials (first-order pullback calculus)

On `\mathcal M`, the exterior differential of the log argument is

```math
du=\frac{dx}{x}-\frac{dc}{c},\qquad d\theta=r\left(\frac{dx}{x}-\frac{dc}{c}\right)+u\,dr.
```

The field differentials are

```math
dS=-SW\,d\theta,\qquad dW=S^2\,d\theta,\qquad dR=b\,d\theta,\qquad db=R\,d\theta
```

for `R=\cosh\theta`, `b=\sinh\theta`. Since `f=S/(2x)`, we obtain the **unified differential identity**

```math
\frac{df}{f}=-\frac{dx}{x}-W\,d\theta=-(1+rW)\frac{dx}{x}+\frac{rW}{c}\,dc-uW\,dr.
```

Here `f>0` on the specified domain. This is the cleanest way to generate all the first partial derivatives and check that no parameter dependence was suppressed.

## 3. Fixed-spatial-coordinate partial derivatives

Taking differentials separately in the three **independent coordinates `(x,c,r)`** gives

```math
\left.\frac{\partial f}{\partial x}\right|_{c,r} =-\frac{1+rW}{x}f,\quad \left.\frac{\partial f}{\partial c}\right|_{x,r} =\frac{rW}{c}f,\quad \left.\frac{\partial f}{\partial r}\right|_{x,c} =-uWf.
```

The other canonical fields obey, again in this chart,

```math
S_x=-\frac{r}{x}SW,\quad S_c=\frac{r}{c}SW,\quad S_r=-uSW, \qquad W_x=\frac{r}{x}S^2,\quad W_c=-\frac{r}{c}S^2,\quad W_r=uS^2.
```

Every subscript derivative in this display holds the other two members of `(x,c,r)` fixed.

### Euler and resolution syzygies

The simultaneous scaling `(x,c)\mapsto(\lambda x,\lambda c)` at fixed `r` satisfies

```math
(x\partial_x+c\partial_c)\,\theta=0,\qquad (x\partial_x+c\partial_c)\,f=-f.
```

At fixed `x`, the vector field

```math
V=r\partial_r+u\,c\partial_c,\qquad u=\log(x/c)
```

also satisfies `V\theta=0` and therefore `V S=V W=V f=0`. This is a **local parameter-direction identity**: different pairs `(r,c)` can preserve the argument `\theta` at one fixed `x`; it does not say that the complete functions of `x` coincide after the variation.

## 4. Fixed-log-coordinate derivatives: the same field, another chart

Let `\widetilde f(u;c,r)=f(ce^u;r,c)=\mathrm{sech}(ru)/(2ce^u)`. At fixed `u`, unlike at fixed `x`, changing `c` also changes `x=ce^u`. Hence

```math
\left.\frac{\partial\widetilde f}{\partial u}\right|_{c,r}=-(1+rW)\widetilde f,\quad \left.\frac{\partial\widetilde f}{\partial r}\right|_{u,c}=-uW\widetilde f,\quad \left.\frac{\partial\widetilde f}{\partial c}\right|_{u,r}=-\frac{\widetilde f}{c}.
```

The corresponding chain-rule operator identities, acting on any smooth scalar function on `\mathcal M`, are

```math
\left.\partial_x\right|_{c,r}=\frac1x\left.\partial_u\right|_{c,r},\qquad \left.\partial_c\right|_{x,r}=\left.\partial_c\right|_{u,r}-\frac1c\left.\partial_u\right|_{c,r},\qquad \left.\partial_r\right|_{x,c}=\left.\partial_r\right|_{u,c}.
```

This resolves the apparent discrepancy between `\partial_c f|_x=(rW/c)f` and `\partial_c\widetilde f|_u=-f/c`.

## 5. Gudermannian-angle chart

Introduce the new **independent chart coordinate**

```math
\eta=\mathrm{gd}(\theta)=\arctan(\sinh\theta) =2\arctan(e^\theta)-\frac{\pi}{2},\qquad -\frac{\pi}{2}<\eta<\frac{\pi}{2}.
```

On this open real chart,

```math
S=\cos\eta,\quad W=\sin\eta,\quad \theta=\mathrm{arsinh}(\tan\eta),\quad x=c\exp\left(\frac{\mathrm{arsinh}(\tan\eta)}{r}\right).
```

The **coordinate differential** is

```math
d\eta=S\,d\theta =S\left[r\left(\frac{dx}{x}-\frac{dc}{c}\right)+u\,dr\right].
```

Thus

```math
\left.\eta_x\right|_{c,r}=\frac{rS}{x},\quad \left.\eta_c\right|_{x,r}=-\frac{rS}{c},\quad \left.\eta_r\right|_{x,c}=uS,\quad \left.\frac{\partial x}{\partial\eta}\right|_{c,r}=\frac{x}{rS}.
```

In these coordinates the kernel becomes

```math
f_{\eta}(\eta;c,r)= \frac{\cos\eta}{2c} \exp\left[-\frac{\mathrm{arsinh}(\tan\eta)}{r}\right].
```

Its derivatives **holding `\eta` fixed when differentiating `c` or `r`** are

```math
\left.\frac{\partial f_\eta}{\partial\eta}\right|_{c,r} =-f_\eta\left(\tan\eta+\frac{\sec\eta}{r}\right),\quad \left.\frac{\partial f_\eta}{\partial c}\right|_{\eta,r}=-\frac{f_\eta}{c},\quad \left.\frac{\partial f_\eta}{\partial r}\right|_{\eta,c}=\frac{u}{r}f_\eta.
```

Because `\cos\eta>0` on the open interval, the Jacobian is nonzero there. The two limiting endpoints are not included in this real diffeomorphic chart.

The **operator transport laws** are

```math
\left.\partial_x\right|_{c,r}=\frac{rS}{x}\left.\partial_\eta\right|_{c,r},\quad \left.\partial_c\right|_{x,r}=\left.\partial_c\right|_{\eta,r}-\frac{rS}{c}\left.\partial_\eta\right|_{c,r},\quad \left.\partial_r\right|_{x,c}=\left.\partial_r\right|_{\eta,c}+uS\left.\partial_\eta\right|_{c,r}.
```

These exact formulas convert the parameter derivatives between charts. For example, `f_r|_{\eta,c}=(u/r)f` and `f_r|_{x,c}=-uWf` are both correct.

## 6. Higher derivatives, mixed partials and parameter sensitivity

The second **spatial** derivative is

```math
f_{xx}=\frac{f}{x^2}\left[2+3rW+r^2(2W^2-1)\right].
```

Two useful checks of smooth parameter differentiation are

```math
\left.\partial_r^2\log f\right|_{x,c}=-u^2S^2,\qquad \left.\partial_r\partial_c\log f\right|_{x}=\frac{W+ruS^2}{c} =\left.\partial_c\partial_r\log f\right|_x.
```

For the mixed derivative of the **kernel itself**,

```math
\left.\partial_r\partial_c f\right|_x =\frac{f}{c}\left[W+ru(1-2W^2)\right].
```

The existence of these derivatives for all `x,c,r>0` follows from the smoothness of the defining functions. Every mixed-derivative assertion must still declare a shared coordinate chart.

### Evaluation at the moving symmetry point is not a fixed-coordinate derivative

At the diagonal `x=c`, `u=W=0`, so

```math
f(c;r,c)=\frac1{2c},\quad \left.f_r\right|_{x=c}=0,\quad \left.f_c\right|_{x=c}=0,\quad \left.f_x\right|_{x=c}=-\frac1{2c^2},\quad \left.f_{xx}\right|_{x=c}=\frac{2-r^2}{2c^3}.
```

But along the **moving diagonal** `x(c)=c`, the total derivative is

```math
\frac{d}{dc}f(c;r,c)=\left.f_x\right|_{x=c}+\left.f_c\right|_{x=c}=-\frac1{2c^2}.
```

Thus “the `c`-derivative vanishes at the center” refers **only** to the partial derivative at fixed `x`.

## 7. Consequences for norms and statistical scores

The chosen *classification norm* is

```math
\int_0^\infty xf(x;r,c)^2\,dx=\frac1{2r}.
```

It has zero `c`-derivative despite the fact that `f_c|_x` is not identically zero. This is a consequence of the moving measure and substitution, not of treating `c` as a constant outside the family.

Normalize the **spatial probability density** as `\rho_X=(2r/\pi)f`. Its parameter scores at fixed observation `x` are

```math
\left.\partial_r\log\rho_X\right|_{x,c}=\frac1r-uW,\qquad \left.\partial_c\log\rho_X\right|_{x,r}=\frac{rW}{c}.
```

In contrast, the transformed log-coordinate density `\rho_U(u;r)=(r/\pi)\mathrm{sech}(ru)` is independent of `c` **at fixed `u`**. This is not a contradiction: `U=\log(X/c)` changes its definition with the parameter `c`.

## 8. Repository rule

**Every differentiated formula must declare:**

1. The **chart** (e.g. `(x,c,r)`, `(u,c,r)` or `(\eta,c,r)`).
2. The **field** (e.g. `f`, `S`, `W`, `\rho_X`, `\rho_U`, or a generic Master solution).
3. The **variable** of differentiation and the **held-fixed coordinates/parameters**.
4. Any **inverse Jacobian**, transformation of the integration measure, and parameter normalization.
5. Whether it is a **partial derivative**, **directional derivative**, **total derivative along a parameter curve**, or **derivative of a derived integral**.

This is a **foundational calculus of families**, not an assertion that the parameter manifold is itself endowed with a particular connection or geometric metric. Metric/Fisher/variational interpretations, if desired, require their own additional contracts.

**Related:** [coordinate dictionary](00-01-variables-parameters.md), [pullbacks](00-04-pullbacks-transformations.md), [differentiation](../02-calculus-norms/02-01-differentiation.md), [norms](../02-calculus-norms/02-03-norms.md), [probability](../04-probability-statistics/04-01-distribution.md), and [Atlas transformation contracts](../../reference/atlas/contracts.json).
