# 03.03 — Sech Fourier self-reciprocity and the regular Langevin hierarchy

**Status:** exact transform identities and classical hypergeometric/modified-Bessel recurrences, with explicit measures, branches, parameters and proof steps. This is an **analytic companion** to the [elementary web §00.11](../00-foundations/00-11-elementary-function-web.md), not a declaration of a new transform or an identification of all the framework's spectral problems.

Throughout, $`x,c,r>0`$, $`u=\log(x/c)`$, $`\theta=ru`$, $`S_r(u)=\mathrm{sech}(ru)`$. The Fourier transform here is in **$`u`$** and must not be conflated with a Fourier transform directly in $`x`$.

## 1. Two Fourier normalizations, explicitly compared

Define the **nonunitary** and **unitary** Fourier transforms by

```math
\widehat h_{\mathrm N}(k)=\int_{\mathbb R}e^{-iku}h(u)\,du,\qquad \widehat h_{\mathrm U}(k)=\frac1{\sqrt{2\pi}}\int_{\mathbb R}e^{-iku}h(u)\,du.
```

**Sech transform.** For real $`k`$ and $`r>0`$,

```math
\widehat {S_r}_{\mathrm N}(k)=\frac\pi r\,\mathrm{sech}\left(\frac{\pi k}{2r}\right),\qquad \widehat {S_r}_{\mathrm U}(k)=\frac{\sqrt{\pi/2}}r\,\mathrm{sech}\left(\frac{\pi k}{2r}\right).
```

**Proof with convergence:** substitute $`t=e^{2ru}`$ in the absolutely convergent integral. Then

```math
\widehat {S_r}_{\mathrm N}(k)=\frac1r\int_0^\infty\frac{t^{-1/2-ik/(2r)}}{1+t}\,dt=\frac1r\mathrm B\left(\frac12-\frac{ik}{2r},\frac12+\frac{ik}{2r}\right).
```

Euler's beta identity and $`\Gamma(1/2+iy)\Gamma(1/2-iy)=\pi/\cosh(\pi y)`$ yield the result. No distributional extension is needed for real $`k`$, and the transform formula respects the positive resolution $`r`$.

Define the **resolution-dual parameter**

```math
r^\vee=\frac{\pi}{2r},\qquad (r^\vee)^\vee=r,\qquad r_*=\sqrt{\frac\pi2}.
```

Then the unitary transform reads $`\widehat {S_r}_{\mathrm U}=(r^\vee/r_*)S_{r^\vee}`$. Precisely at $`r=r_*`$, it is self-reciprocal:

```math
\widehat{S_{r_*}}_{\mathrm U}(k)=S_{r_*}(k).
```

The transform's output variable is the **frequency $`k`$**, not the original spatial coordinate. The fixed point concerns the normalized logarithmic-line profile, not the raw kernel $`f(x;r,c)`$.

## 2. The spatial kernel, its center and Mellin–Fourier relation

The original field $`f(x;r,c)=S_r(u)/(2x)`$ satisfies $`g(u):=xf(ce^u;r,c)=S_r(u)/2`$, and

```math
f(x;r,c)\,dx=g(u)\,du,\qquad x=ce^u.
```

Under the existing nonunitary convention in [§03.01](03-01-mellin-fourier-plancherel.md),

```math
\widehat g_{\mathrm N}(k)=\frac\pi{2r}\mathrm{sech}\left(\frac{\pi k}{2r}\right),\qquad \mathcal M[f](1+ik)=c^{ik}\widehat g_{\mathrm N}(-k).
```

The factor $`c^{ik}`$ remembers the original center in the Mellin transform. The Fourier self-reciprocity in the logarithmic chart is therefore fully compatible with the explicit $`c`$ dependence of $`f(x;r,c)`$.

## 3. A dimension-indexed analytic family behind tanh and Langevin

Let **$`D>0`$ be an independently chosen index**, not an assertion of an ambient space dimension. Define the even entire real function

```math
Z_D(\theta)={}_0F_1\left(;D/2;\theta^2/4\right)=\sum_{n=0}^\infty\frac{(\theta^2/4)^n}{n!(D/2)_n},\qquad Z_D(0)=1.
```

For the integer examples $`D=1,3`$,

```math
Z_1(\theta)=\cosh\theta=R,\qquad Z_3(\theta)=\frac{\sinh\theta}{\theta}=\frac b\theta,\qquad Z_3(0)=1.
```

Define its *logarithmic derivative* $`L_D(\theta)=Z_D'(\theta)/Z_D(\theta)`$. For real $`\theta`$, the series gives $`Z_D(\theta)>0`$, so the log derivative is smooth. Direct differentiation of the series gives the **index-raising recurrence**

```math
Z_D'(\theta)=\frac{\theta}{D}Z_{D+2}(\theta),\qquad Z_{D+2}(\theta)=\frac D\theta Z_D'(\theta)\quad(\theta\ne0).
```

The same series proves

```math
Z_D''+\frac{D-1}{\theta}Z_D'-Z_D=0,\qquad L_D'=1-L_D^2-\frac{D-1}{\theta}L_D\quad(\theta\ne0).
```

Both identities extend through $`\theta=0`$ in the regular solution sense; $`L_D(\theta)=\theta/D+O(\theta^3)`$ there. In particular,

```math
L_1(\theta)=\tanh\theta=W,\qquad L_3(\theta)=\coth\theta-\frac1\theta.
```

The second function is the **classical Langevin function**, whose apparent pole cancels at the origin. This is a mathematically exact dimension-indexed recurrence with a chosen normalization; a higher-dimensional radial PDE interpretation would require its own independent operator and boundary conditions.

## 4. Parameter transport of the Langevin hierarchy

Define the original-chart family $`\mathscr Z_D(x;r,c)=Z_D(r\log(x/c))`$, holding the index $`D>0`$ fixed. Its logarithmic derivatives in the chart $`(x,c,r)`$ are

```math
\partial_x\log\mathscr Z_D=\frac r xL_D(\theta),\qquad \partial_c\log\mathscr Z_D=-\frac r cL_D(\theta),\qquad \partial_r\log\mathscr Z_D=uL_D(\theta).
```

At fixed $`r,c`$, the logarithmic slope with respect to $`u`$ becomes $`q_D=(\log\mathscr Z_D)_u=rL_D(\theta)`$. Its own resolution derivative is **not** obtained by discarding the prefactor $`r`$:

```math
(q_D)_r|_{x,c}=L_D+\theta L_D',\qquad (q_D)_c|_{x,r}=-\frac{r^2}{c}L_D'.
```

Here primes on $`L_D`$ differentiate in **$`\theta`$**, while the subscript $`r,c`$ identifies fixed coordinates. This generalizes the separately audited $`q_1=rW`$ derivative table in [§00.09](../00-foundations/00-09-second-derivative-charts.md).

**Evidence:** the Fourier beta integral and $`{}_0F_1`$ power-series differentiations are proofs under the displayed hypotheses. Finite [symbolic/numerical checks](../_standards/verify_elementary_function_web.py) are supplementary. The transform belongs to chapter 03; the original arctangent primitive belongs to [§02.02](../02-calculus-norms/02-02-primitives.md).
