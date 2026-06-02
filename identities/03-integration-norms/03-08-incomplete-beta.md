### 3.8 Truncated Moments and the Incomplete Beta Function

We now consider the moments of the normalized distribution, but truncated at the median point $x=c$. These "partial" or "truncated" moments have a closed-form solution in terms of the incomplete Beta function, $B_y(p,q)$.

For an integer moment $n < r$, the truncated moment is:

$$
\boxed{ \int_{0}^{c} x^n \rho(x;r,c)\,\mathrm dx = \frac{c^n}{\pi} B_{1/2}\left(\frac{r+n}{2r}, \frac{r-n}{2r}\right) }
$$

where $B_{y}(p,q) := \int_{0}^{y}t^{p-1}(1-t)^{q-1}\,\mathrm dt$ is the incomplete Beta function.

**Derivation:**

The result is achieved via a substitution that precisely maps the integrand to the form required by the incomplete Beta function's definition.

1.  **Set up the Integral**:
Start with the definition of the truncated moment, substituting $\rho(x;r,c) = \frac{2r}{\pi}f(x;r,c)$:

$$
I_{n,c} = \int_{0}^{c} x^n \left(\frac{2r}{\pi} \frac{c^r x^{r-1}}{c^{2r}+x^{2r}}\right) dx = \frac{2r c^r}{\pi} \int_{0}^{c} \frac{x^{n+r-1}}{c^{2r}+x^{2r}} dx
$$

2.  **Define the Substitution**:
The key is the substitution suggested in the derivation sketch, which maps the structure of $f(x)$ to the binomial structure of the Beta integrand:

$$
t = \frac{x^{2r}}{c^{2r}+x^{2r}}
$$

From this, we can derive two crucial relationships:
*   $1-t = 1 - \frac{x^{2r}}{c^{2r}+x^{2r}} = \frac{c^{2r}}{c^{2r}+x^{2r}}$
*   $\frac{t}{1-t} = \frac{x^{2r}}{c^{2r}} \implies x = c\left(\frac{t}{1-t}\right)^{1/(2r)}$

3.  **Find the Differential $dx$**:
It is easiest to find $dx$ by first finding $dt/dx$:

$$
\frac{dt}{dx} = \frac{d}{dx}\left(1 - \frac{c^{2r}}{c^{2r}+x^{2r}}\right) = -c^{2r}\left(-\frac{2rx^{2r-1}}{(c^{2r}+x^{2r})^2}\right) = \frac{2rc^{2r}x^{2r-1}}{(c^{2r}+x^{2r})^2}
$$

We can rewrite this using our expressions for $t$ and $1-t$:

$$
\frac{dt}{dx} = \frac{2r}{x} \cdot \frac{x^{2r}}{c^{2r}+x^{2r}} \cdot \frac{c^{2r}}{c^{2r}+x^{2r}} = \frac{2r}{x} t(1-t) \implies dx = \frac{x}{2r} \frac{dt}{t(1-t)}
$$

4.  **Transform the Integral**:
Now, substitute the expressions for $x$, $1/(c^{2r}+x^{2r})$, and $dx$ into the integral from Step 1:

$$
I_{n,c} = \frac{2r c^r}{\pi} \int_{x=0}^{x=c} (x^{n+r}) \cdot \frac{1}{c^{2r}+x^{2r}} \cdot \frac{dx}{x}
$$

Let's transform each piece:
*   $x^{n+r} = c^{n+r}\left(\frac{t}{1-t}\right)^{(n+r)/(2r)}$
*   $\frac{1}{c^{2r}+x^{2r}} = \frac{1-t}{c^{2r}}$
*   $\frac{dx}{x} = \frac{1}{2r}\frac{dt}{t(1-t)}$
*   Limits: When $x=0$, $t=0$. When $x=c$, $t = c^{2r}/(c^{2r}+c^{2r}) = 1/2$.

5.  **Assemble and Simplify**:

$$
I_{n,c} = \frac{2r c^r}{\pi} \int_0^{1/2} \left[c^{n+r}\left(\frac{t}{1-t}\right)^{\frac{n+r}{2r}}\right] \cdot \left[\frac{1-t}{c^{2r}}\right] \cdot \left[\frac{1}{2r}\frac{dt}{t(1-t)}\right]
$$

Combine the constant prefactors: $\frac{2r c^r}{\pi} \cdot c^{n+r} \cdot \frac{1}{c^{2r}} \cdot \frac{1}{2r} = \frac{c^n}{\pi}$.
Combine the terms involving $t$:

$$
t^{\frac{n+r}{2r}} (1-t)^{-\frac{n+r}{2r}} \cdot (1-t) \cdot t^{-1} (1-t)^{-1} = t^{\frac{n+r}{2r}-1} (1-t)^{-\frac{n+r}{2r}}
$$

My check shows a small discrepancy with the prompt's derivation sketch. Let's re-verify the power of $(1-t)$. The correct power should be: $(-\frac{n+r}{2r}) + 1 - 1 = -\frac{n+r}{2r}$. Let's compare this to the target $q-1 = \frac{r-n}{2r}-1 = \frac{r-n-2r}{2r} = \frac{-n-r}{2r}$. It matches perfectly. The algebra is correct.

The integral becomes:
$$
I_{n,c} = \frac{c^n}{\pi} \int_0^{1/2} t^{\frac{r+n}{2r}-1} (1-t)^{\frac{r-n}{2r}-1} dt
$$
This is precisely the definition of the incomplete Beta function, evaluated at $y=1/2$.

**Verification for n=0 (Half-Mass):**
For $n=0$, the integral represents the total probability mass up to the median `c`.
$$
\int_{0}^{c} \rho(x)\,\mathrm dx = \frac{c^0}{\pi} B_{1/2}\left(\frac{r}{2r}, \frac{r}{2r}\right) = \frac{1}{\pi} B_{1/2}\left(\frac{1}{2}, \frac{1}{2}\right)
$$
The integral for $B_{1/2}(1/2, 1/2)$ is $\int_0^{1/2} t^{-1/2}(1-t)^{-1/2} dt$. With the substitution $t=\sin^2\theta$, this becomes $\int_0^{\pi/4} 2d\theta = \pi/2$.
Therefore, $\int_{0}^{c} \rho(x)\,\mathrm dx = \frac{1}{\pi} \cdot \frac{\pi}{2} = \frac{1}{2}$. This confirms that $c$ is the median, consistent with §3.3.

***

### Unifying Remark on Section 3

This concludes the study of the function's integral properties. A single, elementary antiderivative in terms of the **arctangent** function (§3.1) serves as the ultimate source for every closed-form integral derived in this section. The analysis of the $L^n$ norms reveals a second, deeper structural heart: the substitution $u=(x/c)^{2r}$ which maps the integral to the **Euler Beta function** (§3.5), governing both Lebesgue and multiplicative measures. Finally, the bisection of the total mass at the point $x=c$ (§3.3, §3.8) is now fully understood as the direct integral consequence of the fundamental **Möbius inversion symmetry** from Section 2.
