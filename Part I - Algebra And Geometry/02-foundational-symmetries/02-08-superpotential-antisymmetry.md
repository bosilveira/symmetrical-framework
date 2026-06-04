# 2.8 Superpotential Anti-Symmetry

This section examines the symmetry properties of the function's logarithmic derivative. This quantity, which we define as a "superpotential" in anticipation of its role in supersymmetric quantum mechanics, satisfies an elegant anti-symmetry identity when expressed in the canonical logarithmic coordinate.

We define the superpotential function, $W_{\text{susy}}(x)$, as:

$$
W_{\text{susy}}(x) := -\frac{1}{2} \frac{1}{f(x)} \frac{\mathrm{d}f}{\mathrm{d}x}
$$

In the logarithmic coordinate $u = \log(x/c)$, this function satisfies the following identity:

$$
\boxed{ e^{u} W_{\text{susy}}(ce^{u}) + e^{-u} W_{\text{susy}}(ce^{-u}) = \frac{1}{c} }
$$

### Exposition

This identity demonstrates that the superpotential, when weighted by the coordinate itself, is not purely even or odd under the reflection $u \mapsto -u$. Instead, its even part is constant, while its odd part is non-trivial. This mixed-symmetry property is a direct consequence of the interplay between the hyperbolic functions that define the framework's differential structure.

### Derivation

The derivation is most transparently performed by first finding an explicit expression for $W_{\text{susy}}$ in the canonical coordinate system.

**Step 1: Calculate the Logarithmic Derivative $f'/f$**
We begin with the compact differential relation derived in §4.2 (and verifiable from the Rosetta Stone identity):

$$
x\frac{f'(x)}{f(x)} = -1 - r W(x;r,c) = -1 - r\tanh(r\log(x/c))
$$

Dividing by $x$ gives the logarithmic derivative:

$$
\frac{f'(x)}{f(x)} = -\frac{1 + r\tanh(r\log(x/c))}{x}
$$

**Step 2: Determine the Superpotential**
Using the definition $W_{\text{susy}} = -\frac{1}{2} (f'/f)$, we have:

$$
W_{\text{susy}}(x) = \frac{1 + r\tanh(r\log(x/c))}{2x}
$$

**Step 3: Express the Superpotential in Logarithmic Coordinates**
We now express this in the canonical coordinate $u=\log(x/c)$, where $x=ce^u$:

$$
W_{\text{susy}}(ce^u) = \frac{1 + r\tanh(ru)}{2ce^u}
$$

**Step 4: Prove the Symmetry Identity**
We evaluate the two terms on the left-hand side of the boxed identity separately.

*   **First Term:**

$$
e^u W_{\text{susy}}(ce^u) = e^u \cdot \frac{1 + r\tanh(ru)}{2ce^u} = \frac{1 + r\tanh(ru)}{2c}
$$

*   **Second Term:** We evaluate the expression at $-u$:

$$
e^{-u} W_{\text{susy}}(ce^{-u}) = e^{-u} \cdot \frac{1 + r\tanh(r(-u))}{2ce^{-u}} = \frac{1 + r\tanh(-ru)}{2c}
$$

Since the hyperbolic tangent is an **odd function**, $\tanh(-ru) = -\tanh(ru)$, this becomes:

$$
e^{-u} W_{\text{susy}}(ce^{-u}) = \frac{1 - r\tanh(ru)}{2c}
$$

*   **Sum the Terms:** Adding the two results causes the odd `tanh` components to cancel perfectly:

$$
\frac{1 + r\tanh(ru)}{2c} + \frac{1 - r\tanh(ru)}{2c} = \frac{(1+1) + (r-r)\tanh(ru)}{2c} = \frac{2}{2c} = \frac{1}{c}
$$

This completes the derivation. The identity is a direct consequence of decomposing the weighted superpotential into its constant even part and its `tanh` odd part in the logarithmic coordinate system.
