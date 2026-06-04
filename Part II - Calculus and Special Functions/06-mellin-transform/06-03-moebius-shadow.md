# 6.3 Mellin Functional Equation

The Mellin transform of the function satisfies a remarkably symmetric functional equation. This equation directly reflects the fundamental Möbius inversion symmetry (§2.2) of the original function, casting a "shadow" of that geometric property into the complex $s$-plane.

The functional equation relates the value of the Mellin transform at a point $s$ to its value at the reflected point $2-s$:

$$
\boxed{ \mathcal{M}\{f\}(s) = c^{2s-2} \, \mathcal{M}\{f\}(2-s) }
$$

This identity holds for all $s$ in the strip of convergence. The symmetry occurs as a reflection across the **central line** $\mathrm{Re}(s) = 1$.

### Exposition
This functional equation is a hallmark of functions with deep structural symmetries, famously appearing in a similar form for the Riemann Zeta function. It demonstrates that the analytic structure of the Mellin transform is not arbitrary but is constrained by the underlying geometric involution of the spatial function.

### Derivation 1: Using the Möbius Symmetry in the Integral

This proof shows how the functional equation is a direct consequence of the function's spatial inversion symmetry.

**Step 1:** Start with the definition of the Mellin Transform:

$$
\mathcal{M}\{f\}(s) = \int_0^\infty x^{s-1} f(x;r,c) \,\mathrm{d}x
$$

**Step 2:** Perform the inversion substitution $x = c^2/y$. This implies $\mathrm{d}x = -c^2/y^2 \,\mathrm{d}y$. The integration limits $(0, \infty)$ for $x$ map to $(\infty, 0)$ for $y$.

$$
\mathcal{M}\{f\}(s) = \int_\infty^0 \left(\frac{c^2}{y}\right)^{s-1} f\left(\frac{c^2}{y};r,c\right) \left(-\frac{c^2}{y^2} \,\mathrm{d}y\right)
$$

**Step 3:** Reverse the integration limits, which cancels the minus sign. Then apply the Möbius symmetry identity from §2.2: $f(c^2/y;r,c) = \frac{y^2}{c^2}f(y;r,c)$.

$$
\mathcal{M}\{f\}(s) = \int_0^\infty \frac{c^{2(s-1)}}{y^{s-1}} \left( \frac{y^2}{c^2}f(y;r,c) \right) \frac{c^2}{y^2} \,\mathrm{d}y
$$

**Step 4:** The factors of $y^2/c^2$ cancel perfectly. We are left with grouping the powers of $c$ and $y$.

$$
\mathcal{M}\{f\}(s) = \int_0^\infty c^{2s-2} y^{-(s-1)} f(y;r,c) \,\mathrm{d}y = c^{2s-2} \int_0^\infty y^{(2-s)-1} f(y;r,c) \,\mathrm{d}y
$$

**Step 5:** The integral on the right is, by definition, the Mellin transform of $f(y)$ with the argument $s$ replaced by $2-s$:

$$
\int_0^\infty y^{(2-s)-1} f(y;r,c) \,\mathrm{d}y = \mathcal{M}\{f\}(2-s)
$$

This completes the derivation.

### Derivation 2: Verifying with the Secant Form

This alternative proof provides a powerful consistency check by showing that the closed-form solution from §6.1 inherently satisfies the equation.

**Step 1:** Start with the right-hand side (RHS) of the identity:

$$
\text{RHS} = c^{2s-2} \, \mathcal{M}\{f\}(2-s)
$$

**Step 2:** Substitute the secant form for $\mathcal{M}\{f\}(2-s)$:

$$
\text{RHS} = c^{2s-2} \left[ \frac{\pi c^{(2-s)-1}}{2r} \sec\left(\frac{((2-s)-1)\pi}{2r}\right) \right]
$$

**Step 3:** Simplify the power of $c$:

$$
c^{2s-2} \cdot c^{1-s} = c^{s-1}
$$

**Step 4:** Simplify the argument of the secant:

$$
\frac{(1-s)\pi}{2r} = -\frac{(s-1)\pi}{2r}
$$

**Step 5:** Use the even property of the secant function, $\sec(-z) = \sec(z)$:

$$
\sec\left(-\frac{(s-1)\pi}{2r}\right) = \sec\left(\frac{(s-1)\pi}{2r}\right)
$$

**Step 6:** Assemble the result. The RHS simplifies to:

$$
\text{RHS} = \frac{\pi c^{s-1}}{2r} \sec\left(\frac{(s-1)\pi}{2r}\right)
$$

This is precisely the expression for $\mathcal{M}\{f\}(s)$, the left-hand side. The identity is confirmed.
