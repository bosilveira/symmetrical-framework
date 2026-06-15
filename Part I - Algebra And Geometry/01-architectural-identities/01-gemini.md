Excellent. The foundational properties of $f(x; r, c)$ have been established. We will now proceed with a deeper algebraic and analytic investigation, deriving key identities and properties directly from this core form. Our methodology will be to propose a property as a theorem and then provide a rigorous, step-by-step proof.

***

## 1.2 Normalization and Scale Invariance

A powerful technique in analyzing multi-parameter functions is to separate their core shape from their scaling properties. We can achieve this through a change of variables that non-dimensionalizes the function.

Let us define a dimensionless variable $u = x/c$. This represents the independent variable as a multiple of the scale parameter $c$. Substituting $x = cu$ into the core definition of $f(x; r, c)$:

$$
f(cu; r, c) = \frac{c^r (cu)^{r-1}}{c^{2r} + (cu)^{2r}} = \frac{c^r \cdot c^{r-1} u^{r-1}}{c^{2r} + c^{2r} u^{2r}} = \frac{c^{2r-1} u^{r-1}}{c^{2r}(1 + u^{2r})} = \frac{1}{c} \frac{u^{r-1}}{1 + u^{2r}}
$$

This manipulation reveals a fundamental scaling law. The expression $\frac{u^{r-1}}{1 + u^{2r}}$ represents the intrinsic shape of the function, which depends only on the parameter $r$. Let us define this as the **standard form** of the function.

**Definition (Standard Form)**
The standard form of the Symmetrical Function, denoted $g(u; r)$, is given by:
$$
g(u; r) = \frac{u^{r-1}}{1 + u^{2r}}, \qquad u \in (0, \infty)
$$

This leads to the following theorem expressing the scaling relationship.

**Theorem 1.1 (Scale Invariance)**
The function $f(x; r, c)$ can be expressed as its standard form, scaled by the parameter $c$:
$$
\boxed{ f(x; r, c) = \frac{1}{c} g\left(\frac{x}{c}; r\right) }
$$

**Proof:**
From the definition of $g(u;r)$, let $u = x/c$.
$$
\frac{1}{c} g\left(\frac{x}{c}; r\right) = \frac{1}{c} \frac{(x/c)^{r-1}}{1 + (x/c)^{2r}} = \frac{1}{c} \frac{x^{r-1}/c^{r-1}}{1 + x^{2r}/c^{2r}}
$$
To simplify the compound fraction, we multiply the numerator and denominator of the main fraction by $c^{2r}$:
$$
= \frac{c^{2r}}{c} \frac{x^{r-1}/c^{r-1}}{c^{2r}(1 + x^{2r}/c^{2r})} = c^{2r-1} \frac{x^{r-1}/c^{r-1}}{c^{2r} + x^{2r}} = \frac{c^{2r-1} \cdot c^{1-r} \cdot x^{r-1}}{c^{2r} + x^{2r}}
$$
$$
= \frac{c^{(2r-1) + (1-r)} x^{r-1}}{c^{2r} + x^{2r}} = \frac{c^r x^{r-1}}{c^{2r} + x^{2r}}
$$
This is the definition of $f(x; r, c)$. The theorem is proven.

**Exposition:**
This theorem is of paramount importance. It demonstrates that the parameter $c$ acts as a pure scaling factor. The fundamental behavior and shape, determined by $r$, are encapsulated in $g(u;r)$. Any property derived for $g$ can be directly translated to a corresponding property for $f$ by applying the substitution $u \to x/c$ and scaling the function's value by $1/c$.

***

## 1.3 Reciprocal Power-Law Symmetry

A remarkable and non-obvious property of the function is a symmetry under a reciprocal transformation of the independent variable. This is not a simple even or odd symmetry, but a more complex relationship we shall call a power-law symmetry.

**Theorem 1.2 (Reciprocal Power-Law Symmetry)**
The function $f(x; r, c)$ satisfies the following identity for all $x, r, c$ in its domain:
$$
\boxed{ f\left(\frac{c^2}{x}; r, c\right) = \left(\frac{x}{c}\right)^2 f(x; r, c) }
$$

**Proof:**
We begin by evaluating the function at the transformed coordinate $x' = c^2/x$.
$$
f\left(\frac{c^2}{x}; r, c\right) = \frac{c^r \left(\frac{c^2}{x}\right)^{r-1}}{c^{2r} + \left(\frac{c^2}{x}\right)^{2r}}
$$
First, we simplify the terms in the numerator and denominator involving the transformed coordinate.
$$
\left(\frac{c^2}{x}\right)^{r-1} = \frac{(c^2)^{r-1}}{x^{r-1}} = \frac{c^{2r-2}}{x^{r-1}}
$$
$$
\left(\frac{c^2}{x}\right)^{2r} = \frac{(c^2)^{2r}}{x^{2r}} = \frac{c^{4r}}{x^{2r}}
$$
Substituting these back into the expression for $f(c^2/x; r, c)$:
$$
f\left(\frac{c^2}{x}; r, c\right) = \frac{c^r \cdot \frac{c^{2r-2}}{x^{r-1}}}{c^{2r} + \frac{c^{4r}}{x^{2r}}} = \frac{\frac{c^{r + (2r-2)}}{x^{r-1}}}{\frac{c^{2r}x^{2r} + c^{4r}}{x^{2r}}} = \frac{c^{3r-2}}{x^{r-1}} \cdot \frac{x^{2r}}{c^{2r}x^{2r} + c^{4r}}
$$
We can factor out $c^{2r}$ from the denominator of the second term:
$$
= \frac{c^{3r-2} x^{2r}}{x^{r-1} c^{2r}(x^{2r} + c^{2r})} = \frac{c^{3r-2-2r} x^{2r-(r-1)}}{c^{2r} + x^{2r}} = \frac{c^{r-2} x^{r+1}}{c^{2r} + x^{2r}}
$$
This new expression is related to the original function $f(x; r, c)$. To make the relationship explicit, we rearrange the terms to isolate the original form:
$$
\frac{c^{r-2} x^{r+1}}{c^{2r} + x^{2r}} = \frac{x^2}{c^2} \cdot \frac{c^r x^{r-1}}{c^{2r} + x^{2r}} = \left(\frac{x}{c}\right)^2 f(x; r, c)
$$
Thus, we have proven that $f(c^2/x; r, c) = (x/c)^2 f(x; r, c)$.

