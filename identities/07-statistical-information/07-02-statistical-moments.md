### 7.2 Variance, Skewness, and Kurtosis

Using the exact log-cumulants derived in §7.1, we can compute the standard statistical moments for the logarithmic variable $U = \log(X/c)$. These metrics reveal a distribution that is perfectly symmetric but possesses "heavier tails" than a normal distribution.

*   **Variance ($Var$):** $\frac{\pi^2}{4r^2}$
*   **Skewness ($\gamma_1$):** $0$
*   **Excess Kurtosis ($\gamma_2$):** $2$
*   **Pearson Kurtosis ($\beta_2$):** $5$ (Universal Constant)

**Derivations:**

These values follow directly from the definitions of standardized moments in terms of cumulants ($\kappa_n$):

1.  **Variance**: The variance is exactly the second cumulant. Using $T_1 = 1$:

$$
Var(U) = \kappa_2 = T_1 \left(\frac{\pi}{2r}\right)^2 = \frac{\pi^2}{4r^2}
$$

2.  **Skewness**: Skewness is defined as $\gamma_1 = \kappa_3 / \kappa_2^{3/2}$. Because the distribution of $U$ is an even function (symmetric about 0), all odd-order cumulants vanish ($\kappa_3 = 0$). Therefore, the skewness is exactly $0$.
3.  **Excess Kurtosis**: Excess kurtosis is defined as $\gamma_2 = \kappa_4 / \kappa_2^2$. Using $T_1 = 1$ and $T_2 = 2$:
$$
\gamma_2 = \frac{T_2 (\pi / 2r)^4}{\left[ T_1 (\pi / 2r)^2 \right]^2} = \frac{T_2}{T_1^2} = \frac{2}{1^2} = 2
$$
4.  **Pearson Kurtosis**: Pearson kurtosis (the raw fourth standardized moment) is defined as $\beta_2 = \gamma_2 + 3$, where 3 is the baseline kurtosis of a standard Gaussian distribution.
$$
\beta_2 = 2 + 3 = 5
$$

**Significance:**

The Pearson kurtosis of $5$ reveals that the logarithmic distribution is strictly **leptokurtic** (kurtosis $> 3$). It has a sharper peak and fatter tails than a normal distribution. Remarkably, because the scale parameter `c` was absorbed into the definition of `U`, and the shape parameter `r` cancels out entirely in the ratio $\kappa_4/\kappa_2^2$, this kurtosis of 5 is a **universal geometric invariant** for every single member of this function family.
