# 1.3 Canonical Linearization and the Three Core Objects

The canonical substitution $u = \log(x/c)$ linearizes the framework, converting the multiplicative geometry of the positive half-line into an additive geometry on the full real line $\mathbb{R}$. This transformation gives rise to three fundamental objects in the linearized $u$-space.

The coordinate transformation and its inverse are:

$$
u = \log(x/c) \quad \iff \quad x = c e^u
$$

Under this map, the invariant multiplicative Haar measure transforms into the additive Lebesgue measure:

$$
\frac{\mathrm{d}x}{x} = \mathrm{d}u
$$

### Exposition

This section explicitly defines the three core functions that arise naturally in the linearized $u$-space. Distinguishing between them is critical for the consistency of the framework.
1.  The **Linearized Kernel ($g$)** is a direct substitution.
2.  The **Log-Pushed Density ($p$)** is the pushforward of the probability measure.
3.  The **Conformal Phase ($W$)** is the hyperbolic companion.

### Object 1 — The Linearized Kernel $g(u)$

The linearized kernel is obtained by substituting the coordinate transformation $x = ce^u$ directly into the algebraic definition of $f(x;r,c)$.

$$
\boxed{ g(u;r,c) := f(ce^u;r,c) = \frac{\mathrm{sech}(ru)}{2ce^{u}} }
$$

#### Derivation

**Step 1:** Start with the Rosetta Stone identity (§1.2):

$$
f(x;r,c) = \frac{1}{2x}\mathrm{sech}(r\log(x/c))
$$

**Step 2:** Substitute $x = ce^u$ and $u = \log(x/c)$ into the formula:

$$
f(ce^u;r,c) = \frac{1}{2(ce^u)}\mathrm{sech}(ru) = \frac{\mathrm{sech}(ru)}{2ce^{u}}
$$

This defines $g(u;r,c)$. Due to the $e^u$ term in the denominator (which is a remnant of the Jacobian), $g(u;r,c)$ is not a symmetric function of $u$.

### Object 2 — The Log-Pushed Density $p(u)$

The true probability density function in the linearized space is the pushforward of the normalized density measure $\rho(x)\mathrm{d}x = p(u)\mathrm{d}u$.

$$
\boxed{ p(u;r) := \rho(ce^u;r,c)\cdot \frac{\mathrm{d}x}{\mathrm{d}u} = \frac{r}{\pi}\mathrm{sech}(ru) }
$$

#### Derivation

**Step 1:** Define the normalized density $\rho(x)$ from §1.7, using the total mass from §3.3:

$$
\rho(x;r,c) = \frac{f(x;r,c)}{\int_0^\infty f(x) dx} = \frac{f(x;r,c)}{\pi/(2r)} = \frac{2r}{\pi}f(x;r,c)
$$

**Step 2:** Apply the change of variables formula for probability densities. The Jacobian of the transformation is $\frac{\mathrm{d}x}{\mathrm{d}u} = ce^u$.

$$
p(u;r) = \rho(ce^u;r,c) \cdot \frac{\mathrm{d}x}{\mathrm{d}u} = \left( \frac{2r}{\pi}f(ce^u;r,c) \right) \cdot (ce^u)
$$

**Step 3:** Substitute the linearized kernel $g(u;r,c) = f(ce^u;r,c)$:

$$
p(u;r) = \frac{2r}{\pi} \left( \frac{\mathrm{sech}(ru)}{2ce^u} \right) (ce^u)
$$

The Jacobian factors $ce^u$ cancel completely, yielding a purely symmetric function that is independent of the scale parameter $c$:

$$
p(u;r) = \frac{r}{\pi}\mathrm{sech}(ru)
$$

This function is known as the **hyperbolic secant distribution**. It is an even, unimodal probability density on $\mathbb{R}$ that integrates to 1.

### Object 3 — The Conformal Phase $W(u)$

The hyperbolic tangent companion to the Rosetta Stone's secant (§1.4) linearizes into a pure phase function.

$$
\boxed{ W(u;r) := \tanh(ru) }
$$

#### Derivation

**Step 1:** Recall the definition of the conformal phase from §1.4:

$$
W(x;r,c) = \tanh\left(r\log\left(\frac{x}{c}\right)\right)
$$

**Step 2:** Substitute $u = \log(x/c)$:

$$
W(u;r) = \tanh(ru)
$$

This function is strictly odd, $W(-u) = -W(u)$, and bounded, $W \in (-1, 1)$.
