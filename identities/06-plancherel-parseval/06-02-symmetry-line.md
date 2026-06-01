### 6.2 Central-Line Plancherel — The Symmetry Line $\operatorname{Re}(s) = 1$

When we evaluate the Plancherel-type integral along the central line of the Mellin strip, $s = 1+it$, the dependence on the scale parameter `c` vanishes entirely. The result is a topological constant dependent only on the shape of the function family.

$$
\boxed{\; \frac{1}{2\pi}\int_{-\infty}^{\infty}\left|\mathcal M\{f\}(1+it)\right|^{2}\,\mathrm dt = \frac{1}{2r} \;}
$$

**Derivation:**

The derivation relies on evaluating the secant form of the Mellin transform (§5.1) exactly on this complex line, where the complex exponential of `c` becomes a pure phase factor.

1.  **Evaluate the Transform on the Central Line**: 
Substitute $s = 1+it$ into the secant form of the Mellin transform:
$$
\mathcal M\{f\}(1+it) = \frac{\pi c^{(1+it)-1}}{2r} \sec\left(\frac{((1+it)-1)\pi}{2r}\right) = \frac{\pi c^{it}}{2r} \sec\left(\frac{it\pi}{2r}\right)
$$

2.  **Calculate the Squared Magnitude**:
We take the absolute square of the expression. 
*   The scale parameter term is $|c^{it}|^2 = |e^{it\log c}|^2 = 1$. This is the crucial step where the dependence on `c` evaporates.
*   For the secant term, we use the identity relating the secant of an imaginary number to the hyperbolic secant: $|\sec(iz)|^2 = |\operatorname{sech}(z)|^2 = \operatorname{sech}^2(z)$ for real `z`.

Combining these yields:
$$
\left|\mathcal M\{f\}(1+it)\right|^{2} = \left(\frac{\pi}{2r}\right)^{2} \operatorname{sech}^{2}\left(\frac{t\pi}{2r}\right)
$$

3.  **Set Up and Transform the Integral**:
Substitute this magnitude into the target integral:
$$
I = \frac{1}{2\pi}\int_{-\infty}^{\infty} \left(\frac{\pi}{2r}\right)^{2} \operatorname{sech}^{2}\left(\frac{t\pi}{2r}\right) \,\mathrm dt
$$
To solve this, perform a substitution to simplify the argument of the hyperbolic secant. Let $v = \frac{\pi t}{2r}$. This gives $\mathrm dt = \frac{2r}{\pi} \mathrm dv$.

4.  **Evaluate the Final Integral**:
Substitute $v$ and $\mathrm dt$ into the integral:
$$
I = \frac{1}{2\pi} \left(\frac{\pi}{2r}\right)^{2} \int_{-\infty}^{\infty} \operatorname{sech}^{2}(v) \left(\frac{2r}{\pi} \mathrm dv\right)
$$
Group the constants outside the integral:
$$
I = \frac{1}{2\pi} \cdot \frac{\pi^2}{4r^2} \cdot \frac{2r}{\pi} \int_{-\infty}^{\infty} \operatorname{sech}^{2}(v) \,\mathrm dv = \frac{1}{4r} \int_{-\infty}^{\infty} \operatorname{sech}^{2}(v) \,\mathrm dv
$$
The remaining integral is a standard classical result. Since the derivative of $\tanh(v)$ is $\operatorname{sech}^2(v)$, we have:
$$
\int_{-\infty}^{\infty} \operatorname{sech}^{2}(v) \,\mathrm dv = \Bigl[ \tanh(v) \Bigr]_{-\infty}^{\infty} = 1 - (-1) = 2
$$
Multiplying by the prefactor gives the final result:
$$
I = \frac{1}{4r} \cdot 2 = \frac{1}{2r}
$$

**Significance:**

This result is profoundly beautiful. By evaluating the transform's "energy" along the axis of its functional symmetry (the line $s=1$), we strip away the dimensional scaling of the system. The value $1/(2r)$ is a pure, dimensionless geometric invariant of the specific function shape chosen from the family. Furthermore, because $1/(2r)$ happens to be exactly the prefactor in the general $L^n$ norm identities, this integral provides a deep structural link between the complex-plane symmetries of the transform and the real-space normalization of the function.
