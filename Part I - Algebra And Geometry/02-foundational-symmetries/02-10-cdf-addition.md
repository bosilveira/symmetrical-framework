# 2.10 CDF Addition Formula (Sum of Arguments)

The cumulative distribution function (CDF) of the normalized density $\rho(x)$ satisfies a simple addition formula. This identity arises from the underlying `arctan` structure of the CDF.

Let $F(x) \equiv F_\rho(x; r, c)$. For any two points $x_1, x_2 > 0$ such that $x_1^r x_2^r < c^{2r}$:

$$
\boxed{ F\left( \left( \frac{x_1^r + x_2^r}{1 - (x_1x_2/c^2)^r} \right)^{1/r} \right) = F(x_1) + F(x_2) }
$$

*(Note: This complex form highlights that a simple sum of arguments $F(x_1+x_2)$ is not the natural operation. The natural law is the Product Formula in file 2.11).*

### Exposition
This identity is the direct translation of the tangent addition formula into the language of the CDF. While algebraically exact, its complex argument shows that simple addition of probabilities ($F_1+F_2$) does not correspond to a simple operation on the spatial variable $x$. This motivates the search for a more natural composition law, which is the product formula.

### Derivation

**Step 1:** Recall the arctangent form of the CDF from §1.7:

$$
F(x) = \frac{2}{\pi}\arctan\left(\left(\frac{x}{c}\right)^r\right)
$$

This implies $\frac{\pi}{2}F(x) = \arctan((x/c)^r)$.

**Step 2:** State the tangent addition formula, which is the inverse of the arctangent addition formula:

$$
\tan(A+B) = \frac{\tan(A)+\tan(B)}{1-\tan(A)\tan(B)}
$$

Let $A = \frac{\pi}{2}F(x_1)$ and $B = \frac{\pi}{2}F(x_2)$. Then $\tan(A) = (x_1/c)^r$ and $\tan(B) = (x_2/c)^r$.

**Step 3:** Apply the formula:

$$
\tan\left( \frac{\pi}{2}(F(x_1)+F(x_2)) \right) = \frac{(x_1/c)^r + (x_2/c)^r}{1 - (x_1/c)^r(x_2/c)^r} = \frac{(x_1^r+x_2^r)/c^r}{1 - (x_1x_2/c^2)^r}
$$

**Step 4:** To find the argument of the CDF on the left side, we take the `arctan` and multiply by $2/\pi$:

$$
F(x_1) + F(x_2) = \frac{2}{\pi} \arctan\left( \frac{(x_1^r+x_2^r)/c^r}{1 - (x_1x_2/c^2)^r} \right)
$$

The right-hand side has the form $\frac{2}{\pi}\arctan((x_{new}/c)^r)$. By inspection, we can identify $x_{new}$:

$$
\left(\frac{x_{new}}{c}\right)^r = \frac{(x_1^r+x_2^r)/c^r}{1 - (x_1x_2/c^2)^r} \implies x_{new}^r = \frac{x_1^r+x_2^r}{1 - (x_1x_2/c^2)^r}
$$

This yields the final boxed identity. The convergence condition $x_1^r x_2^r < c^{2r}$ ensures the denominator is positive.
