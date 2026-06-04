# 3.7 Ernst Equation and the Liouville Defect

This section investigates how the function $f(x;r,c)$ relates to the Ernst equation of general relativity and the Liouville equation of conformal field theory. The function is not a vacuum solution to the Ernst equation; instead, it satisfies a related equation with a specific source term, which is identified as the 2D Liouville equation.

### The Ernst Equation (Static, Axisymmetric Vacuum)

In cylindrical coordinates $(\rho, z)$, the Ernst equation for static, axisymmetric vacuum spacetimes can be written in terms of a potential $\mathcal{E}$ as:

$$
\text{Re}(\mathcal{E}) \nabla^2 \mathcal{E} = (\nabla \mathcal{E}) \cdot (\nabla \mathcal{E})
$$

If the potential is real ($\mathcal{E} = e^{2\phi}$), this reduces to the equation for the logarithm of the metric component:

$$
\nabla^2 \phi = 0
$$

In one dimension, with $x$ as the radial coordinate, this is equivalent to:

$$
\frac{\mathrm{d}^2}{\mathrm{d}x^2}(\log f) + \frac{1}{x}\frac{\mathrm{d}}{\mathrm{d}x}(\log f) = 0 \quad \iff \quad f(f''+f'/x) - (f')^2 = 0
$$

### The Laplacian Defect

The symmetrical function $f(x;r,c)$ does **not** satisfy the vacuum Ernst equation. Instead, it possesses a non-zero "Laplacian Defect," which has a simple, exact algebraic form.

$$
\boxed{ \nabla^2(\log f) := (\log f)'' + \frac{1}{x}(\log f)' = -4r^2 f^2 = -\frac{r^2 S^2}{x^2} }
$$

This leads to the **Liouville Equation** for $u = \log f$:

$$
\boxed{ \nabla^2 u = -4r^2 e^{2u} }
$$

### Exposition

This result is highly significant. It demonstrates that the symmetrical function is not a solution corresponding to empty space (a vacuum), but rather one that corresponds to a specific, highly structured distribution of "matter" or "charge". The source term, $-4r^2 f^2$, is proportional to the square of the function itself. This self-sourcing property is characteristic of fields that carry their own energy, and the resulting Liouville equation is one of the foundational equations of 2D conformal field theory and string theory.

### Derivation

The derivation proceeds by explicitly calculating the terms of the 1D Laplacian operator acting on $\log f$.

**Step 1: Compute the First Logarithmic Derivative**
From the Euler-Cauchy identity (§3.2), we have the exact expression for the first logarithmic derivative:

$$
(\log f)' = \frac{f'}{f} = -\frac{1+rW}{x}
$$

**Step 2: Compute the Second Logarithmic Derivative**
We differentiate $(\log f)'$ with respect to $x$ using the quotient rule.

$$
(\log f)'' = \frac{-rW'(x) \cdot x - (-(1+rW)) \cdot 1}{x^2} = \frac{-rxW' + 1+rW}{x^2}
$$

From the Riccati equation (§3.4), we know $xW' = r(1-W^2) = rS^2$. Substitute this in:

$$
(\log f)'' = \frac{-r(rS^2) + 1+rW}{x^2} = \frac{1+rW - r^2S^2}{x^2}
$$

**Step 3: Assemble the Laplacian Operator**
Now, we compute the Laplacian $\nabla^2(\log f) = (\log f)'' + \frac{1}{x}(\log f)'$:

$$
\nabla^2(\log f) = \frac{1+rW - r^2S^2}{x^2} + \frac{1}{x}\left(-\frac{1+rW}{x}\right)
$$

$$
= \frac{1+rW - r^2S^2 - (1+rW)}{x^2} = -\frac{r^2S^2}{x^2}
$$

**Step 4: Relate the Result to $f$**
Using the Half-Density Law from §1.5, we have $S^2 = 4x^2f^2$. Substitute this into the result from Step 3:

$$
\nabla^2(\log f) = -\frac{r^2(4x^2f^2)}{x^2} = -4r^2f^2
$$

This gives the primary form of the Laplacian defect.

**Step 5: Formulate the Liouville Equation**
Let $u = \log f$. Then $f = e^u$. Substituting this into the result from Step 4 gives the canonical form of the 2D Liouville equation:

$$
\nabla^2 u = -4r^2 (e^u)^2 = -4r^2 e^{2u}
$$

This completes the derivation.
