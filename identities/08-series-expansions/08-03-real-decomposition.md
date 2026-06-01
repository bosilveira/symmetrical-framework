This is a highly practical and algebraically beautiful result. For any integer shape parameter $r$, it breaks the function down into a finite sum of simple, resonance-like rational terms. This form is particularly useful for integration, inverse Laplace/Mellin transforms, and control theory applications where the function might represent a system's frequency response.

Here is the revised and formatted version for your GitHub repository.

***

### 8.3 Partial Fraction Decomposition (Real Form, Integer $r$)

When the shape parameter $r$ is a positive integer, the rational function $f(x; r, c)$ can be exactly expanded into a finite partial fraction decomposition. By grouping complex conjugate poles, this expansion can be written entirely in terms of real-valued quadratic components.

For an integer $r \ge 1$:
$$
\boxed{\; f(x;r,c) = \frac{c}{r} \sum_{k=0}^{r-1} \frac{(-1)^{k}\sin\theta_{k}}{x^{2}-2cx\cos\theta_{k}+c^{2}}, \qquad \text{where} \quad \theta_{k} = \frac{(2k+1)\pi}{2r} \;}
$$

**Derivation:**

The derivation uses complex residue calculus. Since the degree of the denominator ($2r$) is strictly greater than the degree of the numerator ($r-1$), the function equals the sum of its principal parts at each pole.

1.  **Find the Poles:**
The poles occur at the roots of the denominator: $c^{2r} + x^{2r} = 0$, which means $x^{2r} = -c^{2r}$.
The $2r$ distinct complex roots are given by:
$$
z_k = c \exp(i\theta_k) \qquad \text{where} \quad \theta_k = \frac{(2k+1)\pi}{2r}, \quad k = 0, 1, \dots, 2r-1
$$

2.  **Calculate the Residues:**
Let the numerator be $N(x) = c^r x^{r-1}$ and the denominator be $D(x) = c^{2r} + x^{2r}$. Because the poles are simple, the residue $A_k$ at $z_k$ is given by $A_k = \frac{N(z_k)}{D'(z_k)}$:
$$
A_k = \frac{c^r z_k^{r-1}}{2r z_k^{2r-1}} = \frac{c^r}{2r z_k^r}
$$
We evaluate $z_k^r$ using the definition of $z_k$:
$$
z_k^r = \left[ c \exp\left(i\frac{(2k+1)\pi}{2r}\right) \right]^r = c^r \exp\left(i\frac{(2k+1)\pi}{2}\right) = c^r i (-1)^k
$$
Substituting this back into the residue formula gives:
$$
A_k = \frac{c^r}{2r [c^r i (-1)^k]} = \frac{1}{2ir(-1)^k} = -i \frac{(-1)^k}{2r}
$$

3.  **Combine Complex Conjugate Pairs:**
The $2r$ poles form $r$ complex conjugate pairs. The sum over the upper half-plane poles ($k=0$ to $r-1$) paired with their conjugates is:
$$
f(x) = \sum_{k=0}^{r-1} \left( \frac{A_k}{x - z_k} + \frac{\bar{A}_k}{x - \bar{z}_k} \right)
$$
Combine each pair over a common denominator:
$$
\frac{A_k(x - \bar{z}_k) + \bar{A}_k(x - z_k)}{(x - z_k)(x - \bar{z}_k)} = \frac{(A_k + \bar{A}_k)x - (A_k\bar{z}_k + \bar{A}_k z_k)}{x^2 - (z_k + \bar{z}_k)x + z_k\bar{z}_k}
$$
Now, evaluate the coefficients using $A_k = -i \frac{(-1)^k}{2r}$ and $z_k = c(\cos\theta_k + i\sin\theta_k)$:
*   **Denominator:** $z_k + \bar{z}_k = 2c\cos\theta_k$ and $z_k\bar{z}_k = c^2$. This yields the required real quadratic factor $x^2 - 2cx\cos\theta_k + c^2$.
*   **Numerator $x$-coefficient:** $A_k + \bar{A}_k = -i\frac{(-1)^k}{2r} + i\frac{(-1)^k}{2r} = 0$. The $x$ term vanishes.
*   **Numerator Constant:** 
$$
- (A_k\bar{z}_k + \bar{A}_k z_k) = - \left[ \left(-i\frac{(-1)^k}{2r}\right) c e^{-i\theta_k} + \left(i\frac{(-1)^k}{2r}\right) c e^{i\theta_k} \right]
$$
$$
= c \frac{(-1)^k}{2r} i \left[ e^{-i\theta_k} - e^{i\theta_k} \right] = c \frac{(-1)^k}{2r} i \left[ -2i\sin\theta_k \right] = \frac{c}{r} (-1)^k \sin\theta_k
$$

4.  **Assemble the Final Sum:**
Substituting the evaluated numerator and denominator back into the sum yields the final boxed real-form identity.
