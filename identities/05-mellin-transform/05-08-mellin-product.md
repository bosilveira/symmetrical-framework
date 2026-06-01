### 5.8 Mellin Transform of a Two-Scale Product

We now generalize the Mellin transform to the product of two functions from the family, $f(x;r,c_1)f(x;r,c_2)$. The result is a complex function whose structure is governed by the geometric relationship between the two scales, $c_1$ and $c_2$.

Let $c_1 \neq c_2$, and define the following constants based on their relationship:
*   $C_g := \sqrt{c_1 c_2}$ (the geometric mean scale)
*   $A := r\log(c_2/c_1)$ (the dimensionless logarithmic distance)
*   $\alpha := \frac{s-2}{2r}$ (a shifted and scaled transform variable)

The Mellin transform of the product is given by:

$$
\boxed{\; \mathcal{M}\left\{f(\cdot;r,c_1)f(\cdot;r,c_2)\right\}(s) = \frac{\pi C_g^{s-2}}{2r} \cdot \frac{\sinh(\alpha A)}{\sin(\pi\alpha)\sinh(A)} \;}
$$

---
**Derivation:**

The derivation hinges on transforming the problem into the logarithmic coordinate space where the two-scale product has a simpler form, and then solving the resulting integral.

1.  **Apply the Two-Scale Product Identity**:  
From §2.6, we have the identity for the product of two functions:
$$
f(x;r,c_1)f(x;r,c_2) = \frac{1}{2x^2 \left( \cosh(A) + \cosh(2r\log(x/C_g)) \right)}
$$
The Mellin transform requires integrating $x^{s-1}$ times this expression:
$$
\mathcal{M}\{f_1 f_2\}(s) = \int_0^\infty x^{s-1} \left[ \frac{1}{2x^2(\dots)} \right] dx = \frac{1}{2} \int_0^\infty \frac{x^{s-3}}{\cosh(A) + \cosh(2r\log(x/C_g))} dx
$$

2.  **Change to Logarithmic Coordinates**:  
The structure of the denominator strongly suggests a change of variable to the logarithmic coordinate $\nu := 2r\log(x/C_g)$.
*   Solving for `x`: $x = C_g e^{\nu/(2r)}$.
*   The term $x^{s-3}dx$ transforms as follows:
$$
dx = \frac{C_g}{2r} e^{\nu/(2r)} d\nu
$$
$$
x^{s-3} = (C_g e^{\nu/(2r)})^{s-3} = C_g^{s-3} e^{(s-3)\nu/(2r)}
$$
$$
x^{s-3}dx = \left(C_g^{s-3} e^{(s-3)\nu/(2r)}\right) \left(\frac{C_g}{2r} e^{\nu/(2r)} d\nu\right) = \frac{C_g^{s-2}}{2r} e^{\frac{(s-2)\nu}{2r}} d\nu = \frac{C_g^{s-2}}{2r} e^{\alpha\nu} d\nu
$$

3.  **Assemble the Transformed Integral**:  
Substituting this back into the integral from Step 1, with limits changing from $(0,\infty)$ for `x` to $(-\infty, \infty)$ for `ν`, we get:
$$
\mathcal{M}\{f_1 f_2\}(s) = \frac{1}{2} \int_{-\infty}^{\infty} \frac{1}{\cosh(A) + \cosh(\nu)} \left( \frac{C_g^{s-2}}{2r} e^{\alpha\nu} d\nu \right) = \frac{C_g^{s-2}}{4r} \int_{-\infty}^{\infty} \frac{e^{\alpha\nu}}{\cosh(A) + \cosh(\nu)} d\nu
$$

4.  **Invoke the Standard Integral Identity**:  
The resulting integral is a well-known, non-trivial definite integral, often solved using contour integration in the complex plane. The standard result is:
$$
\int_{-\infty}^{\infty} \frac{e^{\alpha\nu}}{\cosh(A) + \cosh(\nu)} d\nu = \frac{2\pi \sinh(\alpha A)}{\sin(\pi\alpha)\sinh(A)}
$$
This identity is valid for $|\text{Re}(\alpha)| < 1$.

5.  **Final Result**:  
Substituting the result of the integral back into our expression from Step 3 yields the final formula:
$$
\mathcal{M}\{f_1 f_2\}(s) = \frac{C_g^{s-2}}{4r} \left[ \frac{2\pi \sinh(\alpha A)}{\sin(\pi\alpha)\sinh(A)} \right] = \frac{\pi C_g^{s-2}}{2r} \frac{\sinh(\alpha A)}{\sin(\pi\alpha)\sinh(A)}
$$

---
**Consistency Check: The Limit to the $L^2$ Case**

This general formula must reduce to our previous result for $\mathcal{M}\{f^2\}(s)$ in the limit where the two scales become equal. We check this as $c_2 \to c_1$.

1.  **Evaluate Limits**: As $c_2 \to c_1$, we have $C_g \to c_1$ and $A = r\log(c_2/c_1) \to 0$.
2.  **Handle Indeterminate Form**: The term $\frac{\sinh(\alpha A)}{\sinh(A)}$ becomes an indeterminate form $0/0$. We evaluate its limit as $A \to 0$ using L'Hôpital's rule or by recognizing the definition of the derivative:
$$
\lim_{A\to 0} \frac{\sinh(\alpha A)}{\sinh(A)} = \lim_{A\to 0} \frac{\alpha\cosh(\alpha A)}{\cosh(A)} = \frac{\alpha \cdot 1}{1} = \alpha
$$
3.  **The Limiting Formula**: The full expression becomes:
$$
\lim_{c_2\to c_1} \mathcal{M}\{f_1 f_2\}(s) = \mathcal{M}\{f^2\}(s) = \frac{\pi c_1^{s-2}}{2r} \frac{\alpha}{\sin(\pi\alpha)}
$$
4.  **Compare with §5.5 for n=2**: From §5.5, we have $\mathcal{M}\{f^2\}(s) = \frac{c_1^{s-2}}{2r} B(p,q)$ with $p=\frac{s+2(r-1)}{2r}$ and $q=\frac{2(r+1)-s}{2r}$.
Note that $p = 1+\frac{s-2}{2r} = 1+\alpha$. Then $q=2-p = 1-\alpha$.
Using the Gamma reflection formula, $B(1+\alpha, 1-\alpha) = \Gamma(1+\alpha)\Gamma(1-\alpha) = \alpha\Gamma(\alpha)\Gamma(1-\alpha) = \alpha \frac{\pi}{\sin(\pi\alpha)}$.
Therefore, the formula from §5.5 gives $\mathcal{M}\{f^2\}(s) = \frac{c_1^{s-2}}{2r} \frac{\pi\alpha}{\sin(\pi\alpha)}$.
The results match perfectly, providing a powerful verification of both formulas.
