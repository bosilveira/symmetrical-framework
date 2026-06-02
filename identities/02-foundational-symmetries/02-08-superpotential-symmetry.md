### 2.8 Anti-Symmetry of the Logarithmic Derivative / Superpotential Symmetry

We now examine the properties of the function's logarithmic derivative, which we use to define a "superpotential" function, $W_{\text{susy}}(x)$, a concept borrowed from supersymmetric quantum mechanics.

$$
W_{\text{susy}}(x) := -\frac{1}{2} \frac{f'(x)}{f(x)}
$$

This function exhibits a specific kind of symmetry when expressed in the canonical logarithmic coordinate $u = \log(x/c)$, which is neither purely even nor odd, but satisfies the following elegant identity:

$$
e^{u} W_{\text{susy}}(ce^{u}) + e^{-u} W_{\text{susy}}(ce^{-u}) = \frac{1}{c}
$$

**Derivation:**

The derivation is most transparently performed by first finding an expression for $W_{\text{susy}}$ in the canonical coordinate system.

1.  **Calculate the Logarithmic Derivative**:  
    The cleanest way to find $f'/f$ is by implicit differentiation of the Rosetta Stone identity (§1.3), $2xf(x) = \mathrm{sech}(r\log(x/c))$. Differentiating both sides with respect to `x` gives:

$$
2f(x) + 2xf'(x) = -\mathrm{sech}\left(r\log\tfrac{x}{c}\right)\tanh\left(r\log\tfrac{x}{c}\right) \cdot \frac{r}{x}
$$

Divide the entire equation by $2f(x)$:

$$
1 + x\frac{f'(x)}{f(x)} = -\frac{\mathrm{sech}(r\log\tfrac{x}{c})}{2f(x)} \tanh\left(r\log\tfrac{x}{c}\right) \cdot \frac{r}{x}
$$

Substitute $2xf(x)$ for $\mathrm{sech}(r\log\tfrac{x}{c})$ on the right-hand side:

$$
1 + x\frac{f'(x)}{f(x)} = -\frac{2xf(x)}{2f(x)} \tanh\left(r\log\tfrac{x}{c}\right) \cdot \frac{r}{x} = -r\tanh\left(r\log\tfrac{x}{c}\right)
$$

Solving for $f'/f$ yields:

$$
\frac{f'(x)}{f(x)} = -\frac{1 + r\tanh(r\log(x/c))}{x}
$$

2.  **Determine the Superpotential**:  
    Using the definition $W_{\text{susy}} = -f'/(2f)$, we have:

$$
W_{\text{susy}}(x) = \frac{1 + r\tanh(r\log(x/c))}{2x}
$$

Now, we express this in the canonical coordinate $u=\log(x/c)$, where $x=ce^u$:

$$
W_{\text{susy}}(ce^u) = \frac{1 + r\tanh(ru)}{2ce^u}
$$

3.  **Prove the Symmetry Identity**:  
    We can now evaluate the two terms in the boxed identity. The first term is:

$$
e^u W_{\text{susy}}(ce^u) = e^u \cdot \frac{1 + r\tanh(ru)}{2ce^u} = \frac{1 + r\tanh(ru)}{2c}
$$

For the second term, we replace $u$ with $-u$:

$$
e^{-u} W_{\text{susy}}(ce^{-u}) = e^{-u} \cdot \frac{1 + r\tanh(r(-u))}{2ce^{-u}} = \frac{1 + r\tanh(-ru)}{2c}
$$

Since the hyperbolic tangent is an **odd function**, $\tanh(-ru) = -\tanh(ru)$, this becomes:

$$
e^{-u} W_{\text{susy}}(ce^{-u}) = \frac{1 - r\tanh(ru)}{2c}
$$

Summing the two terms causes the `tanh` components to cancel perfectly:

$$
\frac{1 + r\tanh(ru)}{2c} + \frac{1 - r\tanh(ru)}{2c} = \frac{1+1}{2c} = \frac{1}{c}
$$

This completes the derivation. The identity is a direct consequence of decomposing the superpotential into even and odd parts in the logarithmic coordinate system. The odd part (proportional to `tanh`) cancels out in the symmetric sum, leaving only a constant term.
