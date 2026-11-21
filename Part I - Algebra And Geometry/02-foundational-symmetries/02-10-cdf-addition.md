# 2.10 — Restricted arctangent addition of CDF values

Let

```math
F(x)=\frac2\pi\arctan((x/c)^r),\qquad x>0.
```

For $a=(x_1/c)^r$, $b=(x_2/c)^r$, assume $ab<1$ (equivalently $x_1x_2<c^2$). Then $\arctan a+\arctan b<\pi/2$ and tangent addition has no branch correction:

```math
\tan(\arctan a+\arctan b)=\frac{a+b}{1-ab}.
```

Therefore **[E]**

```math
F\left(\left[\frac{x_1^r+x_2^r} {1-(x_1x_2/c^2)^r}\right]^{1/r}\right) =F(x_1)+F(x_2),\quad x_1x_2<c^2.
```

The expression inside the brackets has dimensions of $x^r$ and is positive on the stated domain.

**Boundary/branch behavior.** If $x_1x_2=c^2$, the sum of CDF values is exactly $1$, corresponding to the limiting argument $x_{\rm new}\to\infty$. If $x_1x_2>c^2$, the sum exceeds $1$, so it cannot be the CDF at a finite positive argument. Tangent addition still holds as an angle identity but requires the correct $\pi$ branch.

This is an algebraic addition law for CDF *values* under a nonlinear composition of their *arguments*, not the distribution of $X_1+X_2$ for independent variables.
