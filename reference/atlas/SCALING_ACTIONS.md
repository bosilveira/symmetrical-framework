# Three Different Scale Actions: Coordinates, Resolution and Gram Boost

**Status:** exact algebraic transport identities derived from the kernel and the exponential envelope. They implement the distinct scale weights in Appendix C of the 16 November Complete Reference; all three transformations are explicitly typed in [contracts.json](contracts.json).

We distinguish a transformed quantity by the subscript $`_{new}`$ rather than by a prime, since a prime in this project normally denotes a derivative.

## 1. Simultaneous spatial dilation (SF-M-017)

For $`\lambda>0`$, define

```math
x_{\mathrm{new}}=\lambda x,\qquad c_{\mathrm{new}}=\lambda c,\qquad r_{\mathrm{new}}=r.
```

**Step 1.** The canonical log-coordinate does not change:

```math
u_{\mathrm{new}}=\log\frac{x_{\mathrm{new}}}{c_{\mathrm{new}}}=\log\frac{x}{c}=u.
```

**Step 2.** The original kernel has spatial density weight $`-1`$:

```math
f(x_{\mathrm{new}};r,c_{\mathrm{new}})=\lambda^{-1}f(x;r,c).
```

**Step 3.** Since $`dx_{\mathrm{new}}=\lambda\,dx`$, the positive measure and the normalized probability measure are preserved:

```math
f(x_{\mathrm{new}};r,c_{\mathrm{new}})\,dx_{\mathrm{new}}=f(x;r,c)\,dx,\qquad \rho_{\mathrm{new}}\,dx_{\mathrm{new}}=\rho\,dx.
```

Here the shape parameter $`r`$, argument $`\theta=ru`$, and centered hyperbolic functions $`S,W`$ are unchanged. The scale $`c`$ is transformed, not silently held fixed.

## 2. Resolution transport (SF-M-016)

Let $`s>0`$ be a **transformation parameter**, not the Mellin variable. Define

```math
u_{\mathrm{new}}=\frac{u}{s},\qquad r_{\mathrm{new}}=sr,\qquad c_{\mathrm{new}}=c.
```

**Step 1.** The oscillator argument is invariant:

```math
\theta_{\mathrm{new}}=r_{\mathrm{new}}u_{\mathrm{new}}=ru=\theta.
```

**Step 2.** To keep the defining coordinate relation consistent, $`x`$ must undergo the nonlinear transformation

```math
x_{\mathrm{new}}=c\left(\frac{x}{c}\right)^{1/s},\qquad \frac{dx_{\mathrm{new}}}{dx}=\frac{x_{\mathrm{new}}}{sx}.
```

**Step 3.** Since the hyperbolic shape is unchanged but the spatial weight $`1/(2x)`$ is not,

```math
f(x_{\mathrm{new}};sr,c)=\frac{x}{x_{\mathrm{new}}}f(x;r,c),\qquad f(x_{\mathrm{new}};sr,c)\,dx_{\mathrm{new}}=\frac1s f(x;r,c)\,dx.
```

**Step 4.** The normalized density absorbs the factor $`s`$:

```math
\rho(x_{\mathrm{new}};sr,c)\,dx_{\mathrm{new}}=\rho(x;r,c)\,dx.
```

**Step 5.** The same transport acts on *every* $`C^2`$ cubic Master solution $`y`$, not only the selected kernel. Define $`y_{\mathrm{new}}(u_{\mathrm{new}})=y(su_{\mathrm{new}})`$ with unchanged coupling $`\mu`$. Then

```math
\frac{d^2y_{\mathrm{new}}}{du_{\mathrm{new}}^2}=r_{\mathrm{new}}^2y_{\mathrm{new}}-2\mu r_{\mathrm{new}}^2y_{\mathrm{new}}^3,\qquad \varepsilon_{\mathrm{new}}=s^2\varepsilon.
```

In particular, the **dimensionless energy** is invariant:

```math
e_{\mathrm{new}}=\frac{\mu\varepsilon_{\mathrm{new}}}{r_{\mathrm{new}}^2}=\frac{\mu\varepsilon}{r^2}=e.
```

This action is *not* a simultaneous dilation of $`(x,c)`$ and does not leave the unnormalized $`f\,dx`$ invariant. It is a different symmetry of the dimensionless dynamical description.

## 3. Restricted diagonal Gram boost (SF-M-018)

For a real logarithmic shift $`\delta`$, keep $`r,c,C`$ fixed and transport the exponential coefficients by

```math
A_{\mathrm{new}}=Ae^{r\delta},\qquad B_{\mathrm{new}}=Be^{-r\delta},\qquad C_{\mathrm{new}}=C.
```

**Step 1.** As functions of the *same coordinate* $`u`$,

```math
J_{G,\mathrm{new}}(u)=J_G(u+\delta).
```

**Step 2.** Both the restricted product $`\mu_0=4AB`$ and full determinant $`\Delta_G=AB-C^2`$ remain invariant, as does $`\chi=C/\sqrt{AB}`$. The Gram shape transforms, however:

```math
\tau_{G,\mathrm{new}}=e^{-r\delta}\tau_G,\qquad u_{0,\mathrm{new}}=u_0-\delta,\qquad c_{\mathrm{eff,new}}=c_{\mathrm{eff}}e^{-\delta}.
```

The transformation retains the Gram cross coefficient $`C`$ and is therefore **only a one-parameter subgroup**, not an arbitrary $`SL(2,\mathbb R)`$ congruence. General determinant-one congruences preserve $`\Delta_G`$ but need not preserve the product $`AB`$.

## 4. Why the distinction matters

The three actions are not interchangeable:

| Action | What changes | What remains | Measure/energy |
|---|---|---|---|
| Simultaneous dilation | $`x,c`$ | $`u,r,\theta`$ | $`f\,dx`$ invariant |
| Resolution transport | $`u,r,x`$ nonlinearly; $`c`$ fixed | $`\theta,\mu,e`$ | $`f\,dx`$ scales by $`1/s`$; normalized $`\rho\,dx`$ invariant; $`\varepsilon`$ scales by $`s^2`$ |
| Gram boost | $`A,B`$, effective center | $`r,c,C,AB,\Delta_G,\chi`$ | Gram shape scales as $`\tau_G\mapsto e^{-r\delta}\tau_G`$ |

A recursive review of any identity involving $`r`$, $`c`$, $`\varepsilon`$, $`\mu`$, or the Gram coefficients must identify which action, if any, is being applied. An operator scaling rule is an additional statement and must have its own differential/Jacobian check.
