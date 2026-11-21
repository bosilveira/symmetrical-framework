# 2.7 — Three-scale product and its general pattern

Let $c_1,c_2,c_3>0$, $P_c=c_1c_2c_3$, $a_j=r\log(x/c_j)$. From the standard expansion

```math
4\cosh a_1\cosh a_2\cosh a_3= \cosh(a_1+a_2+a_3)+\sum_{j=1}^3\cosh(a_1+a_2+a_3-2a_j),
```

we obtain **[E]**

```math
\prod_{j=1}^3f(x;r,c_j)= \frac{1}{2x^3\left[ \cosh(r\log(x^3/P_c))+ \sum_{j=1}^3\cosh(r\log(xc_j^2/P_c)) \right]}.
```

The cyclic terms arise because $a_1+a_2+a_3-2a_j=r\log(xc_j/P_c\cdot c_j)$.

**An $n$-scale extension.** For arbitrary $n\ge1$,

```math
\prod_{j=1}^nf(x;r,c_j) =\frac1{2^nx^n}\prod_{j=1}^n\mathrm{sech}(a_j).
```

A symmetric exponential expansion is

```math
\prod_{j=1}^n 2\cosh(a_j)= \sum_{\epsilon\in\{\pm1\}^n} \exp\left(\sum_{j=1}^n\epsilon_ja_j\right).
```

Pairing $\epsilon$ with $-\epsilon$ produces $2^{n-1}$ hyperbolic-cosine terms. This is an exact combinatorial product-to-sum identity; no assumption of equal scales is needed.
