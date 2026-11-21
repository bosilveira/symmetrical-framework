# 4.2 — Arc length and dimensional normalization

For a graph $(x,F(x))$ in an **abstract Euclidean coordinate plane**, the arc element is

```math
ds=\sqrt{1+[F'(x)]^2}\,dx.
```

Taking $F=f(x;r,c)$ in fixed numerical units yields the historical formula

```math
L_f(a,b)=\int_a^b\sqrt{1+f_x(x;r,c)^2}\,dx,
```

where

```math
f_x=\frac{c^rx^{r-2}\big[(r-1)c^{2r}-(r+1)x^{2r}\big]} {(c^{2r}+x^{2r})^2}.
```

**Units matter.** If $x,c$ carry units of length, $f$ carries units $1/\text{length}$, so the pair $(x,f)$ does not by itself define a physical Euclidean length without choosing a scale for the vertical axis. A canonical dimensionally homogeneous option is

```math
Y(x)=c^2f(x;r,c),\quad t=x/c,\quad k_r(t)=cf(ct;r,c).
```

Then $(x,Y)=(ct,ck_r(t))$, and its length is

```math
L_{\rm scaled}(a,b)=c\int_{a/c}^{b/c} \sqrt{1+[k'_r(t)]^2}\,dt.
```

More generally $Y=\alpha f$ is legitimate with an explicit positive vertical magnification $\alpha$ having units of length squared.

**Exact dimensionless slope [E].**

```math
k_r'(t)=\frac{t^{r-2}[(r-1)-(r+1)t^{2r}]}{(1+t^{2r})^2}.
```

This exact formula supplies the algebraic radicand for the rigorous discussion of genus in §§4.4 and 4.7. No elliptic/hyperelliptic claim follows simply from the presence of a quartic denominator.
