# 13.6 The Log-Normal Asymptotic Limit

As the number of independent interacting components $n$ goes to infinity, the exact $n$-fold multiplicative convolution of the framework asymptotically approaches the **Log-Normal distribution**. This is the multiplicative analogue of the Central Limit Theorem (CLT).

Let $X_1, X_2, \dots, X_n$ be i.i.d. random variables drawn from the normalized distribution $\rho(x;r,c)$. Let $P_n = \prod_{i=1}^n X_i$ be their product. As $n \to \infty$, the standardized logarithmic product converges in distribution to a standard normal variable $\mathcal{N}(0,1)$:

$$
\boxed{\; \lim_{n \to \infty} \frac{\log(P_n / c^n)}{\frac{\pi}{2r} \sqrt{n}} \sim \mathcal{N}(0,1) \;}
$$

### Exposition

While finite convolutions ($n=2, 3$) preserve the fundamental hyperbolic secant structure modulated by polynomials (as seen in §13.1 and §13.4), infinite iteration completely washes away the specific `sech` geometry. The system unavoidably falls into the basin of attraction of the Log-Normal distribution. The scaling factor $\frac{\pi}{2r}\sqrt{n}$ perfectly captures how the standard deviation of the system grows with each interaction.

### Derivation

The derivation relies on translating the product into a sum in the canonical logarithmic coordinate system and applying the classical Central Limit Theorem.

**Step 1: Translate to Logarithmic Coordinates**

Define the log-transformed variables $U_i = \log(X_i/c)$. As established in §1.10 and §12.2, the $U_i$ are independent and identically distributed with density $p(u) = \frac{r}{\pi}\operatorname{sech}(ru)$.

The variables $U_i$ have mean $\mu = 0$ and variance $\sigma^2 = \frac{\pi^2}{4r^2}$.

**Step 2: Formulate the Sum**

The logarithm of the scaled product is exactly the sum of these variables:

$$
\log\left(\frac{P_n}{c^n}\right) = \log\left(\prod_{i=1}^n \frac{X_i}{c}\right) = \sum_{i=1}^n \log\left(\frac{X_i}{c}\right) = \sum_{i=1}^n U_i
$$

**Step 3: Apply the Central Limit Theorem**

The classical Central Limit Theorem states that for a sequence of i.i.d. random variables with mean $\mu$ and finite variance $\sigma^2$, the standardized sum converges in distribution to a standard normal variable as $n \to \infty$:

$$
Z_n = \frac{\sum_{i=1}^n U_i - n\mu}{\sigma \sqrt{n}} \xrightarrow{d} \mathcal{N}(0,1)
$$

**Step 4: Substitute the Framework Parameters**

Substitute our specific mean ($\mu=0$) and standard deviation ($\sigma = \frac{\pi}{2r}$) into the CLT formula:

$$
Z_n = \frac{\log(P_n / c^n) - 0}{\left(\frac{\pi}{2r}\right) \sqrt{n}} = \frac{\log(P_n / c^n)}{\frac{\pi}{2r} \sqrt{n}}
$$

Therefore, this standardized ratio converges to $\mathcal{N}(0,1)$. This implies that the unstandardized product $P_n$ asymptotically follows a Log-Normal distribution with median $c^n$ and logarithmic variance $n \frac{\pi^2}{4r^2}$.
