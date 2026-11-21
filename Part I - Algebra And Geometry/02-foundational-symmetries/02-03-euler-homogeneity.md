# 2.3 — Euler homogeneity in $x$ and $c$

For fixed $r>0$, $f(x;r,c)=c^{-1}k(x/c;r)$ implies

```math
f(\lambda x;r,\lambda c)=\lambda^{-1}f(x;r,c) \qquad(\lambda>0).
```

Differentiate at $\lambda=1$ to obtain Euler's identity **[E]**:

```math
(x\partial_x+c\partial_c+1)f=0.
```

Conversely, on the connected positive quadrant, a differentiable solution of this PDE has the form $c^{-1}k(x/c)$ for some function $k$, by characteristics. This converse does not select the framework's specific $k$.

**Commutation with inversion.** Inversions respect joint scaling:

```math
I_{\lambda c}(\lambda x)=\lambda I_c(x).
```

Hence scale covariance and inversion covariance are compatible but logically separate conditions.

**Scale transport of integrals.** With $x=c\xi$,

```math
\int_0^\infty x^{a-1}f(x;r,c)^p\,dx =c^{a-p} \int_0^\infty \xi^{a-1}k(\xi;r)^p\,d\xi,
```

in its convergence domain. This furnishes a clean, falsifiable dimensional check for every claimed integral identity.

**Derivative conventions.** The Euler vector field $x\partial_x+c\partial_c$ keeps the ratio $x/c$ fixed. It is **not** the same as the operator $D_x=x\partial_x$ with $c$ fixed; the latter equals $\partial_u$ in the logarithmic chart.

## Infinitesimal generators and parameter differentiation

Fix a reference scale $x_*>0$. The dimensionless logarithmic coordinates $\alpha=\log(c/x_*)$ and $y=\log(x/x_*)$ make the distinction between simultaneous scale transport and fixed-center dilation transparent. Their difference is $u=y-\alpha=\log(x/c)$.

At fixed $r$, differentiating the Rosetta Stone identity in $x$ and $c$ separately yields

```math
x\partial_x\log f=-(1+rW),\qquad c\partial_c\log f=rW.
```

Adding them gives $(x\partial_x+c\partial_c)\log f=-1$, the logarithmic form of Euler homogeneity. Differentiating in resolution at fixed $x,c$ gives another exact score:

```math
\partial_r\log f=-uW.
```

The derivative with respect to $\alpha=\log(c/x_*)$ is a location derivative; the derivative in $r$ is a scale/shape derivative in the logarithmic coordinate. They must not be confused with derivatives taken at fixed $u$.

## Commuting group actions on the coordinate-scale pair

Define $D_\lambda(x,c)=(\lambda x,\lambda c)$ and $I(x,c)=(c^2/x,c)$, where $\lambda>0$. A direct calculation gives

```math
D_\lambda\circ I=I\circ D_\lambda,\qquad I^2=\mathrm{id},\qquad D_\lambda D_\eta=D_{\lambda\eta}.
```

The transformations generate an action of the direct product $\mathbb R_{>0}\times C_2$ on the *pair* $(x,c)$. On the normalized coordinate $u=\log(x/c)$, $D_\lambda$ acts trivially and $I$ acts by $u\mapsto-u$. The dependent function transforms by the nontrivial weights specified in §§2.2–2.3; it is **not** invariant pointwise under both generators.

## Explicit factorization from the source derivation

The original proof verifies the scale law directly in the defining powers, before applying Euler's theorem.

**Step 1.** Substitute $(\lambda x,\lambda c)$ into the defining numerator and denominator:

```math
f(\lambda x;r,\lambda c)=\frac{\lambda^{2r-1}c^rx^{r-1}}{\lambda^{2r}(c^{2r}+x^{2r})}.
```

**Step 2.** Cancel $\lambda^{2r}$ and differentiate at $\lambda=1$:

```math
f(\lambda x;r,\lambda c)=\lambda^{-1}f(x;r,c),\qquad x\partial_xf+c\partial_cf=-f.
```

**Step 3.** Replace $c$ by $c/\lambda$ in the joint formula:

```math
f(\lambda x;r,c)=\lambda^{-1}f(x;r,c/\lambda).
```

The third equality is **not** a fixed-$c$ homogeneity law: it requires the transformed parameter $c/\lambda$. The result agrees with the characteristic argument at the beginning of this section.
