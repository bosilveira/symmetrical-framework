# A one-dimensional classification of finite-norm solutions of a cubic Cauchy–Euler equation, and three identifications of its sech profile

*Foundational paper of the Symmetrical Framework series. Working draft v0.1.*

> **How to read the labels.**
> **[T]** a theorem or proposition proved in this paper.
> **[V]** an identity verified by a symbolic or numerical computation (Appendix A).
> **[K]** a known result from the literature (Appendix C records what was and was not checked).
> **[I]** an interpretation; no proof is claimed, and nothing labelled [I] is used in any proof.

---

## Abstract

For constants $r>0$ and $\mu>0$ we study the real equation, labelled **(M)**:

$$
x^2 f'' + 3x f' + (1-r^2)f + 8\mu r^2 x^2 f^3 = 0, \qquad x\in(0,\infty).
$$

We prove that every nonzero real $C^2$ solution on $(0,\infty)$ with $\int_0^\infty f^2x \mathrm{d}x<\infty$ has the form
$f(x)=\pm\mathrm{sech}(r\ln(x/x_0))/(2\sqrt{\mu} x)$ for exactly one pair $(x_0,\pm)$,
and that for every other sign of the parameters the zero function is the only such solution.
Since $x^2f''+3xf'$ is $\lvert z\rvert ^2$ times the radial Laplacian in $\mathbb R^4$, equation (M) is the radial form of a critical (Yamabe-type) equation with a Hardy potential; for $r=1$ the profile is the Aubin–Talenti bubble. The theorem is therefore an elementary one-dimensional proof of a known type of radial classification, written in the variable $u=\ln x$.
We then record three exact identifications of the profile (the Euler-top separatrix; the $SU(2)$-invariant instanton profile at $r=1$; the Friedmann equation for radiation, curvature and a cosmological constant in conformal time) and a few structural properties of (M) (variational structure, prolongation). Interpretive readings are kept separate and labelled.

---

## 1. Introduction

### 1.1 The result in plain language

Consider, for constants $r>0$ and $\mu>0$, the second-order equation (M) above. (Its linear part is a Cauchy–Euler operator, and the whole equation is unchanged under $x\mapsto\lambda x$, $f\mapsto f/\lambda$.)
It has a large family of solutions: some oscillate in $\ln x$, some blow up at a finite point, some level off.
We ask which of them have finite size, meaning $\int_0^\infty f(x)^2 x \mathrm{d}x<\infty$.

The answer is short. Apart from the zero function, a finite-size solution is one single bump, the reciprocal of a hyperbolic cosine in $\ln x$. It can be slid anywhere along the log-axis (this is the parameter $x_0$) and flipped in sign. Such a bump exists only when both parameters of the equation are positive; for any other signs the zero function is the only finite-size solution (Theorem 4.2).

### 1.2 Relation to known results

*(a) Radial form.* For $`F(z)=f(\lvert z\rvert )`$ on $`\mathbb R^4\setminus\lbrace 0\rbrace `$ one has $\lvert z\rvert ^2\Delta F = x^2f''+3xf'$ at $x=\lvert z\rvert $. Hence (M) is equivalent to the following equation, labelled **(1.1)**:

$$
\Delta F+\frac{1-r^2}{\lvert z\rvert ^2}F+8\mu r^2F^3=0 \quad \text{in } \mathbb R^4\setminus\lbrace 0\rbrace .
$$

Here $3=(n+2)/(n-2)$ is the critical Sobolev exponent for $n=4$; the number $1=(n-2)^2/4$ is the Hardy constant of $\mathbb R^4$; and $\lambda=1-r^2<1$ is a Hardy coupling below the Hardy threshold, which corresponds to $r=0$. **[V]**

*(b) The case $r=1$.* Then (1.1) is $\Delta F+8\mu F^3=0$, the critical Yamabe-type equation in $\mathbb R^4$, and the bump of Theorem 4.1 is $F(z)=x_0/(\sqrt\mu (x_0^2+\lvert z\rvert ^2))$, the Aubin–Talenti bubble [1, 2] (Proposition 5.2). **[V], [K]**

*(c) What is known.* The following is recalled from the literature; Appendix C records that the bibliographic data were confirmed but that the theorem statements were **not** re-read in the primary sources.

- Positive solutions of the critical equation $\Delta u+u^{(n+2)/(n-2)}=0$ on $\mathbb R^n$ are radially symmetric about some point and are bubbles; this is due to Gidas–Ni–Nirenberg under a decay hypothesis [3, 4], which was later removed by Caffarelli–Gidas–Spruck [5]. **[K]**
- Caffarelli–Gidas–Spruck [5] also describe positive solutions with an isolated singularity (asymptotic radial symmetry). The radial ones are periodic in $\ln\lvert z\rvert $ (called Fowler or Delaunay-type solutions in the literature). **[K]**
- Terracini [6] studies positive solutions of $-\Delta u=a(x/\lvert x\rvert ) u/\lvert x\rvert ^2+u^{(n+2)/(n-2)}$ on $\mathbb R^n\setminus\lbrace 0\rbrace $, which contains (1.1) (after rescaling $u=\sqrt{8\mu} r F$) as the case of constant $a=1-r^2$. **[K]** (Only the abstract was read.)
- Uniqueness of ground states of autonomous scalar-field equations is a classical subject [7, 8]. **[K]**

*(d) What this paper offers.* We do not claim that the classification is new. We give (i) an elementary proof in the variable $\ln x$ that needs no positivity assumption and covers every real pair of parameters; (ii) an explicit dictionary between (M), its first-order level, a linear equation $J''=r^2J$, and the three structures of §5; (iii) a short list of verified structural properties of (M). Whether any of these identities is new is a question for the literature check in Appendix C.

