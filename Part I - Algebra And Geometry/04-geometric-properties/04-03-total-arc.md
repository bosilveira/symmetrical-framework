# 4.3 Total Arc Length

While the function bounds a finite total area (mass) under its curve, the total geometric length of the curve from its origin at $x=0$ to its tail at $x=\infty$ is strictly infinite for all parameter values.

$$
\boxed{ L(0,\infty) = \int_{0}^{\infty} \sqrt{1+[f'(x;r,c)]^{2}} \,\mathrm{d}x = \infty }
$$

### Exposition

This result highlights a key geometric property of the function's graph. Although the curve approaches the $x$-axis rapidly enough for its integral (area) to converge, it does not flatten out quickly enough for its length to be finite. The "tail" of the curve contributes an infinite length, a property it shares with many asymptotically flat functions.

### Derivation

The divergence of the total arc length is proven by analyzing the asymptotic behavior of the arc-length integrand at the far-field tail ($x \to \infty$).

**Step 1: Define the Total Length Integral**
Using the arc-length element from §4.2, the total length of the curve is defined by the improper integral:

$$
L(0,\infty) = \int_{0}^{\infty} \frac{\mathrm{d}s}{\mathrm{d}x} \,\mathrm{d}x = \int_{0}^{\infty} \sqrt{1+[f'(x)]^{2}} \,\mathrm{d}x
$$

**Step 2: Analyze the Asymptotic Behavior of the Derivative**
We examine the limit of the first derivative, $f'(x)$, as $x \to \infty$. From the asymptotic power-law tails established in §1.9, we know that as $x \to \infty$, the function behaves as $f(x) \sim c^r x^{-r-1}$.
The derivative of this asymptotic form is:

$$
f'(x) \sim \frac{\mathrm{d}}{\mathrm{d}x}(c^r x^{-r-1}) = -(r+1)c^r x^{-r-2}
$$

Since the shape parameter is strictly positive ($r>0$), the exponent $-(r+2)$ is strictly less than $-2$. Therefore, the derivative vanishes at infinity:

$$
\lim_{x \to \infty} f'(x) = 0
$$

**Step 3: Evaluate the Asymptotic Limit of the Integrand**
Substitute the limit of the derivative into the arc-length integrand:

$$
\lim_{x \to \infty} \sqrt{1+[f'(x)]^{2}} = \sqrt{1 + 0^2} = 1
$$

**Step 4: Conclude Divergence using the Limit Comparison Test**
The integral for the total length is $\int_0^\infty \sqrt{1+[f'(x)]^2} \mathrm{d}x$. We compare this to the divergent integral $\int_1^\infty 1 \mathrm{d}x$.
Since the integrand of the arc-length integral approaches a non-zero constant ($1$) as $x \to \infty$, the tail of the integral, $\int_a^\infty \sqrt{1+[f'(x)]^2} \mathrm{d}x$ for some large $a$, behaves like $\int_a^\infty 1 \mathrm{d}x$.

Because the integral $\int_a^\infty 1 \mathrm{d}x$ diverges, by the Limit Comparison Test, the integral for the total arc length must also diverge.

*(Note: While the behavior of the integrand near the origin $x \to 0^+$ can also be singular depending on the value of $r$, the non-vanishing behavior at $x \to \infty$ is sufficient to guarantee the global divergence of the integral for the entire function family).*
