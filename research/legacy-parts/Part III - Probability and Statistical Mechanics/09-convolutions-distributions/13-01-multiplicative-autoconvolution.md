# 13.1 Multiplicative Autoconvolution

The multiplicative (or Mellin) autoconvolution of the function with itself, denoted $(f *_M f)(x)$, yields a new closed-form algebraic structure. Instead of producing another pure power-law/hyperbolic function, the convolution generates a logarithmic numerator modulating a hyperbolic sine denominator.

$$
\boxed{\; (f *_M f)(x; r, c) := \int_{0}^{\infty} f(\xi; r, c) \, f(x/\xi; r, c) \, \frac{\mathrm{d}\xi}{\xi} = \frac{\log(x/c^2)}{2x\sinh\bigl(r\log(x/c^2)\bigr)} \;}
$$

### Exposition

The multiplicative convolution is the natural group operation for functions defined on the scale-invariant half-line $(\mathbb{R}_{>0}, \times)$. This identity demonstrates that the convolution of two functions from the family remains analytically closed. The resulting function has a removable singularity at the symmetry point $x=c^2$, revealing a smooth transition structure governing the interaction of two scaling systems.

### Derivation

The derivation seamlessly translates the multiplicative convolution in $x$-space into a standard additive convolution in logarithmic space, where the Rosetta Stone identity reduces the problem to integrating the product of two hyperbolic secants.

**Step 1: Logarithmic Substitution**

We map the variables into the canonical logarithmic coordinate system. Let the integration variable be $\xi = ce^u$, and let the external variable be defined relative to the squared scale, $x = c^2 e^s$. 

This implies the ratio is $x/\xi = (c^2 e^s) / (c e^u) = ce^{s-u}$. 

The Haar measure is invariant under this translation: $\frac{\mathrm{d}\xi}{\xi} = \frac{ce^u \mathrm{d}u}{ce^u} = \mathrm{d}u$.

**Step 2: Apply the Rosetta Stone**

Using the identity from §1.2, we rewrite the two factors in the integrand:

*   $f(\xi) = \frac{1}{2\xi}\operatorname{sech}\left(r\log\frac{\xi}{c}\right) = \frac{1}{2ce^u}\operatorname{sech}(ru)$
*   $f(x/\xi) = \frac{1}{2(x/\xi)}\operatorname{sech}\left(r\log\frac{x/\xi}{c}\right) = \frac{1}{2ce^{s-u}}\operatorname{sech}(r(s-u))$

**Step 3: Assemble the Transformed Integral**

Substitute these components into the definition of the multiplicative convolution:

$$
(f *_M f)(x) = \int_{-\infty}^{\infty} \left[ \frac{\operatorname{sech}(ru)}{2ce^u} \right] \left[ \frac{\operatorname{sech}(r(s-u))}{2ce^{s-u}} \right] \mathrm{d}u
$$

Combine the exponential denominators: $(2ce^u)(2ce^{s-u}) = 4c^2 e^s = 4x$. We can pull $1/(4x)$ entirely out of the integral:

$$
(f *_M f)(x) = \frac{1}{4x} \int_{-\infty}^{\infty} \operatorname{sech}(ru)\operatorname{sech}(r(s-u)) \, \mathrm{d}u
$$

**Step 4: Solve the Additive Convolution**

The remaining integral is the standard additive convolution of the hyperbolic secant function. It evaluates to a known closed form (verifiable via Fourier transform inversion or complex contour residues):

$$
\int_{-\infty}^{\infty} \operatorname{sech}(ru)\operatorname{sech}(r(s-u)) \, \mathrm{d}u = \frac{2s}{\sinh(rs)}
$$

**Step 5: Final Substitution**

Substitute the result of the integral back into our expression, recalling that $s = \log(x/c^2)$:

$$
(f *_M f)(x) = \frac{1}{4x} \left( \frac{2s}{\sinh(rs)} \right) = \frac{\log(x/c^2)}{2x\sinh\bigl(r\log(x/c^2)\bigr)}
$$

This completes the derivation.

*(Note: The apparent $0/0$ singularity at $x = c^2 \implies s=0$ evaluates via L'Hôpital's rule to $(f *_M f)(c^2) = \frac{1}{2rc^2}$, proving the convolution is perfectly smooth).*
