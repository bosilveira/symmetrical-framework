# 1.11 — Auxiliary Cauchy–Euler linearization and density equations

**Source and status.** This section integrates the valid Riccati-to-linear derivation from the former Chapter 1 research notes. Its auxiliary linear equation must **not** be confused with the nonlinear second-order Master equation of [Chapter 3](../03-differential-structure/03-05-linear-annihilator.md). All displayed identities are exact for $r,c,x>0$ on the distinguished positive kernel; the coupling parameter $\mu$ enters only when a separate Master solution is introduced.

## Step 1 — Define the reciprocal profile

Use the canonical coordinate $u=\log(x/c)$ and the identity $S=2xf=\mathrm{sech}(ru)$. Define its positive reciprocal:

```math
J(x;r,c):=\frac{1}{2xf(x;r,c)}=\cosh\left(r\log(x/c)\right).
```

It is convenient to write $J(u)$ when $x=ce^u$ is understood. Differentiating twice with respect to $u$ gives

```math
J_u=r\sinh(ru),\qquad J_{uu}=r^2\cosh(ru)=r^2J.
```

This is an **auxiliary linear ODE** for the reciprocal of the selected profile.

## Step 2 — Convert to the Cauchy–Euler equation

When $c$ is fixed, the Euler operator is $D=x\,d/dx=d/du$, hence $J_u=xJ_x$ and $J_{uu}=x^2J_{xx}+xJ_x$. Substitution yields

```math
x^2J_{xx}+xJ_x-r^2J=0.
```

**Converse at fixed $r>0$.** Try a power $J=x^\alpha$. The indicial equation is $\alpha(\alpha-1)+\alpha-r^2=\alpha^2-r^2=0$, so the general real solution on $x>0$ is

```math
J(x)=A x^r+B x^{-r}.
```

The two independent constants are restricted by positivity and any normalization conditions. The specific centered kernel imposes $J(c)=1$ and $J_x(c)=0$, which give

```math
A c^r+B c^{-r}=1,\qquad A c^r-B c^{-r}=0.
```

Solving yields $A=1/(2c^r)$ and $B=c^r/2$, hence

```math
J(x;r,c)=\frac12\left((x/c)^r+(c/x)^r\right)=\cosh(ru).
```

This calculation exhibits **how the scale parameter $c$ enters the integration constants** even though the differential operator itself contains only $r$.

## Step 3 — The Riccati equation is the logarithmic derivative

On any interval where $J\neq0$, set $q(u)=J_u/J$. Differentiate with the quotient rule and insert $J_{uu}=r^2J$:

```math
q_u=\frac{J_{uu}}J-\left(\frac{J_u}J\right)^2=r^2-q^2,\qquad q_u+q^2=r^2.
```

The phase of the framework is $W=q/r$, so the spatial logarithmic-derivative formula becomes

```math
W(x;r,c)=\frac{x}{r}\frac{J_x(x)}{J(x)}=\frac{x^{2r}-c^{2r}}{x^{2r}+c^{2r}}.
```

Conversely, a solution of $W_u=r(1-W^2)$ reconstructs a *nonzero* $J$ locally through $J_u=rWJ$. The equation for $W$ alone does not fix the overall multiplicative normalization of $J$.

## Step 4 — A conserved quadratic form

For any solution $J=Ae^{ru}+Be^{-ru}$ of the linear equation in $u$, its derivative is $J_u=r(Ae^{ru}-Be^{-ru})$. Expanding squares and subtracting proves

```math
J^2-\left(\frac{J_u}{r}\right)^2=(Ae^{ru}+Be^{-ru})^2-(Ae^{ru}-Be^{-ru})^2=4AB.
```

Equivalently, for $J=A_xx^r+B_xx^{-r}$,

```math
J^2-\left(\frac{xJ_x}{r}\right)^2=4A_xB_x.
```

For the centered choice above, $4A_xB_x=1$, and division by $J^2$ gives

```math
1-W^2=\frac1{J^2}=(2xf)^2=S^2.
```

The circle relation is therefore the normalized quadratic first integral of this *auxiliary* linear equation.

## Step 5 — A nonlinear ODE for the logarithmic probability density

Let $p(u;r)=(r/\pi)\mathrm{sech}(ru)=r/(\pi J(u))$. We already know from §1.3 that $p_u=-rpW$ and $W_u=rS^2$.

Differentiate the logarithmic-score identity and replace $S=\pi p/r$:

```math
(\log p)_{uu}=-rW_u=-r^2S^2=-\pi^2p^2.
```

Differentiate $p_u=-rpW$ and eliminate $W$ with $W^2+S^2=1$:

```math
p_{uu}=r^2p(W^2-S^2)=r^2p-2\pi^2p^3.
```

Finally, square $p_u=-rpW$ and again eliminate $W$:

```math
p_u^2-r^2p^2+\pi^2p^4=0.
```

These three equations are exact for this normalized density. In particular, the coefficient of the cubic nonlinearity in its **$p$-equation** is $2\pi^2$, independent of $r$, because the amplitude of $p$ itself is proportional to $r$. That observation is an algebraic normalization effect, not a new independent dynamical law.

## Step 6 — What is and is not equivalent

The implications proved above are

```math
f\longmapsto S=2xf\longmapsto J=S^{-1}\longmapsto q=J_u/J=rW,\qquad J_{uu}=r^2J.
```

Recovering the **same** $f$ requires the centered normalization $J(c)=1$, $J_x(c)=0$, and the transformation $f=1/(2xJ)$. A general solution of the linear equation need not yield the specific positive normalized kernel. The nonlinear Master equation has an energy parameter and admits additional solution families; its reciprocal is generally nonlinear away from zero energy (see [Chapter 3, §3.8](../03-differential-structure/03-08-differential-interrelation.md)).

The original source's description “Master Linear Equation” is therefore replaced by the precise title **auxiliary Cauchy–Euler linearization**.
