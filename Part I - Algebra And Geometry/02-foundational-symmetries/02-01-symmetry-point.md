# 2.1 Properties at the Symmetry Point

The behavior of the function $f(x; r, c)$ and its derivatives at the central point of symmetry, $x=c$, reveals a remarkable structural invariance. The value and the first derivative at this point are constant for all possible values of the shape parameter $r$.

The value, first derivative (slope), and second derivative (curvature) at $x=c$ are given by:

$$
\boxed{ f(c; r, c) = \frac{1}{2c} }
$$

$$
\boxed{ \left. \frac{\mathrm{d}f}{\mathrm{d}x} \right|_{x=c} = -\frac{1}{2c^2} }
$$

$$
\boxed{ \left. \frac{\mathrm{d}^2f}{\mathrm{d}x^2} \right|_{x=c} = \frac{2-r^2}{2c^3} }
$$

### Exposition

The $r$-invariance of the function's value and slope at $x=c$ is a profound geometric constraint. It proves that every single function in the two-parameter family, regardless of its shape, passes through the same point $(c, 1/2c)$ and shares the exact same tangent line. The curvature is the first local property that depends on the shape parameter $r$, and its sign dictates the local convexity of the curve at its center, with a critical transition occurring at $r=\sqrt{2}$.

### Derivations

#### Derivation of the Value at $x=c$

**Step 1:** Evaluate the core algebraic form from §1.1 at $x=c$:

$$
f(c; r, c) = \frac{c^r c^{r-1}}{c^{2r} + c^{2r}} = \frac{c^{2r-1}}{2c^{2r}}
$$

**Step 2:** Simplify the expression:

$$
f(c;r,c) = \frac{1}{2c}
$$

This result is independent of $r$.

#### Derivation of the First Derivative at $x=c$

**Step 1:** Compute the first derivative of $f(x)$ using the quotient rule. Let $u(x) = c^r x^{r-1}$ and $v(x) = c^{2r} + x^{2r}$. Then $u'(x) = c^r(r-1)x^{r-2}$ and $v'(x) = 2rx^{2r-1}$.

$$
\frac{\mathrm{d}f}{\mathrm{d}x} = \frac{u'(x)v(x) - u(x)v'(x)}{[v(x)]^2} = \frac{\left(c^r(r-1)x^{r-2}\right)\left(c^{2r}+x^{2r}\right) - \left(c^r x^{r-1}\right)\left(2rx^{2r-1}\right)}{\left(c^{2r}+x^{2r}\right)^2}
$$

**Step 2:** Evaluate the derivative at $x=c$:

$$
\left. \frac{\mathrm{d}f}{\mathrm{d}x} \right|_{x=c} = \frac{\left(c^r(r-1)c^{r-2}\right)\left(2c^{2r}\right) - \left(c^r c^{r-1}\right)\left(2rc^{2r-1}\right)}{\left(2c^{2r}\right)^2}
$$

Simplify the numerator:

$$
\text{Numerator} = 2c^{2r}(r-1)c^{2r-2} - 2rc^{2r-1}c^{2r-1} = 2(r-1)c^{4r-2} - 2rc^{4r-2}
$$

$$
= (2r-2-2r)c^{4r-2} = -2c^{4r-2}
$$

Simplify the denominator:

$$
\text{Denominator} = 4c^{4r}
$$

**Step 3:** Compute the final ratio:

$$
\left. \frac{\mathrm{d}f}{\mathrm{d}x} \right|_{x=c} = \frac{-2c^{4r-2}}{4c^{4r}} = -\frac{1}{2c^2}
$$

This result is also independent of $r$.

#### Derivation of the Second Derivative at $x=c$

**Step 1:** Use the local Taylor series expansion from §8.2, centered at the logarithmic coordinate $u = \log(x/c) = 0$:

$$
f(x;r,c) = \frac{1}{2x} \sum_{n=0}^{\infty} \frac{E_{2n}}{(2n)!} (ru)^{2n} = \frac{1}{2x}\left( E_0 + \frac{E_2}{2!}(ru)^2 + O(u^4) \right)
$$

With $E_0=1$ and $E_2=-1$:

$$
f(x;r,c) = \frac{1}{2x}\left( 1 - \frac{r^2u^2}{2} + O(u^4) \right)
$$

**Step 2:** For small deviations from $c$, let $x = c+h$. Then $u = \log(1+h/c) \approx \frac{h}{c} - \frac{h^2}{2c^2}$. The prefactor is $\frac{1}{2x} = \frac{1}{2(c+h)} \approx \frac{1}{2c}(1 - \frac{h}{c} + \frac{h^2}{c^2})$.

**Step 3:** Expand $f(c+h)$ in powers of $h$:

$$
f(c+h) \approx \frac{1}{2c}\left(1 - \frac{h}{c} + \frac{h^2}{c^2}\right) \left(1 - \frac{r^2}{2}\left(\frac{h}{c}\right)^2 \right) \approx \frac{1}{2c}\left(1 - \frac{h}{c} + h^2\left(\frac{1}{c^2} - \frac{r^2}{2c^2}\right)\right)
$$

$$
f(c+h) \approx \frac{1}{2c} - \frac{1}{2c^2}h + \frac{2-r^2}{4c^3}h^2 + O(h^3)
$$

**Step 4:** Compare this to the standard Taylor series expansion, $f(c+h) \approx f(c) + f'(c)h + \frac{f''(c)}{2}h^2$:
By matching the coefficient of the $h^2$ term, we have:

$$
\frac{f''(c)}{2} = \frac{2-r^2}{4c^3} \quad \implies \quad f''(c) = \frac{2-r^2}{2c^3}
$$

This completes the derivation.
