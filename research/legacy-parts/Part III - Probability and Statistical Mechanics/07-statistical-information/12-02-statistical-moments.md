# 12.2 Variance, Skewness, and Universal Kurtosis

Using the exact log-cumulants, we can compute the standard statistical moments for the logarithmic variable $U = \log(X/c)$. These metrics reveal a distribution that is perfectly symmetric but possesses "heavier tails" than a standard normal distribution.

For the variable $U = \log(X/c)$, the standardized statistical moments are:

*   **Variance:** $\boxed{\; \kappa_2 = \frac{\pi^2}{4r^2} \;}$
*   **Skewness:** $\boxed{\; \gamma_1 = 0 \;}$
*   **Pearson Kurtosis:** $\boxed{\; \beta_2 = 5 \;} \quad$ *(A Universal Constant)*

### Exposition

The Pearson kurtosis of $5$ reveals that the logarithmic distribution is strictly **leptokurtic** (kurtosis $> 3$). It has a sharper peak and fatter tails than a Gaussian distribution. Remarkably, because the scale parameter $c$ was absorbed into the definition of $U$, and the shape parameter $r$ cancels out entirely in the kurtosis ratio, this value of 5 is a **universal geometric invariant** for every single member of this function family.

### Derivations

These values follow directly from the definitions of standardized moments in terms of cumulants ($\kappa_n$), evaluated using the generating formula $\kappa_{2n} = T_n (\pi / 2r)^{2n}$.

**Step 1: Variance**

The variance is exactly the second cumulant. Using $T_1 = 1$:

$$
\text{Var}(U) = \kappa_2 = T_1 \left(\frac{\pi}{2r}\right)^2 = \frac{\pi^2}{4r^2}
$$

**Step 2: Skewness**

Skewness is defined as $\gamma_1 = \kappa_3 / \kappa_2^{3/2}$. Because the distribution of $U$ is an even function (symmetric about 0), all odd-order cumulants vanish ($\kappa_3 = 0$). Therefore, the skewness is identically $0$.

**Step 3: Excess Kurtosis**

Excess kurtosis is defined as $\gamma_2 = \kappa_4 / \kappa_2^2$. Using $T_1 = 1$ and $T_2 = 2$:

$$
\gamma_2 = \frac{T_2 (\pi / 2r)^4}{\left[ T_1 (\pi / 2r)^2 \right]^2} = \frac{T_2}{T_1^2} = \frac{2}{1^2} = 2
$$

**Step 4: Pearson Kurtosis**

Pearson kurtosis (the raw fourth standardized moment) is defined as $\beta_2 = \gamma_2 + 3$, where 3 is the baseline kurtosis of a standard Gaussian distribution.

$$
\beta_2 = 2 + 3 = 5
$$

This completes the derivation.
