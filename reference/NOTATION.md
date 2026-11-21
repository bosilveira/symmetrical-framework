# Canonical Notation

**Status: editorial definitions**, not a theorem. Unless a section explicitly changes the domain, take `x,c,r>0` and, in the coupled Master equation, `\mu>0`.

| Symbol | Meaning | Non-confusion rule |
|---|---|---|
| $`x`$ | positive spatial coordinate | Not the logarithmic coordinate |
| $`c`$ | positive center and scale | Remain explicit in coordinate changes |
| $`r`$ | positive resolution/shape parameter | Do not suppress unless an explicit special case |
| $`\xi=x/c`$ | dimensionless multiplicative coordinate | Never call this $`u`$ |
| $`u=\log(x/c)`$ | **canonical logarithmic coordinate** | $`x=ce^u`$ |
| $`\theta=ru`$ | hyperbolic argument | Not equal to $`u`$ for generic $`r`$ |
| $`D=x\partial_x=\partial_u`$ | Euler derivative at fixed $`c`$ | Not a $`c`$-derivative |
| $`\mu`$ | positive amplitude/cubic coupling | Keep factors of $`\sqrt\mu`$ |

## Original kernel and circle

```math
f(x;r,c)=\frac{c^r x^{r-1}}{c^{2r}+x^{2r}}=\frac{1}{2x}\mathrm{sech}(r\log(x/c)).
```

```math
S(u)=2xf(x;r,c)=\mathrm{sech}(ru),\qquad W(u)=\tanh(ru),\qquad S^2+W^2=1.
```

```math
\rho(x;r,c)=\frac{2r}{\pi}f(x;r,c),\qquad f(x;r,c)\,dx=\frac12S(u)\,du.
```

The **positive measure** associated with $`f(x)\,dx` is invariant under $`x\mapsto c^2/x`$. The oriented differential form changes sign. Do not substitute the distinct Haar measure $`dx/x`$ into this invariance claim.

## The cubic Master and its energy

```math
f_\mu(x;r,c)=\frac{1}{\sqrt\mu}f(x;r,c),\quad y(u)=2xf_\mu(x),\quad \varepsilon=y_u^2-r^2y^2+\mu r^2y^4.
```

```math
y_{uu}=r^2y-2\mu r^2y^3,\quad x^2f_{\mu,xx}+3xf_{\mu,x}+(1-r^2)f_\mu+8\mu r^2x^2f_\mu^3=0.
```

A **general Master solution** is not necessarily the hyperbolic-secant separatrix. The reciprocal $`J=1/y`$ requires nonvanishing $`y`$ and is linear only on the zero-energy branch; the positive square root $`Y=\sqrt J`$ requires $`y>0`$.

The shifted center $`u_0`$ corresponds to $`x_0=ce^{u_0}`$, hence $`u-u_0=\log(x/x_0)`$. Historical $`t=\log x`$ requires a declared reference unit if $`x`$ has dimensions.

## Other conventions

Jacobi $`\mathrm{dn}(z\mid m)`$, $`\mathrm{cn}(z\mid m)`$, and $`K(m)`$ use the elliptic **parameter** $`m`$ rather than its square-root modulus. Independent Mellin variable $`s`$, Fourier variable $`k`$, and modular variable $`\tau`$ are not interchangeable.

A physical or geometric variable named $`c`$, $`J`$ or $`r`$ in an outside source must be mapped explicitly to the framework dictionary. A numerical coincidence or shared symbol does not establish an isomorphism.

See [MARKDOWN_STYLE.md](../MARKDOWN_STYLE.md) for GitHub math delimiters.