*(e) The hypothesis.* The finite-norm hypothesis is $N(f)=\int_0^\infty f^2x \mathrm{d}x=(2\pi^2)^{-1}\int_{\mathbb R^4}F^2\lvert z\rvert ^{-2}\mathrm{d}z<\infty$, a Hardy-weighted $L^2$ norm. The bump also has finite Dirichlet energy (for $r=1.3$, $\mu=0.72$, $x_0=1$: $\int f'^2x^3\mathrm{d}x=0.8351\ldots$), but finiteness of the energy is not used. **[V]**

### 1.3 Scope

This paper

1. proves a classification theorem for (M) (§4);
2. records three exact identifications of its sech profile, each with the regime in which it holds (§5);
3. lists a few structural properties of (M) that do not depend on any identification (§6).

It does **not** claim that (M) is canonical (a forced equation), and it makes no statement about complex-valued solutions or about real solutions with a pole. Questions raised by the identifications are left to the companion essays (§8).

---

## 2. Conventions

The following six conventions are fixed once and repeated in every statement.

| # | Item | Convention in this paper |
|---|------|---------------------------|
| 1 | Equation | **(M)** is the second-order equation; **(E1)** (§3.3) is its first-order level. Always say which is meant. |
| 2 | Regularity | $C^2$ on the open interval. ($C^1$ is not enough for uniqueness of (E1); see Proposition 4.4.) |
| 3 | Domain and reality | Real-valued, defined on all of $(0,\infty)$. Complex-valued solutions and solutions with a real pole are not considered. |
| 4 | Norm | $N(f)=\int_0^\infty f(x)^2x \mathrm{d}x$ (the square of the weighted $L^2$ norm). The weighted $L^2$ norm is $\lVert f\rVert =N(f)^{1/2}$. |
| 5 | Counting | Statements are about nonzero solutions. The family is parametrized by $(x_0,\pm)$, and the map $(x_0,\pm)\mapsto f$ is one-to-one. |
| 6 | Parameters | $r>0$, $\mu>0$ is the same as $s=r^2>0$, $\kappa=\mu r^2>0$. Other real pairs $(s,\kappa)$ are treated in Theorem 4.2. |

Notation: $u=\ln x$, $y(u)=2xf(x)$, $s=r^2$, $\kappa=\mu r^2$. A prime on $f$ means $\mathrm{d}/\mathrm{d}x$; a prime on $y$ means $\mathrm{d}/\mathrm{d}u$. Appendix B lists the notation clashes avoided here.

---

## 3. Equivalent forms of the Master equation

Write $\mathrm{SO}[f]=x^2f''+3xf'+(1-r^2)f+8\mu r^2x^2f^3$, so that (M) is $\mathrm{SO}[f]=0$.

### 3.1 Scale invariance

**Proposition 3.1 [V].** If $f$ solves (M) and $\lambda>0$, then $f_\lambda(x)=\lambda^{-1}f(x/\lambda)$ solves (M), and $N(f_\lambda)=N(f)$. Moreover, for $a\in\mathbb R$ the integral $\int f^2x^a \mathrm{d}x$ is invariant under $f\mapsto f_\lambda$ if and only if $a=1$.

(In words: the weight $x$ in the norm is the unique power that respects the symmetry of the equation.)

### 3.2 Logarithmic form

**Proposition 3.2 [V].** Put $u=\ln x$ and $y(u)=2e^uf(e^u)$. Then

$$
\mathrm{SO}[f]=\frac1{2x}(y''-r^2y+2\mu r^2y^3),
$$

so $f$ solves (M) if and only if $y$ solves the following equation, labelled **(S)**:

$$
y''=sy-2\kappa y^3, \qquad s=r^2, \quad \kappa=\mu r^2.
$$

Moreover $N(f)=\frac14\int_{\mathbb R}y^2 \mathrm{d}u$, and $f\in C^2(0,\infty)$ if and only if $y\in C^2(\mathbb R)$.

(Equation (S) is an undamped, unforced Duffing oscillator; for $s,\kappa>0$ its potential is a double well.)

### 3.3 First integral and the first-order equation

**Proposition 3.3 [V].** On solutions of (S), $\varepsilon=y'^2-sy^2+\kappa y^4$ is constant. In terms of $f$,

$$
\varepsilon=4x^2 \Phi[f],\qquad
\Phi[f]=x^2f'^2+2xff'+(1-r^2)f^2+4\mu r^2x^2f^4 .
$$

The **first-order equation**, labelled **(E1)**, is $\Phi[f]=0$, that is, $\varepsilon=0$.

Solved for $f'$ it reads $xf'/f=-1\pm r\sqrt{1-4\mu x^2f^2}$, so real solutions need $4\mu x^2f^2\le1$. With $S=2\sqrt\mu xf$ and $W=-(1+xf'/f)/r$, equation (E1) is exactly

$$
W^2+S^2=1 .
$$

### 3.4 Radial form in $\mathbb R^4$

**Proposition 3.4 [V].** For $F(z)=f(\lvert z\rvert )$ on $\mathbb R^4\setminus\lbrace 0\rbrace $: $\lvert z\rvert ^2\Delta F=x^2f''+3xf'$ at $x=\lvert z\rvert $, so (M) is equivalent to (1.1), and $N(f)=(2\pi^2)^{-1}\int_{\mathbb R^4}F^2\lvert z\rvert ^{-2}\mathrm{d}z$.

### 3.5 The linear backbone

**Proposition 3.5 [T].** Let $f$ be a positive $C^2$ solution of (M) with $\varepsilon=0$, and put $y=2xf$, $J=1/y$. Then $J''=r^2J$ and $J'^2-r^2J^2=-\mu r^2$. Hence $J(u)=Ae^{ru}+Be^{-ru}$ with $A,B>0$, $4AB=\mu$, and

$$
f(x)=\frac{1}{2x J(\ln x)}=\frac{x^{r-1}}{2 (Ax^{2r}+B)} .
$$

*Proof.* From $y'^2=r^2y^2-\mu r^2y^4$ and $J'=-y'/y^2$ one gets $J'^2=r^2J^2-\mu r^2$. Differentiating, $2J'(J''-r^2J)=0$. The set $\lbrace J'=0\rbrace $ has empty interior: on an interval where $J'=0$ one has $y\equiv\mu^{-1/2}$, which does not satisfy (S) because $y''=0\ne r^2y(1-2\mu y^2)=-r^2y$. So $J''=r^2J$ on a dense set, hence everywhere by continuity. Thus $J=Ae^{ru}+Be^{-ru}$, and $J'^2-r^2J^2=-4r^2AB=-\mu r^2$ gives $4AB=\mu>0$; positivity of $J$ forces $A,B>0$. $\square$

With $x_0=(B/A)^{1/(2r)}$ one has $J(\ln x)=\sqrt\mu \cosh(r\ln(x/x_0))$, which is the sech form of the Theorem below.

---

## 4. The classification theorem

**Theorem 4.1 (Classification of finite-norm solutions).** Let $r>0$ and $\mu>0$, and consider the second-order Cauchy–Euler equation with a cubic nonlinearity

$$
x^2f''+3xf'+(1-r^2)f+8\mu r^2x^2f^3=0,\qquad x\in(0,\infty).
$$

Let $f$ be a nonzero, real-valued $C^2$ solution on all of $(0,\infty)$ with finite weighted $L^2$ norm, that is,

$$
\int_0^\infty f(x)^2 x \mathrm{d}x<\infty .
$$

Then

$$
f(x)=\pm \frac{\mathrm{sech}(r\ln(x/x_0))}{2\sqrt{\mu} x}
$$

for exactly one pair $(x_0,\pm)$ with $x_0>0$. Conversely, every such function is a solution with finite weighted $L^2$ norm, and $\int_0^\infty f(x)^2 x \mathrm{d}x=1/(2r\mu)$.

(In words: apart from the zero function, the only finite-size solutions are one bump shape, placed anywhere along the log-axis and possibly flipped. The parameter $x_0$ marks where $xf$ peaks, and $xf$ is symmetric under $x\mapsto x_0^2/x$.)

**Theorem 4.2 (all real parameters).** Let $s,\kappa\in\mathbb R$ and let $y\in C^2(\mathbb R)$ be a real solution of $y''=sy-2\kappa y^3$ with $\int_{\mathbb R}y^2\mathrm{d}u<\infty$. Then either $y\equiv0$, or $s>0$, $\kappa>0$ and

$$
y(u)=\pm\sqrt{s/\kappa} \mathrm{sech}(\sqrt s (u-u_0))\quad\text{for exactly one pair }(u_0,\pm).
$$

*Theorem 4.1 follows from Theorem 4.2*, with $s=r^2$ and $\kappa=\mu r^2$, by Proposition 3.2: $\sqrt{s/\kappa}=\mu^{-1/2}$, $f=y/(2x)$, $x_0=e^{u_0}$. For the converse, the function $\mu^{-1/2}\mathrm{sech}(r(u-u_0))$ solves (S) (Appendix A) and $\int y^2\mathrm{d}u=2/(r\mu)$, so $N(f)=\frac14\cdot2/(r\mu)=1/(2r\mu)$. The pair is unique because $\lvert y\rvert $ attains its maximum $\sqrt{s/\kappa}$ at $u_0$ only, and the sign of $y$ is the sign of $\pm$.

### Proof of Theorem 4.2

Let $y$ be as in the statement, $y$ is not identically zero. *Global* means $y$ is defined on all of $\mathbb R$; this is used in Steps 3 and 4.

**Step 1 (first integral).** $\varepsilon=y'^2-sy^2+\kappa y^4$ is constant (Proposition 3.3).

**Step 2 ($\kappa=0$).** Then $y''=sy$. For $s>0$, $y=Ae^{\sqrt su}+Be^{-\sqrt su}$ is square-integrable only if $A=B=0$; for $s=0$, $y$ is affine; for $s<0$, $y$ is sinusoidal. In each case $y\in L^2$ forces $y\equiv0$.

**Step 3 ($\kappa<0$, $s\ge0$).** Here $(y^2)''=2y'^2+2sy^2+4\lvert \kappa\rvert y^4\ge0$, so $y^2$ is convex, nonnegative and integrable. A nonnegative convex function $g$ on $\mathbb R$ with $\int g<\infty$ vanishes identically: if $g(u_2)>0$, then either $g'(u_2)\ge0$, so $g\ge g(u_2)$ on $[u_2,\infty)$, or $g'(u_2)<0$, so $g\ge g(u_2)$ on $(-\infty,u_2]$, and in both cases $\int g=\infty$. Hence $y\equiv0$.

**Step 4 ($\kappa<0$, $s<0$).** Put $\sigma=-s>0$, $\varrho=-\kappa>0$, $U(y)=\frac12\sigma y^2-\frac12\varrho y^4$. Then $y''=-U'(y)$, and $E=\frac12y'^2+U(y)=\varepsilon/2$ is constant. $U$ has a strict minimum $U(0)=0$, strict maxima $U(\pm y_h)=M:=\sigma^2/(8\varrho)$ at $y_h^2=\sigma/(2\varrho)$, and $U\to-\infty$ as $\lvert y\rvert \to\infty$.

- *$E>M$.* Then $y'\ne0$ everywhere, so $y$ is strictly monotone and $\lvert y\rvert \to\infty$ in at least one direction. Since $E-U(y)\ge\varrho y^4/4$ for large $\lvert y\rvert $, the integral $\int^\infty \mathrm{d}y/\lvert y'\rvert $ converges: $y$ reaches infinity at a finite $u$, which contradicts globality.
- *$E<M$.* The orbit lies in one component of $\lbrace U\le E\rbrace $. A component not containing $0$ is unbounded, and the same estimate shows blow-up in finite $u$, again impossible. The component containing $0$ is bounded; the orbit is the equilibrium $y\equiv0$ (then $E=0$) or a nonconstant periodic orbit, for which $\int y^2=\infty$.
- *$E=M$.* Then $\frac12y'^2=\frac12\varrho(y^2-y_h^2)^2$. Bounded solutions are the constants $\pm y_h$ or the heteroclinic orbits $y=\pm y_h\tanh(\sqrt\varrho y_h(u-u_0))$; unbounded ones blow up. In all bounded cases $\lvert y\rvert \to y_h\neq0$ at some end, so $y\notin L^2$.

Hence $y\equiv0$.

**Step 5 ($\kappa>0$: boundedness).** From Step 1, $\kappa y^4-sy^2=\varepsilon-y'^2\le\varepsilon$, which bounds $\lvert y\rvert $; then $y'^2=\varepsilon+sy^2-\kappa y^4$ bounds $\lvert y'\rvert $. So $(y^2)'=2yy'$ is bounded by some $L$.

**Step 6 ($\kappa>0$: decay and $\varepsilon=0$).** Suppose $y(u)$ does not tend to $0$ as $u\to+\infty$. Then there are $\delta>0$ and $u_n\to\infty$ with $y(u_n)^2\ge\delta$ and $u_{n+1}>u_n+1$; since $y^2$ is $L$-Lipschitz, $y^2\ge\delta/2$ on $[u_n,u_n+\delta/(2L)]$, so $\int y^2=\infty$, a contradiction. The same argument applies at $-\infty$. Thus $y\to0$ at both ends. Then $y'^2=\varepsilon+sy^2-\kappa y^4\to\varepsilon$, so $\varepsilon\ge0$. If $\varepsilon>0$, then $\lvert y'\rvert \to\sqrt\varepsilon>0$; thus $y'$ has a fixed sign and $\lvert y'\rvert \ge\sqrt\varepsilon/2$ for large $u$, so $\lvert y\rvert \to\infty$, contradicting $y\to0$. Hence $\varepsilon=0$.

**Step 7 ($\kappa>0$: identification).** Now $y'^2=y^2(s-\kappa y^2)$. If $y(u_1)=0$ at some point, then $y'(u_1)^2=\varepsilon=0$ and uniqueness for (S) gives $y\equiv0$. So $y$ never vanishes and has a constant sign; replacing $y$ by $-y$ (equation (S) is odd) assume $y>0$. Since $y\to0$ at both ends, $y$ attains a maximum at some $u_0$, where $y'(u_0)=0$, so $s=\kappa y(u_0)^2>0$ and $y(u_0)=\sqrt{s/\kappa}$. The function $\hat y(u)=\sqrt{s/\kappa}\mathrm{sech}(\sqrt s(u-u_0))$ solves (S) with the same data $(y,y')$ at $u_0$ (Appendix A), and solutions of (S) are unique for given data. Hence $y=\hat y$. $\square$

### Remarks

**Remark 4.3 (variants).** (i) *Other norms.* Since $\int\lvert f\rvert ^px^{p-1}\mathrm{d}x=2^{-p}\int\lvert y\rvert ^pdu$, the condition $\int\lvert f\rvert \mathrm{d}x<\infty$ is the case $p=1$, and $\int f^2x \mathrm{d}x<\infty$ is $p=2$. The same proof gives the same classification for any $p\in(0,\infty)$ (for $\kappa>0$, $y$ is bounded, so $p<2$ reduces to $p=2$; for $\kappa<0$, $s\ge0$, $y^2$ is a convex function in $L^{p/2}$); the details are omitted here. (ii) *No positivity is assumed.* Sign-changing finite-norm solutions are excluded by Step 7. (iii) *Globality is essential:* the solutions with a real pole (for example $\mathrm{csch}$, which solves (S) with $\kappa<0$) are excluded by it.

**Proposition 4.4 (the first-order equation).** Let $r,\mu>0$.

1. The function $f_s(x)=1/(2\sqrt\mu x)$ is smooth and positive and satisfies (E1). It does **not** satisfy (M): $\mathrm{SO}[f_s]=r^2/(2\sqrt\mu x)\ne0$. It has $N(f_s)=\infty$. It is the envelope of the bump family (the bump touches it at $x=x_0$). **[V]**
   (It must not be confused with the equilibrium solutions: the constants $y=\pm1/\sqrt{2\mu}$ of (S), the bottoms of its double well, correspond to $f_\pm=\pm1/(2\sqrt{2\mu} x)$. These **do** solve (M) and have $N=\infty$; $f_s$ has $y=1/\sqrt\mu$. At $r=1$, $f_+$ is the explicit singular solution of $\Delta F+8\mu F^3=0$ on $\mathbb R^4\setminus\lbrace 0\rbrace $. **[V]**)
2. For $0<x_a<x_b$ let $f$ equal $\mathrm{sech}(r\ln(x/x_a))/(2\sqrt\mu x)$ for $x\le x_a$, equal $f_s$ on $[x_a,x_b]$, and equal $\mathrm{sech}(r\ln(x/x_b))/(2\sqrt\mu x)$ for $x\ge x_b$. Then $f$ is positive, $C^1$, satisfies (E1) everywhere, and has finite $N$, but $f''$ jumps at $x_a$ (and at $x_b$). **[V]** So (E1) alone has a two-parameter family of finite-norm $C^1$ solutions.
3. **[T]** If $f$ is a $C^2$ solution that is not identically zero of (E1) on $(0,\infty)$ with $N(f)<\infty$, then $f$ solves (M), and hence is a bump of Theorem 4.1.

*Proof of 3.* With $y=2xf$, (E1) says $y'^2=y^2(s-\kappa y^2)$. Differentiating, $y'(y''-sy+2\kappa y^3)=0$, so (S) holds wherever $y'\ne0$. On an interval where $y'=0$, $y$ is constant with $c^2(s-\kappa c^2)=0$, i.e. $c=0$ or $c^2=s/\kappa$; the plateau $c^2=s/\kappa$ is not a solution of (S) (there $y''=0\ne-sy$), and since $y''$ is continuous it cannot border a region where $y$ solves (S) (where $y''=-sc$ at the junction). Hence a plateau would have to be all of $\mathbb R$, which has infinite norm; and $y\equiv0$ on an interval forces $y\equiv0$ by Gronwall applied to $z=y^2$ ($\lvert z'\rvert \le Cz$). So $\lbrace y'=0\rbrace $ has empty interior, (S) holds on a dense set and hence everywhere, and Theorem 4.2 applies. $\square$

---

## 5. Three identifications of the sech profile

Throughout this section $f$ is the bump of Theorem 4.1, $\theta=r\ln(x/x_0)$, and $S=2\sqrt\mu xf=\mathrm{sech}\theta$, $W=-(1+xf'/f)/r=\tanh\theta$ **[V]**. Each identification uses only §3 and is independent of Theorem 4.1; the theorem explains why the zero level $\varepsilon=0$ is the finite-norm level.

### 5.1 The Euler-top separatrix

**Proposition 5.1 [V].** Put $(V,D,Y)=(\tanh\theta,\mathrm{sech}\theta,\mathrm{sech}\theta)=(W,S,S)$. With $'=\mathrm{d}/\mathrm{d}\theta$,

$$
V'=DY,\quad D'=-VY,\quad Y'=-VD,\qquad V^2+D^2=1,\quad V^2+Y^2=1,\quad D=Y .
$$

This is the member $k=1$ of Jacobi's family $(V,D,Y)=(k\mathrm{sn},\mathrm{dn},k\mathrm{cn})$ **[K]**. The first-order equation (E1) is exactly the circle $V^2+D^2=1$ (Proposition 3.3). The Nahm-type triple $(f_1,f_2,f_3)=(-\coth\theta,-\mathrm{csch}\theta,-\mathrm{csch}\theta)$ solves $f_1'=f_2f_3$ and its cyclic images, and is the image of $(V,D,Y)$ under $\theta\mapsto\theta+i\pi/2$ (up to the factors $-1,-i$).

*Regime.* This identifies the finite-norm solution of (M) with the *separatrix* $k=1$ of the top. For $k<1$ the corresponding solutions of (S) have $\varepsilon\ne0$ and are elliptic; that case is the subject of Essay I. The third component is not independent: it is fixed by $D^2-Y^2=k'^2$.

### 5.2 The instanton profile at $r=1$ and the Yamabe bubble

**Proposition 5.2.**

(a) **[V]** For $r=1$, $F(z)=x_0/(\sqrt\mu (x_0^2+\lvert z\rvert ^2))$ is the bump, and $\Delta F+8\mu F^3=0$ on $\mathbb R^4$. The metric $F^2\lvert \mathrm{d}z\rvert ^2$ has constant scalar curvature $48\mu$ (sectional curvature $4\mu$, radius $1/(2\sqrt\mu)$). For general $r$, the metric $f(\lvert z\rvert )^2\lvert \mathrm{d}z\rvert ^2$ on $\mathbb R^4\setminus\lbrace 0\rbrace $ has scalar curvature $6(1-r^2)/(\lvert z\rvert ^2f^2)+48\mu r^2$, which is not constant if $r\ne1$.

(b) **[V]** Put $\phi=(1+W)/2$. Then $\phi(1-\phi)=\mu x^2f^2$ and, with $'=\mathrm{d}/\mathrm{d}u$,

$$
\phi'=2r\phi(1-\phi),\qquad \phi''=4r^2\phi(1-\phi)(1-2\phi).
$$

For $r=1$, $\phi=x^2/(x^2+x_0^2)$.

(c) **[K]** For $r=1$, the equation $\phi''=4\phi(1-\phi)(1-2\phi)$ is the radial equation of the $SU(2)$-invariant ansatz for the self-dual Yang–Mills equations, and $\phi$ is the profile of the BPST instanton [9]. (The reduction is recalled, not re-derived here; the Chern–Simons change $[\phi^2(3-2\phi)]_0^1=1$ is the instanton number.)

(d) **[V]** In dimension two, on the bump $(\ln f)_{uu}=-r^2S^2=-4\mu r^2x^2f^2$ (with $u=\ln x$), i.e. $\Delta\ln f=-4\kappa f^2$ for $F(z)=f(\lvert z\rvert )$ on $\mathbb R^2\setminus\lbrace 0\rbrace $: the metric $f^2\lvert \mathrm{d}z\rvert ^2$ has constant curvature $4\mu r^2$ for every $r$, with cone angle $2\pi r$ at the origin.

*Regime.* The instanton reading is $r=1$. For $r\ne1$, (1.1) has a Hardy term and the scalar curvature in (a) is not constant.

### 5.3 The Friedmann equation in conformal time

**Proposition 5.3 [V].** Let $k,\Lambda\in\mathbb R$ and let $a(\eta)>0$ be a $C^2$ function. Then $a''=-k a+\frac{2\Lambda}{3}a^3$ if and only if $a$ solves (S) with $y=a$, $u=\eta$ and $(s,\kappa)=(-k,-\Lambda/3)$. For such $a$ the quantity $C=a'^2+k a^2-\frac\Lambda3a^4$ is constant (it is $\varepsilon$), so that, with $'=\mathrm{d}/\mathrm{d}\eta$, the following relation holds, labelled **(5.1)**:

$$
a'^2=C-k a^2+\frac{\Lambda}{3} a^4.
$$

and

$$
(s,\kappa,\varepsilon)=(-k, -\Lambda/3, C).
$$

(Relation (5.1) is the Friedmann constraint for a universe with radiation, spatial curvature $k$ and a cosmological constant $\Lambda$, written in conformal time $\eta$. In terms of $f$: $a(\eta)=2e^\eta f(e^\eta)$.) For $s,\kappa>0$ and $C=0$, that is $k<0$, $\Lambda<0$, the bump is

$$
a(\eta)=\sqrt{s/\kappa} \mathrm{sech}(\sqrt s \eta),
$$

and in cosmic time $t=\int a \mathrm{d}\eta=\mathrm{gd}(\sqrt s \eta)/\sqrt\kappa$ one finds $a=\sqrt{s/\kappa}\cos(\sqrt\kappa t)$, with $\dot a^2=-k+\frac\Lambda3a^2$ and $\ddot a=\frac\Lambda3a$. For $r=1$ one has $k=-1$.

*Cosmic-time form.* With $\mathrm{d}\eta=\mathrm{d}t/a$ and $\varepsilon=C$, the same function satisfies $\ddot a=\frac\Lambda3a-C/a^3$ (an Ermakov–Pinney equation) with energy $\dot a^2-\frac\Lambda3a^2-C/a^2=-k$. So the roles of $k$ and $C$ are exchanged: $k$ is a parameter in conformal time and a constant of integration in cosmic time, and conversely for $C$.

*Regime.* The finite-norm bump corresponds to $C=0$, $k<0$, $\Lambda<0$, an open universe with negative cosmological constant and no radiation. It is not the $\Lambda>0$ universe of observational cosmology; other sign patterns of $(k,\Lambda,C)$ correspond to solutions of (S) of other types, which are not finite-norm. Physical readings of this dictionary (for example kinematic readings) belong to Essay III and are labelled **[I]** there.

---

## 6. Structural properties of the Master equation

These properties hold for every solution of (M) and do not depend on any identification.

### 6.1 Variational structure

**Proposition 6.1 [V].** Let $L=-\frac12x^3f'^2+\frac12(1-r^2)xf^2+2\mu r^2x^3f^4$ and $\mathrm{EL}(L)=\partial L/\partial f-(\partial L/\partial f')'$.

1. $\mathrm{EL}(L)=x \mathrm{SO}[f]$. So (M) is variational with multiplier $M(x)=x$. The multiplier is unique up to a constant among functions of $x$ alone, because $M\cdot\mathrm{SO}$ is self-adjoint iff $(Mx^2)'=3Mx$, i.e. $M'x=M$. (There are other multipliers that depend on $f,f'$ through $\varepsilon$.)
2. The action is invariant under $x\mapsto\lambda x$, $f\mapsto f/\lambda$. For $\mathcal L=-2L$ the Noether charge $Q=p(\delta f-f'\delta x)+\mathcal L \delta x$, with $\delta x=x$, $\delta f=-f$, $p=\partial\mathcal L/\partial f'$, equals $-\varepsilon/4$. The first integral $\varepsilon$ is thus the Noether charge of the dilation.
3. In $(u,y)$: $\mathcal L \mathrm{d}x=\frac14[y'^2+r^2y^2-\mu r^2y^4]\mathrm{d}u-\frac14 \mathrm{d}(y^2)$; the energy of the first term is $\varepsilon/4$. (The $x$-Lagrangian has explicit $x$-dependence, so the Beltrami identity holds in $(u,y)$, where it coincides with the dilation charge.)
4. On the bump (e.g. $r=1.3$, $\mu=0.72$): $\int\mathcal L \mathrm{d}x=r/(3\mu)$, and $\int y'^2:\int r^2y^2:\int\mu r^2y^4=1:3:2$, so that $\int y'^2+\int\mu r^2y^4=\int r^2y^2$ (a virial relation).

### 6.2 Prolongation and the log-derivative map

**Proposition 6.2 [V].**

1. Differentiating (S): $y'''=r^2y'(1-6\mu y^2)$. The quantity $C=y''-r^2y+2\mu r^2y^3$ is a first integral of this third-order equation, and (S) is its invariant surface $C=0$. The general solution of the third-order equation has three constants $(C,\varepsilon_C,u_0)$, where $\varepsilon_C=y'^2-r^2y^2+\mu r^2y^4-2Cy$ is the first integral of $y''=r^2y-2\mu r^2y^3+C$. So $\mathbb R^3\supset\lbrace C=0\rbrace \supset\lbrace C=0,\ \varepsilon=0\rbrace $ (in the phase space $(y,y',y'')$) is a nested chain of invariant sets of dimension 3, 2, 1. (The jerk equation has odd order, so it is not the Euler–Lagrange equation of a regular Lagrangian; it is the union of the variational equations $y''=r^2y-2\mu r^2y^3+C$.)
2. For every solution of (S) (any $\varepsilon$), on every interval where $y\neq0$, $v=y'/y$ satisfies $v'+v^2=r^2(1-2\mu y^2)$ and the closed equation

$$
v''+2r^2v-2v^3=0,\qquad y^2=\frac{r^2-v'-v^2}{2\mu r^2}.
$$

This is a Miura-type map from (S) to the softening Duffing (kink) equation, independent of $\mu$. On the bump, $W=-v/r$ is the kink $\tanh\theta$, with $W'=r(1-W^2)$ and $W''=-2r^2W+2r^2W^3$.
3. On the bump, $\mu y^2=1,\frac12,\frac16$ at the peak, at the inflection (where $y''=0$, which is also the minimum of the potential $V=-\frac12r^2y^2+\frac12\mu r^2y^4$), and at the other zero of $y'''$ (an extremum of $y''$; the first zero of $y'''$ is the peak, where $y'=0$), respectively.

---

## 7. Status ledger

| Item | Label | Basis |
|---|---|---|
| Theorem 4.2 and Theorem 4.1 | **[T]** | proof in §4 is complete as written; independent audit still to be done; Step 4 needs the closest reading |
| Proposition 3.5 | **[T]** | short proof in §3.5 |
| Proposition 4.4 | **[V]** (1, 2), **[T]** (3) | Appendix A |
| Remark 4.3 (other norms) | **[T]**, sketch | details omitted |
| Propositions 3.1–3.4 | **[V]** | Appendix A |
| Proposition 5.1 | **[V]**, Jacobi family **[K]** | Appendix A |
| Proposition 5.2 | **[V]** (a, b, d), **[K]** (c) | Yang–Mills reduction not re-derived |
| Proposition 5.3 | **[V]** | physical reading **[I]**, not claimed here |
| Propositions 6.1, 6.2 | **[V]** | Appendix A |
| Relation to Yamabe/Hardy literature (§1.2) | **[K]** | bibliographic data confirmed; theorem statements not checked (Appendix C) |

---

## 8. The series

This paper is the foundational paper. The companion essays develop the identifications, and each carries its own open questions.

- **Essay I, The Mechanical Mirror (the Euler-top separatrix).** The elliptic branch $k<1$, the relation of its third component to $\varepsilon$, the Nahm form, and what exactly is "mirrored" (the kink $W$ and the bump $S$ on the circle $W^2+S^2=1$).
- **Essay II, The Gauge Node (the instanton profile at $r=1$).** The Yamabe–Hardy connection of §1.2 in detail; the derivation of the Yang–Mills reduction; the role of $r\ne1$ (Hardy coupling, cone angle).
- **Essay III, The Conformal Coast (kinematic identifications in Friedmann cosmology).** The two dictionaries of Proposition 5.3, sector caveats, and the kinematic (Rindler-type) readings, each labelled by status.

A follow-up paper will treat the one-parameter family of equations obtained from the reciprocal powers $y_q=J^{-q}$ of the backbone $J''=r^2J$ (Proposition 3.5 is its $q=1$ case). It is not used here.

---

## Appendix A. Checked identities

Each item was checked symbolically (SymPy) or numerically (mpmath, 20–30 digits) in the working sessions. The scripts are to be assembled into a single regression suite (open item). "Residual 0" means the symbolic difference simplified to 0.

| ID | Statement | Method |
|---|---|---|
| A1 | (M) holds on the bump | symbolic, residual 0 |
| A2 | $f_\lambda$ solves (M); $\mathrm{SO}[f_\lambda](x)=\lambda^{-3}\mathrm{SO}[f](x/\lambda)$; $\int f^2x^a$ invariant iff $a=1$ | symbolic; direct substitution |
| A3 | $\mathrm{SO}[f]=\frac1{2x}(y''-r^2y+2\mu r^2y^3)$ | symbolic, residual 0 |
| A4 | $\varepsilon=4x^2\Phi[f]$ | symbolic, residual 0 |
| A5 | (E1) holds on the bump; $\Phi[f]/(r^2f^2)=W^2+S^2-1$; $S=\mathrm{sech}\theta$, $W=\tanh\theta$ on the bump | symbolic, residual 0 |
| A6 | $\lvert z\rvert ^2\Delta F=x^2f''+3xf'$ (radial Laplacian in $\mathbb R^4$) | direct |
| A7 | $r=1$: bump $=x_0/(\sqrt\mu(x_0^2+x^2))$ and $\Delta F+8\mu F^3=0$ | symbolic, residual 0 |
| A8 | Scalar curvature of $f^2\delta$ on $\mathbb R^4$: $-6\Delta f/f^3=6(1-r^2)/(\lvert z\rvert ^2f^2)+48\mu r^2$; $=48\mu$ at $r=1$ | symbolic, residual 0 |
| A9 | $(\ln f)''=-r^2S^2$ on the bump (Liouville, $K=4\mu r^2$) | numeric, 30 digits |
| A10 | Euler top at $k=1$; Nahm triple $(-\coth,-\mathrm{csch},-\mathrm{csch})$ | symbolic, residual 0 |
| A11 | $\phi=(1+W)/2$: $\phi'=2r\phi(1-\phi)$, $\phi''=4r^2\phi(1-\phi)(1-2\phi)$, $\phi(1-\phi)=\mu x^2f^2$; $r=1$: $\phi=x^2/(x^2+x_0^2)$ | symbolic, residual 0 |
| A12 | Conformal-time Friedmann relation and its bump; cosmic-time form of the bump; $\mathrm{gd}$ time map | symbolic, residual 0; numeric, 30 digits |
| A13 | $N(f)=1/(2r\mu)$ ($r=1.3$, $\mu=0.72$: $0.534188034188$); Dirichlet energy $0.83511396$ ($r=1.3$), $2.3842593$ ($r=0.3$), $x_0=1$ | numeric, 25 digits |
| A14 | $\mathrm{EL}(L)=x \mathrm{SO}$; $M=x$ unique among functions of $x$; Noether charge $=-\varepsilon/4$; $(u,y)$ form of $\mathcal L \mathrm{d}x$ | symbolic, residual 0 |
| A15 | $\int\mathcal L \mathrm{d}x=r/(3\mu)=0.6018518519$; ratio $1:3:2$ | numeric, 20 digits |
| A16 | Jerk equation; $C$ is a first integral | symbolic, residual 0 |
| A17 | $v''+2r^2v-2v^3=0$ for all $\varepsilon$, with $y^2=(r^2-v'-v^2)/(2\mu r^2)$ | symbolic; numeric on a dn solution, residual $3.7\times10^{-31}$ |
| A18 | Proposition 4.4(1,2): $\mathrm{SO}[f_s]=r^2/(2\sqrt\mu x)$; junction jumps in $f,f'\sim10^{-8}$ (numerical), $f''$ jumps from $0.18267$ to $1.17851$ | symbolic; numeric |
| A19 | Step 3: $(y^2)''=2y'^2+2sy^2+4\lvert \kappa\rvert y^4$ | symbolic |
| A20 | Step 7: $\hat y$ solves (S) with data $(\sqrt{s/\kappa},0)$ at $u_0$ | symbolic, residual 0 |
| A21 | $\mathrm{SO}[f_\pm]=0$ for $f_\pm=\pm1/(2\sqrt{2\mu} x)$; $\Delta F+8\mu F^3=0$ for $F=1/(2\sqrt{2\mu} \lvert z\rvert )$ at $r=1$; $\varepsilon_C$ is a first integral of $y''=r^2y-2\mu r^2y^3+C$ | symbolic, residual 0 |
| A22 | Sweep over sign classes of $(s,\kappa)$ on $\varepsilon=0$: only $(s>0,\kappa>0)$ decays at both ends | numeric consistency check only, not a proof |

## Appendix B. Notation

| Symbol | Meaning here | Clash avoided |
|---|---|---|
| $u$ | $\ln x$ | not $\ln(x/c)$ |
| $\theta$ | $r\ln(x/x_0)$, the argument of sech and tanh | not the Gudermannian angle |
| $\varepsilon$ | $y'^2-sy^2+\kappa y^4$ (the cubic's first integral) | not the Ermakov–Pinney energy ($\varepsilon=4E_P$ there) |
| $s,\kappa$ | $r^2$, $\mu r^2$ | $\kappa$ is not $\mu$ |
| $'$ | $\mathrm{d}/\mathrm{d}x$ on $f$; $\mathrm{d}/\mathrm{d}u$ on $y$, $\phi$, $a'$-type objects stated explicitly | in §5.1 prime means $\mathrm{d}/\mathrm{d}\theta$ |
| $\mathrm{SO}$ | operator on the left of (M) | |
| $N(f)$ | $\int f^2x \mathrm{d}x$ | norm squared |

## Appendix C. Status of the literature

Verification here has three levels, kept separate: (1) bibliographic data confirmed; (2) theorem statement read in a primary source; (3) application to this paper checked. Only level (1) was done.

| Ref. | Used for | Level (1) | Levels (2), (3) |
|---|---|---|---|
| [1] Aubin (1976) | bubbles as Sobolev extremals | confirmed in several citing sources | not checked |
| [2] Talenti (1976), DOI 10.1007/bf02418013 | same | confirmed | not checked |
| [3] Gidas–Ni–Nirenberg (1979) | radial symmetry of positive solutions | title confirmed; page range from memory | not checked |
| [4] Gidas–Ni–Nirenberg (1981) | symmetry on $\mathbb R^n$ | title confirmed; volume, publisher and pages from memory | not checked |
| [5] Caffarelli–Gidas–Spruck (1989), pp. 271–297 | removal of the decay hypothesis; isolated singularities | confirmed (title, journal, pages) | the relation to [3, 4] is taken from a secondary source |
| [6] Terracini (1996), DOI 10.57262/ade/1366896239 | critical equation with Hardy-type coefficient | confirmed; abstract read | main theorem not read |
| [7] Berestycki–Lions (1983), DOI 10.1007/BF00250555 | ground states of scalar-field equations | confirmed | not checked |
| [8] Peletier–Serrin (1983) | uniqueness of positive radial solutions | title and volume seen in a reference list | not checked |
| [9] Belavin–Polyakov–Schwartz–Tyupkin (1975) | the instanton | from memory | not checked |

The claim that the periodic positive solutions in $\mathbb R^n\setminus\lbrace 0\rbrace $ are called Fowler or Delaunay-type solutions is taken from secondary literature and is flagged accordingly. No novelty claim is made; a bounded novelty search (terminology variants such as "Emden–Fowler", "Hardy–Sobolev", "Yamabe", "radial", "log variable") is an open item.

## References

1. T. Aubin, *Problèmes isopérimétriques et espaces de Sobolev*, J. Differential Geom. **11** (1976), no. 4, 573–598.
2. G. Talenti, *Best constant in Sobolev inequality*, Ann. Mat. Pura Appl. (4) **110** (1976), 353–372.
3. B. Gidas, W.-M. Ni, L. Nirenberg, *Symmetry and related properties via the maximum principle*, Comm. Math. Phys. **68** (1979), 209–243.
4. B. Gidas, W.-M. Ni, L. Nirenberg, *Symmetry of positive solutions of nonlinear elliptic equations in $\mathbb R^n$*, in *Mathematical Analysis and Applications, Part A*, Adv. Math. Suppl. Stud. **7A**, Academic Press, 1981.
5. L. A. Caffarelli, B. Gidas, J. Spruck, *Asymptotic symmetry and local behavior of semilinear elliptic equations with critical Sobolev growth*, Comm. Pure Appl. Math. **42** (1989), 271–297.
6. S. Terracini, *On positive entire solutions to a class of equations with a singular coefficient and critical exponent*, Adv. Differential Equations **1** (1996), no. 2, 241–264.
7. H. Berestycki, P.-L. Lions, *Nonlinear scalar field equations, I. Existence of a ground state*, Arch. Rational Mech. Anal. **82** (1983), 313–345.
8. L. A. Peletier, J. Serrin, *Uniqueness of positive solutions of semilinear equations in $\mathbb R^n$*, Arch. Rational Mech. Anal. **81** (1983), 181–197.
9. A. A. Belavin, A. M. Polyakov, A. S. Schwartz, Yu. S. Tyupkin, *Pseudoparticle solutions of the Yang–Mills equations*, Phys. Lett. B **59** (1975), 85–87.

---

*Items to finish before submission:* (i) independent audit of the proof of Theorem 4.2, especially Step 4; (ii) literature check of [3–6, 8] at levels (2) and (3), and the bounded novelty search; (iii) one regression suite for Appendix A; (iv) final notation sheet.
