# 1.8 The Schwarzian Derivative

The Schwarzian derivative is a non-linear differential operator known for its invariance under Möbius transformations. It plays a significant role in conformal geometry and the theory of integrable systems. For this framework, the Schwarzian derivative of the conformal phase function $W(x)$ evaluates to a simple, exact rational function.

The Schwarzian derivative of a function $g(x)$ is defined as:

$$
\left\lbrace g,x \right\rbrace := \frac{g'''(x)}{g'(x)} - \frac{3}{2}\left(\frac{g''(x)}{g'(x)}\right)^{2}
$$

For the conformal phase function $W(x;r,c)$:

$$
\boxed{\left\lbrace W,x \right\rbrace = \frac{1 - 4r^2}{2x^2}}
$$

### Exposition

This remarkable result serves as a differential "fingerprint" of the framework's conformal geometry. It reveals that the intrinsic curvature associated with the phase function $W(x)$ is purely a power law in $x$ and depends only on the shape parameter $r$. Notably, the result is completely independent of the scale parameter $c$, confirming its status as a pure shape invariant.

### Derivation

The most direct method for computing this derivative is to use the composition rule for the Schwarzian derivative.

**Step 1: Decompose the Function**

We express $W(x)$ as a composition of two functions, $W(x) = (h \circ v)(x)$, where:

*   Outer function: $h(v) = \tanh(v)$
*   Inner function: $v(x) = r\log(x/c)$

**Step 2: State the Composition Rule**

The composition rule for the Schwarzian derivative is:

$$
\left\lbrace W,x \right\rbrace = \left( \left\lbrace h,v \right\rbrace \circ v(x) \right) \cdot (v'(x))^2 + \left\lbrace v,x \right\rbrace
$$

**Step 3: Compute the Component Schwarzian Derivatives**

We compute the necessary components separately.

*   **Schwarzian of the Outer Function ($h$):** The Schwarzian derivative of the hyperbolic tangent is a standard result:

$$
\left\lbrace h, v \right\rbrace = \left\lbrace \tanh v, v \right\rbrace = -2
$$

*   **Schwarzian of the Inner Function ($v$):** For $v(x) = r\log(x/c)$, we first compute its derivatives:

    *   $v'(x) = r/x$
    *   $v''(x) = -r/x^2$
    *   $v'''(x) = 2r/x^3$

Now, substitute these into the definition of the Schwarzian derivative:

$$
\left\lbrace v,x \right\rbrace = \frac{v'''}{v'} - \frac{3}{2}\left(\frac{v''}{v'}\right)^2 = \frac{2r/x^3}{r/x} - \frac{3}{2}\left(\frac{-r/x^2}{r/x}\right)^2
$$

$$
= \frac{2}{x^2} - \frac{3}{2}\left(\frac{-1}{x}\right)^2 = \frac{2}{x^2} - \frac{3}{2x^2} = \frac{1}{2x^2}
$$

**Step 4: Assemble the Final Result**

We substitute the components from Step 3 back into the composition rule from Step 2:

$$
\left\lbrace W,x \right\rbrace = (-2) \cdot \left(\frac{r}{x}\right)^2 + \frac{1}{2x^2}
$$

$$
= \frac{-2r^2}{x^2} + \frac{1}{2x^2}
$$

Combining the terms gives the final result:

$$
\left\lbrace W,x \right\rbrace = \frac{1 - 4r^2}{2x^2}
$$

This completes the derivation.
