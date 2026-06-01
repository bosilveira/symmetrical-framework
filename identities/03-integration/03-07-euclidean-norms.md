### 3.7 $L^2$ Norm Closed Forms (Special Cases of $n=2$)

The general $L^n$ norm integrals derived in §3.5 and §3.6 simplify beautifully for the case $n=2$. By leveraging identities of the Euler Gamma function, we can express these $L^2$ norms in terms of elementary trigonometric functions. These results are particularly important in fields like quantum mechanics and signal processing, where the $L^2$ norm often represents energy or total probability.

**Case 1: Lebesgue Measure ($dx$)**

$$
\boxed{ \int_{0}^{\infty} [f(x;r,c)]^2 \,\mathrm dx = \frac{\pi}{4r^2 c \sin(\pi / 2r)}, \quad \text{for } r > \frac{1}{2} }
$$

**Case 2: Haar Measure ($dx/x$)**

$$
\boxed{ \int_{0}^{\infty} [f(x;r,c)]^2 \,\frac{\mathrm dx}{x} = \frac{\pi}{2r^2 c^2 \sin(\pi / r)}, \quad \text{for } r > 1 }
$$

---
**Derivation:**

The core of both derivations is the conversion of the Beta function from the general formulas into a trigonometric expression via the Gamma function's reflection formula.

**General Tool: Simplifying the Beta Function for n=2**

For $n=2$, the arguments of the Beta function in §3.5 and §3.6 always sum to 2. Let the arguments be $p$ and $q$. Then $p+q=2$, or $q=2-p$. We can simplify $B(p, 2-p)$ as follows:

1.  **Beta to Gamma:** $B(p, 2-p) = \frac{\Gamma(p)\Gamma(2-p)}{\Gamma(p+2-p)} = \frac{\Gamma(p)\Gamma(2-p)}{\Gamma(2)}$.
2.  **Evaluate $\Gamma(2)$:** Since $\Gamma(2) = 1! = 1$, we have $B(p, 2-p) = \Gamma(p)\Gamma(2-p)$.
3.  **Gamma Recursion:** Use the identity $\Gamma(z+1)=z\Gamma(z)$. For $z=1-p$, we get $\Gamma(2-p) = (1-p)\Gamma(1-p)$.
4.  **Euler's Reflection Formula:** Use the identity $\Gamma(p)\Gamma(1-p) = \frac{\pi}{\sin(\pi p)}$.
5.  **Combine:** $B(p, 2-p) = \Gamma(p)(1-p)\Gamma(1-p) = (1-p)[\Gamma(p)\Gamma(1-p)] = (1-p)\frac{\pi}{\sin(\pi p)}$.

We now apply this tool to each case.

**Derivation of the Lebesgue Measure ($dx$) Formula:**

1.  **Set n=2 in §3.5**: The prefactor is $\frac{c^{-1}}{2r}$. The first argument of the Beta function is:

$$
p = \frac{(r-1)n+1}{2r} \Big|_{n=2} = \frac{2r-2+1}{2r} = \frac{2r-1}{2r} = 1 - \frac{1}{2r}
$$

2.  **Evaluate the Beta Function**: Using our tool with this value of `p`:
*   $1-p = 1 - (1 - \frac{1}{2r}) = \frac{1}{2r}$.
*   $\sin(\pi p) = \sin(\pi(1 - \frac{1}{2r})) = \sin(\pi - \frac{\pi}{2r}) = \sin(\frac{\pi}{2r})$.
*   $B(\dots) = (1-p)\frac{\pi}{\sin(\pi p)} = \frac{1}{2r} \frac{\pi}{\sin(\pi/2r)}$.
3.  **Assemble the Final Result**:

$$
\int_{0}^{\infty}f^2\,\mathrm dx = \frac{c^{-1}}{2r} \cdot \left[ \frac{\pi}{2r \sin(\pi/2r)} \right] = \frac{\pi}{4r^2 c \sin(\pi/2r)}
$$

The convergence condition requires the Beta function arguments to be positive. $p>0$ implies $1 - 1/(2r) > 0$, which means $r > 1/2$.

**Derivation of the Haar Measure ($dx/x$) Formula:**

1.  **Set n=2 in §3.6**: The prefactor is $\frac{c^{-2}}{2r}$. The first argument of the Beta function is:

$$
p = \frac{n(r-1)}{2r} \Big|_{n=2} = \frac{2(r-1)}{2r} = \frac{r-1}{r} = 1 - \frac{1}{r}
$$

2.  **Evaluate the Beta Function**:
*   $1-p = 1 - (1 - \frac{1}{r}) = \frac{1}{r}$.
*   $\sin(\pi p) = \sin(\pi(1 - \frac{1}{r})) = \sin(\pi - \frac{\pi}{r}) = \sin(\frac{\pi}{r})$.
*   $B(\dots) = (1-p)\frac{\pi}{\sin(\pi p)} = \frac{1}{r} \frac{\pi}{\sin(\pi/r)}$.
3.  **Assemble the Final Result**:

$$
\int_{0}^{\infty}f^2\,\frac{\mathrm dx}{x} = \frac{c^{-2}}{2r} \cdot \left[ \frac{\pi}{r \sin(\pi/r)} \right] = \frac{\pi}{2r^2 c^2 \sin(\pi/r)}
$$

The convergence condition $p>0$ implies $1 - 1/r > 0$, which means $r > 1$.
