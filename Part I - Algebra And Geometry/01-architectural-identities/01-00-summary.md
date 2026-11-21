# Chapter 1. Summary and conventions

**[E]** The starting object is
$$
f(x;r,c)=\frac{c^rx^{r-1}}{c^{2r}+x^{2r}}
       =\frac{1}{2x}\operatorname{sech}\!\left(r\log\frac{x}{c}\right),
\qquad x,r,c>0.
$$
This is real-analytic and positive on $x>0$; $r$ controls the logarithmic width, and $c$ is a positive scale (the inversion fixed point, **not** generally the maximum of $f$).

Put $u=\log(x/c)$, $T=e^{ru}$, $S=\operatorname{sech}(ru)$, $W=\tanh(ru)$. Then
$$
S=\frac{2T}{1+T^2},\quad W=\frac{T^2-1}{T^2+1},\quad
S^2+W^2=1,\quad S_u=-rSW,\quad W_u=rS^2.
$$
The pullback $g(u)=f(ce^u)=S/(2ce^u)$ is **not** even. The measure transforms as $f(x)\,dx=\tfrac12S\,du$; after normalization the logarithmic probability density is $p(u)=rS/\pi$, which **is** even. These different objects must never be identified.

The scale-free form is $f(x;r,c)=c^{-1}k(x/c;r)$, $k(z;r)=z^{r-1}/(1+z^{2r})$. The mass is $\pi/(2r)$ and the normalized CDF is $F(x)=2\arctan((x/c)^r)/\pi$.

The smooth positive solution is an exact *example* of later nonlinear ODEs, not a unique solution of a bare inversion identity. In particular, inversion symmetry alone does **not** characterize this function: $x^{-1}h(\log(x/c))$ has the same inversion law for any positive even $h$.