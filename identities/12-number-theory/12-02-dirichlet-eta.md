This is a perfect and necessary companion to the Zeta variation. By alternating the signs, you generate the Dirichlet eta function (also known as the alternating zeta function), which famously possesses better convergence properties than the standard Riemann Zeta function.

Here is the revised and formatted version for your GitHub repository.

***

### 12.2 Dirichlet Eta Variation (Alternating Sum)

By alternating the signs of the terms in our arithmetically smoothed sum, we can connect the function family to the **Dirichlet eta function**, $\eta(s)$. This variation is analytically valuable because the alternating series converges over a strictly wider domain in the complex plane than the standard Zeta series.

Let the alternating Dirichlet-smoothed function be defined as:
$$
F_{\text{alt}}(x) := \sum_{n=1}^{\infty}(-1)^{n-1}f(nx;r,c)
$$
Its Mellin transform is modulated perfectly by the Dirichlet eta function:
$$
\boxed{\; \mathcal M\{F_{\text{alt}}\}(s) = \eta(s)\,\mathcal M\{f\}(s) \;}
$$
where $\eta(s) = (1-2^{1-s})\zeta(s)$.

**Derivation:**

The derivation mirrors the Zeta case (§12.1), simply carrying the alternating sign through the linear transform.

1.  **Apply the Scaling Rule**:
    Using the Mellin scaling rule $\mathcal M\{f(nx)\}(s) = n^{-s}\mathcal M\{f\}(s)$, the transform of the general term is:
    $$
    \mathcal M\{(-1)^{n-1}f(nx)\}(s) = (-1)^{n-1} n^{-s}\mathcal M\{f\}(s)
    $$

2.  **Integrate the Infinite Sum**:
    Applying the Mellin transform to the infinite sum and passing the integral inside (justified by uniform convergence):
    $$
    \mathcal M\{F_{\text{alt}}\}(s) = \sum_{n=1}^{\infty} \mathcal M\{(-1)^{n-1}f(nx;r,c)\}(s) = \sum_{n=1}^{\infty} (-1)^{n-1} n^{-s}\mathcal M\{f\}(s)
    $$

3.  **Factor and Identify Eta**:
    Factoring out the common $\mathcal M\{f\}(s)$ term leaves the classical definition of the Dirichlet eta function:
    $$
    \mathcal M\{F_{\text{alt}}\}(s) = \left( \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^s} \right) \mathcal M\{f\}(s) = \eta(s)\mathcal M\{f\}(s)
    $$
    The relationship $\eta(s) = (1-2^{1-s})\zeta(s)$ is a standard identity derived by separating the even and odd terms of the Zeta series.

**Analytic Advantage (Extended Convergence):**

While the Riemann Zeta sum from §12.1 requires $\operatorname{Re}(s) > 1$ to converge, the alternating Dirichlet eta sum converges for all **$\operatorname{Re}(s) > 0$**. 

Consequently, the strip of convergence for this alternating transform is strictly wider. We only require the overlap between $\operatorname{Re}(s) > 0$ and the base Mellin strip $1-r < \operatorname{Re}(s) < 1+r$. 
Thus, $\mathcal M\{F_{\text{alt}}\}(s)$ is valid in the extended strip:
$$
\max(0, 1-r) < \operatorname{Re}(s) < 1+r
$$
For any $r \ge 1$, this identity is valid starting all the way from the imaginary axis ($\operatorname{Re}(s) > 0$), covering the critical line $\operatorname{Re}(s) = 1/2$ and the symmetry line $\operatorname{Re}(s) = 1$.
