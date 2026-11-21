# 2.10 — Restricted arctangent addition of CDF values

Let

```math
F(x)=\frac2\pi\arctan((x/c)^r),\qquad x>0.
```

For $`a=(x_1/c)^r`$, $`b=(x_2/c)^r`$, assume $`ab<1`$ (equivalently $`x_1x_2<c^2`$). Then $`\arctan a+\arctan b<\pi/2`$ and tangent addition has no branch correction:

```math
\tan(\arctan a+\arctan b)=\frac{a+b}{1-ab}.
```

Therefore **[E]**

```math
F\left(\left[\frac{x_1^r+x_2^r} {1-(x_1x_2/c^2)^r}\right]^{1/r}\right) =F(x_1)+F(x_2),\quad x_1x_2<c^2.
```

The expression inside the brackets has dimensions of $`x^r`$ and is positive on the stated domain.

**Boundary/branch behavior.** If $`x_1x_2=c^2`$, the sum of CDF values is exactly $`1`$, corresponding to the limiting argument $`x_{\rm new}\to\infty`$. If $`x_1x_2>c^2`$, the sum exceeds $`1`$, so it cannot be the CDF at a finite positive argument. Tangent addition still holds as an angle identity but requires the correct $`\pi`$ branch.

This is an algebraic addition law for CDF *values* under a nonlinear composition of their *arguments*, not the distribution of $`X_1+X_2`$ for independent variables.

## A local partial operation, not a global group

Define $`x_1\boxplus_c x_2`$ by the positive expression in the preceding theorem, **only** when $`F(x_1)+F(x_2)<1`$. Equivalently, $`x_1x_2<c^2`$.

```math
x_1\boxplus_c x_2=\left(\frac{x_1^r+x_2^r}{1-(x_1x_2/c^2)^r}\right)^{1/r},\qquad F(x_1\boxplus_c x_2)=F(x_1)+F(x_2).
```

**Associativity on the common domain.** If three arguments satisfy $`F(x_1)+F(x_2)+F(x_3)<1`$, the map $`F`$ is injective and both parenthesizations exist and have the same CDF value. Therefore

```math
(x_1\boxplus_c x_2)\boxplus_c x_3=x_1\boxplus_c(x_2\boxplus_c x_3).
```

The same reasoning applies to any finite collection whose sum of CDF values is less than $`1`$. This structure is **partial**: it has no identity among finite positive $`x`$ (the limiting identity $`x=0`$ lies outside the domain), and it is not closed under arbitrary repeated addition. Accordingly, calling it an ordinary group on $`(0,\infty)`$ would be false.

## Branch check and sharp boundary

Write $`\theta_j=\arctan((x_j/c)^r)\in(0,\pi/2)`$. Then $`F(x_j)=2\theta_j/\pi`$. The tangent addition formula yields the positive real $`x_1\boxplus_c x_2`$ only when $`\theta_1+\theta_2<\pi/2`$. At equality, its value diverges and the CDF sum reaches $`1`$; above equality a finite positive input cannot realize the sum. Passing to a projective tangent coordinate is possible, but it changes the domain and is not the same as a CDF group law.
