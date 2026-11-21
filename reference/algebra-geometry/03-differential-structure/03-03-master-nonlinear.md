# 3.3 — The first-order circle constraint (NOT the second-order Master)

For the distinguished kernel, the Euler identity $`xf_x+f=-rWf`$ and circle identity $`W^2=1-4x^2f^2`$ imply

```math
\Phi[f]:=x^2f_x^2+2xff_x+(1-r^2)f^2 +4r^2x^2f^4=0.\tag{E1}
```

Equivalently $`(xf_x+f)^2=r^2f^2(1-4x^2f^2)`$.

**Coupling convention.** For $`f_\mu=f/\sqrt\mu`$ with $`\mu>0`$, the exact constraint becomes

```math
(xf_{\mu,x}+f_\mu)^2 =r^2f_\mu^2\bigl(1-4\mu x^2f_\mu^2\bigr).\tag{E1_\mu}
```

Let $`y=2xf_\mu`$ and $`u=\log(x/c)`$. Then $`y_u=2x(xf_{\mu,x}+f_\mu)`$, and the coupling-dependent first-order constraint is precisely

```math
y_u^2-r^2y^2+\mu r^2y^4=0.
```

It is the **zero-energy first integral** of the separate second-order equation in §3.5.

**A necessary logical caution.** Squaring eliminates the sign of the Euler relation. As a counterexample, the smooth function

```math
f_s(x)=\frac{1}{2\sqrt\mu\,x}
```

satisfies the coupling-dependent first-order constraint everywhere but **does not** satisfy the second-order Master: its $`y=1/\sqrt\mu`$ is constant and $`r^2y-2\mu r^2y^3=-r^2/\sqrt\mu\ne0`$. Hence (E1) alone cannot be used as a definition of the second-order dynamics. Piecewise $`C^1`$ plateau solutions create further nonuniqueness unless suitable regularity and the full equation are imposed.

In the original draft both equations were called “Master ODE”; we reserve **Master** for the second-order equation and call this one the **first-order constraint**.

## Differentiation of the constraint and the division obstruction

Write $`E[y]=y_u^2-r^2y^2+\mu r^2y^4`$. A derivative of the first-order equation yields an identity, but it does **not** directly give the second-order Master without a nonvanishing condition.

**Step 1.** Differentiate $`E[y]=0`$ once for a twice differentiable real $`y`$:

```math
0=E_u=2y_u\bigl(y_{uu}-r^2y+2\mu r^2y^3\bigr).
```

**Step 2.** On any open interval where $`y_u\ne0`$, division proves $`y_{uu}=r^2y-2\mu r^2y^3`$.

**Step 3.** At a turning point $`y_u=0`$, however, the differentiated equation reads $`0=0`$. In particular the constant functions $`y\equiv\pm1/\sqrt\mu`$ satisfy $`E[y]=0`$ but not the Master, since the latter gives acceleration $`\mp r^2/\sqrt\mu`$.

**Step 4.** A $`C^1`$ solution can even pause at $`y=1/\sqrt\mu`$ before following a branch of a translated $`\mathrm{sech}`$ profile: the energy equation still holds but the resulting second derivative has a jump at the splice. Such a solution is not a classical global $`C^2`$ Master solution.

The sign-free equation $`y_u^2=r^2y^2(1-\mu y^2)`$ therefore determines *energy curves*, not a uniquely selected vector field. Imposing the second-order equation, the initial data and the required regularity resolves this ambiguity.

## An exact first-order factorization on a positive separatrix

If $`y>0`$ and $`E[y]=0`$, then automatically $`0<\sqrt\mu y\le1`$. Away from turning points,

```math
\frac{y_u}{y}=\pm r\sqrt{1-\mu y^2}.
```

A nonconstant global $`C^2`$ solution of the **second-order** Master with zero energy must turn from the increasing branch to the decreasing branch at $`y=1/\sqrt\mu`$; integration gives $`y(u)=\mu^{-1/2}\mathrm{sech}(r(u-u_0))`$. The corresponding negative solution is obtained by a global sign. The constant zero-energy plateaus are eliminated because they fail the second-order equation.
