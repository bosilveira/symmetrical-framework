## 2. Foundational Symmetries and Scale Products

### 2.1 Value, Slope, and Curvature at the Symmetry Point

$$
f(c;r,c)=\frac{1}{2c},\qquad \partial_{x}f\big|_{x=c}=-\frac{1}{2c^{2}},\qquad \partial_{xx}f\big|_{x=c}=\frac{2-r^{2}}{2c^{3}}.
$$

**Derivation.** Substitute $x = c$ in $f$, $f'$, $f''$. For $f$, the denominator becomes $2c^{2r}$ and numerator $c^{r}\cdot c^{r-1}=c^{2r-1}$, giving $1/(2c)$. For $f'$, the explicit derivative (§4.5) evaluates to $-1/(2c^{2})$. The second derivative requires either differentiating $f'$ symbolically or expanding $f$ in a Taylor series around $u=\log(x/c)=0$ using §8.2: $2xf = \operatorname{sech}(ru) \approx 1 - (ru)^2/2 + 5(ru)^4/24-\ldots$. The slope is *independent of $r$* (every member of the family shares the tangent at $(c,1/(2c))$). The curvature *changes sign* at $r=\sqrt 2$.
