# 13.5 $n$-Fold Iterated Convolution

We generalize the multiplicative convolution to an arbitrary number, $n$, of identical functions from the family. While computing the exact spatial density for large $n$ becomes algebraically intensive, the Mellin transform of this $n$-fold convolution assumes a perfectly clean, exact algebraic form.

Let $f *_M \dots *_M f$ denote the $n$-fold multiplicative convolution of $f(x; r, c)$ with itself. Its Mellin transform is:

$$
\boxed{\; \mathcal M\Bigl\{\underbrace{f*_{M}\cdots*_{M}f}_{n\text{ times}}\Bigr\}(s) = \left(\frac{\pi c^{s-1}}{2r}\right)^{n}\sec^{n}\left(\frac{(s-1)\pi}{2r}\right) \;}
$$

### Exposition

This $n$-fold transform serves as the unnormalized characteristic function for the product of $n$ independent, identically distributed random variables drawn from the system. As $n \to \infty$, this identity governs the asymptotic behavior of the system. According to the Central Limit Theorem applied to the logarithmic domain, the standardized sum of $n$ logarithmic variables will converge to a Gaussian distribution, and the heavily convolved multiplicative product will asymptotically flow into a Log-Normal distribution. This exact transform provides the analytical bridge mapping this flow.

### Derivation

This result is a direct, immediate consequence of the Mellin convolution theorem applied to our previously derived fundamental transform.

**Step 1: The Mellin Convolution Theorem**

For any two suitable functions $g(x)$ and $h(x)$, the Mellin transform of their multiplicative (Haar) convolution is equal to the product of their individual Mellin transforms:

$$
\mathcal{M}\{g *_M h\}(s) = \mathcal{M}\{g\}(s) \cdot \mathcal{M}\{h\}(s)
$$

**Step 2: Iterate to $n$ Factors**
By mathematical induction, applying this theorem $n-1$ times to $n$ identical copies of the function $f$ yields:

$$
\mathcal M\Bigl\{\underbrace{f*_{M}\cdots*_{M}f}_{n\text{ times}}\Bigr\}(s) = \Bigl[ \mathcal{M}\{f\}(s) \Bigr]^n
$$

**Step 3: Substitute the Secant Form**

We insert the exact closed-form secant expression for the single Mellin transform derived in §6.1:

$$
\mathcal{M}\{f\}(s) = \frac{\pi c^{s-1}}{2r}\sec\left(\frac{(s-1)\pi}{2r}\right)
$$

Raising this entire expression to the $n$-th power instantly yields the boxed identity:

$$
\Bigl[ \mathcal{M}\{f\}(s) \Bigr]^n = \left(\frac{\pi c^{s-1}}{2r}\right)^{n}\sec^{n}\left(\frac{(s-1)\pi}{2r}\right)
$$

This completes the derivation.
