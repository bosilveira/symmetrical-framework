# Chapter 1. Summary and conventions

**[E]** The starting object is

```math
f(x;r,c)=\frac{c^rx^{r-1}}{c^{2r}+x^{2r}} =\frac{1}{2x}\mathrm{sech}\!\left(r\log\frac{x}{c}\right), \qquad x,r,c>0.
```

This is real-analytic and positive on $x>0$; $r$ controls the logarithmic width, and $c$ is a positive scale (the inversion fixed point, **not** generally the maximum of $f$).

Put $u=\log(x/c)$, $T=e^{ru}$, $S=\mathrm{sech}(ru)$, $W=\tanh(ru)$. Then

```math
S=\frac{2T}{1+T^2},\quad W=\frac{T^2-1}{T^2+1},\quad S^2+W^2=1,\quad S_u=-rSW,\quad W_u=rS^2.
```

The pullback $g(u)=f(ce^u)=S/(2ce^u)$ is **not** even. The measure transforms as $f(x)\,dx=\tfrac12S\,du$; after normalization the logarithmic probability density is $p(u)=rS/\pi$, which **is** even. These different objects must never be identified.

The scale-free form is $f(x;r,c)=c^{-1}k(x/c;r)$, $k(z;r)=z^{r-1}/(1+z^{2r})$. The mass is $\pi/(2r)$ and the normalized CDF is $F(x)=2\arctan((x/c)^r)/\pi$.

The smooth positive solution is an exact *example* of later nonlinear ODEs, not a unique solution of a bare inversion identity. In particular, inversion symmetry alone does **not** characterize this function: $x^{-1}h(\log(x/c))$ has the same inversion law for any positive even $h$.

## Integrated source results: primitives, densities and linearization

Two valid antiderivatives of $f$ were established in the reviewed notes: $A(x)=r^{-1}\arctan((x/c)^r)$ and $B(x)=(2r)^{-1}\arctan(\sinh(ru))$. Both differentiate to $f$, but $A-B=\pi/(4r)$ for real $x>0$. The step-by-step proof and definite integral are in [§1.7](01-07-normalized-density.md) and [§1.10](01-10-logarithmic-pushforward.md).

The Jacobian relationship and the logarithmic derivative of the pushed density are

```math
g(u;r,c)=\frac{\pi}{2rc}e^{-u}p(u;r),\qquad p_u=-rpW,\qquad W=-\frac1r(\log p)_u.
```

The auxiliary reciprocal $J=1/(2xf)=\cosh(ru)$ satisfies a **linear** Cauchy–Euler equation; the normalized density $p$ satisfies its **own nonlinear cubic equation**:

```math
x^2J_{xx}+xJ_x-r^2J=0,\qquad p_{uu}=r^2p-2\pi^2p^3.
```

The constants, proof steps and limits of the correspondence are given in [§1.11](01-11-auxiliary-linearization.md). The exceptional projective Möbius value $r=1/2$ is derived in [§1.8](01-08-schwarzian-derivative.md). None of these identities redefines the general nonlinear Master equation of Chapter 3.
