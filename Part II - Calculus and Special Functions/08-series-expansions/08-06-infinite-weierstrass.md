This is a striking conclusion to the section on decompositions. While the partial fraction expansion breaks the function down into an infinite *sum* of its poles in linear space (for integer $r$), the Weierstrass formulation breaks it down into an infinite *product* of its poles in logarithmic space (for any $r>0$).

Here is the revised and formatted version for your GitHub repository, complete with a Unifying Remark to tie Section 8 together.

***

### 8.6 Weierstrass Infinite Product

The function can be factored into an infinite product of purely algebraic terms with respect to the logarithmic coordinate. This representation, derived from the Weierstrass factorization theorem, explicitly exhibits the infinite sequence of complex poles of the function in logarithmic space.

For any $r>0$ and $x>0$:

$$
\boxed{\; f(x;r,c) = \frac{1}{2x} \prod_{k=0}^{\infty} \left[ 1 + \left( \frac{2r\log(x/c)}{(2k+1)\pi} \right)^{2} \right]^{-1} \;}
$$

**Derivation:**

This elegant factorization is a direct geometric translation of the classical infinite product for the hyperbolic secant function, mediated by the Rosetta Stone identity.

1.  **Invoke the Rosetta Stone**:
    From §1.3, we know the core function is directly proportional to the hyperbolic secant in logarithmic coordinates:
    $$
    f(x;r,c) = \frac{1}{2x} \operatorname{sech}\bigl(r\log(x/c)\bigr)
    $$

2.  **The Weierstrass Product for Secant**:
    The classical Weierstrass infinite product factorization for the hyperbolic secant (which is closely related to Euler's infinite product for the cosine function via $z \mapsto iz$) is:
    $$
    \operatorname{sech}(z) = \prod_{k=0}^{\infty} \left[ 1 + \left( \frac{2z}{(2k+1)\pi} \right)^{2} \right]^{-1}
    $$
    This formula explicitly shows that $\operatorname{sech}(z)$ has no zeros, and has poles where the terms in the brackets vanish: $z = \pm i \frac{(2k+1)\pi}{2}$.

3.  **Substitute and Finalize**:
    Substitute the canonical coordinate $z = r\log(x/c)$ into the infinite product:
    $$
    \operatorname{sech}\bigl(r\log(x/c)\bigr) = \prod_{k=0}^{\infty} \left[ 1 + \left( \frac{2r\log(x/c)}{(2k+1)\pi} \right)^{2} \right]^{-1}
    $$
    Multiply by the $\frac{1}{2x}$ prefactor to recover $f(x;r,c)$, immediately yielding the boxed formula.

**Significance:**
This product formula provides an alternative method for numerically evaluating the function, particularly when $x$ is near $c$ (where the product converges rapidly). More profoundly, it shows that the underlying hyperbolic geometry of the function can be perfectly reconstructed by multiplying an infinite sequence of simple, resonance-like rational filters applied to the logarithmic distance from the median.

***

### Unifying Remark — §8

This section explores the structural "DNA" of the function family by decomposing it into its fundamental building blocks. Because of the singularity structure, a single global description is impossible, requiring different tools for different geometric perspectives:
1.  **Global Asymptotics (§8.1):** The complementary geometric power series perfectly capture the power-law tails outside the symmetry point.
2.  **Local Geometry (§8.2):** The Taylor series, governed by the Euler numbers, perfectly captures the curvature and local behavior around the exact center.
3.  **Additive Pole Structure (§8.3, §8.4):** The partial fraction decompositions break the function into a discrete, uniform sum of its resonances (poles) in the standard linear $x$-space (for integer $r$).
4.  **Multiplicative Pole Structure (§8.6):** The Weierstrass product breaks the function into an infinite product of resonances in the logarithmic coordinate space (for all $r>0$).
5.  **The Unifying Bridge (§8.5):** The Chebyshev discrete orthogonality identity proves that these different representations are not isolated; the discrete complex poles of the partial fractions are perfectly phase-locked to generate the global geometric power series.
