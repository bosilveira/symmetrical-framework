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

## Hyperbolic proof of the unique critical point

The phase is also a convenient coordinate for the extrema of the *original* function, not merely of the symmetric profile $S$.

**Step 1.** Write $f=S/(2x)$ and differentiate at fixed $c$:

```math
f_x=\frac{1}{2x}S_u\frac{du}{dx}-\frac{S}{2x^2}=-\frac{S}{2x^2}(1+rW).
```

**Step 2.** Since $S>0$ and $x>0$, the critical-point condition is $1+rW=0$. Thus

```math
W(x_{\max})=-\frac1r,\qquad u_{\max}=-\frac1r\mathrm{arctanh}\left(\frac1r\right).
```

**Step 3.** The range $-1<W<1$ permits this equation exactly when $r>1$. Inverting the $W$ chart gives

```math
x_{\max}=c\exp(u_{\max})=c\left(\frac{r-1}{r+1}\right)^{1/(2r)}.
```

The sign of $f_x$ changes from positive to negative across this point, proving it is a strict global maximum. The location is **not** $x=c$; the latter is instead the symmetry point and the median of the normalized distribution.

## Phase from the logarithmic density

The earlier notes also correctly identify a second characterization of $W$. With $p(u;r)=(r/\pi)\mathrm{sech}(ru)$,

```math
W(u;r)=-\frac1r\frac{d}{du}\log p(u;r),\qquad W_u=r\left[1-\left(\frac{\pi p}{r}\right)^2\right].
```

These are identities on the chosen solution. If one wishes to *reconstruct* the phase using a Riccati equation, the centering datum $W(0)=0$ must be supplied; otherwise the Riccati ODE has other solutions.
