# 1.5 — Circle and differential half-density relations

The elementary identity $\mathrm{sech}^2z+\tanh^2z=1$, with $S=2xf$, gives

```math
4x^2f(x;r,c)^2+W(x;r,c)^2=1.\tag{1.5a}
```

Differentiate $W=\tanh(ru)$ and use $du/dx=1/x$:

```math
\frac{dW}{dx}=\frac r x S^2=4rxf(x;r,c)^2.\tag{1.5b}
```

Both formulas are **exact** for $x,c,r>0$. They are sometimes called “half-density” relations in this project; this terminology must not be confused with the transformation law of an abstract differential half-density.

A useful differential identity follows:

```math
\frac{d}{du}\left(\frac{1+W}{2}\right) =\frac r2S^2=2rP(1-P).
```

Integrating (1.5b) in $x$ yields

```math
\int_a^b x f(x)^2\,dx=\frac{W(b)-W(a)}{4r},\qquad 0<a<b.
```

At the endpoints $W(0^+)=-1$, $W(\infty)=1$, hence

```math
\int_0^\infty xf(x)^2\,dx=\frac1{2r}.
```

For $f_\mu=f/\sqrt\mu$ the weighted norm is $1/(2r\mu)$.

**Correction.** The older displayed expression involving $(4rx/c^2)f(c^2/x)^2$ is not equal to $W_x$ in general; (1.5b) is the correct formula. Inversion of a measure is handled separately in Chapter 2.

## A second derivation by differentiating the circle constraint

The two “half-density” formulas can be checked independently using the route developed in the earlier notes.

**Step 1.** Differentiate the circle identity in the spatial variable:

```math
-2WW_x=\frac{d}{dx}(4x^2f^2)=8xf^2+8x^2ff_x.
```

**Step 2.** Insert the exact phase derivative $W_x=4rxf^2$:

```math
-8rxWf^2=8xf^2+8x^2ff_x.
```

**Step 3.** Divide by $8xf$, which is strictly positive on the domain:

```math
xf_x+f=-rWf.
```

The equality is the Euler–Cauchy relation of Chapter 3. This is a *consistency derivation*, not an equivalence without hypotheses: the positivity of $f$, the specified $W_x$, and the circle constraint were essential for the division and the conclusion.

As an additional exact integral consequence, integrating $S_u=-rSW$ gives, for $0<a<b$,

```math
\int_a^b f(x)W(x)\,dx=\frac{S(\log(a/c))-S(\log(b/c))}{2r}.
```

For the special endpoint pair $(a,b)=(0,\infty)$, the integral vanishes because $S$ tends to zero at both ends. Thus $W$ is an odd observable for the even logarithmic pushforward density.
