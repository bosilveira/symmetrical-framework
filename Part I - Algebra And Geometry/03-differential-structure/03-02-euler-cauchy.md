# 3.2 — Euler–Cauchy identity and logarithmic derivative

Starting from $2xf=S(u)$ and differentiating with respect to $u$ gives

```math
2D(xf)=S_u=-rSW=-2rxWf.
```

Because $D(xf)=x(xf_x+f)$, division by $2x$ yields **[E]**

```math
xf_x+f=-rWf,\qquad x\,\partial_x\log f=-1-rW.
```

The latter is valid globally on $x>0$ because $f>0$.

The coupled logarithmic derivative satisfies

```math
\frac{d}{du}\log(xf)=-rW,\qquad \frac{d^2}{du^2}\log(xf)=-r^2S^2.
```

These formulas make explicit why a derivative with respect to $x$ differs from a derivative with respect to $u$.

**Reconstruction with initial data.** If $W=\tanh(ru)$ and a positive $F$ satisfies $xF_x+F=-rWF$ with $F(c)=1/(2c)$, then

```math
\log(2xF)= -\log\cosh(ru),\quad F(x)=\frac{S(u)}{2x}.
```

Without that initial amplitude, the linear equation has the family $F(x)=A S(u)/x$ for an arbitrary positive constant $A$.

This is a first-order **linear equation in $F$ for prescribed $W$**. Eliminating $W$ produces a nonlinear equation, which must be treated separately.
