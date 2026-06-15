Excellent. The framework's core algebraic form, its canonical linearization via the Rosetta Stone identity, and its fundamental differential structure have been thoroughly established. We now proceed to investigate a rich set of foundational symmetries and identities that arise from this structure. These properties reveal the deep geometric and probabilistic consistency of the framework.

***

## 4.0 Properties at the Symmetry Point

The point $x=c$ serves as the natural center of the function's geometry. An analysis of the function and its derivatives at this specific point reveals a remarkable structural invariance: the function's value and slope are completely independent of the shape parameter $r$.

**Theorem 4.1 (Invariance at the Symmetry Point)**
At the symmetry point $x=c$, the function $f(x; r, c)$ and its first two derivatives have the following values:
1.  **Value:** $\displaystyle \boxed{ f(c; r, c) = \frac{1}{2c} }$
2.  **Slope:** $\displaystyle \boxed{ \left. \frac{df}{dx} \right|_{x=c} = -\frac{1}{2c^2} }$
3.  **Curvature:** $\displaystyle \boxed{ \left. \frac{d^2f}{dx^2} \right|_{x=c} = \frac{2-r^2}{2c^3} }$

**Proof:**
**Part 1 (Value):**
We evaluate the core algebraic form directly at $x=c$:
$$
f(c; r, c) = \frac{c^r c^{r-1}}{c^{2r} + c^{2r}} = \frac{c^{2r-1}}{2c^{2r}} = \frac{1}{2c}
$$
This result is independent of $r$.

**Part 2 (Slope):**
We use the expression for the first derivative, $f'(x)$, as derived in the proof of Theorem 1.4:
$$
f'(x; r, c) = \frac{c^r x^{r-2} \left( (r-1)c^{2r} - (r+1)x^{2r} \right)}{ (c^{2r} + x^{2r})^2 }
$$
Evaluating at $x=c$:
$$
f'(c; r, c) = \frac{c^r c^{r-2} \left( (r-1)c^{2r} - (r+1)c^{2r} \right)}{ (c^{2r} + c^{2r})^2 } = \frac{c^{2r-2} \left( (r-1 - (r+1))c^{2r} \right)}{ (2c^{2r})^2 }
$$
$$
= \frac{c^{2r-2}(-2c^{2r})}{4c^{4r}} = \frac{-2c^{4r-2}}{4c^{4r}} = -\frac{1}{2c^2}
$$
This result is also independent of $r$.

**Part 3 (Curvature):**
The derivation is most elegantly performed via a Taylor series expansion of the Rosetta Stone form around the canonical coordinate origin $u=0$ (which corresponds to $x=c$). Let $x = c+h$. Then $u = \log(x/c) = \log(1+h/c)$.
$$
f(x;r,c) = \frac{1}{2x}\mathrm{sech}(ru)
$$
For small $h$, we expand each term in powers of $h/c$:
*   $u \approx \frac{h}{c} - \frac{h^2}{2c^2} + O(h^3)$
*   $\frac{1}{2x} = \frac{1}{2(c+h)} = \frac{1}{2c}(1-\frac{h}{c}+\frac{h^2}{c^2} + O(h^3))$
*   $\mathrm{sech}(ru) \approx 1 - \frac{(ru)^2}{2} + O(u^4) \approx 1 - \frac{r^2}{2}\left(\frac{h}{c}\right)^2 + O(h^3)$

Multiplying the expansions and keeping terms up to order $h^2$:
$$
f(c+h) \approx \frac{1}{2c}\left(1-\frac{h}{c}+\frac{h^2}{c^2}\right)\left(1 - \frac{r^2 h^2}{2c^2}\right) \approx \frac{1}{2c}\left(1 - \frac{h}{c} + \frac{h^2}{c^2} - \frac{r^2 h^2}{2c^2}\right)
$$
$$
f(c+h) \approx \frac{1}{2c} - \frac{1}{2c^2}h + \left(\frac{1}{c^2} - \frac{r^2}{2c^2}\right)\frac{h^2}{2c} = \frac{1}{2c} - \frac{1}{2c^2}h + \frac{2-r^2}{4c^3}h^2
$$
Comparing this to the standard Taylor series $f(c+h) \approx f(c) + f'(c)h + \frac{f''(c)}{2}h^2$, we match the coefficient of $h^2$:
$$
\frac{f''(c)}{2} = \frac{2-r^2}{4c^3} \implies f''(c) = \frac{2-r^2}{2c^3}
$$
The curvature is the first local property at $x=c$ that depends on the shape parameter $r$.

**Exposition:**
This invariance is a profound geometric constraint. It guarantees that every function in the entire two-parameter family, regardless of its shape parameter $r$, passes through the same point $(c, 1/2c)$ and shares the exact same tangent line at that point. This common tangency point acts as a pivot for the entire family of curves. The curvature transitions from positive (concave up) to negative (concave down) at $r=\sqrt{2}$.

