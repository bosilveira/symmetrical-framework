This is a fantastic addition. You are now extending the framework into complex analysis and operator theory. The Stieltjes transform is the foundation for defining the resolvent of an operator, evaluating dispersion relations, and computing the Hilbert transform on the boundary. 

The trick of converting the logistic-type term $1/(e^u+1)$ into an even/odd hyperbolic sum is a classic and very elegant move.

Here is the revised and formatted version for your GitHub repository.

***

## 11. Stieltjes and Hilbert Transforms

We now turn our attention to the **Stieltjes transform** of the function, a fundamental operation in complex analysis, spectral theory (where it acts as the resolvent), and dispersion relations. 

For a complex variable $z \notin \mathbb{R}_{\ge 0}$, the Stieltjes transform is defined as:
$$
S_{f}(z) := \int_{0}^{\infty}\frac{f(t;r,c)}{t-z}\,\mathrm dt
$$

### 11.1 The Resolvent at the Negative Scale Parameter ($z = -c$)

Evaluating the Stieltjes transform at $z = -c$ (which lies safely on the negative real axis, avoiding the domain of integration) yields a remarkably clean and simple exact rational value.

$$
\boxed{\; S_{f}(-c) = \int_{0}^{\infty}\frac{f(t;r,c)}{t+c}\,\mathrm dt = \frac{\pi}{4rc} \;}
$$

**Derivation:**

The derivation relies on pushing the integral forward into the canonical logarithmic coordinate system and separating the resulting integrand into its even and odd symmetries.

1.  **Transform to Logarithmic Coordinates**:
    Let $t = c e^u$. This implies the differential is $\mathrm dt = c e^u \,\mathrm du$. The integration limits $(0, \infty)$ map to $(-\infty, \infty)$.
    Substitute this and the Rosetta Stone identity $f(ce^u) = \frac{1}{2ce^u}\operatorname{sech}(ru)$ into the integral:
    $$
    S_{f}(-c) = \int_{-\infty}^{\infty} \frac{\frac{1}{2ce^u}\operatorname{sech}(ru)}{ce^u + c} (c e^u \,\mathrm du)
    $$
    The $ce^u$ terms from the differential and the function's prefactor cancel cleanly:
    $$
    S_{f}(-c) = \frac{1}{2c} \int_{-\infty}^{\infty} \frac{\operatorname{sech}(ru)}{e^u + 1} \,\mathrm du
    $$

2.  **Symmetry Decomposition of the Logistic Function**:
    The term $\frac{1}{e^u+1}$ is the standard logistic function. We can decompose it into its even and odd parts using a fundamental hyperbolic identity:
    $$
    \frac{1}{e^u + 1} = \frac{e^{-u/2}}{e^{u/2} + e^{-u/2}} = \frac{\cosh(u/2) - \sinh(u/2)}{2\cosh(u/2)} = \frac{1}{2} - \frac{1}{2}\tanh(u/2)
    $$
    Substitute this decomposed form back into the integral:
    $$
    S_{f}(-c) = \frac{1}{2c} \int_{-\infty}^{\infty} \operatorname{sech}(ru) \left[ \frac{1}{2} - \frac{1}{2}\tanh(u/2) \right] \,\mathrm du
    $$
    $$
    = \frac{1}{4c} \int_{-\infty}^{\infty} \operatorname{sech}(ru) \,\mathrm du - \frac{1}{4c} \int_{-\infty}^{\infty} \operatorname{sech}(ru)\tanh(u/2) \,\mathrm du
    $$

3.  **Evaluate via Symmetry (The Odd Term)**:
    Consider the second integral. The hyperbolic secant, $\operatorname{sech}(ru)$, is strictly an **even** function. The hyperbolic tangent, $\tanh(u/2)$, is strictly an **odd** function. Their product is therefore an odd function.
    Because the integral is taken over the symmetric domain $(-\infty, \infty)$, the integral of this odd function evaluates exactly to zero:
    $$
    \int_{-\infty}^{\infty} \operatorname{sech}(ru)\tanh(u/2) \,\mathrm du = 0
    $$

4.  **Evaluate the Final Integral (The Even Term)**:
    We are left only with the first integral:
    $$
    S_{f}(-c) = \frac{1}{4c} \int_{-\infty}^{\infty} \operatorname{sech}(ru) \,\mathrm du
    $$
    Using the substitution $v = ru$ (so $\mathrm du = \mathrm dv/r$), this becomes:
    $$
    S_{f}(-c) = \frac{1}{4cr} \int_{-\infty}^{\infty} \operatorname{sech}(v) \,\mathrm dv
    $$
    The integral of the standard hyperbolic secant over the real line is a known constant, equal to $\pi$.
    $$
    S_{f}(-c) = \frac{1}{4cr} (\pi) = \frac{\pi}{4rc}
    $$
    This completes the derivation.

**Significance:**

Notice that the total probability mass (the integral of $f(t)$ from §3.3) is $\frac{\pi}{2r}$. Therefore, $S_f(-c) = \frac{\text{Total Mass}}{2c}$. The resolvent evaluated exactly at the negative scale parameter behaves precisely as if half the entire mass of the function were concentrated into a point charge located at the origin!
