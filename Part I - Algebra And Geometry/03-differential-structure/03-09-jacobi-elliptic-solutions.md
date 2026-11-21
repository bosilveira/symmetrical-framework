# 3.9 — Jacobi-elliptic solutions and the energy-level curve

**Status [E/K].** Fix $`r,\mu,c>0`$ and $`u=\log(x/c)`$. The second-order Master for $`y(u)=2xf_\mu(x)`$ is

```math
y_{uu}=r^2y-2\mu r^2y^3,\qquad \varepsilon=y_u^2-r^2y^2+\mu r^2y^4.
```

The energy level distinguishes the positive periodic solution family, the localized separatrix, and the sign-changing periodic family. Here $`\mathrm{dn}(z\mid m)`$ and $`\mathrm{cn}(z\mid m)`$ denote the standard Jacobi elliptic functions with parameter $`m`$, **not** modulus $`\sqrt m`$.

The translation parameter # 3.9 — Jacobi-elliptic solutions and the energy-level curve

**Status [E/K].** Fix $`r,\mu,c>0`$ and $`u=\log(x/c)`$. The second-order Master for $`y(u)=2xf_\mu(x)`$ is

```math
y_{uu}=r^2y-2\mu r^2y^3,\qquad \varepsilon=y_u^2-r^2y^2+\mu r^2y^4.
```

The energy level distinguishes the positive periodic solution family, the localized separatrix, and the sign-changing periodic family. Here $`\mathrm{dn}(z\mid m)`$ and $`\mathrm{cn}(z\mid m)`$ denote the standard Jacobi elliptic functions with parameter $`m`$, **not** modulus $`\sqrt m`$.

u_0`$ corresponds to a positive spatial center # 3.9 — Jacobi-elliptic solutions and the energy-level curve

**Status [E/K].** Fix $`r,\mu,c>0`$ and $`u=\log(x/c)`$. The second-order Master for $`y(u)=2xf_\mu(x)`$ is

```math
y_{uu}=r^2y-2\mu r^2y^3,\qquad \varepsilon=y_u^2-r^2y^2+\mu r^2y^4.
```

The energy level distinguishes the positive periodic solution family, the localized separatrix, and the sign-changing periodic family. Here $`\mathrm{dn}(z\mid m)`$ and $`\mathrm{cn}(z\mid m)`$ denote the standard Jacobi elliptic functions with parameter $`m`$, **not** modulus $`\sqrt m`$.

x_0=c\exp(u_0)`$, since # 3.9 — Jacobi-elliptic solutions and the energy-level curve

**Status [E/K].** Fix $`r,\mu,c>0`$ and $`u=\log(x/c)`$. The second-order Master for $`y(u)=2xf_\mu(x)`$ is

```math
y_{uu}=r^2y-2\mu r^2y^3,\qquad \varepsilon=y_u^2-r^2y^2+\mu r^2y^4.
```

The energy level distinguishes the positive periodic solution family, the localized separatrix, and the sign-changing periodic family. Here $`\mathrm{dn}(z\mid m)`$ and $`\mathrm{cn}(z\mid m)`$ denote the standard Jacobi elliptic functions with parameter $`m`$, **not** modulus $`\sqrt m`$.

x=ce^u`$. Every elliptic solution below can be mapped back to a spatial Master profile using # 3.9 — Jacobi-elliptic solutions and the energy-level curve

**Status [E/K].** Fix $`r,\mu,c>0`$ and $`u=\log(x/c)`$. The second-order Master for $`y(u)=2xf_\mu(x)`$ is

```math
y_{uu}=r^2y-2\mu r^2y^3,\qquad \varepsilon=y_u^2-r^2y^2+\mu r^2y^4.
```

The energy level distinguishes the positive periodic solution family, the localized separatrix, and the sign-changing periodic family. Here $`\mathrm{dn}(z\mid m)`$ and $`\mathrm{cn}(z\mid m)`$ denote the standard Jacobi elliptic functions with parameter $`m`$, **not** modulus $`\sqrt m`$.

f_\mu(x)=y(\log(x/c))/(2x)`$.

## Dimensionless energy curve and its singular levels

Introduce the dimensionless dependent variable $`z=\sqrt\mu\,y`$, the independent variable $`\theta=ru`$, and $`e=\mu\varepsilon/r^2`$. Then

```math
z_{\theta\theta}=z-2z^3,\qquad z_\theta^2=e+z^2-z^4.
```

**Step 1.** Complete the square:

```math
e+z^2-z^4=e+\tfrac14-(z^2-\tfrac12)^2.
```

Real trajectories require $`e\ge-1/4`$. Equality gives only the constant equilibria $`z=\pm1/\sqrt2`$.

**Step 2.** The complex algebraic energy curve is the quartic

```math
\mathcal C_e:\quad v^2=e+z^2-z^4,\qquad e\in\mathbb C.
```

