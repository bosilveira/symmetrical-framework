# 4.4 Elliptic Integral Reduction for the Case $r=1$

For arbitrary values of the shape parameter $r$, the arc-length integral leads to complex hyperelliptic functions. However, in the classical case where $r=1$ (the Cauchy/Lorentzian kernel), the geometry simplifies significantly. The arc length of any finite segment of this curve can be evaluated exactly using the classical theory of **elliptic integrals**.

### Exposition

The integral for the arc length of the function $f(x;1,c)$ is an elliptic integral. This means that while it does not have an elementary antiderivative, it can be expressed in terms of the canonical Legendre normal forms, most notably the incomplete elliptic integral of the first kind, $F(\phi, k)$. This connection situates the geometry of the $r=1$ curve squarely within the historical context of 19th-century analysis, which arose from studying the arc lengths of ellipses and lemniscates.

### Derivation and Structural Analysis

**Step 1: State the Derivative for $r=1$**
Recall the general first derivative from §4.2. Substituting $r=1$ gives:

$$
f'(x; 1, c) = \frac{c^{1}x^{1-2}\bigl[(1-1)c^{2}-(1+1)x^{2}\bigr]}{(c^{2}+x^{2})^{2}} = \frac{c x^{-1}(-2x^2)}{(c^{2}+x^{2})^{2}} = \frac{-2cx}{(c^{2}+x^{2})^{2}}
$$

**Step 2: Form the Arc-Length Radicand**
We square the derivative and add 1 to form the integrand of the arc-length integral:

$$
\sqrt{1 + [f'(x)]^2} = \sqrt{1 + \frac{4c^2x^2}{(c^2+x^2)^4}} = \frac{\sqrt{(c^2+x^2)^4 + 4c^2x^2}}{(c^2+x^2)^2}
$$

The arc-length integral for a segment $[a,b]$ is therefore:

$$
L(a,b) = \int_a^b \frac{\sqrt{(c^2+x^2)^4 + 4c^2x^2}}{(c^2+x^2)^2} \mathrm{d}x
$$

**Step 3: Identify the Elliptic Structure**
Let the variable be $t=x^2$. The numerator involves the term $\sqrt{(c^2+t)^4 + 4c^2t}$. This is the square root of a polynomial in $t$ of degree 4 (a quartic polynomial). Let this polynomial be $P(t)$:

$$
P(t) = (c^2+t)^4 + 4c^2t = t^4 + 4c^2 t^3 + 6c^4 t^2 + (4c^6+4c^2)t + c^8
$$

The integral takes the form:

$$
L(a,b) = \frac{1}{2} \int_{a^2}^{b^2} \frac{\sqrt{P(t)}}{(c^2+t)^2 \sqrt{t}} \mathrm{d}t
$$

An integral of the form $\int R(t, \sqrt{P(t)}) \mathrm{d}t$, where $R$ is a rational function and $P(t)$ is a polynomial of degree 3 or 4 with no repeated roots, is defined as an **elliptic integral**.

**Step 4: Reduction to Legendre Normal Form**
By a standard sequence of algebraic and trigonometric substitutions (a process first systematized by Weierstrass), any elliptic integral can be brought into one of the three Legendre normal forms. The specific substitutions depend on the complex roots of the polynomial $P(t)$. The final result expresses the arc length $L(a,b)$ as a linear combination of the incomplete elliptic integrals of the first, second, and third kinds, with an elliptic modulus $k$ determined by the cross-ratio of the roots of $P(t)$. While the explicit reduction is algebraically intensive, the existence of this reduction is a classical theorem of integral calculus.
