# 2.10 CDF Addition Formula

The cumulative distribution function (CDF) of the normalized density $\rho(x)$ satisfies a simple addition formula under multiplication of its arguments, analogous to the addition formulas for trigonometric functions.

Let $F(x) \equiv F_\rho(x; r, c)$. For any two points $x_1, x_2 > 0$:

$$
\boxed{ F\left(\frac{x_1 x_2}{c}\right) = F(x_1) + F(x_2) - \frac{\pi}{2} F(x_1)F(x_2) }
$$

The canonical variable is $u=\log(x/c)$. $F(x)$ in terms of $u$ is $F(e^u) = \frac{2}{\pi}\arctan(e^{ru})$. Let $u_1=\log(x_1/c)$ and $u_2=\log(x_2/c)$. Then $\log(\frac{x_1x_2}{c^2}) = u_1+u_2$. Let's call the function of $u$, $\mathcal{F}(u) = F(ce^u)$.

$$
\mathcal{F}(u_1+u_2) = \frac{2}{\pi}\arctan(e^{r(u_1+u_2)}) = \frac{2}{\pi}\arctan(e^{ru_1}e^{ru_2}).
$$

This is the **tangent addition formula**. Let $T_1 = \tan(\frac{\pi}{2}\mathcal{F}(u_1)) = e^{ru_1}$ and $T_2 = \tan(\frac{\pi}{2}\mathcal{F}(u_2)) = e^{ru_2}$.
Then $\mathcal{F}(u_1+u_2) = \frac{2}{\pi}\arctan(T_1 T_2)$.
