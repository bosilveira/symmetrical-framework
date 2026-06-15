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
