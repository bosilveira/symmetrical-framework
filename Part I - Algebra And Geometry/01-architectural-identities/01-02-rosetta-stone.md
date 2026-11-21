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
u=\frac{\mathrm{arctanh}W}{r},\quad x=c\left(\frac{1+W}{1-W}\right)^{1/(2r)},\quad S=\sqrt{1-W^2}.
```

By contrast $x\mapsto S$ is two-to-one away from $x=c$; it forgets the sign of $u$.

This identity makes many later calculations elementary, but it is not an isomorphism of every geometric construction subsequently attached to $f$: measures, differential operators, and boundary conditions must be transformed separately.

## Step-by-step inversion derivation

The reciprocal power-law symmetry from the earlier notes becomes almost immediate in this chart.

**Step 1.** Let $I_c(x)=c^2/x$. Then $u(I_c(x))=\log((c^2/x)/c)=-u(x)$.

**Step 2.** Since $\mathrm{sech}$ is even, $S(u(I_c(x)))=S(-u)=S(u)$.

**Step 3.** Apply the Rosetta Stone identity at the transformed argument:

```math
2I_c(x)f(I_c(x);r,c)=S(-u)=S(u)=2xf(x;r,c).
```

**Step 4.** Substitute $I_c(x)=c^2/x$ and divide by $2c^2/x$:

```math
f(c^2/x;r,c)=\frac{x^2}{c^2}f(x;r,c).
```

This proof preserves the exact coordinate transformation and the weight factor; it does **not** assert that $f$ is an even function of $x$ or that inversion of $f(x)\,dx/x$ preserves its density. The oriented- and absolute-Jacobian statements are proved separately in [§2.2](../02-foundational-symmetries/02-02-moebius-symmetry.md).
