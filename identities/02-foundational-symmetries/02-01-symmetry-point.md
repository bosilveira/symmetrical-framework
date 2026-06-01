### 2.1 Value, Slope, and Curvature at the Symmetry Point

The behavior of the function $f(x; r, c)$ at its central symmetry point, $x=c$, provides critical insights into the entire family. The value, first derivative (slope), and second derivative (curvature) at this point are given by exact, simple expressions:

$$
f(c; r, c) = \frac{1}{2c}
$$

$$
\left. \partial_x f(x; r, c) \right|_{x=c} = -\frac{1}{2c^2}
$$

$$
\left. \partial_{xx} f(x; r, c) \right|_{x=c} = \frac{2-r^2}{2c^3}
$$

**Derivations:**

The results are obtained by direct evaluation of the function and its derivatives at $x=c$.

1.  **Value at x=c**:  
We substitute $x=c$ directly into the core algebraic form (§1.1):

$$
f(c; r, c) = \frac{c^r c^{r-1}}{c^{2r} + c^{2r}} = \frac{c^{2r-1}}{2c^{2r}} = \frac{1}{2c}
$$

  The value at the center is remarkably independent of the shape parameter `r`.

2.  **Slope at x=c**:  
We first compute the derivative of $f(x)$ using the quotient rule. Let $u = c^r x^{r-1}$ and $v = c^{2r} + x^{2r}$. Then $u' = c^r(r-1)x^{r-2}$ and $v' = 2rx^{2r-1}$.
    
$$
\partial_x f(x) = \frac{u'v - uv'}{v^2} = \frac{\left(c^r(r-1)x^{r-2}\right)\left(c^{2r}+x^{2r}\right) - \left(c^r x^{r-1}\right)\left(2rx^{2r-1}\right)}{\left(c^{2r}+x^{2r}\right)^2}
$$

Evaluating at $x=c$ causes significant simplification:

$$
\left. \partial_x f \right|_{x=c} = \frac{\left(c^r(r-1)c^{r-2}\right)\left(2c^{2r}\right) - \left(c^r c^{r-1}\right)\left(2rc^{2r-1}\right)}{\left(2c^{2r}\right)^2}
$$

$$
= \frac{2c^{2r}(r-1)c^{2r-2} - 2r c^{2r-1}c^{2r-1}}{4c^{4r}} = \frac{2(r-1)c^{4r-2} - 2rc^{4r-2}}{4c^{4r}}
$$

$$
= \frac{(2r-2-2r)c^{4r-2}}{4c^{4r}} = \frac{-2c^{4r-2}}{4c^{4r}} = -\frac{1}{2c^2}
$$

Like the value, the slope at the symmetry point is also completely independent of `r`.

3.  **Curvature at x=c**:  
While direct symbolic differentiation is possible, a more elegant approach is to use a Taylor series expansion of the "Rosetta Stone" identity (§1.3) around the symmetry point. Let $x = c+h$ for small $h$. The canonical coordinate is $u = \log(x/c) = \log(1+h/c) \approx \frac{h}{c} - \frac{h^2}{2c^2} + O(h^3)$.

The identity is $f(x) = \frac{1}{2x}\mathrm{sech}(ru)$. We expand each term around $h=0$:
*   $\frac{1}{2x} = \frac{1}{2(c+h)} = \frac{1}{2c}(1+h/c)^{-1} \approx \frac{1}{2c}\left(1 - \frac{h}{c} + \frac{h^2}{c^2}\right)$
*   $\mathrm{sech}(ru) \approx 1 - \frac{(ru)^2}{2} \approx 1 - \frac{r^2}{2}\left(\frac{h}{c}\right)^2$

Multiplying these expansions gives:

$$
f(c+h) \approx \frac{1}{2c}\left(1 - \frac{h}{c} + \frac{h^2}{c^2}\right)\left(1 - \frac{r^2h^2}{2c^2}\right) \approx \frac{1}{2c}\left(1 - \frac{h}{c} + \frac{h^2}{c^2} - \frac{r^2h^2}{2c^2}\right)
$$

$$
f(c+h) \approx \frac{1}{2c} - \frac{1}{2c^2}h + \left(\frac{2-r^2}{4c^3}\right)h^2
$$

Comparing this to the standard Taylor expansion, $f(c+h) \approx f(c) + f'(c)h + \frac{f''(c)}{2}h^2$, we can identify the second derivative term:

$$
\frac{f''(c)}{2} = \frac{2-r^2}{4c^3} \quad \implies \quad f''(c) = \frac{2-r^2}{2c^3}
$$

**Significance and Interpretation:**

*   **Shared Tangent Line**: The fact that both $f(c)$ and $f'(c)$ are independent of `r` is a powerful geometric constraint. It means that *every function in the family, regardless of its shape, passes through the same point* $(c, 1/2c)$ *and shares the exact same tangent line at that point*.
*   **Curvature Transition**: The curvature at the symmetry point is the first local property that depends on `r`. Its sign reveals the local shape:
    *   If $r < \sqrt{2}$, $\partial_{xx}f > 0$, and the function is locally convex (concave up) at $x=c$.
    *   If $r > \sqrt{2}$, $\partial_{xx}f < 0$, and the function is locally concave (concave down) at $x=c$.
    *   If $r = \sqrt{2}$, $\partial_{xx}f = 0$, and $x=c$ is an inflection point. This critical value marks the transition from a "U-shaped" local minimum to a "hump-shaped" local maximum.