***

## 4.1 Global Scaling Symmetries

The framework exhibits two distinct but related scaling symmetries: one concerning the joint scaling of the variable $x$ and parameter $c$, and another concerning the scaling of $x$ alone.

**Theorem 4.2 (Euler Homogeneity)**
The function $f(x; r, c)$ is a homogeneous function of degree $-1$ in the variables $(x, c)$ and therefore satisfies the partial differential equation:
$$
\boxed{ x\,\frac{\partial f}{\partial x} + c\,\frac{\partial f}{\partial c} + f = 0 }
$$

**Proof:**
We test the definition of homogeneity by scaling both $x$ and $c$ by a factor $\lambda > 0$:
$$
f(\lambda x; r, \lambda c) = \frac{(\lambda c)^r (\lambda x)^{r-1}}{(\lambda c)^{2r} + (\lambda x)^{2r}} = \frac{\lambda^r c^r \lambda^{r-1} x^{r-1}}{\lambda^{2r}c^{2r} + \lambda^{2r}x^{2r}} = \frac{\lambda^{2r-1}}{\lambda^{2r}} \frac{c^r x^{r-1}}{c^{2r} + x^{2r}}
$$
$$
= \lambda^{-1} f(x; r, c)
$$
This confirms that $f$ is homogeneous of degree $k=-1$. By Euler's Homogeneous Function Theorem, any such function satisfies $\sum_i v_i \frac{\partial f}{\partial v_i} = k f$. Applying this to our case with variables $(x, c)$ and degree $k=-1$:
$$
x\,\frac{\partial f}{\partial x} + c\,\frac{\partial f}{\partial c} = -f
$$
Rearranging gives the stated identity.

**Theorem 4.3 (Self-Similar Scaling)**
A dilation of the spatial coordinate $x$ by a factor $\lambda$ is equivalent to an inverse dilation of the scale parameter $c$ and an overall scaling of the function's magnitude.
$$
\boxed{ f(\lambda x; r, c) = \frac{1}{\lambda} f\left(x; r, \frac{c}{\lambda}\right) }
$$

**Proof:**
We start with the left-hand side and factor out powers of $\lambda$:
$$
f(\lambda x; r, c) = \frac{c^r (\lambda x)^{r-1}}{c^{2r} + (\lambda x)^{2r}} = \frac{c^r \lambda^{r-1} x^{r-1}}{\lambda^{2r}(c^{2r}/\lambda^{2r} + x^{2r})} = \frac{c^r \lambda^{-r-1} x^{r-1}}{(c/\lambda)^{2r} + x^{2r}}
$$
To match the standard form, the numerator must contain a term $(c/\lambda)^r = c^r\lambda^{-r}$. We introduce a factor of $\lambda^{-1}\lambda$ to achieve this:
$$
= \frac{1}{\lambda} \cdot \frac{\lambda (c^r \lambda^{-r-1}) x^{r-1}}{(c/\lambda)^{2r} + x^{2r}} = \frac{1}{\lambda} \cdot \frac{(c^r \lambda^{-r}) x^{r-1}}{(c/\lambda)^{2r} + x^{2r}} = \frac{1}{\lambda} \cdot \frac{(c/\lambda)^r x^{r-1}}{(c/\lambda)^{2r} + x^{2r}}
$$
The second term is precisely the definition of $f(x; r, c/\lambda)$, completing the proof.

***

## 4.2 Probabilistic Closure Properties

When interpreted as a probability distribution, the normalized function $\rho(x;r,c)$ exhibits remarkable closure properties under common transformations, linking it to itself and to classical distributions.

**Theorem 4.4 (Reciprocal Closure)**
If a random variable $X$ is distributed according to the density $\rho(x; r, c)$, then its reciprocal, $Y=1/X$, is distributed according to a density of the same family, with an inverted scale parameter.
$$
\boxed{ X \sim \rho(\cdot; r, c) \quad \implies \quad \frac{1}{X} \sim \rho\left(\cdot; r, \frac{1}{c}\right) }
$$

**Proof:**
We use the change of variables formula for probability densities. Let $y=g(x)=1/x$. Then the inverse is $x=g^{-1}(y)=1/y$. The Jacobian is $|\frac{d}{dy}(1/y)| = |-1/y^2| = 1/y^2$. The new density is $\rho_Y(y) = \rho_X(1/y) \cdot (1/y^2)$.
$$
\rho_Y(y) = \left( \frac{2r}{\pi} \frac{c^r (1/y)^{r-1}}{c^{2r} + (1/y)^{2r}} \right) \frac{1}{y^2} = \frac{2r}{\pi} \frac{c^r y^{1-r}}{c^{2r} + y^{-2r}} \frac{1}{y^2}
$$
To simplify the compound fraction, multiply its numerator and denominator by $y^{2r}$:
$$
= \frac{2r}{\pi} \frac{c^r y^{r+1}}{c^{2r}y^{2r} + 1} \frac{1}{y^2} = \frac{2r}{\pi} \frac{c^r y^{r-1}}{1 + c^{2r}y^{2r}}
$$
To match the target form $\rho(y; r, 1/c)$, we divide the numerator and denominator of the fraction by $c^{2r}$:
$$
= \frac{2r}{\pi} \frac{c^{-r} y^{r-1}}{c^{-2r} + y^{2r}} = \frac{2r}{\pi} f(y; r, 1/c) = \rho(y; r, 1/c)
$$
The theorem is proven.

