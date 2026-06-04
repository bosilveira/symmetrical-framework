### 5.4 Operational Algebra Rules

The power of the Mellin transform lies in its ability to convert complex operations like differentiation and scaling in the original function space (`x`-space) into simple algebraic manipulations in the transform space (`s`-space). The table below summarizes these key operational rules.

| **Operation on f(x)** | **Effect on Mellin Transform $\mathcal{M}\{f\}(s)$** | **Justification** |
| :--- | :--- | :--- |
| Scaling: $f(\lambda x)$, $\lambda>0$ | $\lambda^{-s} \, \mathcal{M}\{f\}(s)$ | Substitution: $u = \lambda x$ |
| Multiplication by power: $x^a f(x)$ | $\mathcal{M}\{f\}(s+a)$ | Shift in exponent of kernel $x^{s-1}$ |
| Power of argument: $f(x^b)$, $b>0$ | $\frac{1}{b} \, \mathcal{M}\{f\}(s/b)$ | Substitution: $u = x^b$ |
| Differentiation: $f'(x)$ | $-(s-1) \, \mathcal{M}\{f\}(s-1)$ | Integration by parts |
| Integration: $\int_0^x f(t) \,dt$ | $-\frac{1}{s} \, \mathcal{M}\{f\}(s+1)$ | Inverse of differentiation rule |
| $n$-th Derivative: $f^{(n)}(x)$ | $(-1)^n \frac{\Gamma(s)}{\Gamma(s-n)} \, \mathcal{M}\{f\}(s-n)$ | Iterated integration by parts |

---
**Derivations:**

These are standard operational properties of the Mellin transform. Each rule is derived directly from the definition, $\mathcal{M}\{g\}(s) = \int_0^\infty x^{s-1} g(x) \,dx$, assuming that all operations are valid and that any boundary terms from integration by parts vanish within the common strip of convergence.

*   **Scaling, $g(x) = f(\lambda x)$**:
Let $u = \lambda x$, so $x = u/\lambda$ and $dx = du/\lambda$.
$$
\mathcal{M}\{g\}(s) = \int_0^\infty (u/\lambda)^{s-1} f(u) (du/\lambda) = \lambda^{-s} \int_0^\infty u^{s-1} f(u) du = \lambda^{-s} \mathcal{M}\{f\}(s)
$$
*   **Multiplication by power, $g(x) = x^a f(x)$**:
$$
\mathcal{M}\{g\}(s) = \int_0^\infty x^{s-1} [x^a f(x)] dx = \int_0^\infty x^{(s+a)-1} f(x) dx = \mathcal{M}\{f\}(s+a)
$$
*   **Differentiation, $g(x) = f'(x)$**:
We use integration by parts, $\int u \,dv = uv - \int v \,du$, with $u=x^{s-1}$ and $dv=f'(x)dx$.
$$
\mathcal{M}\{f'\}(s) = \int_0^\infty x^{s-1} f'(x) dx = \left[ x^{s-1} f(x) \right]_0^\infty - \int_0^\infty (s-1)x^{s-2} f(x) dx
$$
The boundary term $[x^{s-1}f(x)]_0^\infty$ vanishes for `s` within the strip of convergence. The remaining integral is:
$$
-(s-1) \int_0^\infty x^{(s-1)-1} f(x) dx = -(s-1)\mathcal{M}\{f\}(s-1)
$$
*   **$n$-th Derivative**: This rule follows from applying the differentiation rule `n` times. The term $\frac{\Gamma(s)}{\Gamma(s-n)}$ is the Pochhammer symbol $(s-1)_n$ which arises from the repeated shifts: $-(s-1)$, then $-((s-1)-1)$, etc.

These rules provide a powerful "dictionary" for translating between the function space and the transform space. For instance, the Euler homogeneity identity (§2.3), $x f' + c f'_c + f = 0$, can be transformed into an algebraic equation relating different Mellin transforms, providing another consistency check on the framework.
