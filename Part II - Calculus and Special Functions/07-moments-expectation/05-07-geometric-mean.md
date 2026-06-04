## 5.7 Geometric Mean

The geometric mean of a distribution is defined as the exponential of the expected value of the logarithm of the random variable, $\exp(\mathbb{E}[\log X])$. For the distribution $\rho(x)$, the geometric mean is exactly equal to the scale parameter `c`.

$$
\boxed{\; \exp\left(\langle\log X\rangle\right) = c \;}
$$

**Derivation:**

This result can be derived elegantly by differentiating the dimensionless moment-generating function (or "Mellin characteristic function") from §5.6 with respect to the moment order `t` and evaluating at `t=0`.

1.  **Recall the Dimensionless Moment Function**:
Let $M(t) = \mathbb{E}\left[\left(\frac{X}{c}\right)^t\right] = \sec\left(\frac{t\pi}{2r}\right)$.

2.  **Differentiate with Respect to t**: The derivative of $\mathbb{E}[Y^t]$ at $t=0$ yields $\mathbb{E}[\log Y]$. We apply this principle by differentiating both sides of the equation for $M(t)$.

*   **Left-Hand Side (LHS)**:
$$
\frac{d}{dt} \mathbb{E}\left[\left(\frac{X}{c}\right)^t\right]\Bigg|_{t=0} = \mathbb{E}\left[\log\left(\frac{X}{c}\right)\right] = \mathbb{E}[\log X - \log c] = \langle\log X\rangle - \log c
$$

*   **Right-Hand Side (RHS)**: We use the chain rule for differentiation.
$$
\frac{d}{dt} \sec\left(\frac{t\pi}{2r}\right) = \sec\left(\frac{t\pi}{2r}\right) \tan\left(\frac{t\pi}{2r}\right) \cdot \frac{\pi}{2r}
$$
Evaluating this derivative at $t=0$:
$$
\sec(0) \tan(0) \cdot \frac{\pi}{2r} = (1) \cdot (0) \cdot \frac{\pi}{2r} = 0
$$

3.  **Equate and Solve**: Equating the results from the LHS and RHS gives:
$$
\langle\log X\rangle - \log c = 0 \quad \implies \quad \langle\log X\rangle = \log c
$$

4.  **Exponentiate**: Exponentiating both sides yields the final identity:
$$
\exp(\langle\log X\rangle) = c
$$

**Alternative Derivation (via Logarithmic Symmetry):**

The same result can be seen more directly by considering the distribution in its canonical logarithmic coordinate system, $u = \log(x/c)$.

1.  From §1.6, the probability density for the variable `u` is $p(u) = \frac{1}{2}\mathrm{sech}(ru)$.
2.  The hyperbolic secant is an **even function**, meaning $p(-u) = p(u)$. The probability distribution for `u` is symmetric about the origin.
3.  The expected value of any random variable with a symmetric probability distribution is the point of symmetry. Therefore:
$$
\mathbb{E}[u] = 0
$$
4.  Substituting back the definition of `u`:
$$
\mathbb{E}\left[\log\left(\frac{X}{c}\right)\right] = 0
$$
As shown above, this leads directly to $\exp(\langle\log X\rangle) = c$. This confirms that the geometric mean being `c` is a direct consequence of the distribution's even symmetry in logarithmic space.
