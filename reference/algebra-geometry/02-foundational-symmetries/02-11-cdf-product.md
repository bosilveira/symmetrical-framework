# 2.11 — Global CDF group law induced by multiplication

Define $`\mathcal F(u)=F(ce^u)=2\arctan(e^{ru})/\pi`$ and the bijection

```math
\Theta(v)=\tan\left(\frac{\pi v}{2}\right):(0,1)\longrightarrow(0,\infty).
```

Then $`\Theta(\mathcal F(u))=e^{ru}`$. Thus **[E]**

```math
\mathcal F(u_1+u_2) =\frac2\pi\arctan\bigl(\Theta(\mathcal F(u_1))\, \Theta(\mathcal F(u_2))\bigr).
```

**Abstract group structure.** On $`(0,1)`$ define

```math
v\odot w=\Theta^{-1}(\Theta(v)\Theta(w)).
```

This is an associative, commutative group, because $`\Theta`$ transports multiplication on $`(0,\infty)`$. Its identity is $`1/2`$ and its inverse is $`v\mapsto1-v`$:

```math
v\odot\tfrac12=v,\qquad v\odot(1-v)=\tfrac12.
```

The compatible operation in the $`x`$-coordinate is

```math
x_1\star_c x_2=\frac{x_1x_2}{c}.
```

Then $`F(x_1\star_c x_2)=F(x_1)\odot F(x_2)`$ and $`I_c(x)=c^2/x`$ is the group inverse.

The group isomorphism depends on the fixed parameters $`r,c`$ through $`F`$. It has nothing to do, by itself, with convolutions or the law of products of **independent** random variables.

## Three global charts for the same multiplicative group

The variable $`x>0`$ with the operation $`x_1\star_c x_2=x_1x_2/c`$ is a commutative group. It becomes ordinary addition for $`u=\log(x/c)`$, and it becomes the $`\odot`$ operation on CDF values through the bijection $`F`$.

The conformal phase $`W(x)=\tanh(ru)`$ supplies another globally defined chart. The hyperbolic tangent addition formula yields

```math
W(x_1\star_c x_2)=\frac{W(x_1)+W(x_2)}{1+W(x_1)W(x_2)}.
```

The denominator is strictly positive because both phases lie in $`(-1,1)`$. Thus the interval $`(-1,1)`$ is a commutative group under $`w_1\diamond w_2=(w_1+w_2)/(1+w_1w_2)`$, with identity $`0`$ and inverse $`w\mapsto-w`$.

For the logistic coordinate $`P=(1+W)/2\in(0,1)`$, the odds ratio is $`P/(1-P)=e^{2ru}`$. Consequently its transported multiplication law is

```math
P_1\diamond_P P_2=\frac{P_1P_2}{P_1P_2+(1-P_1)(1-P_2)},\qquad \frac{P_1\diamond_P P_2}{1-(P_1\diamond_P P_2)}=\frac{P_1}{1-P_1}\frac{P_2}{1-P_2}.
```

The logistic group identity is $`1/2`$ and the inverse is $`P\mapsto1-P`$. The CDF group $`\odot`$ in the first part of this section has the **same abstract group structure** but is a *different coordinate formula*: $`P(x)`$ must not be identified with $`F(x)`$ (see Chapter 1).

## Why the two CDF operations differ

The partial angle-addition of [§2.10](02-10-cdf-addition.md) transports the operation $`\theta_1+\theta_2`$ within the principal quadrant. The global $`\odot`$ transports multiplication of $`\tan\theta`$ (equivalently addition of logarithmic coordinates). Their two algebraic expressions and domains differ. Neither is, by itself, the convolution formula for a sum or a product of statistically independent random variables.
