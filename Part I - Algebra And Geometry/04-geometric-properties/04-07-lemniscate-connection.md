# 4.7 Arc Length at r=2 (Lemniscate Connection)

While the general arc-length integral is a hyperelliptic function, for the specific case $r=2$, the integral reduces to a classical elliptic integral that can be parametrized by the **lemniscate functions**. This provides a direct geometric link between the shape of the function at $r=2$ and the geometry of Bernoulli's lemniscate.

**Theorem:** The arc-length integral for $f(x;2,c)$ on the interval $[0,c]$ can be expressed as an elliptic integral in lemniscate coordinates.

### Exposition

The case $r=2$ is special throughout the framework, often corresponding to the Moonshine locus or critical quantum thresholds. Its unique geometric status is reflected here, as its arc length connects to the lemniscate constant $\varpi = \int_0^1 (1-t^4)^{-1/2} \mathrm{d}t$ and its associated functions, $\mathrm{sl}(u)$ and $\mathrm{cl}(u)$.

### Derivation

**Step 1:** State the function and its derivative for $r=2$.

$$
f(x;2,c) = \frac{c^2 x}{c^4+x^4}, \qquad f'(x;2,c) = \frac{c^2(c^4 - 3x^4)}{(c^4+x^4)^2}
$$

**Step 2:** Form the arc-length integral for the segment $[0,c]$.

$$
L_2(0,c) = \int_0^c \sqrt{1 + \left( \frac{c^2(c^4 - 3x^4)}{(c^4+x^4)^2} \right)^2} \mathrm{d}x
$$

**Step 3:** Apply the Lemniscate Substitution.
The structure of the function with $x^4$ suggests the lemniscate substitution $x = c \cdot \mathrm{sl}(u)$, where $\mathrm{sl}(u)$ is the lemniscate sine. As $x$ ranges from $0$ to $c$, the variable $u$ ranges from $0$ to $\varpi$ (the half-period of the lemniscate sine). The differential is $\mathrm{d}x = c \cdot \mathrm{sl}'(u)\mathrm{d}u = c \sqrt{1-\mathrm{sl}^4(u)}\mathrm{d}u$.

**Step 4:** Transform the integrand.
The term $f(x;2,c)$ itself has an elegant form under this substitution (as shown in your notes):

$$
f(c \cdot \mathrm{sl}(u); 2, c) = \frac{\mathrm{sl}(u)}{c(1+\mathrm{sl}^4(u))}
$$

The derivative $f'(x)$ becomes a complex function of $\mathrm{sl}(u)$ and $\mathrm{cl}(u)$. The full integrand transforms into the form:

$$
\text{Integrand} = R(\mathrm{sl}(u), \mathrm{cl}(u)) \sqrt{1-\mathrm{sl}^4(u)}
$$

where $R$ is a rational function.

**Step 5:** State the final integral form.
Let $s = \mathrm{sl}(u)$. The integral for the arc length becomes:

$$
L_2(0,c) = c \int_0^{\varpi} \frac{\sqrt{(1-s^4)\left[ (1+s^4)^4 + (1-3s^4)^2(1-s^4) \right]}}{(1+s^4)^2} \mathrm{d}u
$$

This is a genuine elliptic integral in the lemniscate parametrization. While it does not have a simple closed form, its representation confirms the deep geometric connection between the $r=2$ case and the classical theory of elliptic functions associated with the lemniscate.
