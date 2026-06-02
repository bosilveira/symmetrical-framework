### 3.2 Hypergeometric Representation of the Antiderivative

The antiderivative also has an elegant representation in terms of the classical Gauss hypergeometric function, $_2F_1$. This explicitly places our function family within the broader context of special functions and connects it to a rich analytical theory.

$$
\int f(x;r,c)\ dx = \frac{1}{r}\ \left(\frac{x}{c}\right)^{r}\ _2F_1\left(\frac{1}{2}, 1; \frac{3}{2}; -\left(\frac{x}{c}\right)^{2r}\right) + \text{Constant}
$$

**Derivation:**

The derivation is a direct application of a known series identity that connects the arctangent function to the hypergeometric function.

1.  **Recall the Antiderivative from §3.1.**  
    We begin with the elementary form of the antiderivative:

$$
\int f(x;r,c)\ dx = \frac{1}{r}\ \arctan\left(\left(\frac{x}{c}\right)^r\right) + \text{Constant}
$$

2.  **State the Hypergeometric Identity for Arctangent.**  
    The arctangent function has a standard representation as a specific instance of the Gauss hypergeometric function:

$$
\arctan(z) = z \cdot _2F_1\left(\frac{1}{2}, 1; \frac{3}{2}; -z^2\right)
$$

  This identity is valid for $|z| \le 1$.

3.  **Substitute and Combine.**  
    We apply this identity to the result from Step 1 by setting $z = (x/c)^r$.

$$
\arctan\left(\left(\frac{x}{c}\right)^r\right) = \left(\frac{x}{c}\right)^r \ _2F_1\left(\frac{1}{2}, 1; \frac{3}{2}; -\left(\left(\frac{x}{c}\right)^r\right)^2\right)
$$

$$
= \left(\frac{x}{c}\right)^r \ _2F_1\left(\frac{1}{2}, 1; \frac{3}{2}; -\left(\frac{x}{c}\right)^{2r}\right)
$$

  Substituting this hypergeometric expression back into the antiderivative formula from Step 1 and including the $1/r$ prefactor directly yields the final result.

**Significance:**

This identity serves as a bridge, formally connecting the integral of $f(x;r,c)$ to the vast theory of hypergeometric functions. This is not merely a notational change; it allows the powerful analytical machinery associated with $_2F_1$—including its defining differential equation, integral representations, and transformation formulas—to be applied to the study of this function family.
