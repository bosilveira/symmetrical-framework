# 3.3 — The first-order circle constraint (NOT the second-order Master)

For the distinguished kernel, the Euler identity $xf_x+f=-rWf$ and circle identity $W^2=1-4x^2f^2$ imply
$$
\boxed{\Phi[f]:=x^2f_x^2+2xff_x+(1-r^2)f^2
+4r^2x^2f^4=0.}\tag{E1}
$$
Equivalently $(xf_x+f)^2=r^2f^2(1-4x^2f^2)$.

**Coupling convention.** For $f_\mu=f/\sqrt\mu$ with $\mu>0$, the exact constraint becomes
$$
\boxed{(xf_{\mu,x}+f_\mu)^2
=r^2f_\mu^2\bigl(1-4\mu x^2f_\mu^2\bigr).}\tag{E1-}\mu
$$
Let $y=2xf_\mu$ and $u=\log(x/c)$. Then $y_u=2x(xf_{\mu,x}+f_\mu)$, and (E1-$\mu$) is precisely
$$
y_u^2-r^2y^2+\mu r^2y^4=0.
$$
It is the **zero-energy first integral** of the separate second-order equation in §3.5.

**A necessary logical caution.** Squaring eliminates the sign of the Euler relation. As a counterexample, the smooth function
$$
f_s(x)=\frac{1}{2\sqrt\mu\,x}
$$
satisfies (E1-$\mu$) everywhere but **does not** satisfy the second-order Master: its $y=1/\sqrt\mu$ is constant and $r^2y-2\mu r^2y^3=-r^2/\sqrt\mu\ne0$. Hence (E1) alone cannot be used as a definition of the second-order dynamics. Piecewise $C^1$ plateau solutions create further nonuniqueness unless suitable regularity and the full equation are imposed.

In the original draft both equations were called “Master ODE”; we reserve **Master** for the second-order equation and call this one the **first-order constraint**.