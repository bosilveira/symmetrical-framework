# 8.2 Central-Line Plancherel Identity

When the Plancherel-type integral of the Mellin transform is evaluated along the central line of the Mellin strip, $s = 1+it$, the dependence on the scale parameter `c` vanishes entirely. The result is a universal constant dependent only on the shape parameter `r`.

$$
\boxed{ \frac{1}{2\pi}\int_{-\infty}^{\infty}\left|\mathcal M\{f\}(1+it)\right|^{2}\,\mathrm{d}t = \frac{1}{2r} }
$$

### Exposition

This result is physically and geometrically significant. The line $\mathrm{Re}(s)=1$ is the axis of reflection for the Mellin functional equation (§6.3). By evaluating the transform's "energy" along this axis of symmetry, we strip away the dimensional scaling of the system. The resulting value, $1/(2r)$, is a pure, dimensionless geometric invariant of the specific function shape chosen from the family. This identity provides a deep structural link between the complex-plane symmetries of the transform and the normalization constants of the real-space function.

### Derivation

The derivation relies on evaluating the secant form of the Mellin transform from §6.1 exactly on the complex line $s=1+it$, where the exponential dependence on `c` becomes a pure phase factor that vanishes upon taking the magnitude.

**Step 1: Evaluate the Transform on the Central Line**

Substitute $s = 1+it$ into the secant form of the Mellin transform:

$$
\mathcal M\{f\}(1+it) = \frac{\pi c^{(1+it)-1}}{2r} \sec\left(\frac{((1+it)-1)\pi}{2r}\right) = \frac{\pi c^{it}}{2r} \sec\left(\frac{it\pi}{2r}\right)
$$

**Step 2: Calculate the Squared Magnitude**

We take the absolute square of the expression.

*   The scale parameter term becomes a pure phase, whose magnitude is unity: $|c^{it}|^2 = |e^{it\log c}|^2 = 1$. This is the crucial step where the dependence on `c` is eliminated.
*   For the secant term, we use the identity relating the secant of a pure imaginary number to the hyperbolic secant: $|\sec(iz)|^2 = |\mathrm{sech}(z)|^2 = \mathrm{sech}^2(z)$ for any real `z`.

Combining these yields the squared magnitude of the transform on the central line:

$$
\left|\mathcal M\{f\}(1+it)\right|^{2} = \left(\frac{\pi}{2r}\right)^{2} \mathrm{sech}^{2}\left(\frac{\pi t}{2r}\right)
$$

**Step 3: Set Up and Transform the Integral**

Substitute this magnitude into the target integral:

$$
I = \frac{1}{2\pi}\int_{-\infty}^{\infty} \left(\frac{\pi}{2r}\right)^{2} \mathrm{sech}^{2}\left(\frac{\pi t}{2r}\right) \,\mathrm{d}t
$$

To solve this, perform a substitution to simplify the argument of the hyperbolic secant. Let $v = \frac{\pi t}{2r}$, which gives $\mathrm{d}t = \frac{2r}{\pi} \mathrm{d}v$.

**Step 4: Evaluate the Final Integral**

Substitute $v$ and $\mathrm{d}t$ into the integral:

$$
I = \frac{1}{2\pi} \left(\frac{\pi}{2r}\right)^{2} \int_{-\infty}^{\infty} \mathrm{sech}^{2}(v) \left(\frac{2r}{\pi} \mathrm{d}v\right)
$$

Group the constant factors outside the integral:

$$
I = \frac{1}{2\pi} \cdot \frac{\pi^2}{4r^2} \cdot \frac{2r}{\pi} \int_{-\infty}^{\infty} \mathrm{sech}^{2}(v) \,\mathrm{d}v = \frac{1}{4r} \int_{-\infty}^{\infty} \mathrm{sech}^{2}(v) \,\mathrm{d}v
$$

The remaining integral is a standard classical result. Since the derivative of $\tanh(v)$ is $\mathrm{sech}^2(v)$, we have:

$$
\int_{-\infty}^{\infty} \mathrm{sech}^{2}(v) \,\mathrm{d}v = \Bigl[ \tanh(v) \Bigr]_{-\infty}^{\infty} = 1 - (-1) = 2
$$

Multiplying by the prefactor gives the final result:

$$
I = \frac{1}{4r} \cdot 2 = \frac{1}{2r}
$$

This completes the derivation.
