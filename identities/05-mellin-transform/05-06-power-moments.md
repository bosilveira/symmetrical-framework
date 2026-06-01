### 5.6 Power Moments and the Mellin Characteristic Function

The ultimate purpose of the Mellin transform in this context is to serve as a moment-generating function. By evaluating the transform of the normalized density $\rho(x)$ at specific integer points, we can instantly read off all of the distribution's power moments.

For any real moment `n` such that $|n|<r$, the expected value of $X^n$ is:

$$
\boxed{ \langle X^n \rangle := \mathbb{E}[X^n] = c^n \sec\left(\frac{n\pi}{2r}\right) }
$$

This leads to a universal "characteristic function" for the dimensionless variable $X/c$:

$$
\mathbb{E}\left[\left(\frac{X}{c}\right)^t\right] = \sec\left(\frac{t\pi}{2r}\right), \quad \text{for |t|\<r } 
$$

---
**Derivation:**

The derivation connects the statistical definition of a moment to the analytical definition of the Mellin transform.

1.  **Relate Moments to the Mellin Transform**:  
The $n$-th power moment of a random variable `X` described by the probability density $\rho(x)$ is defined as:
$$
\langle X^n \rangle = \int_0^\infty x^n \rho(x) \,dx
$$
By comparing this to the definition of the Mellin transform, $\mathcal{M}\{g\}(s) = \int_0^\infty x^{s-1} g(x) dx$, we see that the $n$-th moment is precisely the Mellin transform of the density $\rho(x)$ evaluated at $s=n+1$:
$$
\langle X^n \rangle = \mathcal{M}\{\rho\}(s=n+1)
$$

2.  **Find the Mellin Transform of the Density $\rho(x)$**:  
From §1.7, the normalized density is $\rho(x) = \frac{2r}{\pi} f(x)$. Since the Mellin transform is a linear operator, we have:
$$
\mathcal{M}\{\rho\}(s) = \frac{2r}{\pi} \mathcal{M}\{f\}(s)
$$
Using the final secant form for $\mathcal{M}\{f\}(s)$ from §5.1, this becomes:
$$
\mathcal{M}\{\rho\}(s) = \frac{2r}{\pi} \left[ \frac{\pi c^{s-1}}{2r} \sec\left(\frac{(s-1)\pi}{2r}\right) \right] = c^{s-1} \sec\left(\frac{(s-1)\pi}{2r}\right)
$$

3.  **Evaluate at $s=n+1$**:  
We now substitute $s=n+1$ into this expression to find the moment:
$$
\langle X^n \rangle = c^{(n+1)-1} \sec\left(\frac{((n+1)-1)\pi}{2r}\right) = c^n \sec\left(\frac{n\pi}{2r}\right)
$$
This completes the derivation of the first identity.

4.  **Derive the Dimensionless Form**:  
The second identity follows directly. The expected value of $(X/c)^t$ is:
$$
\mathbb{E}\left[\left(\frac{X}{c}\right)^t\right] = \mathbb{E}\left[\frac{X^t}{c^t}\right] = \frac{1}{c^t}\mathbb{E}[X^t] = \frac{1}{c^t} \langle X^t \rangle
$$
Substituting our result for $\langle X^t \rangle$:
$$
\mathbb{E}\left[\left(\frac{X}{c}\right)^t\right] = \frac{1}{c^t} \left[ c^t \sec\left(\frac{t\pi}{2r}\right) \right] = \sec\left(\frac{t\pi}{2r}\right)
$$

**Condition for Existence of Moments:**

The moments are finite only when the Mellin transform integral converges. This requires the evaluation point, $s=n+1$, to be within the strip of convergence for $\mathcal{M}\{f\}(s)$, which was established in §5.1 as $1-r < \text{Re}(s) < 1+r$.
Substituting $s=n+1$ gives:
$$
1-r < n+1 < 1+r
$$
Subtracting 1 from all parts yields the condition:
$$
-r < n < r \quad \text{or} \quad |n|<r
$$
This provides a clear physical interpretation: the parameter `r` defines the range of finite moments. As the argument of the secant, $\frac{n\pi}{2r}$, approaches $\pm \pi/2$ (i.e., as $|n| \to r$), the secant function diverges, and the moments become infinite, precisely as predicted by the convergence condition.
