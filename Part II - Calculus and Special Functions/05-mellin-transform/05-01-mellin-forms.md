## 5. The Mellin Transform — Hub of Algebraic Moments

The Mellin transform is a powerful integral transform that is particularly well-suited to analyzing functions with scaling or multiplicative symmetry. For our function family, the Mellin transform provides a single, compact analytic function that encapsulates all information about the function's algebraic moments. It serves as a central hub connecting the function's structure to the rich theories of the Euler Beta and Gamma functions.

### 5.1 The Mellin Transform — Four Equivalent Forms

The Mellin transform of $f(x;r,c)$, denoted $\mathcal{M}\{f\}(s)$, is a function of the complex variable `s`. It has four equivalent closed-form expressions.

Let $z_1 := \frac{r+s-1}{2r}$ and $z_2 := \frac{r-s+1}{2r}$. Note that these arguments satisfy the fundamental relation $z_1 + z_2 = 1$. The Mellin transform is given by:

$$
\boxed{\ 
\begin{align*}
\mathcal{M}\{f\}(s) &= \frac{c^{s-1}}{2r} B(z_1, z_2) \\
&= \frac{c^{s-1}}{2r} \Gamma(z_1) \Gamma(z_2) \\
&= \frac{\pi c^{s-1}}{2r \sin(\pi z_1)} \\
&= \frac{\pi c^{s-1}}{2r} \sec\left(\frac{(s-1)\pi}{2r}\right)
\end{align*}
\ }
$$

This result is valid for complex `s` within the vertical strip $1-r < \text{Re}(s) < 1+r$.

---
**Derivation of the Primary Beta Form:**

The first form is derived by direct integration using the same substitution that proved essential for the $L^n$ norms.

1.  **Start with the Definition of the Mellin Transform**:

$$
\mathcal{M}\{f\}(s) = \int_{0}^{\infty} x^{s-1} f(x;r,c) \,dx = \int_{0}^{\infty} x^{s-1} \frac{c^r x^{r-1}}{c^{2r}+x^{2r}} \,dx = c^r \int_{0}^{\infty} \frac{x^{s+r-2}}{c^{2r}+x^{2r}} \,dx
$$

2.  **Apply the Standard Substitution**: Let $u = (x/c)^{2r}$. As shown in §3.5, this implies $x = c u^{1/(2r)}$ and $dx = \frac{c}{2r} u^{\frac{1}{2r}-1} du$.
3.  **Transform the Integral**: Substitute `x` and `dx` into the integral expression:

$$
\mathcal{M}\{f\}(s) = c^r \int_{0}^{\infty} \frac{(c u^{1/(2r)})^{s+r-2}}{c^{2r}(1+u)} \left( \frac{c}{2r} u^{\frac{1}{2r}-1} du \right)
$$

Group the constants and combine the powers of `u`:
*   Constants: $c^r \cdot c^{s+r-2} \cdot \frac{1}{c^{2r}} \cdot \frac{c}{2r} = \frac{c^{2r+s-2-2r+1}}{2r} = \frac{c^{s-1}}{2r}$
*   `u` exponent: $\frac{s+r-2}{2r} + \left(\frac{1}{2r}-1\right) = \frac{s+r-2+1}{2r}-1 = \frac{s+r-1}{2r}-1 = z_1 - 1$
4.  **Identify the Beta Function**: The transformed integral is now:

$$
\mathcal{M}\{f\}(s) = \frac{c^{s-1}}{2r} \int_{0}^{\infty} \frac{u^{z_1-1}}{1+u} \,du
$$

The integral is a standard representation of the Beta function, $B(p,q) = \int_0^\infty \frac{u^{p-1}}{(1+u)^{p+q}}du$. In our case, the denominator is $(1+u)^1$, so $p+q=1$. We identify $p=z_1$, which means $q = 1-z_1 = z_2$. The integral is therefore $B(z_1, z_2)$.

---
**Derivation of the Equivalent Forms:**

The other three forms are direct consequences of standard identities for the Beta and Gamma functions.

*   **Beta to Gamma Form**: The relationship $B(p,q) = \frac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}$ is used. Since $z_1+z_2=1$, the denominator is $\Gamma(1)=1$, so $B(z_1,z_2) = \Gamma(z_1)\Gamma(z_2)$.
*   **Gamma to Sine Form**: This follows from **Euler's reflection formula**, $\Gamma(z)\Gamma(1-z) = \frac{\pi}{\sin(\pi z)}$. Since $z_2 = 1-z_1$, we have $\Gamma(z_1)\Gamma(z_2) = \frac{\pi}{\sin(\pi z_1)}$.
*   **Sine to Secant Form**: This is a simple trigonometric identity. We expand $z_1$:

$$
\sin(\pi z_1) = \sin\left(\pi \frac{r+s-1}{2r}\right) = \sin\left(\frac{\pi}{2} + \frac{(s-1)\pi}{2r}\right)
$$

Using the co-function identity $\sin(\pi/2 + \theta) = \cos(\theta)$, this becomes $\cos\left(\frac{(s-1)\pi}{2r}\right)$. The reciprocal is the secant, giving the final form.

**Strip of Convergence:**

The integral defining the Mellin transform converges only when the real part of `s` is within a specific range. This range is determined by the function's power-law asymptotic behavior from §1.1: $f(x) \sim x^{r-1}$ as $x\to 0$ and $f(x) \sim x^{-r-1}$ as $x\to\infty$. For the integral $\int_0^\infty x^{s-1}f(x)dx$ to converge, we need:
*   Near $x=0$: $\text{Re}(s-1) + (r-1) > -1 \implies \text{Re}(s) > 1-r$.
*   Near $x=\infty$: $\text{Re}(s-1) + (-r-1) < -1 \implies \text{Re}(s) < 1+r$.
Combining these gives the strip of convergence $1-r < \text{Re}(s) < 1+r$.
