# 6.1 The Mellin Transform in Four Equivalent Forms

The Mellin transform is an integral transform that is particularly well-suited to analyzing functions with multiplicative or scaling symmetry. For the symmetrical function, the Mellin transform provides a single, compact analytic function that encapsulates all information about the function's algebraic moments. It has four equivalent closed-form expressions.

Let the complex variable be $s$, and define the dependent variables $z_1 := \frac{r+s-1}{2r}$ and $z_2 := \frac{r-s+1}{2r}$. Note that these arguments satisfy the fundamental relation $z_1 + z_2 = 1$. The Mellin transform of $f(x;r,c)$, denoted $\mathcal{M}\{f\}(s)$, is given by:

$$
\boxed{
\begin{align*}
\mathcal{M}\{f\}(s) &= \frac{c^{s-1}}{2r} B(z_1, z_2) \\
&= \frac{c^{s-1}}{2r} \Gamma(z_1) \Gamma(z_2) \\
&= \frac{\pi c^{s-1}}{2r \sin(\pi z_1)} \\
&= \frac{\pi c^{s-1}}{2r} \sec\left(\frac{(s-1)\pi}{2r}\right)
\end{align*}
}
$$

This result is valid for complex $s$ within the vertical strip of convergence defined by $1-r < \mathrm{Re}(s) < 1+r$.

### Exposition
These four equivalent forms provide a complete analytic description of the function in the Mellin domain. Each form is useful in different contexts: the Beta form arises naturally from direct integration; the Gamma form connects to the theory of special functions and residue calculus; the sine form relates to Euler's reflection formula; and the secant form is the most compact, revealing the pole structure and connection to Fourier analysis.

### Derivation of the Primary Beta Form

**Step 1:** Start with the definition of the Mellin Transform:

$$
\mathcal{M}\{f\}(s) = \int_{0}^{\infty} x^{s-1} f(x;r,c) \,\mathrm{d}x = \int_{0}^{\infty} x^{s-1} \frac{c^r x^{r-1}}{c^{2r}+x^{2r}} \,\mathrm{d}x = c^r \int_{0}^{\infty} \frac{x^{s+r-2}}{c^{2r}+x^{2r}} \,\mathrm{d}x
$$

**Step 2:** Apply the standard substitution $u = (x/c)^{2r}$, which implies $x = c u^{1/(2r)}$ and $\mathrm{d}x = \frac{c}{2r} u^{\frac{1}{2r}-1} \mathrm{d}u$.

**Step 3:** Transform the integral in terms of $u$:

$$
\mathcal{M}\{f\}(s) = c^r \int_{0}^{\infty} \frac{(c u^{1/(2r)})^{s+r-2}}{c^{2r}(1+u)} \left( \frac{c}{2r} u^{\frac{1}{2r}-1} \mathrm{d}u \right)
$$

**Step 4:** Group the constants and combine the powers of $u$.
*   Constants: $c^r \cdot c^{s+r-2} \cdot c^{-2r} \cdot \frac{c}{2r} = \frac{c^{s-1}}{2r}$
*   `u` exponent: $\frac{s+r-2}{2r} + \left(\frac{1}{2r}-1\right) = \frac{s+r-1}{2r}-1 = z_1 - 1$

**Step 5:** The integral becomes:

$$
\mathcal{M}\{f\}(s) = \frac{c^{s-1}}{2r} \int_{0}^{\infty} \frac{u^{z_1-1}}{1+u} \,\mathrm{d}u
$$

This integral is a standard representation of the Beta function, $B(p,q) = \int_0^\infty \frac{u^{p-1}}{(1+u)^{p+q}}\mathrm{d}u$, with $p=z_1$ and $p+q=1$, which implies $q=1-z_1=z_2$.

### Derivation of the Equivalent Forms

The other forms are direct consequences of standard identities for the Beta and Gamma functions.
*   **Gamma Form:** Use $B(p,q) = \frac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}$. Since $z_1+z_2=1$, the denominator is $\Gamma(1)=1$.
*   **Sine Form:** Use **Euler's reflection formula**, $\Gamma(z)\Gamma(1-z) = \frac{\pi}{\sin(\pi z)}$. Since $z_2 = 1-z_1$, we have $\Gamma(z_1)\Gamma(z_2) = \frac{\pi}{\sin(\pi z_1)}$.
*   **Secant Form:** Use the co-function identity $\sin(\pi z_1) = \sin\left(\pi (\frac{r+s-1}{2r})\right) = \sin\left(\frac{\pi}{2} + \frac{(s-1)\pi}{2r}\right) = \cos\left(\frac{(s-1)\pi}{2r}\right)$. The reciprocal of cosine is secant.

### Derivation of the Strip of Convergence

The integral $\int_0^\infty x^{s-1}f(x)\mathrm{d}x$ converges if the integrand is appropriately bounded at $x\to 0$ and $x\to\infty$. Using the asymptotic tails from §1.9:
*   Near $x=0$: $x^{s-1}f(x) \sim x^{\mathrm{Re}(s)-1} x^{r-1} = x^{\mathrm{Re}(s)+r-2}$. For convergence, we need the exponent to be greater than $-1$, so $\mathrm{Re}(s)+r-2 > -1 \implies \mathrm{Re}(s) > 1-r$.
*   Near $x=\infty$: $x^{s-1}f(x) \sim x^{\mathrm{Re}(s)-1} x^{-r-1} = x^{\mathrm{Re}(s)-r-2}$. For convergence, we need the exponent to be less than $-1$, so $\mathrm{Re}(s)-r-2 < -1 \implies \mathrm{Re}(s) < 1+r$.

Combining these gives the strip of convergence $1-r < \mathrm{Re}(s) < 1+r$.