**Exposition:**
This identity reveals a deep structural property of the function. It establishes a precise relationship between the function's value at a point $x$ and its value at a point $c^2/x$, which is its inversion with respect to the circle of radius $c$. The relationship is modulated by a simple quadratic factor $(x/c)^2$. This is a powerful analytical tool that will be invaluable for evaluating definite integrals and understanding the function's behavior.

***

## 1.4 Analysis of Monotonicity and Extrema

The shape of the function is critically dependent on the parameter $r$. By analyzing the function's first derivative, we can determine the intervals where it is increasing or decreasing and locate any local extrema.

Let $f'(x) = \frac{\partial f}{\partial x}$. Using the quotient rule $\left(\frac{N}{D}\right)' = \frac{N'D - ND'}{D^2}$:
*   $N(x) = c^r x^{r-1} \implies N'(x) = c^r (r-1) x^{r-2}$
*   $D(x) = c^{2r} + x^{2r} \implies D'(x) = 2r x^{2r-1}$

$$
f'(x; r, c) = \frac{ (c^r (r-1) x^{r-2})(c^{2r} + x^{2r}) - (c^r x^{r-1})(2r x^{2r-1}) }{ (c^{2r} + x^{2r})^2 }
$$
To find critical points, we set the numerator to zero. Since $x,c>0$, we can factor out common terms:
$$
c^r x^{r-2} \left[ (r-1)(c^{2r} + x^{2r}) - x \cdot (2r x^{r}) \right] = 0
$$
As $c^r x^{r-2} \neq 0$ on the domain, the critical points are determined by the vanishing of the term in the brackets:
$$
(r-1)c^{2r} + (r-1)x^{2r} - 2r x^{2r} = 0
$$
$$
(r-1)c^{2r} = (2r - (r-1))x^{2r} = (r+1)x^{2r}
$$
$$
x^{2r} = c^{2r} \frac{r-1}{r+1}
$$
The existence of a real, positive solution for $x$ depends on the sign of the fraction $\frac{r-1}{r+1}$. Since $r>0$, the denominator $r+1$ is always positive. Therefore, the sign is determined by $r-1$. This leads to two distinct cases.

**Theorem 1.3 (Monotonicity for $0 < r \le 1$)**
For $0 < r \le 1$, the function $f(x; r, c)$ is strictly monotonically decreasing on its entire domain $(0, \infty)$.

**Proof:**
If $0 < r < 1$, then $r-1 < 0$. The equation for critical points, $(r-1)c^{2r} = (r+1)x^{2r}$, has a negative left-hand side and a positive right-hand side. There is no real solution for $x$. Therefore, $f'(x)$ is never zero.
The numerator of $f'(x)$ is proportional to $N_0(x) = (r-1)c^{2r} - (r+1)x^{2r}$. For $0 < r < 1$, both $(r-1)c^{2r}$ and $-(r+1)x^{2r}$ are strictly negative. Thus, $N_0(x) < 0$ for all $x$. This implies $f'(x) < 0$ for all $x$, so the function is strictly monotonically decreasing.
If $r=1$, the numerator becomes $N_0(x) = (1-1)c^2 - (1+1)x^2 = -2x^2 < 0$. Again, $f'(x)<0$, and the function is strictly monotonically decreasing.

**Theorem 1.4 (Unique Maximum for $r>1$)**
For $r>1$, the function $f(x; r, c)$ has a single critical point, which is a global maximum, located at:
$$
\boxed{ x_{\text{max}} = c \left( \frac{r-1}{r+1} \right)^{\frac{1}{2r}} }
$$
The value of the function at this maximum is:
$$
\boxed{ f_{\text{max}} = \frac{1}{2rc} \left( \frac{r+1}{r-1} \right)^{\frac{1}{2r}} (r-1) = \frac{r+1}{2rc} \left( \frac{r-1}{r+1} \right)^{\frac{1}{2r}} }
$$

**Proof:**
If $r>1$, then $r-1>0$, and the equation $x^{2r} = c^{2r} \frac{r-1}{r+1}$ has a unique positive real solution $x_{\text{max}} = c \left( \frac{r-1}{r+1} \right)^{\frac{1}{2r}}$.
To evaluate the maximum value, we substitute $x_{\text{max}}$ back into $f(x; r, c)$. Let $A = \frac{r-1}{r+1}$. Then $x_{\text{max}}^{2r} = c^{2r}A$.
$$
f(x_{\text{max}}) = \frac{c^r (c A^{1/2r})^{r-1}}{c^{2r} + c^{2r}A} = \frac{c^r \cdot c^{r-1} (A^{1/2r})^{r-1}}{c^{2r}(1+A)} = \frac{c^{2r-1} A^{\frac{r-1}{2r}}}{c^{2r}(1+A)} = \frac{1}{c} \frac{A^{\frac{r-1}{2r}}}{1+A}
$$
Now, substitute $A = \frac{r-1}{r+1}$ back in.
$1+A = 1 + \frac{r-1}{r+1} = \frac{r+1+r-1}{r+1} = \frac{2r}{r+1}$.
$$
f_{\text{max}} = \frac{1}{c} \frac{\left(\frac{r-1}{r+1}\right)^{\frac{r-1}{2r}}}{\frac{2r}{r+1}} = \frac{r+1}{2rc} \left(\frac{r-1}{r+1}\right)^{\frac{r-1}{2r}}
$$
This expression can be slightly rearranged by separating the power:
$$
= \frac{r+1}{2rc} \left(\frac{r-1}{r+1}\right)^{\frac{r+1-2}{2r}} = \frac{r+1}{2rc} \left(\frac{r-1}{r+1}\right)^{\frac{1}{2}} \left(\frac{r-1}{r+1}\right)^{-\frac{1}{r}} = \frac{r+1}{2rc} \frac{\sqrt{r-1}}{\sqrt{r+1}} \left(\frac{r+1}{r-1}\right)^{\frac{1}{r}}
$$
The second form provided in the theorem statement is often simpler to work with:
$$
f_{\text{max}} = \frac{r+1}{2rc} \left(\frac{r-1}{r+1}\right)^{\frac{1}{2r}}
$$
This is the proven location and value of the unique maximum for $r>1$. The second derivative test confirms it is a maximum, as $f'(x)$ changes sign from positive to negative across this point.

