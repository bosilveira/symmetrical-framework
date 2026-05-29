## 4. Differential Structure & Ward Identities

### 4.1 Master Nonlinear ODE

$$
\boxed{\;x^{2}(f')^{2} + 2x f f' + (1-r^{2})f^{2} + 4r^{2}x^{2}f^{4} \;=\; 0.\;}
$$

**Derivation.** Take the logarithmic derivative of §1.1:
$$
\frac{f'}{f} = \frac{r-1}{x} - \frac{2r\,x^{2r-1}}{c^{2r}+x^{2r}} \;=\; \frac{r-1}{x} - \frac{r}{x}\cdot\frac{2x^{2r}}{c^{2r}+x^{2r}}.
$$
Using $W = (x^{2r}-c^{2r})/(x^{2r}+c^{2r})$ from §1.4, $2x^{2r}/(c^{2r}+x^{2r}) = 1+W$, so $xf'/f = (r-1) - r(1+W) = -1 - rW$. Rewrite:
$$
xf' + f = -rfW \quad\Longrightarrow\quad (xf'+f)^{2} = r^{2}f^{2}W^{2}.
$$
Use the half‑density identity §1.5: $W^{2} = 1 - \operatorname{sech}^{2}(r\log(x/c)) = 1 - 4x^{2}f^{2}$. Substitute:
$$
(xf'+f)^{2} = r^{2}f^{2}(1-4x^{2}f^{2}),
$$
i.e. $x^{2}(f')^{2} + 2xff' + f^{2} = r^{2}f^{2} - 4r^{2}x^{2}f^{4}$. Rearrange to obtain the boxed identity.
