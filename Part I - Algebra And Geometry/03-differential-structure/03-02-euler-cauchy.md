# 3.2 — Euler–Cauchy identity and logarithmic derivative

Starting from $`2xf=S(u)`$ and differentiating with respect to $`u`$ gives

```math
2D(xf)=S_u=-rSW=-2rxWf.
```

Because $`D(xf)=x(xf_x+f)`$, division by $`2x`$ yields **[E]**

```math
xf_x+f=-rWf,\qquad x\,\partial_x\log f=-1-rW.
```

The latter is valid globally on $`x>0`$ because $`f>0`$.

The coupled logarithmic derivative satisfies

```math
\frac{d}{du}\log(xf)=-rW,\qquad \frac{d^2}{du^2}\log(xf)=-r^2S^2.
```

These formulas make explicit why a derivative with respect to $`x`$ differs from a derivative with respect to $`u`$.

**Reconstruction with initial data.** If $`W=\tanh(ru)`$ and a positive $`F`$ satisfies $`xF_x+F=-rWF`$ with $`F(c)=1/(2c)`$, then

```math
\log(2xF)= -\log\cosh(ru),\quad F(x)=\frac{S(u)}{2x}.
```

Without that initial amplitude, the linear equation has the family $`F(x)=A S(u)/x`$ for an arbitrary positive constant $`A`$.

This is a first-order **linear equation in $`F`$ for prescribed $`W`$**. Eliminating $`W`$ produces a nonlinear equation, which must be treated separately.

## Equivalent logarithmic-derivative formulations

The spatial phase can be recovered algebraically from $`f`$ without solving a new differential equation. Since $`f>0`$,

```math
W=-\frac1r\bigl(1+D\log f\bigr)=-\frac1rD\log(xf).
```

**Step 1.** Differentiate $`D\log(xf)=-rW`$ once more, using $`DW=r(1-W^2)`$.

**Step 2.** Substitute $`W=-D\log(xf)/r`$:

```math
D^2\log(xf)=-r^2\left(1-\frac{(D\log(xf))^2}{r^2}\right)=(D\log(xf))^2-r^2.
```

**Step 3.** Define the positive reciprocal $`J=1/(2xf)`$. Since $`\log J=-\log(2xf)`$, differentiation gives $`D\log J=rW`$. The previous nonlinear equation for $`\log(xf)`$ becomes

```math
D^2J=r^2J,\qquad D^2=x^2\partial_x^2+x\partial_x.
```

The linear equation describes the reciprocal **only for the distinguished kernel or an appropriately normalized zero-energy Master solution**, not the reciprocal of every nonlinear Master solution.

## Reconstruction from the coupled system

Suppose a differentiable phase $`V`$ satisfies $`V_u=r(1-V^2)`$ with $`V(0)=0`$. Uniqueness for the smooth Riccati right-hand side gives $`V(u)=\tanh(ru)`$. If $`F>0`$ also satisfies $`D\log(xF)=-rV`$ and $`F(c)=1/(2c)`$, integrate from $`u=0`$:

```math
\log\frac{2xF(x)}{2cF(c)}=-r\int_0^u\tanh(rv)\,dv=-\log\cosh(ru).
```

Since $`2cF(c)=1`$, this recovers $`2xF=\mathrm{sech}(ru)`$. The initial values eliminate both an arbitrary multiplicative amplitude and an arbitrary logarithmic translation.
