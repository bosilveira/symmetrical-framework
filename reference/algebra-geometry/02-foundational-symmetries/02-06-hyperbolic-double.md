# 2.6 — Two-scale product identity

Fix $`r>0`$ and $`c_1,c_2>0`$, and put $`C=\sqrt{c_1c_2}`$. Writing

```math
a=r\log(x/c_1),\quad b=r\log(x/c_2),
```

the identity $`2\cosh a\cosh b=\cosh(a+b)+\cosh(a-b)`$ gives

```math
f(x;r,c_1)f(x;r,c_2)= \frac{1}{ 2x^2\left[ \cosh(2r\log(x/C))+\cosh(r\log(c_2/c_1)) \right]}.
```

This follows algebraically from $`f(x;r,c_j)=\mathrm{sech}(a_j)/(2x)`$.

**Two checks.** The formula is symmetric in $`c_1,c_2`$. At equal scales $`c_1=c_2=c`$ it reduces to $`f(x;r,c)^2=S^2/(4x^2)`$ because $`\cosh(2ru)+1=2\cosh^2(ru)`$.

**What it does not say.** The product is generally not another member of the original two-parameter family: its denominator contains an independent constant $`\cosh(r\log(c_2/c_1))`$. This identity is an explicit hyperbolic factorization, not evidence for a new interaction term or a physical coupling without an independently specified model.

## Direct proof and unequal-resolution extension

The two-scale identity is an instance of a general product-to-sum formula, valid **even if the two resolution parameters differ**.

**Step 1.** Let $`r_1,r_2,c_1,c_2>0`$ and write $`a=r_1\log(x/c_1)`$, $`b=r_2\log(x/c_2)`$. The Rosetta Stone identity gives

```math
f(x;r_1,c_1)f(x;r_2,c_2)=\frac{1}{4x^2\cosh a\cosh b}.
```

**Step 2.** Use $`2\cosh a\cosh b=\cosh(a+b)+\cosh(a-b)`$:

```math
f(x;r_1,c_1)f(x;r_2,c_2)=\frac{1}{2x^2\bigl(\cosh(a+b)+\cosh(a-b)\bigr)}.
```

**Step 3.** The first argument can always be centered at the weighted geometric mean

```math
C_+=\left(c_1^{r_1}c_2^{r_2}\right)^{1/(r_1+r_2)},\qquad a+b=(r_1+r_2)\log(x/C_+).
```

For $`r_1\ne r_2`$ the difference can also be written $`(r_1-r_2)\log(x/C_-)`$ with $`C_-=(c_1^{r_1}/c_2^{r_2})^{1/(r_1-r_2)}`$. For $`r_1=r_2`$ it becomes the **constant** $`r\log(c_2/c_1)`$ from the original theorem. Treating the equal-resolution case by a singular $`C_-`$ is incorrect.

## Reflection exchanging two scales

Return to a common fixed $`r`$ and put $`C=\sqrt{c_1c_2}`$. Since $`\log((C^2/x)/c_1)=-\log(x/c_2)`$, the involution $`I_C(x)=C^2/x`$ exchanges the two normalized profiles:

```math
f(I_C(x);r,c_1)=\frac{x^2}{C^2}f(x;r,c_2),\qquad f(I_C(x);r,c_2)=\frac{x^2}{C^2}f(x;r,c_1).
```

The product is therefore weight-four covariant under this **new** involution. The correct positive invariant measure is $`x f(x;r,c_1)f(x;r,c_2)\,dx`$, rather than the product alone:

```math
I_{C*}\bigl(x f(x;r,c_1)f(x;r,c_2)\,dx\bigr)=x f(x;r,c_1)f(x;r,c_2)\,dx.
```

The proof follows by multiplying the two covariance factors and the Jacobian; all powers of $`x`$ and $`C`$ cancel. Hence the weighted overlap is bisected at $`x=C`$. Its exact value is computed in [§2.13](02-13-weighted-overlap.md).

## Detailed argument reduction retained from the draft

The equal-resolution proof in the original source makes the separation of the two scale variables explicit.

**Step 1.** Set $`A=r\log(x/c_1)`$ and $`B=r\log(x/c_2)`$:

```math
f(x;r,c_1)f(x;r,c_2)=\frac{\mathrm{sech}A\,\mathrm{sech}B}{4x^2}.
```

**Step 2.** Compute the symmetric and antisymmetric combinations:

```math
A+B=2r\log\left(\frac{x}{\sqrt{c_1c_2}}\right),\qquad A-B=r\log(c_2/c_1).
```

**Step 3.** Apply $`\mathrm{sech}A\,\mathrm{sech}B=2/(\cosh(A+B)+\cosh(A-B))`$:

```math
f(x;r,c_1)f(x;r,c_2)=\frac{1}{2x^2\left[\cosh\left(2r\log(x/\sqrt{c_1c_2})\right)+\cosh\left(r\log(c_2/c_1)\right)\right]}.
```

This identifies the geometric mean as a **reflection center for the paired product**, not necessarily a maximum of either factor. The draft's triple-product formula is already established in [§2.7](02-07-hyperbolic-triple.md) and is not repeated as a separate theorem.
