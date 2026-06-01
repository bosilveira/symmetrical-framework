### 5.3 Mellin Functional Equation (The "Möbius Shadow")

The Mellin transform of the function does not just have a simple closed form; it also satisfies a remarkably symmetric functional equation. This equation directly reflects the fundamental Möbius inversion symmetry (§2.2) of the original function.

The functional equation relates the value of the Mellin transform at a point `s` to its value at the reflected point `2-s`:

$$
\boxed{\ \mathcal{M}\{f\}(s) = c^{2s-2} \, \mathcal{M}\{f\}(2-s) \ }
$$

This identity holds across the entire complex plane where the transform is defined. The symmetry occurs as a reflection across the **central line** $\text{Re}(s) = 1$.

---
**Derivation 1: Using the Möbius Symmetry in the Integral**

This derivation shows how the functional equation is a direct consequence of the function's inversion symmetry.

1.  **Start with the Definition**:
$$
\mathcal{M}\{f\}(s) = \int_0^\infty x^{s-1} f(x;r,c) \,dx
$$
2.  **Perform the Inversion Substitution**: Let $x = c^2/y$. This implies $dx = -c^2/y^2 \,dy$. The integration limits flip from $(0, \infty)$ to $(\infty, 0)$.
$$
\mathcal{M}\{f\}(s) = \int_\infty^0 \left(\frac{c^2}{y}\right)^{s-1} f\left(\frac{c^2}{y};r,c\right) \left(-\frac{c^2}{y^2} \,dy\right)
$$
3.  **Simplify and Use Symmetry**: Reverse the integration limits, which cancels the minus sign. Then apply the Möbius symmetry identity from §2.2: $f(c^2/y;r,c) = \frac{y^2}{c^2}f(y;r,c)$.
$$
\mathcal{M}\{f\}(s) = \int_0^\infty \frac{c^{2(s-1)}}{y^{s-1}} \left( \frac{y^2}{c^2}f(y;r,c) \right) \frac{c^2}{y^2} \,dy
$$
4.  **Combine Terms**: The factors of $y^2/c^2$ cancel perfectly. We are left with grouping the powers of `c` and `y`.
$$
\mathcal{M}\{f\}(s) = \int_0^\infty c^{2s-2} y^{-(s-1)} f(y;r,c) \,dy = c^{2s-2} \int_0^\infty y^{-s+1} f(y;r,c) \,dy
$$
5.  **Recognize the New Mellin Transform**: The integral on the right is, by definition, the Mellin transform of $f(y)$ with the argument $s$ replaced by $2-s$:
$$
\int_0^\infty y^{(2-s)-1} f(y;r,c) \,dy = \mathcal{M}\{f\}(2-s)
$$
This completes the derivation.

---
**Derivation 2: Verifying with the Secant Form**

This alternative proof provides a powerful consistency check by showing that our closed-form solution from §5.1 inherently satisfies the equation.

1.  **Start with the Right-Hand Side (RHS)**:
$$
\text{RHS} = c^{2s-2} \, \mathcal{M}\{f\}(2-s)
$$
2.  **Substitute the Secant Form**:
$$
\text{RHS} = c^{2s-2} \left[ \frac{\pi c^{(2-s)-1}}{2r} \sec\left(\frac{((2-s)-1)\pi}{2r}\right) \right]
$$
3.  **Simplify the Power of c**:
$$
c^{2s-2} \cdot c^{1-s} = c^{s-1}
$$
4.  **Simplify the Argument of the Secant**:
$$
\frac{(1-s)\pi}{2r} = -\frac{(s-1)\pi}{2r}
$$
5.  **Use the Even Property of Secant**: Since secant is an even function, $\sec(-z) = \sec(z)$. Therefore:
$$
\sec\left(-\frac{(s-1)\pi}{2r}\right) = \sec\left(\frac{(s-1)\pi}{2r}\right)
$$
6.  **Assemble the Result**: The RHS simplifies to:
$$
\text{RHS} = \frac{\pi c^{s-1}}{2r} \sec\left(\frac{(s-1)\pi}{2r}\right)
$$
This is precisely the expression for $\mathcal{M}\{f\}(s)$, the left-hand side. The identity is confirmed.

**Interpretation:**

The functional equation is the manifestation of the Möbius symmetry in the Mellin domain. The geometric inversion $x \leftrightarrow c^2/x$ is transformed into an analytic reflection $s \leftrightarrow 2-s$ across the line $\text{Re}(s)=1$. This is a hallmark of functions with deep structural symmetries, famously appearing in the functional equation for the Riemann Zeta function.