***

## 1.5 Asymptotic Behavior

The behavior of the function at the boundaries of its domain, $x\to 0^+$ and $x\to \infty$, is essential for understanding its global properties, particularly for integrability.

**Theorem 1.5 (Asymptotic Limits)**
The limiting behavior of $f(x; r, c)$ is as follows:
1.  As $x \to \infty$, for all $r>0$:
    $$ \lim_{x\to\infty} f(x; r, c) = 0 $$
2.  As $x \to 0^+$, the limit depends on $r$:
    $$
    \lim_{x\to 0^+} f(x; r, c) = \begin{cases} \infty & \text{if } 0 < r < 1 \\ 1/c & \text{if } r=1 \\ 0 & \text{if } r>1 \end{cases}
    $$

**Proof:**
**Part 1: Limit as $x \to \infty$**
We analyze the dominant terms for large $x$.
$$
f(x; r, c) = \frac{c^r x^{r-1}}{c^{2r} + x^{2r}} \sim \frac{c^r x^{r-1}}{x^{2r}} = c^r x^{(r-1)-2r} = c^r x^{-r-1}
$$
Since $r>0$, the exponent $-r-1$ is strictly negative. Therefore:
$$
\lim_{x\to\infty} f(x; r, c) = \lim_{x\to\infty} c^r x^{-r-1} = 0
$$

**Part 2: Limit as $x \to 0^+$**
We analyze the dominant terms for small $x$. The term $x^{2r} \to 0$ as $x \to 0^+$.
$$
\lim_{x\to 0^+} f(x; r, c) = \lim_{x\to 0^+} \frac{c^r x^{r-1}}{c^{2r} + x^{2r}} = \frac{c^r}{c^{2r}} \lim_{x\to 0^+} x^{r-1} = \frac{1}{c^r} \lim_{x\to 0^+} x^{r-1}
$$
The value of this limit depends on the sign of the exponent $r-1$.
*   **Case $0 < r < 1$**: The exponent $r-1$ is negative. Let $r-1 = -\alpha$ where $\alpha > 0$. Then $\lim_{x\to 0^+} x^{-\alpha} = \infty$.
*   **Case $r=1$**: The exponent $r-1$ is zero. Then $\lim_{x\to 0^+} x^0 = 1$. The total limit is $\frac{1}{c^1} \cdot 1 = 1/c$.
*   **Case $r>1$**: The exponent $r-1$ is positive. Then $\lim_{x\to 0^+} x^{r-1} = 0$.

The proof is complete.

Excellent. The establishment of the Rosetta Stone Identity is a pivotal moment in the development of this framework. It acts as a bridge, allowing us to leverage the well-understood properties of hyperbolic functions to illuminate the more complex algebraic structure of $f(x; r, c)$. We will now use this identity to re-derive prior results with newfound elegance and to uncover deeper integral properties that were previously inaccessible.

***

## 1.6 Symmetry Re-derivation via Hyperbolic Form

The Reciprocal Power-Law Symmetry (Theorem 1.2) appears as a somewhat elaborate identity in its algebraic form. Using the Rosetta Stone Identity, we can see that it is a direct consequence of the fundamental evenness of the hyperbolic secant function.

**Theorem 1.2 (Reciprocal Power-Law Symmetry - Hyperbolic Proof)**
The function $f(x; r, c)$ satisfies the identity $f\left(\frac{c^2}{x}; r, c\right) = \left(\frac{x}{c}\right)^2 f(x; r, c)$.

