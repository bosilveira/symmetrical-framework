# 12.6 Connection to the Logistic Distribution

The symmetrical framework is intimately related to the classical Logistic distribution, yet distinct from it. The conformal phase $W(u)$ perfectly maps to the logistic CDF, while the square of the symmetrical density maps to the logistic PDF. The information-theoretic distance between these two fundamental distributions is a universal constant governed by Catalan's constant.

### The Algebraic Dictionary

Let $L(z) = 1/(1+e^{-z})$ be the standard logistic function.

*   **Conformal Phase as Logistic CDF:** $\boxed{ W(u) = \tanh(ru) = 2L(2ru) - 1 }$
*   **Squared Density as Logistic PDF:** $\boxed{ p(u;r)^2 = \frac{2r}{\pi^2} p_{\text{logistic}}\left(u; s=\frac{1}{2r}\right) }$

### The Entropy Gap

When matched at the same scale $s = 1/(2r)$, the difference in Shannon differential entropy between the Symmetrical (sech) distribution and the Logistic distribution is a universal information-geometric constant:

$$
\boxed{ H_{\text{sech}} - H_{\text{logistic}} = \frac{4G}{\pi} - 2 \approx 0.168 }
$$

*(where $G$ is Catalan's constant).*

### Exposition & Derivation

*The derivation will show that while both are symmetric, heavy-tailed distributions, the logistic distribution has slightly heavier tails (kurtosis 6/5 vs 2). The entropy gap exactly measures the "information distance" between the square-root of the logistic growth rate and the logistic growth rate itself.*
