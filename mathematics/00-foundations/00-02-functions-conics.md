# 00.02 — Primitive function, hyperbolic fields and conic

**Status:** direct algebraic identities for $`x,c,r>0`$ and $`u=\log(x/c)`$.

## The symmetrical kernel

```math
f(x;r,c)=\frac{c^r x^{r-1}}{c^{2r}+x^{2r}}=\frac{1}{2x}\mathrm{sech}(ru)=\frac{T}{x(1+T^2)},\qquad T=(x/c)^r.
```

The central inversion $`I_c(x)=c^2/x`$ acts as $`u\mapsto-u`$ and $`T\mapsto T^{-1}`$. The identity of **positive measures** is $`f(I_c(x))\,|dI_c(x)|=f(x)\,dx`$; the oriented differential form changes sign.

**Important:** the center $`x=c`$ is not generally the graph maximum of $`f`$, and equal half integrals alone do not uniquely characterize this kernel. See [Part I Chapter 4](../../reference/algebra-geometry/04-geometric-properties/04-00-summary.md) and [Foundation 000](../../reference/foundations/000%20Introduction%20and%20Scope.md).

## Hyperbolic circle and logistic projection

Define $`S=\mathrm{sech}(ru)`$, $`W=\tanh(ru)`$ and $`P=(1+W)/2`$. Then

```math
S=\frac{2T}{1+T^2},\qquad W=\frac{T^2-1}{T^2+1},\qquad P=\frac{T^2}{1+T^2},\qquad S^2+W^2=1.
```

The exact first derivatives, with respect to **$`u`$**, are

```math
S_u=-rSW,\qquad W_u=rS^2=r(1-W^2),\qquad P_u=2rP(1-P).
```

The circle equation is algebraic. It does not, by itself, determine a traversal rate, orientation, or differential equation.

## Linear hyperbola and its normalization

Set $`R=\cosh(ru)`$, $`b=\sinh(ru)`$. Then

```math
R^2-b^2=1,\qquad R_u=rb,\qquad b_u=rR,\qquad SR=1,\qquad W=b/R.
```

These are coordinate forms of the same hyperbolic data, not statements that the Euclidean circle and hyperbola are globally isometric.

## Gudermannian angle (a typed chart)

With $`\eta=\mathrm{gd}(ru)`$ and the standard real branch,

```math
\sin\eta=W,\qquad \cos\eta=S,\qquad \frac{d\eta}{du}=rS.
```

The angle is a coordinate map from the real line to an open angular interval. Any proposed Hopf lift or surface immersion needs additional data and is treated separately in [differential geometry](../05-differential-geometry/README.md).

**Primary sources:** [Part I §1](../../reference/algebra-geometry/01-architectural-identities/01-00-summary.md), [§2 inversion](../../reference/algebra-geometry/02-foundational-symmetries/02-02-moebius-symmetry.md), and Complete Reference v2 F.1.
