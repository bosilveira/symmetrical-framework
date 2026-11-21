# 11.4 Mellin-Barnes Residue Series

For non-integer shape parameters $r$, the Stieltjes transform does not reduce to a finite number of elementary terms. Instead, we can represent it globally as a Mellin-Barnes contour integral, which evaluates exactly to a dual infinite series by summing the residues of the integrand's poles.

For non-integer $r > 0$ and $x > c$:

$$
\boxed{ S_{f}(-x;r,c) = \frac{\pi}{2rc}\sum_{n=1}^{\infty} (-1)^{n+1}\left(\frac{c}{x}\right)^{n}\sec\left(\frac{(n-1)\pi}{2r}\right) + \frac{\pi}{c}\sum_{k=0}^{\infty} \frac{(-1)^{k}}{\sin\bigl(\pi(1+r(2k+1))\bigr)}\left(\frac{c}{x}\right)^{1+r(2k+1)} }
$$

### Exposition

This identity provides an exact series representation for the Stieltjes transform in the outer domain ($x>c$). It is derived by applying the Mellin-Parseval theorem and evaluating the resulting contour integral using Cauchy's Residue Theorem. The formula reveals that the transform is composed of two distinct families of power-law terms, corresponding to the two independent sequences of poles in the complex Mellin-Barnes integrand.

### Derivation

**Step 1: Set up the Mellin-Parseval Integral**

The Stieltjes transform at $-x$ is the integral of a product: $S_{f}(-x) = \int_{0}^{\infty} f(t) \cdot \frac{1}{t+x} \,\mathrm{d}t$.

By the Mellin-Parseval theorem (§6), this is equivalent to the complex contour integral:

$$
S_{f}(-x) = \frac{1}{2\pi i} \int_{\sigma-i\infty}^{\sigma+i\infty} \mathcal{M}\{f\}(s) \, \mathcal{M}\left\{\frac{1}{t+x}\right\}(1-s) \,\mathrm{d}s
$$

**Step 2: Substitute the Component Mellin Transforms**

*   From §6.1, $\mathcal{M}\{f\}(s) = \frac{\pi c^{s-1}}{2r} \sec\left(\frac{(s-1)\pi}{2r}\right)$.
*   The standard Mellin transform of the kernel is $\mathcal{M}\left\{\frac{1}{t+x}\right\}(1-s) = x^{-s} \frac{\pi}{\sin(\pi(1-s))} = x^{-s} \frac{\pi}{\sin(\pi s)}$.

The integrand of the contour integral is the product of these two functions:

$$
I(s) = \left(\frac{\pi c^{s-1}}{2r} \sec\left(\frac{(s-1)\pi}{2r}\right)\right) \left( x^{-s} \frac{\pi}{\sin(\pi s)} \right) = \frac{\pi^2}{2rc} \left(\frac{c}{x}\right)^s \frac{\sec\left(\frac{(s-1)\pi}{2r}\right)}{\sin(\pi s)}
$$

**Step 3: Close the Contour and Identify Poles**

For the case $x > c$, the ratio $c/x < 1$. The term $(c/x)^s$ decays exponentially as $\mathrm{Re}(s) \to +\infty$. We can therefore close the integration contour with an infinite semi-circle in the **right half-plane**. By Cauchy's Residue Theorem, the integral equals **$-2\pi i$** times the sum of the enclosed residues (because closing to the right creates a clockwise contour).

The integrand has two independent sets of simple poles in the right half-plane ($s>0$):

*   **Set 1 (from sine):** The poles from $1/\sin(\pi s)$ occur where $\sin(\pi s) = 0$, which are the positive integers $s = n$ for $n \ge 1$.
*   **Set 2 (from secant):** The poles from $\sec(\dots) = 1/\cos(\dots)$ occur where $\cos\left(\frac{(s-1)\pi}{2r}\right) = 0$. This implies $\frac{(s-1)\pi}{2r} = \frac{(2k+1)\pi}{2}$, which gives $s = 1 + r(2k+1)$ for integers $k \ge 0$.

**Step 4: Evaluate Residues for Set 1 (Sine Poles at $s=n$)**

The residue of $1/\sin(\pi s)$ at $s=n$ is $(-1)^n/\pi$. The residue of the full integrand is:

$$
\mathrm{Res}_{s=n} I(s) = \frac{\pi^2}{2rc} \left(\frac{c}{x}\right)^n \sec\left(\frac{(n-1)\pi}{2r}\right) \frac{(-1)^n}{\pi} = \frac{\pi}{2rc} (-1)^n \left(\frac{c}{x}\right)^n \sec\left(\frac{(n-1)\pi}{2r}\right)
$$

The contribution to the integral is $(-2\pi i) \sum \mathrm{Res}$, which results in the first sum in the boxed formula after accounting for the factor of $1/(2\pi i)$ and the sign change from $(-1)^n$ to $(-1)^{n+1}$.

**Step 5: Evaluate Residues for Set 2 (Secant Poles at $s_k=1+r(2k+1)$)**

The residue of $\sec(g(s))$ at a simple zero of $\cos(g(s))$ is $1/g'(s)$. Here, $g(s) = \frac{(s-1)\pi}{2r}$, so $g'(s) = \frac{\pi}{2r}$. The residue of the secant term at $s=s_k$ is $\frac{(-1)^k}{g'(s_k)} = \frac{2r}{\pi}(-1)^k$. There is a sign error in my previous logic; let me be more careful. The residue of $1/h(s)$ at a simple zero $s_0$ is $1/h'(s_0)$. Let $h(s)=\cos(\dots)$. Then $h'(s) = -\sin(\dots)\cdot(\pi/2r)$. At $s_k$, the argument is $(2k+1)\pi/2$, so $\sin((2k+1)\pi/2) = (-1)^k$. The residue of secant is $1/(-\frac{\pi}{2r}(-1)^k) = \frac{2r}{\pi}(-1)^{k+1}$.

The residue of the full integrand is:

$$
\mathrm{Res}_{s=s_k} I(s) = \frac{\pi^2}{2rc} \left(\frac{c}{x}\right)^{s_k} \frac{1}{\sin(\pi s_k)} \left(\frac{2r}{\pi}(-1)^{k+1}\right) = \frac{\pi}{c} \frac{(-1)^{k+1}}{\sin(\pi s_k)} \left(\frac{c}{x}\right)^{s_k}
$$

The contribution to the integral is $(-2\pi i) \sum \mathrm{Res}$. The final sum, after accounting for all signs and factors, matches the second sum in the boxed formula.

*(Note: When $r$ is an integer, the two sets of poles can collide, creating higher-order poles. The evaluation of these requires taking limits and derivatives of the residues, which is what gives rise to the logarithmic terms seen in the classical $r=1$ case in §11.2).*
