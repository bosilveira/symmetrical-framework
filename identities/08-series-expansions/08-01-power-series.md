## 8. Series Expansions, Decompositions, and Products

### 8.1 Geometric Power Series (Complementary Domains)

$$
f(x;r,c) = \begin{cases}\displaystyle\sum_{k=0}^{\infty}(-1)^{k}c^{-r(2k+1)}\,x^{r(2k+1)-1}, & 0<x<c,\\[6pt] \displaystyle\sum_{k=0}^{\infty}(-1)^{k}c^{r(2k+1)}\,x^{-r(2k+1)-1}, & x>c.\end{cases}
$$

**Derivation.** For $0<x<c$, factor $f = c^{-r}x^{r-1}/[1+(x/c)^{2r}]$ and apply the geometric series $1/(1+z) = \sum(-1)^{k}z^{k}$ with $z = (x/c)^{2r}$, $|z|<1$. For $x>c$, factor instead $f = c^{r}x^{-r-1}/[1+(c/x)^{2r}]$ and expand with $z = (c/x)^{2r}$. The two expansions match continuously at $x=c$ (Abel summable).
