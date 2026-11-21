# 1.1 — Definition, analytic domain and boundary behavior

**Definition [E].** For $`r,c>0`$ and $`x>0`$, set

```math
f(x;r,c)=\frac{c^r x^{r-1}}{c^{2r}+x^{2r}} =\frac{1}{c}\frac{(x/c)^{r-1}}{1+(x/c)^{2r}}.
```

Both numerator and denominator are strictly positive. Because $`x^\alpha=\exp(\alpha\log x)`$ is real-analytic on $`(0,\infty)`$ for every real $`\alpha`$, $`f`$ is real-analytic in $`x,r,c`$ on the positive parameter domain.

**Rationality qualification.** The expression is a rational function in $`x`$ when $`r`$ is a positive integer. For a general real $`r`$ it is a rational expression in the auxiliary monomial $`(x/c)^r`$, **not** a rational function of $`x`$ in the usual algebraic sense. Rational nonintegral $`r`$ gives an algebraic function after an appropriate covering; irrational $`r`$ generally does not.

**Boundary asymptotics [E].**

```math
f(x)\sim c^{-r}x^{r-1}\quad(x\to0^+),\qquad f(x)\sim c^rx^{-r-1}\quad(x\to\infty).
```

Consequently $`\lim_{x\to0^+}f`$ is $`+\infty`$ if $`0<r<1`$, $`1/c`$ if $`r=1`$, and $`0`$ if $`r>1`$. At infinity it always tends to zero. Thus $`x=0`$ is **not** always a singular boundary point; for some integer $`r`$ the formula extends smoothly through it. A finite or vanishing limit at $`0`$ does not imply smooth extension for arbitrary noninteger $`r`$.

The parameter $`c`$ is the fixed point of multiplicative inversion $`x\mapsto c^2/x`$. Although $`f(c)=1/(2c)`$ for every $`r`$, $`f`$ has an interior maximum only for $`r>1`$, and that maximum is at $`x<c`$ (Chapter 4).

## A derivative-based monotonicity theorem (recovered from the earlier notes)

For fixed $`r,c>0`$, differentiate the quotient directly. First set $`N=c^rx^{r-1}`$ and $`D=c^{2r}+x^{2r}`$; then $`N_x=c^r(r-1)x^{r-2}`$ and $`D_x=2rx^{2r-1}`$. The quotient rule gives

```math
f_x=\frac{N_xD-ND_x}{D^2}=\frac{c^rx^{r-2}\bigl((r-1)c^{2r}-(r+1)x^{2r}\bigr)}{(c^{2r}+x^{2r})^2}.
```

All factors outside the parentheses are positive, so the sign of $`f_x`$ is the sign of $`(r-1)c^{2r}-(r+1)x^{2r}`$.

**Case $`0<r\leq1`$.** Both terms make this expression strictly negative for every $`x>0`$. Therefore $`f`$ is strictly decreasing on its domain.

**Case $`r>1`$.** The bracket is strictly decreasing in $`x`$, positive near zero, and negative for large $`x`$. Its unique root occurs at

```math
x_{\max}=c\left(\frac{r-1}{r+1}\right)^{1/(2r)}.
```

Substitute $`z=(x_{\max}/c)^{2r}=(r-1)/(r+1)`$ and use $`1+z=2r/(r+1)`$. The **correct** maximum value is

```math
f(x_{\max})=\frac{1}{c}\frac{z^{(r-1)/(2r)}}{1+z}=\frac{r+1}{2rc}\left(\frac{r-1}{r+1}\right)^{(r-1)/(2r)}.
```

The formerly proposed replacement of the exponent $`(r-1)/(2r)`$ by $`1/(2r)`$ is false in general (it happens to agree when $`r=2`$). The equivalent hyperbolic critical-point equation is $`W(x_{\max})=-1/r`$, derived in §1.4. For the full inflection classification see [Chapter 4, §4.1](../04-geometric-properties/04-01-maximum-inflection.md).
