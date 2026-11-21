# 00.03 — Linear backbone, symmetric-square and Gram distinctions

**Status:** exact algebraic identities. Fixed independent variable $`u=\log(x/c)`$ and rate $`r>0`$.

## Unshifted two-dimensional solution space

For coefficients $`A,B>0`$ define

```math
J_0(u)=Ae^{ru}+Be^{-ru},\qquad J_{0,uu}=r^2J_0,\qquad J_0^2-\frac{J_{0,u}^2}{r^2}=4AB=\mu_0.
```

The positivity assumption permits $`J_0=\sqrt{\mu_0}\cosh(r(u-u_0))`$, with

```math
u_0=\frac{\log(B/A)}{2r},\qquad x_0=ce^{u_0}.
```

Here $`x_0`$ is the **effective center**. Changing the center without tracking $`c`$ or $`u_0`$ changes the coordinate interpretation.

## General Gram envelope is a different object

For a symmetric matrix $`G=\begin{pmatrix}A&C\\C&B\end{pmatrix}`$ define the symmetric-square envelope

```math
J_G=Ae^{ru}+2C+Be^{-ru},\qquad \Delta_G=AB-C^2,\qquad \mu_{\det}=4\Delta_G.
```

The exact differential identities are

```math
J_{G,uu}-r^2J_G=-2Cr^2,\qquad J_{G,uuu}=r^2J_{G,u}.
```

**Do not conflate** $`J_G`$ with $`J_0`$ unless $`C=0`$, or $`\mu_{\det}=4(AB-C^2)`$ with $`\mu_0=4AB`$ unless $`C=0`$. The original scalar kernel scale $`c`$ is not the Gram cross term $`C`$.

## Projectivization and information loss

For a nonvanishing $`J_0`$, define $`Q=J_{0,u}/J_0`$. Then

```math
Q_u+Q^2=r^2,\qquad J_0(u)=J_0(u_*)\exp\left(\int_{u_*}^{u}Q(t)\,dt\right).
```

**The logarithmic derivative forgets a multiplicative constant**. It is not a bijection unless an amplitude is supplied; the Riccati equation is a projective descendant of the linear pair.

The general $`J_G`$ does **not** solve the same homogeneous second-order equation when $`C\ne0`$. Its square-root envelope connects to Ermakov–Pinney after a separately specified map; that connection is indexed in [secondary theories](../06-secondary-theories/README.md).

**Sources:** [Foundation 020](../../reference/foundations/020%20The%20Linear%20Exponential%20Backbone.md), [Atlas Gram contracts](../../reference/atlas/contracts.json), Complete Reference v2 F.2 and §27.
