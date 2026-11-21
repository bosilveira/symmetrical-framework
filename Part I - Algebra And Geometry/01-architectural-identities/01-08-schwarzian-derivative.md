# 1.8 — Schwarzian derivative and projective connection

For a locally univalent $C^3$ function $h$ define
$$
\{h,x\}=\frac{h_{xxx}}{h_x}-\frac32\left(\frac{h_{xx}}{h_x}\right)^2.
$$
The Schwarzian chain rule **[K]** is
$$
\{h\circ v,x\}=\{h,v\}(v_x)^2+\{v,x\}.
$$
Here $W(x)=\tanh(r\log(x/c))$, and
$$
\{\tanh v,v\}=-2,\qquad
v=r\log(x/c),\quad v_x=r/x,\quad \{v,x\}=\frac1{2x^2}.
$$
Consequently **[E]**
$$
\boxed{\{W,x\}=\frac{1-4r^2}{2x^2}},\qquad
\boxed{\{W,u\}=-2r^2}.
$$
The result does not involve $c$ because translating $\log x$ does not affect this projective differential invariant.

**Linear ODE correspondence [K].** If $w_1,w_2$ are independent local solutions of $\psi''+Q(x)\psi=0$, then $z=w_1/w_2$ satisfies $\{z,x\}=2Q(x)$ wherever $z'$ is nonzero. Thus the framework determines the local projective potential
$$
Q_r(x)=\frac{1-4r^2}{4x^2}.
$$
This is the Euler inverse-square projective potential, not by itself the Gaussian curvature of a surface. Conformal curvature requires a specified metric (Chapter 3).

For any fractional-linear map $M(z)=(az+b)/(cz+d)$, $ad-bc\ne0$, one has $\{M\circ W,x\}=\{W,x\}$. This Möbius invariance acts on the **value** of $W$, and should not be conflated with the separate inversion of the **coordinate** $x$.