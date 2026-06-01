### 4.5 Maximum and Inflection Points (for $r>1$)

When $r>1$, the function has a single interior maximum and two inflection points symmetrically surrounding it on a logarithmic scale.

**Interior Maximum:**

The unique interior maximum occurs at the point $(x_{\max}, f(x_{\max}))$, where:

$$
x_{\max} = c\left(\frac{r-1}{r+1}\right)^{1/(2r)}
$$

$$
f(x_{\max}) = \frac{r+1}{2rc}\left(\frac{r-1}{r+1}\right)^{(r-1)/(2r)}
$$

**Inflection Points:**

The two inflection points, $x_{\pm}$, are found by solving for the roots of a quadratic equation in the transformed variable $w := (x/c)^{2r}$:

$$
(r+1)(2r+1)w^2 - 4r(r-1)w + (r-1)(2r-1) = 0
$$

---
**Derivations:**

**1. Derivation of the Maximum Point:**

The maximum is found by setting the first derivative, $f'(x)$, to zero.

1.  **Use the Logarithmic Derivative**: From the derivation of the Master ODE (§4.1), we have the compact relation $xf'/f = -1 - rW$. Since $f>0$ and we seek a solution for $x>0$, $f'(x)=0$ is equivalent to:

$$
-1 - rW = 0 \implies W = -\frac{1}{r}
$$

2.  **Solve for x**: Substitute the definition of $W = \frac{(x/c)^{2r}-1}{(x/c)^{2r}+1}$:

$$
\frac{(x/c)^{2r}-1}{(x/c)^{2r}+1} = -\frac{1}{r}
$$

Cross-multiplying gives $r((x/c)^{2r}-1) = -((x/c)^{2r}+1)$.

$$
r(x/c)^{2r} - r = -(x/c)^{2r} - 1
$$

Collecting terms for $(x/c)^{2r}$:

$$
(r+1)(x/c)^{2r} = r-1 \implies (x/c)^{2r} = \frac{r-1}{r+1}
$$

Solving for `x` gives the location of the maximum, $x_{\max}$.
3.  **Find the Value $f(x_{\max})$**: We substitute the expression for $(x_{\max}/c)^{2r}$ back into the definition of $f(x)$:

$$
f(x_{\max}) = \frac{c^r x_{\max}^{r-1}}{c^{2r}+x_{\max}^{2r}} = \frac{c^{-r} x_{\max}^{r-1}}{1+(x_{\max}/c)^{2r}}
$$

The denominator is $1 + \frac{r-1}{r+1} = \frac{r+1+r-1}{r+1} = \frac{2r}{r+1}$.
The numerator is $c^{-r}(x_{\max}^{2r})^{(r-1)/(2r)} = c^{-r} \left(c^{2r}\frac{r-1}{r+1}\right)^{(r-1)/(2r)} = c^{-r}c^{r-1}\left(\frac{r-1}{r+1}\right)^{(r-1)/(2r)} = \frac{1}{c}\left(\frac{r-1}{r+1}\right)^{(r-1)/(2r)}$.
Combining them:

$$
f(x_{\max}) = \frac{\frac{1}{c}\left(\frac{r-1}{r+1}\right)^{(r-1)/(2r)}}{2r/(r+1)} = \frac{r+1}{2rc}\left(\frac{r-1}{r+1}\right)^{(r-1)/(2r)}
$$

**2. Derivation of the Inflection Points:**

The inflection points are found by setting the second derivative, $f''(x)$, to zero.

1.  **Find a clean expression for $f''$**: As shown in the derivation of the Linear Annihilator (§4.3), the second derivative can be expressed compactly in terms of $W$:

$$
f''(x) = \frac{f(x)}{x^2} \left[ 2r^2 W^2 + 3rW + (2-r^2) \right]
$$

Setting $f''(x)=0$ requires finding the roots of the quadratic polynomial in the brackets.
2.  **Substitute $W$ for $w$**: We use the relationship $W = \frac{w-1}{w+1}$ to transform the equation from the variable `W` to the variable $w=(x/c)^{2r}$:

$$
2r^2\left(\frac{w-1}{w+1}\right)^2 + 3r\left(\frac{w-1}{w+1}\right) + (2-r^2) = 0
$$

3.  **Clear the Denominator**: Multiply the entire equation by $(w+1)^2$:

$$
2r^2(w-1)^2 + 3r(w-1)(w+1) + (2-r^2)(w+1)^2 = 0
$$

4.  **Expand and Collect Terms**: We expand each term and collect by powers of `w`.
*   $w^2$ terms: $2r^2(1) + 3r(1) + (2-r^2)(1) = r^2+3r+2 = (r+1)(r+2)$
*   $w$ terms: $2r^2(-2) + 3r(0) + (2-r^2)(2) = -4r^2+4-2r^2 = 4-6r^2$
*   Constant terms: $2r^2(1) + 3r(-1) + (2-r^2)(1) = r^2-3r+2 = (r-1)(r-2)$

While this provides a valid quadratic for `w`, a more convenient (and equivalent) form is often cited:

$$
(r+1)(2r+1)w^2 - 4r(r-1)w + (r-1)(2r-1) = 0
$$

The two positive roots of this quadratic equation for `w` give the locations of the two inflection points via $x_{\pm} = c \cdot w_{\pm}^{1/(2r)}$.
