# 2.7 — Three-scale product and its general pattern

Let $`c_1,c_2,c_3>0`$, $`P_c=c_1c_2c_3`$, $`a_j=r\log(x/c_j)`$. From the standard expansion

```math
4\cosh a_1\cosh a_2\cosh a_3= \cosh(a_1+a_2+a_3)+\sum_{j=1}^3\cosh(a_1+a_2+a_3-2a_j),
```

we obtain **[E]**

```math
\prod_{j=1}^3f(x;r,c_j)= \frac{1}{2x^3\left[ \cosh(r\log(x^3/P_c))+ \sum_{j=1}^3\cosh(r\log(xc_j^2/P_c)) \right]}.
```

The cyclic terms arise because $`a_1+a_2+a_3-2a_j=r\log(xc_j/P_c\cdot c_j)`$.

**An $`n`$-scale extension.** For arbitrary $`n\ge1`$,

```math
\prod_{j=1}^nf(x;r,c_j) =\frac1{2^nx^n}\prod_{j=1}^n\mathrm{sech}(a_j).
```

A symmetric exponential expansion is

```math
\prod_{j=1}^n 2\cosh(a_j)= \sum_{\epsilon\in\{\pm1\}^n} \exp\left(\sum_{j=1}^n\epsilon_ja_j\right).
```

Pairing $`\epsilon`$ with $`-\epsilon`$ produces $`2^{n-1}`$ hyperbolic-cosine terms. This is an exact combinatorial product-to-sum identity; no assumption of equal scales is needed.

## Fully expanded $`n`$-scale denominator

Write $`a_j=r\log(x/c_j)`$ and group sign vectors $`\epsilon\in\{\pm1\}^n`$ into unordered pairs $`\{\epsilon,-\epsilon\}`$. The exponential expansion in the previous section gives an exact reciprocal formula with $`2^{n-1}`$ terms:

```math
\prod_{j=1}^n f(x;r,c_j)=\frac{1}{2x^n\displaystyle\sum_{[\epsilon]\in\{\pm1\}^n/\pm}\cosh\left(\sum_{j=1}^n\epsilon_j a_j\right)}.
```

**Proof.** For each $`j`$, $`1/f(x;r,c_j)=2x\cosh a_j`$. Multiplication yields $`1/\prod f=x^n\prod_j(2\cosh a_j)`$. Expand the product of $`e^{a_j}+e^{-a_j}`$ into all $`2^n`$ sign vectors; the terms for $`\epsilon`$ and $`-\epsilon`$ sum to $`2\cosh(\sum_j\epsilon_j a_j)`$. Since all hyperbolic cosine terms are positive for real arguments, this representation has no real denominator zeros.

**Symmetry and limitations.** Permuting the scales leaves the expression unchanged. Replacing every $`c_j`$ by $`\lambda c_j`$ while replacing $`x`$ by $`\lambda x`$ multiplies the product by $`\lambda^{-n}`$. These are consequences of individual scaling, not independent interaction laws. The sign-pair quotient is a combinatorial indexing device; no octonionic or higher Lie-algebra structure follows from this identity alone.

## Centrally paired scale multisets

Suppose the multiset of scales is invariant under $`c_j\mapsto C^2/c_j`$, including multiplicities. Then the corresponding hyperbolic profile product is even in $`v=\log(x/C)`$ and the positive measure

```math
x^{n-1}\prod_{j=1}^n f(x;r,c_j)\,dx=\frac{1}{2^n}\prod_{j=1}^n\mathrm{sech}\bigl(r\log(x/c_j)\bigr)\,\frac{dx}{x}
```

is invariant under $`I_C(x)=C^2/x`$. Its total mass, whenever considered, is split into equal halves by $`x=C`$. **The hypothesis on the scale multiset matters**: an arbitrary triple need not be symmetric about a common center in this sense.
