# 4.2 Arc-Length Element

The fundamental metric quantity of a curve embedded in a Euclidean plane is its arc-length element, $\mathrm{d}s$. This element relates the infinitesimal geometric distance along the curve to the infinitesimal displacement along its parameterizing coordinate.

The differential arc-length along the curve $y = f(x;r,c)$ is given by:

$$
\boxed{ \frac{\mathrm{d}s}{\mathrm{d}x} = \sqrt{1 + [f'(x;r,c)]^{2}} }
$$

where the exact first derivative is:

$$
f'(x;r,c) = \frac{c^{r}x^{r-2}\bigl[(r-1)c^{2r}-(r+1)x^{2r}\bigr]}{(c^{2r}+x^{2r})^{2}}
$$

### Exposition

This formula provides the local scaling factor between the coordinate distance $\mathrm{d}x$ and the true geometric path length $\mathrm{d}s$. The integral of this element, $L(a,b) = \int_a^b \frac{\mathrm{d}s}{\mathrm{d}x} \mathrm{d}x$, yields the total length of the curve between points $a$ and $b$. Because the expression for $f'(x)$ is a complex rational function, the arc-length integral generally falls into the category of hyperelliptic integrals.

### Derivation

The derivation is a direct application of the Pythagorean theorem in the context of infinitesimal calculus.

**Step 1: The Euclidean Metric in Infinitesimal Form**
In the two-dimensional Cartesian plane, the infinitesimal distance $\mathrm{d}s$ between two infinitesimally close points $(x, y)$ and $(x+\mathrm{d}x, y+\mathrm{d}y)$ on the curve is given by the Pythagorean theorem:

$$
(\mathrm{d}s)^2 = (\mathrm{d}x)^2 + (\mathrm{d}y)^2
$$

**Step 2: Parameterize by the Independent Variable $x$**
To express the arc-length element solely in terms of the independent variable $x$, we factor out $(\mathrm{d}x)^2$:

$$
(\mathrm{d}s)^2 = (\mathrm{d}x)^2 \left( 1 + \left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2 \right)
$$

Taking the positive square root (as arc length is non-negative) yields the standard formula for the arc-length element:

$$
\frac{\mathrm{d}s}{\mathrm{d}x} = \sqrt{1 + \left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2} = \sqrt{1 + [f'(x)]^2}
$$

**Step 3: Substitute the Explicit Derivative**
The explicit algebraic expression for the first derivative, $f'(x)$, was computed in §3.1 via the quotient rule applied to the core definition of $f(x)$. Substituting this known result completes the specification of the arc-length element:

$$
f'(x) = \frac{c^{r}x^{r-2}\bigl[(r-1)c^{2r}-(r+1)x^{2r}\bigr]}{(c^{2r}+x^{2r})^{2}}
$$
