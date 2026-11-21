# 1.1 — Definition, analytic domain and boundary behavior

**Definition [E].** For $r,c>0$ and $x>0$, set
$$
f(x;r,c)=\frac{c^r x^{r-1}}{c^{2r}+x^{2r}}
       =\frac{1}{c}\frac{(x/c)^{r-1}}{1+(x/c)^{2r}}.
$$
Both numerator and denominator are strictly positive. Because $x^\alpha=\exp(\alpha\log x)$ is real-analytic on $(0,\infty)$ for every real $\alpha$, $f$ is real-analytic in $x,r,c$ on the positive parameter domain.

**Rationality qualification.** The expression is a rational function in $x$ when $r$ is a positive integer. For a general real $r$ it is a rational expression in the auxiliary monomial $(x/c)^r$, **not** a rational function of $x$ in the usual algebraic sense. Rational nonintegral $r$ gives an algebraic function after an appropriate covering; irrational $r$ generally does not.

**Boundary asymptotics [E].**
$$
f(x)\sim c^{-r}x^{r-1}\quad(x\to0^+),\qquad
f(x)\sim c^rx^{-r-1}\quad(x\to\infty).
$$
Consequently $\lim_{x\to0^+}f$ is $+\infty$ if $0<r<1$, $1/c$ if $r=1$, and $0$ if $r>1$. At infinity it always tends to zero. Thus $x=0$ is **not** always a singular boundary point; for some integer $r$ the formula extends smoothly through it. A finite or vanishing limit at $0$ does not imply smooth extension for arbitrary noninteger $r$.

The parameter $c$ is the fixed point of multiplicative inversion $x\mapsto c^2/x$. Although $f(c)=1/(2c)$ for every $r$, $f$ has an interior maximum only for $r>1$, and that maximum is at $x<c$ (Chapter 4).