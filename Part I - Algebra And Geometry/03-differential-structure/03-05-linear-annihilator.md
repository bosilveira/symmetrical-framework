# 3.5 — The second-order cubic Master equation

**Terminology correction.** The original file called the following a “linear annihilator”; that is misleading because its operator contains $f^3$. It is a **second-order nonlinear Cauchy–Euler ODE**.

For $f_\mu=f/\sqrt\mu$ ($\mu>0$ on the distinguished orbit),
$$
\boxed{x^2 f_{\mu,xx}+3x f_{\mu,x}+(1-r^2)f_\mu
+8\mu r^2x^2f_\mu^3=0.}\tag{M}
$$
To derive (M), set $y(u)=2xf_\mu(x)$, $u=\log(x/c)$. Direct differentiation gives the exact operator identity
$$
2x\left[x^2 f_{\mu,xx}+3x f_{\mu,x}
+(1-r^2)f_\mu+8\mu r^2x^2f_\mu^3\right]
=y_{uu}-r^2y+2\mu r^2y^3.
$$
Thus **(M)** is equivalent to
$$
\boxed{y_{uu}=r^2y-2\mu r^2y^3.}\tag{S}
$$

**First integral [E].** Multiplying (S) by $2y_u$ proves conservation of
$$
\boxed{\varepsilon=y_u^2-r^2y^2+\mu r^2y^4.}
$$
The mechanical Hamiltonian is $H=\varepsilon/2$. The equation admits equilibria $y=0,\;\pm1/\sqrt{2\mu}$ and nonconstant elliptic periodic orbits in addition to the localized $\operatorname{sech}$ orbit. It is not uniquely specified by a single solution.

**Finite weighted-norm theorem (real solutions) [E].** If $r,\mu>0$ and $f_\mu\in C^2(0,\infty)$ solves (M) globally with $\int_0^\infty x f_\mu^2\,dx<\infty$, then either $f_\mu=0$, or
$$
f_\mu(x)=\pm\frac{\operatorname{sech}(r\log(x/x_0))}
{2\sqrt\mu\,x},\qquad x_0>0.
$$
Its norm is $1/(2r\mu)$. Proof: the norm is $\tfrac14\int_\mathbb R y^2du$; conservation and boundedness imply $y\to0$ at both ends, forcing $\varepsilon=0$. A nonzero solution has fixed sign and an interior extremum $|y|=1/\sqrt\mu$, and uniqueness of (S) gives the $\operatorname{sech}$ orbit. The full detailed proof, including other real parameter signs, belongs to the foundational classification manuscript.

**A genuinely linear annihilator** instead acts on the reciprocal $J_\mu=1/y$ at $\varepsilon=0$: $J_{\mu,uu}-r^2J_\mu=0$.