# 4.5 Self-Similar Inversion of the Graph

The algebraic Möbius symmetry established in §2.2 manifests as a profound geometric self-similarity of the function's graph in the 2D Cartesian plane. Under a specific coordinate transformation that couples horizontal inversion with vertical scaling, the curve maps perfectly onto itself.

If $S$ is the set of points $(x,y)$ forming the graph $y = f(x;r,c)$, then $S$ is invariant under the transformation:

$$
\boxed{ (x, y) \longmapsto \left( \frac{c^{2}}{x}, \frac{x^{2}}{c^{2}} y \right) }
$$

### Exposition

This identity demonstrates that the graph of the function possesses a non-trivial geometric symmetry. It states that if one takes a point on the curve, inverts its horizontal coordinate through the center point $c$ (via $x \to c^2/x$), and simultaneously rescales its vertical coordinate by a factor of $x^2/c^2$, the resulting point lies on the exact same curve. When translated into the canonical logarithmic coordinate space, this complex scale-coupled inversion reduces to a pure mirror reflection.

### Derivation

The proof demonstrates that the transformation maps any arbitrary point on the curve to another valid point on the same curve.

**Step 1:** Let $P = (x_0, y_0)$ be an arbitrary point on the graph of the function. By definition, its coordinates must satisfy the relation:

$$
y_0 = f(x_0; r, c)
$$

**Step 2:** Apply the geometric transformation $T(x, y) = \left( c^2/x, (x^2/c^2)y \right)$ to the point $P$. The coordinates of the resulting point, $P'=(x', y')$, are:

$$
x' = \frac{c^2}{x_0} \qquad \text{and} \qquad y' = \frac{x_0^2}{c^2} y_0
$$

Substitute $y_0 = f(x_0;r,c)$:

$$
y' = \frac{x_0^2}{c^2} f(x_0; r, c)
$$

**Step 3:** To verify that the point $P'$ lies on the original curve, we must show that its coordinates satisfy the relation $y' = f(x';r,c)$. We evaluate the function $f$ at the new coordinate $x'$:

$$
f(x'; r, c) = f\left(\frac{c^2}{x_0}; r, c\right)
$$

**Step 4:** Invoke the Möbius symmetry identity from §2.2:

$$
f\left(\frac{c^2}{x_0}; r, c\right) = \frac{x_0^2}{c^2} f(x_0; r, c)
$$

**Step 5:** Compare the results. The expression for $f(x')$ from Step 4 is identical to the expression for $y'$ from Step 2. Therefore, $y' = f(x')$.

This proves that the transformed point $P'$ lies on the graph of the original function. Since $x_0$ was arbitrary, the entire graph is invariant under this transformation.
