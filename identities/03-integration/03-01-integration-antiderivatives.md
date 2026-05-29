## 3. Integration, Antiderivatives, and $L^{n}$ Norms

### 3.1 First Antiderivative

$$
\int f(x;r,c)\,\mathrm dx \;=\; \frac{1}{r}\arctan\!\bigl((x/c)^{r}\bigr) + \text{const}.
$$

**Derivation.** Set $u=(x/c)^{r}$, so $\mathrm du/\mathrm dx = (r/c^{r})\,x^{r-1}$. Then
$$
\frac{\mathrm d}{\mathrm dx}\!\left[\tfrac{1}{r}\arctan u\right] = \tfrac{1}{r}\cdot\frac{1}{1+u^{2}}\cdot\frac{r x^{r-1}}{c^{r}} = \frac{x^{r-1}/c^{r}}{1+(x/c)^{2r}} = \frac{c^{r}x^{r-1}}{c^{2r}+x^{2r}} = f(x;r,c).
$$