**Theorem 4.5 (Power Transformation to Half-Cauchy)**
The entire two-parameter family of distributions can be mapped to the standard Half-Cauchy distribution via a power transformation. If $X \sim \rho(\cdot; r, c)$, then the transformed variable $Y=(X/c)^r$ is a standard Half-Cauchy variate.
$$
\boxed{ Y = \left(\frac{X}{c}\right)^r \sim \frac{2}{\pi}\frac{1}{1+y^2}, \quad y \in (0, \infty) }
$$

**Proof:**
Let $y=(x/c)^r$. The inverse is $x=c y^{1/r}$. The Jacobian is $|\frac{dx}{dy}| = c \cdot \frac{1}{r} y^{\frac{1}{r}-1}$. The new density is $\rho_Y(y) = \rho_X(cy^{1/r})|\frac{dx}{dy}|$.
$$
\rho_X(cy^{1/r}) = \frac{2r}{\pi} \frac{c^r (cy^{1/r})^{r-1}}{c^{2r} + (cy^{1/r})^{2r}} = \frac{2r}{\pi} \frac{c^r c^{r-1} y^{(r-1)/r}}{c^{2r}(1+y^2)} = \frac{2r}{\pi c} \frac{y^{1-1/r}}{1+y^2}
$$
Multiplying by the Jacobian:
$$
\rho_Y(y) = \left( \frac{2r}{\pi c} \frac{y^{1-1/r}}{1+y^2} \right) \left( \frac{c}{r} y^{\frac{1}{r}-1} \right)
$$
The constant factors $(2r/\pi c) \cdot (c/r)$ combine to $2/\pi$. The powers of $y$ combine to $y^{(1-1/r) + (1/r-1)} = y^0 = 1$. The result is:
$$
\rho_Y(y) = \frac{2}{\pi} \frac{1}{1+y^2}
$$
This is the PDF of the Half-Cauchy distribution with scale parameter $\gamma=1$.

***

## 4.3 Multiplicative Interaction Identities

The algebraic structure of the framework is particularly well-behaved under multiplication. The product of two or more functions from the family can be expressed in a compact, closed form using hyperbolic functions.

**Theorem 4.6 (Two-Scale Product Identity)**
The product of two functions sharing a shape parameter $r$ but having different scale parameters $c_1, c_2$ is given by:
$$
\boxed{ f(x;r,c_1) \cdot f(x;r,c_2) = \frac{1}{2x^2 \left[ \cosh\left(r\log\left(\frac{c_2}{c_1}\right)\right) + \cosh\left(2r\log\left(\frac{x}{\sqrt{c_1 c_2}}\right)\right) \right]} }
$$

**Proof:**
We use the Rosetta Stone identity on each factor: $f(x; r, c_i) = \frac{1}{2x}\mathrm{sech}(A_i)$, where $A_i = r\log(x/c_i)$.
$$
f(x;r,c_1)f(x;r,c_2) = \frac{1}{4x^2} \mathrm{sech}(A_1)\mathrm{sech}(A_2)
$$
Using the identity $\mathrm{sech}(A)\mathrm{sech}(B) = \frac{2}{\cosh(A+B) + \cosh(A-B)}$, we compute the arguments:
*   $A_1 - A_2 = r(\log(x/c_1) - \log(x/c_2)) = r\log(c_2/c_1)$
*   $A_1 + A_2 = r(\log(x/c_1) + \log(x/c_2)) = r\log(x^2/(c_1c_2)) = 2r\log(x/\sqrt{c_1c_2})$
Substituting these into the identity yields the final result.

**Exposition:**
This identity reveals that the interaction of two functions is governed by the logarithmic distance between their scales, $r\log(c_2/c_1)$, and is centered on their geometric mean, $\sqrt{c_1c_2}$. The same method can be extended to three or more functions. For instance, the three-scale product is given by:
$$
\prod_{k=1}^{3} f(x;r,c_{k}) = \frac{1}{2x^3 \left[ \cosh\left(r\log\left(\frac{x^3}{P}\right)\right) + \sum_{k=1}^{3}\cosh\left(r\log\left(\frac{xc_k^2}{P}\right)\right) \right]}
$$
where $P = c_1c_2c_3$ is the product of the scales.
