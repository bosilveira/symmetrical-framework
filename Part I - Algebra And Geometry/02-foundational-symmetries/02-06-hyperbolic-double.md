# 2.6 — Two-scale product identity

Fix $r>0$ and $c_1,c_2>0$, and put $C=\sqrt{c_1c_2}$. Writing

```math
a=r\log(x/c_1),\quad b=r\log(x/c_2),
```

the identity $2\cosh a\cosh b=\cosh(a+b)+\cosh(a-b)$ gives

```math
f(x;r,c_1)f(x;r,c_2)= \frac{1}{ 2x^2\left[ \cosh(2r\log(x/C))+\cosh(r\log(c_2/c_1)) \right]}.
```

This follows algebraically from $f(x;r,c_j)=\mathrm{sech}(a_j)/(2x)$.

**Two checks.** The formula is symmetric in $c_1,c_2$. At equal scales $c_1=c_2=c$ it reduces to $f(x;r,c)^2=S^2/(4x^2)$ because $\cosh(2ru)+1=2\cosh^2(ru)$.

**What it does not say.** The product is generally not another member of the original two-parameter family: its denominator contains an independent constant $\cosh(r\log(c_2/c_1))$. This identity is an explicit hyperbolic factorization, not evidence for a new interaction term or a physical coupling without an independently specified model.
