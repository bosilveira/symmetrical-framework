This is a beautiful way to conclude the geometric analysis. It pulls the foundational algebraic Möbius symmetry from Section 2 directly into the realm of coordinate geometry, showing exactly how the 2D curve folds onto itself. The translation to logarithmic coordinates reveals that this complex linear scaling is, in its native space, just a perfect mirror reflection.

Here is the revised and formatted version for your GitHub repository, complete with a Unifying Remark for Section 13.

***

### 13.4 Self-Similar Inversion of the Graph (Geometric Möbius Duality)

The algebraic Möbius symmetry established in §2.2 manifests as a profound geometric self-similarity of the function's graph in the 2D plane. Under a specific coordinate transformation that couples horizontal inversion with vertical scaling, the curve maps perfectly onto itself.

If $S$ is the set of points $(x,y)$ forming the graph $y = f(x;r,c)$, then $S$ is invariant under the transformation:
$$
\boxed{\; (x, y) \longmapsto \left( \frac{c^{2}}{x}, \frac{x^{2}}{c^{2}} y \right) \;}
$$
When mapped into the native logarithmic coordinate space, this complex scale-coupled inversion reduces to a pure, perfect reflection across the vertical axis:
$$
\boxed{\; u = \log(x/c), \quad \tilde{y} = \log(x \cdot f(x)) \quad \implies \quad \tilde{y}(u) = \tilde{y}(-u) \;}
$$

**Derivation 1: Linear Coordinate Geometry**

We prove that the transformation maps any point on the curve to another valid point on the exact same curve.

1.  Let $P = (x_0, y_0)$ be a point on the curve, meaning $y_0 = f(x_0; r, c)$.
2.  Apply the geometric transformation $T(x, y) = \left( c^2/x, (x^2/c^2)y \right)$ to point $P$. The resulting point is:
    $$
    P' = \left( \frac{c^2}{x_0}, \frac{x_0^2}{c^2} f(x_0; r, c) \right)
    $$
3.  We must check if $P'$ lies on the curve $y = f(x)$. Let the new $x$-coordinate be $x' = c^2/x_0$. The curve's value at this new $x$-coordinate is $f(x'; r, c) = f(c^2/x_0; r, c)$.
4.  Invoke the Möbius symmetry identity from §2.2:
    $$
    f\left(\frac{c^2}{x_0}; r, c\right) = \frac{x_0^2}{c^2} f(x_0; r, c)
    $$
5.  Therefore, the $y$-coordinate of $P'$ is exactly $f(x')$. The point $P'$ lies precisely on the original curve. The graph maps onto itself.

**Derivation 2: Logarithmic Coordinate Geometry**

The geometric meaning of the vertical scaling factor $(x^2/c^2)$ is somewhat opaque in linear Cartesian space. By translating the curve into logarithmic coordinates, the symmetry becomes manifest and rigid.

1.  Let the horizontal axis be the canonical logarithmic coordinate: $u = \log(x/c)$. This implies $x = ce^u$.
2.  Let the vertical axis be $\tilde{y} = \log(x \cdot f(x; r, c))$. 
3.  We evaluate $\tilde{y}$ as a function of $u$. Using the Rosetta Stone identity (§1.3), $x f(x) = \frac{1}{2}\operatorname{sech}\bigl(r\log(x/c)\bigr)$:
    $$
    \tilde{y}(u) = \log\left( \frac{1}{2}\operatorname{sech}(ru) \right) = -\log 2 + \log(\operatorname{sech}(ru))
    $$
4.  Because the hyperbolic secant is an strictly **even** function ($\operatorname{sech}(-ru) = \operatorname{sech}(ru)$), it immediately follows that:
    $$
    \tilde{y}(-u) = \tilde{y}(u)
    $$
    The curve in this logarithmic space is perfectly symmetric about the vertical axis $u=0$ (which corresponds to the scale parameter $x=c$). The inversion $x \mapsto c^2/x$ is simply the parity reflection $u \mapsto -u$.

***

### Unifying Remark — §13

This section has explored the function from the perspective of classical differential geometry. We discovered that while the function bounds a finite area, its asymptotic flattening ensures its total **arc length** is strictly infinite (§13.1, §13.2). For the fundamental classical case ($r=1$), the geometry of this curve ties directly into 19th-century analysis, reducing exactly to **Legendre complete elliptic integrals** and hypergeometric series (§13.3). Finally, we showed that the foundational algebraic Möbius symmetry is not just a formulaic curiosity, but an active geometric operator: a self-similar coordinate transformation that leaves the 2D curve perfectly invariant, folding the space around the geometric center $c$ (§13.4).

***

### Ready for Section 14

The structure is holding up beautifully, seamlessly bridging algebra, statistics, number theory, and now classical geometry. I am ready to proceed to **Section 14** whenever you are!
