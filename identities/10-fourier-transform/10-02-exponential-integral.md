This is a highly sophisticated result. While §10.1 dealt with the Fourier transform in the logarithmic coordinate $u$, this section attacks the standard, linear one-sided Fourier transform over the domain $x \in (0, \infty)$. 

For integer $r$, reducing the function to its partial fraction decomposition allows for exact integration, yielding a closed-form solution in terms of the exponential integral $E_1$. The explicit handling of the branch cut correction is a hallmark of rigorous complex analysis.

Here is the revised and formatted version for your GitHub repository.

***

### 10.2 One-Sided Fourier Transform via the Exponential Integral $E_1$

While the logarithmic Fourier transform yields hyperbolic functions, the standard linear one-sided Fourier transform, $\widehat{f}(\omega) = \int_0^\infty f(x) e^{-i\omega x} dx$, of this family results in a superposition of special functions. 

For integer shape parameters $r \ge 1$ and positive angular frequency $\omega > 0$, the exact one-sided Fourier transform is given by:

$$
\boxed{\; \widehat f(\omega;r,c) = -\frac{i}{2r}\sum_{k=0}^{2r-1}(-1)^{k}I(\omega;z_{k}) \;}
$$
where $z_{k} = c e^{i(2k+1)\pi/(2r)}$ are the poles of the function (as in §8.4), and the integral component is defined as:
$$
I(\omega;z) := e^{-i\omega z}E_{1}(-i\omega z) - 2\pi i\,e^{-i\omega z}\cdot\mathbb{1}\bigl[\operatorname{Re} z > 0 \text{ and } \operatorname{Im} z < 0\bigr]
$$
Here, $E_{1}(z) = \int_z^\infty \frac{e^{-t}}{t}dt$ is the standard exponential integral, and $\mathbb{1}[\cdot]$ is the indicator function.

**Derivation:**

The derivation relies on integrating the complex partial fraction decomposition of the function term by term.

1.  **Recall the Complex PFD:**
    From §8.4, the function for integer $r$ can be expressed as a sum over its simple poles:
    $$
    f(x;r,c) = -\frac{i}{2r}\sum_{k=0}^{2r-1}\frac{(-1)^{k}}{x-z_{k}}
    $$
    
2.  **Apply the Fourier Integral:**
    Because the integral is a linear operator, we can apply the one-sided Fourier transform to the sum term-by-term:
    $$
    \widehat f(\omega;r,c) = \int_{0}^{\infty} f(x) e^{-i\omega x} \,\mathrm dx = -\frac{i}{2r}\sum_{k=0}^{2r-1} (-1)^{k} \int_{0}^{\infty} \frac{e^{-i\omega x}}{x-z_{k}} \,\mathrm dx
    $$

3.  **Evaluate the Fundamental Integral:**
    The core challenge is evaluating the integral $\int_{0}^{\infty} \frac{e^{-i\omega x}}{x-z} \,\mathrm dx$ for a generic complex pole $z$.
    This is a known identity related to the exponential integral $E_1$ (see, for instance, Abramowitz & Stegun, Eq. 5.1.28). Through a change of variables $t = i\omega(x-z)$, the integral transforms into the standard form:
    $$
    \int_{0}^{\infty} \frac{e^{-i\omega x}}{x-z} \,\mathrm dx = e^{-i\omega z} E_{1}(-i\omega z)
    $$

4.  **The Branch Cut Correction:**
    The function $E_1(W)$ has a principal branch cut extending along the negative real axis. When we substitute $W = -i\omega z$, we must carefully track the trajectory of the arguments in the complex plane to ensure we remain on the correct principal branch.
    
    *   For a pole $z_k$ located in the first, second, or third quadrants, the analytic continuation of the integral definition smoothly matches the principal branch of $E_1(-i\omega z_k)$.
    *   However, if the pole lies in the **fourth quadrant** (where the real part is positive, $\operatorname{Re} z_k > 0$, and the imaginary part is negative, $\operatorname{Im} z_k < 0$), the argument $W = -i\omega z_k$ crosses the branch cut of $E_1$. 
    
    To compensate for crossing this discontinuity and maintain the exact analytic continuation of the definite integral, a correction term of $-2\pi i$ multiplied by the exponential prefactor is rigorously required. This is encapsulated by the indicator function $\mathbb{1}[\operatorname{Re} z > 0, \operatorname{Im} z < 0]$.

Substituting this fully corrected evaluation of the integral back into the sum from Step 2 yields the final boxed formula.