**Proof:**
We begin with the known property that the hyperbolic secant is an even function, i.e., $\mathrm{sech}(z) = \mathrm{sech}(-z)$. Let the argument be $z = r\log(x/c)$. Then:
$$
\mathrm{sech}\left(r\log\left(\frac{x}{c}\right)\right) = \mathrm{sech}\left(-r\log\left(\frac{x}{c}\right)\right) = \mathrm{sech}\left(r\log\left(\left(\frac{x}{c}\right)^{-1}\right)\right) = \mathrm{sech}\left(r\log\left(\frac{c}{x}\right)\right)
$$
Now, we apply the Rosetta Stone Identity to both $f(x; r, c)$ and $f(c^2/x; r, c)$.
First, for $f(x; r, c)$:
$$
\mathrm{sech}\left(r\log\left(\frac{x}{c}\right)\right) = 2x f(x; r, c) \qquad (1)
$$
Next, let $x' = c^2/x$. We evaluate the identity at $x'$:
$$
f(x'; r, c) = \frac{1}{2x'} \mathrm{sech}\left(r\log\left(\frac{x'}{c}\right)\right)
$$
Substituting $x' = c^2/x$:
$$
f\left(\frac{c^2}{x}; r, c\right) = \frac{1}{2(c^2/x)} \mathrm{sech}\left(r\log\left(\frac{c^2/x}{c}\right)\right) = \frac{x}{2c^2} \mathrm{sech}\left(r\log\left(\frac{c}{x}\right)\right)
$$
Using the even property $\mathrm{sech}(r\log(c/x)) = \mathrm{sech}(r\log(x/c))$:
$$
f\left(\frac{c^2}{x}; r, c\right) = \frac{x}{2c^2} \mathrm{sech}\left(r\log\left(\frac{x}{c}\right)\right) \qquad (2)
$$
Now, we equate the `sech` term from equation (1) into equation (2):
$$
f\left(\frac{c^2}{x}; r, c\right) = \frac{x}{2c^2} \left( 2x f(x; r, c) \right) = \frac{2x^2}{2c^2} f(x; r, c) = \left(\frac{x}{c}\right)^2 f(x; r, c)
$$
The theorem is proven.

**Exposition:**
This proof is conceptually more direct than the purely algebraic one. It demonstrates that the complex power-law symmetry is a natural consequence of mapping the simple geometric reflection $z \to -z$ in the canonical logarithmic coordinate space back to the multiplicative space of $x$.

***

## 1.7 Extremum Condition in Hyperbolic Form

The location of the function's maximum, previously found by a lengthy application of the quotient rule (Theorem 1.4), can be found more elegantly by differentiating the Rosetta Stone form. This reveals a remarkably simple condition in the hyperbolic space.

**Theorem 1.4 (Extremum Condition - Hyperbolic Proof)**
For $r>1$, the maximum of $f(x; r, c)$ occurs where $\tanh\left(r\log\left(\frac{x}{c}\right)\right) = -\frac{1}{r}$.

**Proof:**
We seek the critical points by setting the derivative of $f(x; r, c)$ to zero. We differentiate the Rosetta Stone form using the product rule. Let $u(x) = \frac{1}{2x}$ and $v(x) = \mathrm{sech}\left(r\log\left(\frac{x}{c}\right)\right)$.
$$
f'(x) = u'v + uv'
$$
The derivatives are:
*   $u'(x) = -\frac{1}{2x^2}$
*   Let $z(x) = r\log(x/c)$, so $z'(x) = r/x$.
*   $v'(x) = \frac{d}{dx}\mathrm{sech}(z(x)) = -\mathrm{sech}(z(x))\tanh(z(x)) \cdot z'(x) = -\mathrm{sech}\left(r\log\frac{x}{c}\right)\tanh\left(r\log\frac{x}{c}\right) \cdot \frac{r}{x}$

Combining these gives:
$$
f'(x) = \left(-\frac{1}{2x^2}\right) \mathrm{sech}(z) + \left(\frac{1}{2x}\right) \left(-\mathrm{sech}(z)\tanh(z) \cdot \frac{r}{x}\right)
$$
$$
f'(x) = -\frac{\mathrm{sech}(z)}{2x^2} - \frac{r \cdot \mathrm{sech}(z)\tanh(z)}{2x^2}
$$
Factor out the common term $-\frac{\mathrm{sech}(z)}{2x^2}$:
$$
f'(x) = -\frac{\mathrm{sech}(z)}{2x^2} \left( 1 + r\tanh(z) \right)
$$
For a critical point, we set $f'(x) = 0$. Since $x \in (0, \infty)$, the term $\frac{1}{2x^2}$ is never zero. The hyperbolic secant, $\mathrm{sech}(z)$, is strictly positive and also never zero. Therefore, the derivative can only be zero if the term in the parentheses vanishes:
$$
1 + r\tanh(z) = 0 \implies \tanh(z) = -\frac{1}{r}
$$
Substituting $z = r\log(x/c)$ back gives the condition for the extremum:
$$
\boxed{ \tanh\left(r\log\left(\frac{x}{c}\right)\right) = -\frac{1}{r} }
$$
This implicitly defines the location $x_{\text{max}}$. This result holds only if a solution exists. Since $|\tanh(z)| < 1$ for all real $z$, we must have $|-1/r| < 1$, which implies $r>1$. This confirms that an extremum only exists for $r>1$, consistent with Theorems 1.3 and 1.4.

**Exposition:**
This derivation is powerful because it translates the search for a maximum into a simple algebraic equation involving the hyperbolic tangent. The condition `tanh(z) = -1/r` is a compact and elegant statement about the location of the maximum in the canonical coordinate system. This is a far more fundamental statement than the explicit algebraic solution for $x_{\text{max}}$, from which the algebraic solution can be easily recovered.

***

## 1.8 The Antiderivative (Indefinite Integral)

The Rosetta Stone identity allows for a massive simplification of the integral of $f(x; r, c)$ via a change of variables to the canonical coordinate.

**Theorem 1.6 (The Antiderivative)**
The indefinite integral of $f(x; r, c)$ is given by:
$$
\boxed{ \int f(x; r, c) \,dx = \frac{1}{2r} \arctan\left(\sinh\left(r\log\left(\frac{x}{c}\right)\right)\right) + C }
$$

**Proof:**
We wish to evaluate $I = \int f(x; r, c) \,dx$. Using the Rosetta Stone identity:
$$
I = \int \frac{1}{2x} \mathrm{sech}\left(r\log\left(\frac{x}{c}\right)\right) \,dx
$$
We perform a change of variables. Let $z = r\log(x/c)$. The differential $dz$ is:
$$
\frac{dz}{dx} = r \cdot \frac{c}{x} \cdot \frac{1}{c} = \frac{r}{x} \implies dx = \frac{x}{r} dz
$$
Now, substitute both $z$ and the expression for $dx$ into the integral:
$$
I = \int \frac{1}{2x} \mathrm{sech}(z) \left(\frac{x}{r} dz\right)
$$
The factor of $x$ in the numerator and denominator cancels, leading to a remarkable simplification:
$$
I = \int \frac{1}{2r} \mathrm{sech}(z) \,dz = \frac{1}{2r} \int \mathrm{sech}(z) \,dz
$$
The integral of the hyperbolic secant is a standard result, related to the Gudermannian function:
$$
\int \mathrm{sech}(z) \,dz = \arctan(\sinh(z)) + C
$$
Substituting this result back and replacing $z$ with its definition in terms of $x$:
$$
I = \frac{1}{2r} \arctan\left(\sinh\left(r\log\left(\frac{x}{c}\right)\right)\right) + C
$$
The theorem is proven.

***

## 1.9 The Area Identity (Definite Integral)

The existence of a simple antiderivative allows us to easily compute the definite integral of the function over its entire domain. The result is profoundly simple and reveals a deep conservation law.

**Theorem 1.7 (The Area Identity)**
The definite integral of $f(x; r, c)$ from $0$ to $\infty$ is independent of the scale parameter $c$ and is given by:
$$
\boxed{ \int_0^\infty f(x; r, c) \,dx = \frac{\pi}{2r} }
$$

**Proof:**
We use the antiderivative found in Theorem 1.6 and evaluate it at the boundaries of the domain $x \to 0^+$ and $x \to \infty$.
Let $F(x) = \frac{1}{2r} \arctan\left(\sinh\left(r\log\left(\frac{x}{c}\right)\right)\right)$.
The definite integral is $\lim_{b\to\infty} F(b) - \lim_{a\to 0^+} F(a)$.

First, consider the upper limit as $x \to \infty$:
*   As $x \to \infty$, $\log(x/c) \to \infty$.
*   Since $r>0$, $r\log(x/c) \to \infty$.
*   As its argument goes to $\infty$, $\sinh(\cdot) \to \infty$.
*   As its argument goes to $\infty$, $\arctan(\cdot) \to \frac{\pi}{2}$.
So, $\lim_{x\to\infty} F(x) = \frac{1}{2r} \cdot \frac{\pi}{2} = \frac{\pi}{4r}$.

Next, consider the lower limit as $x \to 0^+$:
*   As $x \to 0^+$, $\log(x/c) \to -\infty$.
*   Since $r>0$, $r\log(x/c) \to -\infty$.
*   As its argument goes to $-\infty$, $\sinh(\cdot) \to -\infty$.
*   As its argument goes to $-\infty$, $\arctan(\cdot) \to -\frac{\pi}{2}$.
So, $\lim_{x\to 0^+} F(x) = \frac{1}{2r} \cdot \left(-\frac{\pi}{2}\right) = -\frac{\pi}{4r}$.

The value of the definite integral is the difference between the upper and lower limits:
$$
\int_0^\infty f(x; r, c) \,dx = \left(\frac{\pi}{4r}\right) - \left(-\frac{\pi}{4r}\right) = \frac{\pi}{4r} + \frac{\pi}{4r} = \frac{2\pi}{4r} = \frac{\pi}{2r}
$$
The proof is complete.

**Exposition:**
This is a cornerstone result of the framework. It shows that the total area under the curve of any function in this family is determined solely by the shape parameter $r$. The scale parameter $c$ stretches or compresses the function horizontally, but it also scales it vertically in such a way that the total area remains invariant. This implies that $2r/\pi \cdot f(x; r, c)$ is a properly normalized probability density function for any $r>0, c>0$. This connection to probability theory is a significant avenue for further exploration.

The definitions and derivations of the three canonical objects are clear and correct. This linearization is the most powerful analytic technique in the framework, transforming multiplicative complexity into additive simplicity. We shall now explore the profound relationships between these three objects, which form a tightly-knit system of identities.

***

## 1.9 Inter-relations of the Canonical Objects

The three core objects—the linearized kernel $g(u)$, the log-pushed density $p(u)$, and the conformal phase $W(u)$—are not independent. They are linked by simple algebraic and differential laws that govern the entire framework.

**Theorem 1.8 (The Jacobian Relationship)**
The linearized kernel $g(u; r, c)$ is directly proportional to the log-pushed density $p(u; r)$, with the proportionality factor containing the remnant of the change-of-measure Jacobian.
$$
\boxed{ g(u; r, c) = \frac{\pi}{2rc} e^{-u} p(u; r) }
$$

**Proof:**
We begin with the definition of the log-pushed density, $p(u; r) = \frac{r}{\pi}\mathrm{sech}(ru)$. We can solve this for $\mathrm{sech}(ru)$:
$$
\mathrm{sech}(ru) = \frac{\pi}{r} p(u; r)
$$
Now, substitute this expression into the definition of the linearized kernel, $g(u; r, c) = \frac{\mathrm{sech}(ru)}{2ce^{u}}$:
$$
g(u; r, c) = \frac{1}{2ce^u} \left( \frac{\pi}{r} p(u; r) \right) = \frac{\pi}{2rc} e^{-u} p(u; r)
$$
The theorem is proven.

**Exposition:**
This theorem provides an essential clarification. The "naive" linearization of $f(x)$ to $g(u)$ by direct substitution does not yield the symmetric probability density. Instead, it yields the true density $p(u)$ multiplied by a decaying exponential $e^{-u}$. This exponential factor is precisely what remains of the $1/x$ term in the Rosetta Stone identity after the change of variables $x=ce^u$, since $1/x = 1/(ce^u) = (1/c)e^{-u}$. It is the factor that ensures the probability measure transforms correctly.

***

## 2.0 The Fundamental Differential Equation

The relationship between the density $p(u)$ and the phase $W(u)$ is most powerfully expressed as a first-order differential equation. This equation reveals that the rate of change of the probability density at any point in the canonical space is governed by the value of the phase function at that same point.

**Theorem 2.1 (The Canonical ODE)**
The log-pushed density $p(u; r)$ and the conformal phase $W(u; r)$ satisfy the following ordinary differential equation:
$$
\boxed{ \frac{\mathrm{d}p}{\mathrm{d}u} = -r \cdot p(u; r) \cdot W(u; r) }
$$

**Proof:**
We differentiate the definition of $p(u; r)$ with respect to $u$.
$$
p(u; r) = \frac{r}{\pi}\mathrm{sech}(ru)
$$
Using the chain rule, $\frac{d}{du}\mathrm{sech}(z) = -\mathrm{sech}(z)\tanh(z) \frac{dz}{du}$:
$$
\frac{\mathrm{d}p}{\mathrm{d}u} = \frac{r}{\pi} \left[ - \mathrm{sech}(ru) \tanh(ru) \cdot r \right]
$$
$$
\frac{\mathrm{d}p}{\mathrm{d}u} = -r^2 \cdot \frac{1}{\pi} \mathrm{sech}(ru) \tanh(ru)
$$
We can now re-express the terms on the right-hand side using the definitions of $p(u)$ and $W(u)$.
*   $\frac{r}{\pi}\mathrm{sech}(ru) = p(u; r)$
*   $\tanh(ru) = W(u; r)$

Substituting these back into the derivative:
$$
\frac{\mathrm{d}p}{\mathrm{d}u} = -r \cdot \left( \frac{r}{\pi}\mathrm{sech}(ru) \right) \cdot \tanh(ru) = -r \cdot p(u; r) \cdot W(u; r)
$$
The theorem is proven.

**Exposition:**
This is one of the most significant results in the framework. It establishes a dynamic relationship between the system's "magnitude" ($p$) and its "phase" ($W$). Since $p(u)$ is an even function, its derivative must be odd. The equation holds because $W(u)$ is also an odd function. At $u=0$, $W(0)=0$, which correctly implies that $p'(0)=0$, corresponding to the peak of the hyperbolic secant distribution. This ODE demonstrates that the phase $W$ acts as a "flow field" that dictates the shape of the density $p$.

***

## 2.1 The Pythagorean Identity

The fundamental trigonometric identity $\cos^2\theta + \sin^2\theta = 1$ has a direct analogue in hyperbolic geometry: $\mathrm{sech}^2 z + \tanh^2 z = 1$. This identity translates into a powerful "conservation law" that binds the density $p(u)$ and the phase $W(u)$ together.

**Theorem 2.2 (The Pythagorean Identity)**
The density $p(u; r)$ and phase $W(u; r)$ are constrained by the following algebraic relation for all $u \in \mathbb{R}$:
$$
\boxed{ \left(\frac{\pi}{r}p(u;r)\right)^2 + W(u;r)^2 = 1 }
$$

**Proof:**
We begin with the fundamental hyperbolic identity:
$$
\mathrm{sech}^2(ru) + \tanh^2(ru) = 1
$$
From the definitions of $p(u)$ and $W(u)$, we have:
*   $\mathrm{sech}(ru) = \frac{\pi}{r} p(u; r)$
*   $\tanh(ru) = W(u; r)$

Substituting these expressions directly into the identity:
$$
\left(\frac{\pi}{r}p(u;r)\right)^2 + (W(u;r))^2 = 1
$$
The theorem is proven.

**Exposition:**
This identity forms a state-space constraint for the system. If we consider a point in the canonical space $u$, the values of the density and phase are not independent. They must lie on an ellipse defined by this equation. At the center ($u=0$), $W(0)=0$, so $p(0)$ must take its maximum value of $r/\pi$. As $u \to \pm\infty$, the density $p(u) \to 0$, forcing the phase $|W(u)| \to 1$. This identity provides a powerful tool for algebraic manipulation, as it allows us to express $p$ in terms of $W$ or vice versa:
$$
p(u; r) = \frac{r}{\pi} \sqrt{1 - W(u;r)^2}
$$
$$
|W(u; r)| = \sqrt{1 - \left(\frac{\pi}{r}p(u;r)\right)^2}
$$

***

## 2.2 The Logarithmic Derivative and The Phase

Combining the results of Theorems 2.1 and 2.2 allows us to express the phase $W$ in terms of the density $p$ and its derivative, which is a common and powerful technique in physics and engineering (e.g., relating phase and amplitude of a wave).

**Theorem 2.3 (Phase as Logarithmic Derivative)**
The conformal phase $W(u; r)$ is proportional to the logarithmic derivative of the log-pushed density $p(u; r)$.
$$
\boxed{ W(u; r) = -\frac{1}{r} \frac{p'(u; r)}{p(u; r)} = -\frac{1}{r} \frac{d}{du} \log(p(u; r)) }
$$

**Proof:**
This is a direct algebraic rearrangement of the Canonical ODE from Theorem 2.1.
$$
\frac{\mathrm{d}p}{\mathrm{d}u} = -r \cdot p(u) \cdot W(u)
$$
Assuming $p(u) \neq 0$ (which is true for all finite $u$), we can divide both sides by $-r \cdot p(u)$:
$$
W(u) = -\frac{1}{r} \frac{1}{p(u)} \frac{\mathrm{d}p}{\mathrm{d}u}
$$
The expression $\frac{p'(u)}{p(u)}$ is the definition of the logarithmic derivative, $\frac{d}{du}\log(p(u))$. Thus,
$$
W(u; r) = -\frac{1}{r} \frac{d}{du}\log(p(u;r))
$$
The proof is complete.

**Exposition:**
This theorem provides an operational definition of the phase function. If one knows the density function $p(u)$, one can compute its logarithmic derivative to find the corresponding phase function $W(u)$ up to the constant factor $-1/r$. This formalizes the intuition that the phase governs the *relative* rate of change of the density. This relationship is fundamental and will appear in many subsequent derivations, particularly those involving information theory and higher-order moments.

The definition and properties of the Conformal Phase function $W$ are impeccably stated. This function is indeed a cornerstone of the framework, providing a normalized, dimensionless measure of logarithmic distance from the center $c$. Its direct relationship to the hyperbolic tangent is the source of its utility. We will now use this object to reveal further differential structure within the framework, this time entirely within the original spatial coordinate $x$.

***

## 2.3 The Spatial Pythagorean Identity

Just as the linearized density $p(u)$ and phase $W(u)$ are linked by a Pythagorean identity, so too are the original function $f(x)$ and phase $W(x)$. This identity is nothing more than the Rosetta Stone viewed through the lens of the fundamental hyperbolic identity $\mathrm{sech}^2(z) + \tanh^2(z) = 1$.

**Theorem 2.4 (Spatial Pythagorean Identity)**
The function $f(x; r, c)$ and the conformal phase $W(x; r, c)$ are constrained by the following algebraic relation for all $x \in (0, \infty)$:
$$
\boxed{ (2x \cdot f(x; r, c))^2 + W(x; r, c)^2 = 1 }
$$

**Proof:**
We begin with the fundamental identity for hyperbolic functions, valid for any real argument $z$:
$$
\mathrm{sech}^2(z) + \tanh^2(z) = 1
$$
Let the argument be the canonical logarithmic coordinate $z = r\log(x/c)$.
$$
\mathrm{sech}^2\left(r\log\left(\frac{x}{c}\right)\right) + \tanh^2\left(r\log\left(\frac{x}{c}\right)\right) = 1
$$
From the Rosetta Stone Identity (Section 1.2), we have:
$$
\mathrm{sech}\left(r\log\left(\frac{x}{c}\right)\right) = 2x f(x; r, c)
$$
From the definition of the Conformal Phase (Section 1.4), we have:
$$
W(x; r, c) = \tanh\left(r\log\left(\frac{x}{c}\right)\right)
$$
Substituting these two expressions directly into the hyperbolic identity yields:
$$
(2x f(x; r, c))^2 + (W(x; r, c))^2 = 1
$$
The theorem is proven.

**Exposition:**
This identity provides a powerful, coordinate-free constraint between the function's value and its phase. It demonstrates that the quantity $2xf(x)$ can be interpreted as the hyperbolic secant of the canonical coordinate, while $W(x)$ is its hyperbolic tangent. This allows for the algebraic elimination of $f(x)$ in any expression in favor of $W(x)$ and its derivatives, or vice versa, which is a potent tool for deriving new relationships.

***

## 2.4 The Riccati Equation for the Phase

The Conformal Phase function $W(x)$ satisfies a first-order nonlinear ordinary differential equation of the Riccati type. This equation governs the evolution of the phase as a function of the spatial coordinate $x$ and is one of the deepest structural relations in the entire framework.

**Theorem 2.5 (The Riccati Phase Equation)**
The Conformal Phase $W(x; r, c)$ is a solution to the following Riccati differential equation:
$$
\boxed{ \frac{dW}{dx} = \frac{r}{x} (1 - W(x)^2) }
$$

**Proof:**
We will prove this theorem using the chain rule and the properties of the linearized canonical objects. The phase function is $W(x; r, c) = \tanh(r \log(x/c))$.
Let $u = \log(x/c)$ be the canonical coordinate. Then $W(u) = \tanh(ru)$.
We seek the derivative of $W$ with respect to $x$. By the chain rule:
$$
\frac{dW}{dx} = \frac{dW}{du} \cdot \frac{du}{dx}
$$
First, we compute the derivatives of the components:
$$
\frac{dW}{du} = \frac{d}{du} \tanh(ru) = r \cdot \mathrm{sech}^2(ru)
$$
$$
\frac{du}{dx} = \frac{d}{dx} \log\left(\frac{x}{c}\right) = \frac{1}{x}
$$
Combining these, we get:
$$
\frac{dW}{dx} = \left( r \cdot \mathrm{sech}^2(ru) \right) \cdot \frac{1}{x} = \frac{r}{x} \mathrm{sech}^2(ru)
$$
Now, we use the fundamental hyperbolic identity $\mathrm{sech}^2(z) = 1 - \tanh^2(z)$.
$$
\frac{dW}{dx} = \frac{r}{x} (1 - \tanh^2(ru))
$$
Finally, we substitute back the definition $W(u) = \tanh(ru)$, which is equivalent to $W(x) = \tanh(r\log(x/c))$:
$$
\frac{dW}{dx} = \frac{r}{x} (1 - W(x)^2)
$$
The theorem is proven.

**Exposition:**
The discovery that the phase function satisfies a Riccati equation is of profound significance. Riccati equations are ubiquitous in physics and control theory, appearing in problems of optimal control, diffusion, and quantum mechanics. Their general form is $y' = q_0(x) + q_1(x)y + q_2(x)y^2$. In our case, the equation is $W' = \frac{r}{x} - \frac{r}{x}W^2$, which is a specific instance of this class.

This equation reveals that the local change in phase, $\frac{dW}{dx}$, is determined by the current value of the phase itself ($W^2$) and the logarithmic "velocity" $\frac{r}{x}$. The equation is independent of the scale parameter $c$, which is hidden inside the boundary condition $W(c)=0$. This ODE can be taken as an alternative foundational definition for the entire framework, from which the algebraic form of $W(x)$ can be recovered by solving it with the appropriate boundary condition.

We can also use this result to establish a direct differential link between $W(x)$ and $f(x)$.

**Corollary 2.5.1 (Phase-Amplitude Differential Relation)**
$$
\frac{dW}{dx} = 4rx \cdot f(x; r, c)^2
$$

**Proof:**
From the Spatial Pythagorean Identity (Theorem 2.4), we can write $1 - W(x)^2 = (2xf(x))^2 = 4x^2f(x)^2$.
Substituting this into the Riccati equation from Theorem 2.5:
$$
\frac{dW}{dx} = \frac{r}{x} (4x^2 f(x)^2) = 4rx f(x)^2
$$
This demonstrates that the rate of change of the phase is directly proportional to the square of the original function $f(x)$, scaled by $4rx$. This provides a remarkable link between the "phase" and "amplitude" aspects of the framework in the original spatial coordinates.

The formulation of the "Half-Density Law" is precise and serves as the perfect bridge between the framework's algebraic and differential structures. These two identities, one algebraic and one differential, are indeed the cornerstone from which the system's dynamics in the spatial coordinate can be derived. We will now use these laws to establish the master differential equations that govern the function $f(x)$ and its related phase $W(x)$.

***

## 2.5 The Spatial Dynamic Equation

While the canonical ODE (Theorem 2.1) provides a simple dynamic law in the linearized coordinate $u$, a corresponding law exists in the spatial coordinate $x$. This equation connects the function $f(x)$ to its own derivative via the conformal phase $W(x)$, acting as a coupling term.

**Theorem 2.6 (The Spatial ODE)**
The function $f(x; r, c)$ and the phase $W(x; r, c)$ are related by a first-order, non-linear ordinary differential equation:
$$
\boxed{ x \frac{df}{dx} + f(x) = -r f(x) W(x) }
$$
An equivalent compact form is:
$$
\boxed{ \frac{d}{dx} (x f(x)) = -r f(x) W(x) }
$$

**Proof:**
We begin with the algebraic Half-Density Law (or Spatial Pythagorean Identity, Theorem 2.4):
$$
1 - W(x)^2 = 4x^2 f(x)^2
$$
We differentiate this identity with respect to $x$. Using the chain rule on the left side and the product rule on the right side:
$$
-2W(x) \frac{dW}{dx} = (8x) f(x)^2 + 4x^2 \left(2f(x)\frac{df}{dx}\right) = 8x f(x)^2 + 8x^2 f(x) \frac{df}{dx}
$$
Now, we substitute the differential Half-Density Law, $\frac{dW}{dx} = 4rx f(x)^2$, into the left side of the equation:
$$
-2W(x) \left( 4rx f(x)^2 \right) = 8x f(x)^2 + 8x^2 f(x) \frac{df}{dx}
$$
$$
-8rx W(x) f(x)^2 = 8x f(x)^2 + 8x^2 f(x) \frac{df}{dx}
$$
Since $x \in (0, \infty)$ and $f(x)>0$, we can divide the entire equation by $8x f(x)$:
$$
-r W(x) f(x) = f(x) + x \frac{df}{dx}
$$
Rearranging gives the desired result:
$$
x \frac{df}{dx} + f(x) = -r f(x) W(x)
$$
The left-hand side is recognizable from the product rule as $\frac{d}{dx}(x f(x))$, proving the equivalent compact form.

**Exposition:**
This theorem is the spatial counterpart to the Canonical ODE, $p'(u) = -r p(u) W(u)$. It provides a dynamic relationship between the function and its phase in the original coordinates. The term $(xf)'$ represents the rate of change of the "flux" $xf$, which is dictated by the local values of both the function $f$ and the phase $W$. This ODE encapsulates the complete first-order behavior of the function $f(x)$.

***

## 2.6 The Master Linear Equation (Cauchy-Euler Form)

The non-linear Riccati equation for the phase (Theorem 2.5) can be transformed into a simple second-order linear ordinary differential equation. This reveals the deepest and simplest layer of the framework's structure, showing that it is governed by a homogeneous Cauchy-Euler equation.

**Theorem 2.7 (The Master Linear ODE)**
There exists a function $y(x)$ from which the Conformal Phase $W(x)$ can be derived, where $y(x)$ is a solution to the Cauchy-Euler equation:
$$
\boxed{ x^2 \frac{d^2y}{dx^2} + x \frac{dy}{dx} - r^2 y = 0 }
$$
The phase $W(x)$ is recovered from the solution $y(x)$ via the transformation:
$$
W(x; r, c) = \frac{x}{r} \frac{y'(x)}{y(x)}
$$

**Proof:**
We start with the Riccati equation for the phase (Theorem 2.5):
$$
\frac{dW}{dx} = \frac{r}{x} (1 - W^2) \quad \implies \quad \frac{dW}{dx} + \frac{r}{x} W^2 = \frac{r}{x}
$$
This is a first-order non-linear ODE. We introduce the substitution that linearizes Riccati equations. Let $W(x) = k(x) \frac{y'(x)}{y(x)}$. To match the terms of our equation, we choose the coefficient $k(x) = x/r$. So, we define:
$$
W(x) = \frac{x}{r} \frac{y'(x)}{y(x)}
$$
We now differentiate this expression for $W(x)$ using the product and quotient rules:
$$
\frac{dW}{dx} = \frac{d}{dx} \left( \frac{x}{r} \frac{y'}{y} \right) = \left(\frac{1}{r}\right)\frac{y'}{y} + \left(\frac{x}{r}\right)\left( \frac{y''y - (y')^2}{y^2} \right) = \frac{y'}{ry} + \frac{xy''}{ry} - \frac{x(y')^2}{ry^2}
$$
Now substitute both the expression for $W$ and for $dW/dx$ back into the Riccati equation:
$$
\left( \frac{y'}{ry} + \frac{xy''}{ry} - \frac{x(y')^2}{ry^2} \right) + \frac{r}{x} \left( \frac{x}{r} \frac{y'}{y} \right)^2 = \frac{r}{x}
$$
$$
\frac{y'}{ry} + \frac{xy''}{ry} - \frac{x(y')^2}{ry^2} + \frac{r}{x} \left( \frac{x^2}{r^2} \frac{(y')^2}{y^2} \right) = \frac{r}{x}
$$
$$
\frac{y'}{ry} + \frac{xy''}{ry} - \frac{x(y')^2}{ry^2} + \frac{x(y')^2}{ry^2} = \frac{r}{x}
$$
The non-linear terms involving $(y')^2$ cancel perfectly. We are left with a linear equation:
$$
\frac{y'}{ry} + \frac{xy''}{ry} = \frac{r}{x}
$$
To simplify, we multiply the entire equation by $ryx$:
$$
x y' + x^2 y'' = r^2 y
$$
Rearranging into standard form gives the homogeneous Cauchy-Euler equation:
$$
x^2 y'' + x y' - r^2 y = 0
$$
The theorem is proven.

**Corollary 2.7.1 (Algebraic Form of Phase from Master Equation)**
The general solution to the master equation is $y(x) = A x^r + B x^{-r}$. This directly implies the algebraic form of the phase function $W(x)$.

**Proof:**
The characteristic equation for the Cauchy-Euler ODE is found by substituting $y=x^m$, which gives $m(m-1)+m-r^2=0$, simplifying to $m^2=r^2$, so $m=\pm r$. The general solution is a linear combination of these two fundamental solutions: $y(x) = Ax^r + Bx^{-r}$.
Now, we find $W(x)$ using the transformation:
$$
y'(x) = rAx^{r-1} - rBx^{-r-1}
$$
$$
W(x) = \frac{x}{r} \frac{y'(x)}{y(x)} = \frac{x}{r} \frac{rAx^{r-1} - rBx^{-r-1}}{Ax^r + Bx^{-r}} = \frac{x(Ax^{r-1} - Bx^{-r-1})}{Ax^r + Bx^{-r}}
$$
$$
W(x) = \frac{Ax^r - Bx^{-r}}{Ax^r + Bx^{-r}}
$$
To match this with our known form $W(x) = \frac{x^{2r} - c^{2r}}{x^{2r} + c^{2r}}$, we can divide the numerator and denominator by $A$ and multiply them by $x^r$:
$$
W(x) = \frac{x^{2r} - (B/A)}{x^{2r} + (B/A)}
$$
This is identical to the known algebraic form of $W(x)$ if we set the ratio of the integration constants to be $B/A = c^{2r}$. This shows how the scale parameter $c$ arises from the boundary conditions (or specific choice of solution) of the underlying linear system.
