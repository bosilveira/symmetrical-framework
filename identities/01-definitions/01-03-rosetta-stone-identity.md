### 1.3 Rosetta Stone Identity

$$
\boxed{\;2x\,f(x;r,c)\;=\;\mathrm{sech}\!\bigl(r\log(x/c)\bigr).\;}
$$

**Derivation.** Let $z=r\log(x/c)$, so $e^{z}=(x/c)^{r}$ and $e^{-z}=(c/x)^{r}$. By definition,
$$
\operatorname{sech} z = \frac{2}{e^{z}+e^{-z}} = \frac{2}{(x/c)^{r}+(c/x)^{r}} = \frac{2\,c^{r}x^{r}}{c^{2r}+x^{2r}} = 2x\cdot\frac{c^{r}x^{r-1}}{c^{2r}+x^{2r}} = 2x\,f(x;r,c).
$$
The identity is therefore an algebraic tautology.
