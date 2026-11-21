# 4.1 — Extrema and the exact inflection-point classification

The exact derivative formulas are
$$
f_x=-\frac{S(1+rW)}{2x^2},\qquad
f_{xx}=\frac{S}{2x^3}Q_r(W),\qquad
Q_r(w)=2r^2w^2+3rw+2-r^2.
$$

**Maximum [E].** For $0<r\le1$, $1+rW>0$ for every finite $x>0$, so $f$ strictly decreases. For $r>1$, its unique interior critical point is a strict maximum:
$$
\boxed{x_{\max}=c\left(\frac{r-1}{r+1}\right)^{1/(2r)},\qquad
f(x_{\max})=\frac{r+1}{2rc}
\left(\frac{r-1}{r+1}\right)^{(r-1)/(2r)}.}
$$
It lies left of $c$. At $r=1$, the supremum $1/c$ occurs only at the excluded boundary $x\to0^+$.

**Exact inflection polynomial [E].** Put $z=(x/c)^{2r}>0$, so $W=(z-1)/(z+1)$. The equation $f_{xx}=0$ is
$$
\boxed{(r+1)(r+2)z^2+(4-6r^2)z+(r-1)(r-2)=0.}\tag{4.1}
$$
Its discriminant is $\Delta_z=4r^2(8r^2-7)$. Alternatively the phase roots are
$$
\boxed{W_\pm=\frac{-3\pm\sqrt{8r^2-7}}{4r},\qquad
x_\pm=c\left(\frac{1+W_\pm}{1-W_\pm}\right)^{1/(2r)}}
$$
whenever $-1<W_\pm<1$.

**Number of genuine inflection points (sign changes of $f_{xx}$):**

| Range of $r$ | Inflection points on $(0,\infty)$ |
|---|---:|
| $0<r<\sqrt{7/8}$ | 0 |
| $r=\sqrt{7/8}$ | 0 (one double zero, no sign change) |
| $\sqrt{7/8}<r<1$ | 2 |
| $1\le r\le2$ | 1 |
| $r>2$ | 2 |

At $r=1$ or $2$ one algebraic root is $W=-1$, which is the excluded boundary $x=0$, leaving just one finite inflection. At $r=\sqrt{7/8}$, $Q_r$ is a square times a positive constant and stays nonnegative. The older polynomial $(r+1)(2r+1)z^2-4r(r-1)z+(r-1)(2r-1)$ is not the expansion of the displayed $f_{xx}$ and must not be used.