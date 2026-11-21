This is an excellent transition into the final analytical sections. Examining the asymptotic limits of the shape parameter $r$ reveals the boundary behaviors of the family, connecting it to fundamental non-normalizable distributions and Dirac delta functions.

Here is the revised and formatted version for your GitHub repository.

***

## 15. Limits and Special Cases

Having established the general properties of the function family for $r > 0$, we now examine its behavior at the extreme boundaries of the parameter space. These limits reveal how the function connects to universal distributions and scale-invariant measures.

### 15.1 The Scale-Invariant Limit ($r \to 0^{+}$)

As the shape parameter $r$ approaches zero, the function flattens out, losing its distinct peak and its dependence on the scale parameter $c$. It converges pointwise to the fundamental scale-invariant measure on the positive half-line.

$$
\boxed{\; \lim_{r \to 0^{+}} f(x; r, c) = \frac{1}{2x} \;}
$$

**Derivation:**

The pointwise limit is found by taking the limit of each algebraic component of the core definition as $r \to 0^+$. Assuming $x$ and $c$ are strictly positive and finite:

1.  **Numerator Limits**:
    *   $\lim_{r \to 0^+} c^r = c^0 = 1$
    *   $\lim_{r \to 0^+} x^{r-1} = x^{0-1} = \frac{1}{x}$
    The numerator converges to $1/x$.

2.  **Denominator Limit**:
    *   $\lim_{r \to 0^+} (c^{2r} + x^{2r}) = c^0 + x^0 = 1 + 1 = 2$

3.  **Combine Results**:
    $$
    \lim_{r \to 0^+} f(x; r, c) = \frac{1 \cdot (1/x)}{2} = \frac{1}{2x}
    $$

**Physical and Statistical Significance:**

*   **Divergence of Mass:** While the pointwise limit is a simple inverse function, the total probability mass diverges. From §3.3, the total mass is $\pi/(2r)$. As $r \to 0^+$, the total mass approaches infinity ($\pi/(2r) \to \infty$). The distribution becomes non-normalizable.
*   **The Jeffreys Prior:** The resulting function $1/(2x)$ is proportional to $1/x$, which is the classic **Jeffreys prior** for a scale parameter in Bayesian statistics. It represents a state of complete ignorance regarding the scale.
*   **The Haar Measure connection:** As explored in §1.6, $dx/x$ is the translation-invariant Haar measure on the multiplicative group of positive reals. In this limit, the function strips away all localized shape and becomes the pure geometric measure of the space itself. It acts as the multiplicative analogue of a flat (uniform) logarithmic potential.
