# 3.1 — Derivative hierarchy and the Euler operator

Fix $x,c,r>0$, $u=\log(x/c)$, $S=\operatorname{sech}(ru)$, $W=\tanh(ru)$ and $f=S/(2x)$. Write $D=x\,d/dx=d/du$ when $c$ is fixed.

**First and second derivatives [E].**
$$
\begin{aligned}
S_u&=-rSW,& S_{uu}&=r^2S(2W^2-1),\\
W_u&=rS^2,& W_{uu}&=-2r^2S^2W,\\
f_x&=-\frac{S(1+rW)}{2x^2},&
f_{xx}&=\frac{S}{2x^3}\bigl(2-r^2+3rW+2r^2W^2\bigr).
\end{aligned}
$$
All identities follow from $S^2+W^2=1$, the chain rule $d/dx=x^{-1}d/du$, and the product rule. In particular,
$$
D f=-(1+rW)f,\qquad
D^2f=(1-r^2+2rW+2r^2W^2)f.
$$

**Higher ordinary derivatives [E].** Since $D=x\partial_x$,
$$
x^n\frac{d^nf}{dx^n}=D(D-1)\cdots(D-n+1)f.
$$
This falling-factorial identity is proved by induction from $x^n\partial_x^n=D^{\underline n}$ and the commutator $[D,\partial_x]=-\partial_x$.

**Two second-order identities.** Direct differentiation gives
$$
S_{uu}=r^2S-2r^2S^3,\qquad
W_{uu}=-2r^2W+2r^2W^3.
$$
These are equations satisfied by this pair of particular functions. A second-order equation, by itself, has a larger solution space than this selected profile.