# 9.5 Chebyshev Discrete Orthogonality

By equating the real-form partial fraction decomposition (§9.3) with the inner geometric power series (§9.1), we uncover a remarkable discrete orthogonality identity. This identity involves a weighted sum of the **Chebyshev polynomials of the second kind**, $U_n(x)$, evaluated at a discrete set of points derived from the angles of the function's complex poles.

For any integer $r \ge 1$ and non-negative integer $n$, let $\theta_k = \frac{(2k+1)\pi}{2r}$. The sum over the discrete angles evaluates to:

$$
\boxed{ \sum_{k=0}^{r-1} (-1)^{k}\sin\theta_{k}\,U_{n}(\cos\theta_{k}) = 
\begin{cases} 
r(-1)^{m}, & \text{if } n = r(2m+1)-1 \text{ for integer } m \ge 0\\ 
0, & \text{otherwise} 
\end{cases} }
$$

### Exposition

This identity demonstrates a deep connection between the algebraic structure of the function family (for integer $r$) and the classical theory of orthogonal polynomials. It arises because two vastly different series representations for the same function must have identical coefficients. The right-hand side acts as a "selection rule," indicating that the weighted sum of Chebyshev polynomials is non-zero only for a specific, arithmetically defined subsequence of polynomial degrees $n$.

### Derivation

The derivation relies on using the generating function for Chebyshev polynomials to expand the partial fraction components, and then performing a coefficient-by-coefficient matching with the geometric series.

**Step 1: Expand the Partial Fraction Summands using Chebyshev Polynomials**

Recall the real-form partial fraction decomposition from §9.3 for integer $r$:

$$
f(x;r,c) = \frac{c}{r} \sum_{k=0}^{r-1} \frac{(-1)^k \sin\theta_k}{x^2 - 2cx\cos\theta_k + c^2}
$$

The generating function for the Chebyshev polynomials of the second kind, $U_n(y)$, is:

$$
\frac{1}{1 - 2yt + t^2} = \sum_{n=0}^{\infty} U_n(y) t^n
$$

To apply this, we factor $c^2$ from the denominator of our summand to create the ratio $t = x/c$:

$$
\frac{1}{x^2 - 2cx\cos\theta_k + c^2} = \frac{1}{c^2} \left[ \frac{1}{1 - 2\cos\theta_k \left(\frac{x}{c}\right) + \left(\frac{x}{c}\right)^2} \right]
$$

Using the generating function with $y = \cos\theta_k$ and $t = x/c$, this becomes:

$$
\frac{1}{c^2} \sum_{n=0}^{\infty} U_n(\cos\theta_k) \left(\frac{x}{c}\right)^n
$$

**Step 2: Assemble the Power Series from the Partial Fraction Decomposition**

Substitute this expansion back into the sum from Step 1:

$$
f(x;r,c) = \frac{c}{r} \sum_{k=0}^{r-1} (-1)^k \sin\theta_k \left[ \frac{1}{c^2} \sum_{n=0}^{\infty} U_n(\cos\theta_k) \left(\frac{x}{c}\right)^n \right]
$$

By swapping the order of summation (which is permissible within the radius of convergence), we can group terms by powers of $(x/c)$:

$$
f(x;r,c) = \frac{1}{rc} \sum_{n=0}^{\infty} \left[ \sum_{k=0}^{r-1} (-1)^k \sin\theta_k \,U_n(\cos\theta_k) \right] \left(\frac{x}{c}\right)^n
$$

**Step 3: Match Coefficients with the Inner Geometric Series**

From §9.1, we have the exact geometric power series for the inner domain ($0 < x < c$):

$$
f(x;r,c) = \sum_{m=0}^{\infty} (-1)^m c^{-r(2m+1)} x^{r(2m+1)-1}
$$

To compare coefficients, we must rewrite this series in powers of $(x/c)^n$. We factor out $1/c$:

$$
f(x;r,c) = \frac{1}{c} \sum_{m=0}^{\infty} (-1)^m \left(\frac{x}{c}\right)^{r(2m+1)-1}
$$

**Step 4: Equate Coefficients**

The two power series from Step 2 and Step 3 are alternative representations of the exact same function $f(x;r,c)$ on the interval $(0, c)$. Therefore, their coefficients for each power of $(x/c)^n$ must be identical.

*   **From the geometric series:** The coefficient of $\frac{1}{c}(x/c)^n$ is $(-1)^m$ if the power $n$ is of the form $n = r(2m+1)-1$ for some integer $m \ge 0$. If $n$ is not of this form, the term is absent, and its coefficient is $0$.
*   **From the Chebyshev expansion:** The coefficient of $\frac{1}{c}(x/c)^n$ is exactly $\frac{1}{r} \sum_{k=0}^{r-1} (-1)^k \sin\theta_k \,U_n(\cos\theta_k)$.

Equating these coefficients and multiplying both sides by $r$ immediately yields the boxed discrete orthogonality identity.
