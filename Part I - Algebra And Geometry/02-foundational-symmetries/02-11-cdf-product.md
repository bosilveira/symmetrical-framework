# 2.11 CDF Product Formula (Product of Arguments)

The cumulative distribution function (CDF), when viewed in the canonical logarithmic coordinate, satisfies a simple and natural product formula. This identity reveals the fundamental group operation for combining probabilities in this framework.

Let $\mathcal{F}(u) = F_\rho(ce^u; r, c)$. For any two log-coordinates $u_1, u_2$:

$$
\boxed{ \mathcal{F}(u_1+u_2) = \frac{2}{\pi} \arctan\left[ \tan\left(\frac{\pi}{2}\mathcal{F}(u_1)\right) \tan\left(\frac{\pi}{2}\mathcal{F}(u_2)\right) \right] }
$$

### Exposition
This identity is the true probabilistic "addition formula" for the framework. It describes how the cumulative probability transforms when the input variables are combined multiplicatively ($x_1, x_2 \to x_1 x_2/c \iff u_1, u_2 \to u_1+u_2$). It is a direct consequence of the exponential relationship between the canonical coordinate and the argument of the `arctan` in the CDF.

### Derivation

**Step 1:** Define the CDF in the linearized coordinate $u = \log(x/c)$:

$$
\mathcal{F}(u) := F_\rho(ce^u;r,c) = \frac{2}{\pi}\arctan(e^{ru})
$$

**Step 2:** Isolate the exponential term. From the definition of $\mathcal{F}(u)$, we can write:

$$
\frac{\pi}{2}\mathcal{F}(u) = \arctan(e^{ru})
$$

Taking the tangent of both sides gives:

$$
\tan\left(\frac{\pi}{2}\mathcal{F}(u)\right) = e^{ru}
$$

**Step 3:** Evaluate the CDF at the sum of coordinates, $u_1+u_2$. This corresponds to a product of the spatial variables $x_1$ and $x_2$:

$$
\mathcal{F}(u_1+u_2) = \frac{2}{\pi}\arctan(e^{r(u_1+u_2)}) = \frac{2}{\pi}\arctan(e^{ru_1} e^{ru_2})
$$

**Step 4:** Substitute the expressions from Step 2 back into the equation from Step 3:

$$
\mathcal{F}(u_1+u_2) = \frac{2}{\pi} \arctan\left[ \tan\left(\frac{\pi}{2}\mathcal{F}(u_1)\right) \tan\left(\frac{\pi}{2}\mathcal{F}(u_2)\right) \right]
$$

This completes the derivation of the natural product formula.
