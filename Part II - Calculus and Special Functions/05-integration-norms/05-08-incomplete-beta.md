# 5.8 Truncated Moments and the Incomplete Beta Function

This section derives the moments of the normalized distribution, but truncated at the median point $x=c$. These "partial" or "truncated" moments have a closed-form solution in terms of the **incomplete Beta function**, $B_y(p,q)$. This result is particularly useful in statistics for calculating conditional expectations.

For an integer moment $n$ such that $|n|<r$, the truncated moment is:

$$
\boxed{ \int_{0}^{c} x^n \rho(x;r,c)\,\mathrm{d}x = \frac{c^n}{\pi} B_{1/2}\left(\frac{r+n}{2r}, \frac{r-n}{2r}\right) }
$$

where the incomplete Beta function is defined as $B_{y}(p,q) := \int_{0}^{y}t^{p-1}(1-t)^{q-1}\,\mathrm{d}t$.

### Exposition

This identity provides a powerful tool for analyzing the statistical properties of the distribution over partial domains. The fact that the integral evaluates to an incomplete Beta function with an upper limit of exactly $1/2$ is a deep consequence of the function's central splitting property at $x=c$. This result generalizes the half-mass integral from §5.3, which is recovered by setting $n=0$.

### Derivation

The result is achieved via a substitution that precisely maps the integrand to the form required by the incomplete Beta function's definition.

**Step 1: Set up the Integral**
Start with the definition of the truncated moment, substituting $\rho(x;r,c) = \frac{2r}{\pi}f(x;r,c)$:

$$
I_{n,c} = \int_{0}^{c} x^n \left(\frac{2r}{\pi} \frac{c^r x^{r-1}}{c^{2r}+x^{2r}}\right) \mathrm{d}x = \frac{2r c^r}{\pi} \int_{0}^{c} \frac{x^{n+r-1}}{c^{2r}+x^{2r}} \mathrm{d}x
$$

**Step 2: Define the Substitution**
The structure of the integrand suggests a substitution that maps the rational form of $f(x)$ to the binomial structure of the Beta integrand:

$$
t = \frac{x^{2r}}{c^{2r}+x^{2r}}
$$

From this definition, we can derive two crucial relationships:
*   $1-t = 1 - \frac{x^{2r}}{c^{2r}+x^{2r}} = \frac{c^{2r}}{c^{2r}+x^{2r}}$
*   $\frac{t}{1-t} = \frac{x^{2r}}{c^{2r}} \implies x = c\left(\frac{t}{1-t}\right)^{1/(2r)}$

**Step 3: Find the Differential $\mathrm{d}x$**
It is most direct to find $\mathrm{d}t/\mathrm{d}x$ and rearrange.

$$
\frac{\mathrm{d}t}{\mathrm{d}x} = \frac{(2rx^{2r-1})(c^{2r}+x^{2r}) - (x^{2r})(2rx^{2r-1})}{(c^{2r}+x^{2r})^2} = \frac{2rc^{2r}x^{2r-1}}{(c^{2r}+x^{2r})^2}
$$

We can rewrite this using our expressions for $t$ and $1-t$:

$$
\frac{\mathrm{d}t}{\mathrm{d}x} = \frac{2r}{x} \cdot \frac{x^{2r}}{c^{2r}+x^{2r}} \cdot \frac{c^{2r}}{c^{2r}+x^{2r}} = \frac{2r}{x} t(1-t)
$$

Rearranging for $\mathrm{d}x$ gives:

$$
\mathrm{d}x = \frac{x}{2r} \frac{\mathrm{d}t}{t(1-t)}
$$

**Step 4: Transform the Integral**
Substitute the expressions for $x$, $1/(c^{2r}+x^{2r})$, and $\mathrm{d}x$ into the integral from Step 1. We also transform the limits of integration: when $x=0$, $t=0$; when $x=c$, $t = c^{2r}/(2c^{2r}) = 1/2$.

$$
I_{n,c} = \frac{2r c^r}{\pi} \int_0^{1/2} (x^{n+r-1}) \left(\frac{1-t}{c^{2r}}\right) \left(\frac{x}{2r} \frac{\mathrm{d}t}{t(1-t)}\right) = \frac{c^{r-2r}}{\pi} \int_0^{1/2} x^{n+r} \frac{\mathrm{d}t}{t}
$$

Now substitute $x^{n+r} = c^{n+r} (\frac{t}{1-t})^{(n+r)/(2r)}$:

$$
I_{n,c} = \frac{c^{n}}{\pi} \int_0^{1/2} \left(\frac{t}{1-t}\right)^{\frac{n+r}{2r}} \frac{1}{t} \mathrm{d}t = \frac{c^n}{\pi} \int_0^{1/2} t^{\frac{n+r}{2r}-1} (1-t)^{-\frac{n+r}{2r}} \mathrm{d}t
$$

Using $(1-t)^{-\frac{n+r}{2r}} = (1-t)^{\frac{r-n}{2r}-1}$, we get the final integrand form:

$$
I_{n,c} = \frac{c^n}{\pi} \int_0^{1/2} t^{\frac{r+n}{2r}-1} (1-t)^{\frac{r-n}{2r}-1} \mathrm{d}t
$$

This is precisely the definition of the incomplete Beta function, $B_y(p,q)$, evaluated at $y=1/2$ with $p=\frac{r+n}{2r}$ and $q=\frac{r-n}{2r}$.

### Consistency Check for n=0 (Half-Mass)
For $n=0$, the integral represents the total probability mass up to the median $c$.

$$
\int_{0}^{c} \rho(x)\,\mathrm{d}x = \frac{c^0}{\pi} B_{1/2}\left(\frac{r}{2r}, \frac{r}{2r}\right) = \frac{1}{\pi} B_{1/2}\left(\frac{1}{2}, \frac{1}{2}\right)
$$

The integral for $B_{1/2}(1/2, 1/2)$ is $\int_0^{1/2} t^{-1/2}(1-t)^{-1/2} \mathrm{d}t$. With the substitution $t=\sin^2\theta$, this becomes $\int_0^{\pi/4} 2\mathrm{d}\theta = \pi/2$.
Therefore, $\int_{0}^{c} \rho(x)\,\mathrm{d}x = \frac{1}{\pi} \cdot \frac{\pi}{2} = \frac{1}{2}$. This confirms that $c$ is the median, consistent with §5.3.
