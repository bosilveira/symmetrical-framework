# 1.10 — Logarithmic measure, Mellin and Fourier transform

**Change of variables [E].** Put $x=ce^u$, $dx=x\,du$:

```math
f(x;r,c)\,dx=\frac12\mathrm{sech}(ru)\,du.
```

For every measurable $\phi$ for which either side is absolutely integrable,

```math
\int_0^\infty \phi(x)f(x;r,c)\,dx =\frac12\int_{\mathbb R}\phi(ce^u)\mathrm{sech}(ru)\,du.
```

The half-split follows by evenness:

```math
\int_0^c f\,dx=\int_c^\infty f\,dx=\frac{\pi}{4r}.
```

**Mellin transform [E].** For $1-r<\Re s<1+r$,

```math
\mathcal M f(s):=\int_0^\infty x^{s-1}f(x)\,dx =\frac{\pi c^{s-1}}{2r}\sec\!\left(\frac{\pi(s-1)}{2r}\right).
```

The scale-correct reflection equation is

```math
\mathcal Mf(s)=c^{2s-2}\mathcal Mf(2-s).
```

This equality extends meromorphically, but the integral defining $\mathcal M$ does not converge outside its strip.

**Fourier on the central Mellin line [K/E].** With $\widehat{h}(\omega)=\int_{\mathbb R}h(u)e^{-i\omega u}\,du$,

```math
\widehat S(\omega)=\frac{\pi}{r}\mathrm{sech}\left(\frac{\pi\omega}{2r}\right),\quad \mathcal Mf(1+i\omega)=\frac{c^{i\omega}}2\widehat S(-\omega).
```

Because $|c^{i\omega}|=1$ for $c>0$, Plancherel yields

```math
\frac1{2\pi}\int_{\mathbb R}|\mathcal Mf(1+i\omega)|^2\,d\omega =\int_0^\infty xf(x)^2\,dx=\frac1{2r}.
```

This is the precise Mellin–Fourier correspondence, including the factor $x$ and the log-coordinate shift.

## Step-by-step proof of the half-splitting integral

The original notes used two equivalent primitives. Both give a concise global proof once the endpoint limits and the orientation of the coordinate change are tracked.

**Step 1.** The logarithmic coordinate is $u=\log(x/c)$, and its ordered limits are $x=0^+\leftrightarrow u=-\infty$, $x=c\leftrightarrow u=0$, and $x=\infty\leftrightarrow u=\infty$.

**Step 2.** Substitute $dx=x\,du$ into $f=S/(2x)$:

```math
\int_0^\infty f(x;r,c)\,dx=\frac12\int_{-\infty}^{\infty}\mathrm{sech}(ru)\,du.
```

**Step 3.** Differentiate the real Gudermannian primitive:

```math
\frac{d}{du}\arctan(\sinh(ru))=r\,\mathrm{sech}(ru).
```

**Step 4.** Evaluate its upper and lower endpoint values, $\pi/2$ and $-\pi/2$:

```math
\int_0^\infty f(x;r,c)\,dx=\frac{1}{2r}\left[\arctan(\sinh(ru))\right]_{-\infty}^{\infty}=\frac{\pi}{2r}.
```

**Step 5.** Evenness of the pushed measure gives identical halves:

```math
\int_0^c f(x;r,c)\,dx=\frac12\int_{-\infty}^{0}\mathrm{sech}(ru)\,du=\frac{\pi}{4r}=\int_c^\infty f(x;r,c)\,dx.
```

The equal halves reflect **integration of a positive density**, not a time-dependent conservation law; they are also preserved by the measure involution $x\mapsto c^2/x$ proved in Chapter 2.
