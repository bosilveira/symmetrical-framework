# 11.2 Stieltjes Transform Closed Form for $r=1$

For the classical case where $r=1$ (the unnormalized Cauchy kernel), the Stieltjes transform along the negative real axis ($z = -x$, for $x > 0$) reduces to an elegant combination of elementary rational and logarithmic terms.

For $x>0$:

$$
\boxed{ S_{f}(-x;1,c) = \frac{\frac{\pi}{2}x - c\log(x/c)}{x^{2}+c^{2}} }
$$

### Exposition

This exact closed-form solution demonstrates that for the simplest member of the family, the complex integral transform yields elementary functions. The derivation relies on a standard partial fraction decomposition and a careful evaluation of the resulting improper integrals, paying close attention to the cancellation of logarithmic divergences at infinity. This formula provides a crucial, verifiable benchmark for the more complex series and Mellin-Barnes representations of the Stieltjes transform for general `r`.

### Derivation

**Step 1: Set up the Integral and Decompose the Integrand**

For $r=1$, the function is $f(t;1,c) = \frac{c}{c^2+t^2}$. The Stieltjes transform at $z=-x$ is:

$$
S_{f}(-x;1,c) = \int_{0}^{\infty}\frac{c}{(c^2+t^2)(t+x)}\,\mathrm{d}t
$$

We decompose the integrand into partial fractions with respect to the variable $t$:

$$
\frac{c}{(c^2+t^2)(t+x)} = \frac{A}{t+x} + \frac{Bt+D}{c^2+t^2}
$$

Solving for the coefficients gives $A = \frac{c}{c^2+x^2}$, $B = -\frac{c}{c^2+x^2}$, and $D = \frac{cx}{c^2+x^2}$.

This allows us to rewrite the integrand as:

$$
\frac{1}{x^2+c^2} \left[ \frac{c}{t+x} - \frac{ct}{c^2+t^2} + \frac{cx}{c^2+t^2} \right]
$$

**Step 2: Integrate over a Truncated Domain**

To handle the improper integrals, we integrate from $0$ to a finite upper bound $T$ and will subsequently take the limit as $T \to \infty$. We integrate the three terms inside the bracket:

*   **Term 1:** $\int_{0}^{T}\frac{c}{t+x}\,\mathrm{d}t = c\bigl[\log(t+x)\bigr]_0^T = c\log(T+x) - c\log(x)$
*   **Term 2:** $-\int_{0}^{T}\frac{ct}{c^2+t^2}\,\mathrm{d}t = -\frac{c}{2}\bigl[\log(c^2+t^2)\bigr]_0^T = -\frac{c}{2}\log(c^2+T^2) + c\log(c)$
*   **Term 3:** $\int_{0}^{T}\frac{cx}{c^2+t^2}\,\mathrm{d}t = x\bigl[\arctan(t/c)\bigr]_0^T = x\arctan(T/c)$

**Step 3: Assemble and Evaluate the Limit as $T \to \infty$**

Combining the results and grouping by dependence on $T$:

$$
\int_{0}^{T} \dots \mathrm{d}t = \underbrace{c\log(T+x) - \frac{c}{2}\log(c^2+T^2)}_{\text{Terms dependent on } T} + \underbrace{x\arctan(T/c) - c\log(x) + c\log(c)}_{\text{Finite / Constant terms}}
$$

We now take the limit as $T \to \infty$.

*   For the arctangent term: $\lim_{T \to \infty} x\arctan(T/c) = x\frac{\pi}{2}$.
*   For the logarithmic terms, we combine them into a single logarithm:

$$
c\log\left( \frac{T+x}{\sqrt{c^2+T^2}} \right)
$$

As $T \to \infty$, the argument of the logarithm behaves as $\frac{T}{\sqrt{T^2}} = 1$. Since $\log(1)=0$, the divergent logarithmic terms exactly cancel each other out.

**Step 4: State the Final Result**

The remaining finite terms give the value of the integral:

$$
x\frac{\pi}{2} - c\log(x) + c\log(c) = \frac{\pi}{2}x - c\log\left(\frac{x}{c}\right)
$$

Dividing by the overall prefactor $(x^2+c^2)$ from Step 1 gives the final boxed formula.

### Consistency Check with §11.1

Evaluating this expression at $x=c$:

$$
S_{f}(-c;1,c) = \frac{\frac{\pi}{2}c - c\log(c/c)}{c^2+c^2} = \frac{\frac{\pi}{2}c - 0}{2c^2} = \frac{\pi}{4c}
$$

This perfectly matches the general formula $S_f(-c;r,c) = \frac{\pi}{4rc}$ evaluated at $r=1$.
