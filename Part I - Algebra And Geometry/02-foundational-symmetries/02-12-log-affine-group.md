# 2.12 — The log-affine transformation group and its action on the family

**Status [E].** This section enlarges the scale and inversion identities to an exact group action on the *normalized probability family*. The group itself is a standard affine group of the real line; no exceptional-group identification is implied.

## Dimensionless logarithmic coordinates

Fix an arbitrary positive reference scale $x_*$ and set $z=\log(x/x_*)$, $\alpha=\log(c/x_*)$. The canonical center displacement stays $u=z-\alpha=\log(x/c)$.

For $a\ne0$ and $b\in\mathbb R$, define a transformation of $z$ by $z'=az+b$. In the original positive variable it is

```math
T_{a,b}(x)=x_*\exp\bigl(a\log(x/x_*)+b\bigr).
```

This formula preserves units because only dimensionless ratios occur under the logarithm. It is strictly increasing if $a>0$ and strictly decreasing if $a<0$.

## Composition law and subgroups

**Step 1.** Apply two transformations in succession: first $z\mapsto a'z+b'$, then $z\mapsto az+b$. Their composition is $z\mapsto aa'z+(b+ab')$.

```math
T_{a,b}\circ T_{a',b'}=T_{aa',\,b+ab'},\qquad T_{a,b}^{-1}=T_{1/a,\,-b/a}.
```

**Step 2.** Thus the maps form the real affine group $\mathbb R\rtimes\mathbb R^\times$ in logarithmic coordinates. Its orientation-preserving component is $a>0$; the subgroup $a\in\{1,-1\}$ comprises translations and reflections, isomorphic to $\mathbb R\rtimes C_2$.

**Step 3.** Ordinary joint dilation $x\mapsto\lambda x$ corresponds to $a=1$, $b=\log\lambda$. The centered inversion $x\mapsto c^2/x$ corresponds to $a=-1$, $b=2\alpha$, because

```math
z'=2\alpha-z,\qquad x'=x_*\exp(2\alpha-z)=\frac{c^2}{x}.
```

A fixed-center inversion is one reflection in this affine group, not a generator of the full group by itself.

## Equivariance of the normalized distribution

Let $X$ have density $\rho(x;r,c)$, and let $Y=T_{a,b}(X)$. Its transformed scale $c'$ and resolution $r'$ are

```math
c'=x_*\exp(a\alpha+b),\qquad r'=\frac{r}{|a|}.
```

**Proof.** With $Z=\log(X/x_*)$, the probability density is $q_{r,\alpha}(z)=r\,\mathrm{sech}(r(z-\alpha))/\pi$. Under $Z'=aZ+b$, the density is

```math
q_{Z'}(z')=\frac{r}{\pi|a|}\mathrm{sech}\left(\frac r a(z'-(a\alpha+b))\right)=\frac{r'}{\pi}\mathrm{sech}(r'(z'-\alpha')).
```

Because $\mathrm{sech}$ is even, the last equality holds for either sign of $a$. Return to $Y=x_*e^{Z'}$ using $dy=y\,dz'$ to conclude

```math
(T_{a,b})_*(\rho(x;r,c)\,dx)=\rho(y;r',c')\,dy.
```

For the unnormalized kernel the total mass transforms as

```math
(T_{a,b})_*(f(x;r,c)\,dx)=\frac1{|a|}f(y;r',c')\,dy.
```

This is exact family-level equivariance. **Individual** distributions are invariant only under the stabilizer conditions $r'=r$ and $c'=c$. With $r>0$ this requires $|a|=1$; the two choices are the identity and centered inversion in logarithmic coordinates.

## Group-theoretic caution

The transformations above are standard consequences of a symmetric location-scale density in logarithmic coordinates. They do not furnish a faithful action of an exceptional group such as $E_8$, a tetrahedral $V_4$, or an octonion algebra without additional independently specified structures.
