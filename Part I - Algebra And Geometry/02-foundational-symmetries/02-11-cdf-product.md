# 2.11 — Global CDF group law induced by multiplication

Define $\mathcal F(u)=F(ce^u)=2\arctan(e^{ru})/\pi$ and the bijection

```math
\Theta(v)=\tan\left(\frac{\pi v}{2}\right):(0,1)\longrightarrow(0,\infty).
```

Then $\Theta(\mathcal F(u))=e^{ru}$. Thus **[E]**

```math
\mathcal F(u_1+u_2) =\frac2\pi\arctan\bigl(\Theta(\mathcal F(u_1))\, \Theta(\mathcal F(u_2))\bigr).
```

**Abstract group structure.** On $(0,1)$ define

```math
v\odot w=\Theta^{-1}(\Theta(v)\Theta(w)).
```

This is an associative, commutative group, because $\Theta$ transports multiplication on $(0,\infty)$. Its identity is $1/2$ and its inverse is $v\mapsto1-v$:

```math
v\odot\tfrac12=v,\qquad v\odot(1-v)=\tfrac12.
```

The compatible operation in the $x$-coordinate is

```math
x_1\star_c x_2=\frac{x_1x_2}{c}.
```

Then $F(x_1\star_c x_2)=F(x_1)\odot F(x_2)$ and $I_c(x)=c^2/x$ is the group inverse.

The group isomorphism depends on the fixed parameters $r,c$ through $F$. It has nothing to do, by itself, with convolutions or the law of products of **independent** random variables.
