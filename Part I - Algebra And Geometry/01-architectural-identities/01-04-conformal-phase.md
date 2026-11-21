# 1.4 — The hyperbolic phase and logistic coordinate

**[E]** Define

```math
W(x;r,c)=\tanh\!\left(r\log\frac{x}{c}\right) =\frac{x^{2r}-c^{2r}}{x^{2r}+c^{2r}}.
```

It is strictly increasing from $-1$ to $1$, with $W(c)=0$ and $W(c^2/x)=-W(x)$. Its derivatives are

```math
W_u=r(1-W^2)=rS^2,\qquad W_x=\frac r x(1-W^2)=4rx f(x)^2.
```

The second identity follows from $S=2xf$, not from a separate dynamical assumption.

Set $P=(1+W)/2$. Then

```math
P=\frac{(x/c)^{2r}}{1+(x/c)^{2r}},\quad P_u=2rP(1-P),\quad S^2=4P(1-P).
```

This is the standard logistic equation, with initial condition $P(0)=1/2$. The inverse chart is

```math
u=\frac{1}{2r}\log\frac{P}{1-P}.
```

The name “phase” is descriptive: $W$ is real-valued, not a complex $U(1)$ phase. A circle-valued angle can be introduced by $\sin\phi=W$, $\cos\phi=S$, with $\phi=\operatorname{gd}(ru)\in(-\pi/2,\pi/2)$.

**A projective interpretation [K/E].** The ratio of solutions of $J_{uu}=r^2J$ determines a Möbius coordinate; $W$ is a fractional-linear expression in $e^{2ru}$. The full projective meaning is elaborated in Chapter 3.
