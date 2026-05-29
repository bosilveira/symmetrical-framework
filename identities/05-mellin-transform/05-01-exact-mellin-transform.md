### 5.1 Exact Mellin Transform
$$
\mathcal M\{f\}(s) \;=\; \frac{\pi\,c^{s-1}}{2r}\,\sec\!\Big(\tfrac{(s-1)\pi}{2r}\Big),\qquad 1-r<\operatorname{Re} s<1+r
$$
- **Derivation.** *Substitute $u=(x/c)^{2r}$, reducing the integral to $\int_{0}^{\infty}u^{\alpha-1}/(1+u^{2})\,\mathrm du = \tfrac{\pi}{2}\csc(\alpha\pi/2)$. Convert $\csc$ to $\sec$ via $\csc(\theta) = \sec(\theta-\pi/2)$.*

Mellin Transform, Trigonometric Identities, Gamma Function, Beta Function:
$$
\mathcal{M}\{f\}(s)=\frac{\pi c^{s-1}}{2r}\sec\!\Bigl(\frac{(s-1)\pi}{2r}\Bigr)=\frac{\pi c^{s-1}}{2r}\csc\!\Bigl(\frac{(r+1-s)\pi}{2r}\Bigr)=\frac{c^{s-1}}{2r}\Gamma\!\Bigl(\frac{r+s-1}{2r}\Bigr)\Gamma\!\Bigl(\frac{r+1-s}{2r}\Bigr)=\frac{c^{s-1}}{2r}B\!\Bigl(\frac{r+s-1}{2r},\frac{r+1-s}{2r}\Bigr),
$$
where $z_1+z_2=1$.
- **Derivation.** *Substitution $u=(x/c)^{2r}$ yields the Beta integral; reflection $\Gamma(z)\Gamma(1-z)=\pi/\sin(\pi z)$ and trigonometric identities convert to sec/csc. All six functions ($\sin,\cos,\sinh,\cosh,\Gamma,B$) appear organically.*
