# 1.2 — The Rosetta Stone identity and its inverse charts

Fix $u=\log(x/c)$ and $T=e^{ru}=(x/c)^r>0$. The elementary equality

```math
\mathrm{sech}(ru)=\frac{2}{T+T^{-1}} =\frac{2c^rx^r}{c^{2r}+x^{2r}}
```

immediately proves **[E]**

```math
2xf(x;r,c)=S(u)=\mathrm{sech}(ru).
```

The companion chart is

```math
W(u)=\frac{T^2-1}{T^2+1}=\tanh(ru),\qquad S^2+W^2=1,\quad S>0,\;-1<W<1.
```

**Maps and information.** The coordinate map $(0,\infty)\to\mathbb R$, $x\mapsto u$, is a diffeomorphism once $c$ is fixed. The change $S=2xf$ also multiplies the dependent variable by a nonconstant factor; it is not simply $f(ce^u)=S(u)$. The map $x\mapsto W(x)$ is a bijection onto $(-1,1)$:

```math
u=\frac{\operatorname{arctanh}W}{r},\quad x=c\left(\frac{1+W}{1-W}\right)^{1/(2r)},\quad S=\sqrt{1-W^2}.
```

By contrast $x\mapsto S$ is two-to-one away from $x=c$; it forgets the sign of $u$.

This identity makes many later calculations elementary, but it is not an isomorphism of every geometric construction subsequently attached to $f$: measures, differential operators, and boundary conditions must be transformed separately.