Its discriminant is nonzero exactly when $`e\ne0`$ and $`e\ne-1/4`$. For those generic values the smooth projective normalization has genus one. At $`e=0`$ the root $`z=0`$ is double, and at $`e=-1/4`$ the quartic is a negative perfect square; both are singular degenerations. **A genus-one algebraic curve is not the same as a claim that every real energy level is a compact oval.**

## Positive periodic family: $`\mathrm{dn}`$

For $`0\le m<1`$, define

```math
y_m(u)=\frac{1}{\sqrt{\mu(2-m)}}\,\mathrm{dn}\left(\frac{r(u-u_0)}{\sqrt{2-m}}\mid m\right).
```

**Step 1.** Use the classical Jacobi identity

```math
\frac{d^2}{dz^2}\mathrm{dn}(z\mid m)=(2-m)\mathrm{dn}(z\mid m)-2\mathrm{dn}^3(z\mid m).
```

**Step 2.** Put $`k=r/\sqrt{2-m}`$ and $`A=1/\sqrt{\mu(2-m)}`$. For $`y=A\,\mathrm{dn}(k(u-u_0)\mid m)`$, the Jacobi identity gives

```math
y_{uu}=k^2(2-m)y-\frac{2k^2}{A^2}y^3=r^2y-2\mu r^2y^3.
```

**Step 3.** At $`u=u_0`$, $`\mathrm{dn}(0\mid m)=1`$ and the first derivative is zero. Substitute $`y=A`$ in the energy integral:

```math
\varepsilon_{\mathrm{dn}}(m)=-r^2A^2+\mu r^2A^4=-\frac{r^2}{\mu}\frac{1-m}{(2-m)^2}.
```

For $`0<m<1`$, $`\varepsilon_{\mathrm{dn}}\in(-r^2/(4\mu),0)`$ and the solution stays strictly positive. Its period in $`u`$ is

```math
T_{\mathrm{dn}}(m)=\frac{2\sqrt{2-m}}{r}\,K(m),
```

where $`K(m)`$ is the complete elliptic integral of the first kind with parameter $`m`$. At $`m=0`$, $`\mathrm{dn}\equiv1`$ and $`y=1/\sqrt{2\mu}`$ is an equilibrium. As $`m\uparrow1`$, $`\mathrm{dn}(z\mid m)\to\mathrm{sech}\,z`$ on compact real sets, the period diverges, and $`y_m\to\mu^{-1/2}\mathrm{sech}(r(u-u_0))`$.

## Sign-changing periodic family: $`\mathrm{cn}`$

For $`1/2<m<1`$, define the real solution

```math
y_m^{\mathrm{cn}}(u)=\sqrt{\frac{m}{\mu(2m-1)}}\,\mathrm{cn}\left(\frac{r(u-u_0)}{\sqrt{2m-1}}\mid m\right).
```

**Step 1.** The Jacobi identity for the cosine amplitude is

```math
\frac{d^2}{dz^2}\mathrm{cn}(z\mid m)=(2m-1)\mathrm{cn}(z\mid m)-2m\mathrm{cn}^3(z\mid m).
```

**Step 2.** The scale $`k=r/\sqrt{2m-1}`$ and amplitude $`A^2=m/(\mu(2m-1))`$ satisfy $`k^2(2m-1)=r^2`$ and $`2mk^2/A^2=2\mu r^2`$. Hence the Master equation holds exactly.

**Step 3.** At the positive turning point, energy and period are

```math
\varepsilon_{\mathrm{cn}}(m)=\frac{r^2}{\mu}\frac{m(1-m)}{(2m-1)^2}>0,\qquad T_{\mathrm{cn}}(m)=\frac{4\sqrt{2m-1}}{r}K(m).
```

The $`\mathrm{cn}`$ orbit crosses zero and changes sign. When $`m\uparrow1`$, the period diverges and the profile approaches the positive $`\mathrm{sech}`$ separatrix locally about its maximum. As $`m\downarrow1/2`$, the energy diverges.

## Exhaustion by energy type for bounded real trajectories

For the quartic potential $`\mu r^2(y^2-1/(2\mu))^2-r^2/(4\mu)`$, every real classical solution has $`\varepsilon\ge-r^2/(4\mu)`$ and remains bounded for finite energy.

- $`\varepsilon=-r^2/(4\mu)`$: the two nonzero constant equilibria.
- $`-r^2/(4\mu)<\varepsilon<0`$: periodic non-sign-changing orbits, represented by $`\pm\mathrm{dn}`$ after translation.
- $`\varepsilon=0`$: the zero equilibrium and the translated positive or negative $`\mathrm{sech}`$ separatrices.
- $`\varepsilon>0`$: periodic sign-changing orbits, represented by the $`\mathrm{cn}`$ family after translation.

The $`\mathrm{dn}`$ and $`\mathrm{cn}`$ parametrizations are standard Jacobi-elliptic solutions of a classical Duffing equation. Their place in the Symmetrical Framework is the **exact energy-level classification**; no novel integrability theorem is being claimed.
