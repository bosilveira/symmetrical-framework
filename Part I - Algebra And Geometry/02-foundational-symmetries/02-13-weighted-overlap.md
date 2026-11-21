# 2.13 — Exact weighted two-scale overlap and a positive-definite kernel

**Status [E/K].** Fix the **same** resolution $r>0$ for both profiles, but allow arbitrary $c_1,c_2>0$. Equip the real space of functions on $(0,\infty)$ with the weighted inner product

```math
\langle g,h\rangle_x:=\int_0^\infty x\,g(x)h(x)\,dx.
```

By the identity $\int_0^\infty x f(x;r,c)^2\,dx=1/(2r)$, every profile has the same positive norm. This is the canonical Hilbert space from the logarithmic coordinate change, not the raw $L^2(dx)$ norm.

## Exact overlap theorem

Set the dimensionless log-scale difference $\delta=r\log(c_2/c_1)$. Then

```math
\langle f(\cdot;r,c_1),f(\cdot;r,c_2)\rangle_x=\frac{1}{2r}\frac{\delta}{\sinh\delta},\qquad \left.\frac{\delta}{\sinh\delta}\right|_{\delta=0}:=1.
```

The quotient is positive and even in $\delta$. In particular, the integral depends **only** on the relative scale $c_2/c_1$, not on their geometric mean.

### Step-by-step derivation

**Step 1.** Let $C=\sqrt{c_1c_2}$ and $t=r\log(x/C)$. Then $dx/x=dt/r$, and the two hyperbolic arguments are $t+\delta/2$ and $t-\delta/2$.

```math
\langle f_{c_1},f_{c_2}\rangle_x=\frac{1}{4r}\int_{-\infty}^{\infty}\mathrm{sech}(t+\delta/2)\mathrm{sech}(t-\delta/2)\,dt.
```

**Step 2.** Apply $2\cosh a\cosh b=\cosh(a+b)+\cosh(a-b)$:

```math
\mathrm{sech}(t+\delta/2)\mathrm{sech}(t-\delta/2)=\frac{2}{\cosh(2t)+\cosh\delta}.
```

**Step 3.** Substitute $z=\tanh t$, so $z\in(-1,1)$ and $dt=dz/(1-z^2)$. Simplify $\cosh(2t)=(1+z^2)/(1-z^2)$ to obtain

```math
\int_{\mathbb R}\frac{2\,dt}{\cosh(2t)+\cosh\delta}=\frac1{\cosh^2(\delta/2)}\int_{-1}^{1}\frac{dz}{1-\tanh^2(\delta/2)z^2}.
```

**Step 4.** For $\delta\ne0$, integrate the rational function and use $\mathrm{arctanh}(\tanh(\delta/2))=\delta/2$:

```math
\frac1{\cosh^2(\delta/2)}\int_{-1}^{1}\frac{dz}{1-\tanh^2(\delta/2)z^2}=\frac{2\delta}{\sinh\delta}.
```

**Step 5.** Multiply by $1/(4r)$; the case $\delta=0$ follows continuously from $\delta/\sinh\delta\to1$. This proves the theorem. For $C=\sqrt{c_1c_2}$, the reflection in [§2.6](02-06-hyperbolic-double.md) gives the additional exact half split

```math
\int_0^C x f(x;r,c_1)f(x;r,c_2)\,dx=\frac{\delta}{4r\sinh\delta}=\int_C^\infty x f(x;r,c_1)f(x;r,c_2)\,dx.
```

## Positive definiteness and the Fourier spectrum

Normalize the Hilbert-space vectors by $\phi_c=\sqrt{2r}\,f(\cdot;r,c)$. Their Gram kernel is

```math
K_r(c_1,c_2)=\langle\phi_{c_1},\phi_{c_2}\rangle_x=\frac{r\log(c_2/c_1)}{\sinh(r\log(c_2/c_1))}.
```

For any finite coefficients $z_j\in\mathbb C$ and positive scales $c_j$, $\sum_{j,k}\overline z_jz_k K_r(c_j,c_k)=\|\sum_jz_j\phi_{c_j}\|_x^2\ge0$. Thus the kernel is **positive definite** (indeed strictly positive definite for distinct log-centers, by the Fourier representation below).

Using $\widehat{\mathrm{sech}}(\omega)=\pi\mathrm{sech}(\pi\omega/2)$ and the convolution theorem, the translation-invariant function $k(\delta)=\delta/\sinh\delta$ has the exact Fourier transform

```math
\widehat{k}(\omega)=\int_{\mathbb R}\frac{\delta}{\sinh\delta}e^{-i\omega\delta}\,d\delta=\frac{\pi^2}{2}\mathrm{sech}^2\left(\frac{\pi\omega}{2}\right)>0.
```

The Fourier transform is strictly positive, so the quadratic form above vanishes only for zero coefficients when the scales are pairwise distinct. This is a standard positive-definiteness argument, not evidence for a new integrable hierarchy.

## The induced scale-distance

For the normalized profiles, the exact squared Hilbert distance is

```math
\|\phi_{c_1}-\phi_{c_2}\|_x^2=2\left[1-\frac{\delta}{\sinh\delta}\right].
```

The local expansion $\delta/\sinh\delta=1-\delta^2/6+7\delta^4/360+O(\delta^6)$ therefore gives

```math
\|\phi_{c_1}-\phi_{c_2}\|_x^2=\frac{r^2}{3}\log^2(c_2/c_1)+O(\log^4(c_2/c_1)).
```

This defines an exact, geometrically meaningful metric on the curve of normalized profiles. It is **different** from the Fisher metric on the family of probability distributions derived in [§2.14](02-14-fisher-information.md).
