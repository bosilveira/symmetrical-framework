# 11.1 Stieltjes Transform and the Resolvent at $z = -c$

The Stieltjes transform of the function provides its analytic continuation into the complex plane. Its evaluation at specific points yields important structural constants of the framework.

The Stieltjes transform of a real-valued function $g(t)$ is defined for $z \in \mathbb{C} \setminus \mathrm{supp}(g)$ as:

$$
S_g(z) := \int_{0}^{\infty}\frac{g(t)}{t-z}\,\mathrm{d}t
$$

For our framework, we evaluate the Stieltjes transform of $f(x;r,c)$ at the point $z = -c$, which lies on the negative real axis, safely outside the integration domain $(0,\infty)$. This value has a remarkably simple, exact rational form.

$$
\boxed{ S_{f}(-c) = \int_{0}^{\infty}\frac{f(t;r,c)}{t+c}\,\mathrm{d}t = \frac{\pi}{4rc} }
$$

### Exposition

This result is highly non-trivial. The integral, which involves a complex rational function, collapses to a simple constant. This value can be interpreted as the resolvent of an associated operator evaluated at a specific point in its spectrum. The derivation leverages the framework's canonical logarithmic coordinate system, where the integral is solved by decomposing the integrand into its even and odd symmetries.

### Derivation

**Step 1: Transform the Integral to Logarithmic Coordinates**

Let $t = c e^u$. The differential is $\mathrm{d}t = c e^u \,\mathrm{d}u$. The integration limits for $t$ from $(0, \infty)$ map to limits for $u$ from $(-\infty, \infty)$. We substitute this into the integral and apply the Rosetta Stone identity (§1.2), $f(ce^u) = \frac{1}{2ce^u}\mathrm{sech}(ru)$.

$$
S_{f}(-c) = \int_{-\infty}^{\infty} \frac{f(ce^u;r,c)}{ce^u + c} (ce^u \,\mathrm{d}u) = \int_{-\infty}^{\infty} \frac{\frac{1}{2ce^u}\mathrm{sech}(ru)}{c(e^u + 1)} (ce^u \,\mathrm{d}u)
$$

The factor of $ce^u$ from the differential cancels perfectly with the $ce^u$ in the denominator of the function's prefactor:

$$
S_{f}(-c) = \frac{1}{2c} \int_{-\infty}^{\infty} \frac{\mathrm{sech}(ru)}{e^u + 1} \,\mathrm{d}u
$$

**Step 2: Decompose the Logistic Function into Symmetries**

The term $\frac{1}{e^u+1}$ is the standard logistic function. We decompose it into its even and odd parts using the hyperbolic identity $1/(e^u+1) = \frac{1}{2}(1-\tanh(u/2))$:

$$
S_{f}(-c) = \frac{1}{2c} \int_{-\infty}^{\infty} \mathrm{sech}(ru) \left[ \frac{1}{2} - \frac{1}{2}\tanh(u/2) \right] \,\mathrm{d}u
$$

By linearity of integration, this splits into two integrals:

$$
S_{f}(-c) = \frac{1}{4c} \int_{-\infty}^{\infty} \mathrm{sech}(ru) \,\mathrm{d}u - \frac{1}{4c} \int_{-\infty}^{\infty} \mathrm{sech}(ru)\tanh(u/2) \,\mathrm{d}u
$$

**Step 3: Evaluate the Odd Integral**

The integrand of the second integral is the product of an even function ($\mathrm{sech}(ru)$) and an odd function ($\tanh(u/2)$), which results in an odd function. The integral of any odd function over a symmetric domain $(-\infty, \infty)$ is identically zero:

$$
\int_{-\infty}^{\infty} \mathrm{sech}(ru)\tanh(u/2) \,\mathrm{d}u = 0
$$

**Step 4: Evaluate the Even Integral**

We are left only with the first integral:

$$
S_{f}(-c) = \frac{1}{4c} \int_{-\infty}^{\infty} \mathrm{sech}(ru) \,\mathrm{d}u
$$

This is a standard definite integral. Using the substitution $v = ru$ (so $\mathrm{d}u = \mathrm{d}v/r$):

$$
\int_{-\infty}^{\infty} \mathrm{sech}(ru) \,\mathrm{d}u = \frac{1}{r} \int_{-\infty}^{\infty} \mathrm{sech}(v) \,\mathrm{d}v = \frac{1}{r} \left[ \arctan(\sinh(v)) \right]_{-\infty}^{\infty} = \frac{1}{r} \left( \frac{\pi}{2} - (-\frac{\pi}{2}) \right) = \frac{\pi}{r}
$$

**Step 5: Assemble the Final Result**

Substituting the value of the integral back into the expression for $S_f(-c)$:

$$
S_{f}(-c) = \frac{1}{4c} \left( \frac{\pi}{r} \right) = \frac{\pi}{4rc}
$$

This completes the derivation.
