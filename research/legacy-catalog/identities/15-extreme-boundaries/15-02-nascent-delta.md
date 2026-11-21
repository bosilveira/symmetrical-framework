This is the perfect geometric counterpoint to the $r \to 0^+$ limit. While the $r \to 0$ limit diffuses the function into complete uncertainty (the Jeffreys prior), the $r \to \infty$ limit compresses it into absolute certainty, yielding the Dirac delta distribution.

Here is the revised and formatted version for your GitHub repository. I have expanded the "nascent delta" argument using the variance we computed in Section 7 to make the proof rigorously airtight.

***

### 15.2 The Point-Mass Limit ($r \to +\infty$)

As the shape parameter $r$ grows to infinity, the normalized probability density $\rho(x;r,c) = \frac{2r}{\pi}f(x;r,c)$ becomes infinitely peaked and infinitely narrow. In the limit, it converges to the **Dirac delta distribution** centered exactly at the scale parameter $c$.

In the sense of distributions (i.e., when integrated against a continuous test function):
$$
\boxed{\; \lim_{r \to \infty} \frac{2r}{\pi} f(x;r,c) = \delta(x-c) \;}
$$

**Derivation:**

To rigorously prove that a sequence of functions forms a nascent delta distribution (a Dirac sequence) at a point $x=c$, we must demonstrate three properties: it must maintain a constant unit area, its peak must converge to $c$, and its entire probability mass must concentrate arbitrarily close to $c$ as the parameter scales.

1.  **Conservation of Unit Mass:**
    From §1.7 and §3.3, the normalized density is constructed precisely so that its total integral is invariant with respect to $r$:
    $$
    \int_{0}^{\infty} \rho(x;r,c) \,\mathrm dx = \frac{2r}{\pi} \int_{0}^{\infty} f(x;r,c) \,\mathrm dx = \frac{2r}{\pi} \left( \frac{\pi}{2r} \right) = 1
    $$
    This holds true for all $r > 0$, and therefore holds in the limit.

2.  **Convergence of the Peak (Mode):**
    From §4.5, the unique interior maximum of the function is located at $x_{\max} = c\left(\frac{r-1}{r+1}\right)^{1/(2r)}$. We take the limit of this location as $r \to \infty$:
    $$
    \lim_{r \to \infty} x_{\max} = c \lim_{r \to \infty} \left( \frac{1 - 1/r}{1 + 1/r} \right)^{1/(2r)} = c \cdot (1)^0 = c
    $$
    The geometric peak of the distribution converges strictly to the symmetry point $c$.

3.  **Concentration of Measure (Variance Collapse):**
    The most rigorous way to show that the mass collapses to a single point is to examine its variance. It is easiest to do this in the canonical logarithmic coordinate $U = \log(X/c)$. 
    From §7.2, the exact variance of the logarithmic variable is:
    $$
    \operatorname{Var}(U) = \frac{\pi^2}{4r^2}
    $$
    As $r \to \infty$, the variance $\operatorname{Var}(U) \to 0$. 
    By Chebyshev's inequality, a variance of zero guarantees that the random variable $U$ equals its mean (which is $0$) with a probability of 1.
    If $U \to 0$ almost surely, then by the continuous mapping mapping $X = c e^U$, the variable $X \to c e^0 = c$ almost surely.

**Conclusion:**
Because the function maintains unit mass while its variance shrinks to zero around the point $x=c$, the sequence of densities strictly behaves as a Dirac delta function under integration:
$$
\lim_{r \to \infty} \int_{0}^{\infty} \phi(x) \rho(x;r,c) \,\mathrm dx = \phi(c)
$$
for any smooth test function $\phi(x)$.

**Physical Interpretation:**
In statistical terms, letting $r \to \infty$ corresponds to a transition from a probabilistic ensemble into a purely deterministic state. In the quantum mechanical context (§14), letting the shape parameter go to infinity corresponds to deepening the Pöschl-Teller potential well until the ground state wave function is perfectly localized at the geometric center.
