# Chapter 3 — Differential structure: typed equations and implications

**Revised mathematical exposition, 20 November 2026.** This chapter distinguishes a **specific solution**, a **coupled first-order system**, a **first-order energy-zero equation**, and a **second-order nonlinear ODE**. They are related but they are **not** interchangeable.

With $u=\log(x/c)$, $y=2xf$, $S=\operatorname{sech}(ru)$ and $W=\tanh(ru)$:
$$
S_u=-rSW,\qquad W_u=r(1-W^2),\qquad S^2+W^2=1.
$$
For coupling $\mu>0$, write $f_\mu=f/\sqrt\mu$ and $y_\mu=2xf_\mu$. The autonomous **Master equation** is
$$
y_{\mu,uu}=r^2y_\mu-2\mu r^2y_\mu^3,
$$
equivalently
$$
x^2f_\mu''+3xf_\mu'+(1-r^2)f_\mu+8\mu r^2x^2f_\mu^3=0.
$$
Its conserved energy is $\varepsilon=y_{\mu,u}^2-r^2y_\mu^2+\mu r^2y_\mu^4$. The **first-order constraint** is just the level $\varepsilon=0$, not the full second-order equation.

**Contents:** [derivatives](03-01-derivative-hierarchy.md), [Euler relation](03-02-euler-cauchy.md), [first-order constraint](03-03-master-nonlinear.md), [Riccati system](03-04-riccati-coupled.md), [second-order Master](03-05-linear-annihilator.md), [recurrences](03-06-euler-recurrence.md), [Liouville geometry](03-07-ernst-liouville.md), [logical dependencies and defects](03-08-differential-interrelation.md), [proof register](03-99-notes.md). Historical \`03-gemini.md\` is archival and unreviewed.