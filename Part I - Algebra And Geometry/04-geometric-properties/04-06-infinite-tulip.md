# 4.6 — Solid of revolution: exact volume and surface-area thresholds

Regard $(x,f(x;r,c))$ as a **numerical Euclidean graph in fixed units**, with $f>0$, and revolve it around the $x$-axis. The resulting horn extends to infinity along $x$.

**Volume [E].** Using disks,
$$
V=\pi\int_0^\infty f(x)^2\,dx.
$$
The Beta identity from Chapter 1 gives, for $r>1/2$,
$$
\boxed{V=\frac{\pi^2}{4r^2c\sin(\pi/(2r))}}.
$$
If $0<r\le1/2$, $f^2\sim c^{-2r}x^{2r-2}$ at the origin is nonintegrable and $V=\infty$.

**Surface area [E].** Its lateral area is
$$
A=2\pi\int_0^\infty f(x)\sqrt{1+f_x(x)^2}\,dx.
$$
At infinity, $f=O(x^{-r-1})$ and $f_x=o(1)$, so the tail converges for **all** $r>0$. At zero the cases differ:

- $0<r<1$: $f\sim c^{-r}x^{r-1}$ and $|f_x|\sim(1-r)c^{-r}x^{r-2}$; therefore $f\sqrt{1+f_x^2}\sim(1-r)c^{-2r}x^{2r-3}$, which is nonintegrable.
- $r=1$: $f(x)=c/(c^2+x^2)$ is bounded at zero and $f_x=O(x)$, so the integrand is bounded and integrable there.
- $1<r<2$: $f|f_x|\asymp x^{2r-3}$, which is integrable because $r>1$; the $f$ contribution is also integrable.
- $r\ge2$: $f$ is integrable and $f_x$ is bounded near zero.

Consequently the **correct threshold is**
$$
\boxed{A<\infty\ \Longleftrightarrow\ r\ge1,}
$$
**not** the older $r>1$ claim. The exceptional $r=1$ case is essential because the leading factor $r-1$ in $f_x$ vanishes. Claims about actual volumes and areas in physical units require a separately specified vertical scale; Chapter 4.2 provides a dimensionally coherent alternative.